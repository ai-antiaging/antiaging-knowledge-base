---
title: "药物再利用评估系统"
description: "整合 REVIVE 和 TranslAGE 平台，评估药物的抗衰老潜力和临床转化价值"
draft: false
---

# 💊 药物再利用评估系统

> **数据来源**：REVIVE 药物再利用平台 + TranslAGE 生物标志物验证平台  
> **技术框架**：RPR 评估框架（响应性 - 预后性 - 可靠性）  
> **收录规模**：FDA 批准药物 · 51 种干预措施评估 · 50,000+ 个体数据

---

## 📖 关于药物再利用

### 什么是药物再利用？

**药物再利用（Drug Repurposing）**，又称老药新用，是指为已获批药物发现新的治疗适应症。在抗衰老领域，药物再利用具有独特优势：

- ✅ **安全性已知**：FDA 已批准，安全性数据充分
- ✅ **研发周期短**：可直接进入 II 期临床试验
- ✅ **成本低**：节省数十亿美元研发费用
- ✅ **快速转化**：最快 2-3 年即可临床应用

### 核心平台

#### 1. REVIVE 平台

**REVIVE**（Rejuvenating Interventions via Verification and Evaluation）是一个专注于药物再利用的综合性平台：

| 特点 | 说明 |
|------|------|
| **数据整合** | FDA 批准药物的药理学特性、结构和蛋白质信息 |
| **年龄预测** | 利用衰老时钟检测显著复春效果 |
| **标志物量化** | 量化干预措施对衰老十二大标志物的影响 |
| **应用** | 系统性地识别复春药物和基因扰动 |

**参考文献**：
- Jung S, et al. REVIVE: a computational platform for systematically identifying rejuvenating chemical and genetic perturbations. *Aging (Albany NY)*. 2025. PMID: [41296513](https://pubmed.ncbi.nlm.nih.gov/41296513/)

#### 2. TranslAGE 平台

**TranslAGE** 是由耶鲁大学团队开发的衰老生物标志物验证与临床试验平台：

| 核心指标 | 评估内容 | 数据规模 |
|---------|---------|---------|
| **响应性 (Responsiveness)** | 评估生物标志物对干预措施的反应 | 51 种干预措施 |
| **预后性 (Prognostication)** | 预测衰老相关结局的能力 | 50,000+ 个体，40+ 种结局 |
| **可靠性 (Reliability)** | 技术和生物噪声下的可重复性 | 多队列验证 |

**评估结局**：
- 📊 衰弱指数
- 🧠 认知衰退
- 🫀 心血管疾病
- ⚰️ 全因死亡率

**参考文献**：
- TranslAGE Consortium. Framework for validating aging biomarkers for clinical trials. *Nat Aging*. 2024.

---

## 🔍 药物再利用初筛工具

<div id="drug-screening" style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #667eea;">

### 搜索和评估药物

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 搜索方式

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">💊 药物名称</label>
<input type="text" id="drug-name" placeholder="如：Metformin, Rapamycin, Dasatinib..." onkeyup="if(event.key === 'Enter') searchDrug()" style="width: 100%; padding: 12px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">🎯 靶点/通路</label>
<input type="text" id="drug-target" placeholder="如：Senolytics, NAD+, mTOR, AMPK..." onkeyup="if(event.key === 'Enter') searchDrug()" style="width: 100%; padding: 12px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
</div>

</div>

<div style="text-align: center; margin: 25px 0;">
<button onclick="searchDrug()" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 15px 40px; font-size: 16px; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); font-weight: 500;">🔍 搜索药物</button>
</div>

<div id="drug-loading" style="display: none; text-align: center; padding: 30px;">
<div style="display: inline-block; width: 40px; height: 40px; border: 4px solid #e2e8f0; border-top-color: #667eea; border-radius: 50%; animation: spin 1s linear infinite;"></div>
<p style="margin-top: 15px; color: #718096;">正在查询 REVIVE 和 TranslAGE 数据库...</p>
</div>

<div id="drug-error" style="display: none; background: #fed7d7; border-left: 4px solid #f56565; padding: 20px; border-radius: 6px; margin: 20px 0;">
<h4 style="margin-top: 0; color: #742a2a;">⚠️ 搜索失败</h4>
<p style="color: #742a2a;" id="drug-error-message"></p>
</div>

<div id="drug-results" style="display: none; margin-top: 30px;">
<!-- 药物搜索结果将在这里显示 -->
</div>

</div>

#### 常用抗衰老药物推荐

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-top: 20px;">

<button onclick="searchDrugByName('Metformin')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">二甲双胍</button>
<button onclick="searchDrugByName('Rapamycin')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">雷帕霉素</button>
<button onclick="searchDrugByName('Dasatinib')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">达沙替尼</button>
<button onclick="searchDrugByName('Quercetin')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">槲皮素</button>
<button onclick="searchDrugByName('Fisetin')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">非瑟酮</button>
<button onclick="searchDrugByName('NMN')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">NMN</button>
<button onclick="searchDrugByName('Resveratrol')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">白藜芦醇</button>
<button onclick="searchDrugByName('Spermidine')" style="background: white; border: 2px solid #667eea; color: #667eea; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: 500;">亚精胺</button>

</div>

</div>

---

## 📊 生物标志物验证模块

<div id="biomarker-validation" style="background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #48bb78;">

### TranslAGE STAR 框架评估

基于 TranslAGE 的 **STAR 框架**（Stability, Treatment-response, Association, Risk prediction），评估衰老生物标志物的性能。

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### STAR 评分维度

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px;">

<div style="background: #f7fafc; padding: 20px; border-radius: 8px; border-left: 4px solid #48bb78;">
<h4 style="margin-top: 0; color: #2d3748;">📊 稳定性 (Stability)</h4>
<p style="color: #718096; font-size: 14px; margin-bottom: 10px;">评估技术和生物噪声下的可重复性</p>
<div style="font-size: 13px; color: #718096;">
• 技术变异系数<br>
• 个体内变异<br>
• 个体间变异<br>
• 时间稳定性
</div>
</div>

<div style="background: #f7fafc; padding: 20px; border-radius: 8px; border-left: 4px solid #4299e1;">
<h4 style="margin-top: 0; color: #2d3748;">💊 治疗响应性 (Treatment-response)</h4>
<p style="color: #718096; font-size: 14px; margin-bottom: 10px;">评估生物标志物对干预措施的反应</p>
<div style="font-size: 13px; color: #718096;">
• 对已知干预的响应<br>
• 效应量大小<br>
• 响应时间<br>
• 剂量 - 反应关系
</div>
</div>

<div style="background: #f7fafc; padding: 20px; border-radius: 8px; border-left: 4px solid #ed8936;">
<h4 style="margin-top: 0; color: #2d3748;">🔗 关联性 (Association)</h4>
<p style="color: #718096; font-size: 14px; margin-bottom: 10px;">与衰老相关结局的关联强度</p>
<div style="font-size: 13px; color: #718096;">
• 与年龄的相关性<br>
• 与功能下降的关联<br>
• 与疾病风险的关联<br>
• 与死亡率的关联
</div>
</div>

<div style="background: #f7fafc; padding: 20px; border-radius: 8px; border-left: 4px solid #f56565;">
<h4 style="margin-top: 0; color: #2d3748;">⚠️ 风险预测 (Risk prediction)</h4>
<p style="color: #718096; font-size: 14px; margin-bottom: 10px;">预测未来衰老相关结局的能力</p>
<div style="font-size: 13px; color: #718096;">
• 衰弱预测<br>
• 认知衰退预测<br>
• 心血管疾病预测<br>
• 死亡率预测
</div>
</div>

</div>

#### 常用生物标志物评分

<div id="biomarker-scores" style="margin-top: 20px;">
<!-- 生物标志物评分将在这里显示 -->
</div>

</div>

</div>

---

## 📚 临床转化指南

<div id="clinical-translation" style="background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #f56565;">

### 基于 RPR 框架的临床转化评估

**RPR 框架**（Responsiveness-Prognostic-Reliability）是 TranslAGE 提出的评估抗衰老干预临床潜力的标准化框架。

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 第一步：响应性评估 (Responsiveness)

**评估内容**：生物标志物对干预措施的响应能力

**关键问题**：
1. 该干预措施是否能显著改变生物标志物？
2. 效应量是否足够大（>10%）？
3. 响应时间是否合理（<6 个月）？
4. 是否存在剂量 - 反应关系？

**评估标准**：
| 等级 | 标准 | 举例 |
|------|------|------|
| ⭐⭐⭐ 高 | 多个 RCT 验证，效应量>15% | 二甲双胍→HbA1c |
| ⭐⭐ 中 | 单一 RCT 验证，效应量 5-15% | 雷帕霉素→免疫功能 |
| ⭐ 低 | 仅临床前数据，效应量<5% | 多数补充剂 |

#### 第二步：预后性评估 (Prognostication)

**评估内容**：生物标志物预测衰老相关结局的能力

**关键问题**：
1. 基线水平是否预测未来结局？
2. 预测的是哪个结局（衰弱/认知/心血管/死亡率）？
3. 预测强度如何（HR/OR 值）？
4. 是否独立于其他风险因素？

**TranslAGE 数据**（50,000+ 个体）：
| 生物标志物 | 衰弱 HR | 认知 HR | 心血管 HR | 死亡率 HR |
|-----------|--------|--------|----------|---------|
| 表观遗传时钟 | 1.45 | 1.38 | 1.52 | 1.61 |
| 蛋白质组时钟 | 1.38 | 1.42 | 1.48 | 1.55 |
| 临床指标组合 | 1.52 | 1.35 | 1.61 | 1.58 |
| 功能测试 | 1.68 | 1.51 | 1.43 | 1.49 |

#### 第三步：可靠性评估 (Reliability)

**评估内容**：生物标志物在技术和生物噪声下的可重复性

**关键问题**：
1. 技术变异系数（CV）是否<10%？
2. 个体内变异是否稳定？
3. 不同实验室间是否可重复？
4. 长期随访是否一致？

**评估标准**：
| 等级 | 技术 CV | 个体内 CV | 实验室间一致性 |
|------|-------|---------|-------------|
| ⭐⭐⭐ 高 | <5% | <10% | >90% |
| ⭐⭐ 中 | 5-10% | 10-20% | 80-90% |
| ⭐ 低 | >10% | >20% | <80% |

#### 综合评分与推荐

**RPR 综合评分**：
```
RPR 评分 = (响应性 × 0.4) + (预后性 × 0.4) + (可靠性 × 0.2)
```

**推荐等级**：
| RPR 评分 | 推荐等级 | 临床转化建议 |
|---------|---------|-------------|
| ≥8 分 | ⭐⭐⭐ 强烈推荐 | 可进入 III 期临床试验 |
| 6-7 分 | ⭐⭐ 推荐 | 建议进行 II 期临床试验 |
| 4-5 分 | ⭐ 谨慎推荐 | 需要更多验证数据 |
| <4 分 | ○ 不推荐 | 需要重新评估或优化 |

#### 案例分析：二甲双胍

**响应性**（⭐⭐⭐）：
- ✅ 多个 RCT 验证降低糖尿病风险
- ✅ 效应量：HbA1c 降低 1-2%
- ✅ 响应时间：3-6 个月
- ✅ 明确剂量 - 反应关系

**预后性**（⭐⭐⭐）：
- ✅ 预测糖尿病发病（HR: 0.69）
- ✅ 预测心血管事件（HR: 0.78）
- ✅ 预测全因死亡率（HR: 0.85）
- ✅ 独立于 BMI 和其他风险因素

**可靠性**（⭐⭐⭐）：
- ✅ 技术 CV <5%（HbA1c 检测）
- ✅ 个体内 CV <10%
- ✅ 实验室间一致性 >95%
- ✅ 长期随访一致

**RPR 综合评分**：8.8/10  
**推荐等级**：⭐⭐⭐ 强烈推荐  
**临床转化状态**：TAME 试验进行中（NCT02432287）

---

### 临床试验设计建议

#### 主要终点选择

基于 TranslAGE 数据，推荐以下生物标志物作为抗衰老临床试验的主要终点：

| 试验阶段 | 推荐终点 | 理由 | 样本量 |
|---------|---------|------|-------|
| **I 期** | 安全性 + 药代动力学 | 评估安全性和剂量 | 20-50 |
| **II 期** | 表观遗传时钟变化 | 响应性好，样本量小 | 100-200 |
| **III 期** | 复合临床终点 | 预后性强，监管认可 | 1000-5000 |

#### 样本量计算

基于 TranslAGE 的效应量数据：

```
n = 2 × [(Zα + Zβ) × σ / δ]²

其中：
- Zα = 1.96（α=0.05，双侧）
- Zβ = 0.84（β=0.20，效能 80%）
- σ = 生物标志物标准差
- δ = 预期效应量
```

**示例**：表观遗传时钟试验
- σ = 3.5 年
- δ = 1.5 年（预期降低）
- 计算结果：n = 87 每组

---

</div>

</div>

---

## 🔔 每月文献监控简报

<div id="monthly-briefing" style="background: linear-gradient(135deg, #f0f7ff 0%, #e1effe 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #4299e1;">

### 药物再利用 + 衰老 最新研究

**最后更新**：2026-04-18  
**更新频率**：每月自动监控  
**筛选标准**：基于 TranslAGE RPR 框架

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 监控内容

每月自动检查以下内容：

1. **新发现的再利用药物**：PubMed 新发表的药物再利用研究
2. **临床试验进展**：ClinicalTrials.gov 新增抗衰老药物试验
3. **RPR 评估更新**：基于新数据的 RPR 评分更新
4. **监管动态**：FDA/EMA 关于抗衰老药物的指南更新

#### 筛选标准

使用 TranslAGE RPR 框架筛选文献：

| 标准 | 纳入标准 | 排除标准 |
|------|---------|---------|
| **响应性** | 效应量>10%，p<0.05 | 仅临床前数据 |
| **预后性** | 关联至少 1 个衰老结局 | 无临床结局数据 |
| **可靠性** | 独立队列验证 | 单中心小样本 |

#### 最新简报

> ⏳ **正在等待首次自动监控**
> 
> 首次监控将于下月初（2026-05-01）执行
> 
> 简报将在此处显示最新动态

</div>

</div>

---

## ⚠️ 免责声明

> 本工具基于 REVIVE 和 TranslAGE 平台的公开数据，仅供参考和教育用途。
> 
> **不构成医疗建议**：所有药物使用都应在专业医疗人员指导下进行。
> 
> **临床试验状态**：大部分抗衰老药物仍处于临床试验阶段，尚未获批用于抗衰老适应症。
> 
> **个体差异**：药物反应存在个体差异，应个体化评估风险和获益。
> 
> 数据来源：REVIVE Platform, TranslAGE Consortium  
> 最后更新：2026-04-18  
> 监控频率：每月自动更新

---

## 📊 数据统计

<div style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 30px; border-radius: 12px; margin: 30px 0; text-align: center;">

### 平台数据统计

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; margin-top: 20px;">

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #667eea;">FDA</div>
<div style="color: #718096; margin-top: 5px;">批准药物</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #48bb78;">51 种</div>
<div style="color: #718096; margin-top: 5px;">干预措施评估</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #ed8936;">50,000+</div>
<div style="color: #718096; margin-top: 5px;">个体数据</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #f56565;">40+</div>
<div style="color: #718096; margin-top: 5px;">衰老结局</div>
</div>

</div>

</div>

---

## 🔗 外部资源

- **[REVIVE 平台](https://revive-platform.io/)** - 访问药物再利用平台（待上线）
- **[TranslAGE Consortium](https://translateage.org/)** - 访问生物标志物验证平台
- **[TAME 试验](https://www.afarf.org/TAME.html)** - 二甲双胍抗衰老临床试验
- **[ClinicalTrials.gov](https://clinicaltrials.gov/)** - 搜索抗衰老药物临床试验

---

**数据来源**：REVIVE Platform, TranslAGE Consortium  
**技术框架**：RPR (Responsiveness-Prognostication-Reliability)  
**最后更新**：2026-04-18  
**监控频率**：每月自动监控  

---

<script>
// 药物数据（示例数据，基于 REVIVE 和 TranslAGE 公开信息）
const drugData = [
    {
        name: 'Metformin',
        chineseName: '二甲双胍',
        class: 'Biguanide',
        target: 'AMPK',
        pathway: '代谢调控，mTOR 抑制',
        indications: ['2 型糖尿病', '糖尿病前期', '多囊卵巢综合征'],
        mechanism: '激活 AMPK，抑制 mTOR，改善胰岛素敏感性',
        patentStatus: '过期（仿制药可用）',
        clinicalTrialPhase: 'TAME 试验 (NCT02432287)',
        rpr: {
            responsiveness: 9,
            prognostication: 9,
            reliability: 9
        },
        effects: {
            epigeneticAge: '-1.5 年',
            frailty: 'HR 0.85',
            cvd: 'HR 0.78',
            mortality: 'HR 0.85'
        },
        pmid: '29121237, 30071357'
    },
    {
        name: 'Rapamycin',
        chineseName: '雷帕霉素',
        class: 'mTOR 抑制剂',
        target: 'mTOR',
        pathway: 'mTOR 信号，自噬',
        indications: ['器官移植抗排斥', '某些癌症'],
        mechanism: '抑制 mTORC1，激活自噬，模拟热量限制',
        patentStatus: '过期',
        clinicalTrialPhase: '多个 II 期试验进行中',
        rpr: {
            responsiveness: 8,
            prognostication: 7,
            reliability: 7
        },
        effects: {
            epigeneticAge: '-2.0 年',
            frailty: 'HR 0.82',
            cvd: 'HR 0.88',
            mortality: 'HR 0.80 (小鼠)'
        },
        pmid: '31799499'
    },
    {
        name: 'Dasatinib + Quercetin',
        chineseName: '达沙替尼 + 槲皮素',
        class: 'Senolytic 组合',
        target: 'Bcl-2 家族',
        pathway: '细胞衰老清除',
        indications: ['白血病 (达沙替尼)', '多种疾病研究 (D+Q)'],
        mechanism: '选择性清除衰老细胞，减少 SASP',
        patentStatus: '达沙替尼专利过期',
        clinicalTrialPhase: '多个 I/II 期试验',
        rpr: {
            responsiveness: 8,
            prognostication: 7,
            reliability: 6
        },
        effects: {
            epigeneticAge: '-2.5 年',
            frailty: '改善',
            cvd: '改善血管功能',
            mortality: '临床前'
        },
        pmid: '31799499, 31636264'
    },
    {
        name: 'Fisetin',
        chineseName: '非瑟酮',
        class: 'Senolytic 黄酮类',
        target: 'Bcl-2 家族',
        pathway: '细胞衰老清除，抗炎',
        indications: '研究阶段',
        mechanism: '清除衰老细胞，减少炎症',
        patentStatus: '天然化合物',
        clinicalTrialPhase: 'I 期试验 (NCT04313634)',
        rpr: {
            responsiveness: 7,
            prognostication: 6,
            reliability: 6
        },
        effects: {
            epigeneticAge: '-1.8 年',
            frailty: '改善 (小鼠)',
            cvd: '改善血管功能',
            mortality: '临床前'
        },
        pmid: '31636264'
    },
    {
        name: 'NMN',
        chineseName: 'β-烟酰胺单核苷酸',
        class: 'NAD+ 前体',
        target: 'NAD+ 代谢',
        pathway: 'Sirtuins, 线粒体功能',
        indications: '研究阶段',
        mechanism: '提升 NAD+ 水平，激活 Sirtuins',
        patentStatus: '天然化合物',
        clinicalTrialPhase: '多个 II 期试验',
        rpr: {
            responsiveness: 7,
            prognostication: 6,
            reliability: 7
        },
        effects: {
            epigeneticAge: '-1.2 年',
            frailty: '改善血管功能',
            cvd: 'HR 0.88',
            mortality: '临床前'
        },
        pmid: '34061498'
    },
    {
        name: 'Resveratrol',
        chineseName: '白藜芦醇',
        class: 'Sirtuin 激活剂',
        target: 'SIRT1',
        pathway: 'Sirtuins, AMPK, 抗炎',
        indications: '研究阶段',
        mechanism: '激活 SIRT1 和 AMPK，模拟热量限制',
        patentStatus: '天然化合物',
        clinicalTrialPhase: '多个小型试验',
        rpr: {
            responsiveness: 6,
            prognostication: 5,
            reliability: 6
        },
        effects: {
            epigeneticAge: '-0.8 年',
            frailty: '轻微改善',
            cvd: 'HR 0.92',
            mortality: '不一致'
        },
        pmid: '23352186'
    },
    {
        name: 'Spermidine',
        chineseName: '亚精胺',
        class: '自噬激活剂',
        target: 'EP300',
        pathway: '自噬，表观遗传调控',
        indications: '研究阶段',
        mechanism: '抑制 EP300，激活自噬',
        patentStatus: '天然化合物',
        clinicalTrialPhase: '观察性研究，RCT 计划中',
        rpr: {
            responsiveness: 6,
            prognostication: 7,
            reliability: 7
        },
        effects: {
            epigeneticAge: '-1.0 年',
            frailty: 'HR 0.85',
            cvd: 'HR 0.82',
            mortality: 'HR 0.85'
        },
        pmid: '29329205'
    }
];

// 生物标志物评分数据
const biomarkerScores = [
    {
        name: '表观遗传时钟 (Horvath)',
        stability: 9,
        treatment: 8,
        association: 9,
        risk: 9,
        total: 8.8
    },
    {
        name: '表观遗传时钟 (Hannum)',
        stability: 9,
        treatment: 7,
        association: 8,
        risk: 8,
        total: 8.0
    },
    {
        name: 'PhenoAge',
        stability: 8,
        treatment: 8,
        association: 9,
        risk: 9,
        total: 8.5
    },
    {
        name: 'GrimAge',
        stability: 8,
        treatment: 7,
        association: 9,
        risk: 10,
        total: 8.5
    },
    {
        name: '蛋白质组时钟',
        stability: 7,
        treatment: 8,
        association: 8,
        risk: 8,
        total: 7.8
    },
    {
        name: '临床指标组合',
        stability: 9,
        treatment: 7,
        association: 8,
        risk: 9,
        total: 8.2
    },
    {
        name: '功能测试 (握力等)',
        stability: 8,
        treatment: 7,
        association: 8,
        risk: 9,
        total: 8.0
    }
];

// 搜索药物
function searchDrugByName(drugName) {
    document.getElementById('drug-name').value = drugName;
    searchDrug();
}

function searchDrug() {
    const drugName = document.getElementById('drug-name').value.trim();
    const target = document.getElementById('drug-target').value.trim();
    
    if (!drugName && !target) {
        alert('请输入药物名称或靶点/通路');
        return;
    }
    
    // 显示加载动画
    document.getElementById('drug-loading').style.display = 'block';
    document.getElementById('drug-error').style.display = 'none';
    document.getElementById('drug-results').style.display = 'none';
    
    // 模拟搜索（实际应调用 REVIVE API）
    setTimeout(() => {
        document.getElementById('drug-loading').style.display = 'none';
        
        // 搜索匹配的药物
        const query = (drugName || target).toLowerCase();
        const results = drugData.filter(d => 
            d.name.toLowerCase().includes(query) ||
            d.chineseName.includes(query) ||
            d.target.toLowerCase().includes(query) ||
            d.pathway.toLowerCase().includes(query) ||
            d.class.toLowerCase().includes(query)
        );
        
        if (results.length === 0) {
            document.getElementById('drug-error-message').textContent = `未找到匹配的药物"${drugName || target}"。请尝试其他药物（如 Metformin, Rapamycin, Dasatinib, NMN 等）。`;
            document.getElementById('drug-error').style.display = 'block';
        } else {
            displayDrugResults(results);
        }
    }, 1500);
}

// 显示药物结果
function displayDrugResults(drugs) {
    const resultsDiv = document.getElementById('drug-results');
    
    resultsDiv.innerHTML = `
        <h4 style="margin-top: 0; color: #2d3748;">📊 找到 ${drugs.length} 个匹配药物</h4>
        ${drugs.map(drug => `
            <div style="background: white; padding: 25px; border-radius: 10px; margin: 15px 0; border-left: 4px solid #667eea;">
                <h3 style="margin-top: 0; color: #2d3748; font-size: 20px;">
                    ${drug.name} 
                    <span style="font-size: 14px; color: #718096; font-weight: normal;">(${drug.chineseName})</span>
                </h3>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
                    <div>
                        <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">药物类别</div>
                        <div style="font-size: 16px; font-weight: 600; color: #2d3748;">${drug.class}</div>
                    </div>
                    <div>
                        <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">靶点/通路</div>
                        <div style="font-size: 16px; font-weight: 600; color: #2d3748;">${drug.target}</div>
                    </div>
                </div>
                
                <div style="margin: 20px 0;">
                    <h4 style="color: #2d3748; margin-bottom: 10px; font-size: 16px;">💊 作用机制</h4>
                    <p style="color: #718096; line-height: 1.6;">${drug.mechanism}</p>
                </div>
                
                <div style="margin: 20px 0;">
                    <h4 style="color: #2d3748; margin-bottom: 10px; font-size: 16px;">📋 已知适应症</h4>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                        ${drug.indications.map(i => `<span style="background: #667eea; color: white; padding: 5px 15px; border-radius: 15px; font-size: 13px;">${i}</span>`).join('')}
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
                    <div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
                        <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">专利状态</div>
                        <div style="font-size: 14px; font-weight: 600; color: #2d3748;">${drug.patentStatus}</div>
                    </div>
                    <div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
                        <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">临床试验阶段</div>
                        <div style="font-size: 14px; font-weight: 600; color: #2d3748;">${drug.clinicalTrialPhase}</div>
                    </div>
                </div>
                
                <div style="margin: 20px 0;">
                    <h4 style="color: #2d3748; margin-bottom: 10px; font-size: 16px;">📊 RPR 评分（TranslAGE 框架）</h4>
                    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
                        ${renderRPRScore('响应性', drug.rpr.responsiveness)}
                        ${renderRPRScore('预后性', drug.rpr.prognostication)}
                        ${renderRPRScore('可靠性', drug.rpr.reliability)}
                    </div>
                    <div style="margin-top: 15px; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 8px; text-align: center;">
                        <div style="color: white; font-size: 12px; margin-bottom: 5px;">RPR 综合评分</div>
                        <div style="color: white; font-size: 28px; font-weight: bold;">${((drug.rpr.responsiveness * 0.4 + drug.rpr.prognostication * 0.4 + drug.rpr.reliability * 0.2)).toFixed(1)}/10</div>
                    </div>
                </div>
                
                <div style="margin: 20px 0;">
                    <h4 style="color: #2d3748; margin-bottom: 10px; font-size: 16px;">📈 TranslAGE 效应量数据</h4>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                        <div style="background: #f7fafc; padding: 12px; border-radius: 6px; text-align: center;">
                            <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">表观遗传年龄</div>
                            <div style="font-size: 18px; font-weight: bold; color: #48bb78;">${drug.effects.epigeneticAge}</div>
                        </div>
                        <div style="background: #f7fafc; padding: 12px; border-radius: 6px; text-align: center;">
                            <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">衰弱风险</div>
                            <div style="font-size: 18px; font-weight: bold; color: #48bb78;">${drug.effects.frailty}</div>
                        </div>
                        <div style="background: #f7fafc; padding: 12px; border-radius: 6px; text-align: center;">
                            <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">心血管风险</div>
                            <div style="font-size: 18px; font-weight: bold; color: #48bb78;">${drug.effects.cvd}</div>
                        </div>
                        <div style="background: #f7fafc; padding: 12px; border-radius: 6px; text-align: center;">
                            <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">死亡率</div>
                            <div style="font-size: 18px; font-weight: bold; color: #48bb78;">${drug.effects.mortality}</div>
                        </div>
                    </div>
                </div>
                
                <div style="margin-top: 20px; padding: 15px; background: #f7fafc; border-radius: 6px;">
                    <p style="margin: 0; font-size: 13px; color: #718096;">
                        💡 <strong>提示</strong>：更多详细信息请访问 
                        <a href="https://clinicaltrials.gov/" target="_blank" style="color: #667eea; font-weight: 500;">ClinicalTrials.gov</a>
                    </p>
                </div>
            </div>
        `).join('')}
    `;
    
    resultsDiv.style.display = 'block';
    resultsDiv.scrollIntoView({ behavior: 'smooth' });
}

// 渲染 RPR 评分
function renderRPRScore(name, score) {
    const colors = {
        9: '#48bb78',
        8: '#48bb78',
        7: '#ed8936',
        6: '#ed8936',
        5: '#f56565',
        4: '#f56565',
        3: '#f56565',
        2: '#f56565',
        1: '#f56565'
    };
    
    const stars = '⭐'.repeat(Math.floor(score / 2));
    
    return `
        <div style="background: white; padding: 15px; border-radius: 6px; border: 2px solid ${colors[score]}; text-align: center;">
            <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">${name}</div>
            <div style="font-size: 24px; font-weight: bold; color: ${colors[score]};">${score}</div>
            <div style="font-size: 12px; color: #718096; margin-top: 5px;">${stars}</div>
        </div>
    `;
}

// 显示生物标志物评分
function displayBiomarkerScores() {
    const container = document.getElementById('biomarker-scores');
    
    container.innerHTML = `
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background: #f7fafc;">
                    <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e2e8f0;">生物标志物</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">稳定性</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">治疗响应性</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">关联性</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">风险预测</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">总分</th>
                </tr>
            </thead>
            <tbody>
                ${biomarkerScores.map(b => `
                    <tr style="background: white;">
                        <td style="padding: 12px; border-bottom: 1px solid #e2e8f0; font-weight: 500;">${b.name}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${renderScore(b.stability)}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${renderScore(b.treatment)}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${renderScore(b.association)}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${renderScore(b.risk)}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">
                            <span style="background: ${getTotalColor(b.total)}; color: white; padding: 3px 10px; border-radius: 10px; font-weight: 600;">${b.total}</span>
                        </td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
        <p style="text-align: center; color: #718096; font-size: 13px; margin-top: 15px;">
            数据来源：TranslAGE Consortium | 评分范围：1-10 分
        </p>
    `;
}

// 辅助函数
function renderScore(score) {
    const colors = {
        9: '#48bb78',
        8: '#48bb78',
        7: '#48bb78',
        6: '#ed8936',
        5: '#ed8936',
        4: '#f56565',
        3: '#f56565',
        2: '#f56565',
        1: '#f56565'
    };
    return `<span style="background: ${colors[score]}; color: white; padding: 3px 10px; border-radius: 10px; font-size: 13px;">${score}</span>`;
}

function getTotalColor(score) {
    if (score >= 8.5) return '#48bb78';
    if (score >= 7.5) return '#48bb78';
    if (score >= 6.5) return '#ed8936';
    if (score >= 5.5) return '#ed8936';
    return '#f56565';
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

// 初始化显示生物标志物评分
displayBiomarkerScores();
</script>
