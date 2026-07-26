---
type: research-method
status: active
topic: 线性规划
updated: 2026-07-26
tags: [area/数学建模, topic/优化模型, method/线性规划]
---

# 线性规划

> [!summary] 30 秒复习
> 线性规划在目标、约束和变量关系均线性时求全局最优。建模质量取决于变量、单位、方向与约束是否完整；求解器成功不代表现实模型正确。

## 标准形式

$$\min_x c^\mathsf T x,\qquad
A_{ub}x\le b_{ub},\quad A_{eq}x=b_{eq},\quad l\le x\le u.$$

最大化可最小化 $-c^\mathsf Tx$。影子价格/对偶变量用于解释资源边际价值，但只在当前基与局部扰动范围内成立。

## 建模步骤

1. 逐个定义决策变量、索引、单位和上下界。
2. 写目标函数；逐条把自然语言规则翻译为约束并检查方向。
3. 做量纲和数量级检查，设置紧而合理的边界。
4. 求解后检查状态、约束违反量、松弛变量和目标值回算。
5. 对关键资源、价格与容量做敏感性/情景分析。

## 代码入口

- [Python：`solve_linear_program`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/optimization_models.py)
- [MATLAB：`optimization_network_models("lp", ...)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

## 常见错误

- 最大化忘记取负；`>=` 约束未转向；变量默认非负与题意冲突。
- 漏掉守恒、容量或互斥约束，得到“数学上最优、现实中不可行”方案。
- 系数量级差异过大导致数值病态；只给解不做约束回代。

## 来源

- [SciPy `linprog` 官方文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)
- [MATLAB `linprog` 官方文档](https://www.mathworks.com/help/optim/ug/linprog.html)

## 关联

[[优化模型 Hub]] · [[04-Research/02-经典建模模型库/03-优化类模型/整数规划与0-1规划/Readme|整数规划与0-1规划]] · [[04-Research/02-经典建模模型库/03-优化类模型/多目标规划/Readme|多目标规划]] · [[模型检验 Hub]]
