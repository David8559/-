---
type: generated-code-shard
status: generated
topic_hub: 预测模型 Hub
algorithm: 灰色预测GM
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# 灰色预测GM · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub|预测模型 Hub]]
- 独立实现：2
- 原始来源：2
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

使用少量样本的累加生成与白化方程进行趋势预测。

#### 灰色预测MATLAB程序 · MATLAB · ac1c557a

- 归属算法：灰色预测GM
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#灰色预测GM · 复习|灰色预测GM · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于灰色预测GM中的“预测与推断”。
- **执行主线**：按脚本或函数顺序完成数值计算并返回工作区结果。
- **调用方式**：优先调用 `gm1`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`10f8c4f6ec283d118c26ba49dc03231155fa535bf72608e58762adf3e1251d0c`
- 语言：MATLAB
- 符号：`gm1`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/推荐基础数模资料学习/十大算法/灰色预测/灰色预测MATLAB程序.txt`

<details>
<summary>展开原始代码</summary>

````matlab
灰色预测模型matlab程序 (2007-05-31 11:02:49) 
标签：灰色模型 gm(1 1) 二次拟合 matlab   分类：技术点滴 

%by allen @ 红嘴海鸥 
%灰色模型预测是在数据不呈现一定规律下可以采取的一种建模和预测方法，其预测数据与原始数据存在一定的规律相似性

%下面程序是灰色模型GM(1,1)程序二次拟合和等维新陈代谢改进预测程序,matlab6.5 ,使用本程序请注明，程序存储为gm1.m

%x = [5999,5903,5848,5700,7884];gm1(x);  测试数据 

%二次拟合预测GM(1,1)模型
function  gmcal=gm1(x)
sizexd2 = size(x,2);
%求数组长度

k=0;
for y1=x
    k=k+1;
    if k>1
        x1(k)=x1(k-1)+x(k);
        %累加生成
        z1(k-1)=-0.5*(x1(k)+x1(k-1));   
        %z1维数减1，用于计算B
        yn1(k-1)=x(k);
    else
        x1(k)=x(k);
    end
end
%x1,z1,k,yn1

sizez1=size(z1,2);
%size(yn1);
z2 = z1';
z3 = ones(1,sizez1)';

YN = yn1';   %转置
%YN

B=[z2 z3];
au0=inv(B'*B)*B'*YN;
au = au0';
%B,au0,au

afor = au(1);
ufor = au(2);
ua = au(2)./au(1);
%afor,ufor,ua 
%输出预测的  a u 和 u/a的值

constant1 = x(1)-ua;
afor1 = -afor;
x1t1 = 'x1(t+1)';
estr = 'exp';
tstr = 't';
leftbra = '(';
rightbra = ')';
%constant1,afor1,x1t1,estr,tstr,leftbra,rightbra

strcat(x1t1,'=',num2str(constant1),estr,leftbra,num2str(afor1),tstr,rightbra,'+',leftbra,num2str(ua),rightbra)
%输出时间响应方程

%******************************************************
%二次拟合

k2 = 0;
for y2 = x1
    k2 = k2 + 1;
    if k2 > k  
    else
        ze1(k2) = exp(-(k2-1)*afor);  
    end
end
%ze1

sizeze1 = size(ze1,2);
z4 = ones(1,sizeze1)';
G=[ze1' z4];
X1 = x1';
au20=inv(G'*G)*G'*X1;
au2 = au20';
%z4,X1,G,au20

Aval = au2(1);
Bval = au2(2);
%Aval,Bval
%输出预测的  A,B的值

strcat(x1t1,'=',num2str(Aval),estr,leftbra,num2str(afor1),tstr,rightbra,'+',leftbra,num2str(Bval),rightbra)
%输出时间响应方程

nfinal = sizexd2-1 + 1;
%决定预测的步骤数5  这个步骤可以通过函数传入

%nfinal = sizexd2 - 1 + 1;
%预测的步骤数 1

for  k3=1:nfinal
    x3fcast(k3) = constant1*exp(afor1*k3)+ua;
end
%x3fcast
%一次拟合累加值

for  k31=nfinal:-1:0
    if k31>1
        x31fcast(k31+1) = x3fcast(k31)-x3fcast(k31-1);
    else
        if k31>0
            x31fcast(k31+1) = x3fcast(k31)-x(1);
        else
            x31fcast(k31+1) = x(1);
        end
    end
   
end
x31fcast
%一次拟合预测值


for  k4=1:nfinal
    x4fcast(k4) = Aval*exp(afor1*k4)+Bval;
end
%x4fcast

for  k41=nfinal:-1:0
    if k41>1
        x41fcast(k41+1) = x4fcast(k41)-x4fcast(k41-1);
    else
        if k41>0
            x41fcast(k41+1) = x4fcast(k41)-x(1);
        else
            x41fcast(k41+1) = x(1);
        end
    end
   
end
x41fcast,x
%二次拟合预测值

%***精度检验p C************//////////////////////////////////
k5 = 0;
for y5 = x
    k5 = k5 + 1;
    if k5 > sizexd2  
    else
        err1(k5) = x(k5) - x41fcast(k5);  
    end
end
%err1
%绝对误差


xavg = mean(x);
%xavg
%x平均值

err1avg = mean(err1);
%err1avg
%err1平均值

k5 = 0;
s1total = 0 ;
for y5 = x
    k5 = k5 + 1;
    if k5 > sizexd2  
    else
        s1total = s1total + (x(k5) - xavg)^2;  
    end
end
s1suqare = s1total ./ sizexd2;
s1sqrt = sqrt(s1suqare);
%s1suqare,s1sqrt
%s1suqare  残差数列x的方差  s1sqrt 为x方差的平方根S1

k5 = 0;
s2total = 0 ;
for y5 = x
    k5 = k5 + 1;
    if k5 > sizexd2  
    else
        s2total = s2total + (err1(k5) - err1avg)^2;  
    end
end
s2suqare = s2total ./ sizexd2;
%s2suqare   残差数列err1的方差S2

Cval = sqrt(s2suqare ./ s1suqare);
Cval
%nnn = 0.6745 * s1sqrt
%Cval  C检验值

k5 = 0;
pnum = 0 ;
for y5 = x
    k5 = k5 + 1;
    if abs( err1(k5) - err1avg ) < 0.6745 * s1sqrt
        pnum = pnum + 1;
        %ppp = abs( err1(k5) - err1avg )     
    else
    end
end
pval = pnum ./ sizexd2;
pval
%p检验值

%arr1 = x41fcast(1:6)


%预测结果为区间范围  预测步长和数据长度可调整程序参数进行改进

 

----------程序为原创，引用请注明
````

</details>

#### 灰色预测算法代码 · MATLAB · cc673c84

- 归属算法：灰色预测GM
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#灰色预测GM · 复习|灰色预测GM · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于灰色预测GM中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`511876bdf4ad9fe07bac643604afd11362703afa5387f6db846ee2ac545e6e5a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/灰色预测算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
灰色预测步骤
（1）输入前期的小样本数据
（2）输入预测个数
（3）运行
y=input('请输入数据');
n=length(y);
yy=ones(n,1);
yy(1)=y(1);
for i=2:n
    yy(i)=yy(i-1)+y(i)
end
B=ones(n-1,2);
for i=1:(n-1)
    B(i,1)=-(yy(i)+yy(i+1))/2;
    B(i,2)=1;
end
BT=B';
for j=1:(n-1)
    YN(j)=y(j+1);
end
YN=YN';
A=inv(BT*B)*BT*YN;
a=A(1);
u=A(2);
t=u/a;
t_test=input('输入需要预测的个数');
i=1:t_test+n;
yys(i+1)=(y(1)-t).*exp(-a.*i)+t;
yys(1)=y(1);
for j=n+t_test:-1:2
    ys(j)=yys(j)-yys(j-1);
end
x=1:n;
xs=2:n+t_test;
yn=ys(2:n+t_test);
plot(x,y,'^r',xs,yn,'*-b');
det=0;
for i=2:n
    det=det+abs(yn(i)-y(i));
end
det=det/(n-1);
disp(['百分绝对误差为：',num2str(det),'%']);
    disp(['预测值为：',num2str(ys(n+1:n+t_test))]);
````

</details>
