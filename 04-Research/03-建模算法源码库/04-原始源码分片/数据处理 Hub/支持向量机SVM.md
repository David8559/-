---
type: generated-code-shard
status: generated
topic_hub: 数据处理 Hub
algorithm: 支持向量机SVM
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# 支持向量机SVM · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/05-数据处理方法/数据处理 Hub|数据处理 Hub]]
- 独立实现：6
- 原始来源：6
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

#### anli9_1 · MATLAB · 33386457

- 归属算法：支持向量机SVM
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#支持向量机SVM · 复习|支持向量机SVM · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于支持向量机SVM中的“数据读取与预处理”。
- **执行主线**：训练支持向量分类/回归模型并生成预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`fe00d8399ceec5eb381788a978ef4e4fc328eebe11edc80500e0004b68148017`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/09第9章/anli9_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
%原始数据cancerdata.txt可在网上下载，数据中的B替换成1，M替换成-1，X替换成2，删除了分割符*,替换后的数据命名成cancerdata2.txt
clc,clear
a=load('cancerdata2.txt');
a(:,1)=[];  %删除第一列病例号
gind=find(a(:,1)==1);  %读出良性肿瘤的序号
bind=find(a(:,1)==-1); %读出恶性肿瘤的序号
training0=a([1:500],[2:end]); %提出已知样本点的数据
training=training0'; 
[train,ps]=mapstd(training); %已分类数据标准化
group(gind)=1; group(bind)=-1;  %已知样本点的类别标号
group=group'; %转换成列向量
xa0=a([501:569],[2:end]); %提出待分类数据
xa=xa0'; xa=mapstd('apply',xa,ps); %待分类数据标准化
s=svmtrain(training',group, 'Method','SMO', 'Kernel_Function','quadratic') %使用序列最小化方法训练支持向量机的分类器，如果使用二次规划的方法训练支持向量机则无法求解
sv_index=s.SupportVectorIndices'  %返回支持向量的标号
beta=s.Alpha'  %返回分类函数的权系数
b=s.Bias  %返回分类函数的常数项
mean_and_std_trans=s.ScaleData %第1行返回的是已知样本点均值向量的相反数，第2行返回的是标准差向量的倒数
check=svmclassify(s,training');  %验证已知样本点
err_rate=1-sum(group==check)/length(group) %计算错判率
solution=svmclassify(s,xa'); %进行待判样本点分类
solution=solution' 
sg=find(solution==1)  %求待判样本点中的良性编号
sb=find(solution==-1) %求待判样本点中的恶性编号
````

</details>

#### ex9_1 · MATLAB · b216e494

- 归属算法：支持向量机SVM
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#支持向量机SVM · 复习|支持向量机SVM · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于支持向量机SVM中的“数据读取与预处理”。
- **执行主线**：训练支持向量分类/回归模型并生成预测。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`84c4ddceb4d2f821882472ef235bef4e79bada607141a9ae2b48e92c5121c2d9`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/09第9章/ex9_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a0=load('fenlei.txt'); %把表中x1...x8的所有数据保存在纯文本文件fenlei.txt中
a=a0'; b0=a(:,[1:27]); dd0=a(:,[28:end]); %提取已分类和待分类的数据
[b,ps]=mapstd(b0); %已分类数据的标准化
dd=mapstd('apply',dd0,ps); %待分类数据的标准化
group=[ones(20,1); 2*ones(7,1)]; %已知样本点的类别标号
s=svmtrain(b',group) %训练支持向量机分离器
sv_index=s.SupportVectorIndices  %返回支持向量的标号
beta=s.Alpha  %返回分类函数的权系数
bb=s.Bias  %返回分类函数的常数项
mean_and_std_trans=s.ScaleData %第1行返回的是已知样本点均值向量的相反数，第2行返回的是标准差向量的倒数
check=svmclassify(s,b')  %验证已知样本点
err_rate=1-sum(group==check)/length(group) %计算已知样本点的错判率
solution=svmclassify(s,dd') %对待判样本点进行分类
````

</details>

#### Pex19_1_1 · Python · 6eae62de

- 归属算法：支持向量机SVM
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#支持向量机SVM · 复习|支持向量机SVM · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于支持向量机SVM中的“预测与推断”。
- **执行主线**：训练支持向量分类/回归模型并生成预测；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`415ea275e5760233344f2ddb1c077f0059769ee65384a93fcbef6588dfd67888`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/19第19章  支持向量机(Python 程序及数据)/Pex19_1_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex19_1.py
from sklearn import datasets, svm, metrics
from sklearn.model_selection import GridSearchCV
import numpy as np
iris=datasets.load_iris()
x=iris.data; y=iris.target
parameters = {'kernel':('linear','rbf'), 'C':[1,10,15]}
svc=svm.SVC(gamma='scale')
clf=GridSearchCV(svc,parameters,cv=5)  #cv为交叉验证参数，为5折
clf.fit(x,y)
print("最佳的参数值:", clf.best_params_)
print("score：",clf.score(x,y))
yh=clf.predict(x); print(yh) #显示分类的结果
print("预测准确率：",metrics.accuracy_score(y,yh))
print("误判的样本点为:",np.where(yh!=y)[0]+1)
````

</details>

#### Pex19_1_2 · Python · 4ddedec8

- 归属算法：支持向量机SVM
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#支持向量机SVM · 复习|支持向量机SVM · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于支持向量机SVM中的“预测与推断”。
- **执行主线**：训练支持向量分类/回归模型并生成预测；执行选择、交叉和变异的进化搜索。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`bb59460a94f160f27a18e1caa94cff6b5010223fee4617bcc449f868f9a80f24`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/19第19章  支持向量机(Python 程序及数据)/Pex19_1_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex19_1_2.py
from sklearn import datasets, svm
from sklearn.model_selection import GridSearchCV
import numpy as np
iris=datasets.load_iris()
x=iris.data; y=iris.target
clf=svm.LinearSVC(C=1,max_iter=10000)
clf.fit(x,y); yh=clf.predict(x); print(yh)
print("预测的准确率：",clf.score(x,y))
````

</details>

#### Pex19_2 · Python · edef5c4c

- 归属算法：支持向量机SVM
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#支持向量机SVM · 复习|支持向量机SVM · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于支持向量机SVM中的“结果绘图与展示”。
- **执行主线**：训练支持向量分类/回归模型并生成预测；重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e8a4a0a94502b2eacfd0e67337b336883db020d9d45b6b57fc2f4529669cb2a4`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/19第19章  支持向量机(Python 程序及数据)/Pex19_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex19_2.py
import numpy as np
import pylab as plt
from sklearn.svm import SVR 

np.random.seed(123)
x=np.arange(200).reshape(-1,1)
y=(np.sin(x)+3+np.random.uniform(-1,1,(200,1))).ravel()

model = SVR(gamma='auto'); print(model)
model.fit(x,y); pred_y = model.predict(x)
print("原始数据与预测值前15个值对比：")
for i in range(15): print(y[i],pred_y[i])

plt.rc('font',family='SimHei'); plt.rc('font',size=15)
plt.scatter(x, y, s=5, color="blue", label="原始数据")
plt.plot(x, pred_y, '-r*',lw=1.5, label="预测值")
plt.legend(loc=1)

score=model.score(x,y); print("score:",score)
ss=((y-pred_y)**2).sum()  #计算残差平方和
print("残差平方和：", ss)
plt.show()
````

</details>

#### SVM分类器代码 · MATLAB · cf767b4b

- 归属算法：支持向量机SVM
- 用途：数据读取与预处理
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/05-数据处理方法/数据处理 Hub#支持向量机SVM · 复习|支持向量机SVM · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于支持向量机SVM中的“数据读取与预处理”。
- **执行主线**：训练支持向量分类/回归模型并生成预测。
- **调用方式**：优先调用 `k`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`23a713a5d6f2b2fcb585294e5a0093ab73a15ee52fd4f82049946b81a4c3f72f`
- 语言：MATLAB
- 符号：`k`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/SVM分类器代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab

1.命令函数部分：

clear;%清屏
clc;
X =load('data.txt');
n = length(X);%总样本数量
y = X(:,4);%类别标志
X = X(:,1:3);
TOL = 0.0001;%精度要求
C = 1;%参数，对损失函数的权重
b = 0;%初始设置截距b
Wold = 0;%未更新a时的W(a)
Wnew = 0;%更新a后的W(a)
for i = 1 : 50%设置类别标志为1或者-1
    y(i) = -1;
end
a = zeros(n,1);%参数a
for i = 1 : n%随机初始化a,a属于[0,C]
        a(i) = 0.2;
end

%为简化计算，减少重复计算进行的计算
K = ones(n,n);
for i = 1 :n%求出K矩阵，便于之后的计算
    for j = 1 : n
        K(i,j) = k(X(i,:),X(j,:));
    end
end
sum = zeros(n,1);%中间变量，便于之后的计算，sum(k)=sigma a(i)*y(i)*K(k,i);
for k = 1 : n
    for i = 1 : n
        sum(k) = sum(k) + a(i) * y(i) * K(i,k);
    end
end

while 1%迭代过程
    
%启发式选点
n1 = 1;%初始化，n1,n2代表选择的2个点
n2 = 2;
%n1按照第一个违反KKT条件的点选择
while n1 <= n
    if y(n1) * (sum(n1) + b) == 1 && a(n1) >= C && a(n1) <=  0
         break;
    end
    if y(n1) * (sum(n1) + b) > 1 && a(n1) ~=  0
           break;
    end
    if y(n1) * (sum(n1) + b) < 1 && a(n1) ~=C
          break;
    end
     n1 = n1 + 1;              
end
%n2按照最大化|E1-E2|的原则选取
E1 = 0;
E2 = 0;
maxDiff = 0;%假设的最大误差
E1 = sum(n1) + b - y(n1);%n1的误差
for i = 1 : n
    tempSum = sum(i) + b - y(i);
    if abs(E1 - tempSum)> maxDiff
        maxDiff = abs(E1 - tempSum);
        n2 = i;
        E2 = tempSum;
    end
end

%以下进行更新
a1old = a(n1);
a2old = a(n2);
KK = K(n1,n1) + K(n2,n2) - 2*K(n1,n2);
a2new = a2old + y(n2) *(E1 - E2) / KK;%计算新的a2
%a2必须满足约束条件
S = y(n1) * y(n2);
if S == -1
    U = max(0,a2old - a1old);
    V = min(C,C - a1old + a2old);
else
    U = max(0,a1old + a2old - C);
    V = min(C,a1old + a2old);
end
if a2new > V
    a2new = V;
end
if a2new < U
    a2new = U;
end
a1new = a1old + S * (a2old - a2new);%计算新的a1
a(n1) = a1new;%更新a
a(n2) = a2new;

%更新部分值
sum = zeros(n,1);
for k = 1 : n
    for i = 1 : n
        sum(k) = sum(k) + a(i) * y(i) * K(i,k);
    end
end
Wold = Wnew;
Wnew = 0;%更新a后的W(a)
tempSum = 0;%临时变量
for i = 1 : n
    for j = 1 : n
    tempSum= tempSum + y(i )*y(j)*a(i)*a(j)*K(i,j);
    end
    Wnew= Wnew+ a(i);
end
Wnew= Wnew - 0.5 * tempSum;
%以下更新b：通过找到某一个支持向量来计算
support = 1;%支持向量坐标初始化
while abs(a(support))< 1e-4 && support <= n
    support = support + 1;
end
b = 1 / y(support) - sum(support);
%判断停止条件
if abs(Wnew/ Wold - 1 ) <= TOL
    break;
end
end
%输出结果：包括原分类，辨别函数计算结果，svm分类结果
for i = 1 : n
    fprintf('第%d点:原标号 ',i);
    if i <= 50
        fprintf('-1');
    else
        fprintf(' 1');
    end
    fprintf('    判别函数值%f      分类结果',sum(i) + b);
    if abs(sum(i) + b - 1) < 0.5
        fprintf('1\n');
    else if abs(sum(i) + b + 1) < 0.5
            fprintf('-1\n');
        else
            fprintf('归类错误\n');
        end
    end
end

2.名为f的功能函数部分:
function y = k(x1,x2)
    y = exp(-0.5*norm(x1 - x2).^2);
end

3.数据：
    0.8871   -0.3491    8.3376         0
    1.2519    1.2083    6.5041         0
   -1.1925    1.9338    1.8790         0
   -0.1277    2.4371    2.6971         0
    1.9697    3.0906    6.0391         0
    0.7603    0.8241    1.5323         0
    1.6382    3.5516    4.4694         0
    1.3438   -0.4539    5.9366         0
   -1.3361   -2.0201    1.6393         0
   -0.3886    3.3041    8.0450         0
   -0.6780    6.0196   -0.4084         0
    0.3552   -0.1051    1.2458         0
    1.6560    4.0786    0.8521         0
    0.8117    3.5451    6.8925         0
    1.4773   -1.9340    3.9256         0
   -0.0732   -0.9526    0.4609         0
    0.1521    4.3711    2.2600         0
    1.4820    0.7493    0.3475         0
    0.6140    4.5261    8.3776         0
    0.5721    3.3460    3.7853         0
    0.5269    4.1452    4.3900         0
    1.7879   -0.5390    2.5516         0
    0.9885    5.7625    0.1832         0
   -0.3318    2.4373   -0.6884         0
    1.3578    5.4709    3.4302         0
    2.7210   -1.1268    4.7719         0
    0.5039   -0.1025    2.3650         0
    1.1107    1.6885    3.7650         0
    0.7862    1.3587    7.3203         0
    1.0444   -1.5841    3.6349         0
    1.7795    1.7276    4.9847         0
    0.6710    1.4724   -0.5504         0
    0.2303    0.2720   -1.6028         0
    1.7089   -1.7399    4.8882         0
    1.0059    0.5557    5.1188         0
    2.3050    0.8545    2.8294         0
    1.9555    0.9898    0.3501         0
    1.7141    1.5413    3.8739         0
    2.2749    5.3280    4.9604         0
    1.6171    0.5270    3.3826         0
    3.6681   -1.8409    4.8934         0
    1.1964    1.8781    1.4146         0
    0.7788    2.1048    0.0380         0
    0.7916    5.0906    3.8513         0
    1.0807    1.8849    5.9766         0
    0.6340    2.6030    3.6940         0
    1.9069   -0.0609    7.4208         0
    1.6599    4.9409    8.1108         0
    1.3763    0.8899    3.9069         0
    0.8485    1.4688    6.7393         0
    3.6792    6.1092    4.9051         1
    4.3812    7.2148    6.1211         1
    4.3971    3.4139    7.7974         1
    5.0716    7.7253   10.5373         1
    5.3078    8.8138    6.1682         1
    4.1448    5.5156    2.8731         1
    5.3609    6.0458    4.0815         1
    4.7452    6.6352    1.3689         1
    6.0274    6.5397   -1.9120         1
    5.3174    3.0134    6.7935         1
    7.2459    3.6970    3.1246         1
    6.1007    8.1087    5.5568         1
    5.9924    6.9238    5.7938         1
    6.0263    5.3333    7.5185         1
    3.6470    8.0915    6.4713         1
    3.6543    7.2264    7.5783         1
    5.0114    6.5335    3.5229         1
    4.4348    7.4379   -0.0292         1
    3.6087    3.7351    3.0172         1
    3.5374    5.5354    7.6578         1
    6.0048    2.0691   10.4513         1
    3.1423    4.0003    5.4994         1
    3.4012    7.1536    8.3510         1
    5.5471    5.1372   -1.5090         1
    6.5089    5.4911    8.0468         1
    5.4583    6.7674    5.9353         1
    4.1727    2.9798    3.6027         1
    5.1672    8.4136    4.8621         1
    4.8808    3.5514    1.9953         1
    5.4938    4.1998    3.2440         1
    5.4542    5.8803    4.4269         1
    4.8743    3.9641    8.1417         1
    5.9762    6.7711    2.3816         1
    6.6945    7.2858    1.8942         1
    4.7301    5.7652    1.6608         1
    4.7084    5.3623    3.2596         1
    6.0408    3.3138    7.7876         1
    4.6024    8.3517    0.2193         1
    4.7054    6.6633   -0.3492         1
    4.7139    5.6362    6.2330         1
    4.0850   10.7118    3.3541         1
    6.1088    6.1635    4.2292         1
    4.9836    5.4042    6.7422         1
    6.1387    6.1949    2.5614         1
    6.0700    7.0373    3.3256         1
    5.6881    5.1363    9.9254         1
    7.2058    2.3570    4.7361         1
    4.2972    7.3245    4.7928         1
    4.7794    8.1235    3.1827         1
    3.9282    6.4092   -0.6339         1
````

</details>
