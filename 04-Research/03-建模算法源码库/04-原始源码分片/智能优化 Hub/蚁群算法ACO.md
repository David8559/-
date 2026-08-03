---
type: generated-code-shard
status: generated
topic_hub: 智能优化 Hub
algorithm: 蚁群算法ACO
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# 蚁群算法ACO · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub|智能优化 Hub]]
- 独立实现：1
- 原始来源：1
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

#### 蚁群算法matlab源码 · MATLAB · e3cd9190

- 归属算法：蚁群算法ACO
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/06-智能优化算法/智能优化 Hub#蚁群算法ACO · 复习|蚁群算法ACO · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
