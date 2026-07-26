---
type: research-method
status: active
topic: 种群增长Logistic模型
updated: 2026-07-26
tags: [area/数学建模, topic/微分方程动力学, method/Logistic增长]
---

# 种群增长Logistic模型

> [!summary] 30 秒复习
> Logistic 增长在低密度时近似指数增长，接近环境容量 $K$ 时增速下降。它适合单种群、资源限制近似稳定的 S 形增长，不自动适合存在时滞、迁移或多物种作用的系统。

## 模型

$$\frac{dN}{dt}=rN\left(1-\frac NK\right),$$

解析解：

$$N(t)=\frac{K}{1+\left(\frac{K-N_0}{N_0}\right)e^{-rt}}.$$

$r$ 的单位是时间$^{-1}$，$K,N$ 单位一致；最大绝对增速出现在 $N=K/2$。

## 建模步骤

1. 确认数据呈饱和趋势，定义种群边界与采样间隔。
2. 以非线性最小二乘估计 $r,K,N_0$；不要仅靠线性化。
3. 画拟合、残差和参数区间，检查 $r,K$ 的相关性。
4. 做留后预测并与指数增长/其他饱和模型比较。
5. 对 $K$ 时变、时滞和外部干预进行情景扩展。

## 代码入口

- [Python：`simulate_logistic`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/network_dynamics_models.py)
- [MATLAB：`dynamics_models("logistic", r, K, N0, tspan)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/dynamics_models.m)

## 常见错误

- 观测尚未接近饱和就强估 $K$，导致参数极不稳定。
- 忽略观测误差结构；线性化改变误差分布后仍直接做 OLS。
- 把 $K$ 解释为永恒不变的物理上限。

## 来源

- Verhulst, P. F. (1838), logistic growth model。
- [MATLAB `ode45` 官方文档](https://www.mathworks.com/help/matlab/ref/ode45.html)

## 关联

[[微分方程动力学 Hub]] · [[04-Research/02-经典建模模型库/05-微分方程动力学模型/SIR与SIS传染病模型/Readme|SIR与SIS传染病模型]] · [[04-Research/02-经典建模模型库/02-预测类模型/回归预测/Readme|回归预测]]
