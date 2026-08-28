#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 新闻官 v2.1
功能：每日自动发布抗衰老领域前沿研究解读
升级：接入 DeepSeek API，生成有洞察力的研究摘要
"""

import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
import os

# API 端点
PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# DeepSeek API
DS_API_KEY = os.environ.get("DS_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

# 输出目录
CONTENT_DIR = Path(__file__).parent.parent / "content"
DATA_DIR = Path(__file__).parent.parent / "data"
NEWS_DIR = CONTENT_DIR / "news"

# 高影响力期刊列表
HIGH_IF_JOURNALS = [
    "Nature", "Science", "Cell", "Cell Metabolism", "Nature Metabolism",
    "Nature Aging", "Aging Cell", "Science Translational Medicine", "Nature Medicine",
    "Lancet", "JAMA", "NEJM", "Cell Research", "Nature Communications",
    "Aging", "GeroScience", "Mechanisms of Ageing and Development"
]

# 核心关键词
KEYWORDS = [
    "aging", "longevity", "senescence", "NAD+", "senolytics",
    "epigenetic clock", "mitophagy", "autophagy", "mTOR",
    "sirtuins", "spermidine", "urolithin A", "stem cell",
    "inflammaging", "telomere", "DNA methylation"
]


def search_pubmed(keywords, days=1, max_results=15):
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
    """获取 PubMed 文献详细信息（含摘要）"""
    if not pmid_list:
        return []
    
    # 获取详细信息
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
                    "abstract": ""  # 稍后通过 efetch 获取
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
        # 简化的 XML 解析 - 提取摘要文本
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


def filter_high_impact_papers(papers):
    """筛选高影响力论文"""
    high_impact = []
    regular = []
    
    for paper in papers:
        journal = paper.get("journal", "").lower()
        is_high_impact = any(
            hj.lower() in journal for hj in HIGH_IF_JOURNALS
        )
        if is_high_impact:
            high_impact.append(paper)
        else:
            regular.append(paper)
    
    # 优先高影响力，补充普通论文
    result = high_impact[:5]
    remaining_slots = 5 - len(result)
    if remaining_slots > 0:
        result.extend(regular[:remaining_slots])
    
    return result


def generate_ai_summary(paper):
    """使用 DeepSeek API 生成研究摘要"""
    if not DS_API_KEY:
        print("⚠️  DS_API_KEY 未设置，使用模板摘要")
        return generate_fallback_summary(paper)
    
    title = paper.get("title", "")
    abstract = paper.get("abstract", "")
    journal = paper.get("journal", "")
    
    if not abstract:
        print(f"  ⚠️  PMID {paper['pmid']} 无摘要，使用模板")
        return generate_fallback_summary(paper)
    
    prompt = f"""你是一位抗衰老领域的资深科学编辑。请基于以下论文信息，生成一份面向科研人员和健康领域从业者的研究简报。

论文标题：{title}
期刊：{journal}
摘要：{abstract}

请用中文生成以下四个部分（每个部分2-3句话，简洁有力）：

1. **研究亮点**：这项研究最核心的发现是什么？为什么重要？
2. **关键发现**：具体实验结果或数据是什么？
3. **方法创新**：研究采用了什么新技术或新方法？
4. **临床意义**：这项发现对未来抗衰老干预或临床实践有什么启示？

要求：
- 语言专业但不晦涩，适合有生物学背景的非领域专家阅读
- 避免过度解读，严格基于摘要内容
- 每个部分控制在 100 字以内
- 使用 Markdown 格式输出

输出格式：
研究亮点：...
关键发现：...
方法创新：...
临床意义：...
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
                "temperature": 0.3,
                "max_tokens": 800
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]
        
        # 解析返回的内容
        return parse_ai_response(content, paper)
        
    except Exception as e:
        print(f"  ✗ DeepSeek API 调用失败：{e}")
        return generate_fallback_summary(paper)


def parse_ai_response(content, paper):
    """解析 Kimi API 返回的内容"""
    summary = {
        "highlights": "",
        "findings": "",
        "methods": "",
        "clinical_relevance": ""
    }
    
    lines = content.split('\n')
    current_key = None
    
    for line in lines:
        line = line.strip()
        if line.startswith('研究亮点'):
            current_key = "highlights"
            summary["highlights"] = line.split('：', 1)[1].strip() if '：' in line else ""
        elif line.startswith('关键发现'):
            current_key = "findings"
            summary["findings"] = line.split('：', 1)[1].strip() if '：' in line else ""
        elif line.startswith('方法创新'):
            current_key = "methods"
            summary["methods"] = line.split('：', 1)[1].strip() if '：' in line else ""
        elif line.startswith('临床意义'):
            current_key = "clinical_relevance"
            summary["clinical_relevance"] = line.split('：', 1)[1].strip() if '：' in line else ""
        elif current_key and line and not line.startswith('#'):
            summary[current_key] += " " + line
    
    # 清理
    for key in summary:
        summary[key] = summary[key].strip()
        if not summary[key]:
            summary[key] = "详见原文"
    
    return summary


def generate_fallback_summary(paper):
    """生成模板摘要（API 不可用时 fallback）"""
    journal = paper.get("journal", "知名期刊")
    title = paper.get("title", "")
    
    return {
        "highlights": f"本研究发表于 {journal}，聚焦抗衰老领域前沿问题。",
        "findings": f"研究探索了 {title[:80]}... 的相关机制。",
        "methods": "采用分子生物学、细胞实验或临床队列研究方法。",
        "clinical_relevance": "研究成果为理解衰老机制和开发抗衰老干预策略提供新见解。"
    }


def generate_daily_digest(papers):
    """生成每日快讯"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    content = f"""---
title: "每日快讯 · {today}"
date: {today}
description: "抗衰老领域最新研究进展速递"
draft: false
type: "daily-digest"
---

# 📰 每日快讯 · {today}

> **AI 生成摘要** · 过去 24 小时高影响力研究 · PubMed 精选

---

"""
    
    for i, paper in enumerate(papers, 1):
        # 生成 AI 摘要
        print(f"  正在生成研究 {i} 的 AI 摘要...")
        summary = generate_ai_summary(paper)
        
        # 作者信息
        authors = paper.get("authors", [])
        author_str = ""
        if authors:
            first_author = authors[0].get("name", "") if isinstance(authors[0], dict) else str(authors[0])
            author_str = f"**第一作者**: {first_author} 等 | "
        
        content += f"""## 研究 {i}: {paper['title']}

**期刊**: {paper['journal']}  
**发表日期**: {paper['pubdate']}  
{author_str}**PMID**: [{paper['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/)  
**DOI**: [{paper.get('doi', 'N/A')}](https://doi.org/{paper.get('doi', '')})

### 🌟 研究亮点

{summary['highlights']}

### 🔬 关键发现

{summary['findings']}

### 🧪 方法简介

{summary['methods']}

### 🏥 临床相关性

{summary['clinical_relevance']}

---

"""
    
    content += f"""
**数据来源**: PubMed E-utilities  
**筛选标准**: 高影响力期刊优先 · 过去 24 小时 · 衰老相关研究  
**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**摘要生成**: {'DeepSeek AI' if DS_API_KEY else '模板模式（DeepSeek API 未配置）'}

---

[← 返回首页](/) | [查看更多快讯](/news/)
"""
    
    return content


def save_daily_digest(content):
    """保存每日快讯"""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"daily-digest-{today}.md"
    
    NEWS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = NEWS_DIR / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已保存每日快讯：{filepath}")
    return filepath


def update_news_index():
    """更新 news 索引页"""
    index_file = NEWS_DIR / "_index.md"
    
    # 获取所有快讯文件
    digest_files = sorted(NEWS_DIR.glob("daily-digest-*.md"), reverse=True)
    
    content = """---
title: "AI 新闻官"
description: "每日自动生成的抗衰老研究快讯"
---

# 📰 AI 新闻官

> **自动化专栏** · 每日 08:00 更新 · 精选高影响力抗衰老研究

---

## 最新快讯

"""
    
    for digest_file in digest_files[:30]:  # 显示最近30篇
        date_str = digest_file.stem.replace("daily-digest-", "")
        content += f"- [{date_str}](/news/{digest_file.stem}/)\n"
    
    content += """
---

## 关于 AI 新闻官

AI 新闻官每日自动：
1. 搜索 PubMed 最新抗衰老文献
2. 筛选高影响力期刊论文
3. 使用 AI 生成中文研究摘要
4. 自动发布到本网站

**数据源**: PubMed | **更新频率**: 每日 08:00 (UTC+8)

---

*自动生成 · 最后更新：""" + datetime.now().strftime("%Y-%m-%d") + "*\n"
    
    index_file.write_text(content, encoding='utf-8')
    print(f"✅ 已更新索引页：{index_file}")


def run_daily_task():
    """执行每日任务"""
    print("=" * 60)
    print("AI 新闻官 v2.1 - 每日任务")
    print(f"DeepSeek API: {'已配置 ✅' if DS_API_KEY else '未配置 ⚠️（将使用模板摘要）'}")
    print("=" * 60)
    
    # 搜索 PubMed
    print("正在搜索 PubMed 文献...")
    pmids = search_pubmed(KEYWORDS, days=1, max_results=15)
    print(f"找到 {len(pmids)} 篇文献")
    
    if not pmids:
        print("⚠️  未找到文献，跳过今日更新")
        return
    
    # 获取详细信息
    print("正在获取文献详情...")
    papers = get_pubmed_details(pmids)
    
    # 获取摘要
    print("正在获取摘要...")
    abstracts = get_abstracts(pmids)
    for paper in papers:
        paper["abstract"] = abstracts.get(paper["pmid"], "")
    
    # 筛选高影响力论文
    print("正在筛选高影响力论文...")
    selected_papers = filter_high_impact_papers(papers)
    print(f"精选 {len(selected_papers)} 篇论文")
    
    # 生成每日快讯
    print("正在生成每日快讯...")
    digest_content = generate_daily_digest(selected_papers)
    save_daily_digest(digest_content)
    
    # 更新索引
    update_news_index()
    
    print("=" * 60)
    print("每日任务完成！")
    print("=" * 60)


if __name__ == "__main__":
    run_daily_task()
