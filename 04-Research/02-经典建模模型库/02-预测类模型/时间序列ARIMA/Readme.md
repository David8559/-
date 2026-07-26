---
type: research-method
status: active
topic: 时间序列ARIMA
updated: 2026-07-26
tags: [area/数学建模, topic/预测模型, method/ARIMA]
---

# 时间序列ARIMA

> [!summary] 30 秒复习
> ARIMA$(p,d,q)$ 用 $d$ 阶差分使序列近似平稳，再用 AR 与 MA 描述自相关。重点是时间切分、阶数选择和白噪声残差，不是寻找让训练拟合最好的阶数。

## 模型

$$\phi(B)(1-B)^d y_t=c+\theta(B)\varepsilon_t.$$

$p$ 是 AR 阶数，$d$ 是差分阶数，$q$ 是 MA 阶数；季节模型扩展为 SARIMA$(p,d,q)(P,D,Q)_s$。

## 建模流程

1. 保持等时间间隔；处理缺失但不得用未来值污染过去。
2. 画序列、ACF/PACF；用单位根检验与业务趋势共同判断差分。
3. 在合理的小阶数网格内按 AIC/BIC筛选候选。
4. 检查残差均值、ACF、Ljung–Box、方差稳定性和异常点。
5. 通过滚动预测比较朴素法、指数平滑和 ARIMA，输出预测区间。

## 代码入口

- [Python：`arima_forecast`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/forecast_models.py)
- [MATLAB：`forecast_models("arima", y, [p d q], horizon)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/forecast_models.m)

## 常见错误

- 过度差分；用 ADF 一项结果机械决定 $d$。
- 只凭 ACF/PACF 看图选一个模型，不做候选比较和滚动验证。
- 残差仍有显著自相关却继续解释预测；忽略结构突变和外生变量。

## 来源

- [statsmodels 时间序列模型官方入口](https://www.statsmodels.org/stable/tsa.html)
- [MATLAB `arima` 官方文档](https://www.mathworks.com/help/econ/arima.html)

## 关联

[[预测模型 Hub]] · [[04-Research/02-经典建模模型库/02-预测类模型/指数平滑预测/Readme|指数平滑预测]] · [[04-Research/02-经典建模模型库/02-预测类模型/回归预测/Readme|回归预测]] · [[模型检验 Hub]]
