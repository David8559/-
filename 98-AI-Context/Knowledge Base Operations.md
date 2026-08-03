---
type: ai-context
tags: [system/ai-context]
---

# Knowledge Base Operations

## Agent 操作规范

- 所有读取、引用、修改和完善操作必须遵守 [[数学建模知识库阅读与修改规范]]。
- 根入口规则见 [[AGENTS|98-AI-Context/AGENTS]]；具体项目还必须阅读其 `Project-Status.md`。

## 常用命令

- 清洗：Run-Research-Cleaner.ps1 -Promote
- Inbox 可搜索索引：python build_inbox_search_index.py
- 图谱：python knowledge_graph.py
- 代码验证汇总：python audit_code_validation.py
- MATLAB 正式库复测：在 `04-Research/03-建模算法源码库/03-验证测试` 中运行 `matlab -batch "run_matlab_validation"`
- 巡检：python kb_audit.py
- 全维护：Run-Maintenance.ps1
- Git 同步：Sync-Vault.ps1

所有命令位于 98-AI-Context/Automation。
