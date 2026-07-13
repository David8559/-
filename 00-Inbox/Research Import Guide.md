---
type: guide
tags: [workflow/research-import, system/inbox]
---

# Research Import Guide

1. 网页资料优先用 Obsidian Web Clipper 的 `Research Capture` 模板保存到 `00-Inbox/Downloaded`。
2. MarkDownload 导出的 `.md` 与图片也放入 `00-Inbox/Downloaded`；不要直接放入 Research。
3. PDF、数据压缩包等原始附件放入 `00-Inbox/Attachments`，在 Markdown 中记录来源和对应关系。
4. 运行 `98-AI-Context/Automation/Run-Research-Cleaner.ps1`，清洗副本进入 `00-Inbox/Cleaned`。
5. 原始文件始终保留；确认分类后再把清洗版提升到 `04-Research`。

必需元数据：标题、来源 URL、作者（未知可空）、发布日期/抓取时间、主分类、主题标签。
