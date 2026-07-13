---
type: ai-memory
tags: [system/ai-memory]
---

# Lessons Learned

只记录可跨任务复用的失败模式、根因、修复和预防措施。

- PowerShell 变量名不区分大小写，项目脚本中的 `$Home` 会与只读 `$HOME` 冲突；脚本变量应使用明确的业务名称，例如 `$ProjectHome`。
- 只按正文关键词计数会把综合入门文章误判为竞赛真题；高置信标题意图应优先于正文中的泛化关键词。
- Web Clipper 报 `Vault not found` 时，先核对 URI 是否包含 `vault`，并使用 Obsidian 注册表中的精确 Vault 名称或 ID。
