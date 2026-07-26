---
type: research-method
status: active
topic: 蚁群算法ACO
updated: 2026-07-26
tags: [area/数学建模, topic/智能优化, method/ACO]
---

# 蚁群算法ACO

> [!summary] 30 秒复习
> ACO 用启发信息和信息素概率式构造离散解，优质路径得到强化，蒸发防止早期路径永久支配。经典用途是 TSP/路径/调度等组合优化。

## 转移与更新

蚂蚁从 $i$ 选择未访问节点 $j$ 的概率：

$$p_{ij}\propto \tau_{ij}^{\alpha}\eta_{ij}^{\beta},\qquad
\eta_{ij}=1/d_{ij}.$$

信息素更新：

$$\tau_{ij}\leftarrow(1-\rho)\tau_{ij}+\sum_k\Delta\tau_{ij}^k.$$

## 代码入口

- [Python：`ant_colony_tsp`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/metaheuristics.py)
- [MATLAB：`metaheuristics("aco-tsp", distance, ants, iterations, seed)`](../../../03-建模算法源码库/02-MATLAB实现代码/智能算法代码/metaheuristics.m)

## 使用流程

1. 设计可行的增量构造规则、候选集和启发信息。
2. 设置蚂蚁数、$\alpha,\beta,\rho$ 和信息素上下界。
3. 每轮构造完整解，必要时加 2-opt 等局部搜索。
4. 更新信息素并监控路线多样性和最好值。
5. 多种子、同预算对比最近邻、SA/GA 和小规模精确最优。

## 常见错误

- 距离 0 导致启发值无穷；构造出重复/遗漏节点。
- 蒸发过弱导致早熟，过强导致接近随机搜索。
- 只展示收敛曲线，不回算闭合路线长度与可行性。

## 来源

- Dorigo, Maniezzo & Colorni (1996), “Ant System”。
- Dorigo & Gambardella (1997), [“Ant Colony System”](https://iridia.ulb.ac.be/~mdorigo/Published_papers/All_Dorigo_papers/DorGam1997tec.pdf)。

## 关联

[[智能优化 Hub]] · [[04-Research/02-经典建模模型库/04-图论与网络模型/最短路径/Readme|最短路径]] · [[04-Research/02-经典建模模型库/06-智能优化算法/遗传算法GA/Readme|遗传算法GA]] · [[04-Research/02-经典建模模型库/06-智能优化算法/模拟退火SA/Readme|模拟退火SA]]
