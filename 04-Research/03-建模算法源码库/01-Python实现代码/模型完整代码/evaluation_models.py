"""评价类模型的可复用基础实现。

依赖：numpy。约定：矩阵的行表示方案，列表示指标。
这些函数只实现核心算法；正式论文仍需记录指标含义、正负向、权重来源和敏感性分析。
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _matrix(x: ArrayLike) -> NDArray[np.float64]:
    a = np.asarray(x, dtype=float)
    if a.ndim != 2 or min(a.shape) < 1 or not np.isfinite(a).all():
        raise ValueError("输入必须是非空、有限值二维矩阵")
    return a


def ahp_weights(
    comparison: ArrayLike, *, consistency_threshold: float = 0.10
) -> tuple[NDArray[np.float64], float, bool]:
    """AHP 最大特征根法，返回（权重、CR、是否通过一致性检验）。

    comparison 必须为正互反判断矩阵；n > 15 时 RI 表未覆盖，返回 NaN 的 CR。
    """
    a = _matrix(comparison)
    n, m = a.shape
    if n != m or np.any(a <= 0):
        raise ValueError("AHP 判断矩阵必须是正方形且元素为正")
    if not np.allclose(a * a.T, 1.0, rtol=1e-5, atol=1e-8):
        raise ValueError("判断矩阵不满足 a_ij * a_ji = 1")

    eigvals, eigvecs = np.linalg.eig(a)
    k = int(np.argmax(eigvals.real))
    lambda_max = float(eigvals[k].real)
    w = np.abs(eigvecs[:, k].real)
    w /= w.sum()

    ri = np.array(
        [0.00, 0.00, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49,
         1.51, 1.48, 1.56, 1.57, 1.59]
    )
    ci = 0.0 if n <= 2 else (lambda_max - n) / (n - 1)
    cr = 0.0 if n <= 2 else (ci / ri[n - 1] if n <= len(ri) else np.nan)
    return w, float(cr), bool(np.isnan(cr) or cr < consistency_threshold)


def entropy_weights(data: ArrayLike, *, eps: float = 1e-12) -> NDArray[np.float64]:
    """熵权法。调用前应已将成本型指标正向化，并保证各列非负。"""
    x = _matrix(data)
    if np.any(x < 0):
        raise ValueError("熵权法输入应先正向化且非负")
    col_sum = x.sum(axis=0)
    if np.any(col_sum <= eps):
        raise ValueError("存在全零指标列，无法计算熵权")
    p = np.clip(x / col_sum, eps, None)
    k = 1.0 / np.log(x.shape[0]) if x.shape[0] > 1 else 0.0
    entropy = -k * np.sum(p * np.log(p), axis=0)
    divergence = 1.0 - entropy
    if divergence.sum() <= eps:
        return np.full(x.shape[1], 1.0 / x.shape[1])
    return divergence / divergence.sum()


def topsis(
    data: ArrayLike,
    weights: ArrayLike,
    *,
    benefit: ArrayLike | None = None,
) -> tuple[NDArray[np.float64], NDArray[np.int64]]:
    """TOPSIS，返回（贴近度、从优到劣的行索引）。

    benefit[j] 为 False 时第 j 列是成本型指标；默认全部为效益型。
    """
    x = _matrix(data).copy()
    w = np.asarray(weights, dtype=float).reshape(-1)
    if len(w) != x.shape[1] or np.any(w < 0) or w.sum() <= 0:
        raise ValueError("权重必须非负、和大于零，并与指标数一致")
    w /= w.sum()
    benefit_mask = (
        np.ones(x.shape[1], dtype=bool)
        if benefit is None
        else np.asarray(benefit, dtype=bool).reshape(-1)
    )
    if len(benefit_mask) != x.shape[1]:
        raise ValueError("benefit 长度必须等于指标数")

    # 向量归一化后，成本型指标用方向交换处理，不破坏距离尺度。
    denom = np.linalg.norm(x, axis=0)
    if np.any(denom == 0):
        raise ValueError("存在零范数指标列")
    z = x / denom * w
    positive = np.where(benefit_mask, z.max(axis=0), z.min(axis=0))
    negative = np.where(benefit_mask, z.min(axis=0), z.max(axis=0))
    d_pos = np.linalg.norm(z - positive, axis=1)
    d_neg = np.linalg.norm(z - negative, axis=1)
    score = d_neg / np.maximum(d_pos + d_neg, np.finfo(float).eps)
    return score, np.argsort(-score)


def grey_relational_grade(
    data: ArrayLike,
    reference: ArrayLike | None = None,
    *,
    rho: float = 0.5,
) -> NDArray[np.float64]:
    """灰色关联度。data 的行是待比较序列，列是时刻或指标。"""
    x = _matrix(data)
    if not 0 < rho < 1:
        raise ValueError("分辨系数 rho 应位于 (0, 1)")
    ref = x.max(axis=0) if reference is None else np.asarray(reference, dtype=float)
    if ref.shape != (x.shape[1],):
        raise ValueError("参考序列长度必须等于列数")
    delta = np.abs(x - ref)
    d_min, d_max = float(delta.min()), float(delta.max())
    if d_max == 0:
        return np.ones(x.shape[0])
    coefficient = (d_min + rho * d_max) / (delta + rho * d_max)
    return coefficient.mean(axis=1)


def fuzzy_comprehensive_evaluation(
    weights: ArrayLike, membership: ArrayLike
) -> NDArray[np.float64]:
    """一级模糊综合评价 B = W R，返回各评价等级的隶属度。"""
    w = np.asarray(weights, dtype=float).reshape(-1)
    r = _matrix(membership)
    if len(w) != r.shape[0] or np.any(w < 0) or not np.isclose(w.sum(), 1.0):
        raise ValueError("权重需非负、和为 1，且长度等于因素数")
    if np.any(r < 0) or not np.allclose(r.sum(axis=1), 1.0, atol=1e-6):
        raise ValueError("隶属度矩阵每行应非负且和为 1")
    b = w @ r
    return b / b.sum()
