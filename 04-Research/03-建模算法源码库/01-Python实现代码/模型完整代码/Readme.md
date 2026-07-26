---
type: code-index
status: active
tags: [area/数学建模, tool/Python]
---

# Python 模型完整代码

| 文件 | 核心函数 |
|---|---|
| [evaluation_models.py](evaluation_models.py) | `ahp_weights`、`entropy_weights`、`topsis`、`grey_relational_grade`、`fuzzy_comprehensive_evaluation` |
| [forecast_models.py](forecast_models.py) | `linear_regression_ols`、`simple_exponential_smoothing`、`gm11`、`arima_forecast`、`build_lstm` |
| [network_dynamics_models.py](network_dynamics_models.py) | `shortest_path`、`minimum_spanning_tree`、`maximum_flow_minimum_cut`、`mm1_metrics`、`simulate_sir`、`simulate_logistic`、`diffuse_1d_explicit` |

每个函数只保留算法核心和输入检查，不绑定示例数据。对应原理、适用边界和验证要求从 [[04-Research/02-经典建模模型库/Readme|经典模型库]] 进入。
