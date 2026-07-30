---
type: ai-memory
tags: [system/ai-memory]
---

# Workflows

- [[Research Collection Workflow]]
- [[Knowledge Base Operations]]
- [[Project Status Index]]
- 网页验收链路：Web Clipper → `00-Inbox/Downloaded` → Research Cleaner → 单一 Research 主分类 → Topic Hub → Knowledge Base Audit → GitHub。
- 竞赛资料链路：Inbox → 文本层/扫描检测 → OCR + 视觉复核 → 赛题/数据/获奖论文唯一主分类 → 横向比较 → 项目复现 → Topic Hub → Git LFS/GitHub。
- 代码资料链路：Downloaded 原件 → 文件清单 → 代码证据优先的算法识别 → SHA-256 精确去重 → 相似实现聚类 → 在原有领域 Hub 顶部生成复习卡 → 为每个实现生成理解与调用卡 → Python/MATLAB Hub 只建导航 → 项目最小样例与结果验证。配套数据继续保存在本地 Vault，但不在复习页展开依赖明细。
- AI Agent 竞赛链路：官方规则与 AI 合规检查 → 标准项目骨架 → 读题拆题 → 选题与风险门 → 数据审计 → 基线与候选模型 → 最小实现 → 正式实验 → 检验与独立复跑 → 证据驱动写作 → 独立审稿 → 提交冻结与回执 → 项目复盘和 Research 沉淀。详细操作见 [[04-Research/04-竞赛真题研究/Readme#AI Agent 驱动的数学建模竞赛全流程|AI Agent 驱动的竞赛全流程]]。

## 数学建模竞赛启动顺序

1. 用 [[数学建模竞赛项目启动模板]] 建立唯一项目现场并登记官方规则、截止时间和 AI 合规边界；
2. 将 [[数学建模竞赛阶段门模板]] 复制到项目中，状态统一使用“未开始、进行中、待人工确认、已通过、阻塞”；
3. 每个阶段用 [[AI Agent Task Template]] 新建一个边界明确、可验收的独立任务；
4. 每 3–4 小时把已完成、当前证据、最大风险、下一步唯一动作、负责人和预计完成时间写回 `Project-Status.md`；
5. 写作阶段读取 [[论文写作 Hub]]，只依据已验证公式、代码、结果、图表和引用写作；
6. 提交前完成问题、数学、证据和交付四层审计，冻结论文、代码、附件和版本标识并保存回执；
7. 赛后将通用模型、代码、检验、写作方法和经验分别沉淀到 Research Hub、Best Practices、Lessons Learned 和本文件。
