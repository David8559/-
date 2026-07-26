---
type: research-method
status: active
topic: 最大流最小割
updated: 2026-07-26
tags: [area/数学建模, topic/图论网络, method/最大流]
---

# 最大流最小割

> [!summary] 30 秒复习
> 在有向容量网络中，最大化源点到汇点的总流量；除源汇外各节点满足流量守恒。最大流值等于最小割容量，可用最小割定位瓶颈。

## 模型

$$0\le f_{uv}\le c_{uv},$$

$$\sum_u f_{uv}=\sum_w f_{vw}\quad(v\ne s,t).$$

目标最大化源点净流出。残量网络同时记录剩余容量与可撤销流量，增广路算法据此改进解。

## 建模步骤

1. 明确边方向、容量单位、源点与汇点；并行边不要误合并。
2. 构建容量网络，求最大流及各边流量。
3. 从残量网络可达集合得到最小割两侧和割边。
4. 验证容量约束、节点守恒、最大流值=最小割容量。
5. 对割边容量做边际扩容分析；多商品流不能直接套单商品最大流。

## 代码入口

- [Python：`maximum_flow_minimum_cut`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/network_dynamics_models.py)
- [MATLAB：`optimization_network_models("maxflow", ...)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

## 常见错误

- 无向边直接当成一条有向边；容量和费用混为一个权。
- 忽略反向残量边；只给流值不展示守恒与瓶颈割。
- 把最小割边全部解释为“应扩容”，未考虑替代路径和扩容成本。

## 来源

- [NetworkX 最大流/最小割官方文档](https://networkx.org/documentation/stable/reference/algorithms/flow.html)
- [MATLAB `maxflow` 官方文档](https://www.mathworks.com/help/matlab/ref/graph.maxflow.html)

## 关联

[[图论网络 Hub]] · [[04-Research/02-经典建模模型库/04-图论与网络模型/最短路径/Readme|最短路径]] · [[04-Research/02-经典建模模型库/03-优化类模型/线性规划/Readme|线性规划]]
