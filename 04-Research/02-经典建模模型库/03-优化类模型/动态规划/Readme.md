---
type: research-method
status: active
topic: 动态规划
updated: 2026-07-26
tags: [area/数学建模, topic/优化模型, method/动态规划]
---

# 动态规划

> [!summary] 30 秒复习
> 动态规划把多阶段决策拆成重叠子问题，保存状态最优值并按 Bellman 原理递推。最难的是状态是否包含未来决策需要的全部信息。

## 基本结构

有限期最小化常写为：

$$V_t(s)=\min_{a\in A(s)}
\{g_t(s,a)+V_{t+1}(T(s,a))\}.$$

必须具备最优子结构；状态压缩不能丢掉影响后续转移或成本的信息。

## 建模步骤

1. 定义阶段 $t$、状态 $s$、动作 $a$、转移 $T$ 和阶段收益/成本。
2. 写边界条件，再写状态转移方程。
3. 选择自顶向下记忆化或自底向上递推。
4. 保存前驱/动作以回溯具体方案，不只算最优值。
5. 用小规模穷举校验；分析时间与空间复杂度。

## 代码入口

- [Python：`zero_one_knapsack`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/optimization_models.py)
- [MATLAB：`optimization_network_models("knapsack", ...)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

## 常见错误

- 状态定义不充分，转移隐含依赖被丢失；边界或遍历方向错。
- 只返回数值不回溯方案；滚动数组优化后破坏回溯信息。
- 状态维数过多导致“维数灾难”，却没有剪枝、近似或重新建模。

## 来源

- [MIT 6.006：动态规划、记忆化与最短路](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-19-dynamic-programming-i-fibonacci-shortest-paths/)
- [MIT 6.231：Bellman 原理与通用 DP](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/pages/lecture-notes/)

## 关联

[[动态规划 Hub]] · [[优化模型 Hub]] · [[04-Research/02-经典建模模型库/04-图论与网络模型/最短路径/Readme|最短路径]] · [[04-Research/02-经典建模模型库/03-优化类模型/整数规划与0-1规划/Readme|整数规划与0-1规划]]
