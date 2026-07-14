---
type: ai-memory
tags: [system/ai-memory]
---

# Best Practices

- 原始资料不可被 Cleaner 覆盖。
- 代码、数据、环境与输出共同构成可复现单元。
- 模型结论必须同时记录适用条件、误差和检验。
- Web Clipper 必须绑定 Vault 的精确名称或唯一 ID；目录只填写 Vault 内相对路径。
- Raw、Cleaned、Research 是可追溯生命周期，只有 Research 副本作为主分类笔记参与重复内容判定。
- 综合入门资料先按标题语义确定主分类，再用 Topic 标签表达工具、模型与写作等交叉主题。
- 扫描型竞赛论文先做文本层检测；无文本层时必须结合 OCR 与关键页面视觉复核，公式和数值不能只信 OCR。
- 赛题、数据附件、获奖论文分别采用唯一主分类，用题目总览和项目页建立横向链接。
- 大体积 PDF 使用 Git LFS，避免二进制历史进入普通 Git 对象库。
