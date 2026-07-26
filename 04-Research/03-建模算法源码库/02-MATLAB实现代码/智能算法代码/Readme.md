---
type: code-index
status: active
tags: [area/数学建模, tool/MATLAB, topic/智能优化]
---

# MATLAB 智能算法代码

[metaheuristics.m](metaheuristics.m) 提供：

- `metaheuristics("ga", objective, lb, ub, seed)`
- `metaheuristics("pso", objective, lb, ub, seed)`
- `metaheuristics("sa", objective, initial, lb, ub, seed)`
- `metaheuristics("aco-tsp", distance, ants, iterations, seed)`

GA/PSO/SA 需要 Global Optimization Toolbox；ACO-TSP 为本地教学实现。所有方法按最小化目标，正式比较必须控制相同函数评估预算并进行多种子重复。
