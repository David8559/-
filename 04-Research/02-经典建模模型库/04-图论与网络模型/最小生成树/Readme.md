---
type: research-method
status: active
topic: 最小生成树
updated: 2026-07-26
tags: [area/数学建模, topic/图论网络, method/最小生成树]
---

# 最小生成树

> [!summary] 30 秒复习
> MST 在连通无向加权图中选择 $n-1$ 条无环边连接全部节点，并使总权最小。它优化的是建设网络总成本，不是任意两点的通行距离。

## 算法选择

- Kruskal：按边权排序，用并查集拒绝成环，适合稀疏图。
- Prim：从一个节点扩张割上的最轻边，适合稠密图。
- 图不连通时得到最小生成森林；若题目要求全连通，需要补边或解释不可行。

## 正确性抓手

割性质：对任意割，跨越该割的最轻边属于某棵 MST。若边权不唯一，MST 也可能不唯一，但最小总权相同。

## 代码入口

- [Python：`minimum_spanning_tree`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/network_dynamics_models.py)
- [MATLAB：`optimization_network_models("mst", ...)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

## 验证

- 连通图结果应含 $n-1$ 条边、无环且覆盖所有节点。
- 回算总权；对小图枚举生成树或比较 Kruskal/Prim。
- 做边权扰动，检查关键边与备选网络；现实中还需考虑容量、可靠性和冗余。

## 来源

- [NetworkX `minimum_spanning_tree` 官方文档](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html)
- [MATLAB `minspantree` 官方文档](https://www.mathworks.com/help/matlab/ref/graph.minspantree.html)

## 关联

[[图论网络 Hub]] · [[04-Research/02-经典建模模型库/04-图论与网络模型/最短路径/Readme|最短路径]] · [[04-Research/02-经典建模模型库/03-优化类模型/启发式与贪心方法/Readme|启发式与贪心方法]]
