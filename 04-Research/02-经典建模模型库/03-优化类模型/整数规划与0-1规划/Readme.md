---
type: research-method
status: active
topic: 整数规划与0-1规划
updated: 2026-07-26
tags: [area/数学建模, topic/优化模型, method/MILP]
---

# 整数规划与0-1规划

> [!summary] 30 秒复习
> 当数量必须为整数或决策是“选/不选”时使用 MILP。核心是用紧凑线性约束表达逻辑；不能把 LP 连续解简单四舍五入。

## 模型

$$\min c^\mathsf Tx,\qquad
b_l\le Ax\le b_u,\quad l\le x\le u,\quad x_i\in\mathbb Z.$$

二元变量 $y\in\{0,1\}$ 可表达启用、互斥、蕴含和固定成本。Big-M 必须尽量紧，过大会削弱松弛并导致数值问题。

## 建模步骤

1. 区分连续、整数和二元变量，给出明确上下界。
2. 用二元变量表达选择/逻辑；优先使用紧界、指示约束或凸包形式。
3. 先解 LP 松弛检查模型方向和上/下界。
4. 求解 MILP，记录求解状态、最优间隙、时间/节点上限。
5. 对整数性、约束和目标值逐项回代；比较启发式可行解。

## 代码入口

- [Python：`solve_milp`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/optimization_models.py)
- [MATLAB：`optimization_network_models("milp", ...)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

## 常见错误

- 四舍五入连续解后不再可行；二元变量仅声明为整数却没设 $[0,1]$。
- Big-M 随手取极大值；遗漏“至多/至少/恰好一个”的方向。
- 到时限的可行解写成“已证最优”，却不报告 MIP gap。

## 来源

- [SciPy `milp` 官方文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html)
- [MATLAB `intlinprog` 官方文档](https://www.mathworks.com/help/optim/ug/intlinprog.html)

## 关联

[[优化模型 Hub]] · [[04-Research/02-经典建模模型库/03-优化类模型/线性规划/Readme|线性规划]] · [[04-Research/02-经典建模模型库/03-优化类模型/动态规划/Readme|动态规划]] · [[04-Research/02-经典建模模型库/03-优化类模型/启发式与贪心方法/Readme|启发式与贪心方法]]
