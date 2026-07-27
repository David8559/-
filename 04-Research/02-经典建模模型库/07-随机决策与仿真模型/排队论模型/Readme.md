---
type: research-method
status: active
topic: 排队论模型
updated: 2026-07-26
tags: [area/数学建模, topic/随机仿真, method/排队论]
---

# 排队论模型

> [!summary] 30 秒复习
> 排队模型由到达过程/服务分布/服务台数/容量/规则决定。M/M/1 假设泊松到达、指数服务、单服务台、无限容量与稳态，必须满足 $\lambda<\mu$。

## M/M/1 核心指标

令利用率 $\rho=\lambda/\mu$：

$$L=\frac{\rho}{1-\rho},\qquad
L_q=\frac{\rho^2}{1-\rho},$$

$$W=\frac1{\mu-\lambda},\qquad
W_q=\frac{\lambda}{\mu(\mu-\lambda)}.$$

Little 定律 $L=\lambda W,\ L_q=\lambda W_q$ 是重要一致性检查。

## 建模步骤

1. 从时间戳估计到达间隔和服务时间，检查分布、独立性与时段稳定性。
2. 根据服务台数、容量和规则选择 Kendall 记号，而非默认 M/M/1。
3. 检查稳态条件，计算理论指标。
4. 用离散事件仿真验证；去除预热期并给置信区间。
5. 比较增开服务台、预约、分流等策略的成本与等待收益。

## 代码入口

- [Python：`mm1_metrics`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/network_dynamics_models.py)
- [MATLAB：`optimization_network_models("mm1", lambda, mu)`](../../../03-建模算法源码库/02-MATLAB实现代码/规划求解代码/optimization_network_models.m)

## 常见错误

- $\lambda,\mu$ 时间单位不一致；把服务时间均值直接当服务率。
- $\rho\ge1$ 仍代稳态公式；现实到达/服务不服从指数分布却不检验。
- 仿真从空系统开始却不设预热期，均值被低估。

## 来源

- [MathWorks M/M/1 排队系统官方示例](https://www.mathworks.com/help/simevents/ug/m-m-1-queuing-system.html)

## 关联

[[蒙特卡洛 Hub]] · [[马尔可夫决策过程 Hub]] · [[模型检验 Hub]]
