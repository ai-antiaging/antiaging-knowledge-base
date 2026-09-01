#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
周深度解读生成器
功能：每周自动生成一篇重要抗衰老研究的深度解读
"""

import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
import os
import re

PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

DS_API_KEY = os.environ.get("DS_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

CONTENT_DIR = Path(__file__).parent.parent / "content" / "news" / "deep-dive"
DATA_DIR = Path(__file__).parent.parent / "data"

KEYWORDS = [
    "aging", "longevity", "senescence", "NAD+", "senolytics",
    "epigenetic clock", "mitophagy", "autophagy", "mTOR",
    "sirtuins", "stem cell", "inflammaging", "telomere"
]

HIGH_IF_JOURNALS = [
    "Nature", "Science", "Cell", "Cell Metabolism", "Nature Metabolism",
    "Nature Aging", "Aging Cell", "Science Translational Medicine", "Nature Medicine",
    "Lancet", "JAMA", "NEJM", "Cell Research", "Nature Communications",
    "Circulation", "Circulation Research", "JCI", "Geroscience"
]


def search_pubmed(keywords, days=7, max_results=20):
    """搜索 PubMed 文献"""
    date_from = (datetime.now() - timedelta(days=days)).strftime("%Y/%m/%d")
    date_to = datetime.now().strftime("%Y/%m/%d")
    
    search_terms = " OR ".join(keywords)
    query = f"({search_terms}) AND ({date_from}[Date - Publication] : {date_to}[Date - Publication])"
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results * 2,
        "sort": "pub+date",
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESEARCH, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        pmids = data.get("esearchresult", {}).get("idlist", [])
        return pmids[:max_results]
    except Exception as e:
        print(f"PubMed 搜索失败：{e}")
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
                    "abstract": ""
                })
        return papers
    except Exception as e:
        print(f"获取 PubMed 详情失败：{e}")
        return []


def get_abstracts(pmid_list):
    """通过 efetch 获取摘要"""
    if not pmid_list:
        return {}
    
    params = {
        "db": "pubmed",
        "id": ",".join(pmid_list),
        "retmode": "xml"
    }
    
    try:
        response = requests.get(PUBMED_EFETCH, params=params, timeout=15)
        response.raise_for_status()
        content = response.text
        abstracts = {}
        
        import xml.etree.ElementTree as ET
        root = ET.fromstring(content)
        
        for article in root.findall('.//PubmedArticle'):
            pmid_elem = article.find('.//PMID')
            if pmid_elem is not None:
                pmid = pmid_elem.text
                abstract_elem = article.find('.//Abstract/AbstractText')
                if abstract_elem is not None and abstract_elem.text:
                    abstracts[pmid] = abstract_elem.text
                else:
                    abstracts[pmid] = ""
        
        return abstracts
    except Exception as e:
        print(f"获取摘要失败：{e}")
        return {}


def score_paper(paper):
    """给论文打分，选出最适合深度解读的"""
    score = 0
    journal = paper.get("journal", "").lower()
    
    # 高影响力期刊加分
    for hj in HIGH_IF_JOURNALS:
        if hj.lower() in journal:
            score += 10
    
    # 有 DOI 加分
    if paper.get("doi"):
        score += 2
    
    # 有摘要加分
    if paper.get("abstract"):
        score += 3
    
    return score


def select_best_paper(papers):
    """选择最适合深度解读的论文"""
    if not papers:
        return None
    
    scored = [(p, score_paper(p)) for p in papers]
    scored.sort(key=lambda x: x[1], reverse=True)
    
    return scored[0][0]


def generate_deep_dive(paper):
    """使用 DeepSeek API 生成深度解读"""
    if not DS_API_KEY:
        print("⚠️  DS_API_KEY 未设置")
        return None
    
    title = paper.get("title", "")
    abstract = paper.get("abstract", "")
    journal = paper.get("journal", "")
    
    if not abstract:
        print(f"  ⚠️  PMID {paper['pmid']} 无摘要，跳过")
        return None
    
    prompt = f"""你是一位抗衰老领域的资深科学编辑。请基于以下论文信息，撰写一篇面向科研人员和健康领域从业者的周深度解读文章。

论文标题：{title}
期刊：{journal}
PMID：{paper['pmid']}
DOI：{paper.get('doi', 'N/A')}
摘要：{abstract}

请用中文撰写，结构如下（总计 400-600 字，每个部分简洁有力）：

## 研究背景
为什么这项研究重要？它解决了领域中的什么关键问题？（80-120 字）

## 核心问题
研究要解决的具体科学问题是什么？（50-80 字）

## 方法与数据
使用了什么方法、技术、样本量？（80-120 字）

## 关键发现
主要发现是什么？有什么关键数据？（100-150 字）

## 局限性
研究有哪些限制？（50-80 字）

## 领域意义
对衰老研究或临床实践有什么影响？（80-120 字）

要求：
- 语言专业但不晦涩，适合有生物学背景的非领域专家
- 避免过度解读，严格基于摘要内容
- 使用 Markdown 格式
- 适当使用 emoji 增强可读性
"""
    
    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers={
                "Authorization": f"Bearer {DS_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.4,
                "max_tokens": 2000
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]
        return content
        
    except Exception as e:
        print(f"  ✗ DeepSeek API 调用失败：{e}")
        return None


def save_deep_dive(paper, content):
    """保存深度解读"""
    today = datetime.now().strftime("%Y-%m-%d")
    week_str = f"{today}-weekly"
    
    # 创建目录
    dir_path = CONTENT_DIR / week_str
    dir_path.mkdir(parents=True, exist_ok=True)
    
    # 生成 front matter
    front_matter = f"""---
title: "周深度解读 · {today}"
date: {today}
description: "{paper['title'][:100]}..."
draft: false
type: "deep-dive"
---

# 📚 周深度解读 · {today}

> **{paper['journal']}** · PMID: [{paper['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/)

---

**论文标题**: {paper['title']}

**期刊**: {paper['journal']}

**发表日期**: {paper['pubdate']}

**DOI**: [{paper.get('doi', 'N/A')}](https://doi.org/{paper.get('doi', '')})

---

"""
    
    full_content = front_matter + content + f"""

---

*自动生成 · 最后更新：{datetime.now().strftime("%Y-%m-%d %H:%M")}*

 [← 返回周深度解读列表](../)
"""
    
    filepath = dir_path / "index.md"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"✅ 已保存深度解读：{filepath}")
    return week_str


def update_index(new_entry):
    """更新深度解读索引"""
    index_file = CONTENT_DIR / "_index.md"
    
    # 读取现有内容
    if index_file.exists():
        content = index_file.read_text(encoding='utf-8')
    else:
        content = ""
    
    # 在 "## 最新解读" 后插入新条目
    new_line = f'- **[{new_entry["title"]}](./{new_entry["slug"]}/)** — {new_entry["date"]}\n  - *{new_entry["journal"]}* · {new_entry["summary"]}\n'
    
    # 简单地在 "## 最新解读" 后插入
    marker = "## 最新解读\n\n"
    if marker in content:
        content = content.replace(marker, marker + new_line + "\n")
    
    index_file.write_text(content, encoding='utf-8')
    print(f"✅ 已更新索引页")


def run_weekly_task():
    """执行每周深度解读任务"""
    print("=" * 60)
    print("周深度解读生成器")
    print(f"DeepSeek API: {'已配置 ✅' if DS_API_KEY else '未配置 ⚠️'}")
    print("=" * 60)
    
    # 搜索最近一周的文献
    print("正在搜索 PubMed 文献...")
    pmids = search_pubmed(KEYWORDS, days=7, max_results=20)
    print(f"找到 {len(pmids)} 篇文献")
    
    if not pmids:
        print("⚠️  未找到文献，跳过本周更新")
        return
    
    # 获取详细信息
    print("正在获取文献详情...")
    papers = get_pubmed_details(pmids)
    
    # 获取摘要
    print("正在获取摘要...")
    abstracts = get_abstracts(pmids)
    for paper in papers:
        paper["abstract"] = abstracts.get(paper["pmid"], "")
    
    # 选择最佳论文
    print("正在选择最佳论文...")
    best_paper = select_best_paper(papers)
    
    if not best_paper:
        print("⚠️  无法选择合适的论文")
        return
    
    print(f"选中论文: {best_paper['title'][:80]}...")
    print(f"期刊: {best_paper['journal']}")
    
    # 生成深度解读
    print("正在生成深度解读...")
    dive_content = generate_deep_dive(best_paper)
    
    if not dive_content:
        print("✗ 生成失败")
        return
    
    # 保存
    week_slug = save_deep_dive(best_paper, dive_content)
    
    # 更新索引
    new_entry = {
        "title": best_paper['title'],
        "slug": week_slug,
        "date": datetime.now().strftime("%Y年%m月%d日"),
        "journal": best_paper['journal'],
        "summary": f"PMID: {best_paper['pmid']}"
    }
    update_index(new_entry)
    
    print("=" * 60)
    print("周深度解读任务完成！")
    print("=" * 60)


if __name__ == "__main__":
    run_weekly_task()
