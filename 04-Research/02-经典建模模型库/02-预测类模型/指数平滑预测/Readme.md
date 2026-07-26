---
type: research-method
status: active
topic: 指数平滑预测
updated: 2026-07-26
tags: [area/数学建模, topic/预测模型, method/指数平滑]
---

# 指数平滑预测

> [!summary] 30 秒复习
> 指数平滑递减地加权历史观测：SES 处理水平，Holt 加趋势，Holt–Winters 加季节。先识别结构，再选择误差、趋势、季节的加法或乘法形式。

## 基础公式

一次指数平滑：

$$\ell_t=\alpha y_t+(1-\alpha)\ell_{t-1},\qquad
\hat y_{t+h|t}=\ell_t.$$

$\alpha$ 大时更追随近期变化、方差更大；$\alpha$ 小时更平滑、响应更慢。

## 建模流程

1. 画时序图并判断水平、趋势、季节周期和方差是否随水平变化。
2. 以朴素预测为基线，候选 SES/Holt/阻尼趋势/Holt–Winters。
3. 用训练集估计平滑参数，不凭经验固定后直接评价。
4. 用滚动起点验证比较 MAE、RMSE、MASE；检查残差自相关。
5. 输出点预测和区间，说明季节周期及初始化方法。

## 代码入口

- [Python：`simple_exponential_smoothing`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/forecast_models.py)
- [MATLAB：`forecast_models("ses", y, alpha)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/forecast_models.m)

## 常见错误

- 数据有明显趋势/季节性却使用 SES；乘法季节模型遇到零或负数。
- 随机切分时间序列；只看训练 SSE。
- 没有与季节朴素法比较，或把远期平坦预测当作结构性结论。

## 来源

- [statsmodels 指数平滑官方示例](https://www.statsmodels.org/stable/examples/notebooks/generated/exponential_smoothing.html)
- Hyndman & Athanasopoulos, [Forecasting: Principles and Practice](https://otexts.com/fpp3/)

## 关联

[[预测模型 Hub]] · [[04-Research/02-经典建模模型库/02-预测类模型/时间序列ARIMA/Readme|时间序列ARIMA]] · [[模型检验 Hub]]
