---
type: topic-hub
topic_tag: topic/智能优化
keywords: [遗传算法, 粒子群, 模拟退火, 蚁群]
tags: [system/topic-hub, topic/智能优化]
---

# 智能优化 Hub

<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->
## 复习与调用指南

> [!summary] 阅读顺序
> 先用“快速选择”确定算法，再读复习卡掌握思想和步骤，最后跳到实现区选择代码。源码默认折叠；数据明细不在复习页展开。

### 快速选择

| 算法或用途 | 主要解决什么 | 独立实现 | 语言 |
|---|---|---:|---|
| [[#模拟退火SA · 复习|模拟退火SA]] | 通过按温度概率接受劣解跳出局部最优。 | 125 | MATLAB |
| [[#现代优化算法 · 复习|现代优化算法]] | 用随机化、群体化或启发式搜索求复杂问题的近似最优解。 | 6 | MATLAB |
| [[#粒子群PSO · 复习|粒子群PSO]] | 用群体位置和速度协同搜索连续空间。 | 12 | C++, MATLAB |
| [[#蚁群算法ACO · 复习|蚁群算法ACO]] | 用信息素和启发函数构造组合路径。 | 1 | MATLAB |
| [[#遗传算法GA · 复习|遗传算法GA]] | 通过种群进化搜索复杂空间的近似最优解。 | 169 | C++, MATLAB |

### 逐算法复习卡

#### 模拟退火SA · 复习

- **解决什么**：通过按温度概率接受劣解跳出局部最优。
- **核心思想**：Metropolis接受准则与降温计划控制搜索。
- **标准流程**：给初解/温度 → 生成邻域 → 计算能量差 → 概率接受 → 降温 → 多次复验。
- **何时调用**：组合优化或多峰问题且可设计邻域时使用。
- **最易出错**：降温过快会早熟，过慢成本高；结果需多次统计。
- **库内覆盖**：125 个独立实现、286 个原始来源；语言：MATLAB；其中 91 个识别到函数/类型入口。
- **优先阅读**：[[#相似实现组 · MATLAB · 80a0ea30|try_me]]、[[#anneal · MATLAB · 533206d6|anneal]]、[[#try_me · MATLAB · ef73cd00|try_me]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#模拟退火SA · 实现|跳转到源码实现区]]

#### 现代优化算法 · 复习

- **解决什么**：用随机化、群体化或启发式搜索求复杂问题的近似最优解。
- **核心思想**：在探索全局空间和利用当前优良解之间保持平衡。
- **标准流程**：定义编码/邻域 → 设计评价和约束处理 → 初始化 → 迭代搜索 → 多次复验 → 与精确/简单基线比较。
- **何时调用**：非凸、离散、不可导或精确算法成本过高时使用。
- **最易出错**：算法名称不能替代验证；必须报告参数、随机种子、运行次数和最优性差距。
- **库内覆盖**：6 个独立实现、6 个原始来源；语言：MATLAB；其中 3 个识别到函数/类型入口。
- **优先阅读**：[[#ex12_3 · MATLAB · 658631c2|ex12_3]]、[[#huaxue · MATLAB · 6ea5c533|huaxue]]、[[#tjianyan · MATLAB · 0b738d4b|tjianyan]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#现代优化算法 · 实现|跳转到源码实现区]]

#### 粒子群PSO · 复习

- **解决什么**：用群体位置和速度协同搜索连续空间。
- **核心思想**：个体最优与群体最优共同更新速度。
- **标准流程**：初始化粒子 → 评估 → 更新个体/全局最优 → 更新速度位置 → 边界处理 → 收敛。
- **何时调用**：连续黑箱优化、实现需要简洁时使用。
- **最易出错**：易早熟；惯性权重、速度上限和边界处理要记录。
- **库内覆盖**：12 个独立实现、16 个原始来源；语言：C++, MATLAB；其中 8 个识别到函数/类型入口。
- **优先阅读**：[[#pso · MATLAB · 75e93b49|pso]]、[[#get_psoOptions · MATLAB · c7c32f1e|get_psoOptions]]、[[#pso2 · C++ · 8a112b75|pso2]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#粒子群PSO · 实现|跳转到源码实现区]]

#### 蚁群算法ACO · 复习

- **解决什么**：用信息素和启发函数构造组合路径。
- **核心思想**：多只蚂蚁按概率选边，并蒸发/强化信息素。
- **标准流程**：初始化信息素 → 构造解 → 评价 → 局部/全局更新 → 迭代 → 输出最好路径。
- **何时调用**：路径、排序和图上的组合优化。
- **最易出错**：参数敏感且易停滞；必须处理不可行路径。
- **库内覆盖**：1 个独立实现、1 个原始来源；语言：MATLAB；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#蚁群算法matlab源码 · MATLAB · e3cd9190|蚁群算法matlab源码]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#蚁群算法ACO · 实现|跳转到源码实现区]]

#### 遗传算法GA · 复习

- **解决什么**：通过种群进化搜索复杂空间的近似最优解。
- **核心思想**：编码、适应度、选择、交叉、变异共同维持探索与利用。
- **标准流程**：编码变量 → 适应度/罚函数 → 初始化 → 选择交叉变异 → 精英保留 → 收敛与多次复验。
- **何时调用**：离散、非光滑、多峰且精确算法困难时使用。
- **最易出错**：参数多、随机性强；必须固定种子、多次运行并与基线比较。
- **库内覆盖**：169 个独立实现、208 个原始来源；语言：C++, MATLAB；其中 57 个识别到函数/类型入口。
- **优先阅读**：[[#智能算法之遗传算法代码 · MATLAB · fd246a28|智能算法之遗传算法代码]]、[[#遗传算法程序 matlab · MATLAB · d92f31ce|遗传算法程序 matlab]]、[[#gademo3 · MATLAB · 3e384eb2|gademo3]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#遗传算法GA · 实现|跳转到源码实现区]]

### 通用调用检查表

1. 先确认当前问题是否满足复习卡中的适用条件。
2. 优先选择标有函数/类型入口的实现，脚本型代码先重构参数。
3. 用最小样例跑通，再替换为项目输入；不要一开始就接入完整题目。
4. 检查目标方向、变量单位、边界条件、随机种子和软件版本。
5. 保存运行环境、参数、结果与检验，验证通过后再进入项目正式代码。

<!-- END AUTO-HUB-STUDY-GUIDE -->

> 自动更新：2026-07-27 · 匹配笔记：2

## 相关笔记

- [[04-Research/03-建模算法源码库/代码资料索引]] — 相关度 7
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2021-C题-生产企业原材料订购与运输/2021-C题-本地解答与四篇国奖论文对照复盘]] — 相关度 4

## 邻接主题

- [[Topic Index]]
- [[优化模型 Hub]]
- [[数据处理 Hub]]
- [[模型检验 Hub]]

<!-- BEGIN AUTO-INTEGRATED-CODE -->
## 源码实现库（按需调用）

> [!warning] 使用边界
> 以下源码保留全文与来源，但默认均未运行验证。数据依赖明细已从阅读页省略；调用时按代码理解卡完成参数化、最小样例和结果检验。来源显示为可复制路径，不直接调用 Windows 打开未知扩展名。

- 本 Hub 收录原始源码文件：517
- 精确去重后的独立实现：313
- 合并后的实现组：300

### 实现索引

| 算法或用途 | 独立实现 | 原始源码 |
|---|---:|---:|
| [[#模拟退火SA · 实现|模拟退火SA]] | 125 | 286 |
| [[#现代优化算法 · 实现|现代优化算法]] | 6 | 6 |
| [[#粒子群PSO · 实现|粒子群PSO]] | 12 | 16 |
| [[#蚁群算法ACO · 实现|蚁群算法ACO]] | 1 | 1 |
| [[#遗传算法GA · 实现|遗传算法GA]] | 169 | 208 |

### 模拟退火SA · 实现

通过温度下降和概率接受劣解跳出局部最优。

#### TM · MATLAB · 0eabe22b

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：进行特征分解以获得权重、主成分或稳定性信息；按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`f3df9c3de98481a6f0748ae42564b784ab928c673260328cc6a9580f9aa2d4df`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/TM.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/TM.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/TM.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [M,e,rho,Ebin] = TM(Eh,bins)
% Transition matrix calculation method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [M,e,rho] = TM(Eh) ;
%
%   INPUT:
%   Eh = energy and temperature history
%          i = 1, 1+(steps*walkers), etc.
%          Eh(i,1) = index t of temperature step
%          Eh(i,2) = T corresponding to t
%          Eh(i,3) = equilibrium step #j at T
%          Eh(i,4) = walker #k
%          Eh(i,5) = energy E visited by walker k at step j during T
%          Eh(i,6) = energy E' attempted from E by walker k at step j during T
%
%   OUTPUT:
%   M = Transition Matrix (see book section 12.2.1).
%   e = estimate of relaxation time
%   rho = estimate of equilibrium density of states
%   Ebin = energy bin centroids, min, and max
%           Ebin(1,:) are bin centroids.  Ebin(1,b) is the centroid for rho(b).
%           Ebin(2,:) are bin lower bounds
%           Ebin(3,:) are bin upper bounds
%
M = [] ;
e = 0 ;
rho = [] ;
%
% get the energies of visited (Ej) and neighbor (Ei) states
%
Ej = Eh(:,5)' ;
Ei = Eh(:,6)' ;
%
%  Create a sorted, unique list of all energies, E.
%  k will be the number of unique energies.
%
A = sort(cat(2,Ej,Ei)) ;
L = numel(A) ;
k = 1 ;
E(k) = A(1) ;
for i=2:L
    if A(i) ~= E(k)
        k = k + 1 ;
        E(k) = A(i) ;
    end
end
%
%  Need to have an energy for each bin.
%  Create phony out-of-range energies for any remaining bins.
%
if k < bins
    offset = (max(E) - min(E)) / bins ;
    for i=(k+1):bins
        E(i) = E(i-1) + offset ;
    end
    fullbins = k ;
    k = bins ;
else
    fullbins = bins ;
end
%
%  Create partition locations within E for the bins
%
if k == bins
    for b=1:(bins-1)
        Part(b) = b + 1 ;
    end
else
    m = k / bins ;
    for b=1:(bins-1)
        Part(b) = ceil(b*m) ;
    end
end
Part(bins) = k ;
%
%  Find separation values for each bin
%
for b=1:(bins-1)
    Epart(b) = 0.5*((E(Part(b)-1)) + E(Part(b))) ;
end
Epart(bins) = E(k) ;
%
%  Find # values in each bin and compute sum of values for centroid computation.
%
Esum(1:bins) = 0 ;
Ecount(1:bins) = 0 ;
for i=1:L
    for b=1:bins
        if A(i) <= Epart(b)
            Esum(b) = Esum(b) + A(i) ;
            Ecount(b) = Ecount(b) + 1 ;
            break ;
        end
    end
end
%
%  Compute centroid
%
for b=1:fullbins                                    % real bins
        Ebin(1,b) = Esum(b) / Ecount(b) ;
end
for b=(fullbins+1):bins                             % phony bins
        Ebin(1,b) = 0.5 * (Epart(b-1) + Epart(b)) ;
end
%
%  Compute the min and max for the bins
%
Ebin(2,1) = E(1) ;
Ebin(3,1) = Epart(1) ;
for b=2:bins
    Ebin(2,b) = Epart(b-1) ;
    Ebin(3,b) = Epart(b) ;
end
clear A E Part ;
%
%  Q matrix computation
%
Q(1:bins,1:bins) = 0 ;
L = numel(Ej) ;
for k=1:L
    for b=1:bins
        if Ej(k) <= Epart(b)
            j = b ;
            break ;
        end
    end
    for b=1:bins
        if Ei(k) <= Epart(b)
            i = b ;
            break ;
        end
    end
    Q(i,j) = Q(i,j) + 1 ;
end
%
%  P matrix computation
%
for j=1:bins
    Qjsum(j) = 0 ;
    for i=1:bins
        Qjsum(j) = Qjsum(j) + Q(i,j) ;
    end
end
for i=1:bins
    for j=1:bins
        if Qjsum(j) == 0
            P(i,j) = 0 ;
        else
            P(i,j) = Q(i,j) / Qjsum(j) ;
        end
    end
end
%
%  Infinite temperature density of states estimation
%
[V,D] = eig(P) ;
D = abs(D) ;
maxe = D(1,1) ;
maxel = 1 ;
for b=2:bins
    if D(b,b) > maxe
        maxe = D(b,b) ;
        maxel = b ;
    end
end
principal(1:bins) = V(1:bins,maxel) ;
rho = principal/sum(principal) ;
clear V D ;
%
%  Boltzmannized matrix computation
%
[Ehrows, Ehcols] = size(Eh) ;
T = Eh(Ehrows,2) ;
M(1:bins,1:bins) = 0 ;
for i=1:bins
    for j=1:bins
        if i ~= j
            if Ebin(1,i) <= Ebin(1,j)
                M(i,j) = P(i,j) ;
            else
                M(i,j) = P(i,j)*exp((Ebin(1,j) - Ebin(1,i))/T) ;
            end
        end
    end
end
for i=1:bins
    d = 1 - sum(M(:,i)) ;
    M(i,i) = d ;
end
clear P ;
%
%  Relaxation time estimation
%
[V,D] = eig(M) ;
lambda = sort(abs(diag(D))) ;       % sorted eigenvalue magnitudes
maxlambda = lambda(bins) ;
b = bins - 1 ;
while (b > 0)
    if lambda(b) == maxlambda
        b = b - 1 ;
    else
        break ;
    end
end
if b == 0
    e = Inf ;
elseif lambda(b) == 0
    e = 0 ;
else
    loglambda2 = log(lambda(b)) ;
    if loglambda2 >= 0
        e = Inf ;
    else
        e = -1 / loglambda2 ;
    end
end
````

</details>

#### TfinalNstop · MATLAB · 2233b2ef

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `TfinalNstop`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`72134a4957141587b5d2dedfe00726bb37e85d53944a9aaf362fa21736df3cd8`
- 语言：MATLAB
- 符号：`TfinalNstop`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/TfinalNstop.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/TfinalNstop.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/TfinalNstop.m`

<details>
<summary>展开原始代码</summary>

````matlab
function b = TfinalNstop(W,Ew,t,Tt,Et,Etarget,ert,Kt,Ebsft,f)
% Final temperature determination method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   b = TfinalNstop(W,Ew,t,Tt,Et,Etarget,ert,Kt,Ebsft,f) ;
%
%   INPUTS:
%       W = cell array of current states (size walkers)
%       Ew = energies associated with W
%       t = current temperature step index; i.e., current T = Tt(t).
%       Tt = temperature history of simulation (so far)
%       Et = mean energy history
%       Etarget = target mean energy history
%       ert = relaxation time history
%       Kt = equilibrium step history
%       Ebsft = Ebsf history
%       f = [N, relerr] ;
%   OUTPUT:
%       b = true (equal to 1) when the last N mean energies are equal to within relerr.
%
%       For i = (t+1-N) to t-1:   abs((Et(i) - Et(t))/Et(t)) <= relerr.
%
N = f(1) ;
relerr = f(2) ;
if (t < N) | (N < 1)
    b = 0 ;
elseif N == 1
    b = 1 ;
else
    b = 1 ;
    %
    % handle special cases of zero and infinite denominators
    %
    if abs(Et(t)) == Inf
        for i=(t+1-N):(t-1)
            if Et(i) ~= Et(t)
                b = 0 ;
                break ;
            end
        end
    elseif Et(t) == 0
        for i=(t+1-N):(t-1)
            if abs(Et(i)) > relerr
                b = 0 ;
                break ;
            end
        end
    else
        for i=(t+1-N):(t-1)
            if abs((Et(i) - Et(t))/Et(t)) > relerr
                b = 0 ;
                break ;
            end
        end
    end
end
````

</details>

#### TinitAccept · MATLAB · 2cdb2a29

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径。

- SHA-256：`681ec22a4ccf92ef45b7bb16bf427c063bfb9dc85d542140be0e2db25a412619`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/TinitAccept.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/TinitAccept.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/TinitAccept.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/randomwalk.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/randomwalk.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/randomwalk.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [T0,W,Ew,Wbsf,Ebsf,Ea,Ev,steps] = TinitAccept(r, walkers, newstate, X, cost, moveclass)
% Acceptance ratio temperature initialization method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [T0,W,Ew,Wbsf,Ebsf,Ea,Ev,steps] = TinitAccept(r, walkers, newstate, X, cost, moveclass) ;
%
%   INPUTS:
%       r = [ratio, steps]  where
%               ratio = the fraction of uphill moves that T0 should accept (e.g., 0.5)
%               steps = the number of random steps to determine T0  (e.g., 5)
%       walkers = number of walkers.  Must be positive integer.
%       newstate = (handle to) user-defined method
%           W0 = newstate(X)    where
%               X = user-defined problem domain or other data,
%                       behaviorally static.
%               W0 = an initial user-defined state.
%       X = user-defined problem domain or other data, behaviorally static.
%       cost = (handle to) user-defined objective method (function)
%           Ew = cost(X,W)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%       moveclass = (handle to) user-defined method,
%           W = moveclass(X,W,Ea,T)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%               Ea = average energy at current temperature.
%               T = current temperature (will be infinite in Tinit)
%   OUTPUTS:
%       T0 = initial temperature
%       W = cell array of user-defined state(s) from 'newstate' or 'moveclass'.
%       Ew = current energies corresponding to W (size walkers)
%       Wbsf = array of best-so-far states of size 'walkers'
%       Ebsf = array of best-so-far energies
%       Ea = average energy
%       Ev = energy (cost) history at T
%               i = arbitrary index
%               Ev(i,1) = step #
%               Ev(i,2) = walker #
%               Ev(i,3) = an energy visited during T
%               Ev(i,4) = energy attempted from Ev(i,1:3) during T (will be infinite in Tinit)
%       steps = # of steps taken by each walker during Tinit
%
%   Sets T0 so that fraction r of the states examined in this function
%   would be accepted by metropolis acceptance rule.
%
ratio = r(1) ;
if (ratio < 0) | (1 < ratio)
    error(sprintf('Ratio in TinitAccept must be in range [0,1]  (was: %g)', ratio)) ;
end
steps = r(2) ;
if steps <= 0
    error(sprintf('Steps in TinitAccept must be > 0 (was: %g)', steps)) ;
end
%
% take a random walk
%
[W,Ew,Wbsf,Ebsf,Ea,Ev] = randomwalk(steps, walkers, newstate, X, cost, moveclass) ;
%
% compute array dE containing the energy differences between neighbor states in the walk
%
L = steps*walkers ;
k = 0 ;
for i = 1:L
    d = abs(Ev(i,3) - Ev(i,4)) ;
    if d ~= 0
        k = k + 1 ;
        dE(k) = d ;
    end
end
if k == 0
    error('No difference in energies of states.  TinitAccept cannot continue.') ;
end
%
% Will use bisection search to find value that satisfies acceptance ratio.
% The objective function is  sum(exp(-dE/T)) + b.
%
b = ratio*k ;
%
% Find lower bound for bisection search.
%
Tmin = 1 ;
S = exp(-dE/Tmin) ;
fmin = sum(S) - b ;
while fmin > 0
    Tmin = 0.5 * Tmin ;
    if Tmin == 0
        fmin = -b ;
    else
        S = exp(-dE/Tmin) ;
        fmin = sum(S) - b ;
    end
end
%
% Find upper bound for bisection search.
%
Tmax = Tmin ;
if Tmax == 0
    fmax = -b ;
else
    S = exp(-dE/Tmax) ;
    fmax = sum(S) - b ;
end
while fmax < 0
    Tmax = (2 * Tmax) + 1 ;
    S = exp(-dE/Tmax) ;
    fmax = sum(S) - b ;
end
%
% Perform bisection search with error tolerance of 10^-6.
%
T0 = 0.5 * (Tmin + Tmax) ;
relerr = abs((Tmax-Tmin)/Tmax) ; 
errtol = 0.000001 ;
while relerr > errtol
    S = exp(-dE/T0) ;
    fmid = sum(S) - b ;
    if (fmid < 0)
        Tmin = T0 ;
        fmin = fmid ;
    else
        Tmax = T0 ;
        fmax = fmid ;
    end
    relerr = abs((Tmax-Tmin)/Tmax) ; 
    T0 = 0.5 * (Tmin + Tmax) ;
end
%
````

</details>

#### TinitT0 · MATLAB · f312d025

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径。

- SHA-256：`04082f2467b1d1664f8454efc516d8465c81ffd963c110aaa3fcbc07c73b19e2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/TinitT0.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/TinitT0.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/TinitT0.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/ensembleInit.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/ensembleInit.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/ensembleInit.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [T0,W,Ew,Wbsf,Ebsf,Ea,Ev,steps] = TinitT0(r, walkers, newstate, X, cost, moveclass)
% Fixed temperature initialization method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [T0,W,Ew,Wbsf,Ebsf,Ev,steps] = TinitT0(r, walkers, newstate, X, cost, moveclass) ;
%
%   INPUTS:
%       r = initial temperature T0
%       walkers = number of walkers.  Must be positive integer.
%       newstate = (handle to) user-defined method
%           W0 = newstate(X)    where
%               X = user-defined problem domain or other data,
%                       behaviorally static.
%               W0 = an initial user-defined state.
%       X = user-defined problem domain or other data, behaviorally static.
%       cost = (handle to) user-defined objective method (function)
%           Ew = cost(X,W)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%       moveclass = (handle to) user-defined method,
%           W = moveclass(X,W,Ea,T)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%               Ea = average energy at current temperature.
%               T = current temperature (will be infinite in Tinit)
%   OUTPUTS:
%       T0 = initial temperature
%       W = user-defined state(s) from 'newstate' or 'moveclass'.
%       Ew = current energies corresponding to W (size walkers)
%       Wbsf = array of best-so-far states of size 'walkers'
%       Ebsf = array of best-so-far energies
%       Ea = average energy
%       Ev = energy (cost) history at T
%               i = arbitrary index
%               Ev(i,1) = step #
%               Ev(i,2) = walker #
%               Ev(i,3) = an energy visited during T
%               Ev(i,4) = energy attempted from Ev(i,1:3) during T
%       steps = # of steps taken by each walker during Tinit
%
%   Sets T0 to the user supplied value.  Calls ensembleInit(...).
%
[W,Ew,Wbsf,Ebsf,Ea] = ensembleInit(walkers, newstate, X, cost) ;
T0 = r ;
Ev = [] ;
steps = 0 ;
    
````

</details>

#### TinitWhite · MATLAB · 71b3ea68

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径。

- SHA-256：`a4e9ffdf5be99f56931056d4e12d091ae76c455361bb3daabefdc1ee56b344f9`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/TinitWhite.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/TinitWhite.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/TinitWhite.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/randomwalk.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/randomwalk.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/randomwalk.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [T0,W,Ew,Wbsf,Ebsf,Ea,Ev,steps] = TinitWhite(r, walkers, newstate, X, cost, moveclass)
% White temperature initialization method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [T0,W,Ew,Wbsf,Ebsf,Ea,Ev,steps] = TinitWhite(r, walkers, newstate, X, cost, moveclass) ;
%
%   INPUTS:
%       r = [ratio, steps]  where
%               ratio = scale of stddev(E|infinity) to set initial temperature (e.g., 2.0)
%               steps = the number of random steps to determine T0  (e.g., 5)
%       walkers = number of walkers.  Must be positive integer.
%       newstate = (handle to) user-defined method
%           W0 = newstate(X)    where
%               X = user-defined problem domain or other data,
%                       behaviorally static.
%               W0 = an initial user-defined state.
%       X = user-defined problem domain or other data, behaviorally static.
%       cost = (handle to) user-defined objective method (function)
%           Ew = cost(X,W)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%       moveclass = (handle to) user-defined method,
%           W = moveclass(X,W,Ea,T)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%               Ea = average energy at current temperature.
%               T = current temperature (will be infinite in Tinit)
%   OUTPUTS:
%       T0 = initial temperature
%       W = cell array of user-defined state(s) from 'newstate' or 'moveclass'.
%       Ew = current energies corresponding to W (size walkers)
%       Wbsf = array of best-so-far states of size 'walkers'
%       Ebsf = array of best-so-far energies
%       Ea = average energy
%       Ev = energy (cost) history at T
%               i = arbitrary index
%               Ev(i,1) = step #
%               Ev(i,2) = walker #
%               Ev(i,3) = an energy visited during T
%               Ev(i,4) = energy attempted from Ev(i,1:3) during T (will be infinite in Tinit)
%       steps = # of steps taken by each walker during Tinit
%
%   Sets T0 to user supplied ratio of standard deviation of infinite temperature energies.
%   Calls randomwalk(...).
%
ratio = r(1) ;
if ratio <= 0
    error(sprintf('Ratio in TinitWhite must be > 0  (was: %g)', ratio)) ;
end
steps = r(2) ;
if steps <= 0
    error(sprintf('Steps in TinitWhite must be > 0 (was: %g)', steps)) ;
end
N = steps*walkers ;
if N < 2
    error(sprintf('steps*walkers in TinitWhite must be > 1 (was: %g)', N)) ;
end
%
[W,Ew,Wbsf,Ebsf,Ea,Ev] = randomwalk(steps, walkers, newstate, X, cost, moveclass) ;
%
if walkers == 1
    E(1) = Ew(1) ;
    E(2:(steps+1)) = Ev(:,3) ;
    T0 = ratio * std(E) ;
else
    T0 = ratio * std(Ew) ;
end
````

</details>

#### anneal · MATLAB · 533206d6

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`474c265ee1af87894322fc89f00c0168e4b96552c388755bdf3794e57881cfcc`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/anneal.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/anneal.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/anneal.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/TM.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/TinitT0.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/historyupdate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/hoffmann.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/metropoliswalk.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/TM.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/TinitT0.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/historyupdate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/hoffmann.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/metropoliswalk.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/TM.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/TinitT0.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/historyupdate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/hoffmann.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/metropoliswalk.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = anneal( ...
    verbose, ...
    newstate, X, ...
    cost, moveclass, ...
    walkers, ...
    acceptrule, q, ...
    schedule, P, ...
    equilibrate, C, maxsteps, ...
    Tinit, r, ...
    Tfinal, f, maxtemps, ...
    v, bins, e)
% MAIN DRIVER and HELP file supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
% Get the book:  http://www.frostconcepts.com/books/ebsa/
%
% [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = anneal( ...
%     verbose, ...
%     newstate, X, ...
%     cost, moveclass, ...
%     walkers, ...
%     acceptrule, q, ...
%     schedule, P, ...
%     equilibrate, C, maxsteps, ...
%     Tinit, r, ...
%     Tfinal, f, maxtemps, ...
%     v, bins, e)
%
%   verbose = prints status information when true (1).
%   newstate = (handle to) user-defined method
%           W0 = newstate(X)    where
%               X = user-defined problem domain or other data,
%                       behaviorally static.
%               W0 = an initial user-defined state.
%           Book chapter 2.
%   X = user-defined problem domain or other data, behaviorally static.
%           Book chapter 2.
%   cost = (handle to) user-defined objective method (function)
%           Ew = cost(X,W)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%               Ew = energy corresponding to W
%           Book chapter 9.
%   moveclass = (handle to) user-defined method,
%           W = moveclass(X,W,Ea,T)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%               Ea = average energy at current temperature.
%               T = current temperature
%           Book chapters 2.2 and 10.2.
%   walkers = number of walkers.  Must be positive integer.
%               walkers = 1 implies barebones annealing
%               walkers > 4 suggested for ensemble methods
%           Book chapters 4 and 7.
%   acceptrule = (handle to) SA Tools or user-defined method
%           a = acceptrule(dE,T,q)    where
%               dE = the difference in cost between a trial state and
%                       the current state: dE = Wtrial - W
%               T = the current temperature
%               q = any data required by the acceptrule
%               a = 0 if trial is rejected, otherwise 1.
%           SA Tools supplied methods are:
%               metropolis
%               szu
%               tsallis
%               threshold
%               franz
%           Book chapter 11.    
%   q = any data required by the acceptrule.
%           Book chapter 11.
%   schedule = (handle to) SA Tools or user-defined temperature update
%           nextT = schedule(Ea,Estd,walkers,dEtgt,v,e,T,t,P)    where
%               Ea = average energy at current temperature.
%               Estd = standard deviation of energies
%               dEtgt = difference between present and previous target mean energy
%               walkers = number of walkers.  Must be positive integer.
%               T = current temperature
%               i = # of current temperature
%                   (i.e., 1st temperature is 1, 2nd is 2, etc.)
%               P = any data required by schedule
%               nextT = next temperature
%           SA Tools supplied methods are:
%               geman
%               geometric
%               hartley
%               berkeley
%               thermospeedHC
%               thermospeedR
%               retrospect
%           Book chapter 13.
%   P = any data required by schedule.
%   equilibrate = (handle to) SA Tools method, or user-defined method,
%           or a non-function_handle type (e.g., 0).  If a function handle is 
%           supplied, then the temperature will not change (i.e., schedule will
%           not be called) until equilibrate returns false (0).  Otherwise, the
%           moveclass will be executed maxsteps times between each
%           temperature change.  Method signature:
%               b = equilibrate(Ea0,Ea,Ew,walkers,T,step,maxsteps,C)    where
%                   Ea0 = average energy at the beginning of the metropolis walk
%                   Ea = current average energy
%                   Ew = current energies corresponding to W (size walkers)
%                   walkers = the number of walkers in the simulation
%                   T = the current temperature
%                   step = the current number of steps taken in the walk
%                   maxsteps = an upper limit on the number of steps in the walk
%                   C = any behaviorally constant data required by the method
%                   b = 0 if the temperature may change, otherwise 1.
%               SA Tools supplied methods are:
%                   hoffmann    (wait-for-a-fluctuation)
%           Book chapter 13.
%   C = any data required by equilibrate.
%   maxsteps = maximum number of times to attempt equilibration (call moveclass at fixed T).
%           Book chapter 13.
%   Tinit = initial temperature (Inf ok) -- or (handle to) SA Tools method,
%           or user-defined method.  If method handle is not present, then the
%           initial temperature will be T0 = Tinit.  Otherwise, the method will
%           calculate T0.  All moves made during this method must be accepted.
%           Method signature:
%               [T0,W,Ew,Ev,steps] = Tinit(r, walkers, newstate, X, cost, moveclass)
%                   INPUTS:
%                       r = behaviorially constant data required by Tinit (if any)
%                       walkers, newstate, X, cost, moveclass: defined above
%                   OUTPUTS:
%                       T0 = initial temperature
%                       steps = # of steps taken by each walker during Tinit
%                       Ev = energy (cost) history at T (infinite for Tinit)
%                           i = arbitrary index
%                           Ev(i,1) = step #
%                           Ev(i,2) = walker #
%                           Ev(i,3) = an energy visited during T
%                           Ev(i,4) = energy attempted from Ev(i,1:3) during T
%                       W,Ew: defined below
%               SA Tools supplied methods are:
%                   TinitT0
%                   TinitAccept
%                   TinitWhite
%           Book section 13.1.
%   r = behaviorially constant data required by Tinit (if any)
%           Book section 13.1.
%   Tfinal = final temperature (-Inf ok) or (handle to) SA Tools method,
%           or user-defined method.  If method handle is not present, then the
%           simulation will end when T drops below the value of Tfinal.
%           Otherwise, the method will calculate a logical value which when
%           true (equal to 1) will stop the simulation.
%           Method signature:
%               b = Tfinal(W,Ew,t,Tt,Et,Etarget,ert,Kt,Ebsft,f)
%                   INPUTS:
%                       W = cell array of current states (size walkers)
%                       Ew = energies associated with W
%                       t = current temperature step index; i.e., current T = Tt(t).
%                       Tt = temperature history of simulation (so far)
%                       Et = mean energy history
%                       Etarget = target mean energy history
%                       ert = relaxation time history
%                       Kt = equilibrium step history
%                       Ebsft = Ebsf history
%                       f = behaviorally constant data required by Tfinal method
%                   OUTPUT:
%                       b = true (equal to 1) when final temperature iteration has been reached
%               SA Tools supplied methods are:
%                   TfinalNstep
%           Book section 13.1.
%   f = behaviorally constant data required by Tfinal method
%           Book section 13.1.
%   maxtemps = maximum number of temperature iterations.
%           Book chapter 13.
%   v = thermodynamic speed.
%               Effects thermospeed schedules.
%               Typically 0 < v < 1.  0 ok for non-thermospeed schedules.
%           Book chapter 13.
%   bins = # of bins to use in estimation of M, e, rho, and Ebin each temperature step.
%               If bins <= 0, then M, e, rho, and Ebin will not be calculated
%                   and the user-supplied constant value of e will be used each step.
%               If bins > 0, then the supplied value of e will be ignored and
%                   the TM method will be called to calculate M, e, rho, and Ebin.
%           Book section 12.2.1.
%   e = estimate of relaxation time.  See bins, above.
%           Book section 12.2.1.
%
%   RETURN VALUES:
%   W = cell array of final state(s) of size 'walkers'
%   Ew = array of final energies corresponding to W
%   Wbsf = array of best-so-far states of size 'walkers'
%   Ebsf = array of best-so-far energies
%   Tt(i) = temperature at temperature step i-1
%       NOTE: matlab does not permit indicies less than 1,
%               so step 0 is at i=1, etc.
%   Et(i) = average energy at Tt(i)
%   Etarget(i) = target mean energy at Tt(i), calculated with v.
%   ert(i) = estimated relaxation time at Tt(i), calculated with bins.
%   Kt(i) = number of equilibration steps taken at Tt(i)
%   Ebsft(i) = best-so-far energy at Tt(i)
%   Eh = energy and temperature history
%          i = 1, 1+(steps*walkers), etc.
%          Eh(i,1) = index t of temperature step
%          Eh(i,2) = T corresponding to t
%          Eh(i,3) = equilibrium step #j at T
%          Eh(i,4) = walker #k
%          Eh(i,5) = energy E visited by walker k at step j during T
%          Eh(i,6) = energy E' attempted from E by walker k at step j during T
%   M = final Transition Matrix (see book section 12.2.1).
%   rho = final estimate of equilibrium density of states
%   Ebin = energy bin centroids, min, and max
%          Ebin(1,:) are bin centroids.  Ebin(1,b) is the centroid for rho(b).
%          Ebin(2,:) are bin lower bounds
%          Ebin(3,:) are bin upper bounds
%
% Example uses of this driver can be found in the examples/ directory.
%
%   e.g.,
%
%   rand('state',sum(100*clock)) ;
%   [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = anneal( ...
%       1, ...
%       12, ...
%       @mystate, mydomain, ...
%       @mycost, @myneighbor, ...
%       @metropolis, [], ...
%       @thermospeed, 0, ...
%       @hoffman, 0.75, 20, ...
%       @TinitWhite, [1.7, 3], ...
%       1, 0, 50, ...
%       0.3, 10, 0) ;
%
error(nargchk(21,21,nargin)) ;
%
% Check for valid input
%
if ~isa(newstate, 'function_handle')
    error('No function handle supplied for newstate') ;
end
classX = class(X) ;
sizeX = size(X) ;
if ~isa(cost, 'function_handle')
    error('No function handle supplied for cost') ;
end
if walkers < 1
    error('Number of walkers must be positive') ;
end
if ~isa(acceptrule, 'function_handle')
    error('No function handle supplied for acceptrule') ;
end
classQ = class(q) ;
sizeQ = size(q) ;
if ~isa(schedule, 'function_handle')
    error('No function handle supplied for schedule') ;
end
classP = class(P) ;
sizeP = size(P) ;
if isa(equilibrate, 'function_handle')
    hasEquilibrate = 1 ;
else
    hasEquilibrate = 0 ;
end
classC = class(C) ;
sizeC = size(C) ;
if maxsteps < 1
    error('maxsteps must be positive') ;
end
if isa(Tinit, 'function_handle')
    hasTinitMethod = 1 ;
else
    if ~isa(Tinit, 'numeric')
      error('No numeric value or function handle supplied for Tinit') ;
    end
    hasTinitMethod = 0 ;
end
if ~isa(r, 'numeric')
    error('No numeric value supplied for r') ;
end
if isa(Tfinal, 'function_handle')
    hasTfinalMethod = 1 ;
else
    if ~isa(Tfinal, 'numeric')
      error('No numeric value or function handle supplied for Tfinal') ;
    end
    hasTfinalMethod = 0 ;
end
if ~isa(f, 'numeric')
    error('No numeric value supplied for f') ;
end
if maxtemps < 1
    error('maxtemps must be positive') ;
end
if ~isa(v, 'numeric')
    error('No numeric value supplied for v') ;
end
if ~isa(bins, 'numeric')
    error('No numeric value supplied for bins') ;
end
if ~isa(e, 'numeric')
    error('No numeric value supplied for e') ;
end
%
%
if verbose
    newline = sprintf('\n') ;
    tab = sprintf('\t') ;
    [vnum, vdate] = satoolsversion ;
    disp(['SA Tools anneal. Version ', vnum, ', Last update ', vdate, '.', newline]) ;
    disp([tab, 'newstate = ', func2str(newstate)]) ;
    disp([tab, 'X is ', classX, ' of size ', num2str(sizeX)]) ;
    disp([tab, 'cost = ', func2str(cost)]) ;
    disp([tab, 'moveclass = ', func2str(moveclass)]) ;
    disp([tab, 'walkers = ', num2str(walkers)]) ;
    disp([tab, 'acceptrule = ', func2str(acceptrule)]) ;
    disp([tab, 'q = ', num2str(q)]) ;
    disp([tab, 'schedule = ', func2str(schedule)]) ;
    disp([tab, 'P = ', num2str(P)]) ;
    if hasEquilibrate
        disp([tab, 'equilibrate = ', func2str(equilibrate)]) ;
    else
        disp([tab, 'equilibrate = (none)']) ;
    end
    disp([tab, 'C = ', num2str(C)]) ;
    disp([tab, 'maxsteps = ', num2str(maxsteps)]) ;
    if hasTinitMethod
        disp([tab, 'Tinit = ', func2str(Tinit)]) ;
    else
        disp([tab, 'Tinit = ', num2str(Tinit)]) ;
    end
    disp([tab, 'r = ', num2str(r)]) ;
    if hasTfinalMethod
        disp([tab, 'Tfinal = ', func2str(Tfinal)]) ;
    else
        disp([tab, 'Tfinal = ', num2str(Tfinal)]) ;
    end
    disp([tab, 'f = ', num2str(f)]) ;
    disp([tab, 'maxtemps = ', num2str(maxtemps)]) ;
    disp([tab, 'v = ', num2str(v)]) ;
    disp([tab, 'bins = ', num2str(bins)]) ;
    disp([tab, 'e = ', num2str(e), newline]) ;
end
%
% Perform temperature initialization (temperature step 0).
%
if hasTinitMethod
    [T,W,Ew,Wbsf,Ebsf,Ea,Ev,steps] = feval(Tinit,r, walkers, newstate, X, cost, moveclass) ;
else
    [T,W,Ew,Wbsf,Ebsf,Ea,Ev,steps] = TinitT0(Tinit, walkers, newstate, X, cost, moveclass) ;
end
%
% Initialize counters, histories, etc.
% Note: Matlab matrix indicies run from 1 to whatever.
%   Consequently, temperature steps 0 to maxsteps are
%   internally indexed from 1 to maxsteps+1.
%
Eh = historyupdate([],Ev,0,Inf) ;
j = 1 ;
Tt(j) = Inf ;
Et(j) = Ea ;
Etarget(j) = Ea ;
ert(j) = 0 ;
Kt(j) = steps ;
Ebsft(j) = min(Ebsf) ;
%
if verbose
    disp(sprintf('%8s %10s %10s %10s %10s %10s %10s %10s %12s','t','T','<E>','Etarget', 'Estd','e','steps','Ebsf')) ;
    disp(sprintf('%8d %10.3g %10.3g %10.3g %10.3g %10.3g %10d %12.5g', ...
        round(j-1),Tt(j), Et(j), Etarget(j), std(Ew), ert(j), round(Kt(j)), Ebsft(j))) ;
end
%
% Iterature through the temperature steps
%
for i=1:maxtemps
    clear Ev ;
    %
    % Go take an equilibrium walk
    %
    [W,Ew,Wbsf,Ebsf,Ea,Estd,Ev,steps] = metropoliswalk( ...
        verbose, ...
        Ea, T, ...
        walkers, W, X, cost, moveclass, ...
        acceptrule, q, ...
        hasEquilibrate, equilibrate, C, maxsteps, ...
        Wbsf, Ebsf) ;
    %
    % Record what happenned
    %
    j = i+1 ;
    Tt(j) = T ;
    Et(j) = Ea ;
    Etarget(j) = Ea - (v*Estd) ;   % update the target on-the-fly
    Kt(j) = steps ;
    Ebsft(j) = min(Ebsf) ;
    Eh = historyupdate(Eh,Ev,i,T) ;  % update the history array
    %
    % Compute the density of states and relaxation time
    %
    if bins <= 0    % unless turned off
        M = [] ;
        rho = [] ;
        Ebin = [] ;
    else
        [M, e, rho, Ebin] = TM(Eh,bins) ;
    end
    ert(j) = e ;    % record the relaxation time
    %
    if verbose
        disp(sprintf('%8d %10.3g %10.3g %10.3g %10.3g %10.3g %10d %12.5g', ...
            round(j-1),Tt(j), Et(j), Etarget(j), Estd, ert(j), round(Kt(j)), Ebsft(j))) ;
    end
    %
    % Perform the temperature update.  Halt if some stopping criteria reached.
    %
    dEtgt = Etarget(j) - Etarget(j-1) ;
    T = feval(schedule,Ea,Estd,walkers,dEtgt,v,e,T,i,P) ;
    if hasTfinalMethod
        if feval(Tfinal,W,Ew,j,Tt,Et,Etarget,ert,Kt,Ebsft,f)
            if verbose
                disp(tab) ;
                disp([tab,'Stop criteria met for "',func2str(Tfinal),'"']) ;
            end
            break ;
        end
    elseif T < Tfinal
        if verbose
            disp(tab) ;
            disp([tab,'Tfinal (',num2str(Tfinal),') surpassed at T = ',num2str(T)]) ;
        end
        break ;
    end
end
if verbose
   disp(tab) ;
end
%
% Return data to caller.
%
````

</details>

#### berkeley · MATLAB · 4367fed6

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `berkeley`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`b38a57b4a3a4b2427406987049be0131b9d7923d0b9bbf865572f2f78f27d8bf`
- 语言：MATLAB
- 符号：`berkeley`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/berkeley.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/berkeley.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/berkeley.m`

<details>
<summary>展开原始代码</summary>

````matlab
function T = berkeley(Ea,Estd,walkers,dEtgt,v,e,T,t,P)
% Berkeley temperature update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   T = berkeley(Ea,Estd,walkers,dEtgt,v,e,T,t,P) ;
%
%   Ea = (not used) average energy.
%   Estd = standard deviation of energies
%   walkers = number of walkers
%   dEtgt = (not used) difference between present and previous target mean energy
%   v = (not used) thermodynamic speed.
%   e = (not used) estimate of relaxation time.
%   T = current temperature.
%   t = (not used) temperature step #.
%   P = positive constant < 1.
%
if (P <= 0) | (1 <= P)
    error(sprintf('berkeley method requires 0 < P < 1  (was: %g)',P)) ;
end
if T > 0
    if Estd > 0
        dT = -P*(T*T)/Estd ;
    else
        dT = T ;  % force algorithm into next if statement
    end
    if T <= abs(dT)
        dT = -P*T ;  % when dT out of range, use recommended geometric approximation
    end
    T = T + dT ;
end
````

</details>

#### dispEh · MATLAB · 0ad7c063

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `dispEh`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`379b7e4ab972043c688c6a06f0dfddeede02918b4db3012962bfddd8375b3c75`
- 语言：MATLAB
- 符号：`dispEh`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/dispEh.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/dispEh.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/dispEh.m`

<details>
<summary>展开原始代码</summary>

````matlab
function dispEh(Eh)
% Eh matrix display method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
% dispEh(Eh)
%
%   Eh = energy and temperature history
%          i = 1, 1+(steps*walkers), etc.
%          Eh(i,1) = index t of temperature step
%          Eh(i,2) = T corresponding to t
%          Eh(i,3) = equilibrium step #j at T
%          Eh(i,4) = walker #k
%          Eh(i,5) = energy E visited by walker k at step j during T
%          Eh(i,6) = energy E' attempted from E by walker k at step j during T
%
    newline = sprintf('\n') ;
    tab = sprintf('\t') ;
    sizeEh = size(Eh) ;
    m = sizeEh(1) ;
    disp(sprintf('%12s %12s %12s %12s %12s %12s','t','T','step','walker','E','E"')) ;
    for i=1:m
        disp(sprintf('%12d %12.5g %12d %12d %12.5g %12.5g', ...
            round(Eh(i,1)),Eh(i,2),round(Eh(i,3)),round(Eh(i,4)),Eh(i,5),Eh(i,6))) ;
    end
    disp([tab]) ;
    
````

</details>

#### dispEt · MATLAB · 04f9b66a

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `dispEt`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`17cc3ea07673c8a066ad296cede271d78ab3bb58d33e8c1285ea2f8709026376`
- 语言：MATLAB
- 符号：`dispEt`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/dispEt.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/dispEt.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/dispEt.m`

<details>
<summary>展开原始代码</summary>

````matlab
function dispEt(Tt,Et,Etarget,ert,Kt,Ebsft)
% Et data display method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
% dispEt(Tt,Et,Etarget,Kt,Ebsft)
%
%   Tt(i) = temperature at temperature step i-1
%   Et(i) = average energy at Tt(i)
%   Etarget(i) = target average energy for Tt(i+1)
%   ert(i) = estimate of relaxation time at Tt(i)
%   Kt(i) = number of equilibration steps taken at Tt(i)
%   Ebsft(i) = best-so-far energy at Tt(i)
%
newline = sprintf('\n') ;
tab = sprintf('\t') ;
sizeTt = size(Tt) ;
m = sizeTt(2) ;
disp(sprintf('%8s %12s %12s %12s %12s %12s %12s %12s','t','T','<E>','Etarget','e','steps','Ebsf')) ;
for i=1:m
    disp(sprintf('%8d %12.5g %12.5g %12.5g %12.5g %12d %12.5g', ...
        round(i-1),Tt(i), Et(i), Etarget(i), ert(i), round(Kt(i)), Ebsft(i))) ;
end
disp([tab]) ;
    
````

</details>

#### dispMat · MATLAB · 5c501c33

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `dispMat`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`a039db731b4ff573ed0eb678a8f42a9f31f1e520df3e4ed819b685d566601d00`
- 语言：MATLAB
- 符号：`dispMat`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/dispMat.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/dispMat.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/dispMat.m`

<details>
<summary>展开原始代码</summary>

````matlab
function dispMat(M,name,form)
% Matrix data display method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
% dispMat(M,name,form)
%
%   M = 2D matrix
%   name = text label to display; e.g., 'M'
%   form = numeric print format; e.g, '%4.2f'.  See help format.
%
tab = sprintf('\t') ;
label = sprintf('%s =',name) ;
if nargin == 2
    form = '%5.2f' ;
end
f = sprintf('  %s',form) ;
disp([tab]) ;
disp([tab,label]) ;
n = size(M,1) ;
for i=1:n
    disp([tab,sprintf(f,M(i,:))]) ;
end
disp([tab]) ;
````

</details>

#### ensembleInit · MATLAB · 72f1d1b1

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`fdbaf14c1f7ced86332972b6c753062009b0022224bcf0cabe9600d938effc94`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/ensembleInit.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/ensembleInit.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/ensembleInit.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [W,Ew,Wbsf,Ebsf,Ea] = ensembleInit(walkers, newstate, X, cost)
% Ensemble initialization method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [W,Ew,Wbsf,Ebsf,Ea] = ensembleInit(walkers, newstate, X, cost) ;
%
%   INPUTS:
%       walkers = number of walkers.  Must be positive integer.
%       newstate = (handle to) user-defined method
%           W0 = newstate(X)    where
%               X = user-defined problem domain or other data,
%                       behaviorally static.
%               W0 = an initial user-defined state.
%       X = user-defined problem domain or other data, behaviorally static.
%       cost = (handle to) user-defined objective method (function)
%           Ew = cost(X,W)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%   OUTPUTS:
%       W = cell array of user-defined state(s) from 'newstate'.
%       Ew = current energies corresponding to W (size walkers)
%       Wbsf = array of best-so-far states of size 'walkers'
%       Ebsf = array of best-so-far energies
%       Ea = average ensemble energy
%
W = cell(walkers,1) ;
for j=1:walkers
    W{j} = feval(newstate,X) ;
    Ew(j) = feval(cost,X,W{j}) ;
    Wbsf{j} = W{j} ;
    Ebsf(j) = Ew(j) ;
end
Ea = mean(Ew) ;
````

</details>

#### cluster_cost · MATLAB · 2026c33a

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `cluster_cost`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`56d83d5077a151cdda0b2586e75f4f802e3f987eb5308f7edf42df654988a5e8`
- 语言：MATLAB
- 符号：`cluster_cost`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/cluster_cost.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/cluster_cost.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/cluster_cost.m`

<details>
<summary>展开原始代码</summary>

````matlab
function c = cluster_cost(X,W)
% c = cluster_cost(X,W)
% Method for chemcluster example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   c = cluster_cost(X,W) ;
%
%   X = [N,a,b,g,rho]
%       N = number of molecules
%       a = Lennard-Jones coefficient
%       b = Lennard-Jones coefficient
%       g = compression factor used in perturb
%       rho = (b/a)^(1/6) two-particle 1d solution
%   W = N 3D points.
%   c = total energy of LJ pair potentials
%
N = X(1) ;
a = X(2) ;
b = X(3) ;
c = 0 ;
for j=2:N
    for i=1:(j-1)
        m = norm(W(j,:) - W(i,:)) ;
        f = (-a/(m^6)) + (b/(m^12)) ;
        c = c + f ;
    end
end
````

</details>

#### cluster_init · MATLAB · 5c6e257b

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `cluster_init`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`34f6d0da4d1812aac04a73f8d3fe800379818376067c2803a72be8e3a18c18c1`
- 语言：MATLAB
- 符号：`cluster_init`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/cluster_init.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/cluster_init.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/cluster_init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function X = cluster_init(N,a,b,g)
% X = cluster_init(N,a,b,g) ;
% Method for chemcluster example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   X = cluster_init ;
%   X = cluster_init(N) ;
%   X = cluster_init(N,a,b) ;
%   X = cluster_init(N,a,b,g) ;
%
%   X = [N,a,b,g,rho]
%   N = number of molecules
%   a = Lennard-Jones coefficient
%   b = Lennard-Jones coefficient
%   g = compression factor used in perturb
%   rho = (b/a)^(1/6) two-particle 1d solution
%
% Sets and stores parameters for Lennard-Jones simulation.
% a and b must be positive scalars.
% g must be a positive scalar, typically < 1.
% Execute without arguments to determine default values.
%
if nargin < 4           % set default values of parameters as needed
    g = .97 ;
    if nargin < 3
        a = 4 ;
        b = 3 ;
        if nargin < 1
            N = 7 ;
        end
    end
end
rho = (b/a)^(1/6) ;     % compute for later use
X = [N,a,b,g,rho] ;
````

</details>

#### cluster_new · MATLAB · ba2ea011

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `cluster_new`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`7c342fbdd39cf61aa2cb5c593e146b298cf3f0f7831e4c6ceb056bc8b83a6c9c`
- 语言：MATLAB
- 符号：`cluster_new`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/cluster_new.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/cluster_new.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/cluster_new.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = cluster_new(X)
% W = cluster_new(X)
% Method for chemcluster example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = cluster_new(X) ;
%
%   X = [N,a,b,g,rho]
%   N = number of molecules
%   a = Lennard-Jones coefficient
%   b = Lennard-Jones coefficient
%   g = compression factor used in perturb
%   rho = (b/a)^(1/6) two-particle 1d solution
%   W = N 3D points.
%
%   Creates an initial configuration of molecules
%       based on values stored in X (see clusterparams).
%   Calls stillinger3Dpoints(...).
%
N = X(1) ;
rho = X(5) ;
rmax = (sqrt(3)/2)*(N^(1/3))*rho ;
for n=1:N
    q = n / N ;
    theta = q*2*pi ;
    phi = (pi/2) + (q*pi) ;
    r = q*rmax ;
    [W(n,1),W(n,2),W(n,3)] = sph2cart(theta,phi,r) ;
end
[W,o] = stillinger3Dpoints(W,N,rho) ;
````

</details>

#### cluster_perturb · MATLAB · ff93e79d

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `cluster_perturb`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`17c754e583452090f1abcf3a7e7c1d69eb72876ed3bafebd5713beaa46ef89fb`
- 语言：MATLAB
- 符号：`cluster_perturb`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/cluster_perturb.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/cluster_perturb.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/cluster_perturb.m`

<details>
<summary>展开原始代码</summary>

````matlab
function Wnew = cluster_perturb(X,W,Ea,T)
% Wnew = cluster_perturb(X,W)
% Method for chemcluster example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   Wnew = cluster_perturb(X,W,Ea,T) ;
%
%   X = [N,a,b,g,rho]
%       N = number of molecules
%       a = Lennard-Jones coefficient
%       b = Lennard-Jones coefficient
%       g = compression factor used in perturb
%       rho = (b/a)^(1/6) two-particle 1d solution
%   W = N 3D points.
%   Wnew = perturbed copy of W
%   Ea = (not used) average energy.
%   T = (not used) current temperature.
%
%   Perturbs a cluster either (random choice) by 
%       compression or expansion.  The latter is
%       acheived by the satools method "stillinger3Dpoints".
%   
N = X(1) ;
g = X(4) ;
rho = X(5) ;
if rand < 0.5       % to compress or expand, that is the question!
    Wnew = g*W ;
else
    Wnew = stillinger3Dpoints(W,N,rho) ;
end
````

</details>

#### clusterdistances · MATLAB · b5b27660

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `clusterdistances`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`48655141626b84aa66c03f41bc79e725ac22a5f56917fe3f06e736166d5a4dd1`
- 语言：MATLAB
- 符号：`clusterdistances`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/clusterdistances.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/clusterdistances.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/clusterdistances.m`

<details>
<summary>展开原始代码</summary>

````matlab
function S = clusterdistances(W,N)
% S = clusterdistances(W,N)
% Method for chemcluster example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   S = clusterdistances(W,N) ;
%
%   W = N 3D points;  W(1:N,1:3)
%   N = number of points
%   S = point-to-point distances
%
k = 1 ;
for j=1:(N-1)
    for i=(j+1):N
        S(k) = norm(W(j,1:3) - W(i,1:3)) ;
        k = k + 1;
        end
    end
end
````

</details>

#### clusterplot · MATLAB · 313db0f1

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `clusterplot`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`eaf6c539e1c1cd96c172f010eb4020771b1fc2f9719323e62dfe4b8eb076e8ad`
- 语言：MATLAB
- 符号：`clusterplot`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/clusterplot.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/clusterplot.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/clusterplot.m`

<details>
<summary>展开原始代码</summary>

````matlab
function h = clusterplot(W)
% h = clusterplot(W)
% Method for chemcluster example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   h = clusterplot(W) ;
%
%   W = N 3D points.
%   N = number of molecules
%
%   Produces a scatter plot of a cluster state.
%
scatter3(W(:,1),W(:,2),W(:,3),'filled') ;
````

</details>

#### test_all · MATLAB · af5ccc11

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `test_all`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`b43891d60e986c7bfad0f4d0af03273d57c27119ec5cccbdf4191e746890aa2c`
- 语言：MATLAB
- 符号：`test_all`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/test_all.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/test_all.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/test_all.m`

<details>
<summary>展开原始代码</summary>

````matlab
function test_all
% tests SA Tools annealing methods for chemcluster.
%
% NOTE: These are tests.  Values should not be taken as recommendations.
%
%
rand('state',61) ;
%
verbose = 1 ;
%
newstate =  @cluster_new ;
X =         cluster_init ;
cost =      @cluster_cost ;
moveclass = @cluster_perturb ;
%
scheds = 7 ;
sched =      [@geman, @geometric, @hartley, @berkeley, @thermospeedHC, @thermospeedR, @retrospect] ;
schedP =     { 50      0.9         0.005     0.1        0               0              [100, 10, 1] } ;
schedT0 =    [ Inf,    1000,       Inf,      100,       100,            100,            1000] ;
schedTf =    [ 0,      500,        -Inf,     0,         1,              2.9,              0] ;
schedV =     [ 0,      0,          0,        0,         0.2,            0.2,            0] ;
tempsteps =  [ 10,     10,         10,       10,        10,             15,             4] ;
%
bins = 10 ;
e = Inf ;
%
equils = 2 ;
equilib =    {0  @hoffmann} ;
equilibC =   [0, 2.5] ;
equilsteps = [5, 10] ;
%
t0methods = 2 ;
t0method = [@TinitWhite, @TinitAccept] ;
t0r =      { [0.5, 10]     [0.5, 10]} ;
%
tfmethods = 1 ;
tfmethod = [@TfinalNstop] ;
tff =      {[4, 1e-3]} ;
%
amethods = 5 ;
acceptmethod = [@metropolis, @szu, @tsallis, @threshold, @franz] ;
q =            [0,           0,    4,        0,          4] ;
%
walkertests = 2 ;
walkertest = [1, 5] ;
%
disp(['--------------------------------start--------------------------------']) ;
disp(['NOTE: These are tests.  Values should not be taken as recommendations.']) ;
%
for s=1:scheds
% for s=4:4
%
    for eq=1:equils
    % for eq=1:1
%
        for m=0:t0methods
        % for m=0:0
            if m == 0
                T0initmethod = schedT0(s) ;
                T0initconst = 0 ;
            else
                T0initmethod = t0method(m) ;
                T0initconst = t0r{m} ;
            end
%
            for am = 1:amethods
            % for am = 2:2
%
                for walkerc = 1:walkertests
                % for walkerc = 2:2
%
                    for z=0:tfmethods
                    % for z=1:1
                        if z == 0
                            Tfinalmethod = schedTf(s) ;
                            Tfinalconst = 0 ;
                        else
                            Tfinalmethod = tfmethod(z) ;
                            Tfinalconst = tff{z} ;
                        end
%
                        [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = ...
                            anneal(verbose, ...
                                newstate, X, ...
                                cost, moveclass, ...
                                walkertest(walkerc), ...
                                acceptmethod(am),q(am), ...
                                sched(s), schedP{s}, ...
                                equilib{eq}, equilibC(eq), equilsteps(eq), ...
                                T0initmethod, T0initconst, ...
                                Tfinalmethod, Tfinalconst, tempsteps(s), ...
                                schedV(s), bins, e) ;
%
%                       dispEh(Eh) ;
%                       dispEt(Tt,Et,Etarget,ert,Kt,Ebsft) ;
                        dispMat(rho,'rho','%6.2f') ;
                        dispMat(Ebin,'Ebin','%6.2f') ;
%                       plotBins(Ebin,rho,'E','rho','equilibrium density of states') ;
%
                    end
%
                end
%
            end
%
%
            clear W Ew Wbsf Ebsf Tt Et Etarget ert Kt Ebsft Eh M rho Ebin ;
%
        end
    end
end
%
disp(['---------------------------------end---------------------------------']) ;
````

</details>

#### try_me · MATLAB · a37bbd6b

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `try_me`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`939c9fc1a2c5a9b40e91bdf9e9f96b8a060beca5f0d43525406f50b2e7ad881e`
- 语言：MATLAB
- 符号：`try_me`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/try_me.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/try_me.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/try_me.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/cluster_init.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/chemcluster/clusterplot.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/cluster_init.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/chemcluster/clusterplot.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/cluster_init.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/chemcluster/clusterplot.m`

<details>
<summary>展开原始代码</summary>

````matlab
function try_me
% Example SA Tools annealing for chemcluster.
%
% NOTE: These are tests.  Values should not be taken as recommendations.
%
%
rand('state',sum(100*clock)) ;
%
verbose = 1 ;
%
newstate =  @cluster_new ;
X =         cluster_init(13) ;
cost =      @cluster_cost ;
moveclass = @cluster_perturb ;
%
walkers =       16 ;
acceptrule =    @metropolis ;
q =             0 ;
% schedule =      @thermospeedHC ;
schedule =      @thermospeedR ;
P =             0 ;
equilibrate =   @hoffmann ;
C =             1.75 ;
maxsteps =      32 ;
Tinit =         @TinitAccept ;
r =             [0.75, 32] ;
Tfinal =        @TfinalNstop ;
f =             [4, 1e-3] ;
maxtemps =      10 ;
v =             0.2 ;
bins =          10 ;
e =             Inf ;
%
disp(['--------------------------------start--------------------------------']) ;
disp(['NOTE: These are tests.  Values should not be taken as recommendations.']) ;
%
%
    [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = ...
        anneal(verbose, ...
            newstate, X, ...
            cost, moveclass, ...
            walkers, ...
            acceptrule,q, ...
            schedule, P, ...
            equilibrate, C, maxsteps, ...
            Tinit, r, ...
            Tfinal, f, maxtemps, ...
            v, bins, e) ;
%
    dispMat(rho,'rho','%6.2f') ;
    dispMat(Ebin,'Ebin','%6.2f') ;
    dispMat(Ebsf,'Ebsf') ;
    % [Y,I] = min(Ebsf) ;
    % Wmin = W{I} ;
    % clusterplot(Wmin) ;
%   plotBins(Ebin,rho,'E','rho','equilibrium density of states') ;
%   dispEh(Eh) ;
%
disp(['---------------------------------end---------------------------------']) ;
````

</details>

#### bipart_cost · MATLAB · 8348c48e

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `bipart_cost`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`f79da2aa487a0ea5a992015128221d8fc28849b662b426680b2eedd01c7b6bdf`
- 语言：MATLAB
- 符号：`bipart_cost`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/graphbipart/bipart_cost.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/graphbipart/bipart_cost.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/graphbipart/bipart_cost.m`

<details>
<summary>展开原始代码</summary>

````matlab
function E = bipart_cost(X,W)
% E = bipart_cost(X,W)
% Method for graphbipart example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   E = bipart_cost(X,W) ;
%
%   X = {N, A}
%       N = # of vertices.
%       A = Adjacency matrix.
%   W = vector of +1, -1 partition of length N
%   E = energy corresponding to W
%
N = X{1} ;
A = X{2} ;
%
% count number of edges between partitions
%
B = 0 ;
for i=1:(N-1)
    for j=i+1:N
        B = B + ( A(i,j) * (1 - W(i)*W(j)) ) ;
    end
end
B = 0.5*B ;
%
% Compute the "balance" of the 2 partitions and make it a penalty
% 
S = 0 ;
for i=1:N
    S = S + W(i) ;
end
S = abs(S) ;
%
%
E = B + S ;
````

</details>

#### bipart_init · MATLAB · f975a41a

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `bipart_init`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`4f0fc127f51d2b55fc0f967ad91d50e612ec0f1b284b1d09b6c9c550a0ea761a`
- 语言：MATLAB
- 符号：`bipart_init`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/graphbipart/bipart_init.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/graphbipart/bipart_init.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/graphbipart/bipart_init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function X = bipart_init(N)
% X = bipart_init(N)
% Method for graphbipart example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   X = bipart_init(N) ;
%
%   N = # of vertices.  must be positive integer.
%   X = {N, A}
%       N = # of vertices.
%       A = Adjacency matrix
%
N = floor(N) ;
if N < 1
    error(sprintf('N must be positive.  was: %g', N)) ; 
end
%
%   A graph will be created as follows:
%       1. produce a simple cycle of N verticies
%       2. create additional edges between verticies on the cycle
%       3. the same graph will be created every time for each N.
%
%   Create the cycle:
%
C = 1:N ;
S = rand('state') ;           % save the current state of the random number generator
rand('state',17) ;            % use this fixed state instead
for k=1:N
    i = 1 + floor(rand*N) ;
    j = 1 + floor(rand*N) ;
    tmp = C(i) ;
    C(i) = C(j) ;
    C(j) = tmp ;
end
rand('state',S) ;             % return to previous random number sequence
C(N+1) = C(1) ;
%
%    Record the cycle in an adjacency matrix (math, not CS variety).
%
A(1:N,1:N) = 0 ;
for k=1:N
    i = C(k) ;
    j = C(k+1) ;
    A(i,j) = 1 ;
    A(j,i) = 1 ;
end
%
%   Create additional edges and store in adjacency matrix
%
S = rand('state') ;           % save the current state of the random number generator
rand('state',71+N) ;          % use this fixed state instead
for k=1:N
    i = 1 + floor(rand*N) ;
    j = 1 + floor(rand*N) ;
    if i ~= j
        from = C(i) ;
        to = C(j) ;
        A(from,to) = 1 ;
        A(to,from) = 1 ;
    end
end
rand('state',S) ;             % return to previous random number sequence
%
X = {N A} ;
````

</details>

#### bipart_new · MATLAB · 878ff0a6

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `bipart_new`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`33cd492688279a7d5694a82817bc495ae057b8140604fca086b8c0de7194d6d5`
- 语言：MATLAB
- 符号：`bipart_new`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/graphbipart/bipart_new.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/graphbipart/bipart_new.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/graphbipart/bipart_new.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = bipart_new(X)
% W = W = bipart_new(X)
% Method for graphbipart example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = bipart_new(X) ;
%
%   X = {N, A}
%       N = # of vertices.
%       A = Adjacency matrix.
%   W = new vector of random +1, -1 partition of length N
%
for i=1:X{1}
    if rand < 0.5
        W(i) = -1 ;
    else
        W(i) = +1 ;
    end
end
````

</details>

#### bipart_perturb · MATLAB · 3a95e8cb

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `bipart_perturb`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`712461c50fa65168888df0d30409ac6311950ad21e3a2200cb89e8ea882796b2`
- 语言：MATLAB
- 符号：`bipart_perturb`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/graphbipart/bipart_perturb.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/graphbipart/bipart_perturb.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/graphbipart/bipart_perturb.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = bipart_perturb(X,W,Ea,T)
% W = bipart_perturb(X,W,Ea,T)
% Method for graphbipart example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = bipart_perturb(X,W,Ea,T) ;
%
%   X = {N, A}
%       N = # of vertices.
%       A = Adjacency matrix.
%   W = vector of +1, -1 partition of length N
%   Ea = (not used) average energy at current temperature.
%   T = (not used) current temperature
%
%   Flips the sign of a random element of W.
%
n = X{1} ;
i = 1 + floor(n*rand) ;
W(i) = -W(i) ;
````

</details>

#### try_me · MATLAB · ef73cd00

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `try_me`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`f51ad964135f69284c760f2d5606ef084f3e1c2ec5cbaeca77fb0168d26886da`
- 语言：MATLAB
- 符号：`try_me`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/graphbipart/try_me.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/graphbipart/try_me.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/graphbipart/try_me.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/graphbipart/bipart_init.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/graphbipart/bipart_init.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/graphbipart/bipart_init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function try_me
% Example SA Tools annealing for graphbipart.
%
% NOTE: These are tests.  Values should not be taken as recommendations.
%
%
rand('state',721508) ;
%
verbose = 1 ;
%
newstate =  @bipart_new ;
X =          bipart_init(24) ;
cost =      @bipart_cost ;
moveclass = @bipart_perturb ;
%
walkers =       16 ;
acceptrule =    @metropolis ;
q =             0 ;
schedule =      @thermospeedHC ;
% schedule =      @thermospeedR ;
P =             0 ;
equilibrate =   @hoffmann ;
C =             0.75 ;
maxsteps =      48 ;
Tinit =         @TinitAccept ;
r =             [0.9, 48] ;
Tfinal =        @TfinalNstop ;
f =             [4, 1e-3] ;
maxtemps =      12 ;
v =             0.2 ;
bins =          10 ;
e =             Inf ;
%
disp(['--------------------------------start--------------------------------']) ;
disp(['NOTE: These are tests.  Values should not be taken as recommendations.']) ;
%
%
    [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = ...
        anneal(verbose, ...
            newstate, X, ...
            cost, moveclass, ...
            walkers, ...
            acceptrule,q, ...
            schedule, P, ...
            equilibrate, C, maxsteps, ...
            Tinit, r, ...
            Tfinal, f, maxtemps, ...
            v, bins, e) ;
%
    dispMat(rho,'rho','%6.2f') ;
    dispMat(Ebin,'Ebin','%6.2f') ;
%   plotBins(Ebin,rho,'E','rho','equilibrium density of states') ;
%   dispEh(Eh) ;
%
disp(['---------------------------------end---------------------------------']) ;
````

</details>

#### sequence_cost · MATLAB · 810be0c1

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `sequence_cost`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`6460e0eb403ec86b6052f250a7722ae9b87d652bae5c1dea2db19dc7ccf319fe`
- 语言：MATLAB
- 符号：`sequence_cost`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/proteinfold/sequence_cost.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/proteinfold/sequence_cost.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/proteinfold/sequence_cost.m`

<details>
<summary>展开原始代码</summary>

````matlab
function Ew = sequence_cost(X,W)
% Ew = sequence_cost(X,W)
% Method for proteinfold example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   Ew = sequence_cost(X,W) ;
%
%   X = {N, S SN E}
%       N = length of sequence.
%       S = vector of letters representing sequence.
%       SN = vector of indicies representing sequence, isomorphic to S.
%       E = interaction energies.  E(SN(i),SN(j)) is the interaction energy of i, j.
%
%   W = {edge position} : a valid lattice sequence.
%       edge = N-1 edge directions; e.g., edge(i) = [1, 0, 0]
%       position = N sequence element 3D lattice positions; e.g., position(1) = [0, 0, 0]
%
%   Ew = energy corresponding to W
%
N = X{1} ;
SN = X{3} ;
E = X{4} ;
P = W{2} ;
%
% augment the position matrix to contain position numbers
for i=1:N
    P(i,4) = i ;
end
%
% find all interacting lattice neighbors and store in LE
%
k = 0 ;
P = sortrows(P, [1 2]) ;
for i=1:(N-1)
    if (P(i,1) == P(i+1,1)) & (P(i,2) == P(i+1,2))
        if (abs(P(i,3) - P(i+1,3)) == 1) & (abs(P(i,4) - P(i+1,4)) ~= 1)
            k = k + 1 ;
            LE(k,1) = P(i,4) ;
            LE(k,2) = P(i+1,4) ;
        end
    end
end
P = sortrows(P, [1 3]) ;
for i=1:(N-1)
    if (P(i,1) == P(i+1,1)) & (P(i,3) == P(i+1,3))
        if (abs(P(i,2) - P(i+1,2)) == 1) & (abs(P(i,4) - P(i+1,4)) ~= 1)
            k = k + 1 ;
            LE(k,1) = P(i,4) ;
            LE(k,2) = P(i+1,4) ;
        end
    end
end
P = sortrows(P, [2 3]) ;
for i=1:(N-1)
    if (P(i,2) == P(i+1,2)) & (P(i,3) == P(i+1,3))
        if (abs(P(i,1) - P(i+1,1)) == 1) & (abs(P(i,4) - P(i+1,4)) ~= 1)
            k = k + 1 ;
            LE(k,1) = P(i,4) ;
            LE(k,2) = P(i+1,4) ;
        end
    end
end
%
%  add up the interaction energies
%
Ew = 0 ;
for i=1:k
    Ew = Ew + E( SN(LE(i,1)) , SN(LE(i,2)) ) ;
end
````

</details>

#### sequence_init · MATLAB · 1bb10756

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `sequence_init`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`a213e70d295f8b3877c0b39fa45ecce7745b45f00814f3fcb7475b7082b83efd`
- 语言：MATLAB
- 符号：`sequence_init`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/proteinfold/sequence_init.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/proteinfold/sequence_init.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/proteinfold/sequence_init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function X = sequence_init(N)
% X = sequence_init(N)
% Method for proteinfold example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   X = sequence_init(N) ;
%
%   N = length of sequence.  must be integer >= 7.
%   X = {N, S SN E}
%       N = length of sequence.
%       S = vector of letters representing sequence.
%       SN = vector of indicies representing sequence, isomorphic to S.
%       E = interaction energies.  E(SN(i),SN(j)) is the interaction energy of i, j.
%
%   Initializes a 2-letter sequence S of length N.
%   Produces an integer representation SN of S.
%       A in S  is  1 in SN
%       B in S  is  2 in SN
%   Produces matrix E of interaction energies.
%
%   For each N, the same S, SN, and E are produced.
%
Nin = N ;
N = floor(Nin) ;
if N < 7
    error(sprintf('N must be >= 7.  was: %g', Nin)) ; 
end
%
%  Initialize the core sequence of 7.  Identical to example in book.
%
S =  [ 'B', 'A', 'A', 'B', 'B', 'A', 'B' ] ;
SN = [   2,   1,   1,   2,   2,   1,   2 ] ;
%
%  If requested N was larger, add more to sequence
%
savestate = rand('state') ;     % save the current state of the random number generator
rand('state',2112212) ;         % use this state instead
for i=8:N
    if rand < 0.5
        S(i) = 'A' ;
        SN(i) = 1 ;
    else
        S(i) = 'B' ;
        SN(i) = 2 ;
    end
end
rand('state',savestate) ;       % return to previous random number state
%
%  Set the interaction matrix.  Same as in book.
%
E(1,1) = 1 ;
E(1,2) = -2 ;
E(2,1) = E(1,2) ;
E(2,2) = 2 ;
%
X = {N S SN E} ;
````

</details>

#### sequence_new · MATLAB · 03eb66f4

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `sequence_new`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`33eb4563fc3b99048c98992bf76bc58bbd5718eed194565d6c0bae13a0f4a8b3`
- 语言：MATLAB
- 符号：`sequence_new`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/proteinfold/sequence_new.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/proteinfold/sequence_new.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/proteinfold/sequence_new.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = sequence_new(X)
% W = sequence_new(X)
% Method for proteinfold example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = sequence_new(X) ;
%
%   X = {N, S SN E}
%       N = length of sequence.
%       S = vector of letters representing sequence.
%       SN = vector of indicies representing sequence, isomorphic to S.
%       E = interaction energies.  E(SN(i),SN(j)) is the interaction energy of i, j.
%
%   W = {edge position} : an unfolded lattice sequence based on X.
%       edge = N-1 edge directions; e.g., edge(i) = [1, 0, 0]
%       position = N sequence element 3D lattice positions; e.g., position(1) = [0, 0, 0]
%
%   Instantiates the sequence of letters stored in X as a 3D lattice sequence.
%   Every realization produced by this routine has identical geometry: a straight line
%       beginning at the origin and continuing out along the x-axis ( [1,0,0] axis ).
%
N = X{1} ;
position(1,:) = [0, 0, 0] ;
for i=1:(N-1)
    edge(i,:) = [1, 0, 0] ;
    position(i+1,:) = position(i,:) + edge(i,:) ;
end
W = {edge position} ;
````

</details>

#### sequence_perturb · MATLAB · 70a630ae

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `sequence_perturb`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`85d8deb311028c19813399b97e8b8fed82f101b898c40d6de9a09af9b9b6add3`
- 语言：MATLAB
- 符号：`sequence_perturb`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/proteinfold/sequence_perturb.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/proteinfold/sequence_perturb.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/proteinfold/sequence_perturb.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = sequence_perturb(X,W,Ea,T)
% W = sequence_perturb(X,W,Ea,T)
% Method for proteinfold example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = sequence_perturb(X,W,Ea,T) ;
%
%   X = {N, S SN E}
%       N = length of sequence.
%       S = vector of letters representing sequence.
%       SN = vector of indicies representing sequence, isomorphic to S.
%       E = interaction energies.  E(SN(i),SN(j)) is the interaction energy of i, j.
%
%   W = {edge position} : a valid lattice sequence.
%       edge = N-1 edge directions; e.g., edge(i) = [1, 0, 0]
%       position = N sequence element 3D lattice positions; e.g., position(1) = [0, 0, 0]
%
%   Ea = (not used) current average energy
%   T = (not used) current temperature
%
%   Picks an edge between two verticies in the lattice sequence and changes its
%       direction, keeping the remaining part of the sequence attached and intact.
%       The result is a non-axial rotation of the sequence about the starting
%       vertex of the edge.
%   Checks to make sure the new path is not self-intersecting.
%
N = X{1} ;
G = W{1} ;
P = W{2} ;
%
%   Assume new edge will not be valid
%
notvalid = 1 ;
while notvalid
    q = ceil((N-1)*rand) ;      % pick an edge
    Gq = G(q,:) ;               % save it, in case the new one is not valid
    c = ceil(3*rand) ;          % pick a lattice axis for the new edge
    if rand < 0.5               % pick a lattice direction along the axis
        v = -1 ;
    else
        v = 1 ;
    end
    for i=1:(c-1)               % initialize the new coordinate
        G(q,i) = 0 ;
    end
        G(q,c) = v ;
    for i=(c+1):3
        G(q,i) = 0 ;
    end
    for i=1:(N-1)               % create a list of vertex coordinates
        P(i+1,:) = P(i,:) + G(i,:) ;
    end
    notvalid = 0 ;
    PS = sortrows(P) ;              % sort the list of coordinates
    for i=1:(N-1)                   % look for duplications
        if PS(i,:) == PS(i+1,:)     % if the new edge is invalid, put back the old one.
            notvalid = 1 ;
            G(q,:) = Gq ;
            break ;
        end
    end
end                                 % loop until valid edge is found
%
W = {G P} ;
````

</details>

#### 相似实现组 · MATLAB · 80a0ea30

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：6
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：try_me.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `try_me`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`b9b6148b9dd7e41fc75685ad5e67c97063af29a17596934f351cccca2ff603c8`
- 语言：MATLAB
- 符号：`try_me`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/proteinfold/try_me.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/proteinfold/try_me.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/proteinfold/try_me.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/proteinfold/sequence_init.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/proteinfold/sequence_init.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/proteinfold/sequence_init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function try_me
% Example SA Tools annealing for proteinfold.
%
% NOTE: These are tests.  Values should not be taken as recommendations.
%
%
rand('state',7315118063) ;
%
verbose = 1 ;
%
newstate =  @sequence_new ;
X =          sequence_init(7) ;
cost =      @sequence_cost ;
moveclass = @sequence_perturb ;
%
walkers =       16 ;
acceptrule =    @metropolis ;
q =             0 ;
schedule =      @hartley ;
P =             0.01 ;
equilibrate =   @hoffmann ;
C =             1.25 ;
maxsteps =      8 ;
Tinit =         @TinitT0 ;
r =             10000 ;
Tfinal =        @TfinalNstop ;
f =             [4, 1e-3] ;
maxtemps =      10 ;
v =             0.2 ;
bins =          10 ;
e =             Inf ;
%
disp(['--------------------------------start--------------------------------']) ;
disp(['NOTE: These are tests.  Values should not be taken as recommendations.']) ;
%
%
    [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = ...
        anneal(verbose, ...
            newstate, X, ...
            cost, moveclass, ...
            walkers, ...
            acceptrule,q, ...
            schedule, P, ...
            equilibrate, C, maxsteps, ...
            Tinit, r, ...
            Tfinal, f, maxtemps, ...
            v, bins, e) ;
%
    dispMat(rho,'rho','%6.2f') ;
    dispMat(Ebin,'Ebin','%6.2f') ;
%   plotBins(Ebin,rho,'E','rho','equilibrium density of states') ;
%   dispEh(Eh) ;
%
%    dispMat(Ebsf,'Ebsf','%6.2f') ;
%    Sequence = X{2}
%    [Emin, Eminloc] = min(Ebsf) 
%    W = Wbsf{Eminloc} ;
%    Edges = W{1} 
%    Positions = W{2} 
%
disp(['---------------------------------end---------------------------------']) ;
````

</details>

##### 变体 2：try_me.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `try_me`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`1823d4573a603609f5dc5517a578dfd2cc4d4333d644607d3f25d916238a40e3`
- 语言：MATLAB
- 符号：`try_me`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/try_me.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/try_me.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/try_me.m`

<details>
<summary>展开原始代码</summary>

````matlab
function try_me
% Example SA Tools annealing for seismicdecon.
%
% NOTE: These are tests.  Values should not be taken as recommendations.
%
%
rand('state',1023) ;
%
verbose = 1 ;
%
newstate =  @decon_new ;
[X,TrueModel,noise] = decon_init ;
cost =      @decon_cost ;
moveclass = @decon_perturb ;
%
walkers =       12 ;
acceptrule =    @metropolis ;
q =             0 ;
% schedule =      @thermospeedHC ;
schedule =      @thermospeedR ;
P =             0 ;
equilibrate =   @hoffmann ;
C =             0.75 ;
maxsteps =      16 ;
Tinit =         @TinitAccept ;
r =             [0.99, 12] ;
Tfinal =        @TfinalNstop ;
f =             [4, 1e-3] ;
maxtemps =      10 ;
v =             0.2 ;
bins =          10 ;
e =             Inf ;
%
disp(['--------------------------------start--------------------------------']) ;
disp(['NOTE: These are tests.  Values should not be taken as recommendations.']) ;
%
%
    [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = ...
        anneal(verbose, ...
            newstate, X, ...
            cost, moveclass, ...
            walkers, ...
            acceptrule,q, ...
            schedule, P, ...
            equilibrate, C, maxsteps, ...
            Tinit, r, ...
            Tfinal, f, maxtemps, ...
            v, bins, e) ;
%
    dispMat(rho,'rho','%6.2f') ;
    dispMat(Ebin,'Ebin','%6.2f') ;
%   plotBins(Ebin,rho,'E','rho','equilibrium density of states') ;
%   dispEh(Eh) ;
%
disp(['---------------------------------end---------------------------------']) ;
````

</details>

#### decon_cost · MATLAB · a306d2b9

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `decon_cost`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径。

- SHA-256：`80656b8bce9c38f2f0bb39b8a303a34dadbf4a521d224260447798022615e61e`
- 语言：MATLAB
- 符号：`decon_cost`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/decon_cost.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/decon_cost.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/decon_cost.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/eventparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelsignal.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/eventparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelsignal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/eventparts.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelparts.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelsignal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function c = decon_cost(X,W)
% c = decon_cost(X,W)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   c = decon_cost(X,W) ;
%
%   X = {K L t f g}
%       K = length of alpha, tau vectors
%       L = length of source and detected signals
%       t = time vector
%       f = source signal
%       g = detected signal
%   W = {alpha tau K}
%       alpha = attenuation values
%       tau = translation values
%       K = length of alpha, tau vectors
%   c = goodness of fit between W and X
%
%   Calls modelsignal(...) to compute a signal s from alpha and tau given in W.
%   Computes cost using infinity norm:
%       c = max(abs(g - s))
%
[K,L,t,f,g] = eventparts(X) ;
[alpha,tau,K] = modelparts(W) ;
s = modelsignal(f,L,alpha,tau,K) ;
c = max(abs(g - s)) ;
````

</details>

#### decon_init · MATLAB · a576b130

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`ff28680370275023b2c035c5a4b958283e837bd7b0e9d3d7a19d3f7f4bb55b61`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/decon_init.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/decon_init(1).m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/decon_init.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelsignal.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelsignal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelsignal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [X,M,noise] = decon_init(alpha,tau,noise)
% [X,M,noise] = decon_init(alpha,tau,noise)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [X,M,noise] = decon_init ;
%   [X,M,noise] = decon_init(noise) ;
%   [X,M,noise] = decon_init(alpha,tau) ;
%   [X,M,noise] = decon_init(alpha,tau,noise) ;
%
%   X = {K L t f g}
%       K = length of alpha, tau vectors
%       L = length of source and detected signals
%       t = time vector
%       f = source signal
%       g = detected signal
%   M = {alpha tau K}     (True Model)
%       alpha = attenuation values
%       tau = translation values
%       K = length of alpha, tau vectors
%   noise = scalar noise factor
%
%   Initializes parameters of a toy seismic deconvolution problem.
%   A real problem would read in the signals t, f, and g from source files.
%   Here, the simple model coefficients alpha and tau are supplied (default)
%       or input by the user and used to generate g from an internally supplied f.
%       Consequently, the alpha and tau are the solution to this toy problem.
%
%   If supplied:
%       alpha and tau must be vectors of the same length and contain non-negative values.
%       noise must be a non-negative scalar, typically < 1.
%
%   Execute without arguments to determine default values.
%
if (nargin ~= 1) & (nargin ~= 3)
    noise = 0.1 ;
end
if (nargin ~= 2) & (nargin ~= 3)
    alpha = [  .1,  .4,  .3,  .1, .14, .13, .11, .04, .03, .01 ] ;
    tau =   [ 200, 210, 220, 240, 450, 460, 490, 880, 890, 900 ] ;
end
L = 129 ;
N = (1:L) ;
t = (N-1) / 100.0 ;
for n = N,
    f(n) = 4*exp(-0.5*t(n))*sin(t(n)) ;
end
alphasize = size(alpha) ;
K = alphasize(2) ;
I = 1:K ;
noisemax = noise*mean(f) ;
noisebias = 0.5 * noisemax ;
g = modelsignal(f,L,alpha,tau,K) ;
S = rand('state') ;
rand('state',54845) ;
for n = N,
    g(n) = g(n) + (noisemax*((rand*.2)+.9)*sin(t(n)*t(n)*t(n))) - noisebias ;
end ;
rand('state',S) ;
X = {K L t f g} ;
M = {alpha tau K} ;
````

</details>

#### decon_new(1) · MATLAB · f6935c39

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `decon_new`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`e8eda59754eff350db45bb3b2c2ec6c778610c038626a7876c4d781766e2b60b`
- 语言：MATLAB
- 符号：`decon_new`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/decon_new(1).m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/decon_new.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/decon_new.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = decon_new(X)
% W = decon_new(X)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = decon_new(X) ;
%
%   X = {K L t f g}
%       K = length of alpha, tau vectors
%       L = length of source and detected signals
%       t = time vector
%       f = source signal
%       g = detected signal
%   W = {alpha tau K}
%       alpha = attenuation values
%       tau = translation values
%       K = length of alpha, tau vectors
%
%   Creates a trial solution {alpha tau} for the problem parameters given in X.
%   The same solution is created for each value of K.
%
K = X{1} ;
I = 1:K ;
for i=I,
    alpha(i) = 1/log(i+1) ;
end
alpha = alpha / sum(alpha) ;
tau = (1000/K)*I ;
W = {alpha tau K} ;
````

</details>

#### decon_perturb · MATLAB · b47a3d8e

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `decon_perturb`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径。

- SHA-256：`1b50774c0292dc8315b036c97757093069d683ff558692e24171b784f9ccf0bf`
- 语言：MATLAB
- 符号：`decon_perturb`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/decon_perturb.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/decon_perturb.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/decon_perturb.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelparts.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelparts.m`

<details>
<summary>展开原始代码</summary>

````matlab
function Wnew = decon_perturb(X,W,Ea,T)
% Mnew = decon_perturb(X,W)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   Mnew = decon_perturb(X,W,Ea,T) ;
%
%   X = (not used) problem definition
%   W = {alpha tau K}
%       alpha = attenuation values
%       tau = translation values
%       K = length of alpha, tau vectors
%   Ea = (not used) average energy.
%   T = (not used) current temperature.
%
%   Perturbs a random element of alpha or tau (not both).
%   Checks to make sure perturbation is within reasonable bounds.
%
[alpha,tau,K] = modelparts(W) ;
choice = rand ;
element = ceil(rand*K) ;
amount = rand ;
if choice < .5
    % perturb alpha
    alpha(element) = (0.5 + rand)*alpha(element) ;
    if alpha(element) < 0
        alpha(element) = 0 ;
    elseif alpha(element) > 1
        alpha(element) = 1 ;
    end
else
    % perturb tau
    tau(element) = ceil((0.5 + rand)*tau(element)) ;
    if tau(element) < 0
        tau(element) = 0 ;
    elseif tau(element) > 2000
        tau(element) = 2000 ;
    end
end
Wnew = {alpha tau K} ;
````

</details>

#### eventparts · MATLAB · f6f52900

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`c206fdb95e2fd952dd974697310e3b33f95f65e91e4757c8f0a9d99b9934d0d4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/eventparts.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/eventparts.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/eventparts.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [K,L,t,f,g] = eventparts(X)
% [K,L,t,f,g] = eventparts(X)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [K,L,t,f,g] = eventparts(X) ;
%
%   X = {K L t f g}
%   K = length of alpha, tau vectors
%   L = length of source and detected signals
%   t = time vector
%   f = source signal
%   g = detected signal
%
%   Convenience utility.
%
K = X{1} ;
L = X{2} ;
t = X{3} ;
f = X{4} ;
g = X{5} ;
````

</details>

#### eventplot · MATLAB · aa6fbce2

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `eventplot`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`6ca58614fe6fa406169a76c315773de2663da2c8b52fd2ff33441cb36ba4a008`
- 语言：MATLAB
- 符号：`eventplot`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/eventplot.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/eventplot.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/eventplot.m`

<details>
<summary>展开原始代码</summary>

````matlab
function h = eventplot(X)
% h = eventplot(X)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   h = eventplot(X) ;
%
%   X = {K L t f g}
%       K = length of alpha, tau vectors
%       L = length of source and detected signals
%       t = time vector
%       f = source signal
%       g = detected signal
%   h = handle to plot
%
%   plots time series associated with problem
%
t = X{3} ;
f = X{4} ;
g = X{5} ;
h = plot(t,f,'b') ;
hold on ;
plot(t,g,'r') ;
hold off ;
````

</details>

#### modelparts · MATLAB · c0352eee

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`e9366218cab96e4a591dc07e85fc4073367776382075d1ce1bbed3568287f189`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelparts.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelparts.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelparts.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [alpha,tau,K] = modelparts(W)
% [alpha,tau,K] = modelparts(W)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [alpha,tau,K] = modelparts(W) ;
%
%   W = {alpha tau K}
%       alpha = attenuation values
%       tau = translation values
%       K = length of alpha, tau vectors
%
%   Convenience utility.
%
alpha = W{1} ;
tau = W{2} ;
K = W{3} ;
````

</details>

#### modelplot · MATLAB · 62713a22

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `modelplot`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径。

- SHA-256：`88bee6e636df10f2945b5a17ce0ad972a7a447c156dece8ee010bbe98cbfc191`
- 语言：MATLAB
- 符号：`modelplot`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelplot.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelplot.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelplot.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/eventparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelsignal.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/eventparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelparts.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelsignal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/eventparts.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelparts.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelsignal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function h = modelplot(X,W)
% h = modelplot(X,W)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   h = modelplot(X,W) ;
%
%   X = {K L t f g}
%       K = length of alpha, tau vectors
%       L = length of source and detected signals
%       t = time vector
%       f = source signal
%       g = detected signal
%   W = {alpha tau K}
%       alpha = attenuation values
%       tau = translation values
%       K = length of alpha, tau vectors
%   h = handle to plot
%
%   plots time series associated with trial solution
%
[K,L,t,f,g] = eventparts(X) ;
[alpha,tau,K] = modelparts(W) ;
s = modelsignal(f,L,alpha,tau,K) ;
h = plot(t,s,'k') ;
````

</details>

#### modelsignal · MATLAB · ca76bd3e

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `modelsignal`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`96e908e214f1aafaa9217c108d02475ac166eff400d3acff80ab69d8447f1af2`
- 语言：MATLAB
- 符号：`modelsignal`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/seismicdecon/modelsignal.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/seismicdecon/modelsignal.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/seismicdecon/modelsignal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function s = modelsignal(f,L,alpha,tau,K)
% s = modelsignal(f,L,alpha,tau,K)
% Method for seismicdecon example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   s = modelsignal(f,L,alpha,tau,K) ;
%
%   f = source signal
%   L = length of source signal
%   alpha = attenuation values
%   tau = translation values
%   K = length of alpha, tau vectors
%
%   Computes a signal s from the input model parameters.
%
for n = 1:L,
    s(n) = 0 ;
    for i = 1:K,
        k = n - tau(i) ;
        if k > 0
            s(n) = s(n) + (alpha(i)*f(k)) ;
        end
    end ;
end ;
````

</details>

#### Jcoord · MATLAB · ea9c4687

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Jcoord`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`b85c8f86312f39493e8cce93228c07bfea9c9a19bdcb5499b9f2b75453832183`
- 语言：MATLAB
- 符号：`Jcoord`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/spinglass/Jcoord.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/spinglass/Jcoord.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/spinglass/Jcoord.m`

<details>
<summary>展开原始代码</summary>

````matlab
function j = Jcoord(w,d,h,width,depth,height)
% j = Jcoord(w,d,h)
% Method for spinglass example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   j = Jcoord(w,d,h,width,depth,height) ;
%
%       w,d,h = coordinates in lattice L.  Assumed positive.
%       width,depth,height = size of lattice dimensions.
%       j = index in coupling matrix J
%
%       (1,1,1) = 1
%       (1,1,h) = h
%       (1,2,1) = (2-1)*height + 1
%       (1,d,h) = (d-1)*height + h
%       (2,1,1) = depth*height + 1
%       (2,1,h) = depth*height + h
%       (2,d,h) = depth*height + (d-1)*height + h
%       (w,d,h) = (w-1)*depth*height + (d-1)*height + h
%
j = ((w-1)*depth*height) + ((d-1)*height) + h ;
````

</details>

#### spin_cost · MATLAB · e163cd87

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `spin_cost`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`4cb9a9798cd8f45b7e2b1aa92033fae2f7b9d623cbec975f86578f9b166c4de3`
- 语言：MATLAB
- 符号：`spin_cost`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/spinglass/spin_cost.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/spinglass/spin_cost.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/spinglass/spin_cost.m`

<details>
<summary>展开原始代码</summary>

````matlab
function E = spin_cost(X,W)
% E = spin_cost(X,W)
% Method for spinglass example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   E = spin_cost(X,W) ;
%
%   X = {n, J}
%       n = size of coupling matrix, n = width*depth*height
%       J = restricted range coupling matrix
%   W = vector of +1, -1 spins of length n
%   E = energy corresponding to W
%
%       E  is  sum of  J(i,j)*W(i)*W(j)
%
n = X{1} ;
J = X{2} ;
E = 0 ;
for i=1:(n-1)
    for j=i+1:n
        E = E + (J(i,j)*W(i)*W(j)) ;
    end
end
````

</details>

#### spin_init · MATLAB · da6e7612

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`224e3f1f7a554f20071d156e6e983c69b729b64cac7a74bcb093b7c2ba80ca06`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/spinglass/spin_init.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/spinglass/spin_init.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/spinglass/spin_init.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/spinglass/Jcoord.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/spinglass/Jcoord.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/spinglass/Jcoord.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [X,L] = spin_init(width, depth, height)
% [X,L] = spin_init(width, depth, height)
% Method for spinglass example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [X,L] = spin_init(width, depth, height) ;
%
%   width, height, depth = dimensions of 3D lattice.
%       must be positive integers.
%   X = {n, J}
%       n = size of coupling matrix, n = width*depth*height
%       J = restricted range coupling matrix
%   L = lattice from which coupling coupling matrix is derived
%
%   Generates X and L from lattice size parameters.
%   Any particular triplet of input values will always produce the same lattice.
%       e.g., new_coupling(3,4,5) always produces the same X and L.
%
width = floor(width) ;
depth = floor(depth) ;
height = floor(height) ;
if (width < 1) | (depth < 1) | (height < 1)
    error(sprintf('width, depth, and height must be positive.  was: %g %g %g', width, depth, height)) ; 
end
%
%  Create lattice
%
S = rand('state') ;                     % save the state of the random number generator
rand('state',102302) ;                  % set rand to this state
L(1:width,1:depth,1:height) = 0 ;
n = width*depth*height ;
k = (3*n) / 4 ;                         % lattice "population"
for i=1:k
    w = floor(rand*width) + 1 ;
    d = floor(rand*depth) + 1 ;
    h = floor(rand*height) + 1 ;
    L(w,d,h) = L(w,d,h) + 1 ;
end
%
%   O.K., now create coupling matrix
%
J(1:n,1:n) = 0 ;
for w=1:width
    for d=1:depth
        for h=1:height
            if L(w,d,h) > 0
                j = Jcoord(w,d,h,width,depth,height) ;
                amin = max(1,w-1) ;
                amax = min(width,w+1) ;
                bmin = max(1,d-1) ;
                bmax = min(depth,d+1) ;
                cmin = max(1,h-1) ;
                cmax = min(height,h+1) ;
                for a=amin:amax
                    for b=bmin:bmax
                        for c=cmin:cmax
                            if (a ~= w) | (b ~= d) | (c ~= h)
                                i = Jcoord(a,b,c,width,depth,height) ;
                                J(i,j) = J(i,j) + L(w,d,h) ;
                            end
                        end
                    end
                end
            end
        end
    end
end
%
%   Finally, set magnitudes of J to a random fraction of the number of inputs
%
for i=1:n
    for j=1:n
        J(i,j) = J(i,j)* rand ;
    end
end
%
rand('state',S) ;                  % reset rand to original state
X = {n, J} ;
````

</details>

#### spin_new · MATLAB · 0509d633

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行归一化或标准化以统一变量尺度。
- **调用方式**：优先调用 `spin_new`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`0b6847e96cec90a2826b31923484d01197063576cdf07623e2ae69810ced89de`
- 语言：MATLAB
- 符号：`spin_new`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/spinglass/spin_new.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/spinglass/spin_new.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/spinglass/spin_new.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = spin_new(X)
% W = spin_new(X)
% Method for spinglass example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = spin_new(X) ;
%
%   X = {n, J}
%       n = size of coupling matrix, n = width*depth*height
%       J = normalized restricted range coupling matrix
%   W = new vector of random +1, -1 spins of length n
%
for i=1:X{1}
    if rand < 0.5
        W(i) = -1 ;
    else
        W(i) = +1 ;
    end
end
````

</details>

#### spin_perturb · MATLAB · 80589e3d

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `spin_perturb`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`ec8d2b62ff8165eb01e7872fb6f0181942bbc60a707eef1e720a4a2805f24d5a`
- 语言：MATLAB
- 符号：`spin_perturb`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/spinglass/spin_perturb.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/spinglass/spin_perturb.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/spinglass/spin_perturb.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = spin_perturb(X,W,Ea,T)
% W = spin_perturb(X,W,Ea,T)
% Method for spinglass example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = spin_perturb(X,W,Ea,T) ;
%
%   X = {n, J}
%       n = size of coupling matrix, n = width*depth*height
%       J = restricted range coupling matrix
%   W = vector of +1, -1 spins of length n
%   Ea = (not used) average energy at current temperature.
%   T = (not used) current temperature
%
%   Changes sign of random element of W
%
n = X{1} ;
i = 1 + floor(n*rand) ;
W(i) = -W(i) ;
````

</details>

#### 相似实现组 · MATLAB · 030efe0f

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：6
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：try_me.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `try_me`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`f1d54d5aab390c0d35b78feb7ada6df447775b31f638e4e58c01b9492c58259d`
- 语言：MATLAB
- 符号：`try_me`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/spinglass/try_me.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/spinglass/try_me.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/spinglass/try_me.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/spinglass/spin_init.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/spinglass/spin_init.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/spinglass/spin_init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function try_me
% Example SA Tools annealing for spinglass.
%
% NOTE: These are tests.  Values should not be taken as recommendations.
%
%
rand('state',721508) ;
%
verbose = 1 ;
%
newstate =  @spin_new ;
[X, L] =    spin_init(3,5,4) ;
cost =      @spin_cost ;
moveclass = @spin_perturb ;
%
walkers =       16 ;
acceptrule =    @metropolis ;
q =             0 ;
schedule =      @thermospeedHC ;
% schedule =      @thermospeedR ;
P =             0 ;
equilibrate =   @hoffmann ;
C =             1 ;
maxsteps =      16 ;
Tinit =         @TinitWhite ;
r =             [3, 16] ;
Tfinal =        @TfinalNstop ;
f =             [4, 1e-3] ;
maxtemps =      10 ;
v =             0.2 ;
bins =          10 ;
e =             Inf ;
%
disp(['--------------------------------start--------------------------------']) ;
disp(['NOTE: These are tests.  Values should not be taken as recommendations.']) ;
%
%
    [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = ...
        anneal(verbose, ...
            newstate, X, ...
            cost, moveclass, ...
            walkers, ...
            acceptrule,q, ...
            schedule, P, ...
            equilibrate, C, maxsteps, ...
            Tinit, r, ...
            Tfinal, f, maxtemps, ...
            v, bins, e) ;
%
    dispMat(rho,'rho','%6.2f') ;
    dispMat(Ebin,'Ebin','%6.2f') ;
    dispMat(Ebsf,'Ebsf') ;
    % [Y, I] = min(Ebsf) ;
    % Wmin = W{I} ;
    % dispMat(Wmin,'Wmin') ;
%   plotBins(Ebin,rho,'E','rho','equilibrium density of states') ;
%   dispEh(Eh) ;
%
disp(['---------------------------------end---------------------------------']) ;
````

</details>

##### 变体 2：try_me.m

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `try_me`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`f33553bc4b88d457dc577f19356b59493640db3cf01af2040b98db094fa55da5`
- 语言：MATLAB
- 符号：`try_me`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/tsp/try_me.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/tsp/try_me.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/tsp/try_me.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/tsp/route_init.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/tsp/route_init.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/tsp/route_init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function try_me
% Example SA Tools annealing for tsp.
%
% NOTE: These are tests.  Values should not be taken as recommendations.
%
%
rand('state',721508) ;
%
verbose = 1 ;
%
newstate =  @route_new ;
X =          route_init(12) ;
cost =      @route_cost ;
moveclass = @route_perturb ;
%
walkers =       16 ;
acceptrule =    @metropolis ;
q =             0 ;
schedule =      @thermospeedHC ;
% schedule =      @thermospeedR ;
P =             0 ;
equilibrate =   @hoffmann ;
C =             1 ;
maxsteps =      256 ;
Tinit =         @TinitWhite ;
r =             [2, 16] ;
Tfinal =        @TfinalNstop ;
f =             [4, 1e-3] ;
maxtemps =      20 ;
v =             0.2 ;
bins =          10 ;
e =             Inf ;
%
disp(['--------------------------------start--------------------------------']) ;
disp(['NOTE: These are tests.  Values should not be taken as recommendations.']) ;
%
%
    [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = ...
        anneal(verbose, ...
            newstate, X, ...
            cost, moveclass, ...
            walkers, ...
            acceptrule,q, ...
            schedule, P, ...
            equilibrate, C, maxsteps, ...
            Tinit, r, ...
            Tfinal, f, maxtemps, ...
            v, bins, e) ;
%
    dispMat(rho,'rho','%6.2f') ;
    dispMat(Ebin,'Ebin','%6.2f') ;
    N = X{1} ;
    D = X{2} ;
    for i=1:N
        BSF(:,i) = Wbsf{i} ;
    end
    D
    BSF
    dispMat(Ebsf,'Ebsf','%6.2f') ;
%   plotBins(Ebin,rho,'E','rho','equilibrium density of states') ;
%   dispEh(Eh) ;
%
disp(['---------------------------------end---------------------------------']) ;
````

</details>

#### route_cost · MATLAB · 33874111

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `route_cost`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`b529a2e660924bc9a43908c6d4692c1065c7190110c2b8f0d678068b8381fec8`
- 语言：MATLAB
- 符号：`route_cost`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/tsp/route_cost.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/tsp/route_cost.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/tsp/route_cost.m`

<details>
<summary>展开原始代码</summary>

````matlab
function Ew = route_cost(X,W)
% Ew = route_cost(X,W)
% Method for tsp example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   Ew = route_cost(X,W) ;
%
%   X = {N, D}
%       N = # of cities.
%       D = distance matrix. D(i,j) = distance from city i to j.
%   W = a route, a permutation of the indicies 1:N
%
%   Ew = energy corresponding to W.
%   Computed by summing the distances along the route.
%
N = X{1} ;
D = X{2} ;
Ew = D(W(N),W(1)) ;
for i=1:(N-1)
    Ew = Ew + D(W(i),W(i+1)) ;
end
````

</details>

#### route_init · MATLAB · c3e15cbd

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `route_init`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`71861ccd0163939a5e8e13b69c544db6ea3b33eed664f859632eb859d08b12d0`
- 语言：MATLAB
- 符号：`route_init`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/tsp/route_init.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/tsp/route_init.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/tsp/route_init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function X = route_init(N)
% X = route_init(N)
% Method for tsp example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   X = route_init(N) ;
%
%   N = # of cities.  must be > 3.
%   X = {N, D}
%       N = # of cities.
%       D = distance matrix. D(i,j) = distance from city i to j.
%
%   Generates a distance matrix for N cities in toy TSP problem.
%   In a real problem, the distances are problem-specific and might be read from a file.
%   Values in this matrix are skewed towards the max and min.
%   Each N will always generate the same distance matrix.
%
Nin = N ;
N = floor(Nin) ;
if N < 4
    error(sprintf('N must be > 3.  was: %g', Nin)) ; 
end
%
enatural = exp(1) ;
MaxDistance = 420 ;
S = rand('state') ;
rand('state',731511) ;
for i=1:N
    for j=i:N
        x = (2*pi)*(1 - (2*rand)) ;
        D(i,j) = ceil(MaxDistance*(.5+(.5*tanh(x/enatural)))) ;
        D(j,i) = D(i,j) ;
    end
end
rand('state',S) ;
%
X = {N D} ;
````

</details>

#### route_new · MATLAB · 97413a98

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `route_new`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`adf33023ea2405fa1c0a88dcc0ef39e7288f6ce6b15c70866604e914c902ab4b`
- 语言：MATLAB
- 符号：`route_new`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/tsp/route_new.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/tsp/route_new.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/tsp/route_new.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = route_new(X)
% W = route_new(X)
% Method for tsp example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = route_new(X) ;
%
%   X = {N, D}
%       N = # of cities.
%       D = distance matrix. D(i,j) = distance from city i to j.
%   W = new route, a permutation of the indicies 1:N
%
N = X{1} ;
for i=1:N
    A(i,1) = rand ;
    A(i,2) = i ;
end
B = sortrows(A) ;
W = B(:,2) ;
````

</details>

#### route_perturb · MATLAB · 886aea69

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索；按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `route_perturb`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`b41bfa63285938c7630afaf63fade8d159a4204675dcb666b8047de737fabaef`
- 语言：MATLAB
- 符号：`route_perturb`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/examples/tsp/route_perturb.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/examples/tsp/route_perturb.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/examples/tsp/route_perturb.m`

<details>
<summary>展开原始代码</summary>

````matlab
function W = route_perturb(X,W,Ea,T)
% W = route_perturb(X,W,Ea,T)
% Method for tsp example supplied with SA Tools.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = route_perturb(X,W,Ea,T) ;
%
%   X = {N, D}
%       N = # of cities.
%       D = distance matrix. D(i,j) = distance from city i to j.
%   W = a route, a permutation of the indicies 1:N
%   Ea = (not used) current average energy
%   T = (not used) current temperature
%
%   Chooses two cities along route and then reverses path between those points.
%   Circular boundary conditions are used if the 1st city is "past" the second
%       in the route.
%   N must be greater than 3.
%
N = X{1} ;
if N < 4
    error(sprintf('N must be greater than 3.  was: %g', N)) ;
end
%
%
Wold = W ;
%
a = ceil(N*rand) ;
d = 0 ;
while d < 3
    b = ceil(N*rand) ;
    if a < b
        d = b - a ;
    else
        d = (N - a) + b ;
    end
end
L = d - 1 ;
%
for m=1:L
    i = mod(((a + m) - 1),12) + 1 ;
    k = mod(((b - m) - 1),12) + 1 ;
    W(i) = Wold(k) ;
end
````

</details>

#### franz · MATLAB · 8f049388

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `franz`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`53c4d3ac2277ae04d3a31821036f34e55d705b30ea7b1b7af6535813c13f9e8f`
- 语言：MATLAB
- 符号：`franz`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/franz.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/franz.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/franz.m`

<details>
<summary>展开原始代码</summary>

````matlab
function a = franz(dE,T,q)
% Franz acceptance method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   a = franz(dE,T,q) ;
%
%   dE = the difference in cost between a trial state and
%     the current state: dE = Wtrial - W
%   T = the current temperature
%   q = the "q" parameter of the franz acceptance rule
%   a = 0 if trial is rejected, otherwise 1.
%
a = 0 ;
if dE <= 0                           % accept non-uphill moves
    a = 1 ;
elseif (q == 1) | (q == 2)           % avoid division by 0
    a = 1 ;
else
    if T > 0            % ignore 0 or negative temperatures
        D = ((1 - q)/(2 - q))*(dE/T) ;
        if D <= 1
            if rand < (1 - D)^(1/(1-q))
                a = 1 ;
            end
        end
    end
end
````

</details>

#### geman · MATLAB · af72c288

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `geman`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`fd4a350807c3a736a05e7aec3a34ae59311df39c928cfb830b1a0c8b0834ae27`
- 语言：MATLAB
- 符号：`geman`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/geman.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/geman.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/geman.m`

<details>
<summary>展开原始代码</summary>

````matlab
function T = geman(Ea,Estd,walkers,dEtgt,v,e,T,t,P)
% Geman temperature update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   T = geman(Ea,Estd,walkers,dEtgt,v,e,T,t,P) ;
%
%   Ea = (not used) average energy.
%   Estd = (not used) standard deviation of energies
%   walkers = (not used) number of walkers
%   dEtgt = (not used) difference between present and previous target mean energy
%   v = (not used) thermodynamic speed.
%   e = (not used) estimate of relaxation time.
%   T = (not used) current temperature.
%   t = temperature step #.
%   P = positive constant
%
%   if T > 0
%       T = P / log(t+1) ;
%   end
%
if P <= 0
    error(sprintf('geman method requires 0 < P  (was: %g)',P)) ;
end
if T > 0
    T = P / log(t+1) ;
end
````

</details>

#### geometric · MATLAB · 8ae88632

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `geometric`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`130f6082b3e15570afe303957532c3ee139afbdcb9aaa95d72e3b77692bd38f0`
- 语言：MATLAB
- 符号：`geometric`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/geometric.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/geometric.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/geometric.m`

<details>
<summary>展开原始代码</summary>

````matlab
function T = geometric(Ea,Estd,walkers,dEtgt,v,e,T,t,P)
% Geometric temperature update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   T = geometric(Ea,Estd,walkers,dEtgt,v,e,T,t,P) ;
%
%   Ea = (not used) average energy.
%   Estd = (not used) standard deviation of energies
%   walkers = (not used) number of walkers
%   dEtgt = (not used) difference between present and previous target mean energy
%   v = (not used) thermodynamic speed.
%   e = (not used) estimate of relaxation time.
%   T = current temperature.
%   t = (not used) temperature step #.
%   P = constant: 0 < P <= 1.
%
if (P <= 0) | (1 < P)
    error(sprintf('geometric method requires 0 < P <= 1  (was: %g)',P)) ;
end
if T > 0
    T = T*P ;
end
````

</details>

#### hartley · MATLAB · 795a4682

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `hartley`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`b53dbb13ae3cb465e75cadf8e6a68c79bc0e3348933fb210a9321bfb7a8bbf10`
- 语言：MATLAB
- 符号：`hartley`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/hartley.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/hartley.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/hartley.m`

<details>
<summary>展开原始代码</summary>

````matlab
function T = hartley(Ea,Estd,walkers,dEtgt,v,e,T,t,P)
% Hartley temperature update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   T = hartley(Ea,Estd,walkers,dEtgt,v,e,T,t,P) ;
%
%   Ea = (not used) average energy.
%   Estd = (not used) standard deviation of energies
%   walkers = (not used) number of walkers
%   dEtgt = (not used) difference between present and previous target mean energy
%   v = (not used) thermodynamic speed.
%   e = (not used) estimate of relaxation time.
%   T = current temperature.
%   t = (not used) temperature step #.
%   P = small positive scalar constant 0 < P < 1; e.g., 0.01
%
if (P <= 0) | (1 <= P)
    error(sprintf('hartley method requires 0 < P < 1  (was: %g)',P)) ;
end
if T > 0
    T = 1 / ((1/T) + P) ;
end
````

</details>

#### historyupdate · MATLAB · 71e49daa

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `historyupdate`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`c84dc8bb76375a41614fef8691254b7467d496a958d5d2489f6f4faae778a9b5`
- 语言：MATLAB
- 符号：`historyupdate`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/historyupdate.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/historyupdate.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/historyupdate.m`

<details>
<summary>展开原始代码</summary>

````matlab
function Eh = historyupdate(Eh,Ev,t,T)
% Temperature & Energy history update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%    Eh = historyupdate(Eh,Ev,t,T)
%        INPUT:
%            Eh = previous Eh array
%            Ev = energy (cost) history at T
%                   i = arbitrary index
%                   Ev(i,1) = step #
%                   Ev(i,2) = walker #
%                   Ev(i,3) = an energy visited during T
%                   Ev(i,4) = energy attempted from Ev(i,1:3) during T
%            t = index of current temperature step
%            T = current temperature
%        OUTPUT:
%            Eh = energy and temperature history
%                   i = 1, ..., 1+(steps*walkers), etc.
%                   Eh(i,1) = index t of temperature step
%                   Eh(i,2) = T corresponding to t
%                   Eh(i,3) = equilibrium step #j at T
%                   Eh(i,4) = walker #k
%                   Eh(i,5) = energy E visited by walker k at step j during T
%                   Eh(i,6) = energy E' attempted from E by walker k at step j during T
%
sizeEh = size(Eh) ;
sizeEv = size(Ev) ;
m = sizeEh(1) ;
n = sizeEv(1) ;
clear sizeEh sizeEv ;
for i=1:n
    m = m + 1 ;
    Eh(m,1) = t ;
    Eh(m,2) = T ;
    Eh(m,3:6) = Ev(i,1:4) ;
end
    
````

</details>

#### hoffmann · MATLAB · 8e213fd2

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `hoffmann`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`106d283b01fd4d404b1d3018b0aca6ce344f273bae3b3116bfce4a6c473def4e`
- 语言：MATLAB
- 符号：`hoffmann`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/hoffmann.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/hoffmann.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/hoffmann.m`

<details>
<summary>展开原始代码</summary>

````matlab
function b = hoffmann(Ea0,Ea,Ew,walkers,T,step,maxsteps,C)
% Equilibration method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%    b = hoffmann(Ea0,Ea,Ew,walkers,T,step,maxsteps,C)
%
%   INPUT:
%        Ea0 = average energy at the beginning of the metropolis walk
%        Ea = current average energy
%        Ew = current energies corresponding to W (size walkers)
%        walkers = the number of walkers in the simulation
%        T = the current temperature
%        step = the current number of steps taken in the walk
%        maxsteps = an upper limit on the number of steps in the walk
%        C = problem dependent positive scalar constant
%   OUTPUT:
%        b = 0 if the temperature may change, otherwise 1.
%
%        b will be 0 whenever:
%           1. the number of equalibrium steps has reached or exceeded maxsteps
%           2. the change in average energy DE satisfies
%                   DE  <  C * std(Ew) / sqrt(walkers)
%              In other words, a fraction (C / sqrt(walkers)) of the
%              standard deviation of energies exceeds the change in average energy.
%
if C <= 0
    error(sprintf('hoffmann method requires 0 < C  (was: %g)',C)) ;
end
if step >= maxsteps
    b = 0 ;
else
    DE = abs(Ea - Ea0) ;
    Crit = (C*std(Ew))/sqrt(walkers) ;
    b = (DE < Crit) ;
end
````

</details>

#### metropolis · MATLAB · ec6ca306

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `metropolis`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`0956300792f380b2e8ea834c743377702cd939cf1c93a49ddee3665baedad1dc`
- 语言：MATLAB
- 符号：`metropolis`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/metropolis.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/metropolis.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/metropolis.m`

<details>
<summary>展开原始代码</summary>

````matlab
function a = metropolis(dE,T,q)
% Metropolis acceptance method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   a = metropolis(dE,T,q) ;
%
%   dE = the difference in cost between a trial state and
%     the current state: dE = Wtrial - W
%   T = the current temperature
%   q = (not used) any data required by the acceptrule
%   a = 0 if trial is rejected, otherwise 1.
%
a = 0 ;
if (dE <= 0)
    a = 1 ;
else
    if rand < exp(-dE/T)
        a = 1 ;
    end
end
````

</details>

#### metropoliswalk · MATLAB · 21dffcf3

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径。

- SHA-256：`0188aa4119dc2b58e68affd03c7ebfa1d9d3c500973a77c7e91e2e606a8e775b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/metropoliswalk.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/metropoliswalk.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/metropoliswalk.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/hoffmann.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/nextstate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/hoffmann.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/nextstate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/hoffmann.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/nextstate.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [W,Ew,Wbsf,Ebsf,Ea,Estd,Ev,steps] = metropoliswalk( ...
        verbose, ...
        Ea, T, ...
        walkers, W, X, cost, moveclass, ...
        acceptrule, q, ...
        hasEquilibrate, equilibrate, C, maxsteps, ...
        Wbsf, Ebsf)
% Metropolis search (at constant temperature) algorithm supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [W,Ew,Wbsf,Ebsf,Ea,Estd,Ev,steps] = metropoliswalk( ...
%       verbose, Ea, T, W, X, cost, moveclass, acceptrule, q, maxsteps, Wbsf, Ebsf) ;
%
%   INPUT VALUES:
%   verbose = prints status information when true (1).
%   Ea = average energy.
%   T = current temperature.
%   walkers = number of walkers.  Must be positive integer.
%   W = cell array of user-defined state(s) returned from newstate or moveclass.
%   X = user-defined problem domain or other data, behaviorally static.
%   cost = (handle to) user-defined objective method (function)
%           Ew = cost(X,W)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%   moveclass = (handle to) user-defined method,
%           W = moveclass(X,W,Ea,T)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%               Ea = average energy at current temperature.
%               T = current temperature
%   acceptrule = (handle to) SA Tools or user-defined method
%           a = acceptrule(dE,T,q)    where
%               dE = the difference in cost between a trial state and
%                       the current state: dE = Wtrial - W
%               T = the current temperature
%               q = any data required by the acceptrule
%               a = 0 if trial is rejected, otherwise 1.
%           SA Tools supplied methods are:
%               metropolis
%               szu
%               tsallis
%               threshold
%               franz
%   q = any data required by the acceptrule.
%   hasEquilibrate = true (1) when equilibrate is function handle, otherwise false (0).
%   equilibrate = (handle to) SA Tools method, or user-defined method,
%           or a non-function_handle type (e.g., 0).  If a function handle is 
%           supplied, then the temperature will not change (i.e., schedule will
%           not be called) until equilibrate returns false (0).  Otherwise, the
%           moveclass will be executed maxsteps times between each
%           temperature change.  Method signature:
%               c = equilibrate(Ea0,Ea,Ew,walkers,T,step,maxsteps,C)    where
%                   Ea0 = average energy at the beginning of the metropolis walk
%                   Ea = current average energy
%                   Ew = current energies corresponding to W (size walkers)
%                   walkers = the number of walkers in the simulation
%                   T = the current temperature
%                   step = the current number of steps taken in the walk
%                   maxsteps = an upper limit on the number of steps in the walk
%                   C = any behaviorally constant data required by the method
%                   c = 0 if the temperature may change, otherwise 1.
%               SA Tools supplied methods are:
%                   hoffmann    (wait-for-a-fluctuation)
%           Book chapter 13.
%   C = any data required by equilibrate.
%   maxsteps = number of times to call nextstate.
%   Wbsf = cell array of best-so-far user-defined state(s).
%   Ebsf = array of Wbsf energy(ies).
%
%   OUTPUT VALUES:
%   (several input arguments are also output with updated values).
%   Ew = array of energy(ies) of user-defined state.
%   Ea = average energy during walk.
%   Estd = standard deviation of energies during walk.
%   Ev = energy (cost) history at T
%               i = arbitrary index
%               Ev(i,1) = step #
%               Ev(i,2) = walker #
%               Ev(i,3) = an energy visited during T
%               Ev(i,4) = energy attempted from Ev(i,1:3) during T
%   steps = actual number of steps taken by each walker.
%
Ev(1,1:4) = 0 ;
Ew(1:walkers) = Inf ;
i = 1 ;
k = 1 ;
walking = 1 ;
Ea0 = Ea ;
E = [] ;
%
% take a metropolis walk
%
while walking
    for j=1:walkers
        [W{j},Ew(j),Evisit,Etrial] = nextstate(Ea,T,W{j},X,cost,moveclass,acceptrule,q) ;
        Ev(i,1) = k ;
        Ev(i,2) = j ;
        Ev(i,3) = Evisit ;
        Ev(i,4) = Etrial ;
        if Ew(j) < Ebsf(j)
            Wbsf{j} = W{j} ;
            Ebsf(j) = Ew(j) ;
        end
        i = i + 1 ;
    end
    %
    % update metrics
    %
    E = cat(2,E,Ew) ;
    Ea = mean(E) ;
    Estd = std(E) ;
    %
    % test for equilibration
    %
    if hasEquilibrate
        walking = feval(equilibrate,Ea0,Ea,Ew,walkers,T,k,maxsteps,C) ;
    else
        walking = (k < maxsteps) ;
    end
    k = k + 1 ;
end
steps = k - 1 ;
````

</details>

#### mktemplate · MATLAB · c5df4ba8

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `mktemplate`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`35edb7d6ead0543f789c8c1022d8d6bb2f21f170bc3f6e4460ce2cb0e1afdd05`
- 语言：MATLAB
- 符号：`mktemplate`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/mktemplate.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/mktemplate.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/mktemplate.m`

<details>
<summary>展开原始代码</summary>

````matlab
function mktemplate(problemname)
% Automated file generation supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
% mktemplate(problemname)
%
%   problemname = name of new user directory and problem functions
%
% This function will create a directory, 'problemname' and place in it 5 m-files:
%
%       problemname_init
%       problemname_new
%       problemname_cost
%       problemname_perturb
%       try_me
%
% which comply with the satools method signatures.  The four files
%       problemname_*
% are functional, but only in the sense that X and W are null and
% the cost function returns a random number.  The mktemplate function
% is a convenience tool from which the user can fill in their particular
% problem definition.
%
% After execution, the new directory will be the users current directory.
%
if nargin ~= 1
    help mktemplate ;
    error('problemname is a required argument') ;
end
if length(problemname) < 1
    help mktemplate ;
    error('problemname was empty!') ;
end
%
newline = sprintf('\n') ;
tab = sprintf('\t') ;
%
srcpath = which('mktemplate') ;
srcdir = strrep(srcpath,'\mktemplate.m','') ;  % PC
sep = '\' ;
if strcmp(srcpath,srcdir)
    srcdir = strrep(srcpath, '/mktemplate.m','') ;  % Unix
    sep = '/' ;
    if strcmp(srcpath,srcdir)
        srcdir = strrep(srcpath, ':mktemplate.m','') ;  % Mac
        sep = ':' ;
        if strcmp(srcpath,srcdir)
            error(sprintf('Cannot decipher directory separator in path %s',srcpath)) ;
        end
    end
end
%
thisdir = pwd ;
if strcmp(thisdir,srcdir)
    disp([newline,tab,'Warning: creating in SA Tools source directory.']) ;
    disp([tab,'Directory might be lost in future software upgrade.',newline]) ;
end
%
[status, msg] = mkdir(problemname) ;
if status ~= 1
    error(msg) ;
end
cd(problemname) ;
%
srcnames = strcat(...
        {srcdir, srcdir, srcdir, srcdir, srcdir}, ...
        {sep,    sep,    sep,    sep,    sep   }, ...
        {'template_cost.txt', ...
         'template_init.txt', ...
         'template_new.txt', ...
         'template_perturb.txt', ...
         'template_try_me.txt'} ...
        ) ;
%
cvtname = strrep(problemname,' ','_') ;
while 1 ~= strcmp(cvtname,problemname) ;
    problemname = cvtname ;
    cvtname = strrep(problemname,' ','_') ;
end
problemname = cvtname ;
newnames = strcat(...
        {problemname, problemname, problemname, problemname}, ...
        {'_cost.m', '_init.m', '_new.m', '_perturb.m'} ...
        ) ;
newnames{5} = 'try_me.m' ;
%
srcstr = 'PROBLEMNAME' ;
for i=1:5
    [finp, msg] = fopen(srcnames{i},'rt') ;
    if finp == -1
        error(msg) ;
    end
    [fout, msg] = fopen(newnames{i},'wt') ;
    if fout == -1
        error(msg) ;
    end
    %
    txtline = fgets(finp) ;
    while txtline ~= -1
        txtline = strrep(txtline,srcstr,problemname) ;
        fprintf(fout,'%s',txtline) ;
        txtline = fgets(finp) ;
    end
    %
    fclose(finp) ;
    fclose(fout) ;
end
````

</details>

#### nextstate · MATLAB · b4a870f2

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`13e837ea8c2fdb9091b9bb7204cf838ce9e03d9888418b11fe6fa7ecbdf5d636`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/nextstate.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/nextstate.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/nextstate.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [W,Ew,Evisit,Etrial] = nextstate(Ea,T,W,X,cost,moveclass,acceptrule,q)
% State-update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [W,Ew,Evisit,Eattempt] = nextstate(Ea,T,W,neighbor,X,energy) ;
%
%   Ea = average energy.
%   T = current temperature.
%   W = user-defined state.
%   X = user-defined problem domain or other data.
%   cost = (handle to) user-defined cost evaluation method, takes X and W as arguments.
%   moveclass = (handle to) user-defined neighbor generation method,
%       takes X, W, Ea, and T as arguments.
%   acceptrule = (handle to) SA Tools or user-defined method
%           a = acceptrule(dE,T,q)    where
%               dE = the difference in cost between a trial state and
%                       the current state: dE = Wtrial - W
%               T = the current temperature
%               q = any data required by the acceptrule
%               a = 0 if trial is rejected, otherwise 1.
%           SA Tools supplied methods are:
%               metropolis
%               szu
%               tsallis
%               threshold
%               franz
%   q = any data required by the acceptrule.
%   Ew = energy of user defined state.
%   Evisit = cost of incoming W.
%   Etrial = cost of neighbor state.
%
Ew = feval(cost,X,W) ;
Evisit = Ew ;
Wtrial = feval(moveclass,X,W,Ea,T) ;
Etrial = feval(cost,X,Wtrial) ;
dE = Etrial - Ew ;
if feval(acceptrule,dE,T,q)
    W = Wtrial ;
    Ew = Etrial ;
end
````

</details>

#### plotBins · MATLAB · 74d2187e

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `plotBins`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`b01e113fe1856e804352805302735cf6b9cd64d6c63e5bc0a82cb605cba8a655`
- 语言：MATLAB
- 符号：`plotBins`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/plotBins.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/plotBins.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/plotBins.m`

<details>
<summary>展开原始代码</summary>

````matlab
function plotBins(Xbin,Y,xstr,ystr,tstr)
% Binned data plot method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
% plotBins(Xbin,Y,xstr,ystr,tstr)
%
%   Xbin = bin centroids, min, and max
%           Xbin(1,:) are bin centroids.  Xbin(1,b) is the centroid for Y(b).
%           Xbin(2,:) are bin lower bounds
%           Xbin(3,:) are bin upper bounds
%   Y = frequency, or relative frequency, etc.
%           Y is the same size as Xbin(1,:)
%           Y is assumed to contain non-negative values.
%   xstr = Xbin axis label
%   ystr = Y axis label
%   tstr = plot title
%
[rows, bins] = size(Xbin) ;
%
Xbinmin = Xbin(2,1) ;
Xbinmax = Xbin(1,bins) ;    % instead of Xbin(3,bins)
Xbinrange = Xbinmax - Xbinmin ;
pad = 0.05*Xbinrange ;
xmin = Xbinmin - pad ;
xmax = Xbinmax + pad ;
ymin = 0 ;
ymax = 1.1*max(Y) ;
%
Sx(1) = Xbinmin ;
Sx(2:(bins+1)) = Xbin(2,:) ;
Sx(bins+2) = Xbin(3,bins) ;
Sx(bins+3) = Xbin(3,bins) ;
Sy(1) = 0 ;
Sy(2:(bins+1)) = Y ;
Sy(bins+2) = Y(bins) ;
Sy(bins+3) = 0 ;
%
axis([xmin xmax ymin ymax]) ;
hold on ;
title(tstr) ;
xlabel(xstr) ;
ylabel(ystr) ;
bar(Xbin(1,:),Y) ;
stairs(Sx,Sy,'r') ;
hold off ;
    
````

</details>

#### randomwalk · MATLAB · 7043b51f

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径。

- SHA-256：`deb18107ebd6d5484ae8f68acfb2711f9c26018d64945f3afe5ab92afa8b6aba`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/randomwalk.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/randomwalk.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/randomwalk.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/ensembleInit.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/ensembleInit.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/ensembleInit.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [W,Ew,Wbsf,Ebsf,Ea,Ev] = randomwalk(steps, walkers, newstate, X, cost, moveclass)
% Random walk method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [W,Ew,Wbsf,Ebsf,Ea,Ev] = randomwalk(steps, walkers, newstate, X, cost, moveclass) ;
%
%   INPUTS:
%       steps = the number of random steps to talk
%       walkers = number of walkers.  Must be positive integer.
%       newstate = (handle to) user-defined method
%           W0 = newstate(X)    where
%               X = user-defined problem domain or other data,
%                       behaviorally static.
%               W0 = an initial user-defined state.
%       X = user-defined problem domain or other data, behaviorally static.
%       cost = (handle to) user-defined objective method (function)
%           Ew = cost(X,W)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%       moveclass = (handle to) user-defined method,
%           W = moveclass(X,W,Ea,T)    where
%               X = user-defined problem domain or other data.
%               W = a user-defined state from 'newstate' or 'moveclass'.
%               Ea = average energy at current temperature.
%               T = current temperature (will be infinite in Tinit)
%   OUTPUTS:
%       W = cell array of user-defined state(s) from 'newstate' or 'moveclass'.
%       Ew = current energies corresponding to W (size walkers)
%       Ev = energy (cost) history at T  (T is Inf in random walk)
%               i = arbitrary index
%               Ev(i,1) = step #
%               Ev(i,2) = walker #
%               Ev(i,3) = an energy visited during T
%               Ev(i,4) = energy attempted from Ev(i,1:3) during T
%       Wbsf = cell array of best-so-far states of size 'walkers'
%       Ebsf = array of best-so-far energies
%       Ea = average energy
%
%   Calls ensembleInit(...) and then performs random walk accepting all moves.
%
[W,Ew,Wbsf,Ebsf,Ea] = ensembleInit(walkers, newstate, X, cost) ;
i = 1 ;
E = Ew ;
for k=1:steps
    for j=1:walkers
        Ev(i,1) = i ;
        Ev(i,2) = j ;
        Ev(i,3) = Ew(j) ;
        W{j} = feval(moveclass,X,W{j},Ea,Inf) ;
        Ew(j) = feval(cost,X,W{j}) ;
        if Ew(j) < Ebsf
            Wbsf{j} = W{j} ;
            Ebsf(j) = Ew(j) ;
        end
        Ev(i,4) = Ew(j) ;
        i = i + 1 ;
    end
    E = cat(2,E,Ew) ;
end
Ea = mean(E) ;
````

</details>

#### retrospect · MATLAB · 38aed5fc

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `retrospect`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`eca1a50f46761354df3d0e62f60af7b91be6090f95da7daf6181afae06a5f096`
- 语言：MATLAB
- 符号：`retrospect`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/retrospect.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/retrospect.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/retrospect.m`

<details>
<summary>展开原始代码</summary>

````matlab
function T = retrospect(Ea,Estd,walkers,dEtgt,v,e,T,t,P)
% Retrospective temperature update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   T = retrospect(Ea,Estd,walkers,dEtgt,v,e,T,t,P) ;
%
%   Ea = (not used) average energy.
%   Estd = (not used) standard deviation of energies
%   walkers = (not used) number of walkers
%   dEtgt = (not used) difference between present and previous target mean energy
%   v = (not used) thermodynamic speed.
%   e = (not used) estimate of relaxation time.
%   T =  (not used) current temperature.
%   t =  temperature step #.
%   P =  array containing temperature schedule; i.e., T(t+1) = P(t).
%
%   If you want temperature schedule
%           Tt = [1000, 100, 10, 1]
%   then set
%           schedule = @retrospect
%           Tinit = 1000
%           P = [100, 10, 1]
%           maxtemps = 4
%
%   If maxtemps exceeds the number of elements in P then the final temperature
%   will be repeated.
%
n = numel(P) ;
if t > n
    T = P(n) ;
else
    T = P(t) ;
end
````

</details>

#### satools · MATLAB · 918bb1c4

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`09b9d87fb7fe5861b664c818e4edb8995cd6c5cb5379d3407e8810c4faacc250`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/satools.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/satools.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/satools.m`

<details>
<summary>展开原始代码</summary>

````matlab
% COPYRIGHT file.  Type 'help anneal' for information.
%
% See http://www.frostconcepts.com/software for information on SA Tools.
% Get the book:  http://www.frostconcepts.com/books/ebsa/
% 
% Copyright
%  
%         Richard Frost
%         Frost Concepts
%         P.O. Box 721508
%         San Diego, CA 92172
%  
% Copyright (c) 2002, by Richard Frost and Frost Concepts.  All rights
% reserved except where otherwise noted.  This software is offered on an
% "AS IS" basis.  The copyright holder(s) provide no warranty, expressed
% or implied, that the software will function properly or that it will be
% free of errors.  This software may be freely copied and distributed for
% research and educational purposes only, provided that the above
% copyright notice appear in all copies.  A license is needed for
% commercial sale or use, in whole or in part, from Frost Concepts.
% Users of the software agree to acknowledge the copyright holder(s).
````

</details>

#### satoolsversion · MATLAB · 9a0db8bd

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`7644ee78d3ac119c6034e0470479fc155c6a3c2c624c5f5e97af649e3f54d358`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/satoolsversion.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/satoolsversion.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/satoolsversion.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [vnum, vdate] = satoolsversion
% Returns version string for SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   [vnum, vdate] = satoolsversion ;
%
%       vnum = version number, as a string
%       vdate = version date, as a string
%
vnum = '1.03' ;
vdate = '10/27/2002' ;
````

</details>

#### stillinger3Dpoints · MATLAB · 6b86e351

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`fca0a5b529aabd9938bec325c9fc2b07c04330dfe8b805b20c220043c12076ee`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/stillinger3Dpoints.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/stillinger3Dpoints.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/stillinger3Dpoints.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Cnew,overlapped] = stillinger3Dpoints(C,N,u)
% Stillinger 3D point cluster algorithm supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   Cnew = stillinger3Dpoints(C,N,u) ;
%
%   C = N 3D points;  C(1:N,1:3)
%   N = number of points
%   u = approximate optimal separation
%   Cnew = perturbed copy of C
%   overlapped = equals 1 if C contained points separated by less than u, 0 otherwise
%
%   If no overlapped points are found then the relative positions of the points
%   will not change.
%
%   Regardless of whether overlap is found, the centroid of the cluster will be
%   computed and then all points will be linearly translated so that the centroid
%   is at the origin.
%
overlapped = 0 ;
for j=1:N
    p(j,1:3) = 0 ;
    for i=1:(j-1)
        s = C(j,1:3) - C(i,1:3) ;
        d = norm(s) ;
        if d < u
            overlapped = 1 ;
            dd = ((u - d) / 2)*(.9 + (rand*.2)) ;
            p(j,1:3) = p(j,1:3) + ((dd/d)*s(1:3)) ;
        end
    end
    for i=(j+1):N
        s = C(j,1:3) - C(i,1:3) ;
        d = norm(s) ;
        if d < u
            overlapped = 1 ;
            dd = ((u - d) / 2)*(.9 + (rand*.2)) ;
            p(j,1:3) = p(j,1:3) + ((dd/d)*s(1:3)) ;
        end
    end
end
b(1:3) = 0 ;
for j=1:N
    Cnew(j,1:3) = C(j,1:3) + p(j,1:3) ;
    b(1:3) = b(1:3) + Cnew(j,1:3) ;
end
b = (b/N) ;
for j=1:N
    Cnew(j,1:3) = Cnew(j,1:3) - b(1:3) ;
end
````

</details>

#### szu · MATLAB · c6b6d919

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `szu`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`167e29eb27c086b6e280c5171437c3f0ea50fe17f343a0f3f90291a477d61295`
- 语言：MATLAB
- 符号：`szu`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/szu.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/szu.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/szu.m`

<details>
<summary>展开原始代码</summary>

````matlab
function a = szu(dE,T,q)
% Szu-Hartley "fast annealing" acceptance method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   a = szu(dE,T,q) ;
%
%   dE = the difference in cost between a trial state and
%     the current state: dE = Wtrial - W
%   T = the current temperature
%   q = (not used) any data required by the acceptrule
%   a = 0 if trial is rejected, otherwise 1.
%
a = 0 ;
if T > 0
    if rand < (1 / (1 + exp(dE/T)))
        a = 1 ;
    end
end
````

</details>

#### template_cost · MATLAB · 4c7f7c13

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `PROBLEMNAME_cost`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e72f46f0cc210c5577c2cf1ce45f22009c007954ee0c09a2af27de12148cffe2`
- 语言：MATLAB
- 符号：`PROBLEMNAME_cost`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/template_cost.txt`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/template_cost.txt`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/template_cost.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function Ew = PROBLEMNAME_cost(X,W)
% Ew = PROBLEMNAME_cost(X,W)
%
%   X = behaviorally constant application data
%
%   W = specific data about current state
%
%   Ew = energy corresponding to W
%
Ew = rand ;     % a typical application will use information from W and X to compute Ew.
````

</details>

#### template_init · MATLAB · b801532c

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `PROBLEMNAME_init`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cf3a17099fccefc4cfab0717da64c1370147d02a3ede773ff3a35272179ee98a`
- 语言：MATLAB
- 符号：`PROBLEMNAME_init`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/template_init.txt`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/template_init.txt`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/template_init.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function X = PROBLEMNAME_init()
% X = PROBLEMNAME_init()
%
%   X = behaviorally constant application data
%
X = [] ;        % a typical application will put problem domain data here
````

</details>

#### template_new · MATLAB · ac160086

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `PROBLEMNAME_new`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`0477642751a005607390483fc39081420db20a0f4ef4cdda1432b5f584d1766a`
- 语言：MATLAB
- 符号：`PROBLEMNAME_new`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/template_new.txt`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/template_new.txt`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/template_new.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function W = PROBLEMNAME_new(X)
% W = PROBLEMNAME_new(X)
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   W = PROBLEMNAME_new(X) ;
%
%   X = behaviorally constant application data
%
%   W = specific data about current state
%
%   Instantiates a new state.
%
W = [] ;    % a typical application will put state specific data here
````

</details>

#### template_perturb · MATLAB · 2ada0204

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `PROBLEMNAME_perturb`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2609d75e2dd5f3954a654d7b9a203b857581691c809ca4cb698e63eeb90d0ae9`
- 语言：MATLAB
- 符号：`PROBLEMNAME_perturb`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/template_perturb.txt`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/template_perturb.txt`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/template_perturb.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function W = PROBLEMNAME_perturb(X,W,Ea,T)
% W = PROBLEMNAME_perturb(X,W,Ea,T)
%
%   X = behaviorally constant application data
%
%   W = (on input) current state, (on output) next state.
%
%   Ea = current average energy
%   T = current temperature
%
````

</details>

#### template_try_me · MATLAB · 761766f1

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `try_me`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`255ee88a9df9d61e00b461f8ff0e15f45b37b25fdde5b3aed1be7d8237f57201`
- 语言：MATLAB
- 符号：`try_me`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/template_try_me.txt`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/template_try_me.txt`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/template_try_me.txt`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/anneal.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/dispEh.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/dispMat.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/plotBins.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/anneal.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/dispEh.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/dispMat.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/plotBins.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/anneal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/dispEh.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/dispMat.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/plotBins.m`

<details>
<summary>展开原始代码</summary>

````matlab
function try_me
% Example SA Tools annealing for PROBLEMNAME.
%
%
rand('state',sum(100*clock)) ;
%
verbose = 1 ;
%
newstate =  @PROBLEMNAME_new ;
X =          PROBLEMNAME_init ;
cost =      @PROBLEMNAME_cost ;
moveclass = @PROBLEMNAME_perturb ;
%
walkers =       16 ;
acceptrule =    @metropolis ;
q =             0 ;
schedule =      @thermospeedR ;
P =             0 ;
equilibrate =   @hoffmann ;
C =             1.25 ;
maxsteps =      48 ;
Tinit =         @TinitAccept ;
r =             [0.5, 48] ;
Tfinal =        @TfinalNstop ;
f =             [4, 1e-3] ;
maxtemps =      10 ;
v =             0.2 ;
bins =          10 ;
e =             Inf ;
%
disp(['--------------------------------start--------------------------------']) ;
%
%
    [W,Ew,Wbsf,Ebsf,Tt,Et,Etarget,ert,Kt,Ebsft,Eh,M,rho,Ebin] = ...
        anneal(verbose, ...
            newstate, X, ...
            cost, moveclass, ...
            walkers, ...
            acceptrule,q, ...
            schedule, P, ...
            equilibrate, C, maxsteps, ...
            Tinit, r, ...
            Tfinal, f, maxtemps, ...
            v, bins, e) ;
%
    dispMat(rho,'rho','%6.2f') ;
    dispMat(Ebin,'Ebin','%6.2f') ;
%   plotBins(Ebin,rho,'E','rho','equilibrium density of states') ;
%   dispEh(Eh) ;
%
disp(['---------------------------------end---------------------------------']) ;
````

</details>

#### thermospeedHC · MATLAB · 4ee6e6e8

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `thermospeedHC`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`372b40e64956fe86db2ef38716014dc1479ec6109f9e72a79f049dc3cef6a0a2`
- 语言：MATLAB
- 符号：`thermospeedHC`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/thermospeedHC.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/thermospeedHC.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/thermospeedHC.m`

<details>
<summary>展开原始代码</summary>

````matlab
function T = thermospeedHC(Ea,Estd,walkers,dEtgt,v,e,T,t,P)
% Heat capacity thermospeed temperature update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   T = thermospeedHC(Ea,Estd,walkers,dEtgt,v,e,T,t,P) ;
%
%   Ea = (not used) average energy.
%   Estd = standard deviation of energies
%   walkers = (not used) number of walkers
%   dEtgt = difference between present and previous target mean energy
%   v = (not used) thermodynamic speed.
%   e = (not used) estimate of relaxation time.
%   T = current temperature.
%   t = (not used) temperature step #.
%   P = (not used) constant
%
%   Temperature will not change if
%       1. Estd is zero
%       2. Input T is negative, zero, or infinite
%       3. The calculated temperature would be negative or infinite
%
if (Estd > 0) & (T > 0) & (T ~= Inf)
    B = 1/T ;                       % use inverse temperature for stability
    dB = -dEtgt / (Estd*Estd) ;
    B = B + dB ;
    if B > 0                        % only change if stable
        T = 1 / B ;
    end
end
````

</details>

#### thermospeedR · MATLAB · 623bf62c

- 归属算法：模拟退火SA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“数据读取与预处理”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `thermospeedR`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`1dfe1d45874fd9091699d829b2e56de9f06ffea59fd9b54b8f20e9f5cd3a37cb`
- 语言：MATLAB
- 符号：`thermospeedR`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/thermospeedR.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/thermospeedR.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/thermospeedR.m`

<details>
<summary>展开原始代码</summary>

````matlab
function T = thermospeedR(Ea,Estd,walkers,dEtgt,v,e,T,t,P)
% Heat capacity thermospeed temperature update method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   T = thermospeedR(Ea,Estd,walkers,dEtgt,v,e,T,t,P) ;
%
%   Ea = (not used) average energy.
%   Estd = standard deviation of energies
%   walkers = (not used) number of walkers
%   dEtgt = (not used) difference between present and previous target mean energy
%   v = thermodynamic speed.
%   e = estimate of relaxation time.
%   T = current temperature.
%   t = (not used) temperature step #.
%   P = (not used) constant
%
%   Temperature will not change if
%       1. Estd or e are zero
%       2. Input T is negative, zero, or infinite
%       3. The calculated temperature would be negative
%
if (Estd == 0) | (e == 0) | (T <= 0) | (T == Inf)
    dT = 0 ;
else
    dT = -v*((T*T)/(e*Estd)) ;
    if dT < -T
        dT = 0 ;        % do nothing if unstable
    end
end
T = T + dT ;
````

</details>

#### threshold · MATLAB · ab8791dd

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `threshold`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`8098ae8161209cfb1db7270f824dc9a744a40e3338397dea0c8c958864a62459`
- 语言：MATLAB
- 符号：`threshold`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/threshold.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/threshold.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/threshold.m`

<details>
<summary>展开原始代码</summary>

````matlab
function a = threshold(dE,T,q)
% Threshold acceptance method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   a = threshold(dE,T,q) ;
%
%   dE = the difference in cost between a trial state and
%     the current state: dE = Wtrial - W
%   T = the current temperature.  Must be positive.
%   q = (not used) the "q" parameter of the acceptance rule
%   a = 0 if trial is rejected, otherwise 1.
%
if (T > 0) & (dE <= T)
    a = 1 ;
else
    a = 0 ;
end
````

</details>

#### tsallis · MATLAB · 6875cf9b

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `tsallis`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`8b10b8c6d0e872e64aff31f8446411cccac9ed103a440e8c7b3f096e0aa655b5`
- 语言：MATLAB
- 符号：`tsallis`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/satools/m/tsallis.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/遗传退火算法工具箱（二）/tsallis.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/一个Matlab的模拟退火算法工具箱/tsallis.m`

<details>
<summary>展开原始代码</summary>

````matlab
function a = tsallis(dE,T,q)
% Tsallis acceptance method supplied with SA Tools.
% Copyright (c) 2002, by Richard Frost and Frost Concepts.
% See http://www.frostconcepts.com/software for information on SA Tools.
%
%   a = tsallis(dE,T,q) ;
%
%   dE = the difference in cost between a trial state and
%     the current state: dE = Wtrial - W
%   T = the current temperature
%   q = the "q" parameter of the tsallis acceptance rule
%   a = 0 if trial is rejected, otherwise 1.
%
a = 0 ;
if T > 0
    if (dE <= 0) | (q == 1)
        a = 1 ;
    else
        D = (1 - q)*(dE/T) ;
        if D <= 1
            if rand < (1 - D)^(1/(1-q))
                a = 1 ;
            end
        end
    end
end
````

</details>

#### monituihuo · MATLAB · 5bd60b49

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`3afb99e4b4d2b918734519292327c05ea5d71d7a7268ae30a9a072c737bf0f0a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/模拟退火算法/monituihuo.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear 
load sj.txt    %加载敌方100 个目标的数据， 数据按照表格中的位置保存在纯文本文件 sj.txt 中 
x=sj(:,1:2:8);x=x(:); 
y=sj(:,2:2:8);y=y(:); 
sj=[x y]; d1=[70,40];  
sj=[d1;sj;d1]; sj=sj*pi/180; 
d=zeros(102); %距离矩阵 d 
for i=1:101 
    for j=i+1:102 
        temp=cos(sj(i,1)-sj(j,1))*cos(sj(i,2))*cos(sj(j,2))+sin(sj(i,2))*sin(sj(j,2)); 
        d(i,j)=6370*acos(temp); 
    end 
end 
d=d+d'; 
S0=[];Sum=inf; 
rand('state',sum(clock)); 
for j=1:1000 
    S=[1 1+randperm(100),102]; 
    temp=0; 
        for i=1:101 
        temp=temp+d(S(i),S(i+1)); 
    end 
    if temp<Sum 
        S0=S;Sum=temp; 
    end 
end 
e=0.1^30;L=20000;at=0.999;T=1; 
%退火过程 
for k=1:L 
   %产生新解 
c=2+floor(100*rand(1,2)); 
c=sort(c); 
c1=c(1);c2=c(2); 
  %计算代价函数值 
  df=d(S0(c1-1),S0(c2))+d(S0(c1),S0(c2+1))-d(S0(c1-1),S0(c1))-d(S0(c2),S0(c2+1)); 
   %接受准则 
  if df<0 
  S0=[S0(1:c1-1),S0(c2:-1:c1),S0(c2+1:102)];       
  Sum=Sum+df; 
  elseif exp(-df/T)>rand(1) 
  S0=[S0(1:c1-1),S0(c2:-1:c1),S0(c2+1:102)]; 
  Sum=Sum+df; 
   end 
  T=T*at; 
   if T<e 
       break; 
   end 
end 
 %  输出巡航路径及路径长度 
S0,Sum
path=IX(IZ(1),:) 
long=DZ(1) 
toc 
xx=sj0(path,1);yy=sj0(path,2); 
plot(xx,yy,'-o') 
````

</details>

#### 模拟退火算法及禁忌搜索算法的matlab源程序 · MATLAB · e3f4ec49

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `ChangePath2`、`Fun`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`d803488e9760961e35d099f63e9e927f446f70acac9ee4e6f136cca61973ff8d`
- 语言：MATLAB
- 符号：`ChangePath2`, `Fun`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/模拟退火算法及禁忌搜索算法的matlab源程序.txt`

<details>
<summary>展开原始代码</summary>

````matlab
%%%  模拟退火算法源程序 

%  此题以中国31省会城市的最短旅行路径为例 

%  clear;clc; 

function [MinD,BestPath]=MainAneal(pn) 

% CityPosition存储的为每个城市的二维坐标x和y 

CityPosition=[1304 2312;3639 1315;4177 2244;3712 1399;3488 1535;3326 1556;3238 1229;... 

               4196 1044;4312  790;4386  570;3007 1970;2562 1756;2788 1491;2381 

1676;... 

               1332  695;3715 1678;3918 2179;4061 2370;3780 2212;3676 2578;4029 

2838;... 

               4263 2931;3429 1908;3507 2376;3394 2643;3439 3201;2935 3240;3140 

3550;... 

               2545 2357;2778 2826;2370 2975]; 

figure(1); 

plot(CityPosition(:,1),CityPosition(:,2),'o') 

 

m=size(CityPosition,1);%城市的数目 

% 

D = sqrt((CityPosition(:,ones(1,m)) - CityPosition(:,ones(1,m))').^2 + ... 

         (CityPosition(:,2*ones(1,m)) - CityPosition(:,2*ones(1,m))').^2); 

path=zeros(pn,m); 

for i=1:pn 

    path(i,:)=randperm(m);  

end 

 

iter_max=100;%i 

m_max=5;%  

Len1=zeros(1,pn);Len2=zeros(1,pn);path2=zeros(pn,m); 

t=zeros(1,pn); 

T=1e5; tau=1e-5; 

N=1; 

while T>=tau         

      iter_num=1;  

      m_num=1;  

      while m_num<m_max && iter_num<iter_max 

            for i=1:pn 

                Len1(i)=sum([D(path(i,1:m-1)+m*(path(i,2:m)-1)) 

D(path(i,m)+m*(path(i,1)-1))]);  

                path2(i,:)=ChangePath2(path(i,:),m);  

                Len2(i)=sum([D(path2(i,1:m-1)+m*(path2(i,2:m)-1)) 

D(path2(i,m)+m*(path2(i,1)-1))]); 

            end 

            R=rand(1,pn); 

            if find((Len2-Len1<t&exp((Len1-Len2)/T)>R)~=0)                 

path(find((Len2-Len1<t&exp((Len1-Len2)/T)>R)~=0),:)=path2(find((Len2-Len1<t&exp((Len1-L

en2)/T)>R)~=0),:); %#ok<FNDSB> 

                

Len1(find((Len2-Len1<t&exp((Len1-Len2)/T)>R)~=0))=Len2(find((Len2-Len1<t&exp((Len1-Le

n2)/T)>R)~=0)); 

                [TempMinD,TempIndex]=min(Len1); 

                TracePath(N,:)=path(TempIndex,:); %#ok<AGROW> 

                Distance(N)=TempMinD; %#ok<AGROW> 

                N=N+1; 

                else 

                m_num=m_num+1; 

            end 

end 

            iter_num=iter_num+1; 

            T=T*0.9; 

end 

[MinD,Index]=min(Distance); 

BestPath=TracePath(Index,:);%disp(MinD) 

%画出路线图 

figure(2); 

plot(CityPosition(BestPath(1:end-1),1),CityPosition(BestPath(1:end-1),2),'r*-'); 

 

function p2=ChangePath2(p1,CityNum) 

while(1) 

     R=unidrnd(CityNum,1,2); 

     if abs(R(1)-R(2)) > 0 

         break; 

     end 

end 

I=R(1);J=R(2); 

if I<J 

   p2(1:I)=p1(1:I); 

   p2(I+1:J)=p1(J:-1:I+1); 

   p2(J+1:CityNum)=p1(J+1:CityNum); 

else 

   p2(1:J-1)=p1(1:J-1); 

   p2(J:I+1)=p1(I+1:-1:J); 

   p2(I:CityNum)=p1(I:CityNum); 

end 

 

 

 

%%%  禁忌搜索算法解决TSP问题  %此题以中国31省会城市的最短旅行路径为例 

%禁忌搜索是对局部领域搜索的一种扩展,是一种全局逐步寻优算法,搜索过程可以接受劣解,

有较强的爬山能力.领域结构对收敛性有很大影响。 

function [BestShortcut,theMinDistance]=TabuSearch 

clear; 

clc; 

Clist=[1304 2312;3639 1315;4177 2244;3712 1399;3488 1535;3326 1556;3238 1229;... 

    4196 1044;4312  790;4386  570;3007 1970;2562 1756;2788 1491;2381 1676;... 

    1332  695;3715 1678;3918 2179;4061 2370;3780 2212;3676 2578;4029 2838;... 

    4263 2931;3429 1908;3507 2376;3394 2643;3439 3201;2935 3240;3140 3550;... 

    2545 2357;2778 2826;2370 2975]; 

CityNum=size(Clist,1);%TSP问题的规模,即城市数目 

dislist=zeros(CityNum);  

for i=1:CityNum 

    for j=1:CityNum 

        dislist(i,j)=((Clist(i,1)-Clist(j,1))^2+(Clist(i,2)-Clist(j,2))^2)^0.5;        

    end 

end 

TabuList=zeros(CityNum);% (tabu list) 

TabuLength=round((CityNum*(CityNum-1)/2)^0.5);%禁忌长度(tabu length) 

Candidates=200;%候选集的个数 (全部领域解个数) 

CandidateNum=zeros(Candidates,CityNum);%候选解集合 

S0=randperm(CityNum);%随机产生初始解 

BSF=S0; 

BestL=Inf; 

clf;  

figure(1); 

stop = uicontrol('style','toggle','string'… 

,'stop','background','white'); 

tic; 

p=1; 

StopL=80*CityNum; 

while p<StopL 

    if Candidates>CityNum*(CityNum-1)/2 

        disp('候选解个数不大于n*(n-1)/2!'); 

        break; 

    end 

    ALong(p)=Fun(dislist,S0);      

     

    i=1; 

    A=zeros(Candidates,2); 

    while i<=Candidates         

        M=CityNum*rand(1,2); 

        M=ceil(M);         if M(1)~=M(2) 

            A(i,1)=max(M(1),M(2)); 

            A(i,2)=min(M(1),M(2)); 

                if i==1 

                isa=0; 

            else 

                for j=1:i-1 

                    if A(i,1)==A(j,1) && A(i,2)==A(j,2) 

                        isa=1; 

                        break; 

                    else 

                        isa=0; 

                    end 

                end 

            end  

            if ~isa 

               i=i+1; 

            else  

            end             

        else  

        end 

    end 

     

    BestCandidateNum=100;%保留前BestCandidateNum个最好候选解 

    BestCandidate=Inf*ones(BestCandidateNum,4); 

    F=zeros(1,Candidates); 

    for i=1:Candidates 

        CandidateNum(i,:)=S0; 

        CandidateNum(i,[A(i,2),A(i,1)])=S0([A(i,1),A(i,2)]); 

        F(i)=Fun(dislist,CandidateNum(i,:)); 

        if i<=BestCandidateNum 

            BestCandidate(i,2)=F(i); 

            BestCandidate(i,1)=i; 

            BestCandidate(i,3)=S0(A(i,1)); 

            BestCandidate(i,4)=S0(A(i,2));    

        else 

            for j=1:BestCandidateNum 

                if F(i)<BestCandidate(j,2) 

                    BestCandidate(j,2)=F(i); 

                    BestCandidate(j,1)=i; 

                    BestCandidate(j,3)=S0(A(i,1)); 

                    BestCandidate(j,4)=S0(A(i,2)); 

                    break; 

                end                         end 

        end 

    end 

    %对BestCandidate  

    [JL,Index]=sort(BestCandidate(:,2));  

    SBest=BestCandidate(Index,:); 

    BestCandidate=SBest; 

     

      if BestCandidate(1,2)<BestL 

        BestL=BestCandidate(1,2); 

        S0=CandidateNum(BestCandidate(1,1),:);         

        BSF=S0; 

        for m=1:CityNum 

            for n=1:CityNum 

                if TabuList(m,n)~=0 

                    TabuList(m,n)=TabuList(m,n)-1; 

                end 

            end 

        end 

        TabuList(BestCandidate(1,3),BestCandidate(1,4))=TabuLength; 

    else   

        for  

i=1:BestCandidateNum 

            if  TabuList(BestCandidate(i,3),BestCandidate(i,4))==0 

                S0=CandidateNum(BestCandidate(i,1),:);                 

            for m=1:CityNum 

                for n=1:CityNum 

                    if TabuList(m,n)~=0 

                        TabuList(m,n)=TabuList(m,n)-1; 

                    end 

                end 

            end         

            TabuList(BestCandidate(i,3),BestCandidate(i,4))=TabuLength; 

            break; 

            end 

        end 

    end     

    p=p+1; 

    ArrBestL(p)=BestL; %#ok<AGROW> 

    for i=1:CityNum-1 

        plot([Clist(BSF(i),1),Clist(BSF(i+1),1)],[Clist(BSF(i),2),Clist(BSF(i+1),2)],'bo-'); 

        hold on; 

    end 

    plot([Clist(BSF(CityNum),1),Clist(BSF(1),1)],[Clist(BSF(CityNum),2),Clist(BSF(1),2)],'ro-'); 

    title(['Counter:',int2str(p*Candidates),'  The Min Distance:',num2str(BestL)]); 

    hold off; 

    pause(0.005);     

    if get(stop,'value')==1 

        break; 

    end 

end 

toc; 

BestShortcut=BSF; 

theMinDistance=BestL; 

set(stop,'style','pushbutton','string',… 

'close', 'callback','close(gcf)'); 

figure(2); 

plot(ArrBestL,'r'); hold on; 

plot(ALong,'b');grid; 

title('搜索过程'); 

legend('Best So Far','当前解'); 

end 

 

function F=Fun(dislist,s) %#ok<DEFunNU> 

DistanV=0; 

n=size(s,2); 

for i=1:(n-1) 

    DistanV=DistanV+dislist(s(i),s(i+1)); 

end 

DistanV=DistanV+dislist(s(n),s(1));       

F=DistanV; 

end 

 
````

</details>

#### example23_3 · MATLAB · c7fe8f48

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `example23_3`、`fun1`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`b731c576d894cecdd59ae71c9b28ee4943744b9ffc0fff0e49c7fc22b12f25fe`
- 语言：MATLAB
- 符号：`example23_3`, `fun1`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/模拟退火/直接搜索算法/example23_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
function example23_3 
a=[-1 -2 0;-1 0 0];b=[-1;0]; 
[x,y]=patternsearch(@fun1,rand(1,3),a,b,[],[],[],[],@fun2);  %初始值必须为行向量 
x,y=-y 
%定义目标函数 
function y=fun1(x);   %x为行向量 
c1=[2 3 1]'; c2=[3 1 0]'; 
y=x*c1+x.^2*c2; y=-y; 
%定义非线性约束函数 
function [f,g]=fun2(x); 
f=[x(1)+2*x(1)^2+x(2)+2*x(2)^2+x(3)-10 
   x(1)+x(1)^2+x(2)+x(2)^2-x(3)-50 
   2*x(1)+x(1)^2+2*x(2)+x(3)-40]; 
g=x(1)^2+x(3)-2; 
````

</details>

#### CRTBASE · MATLAB · f292a858

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `crtbase`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e0a5dec9709b6d5c6ebafa3f4a452d455710626114c4add503b1968c4c62a22a`
- 语言：MATLAB
- 符号：`crtbase`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/CRTBASE.M`

<details>
<summary>展开原始代码</summary>

````matlab
% CRTBASE.m - Create base vector 
%
% This function creates a vector containing the base of the loci
% in a chromosome.
%
% Syntax: BaseVec = crtbase(Lind, Base)
%
% Input Parameters:
%
%		Lind	- A scalar or vector containing the lengths
%			  of the alleles.  Sum(Lind) is the length of
%			  the corresponding chromosome.
%
%		Base	- A scalar or vector containing the base of
%			  the loci contained in the Alleles.
%
% Output Parameters:
%
%		BaseVec	- A vector whose elements correspond to the base
%			  of the loci of the associated chromosome structure.

% Author: Andrew Chipperfield
% Date: 19-Jan-94

function BaseVec = crtbase(Lind, Base)

[ml LenL] = size(Lind) ;
if nargin < 2 
	Base = 2 * ones(LenL,1) ; % default to base 2
end
[mb LenB] = size(Base) ;

% check parameter consistency
if ml > 1 | mb > 1
	error( 'Lind or Base is not a vector') ;
elseif (LenL > 1 & LenB > 1 & LenL ~= LenB) | (LenL == 1 & LenB > 1 ) 
	error( 'Vector dimensions must agree' ) ;
elseif LenB == 1 & LenL > 1
	Base = Base * ones(LenL,1) ;
	
end

BaseVec = [] ;
for i = 1:LenL
	BaseVec = [BaseVec, Base(i)*ones(Lind(i),1)'];
end

````

</details>

#### CRTBP · MATLAB · 8e10d95c

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`894b8535d97486a598d8143bcf8fef1d72907caff3870db4955f7a996518a5d2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/CRTBP.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/CRTBASE.M`

<details>
<summary>展开原始代码</summary>

````matlab
% CRTP.m - Create an initial population
%
% This function creates a binary population of given size and structure.
%
% Syntax: [Chrom Lind BaseV] = crtbp(Nind, Lind, Base)
%
% Input Parameters:
%
%		Nind	- Either a scalar containing the number of individuals
%			  in the new population or a row vector of length two
%			  containing the number of individuals and their length.
%
%		Lind	- A scalar containing the length of the individual
%			  chromosomes.
%
%		Base	- A scalar containing the base of the chromosome 
%			  elements or a row vector containing the base(s) 
%			  of the loci of the chromosomes.
%
% Output Parameters:
%
%		Chrom	- A matrix containing the random valued chromosomes 
%			  row wise.
%
%		Lind	- A scalar containing the length of the chromosome.
%
%		BaseV	- A row vector containing the base of the 
%			  chromosome loci.

% Author: Andrew Chipperfield
% Date:	19-Jan-94

function [Chrom, Lind, BaseV] = crtbp(Nind, Lind, Base)
nargs = nargin ;

% Check parameter consistency

if nargs >= 1, [mN, nN] = size(Nind) ; end
if nargs >= 2, [mL, nL] = size(Lind) ; end
if nargs == 3, [mB, nB] = size(Base) ; end

if nN == 2
   if (nargs == 1) 
      Lind = Nind(2) ; Nind = Nind(1) ; BaseV = crtbase(Lind) ;
   elseif (nargs == 2 & nL == 1) 
      BaseV = crtbase(Nind(2),Lind) ; Lind = Nind(2) ; Nind = Nind(1) ; 
   elseif (nargs == 2 & nL > 1) 
      if Lind ~= length(Lind), error('Lind and Base disagree'); end
      BaseV = Lind ; Lind = Nind(2) ; Nind = Nind(1) ; 
   end
elseif nN == 1
   if nargs == 2
      if nL == 1, BaseV = crtbase(Lind) ;
      else, BaseV = Lind ; Lind = nL ; end
   elseif nargs == 3
      if nB == 1, BaseV = crtbase(Lind,Base) ; 
      elseif nB ~= Lind, error('Lind and Base disagree') ; 
      else BaseV = Base ; end
   end
else
   error('Input parameters inconsistent') ;
end

% Create a structure of random chromosomes in row wise order, dimensions
% Nind by Lind. The base of each chromosomes loci is given by the value
% of the corresponding element of the row vector base.

Chrom = floor(rand(Nind,Lind).*BaseV(ones(Nind,1),:)) ;


% End of file 

````

</details>

#### CRTRP · MATLAB · 433fc496

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `crtrp`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`900cb8e84a5ad67fa6798ce0ae0b4a45b9bef93b5cad9a8119c108ecadfd1b36`
- 语言：MATLAB
- 符号：`crtrp`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/CRTRP.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% CRTRP.M        (CReaTe an initial (Real-value) Population)
%
% This function creates a population of given size of random real-values. 
%
% Syntax:       Chrom = crtrp(Nind,FieldDR);
%
% Input parameters:
%    Nind      - A scalar containing the number of individuals in the new 
%                population.
%
%    FieldDR   - A matrix of size 2 by number of variables describing the
%                boundaries of each variable. It has the following structure:
%                [lower_bound;   (vector with lower bound for each veriable)
%                 upper_bound]   (vector with upper bound for each veriable)
%                [lower_bound_var_1  lower_bound_var_2 ... lower_bound_var_Nvar;
%                 upper_bound_var_1  upper_bound_var_2 ... upper_bound_var_Nvar]
%                example - each individuals consists of 4 variables:
%                FieldDR = [-100 -50 -30 -20;   % lower bound
%                            100  50  30  20]   % upper bound
%              
% Output parameter:
%    Chrom     - A matrix containing the random valued individuals of the
%                new population of size Nind by number of variables.

% Author:     Hartmut Pohlheim
% History:    23.11.93     file created
%             25.02.94     clean up, check parameter consistency


function Chrom = crtrp(Nind,FieldDR);

% Check parameter consistency
   if nargin < 2, error('parameter FieldDR missing'); end
   if nargin > 2, nargin = 2; end

   [mN, nN] = size(Nind);
   [mF, Nvar] = size(FieldDR);

   if (mN ~= 1 & nN ~= 1), error('Nind has to be a scalar'); end
   if mF ~= 2, error('FieldDR must be a matrix with 2 rows'); end

% Compute Matrix with Range of variables and Matrix with Lower value
   Range = rep((FieldDR(2,:)-FieldDR(1,:)),[Nind 1]);
   Lower = rep(FieldDR(1,:), [Nind 1]);

% Create initial population
% Each row contains one individual, the values of each variable uniformly
% distributed between lower and upper bound (given by FieldDR)
   Chrom = rand(Nind,Nvar) .* Range + Lower;


% End of function

````

</details>

#### FCMfun · MATLAB · df2b92eb

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`da388fc4191be7bdac76315ad1cc239afa1fa5346c69f3837b7538916c085143`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/FCMfun.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/initFCM.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/iterateFCM.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [obj,center,U]=FCMfun(X,cluster_n,center,options)
%% FCM主函数
% 输入
%        X：样本数据
%cluster_n：聚类数
%   center：初始聚类中心矩阵
%  options：设置幂指数，最大迭代次数，目标函数的终止容限
% 输出
%    obj：目标输出Jb值
% center：优化后的聚类中心
%      U：相似分类矩阵
X_n=size(X,1);
in_n=size(X,2);
b=options(1);		    % 加权参数
max_iter=options(2);		% 最大迭代次数
min_impro=options(3);		% 相邻两次迭代最小改进（用来判断是否提前终止）
obj_fcn=zeros(max_iter,1);	% 初始化目标值矩阵
U = initFCM(X,cluster_n,center,b);			% 初始化聚类相似矩阵
% 主函数循环
for i = 1:max_iter,
    [U, center,obj_fcn(i)]=iterateFCM(X,U,cluster_n,b);
    % 核对终止条件
    if i > 1
        if abs(obj_fcn(i) - obj_fcn(i-1)) < min_impro, break; end,
    end
end
iter_n = i;	% 真实迭代次数
obj_fcn(iter_n+1:max_iter)=[];
obj=obj_fcn(end);
````

</details>

#### FCMpure · MATLAB · 3969ca7d

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`d171aff17d3fca61f2d811f0abe88e72b57240b2338f70d1bee0a33ceb2d8366`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/FCMpure.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 1、随机产生初始聚类中心
% clc;
clear
%% 加载数据
load X
figure
plot(X(:,1),X(:,2),'o')
xlabel('横坐标X');ylabel('纵坐标Y');title('样本数据')
hold on
%% 进行模糊C均值聚类
% 设置幂指数为3，最大迭代次数为20，目标函数的终止容限为1e-6
options=[3,20,1e-6,0];
% 调用fcm函数进行模糊C均值聚类，返回类中心坐标矩阵center，隶属度矩阵U，目标函数值obj_fcn
cn=4; %聚类数
[center,U,obj_fcn]=fcm(X,cn,options);
Jb=obj_fcn(end)
maxU = max(U);
index1 = find(U(1,:) == maxU);
index2 = find(U(2, :) == maxU);
index3 = find(U(3, :) == maxU);
%% 分类情况
% 在前三类样本数据中分别画上不同记号 不加记号的就是第四类了
line(X(index1,1), X(index1, 2), 'linestyle', 'none', 'marker', 'x', 'color', 'g'); 
line(X(index2,1), X(index2, 2), 'linestyle', 'none', 'marker', '*', 'color', 'r');
line(X(index3,1), X(index3, 2), 'linestyle', 'none', 'marker', '+', 'color', 'b');
%% 画出聚类中心
plot(center(:,1),center(:,2),'v')
hold off
````

</details>

#### MIGRATE · MATLAB · cae0b97a

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`8294ef22c9e4017f0b8f14ca16d39e04ff6a922b813b78f5bb7c3034d2efeeb3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MIGRATE.M`

<details>
<summary>展开原始代码</summary>

````matlab
% MIGRATE.M      (MIGRATion of individuals between subpopulations)
%
% This function performs migration of individuals.
%
% Syntax:  [Chrom, ObjV] = migrate(Chrom, SUBPOP, MigOpt, ObjV)
%
% Input parameters:
%    Chrom     - Matrix containing the individuals of the current
%                population. Each row corresponds to one individual.
%    SUBPOP    - Number of subpopulations
%    MigOpt    - (optional) Vector containing migration parameters
%                MigOpt(1): MIGR - Rate of individuals to be migrated per
%                           subpopulation (% of subpopulation)
%                           if omitted or NaN, 0.2 (20%) is assumed
%                MigOpt(2): Select - number indicating the selection method
%                           of replacing individuals
%                           0 - uniform selection
%                           1 - fitness-based selection (replace worst 
%                                  individuals)
%                           if omitted or NaN, 0 is assumed
%                MigOpt(3): Structure - number indicating the structure
%                           of the subpopulations for migration
%                           0 - net structure (unconstrained migration)
%                           1 - neighbourhood structure
%                           2 - ring structure
%                           if omitted or NaN, 0 is assumed
%    ObjV      - (optional) Column vector containing the objective values
%                of the individuals in the current population, needed for
%                fitness-based migration, this saves the
%                recalculation of objective values for population.
%
% Output parameters:
%    Chrom     - Matrix containing the individuals of the current
%                population after migration.
%    ObjV      - if ObjV is input parameter, than column vector containing
%                the objective values of the individuals of the current
%                generation after migration.
           
% Author:     Hartmut Pohlheim
% History:    16.02.94     file created
%             18.02.94     comments at the beginning added
%                          exchange of ObjV too
%             25.02.94     clean up
%             26.02.94     ObjV optional input parameter
%                          Select and Structure added, parameter reordered
%             17.03.94     renamed to migrate.m, more parameter checks

function [Chrom, ObjV] = migrate(Chrom, SUBPOP, MigOpt, ObjV);


% Check parameter consistency
   if nargin < 2, error('Input parameter SUBPOP missing'); end
   if (nargout == 2 & nargin < 4), error('Input parameter ObjV missing'); end

   [Nind, Nvar] = size(Chrom);
   if length(SUBPOP) ~= 1, error('SUBPOP must be a scalar'); end
   if SUBPOP == 1, return; end
   if (Nind/SUBPOP) ~= fix(Nind/SUBPOP), error('Chrom and SUBPOP disagree'); end
   NIND = Nind/SUBPOP;  % Compute number of individuals per subpopulation
   
   if nargin > 3, 
      [mO, nO] = size(ObjV);
      if nO ~= 1, error('ObjV must be a column vector'); end
      if Nind ~= mO, error('Chrom and ObjV disagree'); end
      IsObjV = 1;
   else IsObjV = 0; ObjV = [];
   end

   if nargin < 3, MIGR = 0.2; Select = 0; Structure = 0; end   
   if nargin > 2,
      if isempty(MigOpt), MIGR = 0.2; Select = 0; Structure = 0;
      elseif isnan(MigOpt), MIGR = 0.2; Select = 0; Structure = 0;
      else
         MIGR = NaN; Select = NaN; Structure = NaN;
         if length(MigOpt) > 3, error('Parameter MigOpt is too long'); end
         if length(MigOpt) >= 1, MIGR = MigOpt(1); end
         if length(MigOpt) >= 2, Select = MigOpt(2); end
         if length(MigOpt) >= 3, Structure = MigOpt(3); end
         if isnan(MIGR), MIGR =0.2; end
         if isnan(Select), Select = 0; end
         if isnan(Structure), Structure = 0; end
      end
   end
   
   if (MIGR < 0 | MIGR > 1), error('Parameter for migration rate must be a scalar in [0 1]'); end
   if (Select ~= 0 & Select ~= 1), error('Parameter for selection method must be 0 or 1'); end
   if (Structure < 0 | Structure > 2), error ('Parameter for structure must be 0, 1 or 2'); end
   if (Select == 1 & IsObjV == 0), error('ObjV for fitness-based migration needed');end

   if MIGR == 0, return; end
   MigTeil = max(floor(NIND * MIGR), 1);    % Number of individuals to migrate

% Perform migration between subpopulations --> create a matrix for migration
% in every subpopulation from best individuals of the other subpopulations

   % Clear storing matrices
      ChromMigAll = [];
      if IsObjV == 1, ObjVAll = []; end

   % Create matrix with best/uniform individuals of all subpopulations
      for irun = 1:SUBPOP
         % sort ObjV of actual subpopulation
            if Select == 1,              % fitness-based selection
               [Dummy, IndMigSo]=sort(ObjV((irun-1)*NIND+1:irun*NIND));
            else     % if Select == 0    % uniform selection
               [Dummy, IndMigSo]=sort(rand(NIND, 1));
            end
         % take MigTeil (best) individuals, copy individuals and objective values
            IndMigTeil=IndMigSo(1:MigTeil)+(irun-1)*NIND;
            ChromMigAll = [ChromMigAll; Chrom(IndMigTeil,:)];
            if IsObjV == 1, ObjVAll = [ObjVAll; ObjV(IndMigTeil,:)]; end
      end

   % perform migration
      for irun = 1:SUBPOP
            ChromMig = ChromMigAll;
            if IsObjV == 1, ObjVMig = ObjVAll; end
            if Structure == 1,       % neighbourhood 
               % select individuals of neighbourhood subpopulations for ChromMig and ObjVMig
               popnum = [SUBPOP 1:SUBPOP 1];
               ins1 = popnum(irun); ins2 = popnum(irun + 2);
               InsRows = [(ins1-1)*MigTeil+1:ins1*MigTeil (ins2-1)*MigTeil+1:ins2*MigTeil];
               ChromMig = ChromMig(InsRows,:);
               if IsObjV == 1, ObjVMig = ObjVMig(InsRows,:); end
            elseif Structure == 2,   % ring
               % select individuals of actual-1 subpopulation for ChromMig and ObjVMig
               popnum = [SUBPOP 1:SUBPOP 1];
               ins1 = popnum(irun);
               InsRows = (ins1-1)*MigTeil+1:ins1*MigTeil;
               ChromMig = ChromMig(InsRows,:);
               if IsObjV == 1, ObjVMig = ObjVMig(InsRows,:); end
            else                     % if Structure == 0,  % complete net
               % delete individuals of actual subpopulation from ChromMig and ObjVMig
               DelRows = (irun-1)*MigTeil+1:irun*MigTeil;
               ChromMig(DelRows,:) = [];
               if IsObjV == 1, ObjVMig(DelRows,:) = []; end
            end
         % Create an index from a sorted vector with random numbers   
            [Dummy,IndMigRa]=sort(rand(size(ChromMig,1),1));
         % Take MigTeil numbers from the random vector
            IndMigN=IndMigRa((1:MigTeil)');
         % copy MigTeil individuals into Chrom and ObjV
            Chrom((1:MigTeil)+(irun-1)*NIND,:) = ChromMig(IndMigN,:);
            if IsObjV == 1, ObjV((1:MigTeil)+(irun-1)*NIND,:) = ObjVMig(IndMigN,:); end
      end


% End of function

````

</details>

#### MUT · MATLAB · fbe0a1f2

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `mut`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`f5deb82096f3db334fb30159caacc236ae351eeb99cac69a4b214ed2f88d4d80`
- 语言：MATLAB
- 符号：`mut`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MUT.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/CRTBASE.M`

<details>
<summary>展开原始代码</summary>

````matlab
% MUT.m
%
% This function takes the representation of the current population,
% mutates each element with given probability and returns the resulting
% population.
%
% Syntax:	NewChrom = mut(OldChrom,Pm,BaseV)
%
% Input parameters:
%
%		OldChrom - A matrix containing the chromosomes of the
%			   current population. Each row corresponds to
%			   an individuals string representation.
%
%		Pm	 - Mutation probability (scalar). Default value
%			   of Pm = 0.7/Lind, where Lind is the chromosome
%			   length is assumed if omitted.
%
%		BaseV	 - Optional row vector of the same length as the
%			   chromosome structure defining the base of the 
%			   individual elements of the chromosome. Binary
%			   representation is assumed if omitted.
%
% Output parameter:
%
%		NewChrom - A Matrix containing a mutated version of
%			   OldChrom.
%

% Author: Andrew Chipperfield
% Date: 25-Jan-94

function NewChrom = mut(OldChrom,Pm,BaseV)

% get population size (Nind) and chromosome length (Lind)
[Nind, Lind] = size(OldChrom) ;

% check input parameters
if nargin < 2, Pm = 0.7/Lind ; end
if isnan(Pm), Pm = 0.7/Lind; end

if (nargin < 3), BaseV = crtbase(Lind);  end
if (isnan(BaseV)), BaseV = crtbase(Lind);  end
if (isempty(BaseV)), BaseV = crtbase(Lind);  end

if (nargin == 3) & (Lind ~= length(BaseV))
   error('OldChrom and BaseV are incompatible'), end

% create mutation mask matrix
BaseM = BaseV(ones(Nind,1),:) ;

% perform mutation on chromosome structure
NewChrom = rem(OldChrom+(rand(Nind,Lind)<Pm).*ceil(rand(Nind,Lind).*(BaseM-1)),BaseM);

````

</details>

#### MUTATE · MATLAB · 8e13e3af

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `mutate`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`86b6af2d4a9120aee7f8995d4f609b62cd22e5aecd90ea3e7d60a69cf3c19c8b`
- 语言：MATLAB
- 符号：`mutate`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MUTATE.M`

<details>
<summary>展开原始代码</summary>

````matlab
% MUTATE.M       (MUTATion high-level function)
%
% This function takes a matrix OldChrom containing the 
% representation of the individuals in the current population,
% mutates the individuals and returns the resulting population.
%
% The function handles multiple populations and calls the low-level
% mutation function for the actual mutation process.
%
% Syntax:  NewChrom = mutate(MUT_F, OldChrom, FieldDR, MutOpt, SUBPOP)
%
% Input parameter:
%    MUT_F     - String containing the name of the mutation function
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual.
%    FieldDR   - Matrix describing the boundaries of each variable 
%                (real-values) or defining the base of the variables of 
%                each individual (discrete values).
%                optional for (binary) discrete values
%    MutOpt    - (optional) Vector containing mutation rate and shrink value
%                if omitted or NaN, MutOpt = NaN is assumed
%                MutOpt(1): MutR - number containing the mutation rate -
%                           probability for mutation of a variable
%                MutOpt(2): MutShrink - (optional) number for shrinking the
%                           mutation range in the range [0, 1], possibility to
%                           shrink the range of the mutation depending on,
%                           for instance actual generation (only for
%                           real-values).
%    SUBPOP    - (optional) Number of subpopulations
%                if omitted or NaN, 1 subpopulation is assumed
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mutation in the same format as OldChrom.

% Author:     Hartmut Pohlheim
% History:    19.03.94     file created

function NewChrom = mutate(MUT_F, OldChrom, FieldDR, MutOpt, SUBPOP);

% Check parameter consistency
   if nargin < 2,  error('Not enough input parameter'); end

   % Identify the population size (Nind) and the number of variables (Nvar)
   [Nind,Nvar] = size(OldChrom);

   if nargin < 3, IsDiscret = 1; FieldDR = [];
   elseif isempty(FieldDR), IsDiscret = 1; FieldDR = [];
   elseif isnan(FieldDR), IsDiscret = 1; FieldDR = [];
   else 
      [mF, nF] = size(FieldDR);
      if nF ~= Nvar, error('FieldDR and OldChrom disagree'); end
      if mF == 2, IsDiscret = 0;
      elseif mF == 1, IsDiscret = 1;
      else error('FieldDR must be a matrix with 1 or 2 rows'); end
   end

   if nargin < 4, MutOpt = NaN; end

   if nargin < 5, SUBPOP = 1;
   elseif nargin > 4,
      if isempty(SUBPOP), SUBPOP = 1;
      elseif isnan(SUBPOP), SUBPOP = 1;
      elseif length(SUBPOP) ~= 1, error('SUBPOP must be a scalar'); end
   end

   if (Nind/SUBPOP) ~= fix(Nind/SUBPOP), error('OldChrom and SUBPOP disagree'); end
   Nind = Nind/SUBPOP;  % Compute number of individuals per subpopulation

% Select individuals of one subpopulation and call low level function
   NewChrom = [];
   for irun = 1:SUBPOP,
      ChromSub = OldChrom((irun-1)*Nind+1:irun*Nind,:);  
      if IsDiscret == 1, NewChromSub = feval(MUT_F, ChromSub, MutOpt, FieldDR);
      elseif IsDiscret == 0, NewChromSub = feval(MUT_F, ChromSub, FieldDR, MutOpt); end
      NewChrom=[NewChrom; NewChromSub];
   end


% End of function


````

</details>

#### OBJFUN1 · MATLAB · 3baac127

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `objfun1`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`95863e65c0113af3f1400e6d4fbb0c3d376e840e9330202a38bf19551bb6ea9e`
- 语言：MATLAB
- 符号：`objfun1`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/OBJFUN1.M`

<details>
<summary>展开原始代码</summary>

````matlab
% OBJFUN1.M      (OBJective function for De Jong's FUNction 1)
%
% This function implements the De Jong function 1.
%
% Syntax:  ObjVal = objfun1(Chrom,switch)
%
% Input parameters:
%    Chrom     - Matrix containing the chromosomes of the current
%                population. Each row corresponds to one individual's
%                string representation.
%                if Chrom == [], then special values will be returned
%    switch    - if Chrom == [] and
%                switch == 1 (or []) return boundaries
%                switch == 2 return title
%                switch == 3 return value of global minimum
%
% Output parameters:
%    ObjVal    - Column vector containing the objective values of the
%                individuals in the current population.
%                if called with Chrom == [], then ObjVal contains
%                switch == 1, matrix with the boundaries of the function
%                switch == 2, text for the title of the graphic output
%                switch == 3, value of global minimum
%                

% Author:     Hartmut Pohlheim
% History:    26.11.93     file created
%             27.11.93     text of title and switch added
%             30.11.93     show Dim in figure title
%             16.12.93     switch == 3, return value of global minimum
%             01.03.94     name changed in obj*

function ObjVal = objfun1(Chrom,switch);

% Dimension of objective function
   Dim = 20;
   
% Compute population parameters
   [Nind,Nvar] = size(Chrom);

% Check size of Chrom and do the appropriate thing
   % if Chrom is [], then define size of boundary-matrix and values
   if Nind == 0
      % return text of title for graphic output
      if switch == 2
         ObjVal = ['DE JONG function 1-' int2str(Dim)];
      % return value of global minimum
      elseif switch == 3
         ObjVal = 0;
      % define size of boundary-matrix and values
      else   
         % lower and upper bound, identical for all n variables        
         ObjVal = 100*[-5.12; 5.12];
         ObjVal = ObjVal(1:2,ones(Dim,1));
      end
   % if Dim variables, compute values of function
   elseif Nvar == Dim
      % function 1, sum of xi^2 for i = 1:Dim (Dim=30)
      % n = Dim, -5.12 <= xi <= 5.12
      % global minimum at (xi)=(0) ; fmin=0
      ObjVal = sum((Chrom .* Chrom)')';
      % ObjVal = diag(Chrom * Chrom');  % both lines produce the same
   % otherwise error, wrong format of Chrom
   else
      error('size of matrix Chrom is not correct for function evaluation');
   end   


% End of function


````

</details>

#### OBJHARV · MATLAB · bba67b0c

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `objharv`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`a6208b888f3af5f91cd4717815f2702f3eba5edc0e9ef1fd36a98ae33d1ea36f`
- 语言：MATLAB
- 符号：`objharv`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/OBJHARV.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% OBJHARV.M      (OBJective function for HARVest problem)
%
% This function implements the HARVEST PROBLEM.
%
% Syntax:  ObjVal = objharv(Chrom,switch)
%
% Input parameters:
%    Chrom     - Matrix containing the chromosomes of the current
%                population. Each row corresponds to one individual's
%                string representation.
%                if Chrom == [], then special values will be returned
%    switch    - if Chrom == [] and
%                switch == 1 (or []) return boundaries
%                switch == 2 return title
%                switch == 3 return value of global minimum
%
% Output parameters:
%    ObjVal    - Column vector containing the objective values of the
%                individuals in the current population.
%                if called with Chrom == [], then ObjVal contains
%                switch == 1, matrix with the boundaries of the function
%                switch == 2, text for the title of the graphic output
%                switch == 3, value of global minimum
%                

% Author:     Hartmut Pohlheim
% History:    18.02.94     file created (copy of vallinq.m)
%             01.03.94     name changed in obj*

function ObjVal = objharv(Chrom,switch);

% global gen;

% Dimension of objective function
   Dim = 20;

% values from MICHALEWICZ
   a = 1.1;
   x0 = 100;
   xend = x0;
   XENDWEIGHT = 0.4/(Dim^0.6);
   
% Compute population parameters
   [Nind,Nvar] = size(Chrom);

% Check size of Chrom and do the appropriate thing
   % if Chrom is [], then define size of boundary-matrix and values
   if Nind == 0
      % return text of title for graphic output
      if switch == 2
         ObjVal = ['HARVEST PROBLEM-' int2str(Dim)];
      % return value of global minimum
      elseif switch == 3
         ObjVal = -sqrt(x0*(a^Dim-1)^2/(a^(Dim-1)*(a-1)));
      % define size of boundary-matrix and values
      else   
         % lower and upper bound, identical for all n variables        
         ObjVal1 = [0; 10*Dim];
         ObjVal = rep(ObjVal1,[1 Dim]);
      end
   % if Dim variables, compute values of function
   elseif Nvar == Dim
      ObjVal = zeros(Nind,1);
      X = rep(x0,[Nind 1]);
      for irun = 1:Nvar,
         X = a*X - Chrom(:,irun);
      end
      X;
      ObjVal = -(sum(sqrt(Chrom)')' - XENDWEIGHT * abs(X-x0));
   % otherwise error, wrong format of Chrom
   else
      error('size of matrix Chrom is not correct for function evaluation');
   end   


% End of function


````

</details>

#### ObjFun · MATLAB · bc1e696d

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`d0e1542010e4a3edff199a36fb2503d7b8d17aedb4e117e2bb6f38424f350204`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/ObjFun.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/FCMfun.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Jb,center,U]=ObjFun(X,cn,V,options);
%% 计算种群中每个个体的目标值
% 输入
%        X：样本数据
%       cn：聚类数
%        V：所有的初始聚类中心矩阵
%  options：设置幂指数，最大迭代次数，目标函数的终止容限
% 输出
%    Jb：各个体的目标输出
% center：优化后的各个体的聚类中心
%      U：各样本的相似分类矩阵
[sizepop,m]=size(V);
ch=m/cn;
Jb=zeros(sizepop,1);
center=cell(sizepop,1);
U=cell(sizepop,1);
for i=1:sizepop
    v=reshape(V(i,:),cn,ch);
    [Jb(i),center{i},U{i}]=FCMfun(X,cn,v,options);
end
````

</details>

#### RECDIS · MATLAB · e4132e45

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `recdis`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`3509a126379548e879abb7f9eec4abb67786958f23516a46bc0ea71a44354d0d`
- 语言：MATLAB
- 符号：`recdis`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RECDIS.M`

<details>
<summary>展开原始代码</summary>

````matlab
% RECDIS.M       (RECombination DIScrete)
%
% This function performs discret recombination between pairs of individuals
% and returns the new individuals after mating.
%
% Syntax:  NewChrom = recdis(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%                (in any form, not necessarily real-values).
%    XOVR      - Probability of recombination occurring between pairs
%                of individuals. (not used, only for compatibility)
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mating, ready to be mutated and/or evaluated,
%                in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   23.11.93     file created
%             24.11.93     style improved
%             06.12.93     change of name of function
%             25.02.94     clean up
%             19.03.94     multipopulation support removed

function NewChrom = recdis(OldChrom, XOVR);

% Identify the population size (Nind) and the number of variables (Nvar)
   [Nind,Nvar] = size(OldChrom);

% Identify the number of matings
   Xops = floor(Nind/2);

% which parent gives the value
   Mask1 = (rand(Xops,Nvar)<0.5);
   Mask2 = (rand(Xops,Nvar)<0.5);

% Performs crossover
   odd = 1:2:Nind-1;
   even= 2:2:Nind;
   NewChrom(odd,:)  = (OldChrom(odd,:).* Mask1) + (OldChrom(even,:).*(~Mask1));
   NewChrom(even,:) = (OldChrom(odd,:).* Mask2) + (OldChrom(even,:).*(~Mask2));

% If the number of individuals is odd, the last individual cannot be mated
% but must be included in the new population
   if rem(Nind,2),  NewChrom(Nind,:)=OldChrom(Nind,:); end


% End of function


````

</details>

#### RECINT · MATLAB · 4a5e81d5

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `recint`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`f28039ff4addb00e9527bb5c81eb6c73fdf542b9ebe15a9b929cca771cf5cd0b`
- 语言：MATLAB
- 符号：`recint`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RECINT.M`

<details>
<summary>展开原始代码</summary>

````matlab
% RECINT.M       (RECombination extended INTermediate)
%
% This function performs extended intermediate recombination between
% pairs of individuals and returns the new individuals after mating.
%
% Syntax:  NewChrom = recint(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one
%                individual
%    XOVR      - Probability of crossover occurring between pairs
%                of individuals. (not used, only for compatibility)
%
% Output parameter:
%    NewChrom - Matrix containing the chromosomes of the population
%               after mating, ready to be mutated and/or evaluated,
%               in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   25.11.93     file created
%             06.12.93     change of name of function
%             25.02.94     clean up
%             19.03.94     multipopulation support removed

function NewChrom = recint(OldChrom, XOVR);

% Identify the population size (Nind) and the number of variables (Nvar)
   [Nind,Nvar] = size(OldChrom);

% Identify the number of matings
   Xops = floor(Nind/2);

% Performs recombination
   odd = 1:2:Nind-1;
   even= 2:2:Nind;

   % position of value of offspring compared to parents
   Alpha = -0.25 + 1.5 * rand(Xops,Nvar);

   % recombination
   NewChrom(odd,:)  = OldChrom(odd,:) + Alpha .* (OldChrom(even,:) - OldChrom(odd,:));

   % the same ones more for second half of offspring
   Alpha = -0.25 + 1.5 * rand(Xops,Nvar);
   NewChrom(even,:) = OldChrom(odd,:) + Alpha .* (OldChrom(even,:) - OldChrom(odd,:));

% If the number of individuals is odd, the last individual cannot be mated
% but must be included in the new population
   if rem(Nind,2),  NewChrom(Nind,:)=OldChrom(Nind,:); end


% End of function


````

</details>

#### RECLIN · MATLAB · 0446e95b

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `reclin`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`34f0a46f19e514e77b173b8841a91e686cef0a5f864c3dff6725cb4ab59ff861`
- 语言：MATLAB
- 符号：`reclin`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RECLIN.M`

<details>
<summary>展开原始代码</summary>

````matlab
% RECLIN.M       (RECombination extended LINe)
%
% This function performs extended line recombination between
% pairs of individuals and returns the new individuals after mating.
%
% Syntax:  NewChrom = reclin(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one
%                individual
%    XOVR      - Probability of crossover occurring between pairs
%                of individuals. (not used, only for compatibility)
%
% Output parameter:
%    NewChrom - Matrix containing the chromosomes of the population
%               after mating, ready to be mutated and/or evaluated,
%               in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   26.11.93     file created
%             06.12.93     change of name of function
%             25.02.94     clean up
%             19.03.94     multipopulation support removed

function NewChrom = reclin(OldChrom, XOVR);

% Identify the population size (Nind) and the number of variables (Nvar)
   [Nind,Nvar] = size(OldChrom);

% Identify the number of matings
   Xops = floor(Nind/2);

% Performs recombination
   odd = 1:2:Nind-1;
   even= 2:2:Nind;

   % position of value of offspring compared to parents
   Alpha = -0.25 + 1.5 * rand(Xops,1);
   Alpha = Alpha(1:Xops,ones(Nvar,1));

   % recombination
   NewChrom(odd,:)  = OldChrom(odd,:) + Alpha .* (OldChrom(even,:) - OldChrom(odd,:));

   % the same ones more for second half of offspring
   Alpha = -0.25 + 1.5 * rand(Xops,1);
   Alpha = Alpha(1:Xops,ones(Nvar,1));
   NewChrom(even,:) = OldChrom(odd,:) + Alpha .* (OldChrom(even,:) - OldChrom(odd,:));

% If the number of individuals is odd, the last individual cannot be mated
% but must be included in the new population
   if rem(Nind,2),  NewChrom(Nind,:)=OldChrom(Nind,:); end


% End of function


````

</details>

#### RECMUT · MATLAB · 4658571f

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `recmut`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`1dba80855d9d825d038f939d30b7cddb249dc460ae0b449d0cf6cb9f6a4bc738`
- 语言：MATLAB
- 符号：`recmut`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RECMUT.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% RECLIN.M       (line RECombination with MUTation features)
%
% This function performs line recombination with mutation features between
% pairs of individuals and returns the new individuals after mating.
%
% Syntax:  NewChrom = recmut(OldChrom, FieldDR, MutOpt)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%    FieldDR   - Matrix describing the boundaries of each variable.
%    MutOpt    - (optional) Vector containing recombination rate and shrink value
%                MutOpt(1): MutR - number containing the recombination rate -
%                           probability for recombine a pair of parents
%                           if omitted or NaN, MutOpt(1) = 1 is assumed
%                MutOpt(2): MutShrink - (optional) number for shrinking the
%                           recombination range in the range [0 1], possibility to
%                           shrink the range of the recombination depending on,
%                           for instance actual generation.
%                           if omitted or NaN, MutOpt(2) = 1 is assumed
%
% Output parameter:
%    NewChrom - Matrix containing the chromosomes of the population
%               after mating, ready to be mutated and/or evaluated,
%               in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   27.03.94     file created

function NewChrom = recmut(OldChrom, FieldDR, MutOpt);

% Check parameter consistency
   if nargin < 2,  error('Not enough input parameter'); end

   % Identify the population size (Nind) and the number of variables (Nvar)
   [Nind,Nvar] = size(OldChrom);

   [mF, nF] = size(FieldDR);
   if mF ~= 2, error('FieldDR must be a matrix with 2 rows'); end
   if Nvar ~= nF, error('FieldDR and OldChrom disagree'); end

   if nargin < 3, MutR = 1; MutShrink = 1;
   elseif isempty(MutOpt), MutR = 1; MutShrink = 1;
   elseif isnan(MutOpt), MutR = 1; MutShrink = 1;
   else   
      if length(MutOpt) == 1, MutR = MutOpt; MutShrink = 1;
      elseif length(MutOpt) == 2, MutR = MutOpt(1); MutShrink = MutOpt(2);
      else, error(' Too many parameter in MutOpt'); end
   end

   if isempty(MutR), MutR = 1;
   elseif isnan(MutR), MutR = 1;
   elseif length(MutR) ~= 1, error('Parameter for recombination rate must be a scalar');
   elseif (MutR < 0 | MutR > 1), error('Parameter for recombination rate must be a scalar in [0, 1]'); end

   if isempty(MutShrink), MutShrink = 1;
   elseif isnan(MutShrink), MutShrink = 1;
   elseif length(MutShrink) ~= 1, error('Parameter for shrinking recombination range must be a scalar');
   elseif (MutShrink < 0 | MutShrink > 1), 
      error('Parameter for shrinking recombination range must be a scalar in [0, 1]');
   end

% Identify the number of matings
   Xops = floor(Nind/2);

% NewChrom = OldChrom (+ or -) * Range * MutShrink * Delta * ChromDiff
% - with probability 0.9, + with probability 0.1
% Range = 0.5 * (upperbound - lowerbound), given by FieldDR
% Delta = Sum(Alpha_i * 2^-i) from 0 to ACCUR; Alpha_i = rand(ACCUR,1) < 1/ACCUR
% ChromDiff = (individual1 - individual2) / Distance between individuals 

% Matrix with range values for every variable
   Range = rep(0.5 * MutShrink *(FieldDR(2,:)-FieldDR(1,:)),[Xops 1]);

% zeros and ones for recombine or not this variable, together with Range
   if MutR < 1, Range = Range .* rep((rand(Xops,1) < MutR), [1 Nvar]); end

% compute, if + or - sign 
   Range = Range .* (1 - 2 * (rand(Xops,Nvar) < 0.9));

% compute distance between mating pairs
   NormO = zeros(Xops,1);
   for irun = 1:Xops,
      NormO(irun) = max(realmin,abs(norm(OldChrom(2*irun,:)) - norm(OldChrom(2*irun-1,:))));
   end

% compute difference between variables divided by distance
   ChromDiff = zeros(Xops,Nvar);
   for irun = 1:Xops
      ChromDiff(irun,:) = diff([OldChrom(2*irun-1,:); OldChrom(2*irun,:)]) / NormO(irun);
   end

% compute delta value for all individuals
   ACCUR = 20;
   Vect = 2 .^ (-(0:(ACCUR-1))');
   Delta = (rand(Xops,ACCUR) < 1/ACCUR) * Vect;
   Delta = rep(Delta, [1 Nvar]);

% Performs recombination
   odd = 1:2:Nind-1;
   even= 2:2:Nind;

   % recombination
   NewChrom(odd,:)  = OldChrom(odd,:) + Range .* Delta .* (ChromDiff);
   NewChrom(even,:)  = OldChrom(even,:) + Range .* Delta .* (-ChromDiff);

% If the number of individuals is odd, the last individual cannot be mated
% but must be included in the new population
   if rem(Nind,2),  NewChrom(Nind,:)=OldChrom(Nind,:); end

% Ensure variables boundaries, compare with lower and upper boundaries
   NewChrom = max(rep(FieldDR(1,:),[Nind 1]), NewChrom);
   NewChrom = min(rep(FieldDR(2,:),[Nind 1]), NewChrom);


% End of function


````

</details>

#### RECOMBIN · MATLAB · 0a551532

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `recombin`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1beb08befa03089753f61e6daa8117587823cc59d2e0949e5f78fc4cfa2db767`
- 语言：MATLAB
- 符号：`recombin`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RECOMBIN.M`

<details>
<summary>展开原始代码</summary>

````matlab
% RECOMBIN.M       (RECOMBINation high-level function)
%
% This function performs recombination between pairs of individuals
% and returns the new individuals after mating. The function handles
% multiple populations and calls the low-level recombination function
% for the actual recombination process.
%
% Syntax:  NewChrom = recombin(REC_F, OldChrom, RecOpt, SUBPOP)
%
% Input parameters:
%    REC_F     - String containing the name of the recombination or
%                crossover function
%    Chrom     - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%    RecOpt    - (optional) Scalar containing the probability of 
%                recombination/crossover occurring between pairs
%                of individuals.
%                if omitted or NaN, 1 is assumed
%    SUBPOP    - (optional) Number of subpopulations
%                if omitted or NaN, 1 subpopulation is assumed
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after recombination in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   18.03.94     file created


function NewChrom = recombin(REC_F, Chrom, RecOpt, SUBPOP);


% Check parameter consistency
   if nargin < 2, error('Not enough input parameter'); end

   % Identify the population size (Nind)
   [Nind,Nvar] = size(Chrom);
 
   if nargin < 4, SUBPOP = 1; end
   if nargin > 3,
      if isempty(SUBPOP), SUBPOP = 1;
      elseif isnan(SUBPOP), SUBPOP = 1;
      elseif length(SUBPOP) ~= 1, error('SUBPOP must be a scalar'); end
   end

   if (Nind/SUBPOP) ~= fix(Nind/SUBPOP), error('Chrom and SUBPOP disagree'); end
   Nind = Nind/SUBPOP;  % Compute number of individuals per subpopulation

   if nargin < 3, RecOpt = 0.7; end
   if nargin > 2,
      if isempty(RecOpt), RecOpt = 0.7;
      elseif isnan(RecOpt), RecOpt = 0.7;
      elseif length(RecOpt) ~= 1, error('RecOpt must be a scalar');
      elseif (RecOpt < 0 | RecOpt > 1), error('RecOpt must be a scalar in [0, 1]'); end
   end


% Select individuals of one subpopulation and call low level function
   NewChrom = [];
   for irun = 1:SUBPOP,
      ChromSub = Chrom((irun-1)*Nind+1:irun*Nind,:);  
      NewChromSub = feval(REC_F, ChromSub, RecOpt);
      NewChrom=[NewChrom; NewChromSub];
   end


% End of function


````

</details>

#### REP · MATLAB · 3e212994

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `rep`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`78ec47d1d557452415eae600d8b8bfb01621fc1a319e1f8c8e62d45b887ef7c7`
- 语言：MATLAB
- 符号：`rep`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% REP.m         Replicate a matrix
%
% This function replicates a matrix in both dimensions. 
%
% Syntax:       MatOut = rep(MatIn,REPN);
%
% Input parameters:
%   MatIn    - Input Matrix (before replicating)
%
%   REPN     - Vector of 2 numbers, how many replications in each dimension
%              REPN(1): replicate vertically
%              REPN(2): replicate horizontally
%
%              Example:
%
%              MatIn = [1 2 3]
%              REPN = [1 2]: MatOut = [1 2 3 1 2 3]
%              REPN = [2 1]: MatOut = [1 2 3;
%                                      1 2 3]
%              REPN = [3 2]: MatOut = [1 2 3 1 2 3;
%                                      1 2 3 1 2 3;
%                                      1 2 3 1 2 3]
%
% Output parameter:
%   MatOut   - Output Matrix (after replicating)
%

% Author:   Carlos Fonseca & Hartmut Pohlheim
% History:  14.02.94        file created


function MatOut = rep(MatIn,REPN)

% Get size of input matrix
   [N_D,N_L] = size(MatIn);

% Calculate
   Ind_D = rem(0:REPN(1)*N_D-1,N_D) + 1;
   Ind_L = rem(0:REPN(2)*N_L-1,N_L) + 1;

% Create output matrix
   MatOut = MatIn(Ind_D,Ind_L);


% End of function

````

</details>

#### RESPLOT · MATLAB · 5db15243

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `resplot`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f1c65ba1bd79521d9bd0ce65a2a5381bed89e3e767071ca11c95dd781c637622`
- 语言：MATLAB
- 符号：`resplot`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RESPLOT.M`

<details>
<summary>展开原始代码</summary>

````matlab
% RESPLOT.M       (RESult PLOTing)
%
% This function plots some results during computation.
%
% Syntax:  resplot(Chrom,IndAll,ObjV,Best,gen)
%
% Input parameters:
%    Chrom     - Matrix containing the chromosomes of the current
%                population. Each line corresponds to one individual.
%    IndAll    - Matrix containing the best individual (variables) of each
%                generation. Each line corresponds to one individual.
%    ObjV      - Vector containing objective values of the current
%                generation
%    Best      - Matrix containing the best and average Objective values of 
%                each generation, [best value per generation,average value 
%                per generation]
%    gen       - Scalar containing the number of the current generation
%
% Output parameter:
%    no output parameter

%  Author:    Hartmut Pohlheim
%  History:   27.11.93     file created
%             29.11.93     decision, if plot or not deleted
%                          yscale not log
%             15.12.93     MutMatrix as parameter and plot added
%             16.03.94     function cleaned, MutMatrix removed, IndAll added

function resplot(Chrom,IndAll,ObjV,Best,gen);

   % plot of best and mean value per generation
      subplot(2,2,1), plot(Best);
      title('Best and mean objective value');
      xlabel('generation'), ylabel('objective value');

   % plot of best individuals in all generations
      subplot(2,2,2), plot(IndAll);
      title(['Best individuals']);
      xlabel('generation'), ylabel('value of variable');

   % plot of variables of all individuals in current generation
      subplot(2,2,3), plot(Chrom');
      title(['All individuals in gen ',num2str(gen)]);
      xlabel('number of variable'), ylabel('value of variable');

   % plot of all objective values in current generation
      subplot(2,2,4), plot(ObjV,'y.');
      title(['All objective values']);
      xlabel('number of individual'), ylabel('objective value');

   drawnow;


% End of function


````

</details>

#### RWS · MATLAB · 74f6015d

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `rws`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`1b6fe643ae24bb2a32e135ec0f2d88a2b0b62fa7261b19b427315020161ce7e2`
- 语言：MATLAB
- 符号：`rws`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RWS.M`

<details>
<summary>展开原始代码</summary>

````matlab
% RWS.m - Roulette Wheel Selection
%
%       Syntax:
%               NewChrIx = rws(FitnV, Nsel)
%
%       This function selects a given number of individuals Nsel from a
%       population. FitnV is a column vector containing the fitness
%       values of the individuals in the population.
%
%       The function returns another column vector containing the
%       indexes of the new generation of chromosomes relative to the
%       original population matrix, shuffled. The new population, ready
%       for mating, can be obtained by calculating
%       OldChrom(NewChrIx, :).

% Author: Carlos Fonseca, 	Updated: Andrew Chipperfield
% Date: 04/10/93,		Date: 27-Jan-94

function NewChrIx = rws(FitnV,Nsel);

% Identify the population size (Nind)
[Nind,ans] = size(FitnV);

% Perform Stochastic Sampling with Replacement
cumfit  = cumsum(FitnV);
trials = cumfit(Nind) .* rand(Nsel, 1);
Mf = cumfit(:, ones(1, Nsel));
Mt = trials(:, ones(1, Nind))';
[NewChrIx, ans] = find(Mt < Mf & ...
                        [ zeros(1, Nsel); Mf(1:Nind-1, :) ] <= Mt);

````

</details>

#### SELECT · MATLAB · dd4a889b

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `select`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`93e9c1b839da6ecb637ea9004d21115ecb1084036ee1372172393ad8da6588be`
- 语言：MATLAB
- 符号：`select`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/SELECT.M`

<details>
<summary>展开原始代码</summary>

````matlab
% SELECT.M          (universal SELECTion)
%
% This function performs universal selection. The function handles
% multiple populations and calls the low level selection function
% for the actual selection process.

%
% Syntax:  SelCh = select(SEL_F, Chrom, FitnV, GGAP, SUBPOP)
%
% Input parameters:
%    SEL_F     - Name of the selection function
%    Chrom     - Matrix containing the individuals (parents) of the current
%                population. Each row corresponds to one individual.
%    FitnV     - Column vector containing the fitness values of the
%                individuals in the population.
%    GGAP      - (optional) Rate of individuals to be selected
%                if omitted 1.0 is assumed
%    SUBPOP    - (optional) Number of subpopulations
%                if omitted 1 subpopulation is assumed
%
% Output parameters:
%    SelCh     - Matrix containing the selected individuals.

% Author:     Hartmut Pohlheim
% History:    10.03.94     file created

function SelCh = select(SEL_F, Chrom, FitnV, GGAP, SUBPOP);

% Check parameter consistency
   if nargin < 3, error('Not enough input parameter'); end

   % Identify the population size (Nind)
   [NindCh,Nvar] = size(Chrom);
   [NindF,VarF] = size(FitnV);
   if NindCh ~= NindF, error('Chrom and FitnV disagree'); end
   if VarF ~= 1, error('FitnV must be a column vector'); end
  
   if nargin < 5, SUBPOP = 1; end
   if nargin > 4,
      if isempty(SUBPOP), SUBPOP = 1;
      elseif isnan(SUBPOP), SUBPOP = 1;
      elseif length(SUBPOP) ~= 1, error('SUBPOP must be a scalar'); end
   end

   if (NindCh/SUBPOP) ~= fix(NindCh/SUBPOP), error('Chrom and SUBPOP disagree'); end
   Nind = NindCh/SUBPOP;  % Compute number of individuals per subpopulation

   if nargin < 4, GGAP = 1; end
   if nargin > 3,
      if isempty(GGAP), GGAP = 1;
      elseif isnan(GGAP), GGAP = 1;
      elseif length(GGAP) ~= 1, error('GGAP must be a scalar');
      elseif (GGAP < 0), error('GGAP must be a scalar bigger than 0'); end
   end

% Compute number of new individuals (to select)
   NSel=max(floor(Nind*GGAP+.5),2);

% Select individuals from population
   SelCh = [];
   for irun = 1:SUBPOP,
      FitnVSub = FitnV((irun-1)*Nind+1:irun*Nind);
      ChrIx=feval(SEL_F, FitnVSub, NSel)+(irun-1)*Nind;
      SelCh=[SelCh; Chrom(ChrIx,:)];
   end
 

% End of function

````

</details>

#### SUS · MATLAB · a16d618f

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `sus`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`2b10ad5906524d4e218787b0fb5d1f3c52c24cc66dc847d05fd714d0f0b01d9a`
- 语言：MATLAB
- 符号：`sus`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/SUS.M`

<details>
<summary>展开原始代码</summary>

````matlab
% SUS.M          (Stochastic Universal Sampling)
%
% This function performs selection with STOCHASTIC UNIVERSAL SAMPLING.
%
% Syntax:  NewChrIx = sus(FitnV, Nsel)
%
% Input parameters:
%    FitnV     - Column vector containing the fitness values of the
%                individuals in the population.
%    Nsel      - number of individuals to be selected
%
% Output parameters:
%    NewChrIx  - column vector containing the indexes of the selected
%                individuals relative to the original population, shuffled.
%                The new population, ready for mating, can be obtained
%                by calculating OldChrom(NewChrIx,:).

% Author:     Hartmut Pohlheim (Carlos Fonseca)
% History:    12.12.93     file created
%             22.02.94     clean up, comments


function NewChrIx = sus(FitnV,Nsel);

% Identify the population size (Nind)
   [Nind,ans] = size(FitnV);

% Perform stochastic universal sampling
   cumfit = cumsum(FitnV);
   trials = cumfit(Nind) / Nsel * (rand + (0:Nsel-1)');
   Mf = cumfit(:, ones(1, Nsel));
   Mt = trials(:, ones(1, Nind))';
   [NewChrIx, ans] = find(Mt < Mf & [ zeros(1, Nsel); Mf(1:Nind-1, :) ] <= Mt);

% Shuffle new population
   [ans, shuf] = sort(rand(Nsel, 1));
   NewChrIx = NewChrIx(shuf);


% End of function

````

</details>

#### XOVDP · MATLAB · bd570fa5

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `xovdp`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`36e7e1f37a0707c6785ec214489d551b56d157f8c2c1227e27f93a880df6c70b`
- 语言：MATLAB
- 符号：`xovdp`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVDP.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVMP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% XOVDP.M        (CROSSOVer Double Point)
%
% This function performs double point crossover between pairs of
% individuals and returns the current generation after mating.
%
% Syntax:  NewChrom = xovdp(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%                (in any form, not necessarily real values).
%    XOVR      - Probability of recombination occurring between pairs
%                of individuals.
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mating, ready to be mutated and/or evaluated,
%                in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   28.03.94     file created

function NewChrom = xovdp(OldChrom, XOVR);

if nargin < 2, XOVR = NaN; end

% call low level function with appropriate parameters
   NewChrom = xovmp(OldChrom, XOVR, 2, 0);


% End of function

````

</details>

#### 相似实现组 · MATLAB · 6cef1cb9

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：3
- 原始来源文件：3
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：XOVDPRS.M

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `xovdprs`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`9e38f004605377c6c745681434ae98682be231ea910b71894507753f334c8e54`
- 语言：MATLAB
- 符号：`xovdprs`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVDPRS.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVMP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% XOVDPRS.M      (CROSSOVer Double-Point with Reduced Surrogate)
%
% This function performs double-point 'reduced surrogate' crossover between 
% pairs of individuals and returns the current generation after mating.
%
% Syntax:  NewChrom = xovdprs(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%                (in any form, not necessarily real values).
%    XOVR      - Probability of recombination occurring between pairs
%                of individuals.
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mating, ready to be mutated and/or evaluated,
%                in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   28.03.94     file created

function NewChrom = xovdprs(OldChrom, XOVR);

if nargin < 2, XOVR = NaN; end

% call low-level function with appropriate parameters
   NewChrom = xovmp(OldChrom, XOVR, 2, 1);


% End of function

````

</details>

##### 变体 2：XOVSH.M

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `xovsh`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`fba081244535a69f8765c25d7dc572af5fdc23be033333c847981673ec02a2a4`
- 语言：MATLAB
- 符号：`xovsh`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVSH.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVMP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% XOVSH.M        (CROSSOVer SHuffle)
%
% This function performs shuffle crossover between pairs of
% individuals and returns the current generation after mating.
%
% Syntax:  NewChrom = xovsh(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%                (in any form, not necessarily real values).
%    XOVR      - Probability of recombination occurring between pairs
%                of individuals.
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mating, ready to be mutated and/or evaluated,
%                in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   28.03.94     file created

function NewChrom = xovsh(OldChrom, XOVR);

if nargin < 2, XOVR = NaN; end

% call low level function with appropriate parameters
   NewChrom = xovmp(OldChrom, XOVR, 0, 0);


% End of function

````

</details>

##### 变体 3：XOVSPRS.M

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `xovsprs`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`1fd4438f59f1e79d28ca7949a48dd466fc29300d0a969728af9657bea8809c26`
- 语言：MATLAB
- 符号：`xovsprs`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVSPRS.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVMP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% XOVSPRS.M      (CROSSOVer Single-Point with Reduced Surrogate)
%
% This function performs single-point 'reduced surrogate' crossover between 
% pairs of individuals and returns the current generation after mating.
%
% Syntax:  NewChrom = xovsprs(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%                (in any form, not necessarily real-values).
%    XOVR      - Probability of recombination occurring between pairs
%                of individuals.
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mating, ready to be mutated and/or evaluated,
%                in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   28.03.94     file created

function NewChrom = xovsprs(OldChrom, XOVR);

if nargin < 2, XOVR = NaN; end

% call low-level function with appropriate parameters
   NewChrom = xovmp(OldChrom, XOVR, 1, 1);


% End of function

````

</details>

#### XOVMP · MATLAB · 8fd0524c

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `xovmp`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`492c5255f6c08d5cd3a89d284b09cbbe072271fcb15b44833df2758df7dc7425`
- 语言：MATLAB
- 符号：`xovmp`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVMP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% XOVMP.m                Multi-point crossover
%
%       Syntax: NewChrom =  xovmp(OldChrom, Px, Npt, Rs)
%
%       This function takes a matrix OldChrom containing the binary
%       representation of the individuals in the current population,
%       applies crossover to consecutive pairs of individuals with
%       probability Px and returns the resulting population.
%
%       Npt indicates how many crossover points to use (1 or 2, zero
%       indicates shuffle crossover).
%       Rs indicates whether or not to force the production of
%       offspring different from their parents.
%

% Author: Carlos Fonseca, 	Updated: Andrew Chipperfield
% Date: 28/09/93,		Date: 27-Jan-94

function NewChrom = xovmp(OldChrom, Px, Npt, Rs);

% Identify the population size (Nind) and the chromosome length (Lind)
[Nind,Lind] = size(OldChrom);

if Lind < 2, NewChrom = OldChrom; return; end

if nargin < 4, Rs = 0; end
if nargin < 3, Npt = 0; Rs = 0; end
if nargin < 2, Px = 0.7; Npt = 0; Rs = 0; end
if isnan(Px), Px = 0.7; end
if isnan(Npt), Npt = 0; end
if isnan(Rs), Rs = 0; end
if isempty(Px), Px = 0.7; end
if isempty(Npt), Npt = 0; end
if isempty(Rs), Rs = 0; end

Xops = floor(Nind/2);
DoCross = rand(Xops,1) < Px;
odd = 1:2:Nind-1;
even = 2:2:Nind;

% Compute the effective length of each chromosome pair
Mask = ~Rs | (OldChrom(odd, :) ~= OldChrom(even, :));
Mask = cumsum(Mask')';

% Compute cross sites for each pair of individuals, according to their
% effective length and Px (two equal cross sites mean no crossover)
xsites(:, 1) = Mask(:, Lind);
if Npt >= 2,
        xsites(:, 1) = ceil(xsites(:, 1) .* rand(Xops, 1));
end
xsites(:,2) = rem(xsites + ceil((Mask(:, Lind)-1) .* rand(Xops, 1)) ...
                                .* DoCross - 1 , Mask(:, Lind) )+1;

% Express cross sites in terms of a 0-1 mask
Mask = (xsites(:,ones(1,Lind)) < Mask) == ...
                        (xsites(:,2*ones(1,Lind)) < Mask);

if ~Npt,
        shuff = rand(Lind,Xops);
        [ans,shuff] = sort(shuff);
        for i=1:Xops
          OldChrom(odd(i),:)=OldChrom(odd(i),shuff(:,i));
          OldChrom(even(i),:)=OldChrom(even(i),shuff(:,i));
        end
end

% Perform crossover
NewChrom(odd,:) = (OldChrom(odd,:).* Mask) + (OldChrom(even,:).*(~Mask));
NewChrom(even,:) = (OldChrom(odd,:).*(~Mask)) + (OldChrom(even,:).*Mask);

% If the number of individuals is odd, the last individual cannot be mated
% but must be included in the new population
if rem(Nind,2),
  NewChrom(Nind,:)=OldChrom(Nind,:);
end

if ~Npt,
        [ans,unshuff] = sort(shuff);
        for i=1:Xops
          NewChrom(odd(i),:)=NewChrom(odd(i),unshuff(:,i));
          NewChrom(even(i),:)=NewChrom(even(i),unshuff(:,i));
        end
end

````

</details>

#### 相似实现组 · MATLAB · 37cf1d4f

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：XOVSHRS.M

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `xovshrs`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`05e39153994c1cd4415d9c9412e1f5a2d7298171fdf2501fbd053f3bd3749894`
- 语言：MATLAB
- 符号：`xovshrs`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVSHRS.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVMP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% XOVSHRS.M      (CROSSOVer SHuffle with Reduced Surrogate)
%
% This function performs shuffle 'reduced surrogate' crossover between 
% pairs of individuals and returns the current generation after mating.
%
% Syntax:  NewChrom = xovshrs(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%                (in any form, not necessarily real values).
%    XOVR      - Probability of recombination occurring between pairs
%                of individuals.
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mating, ready to be mutated and/or evaluated,
%                in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   28.03.94     file created

function NewChrom = xovshrs(OldChrom, XOVR);

if nargin < 2, XOVR = NaN; end

% call low level function with appropriate parameters
   NewChrom = xovmp(OldChrom, XOVR, 0, 1);


% End of function

````

</details>

##### 变体 2：XOVSP.M

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `xovsp`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`83492d75f6a1da8f4624cff6a540a7844f89ccdd99d046251a2cf80cae2e2245`
- 语言：MATLAB
- 符号：`xovsp`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVSP.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/XOVMP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% XOVSP.M        (CROSSOVer Single-Point)
%
% This function performs single-point crossover between pairs of 
% individuals and returns the current generation after mating.
%
% Syntax:  NewChrom = xovsp(OldChrom, XOVR)
%
% Input parameters:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual
%                (in any form, not necessarily real values).
%    XOVR      - Probability of recombination occurring between pairs
%                of individuals.
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mating, ready to be mutated and/or evaluated,
%                in the same format as OldChrom.

%  Author:    Hartmut Pohlheim
%  History:   28.03.94     file created

function NewChrom = xovsp(OldChrom, XOVR);

if nargin < 2, XOVR = NaN; end

% call low level function with appropriate parameters
   NewChrom = xovmp(OldChrom, XOVR, 1, 0);


% End of function

````

</details>

#### initFCM · MATLAB · 8bc3f8b7

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `initFCM`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`545f3dfb0fff3fb71a2a974afb8622ed1137ee33af6a735ce9a188e79c5d54e3`
- 语言：MATLAB
- 符号：`initFCM`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/initFCM.m`

<details>
<summary>展开原始代码</summary>

````matlab
function U=initFCM(X,cluster_n,center,b)
%% 初始化相似分类矩阵
% 输入
%        X：样本数据
%cluster_n：聚类数
%   center：初始聚类中心矩阵
%        b：设置幂指数
% 输出
%      U：相似分类矩阵
dist=distfcm(center,X);       % 求出各样本与各聚类中心的距离矩阵
%% 计算新的U矩阵
tmp=dist.^(-2/(b-1));
U=tmp./(ones(cluster_n,1)*sum(tmp));
````

</details>

#### iterateFCM · MATLAB · b9e6d4f8

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5d9cd68bfc54b7d03ee1976360a5745993c1c703025c12ff80229c696e84d8e1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/iterateFCM.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [U_new,center,obj_fcn]=iterateFCM(X,U,cluster_n,b)
%% 迭代
% 输入
%        X：样本数据
%        U：相似分类矩阵
%cluster_n：聚类数
%        b：幂指数
% 输出
%obj_fcn：当前目标输出Jb值
% center：新的的聚类中心
%  U_new：相似分类矩阵
mf=U.^b;       % 指数修正后的mf矩阵
center=mf*X./((ones(size(X,2),1)*sum(mf'))'); % 新的聚类中心
%% 目标值
dist=distfcm(center,X);       % 求出各样本与各聚类中心的距离矩阵
obj_fcn=sum(sum((dist.^2).*mf));  % 目标函数值
%% 计算新的U矩阵
tmp=dist.^(-2/(b-1));
U_new=tmp./(ones(cluster_n,1)*sum(tmp));
````

</details>

#### accept · MATLAB · 95b48ee7

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `accept`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`37f1a15d9220107e0a423c380806ab76821db32cdc10186547b85038388c356a`
- 语言：MATLAB
- 符号：`accept`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/accept.m`

<details>
<summary>展开原始代码</summary>

````matlab
function y=accept(t,df)
y=(df<0)|(((df/t)<88)&(exp(-df/t)>rand(1,1)));
````

</details>

#### annealing · MATLAB · a04a5ed1

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `annealing`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`746a570d02cd07bcd7498d9fa560d3daab38a00c56fca92525c370e1cd725092`
- 语言：MATLAB
- 符号：`annealing`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/annealing.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/accept.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/calculate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/cost_sum.m`

<details>
<summary>展开原始代码</summary>

````matlab
%function R=annealing(N,L,s,t,dt,C,R)
%N为问题规模，即节点个数；L可取较大值，如500、1000；
%s取1、2等；t为初始温度，参考范围为0.5--2；
%dt为衰减因子，一般不小于0.9;
%C为边权矩阵，应是一个强连通图的边权矩阵
%R为初始路径，结果路径也存放在R中
%L、s、t、dt应通过多次试验来确定，以获得优化的结果
%参考《非数值并行算法--模拟退火算法》科学出版社
function R=annealing(N,L,s,t,dt,C,R)
s0=0;
while 1
    a=0;
    for k=1:L
        [r,df]=calculate(R,C,N);
        if accept(t,df)
            R=r;a=1;
            disp(cost_sum(R,C,N));
        end
    end
    t=t*dt
    if a==0
        s0=s0+1;
    else 
        s0=0;
    end
    if s0==s
        break;
    end
end
````

</details>

#### calculate · MATLAB · 1942c55c

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`fbb2b408402373689177973becfcf4bf7e8e3ad6295dbcb8fdbf00af54493d44`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/calculate.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/cost_sum.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/exchange2.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/exchange3.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [r,df]=calculate(R,C,N)
judge=rand(1,1);
if judge<0.5
    r=exchange2(R);
    df=cost_sum(r,C,N)-cost_sum(R,C,N);
else 
    r=exchange3(R);
    df=cost_sum(r,C,N)-cost_sum(R,C,N);
end
````

</details>

#### cost_sum · MATLAB · 0bd5526d

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `cost_sum`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`370bfa87c544488ebce51e97a1102db4a99bd974183fa746d6ca05bb72fdfa65`
- 语言：MATLAB
- 符号：`cost_sum`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/cost_sum.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/三边交换简单算法/cost_sum.m`

<details>
<summary>展开原始代码</summary>

````matlab
function y=cost_sum(x,C,N)
y=0;
for i=1:(N-1)
    y=y+C(x(i),x(i+1));
end
y=y+C(x(N),x(1));
````

</details>

#### exchange2 · MATLAB · d9576a18

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `exchange2`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`c2a77a7d4455114b9155367dff2f79af7f8a0f1d082f9504b9cc9e3bc8cea8a8`
- 语言：MATLAB
- 符号：`exchange2`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/exchange2.m`

<details>
<summary>展开原始代码</summary>

````matlab
function r=exchange2(R)
N=length(R);
I=1+fix(unifrnd(0,N));
J=1+fix(unifrnd(0,N-1));
if I==J
    J=J+1;
end
if J<I
    I=I+J;
    J=I-J;
    I=I-J;
end
r=R;
if J-I~=1&J-I~=N-1
    for p=1:(J-I)
        r(I+p)=R(J-p+1);
    end
end
if J-I==1
    r(I)=R(J);
    r(J)=R(I);
end
if J-I==N-1
    for p=1:(N-2)
        r(p+2)=R(N+1-p)
    end
end
````

</details>

#### exchange3 · MATLAB · 3714ff08

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `exchange3`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`9d2ee0a896ccf5ac1468acd03e0ec30e4aa684bad868c0ab6d7213c42fc9d318`
- 语言：MATLAB
- 符号：`exchange3`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/TSP模拟退火/exchange3.m`

<details>
<summary>展开原始代码</summary>

````matlab
function r=exchange3(R)
N=length(R);
K=fix(unifrnd(0,N));
J=fix(unifrnd(0,N-1));
I=fix(unifrnd(0,N-2));
if I==J
    J=J+1;
end
if I==K
    K=K+2;
end
if J==K
    K=K+1;
end

if I>J
    I=I+J;
    J=I-J;
    I=I-J;
end
if I>K
    I=I+K;
    K=I-K;
    I=I-K;
end
if J>K
    J=J+K;
    K=J-K;
    J=J-K;
end


r=R;
    if J-I~=1&K-J~=1&K-I~=N-1
        for q=1:(J-I)
            r(I+q)=R(J+1-q);
        end
        for q=1:(K-J)
            r(J+q)=R(K+1-q);
        end
    end
    if J-I==1&K-J==1
        r(K)=R(J);r(J)=R(K);
    end
    if J-I==1&K-J~=1&K-I~=N-1
        for q=1:(K-J)
            r(I+q)=R(I+1+q);
        end
        r(K)=R(J);
    end
    if K-J==1&J-I~=1&K~=N
        for q=1:(J-I)
            r(I+1+q)=R(I+q);
        end
        r(I+1)=R(K);
    end
    if I==1&J==2&K==N
        for q=1:(N-2)
            r(1+q)=R(2+q);
        end
        r(N)=R(2);
    end
    if I==1&J==(N-1)&K==N
        for q=1:(N-2)
            r(q)=R(1+q);
        end
        r(N-1)=R(1);
    end
    if J-I~=1&K-I==N-1
        for q=1:(J-1)
            r(q)=R(1+q);
        end
        r(J)=R(1);
    end
    if J==(N-1)&K==N&J-I~=1
        r(J+1)=R(N);
        for q=1:(N-J-1)
            r(J+1+q)=R(J+q);
        end
    end
    
````

</details>

#### 中国数学建模-编程交流-模拟退火算法 · MATLAB · 6bae9a59

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：按温度和接受概率进行模拟退火搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`59a8c73557afc40dbf6da5230e19e8a251551688bb7790f26b0085a9541042e0`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火算法/中国数学建模-编程交流-模拟退火算法.txt`

<details>
<summary>展开原始代码</summary>

````matlab
中国数学建模-编程交流-模拟退火算法
        wh-ee 重登录  隐身  用户控制面板  搜索  风格  论坛状态  论坛展区  社区服务  社区休闲  网站首页  退出 

      >> VC++,C,Perl,Asp...编程学习,算法介绍.  我的收件箱 (0) 
       中国数学建模 → 学术区 → 编程交流 → 模拟退火算法 

             您是本帖的第 1105 个阅读者       
             * 贴子主题：模拟退火算法           

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28

        鲜花(0)  鸡蛋(1)             楼主 



               模拟退火算法
              模拟退火算法
              　　模拟退火算法来源于固体退火原理，将固体加温至充分高，再让其徐徐冷却，加温时，固体内部粒子随温升变为无序状，内能增大，而徐徐冷却时粒子渐趋有序，在每个温度都达到平衡态，最后在常温时达到基态，内能减为最小。根据Metropolis准则，粒子在温度T时趋于平衡的概率为e-ΔE/(kT)，其中E为温度T时的内能，ΔE为其改变量，k为Boltzmann常数。用固体退火模拟组合优化问题，将内能E模拟为目标函数值f，温度T演化成控制参数t，即得到解组合优化问题的模拟退火算法：由初始解i和控制参数初值t开始，对当前解重复“产生新解→计算目标函数差→接受或舍弃”的迭代，并逐步衰减t值，算法终止时的当前解即为所得近似最优解，这是基于蒙特卡罗迭代求解法的一种启发式随机搜索过程。退火过程由冷却进度表(Cooling 
              Schedule)控制，包括控制参数的初值t及其衰减因子Δt、每个t值时的迭代次数L和停止条件S。 
              3.5.1 模拟退火算法的模型
              　　模拟退火算法可以分解为解空间、目标函数和初始解三部分。
              　模拟退火的基本思想:
              　　(1) 初始化：初始温度T(充分大)，初始解状态S(是算法迭代的起点)， 每个T值的迭代次数L
              　　(2) 对k=1，……，L做第(3)至第6步：
              　　(3) 产生新解S′
              　　(4) 计算增量Δt′=C(S′)-C(S)，其中C(S)为评价函数
              　　(5) 若Δt′<0则接受S′作为新的当前解，否则以概率exp(-Δt′/T)接受S′作为新的当前解.
              　　(6) 如果满足终止条件则输出当前解作为最优解，结束程序。
              终止条件通常取为连续若干个新解都没有被接受时终止算法。
              　　(7) T逐渐减少，且T->0，然后转第2步。
              算法对应动态演示图：
              模拟退火算法新解的产生和接受可分为如下四个步骤：
              　　第一步是由一个产生函数从当前解产生一个位于解空间的新解；为便于后续的计算和接受，减少算法耗时，通常选择由当前新解经过简单地变换即可产生新解的方法，如对构成新解的全部或部分元素进行置换、互换等，注意到产生新解的变换方法决定了当前新解的邻域结构，因而对冷却进度表的选取有一定的影响。
              　　第二步是计算与新解所对应的目标函数差。因为目标函数差仅由变换部分产生，所以目标函数差的计算最好按增量计算。事实表明，对大多数应用而言，这是计算目标函数差的最快方法。
              　　第三步是判断新解是否被接受,判断的依据是一个接受准则，最常用的接受准则是Metropo1is准则: 
              若Δt′<0则接受S′作为新的当前解S，否则以概率exp(-Δt′/T)接受S′作为新的当前解S。
              　　第四步是当新解被确定接受时，用新解代替当前解，这只需将当前解中对应于产生新解时的变换部分予以实现，同时修正目标函数值即可。此时，当前解实现了一次迭代。可在此基础上开始下一轮试验。而当新解被判定为舍弃时，则在原当前解的基础上继续下一轮试验。
              　　模拟退火算法与初始值无关，算法求得的解与初始解状态S(是算法迭代的起点)无关；模拟退火算法具有渐近收敛性，已在理论上被证明是一种以概率l 
              收敛于全局最优解的全局优化算法；模拟退火算法具有并行性。

              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:07:29      

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 2 楼 



               
              模拟退火算法的简单应用
              　　作为模拟退火算法应用，讨论货郎担问题(Travelling Salesman 
              Problem，简记为TSP)：设有n个城市，用数码1,…,n代表。城市i和城市j之间的距离为d(i，j) i, 
              j=1,…,n．TSP问题是要找遍访每个域市恰好一次的一条回路，且其路径总长度为最短.。
              　　求解TSP的模拟退火算法模型可描述如下：
              　　解空间 解空间S是遍访每个城市恰好一次的所有回路，是{1，……，n}的所有循环排列的集合，S中的成员记为(w1,w2 
              ,……，wn)，并记wn+1= w1。初始解可选为(1，……，n)
              　　目标函数 此时的目标函数即为访问所有城市的路径总长度或称为代价函数： 

              　　我们要求此代价函数的最小值。
              　　新解的产生 随机产生1和n之间的两相异数k和m，若k<m，则将
              　　(w1, w2 ,…，wk , wk+1 ,…，wm ,…，wn)
              　　变为：
              　　(w1, w2 ,…，wm , wm-1 ,…，wk+1 , wk ,…，wn).
              　　如果是k>m，则将
              　　(w1, w2 ,…，wk , wk+1 ,…，wm ,…，wn)
              　　变为：
              　　(wm, wm-1 ,…，w1 , wm+1 ,…，wk-1 ,wn , wn-1 ,…，wk).
              　　上述变换方法可简单说成是“逆转中间或者逆转两端”。
              　　也可以采用其他的变换方法，有些变换有独特的优越性，有时也将它们交替使用，得到一种更好方法。 
              　　代价函数差 设将(w1, w2 ,……，wn)变换为(u1, u2 ,……，un), 则代价函数差为： 

              根据上述分析，可写出用模拟退火算法求解TSP问题的伪程序：
              Procedure TSPSA:
              　begin 
              　　init-of-T; { T为初始温度}
              　　S={1，……，n}; {S为初始值}
              　　termination=false;
              　　while termination=false
              　　　begin 
              　　　　for i=1 to L do
              　　　　　　begin
              　　　　　　　　generate(S′form S); { 从当前回路S产生新回路S′}
              　　　　　　　　Δt:=f(S′))-f(S);{f(S)为路径总长}
              　　　　　　　　IF(Δt<0) OR (EXP(-Δt/T)>Random-of-[0,1])
              　　　　　　　　S=S′;
              　　　　　　　　IF the-halt-condition-is-TRUE THEN 
              　　　　　　　　termination=true;
              　　　　　　End;
              　　　　T_lower;
              　　　End;
              　End
              　　模拟退火算法的应用很广泛，可以较高的效率求解最大截问题(Max Cut Problem)、0-1背包问题(Zero One 
              Knapsack Problem)、图着色问题(Graph Colouring Problem)、调度问题(Scheduling 
              Problem)等等。

              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:07:41       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 3 楼 



               
              模拟退火算法的参数控制问题
              　　模拟退火算法的应用很广泛，可以求解NP完全问题，但其参数难以控制，其主要问题有以下三点：
              　　(1) 温度T的初始值设置问题。
              　　温度T的初始值设置是影响模拟退火算法全局搜索性能的重要因素之一、初始温度高，则搜索到全局最优解的可能性大，但因此要花费大量的计算时间；反之，则可节约计算时间，但全局搜索性能可能受到影响。实际应用过程中，初始温度一般需要依据实验结果进行若干次调整。
              　　(2) 退火速度问题。
              　　模拟退火算法的全局搜索性能也与退火速度密切相关。一般来说，同一温度下的“充分”搜索(退火)是相当必要的，但这需要计算时间。实际应用中，要针对具体问题的性质和特征设置合理的退火平衡条件。
              　　(3) 温度管理问题。
              　　温度管理问题也是模拟退火算法难以处理的问题之一。实际应用中，由于必须考虑计算复杂度的切实可行性等问题，常采用如下所示的降温方式：

              T(t+1)＝k×T(t)
              式中k为正的略小于1.00的常数，t为降温的次数。

              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:08:10       

              dancing_fish  
        
        
        等级：新手上路 
        文章：51
        积分：438
        门派：☆nudter☆ 
        注册：2004-7-10
                        第 4 楼 



               

              以下是引用b在2004-5-27 19:07:41的发言：
              模拟退火算法的简单应用
              　　作为模拟退火算法应用，讨论货郎担问题(Travelling Salesman 
              Problem，简记为TSP)：设有n个城市，用数码1,…,n代表。城市i和城市j之间的距离为d(i，j) i, 
              j=1,…,n．TSP问题是要找遍访每个域市恰好一次的一条回路，且其路径总长度为最短.。
              　　求解TSP的模拟退火算法模型可描述如下：
              　　解空间 解空间S是遍访每个城市恰好一次的所有回路，是{1，……，n}的所有循环排列的集合，S中的成员记为(w1,w2 
              ,……，wn)，并记wn+1= w1。初始解可选为(1，……，n)
              　　目标函数 此时的目标函数即为访问所有城市的路径总长度或称为代价函数： 

              　　我们要求此代价函数的最小值。
              　　新解的产生 随机产生1和n之间的两相异数k和m，若k<m，则将
              　　(w1, w2 ,…，wk , wk+1 ,…，wm ,…，wn)
              　　变为：
              　　(w1, w2 ,…，wm , wm-1 ,…，wk+1 , wk ,…，wn).
              　　如果是k>m，则将
              　　(w1, w2 ,…，wk , wk+1 ,…，wm ,…，wn)
              　　变为：
              　　(wm, wm-1 ,…，w1 , wm+1 ,…，wk-1 ,wn , wn-1 ,…，wk).
              　　上述变换方法可简单说成是“逆转中间或者逆转两端”。
              　　也可以采用其他的变换方法，有些变换有独特的优越性，有时也将它们交替使用，得到一种更好方法。 
              　　代价函数差 设将(w1, w2 ,……，wn)变换为(u1, u2 ,……，un), 则代价函数差为： 

              根据上述分析，可写出用模拟退火算法求解TSP问题的伪程序：
              Procedure TSPSA:
              　begin 
              　　init-of-T; { T为初始温度}
              　　S={1，……，n}; {S为初始值}
              　　termination=false;
              　　while termination=false
              　　　begin 
              　　　　for i=1 to L do
              　　　　　　begin
              　　　　　　　　generate(S′form S); { 从当前回路S产生新回路S′}
              　　　　　　　　Δt:=f(S′))-f(S);{f(S)为路径总长}
              　　　　　　　　IF(Δt<0) OR (EXP(-Δt/T)>Random-of-[0,1])
              　　　　　　　　S=S′;
              　　　　　　　　IF the-halt-condition-is-TRUE THEN 
              　　　　　　　　termination=true;
              　　　　　　End;
              　　　　T_lower;
              　　　End;
              　End
              　　模拟退火算法的应用很广泛，可以较高的效率求解最大截问题(Max Cut Problem)、0-1背包问题(Zero One 
              Knapsack Problem)、图着色问题(Graph Colouring Problem)、调度问题(Scheduling 
              Problem)等等。



       2004-7-12 10:42:30       

              heihei  
        
        
        等级：新手上路 
        文章：34
        积分：420
        门派：☆nudter☆ 
        注册：2004-6-23
                        第 5 楼 



               

              楼主啊，你能不能把你的所有的关于模拟退火的资料和例题程序都发给我呀!我看你这帖后还是一头雾水啊，似懂非懂啊，能不能给小弟一些例题和相关程序啊!谢谢!
              E-MAIL:dxyaopengfei@163.com

       2004-8-7 11:16:29       

              杭州阿羊  
        
        
        等级：新手上路 
        文章：3
        积分：213
        门派：☆nudter☆ 
        注册：2004-8-7
                        第 6 楼 



               

              我也想知道啊，能不能给出一些经典的数模论文关于使用模拟退火方法的？
              yangxuan0910@sina.com

       2004-8-7 16:08:40       

              konvin  
        
        
        头衔：mcm 
        等级：新手上路 
        文章：6
        积分：216
        门派：☆nudter☆ 
        注册：2004-7-12
                         第 7 楼 



               
              konvin@etang.com谢谢楼主

              ----------------------------------------------
              愿与大家成为朋友，共同讨论一齐建模！
              qq：410072886
              e－mail：410072886@qq.com 

       2004-8-8 20:32:57       

              bashery  
        
        
        等级：新手上路 
        文章：8
        积分：270
        门派：☆nudter☆ 
        注册：2004-7-10
                        第 8 楼 



               

              我也要啊，谢谢楼主
              xyy0231@hotmail.com

       2004-8-8 22:19:12       

              清语依愉  
        
        
        等级：新手上路 
        文章：2
        积分：222
        门派：☆nudter☆ 
        注册：2004-8-10
                        第 9 楼 



               

              xswenxy@nbip.net
              谢谢

       2004-8-10 10:02:20       

              海岩秋沙  
        
        
        等级：论坛游民 
        文章：110
        积分：448
        注册：2004-7-17
                         第 10 楼 



               

              模拟退火我的教练也讲过 
              我还不是很清楚怎样编程！还望各位大虾指点啊！


              ----------------------------------------------
              Magic Lee

              有志者，事竞成！
              海内存知己，天涯若比邻！！！ 

       2004-8-10 21:23:38       

      本主题贴数 23   分页：9 1 2 3 :   跳转论坛至...╋数学建模  ├数模竞赛  ├新手入门  ├数学工具  ├资源与检索╋学术区 
         ├数学思想  ├编程交流  ├学术杂谈  ├English Fans╋休闲专区  ├灌水搞笑专区  ├神秘园╋本站站务  ├站务讨论  
        ├数模管理区  ├回收站


       *快速回复：模拟退火算法
           发贴表情
                  
                  
                  
                  
                  
                  

               段落格式 普通格式标题 1标题 2标题 3标题 4标题 5标题 6标题 7已编排格式地址  
              字体宋体黑体楷体仿宋隶书幼圆新宋体细明体ArialArial BlackCourierVerdanaWide 
              LatinWingdings  字号1234567              


                      第 1 页,共 7 页， 49 个

       显示签名     内容限制：字节. 


      管理选项： 专题管理 | 修复 | 锁定 | 解锁 | 提升 | 跟贴管理 | 删除 | 移动 | 设置固顶 | 奖励 | 惩罚 | 发布公告 

            Copyright &copy;2002 - 2004 Shumo.Com
            执行时间：781.25000毫秒。查询数据库5次。
            当前模板样式：[默认模板] 
````

</details>

#### Anneal · MATLAB · f38bb5fa

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a68b0f4e7a157bbf0c8065df9cefa07bfa3e3703d32607f81f39c48fe5edf1e1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/Anneal.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/Anneal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [X2,fX2] = Anneal(x,fx,FitnessFcn,B,stepSize,A,LB,UB,R,L,t)
GenomeLength = length(x);
Lbnd = B(1,:);
Ubnd = B(2,:);
span = max([sqrt(eps)*x;min([x-Lbnd;Ubnd-x])]);
scale = stepSize * span;

X2=[];fX2=[];
r = 0; l = 0;
while r<R && l<L
    x2 = x  + scale .* randn(1,GenomeLength);
    y2 = (A*x2')';
    if all(LB'<y2 & y2<UB');
        l = l+1;
        fx2 = feval(FitnessFcn,x2);
        delta_f = fx2 - fx;
        if delta_f < 0
            r = r+1;
            x = x2;
            fx = fx2;
            span = min([x-Lbnd;Ubnd-x]);
            scale = stepSize * span;
            X2 = [X2;x2];
            fX2 = [fX2;fx2];
        elseif exp(-delta_f/t) > rand
            r = r+1;
            x = x2;
            fx = fx2;
            span = min([x-Lbnd;Ubnd-x]);
            scale = stepSize * span;
            X2 = [X2;x2];
            fX2 = [fX2;fx2];
        end
    end
end
````

</details>

#### Anneal7 · MATLAB · b9828a01

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`26fac9884ecdd4dbb143f51bfafd3bf0ca778257fe5ce13c14650734dabf2243`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/Anneal7.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/Anneal7.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/Anneal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/Anneal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [X2,fX2] = Anneal(x,fx,FitnessFcn,B,stepSize,A,LB,UB,R,L,t)
GenomeLength = length(x);
Lbnd = B(1,:);
Ubnd = B(2,:);
span = max([sqrt(eps)*x;min([x-Lbnd;Ubnd-x])]);
scale = stepSize * span;

X2=[];fX2=[];
r=0; l=0; nb=0;
while r<R && l<L
    x2 = x  + scale .* randn(1,GenomeLength);
    y2 = (A*x2')';
    if all(LB'<y2 & y2<UB');
        l = l+1;
        fx2 = feval(FitnessFcn,x2);
        delta_f = fx2 - fx;
        if delta_f < 0
            nb = 0;
            r = r+1;
            x = x2;
            fx = fx2;
            span = min([x-Lbnd;Ubnd-x]);
            scale = stepSize * span;
            X2 = [X2;x2];
            fX2 = [fX2;fx2];
        elseif exp(-delta_f/t) > rand
            nb = 0;
            r = r+1;
            x = x2;
            fx = fx2;
            span = min([x-Lbnd;Ubnd-x]);
            scale = stepSize * span;
            X2 = [X2;x2];
            fX2 = [fX2;fx2];
        else
            nb = nb + 1;
            if nb == 10*GenomeLength
                stepSize = stepSize / 10;
                scale = stepSize * span;
            elseif nb == 30*GenomeLength
                stepSize = min(2,stepSize * 20);
                scale = stepSize * span;
            elseif nb == 50*GenomeLength
                stepSize = stepSize / 40;
                scale = stepSize * span;
                nb = 0;
            end
        end
    else
        nb = nb + 1;
    end
end
````

</details>

#### 相似实现组 · MATLAB · d6521834

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：5
- 原始来源文件：10
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：PopAnneal1.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`cc4cfe8b9054aa51690bc0416f2fe187c6abb254f42d596bc1af7e05f2ea3abb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/PopAnneal1.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/PopAnneal1.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/Anneal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/Anneal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Population,Score] = PopAnneal(options,GenomeLength,FitnessFcn, ...
    state,thisScore,thisPopulation)
R=10;L=GenomeLength*100;
%T0=0.1;alpha=0.8;
%t = T0 * alpha^(state.Generation);

nParents = size(thisPopulation,1);
nAnneal = round(nParents / R /2);

[Score,k] = sort(thisScore);
Population  = thisPopulation(k,:);

t = min(1/sqrt(eps),(Score(nAnneal*R)-Score(1))/(log(nAnneal*R)-log(nAnneal*R-1)));
t = max(sqrt(eps),t);

shrink=0.9;
stepSize = max(sqrt(eps),shrink^(state.Generation));

if isfield(options,'LinearConstr')
    % Extract information about constraints
    linCon = options.LinearConstr;
    type = linCon.type;
    % Sub-problem type is constrained?
    if ~strcmpi(type,'unconstrained')
        A = linCon.A;
        LB = linCon.L;
        UB = linCon.U;
    end
end

Lbnd = min(Population);%(1:nParents/2,:)
Ubnd = max(Population);
Bound = [Lbnd;Ubnd];

PopAnneal = [];
ScoreAnneal = [];
for i = 1:nAnneal
    x = Population(i,:);
    fx = Score(i);
    [X2,fX2] = Anneal(x,fx,FitnessFcn,Bound,stepSize^2,A,LB,UB,R,L,t*stepSize);
    PopAnneal = [PopAnneal;X2];
    ScoreAnneal = [ScoreAnneal;fX2];
end

Population = [PopAnneal;Population];
Score = [ScoreAnneal;Score];

[Score,k] = sort(Score);
Population  = Population(k,:);

Population = Population(1:nParents,:);
Score = Score(1:nParents,:);
````

</details>

##### 变体 2：PopAnneal2.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`2c6d1ce8ab716e50486d1ed17150a3991701306932c74e2dde5b9ce0b58ceb4e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/PopAnneal2.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/PopAnneal2.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/Anneal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/Anneal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Population,Score] = PopAnneal(options,GenomeLength,FitnessFcn, ...
    state,thisScore,thisPopulation)
R=10;L=GenomeLength*100;
%T0=1000;alpha=0.8;
%t = T0 * alpha^(state.Generation);

nParents = size(thisPopulation,1);
nAnneal = round(nParents / R /2);

[Score,k] = sort(thisScore);
Population  = thisPopulation(k,:);

t = min(1/sqrt(eps),(Score(nAnneal*R)-Score(1))/log(2));
t = max(sqrt(eps),t);

k2 = state.Generation;

shrink = 0.9;
stepSize = max(sqrt(eps),shrink^k2);

ta = 0.78;
ta = max(sqrt(eps),ta^(k2^(1/2)));

if isfield(options,'LinearConstr')
    % Extract information about constraints
    linCon = options.LinearConstr;
    type = linCon.type;
    % Sub-problem type is constrained?
    if ~strcmpi(type,'unconstrained')
        A = linCon.A;
        LB = linCon.L;
        UB = linCon.U;
        Lbnd = LB((end-GenomeLength)+1:end);
        Ubnd = UB((end-GenomeLength)+1:end);
    else % Or unconstrained sub-problem
        Lbnd = -(1e+20)*ones(GenomeLength,1);
        Ubnd = (1e+20)*ones(GenomeLength,1);
    end
else % Unconstrained 'main' problems;
    type = 'unconstrained';
    Lbnd = -(1e+20)*ones(GenomeLength,1);
    Ubnd = (1e+20)*ones(GenomeLength,1);
end

Bound = [Lbnd';Ubnd'];

PopAnneal = [];
ScoreAnneal = [];
for i = 1:nAnneal
    x = Population(i,:);
    fx = Score(i);
    [X2,fX2] = Anneal(x,fx,FitnessFcn,Bound,stepSize,A,LB,UB,R,L,t*ta);
    PopAnneal = [PopAnneal;X2];
    ScoreAnneal = [ScoreAnneal;fX2];
end

Population = [PopAnneal;Population];
Score = [ScoreAnneal;Score];

[Score,k] = sort(Score);
Population  = Population(k,:);

Population = Population(1:nParents,:);
Score = Score(1:nParents,:);
````

</details>

##### 变体 3：PopAnneal3.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`eee815f63308d9b9529d35780abfbe51a3994f046f0b17fbe8b57aa329fa1ede`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/PopAnneal3.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/PopAnneal3.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/Anneal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/Anneal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Population,Score] = PopAnneal(options,GenomeLength,FitnessFcn, ...
    state,thisScore,thisPopulation)
R=10;L=GenomeLength*100;
%T0=1000;alpha=0.8;
%t = T0 * alpha^(state.Generation);

nParents = size(thisPopulation,1);
nAnneal = ceil(nParents / R /2);

[Score,k] = sort(thisScore);
Population  = thisPopulation(k,:);

t = min(1/sqrt(eps),(Score(nAnneal*R)-Score(1))/log(2));%ta = 0.85;
t = max(sqrt(eps),t);

if isfield(options,'LinearConstr')
    % Extract information about constraints
    linCon = options.LinearConstr;
    type = linCon.type;
    % Sub-problem type is constrained?
    if ~strcmpi(type,'unconstrained')
        A = linCon.A;
        LB = linCon.L;
        UB = linCon.U;
        Lbnd = LB((end-GenomeLength)+1:end);
        Ubnd = UB((end-GenomeLength)+1:end);
    else % Or unconstrained sub-problem
        Lbnd = -(1e+20)*ones(GenomeLength,1);
        Ubnd = (1e+20)*ones(GenomeLength,1);
    end
else % Unconstrained 'main' problems;
    type = 'unconstrained';
    Lbnd = -(1e+20)*ones(GenomeLength,1);
    Ubnd = (1e+20)*ones(GenomeLength,1);
end

Lbnd2 = min(Population(1:nParents/2,:));%(1:nParents/2,:)
Ubnd2 = max(Population(1:nParents/2,:));

k2 = state.Generation;
shrink = 0.95;
stepSize = max(sqrt(eps),shrink^k2);
Lbnd = (Lbnd2' + stepSize*Lbnd) / (1+stepSize);
Ubnd = (Ubnd2' + stepSize*Ubnd) / (1+stepSize);

Bound = [Lbnd';Ubnd'];

ta = 0.78;
ta = max(sqrt(eps),ta^(k2^(1/2)));

shrink = 0.95;
stepSize = max(sqrt(eps),shrink^k2);

PopAnneal = [];
ScoreAnneal = [];
for i = 1:nAnneal
    x = Population(i,:);
    fx = Score(i);
    [X2,fX2] = Anneal(x,fx,FitnessFcn,Bound,stepSize,A,LB,UB,R,L,t*ta);%
    PopAnneal = [PopAnneal;X2];
    ScoreAnneal = [ScoreAnneal;fX2];
end
x = mean(Population(1:nAnneal*R,:));%
fx = feval(FitnessFcn,x);
PopAnneal = [PopAnneal;x];
ScoreAnneal = [ScoreAnneal;fx];
[X2,fX2] = Anneal(x,fx,FitnessFcn,Bound,stepSize,A,LB,UB,R,L,t*ta);%
PopAnneal = [PopAnneal;X2];
ScoreAnneal = [ScoreAnneal;fX2];

Population = [PopAnneal;Population];
Score = [ScoreAnneal;Score];

[Score,k] = sort(Score);
Population  = Population(k,:);

Population = Population(1:nParents,:);
Score = Score(1:nParents,:);
````

</details>

##### 变体 4：PopAnneal5.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`18db5feb4b1b74064c5eaabeb581dfe60aea5296a6181c399a3219032dfdbdbc`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/PopAnneal5.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/PopAnneal5.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/Anneal5.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/Anneal5.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Population,Score] = PopAnneal(options,GenomeLength,FitnessFcn, ...
    state,thisScore,thisPopulation)
R=10;L=GenomeLength*100;
%T0=1000;alpha=0.8;
%t = T0 * alpha^(state.Generation);

nParents = size(thisPopulation,1);
nAnneal = round(nParents / R /2);

[Score,k] = sort(thisScore);
Population  = thisPopulation(k,:);

%t = min(1/sqrt(eps),(Score(nAnneal*R)-Score(1))/...
%(log(nAnneal*R)-log(nAnneal*R-1)));%ta = 0.6;
t = min(1/sqrt(eps),(Score(nAnneal*R)-Score(1))/log(2));%ta = 0.85;
t = max(sqrt(eps),t);

if isfield(options,'LinearConstr')
    % Extract information about constraints
    linCon = options.LinearConstr;
    type = linCon.type;
    % Sub-problem type is constrained?
    if ~strcmpi(type,'unconstrained')
        A = linCon.A;
        LB = linCon.L;
        UB = linCon.U;
        Lbnd = LB((end-GenomeLength)+1:end);
        Ubnd = UB((end-GenomeLength)+1:end);
    else % Or unconstrained sub-problem
        Lbnd = -(1e+20)*ones(GenomeLength,1);
        Ubnd = (1e+20)*ones(GenomeLength,1);
    end
else % Unconstrained 'main' problems;
    type = 'unconstrained';
    Lbnd = -(1e+20)*ones(GenomeLength,1);
    Ubnd = (1e+20)*ones(GenomeLength,1);
end

k2 = state.Generation;

Bound = [Lbnd';Ubnd'];

ta = 0.78;
ta = max(sqrt(eps),ta^(k2^(1/GenomeLength)));

PopAnneal = [];
ScoreAnneal = [];
for i = 1:nAnneal
    x = Population(i,:);
    fx = Score(i);
    [X2,fX2] = Anneal5(x,fx,FitnessFcn,Bound,1,A,LB,UB,R,L,t*ta);%t*ta
    PopAnneal = [PopAnneal;X2];
    ScoreAnneal = [ScoreAnneal;fX2];
end

Population = [PopAnneal;Population];
Score = [ScoreAnneal;Score];

[Score,k] = sort(Score);
Population  = Population(k,:);

Population = Population(1:nParents,:);
Score = Score(1:nParents,:);
````

</details>

##### 变体 5：PopAnneal6.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3e25817c272264e52a30c99d741fafc660a791f8dfb7bdcfc3a82fbae34bc821`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/PopAnneal6.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/PopAnneal6.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Population,Score] = PopAnneal(options,GenomeLength,FitnessFcn, ...
    state,thisScore,thisPopulation)
R=10;L=GenomeLength*100;
%T0=1000;alpha=0.8;
%t = T0 * alpha^(state.Generation);

nParents = size(thisPopulation,1);
nAnneal = round(nParents / R /2);

[Score,k] = sort(thisScore);
Population  = thisPopulation(k,:);

t = min(1/sqrt(eps),(Score(nAnneal*R)-Score(1))/log(2));%ta = 0.85;
t = max(sqrt(eps),t);

if isfield(options,'LinearConstr')
    % Extract information about constraints
    linCon = options.LinearConstr;
    type = linCon.type;
    % Sub-problem type is constrained?
    if ~strcmpi(type,'unconstrained')
        A = linCon.A;
        LB = linCon.L;
        UB = linCon.U;
        Lbnd = LB((end-GenomeLength)+1:end);
        Ubnd = UB((end-GenomeLength)+1:end);
    else % Or unconstrained sub-problem
        Lbnd = -(1e+20)*ones(GenomeLength,1);
        Ubnd = (1e+20)*ones(GenomeLength,1);
    end
else % Unconstrained 'main' problems;
    type = 'unconstrained';
    Lbnd = -(1e+20)*ones(GenomeLength,1);
    Ubnd = (1e+20)*ones(GenomeLength,1);
end

k2 = state.Generation;
if k2 < 50
    AnnealFcn = @Anneal;
    shrink = 0.95;
    stepSize = 0.5*max(sqrt(eps),shrink^k2);
    
    Lbnd2 = min(Population(1:nParents/2,:));%(1:nParents/2,:)
    Ubnd2 = max(Population(1:nParents/2,:));
    Lbnd = (Lbnd2' + stepSize*Lbnd) / (1+stepSize);
    Ubnd = (Ubnd2' + stepSize*Ubnd) / (1+stepSize);
else
    stepSize = 1;
    AnnealFcn = @Anneal5;
end

Bound = [Lbnd';Ubnd'];

ta = 0.78;
ta = max(sqrt(eps),ta^(k2^(1/2)));

PopAnneal = [];
ScoreAnneal = [];
for i = 1:nAnneal
    x = Population(i,:);
    fx = Score(i);
    [X2,fX2] = feval(AnnealFcn,x,fx,FitnessFcn,Bound,stepSize,A,LB,UB,R,L,t*ta);%t*ta
    PopAnneal = [PopAnneal;X2];
    ScoreAnneal = [ScoreAnneal;fX2];
end
x = mean(Population(1:nAnneal*R,:));%
fx = feval(FitnessFcn,x);
PopAnneal = [PopAnneal;x];
ScoreAnneal = [ScoreAnneal;fx];
[X2,fX2] = feval(AnnealFcn,x,fx,FitnessFcn,Bound,stepSize,A,LB,UB,R,L,t*ta);%
PopAnneal = [PopAnneal;X2];
ScoreAnneal = [ScoreAnneal;fX2];

Population = [PopAnneal;Population];
Score = [ScoreAnneal;Score];

[Score,k] = sort(Score);
Population  = Population(k,:);

Population = Population(1:nParents,:);
Score = Score(1:nParents,:);
````

</details>

#### PopAnneal4 · MATLAB · 8d91ce35

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`774ea62a102f2035e81bd2760f1ef7c9546cd0cbba6b9782e3b4fa0de4fac5e1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/PopAnneal4.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/PopAnneal4.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/Anneal.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/Anneal.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [Population,Score] = PopAnneal(options,GenomeLength,FitnessFcn,state,thisScore,thisPopulation)
R=1;L=300;
%T0=1000;alpha=0.8;
%t = T0 * alpha^(state.Generation);

nParents = size(thisPopulation,1);
nAnneal = nParents;

[Score,k] = sort(thisScore);
Population  = thisPopulation(k,:);

t = 10000;

shrink=0.95;
stepSize = max(sqrt(eps),shrink^(state.Generation));

if isfield(options,'LinearConstr')
    % Extract information about constraints
    linCon = options.LinearConstr;
    type = linCon.type;
    % Sub-problem type is constrained?
    if ~strcmpi(type,'unconstrained')
        A = linCon.A;
        LB = linCon.L;
        UB = linCon.U;
        Lbnd = LB((end-GenomeLength)+1:end);
        Ubnd = UB((end-GenomeLength)+1:end);
    else % Or unconstrained sub-problem
        Lbnd = -(1e+20)*ones(GenomeLength,1);
        Ubnd = (1e+20)*ones(GenomeLength,1);
    end
else % Unconstrained 'main' problems;
    type = 'unconstrained';
    Lbnd = -(1e+20)*ones(GenomeLength,1);
    Ubnd = (1e+20)*ones(GenomeLength,1);
end

Bound = [Lbnd';Ubnd'];

PopAnneal = [];
ScoreAnneal = [];
for i = 1:nAnneal
    x = Population(i,:);
    fx = Score(i);
    [X2,fX2] = Anneal(x,fx,FitnessFcn,Bound,stepSize,A,LB,UB,R,L,t*stepSize^2);
    PopAnneal = [PopAnneal;X2];
    ScoreAnneal = [ScoreAnneal;fX2];
end

Population = [PopAnneal;Population];
Score = [ScoreAnneal;Score];

[Score,k] = sort(Score);
Population  = Population(k,:);

Population = Population(1:nParents,:);
Score = Score(1:nParents,:);
````

</details>

#### 智能算法之模拟退火算法代码 · MATLAB · 346c247c

- 归属算法：模拟退火SA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#模拟退火SA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于模拟退火SA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`770e767ad32d436234e294e7e49de5f970e245b302249bed994c2af4e1907ed6`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/智能算法之模拟退火算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab

%生成初始解，求目标函数f(x)=x1^2+x2^2+8在x1^2-x2>0;-x1-x2^2+2=0约束下的最小值问题  
sol_new2=1;%（1）解空间（初始解）  
sol_new1=2-sol_new2^2;  
sol_current1 = sol_new1;   
sol_best1 = sol_new1;  
sol_current2 = sol_new2;   
sol_best2 = sol_new2;  
E_current = inf;  
E_best = inf;  
  
rand('state',sum(clock)); %初始化随机数发生器  
t=90; %初始温度  
tf=89.9; %结束温度  
a = 0.99; %温度下降比例  
  
while t>=tf%（7）结束条件  
    for r=1:1000 %退火次数  
          
        %产生随机扰动（3）新解的产生  
        sol_new2=sol_new2+rand*0.2;  
        sol_new1=2-sol_new2^2;  
          
        %检查是否满足约束  
        if sol_new1^2-sol_new2>=0 && -sol_new1-sol_new2^2+2==0 && sol_new1>=0 &&sol_new2>=0  
        else  
            sol_new2=rand*2;  
            sol_new1=2-sol_new2^2;  
            continue;  
        end  
          
        %退火过程  
        E_new=sol_new1^2+sol_new2^2+8;%（2）目标函数  
        if E_new<E_current%（5）接受准则  
                E_current=E_new;  
                sol_current1=sol_new1;  
                sol_current2=sol_new2;  
                if E_new<E_best  
                    %把冷却过程中最好的解保存下来  
                    E_best=E_new;  
                    sol_best1=sol_new1;  
                    sol_best2=sol_new2;  
                end  
        else  
                if rand<exp(-(E_new-E_current)/t)%（4）代价函数差  
                    E_current=E_new;  
                    sol_current1=sol_new1;  
                    sol_current2=sol_new2;  
                else  
                    sol_new1=sol_current1;  
                    sol_new2=sol_current2;  
                end  
        end  
        plot(r,E_best,'*')  
        hold on  
    end  
    t=t*a;%（6）降温  
end  
  
disp('最优解为：')  
disp(sol_best1)  
disp(sol_best2)  
disp('目标表达式的最小值等于：')  
disp(E_best)  
````

</details>

### 现代优化算法 · 实现

#### ex12_1 · MATLAB · bb3f9129

- 归属算法：现代优化算法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#现代优化算法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于现代优化算法中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e39fe8cbe1f006d5b9892fca3c466b6da507e29fc92eb3b9d15e6c4ef3a57c3f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/ex12_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=[-1 -2 0;-1 0 0];b=[-1;0];
[x,y]=ga(@ycfun1,3,a,b,[],[],[],[],@ycfun2);
x, y=-y
````

</details>

#### ex12_3 · MATLAB · 658631c2

- 归属算法：现代优化算法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#现代优化算法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于现代优化算法中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `ex12_3`、`fun1`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`9178c6251aab2363b06f5e7594528dc56e0855f2c9ed8dfde076697fe9442789`
- 语言：MATLAB
- 符号：`ex12_3`, `fun1`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/ex12_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
function ex12_3
a=[-1 -2 0;-1 0 0];b=[-1;0];
[x,y]=patternsearch(@fun1,rand(1,3),a,b,[],[],[],[],@fun2);  %初始值必须为行向量
x,y=-y
%定义目标函数
function y=fun1(x);   %x为行向量
c1=[2 3 1]; c2=[3 1 0];
y= c1* x' + c2* x'.^2; y=-y;
%定义非线性约束函数
function [f,g]=fun2(x);
f=[x(1)+2*x(1)^2+x(2)+2*x(2)^2+x(3)-10
   x(1)+x(1)^2+x(2)+x(2)^2-x(3)-50
   2*x(1)+x(1)^2+2*x(2)+x(3)-40];
g=x(1)^2+x(3)-2;
````

</details>

#### huaxue · MATLAB · 6ea5c533

- 归属算法：现代优化算法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#现代优化算法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于现代优化算法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `huaxue`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`46e613be1d60233ca45ee26eb655269e0362f9752cf34d3418de73294dde84b6`
- 语言：MATLAB
- 符号：`huaxue`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/huaxue.m`

<details>
<summary>展开原始代码</summary>

````matlab
function yhat=huaxue(beta,x); 
yhat=(beta(4)*x(:,2)-x(:,3)/beta(5))./(1+beta(1)*x(:,1)+... 
beta(2)*x(:,2)+beta(3)*x(:,3)); 
````

</details>

#### tjianyan · MATLAB · 0b738d4b

- 归属算法：现代优化算法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#现代优化算法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于现代优化算法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`41aa4e868a57e285df39c1bad6bfda05f6c48458c97303cf31a6e31883b6bb65`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/tjianyan.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=[78.1  72.4  76.2  74.3  77.4  78.4  76.0  75.6  76.7  77.3]; 
y=[79.1  81.0  77.3  79.1  80.0  79.1  79.1  77.3  80.2  82.1]; 
[h,p,ci]=ttest2(x,y,0.05,-1) 
````

</details>

#### ycfun1 · MATLAB · 53b53e30

- 归属算法：现代优化算法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#现代优化算法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于现代优化算法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `ycfun1`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ade814fbe03c925adaed1e5121671119135e24838fdb4f7595509f5c9cdf3aca`
- 语言：MATLAB
- 符号：`ycfun1`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/ycfun1.m`

<details>
<summary>展开原始代码</summary>

````matlab
function y=ycfun1(x);   %x为行向量
c1=[2 3 1]; c2=[3 1 0];
y= c1* x' + c2* x'.^2; y=-y;
````

</details>

#### ycfun2 · MATLAB · 90f7dd88

- 归属算法：现代优化算法
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#现代优化算法 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于现代优化算法中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`51b932e9efb9abc6981a9cbfe0274458e4d906ef24c5829bb68e02a2a84e8aab`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/ycfun2.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [f,g]=ycfun2(x);
f=[x(1)+2*x(1)^2+x(2)+2*x(2)^2+x(3)-10
   x(1)+x(1)^2+x(2)+x(2)^2-x(3)-50
   2*x(1)+x(1)^2+2*x(2)+x(3)-40];
g=x(1)^2+x(3)-2;
````

</details>

### 粒子群PSO · 实现

使用群体位置与速度更新进行连续或组合空间搜索。

#### DeJong · MATLAB · c7f9552f

- 归属算法：粒子群PSO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于粒子群PSO中的“核心算法与辅助函数”。
- **执行主线**：更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：优先调用 `DeJong`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6bc768f881546edd91011801c016ab7e31f3bd450aebdc9031b21a2e39a6debe`
- 语言：MATLAB
- 符号：`DeJong`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/DeJong.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/functions/DeJong.m`

<details>
<summary>展开原始代码</summary>

````matlab
%The DeJong (Sphere) function for use with the psotoolbox
%
% Function Description:
% Equation -> sum ( x(i)^2 )
%      xmin  = [0, 0, 0.....0]  (all zeroes)
%      fxmin = 0                  (zero)
function Dejed = DeJong(Swarm)
[SwarmSize, Dim] = size(Swarm);
Dejed = sum((Swarm .^2)')';
````

</details>

#### DrawSwarm · MATLAB · 7ea045fe

- 归属算法：粒子群PSO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于粒子群PSO中的“核心算法与辅助函数”。
- **执行主线**：更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：优先调用 `DrawSwarm`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`06873764c2f213d1d954c5466a48fc5274f12893a26516f672fba41cd0ec30b6`
- 语言：MATLAB
- 符号：`DrawSwarm`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/DrawSwarm.m`

<details>
<summary>展开原始代码</summary>

````matlab
%DrawSwarm >> Internal function of psotoolbox.
% Purpose: To draw a visual display of the Swarm.
% 
% You shouldn't need to mess around with this fn. if u don't wanna change the visualization.
% 
% see also: pso.m
%
function DrawSwarm(Swarm, SwarmSize, Generation, Dimensions, GBest, vizAxes)
X = Swarm';
if Dimensions >= 3
    set(vizAxes,'XData',X(1, :),'YData', X(2,:), 'ZData', X(3,:));
elseif Dimensions == 2
    set(vizAxes,'XData',X(1, :),'YData', X(2,:));
end

GenDiv = 100;
xAx = GBest(1);
yAx = GBest(2);
zAx = GBest(2);

zf = 100 * 50/Generation; %zoom factor

if rem(Generation, GenDiv) == 0
    axis([xAx-zf xAx+100 yAx-zf yAx+zf zAx-zf zAx+zf]);
end

title(Generation);
drawnow;
````

</details>

#### Griewank · MATLAB · 1fd81f0d

- 归属算法：粒子群PSO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于粒子群PSO中的“核心算法与辅助函数”。
- **执行主线**：更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：优先调用 `Griewank`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d01fbc478f90f5b7b0d2a3707095a6e868247c5756f143400e1ecc75df52d0a2`
- 语言：MATLAB
- 符号：`Griewank`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/Griewank.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/functions/Griewank.m`

<details>
<summary>展开原始代码</summary>

````matlab
%The Griewank function for use with the psotoolbox
%
% Function Description:
% Equation -> sum(((x(i).^2) / 4000)')' - prod(cos(x(i) ./ sqrt(i))')' + 1
%      xmin  = [0, 0, 0.....0]  (all zeroes)
%      fxmin = 0                  (zero)
function Gred = Griewank(Swarm);
[SwarmSize, Dim] = size(Swarm);
indices = repmat(1:Dim, SwarmSize, 1);
Gred = sum(((Swarm.^2) / 4000)')' - prod(cos(Swarm ./ sqrt(indices))')' + 1;
````

</details>

#### Rastrigrin · MATLAB · 31ff3807

- 归属算法：粒子群PSO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于粒子群PSO中的“核心算法与辅助函数”。
- **执行主线**：更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：优先调用 `Rastrigrin`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ecc69b544573a8d946dd9b7650b9ac401b4170cddb5470a5dee1f84ff6ac0222`
- 语言：MATLAB
- 符号：`Rastrigrin`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/Rastrigrin.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/functions/Rastrigrin.m`

<details>
<summary>展开原始代码</summary>

````matlab
%The Rastrigrin function for use with the psotoolbox
%
% Function Description:
% Equation ->  sum (x(i)^2 - 10 * cos(2 * pi * x(i)) + 10)
%      xmin  = [0, 0, 0.....0]  (all zeoes)
%      fxmin = 0                  (zero)
function Rastred = Rastrigrin(Swarm)
[SwarmSize, Dim] = size(Swarm);
Rastred = Dim * 10 + sum(((Swarm .^2) - 10 * cos(2 * pi * Swarm))')';
````

</details>

#### Rosenbrock · MATLAB · 17fc0c5c

- 归属算法：粒子群PSO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于粒子群PSO中的“核心算法与辅助函数”。
- **执行主线**：更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：优先调用 `Rosenbrock`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`932283b1ec6907be37bedc4c45a3fbdd3438081fe50554445a737f99c4770377`
- 语言：MATLAB
- 符号：`Rosenbrock`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/Rosenbrock.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/functions/Rosenbrock.m`

<details>
<summary>展开原始代码</summary>

````matlab
%The Rosenbrock function for use with the psotoolbox
%
% Function Description:
% Equation -> sum ( 100 * (x(i+1) - x(i)^2)^2 + (1-x(i))^2 )
%      xmin  = [1, 1, 1.....1]  (all ones)
%      fxmin = 0                  (zero)
function Rosened = Rosenbrock(Swarm)
[SwarmSize, Dim] = size(Swarm);
Swarm1 = Swarm(:, 1:(Dim-1));
Swarm2 = Swarm(:, 2:Dim);
if Dim == 2
    Rosened = 100 * (Swarm2 - Swarm1.^2).^2 + (1 - Swarm1).^2;
else     
    Rosened = sum((100 * (Swarm2 - Swarm1.^2).^2 + (1 - Swarm1).^2)')'; 
end   
````

</details>

#### RunExp · MATLAB · d9ed638b

- 归属算法：粒子群PSO
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于粒子群PSO中的“模型求解”。
- **执行主线**：更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：优先调用 `GenExpData`、`RnS`、`RunExp`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、文件结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`307da4eb911e0616ab49e71fb374b61520f0760763a70f5df6eed94a82f7cbea`
- 语言：MATLAB
- 符号：`GenExpData`, `RnS`, `RunExp`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/RunExp.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/pso.m`

<details>
<summary>展开原始代码</summary>

````matlab
%RunExp >> Automation function
% Usage     : RunExp(noRuns, ExitAction) %e.g. RunExp(25, 1); -> Runs each experminet for 25 trials and Exits matlab when doen.
% Arguments : (optional) noRuns     -> Integer -> Number of trials per experiment
%             (optional) ExitAction -> Integer -> Action to perform on completion of experiments
%                                       NOTE: Argument noRuns is required if ExitAction is to be specified.
%                                       Accepted values and their meaning.
%                                       0 = Do Nothing
%                                       1 = Exit Matlab
%                                       2 = Exit Matlab and Shutdown (Windows XP only)
%                                       3 = Exit Matlab and Logoff   (Windows XP only)
%                                       4 = Exit Matlab and Shutdown (Win98 and Me)
%                                       5 = Exit Matlab and Logoff (Win98 and Me)
%
% This function is useful to automate the generation of experimental data.
%
% The default function would conduct the same experiments that were conducted by Ebenhart and Kennedy in their 
% paper - Empirical Study of Particle Swarm Optimization (1999 IEEE 0-708-5536-9/99).
% You may want to change the values of parameters and the names of the functions etc. to suit u'r research
%
% The script stores the values of objective values and history for all the functions in text files for anlysis.
% The name of the function, swarm size and # of dimensions is used to name these files.
% Files starting with an f_ contain the fitness values of the trials while those that begin with an h_ contain the
% history for each trial.
%
% Set the variable numberofRuns to the number of trials needed per experiment.
%
% History        :   Author      :   JAG (Jagatpreet Singh)
%                    Created on  :   07102003 (Thursday. 10th July, 2003)
%                    Comments    :   Arghhhhh! Why don't the results match.
%                    Modified on :   07142003 (Monday. 14th July, 2003)
%                    Comments    :   Converted script into a function. Added code to automatically exit, 
%                                    shutdown or logoff the computer.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Hmm.. I ran the simulations (enter RunExp to try u'rself), but ..er. the results don't match Ebenhart and Kennedy's quoted results.
% So here's somethin for u to work on.>> Answer the following : 
%
% Q|What went wrong? ???
%   Your choices are -
%       a)The code of this toolbox. (if yes, plz point out the location and correction) 
%       b)The random number genrator on my computer
%       c)There was some typo in the paper (try changing values of c1, c2 and w.)
%       d)Er..Code used by Ebenhart and Kennedy in their experiments!
%       e)None/All of the above
% E-mail your answers/comments/analysis to jagatpreet@users.sourceforge.net.
% The one who convinces me with his/her answer would be featured on the psotoolbox website along with the answer. :-) 
% So. Get u'r analytical hats on.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function RunExp(noRuns, ExitAction)
numberofRuns = 50;          %number of trials per experiment
if nargin >= 1
    numberofRuns = noRuns;
    if nargin < 2
        ExitAction = 0; 
    end
end
        
psoOptions = get_psoOptions;

% psoOptions.Vars.ErrGoal = 1e-200

% Parameters common across all functions
psoOptions.SParams.c1 = 2;
psoOptions.SParams.c2 = 2;
psoOptions.SParams.w_start = 0.9;
psoOptions.SParams.w_end = 0.4;
psoOptions.SParams.w_varyfor = 1;

psoOptions.Flags.ShowViz = 0;
psoOptions.Flags.Neighbor = 0;
psoOptions.Save.Interval = 0;
psoOptions.Disp.Interval = 0;


% Run experiments for the three complex functions
psoOptions.Obj.f2eval = 'Rastrigrin';
psoOptions.Obj.lb = 2.56;
psoOptions.Obj.ub = 5.12;
psoOptions.SParams.Vmax = 10;
GenExpData(numberofRuns, psoOptions);

psoOptions.Obj.f2eval = 'Griewank';
psoOptions.Obj.lb = 300;
psoOptions.Obj.ub = 600;
psoOptions.SParams.Vmax = 600;
GenExpData(numberofRuns, psoOptions);

psoOptions.Obj.f2eval = 'Rosenbrock';
psoOptions.Obj.lb = 15;
psoOptions.Obj.ub = 30;
psoOptions.SParams.Vmax = 100;
GenExpData(numberofRuns, psoOptions);

% MANAGE EXIT ACTIONS
if ExitAction
    exitString = sprintf('\n\n\t EXITING MATLAB in 10 seconds. PLEASE SAVE OPEN FILES');
    logoffStr = sprintf('\n Your COMPUTER WILL LOG OFF IN 30 seconds. PLEASE SAVE DATA');
    shutdownStr = sprintf('\n Your COMPUTER WILL SHUTDOWN IN 30 seconds. PLEASE SAVE DATA');
    
    disp( exitString );
    errordlg(exitString)
    pause(5);
    if ExitAction == 1  %Just Exit Matlab
        pause(5);
        exit;
    elseif ExitAction == 2  %Exit and Shutdown WinXP.
        disp(shutdownStr);
        errordlg(shutdownStr);
        dos('shutdown -s -f -t 30 -c "MATLAB:RunExp: The function has finished and the system will go into a planned shutdown"');
        pause(5);
        exit;
    elseif ExitAction == 3
        disp(logoffStr);
        errordlg(logoffStr);
        dos('shutdown -l -f -t 30 -c "MATLAB:RunExp: The function has finished and the system will go into a planned shutdown"');
        pause(5);
        exit;
    elseif ExitAction == 4
        disp(shutdownStr);
        errordlg(shutdownStr);
        dos('rundll32.exe shell32.dll,SHExitWindowsEx 8');
        pause(5);
        exit;
    elseif ExitAction == 4
        disp(logoffStr);
        errordlg(logoffStr);
        dos('rundll32.exe shell32.dll,SHExitWindowsEx 0');
        pause(5);
        exit;
    end

end
    
    

%-----------------------------------------------------------%
%--Run Experiments for different dimensions and SwarmSizes--%
%-----------------------------------------------------------%
function GenExpData(numberofRuns, psoOptions)
	DimIters = [10, 20,   30; ...   %Dimensions
              1000, 1500, 2000];    %Corresponding iterations
	for x = DimIters;
        psoOptions.Vars.Dim = x(1,:);
        psoOptions.Vars.Iterations = x(2,:);
        for swarmsize = [20. 40. 80]
            psoOptions.Vars.SwarmSize = swarmsize;
            RnS(numberofRuns, psoOptions);
        end
    end
    
%----------------%
%---Run & save---%
%----------------%
function RnS(numberofRuns, psoOptions)

disp(sprintf('This experiment will optimize %s function for %d times.', psoOptions.Obj.f2eval, numberofRuns));
disp(sprintf('Population Size: %d\t\tDimensions: %d.', psoOptions.Vars.SwarmSize, psoOptions.Vars.Dim));
fVal = 0;
History=[];
disp(sprintf('\nRun \t\t Best objVal'));
for i = 1:numberofRuns
    [tfxmin, xmin, Swarm, tHistory] = pso(psoOptions);
    
    fVal(i,:) = tfxmin;
    History(:,i) = tHistory;
    disp(sprintf('%4d \t\t%10f', i, tfxmin));
end
Avg = sum(fVal)/numberofRuns;
disp(sprintf('\nAvg. \t\t%10f\n\n', Avg))

fFile = strcat('f_', psoOptions.Obj.f2eval, '_', int2str(psoOptions.Vars.Dim), 'd', int2str(psoOptions.Vars.SwarmSize), 'p'); %e.g. f_Rastrigrin_10d20p
hFile = strcat('h_', psoOptions.Obj.f2eval, '_', int2str(psoOptions.Vars.Dim), 'd', int2str(psoOptions.Vars.SwarmSize), 'p');
save(fFile, 'fVal', '-ascii');
save(hFile, 'History', '-ascii');
````

</details>

#### get_psoOptions · MATLAB · c7c32f1e

- 归属算法：粒子群PSO
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于粒子群PSO中的“模型求解”。
- **执行主线**：更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：优先调用 `get_psoOptions`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`4a13ba667349f501581f0e29cb63fe3d3e99be79be11d7a5bf2a9d75ced71c19`
- 语言：MATLAB
- 符号：`get_psoOptions`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/get_psoOptions.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/pso.m`

<details>
<summary>展开原始代码</summary>

````matlab
%get_psoOptions >>   A function to get an "options structure" that is used to set various option of the PSO Algorithm.
%
% Usage          :   psoOptions = get_psoOptions
% Arguments      :   None
% Return Values  :   psoOptions--> A Matlab structure. It is further divided into the following structures.
%                       |
%                       |_Flags------> PSO FLAGS. (All flags can be set to zero to disable and a positive value to enable)
%                       |   |_ShowViz-----> Show visualization of the particles in motion. (suitable only if dimensions <= 3)
%                       |   |_Neighbor---> Use neighborhood acceleration (in addition to global acceleration)
%                       |
%                       |_Vars------> PSO VARIABLES
%                       |   |_SwarmSize--> Swarm Size. (Also known as population size)
%                       |   |_Iterations-> Maximum Iterations. (Used to terminate the algorithm. see also: Terminate element below)
%                       |   |_ErrGoal----> Error goal. (Also used to terminate the algorithm. see also: Terminate element below)
%                       |   |_Dim--------> Dimensions of the problem. This determines the particle size.
%                       |
%                       |_SParams---> STRATERGY PARAMETERS
%                       |   |_c1---------> Cognitive Acceleration
%                       |   |_c2---------> Social Acceleration
%                       |   |_c3---------> Neighborhood Acceleration
%                       |   |_w_start----> Value of velocity Weight at the begining
%                       |   |_w_end------> Value of velocity Weight at the end of the pso iterations
%                       |   |_w_varyfor--> The fraction of maximum iterations, for which w is linearly varied
%                       |   |_Vmax-------> Maximum velocity step
%                       |   |_Nhood------> Neighborhood size (nhood=1 ==> 2 neighbors, one on each side)
%                       |
%                       |_Obj-------> OBJECTIVE FUNCTION OPTIONS
%                       |   |_f2eval-----> Function/System to optimize (Type Fuzzy if u want to tune an FIS)
%                       |   |_GM---------> Value of Global Minima (Required if Terminate.Err is set. i.e error goal is (one of) the termination criteria).
%                       |   |_lb---------> Lower bounds of Initialization (You may use Asymmetrical Initialization. These bounds don't limit the search space.)
%                       |   |_ub---------> Upper bounds of Initialization (Rather, they are used to Initialize the particles. See: An Empirical Study of PSO (Ebenhart and Shi)
%                       |
%                       |_Terminate-> TERMINATION OPTIONS (Multiple options are allowed)
%                       |   |_Iters------> Use Vars.MaxIt as a termination criterion.   1=Yes, 0=No
%                       |   |_Err--------> Use Vars.ErrGoal as a termination criterion. 1=Yes, 0=No
%                       |
%                       |_Disp------> TEXT MODE DISPLAY OPTIONS
%                       |   |_Interval---> Notify about the progress after these many iterations. 0=Don't Notify
%                       |   |_Header-----> Display the PSO Options header. 0 = Hide, 1 = Show
%                       |   |_Progress---> Display the progress of the Algorithm. 0 = Hide, 1 = Show
%                       |   |_Footer-----> Display Footer (contains experimental results). 0 = Hide, 1 = Show
%                       |
%                       |_Save------> OPTIONS FOR SAVING RESULTS IN A TEXT FILE
%                       |   |_File-------------> Base name of the Output Text File. (see options below for automation options)
%                       |   |_IncludeFnName----> Prefix the name of the name of the Objective function to the file name e.g. DeJong_Results. 1=Yes, 0=No
%                       |   |_IncludeDim-------> Suffix the number of dimensions. DeJong_Results_10d. 1=Yes, 0=No
%                       |   |_IncludeSwarmSize-> Suffix the size of swarm. DeJong_Results_10d20p. 1=Yes, 0=No
%                       |   |_Interval---------> Save after this number of iterations. 0=Don't save the progress report. 
%                       |   |_Header-----------> Save the header information (also see: Disp)
%                       |   |_Footer-----------> Save the Footer information (also see: Disp)
%                       | 
%                       |_Fuzzy-----> FUZZY OPTIONS
%                           |_FIS-------------> An FIS file that contains the system to be optimize. (note: The actual file should have a .fis extension, although u may or may not include it here)
%                           |_DataFile--------> An valid Excel file containing Training Data. The FIS will be tuned to match this data.
%                           |_InitFunc--------> A function to initialize the Swarm using the FIS. (String or Function handle)
%                           |_ValidateFunc----> A function to Validate the Swarm each time particles are moved. This is required to change the co-ordinates of the particles which have bad value of membership function parameters.
%                           |_ErrorFunc-------> A function to evaluate the fitness of the fuzzy system. (note: Fitness is expressed in terms of mean square error. So, more fit functions would return a lower value of error)
%                           |_TuneInputs------> Tune the input membership functions
%                           |_TuneOutputs-----> Tune the output membership functions
%
% History        :   Author      :   JAG (Jagatpreet Singh)
%                   Created on  :   06252003 (Wednesday. 25th June, 2003)
%                   Comments    :   Enjoy!


function psoOptions = get_psoOptions()
psoOptions = struct( ...
    ... %Option FLAGS
    'Flags', struct(...
    'ShowViz',          0, ...      %Show visualization of the particles
    'Neighbor',         0), ...     %Use neighborhood acceleration (in addition to global acceleration)
    ... %Variables of the PSO
    'Vars', struct(...    
    'SwarmSize',   20, ...     %Swarm Size 
    'Iterations',  1000,...    %Maximum Iterations
    'ErrGoal',     1e-10, ...  %Error goal
    'Dim',         10 ), ...   %Dimensions of the problem
    ...  %Stratergy Parameters
    'SParams', struct(... 
    'c1',       2, ...      %Cognitive Acceleration
    'c2',       2, ...      %Social Acceleration
    'c3',       1, ...      %Neighborhood Acceleration
    'w_start',  0.95, ...   %Value of velocity Weight at the begining
    'w_end',    0.4, ...    %Value of velocity Weight at the end of the pso iterations
    'w_varyfor',0.7,...     %The fraction of maximum iterations, for which w is linearly varied
    'Vmax',     100,...     %Maximum velocity step
    'Chi',      1, ...      %Constriction factor
    'Nhood',    1 ), ...    %Neighborhood size (nhood=1 ==> 2 neighbors, one on each side)
    ...  %Objective Function Options
    'Obj', struct(...    
    'f2eval',      'DeJong', ...%Function/System to optimize
    'GM',           0, ...      %Value of Global Minima (Required if Error goal is a termination criteria).
    'lb',           100, ...    %Lower bounds of Initialization
    'ub',           200 ), ...  %Upper bounds of Initialization
    ... %Termination Options
    'Terminate', struct(...
    'Iters',        1, ...      %Use Vars.MaxIt for termination
    'Err',          1), ...     %Use Vars.ErrGoal for termintion
    ... %Display Options
    'Disp', struct( ...
    'Interval',    10, ...     %Notify about the progress after these many iterations
    'Header',      1,  ...     %Display the PSO Options header. 0 = hide, 1 = show
    'Progress',    1,  ...     %Display the progress of the Algorithm. 0 = hide, 1 = show
    'Footer',      1 ),  ...   %Display Footer (contains experimental results). 0 = hide, 1 = show
    ... %Saving Options
    'Save', struct(...
    'File',        'Results', ...  %Base name of the Output Text File. (see options below for automation options)
    'IncludeFnName',    1, ...     %Prefix the name of the name of the Objective function to the file name e.g. DeJong_Results
    'IncludeDim',       1, ...     %Suffix the number of dimensions. DeJong_Results_10d
    'IncludeSwarmSize', 1, ...     %Suffix the size of swarm. DeJong_Results_10d20p
    'Interval',         10,...     %Save after this number of iterations
    'Header',           1, ...     %Save the header information (see Disp)
    'Footer',           1 ) , ...  %Save the Footer information (see Disp)
    ... %info: the PSO Toolbox can used to tune the membership functions of an FIS. Set the options below.
    ... %Fuzzy Options 
    'Fuzzy', struct( ...
    'FIS',          'tipper', ...       %FIS file that contains the system to be optimize. (note: The file should end with a .fis extension)
    'DataFile',     'tipperData', ...   %An Excel File containing Training Data. The FIS will be tuned to match this data.
    'InitFunc',     @initfuzzy, ...     %A function to initialize the Swarm using the FIS
    'ValidateFunc', @validatefuzzy, ... %A function to Validate the Swarm each time particles are moved. This is required to change the co-ordinates of the particles which have bad value of membership function parameters.
    'ErrorFunc',    @fuzEvalFitness,... %A function to evaluate the fitness of the fuzzy system. (note: Fitness is expressed in terms of mean square error. So, more fit functions would return a lower value of error)
    'TuneInputs',    1, ...             %Tune the input membership functions
    'TuneOutputs',   1) ...             %Tune the output membership functions
    );
    
````

</details>

#### pso · MATLAB · 75e93b49

- 归属算法：粒子群PSO
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于粒子群PSO中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、控制台/过程输出、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`b53691eb62a3b656d7fbcabe4361510fb96f6cbcd7f8370a0b274495f8eefca2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/pso.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/DrawSwarm.m`

<details>
<summary>展开原始代码</summary>

````matlab
%PSO >> function for the PSO ALGORITHM
%
% USAGES:   1.) [fxmin, xmin, Swarm, history] = PSO(psoOptions);
%           2.) [fxmin, xmin, Swarm, history] = PSO;
%           3.) fxmin = PSO(psoOptions);
%           3.) PSO 
%           etc.
%
% Arguments     : psoOptions--> A Matlab stucture containing all PSO related options. (see also: get_psoOptions)
% Return Values : [fxmin, xmin, Swarm, history]
%                     |     |       |       |_The history of the algorithm. Depicts how the function value of GBest changes over the run.
%                     |     |       |_The final Swarm. (A matrix containing co-ordinates of all particles)
%                     |     |_The co-ordinates of Best (ever) particle found during the PSO's run.
%                     |__The objective value of Best (^xmin) particle.
%
%  History        :   Author      :   JAG (Jagatpreet Singh)
%                     Created on  :   05022003 (Friday. 2nd May, 2003)
%                     Comments    :   The basic PSO algorithm.
%                     Modified on :   0710003 (Thursday. 10th July, 2003)
%                     Comments    :   It uses psoOptions structure now. More organized.
%  
%                     see also: get_psoOptions
function [fxmin, xmin, Swarm, history] = PSO(psoOptions)

%Globals
global psoFlags;
global psoVars;
global psoSParameters;
global notifications;


upbnd = 600; % Upper bound for init. of the swarm
lwbnd = 300; % Lower bound for init. of the swarm
GM = 0; % Global minimum (used in the stopping criterion)
ErrGoal = 1e-10; % Desired accuracy
% 

%Initializations
if nargin == 0
    psoOptions = get_psoOptions;
end


%For Displaying 
if psoOptions.Flags.ShowViz
    global vizAxes; %Use the specified axes if using GUI or create a new global if called from command window
    vizAxes = plot(0,0, '.');
    axis([-1000 1000 -1000 1000 -1000 1000]);   %Initially set to a cube of this size
    axis square;
    grid off;
    set(vizAxes,'EraseMode','xor','MarkerSize',15); %Set it to show particles.
    pause(1);
end
%End Display initialization

% Initializing variables
success = 0; % Success Flag
iter = 0;   % Iterations' counter
fevals = 0; % Function evaluations' counter

% Using params---
% Determine the value of weight change
w_start = psoOptions.SParams.w_start;   %Initial inertia weight's value
w_end = psoOptions.SParams.w_end;       %Final inertia weight
w_varyfor = floor(psoOptions.SParams.w_varyfor*psoOptions.Vars.Iterations); %Weight change step. Defines total number of iterations for which weight is changed.
w_now = w_start;
inertdec = (w_start-w_end)/w_varyfor; %Inertia weight's change per iteration

% Initialize Swarm and Velocity
SwarmSize = psoOptions.Vars.SwarmSize;
Swarm = rand(SwarmSize, psoOptions.Vars.Dim)*(psoOptions.Obj.ub-psoOptions.Obj.lb) + psoOptions.Obj.lb;
VStep = rand(SwarmSize, psoOptions.Vars.Dim);

f2eval = psoOptions.Obj.f2eval; %The objective function to optimize.

%Find initial function values.
fSwarm = feval(f2eval, Swarm);
fevals = fevals + SwarmSize;

% Initializing the Best positions matrix and
% the corresponding function values
PBest = Swarm;
fPBest = fSwarm;

% Finding best particle in initial population
[fGBest, g] = min(fSwarm);
lastbpf = fGBest;
Best = Swarm(g,:); %Used to keep track of the Best particle ever
fBest = fGBest;
history = [0, fGBest];

if psoOptions.Flags.Neighbor
    % Define social neighborhoods for all the particles
    for i = 1:SwarmSize
        lo = mod(i-psoOptions.SParam.Nhood:i+psoOptions.SParam.Nhood, SwarmSize);
        nhood(i,:) = [lo];
    end
    nhood(find(nhood==0)) = SwarmSize; %Replace zeros with the index of last particle.
end

if psoOptions.Disp.Interval & (rem(iter, psoOptions.Disp.Interval) == 0)
    disp(sprintf('Iterations\t\tfGBest\t\t\tfevals'));
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                  THE  PSO  LOOP                          %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
while( (success == 0) & (iter <= psoOptions.Vars.Iterations) )
    iter = iter+1;
    
    % Update the value of the inertia weight w
    if (iter<=w_varyfor) & (iter > 1)
        w_now = w_now - inertdec; %Change inertia weight
    end
    
    
    %%%%%%%%%%%%%%%%%
    % The PLAIN PSO %
    
    % Set GBest
    A = repmat(Swarm(g,:), SwarmSize, 1); %A = GBest. repmat(X, m, n) repeats the matrix X in m rows by n columns.
    B = A; %B wil be nBest (best neighbor) matrix
    
    % use neighborhood model
    % circular neighborhood is used
    if psoOptions.Flags.Neighbor
        for i = 1:SwarmSize
            [fNBest(i), nb(i)] = min(fSwarm( find(nhood(i)) ));
            B(i, :) = Swarm(nb(i), :);
        end
    end
        
    % Generate Random Numbers
    R1 = rand(SwarmSize, psoOptions.Vars.Dim);
    R2 = rand(SwarmSize, psoOptions.Vars.Dim);
    
    % Calculate Velocity
    if ~psoOptions.Flags.Neighbor %Normal
        VStep = w_now*VStep + psoOptions.SParams.c1*R1.*(PBest-Swarm) + psoOptions.SParams.c2*R2.*(A-Swarm);
    else %With neighborhood
        R3 = rand(SwarmSize, psoOptions.Vars.Dim); %random nos for neighborhood
        VStep = w_now*VStep + psoOptions.SParams.c1*R1.*(PBest-Swarm) + psoOptionsSParams.c2*R2.*(A-Swarm) + psoOptionsSParams.c3*R3.*(B-Swarm);
    end
    
    % Apply Vmax Operator for v > Vmax
    changeRows = VStep > psoOptions.SParams.Vmax;
    VStep(find(changeRows)) = psoOptions.SParams.Vmax;
    % Apply Vmax Operator for v < -Vmax
    changeRows = VStep < -psoOptions.SParams.Vmax;
    VStep(find(changeRows)) = -psoOptions.SParams.Vmax;
    
    % ::UPDATE POSITIONS OF PARTICLES::
    Swarm = Swarm + psoOptions.SParams.Chi * VStep;    % Evaluate new Swarm
    
    fSwarm = feval(f2eval, Swarm);
    fevals = fevals + SwarmSize;
    
    % Updating the best position for each particle
    changeRows = fSwarm < fPBest;
    fPBest(find(changeRows)) = fSwarm(find(changeRows));
    PBest(find(changeRows), :) = Swarm(find(changeRows), :);
    
    lastbpart = PBest(g, :);
    % Updating index g
    [fGBest, g] = min(fPBest);

    %Update Best. Only if fitness has improved.
    if fGBest < lastbpf
        [fBest, b] = min(fPBest);
        Best = PBest(b,:);
    end
    
    %%OUTPUT%%
    if psoOptions.Save.Interval & (rem(iter, psoOptions.Save.Interval) == 0)
        history((size(history,1)+1), :) = [iter, fBest];
    end
    
    if psoOptions.Disp.Interval & (rem(iter, psoOptions.Disp.Interval) == 0)
        disp(sprintf('%4d\t\t\t%.5g\t\t\t%5d', iter, fGBest, fevals));
    end

    if psoOptions.Flags.ShowViz
        [fworst, worst] = max(fGBest);
        DrawSwarm(Swarm, SwarmSize, iter, psoOptions.Vars.Dim, Swarm(g,:), vizAxes);
    end
    
    %%TERMINATION%%
    if abs(fGBest-psoOptions.Obj.GM) <= psoOptions.Vars.ErrGoal     %GBest
        success = 1;
    elseif abs(fBest-psoOptions.Obj.GM)<=psoOptions.Vars.ErrGoal    %Best
        success = 1
    else
        lastbpf = fGBest; %To be used to find Best
    end

    
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                  END  OF PSO  LOOP                       %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



[fxmin, b] = min(fPBest);
xmin = PBest(b, :);

history = history(:,1);
%Comment below line to Return Swarm. Uncomment to return previous best positions.
% Swarm = PBest; %Return PBest
````

</details>

#### show_psoOptions · MATLAB · 63b622e2

- 归属算法：粒子群PSO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于粒子群PSO中的“核心算法与辅助函数”。
- **执行主线**：更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：优先调用 `show_psoOptions`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出、文件结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cd389b01f1ee4496cf5ae0c004c38b53659bf11709dd4dfa6132f5b7c3f2b6a7`
- 语言：MATLAB
- 符号：`show_psoOptions`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群工具箱 - Particle Swarm (PSO) Toolbox-beta-0.3/show_psoOptions.m`

<details>
<summary>展开原始代码</summary>

````matlab
%show_psoOptions >> A function to read and display the psoOptions structure.
%
% Usage          : strOptions = show_psoOptions( psoOptions )
% Arguments      : A structure containing various options for PSO
% Return Values  : A string containing the information abt the elements of the provided structure.
%
% History        :   Author      :   JAG (Jagatpreet Singh)
%                   Created on  :   06252003 (Wednesday. 25th June, 2003)
%                   Comments    :   A nice utility function.
%
%                   see also: get_psoOptions
%
function strOptions = show_psoOptions(IndentLevel, Variable)
if nargin < 1 disp(sprintf('\n\t:::No Options Structure provided:::\n')); return;
elseif nargin == 1 Variable = IndentLevel; IndentLevel = 1; end;

if IndentLevel < 1 IndentLevel = 1; end

subHeads = char(fieldnames(Variable));
indentTab = [sprintf('\t')];

strOptions = '';
for i=1:size(subHeads, 1)
    thisField = getfield(Variable, subHeads(i,:)); %assign the contents of the current structure element to thisField
    strOptions = [strOptions repmat(indentTab, 1, IndentLevel) subHeads(i,:)]; %Display upto the field name
    if isstruct(thisField)
        strOptions = [strOptions sprintf('\n') show_psoOptions(IndentLevel+1, thisField)]; %Write contents of the structure in next line
    else
        if ischar(thisField)
            strField = sprintf('%s', thisField);
        elseif isnumeric(thisField)
            strField = sprintf('%4.5g', thisField);
        else
            strField = sprintf(':::Can''t display item:::');
        end
        strOptions = [strOptions sprintf(' :') indentTab strField sprintf('\n')];
    end
end
        
````

</details>

#### pso1 · MATLAB · 67e765f7

- 归属算法：粒子群PSO
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于粒子群PSO中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`84bb08b9cdea548288f9f16e14599b20281b26291c98b19a935617ebc007eb06`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群算法的源代码/pso1.txt`

<details>
<summary>展开原始代码</summary>

````matlab
%%####################################################################
%%#### Particle swarm optimization
%%#### With linkage operator
%%#### Deepak devicharan july 2003
%%####################################################################

%%## to apply this to different equations do the following
%%## generate initial particles in a search space close to actual soln
%%## fool around with no of iterations, no of particles, learning rates

%%## for a truly generic PSO do the following
%%## increase the number of particles , increase the variance
%%## i.e let the particles cover a larger area of the search space
%%## then fool around as always with the above thins

%declare the parameters of the optimization

max_iterations = 1000;
no_of_particles = 50;
dimensions = 1;

delta_min = -0.003;
delta_max = 0.003;

c1 = 1.3;
c2 = 1.3;

%initialise the particles and teir velocity components

for count_x = 1:no_of_particles
for count_y = 1:dimensions
particle_position(count_x,count_y) = rand*10;
particle_velocity(count_x,count_y) = rand;
p_best(count_x,count_y) = particle_position(count_x,count_y);
end
end

%initialize the p_best_fitness array
for count = 1:no_of_particles
p_best_fitness(count) = -1000;
end

%particle_position
%particle_velocity

%main particle swrm routine
for count = 1:max_iterations

%find the fitness of each particle
%change fitness function as per equation requiresd and dimensions
for count_x = 1:no_of_particles
%x = particle_position(count_x,1);
%y = particle_position(count_x,2);
%z = particle_position(count_x,3);
%soln = x^2 - 3*y*x + z;

%x = particle_position(count_x); 
%soln = x^2-2*x+1;

x = particle_position(count_x);
soln = x-7;

if soln~=0 
current_fitness(count_x) = 1/abs(soln);
else
current_fitness =1000;
end
end

%decide on p_best etc for each particle
for count_x = 1:no_of_particles
if current_fitness(count_x) > p_best_fitness(count_x)
p_best_fitness(count_x) = current_fitness(count_x);
for count_y = 1:dimensions
p_best(count_x,count_y) = particle_position(count_x,count_y);
end
end
end

%decide on the global best among all the particles
[g_best_val,g_best_index] = max(current_fitness);

%g_best contains the position of teh global best
for count_y = 1:dimensions
g_best(count_y) = particle_position(g_best_index,count_y); 
end

%update the position and velocity compponents
for count_x = 1:no_of_particles
for count_y = 1:dimensions
p_current(count_y) = particle_position(count_x,count_y);
end

for count_y = 1:dimensions
particle_velocity(count_y) = particle_velocity(count_y) + c1*rand*(p_best(count_y)-p_current(count_y)) + c2*rand*(g_best(count_y)-p_current(count_y));
particle_positon(count_x,count_y) = p_current(count_y) +particle_velocity(count_y);
end
end


end

g_best 
current_fitness(g_best_index)

clear all, clc % pso example
iter = 1000; % number of algorithm iterations
np = 2; % number of model parameters
ns = 10; % number of sets of model parameters
Wmax = 0.9; % maximum inertial weight
Wmin = 0.4; % minimum inertial weight
c1 = 2.0; % parameter in PSO methodology
c2 = 2.0; % parameter in PSO methodology
Pmax = [10 10]; % maximum model parameter value
Pmin = [-10 -10]; % minimum model parameter value
Vmax = [1 1]; % maximum change in model parameter
Vmin = [-1 -1]; % minimum change in model parameter
modelparameters(1:np,1:ns) = 0; % set all model parameter estimates for all model parameter sets to zero
modelparameterchanges(1:np,1:ns) = 0; % set all change in model parameter estimates for all model parameter sets to zero
bestmodelparameters(1:np,1:ns) = 0; % set best model parameter estimates for all model parameter sets to zero
setbestcostfunction(1:ns) = 1e6; % set best cost function of each model parameter set to a large number
globalbestparameters(1:np) = 0; % set best model parameter values for all model parameter sets to zero
bestparameters = globalbestparameters'; % best model parameter values for all model parameter sets (to plot)
globalbestcostfunction = 1e6; % set best cost function for all model parameter sets to a large number
i = 0; % indicates ith algorithm iteration
j = 0; % indicates jth set of model parameters
k = 0; % indicates kth model parameter
for k = 1:np % initialization
for j = 1:ns
modelparameters(k,j) = (Pmax(k)-Pmin(k))*rand(1) + Pmin(k); % randomly distribute model parameters
    modelparameterchanges(k,j) = (Vmax(k)-Vmin(k))*rand(1) + Vmin(k); % randomly distribute change in model parameters
end
end
for i = 2:iter
for j = 1:ns
x = modelparameters(:,j);
% calculate cost function
costfunction = 105*(x(2)-x(1)^2)^2 + (1-x(1))^2;
    if costfunction < setbestcostfunction(j) % best cost function for jth set of model parameters
bestmodelparameters(:,j) = modelparameters(:,j);
      setbestcostfunction(j) = costfunction;
end
    if costfunction < globalbestcostfunction % best cost function for all sets of model parameters
globalbestparameters = modelparameters(:,j);
bestpar

ameters(:,i) = globalbestparameters;
     globalbestcostfunction(i) = costfunction;
else
bestparameters(:,i) = bestparameters(:,i-1);
globalbestcostfunction(i) = globalbestcostfunction(i-1);
end
end
  W = Wmax - i*(Wmax-Wmin)/iter; % compute inertial weight
for j = 1:ns % update change in model parameters and model parameters
    for k = 1:np
      modelparameterchanges(k,j) = W*modelparameterchanges(k,j) + c1*rand(1)*(bestmodelparameters(k,j)-modelparameters(k,j))...
         + c2*rand(1)*(globalbestparameters(k) - modelparameters(k,j));
      if modelparameterchanges(k,j) < -Vmax(k), modelparameters(k,j) = modelparameters(k,j) - Vmax(k); end
if modelparameterchanges(k,j) > Vmax(k), modelparameters(k,j) = modelparameters(k,j) + Vmax(k); end
if modelparameterchanges(k,j) > -Vmax(k) & modelparameterchanges(k,j) < Vmax(k), modelparameters(k,j) = modelparameters(k,j) + modelparameterchanges(k,j); end
      if modelparameters(k,j) < Pmin(k), modelparameters(k,j) = Pmin(k); end
      if modelparameters(k,j) > Pmax(k), modelparameters(k,j) = Pmax(k); end
end
end
i
end
bp = bestparameters; index = linspace(1,iter,iter);
figure; semilogy(globalbestcostfunction,'k');
set(gca,'FontName','Arial','Fontsize',14); axis tight;
xlabel('iteration'); ylabel('cost function');
figure; q = plot(index,bp(1,,'k-',index,bp(2,,'k:');
set(gca,'FontName','Arial','Fontsize',14); axis tight;
legend(q,'x_1','x_2'); xlabel('iteration'); ylabel('parameter')
````

</details>

#### pso2 · C++ · 8a112b75

- 归属算法：粒子群PSO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于粒子群PSO中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`9c631016ea1f095d4fa4c939d81447722d4183bb43799ab922aee4513331febd`
- 语言：C++
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群算法的源代码/pso2.txt`

<details>
<summary>展开原始代码</summary>

````cpp
一个pso程序的源代码。在vc.net2003下面通过。

建议：看代码之前，请先弄明白pso是怎么回事。然后请对应着来：程序中用Agent代表一只鸟，PSO代表鸟群。阅读源代码，不要顺着看，先看main(),然后按照出现的东西的顺序，一个一个得来，呵呵，纯粹是建议。

// PSO.cpp : 定义控制台应用程序的入口点。
//粒子群优化算法基本程序
//你可以使用本代码，如果感到对你有用的话，请通知作者，作者会很高兴。
//通讯地址：fashionxu@163.com
//by FashionXu

//本程序在vc++.net 2003下面通过，你如果要在vc6.0下面使用，请查阅相关资料修改，或者联系作者
#include "stdafx.h"
#include "iostream"
#define _USE_MATH_DEFINES
#include "math.h"
#include 

const int  iAgentDim=20;//优化函数的维数
const double iRangL=-30;//函数的取值范围
const double iRangR=30;

const int iPSONum=20;//粒子数

int iStep=10000;//跌代次数
//下面的值，要具体程序中具体的修改，根据你优化的函数来修改
double w=0.9;//惯性系数
const double delta1=1;//1.494;//加速度
const double delta2=1;//1.494;

#define rnd(low,uper)((rand()/(double)RAND_MAX)*((uper)-(low))+(low))//这个东西，返回low ,uper之间的一个值
double gbest[iAgentDim];//global best fitness保留全局最优值的坐标
using namespace std;


class Agent//这个类表示单个的粒子，也就是一只鸟  ：）
{
public:
 double dpos[iAgentDim];   //位置，也就是各个维数的值
 double dpbest[iAgentDim];       //维护一个“自己”找到的最优值的解
 double dv[iAgentDim];   //速度
 double m_dFitness;//agent's fitness  当前算出的一个值
 double m_dBestfitness;//agent's best fitness  自己已经找到的最好值

 Agent()//初始化
 { 
  srand( (unsigned)(time( NULL )+rand()) );
  int i=0;
  for(;i<IAGENTDIM;I++)
  {
   dpos[i]=rnd(iRangL,iRangR);
   dv[i]=dpbest[i]=dpos[i];
  }
 }
 void UpdateFitness()
  /*calculate the fitness and find out the best fitness,record*/
 {
  
  double sum1=0;
  double sum2=0;

/*Ackley Funtion*/ 

 for (int i=0;i {
  sum1+=(dpos [i]*dpos [i]);
  sum2+=cos(2*M_PI*dpos [i]);
 }

 m_dFitness=(-20*exp(-0.2*(sqrt((1.0/(double)iAgentDim *sum1))))-exp((1.0/(double)iAgentDim )*sum2)+20+M_E);
 //The Rastrigin function
  //int i=0;
  //for (;i<IAGENTDIM;I++)
  //{
  // sum1+=(dpos [i]*dpos [i])-3.0*cos(2*M_PI*dpos [i]);
  //}
  //m_dFitness=3.0*iAgentDim+sum1;

  //找到一个更好的值后，更新 m_dBestfitness
  if (m_dFitness  {
   m_dBestfitness=m_dFitness;
   int i=0;
   for(;i<IAGENTDIM;I++)
   {
    dpbest[i]=dpos[i];
   }
  }
  
 }
 void UpdatePos()//agent moving
 {
  int i=0;

  for(;i<IAGENTDIM;I++)
  {

//   basi pso
  dv[i]=w*dv[i]+delta1*rnd(0,1)*(dpbest[i]-dpos[i])+delta2*rnd(0,1)*(gbest[i]-dpos[i]);
   dpos[i]+=dv[i];
  }

 }
};
class PSO//这是粒子群，也就是鸟群了
{
private:
 Agent agents[iPSONum];
 double m_dBestFitness;//鸟群找到的最优值
 int m_iTempPos;
public:
 void Init();
 void Search();
};
void PSO::Search()
{
 int k=0; 

 while( k<ISTEP)
 {
  m_iTempPos=999;
  int i;
  for(i=0;i<IPSONUM;I++)
  {//此处是找找鸟群中有没有更好的解，如果有，记录下来
   if (m_dBestFitness>agents[i].m_dBestfitness ) 
   {
    m_dBestFitness=agents[i].m_dBestfitness;
    m_iTempPos=i;//找到到的最好解的位置
   }
  }
  if (m_iTempPos!=999)
  {
   int j;

   for(j=0;j<IAGENTDIM;J++)
   {
    gbest[j]=agents[m_iTempPos].dpos[j];//记录全局最优解的各个坐标
   }
  }
  //printf("The best is %f \n",m_dBestFitness);
  //下一次跌代
  for(i=0;i<IPSONUM;I++)
  { 
   agents[i].UpdatePos();
   agents[i].UpdateFitness ();
  }   
  k++;

 }
  printf("The best result is: %2.15f    after %d step. \n",m_dBestFitness,k);

 {
  for (int i=0;i<IAGENTDIM;I++)
   printf(" %2.15f ",gbest[i]);
 }
 }

void PSO::Init()//初始化，
{
 int i=0;
 m_dBestFitness=100000;
 srand( (unsigned)(time( NULL )+rand()) ); 
 for(;i<IPSONUM;I++)
 { 
  agents[i].m_dBestfitness =100000;//将m_dBestfitness赋值为一个大的值，目的是找最小值，
  agents[i].UpdateFitness();
 }
}
int main(int argc, char* argv[])
{
 PSO pso;
 pso.Init ();
 pso.Search();
 printf("\n");
 char c;
 scanf("%c",&c);
 return 0;
}
````

</details>

#### 智能算法之粒子群优化算法代码 · MATLAB · 2c4687c4

- 归属算法：粒子群PSO
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#粒子群PSO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于粒子群PSO中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`f30a59e5a81945ce506385ba72f12516e78f62fbc2a0d20038ecde0b8e055ae4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/智能算法之粒子群优化算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
粒子群算法基本步骤
1 找出待优化的目标函数
2 设定种群规模大小（不会设置可直接采用下方代码的）
3 替换掉下方公式即可

%% 初始化种群  
f= @(x)x .* sin(x) .* cos(2 * x) - 2 * x .* sin(3 * x); % 函数表达式    % 求这个函数的最大值  
figure(1);ezplot(f,[0,0.01,20]);  
N = 50;                         % 初始种群个数  
d = 1;                          % 空间维数  
ger = 100;                      % 最大迭代次数       
limit = [0, 20];                % 设置位置参数限制  
vlimit = [-1, 1];               % 设置速度限制  
w = 0.8;                        % 惯性权重  
c1 = 0.5;                       % 自我学习因子  
c2 = 0.5;                       % 群体学习因子   
for i = 1:d  
    x = limit(i, 1) + (limit(i, 2) - limit(i, 1)) * rand(N, d);%初始种群的位置  
end  
v = rand(N, d);                  % 初始种群的速度  
xm = x;                          % 每个个体的历史最佳位置  
ym = zeros(1, d);                % 种群的历史最佳位置  
fxm = zeros(N, 1);               % 每个个体的历史最佳适应度  
fym = -inf;                      % 种群历史最佳适应度  
hold on  
plot(xm, f(xm), 'ro');title('初始状态图');  
figure(2)  
%% 群体更新  
iter = 1;  
record = zeros(ger, 1);          % 记录器  
while iter <= ger  
     fx = f(x) ; % 个体当前适应度     
     for i = 1:N        
        if fxm(i) < fx(i)  
            fxm(i) = fx(i);     % 更新个体历史最佳适应度  
            xm(i,:) = x(i,:);   % 更新个体历史最佳位置  
        end   
     end  
if fym < max(fxm)  
        [fym, nmax] = max(fxm);   % 更新群体历史最佳适应度  
        ym = xm(nmax, :);      % 更新群体历史最佳位置  
 end  
    v = v * w + c1 * rand * (xm - x) + c2 * rand * (repmat(ym, N, 1) - x);% 速度更新  
    % 边界速度处理  
    v(v > vlimit(2)) = vlimit(2);  
    v(v < vlimit(1)) = vlimit(1);  
    x = x + v;% 位置更新  
    % 边界位置处理  
    x(x > limit(2)) = limit(2);  
    x(x < limit(1)) = limit(1);  
    record(iter) = fym;%最大值记录  
     x0 = 0 : 0.01 : 20;  
     plot(x0, f(x0), 'b-', x, f(x), 'ro');title('状态位置变化')  
    pause(0.1)  
    iter = iter+1;  
end  
figure(3);plot(record);title('收敛过程')  
x0 = 0 : 0.01 : 20;  
figure(4);plot(x0, f(x0), 'b-', x, f(x), 'ro');title('最终状态位置')  
disp(['最大值：',num2str(fym)]);  
disp(['变量取值：',num2str(ym)]);  
````

</details>

### 蚁群算法ACO · 实现

#### 蚁群算法matlab源码 · MATLAB · e3cd9190

- 归属算法：蚁群算法ACO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#蚁群算法ACO · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于蚁群算法ACO中的“核心算法与辅助函数”。
- **执行主线**：按信息素概率构造解并迭代强化优良路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0a36a33ce293a86437133fde3d9756267c7b08bdebb29e23a3172429b8c77083`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/蚁群算法matlab源码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function [Shortest_Route,Shortest_Length]=ACATSP(D,NC_max,m,Alpha,Beta,Rho,Q)
%%=========================================================================
%% ACATSP.m
%% Ant Colony Algorithm for Traveling Salesman Problem
%% ChengAihua,PLA Information Engineering University,ZhengZhou,China
%% Email:aihuacheng@gmail.com
%% All rights reserved
%%-------------------------------------------------------------------------
%% 主要符号说明
%% C n个城市的坐标，n×2的矩阵
%% NC_max 最大迭代次数
%% m 蚂蚁个数
%% Alpha 表征信息素重要程度的参数
%% Beta 表征启发式因子重要程度的参数
%% Rho 信息素蒸发系数
%% Q 信息素增加强度系数
%% R_best 各代最佳路线
%% L_best 各代最佳路线的长度
%% L_ave  各代路线的平均长度
%%=========================================================================

%%第一步：变量初始化
n=size(D,1);
for i=1:n
    D(i,i)=eps;
end
Eta=1./D;%Eta为启发因子，这里设为距离的倒数
Tau=ones(n,n);%Tau为信息素矩阵
Tabu=zeros(m,n);%存储并记录路径的生成
NC=1;%迭代计数器
R_best=zeros(NC_max,n);%各代最佳路线
L_best=inf.*ones(NC_max,1);%各代最佳路线的长度
L_ave=zeros(NC_max,1);%各代路线的平均长度

while NC<=NC_max%停止条件之一：达到最大迭代次数
%%第二步：将m只蚂蚁放到n个城市上
    Randpos=[];
    for i=1:(ceil(m/n))
        Randpos=[Randpos,randperm(n)];
    end
    Tabu(:,1)=(Randpos(1,1:m))';
    
%%第三步：m只蚂蚁按概率函数选择下一座城市，完成各自的周游
    for j=2:n
        for i=1:m
            visited=Tabu(i,1:(j-1));%已访问的城市
            J=zeros(1,(n-j+1));%待访问的城市
            P=J;%待访问城市的选择概率分布
            Jc=1;
            for k=1:n
                if length(find(visited==k))==0
                    J(Jc)=k;
                    Jc=Jc+1;
                end
            end
            %下面计算待选城市的概率分布
            for k=1:length(J)
                P(k)=(Tau(visited(end),J(k))^Alpha)*(Eta(visited(end),J(k))^Beta);%（信息素^信息素系数）*（启发因子^启发因子系数）
            end
            P=P/(sum(P));
            %按概率原则选取下一个城市
            Pcum=cumsum(P);
            Select=find(Pcum>=rand);
            to_visit=J(Select(1));
            Tabu(i,j)=to_visit;
        end
    end
    if NC>=2
        Tabu(1,:)=R_best(NC-1,:);
    end

%%第四步：记录本次迭代最佳路线
    L=zeros(m,1);
    for i=1:m
        R=Tabu(i,:);
        for j=1:(n-1)
            L(i)=L(i)+D(R(j),R(j+1));
        end
        L(i)=L(i)+D(R(1),R(n));
    end
    L_best(NC)=min(L);
    pos=find(L==L_best(NC));
    R_best(NC,:)=Tabu(pos(1),:);
    L_ave(NC)=mean(L);
    NC=NC+1

%%第五步：更新信息素
    Delta_Tau=zeros(n,n);
    for i=1:m
        for j=1:(n-1)
            Delta_Tau(Tabu(i,j),Tabu(i,j+1))=Delta_Tau(Tabu(i,j),Tabu(i,j+1))+Q/L(i);
        end
        Delta_Tau(Tabu(i,n),Tabu(i,1))=Delta_Tau(Tabu(i,n),Tabu(i,1))+Q/L(i);
    end
    Tau=(1-Rho).*Tau+Delta_Tau;

%%第六步：禁忌表清零
    Tabu=zeros(m,n);
end

%%第七步：输出结果
Pos=find(L_best==min(L_best));
Shortest_Route=R_best(Pos(1),:)
Shortest_Length=L_best(Pos(1))
````

</details>

### 遗传算法GA · 实现

使用选择、交叉和变异搜索复杂或非凸优化问题的近似最优解。

#### anli12_2 · MATLAB · 6b8d3aad

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`b7445300b280dfafdada056590ae4b4bbd62d5b8509442d495eee2b2865980fd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/anli12_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
sj0=load('sj.txt');       %加载100个目标的数据
x=sj0(:,1:2:8); x=x(:);
y=sj0(:,2:2:8); y=y(:);
sj=[x y]; d1=[70,40]; 
sj=[d1;sj;d1]; sj=sj*pi/180;  %单位化成弧度
d=zeros(102); %距离矩阵d的初始值
for i=1:101
  for j=i+1:102
  d(i,j)=6370*acos(cos(sj(i,1)-sj(j,1))*cos(sj(i,2))*cos(sj(j,2))+sin(sj(i,2))*sin(sj(j,2)));
  end
end
d=d+d'; w=50; g=100; %w为种群的个数，g为进化的代数
rand('state',sum(clock)); %初始化随机数发生器
for k=1:w  %通过改良圈算法选取初始种群
    c=randperm(100); %产生1，...，100的一个全排列  
    c1=[1,c+1,102]; %生成初始解
    for t=1:102 %该层循环是修改圈 
        flag=0; %修改圈退出标志
    for m=1:100
      for n=m+2:101
        if d(c1(m),c1(n))+d(c1(m+1),c1(n+1))<d(c1(m),c1(m+1))+d(c1(n),c1(n+1))
           c1(m+1:n)=c1(n:-1:m+1);  flag=1; %修改圈
        end
      end
    end
   if flag==0
      J(k,c1)=1:102; break %记录下较好的解并退出当前层循环
   end
   end
end
J(:,1)=0; J=J/102; %把整数序列转换成[0,1]区间上的实数，即转换成染色体编码
for k=1:g  %该层循环进行遗传算法的操作 
    A=J; %交配产生子代B的初始染色体
    c=randperm(w); %产生下面交叉操作的染色体对 
    for i=1:2:w  
        F=2+floor(100*rand(1)); %产生交叉操作的地址
        temp=A(c(i),[F:102]); %中间变量的保存值
        A(c(i),[F:102])=A(c(i+1),[F:102]); %交叉操作
        A(c(i+1),F:102)=temp;  
    end
    by=[];  %为了防止下面产生空地址，这里先初始化
while ~length(by)
    by=find(rand(1,w)<0.1); %产生变异操作的地址
end
B=A(by,:); %产生变异操作的初始染色体
for j=1:length(by)
   bw=sort(2+floor(100*rand(1,3)));  %产生变异操作的3个地址
   B(j,:)=B(j,[1:bw(1)-1,bw(2)+1:bw(3),bw(1):bw(2),bw(3)+1:102]); %交换位置
end
   G=[J;A;B]; %父代和子代种群合在一起
   [SG,ind1]=sort(G,2); %把染色体翻译成1，...,102的序列ind1
   num=size(G,1); long=zeros(1,num); %路径长度的初始值
   for j=1:num
       for i=1:101
           long(j)=long(j)+d(ind1(j,i),ind1(j,i+1)); %计算每条路径长度
       end
   end
     [slong,ind2]=sort(long); %对路径长度按照从小到大排序
     J=G(ind2(1:w),:); %精选前w个较短的路径对应的染色体
end
path=ind1(ind2(1),:), flong=slong(1)  %解的路径及路径长度
xx=sj(path,1);yy=sj(path,2);
plot(xx,yy,'-o') %画出路径
````

</details>

#### anli12_3 · MATLAB · 17b6f67c

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`3cbc6b7401c73617ba3a512a7831edf58b3578675f11b4c938afce3620281005`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/anli12_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
tic  %计时开始
clc,clear
sj0=load('sj.txt');       %加载100个目标的数据
x=sj0(:,1:2:8); x=x(:);
y=sj0(:,2:2:8); y=y(:);
sj=[x y]; d1=[70,40]; 
sj=[d1;sj;d1]; sj=sj*pi/180;  %单位化成弧度
d=zeros(102); %距离矩阵d的初始值
for i=1:101
  for j=i+1:102
  d(i,j)=6370*acos(cos(sj(i,1)-sj(j,1))*cos(sj(i,2))*cos(sj(j,2))+sin(sj(i,2))*sin(sj(j,2)));
  end
end
d=d+d'; w=50; g=100; %w为种群的个数，g为进化的代数
rand('state',sum(clock)); %初始化随机数发生器
for k=1:w  %通过改良圈算法选取初始种群
    c=randperm(100); %产生1，...，100的一个全排列  
    c1=[1,c+1,102]; %生成初始解
    for t=1:102 %该层循环是修改圈 
        flag=0; %修改圈退出标志
    for m=1:100
      for n=m+2:101
        if d(c1(m),c1(n))+d(c1(m+1),c1(n+1))<d(c1(m),c1(m+1))+d(c1(n),c1(n+1))
           c1(m+1:n)=c1(n:-1:m+1);  flag=1; %修改圈
        end
      end
    end
   if flag==0
      J(k,c1)=1:102; break %记录下较好的解并退出当前层循环
   end
   end
end
J(:,1)=0; J=J/102; %把整数序列转换成[0,1]区间上的实数，即转换成染色体编码
for k=1:g  %该层循环进行遗传算法的操作 
    A=J; %交配产生子代B的初始染色体
    for i=1:2:w
        ch1(1)=rand; %混沌序列的初始值
        for j=2:50
            ch1(j)=4*ch1(j-1)*(1-ch1(j-1)); %产生混沌序列
        end
        ch1=2+floor(100*ch1); %产生交叉操作的地址
        temp=A(i,ch1); %中间变量的保存值
        A(i,ch1)=A(i+1,ch1); %交叉操作
        A(i+1,ch1)=temp;
    end
    by=[];  %为了防止下面产生空地址，这里先初始化
while ~length(by)
    by=find(rand(1,w)<0.1); %产生变异操作的地址
end
num1=length(by); B=J(by,:); %产生变异操作的初始染色体
ch2=rand;  %产生混沌序列的初始值
for t=2:2*num1 
       ch2(t)=4*ch2(t-1)*(1-ch2(t-1)); %产生混沌序列
end
for j=1:num1
   bw=sort(2+floor(100*rand(1,2)));  %产生变异操作的2个地址
   B(j,bw)=ch2([j,j+1]); %bw处的两个基因发生了变异
end
   G=[J;A;B]; %父代和子代种群合在一起
   [SG,ind1]=sort(G,2); %把染色体翻译成1，...,102的序列ind1
   num2=size(G,1); long=zeros(1,num2); %路径长度的初始值
   for j=1:num2
       for i=1:101
           long(j)=long(j)+d(ind1(j,i),ind1(j,i+1)); %计算每条路径长度
       end
   end
     [slong,ind2]=sort(long); %对路径长度按照从小到大排序
     J=G(ind2(1:w),:); %精选前w个较短的路径对应的染色体
end
path=ind1(ind2(1),:), flong=slong(1)  %解的路径及路径长度
toc  %计时结束
xx=sj(path,1);yy=sj(path,2);
plot(xx,yy,'-o') %画出路径
````

</details>

#### 粒子群算法的源代码 · C++ · f596c6b5

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；更新粒子速度与位置进行群体优化；按信息素概率构造解并迭代强化优良路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`cd655386b1170e4e66555dae5f75c083b1b766846f8fa1c69b2c6839d6553741`
- 语言：C++
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/蚁群算法/粒子群算法的源代码/粒子群算法的源代码.txt`

<details>
<summary>展开原始代码</summary>

````cpp
所述，PSO模拟鸟群的捕食行为。设想这样一个场景：一群鸟在随机搜索食物。在这个区域里只有一块食物。所有的鸟都不知道食物在那里。但是他们知道当前的位置离食物还有多远。那么找到食物的最优策略是什么呢。最简单有效的就是搜寻目前离食物最近的鸟的周围区域。 

　　PSO从这种模型中得到启示并用于解决优化问题。PSO中，每个优化问题的解都是搜索空间中的一只鸟。我们称之为“粒子”。所有的粒子都有一个由被优化的函数决定的适应值(fitness value)，每个粒子还有一个速度决定他们飞翔的方向和距离。然后粒子们就追随当前的最优粒子在解空间中搜索。 


　　PSO 初始化为一群随机粒子(随机解)。然后通过迭代找到最优解。在每一次迭代中，粒子通过跟踪两个"极值"来更新自己。第一个就是粒子本身所找到的最优解，这个解叫做个体极值pBest。另一个极值是整个种群目前找到的最优解，这个极值是全局极值gBest。另外也可以不用整个种群而只是用其中一部分作为粒子的邻居，那么在所有邻居中的极值就是局部极值。 


　　在找到这两个最优值时，粒子根据如下的公式来更新自己的速度和新的位置：


　　v[] = w * v[] + c1 * rand() * (pbest[] - present[]) + c2 * rand() * (gbest[] - present[])            (a) 


　　present[] = persent[] + v[]                                                                                                  (b) 


　　v[] 是粒子的速度, w是惯性权重,persent[] 是当前粒子的位置. pbest[] and gbest[] 如前定义 rand () 是介于（0， 1）之间的随机数. c1, c2 是学习因子. 通常 c1 = c2 = 2. 


　　程序的伪代码如下 


　　For each particle 


　　____Initialize particle 


　　END 


　　Do 


　　____For each particle 


　　________Calculate fitness value 


　　________If the fitness value is better than the best fitness value (pBest) in history 


　　____________set current value as the new pBest 


　　____End 


　　____Choose the particle with the best fitness value of all the particles as the gBest 


　　____For each particle 


　　________Calculate particle velocity according equation (a) 


　　________Update particle position according equation (b) 


　　____End 


　　While maximum iterations or minimum error criteria is not attained 


　　在每一维粒子的速度都会被限制在一个最大速度Vmax，如果某一维更新后的速度超过用户设定的Vmax，那么这一维的速度就被限定为Vmax

[遗传算法和 PSO 的比较]

　大多数演化计算技术都是用同样的过程 ：

　　1. 种群随机初始化 

　　2. 对种群内的每一个个体计算适应值(fitness value).适应值与最优解的距离直接有关 

　　3. 种群根据适应值进行复制 

　　4. 如果终止条件满足的话，就停止，否则转步骤2 

　　从以上步骤，我们可以看到PSO和GA有很多共同之处。两者都随机初始化种群，而且都使用适应值来评价系统，而且都根据适应值来进行一定的随机搜索。两个系统都不是保证一定找到最优解 。

　　但是，PSO 没有遗传操作如交叉(crossover)和变异(mutation). 而是根据自己的速度来决定搜索。粒子还有一个重要的特点，就是有记忆。 

　　与遗传算法比较, PSO 的信息共享机制是很不同的. 在遗传算法中，染色体(chromosomes) 互相共享信息，所以整个种群的移动是比较均匀的向最优区域移动. 在PSO中, 只有gBest (or lBest) 给出信息给其他的粒子，这是单向的信息流动. 整个搜索更新过程是跟随当前最优解的过程. 与遗传算法比较, 在大多数的情况下，所有的粒子可能更快的收敛于最优解

[人工神经网络 和 PSO　]　

       神经网络(ANN)是模拟大脑分析过程的简单数学模型，反向转播算法是最流行的神经网络训练算法。进来也有很多研究开始利用演化计算(evolutionary computation)技术来研究人工神经网络的各个方面。 

　　演化计算可以用来研究神经网络的三个方面：网络连接权重，网络结构(网络拓扑结构，传递函数)，网络学习算法。 

　　不过大多数这方面的工作都集中在网络连接权重，和网络拓扑结构上。在GA中，网络权重和/或拓扑结构一般编码为染色体(Chromosome)，适应函数(fitness function)的选择一般根据研究目的确定。例如在分类问题中，错误分类的比率可以用来作为适应值 

　　演化计算的优势在于可以处理一些传统方法不能处理的例子例如不可导的节点传递函数或者没有梯度信息存在。但是缺点在于：在某些问题上性能并不是特别好。2. 网络权重的编码而且遗传算子的选择有时比较麻烦 

　　最近已经有一些利用PSO来代替反向传播算法来训练神经网络的论文。研究表明PSO 是一种很有潜力的神经网络算法。PSO速度比较快而且可以得到比较好的结果。而且还没有遗传算法碰到的问题 

　　这里用一个简单的例子说明PSO训练神经网络的过程。这个例子使用分类问题的基准函数(Benchmark function)IRIS数据集。(Iris 是一种鸢尾属植物) 在数据记录中，每组数据包含Iris花的四种属性：萼片长度，萼片宽度，花瓣长度，和花瓣宽度，三种不同的花各有50组数据. 这样总共有150组数据或模式。 

　　我们用3层的神经网络来做分类。现在有四个输入和三个输出。所以神经网络的输入层有4个节点，输出层有3个节点我们也可以动态调节隐含层节点的数目，不过这里我们假定隐含层有6个节点。我们也可以训练神经网络中其他的参数。不过这里我们只是来确定网络权重。粒子就表示神经网络的一组权重，应该是4*6+6*3=42个参数。权重的范围设定为[-100，100] (这只是一个例子，在实际情况中可能需要试验调整).在完成编码以后，我们需要确定适应函数。对于分类问题，我们把所有的数据送入神经网络，网络的权重有粒子的参数决定。然后记录所有的错误分类的数目作为那个粒子的适应值。现在我们就利用PSO来训练神经网络来获得尽可能低的错误分类数目。PSO本身并没有很多的参数需要调整。所以在实验中只需要调整隐含层的节点数目和权重的范围以取得较好的分类效果。

[PSO的参数设置]　

       面的例子我们可以看到应用PSO解决优化问题的过程中有两个重要的步骤: 问题解的编码和适应度函数 

　　PSO的一个优势就是采用实数编码, 不需要像遗传算法一样是二进制编码(或者采用针对实数的遗传操作.例如对于问题 f(x) = x1^2 + x2^2+x3^2 求解, 粒子可以直接编码为 (x1, x2, x3), 而适应度函数就是f(x). 接着我们就可以利用前面的过程去寻优.这个寻优过程是一个叠代过程, 中止条件一般为设置为达到最大循环数或者最小错误 

　　PSO中并没有许多需要调节的参数,下面列出了这些参数以及经验设置 

　　粒子数: 一般取 20 – 40. 其实对于大部分的问题10个粒子已经足够可以取得好的结果, 不过对于比较难的问题或者特定类别的问题, 粒子数可以取到100 或 200 

　　粒子的长度: 这是由优化问题决定, 就是问题解的长度 

　　粒子的范围: 由优化问题决定,每一维可是设定不同的范围 

　　Vmax: 最大速度,决定粒子在一个循环中最大的移动距离,通常设定为粒子的范围宽度,例如上面的例子里,粒子 (x1, x2, x3) x1 属于 [-10, 10], 那么 Vmax 的大小就是 20 

　  习因子: c1 和 c2 通常等于 2. 不过在文献中也有其他的取值. 但是一般 c1 等于 c2 并且范围在0和4之间 

　　中止条件: 最大循环数以及最小错误要求. 例如, 在上面的神经网络训练例子中, 最小错误可以设定为1个错误分类, 最大循环设定为2000, 这个中止条件由具体的问题确定. 

　　全局PSO和局部PSO: 我们介绍了两种版本的粒子群优化算法: 全局版和局部版. 前者速度快不过有时会陷入局部最优. 后者收敛速度慢一点不过很难陷入局部最优. 在实际应用中, 可以先用全局PSO找到大致的结果,再有局部PSO进行搜索. 

　　另外的一个参数是惯性权重, Shi 和Eberhart指出(A modified particle swarm optimizer,1998)：当Vmax很小时（对schaffer的f6函数，Vmax<=2),使用接近于1的惯性权重;当Vmax不是很小时（对schaffer的f6函数，Vmax>=3),使用权重w=0.8较好.如果没有Vmax的信息,使用0.8作为权重也是一种很好的选择.另外,对于使用时变的权重,结果不清楚,但是预计结果应比较好.

　　附上一个C++实现的C++代码：

　　代码来自2008年数学建模东北赛区B题

　　#include "stdafx.h"

　　#include <math.h>

　　#include <time.h>

　　#include <iostream>

　　#include <fstream>

　　using namespace std;

　　int c1=2; //加速因子

　　int c2=2; //加速因子

　　double w=1; //惯性权重

　　double Wmax=1; //最大惯性权重

　　double Wmin=0.6; //最小惯性权重

　　int Kmax=110; //迭代次数

　　int GdsCnt; //物资总数

　　int const Dim=10; //粒子维数

　　int const PNum=50; //粒子个数

　　int GBIndex=0; //最优粒子索引

　　double a=0.6; //适应度调整因子

　　double b=0.5; //适应度调整因子

　　int Xup[Dim]; //粒子位置上界数组

　　int Xdown[Dim]=; //粒子位置下界数组

　　int Value[Dim]; //初始急需度数组

　　int Vmax[Dim]; //最大速度数组

　　class PARTICLE; //申明粒子节点

　　void Check(PARTICLE&,int); //约束函数

　　void Input(ifstream&); //输入变量

　　void Initial(); //初始化相关变量

　　double GetFit(PARTICLE&); //计算适应度

　　void CalculateFit(); //计算适应度

　　void BirdsFly(); //粒子飞翔

　　void Run(ofstream&,int=2000); //运行函数

　　//微粒类

　　class PARTICLE

　　{


　　public:


　　int X[Dim]; //微粒的坐标数组


　　int XBest[Dim]; //微粒的最好位置数组


　　int V[Dim]; //粒子速度数组


　　double Fit; //微粒适合度


　　double FitBest; //微粒最好位置适合度


　　};


　　PARTICLE Parr[PNum]; //粒子数组


　　int main() //主函数


　　{


　　ofstream outf("out.txt");


　　ifstream inf("data.txt"); //关联输入文件


　　inf>>GdsCnt; //输入物资总数


　　Input(inf);


　　Initial();


　　Run(outf,100);


　　system("pause");


　　return 0;


　　}


　　void Check(PARTICLE& p,int count)//参数:p粒子对象,count物资数量


　　{


　　srand((unsigned)time(NULL));


　　int sum=0;


　　for (int i=0;i<Dim;i++)


　　{


　　if (p.X>Xup)


　　{


　　p.X=Xup;


　　}


　　else if (p.X<Xdown)


　　{


　　p.X=Xdown;


　　}


　　if (p.V>Vmax)


　　{


　　p.V=Vmax;


　　}


　　else if (p.V<0)


　　{


　　p.V=0;


　　}


　　sum+=p.X;


　　}


　　while (sum>count)


　　{


　　p.X[rand()%Dim]--;


　　sum=0;


　　for (int i=0;i<Dim;i++)


　　{


　　if (p.X>Xup)


　　{


　　p.X=Xup;


　　}


　　else if (p.X<Xdown)


　　{


　　p.X=Xdown;


　　}


　　if (p.V>Vmax)


　　{


　　p.V=Vmax;


　　}


　　else if (p.V<0)


　　{


　　p.V=0;


　　}


　　sum+=p.X;


　　}


　　}


　　}


　　void Input(ifstream& inf) //以inf为对象输入数据


　　{


　　for (int i=0;i<Dim;i++)


　　{


　　inf>>Xup;


　　}


　　for (int i=0;i<Dim;i++)


　　{


　　inf>>Value;


　　}


　　}


　　void Initial() //初始化数据


　　{


　　GBIndex=0;


　　srand((unsigned)time(NULL));//初始化随机函数发生器


　　for (int i=0;i<Dim;i++)


　　{


　　Vmax=(int)((Xup-Xdown)*0.035);


　　}


　　for (int i=0;i {


　　for (int j=0;j<Dim;j++)


　　{


　　Parr.X[j]=(int)(rand()/(double)RAND_MAX*(Xup[j]


　　-Xdown[j])-Xdown[j]+0.5);


　　Parr.XBest[j]=Parr.X[j];


　　Parr.V[j]=(int)(rand()/(double)RAND_MAX*(Vmax[j] -Vmax[j]/2));


　　}


　　Parr.Fit=GetFit(Parr);


　　Parr.FitBest=Parr.Fit;


　　if (Parr.Fit>Parr[GBIndex].Fit)


　　{


　　GBIndex=i;


　　}


　　}


　　}


　　double GetFit(PARTICLE& p)//计算对象适应度


　　{


　　double sum=0;


　　for (int i=0;i<Dim;i++)


　　{


　　for (int j=1;j<=p.X;j++)


　　{


　　sum+=(1-(j-1)*a/(Xup-b))*Value;


　　}


　　}


　　return sum;


　　}


　　void CalculateFit()//计算数组内各粒子的适应度


　　{


　　for (int i=0;i {


　　Parr.Fit=GetFit(Parr);


　　}


　　}


　　void BirdsFly()//粒子飞行寻找最优解


　　{


　　srand((unsigned)time(NULL));


　　static int k=10;


　　w=Wmax-k*(Wmax-Wmin)/Kmax;


　　k++;


　　for (int i=0;i {


　　for (int j=0;j<Dim;j++)


　　{


　　Parr.V[j]=(int)(w*Parr.V[j])


　　+(int)(c1*rand()/(double)RAND_MAX*


　　(Parr.XBest[j]-Parr.X[j])


　　+c2*rand()/(double)RAND_MAX*


　　(Parr[GBIndex].XBest[j]-Parr.X[j]));


　　}


　　Check(Parr,GdsCnt);


　　for (int j=0;j<Dim;j++)


　　{


　　Parr.X[j]+=Parr.V[j];


　　}


　　Check(Parr,GdsCnt);


　　}


　　CalculateFit();


　　for (int i=0;i {


　　if (Parr.Fit>=Parr.FitBest)


　　{


　　Parr.FitBest=Parr.Fit;


　　for (int j=0;j<Dim;j++)


　　{


　　Parr.XBest[j]=Parr.X[j];


　　}


　　}


　　}


　　GBIndex=0;


　　for (int i=0;i {


　　if (Parr.FitBest>Parr[GBIndex].FitBest&&i!=GBIndex)


　　{


　　GBIndex=i;


　　}


　　}


　　}


　　void Run(ofstream& outf,int num)//令粒子以规定次数num飞行


　　{


　　for (int i=0;i<num;i++)


　　{


　　BirdsFly();


　　outf<<(i+1)<<ends< for (int j=0;j<Dim;j++)


　　{


　　outf< }


　　outf<<endl;


　　}


　　cout<<"Done!"<<endl;


　　}
````

</details>

#### checkPop(1) · MATLAB · 136228ae

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行插值或参数拟合并评价曲线。
- **调用方式**：优先调用 `checkPop`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5826c2675873b4277fa903044598f06d5189c7af2cc22b79ee89562763150a21`
- 语言：MATLAB
- 符号：`checkPop`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/checkPop(1).m`

<details>
<summary>展开原始代码</summary>

````matlab
function checkPop(n,codeSize)
global pop;
pop(n,:)=sort(pop(n,:));
flag=0;
for j=2:codeSize
    if pop(n,j-1)==pop(n,j)
        pop(n,j)=randi(51);
        flag=1;
    end
end
if flag 
    checkPop(n,codeSize);
end
end
````

</details>

#### cross · MATLAB · ecf78774

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行插值或参数拟合并评价曲线。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e256cadcf64d54ae0b8dc2f133d26484c2e46c5bff08fd5ba3b8453927f32ba8`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/cross.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [] = cross(popSize,codeSize,crossRate)
global pop;
for i=1:2:popSize
    r=rand;
    if r>crossRate
        continue;
    end
    p=randi([2,codeSize]);
    tmp=pop(i,p:codeSize);
    pop(i,p:codeSize)=pop(i+1,p:codeSize);
    pop(i+1,p:codeSize)=tmp;
    checkPop(i,codeSize);
    checkPop(i+1,codeSize);
end
end
````

</details>

#### fitness · MATLAB · 1658a694

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行插值或参数拟合并评价曲线。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`909e9debc77aadcc5f4d7b29745449642e5176412c2689667a97e20789ed6dc6`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/fitness.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [score] = fitness(method)
global voltageX;
global outputY;
global len;                 %样本组容量
codeSize=length(method);     %codeSize=7
sum_A=0;
X=zeros(1,codeSize);
Y=zeros(1,codeSize);
for i=1:len  
    A=0;
    for j=1:codeSize
        X(j)=voltageX(i,method(j));
        Y(j)=outputY(i,method(j));
    end
    Y1=interp1(X,Y,voltageX(i,:),'spline');
    yTable=abs(Y1-outputY(i,:));
    for j=1:51
        dif=yTable(j);
        if dif<=0.5
            A=A+0;
        elseif dif<=1
            A=A+0.5;
        elseif dif<=2
            A=A+1.5;
        elseif dif<=3
            A=A+6;
        elseif dif<=5
            A=A+12;
        elseif dif>5
            A=A+25;
        end
    end
    sum_A=sum_A+A;
end
score=sum_A/len+84;
end
````

</details>

#### init · MATLAB · 402a9765

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行插值或参数拟合并评价曲线。
- **调用方式**：优先调用 `init`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`87fae6e3f824430da5a9a2ed0d8715eb707e30ee8ca264cf5729a5eb1a96421d`
- 语言：MATLAB
- 符号：`init`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/init.m`

<details>
<summary>展开原始代码</summary>

````matlab
function init(popSize,codeSize,maxNum)
global pop;
pop1=zeros(popSize,codeSize);
for i=1:popSize
    for j=1:codeSize
        pop1(i,j) = randi(maxNum);
        k=1;
        while (k<=j-1)
            if (pop1(i,j) == pop1(i,k))
                pop1(i,j) = randi(maxNum);
                k=0;
            end
            k=k+1;
        end
    end
end
pop=sort(pop1,2);
end
````

</details>

#### main · MATLAB · 0d18bb0e

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行插值或参数拟合并评价曲线；重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`e1b829b2512d1f3cca276b0ea66b3edf5901ffff4b764e0cfb83de64c48f5906`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/main.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/cross.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/fitness.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/init.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/mutation.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/readData.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/selection.m`

<details>
<summary>展开原始代码</summary>

````matlab
%使用三次样条插值的遗传算法
%运行过程中显示的tmpMin表示当前种群中的最低成本
%tmpAvg表示当前种群中的平均成本
%minScore表示目前整个运行中出现过的最低成本
%minScoreMethod表示上述最低成本对应的事前观察点
%g表示当前种群的子代数

clear;

global pop;             %取观察点种群
global fitnessTable;    %成本列表
global voltageX;         %样本电压X列表
global outputY;       %样本物理量Y列表
global len;             %样本组数量

popSize=100;            %种群大小
codeSize=7;             %观察点数量
crossRate=0.9;          %交叉概率
mutateRate=0.05;         %变异概率
maxGeneration=1000;     %最大子代数
aimScore=90;           %目标成本
minScore=200;             %最低成本

rand('state',sum(100*clock));

readData();
init(popSize,codeSize,51);
fitnessTable=zeros(popSize,1);
for i=1:popSize
    fitnessTable(i)=fitness(pop(i,:));
end
tmpMin=min(fitnessTable)

if tmpMin<minScore
    minScore=tmpMin;
    minScoreLocation=find(fitnessTable==tmpMin);
    minScoreMethod=pop(minScoreLocation,:);
end
minScore
minScoreMethod
if minScore<aimScore
    return;
end
g=1;
while g<=maxGeneration
    selection(popSize,codeSize);
    cross(popSize,codeSize,crossRate);
    mutation(popSize,codeSize,mutateRate);
    for i=1:popSize
        fitnessTable(i)=fitness(pop(i,:));
    end
    tmpMin=min(fitnessTable)
   
    if tmpMin<minScore
        minScore=tmpMin;
        minScoreLocation=find(fitnessTable==tmpMin);
        minScoreMethod=pop(minScoreLocation,:);
    end
    minScore
    minScoreMethod
    if minScore<aimScore
        break;
    end
    g
    g=g+1;
end
````

</details>

#### mutation · MATLAB · eab6a143

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行插值或参数拟合并评价曲线；重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `mutation`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`e6a39effcc05cecb4be8514f55c088833b78632f852222c3a3cf5e7aa72ca4d4`
- 语言：MATLAB
- 符号：`mutation`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/mutation.m`

<details>
<summary>展开原始代码</summary>

````matlab
function mutation(popSize,codeSize,mutateRate)
global pop;
for i=1:popSize
    r=rand();
    if r<mutateRate
        r=randi(codeSize);
        if rand()>0.5
            x=1;
        else
            x=-1;
        end
        tmp=pop(i,r)+x;
        if (r==1)
            if (tmp>=1)&&(pop(i,r+1)~=tmp)
                pop(i,r)=tmp;
            end
        elseif (r==codeSize)
            if (tmp<=51)&&(pop(i,r-1)~=tmp)
                pop(i,r)=tmp;
            end
        else
            if (pop(i,r-1)~=tmp)&&(pop(i,r+1)~=tmp)
                pop(i,r)=tmp;
            end
        end
        %checkPop(i,codeSize);
    end
end
end
````

</details>

#### readData · MATLAB · 1dff899f

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行插值或参数拟合并评价曲线。
- **调用方式**：优先调用 `readData`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e2383fb1c01806bd7c123ccf3b97da208845fd03a95559d250a0efcc58eb1ea7`
- 语言：MATLAB
- 符号：`readData`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/readData.m`

<details>
<summary>展开原始代码</summary>

````matlab
function readData()
origin=dlmread('20150915dataform.csv');
global voltageX;
global outputY;
global len;
len=length(origin)/2;
voltageX=origin(1:2:(len)*2-1,:);
outputY=origin(2:2:(len)*2,:);
end
````

</details>

#### selection · MATLAB · 18a3ae51

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行插值或参数拟合并评价曲线；重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`6f1b945a8f8a889aff2297790401b0c2d06f2bbceae3a03a6bc6f41726d19dc2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/GA_spline/selection.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [] = selection(popSize,codeSize)
global pop;
global fitnessTable;
fitnessSum=zeros(popSize,1);
fitnessSum(1)=1/fitnessTable(1);
for i=2:popSize
    fitnessSum(i)=fitnessSum(i-1)+1/fitnessTable(i);
end
popNew=zeros(popSize,codeSize);
for i=1:popSize
    r=rand()*fitnessSum(popSize);
    left=1;
    right=popSize;
    mid=round((left+right)/2);
    while 1
        if r>fitnessSum(mid)
            left=mid;
        else
            if r<fitnessSum(mid)
                right=mid;
            else
                popNew(i,:)=pop(mid,:);
                break;
            end
        end
        mid=round((left+right)/2);
        if (mid==left)||(mid==right)
            popNew(i,:)=pop(right,:);
            break;
        end
    end
end
pop=popNew;
````

</details>

#### 相似实现组 · MATLAB · 8c13cb67

- 归属算法：遗传算法GA
- 用途：数据读取与预处理
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：gaijinyichuansuanfa.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“数据读取与预处理”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`4362168f71f89f1809d226dfce04dbc7e0dfcb0e6c44b8ecb391a66e84574b08`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/改进遗传算法/gaijinyichuansuanfa.m`

<details>
<summary>展开原始代码</summary>

````matlab
tic 
clc,clear 
load sj.txt       %加载敌方 100个目标的数据 
x=sj(:,1:2:8);x=x(:); 
y=sj(:,2:2:8);y=y(:); 
sj=[x y]; 
d1=[70,40]; 
sj=[d1;sj;d1]; 
sj=sj*pi/180; 
d=zeros(102); %距离矩阵d 
for i=1:101 
    for j=i+1:102 
         temp=cos(sj(i,1)-sj(j,1))*cos(sj(i,2))*cos(sj(j,2))+sin(sj(i,2))*sin(sj(j,2)); 
        d(i,j)=6370*acos(temp); 
    end 
end 
d=d+d';L=102;w=50;dai=100; 
%通过改良圈算法选取优良父代 A 
for k=1:w 
    c=randperm(100); 
    c1=[1,c+1,102]; 
    flag=1; 
 while flag>0 
      flag=0; 
   for m=1:L-3 
      for n=m+2:L-1 
        if d(c1(m),c1(n))+d(c1(m+1),c1(n+1))<d(c1(m),c1(m+1))+d(c1(n),c1(n+1)) 
           flag=1; 
           c1(m+1:n)=c1(n:-1:m+1); 
        end 
      end 
   end 
   end 
  J(k,c1)=1:102; 
end 
J=J/102;  
J(:,1)=0;J(:,102)=1; 
rand('state',sum(clock)); 
%遗传算法实现过程 
A=J; 
for k=1:dai  %产生 0～1 间随机数列进行编码 
    B=A; 
    %交配产生子代B 
    for i=1:2:w 
        ch0=rand;ch(1)=4*ch0*(1-ch0); 
        for j=2:50 
            ch(j)=4*ch(j-1)*(1-ch(j-1)); 
        end 
        ch=2+floor(100*ch); 
        temp=B(i,ch); 
        B(i,ch)=B(i+1,ch); 
        B(i+1,ch)=temp; 
    end 
%变异产生子代 C 
by=find(rand(1,w)<0.1); 
if length(by)==0 
    by=floor(w*rand(1))+1; 
end 
C=A(by,:); 
L3=length(by); 
for j=1:L3 
   bw=2+floor(100*rand(1,3)); 
   bw=sort(bw); 
   C(j,:)=C(j,[1:bw(1)-1,bw(2)+1:bw(3),bw(1):bw(2),bw(3)+1:102]); 
end 
   G=[A;B;C]; 
   TL=size(G,1); 
   %在父代和子代中选择优良品种作为新的父代 
   [dd,IX]=sort(G,2);temp(1:TL)=0; 
   for j=1:TL 
       for i=1:101 
           temp(j)=temp(j)+d(IX(j,i),IX(j,i+1)); 
       end 
   end 
     [DZ,IZ]=sort(temp); 
     A=G(IZ(1:w),:); 
     end 
path=IX(IZ(1),:) 
long=DZ(1) 
toc 
````

</details>

##### 变体 2：yichuansuanfa.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“数据读取与预处理”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`cdbf05245a0d3863213bbf4791fade6791402a2cda6b88f48f01832d67105150`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/yichuansuanfa.m`

<details>
<summary>展开原始代码</summary>

````matlab
tic 
clc,clear 
load sj.txt       %加载敌方 100 个目标的数据 
x=sj(:,1:2:8); x=x(:); 
y=sj(:,2:2:8); y=y(:); 
sj=[x y]; d1=[70,40];  
sj0=[d1;sj;d1]; sj=sj0*pi/180; 
d=zeros(102); %距离矩阵 d 
for i=1:101 
    for j=i+1:102 
        temp=cos(sj(i,1)-sj(j,1))*cos(sj(i,2))*cos(sj(j,2))+sin(sj(i,2))*sin(sj(j,2)); 
        d(i,j)=6370*acos(temp); 
    end 
end 
d=d+d';L=102;w=50;dai=100; 
%通过改良圈算法选取优良父代 A 
for k=1:w 
    c=randperm(100); 
    c1=[1,c+1,102]; 
    flag=1; 
 while flag>0 
      flag=0; 
   for m=1:L-3 
      for n=m+2:L-1 
        if d(c1(m),c1(n))+d(c1(m+1),c1(n+1))<d(c1(m),c1(m+1))+d(c1(n),c1(n+1)) 
           flag=1; 
                      c1(m+1:n)=c1(n:-1:m+1); 
        end 
      end 
   end 
 end 
  J(k,c1)=1:102; 
end 
J=J/102;  
J(:,1)=0;J(:,102)=1; 
rand('state',sum(clock)); 
%遗传算法实现过程 
A=J; 
for k=1:dai  %产生 0～1间随机数列进行编码 
    B=A; 
    c=randperm(w); 
%交配产生子代 B 
    for i=1:2:w   
        F=2+floor(100*rand(1)); 
        temp=B(c(i),F:102); 
        B(c(i),F:102)=B(c(i+1),F:102); 
        B(c(i+1),F:102)=temp; 
    end 
    %变异产生子代 C 
by=find(rand(1,w)<0.1); 
if length(by)==0 
    by=floor(w*rand(1))+1;
end 
C=A(by,:); 
L3=length(by); 
for j=1:L3 
   bw=2+floor(100*rand(1,3)); 
   bw=sort(bw); 
   C(j,:)=C(j,[1:bw(1)-1,bw(2)+1:bw(3),bw(1):bw(2),bw(3)+1:102]); 
end 
   G=[A;B;C]; 
   TL=size(G,1); 
   %在父代和子代中选择优良品种作为新的父代 
   [dd,IX]=sort(G,2);temp(1:TL)=0; 
   for j=1:TL 
       for i=1:101 
           temp(j)=temp(j)+d(IX(j,i),IX(j,i+1)); 
       end 
   end 
     [DZ,IZ]=sort(temp); 
     A=G(IZ(1:w),:); 
end 
path=IX(IZ(1),:) 
long=DZ(1) 
````

</details>

#### cro · MATLAB · 661411c1

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `cro`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`562446dab063a1febd8e13f5743cc08f5cdec9dcd0a707900a7a4c8030f9f66d`
- 语言：MATLAB
- 符号：`cro`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/cro.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/cro.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/pro.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/pro.m`

<details>
<summary>展开原始代码</summary>

````matlab
%“交叉”操作
function scro=cro(s,seln,pc);

inn=size(s,1);
bn=size(s,2);

pcc=pro(pc);  %根据交叉概率决定是否进行交叉操作，1则是，0则否
if pcc==1
   chb=round(rand*(bn-2))+1;  %在[1,bn-1]范围内随机产生一个交叉位
   scro(1,:)=[s(seln(1),1:chb) s(seln(2),chb+1:bn)];
   scro(2,:)=[s(seln(2),1:chb) s(seln(1),chb+1:bn)];
else
   scro(1,:)=s(seln(1),:);
   scro(2,:)=s(seln(2),:);
end  
````

</details>

#### ft · MATLAB · 1dba99d8

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `ft`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`57f88d5be46ddaa7246d2261256c320f1502811625b08cf4a2c930fefe512767`
- 语言：MATLAB
- 符号：`ft`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/ft.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/ft.m`

<details>
<summary>展开原始代码</summary>

````matlab
%目标函数
function y=ft(x);

y=x.*sin(10*pi*x)+2;
````

</details>

#### ga · MATLAB · 3b708710

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`c1a709b588c07db1b31853790ebcc2ddc6f98fa21af62b990e1cbfcae0558734`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/ga.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/ga.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/cro.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/ft.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/mut.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/n2to10.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/objf.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/sel.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/cro.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/ft.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/mut.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/n2to10.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/objf.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/sel.m`

<details>
<summary>展开原始代码</summary>

````matlab
%用遗传算法进行简单函数的优化,可以显示中间过程
clear

bn=22; %个体串长度
inn=50; %初始种群大小
gnmax=200;  %最大代数
pc=0.8; %交叉概率
pm=0.05; %变异概率

%产生初始种群
s=round(rand(inn,bn));

gnf1=5;
gnf2=20;

%计算适应度,返回适应度f和累积概率p
[f,p]=objf(s);  

gn=1;
while gn<gnmax+1
    xp=-1:0.01:2;
    yp=ft(xp);
    for d=1:inn
        xi=n2to10(s(d,:));
        xdi(d)=-1.0+xi*3/(power(2,bn)-1);
    end
    yi=ft(xdi);
    plot(xp,yp,'b-',xdi,yi,'g*');
    strt=['当前代数 gn=' num2str(gn)];
    text(-0.75,1,strt);
    text(-0.75,3.5,'*  当前种群','Color','g');
    if gn<gnf1
        pause;
    end
    hold on;
           
    for j=1:2:inn
      %选择操作
      seln=sel(s,p);
      xs1=n2to10(s(seln(1),:));
      xds1=-1.0+xs1*3/(power(2,bn)-1);
      ys1=ft(xds1);
      xs2=n2to10(s(seln(2),:));
      xds2=-1.0+xs2*3/(power(2,bn)-1);
      ys2=ft(xds2);
      hold on;
      drawnow;
      plot(xds1,ys1,'r*',xds2,ys2,'r*');
      %交叉操作
      scro=cro(s,seln,pc);
      scnew(j,:)=scro(1,:);
      scnew(j+1,:)=scro(2,:);
      
      %变异操作
      smnew(j,:)=mut(scnew(j,:),pm);
      smnew(j+1,:)=mut(scnew(j+1,:),pm);
      
  end
  drawnow;
  text(-0.75,3.3,'*  选择后','Color','r');
  if gn<gnf1
      pause;
  end
  
  for d=1:inn
      xc=n2to10(scnew(d,:));
      xdc(d)=-1.0+xc*3/(power(2,bn)-1);
  end
  yc=ft(xdc);
  drawnow;
  plot(xdc,yc,'m*');
  text(-0.75,3.1,'*  交叉后','Color','m');
  if gn<gnf1
      pause;
  end
  hold on;
  
  for d=1:inn
      xm=n2to10(smnew(d,:));
      xdm(d)=-1.0+xm*3/(power(2,bn)-1);
  end
  ym=ft(xdm);
  drawnow;
  plot(xdm,ym,'c*');
  text(-0.75,2.9,'*  变异后','Color','c');
  
  if gn<gnf2
      pause;
  end
  hold off;
  s=smnew;  %产生了新的种群
   
   %计算新种群的适应度   
   [f,p]=objf(s);
   
   %记录当前代最好和平均的适应度
   [fmax,nmax]=max(f);
   fmean=mean(f);
   ymax(gn)=fmax;
   ymean(gn)=fmean;
   
   %记录当前代的最佳个体
   x=n2to10(s(nmax,:));
   xx=-1.0+x*3/(power(2,bn)-1);
   xmax(gn)=xx;
   
   gn=gn+1;
end
gn=gn-1;

figure(2);
subplot(2,1,1);
plot(1:gn,[ymax;ymean]);
title('历代适应度变化','fonts',10);
legend('最大适应度','平均适应度');
string1=['最终适应度',num2str(ymax(gn))];
gtext(string1);
subplot(2,1,2);
plot(1:gn,xmax,'r-');
legend('自变量');
string2=['最终自变量',num2str(xmax(gn))];
gtext(string2);
````

</details>

#### main · MATLAB · 6936ab32

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`d233ac06401545a7bba768cdd2825d1c2f1b5790112cd3054fdc4332d62e503f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/main.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/main.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/cro.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/mut.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/n2to10.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/objf.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/sel.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/cro.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/mut.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/n2to10.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/objf.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/sel.m`

<details>
<summary>展开原始代码</summary>

````matlab
%用遗传算法进行简单函数的优化
clear

bn=22; %个体串长度
inn=50; %初始种群大小
gnmax=200;  %最大代数
pc=0.75; %交叉概率
pm=0.05; %变异概率

%产生初始种群
s=round(rand(inn,bn));

%计算适应度,返回适应度f和累积概率p
[f,p]=objf(s);  

gn=1;
while gn<gnmax+1
   for j=1:2:inn
      
      %选择操作
      seln=sel(s,p);
      
      %交叉操作
      scro=cro(s,seln,pc);
      scnew(j,:)=scro(1,:);
      scnew(j+1,:)=scro(2,:);
      
      %变异操作
      smnew(j,:)=mut(scnew(j,:),pm);
      smnew(j+1,:)=mut(scnew(j+1,:),pm);
   end
   s=smnew;  %产生了新的种群
   
   %计算新种群的适应度   
   [f,p]=objf(s);
   
   %记录当前代最好和平均的适应度
   [fmax,nmax]=max(f);
   fmean=mean(f);
   ymax(gn)=fmax;
   ymean(gn)=fmean;
   %记录当前代的最佳个体
   x=n2to10(s(nmax,:));
   xx=-1.0+x*3/(power(2,bn)-1);
   xmax(gn)=xx;
   
   gn=gn+1
end
gn=gn-1;

%绘制曲线
subplot(2,1,1);
plot(1:gn,[ymax;ymean]);
title('历代适应度变化','fonts',10);
legend('最大适应度','平均适应度');
string1=['最终适应度',num2str(ymax(gn))];
gtext(string1);
subplot(2,1,2);
plot(1:gn,xmax,'r-');
legend('自变量');
string2=['最终自变量',num2str(xmax(gn))];
gtext(string2);
````

</details>

#### mut · MATLAB · 4ef51f56

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `mut`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`92824b7c9edbc3038c2f6ac5d07e01e717573ad2dff7c8649605c17c2afdec71`
- 语言：MATLAB
- 符号：`mut`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/mut.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/mut.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/pro.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/pro.m`

<details>
<summary>展开原始代码</summary>

````matlab
%“变异”操作
function snnew=mut(snew,pm);

bn=size(snew,2);
snnew=snew;

pmm=pro(pm);  %根据变异概率决定是否进行变异操作，1则是，0则否
if pmm==1
   chb=round(rand*(bn-1))+1;  %在[1,bn]范围内随机产生一个变异位
   snnew(chb)=abs(snew(chb)-1);
end   
````

</details>

#### n2to10 · MATLAB · 9ce33df4

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `n2to10`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`39c9a211a175cc01609a9a86412bebe3edcf5bf1e3af77be8f7515c68b86d0b5`
- 语言：MATLAB
- 符号：`n2to10`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/n2to10.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/n2to10.m`

<details>
<summary>展开原始代码</summary>

````matlab
%将2进制数转换为10进制数
function x=n2to10(s);

bn=size(s,2);
x=s(bn);
for i=1:bn-1
   x=x+s(bn-i)*power(2,i);
end
````

</details>

#### objf · MATLAB · 88f0b88a

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`73548fe322b023fe09a1fb2476af4ad2b6bee3ed1198e8cfbc61caf76e7d4eb4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/objf.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/objf.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/ft.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/n2to10.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/ft.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/n2to10.m`

<details>
<summary>展开原始代码</summary>

````matlab
%计算适应度函数

function [f,p]=objf(s);

inn=size(s,1);   %有inn个个体
bn=size(s,2);    %个体长度为bn

for i=1:inn
   x=n2to10(s(i,:));  %讲二进制转换为十进制
   xx=-1.0+x*3/(power(2,bn)-1);  %转化为[-1,2]区间的实数
   f(i)=ft(xx);  %计算函数值，即适应度
end
f=f';

%计算选择概率
fsum=sum(f.*f);
ps=f.*f/fsum;

%计算累积概率
p(1)=ps(1);
for i=2:inn
   p(i)=p(i-1)+ps(i);
end
p=p';
````

</details>

#### pro · MATLAB · 138eaa50

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `pro`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2daa3229d842fb0154fdfb8be18da2df13254bc6bdf471a948649d3019fa2d0c`
- 语言：MATLAB
- 符号：`pro`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/pro.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/pro.m`

<details>
<summary>展开原始代码</summary>

````matlab
function pcc=pro(pc);

test(1:100)=0;
l=round(100*pc);
test(1:l)=1;
n=round(rand*99)+1;
pcc=test(n);   
````

</details>

#### sel · MATLAB · 085f86ca

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `sel`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`802791b541fcfaf8a7371d45db2a939462bce2280829a70f2769c258c5c697fd`
- 语言：MATLAB
- 符号：`sel`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/简单函数优化的遗传算法程序/sel.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/模拟退火，禁忌搜索，遗传算法，神经网络-MATLAB程序合集/简单函数优化的遗传算法程序/sel.m`

<details>
<summary>展开原始代码</summary>

````matlab
%“选择”操作
function seln=sel(s,p);

inn=size(p,1);

%从种群中选择两个个体
for i=1:2
   r=rand;  %产生一个随机数
   prand=p-r;
   j=1;
   while prand(j)<0
       j=j+1;
   end
   seln(i)=j; %选中个体的序号
end
````

</details>

#### SGA · MATLAB · b0c7e10c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`2a16212b38575449049a1bb649f1bf79a06b66f47c41a880d43e997bb4539f8f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/SGA.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/b2f.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/calcbits.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/f2b.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/initializega.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/rouletteselect.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/simplexover.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [xval,bpop,fitsumnum,inline,outline,bestfit,worstfit,avgfit,rate,MA,MEP] =SGA(bounds,popsum,evalFN,startpop,pc,pm,maxterm,precision,last)
if isempty(startpop) %Generate a population at random
  startpop=initializega(popsum,bounds,evalFN,precision);
end
oldpop=startpop;
popnum=size(oldpop,1);
numvar=size(bounds,1);
term=1;
newpop=oldpop;
rate=0;
while term<=maxterm
    newpop=rouletteselect(newpop);
    i=0;
    for k=1:popnum
        if rand<pc
            i=i+1;
            ind(i)=k;
        end
    end
    if rem(length(ind),2)==0
        ind=ind;
    else
        ind=ind(1:length(ind)-1);
    end
    i=1;
    for i=1:2:length(ind)
        [newpop(ind(i),:),newpop(ind(i+1),:)]=simplexover(newpop(ind(i),:),newpop(ind(i+1),:),bounds,evalFN,precision);
    end
    newpop1=newpop;
    newpop1(:,end)=[];
    [m,n]=size(newpop1);
    i=1;
    for i=1:m*n
        if rand<pm
            k=ceil(i/n);
            if rem(i,n)==0
               site=n;
            else
               site=rem(i,n);
            end
            if newpop1(k,site)==0
                newpop1(k,site)=1;
            else
                newpop1(k,site)=0;
            end
            
            bits=calcbits(bounds,precision);
            estr=['x=b2f(newpop1(k,:),bounds,bits);[x v]=' evalFN ...
	'(x); newpop(k,:)=[f2b(x,bounds,bits) v];']; 
            eval(estr);
        end
    end
    inline(term)=sum(newpop(:,end))/popsum;%在线指标
    [bestfits,bestind]=max(newpop(:,end));
    bestpop=newpop(bestind,:);
    outline(term)=bestpop(end);%离线
     bestfit(term)=bestpop(end);%最优解搜索性能
     [worstfits,worstind]=min(newpop(:,end));
     worstpop=newpop(worstind,:);
     worstfit(term)=worstpop(end);%最小适应度
     avgfit=inline;%平均适应度
     if last-bestpop(end)<1e-6
           rate=term;%收敛速度
     end
      %=======多样性========
       cspop=newpop;
       cspop(:,end)=[];
       [N,L]=size(cspop);
       arrange1=sum(cspop,1);arrange2=sum(1-cspop,1);
       arrange=[arrange1;arrange2];
       ymax=max(arrange);ymin=min(arrange);
       ydeta=ymax-ymin;
       ysum=sum(ydeta);
       MA(term)=1-ysum/(L*N);
       pl=arrange1/N;
       MEP(term)=-sum(pl.*log(pl))/L;
       
       %=======over=========
   term=term+1; 
end
 estr=['x=b2f(newpop(xind,:),bounds,bits);[x v]=' evalFN ...
	'(x); ']; 
[xval,xind]=max(newpop(:,end));
eval(estr);

[m,n]=size(newpop);
i=1;
for i=1:m
    estr=['x=b2f(newpop(i,:),bounds,bits);[x,v]=' evalFN ...
             '(x);'];
     eval(estr);
     endpop(i,:)=[x,v];
 end
 bpop=endpop(xind,:);
  fitsumnum=maxterm*popsum;%适应度计算次数
  inline=cumsum(inline)./(1:term-1);%inline在线
  outline=cumsum(outline)./(1:term-1);%outline离线
````

</details>

#### b2f · MATLAB · 08e74617

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`813e909bf1d2df157b0892c51855ec0c804c787c9181dbd00461d26657171776`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/b2f.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [fval] = b2f(bval,bounds,bits)
% Return the float number corresponing to the binary representation of bval.
% fval   - the float representation of the number
% bval   - the binary representation of the number
% bounds - the bounds on the variables
% bits   - the number of bits to represent each variable
scale=(bounds(:,2)-bounds(:,1))'./(2.^bits-1); %The range of the variables
numVars=size(bounds,1);
cs=[0 cumsum(bits)]; 
for i=1:numVars
  a=bval((cs(i)+1):cs(i+1));
  fval(i)=sum(2.^(size(a,2)-1:-1:0).*a)*scale(i)+bounds(i,1);
end
````

</details>

#### calcbits · MATLAB · a29aa48b

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`dda343113148db27a562643f49ca9e0847830c0b82df4251da14f6d1b4d73a53`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/calcbits.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [bits]=calcbits(bounds,precision)

% Determine the number of bits to represent a float number to the precision provided.
% bits      - the number of bits required per variable
% bounds    - the bounds on the variables
% precision - the least difference to distinguish two numbers
bits=ceil(log2((bounds(:,2)-bounds(:,1))' ./ precision));
````

</details>

#### examplefun1 · MATLAB · b1e44a95

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1841ed7d9a4611e7fca50acfbfd1f4856f97ef1985da0fd3c36571ed48f4c9e4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/example/examplefun1.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [x,v]=examplefun1(x)
v=x*sin(10*pi*x)+2;
````

</details>

#### examplefun3 · MATLAB · 3084f72c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`986ba472dae18e2f7b971d9b48ffeeaef639fc34a8b379d43d8e2b37902d24ef`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/example/examplefun3.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [x,v]=examplefun3(x)
v=0.5-((sin(sqrt(x(1)^2+x(2)^2)))^2-0.5)/(1+0.001*(x(1)^2+x(2)^2))^2;
````

</details>

#### test1 · MATLAB · 5848b1da

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`85c5e69a7b2fd76750033fec376ecb7d501daa28d11a2fa377aafa9f5e48f9be`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/example/test1.m`

<details>
<summary>展开原始代码</summary>

````matlab
bounds=[-1,2];popsum=120;
evalFN='examplefun1';
startpop=[];pc=0.75;
pm=0.01;
maxterm=100;
precision=1e-6;
last=1;
[xval,bpop] =SGA(bounds,popsum,evalFN,startpop,pc,pm,maxterm,precision,last);
````

</details>

#### test2 · MATLAB · 6756a7fa

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`257b277c92e44ceaea476b209489ed0d7db6b6a2e747beca84b9aaf1145849cd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/example/test2.m`

<details>
<summary>展开原始代码</summary>

````matlab
bounds=[-100,100;-100,100];popsum=120;evalFN='examplefun3';startpop=[];pc=0.75;pm=0.01;maxterm=500;precision=1e-10;last=1;
[xval,bpop] =SGA(bounds,popsum,evalFN,startpop,pc,pm,maxterm,precision,last);
````

</details>

#### testfungraph1 · MATLAB · 1ac0ea3b

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a0000804d5dd4559c5257ff508db3619525855e9749066e43105aba5af0733d8`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/example/testfungraph1.m`

<details>
<summary>展开原始代码</summary>

````matlab
%x=linspace(-100,100,50);
%y=x;
%[X,Y]=meshgrid(x,y);
%Z=0.5-((sin(sqrt(X.^2+Y.^2))).^2-0.5)./(1+0.001*(X.^2+Y.^2)).^2;

%surf(X,Y,Z)
%grid on
%x=linspace(-5.12,5.12,50);
%y=x;
%[X,Y]=meshgrid(x,y);
%Z=(3./(0.05+(X.^2+Y.^2))).^2+(X.^2+Y.^2).^2;
%surf(X,Y,Z)
x=linspace(-1,2,100);
y=x.*sin(10*pi*x)+2;
plot(x,y)
````

</details>

#### testgraph2 · MATLAB · a9832967

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`14840543ce8830dcbac35eecfa775ad4aaa797db9ff69ba04734eec64ccc7fc0`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/example/testgraph2.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=linspace(-100,100,50);
y=linspace(-100,100,50);
[X,Y]=meshgrid(x,y);
Z=0.5-(sin(sqrt(X.^2+Y.^2)).^2-0.5)./(1.0+0.001*(X.^2+Y.^2)).^2;
%Z=(3.0./(0.5+(X.^2+Y.^2))).^2+(X.^2+Y.^2);
surf(X,Y,Z)
````

</details>

#### tran1 · MATLAB · f6e1dbe4

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`bae446a27d40ccc3aebe7d5a0a76bd678300c9b241546fc052f376bafe081a16`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/example/tran1.m`

<details>
<summary>展开原始代码</summary>

````matlab
S=[];m=0;
for i=0:1
    for j=0:1
        for k=0:1
            for l=0:1
                if i==1 & i+j+k+l<=2
                    m=m+1;
                    S(m,:)=[i j k l];
                end
          
            end
        end
    end
end
S
````

</details>

#### examplefun4 · MATLAB · 00a1d717

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`164e3c2c744750135f5e929a8faca5a0f6e5d33f654f843d7235d619aa75e848`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/examplefun4.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [x,v]=examplefun4(x)
v=(3.0/(0.05+(x(1)^2+x(2)^2)))^2+(x(1)^2+x(2)^2)^2;
````

</details>

#### f2b · MATLAB · 08355393

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a115ec348893ed19ef77193a3638e298732d1087b90209985fdee60da068a3df`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/f2b.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [bval] = f2b(fval,bounds,bits)
% function [bval] = f2b(fval,bounds,bits)
%
% Return the binary representation of the float number fval.
%
% fval   - the float representation of the number
% bval   - the binary representation of the number
% bounds - the bounds on the variables
% bits   - the number of bits to represent each variable

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

scale=(2.^bits-1)./ (bounds(:,2)-bounds(:,1))'; %The range of the variables
numV=size(bounds,1);
cs=[0 cumsum(bits)];
bval=[];
for i=1:numV
  fval(i)=(fval(i)-bounds(i,1)) * scale(i);
  bval=[bval rem(floor(fval(i)*pow2(1-bits(i):0)),2)];
end
````

</details>

#### initializega · MATLAB · 0b36d5ff

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`fd484707ed41d6bd765b48aed89bbf69dac6df4f83a1b6fa246bb409ce0df156`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/initializega.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/b2f.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/calcbits.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/f2b.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [pop] = initializega(num, bounds, evalFN,precision)
%Binary GA
estr=['x=b2f(pop(i,:),bounds,bits);[x v]=' evalFN ...
	'(x); pop(i,:)=[f2b(x,bounds,bits) v];'];  
numVars=size(bounds,1);%Number of variables
bits=calcbits(bounds,precision);
xZomeLength=sum(bits)+1;%Length of string is numVar + fit
pop=round(rand(num,sum(bits)+1));
pop1=pop;
for i=1:num
  eval(estr);
end
````

</details>

#### river · MATLAB · 9d27534e

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`51666fbe9bfb09dc0cf28f15e4372aa5251b2465f66717f69f8fd568706bf604`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/river.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear all;clc
a=[0,0;0,1;0,2;0,3;3,0;3,1;3,2;3,3;1,1;2,2];d=[0,2;2,0;1,1;0,1;1,0];i=1;j=1;k=1;s(1,:)=[3,3];
disp('此岸 - 船上 - 对岸')
for i=1:12
    for j=1:5
        t=0;r=mod(i,2);m=r;u=0;
        for k=1:10
            if s(i,:)+(-1)^i*d(j,:)==a(k,:)
                t=1;
            end
        end
        if i+1>=3
            for m=1+r:2:i-1
                if s(i,:)+(-1)^i*d(j,:)==s(m,:)
                    u=1;
                end
            end
        end
        if t==1
            if u==0
                s(i+1,:)=s(i,:)+(-1)^i*d(j,:);
                c(i+1,:)=d(j,:);
                break;
            elseif u==1 
                continue;
            end
            else continue;
        end
    end
if t==0 
    disp('No Result');
    break;
end
b(i+1,:)=[3,3]-s(i+1,:);
play=sprintf('{%d,%d}-{%d,%d}-{%d,%d}',s(i,1),s(i,2),c(i+1,1),c(i+1,2),b(i+1,1),b(i+1,2));
  disp(play)
  if s(i+1,:)==[0,0]
  break;
  end
end
````

</details>

#### rouletteselect · MATLAB · 447abe7a

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `rouletteselect`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`5d9a3d40d4ee6e9ceb42a75ea8fbf7cd2e3e187d8a651f314275eb9c99498d55`
- 语言：MATLAB
- 符号：`rouletteselect`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/rouletteselect.m`

<details>
<summary>展开原始代码</summary>

````matlab
function newpop=rouletteselect(oldpop)
%roulette is the traditional selection function with the probability of
%surviving equal to the fittness of i / sum of the fittness of all
%individuals
%function[newPop] = roulette(oldPop,options)
%newPop  - the new population selected from the oldPop
%oldPop  - the current population


%Get the parameters of the population
numVars = size(oldpop,2);
numSols = size(oldpop,1);

%Generate the relative probabilites of selection
totalFit = sum(oldpop(:,numVars));
prob=oldpop(:,numVars) / totalFit; 
prob=cumsum(prob);

rNums=sort(rand(numSols,1)); 		%Generate random numbers

%Select individuals from the oldPop to the new
fitIn=1;newIn=1;
while newIn<=numSols
  if(rNums(newIn)<prob(fitIn))
    newpop(newIn,:) = oldpop(fitIn,:);
    newIn = newIn+1;
  else
    fitIn = fitIn + 1;
  end
end
````

</details>

#### simplexover · MATLAB · 27a19fd7

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`2551e1d77dc12cc9fad1a43c8cd447707781808d9411814e1278fb192be70f56`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/simplexover.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/b2f.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/calcbits.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/f2b.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [c1,c2] = simplexover(p1,p2,bounds,evalFN,precision)
% Simple crossover takes two parents P1,P2 and performs simple single point
% crossover.  
%
% function [c1,c2] = simpleXover(p1,p2,bounds,Ops)
% p1      - the first parent ( [solution string function value] )
% p2      - the second parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options matrix for simple crossover [gen #SimpXovers].
numVar = size(p1,2)-1; 			% Get the number of variables 
% Pick a cut point randomly from 1-number of vars
bits=calcbits(bounds,precision);
cPoint = round(rand * (numVar-2)) + 1;

c1 = [p1(1:cPoint) p2(cPoint+1:numVar+1)]; % Create the children
c2 = [p2(1:cPoint) p1(cPoint+1:numVar+1)];

estr1=['x=b2f(c1,bounds,bits);[x v]=' evalFN ...
	'(x); c1=[f2b(x,bounds,bits) v];']; 

estr2=['x=b2f(c2,bounds,bits);[x v]=' evalFN ...
	'(x); c2=[f2b(x,bounds,bits) v];']; 
eval(estr1);
eval(estr2);
````

</details>

#### sta · MATLAB · f9e24328

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d711d0b9991ba15ec1c6636e5581878c9f6fa0a326e363edbab4f298ff715494`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/sta.m`

<details>
<summary>展开原始代码</summary>

````matlab
s=[];k=0;
for i=0:3
    for j=0:3
       if i>=j & 3-i>=3-j & ~(i==0 & j==0)
           k=k+1;
           s(k,:)=[i,j];
       end
       if i==0 
            k=k+1;
           s(k,:)=[i,j];
       end
        if i==3 & j~=3
            k=k+1;
           s(k,:)=[i,j];
       end
    end
end
s
````

</details>

#### sta1 · MATLAB · a7ea8592

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f2bdb1040c5358f2a2123396098bc2fd248ce7b0ca48572eac8440f0a9cb7da1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/sta1.m`

<details>
<summary>展开原始代码</summary>

````matlab
S=[];m=0;
for i=0:1
    for j=0:1
        for k=0:1
            for l=0:1
                if (i==1 & (1-j)*(1-k)~=1 & (1-k)*(1-l)~=1) | (i==0 & j*k~=1 & k*l~=1) 
                    m=m+1;
                    S(m,:)=[i j k l]
                end
            end
        end
    end
end
````

</details>

#### sta3 · MATLAB · 707f0c6e

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9ba7ce6d2017cab2b35ee8a99ddfc70b8b023b6d3320abb9c5f42cef187527ca`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/sta3.m`

<details>
<summary>展开原始代码</summary>

````matlab
S=[];m=0;
for i=0:1
    for j=0:1
        for k=0:1
            for l=0:1
                
                    m=m+1;
                    S(m,:)=[i j k l];
          
            end
        end
    end
end
````

</details>

#### test8 · MATLAB · 97e5a6e5

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`70506033316e0be071e669b4b56c3386df31bb333e2d0632c3bfad2b99ddc95b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/test8.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/SGA.m`

<details>
<summary>展开原始代码</summary>

````matlab
bounds=[-5.12,+5.12;-5.12,+5.12];popsum=120;evalFN='examplefun4';startpop=[];pc=0.75;pm=0.01;maxterm=1000;precision=1e-8;last=1;
[xval,bpop] =SGA(bounds,popsum,evalFN,startpop,pc,pm,maxterm,precision,last);
````

</details>

#### tran · MATLAB · 69577ba7

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`dbe085d25aff017314187b116627985640bb942d3d0d4ebfd2a6df107b0b20cf`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法/SGA/tran.m`

<details>
<summary>展开原始代码</summary>

````matlab
S=[];k=0;
for i=0:2
    for j=0:2
        if i+j<=2 & i+j~=0
            k=k+1;
            S(k,:)=[i,j];
        end
    end
end
S
````

</details>

#### Contents · MATLAB · 349a3b2c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`11678efe112025b2703e2059dd1d9ff1f02b2d23c73cc6c7d18e149a7278616a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/Contents.m`

<details>
<summary>展开原始代码</summary>

````matlab
% Genetic Optimization Toolbox
%
% Main interface
% ga.m                   The Genetic Algorithm  
% initialize.m           Initialization function Used by ga.m   
%
% Operators used during simulated evolution
%
% Crossover Operators
% heuristicXover.m       Operator for the Algorithm Used by ga.m 
% arithXover.m           Operator for the Algorithm Used by ga.m 
% simpleXover.m          Operator for the Algorithm Used by ga.m 
%
% Mutation Operators
% binaryMutation.m       Operator for the Algorithm Used by ga.m 
% boundaryMutation.m     Operator for the Algorithm Used by ga.m 
% multiNonUnifMutation.m Operator for the Algorithm Used by ga.m 
% nonUnifMutation.m      Operator for the Algorithm Used by ga.m 
% unifMutation.m         Operator for the Algorithm Used by ga.m
%
% Selection Functions
% normGeomSelect.m       Selection function Used by ga.m
% roulette.m             Selection function Used by ga.m
% tournSelect.m          Selection function Used by ga.m
%
% Termination Functions
% maxGenTerm.m           Termination function Used by ga.m
% optMaxGenTerm.m        Termination function Used by ga.m
%
% Functions used for binary representation
% calcbits.m             Binary precision function used by ga.m
% f2b.m                  Float to Binary conversion used by ga.m
% b2f.m                  Binary to Float conversion used by ga.m
%
% Utility functions
% parse.m                Parse blank separated names used by ga.m
% delta.m                Used by nonUnifMutation.m and mult...m
%
% Demonstrations
% gademo1.m              Introductory demo of GAOT
% gademo2.m              Multi-dimensional demo of GAOT
% gademo3.m              Reference for GAOT
%
% Functions used in Demonstrations
% gademo1eval1.m         Example eval function used by gademo1.m
% coranaEval.m           Calculate Corana functions used by gademo2.m
% coranaMin.m            Calculate negative of Corana used by gademo2.m
% gaEval.m               Calculation of Corana used for testing
% gaGradEval.m           Evaluation Used for Testing      
% gaGradGrad.m           Gradient used for SQP during Testing

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
````

</details>

#### arithXover · MATLAB · 44ede3d4

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fa289c849b880cde1e2b6bda6f1cfd9cecfb7d98b4c2754fb4c0680cbafbf90e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/arithXover.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [c1,c2] = arithXover(p1,p2,bounds,Ops)
% Arith crossover takes two parents P1,P2 and performs an interpolation
% along the line formed by the two parents.
%
% function [c1,c2] = arithXover(p1,p2,bounds,Ops)
% p1      - the first parent ( [solution string function value] )
% p2      - the second parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options matrix for arith crossover [gen #ArithXovers]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

% Pick a random mix amount
a = rand;

% Create the children
c1 = p1*a     + p2*(1-a);
c2 = p1*(1-a) + p2*a; 
end
````

</details>

#### b2f · MATLAB · 3cd9329e

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`06b62dd9938e52d9911900f1a3aec805331dc31a0f57acbae7f35c36cf808dcd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/b2f.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [fval] = b2f(bval,bounds,bits)
% function [fval] = b2f(bval,bounds,bits)
%
% Return the float number corresponing to the binary representation of bval.
%
% fval   - the float representation of the number
% bval   - the binary representation of the number
% bounds - the bounds on the variables
% bits   - the number of bits to represent each variable

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

scale=(bounds(:,2)-bounds(:,1))'./(2.^bits-1); %The range of the variables
numV=size(bounds,1);
cs=[0 cumsum(bits)]; 
for i=1:numV
  a=bval((cs(i)+1):cs(i+1));
  fval(i)=sum(2.^(size(a,2)-1:-1:0).*a)*scale(i)+bounds(i,1);
end
````

</details>

#### binaryMutation · MATLAB · bb5d4a3f

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`5eaf2ba477545018f14e5464ac1bb514388e3a7ad60cd37e2c2f737f0b6cae39`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/binaryMutation.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [parent] = binaryMutate(parent,bounds,Ops)
% Binary mutation changes each of the bits of the parent
% based on the probability of mutation
%
% function [newSol] = binaryMutate(parent,bounds,Ops)
% parent  - the first parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options for binaryMutation [gen prob_of_mutation]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

pm=Ops(2);
numVar = size(parent,2)-1; 		% Get the number of variables 
% Pick a variable to mutate randomly from 1-number of vars
rN=rand(1,numVar)<pm;
parent=[abs(parent(1:numVar) - rN) parent(numVar+1)];
end
  
````

</details>

#### boundaryMutation · MATLAB · 1262d771

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`989873b1e0f18055d3f27379b52a7eb03aad863e49f63270de3296ebbbfc1930`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/boundaryMutation.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [parent] = boundaryMutate(parent,bounds,Ops)
% Boundary Mutation changes one of the parameters of the parent and changes it
% randomly either to its upper or lower bound.
%
% function [newSol] = boundaryMutate(parent,bounds,Ops)
% parent  - the first parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options for boundaryMutation [gen #BndMutations]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

numVar = size(parent,2)-1; 		% Get the number of variables
% Pick a variable to mutate randomly from 1-number of vars
mPoint = round(rand * (numVar-1)) + 1;
b = round(rand)+1; 			% Pick which bound to move to
newValue = bounds(mPoint,b); 		% Now mutate that point
parent(mPoint) = newValue; 		% Make the child
end
````

</details>

#### calcbits · MATLAB · 0394f22d

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`62c5df39e810550a5a5f049fc7af0411c2bdeff36c41413cc1b9ace5628a8530`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/calcbits.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [bits]=calcbits(bounds,precision)
% function [bits]=calcbits(bounds,precision)
%
% Determine the number of bits to represent a float number to the precision
% provided.
%
% bits      - the number of bits required per variable
% bounds    - the bounds on the variables
% precision - the least difference to distinguish two numbers

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

bits=ceil(log2((bounds(:,2)-bounds(:,1))' ./ precision));
% bits=ceil(log( (bounds(:,2)-bounds(:,1))' .* 10.^precision+1) ./ log(2));
````

</details>

#### coranaEval · MATLAB · 8ab257ed

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`80c6cd781427f635aabc77da0918e7ccfc0cfc4f12eb83d8645bbe1a22456a83`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/coranaEval.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [val] = coranaEval(sol)
% function [val] = coranaEval(sol)
%
% Determines the value of the Corana function at point sol.
% This function is used in gademo2.
% 
% val - the value of the Corana function at point sol
% sol - the location to evaluate the Corana function

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

numv = size(sol,2);
x=sol(1:numv);
d0=[1 1000 10 100 1 10 100 1000 1 10];
d=d0(1:numv);
c=0.15;
s=.2*ones(1,numv);
t=0.05*ones(1,numv);
bk = s.*(round(x./s));
dev= (abs(bk-x)<t) & (bk~=0);
z=c*((bk+sign(bk).*t).^2).*d;
y=x.^2.*d;
val = sum((dev.*z) + ((~dev).*y));
````

</details>

#### coranaMin · MATLAB · 27e5acef

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`dc63ff6db166759626f6f4df27902a7ffc87226de4f0ee9a14081db595fd86b3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/coranaMin.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/coranaEval.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [val,sol] = coranaMin(sol,options)
% function [val,sol] = coranaMin(sol,options)
%
% Function to minimize the Corana function.
%
% val - the value of the Corana function at point sol
% sol - the location to evaluate the Corana function

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

numVar=size(sol,2)-1;
val = coranaEval(sol(1:numVar));
val = -val;
````

</details>

#### delta · MATLAB · f25351fe

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4bf099c26e5a6f3cf9291904127fb3e75c0ec1042e25a8a38737d09c99170476`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/delta.m`

<details>
<summary>展开原始代码</summary>

````matlab
function[change] = delta(ct,mt,y,b)
% The delta function is the non-uniform distributions used by the nonUniform
% mutations.  This function returns a change based on the current gen, the
% max gen and the amount of possible deviation.
%
% function[change] = delta(ct,mt,y,b)
% ct - current generation
% mt - maximum generation
% y  - maximum amount of change, i.e. distance from parameter value to bounds
% b  - shape parameter

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

r=ct/mt;
if(r>1)
  r=.99;
  % disp(sprintf('max gen %d < current gen %d setting ratio = 1',mt,ct));
end
change = y*(rand*(1-r))^b;
````

</details>

#### f2b · MATLAB · 169bd33c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c9f42ca7cd8c605bbecd2900755b84c2040852f9c2f4c5659907d3487e6194f6`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/f2b.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [bval] = function(fval,bounds,bits)
% function [bval] = f2b(fval,bounds,bits)
%
% Return the binary representation of the float number fval.
%
% fval   - the float representation of the number
% bval   - the binary representation of the number
% bounds - the bounds on the variables
% bits   - the number of bits to represent each variable

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

scale=(2.^bits-1)./ (bounds(:,2)-bounds(:,1))'; %The range of the variables
numV=size(bounds,1);
cs=[0 cumsum(bits)];
for i=1:numV
  fval(i)=(fval(i)-bounds(i,1)) * scale(i);
  bval=[bval rem(floor(fval(i)*pow2(1-bits(i):0)),2)];
end
````

</details>

#### ga · MATLAB · 3700e0d7

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`3db58ee3ec1b4a262cd8021f12084b0430db596c4d0708b29a3be5da9fa44fe0`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/ga.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/b2f.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/calcbits.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/f2b.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/initialize.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/parse.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [x,endPop,bPop,traceInfo] = ga(bounds,evalFN,evalOps,startPop,opts,...
termFN,termOps,selectFN,selectOps,xOverFNs,xOverOps,mutFNs,mutOps)
% GA run a genetic algorithm
% function [x,endPop,bPop,traceInfo]=ga(bounds,evalFN,evalOps,startPop,opts,
%                                       termFN,termOps,selectFN,selectOps,
%                                       xOverFNs,xOverOps,mutFNs,mutOps)
%                                
% Output Arguments:
%   x            - the best solution found during the course of the run
%   endPop       - the final population 
%   bPop         - a trace of the best population
%   traceInfo    - a matrix of best and means of the ga for each generation
%
% Input Arguments:
%   bounds       - a matrix of upper and lower bounds on the variables
%   evalFN       - the name of the evaluation .m function
%   evalOps      - options to pass to the evaluation function ([NULL])
%   startPop     - a matrix of solutions that can be initialized
%                  from initialize.m
%   opts         - [epsilon prob_ops display] change required to consider two 
%                  solutions different, prob_ops 0 if you want to apply the
%                  genetic operators probabilistly to each solution, 1 if
%                  you are supplying a deterministic number of operator
%                  applications and display is 1 to output progress 0 for
%                  quiet. ([1e-6 1 0])
%   termFN       - name of the .m termination function (['maxGenTerm'])
%   termOps      - options string to be passed to the termination function
%                  ([100]).
%   selectFN     - name of the .m selection function (['normGeomSelect'])
%   selectOpts   - options string to be passed to select after
%                  select(pop,#,opts) ([0.08])
%   xOverFNS     - a string containing blank seperated names of Xover.m
%                  files (['arithXover heuristicXover simpleXover']) 
%   xOverOps     - A matrix of options to pass to Xover.m files with the
%                  first column being the number of that xOver to perform
%                  similiarly for mutation ([2 0;2 3;2 0])
%   mutFNs       - a string containing blank seperated names of mutation.m 
%                  files (['boundaryMutation multiNonUnifMutation ...
%                           nonUnifMutation unifMutation'])
%   mutOps       - A matrix of options to pass to Xover.m files with the
%                  first column being the number of that xOver to perform
%                  similiarly for mutation ([4 0 0;6 100 3;4 100 3;4 0 0])

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

%%$Log: ga.m,v $
%Revision 1.10  1996/02/02  15:03:00  jjoine
% Fixed the ordering of imput arguments in the comments to match
% the actual order in the ga function.
%
%Revision 1.9  1995/08/28  20:01:07  chouck
% Updated initialization parameters, updated mutation parameters to reflect
% b being the third option to the nonuniform mutations
%
%Revision 1.8  1995/08/10  12:59:49  jjoine
%Started Logfile to keep track of revisions
%


n=nargin;
if n<2 | n==6 | n==10 | n==12
  disp('Insufficient arguements') 
end
if n<3 %Default evalation opts.
  evalOps=[];
end
if n<5
  opts = [1e-6 1 0];
end
if opts==[]
  opts = [1e-6 1 0];
end

if any(evalFN<48) %Not using a .m file
  if opts(2)==1 %Float ga
    e1str=['x=c1; c1(xZomeLength)=', evalFN ';'];  
    e2str=['x=c2; c2(xZomeLength)=', evalFN ';'];  
  else %Binary ga
    e1str=['x=b2f(endPop(j,:),bounds,bits); endPop(j,xZomeLength)=',...
	evalFN ';'];
  end
else %Are using a .m file
  if opts(2)==1 %Float ga
    e1str=['[c1(xZomeLength) c1]=' evalFN '(c1,[gen evalOps]);'];  
    e2str=['[c2(xZomeLength) c2]=' evalFN '(c2,[gen evalOps]);'];  
  else %Binary ga
    e1str=['x=b2f(endPop(j,:),bounds,bits);[v x]=' evalFN ...
	'(x,[gen evalOps]); endPop(j,:)=[f2b(x,bounds,bits) v];'];  
  end
end


if n<6 %Default termination information
  termOps=[100];
  termFN='maxGenTerm';
end
if n<12 %Default muatation information
  if opts(2)==1 %Float GA
  mutFNs=['boundaryMutation multiNonUnifMutation nonUnifMutation unifMutation'];
    mutOps=[4 0 0;6 termOps(1) 3;4 termOps(1) 3;4 0 0];
  else %Binary GA
    mutFNs=['binaryMutation'];
    mutOps=[0.05];
  end
end
if n<10 %Default crossover information
  if opts(2)==1 %Float GA
    xOverFNs=['arithXover heuristicXover simpleXover'];
    xOverOps=[2 0;2 3;2 0];
  else %Binary GA
    xOverFNs=['simpleXover'];
    xOverOps=[0.6];
  end
end
if n<9 %Default select opts only i.e. roullete wheel.
  selectOps=[];
end
if n<8 %Default select info
  selectFN=['normGeomSelect'];
  selectOps=[0.08];
end
if n<6 %Default termination information
  termOps=[100];
  termFN='maxGenTerm';
end
if n<4 %No starting population passed given
  startPop=[];
end
if startPop==[] %Generate a population at random
  %startPop=zeros(80,size(bounds,1)+1);
  startPop=initialize(80,bounds,evalFN,evalOps,opts(1:2));
end

if opts(2)==0 %binary
  bits=calcbits(bounds,opts(1));
end

xOverFNs=parse(xOverFNs);
mutFNs=parse(mutFNs);

xZomeLength  = size(startPop,2); 	%Length of the xzome=numVars+fittness
numVar       = xZomeLength-1; 		%Number of variables
popSize      = size(startPop,1); 	%Number of individuals in the pop
endPop       = zeros(popSize,xZomeLength); %A secondary population matrix
c1           = zeros(1,xZomeLength); 	%An individual
c2           = zeros(1,xZomeLength); 	%An individual
numXOvers    = size(xOverFNs,1); 	%Number of Crossover operators
numMuts      = size(mutFNs,1); 		%Number of Mutation operators
epsilon      = opts(1);                 %Threshold for two fittness to differ
oval         = max(startPop(:,xZomeLength)); %Best value in start pop
bFoundIn     = 1; 			%Number of times best has changed
done         = 0;                       %Done with simulated evolution
gen          = 1; 			%Current Generation Number
collectTrace = (nargout>3); 		%Should we collect info every gen
floatGA      = opts(2)==1;              %Probabilistic application of ops
display      = opts(3);                 %Display progress 

while(~done)
  %Elitist Model
  [bval,bindx] = max(startPop(:,xZomeLength)); %Best of current pop
  best =  startPop(bindx,:);

  if collectTrace
    traceInfo(gen,1)=gen; 		          %current generation
    traceInfo(gen,2)=startPop(bindx,xZomeLength);       %Best fittness
    traceInfo(gen,3)=mean(startPop(:,xZomeLength));     %Avg fittness
  end
  
  if ( (abs(bval - oval)>epsilon) | (gen==1)) %If we have a new best sol
    if display
      fprintf(1,'\n%d %f\n',gen,bval);          %Update the display
    end
    if floatGA
      bPop(bFoundIn,:)=[gen startPop(bindx,:)]; %Update bPop Matrix
    else
      bPop(bFoundIn,:)=[gen b2f(startPop(bindx,1:numVar),bounds,bits)...
	  startPop(bindx,xZomeLength)];
    end
    bFoundIn=bFoundIn+1;                      %Update number of changes
    oval=bval;                                %Update the best val
  else
    if display
      fprintf(1,'%d ',gen);	              %Otherwise just update num gen
    end
  end
  
  endPop = feval(selectFN,startPop,[gen selectOps]); %Select
  
  if floatGA %Running with the model where the parameters are numbers of ops
    for i=1:numXOvers,
      for j=1:xOverOps(i,1),
	a = rand*(popSize-1)+1; 	%Pick a parent
	b = rand*(popSize-1)+1; 	%Pick another parent
	xN=deblank(xOverFNs(i,:)); 	%Get the name of crossover function
	[c1 c2] = feval(xN,endPop(a,:),endPop(b,:),bounds,[gen xOverOps(i,:)]);
	
	if c1(1:numVar)==endPop(a,(1:numVar)) %Make sure we created a new 
	  c1(xZomeLength)=endPop(a,xZomeLength); %solution before evaluating
	elseif c1(1:numVar)==endPop(b,(1:numVar))
	  c1(xZomeLength)=endPop(b,xZomeLength);
	else 
	  %[c1(xZomeLength) c1] = feval(evalFN,c1,[gen evalOps]);
	  eval(e1str);
	end
	if c2(1:numVar)==endPop(a,(1:numVar))
	  c2(xZomeLength)=endPop(a,xZomeLength);
	elseif c2(1:numVar)==endPop(b,(1:numVar))
	  c2(xZomeLength)=endPop(b,xZomeLength);
	else 
	  %[c2(xZomeLength) c2] = feval(evalFN,c2,[gen evalOps]);
	  eval(e2str);
	end      
	
	endPop(a,:)=c1;
	endPop(b,:)=c2;
      end
    end
  
    for i=1:numMuts,
      for j=1:mutOps(i,1),
	a = rand*(popSize-1)+1;
	c1 = feval(deblank(mutFNs(i,:)),endPop(a,:),bounds,[gen mutOps(i,:)]);
	if c1(1:numVar)==endPop(a,(1:numVar)) 
	  c1(xZomeLength)=endPop(a,xZomeLength);
	else
	  %[c1(xZomeLength) c1] = feval(evalFN,c1,[gen evalOps]);
	  eval(e1str);
	end
	endPop(a,:)=c1;
      end
    end
    
  else %We are running a probabilistic model of genetic operators
    for i=1:numXOvers,
      xN=deblank(xOverFNs(i,:)); 	%Get the name of crossover function
      cp=find(rand(popSize,1)<xOverOps(i,1)==1);
      if rem(size(cp,1),2) cp=cp(1:(size(cp,1)-1)); end
      cp=reshape(cp,size(cp,1)/2,2);
      for j=1:size(cp,1)
	a=cp(j,1); b=cp(j,2); 
	[endPop(a,:) endPop(b,:)] = feval(xN,endPop(a,:),endPop(b,:),...
	  bounds,[gen xOverOps(i,:)]);
      end
    end
    for i=1:numMuts
      mN=deblank(mutFNs(i,:));
      for j=1:popSize
	endPop(j,:) = feval(mN,endPop(j,:),bounds,[gen mutOps(i,:)]);
	eval(e1str);
      end
    end
  end
  
  gen=gen+1;
  done=feval(termFN,[gen termOps],bPop,endPop); %See if the ga is done
  startPop=endPop; 			%Swap the populations
  
  [bval,bindx] = min(startPop(:,xZomeLength)); %Keep the best solution
  startPop(bindx,:) = best; 		%replace it with the worst
end

[bval,bindx] = max(startPop(:,xZomeLength));
if display 
  fprintf(1,'\n%d %f\n',gen,bval);	  
end

x=startPop(bindx,:);
if opts(2)==0 %binary
  x=b2f(x,bounds,bits);
  bPop(bFoundIn,:)=[gen b2f(startPop(bindx,1:numVar),bounds,bits)...
      startPop(bindx,xZomeLength)];
else
  bPop(bFoundIn,:)=[gen startPop(bindx,:)];
end

if collectTrace
  traceInfo(gen,1)=gen; 		%current generation
  traceInfo(gen,2)=startPop(bindx,xZomeLength); %Best fittness
  traceInfo(gen,3)=mean(startPop(:,xZomeLength)); %Avg fittness
end
````

</details>

#### gademo1 · MATLAB · 3a19cb0a

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`18483bad6bd892a7aef56fab7d923ec833563d275b3ce83d6a651a6ca7949739`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/gademo1.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/ga.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/initialize.m`

<details>
<summary>展开原始代码</summary>

````matlab
% GADEMO1 Introduction to the Genetic Optimization Toolbox

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

clf;
figure(gcf);
more on
echo on
clc
%    ==========================================================
%    GADEMO 1
%    ==========================================================

%    INITIALIZE - Initialize a populutaton of solutions
%    GA         - Simulates evolution

pause % Strike any key for the introduction to Genetic Algorithms
clc

%    Genetic algorithms

%    A genetic algorithm is a simulation of evolution where the
%    rule of survival of the fittest is applied to a population
%    of individuals.
%    The basic genetic algorithm is as follows:
%      1. Create an initial population (usually a randomly
%         generated string)
%      2. Evaluate all of the individuals (apply some function
%         or formula to the individuals)
%      3. Select a new population from the old population based
%         on the fitness of the individuals as given by the
%         evaluation function.
%      4. Apply some genetic operators (mutation & crossover)
%         to members of the population to create new solutions.
%      5. Evaluate these newly created individuals.
%      6. Repeat steps 3-6 (one generation) until the
%         termination criteria has been satisfied (usually
%         perform for a certain fixed number of generations)
%
%    Let's look at an example

pause % Strike any key to define the problem...
clc

%   Let's consider the maximization of the following function:
%   f(x) = x + 10*sin(5*x)+7*cos(4*x) over the interval (0,9)
% This may take several minutes...
fplot('x + 10*sin(5*x)+7*cos(4*x)',[0 9])
% Done!

%   Now, let's set up a genetic algorithm to find the maximum
%   of this problem.  First, we need to create the evaluation
%   function .m file, here is gademo1eval1.m

pause 				% Strike any key to look at gademo1eval1.m
type gademo1eval1.m
pause 					% Strike any key to continue
clc

%   Note that the evaluation function must take two parameters,
%   sol and options.  Sol is a row vector of n+1 elements where
%   the first n elements are the parameters of interest.  The
%   n+1'th element is the value of this solution.  The options
%   matrix is a row matrix of 
%   [current generation, eval options]
%   The eval function must return both the value of the sting,
%   val and the string itself, sol.  This is done so that
%   your evaluation can repair and/or improve the string.

pause 					% Strike any key to continue
clc

%   Now that we have defined the evaluation function, we now
%   have to create an initial population.  The most common way
%   to generate an initial population is to randomly generate
%   solutions within the range of interest, in this case 0-9.
%   The initialize routine will do this for you.

pause 				% Strike any key for help on initialize
clc
help initialize
pause 					% Strke any key to continue.
clc
%   Let's create a random starting popluation of size 10.
initPop=initialize(10,[0 9],'gademo1eval1');
pause 					% Strike any key to continue.

%   We can now take a look at this population.
hold on
plot (initPop(:,1),initPop(:,2),'g+')
pause % Strike any key to continue 
clc
%  We can now run the evolutionary procedure on this
%  population.
help ga
pause 					% Strike any key to continue

% Now let's run the ga for one generation.
[x endPop] = ga([0 9],'gademo1eval1',[],initPop,[1e-6 1 1],'maxGenTerm',1,...
  'normGeomSelect',[0.08],['arithXover'],[2],'nonUnifMutation',[2 1 3]);

x %The best found
%And plot the resulting the resulting population
plot (endPop(:,1),endPop(:,2),'ro')
pause 					% Strike any key to continue

% Now let's run the ga for 25 generations
[x endPop] = ga([0 9],'gademo1eval1',[],initPop,[1e-6 1 1],'maxGenTerm',25,...
  'normGeomSelect',[0.08],['arithXover'],[2],'nonUnifMutation',[2 1 3]);
x %The best found
% And plot the resulting the resulting population
plot (endPop(:,1),endPop(:,2),'y*')

% End of gademo1
````

</details>

#### gademo1eval1 · MATLAB · d77df377

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8bb58f7161db15e1c7933e2d81a8d41c2ee7ceb25e2beedf543dfacce1effee5`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/gademo1eval1.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [val,sol] = gaDemo1Eval(sol,options)
% Demonstration evaluation function used in gademo1.
% f(x)=x+10sin(5x)+7cos(4x)
%
% function [val,sol] = gaDemo1Eval(sol,options)
% 
% val - the fittness of this individual
% sol - the individual, returned to allow for Lamarckian evolution
% options - [current_generation]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

x=sol(1);
val = x + 10*sin(5*x)+7*cos(4*x);
````

</details>

#### gademo2 · MATLAB · 4069e2c2

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`e1468f440fc68eb1b96128a789e3d395b621f4be3d0976c42c1adde69f2331b5`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/gademo2.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/coranaEval.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/ga.m`

<details>
<summary>展开原始代码</summary>

````matlab
% GADEMO2 Use of the Genetic Optimization Toolbox

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

clf;
figure(gcf);
echo on
clc
% This demonstration show the use of the genetic toolbox to optimize a
% multi-dimensional non-convex function.
% The function is coded in the coranaEval.m file

pause %Strike any key to examine coranaEval
clc

type coranaEval.m

pause %Strike any key to continue
clc
%This function is basically a n dimensional parabola with rectangular
%pockets removed. Let's take a look at the function in 2-dimensions
%This may take a couple of minutes...
i=0;
a=-0.5:0.02:0.5;
for x=a
  i=i+1; j=0;
  for y=a
    j=j+1;
    z(i,j)=coranaEval([x y]);
  end
end
%Done!

%First let's look at it in each dimension independently
clg
plot(z(:,1)) %Plot a slice of the function in x max 250.25
%Notice the range is [250.0-250.25]
pause %Strike any key to continue
clg
plot(z(1,:)) %Plot a slice of the function in y 
%Notice the range is [0-250]
pause %Strike any key to continue
mesh(a,a,z);
view(30,60);
grid;
%Remember the deviation in y is 1000 times that of x.
pause %Strike any key to continue
clc
%Lets minimize this function in 4 dimensions between [-10,000 10,000].
%The ga is set up to maximize only.  Minimization of f(x) is equivalent to
%maximizing -f(x), so we use the negative of the Corana function.
type coranaMin.m

pause %Any key to continue
clc

%First set up the bounds
bounds = ones(4,1)*[-10000 10000];

%Now lets optimize
%This may take some time...
[x,endPop,bestSols,trace]=ga(bounds,'coranaMin');
%Done!

pause %Any key to continue
clc
%The first return is the optimal [x1 x2 x3 x4 val]
x

%Lets take a look at the performance of the ga during the run
plot(trace(:,1),trace(:,3),'y-')
hold on
plot(trace(:,1),trace(:,2),'r-')
xlabel('Generation'); ylabel('Fittness');
%The red line is a track of the best solution, the yellow is a track of the
%average of the population

pause %Any key to continue
clc

%End of gademo2
````

</details>

#### gademo3 · MATLAB · 3e384eb2

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0e42ed757454a59a699195646342fe1742bd1f2c81bdd1a89cde2220a93f28a3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/gademo3.m`

<details>
<summary>展开原始代码</summary>

````matlab
% This is a reference for writing evaluation, operator, selection and
% termination functions for the genetic optimization toolbox.

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

echo off
done =0;
while ~done
  K = menu('Choose a topic','Evaluation','Operators','Selection',...
    'Termination','Quit');
  
  if(K==1)
    clc;
    disp('EVALUATION');
    disp(' The evaluation function is the driving force behind the GA.  The');
    disp(' evaluation function is called from the GA to determine the');
    disp(' fitness of each solution string generated during the search.  An');
    disp(' example evaluation function is given below:');
    disp(' ');
    disp(' function [val,x] = gaDemo1Eval(sol,options)');
    disp(' x=sol(1);');
    disp(' val = x + 10*sin(5*x)+7*cos(4*x);    ');
    disp(' ');
    disp(' Note that the evaluation function must take two parameters,');
    disp(' sol and options.  Sol is a row vector of n+1 elements where');
    disp(' the first n elements are the parameters of interest.  The');
    disp(' n+1th element is the value of this solution.  The options');
    disp(' matrix is a row matrix of');
    disp(' ');
    disp(' [current generation, options]');
    disp(' ');
    disp(' The eval function must return both the value of the string,');
    disp(' val and the string itself, sol.  This is done so that');
    disp(' your evaluation can repair or improve the string.');
    disp(' ');
    disp(' An evaluation function is unique to the optimization of the');
    disp(' problem at hand, therefore, every time the ga is used for a');
    disp(' different problem, an evaluation function must be developed to');
    disp(' determine the fitness of the individuals.');
  end
  if(K==2)
    clc;    
    disp('OPERATORS');
    disp(' Operators provide the search mechanism of the GA.  The');
    disp(' operators are used to create new solutions based on existing');
    disp('solutions in the population.  There are two basic types of');
    disp(' operators, crossover and mutation.  Crossover takes two');
    disp(' individuals and produces two new individuals while mutation');
    disp(' alters one individual to produce a single new solution.  The');
    disp(' ga function calls each of the operators to produce new');
    disp(' solutions.  The function call for crossovers is as follows:');
    disp('');
    disp(' function [c1,c2] =crossover(p1,p2,bounds,Ops)'); 
    disp('');
    disp('where');
    disp(' p1 is the first parent ([solution_string function_value])');
    disp(' p2 is the second parent ([solution_string function_value])');
    disp(' bounds is the bounds matrix for the solution space');        
    disp(' ops is a vector of information, i.e. ');
    disp('[current_generation crossover_ops]');
    disp(' while the mutation function call is');
    disp(' similar but only takes one parent and returns one child.');
    disp(' function [c1] = mutation(p1,bounds,Ops)');
    disp(' ');
    disp(' The crossover operator must take all 4 arguments,');
    disp(' the two parents, the bounds of the search space,');
    disp(' the information on how much of the evolution has');
    disp(' taken place and any other special options required,');
    disp(' and similarly mutations must all take the three');
    disp(' arguments and return the resulting');
    disp(' child. ');
  end
  if(K==3)
    clc;    
    disp('SELECTION')
    disp(' The selection function determines which');
    disp(' of the individuals will survive and continue');
    disp(' on to the next generation.  The ga function');
    disp(' calls the selection function each generation');
    disp(' after all the new children have been');
    disp(' evaluated to determine their fitness using');
    disp(' the user provided evaluation function.');
    disp(' ');
    disp(' The basic function call used in the ga for');
    disp(' selection is: ');
    disp(' ');
    disp(' function[newPop] = selectFunction(oldPop,options) ');
    disp(' ');
    disp(' where newPop is the new population selected, ');
    disp(' oldPop is the current population, ');
    disp(' options is a vector for any other optional parameters.');
    disp(' ');
    disp(' Notice that all selection routines must take');
    disp(' three parameters, the old population from');
    disp(' which to select members from, and any');
    disp(' specific options to that particular selection');
    disp(' routine.  The function must return the new');
    disp(' population.');
  end
  if(K==4)
    clc;
    disp('TERMINATION')
    disp(' The termination function determines when to');
    disp(' stop the simulated evolution and return the');
    disp(' resulting population.  The ga function calls');
    disp(' the termination function once every');
    disp(' generation after the application of all of');
    disp(' the operator functions and the evaluation');
    disp(' function for the resulting children.  The');
    disp(' function call is of the format:');
    disp(' ');
    disp(' done = terminateFunction(options,bestPop,pop)');
    disp(' ');
    disp(' options is a vector of termination options');
    disp(' the first of which is always the current generation');
    disp(' bestPop is a matrix of the best individuals and the respective');
    disp(' generation it was found.  ');
    disp(' pop is the current population.');
  end
  if(K==5)
    done=1;
  end
end
````

</details>

#### heuristicXover · MATLAB · 92fc63f3

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ef01a21a13157ae9fb77cbaf9f5f3a50bc14a9c48da3d3696e88247ab0bdf0e4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/heuristicXover.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [c1,c2] = heuristicXover(p1,p2,bounds,Ops)
% Heuristic crossover takes two parents P1,P2 and performs an extrapolation
% along the line formed by the two parents outward in the direction of the
% better parent.
%
% function [c1,c2] = heuristicXover(p1,p2,bounds,Ops)
% p1      - the first parent ( [solution string function value] )
% p2      - the second parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options for heuristic crossover, [gen #heurXovers number_of_retries]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

retry=Ops(3); 				% Number of retries
i=0;
good=0;
b1=bounds(:,1)';
b2=bounds(:,2)';
numVar = size(p1,2)-1;
% Determine the best and worst parent
if(p1(numVar+1) > p2(numVar+1))
  bt = p1; 
  wt = p2;
else
  bt = p2;
  wt = p1;
end
while i<retry
  % Pick a random mix amount
  a = rand;
  % Create the child
  c1 = a * (bt - wt) + bt;
  
  % Check to see if child is within bounds
  if (c1(1:numVar) <= b2 & (c1(1:numVar) >= b1))
    i = retry;
    good=1;
  else
    i = i + 1;
  end
end

% If new child is not feasible just return the new children
if(~good) 
  c1 = wt;
end

% Crossover functions return two children therefore return the best
% and the new child created
c2 = bt;
end
````

</details>

#### initialize · MATLAB · 9121c9e6

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`b0aae211bd3d017d80af0852cd13c90f99e366c5e30fc466363d10149c1f800c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/initialize.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/b2f.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/calcbits.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/f2b.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [pop] = initialize(num,bounds,evalFN,evalOps,options)
% function [pop]=initialize(populationSize, variableBounds,evalFN,
%                           evalOps,options)
%    initialize creates a matrix of random numbers with 
%    a number of rows equal to the populationSize and a number
%    columns equal to the number of rows in bounds plus 1 for
%    the f(x) value which is found by applying the evalFN.
%
% pop            - the initial, evaluated, random population 
% populatoinSize - the size of the population, i.e. the number to create
% variableBounds - a matrix which contains the bounds of each variable, i.e.
%                  [var1_high var1_low; var2_high var2_low; ....]
% evalFN         - the evaluation fn, usually the name of the .m file for 
%                  evaluation
% evalOps        - any options to be passed to the eval function defaults []
% options        - options to the initialize function, ie. 
%                  [eps float/binary prec] where eps is the epsilon value 
%                  and the second option is 1 for float and 0 for binary, 
%                  prec is the precision of the variables defaults [1e-6 1]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

if nargin<5
  options=[1e-6 1];
end
if nargin<4
  evalOps=[];
end

if any(evalFN<48) %Not a .m file
  if options(2)==1 %Float GA
    estr=['x=pop(i,:); pop(i,xZomeLength)=', evalFN ';'];  
  else %Binary GA
    estr=['x=b2f(pop(i,:),bounds,bits); pop(i,xZomeLength)=', evalFN ';']; 
  end
else %A .m file
  if options(2)==1 %Float GA
    estr=['[pop(i,xZomeLength) pop(i,:)]=' evalFN '(pop(i,:),[0 evalOps]);'];  
  else %Binary GA
    estr=['x=b2f(pop(i,:),bounds,bits);[v x]=' evalFN ...
	'(x,[0 evalOps]); pop(i,:)=[f2b(x,bounds,bits) v];'];  
    end
end


numVars     = size(bounds,1); 		%Number of variables
rng         = (bounds(:,2)-bounds(:,1))'; %The variable ranges'

if options(2)==1 %Float GA
  xZomeLength = numVars+1; 		%Length of string is numVar + fit
  pop         = zeros(num,xZomeLength); 	%Allocate the new population
  pop(:,1:numVars)=(ones(num,1)*rng).*(rand(num,numVars))+...
    (ones(num,1)*bounds(:,1)');
else %Binary GA
  bits=calcbits(bounds,options(1));
  xZomeLength = sum(bits)+1; 		%Length of string is numVar + fit
  pop = round(rand(num,sum(bits)+1));
end
  
for i=1:num
  eval(estr);
end
````

</details>

#### maxGenTerm · MATLAB · 2cbc6246

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`486c85caf44d78be1603c1fb88819ea294c342bc4b9effa876ee51c9ad40df3a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/maxGenTerm.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [done] = maxGenTerm(ops,bPop,endPop)
% function [done] = maxGenTerm(ops,bPop,endPop)
% ops    - a vector of options [current_gen maximum_generation]
% bPop   - a matrix of best solutions [generation_found solution_string]
% endPop - the current generation of solutions

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

currentGen = ops(1);
maxGen     = ops(2);
done       = currentGen >= maxGen; 
````

</details>

#### multiNonUnifMutation · MATLAB · 6630a63f

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`63cb60366f073527d546094319f0769a62a191bb4568620626638e886fee67af`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/multiNonUnifMutation.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/delta.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [parent] = multiNonUnifMutation(parent,bounds,Ops)
% Multi-Non uniform mutation changes all of the parameters of the parent
% based on a non-uniform probability distribution.  This Gaussian
% distribution starts wide, and narrows to a point distribution as the
% current generation approaches the maximum generation.
%
% function [newSol] = multiNonUnifMutate(parent,bounds,Ops)
% parent  - the first parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options for multiNonUnifMutation 
%          [gen #MultiNonUnifMutations maxGen b]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

cg=Ops(1); 				% Current Generation
mg=Ops(3); 				% Maximum Number of Generations
b=Ops(4);                               % Shape parameter
df = bounds(:,2) - bounds(:,1); 	% Range of the variables
numVar = size(parent,2)-1; 		% Get the number of variables
% Now mutate that point
md = round(rand(1,numVar));
for i = 1:numVar
  if md(i)
    parent(i)=parent(i)+delta(cg,mg,bounds(i,2)-parent(i),b);
  else
    parent(i)=parent(i)-delta(cg,mg,parent(i)-bounds(i,1),b);
  end
end
````

</details>

#### nonUnifMutation · MATLAB · 82eb32cd

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`2c8713c06a631c80c4bc4f325b3a5d03bffec23cdfeb9e00120d193600da6748`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/nonUnifMutation.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/delta.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [parent] = nonUnifMutate(parent,bounds,Ops)
% Non uniform mutation changes one of the parameters of the parent
% based on a non-uniform probability distribution.  This Gaussian
% distribution starts wide, and narrows to a point distribution as the
% current generation approaches the maximum generation.
%
% function [newSol] = multiNonUnifMutate(parent,bounds,Ops)
% parent  - the first parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options for nonUnifMutate[gen #NonUnifMutations maxGen b]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

cg=Ops(1); 				% Current Generation
mg=Ops(3);                              % Maximum Number of Generations
b=Ops(4);                               % Shape parameter
df = bounds(:,2) - bounds(:,1); 	% Range of the variables
numVar = size(parent,2)-1; 		% Get the number of variables
% Pick a variable to mutate randomly from 1 to number of vars
mPoint = round(rand * (numVar-1)) + 1;
md = round(rand); 			% Choose a direction of mutation
if md 					% Mutate towards upper bound
  newValue=parent(mPoint)+delta(cg,mg,bounds(mPoint,2)-parent(mPoint),b);
else 					% Mutate towards lower bound
  newValue=parent(mPoint)-delta(cg,mg,parent(mPoint)-bounds(mPoint,1),b);
end
parent(mPoint) = newValue; 		% Make the child
end
````

</details>

#### normGeomSelect · MATLAB · d62808aa

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；执行归一化或标准化以统一变量尺度。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`f1c4675b3d99f25bd0d51efdc519453ecba055ca46590bc8d6c54a8a3801c57a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/normGeomSelect.m`

<details>
<summary>展开原始代码</summary>

````matlab
function[newPop] = normGeomSelect(oldPop,options)
% NormGeomSelect is a ranking selection function based on the normalized
% geometric distribution.  
%
% function[newPop] = normGeomSelect(oldPop,options)
% newPop  - the new population selected from the oldPop
% oldPop  - the current population
% options - options to normGeomSelect [gen probability_of_selecting_best]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

q=options(2); 				% Probability of selecting the best
e = size(oldPop,2); 			% Length of xZome, i.e. numvars+fit
n = size(oldPop,1); 			% Number of individuals in pop
newPop = zeros(n,e); 			% Allocate space for return pop
fit = zeros(n,1); 			% Allocates space for prob of select
x=zeros(n,2); 			        % Sorted list of rank and id
x(:,1) =[n:-1:1]'; 			% To know what element it was
[y x(:,2)] = sort(oldPop(:,e)); 	% Get the index after a sort
r = q/(1-(1-q)^n); 			% Normalize the distribution, q prime
fit(x(:,2))=r*(1-q).^(x(:,1)-1); 	% Generates Prob of selection 
fit = cumsum(fit); 			% Calculate the cumulative prob. func
rNums=sort(rand(n,1)); 			% Generate n sorted random numbers
fitIn=1; newIn=1; 			% Initialize loop control
while newIn<=n 				% Get n new individuals
  if(rNums(newIn)<fit(fitIn)) 		
    newPop(newIn,:) = oldPop(fitIn,:); 	% Select the fitIn individual 
    newIn = newIn+1; 			% Looking for next new individual
  else
    fitIn = fitIn + 1; 			% Looking at next potential selection
  end
end
end
````

</details>

#### optMaxGenTerm · MATLAB · c19ef181

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`c8285e812483cb1895c8b250a12aedb817a77c3819b8fa2de44dc6336838b7a9`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/optMaxGenTerm.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/maxGenTerm.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [done] = maxGenTerm(ops,bPop,endPop)
% function [done] = maxGenTerm(ops,bPop,endPop)
% ops    - a vector of options [current_gen maximum_generation epsilon]
% bPop   - a matrix of best solutions [generation_found solution_string]
% endPop - the current generation of solutions

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

currentGen = ops(1);
maxGen     = ops(2);
optimal    = ops(3);
epsilon    = ops(4);
fitIndex   = size(endPop,2);
bestSolVal = max(endPop(:,fitIndex));
done       = (currentGen >= maxGen) | ((optimal - bestSolVal) <= epsilon);
````

</details>

#### parse · MATLAB · d2f5ab45

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4cac9baa65366e9604e3bf061005c8c9c73254320accbad0508aab2e733e3330`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/parse.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [x] = parse(inStr)
% parse is a function which takes in a string vector of blank separated text
% and parses out the individual string items into a n item matrix, one row
% for each string.
%
% function [x] = parse(inStr)
% x     - the return matrix of strings
% inStr - the blank separated string vector

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

sz=size(inStr);
strLen=sz(2);
x=blanks(strLen);
wordCount=1;
last=0;
for i=1:strLen,
  if inStr(i) == ' '
    wordCount = wordCount + 1;
    x(wordCount,:)=blanks(strLen);
    last=i;
  else
    x(wordCount,i-last)=inStr(i);
  end
end
````

</details>

#### roulette · MATLAB · 22f64a70

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`7f54031a43bf3eadb6aa75569d51938f0c479d70df78fd1e7b07720bf1476826`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/roulette.m`

<details>
<summary>展开原始代码</summary>

````matlab
function[newPop] = roulette(oldPop,options)
% roulette is the traditional selection function with the probability of
% surviving equal to the fitness of i / sum of the fitness of all individuals
%
% function[newPop] = roulette(oldPop,options)
% newPop  - the new population selected from the oldPop
% oldPop  - the current population
% options - options [gen]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

% Get the parameters of the population
numVars = size(oldPop,2);
numSols = size(oldPop,1);

% Generate the relative probabilities of selection
totalFit = sum(oldPop(:,numVars));
prob=oldPop(:,numVars) / totalFit; 
prob=cumsum(prob);

rNums=sort(rand(numSols,1)) 		% Generate random numbers

% Select individuals from the oldPop to the new
fitIn=1;newIn=1;
while newIn<=numSols
  if(rNums(newIn)<prob(fitIn))
    newPop(newIn,:) = oldPop(fitIn,:);
    newIn = newIn+1;
  else
    fitIn = fitIn + 1;
  end
end
end
````

</details>

#### simpleXover · MATLAB · d4576edd

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`558dd6bef980160834395343a34418a7f4bde61374b224fefac9b5b5fa146a4e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/simpleXover.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [c1,c2] = simpleXover(p1,p2,bounds,Ops)
% Simple crossover takes two parents P1,P2 and performs simple single point
% crossover.  
%
% function [c1,c2] = simpleXover(p1,p2,bounds,Ops)
% p1      - the first parent ( [solution string function value] )
% p2      - the second parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options matrix for simple crossover [gen #SimpXovers].

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

numVar = size(p1,2)-1; 			% Get the number of variables 
% Pick a cut point randomly from 1-number of vars
cPoint = round(rand * (numVar-2)) + 1;

c1 = [p1(1:cPoint) p2(cPoint+1:numVar+1)]; % Create the children
c2 = [p2(1:cPoint) p1(cPoint+1:numVar+1)];
end
````

</details>

#### tournSelect · MATLAB · 25548e10

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`89e976b3c4590675501c98c739fa5d7023e0b3d67121436623eccdb9961823e1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/tournSelect.m`

<details>
<summary>展开原始代码</summary>

````matlab
function[newPop] = tournSelect(oldPop,options)
% Performs a tournament selection.
%
% function[newPop] = tournSelect(oldPop,options)
% newPop  - the new population selected from the oldPop
% oldPop  - the current population
% options - options to normGeomSelect [gen tournament_size]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

tournSize=options(2); 			% Get the number of tournaments
e = size(oldPop,2); 			% xZome length
n = size(oldPop,1); 			% number in Population
newPop = zeros(n,e); 			% Create the memory for newPop
tourns=floor(rand(tournSize,n)*n)+1; 	% Schedule of tournaments
% Determine the winner of the tournaments
[c b]=max(reshape(oldPop(tourns,e),tournSize,n));
newPop=oldPop(diag(tourns(b,:)),:); 	% Copy the winners in to newPop
end
````

</details>

#### unifMutation · MATLAB · 0d5e2eba

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3bcc9920437174a261b9c338297dabffe002bf911d18625972e265594fd05741`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/GAOT/unifMutation.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [parent] = uniformMutate(parent,bounds,Ops)
% Uniform mutation changes one of the parameters of the parent
% based on a uniform probability distribution.
%
% function [newSol] = multiNonUnifMutate(parent,bounds,Ops)
% parent  - the first parent ( [solution string function value] )
% bounds  - the bounds matrix for the solution space
% Ops     - Options for uniformMutation [gen #UnifMutations]

% Binary and Real-Valued Simulation Evolution for Matlab 
% Copyright (C) 1996 C.R. Houck, J.A. Joines, M.G. Kay 
%
% C.R. Houck, J.Joines, and M.Kay. A genetic algorithm for function
% optimization: A Matlab implementation. ACM Transactions on Mathmatical
% Software, Submitted 1996.
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 1, or (at your option)
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details. A copy of the GNU 
% General Public License can be obtained from the 
% Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

df = bounds(:,2) - bounds(:,1); 	% Range of the variables
numVar = size(parent,2)-1; 		% Get the number of variables 
% Pick a variable to mutate randomly from 1-number of vars
mPoint = round(rand * (numVar-1)) + 1;
newValue = bounds(mPoint,1)+rand * df(mPoint); % Now mutate that point
parent(mPoint) = newValue; 		% Make the child
end
````

</details>

#### binaryExample · MATLAB · 0d31661f

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`e47c7170796ddf355af3d400e839d07519f4e02b34396b20a8d515ef9ef82b42`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/binaryExample.m`

<details>
<summary>展开原始代码</summary>

````matlab

% This script shows how to use the ga using a float representation. 
% You should see the demos for
% more information as well. gademo1, gademo2, gademo3
global bounds

% Setting the seed back to the beginning for comparison sake
rand('seed',0)

% Crossover Operators
xFns = 'simpleXover';
xOpts = [.4];

% Mutation Operators
mFns = 'binaryMutation';

mOpts = [0.005];

% Termination Operators
termFns = 'maxGenTerm';
termOps = [200]; % 200 Generations

% Selection Function
selectFn = 'roulette'
selectOps = [];

% Evaluation Function
evalFn = 'gaMichEval';
evalOps = [];

type gaMichEval

% Bounds on the variables
bounds = [-3 12.1; 4.1 5.8];

% GA Options [epsilon float/binar display]
gaOpts=[1e-6 0 1];

% Generate an intialize population of size 20
startPop = initialize(20,bounds,'gaMichEval',[],[1e-6 0]);

% Lets run the GA
pause

[x endPop bestPop trace]=ga(bounds,evalFn,evalOps,startPop,gaOpts,...
    termFns,termOps,selectFn,selectOps,xFns,xOpts,mFns,mOpts);

pause

% x is the best solution found
x
pause

% endPop is the ending population
endPop
pause

% trace is a trace of the best value and average value of generations
trace
pause

% Plot the best over time
clg
plot(trace(:,1),trace(:,2));
pause

% Add the average to the graph
hold on
plot(trace(:,1),trace(:,3));
pause

% Lets increase the population size by running the defaults
% 
termOps=[100];
[x endPop bestPop trace]=ga(bounds,evalFn,evalOps,[],gaOpts,termFns,termOps,...
    selectFn,selectOps);

% x is the best solution found
x
pause

% endPop is the ending population
endPop
pause

% trace is a trace of the best value and average value of generations
trace
pause

% Plot the best over time
clg
plot(trace(:,1),trace(:,2));
pause

% Add the average to the graph
hold on
plot(trace(:,1),trace(:,3));
pause
````

</details>

#### floatExample · MATLAB · d748ee51

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`7f60fda7a0a68f9ee88656fd3c56775ae44a1052504d731e076a9960f4296101`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/floatExample.m`

<details>
<summary>展开原始代码</summary>

````matlab

% This script shows how to use the ga using a float representation. 
% You should see the demos for
% more information as well. gademo1, gademo2, gademo3
global bounds

% Setting the seed to the same for binary
% rand('seed',sd)

% Crossover Operators
xFns = 'arithXover heuristicXover simpleXover';
xOpts = [1 0; 1 3; 1 0];

% Mutation Operators
mFns = 'boundaryMutation multiNonUnifMutation nonUnifMutation unifMutation';

mOpts = [2 0 0;3 200 3;2 200 3;2 0 0];

% Termination Operators
termFns = 'maxGenTerm';
termOps = [200]; % 200 Generations

% Selection Function
selectFn = 'normGeomSelect';
selectOps = [0.08];

% Evaluation Function
evalFn = 'gaMichEval';
evalOps = [];

type gaMichEval

% Bounds on the variables
bounds = [-3 12.1; 4.1 5.8];

% GA Options [epsilon float/binar display]
gaOpts=[1e-6 1 1];

% Generate an intialize population of size 20
startPop = initialize(20,bounds,'gaMichEval',[1e-6 1]);

% Lets run the GA
pause

[x endPop bestPop trace]=ga(bounds,evalFn,evalOps,startPop,gaOpts,...
    termFns,termOps,selectFn,selectOps,xFns,xOpts,mFns,mOpts);

pause

% x is the best solution found
x
pause

% endPop is the ending population
endPop
pause

% bestPop is the best solution tracked over generations
bestPop
pause

% trace is a trace of the best value and average value of generations
trace
pause

% Plot the best over time
clg
plot(trace(:,1),trace(:,2));
pause

% Add the average to the graph
hold on
plot(trace(:,1),trace(:,3));
pause

% Lets increase the population size by running the defaults
% 

[x endPop bestPop trace]=ga(bounds,evalFn,evalOps,[],gaOpts);

% x is the best solution found
x
pause

% endPop is the ending population
endPop
pause

% bestPop is the best solution tracked over generations
bestPop
pause

% trace is a trace of the best value and average value of generations
trace
pause

% Plot the best over time
clg
plot(trace(:,1),trace(:,2));
pause

% Add the average to the graph
hold on
plot(trace(:,1),trace(:,3));
pause
````

</details>

#### floatGrad · MATLAB · 845acaba

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`16519071d8f15701b75a484561ea20052f49d86d5289e7ba18aa24d5498ba804`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/floatGrad.m`

<details>
<summary>展开原始代码</summary>

````matlab
echo off
load seed.mat
rand('seed',sd);
echo on
% This script shows how to use the ga. You should see the demos for
% more information as well. gademo1, gademo2, gademo3
global bounds

% Crossover Operators
xFns = 'arithXover heuristicXover simpleXover';
xOpts = [2 0; 2 3; 2 0];

% Mutation Operators
mFns = 'boundaryMutation multiNonUnifMutation nonUnifMutation unifMutation';
mOpts = [4 0 0;6 10 3;4 10 3;4 0 0];

% Termination Operators
termFns = 'maxGenTerm';
termOps = [10];

% Selection Function
selectFn = 'normGeomSelect';
selectOps = [0.06];

% Evaluation Function takes two options 
% prob to use gradient, prob to perform Lamarkian evolution
evalFn = 'gaZBGradEval';
evalOps = [1.00 1.00];

% Bounds on the variables
bounds = [-3 12.1; 4.1 5.8];

% GA Options [epsilon float/binar display]
gaOpts=[1e-6 1 1];

% Generate an intialize population of size 80
startPop = initialize(80,bounds,evalFn,evalOps,[1e-6 1]);

% Lets run the GA using Lamarkian Evolution

[x endPop bestPop trace]=ga(bounds,evalFn,evalOps,startPop,gaOpts,...
    termFns,termOps,selectFn,selectOps,xFns,xOpts,mFns,mOpts);

% x is the best solution found
x
pause

% endPop is the ending population
endPop
pause

% bestPop is the best solution tracked over generations
bestPop
pause

% trace is a trace of the best value and average value of generations
trace
pause

% Plot the best over time
clg
plot(trace(:,1),trace(:,2));
pause

% Add the average to the graph
hold on
plot(trace(:,1),trace(:,3));
pause
````

</details>

#### 相似实现组 · MATLAB · 581632fd

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：gaMichEval.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9c6347cb529905b7538f1c15dcde5a62da53812e643cdb4fc1d903d6eaf0a3c8`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/gaMichEval.m`

<details>
<summary>展开原始代码</summary>

````matlab
function  [val,sol]=gaNichEval(sol,options)
val = 21.5 + sol(1)*sin(4*pi*sol(1))+sol(2)*sin(20*pi*sol(2));
%G=zeros(0);
%val = sqrt(sol(1)) * sin(2*sol(1)) + sqrt(sol(1))*cos(5*sol(1))+5;
````

</details>

##### 变体 2：gaSimpleEval.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1b736ca4c5c087ab5f01d52661fc5f6137a230f4285b8a043bc96598b65aa598`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/gaSimpleEval.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [val,sol] = gaTestEval(sol,options)
val = 21.5 + sol(1) * sin(4*pi*sol(1)) + sol(2)*sin(20*pi*sol(2));
%G=zeros(0);
%val = sqrt(sol(1)) * sin(2*sol(1)) + sqrt(sol(1))*cos(5*sol(1))+5;
````

</details>

#### gaZBGrad · MATLAB · 4bad5755

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b5a2df3af293828b22600cff26452e96d7a50ac2de08e40cfa89cc43d676563c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/gaZBGrad.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [val,G] = gaZBGrad(sol)

% Constrain minimizes so we have to take the - to maximize
val = -(21.5 + sol(1) * sin(4*pi*sol(1)) + sol(2)*sin(20*pi*sol(2)));
G=zeros(0);
````

</details>

#### gaZBGradEval · MATLAB · 659a0a24

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1ab07a9cafc850137759649eeeb15345ca16f1d8a2a3c9067034e0206c7a6cc6`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/gaZBGradEval.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [val,nsol] = gaZBGradEval(sol,options)

% This evaluation function takes in a potential solution and two options
% options(3) is the percent of time to perform the gradient heuristic to the
% potential solution
% options(4) is the percentage of time to update the solution based on the
% outcome of the gradient heuristic
% options [currentGen maxGen eval_with_constr update_with_constr]
nsol=sol;
if (rand<options(2))
  % Perform a gradient search
  global bounds;
  [x opt]=constr('gaZBGrad',sol(1:2),[],bounds(:,1),bounds(:,2));
  % opt(8) is the objective val...
      val=-opt(8);
  if (rand<options(3))
    nsol(1:2)=x;
  end
else
  val=-gaTestEval(sol(1:2),[]);
end
````

</details>

#### gas · MATLAB · 8fa5057f

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`22e923000ba3ac417d65e319e67513cdc218431c1e8b2bba399db5fa5529ff8d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/gas.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [val,sol] = gaTestEval(sol,options)
val=sum(sol(1:3));
````

</details>

#### startup · MATLAB · 5e9e9103

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7a31db6b29276c6ca2dc034bb836520ca19dbf905b4af001a50177a412757e25`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/工具箱/遗传算法工具箱/Genetic Algorithms/startup.m`

<details>
<summary>展开原始代码</summary>

````matlab
path(path,'/afs/eos/info/ie/ie589k_info/GAOT');
````

</details>

#### ceshide · MATLAB · 8ba6abae

- 归属算法：遗传算法GA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“数据读取与预处理”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`a340ffcbf05f99980a5b09aad080efa8eca418f5100c063929276a17ca6b76de`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/MTSP问题求解/MTSP的求解程序代码/ceshide.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/MTSP问题求解/MTSP的求解程序代码/floyed.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/MTSP问题求解/MTSP的求解程序代码/mtspf_ga.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear all;clc;close all;
load lujing;                             %其中存储图的邻接矩阵以县政府为起点
dmat=floyed(tu);                         %求图所对应的最短路径矩阵；
[x1,x2,x3,x4]=mtspf_ga(dmat,3,16,100);   %返回求得最优解。
````

</details>

#### floyed · MATLAB · 245be982

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `floyed`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ccb198e8f01bcb03064ed5f427c69a8468a5a49611dc2f116d8448c5617c9b83`
- 语言：MATLAB
- 符号：`floyed`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/MTSP问题求解/MTSP的求解程序代码/floyed.m`

<details>
<summary>展开原始代码</summary>

````matlab
function  matrix=floyed(G)
%存储无向图的邻接矩阵 
%{
G=[ inf inf 10 inf 30 100;
    inf inf 5  inf inf inf;
    inf 5 inf 50 inf inf;
    inf inf inf inf inf 10;
    inf inf inf 20 inf 60;
    inf inf inf inf inf inf;];
%}
d(1,:,:)=G;
%处理第一行与第一列 对应相加时，可以优化的距离
for i=1:size(G,1)
    for j=1:size(G,2)
        s(i,j).trace=i;
        if d(1,i,j)<=d(1,i,1)+d(1,1,j)
           d(1,i,j)=d(1,i,j);
        else
           d(1,i,j)=d(1,i,1)+d(1,1,j);
        end
    end
end
%处理从第二 到 顶点个数 个时的 路径优化
for k=2:size(G,1)
    for i=1:size(G,1)
        for j=1:size(G,1)
            if d(k-1,i,j)<=d(k-1,i,k)+d(k-1,k,j)
                d(k,i,j)=d(k-1,i,j);
            else
                d(k,i,j)=d(k-1,i,k)+d(k-1,k,j);
            end
        end
    end
end
matrix=zeros(size(G,1),size(G,1));
matrix=d(size(G,1),:,:);
matrix=reshape(matrix,size(G,1),size(G,1));
````

</details>

#### mtspf_ga · MATLAB · 79411421

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `mtspf_ga`、`randbreaks`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`8abadf1a9de5ec2d001933d0cba8d15089bb3e4dd7fc9b664dc9c67ff3759315`
- 语言：MATLAB
- 符号：`mtspf_ga`, `randbreaks`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/MTSP问题求解/MTSP的求解程序代码/mtspf_ga.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/MTSP问题求解/MTSP的求解程序代码/myLength.m`

<details>
<summary>展开原始代码</summary>

````matlab
function varargout = mtspf_ga(dmat,salesmen,min_tour,pop_size,num_iter,show_prog,show_res)
%dmat 任意两城市间的最短路径矩阵通过floyed算法求得结果。
%salesmen 旅行商个数
%min_tour 每个旅行商最少访问的城市数
%pop_size 种群个体数
%num_iter  迭代的代数
%show_prog,show_res 显示的参数设定
nargs = 7;                      %处理输入参数，用来给定一些默认的参数；
for k = nargin:nargs-1
    switch k
        case 0
            dmat = 10*rand(20,20);
        case 1
            salesmen = 5;
        case 2
            min_tour = 2;
        case 3
            pop_size = 80;
        case 4
            num_iter = 5e3;
        case 5
            show_prog = 1;
        case 6
            show_res = 1;
        otherwise
    end
end

% 检查输入 矩阵
[nr,nc] = size(dmat);
if nr ~= nc
    error('Invalid XY or DMAT inputs!')
end
n = nr - 1; % 除去起始的城市后剩余的城市的数

% 输入参数的检查
salesmen = max(1,min(n,round(real(salesmen(1)))));
min_tour = max(1,min(floor(n/salesmen),round(real(min_tour(1)))));
pop_size = max(8,8*ceil(pop_size(1)/8));
num_iter = max(1,round(real(num_iter(1))));
show_prog = logical(show_prog(1));
show_res = logical(show_res(1));

% 初始化路线、断点的选择
num_brks = salesmen-1;
dof = n - min_tour*salesmen;          % 可以自由访问的城市数
addto = ones(1,dof+1);
for k = 2:num_brks
    addto = cumsum(addto);
end
cum_prob = cumsum(addto)/sum(addto);

% 初始化种群
pop_rte = zeros(pop_size,n);          % 路径集合的种群
pop_brk = zeros(pop_size,num_brks);   % 断点集合的种群
for k = 1:pop_size
    pop_rte(k,:) = randperm(n)+1;
    pop_brk(k,:) = randbreaks();
end

% 选择绘图时的个商人的颜色  可删去；
clr = [1 0 0; 0 0 1; 0.67 0 1; 0 1 0; 1 0.5 0];
if salesmen > 5
    clr = hsv(salesmen);
end

% 开始运行遗传算法过程
global_min = Inf;                %初始化最短路径
total_dist = zeros(1,pop_size);
dist_history = zeros(1,num_iter);
tmp_pop_rte = zeros(8,n);        %当前的路径设置
tmp_pop_brk = zeros(8,num_brks); %当前的断点设置
new_pop_rte = zeros(pop_size,n); %更新的路径设置
new_pop_brk = zeros(pop_size,num_brks);%更新的断点设置
if show_prog
    pfig = figure('Name','MTSPF_GA | Current Best Solution','Numbertitle','off');
end
for iter = 1:num_iter
    % 评价每一代的种群 适应情况并作出选择。
    for p = 1:pop_size
        d = 0;
        p_rte = pop_rte(p,:);
        p_brk = pop_brk(p,:);
        rng = [[1 p_brk+1];[p_brk n]]';
        for s = 1:salesmen
            
            d = d + dmat(1,p_rte(rng(s,1))); % 添加开始的路径
            for k = rng(s,1):rng(s,2)-1
                d = d + dmat(p_rte(k),p_rte(k+1));
            end
            d = d + dmat(p_rte(rng(s,2)),1); % 添加结束的的路径
            dis(p,s)=d;
            %d=d+myLength(dmat,p_rte(rng(s,1):rng(s,2)));%可调用函数处理
        end
        total_dist(p) = d;
        %distan(p)=max(dis(p,:));%计算三个人中的最大值
    end
    
    % 在每代种群中找到最好的路径
    [min_dist,index] = min(total_dist);
    dist_history(iter) = min_dist;     %+max(distan);

    if min_dist < global_min
        global_min = min_dist;
        opt_rte = pop_rte(index,:);             %最优的最短路径
        opt_brk = pop_brk(index,:);             %最优的断点设置
        rng = [[1 opt_brk+1];[opt_brk n]]';     %设置记录断点的方法
    end

    % 遗传算法算子的操作集合
    rand_grouping = randperm(pop_size);
    for p = 8:8:pop_size
        rtes = pop_rte(rand_grouping(p-7:p),:);
        brks = pop_brk(rand_grouping(p-7:p),:);
        dists = total_dist(rand_grouping(p-7:p));
        [ignore,idx] = min(dists);
        best_of_8_rte = rtes(idx,:);
        best_of_8_brk = brks(idx,:);
        rte_ins_pts = sort(ceil(n*rand(1,2)));
        I = rte_ins_pts(1);
        J = rte_ins_pts(2);
        for k = 1:8 % 产生新的方案
            tmp_pop_rte(k,:) = best_of_8_rte;
            tmp_pop_brk(k,:) = best_of_8_brk;
            switch k
                case 2 % 倒置操作
                    tmp_pop_rte(k,I:J) = fliplr(tmp_pop_rte(k,I:J));
                case 3 % 互换操作
                    tmp_pop_rte(k,[I J]) = tmp_pop_rte(k,[J I]);
                case 4 % 滑动平移操作
                    tmp_pop_rte(k,I:J) = tmp_pop_rte(k,[I+1:J I]);
                case 5 % 更新断点
                    tmp_pop_brk(k,:) = randbreaks();
                case 6 % 倒置并更新断点
                    tmp_pop_rte(k,I:J) = fliplr(tmp_pop_rte(k,I:J));
                    tmp_pop_brk(k,:) = randbreaks();
                case 7 % 互换并更新断点
                    tmp_pop_rte(k,[I J]) = tmp_pop_rte(k,[J I]);
                    tmp_pop_brk(k,:) = randbreaks();
                case 8 % 评议并更新断点
                    tmp_pop_rte(k,I:J) = tmp_pop_rte(k,[I+1:J I]);
                    tmp_pop_brk(k,:) = randbreaks();
                otherwise % 不进行操做
            end
        end
        new_pop_rte(p-7:p,:) = tmp_pop_rte;
        new_pop_brk(p-7:p,:) = tmp_pop_brk;
    end
    pop_rte = new_pop_rte;
    pop_brk = new_pop_brk;
end

% 返回结果部分
rng = [[1 opt_brk+1];[opt_brk n]]';
dis_e=zeros(1,salesmen);    %设置并计算每个旅行商的最短路径
for s = 1:salesmen
    dis_e(s)=myLength(dmat,opt_rte(rng(s,1):rng(s,2)));
end

if nargout
    varargout{1} = opt_rte;
    varargout{2} = opt_brk;
    varargout{3} = min_dist;
    varargout{4} = dis_e;
end
%做出迭代过程的图示
plot(dist_history);
grid on;xlabel('迭代的代数');ylabel('所走的路径之和');
    % 随机产生一套断点 的集合
    function breaks = randbreaks()
        if min_tour == 1 % 一个旅行商时，没有断点的设置
            tmp_brks = randperm(n-1);
            breaks = sort(tmp_brks(1:num_brks));
        else % 强制断点至少  找 到最短的履行长度
            num_adjust = find(rand < cum_prob,1)-1;
            spaces = ceil(num_brks*rand(1,num_adjust));
            adjust = zeros(1,num_brks);
            for kk = 1:num_brks
                adjust(kk) = sum(spaces == kk);
            end
            breaks = min_tour*(1:num_brks) + cumsum(adjust);
        end
    end
end
````

</details>

#### myLength · MATLAB · c7d68c9f

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `myLength`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b3387939f0f3355f00b9bb8e9714d114e26737bcbdba2f7e42d88c78d99de7b6`
- 语言：MATLAB
- 符号：`myLength`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/MTSP问题求解/MTSP的求解程序代码/myLength.m`

<details>
<summary>展开原始代码</summary>

````matlab
function len=myLength(D,p)
N=length(p);
len=D(p(1,N),1)+D(1,p(1,1));
for i=1:(N-1)
    len=len+D(p(1,i),p(1,i+1));
end
````

</details>

#### 基于Matlab的遗传算法解决TSP问题的报告 · MATLAB · d0ba450e

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `ga`、`plot_ga`、`start`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`5fbac372e478779091bd7d3e055125ade49599c2cf583edcaf7ba9ba854eb3ad`
- 语言：MATLAB
- 符号：`ga`, `plot_ga`, `start`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/基于Matlab的遗传算法解决TSP问题的报告.txt`

<details>
<summary>展开原始代码</summary>

````matlab
----------------------- Page 1-----------------------

                         基于Matlab的遗传算法解决TSP问题 

                         基于Matlab的遗传算法解决TSP问题 

          报告题目：基基于于MMaattllaabb的的遗遗传传算算法法解解决决TTSSPP问问题题 



说明： 

说明： 

说说明明：：该文包括了基于Matlab的遗传算法解决TSP问题的 



基本说明，并在文后附录了实现该算法的所有源代码。此代 



码经过本人的运行，没有发现错误，结果比较接近理论最优 



值，虽然最优路径图有点交叉。 



      因为本人才疏学浅，本报告及源代码的编译耗费了本人 



较多的时间与精力，特收取下载积分，还请见谅。若有什么 



问题，可以私信，我们共同探讨这一问题。 



      希望能对需要这方面的知识的人有所帮助！ 


----------------------- Page 2-----------------------

1. 

1.问题介绍 

11.. 



    旅行商问题(Traveling Salesman Problem，简称TSP)是一个经典的组合优 

化问题。它可以描述为：一个商品推销员要去若干个城市推销商品，从一个城市 

出发，需要经过所有城市后，回到出发地，应如何选择行进路线，以使总行程最 

短。从图论的角度看，该问题实质是在一个带权完全无向图中。找一个权值最小 

的Hemilton回路。其数学描述为：设有一个城市集合其中每对城市之间的距离 

d c,c ∈R+ ，求一对经过C中每个城市一次的路线 c ,c ,⋯c  使 

  ( i j)                                          ( Π1  Π2   Πn) 



                              n−1 



                          min  d c ,c       +d c ,c 

                             ∑ ( Πi  Π i+1 )   ( Πn  Π ) 

                                        ( )           1 

                              i=1 



    其中Π ,Π ,⋯Π 是1，2⋯n 的一个置换。 

           1  2   n  (     ) 



2. 

2.遗传算法 

22.. 



2.1遗传算法基本原理 

2.1遗传算法基本原理 

22..11遗遗传传算算法法基基本本原原理理 



    遗传算法是由美国J.Holland教授于1975年在他的专著《自然界和人工系 

统的适应性》中首先提出的，它是一类借鉴生物界自然选择和自然遗传机制的随 

机化搜索算法。 

    遗传算法模拟自然选择和自然遗传过程中发生的繁殖、交叉和基因突变现 

象，在每次迭代中都保留一组候选解，并按某种指标从解群中选取较优的个体， 

利用遗传算子(选择、交叉和变异)对这些个体进行组合，产生新一代的候选解群， 

重复此过程，直到满足某种收敛指标为止。 

    遗传算法，在本质上是一种不依赖具体问题的直接搜索方法，是一种求解问 

题的高效并行全局搜索方法。遗传算法在模式识别、神经网络、图像处理、机器 

学习、工业优化控制、自适应控制、负载平衡、电磁系统设计、生物科学、社会 

科学等方面都得到了应用。在人工智能研究中，现在人们认为“遗传算法、自适 

应系统、细胞自动控制、混沌理论与人工智能一样，都是对今后十年的计算技术 

有重大影响的关键技术”。 



2.2遗传算法的流程 

2.2遗传算法的流程 

22..22遗遗传传算算法法的的流流程程 



    标准的遗传算法包括群体的初始化，选择，交叉，变异操作。流程图如图1 

所示，其主要步骤可描述如下： 

    （1）随机产生一组初始个体构成的初始种群，并评价每一个个体的适配值。 

    （2）判断算法的收敛准则是否满足。若满足输出搜索结果；否则执行以下 

步骤。 


----------------------- Page 3-----------------------

     （3）根据适配值大小以一定方式执行选择操作。 

     （4）按交叉概率Pc执行交叉操作。 

     （5）按变异概率Pm执行变异操作。 

       6             2 

     （ ）返回步骤（ ）。 



                            图 1  遗传算法流程图 



3.TSP 

3.TSP 

33..TTSSPP问题的遗传算法设计与实现 



3.1TSP 问题的图论描述 

3.1TSP 问题的图论描述 

33..11TTSSPP问问题题的的图图论论描描述述 



     求最短路径问题，用图论术语描述如下：在图G(V,A)中，V表示顶点集合， 



V=(v1,v2,…,vn)对G中的某一边(v,v )，相应的有一个数d(v,v )，如果G中不 

                                 i  j                       i j 



存在边(v,v )，则令d(v,v )无穷大，如果把d(v,v )认为是边(v,v )的长度， 

         i  j           i  j                    i  j            i  j 



则通路的长度定义为组成路的各条边的长度总和。顶点v,v 之间是否有边相连， 

                                                       i  j 



由邻接矩阵来决定。 


----------------------- Page 4-----------------------

              A               v         e          G             A=[  ] 

    邻接矩阵 ：对一个具有 个顶点， 条边的图 的邻接矩阵                                      a 是一 

                                                                       ij 



   v×v                 =1                       =0      vi  vj 

个      阶方阵，其中a  ，表示v和v 邻接，a                        表示 和 不相邻接（或 

                      ij         i    j        ij 



i=j）。 



3.2读取txt 文件 

3.2读取txt 文件 

33..22读读取取ttxxtt文文件件 



    标准的测试文件一般都是存储 n*2 的 txt 文件，为此本人编译了一个 

readfile.m的程序，方便了不同文件的使用。此程序返回的是城市的坐标矩阵pop 

和城市的距离矩阵dista。 



3.3初始种群 

3.3初始种群 

33..33初初始始种种群群 



    对于n个城市的问题，每个个体即每个解的长度为n ，用s行, t列的pop矩阵 

表示初始群体，s表示初始群体的个数，t为n+1，矩阵的每一行的前n个元素表示 

城市编码，最后一个元素表示这一路径的长度。这一算法通过start.m程序实现。 



3.3适应度 

3.3适应度 

33..33适适应应度度 



       TSP 

    在  的求解中，可以直接用距离总和作为适应度函数。个体的路径长度越 

                      pop 

小，所得个体优越，以  矩阵的每一行最后一个元素作为个体适应值。求适应 

值的qiujuli.m 程序，见附录。 



3.4选择 

3.4选择 

33..44选选择择 



    选择就是从群体中选择优胜个体、淘汰劣质个体的操作，它是建立在群体中 

个体适应度评估基础上。这里采用方法是最优保存方法。 

    算法就是首先将群体中适应度最大的k个个体直接替换适应度最小的k个个 

体。程序为select.m，见附录。 



3.5交 

3.5交 

33..55交交叉 



    受贪婪算法的启发, 本文设计一种有目的使适应值上升的交叉算子。已知两 

个父代a1(m11,m12,m13,...,m1n),a2(m21,m22,m23,...,m2n)，算法产生后代a1’ 

和a2’的过程如下： 

    (1) 随机产生一个城市d作为交叉起点, 把d作为a1’和a2’的起始点 

    (2) 分别从a1和a2中找出d的右城市dr1和dr2,并计算(d,dr1)和(d,dr2)的 

距离j1和j2。 

    (3) 如果j1<j2,则把dr1作为a1'的第二个点，从a1和a2中删除d，并且把当 

前点改为dr1.转步骤(5)。 


----------------------- Page 5-----------------------

     (4) 如果j1>j2,则把dr2作为a1'的第二个点，从a1和a2中删除d，并且把当 

前点改为dr2。 

     (5) 若此时p1和p2的个数为1，结束，否则回到第二步继续执行。 

     同理，把第二步中的右城市改成左城市dle1和dle2，通过计算(d,d1e1)和 

(d,d1e2) 的距离并比较大小来确定子代a2'。为程序cross.m，见附录。 



3.6变异 

3.6变异 

33..66变变异异 



     变异操作是以变异概率Pm对群体中个体串某些基因位上的基因值作变动，若 

变异后子代的适应度值更加优异，则保留子代染色体，否则，仍保留父代染色体。 

这里采用的方法是倒置变异法。 

     假设当前个体X为（1 3 7 4 8 0 5 9 6 2）。如果Pm>rand，那么随机选择 

来自同一个体的两个点mutatepoint(1)和mutatepoint(2)，比如说3和7，倒置P1 

和P之间的部分，产生下面的子体X'为(1 3 7 5 0 8 4 9 6 2)。为mutate.m程序， 

见附录。 



4. 

4. 

44..试验与结果分析 



     试验采用TSPLib标准库的eil51，eil76，eil101作为测试实例。每个实例分 

别测试五次，求出平均值和最优值作为比较依据。 

   问题        求解次数 最优理论  最优解                        最差解          平均值 

                             解 

  eil51          5          426       432.3981  445.9899  441.2703 

  eil76          5          538       561.5283  576.1645  570.2783 

  eil101         5          629       678.3685  699.7653  693.5415 

     下面给出五次运行中的最优路径图： 



      图1 eil51最优路径图                                图2 eil76最优路径图 


----------------------- Page 6-----------------------

                                图3 eil101最优路径图 



     从图中可以看出，所获得路线都有交叉，明显不是最优路径。对于51个城市 

和76个城市来说，都只有一个交叉，而对于101个城市来说，交叉比较多，求得 

最优路径的结果也不是太理想。 

     从参数设置来说，对于51个城市和76个城市，参数：群体总数s=400，交叉 

概率Pc=0.9，变异概率Pm=0.2，最大迭代次数C=100。对于不断调整试验参数中 

可以得出，最大迭代次数越多，结果比较接近理论最优解。 

     对于101个城市，参数：群体总数s=500，交叉概率Pc=0.9，变异概率Pm=0.1， 

最大迭代次数C=200。对于不断调整试验参数中可以得出，对于较大数目的城市 

数，变异概率小一些，得到结果也会相应好一些。 



5. 

5. 

55..结语 



     本文运用Matlab软件，利用遗传算法解决了小规模的TSP问题。文章首先介 

绍了TSP问题，并给出TSP问题的数学定义，然后介绍了遗传算法的原理以及算法 

的基本过程，最后通过对标准TSPLib中的51、76和101个城市分别进行了测试， 

根据试验对参数进行分析。本文程序解决小规模的TSP问题还可以，随着城市数 

目的增大，计算精度有所下降，计算时间增长很快，效率较低较快，这也是下一 

步需要改进的地方。 



6. 

6. 

66..附录 



%此为主程序代码，将下面各个程序分别保存在同一文件下运行，即可得出比较% 



好的解，只是会有点交叉，但是最小路径值很接近最优理论值 

function ga 


----------------------- Page 7-----------------------

s=500;%群体中个体数目 

k=100;%选择优化个数 

Pc=0.9;%交叉概率 

Pm=0.1;%变异概率 

C=200;%最大循环次数 

[M,dista]=readfile('tsp76.txt');%读取城市坐标文件 

[Ncities,b]=size(M); 

t=Ncities+1; 

farm=start(s,t);        %随机初始化种群 

farm=qiujuli(farm,dista);%求出种群的适应度 

counter=0; 

while counter<=C 

     counter=counter+1; 

     farm=select(farm,k);%选择 

     if(Pc>rand) 

         farm=cross(farm,dista);%交叉 

     end 

     if(Pm>rand) 

         farm=mutate(farm,dista);%变异 

     end 

end 

[a,b]=size(farm); %求出总路径中的最小值 

A=zeros(1,a); 

for i=1:a 

     A(1,i)=farm(i,b); 

end 

shortest_path=min(A)%最短路径值 

[c,d]=find(A==shortest_path); 

e=c(1);%画出最短路径图 

for i=1:Ncities 

     plot(M(i,1),M(i,2),'ro');%‘ro’可改 

     hold on 

end 



for i=1:t-2 

     plot_ga(farm(e,1),farm(e,t-1),M); 

     plot_ga(farm(e,i),farm(e,i+1),M); 

end 



----------------------------------------------------- 

---------------------------------------------------- 

%读取城市坐标的txt文件，格式为n*2的坐标，n为城市数目，%filename为文件 



名，返回n*2的坐标pop，以及城市距离矩阵%city_distance，为n*n 


----------------------- Page 8-----------------------

function [pop,city_distance]=readfile(filename) 

fid=fopen(filename,'r'); 

pop=fscanf(fid,'%d',[2 inf]); 

pop=pop'; 

[a,b]=size(pop); 

city_distance=zeros(a,a); 

for i=1:a 

     for j=i:a 

         city_distance(i,j)=sqrt((pop(i,1)-pop(j,1))^2+(pop(i,2)-pop 



(j,2))^2); 

         city_distance(j,i)=city_distance(i,j); 

     end 

end 

fclose(fid) 



--------------------------------------------------------------------- 

-------------------------------------------------- 

%生成s*t列的种群，其中每一行的前t-1个数为1到t-1的随机不重复排列，用于 

%显示随机行走的路径，最后一列记录这样走的总距离，一般t等于城市数目+1， 

%s为初始设置的群体中个体数目 

function pop=start(s,t) 

pop=zeros(s,t); 

for i=1:s 

pop(i,1:t-1)=randperm(t-1); 

end 



--------------------------------------------------------------------- 

- 



                                编码，生成 个小于 的整数数组 

function [a]=bianma(k,u)  %              k       u 

a=zeros(1,k); 

aa=0:u-1; 

for i=1:k 

    point=round(rand*(u-i))+1; 

    a(i)=aa(point); 

    aa(point)=[]; 

end 



================================================================ 



-------------------------------------------------- 


----------------------- Page 9-----------------------

%该算法主要实现pop矩阵中最后一列的值，即总距离 

function [pop]=qiujuli(pop,D) %D为城市的距离矩阵，pop为种群 

[s,t]=size(pop); 

for i=1:s 

     dd=0; 

     for j=1:t-2 

         dd=D(pop(i,j),pop(i,j+1))+dd; 

     end 

     dd=dd+D(pop(i,1),pop(i,t-1));                    %dd为每个访遍城市路径 

的 



适应度 

     pop(i,t)=dd;                                    %存储适应度 

end 



--------------------------------------------------------------------- 

- 



-------------------------------------------------- 

%该算法是将群体中适应度最大的k个个体直接替换适应度最小的k个%个体 

function [pop]=select(pop,k) 

[s,t]=size(pop); 

m11=(pop(:,t)); 

m11=m11'; 

mmax=zeros(1,k); 

mmin=zeros(1,k); 

num=1; 

while num<k+1; 

[a,mmax(num)]=max(m11); 

m11(mmax(num))=0; 

num=num+1; 

end 

num=1; 

while num<k+1; 

[b,mmin(num)]=min(m11); 

m11(mmin(num))=a; 

num=num+1; 

end 

for i=1:k 

pop(mmax(i),:)=pop(mmin(i),:); 

end 


----------------------- Page 10-----------------------

--------------------------------------------------------------------- 

- 



-------------------------------------------------- 

%交叉算法，主要思想是：每两行进行交叉的操作，使每行的适应度%减少 

function [pop]=cross(pop,D) 

[s,t]=size(pop); 

pop1=pop;%保存原群体矩阵 

m=zeros(1,t);%初始化交叉后第一个个体 

n=zeros(1,t);%初始化交叉后第二个个体 

for i=1:2:s %每两行进行交叉操作 

     x1=pop(i,:); 

     y1=pop(i+1,:); 

     x2=pop(i,:); 

     y2=pop(i+1,:); 

     c1=round(rand*(t-2))+1; %生成1到t-1之间的随机整数 

     c2=c1; 

     m(1)=c1; 

     n(1)=c2; 

     j=2; 

     while size(x1,2)>2           %判断是否继续 

         l=find(x1==c1); 

         h=find(x2==c2); 

         if l==t+1-j 

              lr=1; 

         else 

              lr=l+1; 

         end 

         if h==1 

              hle=t+1-j; 

         else 

              hle=h-1; 

         end 

         q=find(y1==c1); 

         z=find(y2==c2); 

         if q==t+1-j 

              qr=1; 

         else qr=q+1; 

         end 

         if z==1 

              zle=t+1-j; 

         else zle=z-1; 

         end 

         if D(c1,x1(lr))<D(c1,y1(qr)) %根据比较两点间距离进行交换 


----------------------- Page 11-----------------------

              m(j)=x1(lr); 

              c1=x1(lr); 

         else 

              m(j)=y1(qr);c1=y1(qr); 

         end 

         x1(l)=[];                        %删除父节点 

         y1(q)=[];                        %删除父节点 

         if D(c2,x2(hle))<D(c2,y2(zle))%根据比较两点间距离进行交换 

              n(j)=x2(hle); 

              c2=x2(hle); 

         else 

              n(j)=y2(zle);c2=y2(zle); 

         end 

         x2(h)=[];%删除父节点 

         y2(z)=[];%删除父节点 

         j=j+1; 

     end 

     pop1(i,:)=m; 

     pop1(i+1,:)=n; 

end 

pop1=qiujuli(pop1,D);%求出交叉后的路径矩阵 

for i=1:s               %选择适应度变小的交叉，进行更新 

     if pop1(i,t)<pop(i,t) 

         pop(i,:)=pop1(i,:); 

     end 

end 



--------------------------------------------------------------------- 

- 



--------------------------------------------------------------------- 

- 

%变异，D为城市的距离矩阵，进行变异 

function [pop]=mutate(pop,D) 

[s,t]=size(pop); 

pop1=pop; 

for i=1:s 

mutatepoint=bianma(2); 

b=round((mutatepoint(2)-mutatepoint(1))/2-0.5); 

for j=1:b 

zhong=pop1(i,mutatepoint(1)+j); 

pop1(i,mutatepoint(1)+j)=pop1(i,mutatepoint(2)-j); 

pop1(i,mutatepoint(2)-j)=zhong; 

end 


----------------------- Page 12-----------------------

end 

pop1=qiujuli(pop,D); 

for i=1:s 

if pop1(i,t)<pop(i,t) 

pop(i,:)=pop1(i,:) 

end 

end 



--------------------------------------------------------------------- 

- 



--------------------------------------------------------------------- 

- 

%画图 

function plot_ga(a,b,V) 

P=[V(a,1) V(a,2)]; 

Q=[V(b,1) V(b,2)]; 

c=P(1,2); 

P(1,2)=Q(1,1); 

Q(1,1)=c; 

plot(P,Q,'g-')               %g表示颜色，-表示连线的形状，可改。 

hold on 
````

</details>

#### DrawPath · MATLAB · 133f52f7

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `DrawPath`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`096cd91f41dd4c715eb5ec09142bed6c6719939415fa918ca99ebf20f07221c2`
- 语言：MATLAB
- 符号：`DrawPath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/DrawPath.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/DrawPath.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/dsxy2figxy.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/dsxy2figxy.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 画路径函数
%输入
% Chrom  待画路径   
% X      各城市坐标位置
function DrawPath(Chrom,X)
R=[Chrom(1,:) Chrom(1,1)]; %一个随机解(个体)
figure;
hold on
plot(X(:,1),X(:,2),'o','color',[0.5,0.5,0.5])
plot(X(Chrom(1,1),1),X(Chrom(1,1),2),'rv','MarkerSize',20)
for i=1:size(X,1)
    text(X(i,1)+0.05,X(i,2)+0.05,num2str(i),'color',[1,0,0]);
end
A=X(R,:);
row=size(A,1);
for i=2:row
    [arrowx,arrowy] = dsxy2figxy(gca,A(i-1:i,1),A(i-1:i,2));%坐标转换
    annotation('textarrow',arrowx,arrowy,'HeadWidth',8,'color',[0,0,1]);
end
hold off
xlabel('横坐标')
ylabel('纵坐标')
title('轨迹图')
box on
````

</details>

#### GA_TSP · MATLAB · 30d7b519

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`ab7ba8ce6bcae254c590ef95b35672182b1fd7a44ac20d41fb5d2602c38ce4cb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/GA_TSP.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/DrawPath.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/PathLength.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/Reins.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/Reverse.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/crossover.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/draw.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/mutation.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/select.m`

<details>
<summary>展开原始代码</summary>

````matlab
%----------------------- 遗传算法解决TSP问题 -----------------------
%.........<主程序.Main>.........
%******************参数及参数说明******************
%-------nCity：城市数量，参数取值范围，>2 整数；
%-------xyCity：城市二维坐标，本例由计算机随机产生，范围(0,1)，假定起始城市为第nCity个城市；
%-------dCity：城市间距离矩阵，本例考虑城市间往返距离相等，且定义距离为欧几里德范数；
%-------nPopulation：种群个体数量；
%-------Population：种群，nPopulation*(nCity-1)矩阵，每行由{1,2,...,nCity-1}某一个全排列构成；
%-------generation：算法终止条件一，迭代代数；
%-------nR：算法终止条件二，最短路径值连续nR代不变；
%-------R：最短路径；
%-------Rlength：最短路径长度。
%-------Shock：当最优个体保持一段时期不变后，产生震荡
function [R,Rlength]=GA_TSP(xyCity,dCity,Population,nPopulation,pCrossover,percent,pMutation,generation,nR,rr,rangeCity,rR,moffspring,record,pi,Shock,maxShock)
%10个城市坐标
%xyCity=[0.4 0.4439;0.2439 0.1463;0.1707 0.2293;0.2293 0.761;0.5171 0.9414;
 %  0.8732 0.6536;0.6878 0.5219;0.8488 0.3609;0.6683 0.2536;0.6195 0.2634];
%10 cities d'=2.691
%--------------------------------------------------------------------------
%30个城市坐标
xyCity=[25 62;7 64;2 99;68 58;71 44];
xyCity=[41 94;37 84;54 67;25 62;7 64;2 99;68 58;71 44;54 62;83 69;64 60;18 54;22 60;
    83 46;91 38;25 38;24 42;58 69;71 71;74 78;87 76;18 40;13 40;82 7;62 32;58 35;45 21;41 26;44 35;4 50];
%30 cities d'=423.741 by D B Fogel
%--------------------------------------------------------------------------
%50个城市坐标
%xyCity=[31 32;32 39;40 30;37 69;27 68;37 52;38 46;31 62;30 48;21 47;25 55;16 57;
%17 63;42 41;17 33;25 32;5 64;8 52;12 42;7 38;5 25; 10 77;45 35;42 57;32 22;
%27 23;56 37;52 41;49 49;58 48;57 58;39 10;46 10;59 15;51 21;48 28;52 33;
%58 27;61 33;62 63;20 26;5 6;13 13;21 10;30 15;36 16;62 42;63 69;52 64;43 67];
%50 cities d'=427.855 by D B Fogel
%--------------------------------------------------------------------------
%75个城市坐标
%xyCity=[48 21;52 26;55 50;50 50;41 46;51 42;55 45;38 33;33 34;45 35;40 37;50 30;
%55 34;54 38;26 13;15 5;21 48;29 39;33 44;15 19;16 19;12 17;50 40;22 53;21 36;
%20 30;26 29;40 20;36 26;62 48;67 41;62 35;65 27;62 24;55 20;35 51;30 50;
%45 42;21 45;36 6;6 25;11 28;26 59;30 60;22 22;27 24;30 20;35 16;54 10;50 15;
%44 13;35 60;40 60;40 66;31 76;47 66;50 70;57 72;55 65;2 38;7 43;9 56;15 56;
%10 70;17 64;55 57;62 57;70 64;64 4;59 5;50 4;60 15;66 14;66 8;43 26];
%75cities d'=549.18 by D B Fogel
figure(1)
axis([0 10 0 10])                        
grid on
scatter(xyCity(:,1),xyCity(:,2),'x')
grid on
nCity=size(xyCity,1);
for i=1:nCity                                   %计算城市间距离，假设距离为欧几里德范数
    for j=1:nCity
        dCity(i,j)=((xyCity(i,1)-xyCity(j,1))^2+(xyCity(i,2)-xyCity(j,2))^2)^0.5;
    end
end                                             %计算城市间距离，假设距离为欧几里德范数
xyCity;                                        %显示城市坐标
dCity ;                                         %显示城市距离矩阵
%初始种群
nPopulation=50;%种群个体数量                      
for i=1:nPopulation
    Population(i,:)=randperm(nCity-1);          %产生随机个体
end
%Population                                     %显示初始种群
%添加绘图表示
pCrossover=0.85;
percent=0.6;
pMutation=0.01;
nRemain=40;
pi(1)=0.7;   %选择操作最优个体被保护概率
pi(2)=0.7;  %交叉操作最优个体被保护概率
pi(3)=0.6;  %突变操作最优个体被保护概率
maxShock=0.05;  %最大突变概率
Shock=0;
rr=0;
Rlength=0;
counter1=0;
counter2=0;
R=zeros(1,nCity-1);
 %% 选择
[newPopulation,R,Rlength,counter2,rr]=select(Population,nPopulation,nCity,dCity,Rlength,R,counter2,pi,nRemain);
R0=R; 
R0=R;
record(1,:)=R;
rR(1)=Rlength;
Rlength0=Rlength;
figure(2)
subplot(1,3,1)
draw(xyCity,R,nCity)
generation=1000;%最多迭代次数
nR=50;%最短路径连续保持不变代数
while counter1<generation&counter2<nR
    if counter2<nR*1/5
        Shock=0;
    elseif counter2<nR*2/5
        Shock=maxShock*1/4-pMutation;
    elseif counter2<nR*3/5
        Shock=maxShock*2/4-pMutation;
    elseif counter2<nR*4/5
        Shock=maxShock*3/4-pMutation;
    else
        Shock=maxShock-pMutation;
    end
   counter1;
   length=pathlength(dCity,newPopulation);
   %fprintf('%d   %1.10f\n',i,min(length));
   %line([i-1,i],[prelength,min(length)]);pause(0.0001);
%% 交叉操作
   offspring=crossover(newPopulation,nCity,pCrossover,percent,nPopulation,rr,pi,nRemain);  
    %% 变异
 moffspring=mutation(offspring,nCity,pMutation,nPopulation,rr,pi,nRemain,Shock); 
    %% 逆转操作
 niffspring=Reverse(moffspring,dCity);
     %%重新插入
Population=Reins(Population,niffspring,length);
R0=R;
    %% 更新迭代次数
    counter1=counter1+1;
    rR(counter1+1)=Rlength;
    record(counter1+1,:)=R;
end
%R0
%Rlength0
%R
%Rlength
minR=min(rR)
disp('最短路经出现代数:')
rr=find(rR==minR)
disp('最短路径:');
record(rr,:)
mR=record(rr(1,1),:)
disp('终止条件一:')
counter1
disp('终止条件二:')
counter2
disp('最短路径长度:')
minR
disp('最初路径长度:');
rR(1)
subplot(1,3,2)
draw(xyCity,R,nCity);
subplot(1,3,3)
draw(xyCity,mR,nCity);
figure(3)
i=1:counter1+1;
plot(i,rR(i));
grid on
figure();
drawpath(Population(1,:),xyCity);
title('最初路径安排');
````

</details>

#### OutputPath · MATLAB · abc4c560

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `OutputPath`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a29e2635babeb1672684c95178cc74dd8757830f3bda17e5a34a62c510258ba0`
- 语言：MATLAB
- 符号：`OutputPath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/OutputPath.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/OutputPath.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 输出路径函数
%输入：R 路径
function p=OutputPath(R)
R=[R,R(1)];
N=length(R);
p=num2str(R(1));
for i=2:N
    p=[p,'—>',num2str(R(i))];
end
disp(p)
````

</details>

#### PathLength · MATLAB · 26469b48

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `PathLength`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9c626ed9eba0f15634d69a9b2b2a18d1997fe636475c17e19d28e0bdb083b9f4`
- 语言：MATLAB
- 符号：`PathLength`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/PathLength.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/PathLength.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 计算各个体的路径长度
% 输入：
% D     两两城市之间的距离
% Chrom 个体的轨迹
function len=PathLength(D,Chrom)
[row,col]=size(D);
NIND=size(Chrom,1);
len=zeros(NIND,1);
for i=1:NIND
    p=[Chrom(i,:) Chrom(i,1)];
    i1=p(1:end-1);
    i2=p(2:end);
    len(i,1)=sum(D((i1-1)*col+i2));
end
````

</details>

#### Reins · MATLAB · 84af9ea2

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Reins`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9cd03324e1e2bbb617422427bfd1e392c99ea9e6fe25d4d960e589f14f37c257`
- 语言：MATLAB
- 符号：`Reins`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/Reins.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Reins.m`

<details>
<summary>展开原始代码</summary>

````matlab
 %% 重插入子代的新种群
 %输入：
 %Chrom  父代的种群
 %SelCh  子代种群
 %ObjV   父代适应度
 %输出
 % Chrom  组合父代与子代后得到的新种群
function Chrom=Reins(Chrom,SelCh,ObjV)
NIND=size(Chrom,1);
NSel=size(SelCh,1);
[TobjV,index]=sort(ObjV);
Chrom=[Chrom(index(1:NIND-NSel),:);SelCh];
````

</details>

#### Reverse · MATLAB · ba62165c

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Reverse`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`362230ebfeb1275e54333fad3d1cfd1e7c2f6ac7eebef563121f8ac8af481c1e`
- 语言：MATLAB
- 符号：`Reverse`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/Reverse.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Reverse.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/PathLength.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/PathLength.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 进化逆转函数
%输入
%SelCh 被选择的个体
%D     个城市的距离矩阵
%输出
%SelCh  进化逆转后的个体
function SelCh=Reverse(SelCh,D)
[row,col]=size(SelCh);
ObjV=PathLength(D,SelCh);  %计算路径长度
SelCh1=SelCh;
for i=1:row
    r1=randsrc(1,1,[1:col]);
    r2=randsrc(1,1,[1:col]);
    mininverse=min([r1 r2]);
    maxinverse=max([r1 r2]);
    SelCh1(i,mininverse:maxinverse)=SelCh1(i,maxinverse:-1:mininverse);
end
ObjV1=PathLength(D,SelCh1);  %计算路径长度
index=ObjV1<ObjV;
SelCh(index,:)=SelCh1(index,:);
````

</details>

#### crossover · MATLAB · ef1e94e7

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `crossover`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5ce5e4d183194c51934593fdd6cac4c986aad02361ead0dadb122832f43270f9`
- 语言：MATLAB
- 符号：`crossover`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/crossover.m`

<details>
<summary>展开原始代码</summary>

````matlab
%........提供者/daichenglei/...........
%.........本函数为交叉算子操作crossover operator.........
%顺序交叉(OX)算子说明：
%步骤：
%--1.从第一双亲中随机选一个子串；
%--2.将子串复制到一个空字串的相应位置，产生一个原始后代；
%--3.删去第二双亲中子串已有的城市，得到原始后代需要的其他城市的顺序；
%--4.按照这个城市顺序，从左到右将这些城市定位到后代的空缺位置上。
%******************参数及参数说明******************
%-------offspring：子代种群
%-------pCrossover：交叉概率
%-------wCrossover：交叉宽度
%-------pointCrossover：交叉点
%-------percent：交叉比例
function offspring=crossover(newPopulation,nCity,pCrossover,percent,nPopulation,rr,pi,nRemain)
offspring=zeros(nPopulation,nCity-1);          %初始化后代
ccc=0;
for i=1:nPopulation
    s=find(rr==i);
    if size(s,1)~=0&rand<pi(2)&ccc<nRemain
        offspring(i,:)=newPopulation(i,:);
        ccc=ccc+1;
    elseif rand<pCrossover                     %改进方向：优势个体保留，劣势个体不参与交叉
        j=unidrnd(nPopulation);            %选择另一参与交叉的个体
        while i==j
            j=unidrnd(nPopulation);            %unidrnd(n)产生{1,2,...,n}里的随机数
        end
        wCrossover=floor((nCity-1)*percent);        %确定交叉宽度
        backPopulation=newPopulation(i,:);         
        pointCrossover=unidrnd(nCity-1-wCrossover); %随机产生交叉点，做差确保不溢出
        for m=1:wCrossover                          %OX交叉
            offspring(i,pointCrossover+m-1)=newPopulation(j,pointCrossover+m-1);      %步骤1~2
        end
        for n=1:nCity-1
            for m=1:wCrossover
                if backPopulation(n)==newPopulation(j,pointCrossover+m-1)
                    backPopulation(n)=0;
                end
            end
        end
        for n=1:nCity-1
            if backPopulation(n)~=0
                for o=1:nCity-1
                    if offspring(i,o)==0
                        offspring(i,o)=backPopulation(n);
                        break
                    end
                end
            end
        end
    else offspring(i,:)=newPopulation(i,:);
    end
end
%offspring             %显示交叉后子代
````

</details>

#### draw · MATLAB · d94e1047

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `draw`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2d4c4809dd15aebec74a632881c4a124c880ae40b5f6617436c97f5dd066bdb7`
- 语言：MATLAB
- 符号：`draw`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/draw.m`

<details>
<summary>展开原始代码</summary>

````matlab
%.......提供者/daichenglei/........
%.........绘图.picture...........
function draw(xyCity,R,nCity)
scatter(xyCity(:,1),xyCity(:,2),'x')
title('随机城市图位置');
hold on
plot([xyCity(R(1),1),xyCity(nCity,1)],[xyCity(R(1),2),xyCity(nCity,2)])
plot([xyCity(R(nCity-1),1),xyCity(nCity,1)],[xyCity(R(nCity-1),2),xyCity(nCity,2)])
hold on
for i=1:length(R)-1
    x0=xyCity(R(i),1);
    y0=xyCity(R(i),2);
    x1=xyCity(R(i+1),1);
    y1=xyCity(R(i+1),2);
    xx=[x0,x1];
    yy=[y0,y1];
    plot(xx,yy)
    title('最佳路径');
    hold on
end
````

</details>

#### dsxy2figxy · MATLAB · c456204a

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：执行归一化或标准化以统一变量尺度。
- **调用方式**：优先调用 `dsxy2figxy`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e93a50af10a503a456294791f45cdba5c9fd3284f2211ca36b010ae1f7a0c5c7`
- 语言：MATLAB
- 符号：`dsxy2figxy`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/dsxy2figxy.m`
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/dsxy2figxy.m`

<details>
<summary>展开原始代码</summary>

````matlab
function varargout = dsxy2figxy(varargin)
if length(varargin{1}) == 1 && ishandle(varargin{1}) ...
                            && strcmp(get(varargin{1},'type'),'axes')   
    hAx = varargin{1};
    varargin = varargin(2:end);
else
    hAx = gca;
end;
if length(varargin) == 1
    pos = varargin{1};
else
    [x,y] = deal(varargin{:});
end
axun = get(hAx,'Units');
set(hAx,'Units','normalized'); 
axpos = get(hAx,'Position');
axlim = axis(hAx);
axwidth = diff(axlim(1:2));
axheight = diff(axlim(3:4));
if exist('x','var')
    varargout{1} = (x - axlim(1)) * axpos(3) / axwidth + axpos(1);
    varargout{2} = (y - axlim(3)) * axpos(4) / axheight + axpos(2);
else
    pos(1) = (pos(1) - axlim(1)) / axwidth * axpos(3) + axpos(1);
    pos(2) = (pos(2) - axlim(3)) / axheight * axpos(4) + axpos(2);
    pos(3) = pos(3) * axpos(3) / axwidth;
    pos(4) = pos(4) * axpos(4 )/ axheight;
    varargout{1} = pos;
end
set(hAx,'Units',axun)
````

</details>

#### mutation · MATLAB · 256093f4

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `mutation`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5868a0c9d3b7e364a85d8a8fa83cf8370f1a5298602b7cbdb582bc368071629c`
- 语言：MATLAB
- 符号：`mutation`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/mutation.m`

<details>
<summary>展开原始代码</summary>

````matlab
%.........提供者/daichenglei/.............
%.........本函数为突变操作mutation operator.........
%操作目的为两点互换变异
%******************参数及参数说明******************
%-------pMutation：突变概率
function moffspring=mutation(offspring,nCity,pMutation,nPopulation,rr,pi,nRemain,Shock)
exchange=0;
ccc=0;
for m=1:nPopulation
    moffspring(m,:)=offspring(m,:);
    k=find(rr==m);
    if size(k,1)~=0&rand<pi(3)&ccc<nRemain
        m=rr(k(1,1),1);
        moffspring(m,:)=moffspring(m,:);
        ccc=ccc+1;
    else
        for i=1:nCity-1
            if rand<pMutation+Shock
                j=unidrnd(nCity-1);
                while i==j
                    j=unidrnd(nCity-1);
                end
                exchange=moffspring(m,i);
                moffspring(m,i)=moffspring(m,j);
                moffspring(m,j)=exchange;
            end
        end
    end
end
%offspring         %显示突变后子代
````

</details>

#### select · MATLAB · af158726

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e251f368524063c9eb83453549128fd6aeabef28b18d2ca61b9216765692f5a0`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/自创遗传算法解TSP操作/select.m`

<details>
<summary>展开原始代码</summary>

````matlab
%........提供者/daichenglei/........
%.........本函数为选择操作.select operator.........
%******************参数及参数说明******************
%-------newPopulation：选择后的新种群
%-------Distance：用来存储及计算个体路径长度
%-------Sum：总路径长度
%-------Fitness：每个个体的适应概率
%-------sFitness：累积概率
%-------a：甩随机数
function [newPopulation,R,Rlength,counter2,rr]=select(Population,nPopulation,nCity,dCity,Rlength,R,counter2,pi,nRemain)
Distance=zeros(nPopulation,1);                  %零化路径长度
Fitness=zeros(nPopulation,1);                   %零化适应概率
Sum=0;                                          %路径长度
for i=1:nPopulation                             %计算个体路径长度
    for j=1:nCity-2
        Distance(i)=Distance(i)+dCity(Population(i,j),Population(i,j+1)); 
    end                                         %对路径长度调整，增加起始点到路径首尾点的距离
    Distance(i)=Distance(i)+dCity(Population(i,1),nCity)+dCity(Population(i,nCity-1),nCity);
    Sum=Sum+Distance(i);                        %累计总路径长度
end                                             %计算个体路径长度
if Rlength==min(Distance)
    counter2=counter2+1;
else
    counter2=0;
end
Rlength=min(Distance);                          %更新最短路径长度
rr=find(Distance==Rlength);
R=Population(rr(1,1),:);                        %更新最短路径
for i=1:nPopulation
   Fitness(i)=(max(Distance)-Distance(i)+0.001)/(nPopulation*(max(Distance)+0.001)-Sum);     %适应概率=个体/总和...已作调整，大小作了调换
end
%Fitness            %显示适应概率
sFitness=zeros(nPopulation,1);                  %累积概率
sFitness(1)=Fitness(1);
for i=2:nPopulation
    sFitness(i)=sFitness(i-1)+Fitness(i);
end
%sFitness           %显示累积概率
newPopulation=zeros(nPopulation,nCity-1);       %零化新种群
for i=1:nPopulation                             %甩随机数
    a=rand;
    %a              %显示甩出的随机数
    for j=1:nPopulation
        if a<sFitness(j)
            newPopulation(i,:)=Population(j,:);
            break
        end
    end
end
for i=1:size(rr,1)
    if rand<pi(1)&i<=nRemain
        newPopulation(rr(i,1),:)=Population(rr(i,1),:);
    end
end
%newPopulation      %显示被选中的新种群个体
````

</details>

#### Distanse · MATLAB · ad7627bb

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Distanse`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7dba248dc9470b860e35949a942bb1835838f9847d759ca0d57a902dbb19f37d`
- 语言：MATLAB
- 符号：`Distanse`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Distanse.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 计算两两城市之间的距离
%输入 a  各城市的位置坐标
%输出 D  两两城市之间的距离
function D=Distanse(a)
row=size(a,1);
D=zeros(row,row);
for i=1:row
    for j=i+1:row
        D(i,j)=((a(i,1)-a(j,1))^2+(a(i,2)-a(j,2))^2)^0.5;
        D(j,i)=D(i,j);
    end
end
````

</details>

#### Fitness · MATLAB · 4045ead7

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Fitness`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3cbd801e866ead09dd8e38623ac21035e21b4577792cc4ec9d0a230c9fc8513d`
- 语言：MATLAB
- 符号：`Fitness`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Fitness.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 适配值函数     
%输入：
%个体的长度（TSP的距离）
%输出：
%个体的适应度值
function FitnV=Fitness(len)
FitnV=1./len;
````

</details>

#### GA_TSP · MATLAB · af7dc084

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`36c02067f355eef27d71f260b18044e488dc1a8229b38de3d277195acefbeca0`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/GA_TSP.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Distanse.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/DrawPath.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Fitness.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/InitPop.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Mutate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/OutputPath.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/PathLength.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Recombin.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Reins.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Reverse.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Select.m`

<details>
<summary>展开原始代码</summary>

````matlab
%遗传算法求解TSP问题(为选择操作从新设计后程序)
%输入：
%D       距离矩阵
%NIND    为种群个数
%X       参数是中国34个城市的坐标(初始给定)
%MAXGEN  为停止代数，遗传到第MAXGEN代时程序停止,MAXGEN的具体取值视问题的规模和耗费的时间而定
%m       为适值淘汰加速指数,最好取为1,2,3,4,不宜太大
%Pc      交叉概率
%Pm      变异概率
%输出：
%R       为最短路径
%Rlength 为路径长度
clear
clc
close all
%% 加载数据 %%遗传参数
load CityPosition1;%个城市坐标位置
NIND=100;       %种群大小
MAXGEN=200;
Pc=0.9;         %交叉概率
Pm=0.05;        %变异概率
GGAP=0.9;      %代沟(Generation gap)
D=Distanse(X);  %生成距离矩阵
N=size(D,1);    %(34*34)
%% 初始化种群
Chrom=InitPop(NIND,N);
%% 在二维图上画出所有坐标点
% figure
% plot(X(:,1),X(:,2),'o');
%% 画出随机解的路线图
DrawPath(Chrom(1,:),X)
pause(0.0001)
%% 输出随机解的路线和总距离
disp('初始种群中的一个随机值:')
OutputPath(Chrom(1,:));
Rlength=PathLength(D,Chrom(1,:));
disp(['总距离：',num2str(Rlength)]);
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
%% 优化
gen=0;
figure;
hold on;box on
xlim([0,MAXGEN])
title('优化过程')
xlabel('代数')
ylabel('最优值')
ObjV=PathLength(D,Chrom);  %计算路线长度
preObjV=min(ObjV);
while gen<MAXGEN
    %% 计算适应度
    ObjV=PathLength(D,Chrom);  %计算路线长度
    % fprintf('%d   %1.10f\n',gen,min(ObjV))
    line([gen-1,gen],[preObjV,min(ObjV)]);pause(0.0001)
    preObjV=min(ObjV);
    FitnV=Fitness(ObjV);
    %% 选择
    SelCh=Select(Chrom,FitnV,GGAP);
    %% 交叉操作
    SelCh=Recombin(SelCh,Pc);
    %% 变异
    SelCh=Mutate(SelCh,Pm);
    %% 逆转操作
    SelCh=Reverse(SelCh,D);
    %% 重插入子代的新种群
    Chrom=Reins(Chrom,SelCh,ObjV);
    %% 更新迭代次数
    gen=gen+1 ;
end
%% 画出最优解的路线图
ObjV=PathLength(D,Chrom);  %计算路线长度
[minObjV,minInd]=min(ObjV);
DrawPath(Chrom(minInd(1),:),X)
%% 输出最优解的路线和总距离
disp('最优解:')
p=OutputPath(Chrom(minInd(1),:));
disp(['总距离：',num2str(ObjV(minInd(1)))]);
disp('-------------------------------------------------------------')
````

</details>

#### InitPop · MATLAB · 795039d3

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `InitPop`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7e0ec3b6fdad841fbbf8afe515f208681a97e86861403e687e08a76026153ebf`
- 语言：MATLAB
- 符号：`InitPop`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/InitPop.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 初始化种群
%输入：
% NIND：种群大小
% N：   个体染色体长度（这里为城市的个数）  
%输出：
%初始种群
function Chrom=InitPop(NIND,N)
Chrom=zeros(NIND,N);%用于存储种群
for i=1:NIND
    Chrom(i,:)=randperm(N);%随机生成初始种群
end
````

</details>

#### Mutate · MATLAB · 860e8288

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Mutate`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f4d98e0965cb14324c7bc368b0b470ee97af968d374ea4798fbb51df5a4f16ae`
- 语言：MATLAB
- 符号：`Mutate`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Mutate.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 变异操作
%输入：
%SelCh  被选择的个体
%Pm     变异概率
%输出：
% SelCh 变异后的个体
function SelCh=Mutate(SelCh,Pm)
[NSel,L]=size(SelCh);
for i=1:NSel
    if Pm>=rand
        R=randperm(L);
        SelCh(i,R(1:2))=SelCh(i,R(2:-1:1));
    end
end
````

</details>

#### Recombin · MATLAB · dbee42b6

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Recombin`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a70ce4be06389dcd49648ff2cbf599b815218dd1ae7c92cc6ef7ec6e02475be4`
- 语言：MATLAB
- 符号：`Recombin`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Recombin.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 交叉操作
% 输入
%SelCh  被选择的个体
%Pc     交叉概率
%输出：
% SelCh 交叉后的个体
function SelCh=Recombin(SelCh,Pc)
NSel=size(SelCh,1);
for i=1:2:NSel-mod(NSel,2)
    if Pc>=rand %交叉概率Pc
        [SelCh(i,:),SelCh(i+1,:)]=intercross(SelCh(i,:),SelCh(i+1,:));
    end
end

%输入：
%a和b为两个待交叉的个体
%输出：
%a和b为交叉后得到的两个个体

function [a,b]=intercross(a,b)
L=length(a);
r1=randsrc(1,1,[1:L]);
r2=randsrc(1,1,[1:L]);
if r1~=r2
    a0=a;b0=b;
    s=min([r1,r2]);
    e=max([r1,r2]);
    for i=s:e
        a1=a;b1=b;
        a(i)=b0(i);
        b(i)=a0(i);
        x=find(a==a(i));
        y=find(b==b(i));
        i1=x(x~=i);
        i2=y(y~=i);
        if ~isempty(i1)
            a(i1)=a1(i);
        end
        if ~isempty(i2)
            b(i2)=b1(i);
        end
    end
end



%
% %交叉算法采用部分匹配交叉%交叉算法采用部分匹配交叉
% function [a,b]=intercross(a,b)
% L=length(a);
% r1=ceil(rand*L);
% r2=ceil(rand*L);
% r1=4;r2=7;
% if r1~=r2
%     s=min([r1,r2]);
%     e=max([r1,r2]);
%     a1=a;b1=b;
%     a(s:e)=b1(s:e);
%     b(s:e)=a1(s:e);
%     for i=[setdiff(1:L,s:e)]
%         [tf, loc] = ismember(a(i),a(s:e));
%         if tf
%             a(i)=a1(loc+s-1);
%         end
%         [tf, loc]=ismember(b(i),b(s:e));
%         if tf
%             b(i)=b1(loc+s-1);
%         end
%     end
% end
````

</details>

#### Select · MATLAB · 73533989

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Select`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`52bdba55f65890e2b37cf7fbc73e1fa3fcf193ed28d30140aea14f47ba19ef28`
- 语言：MATLAB
- 符号：`Select`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Select.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Sus.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 选择操作
%输入
%Chrom 种群
%FitnV 适应度值
%GGAP：代沟
%输出
%SelCh  被选择的个体
function SelCh=Select(Chrom,FitnV,GGAP)
NIND=size(Chrom,1);
NSel=max(floor(NIND*GGAP+.5),2);
ChrIx=Sus(FitnV,NSel);
SelCh=Chrom(ChrIx,:);
````

</details>

#### Sus · MATLAB · 93d2b654

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `Sus`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`74809141812a4b2625b6b8a60cb874427a81a24cf85e14dce6d897ec1245b35f`
- 语言：MATLAB
- 符号：`Sus`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/Sus.m`

<details>
<summary>展开原始代码</summary>

````matlab
% 输入:
%FitnV  个体的适应度值
%Nsel   被选择个体的数目
% 输出:
%NewChrIx  被选择个体的索引号
function NewChrIx = Sus(FitnV,Nsel)
[Nind,ans] = size(FitnV);
cumfit = cumsum(FitnV);
trials = cumfit(Nind) / Nsel * (rand + (0:Nsel-1)');
Mf = cumfit(:, ones(1, Nsel));
Mt = trials(:, ones(1, Nind))';
[NewChrIx, ans] = find(Mt < Mf & [ zeros(1, Nsel); Mf(1:Nind-1, :) ] <= Mt);
[ans, shuf] = sort(rand(Nsel, 1));
NewChrIx = NewChrIx(shuf);
````

</details>

#### test · MATLAB · 5549c602

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5053ca018c498e3f4ef4247fe1dd64ab5a705a949dff1711e23fe9fba52f6be4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/TSP问题求解/遗传算法求解TSP标准程序/test.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear;
clc
for i=1:100
    i
    [L(i),P{i}]=GA_TSP;
end
[a,index]=min(L);
disp('最优解:')
disp(P{index})
disp(['总距离：',num2str(a)]);
A=P{index};
B=L(index);
save P A B
````

</details>

#### Cross · MATLAB · 2a24261d

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `Cross`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`32f8151959858c90f6e39cba55d7bd67b466c79d75226a6dc50fc6c47d215113`
- 语言：MATLAB
- 符号：`Cross`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/Cross.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/test.m`

<details>
<summary>展开原始代码</summary>

````matlab
function ret=Cross(pcross,chrom,sizepop,length)
% 交叉操作
% pcorss                input  : 交叉概率
% chrom                 input  : 抗体群
% sizepop               input  : 种群规模
% length                input  : 抗体长度
% ret                   output : 交叉得到的抗体群

% 每一轮for循环中，可能会进行一次交叉操作，随机选择染色体是和交叉位置，是否进行交叉操作则由交叉概率（continue）控制
for i=1:sizepop  
    
    % 随机选择两个染色体进行交叉
    pick=rand;
    while prod(pick)==0
        pick=rand(1);
    end
    
    if pick>pcross
        continue;
    end
    
    % 找出交叉个体
    index(1)=unidrnd(sizepop);
    index(2)=unidrnd(sizepop);
    while index(2)==index(1)
        index(2)=unidrnd(sizepop);
    end
    
    % 选择交叉位置
    pos=ceil(length*rand);
    while pos==1
        pos=ceil(length*rand);
    end

    % 个体交叉
    chrom1=chrom(index(1),:);
    chrom2=chrom(index(2),:);
    
    k=chrom1(pos:length);
    chrom1(pos:length)=chrom2(pos:length);
    chrom2(pos:length)=k; 
    
    % 满足约束条件赋予新种群
    flag1=test(chrom(index(1),:));
    flag2=test(chrom(index(2),:));
    
    if flag1*flag2==1
        chrom(index(1),:)=chrom1;
        chrom(index(2),:)=chrom2;
    end
    
end

ret=chrom;
end
````

</details>

#### Mutation · MATLAB · ed3b8c71

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `Mutation`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`2dd1414d6c360924f7d6efa1df977f83be94524f91efce86364e693f7bc8cdf9`
- 语言：MATLAB
- 符号：`Mutation`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/Mutation.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/test.m`

<details>
<summary>展开原始代码</summary>

````matlab
function ret=Mutation(pmutation,chrom,sizepop,length1)
% 变异操作
% pmutation        input  : 变异概率
% chrom            input  : 抗体群
% sizepop          input  : 种群规模
% iii              input  : 进化代数
% MAXGEN           input  : 最大进化代数
% length1          input  : 抗体长度
% ret              output : 变异得到的抗体群
% 每一轮for循环中，可能会进行一次变异操作，染色体是随机选择的，变异位置也是随机选择的
for i=1:sizepop   
    
    % 变异概率
    pick=rand;
    while pick==0
        pick=rand;
    end
    index=unidrnd(sizepop);

   % 判断是否变异
    if pick>pmutation
        continue;
    end
    
    pos=unidrnd(length1);
    while pos==1
        pos=unidrnd(length1);
    end
    
    nchrom=chrom(index,:);
    nchrom(pos)=unidrnd(31);
    while length(unique(nchrom))==(length1-1)
        nchrom(pos)=unidrnd(31);
    end
    
    flag=test(nchrom);
    if flag==1
        chrom(index,:)=nchrom;
    end
    
end

ret=chrom;
end
 
````

</details>

#### Select · MATLAB · c75b4c7d

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `Select`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`74efd3fb8522322d530462157e4e66531744895146e81ca8f7f915e346bddcb4`
- 语言：MATLAB
- 符号：`Select`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/Select.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/concentration.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/excellence.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/fitness.m`

<details>
<summary>展开原始代码</summary>

````matlab
function ret=Select(individuals,sizepop)
% 轮盘赌选择
% individuals input  : 种群信息
% sizepop     input  : 种群规模
% ret         output : 选择后得到的种群

excellence=individuals.excellence;
pselect=excellence./sum(excellence);
% 事实上 pselect = excellence；

index=[]; 
for i=1:sizepop   % 转sizepop次轮盘
    pick=rand;
    while pick==0    
        pick=rand;        
    end
    for j=1:sizepop   
        pick=pick-pselect(j);        
        if pick<0        
            index=[index j];
            break;  % 寻找落入的区间，此次转轮盘选中了染色体j
        end
    end
end
% 注意：在转sizepop次轮盘的过程中，有可能会重复选择某些染色体

individuals.chrom=individuals.chrom(index,:);
individuals.fitness=individuals.fitness(index);
individuals.concentration=individuals.concentration(index);
individuals.excellence=individuals.excellence(index);
ret=individuals;

end
 
````

</details>

#### bestselect · MATLAB · b356189c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `bestselect`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`f05fa6e2a0fc0f87a000cfab4095932952d84359f63400e1229f063ad491b12f`
- 语言：MATLAB
- 符号：`bestselect`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/bestselect.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/concentration.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/excellence.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/fitness.m`

<details>
<summary>展开原始代码</summary>

````matlab
function rets=bestselect(individuals,m,n)
% 初始化记忆库,依据excellence，将群体中高适应度低相似度的overbest个个体存入记忆库
% m                  input          抗体数
% n                  input          记忆库个体数\父代群规模
% individuals        input          抗体群
% bestindividuals    output         记忆库\父代群

% 精英保留策略，将fitness最好的s个个体先存起来，避免因其浓度高而被淘汰
s=3;
rets=struct('fitness',zeros(1,n), 'concentration',zeros(1,n),'excellence',zeros(1,n),'chrom',[]);
[fitness,index] = sort(individuals.fitness);
for i=1:s
    rets.fitness(i) = individuals.fitness(index(i));   
    rets.concentration(i) = individuals.concentration(index(i));
    rets.excellence(i) = individuals.excellence(index(i));
    rets.chrom(i,:) = individuals.chrom(index(i),:);
end

% 剩余m-s个个体
leftindividuals=struct('fitness',zeros(1,m-s), 'concentration',zeros(1,m-s),'excellence',zeros(1,m-s),'chrom',[]);
for k=1:m-s
    leftindividuals.fitness(k) = individuals.fitness(index(k+s));   
    leftindividuals.concentration(k) = individuals.concentration(index(k+s));
    leftindividuals.excellence(k) = individuals.excellence(index(k+s));
    leftindividuals.chrom(k,:) = individuals.chrom(index(k+s),:);
end

% 将剩余抗体按excellence值排序
[excellence,index]=sort(1./leftindividuals.excellence);

% 在剩余抗体群中按excellence再选n-s个最好的个体
for i=s+1:n
    rets.fitness(i) = leftindividuals.fitness(index(i-s));
    rets.concentration(i) = leftindividuals.concentration(index(i-s));
    rets.excellence(i) = leftindividuals.excellence(index(i-s));
    rets.chrom(i,:) = leftindividuals.chrom(index(i-s),:);
end

end
````

</details>

#### concentration · MATLAB · d16b6f5c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `concentration`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`8999aeb7343521126670c7286db80ec7299811e688c823c9903400ef12a42074`
- 语言：MATLAB
- 符号：`concentration`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/concentration.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/similar.m`

<details>
<summary>展开原始代码</summary>

````matlab
function concentration = concentration(i,M,individuals)
% 计算个体浓度值
% i              input      第i个抗体
% M              input      种群规模
% individuals    input     个体
% concentration  output     浓度值

concentration=0;
for j=1:M
    xsd=similar(individuals.chrom(i,:),individuals.chrom(j,:));  % 第i个体与种群个体间的相似度
    % 相似度大于阀值
    if xsd>0.7
        concentration=concentration+1;
    end
end

concentration=concentration/M;

end
````

</details>

#### draw · MATLAB · 7f887d06

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a57b735c61b5abeb7116871ed49194ec9a5ad2c85311f7cab9b59d4daadcbd87`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/draw.m`

<details>
<summary>展开原始代码</summary>

````matlab
% 画出配送中心选址图
% 画出配送中心
cargox=bestchrom([1,3,5,7]);
cargoy=bestchrom([2,4,6,8]);

plot(cargox,cargoy,'rs','LineWidth',2,...
    'MarkerEdgeColor','r',...
    'MarkerFaceColor','b',...
    'MarkerSize',10)
hold on

% 画出需求点
plot(suplocationx,suplocationy,'o','LineWidth',2,...
    'MarkerEdgeColor','k',...
    'MarkerFaceColor','g',...
    'MarkerSize',10)
hold on

% 连接图
carlocationx=bestchrom([1,3,5,7]);
carlocationy=bestchrom([2,4,6,8]);
for i=9:128
    
    superindex=fix((i-8)/6)+1;  % 需求点
    if superindex==21
        superindex=20;
    end
    k=mod((i-8),6);
    cargoindex=bestchrom(i);   % 配送中心
    
    x=[suplocationx(superindex),carlocationx(cargoindex)];
    y=[suplocationy(superindex),carlocationy(cargoindex)];
    switch k
        case 0;plot(x,y,'c');hold on
        case 1;plot(x,y,'r');hold on
        case 2;plot(x,y,'y');hold on
        case 3;plot(x,y,'b');hold on
        case 4;plot(x,y,'g');hold on
        case 5;plot(x,y,'m');hold on
    end  
end
````

</details>

#### excellence · MATLAB · 7e9ad6bf

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `excellence`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ab4a2e258c9b7f86c5068f7c69011ce2665f9bf3abdd08bfcb022eda1c2eb7e5`
- 语言：MATLAB
- 符号：`excellence`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/excellence.m`

<details>
<summary>展开原始代码</summary>

````matlab
function exc=excellence(individuals,M,ps)
% 计算个体繁殖概率
% individuals    input      种群
% M              input      种群规模
% ps             input      多样性评价参数
% exc            output     繁殖概率

fit = 1./individuals.fitness;
sumfit = sum(fit);
con = individuals.concentration;
sumcon = sum(con);
for i=1:M
    exc(i) = fit(i)/sumfit*ps +con(i)/sumcon*(1-ps); 
end

end
````

</details>

#### fitness · MATLAB · 6226a7d1

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `fitness`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`eb5cc5c78f6e7365ae8c2b4cee4916f7c6e656c89d037907781276092ab30e5f`
- 语言：MATLAB
- 符号：`fitness`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/fitness.m`

<details>
<summary>展开原始代码</summary>

````matlab
function fit=fitness(individual)
%计算个体适应度值
%individual    input      个体
%fit           output     适应度值
%城市坐标
city_coordinate=[1304,2312;3639,1315;4177,2244;3712,1399;3488,1535;3326,1556;3238,1229;4196,1044;4312,790;4386,570;
                 3007,1970;2562,1756;2788,1491;2381,1676;1332,695;3715,1678;3918,2179;4061,2370;3780,2212;3676,2578;
                 4029,2838;4263,2931;3429,1908;3507,2376;3394,2643;3439,3201;2935,3240;3140,3550;2545,2357;2778,2826;2370,2975];
%city_coordinate=[1.25,1.25;8.75,0.75;0.5,4.75;5.75,5;3,6.5;7.25,7.75];           
%货物量
carge=[20,90,90,60,70,70,40,90,90,70,60,40,40,40,20,80,90,70,100,50,50,50,80,70,80,40,40,60,70,50,30];
%carge=[3,5,4,7,6,11];

%找出最近配送点
for i=1:31
    distance(i,:)=dist(city_coordinate(i,:),city_coordinate(individual,:)');
end

[a,b]=min(distance');

%计算费用
for i=1:31
    expense(i)=carge(i)*a(i);
end

%距离大于3000取一个惩罚值

fit=sum(expense) + 4.0e+4*length(find(a>3000));


end
````

</details>

#### incorporate · MATLAB · 036f3552

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `incorporate`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`35f97d08d1dfe61fa3666a99b5843ce07fdf42ff00fd892fa0f0cf848204a04f`
- 语言：MATLAB
- 符号：`incorporate`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/incorporate.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/concentration.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/excellence.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/fitness.m`

<details>
<summary>展开原始代码</summary>

````matlab
function newindividuals = incorporate(individuals,sizepop,bestindividuals,overbest)
% 将记忆库中抗体加入，形成新种群
% individuals         input          抗体群
% sizepop             input          抗体数
% bestindividuals     input          记忆库
% overbest            input          记忆库容量

m = sizepop+overbest;
newindividuals = struct('fitness',zeros(1,m), 'concentration',zeros(1,m),'excellence',zeros(1,m),'chrom',[]);

% 遗传操作得到的抗体
for i=1:sizepop
    newindividuals.fitness(i) = individuals.fitness(i);   
    newindividuals.concentration(i) = individuals.concentration(i);   
    newindividuals.excellence(i) = individuals.excellence(i);   
    newindividuals.chrom(i,:) = individuals.chrom(i,:);   
end
% 记忆库中抗体
for i=sizepop+1:m
    newindividuals.fitness(i) = bestindividuals.fitness(i-sizepop);   
    newindividuals.concentration(i) = bestindividuals.concentration(i-sizepop);   
    newindividuals.excellence(i) = bestindividuals.excellence(i-sizepop);   
    newindividuals.chrom(i,:) = bestindividuals.chrom(i-sizepop,:);   
end

end
````

</details>

#### main · MATLAB · 52646775

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`908443b80eb2232282101e31032ce9cae77deef9b1efb22def1799a213fed4c4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/main.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/Cross.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/Mutation.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/Select.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/bestselect.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/concentration.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/excellence.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/fitness.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/incorporate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/popinit.m`

<details>
<summary>展开原始代码</summary>

````matlab
%% 免疫优化算法在物流配送中心选址中的应用
%% 清空环境
clc
clear

%% 算法基本参数           
sizepop=50;           % 种群规模
overbest=10;          % 记忆库容量
MAXGEN=100;            % 迭代次数
pcross=0.5;           % 交叉概率
pmutation=0.4;        % 变异概率
ps=0.95;              % 多样性评价参数
length=6;             % 配送中心数
M=sizepop+overbest;

%% step1 识别抗原,将种群信息定义为一个结构体
individuals = struct('fitness',zeros(1,M), 'concentration',zeros(1,M),'excellence',zeros(1,M),'chrom',[]);
%% step2 产生初始抗体群
individuals.chrom = popinit(M,length);
trace=[]; %记录每代最个体优适应度和平均适应度

%% 迭代寻优
for iii=1:MAXGEN

     %% step3 抗体群多样性评价
     for i=1:M
         individuals.fitness(i) = fitness(individuals.chrom(i,:));      % 抗体与抗原亲和度(适应度值）计算
         individuals.concentration(i) = concentration(i,M,individuals); % 抗体浓度计算
     end
     % 综合亲和度和浓度评价抗体优秀程度，得出繁殖概率
     individuals.excellence = excellence(individuals,M,ps);
          
     % 记录当代最佳个体和种群平均适应度
     [best,index] = min(individuals.fitness);   % 找出最优适应度 
     bestchrom = individuals.chrom(index,:);    % 找出最优个体
     average = mean(individuals.fitness);       % 计算平均适应度
     trace = [trace;best,average];              % 记录
     
     %% step4 根据excellence，形成父代群，更新记忆库（加入精英保留策略，可由s控制）
     bestindividuals = bestselect(individuals,M,overbest);   % 更新记忆库
     individuals = bestselect(individuals,M,sizepop);        % 形成父代群

     %% step5 选择，交叉，变异操作，再加入记忆库中抗体，产生新种群
     individuals = Select(individuals,sizepop);                                                             % 选择
     individuals.chrom = Cross(pcross,individuals.chrom,sizepop,length);                                    % 交叉
     individuals.chrom = Mutation(pmutation,individuals.chrom,sizepop,length);   % 变异
     individuals = incorporate(individuals,sizepop,bestindividuals,overbest);                               % 加入记忆库中抗体      

end

%% 画出免疫算法收敛曲线
figure(1)
plot(trace(:,1));
hold on
plot(trace(:,2),'--');
legend('最优适应度值','平均适应度值')
title('免疫算法收敛曲线','fontsize',12)
xlabel('迭代次数','fontsize',12)
ylabel('适应度值','fontsize',12)

%% 画出配送中心选址图
%城市坐标
city_coordinate=[1304,2312;3639,1315;4177,2244;3712,1399;3488,1535;3326,1556;3238,1229;4196,1044;4312,790;4386,570;
                3007,1970;2562,1756;2788,1491;2381,1676;1332,695;3715,1678;3918,2179;4061,2370;3780,2212;3676,2578;
                 4029,2838;4263,2931;3429,1908;3507,2376;3394,2643;3439,3201;2935,3240;3140,3550;2545,2357;2778,2826;2370,2975];
carge=[20,90,90,60,70,70,40,90,90,70,60,40,40,40,20,80,90,70,100,50,50,50,80,70,80,40,40,60,70,50,30];
%找出最近配送点
for i=1:31
    distance(i,:)=dist(city_coordinate(i,:),city_coordinate(bestchrom,:)');
end
%city_coordinate=[1.25,1.25;8.75,0.75;0.5,4.75;5.75,5;3,6.5;7.25,7.75];           
%货物量
%carge=[3,5,4,7,6,11];

%找出最近配送点
%for i=1:31
   % distance(i,:)=dist(city_coordinate(i,:),city_coordinate(bestchrom,:)');
%end
[a,b]=min(distance');

index=cell(1,length);

for i=1:length
%计算各个派送点的地址
index{i}=find(b==i);
end
figure(2)
title('最优规划派送路线')
cargox=city_coordinate(bestchrom,1);
cargoy=city_coordinate(bestchrom,2);
plot(cargox,cargoy,'rs','LineWidth',2,...
    'MarkerEdgeColor','r',...
    'MarkerFaceColor','b',...
    'MarkerSize',20)
hold on

plot(city_coordinate(:,1),city_coordinate(:,2),'o','LineWidth',2,...
    'MarkerEdgeColor','k',...
    'MarkerFaceColor','g',...
    'MarkerSize',10)

for i=1:31
    x=[city_coordinate(i,1),city_coordinate(bestchrom(b(i)),1)];
    y=[city_coordinate(i,2),city_coordinate(bestchrom(b(i)),2)];
    plot(x,y,'c');hold on
end
````

</details>

#### popinit · MATLAB · 0d4357c6

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `popinit`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`85973658b83ccb706453a0d26887a02a872fbe65ae90755ee29a9997453f24f0`
- 语言：MATLAB
- 符号：`popinit`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/popinit.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/test.m`

<details>
<summary>展开原始代码</summary>

````matlab
function pop = popinit(n,length)
%种群初始化函数(记忆库库为空，全部随机产生)
% n       input    种群数量
% length  input    抗体长度
% pop     output   初始种群
for i=1:n
    flag=0;
    while flag==0
        [a,b]=sort(rand(1,31));    
        pop(i,:)=b(1:length);
        flag=test(pop(i,:));
    end
end
````

</details>

#### similar · MATLAB · 2d5696ce

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `similar`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9701b6cfcc5cdb339a29892bb167f3dafeac46b7074ece39d06139b25d9c4ae8`
- 语言：MATLAB
- 符号：`similar`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/similar.m`

<details>
<summary>展开原始代码</summary>

````matlab
function resemble = similar(individual1,individual2)
% 计算个体individual1和individual2的相似度
% individual1,individual2    input     两个个体
% resemble                   output     相似度

k=zeros(1,length(individual1));
for i=1:length(individual1)
    if find(individual1(i)==individual2)
        k(i)=1;
    end
end

resemble=sum(k)/length(individual1);

end
````

</details>

#### test · MATLAB · 716ce89c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `test`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ec6ab248bdae3fe2bf744d1a2af431a94f02a496c711be4a58249da446a2a81a`
- 语言：MATLAB
- 符号：`test`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/免疫算法程序实现/test.m`

<details>
<summary>展开原始代码</summary>

````matlab
function flag=test(code)
% 检查个体是否满足距离约束
% code    input     个体
% flag    output    是否满足要求标志

city_coordinate=[1304,2312;3639,1315;4177,2244;3712,1399;3488,1535;3326,1556;3238,1229;4196,1044;4312,790;4386,570;
                 3007,1970;2562,1756;2788,1491;2381,1676;1332,695;3715,1678;3918,2179;4061,2370;3780,2212;3676,2578;
                 4029,2838;4263,2931;3429,1908;3507,2376;3394,2643;3439,3201;2935,3240;3140,3550;2545,2357;2778,2826;2370,2975];

flag=1;
if max( max(dist( city_coordinate(code,:)') ) )>3000
    flag=0;
end

end
     
````

</details>

#### best · MATLAB · 2cc1ff2c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`709781c6a646fca338ba142ac77fdcd6127a9c4992aa18883bd3340fd8640f41`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/best.m`

<details>
<summary>展开原始代码</summary>

````matlab
Function
[bestindividual,bestfit,bestrestriction,nopos]=best(chrom,fitvalue,restriction);
[NIND,NVAR]=size(chrom);
pos=l;
for i=l:NIND
   if restriction(pos,l)>restriction(i,l)
      pos=i;
 end
 if(restriction(pos,l)==restriction(i,1))&(fitvalue(pos,l)<fitvalue(i,l))
      pos=i;
   end
end
bestindividual=chrom(pos,:);
bestfit=fitvalue(pos);
bestrestriction=restriction(pos,:);
nopos=l;
for i=l:NIND
   if restriction(nopos,l)<restriction(i,l)
       nopos=i;
   end
   if(restriction(nopos,1)==restriction(i,l))&(fitvalue(nopos,l)>fitvalue(i,l))
       nopos=i;
    end
end
````

</details>

#### calfitvalue · MATLAB · c152c2eb

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`39ca2bf342dbfa05cf0a04f9c2a0190b6d26d795545d02ee39c06e6eb39137d3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/calfitvalue.m`

<details>
<summary>展开原始代码</summary>

````matlab
function[fitvalue restriction]=calfitvalue(objvalue,chrom,Cmax,m,n,l,A,M,D,P)
global gen;
[NIND,NVAR]=size(chrom);
chrom1=chrom(:,1:n);
chrom2=chrom(:,(n+l):(n+m*n));
chrom3=chrom(:,(n+m*n+1):(n+m*n+n*l));
restriction=zeros(NIND,1);
r=zeros(NIND,m);
s=zeros(NIND,n);
t=zeros(NIND,1);
u=zeros(NIND,2);
p=zeros(NIND,n);
for i=l:NIND
   for i=l:m
      r(i,j)=A(j)-sum((chrom2(i,j:m:m*n)),2);
      if r(i,j)<0
      restriction(i,l)=restriction(i,l)+1;
    end
end
for j=1:l
    t(i,j)=sum((chrom3(i,j:l:n*l)),2)-D(j);
    if t(i,j)<0
      restriction(i,l)=restriction(i,l)+1;
     end
end
for j=l:n
 s(i,j)=chrom1(i,j)*M(j)-sum(chrom2(i,(m*(j-1)+2):(m*j),2));
 p(i,j)=abs(sum(chrom3(i,(l*(j-1)+1):(l*j)),2)-sum(chrom2(i,(m*(j-1)+l):(m*j)),2));
       if s(i,j)<0
         restriction(i,1)=restriotion(i,l)+l;
       end
       if p(i,j)>=1e-3
         restriction(i,l)=restriction(i,l)+l;
       end
end
  u(i,l)=P-sum(chrom1(i,:),2);
     if u(i,1)<0
         restriction(i,l)=restriction(i,l)+l;
end
 u(i,2)=sum(chrom1(i,:),2)-l;
     if u(i,2)<0
         restriction(i,l)=restriction(i,l)+l;
     end
if(objvalue(i,1)<Cmax)
  fitvalue(i,l)=Cmax-objvalue(i,l);
else
fitvalue(i,l)=0.0;
     end
end
````

</details>

#### calobjvalue · MATLAB · b80acba7

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a279c5a2fce3132733d342ec607485eba35f5025bafa9aac841e01efd676dd11`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/calobjvalue.m`

<details>
<summary>展开原始代码</summary>

````matlab
 function[objvalue]=calobjvalue(chrom,m,n,l,a,c,v,f)
chrom1=chrom(:,1:n);
chrom2=chrom(:,(n+l):(n+m*n));
chrom3=chrom(:,(n+m*n+1):(n+m*n+n*l));
[NIND,NVAR]=size(chrom);
for i=l:NIND
   for j=l:n
      u(i,j)=120*sum(chrom2(i,(2*(j-1)+l):(2*j)),2);
   end
end
objvalue=chrom2*a*120+chrom3*c*260+sqrt(u).*chrom1*v+chrom1*f;
````

</details>

#### crossover · MATLAB · f6b69ab8

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ff5eedbb59496da1481a36eb895490f4f679b816e2f504a2fc27d281a40a3dc5`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/crossover.m`

<details>
<summary>展开原始代码</summary>

````matlab
function[newchrom]=crossover(chrom,m,n,l)
global gen;
[NIND,NVAR]=size(chrom);
chrom1=chrom(:,1:n);
chrom2=chrom(:,(n+l):(n+m*n));
chrom3=chrom(:,(n+m*n+l):(n+m*n+n*l));
newchrom=zeros(NIND,NVAR);
Pc=0.75;
for i =l:2:NIND-l
    if(rand<Pc)
        point=ceil(rand*(n-l));
        if point<5
    newchrom(i,:)=[chrom1(i,l:point) chroml(i+l,point+l:n)...
chrom2(i,l:m*point)  chrom2(i+l,m*point+l:m*n)...
chrom3(i,1:l*point) chrom3(i+l,l*point+l:n*l)];
newehrom(i+l,:)=[chrom1(i+l,l:point) chrom1(i,point+l:n)...
chrom2(i+l,l:m*point)  chrom2(i,m*point+1:m*n)...
chrom3(i+l,l:l*point)  chrom3(i,l*point+l:n*l)];
        else
          newchrom(i,:)=chrom(i,:);
        newchrom(i+1,:)=chrom(i+l,:);
        end
    else
        newchrom(i,:)=chrom(i,:);
        newchrom(i+l,:)=chrom(i+l,:);
    end
end
````

</details>

#### main · MATLAB · 9de49035

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`33d5d8b275d3538f2696f3bc418fc6563e3f7f627f9e1fd278048b175456a8d4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/main.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/best.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/calfitvalue.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/calobjvalue.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/crossover.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/mutation.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/selection.m`

<details>
<summary>展开原始代码</summary>

````matlab
global gen;
NIND=200;
MAXGEN=2000;
NVAR=55;
Cmax=5000000;
Pm=0.3;
m=2;
n=5;
l=8;
A=[100 100];
M=[90 105 100 115 115];
D=[10 10 10 15 5 15 10 15];
f=[60000;90000;60000;75000;75000];
v=[50;65;60;55;55];
a=[60;120;70;100;80;90;120;60;110;80];
e=[30;55;25;40;25;50;55;55;65;80;40;45;20;35;20;20;50;55;15;25;5;25;45;25;65;75;
45;30;35;10;50;10;45;35;15;10;30;25;60;40];
P=3;
for i=l:NIND
    while 0<l
         for j=l:5
            chroml(i,j)=round(rand(l));
         end
         if(sum(chroml(i,:),2)>=l)&(sum(chroml(i,:),2)<=P)
            break
         end
     end
end
 sumx=zeros(NIND,5); 
 sumy=zeros(NIND,5);
for i=l:NIND
  for j=l:5
if chrom1(i,j)==0
    chrom2(i,(2*(j-l)+l):(2*j))=0;
    chrom3(i,(8*(j-l)+l):(8*j))=0;
else
    while chrom1(i,j)==1
    chrom2(i,(2*(j-1)+l):(2*j))=rand(1,2).*min(A,[M(j),M(j)]);
    sumx(i,j)=sum(chrom2(i,(2*(j-l)+l):(2*j)),2);
	chrom3(i,(8*(j-1)+l):(8*j))=rand(l,8).*(rep(M(j),[1 l]));
	  sumy(i,j)=sum(chrom3(i,(8*(j-l)+l):(8*j)),2);
      chrom3(i,(8*(j-l)+l):(8*j))=(sumx(i,j)/sumy(i,j))*chrom3(i,(8*(j-l)+l):(8*j));
    if sumx(i,j)<=1.0*M(j)
       break
        end
      end
    end
  end
end
Chrom=[chrom1 chrom2 chrom3];
[objvalue]=calobjvalue(chrom,m,n,l,a,c,v,f);
[fitvalue,restriction]=calfitvalue(objvalue,chrom,Cmax,m,n,l,A,M,D,P);
[bestindividual,bestfit,bestrestriction,nopos]=best(chrom,fitvalue,restrietion);
gen= 0;
while gen<MAXGEN
   [objvalue]=calobjvalue(chrom,m,n,l,a,c,v,f);
[fitvalue,restriction]=calfitvalue(objvaluechrom,Cmax,m,n,1,A,M,D,P);
[bestindividual1,bestfit1,bestrestriction1,nopos1]=best(chrom,fitvalue,restriction);
    if bestrestrction>bestrestriction1
      bestindividual=bestindividual1;
      bestfit=bestfit1;
      bestrestriction=bestrestriction1;
end
if(bestrestriction==bestrestriction1)&&(bestfit<bestfit1)
   bestindividual=bestindividual1;
   bestfit=bestfit1;
   bestrestriction=bestrestriction1;
end
chrom(nopos1,:)=bestindividual;
[newchrom]=selection(chrom,fitvalue);
[newchrom]=crossover(newchrom,m,n,l);
[newchrom]=mutation(newchrom,Pm,m,n,l);
[bestindividual2,bestfit2,bestrestriction2,nopos2]=best(newchrom,fitvalue,restriction);
if bestrestriction>bestrestriction2
    bestindividual=bestindividual2;
    bestfit=bestfit2;
    bestrestriction=bestrestriction2;
end
if(bestrestriction==bestrestriction2)&&(bestfit<bestfit2)
   bestindividual=bestindividual2;
   bestfit=bestfit2;
   bestrestriction=bestrestriction2;
end
chrom=newchrom;
gen=gen+l;
end
   bestindividual;bestfit;bestrestriction;
  
````

</details>

#### mutation · MATLAB · 8eeb8a05

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7657678a92efe4351e26955c3b52b5dd42f5697e415f8be53ca8654a871b96a0`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/mutation.m`

<details>
<summary>展开原始代码</summary>

````matlab
function[newchrom]=mutation(chrom,Pm,m,n,l)
global gen;
FieldDR=[0 0 0 0 0 0 0 0 0 0;90 90 105 105 100 100 115 115 115 115];
RANGE=[0 0 0 0 0 0 0 0;10 10 10 15 5 15 10 15];
[NIND,NVAR]=size(chrom);
chrom1=chrom(:,l:n);
chrom2=chrom(:,(n+l):(n+m*n));
chrom3=chrom(:,(n+m*n+1):(n+m*n+n*l));
newchrom=zeros(NIND,NVAR);
newchrom1=zeros(NIND,n);
newchrom2=zeros(NIND,m*n);
newchrom3=zeros(NIND,n*l);
for i=l:NIND
    for j=l:n
        if chrom1(i,j)==0
            newchrom2(i,(m*(j-l)+l):(m*j))=0;
            newchrom3(i,(l*(j-l)+l):(l*j))=0;
    else
       if round(rand)==0
       newchrom2(i,(m*(j-l)+l):(m*j))=chrom2(i,(m*(j-l)+l):(m*j))+...
(FieldDR(2,(m*(j-l)+l):(m*j))-chrom2(i,(m*(j-l)+l):(m*j)))*(l-rand^((l-gen/2000)^10));
       newchrom3(i,(l*(j-l)+l):(l*j))=chrom3(i,(l*(j-l)+l):(l*j))+...
([10 10 10 15 5 15 10 15]-chrom3(i,(l*(j-l)+1):(l*j)))*(l-rand^((1-gen/2000)^10));
        elseif round(rand)==1
        newchrom2(i,(m*(j-l)+l):(m*j))=chrom2(i,(m*(j-l)+1):(m*j))-...
(chrom2(i,(m*(j-l)+l):(m*j))-[0 0])*(1-rand^((l-gen/2000)^10));
        newchrom3(i,(l*(j-l)+l):(l*j))=chrom3(i,(l*(j-1)+l):(l*j))-...
(chrom3(i,(1*(j-1)+l):(l*j))-[0 0 0 0 0 0 0 0]*(l-rand^((l-gen/2000)^10)));
        end
     end
   end
end
 newchrom1=chrom1;
 newchrom=[newchrom1 newchrom2 newchrom3];
````

</details>

#### selection · MATLAB · 3b1222e0

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`f4cbab05c0006e9057e9b3945a9daa584b3eded9e950c36ee266407a7d0eac1d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/物流选址/遗传算法/selection.m`

<details>
<summary>展开原始代码</summary>

````matlab
function[newchrom]=selection(chrom,fitvalue)
totalfit=sum(fitvalue);
fitvalue=fitvalue/totalfit;
fitvalue=cumsum(fitvalue);
[NIND,NVAR]=size(chrom);
ms=sort(rand(NIND,l));
fitin=l;newin=l;
	while newin<=NIND
if(ms(newin))<fitValue(fitin)
temp(newin,:)=chrom(fitin,:);
newin=newin+l;
else
fitin=fitin+1;
end
if fitin>=NIND
    fitin=NIND;
end
end
newchrom=temp;
````

</details>

#### GAFCM · MATLAB · 1c74e832

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`060cf3f5b749ad558d6af0ee54f9403dae8c23f6dc522870d3b4a628da88731b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/GAFCM.m`

<details>
<summary>展开原始代码</summary>

````matlab
% 遗传算法改进的模糊C-均值聚类MATLAB源码
function [BESTX,BESTY,ALLX,ALLY]=GAFCM(K,N,Pm,LB,UB,D,c,m)
%% 此函数实现遗传算法，用于模糊C－均值聚类
%% 输入参数列表
% K        迭代次数
% N        种群规模，要求是偶数
% Pm       变异概率
% LB       决策变量的下界，M×1的向量
% UB       决策变量的上界，M×1的向量
% D        原始样本数据，n×p的矩阵
% c        分类个数
% m        模糊C均值聚类数学模型中的指数
%% 输出参数列表
% BESTX    K×1细胞结构，每一个元素是M×1向量，记录每一代的最优个体
% BESTY    K×1矩阵，记录每一代的最优个体的评价函数值
% ALLX     K×1细胞结构，每一个元素是M×N矩阵，记录全部个体
% ALLY     K×N矩阵，记录全部个体的评价函数值
%% 第一步：
M=length(LB);%决策变量的个数
%种群初始化，每一列是一个样本
farm=zeros(M,N);
for i=1:M
    x=unifrnd(LB(i),UB(i),1,N);
    farm(i,:)=x;
end
%输出变量初始化
ALLX=cell(K,1);%细胞结构，每一个元素是M×N矩阵，记录每一代的个体
ALLY=zeros(K,N);%K×N矩阵，记录每一代评价函数值
BESTX=cell(K,1);%细胞结构，每一个元素是M×1向量，记录每一代的最优个体
BESTY=zeros(K,1);%K×1矩阵，记录每一代的最优个体的评价函数值
k=1;%迭代计数器初始化
%% 第二步：迭代过程
while k<=K
%% 以下是交叉过程
    newfarm=zeros(M,2*N);
    Ser=randperm(N);%两两随机配对的配对表
    A=farm(:,Ser(1));
    B=farm(:,Ser(2));
    P0=unidrnd(M-1);
    a=[A(1:P0,:);B((P0+1):end,:)];%产生子代a
    b=[B(1:P0,:);A((P0+1):end,:)];%产生子代b
    newfarm(:,2*N-1)=a;%加入子代种群
    newfarm(:,2*N)=b;    
    for i=1:(N-1)
        A=farm(:,Ser(i));
        B=farm(:,Ser(i+1));
        P0=unidrnd(M-1);
        a=[A(1:P0,:);B((P0+1):end,:)];
        b=[B(1:P0,:);A((P0+1):end,:)];
        newfarm(:,2*i-1)=a;
        newfarm(:,2*i)=b;
    end    
    FARM=[farm,newfarm];    
%% 选择复制
    SER=randperm(3*N);
    FITNESS=zeros(1,3*N);
    fitness=zeros(1,N);
    for i=1:(3*N)
        Beta=FARM(:,i);
        FITNESS(i)=FIT(Beta,D,c,m);
    end    
    for i=1:N
        f1=FITNESS(SER(3*i-2));
        f2=FITNESS(SER(3*i-1));
        f3=FITNESS(SER(3*i));
        if f1<=f2&&f1<=f3
            farm(:,i)=FARM(:,SER(3*i-2));
            fitness(:,i)=FITNESS(:,SER(3*i-2));
        elseif f2<=f1&&f2<=f3
            farm(:,i)=FARM(:,SER(3*i-1));
            fitness(:,i)=FITNESS(:,SER(3*i-1));
        else
            farm(:,i)=FARM(:,SER(3*i));
            fitness(:,i)=FITNESS(:,SER(3*i));
        end
    end    
    %% 记录最佳个体和收敛曲线
    X=farm;
    Y=fitness;
    ALLX{k}=X;
    ALLY(k,:)=Y;
    minY=min(Y);
    pos=find(Y==minY);
    BESTX{k}=X(:,pos(1));
    BESTY(k)=minY;    
    %% 变异
    for i=1:N
        if Pm>rand&&pos(1)~=i
            AA=farm(:,i);
            BB=GaussMutation(AA,LB,UB);
            farm(:,i)=BB;
        end
    end
    disp(k);
    k=k+1;
end
%% 绘图
BESTY2=BESTY;
BESTX2=BESTX;
for k=1:K
    TempY=BESTY(1:k);
    minTempY=min(TempY);
    posY=find(TempY==minTempY);
    BESTY2(k)=minTempY;
    BESTX2{k}=BESTX{posY(1)};
end
BESTY=BESTY2;
BESTX=BESTX2;
plot(BESTY,'-ko','MarkerEdgeColor','k','MarkerFaceColor','k','MarkerSize',2)
ylabel('函数值')
xlabel('迭代次数')
grid on 
````

</details>

#### MPGA · MATLAB · efc92505

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`3be3ef407462f6d47ada9326340791bb891df5a4e5cecd7e783b01e9b693b195`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MPGA.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/CRTRP.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MIGRATE.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MUTATE.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RANKING.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RECOMBIN.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REINS.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REP.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RESPLOT.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/SELECT.M`

<details>
<summary>展开原始代码</summary>

````matlab
% mpga         multi population genetic algorithm
%
% This script implements the Multi Population Genetic Algorithm.
% A real-valued representation of the individuals is used.
%

% Author:     Andrew Chipperfield
% History:    30-Mar-94     file created

NVAR = 20;		% No. of decision variables (control steps)
RANGE = [0;200];	% Bounds on decision variables

% Set field descriptor
   FieldD = rep(RANGE,[1,NVAR]);

% Define GA Parameters
   GGAP = .8;		% Generation gap, how many new individuals are created
   XOVR =  1;		% Crossover rate
   MUTR = 1/NVAR;	% Mutation rate depending on NVAR
   MAXGEN = 1200;	% Maximum number of generations
   TERMEXACT = 1e-4;    % Value for termination if minimum reached
   INSR = .9;		% Insertion rate, how many of the offspring are inserted
   SUBPOP = 8;		% Number of subpopulations
   MIGR = 0.2;		% Migration rate between subpopulations
   MIGGEN = 20;		% Number of generations between migration
   NIND = 20;		% Number of individuals per subpopulation

% Specify other routines as strings
   SEL_F = 'sus';       % Name of selection function
   XOV_F = 'recdis';    % Name of recombination function for individuals
   MUT_F = 'mutbga';    % Name of mutation function
   OBJ_F = 'objharv';   % Name of function for objective values


% Get value of minimum, defined in objective function
   GlobalMin = feval(OBJ_F,[],3);

% Get title of objective function, defined in objective function
   FigTitle = [feval(OBJ_F,[],2) '   (' int2str(SUBPOP) ':' int2str(MAXGEN) ') '];

% Clear Best  and storing matrix
   % Initialise Matrix for storing best results
      Best = NaN * ones(MAXGEN,3);
      Best(:,3) = zeros(size(Best,1),1);
   % Matrix for storing best individuals
      IndAll = [];

% Create real population
   Chrom = crtrp(SUBPOP*NIND,FieldD);

% reset count variables
   gen = 0;

% Calculate objective function for population
   ObjV = feval(OBJ_F,Chrom);
   % count number of objective function evaluations
   Best(gen+1,3) = Best(gen+1,3) + NIND;

% Generational loop
   while gen < MAXGEN,

   % Save the best and average objective values and the best individual
      [Best(gen+1,1),ix] = min(ObjV);
      Best(gen+1,2) = mean(ObjV);
      IndAll = [IndAll; Chrom(ix,:)];

   % Fitness assignment to whole population
      FitnV = ranking(ObjV,2 ,SUBPOP);
            
   % Select individuals from population
      SelCh = select(SEL_F, Chrom, FitnV, GGAP, SUBPOP);
      
   % Recombine selected individuals
      SelCh=recombin(XOV_F, SelCh, XOVR, SUBPOP);

   % Mutate offspring
      SelCh=mutate(MUT_F, SelCh, FieldD, [MUTR], SUBPOP);

   % Calculate objective function for offsprings
      ObjVOff = feval(OBJ_F,SelCh);
      Best(gen+1,3) = Best(gen+1,3) + size(SelCh,1);

   % Insert best offspring in population replacing worst parents
      [Chrom, ObjV] = reins(Chrom, SelCh, SUBPOP, [1 INSR], ObjV, ObjVOff);

      gen=gen+1;

   % Plot some results, rename title of figure for graphic output
      if ((rem(gen,20) == 1) | (rem(gen,MAXGEN) == 0)),
         set(gcf,'Name',[FigTitle ' in ' int2str(gen)]);
         resplot(Chrom(1:2:size(Chrom,1),:),...
                 IndAll(max(1,gen-39):size(IndAll,1),:),...
                 [ObjV; GlobalMin], Best(max(1,gen-19):gen,[1 2]), gen);
      end


   % migrate individuals between subpopulations
      if (rem(gen,MIGGEN) == 0)
         [Chrom, ObjV] = migrate(Chrom, SUBPOP, [MIGR, 1, 0], ObjV);
      end

   end


% Results
   % add number of objective function evaluations
   Results = cumsum(Best(1:gen,3));
   % number of function evaluation, mean and best results
   Results = [Results Best(1:gen,2) Best(1:gen,1)];
   
% Plot Results and show best individuals => optimum
   figure('Name',['Results of ' FigTitle]);
   subplot(2,1,1), plot(Results(:,1),Results(:,2),'-',Results(:,1),Results(:,3),':');
   subplot(2,1,2), plot(IndAll(gen-4:gen,:)');
 

% End of script


````

</details>

#### MUTBGA · MATLAB · a7bb4f10

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `mutbga`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`b9fe17257bc5a3c5ee901553861c8a13ca51711984d5e24a9dc8d76b391ddf53`
- 语言：MATLAB
- 符号：`mutbga`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MUTBGA.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REP.M`

<details>
<summary>展开原始代码</summary>

````matlab
% MUTBGA.M       (real-value MUTation like Breeder Genetic Algorithm)
%
% This function takes a matrix OldChrom containing the real
% representation of the individuals in the current population,
% mutates the individuals with probability MutR and returns
% the resulting population.
%
% This function implements the mutation operator of the Breeder Genetic
% Algorithm. (Muehlenbein et. al.)
%
% Syntax:  NewChrom = mutbga(OldChrom, FieldDR, MutOpt)
%
% Input parameter:
%    OldChrom  - Matrix containing the chromosomes of the old
%                population. Each line corresponds to one individual.
%    FieldDR   - Matrix describing the boundaries of each variable.
%    MutOpt    - (optional) Vector containing mutation rate and shrink value
%                MutOpt(1): MutR - number containing the mutation rate -
%                           probability for mutation of a variable
%                           if omitted or NaN, MutR = 1/variables per individual
%                           is assumed
%                MutOpt(2): MutShrink - (optional) number for shrinking the
%                           mutation range in the range [0 1], possibility to
%                           shrink the range of the mutation depending on,
%                           for instance actual generation.
%                           if omitted or NaN, MutShrink = 1 is assumed
%
% Output parameter:
%    NewChrom  - Matrix containing the chromosomes of the population
%                after mutation in the same format as OldChrom.

% Author:     Hartmut Pohlheim
% History:    23.11.93     file created
%             24.11.93     function optimised (for,for-loop to for-loop)
%                          mutation rate included
%                          style improved
%             06.12.93     change of function name
%                          check of boundaries after mutation out of loop
%             16.12.93     NewMutMat and OldMutMat included for compability
%             16.02.94     preparation for multi-subpopulations at once
%             25.02.94     NewMutMat and OldMutMat removed (now in mutran10.m)
%                          clean up
%                          change of function name in mutbga.m
%             03.03.94     Lower and Upper directly used (less memory)
%             19.03.94     multipopulation support removed
%                          more parameter checks
%             27.03.94     Delta exact calculated, for loop saved


function NewChrom = mutbga(OldChrom, FieldDR, MutOpt);

% Check parameter consistency
   if nargin < 2,  error('Not enough input parameter'); end

   % Identify the population size (Nind) and the number of variables (Nvar)
   [Nind,Nvar] = size(OldChrom);

   [mF, nF] = size(FieldDR);
   if mF ~= 2, error('FieldDR must be a matrix with 2 rows'); end
   if Nvar ~= nF, error('FieldDR and OldChrom disagree'); end

   if nargin < 3, MutR = 1/Nvar; MutShrink = 1;
   elseif isempty(MutOpt), MutR = 1/Nvar; MutShrink = 1;
   elseif isnan(MutOpt), MutR = 1/Nvar; MutShrink = 1;
   else   
      if length(MutOpt) == 1, MutR = MutOpt; MutShrink = 1;
      elseif length(MutOpt) == 2, MutR = MutOpt(1); MutShrink = MutOpt(2);
      else, error(' Too many parameter in MutOpt'); end
   end

   if isempty(MutR), MutR = 1/Nvar;
   elseif isnan(MutR), MutR = 1/Nvar;
   elseif length(MutR) ~= 1, error('Parameter for mutation rate must be a scalar');
   elseif (MutR < 0 | MutR > 1), error('Parameter for mutation rate must be a scalar in [0, 1]'); end

   if isempty(MutShrink), MutShrink = 1;
   elseif isnan(MutShrink), MutShrink = 1;
   elseif length(MutShrink) ~= 1, error('Parameter for shrinking mutation range must be a scalar');
   elseif (MutShrink < 0 | MutShrink > 1), 
      error('Parameter for shrinking mutation range must be a scalar in [0, 1]');
   end
     
% the variables are mutated with probability MutR
% NewChrom = OldChrom (+ or -) * Range * MutShrink * Delta
% Range = 0.5 * (upperbound - lowerbound)
% Delta = Sum(Alpha_i * 2^-i) from 0 to ACCUR; Alpha_i = rand(ACCUR,1) < 1/ACCUR

% Matrix with range values for every variable
   Range = rep(0.5 * MutShrink *(FieldDR(2,:)-FieldDR(1,:)),[Nind 1]);

% zeros and ones for mutate or not this variable, together with Range
   Range = Range .* (rand(Nind,Nvar) < MutR);

% compute, if + or - sign 
   Range = Range .* (1 - 2 * (rand(Nind,Nvar) < 0.5));

% used for later computing, here only ones computed
   ACCUR = 20;
   Vect = 2 .^ (-(0:(ACCUR-1))');
   Delta = (rand(Nind,ACCUR) < 1/ACCUR) * Vect;
   Delta = rep(Delta, [1 Nvar]);

% perform mutation 
   NewChrom = OldChrom + Range .* Delta;

% Ensure variables boundaries, compare with lower and upper boundaries
   NewChrom = max(rep(FieldDR(1,:),[Nind 1]), NewChrom);
   NewChrom = min(rep(FieldDR(2,:),[Nind 1]), NewChrom);


% End of function


````

</details>

#### RANKING · MATLAB · a6ae6768

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `ranking`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`90523e59f9863d00812e95c0952b04e2064d7e08ca14dfa3830770cf580bb0bb`
- 语言：MATLAB
- 符号：`ranking`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RANKING.M`

<details>
<summary>展开原始代码</summary>

````matlab
% RANKING.M      (RANK-based fitness assignment)
%
% This function performs ranking of individuals.
%
% Syntax:  FitnV = ranking(ObjV, RFun, SUBPOP)
%
% This function ranks individuals represented by their associated
% cost, to be *minimized*, and returns a column vector FitnV
% containing the corresponding individual fitnesses. For multiple
% subpopulations the ranking is performed separately for each
% subpopulation.
%
% Input parameters:
%    ObjV      - Column vector containing the objective values of the
%                individuals in the current population (cost values).
%    RFun      - (optional) If RFun is a scalar in [1, 2] linear ranking is
%                assumed and the scalar indicates the selective pressure.
%                If RFun is a 2 element vector:
%                RFun(1): SP - scalar indicating the selective pressure
%                RFun(2): RM - ranking method
%                         RM = 0: linear ranking
%                         RM = 1: non-linear ranking
%                If RFun is a vector with length(Rfun) > 2 it contains
%                the fitness to be assigned to each rank. It should have
%                the same length as ObjV. Usually RFun is monotonously
%                increasing.
%                If RFun is omitted or NaN, linear ranking
%                and a selective pressure of 2 are assumed.
%    SUBPOP    - (optional) Number of subpopulations
%                if omitted or NaN, 1 subpopulation is assumed
%
% Output parameters:
%    FitnV     - Column vector containing the fitness values of the
%                individuals in the current population.
%                

% Author:     Hartmut Pohlheim (Carlos Fonseca)
% History:    01.03.94     non-linear ranking
%             10.03.94     multiple populations

function FitnV = ranking(ObjV, RFun, SUBPOP);

% Identify the vector size (Nind)
   [Nind,ans] = size(ObjV);

   if nargin < 2, RFun = []; end
   if nargin > 1, if isnan(RFun), RFun = []; end, end
   if prod(size(RFun)) == 2,
      if RFun(2) == 1, NonLin = 1;
      elseif RFun(2) == 0, NonLin = 0;
      else error('Parameter for ranking method must be 0 or 1'); end
      RFun = RFun(1);
      if isnan(RFun), RFun = 2; end
   elseif prod(size(RFun)) > 2,
      if prod(size(RFun)) ~= Nind, error('ObjV and RFun disagree'); end
   end

   if nargin < 3, SUBPOP = 1; end
   if nargin > 2,
      if isempty(SUBPOP), SUBPOP = 1;
      elseif isnan(SUBPOP), SUBPOP = 1;
      elseif length(SUBPOP) ~= 1, error('SUBPOP must be a scalar'); end
   end

   if (Nind/SUBPOP) ~= fix(Nind/SUBPOP), error('ObjV and SUBPOP disagree'); end
   Nind = Nind/SUBPOP;  % Compute number of individuals per subpopulation
   
% Check ranking function and use default values if necessary
   if isempty(RFun),
      % linear ranking with selective pressure 2
         RFun = 2*[0:Nind-1]'/(Nind-1);
   elseif prod(size(RFun)) == 1
      if NonLin == 1,
         % non-linear ranking
         if RFun(1) < 1, error('Selective pressure must be greater than 1');
         elseif RFun(1) > Nind-2, error('Selective pressure too big'); end
         Root1 = roots([RFun(1)-Nind [RFun(1)*ones(1,Nind-1)]]);
         RFun = (abs(Root1(1)) * ones(Nind,1)) .^ [(0:Nind-1)'];
         RFun = RFun / sum(RFun) * Nind;
      else
         % linear ranking with SP between 1 and 2
         if (RFun(1) < 1 | RFun(1) > 2),
            error('Selective pressure for linear ranking must be between 1 and 2');
         end
         RFun = 2-RFun + 2*(RFun-1)*[0:Nind-1]'/(Nind-1);
      end
   end;

   FitnV = [];

% loop over all subpopulations
for irun = 1:SUBPOP,
   % Copy objective values of actual subpopulation
      ObjVSub = ObjV((irun-1)*Nind+1:irun*Nind);
   % Sort does not handle NaN values as required. So, find those...
      NaNix = isnan(ObjVSub);
      Validix = find(~NaNix);
   % ... and sort only numeric values (smaller is better).
      [ans,ix] = sort(-ObjVSub(Validix));

   % Now build indexing vector assuming NaN are worse than numbers,
   % (including Inf!)...
      ix = [find(NaNix) ; Validix(ix)];
   % ... and obtain a sorted version of ObjV
      Sorted = ObjVSub(ix);

   % Assign fitness according to RFun.
      i = 1;
      FitnVSub = zeros(Nind,1);
      for j = [find(Sorted(1:Nind-1) ~= Sorted(2:Nind)); Nind]',
         FitnVSub(i:j) = sum(RFun(i:j)) * ones(j-i+1,1) / (j-i+1);
         i =j+1;
      end

   % Finally, return unsorted vector.
      [ans,uix] = sort(ix);
      FitnVSub = FitnVSub(uix);

   % Add FitnVSub to FitnV
      FitnV = [FitnV; FitnVSub];
end


% End of function

````

</details>

#### REINS · MATLAB · 52ba1584

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`3f260e5b26029fd5b658901251e50c7c6c66ec858682f07c14ad986a44fda98d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REINS.M`

<details>
<summary>展开原始代码</summary>

````matlab
% REINS.M        (RE-INSertion of offspring in population replacing parents)
%
% This function reinserts offspring in the population.
%
% Syntax: [Chrom, ObjVCh] = reins(Chrom, SelCh, SUBPOP, InsOpt, ObjVCh, ObjVSel)
%
% Input parameters:
%    Chrom     - Matrix containing the individuals (parents) of the current
%                population. Each row corresponds to one individual.
%    SelCh     - Matrix containing the offspring of the current
%                population. Each row corresponds to one individual.
%    SUBPOP    - (optional) Number of subpopulations
%                if omitted or NaN, 1 subpopulation is assumed
%    InsOpt    - (optional) Vector containing the insertion method parameters
%                ExOpt(1): Select - number indicating kind of insertion
%                          0 - uniform insertion
%                          1 - fitness-based insertion
%                          if omitted or NaN, 0 is assumed
%                ExOpt(2): INSR - Rate of offspring to be inserted per
%                          subpopulation (% of subpopulation)
%                          if omitted or NaN, 1.0 (100%) is assumed
%    ObjVCh    - (optional) Column vector containing the objective values
%                of the individuals (parents - Chrom) in the current 
%                population, needed for fitness-based insertion
%                saves recalculation of objective values for population
%    ObjVSel   - (optional) Column vector containing the objective values
%                of the offspring (SelCh) in the current population, needed for
%                partial insertion of offspring,
%                saves recalculation of objective values for population
%
% Output parameters:
%    Chrom     - Matrix containing the individuals of the current
%                population after reinsertion.
%    ObjVCh    - if ObjVCh and ObjVSel are input parameter, than column 
%                vector containing the objective values of the individuals
%                of the current generation after reinsertion.
           
% Author:     Hartmut Pohlheim
% History:    10.03.94     file created
%             19.03.94     parameter checking improved

function [Chrom, ObjVCh] = reins(Chrom, SelCh, SUBPOP, InsOpt, ObjVCh, ObjVSel);


% Check parameter consistency
   if nargin < 2, error('Not enough input parameter'); end
   if (nargout == 2 & nargin < 6), error('Input parameter missing: ObjVCh and/or ObjVSel'); end

   [NindP, NvarP] = size(Chrom);
   [NindO, NvarO] = size(SelCh);

   if nargin == 2, SUBPOP = 1; end
   if nargin > 2,
      if isempty(SUBPOP), SUBPOP = 1;
      elseif isnan(SUBPOP), SUBPOP = 1;
      elseif length(SUBPOP) ~= 1, error('SUBPOP must be a scalar'); end
   end

   if (NindP/SUBPOP) ~= fix(NindP/SUBPOP), error('Chrom and SUBPOP disagree'); end
   if (NindO/SUBPOP) ~= fix(NindO/SUBPOP), error('SelCh and SUBPOP disagree'); end
   NIND = NindP/SUBPOP;  % Compute number of individuals per subpopulation
   NSEL = NindO/SUBPOP;  % Compute number of offspring per subpopulation

   IsObjVCh = 0; IsObjVSel = 0;
   if nargin > 4, 
      [mO, nO] = size(ObjVCh);
      if nO ~= 1, error('ObjVCh must be a column vector'); end
      if NindP ~= mO, error('Chrom and ObjVCh disagree'); end
      IsObjVCh = 1;
   end
   if nargin > 5, 
      [mO, nO] = size(ObjVSel);
      if nO ~= 1, error('ObjVSel must be a column vector'); end
      if NindO ~= mO, error('SelCh and ObjVSel disagree'); end
      IsObjVSel = 1;
   end
       
   if nargin < 4, INSR = 1.0; Select = 0; end   
   if nargin >= 4,
      if isempty(InsOpt), INSR = 1.0; Select = 0;   
      elseif isnan(InsOpt), INSR = 1.0; Select = 0;   
      else
         INSR = NaN; Select = NaN;
         if (length(InsOpt) > 2), error('Parameter InsOpt too long'); end
         if (length(InsOpt) >= 1), Select = InsOpt(1); end
         if (length(InsOpt) >= 2), INSR = InsOpt(2); end
         if isnan(Select), Select = 0; end
         if isnan(INSR), INSR =1.0; end
      end
   end
   
   if (INSR < 0 | INSR > 1), error('Parameter for insertion rate must be a scalar in [0, 1]'); end
   if (INSR < 1 & IsObjVSel ~= 1), error('For selection of offspring ObjVSel is needed'); end 
   if (Select ~= 0 & Select ~= 1), error('Parameter for selection method must be 0 or 1'); end
   if (Select == 1 & IsObjVCh == 0), error('ObjVCh for fitness-based exchange needed'); end

   if INSR == 0, return; end
   NIns = min(max(floor(INSR*NSEL+.5),1),NIND);   % Number of offspring to insert   

% perform insertion for each subpopulation
   for irun = 1:SUBPOP,
      % Calculate positions in old subpopulation, where offspring are inserted
         if Select == 1,    % fitness-based reinsertion
            [Dummy, ChIx] = sort(-ObjVCh((irun-1)*NIND+1:irun*NIND));
         else               % uniform reinsertion
            [Dummy, ChIx] = sort(rand(NIND,1));
         end
         PopIx = ChIx((1:NIns)')+ (irun-1)*NIND;
      % Calculate position of Nins-% best offspring
         if (NIns < NSEL),  % select best offspring
            [Dummy,OffIx] = sort(ObjVSel((irun-1)*NSEL+1:irun*NSEL));
         else              
            OffIx = (1:NIns)';
         end
         SelIx = OffIx((1:NIns)')+(irun-1)*NSEL;
      % Insert offspring in subpopulation -> new subpopulation
         Chrom(PopIx,:) = SelCh(SelIx,:);
         if (IsObjVCh == 1 & IsObjVSel == 1), ObjVCh(PopIx) = ObjVSel(SelIx); end
   end


% End of function

````

</details>

#### SAGAFcmMain · MATLAB · d73d4a28

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`9f0e8b3efa3a49376e9789ac4e1fddc39a9a6306c0cbc1edb9da18c962ffe6be`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/SAGAFcmMain.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/CRTBP.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MUT.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/ObjFun.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RANKING.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RECOMBIN.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REP.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/SELECT.M`

<details>
<summary>展开原始代码</summary>

````matlab
%% 2、遗传模拟优化初始聚类中心
clc
clear all
close all
load X
m=size(X,2);% 样本特征维数
% 中心点范围[lb;ub]
lb=min(X);
ub=max(X);
%% 模糊C均值聚类参数
% 设置幂指数为3，最大迭代次数为20，目标函数的终止容限为1e-6
options=[3,20,1e-6];
% 类别数cn
cn=4;
%% 模拟退火算法参数
q =0.8;     % 冷却系数
T0=100;    % 初始温度
Tend=99.999;  % 终止温度
%% 定义遗传算法参数
sizepop=10;               %个体数目(Numbe of individuals)
MAXGEN=100;                %最大遗传代数(Maximum number of generations)
NVAR=m*cn;                %变量的维数
PRECI=10;                 %变量的二进制位数(Precision of variables)
pc=0.7;
pm=0.01;
trace=zeros(NVAR+1,MAXGEN);
%建立区域描述器(Build field descriptor)
FieldD=[rep([PRECI],[1,NVAR]);rep([lb;ub],[1,cn]);rep([1;0;1;1],[1,NVAR])];
Chrom=crtbp(sizepop, NVAR*PRECI); % 创建初始种群
V=bs2rv(Chrom, FieldD);
ObjV=ObjFun(X,cn,V,options); %计算初始种群个体的目标函数值
T=T0;
while T>Tend
    gen=0;                                               %代计数器
    while gen<MAXGEN                                     %迭代
        FitnV=ranking(ObjV);                          %分配适应度值(Assign fitness values)
        SelCh=select('sus', Chrom, FitnV);         %选择
        SelCh=recombin('xovsp', SelCh,pc);             %重组
        SelCh=mut(SelCh,pm);                                %变异
        V=bs2rv(SelCh, FieldD);
        newObjV=ObjFun(X,cn,V,options);  %计算子代目标函数值
        newChrom=SelCh;

        %是否替换旧个体
        for i=1:sizepop
            if ObjV(i)>newObjV(i)
                ObjV(i)=newObjV(i);
                Chrom(i,:)=newChrom(i,:);
            else
                p=rand;
                if p<=exp((newObjV(i)-ObjV(i))/T)
                    ObjV(i)=newObjV(i);
                    Chrom(i,:)=newChrom(i,:);
                end
            end
        end
        gen=gen+1;                                                 %代计数器增加
        [trace(end,gen),index]=min(ObjV);                          %遗传算法性能跟踪
        trace(1:NVAR,gen)=V(index,:);
        fprintf(1,'%d ',gen);
    end
    T=T*q;
    fprintf(1,'\n温度:%1.3f\n',T);
end
[newObjV,center,U]=ObjFun(X,cn,[trace(1:NVAR,end)]',options);  %计算最佳初始聚类中心的目标函数值
% 查看聚类结果
Jb=newObjV
U=U{1};
center=center{1};
figure
plot(X(:,1),X(:,2),'o')
hold on
maxU = max(U);
index1 = find(U(1,:) == maxU);
index2 = find(U(2, :) == maxU);
index3 = find(U(3, :) == maxU);
% 在前三类样本数据中分别画上不同记号 不加记号的就是第四类了
line(X(index1,1), X(index1, 2), 'linestyle', 'none','marker', '*', 'color', 'g');
line(X(index2,1), X(index2, 2), 'linestyle', 'none', 'marker', '*', 'color', 'r');
line(X(index3,1), X(index3, 2), 'linestyle', 'none', 'marker', '*', 'color', 'b');
% 画出聚类中心
plot(center(:,1),center(:,2),'v')
hold off
````

</details>

#### SCALING · MATLAB · 50f6ee16

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `scaling`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9f95050c5b2cedddd9606d27edcf0515f83f9b2fec85a1090d30180e24b0a09b`
- 语言：MATLAB
- 符号：`scaling`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/SCALING.M`

<details>
<summary>展开原始代码</summary>

````matlab
% SCALING.m - linear fitness scaling
%
% This function implements a linear fitness scaling algorithm as described
% by Goldberg in "Genetic Algorithms in Search, Optimization and Machine
% Learning", Addison Wesley, 1989.  It use is not recommended when fitness
% functions produce negative results as the scaling will become unreliable.
% It is included in this version of the GA Toolbox only for the sake of
% completeness.
%
% Syntax:	FitnV = scaling(ObjV, Smul)
%
% Input parameters:
%
%		Objv	- A vector containing the values of individuals
%			  fitness.
%
%		Smul	- Optional scaling parameter (default 2).
%
% Output parameters:
%
%		FitnV	- A vector containing the individual fitnesses
%			  for the current population.
%			  
%

% Author: Andrew Chipperfield
% Date: 24-Feb-94


function FitnV = scaling( ObjV, Smul )

if nargin == 1
	Smul = 2 ;
end

[Nind, Nobj] = size( ObjV ) ;
Oave = sum( ObjV ) / Nind ;
Omin = min( ObjV ) ;
Omax = max( ObjV ) ;

if (Omin > ( Smul * Oave - Omax ) / ( Smul - 1.0 ))
	delta = Omax - Oave 
	a = ( Smul - 1.0 ) * Oave / delta 
	b = Oave * ( Omax - Smul * Oave ) / delta 
else
	delta = Oave - Omin ;
	a = Oave / delta ;
	b = -Omin * Oave / delta ;
end

FitnV = ObjV.*a + b ;

````

</details>

#### SGA · MATLAB · 19660750

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：执行选择、交叉和变异的进化搜索；执行归一化或标准化以统一变量尺度；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`ed469760636b72242f946ec8e3a852688c48ba5f6059ae2835a4fff3bda61b56`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/SGA.M`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/CRTBP.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/MUT.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/OBJFUN1.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RANKING.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/RECOMBIN.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REINS.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/REP.M`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/聚类分析问题/遗传和模拟退火的聚类程序/SELECT.M`

<details>
<summary>展开原始代码</summary>

````matlab
% sga
%
% This script implements the Simple Genetic Algorithm described
% in the examples section of the GA Toolbox manual.
%

% Author:     Andrew Chipperfield
% History:    23-Mar-94     file created
 

NIND = 40;           % Number of individuals per subpopulations
MAXGEN = 300;        % maximum Number of generations
GGAP = .9;           % Generation gap, how many new individuals are created
NVAR = 20;           % Generation gap, how many new individuals are created
PRECI = 20;          % Precision of binary representation

% Build field descriptor
   FieldD = [rep([PRECI],[1, NVAR]); rep([-512;512],[1, NVAR]);...
              rep([1; 0; 1 ;1], [1, NVAR])];

% Initialise population
   Chrom = crtbp(NIND, NVAR*PRECI);

% Reset counters
   Best = NaN*ones(MAXGEN,1);	% best in current population
   gen = 0;			% generational counter

% Evaluate initial population
   ObjV = objfun1(bs2rv(Chrom,FieldD));

% Track best individual and display convergence
   Best(gen+1) = min(ObjV);
   plot(log10(Best),'ro');xlabel('generation'); ylabel('log10(f(x))');
   text(0.5,0.95,['Best = ', num2str(Best(gen+1))],'Units','normalized');   
   drawnow;        


% Generational loop
   while gen < MAXGEN,

    % Assign fitness-value to entire population
       FitnV = ranking(ObjV);

    % Select individuals for breeding
       SelCh = select('sus', Chrom, FitnV, GGAP);

    % Recombine selected individuals (crossover)
       SelCh = recombin('xovsp',SelCh,0.7);

    % Perform mutation on offspring
       SelCh = mut(SelCh);

    % Evaluate offspring, call objective function
       ObjVSel = objfun1(bs2rv(SelCh,FieldD));

    % Reinsert offspring into current population
       [Chrom ObjV]=reins(Chrom,SelCh,1,1,ObjV,ObjVSel);

    % Increment generational counter
       gen = gen+1;

    % Update display and record current best individual
       Best(gen+1) = min(ObjV);
       plot(log10(Best),'ro'); xlabel('generation'); ylabel('log10(f(x))');
       text(0.5,0.95,['Best = ', num2str(Best(gen+1))],'Units','normalized');
       drawnow;
   end 
% End of GA

````

</details>

#### 1 · C++ · ea77cb80

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：使用显式数据结构和循环实现核心算法。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4d9e63593e929cc68928a369d5755192a3f52c9091e57f99dda56979095f01a1`
- 语言：C++
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/1.cpp`

<details>
<summary>展开原始代码</summary>

````cpp
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main()
{
	float min(float,float);
	int i,j,s[9][9]={0},n=8,L[9]={0},Q=8,Ln=0,M[4]={0},jb=0,ib=0,a=0,b=0,N[5]={0},x=0,y=0;
	float t[9][9]={0},DERTAa1,DERTAa2,DERTAb1,DERTAb2,k[9],EF[100],qq=0,q[8]={0};

float g[9]={0,2,1.5,4.5,3,1.5,4,2.5,3};
float T[9]={0,1,2,1,3,2,2.5,3,0.8};
float ET[9]={0,1,4,1,4,3,2,5,1.5};
float LT[9]={0,4,6,2,7,5.5,5,8,4};
int d[9][9]={0,40,60,75,90,200,100,160,80,40,
             0,65,40,100,50,75,110,100,60,65,
             0,75,100,100,75,75,75,75,40,75,
             0,100,50,90,90,150,90,100,100,100,
             0,100,75,75,100,200,50,100,50,100,
             0,70,90,75,100,75,75,90,75,70,
             0,70,100,160,110,75,90,75,90,70,
             0,100,80,100,75,150,100,75,100,100,0};

printf("各任务的货运量g[i]如下：\n");


for (i=1;i<=n;i++)
{printf("g%d=%-5.1f",i,g[i]);
}
printf("\n\n\n");


printf("各任务的装货（或卸货）时间T[i]为：\n");
for (i=1;i<=n;i++)
{printf("T%d=%-5.1f",i,T[i]);
}
printf("\n\n\n");


printf("各任务的开始执行的时间范围[ETi,LTi]为：\n");
for (i=1;i<=n;i++)
{printf("[ET%d,LT%d]=[%-3.1f,%-3.1f]\n",i,i,ET[i],LT[i]);
}
printf("\n\n\n");

 
printf("车场0与各任务点间的距离d[i][j]为：\n");   
	for(i=0;i<=8;i++)
		{for(j=0;j<=8;j++)
	{printf("%5d",d[i][j]);}
	printf("\n");
	}

printf("\n\n");


printf("点对之间连接的费用节约值s[i][j]为：\n");

for(i=1;i<=8;i++)
{for(j=i+1;j<=8;j++)
{ s[i][j]=d[i][0]+d[0][j]-d[i][j];
   
}
}
	for(i=1;i<=8;i++)
		{for(j=i+1;j<=8;j++)
	{printf("s[%d][%d]=%-5d",i,j,s[i][j]);}
	printf("\n");
	}


printf("\n");



for(i=0;i<=8;i++)
{for(j=0;j<=8;j++){t[i][j]=(float)d[i][j]/50;}}

for(i=0;i<=8;i++)
{if ((t[0][i]>=ET[i])&&(t[0][i]<=LT[i]))
{k[i]=t[0][i];}
if (t[0][i]<ET[i])
{k[i]=ET[i];}}







while (1)
{ ib=0;jb=0;
	for(i=1;i<=8;i++)
{   for(j=i+1;j<=8;j++)
{if (s[i][j]>s[a][b])    {a=i;b=j;}} 
}

if (s[a][b]==0) break;
N[1]=0;N[2]=M[1];N[3]=M[1]+M[2];N[4]=M[1]+M[2]+M[3];
for(i=0;i<8;i++)
{if (L[i]==a) {ib=1;x=i;}}
 
for(j=0;j<8;j++)
{if (L[j]==b) {jb=1;y=j;}}

if (ib==0&&jb==0)
{qq=g[a]+g[b];if (qq>Q) {s[a][b]=0;continue;}
EF[b]=k[a]+T[a]+t[a][b]-k[b];
EF[a]=k[b]+T[b]+t[a][b]-k[a];
DERTAb1=LT[b]-k[b];
DERTAb2=k[b]-ET[b];
DERTAa1=LT[a]-k[a];
DERTAa2=k[a]-ET[a];


if (((EF[b]>=0)&&(DERTAb1>=EF[b]))||((EF[b]<0)&&(DERTAb2>=(0-EF[b]))))
{L[N[4]]=a;
L[N[4]+1]=b;
Ln=Ln+1;
q[Ln]=qq;
k[b]=k[b]+EF[b];
s[a][b]=0;
M[Ln]=M[Ln]+2;
continue;}

else if ((EF[a]>=0&&DERTAa1>=EF[a])||(EF[a]<0&&(DERTAa2>=(0-EF[a]))))
{L[N[4]]=b;
L[N[4]+1]=a;
Ln=Ln+1;
q[Ln]=qq;
k[a]=k[a]+EF[a];
s[a][b]=0;
M[Ln]=M[Ln]+2;
continue;}


}


if (ib==0&&jb==1)
{i=a;a=b;b=i;x=y;ib=1;jb=0;}

if (ib==1&&jb==0)
{if (x==N[1]||x==N[2]||x==N[3])
{i=a;a=b;b=i;}

for(i=1;i<=3;i++)
{if (x==N[i])
{qq=q[i]+g[a];
if (qq>Q) {s[a][b]=0;s[b][a]=0;continue;}
EF[b]=k[a]+T[a]+t[a][b]-k[b];


if (EF[b]>0) 
{DERTAb1=min(LT[L[x]]-k[L[x]],LT[L[x+1]]-k[L[x+1]]);
if (EF[b]>DERTAb1) {s[a][b]=0;s[b][a]=0;continue;}}


if (EF[b]<0)
{DERTAb2=min(k[L[x]]-ET[L[x]],k[L[x+1]]-ET[L[x+1]]);

if ((0-EF[b])>DERTAb2) {s[a][b]=0;s[b][a]=0;continue;}}


for(j=6;j>=x;j--)
{L[j+1]=L[j];}
L[x]=a;

k[L[x+1]]=k[L[x+1]]+EF[L[x+1]];

k[L[x+2]]=k[L[x+2]]+EF[L[x+1]];
q[i]=qq;

M[i]=M[i]+1;
}
}

for(i=1;i<=3;i++)
{if (x==N[i+1]-1)
 {qq=q[i]+g[b];

if (qq>Q) {s[a][b]=0;s[b][a]=0;continue;}
EF[b]=k[a]+T[a]+t[a][b]-k[b];
if (EF[b]>=0) 
{DERTAb1=LT[b]-k[b];
if (EF[b]>DERTAb1) {s[a][b]=0;s[b][a]=0;continue;}}

if (EF[b]<0)
{DERTAb2=k[b]-ET[b];
if ((0-EF[b])>DERTAb2) {s[a][b]=0;s[b][a]=0;continue;}}

for(j=6;j>=x;j--)
{L[j+2]=L[j+1];L[x+1]=b;}

k[L[x+1]]=k[L[x+1]]+EF[L[x+1]];

M[i]=M[i]+1;
q[i]=qq;

}
}
}
s[a][b]=0;s[b][a]=0;
}




printf("得到的最终的路线为：\n");

for(i=1;i<=3;i++)
{printf("0->");
	for(j=N[i];j<N[i+1];j++){printf(" %d -> ",L[j]);}
	printf("0");
	printf("\n\n");
}

printf("\n\n");

printf("各路线的总任务量Q[i]为：\n");

for(i=1;i<=3;i++){printf("Q[%d]=%3.1f\n",i,q[i]);}

printf("\n\n");

printf("各路线的新的开始时间s[i]为：\n");
for(i=1;i<=8;i++){printf("s[%d]=%3.1f\n",i,k[i]);}

printf("\n\n");

system ("pause");
return(0);
}

float min(float x,float y)
{float z;z=x<y?x:y;return(z);}
````

</details>

#### VRP · MATLAB · de0c58fd

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `VRP`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`bdb1333ac5c65c709cf65604f50e115e152c36584733001599b7f903213989db`
- 语言：MATLAB
- 符号：`VRP`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/VRP.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/geneticVRP.m`

<details>
<summary>展开原始代码</summary>

````matlab
%%遗传算法求解vrp问题(为选择操作从新设计后程序)
%D是距离矩阵，n为种群个数
%C为停止代数，遗传到第 C代时程序停止,C的具体取值视问题的规模和耗费的时间而定
%m为适配值淘汰加速指数,最好取为1,2,3,4,不宜太大
%交叉概率Pc，变异概率Pm 
%R为最短路径,Rlength为路径长度
function VRP

%初始化
demand=[0 1 2 1 2 1 4 2 2];
D=[ 0 4 6 7.5 9 20 10 16 8;
    4 0 6.5 4 10 5 7.5 11 10;
    6 6.5 0 7.5 10 10 7.5 7.5 7.5;
    7.5 4 7.5 0 10 5 9 9 15;
    9 10 10 10 0 10 7.5 7.5 10;
    20 5 10 5 10 0 7 7 7.5;
    10 7.5 7.5 9 7.5 7 0 0 10;
    16 11 7.5 9 7.5 9 7 10 10;
    8 10 7.5 15 10 7.5 10 10 0];
            
n=100;
C=200;
m=2;
Pc=0.9;
Pm=0.2;


[R,Rlength]=geneticVRP(D,demand,n,C,m,Pc,Pm);%运算返回最优路径R和其总距离Rlength
````

</details>

#### exchange · MATLAB · 7403ee7a

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`97ac6e9fbced40845ac89959893d0bff3248507b1869daeada92ec37449db241`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/exchange.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [x,y]=exchange(x,y)
temp=x;
x=y;
y=temp;
````

</details>

#### geneticVRP · MATLAB · 6ee276a6

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`92d4b8cfff280e7299a282cef4f9870ed8c20ad0a5932a463abaaae1bc05b7bf`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/geneticVRP.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/intercross.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/mutate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/myLength.m`

<details>
<summary>展开原始代码</summary>

````matlab

%D是距离矩阵，n为种群个数

%C为停止代数，遗传到第 C代时程序停止,C的具体取值视问题的规模和耗费的时间而定
%m为适值淘汰加速指数,最好取为1,2,3,4,不宜太大
%交叉概率Pc,变异概率Pm
%R为最短路径,Rlength为路径长度
      
function [R,Rlength]=geneticVRP(D,demand,n,C,m,Pc,Pm)
         [N,NN]=size(D);%(31*31)
         farm=zeros(n,N);%用于存储种群
         for i=1:n
            % flag=0;
             %while flag==0
              %tem=randperm(N); %随机生成初始种群
             %if validate(tem,demand,N)==1
              %  flag=1;
             %end
             %end
             farm(i,:)=randperm(N);
             end
         R=farm(1,:);%一个随机解(个体)

                           %farm(1,:)=R;
        len=zeros(n,1);%存储路径长度
        fitness=zeros(n,1);%存储适配值
        counter=0;
        
       while counter<C
            for i=1:n
                len(i,1)=myLength(D,farm(i,:));%计算路径长度
            end
            %maxlen=max(len);
            minlen=min(len);
           
            %fitness=fit(len,m,maxlen,minlen);%计算适应度
            rr=find(len==minlen);%返回的是在len中路径最短的路径坐标(i,1)
            
            R=farm(rr(1,1),:);%更新最短路径
                                                   %disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            FARM=farm;%优胜劣汰，nn记录了复制的个数
%选择,  
          K=30;
          [aa,bb]=size(FARM);
          FARM2=FARM;
          len2=len;
          [len]=sort(len);
          for i=1:aa
              tt= find(len2==len(i,1));
              FARM(i,:)=FARM2(tt(1,1),:);
          end   
          for i=1:K
              j=aa+1-i;
              FARM(j,:)=FARM(i,:);
              
          end                                 
 %                交叉操作
              [aa,bb]=size(FARM);
               FARM2=FARM;
             
               for i=1:2:aa
                    
                       if Pc>rand&&i<aa %交叉概率Pc
                            A=FARM(i,:);
                            B=FARM(i+1,:);
                            [A,B]=intercross(A,B);
                            FARM(i,:)=A;
                            FARM(i+1,:)=B;
                       end  
                      
               end
              %交叉检验  (可省去)             
               for i=1:aa
                   if myLength(D,FARM(i,:))>myLength(D,FARM2(i,:))
                       FARM(i,:)=FARM2(i,:);
                   end
               end
               clear FARM2
          
             [aa,bb]=size(FARM); %aa=nn2
   
%       变异   
            FARM2=FARM;
            for i=1:aa
                if Pm>=rand                    
                  FARM(i,:)=mutate(FARM(i,:));
                end
            end
             %变异检验(可省略)  
               for i=1:aa
                   if myLength(D,FARM(i,:))>myLength(D,FARM2(i,:))
                       FARM(i,:)=FARM2(i,:);
                   end
               end
               clear FARM2
%群体的更新
           %FARM2=zeros(n-aa+1,N);
           %if n-aa>=1             
           %    for i=1:n-aa
           %       FARM2(i,:)=randperm(N);%随机生成n-aa种群
           %     end
           % end
           FARM=[R;FARM];%将随机产生的n-aa个体加入从后面种群,将上次迭代的最优解从前面加入种群
           [aa,bb]=size(FARM);
                                                   %disp('~~~~~~~~~~~~~~~~4~~~~~~~验证zong~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
             %保持种群规模为n                                         
            if aa>n
                FARM=FARM(1:n,:);
            end   
     
    
                                                    %disp('~~~~~~~~~~~~~~~~~~~5~~~~验证zong~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            %更新farm
            farm=FARM;
            clear FARM
            %更新迭代次数
            counter=counter+1 ; 
            
       end
 %结果输出
      
        Rlength=myLength(D,R)    
        
        R
        Rlength=myLength(D,R)%结果输出
````

</details>

#### immuni · MATLAB · 9bc6ab25

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `immuni`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f6604f865c0cd2e20b94d460b58ab5f1b590349daa85a5427379021d6e8790eb`
- 语言：MATLAB
- 符号：`immuni`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/immuni.m`

<details>
<summary>展开原始代码</summary>

````matlab
% 免疫遗传
function a=immuni(a,b)
m=length(a);
c=zeros(m);

for i=1:m
    c(i)=a(i);  
    c(i+1)=a(b(i,2));
    delete  a(b(i,2));
    c(i+2)=a(i+3);
end

    a=c;
````

</details>

#### intercross · MATLAB · 85ebb9d5

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`6b37d5d716eeea19b849b04c6b5f6d7bce850e4048df02a2f0820789dfa9c01e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/intercross.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/exchange.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/myLength.m`

<details>
<summary>展开原始代码</summary>

````matlab
%交叉算法采用部分匹配交叉%交叉算法采用部分匹配交叉
function [a,b]=intercross(a,b)
L=length(a);
if L<=10  %确定交叉宽度
    W=9;
elseif ((L/10)-floor(L/10))>=rand&&L>10
    W=ceil(L/10)+8;
else
    W=floor(L/10)+8;
end
p=unidrnd(L-W+1);%随机选择交叉范围，从p到p+W
for i=1:W
    %交叉
    x=find(a==b(1,p+i-1));
    y=find(b==a(1,p+i-1));
    [a(1,p+i-1),b(1,p+i-1)]=exchange(a(1,p+i-1),b(1,p+i-1));
    [a(1,x),b(1,y)]=exchange(a(1,x),b(1,y));   
end





%function [FARM]=intercross(FARM,D,Pc)
%[s,t]=size(FARM);%n*N
%FARM1=FARM;
%for i=1:2:s
  %  if Pc>rand&&i<=s-1
    %     crosspoint =randperm(t-1);
  %       if crosspoint(2)<crosspoint(1)
   %          p=crosspoint(2);
 %            crosspoint(2)=crosspoint(1);
   %          crosspoint(1)=p;
   %      end
    %     middle=zeros(1,crosspoint(2)-crosspoint(1));
   %      middle=FARM(i,crosspoint(1)+1:crosspoint(2));
   %      FARM(i,crosspoint(1)+1:crosspoint(2))=FARM(i+1,crosspoint(1)+1:crosspoint(2));
  %       FARM(i+1,crosspoint(1)+1:crosspoint(2))=middle;
    %     for j=1:crosspoint(1)
    %          while find(FARM(i,crosspoint(1)+1:crosspoint(2))==FARM(i,j))
     %            zhi=find(FARM(i,crosspoint(1)+1:crosspoint(2))==FARM(i,j));
  %               y=FARM(i+1,crosspoint(1)+zhi);
    %             FARM(i,j)=y;
   %           end
    %     end
  
  %      for j=crosspoint(2)+1:t
  %           while find(FARM(i,crosspoint(1)+1:crosspoint(2))==FARM(i,j))
  %                zhi=find(FARM(i,crosspoint(1)+1:crosspoint(2))==FARM(i,j));
   %               y=FARM(i+1,crosspoint(1)+zhi);
 %                 FARM(i,j)=y;
    %         end
    %    end
       
       % 如果个体退化选择父代
       
    %   for i=1:s
    %       if myLength(D,FARM1(i,:))<myLength(D,FARM1(i,:))
           %    FARM(i,:)=FARM1(i,:);
    %       end
   %    end
  %  end
%end

        
        
````

</details>

#### mutate · MATLAB · b744d363

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `mutate`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`68d14d7d6bacc962b155d68cb12d3b4cec0bc9596537c926bdfc1ebf73aee0cb`
- 语言：MATLAB
- 符号：`mutate`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/mutate.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/exchange.m`

<details>
<summary>展开原始代码</summary>

````matlab
function a=mutate(a)
L=length(a);
rray=randperm(L);
[a(rray(1)),a(rray(2))]=exchange(a(rray(1)),a(rray(2)));
````

</details>

#### myLength · MATLAB · 4bdc3e11

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `myLength`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`40efd5ca6b9672ddb25337a88c2649f0b1ced2013a8cdc0811545488e6a3ebfc`
- 语言：MATLAB
- 符号：`myLength`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/车辆调度问题/vrp/myLength.m`

<details>
<summary>展开原始代码</summary>

````matlab

%总路径len



function len=myLength(D,p)
[N,NN]=size(D);
%len=D(p(1,N),p(1,1));
 len=0;
for i=1:(N-1)
   len=len+D(p(1,i),p(1,i+1));
end

       total=[0 0];
     volume=8;
     demand=[0 1 2 1 2 1 4 2 2];
   
        x=find(p==1);
  if x<9      
     %len=len+D(p(1,x),p(1,x+1))+D(p(1,N),1)+D(1,p(1,1))+D(p(1,x),1);
     %len=len+D(p(x),p(x+1))+D(p(N),1)+D(1,p(1))+D(p(x),1);
     len=len+D(p(x),p(x+1))+D(p(N),p(x))+D(1,p(1))+D(p(x),1);
  else
      len=len+D(p(1,N),p(1,1))+D(1,p(1,1));
  end
  
   %len=len+D(p(x),p(x+1))+D(p(N),1)+D(1,p(1))+D(p(x),1);
    %len=D(1,p(1,1))+D(p(1,x),1);
    
    for i=1:x
        %len=len+D(p(1,i),p(1,i+1));
        total(1)=demand(p(1,i))+total(1);
    end
    
    %len=len+D(p(1,x),p(1,x+1))+D(p(1,N),1);
    for i=(x+1):N
        total(2)=demand(p(1,i))+total(2);
        %len=len+D(p(1,i),p(1,i+1))+D(1,p(1,1))+D(p(1,x),1);
    end
    
    
    if total(2)>volume | total(1)>volume
       len=len+100;
    end
   
        
````

</details>

#### fun1 · MATLAB · e3dfbf48

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `fun1`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`51e93d0eb6375dbdb0559046a8f701c6dfddb3ea2eb59e457c810677e827e3fa`
- 语言：MATLAB
- 符号：`fun1`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法解方程/fun1.m`

<details>
<summary>展开原始代码</summary>

````matlab
function y=fun1(x);   %x为行向量 
c1=[2 3 1]'; c2=[3 1 0]'; 
y=x*c1+x.^2*c2; y=-y; 
````

</details>

#### fun2 · MATLAB · ca710635

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`71aa177cb922973db39a7364459128a56bced4e0aeaec8d63a450325cf7557bb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法解方程/fun2.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [f,g]=fun2(x); 
f=[x(1)+2*x(1)^2+x(2)+2*x(2)^2+x(3)-10 
   x(1)+x(1)^2+x(2)+x(2)^2-x(3)-50 
   2*x(1)+x(1)^2+2*x(2)+x(3)-40]; 
g=x(1)^2+x(3)-2; 
````

</details>

#### mian · MATLAB · b79c2738

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d62c0300a741a2fb9ecddb95042bec403c2416c28c06b7b46806902bd489c4c4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法解方程/mian.m`

<details>
<summary>展开原始代码</summary>

````matlab
a=[-1 -2 0;-1 0 0];b=[-1;0]; 
[x,y]=ga(@fun1,3,a,b,[],[],[],[],@fun2); 
x,y=-y 
````

</details>

#### 免疫算法 · MATLAB · c4600762

- 归属算法：遗传算法GA
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“模型求解”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `immunity`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`3d6bf9ca684282aa1035311d435d950d8c63db8cda41c28a2856326a05ea6eb8`
- 语言：MATLAB
- 符号：`immunity`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/免疫算法.txt`

<details>
<summary>展开原始代码</summary>

````matlab
免疫算法 matlab程序2008-04-19 21:38%这是免疫算法。这个算法几乎与遗传算法一样，只是多用了一个免疫函数
%免疫算法是遗传算法的变体，它不用杂交，而是采用注入疫苗的方法。
%疫苗是优秀染色体中的一段基因，把疫苗接种到其它染色体中

%注意：标准遗传算法的一个重要概念是，染色体是可能解的2进制顺序号，由这个序号在可能解的集合(解空间)中找到可能解
%这是免疫算法的主程序，它需要调用的函数如下。
%接种疫苗函数：
%function inoculateChromosome=immunity(chromosomeGroup,bacterinChromosome,parameter)
%parameter:1,随机制取染色体接种。2，每个染色体都接种。3，每个染色体都接种，但接种的位置是随机的
%这个函数实现对染色体的疫苗接种
%由染色体(可能解的2进制)顺序号找到可能解：
%x=chromosome_x(fatherChromosomeGroup,oneDimensionSet,solutionSum);
%把解代入非线性方程组计算误差函数：functionError=nonLinearSumError1(x);
%判定程是否得解函数：[solution,isTrue]=isSolution(x,funtionError,solutionSumError);
%选择最优染色体函数：
%[bestChromosome,leastFunctionError]=best_worstChromosome(fatherChromosomeGroup,functionError);
%误差比较函数：从两个染色体中，选出误差较小的染色体
%[holdBestChromosome,holdLeastFunctionError]...
% =compareBestChromosome(holdBestChromosome,holdLeastFunctionError,...
% bestChromosome,leastFuntionError)
%为染色体定义概率函数，好的染色体概率高，坏染色体概率低
%p=chromosomeProbability(functionError);
%按概率选择染色体函数：
%slecteChromosomeGroup=selecteChromome(fatherChromosomeGroup,p);
%父代染色体杂交产生子代染色体函数
%sonChrmosomeGroup=crossChromosome(slecteChromosomeGroup,2);
%防止染色体超出解空间的函数
%chromosomeGroup=checkSequence(chromosomeGroup,solutionSum)
%变异函数
%fatherChromosomeGroup=varianceCh(sonChromosomeGroup,0.8,solutionN);
%通过实验有如下结果：
%1。染色体应当多一些
%2。通过概率选择染色体，在迭代早期会有效选出优秀的染色体，使解的误差迅速降低，
%但随着迭代的进行，概率选择也会导致某种染色体在基因池中迅速增加，使染色体趋同，
%这就减少了物种的多样性，反而难以逼近解
%3。不用概率选择，仅采用染色体杂交，采用保留优秀染色体，也可以得到解
%4。单纯免疫效果不好，杂交+免疫效果比较好

%%%%%%%%%%%%%%%%%%%%%%%%程序开始运行

clear,clc;%清理内存，清屏
circleN=200;%迭代次数
format long

%%%%%%%%%%%%%%%构造可能解的空间，确定染色体的个数、长度
solutionSum=4;leftBoundary=-10;rightBoundary=10;
distance=1;chromosomeSum=500;solutionSumError=0.1;
%solutionSum:非线性方程组的元数(待解变量的个数)；leftBoundary:可能解的左边界；
%rightBoundary:可能解的右边界；distance:可能解的间隔，也是解的精度
%chromosomeSum:染色体的个数；solveSumError:解的误差
oneDimensionSet=leftBoundary:distance:rightBoundary;
%oneDimensionSet:可能解在一个数轴(维)上的集合
oneDimensionSetN=size(oneDimensionSet,2);%返回oneDimensionSet中的元素个数
solutionN=oneDimensionSetN^solutionSum;%解空间(解集合)中可能解的总数
binSolutionN=dec2bin(solutionN);%把可能解的总数转换成二进制数
chromosomeLength=size(binSolutionN,2);%由解空间中可能解的总数(二进制数)计算染色体的长度

%%%%%%%%%%%%%%%%程序初始化
%随机生成初始可能解的顺序号,+1是为了防止出现0顺序号
solutionSequence=fix(rand(chromosomeSum,1)*solutionN)+1;
for i=1:chromosomeSum%防止解的顺序号超出解的个数
if solutionSequence(i)>solutionN;
solutionSequence(i)=solutionN;
end
end
%染色体是解集合中的序号,它对应一个可能解
%把解的十进制序号转成二进制序号
fatherChromosomeGroup=dec2bin(solutionSequence,chromosomeLength);
holdLeastFunctionError=Inf;%可能解的最小误差的初值
holdBestChromosome=0;%对应最小误差的染色体的初值

%%%%%%%%%%%%%%%%%%开始计算
compute=1;
circle=0;
while compute%开始迭代求解
%%%%%%%%%%%%%1:由可能解的序号寻找解本身(关键步骤)
x=chromosome_x(fatherChromosomeGroup,oneDimensionSet,solutionSum);
%%%%%%%%%%%%%2：把解代入非线性方程计算误差
functionError=nonLinearSumError1(x);%把解代入方程计算误差
[solution,minError,isTrue]=isSolution(x,functionError,solutionSumError);
%isSolution函数根据误差functionError判定方程是否已经解开，isTrue=1,方程得解。solution是方程的解
if isTrue==1
'方程得解'
solution
minError
return%结束程序
end
%%%%%%%%%%%%%3：选择最好解对应的最优染色体
[bestChromosome,leastFunctionError]=best_worstChromosome(fatherChromosomeGroup,functionError);
%%%%%%%%%%%%%4：保留每次迭代产生的最好的染色体
%本次最好解与上次最好解进行比较，如果上次最好解优于本次最好解，保留上次最好解；
%反之，保留本次最好解。保留的最好染色体放在holdBestChromosome中
[holdBestChromosome,holdLeastFunctionError]...
=compareBestChromosome(holdBestChromosome,holdLeastFunctionError,...
bestChromosome,leastFunctionError);
circle=circle+1
%minError
%solution
holdLeastFunctionError
if circle>circleN
return
end
%%%%%%%%%%%%%%5:把保留的最好的染色体holdBestChromosome加入到染色体群中
order=round(rand(1)*chromosomeSum);
if order==0
order=1;
end
fatherChromosomeGroup(order,:)=holdBestChromosome;
functionError(order)=holdLeastFunctionError;

%%%%%%%%%%%%%%%6:为每一条染色体(即可能解的序号)定义一个概率(关键步骤)
%%%%%%%%%%%%%%%好的染色体概率高，坏的概率低。依据误差functionError计算概率
[p,trueP]=chromosomeProbability(functionError);
if trueP =='Fail'
'可能解严重不适应方程，请重新开始'
return%结束程序
end
%%%%%%%%%%%%%%%7：按照概率筛选染色体(关键步骤)
%fa=bin2dec(fatherChromosomeGroup)%显示父染色体
%从父染体中选择优秀染色体
%selecteChromosomeGroup=selecteChromosome(fatherChromosomeGroup,p);
%%%%%%%%%%%%%%%8：染色体杂交(关键步骤)
%sle=bin2dec(selecteChromosomeGroup)%显示选择出来的解的序号(染色体)
%用概率筛选出的染色体selecteChromosomeGroup进行杂交，产生子代染色体
%sonChromosomeGroup=crossChromosome(selecteChromosomeGroup,2);
%不用概率筛选出的染色体selecteChromosomeGroup进行杂交，而直接用上一代(父代)的
sonChromosomeGroup=crossChromosome(fatherChromosomeGroup,2);
%sonChromosomeGroup=immunity(fatherChromosomeGroup,holdBestChromosome,3);
%把疫苗接种到其它染色体中
sonChromosomeGroup=immunity(sonChromosomeGroup,holdBestChromosome,3);
%cro=bin2dec(sonChromosomeGroup)%显示杂交后的子代染色体
sonChromosomeGroup=checkSequence(sonChromosomeGroup,solutionN);%检查杂交后的染色体是否越界
%%%%%%%%%%%%%%%9：变异
%不杂交直接变异
%fatherChromosomeGroup=varianceCh(fatherChromosomeGroup,0.1,solutionN);
%杂交后变异
fatherChromosomeGroup=varianceCh(sonChromosomeGroup,0.5,solutionN);
fatherChromosomeGroup=checkSequence(fatherChromosomeGroup,solutionN);%检查变异后的染色体是否越界
end

　

接种疫苗函数，这是和遗传算法唯一不同的函数，可以用它代替染色体的交叉操作。

%chromosomeGroup:染色体组
%bachterinChromosome:疫苗染色体，即最好的染色体。从这个染色体上取疫苗
%parameter:接种疫苗的参数，即用什么方法接种
%inoculateChromosome:接种疫苗后的染色体
function inoculateChromosome=immunity(chromosomeGroup,bacterinChromosome,parameter)
[chromosomeGroupSum,chromosomeLength]=size(chromosomeGroup);
[row,bacterinChromosomeLength]=size(bacterinChromosome);
%chromosomeGroupSum:染色体的条数；chromosomeLength：染色体的长度
switch parameter
case 1%随机选择染色体进行接种
for i=1:chromosomeGroupSum
%%%%%%%%%%%%从疫苗染色体上定位疫苗
headDot=fix(rand(1)*bacterinChromosomeLength);
%疫苗在染色体上左边的点位
if headDot==0%防止出现0点位
headDot=1;
end
tailDot=fix(rand(1)*bacterinChromosomeLength);
%疫苗在染色体上右边的点位
if tailDot==0%防止出现0点位
tailDot=1;
end
if tailDot>headDot%防止右边的点位大于左边的点位
dot=headDot;
headDot=tailDot;
tailDot=dot;
end
%%%%%%%%%%%%%接种
randChromosomeSequence=round(rand(1)*chromosomeGroupSum);
%随机产生1条染色体的序号，对这条染色体进行接种
if randChromosomeSequence==0%防止产生0序号
randChromosomeSequence=1;
end
inoculateChromosome(i,:)...%先把输入染色体传给输出
=chromosomeGroup(randChromosomeSequence,:);
%执行免疫，即从疫苗染色体上取出一段基因做疫苗，再注入到其它染色体中
inoculateChromosome(i,headDot:tailDot)...
=bacterinChromosome(1,headDot:tailDot);
end
case 2 %所有染色体挨个接种
for i=1:chromosomeGroupSum
%%%%%%%%%%%%从疫苗染色体上定位疫苗
headDot=fix(rand(1)*bacterinChromosomeLength);
%疫苗在染色体上左边的点位
if headDot==0%防止出现0点位
headDot=1;
end
tailDot=fix(rand(1)*bacterinChromosomeLength);
%疫苗在染色体上右边的点位
if tailDot==0%防止出现0点位
tailDot=1;
end
if tailDot>headDot%防止右边的点位大于左边的点位
dot=headDot;
headDot=tailDot;
tailDot=dot;
end
%%%%%%%%%%%%%接种
inoculateChromosome(i,:)=chromosomeGroup(i,:);%先把输入染色体传给输出
%执行免疫，即从疫苗染色体上取出一段基因做疫苗，再注入到其它染色体中
inoculateChromosome(i,headDot:tailDot)...
=bacterinChromosome(1,headDot:tailDot);
end
case 3 %接种位置是随机的
for i=1:chromosomeGroupSum
%%%%%%%%%%%%从疫苗染色体上定位疫苗
headDot=fix(rand(1)*bacterinChromosomeLength);
%疫苗在染色体上左边的点位
if headDot==0%防止出现0点位
headDot=1;
end
tailDot=fix(rand(1)*bacterinChromosomeLength);
%疫苗在染色体上右边的点位
if tailDot==0%防止出现0点位
tailDot=1;
end
if tailDot>headDot%防止右边的点位大于左边的点位
dot=headDot;
headDot=tailDot;
tailDot=dot;
end
%%%%%%%%%%%%%在染色体上随机定位接种位置
inoculateDot=fix(rand(1)*chromosomeLength);%随机选择染色体的接种点位
if inoculateDot==0
inoculateDot=1;
inoculateChromosome(i,:)=chromosomeGroup(i,:);
inoculateChromosome(i,inoculateDot:tailDot-headDot+1)...
=bacterinChromosome(1,headDot:tailDot);
elseif inoculateDot<=headDot
inoculateChromosome(i,:)=chromosomeGroup(i,:);
inoculateChromosome(i,inoculateDot:inoculateDot+tailDot-headDot)...
=bacterinChromosome(1,headDot:tailDot);
elseif (chromosomeLength-inoculateDot)>=(tailDot-headDot)
inoculateChromosome(i,:)=chromosomeGroup(i,:);
inoculateChromosome(i,inoculateDot:inoculateDot+tailDot-headDot)...
=bacterinChromosome(1,headDot:tailDot);
else
inoculateChromosome(i,:)=chromosomeGroup(i,:);
inoculateChromosome(i,headDot:tailDot)...
=bacterinChromosome(1,headDot:tailDot);
end
end

 
````

</details>

#### B2F · MATLAB · bad674e9

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`caea6aa308c917bc76e4d3980872e51b48889a0d128b746fe638d85f752e5ef7`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/B2F.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/B2F.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/de2bi.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/de2bi.m`

<details>
<summary>展开原始代码</summary>

````matlab
function  [B,len,v]=B2F(sol,bounds)
%[B,len]=B2F(x,bounds)    二进制编码函数
%x                        编码向量如x=[6 8 9];
%bounds                   边界约束ru如bounds=[4 8 ;3  11;6  12;];
%B                        二进制编码串
%编码长度L由bounds(2)-bounds(1)决定
%以上为例:
%     编码长度向量L=[4 8 6]编成二进制L=[11 1000 110],则len=[2 4 3]
%     计算B=x-bound(1)=[2 5 3]编成二进制 B=[10 0101 011]
%           作者：机自01-2班曾新海
%           zxh21st@163.com
n=length(sol);
len=[];B=[];v=[];
L=bounds(:,2)-bounds(:,1);
L=de2bi(L);
for i=1:n
len(i)=length(L(i,:));
end
v=sol-bounds(:,1)';
for i=1:n
    B=[B de2bi(v(i),len(i))];
end
````

</details>

#### F2B · MATLAB · 4a159133

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a654ccb2ce5b7741bacf18e5a16ae600391206a70d4f5bb6daebdbb2ed3030ef`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/F2B.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/F2B.m`

<details>
<summary>展开原始代码</summary>

````matlab
function  [pops,len]=F2B(x,bounds,len)
%二进制编码转化为十进制
%[pops]=F2B(x,bounds,len)
%x       二进制串如x=[0 1 1  0 0 1 0  1 0 1 0 1]
%len     二进制串的分段len=[3  4  5]
%bounds  边界约束
%pops    十进制
%           作者：机自01-2班曾新海
%           zxh21st@163.com
n=length(x);
m=length(len);
q=[];
for i=1:m
q(i)=sum(len(1:i));
end
q=[0 q];
for j=1:m
    pops(j)=bounds(j,1);
    p=[];
    p=x(q(j)+1:q(j+1));
    L1=q(j+1)-q(j);
    for k=1:L1
        pops(j)=pops(j)+p(k)*2^(k-1);
    end
end

    
````

</details>

#### INTinti · MATLAB · 0f98dcab

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`86e35ec011f252b6ca717adb34969009a3ebc0aceb4c9c4c24b22724a000e949`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/INTinti.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/INTinti.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/myfun.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/myfun.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [pop]=INTinti(num,bounds)
%[pop]=INTinti(num,bounds)
%inti     编码函数
%num      种群数
%bounds   边界约束
%           作者：机自01-2班曾新海
%           zxh21st@163.com
n=size(bounds,1);
L=bounds(:,2)-bounds(:,1);
p=rand(num,n);
for i=1:num
    p(i,:)=round(p(i,:).*L');
    pop(i,:)= p(i,:)+bounds(:,1)';
    f(i)=myfun(pop(i,:));
end
pop=[pop f'];
````

</details>

#### changes · MATLAB · 7affa690

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`6131cf2e58e7b2cd7e9544b4bf335f9125fc89508b6b115d574e43c2a6e1a1d3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/changes.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/changes.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/B2F.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/F2B.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/B2F.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/F2B.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [pops]=changes(cpop,bounds,len,p)
%基因突变函数
%function [pops]=changes(pop,bounds,len,p)
%pop        种群数目
%bounds     边界约束
%len        每个变量的编码长度
%           如len为[4 3 3];表示有三个变量，第一个变量的二进制编码长度为4,依次类推
%p          突变概率
%pops       返回突变后的基因
%p1         基因突变数目
%           作者：机自01-2班曾新海
%           zxh21st@163.com
if isempty(p)
    p=0.01;
end
[n,m]=size(cpop);
pop=cpop;
p1=round(sum(len)*n*p);
k=0;q=[];v=[];
while(k<p1)
    k=k+1;
    q(k)=round(rand*(sum(len)*n-1))+1;
    for i=1:k-1
        if q(k)==q(i)
            q(k)=[];
            k=k-1;
        end
    end
end

for i=1:n
[B(i,:),len]=B2F(pop(i,:),bounds);
end

v=reshape(B,1,n*sum(len));

for i=1:p1
    if v(q(i))==0
        v(q(i))=1;
    else
        v(q(i))=0;
    end
end
v=reshape(v,n,sum(len));
for i=1:n
   pop(i,:)=F2B(v(i,:),bounds,len);
end
pops=pop
cpop
````

</details>

#### cross · MATLAB · 9365180b

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；含随机过程但未发现固定随机种子。

- SHA-256：`8eddbc1746d3ce06c04e4f33f27630936f1363ff0bd4e46b9e4728f0d6a4ef96`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/cross.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/cross.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/B2F.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/F2B.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/B2F.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/F2B.m`

<details>
<summary>展开原始代码</summary>

````matlab
function  [cpop ,len,v]=cross(child,bounds,CP)
%交叉函数，采取点交叉
%[newpop ,len]=cross(child,bounds,CP)
%child      复制后的种群
%bounds     边界约束
%CP         交叉概率
%newpop     交叉后的新种群
%len        每个变量的编码长度
%           如len返回为[4 3 3];表示有三个变量，第一个变量的二进制编码长度为4,依次类推
%           作者：机自01-2班曾新海
%           zxh21st@163.com
if isempty(CP)
    CP=0.25;
end
[n ,m]=size(child);
B=[];len=[];t=[];
mychild=child(:,1:end-1);
v=[];
p=rand(1,n);
k=1;
    for i=1:n
        if p(i)<CP
            v(k)=i;
            k=k+1;
        end
    end
    if (rem(k,2)==0)
        temp=v(k-1);
        while (temp==v(k-1))
        temp=round(rand*(n-1))+1;
    end
    v(k)=temp;
    k=k+1;
   end 
if isempty(v)
    [B(i,:),len]=B2F(mychild(1,:),bounds);
    B=[];
else
    for i=1:k-1
[B(i,:),len]=B2F(mychild(v(i),:),bounds);
end
for i=1:2:k-2
    p2=round(rand*sum(len)-1)+1;
    t=zeros(1,p2);
    t(i,:)=B(i,1:p2);
    B(i,1:p2)=B(i+1,1:p2);
    B(i+1,1:p2)=t(i,:);
end
for i=1:k-1
   mychild(v(i),:)=F2B(B(i,:),bounds,len);
end
end
cpop=mychild;
````

</details>

#### de2bi · MATLAB · 60460ad9

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `de2bi`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4f30725723950ae1bdcef724606abbee72b698362ef807e41355418a50fe37e9`
- 语言：MATLAB
- 符号：`de2bi`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/de2bi.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/de2bi.m`

<details>
<summary>展开原始代码</summary>

````matlab
function b = de2bi(d, n, p)
%function b = de2bi(d, n, p)
%DE2BI  转换10进制数为二进制数。
%        B = DE2BI(D) 转换正整数向量D成二进制矩阵B。
%        二进制矩阵B的每一行表示十进制向量D中相应的数。
%       B = DE2BI(D, N) 转换正整数向量D成二进制矩阵B，
%        但指定B的列数为N。
%       B = DE2BI(D, N, P) 转换正整数向量D成p进制矩阵B。
%      p进制矩阵B的每一行表示十进制向量D中相应的数。
%           作者：机自01-2班曾新海
%           zxh21st@163.com
d = d(:);len_d = length(d);
if min(d) < 0, error('Cannot convert a negative number');
elseif ~isempty(find(d==inf)),
     error('Input must not be Inf.');
elseif find(d ~= floor(d)), 
    error('Input must be an integer.');  
end;
if nargin < 2,
   tmp = max(d); b1 = [];
   while tmp > 0
      b1 = [b1 rem(tmp, 2)];tmp = floor(tmp/2);
   end;
   n = length(b1);
end;
if nargin < 3,p = 2;end;
b = zeros(len_d, n);
for i = 1 : len_d
   j = 1;tmp = d(i);
   while (j <= n) & (tmp > 0)
      b(i, j) = rem(tmp, p);tmp = floor(tmp/p);
      j = j + 1;
end;end;
````

</details>

#### f553 · MATLAB · 1dca28a5

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c3efd92dd04b3ec59c80ec94d94e6296dc2f327da97efc9df149e05e76ed1658`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/f553.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/f553.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [sol,eval]=f553(sol,options)
m(1)=sol(1);
m(2)=sol(2);
m(3)=sol(3);
%失效概率矩阵
q=[0.01 0.05 0.10 0.18;
0.08 0.02 0.15 0.12;
0.04 0.05 0.20 0.10];
%约束条件
g1=51-(m(1)+3).^2+m(2).^2+m(3).^2;
g2=20*sum(m+exp(-m))-120;
g3=20*sum(m.*exp(-m/4))-65;
%计算加惩罚项的适值
if ((g1>=0)&(g2>=0)&(g3>=0))
  multi=1;
  for i=1:3
     summ=0;
     for j=2:4
        summ=summ+q(i,j).^(m(i)+1);
     end      
     multi=multi*(1-(1-(1-q(i,1)).^(m(i)+1))-summ);
  end
  eval=multi;
else
%取M=500
  eval=-500;
end
````

</details>

#### ga · MATLAB · 9be9175b

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`63c2ae74e4a035bbec682e2c8ef9d6b7cb3481ecd2713f56cc86dc7b6e5e8f37`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/ga.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/ga.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/INTinti.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/changes.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/cross.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/mutation.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/myfun.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/myga.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/INTinti.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/changes.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/cross.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/mutation.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/myfun.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/myga.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [f,x]=myga(num,bounds,Myfun,N,CP,P)
%[f,x]=ga(num,bounds,fun,N,CP,P)
%该遗传算法适用于：
%           目标函数为求最大值，且解非负整数解
%bounds     边界约束
%Myfun        为目标函数
%num        初始种群数
%N          最大迭代次数
%CP         交叉概率
%P          突变概率
%f          目标最优解
%x          最优解向量
%           作者：机自01-2班曾新海
%           zxh21st@163.com
m=nargin;
if m<6
disp('-_-  错误!')
disp('>> 输入变量太少')
disp('>>  按回车键查看帮助')
    pause
    help ga
    f='-_- ';
    x='没有规矩不成方圆';
    break;
end
pop=INTinti(num,bounds);
fmax=pop(:,end);
endpop=pop;
n=size(endpop,2);
k=0;x=[];f=zeros(1,num);
while(k<N)
    pop=mutation(endpop);
    [cpop ,len,v]=cross(pop,bounds,CP);
    [pops]=changes(cpop,bounds,len,P);break;
    for i=1:num
        sol=pops(i,:);
        [f(i)]=Myfun(sol);
        if fmax(i)<f(i)
            fmax(i)=f(i);
            endpop(i,1:end-1)=pops(i,:);
        end
end
endpop(:,end)=fmax(:);
k=k+1;
end
[f,ii]=max(fmax);
x=endpop(ii,1:end-1);
````

</details>

#### gaDemo1Eeval · MATLAB · 7f243f21

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`82092f0e0f6cd34f61a92150513e4c7826f922afcb9cd933ad587ca2cac7106e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/gaDemo1Eeval.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/gaDemo1Eeval.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [sol, eval] =gaDemo1Eeval(sol,options)
x=sol(1);
eval = x + 10*sin(5*x)+7*cos(4*x);

%参数说明
%eval：个体的适应度； 
%sol：当前个体，n+1个元素的行向量。
````

</details>

#### mutation · MATLAB · 7d44343d

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`8b1dcac14752d20cfa8a63de5d92b869f5efd00cb7650bbb9cce458a603a390a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/mutation.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/mutation.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [child]=mutation(pop)
%复制函数，采取小盘轮转法
%[child]=mutation(pop)
%mutation    编码
%pop         初始种群
%child       返回复制后的种群
%pop(:,end)  适值度
%           作者：机自01-2班曾新海
%           zxh21st@163.com
[n,m]=size(pop);
f=pop(:,end);
value=sum(f);
for i=1:n
    p(i)=f(i)/value;
    q(i)=sum(p(1:i));
end
    t=rand(1,n);
for j=1:n
    for k=1:n
        if t(j)<q(k)
            v(j)=k;
            break
        end
    end
end
    i=1:n;
    child(i,:)=pop(v(i),:);
````

</details>

#### myfun · MATLAB · 6e48dd7e

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b1855695ae6d222117e6b1937ef2063bbcdbb87810659120e19177ed1da2ed9c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/myfun.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/myfun.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [f]=myfun(sol,bnd)
%           作者：机自01-2班曾新海
%           zxh21st@163.com
x=sol;
n=length(x);
f=0;
for i=1:n
    f=f+x(i)*i;
end
````

</details>

#### myga · MATLAB · 1a8651a0

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`e81f0d48d2000673960cd2f40e86e892a8cab20282d90de7bc0ae7280a0552b2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/myga.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/myga.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/INTinti.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/changes.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/cross.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/ga.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/mutation.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/myfun.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/INTinti.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/changes.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/cross.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/ga.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/mutation.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/myfun.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [f,x]=myga(num,bounds,N,CP,P)
%[f,x]=ga(num,bounds,fun,N,CP,P) 
%[f,x]=myga([],bounds,[],[],[])
%该遗传算法适用于：
%           目标函数为求最大值，且解非负整数解
%bounds     边界约束
%Myfun      为目标函数
%num        初始种群数
%N          最大迭代次数
%CP         交叉概率
%P          突变概率
%f          目标最优解
%x          最优解向量
%           作者：机自01-2班曾新海
%           zxh21st@163.com
m=nargin;
if m<5
disp('-_-  错误!')
disp('>> 输入变量太少')
disp('>>  按回车键查看帮助')
    pause
    help ga
    f='-_- ';
    x='没有规矩不成方圆';
    break;
end
if isempty(CP)
    CP=0.25;
end
if isempty(P)
    P=0.01;
end
if isempty(N)
    N=1000;
end
if any(bounds(:,1))<0
    disp('-_-  错误!')
disp('>>  按回车键查看帮助')
    pause
    help ga
    f='-_- ';
    x='没有规矩不成方圆';
    break;
end
if isempty(num)
    num=100;
end
pop=INTinti(num,bounds);
fmax=pop(:,end);
endpop=pop;
n=size(endpop,2);
count=0;x=[];f=zeros(1,num);
while(count<N)
    pop=mutation(endpop);
    [cpop ,len,v]=cross(pop,bounds,CP);
    [pops]=changes(cpop,bounds,len,P);
    for i=1:num
        sol=pops(i,:);
    [f(i)]=Myfun(sol);
    %惩罚策略
for jj=1:length(sol)
    if sol(jj)<bounds(jj,1)
        f(i)=-inf;
    end
    if sol(jj)>bounds(jj,2)
        f(i)=-inf;
    end
end
            if fmax(i)<f(i)
            fmax(i)=f(i);
            endpop(i,1:end-1)=pops(i,:);
        end
end
endpop(:,end)=fmax(:);
count=count+1;

% [f,ii]=max(fmax);
% x=endpop(ii,1:end-1);
end
[f,ii]=max(fmax);
x=endpop(ii,1:end-1);
````

</details>

#### xcross · MATLAB · 469d3251

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`2ec2484033d8e1167922fbb2b1b9f7c57f2c16034f64f52652be91c9cd4cec84`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/xcross.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/xcross.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/用MATLAB实现遗传算法程序/B2F.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/与已有的相同/B2F.m`

<details>
<summary>展开原始代码</summary>

````matlab
function  [newpop ,len]=xcross(child,bounds,CP)
 mychild=child(:,1:end-1);
[B(1,:),len]=B2F(mychild(1,:),bounds);
newpop=B(1,:);
````

</details>

#### 源程序 · MATLAB · 66675fde

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`ebef31117ca693ca11f54353e194f7b8ee0b2c82fe8ce422d96ddfa3f65c1127`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/源程序.txt`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/源程序.txt`

<details>
<summary>展开原始代码</summary>

````matlab
TSP问题的遗传算法+转载

我这几天做了一个队员选择问题，其中一个问题我是用遗传算法做的，现在我把它整理成解决tsp问题的遗传算法：旅行商问题(traveling saleman problem,简称tsp)：
    已知n个城市之间的相互距离，现有一个推销员必须遍访这n个城市，并且每个城市只能访问一次，最后又必须返回出发城市。如何安排他对这些城市的访问次序，可使其旅行路线的总长度最短？
    用图论的术语来说，假设有一个图g=(v,e)，其中v是顶点集，e是边集，设d=(dij)是由顶点i和顶点j之间的距离所组成的距离矩阵，旅行商问题就是求出一条通过所有顶点且每个顶点只通过一次的具有最短距离的回路。
    这个问题可分为对称旅行商问题(dij=dji,,任意i,j=1,2,3，…,n)和非对称旅行商问题(dij≠dji,,任意i,j=1,2,3，…,n)。
    若对于城市v={v1,v2,v3,…,vn}的一个访问顺序为t=(t1,t2,t3,…,ti,…,tn),其中ti∈v(i=1,2,3,…,n)，且记tn+1= t1，则旅行商问题的数学模型为：
     min     l=σd(t(i),t(i+1))  （i=1,…,n）
    旅行商问题是一个典型的组合优化问题，并且是一个np难问题，其可能的路径数目与城市数目n是成指数型增长的，所以一般很难精确地求出其最优解，本文采用遗传算法求其近似解。
    遗传算法：
初始化过程：用v1,v2,v3,…,vn代表所选n个城市。定义整数pop-size作为染色体的个数，并且随机产生pop-size个初始染色体，每个染色体为1到18的整数组成的随机序列。
适应度f的计算：对种群中的每个染色体vi，计算其适应度，f=σd(t(i),t(i+1)).
评价函数eval(vi)：用来对种群中的每个染色体vi设定一个概率，以使该染色体被选中的可能性与其种群中其它染色体的适应性成比例，既通过轮盘赌，适应性强的染色体被选择产生后台的机会要大，设alpha∈(0,1)，本文定义基于序的评价函数为eval(vi)=alpha*(1-alpha).^(i-1) 。[随机规划与模糊规划]
选择过程：选择过程是以旋转赌轮pop-size次为基础，每次旋转都为新的种群选择一个染色体。赌轮是按每个染色体的适应度进行选择染色体的。
   step1 、对每个染色体vi,计算累计概率qi，q0=0;qi=σeval(vj)   j=1,…,i;i=1,…pop-size.
   step2、从区间(0,pop-size)中产生一个随机数r；
   step3、若qi-1<r<qi,则选择第i个染色体 ；
   step4、重复step2和step3共pop-size次，这样可以得到pop-size个复制的染色体。
grefenstette编码：由于常规的交叉运算和变异运算会使种群中产生一些无实际意义的染色体，本文采用grefenstette编码《遗传算法原理及应用》可以避免这种情况的出现。所谓的grefenstette编码就是用所选队员在未选（不含淘汰）队员中的位置，如：
          8 15 2 16 10 7 4 3 11 14 6 12 9 5 18 13 17 1
          对应：
          8 14 2 13 8 6 3 2 5 7 3 4 3 2 4 2 2 1。
交叉过程：本文采用常规单点交叉。为确定交叉操作的父代，从 到pop-size重复以下过程：从[0，1]中产生一个随机数r，如果r<pc ，则选择vi作为一个父代。
           将所选的父代两两组队，随机产生一个位置进行交叉，如：
          8 14 2 13 8 6 3 2 5 7 3 4 3 2 4 2 2 1
          6 12 3 5 6 8 5 6 3 1 8 5 6 3 3 2 1 1
交叉后为：
         8 14 2 13 8 6 3 2 5 1 8 5 6 3 3 2 1 1
         6 12 3 5 6 8 5 6 3 7 3 4 3 2 4 2 2 1
变异过程：本文采用均匀多点变异。类似交叉操作中选择父代的过程，在r<pm 的标准下选择多个染色体vi作为父代。对每一个选择的父代，随机选择多个位置，使其在每位置按均匀变异（该变异点xk的取值范围为[ukmin,ukmax],产生一个[0，1]中随机数r，该点变异为x'k=ukmin+r(ukmax-ukmin)）操作。如：
         8 14 2 13 8 6 3 2 5 7 3 4 3 2 4 2 2 1
      变异后：
        8 14 2 13 10 6 3 2 2 7 3 4 5 2 4 1 2 1
反grefenstette编码：交叉和变异都是在grefenstette编码之后进行的，为了循环操作和返回最终结果，必须逆grefenstette编码过程，将编码恢复到自然编码。
循环操作：判断是否满足设定的带数xzome，否，则跳入适应度f的计算；是，结束遗传操作，跳出。


function [bestpop,trace]=ga(d,termops,num,pc,cxops,pm,alpha)
%
%————————————————————————
%[bestpop,trace]=ga(d,termops,num,pc,cxops,pm,alpha)
%d:距离矩阵
%termops:种群带数
%num:每带染色体的个数
%pc:交叉概率
%cxops:由于本程序采用单点交叉，交叉点的设置在本程序中没有很好的解决，所以本文了采用定点，即第cxops，可以随机产生。
%pm:变异概率
%alpha:评价函数eval(vi)=alpha*(1-alpha).^(i-1).
%bestpop:返回的最优种群
%trace:进化轨迹
%------------------------------------------------
%####@@@##版权所有！欢迎广大网友改正，改进！##@@@####
%e-mail:tobysidney33@sohu.com
%####################################################
%
citynum=size(d,2);
n=nargin;
if n<2
    disp('缺少变量！！')
    disp('^_^开个玩笑^_^')
end
if n<2
    termops=500;
    num=50;
    pc=0.25;
    cxops=3;
    pm=0.30;
    alpha=0.10;
end
if n<3
    num=50;
    pc=0.25;
    cxops=3;
    pm=0.30;
    alpha=0.10;
end
if n<4
    pc=0.25;
    cxops=3;
    pm=0.30;
    alpha=0.10;
end
if n<5
    cxops=3;
    pm=0.30;
    alpha=0.10;
end
if n<6
    pm=0.30;
    alpha=0.10;
end
if n<7
    alpha=0.10;
end
if isempty(cxops)
    cxops=3;
end

[t]=initializega(num,citynum);
for i=1:termops
[l]=f(d,t);
[x,y]=find(l==max(l));
trace(i)=-l(y(1));
bestpop=t(y(1),:);
[t]=select(t,l,alpha);
[g]=grefenstette(t);
[g1]=crossover(g,pc,cxops);
[g]=mutation(g1,pm);  %均匀变异
[t]=congrefenstette(g);
end

---------------------------------------------------------
function [t]=initializega(num,citynum)
for i=1:num
    t(i,:)=randperm(citynum);
end
-----------------------------------------------------------
function [l]=f(d,t)
[m,n]=size(t);
for k=1:m
    for i=1:n-1
      l(k,i)=d(t(k,i),t(k,i+1));
    end
      l(k,n)=d(t(k,n),t(k,1));
      l(k)=-sum(l(k,:));
end
-----------------------------------------------------------
function [t]=select(t,l,alpha)
[m,n]=size(l);
t1=t;
[beforesort,aftersort1]=sort(l,2);%fsort from l to u
for i=1:n
    aftersort(i)=aftersort1(n+1-i);      %change 
end
for k=1:n;
    t(k,:)=t1(aftersort(k),:);
    l1(k)=l(aftersort(k));
end
t1=t;
l=l1;
for i=1:size(aftersort,2)
    evalv(i)=alpha*(1-alpha).^(i-1);
end
m=size(t,1);
q=cumsum(evalv);
qmax=max(q);
for k=1:m
    r=qmax*rand(1);
    for j=1:m
        if j==1&r<=q(1)
            t(k,:)=t1(1,:);
        elseif j~=1&r>q(j-1)&r<=q(j)
            t(k,:)=t1(j,:);
        end
    end
end
--------------------------------------------------
function [g]=grefenstette(t)
[m,n]=size(t);
for k=1:m
    t0=1:n;
   for i=1:n
       for j=1:length(t0)
           if t(k,i)==t0(j)
              g(k,i)=j;
              t0(j)=[];
              break
           end
       end
    end
end
-------------------------------------------
function [g]=crossover(g,pc,cxops)
[m,n]=size(g);
ran=rand(1,m);
r=cxops;
[x,ru]=find(ran<pc);
if ru>=2
    for k=1:2:length(ru)-1
       g1(ru(k),:)=[g(ru(k),[1:r]),g(ru(k+1),[(r+1):n])];
       g(ru(k+1),:)=[g(ru(k+1),[1:r]),g(ru(k),[(r+1):n])];
       g(ru(k),:)=g1(ru(k),:);
    end
end
--------------------------------------------
function [g]=mutation(g,pm)    %均匀变异
[m,n]=size(g);
ran=rand(1,m);
r=rand(1,3);      %dai gai jin
rr=floor(n*rand(1,3)+1);
[x,mu]=find(ran<pm);
for k=1:length(mu)
    for i=1:length(r)
        umax(i)=n+1-rr(i);
        umin(i)=1;
        g(mu(k),rr(i))=umin(i)+floor((umax(i)-umin(i))*r(i));
    end
end
---------------------------------------------------
function [t]=congrefenstette(g)
[m,n]=size(g);
for k=1:m
    t0=1:n;
   for i=1:n
      t(k,i)=t0(g(k,i));
      t0(g(k,i))=[];
   end
end
````

</details>

#### 遗传算法程序 matlab · MATLAB · d92f31ce

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`5126c26a028c20578f8f37d66349184c4fed80e36ed7770aad75aa6d02d434ea`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/遗传算法程序 matlab.txt`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/遗传算法程序 matlab.txt`

<details>
<summary>展开原始代码</summary>

````matlab
遗传算法程序 matlab
作者：KINGTT  来源：转载  发布时间：2008-7-17 9:10:02
减小字体 增大字体 

本程序收集于网络，本人并未进行过运行，如有问题请与作者联系，如有侵权请告之

遗传算法程序:
   说明: fga.m 为遗传算法的主程序; 采用二进制Gray编码,采用基于轮盘赌法的非线性排名选择, 均匀交叉,变异操作,而且还引入了倒位操作!

function [BestPop,Trace]=fga(FUN,LB,UB,eranum,popsize,pCross,pMutation,pInversion,options)
% [BestPop,Trace]=fmaxga(FUN,LB,UB,eranum,popsize,pcross,pmutation)
% Finds a  maximum of a function of several variables.
% fmaxga solves problems of the form: 
%      max F(X)  subject to:  LB <= X <= UB                           
%  BestPop       - 最优的群体即为最优的染色体群
%  Trace         - 最佳染色体所对应的目标函数值
%  FUN           - 目标函数
%  LB            - 自变量下限
%  UB            - 自变量上限
%  eranum        - 种群的代数,取100--1000(默认200)
%  popsize       - 每一代种群的规模；此可取50--200(默认100)
%  pcross        - 交叉概率,一般取0.5--0.85之间较好(默认0.8)
%  pmutation     - 初始变异概率,一般取0.05-0.2之间较好(默认0.1)
%  pInversion    - 倒位概率,一般取0.05－0.3之间较好(默认0.2)
%  options       - 1*2矩阵,options(1)=0二进制编码(默认0),option(1)~=0十进制编
%码,option(2)设定求解精度(默认1e-4)
%
%  ------------------------------------------------------------------------

T1=clock;
if nargin<3, error('FMAXGA requires at least three input arguments'); end
if nargin==3, eranum=200;popsize=100;pCross=0.8;pMutation=0.1;pInversion=0.15;options=[0 1e-4];end
if nargin==4, popsize=100;pCross=0.8;pMutation=0.1;pInversion=0.15;options=[0 1e-4];end
if nargin==5, pCross=0.8;pMutation=0.1;pInversion=0.15;options=[0 1e-4];end
if nargin==6, pMutation=0.1;pInversion=0.15;options=[0 1e-4];end
if nargin==7, pInversion=0.15;options=[0 1e-4];end
if find((LB-UB)>0)
   error('数据输入错误,请重新输入(LB<UB):');
end
s=sprintf('程序运行需要约%.4f 秒钟时间,请稍等......',(eranum*popsize/1000));
disp(s);

global m n NewPop children1 children2 VarNum

bounds=[LB;UB]';bits=[];VarNum=size(bounds,1);
precision=options(2);%由求解精度确定二进制编码长度
bits=ceil(log2((bounds(:,2)-bounds(:,1))' ./ precision));%由设定精度划分区间
[Pop]=InitPopGray(popsize,bits);%初始化种群
[m,n]=size(Pop);
NewPop=zeros(m,n);
children1=zeros(1,n);
children2=zeros(1,n);
pm0=pMutation;
BestPop=zeros(eranum,n);%分配初始解空间BestPop,Trace
Trace=zeros(eranum,length(bits)+1);
i=1;
while i<=eranum
    for j=1:m
        value(j)=feval(FUN(1,:),(b2f(Pop(j,:),bounds,bits)));%计算适应度
    end
    [MaxValue,Index]=max(value);
    BestPop(i,:)=Pop(Index,:);
    Trace(i,1)=MaxValue;
    Trace(i,(2:length(bits)+1))=b2f(BestPop(i,:),bounds,bits);
    [selectpop]=NonlinearRankSelect(FUN,Pop,bounds,bits);%非线性排名选择
[CrossOverPop]=CrossOver(selectpop,pCross,round(unidrnd(eranum-i)/eranum));
%采用多点交叉和均匀交叉，且逐步增大均匀交叉的概率
    %round(unidrnd(eranum-i)/eranum)
    [MutationPop]=Mutation(CrossOverPop,pMutation,VarNum);%变异
    [InversionPop]=Inversion(MutationPop,pInversion);%倒位
    Pop=InversionPop;%更新
pMutation=pm0+(i^4)*(pCross/3-pm0)/(eranum^4);
%随着种群向前进化，逐步增大变异率至1/2交叉率
    p(i)=pMutation;
    i=i+1;
end
t=1:eranum;
plot(t,Trace(:,1)');
title('函数优化的遗传算法');xlabel('进化世代数(eranum)');ylabel('每一代最优适应度(maxfitness)');
[MaxFval,I]=max(Trace(:,1));
X=Trace(I,(2:length(bits)+1));
hold on;  plot(I,MaxFval,'*');
text(I+5,MaxFval,['FMAX=' num2str(MaxFval)]);
str1=sprintf('进化到 %d 代 ,自变量为 %s 时,得本次求解的最优值 %f\n对应染色体是：%s',I,num2str(X),MaxFval,num2str(BestPop(I,:)));
disp(str1);
%figure(2);plot(t,p);%绘制变异值增大过程
T2=clock;
elapsed_time=T2-T1;
if elapsed_time(6)<0
    elapsed_time(6)=elapsed_time(6)+60; elapsed_time(5)=elapsed_time(5)-1;
end
if elapsed_time(5)<0
    elapsed_time(5)=elapsed_time(5)+60;elapsed_time(4)=elapsed_time(4)-1;
end  %像这种程序当然不考虑运行上小时啦
str2=sprintf('程序运行耗时 %d 小时 %d 分钟 %.4f 秒',elapsed_time(4),elapsed_time(5),elapsed_time(6));
disp(str2);

 

%初始化种群
%采用二进制Gray编码,其目的是为了克服二进制编码的Hamming悬崖缺点
function [initpop]=InitPopGray(popsize,bits)
len=sum(bits);
initpop=zeros(popsize,len);%The whole zero encoding individual
for i=2:popsize-1
    pop=round(rand(1,len));
    pop=mod(([0 pop]+[pop 0]),2);
    %i=1时,b(1)=a(1);i>1时,b(i)=mod(a(i-1)+a(i),2)
    %其中原二进制串:a(1)a(2)...a(n),Gray串:b(1)b(2)...b(n)
    initpop(i,:)=pop(1:end-1);
end
initpop(popsize,:)=ones(1,len);%The whole one encoding individual


 

%解码

function [fval] = b2f(bval,bounds,bits)
% fval   - 表征各变量的十进制数
% bval   - 表征各变量的二进制编码串
% bounds - 各变量的取值范围
% bits   - 各变量的二进制编码长度
scale=(bounds(:,2)-bounds(:,1))'./(2.^bits-1); %The range of the variables
numV=size(bounds,1);
cs=[0 cumsum(bits)];
for i=1:numV
  a=bval((cs(i)+1):cs(i+1));
  fval(i)=sum(2.^(size(a,2)-1:-1:0).*a)*scale(i)+bounds(i,1);
end


 

%选择操作
%采用基于轮盘赌法的非线性排名选择
%各个体成员按适应值从大到小分配选择概率：
%P(i)=(q/1-(1-q)^n)*(1-q)^i,  其中 P(0)>P(1)>...>P(n), sum(P(i))=1

function [selectpop]=NonlinearRankSelect(FUN,pop,bounds,bits)
global m n
selectpop=zeros(m,n);
fit=zeros(m,1);
for i=1:m
    fit(i)=feval(FUN(1,:),(b2f(pop(i,:),bounds,bits)));%以函数值为适应值做排名依据
end
selectprob=fit/sum(fit);%计算各个体相对适应度(0,1)
q=max(selectprob);%选择最优的概率
x=zeros(m,2);
x(:,1)=[m:-1:1]';
[y x(:,2)]=sort(selectprob);
r=q/(1-(1-q)^m);%标准分布基值
newfit(x(:,2))=r*(1-q).^(x(:,1)-1);%生成选择概率
newfit=cumsum(newfit);%计算各选择概率之和
rNums=sort(rand(m,1));
fitIn=1;newIn=1;
while newIn<=m
    if rNums(newIn)<newfit(fitIn)
        selectpop(newIn,:)=pop(fitIn,:);
        newIn=newIn+1;
    else
        fitIn=fitIn+1;
    end
end


 

%交叉操作
function [NewPop]=CrossOver(OldPop,pCross,opts)
%OldPop为父代种群，pcross为交叉概率
global m n NewPop
r=rand(1,m);
y1=find(r<pCross);
y2=find(r>=pCross);
len=length(y1);
if len>2&mod(len,2)==1%如果用来进行交叉的染色体的条数为奇数，将其调整为偶数
    y2(length(y2)+1)=y1(len);
    y1(len)=[];
end
if length(y1)>=2
   for i=0:2:length(y1)-2
       if opts==0
           [NewPop(y1(i+1),:),NewPop(y1(i+2),:)]=EqualCrossOver(OldPop(y1(i+1),:),OldPop(y1(i+2),:));
       else
           [NewPop(y1(i+1),:),NewPop(y1(i+2),:)]=MultiPointCross(OldPop(y1(i+1),:),OldPop(y1(i+2),:));
       end
   end    
end
NewPop(y2,:)=OldPop(y2,:);

%采用均匀交叉
function [children1,children2]=EqualCrossOver(parent1,parent2)

global n children1 children2
hidecode=round(rand(1,n));%随机生成掩码
crossposition=find(hidecode==1);
holdposition=find(hidecode==0);
children1(crossposition)=parent1(crossposition);%掩码为1，父1为子1提供基因
children1(holdposition)=parent2(holdposition);%掩码为0，父2为子1提供基因
children2(crossposition)=parent2(crossposition);%掩码为1，父2为子2提供基因
children2(holdposition)=parent1(holdposition);%掩码为0，父1为子2提供基因

%采用多点交叉，交叉点数由变量数决定

function [Children1,Children2]=MultiPointCross(Parent1,Parent2)

global n Children1 Children2 VarNum
Children1=Parent1;
Children2=Parent2;
Points=sort(unidrnd(n,1,2*VarNum));
for i=1:VarNum
    Children1(Points(2*i-1):Points(2*i))=Parent2(Points(2*i-1):Points(2*i));
    Children2(Points(2*i-1):Points(2*i))=Parent1(Points(2*i-1):Points(2*i));
end


 

%变异操作
function [NewPop]=Mutation(OldPop,pMutation,VarNum)

global m n NewPop
r=rand(1,m);
position=find(r<=pMutation);
len=length(position);
if len>=1
   for i=1:len
       k=unidrnd(n,1,VarNum); %设置变异点数，一般设置1点
       for j=1:length(k)
           if OldPop(position(i),k(j))==1
              OldPop(position(i),k(j))=0;
           else
              OldPop(position(i),k(j))=1;
           end
       end
   end
end
NewPop=OldPop;


 

%倒位操作

function [NewPop]=Inversion(OldPop,pInversion)

global m n NewPop
NewPop=OldPop;
r=rand(1,m);
PopIn=find(r<=pInversion);
len=length(PopIn);
if len>=1
    for i=1:len
        d=sort(unidrnd(n,1,2));
        if d(1)~=1&d(2)~=n
           NewPop(PopIn(i),1:d(1)-1)=OldPop(PopIn(i),1:d(1)-1);
           NewPop(PopIn(i),d(1):d(2))=OldPop(PopIn(i),d(2):-1:d(1));
           NewPop(PopIn(i),d(2)+1:n)=OldPop(PopIn(i),d(2)+1:n);
       end
   end
end

[本日：1 本周：1 本月：1 总数：13 ] [返回上一页] [打 印] 
上一篇文章：Matlab中神经网络模型的互相转化 
下一篇文章：遗传算法解决 TSP 问题（附matlab源程序） 
文章评论 （评论内容只代表网友观点，与本站立场无关！）
````

</details>

#### 遗传算法解决 TSP 问题 · MATLAB · 076cad52

- 归属算法：遗传算法GA
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“数据读取与预处理”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `gatsp1`、`randomize`、`rshift`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`365635e679a735c858baf795b05df00f1262d18cc3e82cf1cf18ba7998abe05c`
- 语言：MATLAB
- 符号：`gatsp1`, `randomize`, `rshift`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传算法的一些应用于编程（含源代码）/遗传算法解决 TSP 问题.txt`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传算法/遗传算法解决 TSP 问题.txt`

<details>
<summary>展开原始代码</summary>

````matlab
遗传算法解决 TSP 问题（附matlab源程序）
作者：KINGTT  来源：转载  发布时间：2008-7-17 9:11:53
减小字体 增大字体 

已知n个城市之间的相互距离，现有一个推销员必须遍访这n个城市，并且每个城市
只能访问一次，最后又必须返回出发城市。如何安排他对这些城市的访问次序，可使其
旅行路线的总长度最短？
    用图论的术语来说，假设有一个图g=(v,e)，其中v是顶点集，e是边集，设d=(dij)
是由顶点i和顶点j之间的距离所组成的距离矩阵，旅行商问题就是求出一条通过所有顶
点且每个顶点只通过一次的具有最短距离的回路。
    这个问题可分为对称旅行商问题(dij=dji,,任意i,j=1,2,3，…,n)和非对称旅行商
问题(dij≠dji,,任意i,j=1,2,3，…,n)。
    若对于城市v={v1,v2,v3,…,vn}的一个访问顺序为t=(t1,t2,t3,…,ti,…,tn),其中
ti∈v(i=1,2,3,…,n)，且记tn+1= t1，则旅行商问题的数学模型为：
     min     l=σd(t(i),t(i+1)) （i=1,…,n）
    旅行商问题是一个典型的组合优化问题，并且是一个np难问题，其可能的路径数目
与城市数目n是成指数型增长的，所以一般很难精确地求出其最优解，本文采用遗传算法
求其近似解。
    遗传算法：
初始化过程：用v1,v2,v3,…,vn代表所选n个城市。定义整数pop-size作为染色体的个数
，并且随机产生pop-size个初始染色体，每个染色体为1到18的整数组成的随机序列。
适应度f的计算：对种群中的每个染色体vi，计算其适应度，f=σd(t(i),t(i+1)).
评价函数eval(vi)：用来对种群中的每个染色体vi设定一个概率，以使该染色体被选中
的可能性与其种群中其它染色体的适应性成比例，既通过轮盘赌，适应性强的染色体被
选择产生后台的机会要大，设alpha∈(0,1)，本文定义基于序的评价函数为eval(vi)=al
pha*(1-alpha).^(i-1) 。[随机规划与模糊规划]
选择过程：选择过程是以旋转赌轮pop-size次为基础，每次旋转都为新的种群选择一个
染色体。赌轮是按每个染色体的适应度进行选择染色体的。
   step1 、对每个染色体vi,计算累计概率qi，q0=0;qi=σeval(vj)   j=1,…,i;i=1,
…pop-size.
   step2、从区间(0,pop-size)中产生一个随机数r；
   step3、若qi-1   step4、重复step2和step3共pop-size次，这样可以得到pop-size个复制的染色体。
grefenstette编码：由于常规的交叉运算和变异运算会使种群中产生一些无实际意义的
染色体，本文采用grefenstette编码《遗传算法原理及应用》可以避免这种情况的出现
。所谓的grefenstette编码就是用所选队员在未选（不含淘汰）队员中的位置，如：
          8 15 2 16 10 7 4 3 11 14 6 12 9 5 18 13 17 1
          对应：
          8 14 2 13 8 6 3 2 5 7 3 4 3 2 4 2 2 1。
交叉过程：本文采用常规单点交叉。为确定交叉操作的父代，从到pop-size重复以下过
程：从[0，1]中产生一个随机数r，如果r            将所选的父代两两组队，随机产生一个位置进行交叉，如：
          8 14 2 13 8 6 3 2 5 7 3 4 3 2 4 2 2 1
          6 12 3 5 6 8 5 6 3 1 8 5 6 3 3 2 1 1
交叉后为：
         8 14 2 13 8 6 3 2 5 1 8 5 6 3 3 2 1 1
         6 12 3 5 6 8 5 6 3 7 3 4 3 2 4 2 2 1
变异过程：本文采用均匀多点变异。类似交叉操作中选择父代的过程，在r 选择多个染色体vi作为父代。对每一个选择的父代，随机选择多个位置，使其在每位置
按均匀变异（该变异点xk的取值范围为[ukmin,ukmax],产生一个[0，1]中随机数r，该点
变异为x'k=ukmin+r(ukmax-ukmin)）操作。如：
         8 14 2 13 8 6 3 2 5 7 3 4 3 2 4 2 2 1
      变异后：
        8 14 2 13 10 6 3 2 2 7 3 4 5 2 4 1 2 1
反grefenstette编码：交叉和变异都是在grefenstette编码之后进行的，为了循环操作
和返回最终结果，必须逆grefenstette编码过程，将编码恢复到自然编码。
循环操作：判断是否满足设定的带数xzome，否，则跳入适应度f的计算；是，结束遗传
操作，跳出。 
matlab 代码


distTSP.txt
0 6 18 4 8
7 0 17 3 7
4 4 0 4 5
20 19 24 0 22
8 8 16 6 0
%GATSP.m
function gatsp1()
clear;
load distTSP.txt;
distance=distTSP;
N=5;
ngen=100;
ngpool=10;
%ngen=input('# of generations to evolve = ');
%ngpool=input('# of chromosoms in the gene pool = '); % size of genepool
gpool=zeros(ngpool,N+1); % gene pool
for i=1:ngpool, % intialize gene pool
gpool(i,:)=[1 randomize([2:N]')' 1];
for j=1:i-1
while gpool(i,:)==gpool(j,:)
       gpool(i,:)=[1 randomize([2:N]')' 1];
                end
             end
          end

costmin=100000;
    tourmin=zeros(1,N);
      cost=zeros(1,ngpool);
increase=1;resultincrease=1;
      for i=1:ngpool,
          cost(i)=sum(diag(distance(gpool(i,:)',rshift(gpool(i,:))')));
     end
% record current best solution
[costmin,idx]=min(cost);
tourmin=gpool(idx,:);
disp([num2str(increase) 'minmum trip length = ' num2str(costmin)])

costminold2=200000;costminold1=150000;resultcost=100000;
tourminold2=zeros(1,N);
tourminold1=zeros(1,N);
resulttour=zeros(1,N);
while (abs(costminold2-costminold1) ;100)&(abs(costminold1-costmin) ;100)&(increase ;500)

costminold2=costminold1; tourminold2=tourminold1;
costminold1=costmin;tourminold1=tourmin;
increase=increase+1;
if resultcost>costmin
   resultcost=costmin;
   resulttour=tourmin;
   resultincrease=increase-1;
         end
for i=1:ngpool,
           cost(i)=sum(diag(distance(gpool(i,:)',rshift(gpool(i,:))')));
end
% record current best solution
[costmin,idx]=min(cost);
tourmin=gpool(idx,:);
%==============
% copy gens in th gpool according to the probility ratio
% >1.1 copy twice
% >=0.9 copy once
% ;0.9 remove
[csort,ridx]=sort(cost);
% sort from small to big.
csum=sum(csort);
caverage=csum/ngpool;
cprobilities=caverage./csort;
copynumbers=0;removenumbers=0;
for i=1:ngpool,
    if cprobilities(i) >1.1
             copynumbers=copynumbers+1;
                    end
           if cprobilities(i) <0.9
                   removenumbers=removenumbers+1;
                           end
                end
   copygpool=min(copynumbers,removenumbers);
               for i=1:copygpool
                  for j=ngpool:-1:2*i+2 gpool(j,:)=gpool(j-1,:);
            end
                   gpool(2*i+1,:)=gpool(i,:);
          end
                 if copygpool==0
                       gpool(ngpool,:)=gpool(1,:);
                  end
%=========
%when genaration is more than 50,or the patterns in a couple are too close,do mutation
for i=1:ngpool/2
        %
sameidx=[gpool(2*i-1,:)==gpool(2*i,:)];
diffidx=find(sameidx==0);
           if length(diffidx)<=2
                gpool(2*i,:)=[1 randomize([2:12]')' 1];
                           end
                               end
%===========
%cross gens in couples
           for i=1:ngpool/2
                  [gpool(2*i-1,:),gpool(2*i,:)]=crossgens(gpool(2*i-1,:),gpool(2*i,:));
       end

        for i=1:ngpool,
              cost(i)=sum(diag(distance(gpool(i,:)',rshift(gpool(i,:))')));
       end
% record current best solution
[costmin,idx]=min(cost);
tourmin=gpool(idx,:);
disp([num2str(increase) 'minmum trip length = ' num2str(costmin)])
end  

disp(['cost function evaluation: ' int2str(increase) ' times!'])
disp(['n:' int2str(resultincrease)])
disp(['minmum trip length = ' num2str(resultcost)])
disp('optimum tour = ')
disp(num2str(resulttour))
%====================================================
function B=randomize(A,rowcol)
% Usage: B=randomize(A,rowcol)
% randomize row orders or column orders of A matrix
% rowcol: if =0 or omitted, row order (default)
% if = 1, column order

rand('state',sum(100*clock))
if nargin == 1,
        rowcol=0;
end
         if rowcol==0,
              [m,n]=size(A);
              p=rand(m,1);
              [p1,I]=sort(p);
              B=A(I,:);
elseif rowcol==1,
          Ap=A';
          [m,n]=size(Ap);
          p=rand(m,1);
          [p1,I]=sort(p);
          B=Ap(I,:)';
end
%=====================================================
function y=rshift(x,dir)
% Usage: y=rshift(x,dir)
% rotate x vector to right (down) by 1 if dir = 0 (default)
% or rotate x to left (up) by 1 if dir = 1
if nargin ;2, dir=0; end
[m,n]=size(x);
if m>1,
if n == 1,
    col=1;
elseif n>1,
    error('x must be a vector! break');
end % x is a column vectorelseif m == 1,
if n == 1, y=x;
return
elseif n>1,
     col=0; % x is a row vector endend
if dir==1, % rotate left or up
       if col==0, % row vector, rotate left
             y = [x(2:n) x(1)];
       elseif col==1,
             y = [x(2:n); x(1)]; % rotate up
end
   elseif dir==0, % default rotate right or down
              if col==0,
                    y = [x(n) x(1:n-1)];
             elseif col==1 % column vector
                       y = [x(n); x(1:n-1)];
                   end
             end
%==================================================
function [L1,L2]=crossgens(X1,X2)
% Usage:[L1,L2]=crossgens(X1,X2)
s=randomize([2:12]')';
n1=min(s(1),s(11));n2=max(s(1),s(11));
X3=X1;X4=X2;
for i=n1:n2,
                for j=1:13,
                     if X2(i)==X3(j),
                          X3(j)=0;
                             end
                  if X1(i)==X4(j),                          X4(j)=0;
               end
           end
        end
   j=13;k=13;
    for i=12:-1:2,
          if X3(i)~=0,
               j=j-1;
                 t=X3(j);X3(j)=X3(i);X3(i)=t;
               end
                    if X4(i)~=0,
                           k=k-1;
                      t=X4(k);X4(k)=X4(i);X4(i)=t;
                   end
               end
           for i=n1:n2
              X3(2+i-n1)=X2(i);
              X4(2+i-n1)=X1(i);
           end
L1=X3;L2=X4;
%=======================
````

</details>

#### 相似实现组 · MATLAB · ce45e8f4

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：2
- 原始来源文件：4
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：ga_nn.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：构造目标与边界/约束并执行连续优化；重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`a7db10132e35c4ca2e6d7054a7ecb74080d1a3cccbd06e461c2eb99076ea4bfa`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/ga_nn.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/ga_nn.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/checkbound.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/constrValidate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/gaoutput.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/gaplot.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/isItTimeToStop.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/makeState.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/migrate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/stepGASA.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/validate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/checkbound.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/constrValidate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/gaoutput.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/gaplot.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/isItTimeToStop.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/makeState.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/migrate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/stepGASA.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/validate.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [X,FVAL,REASON,OUTPUT,POPULATION,SCORES] = ...
    ga_nn(FitnessFcn,GenomeLength,Aineq,Bineq,Aeq,Beq,LB,UB,options)
%GA_NN Genetic algorithm linear constrained solver.
%   Private function to GA
%
%   X = GA_NN(FITNESSFCN,NAVRS,A,b) finds a local minimum X to the function
%   FITNESSFCN, subject to the linear inequalities A*X <= B. FITNESSFCN
%   accepts input X and returns a scalar function value F evaluated at X.
%   X0 may be a scalar, vector, or matrix.
%
%   X = GA_NN(FITNESSFCN,NAVRS,A,b,Aeq,beq) finds a local minimum X to the
%   function FITNESSFCN, subject to the linear equalities Aeq*X = Beq as
%   well as A*X <= B. (Set A=[] and B=[] if no inequalities exist.)
%
%   X = GA_NN(FITNESSFCN,NAVRS,A,b,Aeq,beq,LB,UB) defines a set of lower and
%   upper bounds on the design variables, X, so that a solution is found in
%   the range LB <= X <= UB. Use empty matrices for LB and UB if no bounds
%   exist. Set LB(i) = -Inf if X(i) is unbounded below;  set UB(i) = Inf if
%   X(i) is unbounded above.
%
%   X = GA_NN(FITNESSFCN,NAVRS,A,b,Aeq,beq,LB,UB,options) minimizes
%   with the default optimization parameters replaced by values in the
%   structure OPTIONS. OPTIONS can be created with the GAOPTIMSET function.
%   See GAOPTIMSET for details.
%
%   [X, FVAL] = GA_NN(FITNESSFCN, ...) returns FVAL, the value of the
%   fitness function FITNESSFCN at the solution X.
%
%   [X,FVAL,REASON] = GA_NN(FITNESSFCN, ...) returns the REASON for
%   stopping.
%
%   [X,FVAL,REASON,OUTPUT] = GA_NN(FITNESSFCN, ...) returns a
%   structure OUTPUT with the following information:
%            randstate: <State of the function RAND used before GA started>
%           randnstate: <State of the function RANDN used before GA started>
%          generations: <Total generations, excluding HybridFcn iterations>
%            funccount: <Total function evaluations>
%              message: <GA termination message>
%
%   [X,FVAL,REASON,OUTPUT,POPULATION] = GA_NN(FITNESSFCN, ...) returns the
%   final POPULATION at termination.
%
%   [X,FVAL,REASON,OUTPUT,POPULATION,SCORES] = GA_NN(FITNESSFCN, ...)
%   returns the SCORES of the final POPULATION.
%
%   See also GAOPTIMSET, FITNESSFUNCTION, PATTERNSEARCH, @.

defaultopt = gaoptimset;

% If just 'defaults' passed in, return the default options in X
if nargin == 1 && nargout <= 1 && isequal(FitnessFcn,'defaults')
    X = defaultopt;
    return
end
% Use default options if empty
if ~isempty(options) && ~isa(options,'struct')
    error('gads:GALINCON:ninthInputNotStruct','Invalid input argument to GALINCON.');
elseif isempty(options)
    options = gaoptimset;
end
% Initialize output args
X = []; FVAL = []; REASON = [];POPULATION=[];SCORES=[];state = [];
user_options = options; EXITFLAG = [];
% Determine the verbosity
switch  gaoptimget(options,'Display',defaultopt,'fast')
    case {'off','none'}
        verbosity = 0;
    case 'final'
        verbosity = 1;
    case 'iter'
        verbosity = 2;
    case 'diagnose'
        verbosity = 3;
    otherwise
        verbosity = 1;
end

% Validate options and fitness function
[GenomeLength,FitnessFcn,options] = validate(GenomeLength,FitnessFcn,options);

%Remember the random number states used
output.randstate  = rand('state');
output.randnstate = randn('state');
output.generations = 0;
output.funccount   = 0;
output.message   = '';

if (isempty(Aeq) && isempty(Aineq) && isempty(Bineq) && isempty(Beq) && isempty(LB) && isempty(UB))
    type = 'unconstrained';
elseif ~isempty(Aeq) || ~isempty(Aineq) || ~isempty(LB) || ~isempty(UB)
    % Type of optimization problem
    if ~isempty(Aineq) || ~isempty(Aeq)
        type = 'linearconstraints';
    elseif ~isempty(LB) || ~isempty(UB)
        type = 'boundconstraints';
    else
        type = 'unconstrained'; % Should not reach here
    end

    % Bound correction
    [LB,UB,msg,EXITFLAG] = checkbound(LB,UB,GenomeLength,verbosity);
    if EXITFLAG < 0
        FVAL     =    [];
        REASON = msg;
        OUTPUT.message = msg;
        if verbosity > 0
            fprintf('%s\n',msg)
        end
        return;
    end

    % Reinitialize these
    nineqcstr = size(Aineq,1);
    neqcstr   = size(Aeq,1);
    ncstr     = nineqcstr + neqcstr;

    % Create A, as described in L & T  L <= AX <=U.
    Abox = eye(GenomeLength);
    A    = full([Aeq;Aineq;Abox]);
    U    = full([Beq;Bineq;UB]);
    L    = full([Beq;repmat(-Inf,nineqcstr,1);LB]);

    % Logical indices of constraints.
    IndIneqcstr = false(size(A,1),1);
    IndEqcstr   = false(size(A,1),1);
    IndEqcstr(1:neqcstr) = 1;
    IndIneqcstr(neqcstr+1:ncstr) = 1;

    % Validate constraints and add it to options structure
    options = constrValidate(A,L,U,IndEqcstr,IndIneqcstr,[],options,type,type);
end

% Create initial state: population, scores, status data
state = makeState(GenomeLength,FitnessFcn,options);

% Give the plot/output Fcns a chance to do any initialization they need.
state = gaplot(FitnessFcn,options,state,'init');
[state,options] = gaoutput(FitnessFcn,options,state,'init');

% Print some diagnostic information if asked for
if verbosity > 2
    gadiagnose(FitnessFcn,[],GenomeLength,type,nineqcstr,neqcstr,ncstr,user_options);
end
%Setup display header
if  any(strcmpi(options.Display, {'iter','diagnose'}))
    fprintf('\n                               Best           Mean      Stall\n');
    fprintf('Generation      f-count        f(x)           f(x)    Generations\n');
end

REASON = '';
% run the main loop until some termination condition becomes true
while isempty(REASON)
    state.Generation = state.Generation + 1;
    %Repeat for each subpopulation (element of the populationSize vector)
    offset = 0;
    totalPop = options.PopulationSize;
    % each sub-population loop
    for pop = 1:length(totalPop)
        populationSize =  totalPop(pop);
        thisPopulation = 1 + (offset:(offset + populationSize - 1));
        population = state.Population(thisPopulation,:);
        score = state.Score( thisPopulation );
        %Empty population is also possible
        if isempty(thisPopulation)
            continue;
        end
        [score,population,state] = stepGASA(score,population,options,state,GenomeLength,FitnessFcn);
        % store the results for this sub-population
        state.Population(thisPopulation,:) = population;
        state.Score(thisPopulation) = score;
        offset = offset + populationSize;
    end

    % remember the best score
    scores = state.Score;
    best = min(state.Score);
    generation = state.Generation;
    state.Best(generation) = best;
    % keep track of improvement in the best
    if((generation > 1) && finite(best))
        if(state.Best(generation-1) > best)
            state.LastImprovement = generation;
            state.LastImprovementTime = cputime;
        end
    end
    % do any migration
    state = migrate(FitnessFcn,GenomeLength,options,state);
    % update the Output
    state = gaplot(FitnessFcn,options,state,'iter');
    [state,options,optchanged] = gaoutput(FitnessFcn,options,state,'iter');
    if optchanged
        options = constrValidate(A,L,U,IndEqcstr,IndIneqcstr,[],options,type,type);
    end
    % check to see if any stopping criteria have been met
    REASON = isItTimeToStop(options,state);
end %End while loop

% find and return the best solution
[FVAL,best] = min(state.Score);
X = state.Population(best,:);

%Update output structure
OUTPUT.generations = state.Generation;
OUTPUT.funccount   = state.Generation*length(state.Score);
OUTPUT.maxconstraint = 0.0;
OUTPUT.message     = REASON;

% load up outputs
if(nargout > 4)
    POPULATION = state.Population;
    if(nargout > 5)
        SCORES = state.Score;
    end
end

% Call hybrid function
if ~isempty(options.HybridFcn) && strcmpi(options.PopulationType,'doubleVector')
    [X,FVAL] = callHybridFunction;
end
% give the Output functions a chance to finish up
gaplot(FitnessFcn,options,state,'done');
gaoutput(FitnessFcn,options,state,'done');

%-----------------------------------------------------------------
% Hybrid function
    function [xhybrid,fhybrid] = callHybridFunction
        xhybrid = X;
        fhybrid = FVAL;
        % Who is the hybrid function
        if isa(options.HybridFcn,'function_handle')
            hfunc = func2str(options.HybridFcn);
        else
            hfunc = options.HybridFcn;
        end
        % Inform about hybrid scheme
        if   verbosity > 1
            fprintf('%s%s%s\n','Switching to the hybrid optimization algorithm (',upper(hfunc),').');
        end
        % Create functions handle to be passed to hybrid function
        FitnessHybridFcn = @(x) FitnessFcn(x,options.FitnessFcnArgs{:});
        ConstrHybridFcn = [];
        % Determine which syntax to call
        switch hfunc
            case 'fmincon'
                [xx,ff,e,o] = feval(options.HybridFcn,FitnessHybridFcn,X,Aineq, ...
                    Bineq,Aeq,Beq,LB,UB,ConstrHybridFcn,options.HybridFcnArgs{:});
                OUTPUT.funccount = OUTPUT.funccount + o.funcCount;
                OUTPUT.message   = [OUTPUT.message sprintf('\nFMINCON: \n'), o.message];
            case 'patternsearch'
                [xx,ff,e,o] = feval(options.HybridFcn,FitnessHybridFcn,X,Aineq, ...
                    Bineq,Aeq,Beq,LB,UB,ConstrHybridFcn,options.HybridFcnArgs{:});
                OUTPUT.funccount = OUTPUT.funccount + o.funccount;
                OUTPUT.message   = [OUTPUT.message sprintf('\nPATTERNSEARCH: \n'), o.message];
            case {'fminsearch', 'fminunc'}
                msg = sprintf('%s is unconstrained optimization solver',upper(hfunc));
                msg = [msg, sprintf('\n%s',' using constrained solver FMINCON as hybrid function.')];
                warning('gads:GALINCON:unconstrainedHybridFcn',msg);
                % We need to store this warning state so that we can
                % display it in the GUI
                [lastmsg, lastid] = lastwarn; warning off;
                [xx,ff,e,o] = feval(@fmincon,FitnessHybridFcn,X,Aineq, ...
                    Bineq,Aeq,Beq,LB,UB,ConstrHybridFcn,options.HybridFcnArgs{:});
                warning on; lastwarn(lastmsg,lastid);
                OUTPUT.funccount = OUTPUT.funccount + o.funcCount;
                OUTPUT.message   = [OUTPUT.message sprintf('\nFMINCON: \n'), o.message];
            otherwise
                error('gads:GALINCON:hybridFcnError','Hybrid function must be one of the following:\n@FMINCON, @PATTERNSEARCH.')
        end
        % Check for exitflag and fval
        if ff < fhybrid && e > 0
            fhybrid = ff;
            xhybrid = xx;
        end
        %Inform about hybrid scheme termination
        if  verbosity > 1
            fprintf('%s%s\n',upper(hfunc), ' terminated.');
        end
    end % End of callHybridFunction
end  % End of gaconstr.m
````

</details>

##### 变体 2：ga_nn4.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：构造目标与边界/约束并执行连续优化；重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移；包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`f4b1b5ddba5371de39498cab81891f3123ab53627b2da471987bf87b1a5ea8e5`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/ga_nn4.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/ga_nn4.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/checkbound.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/constrValidate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/ga_nn.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/gaoutput.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/gaplot.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/isItTimeToStop.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/makeState.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/migrate.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/stepGASA4.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/validate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/checkbound.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/constrValidate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/ga_nn.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/gaoutput.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/gaplot.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/isItTimeToStop.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/makeState.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/migrate.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/stepGASA4.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/validate.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [X,FVAL,REASON,OUTPUT,POPULATION,SCORES] = ...
    ga_nn(FitnessFcn,GenomeLength,Aineq,Bineq,Aeq,Beq,LB,UB,options)
%GA_NN Genetic algorithm linear constrained solver.
%   Private function to GA
%
%   X = GA_NN(FITNESSFCN,NAVRS,A,b) finds a local minimum X to the function
%   FITNESSFCN, subject to the linear inequalities A*X <= B. FITNESSFCN
%   accepts input X and returns a scalar function value F evaluated at X.
%   X0 may be a scalar, vector, or matrix.
%
%   X = GA_NN(FITNESSFCN,NAVRS,A,b,Aeq,beq) finds a local minimum X to the
%   function FITNESSFCN, subject to the linear equalities Aeq*X = Beq as
%   well as A*X <= B. (Set A=[] and B=[] if no inequalities exist.)
%
%   X = GA_NN(FITNESSFCN,NAVRS,A,b,Aeq,beq,LB,UB) defines a set of lower and
%   upper bounds on the design variables, X, so that a solution is found in
%   the range LB <= X <= UB. Use empty matrices for LB and UB if no bounds
%   exist. Set LB(i) = -Inf if X(i) is unbounded below;  set UB(i) = Inf if
%   X(i) is unbounded above.
%
%   X = GA_NN(FITNESSFCN,NAVRS,A,b,Aeq,beq,LB,UB,options) minimizes
%   with the default optimization parameters replaced by values in the
%   structure OPTIONS. OPTIONS can be created with the GAOPTIMSET function.
%   See GAOPTIMSET for details.
%
%   [X, FVAL] = GA_NN(FITNESSFCN, ...) returns FVAL, the value of the
%   fitness function FITNESSFCN at the solution X.
%
%   [X,FVAL,REASON] = GA_NN(FITNESSFCN, ...) returns the REASON for
%   stopping.
%
%   [X,FVAL,REASON,OUTPUT] = GA_NN(FITNESSFCN, ...) returns a
%   structure OUTPUT with the following information:
%            randstate: <State of the function RAND used before GA started>
%           randnstate: <State of the function RANDN used before GA started>
%          generations: <Total generations, excluding HybridFcn iterations>
%            funccount: <Total function evaluations>
%              message: <GA termination message>
%
%   [X,FVAL,REASON,OUTPUT,POPULATION] = GA_NN(FITNESSFCN, ...) returns the
%   final POPULATION at termination.
%
%   [X,FVAL,REASON,OUTPUT,POPULATION,SCORES] = GA_NN(FITNESSFCN, ...)
%   returns the SCORES of the final POPULATION.
%
%   See also GAOPTIMSET, FITNESSFUNCTION, PATTERNSEARCH, @.

defaultopt = gaoptimset;

% If just 'defaults' passed in, return the default options in X
if nargin == 1 && nargout <= 1 && isequal(FitnessFcn,'defaults')
    X = defaultopt;
    return
end
% Use default options if empty
if ~isempty(options) && ~isa(options,'struct')
    error('gads:GALINCON:ninthInputNotStruct','Invalid input argument to GALINCON.');
elseif isempty(options)
    options = gaoptimset;
end
% Initialize output args
X = []; FVAL = []; REASON = [];POPULATION=[];SCORES=[];state = [];
user_options = options; EXITFLAG = [];
% Determine the verbosity
switch  gaoptimget(options,'Display',defaultopt,'fast')
    case {'off','none'}
        verbosity = 0;
    case 'final'
        verbosity = 1;
    case 'iter'
        verbosity = 2;
    case 'diagnose'
        verbosity = 3;
    otherwise
        verbosity = 1;
end

% Validate options and fitness function
[GenomeLength,FitnessFcn,options] = validate(GenomeLength,FitnessFcn,options);

%Remember the random number states used
output.randstate  = rand('state');
output.randnstate = randn('state');
output.generations = 0;
output.funccount   = 0;
output.message   = '';

if (isempty(Aeq) && isempty(Aineq) && isempty(Bineq) && isempty(Beq) && isempty(LB) && isempty(UB))
    type = 'unconstrained';
elseif ~isempty(Aeq) || ~isempty(Aineq) || ~isempty(LB) || ~isempty(UB)
    % Type of optimization problem
    if ~isempty(Aineq) || ~isempty(Aeq)
        type = 'linearconstraints';
    elseif ~isempty(LB) || ~isempty(UB)
        type = 'boundconstraints';
    else
        type = 'unconstrained'; % Should not reach here
    end

    % Bound correction
    [LB,UB,msg,EXITFLAG] = checkbound(LB,UB,GenomeLength,verbosity);
    if EXITFLAG < 0
        FVAL     =    [];
        REASON = msg;
        OUTPUT.message = msg;
        if verbosity > 0
            fprintf('%s\n',msg)
        end
        return;
    end

    % Reinitialize these
    nineqcstr = size(Aineq,1);
    neqcstr   = size(Aeq,1);
    ncstr     = nineqcstr + neqcstr;

    % Create A, as described in L & T  L <= AX <=U.
    Abox = eye(GenomeLength);
    A    = full([Aeq;Aineq;Abox]);
    U    = full([Beq;Bineq;UB]);
    L    = full([Beq;repmat(-Inf,nineqcstr,1);LB]);

    % Logical indices of constraints.
    IndIneqcstr = false(size(A,1),1);
    IndEqcstr   = false(size(A,1),1);
    IndEqcstr(1:neqcstr) = 1;
    IndIneqcstr(neqcstr+1:ncstr) = 1;

    % Validate constraints and add it to options structure
    options = constrValidate(A,L,U,IndEqcstr,IndIneqcstr,[],options,type,type);
end

% Create initial state: population, scores, status data
state = makeState(GenomeLength,FitnessFcn,options);

% Give the plot/output Fcns a chance to do any initialization they need.
state = gaplot(FitnessFcn,options,state,'init');
[state,options] = gaoutput(FitnessFcn,options,state,'init');

% Print some diagnostic information if asked for
if verbosity > 2
    gadiagnose(FitnessFcn,[],GenomeLength,type,nineqcstr,neqcstr,ncstr,user_options);
end
%Setup display header
if  any(strcmpi(options.Display, {'iter','diagnose'}))
    fprintf('\n                               Best           Mean      Stall\n');
    fprintf('Generation      f-count        f(x)           f(x)    Generations\n');
end

REASON = '';
% run the main loop until some termination condition becomes true
while isempty(REASON)
    state.Generation = state.Generation + 1;
    %Repeat for each subpopulation (element of the populationSize vector)
    offset = 0;
    totalPop = options.PopulationSize;
    % each sub-population loop
    for pop = 1:length(totalPop)
        populationSize =  totalPop(pop);
        thisPopulation = 1 + (offset:(offset + populationSize - 1));
        population = state.Population(thisPopulation,:);
        score = state.Score( thisPopulation );
        %Empty population is also possible
        if isempty(thisPopulation)
            continue;
        end
        [score,population,state] = stepGASA4(score,population,options,state,GenomeLength,FitnessFcn);
        % store the results for this sub-population
        state.Population(thisPopulation,:) = population;
        state.Score(thisPopulation) = score;
        offset = offset + populationSize;
    end

    % remember the best score
    scores = state.Score;
    best = min(state.Score);
    generation = state.Generation;
    state.Best(generation) = best;
    % keep track of improvement in the best
    if((generation > 1) && finite(best))
        if(state.Best(generation-1) > best)
            state.LastImprovement = generation;
            state.LastImprovementTime = cputime;
        end
    end
    % do any migration
    state = migrate(FitnessFcn,GenomeLength,options,state);
    % update the Output
    state = gaplot(FitnessFcn,options,state,'iter');
    [state,options,optchanged] = gaoutput(FitnessFcn,options,state,'iter');
    if optchanged
        options = constrValidate(A,L,U,IndEqcstr,IndIneqcstr,[],options,type,type);
    end
    % check to see if any stopping criteria have been met
    REASON = isItTimeToStop(options,state);
end %End while loop

% find and return the best solution
[FVAL,best] = min(state.Score);
X = state.Population(best,:);

%Update output structure
OUTPUT.generations = state.Generation;
OUTPUT.funccount   = state.Generation*length(state.Score);
OUTPUT.maxconstraint = 0.0;
OUTPUT.message     = REASON;

% load up outputs
if(nargout > 4)
    POPULATION = state.Population;
    if(nargout > 5)
        SCORES = state.Score;
    end
end

% Call hybrid function
if ~isempty(options.HybridFcn) && strcmpi(options.PopulationType,'doubleVector')
    [X,FVAL] = callHybridFunction;
end
% give the Output functions a chance to finish up
gaplot(FitnessFcn,options,state,'done');
gaoutput(FitnessFcn,options,state,'done');

%-----------------------------------------------------------------
% Hybrid function
    function [xhybrid,fhybrid] = callHybridFunction
        xhybrid = X;
        fhybrid = FVAL;
        % Who is the hybrid function
        if isa(options.HybridFcn,'function_handle')
            hfunc = func2str(options.HybridFcn);
        else
            hfunc = options.HybridFcn;
        end
        % Inform about hybrid scheme
        if   verbosity > 1
            fprintf('%s%s%s\n','Switching to the hybrid optimization algorithm (',upper(hfunc),').');
        end
        % Create functions handle to be passed to hybrid function
        FitnessHybridFcn = @(x) FitnessFcn(x,options.FitnessFcnArgs{:});
        ConstrHybridFcn = [];
        % Determine which syntax to call
        switch hfunc
            case 'fmincon'
                [xx,ff,e,o] = feval(options.HybridFcn,FitnessHybridFcn,X,Aineq, ...
                    Bineq,Aeq,Beq,LB,UB,ConstrHybridFcn,options.HybridFcnArgs{:});
                OUTPUT.funccount = OUTPUT.funccount + o.funcCount;
                OUTPUT.message   = [OUTPUT.message sprintf('\nFMINCON: \n'), o.message];
            case 'patternsearch'
                [xx,ff,e,o] = feval(options.HybridFcn,FitnessHybridFcn,X,Aineq, ...
                    Bineq,Aeq,Beq,LB,UB,ConstrHybridFcn,options.HybridFcnArgs{:});
                OUTPUT.funccount = OUTPUT.funccount + o.funccount;
                OUTPUT.message   = [OUTPUT.message sprintf('\nPATTERNSEARCH: \n'), o.message];
            case {'fminsearch', 'fminunc'}
                msg = sprintf('%s is unconstrained optimization solver',upper(hfunc));
                msg = [msg, sprintf('\n%s',' using constrained solver FMINCON as hybrid function.')];
                warning('gads:GALINCON:unconstrainedHybridFcn',msg);
                % We need to store this warning state so that we can
                % display it in the GUI
                [lastmsg, lastid] = lastwarn; warning off;
                [xx,ff,e,o] = feval(@fmincon,FitnessHybridFcn,X,Aineq, ...
                    Bineq,Aeq,Beq,LB,UB,ConstrHybridFcn,options.HybridFcnArgs{:});
                warning on; lastwarn(lastmsg,lastid);
                OUTPUT.funccount = OUTPUT.funccount + o.funcCount;
                OUTPUT.message   = [OUTPUT.message sprintf('\nFMINCON: \n'), o.message];
            otherwise
                error('gads:GALINCON:hybridFcnError','Hybrid function must be one of the following:\n@FMINCON, @PATTERNSEARCH.')
        end
        % Check for exitflag and fval
        if ff < fhybrid && e > 0
            fhybrid = ff;
            xhybrid = xx;
        end
        %Inform about hybrid scheme termination
        if  verbosity > 1
            fprintf('%s%s\n',upper(hfunc), ' terminated.');
        end
    end % End of callHybridFunction
end  % End of gaconstr.m
````

</details>

#### gacreation_nn · MATLAB · aa889b37

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `gacreation_nn`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`89c6de004ec2a7680eb01c83db348cd143ecb0808b97545cb8b5b13de964b750`
- 语言：MATLAB
- 符号：`gacreation_nn`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/gacreation_nn.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/gacreation_nn.m`

<details>
<summary>展开原始代码</summary>

````matlab
function Population = gacreation_nn(GenomeLength,FitnessFcn,options)
%GACREATION_NN Creates the initial population for genetic algorithm.
%   POP = GACREATION_NN(NVARS,FITNESSFCN,OPTIONS) Creates the
%   initial population that GA will then evolve into a solution.
%
%   Population size can be a vector of separate populations.
%   Here, we are only interested in the total number.
%
%   Example:
%     options = gaoptimset('PopulationType','bitString');
%            NVARS = 1; FitnessFcn = @ackelyfcn;
%
%     pop = GACREATION_NN(NVARS,FitnessFcn,options);
%
%   pop will be a 20-by-1 logical column vector.  Note that the
%   default Population Size in GAOPTIMSET is 20.

popSize = sum(options.PopulationSize);

if(strcmpi(options.PopulationType,'doubleVector'))
    if ~isfield(options,'LinearConstr')
        linConLen = 0;
        range = options.PopInitRange;
        lBound = range(1,:);
        uBound = range(2,:);
    else
        linCon = options.LinearConstr;
        type = linCon.type;
        % Sub-problem type is constrained?
        if strcmpi(type,'unconstrained')
            linConLen = 0;
            range = options.PopInitRange;
            lBound = range(1,:);
            uBound = range(2,:);
        else
            IndIneqcstr = linCon.IndIneqcstr;
            A = [linCon.A(IndIneqcstr,:)];
            b = [linCon.U(IndIneqcstr)];
            linConLen = length(b);
            
            lBound = linCon.L((end-GenomeLength)+1:end);
            uBound = linCon.U((end-GenomeLength)+1:end);
            z = [lBound,uBound];
            flag2 = (z-(1e+20)>0);
            z(flag2) = 1e+20;
            flag2 = (z+(1e+20)<0);
            z(flag2) = -1e+20;
            lBound = z(:,1)';
            uBound = z(:,2)';
        end
    end
    span = uBound - lBound;
    Population0 = repmat(lBound,popSize,1) + repmat(span,popSize,1) .* rand(popSize,GenomeLength);
    
    if linConLen > 0
        y = (A*Population0')';
        flag2 = [];
        for i=1:linConLen
            flag2(:,i) = (y(:,i)<b(i));
        end
        flag2 = all(flag2,2);
        Population2 = Population0(flag2,:);
        nv = size(Population2,1);

        K = (popSize/nv+1);
        while nv < popSize
            nPop2 = ceil(K * (popSize-nv));
            Population0 = repmat(lBound,nPop2,1) + repmat(span,nPop2,1) .* rand(nPop2,GenomeLength);
            y = (A*Population0')';
            flag2 = [];
            for i=1:linConLen
                flag2(:,i) = (y(:,i)<b(i));
            end
            flag2 = all(flag2,2);
            Population2 = [Population2;Population0(flag2,:)];
            nv = size(Population2,1);
        end
        Population0(1:popSize,:) = Population2(1:popSize,:);
    end
else
    msg = sprintf('Unknown population type ''%s'' in problem.',options.PopulationType);
    error('gads:GACREATIONUNIFORM:unknownPopulationType',msg);
end
Population = Population0;

if all(isnan(Population))
    msg = sprintf(['Initial population contains NaN;','OPTIONS.PopInitRange is possibly too big.']);
    error('gads:GACREATIONUNIFORM:populationIsNaN',msg);
elseif all(isinf(Population))
    msg = sprintf(['Initial population contains Inf;','OPTIONS.PopInitRange is possibly too big.']);
    error('gads:GACREATIONUNIFORM:populationIsInf',msg);
end
````

</details>

#### gaoutput · MATLAB · 3bb9bc1b

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f4624239a945630ffc2f63b17caf0d1fe6ecfc55897ccafe7a5290d988c89c69`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/gaoutput.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/gaoutput.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [state,options,optchanged] = gaoutput(FitnessFcn,options,state,flag)
%GAOUTPUT Helper function that manages the output functions for GA.
%
%   [STATE, OPTIONS, OPTCHANGED] = ...
%   GAOUTPUT(FitnessFcn, options, state, flag) runs each of the display
%   functions in the options.OutputFcns cell array.
%
%   this is a helper function called by ga between each generation, and is
%   not typicaly called directly.

%   Copyright 2003-2004 The MathWorks, Inc.
%   $Revision: 1.3.4.1 $  $Date: 2004/08/20 19:49:08 $


% get the functions and return if there are none
optchanged = false;
functions = options.OutputFcns;
if(isempty(functions))
    return
end

% call each output function
args = options.OutputFcnsArgs;
for i = 1:length(functions)
    [state,optnew,changed] = feval(functions{i},options,state,flag,args{i}{:});
    if ~isempty(state.StopFlag)
        return;
    end
    if changed %If changes are not duplicates, we will get all the changes
       options = optnew;
       optchanged = true;
    end
end
````

</details>

#### gaplot · MATLAB · 7420936b

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `beforeClose`、`buttonStop`、`change_runtime`、`gaplot`、`gaplotagain`、`removeDup`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f38bc6cc76f1682a43a7c4a1a9683c0397a969a051d70754019d6c378497967e`
- 语言：MATLAB
- 符号：`beforeClose`, `buttonStop`, `change_runtime`, `gaplot`, `gaplotagain`, `removeDup`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/gaplot.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/gaplot.m`

<details>
<summary>展开原始代码</summary>

````matlab
function state = gaplot(FitnessFcn,options,state,flag)
%GAPLOT Helper function that manages the display functions.
%   STATE = GAPLOT(FitnessFcn, options, state, flag) runs each of the graph
%   functions in the options.GraphFcns cell array.
%
%   This function is private to GA and is called between each generation.

%   Copyright 2003-2004 The MathWorks, Inc. 
%   $Revision: 1.11.4.3 $  $Date: 2004/08/20 19:49:09 $

persistent plotNo plotNames isNew fig position

if (rem(state.Generation,options.PlotInterval) ~=0)
    return;
end
functions = options.PlotFcns;
fname = 'Genetic Algorithm';
if (isempty(functions)) || (strcmpi(flag,'done') ...
    && isempty(findobj(0,'Type','figure','name',fname)))
    return;
end
functions = removeDup(functions);
args = options.PlotFcnsArgs;

%Called with 'init' flag or the figure is not present
if(strcmp(flag,'init')) || isempty(findobj(0,'Type','figure','name',fname))
    fig = findobj(0,'type','figure','name',fname);
    if isempty(fig)
        fig = figure('visible','off');
        if ~isempty(position) && ~strcmpi(get(fig,'WindowStyle'),'docked')
            set(fig,'Position',position);
        end
    end
    set(0,'CurrentFigure',fig);
    clf;
    set(fig,'DoubleBuffer','on','numbertitle','off','name',fname, ...
        'userdata',[],'DockControls','off','Renderer','painters');
    %Initialize the persistent variables
    plotNo = []; plotNames = [];isNew = []; 
    [plotNames, args, plotNo, isNew] = updatelist(plotNames, plotNo, ...
        functions, args, fig, 'init');
   
    %Give a stop button in the figure
    uicontrol('string','stop','Position',[10 10 40 30],'callback',@buttonStop);
    shg
end
set(0,'CurrentFigure',fig);
set(fig,'CloseRequestFcn',@beforeClose);
%determine the layout size in the figure
rows  = ceil(sqrt(length(functions)));
cols  = ceil(length(functions)/rows);


if change_runtime(functions,plotNames)
    [plotNames, args, plotNo, isNew] = updatelist(plotNames, plotNo, ...
        functions, args, fig, '');
end

if all(isNew)
    mouseaction([],[],[],'init');
end
% call each plot function
for i = 1:length(plotNames)
    handle = subplot(rows,cols,plotNo(i));
    if isNew(i)
        set(handle,'ButtonDownFcn',{@mouseaction,plotNames{i},'add'});
        %Do not delete the axis (which is the default settings)
        set(handle,'NextPlot','replacechildren');
        state = feval(plotNames{i},options,state,'init',args{i}{:});
         isNew(i)=false;
        %If in the middle of itertions, call with the regular 'flag' too.
        if ~strcmpi(flag,'init')
            state = feval(plotNames{i},options,state,flag,args{i}{:});
        end
    else
           state = feval(plotNames{i},options,state,flag,args{i}{:});
      end
end

state = gaplotagain(FitnessFcn,plotNames,args,options,state,flag);

drawnow
%Check if the figure is still alive
if isempty(findobj(0,'Type','figure','name',fname))
    state.StopFlag = 'stop requested.';
    return;
end
%Remember the position
position = get(fig,'Position');
%If any button was pressed, handle that
set(fig,'CloseRequestFcn','closereq');
if(strcmpi('stop',getappdata(fig,'data')))
    state.StopFlag = 'stop requested.';
    setappdata(fig,'data','')
    return;
end

%-------------------------------------------------------
%UPDATELIST updates the function list and plot numbers
%-------------------------------------------------------
function [plotNames, fcnArgs, plotNo, isNew] = updatelist(plotNames,plotNo,functions,args,fig,flag)

if strcmpi(flag,'init')
    plotNames = functions;
    plotNo   = 1:length(functions);
    isNew = true(length(plotNames),1);
    fcnArgs = args;
    return;
end

%determine the layout size in the figure
rows = ceil(sqrt(length(functions)));
cols = ceil(length(functions)/rows);
%what was the layout size before
rows1 = ceil(sqrt(length(plotNames)));
cols1 = ceil(length(plotNames)/rows1);

set(0,'CurrentFigure',fig);
fcnArgs = cell(1,length(plotNames));
isNew = false(length(plotNames),1);
to_delete = false(length(plotNames),1);
%Check if any of plotNames is not in functions;remove such entries
for i = 1:length(plotNames)
    [found, index] = foundfunc(plotNames{i},functions);
    if ~found
        delete_this = subplot(rows1,cols1,plotNo(i));
        delete(delete_this);
        to_delete(i) = true;
    else
        fcnArgs(i) = args(index(1));   
    end
end
%delete the plot names which are not in functions
plotNames(to_delete) = []; plotNo(to_delete) = []; 
isNew(to_delete) = []; fcnArgs(to_delete) = [];

%Now, add all new entries of functions in plotNames
for i = 1:length(functions)
    found = foundfunc(functions{i},plotNames);
    if ~found
        plotNames(end+1) = functions(i);
        fcnArgs(end+1) = args(i);
        isNew(end+1) = true;
        plotNo(end+1) = 0; 
    end
end

%Determine the plot numbers
if rows1 == rows && cols1 == cols
    %Binary search and replacement
    for i = 1:length(plotNames)
        if plotNo(i) == 0 
            for j = 1:rows*cols
                if ~any(j == plotNo)
                    plotNo(i) = j;
                end
            end
        end
    end
elseif rows1 > rows || cols1 > cols
    %find position of all existing axes and shift them
    for i = length(plotNames):-1:1
        if plotNo(i) ~=0
            subplot(rows1,cols1,plotNo(i))
            %plotNo(i) = i;
        else
            plotNo(i) = i;
            subplot(rows1,cols1,plotNo(i))
        end
        plotNo(i) = i;
        subplot(rows,cols,plotNo(i),gca);
        
    end
elseif rows1 < rows || cols1 < cols
    for i = 1:length(plotNames)
        if plotNo(i) ~=0
            subplot(rows1,cols1,plotNo(i))
            %plotNo(i) = i;
        else
            plotNo(i) = i;
            subplot(rows,cols,plotNo(i))
        end
        subplot(rows,cols,plotNo(i),gca);
    end
    
end

%-----------------------------------------------------------
%CHANGE_RUNTIME return a boolean if two cell arrays are same or not
%-----------------------------------------------------------
function bool = change_runtime(functions,plotNames)
bool = false;    
    for i = 1:length(functions)
        if ~foundfunc(functions{i},plotNames)
            bool = true;
        end
    end
    
    for i = 1:length(plotNames)
        if ~foundfunc(plotNames{i},functions)
            bool = true;
        end
    end

%-----------------------------------------------------------
%REMOVEDUP remove the duplicate entries in a cell array of function handle
%-----------------------------------------------------------
function functions = removeDup(functions)
i = 1;
while i <= length(functions)
      [found,index] = foundfunc(functions{i},functions);
      if found 
        functions(index(1:end-1)) = [];
    end
    i = i+1;
end

%-------------------------------------------------------------------------
%FOUNDFUNC Finds if STR is in FUNCNAMES, returns a boolean and index
%-------------------------------------------------------------------------
function [bool,index] = foundfunc(str,funcNames)

bool = false;
index = 0;
for i = 1:length(funcNames)
    if strcmpi(func2str(str),func2str(funcNames{i}))
        bool = true;
        if nargout > 1
            index(end+1) = i;
        end
    end
end
index(1) = [];
%-----------------------------------------------------------
%BUTTONSTOP callback for uibutton 'stop'
%-----------------------------------------------------------
function buttonStop(unused,unused2)
setappdata(gcf,'data','stop');

%-----------------------------------------------------------
%BUTTONDOWNACTION maintain a list of all the plot whose ButtondownFcn 
%callback or DeleteFcn is executed.
%-----------------------------------------------------------
function [done, func] = mouseaction(obj,eventdata,Name,what)

persistent list
done = false;
func = [];
switch lower(what)
    case 'length'
        if ~isempty(list)
            done = true;
        else 
            done = false;
        end
    case 'init'
        list = [];
        done = true;
    case 'add'
        if isempty(list)
            list{1} = Name;
        elseif ~foundfunc(Name,list);
            list{end+1} = Name;
            done = true;
        end
        fig = findobj(0,'type','figure','name',value2RHS(Name));
        if ~isempty(fig)
            close(fig);
        end
    case 'remove'
        if ~isempty(list)
          [found,index] = foundfunc(Name,list);
            if found
                list(index) = [];
                done = true;
            end
        end
end
func = list;

%-----------------------------------------------------------
%GAPLOTAGAIN plots all the functions whose ButtondownFcn has been
%called.
%-----------------------------------------------------------
function state = gaplotagain(FitnessFcn,plotNames,args,options,state,flag)

[foundAny, func] = mouseaction([],[],[],'length');
if ~foundAny
    return;
else
    to_delete = false(1,length(func));
    fcnArgs = cell(1,length(func));
    for i = 1:length(func)
        [found, index] = foundfunc(func{i},plotNames);
        if ~found
            to_delete(i) = true;
        else
            fcnArgs(i) = args(index(1));
        end
    end
    %delete the plot names which are not in functions
    func(to_delete) = [];  fcnArgs(to_delete) = [];
end

% call each plot function
for i = 1:length(func)
    fname = value2RHS(func{i});
    fig = findobj(0,'type','figure','name',fname);
    %Called with 'init' flag or the figure is not present
    if isempty(fig)
        fig = figure;
        set(fig,'DoubleBuffer','on','numbertitle','off','name',fname, ...
            'userdata',[],'Renderer','painters');
        handle = figure(fig);
        set(gca,'NextPlot','replacechildren');
        state = feval(func{i},options,state,'init');
        set(handle,'DeleteFcn',{@mouseaction,plotNames{i},'remove'});
    end
    set(0,'CurrentFigure',fig);
    state = feval(func{i},options,state,flag,fcnArgs{i}{:});
    set(gcf,'DeleteFcn',{@mouseaction,func{i},'remove'});
end

%-----------------------------------------------------------
%BEFORECLOSE CloseRequestFcn for main figure window
%-----------------------------------------------------------
function beforeClose(obj,event)

msg = sprintf('%s\n%s','YES will stop the solver (if running) and close the figure.',...
                           'NO will cancel this request.');
handle = questdlg(msg,'Close dialog', 'YES','NO','NO');
switch handle
    case 'YES'
        delete(obj)
    case 'NO' 
        return;
    otherwise
        return;
end
%-------------------------------------------------------------------------
````

</details>

#### 相似实现组 · MATLAB · ba302d0c

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：4
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：stepGASA.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索；按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`2644577c6902eb32d348adc73a91db2ff7d50d33a7987f930b7dc214a47be328`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/stepGASA.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/stepGASA.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/PopAnneal6.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/PopAnneal6.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [nextScore,nextPopulation,state] = stepGA(thisScore,thisPopulation,options,state,GenomeLength,FitnessFcn)
%STEPGA Moves the genetic algorithm forward by one generation
%   This function is private to GA.

%   Copyright 2003-2005 The MathWorks, Inc.
%   $Revision: 1.8.4.2 $  $Date: 2005/05/31 16:30:24 $

% how many crossover offspring will there be from each source?
nPop = size(thisPopulation,1);
nEliteKids = options.EliteCount;
nXoverKids = round(options.CrossoverFraction * (nPop - nEliteKids));
nMutateKids = nPop - nEliteKids - nXoverKids;
% how many parents will we need to complete the population?
nParents = 2 * nXoverKids + nMutateKids;

[unused,k] = sort(thisScore);
eliteKids  = thisPopulation(k(1:nEliteKids),:);

% decide who will contribute to the next generation
% fitness scaling
state.Expectation = feval(options.FitnessScalingFcn,thisScore,nParents,options.FitnessScalingFcnArgs{:});

% selection. parents are indicies into thispopulation
parents = feval(options.SelectionFcn,state.Expectation,nParents,options,options.SelectionFcnArgs{:});

% shuffle to prevent locality effects. It is not the responsibility
% if the selection function to return parents in a "good" order so
% we make sure there is a random order here.
parents = parents(randperm(length(parents)));
%parents = randperm(nParents);

% Everyones parents are stored here for genealogy display
state.Selection = [1:nEliteKids,parents]';

% here we make all of the members of the next generation
xoverKids  = feval(options.CrossoverFcn, parents(1:(2 * nXoverKids)),options,GenomeLength,FitnessFcn,thisScore,thisPopulation,options.CrossoverFcnArgs{:});
mutateKids = feval(options.MutationFcn,  parents((1 + 2 * nXoverKids):end), options,GenomeLength,FitnessFcn,state,thisScore,thisPopulation,options.MutationFcnArgs{:});

% group them into the next generation
Population = [ eliteKids ; xoverKids ; mutateKids ];

% score the population
%We want to add the vectorizer if fitness function is NOT vectorized
if strcmpi(options.Vectorized, 'off')
    Score = feval(@fcnvectorizer,Population,FitnessFcn,options.FitnessFcnArgs{:});
else
    Score = feval(FitnessFcn,Population,options.FitnessFcnArgs{:});
end

%[thisPopulation,thisScore] = gaFmin(options,GenomeLength,FitnessFcn,thisScore,thisPopulation);

%options.AnnealFcnArgs{:}
[nextPopulation,nextScore] = PopAnneal6(options,GenomeLength,FitnessFcn,state,Score,Population);

state.FunEval = state.FunEval + options.PopulationSize;
````

</details>

##### 变体 2：stepGASA4.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索；按温度和接受概率进行模拟退火搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`5aa45fd1d67353db6d032e030193cb1632c0ad38fe3a06158438d100e911a4bb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/stepGASA4.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/stepGASA4.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/PopAnneal4.m`
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/PopAnneal4.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [nextScore,nextPopulation,state] = stepGA(thisScore,thisPopulation,options,state,GenomeLength,FitnessFcn)
%STEPGA Moves the genetic algorithm forward by one generation
%   This function is private to GA.

%   Copyright 2003-2005 The MathWorks, Inc.
%   $Revision: 1.8.4.2 $  $Date: 2005/05/31 16:30:24 $

[thisPopulation,thisScore] = PopAnneal4(options,GenomeLength,FitnessFcn,state,thisScore,thisPopulation);

% how many crossover offspring will there be from each source?
nPop = size(thisPopulation,1);
nEliteKids = options.EliteCount;
nXoverKids = round(options.CrossoverFraction * (nPop - nEliteKids));
nMutateKids = nPop - nEliteKids - nXoverKids;
% how many parents will we need to complete the population?
nParents = 2 * nXoverKids + nMutateKids;

[unused,k] = sort(thisScore);
eliteKids  = thisPopulation(k(1:nEliteKids),:);

% decide who will contribute to the next generation
% fitness scaling
state.Expectation = feval(options.FitnessScalingFcn,thisScore,nParents,options.FitnessScalingFcnArgs{:});

% selection. parents are indicies into thispopulation
parents = feval(options.SelectionFcn,state.Expectation,nParents,options,options.SelectionFcnArgs{:});

% shuffle to prevent locality effects. It is not the responsibility
% if the selection function to return parents in a "good" order so
% we make sure there is a random order here.
parents = parents(randperm(length(parents)));
%parents = randperm(nParents);

% Everyones parents are stored here for genealogy display
state.Selection = [1:nEliteKids,parents]';

% here we make all of the members of the next generation
xoverKids  = feval(options.CrossoverFcn, parents(1:(2 * nXoverKids)),options,GenomeLength,FitnessFcn,thisScore,thisPopulation,options.CrossoverFcnArgs{:});
mutateKids = feval(options.MutationFcn,  parents((1 + 2 * nXoverKids):end), options,GenomeLength,FitnessFcn,state,thisScore,thisPopulation,options.MutationFcnArgs{:});

% group them into the next generation
nextPopulation = [ eliteKids ; xoverKids ; mutateKids ];

% score the population
%We want to add the vectorizer if fitness function is NOT vectorized
if strcmpi(options.Vectorized, 'off')
    nextScore = feval(@fcnvectorizer,nextPopulation,FitnessFcn,options.FitnessFcnArgs{:});
else
    nextScore = feval(FitnessFcn,nextPopulation,options.FitnessFcnArgs{:});
end

%options.AnnealFcnArgs{:}
state.FunEval = state.FunEval + options.PopulationSize;
````

</details>

#### validate · MATLAB · 9b83e170

- 归属算法：遗传算法GA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“核心算法与辅助函数”。
- **执行主线**：执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `functionHandleOrCell`、`functionHandleOrCellArray`、`nonNegInteger`、`nonNegScalar`、`populationCheck`、`positiveInteger`、`positiveIntegerArray`、`positiveScalar`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、文件结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`47e400ecf1d79ac67812cf9fedf6e2edfbb28cbb3f2564b66f1023f4b8a9f7bd`
- 语言：MATLAB
- 符号：`functionHandleOrCell`, `functionHandleOrCellArray`, `nonNegInteger`, `nonNegScalar`, `populationCheck`, `positiveInteger`, `positiveIntegerArray`, `positiveScalar`, `rangeCorrection`, `realScalar`, `realUnitScalar`, `stringSet`, `validNumberofVariables`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/遗传算法/遗传算法@遗传退火算法（算法简介+编程技巧+工具箱+应用大全）（含源代码）/遗传退火算法/代码区/validate.m`
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/遗传退火法/validate.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [gl,ff,o]  = validate(gLength,fitness,o)
%VALIDATE validates the contents of the fitness function, genome length and options struct.
%   [gLength,fitness, OUT] = VALIDATE(GenomeLength,FitnessFcn,IN) validates the FitnessFcn, GenomeLength and 
%   the structure IN. OUT is a structure which have all the fields in IN and it gets other 
%   fields like FitnessFcn, GenomeLength, etc.
%
%   This function is private to GA.

%   Copyright 2003-2005 The MathWorks, Inc.
%   $Revision: 1.26.6.5.2.1 $  $Date: 2005/07/17 06:06:36 $

msg = nargchk(3,3,nargin);
if ~isempty(msg)
    error('MATLAB:Validate:numInputs', ...
          'VALIDATE requires one structure of the format created by GAOPTIMSET.');
end

%We need to validate ALL the information, bundle them all
o.FitnessFcn   = fitness;
o.GenomeLength = gLength;
%gaoptimset does not return 2 fields, which need to be validated
options = gaoptimset;
options.FitnessFcn = [];
options.GenomeLength = [];

%Does the options structure contain the right fields?
template = fieldnames(options);
oFields = fieldnames(o);

f = find(0 == ismember(template,oFields));
if(~isempty(f))
    msg = sprintf('The field "%s" is missing from the gaoptimset Structure.\n',template{f});
    error('gads:VALIDATE:missingField',msg);
end

f = find(0 == ismember(oFields,template));
if(~isempty(f))
    msg = sprintf('There is an unexpected field "%s" in the gaoptimset Structure.\n',oFields{f});
    warning('gads:VALIDATE:unexpectedField',msg);
end

% range check each field
validNumberofVariables(o.GenomeLength);
stringSet('PopulationType',o.PopulationType,{'doubleVector','custom','bitString'});

positiveIntegerArray('PopulationSize',o.PopulationSize);
realUnitScalar('CrossoverFraction',o.CrossoverFraction);
nonNegInteger('EliteCount',o.EliteCount);
o = rangeCorrection(o,'PopInitRange');
populationCheck(o);

positiveInteger('MigrationInterval',o.MigrationInterval);
realUnitScalar('MigrationFraction',o.MigrationFraction);
stringSet('MigrationDirection',o.MigrationDirection,{'both','forward'});
stringSet('Display',o.Display,{'off','none','iter','final','diagnose'});
stringSet('Vectorized',o.Vectorized,{'on','off'});

nonNegScalar('TolFun',o.TolFun);
nonNegScalar('TolCon',o.TolCon);
positiveInteger('Generations',o.Generations);
positiveScalar('TimeLimit',o.TimeLimit);
positiveInteger('StallGenLimit',o.StallGenLimit);
positiveScalar('StallTimeLimit',o.StallTimeLimit);
realScalar('FitnessLimit',o.FitnessLimit);

positiveInteger('PlotInterval',o.PlotInterval);
% These functions not only VALIDATE, they seperate ftns from args for
% speed.
o = functionHandleOrCell(o,'FitnessFcn',o.FitnessFcn);
o = functionHandleOrCell(o,'FitnessScalingFcn',o.FitnessScalingFcn);
o = functionHandleOrCell(o,'SelectionFcn',o.SelectionFcn);
o = functionHandleOrCell(o,'CrossoverFcn',o.CrossoverFcn);
o = functionHandleOrCell(o,'MutationFcn',o.MutationFcn);
o = functionHandleOrCell(o,'CreationFcn',o.CreationFcn);

if ~isempty(o.HybridFcn)
    o = functionHandleOrCell(o,'HybridFcn',o.HybridFcn);
end

% protect against Elite Count greater than population Size.
if ( o.EliteCount >= sum(o.PopulationSize) )
    msg = sprintf('Elite count must be less than Population Size.');
    error('gads:VALIDATE:EliteCountGTPop',msg);
end

% this special case takes an array of function cells
o = functionHandleOrCellArray(o,'PlotFcns',o.PlotFcns);
o = functionHandleOrCellArray(o,'OutputFcns',o.OutputFcns);

%Assign all the outputs;
ff = o.FitnessFcn;
gl = o.GenomeLength;
%Remove these fields we added in options
o=rmfield(o,{'FitnessFcn','GenomeLength'});

%-------------------------------------------------------------------
% any positive integer
function positiveInteger(property,value)
valid =  isreal(value) && isscalar(value) && (value > 0) && (value == floor(value));
if(~valid)
   msg = sprintf('The field ''%s'' must contain a positive integer.',property);
   error('gads:VALIDATE:PostiveInteger:notPosInteger',msg);
end
%-------------------------------------------------------------------
% any nonnegative integer
function nonNegInteger(property,value)
valid =  isreal(value) && isscalar(value) && (value >= 0) && (value == floor(value));
if(~valid)
    msg = sprintf('The field ''%s'' must contain a non negative integer.',property);
    error('gads:VALIDATE:NonNegInteger:negativeNum',msg);
end
%-------------------------------------------------------------------
% any scalar >= 0
function nonNegScalar(property,value)
valid =  isreal(value) && isscalar(value) && (value >= 0);
if(~valid)
    msg = sprintf('The field ''%s'' must contain a scalar.',property);
    error('gads:VALIDATE:greaterEqualZeroScalar:lessThanZeroScalar',msg);
end
%-------------------------------------------------------------------
% any positive scalar
function positiveScalar(property,value)
valid =  isreal(value) && isscalar(value) && (value > 0);
if(~valid)
    msg = sprintf('The field ''%s'' must contain a positive scalar.',property);
    error('gads:VALIDATE:PositiveScalar:notPosScalar',msg);
end
%-------------------------------------------------------------------
function positiveIntegerArray(property,value)
allValid = true;
for i = 1:length(value)
    valid =  isreal(value(i)) && (value(i) == floor(value(i)));
    allValid = allValid && valid;
end

if(~valid)
    msg = sprintf('The field ''%s'' must contain a positive integer.',property);
    error('gads:VALIDATE:POSITIVEINTEGERARRAY:notPosIntegerArray',msg);
end
%-------------------------------------------------------------------
% A scalar on the interval [0,1]
function realUnitScalar(property,value)
valid = isreal(value) && isscalar(value) && (value >= 0) && (value <= 1);
if(~valid)
    msg = sprintf('The field ''%s'' must contain a scalar on the interval (0,1)',property);
    error('gads:VALIDATE:REALUNITSCALAR:notScalarOnUnitInterval',msg);
end
%-------------------------------------------------------------------
% A scalar
function realScalar(property,value)
valid = isreal(value) && isscalar(value);
if(~valid)
    msg = sprintf('The field ''%s'' must contain a scalar',property);
    error('gads:VALIDATE:REALSCALAR:notScalar',msg);
end
%-------------------------------------------------------------------
% Number of variables
function validNumberofVariables(GenomeLength)
valid =  isnumeric(GenomeLength) && isscalar(GenomeLength)&& (GenomeLength > 0) ...
         && (GenomeLength == floor(GenomeLength));
if(~valid)
   msg = sprintf('Number of variables (NVARS) must be a positive integer.');
   error('gads:VALIDATE:validNumberofVariables:notValidNvars',msg);
end

%-------------------------------------------------------------------------
% if it's a scalar fcn handle or a cellarray starting with a fcn handle and
% followed by something other than a fcn handle, return parts, else empty
function [handle,args] =  isFcn(x)
  handle = [];
  args = {};
%If x is a cell array with additional arguments, handle them
if iscell(x) && ~isempty(x)
    args = x(2:end);
    handle = x{1};
else
    args = {};
    handle = x;
end
%Only function_handle or inlines are allowed
if  ~(isa(handle,'inline') || isa(handle,'function_handle'))
    handle = [];
end

%-------------------------------------------------------------------
% a function Handle or a cell array starting with a function handle.
function options = functionHandleOrCell(options,property,value)
[handle,args] = isFcn(value);

if(~isempty(handle)) && (isa(handle,'inline') || isa(handle,'function_handle'))
    options.(property) = handle;
    options.([property 'Args']) = args;
    return
end

if strcmp(property,'FitnessFcn')
    msg = sprintf('The fitness function must be a function handle.');
else
    msg = sprintf('The field ''%s'' must contain a function handle.',property);
end

error('gads:VALIDATE:FUNCTIONHANDLEORCELL:needHandleOrInline',msg);

%---------------------------------------------------------------------
% the most complex one. A fcn handle, a handle plus args, or an array of
% same.
function options = functionHandleOrCellArray(options,property,value)

% clear out any old value
options.(property) = {};
options.([property 'Args']) = {};

%if a scalar  ~cell  is passed convert to cell (for clarity, not speed)
if ~iscell(value) && isscalar(value)
     value = {value};
 end
% If value is an array of functions, it must be a cell array
for i = 1:length(value)
    candidate = value(i);
    %If any element is also a cell array
    if iscell(candidate)
        if isempty(candidate{1})
            continue;
        end
        %Sometimes the variable 'candidate' might have nested cell array 
        %e.g. {{@outputfcn, p1,p2}} instead of just
        %{@outputfcn,p1,p2}. The following code gets rid of extra braces,
        %which are typically introduced by GUI import/export options.
        temp = candidate{1};
        while iscell(temp) && isscalar(temp)
            candidate = temp(1);
            temp = candidate{1};
        end
        [handle,args] = isFcn(candidate{:});
    else
        [handle,args] = isFcn(candidate);
    end
    if(~isempty(handle)) && isa(handle,'function_handle')
        options.(property){i} = handle;
        options.([property 'Args']){i} = args;
    else
        msg = sprintf('The field ''%s'' must contain a function handle.',property);
        error('gads:VALIDATE:FUNCTIONHANDLEORCELLARRAY:needHandleOrInline',msg);
    end
end
%----------------------------------------------------------------
% one of a set of strings
function stringSet(property,value,set)
for i = 1:length(set)
    if(strcmpi(value,set{i}))
        return;
    end
end

msg = sprintf('The field %s must contain one of these strings: %s %s %s %s %s',property,set{:});
error('gads:VALIDATE:STRINGSET:notCorrectChoice',msg);
%----------------------------------------------------------------
function options = rangeCorrection(options,property)

%Check the size of PopInitRange
Range = options.PopInitRange;
%check only for double data type range
if ~isa(Range,'double')
    return;
end

if size(Range,1) ~=2
    msg = sprintf('The field ''%s'' must have two rows.',property);
    error('gads:VALIDATE:RANGECORRECTION:invalidPopInitRange',msg);  
end
lb = Range(1,:);
lb = lb(:);
lenlb = length(lb);
ub = Range(2,:);
ub = ub(:);
lenub = length(ub);
nvars = options.GenomeLength; %This field was inserted

% Check maximum length
if lenlb > nvars
   warning('gads:VALIDATE:extraRange','Length of lower range is > number of variables; ignoring extra bounds.');
   lb = lb(1:nvars);   
   lenlb = nvars;
elseif lenlb < nvars
   lb = [lb; lb(end)*ones(nvars-lenlb,1)];
   lenlb = nvars;
end

if lenub > nvars
   warning('gads:VALIDATE:extraRange','Length of upper range is > number of variables; ignoring extra bounds.');
   ub = ub(1:nvars);
   lenub = nvars;
elseif lenub < nvars
   ub = [ub; ub(end)*ones(nvars-lenub,1)];
   lenub = nvars;
end
% Check feasibility of bounds
len = min(lenlb,lenub);
if any( lb( (1:len)' ) > ub( (1:len)' ) )
   count = full(sum(lb>ub));
   if count == 1
      msg=sprintf(['\nExiting due to infeasibility:  %i lower range exceeds the' ...
            ' corresponding upper range.\n'],count);
   else
      msg=sprintf(['\nExiting due to infeasibility:  %i lower range exceed the' ...
            ' corresponding upper range.\n'],count);
   end
   error('gads:validate:infesibleRange',msg);
end
% check if -inf in ub or inf in lb   
if any(eq(ub, -inf)) 
   error('gads:VALIDATE:infRange','-Inf detected in upper bound: upper bounds must be > -Inf.');
elseif any(eq(lb,inf))
   error('gads:VALIDATE:infRange','+Inf detected in lower bound: lower bounds must be < Inf.');
end

options.PopInitRange = [lb,ub]';
%------------------------------End of rangeCorrection --------------------------

function populationCheck(options)
%Perform some check if Population type is double or bitString
if strcmpi(options.PopulationType,'custom')
    return;
end
if ~isnumeric(gaoptimget(options,'InitialPopulation'))
    error('gads:VALIDATE:invalidPopulation','Invalid value for OPTIONS parameter InitialPopulation.');
end
if ~isnumeric(gaoptimget(options,'InitialScores'))
    error('gads:VALIDATE:invalidScores','Invalid value for OPTIONS parameter InitialScores.');
end
%------------------------------End of populationCheck --------------------------
````

</details>

#### 智能算法之遗传算法代码 · MATLAB · fd246a28

- 归属算法：遗传算法GA
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#遗传算法GA · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于遗传算法GA中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `calfitvalue`、`decodebinary`、`decodechrom`、`genmain`、`initpop`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`d0cfb87da9901dc87d91290a186cff81e6e02e6714bfdbdc4ed7951e1e423da8`
- 语言：MATLAB
- 符号：`calfitvalue`, `decodebinary`, `decodechrom`, `genmain`, `initpop`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/智能算法之遗传算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
% 求下列函数的最大值 %
% f(x)=10*sin(5x)+7*cos(4x) x∈[0,10] %
% 将 x 的值用一个10位的二值形式表示为二值问题，一个10位的二值数提供的分辨率是每为 (10-0)/(2^10-1)≈0.01 。 %
% 将变量域 [0,10] 离散化为二值域 [0,1023], x=0+10*b/1023, 其中 b 是 [0,1023] 中的一个二值数。 %
% %
%--------------------------------------------------------------------------------------------------------------%
%--------------------------------------------------------------------------------------------------------------%
% 编程
%-----------------------------------------------
% 2.8 主程序
%遗传算法主程序
%Name:genmain05.m
function genmain()
tic;
clear
clf
popsize=20; %群体大小
chromlength=10; %字符串长度（个体长度）
pc=0.6; %交叉概率
pm=0.001; %变异概率

pop=initpop(popsize,chromlength); %随机产生初始群体
for i=1:20 %20为迭代次数
[objvalue]=calobjvalue(pop); %计算目标函数
fitvalue=calfitvalue(objvalue); %计算群体中每个个体的适应度
[newpop]=selection(pop,fitvalue); %复制
[newpop]=crossover(pop,pc); %交叉
[newpop]=mutation(pop,pc); %变异
[bestindividual,bestfit]=best(pop,fitvalue); %求出群体中适应值最大的个体及其适应值
y(i)=max(bestfit);
n(i)=i;
pop5=bestindividual;
x(i)=decodechrom(pop5,1,chromlength)*10/1023;
pop=newpop;
end

fplot('10*sin(5*x)+7*cos(4*x)',[0 10])
hold on
plot(x,y,'r*')
hold off

[z index]=max(y); %计算最大值及其位置
x5=x(index)%计算最大值对应的x值
y=z
toc

% 2.1初始化(编码)
% initpop.m函数的功能是实现群体的初始化，popsize表示群体的大小，chromlength表示染色体的长度(二值数的长度)，
% 长度大小取决于变量的二进制编码的长度(在本例中取10位)。
%遗传算法子程序
%Name: initpop.m
%初始化

function pop=initpop(popsize,chromlength) 
pop=round(rand(popsize,chromlength)) % rand随机产生每个单元为 {0,1} 行数为popsize，列数为chromlength的矩阵，
% roud对矩阵的每个单元进行圆整。这样产生的初始种群。

% 2.2 计算目标函数值
% 2.2.1 将二进制数转化为十进制数(1)
%遗传算法子程序
%Name: decodebinary.m
%产生 [2^n 2^(n-1) ... 1] 的行向量，然后求和，将二进制转化为十进制
function pop2=decodebinary(pop)
[px,py]=size(pop); %求pop行和列数
for i=1:py
pop1(:,i)=2.^(py-i).*pop(:,i);
end
pop2=sum(pop1,2); %求pop1的每行之和

% 2.2.2 将二进制编码转化为十进制数(2)
% decodechrom.m函数的功能是将染色体(或二进制编码)转换为十进制，参数spoint表示待解码的二进制串的起始位置
% (对于多个变量而言，如有两个变量，采用20为表示，每个变量10为，则第一个变量从1开始，另一个变量从11开始。本例为1)，
% 参数1ength表示所截取的长度（本例为10）。
%遗传算法子程序
%Name: decodechrom.m
%将二进制编码转换成十进制
function pop2=decodechrom(pop,spoint,length)
pop1=pop(:,spoint:spoint+length-1);
pop2=decodebinary(pop1);

% 2.2.3 计算目标函数值
% calobjvalue.m函数的功能是实现目标函数的计算，其公式采用本文示例仿真，可根据不同优化问题予以修改。
%遗传算法子程序
%Name: calobjvalue.m
%实现目标函数的计算
function [objvalue]=calobjvalue(pop)
temp1=decodechrom(pop,1,10); %将pop每行转化成十进制数
x=temp1*10/1023; %将二值域 中的数转化为变量域 的数
objvalue=10*sin(5*x)+7*cos(4*x); %计算目标函数值

% 2.3 计算个体的适应值
%遗传算法子程序
%Name:calfitvalue.m
%计算个体的适应值
function fitvalue=calfitvalue(objvalue)
global Cmin;
Cmin=0;
[px,py]=size(objvalue);
for i=1:px
if objvalue(i)+Cmin>0
temp=Cmin+objvalue(i);
else
temp=0.0;
end
fitvalue(i)=temp;
end
fitvalue=fitvalue';

% 2.4 选择复制
% 选择或复制操作是决定哪些个体可以进入下一代。程序中采用赌轮盘选择法选择，这种方法较易实现。
% 根据方程 pi=fi/∑fi=fi/fsum ，选择步骤：
% 1） 在第 t 代，由（1）式计算 fsum 和 pi 
% 2） 产生 {0,1} 的随机数 rand( .)，求 s=rand( .)*fsum
% 3） 求 ∑fi≥s 中最小的 k ，则第 k 个个体被选中
% 4） 进行 N 次2）、3）操作，得到 N 个个体，成为第 t=t+1 代种群
%遗传算法子程序
%Name: selection.m
%选择复制
function [newpop]=selection(pop,fitvalue)
totalfit=sum(fitvalue); %求适应值之和
fitvalue=fitvalue/totalfit; %单个个体被选择的概率
fitvalue=cumsum(fitvalue); %如 fitvalue=[1 2 3 4]，则 cumsum(fitvalue)=[1 3 6 10] 
[px,py]=size(pop);
ms=sort(rand(px,1)); %从小到大排列
fitin=1;
newin=1;
while newin<=px
if(ms(newin))<fitvalue(fitin)
newpop(newin)=pop(fitin);
newin=newin+1;
else
fitin=fitin+1;
end
end

% 2.5 交叉
% 交叉(crossover)，群体中的每个个体之间都以一定的概率 pc 交叉，即两个个体从各自字符串的某一位置
% （一般是随机确定）开始互相交换，这类似生物进化过程中的基因分裂与重组。例如，假设2个父代个体x1，x2为：
% x1=0100110
% x2=1010001
% 从每个个体的第3位开始交叉，交又后得到2个新的子代个体y1，y2分别为：
% y1＝0100001
% y2＝1010110
% 这样2个子代个体就分别具有了2个父代个体的某些特征。利用交又我们有可能由父代个体在子代组合成具有更高适合度的个体。
% 事实上交又是遗传算法区别于其它传统优化方法的主要特点之一。
%遗传算法子程序
%Name: crossover.m
%交叉
function [newpop]=crossover(pop,pc)
[px,py]=size(pop);
newpop=ones(size(pop));
for i=1:2:px-1
if(rand<pc)
cpoint=round(rand*py);
newpop(i,:)=[pop(i,1:cpoint),pop(i+1,cpoint+1:py)];
newpop(i+1,:)=[pop(i+1,1:cpoint),pop(i,cpoint+1:py)];
else
newpop(i,:)=pop(i);
newpop(i+1,:)=pop(i+1);
end
end

% 2.6 变异
% 变异(mutation)，基因的突变普遍存在于生物的进化过程中。变异是指父代中的每个个体的每一位都以概率 pm 翻转，即由“1”变为“0”，
% 或由“0”变为“1”。遗传算法的变异特性可以使求解过程随机地搜索到解可能存在的整个空间，因此可以在一定程度上求得全局最优解。
%遗传算法子程序
%Name: mutation.m
%变异
function [newpop]=mutation(pop,pm)
[px,py]=size(pop);
newpop=ones(size(pop));
for i=1:px
if(rand<pm)
mpoint=round(rand*py);
if mpoint<=0
mpoint=1;
end
newpop(i)=pop(i);
if any(newpop(i,mpoint))==0
newpop(i,mpoint)=1;
else
newpop(i,mpoint)=0;
end
else
newpop(i)=pop(i);
end
end

% 2.7 求出群体中最大得适应值及其个体
%遗传算法子程序
%Name: best.m
%求出群体中适应值最大的值
function [bestindividual,bestfit]=best(pop,fitvalue)
[px,py]=size(pop);
bestindividual=pop(1,:);
bestfit=fitvalue(1);
for i=2:px
if fitvalue(i)>bestfit
bestindividual=pop(i,:);
bestfit=fitvalue(i);
end
end
````

</details>

<!-- END AUTO-INTEGRATED-CODE -->
