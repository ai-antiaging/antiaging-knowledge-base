# 文献人工审核指南

> 当自动更新标记 ⚠️ 时，需要人工审核

---

## 📋 审核流程

### 1. 查看更新报告

自动更新后，会在 `reports/` 目录生成报告：

```
reports/
└── update-report-20260418.md
```

报告中会列出：
- 总更新文献数量
- 需要审核的文献列表
- 审核原因（期刊缺失、链接失效等）

### 2. 验证 PubMed 链接

对于需要审核的文献：

1. **点击 PMID 链接**
   - 打开 PubMed 页面
   - 确认文献存在

2. **核对信息**
   - 标题是否匹配
   - 期刊名称是否正确
   - 出版日期是否准确

3. **修正错误**
   - 如信息有误，编辑 `content/recent.md`
   - 更新正确的期刊名称或日期
   - 移除 ⚠️ 标记

### 3. 提交审核结果

审核完成后：

```bash
git add content/recent.md
git commit -m "docs: 人工审核并修正文献信息"
git push
```

---

## 🔍 常见问题

### 问题 1：期刊名称显示为"期刊待确认"

**原因**：PubMed API 返回的数据中期刊字段为空

**解决**：
1. 访问 PubMed 链接
2. 复制期刊名称
3. 手动更新 Markdown 文件

### 问题 2：PubMed 链接失效（404）

**原因**：
- PMID 错误
- 文献刚收录，页面未完全生成
- 罕见的 PMID 格式变更

**解决**：
1. 在 PubMed 首页搜索 PMID
2. 如找到文献，更新正确链接
3. 如确实不存在，移除该条目

### 问题 3：出版日期缺失

**原因**：在线发表（Epub ahead of print）的文献可能没有完整日期

**解决**：
1. 访问 PubMed 页面
2. 查看 "Publication date" 字段
3. 手动补充日期

---

## 📝 手动更新模板

如需手动添加文献，使用以下格式：

```markdown
| 日期 | 标题 | 期刊 | PMID | 关键发现 |
|------|------|------|------|---------|
| 2026-03-11 | Effects of NMN Supplementation on Blood Pressure | Nutrients | [41901064](https://pubmed.ncbi.nlm.nih.gov/41901064/) | NMN 补充与舒张压降低相关 |
```

**必填字段**：
- ✅ 日期：YYYY-MM-DD 格式
- ✅ 标题：英文原文
- ✅ 期刊：完整期刊名
- ✅ PMID：有效的 PubMed ID
- ✅ 关键发现：50-100 字中文总结

---

## 🎯 质量标准

### 优秀条目示例

```markdown
| 2026-03-11 | Effects of NMN Supplementation on Blood Pressure: Systematic Review | Nutrients | [41901064](https://pubmed.ncbi.nlm.nih.gov/41901064/) | Meta 分析显示 NMN 降低舒张压 -2.15 mmHg |
```

✅ 日期准确  
✅ 标题完整  
✅ 期刊名称正确  
✅ PMID 链接有效  
✅ 关键发现简洁明了

### 需要修正的条目

```markdown
| 待确认 ⚠️ | 某研究标题 | 期刊待确认 | [12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/) | 待补充 |
```

❌ 日期缺失  
❌ 期刊名称缺失  
❌ 关键发现过于简单

---

## 📞 需要帮助？

如遇到无法确定的问题：

1. **查看 PubMed 帮助**：https://pubmed.ncbi.nlm.nih.gov/help/
2. **创建 Issue**：在 GitHub 仓库创建 Issue 讨论
3. **查阅更新报告**：`reports/` 目录下的详细报告

---

*最后更新：2026-04-18*
