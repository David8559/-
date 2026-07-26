"""预测类模型的基础实现。

依赖：numpy；ARIMA 需要 statsmodels；LSTM 需要 keras。
时序任务必须按时间切分训练/验证集，禁止随机打乱造成未来信息泄漏。
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def linear_regression_ols(
    x: ArrayLike, y: ArrayLike
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """带截距的最小二乘回归，返回（系数[截距在首位]、拟合值、残差）。"""
    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float).reshape(-1)
    if x_arr.ndim == 1:
        x_arr = x_arr[:, None]
    if x_arr.ndim != 2 or len(y_arr) != x_arr.shape[0]:
        raise ValueError("X 应为 n×p，y 应含 n 个观测")
    design = np.column_stack([np.ones(len(x_arr)), x_arr])
    beta, _, rank, _ = np.linalg.lstsq(design, y_arr, rcond=None)
    if rank < design.shape[1]:
        raise ValueError("设计矩阵秩亏：检查完全共线性或重复变量")
    fitted = design @ beta
    return beta, fitted, y_arr - fitted


def simple_exponential_smoothing(
    series: ArrayLike, alpha: float
) -> tuple[NDArray[np.float64], float]:
    """一次指数平滑，返回（单步拟合序列、下一期预测）。"""
    y = np.asarray(series, dtype=float).reshape(-1)
    if len(y) < 2 or not 0 < alpha <= 1:
        raise ValueError("至少需要 2 个观测，且 alpha 位于 (0, 1]")
    level = np.empty_like(y)
    level[0] = y[0]
    for t in range(1, len(y)):
        level[t] = alpha * y[t] + (1 - alpha) * level[t - 1]
    fitted = np.r_[np.nan, level[:-1]]
    return fitted, float(level[-1])


def gm11(series: ArrayLike, horizon: int = 1) -> dict[str, object]:
    """经典 GM(1,1)，返回参数、拟合值、预测值和后验差比 C。

    输入需为正数、等间隔、小样本序列。C 只是诊断之一，仍应做滚动外推检验。
    """
    x0 = np.asarray(series, dtype=float).reshape(-1)
    if len(x0) < 4 or np.any(x0 <= 0) or horizon < 1:
        raise ValueError("GM(1,1) 至少需要 4 个正数观测，horizon >= 1")
    x1 = np.cumsum(x0)
    z1 = 0.5 * (x1[1:] + x1[:-1])
    b_mat = np.column_stack([-z1, np.ones(len(z1))])
    a, b = np.linalg.lstsq(b_mat, x0[1:], rcond=None)[0]
    if np.isclose(a, 0):
        raise ValueError("发展系数接近 0，经典响应式数值不稳定")
    k = np.arange(len(x0) + horizon)
    x1_hat = (x0[0] - b / a) * np.exp(-a * k) + b / a
    x0_hat = np.r_[x0[0], np.diff(x1_hat)]
    residual = x0 - x0_hat[: len(x0)]
    c_ratio = float(np.std(residual, ddof=1) / np.std(x0, ddof=1))
    return {
        "a": float(a),
        "b": float(b),
        "fitted": x0_hat[: len(x0)],
        "forecast": x0_hat[len(x0) :],
        "posterior_ratio_C": c_ratio,
    }


def arima_forecast(
    series: ArrayLike, order: tuple[int, int, int], horizon: int
) -> dict[str, object]:
    """statsmodels ARIMA 基础封装，返回预测均值、区间、AIC 和残差。"""
    if horizon < 1:
        raise ValueError("horizon 必须大于 0")
    from statsmodels.tsa.arima.model import ARIMA

    y = np.asarray(series, dtype=float).reshape(-1)
    fitted = ARIMA(y, order=order).fit()
    pred = fitted.get_forecast(steps=horizon)
    return {
        "mean": np.asarray(pred.predicted_mean),
        "interval_95": np.asarray(pred.conf_int(alpha=0.05)),
        "aic": float(fitted.aic),
        "residuals": np.asarray(fitted.resid),
    }


def build_lstm(
    lookback: int, n_features: int, *, units: int = 32, learning_rate: float = 1e-3
):
    """建立单步回归 LSTM；数据窗口化、缩放和时间切分由调用者完成。"""
    if min(lookback, n_features, units) < 1:
        raise ValueError("lookback、n_features、units 必须为正整数")
    import keras

    model = keras.Sequential(
        [
            keras.layers.Input(shape=(lookback, n_features)),
            keras.layers.LSTM(units),
            keras.layers.Dense(1),
        ]
    )
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate), loss="mse"
    )
    return model
