---
type: project-code
status: active
updated: 2026-07-28
tags: [project/code, tool/python]
---

# Code

已确认使用 Python。问题 1–5 的链式运动学、碰撞临界、最小螺距、双圆弧调头路径和连续时间速度上限均已完成。

## 跨项目复用

本项目保留完成时的自包含代码快照。已把二分求根和统一约束审计骨架提炼到 [[04-Research/03-建模算法源码库/00-公共复用模块/Readme|公共复用模块]]；后续项目应固定公共模块版本，不反向改写本项目的已验证结果。

## 当前结构

```text
Code/
├─ src/
│  ├─ geometry.py               # 螺线、弧长和龙头状态
│  ├─ chain.py                  # 固定弦长位置与速度递推
│  ├─ collision.py              # 板凳定向矩形与 SAT 碰撞判定
│  ├─ pitch_feasibility.py      # 问题 3 全路径螺距可行性
│  ├─ turning_path.py           # 问题 4 分段相切路径
│  ├─ path_chain.py             # 一般弧长路径上的刚性链
│  └─ speed_limit.py            # 问题 5 速度放大系数与连续极值
├─ tests/
│  ├─ test_head_trajectory.py
│  ├─ test_chain_positions.py
│  ├─ test_chain_velocities.py
│  ├─ test_full_chain.py
│  ├─ test_collision.py
│  ├─ test_pitch_feasibility.py
│  ├─ test_turning_path.py
│  ├─ test_path_chain.py
│  ├─ test_full_turning_chain.py
│  ├─ test_symbolic_velocity_derivation.py
│  └─ test_speed_limit.py
├─ plot_three_benches.py        # 三节板凳几何和弦长残差图
├─ plot_velocity_validation.py  # 速度、中心差分和约束导数残差图
├─ plot_collision_validation.py # 首次接触几何和事件定位图
├─ plot_pitch_feasibility.py    # 最小螺距临界构型和阈值图
├─ plot_turning_validation.py   # 调头路径和全链速度场
├─ plot_speed_limit_validation.py # 连续速度峰值与局部细化图
├─ solve_problem1.py            # 224 把手、0–300 s 全链求解与验证
├─ solve_problem2.py            # 首次物理碰撞搜索与临界状态
├─ solve_problem3.py            # 全路径最小螺距双层搜索
├─ solve_problem4.py            # −100–100 s 调头全链求解
├─ solve_problem5.py            # 连续路径速度上限搜索
└─ requirements.txt
```

## 当前验证

执行：

```powershell
python -m unittest discover -s Code\tests -p "test_*.py" -v
```

环境：Python 3.12.5、NumPy 2.4.3、Matplotlib 3.10.8、SymPy 1.14.0。

结果：35 个测试全部通过。问题 4 的完整链回归覆盖 $t=-100,-99,\ldots,100$ s 全部 201 个官方输出时刻，每个时刻均求解 224 个把手并检查弦长、顺序和非相邻板凳分离余量；问题 5 另检查速度线性缩放、连续峰值定位、路径域覆盖和黄金分割极值器。

当前三节板凳的误差上界：

- 最大弦长误差：$4.827\times10^{-13}$ m；
- 最大速度交叉验证误差：$6.680\times10^{-9}$ m/s；
- 最大约束导数残差：$9.714\times10^{-16}$ m²/s。

完整问题 1 求解：

```powershell
python Code\solve_problem1.py --json-output <临时 JSON 路径>
```

全链结果为 301 个时刻 × 224 个把手；最大弦长误差 $6.763\times10^{-13}$ m，速度范围 $[0.996477539766,1.000000000000]$ m/s。派生工作簿位于 `Paper/Outputs/result1.xlsx`。

问题 2 求解：

```powershell
python Code\solve_problem2.py --json-output <临时 JSON 路径>
```

首次接触时间为 $412.473837682115$ s，碰撞对为龙头板凳与第 8 节龙身板凳；派生工作簿位于 `Paper/Outputs/result2.xlsx`。

问题 3 求解：

```powershell
python Code\solve_problem3.py --json-output Paper\Outputs\problem3_result.json
```

最小螺距为 $p^\ast=0.450337393027$ m，临界接触对为龙头板凳与第 19 节龙身板凳，接触时龙头半径为 $4.572603257399$ m。若必须以 6 位小数给出严格可行值，使用 $0.450338$ m。

问题 4 求解：

```powershell
python Code\solve_problem4.py --json-output <临时 JSON 路径>
```

两圆弧半径为 $3.005417667789$ m 和 $1.502708833895$ m，总弧长为 $13.621244906821$ m。最近根使用“小步扫描 + 二分”确定性求解；201×224 状态的最大弦长误差为 $5.036\times10^{-13}$ m，整数采样时刻的最小板凳分离余量为 $0.289465$ m；派生工作簿位于 `Paper/Outputs/result4.xlsx`。

问题 5 求解：

```powershell
python Code\solve_problem5.py --json-output Paper\Outputs\problem5_result.json --workers 8
```

固定路径下速度递推对龙头速度线性，因此先令龙头速度为 $1$ m/s，求
$K_{\max}=\max_{s_0}\max_i v_i(s_0;1)$，再由 $v_{0,\max}=2/K_{\max}$ 反推上限。对龙头弧长坐标 $s_0\in[0,400]$ m 以 $0.1$ m 全域扫描，随后用黄金分割和 $0.001$ m 局部密扫细化，得到
$K_{\max}=1.604793378967$，发生在 $s_0=14.479969626472$ m，把手 $P_3$–$P_7$ 并列主动；最大龙头恒定速度为 $1.246266358157$ m/s，六位小数安全报告值为 $1.246266$ m/s。

缩放后最大把手速度为 $2.000000000000$ m/s；最大弦长误差 $3.664\times10^{-13}$ m，最大约束导数残差 $8.882\times10^{-16}$ m²/s，中心差分速度误差 $1.938\times10^{-10}$ m/s。负向尾部和 $400$–$800$ m 正向尾部均低于主峰，峰值两侧扰动均下降。只用整数时刻会得到错误上限 $1.406276657321$ m/s，并使真实峰值达到 $2.256783468665$ m/s。

验证图：

- `Paper/Figures/q1_three_benches_validation.png`：600 DPI；
- `Paper/Figures/q1_three_benches_validation.pdf`：矢量版本；
- `Paper/Figures/q1_three_benches_velocity_validation.png`：600 DPI；
- `Paper/Figures/q1_three_benches_velocity_validation.pdf`：矢量版本；
- `Paper/Figures/q2_first_collision_validation.png`：600 DPI；
- `Paper/Figures/q2_first_collision_validation.pdf`：矢量版本。
- `Paper/Figures/q3_minimum_pitch_validation.png`：600 DPI；
- `Paper/Figures/q3_minimum_pitch_validation.pdf`：矢量版本。
- `Paper/Figures/q4_turning_path_validation.png`：600 DPI；
- `Paper/Figures/q4_turning_path_validation.pdf`：矢量版本；
- `Paper/Figures/q5_speed_limit_validation.png`：600 DPI；
- `Paper/Figures/q5_speed_limit_validation.pdf`：矢量版本。

## 最低验证要求

- 相邻把手距离误差；
- 螺线参数和节点顺序单调性；
- 龙头速度误差；
- 路径切向连续性；
- 碰撞临界前后状态；
- 时间步长、根求解容差和随机因素的稳定性；
- Excel 尺寸、表头、精度和非有限值检查；
- 非代码作者可以按说明重跑核心结果。
