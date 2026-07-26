---
type: research-method
status: active
topic: 遗传算法GA
updated: 2026-07-26
tags: [area/数学建模, topic/智能优化, method/GA]
---

# 遗传算法GA

> [!summary] 30 秒复习
> GA 用种群、选择、交叉、变异和精英保留探索搜索空间。编码与约束处理决定算法能否产生有效解；一次运行的最好值不是充分证据。

## 算法骨架

1. 按变量类型设计实数/整数/排列编码并初始化可行种群。
2. 评价适应度；最小化目标转换时避免符号与尺度错误。
3. 选择父代，交叉产生后代，变异维持多样性。
4. 修复或惩罚不可行解，保留精英。
5. 达到代数、评估预算或停滞条件后输出最好解。

## 代码入口

- [Python：`genetic_algorithm`](../../../03-建模算法源码库/01-Python实现代码/优化求解代码/metaheuristics.py)
- [MATLAB：`metaheuristics("ga", objective, lb, ub, seed)`](../../../03-建模算法源码库/02-MATLAB实现代码/智能算法代码/metaheuristics.m)

## 参数与验证

- 记录种群数、代数、交叉/变异率、选择算子、随机种子和函数评估次数。
- 至少多种子重复，报告最好/均值/标准差与收敛曲线。
- 小规模与精确求解器比较；同等评估预算下比较随机搜索或其他算法。

## 常见错误

- 排列问题使用普通实数交叉产生重复城市；惩罚系数过小导致不可行“优解”。
- 过早收敛却只增加代数；未监控种群多样性。
- 调参使用测试集，或不同算法比较时评估预算不相等。

## 来源

- Holland, J. H. (1975), *Adaptation in Natural and Artificial Systems*。
- [pymoo 官方 GitHub：GA 与多目标进化算法](https://github.com/anyoptimization/pymoo)

## 关联

[[智能优化 Hub]] · [[04-Research/02-经典建模模型库/03-优化类模型/多目标规划/Readme|多目标规划]] · [[04-Research/02-经典建模模型库/06-智能优化算法/模拟退火SA/Readme|模拟退火SA]] · [[04-Research/02-经典建模模型库/06-智能优化算法/粒子群PSO/Readme|粒子群PSO]]
