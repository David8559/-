# AI Agent Operating Rules

## Mission

Maintain this Vault as a reproducible mathematical-modeling knowledge system for Obsidian, GitHub, Codex, Claude Code, Cursor, Python, and MATLAB workflows.

## Read before acting

1. `98-AI-Context/About Me.md`
2. `98-AI-Context/Current Focus.md`
3. `98-AI-Context/AI Operating Context.md`
4. `98-AI-Context/数学建模知识库阅读与修改规范.md`
5. The active project's `06-Projects/<name>/Project-Status.md`

Before editing, inspect `git status`, search for existing notes with `rg`, and prefer extending the canonical note over creating a duplicate.

## Token-efficient context loading

- Treat Vault files as the source of truth. Do not reconstruct project state from a long chat transcript.
- Read the operating-rule files once at task startup. Search with `rg` before opening domain notes or project artifacts.
- For a large `Project-Status.md` or project `Readme.md`, initially read frontmatter, headings, current status, completed work, tasks, next step, risks, decisions, and the sections directly relevant to the requested deliverable.
- Expand to the full file, source paper, dataset, PDF, or video only when the current evidence is insufficient.
- Reuse existing extraction, OCR, cleaned notes, code results, and figure explanations; do not repeat expensive extraction without a stated reason.
- Keep tool output bounded, avoid reopening unchanged files, and finish by updating the authoritative project state so the next task can start without old conversation history.

## Write rules

- Never store raw chat logs.
- Store only durable decisions, reusable lessons, proven workflows, project state, or stable user preferences.
- One note has one primary folder/category; connect other meanings with `topic/*`, `tool/*`, `workflow/*` tags and wiki links.
- Do not overwrite raw imports in `00-Inbox/Downloaded`.
- Research Cleaner may change structure and metadata but must not delete, summarize, or rewrite source claims.
- Every research claim needs a source; every code result needs environment, data, parameters, and reproduction steps.
- Every project must contain `Project-Status.md` and keep status, completed work, tasks, next step, risks, and decisions current.
- Use UTF-8 Markdown, preserve valid YAML frontmatter, and use Obsidian wiki links for internal relationships.
- Distinguish sourced facts, computed results, assumptions, and Agent inference. Never invent a source, formula result, experiment, or validation outcome.
- For mathematical models, record variables, units, assumptions, equations, data provenance, parameters, environment, validation, error or sensitivity analysis, limitations, and reproduction steps as applicable.
- Make the smallest coherent change. Do not rename, move, delete, bulk-rewrite, change `.obsidian`, commit, or push unless the user explicitly authorizes that operation.
- Treat `00-Inbox/Downloaded` and original datasets, papers, images, and other source artifacts as immutable. Create a cleaned or derived copy instead.
- After structural or bulk changes, run the Vault audit and report changed files, validation performed, and unresolved risks.

## Memory routing

- Decisions → `97-AI-Memory/Decisions.md`
- Reusable practices → `97-AI-Memory/Best Practices.md`
- Failures and prevention → `97-AI-Memory/Lessons Learned.md`
- Reusable procedures → `97-AI-Memory/Workflows.md`
- Project progress → project `Project-Status.md`
- Stable operating context → the matching file under `98-AI-Context`

Run the maintenance scripts after bulk imports or structural changes.
