---
type: research-method
status: active
topic: 模拟退火SA
updated: 2026-07-26
tags: [area/数学建模, topic/智能优化, method/SA]
---

# 模拟退火SA

> [!summary] 30 秒复习
> SA 在高温阶段以一定概率接受劣解以跳出局部最优，随后逐渐降温加强开发。邻域结构和温度表比“退火”名称本身更重要。

## 接受准则

最小化问题中，若 $\Delta=f(x')-f(x)\le0$ 接受；否则以

$$P(\text{accept})=\exp(-\Delta/T)$$

接受。温度过快下降会退化为局部搜索，过慢则计算昂贵。

## 代码入口

- [Python：`simulated_annealing`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/metaheuristics.py)
- [MATLAB：`metaheuristics("sa", objective, initial, lb, ub, seed)`](../../../03-建模算法源码库/02-MATLAB实现代码/智能算法代码/metaheuristics.m)

## 使用流程

1. 设计能遍历可行域的邻域；尽量直接生成可行解。
2. 用试运行使初温对应合理的劣解接受率。
3. 设冷却率、每温度迭代次数和停止条件。
4. 始终保存历史最好解；多初值、多种子重复。
5. 报告评估预算、接受率、收敛曲线和约束违反。

## 常见错误

- 邻域太小无法跨区域，或太大导致几乎全拒绝。
- 只返回最后状态而不是历史最好；温度下降到 0 造成数值问题。
- 一次运行即声称全局最优，没有精确/随机基线。

## 来源

- Kirkpatrick, Gelatt & Vecchi (1983), [“Optimization by Simulated Annealing”](https://www.science.org/doi/10.1126/science.220.4598.671)。
- [MathWorks 全局优化求解器选择](https://www.mathworks.com/help/gads/choose-a-solver.html)

## 关联

[[智能优化 Hub]] · [[04-Research/02-经典建模模型库/06-智能优化算法/遗传算法GA/Readme|遗传算法GA]] · [[04-Research/02-经典建模模型库/03-优化类模型/启发式与贪心方法/Readme|启发式与贪心方法]]
