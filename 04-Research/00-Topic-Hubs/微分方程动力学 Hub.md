---
type: topic-hub
topic_tag: topic/动力学模型
keywords: [微分方程, sir, sis, logistic, 扩散]
tags: [system/topic-hub, topic/动力学模型]
---

# 微分方程动力学 Hub

<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->
## 复习与调用指南

> [!summary] 阅读顺序
> 先用“快速选择”确定算法，再读复习卡掌握思想和步骤，最后跳到实现区选择代码。源码默认折叠；数据明细不在复习页展开。

### 快速选择

| 算法或用途 | 主要解决什么 | 独立实现 | 语言 |
|---|---|---:|---|
| [[#偏微分方程 · 复习|偏微分方程]] | 描述状态同时随时间和空间变化。 | 1 | MATLAB |
| [[#差分方程 · 复习|差分方程]] | 描述离散时间状态的递推演化。 | 11 | Python |
| [[#常微分方程 · 复习|常微分方程]] | 描述状态随时间连续变化的动力系统。 | 11 | MATLAB, Python |
| [[#微分与差分方程 · 复习|微分与差分方程]] | 覆盖连续时间微分模型和离散时间递推模型。 | 9 | Python |
| [[#微分方程建模 · 复习|微分方程建模]] | 用变化率方程表达系统内部机制与动态反馈。 | 18 | MATLAB |

### 逐算法复习卡

#### 偏微分方程 · 复习

- **解决什么**：描述状态同时随时间和空间变化。
- **核心思想**：扩散、对流、反应项与边界/初始条件共同决定解。
- **标准流程**：写PDE → 定义区域与边界 → 离散空间/时间 → 求解 → 网格收敛检验。
- **何时调用**：存在扩散、传热、波动或空间传播时使用。
- **最易出错**：没有边界条件和网格收敛检验的结果不可直接使用。
- **库内覆盖**：1 个独立实现、1 个原始来源；语言：MATLAB；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#ex13_2 · MATLAB · c01bc570|ex13_2]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#偏微分方程 · 实现|跳转到源码实现区]]

#### 差分方程 · 复习

- **解决什么**：描述离散时间状态的递推演化。
- **核心思想**：下一期状态由当前或若干历史状态决定。
- **标准流程**：定义状态与步长 → 写递推式 → 给初值 → 迭代 → 求平衡点与稳定性。
- **何时调用**：过程天然按期更新或连续模型需离散化时使用。
- **最易出错**：注意时间步长、索引偏移和数值发散。
- **库内覆盖**：11 个独立实现、11 个原始来源；语言：Python；其中 4 个识别到函数/类型入口。
- **优先阅读**：[[#相似实现组 · Python · 3b999fe2|Pex13_5]]、[[#Pex13_4 · Python · 0cdb3eef|Pex13_4]]、[[#相似实现组 · Python · 894a6199|Pex13_7_1]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#差分方程 · 实现|跳转到源码实现区]]

#### 常微分方程 · 复习

- **解决什么**：描述状态随时间连续变化的动力系统。
- **核心思想**：由状态导数、初值和参数决定轨迹。
- **标准流程**：定义状态 → 写导数函数 → 设初值/时间 → 数值积分 → 相图/参数分析。
- **何时调用**：机制可写成变化率且空间效应可忽略时使用。
- **最易出错**：刚性、步长、参数单位和初值敏感性决定可信度。
- **库内覆盖**：11 个独立实现、11 个原始来源；语言：MATLAB, Python；其中 3 个识别到函数/类型入口。
- **优先阅读**：[[#Pex8_5 · Python · 70c68866|Pex8_5]]、[[#Pex8_6 · Python · c7b0adfa|Pex8_6]]、[[#Pex15_3 · Python · 8de3a7bd|Pex15_3]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#常微分方程 · 实现|跳转到源码实现区]]

#### 微分与差分方程 · 复习

- **解决什么**：覆盖连续时间微分模型和离散时间递推模型。
- **核心思想**：根据时间尺度选择导数或差分表达状态变化。
- **标准流程**：确定时间粒度 → 写状态方程 → 给初值 → 求解/迭代 → 平衡点与稳定性分析。
- **何时调用**：过程具有明确动态反馈时进入，再选择ODE、PDE或差分模型。
- **最易出错**：混淆连续与离散时间会造成参数含义和稳定条件错误。
- **库内覆盖**：9 个独立实现、9 个原始来源；语言：Python；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#Pex8_10_1 · Python · fdd1ee45|Pex8_10_1]]、[[#Pex8_11 · Python · 7921e5f8|Pex8_11]]、[[#Pex8_7 · Python · e14fc86f|Pex8_7]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#微分与差分方程 · 实现|跳转到源码实现区]]

#### 微分方程建模 · 复习

- **解决什么**：用变化率方程表达系统内部机制与动态反馈。
- **核心思想**：状态变量、守恒关系、速率项和初边值条件共同定义模型。
- **标准流程**：选状态 → 推导速率 → 定初边值 → 数值求解 → 参数估计 → 稳定性/敏感性分析。
- **何时调用**：需要解释演化机制而不只是预测数值时使用。
- **最易出错**：方程可解不等于机制正确，参数可辨识性和单位一致性必须检查。
- **库内覆盖**：18 个独立实现、18 个原始来源；语言：MATLAB；其中 5 个识别到函数/类型入口。
- **优先阅读**：[[#anli6_2_1 · MATLAB · 3dd9f2f7|anli6_2_1]]、[[#example11 · MATLAB · 98265ef9|example11]]、[[#anli6_1_1 · MATLAB · ec23034b|anli6_1_1]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#微分方程建模 · 实现|跳转到源码实现区]]

### 通用调用检查表

1. 先确认当前问题是否满足复习卡中的适用条件。
2. 优先选择标有函数/类型入口的实现，脚本型代码先重构参数。
3. 用最小样例跑通，再替换为项目输入；不要一开始就接入完整题目。
4. 检查目标方向、变量单位、边界条件、随机种子和软件版本。
5. 保存运行环境、参数、结果与检验，验证通过后再进入项目正式代码。

<!-- END AUTO-HUB-STUDY-GUIDE -->

> 自动更新：2026-07-14 · 匹配笔记：1

## 相关笔记

- [[04-Research/03-建模算法源码库/代码资料索引]] — 相关度 4

## 邻接主题

- [[Topic Index]]
- [[预测模型 Hub]]
- [[蒙特卡洛 Hub]]
- [[模型检验 Hub]]

<!-- BEGIN AUTO-INTEGRATED-CODE -->
## 源码实现库（按需调用）

> [!warning] 使用边界
> 以下源码保留全文与来源，但默认均未运行验证。数据依赖明细已从阅读页省略；调用时按代码理解卡完成参数化、最小样例和结果检验。来源显示为可复制路径，不直接调用 Windows 打开未知扩展名。

- 本 Hub 收录原始源码文件：50
- 精确去重后的独立实现：50
- 合并后的实现组：45

### 实现索引

| 算法或用途 | 独立实现 | 原始源码 |
|---|---:|---:|
| [[#偏微分方程 · 实现|偏微分方程]] | 1 | 1 |
| [[#差分方程 · 实现|差分方程]] | 11 | 11 |
| [[#常微分方程 · 实现|常微分方程]] | 11 | 11 |
| [[#微分与差分方程 · 实现|微分与差分方程]] | 9 | 9 |
| [[#微分方程建模 · 实现|微分方程建模]] | 18 | 18 |

### 偏微分方程 · 实现

#### ex13_2 · MATLAB · c01bc570

- 归属算法：偏微分方程
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#偏微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于偏微分方程中的“结果绘图与展示”。
- **执行主线**：离散空间项并求解偏微分方程；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`328589607718e7c030993ce1373bae6c2d7c46469bfd41f2ccadef931227bb35`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
f=imread('tu2.bmp'); %读取原图像
h1=fspecial('laplacian',0); %式（13.3）的滤波器，等价于式（13.5）中参数为0
g1=f-imfilter(f,h1); %中心为-4，c=-1,即从原图像中减去拉普拉斯算子处理的结果
h2=[1 1 1; 1 -8 1; 1 1 1]; %式（13.4）的滤波器
g2=f-imfilter(f,h2); %中心为-8，c=-1
subplot(1,3,1),imshow(f) %显示原图像
subplot(1,3,2),imshow(g1) %显示滤波器(13.3)修复的图像
subplot(1,3,3),imshow(g2) %显示滤波器(13.4)修复的图像
````

</details>

### 差分方程 · 实现

#### Pex13_1 · Python · bd474599

- 归属算法：差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于差分方程中的“模型求解”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`14ab546a7b0914cb717b4220d16601d2b55e44023f7397f9d2752992df0afc41`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_1.py
from sympy import Function, rsolve
from sympy.abc import n
y = Function('y')
f=y(n+2)-y(n+1)-y(n)
ff=rsolve(f, y(n),{y(1):1,y(2):1})
print(ff)
````

</details>

#### Pex13_2 · Python · 744c4160

- 归属算法：差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于差分方程中的“模型求解”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`aa1823a850796cf4997db2e9c0afaac4137dbd0b4cb520a3ccf7c36cb8797b57`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_2.py
import sympy as sp
sp.var('k'); sp.var('y',cls=sp.Function)
f = y(k+1)-y(k)-3-2*k
f1 = sp.rsolve(f, y(k)); f2 = sp.simplify(f1)
print(f2)
       
````

</details>

#### Pex13_3 · Python · 6a6bef01

- 归属算法：差分方程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于差分方程中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e0f887f40aa9a4cbbe0c5bc121b7a79261e9559ca667764ea5526cc9cf7e7b62`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_3.py
x0=1000000; r=0.005; N=500; n=0; xm=8000
x1=x0*(1+r)-xm
while n<=N and x1>0:
    n+=1;
    if n%12==0: print("第%d个月末欠钱：x(%d)=%.4f"%(n,n,x1))
    x0=x1; x1=x0*(1+r)-xm
print("还款月数n=",n+1)
print("还款%d年%d个月"%((n+1)//12,n+1-12*((n+1)//12)))
````

</details>

#### Pex13_4 · Python · 0cdb3eef

- 归属算法：差分方程
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于差分方程中的“结果绘图与展示”。
- **执行主线**：进行特征分解以获得权重、主成分或稳定性信息；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6534005b62729bf01d8dc6fdc936737f3001db2adfc39b4ffaaf75fbc4aa3fd7`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_4.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_4.py
import numpy as np
from numpy.linalg import eig, inv
from matplotlib.pyplot import bar, show, legend, rc, plot
rc('font',size=16); rc('font',family='SimHei')
L=np.array([[0,4,3],[0.5,0,0],[0,0.25,0]])
X=1000*np.ones((3,1)); TX=np.zeros((3,5))
for i in range(5): X=L.dot(X); TX[:,i]=X.flatten()
print("TX=",TX)
for i in range(3): bar(np.arange(1,6)-0.25+i/4,TX[i],width=0.2)
legend(('幼龄组','二龄组','三龄组')); show()

val,vec=eig(L)  #计算特征值及对应的特征向量
cv=inv(vec).dot(1000*np.ones(3)); c=abs(cv[0])
print("特征值=",val,"\n特征向量为：\n",vec,'\nc=',c)

s=int(input("输入s的值:")); m=10  #计算10年
TY=[]; Y=np.ones(3)*1000; TY=np.zeros((m,3))
for i in range(1,m+1):
    Y=L.dot(Y)-s*np.ones(3); TY[i-1,:]=Y.flatten()
plot(np.arange(1,m+1),TY)
legend(('幼龄组','二龄组','三龄组')); show()
````

</details>

#### 相似实现组 · Python · 3b999fe2

- 归属算法：差分方程
- 用途：结果绘图与展示
- 独立实现变体：4
- 原始来源文件：4
- 复习入口：[[#差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：Pex13_5.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于差分方程中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `fun`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b90d5eb22cbadc517c32b69c20e5447470d0f792f4688d63b78885d7ca4b4a9f`
- 语言：Python
- 符号：`fun`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_5.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_5.py
import numpy as np
import matplotlib.pyplot as plt

def fun(delta,*str):
    w=100; tw=[]
    for k in range(1,11):
        w=delta*w+2.5-0.125*k; tw.append(w)
    print(tw); w2=tw[-1]  #提取第二阶段的初值
    tw2=[]; k=0
    while w2>=75:
        k+=1; w2=delta*w2+1.25;
        tw2.append(w2); tw.append(w2)
    print("k=%d时,w(%d)=%.4f"%(k,k,w2))

    plt.plot(np.arange(1,len(tw)+1),tw,str[0])

fun(0.975,"s-")
fun(0.97,"*-")

plt.legend(("正常代谢","增加运动"),prop={'family': 'SimHei', 'size': 15})
plt.show()
````

</details>

##### 变体 2：Pex13_5_1.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于差分方程中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `fun`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`abd34be8136d2b037b3004696e02f40e20ad2a7605682060a8253134791592df`
- 语言：Python
- 符号：`fun`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_5_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_5_1.py
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='SimHei'); plt.rc('font',size=16) 
def fun(delta,*s):
    w=100; tw=[]
    for k in range(1,11):
        w=delta*w+2.5-0.125*k; tw.append(w)
    print(tw); w2=tw[-1]  #提取第二阶段的初值
    tw2=[]; k=0
    while w2>=75:
        k+=1; w2=delta*w2+1.25;
        tw2.append(w2); tw.append(w2)
    print("k=%d时,w(%d)=%.4f"%(k,k,w2))
    plt.plot(np.arange(1,len(tw)+1),tw,s[0])  #传入的s是tuple类型

fun(0.975,"s-"); fun(0.97,"*-")
plt.legend(("正常代谢","增加运动"))
plt.xlabel("$k$/周"); plt.ylabel("$w$/kg") 
plt.show()
````

</details>

##### 变体 3：Pex13_5_2.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于差分方程中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `fun`、`fun2`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`eb60174c6a2f1fba0970ae2d8182a64a279b84116c74cdda5291de2e4ddb5d52`
- 语言：Python
- 符号：`fun`, `fun2`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_5_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_5_2.py
import numpy as np
import matplotlib.pyplot as plt

def fun(delta,*str):
    w=100; tw=[]
    for k in range(1,11):
        w=delta*w+2.5-0.125*k; tw.append(w)
    print(tw); w2=tw[-1]  #提取第二阶段的初值
    tw2=[]; k=0
    while w2>=75:
        k+=1; w2=delta*w2+1.25;
        tw2.append(w2); tw.append(w2)
    print("k=%d时,w(%d)=%.4f"%(k,k,w2))
    plt.plot(np.arange(1,len(tw)+1),tw,str[0])

def fun2(datas,labels):
    for data, style in datas:
        fun(data, style)
    plt.legend(labels, prop={'family': 'SimHei', 'size': 16})
    plt.show()

fun2([(0.975,"s-"),(0.97,"*-")],("正常代谢","增加运动"))
````

</details>

##### 变体 4：Pex13_5_3.py

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于差分方程中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `fun`、`fun2`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`409c6caf928cba121fcac1b53f84f4414046d7acd38423952e97a99b3d12a88c`
- 语言：Python
- 符号：`fun`, `fun2`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_5_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_5_3.py
import numpy as np
import matplotlib.pyplot as plt

def fun(delta,*str):
    w=100; tw=[]
    for k in range(1,11):
        w=delta*w+2.5-0.125*k; tw.append(w)
    print(tw); w2=tw[-1]  #提取第二阶段的初值
    tw2=[]; k=0
    while w2>=75:
        k+=1; w2=delta*w2+1.25;
        tw2.append(w2); tw.append(w2)
    print("k=%d时,w(%d)=%.4f"%(k,k,w2))
    plt.plot(np.arange(1,len(tw)+1),tw,str[0])

def fun2(datas,labels):
    for data, style in datas:
        fun(data, style)
    plt.legend(labels, prop={'family': 'SimHei', 'size': 16})
    plt.show()

fun2([(0.975,"s-"),(0.97,"*-")],("正常代谢","增加运动"))
````

</details>

#### 相似实现组 · Python · 894a6199

- 归属算法：差分方程
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：Pex13_7_1.py

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于差分方程中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`343c8249da1f3661e74ec6929fff50b7bfc9e552a71922fd01e2e02a8c656d79`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_7_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_7_1.py
import sympy as sp
a0,b0, c0=sp.symbols('a0 b0 c0')
n=sp.symbols('n',positive=True)
A=sp.Matrix([[1,1/2,0],[0,1/2,1],[0,0,0]])
if A.is_diagonalizable(): print("A的对角化矩阵为：\n",A.diagonalize())
else: print("A不能对角化")
P=A.diagonalize()[0]; D=A.diagonalize()[1]
x=P*D**n*(P.inv())*sp.Matrix([a0,b0,c0])
x=sp.simplify(x); print(x)
````

</details>

##### 变体 2：Pex13_7_2.py

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于差分方程中的“核心算法与辅助函数”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`63d2ad3273496c75dc6ab8d326cb6d6893ac46daf7236c59796012a163e66896`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pex13_7_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex13_7_2.py
import sympy as sp
a0,b0, c0=sp.symbols('a0 b0 c0')
n=sp.symbols('n',positive=True)
A=sp.Matrix([[1,1/4,0],[0,1/2,0],[0,1/4,1]])
if A.is_diagonalizable(): print("A的对角化矩阵为：\n",A.diagonalize())
else: print("A不能对角化")
P=A.diagonalize()[0]; D=A.diagonalize()[1]
x=P*D**n*(P.inv())*sp.Matrix([a0,b0,c0])
x=sp.simplify(x); print(x)
````

</details>

#### Pz13_1 · Python · 84cf9f86

- 归属算法：差分方程
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于差分方程中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5f3ddf257cc643aeac0dc8f034f8253c06559ce24c66d7b463f51f987fc18ac2`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/13第13章  差分方程模型（Python 程序及数据）/Pz13_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pz13_1.py
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text',usetex=True); plt.rc('font',size=16)
logistic=lambda k, x: k*x*(1-x)
kk=np.arange(0, 4.01, 0.01); listk=[]; listx=[]
for k in kk:
    x=0.5
    for i in range(1,500):
        x1=logistic(k,x); x=x1
        if i>400: listk.append(k); listx.append(x)
plt.scatter(listk,listx,c='b',s=1); plt.grid(True)
plt.xticks(np.arange(0,4.01,0.5)); plt.xlabel("$k$")
plt.ylabel("$x^*(k)$"); plt.show()
````

</details>

### 常微分方程 · 实现

#### ex6_10 · MATLAB · b52b67ec

- 归属算法：常微分方程
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于常微分方程中的“结果绘图与展示”。
- **执行主线**：定义状态导数并进行常微分方程数值积分；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7e030b857b27ab7b410df8290d343e342b454ed03a5a770ab395c452d5eaa8d2`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_10.m`

<details>
<summary>展开原始代码</summary>

````matlab
rho=10; beta=28; lamda=8/3;
f=@(t,Y) [rho*(Y(2)-Y(1))
beta*Y(1)-Y(2)-Y(1)*Y(3)
-lamda*Y(3)+Y(1)*Y(2)];   %定义微分方程组右端项的匿名函数
[t,y]=ode45(f,[0,30],[5,13,17])   %求数值解
subplot(2,2,1)
plot(t,y(:,1),'*')  %画出x的曲线
subplot(2,2,2)
plot(t,y(:,2),'X')  %画出y的曲线
subplot(2,2,3)
plot(t,y(:,3),'o')  %画出z的曲线
subplot(2,2,4)       
plot3(y(:,1),y(:,2),y(:,3)) %画出空间的轨线
````

</details>

#### ex6_7 · MATLAB · 59a476c6

- 归属算法：常微分方程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于常微分方程中的“核心算法与辅助函数”。
- **执行主线**：定义状态导数并进行常微分方程数值积分。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0aed54afaefe818efffd86db286e4f0f837d5cdb45d419f929d4fe80814705b3`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_7.m`

<details>
<summary>展开原始代码</summary>

````matlab
doty=@(x,y) -2*y+2*x^2+2*x;  %定义匿名函数
[x,y]=ode45(doty,[0,0.5],1)
````

</details>

#### ex6_8 · MATLAB · 4e482274

- 归属算法：常微分方程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于常微分方程中的“核心算法与辅助函数”。
- **执行主线**：定义状态导数并进行常微分方程数值积分。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ca8e8bd3cc7ee3899bd27c76c37eb6a8998b6b3257b2463c59cfabc00be8b576`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_8.m`

<details>
<summary>展开原始代码</summary>

````matlab
[T,Y]=ode45('F',[0 1],[0;1;-1])
````

</details>

#### ex15_1 · MATLAB · 814ca698

- 归属算法：常微分方程
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于常微分方程中的“结果绘图与展示”。
- **执行主线**：定义状态导数并进行常微分方程数值积分；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`030e23751927bcaca6787b4911c665a55cd36e3f177354e69e4cfca2212ade7c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
dxy=@(t,x)[-0.0544*x(2)+54000*(t>=0 & t<1)+6000*(t>=2 & t<3)+13000*(t>=5 & t<6)
    -0.0106*x(1)];  %用匿名函数定义方程右端项，这里用逻辑语句定义分段函数
[t,xy]=ode45(dxy,[0:36],[0,21500])
subplot(211), plot(t,xy(:,1),'r*',t,xy(:,2),'gD')
xlabel('时间t'),  ylabel('人数'), legend('美军','日军')
subplot(212),  plot(xy(:,1),xy(:,2))  %画微分方程组的轨线
xlabel('美军人数x'),  ylabel('日军人数y')  
````

</details>

#### ex15_5 · MATLAB · 3e670ba1

- 归属算法：常微分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于常微分方程中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`d61150642efb2fb993e61a1f4e8d6b2644fab84b75321eaa6745027ba901cf65`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/15第15章/ex15_5.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
x0=[4.93   2.33   3.87   4.35   6.63   7.15   5.37   6.39   7.81   8.35];
x1=cumsum(x0);  %求1次累加序列
n=length(x0);
z=0.5*(x1(2:n)+x1(1:n-1));   %求x1的均值生成序列
B=[-z',z'.^2];
Y=x0(2:end)';
ab_hat=B\Y     %估计参数a,b的值
x=dsolve('Dx+a*x=b*x^2','x(0)=x0');  %求解常微分方程
x=simple(x);  %对符号解进行化简
x=subs(x,{'a','b','x0'},{ab_hat(1),ab_hat(2),x0(1)});  %代入参数值
yuce=subs(x,'t',[0:n-1])   %求已知数据点1次累加序列的预测值
x=vpa(x,6) %显示6位数字的符号解
x0_hat=[yuce(1),diff(yuce)] %求已知数据点的预测值
epsilon=x0-x0_hat    %求残差
delta=abs(epsilon./x0)  %求相对误差
xlswrite('book4.xls',[x0',x0_hat',epsilon',delta'])
````

</details>

#### Pan8_1 · Python · 2aa4a392

- 归属算法：常微分方程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于常微分方程中的“核心算法与辅助函数”。
- **执行主线**：定义状态导数并进行常微分方程数值积分。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2b0470ecfbcc88a5e27e13c01f3e14dabe023431d51c928973ec28ff5f06b2c8`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pan8_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pan8_1.py
import numpy as np
from scipy.integrate import odeint
s0=155.0;  i0=1.0;  s_inf=60.0;
sigma=(np.log(s0)-np.log(s_inf))/(s0+i0-s_inf)
print("sigma=",sigma)
S=np.array([155, 153, 139, 101])
I=(s0+i0)-S+1/sigma*np.log(S/s0)
print("所求的解为：\n",I)
````

</details>

#### Pex8_4 · Python · 847f5b8d

- 归属算法：常微分方程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于常微分方程中的“核心算法与辅助函数”。
- **执行主线**：定义状态导数并进行常微分方程数值积分。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fb4e6e3f31e83122c72e88647d07c3ed10801440a783bbf9673e28f09ad96d7d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_4.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_4.py
from scipy.integrate import odeint
from numpy import arange
dy=lambda y, x: -2*y+x**2+2*x
x=arange(1, 10.5, 0.5)
sol=odeint(dy, 2, x)
print("x={}\n对应的数值解y={}".format(x, sol.T))
````

</details>

#### Pex8_5 · Python · 70c68866

- 归属算法：常微分方程
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于常微分方程中的“结果绘图与展示”。
- **执行主线**：定义状态导数并进行常微分方程数值积分；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `Pfun`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`c8f29eaf47fcb0d6f76b0c082fedb83b6484e11f0dbc6f512a7ebf4a724754cf`
- 语言：Python
- 符号：`Pfun`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_5.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_5.py
from scipy.integrate import odeint
from sympy.abc import t
import numpy as np
import matplotlib.pyplot as plt
def Pfun(y,x):
    y1, y2=y;
    return np.array([y2, -2*y1-2*y2])
x=np.arange(0, 10, 0.1)  #创建时间点
sol1=odeint(Pfun, [0.0, 1.0], x)  #求数值解
plt.rc('font',size=16); plt.rc('font',family='SimHei')
plt.plot(x, sol1[:,0],'r*',label="数值解")
plt.plot(x, np.exp(-x)*np.sin(x), 'g', label="符号解曲线")
plt.legend(); plt.savefig("figure8_5.png"); plt.show()
````

</details>

#### Pex8_6 · Python · c7b0adfa

- 归属算法：常微分方程
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于常微分方程中的“结果绘图与展示”。
- **执行主线**：定义状态导数并进行常微分方程数值积分；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `lorenz`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`c0c6c2909f9c5a2beece99106d60113b3edfe5c82e65a8731aa90d3c7565a693`
- 语言：Python
- 符号：`lorenz`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_6.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_6.py
from scipy.integrate import odeint
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
def lorenz(w,t):
    sigma=10; rho=28; beta=8/3
    x, y, z=w;
    return np.array([sigma*(y-x), rho*x-y-x*z, x*y-beta*z])
t=np.arange(0, 50, 0.01)  #创建时间点
sol1=odeint(lorenz, [0.0, 1.0, 0.0], t)  #第一个初值问题求解
sol2=odeint(lorenz, [0.0, 1.0001, 0.0], t)  #第二个初值问题求解
plt.rc('font',size=16); plt.rc('text',usetex=True)
ax1=plt.subplot(121,projection='3d')
ax1.plot(sol1[:,0], sol1[:,1], sol1[:,2],'r')
ax1.set_xlabel('$x$'); ax1.set_ylabel('$y$'); ax1.set_zlabel('$z$')
ax2=plt.subplot(122,projection='3d')
ax2.plot(sol1[:,0]-sol2[:,0], sol1[:,1]-sol2[:,1], sol1[:,2]-sol2[:,2],'g')
ax2.set_xlabel('$x$'); ax2.set_ylabel('$y$'); ax2.set_zlabel('$z$')
plt.savefig("figure8_6.png", dpi=500); plt.show()
print("sol1=",sol1, '\n\n', "sol1-sol2=", sol1-sol2)
````

</details>

#### Pex15_3 · Python · 8de3a7bd

- 归属算法：常微分方程
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于常微分方程中的“预测与推断”。
- **执行主线**：定义状态导数并进行常微分方程数值积分。
- **调用方式**：优先调用 `Pfun`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`1261b379a05bc5c26ab95c9f8bf6b7c25b66daa1b17fcd393113ca0007e97706`
- 语言：Python
- 符号：`Pfun`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/15第15章  灰色系统预测(Python 程序及数据)/Pex15_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex15_3.py
import numpy as np
from scipy.integrate import odeint
a=np.loadtxt("Pdata15_3.txt")  #加载表中的后4列数据
n=a.shape[0]  #观测数据的个数
x10=a[:,0]; x20=a[:,1]; x30=a[:,2]; x40=a[:,3]
x11=np.cumsum(x10); x21=np.cumsum(x20)
x31=np.cumsum(x30); x41=np.cumsum(x40)
z1=(x11[:-1]+x11[1:])/2.; z2=(x21[:-1]+x21[1:])/2.
z3=(x31[:-1]+x31[1:])/2.; z4=(x41[:-1]+x41[1:])/2.
B1=np.c_[z1,np.ones((n-1,1))]
u1=np.linalg.pinv(B1).dot(x10[1:]); print(u1)
B2=np.c_[z1,z2]
u2=np.linalg.pinv(B2).dot(x20[1:]); print(u2)
B3=np.c_[z3,np.ones((n-1,1))];
u3=np.linalg.pinv(B3).dot(x30[1:]); print(u3)
B4=np.c_[z1,z3,z4]
u4=np.linalg.pinv(B4).dot(x40[1:]); print(u4)
def Pfun(x,t):
    x1, x2, x3, x4 = x;
    return np.array([u1[0]*x1+u1[1], u2[0]*x1+u2[1]*x2,
           u3[0]*x3+u3[1], u4[0]*x1+u4[1]*x3+u4[2]*x4])
t=np.arange(0, 14);
X0=np.array([7.1230,0.7960,13.1080,27.475])
s1=odeint(Pfun, X0, t); s2=np.diff(s1,axis=0)
xh=np.vstack([X0,s2])
cha=a-xh[:-1,:]  #计算残差
delta=np.abs(cha/a)  #计算相对误差
maxd=delta.max(0)  #计算每个指标的最大相对误差
pre=xh[-1,:]; print("最大相对误差：",maxd,"\n预测值为：",pre)
````

</details>

#### Pex15_4_1 · Python · b53a9cb0

- 归属算法：常微分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#常微分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于常微分方程中的“模型求解”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2bed16545e8823e5b1847b0c15dbba8eb650fb687e302d7710102c93d14d346d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/15第15章  灰色系统预测(Python 程序及数据)/Pex15_4_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex15_4_1.py
import numpy as np
from sympy import Function, diff, dsolve, symbols, solve,exp
x0=np.array([41, 49, 61, 78, 96, 104])
n=len(x0); x1=np.cumsum(x0)  #计算1次累加序列
ax0=np.diff(x0)  #计算一次累减序列
z=0.5*(x1[1:]+x1[:-1])  #计算均值生成序列
B=np.c_[-x0[1:],-z,np.ones((n-1,1))]
u=np.linalg.pinv(B).dot(ax0)
p=np.r_[1,u[:-1]]  #构造特征多项式
r=np.roots(p)  #求特征根
xts=u[2]/u[1]  #常微分方程的特解
c1,c2,t=symbols('c1,c2,t'); eq1=c1+c2+xts-41;
eq2=c1*np.exp(5*r[0])+c2*np.exp(5*r[1])+xts-429
c=solve([eq1,eq2],[c1,c2])
s=c[c1]*exp(r[0]*t)+c[c2]*exp(r[1]*t)+xts  #微分方程的符号解
xt1=[]
for i in range(6): xt1.append(s.subs({t:i}))
xh0=np.r_[xt1[0],np.diff(xt1)]
cha=x0-xh0  #计算残差
delta=np.abs(cha)/x0  #计算相对误差
print(xt1,'\n------------\n',xh0,'\n------------\n',
      cha,'\n--------------\n',delta)
````

</details>

### 微分与差分方程 · 实现

#### Pex8_1 · Python · beb2bb81

- 归属算法：微分与差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“模型求解”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5435dccb6efa534e7d8d685c36dd58dfa0d5bf2bf4ed0100768f07f77206ffaa`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_1.py
from sympy.abc import x
from sympy import diff, dsolve, simplify, Function
y=Function('y')
eq=diff(y(x),x,2)+2*diff(y(x),x)+2*y(x)  #定义方程
con={y(0): 0, diff(y(x),x).subs(x,0): 1}  #定义初值条件
y=dsolve(eq, ics=con)
print(simplify(y))
````

</details>

#### Pex8_10_1 · Python · fdd1ee45

- 归属算法：微分与差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“模型求解”。
- **执行主线**：执行插值或参数拟合并评价曲线。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`6a22a3ce143624818e87e183ec84a712207e994018300fb1009fb2f3e5e03d81`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_10_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_10_1.py
import numpy as np
from scipy.optimize import curve_fit
a=[]; b=[];
with open("Pdata8_10_1.txt") as f:    #打开文件并绑定对象f
    s=f.read().splitlines()  #返回每一行的数据
for i in range(0, len(s),2):  #读入奇数行数据
    d1=s[i].split("\t")
    for j in range(len(d1)):
        if d1[j]!="": a.append(eval(d1[j]))  #把非空的字符串转换为年代数据
for i in range(1, len(s), 2):  #读入偶数行数据
    d2=s[i].split("\t")
    for j in range(len(d2)):
        if d2[j] != "": b.append(eval(d2[j])) #把非空的字符串转换为人口数据
c=np.vstack((a,b))  #构造两行的数组
np.savetxt("Pdata8_10_2.txt", c)  #把数据保存起来供下面使用
x=lambda t, r, xm: xm/(1+(xm/3.9-1)*np.exp(-r*(t-1790)))
bd=((0, 200), (0.1,1000))  #约束两个参数的下界和上界
popt, pcov=curve_fit(x, a[1:], b[1:], bounds=bd)
print(popt); print("2010年的预测值为：", x(2010, *popt))
````

</details>

#### Pex8_11 · Python · 7921e5f8

- 归属算法：微分与差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“模型求解”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、文件结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4bd28ea0097973eac7d95ff641984b8b975407a20455a4c11dd417f274963643`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_11.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_11.py
import sympy as sp
sp.var('t',positive=True); sp.var('s')  #定义符号变量
sp.var('Y',cls=sp.Function)  #定义符号函数
g=4*t*sp.exp(t)
Lg=sp.laplace_transform(g,t,s)  #方程右端项的拉氏变换
d=s**4*Y(s)+2*s**2*Y(s)+Y(s)
de=d-Lg[0]    #定义取拉氏变换后的代数方程
Ys=sp.solve(de,Y(s))[0]  #求像函数
Ys=sp.factor(Ys)
yt=sp.inverse_laplace_transform(Ys,s,t)
print("y(t)=",yt); yt=yt.rewrite(sp.exp)
#这里的变换只是为了把解化成指数函数，并且不出现虚数
yt=yt.as_real_imag(); print("y(t)=",yt)
yt=sp.simplify(yt[0]); print("y(t)=",yt)
````

</details>

#### Pex8_2 · Python · f2c5f524

- 归属算法：微分与差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“模型求解”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`ee6d35e5673baf3e293f72555a655b98ac70ba170baf99f084203531f2120d96`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_2.py
from sympy.abc import x  #引进符号变量x
from sympy import Function, diff, dsolve, sin
y=Function('y')
eq=diff(y(x),x,2)+2*diff(y(x),x)+2*y(x)-sin(x)  #定义方程
con={y(0): 0, diff(y(x), x).subs(x,0): 1}  #定义初值条件
y=dsolve(eq, ics=con)
print(y)
````

</details>

#### Pex8_3_1 · Python · 09aef515

- 归属算法：微分与差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“模型求解”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2505811b0e50af81c5112d8d0bfc3457d8c9af47de9d5710d340e164905a613d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_3_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_3_1.py
import sympy as sp
t=sp.symbols('t')
x1,x2,x3=sp.symbols('x1,x2,x3',cls=sp.Function)
eq=[x1(t).diff(t)-2*x1(t)+3*x2(t)-3*x3(t),
    x2(t).diff(t)-4*x1(t)+5*x2(t)-3*x3(t),
    x3(t).diff(t)-4*x1(t)+4*x2(t)-2*x3(t)]
con={x1(0):1, x2(0):2, x3(0):3}
s=sp.dsolve(eq, ics=con); print(s)
````

</details>

#### Pex8_3_2 · Python · 14aed7f9

- 归属算法：微分与差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“模型求解”。
- **执行主线**：估计回归系数并生成拟合/预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`69bb52ecf4bfbd1840d4092f130fadc021b62577e63ef72d7db2328a849033b2`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_3_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_3_2.py
import sympy as sp
t=sp.symbols('t')
x1,x2,x3=sp.symbols('x1:4',cls=sp.Function)
x=sp.Matrix([x1(t),x2(t),x3(t)])
A=sp.Matrix([[2,-3,3],[4,-5,3],[4,-4,2]])
eq=x.diff(t)-A*x
s=sp.dsolve(eq,ics={x1(0):1,x2(0):2,x3(0):3})
print(s)
````

</details>

#### Pex8_7 · Python · e14fc86f

- 归属算法：微分与差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“模型求解”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b1d8dbe1996324a537bc2825916fa1d98c13c84d836a2f1b46258b0776d37e22`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_7.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_7.py
import sympy as sp
sp.var('t, k')  #定义符号变量t,k
u = sp.var('u', cls=sp.Function)  #定义符号函数
eq = sp.diff(u(t), t) + k * (u(t) - 24)  #定义方程
uu = sp.dsolve(eq, ics={u(0): 150}) #求微分方程的符号解
print(uu)
kk = sp.solve(uu, k)  #kk返回值是列表，可能有多个解
k0 = kk[0].subs({t: 10.0, u(t): 100.0})
print(kk, '\t', k0)
u1 = uu.args[1]  #提出符号表达式
u0 = u1.subs({t: 20, k: k0})  #代入具体值
print("20分钟后的温度为：", u0)
````

</details>

#### Pex8_8 · Python · f4ec5e0d

- 归属算法：微分与差分方程
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“模型求解”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`06be671104d1d1d0d95d5fc2821b19f2ba85e74affd3ce5eccc4103cc81631a3`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_8.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_8.py
import sympy as sp
sp.var('h')  #定义符号变量
sp.var('t', cls=sp.Function)  #定义符号函数
g = 9.8
eq = t(h).diff(h) -10000*sp.pi/0.62/sp.sqrt(2*g)*(h**(3/2)-2*h**(1/2))  #定义方程
t = sp.dsolve(eq, ics={t(1): 0}) #求微分方程的符号解
t = sp.simplify(t)
print(t.args[1].n(9))
````

</details>

#### Pex8_9 · Python · c5a55b7e

- 归属算法：微分与差分方程
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分与差分方程 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分与差分方程中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0d2b4107ccad46a14829de69bbb09db8764358ae3ccb67ac283b850fb2806f9e`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_9.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_9.py
from numpy import array
v0=array([45, 65, 80])
T0=1; L=4.5; I=9; mu=0.7; g=9.8
T=v0/(2*mu*g)+(I+L)/v0+T0
print(T)
````

</details>

### 微分方程建模 · 实现

#### F · MATLAB · e098218b

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `F`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6a301e82ad237332ae24e61ac013740b0c0509da79f98041aa345af6d1939dc0`
- 语言：MATLAB
- 符号：`F`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/F.m`

<details>
<summary>展开原始代码</summary>

````matlab
function dy=F(t,y);
dy=[y(2);y(3);3*y(3)+y(2)*y(1)];
````

</details>

#### anli6_1_1 · MATLAB · ec23034b

- 归属算法：微分方程建模
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“预测与推断”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`2a9e4b1de99b00f0fd57095181535cd28f85fcaa51cc425884b30d7fc391364b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/anli6_1_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=textread('data4.txt'); %把原始数据保存在纯文本文件data4.txt中
x=a([2:2:6],:)';   %提出人口数据
x=nonzeros(x);  %去掉后面的零，并变成列向量
t=[1790:10:2000]';
t0=t(1); x0=x(1);
fun=@(cs,td)cs(1)./(1+(cs(1)/x0-1)*exp(-cs(2)*(td-t0))); %cs(1)=xm,cs(2)=r
cs=lsqcurvefit(fun,rand(2,1),t(2:end),x(2:end),zeros(2,1))
xhat=fun(cs,[t;2010])  %预测已知年代和2010年的人口
````

</details>

#### 相似实现组 · MATLAB · 6f16f0a9

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：anli6_1_2.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`3d384bd0069afaeac0c5ede5c001125b0b6e7140e30f582f3d8612a2cae37cdb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/anli6_1_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=textread('data4.txt'); %把原始数据保存在纯文本文件data4.txt中
x=a([2:2:6],:)'; x=nonzeros(x);
t=[1790:10:2000]';
a=[ones(21,1), -x(2:end)]; 
b=diff(x)./x(2:end)/10;
cs=a\b;
r=cs(1), xm=r/cs(2)
````

</details>

##### 变体 2：anli6_1_3.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`7468b62bf741f4fd63c41dae067326c015d758d40545756cb006aff9d26b315a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/anli6_1_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=textread('data4.txt'); %把原始数据保存在纯文本文件data4.txt中
x=a([2:2:6],:)'; x=nonzeros(x);
t=[1790:10:2000]';
a=[ones(21,1), -x(1:end-1)]; 
b=diff(x)./x(1:end-1)/10;
cs=a\b;
r=cs(1), xm=r/cs(2)
````

</details>

#### anli6_2_1 · MATLAB · 3dd9f2f7

- 归属算法：微分方程建模
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`cf17b8c57cf031c57df886189dd73aca57c6f2674a6ce61bb0ceebb37e9da50c`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/anli6_2_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
syms m V rho g k
s=dsolve('m*D2s-m*g+rho*g*V+k*Ds','s(0)=0,Ds(0)=0');
s=subs(s,{m,V,rho,g,k},{239.46,0.2058,1035.71,9.8,0.6});
s=vpa(s,10)  %求位移函数
v=dsolve('m*Dv-m*g+rho*g*V+k*v','v(0)=0');
v=subs(v,{m,V,rho,g,k},{239.46,0.2058,1035.71,9.8,0.6});
v=vpa(v,7)  %求速度函数
y=s-90; 
tt=solve(y)   %求到达海底90米处的时间
vv=subs(v,tt)  %求到底海底90米处的速度
````

</details>

#### anli6_2_2 · MATLAB · f9f5ac33

- 归属算法：微分方程建模
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`72b258dbb963c62ce6d8d88dd841c3e2da25e4b9f3d9486dd23529a190eae205`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/anli6_2_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
syms m V rho g k t real
v=dsolve('m*Dv-m*g+rho*g*V+k*v^2','v(0)=0'); v=simple(v);
v=subs(v,{m,V,rho,g,k},{239.46,0.2058,1035.71,9.8,0.6});
v=simple(v); v=vpa(v,7)  %求速度函数系数的小数表达式
tt=solve(v-12.2)   %求时间的临界值T
s=int(v,0,tt)      %求位移的临界值
````

</details>

#### drop · MATLAB · 0bb9eeff

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `drop`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b7b46b67344aa135f74a34c94107cec714d5360f72284a35313f4c1abd2313df`
- 语言：MATLAB
- 符号：`drop`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/drop.m`

<details>
<summary>展开原始代码</summary>

````matlab
function yprime=drop(x,y);
yprime=[y(2);(y(1)-1)*(1+y(2)^2)^(3/2)];
````

</details>

#### dropbc · MATLAB · 7963688d

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `dropbc`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`949af44d242099718e02dcade802799ad9e6e982ebcaeb3e668b0d6e38734ce7`
- 语言：MATLAB
- 符号：`dropbc`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/dropbc.m`

<details>
<summary>展开原始代码</summary>

````matlab
function res=dropbc(ya,yb);
res=[ya(1);yb(1)];
````

</details>

#### dropinit · MATLAB · 21d68f34

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `dropinit`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fa0f90e357658ca18f3acaabf463af3cd24546ba552821b7436c6241af658a5c`
- 语言：MATLAB
- 符号：`dropinit`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/dropinit.m`

<details>
<summary>展开原始代码</summary>

````matlab
function yinit=dropinit(x);
yinit=[sqrt(1-x.^2);-x./(0.1+sqrt(1-x.^2))];
````

</details>

#### ex6_1 · MATLAB · 3872eabf

- 归属算法：微分方程建模
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e3fbe0fbd87ed32279cbce2cab57d0bca5758595008b2ff766d209e01928f542`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
diff_equ='x^2+y+(x-2*y)*Dy=0';
dsolve(diff_equ,'x')
````

</details>

#### ex6_11_1 · MATLAB · f939982f

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`07bf3f8b4ab2b275039df929ec251cb58bd7ed88b51b4293f90d124d60c4a290`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_11_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
solinit=bvpinit(linspace(-1,1,20),@dropinit);
sol=bvp4c(@drop,@dropbc,solinit);
fill(sol.x,sol.y(1,:),[0.7,0.7,0.7])
axis([-1,1,0,1])
xlabel('x','FontSize',12)
ylabel('h','Rotation',0,'FontSize',12)
````

</details>

#### ex6_11_2 · MATLAB · df1d6924

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e983b0c0d8d26fb7c7dd9a751b3d7f7bd05c8c39eaea882fc6b7d24273095c34`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_11_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
yprime=@(x,y)[y(2);(y(1)-1)*(1+y(2)^2)^(3/2)]; %定义一阶方程组的匿名函数
res=@(ya,yb)[ya(1);yb(1)]; %定义边值条件的匿名函数
yinit=@(x)[x.^2;2*x]; %定义初始猜测解的匿名函数，这里换了另外一个初始猜测解
solinit=bvpinit(linspace(-1,1,20),yinit); %给出初始猜测解的结构
sol=bvp4c(yprime,res,solinit); %计算数值解
fill(sol.x,sol.y(1,:),[0.7,0.7,0.7]) %填充解曲线
axis([-1,1,0,1])
xlabel('x','FontSize',12)
ylabel('h','Rotation',0,'FontSize',12)
````

</details>

#### ex6_2 · MATLAB · 558f6a36

- 归属算法：微分方程建模
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f5667824893058c4e3b28dd660ed535f5db124bf0e365d6ab2f3b46659b3e71e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
y=dsolve('D3y-D2y=x','y(1)=8,Dy(1)=7,D2y(2)=4','x')
````

</details>

#### ex6_3 · MATLAB · c8f56ee6

- 归属算法：微分方程建模
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`82ac1327e501a419774ea0bc75e39a14dde1bc08d271f9e5f8acd522aec922cd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_3.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/F.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
equ1='D2f+3*g=sin(x)';
equ2='Dg+Df=cos(x)';
[general_f,general_g]=dsolve(equ1,equ2,'x')  %求通解
[f,g]=dsolve(equ1,equ2,'Df(2)=0,f(3)=3,g(5)=1','x')
````

</details>

#### ex6_4 · MATLAB · 7bd9658e

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`3835b15ee599aa7f7ef41de7f1d0c7c842ed76d10def738a077b9f39ae00bb6b`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_4.m`

<details>
<summary>展开原始代码</summary>

````matlab
syms t
a=[2,1,3;0,2,-1;0,0,2];
x0=[1;2;1];
x=expm(a*t)*x0, pretty(x)
````

</details>

#### ex6_5 · MATLAB · 16b6ba71

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4e6ae89001705a743ea73e55e170abe49c12c5d33dc2987bfb60db5b11d5db63`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_5.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
syms t s
a=[1,0,0;2,1,-2;3,2,1];fs=[0;0;exp(s)*cos(2*s)];
x0=[0;1;1];
tx=int(expm(a*(t-s))*fs,s);  %先求不定积分
xstar=subs(tx,s,t)-subs(tx,s,0); %再求定积分，这样运行速度快
x=expm(a*t)*x0+xstar;
x=simple(x), pretty(x)
````

</details>

#### ex6_6 · MATLAB · c9492872

- 归属算法：微分方程建模
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于微分方程建模中的“模型求解”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4484c6e67a318ea80fd6a999660dcb39ef66e2753bd0db71752e2333514a2c3d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_6.m`

<details>
<summary>展开原始代码</summary>

````matlab
t=dsolve('Dt=10000*pi/sqrt(2*g)*(h^(3/2)-2*h^(1/2))','t(1)=0','h');
t=simple(t), pretty(t)
````

</details>

#### example11 · MATLAB · 98265ef9

- 归属算法：微分方程建模
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#微分方程建模 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于微分方程建模中的“核心算法与辅助函数”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `drop`、`dropbc`、`dropinit`、`example11`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`ae0011787d3f79b230ab3e9a1d509793b25e421e34cb0536e733064a683ceb2c`
- 语言：MATLAB
- 符号：`drop`, `dropbc`, `dropinit`, `example11`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/example11.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/drop.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/dropbc.m`
  - 被调用代码：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/dropinit.m`

<details>
<summary>展开原始代码</summary>

````matlab
function sol=example11;
solinit=bvpinit(linspace(-1,1,20),@dropinit);
sol=bvp4c(@drop,@dropbc,solinit);
fill(sol.x,sol.y(1,:),[0.7,0.7,0.7])
axis([-1,1,0,1])
xlabel('x','FontSize',12)
ylabel('h','Rotation',0,'FontSize',12)
 
function yprime=drop(x,y);
yprime=[y(2);(y(1)-1)*(1+y(2)^2)^(3/2)];
 
function res=dropbc(ya,yb);
res=[ya(1);yb(1)];
 
function yinit=dropinit(x);
yinit=[sqrt(1-x.^2);-x./(0.1+sqrt(1-x.^2))];
````

</details>

<!-- END AUTO-INTEGRATED-CODE -->
