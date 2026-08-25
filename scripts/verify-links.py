#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PubMed 链接验证脚本
功能：验证 Markdown 文件中的 PubMed 链接是否有效
"""

import re
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

CONTENT_DIR = Path(__file__).parent.parent / "content"


def extract_pubmed_links(markdown_content):
    """从 Markdown 内容中提取 PubMed 链接"""
    pattern = r'https://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/'
    return re.findall(pattern, markdown_content)


def verify_pubmed_link(pmid):
    """验证 PubMed 链接是否有效"""
    url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return {
            "pmid": pmid,
            "valid": response.status_code in (200, 203),
            "status_code": response.status_code,
            "url": url
        }
    except Exception as e:
        return {
            "pmid": pmid,
            "valid": False,
            "error": str(e),
            "url": url
        }


def verify_all_files():
    """验证所有内容文件的 PubMed 链接"""
    print("=" * 60)
    print("PubMed 链接验证")
    print("=" * 60)
    
    all_links = set()
    
    # 提取所有 PubMed 链接
    for md_file in CONTENT_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        links = extract_pubmed_links(content)
        all_links.update(links)
        print(f"✓ {md_file.name}: {len(links)} 个 PubMed 链接")
    
    print(f"\n共发现 {len(all_links)} 个唯一的 PubMed 链接")
    print("\n正在验证链接有效性...")
    
    # 并发验证链接
    valid_count = 0
    invalid_links = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(verify_pubmed_link, pmid): pmid for pmid in all_links}
        
        for future in as_completed(futures):
            result = future.result()
            if result.get("valid"):
                valid_count += 1
            else:
                invalid_links.append(result)
                print(f"✗ PMID {result['pmid']}: {result.get('error', result.get('status_code', 'Unknown'))}")
    
    print("\n" + "=" * 60)
    print(f"验证完成：{valid_count}/{len(all_links)} 有效 ({valid_count/len(all_links)*100:.1f}%)")
    
    if invalid_links:
        print(f"\n⚠️  发现 {len(invalid_links)} 个无效链接:")
        for link in invalid_links[:10]:  # 只显示前 10 个
            print(f"  - PMID {link['pmid']}: {link.get('error', link.get('status_code', 'Unknown'))}")
    
    print("=" * 60)
    
    return valid_count == len(all_links)


if __name__ == "__main__":
    success = verify_all_files()
    exit(0 if success else 1)
