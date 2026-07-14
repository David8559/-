---
type: project-code
project: "2020国赛B题-穿越沙漠研究"
status: active
tags: [competition/国赛, year/2020, problem/B题, topic/动态规划, topic/图论]
---

# 2020 国赛 B 题核心代码

本目录不是扫描代码的逐字抄录，而是基于四篇论文算法与附件规则整理的、可审计的 Python 重构版。论文中的原始语言、文件名和依赖见 [[四篇论文核心代码索引]]。

## 已整理内容

- `data/level1_b078_distance_matrix.csv`：B078 附录 `dis[26][26]` 去除 0 号占位后的 25×25 距离矩阵。
- `data/level1_b078_nodes.csv`：B078 节点类型；起点 1、村庄 14、矿山 18、终点 25。
- `src/graph_reconstruction.py`：由距离矩阵反推邻接边，并以 Floyd–Warshall 回算验证。
- `src/desert_core.py`：统一状态、购买、移动、停留、挖矿和终点结算规则。
- `tests/test_core.py`：图闭环和核心规则的自动测试。
- [[2020-B题-第一关地图与邻接关系]]：Obsidian 可读地图、边表与证据说明。

## 运行

在本目录执行：

```powershell
python src/graph_reconstruction.py
python -m unittest discover -s tests -v
```

图脚本会生成 `data/level1_b078_edges.csv`，并在终端报告节点数、边数和闭环校验结果。

## 当前边界

- B078 的 25 节点第一关图已完整恢复并自动验证。
- B108 第一关使用 27 节点编号，第二关使用 64 节点编号；扫描页中的超长 `wmap` 行被页面裁切，目前只保留为独立图版本，不能与 B078 强行合并。
- B125、B175 的完整邻接矩阵存于论文所述 `u1.mat`，当前资料中没有该文件；已整理其算法结构和依赖，但不伪造缺失矩阵。
