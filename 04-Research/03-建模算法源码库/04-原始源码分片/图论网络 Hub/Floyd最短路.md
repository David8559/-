---
type: generated-code-shard
status: generated
topic_hub: 图论网络 Hub
algorithm: Floyd最短路
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# Floyd最短路 · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/02-经典建模模型库/04-图论与网络模型/图论网络 Hub|图论网络 Hub]]
- 独立实现：6
- 原始来源：6
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

用动态规划求图中任意两点之间的最短距离。

#### anli4_1_1 · LINGO · 989227cb

- 归属算法：Floyd最短路
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/04-图论与网络模型/图论网络 Hub#Floyd最短路 · 复习|Floyd最短路 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/04-图论与网络模型/图论网络 Hub#Floyd最短路 · 复习|Floyd最短路 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/04-图论与网络模型/图论网络 Hub#Floyd最短路 · 复习|Floyd最短路 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/04-图论与网络模型/图论网络 Hub#Floyd最短路 · 复习|Floyd最短路 · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/04-图论与网络模型/图论网络 Hub#Floyd最短路 · 复习|Floyd最短路 · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
- 复习入口：[[04-Research/02-经典建模模型库/04-图论与网络模型/图论网络 Hub#Floyd最短路 · 复习|Floyd最短路 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

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
