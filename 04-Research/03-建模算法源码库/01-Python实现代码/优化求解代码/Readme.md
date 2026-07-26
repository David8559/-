---
type: code-index
status: active
tags: [area/数学建模, tool/Python, topic/优化模型]
---

# Python 优化求解代码

| 文件 | 核心函数 |
|---|---|
| [optimization_models.py](optimization_models.py) | `solve_linear_program`、`solve_milp`、`weighted_sum_multiobjective`、`zero_one_knapsack`、`greedy_interval_scheduling` |
| [metaheuristics.py](metaheuristics.py) | `genetic_algorithm`、`particle_swarm`、`simulated_annealing`、`ant_colony_tsp` |

精确规划先检查求解状态、可行性和 MIP gap；随机算法固定种子、多次重复，并在相同函数评估预算下比较。
