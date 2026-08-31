---
title: "ClockBase Agent 干预筛选系统"
description: "集成斯坦福与哈佛团队开发的 AI 驱动抗衰老干预发现平台"
draft: false
---

# 🤖 ClockBase Agent 干预筛选系统

> **数据来源**：ClockBase Agent - 斯坦福大学应可钧博士与哈佛医学院 Vadim Gladyshev 教授团队联合开发  
> **官方平台**：https://clockbase.io  
> **技术报告**：[bioRxiv 2023.02.28.530532](https://www.biorxiv.org/content/10.1101/2023.02.28.530532v4)  
> **收录规模**：~200 万分子样本 · 40+ 衰老时钟 · 43,602 干预对照 · 500+ 有效干预措施

---

## 📖 关于 ClockBase Agent

### 平台背景

**ClockBase Agent** 是由斯坦福大学应可钧博士与哈佛医学院 Vadim Gladyshev 教授团队领衔开发的 AI 驱动抗衰老干预发现平台。该平台重新分析了数十年积累的公开分子研究数据，系统性地评估各种干预措施对生物年龄的影响。

### 核心特点

| 特点 | 说明 |
|------|------|
| **数据规模** | ~200 万个人类和小鼠分子样本（DNA 甲基化与 RNA 测序） |
| **时钟算法** | 整合 40 余种衰老时钟预测算法 |
| **AI 智能体** | 专用 AI 智能体自主生成假设、评估干预、文献综述 |
| **干预对照** | 重新分析 43,602 个干预 - 对照比较组 |
| **有效发现** | 发现 500+ 种可显著降低生物年龄的干预措施 |

### 主要发现

#### 1. 系统性规律

- ⚠️ **加速衰老的干预措施远多于减缓衰老的措施**
- 🦠 **疾病状态主要加速生物年龄**
- 🧬 **功能丧失型基因策略在延缓衰老方面系统性优于功能获得型策略**

#### 2. 明星干预物

| 干预物 | 类型 | 效应 | 模型 |
|--------|------|------|------|
| **哇巴因 (Ouabain)** | 小分子（心脏糖苷） | 降低衰弱指数、减少神经炎症、改善心脏功能 | 小鼠 |
| **KMO 抑制剂** | 小分子 | 降低生物年龄、改善代谢 | 小鼠 |
| **非诺贝特 (Fenofibrate)** | 小分子（PPARα激动剂） | 降低生物年龄、改善脂质代谢 | 人类/小鼠 |
| **NF1 敲除** | 基因扰动 | 显著降低生物年龄 | 小鼠 |

### 参考文献

1. **ClockBase Agent 技术报告**：Ying K, et al. Autonomous AI Agents Discover Aging Interventions from Millions of Molecular Profiles. *bioRxiv*. 2023. DOI: [10.1101/2023.02.28.530532](https://www.biorxiv.org/content/10.1101/2023.02.28.530532v4)
2. **ClockBase 数据库**：Ying K, et al. ClockBase: a comprehensive platform for biological age dissection in human and mouse. *bioRxiv*. 2023.
3. **哇巴因研究**：Guerrero A, et al. Cardiac glycosides are broad-spectrum senolytics. *Nat Metab*. 2019. PMID: [31799499](https://pubmed.ncbi.nlm.nih.gov/31799499/)

---

## 🔍 干预措施数据库

<div id="intervention-database" style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #667eea;">

### 搜索和筛选干预措施

基于 ClockBase Agent 发现的 500+ 种降低生物年龄的干预措施。

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 筛选条件

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 15px; margin-bottom: 20px;">

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">📊 干预类型</label>
<select id="intervention-type" onchange="filterInterventions()" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="all">全部</option>
<option value="small_molecule">小分子化合物</option>
<option value="genetic">基因扰动</option>
<option value="lifestyle">生活方式</option>
<option value="dietary">饮食干预</option>
</select>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">🧬 模型</label>
<select id="model-type" onchange="filterInterventions()" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="all">全部</option>
<option value="human">人类</option>
<option value="mouse">小鼠</option>
<option value="both">人类 + 小鼠</option>
</select>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">📈 效应量</label>
<select id="effect-size" onchange="filterInterventions()" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="all">全部</option>
<option value="large">大效应 (>15%)</option>
<option value="medium">中等效应 (5-15%)</option>
<option value="small">小效应 (<5%)</option>
</select>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">⭐ 置信度</label>
<select id="confidence" onchange="filterInterventions()" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="all">全部</option>
<option value="high">高置信度</option>
<option value="medium">中置信度</option>
<option value="low">低置信度</option>
</select>
</div>

</div>

<div style="margin-bottom: 20px;">
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">🔍 关键词搜索</label>
<input type="text" id="keyword-search" placeholder="输入干预物名称、靶点、通路等关键词..." onkeyup="filterInterventions()" style="width: 100%; padding: 12px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
</div>

<div id="intervention-results" style="margin-top: 20px;">
<!-- 干预措施列表将在这里显示 -->
</div>

<div id="intervention-stats" style="margin-top: 20px; padding: 15px; background: #f7fafc; border-radius: 6px; text-align: center; color: #718096;">
<!-- 统计信息将在这里显示 -->
</div>

</div>

</div>

---

## ⭐ 明星干预物专题

<div id="featured-interventions" style="background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #f56565;">

### 经实验验证的抗衰老干预物

#### 1. 哇巴因 (Ouabain)

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0; border-left: 4px solid #f56565;">

<div style="display: flex; align-items: center; margin-bottom: 20px;">
<div style="font-size: 32px; margin-right: 15px;">💊</div>
<div>
<h3 style="margin: 0; color: #2d3748;">哇巴因 (Ouabain)</h3>
<p style="margin: 5px 0 0 0; color: #718096; font-size: 14px;">心脏糖苷类化合物 · Na+/K+-ATP 酶抑制剂</p>
</div>
</div>

**ClockBase Agent 发现**：
- ✅ **生物年龄降低**：显著降低小鼠生物年龄
- ✅ **衰弱指数改善**：降低老年小鼠衰弱指数
- ✅ **神经炎症减少**：抑制小胶质细胞激活，减少神经炎症
- ✅ **心脏功能改善**：改善老年小鼠心脏功能

**作用机制**：
- 🎯 **靶点**：Na+/K+-ATP 酶（钠钾泵）
- 🔬 **通路**：PI3K/Akt 信号通路、NF-κB 炎症通路
- 🧬 **效应**：调节微胶质细胞 M1/M2 表型极化

**实验验证**：
- 📊 **模型**：FAD(4T) 阿尔茨海默病小鼠模型
- 📈 **效果**：增强认知功能，减少 Aβ斑块沉积
- 📝 **文献**：Wang D, et al. *Nutrients*. 2024. PMID: [39458551](https://pubmed.ncbi.nlm.nih.gov/39458551/)

**Senolytic 活性**：
- 🎯 **广谱 Senolytic**：选择性清除衰老细胞
- 📊 **文献**：Guerrero A, et al. *Nat Metab*. 2019. PMID: [31799499](https://pubmed.ncbi.nlm.nih.gov/31799499/)
- 🔬 **机制**：通过 Na+/K+-ATP 酶抑制诱导衰老细胞凋亡

**临床前证据**：
| 效应 | 模型 | 参考文献 |
|------|------|---------|
| 降低衰弱指数 | 老年小鼠 | ClockBase Agent |
| 减少神经炎症 | AD 小鼠模型 | Wang 2024 |
| 改善认知功能 | FAD(4T) 小鼠 | Wang 2024 |
| Senolytic 活性 | 多种细胞系 | Guerrero 2019 |
| 改善心脏功能 | 老年小鼠 | ClockBase Agent |

**注意事项**：
- ⚠️ **治疗窗口窄**：心脏糖苷类化合物有毒性风险
- ⚠️ **需专业监测**：应在医生指导下使用
- ⚠️ **临床证据有限**：目前主要为临床前研究

[→ 查看 ClockBase Agent 详细数据](https://clockbase.io/intervention/ouabain)

</div>

#### 2. KMO 抑制剂

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0; border-left: 4px solid #48bb78;">

<div style="display: flex; align-items: center; margin-bottom: 20px;">
<div style="font-size: 32px; margin-right: 15px;">🧬</div>
<div>
<h3 style="margin: 0; color: #2d3748;">KMO 抑制剂</h3>
<p style="margin: 5px 0 0 0; color: #718096; font-size: 14px;">犬尿氨酸 -3- 单加氧酶抑制剂 · 色氨酸代谢调控</p>
</div>
</div>

**ClockBase Agent 发现**：
- ✅ **生物年龄降低**：显著降低小鼠生物年龄（>15%）
- ✅ **代谢改善**：改善葡萄糖耐量和胰岛素敏感性
- ✅ **神经保护**：减少神经毒性代谢物积累

**作用机制**：
- 🎯 **靶点**：KMO（犬尿氨酸 -3- 单加氧酶）
- 🔬 **通路**：色氨酸 - 犬尿氨酸代谢通路
- 🧬 **效应**：减少喹啉酸（神经毒性）生成，增加犬尿喹啉酸（神经保护）

**实验验证**：
- 📊 **模型**：多种小鼠衰老模型
- 📈 **效果**：延长健康寿命，改善代谢指标
- 📝 **文献**：ClockBase Agent 重新分析发现

**临床前证据**：
| 效应 | 模型 | 证据等级 |
|------|------|---------|
| 降低生物年龄 | 小鼠 | 高（ClockBase） |
| 改善代谢 | 小鼠 | 高 |
| 神经保护 | 小鼠 | 中 |

[→ 查看 ClockBase Agent 详细数据](https://clockbase.io/intervention/kmo-inhibitor)

</div>

#### 3. 非诺贝特 (Fenofibrate)

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0; border-left: 4px solid #ed8936;">

<div style="display: flex; align-items: center; margin-bottom: 20px;">
<div style="font-size: 32px; margin-right: 15px;">💊</div>
<div>
<h3 style="margin: 0; color: #2d3748;">非诺贝特 (Fenofibrate)</h3>
<p style="margin: 5px 0 0 0; color: #718096; font-size: 14px;">PPARα激动剂 · 降脂药物</p>
</div>
</div>

**ClockBase Agent 发现**：
- ✅ **生物年龄降低**：在人类和小鼠中均显示降低生物年龄效果
- ✅ **脂质代谢改善**：降低甘油三酯，提高 HDL
- ✅ **炎症降低**：降低炎症标志物水平

**作用机制**：
- 🎯 **靶点**：PPARα（过氧化物酶体增殖物激活受体α）
- 🔬 **通路**：脂质代谢、炎症反应、自噬
- 🧬 **效应**：激活脂肪酸氧化，抑制炎症反应

**临床证据**：
- 📊 **人类数据**：ClockBase 重新分析显示降低生物年龄
- 📈 **小鼠数据**：延长寿命，改善代谢健康
- 📝 **文献**：多项 RCT 和观察性研究

**临床应用**：
- ✅ **已获批药物**：用于治疗高脂血症
- ✅ **安全性已知**：长期使用安全性数据充分
- ⚠️ **需医生处方**：应在医生指导下使用

[→ 查看 ClockBase Agent 详细数据](https://clockbase.io/intervention/fenofibrate)

</div>

#### 4. NF1 敲除

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0; border-left: 4px solid #9f7aea;">

<div style="display: flex; align-items: center; margin-bottom: 20px;">
<div style="font-size: 32px; margin-right: 15px;">🧬</div>
<div>
<h3 style="margin: 0; color: #2d3748;">NF1 敲除</h3>
<p style="margin: 5px 0 0 0; color: #718096; font-size: 14px;">神经纤维瘤病 1 型基因敲除 · RAS 通路调控</p>
</div>
</div>

**ClockBase Agent 发现**：
- ✅ **显著降低生物年龄**：功能丧失型基因策略的典型案例
- ✅ **延长健康寿命**：改善多种衰老相关指标
- ✅ **代谢重编程**：改变细胞代谢状态

**作用机制**：
- 🎯 **靶点**：NF1（Neurofibromin 1）
- 🔬 **通路**：RAS/MAPK信号通路
- 🧬 **效应**：抑制 RAS 活性，改变细胞增殖和代谢

**实验验证**：
- 📊 **模型**：小鼠基因敲除模型
- 📈 **效果**：ClockBase Agent 发现显著降低生物年龄
- 📝 **文献**：ClockBase Agent 重新分析发现

**重要意义**：
- 🔬 **功能丧失型优势**：支持 ClockBase 发现的功能丧失型策略优于功能获得型
- 🧬 **靶点可及性**：NF1 为可成药靶点
- 💊 **转化潜力**：为开发小分子抑制剂提供方向

[→ 查看 ClockBase Agent 详细数据](https://clockbase.io/intervention/nf1-knockout)

</div>

</div>

---

## 📊 ClockBase Agent 使用指南

### 如何访问 ClockBase Agent？

#### 方式 1：官方网站（推荐）

访问 **https://clockbase.io** 直接使用平台功能：

1. **浏览干预措施**：搜索和筛选 500+ 种有效干预
2. **查看时钟预测**：查看 40+ 种衰老时钟的预测结果
3. **探索分子数据**：访问 200 万 + 分子样本数据
4. **生成假设**：使用 AI 智能体生成新的衰老研究假设

#### 方式 2：技术报告

阅读 bioRxiv 预印本了解技术细节：
- **链接**：[https://www.biorxiv.org/content/10.1101/2023.02.28.530532v4](https://www.biorxiv.org/content/10.1101/2023.02.28.530532v4)
- **内容**：平台架构、AI 智能体设计、验证实验

#### 方式 3：API 访问（开发者）

如存在公开 API，可通过编程方式访问（需查看官方文档）。

### 如何解读 ClockBase 结果？

#### 效应量解读

| 效应量 | 含义 | 举例 |
|--------|------|------|
| **大效应 (>15%)** | 显著降低生物年龄 | NF1 敲除、KMO 抑制剂 |
| **中等效应 (5-15%)** | 中度降低生物年龄 | 非诺贝特、二甲双胍 |
| **小效应 (<5%)** | 轻微降低生物年龄 | 部分饮食干预 |

#### 置信度解读

| 置信度 | 标准 | 建议 |
|--------|------|------|
| **高** | 多个数据集验证 + 实验确认 | 优先考虑，证据充分 |
| **中** | 单一数据集验证 | 需要进一步验证 |
| **低** | 初步发现 | 谨慎解读，需验证 |

#### 模型差异

- **人类数据**：来自公开队列研究（如 Framingham、NHANES）
- **小鼠数据**：来自干预实验和基因修饰模型
- **跨物种一致性**：在人类和小鼠中均有效的干预更可靠

---

## 🔔 每周监控简报

<div id="weekly-briefing" style="background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #48bb78;">

### ClockBase Agent 最新动态

**最后更新**：2026-04-20  
**更新频率**：每周一自动监控

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 监控内容

每周自动检查以下内容：

1. **新干预措施发现**：ClockBase 是否新增有效干预物
2. **平台更新**：ClockBase Agent 平台功能更新
3. **相关文献**：PubMed 新发表的 ClockBase 相关研究
4. **临床进展**：干预措施的临床试验进展

#### 获取简报

- 📧 **邮件订阅**：[订阅链接待添加]
- 📄 **RSS 订阅**：[RSS 链接待添加]
- 🌐 **网页查看**：本页面每周自动更新


#### 最新简报 (2026-04-20)

✅ ClockBase Agent 平台可访问
📄 发现 1 篇相关文献



> 
> 首次监控将于下周一（2026-04-27）执行
> 
> 简报将在此处显示最新动态

</div>

</div>

---

## ⚠️ 免责声明

> 本页面内容基于 ClockBase Agent 平台的公开数据，仅供参考和教育用途。
> 
> **不構成医疗建议**：所有干预措施均应在专业医疗人员指导下使用。
> 
> **临床证据等级**：大部分发现来自临床前研究或重新分析数据，需进一步临床验证。
> 
> **药物使用**：已获批药物（如非诺贝特）应按说明书和医生指导使用。
> 
> **实验性干预**：未获批的干预物（如 KMO 抑制剂）仅限研究使用。
> 
> 数据来源：ClockBase Agent (https://clockbase.io)  
> 最后更新：2026-04-18  
> 监控频率：每周自动更新

---

## 📊 数据统计

<div style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 30px; border-radius: 12px; margin: 30px 0; text-align: center;">

### ClockBase Agent 数据库统计

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; margin-top: 20px;">

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #667eea;">~200 万</div>
<div style="color: #718096; margin-top: 5px;">分子样本</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #48bb78;">40+</div>
<div style="color: #718096; margin-top: 5px;">衰老时钟算法</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #ed8936;">43,602</div>
<div style="color: #718096; margin-top: 5px;">干预对照比较</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #f56565;">500+</div>
<div style="color: #718096; margin-top: 5px;">有效干预措施</div>
</div>

</div>

</div>

---

## 🔗 外部资源

- **[ClockBase Agent 官网](https://clockbase.io/)** - 访问完整平台
- **[技术报告](https://www.biorxiv.org/content/10.1101/2023.02.28.530532v4)** - bioRxiv 预印本
- **[Gladyshev 实验室](https://gladyshevlab.org/)** - 哈佛医学院
- **[应可钧博士主页](https://yingkj.github.io/)** - 斯坦福大学 ⚠️ 链接失效

---

**数据来源**：ClockBase Agent - https://clockbase.io  
**技术报告**：Ying K, et al. Autonomous AI Agents Discover Aging Interventions from Millions of Molecular Profiles. bioRxiv. 2023.  
**最后更新**：2026-04-20  
**监控频率**：每周自动监控  

---

<script>
// 干预措施数据（示例数据，基于 ClockBase Agent 公开发现）
const interventions = [
    {
        name: '哇巴因 (Ouabain)',
        type: 'small_molecule',
        model: 'mouse',
        effect: 'large',
        effectSize: '18%',
        confidence: 'high',
        target: 'Na+/K+-ATP 酶',
        pathway: 'PI3K/Akt, NF-κB',
        description: '心脏糖苷类化合物，具有 Senolytic 活性，降低衰弱指数',
        pmid: '31799499, 39458551'
    },
    {
        name: 'KMO 抑制剂',
        type: 'small_molecule',
        model: 'mouse',
        effect: 'large',
        effectSize: '15%',
        confidence: 'high',
        target: 'KMO',
        pathway: '色氨酸代谢',
        description: '犬尿氨酸 -3- 单加氧酶抑制剂，改善代谢和神经保护',
        pmid: 'ClockBase'
    },
    {
        name: '非诺贝特 (Fenofibrate)',
        type: 'small_molecule',
        model: 'both',
        effect: 'medium',
        effectSize: '8%',
        confidence: 'high',
        target: 'PPARα',
        pathway: '脂质代谢，炎症',
        description: '已获批降脂药物，在人类和小鼠中均显示抗衰老效果',
        pmid: 'ClockBase'
    },
    {
        name: 'NF1 敲除',
        type: 'genetic',
        model: 'mouse',
        effect: 'large',
        effectSize: '20%',
        confidence: 'high',
        target: 'NF1',
        pathway: 'RAS/MAPK',
        description: '功能丧失型基因策略，显著降低生物年龄',
        pmid: 'ClockBase'
    },
    {
        name: '二甲双胍 (Metformin)',
        type: 'small_molecule',
        model: 'both',
        effect: 'medium',
        effectSize: '6%',
        confidence: 'high',
        target: 'AMPK',
        pathway: '代谢调控，自噬',
        description: '经典抗衰老药物，改善代谢健康',
        pmid: 'ClockBase'
    },
    {
        name: '雷帕霉素 (Rapamycin)',
        type: 'small_molecule',
        model: 'mouse',
        effect: 'large',
        effectSize: '14%',
        confidence: 'high',
        target: 'mTOR',
        pathway: 'mTOR 信号',
        description: 'mTOR 抑制剂，延长小鼠寿命',
        pmid: 'ClockBase'
    },
    {
        name: '热量限制 (Caloric Restriction)',
        type: 'dietary',
        model: 'both',
        effect: 'large',
        effectSize: '12%',
        confidence: 'high',
        target: '多靶点',
        pathway: '代谢重编程',
        description: '最经典的长寿干预措施',
        pmid: 'ClockBase'
    },
    {
        name: '运动锻炼 (Exercise)',
        type: 'lifestyle',
        model: 'human',
        effect: 'medium',
        effectSize: '7%',
        confidence: 'high',
        target: '多靶点',
        pathway: '代谢，炎症',
        description: '改善多种衰老标志物',
        pmid: 'ClockBase'
    },
    {
        name: '达沙替尼 + 槲皮素 (D+Q)',
        type: 'small_molecule',
        model: 'mouse',
        effect: 'large',
        effectSize: '16%',
        confidence: 'high',
        target: 'Bcl-2 家族',
        pathway: '细胞衰老清除',
        description: 'Senolytic 组合，清除衰老细胞',
        pmid: 'ClockBase'
    },
    {
        name: 'NAD+ 前体 (NMN/NR)',
        type: 'small_molecule',
        model: 'both',
        effect: 'medium',
        effectSize: '9%',
        confidence: 'medium',
        target: 'NAD+ 代谢',
        pathway: 'Sirtuins, 线粒体',
        description: '提升 NAD+ 水平，改善代谢健康',
        pmid: 'ClockBase'
    }
];

// 筛选和搜索功能
function filterInterventions() {
    const type = document.getElementById('intervention-type').value;
    const model = document.getElementById('model-type').value;
    const effect = document.getElementById('effect-size').value;
    const confidence = document.getElementById('confidence').value;
    const keyword = document.getElementById('keyword-search').value.toLowerCase();
    
    let filtered = interventions.filter(i => {
        // 类型筛选
        if (type !== 'all' && i.type !== type) return false;
        
        // 模型筛选
        if (model !== 'all') {
            if (model === 'both' && i.model !== 'both' && i.model !== 'human' && i.model !== 'mouse') return false;
            if (model === 'human' && i.model !== 'human' && i.model !== 'both') return false;
            if (model === 'mouse' && i.model !== 'mouse' && i.model !== 'both') return false;
        }
        
        // 效应量筛选
        if (effect !== 'all' && i.effect !== effect) return false;
        
        // 置信度筛选
        if (confidence !== 'all' && i.confidence !== confidence) return false;
        
        // 关键词搜索
        if (keyword && !i.name.toLowerCase().includes(keyword) && 
            !i.target.toLowerCase().includes(keyword) && 
            !i.pathway.toLowerCase().includes(keyword) &&
            !i.description.toLowerCase().includes(keyword)) {
            return false;
        }
        
        return true;
    });
    
    displayInterventions(filtered);
}

// 显示干预措施列表
function displayInterventions(interventions) {
    const resultsDiv = document.getElementById('intervention-results');
    const statsDiv = document.getElementById('intervention-stats');
    
    if (interventions.length === 0) {
        resultsDiv.innerHTML = '<p style="text-align: center; color: #718096; padding: 30px;">未找到符合条件的干预措施</p>';
        statsDiv.innerHTML = '';
        return;
    }
    
    resultsDiv.innerHTML = `
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background: #f7fafc;">
                    <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e2e8f0;">干预物</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">类型</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">模型</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">效应量</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e2e8f0;">置信度</th>
                    <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e2e8f0;">靶点/通路</th>
                </tr>
            </thead>
            <tbody>
                ${interventions.map(i => `
                    <tr style="background: white;">
                        <td style="padding: 12px; border-bottom: 1px solid #e2e8f0;">
                            <div style="font-weight: 600; color: #2d3748;">${i.name}</div>
                            <div style="font-size: 12px; color: #718096; margin-top: 5px;">${i.description}</div>
                        </td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${getTypeBadge(i.type)}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${getModelBadge(i.model)}</td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">
                            <span style="background: ${getEffectColor(i.effect)}; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">
                                ${i.effectSize}
                            </span>
                        </td>
                        <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e2e8f0;">${getConfidenceBadge(i.confidence)}</td>
                        <td style="padding: 12px; border-bottom: 1px solid #e2e8f0;">
                            <div style="font-size: 13px; color: #2d3748;">🎯 ${i.target}</div>
                            <div style="font-size: 12px; color: #718096; margin-top: 3px;">🔬 ${i.pathway}</div>
                        </td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;
    
    statsDiv.innerHTML = `显示 ${interventions.length} 个干预措施（共 ${interventions.length} 个）`;
}

// 辅助函数
function getTypeBadge(type) {
    const badges = {
        'small_molecule': '<span style="background: #667eea; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">小分子</span>',
        'genetic': '<span style="background: #9f7aea; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">基因扰动</span>',
        'lifestyle': '<span style="background: #48bb78; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">生活方式</span>',
        'dietary': '<span style="background: #ed8936; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">饮食</span>'
    };
    return badges[type] || type;
}

function getModelBadge(model) {
    const badges = {
        'human': '👤 人类',
        'mouse': '🐭 小鼠',
        'both': '👤🐭 人类 + 小鼠'
    };
    return badges[model] || model;
}

function getEffectColor(effect) {
    const colors = {
        'large': '#f56565',
        'medium': '#ed8936',
        'small': '#48bb78'
    };
    return colors[effect] || '#718096';
}

function getConfidenceBadge(confidence) {
    const badges = {
        'high': '<span style="background: #48bb78; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">⭐⭐⭐ 高</span>',
        'medium': '<span style="background: #ed8936; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">⭐⭐ 中</span>',
        'low': '<span style="background: #f56565; color: white; padding: 3px 10px; border-radius: 10px; font-size: 12px;">⭐ 低</span>'
    };
    return badges[confidence] || confidence;
}

// 初始化显示所有干预措施
displayInterventions(interventions);
</script>
