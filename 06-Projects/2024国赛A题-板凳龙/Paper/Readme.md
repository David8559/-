---
type: project-paper
status: outline
updated: 2026-07-28
tags: [project/paper, topic/论文写作]
---

# Paper

论文正文尚未开始写入数值结论。当前只建立证据驱动的大纲。

## 适用格式

当前按 [[Data/Raw/论文格式规范-2026.pdf|全国大学生数学建模竞赛论文格式规范（2026年修订稿）]] 准备：

- 电子版论文为单独的 PDF 或 Word 文件，建议 PDF，大小不超过 20MB；
- 电子版不含承诺书和编号专用页，第一页必须为摘要专用页；
- 摘要含标题和关键词，原则上不超过一页，不要求英文摘要；
- 正文从摘要后的下一页开始，不要目录，正文不超过 30 页；
- 附录页数不限，需给出支撑材料文件列表及全部完整、可运行源代码；
- 论文和支撑材料必须一致，支撑材料单独压缩为 RAR 或 ZIP，不超过 20MB；
- 摘要、正文、附录和支撑材料均不得出现队员、学校和赛区身份信息；
- 引用公开资料必须列入参考文献，并在正文对应位置标注。

该规范是 2026 年修订稿；本项目使用 2024 年赛题作练习，最终以实际参赛年份的报名须知和赛区要求再次核对。

## 建议标题

基于弧长参数化与刚性链约束的板凳龙盘入、碰撞及调头优化

## 论文结构

1. 摘要：最后完成，必须包含五问方法、关键数值和验证。
2. 问题重述：用任务语言概括五问，不复制大段原题。
3. 问题分析：说明五问依赖关系和统一求解器。
4. 模型假设：逐条说明合理性、影响和失效情形。
5. 符号说明：统一几何、路径、把手、速度和碰撞符号。
6. 问题 1：螺线运动学和链式位置速度递推。
7. 问题 2：板凳有宽度碰撞模型与临界时刻。
8. 问题 3：以可行性为约束的最小螺距搜索。
9. 问题 4：相切双圆弧调头路径优化和全队运动。
10. 问题 5：速度放大系数和龙头最大速度。
11. 模型检验：距离、速度、碰撞、切向、容差和敏感性。
12. 模型评价与推广。
13. 参考文献。
14. 附录：核心代码、运行说明和结果文件。

## 证据规则

论文中的每个关键数字必须记录：

| 论文位置 | 结果含义 | 生成脚本 | 参数/版本 | 输出文件 | 验证 |
|---|---|---|---|---|---|
| 问题 1 几何验证图 | 三节板凳固定弦长递推与残差 | `Code/plot_three_benches.py` | Python 3.12.5；NumPy 2.4.3；Matplotlib 3.10.8 | `Paper/Figures/q1_three_benches_validation.pdf` | 13 组测试通过；最大弦长误差 $4.827\times10^{-13}$ m |
| 问题 1 速度验证图 | 三节板凳解析速度、中心差分和约束导数残差 | `Code/plot_velocity_validation.py` | Python 3.12.5；NumPy 2.4.3；Matplotlib 3.10.8；SymPy 1.14.0；差分步长 $10^{-3}$ s | `Paper/Figures/q1_three_benches_velocity_validation.pdf` | 最大速度误差 $6.680\times10^{-9}$ m/s；最大约束导数残差 $9.714\times10^{-16}$ m²/s |
| 问题 1 完整结果 | 224 把手在 0–300 s 的逐秒位置和速度 | `Code/solve_problem1.py` | 223 段固定弦；301 个整数时刻；写入时保留 6 位小数 | `Paper/Outputs/result1.xlsx` | 15 组测试通过；全链最大弦长误差 $6.763\times10^{-13}$ m；工作簿重开与分区渲染通过 |
| 问题 2 碰撞验证图 | 定向矩形首次接触与全队最小分离余量 | `Code/plot_collision_validation.py` | 实际板长；宽 0.30 m；非相邻板凳 SAT | `Paper/Figures/q2_first_collision_validation.pdf` | 临界前后 $1\,\mu$s 余量异号；0.25 s 密集扫描与碰撞对一致 |
| 问题 2 完整结果 | 临界时刻 224 把手的位置和速度 | `Code/solve_problem2.py` | 1 s 粗扫描；$10^{-12}$ s 二分容差 | `Paper/Outputs/result2.xlsx` | $t^\ast=412.473837682115$ s；全链最大弦长误差 $3.122\times10^{-13}$ m；工作簿重开与分区渲染通过 |
| 问题 3 最小螺距 | 从第 16 圈到 4.5 m 边界的全路径可行性阈值 | `Code/solve_problem3.py`、`Code/plot_pitch_feasibility.py` | 内层黄金分割；外层 $10^{-12}$ m 二分；480 段全体板凳复核 | `Paper/Outputs/problem3_result.json`、`Paper/Figures/q3_minimum_pitch_validation.pdf` | $p^\ast=0.450337393027$ m；临界对为 0 与 19；$\pm1\,\mu$m 螺距扰动余量异号 |
| 问题 4 调头路径 | 固定边界切点假设下的螺线—双圆弧—螺线相切路径与速度场 | `Code/solve_problem4.py`、`Code/plot_turning_validation.py` | $p=1.7$ m；$R_1:R_2=2:1$；单位弧长参数；首根扫描加二分；201 个整数时刻 | `Paper/Outputs/result4.xlsx`、`Paper/Figures/q4_turning_path_validation.pdf` | 三处位置/切向连续；最大弦长误差 $5.036\times10^{-13}$ m；整数采样最小碰撞余量 $0.289465$ m；完整逐秒回归、工作簿重开与渲染通过 |
| 问题 5 最大速度 | 固定调头路径上所有把手速度不超过 2 m/s 时的龙头恒定速度上限 | `Code/solve_problem5.py`、`Code/plot_speed_limit_validation.py` | $s_0\in[0,400]$ m；$0.1$ m 全域网格；黄金分割连续细化；$0.001$ m 局部密扫；正负尾部复核 | `Paper/Outputs/problem5_result.json`、`Paper/Figures/q5_speed_limit_validation.pdf` | $K_{\max}=1.604793378967$；$v_{0,\max}=1.246266358157$ m/s；缩放后峰值 2 m/s；弦长误差 $3.664\times10^{-13}$ m；差分速度误差 $1.938\times10^{-10}$ m/s |

## 当前禁止写入

- 未运行的数值；
- 未核实的参考文献；
- 没有实验支持的“精度高”“效果好”；
- 与代码定义不一致的符号和公式；
- 只根据图形观察得到的临界结论。
