---
type: generated-code-shard
status: generated
topic_hub: 数据处理 Hub
algorithm: KMeans聚类
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# KMeans聚类 · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/05-数据处理方法/数据处理 Hub|数据处理 Hub]]
- 独立实现：8
- 原始来源：8
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

#### 相似实现组 · Python · 5540a834

- 归属算法：KMeans聚类
- 用途：结果绘图与展示
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#KMeans聚类 · 复习|KMeans聚类 · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 变体 1：Pan11_2.py

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于KMeans聚类中的“结果绘图与展示”。
- **执行主线**：迭代更新簇分配和中心完成聚类；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`300341a9ccdbd606e4115309e510c178454fd78fdf0edbd1d2c25e0b74fd2eb2`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pan11_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pan11_2.py
import numpy as np; import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
a=pd.read_csv("iris.csv")
b=a.drop(labels="Species",axis=1)
md=KMeans(3); md.fit(b)  #构建模型并求解模型
labels=md.labels_ ;  centers=md.cluster_centers_
b['cluster']=labels  #数据框b添加一个列变量cluster
c=b.cluster.value_counts()  #各类频数统计
plt.rc('font',family='SimHei'); 
str1=['^r','.k','*b']; plt.subplot(121)
for i in range(len(centers)):
    plt.plot(b['Petal_Length'][labels==i],b['Petal_Width'][labels==i],
                str1[i],markersize=3,label=str(i))
    plt.legend(); plt.xlabel("(a)KMeans聚类结果")
plt.subplot(122); str2=['setosa','versicolour','virginica']
ind=np.c_[np.zeros((1,50)),np.ones((1,50)),2*np.ones((1,50))].flatten()
for i in range(3):
    plt.plot(b['Petal_Length'][ind==i],b['Petal_Width'][ind==i],
                str1[i],markersize=3,label=str2[i])
    plt.legend(); plt.xlabel("(b)原数据的类别")
plt.show()
````

</details>

##### 变体 2：Pex11_14.py

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于KMeans聚类中的“结果绘图与展示”。
- **执行主线**：迭代更新簇分配和中心完成聚类；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`7a02e751714f852179a384c9969da5522e84612857f39c91019a54c90dcc90b0`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pex11_14.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex11_14.py
import numpy as np; import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
a=pd.read_csv("iris.csv")
b=a.iloc[:,:-1]
md=KMeans(3); md.fit(b)  #构建模型并求解模型
labels=md.labels_ ;  centers=md.cluster_centers_
b['cluster']=labels  #数据框b添加一个列变量cluster
c=b.cluster.value_counts()  #各类频数统计
plt.rc('font',family='SimHei'); plt.rc('font',size=16)
str1=['^r','.k','*b']; plt.subplot(121)
for i in range(len(centers)):
    plt.plot(b['Petal_Length'][labels==i],b['Petal_Width']
             [labels==i], str1[i],markersize=3,label=str(i))
    plt.legend(); plt.xlabel("(a)KMeans聚类结果")
plt.subplot(122); str2=['setosa','versicolour','virginica']
ind=np.hstack([np.zeros(50),np.ones(50),2*np.ones(50)])
for i in range(3):
    plt.plot(b['Petal_Length'][ind==i],b['Petal_Width'][ind==i],
                str1[i],markersize=3,label=str2[i])
    plt.legend(loc='lower right'); plt.xlabel("(b)原数据的类别")
plt.show()
````

</details>

#### Pex11_13 · Python · 0c109b1b

- 归属算法：KMeans聚类
- 用途：模型求解
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#KMeans聚类 · 复习|KMeans聚类 · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于KMeans聚类中的“模型求解”。
- **执行主线**：迭代更新簇分配和中心完成聚类。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fe6cf8a3252d87f14941aa1b44afab34f0c8dad30581883320b55394dc3a2c4c`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pex11_13.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex11_13.py
import numpy as np
from sklearn.cluster import KMeans
a=np.array([[1, 3],[1.5, 3.2],[1.3, 2.8],[3, 1]])
md=KMeans(n_clusters=2)  #构建模型
md.fit(a)   #求解模型
labels=1+md.labels_   #提取聚类标签
centers=md.cluster_centers_   #提取聚类中心,每一行是一个聚类中心
print(labels,'\n-----------\n',centers)
````

</details>

#### Pz11_1 · Python · b5e06253

- 归属算法：KMeans聚类
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#KMeans聚类 · 复习|KMeans聚类 · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于KMeans聚类中的“结果绘图与展示”。
- **执行主线**：迭代更新簇分配和中心完成聚类；重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`51fd67b39bbe72155521d9c7add040c935d6746e75761db8c7435dc869d6830d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pz11_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pz11_1
import numpy as np  
import matplotlib.pyplot as plt; from sklearn.cluster import KMeans
mean=np.array([[-2, -2],[2, 2], [6,6]])
cov=np.array([[[0.3, 0], [0, 0.3]],[[0.4, 0], [0, 0.4]],[[0.5, 0], [0, 0.5]]])
x0=[]; y0=[];
for i in range(3):
    x,y=np.random.multivariate_normal(mean[i], cov[i],1000).T
    x0=np.hstack([x0,x]); y0=np.hstack([y0,y])
plt.rc('font',size=16); plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False); plt.subplot(121)
plt.scatter(x0,y0,marker='.')  #画模拟数据散点图
X=np.vstack([x0,y0]).T
np.save("Pzdata11_1.npy",X)  #保存数据供下面使用
TSSE=[]; K=10
for k in range(1,K+1):
    SSE = []
    md = KMeans(n_clusters=k); md.fit(X)
    labels = md.labels_; centers = md.cluster_centers_
    for label in set(labels):
        SSE.append(np.sum((X[labels == label,:]-centers[label,:])**2))
    TSSE.append(np.sum(SSE))
plt.subplot(122); plt.style.use('ggplot')
plt.plot(range(1,K+1), TSSE, 'b*-')
plt.xlabel('簇的个数'); plt.ylabel('簇内离差平方和之和'); plt.show()
````

</details>

#### Pz11_2 · Python · 412e2a7d

- 归属算法：KMeans聚类
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#KMeans聚类 · 复习|KMeans聚类 · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于KMeans聚类中的“结果绘图与展示”。
- **执行主线**：迭代更新簇分配和中心完成聚类；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`0a3a639cdb96f13b1113cb9d8b1bdbb3ff0e430e6892c51e2ef3efcc8a2a896b`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pz11_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pz11_2.py
import numpy as np; import matplotlib.pyplot as plt
from sklearn.cluster import KMeans; from sklearn import metrics
X=np.load("Pzdata11_1.npy")
S=[]; K=10
for k in range(2,K+1):
    md = KMeans(k); md.fit(X)
    labels = md.labels_;
    S.append(metrics.silhouette_score(X,labels,metric='euclidean'))  #计算轮廓系数
plt.rc('font',size=16); plt.rc('font',family='SimHei')
plt.plot(range(2,K+1), S, 'b*-')
plt.xlabel('簇的个数'); plt.ylabel('轮廓系数'); plt.show()
````

</details>

#### Pz11_3 · Python · 07f50dfd

- 归属算法：KMeans聚类
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#KMeans聚类 · 复习|KMeans聚类 · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于KMeans聚类中的“结果绘图与展示”。
- **执行主线**：迭代更新簇分配和中心完成聚类；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e678faaf90ea139446efdc28b77db5841243c778d22ae069b54450b0d1911efc`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/11第11章  多元分析Python 程序及数据）/Pz11_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pz11_3
import numpy as np; import matplotlib.pyplot as plt
from sklearn.cluster import KMeans; from sklearn import metrics
X=np.load("Pzdata11_1.npy")
TSSE=[]; K=10
for k in range(1,K+1):
    SSE = []
    md = KMeans(n_clusters=k); md.fit(X)
    labels = md.labels_; centers = md.cluster_centers_
    for label in set(labels):
        SSE.append(np.sum((X[labels == label,:]-centers[label,:])**2))
    TSSE.append(np.sum(SSE))
plt.rc('font',family='SimHei'); 
plt.style.use('ggplot'); plt.plot(range(1,K+1), TSSE, 'b*-')
plt.xlabel('簇的个数');
plt.ylabel('簇内离差平方和之和'); plt.show()
````

</details>

#### K-means算法代码 · MATLAB · 0d20ec54

- 归属算法：KMeans聚类
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#KMeans聚类 · 复习|KMeans聚类 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于KMeans聚类中的“结果绘图与展示”。
- **执行主线**：迭代更新簇分配和中心完成聚类；重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`1fec7baeb7d32a66b9d71559c9e51f77a9e70834f95d5809cda1c8d538610447`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/K-means算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function [Idx, Center] = K_means(X, xstart)
% K-means聚类
% Idx是数据点属于哪个类的标记，Center是每个类的中心位置
% X是全部二维数据点，xstart是类的初始中心位置

len = length(X);        %X中的数据点个数
Idx = zeros(len, 1);    %每个数据点的Id，即属于哪个类

C1 = xstart(1,:);       %第1类的中心位置
C2 = xstart(2,:);       %第2类的中心位置
C3 = xstart(3,:);       %第3类的中心位置

for i_for = 1:100
    %为避免循环运行时间过长，通常设置一个循环次数
    %或相邻两次聚类中心位置调整幅度小于某阈值则停止
    
    %更新数据点属于哪个类
    for i = 1:len
        x_temp = X(i,:);    %提取出单个数据点
        d1 = norm(x_temp - C1);    %与第1个类的距离
        d2 = norm(x_temp - C2);    %与第2个类的距离
        d3 = norm(x_temp - C3);    %与第3个类的距离
        d = [d1;d2;d3];
        [~, id] = min(d);   %离哪个类最近则属于那个类
        Idx(i) = id;
    end
    
    %更新类的中心位置
    L1 = X(Idx == 1,:);     %属于第1类的数据点
    L2 = X(Idx == 2,:);     %属于第2类的数据点
    L3 = X(Idx == 3,:);     %属于第3类的数据点
    C1 = mean(L1);      %更新第1类的中心位置
    C2 = mean(L2);      %更新第2类的中心位置
    C3 = mean(L3);      %更新第3类的中心位置
end

Center = [C1; C2; C3];  %类的中心位置


%演示数据
%% 1 random sample
%随机生成三组数据
a = rand(30,2) * 2;
b = rand(30,2) * 5;
c = rand(30,2) * 10;
figure(1);
subplot(2,2,1); 
plot(a(:,1), a(:,2), 'r.'); hold on
plot(b(:,1), b(:,2), 'g*');
plot(c(:,1), c(:,2), 'bx'); hold off
grid on;
title('raw data');

%% 2 K-means cluster
X = [a; b; c];  %需要聚类的数据点
xstart = [2 2; 5 5; 8 8];  %初始聚类中心
subplot(2,2,2);
plot(X(:,1), X(:,2), 'kx'); hold on
plot(xstart(:,1), xstart(:,2), 'r*'); hold off
grid on;
title('raw data center');

[Idx, Center] = K_means(X, xstart);
subplot(2,2,4);
plot(X(Idx==1,1), X(Idx==1,2), 'kx'); hold on
plot(X(Idx==2,1), X(Idx==2,2), 'gx');
plot(X(Idx==3,1), X(Idx==3,2), 'bx');
plot(Center(:,1), Center(:,2), 'r*'); hold off
grid on;
title('K-means cluster result');

disp('xstart = ');
disp(xstart);
disp('Center = ');
disp(Center);
````

</details>

#### 聚类分析代码 · MATLAB · 5ff88c8e

- 归属算法：KMeans聚类
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#KMeans聚类 · 复习|KMeans聚类 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于KMeans聚类中的“结果绘图与展示”。
- **执行主线**：迭代更新簇分配和中心完成聚类；重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e102f685cf5c84d8b0aa723df5ff7715877af227616a6acdd66f86de0bc17af8`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/聚类分析代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
聚类分析主要过程
（1）将数据展绘
% 随机生成3个中心以及标准差
s = rng(5,'v5normal');
mu = round((rand(3,2)-0.5)*19)+1;
sigma = round(rand(3,2)*40)/10+1;
X = [mvnrnd(mu(1,:),sigma(1,:),200);
mvnrnd(mu(2,:),sigma(2,:),300);
mvnrnd(mu(3,:),sigma(3,:),400)];
% 作图
P1 = figure;clf;
scatter(X(:,1),X(:,2),10,'ro');


（2）利用不同的算法进行带入分析
1 高斯混合聚类代码
高斯混合聚类的步骤：首先假设样本集具有一些规律，包括可以以α \alphaα参数作为比例分为k kk类且每类内符合高斯分布。
然后根据贝叶斯原理利用极大似然法同时求出决定分类比例的α \alphaα和决定类内高斯分布的μ \muμ、Σ \SigmaΣ。
最后将样本根据α \alphaα、μ \muμ、Σ \SigmaΣ再次通过贝叶斯原理求出样本该分在哪个簇。
整个步骤下来，
这种做法其实就是一种原型聚类：通过找到可以刻画样本的原型（α \alphaα、μ \muμ、Σ \SigmaΣ参数），迭代得到α \alphaα、μ \muμ、Σ \SigmaΣ参数的最优解。
将逻辑思路理清楚之后，高斯混合聚类并不复杂，只是因为它同时运用了高斯分布、贝叶斯公式、极大似然法和聚类的原理和思想，加上高数化简求解的步骤，而导致初读时比较容易感到有些混乱。
% 等高线
options = statset('Display','off');
gm = gmdistribution.fit(X,3,'Options',options);
P6 = figure;clf
scatter(X(:,1),X(:,2),10,'ro');
hold on
ezcontour(@(x,y) pdf(gm,[x,y]),[-15 15],[-15 10]);
hold off
P7 = figure;clf
scatter(X(:,1),X(:,2),10,'ro');
hold on
ezsurf(@(x,y) pdf(gm,[x,y]),[-15 15],[-15 10]);
hold off
view(33,24)
cluster1 = (cidx3 == 1);
cluster3 = (cidx3 == 2);
% 通过观察，K均值方法的第二类是gm的第三类
cluster2 = (cidx3 == 3);
% 计算分类概率
P = posterior(gm,X);
P8 = figure;clf
plot3(X(cluster1,1),X(cluster1,2),P(cluster1,1),'r.')
grid on;hold on
plot3(X(cluster2,1),X(cluster2,2),P(cluster2,2),'bo')
plot3(X(cluster3,1),X(cluster3,2),P(cluster3,3),'g*')
legend('第 1 类','第 2 类','第 3 类','Location','NW')
clrmap = jet(80); colormap(clrmap(9:72,:))
ylabel(colorbar,'Component 1 Posterior Probability')
view(-45,20);
% 第三类点部分概率值较低，可能需要其他数据来进行分析。
% 概率图
P9 = figure;clf
[~,order] = sort(P(:,1));
plot(1:size(X,1),P(order,1),'r-',1:size(X,1),P(order,2),'b-',1:size(X,1),P(order,3),'y-');
legend({'Cluster 1 Score' 'Cluster 2 Score' 'Cluster 3 Score'},'location','NW');
ylabel('Cluster Membership Score');
xlabel('Point Ranking');



2 K均值聚类算法
[cidx3,cmeans3,sumd3,D3] = kmeans(X,3,'dist','sqEuclidean');
P4 = figure;clf;
[silh3,h3] = silhouette(X,cidx3,'sqeuclidean');
P5 = figure;clf
ptsymb = {'bo','ro','go',',mo','c+'};
MarkFace = {[0 0 1],[.8 0 0],[0 .5 0]};
hold on
for i =1:3
clust = find(cidx3 == i);
plot(X(clust,1),X(clust,2),ptsymb{i},'MarkerSize',3,'MarkerFace',MarkFace{i},'MarkerEdgeColor','black');
plot(cmeans3(i,1),cmeans3(i,2),ptsymb{i},'MarkerSize',10,'MarkerFace',MarkFace{i});
end
hold off




3 分层聚类算法代码
又叫系统聚类，基本思路是将多个样本各作为一类，计算样本两两之间的距离，合并距离最近的两类成新的一类，
然后再计算距离，再合并，直到只有一类为止。层次聚类可以处理分类数据和定量数据，但处理速度相对较慢，
通常情况下需要结合相关结果进行主观判断聚类类别数量。
eucD = pdist(X,'euclidean');
clustTreeEuc = linkage(eucD,'average');
cophenet(clustTreeEuc,eucD);
P3 = figure;clf;
[h,nodes] =? dendrogram(clustTreeEuc,20);
set(gca,'TickDir','out','TickLength',[.002 0],'XTickLabel',[]);
````

</details>
