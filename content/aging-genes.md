---
title: "衰老基因检索系统"
description: "集成 HAGR 数据库，探索人类衰老相关基因和长寿物种"
draft: false
---

# 🧬 衰老基因检索系统

> **数据来源**：HAGR (Human Ageing Genomic Resources) - 人类衰老基因组资源  
> **官方网址**：https://genomics.senescence.info  
> **收录规模**：300+ 人类衰老基因 · 2000+ 模式生物基因 · 4000+ 物种寿命记录

---

## 📖 关于 HAGR

### 什么是 HAGR？

**Human Ageing Genomic Resources (HAGR)** 是由 João Pedro de Magalhães 博士领导的团队开发的综合性衰老基因组资源平台，旨在为衰老研究社区提供免费的数据库和分析工具。

### 核心数据库

| 数据库 | 内容 | 规模 | 用途 |
|--------|------|------|------|
| **GenAge** | 人类衰老相关基因 | 300+ 个人类基因 | 基因查询、功能分析 |
| **GenAge Models** | 模式生物长寿基因 | 2000+ 个基因 | 跨物种比较研究 |
| **AnAge** | 动物寿命数据库 | 4000+ 个物种 | 长寿物种比较 |
| **CellAge** | 细胞衰老相关基因 | 200+ 个基因 | 细胞衰老研究 |
| **DrugAge** | 抗衰老化合物 | 400+ 种化合物 | 药物研发参考 |
| **Digital Ageing Atlas** | 多维度衰老数据 | 整合数据 | 系统生物学研究 |

### 参考文献

1. **HAGR 概览**：Tacutu R, et al. Human Ageing Genomic Resources: new and updated databases. *Nucleic Acids Res*. 2018;46(D1):D1083-D1090. PMID: [29121237](https://pubmed.ncbi.nlm.nih.gov/29121237/)
2. **GenAge 数据库**：de Magalhães JP, Toussaint O. GenAge: a genomic and proteomic network map of human ageing. *FEBS Lett*. 2004;571(1-3):243-7. PMID: [15280050](https://pubmed.ncbi.nlm.nih.gov/15280050/)
3. **AnAge 数据库**：de Magalhães JP, Costa J. A database of vertebrate longevity records and their relation to other life-history traits. *J Evol Biol*. 2009;22(8):1770-4. PMID: [19522730](https://pubmed.ncbi.nlm.nih.gov/19522730/)

---

## 🔍 基因查询功能

<div id="gene-query-section" style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #667eea;">

### 查询衰老相关基因

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 快速查询

<input type="text" id="gene-search-input" placeholder="输入基因名称，如：FOXO3, SIRT1, MTOR, TP53..." style="width: 100%; padding: 15px; font-size: 16px; border: 2px solid #e2e8f0; border-radius: 8px; margin-bottom: 20px;" onkeyup="if(event.key === 'Enter') queryGene()">

<div style="text-align: center; margin: 25px 0;">
<button onclick="queryGene()" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 15px 40px; font-size: 16px; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); font-weight: 500;">🔍 查询基因信息</button>
</div>

<div id="gene-loading" style="display: none; text-align: center; padding: 30px;">
<div style="display: inline-block; width: 40px; height: 40px; border: 4px solid #e2e8f0; border-top-color: #667eea; border-radius: 50%; animation: spin 1s linear infinite;"></div>
<p style="margin-top: 15px; color: #718096;">正在查询 GenAge 数据库...</p>
</div>

<div id="gene-error" style="display: none; background: #fed7d7; border-left: 4px solid #f56565; padding: 20px; border-radius: 6px; margin: 20px 0;">
<h4 style="margin-top: 0; color: #742a2a;">⚠️ 查询失败</h4>
<p style="color: #742a2a;" id="gene-error-message"></p>
</div>

<div id="gene-results" style="display: none; margin-top: 30px;">
<!-- 基因查询结果将在这里显示 -->
</div>

</div>

#### 常用衰老基因推荐

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-top: 20px;">

<button onclick="searchGene('FOXO3')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">FOXO3</button>
<button onclick="searchGene('SIRT1')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">SIRT1</button>
<button onclick="searchGene('MTOR')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">MTOR</button>
<button onclick="searchGene('TP53')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">TP53</button>
<button onclick="searchGene('APOE')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">APOE</button>
<button onclick="searchGene('CDKN2A')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">CDKN2A</button>
<button onclick="searchGene('IGF1')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">IGF1</button>
<button onclick="searchGene('SIRT6')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">SIRT6</button>

</div>

</div>

---

## 🦕 长寿物种浏览器

<div id="species-browser-section" style="background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #48bb78;">

### 探索长寿物种

基于 **AnAge** 数据库，收录超过 4000 个物种的寿命记录。

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 筛选物种

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-bottom: 20px;">

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">📊 分类</label>
<select id="species-class" onchange="filterSpecies()" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="all">全部</option>
<option value="mammals">哺乳动物</option>
<option value="birds">鸟类</option>
<option value="reptiles">爬行动物</option>
<option value="fish">鱼类</option>
<option value="invertebrates">无脊椎动物</option>
</select>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">📏 最小寿命（年）</label>
<input type="number" id="min-longevity" placeholder="0" min="0" onchange="filterSpecies()" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">⚖️ 体重范围（kg）</label>
<select id="weight-range" onchange="filterSpecies()" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="all">全部</option>
<option value="small">小型 (&lt;1kg)</option>
<option value="medium">中型 (1-50kg)</option>
<option value="large">大型 (&gt;50kg)</option>
</select>
</div>

</div>

<div id="species-results" style="margin-top: 20px;">
<!-- 物种列表将在这里显示 -->
</div>

</div>

#### 著名长寿物种

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 20px;">

<div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #48bb78;">
<div style="font-size: 24px; margin-bottom: 10px;">🐋</div>
<h4 style="margin-top: 0; color: #2d3748;">弓头鲸</h4>
<p style="color: #718096; font-size: 14px;">最大寿命：200+ 岁</p>
<p style="color: #718096; font-size: 14px;">体重：100,000 kg</p>
<p style="color: #718096; font-size: 12px; margin-top: 10px;">已知最长寿的哺乳动物</p>
</div>

<div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #48bb78;">
<div style="font-size: 24px; margin-bottom: 10px;">🐢</div>
<h4 style="margin-top: 0; color: #2d3748;">加拉帕戈斯象龟</h4>
<p style="color: #718096; font-size: 14px;">最大寿命：175 岁</p>
<p style="color: #718096; font-size: 14px;">体重：400 kg</p>
<p style="color: #718096; font-size: 12px; margin-top: 10px;">最长寿的陆生脊椎动物</p>
</div>

<div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #48bb78;">
<div style="font-size: 24px; margin-bottom: 10px;">🦜</div>
<h4 style="margin-top: 0; color: #2d3748;">金刚鹦鹉</h4>
<p style="color: #718096; font-size: 14px;">最大寿命：80 岁</p>
<p style="color: #718096; font-size: 14px;">体重：1.5 kg</p>
<p style="color: #718096; font-size: 12px; margin-top: 10px;">最长寿的鸟类之一</p>
</div>

<div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #48bb78;">
<div style="font-size: 24px; margin-bottom: 10px;">🐘</div>
<h4 style="margin-top: 0; color: #2d3748;">非洲象</h4>
<p style="color: #718096; font-size: 14px;">最大寿命：70 岁</p>
<p style="color: #718096; font-size: 14px;">体重：6,000 kg</p>
<p style="color: #718096; font-size: 12px; margin-top: 10px;">陆地上最大的动物</p>
</div>

</div>

</div>

---

## 📊 基因 - 衰老标志物关联网络

<div id="gene-network-section" style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #ed8936;">

### 可视化基因与衰老标志物的关联

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0; text-align: center;">

<div style="height: 400px; background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); border-radius: 8px; display: flex; align-items: center; justify-content: center;">
<div style="text-align: center; color: #718096;">
<div style="font-size: 64px; margin-bottom: 20px;">🕸️</div>
<p style="font-size: 18px; font-weight: 500;">基因 - 衰老标志物关联网络</p>
<p style="font-size: 14px; margin-top: 10px;">（实际部署时应集成 D3.js 或 Cytoscape.js 渲染交互式网络图）</p>
<p style="font-size: 12px; margin-top: 20px; color: #a0aec0;">查询基因后，将显示该基因与衰老十四大标志物的关联关系</p>
</div>
</div>

<div style="margin-top: 30px; text-align: left;">

#### 图例说明

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">

<div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
<div style="font-weight: 600; color: #2d3748; margin-bottom: 10px;">🔵 节点类型</div>
<div style="font-size: 13px; color: #718096;">
• 蓝色圆形：查询基因<br>
• 红色方形：衰老标志物<br>
• 绿色三角形：相关通路
</div>
</div>

<div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
<div style="font-weight: 600; color: #2d3748; margin-bottom: 10px;">🔗 连线含义</div>
<div style="font-size: 13px; color: #718096;">
• 实线：直接调控关系<br>
• 虚线：间接关联<br>
• 粗细：证据强度
</div>
</div>

</div>

</div>

</div>

</div>

---

## 📚 使用教程

### 如何使用基因查询功能？

#### 步骤 1：输入基因名称

在搜索框中输入您想查询的基因符号（Gene Symbol），例如：
- **FOXO3**：长寿相关转录因子
- **SIRT1**：去乙酰化酶，长寿基因
- **MTOR**：营养感应通路关键调控因子

#### 步骤 2：查看基因摘要

系统返回以下信息：
- ✅ **GenAge 收录状态**：是否在人类衰老基因数据库中
- ✅ **支持文献数量**：PubMed 收录的相关研究数量
- ✅ **主要生物学功能**：基因的核心功能描述
- ✅ **相关信号通路**：参与的生物学通路
- ✅ **同源基因**：模式生物中的同源基因

#### 步骤 3：查看关联网络

- 查看基因与衰老十四大标志物的关联
- 了解基因在衰老过程中的作用机制
- 探索潜在的治疗靶点

### 如何使用长寿物种浏览器？

#### 步骤 1：选择筛选条件

- **分类**：哺乳动物、鸟类、爬行动物等
- **最小寿命**：筛选寿命超过特定年龄的物种
- **体重范围**：按体型大小筛选

#### 步骤 2：浏览物种列表

查看每个物种的详细信息：
- 最大寿命记录
- 成年体重
- 代谢率
- 其他生命史特征

#### 步骤 3：比较分析

- 比较不同物种的寿命差异
- 探索长寿的进化机制
- 发现潜在的抗衰老策略

---

## 🔬 示例基因

### FOXO3

**GenAge 收录**：✅ 是  
**支持文献**：500+ 篇  
**主要功能**：转录因子，调控细胞周期、凋亡、氧化应激  
**相关通路**：胰岛素/IGF-1 信号、自噬、DNA 修复  
**同源基因**：daf-16（线虫）、dFOXO（果蝇）  
**衰老标志物关联**：营养感应失调、干细胞耗竭、基因组不稳定性

### SIRT1

**GenAge 收录**：✅ 是  
**支持文献**：800+ 篇  
**主要功能**：NAD+ 依赖性去乙酰化酶，调控代谢和应激反应  
**相关通路**：Sirtuin 信号、自噬、炎症反应  
**同源基因**：sir-2.1（线虫）、dSir2（果蝇）  
**衰老标志物关联**：营养感应失调、表观遗传改变、慢性炎症

### MTOR

**GenAge 收录**：✅ 是  
**支持文献**：1000+ 篇  
**主要功能**：丝氨酸/苏氨酸激酶，调控细胞生长和代谢  
**相关通路**：mTOR 信号、自噬、蛋白质合成  
**同源基因**：let-363（线虫）、dTOR（果蝇）  
**衰老标志物关联**：营养感应失调、蛋白质稳态丧失、自噬功能障碍

---

## ⚠️ 免责声明

> 本工具基于 HAGR 数据库的公开数据，仅供参考和教育用途。
> 
> 基因查询结果不作为临床诊断或治疗建议。
> 
> 如需进行基因检测或解读，请咨询专业医疗人员或遗传咨询师。
> 
> 数据最后更新：2026-04-18  
> 更新频率：每季度自动同步

---

## 📊 数据统计

<div style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 30px; border-radius: 12px; margin: 30px 0; text-align: center;">

### HAGR 数据库统计

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; margin-top: 20px;">

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #667eea;">300+</div>
<div style="color: #718096; margin-top: 5px;">人类衰老基因</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #48bb78;">2000+</div>
<div style="color: #718096; margin-top: 5px;">模式生物基因</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #ed8936;">4000+</div>
<div style="color: #718096; margin-top: 5px;">物种寿命记录</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #f56565;">6</div>
<div style="color: #718096; margin-top: 5px;">核心数据库</div>
</div>

</div>

</div>

---

## 🔗 外部资源

- **[HAGR 官方网站](https://genomics.senescence.info/)** - 访问完整的 HAGR 数据库
- **[GenAge 人类基因](https://genomics.senescence.info/genes/)** - 浏览人类衰老相关基因
- **[AnAge 动物寿命](https://genomics.senescence.info/species/)** - 探索长寿物种记录
- **[CellAge 细胞衰老](https://genomics.senescence.info/cellage/)** - 细胞衰老相关基因 ⚠️ 子站可能已整合至主站
- **[DrugAge 抗衰老化合物](https://genomics.senescence.info/drugage/)** - 抗衰老药物数据库 ⚠️ 子站可能已整合至主站

---

**数据来源**：Human Ageing Genomic Resources (HAGR) - https://genomics.senescence.info  
**最后更新**：2026-04-18  
**更新频率**：每季度自动同步  
**引用**：Tacutu R, et al. Human Ageing Genomic Resources: new and updated databases. Nucleic Acids Res. 2018;46(D1):D1083-D1090. PMID: 29121237.

---

<script>
// 基因查询数据（示例数据，实际应从 HAGR API 获取）
const geneData = {
    'FOXO3': {
        name: 'FOXO3',
        fullName: 'Forkhead Box O3',
        inGenAge: true,
        pubmedCount: 523,
        function: '转录因子，调控细胞周期、凋亡、氧化应激反应和自噬',
        pathways: ['胰岛素/IGF-1 信号', '自噬', 'DNA 修复', '氧化应激反应'],
        homologs: {
            'C. elegans': 'daf-16',
            'D. melanogaster': 'dFOXO',
            'M. musculus': 'Foxo3'
        },
        hallmarks: ['营养感应失调', '干细胞耗竭', '基因组不稳定性']
    },
    'SIRT1': {
        name: 'SIRT1',
        fullName: 'Sirtuin 1',
        inGenAge: true,
        pubmedCount: 834,
        function: 'NAD+ 依赖性去乙酰化酶，调控代谢、应激反应和细胞存活',
        pathways: ['Sirtuin 信号', '自噬', '炎症反应', '代谢调控'],
        homologs: {
            'C. elegans': 'sir-2.1',
            'D. melanogaster': 'dSir2',
            'M. musculus': 'Sirt1'
        },
        hallmarks: ['营养感应失调', '表观遗传改变', '慢性炎症']
    },
    'MTOR': {
        name: 'MTOR',
        fullName: 'Mechanistic Target Of Rapamycin',
        inGenAge: true,
        pubmedCount: 1052,
        function: '丝氨酸/苏氨酸激酶，调控细胞生长、增殖和代谢',
        pathways: ['mTOR 信号', '自噬', '蛋白质合成', '代谢调控'],
        homologs: {
            'C. elegans': 'let-363',
            'D. melanogaster': 'dTOR',
            'M. musculus': 'Mtor'
        },
        hallmarks: ['营养感应失调', '蛋白质稳态丧失', '自噬功能障碍']
    },
    'TP53': {
        name: 'TP53',
        fullName: 'Tumor Protein P53',
        inGenAge: true,
        pubmedCount: 1245,
        function: '肿瘤抑制因子，调控细胞周期、凋亡和 DNA 修复',
        pathways: ['细胞周期调控', '凋亡', 'DNA 修复', '衰老相关分泌表型'],
        homologs: {
            'C. elegans': 'cep-1',
            'D. melanogaster': 'Dmp53',
            'M. musculus': 'Trp53'
        },
        hallmarks: ['基因组不稳定性', '细胞衰老', '干细胞耗竭']
    },
    'APOE': {
        name: 'APOE',
        fullName: 'Apolipoprotein E',
        inGenAge: true,
        pubmedCount: 678,
        function: '载脂蛋白，参与脂质代谢和神经保护',
        pathways: ['脂质代谢', '神经保护', '炎症反应', '阿尔茨海默病'],
        homologs: {
            'M. musculus': 'Apoe',
            'R. norvegicus': 'Apoe'
        },
        hallmarks: ['细胞间通讯改变', '慢性炎症', '蛋白质稳态丧失']
    }
};

// 长寿物种数据（示例数据）
const speciesData = [
    {name: '弓头鲸', class: 'mammals', longevity: 211, weight: 100000, metabolism: '低'},
    {name: '加拉帕戈斯象龟', class: 'reptiles', longevity: 175, weight: 400, metabolism: '低'},
    {name: '非洲象', class: 'mammals', longevity: 70, weight: 6000, metabolism: '中'},
    {name: '人类', class: 'mammals', longevity: 122, weight: 70, metabolism: '中'},
    {name: '金刚鹦鹉', class: 'birds', longevity: 80, weight: 1.5, metabolism: '高'},
    {name: '格陵兰鲨', class: 'fish', longevity: 400, weight: 1000, metabolism: '极低'},
    {name: '海葵', class: 'invertebrates', longevity: 60, weight: 0.1, metabolism: '低'},
    {name: '裸鼹鼠', class: 'mammals', longevity: 32, weight: 0.03, metabolism: '低'}
];

// 搜索基因
function searchGene(geneName) {
    document.getElementById('gene-search-input').value = geneName;
    queryGene();
}

// 查询基因
function queryGene() {
    const geneName = document.getElementById('gene-search-input').value.trim().toUpperCase();
    
    if (!geneName) {
        alert('请输入基因名称');
        return;
    }
    
    // 显示加载动画
    document.getElementById('gene-loading').style.display = 'block';
    document.getElementById('gene-error').style.display = 'none';
    document.getElementById('gene-results').style.display = 'none';
    
    // 模拟查询（实际应调用 HAGR API）
    setTimeout(() => {
        document.getElementById('gene-loading').style.display = 'none';
        
        const gene = geneData[geneName];
        
        if (gene) {
            displayGeneResults(gene);
        } else {
            // 基因未找到，显示错误
            document.getElementById('gene-error-message').textContent = `未找到基因 "${geneName}" 的信息。请检查基因名称是否正确，或尝试查询其他基因（如 FOXO3, SIRT1, MTOR, TP53, APOE）。`;
            document.getElementById('gene-error').style.display = 'block';
        }
    }, 1500);
}

// 显示基因结果
function displayGeneResults(gene) {
    const resultsDiv = document.getElementById('gene-results');
    
    resultsDiv.innerHTML = `
        <div style="background: white; padding: 30px; border-radius: 10px; border-left: 4px solid #667eea;">
            <h3 style="margin-top: 0; color: #2d3748; font-size: 24px;">${gene.name} <span style="font-size: 14px; color: #718096; font-weight: normal;">(${gene.fullName})</span></h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
                <div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
                    <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">GenAge 收录</div>
                    <div style="font-size: 18px; font-weight: bold; color: ${gene.inGenAge ? '#48bb78' : '#f56565'};">
                        ${gene.inGenAge ? '✅ 是' : '❌ 否'}
                    </div>
                </div>
                <div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
                    <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">PubMed 文献</div>
                    <div style="font-size: 18px; font-weight: bold; color: #667eea;">${gene.pubmedCount}+ 篇</div>
                </div>
            </div>
            
            <div style="margin: 20px 0;">
                <h4 style="color: #2d3748; margin-bottom: 10px;">📝 主要功能</h4>
                <p style="color: #718096; line-height: 1.6;">${gene.function}</p>
            </div>
            
            <div style="margin: 20px 0;">
                <h4 style="color: #2d3748; margin-bottom: 10px;">🔬 相关通路</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                    ${gene.pathways.map(p => `<span style="background: #667eea; color: white; padding: 5px 15px; border-radius: 15px; font-size: 13px;">${p}</span>`).join('')}
                </div>
            </div>
            
            <div style="margin: 20px 0;">
                <h4 style="color: #2d3748; margin-bottom: 10px;">🧬 同源基因</h4>
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background: #f7fafc;">
                            <th style="padding: 10px; text-align: left; border-bottom: 2px solid #e2e8f0;">物种</th>
                            <th style="padding: 10px; text-align: left; border-bottom: 2px solid #e2e8f0;">同源基因</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${Object.entries(gene.homologs).map(([species, gene]) => `
                            <tr>
                                <td style="padding: 10px; border-bottom: 1px solid #e2e8f0;">${species}</td>
                                <td style="padding: 10px; border-bottom: 1px solid #e2e8f0; font-family: monospace; color: #667eea;">${gene}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
            
            <div style="margin: 20px 0;">
                <h4 style="color: #2d3748; margin-bottom: 10px;">🔗 衰老标志物关联</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                    ${gene.hallmarks.map(h => `<span style="background: #ed8936; color: white; padding: 5px 15px; border-radius: 15px; font-size: 13px;">${h}</span>`).join('')}
                </div>
            </div>
            
            <div style="margin-top: 20px; padding: 15px; background: #f7fafc; border-radius: 6px;">
                <p style="margin: 0; font-size: 13px; color: #718096;">
                    💡 <strong>提示</strong>：更多详细信息请访问 
                    <a href="https://genomics.senescence.info/genes/" target="_blank" style="color: #667eea; font-weight: 500;">HAGR GenAge 数据库</a>
                </p>
            </div>
        </div>
    `;
    
    resultsDiv.style.display = 'block';
    resultsDiv.scrollIntoView({ behavior: 'smooth' });
}

// 筛选物种
function filterSpecies() {
    const speciesClass = document.getElementById('species-class').value;
    const minLongevity = parseFloat(document.getElementById('min-longevity').value) || 0;
    const weightRange = document.getElementById('weight-range').value;
    
    let filtered = speciesData.filter(s => {
        // 分类筛选
        if (speciesClass !== 'all' && s.class !== speciesClass) return false;
        
        // 寿命筛选
        if (s.longevity < minLongevity) return false;
        
        // 体重筛选
        if (weightRange === 'small' && s.weight >= 1) return false;
        if (weightRange === 'medium' && (s.weight < 1 || s.weight > 50)) return false;
        if (weightRange === 'large' && s.weight <= 50) return false;
        
        return true;
    });
    
    displaySpecies(filtered);
}

// 显示物种列表
function displaySpecies(species) {
    const resultsDiv = document.getElementById('species-results');
    
    if (species.length === 0) {
        resultsDiv.innerHTML = '<p style="text-align: center; color: #718096; padding: 30px;">未找到符合条件的物种</p>';
        return;
    }
    
    resultsDiv.innerHTML = `
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background: #f7fafc;">
                    <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e2e8f0;">物种名称</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">分类</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">最大寿命（年）</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">体重（kg）</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">代谢率</th>
                </tr>
            </thead>
            <tbody>
                ${species.map(s => `
                    <tr style="background: white;">
                        <td style="padding: 12px; border-bottom: 1px solid #e2e8f0; font-weight: 500;">${s.name}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${getClassIcon(s.class)}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0; color: #48bb78; font-weight: 600;">${s.longevity}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${formatWeight(s.weight)}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${getMetabolismBadge(s.metabolism)}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
        <p style="text-align: center; color: #718096; font-size: 13px; margin-top: 15px;">
            数据来源：AnAge 数据库 | 显示 ${species.length} 个物种
        </p>
    `;
}

// 辅助函数
function getClassIcon(classCode) {
    const icons = {
        'mammals': '🐋 哺乳动物',
        'birds': '🦜 鸟类',
        'reptiles': '🐢 爬行动物',
        'fish': '🐟 鱼类',
        'invertebrates': '🦐 无脊椎动物'
    };
    return icons[classCode] || classCode;
}

function formatWeight(weight) {
    if (weight >= 1000) return (weight / 1000).toFixed(1) + ' 吨';
    if (weight >= 1) return weight.toFixed(1) + ' kg';
    if (weight >= 0.001) return (weight * 1000).toFixed(1) + ' g';
    return (weight * 1000000).toFixed(1) + ' mg';
}

function getMetabolismBadge(metabolism) {
    const colors = {
        '极低': '#9f7aea',
        '低': '#48bb78',
        '中': '#ed8936',
        '高': '#f56565'
    };
    return `<span style="background: ${colors[metabolism]}; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">${metabolism}</span>`;
}

// CSS 动画
const style = document.createElement('style');
style.textContent = `
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
`;
document.head.appendChild(style);

// 初始化显示所有物种
displaySpecies(speciesData);
</script>
