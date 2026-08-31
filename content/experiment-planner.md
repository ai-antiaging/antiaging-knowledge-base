---
title: "实验规划助手"
description: "基于 K-Dense 最佳实践的衰老研究实验设计工具与指南"
draft: false
---

# 🧪 实验规划助手

> **技术参考**：K-Dense Beta · Biostate AI  
> **适用领域**：衰老生物学 · 转化医学 · 生物信息学  
> **功能定位**：研究设计模板 · 样本量计算 · 实验方案清单 · 技能索引

---

## 📖 关于 K-Dense

### 什么是 K-Dense？

**K-Dense** 是 Biostate AI 推出的综合性多智能体 AI 研究系统，可将研究周期从数年压缩至数天，同时消除生成式 AI 模型中的幻觉问题。

### 核心能力

| 能力 | 说明 |
|------|------|
| **250+ 数据库** | PubMed, ChEMBL, UniProt, SEC EDGAR, FRED 等 |
| **500K+ Python 包** | 任何 PyPI 包，包括 RDKit, Scanpy, scikit-learn, BioPython |
| **200+ 科学数据格式** | FASTA, BAM, VCF, DICOM, mzML, FITS 等 |
| **136 项科学技能** | 生物信息学、化学信息学、蛋白质组学、临床研究 |
| **代码执行沙箱** | 安全执行 Python/R 代码，生成可发表图表 |
| **出版物就绪输出** | 论文、幻灯片、LaTeX、交互式可视化 |

### K-Dense 与哈佛医学院合作案例

**David Sinclair 团队**使用 K-Dense 构建了转录组衰老时钟：
- 📊 分析超过 **600,000 个转录组谱**
- 🔬 筛选出 **关键衰老相关基因**
- 📈 构建了 **跨组织衰老时钟**
- 📝 生成 **可发表的研究论文**

### 版本选择

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|---------|
| **K-Dense BYOK** | 免费 | 网络搜索、文件处理、100+ 科学数据库、136 项技能 | 个人研究者、学生 |
| **K-Dense Pro** | 订阅制 | 全部数据库、优先支持、团队协作 | 实验室、研究团队 |
| **K-Dense Enterprise** | 企业定制 | 私有部署、自定义数据库、API 接入 | 制药公司、CRO |

**本地部署要求**（BYOK 版本）：
- 💻 CPU: 8 核以上
- 📀 RAM: 16GB 以上
- 💾 存储：50GB 可用空间
- 🐍 Python: 3.10+
- 🔗 网络：需要访问科学数据库

---

## 🎯 实验规划工具

<div id="experiment-planner" style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #667eea;">

### 研究设计助手

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 步骤 1：定义研究问题

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">🔬 研究领域</label>
<select id="research-field" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="">请选择...</option>
<option value="aging_biology">衰老生物学</option>
<option value="senolytics">Senolytics</option>
<option value="nad">NAD+ 代谢</option>
<option value="epigenetics">表观遗传学</option>
<option value="transcriptomics">转录组学</option>
<option value="proteomics">蛋白质组学</option>
<option value="metabolomics">代谢组学</option>
<option value="clinical">临床研究</option>
</select>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">📋 研究类型</label>
<select id="study-type" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="">请选择...</option>
<option value="observational">观察性研究</option>
<option value="interventional">干预性研究</option>
<option value="meta_analysis">Meta 分析</option>
<option value="bioinformatics">生物信息学分析</option>
<option value="drug_screening">药物筛选</option>
</select>
</div>

</div>

<div style="margin-bottom: 20px;">
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">📝 研究问题描述</label>
<textarea id="research-question" rows="4" placeholder="请详细描述您的研究问题，例如：'探究 NMN 补充对老年小鼠肝脏转录组的影响'..." style="width: 100%; padding: 12px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px; font-family: inherit;"></textarea>
</div>

#### 步骤 2：实验参数

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-bottom: 20px;">

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">🧬 实验模型</label>
<select id="model-system" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="">请选择...</option>
<option value="cell_line">细胞系</option>
<option value="mouse">小鼠</option>
<option value="rat">大鼠</option>
<option value="non_human_primate">非人灵长类</option>
<option value="human_cohort">人类队列</option>
<option value="public_data">公共数据库</option>
</select>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">💰 预算范围（USD）</label>
<select id="budget-range" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="">请选择...</option>
<option value="low">< $10,000</option>
<option value="medium">$10,000 - $50,000</option>
<option value="high">$50,000 - $200,000</option>
<option value="very_high">> $200,000</option>
</select>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">⏱️ 时间限制</label>
<select id="timeline" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<option value="">请选择...</option>
<option value="short">< 6 个月</option>
<option value="medium">6-12 个月</option>
<option value="long">1-2 年</option>
<option value="very_long">> 2 年</option>
</select>
</div>

</div>

<div style="text-align: center; margin: 25px 0;">
<button onclick="generateExperimentPlan()" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 15px 40px; font-size: 16px; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); font-weight: 500;">📋 生成实验设计方案</button>
</div>

<div id="plan-loading" style="display: none; text-align: center; padding: 30px;">
<div style="display: inline-block; width: 40px; height: 40px; border: 4px solid #e2e8f0; border-top-color: #667eea; border-radius: 50%; animation: spin 1s linear infinite;"></div>
<p style="margin-top: 15px; color: #718096;">正在生成实验设计方案...</p>
</div>

<div id="experiment-plan" style="display: none; margin-top: 30px;">
<!-- 实验设计方案将在这里显示 -->
</div>

</div>

</div>

---

## 🧮 样本量计算器

<div id="sample-size-calculator" style="background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #48bb78;">

### 基于效应量的样本量估算

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 参数设置

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 20px;">

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">📊 效应量 (Cohen's d)</label>
<input type="number" id="effect-size" step="0.1" min="0.1" max="3.0" value="0.5" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<div style="font-size: 12px; color: #718096; margin-top: 5px;">小=0.2, 中=0.5, 大=0.8</div>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">🎯 显著性水平 (α)</label>
<input type="number" id="alpha" step="0.01" min="0.001" max="0.1" value="0.05" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<div style="font-size: 12px; color: #718096; margin-top: 5px;">通常设为 0.05</div>
</div>

<div>
<label style="display: block; margin-bottom: 8px; font-weight: 500; color: #2d3748;">⚡ 统计效能 (1-β)</label>
<input type="number" id="power" step="0.05" min="0.5" max="0.99" value="0.8" style="width: 100%; padding: 10px; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 14px;">
<div style="font-size: 12px; color: #718096; margin-top: 5px;">通常设为 0.8</div>
</div>

</div>

<div style="text-align: center; margin: 25px 0;">
<button onclick="calculateSampleSize()" style="background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); color: white; border: none; padding: 15px 40px; font-size: 16px; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 15px rgba(72, 187, 120, 0.4); font-weight: 500;">🧮 计算样本量</button>
</div>

<div id="sample-size-result" style="display: none; margin-top: 30px; padding: 25px; background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); border-radius: 8px;">
<!-- 样本量计算结果将在这里显示 -->
</div>

</div>

</div>

---

## 📚 K-Dense 技能集索引

<div id="kdense-skills" style="background: linear-gradient(135deg, #faf5ff 0%, #e9d8fd 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #9f7aea;">

### 136 项科学技能分类目录

基于 K-Dense 的技能集，分类展示与衰老研究相关的技能。

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 🔬 生物信息学技能（42 项）

| 技能名称 | 功能描述 | 适用场景 |
|---------|---------|---------|
| **衰老时钟构建** | 从多组学数据构建衰老预测模型 | 转录组、表观组、蛋白组 |
| **差异表达分析** | 识别不同条件下的差异表达基因 | RNA-seq, 单细胞测序 |
| **通路富集分析** | GO/KEGG 通路富集分析 | 功能注释、机制研究 |
| **GSEA 分析** | 基因集富集分析 | 通路水平分析 |
| **WGCNA** | 加权基因共表达网络分析 | 模块识别、hub 基因 |
| **生存分析** | Kaplan-Meier、Cox 回归 | 临床队列分析 |

#### 🧪 化学信息学技能（28 项）

| 技能名称 | 功能描述 | 适用场景 |
|---------|---------|---------|
| **分子对接** | 小分子 - 蛋白相互作用预测 | 药物筛选、机制研究 |
| **ADMET 预测** | 吸收、分布、代谢、排泄、毒性 | 药物开发 |
| **QSAR 建模** | 定量构效关系分析 | 药物优化 |
| **虚拟筛选** | 大规模化合物库筛选 | 药物发现 |

#### 🧬 蛋白质组学技能（24 项）

| 技能名称 | 功能描述 | 适用场景 |
|---------|---------|---------|
| **质谱数据分析** | LC-MS/MS数据处理 | 蛋白质鉴定、定量 |
| **蛋白质相互作用** | PPI 网络构建与分析 | 机制研究 |
| **磷酸化分析** | 磷酸化位点鉴定 | 信号通路研究 |

#### 🏥 临床研究技能（22 项）

| 技能名称 | 功能描述 | 适用场景 |
|---------|---------|---------|
| **临床试验设计** | RCT、队列研究设计 | 临床研究规划 |
| **Meta 分析** | 系统综述与 Meta 分析 | 证据整合 |
| **生物标志物验证** | 诊断/预后标志物评估 | 转化研究 |

#### 📊 数据科学技能（20 项）

| 技能名称 | 功能描述 | 适用场景 |
|---------|---------|---------|
| **机器学习建模** | 分类、回归、聚类 | 预测模型 |
| **深度学习** | 神经网络、CNN、RNN | 复杂模式识别 |
| **数据可视化** | 出版级图表生成 | 论文、报告 |

[→ 查看完整 136 项技能列表](https://k-dense.ai/skills) ⚠️ 链接失效

</div>

</div>

---

## 📖 David Sinclair 团队案例分析

<div id="sinclair-case-study" style="background: linear-gradient(135deg, #f0f7ff 0%, #e1effe 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #4299e1;">

### K-Dense 构建转录组衰老时钟

**合作团队**：哈佛医学院 David Sinclair 教授团队  
**研究内容**：从超过 600,000 个转录组谱中筛选关键衰老基因  
**使用工具**：K-Dense Beta

#### 研究流程

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

##### 阶段 1：数据收集与质控（K-Dense 自动化）

- 📊 **数据来源**：GEO、ArrayExpress、GTEx 等公共数据库
- 🔍 **自动检索**：K-Dense 自动搜索并下载 600,000+ 转录组样本
- ✅ **质量控制**：自动过滤低质量样本，保留 60,000 个高质量样本
- 📋 **元数据标准化**：统一组织类型、年龄、性别等信息

**K-Dense 技能应用**：
- 公共数据库检索
- 数据质控流程
- 元数据标准化

##### 阶段 2：差异表达分析

- 🧬 **年龄相关基因筛选**：识别随年龄变化的基因
- 📈 **组织特异性分析**：比较不同组织的衰老特征
- 🔬 **共表达网络构建**：WGCNA 识别衰老相关模块

**K-Dense 技能应用**：
- 差异表达分析（DESeq2, edgeR）
- WGCNA 共表达网络
- 组织特异性分析

##### 阶段 3：衰老时钟构建

- 🤖 **机器学习建模**：Elastic Net、Random Forest、XGBoost
- 📊 **模型优化**：交叉验证、超参数调优
- 🎯 **特征选择**：从 20,000+ 基因筛选出关键预测基因

**K-Dense 技能应用**：
- 机器学习建模
- 特征选择
- 模型评估

##### 阶段 4：生物学验证

- 🧪 **通路富集分析**：GO/KEGG 通路注释
- 🔬 **实验验证**：关键基因的敲除/过表达验证
- 📝 **论文撰写**：K-Dense 自动生成初稿

**K-Dense 技能应用**：
- 通路富集分析
- 实验设计建议
- 论文撰写辅助

#### 关键发现

| 发现 | 描述 | 意义 |
|------|------|------|
| **核心衰老基因** | 筛选出 150 个跨组织保守的衰老相关基因 | 潜在干预靶点 |
| **组织特异性** | 不同组织有独特的衰老转录特征 | 精准干预策略 |
| **生命阶段标志物** | 识别出不同生命阶段的差异预测基因 | 早期衰老检测 |
| **干预响应基因** | 筛选出对热量限制、雷帕霉素等干预敏感的基因 | 药物筛选靶点 |

#### 研究时间对比

| 阶段 | 传统方法 | K-Dense 辅助 | 时间节省 |
|------|---------|------------|---------|
| 数据收集 | 2-3 个月 | 2-3 天 | 95% |
| 数据分析 | 6-12 个月 | 2-4 周 | 85% |
| 论文撰写 | 2-3 个月 | 1-2 周 | 80% |
| **总计** | **10-18 个月** | **1-2 个月** | **85-90%** |

#### 可复现性

K-Dense 生成的完整研究流程包括：
- ✅ 所有分析代码（Python/R）
- ✅ 数据处理流程
- ✅ 统计方法详情
- ✅ 图表生成脚本
- ✅ 论文 LaTeX 模板

[→ 查看完整案例研究](https://k-dense.ai/case-studies/sinclair-transcriptomic-clock) ⚠️ 链接失效

</div>

</div>

---

## 📋 衰老研究常用实验方案清单

<div id="protocol-checklist" style="background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%); padding: 40px; border-radius: 12px; margin: 40px 0; border: 2px solid #f56565;">

### 基于 K-Dense 最佳实践

<div style="background: white; padding: 30px; border-radius: 10px; margin: 20px 0;">

#### 转录组学研究方案

- [ ] **实验设计**
  - [ ] 明确研究问题和假设
  - [ ] 选择合适的实验模型（细胞/动物/人类）
  - [ ] 计算样本量（使用上方计算器）
  - [ ] 设置合适的对照组

- [ ] **样本采集**
  - [ ] 标准化采样流程
  - [ ] 快速冷冻保存（液氮）
  - [ ] 记录详细元数据
  - [ ] 质量控制（RNA integrity number > 7）

- [ ] **测序与质控**
  - [ ] 选择合适的测序平台（Illumina, Nanopore）
  - [ ] 测序深度（至少 30M reads/sample）
  - [ ] 质控指标（Q30, mapping rate）
  - [ ] 去除批次效应

- [ ] **数据分析**
  - [ ] 差异表达分析（DESeq2/edgeR）
  - [ ] 通路富集分析（GO/KEGG）
  - [ ] GSEA 分析
  - [ ] 衰老时钟构建（如适用）

- [ ] **验证实验**
  - [ ] qPCR 验证关键基因
  - [ ] 蛋白质水平验证（Western blot）
  - [ ] 功能验证（敲除/过表达）

#### Senolytics 研究方案

- [ ] **体外筛选**
  - [ ] 选择衰老细胞模型（复制性衰老、药物诱导）
  - [ ] 设置 senolytic 和 senomorphic 对照
  - [ ] 细胞活力检测（CCK-8, MTT）
  - [ ] 衰老标志物检测（SA-β-gal, p16, p21）

- [ ] **体内验证**
  - [ ] 选择合适的动物模型（自然衰老、诱导衰老）
  - [ ] 确定给药方案（剂量、频率、途径）
  - [ ] 监测安全性（体重、器官功能）
  - [ ] 评估疗效（组织学、功能测试）

- [ ] **机制研究**
  - [ ] 凋亡通路检测（caspase 活性）
  - [ ] SASP 因子检测（ELISA, qPCR）
  - [ ] 线粒体功能评估
  - [ ] 自噬水平检测

#### NAD+ 研究方案

- [ ] **NAD+ 水平检测**
  - [ ] 选择合适的检测方法（LC-MS/MS, 酶法）
  - [ ] 区分 NAD+ 和 NADH
  - [ ] 组织特异性分析
  - [ ] 亚细胞定位（细胞质 vs 线粒体）

- [ ] **功能评估**
  - [ ] 线粒体功能（Seahorse 分析）
  - [ ] Sirtuin 活性检测
  - [ ] DNA 修复能力
  - [ ] 代谢组学分析

- [ ] **干预研究**
  - [ ] 前体选择（NMN, NR, NAM）
  - [ ] 剂量反应曲线
  - [ ] 时间进程分析
  - [ ] 联合干预评估

</div>

</div>

---

## ⚠️ 免责声明

> 本页面提供的实验规划工具和指南仅供参考，不构成医疗或研究建议。
> 
> **研究伦理**：所有涉及人类或动物的研究必须获得伦理委员会批准。
> 
> **K-Dense 说明**：本页面基于 K-Dense 公开文档编写，与 Biostate AI 无官方合作关系。
> 
> **样本量计算**：计算结果仅供参考，实际样本量应结合预实验和领域专家意见确定。
> 
> 技术参考：K-Dense Beta - https://k-dense.ai  
> 最后更新：2026-04-18

---

## 📊 工具统计

<div style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 30px; border-radius: 12px; margin: 30px 0; text-align: center;">

### K-Dense 技能集统计

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; margin-top: 20px;">

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #667eea;">136</div>
<div style="color: #718096; margin-top: 5px;">总技能数</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #48bb78;">42</div>
<div style="color: #718096; margin-top: 5px;">生物信息学</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #ed8936;">28</div>
<div style="color: #718096; margin-top: 5px;">化学信息学</div>
</div>

<div style="background: white; padding: 20px; border-radius: 8px;">
<div style="font-size: 36px; font-weight: bold; color: #f56565;">24</div>
<div style="color: #718096; margin-top: 5px;">蛋白质组学</div>
</div>

</div>

</div>

---

**技术参考**：K-Dense Beta - https://k-dense.ai  
**合作案例**：哈佛医学院 David Sinclair 团队  
**最后更新**：2026-04-18

---

<script>
// 实验方案生成
function generateExperimentPlan() {
    const field = document.getElementById('research-field').value;
    const studyType = document.getElementById('study-type').value;
    const question = document.getElementById('research-question').value;
    const model = document.getElementById('model-system').value;
    const budget = document.getElementById('budget-range').value;
    const timeline = document.getElementById('timeline').value;
    
    if (!field || !studyType || !question) {
        alert('请填写完整的研究问题信息');
        return;
    }
    
    // 显示加载动画
    document.getElementById('plan-loading').style.display = 'block';
    document.getElementById('experiment-plan').style.display = 'none';
    
    // 模拟生成（实际应调用 K-Dense API 或本地分析）
    setTimeout(() => {
        document.getElementById('plan-loading').style.display = 'none';
        
        // 生成实验设计方案
        const plan = generatePlanContent(field, studyType, question, model, budget, timeline);
        
        document.getElementById('experiment-plan').innerHTML = plan;
        document.getElementById('experiment-plan').style.display = 'block';
        document.getElementById('experiment-plan').scrollIntoView({ behavior: 'smooth' });
    }, 2000);
}

// 生成计划内容
function generatePlanContent(field, studyType, question, model, budget, timeline) {
    const fieldNames = {
        'aging_biology': '衰老生物学',
        'senolytics': 'Senolytics',
        'nad': 'NAD+ 代谢',
        'epigenetics': '表观遗传学',
        'transcriptomics': '转录组学',
        'proteomics': '蛋白质组学',
        'metabolomics': '代谢组学',
        'clinical': '临床研究'
    };
    
    const modelNames = {
        'cell_line': '细胞系',
        'mouse': '小鼠',
        'rat': '大鼠',
        'non_human_primate': '非人灵长类',
        'human_cohort': '人类队列',
        'public_data': '公共数据库'
    };
    
    return `
        <div style="background: white; padding: 25px; border-radius: 8px; border-left: 4px solid #667eea;">
            <h3 style="margin-top: 0; color: #2d3748;">📋 实验设计方案</h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
                <div>
                    <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">研究领域</div>
                    <div style="font-weight: 600; color: #2d3748;">${fieldNames[field] || field}</div>
                </div>
                <div>
                    <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">研究类型</div>
                    <div style="font-weight: 600; color: #2d3748;">${studyType}</div>
                </div>
                <div>
                    <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">实验模型</div>
                    <div style="font-weight: 600; color: #2d3748;">${modelNames[model] || model}</div>
                </div>
                <div>
                    <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">预算范围</div>
                    <div style="font-weight: 600; color: #2d3748;">${budget}</div>
                </div>
            </div>
            
            <div style="margin: 20px 0;">
                <h4 style="color: #2d3748; margin-bottom: 10px;">🔬 研究问题</h4>
                <p style="color: #718096; line-height: 1.6;">${question}</p>
            </div>
            
            <div style="margin: 20px 0;">
                <h4 style="color: #2d3748; margin-bottom: 10px;">📝 建议实验流程</h4>
                <ol style="color: #718096; line-height: 2; padding-left: 20px;">
                    <li><strong>文献综述</strong>：使用 K-Dense 检索相关文献，建立研究背景</li>
                    <li><strong>预实验</strong>：小规模实验验证实验条件</li>
                    <li><strong>正式实验</strong>：按照标准化流程执行</li>
                    <li><strong>数据分析</strong>：使用 K-Dense 生物信息学技能进行分析</li>
                    <li><strong>验证实验</strong>：关键发现的独立验证</li>
                    <li><strong>论文撰写</strong>：K-Dense 辅助生成初稿</li>
                </ol>
            </div>
            
            <div style="margin: 20px 0;">
                <h4 style="color: #2d3748; margin-bottom: 10px;">💰 预算分配建议</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                    <div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
                        <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">试剂与耗材</div>
                        <div style="font-size: 18px; font-weight: bold; color: #667eea;">40-50%</div>
                    </div>
                    <div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
                        <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">测序与检测</div>
                        <div style="font-size: 18px; font-weight: bold; color: #667eea;">30-40%</div>
                    </div>
                    <div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
                        <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">动物饲养</div>
                        <div style="font-size: 18px; font-weight: bold; color: #667eea;">10-20%</div>
                    </div>
                    <div style="background: #f7fafc; padding: 15px; border-radius: 6px;">
                        <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">数据分析</div>
                        <div style="font-size: 18px; font-weight: bold; color: #667eea;">5-10%</div>
                    </div>
                </div>
            </div>
            
            <div style="margin: 20px 0; padding: 20px; background: #f0fff4; border-radius: 6px; border-left: 4px solid #48bb78;">
                <h4 style="margin-top: 0; color: #22543d;">💡 K-Dense 技能推荐</h4>
                <ul style="color: #276749; line-height: 1.8; margin: 10px 0; padding-left: 20px;">
                    <li><strong>文献综述</strong>：PubMed 检索、文献筛选、证据整合</li>
                    <li><strong>实验设计</strong>：样本量计算、随机化方案、对照设置</li>
                    <li><strong>数据分析</strong>：差异表达、通路富集、机器学习建模</li>
                    <li><strong>论文撰写</strong>：初稿生成、图表制作、参考文献管理</li>
                </ul>
            </div>
            
            <div style="margin-top: 20px; padding: 15px; background: #f7fafc; border-radius: 6px;">
                <p style="margin: 0; font-size: 13px; color: #718096;">
                    💡 <strong>提示</strong>：本方案基于 K-Dense 最佳实践生成。建议使用 K-Dense BYOK 版本执行详细分析。
                    <a href="https://k-dense.ai/" target="_blank" style="color: #667eea; font-weight: 500;">访问 K-Dense 官网</a>
                </p>
            </div>
        </div>
    `;
}

// 样本量计算
function calculateSampleSize() {
    const effectSize = parseFloat(document.getElementById('effect-size').value);
    const alpha = parseFloat(document.getElementById('alpha').value);
    const power = parseFloat(document.getElementById('power').value);
    
    if (!effectSize || !alpha || !power) {
        alert('请填写完整的参数');
        return;
    }
    
    // 简化的样本量计算公式（两样本 t 检验）
    // n = 2 * [(Zα + Zβ) * σ / δ]²
    // 其中 Zα 对应显著性水平，Zβ 对应统计效能
    
    const Z_alpha = alpha === 0.05 ? 1.96 : (alpha === 0.01 ? 2.576 : 1.645);
    const Z_beta = power === 0.8 ? 0.84 : (power === 0.9 ? 1.28 : 0.67);
    
    const n = 2 * Math.pow((Z_alpha + Z_beta) / effectSize, 2);
    const nPerGroup = Math.ceil(n / 2);
    const totalN = nPerGroup * 2;
    
    const resultDiv = document.getElementById('sample-size-result');
    resultDiv.style.display = 'block';
    
    resultDiv.innerHTML = `
        <h4 style="margin-top: 0; color: #2d3748;">📊 样本量计算结果</h4>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin: 20px 0;">
            <div style="background: white; padding: 20px; border-radius: 8px; text-align: center;">
                <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">每组样本量</div>
                <div style="font-size: 36px; font-weight: bold; color: #48bb78;">${nPerGroup}</div>
            </div>
            <div style="background: white; padding: 20px; border-radius: 8px; text-align: center;">
                <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">总样本量</div>
                <div style="font-size: 36px; font-weight: bold; color: #667eea;">${totalN}</div>
            </div>
            <div style="background: white; padding: 20px; border-radius: 8px; text-align: center;">
                <div style="font-size: 12px; color: #718096; margin-bottom: 5px;">效应量</div>
                <div style="font-size: 36px; font-weight: bold; color: #ed8936;">${effectSize}</div>
            </div>
        </div>
        
        <div style="padding: 15px; background: #f7fafc; border-radius: 6px; margin: 20px 0;">
            <h5 style="margin-top: 0; color: #2d3748;">📝 计算说明</h5>
            <ul style="color: #718096; line-height: 1.8; margin: 10px 0; padding-left: 20px;">
                <li>基于两样本 t 检验的样本量估算公式</li>
                <li>显著性水平 (α)：${alpha}（对应 Z 值：${Z_alpha.toFixed(3)}）</li>
                <li>统计效能 (1-β)：${power}（对应 Z 值：${Z_beta.toFixed(3)}）</li>
                <li>效应量 (Cohen's d)：${effectSize}（${effectSize < 0.3 ? '小' : (effectSize < 0.8 ? '中' : '大')}效应）</li>
            </ul>
        </div>
        
        <div style="padding: 15px; background: #fff5f5; border-left: 4px solid #f56565; border-radius: 6px;">
            <p style="margin: 0; font-size: 13px; color: #742a2a;">
                ⚠️ <strong>注意</strong>：此计算结果仅供参考。实际样本量应考虑预实验结果、预期脱落率、亚组分析需求等因素，并咨询统计学专家。
            </p>
        </div>
    `;
    
    resultDiv.scrollIntoView({ behavior: 'smooth' });
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
</script>
