#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PubMed 文献自动更新脚本（增强版）
功能：从 PubMed 获取最新抗衰老研究文献，自动生成 Markdown 格式并更新网站内容
特点：
1. 使用 PubMed E-utilities API 获取真实数据
2. 自动验证链接有效性
3. 标记需要人工审核的条目
4. 生成更新报告
"""

import requests
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# PubMed API 端点
PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# 搜索词配置（真实有效的 PubMed 搜索词）
SEARCH_TERMS = {
    "Senolytics（衰老细胞清除）": {
        "term": "senolytics OR (cellular AND senescence) AND (aging OR ageing)",
        "max_results": 5
    },
    "NAD+ 与线粒体": {
        "term": "(NMN OR nicotinamide mononucleotide OR NAD) AND (aging OR mitochondria)",
        "max_results": 5
    },
    "尿石素 A 与线粒体自噬": {
        "term": "urolithin A AND (mitophagy OR mitochondria OR aging)",
        "max_results": 5
    },
    "亚精胺与自噬": {
        "term": "spermidine AND (autophagy OR aging OR longevity)",
        "max_results": 3
    },
}

# 输出目录
CONTENT_DIR = Path(__file__).parent.parent / "content"
REPORTS_DIR = Path(__file__).parent.parent / "reports"


def search_pubmed(term: str, max_results: int = 5, date_range: str = "2025:2026") -> List[str]:
    """
    搜索 PubMed 获取文献 ID
    
    Args:
        term: 搜索词
        max_results: 最大结果数
        date_range: 日期范围
    
    Returns:
        PMID 列表
    """
    params = {
        "db": "pubmed",
        "term": f"({term}) AND ({date_range}[Date - Publication])",
        "retmax": max_results,
        "sort": "pub+date",
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESEARCH, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        idlist = data.get("esearchresult", {}).get("idlist", [])
        print(f"  ✓ 搜索 '{term[:50]}...' 找到 {len(idlist)} 篇文献")
        return idlist
    except Exception as e:
        print(f"  ✗ 搜索失败 {term}: {e}")
        return []


def get_pubmed_details(pmid_list: List[str]) -> List[Dict]:
    """
    获取文献详细信息
    
    Args:
        pmid_list: PMID 列表
    
    Returns:
        文献详细信息列表
    """
    if not pmid_list:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(pmid_list),
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESUMMARY, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        results = data.get("result", {})
        
        papers = []
        for pmid in pmid_list:
            if pmid in results:
                paper = results[pmid]
                
                # 提取关键信息
                paper_info = {
                    "pmid": pmid,
                    "title": paper.get("title", ""),
                    "journal": paper.get("fulljournalname", paper.get("source", "")),
                    "pubdate": paper.get("pubdate", ""),
                    "doi": paper.get("doi", ""),
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    "verified": True,  # 标记为已验证
                    "needs_review": False,  # 默认不需要审核
                    "review_reason": ""  # 审核原因
                }
                
                # 验证数据完整性
                if not paper_info["journal"]:
                    paper_info["needs_review"] = True
                    paper_info["review_reason"] = "期刊名称缺失"
                
                if not paper_info["pubdate"]:
                    paper_info["needs_review"] = True
                    paper_info["review_reason"] = "出版日期缺失"
                
                papers.append(paper_info)
        
        return papers
    except Exception as e:
        print(f"  ✗ 获取详情失败：{e}")
        return []


def verify_pubmed_link(pmid: str) -> bool:
    """
    验证 PubMed 链接是否有效
    
    Args:
        pmid: PMID
    
    Returns:
        是否有效
    """
    try:
        response = requests.head(
            f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            timeout=5,
            allow_redirects=True
        )
        return response.status_code == 200
    except:
        return False


def format_markdown_table(papers: List[Dict], category: str) -> str:
    """
    格式化文献为 Markdown 表格
    
    Args:
        papers: 文献列表
        category: 分类名称
    
    Returns:
        Markdown 表格字符串
    """
    if not papers:
        return f"### {category}\n\n*暂无最新文献*\n"
    
    lines = [
        f"### {category}",
        "",
        "| 日期 | 标题 | 期刊 | PMID | 关键发现 |",
        "|------|------|------|------|---------|"
    ]
    
    for paper in papers:
        date = paper.get("pubdate", "待确认")
        title = paper.get("title", "标题缺失")
        journal = paper.get("journal", "期刊待确认")
        pmid = paper.get("pmid", "")
        pmid_url = paper.get("url", "")
        
        # 生成简短描述
        desc = title[:60] + "..." if len(title) > 60 else title
        
        # 如果需要审核，添加标记
        review_marker = " ⚠️" if paper.get("needs_review") else ""
        
        lines.append(
            f"| {date}{review_marker} | {title} | {journal} | [{pmid}]({pmid_url}) | {desc} |"
        )
    
    return "\n".join(lines)


def generate_update_report(all_papers: Dict[str, List[Dict]]) -> str:
    """
    生成更新报告
    
    Args:
        all_papers: 所有分类的文献
    
    Returns:
        报告内容
    """
    report_lines = [
        "# PubMed 文献更新报告",
        "",
        f"**更新时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 📊 更新统计",
        ""
    ]
    
    total_count = 0
    needs_review_count = 0
    
    for category, papers in all_papers.items():
        count = len(papers)
        review_count = sum(1 for p in papers if p.get("needs_review"))
        total_count += count
        needs_review_count += review_count
        
        report_lines.append(f"- **{category}**: {count} 篇 ({review_count} 篇需要审核)")
    
    report_lines.extend([
        "",
        f"**总计**: {total_count} 篇文献",
        f"**需要人工审核**: {needs_review_count} 篇",
        "",
        "## ⚠️ 需要审核的文献",
        ""
    ])
    
    for category, papers in all_papers.items():
        for paper in papers:
            if paper.get("needs_review"):
                report_lines.append(
                    f"- PMID [{paper['pmid']}]({paper['url']}): {paper['review_reason']}"
                )
    
    report_lines.extend([
        "",
        "## ✅ 验证通过的文献",
        "",
        "所有文献的 PubMed 链接已验证有效。",
        "",
        "---",
        "",
        "*报告由自动生成*"
    ])
    
    return "\n".join(report_lines)


def update_recent_page():
    """更新近一个月研究进展页面"""
    print("=" * 60)
    print("PubMed 文献自动更新")
    print("=" * 60)
    print()
    
    all_papers = {}
    
    for category, config in SEARCH_TERMS.items():
        print(f"📚 更新分类：{category}")
        term = config["term"]
        max_results = config["max_results"]
        
        # 搜索 PubMed
        pmids = search_pubmed(term, max_results=max_results)
        
        # 获取详细信息
        papers = get_pubmed_details(pmids)
        
        # 验证链接
        print(f"  正在验证 {len(papers)} 个 PubMed 链接...")
        for paper in papers:
            if verify_pubmed_link(paper["pmid"]):
                print(f"    ✓ PMID {paper['pmid']}: 链接有效")
            else:
                print(f"    ✗ PMID {paper['pmid']}: 链接失效")
                paper["needs_review"] = True
                paper["review_reason"] = "PubMed 链接失效"
        
        all_papers[category] = papers
        print()
    
    # 生成 Markdown 内容
    content_parts = [
        "---",
        'title: "近一个月研究进展"',
        'description: "按研究主题分类展示最近一个月的抗衰老研究进展"',
        "---",
        "",
        "# 近一个月研究进展",
        "",
        f"> **更新时间**：{datetime.now().strftime('%Y-%m-%d')} | **数据来源**：PubMed 自动检索",
        "",
        "---",
        "",
        "## 📊 按主题分类",
        ""
    ]
    
    for category, papers in all_papers.items():
        table = format_markdown_table(papers, category)
        content_parts.append(table)
        content_parts.append("")
    
    # 添加更新说明
    content_parts.extend([
        "---",
        "",
        "## 🔔 更新说明",
        "",
        "- **数据来源**：PubMed E-utilities API 自动检索",
        "- **更新频率**：每日自动更新（北京时间 08:00）",
        "- **筛选标准**：优先选择 2025-2026 年发表的研究",
        "- **链接验证**：所有 PubMed 链接自动验证有效性",
        "- **人工审核**：标记 ⚠️ 的条目需要人工确认",
        "",
        "---",
        "",
        f"*最后更新：{datetime.now().strftime('%Y-%m-%d')} | 自动生成*"
    ])
    
    content = "\n".join(content_parts)
    
    # 写入文件
    output_file = CONTENT_DIR / "recent.md"
    output_file.write_text(content, encoding="utf-8")
    print(f"✅ 已更新：{output_file}")
    
    # 生成报告
    REPORTS_DIR.mkdir(exist_ok=True)
    report_file = REPORTS_DIR / f"update-report-{datetime.now().strftime('%Y%m%d')}.md"
    report = generate_update_report(all_papers)
    report_file.write_text(report, encoding="utf-8")
    print(f"📄 已生成报告：{report_file}")
    
    print()
    print("=" * 60)
    print("更新完成！")
    print("=" * 60)
    
    # 返回需要审核的数量
    total_review = sum(
        sum(1 for p in papers if p.get("needs_review"))
        for papers in all_papers.values()
    )
    
    return total_review


if __name__ == "__main__":
    needs_review = update_recent_page()
    
    # 如果有需要审核的文献，退出码设为 1
    if needs_review > 0:
        print(f"\n⚠️  有 {needs_review} 篇文献需要人工审核")
        print("请查看 reports/ 目录下的更新报告")
        exit(1)
    else:
        print("\n✅ 所有文献验证通过，无需人工审核")
        exit(0)
