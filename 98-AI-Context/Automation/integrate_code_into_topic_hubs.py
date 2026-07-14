#!/usr/bin/env python3
"""Embed every local source file into the existing mathematical-modeling hubs.

This generator creates no code-file, data-file, language, package, or folder
nodes. Exact duplicates share one embedded implementation; similar sources are
kept as variants under one heading. Every original path remains traceable.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import build_code_knowledge_graph as core


BEGIN = "<!-- BEGIN AUTO-INTEGRATED-CODE -->"
END = "<!-- END AUTO-INTEGRATED-CODE -->"
LANG_BEGIN = "<!-- BEGIN AUTO-LANGUAGE-CODE-INDEX -->"
LANG_END = "<!-- END AUTO-LANGUAGE-CODE-INDEX -->"
STUDY_BEGIN = "<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->"
STUDY_END = "<!-- END AUTO-HUB-STUDY-GUIDE -->"
HUB_DIR = core.VAULT / "04-Research" / "00-Topic-Hubs"

MODEL_HUB = {
    "AHP层次分析": "评价模型 Hub", "TOPSIS": "评价模型 Hub", "熵权法": "评价模型 Hub",
    "模糊综合评价": "评价模型 Hub", "灰色关联分析": "评价模型 Hub", "主成分分析PCA": "评价模型 Hub",
    "回归分析": "预测模型 Hub", "ARIMA时间序列": "预测模型 Hub", "指数平滑": "预测模型 Hub",
    "灰色预测GM": "预测模型 Hub", "LSTM预测": "预测模型 Hub",
    "线性规划": "优化模型 Hub", "整数规划": "优化模型 Hub", "非线性规划": "优化模型 Hub",
    "多目标规划": "优化模型 Hub", "动态规划": "动态规划 Hub",
    "遗传算法GA": "智能优化 Hub", "粒子群PSO": "智能优化 Hub", "模拟退火SA": "智能优化 Hub",
    "蚁群算法ACO": "智能优化 Hub",
    "Dijkstra最短路": "图论网络 Hub", "Floyd最短路": "图论网络 Hub", "最小生成树": "图论网络 Hub",
    "网络流": "图论网络 Hub", "排队论": "图论网络 Hub",
    "常微分方程": "微分方程动力学 Hub", "偏微分方程": "微分方程动力学 Hub",
    "差分方程": "微分方程动力学 Hub",
    "Monte Carlo": "蒙特卡洛 Hub", "元胞自动机": "蒙特卡洛 Hub",
    "马尔可夫模型": "马尔可夫决策过程 Hub", "博弈论": "博弈论 Hub",
    "数据预处理": "数据处理 Hub", "KMeans聚类": "数据处理 Hub", "聚类分析": "数据处理 Hub",
    "插值与拟合": "数据处理 Hub", "支持向量机SVM": "数据处理 Hub", "RBF神经网络": "数据处理 Hub",
    "神经网络": "数据处理 Hub", "绘图可视化": "可视化 Hub", "数字图像处理": "可视化 Hub",
}

TOPIC_HUB = {
    "评价与决策": "评价模型 Hub", "预测与时间序列": "预测模型 Hub", "优化与规划": "优化模型 Hub",
    "图论与排队": "图论网络 Hub", "微分与差分方程": "微分方程动力学 Hub",
    "统计与数据处理": "数据处理 Hub", "机器学习与神经网络": "数据处理 Hub",
    "仿真与随机模型": "蒙特卡洛 Hub", "博弈论": "博弈论 Hub",
    "可视化与图像": "可视化 Hub", "竞赛与论文写作": "论文写作 Hub",
    "数学基础": "数学建模 Hub", "待人工分类": "数学建模 Hub",
}

# Verified against the local “数学建模算法与应用课件（第二版）” chapter files.
CHAPTER_LABEL = {
    "01": "线性规划", "02": "整数规划", "03": "非线性规划", "04": "图与网络综合例程",
    "05": "插值与拟合", "06": "微分方程建模", "07": "数理统计", "08": "时间序列方法",
    "09": "支持向量机SVM", "10": "多元分析", "11": "偏最小二乘回归",
    "12": "现代优化算法", "13": "数字图像处理", "14": "综合评价与决策",
    "15": "预测方法", "16": "目标规划",
}

MODEL_HUB.update(
    {
        "图与网络综合例程": "图论网络 Hub", "微分方程建模": "微分方程动力学 Hub",
        "数理统计": "数据处理 Hub", "时间序列方法": "预测模型 Hub", "多元分析": "数据处理 Hub",
        "偏最小二乘回归": "预测模型 Hub", "现代优化算法": "智能优化 Hub",
        "综合评价与决策": "评价模型 Hub", "预测方法": "预测模型 Hub", "目标规划": "优化模型 Hub",
    }
)

# Each card is: problem, mathematical core, standard workflow, invocation advice,
# and the most important review risk.  Aliases below reuse the same concept card.
GUIDES: dict[str, tuple[str, str, str, str, str]] = {
    "线性规划": ("在线性目标和线性约束下求资源配置最优解。", "把决策变量、目标函数和约束统一写成矩阵形式。", "定义变量 → 写目标 → 写不等式/等式约束 → 设边界 → 求解 → 检查可行性与影子价格。", "目标与约束均线性、变量连续时优先调用。", "先统一最大化/最小化符号；不可行通常来自约束方向或单位错误。"),
    "整数规划": ("处理选或不选、数量必须为整数的组合决策。", "在线性或非线性模型上增加整数/0-1约束。", "定义整数变量 → 建目标与约束 → 设置整数索引 → 分支定界求解 → 校验组合含义。", "排班、选址、指派、路径选择等离散问题。", "不要先求连续解再简单四舍五入；规模大时注意求解时间与最优间隙。"),
    "非线性规划": ("求目标或约束非线性的局部/全局最优解。", "利用梯度、约束处理和初值进行连续优化。", "写目标与非线性约束 → 给边界和初值 → 选择算法 → 多初值求解 → 检查KKT与敏感性。", "模型平滑且变量连续时调用局部求解器；多峰问题配合全局搜索。", "结果高度依赖初值、尺度与局部极值。"),
    "目标规划": ("在多个有优先级或期望值的目标间折中。", "引入正负偏差变量并最小化加权或分层偏差。", "设目标值 → 定义偏差 → 设优先级/权重 → 建硬约束 → 求解并解释偏差。", "多个目标无法直接合并且允许偏离目标值时使用。", "权重不是天然客观量，必须做尺度统一和敏感性分析。"),
    "动态规划": ("把多阶段决策拆为可复用的子问题。", "状态、动作、转移和价值函数满足最优子结构。", "定义阶段/状态 → 写转移 → 给边界 → Bellman递推 → 回溯策略。", "阶段清晰、状态可压缩且具有无后效性时使用。", "状态定义错误会造成维度爆炸或重复/遗漏决策。"),
    "博弈论": ("分析多个决策者相互影响下的策略与均衡。", "用策略集、支付函数和信息结构刻画互动。", "识别参与者 → 定义策略与支付 → 判断信息/时序 → 求均衡 → 做稳定性与机制解释。", "他人策略会改变本方收益时使用，而非普通单主体优化。", "必须说明合作/非合作、完全/不完全信息以及均衡是否唯一。"),
    "绘图可视化": ("把数据、模型结果和不确定性转成可解释图形。", "图形编码必须与变量类型和比较任务匹配。", "明确表达任务 → 选择图形 → 整理数据 → 统一尺度/配色 → 标注单位 → 导出论文规格。", "在探索、诊断和论文表达三个阶段分别调用。", "避免双轴误导、无单位、过度平滑和仅追求美观。"),
    "数字图像处理": ("对像素矩阵进行增强、分割、特征提取或压缩。", "通过空间域/频域变换和形态学操作提取结构。", "读入与归一化 → 去噪/增强 → 分割 → 特征 → 评价 → 可视化。", "输入本身是图像或空间栅格时使用。", "参数依赖分辨率；必须保存原图并用客观指标评价。"),
    "Dijkstra最短路": ("求非负权图的单源最短路径。", "每次永久标记当前距离最小的未访问节点并松弛邻边。", "建邻接表/矩阵 → 初始化距离 → 优先队列迭代 → 记录前驱 → 回溯路径。", "边权非负且需要单源路径时优先。", "存在负权边时不能使用；注意不可达节点和有向性。"),
    "Floyd最短路": ("求任意两点之间的最短距离和路径。", "以中间节点为阶段进行三重动态规划。", "初始化距离/前驱矩阵 → 枚举中间点 → 更新距离 → 检查负环 → 重建路径。", "节点数中小且需要全源最短路时使用。", "时间复杂度O(n³)，无穷大初始化和路径矩阵最容易出错。"),
    "最小生成树": ("以最小总权连接无向图全部节点。", "Prim扩展已选节点集合，Kruskal按边权合并连通分量。", "检查连通性 → 选Prim/Kruskal → 维护候选边/并查集 → 输出树边 → 验证n-1条边。", "网络铺设、聚类骨架和最低连接成本。", "它最小化总连接成本，不保证任意两点路径最短。"),
    "网络流": ("在容量限制网络中求最大流、最小费用流或匹配。", "流守恒、容量约束和增广路径构成核心。", "建有向容量图 → 设源汇 → 增广/分层 → 更新残量网络 → 读最小割。", "运输、指派、匹配和资源流转问题。", "方向、反向边、容量单位和源汇定义必须核对。"),
    "排队论": ("估计随机到达与随机服务系统的等待和拥堵。", "用到达率、服务率、服务台数及稳态分布刻画队列。", "检验分布假设 → 计算利用率 → 选M/M/1等模型 → 求队长/等待 → 仿真验证。", "服务系统存在随机等待且关注容量配置时使用。", "必须先检查稳定条件，现实到达/服务分布可能不满足指数假设。"),
    "常微分方程": ("描述状态随时间连续变化的动力系统。", "由状态导数、初值和参数决定轨迹。", "定义状态 → 写导数函数 → 设初值/时间 → 数值积分 → 相图/参数分析。", "机制可写成变化率且空间效应可忽略时使用。", "刚性、步长、参数单位和初值敏感性决定可信度。"),
    "偏微分方程": ("描述状态同时随时间和空间变化。", "扩散、对流、反应项与边界/初始条件共同决定解。", "写PDE → 定义区域与边界 → 离散空间/时间 → 求解 → 网格收敛检验。", "存在扩散、传热、波动或空间传播时使用。", "没有边界条件和网格收敛检验的结果不可直接使用。"),
    "差分方程": ("描述离散时间状态的递推演化。", "下一期状态由当前或若干历史状态决定。", "定义状态与步长 → 写递推式 → 给初值 → 迭代 → 求平衡点与稳定性。", "过程天然按期更新或连续模型需离散化时使用。", "注意时间步长、索引偏移和数值发散。"),
    "数据预处理": ("把原始数据转换成可建模、可比较的输入。", "缺失、异常、尺度、编码和泄漏控制是主线。", "数据审计 → 缺失/异常处理 → 编码 → 标准化 → 划分训练验证 → 保存变换器。", "任何正式建模前都应执行，但方法必须服务于后续模型。", "先划分后拟合预处理器，避免把测试信息泄漏给训练过程。"),
    "插值与拟合": ("从离散观测构造连续关系或参数化趋势。", "插值要求过点，拟合强调总体误差最小。", "看散点/误差 → 选函数族 → 估参 → 残差诊断 → 交叉验证 → 限制外推。", "补齐区间内函数值或建立经验关系时使用。", "高阶多项式、过拟合和区间外预测风险高。"),
    "KMeans聚类": ("把样本划分为K个紧凑簇。", "交替分配最近中心并更新均值，最小化簇内平方和。", "标准化 → 选K → 多次初始化 → 迭代 → 轮廓系数/稳定性评价。", "数值特征、近似球形且需要硬聚类时使用。", "对尺度、初值和离群点敏感，K需要证据。"),
    "聚类分析": ("在无标签数据中发现相似群组。", "距离/相似度、连接准则和簇结构假设决定结果。", "选特征 → 标准化 → 选距离和算法 → 定参 → 稳定性/解释性检验。", "探索分群、画像或异常结构时使用。", "聚类不是天然真实类别，必须检查稳定性和业务含义。"),
    "多元分析": ("联合分析多个相关变量的结构、差异和关系。", "协方差/相关矩阵及降维、判别、聚类等方法。", "尺度处理 → 相关性诊断 → 选PCA/因子/判别等 → 估计 → 解释 → 验证。", "多个指标相关且单变量分析不足时使用。", "样本量、共线性、异常值和标准化选择影响很大。"),
    "支持向量机SVM": ("用最大间隔超平面完成分类或回归。", "核函数把非线性关系映射到高维，C与核参数控制偏差方差。", "缩放特征 → 选核 → 交叉验证C/γ → 训练 → 评价 → 检查支持向量。", "中小样本、高维或边界复杂时适用。", "必须标准化；概率解释和大样本训练成本需注意。"),
    "RBF神经网络": ("用径向基函数组合逼近非线性映射。", "隐藏层以中心距离响应，输出层线性组合。", "标准化 → 选中心/宽度 → 求权重 → 验证 → 调整复杂度。", "平滑函数逼近和中小样本回归。", "中心数与宽度过大会过拟合，过小则欠拟合。"),
    "遗传算法GA": ("通过种群进化搜索复杂空间的近似最优解。", "编码、适应度、选择、交叉、变异共同维持探索与利用。", "编码变量 → 适应度/罚函数 → 初始化 → 选择交叉变异 → 精英保留 → 收敛与多次复验。", "离散、非光滑、多峰且精确算法困难时使用。", "参数多、随机性强；必须固定种子、多次运行并与基线比较。"),
    "粒子群PSO": ("用群体位置和速度协同搜索连续空间。", "个体最优与群体最优共同更新速度。", "初始化粒子 → 评估 → 更新个体/全局最优 → 更新速度位置 → 边界处理 → 收敛。", "连续黑箱优化、实现需要简洁时使用。", "易早熟；惯性权重、速度上限和边界处理要记录。"),
    "模拟退火SA": ("通过按温度概率接受劣解跳出局部最优。", "Metropolis接受准则与降温计划控制搜索。", "给初解/温度 → 生成邻域 → 计算能量差 → 概率接受 → 降温 → 多次复验。", "组合优化或多峰问题且可设计邻域时使用。", "降温过快会早熟，过慢成本高；结果需多次统计。"),
    "蚁群算法ACO": ("用信息素和启发函数构造组合路径。", "多只蚂蚁按概率选边，并蒸发/强化信息素。", "初始化信息素 → 构造解 → 评价 → 局部/全局更新 → 迭代 → 输出最好路径。", "路径、排序和图上的组合优化。", "参数敏感且易停滞；必须处理不可行路径。"),
    "Monte Carlo": ("用随机抽样估计难以解析计算的概率、积分或风险。", "大数定律保证样本统计量趋近目标量。", "定义随机输入 → 设计采样 → 重复仿真 → 汇总均值/分位数/置信区间 → 收敛检查。", "解析解困难但单次仿真可计算时使用。", "固定随机种子、报告样本量和置信区间，避免只给一次结果。"),
    "元胞自动机": ("用局部规则模拟离散空间中的整体演化。", "网格状态按邻域规则同步或异步更新。", "定义网格/状态 → 设邻域 → 写转移规则 → 迭代 → 统计宏观模式 → 参数实验。", "传播、交通、生态和空间涌现问题。", "边界条件、更新顺序和网格尺度会改变结果。"),
    "主成分分析PCA": ("把相关指标压缩为少量互不相关的综合成分。", "对协方差/相关矩阵做特征分解并按方差排序。", "标准化 → 求相关矩阵 → 特征分解 → 选成分 → 算得分 → 解释载荷。", "指标多且共线，希望降维或综合评价时使用。", "主成分最大化方差而非因果/预测能力；载荷解释需谨慎。"),
    "AHP层次分析": ("把复杂评价拆成层次并由成对比较得到权重。", "判断矩阵最大特征向量给权重，一致性比率检查逻辑。", "建层次 → 构造判断矩阵 → 算权重 → 一致性检验 → 层次总排序。", "指标难以直接量化且需要专家判断时使用。", "主观性强；CR不通过必须调整，不能只给权重。"),
    "TOPSIS": ("按方案距正理想解近、负理想解远进行排序。", "标准化加权矩阵上的欧氏距离和贴近度。", "同向化 → 标准化 → 加权 → 定正负理想解 → 算距离/贴近度 → 排序。", "多指标方案排序且指标方向明确时使用。", "标准化、权重和异常值会改变距离结构。"),
    "熵权法": ("按指标样本差异程度客观赋权。", "信息熵越小、差异越大，指标权重越高。", "同向化/平移 → 归一化 → 算比重与熵 → 算差异系数 → 归一化权重。", "希望权重反映数据离散度时使用，常与TOPSIS组合。", "差异大不等于重要；零值、负值和样本变化需处理。"),
    "灰色关联分析": ("比较各序列与参考序列的形状接近程度。", "由逐点差异构造关联系数并聚合关联度。", "定参考序列 → 无量纲化 → 求差序列 → 算关联系数 → 加权聚合 → 排序。", "小样本、指标关系不清且关注趋势相似性。", "分辨系数、标准化和参考序列选择影响结论。"),
    "模糊综合评价": ("把模糊、语言化评价映射为等级隶属度。", "因素集、评语集、权重与隶属矩阵进行模糊合成。", "定因素/评语 → 构造隶属矩阵 → 定权 → 合成 → 解模糊/等级判定。", "评价边界模糊且专家语言信息较多时使用。", "隶属函数与权重需有来源，最大隶属原则可能丢信息。"),
    "回归分析": ("估计因变量与解释变量的条件关系并用于解释或预测。", "通过损失最小化估计系数，并用残差和推断检验模型。", "探索关系 → 编码/变换 → 拟合 → 残差诊断 → 共线性检查 → 验证/预测。", "目标连续或可用GLM描述且需要可解释关系。", "相关不等于因果；外推、异方差、共线性和数据泄漏常见。"),
    "ARIMA时间序列": ("利用差分后的自相关结构预测单变量序列。", "AR描述滞后值，MA描述滞后误差，I负责平稳化。", "画序列 → 平稳/差分 → ACF/PACF定阶 → 拟合 → 白噪声检验 → 滚动预测。", "单变量、等间隔、差分后近似平稳的序列。", "不能随机划分训练集；季节性、结构突变和残差相关必须检查。"),
    "指数平滑": ("用递减权重平滑历史并递推预测。", "水平、趋势和季节项按平滑系数更新。", "识别水平/趋势/季节 → 选SES/Holt/Winters → 估参数 → 滚动验证 → 预测区间。", "短中期预测且近期信息更重要时使用。", "结构突变和长周期外推能力有限。"),
    "灰色预测GM": ("用少量数据的累加生成序列建立指数趋势预测。", "AGO削弱波动，再拟合一阶白化微分方程。", "级比检验 → AGO → 估参数 → 时间响应 → 还原 → 残差/后验差检验。", "样本少、趋势较单调且信息不完整。", "波动大、结构突变或长期预测时可靠性下降。"),
}

GUIDES.update(
    {
        "现代优化算法": ("用随机化、群体化或启发式搜索求复杂问题的近似最优解。", "在探索全局空间和利用当前优良解之间保持平衡。", "定义编码/邻域 → 设计评价和约束处理 → 初始化 → 迭代搜索 → 多次复验 → 与精确/简单基线比较。", "非凸、离散、不可导或精确算法成本过高时使用。", "算法名称不能替代验证；必须报告参数、随机种子、运行次数和最优性差距。"),
        "图与网络综合例程": ("把实体与关系抽象为节点、边和权重后完成路径、连通或流量分析。", "邻接结构、方向和权重定义决定可调用的图算法。", "定义节点/边 → 建图 → 判断问题类型 → 选择最短路/生成树/网络流 → 重建结果 → 图示验证。", "问题的核心是关系结构而非单纯表格计算时使用。", "先核对有向/无向、权重意义和不可达状态，再选择算法。"),
        "图论与排队": ("汇总图网络与服务系统中的路径、连通、流量和等待问题。", "根据关系网络或随机服务机制选择不同子模型。", "识别问题结构 → 建图或队列参数 → 选具体算法 → 求解 → 用路径/守恒/稳定条件验算。", "作为入口使用，不能把不同图算法或排队模型混为一类。", "必须下钻到具体算法卡确认假设与复杂度。"),
        "微分方程建模": ("用变化率方程表达系统内部机制与动态反馈。", "状态变量、守恒关系、速率项和初边值条件共同定义模型。", "选状态 → 推导速率 → 定初边值 → 数值求解 → 参数估计 → 稳定性/敏感性分析。", "需要解释演化机制而不只是预测数值时使用。", "方程可解不等于机制正确，参数可辨识性和单位一致性必须检查。"),
        "微分与差分方程": ("覆盖连续时间微分模型和离散时间递推模型。", "根据时间尺度选择导数或差分表达状态变化。", "确定时间粒度 → 写状态方程 → 给初值 → 求解/迭代 → 平衡点与稳定性分析。", "过程具有明确动态反馈时进入，再选择ODE、PDE或差分模型。", "混淆连续与离散时间会造成参数含义和稳定条件错误。"),
        "统计与数据处理": ("对数据质量、分布、关系和不确定性进行整理与推断。", "描述统计、变换、抽样推断和模型诊断构成完整链路。", "审计数据 → 预处理 → 描述探索 → 选择统计模型 → 检验假设 → 报告效应与不确定性。", "任何以观测数据支撑结论的任务都应从这里进入。", "不要只报告p值或单一精度；定义、样本偏差和效应大小同样重要。"),
        "综合评价与决策": ("把多个指标转换成可比较的综合得分或排序。", "指标同向化、无量纲化、赋权和聚合是共同骨架。", "定义对象/指标 → 处理方向与尺度 → 选权重 → 选聚合模型 → 排序 → 稳健性检验。", "需要多指标排序、分级或方案优选时使用。", "权重和标准化方案会改变结论，至少进行一种替代方案比较。"),
        "评价与决策": ("作为AHP、TOPSIS、熵权、模糊评价和灰色关联的总入口。", "不同方法分别解决主观权重、距离排序、客观赋权、模糊等级和趋势关联。", "明确评价目标 → 判断信息类型 → 选择具体方法 → 计算 → 排序/分级 → 稳健性分析。", "先选具体评价算法，不直接把多个方法机械叠加。", "方法堆叠不等于可靠，指标体系与权重依据最重要。"),
        "预测方法": ("根据历史和解释变量估计未来或未知结果。", "趋势、相关结构、机制和不确定性共同决定模型选择。", "定义预测目标/跨度 → 时间切分 → 建基线 → 选模型 → 滚动验证 → 预测区间。", "需要外推到未来或未观测样本时使用。", "必须防止未来信息泄漏，并与朴素基线比较。"),
        "预测与时间序列": ("汇总回归、平滑、ARIMA和灰色预测等方法。", "横截面关系与时间依赖需要不同验证方式。", "判断数据是否有时间顺序 → 选回归或序列模型 → 按时间验证 → 诊断残差 → 输出区间。", "作为预测模型选择入口。", "随机划分时间序列、忽略结构突变和只给点预测是常见错误。"),
        "时间序列方法": ("分析按时间排列数据的趋势、季节和自相关。", "当前值与历史状态/误差相关，验证必须保持时间顺序。", "可视化 → 分解/平稳性 → 定模型 → 拟合 → 残差白噪声 → 滚动预测。", "等间隔观测且顺序信息不可打乱时使用。", "训练测试切分、缺失时间点和季节周期必须明确。"),
        "数学基础": ("提供建模代码依赖的代数、数值计算、概率与函数工具。", "把公式、矩阵和数值算法转成可验证计算。", "确认数学定义 → 选择稳定算法 → 处理边界/精度 → 与解析或简单结果对照。", "作为其他模型的底层工具调用，而非独立结论。", "注意浮点误差、矩阵条件数、维度和定义域。"),
    }
)

GUIDE_ALIASES = {
    "多目标规划": "目标规划", "数理统计": "统计与数据处理", "偏最小二乘回归": "回归分析",
}


def signature_label(item: core.SourceVariant) -> str:
    """Infer an algorithm from executable evidence before using folder context."""
    text = item.code.lower()
    source_path = Path(item.canonical_path)
    full_path = item.canonical_path.lower()
    filename = source_path.name.lower()
    local_context = "/".join(source_path.parts[-3:]).lower()
    def contains(haystack: str, token: str) -> bool:
        if token.isascii() and re.fullmatch(r"[a-z0-9_]+", token):
            return bool(re.search(rf"(?<![a-z0-9_]){re.escape(token)}(?![a-z0-9_])", haystack))
        return token in haystack

    # An explicit metaheuristic name is stronger evidence than a generic
    # solver called inside it (for example GA code may use fmincon as a
    # hybrid local-search step).
    if (
        "genetic algorithm" in text
        or "遗传算法" in text
        or bool(re.search(r"(^|[_-])ga([_-]|$)", Path(filename).stem))
        or any(token in filename for token in ("selection", "crossover", "mutation", "ranking", "reins"))
        or all(token in text for token in ("selection", "crossover", "mutation"))
    ):
        return "遗传算法GA"
    if any(token in text for token in ("particleswarm", "particle swarm", "pbest", "gbest")) or bool(re.search(r"(^|[_-])pso([_-]|$)", Path(filename).stem)):
        return "粒子群PSO"
    if "simulated anneal" in text or "模拟退火" in text or ("metropolis" in text and "temperature" in text):
        return "模拟退火SA"
    if "ant colony" in text or "蚁群" in text or bool(re.search(r"(^|[_-])aco([_-]|$)", Path(filename).stem)) or ("pheromone" in text and "evaporation" in text):
        return "蚁群算法ACO"
    path_hints = {
        "遗传算法GA": max(full_path.rfind("遗传算法"), full_path.rfind("genetic algorithm")),
        "粒子群PSO": max(full_path.rfind("粒子群"), full_path.rfind("particle swarm")),
        "模拟退火SA": max(full_path.rfind("模拟退火"), full_path.rfind("simulated anneal")),
        "蚁群算法ACO": max(full_path.rfind("蚁群"), full_path.rfind("ant colony")),
        "Monte Carlo": max(full_path.rfind("蒙特卡"), full_path.rfind("monte carlo")),
    }
    path_label, path_position = max(path_hints.items(), key=lambda pair: pair[1])
    if path_position >= 0:
        return path_label

    rules: tuple[tuple[str, tuple[str, ...]], ...] = (
        ("AHP层次分析", ("ci=(", "cr=ci/", "ri=[", "一致性检验")),
        ("TOPSIS", ("topsis", "正理想", "负理想", "closeness")),
        ("灰色预测GM", ("gm(1,1)", "gm11", "累加生成")),
        ("Dijkstra最短路", ("dijkstra", "graphshortestpath")),
        ("Floyd最短路", ("floyd",)),
        ("最小生成树", ("minspantree", "kruskal", "prim(")),
        ("网络流", ("maxflow", "maximum_flow", "mincostmaxflow")),
        ("整数规划", ("intlinprog", "bintprog", "@bin(", "@gin(")),
        ("线性规划", ("linprog", "scipy.optimize.linprog")),
        ("非线性规划", ("fmincon", "fminsearch", "quadprog", "scipy.optimize.minimize")),
        ("KMeans聚类", ("kmeans", "k-means")),
        ("聚类分析", ("proc cluster", "linkage(", "hierarchical clustering")),
        ("支持向量机SVM", ("svm", "svc(", "svr(")),
        ("主成分分析PCA", ("pca(", "proc princomp", "explained_variance", "principal component")),
        ("多元分析", ("proc factor", "factoran(", "proc discrim", "proc candisc")),
        ("ARIMA时间序列", ("arima", "sarima")),
        ("指数平滑", ("exponentialsmoothing", "simpleexp", "holt(")),
        ("回归分析", ("linearregression", "statsmodels.api", "proc reg", "regress(")),
        ("常微分方程", ("ode45", "ode23", "odeint", "solve_ivp")),
        ("偏微分方程", ("pdepe", "laplacian", "有限差分")),
        ("数字图像处理", ("imread(", "imshow(", "imfilter(", "dct2(")),
    )
    for label, tokens in rules:
        if any(contains(text, token) or contains(filename, token) for token in tokens):
            return label
    local_models = core.detect_models(local_context, item.code)
    if local_models:
        return ""
    random_tokens = ("unifrnd", "normrnd", "randint", "rand(", "np.random", "random.")
    repeated_sampling = bool(re.search(r"10\s*\^\s*[4-9]|100000|for\s+\w+\s*=\s*1:", text))
    if "mengte" in filename or (any(token in text for token in random_tokens) and repeated_sampling):
        return "Monte Carlo"
    return ""


def inferred_label(item: core.SourceVariant) -> str:
    signature = signature_label(item)
    if signature:
        return signature
    source_path = Path(item.canonical_path)
    local_context = "/".join(source_path.parts[-3:])
    local_models = core.detect_models(local_context, item.code)
    if local_models:
        return local_models[0]
    if item.topic != "待人工分类":
        return item.topic
    chapter = re.search(r"/程序及数据/(\d{2})第\d+章(?:/|$)", item.canonical_path)
    if chapter and chapter.group(1) in CHAPTER_LABEL:
        return CHAPTER_LABEL[chapter.group(1)]
    return f"未标注例程·{purpose(item)}"


def primary_label(items: list[core.SourceVariant]) -> str:
    return Counter(inferred_label(item) for item in items).most_common(1)[0][0]


def destination(items: list[core.SourceVariant]) -> str:
    label = primary_label(items)
    if label.startswith("未标注例程·"):
        suffix = label.split("·", 1)[1]
        return {
            "结果绘图与展示": "可视化 Hub", "数据读取与预处理": "数据处理 Hub",
            "模型求解": "优化模型 Hub", "预测与推断": "预测模型 Hub",
        }.get(suffix, "数学建模 Hub")
    return MODEL_HUB.get(label, TOPIC_HUB.get(label, "数学建模 Hub"))


def purpose(item: core.SourceVariant) -> str:
    haystack = f"{item.canonical_path}\n{item.code[:50000]}".lower()
    if any(word in haystack for word in ("plot(", "figure(", "matplotlib", "绘图", "可视化")):
        return "结果绘图与展示"
    if any(word in haystack for word in ("read_csv", "read_excel", "load(", "load ", "数据清洗", "standard")):
        return "数据读取与预处理"
    if any(word in haystack for word in ("linprog", "fmincon", "solve", "optimize", "求解")):
        return "模型求解"
    if any(word in haystack for word in ("predict", "forecast", "预测")):
        return "预测与推断"
    return "核心算法与辅助函数"


def guide_for(label: str) -> tuple[str, str, str, str, str]:
    key = GUIDE_ALIASES.get(label, label)
    if key in GUIDES:
        return GUIDES[key]
    if label.startswith("未标注例程·"):
        use = label.split("·", 1)[1]
        return (
            f"这组代码的文件名缺乏算法语义，静态分析表明主要承担“{use}”。",
            "先从函数、调用链和关键库识别计算角色，不在证据不足时强行归入具体模型。",
            "确认入口 → 阅读参数和关键操作 → 分离硬编码 → 包装成函数 → 用最小样例验证。",
            "仅在核对源码正文和输出后复用；优先把它作为辅助代码而非完整模型。",
            "当前分类属于保守推断，运行验证后应补充准确算法名称。",
        )
    return (
        f"该组实现围绕“{label}”完成建模计算或辅助处理。",
        "通过输入、核心变换/求解器和输出三部分理解代码，而不是依赖原文件夹名称。",
        "确认问题类型 → 找入口与参数 → 理清核心计算 → 运行最小样例 → 检验输出。",
        "先阅读下方代码理解卡，再选择函数型实现；脚本型实现应先重构参数。",
        "自动总结只能用于导航，最终调用前仍需做数据、环境和结果验证。",
    )


OPERATION_RULES: tuple[tuple[tuple[str, ...], str], ...] = (
    (("linprog", "scipy.optimize.linprog"), "组装目标和线性约束并调用线性规划求解器"),
    (("intlinprog", "milp", "@bin", "@gin"), "声明整数/0-1变量并求解离散优化模型"),
    (("fmincon", "minimize(", "fminsearch", "quadprog"), "构造目标与边界/约束并执行连续优化"),
    (("@sum", "model:", "endsets"), "在LINGO中声明集合、目标函数和约束后交给求解器"),
    (("eig(", "np.linalg.eig", "eigen"), "进行特征分解以获得权重、主成分或稳定性信息"),
    (("svd(", "np.linalg.svd"), "使用奇异值分解提取低维结构"),
    (("pca(", "pca(", "sklearn.decomposition"), "标准化后提取主成分与解释方差"),
    (("kmeans", "k-means"), "迭代更新簇分配和中心完成聚类"),
    (("svm", "svc(", "svr("), "训练支持向量分类/回归模型并生成预测"),
    (("polyfit", "curve_fit", "interp1", "spline", "griddata"), "执行插值或参数拟合并评价曲线"),
    (("arima", "sarima", "autoreg"), "识别并拟合时间序列滞后结构"),
    (("expsmooth", "exponential", "holt"), "递推更新水平、趋势或季节项完成预测"),
    (("ode45", "odeint", "solve_ivp", "ode23"), "定义状态导数并进行常微分方程数值积分"),
    (("pdepe", "del2", "laplacian"), "离散空间项并求解偏微分方程"),
    (("dijkstra", "graphshortestpath"), "通过松弛操作求单源最短路径"),
    (("floyd", "all_pairs_shortest"), "用中间节点递推更新全源最短路矩阵"),
    (("minspantree", "kruskal", "prim("), "选择低权边构造最小生成树"),
    (("maxflow", "maximum_flow", "mincostmaxflow"), "在残量网络上计算最大流或最小费用流"),
    (("rand(", "random.", "np.random", "unifrnd", "normrnd", "randint", "monte carlo"), "重复随机采样并汇总模拟结果"),
    (("ga(", "genetic", "selection", "crossover", "mutation"), "执行选择、交叉和变异的进化搜索"),
    (("particleswarm", "particle swarm", "pbest", "gbest"), "更新粒子速度与位置进行群体优化"),
    (("anneal", "temperature", "metropolis"), "按温度和接受概率进行模拟退火搜索"),
    (("pheromone", "ant colony", "蚁群"), "按信息素概率构造解并迭代强化优良路径"),
    (("regress", "ols(", "linearregression", "proc reg"), "估计回归系数并生成拟合/预测"),
    (("standardscaler", "normalize", "zscore", "standard_"), "执行归一化或标准化以统一变量尺度"),
    (("plot(", "figure(", "matplotlib", "surf(", "imshow("), "把计算结果转换为二维、三维或图像表达"),
)


def code_understanding(item: core.SourceVariant, label: str) -> dict[str, str]:
    haystack = f"{item.canonical_path}\n{item.code}".lower()
    operations = [description for keys, description in OPERATION_RULES if any(key in haystack for key in keys)]
    operations = list(dict.fromkeys(operations))[:4]
    if not operations:
        operations = {
            "LINGO": ["声明集合/参数、目标和约束并由LINGO求解"],
            "SAS": ["按DATA/PROC流程完成统计计算并输出过程结果"],
            "MATLAB": ["按脚本或函数顺序完成数值计算并返回工作区结果"],
            "Python": ["导入依赖后执行数值变换、模型计算和结果输出"],
            "C++": ["使用显式数据结构和循环实现核心算法"],
        }.get(item.language, ["执行该算法的核心数值步骤"])

    if item.symbols:
        role = "函数/类型实现，可优先封装复用"
        invocation = "优先调用 " + "、".join(f"`{name}`" for name in item.symbols[:8]) + "；先核对参数顺序和返回值。"
    elif item.language == "LINGO":
        role = "完整优化模型或模型片段"
        invocation = "在 LINGO 中载入模型；先把集合、参数和约束改成当前问题定义。"
    elif item.language == "SAS":
        role = "统计过程脚本"
        invocation = "按 DATA → PROC → RUN 顺序整体执行；把分析过程和变量名换成当前任务。"
    else:
        role = "脚本型示例，适合学习后重构"
        invocation = "不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。"

    outputs: list[str] = []
    if re.search(r"\breturn\b", haystack):
        outputs.append("函数返回值")
    if any(token in haystack for token in ("print(", "disp(", "proc print", "@write")):
        outputs.append("控制台/过程输出")
    if any(token in haystack for token in ("plot(", "figure(", "imshow(", "matplotlib", "surf(")):
        outputs.append("图形")
    if any(token in haystack for token in ("save(", "write", "dlmwrite", "to_csv", "export")):
        outputs.append("文件结果")
    if not outputs:
        outputs.append("工作区变量或求解器结果")

    risks: list[str] = []
    if item.data_paths or item.unresolved_data:
        risks.append("原实现含外部输入，复用时应改成显式函数参数")
    if item.call_paths:
        risks.append("存在同目录辅助函数调用，需要一起迁移")
    if re.search(r"[a-z]:[\\/]", haystack):
        risks.append("包含绝对路径，必须改为项目相对路径")
    if any(token in haystack for token in ("rand(", "random.", "np.random", "unifrnd", "normrnd", "randint")) and not any(token in haystack for token in ("seed(", "rng(")):
        risks.append("含随机过程但未发现固定随机种子")
    if any(token in haystack for token in ("graphshortestpath", "biograph(", "xlsread(")):
        risks.append("使用旧版接口，运行前检查当前软件兼容性")
    if not risks:
        risks.append("未发现明显静态风险，但仍需运行测试和结果校验")
    return {
        "position": f"{role}；当前用于{label}中的“{purpose(item)}”。",
        "flow": "；".join(operations) + "。",
        "invoke": invocation,
        "output": "、".join(outputs),
        "risk": "；".join(risks) + "。",
    }


def clean_heading(value: str) -> str:
    value = re.sub(r"[\r\n|#]", "-", value).strip(" .-")
    return value[:90] or "未命名实现"


def local_path(relative: str) -> str:
    """Render provenance without asking Windows to open an unknown extension."""
    return f"`00-Inbox/Downloaded/{relative.replace('`', 'ˋ')}`"


def group_heading(group: list[int], variants: list[core.SourceVariant]) -> str:
    items = [variants[index] for index in group]
    digest = hashlib.sha256("|".join(sorted(item.digest for item in items)).encode("utf-8")).hexdigest()[:8]
    language = ", ".join(sorted({item.language for item in items}))
    if len(items) > 1:
        return f"相似实现组 · {language} · {digest}"
    return f"{clean_heading(Path(items[0].canonical_path).stem)} · {language} · {digest}"


REPRESENTATIVE_SIGNALS: dict[str, tuple[str, ...]] = {
    "线性规划": ("linprog", "scipy.optimize.linprog"),
    "整数规划": ("intlinprog", "bintprog", "@bin(", "@gin(", "milp("),
    "非线性规划": ("fmincon", "fminsearch", "quadprog", "scipy.optimize.minimize"),
    "目标规划": ("deviation", "偏差变量", "priority", "goal programming"),
    "动态规划": ("bellman", "dynamic programming", "状态转移", "dp["),
    "Dijkstra最短路": ("dijkstra", "graphshortestpath"),
    "Floyd最短路": ("floyd",),
    "最小生成树": ("minspantree", "kruskal", "prim("),
    "网络流": ("maxflow", "maximum_flow", "mincostmaxflow"),
    "常微分方程": ("ode45", "ode23", "odeint", "solve_ivp"),
    "偏微分方程": ("pdepe", "laplacian", "有限差分"),
    "KMeans聚类": ("kmeans", "k-means"),
    "聚类分析": ("proc cluster", "linkage(", "dendrogram("),
    "支持向量机SVM": ("svc(", "svr(", "svmtrain", "fitcsvm"),
    "主成分分析PCA": ("pca(", "proc princomp", "explained_variance"),
    "多元分析": ("proc factor", "factoran(", "proc discrim", "proc candisc"),
    "ARIMA时间序列": ("proc arima", "arima(", "sarima", "forecast", "estimate"),
    "指数平滑": ("exponentialsmoothing", "simpleexp", "holt("),
    "回归分析": ("linearregression", "proc reg", "regress(", "ols("),
    "遗传算法GA": ("crossover", "mutation", "selection", "ga("),
    "粒子群PSO": ("particleswarm", "pbest", "gbest", "velocity"),
    "模拟退火SA": ("metropolis", "temperature", "anneal"),
    "蚁群算法ACO": ("pheromone", "ant colony", "蚁群"),
    "Monte Carlo": ("monte carlo", "mengte", "unifrnd", "np.random", "rand("),
    "AHP层次分析": ("cr=ci/", "ri=[", "一致性检验", "eig("),
    "TOPSIS": ("topsis", "closeness", "正理想", "负理想"),
    "熵权法": ("entropy", "熵权", "信息熵"),
    "灰色关联分析": ("灰色关联", "关联系数", "grey relation"),
    "模糊综合评价": ("隶属", "fuzzy", "评语集"),
    "灰色预测GM": ("gm(1,1)", "gm11", "累加生成"),
}


def representative_score(item: core.SourceVariant, label: str) -> float:
    """Prefer reusable core implementations over diagnostics and helper fragments."""
    code = item.code.lower()
    filename = Path(item.canonical_path).stem.lower()
    score = 0.0
    signals = REPRESENTATIVE_SIGNALS.get(label, ())
    hits = sum(signal.lower() in code or signal.lower() in filename for signal in signals)
    score += min(hits, 3) * 4.0
    if item.symbols:
        score += 3.0
    if 300 <= len(item.code) <= 20000:
        score += 2.0
    elif len(item.code) < 120:
        score -= 3.0
    if any(token in code for token in ("forecast", "predict", "optimize", "solve", "estimate")):
        score += 1.5
    if re.search(r"(^|[_-])(test|check|validate|validation|jian_?yan|diagnostic|residual|white_?noise)([_-]|$)", filename):
        score -= 5.0
    if re.search(r"(^|[_-])(fun|func|helper|util|utility|contents?|readme)([_-]|$)", filename):
        score -= 3.0
    if re.fullmatch(r"fun\d*|test\d*|check\d*|validate\d*|fitness\d*|objective\d*|constraint\d*|constr\d*", filename):
        score -= 4.0
    if re.search(r"[a-z]:[\\/]", code):
        score -= 2.0
    score -= min(len(item.call_paths), 4) * 0.5
    return score


def representative_index(group: list[int], variants: list[core.SourceVariant], label: str) -> int:
    return max(
        group,
        key=lambda index: (
            representative_score(variants[index], label),
            bool(variants[index].symbols),
            -len(variants[index].canonical_path),
        ),
    )


def render_study_guide(
    hub: str,
    model_groups: dict[str, list[list[int]]],
    variants: list[core.SourceVariant],
) -> str:
    lines = [
        STUDY_BEGIN,
        "## 复习与调用指南", "",
        "> [!summary] 阅读顺序",
        "> 先用“快速选择”确定算法，再读复习卡掌握思想和步骤，最后跳到实现区选择代码。源码默认折叠；数据明细不在复习页展开。", "",
        "### 快速选择", "",
        "| 算法或用途 | 主要解决什么 | 独立实现 | 语言 |",
        "|---|---|---:|---|",
    ]
    for label, label_groups in sorted(model_groups.items()):
        items = [variants[index] for group in label_groups for index in group]
        problem, _, _, _, _ = guide_for(label)
        languages = ", ".join(sorted({item.language for item in items}))
        lines.append(f"| [[#{label} · 复习|{label}]] | {problem} | {len(items)} | {languages} |")
    lines.extend(["", "### 逐算法复习卡", ""])
    for label, label_groups in sorted(model_groups.items()):
        items = [variants[index] for group in label_groups for index in group]
        problem, principle, workflow, invocation, pitfall = guide_for(label)
        source_count = sum(len(item.paths) for item in items)
        function_count = sum(bool(item.symbols) for item in items)
        languages = ", ".join(sorted({item.language for item in items}))
        ranked = sorted(
            label_groups,
            key=lambda group: (
                -representative_score(
                    variants[representative_index(group, variants, label)], label
                ),
                variants[representative_index(group, variants, label)].canonical_path,
            ),
        )[:3]
        recommendations = "、".join(
            f"[[#{group_heading(group, variants)}|{clean_heading(Path(variants[representative_index(group, variants, label)].canonical_path).stem)}]]"
            for group in ranked
        )
        lines.extend(
            [
                f"#### {label} · 复习", "",
                f"- **解决什么**：{problem}",
                f"- **核心思想**：{principle}",
                f"- **标准流程**：{workflow}",
                f"- **何时调用**：{invocation}",
                f"- **最易出错**：{pitfall}",
                f"- **库内覆盖**：{len(items)} 个独立实现、{source_count} 个原始来源；语言：{languages}；其中 {function_count} 个识别到函数/类型入口。",
                f"- **优先阅读**：{recommendations or '暂无可优先推荐的实现。'}（按核心算法证据、可复用入口与脚本完整度排序）",
                f"- **全部实现**：[[#{label} · 实现|跳转到源码实现区]]", "",
            ]
        )
    lines.extend(
        [
            "### 通用调用检查表", "",
            "1. 先确认当前问题是否满足复习卡中的适用条件。",
            "2. 优先选择标有函数/类型入口的实现，脚本型代码先重构参数。",
            "3. 用最小样例跑通，再替换为项目输入；不要一开始就接入完整题目。",
            "4. 检查目标方向、变量单位、边界条件、随机种子和软件版本。",
            "5. 保存运行环境、参数、结果与检验，验证通过后再进入项目正式代码。", "",
            STUDY_END, "",
        ]
    )
    return "\n".join(lines)


def render_group(group: list[int], variants: list[core.SourceVariant]) -> list[str]:
    items = [variants[index] for index in group]
    label = primary_label(items)
    heading = group_heading(group, variants)
    lines = [
        f"#### {heading}", "",
        f"- 归属算法：{label}",
        f"- 用途：{purpose(items[0])}",
        f"- 独立实现变体：{len(items)}",
        f"- 原始来源文件：{sum(len(item.paths) for item in items)}",
        f"- 复习入口：[[#{label} · 复习]]",
        "- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。",
        "",
    ]
    for number, item in enumerate(items, 1):
        if len(items) > 1:
            lines.extend([f"##### 变体 {number}：{clean_heading(Path(item.canonical_path).name)}", ""])
        understanding = code_understanding(item, label)
        lines.extend(
            [
                "##### 代码理解与调用", "",
                f"- **定位**：{understanding['position']}",
                f"- **执行主线**：{understanding['flow']}",
                f"- **调用方式**：{understanding['invoke']}",
                f"- **主要输出**：{understanding['output']}",
                f"- **调用风险**：{understanding['risk']}", "",
                f"- SHA-256：`{item.digest}`",
                f"- 语言：{item.language}",
                f"- 符号：{', '.join(f'`{value}`' for value in item.symbols) if item.symbols else '未自动识别'}",
                "- 原始路径：",
            ]
        )
        lines.extend(f"  - 源文件：{local_path(path)}" for path in item.paths)
        if item.call_paths:
            lines.append("- 同目录代码调用：")
            lines.extend(f"  - 被调用代码：{local_path(path)}" for path in item.call_paths)
        fence = "````" if "````" not in item.code else "`````"
        lines.extend(
            [
                "", "<details>", "<summary>展开原始代码</summary>", "",
                f"{fence}{core.LANGUAGE_FENCES.get(item.language, 'text')}", item.code.rstrip("\n"), fence,
                "", "</details>", "",
            ]
        )
    return lines


def replace_section(path: Path, generated: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else f"# {path.stem}\n"
    if BEGIN in text:
        text = text.split(BEGIN, 1)[0].rstrip()
    path.write_text(f"{text}\n\n{generated.rstrip()}\n", encoding="utf-8")


def replace_study_guide(path: Path, generated: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else f"# {path.stem}\n"
    text = re.sub(
        rf"\n*{re.escape(STUDY_BEGIN)}.*?{re.escape(STUDY_END)}\n*",
        "\n\n",
        text,
        flags=re.S,
    )
    heading = re.search(r"(?m)^# [^\n]+$", text)
    if not heading:
        raise RuntimeError(f"Hub has no H1 heading: {path}")
    insertion = heading.end()
    updated = text[:insertion].rstrip() + "\n\n" + generated.rstrip() + "\n\n" + text[insertion:].lstrip()
    path.write_text(updated, encoding="utf-8")


def replace_language_index(path: Path, generated: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else f"# {path.stem}\n"
    if LANG_BEGIN in text:
        text = text.split(LANG_BEGIN, 1)[0].rstrip()
    path.write_text(f"{text}\n\n{generated.rstrip()}\n", encoding="utf-8")


def write_language_indexes(variants: list[core.SourceVariant], groups: list[list[int]]) -> None:
    for language in ("Python", "MATLAB"):
        distribution: defaultdict[str, list[list[int]]] = defaultdict(list)
        for group in groups:
            items = [variants[index] for index in group]
            if items[0].language == language:
                distribution[destination(items)].append(group)
        total_variants = sum(len(group) for hub_groups in distribution.values() for group in hub_groups)
        total_sources = sum(
            len(variants[index].paths)
            for hub_groups in distribution.values()
            for group in hub_groups
            for index in group
        )
        if language == "Python":
            principles = [
                "优先调用函数/类实现，把输入、参数和返回值显式化。",
                "为每个项目建立独立环境并记录依赖版本；随机算法固定种子。",
                "数据处理、建模、评价和绘图分层，避免一个脚本承担全部工作。",
                "先运行最小样例，再接入真实任务；用断言检查形状、类型和取值范围。",
            ]
        else:
            principles = [
                "优先调用函数文件；旧脚本先把工作区变量和绝对路径改成参数。",
                "记录 MATLAB 版本与所需工具箱，避免依赖已废弃函数。",
                "矩阵维度、行列方向和索引从1开始是调用前重点检查项。",
                "先用小矩阵验证目标、约束与输出，再运行完整规模。",
            ]
        study = [
            STUDY_BEGIN,
            f"## {language} 复习与调用指南", "",
            "> 本 Hub 是语言入口，完整算法思想与源码位于对应领域 Hub；这里用于选择代码所在主题和规范调用方式。", "",
            "### 调用原则", "",
        ]
        study.extend(f"{index}. {value}" for index, value in enumerate(principles, 1))
        study.extend(["", "### 按主题进入", ""])
        for hub, hub_groups in sorted(distribution.items()):
            count = sum(len(group) for group in hub_groups)
            study.append(f"- [[{hub}]]：{count} 个独立实现")
        study.extend(["", STUDY_END, ""])
        replace_study_guide(HUB_DIR / f"{language} Hub.md", "\n".join(study))
        lines = [
            LANG_BEGIN,
            "## 本地源码主题分布", "",
            "> 本页只提供跨主题导航，不重复嵌入源码；完整代码保存在对应领域 Hub 的折叠标题下。", "",
            f"- 原始源码：{total_sources}",
            f"- 精确去重后的实现：{total_variants}", "",
            "| 领域 Hub | 独立实现 | 原始源码 |",
            "|---|---:|---:|",
        ]
        for hub, hub_groups in sorted(distribution.items()):
            variant_count = sum(len(group) for group in hub_groups)
            source_count = sum(len(variants[index].paths) for group in hub_groups for index in group)
            lines.append(f"| [[{hub}]] | {variant_count} | {source_count} |")
        lines.extend(["", LANG_END, ""])
        replace_language_index(HUB_DIR / f"{language} Hub.md", "\n".join(lines))


def main() -> int:
    code_rows = core.load_catalog(core.CODE_CATALOG)
    all_rows = core.load_catalog(core.ALL_CATALOG)
    variants = core.make_variants(code_rows)
    groups = core.cluster_similar(variants)
    core.resolve_data_and_calls(variants, all_rows)

    routed: defaultdict[str, list[list[int]]] = defaultdict(list)
    for group in groups:
        routed[destination([variants[index] for index in group])].append(group)

    written_sources = 0
    embedded_variants = 0
    for hub, hub_groups in sorted(routed.items()):
        model_groups: defaultdict[str, list[list[int]]] = defaultdict(list)
        for group in hub_groups:
            model_groups[primary_label([variants[index] for index in group])].append(group)
        source_count = sum(len(variants[index].paths) for group in hub_groups for index in group)
        variant_count = sum(len(group) for group in hub_groups)
        replace_study_guide(HUB_DIR / f"{hub}.md", render_study_guide(hub, model_groups, variants))
        lines = [
            BEGIN,
            "## 源码实现库（按需调用）", "",
            "> [!warning] 使用边界", 
            "> 以下源码保留全文与来源，但默认均未运行验证。数据依赖明细已从阅读页省略；调用时按代码理解卡完成参数化、最小样例和结果检验。来源显示为可复制路径，不直接调用 Windows 打开未知扩展名。", "",
            f"- 本 Hub 收录原始源码文件：{source_count}",
            f"- 精确去重后的独立实现：{variant_count}",
            f"- 合并后的实现组：{len(hub_groups)}", "",
            "### 实现索引", "",
            "| 算法或用途 | 独立实现 | 原始源码 |",
            "|---|---:|---:|",
        ]
        for label, label_groups in sorted(model_groups.items()):
            label_variants = sum(len(group) for group in label_groups)
            label_sources = sum(len(variants[index].paths) for group in label_groups for index in group)
            lines.append(f"| [[#{label} · 实现|{label}]] | {label_variants} | {label_sources} |")
        lines.append("")
        for label, label_groups in sorted(model_groups.items()):
            lines.extend([f"### {label} · 实现", ""])
            summary = core.MODEL_SUMMARIES.get(label)
            if summary:
                lines.extend([summary, ""])
            for group in sorted(label_groups, key=lambda value: variants[value[0]].canonical_path):
                lines.extend(render_group(group, variants))
        lines.extend([END, ""])
        replace_section(HUB_DIR / f"{hub}.md", "\n".join(lines))
        written_sources += source_count
        embedded_variants += variant_count

    write_language_indexes(variants, groups)

    # Validate coverage after writing.  Every catalog row must appear exactly in
    # at least one destination section; exact duplicates intentionally share code.
    hub_text = "\n".join((HUB_DIR / f"{hub}.md").read_text(encoding="utf-8") for hub in routed)
    missing = [row["relative_path"] for row in code_rows if f"源文件：`00-Inbox/Downloaded/{row['relative_path']}" not in hub_text]
    result = {
        "status": "PASS" if not missing and written_sources == len(code_rows) and embedded_variants == len(variants) else "FAIL",
        "topic_hubs_with_full_source": len(routed),
        "language_hubs_with_navigation": 2,
        "source_files_integrated": written_sources,
        "exact_unique_implementations": embedded_variants,
        "implementation_groups": len(groups),
        "similar_groups": sum(len(group) > 1 for group in groups),
        "new_graph_nodes": 0,
        "missing_source_paths": missing[:20],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
