---
type: generated-code-shard
status: generated
topic_hub: 智能优化 Hub
algorithm: 模拟退火SA
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# 模拟退火SA · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub|智能优化 Hub]]
- 独立实现：125
- 原始来源：286
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

通过温度下降和概率接受劣解跳出局部最优。

#### TM · MATLAB · 0eabe22b

- 归属算法：模拟退火SA
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：3
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#模拟退火SA · 复习|模拟退火SA · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
