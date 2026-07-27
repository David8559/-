---
type: topic-hub
topic_tag: topic/预测模型
keywords: [预测, 回归, arima, 指数平滑, lstm, gm(1,1)]
tags: [system/topic-hub, topic/预测模型]
---

# 预测模型 Hub

<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->
## 复习与调用指南

> [!summary] 阅读顺序
> 先用“快速选择”确定算法，再读复习卡掌握思想和步骤，最后跳到实现区选择代码。源码默认折叠；数据明细不在复习页展开。

### 快速选择

| 算法或用途 | 主要解决什么 | 独立实现 | 语言 |
|---|---|---:|---|
| [[#ARIMA时间序列 · 复习|ARIMA时间序列]] | 利用差分后的自相关结构预测单变量序列。 | 28 | Python, SAS |
| [[#回归分析 · 复习|回归分析]] | 估计因变量与解释变量的条件关系并用于解释或预测。 | 60 | MATLAB, Python, SAS |
| [[#指数平滑 · 复习|指数平滑]] | 用递减权重平滑历史并递推预测。 | 3 | MATLAB |
| [[#时间序列方法 · 复习|时间序列方法]] | 分析按时间排列数据的趋势、季节和自相关。 | 7 | MATLAB |
| [[#未标注例程·预测与推断 · 复习|未标注例程·预测与推断]] | 这组代码的文件名缺乏算法语义，静态分析表明主要承担“预测与推断”。 | 3 | Python |
| [[#灰色预测GM · 复习|灰色预测GM]] | 用少量数据的累加生成序列建立指数趋势预测。 | 2 | MATLAB |
| [[#预测与时间序列 · 复习|预测与时间序列]] | 汇总回归、平滑、ARIMA和灰色预测等方法。 | 12 | MATLAB, Python, SAS |
| [[#预测方法 · 复习|预测方法]] | 根据历史和解释变量估计未来或未知结果。 | 15 | MATLAB |

### 逐算法复习卡

#### ARIMA时间序列 · 复习

- **解决什么**：利用差分后的自相关结构预测单变量序列。
- **核心思想**：AR描述滞后值，MA描述滞后误差，I负责平稳化。
- **标准流程**：画序列 → 平稳/差分 → ACF/PACF定阶 → 拟合 → 白噪声检验 → 滚动预测。
- **何时调用**：单变量、等间隔、差分后近似平稳的序列。
- **最易出错**：不能随机划分训练集；季节性、结构突变和残差相关必须检查。
- **库内覆盖**：28 个独立实现、28 个原始来源；语言：Python, SAS；其中 27 个识别到函数/类型入口。
- **优先阅读**：[[#ch39_ARIMA_sui_ji_fen_xi · SAS · fa831ed1|ch39_ARIMA_sui_ji_fen_xi]]、[[#相似实现组 · SAS · 306693de|example3_1]]、[[#例2.5 · SAS · 2f5f258b|例2.5]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#ARIMA时间序列 · 实现|跳转到源码实现区]]

#### 回归分析 · 复习

- **解决什么**：估计因变量与解释变量的条件关系并用于解释或预测。
- **核心思想**：通过损失最小化估计系数，并用残差和推断检验模型。
- **标准流程**：探索关系 → 编码/变换 → 拟合 → 残差诊断 → 共线性检查 → 验证/预测。
- **何时调用**：目标连续或可用GLM描述且需要可解释关系。
- **最易出错**：相关不等于因果；外推、异方差、共线性和数据泄漏常见。
- **库内覆盖**：60 个独立实现、60 个原始来源；语言：MATLAB, Python, SAS；其中 18 个识别到函数/类型入口。
- **优先阅读**：[[#第3章例题程序 · SAS · 7d1a3235|第3章例题程序]]、[[#ch27_fei_xian_xing_hui_gui1 · SAS · cb48d5ff|ch27_fei_xian_xing_hui_gui1]]、[[#ch25_duo_yuan_xian_xing_hui_gui · SAS · e4f5df20|ch25_duo_yuan_xian_xing_hui_gui]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#回归分析 · 实现|跳转到源码实现区]]

#### 指数平滑 · 复习

- **解决什么**：用递减权重平滑历史并递推预测。
- **核心思想**：水平、趋势和季节项按平滑系数更新。
- **标准流程**：识别水平/趋势/季节 → 选SES/Holt/Winters → 估参数 → 滚动验证 → 预测区间。
- **何时调用**：短中期预测且近期信息更重要时使用。
- **最易出错**：结构突变和长周期外推能力有限。
- **库内覆盖**：3 个独立实现、3 个原始来源；语言：MATLAB；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#ex8_5 · MATLAB · 34880373|ex8_5]]、[[#三次指数平滑及其时间序列预测 · MATLAB · 08136fda|三次指数平滑及其时间序列预测]]、[[#二次指数平滑及其时间序列预测代码 · MATLAB · 0418eacb|二次指数平滑及其时间序列预测代码]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#指数平滑 · 实现|跳转到源码实现区]]

#### 时间序列方法 · 复习

- **解决什么**：分析按时间排列数据的趋势、季节和自相关。
- **核心思想**：当前值与历史状态/误差相关，验证必须保持时间顺序。
- **标准流程**：可视化 → 分解/平稳性 → 定模型 → 拟合 → 残差白噪声 → 滚动预测。
- **何时调用**：等间隔观测且顺序信息不可打乱时使用。
- **最易出错**：训练测试切分、缺失时间点和季节周期必须明确。
- **库内覆盖**：7 个独立实现、7 个原始来源；语言：MATLAB；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#ex8_7 · MATLAB · 9f7d97f2|ex8_7]]、[[#ex8_1 · MATLAB · 5ce96690|ex8_1]]、[[#ex8_2 · MATLAB · d154d8db|ex8_2]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#时间序列方法 · 实现|跳转到源码实现区]]

#### 未标注例程·预测与推断 · 复习

- **解决什么**：这组代码的文件名缺乏算法语义，静态分析表明主要承担“预测与推断”。
- **核心思想**：先从函数、调用链和关键库识别计算角色，不在证据不足时强行归入具体模型。
- **标准流程**：确认入口 → 阅读参数和关键操作 → 分离硬编码 → 包装成函数 → 用最小样例验证。
- **何时调用**：仅在核对源码正文和输出后复用；优先把它作为辅助代码而非完整模型。
- **最易出错**：当前分类属于保守推断，运行验证后应补充准确算法名称。
- **库内覆盖**：3 个独立实现、3 个原始来源；语言：Python；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#Pex11_1 · Python · 2b50fca2|Pex11_1]]、[[#相似实现组 · Python · 6ed53c71|Pex11_3]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#未标注例程·预测与推断 · 实现|跳转到源码实现区]]

#### 灰色预测GM · 复习

- **解决什么**：用少量数据的累加生成序列建立指数趋势预测。
- **核心思想**：AGO削弱波动，再拟合一阶白化微分方程。
- **标准流程**：级比检验 → AGO → 估参数 → 时间响应 → 还原 → 残差/后验差检验。
- **何时调用**：样本少、趋势较单调且信息不完整。
- **最易出错**：波动大、结构突变或长期预测时可靠性下降。
- **库内覆盖**：2 个独立实现、2 个原始来源；语言：MATLAB；其中 1 个识别到函数/类型入口。
- **优先阅读**：[[#灰色预测MATLAB程序 · MATLAB · ac1c557a|灰色预测MATLAB程序]]、[[#灰色预测算法代码 · MATLAB · cc673c84|灰色预测算法代码]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#灰色预测GM · 实现|跳转到源码实现区]]

#### 预测与时间序列 · 复习

- **解决什么**：汇总回归、平滑、ARIMA和灰色预测等方法。
- **核心思想**：横截面关系与时间依赖需要不同验证方式。
- **标准流程**：判断数据是否有时间顺序 → 选回归或序列模型 → 按时间验证 → 诊断残差 → 输出区间。
- **何时调用**：作为预测模型选择入口。
- **最易出错**：随机划分时间序列、忽略结构突变和只给点预测是常见错误。
- **库内覆盖**：12 个独立实现、12 个原始来源；语言：MATLAB, Python, SAS；其中 7 个识别到函数/类型入口。
- **优先阅读**：[[#example1_1 · SAS · f8540a61|example1_1]]、[[#example1_2 · SAS · 2fa257b0|example1_2]]、[[#example1_3 · SAS · 183adc9b|example1_3]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#预测与时间序列 · 实现|跳转到源码实现区]]

#### 预测方法 · 复习

- **解决什么**：根据历史和解释变量估计未来或未知结果。
- **核心思想**：趋势、相关结构、机制和不确定性共同决定模型选择。
- **标准流程**：定义预测目标/跨度 → 时间切分 → 建基线 → 选模型 → 滚动验证 → 预测区间。
- **何时调用**：需要外推到未来或未观测样本时使用。
- **最易出错**：必须防止未来信息泄漏，并与朴素基线比较。
- **库内覆盖**：15 个独立实现、15 个原始来源；语言：MATLAB；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#anli15_1 · MATLAB · 64e3508f|anli15_1]]、[[#相似实现组 · MATLAB · d99f5284|Untitled5]]、[[#ex15_10 · MATLAB · 733b1ff4|ex15_10]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#预测方法 · 实现|跳转到源码实现区]]

### 通用调用检查表

1. 先确认当前问题是否满足复习卡中的适用条件。
2. 优先选择标有函数/类型入口的实现，脚本型代码先重构参数。
3. 用最小样例跑通，再替换为项目输入；不要一开始就接入完整题目。
4. 检查目标方向、变量单位、边界条件、随机种子和软件版本。
5. 保存运行环境、参数、结果与检验，验证通过后再进入项目正式代码。

<!-- END AUTO-HUB-STUDY-GUIDE -->

> 自动更新：2026-07-27 · 匹配笔记：6

## 相关笔记

- [[04-Research/01-建模基础理论/【数学建模入门】保姆级小白教程，没学过建模的看完这篇也能提交竞赛论文！]] — 相关度 18
- [[04-Research/03-建模算法源码库/代码资料索引]] — 相关度 12
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2021-C题-生产企业原材料订购与运输/2021-C题-本地解答与四篇国奖论文对照复盘]] — 相关度 3
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B175-论文拆解]] — 相关度 2
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/2020-B题-获奖论文横向对比]] — 相关度 1
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B125-论文拆解]] — 相关度 1

## 邻接主题

- [[Topic Index]]
- [[数据处理 Hub]]
- [[模型检验 Hub]]
- [[微分方程动力学 Hub]]

<!-- BEGIN AUTO-INTEGRATED-CODE -->
## 源码实现库（按需调用）

> [!warning] 使用边界
> 以下源码保留全文与来源，但默认均未运行验证。数据依赖明细已从阅读页省略；调用时按代码理解卡完成参数化、最小样例和结果检验。来源显示为可复制路径，不直接调用 Windows 打开未知扩展名。

- 本 Hub 收录原始源码文件：130
- 精确去重后的独立实现：130
- 合并后的实现组：124

### 实现索引

| 算法或用途 | 独立实现 | 原始源码 |
|---|---:|---:|
| [[#ARIMA时间序列 · 实现|ARIMA时间序列]] | 28 | 28 |
| [[#回归分析 · 实现|回归分析]] | 60 | 60 |
| [[#指数平滑 · 实现|指数平滑]] | 3 | 3 |
| [[#时间序列方法 · 实现|时间序列方法]] | 7 | 7 |
| [[#未标注例程·预测与推断 · 实现|未标注例程·预测与推断]] | 3 | 3 |
| [[#灰色预测GM · 实现|灰色预测GM]] | 2 | 2 |
| [[#预测与时间序列 · 实现|预测与时间序列]] | 12 | 12 |
| [[#预测方法 · 实现|预测方法]] | 15 | 15 |

### ARIMA时间序列 · 实现

利用差分、自回归和移动平均结构进行时间序列建模与预测。

#### ch37_chun_sui_ji_xing_jian_yan1 · SAS · ac6519cb

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`859aa72cdaf6864683948d1882f779efeff8fc8b11773f2e2fa43113b86303ff`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch37_chun_sui_ji_xing_jian_yan1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data ex1;
input price @@;
time=intnx('week','13oct2006'd,_n_-1);
format time date7.;
cards;
10.3000 8.5269 9.0421 10.1727 9.9079 8.9714 9.0145 9.4738 9.5258 9.7017
10.0582 9.5292 8.9786 9.1743 9.8478 9.6218 9.0342 9.1891 9.6062 9.8946 
9.4853 9.2557 9.2805 9.5258 10.1192 9.6384 8.8495 9.2644 9.4939 9.6623
9.4212 9.5570 9.7627 9.5639 8.7962 9.1777 10.2288 10.3722 9.0861 8.8148  
9.2055 9.4473 9.2903 9.5358 9.5294 9.5368 9.4168 9.3237 9.5939 9.8874  
10.3007 9.3051 8.6804 9.5337 9.8757 9.2799 9.3030 10.0135 10.1025 10.1310
9.6605 9.8175 9.4935 9.0052 9.2178 10.0131 9.6019 9.4843 9.2807 9.4567
;
run;
proc gplot;
plot price*time/ vaxis=8.5 to 10.5 by 0.1;
symbol i=join v=star cv=red ci=green;
run;
/*proc arima data=ex1;
identify var=price;
run;*/
/*proc arima data=ex1;
identify var=price minic p=(0:6) q=(0:6);
run;*/
proc arima data=ex1;
identify var=price;
estimate p=2 method=ml;
run;
````

</details>

#### ch37_chun_sui_ji_xing_jian_yan2 · SAS · 6319fb79

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`762d9b4ef5a7b3909f7fb8ac4bcf20a28ee760d25f0f8a2e074f4baad0a562b6`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch37_chun_sui_ji_xing_jian_yan2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data datas1;
  input x_t @@;
  time=intnx('day','01jan2014'd,_n_-1);
  format time monyy.;
  cards;
    10	15	10	10	12	10	7	7	10	14	8	17
    14	18	3	9	11	10	6	12	14	10	25	29
    33	33	12	19	16	19	19	12	34	15	36	29
    26	21	17	19	13	20	24	12	6	14	6	12
    9	11	17	12	8	14	14	12	5	8	10	3
    16	8	8	7	12	6	10	8	10	5		
;
run;
proc gplot data = datas1;
plot x_t*time;
symbol i=join v=star cv=red ci=green;
run;
proc arima data = datas1;
identify var=x_t nlag=24; 
run;
data datas2;
set datas1;
y_t = dif1(x_t);
run;
proc gplot data = datas2;
plot y_t*time;
symbol i=join v=star cv=red ci=green;
run;
proc arima data = datas2;
identify var=y_t nlag=24; 
run;
````

</details>

#### ch38_yue_du_shu_ju_ji_jie_tiao_zheng · SAS · d31e3107

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC PRINT`、`PROC SGPLOT`、`PROC X11`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`125956ed3cebb0d08ffb48e3eaa440557690966ce3e6750932178bb85b5867a8`
- 语言：SAS
- 符号：`PROC PRINT`, `PROC SGPLOT`, `PROC X11`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch38_yue_du_shu_ju_ji_jie_tiao_zheng.sas`

<details>
<summary>展开原始代码</summary>

````sas
data sales;
input sales @@;
date = intnx( 'month', '01jan1993'd, _n_-1 );
format date monyy5.;
datalines;
977.5	892.5	942.3	941.3	962.2	1005.7	963.8	959.8	1023.3	1051.1	1102	1415.5
1192.2	1162.7	1167.5	1170.4	1213.7	1281.1	1251.5	1286	1396.2	1444.1	1553.8	1932.2
1602.2	1491.5	1533.3	1548.7	1585.4	1639.7	1623.6	1637.1	1756	1818	1935.2	2389.5
1909.1	1911.2	1860.1	1854.8	1898.3	1966	1888.7	1916.4	2083.5	2148.3	2290.1	2848.6
2288.5	2213.5	2130.9	2100.5	2108.2	2164.7	2102.5	2104.4	2239.6	2348	2454.9	2881.7
2549.5	2306.4	2279.7	2252.7	2265.2	2326	2286.1	2314.6	2443.1	2536	2652.2	3131.4
2662.1	2538.4	2403.1	2356.8	2364	2428.8	2380.3	2410.9	2604.3	2743.9	2781.5	3405.7
2774.7	2805	2627	2572	2637	2645	2597	2636	2854	3029	3108	3680
;
run;
proc x11 data=sales;
monthly date=date;
var     sales;
arima   maxit=60;
tables  d11;
output  out=out b1=series d10=season d11=adjusted d12=trend d13=irr;
proc print data=out;
run ;
title 'Monthly Retail Sales Data';
proc sgplot data=out;
series x=date y=series / markers
markerattrs=(color=red symbol='asterisk')
lineattrs=(color=red)
legendlabel="original" ;
series x=date y=adjusted / markers
markerattrs=(color=blue symbol='circle')
lineattrs=(color=blue)
legendlabel="adjusted" ;
yaxis label='Original and Seasonally Adjusted Time Series';
run;
title 'Monthly Seasonal Factors (in percent)';
proc sgplot data=out;
series x=date y=season / markers markerattrs=(symbol=CircleFilled) ;
run;
title 'Monthly Retail Sales Data (in $1000)';
proc sgplot data=out;
series x=date y=trend / markers markerattrs=(symbol=CircleFilled) ;
run;
title 'Monthly Irregular Factors (in percent)';
proc sgplot data=out;
series x=date y=irr / markers markerattrs=(symbol=CircleFilled) ;
run;
````

</details>

#### ch39_ARIMA_sui_ji_fen_xi · SAS · fa831ed1

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`、`PROC PRINT`、`PROC SGPLOT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`77b91776c73b4e70492d08d66e645cccb67f4ac4f079191d9bc9bb0c91f778f6`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`, `PROC PRINT`, `PROC SGPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch39_ARIMA_sui_ji_fen_xi.sas`

<details>
<summary>展开原始代码</summary>

````sas
data arimad01;
date=intnx('month','31dec1948'd,_n_);
input x @@;
format date monyy5.;
datalines;
112	118	132	129	121	135	148	148	136	119	104	118
115	126	141	135	125	149	170	170	158	133	114	140
145	150	178	163	172	178	199	199	184	162	146	166
171	180	193	181	183	218	230	242	209	191	172	194
196	196	236	235	229	243	264	272	237	211	180	201
204	188	235	227	234	264	302	293	259	229	203	229
242	233	267	269	270	315	364	347	312	274	237	278
284	277	317	313	318	374	413	405	355	306	271	306
315	301	356	348	355	422	465	467	404	347	305	336
340	318	362	348	363	435	491	505	404	359	310	337
360	342	406	396	420	472	548	559	463	407	362	405
417	391	419	461	472	535	622	606	408	461	390	432
;
run;
proc sgplot data=arimad01;
series x=date y=x / markers;
run;
proc arima data=arimad01;
identify var=x;
run;
data arimad02;
set arimad01 ;
xlog=log(x);
run;
proc print data = arimad02;
run;
goptions reset=global gunit=pct cback=white border
             htitle=6 htext=3 ftext=swissb colors=(black);
proc gplot data=arimad02 ;
plot  xlog*date  / vaxis=axis1 haxis=axis2 
href='31dec1949'd to '1jan61'd by year;
plot2   x*date  /vaxis=axis3 vref=100;
symbol1 i=join v=c h=3 l=1 r=1 font=swissb c=green;
symbol2 i=join v=c h=3 l=1 r=1 font=swissb c=blue;
    axis1   label=('Log')       order=(4.5 to 6.5 by 0.5) offset=(0,45);
axis2   label=('12 Month')  order=('1jan49'd to '1jan61'd by year);
axis3   label=('Passenger') order=(100 to 700 by 100) offset=(23,0);
format  date monyy. ;
title1 'Time Serial Log Chart';
run;
data arimad03;
set arimad02;
dif12=dif1(xlog)-(lag1(xlog)-lag12(xlog));
run;
proc gplot data=arimad03 ;
plot    xlog*date   /vaxis=axis1 haxis=axis2 
href='31dec1949'd to '1jan61'd by year;
plot2   dif12*date  /vaxis=axis3 vref=-1;
symbol1 i=join v=c h=3 l=1 r=1 font=swissb c=green;
symbol2 i=join v=c h=3 l=1 r=1 font=swissb c=blue;
axis1   label=('Log')      order=(4.5 to 6.5 by 0.5) offset=(0,45);
axis2   label=('12 Month') order=('1jan49'd to '1jan61'd by year);
axis3   label=('Dif1-12')  order=(-1 to 1 by 0.2) offset=(23,0);
format  date monyy. ;
title1 'Time Serial Dif Chart';
run;
proc arima data=arimad02;
identify  var=xlog(1,12) nlag=15;
run;
proc arima data=arimad03;
identify var=xlog(1,12) nlag=15;
estimate q=(1)(12) p=(1)(12) noconstant outmodel=xmode;
run;
proc arima data=arimad03;
identify  var=xlog(1,12) nlag=15;
estimate  q=(1)(12)  noconstant outmodel=xmode;
forecast lead=12 interval=month id=date out=forxlog;
run;
proc print data=forxlog;
run;
data arimad04;
set forxlog;
x=exp(xlog);
forecast=exp(forecast);
l95=exp(l95);
u95=exp(u95);
proc print data=arimad04;
run;
proc gplot data=arimad04;
where date>='1jan57'd;
plot x*date forecast*date l95*date u95*date /overlay vaxis=axis1 haxis=axis2 href='31dec60'd ;
symbol1 i=join  v=C h=2.5 l=1 font=swissb c=red;
symbol2 i=join  v=F h=3   l=1 font=swissb c=blue;
symbol3 i=join  l=1 font=swissb c=green;
symbol4 i=join  l=1 font=swissb c=green;
axis1   label=('Passenger') order=(250 to 800 by 50);
axis2   label=('Month')     order=('1jan57'd to '1jan62'd by year);
format  date monyy. ;
title1 'Forecast Chart';
title2 'C--x';
title3 'F--forecast';
title4 'None--u95 and l95';
run;
````

</details>

#### 相似实现组 · SAS · 306693de

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：example3_1.sas

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9d5cf548b36f9252c43073104f5736cc6f24bb5eeb50381a07c8467ca3b6a7f4`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/example3_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example3_1;                                                                                                                           
input x@@;                                                                                                                              
time=_n_;                                                                                                                               
cards;                                                                                                                                  
0.30	-0.45	0.36	0.00	0.17	0.45	2.15
4.42	3.48	2.99	1.74	2.40	0.11	0.96
0.21	-0.10	-1.27	-1.45	-1.19	-1.47	-1.34
-1.02	-0.27	0.14	-0.07	0.10	-0.15	-0.36
-0.50	-1.93	-1.49	-2.35	-2.18	-0.39	-0.52
-2.24	-3.46	-3.97	-4.60	-3.09	-2.19	-1.21
0.78	0.88	2.07	1.44	1.50	0.29	-0.36
-0.97	-0.30	-0.28	0.80	0.91	1.95	1.77
1.80	0.56	-0.11	0.10	-0.56	-1.34	-2.47
0.07	-0.69	-1.96	0.04	1.59	0.20	0.39
1.06	-0.39	-0.16	2.07	1.35	1.46	1.50
0.94	-0.08	-0.66	-0.21	-0.77	-0.52	0.05
； 
proc gplot data=example3_1;
plot x*time=1;
symbol1 c=red I=join v=star;   
proc arima data= example3_1;                                                                                                                             
identify var=x nlag=8;   
estimate q=4;
forecast lead=5 id=time out=results;
proc gplot data=results;                                                                                                                
plot x*time=1 forecast*time=2 l95*time=3 u95*time=3/overlay;                                                                            
symbol1 c=black i=none v=star;                                                                                                          
symbol2 c=red i=join v=none;                                                                                                            
symbol3 c=green i=join v=none l=2;                                                                                                          
run;
````

</details>

##### 变体 2：example6_1.sas

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`、`PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`82492837cfac22b87203b5a2ab63b676d37b6962cddef885d5fb1b1c77c3ba0f`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`, `PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第六章/example6_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
  data example6_1;                                                                                                                           
input x y@@;                                                                                                                              
t=_n_;                                                                                                                                  
cards;
-2.94 	9.83 	-2.14 	12.63 	1.01 	14.77 
2.84 	17.29 	-0.79 	18.07 	1.46 	17.38 
5.44 	19.17 	1.65 	9.12 	6.53 	22.82 
8.93 	23.58 	8.67 	15.19 	8.36 	22.43 
9.79 	17.83 	11.67 	25.49 	9.70 	28.40 
9.18 	23.15 	11.13 	19.70 	9.39 	22.32 
12.89 	30.01 	8.45 	21.27 	6.66 	11.52 
4.15 	15.57 	2.57 	9.91 	2.29 	23.28 
-3.28 	13.75 	-5.21 	3.38 	-3.74 	15.81 
-8.73 	12.41 	-15.89 	5.54 	-12.15 	4.83 
-10.86 	14.79 	-17.16 	4.14 	-18.55 	-5.36 
-11.42 	4.79 	-16.02 	0.91 	-14.36 	-5.49 
-17.98 	6.01 	-16.94 	2.78 	-17.52 	-2.49 
-13.44 	10.30 	-14.11 	-0.32 	-15.16 	2.35 
;
proc gplot data=example6_1;
plot x*t=1 y*t=2/overlay;
symbol1 c=black i=join v=none;
symbol2 c=red i=join v=none w=2 l=2;
proc arima data=example6_1;
identify var=x stationarity=(adf=1);                                                                                                                                                                                                 
identify var=y stationarity=(adf=1); 
proc reg data= example6_1;
model y=x;
output out=out residual=residual;
proc arima data=out;
identify var=residual stationarity=(adf);
proc arima data=example6_1;
identify var=y crosscorr=x;  
estimate input=x plot;
forecast lead=5 id=t out=result;
proc gplot data=result;
plot y*t=1 forecast*t=2 l95*t=3 u95*t=3/overlay;
symbol1 c=black i=none v=star;
symbol2 c=rd i=join v=none;
symbol3 c=green i=join v=none;
run;
````

</details>

#### 例3.13 · SAS · 1704e4ef

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`35617dc49dec4e4c11673954c52881e34bffb5c7863186b9c63a30ccdbaf509b`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.13.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input yield @@;
time=_n_;
cards;
47	64	23	71	38	64	55	41	59	48	71	35	57	40
58	44	80	55	37	74	51	57	50	60	45	57	50	45
25	59	50	71	56	74	50	58	45	54	36	54	48	55
45	57	50	62	44	64	43	52	38	59	55	41	53	49
34	35	54	45	68	38	50	60	39	59	40	57	54	23
;
proc gplot;
plot yield*time;
symbol v=star i=join c=red;
proc arima data=a;
identify var=yield nlag=18;
run;
````

</details>

#### 例3.5 · SAS · 74ad697c

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fb03732356fca16a9db7c5814e699c0c7bcf350c39b9e86cdf84cab6249ae753`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.5.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
x1_0=0;
x2_0=0;
x3_0=0;
x3_1=0;
x4_0=0;
x4_1=0;
do t=-100 to 1000;
e=rannor(12345);
x1=0.8*x1_0+e;
x2=-0.8*x2_0+e;
x3=x3_0-0.5*x3_1+e;
x4=-x4_0-0.5*x4_1+e;
x1_0=x1;
x2_0=x2;
x3_1=x3_0;
x4_1=x4_0;
x3_0=x3;
x4_0=x4;
if t>0 then output ;
end;
data a;
set a;
keep t x1 x2 x3 x4;
proc arima;
identify var=x1 nlag=20 outcov=out1;
identify var=x2 nlag=20 outcov=out2;
identify var=x3 nlag=20 outcov=out3;
identify var=x4 nlag=20 outcov=out4;
proc gplot data=out1;
plot corr*lag ;
proc gplot data=out2;
plot corr*lag ;
proc gplot data=out3;
plot corr*lag ;
proc gplot data=out4;
plot corr*lag ;
proc gplot data=out1;
plot partcorr*lag ;
proc gplot data=out2;
plot partcorr*lag ;
proc gplot data=out3;
plot partcorr*lag ;
proc gplot data=out4;
plot partcorr*lag ;
symbol c=red i=needle v=none;
run;
````

</details>

#### 例3.6 · SAS · bb373875

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2e11630e779f22dd44134ec46155253fbd3f140ded5f25fa7110a81d3ce12232`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.6.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
e_1=0;
e_2=0;
do t=-100 to 1000;
e=rannor(12345);
x1=e-2*e_1;
x2=e-0.5*e_1;
x3=e-4/5*e_1+16/25*e_2;
x4=e-5/4*e_1+25/16*e_2;
e_2=e_1;
e_1=e;
if t>0 then output ;
end;
data a;
set a;
keep t x1 x2 x3 x4;
proc arima;
identify var=x1 nlag=20 outcov=out1;
identify var=x2 nlag=20 outcov=out2;
identify var=x3 nlag=20 outcov=out3;
identify var=x4 nlag=20 outcov=out4;
proc gplot data=out1;
plot corr*lag ;
proc gplot data=out2;
plot corr*lag ;
proc gplot data=out3;
plot corr*lag ;
proc gplot data=out4;
plot corr*lag ;
proc gplot data=out1;
plot partcorr*lag ;
proc gplot data=out2;
plot partcorr*lag ;
proc gplot data=out3;
plot partcorr*lag ;
proc gplot data=out4;
plot partcorr*lag ;
symbol c=red i=needle v=none;
run;
````

</details>

#### 例3.7 · SAS · 54dbb8b0

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e6b67c23f61c5002a4999bddffe0b48161b112eeb5ef4cf714dfa9d89e5b720e`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.7.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
x_1=0;
e_1=0;
do t=-100 to 1000;
e=rannor(12345);
x=0.5*x_1+e-0.8*e_1;
x_1=x;
e_1=e;
if t>0 then output ;
end;
data a;
set a;
keep t x;
proc arima;
identify var=x nlag=20 outcov=out;
proc gplot data=out;
plot corr*lag partcorr*lag ;
symbol c=red i=needle v=none;
run;
````

</details>

#### 例3.8 · SAS · 54228bd3

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4e9479a3845ebe8f50bb9b7e9207d87ebeb1fa585d333895a5c27af2818f1263`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.8.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm;
data a;
input overshort@@;
day=_n_;
cards;
78	-58	53	-63	13	-6	-16	-14
3	-74	89	-48	-14	32	56	-86
-66	50	26	59	-47	-83	2	-1
124	-106	113	-76	-47	-32	39	-30
6	-73	18	2	-24	23	-38	91
-56	-58	1	14	-4	77	-127	97
10	-28	-17	23	-2	48	-131	65
-17							
;
proc gplot;
plot overshort*day;
symbol v=diamond i=join c=red;
proc arima data=a;
identify var=overshort;
estimate q=1;
run;
````

</details>

#### 例3.9 · SAS · e521ea2b

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`、`PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a145a8f0b96d6dc4f5d1e5df941091af67ad78a226c0aeac26db1737a2e34b3a`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`, `PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.9.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data a;
input change_temp@@;
dif=dif(change_temp);
year=1880+_n_-1;
cards;
-.40    -.37    -.43    -.47    -.72    -.54    -.47    -.54    -.39    -.19
-.40    -.44    -.44    -.49    -.38    -.41    -.27    -.18    -.38    -.22
-.03    -.09    -.28    -.36    -.49    -.25    -.17    -.45    -.32    -.33
-.32    -.29    -.32    -.25    -.05    -.01    -.26    -.48    -.37    -.20
-.15    -.08    -.14    -.13    -.12    -.10     .13    -.01     .06    -.17
-.01     .09     .05    -.16     .05    -.02     .04     .17     .19     .05
 .15     .13     .09     .04     .11    -.03     .03     .15     .04    -.02
-.13     .02     .07     .20    -.03    -.07    -.19     .09     .11     .06
 .01     .08     .02     .02    -.27    -.18    -.09    -.02    -.13     .02
 .03    -.12    -.08     .17    -.09    -.04    -.24    -.16    -.09     .12
 .27     .42     .02     .30     .09     .05
;
proc print;
proc gplot;
plot dif*year;
symbol v=star i=join c=black;
proc arima data=a;
identify var=dif nlag=12;
estimate p=1 q=1;
run;
````

</details>

#### example2_1 · SAS · 00fbc0b6

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6109a0cb018578784a2f1304713b299e0a52c81ce285e0bbcd30ebc3ecb431f6`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/example2_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example2_2;
input  freq@@;
year=intnx('year','1jan1970'd,_n_-1);
format year year4.;
cards;
97 154 101 149 221 157 128 215 129 239 155 238 276
204 136 296 176 307 154 227 200 291 233 356 221 309
321 156 234 432 278 356 254 349 322 254 327 432 401
;
proc gplot;
plot freq*year;
symbol v=square c=red i=join;
proc arima data= example2_2;
identify var=freq nlag=22;
run;
````

</details>

#### example2_2 · SAS · 50bfb197

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`52be3f09feb2b5abfcaf3dfeba9a5d132dd32433f3d4090eab24798a7f426c0e`
- 语言：SAS
- 符号：`PROC ARIMA`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/example2_2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example2_2;
input  freq@@;
year=intnx('year','1jan1970'd,_n_-1);
format year year4.;
cards;
97 154 137.7 149 164 157 188 204 179 210 202 218 209
204 211 206 214 217 210 217 219 211 233 316 221 239
215 228 219 239 224 234 227 298 332 245 357 301 389
;
proc arima data= example2_2;
identify var=freq ;
run;
````

</details>

#### 例2.1 · SAS · 8d5286b4

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a92aefeae37123b98d9e30e744f0794416e3b27650ef4844150e95f4d739aec4`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.1.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=10cm hsize=10cm;
data a;
input  sha@@;
year=intnx('year','1jan1964'd,_n_-1);
format year year4.;
dif=dif(sha);
cards;
97 130 156.5 135.2 137.7 180.5 205.2 190 188.6 196.7
180.3 210.8 196 223 238.2 263.5 292.6 317 335.4 327
321.9 353.5 397.8 436.8 465.7 476.7 462.6 460.8
501.8 501.5 489.5 542.3 512.2 559.8 542 567
;
run;
proc gplot;
plot sha*year=1 dif*year=2;
symbol1 v=circle i=join c=black;
symbol2 v=star i=join c=red;
proc arima data=a;
identify var=sha nlag=22;
run;
````

</details>

#### 例2.2 · SAS · 690eaff6

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e7ee5e7e691eb67d7a89e1858d89e392823e3f78bcaba00a4a8a1ed2baf944ed`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input  milk@@;
time=intnx('month','1jan1962'd,_n_-1);
format time date.;
cards;
589   561   640   656   727   697   640   599
568   577   553   582   600   566   653   673
742   716   660   617   583   587   565   598
628   618   688   705   770   736   678   639
604   611   594   634   658   622   709   722
782   756   702   653   615   621   602   635
677   635   736   755   811   798   735   697
661   667   645   688   713   667   762   784
837   817   767   722   681   687   660   698
717   696   775   796   858   826   783   740
701   706   677   711   734   690   785   805
871   845   801   764   725   723   690   734
750   707   807   824   886   859   819   783
740   747   711   751   804   756   860   878
942   913   869   834   790   800   763   800
826   799   890   900   961   935   894   855
809   810   766   805   821   773   883   898
957   924   881   837   784   791   760   802
828   778   889   902   969   947   908   867
815   812   773   813   834   782   892   903
966   937   896   858   817   827   797   843
;
run;
proc gplot;
plot milk*time;
symbol v=square i=join c=red;
proc arima data=a;
identify var=milk nlag=22;
run;
````

</details>

#### 例2.3 · SAS · b6770e1a

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`53ba4700eddccb1eb80598060a38e54725e424b5ba8bb2bff51d7c153e0abb4e`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.3.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input  time hign;
cards;
1949	38.8
1950	35.6
1951	38.3
1952	39.6
1953	37.0
1954	33.4
1955	39.6
1956	34.6
1957	36.2
1958	37.6
1959	36.8
1960	38.1
1961	40.6
1962	37.1
1963	39.0
1964	37.5
1965	38.5
1966	37.5
1967	35.8
1968	40.1
1969	35.9
1970	35.3
1971	35.2
1972	39.5
1973	37.5
1974	35.8
1975	38.4
1976	35.0
1977	34.1
1978	37.5
1979	35.9
1980	35.1
1981	38.1
1982	37.3
1983	37.2
1984	36.1
1985	35.1
1986	38.5
1987	36.1
1988	38.1
1989	35.8
1990	37.5
1991	35.7
1992	37.5
1993	35.8
1994	37.2
1995	35.0
1996	36.0
1997	38.2
1998	37.2
;
run;
proc gplot;
plot hign*time;
symbol v=square i=join c=red;
proc arima data=a;
identify var=hign nlag=22;
run;
````

</details>

#### 例2.4 · SAS · b21a0312

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c41b4382e2cda15d3a3ba6e66d5c9ec505da39d95707e24d58a68cf3c7506f4d`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.4.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
do time=-50 to 1000 by 1;
noise=rannor(12345);
if time>0 then output;
end;
proc gplot;
plot noise*time;
symbol v=none i=join c=red;
proc arima data=a;
identify var=noise;
run;
````

</details>

#### 例2.5 · SAS · 2f5f258b

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8f768fbb252a39438177684bf56238bad0199d30815ba8c3c4e97afc6a9c42fa`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.5.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input year prop;
cards;
1950	83.5
1951	63.1
1952	71
1953	76.3
1954	70.5
1955	80.5
1956	73.6
1957	75.2
1958	69.1
1959	71.4
1960	73.6
1961	78.8
1962	84.4
1963	84.1
1964	83.3
1965	83.1
1966	81.6
1967	81.4
1968	84
1969	82.9
1970	83.5
1971	83.2
1972	82.2
1973	83.2
1974	83.5
1975	83.8
1976	84.5
1977	84.8
1978	83.9
1979	83.9
1980	81
1981	82.2
1982	82.7
1983	82.3
1984	80.9
1985	80.3
1986	81.3
1987	81.6
1988	83.4
1989	88.2
1990	89.6
1991	90.1
1992	88.2
1993	87
1994	87
1995	88.3
1996	87.8
1997	84.7
1998	80.2
;
proc gplot;
plot prop*year=1;
symbol1 v=diamond i=join c=red;
proc arima data=a;
identify var=prop;
estimate p=1 method=ml;
forecast id=year lead=5 out=out;
proc gplot data=out;
plot prop*year=2 forecast*year=3 l95*year=4 u95*year=4/overlay;
symbol2 v=star i=none c=black ;
symbol3 v=none i=join c=red w=2;
symbol4 v=none i=join c=green l=2 ;
run;
````

</details>

#### example5_1 · SAS · e9bb9d94

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`abe10bc1450201363fb21ed4e737ac642cff63514e6928703621afa807e9ea99`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/example5_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example5_1;
input x@@;
difx=dif(x);
t=_n_;
cards;
1.05 	-0.84 	-1.42 	0.20 	2.81 	6.72 	5.40 	4.38 
5.52 	4.46 	2.89 	-0.43 	-4.86 	-8.54 	-11.54 	-16.22 
-19.41 	-21.61 	-22.51 	-23.51 	-24.49 	-25.54 	-24.06 	-23.44 
-23.41 	-24.17 	-21.58 	-19.00 	-14.14 	-12.69 	-9.48 	-10.29 
-9.88 	-8.33 	-4.67 	-2.97 	-2.91 	-1.86 	-1.91 	-0.80 
;
proc gplot;
plot x*t difx*t;
symbol v=star c=black i=join;
proc arima;
identify var=x(1);
estimate p=1;
forecast lead=5 id=t out=out;
proc gplot data=out;
plot x*t=1 forecast*t=2 l95*t=3 u95*t=3/overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
symbol3 c=green I=join v=none;
run;
````

</details>

#### 例5.10 · SAS · 06859043

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`45fb5ceb4d84d71c9c803fb6001a1290c123763bccb613fd5da9d8f3ed12d30a`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.10.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input x@@;
dif1_12=dif12(dif(x));
time=intnx('month','1jan1948'd,_n_-1);
format time year4.;
cards;
446	650	592	561	491	592	604	635	580
510	553	554	628	708	629	724	820	865
1007	1025	955	889	965	878	1103	1092	978
823	827	928	838	720	756	658	838	684
779	754	794	681	658	644	622	588	720
670	746	616	646	678	552	560	578	514
541	576	522	530	564	442	520	484	538
454	404	424	432	458	556	506	633	708
1013	1031	1101	1061	1048	1005	987	1006	1075
854	1008	777	982	894	795	799	781	776
761	839	842	811	843	753	848	756	848
828	857	838	986	847	801	739	865	767
941	846	768	709	798	831	833	798	806
771	951	799	1156	1332	1276	1373	1325	1326
1314	1343	1225	1133	1075	1023	1266	1237	1180
1046	1010	1010	1046	985	971	1037	1026	947
1097	1018	1054	978	955	1067	1132	1092	1019
1110	1262	1174	1391	1533	1479	1411	1370	1486
1451	1309	1316	1319	1233	1113	1363	1245	1205
1084	1048	1131	1138	1271	1244	1139	1205	1030
1300	1319	1198	1147	1140	1216	1200	1271	1254
1203	1272	1073	1375	1400	1322	1214	1096	1198
1132	1193	1163	1120	1164	966	1154	1306	1123
1033	940	1151	1013	1105	1011	963	1040	838
1012	963	888	840	880	939	868	1001	956
966	896	843	1180	1103	1044	972	897	1103
1056	1055	1287	1231	1076	929	1105	1127	988
903	845	1020	994	1036	1050	977	956	818
1031	1061	964	967	867	1058	987	1119	1202
1097	994	840	1086	1238	1264	1171	1206	1303
1393	1463	1601	1495	1561	1404	1705	1739	1667
1599	1516	1625	1629	1809	1831	1665	1659	1457
1707	1607	1616	1522	1585	1657	1717	1789	1814
1698	1481	1330	1646	1596	1496	1386	1302	1524
1547	1632	1668	1421	1475	1396	1706	1715	1586
1477	1500	1648	1745	1856	2067	1856	2104	2061
2809	2783	2748	2642	2628	2714	2699	2776	2795
2673	2558	2394	2784	2751	2521	2372	2202	2469
2686	2815	2831	2661	2590	2383	2670	2771	2628
2381	2224	2556	2512	2690	2726	2493	2544	2232
2494	2315	2217	2100	2116	2319	2491	2432	2470
2191	2241	2117	2370	2392	2255	2077	2047	2255
2233	2539	2394	2341	2231	2171	2487	2449	2300
2387	2474	2667	2791	2904	2737	2849	2723	2613
2950	2825	2717	2593	2703	2836	2938	2975	3064
3092	3063	2991						

;
proc gplot;
plot x*time dif1_12*time;
symbol c=black i=join v=none;
proc arima;
identify var=x(1,12);
estimate p=1 q=(1)(12) noint;
forecast lead=0 id=time out=out;
proc gplot data=out;
plot x*time=1 forecast*time=2 /overlay;
symbol1 c=black i=none v=dot h=0.2;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例5.11 · SAS · 983295c0

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0a7e3a541d9a303c721f8b21cbfb1b1a92c8efde6608b10b696a3aa200a95627`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.11.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input returns@@;
dif=dif(returns);
r2=dif**2;
y=log(returns);
dify=dif(y);
time=intnx('month','1apr1963'd,_n_-1);
format time year4.;
cards;
0.00238	0.00238	0.00236	0.0025	0.00254	0.0026	0.00285	0.00281
0.00241	0.00288	0.00287	0.00292	0.00294	0.00273	0.00271	0.00282
0.00267	0.00273	0.00293	0.00285	0.00296	0.00281	0.00326	0.00321
0.00315	0.00319	0.00313	0.00313	0.00319	0.00313	0.0033	0.00319
0.00315	0.00355	0.0037	0.00371	0.00364	0.00381	0.00372	0.00368
0.00374	0.00389	0.00415	0.00389	0.00343	0.00377	0.00368	0.00364
0.00338	0.00283	0.00271	0.003	0.00309	0.00317	0.00343	0.00347
0.00355	0.0036	0.00398	0.00385	0.00389	0.00444	0.00453	0.00444
0.00432	0.00406	0.00432	0.00461	0.00398	0.005	0.00487	0.0047
0.00432	0.00508	0.00478	0.00508	0.00593	0.0055	0.00593	0.00542
0.0054	0.0054	0.00631	0.00534	0.00546	0.00542	0.00546	0.00495
0.005	0.00508	0.00483	0.00444	0.00377	0.00355	0.00338	0.00264
0.00283	0.00305	0.00338	0.00406				
;
proc gplot;
plot returns*time dif*time r2*time y*time dify*time;
symbol c=black i=join v=none;
proc arima;
identify var=returns ;
identify var=y(1);
estimate p=0 q=0 noint;
forecast lead=0 id=time  out=out;
data out;
merge a out;
by time;
estimate=exp(y);
proc gplot;
plot returns*time=1 estimate*time=2 /overlay;
symbol1 c=black i=none v=star h=0.5;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例5.6 · SAS · 0cb94755

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC AUTOREG`、`PROC GPLOT`、`PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6397f4ac81313250518c147676c252b4df0e65bd5d60e43aea3a3fd0c1414021`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC AUTOREG`, `PROC GPLOT`, `PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.6.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data na_in;
t=_n_;
time=intnx('year','1jan1952'd,_n_-1);
format time year4.;
input agric     indus   cons    trans   commer;
dif=dif(agric) ;
keep time agric dif;
cards;
100     100     100     100     100
101.6   133.6   138.1   12      133
103.3   159.1   133.3   136     136.4
111.5   169.1   152.4   140     137.5
116.5   219.1   261.9   164     146.6
120.1   244.5   242.9   176     146.6
120.3   383.5   367     270.8   155.9
100.6   501.5   388.6   356.5   170.3
83.6    541.4   394     383.6   164.1
84.7    315.9   129.5   221.1   130.1
88.7    267.4   161.9   171.5   117.7
98.9    300.7   205.1   176     120.8
111.9   374.9   259     198.6   123.9
122.9   477.7   286     261.7   128
131.9   598.5   313     297.8   155.9
134.2   504.3   296.8   239.2   164.1
131.6   458.6   237.5   225.6   151.8
132.2   622.3   323.8   284.3   179.6
139.8   863     421     343     199.2
142     979     468.3   370.8   201.2
140.5   1043.5  452.5   389.3   208
153.1   1134.3  457.8   412.5   224.5
159.2   1128.9  484.1   394     220.6
162.3   1297.3  542     444.9   220.6
159.1   1249.2  568.3   426.4   214.8
155.1   1434    578.8   491.3   242
161.2   1679.1  573.5   546.9   296.4
171.5   1814.7  584.1   560.8   316.8
168.4   2012.7  757.7   584     318.8
180.4   2046.8  770     607.2   379.4
201.6   2170.1  806.9   681.3   397.5
218.7   2383.7  954.3   755.5   449.1
247     2738.8  1056.7  852.8   499.5
253.7   3275.2  1310.6  1024.3  593.7
261.4   3590.6  1540    1140.2  636.3
273.2   4058.8  1744.8  1269.9  715
279.4   4765    1884    1413.6  760.8
;
proc print;
proc gplot;
plot agric*time=1 dif*time=1;
symbol1 c=red i=join v=square;
proc arima;
identify var=agric(1) stationarity=(adf) nlag=18;
estimate q=1;
forecast lead=10 id=time interval=year out=out;
proc print data=out;
proc gplot;
where time>='1jan1955'd;
plot agric*time=2 forecast*time=3 (l95 u95)*time=4/overlay;
symbol2 c=black i=none v=star;
symbol3 c=red i=join v=none;
symbol4 c=green i=join v=none l=3 w=1;
proc autoreg data=na_in;
model agric=t/nlag=2 method=ml dwprob;
output out=p p=a1 pm=a2 lcl=lcl ucl=ucl;
proc gplot data=p;
where time>='1jan1955'd;
plot agric*time=2 a1*time=3 lcl*time=4 ucl*time=4/overlay;
proc autoreg data=na_in;
model agric=dif/LAGDEP=DIF nlag=1 method=ml noint;
output out=p p=b1 pm=b2 lcl=lcl ucl=ucl;
proc gplot data=p;
where time>='1jan1955'd;
plot agric*time=2 b1*time=3 lcl*time=4 ucl*time=4/overlay;
run;
````

</details>

#### 例5.8 · SAS · 7f49d74b

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8cf212db6ccda7b3f65fe8873aeab79d7145a6222bddd62c3ae507b270f80fac`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.8.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data a;
input year x@@;
dif=dif(x);
cards;
1917	183.1
1918	183.9
1919	163.1
1920	179.5
1921	181.4
1922	173.4
1923	167.6
1924	177.4
1925	171.7
1926	170.1
1927	163.7
1928	151.9
1929	145.4
1930	145
1931	138.9
1932	131.5
1933	125.7
1934	129.5
1935	129.6
1936	129.5
1937	132.2
1938	134.1
1939	132.1
1940	137.4
1941	148.1
1942	174.1
1943	174.7
1944	156.7
1945	143.3
1946	189.7
1947	212
1948	200.4
1949	201.8
1950	200.7
1951	215.6
1952	222.5
1953	231.5
1954	237.9
1955	244
1956	259.4
1957	268.8
1958	264.3
1959	264.5
1960	268.1
1961	264
1962	252.8
1963	240
1964	229.1
1965	204.8
1966	193.3
1967	179
1968	178.1
1969	181.1
1970	165.6
1971	159.8
1972	136.1
1973	126.3
1974	123.3
1975	118.5
;
proc gplot;
plot x*year dif*year;
symbol c=black i=join v=square;
proc arima;
identify var=x(1);
estimate p=(1 4) noint;
forecast lead=5 id=year out=out;
proc gplot data=out;
plot x*year=1 forecast*year=2 l95*year=3 u95*year=3/overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
symbol3 c=green i=join v=none;
run;
````

</details>

#### 例5.9 · SAS · 94c5884f

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a2ca740bf2707bc669131dc724b574359e21b16ca2cfa6a5bf9561b5af5d8748`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.9.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data a;
input x@@;
dif1_4=dif4(dif(x));
time=intnx('quarter','1jan1962'd,_n_-1);
format time year4.;
cards;
1.1	0.5	0.4	0.7	1.6	0.6	0.5	0.7
1.3	0.6	0.5	0.7	1.2	0.5	0.4	0.6
0.9	0.5	0.5	1.1	2.9	2.1	1.7	2
2.7	1.3	0.9	1	1.6	0.6	0.5	0.7
1.1	0.5	0.5	0.6	1.2	0.7	0.7	1
1.5	1	0.9	1.1	1.5	1	1	1.6
2.6	2.1	2.3	3.6	5	4.5	4.5	4.9
5.7	4.3	4	4.4	5.2	4.3	4.2	4.5
5.2	4.1	3.9	4.1	4.8	3.5	3.4	3.5
4.2	3.4	3.6	4.3	5.5	4.8	5.4	6.5
8	7	7.4	8.5	10.1	8.9	8.8	9
10	8.7	8.8	8.9	10.4	8.9	8.9	9
10.2	8.6	8.4	8.4	9.9	8.5	8.6	8.7
9.8	8.6	8.4	8.2	8.8	7.6	7.5	7.6
8.1	7.1	6.9	6.6	6.8	6	6.2	6.2
;
proc gplot;
plot x*time dif1_4*time;
symbol c=black i=join v=star;
proc arima;
identify var=x(1,4);
estimate p=2 noint;
forecast lead=0 id=time out=out;
proc gplot data=out;
plot x*time=1 forecast*time=2 /overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例6.1 · SAS · 959a8745

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4dd48668e66f85fb7a8da39c911a5c592e4bd8bee8bd3a00cb75fee7911235c5`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第六章/例6.1.sas`

<details>
<summary>展开原始代码</summary>

````sas
 data b_j_seriesj;
   input x y @@;
   label x = 'Input Gas Rate'
         y = 'Output CO2';
		 t=_n_;
cards;
-0.109  53.8  0.000  53.6  0.178  53.5  0.339  53.5
 0.373  53.4  0.441  53.1  0.461  52.7  0.348  52.4
 0.127  52.2 -0.180  52.0 -0.588  52.0 -1.055  52.4
-1.421  53.0 -1.520  54.0 -1.302  54.9 -0.814  56.0
-0.475  56.8 -0.193  56.8  0.088  56.4  0.435  55.7
 0.771  55.0  0.866  54.3  0.875  53.2  0.891  52.3
 0.987  51.6  1.263  51.2  1.775  50.8  1.976  50.5
 1.934  50.0  1.866  49.2  1.832  48.4  1.767  47.9
 1.608  47.6  1.265  47.5  0.790  47.5  0.360  47.6
 0.115  48.1  0.088  49.0  0.331  50.0  0.645  51.1
 0.960  51.8  1.409  51.9  2.670  51.7  2.834  51.2
 2.812  50.0  2.483  48.3  1.929  47.0  1.485  45.8
 1.214  45.6  1.239  46.0  1.608  46.9  1.905  47.8
 2.023  48.2  1.815  48.3  0.535  47.9  0.122  47.2
 0.009  47.2  0.164  48.1  0.671  49.4  1.019  50.6
 1.146  51.5  1.155  51.6  1.112  51.2  1.121  50.5
 1.223  50.1  1.257  49.8  1.157  49.6  0.913  49.4
 0.620  49.3  0.255  49.2 -0.280  49.3 -1.080  49.7
-1.551  50.3 -1.799  51.3 -1.825  52.8 -1.456  54.4
-0.944  56.0 -0.570  56.9 -0.431  57.5 -0.577  57.3
-0.960  56.6 -1.616  56.0 -1.875  55.4 -1.891  55.4
-1.746  56.4 -1.474  57.2 -1.201  58.0 -0.927  58.4
-0.524  58.4  0.040  58.1  0.788  57.7  0.943  57.0
 0.930  56.0  1.006  54.7  1.137  53.2  1.198  52.1
 1.054  51.6  0.595  51.0 -0.080  50.5 -0.314  50.4
-0.288  51.0 -0.153  51.8 -0.109  52.4 -0.187  53.0
-0.255  53.4 -0.229  53.6 -0.007  53.7  0.254  53.8
 0.330  53.8  0.102  53.8 -0.423  53.3 -1.139  53.0
-2.275  52.9 -2.594  53.4 -2.716  54.6 -2.510  56.4
-1.790  58.0 -1.346  59.4 -1.081  60.2 -0.910  60.0
-0.876  59.4 -0.885  58.4 -0.800  57.6 -0.544  56.9
-0.416  56.4 -0.271  56.0  0.000  55.7  0.403  55.3
 0.841  55.0  1.285  54.4  1.607  53.7  1.746  52.8
 1.683  51.6  1.485  50.6  0.993  49.4  0.648  48.8
 0.577  48.5  0.577  48.7  0.632  49.2  0.747  49.8
 0.900  50.4  0.993  50.7  0.968  50.9  0.790  50.7
 0.399  50.5 -0.161  50.4 -0.553  50.2 -0.603  50.4
-0.424  51.2 -0.194  52.3 -0.049  53.2  0.060  53.9
 0.161  54.1  0.301  54.0  0.517  53.6  0.566  53.2
 0.560  53.0  0.573  52.8  0.592  52.3  0.671  51.9
 0.933  51.6  1.337  51.6  1.460  51.4  1.353  51.2
 0.772  50.7  0.218  50.0 -0.237  49.4 -0.714  49.3
-1.099  49.7 -1.269  50.6 -1.175  51.8 -0.676  53.0
 0.033  54.0  0.556  55.3  0.643  55.9  0.484  55.9
 0.109  54.6 -0.310  53.5 -0.697  52.4 -1.047  52.1
-1.218  52.3 -1.183  53.0 -0.873  53.8 -0.336  54.6
 0.063  55.4  0.084  55.9  0.000  55.9  0.001  55.2
 0.209  54.4  0.556  53.7  0.782  53.6  0.858  53.6
 0.918  53.2  0.862  52.5  0.416  52.0 -0.336  51.4
-0.959  51.0 -1.813  50.9 -2.378  52.4 -2.499  53.5
-2.473  55.6 -2.330  58.0 -2.053  59.5 -1.739  60.0
-1.261  60.4 -0.569  60.5 -0.137  60.2 -0.024  59.7
-0.050  59.0 -0.135  57.6 -0.276  56.4 -0.534  55.2
-0.871  54.5 -1.243  54.1 -1.439  54.1 -1.422  54.4
-1.175  55.5 -0.813  56.2 -0.634  57.0 -0.582  57.3
-0.625  57.4 -0.713  57.0 -0.848  56.4 -1.039  55.9
-1.346  55.5 -1.628  55.3 -1.619  55.2 -1.149  55.4
-0.488  56.0 -0.160  56.5 -0.007  57.1 -0.092  57.3
-0.620  56.8 -1.086  55.6 -1.525  55.0 -1.858  54.1
-2.029  54.3 -2.024  55.3 -1.961  56.4 -1.952  57.2
-1.794  57.8 -1.302  58.3 -1.030  58.6 -0.918  58.8
-0.798  58.8 -0.867  58.6 -1.047  58.0 -1.123  57.4
-0.876  57.0 -0.395  56.4  0.185  56.3  0.662  56.4
 0.709  56.4  0.605  56.0  0.501  55.2  0.603  54.0
 0.943  53.0  1.223  52.0  1.249  51.6  0.824  51.6
 0.102  51.1  0.025  50.4  0.382  50.0  0.922  50.0
 1.032  52.0  0.866  54.0  0.527  55.1  0.093  54.5
-0.458  52.8 -0.748  51.4 -0.947  50.8 -1.029  51.2
-0.928  52.0 -0.645  52.8 -0.424  53.8 -0.276  54.5
-0.158  54.9 -0.033  54.9  0.102  54.8  0.251  54.4
 0.280  53.7  0.000  53.3 -0.493  52.8 -0.759  52.6
-0.824  52.6 -0.740  53.0 -0.528  54.3 -0.204  56.0
 0.034  57.0  0.204  58.0  0.253  58.6  0.195  58.5
 0.131  58.3  0.017  57.8 -0.182  57.3 -0.262  57.0
;

proc arima data=b_j_seriesj;
identify var=x nlag=10;
estimate p=3;
identify var=y nalg=10;
estimate p=(1 2 4);
forecast lead=10 id=t out=out1;
identify var=y crosscorr=(x) nlag=10;
estimate input=( 3$ (1,2)/(1,2) x ) plot;
estimate p=2 input=( 3$ (1,2)/(1) x );
forecast lead=10 id=t out=out2;
proc gplot data=out1;
plot y*t=1 forecast1*t=2 /overlay;
proc gplot data=out2;
plot y*t=1 forecast2*t=2 /overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例6.2 · SAS · 69f74e3e

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`、`PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fbd199d2ec63c58b0bda11e9703bd7d6e4b7deaa378bb9a10a3fa6923f538650`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`, `PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第六章/例6.2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input year x y;
lnx=log(x);
lny=log(y);
cards;
1978	133.6	116.1
1979	160.7	134.5
1980	191.3	162.2
1981	223.4	190.8
1982	270.1	220.2
1983	309.8	248.3
1984	355.3	273.8
1985	397.6	317.4
1986	423.8	357
1987	462.6	398.3
1988	544.9	476.7
1989	601.5	535.4
1990	686.3	584.6
1991	708.6	619.8
1992	784	659.8
1993	921.6	769.7
1994	1221	1016.8
1995	1577.7	1310.4
1996	1926.1	1572.1
1997	2090.1	1617.2
1998	2162	1590.3
1999	2210.3	1577.4
2000	2253.4	1670.1
2001	2366.4	1741
2002	2476	1834
;
proc gplot data=a;
plot lnx*year=1 lny*year=2/overlay;
symbol1 c=black i=join v=circle;
symbol2 c=black i=join v=star;
proc arima data=a;
identify var=lnx stationarity=(adf);
identify var=lny stationarity=(adf);
identify var=lnx(1) stationarity=(adf);
identify var=lny(1) stationarity=(adf);
identify var=lnx(1) stationarity=(pp);
identify var=lny(1) stationarity=(pp);
proc reg;
model lny=lnx /noint;
output out=out residual=residual;
proc arima data=out;
identify var=residual stationarity=(adf);
proc arima data=a;
identify var=lny crosscorr=(lnx);
estimate p=1 input=lnx noint;
forecast lead=10 id=year out=result;
data result;
set result;
y=exp(lny);
estimate=exp(forecast);
proc gplot data=result;
plot lny*year=1 forecast*year=2 /overlay;
plot y*year=1 estimate*year=2 /overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
data b;
set a;
ecm=lny-0.96832*lnx;
lag_ecm=lag(ecm);
dif_lnx=dif(lnx);
dif_lny=dif(lny);
proc reg data=b;
model dif_lny=dif_lnx lag_ecm /noint;
run;
````

</details>

#### Pex18_6 · Python · c754bf31

- 归属算法：ARIMA时间序列
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#ARIMA时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于ARIMA时间序列中的“结果绘图与展示”。
- **执行主线**：识别并拟合时间序列滞后结构；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`2e263117c42c6348c0a0d0765d5029a3327ecd00963d3beb58553ff5765866c4`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_6.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_6.py
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import pylab as plt
from statsmodels.tsa.arima_model import ARIMA

plt.rc('axes',unicode_minus=False)
plt.rc('font',size=16); plt.rc('font',family='SimHei')
df=pd.read_csv('austa.csv')
plt.subplot(121); plt.plot(df.value.diff())
plt.title('一次差分')
ax2=plt.subplot(122)
plot_acf(df.value.diff().dropna(), ax=ax2,title='自相关')

md=ARIMA(df.value, order=(2,1,0))
mdf=md.fit(disp=0)
print(mdf.summary())

residuals = pd.DataFrame(mdf.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="残差", ax=ax[0])
residuals.plot(kind='kde', title='密度', ax=ax[1])
plt.legend(''); plt.ylabel('')          

mdf.plot_predict()  #原始数据与预测值对比图
plt.show()
````

</details>

### 回归分析 · 实现

#### anli10_3 · MATLAB · d93e5812

- 归属算法：回归分析
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“数据读取与预处理”。
- **执行主线**：识别并拟合时间序列滞后结构；估计回归系数并生成拟合/预测；执行归一化或标准化以统一变量尺度。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`1bbfd0789c6f1c872554d45ed2a397c863d40c11beccf407b5c2d7f064385123`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/10第10章/anli10_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
load ssgs.txt   %把原始数据保存在纯文本文件ssgs.txt中
n=size(ssgs,1);
x=ssgs(:,[1:4]); y=ssgs(:,5); %分别提出自变量x1...x4和因变量x的值
x=zscore(x); %数据标准化
r=corrcoef(x)  %求相关系数矩阵
[vec1,val,con1]=pcacov(r)  %进行主成分分析的相关计算
f1=repmat(sign(sum(vec1)),size(vec1,1),1);
vec2=vec1.*f1;     %特征向量正负号转换
f2=repmat(sqrt(val)',size(vec2,1),1); 
a=vec2.*f2   %求初等载荷矩阵
num=input('请选择主因子的个数：');  %交互式选择主因子的个数
am=a(:,[1:num]);  %提出num个主因子的载荷矩阵
[bm,t]=rotatefactors(am,'method', 'varimax') %am旋转变换,bm为旋转后的载荷阵
bt=[bm,a(:,[num+1:end])];  %旋转后全部因子的载荷矩阵,前两个旋转，后面不旋转
con2=sum(bt.^2)       %计算因子贡献
check=[con1,con2'/sum(con2)*100]%该语句是领会旋转意义,con1是未旋转前的贡献率
rate=con2(1:num)/sum(con2) %计算因子贡献率
coef=inv(r)*bm          %计算得分函数的系数
score=x*coef           %计算各个因子的得分
weight=rate/sum(rate)  %计算得分的权重
Tscore=score*weight'   %对各因子的得分进行加权求和，即求各企业综合得分
[STscore,ind]=sort(Tscore,'descend')      %对企业进行排序
display=[score(ind,:)';STscore';ind'] %显示排序结果
[ccoef,p]=corrcoef([Tscore,y])    %计算F与资产负债的相关系数
[d,dt,e,et,stats]=regress(Tscore,[ones(n,1),y]);%计算F与资产负债的方程
d,stats  %显示回归系数，和相关统计量的值
````

</details>

#### ex11_1 · MATLAB · 38df55de

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；执行归一化或标准化以统一变量尺度；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`1c93071ebb575734607bc5fac02817960d2e415029d7f34c2b7d1b75723201d4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/11第11章/ex11_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
ab0=load('pz.txt');   %原始数据存放在纯文本文件pz.txt中
mu=mean(ab0);sig=std(ab0); %求均值和标准差
rr=corrcoef(ab0);   %求相关系数矩阵
ab=zscore(ab0); %数据标准化
a=ab(:,[1:3]);b=ab(:,[4:end]);  %提出标准化后的自变量和因变量数据
[XL,YL,XS,YS,BETA,PCTVAR,MSE,stats] =plsregress(a,b)
xw=a\XS  %求自变量提出成分系数，每列对应一个成分，这里xw等于stats.W
yw=b\YS  %求因变量提出成分的系数
ncomp=input('请根据PCTVAR的值确定提出成分对的个数ncomp=');
[XL2,YL2,XS2,YS2,BETA2,PCTVAR2,MSE2,stats2] =plsregress(a,b,ncomp)
n=size(a,2); m=size(b,2);%n是自变量的个数,m是因变量的个数
beta3(1,:)=mu(n+1:end)-mu(1:n)./sig(1:n)*BETA2([2:end],:).*sig(n+1:end); %原始数据回归方程的常数项
beta3([2:n+1],:)=(1./sig(1:n))'*sig(n+1:end).*BETA2([2:end],:) %计算原始变量x1,...,xn的系数，每一列是一个回归方程
bar(BETA2','k')   %画直方图
yhat=repmat(beta3(1,:),[size(a,1),1])+ab0(:,[1:n])*beta3([2:end],:)  %求y1,..,ym的预测值
ymax=max([yhat;ab0(:,[n+1:end])]); %求预测值和观测值的最大值
%下面画y1,y2,y3的预测图，并画直线y=x
figure, subplot(2,2,1)
plot(yhat(:,1),ab0(:,n+1),'*',[0:ymax(1)],[0:ymax(1)],'Color','k')
legend('单杠成绩预测图',2)
subplot(2,2,2)
plot(yhat(:,2),ab0(:,n+2),'O',[0:ymax(2)],[0:ymax(2)],'Color','k')
legend('弯曲成绩预测图',2)
subplot(2,2,3)
plot(yhat(:,3),ab0(:,end),'H',[0:ymax(3)],[0:ymax(3)],'Color','k')
legend('跳高成绩预测图',2)
````

</details>

#### ex11_2 · MATLAB · d45a3024

- 归属算法：回归分析
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“数据读取与预处理”。
- **执行主线**：估计回归系数并生成拟合/预测；执行归一化或标准化以统一变量尺度。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`cd630a4d35f8d4c5937144302a084da0416946b6dccec8a23063ddce0e91cb50`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/11第11章/ex11_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear,format long g  %长小数的显示方式
ab0=load('you.txt');
mu=mean(ab0);sig=std(ab0); %求均值和标准差
ab=zscore(ab0); %数据标准化
a=ab(:,[1:7]);b=ab(:,[8:end]);
ncomp=2; %试着选择成分的对数
[XL,YL,XS,YS,BETA,PCTVAR,MSE,stats]=plsregress(a,b,ncomp)
n=size(a,2); m=size(b,2); %n是自变量的个数,m是因变量的个数
BETA2(1,:)=mu(n+1:end)-mu(1:n)./sig(1:n)*BETA([2:end],:).*sig(n+1:end); %原始数据回归方程的常数项
BETA2([2:n+1],:)=(1./sig(1:n))'*sig(n+1:end).*BETA([2:end],:) %计算原始变量x1,...,xn的系数，每一列是一个回归方程
format  %恢复到短小数的显示方式
````

</details>

#### huiguifenxi · MATLAB · 2a7f8f93

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`876c73bdf56c609cb520909f6a58b847db1858fa1015625149b332f3c50da2e4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/huiguifenxi.m`

<details>
<summary>展开原始代码</summary>

````matlab
% 一元回归
x=[1097  1284  1502  1394  1303  1555  1917  2051  2111  2286  2311  2003  2435  2625  2948  3, 55  3372];%因变量时间序列数据
y=[698  872  988  807  738  1025  1316  1539  1561  1765  1762  1960  1902  2013  2446  2736  2825];%自变量时间序列数据
X=[ones(size(x')),x'],pause    
[b,bint,r,rint,stats]=regress(y',X,0.05),pause%调用一元回归分析函数
rcoplot(r,rint)%画出在置信度区间下误差分布。

% 多元回归分析
% 输入各种因变量数据
x1=[5.5 2.5 8 3 3 2.9 8 9 4 6.5 5.5 5 6 5 3.5 8 6 4 7.5 7]';
x2=[31 55 67 50 38 71 30 56 42 73 60 44 50 39 55 70 40 50 62 59]';
x3=[10 8 12 7 8 12 12 5 8 5 11 12 6 10 10 6 11 11 9 9]';
x4=[8 6 9 16 15 17 8 10 4 16 7 12 6 4 4 14 6 8 13 11]';
%输入自变量数据
y=[79.3 200.1 163.1 200.1 146.0 177.7 30.9 291.9 160 339.4 159.6 86.3 237.5 107.2 155 201.4 100.2 135.8 223.3 195]';
X=[ones(size(x1)),x1,x2,x3,x4];
[b,bint,r,rint,stats]=regress(y,X)%回归分析
Q=r'*r
sigma=Q/18
rcoplot(r,rint);pause
X1=[x1,x2,x3,x4];
stepwise(X1,y,[1,2,3])%逐步回归
% X2=[ones(size(x1)),x2,x3];
% X3=[ones(size(x1)),x1,x2,x3];
% X4=[ones(size(x1)),x2,x3,x4];
% [b1,b1int,r1,r1int,stats1]=regress(y,X2)
% [b2,b2int,r2,r2int,stats2]=regress(y,X3);
% [b3,b3int,r3,r3int,stats3]=regress(y,X4);
````

</details>

#### yucezhixinqujian · MATLAB · 3cc4078e

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9e2a44fef40e199e1828c126eafd0302aed552c77a373bfecc2a7978a0811dd4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/yucezhixinqujian.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear 
x0=[ 1       8.55      470      300       10 
 2       3.79      285      80        10 
 3       4.82      470      300       120 
 4       0.02      470      80        120 
 5       2.75      470      80        10 
 6       14.39     100      190       10 
 7       2.54      100      80        65 
 8       4.35      470      190       65 
 9       13.00     100      300       54 
 10      8.50      100      300       120 
 11      0.05      100      80        120 
 12      11.32     285      300       10 
 13      3.13      285      190       120]; 
x=x0(:,3:5); 
y=x0(:,2); 
beta=[0.1,0.05,0.02,1,2]';  %回归系数的初值,可以任意取，这里是给定的 
[betahat,r,j]=nlinfit(x,y,@huaxue,beta);  %r,j是下面命令用的信息 
betaci=nlparci(betahat,r,'jacobian',j); 
betaa=[betahat,betaci]   %回归系数及其置信区间 
[yhat,delta]=nlpredci(@huaxue,x,betahat,r,'jacobian',j)  
%y的预测值及其置信区间的半径，置信区间为yhat±delta。 
nlintool(x,y,'huaxue',beta) 
````

</details>

#### ex14_7 · MATLAB · 9ef50e37

- 归属算法：回归分析
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“数据读取与预处理”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`5456443d49527c8369dce2743dbd1e008b6f2bb33eedee309321389c824a8b34`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/14第14章/ex14_7.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
aw=load('zhb.txt'); %把x1,...,x6的数据和权重数据保存在纯文本文件zhb.txt中
w=aw(end,:); %提取权重向量
a=aw([1:end-1],:); %提取指标数据
a(:,[2,6])=-a(:,[2,6]); %把成本型指标转换成效益型指标
ra=tiedrank(a) %对每个指标值分别编秩，即对a的每一列分别编秩
[n,m]=size(ra); %计算矩阵sa的维数
RSR=mean(ra,2)/n  %计算秩和比
W=repmat(w,[n,1]);
WRSR=m*mean(ra.*W,2)/n  %计算加权秩和比
p=[1:n]/n;    %计算累积频率
p(end)=1-1/(4*n) %修正最后一个累积频率，最后一个累积频率按1-1/(4*n)估计
Probit=norminv(p,0,1)+5  %计算标准正态分布的p分位数+5
X=[ones(n,1),Probit'];  %构造一元线性回归分析的数据矩阵
[ab,abint,r,rint,stats]=regress(WRSR,X)  %一元线性回归分析
WRSRfit=ab(1)+ab(2)*Probit  %计算WRNR的估计值
[sWRSRfit,ind]=sort(WRSRfit,'descend')  %对WRNR的估计值按照从大到小排序
````

</details>

#### ex15_6_1 · MATLAB · 6b9aaea6

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`bcdd57676fe4169596b5ba7b598639af37bdbb421024fc6cf2cb7e6890a7e263`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_6_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
ab=textread('zhu.txt');  %
y=ab(:,[2:5:10]); %提取因变量y的观测值
Y=nonzeros(y) %去掉y后面的0，并变成列向量
x123=[ab([1:13],[3:5]); ab([1:12],[8:10])]; %提取x1,x2,x3的观测值
X=[ones(25,1),x123]; %构造多元线性回归分析的数据矩阵X
[beta,betaint,r,rint,st]=regress(Y,X)  %计算回归系数和统计量等，st的第2个分量就是F统计量，下面根据统计量的表达式重新计算的结果和这里是一样的。
q=sum(r.^2)   %计算残差平方和
ybar=mean(Y)  %计算y的观测值的平均值
yhat=X*beta;   %计算y的估计值
u=sum((yhat-ybar).^2)   %计算回归平方和
m=3;    %变量的个数，拟合参数的个数为m+1
n=length(Y); %样本点的个数
F=u/m/(q/(n-m-1))   %计算F统计量的值,自由度为样本点的个数减拟合参数的个数
fw1=finv(0.025,m,n-m-1) %计算上alpha/2分位数
fw2=finv(0.975,m,n-m-1) %计算上1-alpha/2分位数
c=diag(inv(X'*X))   %计算c（j，j）的值
t=beta./sqrt(c)/sqrt(q/(n-m-1))  %计算t统计量的值
tfw=tinv(0.975,n-m-1)   %计算t分布的上alpha/2分位数
save xydata Y x123  %把Y和x123保存到mat文件xydata中，供问题（3）的二次模型使用
````

</details>

#### 相似实现组 · MATLAB · ec0ec91a

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：ex15_6_111.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ee4421421dad4bf8221206582d24bb2863d0972cd54ba6f0ac48387ff952ec8b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_6_111.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=[3.3	3.4	2.4	3.1	15	5.5	8.5	2.7	2.3	3.5	1.8	9.5	2.15	1.44	12	5.75	1.95	6.5	3.25	2.55	2.75	1.79	1.73	5	3.3	3.25	2.01	15	3.1	3.6	5	3.75	1.7	8	3.1	6.5	17	4.2	15	1.18	2.45	1.4	3.75	2.5	3.75	1.33	1.45	1.57	5.5	7	1.45	1.33	1.55	3.3	3	1.8	1.67	1.67	3.1	3.75	3	2	1.57	1.5
3.4	3.3	3.3	3.4	9	3.8	4.75	3.3	2.9	4.2	3.9	4	3.6	4.2	7	3.8	3.6	3.6	3.6	3.1	3.4	3.86	3.6	4.2	3.43	3.4	3.45	8	3.5	3.8	3.8	3.4	3.5	4.5	3.2	4	8.5	3.75	7	7	3.25	4.5	3.6	3.25	3.3	4.75	4.75	4	3.6	4.5	4	5.25	4	3.3	3.25	3.6	4	4	3.75	3.3	3.5	3.5	4	4.33
2.15	2.15	2.88	2.25	1.12	1.62	1.36	2.55	3.5	1.85	4	1.4	3.1	7.5	1.2	1.6	3.6	1.57	2.1	2.9	2.5	4.82	4.75	1.62	2.33	2.15	4.23	1.14	2.2	1.91	1.65	2	4.5	1.4	2.3	1.53	1.13	1.8	1.17	13	2.88	7.5	1.95	2.8	2	10	6	5.5	1.65	1.36	8	8	6	2.2	2.38	4.33	4.75	4.75	2.1	2	2.2	3.6	5.5	6];
y=[0.33 	0.50 	1.33 	0.67 	0.33 	0.00 	0.20 	2.00 	0.00 	5.00 	1.00 	0.33 	1.50 	1.00 	0.40 	0.33 	0.5	0.33	2	0.5	2	1	0	0.333333333	0	1	2	0.5	1	0.33	3	1	2	0.2	0	1	0	0.5	0	2	1	3	0	0	0.2	4	1	2	0	0	1	0.5	1	0.667	0.33	2	1	5	1	1	1	0	0.25	1.33];
n=64;
X=[ones(n,1),x'];
[b,bint,r,rint,s]=regress(y',X);
b,bint,s,
rcoplot(r,rint)
````

</details>

##### 变体 2：ex15_99.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`520bb114cb289efdf4a642588c8f7d7e33d2aa591b05a9cf93066f97715e4d2b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_99.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=[1.189189189	1.247706422	0.776699029	1.097345133	2.964426877	2.029520295	2.782324059	0.923076923	0.71875	1.157024793	0.455696203	3.518518519	0.641791045	0.246153846	2.926829268	2.12962963	0.541666667	2.51450677	1.140350877	0.85	0.93220339	0.412442396	0.414371257	1.718213058	1.145833333	1.171171171	0.5234375	3.282275711	1.087719298	1.260945709	1.834862385	1.25	0.207407407	1.388888889	0.425	2.711864407	1.127272727	2.350813743	3.530633437	1.513513514	3.671970624	0.118	0.076	0.799347471	0.233333333	1.351351351	1.056338028	0.826446281	1.41509434	0.180338983	0.269767442	0.330526316	2.095238095	0.0925	2.389078498	0.241666667	0.200754717	0.31	0.034	0.130133333	1.2	0.98245614	1.065719361	0.407058824	0.453972257	0.381714286	0.381714286	1.05982906	1.41509434	0.463291139	1.052631579	0.322051282	0.2176	0.563380282	0.330526316	0.290416263];
y=[0.33 	0.50 	1.33 	0.67 	0.33 	0.00 	0.20 	2.00 	0.00 	5.00 	1.00 	0.33 	1.50 	1.00 	0.40 	0.33 	0.5	0.33	2	0.5	2	1	0	0.333333333	0	1	2	0.5	1	0.33	3	10	10	1	2	0.2	0	1	0	0.5	0	2	10	1	3	0	10	0	0.2	4	1	2	0	10	0	1	0.5	1	10	20	0.667	10	0.33	10	2	1	5	1	1	10	1	10	10	0	0.25	1.33];
n=76 ;
X=[ones(n,1),x'];
[b,bint,r,rint,s]=regress(y',X);
b,bint,s,
rcoplot(r,rint)
````

</details>

#### ex15_7 · MATLAB · 6854b0ff

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`45f171956007e5ba9a78319790f0d792860963bdf01b4bf54913f5e893aee21b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_7.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
xy0=[8.55	470	300	10
3.79	285	80	10
4.82	470	300	120
0.02	470	80	120
2.75	470	80	10
14.39	100	190	10
2.54	100	80	65
4.35	470	190	65
13.00	100	300	54
8.50	100	300	120
0.05	100	80	120
11.32	285	300	10
3.13	285	190	120];
x=xy0(:,[2:4]);
y=xy0(:,1);
huaxue=@(beta,x) (beta(4)*x(:,2)-x(:,3)/beta(5))./(1+beta(1)*x(:,1)+beta(2)*x(:,2)+beta(3)*x(:,3)); %用匿名函数定义要拟合的函数
beta0=[0.1,0.05,0.02,1,2]';  %回归系数的初值,可以任意取，这里是给定的
[beta,r,j]=nlinfit(x,y,huaxue,beta0)  %计算回归系数beta; r,j是下面命令用的信息
betaci=nlparci(beta,r,'jacobian',j)  %计算回归系数的置信区间
[yhat,delta]=nlpredci(huaxue,x,beta,r,'jacobian',j) %计算y的预测值及置信区间半径，
````

</details>

#### 第3章例题程序 · SAS · 7d1a3235

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“预测与推断”。
- **执行主线**：执行选择、交叉和变异的进化搜索；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC CAPABILITY`、`PROC CORR`、`PROC GCHART`、`PROC GPLOT`、`PROC PLOT`、`PROC PRINT`、`PROC REG`、`PROC SORT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cc2f3747429ca02959fd4dc285fe6369a1877927e3465a823444ef86ccca1a42`
- 语言：SAS
- 符号：`PROC CAPABILITY`, `PROC CORR`, `PROC GCHART`, `PROC GPLOT`, `PROC PLOT`, `PROC PRINT`, `PROC REG`, `PROC SORT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/00预备知识 SAS软件简介/第3章例题程序.txt`

<details>
<summary>展开原始代码</summary>

````sas
例3.1
data sell;
input y x1 x2;
cards;
162 274 2450
120 180 3254
223 375 3802
131 205 2838
67 86 2347
169 265 3782
81 98 3008
192 330 2450
116 195 2137
55 53 2560
252 430 4020
232 372 4427
144 236 2660
103 157 2088
212 370 2605
;
proc plot data=sell;
plot y*(x1 x2);   /*plot y*x1='1' y*x2='2'/overlay;*/
run;
proc corr data=sell;
var y x1 x2;
run;
proc reg data=sell;
model y=x1 x2/p r cli clm ;   /*model y=x1 x2/vif 可计算自变量的方差膨胀因子，越大共线性越大*/
output out=sell1 p=p L95M=xiaxian U95M=shangxian H=touying r=r student=stdr ;
proc print data=sell1;
run;

下面画出拟合值与残差的散点图。
proc reg data=sell;
model y=x1 x2/all ;   /*model y=x1 x2/vif collin colinoint vif 可计算自变量的方差膨胀因子，越大共线性越大*/
plot residual. *(predicted. obs. x1 x2);
run;

例3.3
data new;
set sell1;
keep r;
run;
proc sort data=new;
by r;
run;

data new1;
i=1;
do until (i=16);
q=sqrt(4.7403)*probit((i-0.375)/(15+0.25));
output;
i=i+1;
end;
run;
data new2;
merge new1 new;
run;
proc print data=new2;
run;
proc plot;
plot r*q;
run;

proc corr data=new2;   /*计算相关系数*/
var r q;
run;

可以使用前面的capability过程作qq图
proc capability graphics data=sell1;
qqplot r/normal;
run;





例3.4
data survival;
input x1-x4 y;
y1=log10(y);
cards;
6.7 62 81 2.59 200 
5.1 59 66 1.70 101
7.4 57 83 2.16 204 
6.5 73 41 2.01 101
7.8 65 115 4.30 509
5.8 38 72 1.42 80
5.7 46 63 1.91 80
3.7 68 81 2.57 127 
6.0 67 93 2.50 202
3.7 76 94 2.4 203
6.3 84 83 4.13 329 
6.7 51 43 4.86 65 
5.8 96 114 3.95 830
5.8 83 88 3.95 330
7.7 62 67 3.4 168
7.4 74 68 2.40 217
6.0 85 28 2.98 87
3.7 51 41 1.55 34
7.3 68 74 3.56 215
5.6 57 87 3.02 172
5.2 52 76 2.85 109
3.4 83 53 1.12 136
6.7 26 68 2.10 70
5.8 67 86 3.40 220
6.3 59 100 2.95 276
5.8 61 73 3.50 144
5.2 52 86 2.45 181 
11.2 76 90 5.59 574
5.2 54 56 2.71 72 
5.8 76 59 2.58 178
3.2 64 65 0.74 71 
8.7 45 23 2.52 58
5.0 59 73 3.50 116
5.8 72 93 3.30 295
5.4 58 70 2.64 115
5.3 51 99 2.60 184
2.6 74 86 2.05 118
4.3 8 119 2.85 120
4.8 61 76 2.54 151
5.4 52 88 1.81 148
5.2 49 72 1.84 95 
3.6 28 99 1.30 75
8.8 86 88 6.40 483
6.5 56 77 2.85 153
3.4 77 93 1.48 191
6.5 40 84 3.00 123
4.5 73 106 3.05 311 
4.8 86 101 4.10 398
5.1 67 77 2.86 158
3.9 82 103 4.55 310
6.6 77 46 1.95 124
6.4 85 40 1.21 125
6.4 59 85 2.33 198
8.8 78 72 3.20 313
;
proc reg data=survival;/*变换前残差正态QQ图*/
model y=x1-x4;   
output out=survival1 p=p r=r student=stdr;
proc print data=survival1;
run;
proc capability graphics;
qqplot r;
run;

proc reg data=survival; /*变换后残差正态QQ图*/
model y1=x1-x4;  
output out=survival1 p=p r=r student=stdr;
proc print data=survival1;
run;
proc capability graphics;
qqplot r;
run;

proc reg data=survival; /*RP2值决定*/
model y1=x1-x4/selection=Rsquare details;  
run;
proc reg data=survival; /*RA2值决定*/
model y1=x1-x4/selection=adjrsq details;  
run;
proc reg data=survival; /*cp值决定*/
model y1=x1-x4/selection=cp details;  
run;


例五
proc reg data=survival;
model y1=x1-x4/selection=stepwise slentry=0.05 slstay=0.05 details;
run;

补充实例

title ' "应用多元统计分析"  p128:例4.2.1';
/*----yydy421.sas  */


data d411;
  input x1-x4 y ;
  cards;
7  26  6 60  78.5
1  29 15 52  74.3
11 56  8 20 104.3
11 31  8 47  87.6
7  52  6 33  95.9
11 55  9 22 109.2
3  71 17  6 102.7
1  31 22 44  72.5
2  54 18 22  93.1
21 47  4 26 115.9
1  40 23 34  83.8
11 66  9 12 113.3
10 68  8 12 109.4
;

proc reg data=d411;
   model y=x1-x4 / selection=stepwise
                   sle=0.10 sls=0.10 details; 
run;
quit;

title ' "应用多元统计分析"  p128-P130:例4.2.2';
/*----yydy422.sas  */


data d411;
  input x1-x4 y ;
  cards;
7  26  6 60  78.5
1  29 15 52  74.3
11 56  8 20 104.3
11 31  8 47  87.6
7  52  6 33  95.9
11 55  9 22 109.2
3  71 17  6 102.7
1  31 22 44  72.5
2  54 18 22  93.1
21 47  4 26 115.9
1  40 23 34  83.8
11 66  9 12 113.3
10 68  8 12 109.4
;

proc reg data=d411;
   model y=x1-x4 / selection=rsquare 
                   b adjrsq cp aic mse sbc; 
run;

quit;
/*说明回归子集中几种最优准则的统计量，其中R-Square增加最快的好； Adjusted-R-Square越大越好，Cp值越接近P值越好，AIC、SBC、MSE越小越好*/



应用实例
data shiyan;
input x y @@;
cards;
170 45 173 42 160 44 155 41 173 47 168 50 178 47 183 46 180 49 165 43
;
proc gplot data=shiyan;
plot y*x/ctext=blue;
symbol value=diamond color=red width=2;
run;

proc gchart data=shiyan;
hbar x;
pie x;
run;
````

</details>

#### ch24_xian_xing_hui_gui · SAS · 48288065

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`5e1970e60bbd08f8416d9b4992a28e11d6bf81eaf07bb94e00e9176f13995053`
- 语言：SAS
- 符号：`PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch24_xian_xing_hui_gui.sas`

<details>
<summary>展开原始代码</summary>

````sas
data hits;
infile 'c:\MyRawData\Baseball.dat';
input Height Distance @@;
run;
proc reg data = hits PLOTS(ONLY) = (DIAGNOSTICS FITPLOT);
model Distance = Height /r clm cli dw;
title 'Results of Regression Analysis';
run;
````

</details>

#### ch25_duo_yuan_xian_xing_hui_gui · SAS · e4f5df20

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC CORR`、`PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`95ad37540b770261ff6de0a53de6a03630ada7970996d648bfdebb3e29a369e3`
- 语言：SAS
- 符号：`PROC CORR`, `PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch25_duo_yuan_xian_xing_hui_gui.sas`

<details>
<summary>展开原始代码</summary>

````sas
data fitness ;
input age weight oxygen runtime rstpulse runpulse maxpulse;
datalines; 
44	89.47	44.609	11.37	62	178	182
40	75.07	45.313	10.07	62	185	185
44	85.84	54.297	8.65	45	156	168
42	68.15	59.571	8.17	40	166	172
38	89.02	49.874	9.22	55	178	180
47	77.45	44.811	11.63	58	176	176
40	75.98	45.681	11.95	70	176	180
43	81.19	49.091	10.85	64	162	170
44	81.42	39.442	13.08	63	174	176
38	81.87	60.055	8.63	48	170	186
44	73.03	50.541	10.13	45	168	168
45	87.66	37.388	14.03	56	186	192
45	66.45	44.754	11.12	51	176	176
47	79.15	47.273	10.60	47	162	164
54	83.12	51.855	10.33	50	166	170
49	81.42	49.156	8.95	44	180	185
51	69.63	40.836	10.95	57	168	172
51	77.91	46.672	10.00	48	162	168
48	91.63	46.774	10.25	48	162	164
49	73.37	50.388	10.08	76	168	168
57	73.37	39.407	12.63	58	174	176
54	79.38	46.080	11.17	62	156	165
52	76.32	45.441	9.63	48	164	166
50	70.87	54.625	8.92	48	146	155
51	67.25	45.118	11.08	48	172	172
54	91.63	39.203	12.88	44	168	172
51	73.71	45.790	10.47	59	186	188
57	59.08	50.545	9.93	49	148	155
49	76.32	48.673	9.40	56	186	188
48	61.24	47.920	11.50	52	170	176
52	82.78	47.467	10.50	53	170	172
;
run;
proc corr data = fitness PLOT = MATRIX(HISTOGRAM nvar=all);
var oxygen age weight runtime rstpulse runpulse maxpulse;
label   oxygen  = 'Oxygen consumption'
            age = 'Age in years'  
        weight  = 'weight in kg'  
        runtime = 'Min. to run 1.5 miles'
       rstpulse = 'Heart rate while resting'
       runpulse = 'Heart rate while running'
       maxpulse = 'Maximum heart rate';
run;
proc reg data = fitness PLOTS(ONLY) = (DIAGNOSTICS FITPLOT);
model oxygen = age maxpulse rstpulse runpulse runtime weight/ss1 ss2; /* ss1为第Ⅰ类型平方和， ss2为第Ⅱ类型平方和 */
run;
delete rstpulse;
print;
run;
proc reg data= fitness;
model oxygen = age maxpulse runpulse runtime weight;
pulse: test maxpulse+runpulse=0;
run;
proc reg data= fitness;
model oxygen = age maxpulse runpulse runtime weight/ss2;  /* 带restrict约束条件的回归，ss1不可用 */
restrict maxpulse+runpulse=0;
run;
data fitness2;
set fitness;
maxrun=maxpulse-runpulse;
run;
proc reg data= fitness2;
model oxygen = age maxrun runtime weight/ss1 ss2;
run;
````

</details>

#### 相似实现组 · SAS · 4962da93

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：ch26_zhu_bu_hui_gui.sas

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7ebaba253d3e04c76417ed655a360c7a2c560ebced336f7ec58bf04db2d3e5c2`
- 语言：SAS
- 符号：`PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch26_zhu_bu_hui_gui.sas`

<details>
<summary>展开原始代码</summary>

````sas
data fitness ;
input age weight oxygen runtime rstpulse runpulse maxpulse;
datalines; 
44	89.47	44.609	11.37	62	178	182
40	75.07	45.313	10.07	62	185	185
44	85.84	54.297	8.65	45	156	168
42	68.15	59.571	8.17	40	166	172
38	89.02	49.874	9.22	55	178	180
47	77.45	44.811	11.63	58	176	176
40	75.98	45.681	11.95	70	176	180
43	81.19	49.091	10.85	64	162	170
44	81.42	39.442	13.08	63	174	176
38	81.87	60.055	8.63	48	170	186
44	73.03	50.541	10.13	45	168	168
45	87.66	37.388	14.03	56	186	192
45	66.45	44.754	11.12	51	176	176
47	79.15	47.273	10.60	47	162	164
54	83.12	51.855	10.33	50	166	170
49	81.42	49.156	8.95	44	180	185
51	69.63	40.836	10.95	57	168	172
51	77.91	46.672	10.00	48	162	168
48	91.63	46.774	10.25	48	162	164
49	73.37	50.388	10.08	76	168	168
57	73.37	39.407	12.63	58	174	176
54	79.38	46.080	11.17	62	156	165
52	76.32	45.441	9.63	48	164	166
50	70.87	54.625	8.92	48	146	155
51	67.25	45.118	11.08	48	172	172
54	91.63	39.203	12.88	44	168	172
51	73.71	45.790	10.47	59	186	188
57	59.08	50.545	9.93	49	148	155
49	76.32	48.673	9.40	56	186	188
48	61.24	47.920	11.50	52	170	176
52	82.78	47.467	10.50	53	170	172
;
run;
data fitness2;
set fitness;
maxrun=maxpulse-runpulse;
run;
proc reg data= fitness2;
model oxygen = age weight rstpulse maxrun runtime /selection=stepwise  ;
run;
````

</details>

##### 变体 2：ch26_zhu_bu_hui_gui0.sas

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`20a923bdbef370b9a25ca34b04d346774cc70c49e56404a64ba440762488d9cc`
- 语言：SAS
- 符号：`PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch26_zhu_bu_hui_gui0.sas`

<details>
<summary>展开原始代码</summary>

````sas
data fitness ;
input age weight oxygen runtime rstpulse runpulse maxpulse;
datalines; 
44	89.47	44.609	11.37	62	178	182
40	75.07	45.313	10.07	62	185	185
44	85.84	54.297	8.65	45	156	168
42	68.15	59.571	8.17	40	166	172
38	89.02	49.874	9.22	55	178	180
47	77.45	44.811	11.63	58	176	176
40	75.98	45.681	11.95	70	176	180
43	81.19	49.091	10.85	64	162	170
44	81.42	39.442	13.08	63	174	176
38	81.87	60.055	8.63	48	170	186
44	73.03	50.541	10.13	45	168	168
45	87.66	37.388	14.03	56	186	192
45	66.45	44.754	11.12	51	176	176
47	79.15	47.273	10.60	47	162	164
54	83.12	51.855	10.33	50	166	170
49	81.42	49.156	8.95	44	180	185
51	69.63	40.836	10.95	57	168	172
51	77.91	46.672	10.00	48	162	168
48	91.63	46.774	10.25	48	162	164
49	73.37	50.388	10.08	76	168	168
57	73.37	39.407	12.63	58	174	176
54	79.38	46.080	11.17	62	156	165
52	76.32	45.441	9.63	48	164	166
50	70.87	54.625	8.92	48	146	155
51	67.25	45.118	11.08	48	172	172
54	91.63	39.203	12.88	44	168	172
51	73.71	45.790	10.47	59	186	188
57	59.08	50.545	9.93	49	148	155
49	76.32	48.673	9.40	56	186	188
48	61.24	47.920	11.50	52	170	176
52	82.78	47.467	10.50	53	170	172
;
run;
proc reg data= fitness;
model oxygen = age weight rstpulse maxpulse runpulse runtime /selection=stepwise  ;
run;
````

</details>

#### ch26_zhu_bu_hui_gui_cp · SAS · 2efeba46

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`159e40d8acee052082e231393c7cef9ffcbc43cbfa8c59a99d36b4d9ff18c596`
- 语言：SAS
- 符号：`PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch26_zhu_bu_hui_gui_cp.sas`

<details>
<summary>展开原始代码</summary>

````sas
data fitness;
input age weight oxygen runtime rstpulse runpulse maxpulse;
datalines; 
44	89.47	44.609	11.37	62	178	182
40	75.07	45.313	10.07	62	185	185
44	85.84	54.297	8.65	45	156	168
42	68.15	59.571	8.17	40	166	172
38	89.02	49.874	9.22	55	178	180
47	77.45	44.811	11.63	58	176	176
40	75.98	45.681	11.95	70	176	180
43	81.19	49.091	10.85	64	162	170
44	81.42	39.442	13.08	63	174	176
38	81.87	60.055	8.63	48	170	186
44	73.03	50.541	10.13	45	168	168
45	87.66	37.388	14.03	56	186	192
45	66.45	44.754	11.12	51	176	176
47	79.15	47.273	10.60	47	162	164
54	83.12	51.855	10.33	50	166	170
49	81.42	49.156	8.95	44	180	185
51	69.63	40.836	10.95	57	168	172
51	77.91	46.672	10.00	48	162	168
48	91.63	46.774	10.25	48	162	164
49	73.37	50.388	10.08	76	168	168
57	73.37	39.407	12.63	58	174	176
54	79.38	46.080	11.17	62	156	165
52	76.32	45.441	9.63	48	164	166
50	70.87	54.625	8.92	48	146	155
51	67.25	45.118	11.08	48	172	172
54	91.63	39.203	12.88	44	168	172
51	73.71	45.790	10.47	59	186	188
57	59.08	50.545	9.93	49	148	155
49	76.32	48.673	9.40	56	186	188
48	61.24	47.920	11.50	52	170	176
52	82.78	47.467	10.50	53	170	172
;
run;
goptions reset=global gunit=pct cback=white border
        htitle=6 htext=3 ftext=swissb colors=(back);
title 'Cp plot with Reference Lines';
proc reg data= fitness;
model oxygen = age weight rstpulse maxpulse runpulse runtime /selection=cp adjrsq  best=5 ;
plot cp. * np. /chocking=red cmallows=blue vaxis=0 to 15 by 2 haxis=0 to  8 by 1;
run;
````

</details>

#### ch26_zhu_bu_hui_gui_rsuare · SAS · b857b0ed

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a63c3a9c1725921788346130f68e2b6f41c4b0542bb8923bb204f2c4160c4500`
- 语言：SAS
- 符号：`PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch26_zhu_bu_hui_gui_rsuare.sas`

<details>
<summary>展开原始代码</summary>

````sas
data fitness;
input age weight oxygen runtime rstpulse runpulse maxpulse;
datalines; 
44	89.47	44.609	11.37	62	178	182
40	75.07	45.313	10.07	62	185	185
44	85.84	54.297	8.65	45	156	168
42	68.15	59.571	8.17	40	166	172
38	89.02	49.874	9.22	55	178	180
47	77.45	44.811	11.63	58	176	176
40	75.98	45.681	11.95	70	176	180
43	81.19	49.091	10.85	64	162	170
44	81.42	39.442	13.08	63	174	176
38	81.87	60.055	8.63	48	170	186
44	73.03	50.541	10.13	45	168	168
45	87.66	37.388	14.03	56	186	192
45	66.45	44.754	11.12	51	176	176
47	79.15	47.273	10.60	47	162	164
54	83.12	51.855	10.33	50	166	170
49	81.42	49.156	8.95	44	180	185
51	69.63	40.836	10.95	57	168	172
51	77.91	46.672	10.00	48	162	168
48	91.63	46.774	10.25	48	162	164
49	73.37	50.388	10.08	76	168	168
57	73.37	39.407	12.63	58	174	176
54	79.38	46.080	11.17	62	156	165
52	76.32	45.441	9.63	48	164	166
50	70.87	54.625	8.92	48	146	155
51	67.25	45.118	11.08	48	172	172
54	91.63	39.203	12.88	44	168	172
51	73.71	45.790	10.47	59	186	188
57	59.08	50.545	9.93	49	148	155
49	76.32	48.673	9.40	56	186	188
48	61.24	47.920	11.50	52	170	176
52	82.78	47.467	10.50	53	170	172
;
run;
proc reg data= fitness;
model oxygen = age weight rstpulse maxpulse runpulse runtime /selection= rsquare b best=2;
*选项 b 输出各回归系数，best=2只输出R方最大的两种情况;
run;
````

</details>

#### ch27_fei_xian_xing_hui_gui1 · SAS · cb48d5ff

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC CORR`、`PROC GPLOT`、`PROC REG`、`PROC SGPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e0f8c351c8dca545e99388f552559bf3bce3b7fbc7ec195e17973e523e4581b3`
- 语言：SAS
- 符号：`PROC CORR`, `PROC GPLOT`, `PROC REG`, `PROC SGPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch27_fei_xian_xing_hui_gui1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data exam25_1;
input x y;
cards;
1.1  109.95
1.2  40.45
1.3  20.09
1.4  24.53
1.5  11.02
1.6  7.39
1.7  4.95
1.8  2.72
1.9  1.82
2  1.49
2.1  0.82
2.2  0.3
2.3  0.2
2.4  0.22
;
run;
proc sgplot data = exam25_1;
scatter x = x  y = y;
run;
proc corr data = exam25_1;
var x y;
run;
data new1;
set exam25_1;
v = log(y);
run;
proc sgplot data = new1;
scatter x = x  y = v;
title '变量代换后数据';
run;
proc reg data = new1; 
var x v;
model v = x; 
print cli; 
title '残差图';
plot residual. * predicted.;
run; 
data new2; 
set exam25_1;
y1 = 14530.28*exp(-4.73895*x); 
run; 
proc gplot data = new2; 
plot y*x=1 y1*x=2 /overlay; 
symbol v=dot i=none cv=red; 
symbol2 i=sm color=blue;
title '指数回归图';
run;
````

</details>

#### ch27_fei_xian_xing_hui_gui2 · SAS · c461f49c

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC GLM`、`PROC REG`、`PROC SGPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`82e3bfdc3fd1ed794e564069560cd68ca02e71ebb27d3f09b27348a31978a325`
- 语言：SAS
- 符号：`PROC GLM`, `PROC REG`, `PROC SGPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch27_fei_xian_xing_hui_gui2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data exam25_2;
input x1 y @@; 
x2=x1*x1; 
datalines;  
1 3833.43 
7 3476.76 
2 3811.58 
8 3466.22 
3 3769.47 
9 3395.42 
4 3565.74 
10 3807.08 
5 3481.99 
11 3817.03 
6 3372.82 
12 3884.52 
;  
run;
proc sgplot data = exam25_2; 
scatter x = x1 y = y;
title '原始数据散点图';
run; 
proc reg data = exam25_2; 
model y=x1 x2; 
run; 






  

proc reg;model y=x1 x2 x3/ss1 ss2; run; 






  






proc reg;model y=x1-x5/selection=backward sls=0.05; run; 






proc glm; model y=x1 x1*x1; 

run; 
````

</details>

#### ch28_Logistic_1 · SAS · 070eaf82

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“预测与推断”。
- **执行主线**：执行选择、交叉和变异的进化搜索；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC LOGISTIC`、`PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ac88325c16eff7280c54cb498c8c82fcb1f9f45aada81ddedc299c02c1c95111`
- 语言：SAS
- 符号：`PROC LOGISTIC`, `PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch28_Logistic_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data Remission;
   input remiss cell smear infil li blast temp;
   label remiss='Complete Remission';
   datalines;
1   .8   .83  .66  1.9  1.1     .996
1   .9   .36  .32  1.4   .74    .992
0   .8   .88  .7    .8   .176   .982
0  1     .87  .87   .7  1.053   .986
1   .9   .75  .68  1.3   .519   .98
0  1     .65  .65   .6   .519   .982
1   .95  .97  .92  1    1.23    .992
0   .95  .87  .83  1.9  1.354  1.02
0  1     .45  .45   .8   .322   .999
0   .95  .36  .34   .5  0      1.038
0   .85  .39  .33   .7   .279   .988
0   .7   .76  .53  1.2   .146   .982
0   .8   .46  .37   .4   .38   1.006
0   .2   .39  .08   .8   .114   .99
0  1     .9   .9   1.1  1.037   .99
1  1     .84  .84  1.9  2.064  1.02
0   .65  .42  .27   .5   .114  1.014
0  1     .75  .75  1    1.322  1.004
0   .5   .44  .22   .6   .114   .99
1  1     .63  .63  1.1  1.072   .986
0  1     .33  .33   .4   .176  1.01
0   .9   .93  .84   .6  1.591  1.02
1  1     .58  .58  1     .531  1.002
0   .95  .32  .3   1.6   .886   .988
1  1     .6   .6   1.7   .964   .99
1  1     .69  .69   .9   .398   .986
0  1     .73  .73   .7   .398   .986
;
run;
title 'Stepwise Regression on Cancer Remission Data';
proc logistic data=Remission outest=betas covout;
   model remiss(event='1')=cell smear infil li blast temp
                / selection=stepwise
                  slentry=0.3
                  slstay=0.35
                  details
                  lackfit;
   output out=pred p=phat lower=lcl upper=ucl
          predprob=(individual crossvalidate);
run;
proc print data=betas;
   title2 'Parameter Estimates and Covariance Matrix';
run;
proc print data=pred;
   title2 'Predicted Probabilities and 95% Confidence Limits';
run;
````

</details>

#### ch28_Logistic_lian_xu_bian_liang · SAS · 7bfa8f7c

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `PROC LOGISTIC`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`aee8f163d62fbfa69b930f8dc685c2ef8fbb0089c45e6cf5fa8823dad194301a`
- 语言：SAS
- 符号：`PROC LOGISTIC`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch28_Logistic_lian_xu_bian_liang.sas`

<details>
<summary>展开原始代码</summary>

````sas
data coronary;  
input sex ecg age ca @@ ;  
datalines;  
0 0 28 0 1 0 42 1 0 1 46 0 1 1 45 0  
0 0 34 0 1 0 44 1 0 1 48 1 1 1 45 1  
0 0 38 0 1 0 45 0 0 1 49 0 1 1 45 1  
0 0 41 1 1 0 46 0 0 1 49 0 1 1 46 1  
0 0 44 0 1 0 48 0 0 1 52 0 1 1 48 1  
0 0 45 1 1 0 50 0 0 1 53 1 1 1 57 1  
0 0 46 0 1 0 52 1 0 1 54 1 1 1 57 1  
0 0 47 0 1 0 52 1 0 1 55 0 1 1 59 1  
0 0 50 0 1 0 54 0 0 1 57 1 1 1 60 1  
0 0 51 0 1 0 55 0 0 2 46 1 1 1 63 1  
0 0 51 0 1 0 59 1 0 2 48 0 1 2 35 0  
0 0 53 0 1 0 59 1 0 2 57 1 1 2 37 1  
0 0 55 1 1 1 32 0 0 2 60 1 1 2 43 1  
0 0 59 0 1 1 37 0 1 0 30 0 1 2 47 1  
0 0 60 1 1 1 38 1 1 0 34 0 1 2 48 1  
0 1 32 1 1 1 38 1 1 0 36 1 1 2 49 0  
0 1 33 0 1 1 42 1 1 0 38 1 1 2 58 1  
0 1 35 0 1 1 43 0 1 0 39 0 1 2 59 1  
0 1 39 0 1 1 43 1 1 0 42 0 1 2 60 1  
0 1 40 0 1 1 44 1  
;  
run;  
*selection用于选择逐步回归方法,包括forward,backward,stepwise
include:设定每个拟合模型中包含model语句中列的因子的个数. units:可以设置自变量每次变化10个单位，计算的调整的发生比率AOR;  
proc logistic data = coronary descending;  
model ca = sex ecg age ecg*ecg age*age sex*ecg sex*age ecg*age / selection=forward include=3 details lackfit;  
run;  
proc logistic descending;  
model ca=sex ecg age;  
units age=10;  
run;  
````

</details>

#### ch37_ping_wen_xing_jian_yan · SAS · 10cc6636

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0c77167ebc7842d74499c42ea9668773079fb8c834d06e668daccaa830dfd760`
- 语言：SAS
- 符号：`PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch37_ping_wen_xing_jian_yan.sas`

<details>
<summary>展开原始代码</summary>

````sas
data RawData;
input Year Qtr x y;
datalines;
1987 4 -0.05294 0.067891
1988 1 -0.14696 0.063533
1988 2 -0.12600 0.065794
1988 3 -0.14656 0.060760
1988 4 -0.06056 0.062053
1989 1 -0.02644 0.057527
1989 2 -0.05778 0.049068
1989 3 0.01924 0.061497
1989 4 -0.10823 0.060421
1990 1 -0.04056 0.050771
1990 2 -0.03390 0.036702
1990 3 -0.06903 0.016959
1990 4 0.07547 0.002585
;
run;
data TimeSeries;
set RawData;
x_1st_LAG = LAG1(x);
x_1st_DIFF = DIF1(x);
x_1st_DIFF_1st_LAG = DIF1(LAG1(x));
x_1st_DIFF_2nd_LAG = DIF1(LAG2(x));
x_1st_DIFF_3rd_LAG = DIF1(LAG3(x));
x_1st_DIFF_4th_LAG = DIF1(LAG4(x));
x_1st_DIFF_5th_LAG = DIF1(LAG5(x));
run;
proc reg data = TimeSeries;
model x_1st_DIFF = x_1st_LAG 
x_1st_DIFF_1st_LAG 
x_1st_DIFF_2nd_LAG 
x_1st_DIFF_3rd_LAG 
x_1st_DIFF_4th_LAG 
x_1st_DIFF_5th_LAG;
run;
````

</details>

#### ch37_ping_wen_xing_jian_yan2 · SAS · c997bb68

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c47e8266d2fb87e04ce2dfd0d072a9fe0677f1a144223778461f0993b9c21f7e`
- 语言：SAS
- 符号：`PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch37_ping_wen_xing_jian_yan2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data simulation;     
do i=1 to 100;          
x=rannor(1234);          
output;    
end;
run;
data timeseries;      
set simulation;     
x_1st_lag= lag1(x);      
x_1st_diff= dif1(x);     
x_1st_diff_1st_lag= dif1(lag1(x));      
x_1st_diff_2nd_lag= dif1(lag2(x));     
x_1st_diff_3rd_lag= dif1(lag3(x));      
x_1st_diff_4th_lag= dif1(lag4(x));     
x_1st_diff_5th_lag= dif1(lag5(x));
run;
proc reg data=timeseries;      
model x_1st_diff= x_1st_lag                                    
x_1st_diff_1st_lag                                    
x_1st_diff_2nd_lag                                    
x_1st_diff_3rd_lag                                    
x_1st_diff_4th_lag                                    
x_1st_diff_5th_lag;
run;
````

</details>

#### ch40_GARCH_yi_fang_cha · SAS · a16c50c7

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC AUTOREG`、`PROC GPLOT`、`PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`02e935ab947b0ee2da5a1730d93cda4c7c8916b3cf0a13e1750fe4344a8b27ff`
- 语言：SAS
- 符号：`PROC AUTOREG`, `PROC GPLOT`, `PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch40_GARCH_yi_fang_cha.sas`

<details>
<summary>展开原始代码</summary>

````sas
data randar;
     e1=0;
     e11=0;
     do t=-10 to 36;
        e=1.3*e1-0.5*e11+2*rannor(12346);
        x=10+0.5*t+e;
        e11=e1;
        e1=e;
        if t>0 then
           output;
        end;
run;
proc print data=randar;
run;
proc autoreg data=randar PLOTS(ONLY) = FITPLOT;
     model x=t;
run;
proc autoreg data=randar;
     model x=t /dw=4 dwprob;
run;
proc autoreg data=randar;
     model x=t /nlag=2 method=ml;
     output out=pout p=xhat pm=trendhat;
run;
proc gplot data=pout;
     plot x*t=1 xhat*t=2 trendhat*t=3 /overlay;
     symbol1 v=star i=none c=red   h=2.5;
     symbol2 v=plus i=join c=blue  h=2.5;
     symbol3 v=none i=join c=green w=2;
     title1 'Auto-Regression';
     title2 'nlag=2 method=ml';
run;
data new;
     x=. ;
     do t=37 to 46;
        output;
     end;
run;
data randar37;
     merge randar new;
     by t;
run;
proc autoreg data=randar37;
     model x=t /nlag=2 method=ml;
     output out=poutp p=xhat pm=trendhat lcl=lcl ucl=ucl;
run;
proc gplot data=poutp;
     plot x*t=1 xhat*t=2 trendhat*t=3 lcl*t=3 ucl*t=3/overlay href=36.5;
     symbol1 v=star i=none c=red   h=2.5;
     symbol2 v=plus i=join c=blue  h=2.5 l=1;
     symbol3 v=none i=join c=green w=2 ;
     title1 'Auto-Regression:AR(2)';
     title2 'predict estimation';
run;
proc autoreg data=randar;
     model x=t /nlag=5 method=ml backstep;
     title 'Auto-Regression:Backstep';
run;
````

</details>

#### 例4.1 · SAS · 3ffa93d5

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC GPLOT`、`PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5f48edd44922817550c16a3e5b1358a2b52812933f3aff2bb173b506bde013e3`
- 语言：SAS
- 符号：`PROC GPLOT`, `PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第四章/例4.1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input gov_cons@@;
time=intnx('quarter','1jan1981'd,_n_-1);
format time year2.;
t=_n_;
cards;
8444	9215	8879	8990	8115	9457	8590	9294	8997	9574
9051	9724	9120	10143	9746	10074	9578	10817	10116	10779
9901	11266	10686	10961	10121	11333	10677	11325	10698	11624
11052	11393	10609	12077	11376	11777	11225	12231	11884	12109
;
proc gplot;
plot gov_cons*time=1;
symbol1 c=black v=star i=join;
proc reg;
model gov_cons=t;
output out=out p=gov_cons_cup;
proc gplot data=out;
plot gov_cons*time=1 gov_cons_cup*time=2/overlay haxis='1jan1981'd to '1jan1991'd by year;
symbol2 c=red v=none i=join w=2 l=3;
run;
````

</details>

#### 例4.2 · SAS · 264487df

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC GPLOT`、`PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3e12d7678e1aaba7d8878e4f75c2e03f2c89c466fe5411add8782b74bad922cc`
- 语言：SAS
- 符号：`PROC GPLOT`, `PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第四章/例4.2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input index@@;
time=intnx('month','1jan1991'd,_n_-1);
format time year2.;
t=_n_;
t2=t**2;
cards;
130.44	133.47	120.19	113.94	114.83	137.56	143.80	178.43	180.92
218.60	259.60	292.75	313.24	364.66	381.24	445.38	1234.71	1191.19
1052.07	823.27	702.32	507.25	724.60	780.39	1198.48	1339.88	925.91
1358.78	935.48	1007.05	881.07	895.68	890.27	814.82	984.93	833.80
770.25	770.98	704.46	592.56	556.26	469.29	333.92	785.33	791.15
654.98	683.59	647.87	562.59	549.26	646.92	579.93	700.51	630.58
695.55	723.87	722.43	717.32	641.13	555.29	537.34	552.93	556.39
681.16	643.65	804.25	822.48	809.94	875.52	976.71	1032.95	917.02
964.74	1040.27	1234.62	1393.75	1285.18	1250.27	1189.76	1221.06	1097.38
1180.39	1139.63	1194.10	1222.91	1206.53	1243.01	1343.44	1411.20	1339.20
1316.91	1150.22	1242.09	1217.31	1247.42	1146.70	1134.67	1090.09	1158.05
1120.92	1279.32	1689.42	1601.45	1627.12	1570.70	1504.56	1434.97	1366.58
1535.00	1714.58	1800.22	1836.32	1894.55	1928.11	2023.54	2021.20	1910.16
1961.29	2070.61	2073.48	2065.61	1959.18	2112.78	2119.18	2213.18	2218.03
1920.32	1834.14	1764.87	1689.17
;
proc gplot;
plot index*time=1;
symbol1 c=black v=none i=join;
proc reg;
model index=t t2;
model index=t2;
output out=out p=index_cup;
proc gplot data=out;
plot index*time=1 index_cup*time=2/overlay;
symbol2 c=red v=none i=join w=2 l=3;
run;
````

</details>

#### 相似实现组 · MATLAB · 2ae4d944

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：liti11.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3aae1fbfac43ea6d39e12582fc1bd7621c85a62931ff9d91dacb9768f11193f1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti11.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=[143 145 146 147 149 150 153 154 155 156 157 158 159 160 162 164]';
X=[ones(16,1) x];
Y=[88 85 88 91 92 93 93 95 96 98 97 96 98 99 100 102]';
[b,bint,r,rint,stats]=regress(Y,X);
b,bint,stats
````

</details>

##### 变体 2：liti22.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3a3a9e7d659cc914620daff44a48368e5744d9ce6cf394d0c5bef477b84f753e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti22.m`

<details>
<summary>展开原始代码</summary>

````matlab
t=1/30:1/30:14/30;
 s=[11.86 15.67 20.60 26.69 33.71 41.93 51.13 61.49 72.90 85.44 99.08 113.77 129.54 146.48];

T=[ones(14,1) t' (t.^2)' (t.^3)'];
[b,bint,r,rint,stats]=regress(s',T);
b,stats
````

</details>

#### liti12 · MATLAB · da3a8e4c

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`02ff0a9ffc4a53d1c8893d48bf32ea39f9d507cd9110468547ee7c46ff4a4c78`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti12.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=[143 145 146 147 149 150 153 154 155 156 157 158 159 160 162 164]';
X=[ones(16,1) x];
Y=[88 85 88 91 92 93 93 95 96 98 97 96 98 99 100 102]';
[b,bint,r,rint,stats]=regress(Y,X);

rcoplot(r,rint)

figure(2)
z=b(1)+b(2)*x
plot(x,Y,'k+',x,z,'r')
````

</details>

#### liti21 · MATLAB · 71870bc9

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：执行插值或参数拟合并评价曲线。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`28a82b656a676f5f54c6358857577eb63fabc4c9e4a7e8b1afa219a5d12bea29`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti21.m`

<details>
<summary>展开原始代码</summary>

````matlab
 t=1/30:1/30:14/30;
 s=[11.86 15.67 20.60 26.69 33.71 41.93 51.13 61.49 72.90 85.44 99.08 113.77 129.54 146.48];

     [p,S]=polyfit(t,s,2)
   
````

</details>

#### liti23 · MATLAB · c86dedfc

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：执行插值或参数拟合并评价曲线；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a1dbf37bf6fd67769e10d6a60737b84d80fdf3244af4cd23631647d9c8a1b136`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti23.m`

<details>
<summary>展开原始代码</summary>

````matlab
t=1/30:1/30:14/30;
 s=[11.86 15.67 20.60 26.69 33.71 41.93 51.13 61.49 72.90 85.44 99.08 113.77 129.54 146.48];

[p,S]=polyfit(t,s,3)


Y=polyconf(p,t,S)
plot(t,s,'k+',t,Y,'r')
````

</details>

#### liti31 · MATLAB · 025414fd

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c6a9e2ba09c2762150b4837bcbc79842365b4c30e0ebe14ebaf0c6d377dc0ada`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti31.m`

<details>
<summary>展开原始代码</summary>

````matlab
x1=[1000 600 1200 500 300 400 1300 1100 1300 300];
x2=[5 7 6 6 8 7 5 4 3 9];
y=[100 75 80 70 50 65 90 100 110 60]';
x=[x1' x2'];
rstool(x,y,'purequadratic')
````

</details>

#### liti32 · MATLAB · 377e2b5e

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8eef3352538f8ed1ec269d097f5f42270f33912f87be66bdd9c8ee131c57c568`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti32.m`

<details>
<summary>展开原始代码</summary>

````matlab
x1=[1000 600 1200 500 300 400 1300 1100 1300 300];
x2=[5 7 6 6 8 7 5 4 3 9];
y=[100 75 80 70 50 65 90 100 110 60]';

X=[ones(10,1) x1' x2' (x1.^2)' (x2.^2)'];
[b,bint,r,rint,stats]=regress(y,X);
b,stats
````

</details>

#### liti41 · MATLAB · ccef652a

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`890d835ca05e3de57e1079c0e77337b5ff7c6c7f7c19921b27a932dcf1e9f010`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti41.m`

<details>
<summary>展开原始代码</summary>

````matlab
     x=2:16;
     y=[6.42 8.20 9.58 9.5 9.7 10 9.93 9.99 10.49 10.59 10.60 10.80 10.60 10.90 10.76];
     beta0=[8 2]';
     
     [beta,r,J]=nlinfit(x',y','volum',beta0);
     beta
````

</details>

#### liti42 · MATLAB · 3afdd5a0

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2320c9a8b117e6323f077a2048babb10c21b33d33d5046f195caac88cc2ca18c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti42.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=2:16;
     y=[6.42 8.20 9.58 9.5 9.7 10 9.93 9.99 10.49 10.59 10.60 10.80 10.60 10.90 10.76];
     beta0=[8 2]';
     
[beta,r,J]=nlinfit(x',y','volum',beta0);

[YY,delta]=nlpredci('volum',x',beta,r ,J);
plot(x,y,'k+',x,YY,'r')
````

</details>

#### liti51 · MATLAB · c043b2c6

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6e940521a2f927787e36ce30bf0a0460a82cf6c293eb44640e266cf281745b05`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti51.m`

<details>
<summary>展开原始代码</summary>

````matlab
x1=[7 1 11 11 7 11 3 1 2 21 1 11 10]';
x2=[26 29 56 31 52 55 71 31 54 47 40 66 68]';
x3=[6 15 8 8 6 9 17 22 18 4 23 9 8]';
x4=[60 52 20 47 33 22 6 44 22 26 34 12 12]';
y=[78.5 74.3 104.3 87.6 95.9 109.2 102.7 72.5 93.1 115.9 83.8 113.3 109.4]';
x=[x1 x2 x3 x4];

stepwise(x,y)
````

</details>

#### liti52 · MATLAB · a0feeeff

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a0729357cd6fc7a44772b38ad2f096fd13358a9b1650b6ee10f0ad28971db562`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti52.m`

<details>
<summary>展开原始代码</summary>

````matlab
x1=[7 1 11 11 7 11 3 1 2 21 1 11 10]';
x2=[26 29 56 31 52 55 71 31 54 47 40 66 68]';
y=[78.5 74.3 104.3 87.6 95.9 109.2 102.7 72.5 93.1 115.9 83.8 113.3 109.4]';

X=[ones(13,1) x1 x2];
   b=regress(y,X)
````

</details>

#### liti6 · MATLAB · ed6b8530

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6d72b1615da127d035c94ef237f9a665076bc652c03d13b2accfb2255d065602`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/liti6.m`

<details>
<summary>展开原始代码</summary>

````matlab
    X=[598.00  349.00  461.00 57482.00 20729.00   44.00
       586.00  455.00  475.00 58796.00 21364.00   89.00
       707.00  520.00  491.00 60266.00 21832.00   97.00
       737.00  558.00  529.00 61465.00 22328.00   98.00
       825.00  715.00  556.00 62828.00 23018.00  150.00
       837.00  798.00  575.00 64653.00 23711.00  139.00
       1028.00 1235.00  598.00 65994.00 26600.00  256.00
       1114.00 1681.00  509.00 67207.00 26173.00  338.00
       1079.00 1870.00  444.00 66207.00 25880.00  380.00
       757.00 1156.00  434.00 65859.00 25590.00  138.00
       677.00  964.00  461.00 67295.00 25110.00   66.00
       779.00 1046.00  514.00 69172.00 26640.00   85.00
       943.00 1250.00  584.00 70499.00 27736.00  129.00
      1152.00 1581.00  632.00 72538.00 28670.00  175.00
      1322.00 1911.00  687.00 74542.00 29805.00  212.00
      1249.00 1647.00  697.00 76368.00 30814.00  156.00
      1187.00 1565.00  680.00 78534.00 31915.00  127.00
      1372.00 2101.00  688.00 80671.00 33225.00  207.00
      1638.00 2747.00  767.00 82992.00 34432.00  312.00
      1780.00 3156.00  790.00 85229.00 35620.00  355.00
      1833.00 3365.00  789.00 87177.00 35854.00  354.00
      1978.00 3684.00  855.00 89211.00 36652.00  374.00
      1993.00 3696.00  891.00 90859.00 37369.00  393.00
      2121.00 4254.00  932.00 92421.00 38168.00  462.00
      2052.00 4309.00  955.00 93717.00 38834.00  443.00
      2189.00 4925.00  971.00 94974.00 39377.00  454.00
        2475.00 5590.00 1058.00 96259.00 39856.00  550.00
        2702.00 6065.00 1150.00 97542.00 40581.00  564.00
        2791.00 6592.00 1194.00 98705.00 41896.00  568.00
       2927.00 6862.00 1273.00 100072.0 43280.00  496.00];
y=[184.00 216.00 248.00 254.00 268.00 286.00 357.00 444.00 506.00 ... 
   271.00 230.00 266.00 323.00 393.00 466.00 352.00 303.00 447.00 ...
   564.00 638.00 658.00 691.00 655.00 692.00 657.00 723.00 922.00 ...
   890.00 826.00 810.0]';
beta0=[0.50 -0.03 -0.60 0.01 -0.02 0.35];
betafit = nlinfit(X,y,'model',beta0)
````

</details>

#### model · MATLAB · 09a0a87e

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `model`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e1567d5d08059e276457b1e2c676ec084f630eae306f939751e897a9c4208599`
- 语言：MATLAB
- 符号：`model`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/model.m`

<details>
<summary>展开原始代码</summary>

````matlab
      function yy=model(beta0,X)
         a=beta0(1);
         b=beta0(2);
         c=beta0(3);
         d=beta0(4);
         e=beta0(5);
         f=beta0(6);
         x1=X(:,1);
         x2=X(:,2);
         x3=X(:,3);
         x4=X(:,4);
         x5=X(:,5);
         x6=X(:,6);
         yy=a*x1+b*x2+c*x3+d*x4+e*x5+f*x6;
````

</details>

#### yhat · MATLAB · ddaa622e

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于回归分析中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `volum`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6ed09bed3549bb8b9c63284c1787b549c3c77e9772baacdbfbfa2a9a75b9416b`
- 语言：MATLAB
- 符号：`volum`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/预测方法/回归分析/第11讲 回归分析/yhat.m`

<details>
<summary>展开原始代码</summary>

````matlab
function yhat=volum(beta,x)
     yhat=beta(1)*exp(-beta(2)./x);
     
     
````

</details>

#### Pex4_22 · Python · 79021d18

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`71941c29d4dedce1b3e761849dbe338399b61b82cab45da0be4d0d6f2928619d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/04第4章  概率论与数理统计(Python 程序及数据)/Pex4_22.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex4_22.py
import numpy as np
import statsmodels.api as sm
y=np.array([1620, 1670, 1700, 1750, 1800, 1580, 1600, 1640, 1720,
            1460, 1540, 1620, 1680, 1500, 1550, 1610])
x=np.hstack([np.ones(5), np.full(4,2), np.full(4,3), np.full(3,4)])
d= {'x':x,'y':y}   #构造字典
model = sm.formula.ols("y~C(x)",d).fit()   #构建模型
anovat = sm.stats.anova_lm(model)  #进行单因素方差分析
print(anovat)
````

</details>

#### Pex4_23 · Python · 4fd9e144

- 归属算法：回归分析
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“数据读取与预处理”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`5af646fb7d623560770904847815bcf1bd18394e0a307660e09a28b5266e5181`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/04第4章  概率论与数理统计(Python 程序及数据)/Pex4_23.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex4_23.py
import numpy as np
import pandas as pd
import statsmodels.api as sm
df = pd.read_excel("Pdata4_23.xlsx", header=None)
a=df.values.T.flatten()
b=np.arange(1,6)
x=np.tile(b,(4,1)).T.flatten()
d={'x':x,'y':a} #构造求解需要的字典
model = sm.formula.ols("y~C(x)",d).fit()  #构建模型
anovat = sm.stats.anova_lm(model)  #进行单因素方差分析
print(anovat)
````

</details>

#### Pex4_24 · Python · bc61e191

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`bab8b3688ffc867836d3a9581a64aebfa02bf43456d05f7acb4ece9eb023b3cc`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/04第4章  概率论与数理统计(Python 程序及数据)/Pex4_24.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex4_24.py
import numpy as np
import statsmodels.api as sm
y=np.array([[11, 11, 13, 10], [10, 11, 9, 12],
         [9, 10, 7, 6], [7, 8, 11, 10],
         [5, 13, 12, 14], [11, 14, 13, 10]]).flatten()
A=np.tile(np.arange(1,5),(6,1)).flatten()
B=np.tile(np.arange(1,4).reshape(3,1),(1,8)).flatten()
d={'x1':A,'x2':B,'y':y}
model = sm.formula.ols("y~C(x1)+C(x2)+C(x1):C(x2)",d).fit()  #注意交互作用公式的写法
anovat = sm.stats.anova_lm(model)  #进行双因素方差分析
print(anovat)
````

</details>

#### Pex4_25_2 · Python · fb0c77ad

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`82dd8db9a613b4c44f4045cd0fb82e60790a9e0deac9a5547213984ae22a926c`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/04第4章  概率论与数理统计(Python 程序及数据)/Pex4_25_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex4_25_2.py
import statsmodels.api as sm
x=[2.5, 3.9, 2.9, 2.4, 2.9, 0.8, 9.1, 0.8, 0.7,7.9,
   1.8, 1.9, 0.8, 6.5, 1.6, 5.8, 1.3, 1.2, 2.7]
y=[211, 167, 131, 191, 220, 297, 71, 211, 300, 107,
   167, 266, 277, 86, 207, 115, 285, 199, 172]
df={'x':x,'y':y}
res=sm.formula.ols('y~x',data=df).fit()
print(res.summary(),'\n')
ypred=res.predict(dict(x=8))
print('所求的预测值为:',list(ypred))
````

</details>

#### Pex4_25_3 · Python · 533718e2

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ec6784b3705e3556ff64f75700d3222589021570fd221e965c888e2509c3c88f`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/04第4章  概率论与数理统计(Python 程序及数据)/Pex4_25_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex4_25_3.py
import statsmodels.api as sm
import numpy as np
x=np.array([2.5, 3.9, 2.9, 2.4, 2.9, 0.8, 9.1, 0.8, 0.7,
    7.9, 1.8, 1.9, 0.8, 6.5, 1.6, 5.8, 1.3, 1.2, 2.7])
y=np.array([211, 167, 131, 191, 220, 297, 71, 211, 300,
    107, 167, 266, 277, 86, 207, 115, 285, 199, 172])
X=sm.add_constant(x)
md=sm.OLS(y,X).fit()  #构建并拟合模型
print(md.params,'\n--------\n')  #提取回归系数
print(md.summary2())
ypred=md.predict([1,8])  #第一列必须加1
print("预测值为：",ypred)
````

</details>

#### Pex12_1 · Python · d64767fa

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`dabb14d085cf403926112d309cdcd45c767c44194b95704bc4ea7a02e06a41c7`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_1.py
import numpy as np
from sklearn.linear_model import LinearRegression
a=np.loadtxt("Pdata12_1.txt")   #加载表中x1,x2,y的13行3列数据
md=LinearRegression().fit(a[:,:2],a[:,2])    #构建并拟合模型
y=md.predict(a[:,:2])       #求预测值
b0=md.intercept_; b12=md.coef_   #输出回归系数
R2=md.score(a[:,:2],a[:,2])      #计算R^2
print("b0=%.4f\nb12=%.4f%10.4f"%(b0,b12[0],b12[1]))
print("拟合优度R^2=%.4f"%R2)
````

</details>

#### Pex12_10 · Python · 835c32c5

- 归属算法：回归分析
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“模型求解”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`353ee133a62ef55dfbfe05a04086ec0450c5fd97740d359b8d02640e5113f451`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_10.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_10.py
import numpy as np
from sklearn.linear_model import LogisticRegression
a=np.loadtxt("Pdata12_9.txt")
n=a.shape[1]  #提取矩阵的列数
x=a[:,:n-1]; y=a[:,n-1]
md=LogisticRegression(solver='lbfgs')
md=md.fit(x,y)
print(md.intercept_,md.coef_)
print(md.predict(x))   #检验预测模型
print(md.predict([[-49.2,-17.2,0.3],[40.6,26.4,1.8]]))  #求预测值
````

</details>

#### Pex12_2_1 · Python · 894ddd51

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`b7cb19a97a2ce951418a4b4178de1b7c0995d70752f2d56eaaf42eba48844ab0`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_2_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_2_1.py
import numpy as np; import statsmodels.api as sm
a=np.loadtxt("Pdata12_1.txt")
#加载表中x1,x2,y的13行3列数据（数据见封底二维码）
d={'x1':a[:,0],'x2':a[:,1],'y':a[:,2]}
md=sm.formula.ols('y~x1+x2',d).fit()  #构建并拟合模型
print(md.summary(),'\n------------\n')  #显示模型所有信息
ypred=md.predict({'x1':a[:,0],'x2':a[:,1]})  #计算预测值
print(ypred)  #输出预测值
````

</details>

#### Pex12_2_2 · Python · 5959e8a3

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`7c9e0127c1de13196316a2c6a5f6d90537e3ab512d518cf7b8be749541c4d751`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_2_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_2_2.py
import numpy as np; import statsmodels.api as sm
a=np.loadtxt("Pdata12_1.txt")
#加载表中x1,x2,y的13行3列数据（数据见封底二维码）
X = sm.add_constant(a[:,:2])  #增加第一列全部元素为1得到增广矩阵
md=sm.OLS(a[:,2],X).fit()  #构建并拟合模型
print(md.params,'\n------------\n')  #提取所有回归系数
y=md.predict(X)      #求已知自变量值的预测值
print(md.summary2())  #输出模型的所有结果
````

</details>

#### Pex12_3 · Python · 53e9f20d

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e65088bfee1956bc67887a44947b67373f1ea25c77478a4996de4ac65531d950`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_3.py
import numpy as np; import statsmodels.api as sm
a=np.loadtxt("Pdata12_3.txt")   #加载表中x1,x2,x3,y的11行4列数据
x=a[:,:3]  #提出自变量观测值矩阵
X=sm.add_constant(x)  #增加第一列全部元素为1得到增广矩阵
md=sm.OLS(a[:,3],X).fit()  #构建并拟合模型
b=md.params          #提取所有回归系数
y=md.predict(X)      #求已知自变量值的预测值
print(md.summary())  #输出模型的所有结果
print("相关系数矩阵:\n",np.corrcoef(x.T))
X1=sm.add_constant(a[:,0])
md1=sm.OLS(a[:,2],X1).fit()
print("回归系数为：",md1.params)
````

</details>

#### Pex12_4 · Python · 47e6d30b

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：执行归一化或标准化以统一变量尺度；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`80e8af8e8b8027491701253972994cac0f91a642b10edf498fd30f6e8205303a`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_4.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_4.py
import numpy as np; import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, RidgeCV
from scipy.stats import zscore
#plt.rc('text', usetex=True)  #没装LaTeX宏包把该句注释
a=np.loadtxt("Pdata12_3.txt")
n=a.shape[1]-1  #自变量的总个数
aa=zscore(a)  #数据标准化
x=aa[:,:n]; y=aa[:,n]  #提出自变量和因变量观测值矩阵
b=[]  #用于存储回归系数的空列表
kk=np.logspace(-4,0,100)  #循环迭代的不同k值
for k in kk:
    md=Ridge(alpha=k).fit(x,y)
    b.append(md.coef_)
st=['s-r','*-k','p-b']  #下面画图的控制字符串
for i in range(3): plt.plot(kk,np.array(b)[:,i],st[i]);
plt.legend(['$x_1$','$x_2$','$x_3$'],fontsize=15); plt.show()
mdcv=RidgeCV(alphas=np.logspace(-4,0,100)).fit(x,y);
print("最优alpha=",mdcv.alpha_) 
#md0=Ridge(mdcv.alpha_).fit(x,y)  #构建并拟合模型
md0=Ridge(0.4).fit(x,y)  #构建并拟合模型
cs0=md0.coef_  #提出标准化数据的回归系数b1,b2,b3
print("标准化数据的所有回归系数为：",cs0)
mu=np.mean(a,axis=0); s=np.std(a,axis=0,ddof=1) #计算所有指标的均值和标准差
params=[mu[-1]-s[-1]*sum(cs0*mu[:-1]/s[:-1]),s[-1]*cs0/s[:-1]] 
print("原数据的回归系数为：",params)
print("拟合优度：",md0.score(x,y))
````

</details>

#### Pex12_5 · Python · c3f33089

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：执行归一化或标准化以统一变量尺度；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`c2615a917be68f8a1e8ab97a7dfdc421c4dd5c6b77e7257fc27ce04e08c2e8a3`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_5.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_5.py
import numpy as np; import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso, LassoCV
from scipy.stats import zscore
plt.rc('font',size=16)
plt.rc('text', usetex=True)  #没装LaTeX宏包把该句注释
a=np.loadtxt("Pdata12_3.txt")
n=a.shape[1]-1  #自变量的总个数
aa=zscore(a)  #数据标准化
x=aa[:,:n]; y=aa[:,n]  #提出自变量和因变量观测值矩阵
b=[]  #用于存储回归系数的空列表
kk=np.logspace(-4,0,100)  #循环迭代的不同k值
for k in kk:
    md=Lasso(alpha=k).fit(x,y)
    b.append(md.coef_)
st=['s-r','*-k','p-b']  #下面画图的控制字符串
for i in range(3): plt.plot(kk,np.array(b)[:,i],st[i]);
plt.legend(['$x_1$','$x_2$','$x_3$'],fontsize=15); plt.show()
mdcv=LassoCV(alphas=np.logspace(-4,0,100)).fit(x,y);
print("最优alpha=",mdcv.alpha_) 
#md0=Lasso(mdcv.alpha_).fit(x,y)  #构建并拟合模型
md0=Lasso(0.21).fit(x,y)  #构建并拟合模型
cs0=md0.coef_  #提出标准化数据的回归系数b1,b2,b3
print("标准化数据的所有回归系数为：",cs0)
mu=np.mean(a,axis=0); s=np.std(a,axis=0,ddof=1) #计算所有指标的均值和标准差
params=[mu[-1]-s[-1]*sum(cs0*mu[:-1]/s[:-1]),s[-1]*cs0/s[:-1]] 
print("原数据的回归系数为：",params)
print("拟合优度：",md0.score(x,y))
````

</details>

#### Pex12_6 · Python · 2f34bea4

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；执行归一化或标准化以统一变量尺度；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`6d6818ff47c10d44816fe0443841b42559bb6bc87e925b279ef4f5f99868510b`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_6.py`

<details>
<summary>展开原始代码</summary>

````python
 #程序文件Pex12_6.py
import numpy as np; import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import Lasso
from scipy.stats import zscore
#plt.rc('text', usetex=True)  #没装LaTeX宏包把该句注释
a=np.loadtxt("Pdata12_6.txt")  #加载表中的9行5列数据
n=a.shape[1]-1  #自变量的总个数
x=a[:,:n]  #提出自变量观测值矩阵
X = sm.add_constant(x)
md=sm.OLS(a[:,n],X).fit()  #构建并拟合模型
print(md.summary())  #输出模型的所有结果

aa=zscore(a)  #数据标准化
x=aa[:,:n]; y=aa[:,n]  #提出自变量和因变量观测值矩阵
b=[]  #用于存储回归系数的空列表
kk=np.logspace(-4,0,100)  #循环迭代的不同k值
for k in kk:
    md=Lasso(alpha=k).fit(x,y)
    b.append(md.coef_)
st=['s-r','*-k','p-b','^-y']  #下面画图的控制字符串
for i in range(n): plt.plot(kk,np.array(b)[:,i],st[i]);
plt.legend(['$x_1$','$x_2$','$x_3$','$x_4$'],fontsize=15); plt.show()
md0=Lasso(0.05).fit(x,y)  #构建并拟合模型
cs0=md0.coef_  #提出标准化数据的回归系数b1,b2,b3,b4
print("标准化数据的所有回归系数为：",cs0)
mu=a.mean(axis=0); s=a.std(axis=0,ddof=1) #计算所有指标的均值和标准差
params=[mu[-1]-s[-1]*sum(cs0*mu[:-1]/s[:-1]),s[-1]*cs0/s[:-1]] 
print("原数据的回归系数为：",params)
print("拟合优度：",md0.score(x,y))
````

</details>

#### Pex12_7 · Python · 76458db6

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`d02ac7c5fe61ca659a2ce83a448d3bd60e65813311f87dcfb12029240ae03c62`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_7.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_7.py
import numpy as np
import statsmodels.api as sm
a=np.loadtxt("Pdata12_7_1.txt")   #加载表中x,ni,mi的9行3列数据
x=a[:,0]; pi=a[:,2]/a[:,1]
X=sm.add_constant(x); yi=np.log(pi/(1-pi))
md=sm.OLS(yi,X).fit()  #构建并拟合模型
print(md.summary())  #输出模型的所有结果
b=md.params  #提出所有的回归系数
p0=1/(1+np.exp(-np.dot(b,[1,9])))
print("所求概率p0=%.4f"%p0)
np.savetxt("Pdata12_7_2.txt", b)  #把回归系数保存到文本文件
````

</details>

#### Pex12_8 · Python · 08f6729a

- 归属算法：回归分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`be20f59152068b730b9bd497d864f5c11e08d024ddfdf77449dd7554bec5f90e`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_8.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex12_8.py
import numpy as np
b=np.loadtxt("Pdata12_7_2.txt")
odds9=np.exp(np.dot(b,[1,9]))
odds9vs8=np.exp(np.dot([1,9],b))/np.exp(np.dot([1,8],b))
print("odds9=%.4f,odds9vs8=%.4f"%(odds9,odds9vs8))
````

</details>

#### Pex12_9 · Python · 75dbc045

- 归属算法：回归分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`70143e759520242264fa54dc7543dadde7f0930b2bb5810f0b882de74fe8d207`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/12第12章  回归分析（Python 程序及数据）/Pex12_9.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件 Pex12_9.py
import numpy as np
import statsmodels.api as sm
a=np.loadtxt("Pdata12_9.txt")
n=a.shape[1] #提取矩阵的列数
x=a[:,:n-1]; y=a[:,n-1]
md=sm.Logit(y,x)
md=md.fit(method="bfgs")  #这里必须使用bfgs方法，使用默认牛顿方法出错
print(md.params,'\n----------\n'); print(md.summary2())
print(md.predict([[-49.2,-17.2,0.3],[40.6,26.4,1.8]]))  #求预测值
````

</details>

#### Pex18_5_1 · Python · 9fe0bdd6

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`8971e5cd17330ccd07d57e74a04a263b0ea35e5feb6173fddf8c8e751bea04b9`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_5_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_5_1.py
import pandas as pd, numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.rc('font',family='SimHei'); plt.rc('font',size=16)
d=pd.read_csv('sunspots.csv',usecols=['counts'])
md=sm.tsa.ARMA(d,(9,1)).fit()
years=np.arange(1700,1989)  #已知观测值的年代
dhat=md.predict()
plt.plot(years[-20:],d.values[-20:],'o-k')
plt.plot(years[-20:],dhat.values[-20:],'P--')
plt.legend(('原始观测值','预测值')); plt.show()
dnext=md.predict(d.shape[0],d.shape[0])
print(dnext)  #显示下一期的预测值
````

</details>

#### Pex18_5_2 · Python · 94179c16

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`a6a0a7fe958e8fa3e85ea2b0ebb1c68365b16c5f55467896e14e4e5c6625aa5f`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_5_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_5_2.py
import pandas as pd, numpy as np
import statsmodels.api as sm
import matplotlib.pylab as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plt.rc('axes',unicode_minus=False)
plt.rc('font',family='SimHei'); plt.rc('font',size=16)
d=pd.read_csv('sunspots.csv'); dd=d['counts']
years=d['year'].values.astype(int)
plt.plot(years,dd.values,'-*'); plt.figure()
ax1=plt.subplot(121); plot_acf(dd,ax=ax1,title='自相关')
ax2=plt.subplot(122); plot_pacf(dd,ax=ax2,title='偏自相关')

for i in range(1,6):
    for j in range(1,6):
        md=sm.tsa.ARMA(dd,(i,j)).fit()
        print([i,j,md.aic,md.bic])
zmd=sm.tsa.ARMA(dd,(4,2)).fit()
print(zmd.summary())  #显示模型的所有信息

residuals = pd.DataFrame(zmd.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="残差", ax=ax[0])
residuals.plot(kind='kde', title='密度', ax=ax[1])
plt.legend(''); plt.ylabel('') 

dhat=zmd.predict(); plt.figure()
plt.plot(years[-20:],dd.values[-20:],'o-k')
plt.plot(years[-20:],dhat.values[-20:],'P--')
plt.legend(('原始观测值','预测值'))
dnext=zmd.predict(d.shape[0],d.shape[0])
print(dnext)  #显示下一期的预测值
plt.show()
````

</details>

#### jingxiangjiyuce · MATLAB · 511cb63d

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径；使用旧版接口，运行前检查当前软件兼容性。

- SHA-256：`d9be4fbd2e5877a6e5e4b1ede750f8b2bc4a65e61f63d3d426176749e89ed017`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/RBF神经网络做回归预测代码/jingxiangjiyuce.m`

<details>
<summary>展开原始代码</summary>

````matlab
%%主要程序   前200个点用于训练网络，并且生成三维神经网络图。然后代入后400个点于三维图中，并记录实验数据
% clear all
% close all
% clc
% % tic,
% xlsfile='C:\Users\Administrator\Desktop\误差.xlsx';
% [xji]=xlsread(xlsfile,'Sheet1','A1:A13880');
% [yji]=xlsread(xlsfile,'Sheet1','B1:B13880');
% [feng]=xlsread(xlsfile,'Sheet1','C1:C13880');
% 
% 
% [b,ps]=mapminmax(xji',0,1);
% [c,ps]=mapminmax(yji',0,1);
% [d,ps]=mapminmax(feng',0,1);

% t=b(1:11000);
% u=c(1:11000);
% v=d(1:11000);                        
% 
% p1=[t;u];
% t1=v;
clc;
A=untitled;
x1=A(1:157,1);
x2=A(2:158,1);
x3=A(3:159,1);
p1=[x1 x2 x3]';
t1=A(4:160,1)';
% spread=80000;  
% net=newrbe(p1,t1,spread);

net=newff(p1,t1);
% toc

%绘制预测模型
% [x2,v2]=meshgrid(0:0.02:1); 
% P = [x2(:)';v2(:)'];
% z2 = sim(net,P);
% z2=reshape(z2,51,51);
% surf(x2,v2,z2);
% title('神经网络预测曲面');  
% x1=xlabel('风速');       
% x2=ylabel('主轴转速');        
% x3=zlabel('振动特征值');        
% set(x1,'Rotation',30);    
% set(x2,'Rotation',-30); 
% hold on;
% 代入检测点
% bb=b(11001:13880);
% cc=c(11001:13880);
% dd=d(11001:13880);
% 
% 
% % scatter3(xx,vv,zz)%散点图
% % hold off;
% P_test=[bb;cc];
% t_test=dd;
test_x1=A(161:197,1);
test_x2=A(162:198,1);
test_x3=A(163:199,1);
P_test=[test_x1 test_x2 test_x3]';
t_test=A(164:200,1)';

Y=sim(net,P_test);
Z=Y';
e1=abs(Y-t_test);
% figure(2)
% ll1=(1:1:37);
% plot(ll1,dd,'b');
% hold on;
% plot(ll1,Y,'r');
% hold on;
% plot(ll1,e1,'m');
% legend('RBF神经网络预测','测量值','误差')
% hold off;
% xlabel('时间轴/10min');ylabel('功率');
% title('径向基神经网络预测'); 
g=mean(e1)
n=37;
j=sqrt(sum((Y-t_test).^2)/n) 
c=mean(abs(e1./t_test))
d=sqrt(sum((e1./t_test.^2)/n))
````

</details>

#### 回归预测分析MATLAB代码 · MATLAB · c56e38fb

- 归属算法：回归分析
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#回归分析 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于回归分析中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`eff8a3199303d8e3758829f04bb6ae0ad59911b3859fdd04133dc3a92ae0967e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/回归预测分析MATLAB代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
%reg.m
%回归分析法解
%…………………………………………
clc
%原始数据
%公路客运量(万人)
glkyl=[12815 15543 19326 22864 26150 28468 30882 39375 45759 49589 52560 48726 51083 56495 62767 83606 92090 101370 107317 108654 111847 112872 116997 126007 128980];
%公路货运量(万吨)
glhyl=[2690 2998 3012 3042 3616 3728 3988 9397 17680 19426 24128 24354 22879 24162 28957 36439 40593 45052 47400 45224 45338 45815 47151 55705 63532];
%市区人数(万人)
sqrs=[47.8 52.2 59 63.1 68.5 70 72 79.2 84.7 88.6 91 93 97.5 103.7 110 123 129.6 132 137.6 141 145 155.5 157 163.1 165.9];
%市区机动车数(万辆)
sqjdcs=[1.2 1.5 1.7 1.8 2.1 2.7 2.9	3.2	3.4	3.7	4.3	4.4	4.5	4.7	5 5.2 5.4 5.7 5.9 6.2 6.3 6.7 7.2 7.5 7.9];
%市区公路面积(万平方公里)
sqglmj=[0.2 0.25 0.25 0.3 0.45 0.5 0.5 0.7 0.7 0.75 0.8 0.8 0.85 1.1 1.25 1.3 1.3 1.5 1.55 1.75 1.8 1.8 2.05 2.1 2.3];
bb=[sqrs;sqjdcs;sqglmj]';  %输入数据矩阵
cc=[glkyl;glhyl]';         %输出数据矩阵

V=[];                      %将来的系数矩阵
sh=[];
X=[ones(25,1) , bb];       %自变量矩阵（注意：第一列全为1）

%回归法求系数
for n=1:2    
    [b,bint,r,rint,ss]=regress(cc(:,n),X,0.0005); %regress函数
    V(:,n)=b;              %系数矩阵
    sh(:,n)=r;
end

%带回验算  并绘图与原始数据对比
nf=1980:2004;
RLW=X*V;
figure;plot(nf,cc,'b:+');
hold on
plot(nf,RLW,'r-.');
grid on

%利用线性拟合出的数据来预测05、06的公路客运量和货运量
nh=[170.67	175.7
7.927	8.1949
2.1955	2.2818]';
nn=[zeros(2,1),nh];
ycc=nn*V;  %预测结果
````

</details>

### 指数平滑 · 实现

#### ex8_5 · MATLAB · 34880373

- 归属算法：指数平滑
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#指数平滑 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于指数平滑中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`7049198e81c09473d7b8ddc9a4ad7ef494333eced83ec3ec5e30b803d3538932`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_5.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
yt=load('ranliao.txt'); %实际燃料消耗量数据以列向量的方式存放在纯文本文件中
n=length(yt); alpha=0.4; 
dyt=diff(yt); %求yt的一阶向前差分
dyt=[0;dyt]; %这里使用的是一阶向后差分，加“0”补位
dyhat(2)=dyt(2); %指数平滑值的初始值
for i=2:n
    dyhat(i+1)=alpha*dyt(i)+(1-alpha)*dyhat(i);
end
for i=1:n
    yhat(i+1)=dyhat(i+1)+yt(i);  
end
yhat
xlswrite('ranliao.xls',[yt,dyt]) 
xlswrite('ranliao.xls',[dyhat',yhat'],'Sheet1','C1')
````

</details>

#### 三次指数平滑及其时间序列预测 · MATLAB · 08136fda

- 归属算法：指数平滑
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#指数平滑 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于指数平滑中的“结果绘图与展示”。
- **执行主线**：递推更新水平、趋势或季节项完成预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f63ead062cc341b719119c785a5ca1a23a8d756c32e9a861d0c4a1c42eabfedb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/三次指数平滑及其时间序列预测.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function [Y,S1,S2,S3,a,b,c] = expsmooth3(Yt,alpha,t)
%Yt:原时间序列；alpha:平滑系数；t:预测时长
%Y:预测值；S1/S2/S3:一次/二次/三次指数平滑值；a/b/c:预测公式参数
n=length(Yt);
%计算一次指数平滑值
S1(1)=Yt(1);
for i=2:n
    S1(i)=alpha*Yt(i)+(1-alpha)*S1(i-1);
end
%计算二次指数平滑值
S2(1)=S1(1);
for i=2:n
    S2(i)=alpha*S1(i)+(1-alpha)*S2(i-1);
end
%计算三次指数平滑值
S3(1)=S2(1);
for i=2:n
    S3(i)=alpha*S2(i)+(1-alpha)*S3(i-1);
end
%计算参数a、b、c
for i=1:n
    a(i)=3*S1(i)-3*S2(i)+S3(i);
    b(i)=alpha/(1-alpha)^2/2 * ((6-5*alpha)*S1(i) - 2*(5-4*alpha)*S2(i) + (4-3*alpha)*S3(i));
    c(i)=alpha/(1-alpha)^2/2 * (S1(i)-2*S2(i)+S3(i));
end
%计算预测值Y
for i=1:t
    Y(i)=a(n)+b(n)*i+c(n)*i^2;
end
%绘图
plot(1:n,Yt,(n+1):(n+t),Y,'*');
end
````

</details>

#### 二次指数平滑及其时间序列预测代码 · MATLAB · 0418eacb

- 归属算法：指数平滑
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#指数平滑 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于指数平滑中的“结果绘图与展示”。
- **执行主线**：递推更新水平、趋势或季节项完成预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`47c42c2c24c4c39c33dee5ad0770ee8f25914f1071f3e6389080abd380c671e9`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/二次指数平滑及其时间序列预测代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function [Y,S1,S2,a,b] = expsmooth2(Yt,alpha,t)
%Yt:原时间序列；alpha:平滑系数；t:预测时长
%Y:预测值；S1/S2:一次/二次指数平滑值；a/b:预测公式参数
n=length(Yt);
%计算一次指数平滑值
S1(1)=Yt(1);
for i=2:n
    S1(i)=alpha*Yt(i)+(1-alpha)*S1(i-1);
end
%计算二次指数平滑值
S2(1)=S1(1);
for i=2:n
    S2(i)=alpha*S1(i)+(1-alpha)*S2(i-1);
end
%计算参数a和b
for i=1:n
    a(i)=2*S1(i)-S2(i);
    b(i)=alpha/(1-alpha)*(S1(i)-S2(i));
end
%计算预测值Y
for i=1:t
    Y(i)=a(n)+b(n)*i;
end
%绘图
plot(1:n,Yt,(n+1):(n+t),Y,'*');
end
````

</details>

### 时间序列方法 · 实现

#### ex8_1 · MATLAB · 5ce96690

- 归属算法：时间序列方法
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#时间序列方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于时间序列方法中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0ecfe1989841f9f45577d80148fbb2cd67e5f7f4b03f81b774bf0da56971464c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
y=[533.8  574.6  606.9  649.8   705.1  772.0  816.4  892.7  963.9  1015.1  1102.7];
m=length(y);   
n=[4,5];   %n为移动平均的项数
for i=1:length(n)    %由于n的取值不同，下面使用了细胞数组
    for j=1:m-n(i)+1
        yhat{i}(j)=sum(y(j:j+n(i)-1))/n(i); 
    end
    y12(i)=yhat{i}(end);  %提出第12月份的预测值
    s(i)=sqrt(mean((y(n(i)+1:end)-yhat{i}(1:end-1)).^2)); %求预测的标准误差
end
y12, s   %分别显示两种方法的预测值和预测的标准误差
````

</details>

#### ex8_13 · MATLAB · 2f6b48ba

- 归属算法：时间序列方法
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#时间序列方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于时间序列方法中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`2ad19a147053f97237bd37ec46db32ac4fd82c3010069c1b195057423e23abe1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_13.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
spec=garchset('R',2);
y=load('mydata.txt');
[Coeff,Errors,LLF,Innovations,Sigmas,Summary]=garchfit(spec,y);
Coeff
[SigmaForecast,MeanForecast]=garchpred(Coeff,y,3)
````

</details>

#### ex8_14 · MATLAB · a97e4605

- 归属算法：时间序列方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#时间序列方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于时间序列方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`74f5e305685cca17538e8d3f1e1ff5e477233a75e60a7d352fa39c7c029e3573`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_14.m`

<details>
<summary>展开原始代码</summary>

````matlab
price=[1:6]'
dates=[today:today+5]'
obj=fints(dates,price)
````

</details>

#### ex8_2 · MATLAB · d154d8db

- 归属算法：时间序列方法
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#时间序列方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于时间序列方法中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`28543ce6a6035bdbad2ca946587e88f327aaf40ea1ead4c69459ca5d37babbc2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
yt=load('dianqi.txt');   %实际销售额数据以列向量的方式存放在纯文本文件中
n=length(yt); alpha=[0.2 0.5 0.8]; m=length(alpha);
yhat(1,[1:m])=(yt(1)+yt(2))/2;
for i=2:n
    yhat(i,:)=alpha*yt(i-1)+(1-alpha).*yhat(i-1,:);
end
yhat
err=sqrt(mean((repmat(yt,1,m)-yhat).^2)) 
xlswrite('dianqi.xls',yhat) %把预测数据写到Excel文件，准备在word表格中使用
yhat1988=alpha*yt(n)+(1-alpha).*yhat(n,:)
````

</details>

#### ex8_3 · MATLAB · c12493ed

- 归属算法：时间序列方法
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#时间序列方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于时间序列方法中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`a3a2cfbbcb6fcf27f78f68b165ca99f7e10947557e19057c09fa8e4c26c68930`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
yt=load('fadian.txt');  %原始发电总量数据以列向量的方式存放在纯文本文件中
n=length(yt), alpha=0.3; st1(1)=yt(1); st2(1)=yt(1);
for i=2:n
    st1(i)=alpha*yt(i)+(1-alpha)*st1(i-1);
    st2(i)=alpha*st1(i)+(1-alpha)*st2(i-1);
end
xlswrite('fadian.xls',[st1',st2']) %把数据写入表单Sheet1中的前两列
at=2*st1-st2;
bt=alpha/(1-alpha)*(st1-st2);
yhat=at+bt;  %最后的一个分量为1986年的预测值
xlswrite('fadian.xls',yhat','Sheet1','C2') %把预测值写入第3列
str=['C',int2str(n+2)]; %准备写1987年预测值位置的字符串
xlswrite('fadian.xls',at(n)+2*bt(n),'Sheet1',str)%把1987年预测值写到相应位置
````

</details>

#### ex8_6 · MATLAB · 4bd4e81e

- 归属算法：时间序列方法
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#时间序列方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于时间序列方法中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`1b53f53bc8e7499bcff95340c9829083baab5e19c2b3f2a11555758adac936e0`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_6.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
format long g
a=load('jijie.txt');
[m,n]=size(a);
a_mean=mean(mean(a));  %计算所有数据的算术平均值
aj_mean=mean(a);  %计算同季节的算术平均值
bj=aj_mean/a_mean  %计算季节系数
w=1:m;
yhat=w*sum(a,2)/sum(w)  %预测下一年的年加权平均值,这里是求行和
yjmean=yhat/n  %计算预测年份的季节平均值
yjhat=yjmean*bj  %预测年份的季节预测值
format   %恢复默认的显示格式
````

</details>

#### ex8_7 · MATLAB · 9f7d97f2

- 归属算法：时间序列方法
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#时间序列方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于时间序列方法中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`73c38fea171eb9415b96c51185a57abff420f2e1ae9137269753faa56b5cff70`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_7.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
elps=randn(10000,1); x(1:2)=0;
for i=3:10000
    x(i)=-0.6*x(i-1)-0.2*x(i-2)+elps(i); %产生模拟数据
end
xlswrite('data1.xls',x(end-9:end)) %把x的后10个数据保存到Excel文件中
dlmwrite('mydata.txt',x)  %供下面例8.13的GARCH模型使用同样的数据
x=x'; m=ar(x,2)   %进行参数估计
xp1=predict(m,[x;0],1);  %1步预测，样本数据必须为列向量,要预测1个值，x后要加1个任意数，1步预测数据使用到t-1步的数据
x10001=xp1{1}(end)  %预测第10001个值,为xp1的最后一个值
xp2=predict(m,[x;x10001;0],1); %已知数据后要加1个任意数
x10002=xp2{1}(end)  %预测第10002个值，为xp2的最后一个值
xp3=predict(m,[x;x10001;x10002;0],1); %已知数据后要加1个任意数
x10003=xp3{1}(end)  %预测第10003个值，为xp3的最后一个值
````

</details>

### 未标注例程·预测与推断 · 实现

#### Pex11_1 · Python · 2b50fca2

- 归属算法：未标注例程·预测与推断
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#未标注例程·预测与推断 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·预测与推断中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4efc7be504c33e02d60f9dce29046d076750d12cb514e4cfa5cebd10900d9b6e`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pex11_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex11_1.py
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
x0=np.array([[1.24,1.27], [1.36,1.74], [1.38,1.64], [1.38,1.82], [1.38,1.90], [1.40,1.70],
    [1.48,1.82], [1.54,1.82], [1.56,2.08], [1.14,1.78], [1.18,1.96], [1.20,1.86],
    [1.26,2.00], [1.28,2.00], [1.30,1.96]])   #输入已知样本数据
x=np.array([[1.24,1.80], [1.28,1.84], [1.40,2.04]])  #输入待判样本点数据
g=np.hstack([np.ones(9),2*np.ones(6)])  #g为已知样本数据的类别标号
v=np.cov(x0.T)  #计算协方差
knn=KNeighborsClassifier(2,metric='mahalanobis',metric_params={'V': v}) #马氏距离分类
knn.fit(x0,g); pre=knn.predict(x); print("马氏距离分类结果：",pre)
print("马氏距离已知样本的误判率为：",1-knn.score(x0,g))
knn2=KNeighborsClassifier(2)  #欧氏距离分类
knn2.fit(x0,g); pre2=knn2.predict(x); print("欧氏距离分类结果：",pre2)
print("欧氏距离已知样本的误判率为：",1-knn2.score(x0,g))
````

</details>

#### 相似实现组 · Python · 6ed53c71

- 归属算法：未标注例程·预测与推断
- 用途：预测与推断
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#未标注例程·预测与推断 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：Pex11_3.py

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·预测与推断中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cafdc18c81f1bcf12f1302021b4ee75385f149f70acdd2ce63d9b49b82d88335`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pex11_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex11_3.py
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
x0=np.array([[1.24,1.27], [1.36,1.74], [1.38,1.64], [1.38,1.82], [1.38,1.90], [1.40,1.70],
    [1.48,1.82], [1.54,1.82], [1.56,2.08], [1.14,1.78], [1.18,1.96], [1.20,1.86],
    [1.26,2.00], [1.28,2.00], [1.30,1.96]])   #输入已知样本数据
x=np.array([[1.24,1.80], [1.28,1.84], [1.40,2.04]])  #输入待判样本点数据
y0=np.hstack([np.ones(9),2*np.ones(6)])  #y0为已知样本数据的类别
clf = LDA()
clf.fit(x0, y0)
print("判别结果为：",clf.predict(x))
print("已知样本的误判率为：",1-clf.score(x0,y0))
````

</details>

##### 变体 2：Pex11_5.py

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·预测与推断中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ac85a5943a0318121e7148ed34b46d8b2edfc5e99f94c1a301b925332cf0b122`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pex11_5.py`

<details>
<summary>展开原始代码</summary>

````python
import numpy as np
from sklearn.naive_bayes import GaussianNB
x0=np.array([[1.24,1.27], [1.36,1.74], [1.38,1.64], [1.38,1.82], [1.38,1.90], [1.40,1.70],
    [1.48,1.82], [1.54,1.82], [1.56,2.08], [1.14,1.78], [1.18,1.96], [1.20,1.86],
    [1.26,2.00], [1.28,2.00], [1.30,1.96]])   #输入已知样本数据
x=np.array([[1.24,1.80], [1.28,1.84], [1.40,2.04]])  #输入待判样本点数据
y0=np.hstack([np.ones(9),2*np.ones(6)])  #y0为已知样本数据的类别
clf = GaussianNB()
clf.fit(x0, y0)
print("判别结果为：",clf.predict(x))
print("已知样本的误判率为：",1-clf.score(x0,y0))
````

</details>

### 灰色预测GM · 实现

使用少量样本的累加生成与白化方程进行趋势预测。

#### 灰色预测MATLAB程序 · MATLAB · ac1c557a

- 归属算法：灰色预测GM
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#灰色预测GM · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于灰色预测GM中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `gm1`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`10f8c4f6ec283d118c26ba49dc03231155fa535bf72608e58762adf3e1251d0c`
- 语言：MATLAB
- 符号：`gm1`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/灰色预测/灰色预测MATLAB程序.txt`

<details>
<summary>展开原始代码</summary>

````matlab
灰色预测模型matlab程序 (2007-05-31 11:02:49) 
标签：灰色模型 gm(1 1) 二次拟合 matlab   分类：技术点滴 

%by allen @ 红嘴海鸥 
%灰色模型预测是在数据不呈现一定规律下可以采取的一种建模和预测方法，其预测数据与原始数据存在一定的规律相似性

%下面程序是灰色模型GM(1,1)程序二次拟合和等维新陈代谢改进预测程序,matlab6.5 ,使用本程序请注明，程序存储为gm1.m

%x = [5999,5903,5848,5700,7884];gm1(x);  测试数据 

%二次拟合预测GM(1,1)模型
function  gmcal=gm1(x)
sizexd2 = size(x,2);
%求数组长度

k=0;
for y1=x
    k=k+1;
    if k>1
        x1(k)=x1(k-1)+x(k);
        %累加生成
        z1(k-1)=-0.5*(x1(k)+x1(k-1));   
        %z1维数减1，用于计算B
        yn1(k-1)=x(k);
    else
        x1(k)=x(k);
    end
end
%x1,z1,k,yn1

sizez1=size(z1,2);
%size(yn1);
z2 = z1';
z3 = ones(1,sizez1)';

YN = yn1';   %转置
%YN

B=[z2 z3];
au0=inv(B'*B)*B'*YN;
au = au0';
%B,au0,au

afor = au(1);
ufor = au(2);
ua = au(2)./au(1);
%afor,ufor,ua 
%输出预测的  a u 和 u/a的值

constant1 = x(1)-ua;
afor1 = -afor;
x1t1 = 'x1(t+1)';
estr = 'exp';
tstr = 't';
leftbra = '(';
rightbra = ')';
%constant1,afor1,x1t1,estr,tstr,leftbra,rightbra

strcat(x1t1,'=',num2str(constant1),estr,leftbra,num2str(afor1),tstr,rightbra,'+',leftbra,num2str(ua),rightbra)
%输出时间响应方程

%******************************************************
%二次拟合

k2 = 0;
for y2 = x1
    k2 = k2 + 1;
    if k2 > k  
    else
        ze1(k2) = exp(-(k2-1)*afor);  
    end
end
%ze1

sizeze1 = size(ze1,2);
z4 = ones(1,sizeze1)';
G=[ze1' z4];
X1 = x1';
au20=inv(G'*G)*G'*X1;
au2 = au20';
%z4,X1,G,au20

Aval = au2(1);
Bval = au2(2);
%Aval,Bval
%输出预测的  A,B的值

strcat(x1t1,'=',num2str(Aval),estr,leftbra,num2str(afor1),tstr,rightbra,'+',leftbra,num2str(Bval),rightbra)
%输出时间响应方程

nfinal = sizexd2-1 + 1;
%决定预测的步骤数5  这个步骤可以通过函数传入

%nfinal = sizexd2 - 1 + 1;
%预测的步骤数 1

for  k3=1:nfinal
    x3fcast(k3) = constant1*exp(afor1*k3)+ua;
end
%x3fcast
%一次拟合累加值

for  k31=nfinal:-1:0
    if k31>1
        x31fcast(k31+1) = x3fcast(k31)-x3fcast(k31-1);
    else
        if k31>0
            x31fcast(k31+1) = x3fcast(k31)-x(1);
        else
            x31fcast(k31+1) = x(1);
        end
    end
   
end
x31fcast
%一次拟合预测值


for  k4=1:nfinal
    x4fcast(k4) = Aval*exp(afor1*k4)+Bval;
end
%x4fcast

for  k41=nfinal:-1:0
    if k41>1
        x41fcast(k41+1) = x4fcast(k41)-x4fcast(k41-1);
    else
        if k41>0
            x41fcast(k41+1) = x4fcast(k41)-x(1);
        else
            x41fcast(k41+1) = x(1);
        end
    end
   
end
x41fcast,x
%二次拟合预测值

%***精度检验p C************//////////////////////////////////
k5 = 0;
for y5 = x
    k5 = k5 + 1;
    if k5 > sizexd2  
    else
        err1(k5) = x(k5) - x41fcast(k5);  
    end
end
%err1
%绝对误差


xavg = mean(x);
%xavg
%x平均值

err1avg = mean(err1);
%err1avg
%err1平均值

k5 = 0;
s1total = 0 ;
for y5 = x
    k5 = k5 + 1;
    if k5 > sizexd2  
    else
        s1total = s1total + (x(k5) - xavg)^2;  
    end
end
s1suqare = s1total ./ sizexd2;
s1sqrt = sqrt(s1suqare);
%s1suqare,s1sqrt
%s1suqare  残差数列x的方差  s1sqrt 为x方差的平方根S1

k5 = 0;
s2total = 0 ;
for y5 = x
    k5 = k5 + 1;
    if k5 > sizexd2  
    else
        s2total = s2total + (err1(k5) - err1avg)^2;  
    end
end
s2suqare = s2total ./ sizexd2;
%s2suqare   残差数列err1的方差S2

Cval = sqrt(s2suqare ./ s1suqare);
Cval
%nnn = 0.6745 * s1sqrt
%Cval  C检验值

k5 = 0;
pnum = 0 ;
for y5 = x
    k5 = k5 + 1;
    if abs( err1(k5) - err1avg ) < 0.6745 * s1sqrt
        pnum = pnum + 1;
        %ppp = abs( err1(k5) - err1avg )     
    else
    end
end
pval = pnum ./ sizexd2;
pval
%p检验值

%arr1 = x41fcast(1:6)


%预测结果为区间范围  预测步长和数据长度可调整程序参数进行改进

 

----------程序为原创，引用请注明
````

</details>

#### 灰色预测算法代码 · MATLAB · cc673c84

- 归属算法：灰色预测GM
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#灰色预测GM · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于灰色预测GM中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`511876bdf4ad9fe07bac643604afd11362703afa5387f6db846ee2ac545e6e5a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/灰色预测算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
灰色预测步骤
（1）输入前期的小样本数据
（2）输入预测个数
（3）运行
y=input('请输入数据');
n=length(y);
yy=ones(n,1);
yy(1)=y(1);
for i=2:n
    yy(i)=yy(i-1)+y(i)
end
B=ones(n-1,2);
for i=1:(n-1)
    B(i,1)=-(yy(i)+yy(i+1))/2;
    B(i,2)=1;
end
BT=B';
for j=1:(n-1)
    YN(j)=y(j+1);
end
YN=YN';
A=inv(BT*B)*BT*YN;
a=A(1);
u=A(2);
t=u/a;
t_test=input('输入需要预测的个数');
i=1:t_test+n;
yys(i+1)=(y(1)-t).*exp(-a.*i)+t;
yys(1)=y(1);
for j=n+t_test:-1:2
    ys(j)=yys(j)-yys(j-1);
end
x=1:n;
xs=2:n+t_test;
yn=ys(2:n+t_test);
plot(x,y,'^r',xs,yn,'*-b');
det=0;
for i=2:n
    det=det+abs(yn(i)-y(i));
end
det=det/(n-1);
disp(['百分绝对误差为：',num2str(det),'%']);
    disp(['预测值为：',num2str(ys(n+1:n+t_test))]);
````

</details>

### 预测与时间序列 · 实现

#### example1_1 · SAS · f8540a61

- 归属算法：预测与时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于预测与时间序列中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e0abb16176d8bab39c5b46c5880013bf803eae764310f819dff0847ab33049c3`
- 语言：SAS
- 符号：`PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第一章/example1_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data  example1_1;                                                                                                                         
input  time  monyy7.  price;                                                                                                            
format  time  monyy5.;                                                                                                                  
cards;                                                                                                                                  
Jan2005      101                                                                                                                        
Feb2005      82                                                                                                                         
Mar2005      66                                                                                                                         
Apr2005      35                                                                                                                         
May2005      31                                                                                                                         
Jun2005      7                                                                                                                          
;                                                                                                                                       
Run;
proc  print  data=example1_1;                                                                                                             
Run;  
````

</details>

#### example1_2 · SAS · 2fa257b0

- 归属算法：预测与时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于预测与时间序列中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7c3bfb2f7e0ea9ec2000c4ef022ee9aa3d49b3994f51ad9650c3aa69116e9ed7`
- 语言：SAS
- 符号：`PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第一章/example1_2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example1_2;
input price ; 
time=intnx('month','01jan2005'd,_n_-1);
format time monyy.;
cards;
3.41                                                                                                                      
3.45                                                                                                                      
3.42                                                                                                                      
3.53                                                                                                                      
3.45                                                                                                                      
;                                                                                                                                       
proc print data= example1_2 ;                                                                                                                     
run;
````

</details>

#### example1_3 · SAS · 183adc9b

- 归属算法：预测与时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于预测与时间序列中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3f17234483088b6eebe0a7943b1fb9d92d82a74e2f342254e2ca9ea584b8a7e6`
- 语言：SAS
- 符号：`PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第一章/example1_3.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example1_3;
input price ; 
lotprice=log(price);
time=intnx('month','01jan2005'd,_n_-1);
format time monyy.;
cards;
3.41                                                                                                                      
3.45                                                                                                                      
3.42                                                                                                                      
3.53                                                                                                                      
3.45                                                                                                                      
;                                                                                                                                       
proc print data= example1_3 ;                                                                                                                     
run;
````

</details>

#### example1_4 · SAS · 176ee738

- 归属算法：预测与时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于预测与时间序列中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6b33dc5d0fa70ec56bc2ed26f2667161b33c9881d6d757c1b007e823b31f0609`
- 语言：SAS
- 符号：`PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第一章/example1_4.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example1_4;                                                                                                             
set example1_3;    
keep time logprice;                                                                                                                              
where time>='01mar2005'd;                                                                                                    
proc print data= example1_4;                                                                                                                      
run;
````

</details>

#### example1_5 · SAS · 07aa40ad

- 归属算法：预测与时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于预测与时间序列中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC EXPAND`、`PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d9b5a61ac672ee67ebe2dd9d01d5152be8b7efe796c73260f1afb583db2ab392`
- 语言：SAS
- 符号：`PROC EXPAND`, `PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第一章/example1_5.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example1_5;
input price ; 
time=intnx('month','01jan2005'd,_n_-1);
format time date.;
cards;
3.41                                                                                                                      
3.45                                                                                                                      
.                                                                                                                     
3.53                                                                                                                      
3.45                                                                                                                      
;  
proc expand data= example1_5 out= example1_6;
id time;                                                                                                                                     
proc print data= example1_5;
proc print data= example1_6;                                                                                                                       
run;
````

</details>

#### Pex18_1_1 · Python · 4cebf317

- 归属算法：预测与时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于预测与时间序列中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：优先调用 `MoveAverage`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`dddcae2227cb993337e4753e4dd9874f1ef06070802e0fb9a86a174b73b04b25`
- 语言：Python
- 符号：`MoveAverage`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_1_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_1_1.py
import numpy as np
y=np.array([423,358,434,445,527,429,426,502,480,384,427,446])
def MoveAverage(y,N):
    Mt=['*']*N
    for i in range(N+1,len(y)+2):
        M=y[i-(N+1):i-1].mean()
        Mt.append(M)
    return Mt
yt3=MoveAverage(y,3) 
s3=np.sqrt(((y[3:]-yt3[3:-1])**2).mean())
yt5=MoveAverage(y,5)
s5=np.sqrt(((y[5:]-yt5[5:-1])**2).mean())
print('N=3时,预测值：',yt3,'，预测的标准误差：',s3)
print('N=5时,预测值：',yt5,'，预测的标准误差：',s5)
````

</details>

#### Pex18_1_2 · Python · 34baec8f

- 归属算法：预测与时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测与时间序列中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`505143d8312bf540a75f5f91825fcf584c2b91cfc38076a774d1929446931990`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_1_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_1_2.py
import numpy as np
y=np.array([423,358,434,445,527,429,426,502,480,384,427,446])
n1=3; yt1=np.convolve(np.ones(n1)/n1,y)[n1-1:-n1+1]
s1=np.sqrt(((y[n1:]-yt1[:-1])**2).mean())
n2=5; yt2=np.convolve(np.ones(n2)/n2,y)[n2-1:-n2+1]
s2=np.sqrt(((y[n2:]-yt2[:-1])**2).mean())
print('N=3时,预测值：',yt1,'，预测的标准误差：',s1)
print('N=5时,预测值：',yt2,'，预测的标准误差：',s2)
````

</details>

#### Pex18_2 · Python · 12801fc8

- 归属算法：预测与时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于预测与时间序列中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：优先调用 `ExpMove`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`664bdbdcca4d678dc5a56b005e8b37ba2e3ed4642acd5cbb04b7fb34f62299b1`
- 语言：Python
- 符号：`ExpMove`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_2.py
import numpy as np
import pandas as pd
y=np.array([4.81,4.8,4.73,4.7,4.7,4.73,4.75,4.75,5.43,5.78,5.85])
def ExpMove(y,a):
    n=len(y); M=np.zeros(n); M[0]=(y[0]+y[1])/2;
    for i in range(1,len(y)):
        M[i]=a*y[i-1]+(1-a)*M[i-1]
    return M
yt1=ExpMove(y,0.2); yt2=ExpMove(y,0.5)
yt3=ExpMove(y,0.8); s1=np.sqrt(((y-yt1)**2).mean())
s2=np.sqrt(((y-yt2)**2).mean())
s3=np.sqrt(((y-yt3)**2).mean())
d=pd.DataFrame(np.c_[yt1,yt2,yt3])
f=pd.ExcelWriter("Pdata18_2.xlsx");
d.to_excel(f); f.close()  #数据写入Excel文件，便于做表
print("预测的标准误差分别为：",s1,s2,s3)  #输出预测的标准误差
yh=0.8*y[-1]+0.2*yt3[-1]
print("下一期的预测值为：",yh)
````

</details>

#### Pex18_3 · Python · d4a6871f

- 归属算法：预测与时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测与时间序列中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`5358fb0a9c8f7d0bdfe190a0a8b0d77cb7a9b6959fdeb96358e00ff0b1b8e513`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_3
import numpy as np
import pandas as pd
y=np.loadtxt('Pdata18_3.txt')
n=len(y); alpha=0.3; yh=np.zeros(n)
s1=np.zeros(n); s2=np.zeros(n)
s1[0]=y[0]; s2[0]=y[0]
for i in range(1,n):
    s1[i]=alpha*y[i]+(1-alpha)*s1[i-1]
    s2[i]=alpha*s1[i]+(1-alpha)*s2[i-1];
    yh[i]=2*s1[i-1]-s2[i-1]+alpha/(1-alpha)*(s1[i-1]-s2[i-1])
at=2*s1[-1]-s2[-1]; bt=alpha/(1-alpha)*(s1[-1]-s2[-1])
m=np.array([1,2])
yh2=at+bt*m
print("预测值为：",yh2)
d=pd.DataFrame(np.c_[s1,s2,yh])
f=pd.ExcelWriter("Pdata18_3.xlsx");
d.to_excel(f); f.close()
````

</details>

#### Pex18_4 · Python · e0f39506

- 归属算法：预测与时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测与时间序列中的“预测与推断”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e3198689a933d7237bfca2f6d1e32e6f09aeb557855e3d5fdc43a3945b9b1666`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_4.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_4
import numpy as np
a=np.loadtxt('Pdata18_4.txt')
m,n=a.shape
amean=a.mean()  #计算所有数据的平均值
cmean=a.mean(axis=0)   #逐列求均值
r=cmean/amean   #计算季节系数
w=np.arange(1,m+1)
yh=w.dot(a.sum(axis=1))/w.sum()  #计算下一年的预测值
yj=yh/n   #计算预测年份的季度平均值
yjh=yj*r  #计算季度预测值
print("下一年度各季度的预测值为：",yjh)
````

</details>

#### 时间序列-滑动平均代码 · MATLAB · ff489cfb

- 归属算法：预测与时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测与时间序列中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4ba1bbb6d800aeb0f197814f5c21df042b54982b87d128058aeb865550858041`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/时间序列-滑动平均代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function [movaver3,movaver5]= moveaver(Y)
%Y:原时间序列
%movaver3,movaver5: 三点/五点滑动平均值
n=length(Y);
%计算三点滑动平均值
movaver3(1)=0;
movaver3(n)=0;
for i=2:(n-1)
    movaver3(i)=(Y(i-1)+Y(i)+Y(i+1))/3;
end
%计算五点滑动平均值
movaver5(1)=0;
movaver5(2)=0;
movaver5(n-1)=0;
movaver5(n)=0;
for i=3:(n-2)
    movaver5(i)=(Y(i-2)+Y(i-1)+Y(i)+Y(i+1)+Y(i+2))/5;
end
end
````

</details>

#### 时间序列-移动平均法代码 · MATLAB · d9d94bdc

- 归属算法：预测与时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测与时间序列 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测与时间序列中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f6bede96882efd620d1ed2f3c2c53fc54d6c405763df134774f5a9163524ab70`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/时间序列-移动平均法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function [floaver3,floaver5]= floataver(Y)
%Y:原时间序列
%floaver3,floaver5: 三点/五点移动平均值
n=length(Y);
%计算三点移动平均值
floaver3(1)=0;
floaver3(2)=0;
floaver3(3)=0;
for i=4:n
    floaver3(i)=(Y(i-1)+Y(i-2)+Y(i-3))/3;
end
%计算五点移动平均值
floaver5(1)=0;
floaver5(2)=0;
floaver5(3)=0;
floaver5(4)=0;
floaver5(5)=0;
for i=6:n
    floaver5(i)=(Y(i-1)+Y(i-2)+Y(i-3)+Y(i-4)+Y(i-5))/5;
end
end
````

</details>

### 预测方法 · 实现

#### 相似实现组 · MATLAB · d99f5284

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：Untitled5.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`219858f5d8345896ee4d9581535e2a5c3dcc48644683e5a1b0834185fd8da141`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/Untitled5.m`

<details>
<summary>展开原始代码</summary>

````matlab
  x1=[3.3	3.4	2.4	3.1	15	5.5	8.5	2.7	2.3	3.5	1.8	9.5	2.15	1.44	12	5.75	1.95	6.5	3.25	2.55	2.75	1.79	1.73	5	3.3	3.25	2.01	15	3.1	3.6	5	3.75	1.7	8	3.1	6.5	17	4.2	15	1.18	2.45	1.4	3.75	2.5	3.75	1.33	1.45	1.57	5.5	7	1.45	1.33	1.55	3.3	3	1.8	1.67	1.67	3.1	3.75	3	2	1.57	1.5];
  x2=[3.4	3.3	3.3	3.4	9	3.8	4.75	3.3	2.9	4.2	3.9	4	3.6	4.2	7	3.8	3.6	3.6	3.6	3.1	3.4	3.86	3.6	4.2	3.43	3.4	3.45	8	3.5	3.8	3.8	3.4	3.5	4.5	3.2	4	8.5	3.75	7	7	3.25	4.5	3.6	3.25	3.3	4.75	4.75	4	3.6	4.5	4	5.25	4	3.3	3.25	3.6	4	4	3.75	3.3	3.5	3.5	4	4.33];
  x3=[2.15	2.15	2.88	2.25	1.12	1.62	1.36	2.55	3.5	1.85	4	1.4	3.1	7.5	1.2	1.6	3.6	1.57	2.1	2.9	2.5	4.82	4.75	1.62	2.33	2.15	4.23	1.14	2.2	1.91	1.65	2	4.5	1.4	2.3	1.53	1.13	1.8	1.17	13	2.88	7.5	1.95	2.8	2	10	6	5.5	1.65	1.36	8	8	6	2.2	2.38	4.33	4.75	4.75	2.1	2	2.2	3.6	5.5	6];
y=0.206919701534323-0.229635122917913*x1+0.445807468587154*x2-0.0323088413825895*x3;

 y
````

</details>

##### 变体 2：Untitled6.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`841a8628bf16bdcf56b8ff621db11a3fbced740eb5579115badc3adb98568545`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/Untitled6.m`

<details>
<summary>展开原始代码</summary>

````matlab
  x1=[2.15	1.62	2.3	1.67	3.3	1.57	2.25	1.36	2.55	3.1	2.38	2.75	2.2	1.7	1.65	2.3	5.5	1.08	1.6	1.67	1.73	1.91	1.36	1.4	3.4	2.45	1.4	1.83	1.29	1.25	2.15	4.2	4.2	1.36	3	1.91	1.44	2.38	2.45	1.44	1.53	2.05	1.4	1.75	2.63	1.95	2.7];
  x2=[3.1	3.8	3.4	3.6	3.1	3.8	3	5	3.4	3.6	3.2	3.2	3.3	3.8	3.8	3.6	4	12	4	4	3.75	3.6	4.75	4	3.1	3.3	4.2	3.6	5.5	5.5	3.1	3.6	3.75	4.75	3.2	3.4	4.33	3.6	3.4	4.5	4.33	3.6	4.2	3.6	3.2	3.25	3.2];
  x3=[3.5	5.5	3	5.25	2.3	6	3.5	7.5	2.63	2.15	3	2.63	3.3	4.75	5	2.8	1.57	19	5.25	4.75	4.5	3.8	8	9.5	2.25	2.8	9	4.2	10	12	3.25	1.83	1.8	8	2.25	4	7	2.75	2.8	6.5	5.5	3.3	7	4.75	2.7	4.2	2.6];
  y=0.206919701534323-0.229635122917913*x1+0.445807468587154*x2-0.0323088413825895*x3;

 y
````

</details>

#### anli15_1 · MATLAB · 64e3508f

- 归属算法：预测方法
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`8031923735a44e62980302111d9c6abed6d3cadbe958a56dde51d42290de4bfe`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/anli15_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=[15.2	 15.9	18.7	22.4	26.9	28.3	30.5
   33.8	 40.4	50.7	58	    66.7	81.2	83.4];
a=a'; a=a(:); a=a'; %把原始数据按照时间顺序展开成一个行向量
Rt=tiedrank(a)  %求原始时间序列的秩
n=length(a); t=1:n; 
Qs=1-6/(n*(n^2-1))*sum((t-Rt).^2)   %计算Qs的值
t=Qs*sqrt(n-2)/sqrt(1-Qs^2)   %计算T统计量的值
t_0=tinv(0.975,n-2)     %计算上alpha/2分位数
b=diff(a)   %求原始时间序列的一阶差分
m=ar(b,2,'ls')  %利用最小二乘法估计模型的参数
bhat=predict(m,[b'; 0],1)  %1步预测，样本数据必须为列向量,要预测1个值，b后要加1个任意数，1步预测数据使用到t-1步的数据
ahat=[a(1),a+bhat{1}']  %求原始数据的预测值，并计算t=15的预测值
delta=abs((ahat(1:end-1)-a)./a)  %计算原始数据预测的相对误差
xlswrite('yu.xls',ahat), xlswrite('yu.xls',delta,'Sheet1','A3') %数据写到Excel文件中，方便word中做表格贴入数据
````

</details>

#### anli15_3 · MATLAB · 80720fe6

- 归属算法：预测方法
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`7794620fd7122ecb13c0c2bc8efa5dbb8f22f154b7d4d3a11cc3294c09675eaf`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/anli15_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=load('jishu.txt');  %把表15.15中的数据保存到纯文本文件jishu.txt中
t=a([1,3],:); t=t(:); %提取时间t数据，并变成列向量，这里t没有顺序
n=a([2,4],:); n=n(:); %提取计算器读数n的数据
xishu=[n.^2,n]; %构造系数阵
ab=xishu\t
n0=4450
that=ab(1)*n0^2+ab(2)*n0
````

</details>

#### ex15_10 · MATLAB · 733b1ff4

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`2d3f944594004fb36861876f33cbbea6a3fc5596c813de67746ab4e3cb7b5f39`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_10.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
format rat  %数据格式是有理分数
fid=fopen('msdata.txt','r');
a=[];
while (~feof(fid))
    a=[a fgetl(fid)];  %把所有字符串连接成一个大字符串行向量
end
for i=0:1
    for j=0:1
        s=[int2str(i),int2str(j)]; %构造子字符串‘ij’
        f(i+1,j+1)=length(findstr(s,a));  %计算子串‘ij’的个数
    end
end
fs=sum(f,2);  %求f矩阵的行和
f=f./repmat(fs,1,size(f,2))  %求状态转移频率
````

</details>

#### ex15_11 · MATLAB · 95be474f

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`98ce3e300614463a011d300e58530aebaff27823459f96a70d43dcd3d238fadd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_11.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear, format rat
a=[4  3  2  1  4  3  1  1  2  3 
   2  1  2  3  4  4  3  3  1  1
   1  3  3  2  1  2  2  2  4  4
   2  3  2  3  1  1  2  4  3  1];
a=a'; a=a(:)'; %把矩阵a逐行展开成一个行向量
for i=1:4
   for j=1:4
      f(i,j)=length(findstr([i j],a)); %统计子串‘ij’的个数
   end
end
ni=sum(f,2);  %计算矩阵f的行和
phat=f./repmat(ni,1,size(f,2))  %求状态转移的频率
format %恢复到短小数的显示格式
````

</details>

#### ex15_13_1 · MATLAB · 843c011d

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ed3a60f3ad13af65d5371de15d542afc9a32ba4e8a339af712fe7889e873d5a3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_13_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
format rat  %有理分数的数据格式
p=[0.8 0.1 0.1;0.5 0.1 0.4;0.5 0.3 0.2];
a=[p'-eye(3);ones(1,3)];  %构造方程组ax=b的系数矩阵 
b=[zeros(3,1);1];  %构造方程组ax=b的常数项列
p_limit=a\b  %求方程组的解
format %恢复到短小数的显示格式
````

</details>

#### ex15_13_2 · MATLAB · 1350c3bd

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：进行特征分解以获得权重、主成分或稳定性信息。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`22c82978dd5800ff94007b304cef4e52338f72c865de86e650a617435c31e830`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_13_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
p=[0.8 0.1 0.1;0.5 0.1 0.4;0.5 0.3 0.2];
p=sym(p'); %把p的转置矩阵变成符号矩阵，为了求精确解
[v,d]=eig(p) %求符号矩阵的特征向量矩阵v,特征值矩阵d
d=diag(d); d=double(d); %提取特征值，为了比较大小，把符号值转换成double类型
ind=find(d==max(d));  %求最大特征值的地址
p=v(:,ind)/sum(v(:,ind))  %把最大特征值对应的特征向量化成概率向量
````

</details>

#### ex15_55 · MATLAB · 200862a7

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`576275b0b51518fc9a34f0957b1c00730f64f4f534444b775f99382046ffd69c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_55.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
x1=[3.3	3.4	2.4	3.1	15	5.5	8.5	2.7	2.3	3.5	1.8	9.5	2.15	1.44	12	5.75	1.95	6.5	3.25	2.55	2.75	1.79	1.73	5	3.3	3.25	2.01	15	3.1	3.6	5	3.5	1.4	3.75	1.7	8	3.1	6.5	17	4.2	15	1.18	1.14	2.45	1.4	3.75	3	2.5	3.75	1.33	1.45	1.57	5.5	1.11	7	1.45	1.33	1.55	1.02	1.22	3.3	2.8	3	1.73	1.8	1.67	1.67	3.1	3.75	1.83	3	1.73	1.73	1.57	1.36	2	1.57	1.5];
x2=[2.775	2.725	3.09	2.825	5.06	2.71	3.055	2.925	3.2	3.025	3.95	2.7	3.35	5.85	4.1	2.7	3.6	2.585	2.85	3	2.95	4.34	4.175	2.91	2.88	2.775	3.84	4.57	2.85	2.855	2.725	2.8	6.75	2.7	4	2.95	2.75	2.765	4.815	2.775	4.085	10	15	3.065	6	2.775	2.84	3.025	2.65	7.375	5.375	4.75	2.625	12	2.93	6	6.625	5	30	9.375	2.75	2.85	2.815	4.25	3.965	4.375	4.375	2.925	2.65	3.95	2.85	4.175	4.175	4.875	6.25	3.55	4.75	5.165];
y=[0.333333333	0.5	1.333333333	0.666666667	0.333333333	0	0.2	2	0	5	1	0.333	1.5	1	0.4	0.333333333	0.5	0.33	2	0.5	2	1	0	0.333333333	0	1	2	0.5	1	0.33	3	10	10	1	2	0.2	0	1	0	0.5	0	2	10	1	3	0	10	0	0.2	4	1	2	0	10	0	1	0.5	1	10	20	0.667	10	0.33	10	2	1	5	1	1	10	1	0	1	10	10	0	0.25	1.33]';
x=[x1' x2'];
      rstool(x,y,'purequadratic')
````

</details>

#### ex15_6_11 · MATLAB · 87e10a61

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`50a7f14d1d78befe273848739313576c91da75ace3be2c057b2d0d8f010bb07d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_6_11.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
x1=[3.3	3.4	2.4	3.1	15	5.5	8.5	2.7	2.3	3.5	1.8	9.5	2.15	1.44	12	5.75	1.95	6.5	3.25	2.55	2.75	1.79	1.73	5	3.3	3.25	2.01	15	3.1	3.6	5	3.5	1.4	3.75	1.7	8	3.1	6.5	17	4.2	15	1.18	1.14	2.45	1.4	3.75	3	2.5	3.75	1.33	1.45	1.57	5.5	1.11	7	1.45	1.33	1.55	1.02	1.22	3.3	2.8	3	1.73	1.8	1.67	1.67	3.1	3.75	1.83	3	1.73	1.73	1.57	1.36	2	1.57	1.5];
x2=[3.4	3.3	3.3	3.4	9	3.8	4.75	3.3	2.9	4.2	3.9	4	3.6	4.2	7	3.8	3.6	3.6	3.6	3.1	3.4	3.86	3.6	4.2	3.43	3.4	3.45	8	3.5	3.8	3.8	3.6	4	3.4	3.5	4.5	3.2	4	8.5	3.75	7	7	7	3.25	4.5	3.6	3.3	3.25	3.3	4.75	4.75	4	3.6	9	4.5	4	5.25	4	19	5.75	3.3	3	3.25	3.5	3.6	4	4	3.75	3.3	3.4	3.5	3.75	5	3.5	4	4.33];
x3=[2.15	2.15	2.88	2.25	1.12	1.62	1.36	2.55	3.5	1.85	4	1.4	3.1	7.5	1.2	1.6	3.6	1.57	2.1	2.9	2.5	4.82	4.75	1.62	2.33	2.15	4.23	1.14	2.2	1.91	1.65	2	9.5	2	4.5	1.4	2.3	1.53	1.13	1.8	1.17	13	23	2.88	7.5	1.95	2.38	2.8	2	10	6	5.5	1.65	15	1.36	8	8	6	41	13	2.2	2.7	2.38	5	4.33	4.75	4.75	2.1	2	4.5	2.2	6	7.5	3.6	5.5	6];
y=[0.333333333	0.5	1.333333333	0.666666667	0.333333333	0	0.2	2	0	5	1	0.333	1.5	1	0.4	0.333333333	0.5	0.33	2	0.5	2	1	0	0.333333333	0	1	2	0.5	1	0.33	3	10	10	1	2	0.2	0	1	0	0.5	0	2	10	1	3	0	10	0	0.2	4	1	2	0	10	0	1	0.5	1	10	20	0.667	10	0.33	10	2	1	5	1	1	10	1	0	1	10	10	0	0.25	1.33]';
x=[x1' x2' x3'];
      rstool(x,y,'purequadratic')
````

</details>

#### ex15_6_2 · MATLAB · bc138d46

- 归属算法：预测方法
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`3961fc997120c9a10763a43031dbe9803c12934ef2cd88878c2b12c25f91f28e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_6_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
load xydata
rstool(x123,Y)
````

</details>

#### ex15_8_1 · MATLAB · 05908eda

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e64c9a64e9619b717733d95cb9ad4d05217fb792faf6cabd824645fd0954604f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_8_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=[[1:5]',ones(5,1)];y=[11 12 13 15 16]';z=x\y
````

</details>

#### ex15_8_2 · MATLAB · 092f5024

- 归属算法：预测方法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`41d2a279f454829d61e17a18f4cb96dd9d996290f1dee2c3ab284663f9998d45`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_8_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
y0=[11 12 13 15 16]';
y=y0(3:5);x=[y0(2:4),y0(1:3),ones(3,1)];
z=x\y
````

</details>

#### ex15_8_3 · MATLAB · 7185da45

- 归属算法：预测方法
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c1fe25b11cb4c815b40f253695c6b936fd690df0414e94c0e8cf1a7e9e66edb8`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_8_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
y0=[11 16 25 12 12 18 26 14 13 20 27 15 15 24 30 15 16 25 32 17]';
y=y0(9:20);
x=[y0(5:16),y0(1:12),ones(12,1)];
z=x\y
for t=21:25
    y0(t)=z(1)*y0(t-4)+z(2)*y0(t-8)+z(3);
end
yhat=y0(21:25)   %提取t=21,…，25时是预测值
````

</details>

#### ex15_9 · MATLAB · c8a20f0c

- 归属算法：预测方法
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#预测方法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于预测方法中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`940dc166cb6fafc52a9ac4b454b4bda8fa5b46de4f37c2fea5bb1039591ea519`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_9.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
M=600; N=420; p=200; q=2282;
eq=@(x) x^M-(1+q/p)*x^(M-N)+q/p
options=optimset('MaxFunEvals',10000,'MaxIter',1000);
x=fsolve(eq,1.2345,options) %初始值取为1.2345
````

</details>

<!-- END AUTO-INTEGRATED-CODE -->
