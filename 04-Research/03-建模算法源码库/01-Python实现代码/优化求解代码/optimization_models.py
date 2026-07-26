"""规划、动态规划与贪心方法的基础实现。"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import numpy as np
from numpy.typing import ArrayLike, NDArray


def solve_linear_program(
    c: ArrayLike,
    *,
    a_ub: ArrayLike | None = None,
    b_ub: ArrayLike | None = None,
    a_eq: ArrayLike | None = None,
    b_eq: ArrayLike | None = None,
    bounds: Sequence[tuple[float | None, float | None]] | None = None,
) -> dict[str, object]:
    """SciPy/HiGHS 线性规划封装；统一求最小值，最大化时传入 -c。"""
    from scipy.optimize import linprog

    result = linprog(
        np.asarray(c, dtype=float),
        A_ub=a_ub,
        b_ub=b_ub,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"LP 求解失败：{result.message}")
    return {"x": result.x, "objective": float(result.fun), "message": result.message}


def solve_milp(
    c: ArrayLike,
    a: ArrayLike,
    lower: ArrayLike,
    upper: ArrayLike,
    *,
    integrality: ArrayLike,
    variable_bounds=None,
) -> dict[str, object]:
    """SciPy/HiGHS MILP；约束写成 lower <= A @ x <= upper。"""
    from scipy.optimize import LinearConstraint, milp

    constraint = LinearConstraint(
        np.asarray(a, dtype=float),
        np.asarray(lower, dtype=float),
        np.asarray(upper, dtype=float),
    )
    result = milp(
        c=np.asarray(c, dtype=float),
        integrality=np.asarray(integrality, dtype=int),
        bounds=variable_bounds,
        constraints=constraint,
    )
    if not result.success:
        raise RuntimeError(f"MILP 求解失败：{result.message}")
    return {
        "x": result.x,
        "objective": float(result.fun),
        "mip_gap": getattr(result, "mip_gap", None),
    }


def weighted_sum_multiobjective(
    objectives: Sequence,
    weights: ArrayLike,
    x: ArrayLike,
    *,
    ideal: ArrayLike | None = None,
    nadir: ArrayLike | None = None,
) -> float:
    """归一化加权和标量化；所有目标函数须已统一为“越小越好”。"""
    w = np.asarray(weights, dtype=float).reshape(-1)
    values = np.array([float(f(np.asarray(x, dtype=float))) for f in objectives])
    if len(w) != len(values) or np.any(w < 0) or w.sum() <= 0:
        raise ValueError("权重与目标数不一致，或权重无效")
    w /= w.sum()
    if ideal is not None and nadir is not None:
        lo, hi = np.asarray(ideal, float), np.asarray(nadir, float)
        if np.any(hi <= lo):
            raise ValueError("nadir 必须逐项大于 ideal")
        values = (values - lo) / (hi - lo)
    return float(w @ values)


def zero_one_knapsack(
    values: Sequence[float], weights: Sequence[int], capacity: int
) -> tuple[float, list[int]]:
    """0-1 背包动态规划，返回最大价值与选中物品下标。"""
    if len(values) != len(weights) or capacity < 0 or any(w <= 0 for w in weights):
        raise ValueError("价值/重量长度需一致，重量为正整数，容量非负")
    n = len(values)
    dp = np.zeros((n + 1, capacity + 1), dtype=float)
    for i, (value, weight) in enumerate(zip(values, weights), start=1):
        dp[i] = dp[i - 1]
        if weight <= capacity:
            candidate = dp[i - 1, : capacity + 1 - weight] + value
            dp[i, weight:] = np.maximum(dp[i, weight:], candidate)
    chosen: list[int] = []
    cap = capacity
    for i in range(n, 0, -1):
        if not np.isclose(dp[i, cap], dp[i - 1, cap]):
            chosen.append(i - 1)
            cap -= weights[i - 1]
    return float(dp[n, capacity]), chosen[::-1]


def greedy_interval_scheduling(
    intervals: Sequence[tuple[float, float, Any]]
) -> list[tuple[float, float, Any]]:
    """按最早结束时间选择最多互不重叠区间；适用于无权区间调度。"""
    ordered = sorted(intervals, key=lambda item: item[1])
    selected: list[tuple[float, float, Any]] = []
    last_end = -np.inf
    for item in ordered:
        start, end, _ = item
        if end < start:
            raise ValueError("区间结束时间不能早于开始时间")
        if start >= last_end:
            selected.append(item)
            last_end = end
    return selected
