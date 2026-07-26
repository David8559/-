---
type: research-method
status: active
topic: 多目标规划
updated: 2026-07-26
tags: [area/数学建模, topic/优化模型, method/多目标优化]
---

# 多目标规划

> [!summary] 30 秒复习
> 多目标问题通常没有唯一“最优”，而是一组不能在不损害其他目标的情况下继续改进的 Pareto 解。先统一方向和尺度，再选择权重法、$\varepsilon$-约束或进化算法。

## 核心概念

$$\min_x F(x)=(f_1(x),\ldots,f_m(x)),\qquad x\in\Omega.$$

若不存在 $x$ 使所有目标不差且至少一个严格更好，则 $x^\*$ 为 Pareto 最优。加权和：

$$\min_x\sum_j w_j\tilde f_j(x),\quad w_j\ge0,\ \sum_jw_j=1,$$

其中 $\tilde f_j$ 应先按理想/最差值归一化。

## 建模步骤

1. 明确每个目标的方向、单位和决策含义；区分目标与硬约束。
2. 单目标分别求解，获得理想点、尺度和冲突程度。
3. 生成 Pareto 候选：权重扫描、$\varepsilon$-约束或 NSGA-II。
4. 画 Pareto 前沿，剔除被支配解；再依据偏好选折中点。
5. 对权重/阈值和数据扰动检查折中方案稳定性。

## 代码入口

- [Python：`weighted_sum_multiobjective`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/optimization_models.py)
- [MATLAB：`optimization_network_models("weighted-sum", ...)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

复杂非凸前沿可参考 [pymoo 官方 GitHub](https://github.com/anyoptimization/pymoo) 的 NSGA-II/III 等算法。

## 常见错误

- 未归一化就加权，结果被数量级最大目标支配。
- 把任意一个加权结果称为“全局最优”；不展示目标之间的代价交换。
- 先由结果反推权重，却称权重为事前偏好。

## 来源

- [pymoo 文档：多目标算法与 Pareto 分析](https://pymoo.org/)
- Blank & Deb (2020), “pymoo: Multi-Objective Optimization in Python”, *IEEE Access*。

## 关联

[[优化模型 Hub]] · [[智能优化 Hub]] · [[04-Research/02-经典建模模型库/01-评价类模型/TOPSIS优劣解距离法/Readme|TOPSIS优劣解距离法]]
