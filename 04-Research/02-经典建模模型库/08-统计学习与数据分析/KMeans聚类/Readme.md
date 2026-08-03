---
type: model-card
status: reviewed-theory
created: 2026-08-03
updated: 2026-08-03
tags: [area/数学建模, topic/统计学习, model/KMeans]
topic_hubs: [统计学习 Hub, 数据处理 Hub]
---

# KMeans 聚类

## 目标与假设

把 $n$ 个样本划分为 $K$ 个簇，最小化簇内平方和 $\sum_{k=1}^K\sum_{x_i\in C_k}\lVert x_i-\mu_k\rVert^2$。它隐含欧氏距离有意义、簇近似凸且尺度相近。非球形簇、强离群点、类别密度差异大时不应硬套。

## 标准流程

字段审计 → 训练集拟合标准化 → 用肘部法/轮廓系数和业务解释提出 K 候选 → `k-means++` 多次初始化 → 比较目标值和簇稳定性 → 用中心、规模和特征分布解释每簇。

## 必做检验

- 报告是否标准化、距离、K、初始化次数和随机种子。
- 比较多个 K，而不是只展示最漂亮的二维图。
- 重抽样或多种子后，用调整兰德指数/中心漂移检查稳定性。
- 检查离群点和空簇；PCA 图只用于展示，不能替代原空间评价。

## 代码与论文

Python 优先 `sklearn.cluster.KMeans`；自动 Hub 中的原始实现未全部运行，正式项目先用合成簇检查标签置换、中心和目标函数。论文应写“发现何种群组、群组如何影响决策”，而非把标签编号当作自然等级。

## 来源与链接

- MacQueen J. Some methods for classification and analysis of multivariate observations. 1967.
- Rousseeuw P J. Silhouettes. *Journal of Computational and Applied Mathematics*, 1987.
- [[统计学习 Hub]]；[[模型检验实战清单]]。
