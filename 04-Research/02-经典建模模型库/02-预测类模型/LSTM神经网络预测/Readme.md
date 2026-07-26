---
type: research-method
status: active
topic: LSTM神经网络预测
updated: 2026-07-26
tags: [area/数学建模, topic/预测模型, method/LSTM]
---

# LSTM神经网络预测

> [!summary] 30 秒复习
> LSTM 用门控状态学习长短期依赖，适合数据量较大、非线性和多变量时序。它不是小样本的默认选择；窗口、缩放、切分和基线比较比堆叠网络更重要。

## 核心结构

遗忘门、输入门、候选状态和输出门共同更新：

$$f_t=\sigma(W_f[h_{t-1},x_t]+b_f),\qquad
c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t.$$

训练样本形状通常为 `(样本数, lookback, 特征数)`，预测目标应明确是单步还是多步。

## 建模流程

1. 严格按时间分训练/验证/测试；缩放器仅在训练集拟合。
2. 以朴素法、线性回归、指数平滑/ARIMA 为基线。
3. 固定窗口和预测步长，建立小型单层 LSTM，再逐步增加复杂度。
4. 用早停、固定随机种子和多个种子重复；监控训练/验证曲线。
5. 在原量纲报告 MAE/RMSE，做滚动预测、残差和极端时段分析。

## 代码入口

- [Python：`build_lstm`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/forecast_models.py)
- [MATLAB：`forecast_models("lstm-layers", numFeatures, numHidden)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/forecast_models.m)

## 常见错误

- 随机打乱时序；对全数据拟合标准化器；窗口越过测试边界。
- 数据很少却用深网，未与简单基线比较。
- 多步递归预测不传播不确定性；只展示一条漂亮拟合曲线。

## 来源

- Hochreiter & Schmidhuber (1997), “Long Short-Term Memory”。
- [Keras 官方 LSTM 时间序列预测示例](https://keras.io/examples/timeseries/timeseries_weather_forecasting/)

## 关联

[[预测模型 Hub]] · [[04-Research/02-经典建模模型库/02-预测类模型/时间序列ARIMA/Readme|时间序列ARIMA]] · [[04-Research/02-经典建模模型库/02-预测类模型/回归预测/Readme|回归预测]] · [[模型检验 Hub]]
