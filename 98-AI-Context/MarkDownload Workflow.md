---
type: workflow
tags: [workflow/markdownload, workflow/research-import]
---

# MarkDownload Workflow

```mermaid
flowchart LR
    A[MarkDownload] --> B[00-Inbox/Downloaded]
    B --> C[Research Cleaner]
    C --> D[00-Inbox/Cleaned]
    D --> E[04-Research]
    E --> F[Topic Hub]
```

## MarkDownload 设置

- 下载目录：`C:\Users\17888\Documents\0.数学建模知识库\0.数学建模\00-Inbox\Downloaded`
- 文件名：使用网页标题，避免仅日期或随机 ID。
- Frontmatter 至少包含 `title`、`source`、`author`、`published`、`captured`。
- 图片若不能下载到同目录，先进入 `00-Inbox/Attachments`，再由研究笔记引用。

## 执行

运行 `98-AI-Context/Automation/Run-Research-Cleaner.ps1`。默认只生成清洗副本并建议分类；加 `-Promote` 时才复制到 Research。原始文件永不覆盖。
