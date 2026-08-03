---
type: generated-code-shard
status: generated
topic_hub: 评价模型 Hub
algorithm: AHP层次分析
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# AHP层次分析 · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub|评价模型 Hub]]
- 独立实现：3
- 原始来源：3
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

通过成对比较矩阵、权重计算和一致性检验完成多准则决策。

#### 层次分析法MATLAB实现 · MATLAB · 46280838

- 归属算法：AHP层次分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub#AHP层次分析 · 复习|AHP层次分析 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于AHP层次分析中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4f98c74fb783cfbd7dec67f98596097e17407eb5d24a4705ef77874f3edb963c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/综合评价方法/层次分析法/AHP理论/层次分析法MATLAB实现.txt`

<details>
<summary>展开原始代码</summary>

````matlab
%层次分析法的matlab程序  

disp('请输入判断矩阵A(n阶)');
A=input('A=');
[n,n]=size(A);
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
         %以下是一致性检验
CI=(t-n)/(n-1);RI=[0 0 0.52 0.89 1.12 1.26 1.36 1.41 1.46 1.49 1.52 1.54 1.56 1.58 1.59];
CR=CI/RI(n);
if CR<0.10
    disp('此矩阵的一致性可以接受!');
    disp('CI=');disp(CI);
    disp('CR=');disp(CR);
else 
    disp('此矩阵的一致性不可以接受!');
end
````

</details>

#### Untitled12 · MATLAB · 55fc5e96

- 归属算法：AHP层次分析
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub#AHP层次分析 · 复习|AHP层次分析 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于AHP层次分析中的“核心算法与辅助函数”。
- **执行主线**：进行特征分解以获得权重、主成分或稳定性信息。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`bd087b8f7ea86dde20a69da6137644eec8ea726b6be60fc190dc0bb99eb116d7`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/综合评价方法/层次分析法/Untitled12.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear 
fid=fopen('txt3.txt','r');
n1=6;
n2=3;
a=[];
for i=1:n1
 tmp=str2num(fgetl(fid));
 a=[a;tmp]; %读准则层判断矩阵
end
for i=1:n1 
    str1=char(['b',int2str(i),'=[];']); 
    str2=char(['b',int2str(i),'=[b',int2str(i),';tmp];']);
    eval(str1);
  for j=1:n2
    tmp=str2num(fgetl(fid));
    eval(str2); %读方案层的判断矩阵
  end
end
ri=[0,0,0.58,0.90,1.12,1.24,1.32,1.41,1.45]; %一致性指标
[x,y]=eig(a); lamda=max(diag(y)); 
num=find(diag(y)==lamda);
w0=x(:,num)/sum(x(:,num)); 
cr0=(lamda-n1)/(n1-1)/ri(n1)
for i=1:n1
[x,y]=eig(eval(char(['b',int2str(i)]))); 
lamda=max(diag(y));
num=find(diag(y)==lamda);
w1(:,i)=x(:,num)/sum(x(:,num));
cr1(i)=(lamda-n2)/(n2-1)/ri(n2);
end
cr1, ts=w1*w0, cr=cr1*w0
````

</details>

#### cengcifenxi · MATLAB · 228af15a

- 归属算法：AHP层次分析
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub#AHP层次分析 · 复习|AHP层次分析 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于AHP层次分析中的“预测与推断”。
- **执行主线**：进行特征分解以获得权重、主成分或稳定性信息。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cceef31492709df622488482d3f95b07cc658f98a924013e62262e638a1ebf6a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/小波神经网络预测代码/cengcifenxi.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc
clear 
A=[1 5 3 7;1/5 1 1/3 3;1/3 3 1 5;1/7 1/3 1/5 1];
[m,n]=size(A);
RI=[0 0 0.58 0.90 1.12 1.24 1.32 1.41 1.45 1.49 1.51];
R=rank(A);
[V,D]=eig(A);
tz=max(D);
B=max(tz);
[row,col]=find(D==B);
C=V(:,col);
CI=(B-n)/(n-1);
CR=CI/RI(1,n);
if CR<0.10
    disp('CI=');disp(CI);
    disp('CR=');disp(CR);
    disp('矩阵通过一致性检验，各向量权重向量Q为：');
    Q=zeros(n,1);
    for i=1:n
        Q(i,1)=C(i,1)/sum(C(:,1));
    end
    Q
else
    disp('矩阵没有通过一致性检验，请重新构造');
end
````

</details>
