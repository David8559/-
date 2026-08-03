"""Uniform constraint-violation reporting for optimization results."""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ConstraintViolationReport:
    maximum: float
    inequality: float
    equality: float
    lower_bound: float
    upper_bound: float
    feasible: bool
    tolerance: float


def _maximum(values: Iterable[float], *, absolute: bool = False) -> float:
    array = np.asarray(list(values), dtype=float)
    if array.size == 0:
        return 0.0
    if not np.all(np.isfinite(array)):
        return float("inf")
    if absolute:
        array = np.abs(array)
    return float(np.max(array))


def constraint_violation_report(
    decision: Sequence[float],
    *,
    inequalities: Iterable[float] = (),
    equalities: Iterable[float] = (),
    lower_bounds: Sequence[float] | None = None,
    upper_bounds: Sequence[float] | None = None,
    tolerance: float = 1e-8,
) -> ConstraintViolationReport:
    """Report violations for ``g(x)<=0``, ``h(x)=0`` and optional bounds."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    vector = np.asarray(decision, dtype=float)
    if vector.ndim != 1 or not np.all(np.isfinite(vector)):
        raise ValueError("decision must be a finite one-dimensional vector")
    inequality = max(0.0, _maximum(inequalities))
    equality = _maximum(equalities, absolute=True)
    lower_violation = upper_violation = 0.0
    if lower_bounds is not None:
        lower = np.asarray(lower_bounds, dtype=float)
        if lower.shape != vector.shape:
            raise ValueError("lower bounds must match the decision shape")
        lower_violation = max(0.0, _maximum(lower - vector))
    if upper_bounds is not None:
        upper = np.asarray(upper_bounds, dtype=float)
        if upper.shape != vector.shape:
            raise ValueError("upper bounds must match the decision shape")
        upper_violation = max(0.0, _maximum(vector - upper))
    maximum = max(inequality, equality, lower_violation, upper_violation)
    return ConstraintViolationReport(
        maximum=maximum,
        inequality=inequality,
        equality=equality,
        lower_bound=lower_violation,
        upper_bound=upper_violation,
        feasible=maximum <= tolerance,
        tolerance=tolerance,
    )
