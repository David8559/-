# Vault Agent Entry Point

All AI agents must follow [[98-AI-Context/AGENTS|98-AI-Context/AGENTS.md]] and [[数学建模知识库阅读与修改规范]]. Read [[AI Operating Context]] before changing this Vault.

## Low-token startup

1. Search before reading; do not scan the whole Vault by default.
2. Treat the active project's `Project-Status.md` as the authoritative handoff, not chat history.
3. For large project files, first read frontmatter, headings, current status, next step, risks, decisions, and the sections relevant to the task. Expand only when evidence is missing.
4. Do not reread an unchanged file within the same task.
5. Keep one task scoped to one clear deliverable, then write durable progress back to the project state.
