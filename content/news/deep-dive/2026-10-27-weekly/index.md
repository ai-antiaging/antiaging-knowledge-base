---
title: "周深度解读 · 2026-10-27"
date: 2026-10-27
description: "One-shot learning of paired association navigation with biologically plausible schemas...."
draft: false
type: "deep-dive"
---

# 📚 周深度解读 · 2026-10-27

> **The Journal of neuroscience : the official journal of the Society for Neuroscience** · PMID: [42933903](https://pubmed.ncbi.nlm.nih.gov/42933903/)

---

**论文标题**: One-shot learning of paired association navigation with biologically plausible schemas.

**期刊**: The Journal of neuroscience : the official journal of the Society for Neuroscience

**发表日期**: 2026 Oct 26

**DOI**: [](https://doi.org/)

---

## 研究背景
啮齿动物在掌握多重配对关联（MPA）导航任务后，仅需单次暴露即可快速习得新的线索-位置关联，这一现象被认为由“认知图式”驱动。然而，图式的具体内容及其在生物神经网络中的实现机制长期不明，是连接行为学与计算神经科学的关键缺口。

## 核心问题
哪些图式足以支撑从渐进学习到“一次性”配对关联导航？这些图式能否用生物合理的突触可塑性规则在全神经网络智能体中实现？

## 方法与数据
研究采用计算建模方法，构建了一个完全神经网络智能体，包含三个核心网络：基于路径积分时间差分误差的低维空间度量表征网络、采用奖励调制探索性Hebbian可塑性的记忆网络（实现线索-目标一次性关联）、以及通过向量减法计算目标导向动作的网络。另辅以actor-critic模块和经时间差分误差学习的工作记忆门控机制。模型行为与啮齿动物MPA任务数据进行了比对验证。

## 关键发现
所提图式集合足以复现“先渐进、后一次性”的学习曲线。记忆网络借助奖励调制EH可塑性，在单次线索-目标配对后即形成关联；向量减法网络支持跨环境自定位与目标导向行动。补充actor-critic后可一次性绕障导航；学习工作记忆门控后，即使线索和干扰物短暂呈现仍能一次性学习。模型复现了啮齿动物MPA任务的关键行为特征，并生成关于图式性一次性学习神经机制的可检验预测。

## 局限性
研究为计算建模，尚未在活体动物中进行实验验证；所提预测仍需电生理或干预实验检验；模型对真实神经回路细节做了简化。

## 领域意义
该工作将“认知图式”从抽象心理学概念转化为可实现的神经计算架构，为理解衰老过程中一次性学习能力下降的回路基础提供框架。对临床而言，奖励调制Hebbian可塑性与工作记忆门控的失效机制，或可解释早期认知衰退中情境适应困难，并为靶向干预提供计算假设。🧠

---

*自动生成 · 最后更新：2026-10-27 07:32*

 [← 返回周深度解读列表](../)
