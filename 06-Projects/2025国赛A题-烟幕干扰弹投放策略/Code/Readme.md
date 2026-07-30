---
type: project-code
status: active
updated: 2026-07-30
---

# 代码与复现

## 计划结构

- `src/`：轨迹、遮蔽判据、有效区间、优化、结果导出与绘图代码。
- `tests/`：解析解、边界条件、约束和结果模板测试。
- `outputs/`：可再生的数值结果、日志和中间图，不存放唯一证据。

## 已实现：问题 1

- `src/problem1_model.py`：轨迹、线段距离、完整圆柱/中心视线遮蔽判据、区间端点和解析复核。
- `src/run_problem1.py`：结果、时间序列和四组论文图的一键生成。
- `tests/test_problem1.py`：11 个轨迹、边界、收敛与复核测试。
- `outputs/problem1_result.json`：机器可读关键结果和运行环境。
- `outputs/problem1_timeseries.csv`：遮蔽距离、投影参数和导弹—烟幕距离时间序列。

### 实际运行环境

- Windows 11
- Python 3.12.5
- NumPy 2.4.3
- Matplotlib 3.10.8

### 复现命令

在项目根目录执行：

```powershell
python -m unittest discover -s Code/tests -p 'test_*.py' -v
python Code/src/run_problem1.py --output-dir Code/outputs --figure-dir Paper/figures
```

本次结果：11 个测试全部通过；完整圆柱判据时长 1.391643 s；目标中心基准时长 1.435082 s。

## 已实现：问题 2

- `src/problem2_model.py`：任意单弹策略的运动学、可行参数化、中心视线代理、完整圆柱目标函数、差分进化与坐标精化。
- `src/run_problem2.py`：三随机种子全局搜索、完整圆柱重排、离散收敛、JSON/CSV 和 5 组论文图的一键生成。
- `tests/test_problem2.py`：8 个策略转换、约束、轨迹、区间和问题 1 回归测试。
- `outputs/problem2_result.json`：最优参数、遮蔽区间、离散收敛和运行环境。
- `outputs/problem2_timeseries.csv`：最优策略的完整圆柱/中心视线距离时间序列。
- `outputs/problem2_optimization_history.csv`：三组差分进化收敛历史。
- `outputs/problem2_sensitivity.csv`：航向、速度、投放与引信延迟的单因素扰动。

### 复现命令

```powershell
python -m unittest discover -s Code/tests -p 'test_*.py' -v
python Code/src/run_problem2.py --output-dir Code/outputs --figure-dir Paper/figures
```

问题 1–2 共 19 个测试全部通过。问题 2 完整圆柱最优时长为 4.587672 s；三组中心视线代理搜索均收敛到约 4.83249 s 的同一主盆地，最终结果经 180–1440 周向点复算。

## 实现顺序

1. `geometry/kinematics`：导弹、无人机、干扰弹、烟幕中心轨迹。
2. `occlusion`：候选遮蔽判据与有效区间端点。
3. `problem1`：固定参数基准计算。
4. `optimization`：问题 2–5 的分层求解。
5. `export`：在派生副本上填写三个 Excel 模板并校验。
6. `figures`：论文图表统一生成。

## 绘图合同

每张图在编码前登记：

- 核心结论；
- 所需证据和数据来源；
- 图形类型及为何适合；
- 坐标、单位、颜色语义和关键标注；
- 导出格式与最终版面尺寸；
- 可能误导读者的风险。

默认采用 Python 科学计算栈；若后续变更语言，必须在状态页登记。最终图形优先导出 SVG/PDF，位图预览不少于 300 dpi，并在最终排版尺寸下人工检查字体、线宽和标注。

### 工具路由

| 场景 | 首选工具 | 备用或后续工具 |
|---|---|---|
| 数据比较、统计分布、回归、时间序列与预测 | Matplotlib | Seaborn、Plotly、Origin |
| 优化过程、收敛性、灵敏度与参数空间 | Matplotlib | Plotly；三维问题可用 MATLAB |
| 网络拓扑、路径规划与车辆路径 | NetworkX | 未安装时用 Matplotlib 绘制简化节点—边图 |
| 空间分布、热力地图与聚类地图 | GeoPandas、Folium | 未安装时先绘制坐标系中的空间散点、轨迹或热力图 |
| 三维曲面、等高线、曲率和相图 | Matplotlib、MATLAB | Origin 用于最终科研风格美化 |
| 评价模型、特征解释与降维 | Matplotlib | Plotly、scikit-learn、SHAP、UMAP |
| 技术路线、算法流程和系统框图 | PPT、Visio/亿图图示 | 工具不可用时采用可编辑的 Mermaid 或简洁矢量图 |
| 最终矢量美化 | 原绘图工具直接导出 SVG/PDF | Origin、Illustrator；不得丢失原始数据、代码或可编辑源文件 |

问题 1 的四组图继续使用 Matplotlib。问题 2 优先生成目标函数地形、收敛曲线和灵敏度图；问题 3–5 的时间调度、路径和任务分配图可先用 Matplotlib，待 Plotly 或 NetworkX 可用后再按展示需要升级。是否使用某类图由模型结论和证据需求决定。

### 当前可用性（2026-07-30）

- 已验证可调用：Python 3.12.5、NumPy 2.4.3、Pandas、Matplotlib 3.10.8、MATLAB（`D:\bin\matlab.exe`）。
- 当前 Python 环境未检测到：Seaborn、Plotly、NetworkX、GeoPandas、Folium、scikit-learn、SHAP、UMAP。
- 当前命令环境未检测到：Origin、Visio、PowerPoint、Illustrator；这不排除存在未加入命令路径的桌面安装。
- 不为本项目自行安装缺失软件；先用已验证工具完成可复现图表，用户安装新工具后再复查可用性。

## 最小测试集

- 初始时刻位置与速度。
- 投放瞬间位置连续。
- 起爆点由投放时刻和延迟唯一确定。
- 烟幕中心在起爆后按 3 m/s 下沉。
- 有效时间严格限制在起爆后 20 秒内。
- 区间端点附近的遮蔽真假值正确切换。
- 速度、航向、投放间隔和弹数约束均可程序化断言。
- Excel 输出字段、行数和数据类型符合原模板。
