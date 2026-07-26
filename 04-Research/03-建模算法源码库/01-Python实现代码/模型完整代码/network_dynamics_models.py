"""图论、排队论与动力学模型的基础实现。"""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np
from numpy.typing import ArrayLike


def shortest_path(
    edges: Iterable[tuple[object, object, float]], source: object, target: object
) -> tuple[list[object], float]:
    """非负权图最短路（NetworkX 自动选择合适接口）。"""
    import networkx as nx

    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)
    path = nx.shortest_path(graph, source, target, weight="weight")
    length = nx.shortest_path_length(graph, source, target, weight="weight")
    return path, float(length)


def minimum_spanning_tree(
    edges: Iterable[tuple[object, object, float]]
) -> tuple[list[tuple[object, object, dict]], float]:
    """无向图最小生成树；非连通输入会得到最小生成森林。"""
    import networkx as nx

    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)
    tree = nx.minimum_spanning_tree(graph, weight="weight", algorithm="kruskal")
    return list(tree.edges(data=True)), float(tree.size(weight="weight"))


def maximum_flow_minimum_cut(
    edges: Iterable[tuple[object, object, float]], source: object, sink: object
) -> dict[str, object]:
    """有向容量网络的最大流与对应最小割。"""
    import networkx as nx

    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges, weight="capacity")
    flow_value, flow = nx.maximum_flow(graph, source, sink, capacity="capacity")
    cut_value, partition = nx.minimum_cut(graph, source, sink, capacity="capacity")
    return {
        "max_flow": float(flow_value),
        "flow": flow,
        "min_cut": float(cut_value),
        "partition": partition,
    }


def mm1_metrics(arrival_rate: float, service_rate: float) -> dict[str, float]:
    """M/M/1 稳态指标；速率单位须一致，且 lambda < mu。"""
    lam, mu = float(arrival_rate), float(service_rate)
    if not 0 <= lam < mu:
        raise ValueError("稳态 M/M/1 必须满足 0 <= lambda < mu")
    rho = lam / mu
    return {
        "utilization_rho": rho,
        "mean_number_system_L": rho / (1 - rho),
        "mean_number_queue_Lq": rho**2 / (1 - rho),
        "mean_time_system_W": 1 / (mu - lam),
        "mean_time_queue_Wq": lam / (mu * (mu - lam)),
    }


def simulate_sir(
    beta: float,
    gamma: float,
    initial: tuple[float, float, float],
    t_eval: ArrayLike,
):
    """SIR 常微分方程；状态既可用人数也可用比例，但三者单位必须一致。"""
    from scipy.integrate import solve_ivp

    t = np.asarray(t_eval, dtype=float)
    if len(t) < 2 or min(beta, gamma, *initial) < 0:
        raise ValueError("参数、初值需非负，且至少给两个时间点")
    population = sum(initial)

    def rhs(_t, y):
        s, i, r = y
        incidence = beta * s * i / population
        return (-incidence, incidence - gamma * i, gamma * i)

    return solve_ivp(rhs, (t[0], t[-1]), initial, t_eval=t, rtol=1e-8, atol=1e-10)


def simulate_logistic(
    growth_rate: float, capacity: float, initial: float, t_eval: ArrayLike
):
    """Logistic 增长 dN/dt = r*N*(1-N/K)。"""
    from scipy.integrate import solve_ivp

    t = np.asarray(t_eval, dtype=float)
    if len(t) < 2 or growth_rate <= 0 or capacity <= 0 or initial <= 0:
        raise ValueError("r、K、N0 必须为正，且至少给两个时间点")
    return solve_ivp(
        lambda _t, y: growth_rate * y * (1 - y / capacity),
        (t[0], t[-1]),
        [initial],
        t_eval=t,
        rtol=1e-8,
        atol=1e-10,
    )


def diffuse_1d_explicit(
    initial: ArrayLike,
    diffusivity: float,
    dx: float,
    dt: float,
    steps: int,
) -> np.ndarray:
    """一维热/扩散方程显式差分，端点采用固定边界。

    稳定条件为 r = D*dt/dx^2 <= 1/2。
    """
    u = np.asarray(initial, dtype=float).copy()
    r = diffusivity * dt / dx**2
    if u.ndim != 1 or len(u) < 3 or min(diffusivity, dx, dt, steps) <= 0:
        raise ValueError("输入与网格参数无效")
    if r > 0.5:
        raise ValueError("显式格式不稳定：需要 D*dt/dx^2 <= 0.5")
    history = np.empty((steps + 1, len(u)))
    history[0] = u
    for k in range(1, steps + 1):
        new = u.copy()
        new[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
        u = new
        history[k] = u
    return history
