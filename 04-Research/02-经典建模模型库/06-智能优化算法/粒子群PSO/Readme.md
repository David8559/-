---
type: research-method
status: active
topic: 粒子群PSO
updated: 2026-07-26
tags: [area/数学建模, topic/智能优化, method/PSO]
---

# 粒子群PSO

> [!summary] 30 秒复习
> PSO 用粒子位置表示候选解，速度由惯性、个体最好和群体最好共同更新。它适合有边界的连续黑箱优化，但容易早熟且原生形式不处理一般约束。

## 更新公式

$$v_i^{t+1}=\omega v_i^t+c_1r_1(p_i-x_i^t)+c_2r_2(g-x_i^t),$$

$$x_i^{t+1}=x_i^t+v_i^{t+1}.$$

$\omega$ 控制探索惯性，$c_1,c_2$ 平衡个体与群体学习；边界截断/反弹策略会影响结果。

## 代码入口

- [Python：`particle_swarm`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/metaheuristics.py)
- [MATLAB：`metaheuristics("pso", objective, lb, ub, seed)`](../../../03-建模算法源码库/02-MATLAB实现代码/智能算法代码/metaheuristics.m)

## 使用流程

1. 统一变量尺度并给紧边界；定义可复现的目标函数。
2. 设置粒子数、迭代数、速度/边界规则与种子。
3. 监控全局最好值、粒子离散度和约束违反。
4. 多种子重复，并在相同函数评估预算下比较基线。
5. 对最好解用局部搜索或可行性修复精炼。

## 常见错误

- 变量尺度差异巨大；边界过宽；速度无控制导致反复撞边。
- 仅跑一次；把停滞当作已找到全局最优。
- 用罚函数但不报告最终约束违反量。

## 来源

- Kennedy & Eberhart (1995), [“Particle Swarm Optimization”](https://ieeexplore.ieee.org/document/488968)。
- [MathWorks PSO 算法说明](https://www.mathworks.com/help/gads/particle-swarm-optimization-algorithm.html)

## 关联

[[智能优化 Hub]] · [[04-Research/02-经典建模模型库/06-智能优化算法/遗传算法GA/Readme|遗传算法GA]] · [[04-Research/02-经典建模模型库/06-智能优化算法/模拟退火SA/Readme|模拟退火SA]]
