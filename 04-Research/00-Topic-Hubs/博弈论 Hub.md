---
type: topic-hub
topic_tag: topic/博弈论
keywords: [博弈, 纳什均衡, 支付矩阵, 混合策略, 占优策略]
tags: [system/topic-hub, topic/博弈论]
---

# 博弈论 Hub

<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->
## 复习与调用指南

> [!summary] 阅读顺序
> 先用“快速选择”确定算法，再读复习卡掌握思想和步骤，最后跳到实现区选择代码。源码默认折叠；数据明细不在复习页展开。

### 快速选择

| 算法或用途 | 主要解决什么 | 独立实现 | 语言 |
|---|---|---:|---|
| [[#博弈论 · 复习|博弈论]] | 分析多个决策者相互影响下的策略与均衡。 | 36 | LINGO, MATLAB |

### 逐算法复习卡

#### 博弈论 · 复习

- **解决什么**：分析多个决策者相互影响下的策略与均衡。
- **核心思想**：用策略集、支付函数和信息结构刻画互动。
- **标准流程**：识别参与者 → 定义策略与支付 → 判断信息/时序 → 求均衡 → 做稳定性与机制解释。
- **何时调用**：他人策略会改变本方收益时使用，而非普通单主体优化。
- **最易出错**：必须说明合作/非合作、完全/不完全信息以及均衡是否唯一。
- **库内覆盖**：36 个独立实现、36 个原始来源；语言：LINGO, MATLAB；其中 34 个识别到函数/类型入口。
- **优先阅读**：[[#anli3_1 · LINGO · 53499de4|anli3_1]]、[[#ex4_17 · LINGO · b1f5bbac|ex4_17]]、[[#ex4_18 · LINGO · 58b3a1ad|ex4_18]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#博弈论 · 实现|跳转到源码实现区]]

### 通用调用检查表

1. 先确认当前问题是否满足复习卡中的适用条件。
2. 优先选择标有函数/类型入口的实现，脚本型代码先重构参数。
3. 用最小样例跑通，再替换为项目输入；不要一开始就接入完整题目。
4. 检查目标方向、变量单位、边界条件、随机种子和软件版本。
5. 保存运行环境、参数、结果与检验，验证通过后再进入项目正式代码。

<!-- END AUTO-HUB-STUDY-GUIDE -->

> 自动更新：2026-07-14 · 匹配笔记：8

## 相关笔记

- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B078-多人博弈建模思路]] — 相关度 30
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B078-论文拆解]] — 相关度 11
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B108-论文拆解]] — 相关度 10
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/2020-B题-获奖论文横向对比]] — 相关度 9
- [[04-Research/04-竞赛真题研究/01-全国大学生数学建模竞赛/2020-B题-穿越沙漠/2020-B题-穿越沙漠-题目总览]] — 相关度 8
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B125-论文拆解]] — 相关度 4
- [[04-Research/04-竞赛真题研究/03-优秀获奖论文拆解/2020-B题-穿越沙漠/B175-论文拆解]] — 相关度 2
- [[04-Research/03-建模算法源码库/代码资料索引]] — 相关度 1

## 邻接主题

- [[Topic Index]]
- [[优化模型 Hub]]
- [[动态规划 Hub]]
- [[蒙特卡洛 Hub]]

<!-- BEGIN AUTO-INTEGRATED-CODE -->
## 源码实现库（按需调用）

> [!warning] 使用边界
> 以下源码保留全文与来源，但默认均未运行验证。数据依赖明细已从阅读页省略；调用时按代码理解卡完成参数化、最小样例和结果检验。来源显示为可复制路径，不直接调用 Windows 打开未知扩展名。

- 本 Hub 收录原始源码文件：36
- 精确去重后的独立实现：36
- 合并后的实现组：34

### 实现索引

| 算法或用途 | 独立实现 | 原始源码 |
|---|---:|---:|
| [[#博弈论 · 实现|博弈论]] | 36 | 36 |

### 博弈论 · 实现

分析多个决策主体相互影响下的策略、支付与均衡。

#### ex1_2 · LINGO · d9ded703

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`56e054182249e28c480017ff236bb8e7787925e73f831e82c98a9acdec12b305`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/01第1章/ex1_2.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

row/1..2/:b;

col/1..3/:c,x;

links(row,col):a;

endsets

data:

c=2 3 -5;

a=-2 5 -1 1 3 1;

b=-10 12;

enddata

max=@sum(col:c*x);

@for(row(i):@sum(col(j):a(i,j)*x(j))<b(i));

@sum(col:x)=7;

end
````

</details>

#### ex1_5 · LINGO · a3a89c3c

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e7d79e40c8c3a0252b71f68b7aa6cd6539d02f1708325c5d1a3c6976b42cd8c7`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/01第1章/ex1_5.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

col/1..4/:c,x;

row/1..3/:b;

links(row,col):a;

endsets

data:

c=1 2 3 4;

b=-2 -1 -0.5;

a=1 -1 -1 1  1 -1 1 -3  1 -1 -2 3;

enddata

min=@sum(col:c*@abs(x));

@for(row(i):@sum(col(j):a(i,j)*x(j))<b(i));

@for(col:@free(x));  !x的分量可正可负;

       end
````

</details>

#### anli3_1 · LINGO · 53499de4

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`f89f98f458d7adff28a3ec8008957ec53cf2b314beb78dc0f28d7f933b826068`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/03第3章/anli3_1.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

plane/1..6/:delta;

link(plane,plane):alpha,beta;

endsets

data:

alpha=@file('txt1.txt');

beta=@file('txt1.txt');

enddata

min=@sum(plane:@abs(delta));

@for(plane:@bnd(-30,delta,30));

@for(plane(i)|i#le#5:@for(plane(j)| j#ge#i+1: @abs(beta(i,j)+0.5*delta(i)+0.5*delta(j))>alpha(i,j)));

end




	

�����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������

model:

sets:

plane/1..6/:delta;

link(plane,plane):alpha,beta;

endsets

data:

alpha=@file('txt1.txt');

beta=@file('txt1.txt');

enddata

min=@sum(plane:@abs(delta));

@for(plane:@bnd(-30,delta,30));

@for(plane(i)|i#le#5:@for(plane(j)| j#ge#i+1: @abs(beta(i,j)+0.5*delta(i)+0.5*delta(j))>alpha(i,j)));

end
````

</details>

#### anli3_1 · MATLAB · f1caf63a

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`ce6b89b60e853f04694e4677f2680b1be5b898de10d060cf3b7596ebe3136f67`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/03第3章/anli3_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
x0=[150 85 150 145 130 0];
y0=[140 85 155 50 150 0];
q=[243 236 220.5 159 230 52];
xy0=[x0; y0];
d0=dist(xy0);   %求矩阵各个列向量之间的距离
d0(find(d0==0))=inf;
a0=asind(8./d0)  %以度为单位的反函数
xy1=x0+i*y0
xy2=exp(i*q*pi/180)
for m=1:6
     for n=1:6
         if n~=m
         b0(m,n)=angle((xy2(n)-xy2(m))/(xy1(m)-xy1(n))); 
         end
     end
end
b0=b0*180/pi;
dlmwrite('txt1.txt',a0,'delimiter', '\t','newline','PC');
dlmwrite('txt1.txt','~','-append');       %往纯文本文件中写LINGO数据的分割符
dlmwrite('txt1.txt',b0,'delimiter', '\t','newline','PC','-append','roffset', 1)
````

</details>

#### ex4_16 · LINGO · 44a04b8f

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`07e2761d06b89f6b69a123ad810e70f34b45e0844a0ce6a1cf1e04c04c4bc6ac`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_16.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

events/1..8/:x;

operate(events,events)/1 2,1 3,1 4,2 5,3 4,3 5,4 6,5 6,

5 7,5 8,6 7,6 8,7 8/:t;

endsets

data:

t=5 10 11 4 4 0 15 21 25 35 0 20 15;

enddata

min=@sum(events:x);

@for(operate(i,j):x(j)>x(i)+t(i,j));

end
````

</details>

#### ex4_17 · LINGO · b1f5bbac

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`23449aebf4d8db9edc7b6f723878ac459f3195accffdfff4254fd11e3330263d`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_17.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

events/1..8/:x,z; !x为事件的最早时间，z为事件的最迟时间;

operate(events,events)/1 2,1 3,1 4,2 5,3 4,3 5,4 6,5 6,

5 7,5 8,6 7,6 8,7 8/:t,s,ls,es,ef,lf; !s为松弛变量，ls为作业的最迟开工时间，es为最早开工时间，ef为最早完工时间，lf为最迟完工时间;

endsets

data:

t=5 10 11 4 4 0 15 21 25 35 0 20 15;

@text(txt1.txt)=es,ls; !把计算结果输出到外部纯文本文件;

enddata

min=@sum(events:x);

@for(operate(i,j):x(j)>x(i)+t(i,j));

n=@size(events);

z(n)=x(n);

@for(events(i)|i#lt#n:z(i)=@min(operate(i,j):z(j)-t(i,j)));

@for(operate(i,j):es(i,j)=x(i));

@for(operate(i,j):lf(i,j)=z(j));

@for(operate(i,j):ls(i,j)=lf(i,j)-t(i,j));

@for(operate(i,j):ef(i,j)=x(i)+t(i,j));

end
````

</details>

#### ex4_18 · LINGO · 58b3a1ad

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7b2c871ffbf1265b08c38fcc75850a934f0ef21cb417becdf17478c8b8e5ba60`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_18.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

events/1..8/:d;

operate(events,events)/1 2,1 3,1 4,2 5,3 4,3 5,4 6,5 6,

5 7,5 8,6 7,6 8,7 8/:t,x;

endsets

data:

t=5 10 11 4 4 0 15 21 25 35 0 20 15;

d=1 0 0 0 0 0 0 -1;

enddata

max=@sum(operate:t*x);

@for(events(i):@sum(operate(i,j):x(i,j))-@sum(operate(j,i):x(j,i))=d(i));

end
````

</details>

#### ex4_19 · LINGO · 096d51b6

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e12adc63d8ddcd5284852c3d96f2b33d912368c52e6f3474c258ca489e6a85eb`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_19.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

events/1..8/:x;

operate(events,events)/1 2,1 3,1 4,2 5,3 4,3 5,4 6,5 6,

5 7,5 8,6 7,6 8,7 8/:t,m,c,y;

endsets

data:

t=5 10 11 4 4 0 15 21 25 35 0 20 15;

m=5 8  8  3 4 0 15 16 22 30 0 16 12;

c=0 700 400 450 0 0 0 600 300 500 0 500 400; 

d=49;

enddata

min=@sum(operate:c*y);

@for(operate(i,j):x(j)-x(i)+y(i,j)>t(i,j));

n=@size(events);

x(n)-x(1)<d;

@for(operate:@bnd(0,y,t-m));

end
````

</details>

#### ex4_2 · LINGO · 42684aae

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f9defb032719eb4fa070bf0baee2226328cb9c0f266cb778bdc34c2645d5a59b`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_2.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

cities/A,B1,B2,C1,C2,C3,D/;

roads(cities,cities)/A B1,A B2,B1 C1,B1 C2,B1 C3,B2 C1,

B2 C2,B2 C3,C1 D,C2 D,C3 D/:w,x;

endsets

data:

w=2 4 3 3 1 2 3 1 1 3 4;

enddata

n=@size(cities); !城市的个数;

min=@sum(roads:w*x);

@for(cities(i)|i #ne#1 #and# i #ne#n:

@sum(roads(i,j):x(i,j))=@sum(roads(j,i):x(j,i)));

@sum(roads(i,j)|i #eq#1:x(i,j))=1;

@sum(roads(i,j)|j #eq#n:x(i,j))=1;

       end
````

</details>

#### ex4_20 · LINGO · 4fe97d66

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0fdfbca56cfd918cf77ae23c2e88eeeb71b3ca7b5f38b07d69c14b667ab69d83`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_20.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

events/1..8/:x,z;

operate(events,events)/1 2,1 3,1 4,2 5,3 4,3 5,4 6,5 6,

5 7,5 8,6 7,6 8,7 8/:t,m,c,y,es,ls;

endsets

data:

t=5 10 11 4 4 0 15 21 25 35 0 20 15;

m=5 8  8  3 4 0 15 16 22 30 0 16 12;

c=0 700 400 450 0 0 0 600 300 500 0 500 400; 

d=49;

@text(txt2.txt)=es,ls; !把作业最早开工时间es和最迟开工时间ls输出到外部纯文本文件;

enddata

min=@sum(operate:c*y)+@sum(events:x);

@for(operate(i,j):x(j)-x(i)+y(i,j)>t(i,j));

n=@size(events);

x(n)-x(1)<=d;

@for(operate:@bnd(0,y,t-m));

z(n)=x(n);

@for(events(i)|i#lt#n:z(i)=@min(operate(i,j):z(j)-t(i,j)+y(i,j)));

@for(operate(i,j):es(i,j)=x(i));

@for(operate(i,j):ls(i,j)=z(j)-t(i,j)+y(i,j));

     end
````

</details>

#### ex4_21 · LINGO · 8dface61

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`673f7ded280b3f2dd59b83daa4840e6ad8cc2d4c665ea7e7006dba1d830c6ce9`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_21.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

events/1..8/:d;

operate(events,events)/1 2,1 3,1 4,2 5,3 4,3 5,4 6,5 6,

5 7,5 8,6 7,6 8,7 8/:a,m,b,et,dt,x;

endsets

data:

a=3 8 8 3 2 0 8 18 18 26 0 11 12;

m= 5 9 11 4 4 0 16 20 25 33 0 21 15;

b=7 16 14 5 6 0 18 28 32 52 0 25 18;

d=1 0 0 0 0 0 0 -1;

limit=52;

enddata

@for(operate:et=(a+4*m+b)/6;dt=(b-a)^2/36);

max=tbar;

tbar=@sum(operate:et*x);

@for(events(i):@sum(operate(i,j):x(i,j))-@sum(operate(j,i):x(j,i))=d(i));

s^2=@sum(operate:dt*x);

p=@psn((limit-tbar)/s);

@psn((days-tbar)/s)=0.95;

end
````

</details>

#### ex4_4 · LINGO · 6ee7aade

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、文件结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5319460b3a2e0c72f57fa83fac5448161512d4b3606027cba88212facdc6b217`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_4.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

nodes/c1..c6/;

link(nodes,nodes):w,path;  !path标志最短路径上走过的顶点;

endsets

data:

path=0;

w=0;

@text(mydata1.txt)=@writefor(nodes(i):@writefor(nodes(j):

@format(w(i,j),' 10.0f')),@newline(1));

@text(mydata1.txt)=@write(@newline(1));

@text(mydata1.txt)=@writefor(nodes(i):@writefor(nodes(j):

@format(path(i,j),' 10.0f')),@newline(1));

enddata

calc:

w(1,2)=50;w(1,4)=40;w(1,5)=25;w(1,6)=10;

w(2,3)=15;w(2,4)=20;w(2,6)=25;

w(3,4)=10;w(3,5)=20;

w(4,5)=10;w(4,6)=25;w(5,6)=55;

@for(link(i,j):w(i,j)=w(i,j)+w(j,i));

@for(link(i,j) |i#ne#j:w(i,j)=@if(w(i,j)#eq#0,10000,w(i,j)));

@for(nodes(k):@for(nodes(i):@for(nodes(j):

tm=@smin(w(i,j),w(i,k)+w(k,j));

path(i,j)=@if(w(i,j)#gt# tm,k,path(i,j));w(i,j)=tm))); 

endcalc

end
````

</details>

#### ex4_7_1 · LINGO · e671e15d

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7033fbcdb7380c38deaf115141567f463418e1adcf755e77181f073bade8e246`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_7_1.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

nodes/s,1,2,3,4,t/;

arcs(nodes,nodes)/s 1,s 3,1 2,1 3,2 3,2 t,3 4,4 2,4 t/:c,f;

endsets

data:

c=8 7 9 5 2 5 9 6 10;

enddata

n=@size(nodes); !顶点的个数;

max=flow;

@for(nodes(i)|i #ne#1 #and# i #ne# n:

@sum(arcs(i,j):f(i,j))=@sum(arcs(j,i):f(j,i)));

@sum(arcs(i,j)|i #eq# 1:f(i,j))=flow;

@sum(arcs(i,j)|j #eq# n:f(i,j))=flow;

@for(arcs:@bnd(0,f,c));

end
````

</details>

#### ex4_7_2 · LINGO · 0482928f

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`a18e216e4ae2fbc0985824c777296d2102ca407f5f65cb59e17d959ab31d0421`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_7_2.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

nodes/s,1,2,3,4,t/;

arcs(nodes,nodes):c,f;

endsets

data:

c=0;

@text('fdata.txt')=f;

enddata

calc:

c(1,2)=8;c(1,4)=7;

c(2,3)=9;c(2,4)=5;

c(3,4)=2;c(3,6)=5;

c(4,5)=9;c(5,3)=6;c(5,6)=10;

endcalc

n=@size(nodes); !顶点的个数;

max=flow;

@for(nodes(i)|i #ne#1 #and# i #ne# n:

@sum(nodes(j):f(i,j))=@sum(nodes(j):f(j,i)));

@sum(nodes(i):f(1,i))=flow;

@sum(nodes(i):f(i,n))=flow;

@for(arcs:@bnd(0,f,c));

end
````

</details>

#### ex4_8_2 · LINGO · 4aa9a394

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d1557b78f02e7b16daaacbb3941b604b268576752e4ca734eea8500509b79fef`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/04第4章/ex4_8_2.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

nodes/s,1,2,3,4,t/:d;

arcs(nodes,nodes):b,c,f;  !c为容量，b为单位运价;

endsets

data:

d=14 0 0 0 0 -14;

b=0; c=0;

enddata

calc:

b(1,2)=2;b(1,4)=8;

b(2,3)=2;b(2,4)=5;

b(3,4)=1;b(3,6)=6;

b(4,5)=3;b(5,3)=4;b(5,6)=7;

c(1,2)=8;c(1,4)=7;

c(2,3)=9;c(2,4)=5;

c(3,4)=2;c(3,6)=5;

c(4,5)=9;c(5,3)=6;c(5,6)=10;

endcalc

min=@sum(arcs:b*f);

@for(nodes(i):@sum(nodes(j):f(i,j))-@sum(nodes(j):f(j,i))=d(i));

@for(arcs:@bnd(0,f,c));

end
````

</details>

#### 相似实现组 · LINGO · 26bbba0d

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：ex7_10.lg4

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1b931b7127f6f5b6d905eb32ad7d09f82e1e79176e2c2a5a383398ca52739861`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/07第7章/ex7_10.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

dmu/1..6/:s,t,p;    !决策单元，p为单位坐标向量，s,t为中间变量;

inw/1..2/:omega;        !输入权重; 

outw/1..2/:mu;       !输出权重;

inv(inw,dmu):x;     !输入变量;

outv(outw,dmu):y;

endsets

data:

ctr=?; !实时输入数据，对第n个单元做评价时，就输入n;

x=89.39      86.25        108.13    106.38      62.40      47.19

  64.3       99           99.6      96          96.2       79.9;

y=25.2       28.2         29.4      26.4        27.2       25.2

  223        287          317       291         295        222;

enddata

max=@sum(dmu:p*t);

p(ctr)=1; 

@for(dmu(i)|i#ne#ctr:p(i)=0);

@for(dmu(j):s(j)=@sum(inw(i):omega(i)*x(i,j));

t(j)=@sum(outw(i):mu(i)*y(i,j));s(j)>t(j));

@sum(dmu:p*s)=1;

end
````

</details>

##### 变体 2：ex14_4.lg4

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器；执行选择、交叉和变异的进化搜索。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3069bd50eab9a2938ef75e66b3e4b9d6d769fb844aec9777593582717d2952e3`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/14第14章/ex14_4.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

dmu/1..10/:s,t,p;    !决策单元，p为单位坐标向量，s,t为中间变量;

inw/1..3/:omega;        !输入权重; 

outw/1..2/:mu;       !输出权重;

inv(inw,dmu):x;     !输入变量;

outv(outw,dmu):y;

endsets

data:

ctr=?; !实时输入数据，对第n个单元做评价时，就输入n;

x=14.4	16.9	 15.53    15.4	14.17  13.33	  12.83   13	     13.4	  14

  0.65	0.72	 0.72	 0.76   0.76    0.69    0.61	  0.63	 0.75	  0.84

  31.3	32.2	 31.87	 32.23   32.4   30.77	  29.23	  28.2	 28.8	  29.1;

y=3621  3943  4086.67  4904.67  6311.67  8173.33  10236  12094.33     13603.33  14841

  0	   0.09	  0.07	0.13	  0.37	0.59	  0.51	0.44	  0.58	  1;

enddata

max=@sum(dmu:p*t);

p(ctr)=1; 

@for(dmu(i)|i#ne#ctr:p(i)=0);

@for(dmu(j):s(j)=@sum(inw(i):omega(i)*x(i,j));

t(j)=@sum(outw(i):mu(i)*y(i,j));s(j)>t(j));

@sum(dmu:p*s)=1;

end
````

</details>

#### ex7_3_1 · LINGO · 24671940

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8294a97f108df3d5af4eb4f5ea367f5b630425fdfa7f2ad298fad68839697cb9`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/07第7章/ex7_3_1.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

variable/1..2/:x;

S_Con_Num/1..4/:g,dplus,dminus;

S_con(S_Con_Num,Variable):c;

endsets

data:

g=1500 0 16 15;

c=200 300 2 -1 4 0 0 5;

enddata

min=dminus(1);

2*x(1)+2*x(2)<12;

@for(S_Con_Num(i):@sum(Variable(j):c(i,j)*x(j))+dminus(i)-dplus(i)=g(i));

end
````

</details>

#### ex7_3_3 · LINGO · 075efa55

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ee8d58615e3022e6813d2bb2ae0effe07eb47aa978f4b7e80e0c7edca4c026c1`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/07第7章/ex7_3_3.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

variable/1..2/:x;

S_Con_Num/1..4/:g,dplus,dminus;

S_con(S_Con_Num,Variable):c;

endsets

data:

g=1500 0 16 15;

c=200 300 2 -1 4 0 0 5;

enddata

min=3*dplus(3)+3*dminus(3)+dplus(4);    !三级目标函数;

2*x(1)+2*x(2)<12;

@for(S_Con_Num(i):@sum(Variable(j):c(i,j)*x(j))+dminus(i)-dplus(i)=g(i));

dminus(1)=0;!一级目标约束;

dplus(2)+dminus(2)=0;!二级目标约束;

end
````

</details>

#### 相似实现组 · LINGO · 7c359a84

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：ex7_4.lg4

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c33592750089f5475ef6b3719c6289f9ab87b6071a53690c5f79827a25321257`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/07第7章/ex7_4.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

level/1..3/:p,z,goal;

variable/1..2/:x;

h_con_num/1..1/:b;

s_con_num/1..4/:g,dplus,dminus;

h_con(h_con_num,variable):a;

s_con(s_con_num,variable):c;

obj(level,s_con_num)/1 1,2 2,3 3,3 4/:wplus,wminus;

endsets

data:

ctr=?;

goal=? ? 0;

b=12;

g=1500 0 16 15;

a=2 2;

c=200 300 2 -1 4 0 0 5;

wplus=0 1 3 1;

wminus=1 1 3 0;

enddata

min=@sum(level:p*z);

p(ctr)=1;

@for(level(i)|i#ne#ctr:p(i)=0);

@for(level(i):z(i)=@sum(obj(i,j):wplus(i,j)*dplus(j)+wminus(i,j)*dminus(j)));

@for(h_con_num(i):@sum(variable(j):a(i,j)*x(j))<b(i));

@for(s_con_num(i):@sum(variable(j):c(i,j)*x(j))+dminus(i)-dplus(i)=g(i));

@for(level(i)|i #lt# @size(level):@bnd(0,z(i),goal(i)));

end
````

</details>

##### 变体 2：ex7_6.lg4

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`667cf95d1f3187af19c142adda31aae4a9a761f5908505691207990ca2d3bab8`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/07第7章/ex7_6.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

level/1..5/:p,z,goal;

variable/1..3/:x;

s_con_num/1..8/:g,dplus,dminus;

s_con(s_con_num,variable):c;

obj(level,s_con_num)/1 1,2 2,2 3,2 4,3 8,4 5,4 6,4 7,5 1/:wplus,wminus;

endsets

data:

ctr=?;

goal=? ? ? ? 0;

g=1700 50 50 80 100 120 100 1900;

c=5 8 12 1 0 0 0 1 0 0 0 1 1 0 0 0 1 0 0 0 1 5 8 12;

wplus=0 0 0 0 1 0 0 0 1;

wminus=1 20 18 21 0 20 18 21 0;

enddata

min=@sum(level:p*z);

p(ctr)=1;

@for(level(i)|i#ne#ctr:p(i)=0);

@for(level(i):z(i)=@sum(obj(i,j):wplus(i,j)*dplus(j)+wminus(i,j)*dminus(j)));

@for(s_con_num(i):@sum(variable(j):c(i,j)*x(j))+dminus(i)-dplus(i)=g(i));

@for(level(i)|i #lt# @size(level):@bnd(0,z(i),goal));

end
````

</details>

#### ex7_7_1 · LINGO · da774889

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`19ef6bc2e4ede19dff4c5a1e9820e65757dfbfc76fc05f2a38c934ef06b72a6d`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/07第7章/ex7_7_1.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

plant/1..3/:b;

customer/1..4/:a;

routes(plant,customer):c,x;

endsets

data:

b=300 200 400;

a=200 100 450 250;

c=5 2 6 7 3 5 4 6 4 5 2 3;

enddata

min=@sum(routes:c*x);

@for(plant(i):@sum(customer(j):x(i,j))=b(i));

@for(customer(j):@sum(plant(i):x(i,j))<a(j));

end
````

</details>

#### ex7_7_2 · LINGO · 84d3692c

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d702c6c7a23d77f769217d75b6fff738833fe6e39638913f7ba8f8729c2aa1ad`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/07第7章/ex7_7_2.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

level/1..8/:p,z,goal;

s_con_num/1..13/:g,dplus,dminus;

plant/1..3/:b;

customer/1..4/:a;

routes(plant,customer):c,x;

obj(level,s_con_num)/1 9,2 1,3 2,3 3,3 4,3 5,4 6,4 7,4 8,4 9,5 10,6 11,7 12,8 13/:wplus,wminus;

endsets

data:

ctr=?;

goal=? ? ? ? ? ? ? 0;

b=300 200 400;

a=200 100 450 250;

c=5 2 6 7 3 5 4 6 4 5 2 3;

wplus=0 0 0 0 0 0 0 0 0 0 1 1 1 1;

wminus=1 1 1 1 1 1 1 1 1 1 0 0 1 0;

enddata

min=@sum(level:p*z);

p(ctr)=1;

@for(level(i)|i#ne#ctr:p(i)=0);

@for(level(i):z(i)=@sum(obj(i,j):wplus(i,j)*dplus(j)+wminus(i,j)*dminus(j)));

@for(plant(i):@sum(customer(j):x(i,j))<b(i));

x(3,1)+dminus(1)-dplus(1)=100;

@for(customer(j):@sum(plant(i):x(i,j))+dminus(1+j)-dplus(1+j)=0.8*b(j);

@sum(plant(i):x(i,j))+dminus(5+j)-dplus(5+j)=a(j));

@sum(routes:c*x)+dminus(10)-dplus(10)=3245;

x(2,4)+dminus(11)-dplus(11)=0;

@sum(plant(i):x(i,1))-20/45*@sum(plant(i):x(i,3))+dminus(12)-dplus(12)=0;

@sum(routes:c*x)+dminus(13)-dplus(13)=2950;

@for(level(i)|i #lt# @size(level):@bnd(0,z(i),goal));

end
````

</details>

#### ex7_8 · LINGO · a67b5079

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6b315dd22c36a418f64649d89138fe3d97c738475da9dee1c642d1e291f6869b`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/07第7章/ex7_8.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

plant/A1..A3/:b;

customer/B1..B4/:a;

routes(plant,customer):c,x;

deviation/1..12/:d1,d2,p1,p2;

endsets

data:

b=300 200 400;

a=200 100 450 250;

c=5 2 6 7 3 5 4 6 4 5 2 3;

p1=0,0,0,100000,10000,1000,1000,1000,1000,0,10,0;

p2=0,0,0,0,0,0,0,0,0,100,10,1;

enddata

@for(plant(i):[con1]@sum(customer(j):x(i,j))<b(i));

@for(customer(j):[con2]@sum(plant(i):x(i,j))+d1(j)=a(j));

[con3] x(3,1)+d1(5)-d2(5)=100;

@for(customer(j):[con4]@sum(plant(i):x(i,j))+d1(5+j)-d2(5+j)=0.8*a(j));

[con5] x(1,2)-d2(10)=0;

[con6] @sum(plant(i):x(i,1))-4/9*@sum(plant(i):x(i,3))+d1(11)-d2(11)=0;

[con7] @sum(routes:c*x)-d2(12)=0;

[obj] min=@sum(deviation:p1*d1+p2*d2);

end
````

</details>

#### B_10 · LINGO · 303f4543

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3ca803fd304fb01be67733163682b8c2e9289f65ea52354b40bc1acdd0927d2b`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/B_10.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

!6产地8销地运输问题;

sets:

  warehouses/wh1..wh6/: capacity;

  vendors/v1..v8/: demand;

  links(warehouses,vendors): cost, volume;

endsets

!目标函数;

  min=@sum(links: cost*volume);

!需求约束;

  @for(vendors(J):@sum(warehouses(I): volume(I,J))=demand(J));

!产量约束;

  @for(warehouses(I):@sum(vendors(J): volume(I,J))<=capacity(I));

 !下面是数据;

data:

  capacity=60 55 51 43 41 52;

  demand=35 37 22 32 41 32 43 38;

  cost=6 2 6 7 4 2 9 5

       4 9 5 3 8 5 8 2

       5 2 1 9 7 4 3 3

       7 6 7 3 9 2 7 1

       2 3 9 5 7 2 6 5

       5 5 2 2 8 1 4 3;

enddata

end
````

</details>

#### B_11 · LINGO · d54eaf4e

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b92e262d1a8c51a4628aa866545024c3ae9bcd29ce5b7d4481f22700b06fe9fd`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/B_11.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

  warehouses/wh1..wh6/: capacity;

  vendors/v1..v8/: demand;

  links(warehouses,vendors): cost, volume;

endsets

  min=@sum(links: cost*volume);

  @for(vendors(J):@sum(warehouses(I): volume(I,J))=demand(J));

  @for(warehouses(I):@sum(vendors(J): volume(I,J))<=capacity(I));

data:

  capacity=@file(Ldata.txt);

  demand=@file(Ldata.txt);

  cost=@file(Ldata.txt);

enddata

      end
````

</details>

#### B_12 · LINGO · 4b9115ce

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`40fcdfa5bb4a12ac2831d16b601b42a1583ad587ffa609c728286fe424caf4e5`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/B_12.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

sets:

  warehouses/wh1..wh6/: capacity;

  vendors/v1..v8/: demand;

  links(warehouses,vendors): cost, volume;

endsets

  min=@sum(links: cost*volume);

  @for(vendors(J):@sum(warehouses(I): volume(I,J))=demand(J));

  @for(warehouses(I):@sum(vendors(J): volume(I,J))<=capacity(I));

data:

  capacity=@ole(ydata.xls);

  demand=@ole(ydata.xls);

  cost=@ole(ydata.xls);

enddata

end






	

���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������

model:

sets:

  warehouses/wh1..wh6/: capacity;

  vendors/v1..v8/: demand;

  links(warehouses,vendors): cost, volume;

endsets

  min=@sum(links: cost*volume);

  @for(vendors(J):@sum(warehouses(I): volume(I,J))=demand(J));

  @for(warehouses(I):@sum(vendors(J): volume(I,J))<=capacity(I));

data:

  capacity=@ole(ydata.xls);

  demand=@ole(ydata.xls);

  cost=@ole(ydata.xls);

  @ole(ydata.xls)=volume;

enddata

end
````

</details>

#### exB_1 · LINGO · fda76a44

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3221b09d340531bef27dc9129240dc6c38b6e6c3c3e8ad3d18351be9cb23d77e`
- 语言：LINGO
- 符号：`sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_1.lg4`

<details>
<summary>展开原始代码</summary>

````text
sets:

  product/A B/;

  machine/M N/;

  week/1..2/;

  allowed(product,machine,week):x;

endsets
````

</details>

#### exB_2 · LINGO · afd7427f

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：完整优化模型或模型片段；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：声明集合/参数、目标和约束并由LINGO求解。
- **调用方式**：在 LINGO 中载入模型；先把集合、参数和约束改成当前问题定义。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9f35480038307c374585a93189d301a32afa7989e15fca6077511f3e7c42058f`
- 语言：LINGO
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_2.lg4`

<details>
<summary>展开原始代码</summary>

````text
init:

  X, Y = 0, .1;

endinit

Y=@log(X);

X^2+Y^2<=1;
````

</details>

#### exB_3 · LINGO · c995ef6f

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：声明集合/参数、目标和约束并由LINGO求解。
- **调用方式**：优先调用 `data`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d78989f3c97e2d1274a2f7f14e52ace23d171163f2c848c07b32497bc8f74669`
- 语言：LINGO
- 符号：`data`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_3.lg4`

<details>
<summary>展开原始代码</summary>

````text
data:

  interest_rate,inflation_rate = .085  ?;

enddata
````

</details>

#### exB_4 · LINGO · 42f5d34a

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`32d52f475231a3ef2d9c46623f546d99f3b68c5ca9b16d6f230ee48e51bf12b2`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_4.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

data:

      N=6;

enddata

sets:

      number/1..N/:x;

endsets

data:

      x = 5 1 3 4 6 10;

enddata

    minv=@min(number(I) | I #le# 5: x);

    maxv=@max(number(I) | I #ge# N-2: x);




	

���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������

model:

data:

      N=6;

enddata

sets:

      number/1..N/:x;

endsets

data:

      x = 5 1 3 4 6 10;

enddata

    minv=@min(number(I) | I #le# 5: x);

    maxv=@max(number(I) | I #ge# N-2: x);

  end
````

</details>

#### exB_5 · LINGO · 771beb3e

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器；重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `data`、`model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`90b7b676f51b2ddbac4a10408a69e6c2cc0455d5505e857438339706fc53f8d4`
- 语言：LINGO
- 符号：`data`, `model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_5.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

data:

  M=4; N=2; seed=1234567;

enddata

sets:

  rows/1..M/;

  cols/1..N/;

  table(rows,cols): X;

endsets

data:

  X=@qrand(seed);

enddata

end
````

</details>

#### exB_6 · LINGO · c696a1f1

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器；重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `model`、`sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`e96a9a9cb814a3c0805b8304f1248e261a79c5e7fa9f2e6512ae528d9a1b109a`
- 语言：LINGO
- 符号：`model`, `sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_6.lg4`

<details>
<summary>展开原始代码</summary>

````text
model:

!产生一列正态分布和t分布的随机数;

sets:

  series/1..15/: u, znorm, zt;

endsets

 !第一个均匀分布随机数是任意的;

  u(1) = @rand( .1234);

  !产生其余的均匀分布的随机数;

  @for(series(I)|I #GT# 1:u(I)=@rand(u(I-1)));

  @for(series( I):

    !正态分布随机数;

    @psn(znorm(I))=u(I);

    !和自由度为2的t分布随机数;

    @ptd(2,zt(I))=u(I);

    !znorm 和 zt 可以是负数;

    @free(znorm(I)); @free(zt(I)));

end
````

</details>

#### exB_7 · LINGO · d4d21bd8

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ee2209e344d3959537a2ff64afa1a8ed8450d86296b5555f88f416489406c22e`
- 语言：LINGO
- 符号：`sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_7.lg4`

<details>
<summary>展开原始代码</summary>

````text
sets:

  I/x1..x4/:x;

  B(I)/x2/:y;

  C(I)|#not#@in(B,&1):z;

endsets
````

</details>

#### exB_8 · LINGO · 4503d412

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f986ab7071385f92ba42474e171d2de26c370e6c84e04076924c0e8a6a359416`
- 语言：LINGO
- 符号：`sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_8.lg4`

<details>
<summary>展开原始代码</summary>

````text
sets:

  S1/A B C/;

  S2/X Y Z/;

  S3(S1,S2)/A X, A Z, B Y, C X/;

endsets

L=@in(S3,@index(S1,B),@index(S2,Y));
````

</details>

#### exB_9 · LINGO · 427f75d5

- 归属算法：博弈论
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#博弈论 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于博弈论中的“核心算法与辅助函数”。
- **执行主线**：在LINGO中声明集合、目标函数和约束后交给求解器。
- **调用方式**：优先调用 `sets`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`54218d59100055c7c816ac38c2091d8ca53f6358984741f4e70709c222e6badd`
- 语言：LINGO
- 符号：`sets`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/17附录B/exB_9.lg4`

<details>
<summary>展开原始代码</summary>

````text
sets:

  girls/debble,sue,alice/;

  boys/bob,joe,sue,fred/;

endsets

I1=@index(sue);

I2=@index(boys,sue);
````

</details>

<!-- END AUTO-INTEGRATED-CODE -->
