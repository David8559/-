---
type: generated-code-shard
status: generated
topic_hub: 数据处理 Hub
algorithm: RBF神经网络
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# RBF神经网络 · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/05-数据处理方法/数据处理 Hub|数据处理 Hub]]
- 独立实现：1
- 原始来源：1
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

#### anli15_4 · MATLAB · c15410ac

- 归属算法：RBF神经网络
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#RBF神经网络 · 复习|RBF神经网络 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于RBF神经网络中的“数据读取与预处理”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`9af33037db062d64e61f291c24ed8b4c46aaab44178dc44ab46736922aa7c47f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/anli15_4.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=load('jingliu.txt'); %把表中第2列到第6列的数据保存到纯文本文件jingliu.txt
a=a'; %注意神经网络的数据格式，不要把矩阵搞转置了。
P=a([1:4],[1:end-1]); [PN,PS1]=mapminmax(P); %自变量数据规格化到[-1,1]
T=a(5,[1:end-1]);  [TN,PS2]=mapminmax(T); %因变量数据规格化到[-1,1]
net1=newrb(PN,TN)  %训练RBF网络
x=a([1:4],end); xn=mapminmax('apply',x,PS1); %预测样本点自变量规格化
yn1=sim(net1,xn); y1=mapminmax('reverse',yn1,PS2) %求预测值，并把数据还原
delta1=abs(a(5,20)-y1)/a(5,20)  %计算RBF网络预测的相对误差
net2=feedforwardnet(4);  %初始化BP网络，隐含层的神经元取为4个（多次试验）
net2 = train(net2,PN,TN); %训练BP网络
yn2= net2(xn); y2=mapminmax('reverse',yn2,PS2)  %求预测值，并把数据还原
````

</details>
