---
type: generated-code-shard
status: generated
topic_hub: 评价模型 Hub
algorithm: TOPSIS
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# TOPSIS · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub|评价模型 Hub]]
- 独立实现：4
- 原始来源：4
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

通过正负理想解距离计算方案相对贴近度，适合综合评价与排序。

#### anli14_1 · MATLAB · abb670ff

- 归属算法：TOPSIS
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub#TOPSIS · 复习|TOPSIS · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于TOPSIS中的“数据读取与预处理”。
- **执行主线**：执行归一化或标准化以统一变量尺度。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`4a309ce92f95679eda422eee4f8f9b23c5db8aeb5d9c55f69dfa719a921ffc4c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/14第14章/anli14_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=load('zhaopin.txt');   %把原始数据保存在纯文本文件zhaopin.txt中，并且把A，B，C，D分别替换成相应的数值
b=zscore(a); %数据标准化
w=[0.4211    0.1053    0.2105    0.0526    0.2105];
w=repmat(w,16,1);
c=b.*w    %计算加权属性
cstar=max(c)    %求正理想解
c0=min(c)       %求负理想解
for i=1:16
    sstar(i)=norm(c(i,:)-cstar);   %求到正理想解的距离
    s0(i)=norm(c(i,:)-c0);       %求到负理想的距离
end
f=s0./(sstar+s0);
xlswrite('book3.xls',[sstar' s0' f'])  %把计算结果写到Excel文件中，便于将来做表
[sc,ind]=sort(f,'descend')       %求排序结果
````

</details>

#### ex14_1_3 · MATLAB · c5382e4f

- 归属算法：TOPSIS
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub#TOPSIS · 复习|TOPSIS · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于TOPSIS中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f8c8e0417bcfa90f17a49892d267d700fb0168af76e8e82506b1191cd734b769`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/14第14章/ex14_1_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=[0.1	5	5000	4.7
 0.2	6	6000	5.6
 0.4	7	7000	6.7
 0.9	10	10000	2.3
 1.2	2	400	    1.8];
[m,n]=size(a);
x2=@(qujian,lb,ub,x)(1-(qujian(1)-x)./(qujian(1)-lb)).*(x>=lb & x<qujian(1))+(x>=qujian(1) & x<=qujian(2))+(1-(x-qujian(2))./(ub-qujian(2))).*(x>qujian(2) & x<=ub);
qujian=[5,6]; lb=2; ub=12;
a(:,2)=x2(qujian,lb,ub,a(:,2)); %对属性2进行变换
for j=1:n
    b(:,j)=a(:,j)/norm(a(:,j));  %向量规划化
end
w=[0.2 0.3 0.4 0.1];
c=b.*repmat(w,m,1);      %求加权矩阵
Cstar=max(c);    %求正理想解
Cstar(4)=min(c(:,4))  %属性4为成本型的
C0=min(c);       %q求负理想解
C0(4)=max(c(:,4))        %属性4为成本型的
for i=1:m
    Sstar(i)=norm(c(i,:)-Cstar);  %求到正理想解的距离
    S0(i)=norm(c(i,:)-C0);      %求到负理想的距离
end
f=S0./(Sstar+S0);
[sf,ind]=sort(f,'descend')       %求排序结果
````

</details>

#### Pex9_2 · Python · 01c1ab3e

- 归属算法：TOPSIS
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub#TOPSIS · 复习|TOPSIS · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于TOPSIS中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`dae6d81eeb489470e6085d38e726b9c494d2d7167e65a02eecf107fec6d5e37d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/09第9章  综合评价方法(Python 程序及数据)/Pex9_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex9_2.py
import numpy as np
from scipy.stats import rankdata
a=np.loadtxt("Pdata9_1_3.txt")

cplus=a.max(axis=0)   #逐列求最大值
cminus=a.min(axis=0)  #逐列求最小值
print("正理想解=",cplus,"负理想解=",cminus)
d1=np.linalg.norm(a-cplus, axis=1)  #求到正理想解的距离
d2=np.linalg.norm(a-cminus, axis=1) #求到负理想解的距离
print(d1, d2)   #显示到正理想解和负理想解的距离
f1=d2/(d1+d2); print("TOPSIS的评价值为：", f1)

t=cplus-a   #计算参考序列与每个序列的差
mmin=t.min(); mmax=t.max()  #计算最小差和最大差
rho=0.5  #分辨系数
xs=(mmin+rho*mmax)/(t+rho*mmax)  #计算灰色关联系数
f2=xs.mean(axis=1)  #求每一行的均值
print("\n关联系数=", xs,'\n关联度=',f2)  #显示灰色关联系数和灰色关联度

[n, m]=a.shape
cs=a.sum(axis=0)  #逐列求和
P=1/cs*a   #求特征比重矩阵
e=-(P*np.log(P)).sum(axis=0)/np.log(n)  #计算熵值
g=1-e   #计算差异系数
w = g / sum(g)  #计算权重
F = P @ w       #计算各对象的评价值
print("\nP={}\n,e={}\n,g={}\n,w={}\nF={}".format(P,e,g,w,F))

R=[rankdata(a[:,i]) for i in np.arange(6)]  #求每一列的秩
R=np.array(R).T   #构造秩矩阵
print("\n秩矩阵为：\n",R)
RSR=R.mean(axis=1)/n; print("RSR=", RSR)



    
````

</details>

#### Topsis算法综合评价代码 · MATLAB · 67545c87

- 归属算法：TOPSIS
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/01-评价类模型/评价模型 Hub#TOPSIS · 复习|TOPSIS · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于TOPSIS中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`77ec89fc1eb901c8ba2554f054fe3ac07eb5b63afcec08f04a2ae914eb0de737`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/Topsis算法综合评价代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
Topsis算法基本思想：基于归一化后的原始数据矩阵，采用余弦法找出有限方案中的最优方案和最劣方案（分别用最优向量和最劣向量表示），
然后分别计算各评价对象与最优方案和最劣方案间的距离，获得各评价对象与最优方案的相对接近程度，以此作为评价优劣的依据。
案例代码：x是需要评价的对象矩阵

x=[
21584   76.7    7.3 1.01    78.3    97.5    2.0
24372   86.3    7.4 0.80    91.1    98.0    2.0
22041   81.8    7.3 0.62    91.1    97.3    3.2
21115   84.5    6.9 0.60    90.2    97.7    2.9
24633   90.3    6.9 0.25    95.5    97.9    3.6];%矩阵
[n,m]=size(x);
%将3，4，7的低优指标去倒数转化为高优指标并且把所有指标换成接近的大小?
x(:,1)=x(:,1)/100;
x(:,3)=(1./x(:,3))*100;
x(:,4)=(1./x(:,4))*100;
x(:,7)=(1./x(:,7))*100;
zh=zeros(1,m);
d1=zeros(1,n); %最小值矩阵
d2=zeros(1,n); %最大值矩阵
c=zeros(1,n);  %接近程度
%归一化
for i=1:m
    for j=1:n
        zh(i)=zh(i)+x(j,i)^2;
    end
end
for i=1:m
    for j=1:n
       x(j,i)=x(j,i)/sqrt( zh(i));
    end
end
%计算距离
xx=min(x);
dd=max(x);
for i=1:n
    for j=1:m
        d1(i)=d1(i)+(x(i,j)-xx(j))^2;
    end
    d1(i)=sqrt(d1(i));
end
for i=1:n
    for j=1:m
        d2(i)=d2(i)+(x(i,j)-dd(j))^2;
    end
    d2(i)=sqrt(d2(i));
end
%计算接近程度
for i=1:n
    c(i)=d1(i)/(d2(i)+d1(i));
end
c
````

</details>
