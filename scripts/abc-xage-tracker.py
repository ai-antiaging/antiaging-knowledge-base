#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABC / X-Age 追踪器
功能：追踪中国衰老标志物研究联合体（ABC/X-Age）核心成员的最新论文发表
"""

import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
import os

PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

CONTENT_DIR = Path(__file__).parent.parent / "content" / "news" / "abc-updates"
DATA_DIR = Path(__file__).parent.parent / "data"

# ABC/X-Age 核心成员（作者名用于 PubMed 搜索）
ABC_AUTHORS = [
    "Qu J",      # 曲静
    "Zhang W",   # 张维绮
    "Liu GH",    # 刘光慧
    "Sun S",     # 孙淑慧
    "Wang S",    # 王斯瑶
]

AGING_KEYWORDS = [
    "aging", "longevity", "senescence", "epigenetic clock",
    "stem cell", "regeneration", "rejuvenation"
]


def search_author_papers(author, days=7):
    """搜索特定作者的近期论文"""
    date_from = (datetime.now() - timedelta(days=days)).strftime("%Y/%m/%d")
    date_to = datetime.now().strftime("%Y/%m/%d")
    
    # 搜索该作者 AND 衰老相关关键词
    query = f"{author}[Author] AND ({' OR '.join(AGING_KEYWORDS)}) AND ({date_from}[Date - Publication] : {date_to}[Date - Publication])"
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 50,
        "sort": "pub+date",
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESEARCH, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        pmids = data.get("esearchresult", {}).get("idlist", [])
        return pmids
    except Exception as e:
        print(f"搜索作者 {author} 失败：{e}")
        return []


def get_pubmed_details(pmid_list):
    """获取 PubMed 文献详细信息"""
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
                papers.append({
                    "pmid": pmid,
                    "title": paper.get("title", ""),
                    "journal": paper.get("fulljournalname", ""),
                    "pubdate": paper.get("pubdate", ""),
                    "doi": paper.get("doi", ""),
                    "authors": paper.get("authors", []),
                })
        return papers
    except Exception as e:
        print(f"获取 PubMed 详情失败：{e}")
        return []


def format_paper_row(paper, author_tag):
    """格式化论文为 Markdown 表格行"""
    authors = paper.get("authors", [])
    author_names = [a.get("name", "") if isinstance(a, dict) else str(a) for a in authors[:3]]
    author_str = ", ".join(author_names)
    if len(authors) > 3:
        author_str += " 等"
    
    return f"""### {paper['title']}

| 项目 | 详情 |
|------|------|
| 作者 | {author_str} |
| 期刊 | {paper['journal']} |
| 日期 | {paper['pubdate']} |
| PMID | [{paper['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/) |
| DOI | [{paper.get('doi', 'N/A')}](https://doi.org/{paper.get('doi', '')}) |
| 关联 | {author_tag} |

"""


def generate_abc_report(papers_by_author):
    """生成 ABC 追踪报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 统计
    total_papers = sum(len(papers) for papers in papers_by_author.values())
    
    content = f"""---
title: "ABC / X-Age 追踪报告 · {today}"
date: {today}
description: "中国衰老标志物研究联合体最新动态追踪"
draft: false
type: "abc-update"
---

# ABC / X-Age 追踪报告 · {today}

> **中国衰老标志物研究联合体** · 核心成员最新论文动态

---

## 📋 检查概要

- **检查时间**: {today}
- **追踪成员**: {', '.join(ABC_AUTHORS)}
- **新增论文**: {total_papers} 篇
- **检查周期**: 过去 7 天

---

"""
    
    if total_papers == 0:
        content += """## 🔍 本周动态

本周未检索到 ABC/X-Age 核心成员在衰老领域的新发表论文。

> 注：可能的原因包括：
> - 本周确实无新发表
> - 论文尚未被 PubMed 收录
> - 作者署名使用了变体拼写

"""
    else:
        content += "## 🔬 新增论文\n\n"
        
        for author, papers in papers_by_author.items():
            if not papers:
                continue
            
            # 确定作者中文名
            author_cn = {
                "Qu J": "曲静",
                "Zhang W": "张维绮",
                "Liu GH": "刘光慧",
                "Sun S": "孙淑慧",
                "Wang S": "王斯瑶",
            }.get(author, author)
            
            content += f"### {author_cn} ({author})\n\n"
            
            for paper in papers:
                # 判断论文类型
                title_lower = paper['title'].lower()
                if any(k in title_lower for k in ["aging", "senescence", "longevity", "epigenetic", "rejuvenation"]):
                    tag = "🧬 衰老核心研究"
                else:
                    tag = "🔬 合作网络产出"
                
                content += format_paper_row(paper, tag)
    
    content += f"""
---

## 📊 追踪统计

| 成员 | 本周新增 | 追踪状态 |
|------|---------|---------|
"""
    
    for author in ABC_AUTHORS:
        author_cn = {
            "Qu J": "曲静",
            "Zhang W": "张维绮", 
            "Liu GH": "刘光慧",
            "Sun S": "孙淑慧",
            "Wang S": "王斯瑶",
        }.get(author, author)
        count = len(papers_by_author.get(author, []))
        status = "✅ 有更新" if count > 0 else "⏳ 无更新"
        content += f"| {author_cn} ({author}) | {count} | {status} |\n"
    
    content += f"""
---

## 🔗 相关资源

- [ABC 官网](https://agingchina.org/)
- [X-Age 追踪页面](/news/abc-updates/)
- [PubMed 作者搜索: Qu J](https://pubmed.ncbi.nlm.nih.gov/?term=Qu+J%5BAuthor%5D&sort=date)

---

*自动生成 · 数据来源: PubMed · 更新频率: 每周*  
*最后更新: {datetime.now().strftime("%Y-%m-%d %H:%M")}*

 [← 返回 AI 新闻官专栏](/news/)
"""
    
    return content


def save_report(content):
    """保存报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}.md"
    
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = CONTENT_DIR / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已保存 ABC 追踪报告：{filepath}")
    return filepath


def update_index(new_file):
    """更新索引"""
    index_file = CONTENT_DIR / "_index.md"
    
    if not index_file.exists():
        # 创建初始索引
        index_content = f"""---
title: "ABC 与 X-Age 追踪"
description: "中国衰老标志物研究联合体最新动态"
---

# ABC 与 X-Age 追踪

> **中国衰老标志物研究联合体** · 核心成员论文动态自动追踪

---

## 最新报告

"""
    else:
        index_content = index_file.read_text(encoding='utf-8')
    
    # 在 "## 最新报告" 后插入
    marker = "## 最新报告\n\n"
    today = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"- [{today}](/news/abc-updates/{today}/)\n"
    
    if marker in index_content and new_entry not in index_content:
        index_content = index_content.replace(marker, marker + new_entry)
        index_file.write_text(index_content, encoding='utf-8')
        print("✅ 已更新索引页")


def run_abc_tracker():
    """执行 ABC 追踪任务"""
    print("=" * 60)
    print("ABC / X-Age 追踪器")
    print("=" * 60)
    
    all_papers = {}
    
    for author in ABC_AUTHORS:
        print(f"正在搜索 {author} 的近期论文...")
        pmids = search_author_papers(author, days=7)
        papers = get_pubmed_details(pmids)
        all_papers[author] = papers
        print(f"  找到 {len(papers)} 篇")
    
    # 生成报告
    print("正在生成追踪报告...")
    report = generate_abc_report(all_papers)
    filepath = save_report(report)
    
    # 更新索引
    update_index(filepath)
    
    print("=" * 60)
    print("ABC 追踪任务完成！")
    print("=" * 60)


if __name__ == "__main__":
    run_abc_tracker()
