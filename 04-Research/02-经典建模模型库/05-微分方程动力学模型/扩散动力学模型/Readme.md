---
type: research-method
status: active
topic: 扩散动力学模型
updated: 2026-07-26
tags: [area/数学建模, topic/微分方程动力学, method/扩散方程]
---

# 扩散动力学模型

> [!summary] 30 秒复习
> 扩散方程描述物质/热量从高浓度向低浓度传播。模型由守恒定律、Fick 定律、初始条件和边界条件共同决定；边界写错比求解器选错更致命。

## 基础模型

$$\frac{\partial u}{\partial t}=D\nabla^2u+q(x,t),$$

$u$ 可为浓度或温度，$D$ 为扩散系数，$q$ 为源汇项。一维显式差分：

$$u_i^{n+1}=u_i^n+r(u_{i+1}^n-2u_i^n+u_{i-1}^n),\qquad
r=\frac{D\Delta t}{\Delta x^2}.$$

一维显式格式通常需 $r\le1/2$ 才稳定。

## 建模步骤

1. 从控制体守恒推导方程，定义几何、单位、源汇和 $D$。
2. 指定初值；区分定值、通量和混合边界。
3. 选有限差分/有限元等离散，做网格与时间步收敛检查。
4. 验证非负性、质量守恒或能量变化；与解析解/基准算例比较。
5. 估计 $D$ 时给出数据来源、参数区间和敏感性。

## 代码入口

- [Python：`diffuse_1d_explicit`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/network_dynamics_models.py)
- [MATLAB：`dynamics_models("diffusion", initial, D, dx, dt, steps)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/dynamics_models.m)

## 常见错误

- 数值不稳定仍把振荡/负浓度解释为现象。
- 边界条件与题意不符；网格变化后结论明显变却未检查。
- $D,\Delta x,\Delta t$ 单位不一致；源汇破坏守恒但无说明。

## 来源

- [MATLAB `pdepe` 官方文档](https://www.mathworks.com/help/matlab/ref/pdepe.html)
- [SciPy 积分与微分方程教程](https://docs.scipy.org/doc/scipy/tutorial/integrate.html)

## 关联

[[微分方程动力学 Hub]] · [[模型检验 Hub]] · [[可视化 Hub]]
