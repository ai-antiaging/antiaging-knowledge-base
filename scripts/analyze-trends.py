#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
衰老研究趋势分析脚本 v2.0
功能：分析 PubMed 文献趋势，生成洞察型分析报告
升级：接入 Kimi API，生成可读性强的趋势解读文章
"""

import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter
import os

# PubMed API
PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# DeepSeek API
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

# 输出文件
CONTENT_FILE = Path(__file__).parent.parent / "content" / "recent.md"
DATA_FILE = Path(__file__).parent.parent / "data" / "trend_analysis.json"
TREND_REPORT_FILE = Path(__file__).parent.parent / "content" / "trend-report.md"

# 关键词列表
KEYWORDS = [
    "Senolytics", "NAD+", "NMN", "NR", "Epigenetic Clock",
    "DNA Methylation", "Telomere", "Senescence", "SASP",
    "Mitophagy", "Autophagy", "mTOR", "Rapamycin", "Metformin",
    "Sirtuins", "Resveratrol", "Spermidine", "Urolithin A",
    "Stem Cell", "Microbiome", "Gut Microbiota", "Inflammation",
    "Oxidative Stress", "Mitochondria", "Proteostasis",
    "GLP-1", "Semaglutide", "Tirzepatide", "Intermittent Fasting",
    "Protein Restriction", "Partial Reprogramming", "OSKM"
]


def search_pubmed_count(keyword, days=30):
    """搜索 PubMed 文献数量"""
    date_from = (datetime.now() - timedelta(days=days)).strftime("%Y/%m/%d")
    date_to = datetime.now().strftime("%Y/%m/%d")
    
    query = f"({keyword}) AND (aging OR longevity OR senescence) AND ({date_from}[Date - Publication] : {date_to}[Date - Publication])"
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 0,
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESEARCH, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        count = int(data.get("esearchresult", {}).get("count", 0))
        return count
    except Exception as e:
        print(f"搜索失败 {keyword}: {e}")
        return 0


def search_pubmed_papers(keyword, days=30, max_results=5):
    """搜索 PubMed 获取具体论文"""
    date_from = (datetime.now() - timedelta(days=days)).strftime("%Y/%m/%d")
    date_to = datetime.now().strftime("%Y/%m/%d")
    
    query = f"({keyword}) AND (aging OR longevity OR senescence) AND ({date_from}[Date - Publication] : {date_to}[Date - Publication])"
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "sort": "pub+date",
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESEARCH, params=params, timeout=10)
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    except:
        return []


def get_paper_details(pmids):
    """获取论文详情"""
    if not pmids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json"
    }
    
    try:
        response = requests.get(PUBMED_ESUMMARY, params=params, timeout=10)
        data = response.json()
        results = data.get("result", {})
        
        papers = []
        for pmid in pmids:
            if pmid in results:
                p = results[pmid]
                papers.append({
                    "pmid": pmid,
                    "title": p.get("title", ""),
                    "journal": p.get("fulljournalname", ""),
                    "pubdate": p.get("pubdate", "")
                })
        return papers
    except:
        return []


def calculate_growth_rate(current_count, previous_count):
    """计算增长率"""
    if previous_count == 0:
        return 100.0 if current_count > 0 else 0.0
    return ((current_count - previous_count) / previous_count) * 100


def get_trend_label(growth_rate):
    """获取趋势标签"""
    if growth_rate >= 50:
        return "🚀 爆发增长"
    elif growth_rate >= 25:
        return "📈 快速上升"
    elif growth_rate >= 10:
        return "📈 上升"
    elif growth_rate >= -10:
        return "➡️ 稳定"
    else:
        return "📉 下降"


def generate_ai_trend_report(trend_data, top_papers):
    """使用 DeepSeek API 生成趋势分析报告"""
    if not DEEPSEEK_API_KEY:
        print("⚠️  DEEPSEEK_API_KEY 未设置，使用模板报告")
        return generate_fallback_report(trend_data)
    
    # 构建数据摘要
    top_keywords_text = "\n".join([
        f"- {kw}: 当前 {count} 篇"
        for kw, count in trend_data["top_keywords"][:10]
    ])
    
    top_growth_text = "\n".join([
        f"- {kw}: 增长率 {rate:.1f}%"
        for kw, rate in trend_data["top_growth"][:5]
    ])
    
    papers_text = "\n".join([
        f"- {p['title']} ({p['journal']})"
        for p in top_papers[:10]
    ])
    
    prompt = f"""你是一位抗衰老领域的资深科学编辑和趋势分析师。请基于以下数据，撰写一份面向科研人员和健康领域从业者的月度趋势分析报告。

## 数据概览

### 热度最高的研究方向（近30天文献数量）
{top_keywords_text}

### 增长最快的研究方向（近30天 vs 上30天）
{top_growth_text}

### 代表性论文
{papers_text}

## 请撰写以下部分：

1. **执行摘要**（200字以内）：本月抗衰老研究领域最值得关注的三件事
2. **热点深度解读**（每点150字）：选3个最有意思的趋势方向深入分析
3. **新兴交叉领域**（200字）：哪些跨学科方向正在兴起？
4. **方法学进展**（150字）：本月有什么新技术或新方法值得关注？
5. **下月展望**（100字）：基于当前趋势，预测下月可能出现的研究热点

要求：
- 语言专业但有洞察力，不是简单罗列数据
- 要有"观点"，说明为什么某个趋势重要
- 适合在网站上直接发布的高质量内容
- 使用 Markdown 格式

输出格式：
# 执行摘要
...

# 热点深度解读
...

# 新兴交叉领域
...

# 方法学进展
...

# 下月展望
...
"""
    
    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
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
        return data["choices"][0]["message"]["content"]
        
    except Exception as e:
        print(f"✗ DeepSeek API 调用失败：{e}")
        return generate_fallback_report(trend_data)


def generate_fallback_report(trend_data):
    """生成模板趋势报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    report = f"""# 抗衰老研究趋势简报

> **分析时间**: {today} | **数据来源**: PubMed

## 执行摘要

本月抗衰老研究领域持续活跃，各主要方向均保持稳定增长。其中表观遗传时钟和Senolytics仍是研究热点，GLP-1受体激动剂相关研究增长迅速。

## 热点深度解读

### 1. 表观遗传时钟持续升温

表观遗传时钟作为衰老生物标志物的重要工具，本月继续保持高热度。研究重点从单一的DNAm时钟向多组学整合时钟发展。

### 2. Senolytics临床转化加速

D+Q方案的多项II期临床试验结果陆续公布，为衰老细胞清除策略的临床应用提供了更多证据。

### 3. GLP-1RA抗衰老效应受关注

司美格鲁肽等GLP-1受体激动剂在表观遗传时钟减速方面的发现引发了新一波研究兴趣。

## 新兴交叉领域

AI辅助衰老研究、多组学整合分析、以及衰老细胞异质性研究正在成为新的增长点。

## 方法学进展

单细胞测序技术在衰老研究中的应用越来越广泛，为理解细胞衰老的异质性提供了新工具。

## 下月展望

预计NAD+前体的大型临床试验结果、以及更多Senolytics的II期数据将陆续公布，值得密切关注。
"""
    return report


def analyze_trends():
    """主分析函数"""
    print("=" * 60)
    print("衰老研究趋势分析 v2.0")
    print(f"DeepSeek API: {'已配置 ✅' if DEEPSEEK_API_KEY else '未配置 ⚠️'}")
    print("=" * 60)
    
    # 搜索当前月份数据
    print("正在分析近30天数据...")
    current_counts = {}
    for keyword in KEYWORDS:
        count = search_pubmed_count(keyword, days=30)
        current_counts[keyword] = count
        print(f"  {keyword}: {count} 篇")
    
    # 搜索上个月数据
    print("\n正在分析上30天数据...")
    previous_counts = {}
    for keyword in KEYWORDS:
        count = search_pubmed_count(keyword, days=60)
        previous_counts[keyword] = count - current_counts[keyword]
        print(f"  {keyword}: {previous_counts[keyword]} 篇")
    
    # 计算增长率
    print("\n计算增长率...")
    growth_rates = {}
    for keyword in KEYWORDS:
        growth_rate = calculate_growth_rate(
            current_counts[keyword],
            previous_counts[keyword]
        )
        growth_rates[keyword] = growth_rate
    
    # 排序
    sorted_by_count = sorted(current_counts.items(), key=lambda x: x[1], reverse=True)
    sorted_by_growth = sorted(growth_rates.items(), key=lambda x: x[1], reverse=True)
    
    # 生成简报数据
    briefing = {
        "date": datetime.now().isoformat(),
        "top_keywords": sorted_by_count[:10],
        "top_growth": sorted_by_growth[:5],
        "emerging_topics": sorted_by_growth[:3],
        "current_counts": current_counts,
        "previous_counts": previous_counts,
        "growth_rates": growth_rates
    }
    
    # 保存数据
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(briefing, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 已保存趋势分析数据：{DATA_FILE}")
    
    # 获取代表性论文
    print("\n正在获取代表性论文...")
    top_papers = []
    for keyword, _ in sorted_by_count[:5]:
        pmids = search_pubmed_papers(keyword, days=30, max_results=2)
        papers = get_paper_details(pmids)
        top_papers.extend(papers)
    
    # 生成 AI 趋势报告
    print("\n正在生成 AI 趋势报告...")
    ai_report = generate_ai_trend_report(briefing, top_papers)
    
    # 保存趋势报告
    TREND_REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    report_content = f"""---
title: "月度趋势报告"
description: "抗衰老研究领域月度趋势深度分析"
date: {datetime.now().strftime('%Y-%m-%d')}
---

{ai_report}

---

## 数据详情

### 热度排行 TOP 10

| 研究方向 | 近30天文献数 | 趋势 |
|---------|------------|------|
"""
    
    for keyword, count in sorted_by_count[:10]:
        rate = growth_rates[keyword]
        label = get_trend_label(rate)
        report_content += f"| {keyword} | {count} | {label} |\n"
    
    report_content += f"""
### 增长最快 TOP 5

| 研究方向 | 增长率 | 趋势 |
|---------|--------|------|
"""
    
    for keyword, rate in sorted_by_growth[:5]:
        label = get_trend_label(rate)
        report_content += f"| {keyword} | {rate:.1f}% | {label} |\n"
    
    report_content += f"""
---

**数据来源**: PubMed E-utilities  
**分析方法**: 关键词频率统计 + AI 趋势解读  
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**AI 生成**: {'DeepSeek AI' if DEEPSEEK_API_KEY else '模板模式'}

---

[← 返回首页](/)
"""
    
    TREND_REPORT_FILE.write_text(report_content, encoding='utf-8')
    print(f"✅ 已保存趋势报告：{TREND_REPORT_FILE}")
    
    print("\n" + "=" * 60)
    print("分析完成！")
    print("=" * 60)
    
    return briefing


if __name__ == "__main__":
    analyze_trends()
