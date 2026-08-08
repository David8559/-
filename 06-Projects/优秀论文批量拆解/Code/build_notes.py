from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, os, re
from collections import Counter
from pathlib import Path
import pymupdf

SRC=Path(r"D:\数学建模优秀论文分析\高教社杯全国大学生数学建模竞赛优秀论文")
QUESTION_SRC=Path(r"D:\数学建模优秀论文分析\高校社杯全国大学生数学建模竞赛题目")
VAULT=Path(r"C:\Users\17888\Documents\0.数学建模知识库\0.数学建模")
PROJECT=VAULT/"06-Projects"/"优秀论文批量拆解"
CACHE=PROJECT/"Data"/"Extracted"
OUT=VAULT/"04-Research"/"04-竞赛真题研究"/"03-优秀获奖论文拆解"/"批量标准化拆解"
CATS={"A":"连续型模型","B":"离散型模型","C":"数据分析与数据挖掘","D":"综合决策与评价","E":"社会环境政策与系统仿真","F":"博弈与对策"}
TITLE_OVERRIDES={
"2012国赛国家一等奖A题优秀论文5_20220719111558.pdf":"葡萄酒的评价",
"2010B：上海世博会影响力的定量评估.pdf":"上海世博会影响力的定量评估",
"[2011年国赛MATLAB创新奖B题]第三军医大学交巡警平台设置与调度模型.pdf":"交巡警平台设置与调度模型",
"[2011年国赛高教杯奖A题]南京信息工程大学城市表层土壤重金属污染.pdf":"城市表层土壤重金属污染分析",
"[2011年国赛MATLAB创新奖C题]九江学院-企业退休职工养老金模型.pdf":"企业退休职工养老金模型",
"2010A：基于数学建模的储油罐变形监测研究.pdf":"基于数学建模的储油罐变形监测研究",
"12a01.pdf":"基于数理分析的葡萄及葡萄酒评价体系"}

# 17 篇原自动抽取未识别出模型名的论文，均已回原 PDF 摘要/模型章节人工复核。
# 键为原 PDF SHA256，避免同题同名论文互相覆盖；pages 保留证据页码。
MODEL_CHAIN_OVERRIDES={
"2c46e77271decd4f72c3f5d503fbf5c2e0fc55a00c5114681c59fc8a54da6894":{"models":["太阳赤纬模型","太阳地方时角模型","月亮上中天时间模型","球面三角天体高度模型"],"pages":"1-2","method":"原生文本逐页核读"},
"53ab0841ed9ab2fda1fa8496ef2d905436cfa88f16f2314958904af0b2f6abb5":{"models":["一维鼓-球碰撞运动模型","鼓的三维平动-转动微分方程模型","误差扰动分析","协作策略优化"],"pages":"1-3","method":"扫描版原页 OCR 核读"},
"826bd8a874513236a7ac18c4ecb5dc71e2ec0b4a767243b9738462fc6e4b9d4e":{"models":["纯方位计算几何定位模型","两圆轨迹求交模型","带阈值启发式搜索算法","预设发射顺序随机调整模型"],"pages":"1-2","method":"扫描版原页 OCR 核读"},
"5bb37151e8c6023ed47b2dd1e553d6fb6d93ebeee0ad1d28feb12dc57a366904":{"models":["三维独立正态定位误差模型","分情形命中概率积分模型","定深引信数值优化模型","九枚深弹阵列优化模型"],"pages":"1-2","method":"扫描版原页 OCR 核读"},
"d8b8621931d04275d16973430af3bbe1acb87906c366a24660d41cba40fa0a4f":{"models":["椭圆柱罐体积分模型","变位罐体数值积分模型","最小二乘变位参数识别","罐容表误差检验"],"pages":"1-3","method":"原生文本逐页核读"},
"d0088efd6045034309a81330559bd64075e0329633bc178b71823d0ffd9ddcba":{"models":["截面体积分模型","纵横向变位几何换算模型","最小二乘参数识别","罐容表误差检验"],"pages":"1-3","method":"原生文本逐页核读"},
"d5025eca8cecd9b40f21cf6ed1d86ea77d7d3b54d880336ecc65173d607ecb44":{"models":["微元积分罐容模型","纵横倾角分步变换模型","最小二乘参数拟合","误差修正与可靠性检验"],"pages":"4-7","method":"扫描版原页 OCR 核读"},
"bce4697cf54df8fe9b31699e2201ccf24c4df9e891d034d6a0f19b8ddab89d7e":{"models":["平行截面面积积分模型","纵向变位分段模型","三段式实际罐体积分模型","双角度拟合识别"],"pages":"1-3","method":"扫描版原页 OCR 核读"},
"0af6c859fbb5aadf8a105bb97562b51daf79cd10b9fc31ec712d6aaa55beb891":{"models":["投影-截面-微元体积模型","纵向变位分情形模型","纵横变位四部分体积分模型","误差分布与相对误差检验"],"pages":"3","method":"扫描版原页 OCR 核读"},
"4bf99bf49099a71e6c970e938b2f6aa08785fce95df9b167ec8599d8168fd3ca":{"models":["二次多项式放电曲线模型","对数电流-系数线性回归模型","衰减状态比例外推模型","MRE误差检验"],"pages":"1-3","method":"原生文本逐页核读"},
"570c469618b346e065a4be647150561fe127959d409dcfd6de2f9172120a0b7f":{"models":["FMS会员购买力模型","RF生命周期状态模型","滑动窗口激活率模型","商品偏好-交叉连带率模型"],"pages":"1-3","method":"原生文本逐页核读"},
"573cb913ddc905f01182a20f3651c3042e4657d682a1c83e4f665845bfba5ab4":{"models":["分层规则排序模型","颜色分组与交替排列算法","驱动-动力间隔调整算法","配置切换次数优化"],"pages":"1-3","method":"原生文本逐页核读"},
"e57d13610e8d48de1a14a748bcb58a4892e832d55ab00bf7f919f003cbe0e2f5":{"models":["分段直线与圆弧拟合模型","倾斜角平均校准模型","特征点配准模型","多次测量轮廓融合模型"],"pages":"1-2","method":"扫描版原页 OCR 核读"},
"b78ec2af2e8de2ae99679cecdbdb86c73f17f20ec678c1477e5f7ba43568f926":{"models":["尾坯最小损失切割模型","分情形枚举调整算法","报废段在线重规划模型","用户目标分层优化模型"],"pages":"1-2","method":"扫描版原页 OCR 核读"},
"60b0116be30699279cb43a8e8854cd4ba97206efc77ba3696671366f402080ce":{"models":["对称信息传输模型","最小传输次数模型","副站可靠传输概率模型","期望站点数模型"],"pages":"1-2","method":"扫描版原页 OCR 核读"},
"d4009bf9120cdc89e796de2101592c46665b0af322a56bdb2f4e8ab52414801a":{"models":["双光束干涉-Cauchy色散模型","FFT初值与非线性联合拟合","Airy多光束干涉模型","残差-敏感性可靠性检验"],"pages":"1-2","method":"扫描版原页 OCR 核读"},
"bf211e0d2901698f856b2b75b528419b89fed8c408950a1596970259ebecae84":{"models":["差异显著性检验","逐步回归模型","聚类分析","判别分析"],"pages":"1","method":"原 PDF 页面渲染人工核读"}}

# 名称、匹配式、类别、已有知识节点
RAW=r"""偏微分方程|偏微分方程|(?<![A-Za-z])PDE(?![A-Za-z])|A|偏微分方程
常微分方程|常微分方程|微分方程组|(?<![A-Za-z])ODE(?![A-Za-z])|A|常微分方程
有限差分法|有限差分|A|模型-有限差分法
动力学模型|动力学模型|运动学模型|力学模型|A|微分方程动力学 Hub
热传导模型|热传导|传热模型|炉温|A|模型-热传导模型
扩散模型|扩散方程|污染物扩散|对流扩散|A|扩散动力学模型
SIR传染病模型|SIR|SEIR|传染病模型|A|SIR与SIS传染病模型
Logistic模型|Logistic模型|种群增长|A|种群增长Logistic模型
几何模型|几何模型|解析几何|空间几何|几何关系|A|模型-几何模型
线性规划|线性规划|B|线性规划
非线性规划|非线性规划|B|非线性规划
优化模型|优化模型|目标函数|最小费用|最小成本|费用最少|总费用最小|min\s*[A-Za-z]|B|模型-优化模型
整数规划|整数规划|0-1规划|混合整数|B|整数规划与0-1规划
多目标规划|多目标规划|多目标优化|Pareto|B|多目标规划
动态规划|动态规划|Bellman|B|动态规划
图论模型|图论|网络模型|复杂网络|B|图论网络 Hub
最短路径|最短路径|Dijkstra|Floyd|B|最短路径
网络流|网络流|最大流|最小费用流|B|网络流
路径规划|车辆路径|路径规划|旅行商|TSP|VRP|B|模型-车辆路径规划
排队论|排队论|排队模型|B|排队论模型
遗传算法|遗传算法|(?<![A-Za-z])GA(?![A-Za-z])|B|遗传算法GA
粒子群算法|粒子群|(?<![A-Za-z])PSO(?![A-Za-z])|B|粒子群PSO
模拟退火|模拟退火|(?<![A-Za-z])SA(?![A-Za-z])|B|模拟退火SA
蚁群算法|蚁群算法|(?<![A-Za-z])ACO(?![A-Za-z])|B|蚁群算法ACO
回归分析|回归分析|线性回归|多元回归|逐步回归|C|回归分析
Logistic回归|Logistic回归|逻辑回归|C|模型-Logistic回归
时间序列|时间序列|ARIMA|指数平滑|C|预测与时间序列
灰色预测|灰色预测|GM(1,1)|C|灰色预测GM
插值与拟合|插值|曲线拟合|样条|C|插值与拟合
主成分分析|主成分分析|PCA|C|主成分分析PCA
聚类分析|聚类分析|K-means|K均值|系统聚类|C|聚类分析
支持向量机|支持向量机|SVM|C|支持向量机SVM
随机森林|随机森林|Random Forest|C|模型-随机森林
决策树|决策树|CART|C|模型-决策树
神经网络|神经网络|BP网络|LSTM|RBF网络|C|神经网络
相关分析|相关分析|Pearson|Spearman|C|模型-相关分析
层次分析法|层次分析法|AHP|D|AHP层次分析法
熵权法|熵权法|熵值法|D|熵权法
TOPSIS|TOPSIS|优劣解距离|D|TOPSIS优劣解距离法
灰色关联分析|灰色关联|D|灰色关联分析
模糊综合评价|模糊综合评价|模糊评价|D|模糊综合评价
综合评价模型|综合评价|评价指标体系|综合评分|D|评价模型 Hub
蒙特卡洛模拟|蒙特卡洛|Monte Carlo|随机模拟|E|蒙特卡洛方法
系统动力学|系统动力学|因果回路|存量流量|E|模型-系统动力学
元胞自动机|元胞自动机|cellular autom|E|元胞自动机
马尔可夫模型|马尔可夫|Markov|MDP|E|马尔可夫决策过程MDP
博弈论|博弈论|博弈模型|支付矩阵|纳什均衡|Nash|F|博弈论基础
演化博弈|演化博弈|复制动态|F|博弈论 Hub"""
MODELS=[]
for row in RAW.splitlines():
    a=row.split("|"); MODELS.append((a[0],"|".join(a[1:-2]),a[-2],a[-1]))

REASON={
"A":"状态变量随时间或空间连续变化，题目给出了可用于守恒、传递或动力学关系的机理条件",
"B":"核心任务是从有限方案中选择、分配或排序，并同时满足目标函数与离散或资源约束",
"C":"结论主要由样本数据、特征关系和样本内外预测或分类性能支撑",
"D":"题目需要把多维指标转换为权重、综合得分与可解释排序",
"E":"对象包含长期反馈、情景假设与政策干预，需要比较多情景演化结果",
"F":"多个主体的收益相互依赖，结论取决于策略组合、信息结构与均衡"}
GUIDE={
"A":["模型建立后绘制物理结构、坐标系或受力示意图","求解后绘制状态量随时间或空间变化曲线","检验部分绘制参数扰动—输出响应曲线并制误差表"],
"B":["问题抽象后绘制网络、路径或调度结构图","算法说明处绘制状态转移或求解流程图","结果部分制方案对比表、资源分配表，并绘制收敛曲线或路线图"],
"C":["数据理解阶段绘制缺失率、分布、箱线图与相关热图","建模阶段制特征与模型选择表","结果阶段绘制预测—真实值、残差、混淆矩阵或特征重要性图并制指标对比表"],
"D":["指标构建处绘制指标层次结构图","权重计算后制权重与一致性检验表","结果阶段绘制排序图、雷达图，并制权重扰动稳健性表"],
"E":["问题机制处绘制因果回路、利益相关者或系统边界图","情景设定处制基准/乐观/悲观参数表","结果阶段绘制多情景演化曲线、空间分布图或政策权衡图"],
"F":["模型建立处制参与者—策略—收益表或支付矩阵","均衡分析处绘制最优反应或策略演化图","检验部分制不同参数与信息结构下的均衡对比表"]}

# 竞赛语境中的“创新”候选：只记录可从摘要或提取页定位的增量，不声明学术首创。
INNOVATION_RULES=[
    ("模型融合",r"耦合|融合|组合模型|联合模型|混合模型|将[^。；]{1,50}(?:模型|方法)[^。；]{0,30}(?:结合|融合)","把两类以上机理或方法组织为同一条建模链"),
    ("模型改进与推广",r"改进(?:了|的)?(?:模型|算法|方法)|在[^。；]{0,40}基础上[^。；]{0,30}改进|一般化|推广至|扩展到|统一模型|引入时变参数|重新构建","对基线模型的结构、参数或适用范围作了明确扩展"),
    ("分阶段与分类讨论",r"两阶段|多阶段|分阶段|分步骤|分步求解|分类讨论|分情况|不同情形|逐层|分层建模","按情形、阶段或层次拆分复杂任务并保持分问递进"),
    ("多目标与权衡",r"多目标|Pareto|帕累托|权衡|兼顾[^。；]{0,30}(?:成本|效益|风险|公平|环境|效率)","显式处理相互冲突的目标或评价维度"),
    ("数据处理与特征构造",r"数据清洗|异常值|缺失值|标准化|归一化|特征选择|特征筛选|指标筛选|主成分|降维|聚类分析|相关系数矩阵","对原始数据、指标或特征进行有目的的筛选和变换"),
    ("专用求解策略",r"遗传算法|粒子群|模拟退火|蚁群|动态规划|启发式|邻域搜索|迭代算法|分解算法|搜索算法|枚举法","根据问题结构选择或设计求解策略"),
    ("不确定性与情景分析",r"不确定性|随机模型|鲁棒|区间参数|蒙特卡洛|情景分析|多情景|风险分析|置信区间","把随机性、风险或情景差异纳入结论"),
    ("检验与稳健性",r"灵敏度分析|敏感性分析|稳健性分析|鲁棒性分析|误差分析|残差分析|交叉验证|模型检验|结果验证","使用误差、检验或扰动分析评估结果可信度"),
    ("政策与机制设计",r"激励机制|惩罚机制|政策组合|利益相关者|可持续|因果回路|反馈机制|均衡分析|纳什均衡","从主体互动、反馈或政策工具角度设计决策机制"),
    ("时空动态刻画",r"时空|空间分布|动态演化|时间序列|滚动预测|实时更新|在线优化|轨迹优化","刻画对象随时间、空间或事件更新的变化"),
    ("表达与可视化",r"流程图|热力图|雷达图|三维图|可视化|绘制[^。；]{0,25}(?:曲线|图像|图形)","用结构图、对比图或表格提高模型链与结果的可审查性")]
INNOVATION_PRIORITY={
    "A":["模型改进与推广","模型融合","时空动态刻画","检验与稳健性","专用求解策略","不确定性与情景分析","表达与可视化"],
    "B":["分阶段与分类讨论","专用求解策略","多目标与权衡","不确定性与情景分析","模型改进与推广","检验与稳健性","表达与可视化"],
    "C":["数据处理与特征构造","模型融合","时空动态刻画","检验与稳健性","不确定性与情景分析","模型改进与推广","表达与可视化"],
    "D":["数据处理与特征构造","多目标与权衡","不确定性与情景分析","检验与稳健性","模型融合","模型改进与推广","表达与可视化"],
    "E":["政策与机制设计","不确定性与情景分析","时空动态刻画","模型融合","多目标与权衡","检验与稳健性","表达与可视化"],
    "F":["政策与机制设计","模型改进与推广","不确定性与情景分析","时空动态刻画","检验与稳健性","模型融合","表达与可视化"]}

# “怎么创新”不是再列一个算法名，而是把基线、改动、数学落点和验证证据连成闭环。
# 下列内容是面向复用的 Agent 分析，不冒充原论文已经实施的步骤。
CATEGORY_BASELINE={
    "A":"先建立固定参数、单一主导机理的连续模型，并给定完整初值和边界条件",
    "B":"先建立静态、确定性、单目标的离散优化基线，并逐条审计约束可行性",
    "C":"先固定数据清洗和训练/验证/测试划分，建立一个简单且可解释的统计或机器学习基线",
    "D":"先用方向一致的标准化指标、固定权重和一种聚合方法得到基准排序",
    "E":"先明确系统边界和基准情景，用最少反馈关系得到无政策或现行政策下的演化结果",
    "F":"先建立完全信息、同质理性主体和固定收益下的基准博弈并求出均衡"}
CATEGORY_VALIDATION={
    "A":"同时检查量纲、守恒或物理边界、步长/网格收敛和参数敏感性",
    "B":"同时检查约束满足、解质量、上下界或最优间隙、计算时间和规模扩展性",
    "C":"同时固定数据划分、防止数据泄漏，并报告样本外性能、稳定性和错误分群",
    "D":"同时检查指标冗余、权重依据、排序一致性、名次翻转阈值和外部效度",
    "E":"同时检查参数来源、历史回测、多情景压力、利益相关者分配影响和政策失效边界",
    "F":"同时检查收益函数依据、均衡存在性/唯一性/稳定性、参数阈值和替代收益设定"}
INNOVATION_PLAYBOOK={
    "模型融合":{
        "gap":"单一模型只能解释一个局部机制，子问题之间的变量传递或相互反馈被割裂",
        "action":"先拆出各子模型的输入、输出和时间/空间尺度，再用共享变量、耦合项或顺序传递把它们接成闭环",
        "math":"在方程、目标或约束中增加耦合项与接口变量，统一量纲、索引和参数来源",
        "validation":"在相同输入下比较各子模型单独运行与融合模型的误差、解释增益和计算代价",
        "figure":"模型耦合流程图、基线/融合结果对比图、耦合参数敏感性图",
        "table":"子模型输入—输出—接口变量表、基线与融合模型指标表",
        "risk":"只把多个模型首尾罗列、没有接口变量或没有对照实验，不能算模型融合创新"},
    "模型改进与推广":{
        "gap":"基线依赖过强假设、固定参数或狭窄边界，无法覆盖题目中的非线性、异质性或新情形",
        "action":"先定位限制结论的那条假设，再把常数改为可解释函数、增加状态/决策变量，或放宽原约束与适用边界",
        "math":"明确写出改进前后方程或约束的差分，并给新增参数的估计方式和取值范围",
        "validation":"用同一数据和评价指标比较原模型与改进模型，并做新增部件消融、参数扰动和边界情形检验",
        "figure":"改进前后结构图、结果误差对比图、新参数响应曲线",
        "table":"原假设—改进假设—数学变化表、原模型与改进模型对照表",
        "risk":"只把常数写成函数或换一个模型名称，却没有现实理由、重新标定和增量验证，属于形式创新"},
    "分阶段与分类讨论":{
        "gap":"一步式模型混合了不同状态、群体或事件阶段，导致规则冲突、参数失真或结论不可执行",
        "action":"按可观测触发条件划分阶段或类别，为每段定义状态、规则和输出，并用转移条件连接相邻阶段",
        "math":"增加阶段/类别索引、分段函数、状态转移方程或阶段间衔接约束",
        "validation":"比较整体模型与分阶段模型的拟合或方案质量，并检查转移点附近连续性、可行性和稳定性",
        "figure":"阶段流程图、状态转移图、分段结果曲线或分群差异图",
        "table":"阶段定义—触发条件—变量—输出表、整体与分阶段结果表",
        "risk":"按题目小问机械分段、各阶段没有不同机制或衔接条件，不构成有效创新"},
    "多目标与权衡":{
        "gap":"单一目标掩盖成本、效率、公平、风险或环境代价之间的冲突",
        "action":"分别定义冲突目标，统一方向与尺度，再选择加权、分层、约束化或 Pareto 方法展示权衡",
        "math":"写出目标向量、归一化方式、权重/优先级或 ε 约束，并保留可行域不变",
        "validation":"与单目标基线比较各目标损失和综合收益，改变权重或阈值检查方案是否稳定",
        "figure":"Pareto 前沿、权重—目标响应图、方案雷达图",
        "table":"目标定义与单位表、代表性 Pareto 方案对比表、权重敏感性表",
        "risk":"把多个指标简单相加、权重无依据且不展示权衡曲线，只是目标堆叠"},
    "数据处理与特征构造":{
        "gap":"原始字段不能直接表达题目机制，缺失、异常、尺度差异或样本偏差会掩盖真实关系",
        "action":"先审计数据质量，再依据机理构造交互、滞后、周期、空间或聚合特征，并仅在训练数据上拟合预处理器",
        "math":"给出清洗阈值、特征定义、变换公式、时间窗口和数据划分规则",
        "validation":"在统一数据划分下进行原始特征基线、逐类特征消融和样本外验证，报告提升与方差",
        "figure":"缺失/异常分布图、特征相关或重要性图、消融结果图",
        "table":"字段口径与清洗规则表、特征定义表、消融与模型指标表",
        "risk":"在全量数据上预处理、只凭相关性造特征或只报告最高精度，会造成泄漏和伪提升"},
    "专用求解策略":{
        "gap":"通用求解器或直接枚举在规模、离散结构、非凸性或实时要求下难以得到可行且高质量的解",
        "action":"利用题目的图结构、可分解性、对称性或局部变动设计编码、邻域、剪枝、分解或混合精确—启发式流程",
        "math":"明确解的表示、可行性修复、转移/邻域算子、终止条件和复杂度来源",
        "validation":"在相同算例、停止条件和硬件口径下比较基线算法的目标值、可行率、时间、最优间隙和规模表现",
        "figure":"算法流程图、收敛曲线、规模—时间曲线、代表性方案图",
        "table":"算法设置表、同算例性能对比表、约束满足审计表",
        "risk":"只把遗传算法换成粒子群或增加迭代次数，没有结构适配和公平基线，不能证明算法创新"},
    "不确定性与情景分析":{
        "gap":"点估计默认未来与观测完全一致，无法反映需求、参数、测量或政策环境的波动风险",
        "action":"识别最影响结论的不确定量，用分布、区间或有来源的情景表示，并将风险显式传入模型",
        "math":"把点参数改写为随机变量/区间参数，采用期望、最坏情形、CVaR、机会约束或情景约束",
        "validation":"校准分布或情景范围，比较确定性与稳健/随机方案的平均表现、尾部风险和保守代价",
        "figure":"情景演化带、输出分布图、风险—收益前沿、压力测试曲线",
        "table":"不确定量来源与范围表、情景参数表、平均/最坏结果对比表",
        "risk":"随意调几个参数并称为情景分析，或只报告均值而忽略尾部风险，不足以支撑创新"},
    "检验与稳健性":{
        "gap":"单次求解只能说明模型能运行，不能说明结论正确、稳定或可推广",
        "action":"围绕核心结论选择残差、守恒、交叉验证、参数扰动、极端情形或外部数据，建立独立验证链",
        "math":"定义误差指标、扰动范围、重复抽样方案、置信区间或稳健性判据",
        "validation":"报告基线结果在多种检验下是否保持，并定位结论翻转点、失败样本和误差来源",
        "figure":"残差图、敏感性曲线、不确定性带、预测—真实值图",
        "table":"误差分解表、扰动前后结果表、外部验证或失败情形表",
        "risk":"只写“模型稳定”或展示一条拟合曲线，没有判据、扰动范围和对照数据，不构成检验创新"},
    "政策与机制设计":{
        "gap":"只预测现状不能回答如何干预，多主体利益、反馈和副作用没有进入决策",
        "action":"先列参与者、可操作政策变量和行为响应，再设计奖励、惩罚、信息或资源配置机制",
        "math":"把政策写成控制/决策变量，将主体收益、反馈、预算、公平和执行约束纳入模型",
        "validation":"比较无政策、现行政策和候选政策的效率、公平、风险、副作用与失效边界",
        "figure":"利益相关者图、因果回路图、政策情景曲线、权衡前沿",
        "table":"主体—目标—行为表、政策参数表、政策组合与影响对比表",
        "risk":"由相关性直接推出政策结论、忽略执行约束和受损群体，属于过度推断"},
    "时空动态刻画":{
        "gap":"静态总体平均会掩盖时间滞后、空间异质、路径依赖或实时事件带来的变化",
        "action":"加入时间/空间索引、状态转移、邻接关系或滚动窗口，使模型随观测或事件更新",
        "math":"建立差分/微分转移、时空权重、动态参数或滚动优化约束，并明确更新频率",
        "validation":"与静态模型比较不同时段/区域的误差和决策质量，进行滚动回测和漂移压力测试",
        "figure":"时间轨迹、空间热图、时空演化图、滚动误差图",
        "table":"时空索引与更新规则表、分区域/分时段指标表、静态与动态对比表",
        "risk":"只增加时间变量却不更新参数或只画地图没有空间机制，不能称为时空创新"},
    "表达与可视化":{
        "gap":"模型结构、变量传递或结果差异只靠长段文字呈现，评阅者难以快速核查论证闭环",
        "action":"把模型链、关键变量、基线对比和不确定性分别落到结构图、结果图与审计表中",
        "math":"图表必须绑定明确变量、单位、样本口径和评价指标，不新增未经模型计算的结论",
        "validation":"检查每幅图表是否能回答一个具体判断，并与正文结论、公式和数据来源逐项一致",
        "figure":"模型流程图、关键结果对比图、误差或敏感性图",
        "table":"变量口径表、模型对比表、结论—证据映射表",
        "risk":"仅美化配色或重复正文数字、没有提高可验证性，只能算排版改进"},
    "结构化建模亮点（待核实）":{
        "gap":"题目任务较多但缺少清晰的输入—模型—输出链，容易出现分问割裂和结论漏答",
        "action":"先建立最简单可运行基线，再把子问题按共享变量和依赖关系组织为递进链，随后选择一个真实缺口做实质改进",
        "math":"列出各子问题的变量、方程/目标、约束、输出和接口；证据不足处回原 PDF 补全",
        "validation":"逐问做闭环审计，并至少增加一个基线对比、误差、敏感性或可行性检验后再声明创新",
        "figure":"总流程图、子模型依赖图、结果—问题对应图",
        "table":"分问输入—模型—输出表、基线与候选改进对比表",
        "risk":"当前只有结构推断证据，不能把整理清楚直接写成方法创新，必须回原文核实"}}

def add_innovation_routes(items,primary,model_names):
    model_chain=" → ".join(model_names[:4])
    for item in items:
        play=INNOVATION_PLAYBOOK[item["type"]]
        clue=item["evidence"][:100]
        item["route"]={
            "baseline":CATEGORY_BASELINE[primary],
            "gap":play["gap"],
            "paper_focus":f"本篇识别到的模型链为“{model_chain}”。围绕原文线索“{clue}”，先定位该线索对应的变量、方程、目标、约束、特征或检验，再撤去这一变化构造论文内生基线",
            "action":play["action"],
            "math":play["math"],
            "validation":play["validation"]+"；"+CATEGORY_VALIDATION[primary],
            "figure":play["figure"],
            "table":play["table"],
            "risk":play["risk"]}
    return items

def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""): h.update(b)
    return h.hexdigest()

def norm(s): return re.sub(r"\n{3,}","\n\n",re.sub(r"[ \t]+"," ",s.replace("\u3000"," ").replace("\x00"," "))).strip()
OCR=None
def init_ocr():
    global OCR
    os.environ["OMP_NUM_THREADS"]="1"
    from rapidocr_onnxruntime import RapidOCR
    OCR=RapidOCR()

def extract_one(arg):
    ps,h=arg; p=Path(ps); dest=CACHE/f"{h}.json"
    if dest.exists(): return "cached"
    try:
        d=pymupdf.open(p); native=[norm(x.get_text("text")) for x in d]
        if sum(map(len,native[:5]))>=500: pages=[{"page":i+1,"text":t} for i,t in enumerate(native)]; mode="embedded-text"
        else:
            import numpy as np
            ids=sorted({i for i in [0,1,int(len(d)*.62),max(0,len(d)-3)] if i<len(d)}); pages=[]
            for i in ids:
                pix=d[i].get_pixmap(matrix=pymupdf.Matrix(1.35,1.35),alpha=False)
                img=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)
                r,_=OCR(img); pages.append({"page":i+1,"text":norm("\n".join(x[1] for x in (r or [])))})
            mode="selected-page-ocr"
        data={"source":str(p),"sha256":h,"pages_total":len(d),"mode":mode,"pages":pages}
    except Exception as e: data={"source":str(p),"sha256":h,"pages_total":0,"mode":"error","pages":[],"error":repr(e)}
    dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(json.dumps(data,ensure_ascii=False),encoding="utf-8"); return data["mode"]

def unique_pdfs():
    inv=PROJECT/"Data"/"inventory.json"
    if inv.exists():
        data=json.loads(inv.read_text(encoding="utf-8"))
        return [(Path(x["path"]),x["sha256"]) for x in data["chosen"]],data["duplicates"]
    g={}
    for p in SRC.rglob("*.pdf"): g.setdefault(digest(p),[]).append(p)
    chosen=[]; dup=[]
    for h,ps in g.items():
        q=max(ps,key=lambda p:(("一等奖" in p.name or "二等奖" in p.name),len(p.stem))); chosen.append((q,h))
        dup += [{"duplicate":str(p),"canonical":str(q),"sha256":h} for p in ps if p!=q]
    chosen=sorted(chosen); inv.parent.mkdir(parents=True,exist_ok=True)
    inv.write_text(json.dumps({"chosen":[{"path":str(p),"sha256":h} for p,h in chosen],"duplicates":dup},ensure_ascii=False,indent=2),encoding="utf-8")
    return chosen,dup

def strip_impl(x):
    x=re.sub(r"(?:并|再|然后)?(?:利用|运用|采用|通过)?(?:MATLAB|LINGO|SPSS|PYTHON|EXCEL|R语言|SAS)(?:软件|程序|函数|工具|平台)?(?:编程)?(?:进行)?(?:求解|计算|实现)?","经数学求解",x,flags=re.I)
    x=x.replace("用经数学求解","经数学求解")
    return re.sub(r"(?:代码|程序)(?:见|详见)附录[^。；]*[。；]?","",x)
def sents(t):
    out=[]
    for x in re.split(r"(?<=[。！？；])",t):
        x=strip_impl(re.sub(r"\s+","",x))
        x=re.sub(r"\*{2,}","〔显著性星号〕",x)
        if len(x)>12 and not re.search(r"承诺书|参赛报名号|参赛队员|所属学校|指导教师|从A/B/C/D中选择",x): out.append(x)
    return out
def select(t,pats,n=5):
    z=[]
    for s in sents(t):
        if any(re.search(p,s,re.I) for p in pats):
            s=s[:180]+("…" if len(s)>180 else "")
            if s not in z:z.append(s)
            if len(z)>=n:break
    return z
def innovation_carrier(kind):
    if kind in {"模型融合","模型改进与推广","分阶段与分类讨论","不确定性与情景分析","时空动态刻画","政策与机制设计"}:return "模型"
    if kind in {"专用求解策略","多目标与权衡"}:return "算法"
    if kind=="数据处理与特征构造":return "数据"
    if kind=="检验与稳健性":return "检验"
    return "表达"
def innovation_strength(kind,evidence):
    if kind=="结构化建模亮点（待核实）":return "无明确创新"
    if kind=="表达与可视化":return "表达优化"
    if kind=="检验与稳健性":return "证据增强"
    if re.search(r"(?:提高|降低|优于|改善|误差|精度|拟合度)[^。；]{0,35}(?:\d+(?:\.\d+)?%|\d+\.\d+)",evidence):return "实质性创新"
    return "题目适配创新"
def innovation_evidence_type(kind,evidence,basis):
    if basis=="结构推断":return "结构推断"
    carrier=innovation_carrier(kind)
    if carrier=="算法":return "算法或求解操作"
    if carrier=="数据":return "数据操作"
    if carrier=="检验":
        return "定量验证结果" if re.search(r"\d|结果表明|结果显示|达到|误差",evidence) else "检验操作"
    if carrier=="表达":return "图表或行文证据"
    return "模型或机制声明"
def evidence_page(evidence,pages):
    key=re.sub(r"\s+","",evidence)[:18]
    for page in pages:
        if key and key in re.sub(r"\s+","",page["text"]):return f"PDF第{page['page']}页"
    return "当前提取页未精确定位"
def innovation_points(t,primary,mode,probs,model_names,pages):
    hits=[]
    for kind,pat,delta in INNOVATION_RULES:
        evidence=select(t,[pat],1)
        if evidence:hits.append({"type":kind,"delta":delta,"evidence":evidence[0],"basis_raw":"原文可定位"})
    order={name:i for i,name in enumerate(INNOVATION_PRIORITY[primary])}
    hits.sort(key=lambda x:(order.get(x["type"],99),x["type"]))
    chosen=[]; seen=set()
    for hit in hits:
        if hit["type"] not in seen:chosen.append(hit); seen.add(hit["type"])
        if len(chosen)>=3:break
    if not chosen:
        clue=probs[0][1] if probs else "提取文本不足，未稳定定位明确的模型增量"
        chosen=[{"type":"结构化建模亮点（待核实）","delta":f"围绕{CATS[primary]}组织分问、模型与结果，但尚不能据此声明方法创新","evidence":clue[:180],"basis_raw":"结构推断"}]
    for item in chosen:
        item["carrier"]=innovation_carrier(item["type"])
        item["strength"]=innovation_strength(item["type"],item["evidence"])
        item["basis"]=innovation_evidence_type(item["type"],item["evidence"],item["basis_raw"])
        item["level"]="低" if item["basis"]=="结构推断" else ("中" if mode=="embedded-text" else "中-低")
        item["anchor"]=evidence_page(item["evidence"],pages)
    level="低" if all(x["level"]=="低" for x in chosen) else ("中" if mode=="embedded-text" else "中-低")
    return add_innovation_routes(chosen,primary,model_names),level
def abstract(t):
    m=re.search(r"摘\s*要\s*(.*?)(?:关\s*键\s*词|关键词|\n\s*1[\.、 ])",t,re.S); return (m.group(1) if m else t[:3500])[:5000]
def models(t):
    z=[]
    for name,pat,cat,target in MODELS:
        ms=list(re.finditer(pat,t,re.I))
        if ms:z.append({"name":name,"cat":cat,"target":target,"n":len(ms),"pos":ms[0].start()})
    return sorted(z,key=lambda x:(-x["n"],x["pos"]))
def classify(title,t,ms):
    c=Counter()
    for m in ms:c[m["cat"]]+=min(4,1+m["n"]//3)
    pats={"A":"压力|温度|轨迹|运动|物理|工程|流量|传热|扩散|力学","B":"调度|路径|配送|排班|选址|资源分配|组合优化","C":"数据|预测|分类|聚类|识别|特征|拟合|回归","D":"评价|评估|指标体系|排序|权重","E":"政策|可持续|生态|环境|人口|社会|经济|碳排放","F":"对策|竞争|冲突|多方利益|博弈"}
    for k,p in pats.items(): c[k]+=min(3,len(re.findall(p,title+t[:8000])))
    if not c:c["C"]=1
    x=[k for k,_ in c.most_common()]; return x[0],x[1:3]
def title_of(p,pages):
    if p.name in TITLE_OVERRIDES:return TITLE_OVERRIDES[p.name]
    def candidates(text):
        m=re.search(r"摘\s*要",text); pre=text[:m.start()] if m else text
        out=[]
        for line in pre.splitlines():
            x=re.sub(r"\s+","",line).strip("-—_：:《》.。")
            if 4<=len(x)<=48 and not re.search(r"承诺|编号|大学生数学建模|竞赛组委会|参赛队员|指导教师|学校|评阅|打印|日期|签名|第\d+页|我们完全明白|论文版权",x) and not re.fullmatch(r"[\d\W]+",x): out.append(x)
        return out, bool(m)
    for page in pages[:8]:
        cs,has_abstract=candidates(page["text"])
        if has_abstract and cs:return cs[-1]
    for page in pages[:3]:
        cs,_=candidates(page["text"])
        if cs:return min(cs,key=lambda x:(abs(len(x)-16),len(x)))
    x=re.sub(r"^(?:20\d{2})?.*?[A-FＥ]题?","",p.stem); return x[:50] or p.stem+"【标题解析缺失，人工补全】"
def problems(t):
    a=abstract(t); z=[]
    for sentence in sents(a):
        m=re.match(r"(?:针对|对于|在)?问题\s*([一二三四五六七八九十123456789])\s*[：:，,]?",sentence)
        if m:z.append((m.group(1),sentence[m.end():][:420]))
    if not z:z=[(str(i+1),x) for i,x in enumerate(select(a,["建立|求解|确定|预测|评价|分析"],4))]
    return z[:9]
def metadata(p,t):
    y=(re.search(r"20\d{2}",str(p)) or ["年份待核"])[0]; stem=p.stem.upper().replace("Ｅ","E")
    q=next((m.group(1) for pat in [
        r"([A-F])题",
        r"(?:20\d{2}|\d{2})([A-F])(?=[：:_\-\s\d])",
        r"^([A-F])\d{2,3}",
        r"20\d{2}[^\]\[（）()]{0,30}?([A-F])(?:题|\d)",
    ] if (m:=re.search(pat,stem))),"题号待核")
    probe=p.name+t[:2000]; award="国家一等奖" if re.search("国家?一等|国赛一等|国一",probe) else "国家二等奖" if re.search("国家?二等|国赛二等|国二",probe) else "奖项待核"
    pid=(re.search(r"([A-F]\d{2,3})",stem) or [f"{y}-{q}-{hashlib.md5(p.name.encode()).hexdigest()[:5]}"])[0]
    return y,q,award,pid
def safe(x):
    x=re.sub(r"[\x00-\x1f\x7f]","",x)
    x=re.sub(r'[<>:"/\\|?*]','',re.sub(r"\s+","",x)).strip(". ")[:28]
    return x or "标题待核"

def problem_source(year,problem):
    if not re.fullmatch(r"20\d{2}",str(year)) or not re.fullmatch(r"[A-F]",str(problem)):return None
    root=QUESTION_SRC/str(year)
    if not root.exists():return None
    candidates=[]
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".doc",".docx",".pdf"}:continue
        raw=p.stem.upper(); compact=re.sub(r"[^A-Z0-9题]","",raw)
        if re.search(r"附件|APPENDIX|FORMAT|README|参考",p.name,re.I):continue
        hit=(f"{year}{problem}" in compact or f"PROBLEM{problem}" in compact or compact in {f"{problem}题",problem} or compact.startswith(f"{year}{problem}"))
        if not hit:continue
        ext_rank={".pdf":0,".docx":1,".doc":2}[p.suffix.lower()]
        candidates.append((ext_rank,len(p.name),p))
    return str(min(candidates,key=lambda x:(x[0],x[1],str(x[2])))[2]) if candidates else None

def make_note(d):
    p=Path(d["source"]); pages=d["pages"]; full="\n".join(f'[PDF第{x["page"]}页]\n{x["text"]}' for x in pages); ti=title_of(p,pages); y,q,award,pid=metadata(p,full)
    ms=models(full); primary,secondary=classify(ti,full,ms); override=MODEL_CHAIN_OVERRIDES.get(d["sha256"]); names=(override["models"] if override else ([x["name"] for x in ms[:8]] or ["【模型名称解析缺失，人工补全】"])); probs=problems(full); qsource=problem_source(y,q)
    solve=select(full,["采用|利用|通过|求解|迭代|优化|拟合|检验"],6); res=select(abstract(full)+full[-5000:],["结果表明|结果显示|得出|求得|最优|最少|结论"],6); ana=select(full,["灵敏度|敏感性|稳健|鲁棒|误差|残差|检验|验证"],5); assumptions=select(full,["模型假设|假设|忽略|不考虑"],4)
    figs=select(full,[r"图\s*\d+|如图"],4); tabs=select(full,[r"表\s*\d+|如下表"],4); innovations,innovation_level=innovation_points(full,primary,d["mode"],probs,names,pages); miss="【解析缺失，人工补全】"; cat=f"{primary}类 {CATS[primary]}"
    L=["---","type: award-paper-review",f'paper_id: "{pid}"',f'year: "{y}"',f'problem: "{q}"',f'award: "{award}"',f'primary_category: "{cat}"',f'extraction_mode: "{d["mode"]}"',f'source_sha256: "{d["sha256"]}"',f'model_chain_review: "{"manual-pdf-reviewed" if override else "machine-extracted"}"',"status: machine-reviewed-needs-human-formula-check","tags: [competition/国赛, workflow/优秀论文拆解, area/数学建模]","---",f"# 论文标题：{ti}","## 基础元数据","- 竞赛：全国大学生数学建模竞赛",f"- 年份：{y}",f"- 题号：{q}",f"- 奖项：{award}",f"- 选题归类：{cat}"+(f"；次类别：{'、'.join(c+'类 '+CATS[c] for c in secondary)}" if secondary else ""),f"- 核心关键词：{'、'.join(names[:6])}",f"- 原始来源：{p}",f"- 解析说明：{d['mode']}；总页数 {d['pages_total']}；提取页 {','.join(str(x['page']) for x in pages)}","","## 1 赛题问题提炼"]
    L += [f"- 子问题{i}：{x}" for i,(_,x) in enumerate(probs,1)] or [f"- {miss}未稳定识别子问题边界。"]
    L += ["","## 2 模型整体框架",f"- 模型链：{' → '.join(names)}",f"- 模型链证据：{('PDF第'+override['pages']+'页；'+override['method']+'；2026-08-08 已复核') if override else '由当前 PDF 提取文本自动识别，待人工复核'}。","- 逻辑递进：题意与数据/机理抽象 → 分问建模 → 求解 → 结果检验 → 回答题目。","- 有效模型假设："]
    L += ([f"  - {x}" for x in assumptions] if assumptions else [f"  - {miss}未在提取页稳定定位完整假设段。"]) + ["- 符号说明：","","| 符号 | 含义 | 单位/取值域 |","|---|---|---|",f"| {miss} | 原文符号表或公式未能可靠转换 | 待人工核对 |","","## 3 各子问题建模思路【核心模块】"]
    for i,(_,x) in enumerate(probs or [("1",miss)],1):
        lm=[m["name"] for m in models(x)[:4]] or names[:2]; anchor=next((r["page"] for r in pages if x[:8] and x[:8] in r["text"]),pages[0]["page"] if pages else "待核")
        L.append(f"- 子问题{i}：选用模型为{'、'.join(lm)}；建模逻辑为{x}；模型选择理由：{REASON[primary]}；核心数学公式：{miss}；证据位置：PDF第{anchor}页附近。")
    L += ["","## 4 求解与计算思路"]+( [f"- {x}" for x in solve] if solve else [f"- {miss}未稳定定位求解说明。"] )+["- 仅保留数学处理与求解路线，已跳过代码、软件函数和编程步骤。","","## 5 结果与分析","- 核心结论："]
    L += ([f"  - {x}" for x in res] if res else [f"  - {miss}未稳定识别定量结论。"])+["- 分析工作："]+([f"  - {x}" for x in ana] if ana else ["  - 可解析文本中未定位到明确的灵敏度、稳健性或误差分析；不等于原文一定缺失。"])
    L += ["","## 6 模型评价","- 模型优点：",("  - 摘要按子问题交代方法与结果，模型链与任务对应较清楚。" if len(probs)>=2 else "  - 当前抽取范围不足以可靠归纳全部优点。"),f"  - 组合使用{'、'.join(names[:4])}处理题目。","- 模型存在不足与改进方向："]
    if d["mode"]=="selected-page-ocr":L.append("  - 扫描版仅对代表页 OCR，公式、符号和中间论证链需人工逐页复核。")
    if not ana:L.append("  - 建议补充参数扰动、样本外验证或误差分解。")
    L += ["  - 检查假设、变量、目标、约束、输出和结论是否逐项闭环。","","## 7 论文复用&写作亮点（知识库专用）",f"- 适用场景：以{CATS[primary]}为主的问题；数据结构、变量类型或机制不同不得直接套用。","- 结构亮点：摘要宜按“子问题—模型—求解—关键结果”，正文宜按“问题分析—假设与符号—建模—求解—检验—评价”闭环。","- 创新点提炼（竞赛语境，不构成学术首创声明）：",f"  - 总体证据等级：{innovation_level}。"]
    for item in innovations:
        L += [f"  - {item['type']}：{item['delta']}。",f"    - 创新载体：{item['carrier']}。",f"    - 创新强度：{item['strength']}。",f"    - 证据依据：{item['basis']}。",f"    - 证据等级：{item['level']}。",f"    - 证据位置：{item['anchor']}。",f"    - 原文线索：{item['evidence']}"]
    L += ["  - 使用限制：创新结论只相对本题常规解法成立；若要声称学术新颖性，必须另做文献检索与人工复核。","- 创新如何实现（Agent 复用分析，非论文原文声明）："]
    for i,item in enumerate(innovations,1):
        route=item["route"]
        L += [f"  - 路径{i}：{item['type']}",f"    - 第一步·建立基线：{route['baseline']}。",f"    - 第二步·定位缺口：{route['gap']}。",f"    - 本篇切入点：{route['paper_focus']}。",f"    - 第三步·实施改进：{route['action']}。",f"    - 第四步·数学落点：{route['math']}。",f"    - 第五步·验证增量：{route['validation']}。",f"    - 第六步·图表证据：图用{route['figure']}；表用{route['table']}。",f"    - 失败判据：{route['risk']}。",f"    - 写作句式：相较于上述基线，本文针对“{route['gap']}”实施“{route['action']}”，并通过“{route['validation']}”证明该改动的增量价值。"]
    L += ["- 对应评阅与任务要点映射：",f"  - 赛题原文：{qsource or '【未找到可靠赛题原文文件】'}。","  - 逐题官方评阅细则：题目目录未检出公开的逐题评分点文件，不编造评分权重或隐含标准。","  - 官方通用要求：[[04-Research/04-竞赛真题研究/05-官方规则与评阅/官方评阅资料索引|官方评阅资料索引]]。","  - 映射性质：Agent 将论文问题重述、模型章节与官方通用论文要求对照；不是官方逐题评分细则。","","| 要点 | 来源性质 | 论文对应处理 | 对齐判断 |","|---|---|---|---|"]
    for i,(_,x) in enumerate(probs or [("1",miss)],1):
        L.append(f"| 子问题{i}：{x[:90]} | 论文问题重述摘要；赛题原文路径供复核 | 第3节子问题{i}与模型链“{' → '.join(names[:2])}” | 已建立对应处理；公式与结果仍需回原 PDF 核验 |")
    L += ["| 论文结构完整性 | 官方通用要求 | 第2—6节覆盖假设、符号、建模、求解、结果、检验和评价 | 结构已覆盖；解析缺失项不视为已完成 |","- 原文图表线索："]
    L += ([f"  - {x}" for x in figs] if figs else ["  - 提取页未稳定识别图题，需核对原文。"])+["- 原文表格线索："]+([f"  - {x}" for x in tabs] if tabs else ["  - 提取页未稳定识别表题，需核对原文。"])+["- 建议的图表落点："]+[f"  - {x}" for x in GUIDE[primary]]+["- 客观缺口：所有“解析缺失”项必须回到原 PDF 补全，严禁反推或编造。","","## 8 双向链接标签"]
    target_for={name:target for name,_,_,target in MODELS}
    L += [f"[[{target_for.get(name,'模型-'+safe(name))}|模型-{name}]]" for name in names[:8]]
    L += [f"[[论文模型分类-{primary}类{CATS[primary]}]]",f"[[赛题-国赛{y}第{q}题]]","[[论文写作 Hub|写作-数模论文模板]]",""]
    return "\n".join(L),{"title":ti,"year":y,"problem":q,"award":award,"paper_id":pid,"primary":primary,"secondary":secondary,"models":names,"source":str(p),"mode":d["mode"],"sha256":d["sha256"],"model_chain_reviewed":bool(override),"model_chain_evidence":override,"question_source":qsource,"innovations":innovations,"innovation_types":[x["type"] for x in innovations],"innovation_carriers":sorted({x["carrier"] for x in innovations}),"innovation_strengths":sorted({x["strength"] for x in innovations}),"innovation_level":innovation_level}

def extract(workers):
    chosen,dup=unique_pdfs(); CACHE.mkdir(parents=True,exist_ok=True); counts=Counter()
    pending=[(p,h) for p,h in chosen if not (CACHE/f"{h}.json").exists()]
    counts["cached"]=len(chosen)-len(pending); print(f"[cached/{len(chosen)}] {counts['cached']}",flush=True)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers,initializer=init_ocr) as ex:
        jobs=[ex.submit(extract_one,(str(p),h)) for p,h in pending]
        for i,job in enumerate(concurrent.futures.as_completed(jobs),1):
            mode=job.result(); counts[mode]+=1; print(f"[{i}/{len(pending)}] {mode}",flush=True)
    (PROJECT/"Data"/"duplicates.json").write_text(json.dumps(dup,ensure_ascii=False,indent=2),encoding="utf-8"); print(dict(counts))
def build():
    OUT.mkdir(parents=True,exist_ok=True)
    expected=VAULT/"04-Research"/"04-竞赛真题研究"/"03-优秀获奖论文拆解"/"批量标准化拆解"
    if OUT.resolve()!=expected.resolve(): raise RuntimeError("Refusing to clean unexpected output directory")
    for old in OUT.rglob("G-*.md"): old.unlink()
    [ (OUT/f"{c}类-{n}").mkdir(exist_ok=True) for c,n in CATS.items() ]; recs=[]; used_stems=set()
    for f in sorted(CACHE.glob("*.json")):
        note,r=make_note(json.loads(f.read_text(encoding="utf-8"))); short={"国家一等奖":"国一","国家二等奖":"国二"}.get(r["award"],"奖项待核"); out=OUT/f"{r['primary']}类-{CATS[r['primary']]}"/f"G-{r['year']}-{r['problem']}-{short}-{safe(r['title'])}.md"
        if out.stem.lower() in used_stems:out=out.with_stem(out.stem+"-"+r["paper_id"])
        used_stems.add(out.stem.lower())
        out.write_text(note,encoding="utf-8"); r["note"]=str(out); recs.append(r)
    recs.sort(key=lambda r:(r["primary"],r["year"],r["problem"],r["title"])); counts=Counter(r["primary"] for r in recs)
    idx=["# 优秀论文模型分类索引","","分类依据是主要模型机制，不等同于赛题字母；次类别记录在单篇元数据中。",""]
    for c,n in CATS.items():
        idx += [f"## {c}类 {n}（{counts[c]}篇）","","| 年份 | 题号 | 奖项 | 论文 | 主要模型 |","|---|---|---|---|---|"]
        for r in [x for x in recs if x["primary"]==c]:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); idx.append(f"| {r['year']} | {r['problem']} | {r['award']} | [[{rel}|{r['title']}]] | {'、'.join(r['models'][:5])} |")
        idx.append("")
    (OUT/"优秀论文模型分类索引.md").write_text("\n".join(idx),encoding="utf-8")
    for c,n in CATS.items():
        hub=[f"# 论文模型分类-{c}类{n}","",f"- 分类定义：以{n}为论文主要建模机制。","- 分类原则：按主导数学机制归类，赛题字母仅作元数据，不直接决定类别。",f"- 总篇数：{counts[c]}",f"- 可创新方向：[[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/批量标准化拆解/优秀论文结构与模型分析指南#{c}类可创新点|{c}类可创新点]]。",f"- 创新生成法：[[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/批量标准化拆解/优秀论文结构与模型分析指南#12 如何从零形成可验证的创新|如何从零形成可验证的创新]]。",f"- 逐篇统计：[[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/批量标准化拆解/逐篇论文创新点统计与分类总结#{c}类 {n}|{c}类创新统计]]。","",f"## {c}类论文","",f"完整表格见 [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/批量标准化拆解/优秀论文模型分类索引#{c}类 {n}（{counts[c]}篇）|分类索引]]。",""]
        for r in [x for x in recs if x["primary"]==c]:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); hub.append(f"- [[{rel}|{r['title']}]]：{'、'.join(r['models'][:5])}")
        (OUT/f"论文模型分类-{c}类{n}.md").write_text("\n".join(hub)+"\n",encoding="utf-8")
    nodes=OUT/"知识节点"; model_dir=nodes/"模型"; problem_dir=nodes/"赛题"; model_dir.mkdir(parents=True,exist_ok=True); problem_dir.mkdir(parents=True,exist_ok=True)
    for old in nodes.rglob("*.md"):old.unlink()
    existing={p.stem for p in VAULT.rglob("*.md") if nodes not in p.parents}; target_for={name:target for name,_,_,target in MODELS}; by_model={}
    for r in recs:
        for name in r["models"]:
            target=target_for.get(name,"模型-"+safe(name)); by_model.setdefault(target,[]).append(r)
    for target,items in by_model.items():
        if target in existing:continue
        lines=[f"# {target}","","- 节点类型：模型/算法","- 说明：由优秀论文批量拆解自动建立的反向索引；具体定义、公式、创新性与适用条件需进入单篇笔记和原 PDF 复核。","","## 相关论文",""]
        for r in items:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); lines.append(f"- [[{rel}|{r['title']}]]")
        (model_dir/f"{target}.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    by_problem={}
    for r in recs:by_problem.setdefault(f"赛题-国赛{r['year']}第{r['problem']}题",[]).append(r)
    for target,items in by_problem.items():
        if target in existing:continue
        lines=[f"# {target}","","- 节点类型：竞赛赛题","- 说明：按论文元数据自动汇集；题号待核节点必须回到原文件名或赛题资料核实。","","## 相关优秀论文",""]
        for r in items:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); lines.append(f"- [[{rel}|{r['title']}]]")
        (problem_dir/f"{target}.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    type_counts=Counter(t for r in recs for t in r["innovation_types"]); level_counts=Counter(r["innovation_level"] for r in recs); carrier_counts=Counter(t for r in recs for t in r["innovation_carriers"]); strength_counts=Counter(t for r in recs for t in r["innovation_strengths"])
    inov=["# 逐篇论文创新点统计与分类总结","","## 统计口径","",f"- 统计论文：{len(recs)} 篇；本页只保留类别、创新载体、证据等级、模型链和单篇链接。","- 创新载体：模型、算法、数据、检验、表达；创新强度：实质性创新、题目适配创新、证据增强、表达优化、无明确创新。二者不可混用。","- 证据依据只使用：模型或机制声明、算法或求解操作、数据操作、检验操作、定量验证结果、图表或行文证据、结构推断。","- 证据等级衡量证据来源强度，不代表创新强弱：原生文本可定位为中，扫描版代表页 OCR 为中-低，仅结构推断为低。","- 逐题官方评分细则未在题目目录检出；本库仅映射赛题原文交付项与官方通用要求，不编造评分权重。详见 [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/批量标准化拆解/赛题原文与评阅映射来源审计|赛题原文与评阅映射来源审计]]。","- 创新强度、证据类型、原文线索、实施路径、图表位置和评阅映射均在单篇 `## 7`。","","## 汇总统计","",f"- 创新载体：{'、'.join(f'{k} {v}' for k,v in carrier_counts.most_common())}。",f"- 创新强度：{'、'.join(f'{k} {v}' for k,v in strength_counts.most_common())}。",f"- 证据等级：{'、'.join(f'{k} {v}' for k,v in sorted(level_counts.items()))}。",""]
    for c,n in CATS.items():
        subset=[r for r in recs if r["primary"]==c]
        inov += [f"## {c}类 {n}","","| 类别 | 创新载体 | 证据等级 | 模型链 | 论文 |","|---|---|---|---|---|"]
        for r in subset:
            rel=Path(r["note"]).relative_to(VAULT).with_suffix("").as_posix(); chain=" → ".join(r["models"][:4]).replace("|","／")
            inov.append(f"| {c}类 | {'、'.join(r['innovation_carriers'])} | {r['innovation_level']} | {chain} | [[{rel}|{r['title']}]] |")
        inov.append("")
    (OUT/"逐篇论文创新点统计与分类总结.md").write_text("\n".join(inov),encoding="utf-8")
    source_rows={}
    for r in recs:source_rows[(r["year"],r["problem"])]=r["question_source"]
    audit=["# 赛题原文与评阅映射来源审计","","- 本页只审计来源性质，不把赛题要求改写成官方评分细则。","- 题目目录中未检出命名为逐题评阅要点、评分细则或评分权重的公开文件。","- “赛题原文”用于核对交付任务；“官方通用要求”见 [[04-Research/04-竞赛真题研究/05-官方规则与评阅/官方评阅资料索引|官方评阅资料索引]]。","","| 年份 | 题号 | 来源性质 | 来源文件 | 使用限制 |","|---|---|---|---|---|"]
    for (year,problem),source in sorted(source_rows.items()):
        audit.append(f"| {year} | {problem} | {'赛题原文' if source else '未找到可靠来源'} | {source or '【缺失】'} | 仅映射交付任务，不代表逐题官方评分点 |")
    (OUT/"赛题原文与评阅映射来源审计.md").write_text("\n".join(audit)+"\n",encoding="utf-8")
    dup=json.loads((PROJECT/"Data"/"duplicates.json").read_text(encoding="utf-8")); ocr=sum(r["mode"]=="selected-page-ocr" for r in recs); pending=sum(r["award"]=="奖项待核" for r in recs)
    rep=["# 优秀论文批量处理汇总报告","",f"- 原始 PDF：{len(recs)+len(dup)} 份",f"- 去重后论文：{len(recs)} 篇",f"- 重复文件：{len(dup)} 份",f"- 扫描版代表页 OCR：{ocr} 篇",f"- 奖项待核：{pending} 篇","- 公式与符号：全部需对照原 PDF 人工复核","- 未处理：RAR、ZIP、DOC、DOCX","","## 分类统计","","| 类别 | 篇数 |","|---|---:|"]+[f"| {c}类 {n} | {counts[c]} |" for c,n in CATS.items()]+["","## 输出文件",""]+[f"- {Path(r['note']).name}" for r in recs]+["","## 缺失内容统计","","- PDF 文本层通常不能可靠保留公式版式，统一标记人工补全。","- 扫描版只 OCR 代表页，中间页图表和公式需人工复核。","- 未明确写出国一/国二时标记奖项待核。",""]
    (OUT/"处理汇总报告.md").write_text("\n".join(rep),encoding="utf-8"); (PROJECT/"Data"/"manifest.json").write_text(json.dumps(recs,ensure_ascii=False,indent=2),encoding="utf-8"); print(json.dumps({"notes":len(recs),"counts":dict(counts),"out":str(OUT)},ensure_ascii=False))
def main():
    a=argparse.ArgumentParser(); a.add_argument("action",choices=["extract","build","all"]); a.add_argument("--workers",type=int,default=4); x=a.parse_args()
    if x.action in ("extract","all"):extract(x.workers)
    if x.action in ("build","all"):build()
if __name__=="__main__":main()
