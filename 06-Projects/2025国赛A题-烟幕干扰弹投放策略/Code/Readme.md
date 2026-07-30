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

## 最小测试集

- 初始时刻位置与速度。
- 投放瞬间位置连续。
- 起爆点由投放时刻和延迟唯一确定。
- 烟幕中心在起爆后按 3 m/s 下沉。
- 有效时间严格限制在起爆后 20 秒内。
- 区间端点附近的遮蔽真假值正确切换。
- 速度、航向、投放间隔和弹数约束均可程序化断言。
- Excel 输出字段、行数和数据类型符合原模板。
