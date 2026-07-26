---
type: research-method
status: active
topic: 回归预测
updated: 2026-07-26
tags: [area/数学建模, topic/预测模型, method/回归]
---

# 回归预测

> [!summary] 30 秒复习
> 回归用解释变量描述响应变量的条件均值。最小二乘只保证样本内残差平方和最小；可信预测还依赖变量设计、误差假设、外推范围和样本外验证。

## 基础模型

$$y=X\beta+\varepsilon,\qquad
\hat\beta=(X^\mathsf TX)^{-1}X^\mathsf Ty.$$

实际计算用 QR/SVD 或求解器，不直接求逆。系数解释必须固定其他变量并结合单位。

## 建模流程

1. 依据机制提出变量与可能的交互/非线性项，先画散点和残差图。
2. 划分训练/验证集；时间数据按时间切分。
3. 拟合 OLS 基线，检查共线性、异常点、异方差、自相关和残差结构。
4. 比较线性、变换、正则化或稳健回归；用交叉验证/滚动验证选模。
5. 报告系数区间、样本外 MAE/RMSE、预测区间及适用范围。

## 代码入口

- [Python：`linear_regression_ols`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/forecast_models.py)
- [MATLAB：`forecast_models("ols", X, y)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/forecast_models.m)

## 必查问题

- 训练集 $R^2$ 高不代表外推好；比较调整 $R^2$ 与样本外误差。
- VIF/条件数用于发现共线性；残差图用于发现非线性、异方差和异常点。
- 相关关系不能自动解释为因果，变量选择不得偷看测试集结果。

## 来源

- [statsmodels 线性回归官方文档](https://www.statsmodels.org/stable/regression.html)
- [scikit-learn 常见数据泄漏与随机性陷阱](https://scikit-learn.org/stable/common_pitfalls.html)

## 关联

[[预测模型 Hub]] · [[04-Research/02-经典建模模型库/02-预测类模型/时间序列ARIMA/Readme|时间序列ARIMA]] · [[模型检验 Hub]] · [[数据处理 Hub]]
