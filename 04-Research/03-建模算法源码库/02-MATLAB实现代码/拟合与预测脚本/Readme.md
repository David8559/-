---
type: code-index
status: active
tags: [area/数学建模, tool/MATLAB, topic/预测模型]
---

# MATLAB 评价、拟合与预测脚本

| 文件 | 调用方法 |
|---|---|
| [evaluation_models.m](evaluation_models.m) | `"ahp"`、`"entropy"`、`"topsis"`、`"gra"`、`"fuzzy"` |
| [forecast_models.m](forecast_models.m) | `"ols"`、`"ses"`、`"gm11"`、`"arima"`、`"lstm-layers"` |
| [dynamics_models.m](dynamics_models.m) | `"sir"`、`"logistic"`、`"diffusion"` |

统一入口示例：`[w, CR, ok] = evaluation_models("ahp", A)`。工具箱依赖见 [[04-Research/03-建模算法源码库/Readme|源码库说明]]。
