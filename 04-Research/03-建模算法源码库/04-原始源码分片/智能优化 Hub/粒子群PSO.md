---
type: generated-code-shard
status: generated
topic_hub: 智能优化 Hub
algorithm: 粒子群PSO
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# 粒子群PSO · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub|智能优化 Hub]]
- 独立实现：12
- 原始来源：16
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

使用群体位置与速度更新进行连续或组合空间搜索。

#### DeJong · MATLAB · c7f9552f

- 归属算法：粒子群PSO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：2
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#粒子群PSO · 复习|粒子群PSO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
