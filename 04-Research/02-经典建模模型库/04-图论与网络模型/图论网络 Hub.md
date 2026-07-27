---
type: topic-hub
topic_tag: topic/图论网络
keywords: [图论, 最短路径, 生成树, 最大流]
tags: [system/topic-hub, topic/图论网络]
---

# 图论网络 Hub

<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->
## 复习与调用指南

> [!summary] 阅读顺序
> 先用“快速选择”确定算法，再读复习卡掌握思想和步骤，最后跳到实现区选择代码。源码默认折叠；数据明细不在复习页展开。

### 快速选择

| 算法或用途 | 主要解决什么 | 独立实现 | 语言 |
|---|---|---:|---|
| [[#Dijkstra最短路 · 复习|Dijkstra最短路]] | 求非负权图的单源最短路径。 | 9 | C++, MATLAB, Python |
| [[#Floyd最短路 · 复习|Floyd最短路]] | 求任意两点之间的最短距离和路径。 | 6 | LINGO, MATLAB, Python |
| [[#图与网络综合例程 · 复习|图与网络综合例程]] | 把实体与关系抽象为节点、边和权重后完成路径、连通或流量分析。 | 6 | MATLAB |
| [[#图论与排队 · 复习|图论与排队]] | 汇总图网络与服务系统中的路径、连通、流量和等待问题。 | 21 | MATLAB, Python |
| [[#最小生成树 · 复习|最小生成树]] | 以最小总权连接无向图全部节点。 | 4 | MATLAB, Python |
| [[#网络流 · 复习|网络流]] | 在容量限制网络中求最大流、最小费用流或匹配。 | 5 | LINGO, MATLAB, Python |

### 逐算法复习卡

#### Dijkstra最短路 · 复习

- **解决什么**：求非负权图的单源最短路径。
- **核心思想**：每次永久标记当前距离最小的未访问节点并松弛邻边。
- **标准流程**：建邻接表/矩阵 → 初始化距离 → 优先队列迭代 → 记录前驱 → 回溯路径。
- **何时调用**：边权非负且需要单源路径时优先。
- **最易出错**：存在负权边时不能使用；注意不可达节点和有向性。
- **库内覆盖**：9 个独立实现、9 个原始来源；语言：C++, MATLAB, Python；其中 1 个识别到函数/类型入口。
- **优先阅读**：[[#ex4_11 · MATLAB · 95525d20|ex4_11]]、[[#mydijkstra · Python · 08b68c5f|mydijkstra]]、[[#ex4_10 · MATLAB · a3948441|ex4_10]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#Dijkstra最短路 · 实现|跳转到源码实现区]]

#### Floyd最短路 · 复习

- **解决什么**：求任意两点之间的最短距离和路径。
- **核心思想**：以中间节点为阶段进行三重动态规划。
- **标准流程**：初始化距离/前驱矩阵 → 枚举中间点 → 更新距离 → 检查负环 → 重建路径。
- **何时调用**：节点数中小且需要全源最短路时使用。
- **最易出错**：时间复杂度O(n³)，无穷大初始化和路径矩阵最容易出错。
- **库内覆盖**：6 个独立实现、6 个原始来源；语言：LINGO, MATLAB, Python；其中 4 个识别到函数/类型入口。
- **优先阅读**：[[#anli4_1_1 · LINGO · 989227cb|anli4_1_1]]、[[#anli4_1_2 · LINGO · 82bd1630|anli4_1_2]]、[[#Pex10_7 · Python · 2df171f4|Pex10_7]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#Floyd最短路 · 实现|跳转到源码实现区]]

#### 图与网络综合例程 · 复习

- **解决什么**：把实体与关系抽象为节点、边和权重后完成路径、连通或流量分析。
- **核心思想**：邻接结构、方向和权重定义决定可调用的图算法。
- **标准流程**：定义节点/边 → 建图 → 判断问题类型 → 选择最短路/生成树/网络流 → 重建结果 → 图示验证。
- **何时调用**：问题的核心是关系结构而非单纯表格计算时使用。
- **最易出错**：先核对有向/无向、权重意义和不可达状态，再选择算法。
- **库内覆盖**：6 个独立实现、6 个原始来源；语言：MATLAB；其中 1 个识别到函数/类型入口。
- **优先阅读**：[[#main · MATLAB · 41d01094|main]]、[[#ex4_1 · MATLAB · 76ded227|ex4_1]]、[[#ex4_4 · MATLAB · 3b0568a8|ex4_4]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#图与网络综合例程 · 实现|跳转到源码实现区]]

#### 图论与排队 · 复习

- **解决什么**：汇总图网络与服务系统中的路径、连通、流量和等待问题。
- **核心思想**：根据关系网络或随机服务机制选择不同子模型。
- **标准流程**：识别问题结构 → 建图或队列参数 → 选具体算法 → 求解 → 用路径/守恒/稳定条件验算。
- **何时调用**：作为入口使用，不能把不同图算法或排队模型混为一类。
- **最易出错**：必须下钻到具体算法卡确认假设与复杂度。
- **库内覆盖**：21 个独立实现、21 个原始来源；语言：MATLAB, Python；其中 8 个识别到函数/类型入口。
- **优先阅读**：[[#floydpath · MATLAB · 1a51c231|floydpath]]、[[#相似实现组 · Python · c2f0a841|Pex10_5]]、[[#mydijkstra · MATLAB · 8ee5fec3|mydijkstra]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#图论与排队 · 实现|跳转到源码实现区]]

#### 最小生成树 · 复习

- **解决什么**：以最小总权连接无向图全部节点。
- **核心思想**：Prim扩展已选节点集合，Kruskal按边权合并连通分量。
- **标准流程**：检查连通性 → 选Prim/Kruskal → 维护候选边/并查集 → 输出树边 → 验证n-1条边。
- **何时调用**：网络铺设、聚类骨架和最低连接成本。
- **最易出错**：它最小化总连接成本，不保证任意两点路径最短。
- **库内覆盖**：4 个独立实现、4 个原始来源；语言：MATLAB, Python；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#ex4_12 · MATLAB · ac643fc2|ex4_12]]、[[#中国数学建模-编程交流-贪婪算法_2 · MATLAB · cf419820|中国数学建模-编程交流-贪婪算法_2]]、[[#Pex10_13 · Python · 4c4628f1|Pex10_13]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#最小生成树 · 实现|跳转到源码实现区]]

#### 网络流 · 复习

- **解决什么**：在容量限制网络中求最大流、最小费用流或匹配。
- **核心思想**：流守恒、容量约束和增广路径构成核心。
- **标准流程**：建有向容量图 → 设源汇 → 增广/分层 → 更新残量网络 → 读最小割。
- **何时调用**：运输、指派、匹配和资源流转问题。
- **最易出错**：方向、反向边、容量单位和源汇定义必须核对。
- **库内覆盖**：5 个独立实现、5 个原始来源；语言：LINGO, MATLAB, Python；其中 2 个识别到函数/类型入口。
- **优先阅读**：[[#mainexample19 · MATLAB · fd75c78f|mainexample19]]、[[#mincostmaxflow · MATLAB · 94e91832|mincostmaxflow]]、[[#Pex10_16 · Python · bae89d16|Pex10_16]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#网络流 · 实现|跳转到源码实现区]]

### 通用调用检查表

1. 先确认当前问题是否满足复习卡中的适用条件。
2. 优先选择标有函数/类型入口的实现，脚本型代码先重构参数。
3. 用最小样例跑通，再替换为项目输入；不要一开始就接入完整题目。
4. 检查目标方向、变量单位、边界条件、随机种子和软件版本。
5. 保存运行环境、参数、结果与检验，验证通过后再进入项目正式代码。

<!-- END AUTO-HUB-STUDY-GUIDE -->

> 自动更新：2026-07-27 · 匹配笔记：5

## 相关笔记

- [[04-Research/03-建模算法源码库/代码资料索引]] — 相关度 6
- [[04-Research/04-竞赛真题研究/01-全国大学生数学建模竞赛/2020-B题-穿越沙漠/2020-B题-穿越沙漠-题目总览]] — 相关度 3
- [[04-Research/04-竞赛真题研究/01-全国大学生数学建模竞赛/2020-B题-穿越沙漠/2020-B题-B078第四关地图与邻接关系]] — 相关度 2
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B078-论文拆解]] — 相关度 2
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B125-论文拆解]] — 相关度 2

## 邻接主题

- [[Topic Index]]
- [[优化模型 Hub]]
- [[动态规划 Hub]]
- [[可视化 Hub]]

<!-- BEGIN AUTO-INTEGRATED-CODE -->
## 源码实现库（按需调用）

> [!warning] 使用边界
> 以下源码保留全文与来源，但默认均未运行验证。数据依赖明细已从阅读页省略；调用时按代码理解卡完成参数化、最小样例和结果检验。来源显示为可复制路径，不直接调用 Windows 打开未知扩展名。

- 本 Hub 收录原始源码文件：51
- 精确去重后的独立实现：51
- 合并后的实现组：45

### 实现索引

| 算法或用途 | 独立实现 | 原始源码 |
|---|---:|---:|
| [[#Dijkstra最短路 · 实现|Dijkstra最短路]] | 9 | 9 |
| [[#Floyd最短路 · 实现|Floyd最短路]] | 6 | 6 |
| [[#图与网络综合例程 · 实现|图与网络综合例程]] | 6 | 6 |
| [[#图论与排队 · 实现|图论与排队]] | 21 | 21 |
| [[#最小生成树 · 实现|最小生成树]] | 4 | 4 |
| [[#网络流 · 实现|网络流]] | 5 | 5 |

### Dijkstra最短路 · 实现

求非负权图中单源最短路径。

#### ex4_10 · MATLAB · a3948441

- 归属算法：Dijkstra最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Dijkstra最短路中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：使用旧版接口，运行前检查当前软件兼容性。

- SHA-256：`120233de26e6c953f935623402a7b338d8c1d2cd87626b778198ea06fa2fb688`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_10.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=[1 1 1 1;1 1 1 0;1 1 0 1;1 0 1 1;1 0 1 0
   0 1 0 1;0 1 0 0;0 0 1 0;0 0 0 1; 0 0 0 0]; %每一行是一个可行状态
b=[1 0 0 0;1 1 0 0;1 0 1 0;1 0 0 1]; %每一行是一个转移状态
w=zeros(10); %邻接矩阵初始化
for i=1:9
    for j=i+1:10
        for k=1:4
            if findstr(mod(a(i,:)+b(k,:),2),a(j,:))
                w(i,j)=1;
            end
        end
    end
end
w=w'; %变成下三角矩阵
[i,j,v]=find(w);  %找非零元素
c=sparse(i,j,v,10,10) %构造稀疏矩阵
[x,y,z]=graphshortestpath(c,1,10,'Directed',false)  % 该图是无向图
h = view(biograph(c,[],'ShowArrows','off','ShowWeights','off'));
Edges = getedgesbynodeid(h); %提取句柄h中的边集
set(Edges,'LineColor',[0 0 0]); %为了将来打印清楚，边画成黑色
set(Edges,'LineWidth',1.5);  %线型宽度设置为1.5
````

</details>

#### ex4_11 · MATLAB · 95525d20

- 归属算法：Dijkstra最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Dijkstra最短路中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：使用旧版接口，运行前检查当前软件兼容性。

- SHA-256：`207698fa9ee620430d0991320da4343ea621fae9c3dad8bec2c819e24fbebb96`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_11.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=zeros(7);
a(1,2)=4; a(1,3)=2;
a(2,3)=3; a(2,4)=2; a(2,5)=6;
a(3,4)=5; a(3,6)=4;
a(4,5)=2; a(4,6)=7;
a(5,6)=4; a(5,7)=8;
a(6,7)=3;
b=sparse(a); %构造稀疏矩阵，这里给出构造稀疏矩阵的另一种方法
[x,y,z]=graphshortestpath(b,1,7,'Directed',true,'Method','Dijkstra')  % Directed是有向的
h=view(biograph(b,[],'ShowArrows','on','ShowWeights','on'))
````

</details>

#### ex4_9 · MATLAB · 300072c1

- 归属算法：Dijkstra最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Dijkstra最短路中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：使用旧版接口，运行前检查当前软件兼容性。

- SHA-256：`b56eb2d516a727b5bbadcc71940ae59abdb4ed274e9b9a4b3853dd2ce60120d3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_9.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a(1,2)=2;a(1,3)=8;a(1,4)=1;
a(2,3)=1;a(2,3)=6;a(2,5)=1;
a(3,4)=7;a(3,5)=5;a(3,6)=1;a(3,7)=2;
a(4,7)=9;
a(5,6)=3;a(5,8)=2;a(5,9)=9;
a(6,7)=4;a(6,9)=6;
a(7,9)=3;a(7,10)=1;
a(8,9)=7;a(8,11)=9;
a(9,10)=1;a(9,11)=2;
a(10,11)=4;
a=a';   %matlab工具箱要求数据是下三角矩阵
[i,j,v]=find(a);
b=sparse(i,j,v,11,11) %构造稀疏矩阵
[x,y,z]=graphshortestpath(b,1,11,'Directed',false) % Directed是标志图为有向或无向的属性，该图是无向图，对应的属性值为false，或0。
````

</details>

#### dijk · C++ · fa51b5e0

- 归属算法：Dijkstra最短路
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Dijkstra最短路中的“结果绘图与展示”。
- **执行主线**：通过松弛操作求单源最短路径；选择低权边构造最小生成树；重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、控制台/过程输出、图形
- **调用风险**：包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`2dfbc31cb362c44c4918a2aec01cd029f8451b17392ad7da602ebab960a026fa`
- 语言：C++
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/dijkstra  c++程序/dijk.txt`

<details>
<summary>展开原始代码</summary>

````cpp
Dijkstra算法 
开放分类： 算法、单源最短路径

关于 Dijkstra算法解决voronoi图的问题
macrolian 发表于: 2008-5-03 19:36 来源: Matlab中文学习站 

我想用 Dijkstra算法解决voronoi图中求解最短路径的时候,有一个"dijkstra.m"的文件
代码如下:function [dist,path] = dijkstra(nodes,segments,start_id,finish_id)
%DIJKSTRA Calculates the shortest distance and path between points on a map
%   using Dijkstra's Shortest Path Algorithm
% 
% [DIST, PATH] = DIJKSTRA(NODES, SEGMENTS, SID, FID)
%   Calculates the shortest distance and path between start and finish nodes SID and FID
% 
% [DIST, PATH] = DIJKSTRA(NODES, SEGMENTS, SID)
%   Calculates the shortest distances and paths from the starting node SID to all
%     other nodes in the map
% 
% Note:
%     DIJKSTRA is set up so that an example is created if no inputs are provided,
%       but ignores the example and just processes the inputs if they are given.
% 
% Inputs:
%     NODES should be an Nx3 or Nx4 matrix with the format [ID X Y] or [ID X Y Z]
%       where ID is an integer, and X, Y, Z are cartesian position coordinates)
%     SEGMENTS should be an Mx3 matrix with the format [ID N1 N2]
%       where ID is an integer, and N1, N2 correspond to node IDs from NODES list
%       such that there is an [undirected] edge/segment between node N1 and node N2
%     SID should be an integer in the node ID list corresponding with the starting node
%     FID (optional) should be an integer in the node ID list corresponding with the finish
% 
% Outputs:
%     DIST is the shortest Euclidean distance
%       If FID was specified, DIST will be a 1x1 double representing the shortest
%         Euclidean distance between SID and FID along the map segments. DIST will have
%         a value of INF if there are no segments connecting SID and FID.
%       If FID was not specified, DIST will be a 1xN vector representing the shortest
%         Euclidean distance between SID and all other nodes on the map. DIST will have
%         a value of INF for any nodes that cannot be reached along segments of the map.
%     PATH is a list of nodes containing the shortest route
%       If FID was specified, PATH will be a 1xP vector of node IDs from SID to FID.
%         NAN will be returned if there are no segments connecting SID to FID.
%       If FID was not specified, PATH will be a 1xN cell of vectors representing the
%         shortest route from SID to all other nodes on the map. PATH will have a value
%         of NAN for any nodes that cannot be reached along the segments of the map.
% 
% Example:
%     dijkstra; % calculates shortest path and distance between two nodes
%               % on a map of randomly generated nodes and segments
% 
% Example:
%     nodes = [(1:10); 100*rand(2,10)]';
%     segments = [(1:17); floor(1:0.5:9); ceil(2:0.5:10)]';
%     figure; plot(nodes(:,2), nodes(:,3),'k.');
%     hold on;
%     for s = 1:17
%         if (s &lt;= 10) text(nodes(s,2),nodes(s,3),[' ' num2str(s)]); end
%         plot(nodes(segments(s,2:3)',2),nodes(segments(s,2:3)',3),'k');
%     end
%     [d, p] = dijkstra(nodes, segments, 1, 10)
%     for n = 2:length(p)
%         plot(nodes(p(n-1:n),2),nodes(p(n-1:n),3),'r-.','linewidth',2);
%     end
%     hold off;
% 
% Author: Joseph Kirk
% Email: jdkirk630 at gmail dot com
% Release: 1.3
% Release Date: 5/18/07
if (nargin &lt; 3) % SETUP
    % (GENERATE RANDOM EXAMPLE OF NODES AND SEGMENTS IF NOT GIVEN AS INPUTS)
    % Create a random set of nodes/vertices,and connect some of them with
    % edges/segments. Then graph the resulting map.
    num_nodes = 40; L = 100; max_seg_length = 30; ids = (1:num_nodes)';
    nodes = [ids L*rand(num_nodes,2)]; % create random nodes
    h = figure; plot(nodes(:,2),nodes(:,3),'k.') % plot the nodes
    text(nodes(num_nodes,2),nodes(num_nodes,3),...
        [' ' num2str(ids(num_nodes))],'Color','b','FontWeight','b')
    hold on
    num_segs = 0; segments = zeros(num_nodes*(num_nodes-1)/2,3);
    for i = 1:num_nodes-1 % create edges between some of the nodes
        text(nodes(i,2),nodes(i,3),[' ' num2str(ids(i))],'Color','b','FontWeight','b')
        for j = i+1:num_nodes
            d = sqrt(sum((nodes(i,2:3) - nodes(j,2:3)).^2));
            if and(d &lt; max_seg_length,rand &lt; 0.6)
                plot([nodes(i,2) nodes(j,2)],[nodes(i,3) nodes(j,3)],'k.-')
                % add this link to the segments list
                num_segs = num_segs + 1;
                segments(num_segs, = [num_segs nodes(i,1) nodes(j,1)];
            end
        end
    end
    segments(num_segs+1:num_nodes*(num_nodes-1)/2, = [];
    axis([0 L 0 L])
    % Calculate Shortest Path Using Dijkstra's Algorithm
    % Get random starting/ending nodes,compute the shortest distance and path.
    start_id = ceil(num_nodes*rand); disp(['start id = ' num2str(start_id)]);
    finish_id = ceil(num_nodes*rand); disp(['finish id = ' num2str(finish_id)]);
    [distance,path] = dijkstra(nodes,segments,start_id,finish_id);
    disp(['distance = ' num2str(distance)]); disp(['path = [' num2str(path) ']']);
    % If a Shortest Path exists,Plot it on the Map.
    figure(h)
    for k = 2:length(path)
        m = find(nodes(:,1) == path(k-1));
        n = find(nodes(:,1) == path(k));
        plot([nodes(m,2) nodes(n,2)],[nodes(m,3) nodes(n,3)],'ro-','LineWidth',2);
    end
    title(['Shortest Distance from ' num2str(start_id) ' to ' ...
        num2str(finish_id) ' = ' num2str(distance)])
    hold off
    
else %--------------------------------------------------------------------------
    % MAIN FUNCTION - DIJKSTRA'S ALGORITHM
    
    % initializations
    node_ids = nodes(:,1);
    [num_map_pts,cols] = size(nodes);
    table = sparse(num_map_pts,2);
    shortest_distance = Inf(num_map_pts,1);
    settled = zeros(num_map_pts,1);
    path = num2cell(NaN(num_map_pts,1));
    col = 2;
    pidx = find(start_id == node_ids);
    shortest_distance(pidx) = 0;
    table(pidx,col) = 0;
    settled(pidx) = 1;
    path(pidx) = {start_id};
    if (nargin &lt; 4) % compute shortest path for all nodes
        while_cmd = 'sum(~settled) &gt; 0';
    else % terminate algorithm early
        while_cmd = 'settled(zz) == 0';
        zz = find(finish_id == node_ids);
    end
    while eval(while_cmd)
        % update the table
        table(:,col-1) = table(:,col);
        table(pidx,col) = 0;
        % find neighboring nodes in the segments list
        neighbor_ids = [segments(node_ids(pidx) == segments(:,2),3);
            segments(node_ids(pidx) == segments(:,3),2)];
        % calculate the distances to the neighboring nodes and keep track of the paths
        for k = 1:length(neighbor_ids)
            cidx = find(neighbor_ids(k) == node_ids);
            if ~settled(cidx)
                d = sqrt(sum((nodes(pidx,2:cols) - nodes(cidx,2:cols)).^2));
                if (table(cidx,col-1) == 0) || ...
                        (table(cidx,col-1) &gt; (table(pidx,col-1) + d))
                    table(cidx,col) = table(pidx,col-1) + d;
                    tmp_path = path(pidx);
                    path(cidx) = {[tmp_path{1} neighbor_ids(k)]};
                else
                    table(cidx,col) = table(cidx,col-1);
                end
            end
        end
        % find the minimum non-zero value in the table and save it
        nidx = find(table(:,col));
        ndx = find(table(nidx,col) == min(table(nidx,col)));
        if isempty(ndx)
            break
        else
            pidx = nidx(ndx(1));
            shortest_distance(pidx) = table(pidx,col);
            settled(pidx) = 1;
        end
    end
    if (nargin &lt; 4) % return the distance and path arrays for all of the nodes
        dist = shortest_distance';
        path = path';
    else % return the distance and path for the ending node
        dist = shortest_distance(zz);
        path = path(zz);
        path = path{1};
    end
end
在command windows 输入这些代码出现Strings passed to EVAL cannot contain function declarations.这是怎么回事,各路高手帮帮菜鸟,相当感谢!












Dijkstra算法是典型最短路算法，用于计算一个节点到其他所有节点的最短路径。主要特点是以起始点为中心向外层层扩展，直到扩展到终点为止。Dijkstra算法能得出最短路径的最优解，但由于它遍历计算的节点很多，所以效率低。

Dijkstra算法是很有代表性的最短路算法，在很多专业课程中都作为基本内容有详细的介绍，如数据结构，图论，运筹学等等。

Dijkstra一般的表述通常有两种方式，一种用永久和临时标号方式，一种是用OPEN, CLOSE表方式，Drew为了和下面要介绍的 A* 算法和 D* 算法表述一致，这里均采用OPEN,CLOSE表的方式。

其采用的是贪心法的算法策略

大概过程：

创建两个表，OPEN, CLOSE。

OPEN表保存所有已生成而未考察的节点，CLOSED表中记录已访问过的节点。

1． 访问路网中距离起始点最近且没有被检查过的点，把这个点放入OPEN组中等待检查。

2． 从OPEN表中找出距起始点最近的点，找出这个点的所有子节点，把这个点放到CLOSE表中。

3． 遍历考察这个点的子节点。求出这些子节点距起始点的距离值，放子节点到OPEN表中。

4． 重复第2和第3步,直到OPEN表为空，或找到目标点。


算法实现
[编辑本段]
#include<fstream>
#define MaxNum 765432100
using namespace std;

ifstream fin("Dijkstra.in");
ofstream fout("Dijkstra.out");

int Map[501][501];
bool is_arrived[501];
int Dist[501],From[501],Stack[501];
int p,q,k,Path,Source,Vertex,Temp,SetCard;

int FindMin()
{
int p,Temp=0,Minm=MaxNum;
for(p=1;p<=Vertex;p++)
if ((Dist[p]<Minm)&&(!is_arrived[p]))
{
Minm=Dist[p];
Temp=p;
}
return Temp;
}
int main()
{
memset(is_arrived,0,sizeof(is_arrived));

fin >> Source >> Vertex;
for(p=1;p<=Vertex;p++)
for(q=1;q<=Vertex;q++)
{
fin >> Map[p][q];
if (Map[p][q]==0) Map[p][q]=MaxNum;
}
for(p=1;p<=Vertex;p++)
{
Dist[p]=Map[Source][p];
if (Dist[p]!=MaxNum) 
From[p]=Source;
else 
From[p]=p;
}

is_arrived[Source]=true;
SetCard=1;
do
{
Temp=FindMin();
if (Temp!=0)
{
SetCard=SetCard+1;
is_arrived[Temp]=true;
for(p=1;p<=Vertex;p++)
if ((Dist[p]>Dist[Temp]+Map[Temp][p])&&(!is_arrived[p]))
{
Dist[p]=Dist[Temp]+Map[Temp][p];
From[p]=Temp;
}
}
else
break;
}
while (SetCard!=Vertex);

for(p=1;p<=Vertex;p++)
if(p!=Source)
{
fout << "========================\n";
fout << "Source:" << Source << "\nTarget:" << p << '\n';
if (Dist[p]==MaxNum)
{
fout << "Distance:" << "Infinity\n";
fout << "Path:No Way!";
}
else
{ 
fout << "Distance:" << Dist[p] << '\n';
k=1;
Path=p;
while (From[Path]!=Path)
{
Stack[k]=Path;
Path=From[Path];
k=k+1;
}
fout << "Path:" << Source;
for(q=k-1;q>=1;q--)
fout << "-->" << Stack[q];
}
fout << "\n========================\n\n";
}

fin.close();
fout.close();
return 0;
}

Sample Input
2
7
00 20 50 30 00 00 00
20 00 25 00 00 70 00
50 25 00 40 25 50 00
30 00 40 00 55 00 00
00 00 25 55 00 10 00
00 70 50 00 10 00 00
00 00 00 00 00 00 00

Sample Output
========================
Source:2
Target:1
Distance:20
Path:2-->1
========================
========================
Source:2
Target:3
Distance:25
Path:2-->3
========================
========================
Source:2
Target:4
Distance:50
Path:2-->1-->4
========================
========================
Source:2
Target:5
Distance:50
Path:2-->3-->5
========================
========================
Source:2
Target:6
Distance:60
Path:2-->3-->5-->6
========================
========================
Source:2
Target:7
Distance:Infinity
Path:No Way!
========================
示例程序及相关子程序：

void Dijkstra(int n,int[] Distance,int[] iPath)
{
int MinDis,u;
int i,j;
//从邻接矩阵复制第n个顶点可以走出的路线，就是复制第n行到Distance[]
for(i=0;i<VerNum;i++)
{
Distance=Arc[n,i];
Visited=0;
}//第n个顶点被访问，因为第n个顶点是开始点
Visited[n]=1;
//找到该顶点能到其他顶点的路线、并且不是开始的顶点n、以前也没走过。
//相当于寻找u点，这个点不是开始点n
for(i=0;i<VerNum;i++)
{
u=0;
MinDis=No;
for(j=0;j<VerNum;j++)
if(Visited[j] == 0&&(Distance[j]<MinDis))
{
MinDis=Distance[j];
u=j;
}
//如范例P1871图G6，Distance=[No,No,10,No,30,100]，第一次找就是V2，所以u=2
//找完了，MinDis等于不连接，则返回。这种情况类似V5。
if(MinDis==No) return ;
//确立第u个顶点将被使用，相当于Arc[v,u]+Arc[u,w]中的第u顶点。
Visited[u]=1;
//寻找第u个顶点到其他所有顶点的最小路，实际就是找Arc[u,j]、j取值在[0，VerNum]。
//如果有Arc[i,u]+Arc[u,j]<Arc[i,j]，则Arc[i,j]=Arc[i,u]+Arc[u,j]<Arc[i,j]
//实际中，因为Distance[]是要的结果，对于起始点确定的情况下，就是：
//如果(Distance[u] + Arc[u,j]) <= Distance[j] 则：
//Distance[j] = Distance[u] + Arc[u, j]；
//而iPath[]保存了u点的编号；
//同理：对新找出的路线，要设置Visited[j]=0，以后再找其他路，这个路可能别利用到。例如V3
for(j=0;j<VerNum;j++)
if(Visited[j]==0&&Arc[u,j]<No&&u!= j) 
{
if ((Distance[u] + Arc[u,j]) <= Distance[j])
{
Distance[j] = Distance[u] + Arc[u, j];
Visited[j]=0;
iPath[j] = u;
}
}
}
}
//辅助函数
void Prim()
{
int i,m,n=0;
for(i=0;i<VerNum;i++) 
{
Visited=0;
T=new TreeNode();
T.Text =V;
}
Visited[n]++;
listBox1.Items.Add (V[n]); 
while(Visit()>0)
{
if((m=MinAdjNode(n))!=-1)
{
T[n].Nodes.Add(T[m]); 
n=m;
Visited[n]++;
}
else
{
n=MinNode(0);
if(n>0) T[Min2].Nodes.Add(T[Min1]); 
Visited[n]++;
}
listBox1.Items.Add (V[n]); 
}
treeView1.Nodes.Add(T[0]); 
}
void TopoSort()
{
int i,n;
listBox1.Items.Clear(); 
Stack S=new Stack();
for(i=0;i<VerNum;i++)
Visited=0;
for(i=VerNum-1;i>=0;i--)
if(InDegree(i)==0)
{
S.Push(i);
Visited++;
}
while(S.Count!=0)
{
n=(int )S.Pop();
listBox1.Items.Add (V[n]); 
ClearLink(n);
for(i=VerNum-1;i>=0;i--)
if(Visited==0&&InDegree(i)==0)
{
S.Push(i);
Visited++;
}
}
}
void AOETrave(int n,TreeNode TR,int w)
{
int i,w0;
if(OutDegree(n)==0) return;
for(i=0;i<VerNum;i++)
if((w0=Arc[n,i])!=0)
{
listBox1.Items.Add (V+"\t"+(w+w0).ToString()+"\t"+i.ToString()+"\t"+n.ToString());
TreeNode T1=new TreeNode();
T1.Text =V+" [W="+(w+w0).ToString()+"]"; 
TR.Nodes.Add(T1); 
AOETrave(i,T1,w+w0);
}
}
void AOE()
{
int i,w=0,m=1;
TreeNode T1=new TreeNode();
for(i=0;i<VerNum;i++)
{
Visited=0;
}
T1.Text =V[0];
listBox1.Items.Add ("双亲表示法显示这个生成树："); 
listBox1.Items.Add ("V\tW\tID\tPID");
for(i=0;i<VerNum;i++)
{
if((w=Arc[0,i])!=0)
{
listBox1.Items.Add (V+"\t"+w.ToString()+"\t"+i.ToString()+"\t0");
TreeNode T2=new TreeNode();
T2.Text=V+" [W="+w.ToString()+"]";
AOETrave(i,T2,w);
T1.Nodes.Add (T2); 
listBox1.Items.Add("\t\t树"+m.ToString());
m++;
}
}
treeView1.Nodes.Clear(); 
treeView1.Nodes.Add (T1);
}
int IsZero()
{
int i;
for(i=0;i<VerNum;i++)
if(LineIsZero(i)>=0) return i;
return -1;
}
int LineIsZero(int n)
{
int i;
for(i=0;i<VerNum;i++)
if (Arc[n,i]!=0) return i;
return -1;
}
void DepthTraverse()
{
int i,m;
for(i=0;i<VerNum;i++)
{
Visited=0;
T=new TreeNode();
T.Text =V;
R=0;
}
while((m=IsZero())>=0)
{
if(Visited[m]==0) 
{
listBox1.Items.Add (V[m]);
R[m]=1;
}
Visited[m]++;
DTrave(m);
}
for(i=0;i<VerNum;i++)
{
if(R==1)
treeView1.Nodes.Add (T); 
}
}
void DTrave(int n)
{
int i;
if (LineIsZero(n)<0) return;
for(i=VerNum-1;i>=0;i--)
if(Arc[n,i]!=0)
{
Arc[n,i]=0;
Arc[i,n]=0;
if(Visited==0)
{
listBox1.Items.Add (V);
T[n].Nodes.Add (T); 
R=0;
}
Visited++;
DTrave(i);
}
}
void BreadthTraverse()
{
int i,m;
for(i=0;i<VerNum;i++)
{
Visited=0;
T=new TreeNode();
T.Text =V;
R=0;
}
while((m=IsZero())>=0)
{
if(Visited[m]==0) 
{
listBox1.Items.Add (V[m]);
R[m]=1;
}
Visited[m]++;
BTrave(m);
}
for(i=0;i<VerNum;i++)
{
if(R==1)
treeView1.Nodes.Add (T); 
}
}
void BTrave(int n)
{
int i;
Queue Q=new Queue();
Q.Enqueue(n);
while(Q.Count!=0)
{
for(i=0;i<VerNum;i++)
{
if(Arc[n,i]!=0)
{
Arc[n,i]=0;
Arc[i,n]=0;
if(Visited==0)
{
listBox1.Items.Add(V); 
T[n].Nodes.Add (T); 
R=0;
}
Visited++;
Q.Enqueue(i);
}
}
n=(int )Q.Dequeue(); 
}
}
int MinNode(int vn)
{
int i,j,n,m,Min=No;
n=-1;m=-1;
for (i=vn;i<VerNum;i++)
for(j=0;j<VerNum;j++)
if(Arc[i,j]!=No&&Arc[i,j]<Min&&Visited==0&&Visited[j]==1)
{
Min=Arc[i,j];n=i;m=j;
}
Min1=n;Min2=m;
return n;
}
int MinAdjNode(int n)
{
int i,Min,m;
Min=No;m=-1;
for(i=0;i<VerNum;i++)
if(Arc[n,i]!=No&&Visited==0&&Min>Arc[n,i]&&Visited[n]==1)
{
Min=Arc[n,i];m=i;
}
return m;
}
int Visit()
{
int i,s=0;
for(i=0;i<VerNum;i++)
if(Visited==0) s++;
return s;
}



如果您认为本词条还有待完善，需要补充新内容或修改错误内容，请 编辑词条 
参考资料：
 1.http://blog.csdn.net/ctu_85/archive/2006/11/17/1393130.aspx 
 2.算法设计 
 3.http://hi.baidu.com/zhyf%5F2008/blog/item/e566680fcd6110e9aa64570d.html 
 
````

</details>

#### 中国数学建模-编程交流-组合算法概论 · MATLAB · d41f62aa

- 归属算法：Dijkstra最短路
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Dijkstra最短路中的“结果绘图与展示”。
- **执行主线**：通过松弛操作求单源最短路径；用中间节点递推更新全源最短路矩阵；选择低权边构造最小生成树；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、图形
- **调用风险**：包含绝对路径，必须改为项目相对路径。

- SHA-256：`67c17e9e3854be8744ef10882a10ca01a0e946f16f1e9c87084704408e2ebce2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/组合算法/中国数学建模-编程交流-组合算法概论.txt`

<details>
<summary>展开原始代码</summary>

````matlab
中国数学建模-编程交流-组合算法概论  ├数学思想
  ├编程交流
  ├学术杂谈
  ├English Fans

        wh-ee 重登录  隐身  用户控制面板  搜索  风格  论坛状态  论坛展区  社区服务  社区休闲  网站首页  退出 

      >> VC++,C,Perl,Asp...编程学习,算法介绍.  我的收件箱 (0) 
       中国数学建模 → 学术区 → 编程交流 → 组合算法概论 

             您是本帖的第 623 个阅读者       
             * 贴子主题：组合算法概论           

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28

        鲜花(1)  鸡蛋(0)             楼主 



               组合算法概论

              组合算法概论(A Brief Introduction to Combinatorial Algorithm) 
                  
              组合算法是算法分析学当中非常重要的一个分支，关于它在计算机科学的地位我就不敖述了，下面为大家整理了整个材料，算法是我收集的，只是分门别类简单介绍一下，然后把我的材料做了个整理，大家收藏吧，感觉挺有用的，费了我好长时间和精力呀，我现在准备考研了，没有太多时间发很多经典文章了，这片算是大部头了。 

                  
              关于组合学问题的算法，计算对象是离散的、有限的数学结构。从方法学的角度，组合算法包括算法设计和算法分析两个方面。关于算法设计，历史上已经总结出了若干带有普遍意义的方法和技术，包括动态规划、回溯法、分支限界法、分治法、贪心法等。下面我们着重谈谈几个有代表性的组合算法： 

              单纯形法： 
                  
              这是一种线性规划算法，由G.B.Dantzig在1947年提出，后来由他和其他的学者又提出了单纯形法的变形和改进。这些被实践证明都是行之有效的，线性规划研究线性目标函数在一组线性等式与线性不等式约束下的极值问题。这本来是连续问题，Dantzig发现线性规划问题的可行解集（即满足约束条件的点的全体）是一个超多面体。如果它的最优解存在，那么这个最优解一定可以在超多面体的一个顶点取到。由于超多面体的顶点只有有限个，从而使线性规划成为一个组和优化问题。单纯形法是按照一定的规则，从可行解集的一个顶点转移到另一个顶点，使得目标函数的值不断地得到改进，最后达到最优。尽管单纯形法一直使用得很好，但是在最坏情况下它需要指数运行时间，从而使线性规划问题是否属于P类一度成为人们关心的问题。后来的椭球算法和投影算法都很好的解决了这个问题。 

              排序和检索： 
                  
              这两部分应当是大家比较熟悉的，所谓排序，就是将给定的元素序列按照某种顺序关系重新排列成有序序列。例如将n个数组成的序列按照从小到大的顺序重新排列；将n个英语单词组成的的序列按照字典顺序重新排列。所谓检索，就是在给定的集合中查找某个特定的元素或是元素组。排序和检索已经成为计算机科学技术中最基本、使用最频繁的算法。下面我们专门谈谈排序算法（sorting 
              algorithm）。
                  
              在讨论此种算法时，数据通常是指由若干记录组成的文件，每个记录包含一个或多个数据项，其中能够标志该记录的数据项称为键码。给定一文件的n个记录{R1,R2,…,Rn}及其相应的键码的集合{K1,K2,…,Kn}。所谓排序算法就是在数据处理中将文件中的记录按键码的一定次序要求排列起来的算法。若待排序的文件能够同时装入计算机的主存中，整个排序过程不需要访问外存便能完成，则称此类排序问题为内部排序；若参加排序的记录数量很大，整个序列的排序过程不可能在内存中完成，有一部分必须放在外存上，则称此类排序问题为外部排序。当待排序的文件中包含有一些相同键码的记录时，如果经过排序后这些相同的键码的记录的相对次序仍然保持不变，则相应的排序算法是稳定的，否则为不稳定的。如果排序算法设计成单处理机完成的，则此排序算法称为串行（或顺序）排序算法；如果排序算法时设计成多处理机实现的，则称为并行排序算法。 

                  
              首先谈谈内部排序：内部排序的过程是一个逐步扩大记录的有序序列长度的过程。在排序的过程中，参与排序的记录序列中存在两个区域：有序区和无序区。 

              使有序区中记录的数目增加一个或几个的操作称为一趟排序。 
                  逐步扩大记录有序序列长度的方法大致有下列几类： 
              一．插入排序 
                  假设在排序过程中，记录序列R[1..n]的状态为： 
              则一趟直接插入排序的基本思想为：将记录R 
              插入到有序子序列R[1..i-1]中，使记录的有序序列从R[1..i-1]变为R[1..i]。 
                  显然，完成这个“插入”需分三步进行： 
              1．查找R的插入位置j+1； 
              2．将R[j+1..i-1]中的记录后移一个位置； 
              3．将R复制到R[j+1]的位置上。 
              [I]直接插入排序 
                  利用顺序查找实现“在R[1..i-1]中查找R的插入位置”的插入排序。 
                  注意直接插入排序算法的三个要点： 
              1．从R[i-1]起向前进行顺序查找，监视哨设置在R[0]； 
                R[0] = R;    // 设置“哨兵” 
                for (j=i-1; R[0].key<R[j].key; --j); // 从后往前找 
                return j+1;     // 返回R的插入位置为j+1 
              2．对于在查找过程中找到的那些关键字不小于R.key的记录，可以在查找的同时实现向后移动； 
                for (j=i-1; R[0].key<R[j].key; --j);   
                R[j+1] = R[j] 
              3．i = 2，3，…, n, 实现整个序列的排序。 
                template<class Elem> 
                void InsertionSort ( Elem R[],  int n) 
                { 
                    // 对记录序列R[1..n]作直接插入排序。 
                    for ( i=2; i<=n; ++i ) 
                    { 
                        R[0] = R;            // 复制为监视哨 
                        for ( j=i-1; R[0].key < R[j].key;  --j ) 
                            R[j+1] = R[j];    // 记录后移 
                        R[j+1] = R[0];        // 插入到正确位置 
                    } 
                } // InsertSort 
                  时间分析： 
                  实现排序的基本操作有两个： 
              （1）“比较”序列中两个关键字的大小； 
              （2）“移动”记录。 
                  对于直接插入排序： 
              [II]折半插入排序 
                   
              因为R[1..i-1]是一个按关键字有序的有序序列，则可以利用折半查找实现“在R[1..i-1]中查找R的插入位置”，如此实现的插入排序为折半插入排序。其算法如下： 

                template<class Elem> 
                void BiInsertionSort (Elem R[]， int n) 
                { 
                    // 对记录序列R[1..n]作折半插入排序。 
                    for ( i=2; i<=L.length; ++i ) 
                    { 
                        R[0] = R;      // 将R暂存到R[0] 
                        low = 1; high = i-1; 
                        while (low<=high) 
                        { //在R[low..high]中折半查找插入的位置 
                            m = (low+high)/2;           // 折半 
                            if (R[0].key < R[m].key)) 
                                high = m-1;   // 插入点在低半区 
                            else
                                low = m+1;    // 插入点在高半区 
                        } 
                        for ( j=i-1; j>=high+1; --j ) 
                            R[j+1] = R[j];      // 记录后移 
                        R[high+1] = R[0];  // 插入 
                    } 
                } // BInsertSort 
                  折半插入排序比直接插入排序明显地减少了关键字间的“比较”次数，但记录“移动”的次数不变。 
              [III]表插入排序 
                  
              为了减少在排序过程中进行的“移动”记录的操作，必须改变排序过程中采用的存储结构。利用静态链表进行排序，并在排序完成之后，一次性地调整各个记录相互之间的位置，即将每个记录都调整到它们所应该在的位置上。 

              算法描述如下： 
                template<class Elem> 
                void LInsertionSort (Elem SL[]， int n) 
                {
                    // 对记录序列SL[1..n]作表插入排序。 
                    SL[0].key = MAXINT ; 
                    SL[0].next = 1;  SL[1].next = 0; 
                    for ( i=2; i<=n; ++i ) 
                        for ( j=0, k = SL[0].next; 
                            SL[k].key <= SL.key ; j = k, k = SL[k].next ) 
                    { SL[j].next = i;  SL.next = k; } 
                    // 结点i插入在结点j和结点k之间 
                }// LinsertionSort 
              关于如在排序之后调整记录序列： 
              算法中使用了三个指针: 
              其中：p指示第i个记录的当前位置； 
                    i指示第i个记录应在的位置； 
                    q指示第i+1个记录的当前位置 
                template<class Elem> 
                void Arrange ( SLinkListType SL[ ], int n ) { 
                    // 根据静态链表SL中各结点的指针值调整 
                    // 记录位置，使得SL中记录按关键字非递减 
                    // 有序顺序排列 
                    p = SL[0].next;// p指示第一个记录的当前位置 
                    for ( i=1; i<n; ++i ) {       
                        // SL[1..i-1]中记录已按关键字有序排列， 
                        // 第i个记录在SL中的当前位置应不小于i 
                        while (p<i)  p = SL[p].next; 
                        // 找到第i个记录，并用p指示 
                        // 其在SL中当前位置 
                        q = SL[p].next;     // q指示尚未调整的表尾 
                        if ( p!= i ) { 
                            SL[p]←→SL;   // 交换记录，使第i个 
                            // 记录到位 
                            SL.next = p;    // 指向被移走的记录， 
                            // 使得以后可由while循环找回 
                        } 
                        p = q;         // p指示尚未调整的表尾， 
                        // 为找第i+1个记录作准备 
                    } 
                } // Arrange 
              二． 交换排序
                  
              通过“交换”无序序列中的记录从而得到其中关键字最小或最大的记录，并将它加入到有序子序列中，以此方法增加记录的有序子序列的长度; 
              [I]起泡排序 
                  假设在排序过程中，记录序列R[1..n]的状态为：n-i+1 
              则第i趟起泡插入排序的基本思想为：借助对无序序列中的记录进行“交换”的操作，将无序序列中关键字最大的记录“交换”到R[n-i+1]的位置上。 

              算法描述： 
                template <class Elem> 
                void BubbleSort(Elem R[], int n) 
                { 
                    // i 指示无序序列中最后一个记录的位置 
                    i = n; 
                    while (i > 1) { 
                        lastExchangeIndex = 1; 
                        for (j = 1; j < i; j++) {
                            if (A[j+1] < A[j]) { 
                                Swap(A[j],A[j+1]); 
                                lastExchangeIndex = j; 
                            } //if
                        } // for 
                        i = lastExchangeIndex; 
                    } // while 
                } // BubbleSort 
                  起泡排序的结束条件为：最后一趟没有进行“交换”。 
                  
              从起泡排序的过程可见，起泡排序是一个增加有序序列长度的过程，也是一个缩小无序序列长度的过程，每经过一趟起泡，无序序列的长度只缩小1。我们可以设想，若能在经过一趟排序，使无序序列的长度缩小一半，则必能加快排序的速度。 




              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 20:07:19      

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 2 楼 



               
              [II]一趟快速排序 
                  
              目标：找一个记录，以它的关键字作为“枢轴”，凡其关键字小于枢轴的记录均移动至该记录之前，反之，凡关键字大于枢轴的记录均移动至该记录之后。致使一趟排序之后，记录的无序序列R[s..t]将分割成两部分：R[s..i-1]和R[i+1..t],且R[j].key≤ 
              R.key ≤ R[j].key 
                    (s≤j≤i-1)   枢轴     (i+1≤j≤t) 
              例如:关键字序列 
                      52, 49, 80, 36, 14, 58, 61, 97, 23, 75   
              调整为:  23, 49, 14, 36, (52) 58, 61, 97, 80, 75 
                  其中(52)为枢轴，在调整过程中，需设立两个指针:low和high，它们的初值分别为:s和t, 
              之后逐渐减小high，增加low，并保证R[high].key≥52，而R[low].key≤52,否则进行记录的“交换”。 
              算法描述如下: 
                template<class Elem> 
                int Partition (Elem R[], int low, int high) { 
                    // 交换记录子序列R[low..high]中的记录，使 
                    // 枢轴记录到位，并返回其所在位置，此时， 
                    // 在它之前（后）的记录均不大（小）于它 
                    pivotkey = R[low].key; 
                    // 用子表的第一个记录作枢轴记录 
                    while (low<high) { 
                        // 从表的两端交替地向中间扫描 
                        while (low<high && R[high].key>=pivotkey)     
                            --high; 
                        R[low]←→R[high];   
                        // 将比枢轴记录小的记录交换到低端 
                        while (low<high && R[low].key<=pivotkey) 
                            ++low; 
                        R[low]←→R[high]; 
                        // 将比枢轴记录大的记录交换到高端 
                    } 
                    return low;          // 返回枢轴所在位置 
                } // Partition 
                  
              容易看出，调整过程中的枢轴位置并不重要，因此，为了减少记录的移动次数，应先将枢轴记录“移出”，待求得枢轴记录应在的位置之后(此时low=high),再将枢轴记录到位。 

                  将上述“一次划分”的算法改写如下： 
                template<class Elem> 
                int Partition (Elem R[], int low, int high) { 
                    // 交换记录子序列R[low..high]中的记录，使 
                    //枢轴记录到位，并返回其所在位置，此时， 
                    // 在它之前（后）的记录均不大（小）于它 
                    R[0] = R[low]; 
                    // 用子表的第一个记录作枢轴记录 
                    pivotkey = R[low].key;    // 枢轴记录关键字 
                    while (low < high) { 
                        // 从表的两端交替地向中间扫描 
                        while(low=pivotkey) 
                            --high; 
                        R[low] = R[high]; 
                        // 将比枢轴记录小的记录移到低端 
                        while (low<high && R[low].key<=pivotkey) 
                            ++low; 
                        R[high] = R[low]; 
                        // 将比枢轴记录大的记录移到高端 
                    } 
                    R[low] = R[0];          // 枢轴记录到位 
                    return low;             // 返回枢轴位置 
                } // Partition 
              [III]快速排序 
                  在对无序序列中记录进行了一次分割之后，分别对分割所得两个子序列进行快速排序，依次类推，直至每个子序列中只含一个记录为止。  
              快速排序的算法描述如下: 
                template<class Elem> 
                void QSort (Elem R[], int low, int high) { 
                    // 对记录序列R[low..high]进行快速排序 
                    if (low < high-1) {             // 长度大于1 
                        pivotloc = Partition(L, low, high); 
                        // 将L.r[low..high]一分为二 
                        QSort(L, low, pivotloc-1); 
                        // 对低子表递归排序，pivotloc是枢轴位置 
                        QSort(L, pivotloc+1, high); 
                        // 对高子表递归排序 
                    } 
                } // QSort 

                template<class Elem> 
                void QuickSort(Elem R[],  int n) { 
                    // 对记录序列进行快速排序 
                    QSort(R, 1, n); 
                } // QuickSort 
              快速排序的时间分析 
                  假设一次划分所得枢轴位置i=k，则对n个记录进行快排所需时间 
              T(n) = Tpass(n)+T(k-1)+T(n-k) 
                  其中 
              Tpass(n)为对n个记录进行一次划分所需时间，若待排序列中记录的关键字是随机分布的，则k取1至n中任意一值的可能性相同，由此可得快速排序所需时间的平均值为： 

              设 Tavg(1)≤b 
              则可得结果 
                  
              通常，快速排序被认为是在所有同数量级O(nlogn)的排序方法中，其平均性能是最好的。但是，若待排记录的初始状态为按关键字有序时，快速排序将蜕化为起泡排序，其时间复杂度为O(n2)。 

                  为避免出现这种情况，需在进行快排之前，进行“予处理”，即：比较 R(s).key, 
              R(t).key和R[&#61675;(s+t)/2&#61691;.key，然后取关键字为“三者之中”的记录为枢轴记录。 
              三． 选择排序
                  从记录的无序子序列中“选择”关键字最小或最大的记录，并将它加入到有序子序列中，以此方法增加记录的有序子序列的长度; 
              [I]简单选择排序 
                  假设排序过程中，待排记录序列的状态为： 
                  
              并且有序序列中所有记录的关键字均小于无序序列中记录的关键字，则第i趟简单选择排序是，从无序序列R[i..n]的n-i+1记录中选出关键字最小的记录加入有序序列。 

                  简单选择排序的算法描述如下： 
              template 
              void SelectSort (Elem R[], int n ) { 
              // 对记录序列R[1..n]作简单选择排序。 
              for (i=1; i           // 选择第i小的记录，并交换到位 
              j = SelectMinKey(R, i);       
                    // 在R[i..n]中选择key最小的记录 
              if (i!=j) R←→R[j]; 
                                // 与第i个记录交换 
              } 
              } // SelectSort 
              时间性能分析 
                对n个记录进行简单选择排序，所需进行的关键字间的比较次数总计为 
                      
              移动记录的次数，最小值为0, 最大值为3(n-1) 
              [II]堆排序

              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 20:07:36       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 3 楼 



               
              堆排序也是选择排序的一种，其特点是，在以后各趟的“选择”中利用在第一趟选择中已经得到的关键字比较的结果。 
              堆的定义: 
              堆是满足下列性质的数列{r1, r2, …，rn}： 
                       或   
              若将此数列看成是一棵完全二叉树，则堆或是空树或是满足下列特性的完全二叉树：其左、右子树分别是堆，并且当左/右子树不空时，根结点的值小于(或大于)左/右子树根结点的值。 

              由此，若上述数列是堆，则r1必是数列中的最小值或最大值，分别称作小顶堆或大顶堆。 
                 
              堆排序即是利用堆的特性对记录序列进行排序的一种排序方法。具体作法是：先建一个“大顶堆”，即先选得一个关键字为最大的记录，然后与序列中最后一个记录交换，之后继续对序列中前n-1记录进行“筛选”，重新将它调整为一个“大顶堆”，再将堆顶记录和第n-1个记录交换，如此反复直至排序结束。 

              所谓“筛选”指的是，对一棵左/右子树均为堆的完全二叉树，“调整”根结点使整个二叉树为堆。 
              堆排序的算法如下所示： 
              template 
              void HeapSort ( Elem R[], int n ) { 
              // 对记录序列R[1..n]进行堆排序。 
              for ( i=n/2; i>0; --i ) 
                                  // 把R[1..n]建成大顶堆 
                 HeapAdjust ( R, i, n ); 
              for ( i=n; i>1; --i ) { 
              R[1]←→R;           
                      // 将堆顶记录和当前未经排序子序列 
                      // R[1..i]中最后一个记录相互交换 
              HeapAdjust(R, 1, i-1);             
                      // 将R[1..i-1] 重新调整为大顶堆 
              } 
              } // HeapSort 
              其中筛选的算法如下所示。为将R[s..m]调整为“大顶堆”，算法中“筛选”应沿关键字较大的孩子结点向下进行。 
              Template 
              void HeapAdjust (Elem R[], int s, int m) { 
              // 已知R[s..m]中记录的关键字除R[s].key之 
              // 外均满足堆的定义，本函数调整R[s] 的关 
              // 键字，使R[s..m]成为一个大顶堆（对其中 
              // 记录的关键字而言） 
              rc = R[s]; 
              for ( j=2*s; j<=m; j*=2 ) {// 沿key较大的孩子结点向下筛选 
              if ( j    if ( rc.key >= R[j].key )  break; // rc应插入在位置s上 
                 R[s] = R[j];  s = j; 
                 } 
                 R[s] = rc; // 插入 
              } // HeapAdjust 
              堆排序的时间复杂度分析： 
              1. 对深度为k的堆，“筛选”所需进行的关键字比较的次数至多为2(k-1); 
              2．对n个关键字，建成深度为h(=&#61675;log2n&#61691;+1)的堆，所需进行的关键字比较的次数至多为4n; 
              3. 调整“堆顶”n-1次，总共进行的关键字比较的次数不超过 
              2(log2(n-1)&#61691;+ &#61675;log2(n-2)&#61691;+ …+log22)<2n(&#61675;log2n&#61691;) 
              因此，堆排序的时间复杂度为O(nlogn) 
              四．归并排序：是通过“归并”两个或两个以上的记录有序子序列，逐步增加记录有序序列的长度;归并排序的基本思想是：将两个或两个以上的有序子序列“归并”为一个有序序列。 

                在内部排序中，通常采用的是2-路归并排序。即：将两个位置相邻的有序子序列 归并为一个有序序列。 
              “归并”算法描述如下： 
              template 
              void Merge (Elem SR[], Elem TR[], int i, int m, int n) { 
              // 将有序的SR[i..m]和SR[m+1..n]归并为 
              // 有序的TR[i..n] 
              for (j=m+1, k=i;  i<=m && j<=n;  ++k)   
              {        // 将SR中记录由小到大地并入TR 
                 if (SR.key<=SR[j].key)  TR[k] = SR[i++]; 
                 else TR[k] = SR[j++]; 
              } 
              if (i<=m) TR[k..n] = SR[i..m]; 
                            // 将剩余的SR[i..m]复制到TR 
              if (j<=n) TR[k..n] = SR[j..n]; 
                             // 将剩余的SR[j..n]复制到TR 
              } // Merge 
              归并排序的算法可以有两种形式：递归的和递推的，它是由两种不同的程序设计思想得出的。在此，只讨论递归形式的算法。 
              这是一种自顶向下的分析方法： 
              如果记录无序序列R[s..t]的两部分R[s..&#61675;(s+t)/2&#61691;]和R[&#61675;(s+t)/2+1..t&#61691;分别按关键字有序，则利用上述归并算法很容易将它们归并成整个记录序列是一个有序序列，由此，应该先分别对这两部分进行2-路归并排序。 

              template 
              void Msort ( Elem SR[], Elem TR1[], int s, int t ) { 
              // 将SR[s..t]进行2-路归并排序为TR1[s..t]。 
              if (s==t)  TR1[s] = SR[s]; 
              else { 
              m = (s+t)/2; 
              // 将SR[s..t]平分为SR[s..m]和SR[m+1..t] 
              Msort (SR, TR2, s, m); 
                // 递归地将SR[s..m]归并为有序的TR2[s..m] 
              Msort (SR, TR2, m+1, t); 
              //递归地SR[m+1..t]归并为有序的TR2[m+1..t] 
              Merge (TR2, TR1, s, m, t); 
              // 将TR2[s..m]和TR2[m+1..t]归并到TR1[s..t] 
              } 
              } // MSort 
                
              template 
              void MergeSort (Elem R[]) { 
              // 对记录序列R[1..n]作2-路归并排序。 
                MSort(R, R, 1, n); 
              } // MergeSort 

              容易看出，对n个记录进行归并排序的时间复杂度为Ο(nlogn)。即：每一趟归并的时间复杂度为O(n)，总共需进行logn趟。 
              五．基数排序：借助“多关键字排序”的思想来实现“单关键字排序”的算法。 
              [I]多关键字的排序 
              假设有n个记录……的序列 
                   { R1, R2, …，Rn} 
              每个记录Ri中含有d个关键字(Ki0, Ki1, …,Kid-1),则称上述记录序列对关键字(Ki0, Ki1, 
              …,Kid-1)有序是指：对于序列中任意两个记录Ri和Rj(1≤i (Ki0, Ki1, …,Kid-1)< (Kj0, Kj1, 
              …,Kjd-1) 
              其中K0被称为“最主”位关键字，Kd-1被称为 “最次”位关键字。 
              实现多关键字排序通常有两种作法: 
              最高位优先MSD法：先对K0进行排序，并按K0的不同值将记录序列分成若干子序列之后，分别对K1进行排序，…，依次类推，直至最后对最次位关键字排序完成为止。 

              最低位优先LSD法：先对Kd-1进行排序，然后对Kd-2进行排序，依次类推，直至对最主位关键字K0排序完成为止。排序过程中不需要根据“前一个”关键字的排序结果，将记录序列分割成若干个(“前一个”关键字不同的)子序列。 



              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 20:07:55       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 4 楼 



               
              例如:学生记录含三个关键字:系别、班号和班内的序列号，其中以系别为最主位关键字。LSD的排序过程如下: 
              [II]链式基数排序 
              假如多关键字的记录序列中，每个关键字的取值范围相同，则按LSD法进行排序时，可以采用“分配-收集”的方法，其好处是不需要进行关键字间的比较。 

              对于数字型或字符型的单关键字，可以看成是由多个数位或多个字符构成的多关键字，此时可以采用这种“分配-收集”的办法进行排序，称作基数排序法。 

              例如：对下列这组关键字 
              {209, 386, 768, 185, 247, 606, 230, 834, 539 } 
              首先按其“个位数”取值分别为0, 1, …，9“分配”成10组，之后按从0至9的顺序将它们“收集”在一起;然后按其“十位数” 
              取值分别为0, 1, 
              …，9“分配”成10组，之后再按从0至9的顺序将它们“收集”在一起;最后按其“百位数”重复一遍上述操作，便可得到这组关键字的有序序列。 

              在计算机上实现基数排序时，为减少所需辅助存储空间，应采用链表作存储结构，即链式基数排序，具体作法为： 
              １． 待排序记录以指针相链，构成一个链表；
              ２．“分配”时，按当前“关键字位”所取值，将记录分配到不同的“链队列”中，每个队列中记录的“关键字位”相同； 
              ３．“收集”时，按当前关键字位取值从小到大将各队列首尾相链成一个链表; 
              ４．对每个关键字位均重复2)和3)两步。 
              例如： 
              p→369→367→167→239→237→138→230→139 
              第一次分配得到 
              f[0]→230←r[0] 
              f[7]→367→167→237←r[7] 
              f[8]→138←r[8] 
              f[9]→369→239→139←r[9] 
              第一次收集得到 
              p→230→367→167→237→138→368→239→139 
              第二次分配得到 
              f[3]→230→237→138→239→139←r[3] 
              f[6]→367→167→368←r[6] 
              第二次收集得到 
              p→230→237→138→239→139→367→167→368 
              第三次分配得到 
              f[1]→138→139→167←r[1] 
              f[2]→230→237→239←r[2] 
              f[3]→367→368←r[3] 
              第三次收集之后便得到记录的有序序列 
              p→138→139→167→230→237→239→367→368 
              我们在技术排序中需要注意的是： 
              １．“分配”和“收集”的实际操作仅为修改链表中的指针和设置队列的头、尾指针； 
              ２．为查找使用，该链表尚需应用算法Arrange将它调整为有序表。 
              基数排序的时间复杂度为O(d(n+rd))。 
              其中，分配为O(n);收集为O(rd)(rd为“基”),d为“分配-收集”的趟数。 
              下面我们比较一下上面谈到的各种内部排序方法 
              首先，从时间性能上说： 
              1. 按平均的时间性能来分，有三类排序方法： 
              时间复杂度为O(nlogn)的方法有：快速排序、堆排序和归并排序，其中以快速排序为最好； 
              时间复杂度为O(n2)的有：直接插入排序、起泡排序和简单选择排序，其中以直接插入为最好，特别是对那些对关键字近似有序的记录序列尤为如此； 

              时间复杂度为O(n)的排序方法只有，基数排序。 
              2. 
              当待排记录序列按关键字顺序有序时，直接插入排序和起泡排序能达到O(n)的时间复杂度;而对于快速排序而言，这是最不好的情况，此时的时间性能蜕化为O(n2)，因此是应该尽量避免的情况。 

              3. 简单选择排序、堆排序和归并排序的时间性能不随记录序列中关键字的分布而改变。 
              其次，从空间性能上说： 
              指的是排序过程中所需的辅助空间大小。 
              1. 所有的简单排序方法(包括：直接插入、起泡和简单选择)和堆排序的空间复杂度为O(1)； 
              2. 快速排序为O(logn)，为栈所需的辅助空间; 
              3. 归并排序所需辅助空间最多，其空间复杂度为O(n); 
              4. 链式基数排序需附设队列首尾指针，则空间复杂度为O(rd)。 
              再次，从排序方法的稳定性能上说： 
              稳定的排序方法指的是，对于两个关键字相等的记录，它们在序列中的相对位置，在排序之前和经过排序之后，没有改变。当对多关键字的记录序列进行LSD方法排序时，必须采用稳定的排序方法。对于不稳定的排序方法，只要能举出一个实例说明即可。我们需要指出的是：快速排序和堆排序是不稳定的排序方法。 

              我们再谈谈关于“排序方法的时间复杂度的下限” 
              这里讨论的各种排序方法，除基数排序外，其它方法都是基于“比较关键字”进行排序的排序方法，可以证明，这类排序法可能达到的最快的时间复杂度为O(nlogn)。(基数排序不是基于“比较关键字”的排序方法,所以它不受这个限制)。可以用一棵判定树来描述这类基于“比较关键字”进行排序的排序方法。 

              例如，对三个关键字进行排序的判定树如下： 
                                   K1 
                          K1 
                     K2< K3         K2 
              K3 描述排序的判定树有两个特点： 
              １．树上的每一次“比较”都是必要的; 
              ２． 树上的叶子结点包含所有可能情况。 
              则由上图所示“判定树的深度为4”可以推出“至多进行三次比较”即可完成对三个关键字的排序。反过来说，由此判定树可见，考虑最坏情况，“至少要进行三次比较”才能完成对三个关键字的排序。对三个关键字进行排序的判定树深度是唯一的。即无论按什么先后顺序去进行比较，所得判定树的深度都是3。当关键字的个数超过3之后，不同的排序方法其判定树的深度不同。例如，对4个关键字进行排序时，直接插入的判定树的深度为6, 
              而折半插入的判定树的深度为5。 
                 
              可以证明，对4个关键字进行排序，至少需进行5次比较。因为，4个关键字排序的结果有4!=24种可能，即排序的判定树上必须有24个叶子结点，其深度的最小值为6。 

              一般情况下，对n个关键字进行排序，可能得到的结果有n! 种，由于含n! 个叶子结点的二叉树的深度不小于&#61673;log2(n!)&#61689; +1, 
              则对n个关键字进行排序的比较次数至少是&#61673;log2(n!)&#61689; 。利用斯蒂林近似公式&#61673;log2(n!)&#61689; &#61627; nlog2n 
              所以，基于“比较关键字”进行排序的排序方法，可能达到的最快的时间复杂度为O(nlogn)。 
              下面我们再来谈谈外部排序： 
              常见的外部排序有： 
              磁盘排序和磁带排序，之所以这么分是因为外排序不但与排序的算法有关，还与外存设备的特征有关。结合外存设备特征，大体上可分为顺序存取（如磁带）和直接存取（如磁盘）两大类。磁带排序时间主要取决于对带的读写。（这里只是交代一下，实际上正如大家知道的，基本上现在已经淘汰了磁带存储的方式）需要指出的是外部排序的这两种方式的工作过程是一致的，外部排序的基本过程由相对独立的两个步骤组成： 

              １．按可用内存大小，利用内部排序的方法，构造若干(记录的)有序子序列，通常称外存中这些记录有序子序列为“归并段”; 
              ２．通过“归并”，逐步扩大(记录的)有序子序列的长度，直至外存中整个记录序列按关键字有序为止。 
              例如：假设有一个含10,000个记录的磁盘文件，而当前所用的计算机一次只能对1,000个记录进行内部排序，则首先利用内部排序的方法得到10个初始归并段，然后进行逐趟归并。 

              假设进行2&#61485;路归并(即两两归并)，则 
              第一趟由10个归并段得到5个归并段; 
              第二趟由 5 个归并段得到3个归并段; 
              第三趟由 3 个归并段得到2个归并段; 
              最后一趟归并得到整个记录的有序序列。 
              我们来分析上述外排过程中访问外存(对外存进行读/写)的次数：假设“数据块”的大小为200，即每一次访问外存可以读/写200个记录。则对于10,000个记录，处理一遍需访问外存100次(读和写各50次)。 

              由此，对上述例子而言， 
              1) 求得10个初始归并段需访问外存100次; 
              2) 每进行一趟归并需访问外存100次; 
              3) 总计访问外存 100 + 4 &#61620; 100 = 500次。 
              外排总的时间还应包括内部排序所需时间和逐趟归并时进行内部归并的时间，显然，除去内部排序的因素外，外部排序的时间取决于逐趟归并所需进行的“趟数”。 

              例如，若对上述例子采用5&#61485;路归并，则只需进行2趟归并，总的访问外存的次数将压缩到   100 + 2 &#61620; 100 = 300 次 
              一般情况下，假设待排记录序列含m个初始归并段，外排时采用k&#61485;路归并，则归并趟数为 
              &#61673;logkm&#61689;，显然，随之k的增大归并的趟数将减少，因此对外排而言，通常采用多路归并。k的大小可选，但需综合考虑各种因素。 
              上面谈的都是假设在单处理机上完成的工作，下面将谈谈并行排序： 
              并行排序：是指利用多台处理机（并行机）进行的排序，其目的主要是为了提高速度。并行排序算法虽然和前面谈到的单处理机上的串行排序算法有不少相似之处，但不能认为它只是它是串行算法的简单推广和扩充。它的最大特点之一就是他和并行计算机的体系结构密切相关，不同体系结构导致不同加速和不同设计风格的并行排序算法。 

              图与网络优化算法： 
                
              组合算法中内容最丰富的部分就是图与网络优化算法。图论中的计算问题包括图的搜索、路径问题、连通性问题、可平面性检验、着色问题、网络优化等。图论中的著名算法有：求最小生成树的Kruskal算法、求最短路径的Dijkstra算法和Floyd算法、求二部图最大匹配（指派问题）的匈牙利算法、求一般图最大匹配的Edmonds“花”算法、求网络最大流和最小割的算法等。 

              求最小生成树的Kruskal算法 
              由于这个是大家都熟悉的，我只简单的说说：为使生成树上边的权值之和最小，显然，其中每一条边的权值应该尽可能地小。Kruskal算法的做法就是：先构造一个只含n个顶点的子图SG，然后从权值最小的边开始，若它的添加不使SG中产生回路，则在SG上加上这条边，如此重复，直至加上n-1条边为止。算法如下: 

              构造非连通图 ST=( V,{ } ); 
              k = i = 0; 
              while (k ++i; 
              从边集 E 中选取第i条权值最小的边(u,v); 
              若(u,v)加入ST后不使ST中产生回路， 
              则  输出边(u,v);   
                   k++; 
              } 

              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 20:08:26       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 5 楼 



               
              求最短路径的Dijkstra算法： 
              Dijkstra算法是一种解决最短路径问题的非常有效的算法，时间复杂度为 
              O(│V│2)，下面是一段精确的描述（本段引自MIT的课程主页，不翻译了，保持原作）中文描述一般的书上都会有： 
              1. Set i=0, S0= {u0=s}, L(u0)=0, and L(v)=infinity for v <> u0. If 
              │V│ = 1 then stop, otherwise go to step 2. 
              2. For each v in V\Si, replace L(v) by min{L(v), L(ui)+dvui}. If 
              L(v) is replaced, put a label (L(v), ui) on v. 
              3. Find a vertex v which minimizes {L(v): v in V\Si}, say ui+1. 
              4. Let Si+1 = Si cup {ui+1}. 
              5. Replace i by i+1. If i=│V│-1 then stop, otherwise go to step 2. 

              6. Set i=0, S0= {u0=s}, L(u0)=0, and L(v)=infinity for v <> u0. If 
              │V│ = 1 then stop, otherwise go to step 2. 
              7. For each v in V\Si, replace L(v) by min{L(v), L(ui)+dvui}. If 
              L(v) is replaced, put a label (L(v), ui) on v. 
              8. Find a vertex v which minimizes {L(v): v in V\Si}, say ui+1. 
              9. Let Si+1 = Si cup {ui+1}. 
              10. Replace i by i+1. If i=│V│-1 then stop, otherwise go to step 
              2. 
              求二部图最大匹配（指派问题）的匈牙利算法： 
              谈匈牙利算法自然避不开Hall定理，即是：对于二部图G，存在一个匹配M，使得X的所有顶点关于M饱和的充要条件是：对于X的任意一个子集A，和A邻接的点集为T(A)，恒有： 
              │T(A)│ >= │A│ 
              匈牙利算法是基于Hall定理中充分性证明的思想，其基本步骤为： 
              1．任给初始匹配M； 
              2．若X已饱和则结束，否则进行第3步； 
              3．在X中找到一个非饱和顶点x0，作V1 ← {x0},  V2 ← Φ； 
              4．若T(V1) = V2则因为无法匹配而停止，否则任选一点y ∈T(V1)\V2； 
              5．若y已饱和则转6，否则做一条从x0 →y的可增广道路P，M←M⊕E(P)，转2； 
              6．由于y已饱和，所以M中有一条边(y,z)，作 V1 ← V1 ∪{z}, V2 ← V2 ∪ {y}， 转4； 
              关于求网络最大流和最小割的标号算法： 
              给定一个有向图G=(V,E)，把图中的边看作管道，每条边上有一个权值，表示该管道的流量上限。给定源点s和汇点t，现在假设在s处有一个水源，t处有一个蓄水池，问从s到t的最大水流量是多少。这就叫做网络流问题。用数学语言描述就是： 

              设G=(V,E)是一个流网络，设c(u, v)>＝0 表示从u到v的管道的流量上限。设s为源，t为汇。G的流是一个函数f: V×V 
              →R，且满足下面三个特征： 
              1. 容量限制：对于所有的 u,v ∈ V, 要求f(u, v) <= c(u, v) 
              2. 斜对称性：对于所有的 u,v ∈ V, 要求f(u, v) = - f(v, u) 
              3. 流的会话：对于所有的 u ∈ V - {s, t}，要求∑  f(u, v) = 0；v∈V 
              f(u,v)称为从结点u到v的网络流，它可以为正也可以为负。流 f 的值定义为： 
              │f│ =   ∑  f(s, v) 
                     v∈V 
              即从源出发的所有流的总和。 
              最大流问题就是找出给定流网络的最大流。网络流问题可以归结为一类特殊的线性规划问题。 
              寻找最大流的基本方法是Ford-Fulkerson方法，该方法有多种实现，其基本思想是从某个可行流F出发，找到关于这个流的一个可改进路经P，然后沿着P调整F，对新的可行流试图寻找关于他的可改进路经，如此反复直至求得最大流。现在要找最小费用的最大流，可以证明，若F是流量为V(F)的流中费用最小者，而P是关于F的所有可改进路中费用最小的可改进路，则沿着P去调整F,得到的可行流F'一定是流量为V(F')的所有可行流中的最小费用流。这样，当F是最大流时候，他就是所要求的最小费用最大流。 

              注意到每条边的单位流量费用B(i,j)≥0，所以F=0必是流量为0的最小费用流，这样总可以 
              从F=0出发求出最小费用最大流。一般的，设已知F是流量V(F)的最小费用流，余下的问题就是如何去寻找关于F的最小费用可改进路。为此我们将原网络中的每条弧变成两条方向相反的弧： 

              1。前向弧，容量C和费用B不变，流量F为0； 
              2。后向弧，容量C为0，费用为-B，流量F为0； 
              每一个顶点上设置一个参数CT，表示源点至该顶点的通路上的费用和。如果我们得出一条关于F的最小费用可改进路时，则该路上的每一个顶点的CT值相对于其它可改进路来说是最小的。每一次寻找最小费用可改进路时前，源点的CT为0，其它顶点的CT为+∞。 

              设cost为流的运输费用，初始时由于F=0,则cost=0,我们每求出一条关于F的最小费用可改进路，则通过cost ← cost + 
              ∑B(e)*d, （其中e∈P,d为P的可改进量）来累积流的运输费用 
              的增加量。显然，当求出最小费用最大流时，cost便成为最大流的运输费用了。 
              另外设置布尔变量break为最小费用可改进路的延伸标志，在搜索了网络中的每一个顶点后 
              ，若break=true表示可改进路还可以延伸，还需要重新搜索网络中的顶点；否则说明最小费 
              用的可改进路已经找到或者最大流已经求出。 
              下面是算法的伪代码： 
              cost  ← 0; 
              repeat 
              可改进路撤空； 
              设源点的CT值为0并进入可改进路； 
              repeat 
                 break  ← false; 
                 for u ←1 to N do 
                   begin 
                     分析U出发的所有弧; 
                     if (的流量可改进）and(源点至U有通路)and(U的CT值+的费用 < V的CT值) then 
                       begin 
                         break  ← true; 
                         V的CT值  ← U的CT值+的费用； 
                         V进入可改进路经并为之标号； 
                       end if 
                   end for 
              until break=false 
              if 汇点已标号 then 
                 begin 
                   从汇点出发倒向修正可改进路的流量； 
                   cost ← cost + ∑B(e)*d（其中e∈P,d为P的可改进量）； 
                 end if 
              until 汇点未标号； 
              可见，上述的算法和求最大流的Edmonds-Karp标号算法几乎一样，因为这两种算法都使用宽度优先搜索来来寻找增广路径，所以复杂度也相同，都是O(VE)，其中V是节点数目，E是边数目。 

              其他的就不详述了，大家感兴趣的可以查阅TAOCP或者是算法导论的相关内容。 

              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 20:09:12       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 6 楼 



               
              贪心法与拟阵： 
              贪心法是求解关于独立系统组合优化问题的一种简单算法，求最小生成树的Kruskal算法就是一种贪心算法。但是贪心法并不总能找到最优独立集。贪心法能求得最优独立集的充分必要条件是L为一个拟阵。事实上，求最大生成树是关于拟阵的组合优化问题，而二部图的所有匹配构成的独立系统U不是拟阵。 

              贪心法的基本思路是：从问题的某一个初始解出发逐步逼近给定的目标，以尽可能快的地求得更好的解。当达到某算法中的某一步不能再继续前进时，算法停止。 

              该算法存在问题： 
              1. 不能保证求得的最后解是最佳的； 
              2. 不能用来求最大或最小解问题； 
              3. 只能求满足某些约束条件的可行解的范围。 
              实现该算法的过程： 
              从问题的某一初始解出发； 
              while 能朝给定总目标前进一步 do 
              　　求出可行解的一个解元素； 
              由所有解元素组合成问题的一个可行解； 
              穷举搜索： 
                 
              组合算法要解决的问题只有有限种可能，在没有跟好算法时总可以用穷举搜索的办法解决，即逐个的检查所有可能的情况。可以想象，情况较多时这种方法极为费时。实际上并不需要机械的检查每一种情况，常常是可以提前判断出某些情况不可能取到最优解，从而可以提前舍弃这些情况。这样也是隐含的检查了所有可能的情况，既减少了搜索量，又保证了不漏掉最优解。这方面怒火之炮写过文章，我认为没必要敖述了。 

              分支限界法： 
              这是一种用于求解组合优化问题的排除非解的搜索算法。类似于回溯法，分枝定界法在搜索解空间时，也经常使用树形结构来组织解空间。然而与回溯法不同的是，回溯算法使用深度优先方法搜索树结构，而分枝定界一般用宽度优先或最小耗费方法来搜索这些树。因此，可以很容易比较回溯法与分枝定界法的异同。相对而言，分枝定界算法的解空间比回溯法大得多，因此当内存容量有限时，回溯法成功的可能性更大。 

              算法思想：分枝定界（branch and 
              bound）是另一种系统地搜索解空间的方法，它与回溯法的主要区别在于对E-节点的扩充方式。每个活节点有且仅有一次机会变成E-节点。当一个节点变为E-节点时，则生成从该节点移动一步即可到达的所有新节点。在生成的节点中，抛弃那些不可能导出（最优）可行解的节点，其余节点加入活节点表，然后从表中选择一个节点作为下一个E-节点。从活节点表中取出所选择的节点并进行扩充，直到找到解或活动表为空，扩充过程才结束。 

              有两种常用的方法可用来选择下一个E-节点（虽然也可能存在其他的方法）： 
              1) 先进先出（F I F O） 即从活节点表中取出节点的顺序与加入节点的顺序相同，因此活 
              节点表的性质与队列相同。 
              2) 最小耗费或最大收益法在这种模式中，每个节点都有一个对应的耗费或收益。如果查找 
              一个具有最小耗费的解，则活节点表可用最小堆来建立，下一个E-节点就是具有最小耗费 
              的活节点；如果希望搜索一个具有最大收益的解，则可用最大堆来构造活节点表，下一个 
              E-节点是具有最大收益的活节点。 
              动态规划： 
              动态规划(dynamic programming)是运筹学的一个分支，是求解决策过程(decision 
              process)最优化的数学方法。20世纪50年代初美国数学家R.E.Bellman等人在研究 
              多阶段决策过程(multistep decision process)的优化问题时，提出了著名的最优化原理(principle of 
              optimality)，把多阶段过程转化为一系列单阶段问题，逐个求解，创立了解决这类过程优化问题的新方法——动态规划。1957年出版了他的名著Dynamic 
              Programming，这是该领域的第一本著作。动态规划问世以来，在经济管理、生产调度、工程技术和最优控制等方面得到了广泛的应用。例如最短路线、库存管理、资源分配、设备更新、排序、装载等问题，用动态规划方法比用其它方法求解更为方便。虽然动态规划主要用于求解以时间划分阶段的动态过程的优化问题，但是一些与时间无关的静态规划(如线性规划、非线性规划)，只要人为地引进时间因素，把它视为多阶段决策过程，也可以用动态规划方法方便地求解。 

              一般来说，只要问题可以划分成规模更小的子问题，并且原问题的最优解中包含了 
              子问题的最优解（即满足最优子化原理），则可以考虑用动态规划解决。动态规划的实质是分治思想和解决冗余，因此，动态规划是一种将问题实例分解为更小的、相似的子问题，并存储子问题的解而避免计算重复的子问题，以解决最优化问题的算法策略。 

              由此可知，动态规划法与分治法和贪心法类似，它们都是将问题实例归纳为更小的、相似的子问题，并通过求解子问题产生一个全局最优解。其中贪心法的当前选择可能要依赖已经作出的所有选择，但不依赖于有待于做出的选择和子问题。因此贪心法自顶向下，一步一步地作出贪心选择；而分治法中的各个子问题是独立的 
              (即不包含公共的子子问题)，因此一旦递归地求出各子问题的解后，便可自下而上地将子问题的解合并成问题的解。但不足的是，如果当前选择可能要依赖子问题的解时，则难以通过局部的贪心策略达到全局最优解；如果各子问题是不独立的，则分治法要做许多不必要的工作，重复地解公共的子问题。解决上述问题的办法是利用动态规划。该方法主要应用于最优化问题，这类问题会有多种可能的解，每个解都有一个值，而动态规划找出其中最优(最大或最小)值的解。若存在若干个取最优值的解的话，它只取其中的一个。在求解过程中，该方法也是通过求解局部子问题的解达到全局最优解，但与分治法和贪心法不同的是，动态规划允许这些子问题不独立，(亦即各子问题可包含公共的子子问题)也允许其通过自身子问题的解作出选择，该方法对每一个子问题只解一次，并将结果保存起来，避免每次碰到时都要重复计算。 

              因此，动态规划法所针对的问题有一个显著的特征，即它所对应的子问题树中的子问题呈现大量的重复。动态规划法的关键就在于，对于重复出现的子问题，只在第一次遇到时加以求解，并把答案保存起来，让以后再遇到时直接引用，不必重新求解。 

              设计一个标准的动态规划算法，通常可按以下几个步骤进行： 
              1．划分阶段：按照问题的时间或空间特征，把问题分为若干个阶段。注意这若干 
              个阶段一定要是有序的或者是可排序的（即无后向性），否则问题就无法用动态规 
              划求解。 
              2．选择状态：将问题发展到各个阶段时所处于的各种客观情况用不同的状态表示 
              出来。当然，状态的选择要满足无后效性。 
              确定决策并写出状态转移方程：之所以把这两步放在一起，是因为决策和状态转移 
              有着天然的联系，状态转移就是根据上一阶段的状态和决策来导出本阶段的状态。 
              所以，如果我们确定了决策，状态转移方程也就写出来了。但事实上，我们常常是 
              反过来做，根据相邻两段的各状态之间的关系来确定决策。 
              3．写出规划方程（包括边界条件）：动态规划的基本方程是规划方程的通用形式 
              化表达式。一般说来，只要阶段、状态、决策和状态转移确定了，这一步还是比较 
              简单的。 动态规划的主要难点在于理论上的设计，一旦设计完成，实现部分就会非常简单。 
              分治法： 
              对于一个规模为n的问题，若该问题可以容易地解决（比如说规模n较小）则直接解 
              决，否则将其分解为k个规模较小的子问题，这些子问题互相独立且与原问题形式相同，递归地解这些子问题，然后将各子问题的解合并得到原问题的解。这种算法设计策略叫做分治法。 
              任何一个可以用计算机求解的问题所需的计算时间都与其规模有关。问题的规模越小，越容易直接求解，解题所需的计算时间也越少。例如，对于n个元素的排序问题，当n=1时，不需任何计算。n=2时，只要作一次比较即可排好序。n=3时只要作3次比较即可，…。而当n较大时，问题就不那么容易处理了。要想直接解决一个规模较大的问题，有时是相当困难的。分治法的设计思想是，将一个难以直接解决的大问题，分割成一些规模较小的相同问题，以便各个击破，分而治之。 

                  如果原问题可分割成k个子问题，1 < k ≤ n 
              ，且这些子问题都可解，并可利用这些子问题的解求出原问题的解，那么这种分治法就是可行的。由分治法产生的子问题往往是原问题的较小模式，这就为使用递归技术提供了方便。在这种情况下，反复应用分治手段，可以使子问题与原问题类型一致而其规模却不断缩小，最终使子问题缩小到很容易直接求出其解。这自然导致递归过程的产生。分治与递归像一对孪生兄弟，经常同时应用在算法设计之中，并由此产生许多高效算法。 

              其基本步骤是： 
              分解：将原问题分解为若干个规模较小，相互独立，与原问题形式相同的子问题； 
              解决：若子问题规模较小而容易被解决则直接解，否则递归地解各个子问题； 
              合并：将各个子问题的解合并为原问题的解。 
              它的一般的算法设计模式如下： 
              Divide-and-Conquer(P) 
              1．if │P│≤n0 
              2．then return( ADHOC(P) ) 
              3．将P分解为较小的子问题 P1 ,P2 ,...,Pk 
              4．for i←1 to k 
              5．do yi ← Divide-and-Conquer(Pi)     △ 递归解决Pi 
              6．T ← MERGE(y1,y2,...,yk)          △ 合并子问题 
              7．return(T) 
              其中│P│表示问题P的规模；n0为一阈值，表示当问题P的规模不超过n0时，问题已 
              容易直接解出，不必再继续分解。ADHOC(P)是该分治法中的基本子算法，用于直接 
              解小规模的问题P。因此，当P的规模不超过n0时，直接用算法ADHOC(P)求解。算法 
              MERGE(y1,y2,...,yk)是该分治法中的合并子算法，用于将P的子问题P1 ,P2 ,... 
              ,Pk的相应的解y1,y2,...,yk合并为P的解。 
              根据分治法的分割原则，原问题应该分为多少个子问题才较适宜？各个子问题的规 
              模应该怎样才为适当？这些问题很难予以肯定的回答。但人们从大量实践中发现， 
              在用分治法设计算法时，最好使子问题的规模大致相同。换句话说，将一个问题分 
              成大小相等的k个子问题的处理方法是行之有效的。许多问题可以取k=2。这种使子 
              问题规模大致相等的做法是出自一种平衡(balancing)子问题的思想，它几乎总是 
              比子问题规模不等的做法要好。 
              分治法的合并步骤是算法的关键所在。有些问题的合并方法比较明显，有些问题合并方法比较复杂，或者是有多种合并方案，或者是合并方案不明显，究竟应该怎样合并，没有统一的模式，需要具体问题具体分析。 

                   其他的一些经典的算法，如快速傅里叶变换，大家都非常熟悉，这里就不再涉及。如果想深入学习不妨参考San Diego 
              州立大学的相关课程主页 
              http://www.eli.sdsu.edu/courses/fall95/cs660/notes/ 
              组合算法的设计是一门艺术，需要高度的技巧和灵感。算法分析的任务是分析算法的优劣，算法分析的任务是分析算法的优劣，主要是讨论算法的时间复杂性和空间复杂性。它的理论基础是组合分析，包括计数和枚举。计算复杂性理论，特别是NP完全性理论，与组合算法是紧密相关的。NP完全性概念的提出，正是为了刻画包括旅行商问题、图着色问题、图着色问题、整数规划等一大批组合问题的计算难度。计算复杂性理论研究算法在时间和空间限制下的能力以及问题的难度，使组合算法的研究有了更加清晰的框架，将组合算法的研究提高到一个新的水平。 



              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 20:09:33       

              wgd243  
        
        
        等级：新手上路 
        文章：8
        积分：100
        注册：2004-3-27
                        第 7 楼 



               

              thanks

       2004-8-15 10:51:40       

              飞云0616  
        
        
        头衔：云 
        等级：黑侠 
        威望：1
        文章：713
        积分：973
        门派：☆nudter☆ 
        注册：2003-8-9
                         第 8 楼 



               

              我还没看
              谢谢楼主的工作
              我一定会仔细看一遍的


              ----------------------------------------------
              路过绿洲，就要留住！
              留住爱情，感受生活！ 

       2004-8-17 14:53:35       

              wenhairong  
        
        
        等级：新手上路 
        文章：2
        积分：302
        门派：☆nudter☆ 
        注册：2004-8-1
                        第 9 楼 



               

              thinks
              经典

       2004-8-17 20:14:46       

              cloud_drift  
        
        
        等级：新手上路 
        文章：8
        积分：298
        门派：☆nudter☆ 
        注册：2004-8-4
                        第 10 楼 



               
              楼主好样的！ 

       2004-8-18 14:19:26       

      本主题贴数 15   分页：9 1 2 :   跳转论坛至...╋数学建模  ├数模竞赛  ├新手入门  ├数学工具  ├资源与检索╋学术区  
        ├数学思想  ├编程交流  ├学术杂谈  ├English Fans╋休闲专区  ├灌水搞笑专区  ├神秘园╋本站站务  ├站务讨论  
        ├数模管理区  ├回收站


       *快速回复：组合算法概论
           发贴表情
                  
                  
                  
                  
                  
                  

               段落格式 普通格式标题 1标题 2标题 3标题 4标题 5标题 6标题 7已编排格式地址  
              字体宋体黑体楷体仿宋隶书幼圆新宋体细明体ArialArial BlackCourierVerdanaWide 
              LatinWingdings  字号1234567              


                      第 1 页,共 7 页， 49 个

       显示签名     内容限制：字节. 


      管理选项： 专题管理 | 修复 | 锁定 | 解锁 | 提升 | 跟贴管理 | 删除 | 移动 | 设置固顶 | 奖励 | 惩罚 | 发布公告 

            Copyright &copy;2002 - 2004 Shumo.Com
            执行时间：156.25000毫秒。查询数据库5次。
            当前模板样式：[默认模板] 
````

</details>

#### 中国数学建模-编程交流-贪婪算法_1 · MATLAB · c0828ea8

- 归属算法：Dijkstra最短路
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Dijkstra最短路中的“结果绘图与展示”。
- **执行主线**：通过松弛操作求单源最短路径；选择低权边构造最小生成树；执行选择、交叉和变异的进化搜索；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9521da8225fcaa9be49d08fe4cec8582acce02662ed2db86291bc651922d68ef`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/贪婪算法/中国数学建模-编程交流-贪婪算法_1.txt`

<details>
<summary>展开原始代码</summary>

````matlab
中国数学建模-编程交流-贪婪算法
        wh-ee 重登录  隐身  用户控制面板  搜索  风格  论坛状态  论坛展区  社区服务  社区休闲  网站首页  退出 

      >> VC++,C,Perl,Asp...编程学习,算法介绍.  我的收件箱 (0) 
       中国数学建模 → 学术区 → 编程交流 → 贪婪算法 

             您是本帖的第 889 个阅读者       
             * 贴子主题：贪婪算法           

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28

        鲜花(0)  鸡蛋(0)             楼主 



               贪婪算法

              第 1 章  贪婪算法
              虽然设计一个好的求解算法更像是一门艺术，而不像是技术，但仍然存在一些行之有效的能够用于解决许多问题的算法设计方法，你可以使用这些方法来设计算法，并观察这些算法是如何工作的。一般情况下，为了获得较好的性能，必须对算法进行细致的调整。但是在某些情况下，算法经过调整之后性能仍无法达到要求，这时就必须寻求另外的方法来求解该问题。
              本章首先引入最优化的概念，然后介绍一种直观的问题求解方法：贪婪算法。最后，应用该算法给出货箱装船问题、背包问题、拓扑排序问题、二分覆盖问题、最短路径问题、最小代价生成树等问题的求解方案。
              1.1 最优化问题
              本章及后续章节中的许多例子都是最优化问题（ optimization problem），每个最优化问题都包含一组限制条件（ c o 
              n s t r a i n t）和一个优化函数（ optimization 
              function），符合限制条件的问题求解方案称为可行解（ feasible 
              solution），使优化函数取得最佳值的可行解称为最优解（optimal solution）。
              例1-1 [ 渴婴问题] 
              有一个非常渴的、聪明的小婴儿，她可能得到的东西包括一杯水、一桶牛奶、多罐不同种类的果汁、许多不同的装在瓶子或罐子中的苏打水，即婴儿可得到n 
              种不同的饮料。根据以前关于这n 
              种饮料的不同体验，此婴儿知道这其中某些饮料更合自己的胃口，因此，婴儿采取如下方法为每一种饮料赋予一个满意度值：饮用1盎司第i 
              种饮料，对它作出相对评价，将一个数值si 作为满意度赋予第i 种饮料。
              通常，这个婴儿都会尽量饮用具有最大满意度值的饮料来最大限度地满足她解渴的需要，但是不幸的是：具有最大满意度值的饮料有时并没有足够的量来满足此婴儿解渴的需要。设ai是第i 
              种饮料的总量（以盎司为单位），而此婴儿需要t 盎司的饮料来解渴，那么，需要饮用n种不同的饮料各多少量才能满足婴儿解渴的需求呢？
              设各种饮料的满意度已知。令xi 为婴儿将要饮用的第i 种饮料的量，则需要解决的问题是：
              找到一组实数xi（1≤i≤n），使n &aring;i = 1si xi 最大，并满足：n &aring;i=1xi =t 及0≤xi≤ai 。
              需要指出的是：如果n &aring;i = 1ai < t，则不可能找到问题的求解方案，因为即使喝光所有的饮料也不能使婴儿解渴。
              对上述问题精确的数学描述明确地指出了程序必须完成的工作，根据这些数学公式，可以对输入/ 输出作如下形式的描述：
              输入：n，t，si ，ai（其中1≤i≤n，n 为整数，t、si 、ai 为正实数）。
              输出：实数xi（1≤i≤n），使n &aring;i= 1si xi 最大且n &aring;i=1xi =t（0≤xi≤ai）。如果n &aring;i = 1ai 
              <t，则输出适当的错误信息。
              在这个问题中，限制条件是n &aring;i= 1xi =t 且0≤xi≤ai，1≤i≤n。而优化函数是n &aring;i= 1si xi 
              。任何满足限制条件的一组实数xi 都是可行解，而使n &aring;i= 1si xi 最大的可行解是最优解。
              例1-2 [装载问题] 有一艘大船准备用来装载货物。所有待装货物都装在货箱中且所有货箱的大小都一样，但货箱的重量都各不相同。设第i 
              个货箱的重量为wi（1≤i≤n），而货船的最大载重量为c，我们的目的是在货船上装入最多的货物。
              这个问题可以作为最优化问题进行描述：设存在一组变量xi ，其可能取值为0或1。如xi 为0，则货箱i 将不被装上船；如xi 
              为1，则货箱i 将被装上船。我们的目的是找到一组xi ，使它满足限制条件n &aring;i = 1wi xi ≤c 且x i &Icirc; {0, 
              1}, 1 ≤i≤n。相应的优化函数是n &aring;i= 1xi 。
              满足限制条件的每一组xi 都是一个可行解，能使n &aring;i= 1xi 取得最大值的方案是最优解。
              例1-3 [最小代价通讯网络] 
              城市及城市之间所有可能的通信连接可被视作一个无向图，图的每条边都被赋予一个权值，权值表示建成由这条边所表示的通信连接所要付出的代价。包含图中所有顶点（城市）的连通子图都是一个可行解。设所有的权值都非负，则所有可能的可行解都可表示成无向图的一组生成树，而最优解是其中具有最小代价的生成树。
              在这个问题中，需要选择一个无向图中的边集合的子集，这个子集必须满足如下限制条件：所有的边构成一个生成树。而优化函数是子集中所有边的权值之和。


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:37:49      

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 2 楼 



               

              1.2 算法思想
              在贪婪算法（greedy 
              method）中采用逐步构造最优解的方法。在每个阶段，都作出一个看上去最优的决策（在一定的标准下）。决策一旦作出，就不可再更改。作出贪婪决策的依据称为贪婪准则（greedy 
              criterion）。
              例1-4 [找零钱] 
              一个小孩买了价值少于1美元的糖，并将1美元的钱交给售货员。售货员希望用数目最少的硬币找给小孩。假设提供了数目不限的面值为2 
              5美分、1 
              0美分、5美分、及1美分的硬币。售货员分步骤组成要找的零钱数，每次加入一个硬币。选择硬币时所采用的贪婪准则如下：每一次选择应使零钱数尽量增大。为保证解法的可行性（即：所给的零钱等于要找的零钱数），所选择的硬币不应使零钱总数超过最终所需的数目。
              假设需要找给小孩6 7美分，首先入选的是两枚2 5美分的硬币，第三枚入选的不能是2 
              5美分的硬币，否则硬币的选择将不可行（零钱总数超过6 7美分），第三枚应选择1 
              0美分的硬币，然后是5美分的，最后加入两个1美分的硬币。
              贪婪算法有种直觉的倾向，在找零钱时，直觉告诉我们应使找出的硬币数目最少（至少是接近最少的数目）。可以证明采用上述贪婪算法找零钱时所用的硬币数目的确最少（见练习1）。
              例1-5 [机器调度] 现有n 件任务和无限多台的机器，任务可以在机器上得到处理。每件任务的开始时间为si，完成时间为fi ，si 
              < fi 。[si , fi ] 为处理任务i 的时间范围。两个任务i，j 重指两个任务的时间范围区间有重叠，而并非是指i，j 
              的起点或终点重合。例如：区间[ 1，4 ]与区间[ 2，4 ]重叠，而与区间[ 4，7 
              ]不重叠。一个可行的任务分配是指在分配中没有两件重叠的任务分配给同一台机器。因此，在可行的分配中每台机器在任何时刻最多只处理一个任务。最优分配是指使用的机器最少的可行分配方案。
              假设有n= 7件任务，标号为a 到g。它们的开始与完成时间如图13-1a 所示。若将任务a分给机器M1，任务b 分给机器M2，. . 
              .，任务g 
              分给机器M7，这种分配是可行的分配，共使用了七台机器。但它不是最优分配，因为有其他分配方案可使利用的机器数目更少，例如：可以将任务a、b、d分配给同一台机器，则机器的数目降为五台。
              一种获得最优分配的贪婪方法是逐步分配任务。每步分配一件任务，且按任务开始时间的非递减次序进行分配。若已经至少有一件任务分配给某台机器，则称这台机器是旧的；若机器非旧，则它是新的。在选择机器时，采用以下贪婪准则：根据欲分配任务的开始时间，若此时有旧的机器可用，则将任务分给旧的机器。否则，将任务分配给一台新的机器。
              根据例子中的数据，贪婪算法共分为n = 7步，任务分配的顺序为a、f、b、c、g、e、d。第一步没有旧机器，因此将a 
              分配给一台新机器（比如M1）。这台机器在0到2时刻处于忙状态。在第二步，考虑任务f。由于当f 启动时旧机器仍处于忙状态，因此将f 
              分配给一台新机器(设为M2 )。第三步考虑任务b, 由于旧机器M1在Sb = 
              3时刻已处于闲状态，因此将b分配给M1执行，M1下一次可用时刻变成fb = 7，M2的可用时刻变成ff = 
              5。第四步，考虑任务c。由于没有旧机器在Sc = 4时刻可用，因此将c 分配给一台新机器（M3），这台机器下一次可用时间为fc = 
              7。第五步考虑任务g，将其分配给机器M2，第六步将任务e 分配给机器M1, 最后在第七步，任务2分配给机器M3。（注意：任务d 
              也可分配给机器M2）。
              上述贪婪算法能导致最优机器分配的证明留作练习（练习7）。可按如下方式实现一个复杂性为O (nl o 
              gn)的贪婪算法：首先采用一个复杂性为O (nl o gn)的排序算法（如堆排序）按Si 
              的递增次序排列各个任务，然后使用一个关于旧机器可用时间的最小堆。
              例1-6 [最短路径] 给出一个有向网络，路径的长度定义为路径所经过的各边的耗费之和。要求找一条从初始顶点s 到达目的顶点d 
              的最短路径。
              贪婪算法分步构造这条路径，每一步在路径中加入一个顶点。假设当前路径已到达顶点q，
              且顶点q 并不是目的顶点d。加入下一个顶点所采用的贪婪准则为：选择离q 最近且目前不在路径中的顶点。
              这种贪婪算法并不一定能获得最短路径。例如，假设在图1 3 - 
              2中希望构造从顶点1到顶点5的最短路径，利用上述贪婪算法，从顶点1开始并寻找目前不在路径中的离顶点1最近的顶点。到达顶点3，长度仅为2个单位，从顶点3可以到达的最近顶点为4，从顶点4到达顶点2，最后到达目的顶点5。所建立的路径为1 
              , 3 , 4 , 2 , 5，其长度为1 
              0。这条路径并不是有向图中从1到5的最短路径。事实上，有几条更短的路径存在，例如路径1，4，5的长度为6。
              根据上面三个例子，回想一下前几章所考察的一些应用，其中有几种算法也是贪婪算法。例如，霍夫曼树算法，利用n- 
              1步来建立最小加权外部路径的二叉树，每一步都将两棵二叉树合并为一棵，算法中所使用的贪婪准则为：从可用的二叉树中选出权重最小的两棵。L 
              P T调度规则也是一种贪婪算法，它用n 步来调度n 
              个作业。首先将作业按时间长短排序，然后在每一步中为一个任务分配一台机器。选择机器所利用的贪婪准则为：使目前的调度时间最短。将新作业调度到最先完成的机器上（即最先空闲的机器）。
              注意到在机器调度问题中，贪婪算法并不能保证最优，然而，那是一种直觉的倾向且一般情况下结果总是非常接近最优值。它利用的规则就是在实际环境中希望人工机器调度所采用的规则。算法并不保证得到最优结果，但通常所得结果与最优解相差无几，这种算法也称为启发式方法（ 
              h e u r i s t i c s )。因此L P T方法是一种启发式机器调度方法。定理9 - 2陈述了L P 
              T调度的完成时间与最佳调度的完成时间之间的关系，因此L P T启发式方法具有限定性
              能（ bounded performance ）。具有限定性能的启发式方法称为近似算法（ a p p r o x i m a t i 
              o na l g o r i t h m）。
              本章的其余部分将介绍几种贪婪算法的应用。在有些应用中，贪婪算法所产生的结果总是最优的解决方案。但对其他一些应用，生成的算法只是一种启发式方法，可能是也可能不是近似算法。


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:39:12       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 3 楼 



               

              练习
              1. 证明找零钱问题（例1 3 - 4）的贪婪算法总能产生具有最少硬币数的零钱。
              2. 考虑例1 3 - 4的找零钱问题，假设售货员只有有限的2 5美分， 1 0美分， 
              5美分和1美分的硬币，给出一种找零钱的贪婪算法。这种方法总能找出具有最少硬币数的零钱吗？证明结论。
              3. 扩充例1 3 - 4的算法，假定售货员除硬币外还有50, 20, 10, 5, 和1美元的纸币，顾客买价格为x 美元和y 
              美分的商品时所付的款为u 美元和v 美分。算法总能找出具有最少纸币与硬币数目的零钱吗？证明结论。
              4. 编写一个C + +程序实现例1 3 - 4的找零钱算法。假设售货员具有面值为1 0 0，2 0，1 
              0，5和1美元的纸币和各种硬币。程序可包括输入模块（即输入所买商品的价格及顾客所付的钱数），输出模块（输出零钱的数目及要找的各种货币的数目）和计算模块（计算怎样给出零钱）。
              5. 假设某个国家所使用硬币的币值为1 4 , 2 , 5和1分，则例1 3 - 
              4的贪婪算法总能产生具有最少硬币数的零钱吗？证明结论。
              6. 1) 证明例1 3 - 5的贪婪算法总能找到最优任务分配方案。
              2) 实现这种算法，使其复杂性为O (nl o gn)（提示：根据完成时间建立最小堆）。
              *7. 考察例1 3 - 
              5的机器调度问题。假定仅有一台机器可用，那么将选择最大数量的任务在这台机器上执行。例如，所选择的最大任务集合为{a,b,e}。解决这种任务选择问题的贪婪算法可按步骤选择任务，每步选择一个任务，其贪婪准则如下：从剩下的任务中选择具有最小的完成时间且不会与现有任务重叠的任务。
              1) 证明上述贪婪算法能够获得最优选择。
              2) 实现该算法，其复杂性应为O(nl o gn)。（提示：采用一个完成时间的最小堆）


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:39:26       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 4 楼 



               

              1.3 应用
              1.3.1 货箱装船
              这个问题来自例1  - 
              2。船可以分步装载，每步装一个货箱，且需要考虑装载哪一个货箱。根据这种思想可利用如下贪婪准则：从剩下的货箱中，选择重量最小的货箱。这种选择次序可以保证所选的货箱总重量最小，从而可以装载更多的货箱。根据这种贪婪策略，首先选择最轻的货箱，然后选次轻的货箱，如此下去直到所有货箱均装上船或船上不能再容纳其他任何一个货箱。
              例1-7 假设n =8, [w1 , ... w8 ]=[100,200,50,90,150,50,20,80], c= 4 0 
              0。利用贪婪算法时，所考察货箱的顺序为7 , 3 , 6 , 8 , 4 , 1 , 5 , 2。货箱7 , 3 , 6 , 8 , 
              4 , 1的总重量为3 9 0个单位且已被装载，剩下的装载能力为1 0个单位，小于剩下的任何一个货箱。在这种贪婪解决算法中得到[x1 
              , ..., x8 ] = [ 1 , 0 , 1 , 1 , 0 , 1 , 1 , 1 ]且&aring;xi = 6。
              定理1-1 利用贪婪算法能产生最佳装载。
              证明可以采用如下方式来证明贪婪算法的最优性：令x = [x1 , ..., xn ]为用贪婪算法获得的解，令y =[ y1 , 
              ..., yn ]为任意一个可行解，只需证明n &aring;i= 1xi ≥n &aring;i= 1yi 
              。不失一般性，可以假设货箱都排好了序：即wi≤wi + 1（1≤i≤n）。然后分几步将y 
              转化为x，转换过程中每一步都产生一个可行的新y，且n &aring;i = 1yi 大于等于未转化前的值，最后便可证明n &aring;i = 1xi ≥n 
              &aring;j = 1yi 。
              根据贪婪算法的工作过程，可知在[0, n] 的范围内有一个k，使得xi =1, i≤k且xi =0, i>k。寻找[ 1 
              ,n]范围内最小的整数j，使得xj≠yj 。若没有这样的j 存在，则n &aring;i= 1xi =n &aring;i = 1yi 。如果有这样的j 
              存在，则j≤k，否则y 就不是一个可行解，因为xj≠yj ，xj = 1且yj = 0。令yj = 1，若结果得到的y 
              不是可行解，则在[ j+ 1 ,n]范围内必有一个l 使得yl = 1。令yl = 0，由于wj≤wl ，则得到的y 
              是可行的。而且，得到的新y 至少与原来的y 具有相同数目的1。
              经过数次这种转化，可将y 转化为x。由于每次转化产生的新y 至少与前一个y 具有相同数目的1，因此x 至少与初始的y 
              具有相同的数目1。货箱装载算法的C + +代码实现见程序1 3 - 1。由于贪婪算法按货箱重量递增的顺序装载，程序1 3 - 
              1首先利用间接寻址排序函数I n d i r e c t S o r t对货箱重量进行排序（见3 . 
              5节间接寻址的定义），随后货箱便可按重量递增的顺序装载。由于间接寻址排序所需的时间为O (nl o gn)（也可利用9 . 5 . 
              1节的堆排序及第2章的归并排序），算法其余部分所需时间为O (n)，因此程序1 3 - 1的总的复杂性为O (nl o gn)。
              程序13-1 货箱装船
              template<class T>
              void ContainerLoading(int x[], T w[], T c, int n)
              {// 货箱装船问题的贪婪算法
              // x[i] = 1 当且仅当货箱i被装载， 1<=i<=n
              // c是船的容量, w 是货箱的重量
              // 对重量按间接寻址方式排序
              // t 是间接寻址表
              int *t = new int [n+1];
              I n d i r e c t S o r t ( w, t, n);
              // 此时, w[t[i]] <= w[t[i+1]], 1<=i<n
              // 初始化x
              for (int i = 1; i <= n; i++)
              x[i] = 0;
              // 按重量次序选择物品
              for (i = 1; i <= n && w[t[i]] <= c; i++) {
              x[t[i]] = 1;
              c -= w[t[i]];} // 剩余容量
              delete [] t;
              }


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:39:39       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 5 楼 



               

              1.3.2 0/1背包问题
              在0 / 1背包问题中，需对容量为c 的背包进行装载。从n 个物品中选取装入背包的物品，每件物品i 的重量为wi ，价值为pi 
              。对于可行的背包装载，背包中物品的总重量不能超过背包的容量，最佳装载是指所装入的物品价值最高，即n &aring;i=1pi xi 
              取得最大值。约束条件为n &aring;i =1wi xi≤c 和xi&Icirc;[ 0 , 1 ] ( 1≤i≤n)。
              在这个表达式中，需求出xt 的值。xi = 1表示物品i 装入背包中，xi =0 表示物品i 不装入背包。0 / 
              1背包问题是一个一般化的货箱装载问题，即每个货箱所获得的价值不同。货箱装载问题转化为背包问题的形式为：船作为背包，货箱作为可装入背包的物品。
              例1-8 在杂货店比赛中你获得了第一名，奖品是一车免费杂货。店中有n 
              种不同的货物。规则规定从每种货物中最多只能拿一件，车子的容量为c，物品i 需占用wi 的空间，价值为pi 
              。你的目标是使车中装载的物品价值最大。当然，所装货物不能超过车的容量，且同一种物品不得拿走多件。这个问题可仿照0 / 
              1背包问题进行建模，其中车对应于背包，货物对应于物品。
              0 / 
              1背包问题有好几种贪婪策略，每个贪婪策略都采用多步过程来完成背包的装入。在每一步过程中利用贪婪准则选择一个物品装入背包。一种贪婪准则为：从剩余的物品中，选出可以装入背包的价值最大的物品，利用这种规则，价值最大的物品首先被装入（假设有足够容量），然后是下一个价值最大的物品，如此继续下去。这种策略不能保证得到最优解。例如，考虑n=2, 
              w=[100,10,10], p =[20,15,15], c = 1 0 5。当利用价值贪婪准则时，获得的解为x= [ 1 , 0 
              , 0 ]，这种方案的总价值为2 0。而最优解为[ 0 , 1 , 1 ]，其总价值为3 0。
              另一种方案是重量贪婪准则是：从剩下的物品中选择可装入背包的重量最小的物品。虽然这种规则对于前面的例子能产生最优解，但在一般情况下则不一定能得到最优解。考虑n= 
              2 ,w=[10,20], p=[5,100], c= 2 5。当利用重量贪婪策略时，获得的解为x =[1,0], 比最优解[ 0 
              , 1 ]要差。
              还可以利用另一方案，价值密度pi /wi 贪婪算法，这种选择准则为：从剩余物品中选择可
              装入包的pi /wi 值最大的物品，这种策略也不能保证得到最优解。利用此策略试解n= 3 ,w=[20,15,15], 
              p=[40,25,25], c=30 时的最优解。
              我们不必因所考察的几个贪婪算法都不能保证得到最优解而沮丧， 0 / 1背包问题是一个N 
              P-复杂问题。对于这类问题，也许根本就不可能找到具有多项式时间的算法。虽然按pi /wi 
              非递（增）减的次序装入物品不能保证得到最优解，但它是一个直觉上近似的解。我们希望它是一个好的启发式算法，且大多数时候能很好地接近最后算法。在6 
              0 0个随机产生的背包问题中，用这种启发式贪婪算法来解有2 3 9题为最优解。有5 8 3个例子与最优解相差1 0 %，所有6 0 
              0个答案与最优解之差全在2 5 %以内。该算法能在O (nl o gn)时间内获得如此好的性能。我们也许会问，是否存在一个x 
              (x<1 0 0 )，使得贪婪启发法的结果与最优值相差在x%以内。答案是否定的。为说明这一点，考虑例子n =2, w = [ 1 
              ,y], p= [ 1 0 , 9y], 和c= y。贪婪算法结果为x=[1,0], 这种方案的值为1 0。对于y≥1 0 / 
              9，最优解的值为9 y。因此，贪婪算法的值与最优解的差对最优解的比例为( ( 9y - 1 0)/9y* 1 0 0 ) 
              %，对于大的y，这个值趋近于1 0 0 %。但是可以建立贪婪启发式方法来提供解，使解的结果与最优解的值之差在最优值的x% 
              (x<100) 之内。首先将最多k 件物品放入背包，如果这k 件物品重量大于c，则放弃它。否则，剩余的容量用来考虑将剩余物品按pi 
              /wi 递减的顺序装入。通过考虑由启发法产生的解法中最多为k 件物品的所有可能的子集来得到最优解。
              例13-9 考虑n =4, w=[2,4,6,7], p=[6,10,12,13], c = 11。当k= 
              0时，背包按物品价值密度非递减顺序装入，首先将物品1放入背包，然后是物品2，背包剩下的容量为5个单元，剩下的物品没有一个合适的，因此解为x 
              = [ 1 , 1 , 0 , 0 ]。此解获得的价值为1 6。
              现在考虑k = 1时的贪婪启发法。最初的子集为{ 1 } , { 2 } , { 3 } , { 4 }。子集{ 1 } , { 2 
              }产生与k= 0时相同的结果，考虑子集{ 3 }，置x3 
              为1。此时还剩5个单位的容量，按价值密度非递增顺序来考虑如何利用这5个单位的容量。首先考虑物品1，它适合，因此取x1 
              为1，这时仅剩下3个单位容量了，且剩余物品没有能够加入背包中的物品。通过子集{ 3 }开始求解得结果为x = [ 1 , 0 , 1 
              , 0 ]，获得的价值为1 8。若从子集{ 4 }开始，产生的解为x = [ 1 , 0 , 0 , 1 ]，获得的价值为1 
              9。考虑子集大小为0和1时获得的最优解为[ 1 , 0 , 0 , 1 ]。这个解是通过k= 1的贪婪启发式算法得到的。
              若k= 2，除了考虑k< 2的子集，还必需考虑子集{ 1 , 2 } , { 1 , 3 } , { 1 , 4 } , { 2 , 
              3 } , { 2 , 4 }和{ 3 , 4 
              }。首先从最后一个子集开始，它是不可行的，故将其抛弃，剩下的子集经求解分别得到如下结果：[ 1 , 1 , 0 , 0 ] , [ 
              1 , 0 , 1 , 0 ] , [ 1 , 0 , 0 , 1 ] , [ 0 , 1 , 1 , 0 ]和[ 0 , 1 , 
              0 , 1 ]，这些结果中最后一个价值为2 3，它的值比k= 0和k= 1时获得的解要高，这个答案即为启发式方法产生的结果。
              这种修改后的贪婪启发方法称为k阶优化方法（k - o p t i m a l）。也就是，若从答案中取出k 件物品，并放入另外k 
              件，获得的结果不会比原来的好，而且用这种方式获得的值在最优值的( 1 0 0 / (k + 1 ) ) %以内。当k= 
              1时，保证最终结果在最佳值的5 0 %以内；当k= 2时，则在3 3 . 3 3 %以内等等，这种启发式方法的执行时间随k 
              的增大而增加，需要测试的子集数目为O (nk )，每一个子集所需时间为O (n)，因此当k >0时总的时间开销为O (nk+1 
              )。实际观察到的性能要好得多。


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:39:53       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 6 楼 



               

              1.3.3 拓扑排序
              一个复杂的工程通常可以分解成一组小任务的集合，完成这些小任务意味着整个工程的完成。例如，汽车装配工程可分解为以下任务：将底盘放上装配线，装轴，将座位装在底盘上，上漆，装刹车，装门等等。任务之间具有先后关系，例如在装轴之前必须先将底板放上装配线。任务的先后顺序可用有向图表示——称为顶点活动（ 
              Activity On Vertex, AOV）网络。有向图的顶点代表任务，有向边(i, j) 表示先后关系：任务j 开始前任务i 
              必须完成。图1  - 4显示了六个任务的工程，边（ 1 , 4）表示任务1在任务4开始前完成，同样边（ 4 , 
              6）表示任务4在任务6开始前完成，边（1 , 4）与（4 , 
              6）合起来可知任务1在任务6开始前完成，即前后关系是传递的。由此可知，边（1 , 4）是多余的，因为边（1 , 3）和（3 , 
              4）已暗示了这种关系。
              在很多条件下，任务的执行是连续进行的，例如汽车装配问题或平时购买的标有“需要装配”的消费品（自行车、小孩的秋千装置，割草机等等）。我们可根据所建议的顺序来装配。在由任务建立的有向图中，边（ 
              i, j）表示在装配序列中任务i 在任务j 的前面，具有这种性质的序列称为拓扑序列（topological 
              orders或topological sequences)。根据任务的有向图建立拓扑序列的过程称为拓扑排序（topological 
              sorting）。图1 - 4的任务有向图有多种拓扑序列，其中的三种为1 2 3 4 5 6，1 3 2 4 5 6和2 1 5 3 
              4 6，序列1 4 2 3 5 6就不是拓扑序列，因为在这个序列中任务4在3的前面，而任务有向图中的边为（ 3 , 
              4），这种序列与边（ 3 , 
              4）及其他边所指示的序列相矛盾。可用贪婪算法来建立拓扑序列。算法按从左到右的步骤构造拓扑序列，每一步在排好的序列中加入一个顶点。利用如下贪婪准则来选择顶点：从剩下的顶点中，选择顶点w，使得w 
              不存在这样的入边（ v,w），其中顶点v 不在已排好的序列结构中出现。注意到如果加入的顶点w违背了这个准则（即有向图中存在边（ 
              v,w）且v 不在已构造的序列中），则无法完成拓扑排序，因为顶点v 必须跟随在顶点w 之后。贪婪算法的伪代码如图1 3 - 
              5所示。while 循环的每次迭代代表贪婪算法的一个步骤。
              现在用贪婪算法来求解图1 - 
              4的有向图。首先从一个空序列V开始，第一步选择V的第一个顶点。此时，在有向图中有两个候选顶点1和2，若选择顶点2，则序列V = 
              2，第一步完成。第二步选择V的第二个顶点，根据贪婪准则可知候选顶点为1和5，若选择5，则V = 2 
              5。下一步，顶点1是唯一的候选，因此V = 2 5 1。第四步，顶点3是唯一的候选，因此把顶点3加入V
              得到V = 2 5 1 3。在最后两步分别加入顶点4和6 ，得V = 2 5 1 3 4 6。
              1. 贪婪算法的正确性
              为保证贪婪算法算的正确性，需要证明： 1) 当算法失败时，有向图没有拓扑序列； 2) 若
              算法没有失败，V即是拓扑序列。2) 即是用贪婪准则来选取下一个顶点的直接结果， 1) 的证明见定理1 3 - 
              2，它证明了若算法失败，则有向图中有环路。若有向图中包含环qj qj + 1.qk qj , 则它没有拓扑序列，因为该序列暗示了qj 
              一定要在qj 开始前完成。
              定理1-2 如果图1 3 - 5算法失败，则有向图含有环路。
              证明注意到当失败时| V |<n, 且没有候选顶点能加入V中，因此至少有一个顶点q1 不在V中，有向图中必包含边（ q2 , 
              q1）且q2 不在V中，否则， q1 是可加入V的候选顶点。同样，必有边（q3 , q2）使得q3 不在V中，若q3 = q1 
              则q1 q2 q3 是有向图中的一个环路；若q3 ≠q1，则必存在q4 使（q4 , q3）是有向图的边且q4 不在V中，否则，q3 
              便是V的一个候选顶点。若q4 为q1 , q2 , q3 
              中的任何一个，则又可知有向图含有环，因为有向图具有有限个顶点数n，继续利用上述方法，最后总能找到一个环路。
              2. 数据结构的选择
              为将图1 - 5用C + 
              +代码来实现，必须考虑序列V的描述方法，以及如何找出可加入V的候选顶点。一种高效的实现方法是将序列V用一维数组v 
              来描述的，用一个栈来保存可加入V的候选顶点。另有一个一维数组I n D e g r e e，I n D e g r e e[ j 
              ]表示与顶点j相连的节点i 的数目，其中顶点i不是V中的成员，它们之间的有向图的边表示为（ i, j）。当I n D e g r e 
              e[ j ]变为0时表示j 成为一个候选节点。序列V初始时为空。I n D e g r e e[ j ]为顶点j 
              的入度。每次向V中加入一个顶点时，所有与新加入顶点邻接的顶点j，其I n D e g r e e[ j ]减1。对于有向图1 - 
              4，开始时I n D e g r e e [ 1 : 6 ] = [ 0 , 0 , 1 , 3 , 1 , 3 
              ]。由于顶点1和2的I n D e g r e 
              e值为0，因此它们是可加入V的候选顶点，由此，顶点1和2首先入栈。每一步，从栈中取出一个顶点将其加入V，同时减去与其邻接的顶点的I 
              n D e g r e e值。若在第一步时从栈中取出顶点2并将其加入V，便得到了v [ 0 ] = 2，和I n D e g r e 
              e [ 1 : 6 ] = [ 0 , 0 , 1 , 2 , 0 , 3 ]。由于I n D e g r e e [ 5 
              ]刚刚变为0，因此将顶点5入栈。
              程序1 3 - 2给出了相应的C + +代码，这个代码被定义为N e t w o r 
              k的一个成员函数。而且，它对于有无加权的有向图均适用。但若用于无向图（不论其有无加权）将会得到错误的结果，因为拓扑排序是针对有向图来定义的。为解决这个问题，利用同样的模板来定义成员函数AdjacencyGraph, 
              AdjacencyWGraph，L i n k e d G r a p h和L i n k e d W G r a p 
              h。这些函数可重载N e t w o r k中的函数并可输出错误信息。如果找到拓扑序列，则Topological 函数返回t r u 
              e；若输入的有向图无拓扑序列则返回f a l s e。当找到拓扑序列时，将其返回到v [ 0 :n- 1 ]中。
              3. Network:Topological 的复杂性
              第一和第三个f o r循环的时间开销为(n )。若使用（耗费）邻接矩阵,则第二个for 循环所用的时间为(n2 
              )；若使用邻接链表,则所用时间为(n+e)。在两个嵌套的while 循环中，外层循环需执行n次，每次将顶点w 加入到v 
              中，并初始化内层while 循环。使用邻接矩阵时，内层w h i l e循环对于每个顶点w 
              需花费(n)的时间；若利用邻接链表，则这个循环需花费dwout 的时间，因此，内层while 循环的时间开销为(n2 
              )或(n+e)。所以，若利用邻接矩阵，程序1 3 - 2的时间复杂性为(n2 )，若利用邻接链表则为(n+e)。
              程序13-2 拓扑排序
              bool Network::Topological(int v[])
              {// 计算有向图中顶点的拓扑次序
              // 如果找到了一个拓扑次序，则返回t r u e，此时，在v [ 0 : n - 1 ]中记录拓扑次序
              // 如果不存在拓扑次序，则返回f a l s e
              int n = Ve r t i c e s ( ) ;
              // 计算入度
              int *InDegree = new int [n+1];
              InitializePos(); // 图遍历器数组
              for (int i = 1; i <= n; i++) // 初始化
              InDegree[i] = 0;
              for (i = 1; i <= n; i++) {// 从i 出发的边
              int u = Begin(i);
              while (u) {
              I n D e g r e e [ u ] + + ;
              u = NextVe r t e x ( i ) ; }
              }
              // 把入度为０的顶点压入堆栈
              LinkedStack<int> S;
              for (i = 1; i <= n; i++)
              if (!InDegree[i]) S.Add(i);
              // 产生拓扑次序
              i = 0; // 数组v 的游标
              while (!S.IsEmpty()) {// 从堆栈中选择
              int w; // 下一个顶点
              S . D e l e t e ( w ) ;
              v[i++] = w;
              int u = Begin(w);
              while (u) {// 修改入度
              I n D e g r e e [ u ] - - ;
              if (!InDegree[u]) S.Add(u);
              u = NextVe r t e x ( w ) ; }
              }
              D e a c t i v a t e P o s ( ) ;
              delete [] InDegree;
              return (i == n);
              }


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:40:10       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 7 楼 



               

              1.3.4 二分覆盖
              二分图是一个无向图，它的n 
              个顶点可二分为集合A和集合B，且同一集合中的任意两个顶点在图中无边相连（即任何一条边都是一个顶点在集合A中，另一个在集合B中）。当且仅当B中的每个顶点至少与A中一个顶点相连时，A的一个子集A' 
              覆盖集合B（或简单地说，A' 是一个覆盖）。覆盖A' 的大小即为A' 中的顶点数目。当且仅当A' 是覆盖B的子集中最小的时，A' 
              为最小覆盖。
              例1-10 考察如图1 - 6所示的具有1 7个顶点的二分图，A={1, 2, 3, 16, 17}和B={4, 5, 6, 7, 
              8, 9,10, 11, 12, 13, 14, 15}，子集A' = { 1 , 1 6 , 1 7 
              }是B的最小覆盖。在二分图中寻找最小覆盖的问题为二分覆盖（ b i p a r t i t e - c o v e r）问题。在例1 
              2 - 3中说明了最小覆盖是很有用的，因为它能解决“在会议中使用最少的翻译人员进行翻译”这一类的问题。
              二分覆盖问题类似于集合覆盖（ s e t - c o v e r）问题。在集合覆盖问题中给出了k 个集合S= {S1 , S2 
              ,., Sk }，每个集合Si 中的元素均是全集U中的成员。当且仅当&Egrave;i S'Si =U时，S的子集S' 覆盖U，S 
              '中的集合数目即为覆盖的大小。当且仅当没有能覆盖U的更小的集合时，称S' 
              为最小覆盖。可以将集合覆盖问题转化为二分覆盖问题（反之亦然），即用A的顶点来表示S1 , ., Sk 
              ，B中的顶点代表U中的元素。当且仅当S的相应集合中包含U中的对应元素时，在A与B的顶点之间存在一条边。
              例1 - 11 令S= {S1，. . .，S5 }, U= { 4，5，. . .，15}, S1 = { 4，6，7，8，9，1 
              3 }，S2 = { 4，5，6，8 }，S3 = { 8，1 0，1 2，1 4，1 5 }，S4 = { 5，6，8，1 2，1 
              4，1 5 }，S5 = { 4，9，1 0，11 }。S ' = {S1，S4，S5 }是一个大小为3的覆盖，没有更小的覆盖， 
              S' 即为最小覆盖。这个集合覆盖问题可映射为图1-6的二分图，即用顶点1，2，3，1 6和1 7分别表示集合S1，S2，S3，S4 
              和S5，顶点j 表示集合中的元素j，4≤j≤1 5。
              集合覆盖问题为N P-复杂问题。由于集合覆盖与二分覆盖是同一类问题，二分覆盖问题也是N 
              P-复杂问题。因此可能无法找到一个快速的算法来解决它，但是可以利用贪婪算法寻找一种快速启发式方法。一种可能是分步建立覆盖A' 
              ，每一步选择A中的一个顶点加入覆盖。顶点的选择利用贪婪准则：从A中选取能覆盖B中还未被覆盖的元素数目最多的顶点。
              例1-12 考察图1 - 6所示的二分图，初始化A' = 且B中没有顶点被覆盖，顶点1和1 
              6均能覆盖B中的六个顶点，顶点3覆盖五个，顶点2和1 7分别覆盖四个。因此，在第一步往A' 中加入顶点1或1 6，若加入顶点1 
              6，则它覆盖的顶点为{ 5 , 6 , 8 , 1 2 , 1 4 , 1 5 }，未覆盖的顶点为{ 4 , 7 , 9 , 1 0 
              , 11 , 1 3 }。顶点1能覆盖其中四个顶点（ { 4 , 7 , 9 , 1 3 }），顶点2 覆盖一个( { 4 } 
              )，顶点3覆盖一个（{ 1 0 }），顶点1 6覆盖零个，顶点1 7覆盖四个{ 4 , 9 , 1 0 , 11 
              }。下一步可选择1或1 7加入A' 。若选择顶点1，则顶点{ 1 0 , 11} 仍然未被覆盖，此时顶点1，2，1 
              6不覆盖其中任意一个，顶点3覆盖一个，顶点1 7覆盖两个，因此选择顶点1 7，至此所有顶点已被覆盖，得A' = { 1 6 , 1 
              , 1 7 }。
              图1 - 7给出了贪婪覆盖启发式方法的伪代码，可以证明： 1) 当且仅当初始的二分图没有覆盖时，算法找不到覆盖；2) 
              启发式方法可能找不到二分图的最小覆盖。
              1. 数据结构的选取及复杂性分析
              为实现图13 - 7的算法，需要选择A' 的描述方法及考虑如何记录A中节点所能覆盖的B中未覆盖节点的数目。由于对集合A' 
              仅使用加法运算，则可用一维整型数组C来描述A '，用m 来记录A' 中元素个数。将A' 中的成员记录在C[ 0 :m-1] 
              中。对于A中顶点i，令N e wi 为i 所能覆盖的B中未覆盖的顶点数目。逐步选择N e wi 
              值最大的顶点。由于一些原来未被覆盖的顶点现在被覆盖了，因此还要修改各N e wi 
              值。在这种更新中，检查B中最近一次被V覆盖的顶点，令j 为这样的一个顶点，则A中所有覆盖j 的顶点的N e wi 值均减1。
              例1-13 考察图1 - 6，初始时(N e w1 , N e w2 , N e w3 , N e w16 , N e w17 ) 
              = ( 6 , 4 , 5 , 6 , 4 )。假设在例1 - 1 2中，第一步选择顶点1 6，为更新N e wi 
              的值检查B中所有最近被覆盖的顶点，这些顶点为5 , 6 , 8 , 1 2 , 1 4和1 5。当检查顶点5时，将顶点2和1 6的N 
              e wi 值分别减1，因为顶点5不再是被顶点2和1 6覆盖的未覆盖节点；当检查顶点6时，顶点1 , 2 ,和1 
              6的相应值分别减1；同样，检查顶点8时，1，2，3和1 6的值分别减1；当检查完所有最近被覆盖的顶点，得到的N e wi 
              值为（4，1，0，4）。下一步选择顶点1，最新被覆盖的顶点为4，7，9和1 3；检查顶点4时，N e w1 , N e w2, 和N 
              e w1 7 的值减1；检查顶点7时，N e w1 的值减1，因为顶点1是覆盖7的唯一顶点。
              为了实现顶点选取的过程，需要知道N e wi 的值及已被覆盖的顶点。可利用一个二维数组来达到这个目的，N e 
              w是一个整型数组，New[i] 即等于N e wi，且c o v为一个布尔数组。若顶点i未被覆盖则c o v [ i ]等于f a 
              l s e，否则c o v [ i ]为t r u e。现将图1 - 7的伪代码进行细化得到图1 - 8。
              m=0; //当前覆盖的大小
              对于A中的所有i，New[i]=Degree[i]
              对于B中的所有i，C o v [ i ] = f a l s e
              while (对于A中的某些i,New[i]>0) {
              设v是具有最大的N e w [ i ]的顶点；
              C [ m + + ] = v ;
              for ( 所有邻接于v的顶点j) {
              if (!Cov[j]) {
              Cov[j]= true;
              对于所有邻接于j的顶点，使其N e w [ k ]减1
              } } }
              if (有些顶点未被覆盖) 失败
              else 找到一个覆盖
              图1-8  图1-7的细化
              更新N e w的时间为O (e)，其中e 为二分图中边的数目。若使用邻接矩阵，则需花(n2 ) 
              的时间来寻找图中的边，若用邻接链表，则需(n+e) 的时间。实际更新时间根据描述方法的不同为O (n2 ) 或O 
              (n+e)。逐步选择顶点所需时间为(S i z e O f A)，其中S i z e O f A=| A 
              |。因为A的所有顶点都有可能被选择，因此所需步骤数为O ( S i z e O f A )，覆盖算法总的复杂性为O ( S i z 
              e O f A 2+n2) = O ( n2)或O (S i z e Of A2+n + e)。
              2. 降低复杂性
              通过使用有序数组N e wi、最大堆或最大选择树（max selection tree）可将每步选取顶点v的复杂性降为( 1 
              )。但利用有序数组，在每步的最后需对N e wi 值进行重新排序。若使用箱子排序，则这种排序所需时间为(S i z e O f B 
              ) ( S i z e O fB =|B| ) （见3 . 8 . 1节箱子排序）。由于一般S i z e O f B比S i z 
              e O f A大得多，因此有序数组并不总能提高性能。
              如果利用最大堆，则每一步都需要重建堆来记录N e w值的变化，可以在每次N e w值减1时进行重建。这种减法操作可引起被减的N e 
              w值最多在堆中向下移一层，因此这种重建对于每次N e w值减1需( 1 )的时间，总共的减操作数目为O 
              (e)。因此在算法的所有步骤中，维持最大堆仅需O (e)的时间，因而利用最大堆时覆盖算法的总复杂性为O (n2 )或O (n+e)。
              若利用最大选择树，每次更新N e w值时需要重建选择树，所需时间为(log S i z e O f 
              A)。重建的最好时机是在每步结束时，而不是在每次N e w值减1时，需要重建的次数为O (e)，因此总的重建时间为O (e log 
              S i z e OfA)，这个时间比最大堆的重建时间长一些。然而，通过维持具有相同N e 
              w值的顶点箱子，也可获得和利用最大堆时相同的时间限制。由于N e w的取值范围为0到S i z e O f B，需要S i z e 
              O f B+ 1个箱子，箱子i 是一个双向链表，链接所有N e w值为i 的顶点。在某一步结束时，假如N e w [ 6 ]从1 
              2变到4，则需要将它从第1 2个箱子移到第4个箱子。利用模拟指针及一个节点数组n o d e（其中n o d e [ i 
              ]代表顶点i，n o d e [ i ] . l e f t和n o d e [ i ] . r i g h 
              t为双向链表指针），可将顶点6从第1 2个箱子移到第4个箱子，从第1 2个箱子中删除n o d e [ 0 
              ]并将其插入第4个箱子。利用这种箱子模式，可得覆盖启发式算法的复杂性为O (n2 
              )或O(n+e)。（取决于利用邻接矩阵还是线性表来描述图）。
              3. 双向链接箱子的实现
              为了实现上述双向链接箱子，图1 - 9定义了类U n d i r e c t e d的私有成员。N o d e Ty p 
              e是一个具有私有整型成员l e f t和r i g h t的类，它的数据类型是双向链表节点，程序1 3 - 3给出了U n d i 
              r e c t e d的私有成员的代码。
              void CreateBins (int b, int n)
              创建b个空箱子和n个节点
              void DestroyBins() { delete [] node;
              delete [] bin;}
              void InsertBins(int b, int v)
              在箱子b中添加顶点v
              void MoveBins(int bMax, int ToBin, int v)
              从当前箱子中移动顶点v到箱子To B i n
              int *bin;
              b i n [ i ]指向代表该箱子的双向链表的首节点
              N o d e Type *node;
              n o d e [ i ]代表存储顶点i的节点
              图1-9 实现双向链接箱子所需的U n d i r e c t e d私有成员


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:40:45       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 8 楼 



               

              程序13-3 箱子函数的定义
              void Undirected::CreateBins(int b, int n)
              {// 创建b个空箱子和n个节点
              node = new NodeType [n+1];
              bin = new int [b+1];
              // 将箱子置空
              for (int i = 1; i <= b; i++)
              bin[i] = 0;
              }
              void Undirected::InsertBins(int b, int v)
              {// 若b不为０，则将v 插入箱子b
              if (!b) return; // b为0，不插入
              node[v].left = b; // 添加在左端
              if (bin[b]) node[bin[b]].left = v;
              node[v].right = bin[b];
              bin[b] = v;
              }
              void Undirected::MoveBins(int bMax, int ToBin, int v)
              {// 将顶点v 从其当前所在箱子移动到To B i n .
              // v的左、右节点
              int l = node[v].left;
              int r = node[v].right;
              // 从当前箱子中删除
              if (r) node[r].left = node[v].left;
              if (l > bMax || bin[l] != v) // 不是最左节点
              node[l].right = r;
              else bin[l] = r; // 箱子l的最左边
              // 添加到箱子To B i n
              I n s e r t B i n s ( ToBin, v);
              }
              函数C r e a t e B i n s动态分配两个数组： n o d e和b i n，n o d e [i ]表示顶点i, 
              bin[i ]指向其N e w值为i的双向链表的顶点, f o r循环将所有双向链表置为空。如果b≠0，函数InsertBins 
              将顶点v 插入箱子b 中。因为b 是顶点v 的New 值，b = 0意味着顶点v 
              不能覆盖B中当前还未被覆盖的任何顶点，所以，在建立覆盖时这个箱子没有用处，故可以将其舍去。当b≠0时，顶点n 加入New 值为b 
              的双向链表箱子的最前面，这种加入方式需要将node[v] 加入bin[b] 
              中第一个节点的左边。由于表的最左节点应指向它所属的箱子，因此将它的node[v].left 
              置为b。若箱子不空，则当前第一个节点的left 指针被置为指向新节点。node[v] 的右指针被置为b i n [ b 
              ]，其值可能为0或指向上一个首节点的指针。最后， b i n [ b ]被更新为指向表中新的第一个节点。MoveBins 将顶点v 
              从它在双向链表中的当前位置移到New 值为ToBin 的位置上。其中存在bMa x，使得对所有的箱子b i n[ j 
              ]都有：如j>bMa x，则b i n [ j ]为空。代码首先确定n o d e [ v 
              ]在当前双向链表中的左右节点，接着从双链表中取出n o d e [ v ]，并利用I n s e r t B i n 
              s函数将其重新插入到b i n [ To B i n ]中。
              4. Undirected::BipartiteCover的实现
              函数的输入参数L用于分配图中的顶点（分配到集合A或B）。L [i ] = 1表示顶点i在集合A中，L[ i ] = 
              2则表示顶点在B中。函数有两个输出参数： C和m，m为所建立的覆盖的大小， C [ 0 , m - 1 
              ]是A中形成覆盖的顶点。若二分图没有覆盖，函数返回f a l s e；否则返回t r u e。完整的代码见程序1 3 - 4。
              程序13-4 构造贪婪覆盖
              bool Undirected::BipartiteCover(int L[], int C[], int& m)
              {// 寻找一个二分图覆盖
              // L 是输入顶点的标号, L[i] = 1 当且仅当i 在Ａ中
              // C 是一个记录覆盖的输出数组
              // 如果图中不存在覆盖，则返回f a l s e
              // 如果图中有一个覆盖，则返回t r u e ;
              // 在m中返回覆盖的大小; 在C [ 0 : m - 1 ]中返回覆盖
              int n = Ve r t i c e s ( ) ;
              // 插件结构
              int SizeOfA = 0;
              for (int i = 1; i <= n; i++) // 确定集合A的大小
              if (L[i] == 1) SizeOfA++;
              int SizeOfB = n - SizeOfA;
              CreateBins(SizeOfB, n);
              int *New = new int [n+1]; / /顶点i覆盖了Ｂ中N e w [ i ]个未被覆盖的顶点
              bool *Change = new bool [n+1]; // Change[i]为t r u e当且仅当New[i] 已改变
              bool *Cov = new bool [n+1]; // Cov[i] 为true 当且仅当顶点i 被覆盖
              I n i t i a l i z e P o s ( ) ;
              LinkedStack<int> S;
              // 初始化
              for (i = 1; i <= n; i++) {
              Cov[i] = Change[i] = false;
              if (L[i] == 1) {// i 在A中
              New[i] = Degree(i); // i 覆盖了这么多
              InsertBins(New[i], i);}}
              // 构造覆盖
              int covered = 0, // 被覆盖的顶点
              MaxBin = SizeOfB; // 可能非空的最大箱子
              m = 0; // C的游标
              while (MaxBin > 0) { // 搜索所有箱子
              // 选择一个顶点
              if (bin[MaxBin]) { // 箱子不空
              int v = bin[MaxBin]; // 第一个顶点
              C[m++] = v; // 把v 加入覆盖
              // 标记新覆盖的顶点
              int j = Begin(v), k;
              while (j) {
              if (!Cov[j]) {// j尚未被覆盖
              Cov[j] = true;
              c o v e r e d + + ;
              // 修改N e w
              k = Begin(j);
              while (k) {
              New[k]--; // j 不计入在内
              if (!Change[k]) {
              S.Add(k); // 仅入栈一次
              Change[k] = true;}
              k = NextVe r t e x ( j ) ; }
              }
              j = NextVe r t e x ( v ) ; }
              // 更新箱子
              while (!S.IsEmpty()) {
              S . D e l e t e ( k ) ;
              Change[k] = false;
              MoveBins(SizeOfB, New[k], k);}
              }
              else MaxBin--;
              }
              D e a c t i v a t e P o s ( ) ;
              D e s t r o y B i n s ( ) ;
              delete [] New;
              delete [] Change;
              delete [] Cov;
              return (covered == SizeOfB);
              }
              程序1 3 - 4首先计算出集合A和B的大小、初始化必要的双向链表结构、创建三个数组、初始化图遍历器、并创建一个栈。然后将数组C o 
              v和C h a n g e初始化为f a l s e，并将A中的顶点根据它们覆盖B中顶点的数目插入到相应的双向链表中。
              为了构造覆盖，首先按SizeOfB 递减至1的顺序检查双向链表。当发现一个非空的表时，就将其第一个顶点v 
              加入到覆盖中，这种策略即为选择具有最大New 值的顶点。将所选择的顶点加入覆盖数组C并检查B中所有与它邻接的顶点。若顶点j 与v 
              邻接且还未被覆盖，则将C o v [ j ]置为t r u e，表示顶点j 现在已被覆盖，同时将已被覆盖的B中的顶点数目加1。由于j 
              是最近被覆盖的，所有A中与j 邻接的顶点的New 值减1。下一个while 循环降低这些New 值并将New 
              值被降低的顶点保存在一个栈中。当所有与顶点v邻接的顶点的Cov 值更新完毕后，N e 
              w值反映了A中每个顶点所能覆盖的新的顶点数，然而A中的顶点由于New 值被更新，处于错误的双向链表中，下一个while 
              循环则将这些顶点移到正确的表中。


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:40:53       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 9 楼 



               

              1.3.5 单源最短路径
              在这个问题中，给出有向图G，它的每条边都有一个非负的长度（耗费） a [i ][ j 
              ]，路径的长度即为此路径所经过的边的长度之和。对于给定的源顶点s，需找出从它到图中其他任意顶点（称为目的）的最短路径。图13-10a 
              给出了一个具有五个顶点的有向图，各边上的数即为长度。假设源顶点s 为1，从顶点1出发的最短路径按路径长度顺序列在图13-10b 
              中，每条路径前面的数字为路径的长度。
              利用E. 
              Dijkstra发明的贪婪算法可以解决最短路径问题，它通过分步方法求出最短路径。每一步产生一个到达新的目的顶点的最短路径。下一步所能达到的目的顶点通过如下贪婪准则选取：在还未产生最短路径的顶点中，选择路径长度最短的目的顶点。也就是说， 
              D i j k s t r a的方法按路径长度顺序产生最短路径。
              首先最初产生从s 
              到它自身的路径，这条路径没有边，其长度为0。在贪婪算法的每一步中，产生下一个最短路径。一种方法是在目前已产生的最短路径中加入一条可行的最短的边，结果产生的新路径是原先产生的最短路径加上一条边。这种策略并不总是起作用。另一种方法是在目前产生的每一条最短路径中，考虑加入一条最短的边，再从所有这些边中先选择最短的，这种策略即是D 
              i j k s t r a算法。
              可以验证按长度顺序产生最短路径时，下一条最短路径总是由一条已产生的最短路径加上一条边形成。实际上，下一条最短路径总是由已产生的最短路径再扩充一条最短的边得到的，且这条路径所到达的顶点其最短路径还未产生。例如在图1 
              3 - 1 0中，b 
              中第二条路径是第一条路径扩充一条边形成的；第三条路径则是第二条路径扩充一条边；第四条路径是第一条路径扩充一条边；第五条路径是第三条路径扩充一条边。
              通过上述观察可用一种简便的方法来存储最短路径。可以利用数组p，p [ i ]给出从s 到达i的路径中顶点i 
              前面的那个顶点。在本例中p [ 1 : 5 ] = [ 0 , 1 , 1 , 3 , 4 ]。从s 到顶点i 
              的路径可反向创建。从i 出发按p[i],p[p[i]],p[p[p[i]]], .的顺序，直到到达顶点s 或0。在本例中，如果从i 
              = 5开始，则顶点序列为p[i]=4, p[4]=3, p[3]=1=s，因此路径为1 , 3 , 4 , 5。
              为能方便地按长度递增的顺序产生最短路径，定义d [ i 
              ]为在已产生的最短路径中加入一条最短边的长度，从而使得扩充的路径到达顶点i。最初，仅有从s 到s 
              的一条长度为0的路径，这时对于每个顶点i，d [ i ]等于a [ s ] [ i ]（a 
              是有向图的长度邻接矩阵）。为产生下一条路径，需要选择还未产生最短路径的下一个节点，在这些节点中d值最小的即为下一条路径的终点。当获得一条新的最短路径后，由于新的最短路径可能会产生更小的d值，因此有些顶点的d值可能会发生变化。
              综上所述，可以得到图1 3 - 11所示的伪代码， 1) 将与s 邻接的所有顶点的p 
              初始化为s，这个初始化用于记录当前可用的最好信息。也就是说，从s 到i 
              的最短路径，即是由s到它自身那条路径再扩充一条边得到。当找到更短的路径时， p [ i 
              ]值将被更新。若产生了下一条最短路径，需要根据路径的扩充边来更新d 的值。
              1) 初始化d[i ] =a[s] [i ]（1≤i≤n），
              对于邻接于s的所有顶点i，置p[i ] =s, 对于其余的顶点置p[i ] = 0；
              对于p[i]≠0的所有顶点建立L表。
              2) 若L为空，终止，否则转至3 )。
              3) 从L中删除d值最小的顶点。
              4) 对于与i 邻接的所有还未到达的顶点j，更新d[ j ]值为m i n{d[ j ], d[i ] +a[i ][ j ] 
              }；若d[ j ]发生了变化且j 还未
              在L中，则置p[ j ] = 1，并将j 加入L，转至2。
              图1 - 11 最短路径算法的描述
              1. 数据结构的选择
              我们需要为未到达的顶点列表L选择一个数据结构。从L中可以选出d 值最小的顶点。如果L用最小堆（见9 . 
              3节）来维护，则这种选取可在对数时间内完成。由于3) 的执行次数为O ( n )，所以所需时间为O ( n l o g n 
              )。由于扩充一条边产生新的最短路径时，可能使未到达的顶点产生更小的d 值，所以在4) 中可能需要改变一些d 
              值。虽然算法中的减操作并不是标准的最小堆操作，但它能在对数时间内完成。由于执行减操作的总次数为： O(有向图中的边数)= O ( 
              n2 )，因此执行减操作的总时间为O ( n2 l o g n )。
              若L用无序的链表来维护，则3) 与4) 花费的时间为O ( n2 )，3) 的每次执行需O(|L | ) =O( n 
              )的时间，每次减操作需( 1 )的时间（需要减去d[j] 的值，但链表不用改变）。利用无序链表将图1 - 11的伪代码细化为程序1 
              3 - 5，其中使用了C h a i n (见程序3 - 8 )和C h a i n I t e r a t o r类（见程序3 - 
              1 8）。
              程序13-5 最短路径程序
              template<class T>
              void AdjacencyWDigraph<T>::ShortestPaths(int s, T d[], int p[])
              {// 寻找从顶点s出发的最短路径, 在d中返回最短距离
              // 在p中返回前继顶点
              if (s < 1 || s > n) throw OutOfBounds();
              Chain<int> L; // 路径可到达顶点的列表
              ChainIterator<int> I;
              // 初始化d, p, L
              for (int i = 1; i <= n; i++){
              d[i] = a[s][i];
              if (d[i] == NoEdge) p[i] = 0;
              else {p[i] = s;
              L . I n s e r t ( 0 , i ) ; }
              }
              // 更新d, p
              while (!L.IsEmpty()) {// 寻找具有最小d的顶点v
              int *v = I.Initialize(L);
              int *w = I.Next();
              while (w) {
              if (d[*w] < d[*v]) v = w;
              w = I.Next();}
              // 从L中删除通向顶点v的下一最短路径并更新d
              int i = *v;
              L . D e l e t e ( * v ) ;
              for (int j = 1; j <= n; j++) {
              if (a[i][j] != NoEdge && (!p[j] ||
              d[j] > d[i] + a[i][j])) {
              // 减小d [ j ]
              d[j] = d[i] + a[i][j];
              // 将j加入L
              if (!p[j]) L.Insert(0,j);
              p[j] = i;}
              }
              }
              }
              若N o E d g e足够大，使得没有最短路径的长度大于或等于N o E d g e，则最后一个for 循环的i 
              f条件可简化为：if (d[j] > d[i] + a[i][j]))  NoEdge 的值应在能使d[j]+a[i][j] 
              不会产生溢出的范围内。
              2. 复杂性分析
              程序1 3 - 5的复杂性是O ( n2 
              )，任何最短路径算法必须至少对每条边检查一次，因为任何一条边都有可能在最短路径中。因此这种算法的最小可能时间为O ( e 
              )。由于使用耗费邻接矩阵来描述图，仅决定哪条边在有向图中就需O ( n2 )的时间。因此，采用这种描述方法的算法需花费O ( n2 
              )的时间。不过程序1 3 - 5作了优化（常数因子级）。即使改变邻接表，也只会使最后一个f o r循环的总时间降为O ( e 
              )（因为只有与i 邻接的顶点的d 值改变）。从L中选择及删除最小距离的顶点所需总时间仍然是O( n2 )。


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:41:07       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 10 楼 



               

              1.3.6 最小耗费生成树
              在例1 - 2及1 - 3中已考察过这个问题。因为具有n 
              个顶点的无向网络G的每个生成树刚好具有n-1条边，所以问题是用某种方法选择n-1条边使它们形成G的最小生成树。至少可以采用三种不同的贪婪策略来选择这n-1条边。这三种求解最小生成树的贪婪算法策略是： 
              K r u s k a l算法，P r i m算法和S o l l i n算法。
              1. Kruskal算法
              (1) 算法思想
              K r u s k a l算法每次选择n- 
              1条边，所使用的贪婪准则是：从剩下的边中选择一条不会产生环路的具有最小耗费的边加入已选择的边的集合中。注意到所选取的边若产生环路则不可能形成一棵生成树。K 
              r u s k a l算法分e 步，其中e 是网络中边的数目。按耗费递增的顺序来考虑这e 
              条边，每次考虑一条边。当考虑某条边时，若将其加入到已选边的集合中会出现环路，则将其抛弃，否则，将它选入。
              考察图1-12a 中的网络。初始时没有任何边被选择。图13-12b 显示了各节点的当前状态。边（ 1 , 
              6）是最先选入的边，它被加入到欲构建的生成树中，得到图1 3 - 1 2 c。下一步选择边（ 3，4）并将其加入树中（如图1 3 - 
              1 2 d所示）。然后考虑边( 2，7 )，将它加入树中并不会产生环路，于是便得到图1 3 - 1 2 e。下一步考虑边（ 
              2，3）并将其加入树中（如图1 3 - 1 2 
              f所示）。在其余还未考虑的边中，（7，4）具有最小耗费，因此先考虑它，将它加入正在创建的树中会产生环路，所以将其丢弃。此后将边（ 
              5，4）加入树中，得到的树如图13-12g 所示。下一步考虑边（ 7，5），由于会产生环路，将其丢弃。最后考虑边（ 
              6，5）并将其加入树中，产生了一棵生成树，其耗费为9 9。图1 - 1 3给出了K r u s k a l算法的伪代码。
              / /在一个具有n 个顶点的网络中找到一棵最小生成树
              令T为所选边的集合，初始化T=
              令E 为网络中边的集合
              w h i l e(E≠ )&&(| T |≠n- 1 ) {
              令(u,v)为E中代价最小的边
              E=E- { (u,v) } / /从E中删除边
              i f( (u,v)加入T中不会产生环路)将（ u,v）加入T
              }
              i f(| T | = =n-1) T是最小耗费生成树
              e l s e 网络不是互连的，不能找到生成树
              图13-13 Kruskao算法的伪代码
              (2) 正确性证明
              利用前述装载问题所用的转化技术可以证明图1 3 - 1 3的贪婪算法总能建立一棵最小耗费生成树。需要证明以下两点： 1) 
              只要存在生成树，K r u s k a l算法总能产生一棵生成树； 2) 
              产生的生成树具有最小耗费。令G为任意加权无向图（即G是一个无向网络）。从1 2 . 11 . 
              3节可知当且仅当一个无向图连通时它有生成树。而且在Kruskal 
              算法中被拒绝（丢弃）的边是那些会产生环路的边。删除连通图环路中的一条边所形成的图仍是连通图，因此如果G在开始时是连通的，则T与E中的边总能形成一个连通图。也就是若G开始时是连通的，算法不会终止于E= 
              和| T |< n- 1。
              现在来证明所建立的生成树T具有最小耗费。由于G具有有限棵生成树，所以它至少具有一棵最小生成树。令U为这样的一棵最小生成树， 
              T与U都刚好有n- 1条边。如果T=U, 则T就具有最小耗费，那么不必再证明下去。因此假设T≠U，令k(k >0) 
              为在T中而不在U中的边的个数，当然k 也是在U中而不在T中的边的数目。
              通过把U变换为T来证明U与T具有相同的耗费，这种转化可在k 
              步内完成。每一步使在T而不在U中的边的数目刚好减1。而且U的耗费不会因为转化而改变。经过k 
              步的转化得到的U将与原来的U具有相同的耗费，且转化后U中的边就是T中的边。由此可知， T具有最小耗费。每步转化包括从T中移一条边e 
              到U中，并从U中移出一条边f。边e 与f 的选取按如下方式进行：
              1) 令e 是在T中而不在U中的具有最小耗费的边。由于k >0，这条边肯定存在。
              2) 当把e 加入U时，则会形成唯一的一条环路。令f 为这条环路上不在T中的任意一条边。
              由于T中不含环路，因此所形成的环路中至少有一条边不在T中。
              从e 与f 的选择方法中可以看出， V=U+ {e} -{ f } 是一棵生成树，且T中恰有k- 
              1条边不在V中出现。现在来证明V的耗费与U的相同。显然，V的耗费等于U的耗费加上边e 的耗费再减去边f 的耗费。若e 的耗费比f 
              的小，则生成树V的耗费比U的耗费小，这是不可能的。如果e 的耗费高于f，在K r u s k a l算法中f 会在e 
              之前被考虑。由于f 不在T中，Kruskal 算法在考虑f 能否加入T时已将f 丢弃，因此f 和T中耗费小于或等于f 
              的边共同形成环路。通过选择e，所有这些边均在U中，因此U肯定含有环路，但是实际上这不可能，因为U是一棵生成树。e 的代价高于f 
              的假设将会导致矛盾。剩下的唯一的可能是e 与f 具有相同的耗费，由此可知V与U的耗费相同。
              (3) 数据结构的选择及复杂性分析


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:41:42       

      本主题贴数 20   分页：9 1 2 :   跳转论坛至...╋数学建模  ├数模竞赛  ├新手入门  ├数学工具  ├资源与检索╋学术区  
        ├数学思想  ├编程交流  ├学术杂谈  ├English Fans╋休闲专区  ├灌水搞笑专区  ├神秘园╋本站站务  ├站务讨论  
        ├数模管理区  ├回收站


       *快速回复：贪婪算法
           发贴表情
                  
                  
                  
                  
                  
                  

               段落格式 普通格式标题 1标题 2标题 3标题 4标题 5标题 6标题 7已编排格式地址  
              字体宋体黑体楷体仿宋隶书幼圆新宋体细明体ArialArial BlackCourierVerdanaWide 
              LatinWingdings  字号1234567              


                      第 1 页,共 7 页， 49 个

       显示签名     内容限制：字节. 


      管理选项： 专题管理 | 修复 | 锁定 | 解锁 | 提升 | 跟贴管理 | 删除 | 移动 | 设置固顶 | 奖励 | 惩罚 | 发布公告 

            Copyright &copy;2002 - 2004 Shumo.Com
            执行时间：250.00000毫秒。查询数据库5次。
            当前模板样式：[默认模板] 
````

</details>

#### mydijkstra · Python · 08b68c5f

- 归属算法：Dijkstra最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Dijkstra最短路中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：优先调用 `dijkstra`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`dab979f21e46b538929045e5c4bbe6e37fe2dad7eac711b7a66a1a991eea162a`
- 语言：Python
- 符号：`dijkstra`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/mydijkstra.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_12.py
import numpy as np
inf=np.inf


def dijkstra(a,sb,db):
    n=len(a); visit=[0]*n
    dis=[inf]*n; dis[0]=0
    visit[sb]=1; u=sb  #u为最新的P标号顶点
    parent=[0]*n  #前驱顶点的初始化
    for i in range(n):
        id=[index for index,value in enumerate(visit) if value==0]  #查找未标号的顶点
        for v in id:
            if a[u,v]+dis[u]<dis[v]:
                dis[v]=dis[u]+a[u][v]
                parent[v]=u
        temp=dis
        temp[visit==1]=inf  #已标号点的距离换成无穷
        t=np.min(temp); u=temp.index(t)  #找标号值最小的顶点
        visit[u]=1  #标记已经标号的顶点
        mypath=[]
        if parent[db]!=0:  #存在路
            t=db; mypath=[db]
            while t!=sb:
                p=parent[t]; mypath.insert(0,p); t=p
#return dis[db], mypath
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]
path,distance=dijkstra(a,1,3)
         

            
            
            
    
````

</details>

#### Dijkstra算法找最短路径代码 · MATLAB · d126427e

- 归属算法：Dijkstra最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Dijkstra最短路中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d40493c81e9f32a7a8e92e824c418616dc46cf6e206575d69cb14279ad07eeb1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/Dijkstra算法找最短路径代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
克拉算法的核心就是从原点出发（原点可以是自己定义的任意一个点），
以原点为圆心，半径从小到大，判断原点到半径上面的点的最短距离，
这个距离可能是圆心r0->r1（半径较小）->r2（半径较大）或者是r0->r2（如果存在r0到r2这条路径的话）

例 某公司在六个城市c1, c2,,,, c6 中有分公司，从 ci到 cj 的直接航程票价记在 
下述矩阵的 (i, j) 位置上。（∞ 表示无直接航路），请帮助该公司设计一张城市 c1 到其它城市间的票价最便宜的路线图。 

符号含义：用矩阵 a[n,n]（n 为顶点个数）存放各边权的邻接矩阵， 行向量 pb 、 index1、 index2 、d 分别用来存放 P 标号信息、标号顶点顺序、标号顶点索引、最短通路的值。
其中分量 index2(i) 存放始点到第i 点最短通路中第i 顶点前一顶点的序号； 
d(i) 存放由始点到第i 点最短通路的值。 
求第一个城市到其它城市的最短路径的 Matlab 程序如下：
（可以直接复制下方代码运行）
其中a(1,2)表示第一个点到第二个点的距离，以此类推，在实际应用中先把所有点直接的距离矩阵写出来，不连通的点用无穷大表示

clc,clear all
a=zeros(6);
a(1,2)=50;a(1,4)=40;a(1,5)=25;a(1,6)=10;               
a(2,3)=15;a(2,4)=20;a(2,6)=25;
a(3,4)=10;a(3,5)=20;
a(4,5)=10;a(4,6)=25;
a(5,6)=55;
a=a+a'                                                  
a(find(a==0))=inf %将a=0的数全部替换为无强大               
pb(1:length(a))=0;pb(1)=1;  %当一个点已经求出到原点的最短距离时，其下标i对应的pb(i)赋1
index1=1; %存放存入S集合的顺序
index2=ones(1,length(a)); %存放始点到第i点最短通路中第i顶点前一顶点的序号
d(1:length(a))=inf;d(1)=0;  %存放由始点到第i点最短通路的值
temp=1;  %temp表示c1,算c1到其它点的最短路。
while sum(pb)<length(a)  %看是否所有的点都标记为P标号
tb=find(pb==0); %找到标号为0的所有点,即找到还没有存入S的点
d(tb)=min(d(tb),d(temp)+a(temp,tb));%计算标号为0的点的最短路，或者是从原点直接到这个点，又或者是原点经过r1,间接到达这个点
tmpb=find(d(tb)==min(d(tb)));  %求d[tb]序列最小值的下标
temp=tb(tmpb(1));%可能有多条路径同时到达最小值，却其中一个，temp也从原点变为下一个点
pb(temp)=1;%找到最小路径的表对应的pb(i)=1
index1=[index1,temp];  %存放存入S集合的顺序
temp2=find(d(index1)==d(temp)-a(temp,index1));
index2(temp)=index1(temp2(1)); %记录标号索引
end
d, index1, index2
````

</details>

#### 图论算法代码 · MATLAB · f3721e05

- 归属算法：Dijkstra最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Dijkstra最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Dijkstra最短路中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径；用中间节点递推更新全源最短路矩阵。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cdf76117f44877ea7010d93d82863333e0b2c41e45eccda48f21c66f2f9f90ff`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/图论算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
Dijkstra算法步骤
（1）构造邻接矩阵
（2）定义起始点
（3）运行代码
M=[  0     5     9   Inf   Inf   Inf   Inf
   Inf     0   Inf   Inf    12   Inf   Inf
   Inf     3     0    15   Inf    23   Inf
   Inf     6   Inf     0   Inf     8     7
   Inf    12   Inf     5     0   Inf    14
   Inf   Inf   Inf   Inf   Inf     0    10
   Inf   Inf   Inf   Inf   Inf   Inf     0];
first=2;
last=4;
[m,n]=size(M);
L=zeros(1,m);
symbol=zeros(1,m);
direction=zeros(1,m);
for i=1:m
    if(i~=first)
        L(i)=inf;
    end
    direction(i)=first;
end
judge=1;
while judge
for i=1:m
    if(symbol(i)==0)
        min=L(i);
        temporary=i;
        break
    end
end
for i=1:m
    if(symbol(i)==0)
        if(L(i)<min)
            min=L(i);
            temporary=i;
        end
    end
end
k=temporary;
for j=1:m
    if(symbol(1,j)==0)
        if(M(k,j)==inf)
            continue;
        else
            if(L(k)+M(k,j)<L(j))
                L(j)=L(k)+M(k,j);
                direction(j)=k;
            end
        end
    end
end
symbol(k)=1;
num=0;
for i=1:m
    if(symbol(i)==1)
        num=num+1;
    end
end
if(num==m)
    judge=0;
end
end
p=last;
arrow=zeros(1,m);
arrow(1)=last;
i=2;
while p~=first
    arrow(1,i)=direction(p);
    i=i+1;
    p=direction(p);
end
distance=L(last);

floyd 算法代码
d=[inf 6 0 4 0 0 0
   0 inf 0 0 5 0 0
   4 7 inf 0 0 5 0
   0 0 4 inf 0 3 0
   0 0 2 0 inf 0 0
   0 0 0 0 4 inf 5
   0 0 0 0 6 0 inf];
[m,n]=size(d);
first=1;
last=7;
direction=zeros(m,m);
for i=1:m
    direction(:,i)=i;
end
for i=1:m
    for j=1:m
        for k=1:m
            small=min(d(i,k),d(k,j));
            if d(i,j)<small
                d(i,j)=small;
                direction(i,j)=direction(i,k);
            end
        end
    end
end
arrow=zeros(1,m);
arrow(1)=first;
i=2;
p=first;
while p~=last
    p=direction(p,last);
    arrow(i)=p;
    i=i+1;
end


生成树算法代码
M=[ 0 17 11 inf inf inf
    17 0 13 12 28 15
    11 13 0 inf 19 inf
    inf 12 inf 0 inf 16
    inf 28 19 inf 0 10
    inf 15 inf 16 10 0];
[m,n]=size(M);
X=zeros(m,n);
Y=zeros(m);
Z=zeros(m);
Y(1)=1;
for i=2:m
    Z(i)=i;
end
judge=1;
while judge
for i=1:m
    if(Y(i)~=0)
        for j=1:m
            if(Z(j)~=0)
                min=M(i,j);
                a=i;
                b=j;
            end
        end
    end
end
for i=1:m
    if(Y(i)~=0)
        for j=1:m
            if(Z(j)~=0)
                if(M(i,j)<min)
                    min=M(i,j);
                    a=i;
                    b=j;
                end
            end
        end
    end
end
Y(b)=b;
Z(b)=0;
X(a,b)=1;
X(b,a)=1;
c=0;
for i=1:m
    if(Y(i)~=0)
        c=c+1;
    end
end
if(c==m)
    judge=0;
end
end
````

</details>

### Floyd最短路 · 实现

用动态规划求图中任意两点之间的最短距离。

#### anli4_1_1 · LINGO · 989227cb

- 归属算法：Floyd最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Floyd最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Floyd最短路中的“核心算法与辅助函数”。
- **执行主线**：声明整数/0-1变量并求解离散优化模型；在LINGO中声明集合、目标函数和约束后交给求解器；用中间节点递推更新全源最短路矩阵。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、文件结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`27385ef6e536da42aef9f34763e2b2de673e1c49754bf9199e54ed6f725916ab`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/anli4_1_1.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

!nodes表示节点集合;  

nodes /S1,S2,S3,S4,S5,S6,S7,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,

B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17/;         

!c1(i,j)表示节点i到j铁路运输的最小运价（万元）,c2(i,j)表示节点i到j公路运输的费用邻接矩阵，c(i,j)表示节点i到j的最小运价，path标志最短路径上走过的顶点;

link(nodes, nodes): w, c1,c2,c,path1,path;

supply/S1..S7/:S,P,f;

need/A1..A15/:b,y,z; !y表示每一点往左铺的量，z表示往右铺的量;

linkf(supply, need):cf,X;

endsets

data:

S=800 800 1000 2000 2000 2000 3000;

P=160 155  155  160  155  150  160;

b=104,301,750,606,194,205,201,680,480,300,220,210,420,500,0;

path1=0; path=0; w=0; c2=0;

! 以下是格式化输出计算的中间结果和最终结果;

@text(MiddleCost.txt)=@writefor(supply(i): @writefor(need(j): @format(cf(i,j),' 6.1f' )), @newline(1));

@text(Train_path.txt)=@writefor(nodes(i):@writefor(nodes(j):@format(path1(i,j),'5.0f')),

@newline(1));

@text(Final_path.txt)=@writefor(nodes(i):@writefor(nodes(j):@format(path(i,j),'5.0f')),

@newline(1));

@text(FinalResult.txt)=@writefor(supply(i):@writefor(need(j):@format(x(i,j),'5.0f')), @newline(1) );

@text(FinalResult.txt)=@write(@newline(1));

@text(FinalResult.txt)=@writefor(need:@format(y,'5.0f') );

@text(FinalResult.txt)=@write(@newline(2));

@text(FinalResult.txt)=@writefor(need:@format(z,'5.0f') );

enddata 

calc:

!输入铁路距离邻接矩阵的上三角元素;

w(1,29)=20;w(1,30)=202;w(2,30)=1200;w(3,31)=690;w(4,34)=690;w(5,33)=462;

w(6,38)=70;w(7,39)=30;w(23,25)=450;w(24,25)=80;w(25,27)=1150;w(26,28)=306;

w(27,30)=1100;w(28,29)=195;w(30,31)=720;w(31,32)=520;w(32,34)=170;w(33,34)=88;

w(34,36)=160;w(35,36)=70;w(36,37)=320;w(37,38)=160;w(38,39)=290;

@for(link(i,j): w(i,j) =  w(i, j)+w(j,i) ); !输入铁路距离邻接矩阵的下三角元素;

@for(link(i,j)|i#ne#j: w(i,j)=@if(w(i,j) #eq# 0, 20000,w(i,j)));  ! 无铁路连接，元素为充分大的数; 

!以下就是最短路计算公式（Floyd-Warshall算法）;

@for(nodes(k):@for(nodes(i):@for(nodes(j):tm=@smin(w(i,j),w(i,k)+w(k,j));

path1(i,j)=@if(w(i,j)#gt# tm,k,path1(i,j));w(i,j)=tm))); 

!以下就是按最短路w查找相应运费C1的计算公式;

@for(link|w#eq#0: C1=0);

@for(link|w#gt#0   #and# w#le#300: C1=20);

@for(link|w#gt#300 #and# w#le#350: C1=23);

@for(link|w#gt#350 #and# w#le#400: C1=26);

@for(link|w#gt#400 #and# w#le#450: C1=29);

@for(link|w#gt#450 #and# w#le#500: C1=32);

@for(link|w#gt#500 #and# w#le#600: C1=37);

@for(link|w#gt#600 #and# w#le#700: C1=44);

@for(link|w#gt#700 #and# w#le#800: C1=50);

@for(link|w#gt#800 #and# w#le#900: C1=55);

@for(link|w#gt#900 #and# w#le#1000: C1=60);

@for(link|w#gt#1000: C1= 60+5*@floor(w/100-10)+@if(@mod(w,100)#eq#0,0,5) );

!输入公路距离邻接矩阵的上三角元素;

c2(1,14)=31;c2(6,21)=110;c2(7,22)=20;c2(8,9)=104;c2(9,10)=301;c2(9,23)=3;

c2(10,11)=750;c2(10,24)=2;c2(11,12)=606;c2(11,27)=600;c2(12,13)=194;c2(12,26)=10;

c2(13,14)=205;c2(13,28)=5;c2(14,15)=201;c2(14,29)=10;c2(15,16)=680;c2(15,30)=12;

c2(16,17)=480;c2(16,31)=42;c2(17,18)=300;c2(17,32)=70;c2(18,19)=220;c2(18,33)=10;

c2(19,20)=210;c2(19,35)=10;c2(20,21)=420;c2(20,37)=62;c2(21,22)=500;c2(21,38)=30;

c2(22,39)=20;

@for(link(i,j): c2(i,j) = c2(i,j)+c2(j,i));  !输入公路距离邻接矩阵的下三角元素;

@for(link(i,j):c2(i,j)=0.1*c2(i,j)); ! 距离转化成费用;

@for(link(i,j)|i#ne#j: c2(i,j) =@if(c2(i,j)#eq#0,10000,c2(i,j) ));  !无公路连接，元素为充分大的数;

@for(link: C= @smin(C1,C2));  ! C1和C2矩阵对应元素取最小; 

@for(nodes(k):@for(nodes(i):@for(nodes(j):tm=@smin(C(i,j),C(i,k)+C(k,j));

path(i,j)=@if(C(i,j)#gt# tm,k,path(i,j));C(i,j)=tm))); 

@for(link(i,j)|i #le# 7 #and# j#ge#8 #and# j#le# 22:cf(i,j-7)=c(i,j)); !提取下面二次规划模型需要的7×15矩阵;

endcalc

[obj]min=@sum(linkf(i,j):(cf(i,j)+p(i))*x(i,j))+0.05*@sum(need(j):y(j)^2+y(j)+z(j)^2+z(j));

! 约束;

@for(supply(i):[con1]@sum(need(j):x(i,j))<= S(i)*f(i));

@for(supply(i):[con2]@sum(need(j):x(i,j)) >= 500*f(i)); 

@for(need(j):[con3] @sum(supply(i):x(i,j))=y(j)+z(j)); 

@for(need(j)|j#NE#15:[con4] z(j)+y(j+1)=b(j)); 

y(1)=0; z(15)=0;

@for(supply: @bin(f));

@for(need: @gin(y));

end
````

</details>

#### anli4_1_2 · LINGO · 82bd1630

- 归属算法：Floyd最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Floyd最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Floyd最短路中的“核心算法与辅助函数”。
- **执行主线**：声明整数/0-1变量并求解离散优化模型；在LINGO中声明集合、目标函数和约束后交给求解器；用中间节点递推更新全源最短路矩阵。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、文件结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e64711ecc8d41be5abc55e16dec1033be20eca039de642a57d0fb8dd1cbe6d16`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/anli4_1_2.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

 ! nodes表示节点集合;  

nodes /S1,S2,S3,S4,S5,S6,S7,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12/;         

!c1(i,j)表示节点i到j铁路运输的最小单位运价（万元）,c2(i,j)表示节点i到j公路运输的邻接权重矩阵，c(i,j)表示节点i到j的最小单位运价，path标志最短路径上走过的顶点;

link(nodes, nodes): w, c1,c2,c,path1,path;

supply/S1..S7/:s,p,f;

need/A1..A21/:b,y,z;!y表示每一点往节点编号小的方向铺设量，z表示往节点编号大的方向铺设量;

linkf(supply, need):cf,x;

special/1..3/:sx;  ! 铺设节点9，11，17往最大编号节点方向的铺设量;

endsets

data:

s=800 800 1000 2000 2000 2000 3000;

p=160 155  155  160  155  150  160;

b=104,301,750,606,194,205,201,680,480,300,220,210,420,500,42,10,130,190,260,100,0;

path1=0; path=0; w=0; c2=0;

! 以下是格式化输出计算的中间结果和最终结果;

@text(MiddleCost.txt)=@writefor(supply(i): @writefor(need(j): @format(cf(i,j),' 6.1f' )), @newline(1));

@text(Train_path.txt)=@writefor(nodes(i):@writefor(nodes(j):@format(path1(i,j),'5.0f')),

@newline(1));

@text(Final_path.txt)=@writefor(nodes(i):@writefor(nodes(j):@format(path(i,j),'5.0f')),

@newline(1));

@text(FinalResult.txt)=@writefor(supply(i):@writefor(need(j):@format(x(i,j),'5.0f')), @newline(1) );

@text(FinalResult.txt)=@write(@newline(1));

@text(FinalResult.txt)=@writefor(need:@format(y,'5.0f'));

@text(FinalResult.txt)=@write(@newline(2));

@text(FinalResult.txt)=@writefor(need:@format(z,'5.0f'));

enddata 

calc:

!输入铁路距离邻接矩阵的上三角元素;

w(28,30)=450;w(29,30)=80;w(30,32)=1150;w(31,33)=306;w(33,34)=195;w(1,34)=20;

w(1,35)=202;w(32,35)=1100;w(2,35)=1200;w(23,35)=720;w(3,23)=690;w(23,36)=520;

w(36,37)=170;w(4,37)=690;w(5,24)=462;w(24,37)=88;w(25,37)=160;w(25,26)=70;

w(25,27)=320;w(27,38)=160;w(6,38)=70;w(38,39)=290;w(7,39)=30;

@for(link(i,j): w(i,j) =  w(i, j)+w(j,i) );!输入铁路距离邻接矩阵的下三角元素;

@for(link(i,j)|i#ne#j: w(i,j)=@if(w(i,j) #eq# 0, 20000,w(i,j)));  ! 无铁路连接，元素为充分大的数; 

!以下就是最短路计算公式（Floyd-Warshall算法）;

@for(nodes(k):@for(nodes(i):@for(nodes(j):tm=@smin(w(i,j),w(i,k)+w(k,j));

path1(i,j)=@if(w(i,j)#gt# tm,k,path1(i,j));w(i,j)=tm))); 

!以下就是按最短路w查找相应运费C1的计算公式;

@for(link|w#eq#0: C1=0);

@for(link|w#gt#0   #and# w#le#300: C1=20);

@for(link|w#gt#300 #and# w#le#350: C1=23);

@for(link|w#gt#350 #and# w#le#400: C1=26);

@for(link|w#gt#400 #and# w#le#450: C1=29);

@for(link|w#gt#450 #and# w#le#500: C1=32);

@for(link|w#gt#500 #and# w#le#600: C1=37);

@for(link|w#gt#600 #and# w#le#700: C1=44);

@for(link|w#gt#700 #and# w#le#800: C1=50);

@for(link|w#gt#800 #and# w#le#900: C1=55);

@for(link|w#gt#900 #and# w#le#1000: C1=60);

@for(link|w#gt#1000: C1= 60+5*@floor(w/100-10)+@if(@mod(w,100)#eq#0,0,5) );

!输入公路距离邻接矩阵的上三角元素;

c2(8,9)=104;c2(9,10)=301;c2(10,11)=750;c2(11,12)=606;c2(12,13)=194;c2(13,14)=205;

c2(14,15)=201;c2(15,16)=680;c2(16,17)=480;c2(16,23)=42;c2(17,18)=300;c2(18,19)=220;

c2(18,24)=10;c2(19,20)=210;c2(20,21)=420;c2(21,22)=500;c2(24,25)=130;c2(24,26)=190;

c2(26,27)=260;c2(6,27)=100;c2(9,28)=3;c2(10,29)=2;c2(11,32)=600;c2(12,31)=10;

c2(13,33)=5;c2(14,34)=10;c2(1,14)=31;c2(15,35)=12;c2(17,36)=70;c2(19,26)=10;

c2(20,27)=62;c2(6,21)=110;c2(21,38)=30;c2(22,39)=20;c2(7,22)=20;

@for(link(i,j): c2(i,j) = c2(i,j)+c2(j,i)); !输入公路距离邻接矩阵的下三角元素;

@for(link(i,j):c2(i,j)=0.1*c2(i,j));  ! 距离转化成费用;

@for(link(i,j)|i#ne#j: c2(i,j) =@if(c2(i,j)#eq#0,10000,c2(i,j) )); !无边对应的元素充分大;

@for(link: C= @smin(C1,C2));  ! C1和C2矩阵对应元素取最小;

@for(nodes(k):@for(nodes(i):@for(nodes(j):tm=@smin(C(i,j),C(i,k)+C(k,j));

path(i,j)=@if(C(i,j)#gt# tm,k,path(i,j));C(i,j)=tm))); 

@for(link(i,j)|i #le# 7 #and# j#ge#8 #and# j#le# 27:cf(i,j-7)=c(i,j)); !提取下面二次规划模型需要的7×21矩阵;

@for(supply(i):cf(i,21)=c(i,6));

endcalc

[obj]min=@sum(linkf(i,j):(cf(i,j)+p(i))*x(i,j))+0.05*@sum(need(j):y(j)^2+y(j)+z(j)^2+z(j))+0.05*@sum(special:sx^2+sx);

! 约束;

@for(supply(i):[con1]@sum(need(j):x(i,j))<= s(i)*f(i));

@for(supply(i):[con2]@sum(need(j):x(i,j)) >= 500*f(i)); 

@for(need(j)|j#ne#9 #and# j#ne#11 #and# j#ne#17:[con3] @sum(supply(i):x(i,j))=y(j)+z(j)); 

y(9)+z(9)+sx(1)=@sum(supply(i):x(i,9)); y(11)+z(11)+sx(2)=@sum(supply(i):x(i,11));

y(17)+z(17)+sx(3)=@sum(supply(i):x(i,17));

@for(need(j)|j #le# 14:(z(j)+y(j+1))=b(j));

@for(need(j)|j#ge#19 #and# j#le#20:z(j)+y(j+1)=b(j));

sx(1)+y(16)=42; sx(2)+y(17)=10; sx(3)+y(19)=190; z(17)+y(18)=130;

y(1)+z(15)+z(16)+z(18)+z(21)=0;

@for(supply: @bin(f)); @for(need: @gin(y));

end
````

</details>

#### 足球队排名matlab实现 · MATLAB · 906d0d44

- 归属算法：Floyd最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Floyd最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Floyd最短路中的“核心算法与辅助函数”。
- **执行主线**：用中间节点递推更新全源最短路矩阵。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9182a9f131e20916b267c837c07436821188ddc45123edfcb20207c5c00c7fac`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/综合评价方法/层次分析法/AHP理论/足球队排名matlab实现.txt`

<details>
<summary>展开原始代码</summary>

````matlab
%足球队排名次的matlab程序
%interWinTimes(i,j)表示Ti与Tj对抗时胜的场次；  
%netWinGoals(i,j)表示Ti与Tj对抗时净胜球数；
%无比赛interWinTimes设为-1；当i=j时，interWinTimes设为0；
%无比赛netWinGoals设为-1；当i=j时，netWinGoals设为0；




%输入数据 
%disp('请输入interWinTimes矩阵(n阶)');
%interWinTimes=input('interWinTimes=');

%disp('请输入netWinGoals矩阵(n阶)');
%netWinGoals=input('netWinGoals=');

%程序核心部分开始；

interWinTimes=[0 1 1 3 1 1 0 1 2 0 -1 -1;1 0 1 1 0 1 0 0 1 0 -1 -1;1 2 0 1 1 1 1 1 1 1 -1 -1;0 0 0 0 0 0 0 1 0 0 -1 -1;0 0 0 1 0 0 -1 -1 -1 -1 1 0;0 0 0 1 1 0 -1 -1 -1 -1 -1 -1;2 0 1 2 -1 -1 0 2 3 2 1 1;1 0 1 1 -1 -1 0 0 1 1 1 0;0 0 1 1 -1 -1 0 2 0 2 1 1;0 1 1 1 -1 -1 0 1 0 0 1 1;-1 -1 -1 -1 1 -1 0 0 0 0 0 0;-1 -1 -1 -1 1 -1 0 0 0 0 1 0];
netWinGoals=[0 0 -1 5 2 1 -3 -1 5 0 -1 -1;0 0 -1 2 0 1 0 0 2 -2 -1 -1;1 1 0 2 1 3 -2 1 0 1 -1 -1;-5 -2 -2 0 -1 -1 -6 -1 -1 -1 -1 -1;-2 0 -1 1 0 -1 -1 -1 -1 -1 0 -1;-1 -1 -3 1 1 0 -1 -1 -1 -1 -1 -1;3 0 2 6 -1 -1 0 3 5 5 2 2;1 0 -1 1 -1 -1 -3 0 0 0 2 0;-5 -2 0 1 -1 -1 -5 0 0 4 1 1;0 2 -1 1 -1 -1 -5 0 -4 0 1 2;-1 -1 -1 -1 0 -1 -2 -2 -1 -1 0 -1;-1 -1 -1 -1 1 -1 -2 0 -1 -2 1 0];
[n,n]=size(interWinTimes);
a=zeros(n,n);

for i=1:n
  for j=1:n
    if interWinTimes(i,j)==interWinTimes(j,i) 
      if netWinGoals(i,j)==0
          a(i,j)=1;
          a(j,i)=1;
          continue;
      end 

      if netWinGoals(i,j)>0
          interWinTimes(i,j)=1
          interWinTimes(j,i)=0 
      end 
    end
    k=0;
    k=interWinTimes(i,j)- interWinTimes(j,i)
if k>0 
%根据k值设定相应的b,用的是一个尺度判定的方法.再根据Ti胜Tj每场净胜球数来决定d
if k>4
   b(i,j)=9
else
   b(i,j)=2*k
end

%计算平均每场净胜球数=净胜球数/净胜场次
m=zeros(n,n);
d=zeros(n,n);
m(i,j)=netWinGoals(i,j)/k;
if m(i,j)>2
    d(i,j)=1;
     else if m(i,j)<0
      d(i,j)=-1;
         else
         d(i,j)=0;
         end
     end
     a(i,j)=b(i,j)+d(i,j);
     a(j,i)=1/a(i,j);
end
if interWinTimes(i,j)==-1
    a(i,j)=0;
    a(j,i)=0;
end
  end
end
%判断矩阵a的可约性（修改的floyd算法）
for i=1:n
    for j=1:n
        if a(i,j)==0
            a(i,j)=inf;
        end
    end
end
n=size(a,1);
D=a
for k=1:n
    for i=1:n
        for j=1:n
            if D(i,k)+D(k,j)<D(i,j)
                D(i,j)=D(i,k)+D(k,j);
            end
        end
    end
end
for i=1:n
    for j=1:n
        if D(i,j)==inf
            disp('成绩表可约，无法排序');
            pause
            quit
        end
    end
end
for i=1:n
    for j=1:n
        if a(i,j)==inf
            a(i,j)=0;
        end
    end
end
%构造辅助矩阵A
A=zeros(n,n);
m=zeros(n);
for i=1:n
    for j=1:n
        if a(i,j)==0
            m(i)=m(i)+1;
        end
    end
end
for i=1:n
    for j=1:n
        if a(i,j)~=0 & i~=j
            A(i,j)=a(i,j);
        else if i==j
                A(i,j)=m(i)+1;
            else
                A(i,j)=0;
            end
        end
    end
end
%计算A的主特征根和主特征向量(用的是幂法)
x=ones(n,100);
y=ones(n,100);
m=zeros(1,100);
m(1)=max(x(:,1));
y(:,1)=x(:,1);
x(:,2)=A*y(:,1);
m(2)=max(x(:,2));
y(:,2)=x(:,2)/m(2);
p=0.0001;i=2;k=abs(m(2)-m(1));
while  k>p
    i=i+1;
    x(:,i)=A*y(:,i-1);
    m(i)=max(x(:,i));
    y(:,i)=x(:,i)/m(i);
    k=abs(m(i)-m(i-1));
end
a=sum(y(:,i));
w=y(:,i)/a;
t=m(i);
disp('权向量');disp(w);
disp('最大特征值');disp(t);
````

</details>

#### Pex10_7 · Python · 2df171f4

- 归属算法：Floyd最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Floyd最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Floyd最短路中的“核心算法与辅助函数”。
- **执行主线**：用中间节点递推更新全源最短路矩阵。
- **调用方式**：优先调用 `floyd`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e2b8b15a754bda13742255c04c74f5b8f09f30948fce31a9c9522b68675a9cc3`
- 语言：Python
- 符号：`floyd`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_7.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件py10_7.py
import numpy as np
def floyd(graph):
    m = len(graph)
    dis = graph
    path = np.zeros((m, m))  #路由矩阵初始化
    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = k
    return dis, path
inf=np.inf
a=np.array([[0,1,2,inf,7,inf,4,8],[1,0,2,3,inf,inf,inf,7],
  [2,2,0,1,5,inf,inf,inf],[inf,3,1,0,3,6,inf,inf],
  [7,inf,5,3,0,4,3,inf],[inf,inf,inf,6,4,0,6,4],
  [4,inf,inf,inf,3,6,0,2],[8,7,inf,inf,inf,4,2,0]])  #输入邻接矩阵
dis, path=floyd(a)
print("所有顶点对之间的最短距离为：\n", dis, '\n',"路由矩阵为：\n",path)
````

</details>

#### myfloyd · Python · f9772524

- 归属算法：Floyd最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Floyd最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于Floyd最短路中的“核心算法与辅助函数”。
- **执行主线**：用中间节点递推更新全源最短路矩阵。
- **调用方式**：优先调用 `floyd`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6e56eff6af87278d48bc8d093231713afe6f06f4295afdce323c3ac98b929563`
- 语言：Python
- 符号：`floyd`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/myfloyd.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件py10_6.py
import numpy as np
def floyd(graph):
    m = len(graph)
    dis = graph
    path = np.zeros((m, m))  #路由矩阵初始化
    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = k

    return dis, path
inf=np.inf
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]  #输入邻接矩阵
dis, path=floyd(a)
print("所有顶点对之间的最短距离为：\n", dis, '\n',"路由矩阵为：\n",path)
        
    
````

</details>

#### Floyd算法求最小距离代码 · MATLAB · efdfd798

- 归属算法：Floyd最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#Floyd最短路 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于Floyd最短路中的“核心算法与辅助函数”。
- **执行主线**：用中间节点递推更新全源最短路矩阵。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e8ee1147deb430d0906cd5642ef79a79451072c8e8d1d63a16c50a2be8d1ea91`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/Floyd算法求最小距离代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
基本函数代码，请将下属代码复制到Matlab函数输入中，将其保存在根目录下
function [d,r]=floyd(a)
n=size(a,1);
% 初始化距离矩阵
d=a;
% 初始化路由矩阵
for i=1:n
    for j=1:n
        r(i,j)=j;
    end 
end 
r;

% Floyd算法开始
for k=1:n
    for i=1:n
        for j=1:n
            if d(i,k)+d(k,j)<d(i,j)
                d(i,j)=d(i,k)+d(k,j);
                r(i,j)=r(i,k);
            end 
        end 
    end
    k;
    d;
    r;
end
d
r

复制到上面截至就可以了，直接调用是不可以的，因为a还没有赋值，下面是具体的符号解释
a是距离矩阵，也就是各顶点间的距离
R是路由矩阵，指的是找到各点之间的最短距离对应的路径，不懂得可以看一下原理
例如
a=[0 4 11;6 0 2;3 inf 0];
````

</details>

### 图与网络综合例程 · 实现

#### ex4_1 · MATLAB · 76ded227

- 归属算法：图与网络综合例程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图与网络综合例程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图与网络综合例程中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`88bcda71e2d0c05ec4204202df10d3843adcc5565bbd7952dfb7684f52ebcc3d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
a=zeros(6); %邻接矩阵初始化
a(1,2)=50;a(1,4)=40;a(1,5)=25;a(1,6)=10;
a(2,3)=15;a(2,4)=20;a(2,6)=25;
a(3,4)=10;a(3,5)=20;
a(4,5)=10;a(4,6)=25;
a(5,6)=55;
a=a+a';
a(find(a==0))=inf;
pb(1:length(a))=0;pb(1)=1;index1=1;index2=ones(1,length(a));
d(1:length(a))=inf;d(1)=0;
temp=1; %最新的P标号的顶点
while sum(pb)<length(a)
   tb=find(pb==0);
   d(tb)=min(d(tb),d(temp)+a(temp,tb));
   tmpb=find(d(tb)==min(d(tb)));
   temp=tb(tmpb(1)); %可能有多个点同时达到最小值，只取其中的一个
   pb(temp)=1;
   index1=[index1,temp];
   temp2=find(d(index1)==d(temp)-a(temp,index1));
   index2(temp)=index1(temp2(1));
end
d, index1, index2
````

</details>

#### ex4_13 · MATLAB · 949d59fb

- 归属算法：图与网络综合例程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图与网络综合例程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图与网络综合例程中的“核心算法与辅助函数”。
- **执行主线**：在残量网络上计算最大流或最小费用流。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`37ee181cc769858038142b9401bcb1d2edb199a66e1565e6d8ff8abdf6608858`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_13.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear, a=zeros(9);
a(1,2)=6; a(1,3)=4; a(1,4)=5;
a(2,3)=3; a(2,5)=9; a(2,6)=9;
a(3,4)=4; a(3,5)=6; a(3,6)=7; a(3,7)=3;
a(4,7)=5; a(4,9)=2;
a(5,8)=12;
a(6,5)=8; a(6,8)=10;
a(7,6)=4; a(7,8)=15; 
a(9,3)=2;
b=sparse(a);
[x,y,z]=graphmaxflow(b,1,8)
````

</details>

#### ex4_4 · MATLAB · 3b0568a8

- 归属算法：图与网络综合例程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图与网络综合例程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图与网络综合例程中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5d9b514c810e13db875d05a0ca6ccd672126b4f43f4b9606a97c0e869aaad09a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_4.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear;clc;
n=6; a=zeros(n);
a(1,2)=50;a(1,4)=40;a(1,5)=25;a(1,6)=10;
a(2,3)=15;a(2,4)=20;a(2,6)=25; a(3,4)=10;a(3,5)=20;
a(4,5)=10;a(4,6)=25; a(5,6)=55;
a=a+a'; 
a(a==0)=inf; %把所有零元素替换成无穷
a([1:n+1:n^2])=0; %对角线元素替换成零，Matlab中数据是逐列存储的
path=zeros(n);
for k=1:n
   for i=1:n
      for j=1:n
         if a(i,j)>a(i,k)+a(k,j)
            a(i,j)=a(i,k)+a(k,j);
            path(i,j)=k;
         end 
      end
   end
end
a, path
````

</details>

#### ex4_5 · MATLAB · ece0f8f3

- 归属算法：图与网络综合例程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图与网络综合例程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图与网络综合例程中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`73f0fc116469943367e6da5a3ba5722b5047533da3838637ad58a317e5ea21a1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_5.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc;clear;
a=zeros(7);
a(1,2)=50; a(1,3)=60;
a(2,4)=65; a(2,5)=40;
a(3,4)=52;a(3,7)=45;
a(4,5)=50; a(4,6)=30;a(4,7)=42;
a(5,6)=70; 
a=a+a';a(a==0)=inf;
result=[];p=1;tb=2:length(a);
while size(result,2)~=length(a)-1
   temp=a(p,tb);temp=temp(:);
   d=min(temp);
   [jb,kb]=find(a(p,tb)==d);
   j=p(jb(1));k=tb(kb(1));
   result=[result,[j;k;d]];p=[p,k];tb(find(tb==k))=[];
end
result
````

</details>

#### ex4_6 · MATLAB · 40c51c3f

- 归属算法：图与网络综合例程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图与网络综合例程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图与网络综合例程中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`96b7e3eba8b297957aa2b912ab6f2fee8c4a8cf4a1d25000c1a48859ee270623`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_6.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc;clear;
a(1,2)=50; a(1,3)=60; a(2,4)=65; a(2,5)=40;
a(3,4)=52;a(3,7)=45; a(4,5)=50; a(4,6)=30;
a(4,7)=42; a(5,6)=70; 
[i,j,b]=find(a);
data=[i';j';b'];index=data(1:2,:);
loop=length(a)-1;
result=[];
while length(result)<loop
   temp=min(data(3,:));
   flag=find(data(3,:)==temp);
   flag=flag(1);
   v1=index(1,flag);v2=index(2,flag);
   if v1~=v2
      result=[result,data(:,flag)];
   end
   index(find(index==v2))=v1;
   data(:,flag)=[];
   index(:,flag)=[];
end
result
````

</details>

#### main · MATLAB · 41d01094

- 归属算法：图与网络综合例程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图与网络综合例程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图与网络综合例程中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `main`；先核对参数顺序和返回值。
- **主要输出**：函数返回值
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`34b9185cb5f2a1fd02269a5a370f86e8b872242df6b34b75c8ef353d51d01d40`
- 语言：MATLAB
- 符号：`main`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/main.m`

<details>
<summary>展开原始代码</summary>

````matlab
function main
a=zeros(6);
a(1,2)=56;a(1,3)=35;a(1,4)=21;a(1,5)=51;a(1,6)=60;
a(2,3)=21;a(2,4)=57;a(2,5)=78;a(2,6)=70; a(3,4)=36;a(3,5)=68;a(3,6)=68; a(4,5)=51;a(4,6)=61;
a(5,6)=13; a=a+a'; L=size(a,1);
c=[5 1:4 6 5]; %选取初始圈
[circle,long]=modifycircle(a,L,c)  %调用下面修改圈的子函数
%*******************************************
%以下为修改圈的子函数
%*******************************************
function [circle,long]=modifycircle(a,L,c);
for k=1:L
flag=0;   %退出标志
for m=1:L-2   %m为算法中的i
for n=m+2:L   %n为算法中的j
 if a(c(m),c(n))+a(c(m+1),c(n+1))<a(c(m),c(m+1))+a(c(n),c(n+1))
      c(m+1:n)=c(n:-1:m+1); flag=flag+1; %修改一次，标志加1
 end
end
end
     if flag==0   %一条边也没有修改,就返回
       long=0;   %圈长的初始值
       for i=1:L
         long=long+a(c(i),c(i+1)); %求改良圈的长度
       end
       circle=c;   %返回修改圈
       return
     end
end
````

</details>

### 图论与排队 · 实现

#### floydpath · MATLAB · 1a51c231

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：用中间节点递推更新全源最短路矩阵。
- **调用方式**：优先调用 `floydpath`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a8cc013f5de6915302e69fee5b88474fe181d7013acbb41fb6a3c8fb03e29ddd`
- 语言：MATLAB
- 符号：`floydpath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/ZUIXIAOFEI/floydpath.m`

<details>
<summary>展开原始代码</summary>

````matlab
%求最短路径函数
function path=floydpath(w);
global M num
w=w+((w==0)-eye(num))*M;
p=zeros(num);
for k=1:num
for i=1:num
for j=1:num
if w(i,j)>w(i,k)+w(k,j)
w(i,j)=w(i,k)+w(k,j);
p(i,j)=k;
end
end
end
end
if w(1,num) ==M
path=[];
else
path=zeros(num);
s=1;t=num;m=p(s,t);
while ~isempty(m)
if m(1)
s=[s,m(1)];t=[t,t(1)];t(1)=m(1);
m(1)=[];m=[p(s(1),t(1)),m,p(s(end),t(end))];
else
path(s(1),t(1))=1;s(1)=[];m(1)=[];t(1)=[];
end
end
end
````

</details>

#### mydijkstra · MATLAB · 8ee5fec3

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a043fa389e11731b2036a02cf7acc7a856fd76a431c8004362b85cab9fba76ec`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/mydijkstra.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [mydistance,mypath]=mydijkstra(a,sb,db);
% 输入：a—邻接矩阵，a（i，j)是指i到j之间的距离，可以是有向的
% sb—起点的标号, db—终点的标号
% 输出：mydistance—最短路的距离, mypath—最短路的路径
n=size(a,1); visited(1:n) = 0;
distance(1:n) = inf; distance(sb) = 0; %起点到各顶点距离的初始化
visited(sb)=1; u=sb;  %u为最新的P标号顶点
parent(1:n) = 0; %前驱顶点的初始化
for i = 1: n-1
     id=find(visited==0); %查找未标号的顶点
     for v = id           
         if  a(u, v) + distance(u) < distance(v)
             distance(v) = distance(u) + a(u, v);  %修改标号值 
             parent(v) = u;                                    
         end            
     end
     temp=distance;
     temp(visited==1)=inf;  %已标号点的距离换成无穷
     [t, u] = min(temp);  %找标号值最小的顶点 
     visited(u) = 1;       %标记已经标号的顶点
 end
mypath = [];
if parent(db) ~= 0   %如果存在路!
    t = db; mypath = [db];
    while t ~= sb
        p = parent(t);
        mypath = [p mypath];
        t = p;      
    end
end
mydistance = distance(db);
````

</details>

#### myfloyd · MATLAB · 4cf84f75

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：用中间节点递推更新全源最短路矩阵。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`aa92ff5c00ce16e9620af1661faf279b3a67e887e7209213a5cd559a66d281b9`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/myfloyd.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [dist,mypath]=myfloyd(a,sb,db);
% 输入：a—邻接矩阵，元素(aij)是顶点i到j之间的直达距离，可以是有向的
% sb—起点的标号；db—终点的标号
% 输出：dist—最短路的距离；% mypath—最短路的路径
n=size(a,1); path=zeros(n);
for k=1:n
    for i=1:n
        for j=1:n
            if a(i,j)>a(i,k)+a(k,j)
                a(i,j)=a(i,k)+a(k,j);
                path(i,j)=k;
            end
        end
    end
end
dist=a(sb,db);
parent=path(sb,:); %从起点sb到终点db的最短路上各顶点的前驱顶点
parent(parent==0)=sb; %path中的分量为0，表示该顶点的前驱是起点
mypath=db; t=db;
while t~=sb
        p=parent(t); mypath=[p,mypath];
        t=p;
end
````

</details>

#### bianquan · MATLAB · 049d2d5b

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f2855c207c85a400617240c87300a516440286b593799105317b160a1c3e0d92`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/三边交换简单算法/bianquan.m`

<details>
<summary>展开原始代码</summary>

````matlab
N=13;
for i=1:N
    for j=1:N
        C(i,j)=inf;
    end
end
for i=1:N
    C(i,i)=0;
end
C(1,2)=6.0;C(1,13)=12.9;
C(2,3)=5.9;C(2,4)=10.3;
C(3,4)=12.2;C(3,5)=17.6;
C(4,13)=8.8;C(4,7)=7.4;
C(4,5)=11.5;
C(5,2)=17.6;C(5,6)=8.2;
C(6,9)=14.9;C(6,7)=20.3;
C(7,9)=19.0;C(7,8)=7.3;
C(8,9)=8.1;C(8,13)=9.2;
C(9,10)=10.3;
C(10,11)=7.7;
C(11,12)=7.2;
C(12,13)=7.9;
for i=1:N
    for j=1:N
        if  C(i,j) < inf
            C(j,i)=C(i,j);
        end
    end
end
for i=1:N
    C(i,i)=0;
end

R=[4 7 6 5 3 2 1 13 12 11 10 9 8];
````

</details>

#### jiaohuan3 · MATLAB · 076f9cd4

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`1f874395344a4e840d279ae18577c1b313d869c7f295422a06e6506598a11cfe`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/三边交换简单算法/jiaohuan3.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/图论/哈密尔顿回路/三边交换简单算法/cost_sum.m`

<details>
<summary>展开原始代码</summary>

````matlab
n=0;
for I=1:(N-2)
    for J=(I+1):(N-1)
        for K=(J+1):N
            n=n+1;
            Z(n,:)=[I J K];
        end
    end
end
R=1:N
for m=1:(N*(N-1)*(N-2)/6)
    I=Z(m,1);J=Z(m,2);K=Z(m,3);
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
    if cost_sum(r,C,N)<cost_sum(R,C,N)
        R=r
    end
end
fprintf('总长为%f\n',cost_sum(R,C,N))
````

</details>

#### Pex10_10 · Python · 11763405

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`de68538fe91d8828bad1e6af79cd64b0bbc0c0beb7960a0b654c3a4cceea3878`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_10.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_10.py
import numpy as np
import networkx as nx
List=[(1,2,20),(1,5,15),(2,3,20),(2,4,40),
      (2,5,25),(3,4,30),(3,5,10),(5,6,15)]
G=nx.Graph()
G.add_nodes_from(range(1,7))
G.add_weighted_edges_from(List)
c=dict(nx.shortest_path_length(G,weight='weight'))
d=np.zeros((6,6))
for i in range(1,7):
    for j in range(1,7): d[i-1,j-1]=c[i][j]
print(d)
q=np.array([80,90,30,20,60,10])
m=d@q  #计算运力，这里使用矩阵乘法
mm=m.min()  #求运力的最小值
ind=np.where(m==mm)[0]+1  #python下标从0开始，np.where返回值为元组
print("运力m=",m,'\n最小运力mm=',mm,"\n选矿厂的设置位置为：",ind)
````

</details>

#### Pex10_15 · Python · 3e400166

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ac9c36529dd3332afc87f03decf7c2f3c722f0a41f5ecba8ed48b7fdb00f580c`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_15.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_15.py
import numpy as np
import networkx as nx
from networkx.algorithms.matching import max_weight_matching
a=np.array([[3,5,5,4,1],[2,2,0,2,2],[2,4,4,1,0],
            [0,2,2,1,0],[1,2,1,3,3]])
b=np.zeros((10,10)); b[0:5,5:]=a; G=nx.Graph(b)
s0=max_weight_matching(G)  #返回值为（人员，工作）的集合
s=[sorted(w) for w in s0]
L1=[x[0] for x in s]; L1=np.array(L1)+1  #人员编号
L2=[x[1] for x in s]; L2=np.array(L2)-4  #工作编号
c=a[L1-1,L2-1]  #提取对应的效益
d=c.sum()  #计算总的效益
print("工作分配对应关系为：\n人员编号：",L1)
print("工作编号：", L2); print("总的效益为：",d)
````

</details>

#### Pex10_2_1 · Python · a271e9d0

- 归属算法：图论与排队
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`167d3101c16d505ac957d518dce13754b73220ddcb797cf232fb8aa14e55c5b7`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_2_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_2_1.py
import numpy as np
import networkx as nx
import pylab as plt
a=np.zeros((5,5))
a[0,1:5]=[9, 2, 4, 7]; a[1,2:4]=[3,4]
a[2,[3,4]]=[8, 4]; #输入邻接矩阵的上三角元素
a[3,4]=6; print(a); np.savetxt("Pdata10_2.txt",a) #保存邻接矩阵供以后使用
i,j=np.nonzero(a)  #提取顶点的编号
w=a[i,j]  #提出a中的非零元素
edges=list(zip(i,j,w))
G=nx.Graph()
G.add_weighted_edges_from(edges)
key=range(5); s=[str(i+1) for i in range(5)]
s=dict(zip(key,s))  #构造用于顶点标注的字符字典
plt.rc('font',size=18)
plt.subplot(121); nx.draw(G,font_weight='bold',labels=s)
plt.subplot(122); pos=nx.shell_layout(G)  #布局设置
nx.draw_networkx(G,pos,node_size=260,labels=s)
w = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,font_size=12,edge_labels=w) #标注权重
plt.savefig("figure10_2.png", dpi=500); plt.show()
````

</details>

#### Pex10_2_2 · Python · bea17fa6

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c1a7ae0d7e0c72c579aeb0b4a25174ee47c85c82edd805a3e69d7e381c8c1314`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_2_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_2_2.py
import networkx as nx
import pylab as plt
import numpy as np
List=[(1,2,9),(1,3,2),(1,4,4),(1,5,7),
  (2,3,3),(2,4,4),(3,4,8),(3,5,4),(4,5,6)]
G=nx.Graph()
G.add_nodes_from(range(1,6))
G.add_weighted_edges_from(List)
pos=nx.shell_layout(G)
w = nx.get_edge_attributes(G,'weight')
nx.draw(G, pos,with_labels=True, font_weight='bold',font_size=12)
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
plt.show()
````

</details>

#### Pex10_3 · Python · 9e451e37

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`d49c69a77f2cf897659526d74242af8062022350565373d29f772b8c186c9873`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_3.py
import numpy as np
import networkx as nx
import pylab as plt
G=nx.DiGraph()
List=[(1,2),(1,3),(2,3),(3,2),(3,5),(4,2),(4,6),
      (5,2),(5,4),(5,6),(6,5)]
G.add_nodes_from(range(1,7))
G.add_edges_from(List)
plt.rc('font',size=16)
pos=nx.shell_layout(G) 
nx.draw(G,pos,with_labels=True, font_weight='bold',node_color='r')
plt.savefig("figure10_3.png", dpi=500); plt.show()
````

</details>

#### Pex10_4 · Python · feff6737

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`ee0b2632a6680506452ae5de58e9fe0f4ef915c2afffee3124bc5d58173b7ea7`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_4.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_4.py
import numpy as np
import networkx as nx
import pylab as plt
a=np.loadtxt("Pdata10_2.txt")
G=nx.Graph(a)     #利用邻接矩阵构造赋权无向图
print("图的顶点集为：", G.nodes(),"\n边集为：", G.edges())
print("邻接表为：", list(G.adjacency()))  #显示图的邻接表
print("列表字典为：", nx.to_dict_of_lists(G)) 
B=nx.to_numpy_matrix(G)  #从图G中导出邻接矩阵B，这里B=a
C=nx.to_scipy_sparse_matrix(G)  #从图G中导出稀疏矩阵C
````

</details>

#### 相似实现组 · Python · c2f0a841

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：7
- 原始来源文件：7
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：Pex10_5.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：优先调用 `Dijkstra_all_minpath`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`bab5c6aa61c525c8f19d4af06c0cd9095d2bf1f1adad963e93b8759d369604f8`
- 语言：Python
- 符号：`Dijkstra_all_minpath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_5.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_5.py
import numpy as np
inf=np.inf
def Dijkstra_all_minpath( matr,start): #matr为邻接矩阵的数组，start表示起点
    n=len( matr) #该图的节点数
    dis=[]; temp=[]
    dis.extend(matr[start])  #添加数组matr的start行元素
    temp.extend(matr[start]) #添加矩阵matr的start行元素
    temp[start] = inf  #临时数组会把处理过的节点的值变成inf
    visited=[start]  #start已处理
    parent=[start]*n   #用于画路径，记录此路径中该节点的父节点
    while len(visited)<n:
        i= temp.index(min(temp)) #找最小权值的节点的坐标
        temp[i]=inf
        for j in range(n):
            if j not in visited:
                if (dis[i]+ matr[i][j])<dis[j]:
                    dis[j] = temp[j] =dis[i]+ matr[i][j]
                    parent[j]=i  #说明父节点是i
        visited.append(i)  #该索引已经处理了
        path=[]  #用于画路径
        path.append(str(i))
        k=i
        while(parent[k]!=start):  #找该节点的父节点添加到path，直到父节点是start
            path.append(str(parent[k]))
            k=parent[k]
        path.append(str(start))
        path.reverse()   #path反序产生路径
        print(str(i)+':','->'.join(path))  #打印路径
    return dis
a=[[0,1,2,inf,7,inf,4,8],[1,0,2,3,inf,inf,inf,7],
  [2,2,0,1,5,inf,inf,inf],[inf,3,1,0,3,6,inf,inf],
  [7,inf,5,3,0,4,3,inf],[inf,inf,inf,6,4,0,6,4],
  [4,inf,inf,inf,3,6,0,2],[8,7,inf,inf,inf,4,2,0]]
d=Dijkstra_all_minpath(a,3)
print("v3到所有顶点的最短距离为：",d)
````

</details>

##### 变体 2：mydijkstra1.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：优先调用 `Dijkstra_all_minpath`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1d77c33136edc868b154899c1b14f20a3d07dbf2a9fe781d783218a8f48f53b4`
- 语言：Python
- 符号：`Dijkstra_all_minpath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/mydijkstra1.py`

<details>
<summary>展开原始代码</summary>

````python
import numpy as np
inf=np.inf
def Dijkstra_all_minpath(matrix,start):
    n=len(matrix)#该图的节点数
    path_array=[]
    temp_array=[]
    path_array.extend(matrix[start])#深复制
    temp_array.extend(matrix[start])#深复制
    temp_array[start] = inf#临时数组会把处理过的节点的值变成inf，表示不是最小权值的节点了
    visited=[start]#start已处理
    path_parent=[start]*n#用于画路径，记录此路径中该节点的父节点
    while(len(visited)<n):
        i= temp_array.index(min(temp_array))#找最小权值的节点的坐标
        temp_array[i]=inf
        path=[]#用于画路径
        path.append(str(i))
        k=i
        while(path_parent[k]!=start):#找该节点的父节点添加到path，直到父节点是start
            path.append(str(path_parent[k]))
            k=path_parent[k]
        path.append(str(start))
        path.reverse()#path反序产生路径
        print(str(i)+':','->'.join(path))#打印路径
        visited.append(i)#该索引已经处理了
        for j in range(n):#这个不用多说了吧
            if j not in visited:
                if (path_array[i]+matrix[i][j])<path_array[j]:
                    path_array[j] = temp_array[j] =path_array[i]+matrix[i][j]
                    path_parent[j]=i#说明父节点是i
    return path_array
 
#领接矩阵
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]

print(Dijkstra_all_minpath(a,0))
````

</details>

##### 变体 3：mydijkstra2.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：优先调用 `Dijkstra_all_minpath`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`bb28c07321620d5025b89af520208167f3377eefae7561f3e1e98a7629237c32`
- 语言：Python
- 符号：`Dijkstra_all_minpath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/mydijkstra2.py`

<details>
<summary>展开原始代码</summary>

````python
import numpy as np
inf=np.inf
def Dijkstra_all_minpath(matrix,start):
    n=len(matrix)#该图的节点数
    path_array=[]
    temp=[]
    path_array.extend(matrix[start])  #深复制
    temp.extend(matrix[start])        #深复制
    temp[start] = inf  #临时数组会把处理过的节点的值变成inf，表示不是最小权值的节点了
    visited=[start]  #start已处理
    parent=[start]*n   #用于画路径，记录此路径中该节点的父节点
    while(len(visited)<n):
        i= temp.index(min(temp)) #找最小权值的节点的坐标
        temp[i]=inf
        path=[]  #用于画路径
        path.append(str(i))
        k=i
        while(parent[k]!=start):  #找该节点的父节点添加到path，直到父节点是start
            path.append(str(parent[k]))
            k=parent[k]
        path.append(str(start))
        path.reverse()   #path反序产生路径
        print(str(i)+':','->'.join(path))  #打印路径
        visited.append(i)  #该索引已经处理了
        for j in range(n):
            if j not in visited:
                if (path_array[i]+matrix[i][j])<path_array[j]:
                    path_array[j] = temp[j] =path_array[i]+matrix[i][j]
                    parent[j]=i  #说明父节点是i
    return path_array
 
#领接矩阵
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]

d=Dijkstra_all_minpath(a,0)
print("计算结果为：\n")
print(d)
````

</details>

##### 变体 4：mydijkstra3.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：优先调用 `Dijkstra_all_minpath`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0af3a29dcb895b3cf0a510fd61aa4247528f9b1f5ac49e07349773744675b293`
- 语言：Python
- 符号：`Dijkstra_all_minpath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/mydijkstra3.py`

<details>
<summary>展开原始代码</summary>

````python
import numpy as np
inf=np.inf
def Dijkstra_all_minpath(matrix,start):
    n=len(matrix)#该图的节点数
    dis=[]; temp=[]
    dis.extend(matrix[start])  #深复制
    temp.extend(matrix[start])        #深复制
    temp[start] = inf  #临时数组会把处理过的节点的值变成inf，表示不是最小权值的节点了
    visited=[start]  #start已处理
    parent=[start]*n   #用于画路径，记录此路径中该节点的父节点
    while len(visited)<n:
        i= temp.index(min(temp)) #找最小权值的节点的坐标
        temp[i]=inf
        path=[]  #用于画路径
        path.append(str(i))
        k=i
        while(parent[k]!=start):  #找该节点的父节点添加到path，直到父节点是start
            path.append(str(parent[k]))
            k=parent[k]
        path.append(str(start))
        path.reverse()   #path反序产生路径
        print(str(i)+':','->'.join(path))  #打印路径
        visited.append(i)  #该索引已经处理了
        for j in range(n):
            if j not in visited:
                if (dis[i]+matrix[i][j])<dis[j]:
                    dis[j] = temp[j] =dis[i]+matrix[i][j]
                    parent[j]=i  #说明父节点是i
    return dis
 
#领接矩阵
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]

d=Dijkstra_all_minpath(a,0)
print("计算结果为：\n")
print(d)
````

</details>

##### 变体 5：mydijkstra4.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：优先调用 `Dijkstra_all_minpath`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`41e0ba0d0b1381e01f0908279f5de9cc1469bddb8d25b3efd9d47889d525d3a1`
- 语言：Python
- 符号：`Dijkstra_all_minpath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/mydijkstra4.py`

<details>
<summary>展开原始代码</summary>

````python
import numpy as np
inf=np.inf
def Dijkstra_all_minpath(matrix,start):
    n=len(matrix)#该图的节点数
    dis=[]; temp=[]
    dis.extend(matrix[start])  #深复制
    temp.extend(matrix[start])        #深复制
    temp[start] = inf  #临时数组会把处理过的节点的值变成inf，表示不是最小权值的节点了
    visited=[start]  #start已处理
    parent=[start]*n   #用于画路径，记录此路径中该节点的父节点
    while len(visited)<n:
        i= temp.index(min(temp)) #找最小权值的节点的坐标
        temp[i]=inf
        for j in range(n):
            if j not in visited:
                if (dis[i]+matrix[i][j])<dis[j]:
                    dis[j] = temp[j] =dis[i]+matrix[i][j]
                    parent[j]=i  #说明父节点是i
        path=[]  #用于画路径
        path.append(str(i))
        k=i
        while(parent[k]!=start):  #找该节点的父节点添加到path，直到父节点是start
            path.append(str(parent[k]))
            k=parent[k]
        path.append(str(start))
        path.reverse()   #path反序产生路径
        print(str(i)+':','->'.join(path))  #打印路径
        visited.append(i)  #该索引已经处理了
    return dis
 
#领接矩阵
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]

d=Dijkstra_all_minpath(a,0)
print("计算结果为：\n")
print(d)
````

</details>

##### 变体 6：mydijkstra5.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：优先调用 `Dijkstra_all_minpath`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0be3f35939c4cd113d18ed747f391b229b15c319ef30338fac20a0537f7ace49`
- 语言：Python
- 符号：`Dijkstra_all_minpath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/mydijkstra5.py`

<details>
<summary>展开原始代码</summary>

````python
import numpy as np
inf=np.inf
def Dijkstra_all_minpath(matrix,start):
    n=len(matrix)#该图的节点数
    dis=[]; temp=[]
    dis.extend(matrix[start])  #深复制
    temp.extend(matrix[start]) #深复制
    temp[start] = inf  #临时数组会把处理过的节点的值变成inf，表示不是最小权值的节点了
    visited=[start]  #start已处理
    parent=[start]*n   #用于画路径，记录此路径中该节点的父节点
    while len(visited)<n:
        i= temp.index(min(temp)) #找最小权值的节点的坐标
        temp[i]=inf
        for j in range(n):
            if j not in visited:
                if (dis[i]+matrix[i][j])<dis[j]:
                    dis[j] = temp[j] =dis[i]+matrix[i][j]
                    parent[j]=i  #说明父节点是i
        visited.append(i)  #该索引已经处理了
        path=[]  #用于画路径
        path.append(str(i))
        k=i
        while(parent[k]!=start):  #找该节点的父节点添加到path，直到父节点是start
            path.append(str(parent[k]))
            k=parent[k]
        path.append(str(start))
        path.reverse()   #path反序产生路径
        print(str(i)+':','->'.join(path))  #打印路径
    return dis
 
#领接矩阵
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]
d=Dijkstra_all_minpath(a,0)
print("计算结果为：\n")
print(d)
````

</details>

##### 变体 7：mydijkstra6.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：优先调用 `Dijkstra_all_minpath`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`953cae0079bdaaff4a33d651774d0ef51d4a949f2a963d78e223fccc9fc7040f`
- 语言：Python
- 符号：`Dijkstra_all_minpath`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/mydijkstra6.py`

<details>
<summary>展开原始代码</summary>

````python
import numpy as np
inf=np.inf
def Dijkstra_all_minpath( mat,start): #mat为邻接矩阵，start表示起点
    n=len( mat)#该图的节点数
    dis=[]; temp=[]
    dis.extend(mat[start])  #添加矩阵mat的start行元素
    temp.extend(mat[start]) #添加矩阵mat的start行元素
    temp[start] = inf  #临时数组会把处理过的节点的值变成inf
    visited=[start]  #start已处理
    parent=[start]*n   #用于画路径，记录此路径中该节点的父节点
    while len(visited)<n:
        i= temp.index(min(temp)) #找最小权值的节点的坐标
        temp[i]=inf
        for j in range(n):
            if j not in visited:
                if (dis[i]+ mat[i][j])<dis[j]:
                    dis[j] = temp[j] =dis[i]+ mat[i][j]
                    parent[j]=i  #说明父节点是i
        visited.append(i)  #该索引已经处理了
        path=[]  #用于画路径
        path.append(str(i))
        k=i
        while(parent[k]!=start):  #找该节点的父节点添加到path，直到父节点是start
            path.append(str(parent[k]))
            k=parent[k]
        path.append(str(start))
        path.reverse()   #path反序产生路径
        print(str(i)+':','->'.join(path))  #打印路径
    return dis

a=[[0,1,2,inf,7,inf,4,8],[1,0,2,3,inf,inf,inf,7],
            [2,2,0,1,5,inf,inf,inf],[inf,3,1,0,3,6,inf,inf],
            [7,inf,5,3,0,4,3,inf],[inf,inf,inf,6,4,0,6,4],
            [4,inf,inf,inf,3,6,0,2],[8,7,inf,inf,inf,4,2,0]]
d=Dijkstra_all_minpath(a,3)
print("所求最短距离为：",d)
````

</details>

#### Pex10_6 · Python · 9fd8e07e

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`7f22b0e8abea56e9b3fdb4d04a7af3fa7eef2106c91b81be07cefed289bd658c`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_6.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_6.py
import numpy as np
import networkx as nx
List=[(0,1,1),(0,2,2),(0,4,7),(0,6,4),(0,7,8),(1,2,2),(1,3,3),
      (1,7,7),(2,3,1),(2,4,5),(3,4,3),(3,5,6),(4,5,4),(4,6,3),
      (5,6,6),(5,7,4),(6,7,2)]
G=nx.Graph()
G.add_weighted_edges_from(List)
A=nx.to_numpy_matrix(G, nodelist=range(8))  #导出邻接矩阵
np.savetxt('Pdata10_6.txt',A)
p=nx.dijkstra_path(G, source=3, target=7, weight='weight')  #求最短路径；
d=nx.dijkstra_path_length(G, 3, 7, weight='weight') #求最短距离
print("最短路径为：",p,"；最短距离为：",d)
````

</details>

#### Pex10_8 · Python · f6b8863f

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`bf802d869de04295f6ed5ed1f3d20a90b1f4fa73f011435c67b4514f6c2812d0`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_8.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_8.py
import numpy as np
import networkx as nx
a=np.loadtxt("Pdata10_6.txt")
G=nx.Graph(a)     #利用邻接矩阵构造赋权无向图
d=nx.shortest_path_length(G,weight='weight')  #返回值是可迭代类型
Ld=dict(d)  #转换为字典类型
print("顶点对之间的距离为：",Ld)  #显示所有顶点对之间的最短距离
print("顶点0到顶点4的最短距离为:",Ld[0][4])  #显示一对顶点之间的最短距离
m,n=a.shape; dd=np.zeros((m,n))
for i in range(m):
    for j in range(n): dd[i,j]=Ld[i][j]
print("顶点对之间最短距离的数组表示为：\n",dd)  #显示所有顶点对之间最短距离
np.savetxt('Pdata10_8.txt',dd) #把最短距离数组保存到文本文件中
p=nx.shortest_path(G, weight='weight')  #返回值是可迭代类型
dp=dict(p)  #转换为字典类型
print("\n顶点对之间的最短路径为：", dp)
print("顶点0到顶点4的最短路径为：",dp[0][4])
````

</details>

#### Pex10_9 · Python · fb6cca49

- 归属算法：图论与排队
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#图论与排队 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于图论与排队中的“核心算法与辅助函数”。
- **执行主线**：通过松弛操作求单源最短路径。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`35ab5b315e39b20817502c5f39b8459aaa46d2f8b01edbcb2a2f71b38f355d3e`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_9.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_9.py
import numpy as np
import networkx as nx
import pylab as plt
p=[25,26,28,31]; a=[10,14,18,26]; r=[20,16,13,11];
b=np.zeros((5,5)); #邻接矩阵（非数学上的邻接矩阵）初始化
for i in range(5):
    for j in range(i+1,5):
        b[i,j]=p[i]+np.sum(a[0:j-i])-r[j-i-1];
print(b)
G=nx.DiGraph(b)
p=nx.dijkstra_path(G, source=0, target=4, weight='weight')  #求最短路径；
print("最短路径为:",np.array(p)+1)  #python下标从0开始
d=nx.dijkstra_path_length(G, 0, 4, weight='weight') #求最短距离
print("所求的费用最小值为：",d)
s=dict(zip(range(5),range(1,6))) #构造用于顶点标注的标号字典
plt.rc('font',size=16)
pos=nx.shell_layout(G)  #设置布局
w=nx.get_edge_attributes(G,'weight')
nx.draw(G,pos,font_weight='bold',labels=s,node_color='r')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
path_edges=list(zip(p,p[1:]))
nx.draw_networkx_edges(G,pos,edgelist=path_edges,
            edge_color='r',width=3)
plt.savefig("figure10_9.png",pdi=500); plt.show()
````

</details>

### 最小生成树 · 实现

#### ex4_12 · MATLAB · ac643fc2

- 归属算法：最小生成树
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#最小生成树 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于最小生成树中的“核心算法与辅助函数”。
- **执行主线**：选择低权边构造最小生成树。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：使用旧版接口，运行前检查当前软件兼容性。

- SHA-256：`3b070788ab9cc97672ec5ebcb250fce9693b3f01a01458d2c87bff7ed45b0833`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_12.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
x=[0     5    16    20    33    23    35    25    10];
y=[15    20    24    20    25    11     7     0     3];
xy=[x;y];
d=mandist(xy); %求xy的两两列向量间的绝对值距离
d=tril(d); %截取matlab工具箱要求的下三角矩阵
b=sparse(d) %转化为稀疏矩阵
[ST,pred]=graphminspantree(b,'Method','Kruskal')  %调用最小生成树的命令
st=full(ST); %把最小生成树的稀疏矩阵转化成普通矩阵
TreeLength=sum(sum(st))  %求最小生成树的长度
view(biograph(ST,[],'ShowArrows','off','ShowWeights','on')) %画出最小生成树
````

</details>

#### 中国数学建模-编程交流-贪婪算法_2 · MATLAB · cf419820

- 归属算法：最小生成树
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#最小生成树 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于最小生成树中的“结果绘图与展示”。
- **执行主线**：选择低权边构造最小生成树；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`016d25be5fb8343a1f43ffb6326ebc252405317afc7b1a04792baab42c280b5e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/贪婪算法/中国数学建模-编程交流-贪婪算法_2.txt`

<details>
<summary>展开原始代码</summary>

````matlab
中国数学建模-编程交流-贪婪算法  ├数学思想
  ├编程交流
  ├学术杂谈
  ├English Fans

        wh-ee 重登录  隐身  用户控制面板  搜索  风格  论坛状态  论坛展区  社区服务  社区休闲  网站首页  退出 

      >> VC++,C,Perl,Asp...编程学习,算法介绍.  我的收件箱 (0) 
       中国数学建模 → 学术区 → 编程交流 → 贪婪算法 

             您是本帖的第 890 个阅读者       
             * 贴子主题：贪婪算法           

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 11 楼 



               

              1.3.6 最小耗费生成树
              在例1 - 2及1 - 3中已考察过这个问题。因为具有n 
              个顶点的无向网络G的每个生成树刚好具有n-1条边，所以问题是用某种方法选择n-1条边使它们形成G的最小生成树。至少可以采用三种不同的贪婪策略来选择这n-1条边。这三种求解最小生成树的贪婪算法策略是： 
              K r u s k a l算法，P r i m算法和S o l l i n算法。
              1. Kruskal算法
              (1) 算法思想
              K r u s k a l算法每次选择n- 
              1条边，所使用的贪婪准则是：从剩下的边中选择一条不会产生环路的具有最小耗费的边加入已选择的边的集合中。注意到所选取的边若产生环路则不可能形成一棵生成树。K 
              r u s k a l算法分e 步，其中e 是网络中边的数目。按耗费递增的顺序来考虑这e 
              条边，每次考虑一条边。当考虑某条边时，若将其加入到已选边的集合中会出现环路，则将其抛弃，否则，将它选入。
              考察图1-12a 中的网络。初始时没有任何边被选择。图13-12b 显示了各节点的当前状态。边（ 1 , 
              6）是最先选入的边，它被加入到欲构建的生成树中，得到图1 3 - 1 2 c。下一步选择边（ 3，4）并将其加入树中（如图1 3 - 
              1 2 d所示）。然后考虑边( 2，7 )，将它加入树中并不会产生环路，于是便得到图1 3 - 1 2 e。下一步考虑边（ 
              2，3）并将其加入树中（如图1 3 - 1 2 
              f所示）。在其余还未考虑的边中，（7，4）具有最小耗费，因此先考虑它，将它加入正在创建的树中会产生环路，所以将其丢弃。此后将边（ 
              5，4）加入树中，得到的树如图13-12g 所示。下一步考虑边（ 7，5），由于会产生环路，将其丢弃。最后考虑边（ 
              6，5）并将其加入树中，产生了一棵生成树，其耗费为9 9。图1 - 1 3给出了K r u s k a l算法的伪代码。
              / /在一个具有n 个顶点的网络中找到一棵最小生成树
              令T为所选边的集合，初始化T=
              令E 为网络中边的集合
              w h i l e(E≠ )&&(| T |≠n- 1 ) {
              令(u,v)为E中代价最小的边
              E=E- { (u,v) } / /从E中删除边
              i f( (u,v)加入T中不会产生环路)将（ u,v）加入T
              }
              i f(| T | = =n-1) T是最小耗费生成树
              e l s e 网络不是互连的，不能找到生成树
              图13-13 Kruskao算法的伪代码
              (2) 正确性证明
              利用前述装载问题所用的转化技术可以证明图1 3 - 1 3的贪婪算法总能建立一棵最小耗费生成树。需要证明以下两点： 1) 
              只要存在生成树，K r u s k a l算法总能产生一棵生成树； 2) 
              产生的生成树具有最小耗费。令G为任意加权无向图（即G是一个无向网络）。从1 2 . 11 . 
              3节可知当且仅当一个无向图连通时它有生成树。而且在Kruskal 
              算法中被拒绝（丢弃）的边是那些会产生环路的边。删除连通图环路中的一条边所形成的图仍是连通图，因此如果G在开始时是连通的，则T与E中的边总能形成一个连通图。也就是若G开始时是连通的，算法不会终止于E= 
              和| T |< n- 1。
              现在来证明所建立的生成树T具有最小耗费。由于G具有有限棵生成树，所以它至少具有一棵最小生成树。令U为这样的一棵最小生成树， 
              T与U都刚好有n- 1条边。如果T=U, 则T就具有最小耗费，那么不必再证明下去。因此假设T≠U，令k(k >0) 
              为在T中而不在U中的边的个数，当然k 也是在U中而不在T中的边的数目。
              通过把U变换为T来证明U与T具有相同的耗费，这种转化可在k 
              步内完成。每一步使在T而不在U中的边的数目刚好减1。而且U的耗费不会因为转化而改变。经过k 
              步的转化得到的U将与原来的U具有相同的耗费，且转化后U中的边就是T中的边。由此可知， T具有最小耗费。每步转化包括从T中移一条边e 
              到U中，并从U中移出一条边f。边e 与f 的选取按如下方式进行：
              1) 令e 是在T中而不在U中的具有最小耗费的边。由于k >0，这条边肯定存在。
              2) 当把e 加入U时，则会形成唯一的一条环路。令f 为这条环路上不在T中的任意一条边。
              由于T中不含环路，因此所形成的环路中至少有一条边不在T中。
              从e 与f 的选择方法中可以看出， V=U+ {e} -{ f } 是一棵生成树，且T中恰有k- 
              1条边不在V中出现。现在来证明V的耗费与U的相同。显然，V的耗费等于U的耗费加上边e 的耗费再减去边f 的耗费。若e 的耗费比f 
              的小，则生成树V的耗费比U的耗费小，这是不可能的。如果e 的耗费高于f，在K r u s k a l算法中f 会在e 
              之前被考虑。由于f 不在T中，Kruskal 算法在考虑f 能否加入T时已将f 丢弃，因此f 和T中耗费小于或等于f 
              的边共同形成环路。通过选择e，所有这些边均在U中，因此U肯定含有环路，但是实际上这不可能，因为U是一棵生成树。e 的代价高于f 
              的假设将会导致矛盾。剩下的唯一的可能是e 与f 具有相同的耗费，由此可知V与U的耗费相同。
              (3) 数据结构的选择及复杂性分析
              为了按耗费非递减的顺序选择边，可以建立最小堆并根据需要从堆中一条一条地取出各边。当图中有e 条边时，需花(e) 的时间初始化堆及O 
              ( l o ge) 的时间来选取每一条边。边的集合T与G中的顶点一起定义了一个由至多n 
              个连通子图构成的图。用顶点集合来描述每个子图，这些顶点集合没有公共顶点。为了确定边（ u,v）是否会产生环路，仅需检查u,v 
              是否在同一个顶点集中（即处于同一子图）。如果是，则会形成一个环路；如果不是，则不会产生环路。因此对于顶点集使用两个F i n 
              d操作就足够了。当一条边包含在T中时，2个子图将被合并成一个子图，即对两个集合执行U n i o n操作。集合的F i n d和U 
              n i o n操作可利用8 . 1 0 . 2节的树（以及加权规则和路径压缩）来高效地执行。F i n d操作的次数最多为2e，Un 
              i o n操作的次数最多为n- 1（若网络是连通的，则刚好是n- 1次）。加上树的初始化时间，算法中这部分的复杂性只比O (n+e) 
              稍大一点。
              对集合T所执行的唯一操作是向T中添加一条新边。T可用数组t 来实现。添加操作在数组
              的一端进行，因为最多可在T中加入n- 1条边，因此对T的操作总时间为O (n)。
              总结上述各个部分的执行时间，可得图1 3 - 1 3算法的渐进复杂性为O (n+el o ge)。
              (4) 实现
              利用上述数据结构，图1 - 1 3可用C + +代码来实现。首先定义E d g e N o d e类（见程序1 3 - 6 
              )，它是最小堆的元素及生成树数组t 的数据类型


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:42:37       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 12 楼 



               

              程序13-6 Kruskal算法所需要的数据类型
              template <class T>
              class EdgeNode {
              p u b l i c :
              operator T() const {return weight;}
              p r i v a t e :
              T weight;//边的高度
              int u, v;//边的端点
              } ;
              为了更简单地使用8 . 1 0 . 2节的查找和合并策略，定义了U n i o n F i n d类，它的构造函数是程序8 - 1 
              6的初始化函数，U n i o n是程序8 - 1 6的加权合并函数，F i n d是程序8 - 1 7的路径压缩搜索函数。
              为了编写与网络描述无关的代码，还定义了一个新的类U N e t Wo r k，它包含了应用于无向网络的所有函数。这个类与U n d 
              i r e c t e d类的差别在于U n d i r e c t e d类中的函数不要求加权边，而U N e t Wo r 
              k要求边必须带有权值。U N e t Wo r k中的成员需要利用N e t w o r k类中定义的诸如B e g i n和N e 
              x t Ve r t e 
              x的遍历函数。不过，新的遍历函数不仅需要返回下一个邻接的顶点，而且要返回到达这个顶点的边的权值。这些遍历函数以及有向和无向加权网络的其他函数一起构成了W 
              N e t w o r k类（见程序1 3 - 7）。
              程序13-7 WNetwork类
              template<class T>
              class WNetwork : virtual public Network
              {
              public :
              virtual void First(int i, int& j, T& c)=0;
              virtual void Next(int i, int& j, T& c)=0;
              } ;
              象B e g i n和N e x t Ve r t e x一样，可在A d j a c e n c y W D i g r a p 
              h及L i n k e d W D i g r a p h类中加入函数F i r s t与N e x t。现在A d j a c e 
              n c y W D i g r a p h及L i n k e d W D i g r a p h类都需要从W N e t Wo r 
              k中派生而来。由于A d j a c e n c y W G r a p h类和L i n k e d W G r a p 
              h类需要访问U N e t w o r k的成员，所以这两个类还必须从U N e t Wo r k中派生而来。U N e t Wo 
              r k : : K r u s k a l的代码见程序1 3 - 8，它要求将Edges() 定义为N e t Work 
              类的虚成员，并且把U N e t Wo r k定义为E d g e N o d e的友元）。如果没有生成树，函数返回f a l s 
              e，否则返回t r u e。注意当返回true 时，在数组t 中返回最小耗费生成树。
              程序13-8 Kr u s k a l算法的C + +代码
              template<class T>
              bool UNetwork<T>::Kruskal(EdgeNode<T> t[])
              {// 使用K r u s k a l算法寻找最小耗费生成树
              // 如果不连通则返回false
              // 如果连通，则在t [ 0 : n - 2 ]中返回最小生成树
              int n = Ve r t i c e s ( ) ;
              int e = Edges();
              / /设置网络边的数组
              InitializePos(); // 图遍历器
              EdgeNode<T> *E = new EdgeNode<T> [e+1];
              int k = 0; // E的游标
              for (int i = 1; i <= n; i++) { // 使所有边附属于i
              int j;
              T c;
              First(i, j, c);
              while (j) { // j 邻接自i
              if (i < j) {// 添加到达E的边
              E[++k].weight = c;
              E[k].u = i;
              E[k].v = j;}
              Next(i, j, c);
              }
              }
              // 把边放入最小堆
              MinHeap<EdgeNode<T> > H(1);
              H.Initialize(E, e, e);
              UnionFind U(n); // 合并/搜索结构
              // 根据耗费的次序来抽取边
              k = 0; // 此时作为t的游标
              while (e && k < n - 1) {
              // 生成树未完成，尚有剩余边
              EdgeNode<T> x;
              H.DeleteMin(x); // 最小耗费边
              e - - ;
              int a = U.Find(x.u);
              int b = U.Find(x.v);
              if (a != b) {// 选择边
              t[k++] = x;
              U . U n i o n ( a , b ) ; }
              }
              D e a c t i v a t e P o s ( ) ;
              H . D e a c t i v a t e ( ) ;
              return (k == n - 1);
              }
              2. Prim算法
              与Kr u s k a l算法类似，P r i 
              m算法通过每次选择多条边来创建最小生成树。选择下一条边的贪婪准则是：从剩余的边中，选择一条耗费最小的边，并且它的加入应使所有入选的边仍是一棵树。最终，在所有步骤中选择的边形成一棵树。相反，在Kruskal 
              算法中所有入选的边集合最终形成一个森林。
              P r i m算法从具有一个单一顶点的树T开始，这个顶点可以是原图中任意一个顶点。然后往T中加入一条代价最小的边（ u , 
              v）使T&Egrave;{ (u , v) }仍是一棵树，这种加边的步骤反复循环直到T中包含n- 1条边。注意对于边（ u , v），u、v 
              中正好有一个顶点位于T中。P r i m算法的伪代码如图1 -1 
              4所示。在伪代码中也包含了所输入的图不是连通图的可能，在这种情况下没有生成树。图1 - 1 5显示了对图1-12a 使用P r i 
              m算法的过程。把图1 - 1 4的伪代码细化为C + +程序及其正确性的证明留作练习（练习3 1）。
              / /假设网络中至少具有一个顶点
              设T为所选择的边的集合，初始化T=
              设T V为已在树中的顶点的集合，置T V= { 1 }
              令E为网络中边的集合
              w h i l e(E< > ) & & (| T | < > n-1) {
              令（u , v）为最小代价边，其中u T V, v T V
              i f（没有这种边） b re a k
              E=E- { (u,v) } / /从E中删除此边
              在T中加入边（ u , v）
              }
              if (| T | = =n- 1 ) T是一棵最小生成树
              else 网络是不连通的，没有最小生成树
              图13-14 Prim最小生成树算法
              如果根据每个不在T V中的顶点v 选择一个顶点n e ar (v)，使得n e ar (v) &Icirc; TV 且c o st (v, n 
              e ar (v) )的值是所有这样的n e ar (v) 节点中最小的，则实现P r i m算法的时间复杂性为O (n2 
              )。下一条添加到T中的边是这样的边：其cost (v, near (v)) 最小，且v T V。
              3. Sollin算法
              S o l l i 
              n算法每步选择若干条边。在每步开始时，所选择的边及图中的n个顶点形成一个生成树的森林。在每一步中为森林中的每棵树选择一条边，这条边刚好有一个顶点在树中且边的代价最小。将所选择的边加入要创建的生成树中。注意一个森林中的两棵树可选择同一条边，因此必须多次复制同一条边。当有多条边具有相同的耗费时，两棵树可选择与它们相连的不同的边，在这种情况下，必须丢弃其中的一条边。开始时，所选择的边的集合为空。若某一步结束时仅剩下一棵树或没有剩余的边可供选择时算法终止。
              图1 - 6给出了初始状态为图1-12a 时，使用S o l l i n算法的步骤。初始入选边数为0时的情形如图13-12a 
              时,森林中的每棵树均是单个顶点。顶点1，2，.，7所选择的边分别是(1.6), (2,7),(3,4), (4,3), (5,4), 
              (6,1), (7,2)，其中不同的边是( 1 , 6 )，( 2 , 7 )，(3,4) 和( 5 , 4 
              )，将这些边加入入选边的集合后所得到的结果如图1 3 - 1 6 a所示。下一步具有顶点集{ 1 , 6 }的树选择边( 6 , 5 
              )，剩下的两棵树选择边( 2 , 3 )，加入这两条边后已形成一棵生成树，构建好的生成树见图1 3 - 6 b。S o l l i 
              n算法的C + +程序实现及其正确性证明留作练习（练习3 2 )。


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:42:54       

              b  
        
        
        等级：职业侠客 
        文章：470
        积分：956
        门派：黑客帝国 
        注册：2003-8-28
                        第 13 楼 



               

              练习
              8. 针对装载问题，扩充贪婪算法，考虑有两条船的情况，算法总能产生最优解吗？
              9. 已知n 个任务的执行序列。假设任务i 需要ti 个时间单位。若任务完成的顺序为1，2，.，n，则任务i 完成的时间为ci =i 
              &aring;j = 1tj 。任务的平均完成时间（Av e rge Completion Time, ACT）
              为1–nn &aring;i = 1ci 。
              1) 考虑有四个任务的情况，每个任务所需时间分别是（ 4，2，8，1）。若任务的顺序为1，2，3，4，则A C T是多少？
              2) 若任务顺序为2，1，4，3，则A C T是多少？
              3) 创建具有最小A C T的任务序列的贪婪算法分n 步来构造该任务序列，在每一步中，从剩下的任务里选择时间最小的任务。对于1 
              )，利用这种策略获得的任务顺序为4，2，1，3，这种顺序的A C T是多少？
              4) 写一个C + +程序实现3) 中的贪婪策略，程序的复杂性应为O (nl o gn)，试证明之。
              5) 证明利用3) 中的贪婪算法获得的任务顺序具有最小的A C T。
              10. 若有两个工人执行练习9中的n个任务，需将任务分配给他们，同时他们具有自己的任务执行顺序。任务完成时间及A C 
              T的定义同练习9。使A C 
              T最小化的一种可行的贪婪算法是：两个工人轮流选择任务，每次从剩余的任务中选择时间最小的任务。每个人按照自己所选任务的顺序执行任务。对于练习9中的例子，假定工人1首先选择任务4，然后工人2选择任务2，工人1选择任务1，最后工人2选择任务3。
              1) 利用C + +程序实现这种策略，其时间复杂性为多少？
              2) 上述的贪婪策略总能获得最小的A C T吗？证明结论。
              11. 1) 考虑有m 个人可以执行任务，扩充练习1 0中的贪婪算法。
              2) 算法能保证获得最优解吗？证明结论。
              3) 用C + +程序实现此算法，其复杂性是多少？
              12. 考虑例4 - 4的堆栈折叠问题。
              1) 设计一个贪婪算法，将堆栈折叠为最小数目的子堆栈，使得每个子堆栈的高度均不超过H。
              2) 算法总能保证得到数目最少的子堆栈吗？证明结论。
              3) 用C + +代码实现1) 的算法。
              4) 代码的时间复杂性是多少？
              13. 编写C + +程序实现0 / 1背包问题，使用如下启发式方法：按价值密度非递减的顺序打包。
              14. 根据k= 1的性能受限启发式方法编写一个C + +程序来实现0 / 1背包问题。
              15. 对于k= 1的情况证明用性能受限的启发式方法求解0 / 1背包问题会发生边界错误。
              16. 根据k= 2的性能受限启发式方法编写一个C + +程序来实现0 / 1背包问题。
              17. 考虑0≤xi ≤1而不是xi &Icirc;{ 0 , 1 
              }的连续背包问题。一种可行的贪婪策略是：按价值密度非递减的顺序检查物品，若剩余容量能容下正在考察的物品，将其装入；否则，往背包中装入此物品的一部分。
              1) 对于n=3, w=[100,10,10], p= [ 2 0 , 1 5 , 1 5 ]及c= 1 0 5 
              ,上述装入方法获得的结果是什么？
              2) 证明这种贪婪算法总能获得最优解。
              3) 用一个C + +程序实现此算法。
              18. 例1 3 - 1的渴婴问题是练习1 7中连续背包问题的一般化，将练习1 
              7的贪婪算法用于渴婴问题，算法能保证总能得到最优解吗？证明结论。
              19. 1) 证明当且仅当二分图没有覆盖时，图1 3 - 7的算法找不到覆盖。
              2) 给出一个具有覆盖的二分图，使得图1 3 - 7的算法找不到最小覆盖。
              20. 当第一步选择了顶点1时，给出图1 3 - 7的工作过程。
              21. 
              对于二分图覆盖问题设计另外一种贪婪启发式方法，可使用如下贪婪准则：如果B中的某一个顶点仅被A中一个顶点覆盖，选择A中这个顶点；否则，从A中选择一个顶点，使得它所覆盖的未被覆盖的顶点数目最多。
              1) 给出这种贪婪算法的伪代码。
              2) 编写一个C + +函数作为U n d i r e c t e d类的成员来实现上述贪婪算法。
              3) 函数的复杂性是多少？
              4) 验证代码的正确性。
              22. 令G为无向图，S为G中顶点的子集，当且仅当S中的任意两个顶点都有一条边相连时，S为完备子图（c l i q u 
              e），完备子图的大小即S中的顶点数目。最大完备子图（ maximum 
              clique）即具有最大项点数目的完备子图。在图中寻找最大完备子图的问题（即最大完备子图问题）是一个N P-复杂问题。
              1) 给出最大完备子图问题的一种可行的贪婪算法及其伪代码。
              2) 给出一个能用1) 中的启发式算法求解最大完备子图的图例，以及不能用该算法求解的一个图例。
              3) 将1) 中的启发式算法实现为Undirected::Clique(int C, int m) 
              共享成员，其中最大完备子图的大小返回到m中，最大完备子图的顶点返回到C中。
              4) 代码的复杂性是多少？
              23. 令G为一无向图，S为G中顶点的子集，当且仅当S中任意两个顶点都无边相连时， S为无关集（independent 
              set）。最大无关集即是顶点数目最多的无关集。在一幅图中寻找最大无关集是一个N P-复杂问题。按练习2 2的要求解决最大无关集问题。
              24. 对无向图G着色的方法是：为G中的顶点编号（{ 1 , 2 
              ,.}），使得由一条边相连的两个顶点具有不同的编号。在图的着色问题中，要求利用最少的相互不同的颜色（编号）来给图G着色。图的着色问题也是一个N 
              P-复杂问题。按练习2 2的要求解决图着色问题。
              25. 证明当按路径长度的顺序产生一条最短路径时，所产生的下一条最短路径总是由已产生的一条最短路径扩充一条边得到。
              26. 证明对于具有一条或多条具有负长度的边，图1 3 - 11的贪婪算法不一定能正确地计算出最短路径的长度。
              27. 编写一个P a t h ( p , s , i )函数，利用函数S h o r t e s t P a t h s计算出的p 
              值，输出从顶点s到顶点i的一条最短路径。函数的复杂性是多少？
              28. 若把有向图作为L i n k e d w D i g r a p h类的一个成员，重写程序1 3 - 
              5，函数应作为该类的一个成员。函数的复杂性是多少？
              29. 若把有向图作为L i n k e d W D i g r a p h类的一个成员且仅有O (n)条边，重写程序1 3 - 
              5，L用最小堆来实现。函数的复杂性是多少？
              30. 从N e t w o r k类（见程序1 2 - 1 5）派生出一个新的模板类D N e t w o r 
              k（有向网络），这个类仅包含应用于有向网络的所有函数。为该类定义一个S h o r t e s t P a t h 
              s函数，使得它与有向网络的描述形式无关，尤其适用于耗费邻接矩阵及邻接链表描述方法。在函数的实现过程中可利用原来的遍历函数，也可根据需要定义新的遍历函数。函数的复杂性应为O 
              (n2 )，其中n 是顶点的数目，试证明之。
              *31. 1) 给出P r i m算法（如图1 3 - 1 4所示）的一种正确性证明。
              2) 将图1 3 - 1 4细化为一个C + +程序U N e t w o r k : : P r i m，其复杂性应为O (n2 
              )。
              3) 证明程序的复杂性确实是O(n2 )。
              *32. 1) 证明对于任意连通无向图，S o l l i n算法总能找到一个最小耗费生成树。
              2) 在S o l l i n算法中，最大的步骤数是多少？试用图中顶点数n 来表示。
              3) 编写一个C + +程序U N e t w o r k : : S o l l i n，使用S o l l i 
              n算法找到一棵最小生成树。
              4) 程序的复杂性是多少？
              *33. 令T为一棵每条边均带有长度的树（不一定是二叉树）。令S为T中顶点的子集，并令T / 
              S为从T中删除S中的顶点所得到的森林。我们希望能找到具有最小走势的子集S，使得T / S中没有从根到叶的距离大于d的森林。
              1) 给出一种寻找最小走势子集S的贪婪算法（提示：从叶节点开始向根移动）。
              2) 证明算法的正确性。
              3) 算法的复杂性是多少？如果它不是T中顶点数的线性函数，则重新设计算法，使其复杂性是线性的。
              *34. 令T / 
              S表示将S中的每个顶点复制两份而获得的森林，其中父节点的指针指向一个复本，而另一复本的指针指向其儿子。针对这种情况再做练习3 3。
              （ 说明：本资料是根据《数据结构、算法与应用》（美，Sartaj  
              Sahni著）一书第13-17章编辑、改写的。考虑到因特网传输速度等因素，大部分插图和公式不得不被删除。对于内容不连贯之处，请网友或读者参阅该书，敬请原谅。 
              ）


              ----------------------------------------------

              plot(100+t+15*cos(3.05*t),t=0..200,coords=polar,axes=none,scaling=constrained); 


       2004-5-27 19:43:19       

              lantian3  
        
        
        等级：新手上路 
        文章：2
        积分：52
        门派：☆nudter☆ 
        注册：2004-6-5
                        第 14 楼 



               

              怎么没人顶？
              我先来
               

       2004-6-5 10:49:29       

              jolin  
        
        
        等级：新手上路 
        文章：28
        积分：179
        注册：2004-3-26
                        第 15 楼 



               

              虽然我还没看，但是还是要顶一顶

       2004-6-5 18:12:35       

              afliboy  
        
        
        头衔：打吗啡的浣熊 
        等级：新手上路 
        文章：4
        积分：84
        门派：桃花岛 
        注册：2004-6-5
                        第 16 楼 



               

              狂顶

       2004-6-5 23:41:53       

              king8egg  
        
        
        等级：新手上路 
        文章：2
        积分：53
        门派：☆nudter☆ 
        注册：2004-6-3
                        第 17 楼 



               

              不错不错,看你发了这么多,不顶不好意思啊,以后有时间再慢慢看吧

       2004-6-6 21:49:31       

              寒枫  
        
        
        等级：新手上路 
        文章：11
        积分：93
        门派：☆nudter☆ 
        注册：2004-6-8
                        第 18 楼 



               

              练习做完了是不是直接跟帖就行？

       2004-6-8 21:15:26       

              lwd1981  
        
        
        等级：新手上路 
        文章：91
        积分：353
        门派：☆nudter☆ 
        注册：2004-8-21
                        第 19 楼 



               
              很好啊！ 

       2004-8-24 20:57:12       

              zouch99  
        
        
        等级：新手上路 
        文章：39
        积分：323
        门派：☆nudter☆ 
        注册：2004-8-10
                        第 20 楼 



               
              好东东 

       2004-8-25 9:29:56       

      本主题贴数 20   分页：9 1 2 :  跳转论坛至...╋数学建模  ├数模竞赛  ├新手入门  ├数学工具  ├资源与检索╋学术区  
        ├数学思想  ├编程交流  ├学术杂谈  ├English Fans╋休闲专区  ├灌水搞笑专区  ├神秘园╋本站站务  ├站务讨论  
        ├数模管理区  ├回收站


       *快速回复：贪婪算法
           发贴表情
                  
                  
                  
                  
                  
                  

               段落格式 普通格式标题 1标题 2标题 3标题 4标题 5标题 6标题 7已编排格式地址  
              字体宋体黑体楷体仿宋隶书幼圆新宋体细明体ArialArial BlackCourierVerdanaWide 
              LatinWingdings  字号1234567              


                      第 1 页,共 7 页， 49 个

       显示签名     内容限制：字节. 


      管理选项： 专题管理 | 修复 | 锁定 | 解锁 | 提升 | 跟贴管理 | 删除 | 移动 | 设置固顶 | 奖励 | 惩罚 | 发布公告 

            Copyright &copy;2002 - 2004 Shumo.Com
            执行时间：156.25000毫秒。查询数据库5次。
            当前模板样式：[默认模板] 
````

</details>

#### Pex10_13 · Python · 4c4628f1

- 归属算法：最小生成树
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#最小生成树 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于最小生成树中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e910b7515dd21db9b8510e8bebe5fd4daccb422ca7f0ebd94d570e6b70eff67f`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_13.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_13.py
import numpy as np
import networkx as nx
import pylab as plt
L=[(1,2,8),(1,3,4),(1,5,2),(2,3,4),(3,4,2),(3,5,1),(4,5,5)]
b=nx.Graph()
b.add_nodes_from(range(1,6))
b.add_weighted_edges_from(L)
T=nx.minimum_spanning_tree(b)  #返回可迭代对象
w=nx.get_edge_attributes(T,'weight') #提取字典数据
TL=sum(w.values())  #计算最小生成树的长度
print("最小生成树为:",w)
print("最小生成树的长度为：",TL)
pos=nx.shell_layout(b)
nx.draw(T,pos,node_size=280,with_labels=True,node_color='r')
nx.draw_networkx_edge_labels(T,pos,edge_labels=w)
plt.show()
````

</details>

#### Pex10_14 · Python · 85c2dd04

- 归属算法：最小生成树
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#最小生成树 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于最小生成树中的“数据读取与预处理”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`d87c95988054860d0695988ae023cc823b6ed9af43066fc16dd135f208c1e04e`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_14.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_14.py
import numpy as np
import networkx as nx
import pandas as pd
import pylab as plt
a=pd.read_excel("Pdata10_14.xlsx",header=None)
b=a.values; b[np.isnan(b)]=0
c=np.zeros((8,8))  #邻接矩阵初始化
c[0:7,1:8]=b  #构造图的邻接矩阵
G=nx.Graph(c)
T=nx.minimum_spanning_tree(G)  #返回可迭代对象
d=nx.to_numpy_matrix(T)  #返回最小生成树的邻接矩阵
print("邻接矩阵c=\n",d)
W=d.sum()/2+5  #求油管长度
print("油管长度W=",W)
s=dict(zip(range(8),range(1,9))) #构造用于顶点标注的标号字典
plt.rc('font',size=16); pos=nx.shell_layout(G)
nx.draw(T,pos,node_size=280,labels=s,node_color='r')
w=nx.get_edge_attributes(T,'weight')
nx.draw_networkx_edge_labels(T,pos,edge_labels=w)
plt.savefig('figure10_14.png'); plt.show()
````

</details>

### 网络流 · 实现

#### mainexample19 · MATLAB · fd75c78f

- 归属算法：网络流
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#网络流 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于网络流中的“核心算法与辅助函数”。
- **执行主线**：在残量网络上计算最大流或最小费用流。
- **调用方式**：优先调用 `mainexample19`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`d6d0f9dd6769daff6eb41cdf0c55b456c64a08842905cfdf240b2c066f5a6e39`
- 语言：MATLAB
- 符号：`mainexample19`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/ZUIXIAOFEI/mainexample19.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/ZUIXIAOFEI/mincostmaxflow.m`

<details>
<summary>展开原始代码</summary>

````matlab
function mainexample19
clear;clc;
global M num
c=zeros(6);u=zeros(6);
c(1,2)=2;c(1,4)=8;c(2,3)=2;c(2,4)=5;
c(3,4)=1;c(3,6)=6;c(4,5)=3;c(5,3)=4;c(5,6)=7;
u(1,2)=8;u(1,4)=7;u(2,3)=9;u(2,4)=5;
u(3,4)=2;u(3,6)=5;u(4,5)=9;u(5,3)=6;u(5,6)=10;
num=size(u,1);M=sum(sum(u))*num^2;
[f,val]=mincostmaxflow(u,c)
````

</details>

#### mincostmaxflow · MATLAB · 94e91832

- 归属算法：网络流
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#网络流 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于网络流中的“核心算法与辅助函数”。
- **执行主线**：用中间节点递推更新全源最短路矩阵；在残量网络上计算最大流或最小费用流。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：函数返回值
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`c14786ab7c524ae0bd43154308048a94c09f8e45d211433dc57c45955b09d090`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/ZUIXIAOFEI/mincostmaxflow.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/ZUIXIAOFEI/floydpath.m`

<details>
<summary>展开原始代码</summary>

````matlab
%最小费用最大流函数
function [flow,val]=mincostmaxflow(rongliang,cost,flowvalue);
%第一个参数：容量矩阵；第二个参数：费用矩阵；
%前两个参数必须在不通路处置零
%第三个参数：指定容量值（可以不写，表示求最小费用最大流）
%返回值flow 为可行流矩阵,val 为最小费用值
global M
flow=zeros(size(rongliang));allflow=sum(flow(1,:));
if nargin<3
flowvalue=M;
end
while allflow<flowvalue
w=(flow<rongliang).*cost-((flow>0).*cost)';
path=floydpath(w);%调用floydpath 函数
if isempty(path)
val=sum(sum(flow.*cost));
return;
end
theta=min(min(path.*(rongliang-flow)+(path.*(rongliang-flow)==0).*M));
theta=min([min(path'.*flow+(path'.*flow==0).*M),theta]);
flow=flow+(rongliang>0).*(path-path').*theta;
allflow=sum(flow(1,:));
end
val=sum(sum(flow.*cost));
````

</details>

#### ex4_8_1 · LINGO · 02d6d81c

- 归属算法：网络流
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#网络流 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于网络流中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1f8066175a491a4e599d8430aed43c259f8c7a8dadce4af14a479c5784ef5620`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_8_1.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

nodes/s,1,2,3,4,t/:d;

arcs(nodes,nodes)/s 1,s 3,1 2,1 3,2 3,2 t,3 4,4 2,4 t/:b,c,f;

endsets

data:

d=14 0 0 0 0 -14;  !最大流为14;

b=2 8 2 5 1 6 3 4 7;

c=8 7 9 5 2 5 9 6 10;

enddata

min=@sum(arcs:b*f);

@for(nodes(i):@sum(arcs(i,j):f(i,j))-@sum(arcs(j,i):f(j,i))=d(i));

@for(arcs:@bnd(0,f,c));

end
````

</details>

#### Pex10_16 · Python · bae89d16

- 归属算法：网络流
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#网络流 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于网络流中的“核心算法与辅助函数”。
- **执行主线**：在残量网络上计算最大流或最小费用流。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`212206c212a56bce3cff819f273769511a53bfc5231a62e92b1fffaf85723dac`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_16.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_16.py
import numpy as np
import networkx as nx
import pylab as plt
L=[(1,2,5),(1,3,3),(2,4,2),(3,2,1),(3,5,4),
   (4,3,1),(4,5,3),(4,6,2),(5,6,5)]
G=nx.DiGraph()
for k in range(len(L)):
    G.add_edge(L[k][0]-1,L[k][1]-1, capacity=L[k][2])
value, flow_dict= nx.maximum_flow(G, 0, 5)
print("最大流的流量为：",value)
print("最大流为：", flow_dict)
n = len(flow_dict)
adj_mat = np.zeros((n, n), dtype=int)
for i, adj in flow_dict.items():
    for j, weight in adj.items():
        adj_mat[i,j] = weight
print("最大流的邻接矩阵为：\n",adj_mat)
ni,nj=np.nonzero(adj_mat)  #非零弧的两端点编号
key=range(n)
s=['v'+str(i+1) for i in range(n)]
s=dict(zip(key,s)) #构造用于顶点标注的字符字典
plt.rc('font',size=16)
pos=nx.shell_layout(G)  #设置布局
w=nx.get_edge_attributes(G,'capacity')
nx.draw(G,pos,font_weight='bold',labels=s,node_color='r')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
path_edges=list(zip(ni,nj))
nx.draw_networkx_edges(G,pos,edgelist=path_edges,
            edge_color='r',width=3)
plt.show()
````

</details>

#### Pex10_17 · Python · a439927b

- 归属算法：网络流
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#网络流 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于网络流中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`273450bed37c5e0232de53b55a5275d9e956ea0534d2b4db17016a08b1328215`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_17.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_17.py
import numpy as np
import networkx as nx
L=[(1,2,5,3),(1,3,3,6),(2,4,2,8),(3,2,1,2),(3,5,4,2),
   (4,3,1,1),(4,5,3,4),(4,6,2,10),(5,6,5,2)]
G=nx.DiGraph()
for k in range(len(L)):
    G.add_edge(L[k][0]-1,L[k][1]-1, capacity=L[k][2], weight=L[k][3])
mincostFlow=nx.max_flow_min_cost(G,0,5)
print("所求流为：",mincostFlow)
mincost=nx.cost_of_flow(G, mincostFlow)
print("最小费用为：", mincost)
flow_mat=np.zeros((6,6),dtype=int)
for i,adj in mincostFlow.items():
    for j,f in adj.items():
        flow_mat[i,j]=f
print("最小费用最大流的邻接矩阵为：\n",flow_mat)
````

</details>

<!-- END AUTO-INTEGRATED-CODE -->
