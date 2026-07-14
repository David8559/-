---
type: project-code
project: "2020国赛B题-穿越沙漠研究"
status: active
tags: [competition/国赛, year/2020, problem/B题, topic/动态规划, topic/图论]
---

# 2020 国赛 B 题核心代码

本目录不是扫描代码的逐字抄录，而是基于四篇论文算法与附件规则整理的、可审计的 Python 重构版。论文中的原始语言、文件名和依赖见 [[四篇论文核心代码索引]]。

## 已整理内容

- `src/b078_core.py`：B078 的 Floyd、最少物资贪心、特殊节点回溯剪枝和随机天气生成。
- `src/run_b078.py`：运行第一关并导出逐日审计表。
- `data/b078_first_level_strategy.csv`：B078 第一关 `10470` 策略的程序输出。
- `data/level4_b078_distance_matrix.csv`：B078 第四关代码中 `dis[26][26]` 去除 0 号占位后的 25×25 距离矩阵。
- `data/level4_b078_nodes.csv`：第四关节点类型；起点 1、村庄 14、矿山 18、终点 25。
- `src/graph_reconstruction.py`：由距离矩阵反推邻接边，并以 Floyd–Warshall 回算验证。
- `src/desert_core.py`：统一状态、购买、移动、停留、挖矿和终点结算规则。
- `tests/test_core.py`：图闭环和核心规则的自动测试。
- [[B078核心算法实现说明]]：算法与论文附录的逐项映射。
- [[2020-B题-B078第四关地图与邻接关系]]：第四关代码矩阵推出的地图。

## 运行

在本目录执行：

```powershell
python src/graph_reconstruction.py
python src/run_b078.py
python -m unittest discover -s tests -v
```

图脚本会生成 `data/level4_b078_edges.csv`。B078 运行器会复现第一关不挖矿 `9410`、含挖矿 `10470`，并生成策略 CSV。

## 当前边界

- B078 第一关按论文实际使用的 4 个特殊节点距离矩阵完成回溯搜索，已复现 `10470`。
- B078 第四关的 25 节点图已完整恢复并自动验证。
- B108 第一关使用 27 节点编号，第二关使用 64 节点编号；扫描页中的超长 `wmap` 行被页面裁切，目前只保留为独立图版本，不能与 B078 强行合并。
- B125、B175 的完整邻接矩阵存于论文所述 `u1.mat`，当前资料中没有该文件；已整理其算法结构和依赖，但不伪造缺失矩阵。
