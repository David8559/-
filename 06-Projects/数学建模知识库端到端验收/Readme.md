---
type: project-home
status: active
created: "2026-07-14"
tags: [project/active]
---

# 数学建模知识库端到端验收

- 状态：[[Project-Status]]
- 代码：Code/
- 数据：Data/
- 论文：Paper/

## 目标与验收标准

目标：验证 AI Native Obsidian 知识库从真实网页采集到 GitHub 远端同步的完整链路。

- [x] Web Clipper 将网页原文写入 `00-Inbox/Downloaded`
- [x] Cleaner 在不删减、不总结、不改写观点的前提下生成清洗副本
- [x] 资料只有一个 Research 主分类，同时拥有多个主题标签和 Hub 链接
- [x] Knowledge Graph 与 Knowledge Base Audit 正常运行
- [ ] GitHub `main` 与本地 HEAD 一致

## 交付物

- 原始网页抓取：[[00-Inbox/Downloaded/【数学建模入门】保姆级小白教程，没学过建模的看完这篇也能提交竞赛论文！]]
- 清洗副本：[[00-Inbox/Cleaned/【数学建模入门】保姆级小白教程，没学过建模的看完这篇也能提交竞赛论文！]]
- Research 正式笔记：[[04-Research/01-建模基础理论/【数学建模入门】保姆级小白教程，没学过建模的看完这篇也能提交竞赛论文！]]
- 主题图谱：[[04-Research/00-Topic-Hubs/Topic Index]]
- 巡检报告：[[98-AI-Context/Knowledge Base Audit Report]]

## 复现方式

1. 用 Web Clipper 的“数学建模”模板抓取网页。
2. 运行 `98-AI-Context/Automation/Run-Research-Cleaner.ps1 -Promote`。
3. 运行 `98-AI-Context/Automation/Run-Maintenance.ps1`。
4. 核对 Git 状态并推送 `main`。
