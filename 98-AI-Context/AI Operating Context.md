---
type: ai-context
tags: [system/ai-context]
---

# AI Operating Context

Agent 每次工作前阅读 `98-AI-Context/AGENTS.md`、`About Me.md`、`Current Focus.md` 和目标项目的 `Project-Status.md`。只将稳定经验、决策、工作流、项目进展写入长期记忆；不要保存聊天记录。

## 低 Token 默认工作方式

- Vault 文件是长期状态源，聊天记录不是。新阶段优先新建独立任务，并从 `Project-Status.md` 恢复状态。
- 使用 [[AI Agent Task Template]] 明确单次任务、交付物和验收标准；一个任务只处理一个清晰阶段。
- 先搜索、后读取；先读取相关片段，证据不足时再扩展到全文、原始 PDF、视频或数据。
- 已有 OCR、清洗稿、代码结果、图表说明和论文拆解优先复用，不进行无理由的重复提取。
- 任务结束前更新项目状态、下一步、风险和决策，让后续 Agent 无需读取旧对话即可接续。

用户已对本 Vault 的常规 GitHub 自动同步给出持续授权：任务完成并通过验证后，可提交并推送到 `origin/main`。若存在混合来源改动、冲突、敏感信息、异常大文件、远端异常或验证失败，停止自动同步并向用户报告；不得强制推送或改写历史。Obsidian Git 负责日常自动备份，重大代码或论文改版仍可使用独立分支和 PR。
