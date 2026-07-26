---
type: research-method
status: active
topic: 最短路径
updated: 2026-07-26
tags: [area/数学建模, topic/图论网络, method/最短路径]
---

# 最短路径

> [!summary] 30 秒复习
> 将地点/状态作为节点、可达关系作为边、成本作为权。非负单源用 Dijkstra；含负边的有向图用 Bellman–Ford；全源可用 Floyd–Warshall/Johnson。

## 建模前先问

- 图是有向还是无向？权重是距离、时间、费用还是风险，能否相加？
- 多条边、不可达、时变权和负权是否存在？
- 目标是单源单终点、单源全点还是所有点对？

## 核心递推

Dijkstra 的松弛操作：

$$d(v)\leftarrow\min\{d(v),d(u)+w(u,v)\}.$$

Floyd–Warshall：

$$D_{ij}^{(k)}=\min\{D_{ij}^{(k-1)},D_{ik}^{(k-1)}+D_{kj}^{(k-1)}\}.$$

## 代码入口

- [Python：`shortest_path`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/network_dynamics_models.py)
- [MATLAB：`optimization_network_models("shortest", ...)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

## 验证

- 路径首尾正确、相邻节点确有边；手工回算边权和。
- 小图与穷举/另一算法交叉验证；检查不可达与并列最短路径。
- Dijkstra 禁止负权；负环存在时“最短路径”无有限解。

## 来源

- [NetworkX 最短路径官方文档](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths/index.html)
- [MATLAB `shortestpath` 官方文档](https://www.mathworks.com/help/matlab/ref/graph.shortestpath.html)

## 关联

[[图论网络 Hub]] · [[04-Research/02-经典建模模型库/04-图论与网络模型/最小生成树/Readme|最小生成树]] · [[04-Research/02-经典建模模型库/03-优化类模型/动态规划/Readme|动态规划]] · [[04-Research/02-经典建模模型库/04-图论与网络模型/最大流最小割/Readme|最大流最小割]]
