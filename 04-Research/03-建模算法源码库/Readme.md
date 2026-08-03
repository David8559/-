---
type: map-of-content
tags: [area/数学建模, topic/建模算法源码库]
---

# 建模算法源码库

Python 与 MATLAB 的可复现基础实现、绘图和求解代码。这里的代码用于复习算法骨架和快速建立比赛基线；实际项目应复制到 `06-Projects/<项目>/Code`，补齐真实数据接口、环境、参数和测试。

唯一入口保留在本页；新项目优先使用 [[04-Research/03-建模算法源码库/00-公共复用模块/Readme|公共复用模块]]，Python 模型函数集中在 [模型完整代码](01-Python实现代码/模型完整代码/)，优化与智能算法集中在 [优化求解代码](01-Python实现代码/优化求解代码/)。逐文件验证等级见 [[代码验证报告]] 与 [[代码验证状态.csv]]。

## 公共复用层

- `mm_common.intervals`：区间并、交、测度与删除边际。
- `mm_common.roots`：保留括区间的事件二分求根。
- `mm_common.optimization`：带可行性过滤和 incumbent guard 的差分进化与坐标精修。
- `mm_common.validation`：统一约束违反量报告。

公共层来自 2024/2025 项目的稳定算法骨架，但不包含赛题参数；12 项单元测试已在 Python 3.12.5、NumPy 2.4.3 下通过。完成项目继续保留自包含快照，未来项目从公共层固定版本，避免跨项目隐式漂移。

## 本轮新增基础实现

| 模型族 | Python | MATLAB |
|---|---|---|
| AHP、熵权、TOPSIS、灰色关联、模糊综合评价 | [evaluation_models.py](01-Python实现代码/模型完整代码/evaluation_models.py) | [evaluation_models.m](02-MATLAB实现代码/拟合与预测脚本/evaluation_models.m) |
| OLS、指数平滑、GM(1,1)、ARIMA、LSTM | [forecast_models.py](01-Python实现代码/模型完整代码/forecast_models.py) | [forecast_models.m](02-MATLAB实现代码/拟合与预测脚本/forecast_models.m) |
| LP、MILP、多目标加权和、0-1 背包、区间贪心 | [optimization_models.py](01-Python实现代码/优化求解代码/optimization_models.py) | [optimization_network_models.m](02-MATLAB实现代码/规划求解代码/optimization_network_models.m) |
| 最短路、MST、最大流最小割、M/M/1、SIR、Logistic、扩散 | [network_dynamics_models.py](01-Python实现代码/模型完整代码/network_dynamics_models.py) | [optimization_network_models.m](02-MATLAB实现代码/规划求解代码/optimization_network_models.m)、[dynamics_models.m](02-MATLAB实现代码/拟合与预测脚本/dynamics_models.m) |
| GA、PSO、SA、ACO-TSP | [metaheuristics.py](01-Python实现代码/优化求解代码/metaheuristics.py) | [metaheuristics.m](02-MATLAB实现代码/智能算法代码/metaheuristics.m) |

共覆盖现有 26 个经典模型节点。代码不内置赛题数据；函数参数就是数据/目标/约束接口，便于后续项目调用。

## 依赖与环境

- Python 3.10+；基础评价算法使用 NumPy。
- LP/MILP/ODE 需要 SciPy；ARIMA 需要 statsmodels；图算法需要 NetworkX；LSTM 需要 Keras。
- MATLAB 基础矩阵函数可直接使用；`linprog/intlinprog` 需要 Optimization Toolbox，`arima` 需要 Econometrics Toolbox，`ga/particleswarm/simulannealbnd` 需要 Global Optimization Toolbox，LSTM 需要 Deep Learning Toolbox。
- 随机算法必须显式记录 `seed`，多次运行并报告最好值、均值、标准差和函数评估预算。

## 使用前检查

1. 阅读对应的模型 `Readme.md`，确认适用条件与输入方向。
2. 把代码复制到具体项目，禁止直接在本库模板上硬编码赛题数据。
3. 安装依赖并记录版本；先运行小规模可手算样例。
4. 检查求解状态、约束违反、残差/误差和敏感性。
5. 未实际运行的实现标注“未运行”，不要将语法通过写成结果已验证。

## 验证记录（2026-07-26）

- Python：5 个源码文件通过 `py_compile`；在 Python 3.12 的临时环境中对 25 个可调用分支完成数值冒烟测试。Keras 未作为测试依赖安装，`build_lstm` 仅完成语法检查。
- MATLAB：本机实际调用 17 个无额外工具箱或自实现分支通过；`arima`、LSTM、`linprog/intlinprog`、GA/PSO/SA 的工具箱分支未在本次冒烟测试中执行。
- 验证只覆盖算法接口和小型基准，不代表任何具体赛题的数据、参数或结论已经复现。

## 当前复核（2026-08-03）

- 原始资料：1323 个去重实现、1566 个源路径全部可追溯；347/347 个 Python 实现通过 AST 解析。静态解析不等于运行验证。
- 精选 Python 库：5 个文件通过语法检查；持久化冒烟测试覆盖 25 个分支，其中当前环境执行 17 个，SciPy、NetworkX、statsmodels 缺失导致 8 个明确跳过；Keras/LSTM 仍未执行。
- 公共复用模块：12 项单元测试全部通过。
- 机器可读状态和复现命令见 [[代码验证报告]]；不再用单一“已验证/未验证”掩盖不同证据等级。

新增原始资料的检索入口：[[代码资料索引]]。完整文件级目录见 [[基础资料文件清单.csv]]，源代码目录见 [[代码文件索引.csv]]。

代码内容已并入 [[04-Research/00-知识导航/Topic Index]] 下各自对应的主题目录：按算法和用途在 Hub 内细分，直接阅读原始源码与本地数据依赖，不为单个文件或资料包新增节点。

> [!warning]
> `00-Inbox/Downloaded` 中的代码属于原始资料，尚未全部验证。只有补齐依赖、输入输出说明和测试的代码，才视为正式可复现实现。

## 外部参考

- [SciPy optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [statsmodels 时间序列](https://www.statsmodels.org/stable/tsa.html)
- [NetworkX 算法](https://networkx.org/documentation/stable/reference/algorithms/)
- [MathWorks 图与网络算法](https://www.mathworks.com/help/matlab/graph-and-network-algorithms.html)
- [pyDecision GitHub](https://github.com/Valdecy/pyDecision)
- [pymoo GitHub](https://github.com/anyoptimization/pymoo)
- [scikit-fuzzy GitHub](https://github.com/scikit-fuzzy/scikit-fuzzy)

返回 [[04-Research/Readme|Research Index]]，跨主题浏览 [[Topic Index]]。
