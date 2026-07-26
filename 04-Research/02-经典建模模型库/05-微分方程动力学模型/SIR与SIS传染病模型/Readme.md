---
type: research-method
status: active
topic: SIR与SIS传染病模型
updated: 2026-07-26
tags: [area/数学建模, topic/微分方程动力学, method/SIR]
---

# SIR与SIS传染病模型

> [!summary] 30 秒复习
> SIR 把人群分为易感、感染、移除，适合感染后获得免疫或退出传播；SIS 的康复者回到易感，适合无持久免疫。分舱和转移必须对应真实机制。

## SIR 方程

$$\frac{dS}{dt}=-\beta\frac{SI}{N},\qquad
\frac{dI}{dt}=\beta\frac{SI}{N}-\gamma I,\qquad
\frac{dR}{dt}=\gamma I.$$

初始基本再生数近似 $R_0=\beta/\gamma$；更严格的有效再生数随 $S/N$ 改变。SIS 将 $\gamma I$ 返回 $S$。

## 建模步骤

1. 规定分舱、人口边界、时间单位和观测变量。
2. 从机制写流量，验证总人口守恒与状态非负。
3. 依据病例/恢复数据估计 $\beta,\gamma$；报告可识别性与区间。
4. 数值求解并与留出时段比较，检查残差和峰值时间。
5. 对初值、参数和干预情景做敏感性分析；变参数必须有依据。

## 代码入口

- [Python：`simulate_sir`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/network_dynamics_models.py)
- [MATLAB：`dynamics_models("sir", beta, gamma, initial, tspan)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/dynamics_models.m)

## 常见错误

- 把报告病例直接当真实 $I$；忽略漏报、潜伏期和时变接触率。
- $\beta,\gamma$ 单位不一致；用比例状态却又除一次 $N$。
- 仅拟合总病例，不检查参数不可识别和预测区间。

## 来源

- Kermack & McKendrick (1927), “A Contribution to the Mathematical Theory of Epidemics”。
- [SciPy `solve_ivp` 官方文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)

## 关联

[[微分方程动力学 Hub]] · [[04-Research/02-经典建模模型库/05-微分方程动力学模型/种群增长Logistic模型/Readme|种群增长Logistic模型]] · [[模型检验 Hub]]
