---
type: research-method
status: active
topic: 启发式与贪心方法
updated: 2026-07-26
tags: [area/数学建模, topic/优化模型, method/贪心]
---

# 启发式与贪心方法

> [!summary] 30 秒复习
> 贪心算法每步做局部最优选择；只有能证明贪心选择性质和最优子结构时才保证全局最优。一般启发式只承诺“较快得到可行好解”，必须给下界/基线或实验比较。

## 选用判断

- 能通过交换论证、割性质或拟阵结构证明局部选择不会破坏全局最优。
- 大规模组合问题需要快速可行解，可把贪心作为构造器、热启动或基线。
- 加权区间调度、一般背包等问题不能直接照搬无权贪心规则。

## 算法步骤

1. 明确候选集合、局部评分和可行性检查。
2. 写出循环不变量；尝试交换论证或反例搜索。
3. 若无正确性证明，标注为启发式并设置改进/局部搜索。
4. 与精确算法的小规模最优值比较，报告最优差距和运行时间。
5. 检查排序并列、边界输入和确定性。

## 代码入口

- [Python：`greedy_interval_scheduling`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/optimization_models.py)
- [MATLAB：`optimization_network_models("interval", intervals)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

## 常见错误

- “看起来合理”就声称最优；只展示一个成功案例。
- 局部指标没有量纲或业务依据；不同排序并列导致结果不稳定。
- 启发式解未检查全部约束，或没有与随机/简单基线比较。

## 来源

- [MIT 6.046：贪心、动态规划、MST 与最短路课程材料](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/resources/lecture-videos/)

## 关联

[[优化模型 Hub]] · [[04-Research/02-经典建模模型库/03-优化类模型/动态规划/Readme|动态规划]] · [[04-Research/02-经典建模模型库/04-图论与网络模型/最小生成树/Readme|最小生成树]] · [[智能优化 Hub]]
