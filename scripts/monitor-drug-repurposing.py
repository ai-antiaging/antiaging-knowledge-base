#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
药物再利用文献监控脚本
功能：每月搜索"药物再利用 + 衰老"主题新文献，基于 RPR 框架筛选
"""

import requests
import json
from datetime import datetime
from pathlib import Path

# PubMed API
PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# 输出文件
CONTENT_FILE = Path(__file__).parent.parent / "content" / "drug-repurposing.md"
BRIEFING_FILE = Path(__file__).parent.parent / "data" / "drug_repurposing_briefing.json"


def search_pubmed(query, max_results=10, date_range="1"):
    """
    搜索 PubMed 文献
    
    Args:
        query: 搜索词
        max_results: 最大结果数
        date_range: 日期范围（月数）
    
    Returns:
        list: PMID 列表
    """
    params = {
        "db": "pubmed",
        "term": f"({query}) AND (drug repurposing OR drug repositioning) AND (aging OR longevity OR senescence)",
        "retmax": max_results,
        "sort": "pub+date",
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESEARCH, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"搜索失败：{e}")
        return []


def get_pubmed_details(pmid_list):
    """
    获取 PubMed 文献详细信息
    
    Args:
        pmid_list: PMID 列表
    
    Returns:
        list: 文献详细信息
    """
    if not pmid_list:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(pmid_list),
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESUMMARY, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = data.get("result", {})
        
        papers = []
        for pmid in pmid_list:
            if pmid in results:
                paper = results[pmid]
                papers.append({
                    "pmid": pmid,
                    "title": paper.get("title", ""),
                    "journal": paper.get("fulljournalname", ""),
                    "pubdate": paper.get("pubdate", ""),
                    "doi": paper.get("doi", ""),
                    "authors": paper.get("authors", [])
                })
        return papers
    except Exception as e:
        print(f"获取详情失败：{e}")
        return []


def evaluate_rpr(paper):
    """
    基于 RPR 框架评估文献
    
    Args:
        paper: 文献信息
    
    Returns:
        dict: RPR 评分
    """
    # 简化的评估逻辑（实际应更复杂）
    title_lower = paper.get("title", "").lower()
    
    # 响应性评估
    responsiveness = 5
    if "randomized" in title_lower or "clinical trial" in title_lower:
        responsiveness = 8
    elif "cohort" in title_lower or "observational" in title_lower:
        responsiveness = 6
    
    # 预后性评估
    prognostication = 5
    if "mortality" in title_lower or "survival" in title_lower:
        prognostication = 8
    elif "frailty" in title_lower or "cognitive" in title_lower:
        prognostication = 7
    
    # 可靠性评估
    reliability = 5
    if "meta-analysis" in title_lower or "systematic review" in title_lower:
        reliability = 9
    elif "multicenter" in title_lower:
        reliability = 7
    
    return {
        "responsiveness": responsiveness,
        "prognostication": prognostication,
        "reliability": reliability,
        "total": (responsiveness * 0.4 + prognostication * 0.4 + reliability * 0.2)
    }


def load_last_briefing():
    """
    加载上次简报
    
    Returns:
        dict: 上次简报数据
    """
    if BRIEFING_FILE.exists():
        with open(BRIEFING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"last_check": None, "briefings": []}


def save_briefing(data):
    """
    保存简报数据
    
    Args:
        data: 要保存的数据
    """
    BRIEFING_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(BRIEFING_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def update_content_file(briefing):
    """
    更新内容文件
    
    Args:
        briefing: 简报信息
    """
    if not CONTENT_FILE.exists():
        print(f"内容文件不存在：{CONTENT_FILE}")
        return
    
    content = CONTENT_FILE.read_text(encoding='utf-8')
    
    # 更新最后更新时间
    today = datetime.now().strftime("%Y-%m-%d")
    content = content.replace(
        "**最后更新**：2026-04-18",
        f"**最后更新**：{today}"
    )
    
    # 添加最新简报
    if briefing.get("papers"):
        briefing_text = f"""
#### 最新简报 ({today})

**找到 {len(briefing["papers"])} 篇相关文献**

"""
        for i, paper in enumerate(briefing["papers"][:5], 1):
            rpr = paper.get("rpr", {})
            briefing_text += f"""
**{i}. {paper.get("title", "")}**

- **期刊**: {paper.get("journal", "")}
- **日期**: {paper.get("pubdate", "")}
- **PMID**: [{paper.get("pmid", "")}](https://pubmed.ncbi.nlm.nih.gov/{paper.get("pmid", "")}/)
- **RPR 评分**: 响应性 {rpr.get('responsiveness', 0)}/10 | 预后性 {rpr.get('prognostication', 0)}/10 | 可靠性 {rpr.get('reliability', 0)}/10 | 总分 {rpr.get('total', 0):.1f}/10

"""
        
        # 在"最新简报"部分前添加
        content = content.replace(
            "#### 最新简报\n\n> ⏳ **正在等待首次自动监控**",
            briefing_text
        )
    
    CONTENT_FILE.write_text(content, encoding='utf-8")
    print(f"✅ 已更新内容文件：{CONTENT_FILE}")


def monitor_drug_repurposing():
    """
    主监控函数
    """
    print("=" * 60)
    print("药物再利用文献监控")
    print("=" * 60)
    
    # 搜索文献
    print("正在搜索 PubMed 文献...")
    pmids = search_pubmed("drug repurposing aging", max_results=10)
    print(f"找到 {len(pmids)} 篇文献")
    
    # 获取详细信息
    if pmids:
        papers = get_pubmed_details(pmids)
        print(f"获取 {len(papers)} 篇文献详情")
        
        # RPR 评估
        briefing = {
            "date": datetime.now().isoformat(),
            "papers": []
        }
        
        for paper in papers:
            rpr = evaluate_rpr(paper)
            paper["rpr"] = rpr
            briefing["papers"].append(paper)
            print(f"  - {paper['title'][:50]}... | RPR: {rpr['total']:.1f}")
        
        # 保存简报
        briefing_data = load_last_briefing()
        briefing_data["last_check"] = datetime.now().isoformat()
        briefing_data["briefings"].append(briefing)
        save_briefing(briefing_data)
        
        # 更新内容文件
        update_content_file(briefing)
    else:
        print("未找到相关文献")
    
    print("=" * 60)
    print("监控完成！")
    print("=" * 60)


if __name__ == "__main__":
    monitor_drug_repurposing()
