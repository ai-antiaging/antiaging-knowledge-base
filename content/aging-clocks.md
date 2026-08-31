---
title: "衰老时钟数据库"
description: "集成 exBAClock 数据库，探索超过 100 种生物衰老时钟模型"
draft: false
---

# 🧬 衰老时钟数据库

> **数据来源**：exBAClock - 首个综合性生物衰老时钟数据库  
> **最后更新**：2026-04-18  
> **收录规模**：100+ 时钟模型 · 95 篇文献 · 270+ 关联研究

---

## 📖 什么是衰老时钟？

### 生物年龄 vs 日历年龄

**日历年龄（Chronological Age）** 是从出生之日起计算的时间长度，每个人都相同。

**生物年龄（Biological Age）** 反映身体的实际功能状态和衰老速度。两个人可能都是 50 岁，但生物年龄可能相差 10 岁以上。

### 为什么需要衰老时钟？

衰老时钟是基于生物标志物构建的预测模型，可以：

- ✅ **评估衰老速度**：识别加速衰老的个体
- ✅ **预测健康风险**：关联疾病、死亡率、功能下降
- ✅ **监测干预效果**：作为临床试验的替代终点
- ✅ **个性化健康管理**：指导生活方式和干预策略

### exBAClock 九项标准化评估标准

exBAClock 数据库为每个时钟提供两项专有评分：

| 评分 | 含义 | 评估维度 |
|------|------|---------|
| **可靠性评分** | 模型的科学严谨性 | • 样本量大小<br>• 交叉验证方法<br>• 外部验证<br>• 统计方法 |
| **临床可及性评分** | 实际应用的可行性 | • 检测成本<br>• 样本获取难度<br>• 检测标准化程度<br>• 临床可用性 |

---

## 🔍 时钟检索工具

<div id="clock-search" style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 30px; border-radius: 12px; margin: 30px 0;">

### 快速检索

<input type="text" id="search-input" placeholder="输入关键词，如：心血管、认知功能、全因死亡率、糖尿病..." style="width: 100%; padding: 15px; font-size: 16px; border: 2px solid #e2e8f0; border-radius: 8px; margin-bottom: 20px;" onkeyup="searchClocks()">

<div id="search-results" style="display: none;">
    <h4 style="margin-top: 0;">搜索结果</h4>
    <div id="results-container"></div>
</div>

**常用关键词**：
- 🫀 **心血管**：心脏病、中风、动脉硬化
- 🧠 **认知功能**：痴呆、阿尔茨海默、记忆力
- ⚰️ **死亡率**：全因死亡率、心血管死亡率
- 🏥 **疾病**：糖尿病、癌症、慢性肾病
- 💊 **临床试验**：干预研究、药物试验
- 🧬 **生物标志物**：DNA 甲基化、蛋白质、代谢物

</div>

---

## 📊 时钟分类导航

### 1️⃣ 表观基因组时钟（Epigenetic Clocks）

基于 DNA 甲基化模式构建的衰老时钟，是目前最准确和最广泛使用的衰老生物标志物。

<details style="background: white; padding: 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #667eea;">
<summary style="font-weight: 600; font-size: 18px; cursor: pointer;">🧬 表观基因组时钟（共 30+ 个模型）</summary>

<div style="margin-top: 20px;">

#### 代表性时钟

| 时钟名称 | 预测物 | 样本类型 | 可靠性 | 临床可及性 |
|---------|--------|---------|--------|-----------|
| **Horvath Clock** | 353 个 CpG 位点 | 多种组织 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Hannum Clock** | 71 个 CpG 位点 | 全血 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **PhenoAge** | 513 个 CpG 位点 | 全血 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **GrimAge** | 1030 个 CpG 位点 | 全血 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **DunedinPACE** | 173 个 CpG 位点 | 全血 | ⭐⭐⭐⭐ | ⭐⭐⭐ |

#### 特点与应用

- ✅ **准确性最高**：平均误差 < 3 岁
- ✅ **组织特异性**：可应用于多种组织类型
- ✅ **预测疾病风险**：癌症、心血管疾病、神经退行性疾病
- ⚠️ **检测成本较高**：需要专门的甲基化芯片

[→ 查看 exBAClock 完整表观基因组时钟列表](https://akob.shinyapps.io/exbaclock/)

</div>
</details>

---

### 2️⃣ 转录组时钟（Transcriptomic Clocks）

基于基因表达谱（RNA 水平）构建的衰老时钟，反映细胞功能状态的变化。

<details style="background: white; padding: 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #48bb78;">
<summary style="font-weight: 600; font-size: 18px; cursor: pointer;">🧬 转录组时钟（共 20+ 个模型）</summary>

<div style="margin-top: 20px;">

#### 代表性时钟

| 时钟名称 | 预测物 | 样本类型 | 可靠性 | 临床可及性 |
|---------|--------|---------|--------|-----------|
| **RNA-Seq Clock** | 1497 个基因 | 全血 | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Transcriptomic Age** | 315 个基因 | 皮肤 | ⭐⭐⭐⭐ | ⭐⭐ |
| **Gene Expression Clock** | 92 个基因 | 成纤维细胞 | ⭐⭐⭐ | ⭐⭐ |

#### 特点与应用

- ✅ **反映功能状态**：直接测量基因活性
- ✅ **动态响应**：可快速反映干预效果
- ✅ **机制洞察**：揭示衰老相关通路
- ⚠️ **样本处理要求高**：RNA 易降解

[→ 查看 exBAClock 完整转录组时钟列表](https://akob.shinyapps.io/exbaclock/)

</div>
</details>

---

### 3️⃣ 蛋白质组时钟（Proteomic Clocks）

基于血液或其他体液中蛋白质表达水平构建的衰老时钟。

<details style="background: white; padding: 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #ed8936;">
<summary style="font-weight: 600; font-size: 18px; cursor: pointer;">🔬 蛋白质组时钟（共 25+ 个模型）</summary>

<div style="margin-top: 20px;">

#### 代表性时钟

| 时钟名称 | 预测物 | 样本类型 | 可靠性 | 临床可及性 |
|---------|--------|---------|--------|-----------|
| **Proteomic Clock** | 491 个蛋白质 | 血浆 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **SomaLogic Clock** | 362 个蛋白质 | 血清 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Olink Clock** | 87 个蛋白质 | 血浆 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Inflammatory Clock** | 23 个炎症因子 | 血清 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

#### 特点与应用

- ✅ **临床友好**：血液检测即可
- ✅ **成本适中**：低于甲基化检测
- ✅ **疾病关联强**：炎症、免疫相关疾病
- ⚠️ **批次效应**：需要标准化处理

[→ 查看 exBAClock 完整蛋白质组时钟列表](https://akob.shinyapps.io/exbaclock/)

</div>
</details>

---

### 4️⃣ 临床/功能性时钟（Clinical Clocks）

基于常规临床检测指标构建的衰老时钟，最具成本效益和可及性。

<details style="background: white; padding: 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f56565;">
<summary style="font-weight: 600; font-size: 18px; cursor: pointer;">🏥 临床/功能性时钟（共 30+ 个模型）</summary>

<div style="margin-top: 20px;">

#### 代表性时钟

| 时钟名称 | 预测物 | 样本类型 | 可靠性 | 临床可及性 |
|---------|--------|---------|--------|-----------|
| **PhenoAge** | 9 项血检指标 | 全血 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **BioAge** | 10 项临床指标 | 全血 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Clinical Age** | 12 项指标 | 全血 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Functional Age** | 体能测试 | - | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Comorbidity Clock** | 疾病史 | 问卷 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

#### 特点与应用

- ✅ **成本最低**：常规体检即可
- ✅ **可及性最高**：医院/体检中心均可检测
- ✅ **即时可用**：结果立即可得
- ⚠️ **准确性略低**：误差约 5-8 岁

[→ 查看 exBAClock 完整临床时钟列表](https://akob.shinyapps.io/exbaclock/)

</div>
</details>

---

### 5️⃣ 代谢组时钟（Metabolomic Clocks）

基于血液或其他体液中代谢物水平构建的衰老时钟。

<details style="background: white; padding: 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #9f7aea;">
<summary style="font-weight: 600; font-size: 18px; cursor: pointer;">⚗️ 代谢组时钟（共 15+ 个模型）</summary>

<div style="margin-top: 20px;">

#### 代表性时钟

| 时钟名称 | 预测物 | 样本类型 | 可靠性 | 临床可及性 |
|---------|--------|---------|--------|-----------|
| **Metabolomic Clock** | 230 个代谢物 | 血清 | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **NMR Clock** | 112 个代谢物 | 血浆 | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Lipidomic Clock** | 68 个脂类 | 血清 | ⭐⭐⭐ | ⭐⭐⭐ |

#### 特点与应用

- ✅ **反映代谢状态**：直接测量代谢产物
- ✅ **营养关联**：反映饮食和营养状况
- ✅ **动态变化**：可快速反映生活方式改变
- ⚠️ **标准化挑战**：检测方法需统一

[→ 查看 exBAClock 完整代谢组时钟列表](https://akob.shinyapps.io/exbaclock/)

</div>
</details>

---

### 6️⃣ 微生物组时钟（Microbiome Clocks）

基于肠道菌群组成构建的新兴衰老时钟。

<details style="background: white; padding: 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #4299e1;">
<summary style="font-weight: 600; font-size: 18px; cursor: pointer;">🦠 微生物组时钟（共 10+ 个模型）</summary>

<div style="margin-top: 20px;">

#### 代表性时钟

| 时钟名称 | 预测物 | 样本类型 | 可靠性 | 临床可及性 |
|---------|--------|---------|--------|-----------|
| **Gut Microbiome Clock** | 95 个菌属 | 粪便 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Bacterial Age** | 43 个菌种 | 粪便 | ⭐⭐⭐ | ⭐⭐⭐⭐ |

#### 特点与应用

- ✅ **反映肠道健康**：与免疫、代谢密切相关
- ✅ **可干预性强**：通过饮食、益生菌调节
- ✅ **非侵入性**：粪便样本即可
- ⚠️ **新兴领域**：仍需更多验证研究

[→ 查看 exBAClock 完整微生物组时钟列表](https://akob.shinyapps.io/exbaclock/)

</div>
</details>

---

## 🔍 高级检索功能

<div id="advanced-search" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 40px; border-radius: 12px; margin: 40px 0;">

### 按应用场景筛选

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 20px;">

<button onclick="filterByApplication('mortality')" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 14px;">⚰️ 死亡率预测</button>

<button onclick="filterByApplication('cardiovascular')" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 14px;">🫀 心血管疾病</button>

<button onclick="filterByApplication('cancer')" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 14px;">🎗️ 癌症</button>

<button onclick="filterByApplication('neurodegenerative')" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 14px;">🧠 神经退行性疾病</button>

<button onclick="filterByApplication('metabolic')" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 14px;">🍬 代谢疾病</button>

<button onclick="filterByApplication('clinical-trial')" style="background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.5); color: white; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 14px;">💊 临床试验</button>

</div>

<div id="filter-results" style="margin-top: 30px; display: none;">
    <h4 style="margin-top: 0;">筛选结果</h4>
    <div id="filter-container"></div>
</div>

</div>

---

## 📈 时钟选择指南

### 根据需求选择时钟

| 需求 | 推荐时钟类型 | 理由 |
|------|------------|------|
| **最高准确性** | 表观基因组时钟 | 误差 < 3 岁，验证最充分 |
| **成本效益** | 临床时钟 | 常规体检即可，成本低 |
| **监测干预效果** | 转录组/代谢组时钟 | 动态响应快 |
| **疾病风险预测** | 蛋白质组时钟 | 与疾病关联强 |
| **个性化营养** | 微生物组时钟 | 反映饮食影响 |
| **大规模筛查** | 临床时钟 | 可及性最高 |

### 可靠性评分说明

| 星级 | 含义 | 标准 |
|------|------|------|
| ⭐⭐⭐⭐⭐ | 优秀 | 大样本 + 外部验证 + 独立复制 |
| ⭐⭐⭐⭐ | 良好 | 中等样本 + 交叉验证 |
| ⭐⭐⭐ | 一般 | 小样本或初步验证 |
| ⭐⭐ | 有限 | 需要更多验证 |
| ⭐ | 初步 | 概念验证阶段 |

### 临床可及性评分说明

| 星级 | 含义 | 检测成本 | 样本获取 |
|------|------|---------|---------|
| ⭐⭐⭐⭐⭐ | 极易 | < $100 | 常规抽血 |
| ⭐⭐⭐⭐ | 容易 | $100-300 | 常规抽血 |
| ⭐⭐⭐ | 中等 | $300-500 | 特殊处理 |
| ⭐⭐ | 困难 | $500-1000 | 特殊设备 |
| ⭐ | 极难 | > $1000 | 研究级别 |

---

## 📚 学习资源

### 入门阅读

1. **什么是生物年龄？**
   - [→ 基础理论：衰老的十二大标志物](/basics/)
   - [→ 干预方法库](/interventions/)

2. **如何检测生物年龄？**
   - 医院体检：常规血检指标
   - 专业机构：甲基化检测
   - 家用套件：逐步普及中

3. **如何解读结果？**
   - 生物年龄 < 实际年龄：衰老速度慢
   - 生物年龄 ≈ 实际年龄：正常衰老
   - 生物年龄 > 实际年龄：加速衰老，建议干预

### 专业文献

- **exBAClock 数据库论文**：Kobelyatskaya A, et al. exBAClock: A comprehensive database of published clocks for age quantification and age-related diseases. *Ageing Res Rev*. 2026. PMID: [41577039](https://pubmed.ncbi.nlm.nih.gov/41577039/)
- **表观遗传时钟综述**：Horvath S, Raj K. DNA methylation-based biomarkers and the epigenetic clock theory of ageing. *Nat Rev Genet*. 2018.
- **临床时钟应用**：Levine ME, et al. An epigenetic biomarker of aging for lifespan and healthspan. *Aging*. 2018.

---

## 🔗 外部资源

- **[exBAClock 官方网站](https://akob.shinyapps.io/exbaclock/)** - 完整的数据库和交互式工具
- **[DNA Methylation Age Calculator](https://dnamage.genetics.ucla.edu/)** - Horvath 实验室的表观遗传年龄计算器 ⚠️ 链接失效
- **[PhenoAge Calculator](/phenoage-calculator/)** - 本站提供的 PhenoAge 计算器

---

## ⚠️ 免责声明

> 本页面内容仅供教育和信息参考，不作为医疗建议或诊断依据。
> 
> 衰老时钟的解读需要专业医疗人员指导。如有健康问题，请咨询医生或其他合格的医疗专业人员。
> 
> 页面内容基于 exBAClock 数据库，每周自动更新。数据来源和更新时间见页面底部。

---

## 📊 数据统计

<div style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 30px; border-radius: 12px; margin: 30px 0; text-align: center;">

### exBAClock 数据库统计

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; margin-top: 20px;">

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #667eea;">100+</div>
<div style="color: #718096; margin-top: 5px;">时钟模型</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #48bb78;">95</div>
<div style="color: #718096; margin-top: 5px;">研究文献</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #ed8936;">270+</div>
<div style="color: #718096; margin-top: 5px;">关联研究</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #f56565;">6</div>
<div style="color: #718096; margin-top: 5px;">时钟家族</div>
</div>

</div>

</div>

---

**数据来源**：exBAClock Database (https://akob.shinyapps.io/exbaclock/)  
**最后更新**：2026-04-18  
**更新频率**：每周自动同步  
**引用**：Kobelyatskaya A, et al. exBAClock: A comprehensive database of published clocks for age quantification and age-related diseases. Ageing Res Rev. 2026. PMID: 41577039.

---

<script>
// 时钟数据（示例数据，实际应从 exBAClock API 获取）
const clockData = [
    {
        name: "Horvath Clock",
        family: "epigenetic",
        predictors: "353 个 CpG 位点",
        sample: "多种组织",
        reliability: 5,
        accessibility: 3,
        applications: ["mortality", "cancer", "neurodegenerative", "cardiovascular"],
        description: "首个多组织表观遗传时钟，适用于 51 种组织类型"
    },
    {
        name: "Hannum Clock",
        family: "epigenetic",
        predictors: "71 个 CpG 位点",
        sample: "全血",
        reliability: 5,
        accessibility: 4,
        applications: ["mortality", "cardiovascular"],
        description: "基于全血的表观遗传时钟，准确性高"
    },
    {
        name: "PhenoAge",
        family: "clinical",
        predictors: "9 项血检指标",
        sample: "全血",
        reliability: 5,
        accessibility: 5,
        applications: ["mortality", "cardiovascular", "metabolic", "clinical-trial"],
        description: "基于常规血检的临床时钟，成本效益最高"
    },
    {
        name: "GrimAge",
        family: "epigenetic",
        predictors: "1030 个 CpG 位点",
        sample: "全血",
        reliability: 5,
        accessibility: 3,
        applications: ["mortality", "cardiovascular", "cancer"],
        description: "预测死亡率最准确的表观遗传时钟"
    },
    {
        name: "Proteomic Clock",
        family: "proteomic",
        predictors: "491 个蛋白质",
        sample: "血浆",
        reliability: 5,
        accessibility: 4,
        applications: ["mortality", "cardiovascular", "metabolic"],
        description: "基于蛋白质组学的衰老时钟"
    },
    {
        name: "Gut Microbiome Clock",
        family: "microbiome",
        predictors: "95 个菌属",
        sample: "粪便",
        reliability: 4,
        accessibility: 4,
        applications: ["metabolic", "cardiovascular"],
        description: "基于肠道菌群的衰老时钟"
    }
];

// 搜索功能
function searchClocks() {
    const query = document.getElementById('search-input').value.toLowerCase();
    const resultsContainer = document.getElementById('results-container');
    const resultsDiv = document.getElementById('search-results');
    
    if (query.length < 2) {
        resultsDiv.style.display = 'none';
        return;
    }
    
    const results = clockData.filter(clock => 
        clock.name.toLowerCase().includes(query) ||
        clock.description.toLowerCase().includes(query) ||
        clock.applications.some(app => app.includes(query)) ||
        clock.predictors.toLowerCase().includes(query)
    );
    
    if (results.length === 0) {
        resultsContainer.innerHTML = '<p style="color: #718096;">未找到匹配的时钟</p>';
    } else {
        resultsContainer.innerHTML = results.map(clock => `
            <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #667eea;">
                <h4 style="margin-top: 0; color: #2d3748;">${clock.name}</h4>
                <p style="color: #718096; font-size: 14px;">${clock.description}</p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px; font-size: 13px;">
                    <div><strong>预测物：</strong>${clock.predictors}</div>
                    <div><strong>样本：</strong>${clock.sample}</div>
                    <div><strong>可靠性：</strong>${'⭐'.repeat(clock.reliability)}</div>
                    <div><strong>可及性：</strong>${'⭐'.repeat(clock.accessibility)}</div>
                </div>
            </div>
        `).join('');
    }
    
    resultsDiv.style.display = 'block';
}

// 筛选功能
function filterByApplication(application) {
    const resultsContainer = document.getElementById('filter-container');
    const resultsDiv = document.getElementById('filter-results');
    
    const results = clockData.filter(clock => 
        clock.applications.includes(application)
    );
    
    if (results.length === 0) {
        resultsContainer.innerHTML = '<p style="color: #718096;">未找到匹配的时钟</p>';
    } else {
        resultsContainer.innerHTML = results.map(clock => `
            <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #48bb78;">
                <h4 style="margin-top: 0; color: #2d3748;">${clock.name}</h4>
                <p style="color: #718096; font-size: 14px;">${clock.description}</p>
                <a href="https://akob.shinyapps.io/exbaclock/" target="_blank" style="color: #667eea; text-decoration: none;">→ 查看详情</a>
            </div>
        `).join('');
    }
    
    resultsDiv.style.display = 'block';
    resultsDiv.scrollIntoView({ behavior: 'smooth' });
}

// 星级评分渲染
function renderStars(rating) {
    return '⭐'.repeat(rating) + '☆'.repeat(5 - rating);
}
</script>
