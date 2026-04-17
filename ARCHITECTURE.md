# 网站架构文档

> **版本**：2.0  
> **更新日期**：2026-04-18  
> **架构师**：抗衰小杨 · JVS Claw AI

---

## 📐 架构概览

```
┌─────────────────────────────────────────────────────────────┐
│                     抗衰老科学前沿知识库                      │
│                   Hugo 静态网站架构 v2.0                      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   内容源        │     │   构建系统       │     │   部署平台      │
│                 │     │                  │     │                 │
│ • Markdown      │────▶│   Hugo SSG       │────▶│   GitHub Pages  │
│ • Front Matter  │     │   • 模板渲染     │     │   • CDN 分发    │
│ • 配置文件      │     │   • 资源优化     │     │   • HTTPS       │
│                 │     │   • SEO 生成      │     │                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   内容管理      │     │   CI/CD 流程      │     │   监控告警      │
│                 │     │                  │     │                 │
│ • Git 版本控制  │     │ • GitHub Actions │     │ • Lighthouse    │
│ • 定时任务      │     │ • 自动部署       │     │ • 链接检查      │
│ • AI 生成       │     │ • 质量检查       │     │ • SEO 审计       │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

---

## 🏗️ 目录结构

```
antiaging-site/
├── config/                 # 配置文件
│   └── _default/
│       ├── hugo.toml      # 主配置
│       ├── params.toml    # 站点参数
│       ├── markup.toml    # Markdown 渲染
│       ├── outputs.toml   # 输出格式
│       ├── permalinks.toml# 永久链接
│       ├── sitemap.toml   # Sitemap 配置
│       └── robots.toml    # Robots 配置
│
├── content/               # 内容目录
│   ├── _index.md         # 首页内容
│   ├── basics.md         # 基础理论
│   ├── interventions.md  # 干预方法
│   ├── research.md       # 研究前沿
│   ├── recent.md         # 近一月研究
│   ├── metabolism.md     # 代谢网络
│   └── about.md          # 关于本站
│
├── layouts/               # 模板目录
│   ├── _default/
│   │   ├── baseof.html   # 基础模板
│   │   ├── single.html   # 单页模板
│   │   ├── list.html     # 列表模板
│   │   └── sitemap.xml   # Sitemap 模板
│   ├── partials/
│   │   ├── header.html   # 页头
│   │   ├── navigation.html # 导航
│   │   ├── breadcrumbs.html # 面包屑
│   │   ├── toc.html      # 目录
│   │   ├── meta-info.html # 元信息
│   │   ├── footer.html   # 页脚
│   │   └── performance-hints.html # 性能提示
│   └── index.html        # 首页模板
│
├── static/               # 静态资源
│   └── robots.txt       # Robots 文件
│
├── .github/
│   └── workflows/       # GitHub Actions
│       ├── hugo.yml          # 部署工作流
│       ├── seo-audit.yml     # SEO 审计
│       ├── broken-links.yml  # 链接检查
│       └── performance-monitor.yml # 性能监控
│
├── themes/              # 主题（自定义）
├── hugo.toml           # Hugo 主配置
└── ARCHITECTURE.md     # 本文档
```

---

## 🔧 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| **静态生成** | Hugo v0.160+ | Go 语言编写，极速构建 |
| **模板引擎** | Go Templates | Hugo 内置模板系统 |
| **样式** | CSS3 | 自定义样式，无框架依赖 |
| **部署** | GitHub Pages | 免费 CDN，自动 HTTPS |
| **CI/CD** | GitHub Actions | 自动化部署和检查 |
| **监控** | Lighthouse CI | 性能和质量监控 |
| **内容** | Markdown | 易读易写的标记语言 |

---

## 📊 性能指标目标

| 指标 | 目标值 | 当前值 | 状态 |
|------|-------|-------|------|
| **Lighthouse Performance** | ≥90 | 待测 | 🟡 |
| **Lighthouse Accessibility** | ≥90 | 待测 | 🟡 |
| **Lighthouse Best Practices** | ≥90 | 待测 | 🟡 |
| **Lighthouse SEO** | ≥90 | 待测 | 🟡 |
| **First Contentful Paint** | <1.5s | 待测 | 🟡 |
| **Time to Interactive** | <3.5s | 待测 | 🟡 |
| **Total Blocking Time** | <200ms | 待测 | 🟡 |
| **Cumulative Layout Shift** | <0.1 | 待测 | 🟡 |

---

## 🔐 安全策略

### 内容安全策略 (CSP)

```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:;">
```

### HTTPS 强制

GitHub Pages 自动提供 HTTPS，无需额外配置。

### 依赖检查

每周自动检查依赖漏洞：

```yaml
# .github/workflows/security.yml
name: Security Audit
on:
  schedule:
    - cron: '0 0 * * 0'  # 每周日
```

---

## 📈 监控体系

### 1. 性能监控

- **频率**：每 6 小时
- **工具**：Lighthouse CI
- **指标**：Performance、Accessibility、Best Practices、SEO
- **告警**：指标低于阈值时创建 Issue

### 2. 链接检查

- **频率**：每天
- **工具**：lychee
- **范围**：内部链接 + 外部链接
- **告警**：发现死链时创建 Issue

### 3. SEO 审计

- **频率**：每周
- **工具**：Lighthouse CI
- **检查项**：Meta 标签、结构化数据、Sitemap

---

## 🔄 CI/CD 流程

```
代码提交 → Git Push → GitHub Actions
                              │
                              ▼
                    ┌─────────────────┐
                    │   Hugo 构建     │
                    │  • 安装 Hugo    │
                    │  • 安装主题     │
                    │  • 生成静态文件 │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   质量检查      │
                    │  • Lighthouse   │
                    │  • 链接检查     │
                    │  • SEO 审计     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   部署          │
                    │  • 上传产物     │
                    │  • 更新 Pages   │
                    │  • 清除缓存     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   通知          │
                    │  • 成功：忽略   │
                    │  • 失败：Issue  │
                    └─────────────────┘
```

---

## 📝 内容规范

### Front Matter 标准

```yaml
---
title: "页面标题"
description: "页面描述（用于 SEO）"
date: 2026-04-18
draft: false
keywords: ["关键词 1", "关键词 2"]
sitemap:
  priority: 0.8
  changefreq: weekly
---
```

### 内容结构

1. **标题**：使用 H1，每页唯一
2. **副标题**：H2-H6 层级清晰
3. **列表**：优先使用无序列表
4. **表格**：包含表头，数据对齐
5. **引用**：使用 blockquote，标注来源
6. **代码**：使用 code 块，指定语言

---

## 🎯 优化清单

### 已完成 ✅

- [x] 模块化布局（partials）
- [x] SEO Meta 标签
- [x] 面包屑导航
- [x] 目录生成（TOC）
- [x] 响应式设计
- [x] Sitemap 生成
- [x] Robots.txt 配置
- [x] CI/CD 自动化
- [x] 性能监控
- [x] 链接检查

### 待完成 🔄

- [ ] 搜索功能（Fuse.js）
- [ ] 暗色模式
- [ ] 阅读进度条
- [ ] 社交分享
- [ ] 评论系统（可选）
- [ ] 分析工具集成
- [ ] PWA 支持
- [ ] RSS 订阅优化

---

## 📞 维护指南

### 日常维护

1. **内容更新**：编辑 Markdown → Git Push → 自动部署
2. **配置修改**：修改 config/ → Git Push → 自动部署
3. **模板更新**：修改 layouts/ → Git Push → 自动部署

### 故障排查

1. **构建失败**：检查 Actions 日志
2. **页面 404**：检查文件路径和 Front Matter
3. **样式异常**：清除浏览器缓存
4. **性能下降**：查看 Lighthouse 报告

### 版本升级

1. **Hugo 升级**：更新 `.github/workflows/hugo.yml` 中的版本号
2. **依赖升级**：运行 `hugo mod get -u`
3. **配置迁移**：参考 Hugo 官方迁移指南

---

*最后更新：2026-04-18 | 维护者：抗衰小杨 · JVS Claw AI*
