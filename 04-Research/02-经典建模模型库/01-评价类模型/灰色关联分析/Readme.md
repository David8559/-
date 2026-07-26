---
type: research-method
status: active
topic: 灰色关联分析
updated: 2026-07-26
tags: [area/数学建模, topic/评价模型, method/灰色关联分析]
---

# 灰色关联分析

> [!summary] 30 秒复习
> 灰色关联分析比较序列相对参考序列的几何接近程度。它适合小样本、信息不完全的关联排序，但“关联度高”不代表因果关系。

## 核心数学

对无量纲化后的参考序列 $x_0(k)$ 和比较序列 $x_i(k)$：

$$\Delta_i(k)=|x_0(k)-x_i(k)|,$$

$$\xi_i(k)=\frac{\Delta_{\min}+\rho\Delta_{\max}}
{\Delta_i(k)+\rho\Delta_{\max}},\qquad
\gamma_i=\frac1n\sum_k\xi_i(k).$$

分辨系数通常取 $\rho=0.5$，但应检查 $\rho$ 变化对排序的影响。

## 算法步骤

1. 明确参考序列：理想方案、目标轨迹或母序列。
2. 对序列作同向、无量纲处理，不能混用不同定义的标准化结果。
3. 计算差序列、全局极差、关联系数与平均/加权关联度。
4. 排序并检查参考序列、$\rho$、权重和预处理的敏感性。

## 代码入口

- [Python：`grey_relational_grade`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/evaluation_models.py)
- [MATLAB：`evaluation_models("gra", X, reference, rho)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/evaluation_models.m)

## 常见错误

- 比较序列行列含义颠倒；不同量纲未处理。
- 参考序列随意取最大值却不说明业务含义。
- 用关联度声称变量存在因果影响；忽略时间滞后。

## 来源

- Deng, J. (1989), “Introduction to Grey System Theory”, *The Journal of Grey System*, 1(1), 1–24。
- [pyDecision 的 GRA 实现](https://github.com/Valdecy/pyDecision)

## 关联

[[评价模型 Hub]] · [[04-Research/02-经典建模模型库/02-预测类模型/灰色预测GM(1,1)/Readme|灰色预测GM(1,1)]] · [[04-Research/02-经典建模模型库/01-评价类模型/TOPSIS优劣解距离法/Readme|TOPSIS优劣解距离法]]
