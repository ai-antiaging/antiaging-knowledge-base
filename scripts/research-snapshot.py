#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
研究快照生成器
功能：将抗衰老领域重要研究转化为社交媒体风格的简短图文卡片
"""

import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
import os

PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

DS_API_KEY = os.environ.get("DS_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

CONTENT_DIR = Path(__file__).parent.parent / "content" / "news" / "snapshots"
DATA_DIR = Path(__file__).parent.parent / "data"

KEYWORDS = [
    "aging", "longevity", "senescence", "NAD+", "senolytics",
    "epigenetic clock", "mitophagy", "autophagy", "mTOR",
    "sirtuins", "stem cell", "inflammaging", "telomere"
]

HIGH_IF_JOURNALS = [
    "Nature", "Science", "Cell", "Cell Metabolism", "Nature Metabolism",
    "Nature Aging", "Aging Cell", "Science Translational Medicine", "Nature Medicine"
]


def search_pubmed(keywords, days=None, max_results=10):
    """搜索 PubMed 文献"""
    if days is None:
        days = int(os.environ.get("LOOKBACK_DAYS", "1"))
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
                })
        return papers
    except Exception as e:
        print(f"获取 PubMed 详情失败：{e}")
        return []


def generate_snapshot_card(paper):
    """生成社交媒体风格的研究快照"""
    if not DS_API_KEY:
        print("⚠️  DS_API_KEY 未设置，使用模板")
        return generate_fallback_card(paper)
    
    title = paper.get("title", "")
    journal = paper.get("journal", "")
    
    prompt = f"""你是一位抗衰老领域的科普博主。请将以下论文转化为一条社交媒体风格的研究快照（类似 Twitter/X 上的科普推文）。

论文标题：{title}
期刊：{journal}

要求：
1. 用 2-3 句话概括核心发现
2. 语言活泼但不失专业，适合社交媒体传播
3. 包含一个引人注目的 emoji 开头
4. 末尾加上 #抗衰老 #长寿科学 等标签
5. 总字数控制在 120-180 字（中文）
6. 格式：一句话吸引眼球的开头 + 核心发现 + 意义/展望

请直接输出最终文案，不要加任何说明。
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
                "temperature": 0.6,
                "max_tokens": 400
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"].strip()
        return content
        
    except Exception as e:
        print(f"  ✗ DeepSeek API 调用失败：{e}")
        return generate_fallback_card(paper)


def generate_fallback_card(paper):
    """模板模式快照"""
    title = paper.get("title", "")
    journal = paper.get("journal", "")
    
    return f"""🔬 新研究速递

{title[:80]}{'...' if len(title) > 80 else ''}

发表于 {journal}，为抗衰老领域带来新见解。

#抗衰老 #长寿科学 #{journal.replace(' ', '')}
"""


def generate_hashtags(paper):
    """生成标签"""
    tags = ["#抗衰老", "#长寿科学"]
    
    title_lower = paper.get("title", "").lower()
    if "senescence" in title_lower or "senolytic" in title_lower:
        tags.append("#细胞衰老")
    if "nad" in title_lower:
        tags.append("#NAD")
    if "epigenetic" in title_lower or "clock" in title_lower:
        tags.append("#表观遗传")
    if "stem" in title_lower:
        tags.append("#干细胞")
    if "mitochondria" in title_lower:
        tags.append("#线粒体")
    if "autophagy" in title_lower or "mitophagy" in title_lower:
        tags.append("#自噬")
    
    return " ".join(tags)


def save_snapshot(paper, card_content):
    """保存研究快照"""
    output_date = os.environ.get("OUTPUT_DATE", "")
    if output_date:
        today = output_date
    else:
        today = datetime.now().strftime("%Y-%m-%d")
    
    # 创建目录（支持每天多篇）
    dir_path = CONTENT_DIR / today
    dir_path.mkdir(parents=True, exist_ok=True)
    
    # 计算文件序号
    existing = list(dir_path.glob("*.md"))
    seq = len(existing) + 1
    filename = f"snapshot-{seq:02d}.md"
    
    hashtags = generate_hashtags(paper)
    
    content = f"""---
title: "研究快照 · {today} #{seq}"
date: {today}
description: "{paper['title'][:80]}..."
draft: false
type: "snapshot"
---

# 📸 研究快照 · {today}

> **{paper['journal']}** · 社交媒体风格速览

---

{card_content}

---

**原文**: [{paper['title'][:60]}...](https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/)

**PMID**: [{paper['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/)

{hashtags}

---

*自动生成 · 适合社交媒体分享*  
*生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}*

 [← 返回快照列表](../)
"""
    
    filepath = dir_path / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已保存快照：{filepath}")
    return filepath


def update_index(today):
    """更新快照索引"""
    index_file = CONTENT_DIR / "_index.md"
    
    if not index_file.exists():
        index_content = f"""---
title: "研究快照"
description: "社交媒体风格的研究速览卡片"
---

# 📸 研究快照

> **社交媒体风格** · 快速传播核心发现

---

## 最新快照

"""
    else:
        index_content = index_file.read_text(encoding='utf-8')
    
    marker = "## 最新快照\n\n"
    new_entry = f"- [{today}](/news/snapshots/{today}/)\n"
    
    if marker in index_content and new_entry not in index_content:
        index_content = index_content.replace(marker, marker + new_entry)
        index_file.write_text(index_content, encoding='utf-8')
        print("✅ 已更新索引页")


def run_snapshot_task():
    """执行研究快照任务"""
    lookback = os.environ.get("LOOKBACK_DAYS", "1")
    print("=" * 60)
    print("研究快照生成器")
    print(f"DeepSeek API: {'已配置 ✅' if DS_API_KEY else '未配置 ⚠️'}")
    print(f"回溯天数: {lookback}")
    print("=" * 60)
    
    # 搜索文献
    print("正在搜索 PubMed 文献...")
    pmids = search_pubmed(KEYWORDS, days=int(lookback), max_results=5)
    print(f"找到 {len(pmids)} 篇文献")
    
    if not pmids:
        print("⚠️  未找到文献，跳过今日更新")
        return
    
    # 获取详细信息
    print("正在获取文献详情...")
    papers = get_pubmed_details(pmids)
    
    # 生成快照
    today = datetime.now().strftime("%Y-%m-%d")
    generated = 0
    
    for i, paper in enumerate(papers[:3], 1):  # 每天最多3篇
        print(f"\n正在生成快照 {i}/{min(len(papers), 3)}...")
        print(f"  论文: {paper['title'][:60]}...")
        
        card = generate_snapshot_card(paper)
        save_snapshot(paper, card)
        generated += 1
    
    if generated > 0:
        update_index(today)
    
    print("=" * 60)
    print(f"研究快照任务完成！生成 {generated} 篇")
    print("=" * 60)


if __name__ == "__main__":
    run_snapshot_task()
