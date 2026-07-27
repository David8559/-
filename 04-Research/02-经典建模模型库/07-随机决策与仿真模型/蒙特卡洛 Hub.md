---
type: topic-hub
topic_tag: topic/蒙特卡洛
keywords: [蒙特卡洛, 随机模拟, 抽样统计, 排队论]
tags: [system/topic-hub, topic/蒙特卡洛]
---

# 蒙特卡洛 Hub

<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->
## 复习与调用指南

> [!summary] 阅读顺序
> 先用“快速选择”确定算法，再读复习卡掌握思想和步骤，最后跳到实现区选择代码。源码默认折叠；数据明细不在复习页展开。

### 快速选择

| 算法或用途 | 主要解决什么 | 独立实现 | 语言 |
|---|---|---:|---|
| [[#Monte Carlo · 复习|Monte Carlo]] | 用随机抽样估计难以解析计算的概率、积分或风险。 | 65 | MATLAB, Python |
| [[#仿真与随机模型 · 复习|仿真与随机模型]] | 该组实现围绕“仿真与随机模型”完成建模计算或辅助处理。 | 10 | MATLAB |
| [[#元胞自动机 · 复习|元胞自动机]] | 用局部规则模拟离散空间中的整体演化。 | 17 | MATLAB |
| [[#排队论 · 复习|排队论]] | 估计随机到达与随机服务系统的等待和拥堵。 | 1 | MATLAB |

### 逐算法复习卡

#### Monte Carlo · 复习

- **解决什么**：用随机抽样估计难以解析计算的概率、积分或风险。
- **核心思想**：大数定律保证样本统计量趋近目标量。
- **标准流程**：定义随机输入 → 设计采样 → 重复仿真 → 汇总均值/分位数/置信区间 → 收敛检查。
- **何时调用**：解析解困难但单次仿真可计算时使用。
- **最易出错**：固定随机种子、报告样本量和置信区间，避免只给一次结果。
- **库内覆盖**：65 个独立实现、65 个原始来源；语言：MATLAB, Python；其中 11 个识别到函数/类型入口。
- **优先阅读**：[[#montec2var · MATLAB · 17c2a205|montec2var]]、[[#montec2vvar · MATLAB · db69a59c|montec2vvar]]、[[#ex2_6 · MATLAB · af56847e|ex2_6]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#Monte Carlo · 实现|跳转到源码实现区]]

#### 仿真与随机模型 · 复习

- **解决什么**：该组实现围绕“仿真与随机模型”完成建模计算或辅助处理。
- **核心思想**：通过输入、核心变换/求解器和输出三部分理解代码，而不是依赖原文件夹名称。
- **标准流程**：确认问题类型 → 找入口与参数 → 理清核心计算 → 运行最小样例 → 检验输出。
- **何时调用**：先阅读下方代码理解卡，再选择函数型实现；脚本型实现应先重构参数。
- **最易出错**：自动总结只能用于导航，最终调用前仍需做数据、环境和结果验证。
- **库内覆盖**：10 个独立实现、34 个原始来源；语言：MATLAB；其中 10 个识别到函数/类型入口。
- **优先阅读**：[[#相似实现组 · MATLAB · 9de76572|create_entry]]、[[#相似实现组 · MATLAB · 83a55d96|create_plaza]]、[[#move_forward · MATLAB · 31573d2c|move_forward]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#仿真与随机模型 · 实现|跳转到源码实现区]]

#### 元胞自动机 · 复习

- **解决什么**：用局部规则模拟离散空间中的整体演化。
- **核心思想**：网格状态按邻域规则同步或异步更新。
- **标准流程**：定义网格/状态 → 设邻域 → 写转移规则 → 迭代 → 统计宏观模式 → 参数实验。
- **何时调用**：传播、交通、生态和空间涌现问题。
- **最易出错**：边界条件、更新顺序和网格尺度会改变结果。
- **库内覆盖**：17 个独立实现、20 个原始来源；语言：MATLAB；其中 8 个识别到函数/类型入口。
- **优先阅读**：[[#move_forward · MATLAB · 27e8730c|move_forward]]、[[#new_cars · MATLAB · bb5fd788|new_cars]]、[[#show_plaza · MATLAB · 5b82e0d9|show_plaza]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#元胞自动机 · 实现|跳转到源码实现区]]

#### 排队论 · 复习

- **解决什么**：估计随机到达与随机服务系统的等待和拥堵。
- **核心思想**：用到达率、服务率、服务台数及稳态分布刻画队列。
- **标准流程**：检验分布假设 → 计算利用率 → 选M/M/1等模型 → 求队长/等待 → 仿真验证。
- **何时调用**：服务系统存在随机等待且关注容量配置时使用。
- **最易出错**：必须先检查稳定条件，现实到达/服务分布可能不满足指数假设。
- **库内覆盖**：1 个独立实现、1 个原始来源；语言：MATLAB；其中 1 个识别到函数/类型入口。
- **优先阅读**：[[#排队论算法代码 · MATLAB · 9242c0d2|排队论算法代码]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#排队论 · 实现|跳转到源码实现区]]

### 通用调用检查表

1. 先确认当前问题是否满足复习卡中的适用条件。
2. 优先选择标有函数/类型入口的实现，脚本型代码先重构参数。
3. 用最小样例跑通，再替换为项目输入；不要一开始就接入完整题目。
4. 检查目标方向、变量单位、边界条件、随机种子和软件版本。
5. 保存运行环境、参数、结果与检验，验证通过后再进入项目正式代码。

<!-- END AUTO-HUB-STUDY-GUIDE -->

> 自动更新：2026-07-27 · 匹配笔记：8

## 相关笔记

- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/2020-B题-获奖论文横向对比]] — 相关度 4
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B108-论文拆解]] — 相关度 4
- [[04-Research/04-竞赛真题研究/01-全国大学生数学建模竞赛/2020-B题-穿越沙漠/2020-B题-穿越沙漠-题目总览]] — 相关度 3
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B078-论文拆解]] — 相关度 3
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2021-C题-生产企业原材料订购与运输/2021-C题-本地解答与四篇国奖论文对照复盘]] — 相关度 3
- [[04-Research/03-建模算法源码库/代码资料索引]] — 相关度 2
- [[04-Research/04-竞赛真题研究/01-全国大学生数学建模竞赛/2020-B题-穿越沙漠/2020-B题-B078第四关地图与邻接关系]] — 相关度 1
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B078-多人博弈建模思路]] — 相关度 1

## 邻接主题

- [[Topic Index]]
- [[模型检验 Hub]]
- [[数据处理 Hub]]
- [[微分方程动力学 Hub]]

<!-- BEGIN AUTO-INTEGRATED-CODE -->
## 源码实现库（按需调用）

> [!warning] 使用边界
> 以下源码保留全文与来源，但默认均未运行验证。数据依赖明细已从阅读页省略；调用时按代码理解卡完成参数化、最小样例和结果检验。来源显示为可复制路径，不直接调用 Windows 打开未知扩展名。

- 本 Hub 收录原始源码文件：120
- 精确去重后的独立实现：93
- 合并后的实现组：88

### 实现索引

| 算法或用途 | 独立实现 | 原始源码 |
|---|---:|---:|
| [[#Monte Carlo · 实现|Monte Carlo]] | 65 | 65 |
| [[#仿真与随机模型 · 实现|仿真与随机模型]] | 10 | 34 |
| [[#元胞自动机 · 实现|元胞自动机]] | 17 | 20 |
| [[#排队论 · 实现|排队论]] | 1 | 1 |

### Monte Carlo · 实现

通过随机抽样估计概率、期望、风险或复杂系统输出。

#### ex2_5 · MATLAB · 82e1033b

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`a0f714a7b8bf5db47404be66a089a038a2208a6707abe3f147bc1cc58e229a3d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/02第2章/ex2_5.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
x=unifrnd(0,12,[1,10000000]);
y=unifrnd(0,9,[1,10000000]);
pinshu=sum(y<x.^2 & x<=3)+sum(y<12-x & x>=3);
area_appr=12*9*pinshu/10^7
````

</details>

#### ex2_6 · MATLAB · af56847e

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`2d1a96efae2b622b116f584f5240bfd942d23bfefd90611921802a91baa30a88`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/02第2章/ex2_6.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/02第2章/mengte.m`

<details>
<summary>展开原始代码</summary>

````matlab
rand('state',sum(clock));  %初始化随机数发生器
p0=0;
tic    %计时开始
for i=1:10^6
   x=randint(1,5,[1,99]); %产生一行五列的区间[1,99]上的随机整数
   [f,g]=mengte(x);
   if all(g<=0)
       if p0<f
           x0=x; p0=f; %记录下当前较好的解
       end
   end
end
x0,p0
toc    %计时结束
````

</details>

#### mengte · MATLAB · fb8cbe23

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1f9fc1588757654c6db8ac45e86ec01f203a563b1fc76239005f98295f74ebd4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/02第2章/mengte.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [f,g]=mengte(x);
f=x(1)^2+x(2)^2+3*x(3)^2+4*x(4)^2+2*x(5)-8*x(1)-2*x(2)-3*x(3)-...
x(4)-2*x(5);
g=[sum(x)-400
x(1)+2*x(2)+2*x(3)+x(4)+6*x(5)-800
2*x(1)+x(2)+6*x(3)-200
x(3)+x(4)+5*x(5)-200];
````

</details>

#### exA_36 · MATLAB · 3c431be7

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`ddcb5595a7391afffd83a92f3c075791a14fe554da9e6ebec4ce32fb39dcf4ab`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/16附录A/exA_36.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
for i=1:10
    str=['jpg',int2str(i),'.jpg'];
    a(:,:,1)=rand(500); a(:,:,2)=rand(500)+100; a(:,:,3)=rand(500)+200;
    imwrite(a,str);
end
````

</details>

#### ConfidenceIntervalInMC · MATLAB · 87f338f7

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`2494f0f2ff33c4e2e2966cd4f24bf31c5723c7b6d56ab5152dab894a14a9734a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/LakeArea/ConfidenceIntervalInMC.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/LakeArea/EstimateAreaMC.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% Clear the environment
clear all;
close all;

%% Select a method
% 3 Choices : standard merssone twister (rand function), halton sequences ,
% or Sobol sequences

Method = 'Standard'; 

%% Create a Random Polygon
maxsize = 100;
NbMaxPoints = 8;

[xpoly, ypoly , h] =CreateConvexPolygon(maxsize,NbMaxPoints);

%% Compute tis real area using MATLAB function
disp(['Area of the polygon is ' num2str(polyarea(xpoly,ypoly)) ]);


%%
NbSimu = (10000 : 10000 : 50000)';
NbIter = numel(NbSimu);
CI   = zeros(NbIter,2);
Area = zeros(NbIter,1);
Time = zeros(NbIter,1);
CI_bis = zeros(NbIter,2);
StdUniforme = (1/12) * 100*100;
%%
for i = 1 : NbIter
    tic;
    [Area(i),CI(i,:)] = EstimateAreaMC(xpoly,ypoly,maxsize,NbSimu(i) ,100, Method,false);
    RelativePercent = 100 * (CI(i,2) - CI(i,1)) ./ (2 * Area(i));
    disp(['Computing with '   num2str(NbSimu(i)) ' simulations, and estimated Area is ' num2str(Area(i)) ' , + or - ' num2str(RelativePercent) '% at 95% confidence']);
    Time(i)= toc;
end

%% Display the results with the confidence interval
h = figure;
color = [0 1 0];
FaceAlpha = 0.4;


FillBetween(NbSimu,CI(:,1),CI(:,2),color,FaceAlpha);
hold on;
plot(NbSimu,Area,'LineWidth',1.5,'Color','r');
plot(NbSimu,repmat(polyarea(xpoly,ypoly),NbIter,1),'LineWidth',1.5,'Color','b');
xlim([NbSimu(1) NbSimu(end)]);
MyLimits = ylim;

%plot(NbSimu,CI,'g');

ylim(gca, [0.98.*min(CI(:,1)) 1.02 .* max(CI(:,2))]);
grid on;


%% Display the simulation time as a function of number of simulation

h3 = figure;
plot(NbSimu,Time);
save('Resultats.mat');
````

</details>

#### CreateConvexPolygon(1) · MATLAB · 93ecdfab

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`dbb202c3a1bd6012440f6216c5445450c827b574d242e15c15370d54e23a5320`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/LakeArea/CreateConvexPolygon(1).m`

<details>
<summary>展开原始代码</summary>

````matlab
function [xpoly, ypoly , h] = CreateConvexPolygon(ContainingSquareWidth,NbPointsMax)
h = figure;

rectangle('Position',[0,0,ContainingSquareWidth,ContainingSquareWidth]);
rand('twister',0);
Points = ContainingSquareWidth * rand(NbPointsMax,2);
K = convhull(Points(:,1),Points(:,2));

xpoly = Points(K,1);
ypoly = Points(K,2);
hold on;

plot(xpoly,ypoly,'-r','LineWidth',2);
````

</details>

#### EstimateAreaMC · MATLAB · 6aeaa6e9

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`889c4cfb0b7b2823bfd17474dc2428dae9b3248e2d04667756844d96fc8fe890`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/LakeArea/EstimateAreaMC.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Area] = EstimateAreaMC(xpoly,ypoly,maxsize,NbPoints,Method,VerboseOutput)

switch Method
    case 'Halton'
        P = haltonset(2);
        RandomPoints = maxsize .* net(P,NbPoints);
        k = 0;
    case 'Sobol'
        P = sobolset(2);
        RandomPoints = maxsize .* net(P,NbPoints);
    case 'Standard'
        RandomPoints = maxsize .* rand(NbPoints,2);
    otherwise
        error('Invalid Method');
end


IN = inpolygon(RandomPoints(:,1),RandomPoints(:,2),xpoly,ypoly);
Area = maxsize .* maxsize * sum(sum(IN)) ./ NbPoints;





hold on;

if (VerboseOutput)
    h = gcf;
    plot(RandomPoints(IN(:,end),end-1),RandomPoints(IN(:,end),end),'g.','LineWidth',1.5);
    plot(RandomPoints(~IN(:,end),end-1),RandomPoints(~IN(:,end),end),'rx','LineWidth',1.5);
    set(h,'WindowStyle','Docked');
    disp(['Area of the Polygon -> ' num2str(polyarea(xpoly,ypoly))]);
    disp(['Estimated Area of the Polygon  -> ' num2str( Area)]);
end
````

</details>

#### MainLakeArea · MATLAB · 2e1cf597

- 归属算法：Monte Carlo
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“数据读取与预处理”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`75c522674eaa66ce4b5cbf195c4057b6a16f8b17818ffeafb5765f08636a744f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/LakeArea/MainLakeArea.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/LakeArea/TestPolyGon.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% First Test With Standard uniform law

close all;
rand('seed',0);
TestPolyGon('Standard');

%% Now try with Halton

rand('seed',0);
TestPolyGon('Halton');

%% Finally with Halton

rand('seed',0);
TestPolyGon('Sobol');
````

</details>

#### TestPolyGon · MATLAB · 6fc37bbb

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `TestPolyGon`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`f6e8995cb71823dd6e61a2483e022b5c94a6e794f28a21a746b84033fe28d7d4`
- 语言：MATLAB
- 符号：`TestPolyGon`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/LakeArea/TestPolyGon.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/LakeArea/EstimateAreaMC.m`

<details>
<summary>展开原始代码</summary>

````matlab
function TestPolyGon(Method)
%% Create a Random Polygon
maxsize = 100;
NbMaxPoints = 8;
[xpoly, ypoly , h] =CreateConvexPolygon(maxsize,NbMaxPoints);
Area= EstimateAreaMC(xpoly,ypoly,maxsize,2500, Method,true)
````

</details>

#### MonteCarlo · MATLAB · bd1bca7e

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`072ceaf785217d4020c4f67e9e7b990e69605ae00fd22a4bafe61ed558777358`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/MyMC/MonteCarlo.m`

<details>
<summary>展开原始代码</summary>

````matlab
┥匠浩汵瑡潩⁮敤洠湯整挠牡潬搠甧⁮捡楴⁦敤爠楰⁸灓瑯ㄠ〰‬敤瘠汯瑡汩瑩෩┊猠杩慭‬瑥搠⁥牤晩⁴湉整敲瑳慒整‮਍‥楖据湥⁴敌汣牥煣‬桔⁥慍桴潗歲ⱳ㈠〰⸷瘠湩散瑮氮捥敬捲䁱慭桴潷歲⹳牦਍汣慥⁲污㭬਍汣獯⁥污㭬਍┥匠慴瑲湩⁧慰慲敭整獲਍楴㭣਍਍䅮瑣晩⁳‽㬲਍潃牲汥瑡潩䵮瑡楲⁸‽ㅛ〠㤮〻㤮ㄠ㭝਍潖獬㴠嬠⸰‵⸰崹഻䐊癩教摬⁳‽せ〠㭝਍瑓牡噴污敵⁳‽ㅛ〰ㄠ〰㭝਍硅䍰癯牡慩据⁥‽潣牲挲癯嘨汯ⱳ䌠牯敲慬楴湯慍牴硩㬩਍桃汯慆瑣牯††‽档汯䔨灸潃慶楲湡散㬩਍਍湉整敲瑳慒整㴠〠〮㬳਍楔敭潔慍畴楲祴㴠〠㔮※‥湩礠慥獲ഠഊ上楓畭慬楴湯†‽〱〰㬰਍卮整獰㴠㈠㬰਍਍┥吠浩⁥瑓灥਍瑄㴠吠浩呥䵯瑡牵瑩⽹卮整獰഻ഊ┊‥敇敮慲整删湡潤⁭畮扭牥൳ഊ唊楮潦割湡潤⁭†††††㴠爠湡⁤⠠卮整獰Ⱐ丠楓畭慬楴湯‬䅮瑣晩⁳㬩਍潃牲汥瑡摥慒摮浯畎扭牥⁳‽敺潲⁳渨瑓灥⁳‬华浩汵瑡潩Ɱ渠捁楴獦⤠഻刊湡潤乭浵敢獲†††††㴠渠牯業癮唨楮潦割湡潤Ɑⰰ⤱഻ഊ┊‥潔匠潴敲琠敨爠獥汵⁴਍਍慐桴⁳‽敺潲⁳渨瑓灥⁳‬华浩汵瑡潩Ɱ渠捁楴獦㬩਍਍┥倠敲敳癲⁥潃牲汥瑡潩⁮潦⁲慥档爠慥楬慳楴湯਍਍潦⁲⁩‽‱›华浩汵瑡潩൮ †潃牲汥瑡摥慒摮浯畎扭牥⁳㨨椬㨬 ‽煳敵穥⡥慒摮浯畎扭牥⡳ⰺⱩ⤺ ‪桃汯慆瑣牯഻攊摮਍਍਍┥਍潦⁲⁩‽‱›䅮瑣晩⁳਍††‥敇敮慲整琠敨搠⁴敲畴湲൳ †倠瑡獨㨨㨬椬 ‽硥⡰⠠湉整敲瑳慒整䐭癩教摬⡳⥩嘭汯⡳⥩㉞㈯⨩瑄⬠嘠汯⡳⥩猪牱⡴瑄⸩‪䌠牯敲慬整剤湡潤乭浵敢獲⠠ⰺⰺ⥩㬩਍††慐桴⡳ⰺⰺ⥩㴠挠浵牰摯倨瑡獨㨨㨬椬Ⱙㄠ㬩਍††慐桴⡳ⰺⰺ⥩㴠倠瑡獨㨨㨬椬 ‪瑓牡噴污敵⡳⥩഻ †┠††††††††††਍湥㭤਍਍┥䌠浯慰敲映牯琠敨映物瑳琠浩⁥瑳灥琠敨匠浩慵瑬潩獮漠⁦桴⁥′獡敳獴਍ㅨ㴠映杩牵㭥汰瑯倨瑡獨ㄨ㨬ㄬⰩ慐桴⡳ⰱ㨠Ⱐ⤲✬⹲⤧഻猊瑥栨ⰱ圧湩潤卷祴敬Ⱗ䐧捯敫❤㬩਍汹浩木慣栨⤱砬楬⥭഻ഊഊ栊′‽楦畧敲瀻潬⡴‱›〲Ⱐ偛瑡獨㨨ㄬⰠ⤱倬瑡獨㨨ㄬⰠ⤲ⱝⴧ⤧഻猊瑥栨ⰲ圧湩潤卷祴敬Ⱗ䐧捯敫❤㬩਍਍潃牲汥瑡潩据敯晦㴠挠牯捲敯⡦慐桴⡳ⰺⰺ⤱倬瑡獨㨨㨬㈬⤩
````

</details>

#### GetOptionPrice · MATLAB · ac3f8553

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b98bb22df791d4c8e6f5b4ec8108a807e8d19869609b01bbc1b5d9d1ed428142`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/PortSim/GetOptionPrice.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Price, ProbaITM , CI] = GetOptionPrice(Paths,Exercise,TimeToExpiry,RiskFreeRate,Optiontype)

switch Optiontype
    case 'Asian'
        
        MeanPrices = mean(Paths,1) ;
        OptionPricesAtMaturity = max(MeanPrices- Exercise,0);
           case 'Vanilla'
        OptionPricesAtMaturity = max(Paths(end,:)- Exercise,0);
       
end;
[MeanPriceAtMaturity, dummy,CI] = normfit(OptionPricesAtMaturity,0.01);
CI                     = CI* exp(-TimeToExpiry * RiskFreeRate);
Price                  = MeanPriceAtMaturity * exp(-TimeToExpiry * RiskFreeRate);
ProbaITM               = 100 * sum(OptionPricesAtMaturity > 0) ./ length(OptionPricesAtMaturity);
````

</details>

#### WebinarScript · MATLAB · 532a5389

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`457e4d05effecdf02b5dcd2f0ae6bef279fdc47fdb59c1ceaef555bb17156731`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/PortSim/WebinarScript.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/PortSim/GetOptionPrice.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% Classic Monte Carlo simualtion
% Vincent Leclercq, The MathWorks, 2007, vincent.leclercq@mathworks.fr
%

clear all;
close all;


NbTrials = 10000;

%RunMode = 'LogNomrality';

RunMode = 'OptionPricing';
%% Load Data (retrieved originally from Thomson Datastream)

load Equities.mat
PastDate = today()-1 * 365;

%% Retrieve the dates in a numeric format

Dates   = cellfun(@(x)(datenum(x,'yyyy-mm-ddTHH:MM:SS')),Equities.DATE);
AssetPrices = cellfun(@(x) (str2double(x)),Equities.P );
    
%% Plot the Series

plot(Dates,AssetPrices);set(gcf,'WindowStyle','Docked');
legend(Equities.DISPNAME);
datetick('x','mmmyy');
xlim([PastDate, today()]);
grid on;


%% Compute the returns
% We can compute the returns for one or many stocks at the same time using
% matrix computation and matlab easy syntax

Suez_Returns = tick2ret(AssetPrices);
DailyVol = std(Suez_Returns);
AnnualVol = DailyVol * sqrt(252);

SpotPrice = AssetPrices(end);

InterestRate = 0.0375;

%% Portfolio simulation (Monte Carlo) using the Financial toolbox function
% For help, one can use the doc portsim function
% We call the portfolio simulation using Financial toolbox to
% simulate 10000 scenarios. Of course, correlation are preserved
% We assume an horizon of 6 * 22 trading days, ie 6 month maturity

%% Using Annual statistics


SimulatedRetsAnnual = portsim(InterestRate,AnnualVol^2, 12, 1/12, NbTrials,'Expected'); % NbStep * TimeStep = 1 (in years !!!)

%% Using Daily statistics
NumberOfSimulationSteps = 12;
SimulatedRetsDaily = portsim(InterestRate./252, DailyVol^2, 12, 252./12, NbTrials,'Expected');% NbStep * TimeStep = 252 (in days!!!)




%% Generate the Prices and plot them

SimulatedPricesAnnual = ret2tick(squeeze(SimulatedRetsAnnual) ,SpotPrice);
SimulatedPricesDaily  = ret2tick(squeeze(SimulatedRetsDaily)  ,SpotPrice );

figure;hist(SimulatedPricesAnnual(end,:),40);title('Prices, annual timestep used');set(gcf,'WindowStyle','Docked');
figure;hist(SimulatedPricesDaily(end,:),40);title('Prices, daily timestep used');set(gcf,'WindowStyle','Docked');

%% Check For LogNormality of the Price series

ExpectedVariance = (SpotPrice^2)  * (exp(AnnualVol^2) - 1)* exp(2*InterestRate);

disp(['Mean Price (Annual Parameters) -> ', num2str(mean(SimulatedPricesAnnual(end,:))) ' , Theoric value (Hull) :' num2str(SpotPrice * exp(InterestRate))]);
disp(['Mean Price (Daily Parameters) -> ', num2str(mean(SimulatedPricesDaily(end,:))) ' , Theoric value (Hull) :' num2str(SpotPrice * exp(InterestRate))]);

disp(['Expected Variance (Annual Parameters) -> ', num2str(var(SimulatedPricesAnnual(end,:))) ' , Theoric value (Hull) :' num2str(ExpectedVariance)]);
disp(['Expected Variance (Daily Parameters) -> ', num2str(var(SimulatedPricesDaily(end,:))) ' , Theoric value (Hull) :' num2str(ExpectedVariance)]);


%% Parameter sweep
% Now that we have done this, we can ccompute the same thing for different
% Exercise prices
if strcmp(RunMode,'OptionPricing')
    k = 1;
    NumberOfSteps = 400;
    ExercisePrices= linspace(0.8 * SpotPrice,1.2 * SpotPrice,NumberOfSteps);


    VanillaPriceAnnual    = zeros(NumberOfSteps,1);
    VanillaPriceDaily    = zeros(NumberOfSteps,1);

    ProbabilityITMAnnual  = zeros(NumberOfSteps,1);
    ProbabilityITMDaily  = zeros(NumberOfSteps,1);
    CIAnnual    =     zeros(NumberOfSteps,2);
    CIDaily     =     zeros(NumberOfSteps,2);
    BLSPrices       = zeros(NumberOfSteps,1);

    %%
    TimeInYear = 1;
    for i = 1 : NumberOfSteps
        [BLSPrices(i),dummy]   = blsprice(SpotPrice, ExercisePrices(i), InterestRate, TimeInYear, AnnualVol, 0);
        [VanillaPriceAnnual(i), ProbabilityITMAnnual(i) ,CIAnnual(i,:)] = GetOptionPrice(SimulatedPricesAnnual,ExercisePrices(i),TimeInYear,InterestRate,'Vanilla');
        [VanillaPriceDaily(i), ProbabilityITMDaily(i) ,  CIDaily(i,:)] = GetOptionPrice(SimulatedPricesDaily,ExercisePrices(i),TimeInYear,InterestRate,'Vanilla');

    end;

%% 
    
    h =    figure;
    [AX,H1,H2] = plotyy(ExercisePrices,[VanillaPriceAnnual BLSPrices CIAnnual] , ExercisePrices,ProbabilityITMAnnual);


    xlabel('Exercise Price');
    title('Option prices for a Vanilla option using a 1 year - Annual volatility');
    Axes_YLabels = get(AX,'Ylabel');
    set(Axes_YLabels{1},'String','Option Price') ;

    set(H1(1),'LineStyle','-');
    set(H1(1),'Color','r');
    set(H1(1),'LineWidth',2);


    set(H1(2),'LineStyle','-');
    set(H1(2),'Color','b');
    set(H1(2),'LineWidth',2);

    set(H1(3),'LineStyle','--');
    set(H1(3),'Color','r');
    set(H1(3),'LineWidth',1);

    set(H1(4),'LineStyle',':');
    set(H1(4),'Color','r');
    set(H1(4),'LineWidth',1);


    set(H2,'LineStyle','-');
    set(H2,'Color','g');
    set(H2,'LineWidth',2);

    set(get(AX(2),'Ylabel'),'String','Probability of being In the Money');
    legend(H1,{['Option Price (Monte Carlo)'], ['Option Price (Black Scholes)'], ['99% Confidence interval (Lower)'],['99% Confidence interval (Upper)']},'Location','NorthEast');
    legend(H1(2),{'Option Price (Black Shcoles)'},'Location','NorthEast');
    legend(H2,{'Probability'},'Location','SouthWest');
    grid on;
set(h,'WindowStyle','Docked');

%%
h=     figure;
    [AX,H1,H2] = plotyy(ExercisePrices,[VanillaPriceDaily BLSPrices CIDaily] , ExercisePrices,ProbabilityITMDaily);


    xlabel('Exercise Price');
    title('Option prices for a Vanilla option using a 1 year - Daily volatility');
    Axes_YLabels = get(AX,'Ylabel');
    set(Axes_YLabels{1},'String','Option Price') ;

    set(H1(1),'LineStyle','-');
    set(H1(1),'Color','r');
    set(H1(1),'LineWidth',2);


    set(H1(2),'LineStyle','-');
    set(H1(2),'Color','b');
    set(H1(2),'LineWidth',2);


    set(H1(3),'LineStyle','--');
    set(H1(3),'Color','r');
    set(H1(3),'LineWidth',1);

    set(H1(4),'LineStyle',':');
    set(H1(4),'Color','r');
    set(H1(4),'LineWidth',1);
    

    set(H2,'LineStyle','-');
    set(H2,'Color','g');
    set(H2,'LineWidth',2);

    set(get(AX(2),'Ylabel'),'String','Probability of being In the Money');
    legend(H1,{['Option Price (Monte Carlo)'], ['Option Price (Black Scholes)'], ['99% Confidence interval (Lower)'],['99% Confidence interval (Upper)']},'Location','NorthEast');
    legend(H2,{'Probability'},'Location','SouthWest');
    grid on;
    set(h,'WindowStyle','Docked');
 end;
````

</details>

#### BlsHalton · MATLAB · 54490db2

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cc43279586adc549623834663bedb9b60e984d6ecb930e88582227732992847b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsHalton.m`

<details>
<summary>展开原始代码</summary>

````matlab
% BlsHalton.m
function [Price , CI]= BlsHalton(S0,X,r,T,sigma,NPoints)
nuT = (r - 0.5*sigma^2)*T;
siT = sigma * sqrt(T);


H = haltonset(1);
HaltonRandomNumbers = net(H,NPoints);

Norm = norminv(HaltonRandomNumbers);
DiscPayoff = exp(-r*T) * max( 0 , S0*exp(nuT+siT*Norm) - X);
[Price, VarPrice, CI] = normfit(DiscPayoff);
````

</details>

#### BlsMC · MATLAB · 2bc24f32

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`969a07109e6e392d375314f87c5cd713709edf3a22c61acc672d9a2d6718c5c5`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsMC.m`

<details>
<summary>展开原始代码</summary>

````matlab
% BlsTMC.m
function [Price, CI] = BlsMC(S0,X,r,T,sigma,NRepl)
nuT = (r - 0.5*sigma^2)*T;
siT = sigma * sqrt(T);
DiscPayoff = exp(-r*T) * max( 0 , S0*exp(nuT+siT*randn(NRepl,1)) - X);
[Price, VarPrice, CI] = normfit(DiscPayoff);
````

</details>

#### BlsMCAV · MATLAB · 5aa3030a

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`286394376e2ffe2b80975bee9a1f255f5ce45939b1a703d45c7bcb10a42d6cc3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsMCAV.m`

<details>
<summary>展开原始代码</summary>

````matlab
% BlsMC.m
function [Price, CI] = BlsMCAV(S0,X,r,T,sigma,NRepl)
nuT = (r - 0.5*sigma^2)*T;
siT = sigma * sqrt(T);
Veps = randn(NRepl,1);
Payoff1 = max( 0 , S0*exp(nuT+siT*Veps) - X);
Payoff2 = max( 0 , S0*exp(nuT+siT*(-Veps)) - X);
DiscPayoff = exp(-r*T) * 0.5 * (Payoff1+Payoff2);
[Price, VarPrice, CI] = normfit(DiscPayoff);
````

</details>

#### BlsMCCV · MATLAB · 5fc8806c

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cff59b0d7c790f9e04e6cee6fd3a91eb8ade81853ac6de6d123165702f58073d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsMCCV.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Price, CI] = BlsMCCV(S0,X,r,T,sigma,NRepl,NPilot)
% Price a vanilla cal using the stock price s a control variable
nuT = (r - 0.5*sigma^2)*T;
siT = sigma * sqrt(T);

%% Compute parameters first 

StockVals = S0*exp(nuT+siT*randn(NPilot,1));
OptionVals = exp(-r*T) * max( 0 , StockVals - X);
MatCov = cov(StockVals, OptionVals);

%% Compute Expected value and Variacne of our control Variable

VarY = S0^2 * exp(2*r*T) * (exp(T * sigma^2) - 1);
ExpY = S0 * exp(r*T);

%% compute the optimal control parameter

c = - MatCov(1,2) / VarY;

% % Compute the MC expected value  
NewStockVals = S0*exp(nuT+siT*randn(NRepl,1));
NewOptionVals = exp(-r*T) * max( 0 , NewStockVals - X);
%% Use the control parameter
ControlVars = NewOptionVals + c * (NewStockVals - ExpY);
[Price, VarPrice, CI] = normfit(ControlVars);
````

</details>

#### BlsSobol · MATLAB · 44e7004e

- 归属算法：Monte Carlo
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b80855f7189a7d3552515aa7909f46fd4a23f0679dbb959dd8c57a8ca91ed9bf`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsSobol.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [price, CI]  = blsSobol(S,E,r,T,sigma,nSims)
% 
%GetSobolVanillaPrice - Vanilla option pricing using simulation and Sobol
% generator
%
% Return the pice of a vanilla option and the standard deviation of the
% price simulated
%
% Inputs:
%   S   	- Current price of the underlying asset.
%
%   E        - Strike (i.e., exercise) price of the option.
%
%   r        - Annualized continuously compounded risk-free rate of return
%                 over the life of the option, expressed as a positive decimal
%                 number.
%
%   T        - Time to expiration of the option, expressed in years.
%
%   sigma    - Annualized asset price volatility (i.e., annualized standard
%                 deviation of the continuously compounded asset return),
%                 expressed as a positive decimal number.
%
%   
%   divYield  - Annualized continuously compounded yield of the underlying
%                 asset over the life of the option, expressed as a decimal
%                 number. If Yield is empty or missing. the default value is
%                 zero.
%
%                 For example, this could represent the dividend yield (annual
%                 dividend rate expressed as a percentage of the price of the
%                 security) or foreign risk-free interest rate for options
%                 written on stock indices and currencies, respectively.
%   nSims      - Number of Simulation used for the pricing
%   nSteps     - Number of time steps used to simulate
%  [SobolPrice,stdSobol] =   GetSobolVanillaPrice(S,E,r,T,sigma,divYield,nsim,nSteps);

Dt = T;

%Generate the random numbers using SOBOL sequences

% Sobol sequences have some zeros
% a common approach in the litterature is to suppress the 64 first points
% the sobol generator has been found on the web

P = sobolset(1);
SobolRandomNumbers = net(P,nSims);


% Sobol numbers are between 0 and  1
% We need to get a normal distribution from this pseudo uniform drawing

RandomNumbers = norminv(SobolRandomNumbers');
mat = exp( (r-sigma^2/2)*Dt + sigma*sqrt(Dt).*RandomNumbers  );
mat = cumprod(mat , 1);
mat = mat.*S;

% Discount and calculate the option price

V = exp(-r*T) * max(mat(end,:)-E , 0);
[price,VarParice,CI]= normfit(V);
````

</details>

#### FillBetween · MATLAB · f58e372a

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `FillBetween`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8452d358e4ddd868f6c2c833ecd8a24c11b9cd122c8b4b54484b89a7c85077e6`
- 语言：MATLAB
- 符号：`FillBetween`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/FillBetween.m`

<details>
<summary>展开原始代码</summary>

````matlab
function FillBetween(Xdata,YLower,YUpper,AreaColor,Alpha)

if size(Xdata) == size(YLower)
    fill([vertcat(Xdata,Xdata(end:-1:1))],[vertcat(YLower,YUpper(end:-1:1))],AreaColor,'FaceAlpha',Alpha);
else
    warning('MATLAB:InvlaidArgumentSize','The size of the input is not consistent');
end
````

</details>

#### VanillaPricingUsingDifferentMethods · MATLAB · 8f05121d

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`7ef47565bad9f23a6efb3b0f7dbf1c5dbcaad63dcbd86afcb307a802200e7aac`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/VanillaPricingUsingDifferentMethods.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsHalton.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsMC.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsMCAV.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsMCCV.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/BlsSobol.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/MonteCarlo/Demos/VarReduction/FillBetween.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear all;
close all;

NbSimu = 20000 : 20000: 200000;
NbPoints = numel(NbSimu);

ResAV =  zeros(NbPoints,1);
ResMC =  zeros(NbPoints,1);
ResMCCV =  zeros(NbPoints,1);
ResSobol = zeros(NbPoints,1);
ResHalton = zeros(NbPoints,1);

CIAV   =  zeros(NbPoints,2);
CIMC   =  zeros(NbPoints,2);
CIMCCV =  zeros(NbPoints,2);
CIQMC  = zeros(NbPoints,2);
CIHalton = zeros(NbPoints,2);


BLprice = blsprice(100,100,0.03,0.25,0.5,0);
%% Run 
for i = 1 :numel(NbSimu)
  disp(['Computing Iteration N°' num2str(i) ' with ' num2str(NbSimu(i)) ' Simulated Paths']);
    [ResAV(i),CIAV(i,:)] =  BlsMCAV(100,100,0.03,0.25,0.5,NbSimu(i));
    [ResMC(i),CIMC(i,:)] =  BlsMC(100,100,0.03,0.25,0.5,NbSimu(i));
    [ResMCCV(i),CIMCCV(i,:)] =  BlsMCCV(100,100,0.03,0.25,0.5,NbSimu(i),1000);
    [ResSobol(i),CIQMC(i,:)] =  BlsSobol(100,100,0.03,0.25,0.5,NbSimu(i));
    [ResHalton(i),CIHalton(i,:)] =  BlsHalton(100,100,0.03,0.25,0.5,NbSimu(i));
end;

%% Display Results
h= figure;
plot(NbSimu,[repmat(BLprice,NbPoints,1) ResAV ResMC ResMCCV ResSobol ResHalton]);
legend({'Black Scholes' 'Antithetic', 'Simple Monte Carlo', 'Monte Carlo with Control Variable', 'Sobol sequences', 'Halton Sequences'});
set(h,'WindowStyle','Docked');
grid on;
xlabel('Number of simuation');
Ylabel('Vanilla option Price');
xlim([NbSimu(1) NbSimu(end)]);
ylim([10 10.5]);
%%
h= figure;
plot(NbSimu,[diff(CIAV,1,2) diff(CIMC,1,2) diff(CIMCCV,1,2) ]);
legend({'Antithetic', 'Simple Monte Carlo', 'Monte Carlo with Control Variable', });
grid on;xlim([NbSimu(1) NbSimu(end)]);
title('Comparing different Monte Carlo methods')
set(h,'WindowStyle','Docked');
xlabel('Number of simuation');
Ylabel('absolute confidence ionterval');
h= figure;
FillBetween(NbSimu',CIMCCV(:,1),CIMCCV(:,2),'g',0.3);
hold on;
plot(NbSimu,ResMCCV,'LineWidth',1.5,'Color','r');
plot(NbSimu,repmat(BLprice,NbPoints,1),'b');
xlim([NbSimu(1) NbSimu(end)])
set(h,'WindowStyle','Docked');
title('Monte Carlo with Control Variable');
xlabel('Number of simulation');
Ylabel('Vanilla option Price');
grid on;
````

</details>

#### montec · MATLAB · 361c2066

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `montec`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`d5b5e129254d165ad256c0f86d3ddf5c51aeb6933f65c72ddc73dd2056e74c2f`
- 语言：MATLAB
- 符号：`montec`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/蒙特卡洛/montec.m`

<details>
<summary>展开原始代码</summary>

````matlab
function I=montec(f,a,b,n)

%I=montec('f',a,b,k);
%Calculates integral using montecarlo method
for k=1:n
    s=2.^k;
    t=rand(1,s);
    x=a+t.*(b-a);

    for i=1:s
        y(i)=feval(f,x(i));
    end

    I(k)=((b-a)./s)*sum(y);
end
plot(I);


   
````

</details>

#### montec2var · MATLAB · 17c2a205

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `montec2var`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`489ce9d7f9c915932fd23ee44affe85b66f7760a605b9146961e6d4604075690`
- 语言：MATLAB
- 符号：`montec2var`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/蒙特卡洛/montec2var.m`

<details>
<summary>展开原始代码</summary>

````matlab
function I=montec2var(g,a,b,c,d,n)

%I=montec2var('g',a,b,c,d,n)
%Calculates doble integral using Montecarlo method (fixed boundaries)
for k=1:n
    s=2.^k;
    t=rand(2,s);
    x=a+t(1,:).*(b-a);			%extremos a,b fijos
    y=c+t(2,:).*(d-c);			%extremos c,d fijos

    for i=1:s
        z(i)=feval(g,x(i),y(i));
    end

    I(k)=(((b-a).*(d-c))./s).*sum(z);
end

plot(I);
````

</details>

#### montec2vvar · MATLAB · db69a59c

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `montec2vvar`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`f8a56eaf36e0970689d6bfce638adbf95998dceaf0e0f3b028ab062621ebca4b`
- 语言：MATLAB
- 符号：`montec2vvar`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/蒙特卡洛/montec2vvar.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/蒙特卡洛/simpson.m`

<details>
<summary>展开原始代码</summary>

````matlab
function I=montec2vvar(g,cx,dx,a,b,c,d,n)

%I=montec2vvar('g',cx,dx,a,b,c,d,n)
%Calculates integral on no rectangular space using monte-carlo method
%a,b, fixed boundaries
%cx,dx, variable boundaries (of x)
%c,d fixed boundaries (of y) that form a rectangular space with a and b
%boundaries.
t=rand(1,n);
u=rand(1,n);
x=a+t.*(b-a);			%extremos a,b fijos
y=c+u.*(d-c);			%extremos c,d variabales

cont=0;
s=0;

for i=1:n
   if (y(i)>feval(cx,x(i))&&y(i)<feval(dx,x(i)))
      cont=cont+1;
      fx=feval(g,x(i),y(i));
      s=s+fx;
   end
end

area=(simpson(dx,a,b,20)-simpson(cx,a,b,20))
I=((area./cont).*s);
````

</details>

#### simpson · MATLAB · cdcc9b94

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`05bdaf86762a246c931e9c5f749b84269a79aff668b6e06efb8d830f0ee571dd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛/蒙特卡洛/simpson.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [i]=simpson(f,a,b,n)

% [i]=simpson(f,a,b,n)
% f: function to integrate
% a,b: Integration interval
% n: Number of subintervals (must be an even number)

h=(b-a)/n			
x=a:h:b;			
y=feval(f,x);		

p(1)=1;
for k=2:2:n
   p(k)=4;
   p(k+1)=2;
end
p(n+1)=1;
p=p.*h/3;
% p: vector de pasos

i=p*y';
````

</details>

#### combat1 · MATLAB · 916f9e2e

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`c5c0a06ca169f7ec744471bab76b70b209a62ec2a706ae4ccbef7d7cecd3de68`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/combat1.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/computing.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/leaveflash.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/personcreat.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/serveflash.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear all
close all


tim0=720;%需要模拟的时间
[num,pass]=computing(tim0);%计算模拟数据

%动画制作
envirment    %场景
title1= annotation('textbox', 'Position',[0.3377 0.8712 0.3348 0.07885],...
  'EdgeColor','none','FitHeightToText','off', 'FontName','Arial','FontSize',16,...
  'FontWeight','bold','String',{'理发店忙闲情况分析'});
time1 = annotation('textbox','Position',[0.02754 0.1019 0.0942 0.06538],...
  'EdgeColor','none','FitHeightToText','off','FontSize',14,'FontWeight','bold',...
  'String',{'时间'});
hour1 = annotation('textbox','Position',[0.1072 0.1038 0.07536 0.06346],...
  'EdgeColor','none','FitHeightToText','off','FontSize',14,...
  'FontWeight','bold','String',{'08：'});
minute1 = annotation('textbox','Position',[0.1493 0.1038 0.07246 0.06538],...
  'EdgeColor','none','FitHeightToText','off', 'FontSize',14,...
  'FontWeight','bold','String',{'10'});
counter1=1;  %时间计数
temp1=1;     %顾客计数
counter=1;
counterxy=zeros(7,2);
tempa=0;
tempb=0;
tempc=0;
tempd=0;
tempe=0;
tempf=0;
tempg=0;
global man1 mana1 mana2 mana3 mana4 mana5
global manb1 manb2 manb3 manb4 manb5
global manc1 manc2 manc3 manc4 manc5
global mand1 mand2 mand3 mand4 mand5
global mane1 mane2 mane3 mane4 mane5
    man1(1,:)=[0.4625 0.1786 0.0982 0.1381];  %[x0 y0 x1 y1]
    man1(2,:)=[0.4875 0.2667 0.5018 0.2667];  %[x0 y0 x1 y1]
    man1(3,:)=[0.5214 0.2667 0.5339 0.2667];  %[x0 y0 x1 y1]
    man1(4,:)=[0.5125 0.25 0.5125 0.23];      %[x0 y0 x1 y1]
    man1(5,:)=[0.4968 0.2081 0.525 0.2072];   %[x0 y0 x1 y1]
axis off    

while  counter1<=100  %时间计数
    %显示时间
    minutex=rem(counter1,60);
    hourx=8+(counter1-minutex)/60;
    set(hour1,'String',{hourx})
    set(minute1,'String',{minutex})
  
    if temp1<=num
        
        %离开与删除人脸对象
        if tempa ~= 0
           if  pass(tempa,6) == counter1
               leaveflash(1,counterxy(1,1),counterxy(1,2))
               tempa=0;
               delete(mana1,mana2,mana3,mana4,mana5);
           end
        end
        if tempb~=0
           if  pass(tempb,6) == counter1
               leaveflash(2,counterxy(2,1),counterxy(2,2))
               tempb=0;
               delete(manb1,manb2,manb3,manb4,manb5);
           end
        end
        if tempc~=0            
           if  pass(tempc,6) == counter1
               leaveflash(3,counterxy(3,1),counterxy(3,2))
               tempc=0;
               delete(manc1,manc2,manc3,manc4,manc5);
           end
        end
        if tempd~=0
           if  pass(tempd,6) == counter1
               leaveflash(4,counterxy(4,1),counterxy(4,2))
               tempd=0;
               delete(mand1,mand2,mand3,mand4,mand5);
           end
        end
        if tempe~=0
           if  pass(tempe,6) == counter1
               leaveflash(5,counterxy(5,1),counterxy(5,2))
               tempe=0;
               delete(mane1,mane2,mane3,mane4,mane5);
           end
        end
        if tempf~=0
           if  pass(tempf,6) == counter1
               leaveflash(6,counterxy(6,1),counterxy(6,2))
               tempf=0;
               delete(manf1,manf2,manf3,manf4,manf5);
           end
        end
        if tempg~=0
           if  pass(tempg,6) == counter1
               leaveflash(7,counterxy(7,1),counterxy(7,2))
               tempg=0;
               delete(mang1,mang2,mang3,mang4,mang5);
           end
        end
         
        %产生人脸
        if pass(temp1,2)==counter1
            if tempa==0
               [mana1,mana2,mana3,mana4,mana5]=personcreat(pass(temp1,3))
               tempa=temp1;
               if pass(temp1,5)==1
                   counterxy(1,:)=[-0.027 0.055];
               end
               if pass(temp1,5)==2
                   counterxy(1,:)=[0 0.055];
               end
               if pass(temp1,5)==3
                   counterxy(1,:)=[0.027 0.055];
               end
               temp1=temp1+1;            
            else
                if tempb==0
                    [manb1,manb2,manb3,manb4,manb5]=personcreat(pass(temp1,3))
                    tempb=temp1;
                    if pass(temp1,5)==1
                        counterxy(2,:)=[-0.027 0.055];
                    end
                    if pass(temp1,5)==2
                        counterxy(2,:)=[0 0.055];
                    end
                    if pass(temp1,5)==3
                        counterxy(3,:)=[0.027 0.055];
                    end
                    temp1=temp1+1;
                else
                    if tempc==0
                        [manc1,manc2,manc3,manc4,manc5]=personcreat(pass(temp1,3))
                        tempc=temp1;
                        if pass(temp1,5)==1
                            counterxy(3,:)=[-0.027 0.055];
                        end
                        if pass(temp1,5)==2
                            counterxy(3,:)=[0 0.055];
                        end
                        if pass(temp1,5)==3
                            counterxy(3,:)=[0.027 0.055];
                        end
                        temp1=temp1+1;
                    else
                        if tempd==0
                            [mand1,mand2,mand3,mand4,mand5]=personcreat(pass(temp1,3))
                            tempd=temp1;
                            if pass(temp1,5)==1
                                counterxy(4,:)=[-0.027 0.055];
                            end
                            if pass(temp1,5)==2
                                counterxy(4,:)=[0 0.055];
                            end
                            if pass(temp1,5)==3
                                counterxy(4,:)=[0.027 0.055];
                            end
                            temp1=temp1+1;
                        else
                            if tempe==0
                                [mane1,mane2,mane3,mane4,mane5]=personcreat(pass(temp1,3))
                                tempe=temp1;  
                                if pass(temp1,5)==1
                                    counterxy(5,:)=[-0.027 0.055];
                                end
                                if pass(temp1,5)==2
                                    counterxy(5,:)=[0 0.055];
                                end
                                if pass(temp1,5)==3
                                    counterxy(5,:)=[0.027 0.055];
                                end
                                temp1=temp1+1;
                            else
                                if tempf==0
                                    [manf1,manf2,manf3,manf4,manf5]=personcreat(pass(temp1,3))
                                    tempf=temp1;  
                                    if pass(temp1,5)==1
                                        counterxy(6,:)=[-0.027 0.055];
                                    end
                                    if pass(temp1,5)==2
                                        counterxy(6,:)=[0 0.055];
                                    end
                                    if pass(temp1,5)==3
                                        counterxy(6,:)=[0.027 0.055];
                                    end
                                    temp1=temp1+1;
                                else
                                    if tempg==0
                                        [mang1,mang2,mang3,mang4,mang5]=personcreat(pass(temp1,3))
                                        tempg=temp1;  
                                        if pass(temp1,5)==1
                                            counterxy(7,:)=[-0.027 0.055];
                                        end
                                        if pass(temp1,5)==2
                                            counterxy(7,:)=[0 0.055];
                                        end
                                        if pass(temp1,5)==3
                                            counterxy(7,:)=[0.027 0.055];
                                        end
                                        temp1=temp1+1;
                                    end
                                end                                
                            end
                        end
                    end
                end
            end
        end
        
        %开始服务
         if tempa~=0
             if  pass(tempa,2)+pass(tempa,7) == counter1
                 serveflash(1,counterxy(1,1),counterxy(1,2))
             end
         end
         if tempb~=0
             if  pass(tempb,2)+pass(tempb,7) == counter1
                 serveflash(2,counterxy(2,1),counterxy(2,2))
             end
         end
         if tempc~=0
             if  pass(tempc,2)+pass(tempc,7) == counter1
                 serveflash(3,counterxy(3,1),counterxy(3,2))
             end
         end
         if tempd~=0
             if  pass(tempd,2)+pass(tempd,7) == counter1
                 serveflash(4,counterxy(4,1),counterxy(4,2))
             end
         end
         if tempe~=0
             if  pass(tempe,2)+pass(tempe,7) == counter1
                 serveflash(5,counterxy(5,1),counterxy(5,2))
             end
         end
         if tempf~=0
             if  pass(tempf,2)+pass(tempf,7) == counter1
                 serveflash(6,counterxy(6,1),counterxy(6,2))
             end
         end
         if tempg~=0
             if  pass(tempg,2)+pass(tempg,7) == counter1
                 serveflash(7,counterxy(7,1),counterxy(7,2))
             end
         end
    end   
    counter1=counter1+1;
end

iiii=1;
sumtime=0;
sumtimea=0;
sumtimeb=0;
sumtimec=0;
numa=0;
numb=0;
numc=0;
while iiii<num
    sumtime=sumtime+pass(iiii,3)+pass(iiii,4);
    if pass(iiii,5)==1
        sumtimea=sumtimea+pass(iiii,3)+pass(iiii,4);
        numa=numa+1;
    end
    if pass(iiii,5)==2
        sumtimeb=sumtimeb+pass(iiii,3)+pass(iiii,4);
        numb=numb+1;
    end
    if pass(iiii,5)==3
        sumtimec=sumtimec+pass(iiii,3)+pass(iiii,4);
        numc=numc+1;
    end
iiii=iiii+1;
end

num=num-1;
freetimea=720-sumtimea;
freetimeb=720-sumtimeb;
freetimec=720-sumtimec;
freetime=freetimea+freetimeb+freetimec;
avetimea=round(1000*sumtimea/numa)/1000;
avetimeb=round(1000*sumtimeb/numb)/1000;
avetimec=round(1000*sumtimec/numc)/1000;

scaleaa=freetimea/720;
scaleab=freetimeb/720;
scaleac=freetimec/720;

dispdata(1,:)=[numa numb numc];
dispdata(2,:)=[sumtimea sumtimeb sumtimec];
dispdata(3,:)=[avetimea avetimeb avetimec];
dispdata(4,:)=[freetimea freetimeb freetimec];
dispdata(5,:)=[freetimea/720 freetimeb/720 freetimec/720];

figure(2)
subplot(2,2,1)
bar(dispdata(1,:))
title('服务顾客数')
subplot(2,2,2)
bar(dispdata(2,:))
title('服务时间')
subplot(2,2,3)
bar(dispdata(3,:))
title('平均服务时间')
subplot(2,2,4)
pie(dispdata(5,:))
title('空闲比例')




        
````

</details>

#### computing · MATLAB · b14dc1d6

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`24ecc1bde540e4fb22d1538e18f5a65cb0319c8cefde6a551e5d5520677dcf71`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/computing.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/timinge1.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [num,pass]=computing(tim0)

seat=[0 0 0];%服务员属性
pass=rand(1,4);%序号、到达时间、特殊要求时间、正常理发时间
pass(5)=0;%服务员
pass(6)=0;%离开时间
pass(7)=0;%等待时间
num=1;%服务人数
tim=0;%时间计数器
temp=0;%

while tim<=tim0 
    pass(num,1)=num;  %装入序号
    pass(num,2)=rand;
    pass(num,3)=rand;
    pass(num,4)=rand;
    
    %计算顾客到达时间
    if pass(num,2)<=0.07
       temp=4;
    else if  pass(num,2)<=0.17
            temp=5;
        else if  pass(num,2)<=0.69
            temp=6;
            else if  pass(num,2)<=0.89
            temp=7;
                else temp=8;
                end
            end
        end
    end
    tim=tim+temp;   %装入顾客到达时间
    pass(num,2)=tim;
    if pass(num,3)<=0.1 
        pass(num,3)=4;  %装入需要特殊服务的时间
    else pass(num,3)=0;
    end
    num=num+1;
end
num=num-1;

for i=1:num
    
    %计算顾客的理发席位
    if seat(1)<=pass(i,2)+pass(i,7)
        pass(i,5)=1; %由1号服务员理发
        temp1=timinge1(1,pass(i,4));
        seat(1)=pass(i,2)+pass(i,3)+temp1;
        pass(i,4)=temp1;  %装入正常理发所需时间
    else if seat(2)<=pass(i,2)+pass(i,7)
            pass(i,5)=2;  %由2号服务员理发
            temp1=timinge1(2,pass(i,4));
            seat(2)=pass(i,2)+pass(i,3)+temp1;
            pass(i,4)=temp1; %装入正常理发所需时间
        else if seat(3)<=pass(i,2)+pass(i,7)
                pass(i,5)=3; %由2号服务员理发
                temp1=timinge1(3,pass(i,4));
                seat(3)=pass(i,2)+pass(i,3)+temp1;
                pass(i,4)=temp1;                
            else               %计算等待时间
                x=seat(1);
                y=1; 
                if x>seat(2)
                    x=seat(2);
                    y=2;
                end
                if x>seat(3)
                    x=seat(3);
                    y=3;
                end
                pass(i,5)=y;
                temp1=timinge1(y,pass(i,4));
                pass(i,7)=seat(y)-pass(i,2);
                seat(y)=seat(y)+temp1+pass(i,3);
                pass(i,4)=temp1;
            end
        end
    end
pass(i,6)=pass(i,2)+pass(i,3)+pass(i,4);
end
````

</details>

#### envirment · MATLAB · ff7b3772

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `envirment`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f21163a47eaffb81a08f8b704fdef1d02c74020bdd54a3f8838ae1fcf16ddeb7`
- 语言：MATLAB
- 符号：`envirment`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/envirment.m`

<details>
<summary>展开原始代码</summary>

````matlab
function envirment
%场景设置
    pict=figure('color',[0.75 0.75 0.75],'position',[50 50 690 520]);

    door = annotation('rectangle',[0.4214 0.1405 0.1946 0.03333],'FaceColor',[0 1 0],'EdgeColor',[0 1 0]);
    word1 = annotation('textbox','Position',[0.3393 0.1143 0.0875 0.07619],'EdgeColor','none','FitHeightToText','off','FontSize',12,'String',{'门口'});
    
    seata1= annotation('rectangle',[0.2054 0.8214 0.1107 0.02857],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    seata2 = annotation('rectangle',[0.2071 0.7476 0.01429 0.1024],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    seata3 = annotation('rectangle',[0.3021 0.7419 0.01429 0.1024],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    word2 = annotation('textbox','Position',[0.1607 0.65 0.1107 0.06667],'EdgeColor','none','FitHeightToText','off','String',{'Seat A'});
    
    seatb1 = annotation('rectangle',[0.4579 0.8171 0.1107 0.02857],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    seatb2 = annotation('rectangle',[0.4579 0.7386 0.01429 0.1024],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    seatb3 = annotation('rectangle',[0.5564 0.7448 0.01429 0.1024],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    word3 = annotation('textbox','Position',[0.3768 0.6381 0.1036 0.07381],'EdgeColor','none','FitHeightToText','off','String',{'Seat B'});
    
    seatc1 = annotation('rectangle',[0.6986 0.8157 0.1107 0.02857],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    seatc2 = annotation('rectangle',[0.6996 0.7343 0.01429 0.1024],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    seatc3 = annotation('rectangle',[0.7964 0.7333 0.01429 0.1024],'FaceColor',[0.8471 0.1608 0],'EdgeColor',[0.8471 0.1608 0]);
    word4 = annotation('textbox','Position',[0.6429 0.6286 0.1018 0.07619],'EdgeColor','none','FitHeightToText','off','String',{'Seat C'});
    
    watierplace = annotation('rectangle',[0.8214 0.1762 0.01964 0.3857],'FaceColor',[0 1 1],'EdgeColor',[0 1 1]);
    word5 = annotation('textbox','Position',[0.7107 0.2 0.1179 0.0619],'EdgeColor','none','FitHeightToText','off','String',{'等待席'});
````

</details>

#### 相似实现组 · MATLAB · d2ba4f56

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：leaveflash.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `leaveflash`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6fb1754ae9ca50374cd59a706315c2aac158e14b40ee412ae4dee1fce08b1cfa`
- 语言：MATLAB
- 符号：`leaveflash`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/leaveflash.m`

<details>
<summary>展开原始代码</summary>

````matlab
function leaveflash(xx,yy,zz)

global man1 mana1 mana2 mana3 mana4 mana5
global manb1 manb2 manb3 manb4 manb5
global manc1 manc2 manc3 manc4 manc5
global mand1 mand2 mand3 mand4 mand5
global mane1 mane2 mane3 mane4 mane5
    
    switch xx
    case 1
          for ii = 10:-1:1
               face(:,1)=man1(:,1)+yy*(ii-1);
               face(:,3)=man1(:,3)+yy*(ii-1); 
               face(:,2)=man1(:,2)+zz*(ii-1);
               face(:,4)=man1(:,4)+zz*(ii-1);
               face(1,3)=0.0982;
               face(1,4)=0.1381;
               set(mana1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)]);
               set(mana2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)]);
               set(mana3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)]);
               set(mana4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)]);
               set(mana5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]);
               MM(ii)=getframe;
          end          
    case 2
           for ii = 10:-1:1
               face(:,1)=man1(:,1)+yy*(ii-1);
               face(:,3)=man1(:,3)+yy*(ii-1);
               face(:,2)=man1(:,2)+zz*(ii-1);
               face(:,4)=man1(:,4)+zz*(ii-1);
               face(1,3)=0.0982;
               face(1,4)=0.1381;
               set(manb1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)]);
               set(manb2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)]);
               set(manb3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)]);
               set(manb4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)]);
               set(manb5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]);
               MM(ii)=getframe;
            end
    case 3
           for ii = 10:-1:1
               face(:,1)=man1(:,1)+yy*(ii-1);
               face(:,3)=man1(:,3)+yy*(ii-1); 
               face(:,2)=man1(:,2)+zz*(ii-1);
               face(:,4)=man1(:,4)+zz*(ii-1);
               face(1,3)=0.0982;
               face(1,4)=0.1381;
               set(manc1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)]);
               set(manc2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)]);
               set(manc3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)]);
               set(manc4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)]);
               set(manc5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]);
               MM(ii)=getframe;
           end
    case 4
           for ii = 10:-1:1
               face(:,1)=man1(:,1)+yy*(ii-1);
               face(:,3)=man1(:,3)+yy*(ii-1); 
               face(:,2)=man1(:,2)+zz*(ii-1);
               face(:,4)=man1(:,4)+zz*(ii-1);
               face(1,3)=0.0982;
               face(1,4)=0.1381;
               set(mand1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)]);
               set(mand2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)]);
               set(mand3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)]);
               set(mand4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)]);
               set(mand5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]);
               MM(ii)=getframe;
           end
     case 5
           for ii = 10:-1:1
               face(:,1)=man1(:,1)+yy*(ii-1);
               face(:,3)=man1(:,3)+yy*(ii-1); 
               face(:,2)=man1(:,2)+zz*(ii-1);
               face(:,4)=man1(:,4)+zz*(ii-1);
               face(1,3)=0.0982;
               face(1,4)=0.1381;
               set(mane1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)]);
               set(mane2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)]);
               set(mane3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)]);
               set(mane4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)]);
               set(mane5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]);
               MM(ii)=getframe;
           end
     case 6
           for ii = 10:-1:1
               face(:,1)=man1(:,1)+yy*(ii-1);
               face(:,3)=man1(:,3)+yy*(ii-1); 
               face(:,2)=man1(:,2)+zz*(ii-1);
               face(:,4)=man1(:,4)+zz*(ii-1);
               face(1,3)=0.0982;
               face(1,4)=0.1381;
               set(manf1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)]);
               set(manf2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)]);
               set(manf3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)]);
               set(manf4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)]);
               set(manf5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]);
               MM(ii)=getframe;
           end
     case 7
           for ii = 10:-1:1
               face(:,1)=man1(:,1)+yy*(ii-1);
               face(:,3)=man1(:,3)+yy*(ii-1); 
               face(:,2)=man1(:,2)+zz*(ii-1);
               face(:,4)=man1(:,4)+zz*(ii-1);
               face(1,3)=0.0982;
               face(1,4)=0.1381;
               set(mang1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)]);
               set(mang2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)]);
               set(mang3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)]);
               set(mang4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)]);
               set(mang5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]);
               MM(ii)=getframe;
           end 
end
````

</details>

##### 变体 2：serveflash.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `serveflash`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d0c90eb6a50306344b0c49432d88307db31cde8e2c30b9aea188dadc7d2adb04`
- 语言：MATLAB
- 符号：`serveflash`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/serveflash.m`

<details>
<summary>展开原始代码</summary>

````matlab
function serveflash(xx,yy,zz)
global man1 mana1 mana2 mana3 mana4 mana5
global manb1 manb2 manb3 manb4 manb5
global manc1 manc2 manc3 manc4 manc5
global mand1 mand2 mand3 mand4 mand5
global mane1 mane2 mane3 mane4 mane5
        
switch xx
    case 1
            for ii = 1:10  %开始服务动画
                   face(:,1)=man1(:,1)+yy*(ii-1);
                   face(:,3)=man1(:,3)+yy*(ii-1); 
                   face(:,2)=man1(:,2)+zz*(ii-1);
                   face(:,4)=man1(:,4)+zz*(ii-1);
                   face(1,3)=0.0982;
                   face(1,4)=0.1381;
                   set(mana1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)])
                   set(mana2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)])
                   set(mana3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)])
                   set(mana4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)])
                   set(mana5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]) 
                   MM(ii)=getframe;
            end
    case 2
        for ii = 1:10  %开始服务动画
                   face(:,1)=man1(:,1)+yy*(ii-1);
                   face(:,3)=man1(:,3)+yy*(ii-1); 
                   face(:,2)=man1(:,2)+zz*(ii-1);
                   face(:,4)=man1(:,4)+zz*(ii-1);
                   face(1,3)=0.0982;
                   face(1,4)=0.1381;
                   set(manb1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)])
                   set(manb2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)])
                   set(manb3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)])
                   set(manb4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)])
                   set(manb5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]) 
                   MM(ii)=getframe;
        end
    case 3
        for ii = 1:10  %开始服务动画
                   face(:,1)=man1(:,1)+yy*(ii-1);
                   face(:,3)=man1(:,3)+yy*(ii-1); 
                   face(:,2)=man1(:,2)+zz*(ii-1);
                   face(:,4)=man1(:,4)+zz*(ii-1);
                   face(1,3)=0.0982;
                   face(1,4)=0.1381;
                   set(manc1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)])
                   set(manc2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)])
                   set(manc3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)])
                   set(manc4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)])
                   set(manc5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]) 
                   MM(ii)=getframe;
        end
    case 4
        for ii = 1:10  %开始服务动画
                   face(:,1)=man1(:,1)+yy*(ii-1);
                   face(:,3)=man1(:,3)+yy*(ii-1); 
                   face(:,2)=man1(:,2)+zz*(ii-1);
                   face(:,4)=man1(:,4)+zz*(ii-1);
                   face(1,3)=0.0982;
                   face(1,4)=0.1381;
                   set(mand1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)])
                   set(mand2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)])
                   set(mand3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)])
                   set(mand4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)])
                   set(mand5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]) 
                   MM(ii)=getframe;
        end
    case 5
        for ii = 1:10  %开始服务动画
                   face(:,1)=man1(:,1)+yy*(ii-1);
                   face(:,3)=man1(:,3)+yy*(ii-1); 
                   face(:,2)=man1(:,2)+zz*(ii-1);
                   face(:,4)=man1(:,4)+zz*(ii-1);
                   face(1,3)=0.0982;
                   face(1,4)=0.1381;
                   set(mane1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)])
                   set(mane2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)])
                   set(mane3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)])
                   set(mane4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)])
                   set(mane5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]) 
                   MM(ii)=getframe;
        end
    case 6
        for ii = 1:10  %开始服务动画
                   face(:,1)=man1(:,1)+yy*(ii-1);
                   face(:,3)=man1(:,3)+yy*(ii-1); 
                   face(:,2)=man1(:,2)+zz*(ii-1);
                   face(:,4)=man1(:,4)+zz*(ii-1);
                   face(1,3)=0.0982;
                   face(1,4)=0.1381;
                   set(manf1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)])
                   set(manf2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)])
                   set(manf3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)])
                   set(manf4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)])
                   set(manf5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]) 
                   MM(ii)=getframe;
        end
    case 7
        for ii = 1:10  %开始服务动画
                   face(:,1)=man1(:,1)+yy*(ii-1);
                   face(:,3)=man1(:,3)+yy*(ii-1); 
                   face(:,2)=man1(:,2)+zz*(ii-1);
                   face(:,4)=man1(:,4)+zz*(ii-1);
                   face(1,3)=0.0982;
                   face(1,4)=0.1381;
                   set(mang1,'position',[face(1,1) face(1,2)  face(1,3) face(1,4)])
                   set(mang2,'X',[face(2,1);face(2,3)],'Y',[face(2,2);face(2,4)])
                   set(mang3,'X',[face(3,1);face(3,3)],'Y',[face(3,2);face(3,4)])
                   set(mang4,'X',[face(4,1);face(4,3)],'Y',[face(4,2);face(4,4)])
                   set(mang5,'X',[face(5,1);face(5,3)],'Y',[face(5,2);face(5,4)]) 
                   MM(ii)=getframe;
        end        
end
               
````

</details>

#### personcreat · MATLAB · f5253ab7

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e172c1c6fa5fedf350965dbddeee37bfe41250fbe6b0e1e5b4c4a7b1cb20fd52`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/personcreat.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [face1,face2,face3,face4,face5]=personcreat(vect)

if vect==0
     face1 = annotation('ellipse',[0.4625 0.1786 0.0982 0.1381],'FaceColor',[0.6824 0.4667 0],'EdgeColor',[0.6824 0.4667 0]);
else face1 = annotation('ellipse',[0.4625 0.1786 0.0982 0.1381],'FaceColor',[0.4 0.6 0],'EdgeColor',[0.6824 0.4667 0]);%[0.2096 0.6881 0.09821 0.1381]
end
    face2 = annotation('line',[0.4875 0.5018],[0.2667 0.2667],'LineWidth',3);
    face3 = annotation('line',[0.5214 0.5339],[0.2667 0.2667],'LineWidth',3);
    face4 = annotation('line',[0.5125 0.5125],[0.25 0.2309],'LineWidth',3);
    face5 = annotation('line',[0.4968 0.525],[0.2081 0.2072],'LineWidth',3);
````

</details>

#### timinge1 · MATLAB · 6460b657

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `timinge1`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2f7ade97bb645d88c9e08fe535261d07a0a975d9e45e358b8c6f3158f536c89a`
- 语言：MATLAB
- 符号：`timinge1`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡洛法/蒙特卡洛法/timinge1.m`

<details>
<summary>展开原始代码</summary>

````matlab
function xxxx=timinge1(vect1,vect)

switch vect1
    case 1    
       if vect<=0.18
            xxxx=8;
        else if  vect<=0.4
               xxxx=9;
            else if vect<=0.77
                    xxxx=10;
                else xxxx=11;
                end
            end
       end
   case 2    
       if vect<=0.18
            xxxx=10;
        else if  vect<=0.37
               xxxx=11;
            else if vect<=0.72
                    xxxx=12;
                else xxxx=13;
                end
            end
       end
    otherwise  
        if vect<=0.15
            xxxx=12;
        else if  vect<=0.37
               xxxx=13;
            else if vect<=0.74
                    xxxx=14;
                else xxxx=15;
                end
            end
       end
end
````

</details>

#### Contents · MATLAB · 1fb0d48d

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`8dc1bb3878bd09cdb944cf4ff5d25eceb6d46247018f72af3fea8ad567911aa3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/Contents.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MCMC -- Markov Chain Monte Carlo Tools
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
% There are three parts to this library of routines.
% 1. *[rnd,pdf,lpr].m - distribution function tools to complement Matlab's
% 2. mcmc*.m - routines to calculate and display summaries of MCMC output
% 3. other - other useful routines
%  
%   1. Distribution Function Tools
%
%   These function help in random number generation and
%   various calculations involving density functions.
%   The names attempt to match those that MatLab uses,
%   namely, *pdf, *cdf, and *rnd.   Those that end in
%   "lpr" are for "Log. Probability Ratio", which are
%   useful for a Metropolis-Hastings algorithm.
% 
%   Note: there are two random number generators in Matlab 
%   one for normals and the other for everything else.
%   For reseting the normal random seed use  randn('state', ...)
%   and for all others use rand('state', ...).
%
% randrand - randomize both random number chains off the clock
% 
% mvnormrnd - random multivariate normal - different from Matlab's mvnrnd
%
% wishrnd - random Wishart value
% wishirnd - random Wishart value - integer df only
% invwishrnd - random inverse Wishart value
% invwishirnd - random inverse Wishart value - integer df only
% invwishpdf - inverse Wishart density
%
% metrop - a general Metropolis-Hastings step
%
% betalpr - log probability ratio for beta distribution
% gamlpr  - log probability ratio for gamma distribution
% invwishlpr - log probability ratio for inverse wishart distribution
% mvnormlpr - log probability ratio for multivariate normal distribution
%   
%   2. MCMC Summaries
%     
% These routines use the last dimension of an array as the
% sample index.  So an array with dimension (nr,nc,ns) 
% will be a collection of ns samples of an nr by nc matrix of 
% parameters.  An array with dimension (nr,nc) will
% be nc samples of an nr-vector of parameters.
% When the summary statistics are calculated, the last dimension
% is dropped.  
%
% Note: Matlab routines tend to collapse over the first dimension
% instead of the last.  I chose to use the last dimension for
% an aesthetic reason, when simply displaying a 3+ dimensional
% array, Matlab displays the first two dimensions as a matrix
% and splits over the 3rd+ dimensions.  To see what I mean
% enter 'x = zeros(2,3,4)'.
% 
% mcmclt - lower triangle - for symmetric matricies - to use with mcmctrace
% mcmcsumm - calculate summary statistics
%   (includes autocorrelations and Gelman-Rubin statistics)
% mcmctrace - matrix of trace plots 
% mcmcacf - to plot autocorrelations
% mcmcgr - Gelman-Rubin R statistic for convergence
% 
% mcmcdemo - short demonstration program
% 
%   3. Other
%
% ltvec - convert a lower-triangular matrix into a vector
% veclt - convert a vector into a lower-triangular matrix
% ltindex - convert row and column index into lt-index
%
%
% Bug reports and suggestions are welcome, but quick
% response is not guaranteed.
%
%   David Shera - shera@hsph.harvard.edu
%   http://www.biostat.harvard.edu/~shera/mcmc
````

</details>

#### betalpr · MATLAB · c7791e78

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ed67fb8e94cbef10593c204c47540cabba4aea9fb4f0f2dfcdc6a2039c0af0e4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/betalpr.m`

<details>
<summary>展开原始代码</summary>

````matlab
% BETALPR - Beta Distribution - Log Probability Ratio
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
% 
%   [ lpr ] = betalpr(p1,p2,alpha,beta)
%
% returns the log of the p(p1) / p(p2) when both
% are distributed Beta(alpha,beta).
%
% See also: METROP, *LPR

function [ lpr ] = betalpr(p1,p2,alpha,beta)
lpr = (alpha-1) * log(p1/p2) + (beta-1) * log((1-p1)/(1-p2)) ;
````

</details>

#### gamlpr · MATLAB · db52df25

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`163aea6d307c3443f1fc3046ccfe3cd35c7dbe52fdc28c4daaff3db8da8fcdcd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/gamlpr.m`

<details>
<summary>展开原始代码</summary>

````matlab
% GAMLPR = Gamma Distribution - Log Probability Density Ratio
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
% 
%   [ lpr ] = gamlpr( g1, g2, alph, gam ) 
%
% returns log ( p(g1)/p(g2) ) when g1 and g2 are
% distributed gamma(alph,gam)
%

function [ lpr ] = gamlpr(g1, g2, alph, gam) 
lpr = (alph-1)*log(g1/g2)  - (g1-g2)/gam ;
````

</details>

#### invwishirnd · MATLAB · ad54236b

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`cbac5f181b709c602610381e871916fe64a25292ebe347d7ec65ca5cc4080bd2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/invwishirnd.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/wishirnd.m`

<details>
<summary>展开原始代码</summary>

````matlab
% INVWISHIRND - Inverse Wishart Random Matrix
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [IW] = invwishirnd(S,d) 
%
% S = p x p symmetric, postitive definite "scale" matrix 
% d = "degrees of freedom" parameter
%   = "precision" parameter 
%   (d must be an integer for this routine, see INVWISHRND)
%
% IW = random matrix from the inverse Wishart distribution
%
% Note:
%   different sources use different parameterizations w.r.t. nu
%   this routine uses that of Press and Shigemasu (1989):
%   density(IW) is proportional to  
%     exp[-.5*trace(S*inv(IW))] / [det(IW) ^ (d/2)].
%
%   With this density definition:
%   mean(IW) = S/(d-2p-2) when d>2p+2,
%   mode(IW) = S/d.
%
% See also: INVWISHRND, WISHRND

function [IW] = invwishirnd(S,d) 
[p,p2] = size(S) ;
W = wishirnd(inv(S),d-p-1) ;
IW = inv(W) ;
````

</details>

#### invwishlpr · MATLAB · 59d0f655

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：执行归一化或标准化以统一变量尺度。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`bff55ae50c253613e3ccdecc5cbbc4e3d726b1f5e566a70389ead7e95aa7f7bc`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/invwishlpr.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/invwishpdf.m`

<details>
<summary>展开原始代码</summary>

````matlab
% INVWISHLPR = Inverse Wishart Distribution - Log Probability Density Ratio
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
% 
%   [ lpr ] = invwishpdf( IW1, IW2, S, d ) ;
%
% IW = argument matrix, should be positive definite
% S = p x p symmetric, postitive definite "scale" matrix 
% d = "precision" parameter = "degrees of freeedom"
%
% lpr = probability density function, properly normalized
%
% Note: 
%   different sources use different parameterizations 
%   see INVWISHRND for details
%
% See Also: INVWISHRND, INVWISH

function [ lpr ] = invwishlpr(IW1, IW2, S, d) 

% [k,k2] = size(IW1) ;

logexpterm1 = -.5*trace(S/IW1) ;
logexpterm2 = -.5*trace(S/IW2) ;

logdetIWterm1 = log(det(IW1))*(d/2) ;
logdetIWterm2 = log(det(IW2))*(d/2) ;

lpr = logexpterm1 - logexpterm2 - logdetIWterm1 + logdetIWterm2 ;
````

</details>

#### invwishpdf · MATLAB · c6c2c7e6

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：执行归一化或标准化以统一变量尺度。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b42c5c928fa6910f58b0108ed0e52ab069a9958df705d9fbc759226243eb6e4d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/invwishpdf.m`

<details>
<summary>展开原始代码</summary>

````matlab
% INVWISHPDF = Inverse Wishart Distribution - Probability Density Function
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
% 
%   [pdf] = invwishpdf( IW, S, d ) ;
%
% IW = argument matrix, should be positive definite
% S = p x p symmetric, postitive definite "scale" matrix 
% d = "precision" parameter = "degrees of freeedom"
%
% pdf = probability density function, properly normalized
% logpdf = log(pdf)
%
% Note:
%   different sources use different parameterizations w.r.t. d
%   this routine uses that of Press and Shigemasu
%   density(IW) is proportional to  
%     exp[-.5*trace(S*inv(IW))] / [det(IW) ^ (d/2)]
%
%   With this density definitions,
%   mean(IW) = S/(d-2p-2),
%   mode(IW) = S/d.
%
% See also: INVWISHRND, INVWISHIRND, INVWISHLPR, WISHRND

function [ pdf, logpdf ] = invwishpdf(IW,S,d) 

[k,k2] = size(IW) ;

logexpterm = -.5*trace(S/IW) ;
logdetIWterm = log(det(IW))*(d/2) ;
logdetSterm = log(det(S))*((d-k-1)/2) ;
logtwoterm = log(2)*((d-k-1)*k/2) ;
logpiterm = log(pi)*((k-1)*k/4) ;

klst = 1:k ;
dkk2 = (d-k-klst)/2 ;
gamln = gammaln(dkk2) ;
sumgamln = sum(gamln) ;

logpdf = logexpterm + logdetSterm - ...
         (logdetIWterm + logtwoterm + logpiterm + sumgamln  ) ;

pdf = exp(logpdf) ;
````

</details>

#### invwishrnd · MATLAB · cca4ed5a

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`bb218409270a5700465e5802cc168378bfaf3938febd4d13c51a6e88ad02a867`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/invwishrnd.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/wishrnd.m`

<details>
<summary>展开原始代码</summary>

````matlab
% INVWISHRND - Inverse Wishart Distribution - Random Matrix Value
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [ IW ] = invwishrnd(S,d) 
%
% S = p x p symmetric, postitive definite "scale" matrix 
% d = "degrees of freedom" parameter (integer)
%   = "precision" parameter (d may be non-integer)
%
% IW = random matrix from the inverse Wishart distribution
%
% Note:
%   Different sources use different parameterizations.
%   This routine uses that of Press and Shigemasu (1989):
%   density (IW) is proportional to  
%     exp[-.5*trace(S*inv(IW))] / [det(IW) ^ (d/2)].
%
%   With this density definition:
%   mean of IW = S/(d-2p-2) for d>2p+2,
%   mode of IW = S/d.
%
% See also: INVWISHIRND, WISHRND

function [IW] = invwishrnd(S,d) 

[p,p2] = size(S) ;

W = wishrnd(inv(S),d-p-1) ;

IW = inv(W) ;
````

</details>

#### ltindex · MATLAB · 950175d5

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3beda5b65a8c34c097cc7529c6ecf9294f92ffbcec73d0d825c84f51da0db316`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/ltindex.m`

<details>
<summary>展开原始代码</summary>

````matlab
% LTINDEX - Lower Triangular Index
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%  [irow, icol] = ltindex(index, dim) ;
%
% If a lower triangular matrix is packed in to a vector (column wise),
% this calculates the matching row and column in the matrix for a 
% given index and dimension. (1,p) -> (1,1), (2,p) -> (2,1),
% (p+1,p) -> (2,2), etc.
%
% See also:  LTVEC
%

function [irow, icol] = ltindex(index, dim) ;

irow = index ;

icol = 1 ;
while irow>dim & icol<= dim,
  icol = icol+1 ;
  irow = irow - dim + (icol-1) ;
end

if icol>dim,
  disp(sprintf('Error: ltindex: index=%d is too big for dim=%d',index,dim));
  irow=NaN ;
  icol=NaN ;  
end
````

</details>

#### ltvec · MATLAB · dced89a0

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a8321be3248c728837cfc654b4e3505d3d4db8528c2f24892748a3e7a342dadd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/ltvec.m`

<details>
<summary>展开原始代码</summary>

````matlab
% LTVEC - Change a Lower-Triangular Matrix into a Vector
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [V] = ltvec(M) 
%
% M = square matrix, only the diagonal and lower triangle is used.
% 
% V = vector to be returned
%
%   If M is a p x p matrix, then V consists of 
%   [ M(:,1) ; M(2:p,2) ; M(3:p,3), etc. ]
%
% See also: LTINDEX

function [v] = ltvec(m) 

[p,nc] = size(m) ;

if p==0,
  v = [] ;
else 
  for ic = 1:p,
    if ic==1,
      v = m(:,1) ;
    else
      v = [ v ; m(ic:p,ic) ] ;
    end 
  end
end
````

</details>

#### mcmcacf · MATLAB · 3db44597

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`e6b3fb3c0e71f98ff046f9e1ee6d756ec489a43b44283f5fbe7fa947264b259e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmcacf.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmcsumm.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmctrace.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MCMCACF - autocorrelation plots
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
% 
% This is not a function, but a way to get acf plots for MCMC runs.
%
% S = mcmcsumm(A) contains S.acf, a matrix of the autocorrelations.
%
% So, mcmctrace(S.acf) will plot the autocorrelations.
%
% See also: MCMCSUMM, MCMCTRACE
````

</details>

#### mcmcdemo · MATLAB · d5586201

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`8d98041eea32c9b28b9c753b608962710a2f22de1a08ea66a3f0b0f92aae400e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmcdemo.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/invwishrnd.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmclt.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmcsumm.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmctrace.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MCMCDEMO - small demonstration program for the use of MCMC library
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
% There is no MCMC chain set up here, just a random sample
% of matricies from an inverse wishart distribution.
%
% The use of the summary and trace functions are demonstrated.
%
% The program is commented.
% 

echo 

% Creating an array to hold all the values so that things run a little
% faster.

% SIW = Sample of Inverse Wisharts

SIW = NaN* zeros(5,5,200) ;

% nu = degrees of freedom = precision parameter
nu = 50

% IWmode = mode of distribution of SIW
IWmode = 3*eye(5) + 2 * ones(5,5) 

% The inverse Wishart scale parameter = nu * the mode.
% (in our parameterization)
IWparm = nu * IWmode

% This is not really an MCMC run, simply a random sample.
echo off all

for ii = 1 : 200 ;
  IW = invwishrnd ( IWparm, nu ) ;
  SIW(:,:,ii) = IW ;
end ;

echo on 

% display the dimensions of SIW
size(SIW)

% create structure of summary statistics
SIWsumm = mcmcsumm(SIW) ;

SIWsumm.mean
SIWsumm.median
SIWsumm.std
SIWsumm.min
SIWsumm.max

% SIWsumm.sorted - not printed, but available for later use.
% SIWsumm.acf - autocorrelation, not printed but available.

% create lower triangular version, upper triangle is redundant
SIWlt = mcmclt(SIW) ;

% plot trace of upper triangular version
mcmctrace(SIWlt) ;

% for a plot of the autocorrelation, use mcmctrace(SIWsumm.acf) 
````

</details>

#### mcmcgr · MATLAB · 1cc97922

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ff53cbf3de7cdce5f183d5be1858cb6ae82cae6203194eccc27461e0785edbfb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmcgr.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MCMCGR - Gelman-Rubin R statistic for convergence
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
% function [ R ] = mcmcgr(A,ng) ;
%
% calculates the Gelman-Rubin R statistic for each chain
%
% A = chain of values from an MCMC run
% ng = number of groups to use
% 
% See also: MCMCSUMM


function [ R ] = mcmcgr(A,ng) ;

[nr, nc, chainlen] = size(A) ;

gsize = chainlen/ng ;

X = NaN*zeros(nr,nc,ng,gsize);

gstart = 1 ;
for ig = 1:ng ;
  gend = gstart+gsize-1 ;
  X(:,:,ig,:) = A(:,:,gstart:gend) ;
  gstart = gend+1 ;
end

M = mean(X,4) ;

tB = std(M,0,3) ;

B = gsize * tB .* tB ;

S = std(X,0,4) ;

S2 = S .* S ;

W = sum(S2,3) / ng ;
vplus = (gsize-1)/gsize*W + B/gsize ;

R = vplus./W ;
````

</details>

#### mcmclt · MATLAB · 30317d46

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`77a90440490e25ff414826b55bb1f8443e6d0a07387686647a57138bb5acc8f7`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmclt.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MCMLT - makes matrix of MCMC runs lower triangular
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [ Alt ] = MCMCLT(A)
%
% A = a chain of matricies, typically covariances
%
% Alt = A with all elements above the diagonal changed to NaNs
%
% Good for removing redundant trace plots and values,
% especially for samples of covariance matricies.
% 
% MCMCTRACE will not plot chains that begin with NaNs.
%
% See also: LTVEC, VECLT

function [Alt] = mcmclt(A) 

dd = size(A) ;
ll = length(dd) ;
d1 = dd(1) ;
d2 = dd(2) ;

if (ll==2),
  Alt = A ;
  for i1 = 1:d1,
  for i2 = 1:d2,
    if i2>i1,
      Alt(i1,i2)=NaN ;
    end
  end
  end
else
  Alt = A ;
  for i1 = 1:d1,
  for i2 = 1:d2,
    if i2>i1,
      Alt(i1,i2,:)=NaN ;
    end
  end
  end
end
````

</details>

#### mcmcsumm · MATLAB · ca4b4558

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`bc739aaa28fff46ea2ba6ae57d30119c88423e4a6a0d02035f4562cb113f8f35`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmcsumm.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmcgr.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MCMCSUMM - Summary Statistics 
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [S] = mcmcsumm(A) 
%
% A = r x c x s array of s samples of an r x c matrix of parameters
%
% S = structure containing returned values (mean, median, etc.)
%   select components with S.mean, S.median, etc.
%
% Note: all summary statistics are marginal, there are no multivariate
%   summaries at this time.
%
% These routines use the last dimension of an array as the
% sample index.  So an array with dimension (nr,nc,ns) 
% will be a collection of ns samples of an nr by nc matrix of 
% parameters.  An array with dimension (nr,nc) will
% be nc samples of an nr-vector of parameters.
% When the summary statistics are calculated, the last dimension
% is dropped.  
% 
% See also: MCMCTRACE, MCMCLT
%

function [S] = mcmcsumm(A) 

if isnan(A),
 S.mean = NaN;
 S.min = NaN;
 S.max = NaN;
 S.std = NaN;
 S.sorted = NaN;
 S.median = NaN;
 S.meanvec = NaN;
 S.cov = NaN;
 S.acf= NaN;
 S.acf10max = NaN;
 S.acf10med = NaN;
 S.gr2 = NaN ;
 S.gr2max = NaN ;
else

dd = size(A) ;
ll = length(dd) ;
if (ll==2),
  aa = reshape(A, [dd(1),1,dd(2)]) ;
else
  aa = A ;
end

[nr,nc,ns] = size(aa) ;

maxlag = min(100,ns-1) ;

Z = zeros(nr,nc,ns) ;
S = struct('mean',Z) ;

S.mean = mean(aa,3) ;
S.min = min(aa,[],3) ;
S.max = max(aa,[],3) ;
S.std = std(aa,0,3) ;
S.sorted = NaN*zeros(nr,nc,ns) ;
S.median = NaN*zeros(nr,nc) ;

tmpvec = reshape(S.mean, nr*nc, 1) ;
sel = ~isnan(tmpvec) ;
S.meanvec = tmpvec(sel,:) ;

aavec = reshape(aa, nr*nc, ns) ;
aavec = aavec(sel,:) ;

if nr>0 & nc>0 & ns>0,  
% then there's something to work with

S.cov = cov(aavec') ;

for ir = 1:nr,
for ic = 1:nc,
  xx = reshape(aa(ir,ic,:),1,ns) ;
  S.sorted(ir,ic,:) = sort(xx) ;
  S.median(ir,ic) = median(xx) ;
  xx0 = xx - mean(xx) ;
  if S.max(ir,ic)-S.min(ir,ic) < .0000000001,
    xc = NaN * zeros(1,2*maxlag+1) ;
  else
    xc = xcorr(xx0,xx0,maxlag,'coeff'); 
  end 
  S.acf(ir,ic,:) = [xc(maxlag+(1:(maxlag+1)))] ;
  S.acf1 = S.acf(:,:,2) ;
end 
end 

if ns>10,
  S.acf10 = S.acf(:,:,11) ;
  tmpacf = reshape(S.acf10,1,nr*nc) ;
  if any(~isnan(tmpacf)),
    tmpacf = tmpacf(~isnan(tmpacf)) ;
    S.acf10max = max(max( tmpacf )) ;
    S.acf10med = median(median( tmpacf )) ;
  else
    S.acf10max = NaN ;
    S.acf10med = NaN ;
  end
else
  S.acf10 = NaN*S.acf(:,:,1) ;
  S.acf10max = NaN ;
  S.acf10med = NaN ;
end

else 
  % one of nr nc ns == 0
  S.sorted(:,:,:) = A ;
  S.median = A(:,:,1) ;
  S.acf10max = NaN ;
  S.acf10med = NaN ;
  S.acf = NaN * zeros(nr,nc,maxlag+1) ;
  S.acf1 = S.acf(:,:,2) ;
  S.acf10 = S.acf(:,:,11) ;
  S.cov = A(:,:,1) ;
end

S.gr2 = mcmcgr(A,2) ;
S.gr2max = max(max(S.gr2)) ;

end
% end of NaN branch
````

</details>

#### mcmctrace · MATLAB · ac7adb06

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `mcmctrace`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`58a4ee8cd914163d5f70f5dc6bfc29d65eb39b7aa35c5959cf9d88cd3d7fa7e1`
- 语言：MATLAB
- 符号：`mcmctrace`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mcmctrace.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MCMCTRACE - trace plots
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   mcmctrace(A)
%
% A = an array of MCMC output, the last dimension
%     is the index of the different samples
%
% The resulting graph will be an array of trace
% plots of the values over time.  
%
% if the first element of each trace is NaN, the
% trace plot will be empty.
%
% See also: MCMCLT, MCMCSUMM

function mcmctrace(A) 

dd = size(A) ;
ll = length(dd) ;
d1 = dd(1) ;
d2 = dd(2) ;

if (ll==2),
  aa = reshape(A, [d1 1 d2]) ;
  d3 = d2 ;
  d2 = 1 ;
else
  aa = A ;
  d3 = dd(3) ;
end ;

ix = 0 ;
for i1 = 1:d1,
for i2 = 1:d2,
  ix = ix + 1 ;
  bb = reshape(aa(i1,i2,:),[1 d3]) ;
  if ( ~isnan (bb(1,1)) ),
    subplot(d1,d2,ix), plot(bb,'k-') ;
  end 
end
end
````

</details>

#### metrop · MATLAB · 149cb4dd

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索；执行归一化或标准化以统一变量尺度。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`5d79dc658fab3c5045360c0daf2fac6f1586e60e9045ff8d6319826149cd1a0f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/metrop.m`

<details>
<summary>展开原始代码</summary>

````matlab
% METROP - perform a Metropolis-Hastings step
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [KEEPV, ACCEPT] = METROP(LOGQ,NV,OV)
%
% LOGQ = log (unnormalized) density ratio
%
%   If targ(x) is the target density (may be unnormalized)
%   and gen(x) is the generating density (may be unnormalized),
% 
%   then LOGQ = log( targ(NV) gen(OV|NV) / targ(OV) gen(NV|OV) ) 
%
% NV = new sample value
% OV = old sample value
%
% KEEPV = value of NV or OV that is kept
% ACCEPT = 1 if NV was kept, 0 if OV was kept
%
% See also: BETALPR, GAMLPR, INVWISHLPR, MVNORMLPR

function [ keepv, accept ] = metrop ( logq, newval, oldval, acc, ix ) ;

accept = acc ;

if (logq>0),
  keepv = newval ;
  accept(ix) = 1 ;
elseif (unifrnd(0,1) <= exp(logq)),
  keepv = newval ;
  accept(ix) = 1 ;
else
  keepv = oldval ;
  accept(ix) = 0 ;
end
````

</details>

#### mvnormlpr · MATLAB · 2d27052b

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`469d9ebb77e57434d3a04c337e3c6af65f6e57afc7d5178cd3185e0a709a7187`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mvnormlpr.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MVNORMLPR - Multivariate Normal Distribution - Log Density Ratio
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
% 
% [ lpr ] = mvnormlpr(x1, x2, mu, sigma)
%
%   mu = mean column vector, p x 1
%   sigma = covariance matrix, p x p 
%   x1, x2 = sample values, p x 1
%
%   lpr = log probability ratio
%
% returns the log of the p(p1) / p(p2) when both
% are distributed Multivariate Normal (mu,sigma).
%
% Useful for calculations in Metropolis-Hastings steps
%
% See also: METROP

function [ lpr ] = mvnormlpr (x1, x2, mu, sigma) 

d1 = x1 - mu ;
d2 = x2 - mu ;
lpr = (-(d1'/sigma)*d1 + (d2'/sigma)*d2) / 2 ;
````

</details>

#### mvnormrnd · MATLAB · 5f666574

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`160a114b7da0201acbf477205534b8a60b5610f7621544693015f8fe0e34d100`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/mvnormrnd.m`

<details>
<summary>展开原始代码</summary>

````matlab
% MVNORMRND - Multivariate Normal - Random Number Generation
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
% 
% Y = mvnormrnd(mu, sigma, n) 
%
%   mu = p by 1 mean column vector or n by p matrix of means
%   sigma = covariance matrix
%   n = number of observations to generate
%
%   Y = an n by p matrix of row vectors with mean mu and covariance sigma
%
% Note: works slightly different from Matlab builtin MVNRND.
%
%   if mu is a column vector, n rows will be returned, all with mean mu
%
%   if mu is a matrix, a matrix of the same size will be returned with
%   row Y(i,:) having mean mu(i,:) .
% 
% See also: MVNORMPDF, MVNORMLPR

function [Y] = mvnormrnd (mu,sigma,n) 

[d1,d2] = size(mu);
S = chol(sigma)';

if d2==1,
  % then mu is a column vector
  X = normrnd(0,1,n,d1);
  Y = X*S' + ones(n,1)*mu' ;
else 
  X = normrnd(0,1,d1,d2);
  Y = X*S' + mu ;
end
````

</details>

#### randrand · MATLAB · f3193b9a

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`e294f81aa86fd7f1b78e42996a753e78011a6640b21b7f86256efa92590f66b8`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/randrand.m`

<details>
<summary>展开原始代码</summary>

````matlab
% RANDRAND - Reset both Random Number Generator Seeds to the clock
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
% 
% Note: there are two random number generators in Matlab 
% one for normals and one for everything else.
% For reseting the normal random seed use  randn('state', ...)
% and for all others use rand('state, ...).
%
% This program initializes both off the system clock.
%
randn('state',sum(100*clock)) ;
rand('state',sum(100*clock)+10*normrnd(0,1,1,1)^2) ;
````

</details>

#### veclt · MATLAB · 0291f9d6

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`e00f0df791b5dac233543b26f20bb1148a1d6cc1d27bf030d00961327d2f895d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/veclt.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/ltvec.m`

<details>
<summary>展开原始代码</summary>

````matlab
% VECLT - change a vector into a lower-triangular matrix
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [M] = ltvec(V) 
%
% V = vector argument
%
% M = square, symmetric matrix
% 
%   If M is a p x p matrix, then V consists of 
%   [ M(:,1) ; M(2:p,2) ; M(3:p,3) ; etc. ]
%
% See also: LTVEC, LTINDEX, MCMCLT

function [m] = ltvec(v) 

[ll,oo] = size(v) ;

p = floor(sqrt(2*ll)) ;

ix = 0 ;
il = p ;
m = NaN * zeros(p) ;

for ic = 1:p,
  m ( (ic:p) , ic ) = v ( (ix+1:ix+il) ) ;
  m ( ic, ((ic+1):p)) = m(((ic+1):p),ic)' ;
  ix = ix + il ;
  il = il - 1 ;
end
````

</details>

#### wishirnd · MATLAB · c13fc16f

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`939ff4ad402a0415dca3d2cf790561263eaf9a04724096020deb3ad2ba7eb262`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/wishirnd.m`

<details>
<summary>展开原始代码</summary>

````matlab
% WISHIRND - Wishart Distribution - Random Matrix
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [W] = wishirnd(Sc,nu) 
%
% W = returned random symmetric positive definite matrix
% 
% Sc = p x p symmetric, postitive definite "scale" matrix 
% nu = "degrees of freedom" (when integer)
%    = "number of observations" (when integer)
%    (this routine assumes integer only.)
%
% uses the Odell and Feiveson (1966) algorithm
% as printed in Kennedy and Gentle (1980) 
%
% Note:
%   Different sources use different parameterizations.
%   See INVWISHRND for details.
%
% See also: INVWISHRND, INVWISHIRND

function [W] = wishirnd(Sc,n) 

d = round(n) ; 
[p,p2] = size(Sc) ;
Z = normrnd(0,1,d,p) ;
ZZ = Z'*Z ;
A = chol(Sc) ;
W = A'*ZZ*A ;
````

</details>

#### wishrnd · MATLAB · d94828b9

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`9a96a4009134bbcc908046afe2c8eca48f05db06ceade954b77f7e3c5a243315`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗算法mcmc/wishrnd.m`

<details>
<summary>展开原始代码</summary>

````matlab
% WISHRND - Random Matrix from Wishart Distribution
% Copyright (c) 1998, Harvard University. Full copyright in the file Copyright
%
%   [W] = wishrnd(Sc,nu) 
%
% W = returned random symmetric positive definite matrix
% 
% Sc = p x p symmetric, postitive definite "scale" matrix 
% nu = "degrees of freedom" (when integer)
%    = "number of observation" (when integer)
%    = precision parameter (when non-integer)
%
% uses the Odell and Feiveson (1966) algorithm
% as printed in Kennedy and Gentle (1980) 
%
% Note:
%   Different sources use different parameterizations.
%   See INVWISHRND for details.
%
% See also INVWISHIRND, WISHIRND

function [W] = wishrnd(Sc,nu) 

[p,p2] = size(Sc) ;
z = normrnd(0,1,p,p) ;

% y = chi2rnd(nu-(1:p)) 
% --- note, matlab's chi2 functions do not work for non-integer DF.
% --- thus, we use the gamma equivalent

y = gamrnd( (nu-(1:p))/2, 2 ) ;
b = NaN*Sc ;

% first element
b(1,1) = y(1) ;

if (p>1),
% rest of diagonal
for (j=2:p), 
  zz = z( 1:(j-1) ,j) ;
  b(j,j) = y(j) + zz'*zz ;
end

%first row and column
for (j=2:p),
  b(1,j) = z(1,j) * sqrt(y(1)) ;
  b(j,1) = b(1,j) ;  % mirror
end 
end

if p>2,
for (j=3:p),
for ( i=2:(j-1) ),
  ix = 1:(i-1) ;
  zki = z(ix,i) ;
  zkj = z(ix,j) ;
  b(i,j) = z(i,j)*sqrt(y(i)) + zki'*zkj ;
  b(j,i) = b(i,j) ;   %mirror
end 
end
end

[ A, nonposdef ] = chol(Sc) ;

if nonposdef,
  disp('ERROR: wishrnd: parameter is not positive-definite')
  Argument = A
end

W = A'*b*A ;
````

</details>

#### 中国数学建模-编程交流-概率算法简介 · MATLAB · f23d1103

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`82d836473b732f7246f0cff98ebbed46eeb7a98b0a18180655755006da88eae9`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/概率算法/中国数学建模-编程交流-概率算法简介.txt`

<details>
<summary>展开原始代码</summary>

````matlab
中国数学建模-编程交流-概率算法简介  ├数学思想
  ├编程交流
  ├学术杂谈
  ├English Fans

        登录  注册  搜索  风格  论坛状态  论坛展区  社区服务  社区休闲  网站首页  我能做什么 

      >> VC++,C,Perl,Asp...编程学习,算法介绍. 
       中国数学建模 → 学术区 → 编程交流 → 概率算法简介 

             您是本帖的第 1010 个阅读者       
             * 贴子主题：概率算法简介           

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28

        鲜花(0)  鸡蛋(0)             楼主 



               概率算法简介
              很多算法的每一个计算步骤都是固定的，而在下面我们要讨论的概率算法，允许算法在执行的过程中随机选择下一个计算步骤。许多情况下，当算法在执行过程中面临一个选择时，随机性选择常比最优选择省时。因此概率算法可在很大程度上降低算法的复杂度。 


              概率算法的一个基本特征是对所求解问题的同一实例用同一概率算法求解两次可能得到完全不同的效果。这两次求解问题所需的时间甚至所得到的结果可能会有相当大的差别。一般情况下，可将概率算法大致分为四类:数值概率算法，蒙特卡罗（Monte 
              Carlo）算法，拉斯维加斯（Las Vegas）算法和舍伍德（Sherwood）算法。 

              数值概率算法常用于数值问题的求解。这类算法所得到的往往是近似解。而且近似解的精度随计算时间的增加不断提高。在许多情况下，要计算出问题的精确解是不可能或没有必要的，因此用数值概率算法可得到相当满意的解。 


              蒙特卡罗算法用于求问题的准确解。对于许多问题来说，近似解毫无意义。例如，一个判定问题其解为“是”或“否”，二者必居其一，不存在任何近似解答。又如，我们要求一个整数的因子时所给出的解答必须是准确的，一个整数的近似因子没有任何意义。用蒙特卡罗算法能求得问题的一个解，但这个解未必是正确的。求得正确解的概率依赖于算法所用的时间。算法所用的时间越多，得到正确解的概率就越高。蒙特卡罗算法的主要缺点就在于此。一般情况下，无法有效判断得到的解是否肯定正确。 


              拉斯维加斯算法不会得到不正确的解，一旦用拉斯维加斯算法找到一个解，那么这个解肯定是正确的。但是有时候用拉斯维加斯算法可能找不到解。与蒙特卡罗算法类似。拉斯维加斯算法得到正确解的概率随着它用的计算时间的增加而提高。对于所求解问题的任一实例，用同一拉斯维加斯算法反复对该实例求解足够多次，可使求解失效的概率任意小。 


              舍伍德算法总能求得问题的一个解，且所求得的解总是正确的。当一个确定性算法在最坏情况下的计算复杂性与其在平均情况下的计算复杂性有较大差别时，可以在这个确定算法中引入随机性将它改造成一个舍伍德算法，消除或减少问题的好坏实例间的这种差别。舍伍德算法精髓不是避免算法的最坏情况行为，而是设法消除这种最坏行为与特定实例之间的关联性。 


              本文简要的介绍一下数值概率算法和舍伍德算法。 

              首先来谈谈随机数。随机数在概率算法设计中扮演着十分重要的角色。在现实计算机上无法产生真正的随机数，因此在概率算法中使用的随机数都是一定程度上随机的，即伪随机数。 


              产生随机数最常用的方法是线性同余法。由线性同余法产生的随机序列a1,a2,...,an满足 

              a0=d 

              an=(ban-1+c)mod m n=1,2....... 

              其中,b>=0, c>=0, d>=m。d称为该随机序列的种子。 

              下面我们建立一个随机数类RadomNumber，该类包含一个由用户初始化的种子randSeed。给定种子之后，既可产生与之相应的随机数序列。randseed是一个无符号长整型数，既可由用户指定也可由系统时间自动产生。 


              const unsigned long maxshort=65536L; 
              const unsigned long multiplier=1194211693L; 
              const unsigned long adder=12345L; 

              class RandomNumber 
              { 
              private: 
              //当前种子 
              unsigned long randseed; 
              public: 
              //构造函数，缺省值0表示由系统自动产生种子 
              RandomNumber(unsigned long s=0); 
              //产生0-n-1之间的随机整数 
              unsigned short Random(unsigned long n); 
              //产生[0，1)之间的随机实数 
              double fRandom(void); 
              }; 

              RandomNumber::RandomNumber(unsigned long s) 
              { 
              if(s==0) 
              randseed=time(0); 
              else 
              randseed=s; 
              } 

              unsigned short RandomNumber::Random(unsigned long n) 
              { 
              randseed=multiplier*randseed+adder; 
              return (unsigned short)((randseed>>16)%n); 
              } 

              double RandomNumber::fRandom(void) 
              { 
              return Random(maxshort)/double(maxshort); 
              } 


              函数Random在每次计算时，用线性同余式计算新的种子。它的高16位的随机性较好，将randseed右移16位得到一个0-65535之间的随机整数然后再将此随机整数映射到0-n-1范围内。 


              对于函数fRandom,先用Random(maxshort)产生一个0-(maxshort-1之间的整型随机序列)，将每个整型随机数除以maxshort，就得到[0，1）区间中的随机实数。 


              下面来看看数值概率算法的两个例子： 

              1.用随机投点法计算π 

              设有一半径为r的圆及其外切四边形，如图所示。向该正方形随机投掷n个点。设落入圆内的点在正方形上均匀分布，因而所投入点落入圆内的概率为πr^2/4r^2，所以当n足够大时，k与n之比就逼近这一概率，即π/4。由此可得使用随机投点法计算π值的数值概率算法。具体实现时，只需要在第一次象限计算即可。 




              double Darts(int n) 
              { 
              static RandomNumber dart; 
              int k=0; 


              for(int i=1;i<=n;i++){ 
              double x=dart.fRandom(); 
              double y=dart.fRandom(); 
              if((x*x+y*y)<1) 
              k++; 
              } 
              return 4*k/double(n); 
              } 

              再简单举个舍伍德算法的例子。 

              我们在分析一个算法在平均情况下的计算复杂性时，通常假定算法的输入数据服从某一特定的概率分布。例如，在输入数据是均匀分布时，快速排序算法所需的平均时间是O(n 
              logn)。但是如果其输入已经基本上排好序时，所用时间就大大增加了。此时，可采用舍伍德算法消除算法所需计算时间与输入实例间的这种联系。 


              在这里，我们用舍伍德型选择算法随机的选择一个数组元素作为划分标准。这样既能保证算法的线性时间平均性能又避免了计算拟中位数的麻烦。非递归的舍伍德型算法可描述如下： 


              template<class Type> 
              Type select(Type a[], int l, int r, int k) 
              { 
              static RandomNumber rnd; 

              while(true){ 
              if(l>=r) 
              return a[l]; 
              int i=l, j=l=rnd.Random(r-l+1); 
              Swap(a[i], a[j]); 
              j=r+1; 
              Type pivot=a[l]; 

              while(true) 
              { 
              while(a[++i]<pivot); 
              while(a[--j]>pivot); 
              if(i>=j) 
              break; 
              Swap(a[i], a[j]); 
              } 
              if(j-l+1==k) 
              return pivot; 
              a[l]=a[j]; 
              a[j]=pivot; 
              if(j-l+1<k) 
              { 
              k=k-j+l-1; 
              l=j+1; 
              } 
              else 
              r=j-1; 
              } 
              } 

              template <class Type> 
              Type Select(Type a[], int n, int k) 
              { 
              if(k<1||k>n) 
              throw OutOfBounds(); 
              return select(a, 0, n-1, k); 
              } 


              平时我们一般开始考虑的是一个有着很好平均性能的选择算法，但在最坏情况下对某些实例算法效率较低。这时候我们用概率算法，将上述算法改造成一个舍伍德型算法，使得该算法对任何实例均有效。 


              不过在有些情况下，所给的确定性算法无法直接改造成舍伍德型算法。这时候就可以借助随机预处理技术，不改变原有的确定性算法，仅对其输入进行随机洗牌，同样可以得到舍伍德算法的效果。还是刚才的例子，换一种方法实现： 


              template<class Type> 
              void Shuffle(Type a[], int n) 
              { 
              static RandomNumber rnd; 
              for(int i=1;i<n;i++){ 
              int j=rnd.Random(n-i)+i; 
              Swap(a[i], a[j]); 
              } 
              } 


              在上文里，我们对概率算法中的数值概率算法以及舍伍德算法举例作了简要的介绍，希望能使大家对概率算法有一个初步的认识，并且将这种思想运用到自己平时的编程中。

              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 21:22:19      

              chw1919529  
        
        
        等级：新手上路 
        文章：19
        积分：37
        注册：2003-5-28
                        第 2 楼 



               

              很好

       2004-5-29 18:20:36       

              fmmugw  
        
        
        等级：新手上路 
        文章：1
        积分：54
        门派：☆nudter☆ 
        注册：2004-5-5
                        第 3 楼 



               

              有深度呀
               

       2004-5-30 11:22:34       

              yxabc  
        
        
        等级：新手上路 
        文章：10
        积分：66
        门派：☆nudter☆ 
        注册：2004-5-30
                        第 4 楼 



               
              好多呀 

       2004-5-31 22:10:27       

              guoke135  
        
        
        等级：新手上路 
        文章：4
        积分：57
        门派：☆nudter☆ 
        注册：2004-5-24
                        第 5 楼 



               

              Wonderful    ！！！
               

       2004-6-2 16:41:25       

              akin7738  
        
        
        等级：新手上路 
        文章：5
        积分：58
        门派：☆nudter☆ 
        注册：2004-6-3
                        第 6 楼 



               

                   
              繁复!    精辟

       2004-6-3 16:06:07       

              lwd1981  
        
        
        等级：新手上路 
        文章：91
        积分：353
        门派：☆nudter☆ 
        注册：2004-8-21
                        第 7 楼 



               
              好！ 

       2004-8-24 20:43:33       

      本主题贴数 7   分页：9 1 :  跳转论坛至...╋数学建模  ├数模竞赛  ├新手入门  ├数学工具  ├资源与检索╋学术区  
        ├数学思想  ├编程交流  ├学术杂谈  ├English Fans╋休闲专区  ├灌水搞笑专区  ├神秘园╋本站站务  ├站务讨论  
        ├数模管理区  ├回收站
            Copyright &copy;2002 - 2004 Shumo.Com
            执行时间：171.87500毫秒。查询数据库5次。
            当前模板样式：[默认模板] 
````

</details>

#### Pex16_1 · Python · e40825ee

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`0ba30077ead435b34d870aaefd878fe735cebf64b02778ef61fe1f17532e0177`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_1.py
from numpy.random import rand
import numpy as np
n=100000; a=rand(n); n1=np.sum(a<=0.2)
n2=np.sum((a>0.2) & (a<=0.5)); n3=np.sum(a>0.5)
f=np.array([n1,n2,n3])/n; print(f)
````

</details>

#### Pex16_10 · Python · d6a6de80

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：递推更新水平、趋势或季节项完成预测；重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `oneday`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`26b2c14add786323648931697264f59d01d748bc452e632b6423331860338a8e`
- 语言：Python
- 符号：`oneday`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_10.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_10
from numpy.random import exponential, uniform, seed
from numpy import mean, array, zeros
seed(4)  #进行一致性比较,每次运行结果一样
def oneday():
    W=[0]  #第一个顾客的等待时间
    t0=exponential(10); c0=t0
    g0=c0+uniform(4,15); g=g0
    while g<480:
        t=exponential(10)  #下一个到达时间间隔
        c=c0+t  #下一个到达时刻
        w=max(0,g-c)  #下一个等待时间
        g=max(g,c)+uniform(4,15)  #下一个离开时刻
        c0=c  #把当前到达时刻保存起来
        W.append(w)  #把等待时间保存到列表中
    return len(W), mean(W)
W1=oneday(); print("服务人数和平均等待时间分别为：",W1)
d=1000  #模拟的天数
T=zeros(d); N=zeros(d)
for i in range(d):
    N[i],T[i]=oneday()
print("平均服务人数为：",round(N.mean()))
print("平均等待时间为：",T.mean())
````

</details>

#### Pex16_11 · Python · e7e8ee47

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`6bb097c9e8c544efdc636491f83ff5dfe70f6c81892ebdb5be965df2bb849843`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_11.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_11
import numpy as np
N=100000; mu=[0.1, 0.3, 0.1, 0.1, 1.5, 16, 0.75]
cov=np.diag([(0.005/3)**2,0.005**2,(0.005/3)**2,
    (0.01/3)**2, 0.05**2, (0.8/3)**2, 0.0125**2])
a=np.random.multivariate_normal(mu,cov,size=N)
x1,x2,x3,x4,x5,x6,x7 = a.T
y=174.42*x1/x5*(x3/(x2-x1))**0.85*np.sqrt((1-2.62*(1-0.36*
         (x4/x2)**(-0.56))**(3/2)*(x4/x2)**1.16)/(x6*x7))
d=np.abs(y-1.5)
f=np.sum(9000*(d>=0.3)+1000*((d<0.3)&(d>=0.1)))/N
print("平均损失为：",f)
````

</details>

#### Pex16_2 · Python · 32742274

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`c056b2bff91669e68f6cc896b36aff016d2e54ec4c868082b1199eaf0ac35e3d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_2.py
from numpy.random import rand
import numpy as np
n=10000; a=rand(n);
p=np.array([0.2,0.05,0.01,0.06,0.08,0.1,0.3,0.05,0.03,0.12])
cp=np.cumsum(p); c=[]; c.append(np.sum(a<=cp[0]))
for i in range(1,len(p)):
    c.append(np.sum((a>cp[i-1]) & (a<=cp[i])))
print(c)
````

</details>

#### Pex16_4 · Python · 8a52bb6c

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`38411c9345cc493a038d85b9d4ad4833a4b194078739a10c961e5bc5b7320784`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_4.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_4.py
from numpy.random import uniform
import numpy as np
N=10000000; x=uniform(-1,1,size=N)
y=uniform(-1,1,N); z=uniform(0,1,N)
n=np.sum((x**2+y**2<=1) & (z>=0) & (z<=np.sqrt(1-x**2)))
I=n/N*4; print("I的近似值为：",I)
````

</details>

#### Pex16_5 · Python · 64896e54

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`acbbdc4cc576c3cca2d6ebb4db39f5ade5f78f09c5fe0ad1318cbec84a6e6160`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_5.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_5.py
from numpy.random import rand
import numpy as np
N=1000000; x=rand(N); y=rand(N)
n=np.sum(x**2+y**2<1)
s=4*n/N; print(s)
````

</details>

#### Pex16_6 · Python · 2923d634

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`3977d0bf14378385d24a0001503243f565f801702454d7421bf9fc15d7a99617`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_6.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_6.py
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',size=16); N=10000;
x,y=np.random.uniform(-1,1,size=(2,N))
inside=(x**2+y**2)<=1
mpi=inside.sum()*4/N  #求pi的近似值
error=abs((mpi-np.pi)/np.pi)*100
outside=np.invert(inside)
plt.plot(x[inside],y[inside],'b.')
plt.plot(x[outside],y[outside],'r.')
plt.plot(0,0,label='$\hat\pi$={:4.3f}\nerror={:4.3f}%'.
         format(mpi,error),alpha=0)
plt.axis('square'); plt.legend(); plt.show()
````

</details>

#### Pex16_7 · Python · d54947a9

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`8b6db74adba3ee15b032a1fbeac127f7e0030c08bc0d0d9dcfe2b5f4f2489f0e`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_7.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_7.py
import numpy as np
from scipy.integrate import dblquad
fxy=lambda x,y: 1/(20000*np.pi)*np.exp(-(x**2+y**2)/20000)
bdy=lambda x: 80*np.sqrt(1-x**2/120**2)
p1=dblquad(fxy,-120,120,lambda x:-bdy(x),bdy)
print("概率的数值解为：",p1)
N=1000000; mu=[0,0]; cov=10000*np.identity(2);
a=np.random.multivariate_normal(mu,cov,size=N)
n=((a[:,0]**2/120**2+a[:,1]**2/80**2)<=1).sum()
p2=n/N; print('概率的近似值为：',p2)
````

</details>

#### Pex16_8 · Python · 1d83bd02

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`ffacef175381da13c2e2b40fc9c7a47f39752b0a5f6d68e1d4f1f81876a6e469`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_8.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_8.py
import numpy as np
from matplotlib.pyplot import rc, plot, show
from scipy.optimize import fminbound, fmin
rc('font',size=16)
fx=lambda x:(1-x**3)*np.sin(3*x);
x0=np.linspace(-2*np.pi,2*np.pi,100);
y0=fx(x0); plot(x0,y0); show()
xm1=fminbound(lambda x:-fx(x),-2*np.pi,2*np.pi)
ym1=fx(xm1); print(xm1,ym1,'\n--------------')
xm2=fmin(lambda x:-fx(x), -2*np.pi)
ym2=fx(xm2); print(xm2,ym2,'\n--------------')
x=np.random.uniform(-2*np.pi,2*np.pi,100)
y=fx(x); ym=y.max()
xm=x[y==ym]; print(xm,ym)
````

</details>

#### Pex16_9_1 · Python · 74d9f0fa

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c4ef5d43bbbbc9806dc954cc3ecf148b13378426e58ca7fcffe06d509ea875e1`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_9_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_9_1.py
from scipy.stats import poisson
a=2; b=3; lamda=10; p=1-a/b
u=poisson.ppf(1-a/b,lamda)  #求最佳订购量
p1=poisson.cdf(u-1,lamda)  #p1和p2是为验证最佳购进量
p2=poisson.cdf(u,lamda)
print(u,p1,p,p2)
````

</details>

#### Pex16_9_2 · Python · 50667ee7

- 归属算法：Monte Carlo
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`ec0e60524bc41558dd0e8d81b71c116807c55c5068aa3c1f82e32aa8d6ae9728`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/16第16章  Monte Carlo模拟(Python 程序及数据)/Pex16_9_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex16_9_2.py
import numpy as np
a=2; b=3; lamda=10; M1=0;
u=1; n=10000;
for i in range(1,2*lamda):
    d=np.random.poisson(lamda,n)  #产生n个服从Poiss分布的需求量数据
    M2=np.mean(((b-a)*u*(u<=d)+((b-a)*d-a*(u-d))*(u>d)))  #求平均利润
    if M2>M1: M1=M2; u=u+1;
    else: print('最佳购进量:',u-1); break
````

</details>

#### 蒙特卡洛算法模拟随机数代码 · MATLAB · fbebe856

- 归属算法：Monte Carlo
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Monte Carlo · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Monte Carlo中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`400184b369299357882ead8a38c89327528f3bfcf6a0aa497896cb120afddf3b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/蒙特卡洛算法模拟随机数代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
蒙特卡洛法是经过大量事件的统计结果来实现一些确定性问题的计算。
使用蒙特卡洛法必须使用计算机生成相关分布的随机数。
例如：y = x^2 ，y = 12 - x与X轴在第一象限与X轴围成一个曲边三角形。设计一个随机试验，求该图形的近似值。
x=0:0.25:12
y1=x.^2;
y2=12-x;
plot(x,y1,x,y2)
xlabel('x');ylabel('y');
legend('y1=x^2','y2=12-x');
title('王晨绘制');
axis([0 15 0 15]);
text(3,9,'交点');
grid on

x=unifrnd(0,12,[1,10000000]);
y=unifrnd(0,9,[1,10000000]);
frequency=sum(y<x.^2 & x<=3)+sum(y<12-x & x>=3)
area=12*9*frequency/10^7
````

</details>

### 仿真与随机模型 · 实现

#### clear_boundary · MATLAB · 49ee3da0

- 归属算法：仿真与随机模型
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：4
- 复习入口：[[#仿真与随机模型 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `clear_boundary`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`069a9a92d89feb4dd2c1ab289256d9bdb142a2dd8d6488e3909fd9cd646fccbf`
- 语言：MATLAB
- 符号：`clear_boundary`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/clear_boundary.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/clear_boundary.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/新建文件夹/clear_boundary.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/clear_boundary.m`

<details>
<summary>展开原始代码</summary>

````matlab
function plaza = clear_boundary(input)
plaza = input;
[a,b] = size(plaza);
for i = 1:b
if plaza(a,i) > 0
plaza(a,i) = 0;
end
end
````

</details>

#### compute_output · MATLAB · a3cef034

- 归属算法：仿真与随机模型
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：4
- 复习入口：[[#仿真与随机模型 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `compute_output`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9aca18c4e481770651c26a9b6f1b74cbfd0f1433d0c2f27be9bdcf3f50822046`
- 语言：MATLAB
- 符号：`compute_output`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/compute_output.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/compute_output.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/新建文件夹/compute_output.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/compute_output.m`

<details>
<summary>展开原始代码</summary>

````matlab
function count = compute_output(plaza)
count = 0;
[a, b] = size(plaza);
for j = 1:b
count = count + (plaza(a,j) > 0);
end
````

</details>

#### compute_wait · MATLAB · 25f34c1a

- 归属算法：仿真与随机模型
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：4
- 复习入口：[[#仿真与随机模型 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `compute_wait`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c81807a425590771bf657609a0622b5933cc32e6d8fc2b935aa3d30219376e2c`
- 语言：MATLAB
- 符号：`compute_wait`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/compute_wait.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/compute_wait.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/新建文件夹/compute_wait.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/compute_wait.m`

<details>
<summary>展开原始代码</summary>

````matlab
function time = compute_wait(plaza)
[a,b] = size(plaza);
time = 0;
for i = 1:a
for j = 1:b
time = time + (plaza(i,j) > 0);
end
end
````

</details>

#### 相似实现组 · MATLAB · 9de76572

- 归属算法：仿真与随机模型
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：5
- 复习入口：[[#仿真与随机模型 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：create_entry.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `create_entry`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fcdb894b6098cb7de6dbd3de2f712ce511809dbb6b0fa906591650a43a4e0eea`
- 语言：MATLAB
- 符号：`create_entry`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/create_entry.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/create_entry.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/新建文件夹/create_entry.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/create_entry.m`

<details>
<summary>展开原始代码</summary>

````matlab
function entry = create_entry(T,L)
k = linspace(0,T,34560);
a0 = 41.68;
entry = a0.*ones(size(k));
a = [-16.38, -18.59, 3.572, 7.876, -.5048, -2.97, 0.2518, 0.5785];
b = [12.53, 0.6307, -13.67, 0.4378, 6.93, 0.4869, -1.554, -0.5871];
omega = 0.2513;
for n = 1:8
entry = entry + a(n).*cos(n.*k.*omega) + b(n).*sin(n.*k.*omega);
end
k = k.*1440;
entry = entry./24.*3;
entry = round(entry);
%%% FOR RUSH HOUR SIMULATION %%%
% k = linspace(0,T,T.*60.*24);
% entry = zeros(size(k));
% entry(1:2:length(k)) = L;
````

</details>

##### 变体 2：create_entry.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `create_entry`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0940eb3d95b4e681724907dd1a3af5dac51df3705e6435436c198025c0308428`
- 语言：MATLAB
- 符号：`create_entry`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/create_entry.m`

<details>
<summary>展开原始代码</summary>

````matlab
function entry = create_entry(T,L)
k = linspace(0,T,T.*60.*24);
a0 = 41.68;
entry = a0.*ones(size(k));
a = [-16.38, -18.59, 3.572, 7.876, -.5048, -2.97, 0.2518, 0.5785];
b = [12.53, 0.6307, -13.67, 0.4378, 6.93, 0.4869, -1.554, -0.5871];
omega = 0.2513;
for n = 1:8
    entry = entry + a(n).*cos(n.*k.*omega) + b(n).*sin(n.*k.*omega);
end
k = k.*1440;
entry = entry./24;
entry = round(entry);
%%% FOR RUSH HOUR SIMULATION %%%
% k = linspace(0,T,T.*60.*24);
% entry = zeros(size(k));
% entry(1:2:length(k)) = L;
````

</details>

#### 相似实现组 · MATLAB · 83a55d96

- 归属算法：仿真与随机模型
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：5
- 复习入口：[[#仿真与随机模型 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：create_plaza.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `create_plaza`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3badff0aee692227a10fcc571c375ffb6449b054dd40049991dda05cf6b194b2`
- 语言：MATLAB
- 符号：`create_plaza`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/create_plaza.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/create_plaza.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/新建文件夹/create_plaza.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/create_plaza.m`

<details>
<summary>展开原始代码</summary>

````matlab
function plaza = create_plaza(B, L)
global plazalength;
topgap = 5;
bottomgap = 1;
plaza = zeros(plazalength,B+2);
if mod(B-L,2)==0
for row = 1:plazalength
plaza(row,1) = -888;
plaza(row,2+B) = -888;
end
for col = 2:B/2 - L/2 + 1
for row = 1:(plazalength-1)/2 - topgap * (col-1)
plaza(row,col) = -888;
plaza(row,B+3-col) = -888;
end
end
for col = 2:B/2 - L/2 + 1
for row = (plazalength+3)/2 + bottomgap*(col-1):plazalength
plaza(row,col) = -888;
plaza(row,B+3-col) = -888;
end
end
else
for row = 1:plazalength
plaza(row,1) = -888;
plaza(row,3+B) = -888;
end
for col = 2:(B+1)/2 - L/2 + 1
for row = 1:(plazalength-1)/2 - topgap * (col-1)
plaza(row,col) = -888;
plaza(row,B+4-col) = -888;
end
end
for col = 2:(B+1)/2 - L/2 + 1
for row = (plazalength+3)/2 + bottomgap*(col-1):plazalength
plaza(row,col) = -888;
plaza(row,B+4-col) = -888;
end
end
for row = 1:plazalength
plaza(row,2+B) = -888;
end
end
````

</details>

##### 变体 2：create_plaza.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `create_plaza`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f28a1cc02e093c7d747cf11707186fcaecb850c39e5a0ccf0cd8b51a9a88dd64`
- 语言：MATLAB
- 符号：`create_plaza`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/create_plaza.m`

<details>
<summary>展开原始代码</summary>

````matlab
function plaza = create_plaza(B, L)
global plazalength;
topgap = 5;
bottomgap = 1;
plaza = zeros(plazalength,B+2);
plaza(1:plazalength,[1,2+B]) = -888;
if mod(B-L,2)==0 
    for col = 2:B/2 - L/2 + 1
        for row = 1:(plazalength-1)/2 - topgap * (col-1)
            plaza(row,[col, B+3-col]) = -888;
        end
        for row = (plazalength+3)/2 + bottomgap*(col-1):plazalength
            plaza(row,[col, B+3-col]) = -888;
        end
    end
else
    plaza(1:plazalength, B+3) = -888;
    for col = 2:(B+1)/2 - L/2 + 1
        for row = 1:(plazalength-1)/2 - topgap * (col-1)
            plaza(row, [col, B+4-col]) = -888;
        end
        for row = (plazalength+3)/2 + bottomgap*(col-1):plazalength
            plaza(row, [col, B+4-col]) = -888;
        end
    end
end
````

</details>

#### move_forward · MATLAB · 31573d2c

- 归属算法：仿真与随机模型
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：4
- 复习入口：[[#仿真与随机模型 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `move_forward`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`16b5ae47abc96ab45559e19fbc6c5bcd7b711f2d6cd85ceaed489ab266df0854`
- 语言：MATLAB
- 符号：`move_forward`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/move_forward.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/move_forward.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/新建文件夹/move_forward.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/move_forward.m`

<details>
<summary>展开原始代码</summary>

````matlab
function new = move_forward(old)
new = old; %create new plaza looking same as old
[L, W] = size(new); %get its dimensions
prob = .7;
delay = 3;
%%%DOWNSTREAM OF TOLL BOOTHS %%%
for i = (L-1):-1:((L - 1)/2 + 1)
   for j = 1:W
      if new(i,j) == 1
         if new(i+1, j) ~= 0
            new(i,j) = -2;
         end
         if new(i+1, j) == 0
            if prob >= rand
               new(i,j) = 0;
               new(i+1, j) = 1;
            end
         end
      end
   end
end
%%AT TOLL BOOTHS %%
for i = (L-1)/2
   for j = 1:W
       if new(i,j) > 0
          if new(i,j) == delay
             new(i,j) = 0;
             new(i+1,j) = 1;
          end
          if new(i,j) ~= delay
             if new(i,j) ~= 0
                new(i,j) = new(i,j) + 1;
             end
          end
       end
    end
end
%% UPSTREAM OF TOLL BOOTHS %%
for i = (L-1):-1:1
    for j = 1:W
        if new(i,j) == 1
           if new(i+1, j) ~= 0
              new(i,j) = -2;
           end
           if new(i+1, j) == 0
              if prob >= rand
                 new(i,j) = 0;
                 new(i+1, j) = 1;
              end
           end
        end
    end
end
````

</details>

#### new_cars · MATLAB · 93bbd9dc

- 归属算法：仿真与随机模型
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：4
- 复习入口：[[#仿真与随机模型 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `new_cars`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e2dd245d8b136ede719b6c8099ed161dd4a36ab730a2e553e6a60684f31b717f`
- 语言：MATLAB
- 符号：`new_cars`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/new_cars.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/new_cars.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/新建文件夹/new_cars.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/new_cars.m`

<details>
<summary>展开原始代码</summary>

````matlab
function new = new_cars(B, L, old, entry)
new = old;
if entry > 0
if entry <= L
x = randperm(L);
y = ceil((B-L)/2+1);
for i = 1:entry
new(1, (y + x(i))) = 1;
end
end
if entry > L
y = ceil((B-L)/2+1);
for i = 1:L
new(1,(y + i)) = 1;
end
end
end
````

</details>

#### switch_lanes · MATLAB · 1e89bb35

- 归属算法：仿真与随机模型
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：4
- 复习入口：[[#仿真与随机模型 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于仿真与随机模型中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `switch_lanes`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`78fd6854688bd150afa33a0e162eac1ee39c8f79ac48f131e6ce8784c9be5f52`
- 语言：MATLAB
- 符号：`switch_lanes`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/switch_lanes.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/switch_lanes(1).m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/新建文件夹/switch_lanes.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/switch_lanes.m`

<details>
<summary>展开原始代码</summary>

````matlab
function new = switch_lanes(old)
new = old;
prob = 0.8;
x = rand;
y = rand;
[L,W] = size(new);
for i = (L-1):-1:1
    for j = 2:(W-1)
        if new(i,j) == -2
           if x < prob %chance turn will be made
              if y > 0.5 %will attempt left
                 if new(i, j-1) == 0
                    new(i, j-1) = 1;
                    new(i, j) = 0;
                 elseif new(i, j+1) == 0
                    new(i, j+1) = 1;
                    new(i,j) = 0;
                 elseif new(i,j) == -2
                    new(i,j) = 1;
                 end
              end
              if y <= 0.5 %will attempt right
                 if new(i, j+1) == 0
                    new(i,j+1) = 1;
                    new(i,j) = 0;
                 elseif new(i, j-1) == 0
                    new(i, j-1) = 1;
                    new(i,j) = 0;
                 elseif new(i,j) == -2
                    new(i,j) = 1;
                 end
              end
           end
           if x >= prob
              new(i,j) = 1;
           end
        end
    end
end
````

</details>

### 元胞自动机 · 实现

通过局部状态和邻域规则模拟离散时空系统演化。

#### cellular · MATLAB · 187ead29

- 归属算法：元胞自动机
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`341cbfad5e8e9ec01340441520744b06206cc329d6f2091ca0e649895cdcdf19`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/cellular.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/cellular.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/cellular.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/clear_boundary.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/compute_output.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/compute_wait.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/create_entry.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/create_plaza.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/move_forward.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/new_cars.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/The Booth Tolls for Thee/switch_lanes.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/clear_boundary.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/compute_output.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/compute_wait.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/create_entry.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/create_plaza.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/move_forward.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/new_cars.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/clear_boundary.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/compute_output.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/compute_wait.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/create_entry.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/create_plaza.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/move_forward.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/new_cars.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/The Booth Tolls for Thee/switch_lanes.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear;
figure('position',[50 132 900 400],'doublebuffer','on') 
W = [];
for j=0:7;
B = 6+j; %number booths
L = 6; %number lanes in highway before and after plaza
T = 1; % # hrs to simulate
global plazalength;
plazalength = 101;
plaza = create_plaza(B,L);
set(gcf,'resize','off')
PLAZA=rot90(plaza);
PLAZAA=0.8*ones(40,101,3);
PLAZA(PLAZA==1)=2;
PLAZA(PLAZA==0)=1;
PLAZA(PLAZA==2)=0;
PLAZA(PLAZA~=0&PLAZA~=1)=0.8;
PLAZAA(20-ceil(B/2):21+ceil(B/2),:,1)=PLAZA;
PLAZAA(20-ceil(B/2):21+ceil(B/2),:,2)=PLAZA;
PLAZAA(20-ceil(B/2):21+ceil(B/2),:,3)=PLAZA;
H=image(PLAZAA);
axis off
entry_vector = create_entry(T,L);
waiting_time = 0;
output = 0;
for i = 1:T*1440
plaza = move_forward(plaza); %move cars forward
plaza = new_cars(B, L, plaza, entry_vector(1,i)); %allow new cars to enter
plaza = switch_lanes(plaza); %allow lane changes
waiting_time = waiting_time + compute_wait(plaza); %compute waiting time during timestep i
output = output + compute_output(plaza);
plaza = clear_boundary(plaza);
PLAZA=rot90(plaza);
PLAZA(PLAZA==1)=2;
PLAZA(PLAZA==0)=1;
PLAZA(PLAZA==2)=0;
PLAZA(PLAZA~=0&PLAZA~=1)=0.8;
PLAZAA(20-ceil(B/2):21+ceil(B/2),:,1)=PLAZA;
PLAZAA(20-ceil(B/2):21+ceil(B/2),:,2)=PLAZA;
PLAZAA(20-ceil(B/2):21+ceil(B/2),:,3)=PLAZA;
plaza50=PLAZAA(:,50,1);plaza50(plaza50==1)=0;PLAZAA(:,50,2)=plaza50;PLAZAA(:,50,3)=plaza50;
set(H,'CData',PLAZAA);
set(gcf,'position',[50 132 900 400])
pause(0.01)
end
plaza;
W=[W waiting_time]
end
````

</details>

#### calife · MATLAB · 3872ed2c

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`a83afc6b7294413541e6455987490c9efedd6135ded90ef2ad5263778a6cb5bb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/calife.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/calife.m`

<details>
<summary>展开原始代码</summary>

````matlab

%Conway's life with GUI

clf
clear all

%=============================================
%build the GUI
%define the plot button
plotbutton=uicontrol('style','pushbutton',...
   'string','Run', ...
   'fontsize',12, ...
   'position',[100,400,50,20], ...
   'callback', 'run=1;');

%define the stop button
erasebutton=uicontrol('style','pushbutton',...
   'string','Stop', ...
   'fontsize',12, ...
   'position',[200,400,50,20], ...
   'callback','freeze=1;');

%define the Quit button
quitbutton=uicontrol('style','pushbutton',...
   'string','Quit', ...
   'fontsize',12, ...
   'position',[300,400,50,20], ...
   'callback','stop=1;close;');

number = uicontrol('style','text', ...
    'string','1', ...
   'fontsize',12, ...
   'position',[20,400,50,20]);
    

%=============================================
%CA setup

n=128;

%initialize the arrays
z = zeros(n,n);
cells = z;
sum = z;
%set a few cells to one
cells(n/2,.25*n:.75*n) = 1;
cells(.25*n:.75*n,n/2) = 1;

%cells(.5*n-1,.5*n-1)=1;
%cells(.5*n-2,.5*n-2)=1;
%cells(.5*n-3,.5*n-3)=1;
cells = (rand(n,n))<.5 ;
%how long for each case to stability or simple oscillators

%build an image and display it
imh = image(cat(3,cells,z,z));
set(imh, 'erasemode', 'none')
axis equal
axis tight

%index definition for cell update
x = 2:n-1;
y = 2:n-1;

%Main event loop
stop= 0; %wait for a quit button push
run = 0; %wait for a draw 
freeze = 0; %wait for a freeze

while (stop==0) 
    
    if (run==1)
        %nearest neighbor sum
        sum(x,y) = cells(x,y-1) + cells(x,y+1) + ...
            cells(x-1, y) + cells(x+1,y) + ...
            cells(x-1,y-1) + cells(x-1,y+1) + ...
            cells(3:n,y-1) + cells(x+1,y+1);
        % The CA rule
        cells = (sum==3) | (sum==2 & cells);       
        %draw the new image
        set(imh, 'cdata', cat(3,cells,z,z) )
        %update the step number diaplay
        stepnumber = 1 + str2num(get(number,'string'));
        set(number,'string',num2str(stepnumber))
    end
    
    if (freeze==1)
        run = 0;
        freeze = 0;
    end
    
    drawnow  %need this in the loop for controls to work
    
end
    
    
````

</details>

#### 相似实现组 · MATLAB · f24db7ce

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：3
- 原始来源文件：3
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：forest.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`ae7533c05161b666110329c521bc8f8f466e46cf095b12e0a76ae0a9ef32d0a1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/1月13日课件（元胞自动机）/程序/forest.m`

<details>
<summary>展开原始代码</summary>

````matlab
%
%CA driver
%
%forest fire

clf
clear all

n=100;

Plightning = .000005;
Pgrowth = .01; %.01

z=zeros(n,n);
o=ones(n,n);
veg=z;
sum=z;


imh = image(cat(3,z,veg*.02,z));
set(imh, 'erasemode', 'none')
axis equal
axis tight
 
% burning -> empty
% green -> burning if one neigbor burning or with prob=f (lightning)
% empty -> green with prob=p (growth)
% veg = {empty=0 burning=1 green=2}
for i=1:3000
    %nearby fires?
    
     sum = (veg(1:n,[n 1:n-1])==1) + (veg(1:n,[2:n 1])==1) + ...
           (veg([n 1:n-1], 1:n)==1) + (veg([2:n 1],1:n)==1) ;
 
    veg = ...
         2*(veg==2) - ((veg==2) & (sum>0 | (rand(n,n)<Plightning))) + ...
         2*((veg==0) & rand(n,n)<Pgrowth) ;
     
    set(imh, 'cdata', cat(3,(veg==1),(veg==2),z) )
    drawnow
end
````

</details>

##### 变体 2：forest.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`a4906d30c69a5d4538a0c5f454e245ce451ba52c1f34fe81e9c6e6733825539d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/1月13日课件（元胞自动机）/程序/forest.m`

<details>
<summary>展开原始代码</summary>

````matlab
%
%CA driver
%
%forest fire

clf
clear all

n=300;%矩阵大小

Plightning = .000005;%被闪电几种概率
Pgrowth = 0; %空地长出新树的概率
%Pgrowth = 0.001;

z=zeros(n,n);
o=ones(n,n);

veg=z+2;
sum=z;


%imh = image(cat(3,z,veg*.02,z));
imh = image(cat(3,z,o,z));
set(imh, 'erasemode', 'none')
axis equal
axis tight
 
% burning -> empty
% green -> burning if one neigbor burning or with prob=f (lightning)
% empty -> green with prob=p (growth)
% veg = {empty=0 burning=1 green=2}
  set(imh, 'cdata', cat(3,z,o,z) )
  drawnow
  moni=z;
 for j=100:110
    moni(j,j)=1;
 end
for i=1:3000
    %nearby fires?
    
    sum = (veg(1:n,[n 1:n-1])==1) + (veg(1:n,[2:n 1])==1) + ...
           (veg([n 1:n-1], 1:n)==1) + (veg([2:n 1],1:n)==1) ;
 
    veg = ...
         2*(veg==2) - ((veg==2) & (sum>0 |moni))...
         +2*((veg==0) & rand(n,n)<Pgrowth) ;


    set(imh, 'cdata', cat(3,(veg==1),(veg==2),z) )
    drawnow
end
````

</details>

##### 变体 3：forest.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`ba4647a9516eca7f8bc902bbc7de9ce5862cc877346d197b25849c6550f67eda`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/cellular automata Matlab code/forest.m`

<details>
<summary>展开原始代码</summary>

````matlab
%
%CA driver
%
%forest fire

clf
clear all

n=300;

Plightning = .000005;
Pgrowth = .01; %.01

z=zeros(n,n);
o=ones(n,n);
veg=z;
sum=z;


imh = image(cat(3,z,veg*.02,z));
set(imh, 'erasemode', 'none')
axis equal
axis tight
 
% burning -> empty
% green -> burning if one neigbor burning or with prob=f (lightning)
% empty -> green with prob=p (growth)
% veg = {empty=0 burning=1 green=2}
while 1
    %nearby fires?
    
     sum = (veg(1:n,[n 1:n-1])==1) + (veg(1:n,[2:n 1])==1) + ...
           (veg([n 1:n-1], 1:n)==1) + (veg([2:n 1],1:n)==1) ;
 
    veg = ...
         2*(veg==2) - ((veg==2) & (sum>0 | (rand(n,n)<Plightning))) + ...
         2*((veg==0) & rand(n,n)<Pgrowth) ;
     
    set(imh, 'cdata', cat(3,(veg==1),(veg==2),z) )
    drawnow
end
````

</details>

#### cellular · MATLAB · 9777da29

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`8a8c4a378dd48006909f5bb92dabfc64cf7d7ca55cb382dba61036e9dad6ec72`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/cellular.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/compute_output.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/compute_wait.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/create_entry.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/create_plaza.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/move_forward.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/new_cars.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/show_plaza.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/switch_lanes.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear all;
W = 0;
for j = 6
    B = 6+j; %number booths
    L = 6; %number lanes in highway before and after plaza
    T = 24; % # hrs to simulate
    global plazalength;
    plazalength = 101;
    plaza = create_plaza(B,L);
    %====================================================
    h = show_plaza(plaza,B,NaN);                        %    
    %====================================================
    entry_vector = create_entry(T,L);
    waiting_time = 0;
    output = 0;
    for i = 1:T*1440
        plaza = move_forward(plaza); %move cars forward
        plaza = new_cars(plaza, entry_vector(i)); %allow new cars to enter
        plaza = switch_lanes(plaza); %allow lane changes
        %compute waiting time during timestep i
        waiting_time = waiting_time + compute_wait(plaza); 
        output = output + compute_output(plaza);
        %===============================================
        h = show_plaza(plaza,B,h);                     %
        drawnow 
        %===============================================
        plaza = clear_boundary(plaza);
    end
    show_plaza(plaza,B,h); 
    W(j+1) = waiting_time/output;
    xlabel({strcat('B = ',num2str(B)), ...
    strcat('mean cost time = ', num2str(round(W(j+1))))})
end
````

</details>

#### clear_boundary(1) · MATLAB · fff25055

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `clear_boundary`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0425d860f5b5f85e2a5022f2c461a8c99be8db8f4876300660191202cab4518f`
- 语言：MATLAB
- 符号：`clear_boundary`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/clear_boundary(1).m`

<details>
<summary>展开原始代码</summary>

````matlab
function plaza = clear_boundary(plaza)

[a,b] = size(plaza);
for i = 1:b
    if plaza(a,i) > 0
        plaza(a,i) = 0;
    end
end
````

</details>

#### compute_output · MATLAB · 395f9d94

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `compute_output`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ed4a8960effe737cee89e054e9642a56cd71af31ea58922cf472639a7ef74398`
- 语言：MATLAB
- 符号：`compute_output`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/compute_output.m`

<details>
<summary>展开原始代码</summary>

````matlab
function count = compute_output(plaza)
count = sum(plaza(end,:)>0);
````

</details>

#### compute_wait · MATLAB · 2c9338ea

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `compute_wait`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6c71012fc482097d78576fd2f945a847b3f752e00155b112d6d08b82d87d06d1`
- 语言：MATLAB
- 符号：`compute_wait`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/compute_wait.m`

<details>
<summary>展开原始代码</summary>

````matlab
function time = compute_wait(plaza)
time = sum(sum(plaza>0));
````

</details>

#### move_forward · MATLAB · 27e8730c

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `move_forward`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`646cee65b077f57385dd56a7ab29e22de45938b4ab78c9f29bec869bda3a6d0a`
- 语言：MATLAB
- 符号：`move_forward`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/move_forward.m`

<details>
<summary>展开原始代码</summary>

````matlab
function plaza = move_forward(plaza)

[L, W] = size(plaza); %get its dimensions
prob = .7;
delay = 3;
%%DOWNSTREAM OF TOLL BOOTHS %%
for i = (L-1):-1:((L + 1)/2 + 1)
    for j = 1:W
        if plaza(i,j) == 1
            if plaza(i+1, j) ~= 0
                plaza(i,j) = -2;
            elseif prob >= rand
                plaza(i,j) = 0;
                plaza(i+1, j) = 1;
            end
        end
    end
end
%%AT TOLL BOOTHS %%
for i = (L+1)/2
    for j = 1:W
        if plaza(i,j) > 0
            if plaza(i,j) == delay
                plaza(i,j) = 0;
                plaza(i+1,j) = 1;
            else
                plaza(i,j) = plaza(i,j) + 1;
            end
        end
    end
end
%% UPSTREAM OF TOLL BOOTHS %%
for i = (L-1)/2:-1:1
    for j = 1:W
        if plaza(i,j) == 1
            if plaza(i+1, j) ~= 0
                plaza(i,j) = -2;
            elseif prob >= rand
                plaza(i,j) = 0;
                plaza(i+1, j) = 1;
            end
        end
    end
end
````

</details>

#### new_cars · MATLAB · bb5fd788

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `new_cars`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`40993ed9babedf6488730284681659e53d372d93f62d0b8e9737897ad128d220`
- 语言：MATLAB
- 符号：`new_cars`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/new_cars.m`

<details>
<summary>展开原始代码</summary>

````matlab
function plaza = new_cars(plaza, entry)

if entry > 0 
    % Find the empty lanes of the entrance where a new car can be add.
    unoccupied = find( plaza(1,:) == 0 );
    n = length(unoccupied); % number of available lanes
    x = randperm(n);
    for i = 1:min(entry,n)
         plaza(1, unoccupied(x(i)) ) = 1;
    end
end
````

</details>

#### show_plaza · MATLAB · 5b82e0d9

- 归属算法：元胞自动机
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于元胞自动机中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `show_plaza`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`db41189c7c4323f6b52688fd1ee7ad59ff8bf8937441ced98cf6e41bafd0a56d`
- 语言：MATLAB
- 符号：`show_plaza`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/show_plaza.m`

<details>
<summary>展开原始代码</summary>

````matlab
function h = show_plaza(plaza, B, h)
[L, W] = size(plaza); %get its dimensions
temp = plaza;
temp(temp==1) = 0;

PLAZA(:,:,1) = plaza;
PLAZA(:,:,2) = plaza;
PLAZA(:,:,3) = temp;

PLAZA = 1-PLAZA;
PLAZA(PLAZA>=888)=0.3;

for i = (L+1)/2
    for j = ceil(W/2)-ceil(B/2)+1:ceil(W/2)+floor(B/2)
        if plaza(i,j) == 0;
            PLAZA(i,j,1) =0;
            PLAZA(i,j,2) =1;
            PLAZA(i,j,3) =0;
        else
            PLAZA(i,j,1) =1;
            PLAZA(i,j,2) =0;
            PLAZA(i,j,3) =0;
        end
    end
end

if ishandle(h)
    set(h,'CData',PLAZA)
else
    figure('position',[20,50,200,700])
    h = imagesc(PLAZA);    
    hold on
    plot([[0:W]',[0:W]']+0.5,[0,L]+0.5,'k')
    plot([0,W]+0.5,[[0:L]',[0:L]']+0.5,'k')
    axis image
    set(gca,'xtick',[]);
    set(gca,'ytick',[]);
end
````

</details>

#### switch_lanes · MATLAB · 6a9650bc

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `switch_lanes`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c7c104033d8128b6e8cf793c76e61b0a0dbeff64e9cdc8211ae6c0914500051f`
- 语言：MATLAB
- 符号：`switch_lanes`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/MatLab code/switch_lanes.m`

<details>
<summary>展开原始代码</summary>

````matlab
function plaza = switch_lanes(plaza)
prob = 0.8;
[L,W] = size(plaza);
for i = (L-1):-1:1
    for j = 2:(W-1)
        if plaza(i,j) == -2
            if rand < prob %chance turn will be made
                if rand > 0.5 %will attempt left
                    if plaza(i, j-1) == 0 
                        plaza(i, j-1) = 1;
                        plaza(i, j) = 0;
                    elseif plaza(i, j+1) == 0
                        plaza(i, j+1) = 1;
                        plaza(i,j) = 0;
                    else
                        plaza(i,j) = 1;
                    end
                else %will attempt right
                    if plaza(i, j+1) == 0
                        plaza(i,j+1) = 1;
                        plaza(i,j) = 0;
                    elseif plaza(i, j-1) == 0
                        plaza(i, j-1) = 1;
                        plaza(i,j) = 0;
                    else
                        plaza(i,j) = 1;
                    end
                end
            else
                plaza(i,j) = 1;
            end
        end
    end
end
````

</details>

#### GameofLife · MATLAB · c7bd628b

- 归属算法：元胞自动机
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`ef80f56639ddc5cd17e492dd7aadd1ce275b40911925114cefb62d456d03c3f6`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/cellular automata Matlab code/GameofLife.m`

<details>
<summary>展开原始代码</summary>

````matlab
% life.m - Conway's Game of Life
%
% A grid of dead and living cells is made.
% Cells are born to three adjacent parents,
% and die of overcrowding or loneliness.
%        Iain Haslam, December 2005
 
len=15; GRID=int8(rand(len,len));
up=[2:len 1]; down=[len 1:len-1]; %the world is round
%colormap(gray(2));
figure('position',[100,100, 400,400])
subplot('position',[0.05,0.05,0.9,0.9])
for i=1:50
    neighbours=GRID(up,:)+GRID(down,:)+GRID(:,up)+GRID(:,down)+...
        GRID(up,up)+GRID(up,down)+GRID(down,up)+GRID(down,down);
    GRID = neighbours==3 | GRID & neighbours==2;
    R=1-GRID;
    G=1-GRID;
    B=1-GRID;
    R(R==0)=0.3;
    G(G==0)=0.3;
    B(B==0)=0.3;
    
    image(cat(3,R,G, B)); 
    hold on
    for j = 0.5:15.5
    plot([0.5,15.5],[j,j],'k','linewidth',2);
    plot([j,j],[0.5,15.5],'k','linewidth',2);
    end
    axis image;
    axis off
    drawnow
end
````

</details>

#### excitable · MATLAB · aba81c0e

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`9867fc80fd56d34eeb8083ccddd3d107f4e62664882a6b9fa54e8ed37b05878f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/cellular automata Matlab code/excitable.m`

<details>
<summary>展开原始代码</summary>

````matlab
%
%CA driver
%
%excitable media

clf
clear all

n=128;

z=zeros(n,n);
cells=z;

cells = (rand(n,n))<.1 ;
%cells(n/2,n*.25:n*.75) = 1;
%cells(n*.25:n*.75,n/2) = 1;
sum=z;

imh = image(cat(3,cells,z,z));
set(imh, 'erasemode', 'none')
axis equal
axis tight

x = [2:n-1];
y = [2:n-1];

t = 6; % center value=6; 7 makes fast pattern; 5 analiating waves
t1 = 3; % center value=3
for i=1:1200
    
    
    sum(x,y) = ((cells(x,y-1)>0)&(cells(x,y-1)<t)) + ((cells(x,y+1)>0)&(cells(x,y+1)<t)) + ...
        ((cells(x-1, y)>0)&(cells(x-1, y)<t)) + ((cells(x+1,y)>0)&(cells(x+1,y)<t)) + ...
        ((cells(x-1,y-1)>0)&(cells(x-1,y-1)<t)) + ((cells(x-1,y+1)>0)&(cells(x-1,y+1)<t)) + ...
        ((cells(x+1,y-1)>0)&(cells(x+1,y-1)<t)) + ((cells(x+1,y+1)>0)&(cells(x+1,y+1)<t));
       
    cells = ((cells==0) & (sum>=t1)) + ...
            2*(cells==1) + ...
            3*(cells==2) + ...
            4*(cells==3) + ...
            5*(cells==4) + ...
            6*(cells==5) +...
            7*(cells==6) +...
            8*(cells==7) +...
            9*(cells==8) +...
            0*(cells==9);
    
    set(imh, 'cdata', cat(3,z,cells/10,z) )
    drawnow
end
````

</details>

#### gas2 · MATLAB · 91e901bc

- 归属算法：元胞自动机
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于元胞自动机中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`b0fd0235425e3311e4b740e526d6f445cf0a017454fb687236ff88b863fc8538`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机/论文讲解1-15（元胞自动机实例）/cellular automata Matlab code/gas2.m`

<details>
<summary>展开原始代码</summary>

````matlab

%CA driver
%HPP-gas

clear all
clf

nx=52; %must be divisible by 4
ny=100;

z=zeros(nx,ny);
o=ones(nx,ny);
sand = z ;
sandNew = z;
gnd = z ;
diag1 = z;
diag2 = z;
and12 = z;
or12 = z;
sums = z;
orsum = z;

gnd(1:nx,ny-3)=1 ; % right ground line
gnd(1:nx,3)=1 ; % left ground line
gnd(nx/4:nx/2-2,ny/2)=1; %the hole line
gnd(nx/2+2:nx,ny/2)=1; %the hole line
gnd(nx/4, 1:ny) = 1; %top line
gnd(3*nx/4, 1:ny) = 1 ;%bottom line

%fill the left side
r = rand(nx,ny);
sand(nx/4+1:3*nx/4-1, 4:ny/2-1) = r(nx/4+1:3*nx/4-1, 4:ny/2-1)<0.3;
%sand(nx/4+1:3*nx/4-1, ny*.75:ny-4) = r(nx/4+1:3*nx/4-1, ny*.75:ny-4)<0.75;
%sand(nx/2,ny/2) = 1;
%sand(nx/2+1,ny/2+1) = 1;

imh = image(cat(3,z,sand,gnd));
set(imh, 'erasemode', 'none')
axis equal
axis tight
 

for i=1:1000
    p=mod(i,2); %margolis neighborhood
   
    %upper left cell update
    xind = [1+p:2:nx-2+p];
    yind = [1+p:2:ny-2+p];
    
    %See if exactly one diagonal is ones
    %only (at most) one of the following can be true!
    diag1(xind,yind) = (sand(xind,yind)==1) & (sand(xind+1,yind+1)==1) & ...
        (sand(xind+1,yind)==0) & (sand(xind,yind+1)==0);
    
    diag2(xind,yind) = (sand(xind+1,yind)==1) & (sand(xind,yind+1)==1) & ...
        (sand(xind,yind)==0) & (sand(xind+1,yind+1)==0);
    
    %The diagonals both not occupied by two particles
    and12(xind,yind) = (diag1(xind,yind)==0) & (diag2(xind,yind)==0);
    
    %One diagonal is occupied by two particles
    or12(xind,yind)  = diag1(xind,yind) | diag2(xind,yind);
    
    %for every gas particle see if it near the boundary
    sums(xind,yind) = gnd(xind,yind) | gnd(xind+1,yind) | ...
                        gnd(xind,yind+1) | gnd(xind+1,yind+1) ;
    
    % cell layout:
    % x,y    x+1,y
    % x,y+1  x+1,y+1
    %If (no walls) and (diagonals are both not occupied)  
    %then there is no collision, so move opposite cell to current cell
    %If (no walls) and (only one diagonal is occupied) 
    %then there is a collision so move ccw cell to the current cell
    %If (a wall) 
    %then don't change the cell (causes a reflection)
    sandNew(xind,yind) = ...
        (and12(xind,yind)  & ~sums(xind,yind) & sand(xind+1,yind+1)) + ... 
        (or12(xind,yind) & ~sums(xind,yind) & sand(xind,yind+1)) + ...
        (sums(xind,yind) & sand(xind,yind)); 
        
    sandNew(xind+1,yind) = ...
        (and12(xind,yind)  & ~sums(xind,yind) & sand(xind,yind+1)) + ... 
        (or12(xind,yind) & ~sums(xind,yind) & sand(xind,yind))+ ...
        (sums(xind,yind) & sand(xind+1,yind));  
        
    sandNew(xind,yind+1) = ...    
        (and12(xind,yind)  & ~sums(xind,yind) & sand(xind+1,yind)) + ... 
        (or12(xind,yind) & ~sums(xind,yind) & sand(xind+1,yind+1))+ ...
        (sums(xind,yind) & sand(xind,yind+1)); 
        
     sandNew(xind+1,yind+1) = ...    
        (and12(xind,yind)  & ~sums(xind,yind) & sand(xind,yind)) + ... 
        (or12(xind,yind) & ~sums(xind,yind) & sand(xind+1,yind))+ ...
        (sums(xind,yind) & sand(xind+1,yind+1)); 
    
    sand = sandNew;
    
    set(imh, 'cdata', cat(3,z,sand,gnd) )
    drawnow
end
````

</details>

#### ts · MATLAB · 92b96aad

- 归属算法：元胞自动机
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#元胞自动机 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于元胞自动机中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `ts`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ca4ff3b32c8c45f4db0b087e344338444e9235620682c145b15a9854a7a89597`
- 语言：MATLAB
- 符号：`ts`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/元胞自动机代码可直接运行（建议学会基本原理再用）/ts.m`

<details>
<summary>展开原始代码</summary>

````matlab
function ts(simulation_steps,history)
figTS=figure;
axes1 = axes('Parent',figTS,'FontSize',12,'FontName','Arial');
for i=1:1:simulation_steps
    [~,col]=find(history(i,:)==1);
    plot(i*ones(1,length(col)),col,'k.');
    hold on
end
xlabel('Time','FontSize',12,'FontName','Arial')
ylabel('Space','FontSize',12,'FontName','Arial')
````

</details>

### 排队论 · 实现

#### 排队论算法代码 · MATLAB · 9242c0d2

- 归属算法：排队论
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#排队论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于排队论中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `MMSmteam`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e4775207ebdc5ac3af39588e585e34d57d0302c2e3bd315796a63ff7dbfdd6b6`
- 语言：MATLAB
- 符号：`MMSmteam`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/排队论算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
步骤：
（1）确定问题是否属于排队论领域
（2）确定修理工个数s
（3）确定机器源数m
（4）找到时间终止点T
（5）带入模型即可
function out=MMSmteam(s,m,mu1,mu2,T)
%M/M/S/m排队模型
%s——修理工个数
%m——机器源数
%T——时间终止点
%mu1——机器离开-到达时间服从指数分布
%mu2——修理时间服从指数分布
%事件表：
%  p_s——修理工空闲概率
%   arrive_time——机器到达事件
%   leave_time——机器离开事件
%mintime——事件表中的最近事件
%current_time——当前时间
%L——队长
%tt——时间序列
%LL——队长序列
%c——机器到达时间序列
%b——修理开始时间序列
%e——机器离开时间序列
%a_count——到达机器数
%b_count——修理机器数
%e_count——损失机器数

%初始化

arrive_time=exprnd(mu1,1,m);
arrive_time=sort(arrive_time);
leave_time=[];
current_time=0;
L=0;
LL=[L];
tt=[current_time];
c=[];
b=[];
e=[];
a_count=0;
%循环
while min([arrive_time,leave_time])<T
    current_time=min([arrive_time,leave_time]);
    tt=[tt,current_time];    %记录时间序列
    if current_time==min(arrive_time)      %机器到达子过程
        arrive_time(1)=[];  % 从事件表中抹去机器到达事件
        a_count=a_count+1; %累加到达机器数
        if  L<s            %有空闲修理工
            L=L+1;        %更新队长
            c=[c,current_time];%记录机器到达时间序列
            b=[b,current_time];%记录修理开始时间序列
            leave_time=[leave_time,current_time+exprnd(mu2)];%产生新的机器离开事件
            leave_time=sort(leave_time);%离开事件表排序
        else             %无空闲修理工
            L=L+1;        %更新队长
            c=[c,current_time];%记录机器到达时间序列
        end
    else                   %机器离开子过程
            leave_time(1)=[];%从事件表中抹去机器离开事件
            arrive_time=[arrive_time,current_time+exprnd(mu1)];
            arrive_time=sort(arrive_time);%到达事件表排序
            e=[e,current_time];%记录机器离开时间序列
            if L>s   %有机器等待
                L=L-1;        %更新队长
                b=[b,current_time];%记录修理开始时间序列
                leave_time=[leave_time,current_time+exprnd(mu2)];%产生新的机器离开事件
                leave_time=sort(leave_time);%离开事件表排序
            else    %无机器等待
                L=L-1;        %更新队长
            end
    end
    LL=[LL,L];   %记录队长序列
end
Ws=sum(e-c(1:length(e)))/length(e);
Wq=sum(b-c(1:length(b)))/length(b);
Wb=sum(e-b(1:length(e)))/length(e);
Ls=sum(diff([tt,T]).*LL)/T;
Lq=sum(diff([tt,T]).*max(LL-s,0))/T;
p_s=1.0/(factorial(m)/factorial(m).*(mu2/mu1)^0+factorial(m)/factorial(m-1).*(mu2/mu1)^1+factorial(m-2)/factorial(m-1).*(mu2/mu1)^2+factorial(m)/factorial(m-2).*(mu2/mu1)^2+factorial(m)/factorial(m-4).*(mu2/mu1)^4+factorial(m)/factorial(m-5).*(mu2/mu1)^5);
fprintf('修理工空闲概率:%d\n',p_s)%修理工空闲概率
fprintf('到达机器数:%d\n',a_count)%到达机器数
fprintf('平均逗留时间:%f\n',sum(e-c(1:length(e)))/length(e))%平均逗留时间
fprintf('平均等待时间:%f\n',sum(b-c(1:length(b)))/length(b))%平均等待时间
fprintf('平均修理时间:%f\n',sum(e-b(1:length(e)))/length(e))%平均修理时间
fprintf('平均队长:%f\n',sum(diff([tt,T]).*LL)/T)%平均队长
fprintf('平均等待队长:%f\n',sum(diff([tt,T]).*max(LL-s,0))/T)%平均等待队长
for i=0:m
     p(i+1)=sum((LL==i).*diff([tt,T]))/T;%队长为i的概率
     fprintf('队长为%d的概率:%f\n',i,p(i+1));
end
fprintf('机器不能马上得到修理的概率:%f\n',1-sum(p(1:s)))%机器不能马上得到修理的概率
out=[Ws,Wq,Wb,Ls,Lq,p];


演示代码
clear 
clc 
%***************************************** 
%初始化顾客源 
%***************************************** 
%总仿真时间 
Total_time = 10; 
%队列最大长度 
N = 10000000000; 
%到达率与服务率 
lambda = 10; 
mu = 6; 
%平均到达时间与平均服务时间 
arr_mean = 1/lambda; 
ser_mean = 1/mu; 
arr_num = round(Total_time*lambda*2); 
events = []; 
%按负指数分布产生各顾客达到时间间隔 
events(1,:) = exprnd(arr_mean,1,arr_num); 
%各顾客的到达时刻等于时间间隔的累积和 
events(1,:) = cumsum(events(1,:)); 
%按负指数分布产生各顾客服务时间 
events(2,:) = exprnd(ser_mean,1,arr_num); 
%计算仿真顾客个数，即到达时刻在仿真时间内的顾客数 
len_sim = sum(events(1,:)<= Total_time); 
%***************************************** 
%计算第 1个顾客的信息 
%***************************************** 
%第 1个顾客进入系统后直接接受服务，无需等待 
events(3,1) = 0; 
%其离开时刻等于其到达时刻与服务时间之和 
events(4,1) = events(1,1)+events(2,1); 
%其肯定被系统接纳，此时系统内共有 
%1个顾客，故标志位置1 
events(5,1) = 1; 
%其进入系统后，系统内已有成员序号为 1 
member = [1]; 
for i = 2:arr_num 
%如果第 i个顾客的到达时间超过了仿真时间，则跳出循环 

if events(1,i)>Total_time 

break; 

else 
number = sum(events(4,member) > events(1,i)); 
%如果系统已满，则系统拒绝第 i个顾客，其标志位置 0 
if number >= N+1 
events(5,i) = 0; 
%如果系统为空，则第 i个顾客直接接受服务 
else 
if number == 0 
%其等待时间为 0

2009.1516

%PROGRAMLANGUAGEPROGRAMLANGUAGE
events(3,i) = 0; 
%其离开时刻等于到达时刻与服务时间之和 
events(4,i) = events(1,i)+events(2,i); 
%其标志位置 1 
events(5,i) = 1; 
member = [member,i]; 
%如果系统有顾客正在接受服务，且系统等待队列未满，则 第 i个顾客进入系统 

else len_mem = length(member); 
%其等待时间等于队列中前一个顾客的离开时刻减去其到 达时刻 
events(3,i)=events(4,member(len_mem))-events(1,i); 
%其离开时刻等于队列中前一个顾客的离开时刻加上其服 
%务时间 
events(4,i)=events(4,member(len_mem))+events(2,i); 
%标识位表示其进入系统后，系统内共有的顾客数 
events(5,i) = number+1; 
member = [member,i]; 
end 
end 

end 
end 
%仿真结束时，进入系统的总顾客数 
len_mem = length(member); 
%***************************************** 
%输出结果 
%***************************************** 
%绘制在仿真时间内，进入系统的所有顾客的到达时刻和离 
%开时刻曲线图（stairs：绘制二维阶梯图） 
stairs([0 events(1,member)],0:len_mem); 
hold on; 
stairs([0 events(4,member)],0:len_mem,'.-r'); 
legend('到达时间 ','离开时间 '); 
hold off; 
grid on; 
%绘制在仿真时间内，进入系统的所有顾客的停留时间和等 
%待时间曲线图（plot：绘制二维线性图） 
figure; 
plot(1:len_mem,events(3,member),'r-*',1: len_mem,events(2,member)+events(3,member),'k-'); 
legend('等待时间 ','停留时间 '); 
grid on;
````

</details>

<!-- END AUTO-INTEGRATED-CODE -->
