---
type: template
status: active
created: 2026-07-30
updated: 2026-07-30
tags: [system/template, workflow/agent, workflow/low-token]
---

# AI Agent Task Template

> [!summary] 用途
> 用于为 Codex、Claude Code、Cursor 等 Agent 新建独立任务。项目文件负责交接状态，不依赖旧聊天记录。

## 可直接复制的任务提示词

```text
Vault：
C:\Users\17888\Documents\0.数学建模知识库\0.数学建模

项目：
06-Projects/<项目名>

请先读取：
1. AGENTS.md
2. 98-AI-Context/AGENTS.md
3. 98-AI-Context/AI Operating Context.md
4. <项目>/Project-Status.md
5. <项目>/Readme.md 中与本次任务相关的章节

本次任务：
<只写一个明确阶段或一项工作>

允许修改：
<文件或目录范围>

不要执行：
<删除原始资料、改动无关文件、上传隐私等边界>

交付物：
<明确的文件、代码、图表、分析或论文章节>

验收标准：
<可运行、误差阈值、图表要求、引用要求、结构要求等>

结束前：
1. 验证本次交付物；
2. 更新 Project-Status.md 的已完成事项、待办事项、下一步、风险和决策；
3. 按 Vault 规则处理 GitHub 同步。

不要读取无关历史。先搜索后读取，只读取完成任务所需的相关片段；证据不足时再扩展。
```

## 无具体竞赛项目时

将“项目”改为目标知识库目录，并把交付状态写入对应的权威笔记。维护类任务仍需明确修改范围与验收标准。

## 填写原则

- 一次任务只写一个阶段，例如“复核问题四的几何碰撞算法”，不要只写“继续”。
- 交付物使用可验证的文件路径或结果，不使用“完善一下”等模糊描述。
- 大型论文、PDF、视频和数据默认按需读取；已有提取结果优先复用。
- 新阶段另建任务，上一阶段的结论必须先写回项目状态。

## 相关规则

- [[98-AI-Context/AGENTS|AI Agent Operating Rules]]
- [[AI Operating Context]]
- [[数学建模知识库阅读与修改规范]]
