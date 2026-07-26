---
type: code-index
status: active
tags: [area/数学建模, tool/MATLAB, topic/优化模型, topic/图论网络]
---

# MATLAB 规划与图网络代码

[optimization_network_models.m](optimization_network_models.m) 提供统一入口：

- `"lp"`、`"milp"`、`"weighted-sum"`
- `"knapsack"`、`"interval"`
- `"shortest"`、`"mst"`、`"maxflow"`、`"mm1"`

规划结果必须检查 `exitflag`、约束回代和整数间隙；图结果需回算边权、守恒或连通性。
