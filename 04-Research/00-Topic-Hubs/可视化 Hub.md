---
type: topic-hub
topic_tag: topic/可视化
keywords: [绘图, 可视化, 图表, matplotlib]
tags: [system/topic-hub, topic/可视化]
---

# 可视化 Hub

<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->
## 复习与调用指南

> [!summary] 阅读顺序
> 先用“快速选择”确定算法，再读复习卡掌握思想和步骤，最后跳到实现区选择代码。源码默认折叠；数据明细不在复习页展开。

### 快速选择

| 算法或用途 | 主要解决什么 | 独立实现 | 语言 |
|---|---|---:|---|
| [[#数字图像处理 · 复习|数字图像处理]] | 对像素矩阵进行增强、分割、特征提取或压缩。 | 38 | MATLAB, Python |
| [[#未标注例程·结果绘图与展示 · 复习|未标注例程·结果绘图与展示]] | 这组代码的文件名缺乏算法语义，静态分析表明主要承担“结果绘图与展示”。 | 6 | MATLAB |
| [[#绘图可视化 · 复习|绘图可视化]] | 把数据、模型结果和不确定性转成可解释图形。 | 46 | MATLAB, Python, SAS |

### 逐算法复习卡

#### 数字图像处理 · 复习

- **解决什么**：对像素矩阵进行增强、分割、特征提取或压缩。
- **核心思想**：通过空间域/频域变换和形态学操作提取结构。
- **标准流程**：读入与归一化 → 去噪/增强 → 分割 → 特征 → 评价 → 可视化。
- **何时调用**：输入本身是图像或空间栅格时使用。
- **最易出错**：参数依赖分辨率；必须保存原图并用客观指标评价。
- **库内覆盖**：38 个独立实现、38 个原始来源；语言：MATLAB, Python；其中 3 个识别到函数/类型入口。
- **优先阅读**：[[#小波特征提取算法代码 · MATLAB · 781278b4|小波特征提取算法代码]]、[[#元胞自动机程序 · MATLAB · 25b5459c|元胞自动机程序]]、[[#Pex20_15 · Python · 20f6974c|Pex20_15]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#数字图像处理 · 实现|跳转到源码实现区]]

#### 未标注例程·结果绘图与展示 · 复习

- **解决什么**：这组代码的文件名缺乏算法语义，静态分析表明主要承担“结果绘图与展示”。
- **核心思想**：先从函数、调用链和关键库识别计算角色，不在证据不足时强行归入具体模型。
- **标准流程**：确认入口 → 阅读参数和关键操作 → 分离硬编码 → 包装成函数 → 用最小样例验证。
- **何时调用**：仅在核对源码正文和输出后复用；优先把它作为辅助代码而非完整模型。
- **最易出错**：当前分类属于保守推断，运行验证后应补充准确算法名称。
- **库内覆盖**：6 个独立实现、6 个原始来源；语言：MATLAB；其中 0 个识别到函数/类型入口。
- **优先阅读**：[[#exA_5 · MATLAB · de652f6a|exA_5]]、[[#exA_14 · MATLAB · 43849aa9|exA_14]]、[[#exA_1_1 · MATLAB · 41dbe94d|exA_1_1]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#未标注例程·结果绘图与展示 · 实现|跳转到源码实现区]]

#### 绘图可视化 · 复习

- **解决什么**：把数据、模型结果和不确定性转成可解释图形。
- **核心思想**：图形编码必须与变量类型和比较任务匹配。
- **标准流程**：明确表达任务 → 选择图形 → 整理数据 → 统一尺度/配色 → 标注单位 → 导出论文规格。
- **何时调用**：在探索、诊断和论文表达三个阶段分别调用。
- **最易出错**：避免双轴误导、无单位、过度平滑和仅追求美观。
- **库内覆盖**：46 个独立实现、46 个原始来源；语言：MATLAB, Python, SAS；其中 21 个识别到函数/类型入口。
- **优先阅读**：[[#例5.12 · SAS · b7517368|例5.12]]、[[#example4_2 · SAS · dbbc54d8|example4_2]]、[[#ch27_fei_xian_xing_hui_gui3 · SAS · 605522b3|ch27_fei_xian_xing_hui_gui3]]（按核心算法证据、可复用入口与脚本完整度排序）
- **全部实现**：[[#绘图可视化 · 实现|跳转到源码实现区]]

### 通用调用检查表

1. 先确认当前问题是否满足复习卡中的适用条件。
2. 优先选择标有函数/类型入口的实现，脚本型代码先重构参数。
3. 用最小样例跑通，再替换为项目输入；不要一开始就接入完整题目。
4. 检查目标方向、变量单位、边界条件、随机种子和软件版本。
5. 保存运行环境、参数、结果与检验，验证通过后再进入项目正式代码。

<!-- END AUTO-HUB-STUDY-GUIDE -->

> 自动更新：2026-07-14 · 匹配笔记：2

## 相关笔记

- [[04-Research/01-建模基础理论/【数学建模入门】保姆级小白教程，没学过建模的看完这篇也能提交竞赛论文！]] — 相关度 9
- [[04-Research/03-建模算法源码库/代码资料索引]] — 相关度 5

## 邻接主题

- [[Topic Index]]
- [[数据处理 Hub]]
- [[论文写作 Hub]]
- [[Python Hub]]
- [[MATLAB Hub]]

<!-- BEGIN AUTO-INTEGRATED-CODE -->
## 源码实现库（按需调用）

> [!warning] 使用边界
> 以下源码保留全文与来源，但默认均未运行验证。数据依赖明细已从阅读页省略；调用时按代码理解卡完成参数化、最小样例和结果检验。来源显示为可复制路径，不直接调用 Windows 打开未知扩展名。

- 本 Hub 收录原始源码文件：90
- 精确去重后的独立实现：90
- 合并后的实现组：89

### 实现索引

| 算法或用途 | 独立实现 | 原始源码 |
|---|---:|---:|
| [[#数字图像处理 · 实现|数字图像处理]] | 38 | 38 |
| [[#未标注例程·结果绘图与展示 · 实现|未标注例程·结果绘图与展示]] | 6 | 6 |
| [[#绘图可视化 · 实现|绘图可视化]] | 46 | 46 |

### 数字图像处理 · 实现

#### 元胞自动机程序 · MATLAB · 25b5459c

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；执行归一化或标准化以统一变量尺度；把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `CA_sim_cloud`、`Clumsychild`、`Game_of_Life`、`evolvement`、`sands`、`sierpinski`、`sierpinski3_by_CA`、`sumfun`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`e730d380e9996c6fdb246b5ed85b30c22f64385e8d7a4c99cddb4fe3110c46c3`
- 语言：MATLAB
- 符号：`CA_sim_cloud`, `Clumsychild`, `Game_of_Life`, `evolvement`, `sands`, `sierpinski`, `sierpinski3_by_CA`, `sumfun`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/元胞自动机/元胞自动机程序.txt`

<details>
<summary>展开原始代码</summary>

````matlab
用Matlab实现元胞自动机（网上收集、转载）技术 2010-03-13 13:04:28 阅读121 评论0   字号：大中小 订阅 .

file:life.m

%% 初始化
m = 50;
X = zeros(m,m);
X(25,25) = 1;

   n = [m 1:m-1];
   e = [2:m 1];
   s = [2:m 1];
   w = [m 1:m-1];
   
  % 绘制初始图形
   [i,j] = find(X);
   figure(gcf);
   plothandle = plot(i,j,'.', ...
      'Color','blue', ...
      'MarkerSize',12);
   axis([0 m+1 0 m+1]);
%% 演化
   for k = 1:50
    %邻居数
    N = X(n,:) + X(s,:) + X(:,e) + X(:,w) + ...
     X(n,e) + X(n,w) + X(s,e) + X(s,w);
    %概率阵 
    RAND = rand(m);
    %换代
    X = X | (N.*RAND>0.99);
    %绘图
    [i,j] = find(X);
    set(plothandle,'xdata',i,'ydata',j)
    drawnow
    pause(0.2)
    k  
   end


file 2:

function sierpinski(n); 
% 使用元胞自动机生成sierpinski直角垫片 
% Example: 
%     sierpinski(256); 
% %算法见:孙博文,《分形算法与程序设计：用Visual C++实现》 
if nargin==0; 
   n=256; 
end 
X=ones(n); 
X(1,n-1)=0; 
H=imshow(X,[]); 
set(gcf,'doublebuffer','on'); 
k=1; 
while k<n; 
   X(k+1,1:end-1)=xor(X(k,1:end-1),X(k,2:end)); 
   X(k+1,n)=1; 
   set(H,'CData',X); 
   pause(0.1); 
   k=k+1; 
end 

file 3:
function CA_sim_cloud; 
% 使用元胞自动机模拟地球卫星的云图 
% 
% reference: 
% Piazza, E.; Cuccoli, F.; 
% Cellular Automata Simulation of Clouds in Satellite Images, 
% Geoscience and Remote Sensing Symposium, 2001. IGARSS '01. 
% IEEE 2001 International Volume 4,  9-13 July 2001 Page(s): 
% 1722 - 1724 vol.4 Digital Object Identifier 10.1109/IGARSS. 
% 2001.977050 
time=888;       % 程序执行步数 
M=240; 
N=320; 
S=round(rand(M,N)*15); 
p=[1,2,1,6,6,1,2,1]; 
p=sum(tril(meshgrid(p)),2)/20; 
rand('state',0); 
SS=S; 
R=rand(M,N); 
G=R; 
B=R; 
C=cat(3,R,G,B); 
fig=figure; 
set(fig,'DoubleBuffer','on'); 
mov = avifile('example2.avi'); 
cc=imshow(C,[]); 
set(gcf,'Position',[13 355 157 194]) 
x1=(1:3)+round(M/2);y1=(1:3)+round(N/3); 
x2=(1:3)+round(M/3);y2=(1:3)+round(N/2); 
x3=(1:3)+round(M/1.5);y3=(1:3)+round(N/2); 
q=0; 
qq=15/4; 
while q<time;            
  SS=zeros(M,N); 
  for k=1:15; 
      r=rand(M,N);   % 生成几率r          
      K=zeros(M+2,N+2); 
      T=(S-k>=0);    % 粒子数矩阵 
      K(2:end-1,2:end-1)=T; 
      SS=K(1:end-2,1:end-2).*(r<p(1))+... 
          K(1:end-2,2:end-1).*(r<p(2) & r>=p(1))+... 
          K(1:end-2,3:end).*(r<p(3) & r>=p(2))+... 
          K(2:end-1,1:end-2).*(r<p(4) & r>=p(3))+... 
          K(2:end-1,3:end).*(r<p(5) & r>=p(4))+... 
          K(3:end,1:end-2).*(r<p(6) & r>=p(5))+... 
          K(3:end,2:end-1).*(r<p(7) & r>=p(6))+... 
          K(3:end,3:end).*(r>=p(7))+SS; 
  end 
  S=SS;   %SS是粒子扩散后的分布 
  S(S>15)=15; 
  S(x1,y1)=15; 
  S(x2,y2)=15; 
  S(x3,y3)=15; % 粒子源赋值 
  G=(S<=7.5); 
  B=(S>qq); 
  R=(S>qq & S<=7.5); 
  C=double(cat(3,R,G,B)); 
  set(cc,'CData',C); 
  q=q+1; 
  pause(0.2); 
  title(['q=',num2str(q)]); 
  Nu(q)=sum(S(1:end)); 
  F = getframe(gca); 
  mov = addframe(mov,F); 
end 
mov = close(mov); 
figure; 
plot(Nu) 

file 4:
题目: 六边形的元胞自动机上的单粒子运动
摘要: 本程序在六边形的元胞自动机上模拟单粒子运动,算法是基于FHP规则.元胞自动机模拟地球卫星的云图 
关键词: 六边形, 元胞自动机, FHP规则

figure('Position',[15 30 997 658],'NumberTitle','off');
set(gcf,'name','     六边形的元胞自动机上的单粒子运动');
% Author's email: zjliu2001@163.com
% Reference:
% U. Frisch, B. Hasslacher, Y. Pomeau, Lattice-gas
% automata for the Navier-Stokes rquation, Phys. Rev. 
% Lett. 1986,56: 1505-1508
set(gcf,'DoubleBuffer','on');
axis square;box on;
set(gca,'XColor','r','YColor','r');
set(gca,'Position',[-0.01 0.11 0.775 0.815]);
L=17.5*0.1/sqrt(3);
axis([0,L,0,1]); hold on;
for p=0:.1:0.9;
    plot([0,(1-p)/sqrt(3)],[p,1],'k');
end
for p=0:0.1/sqrt(3):1;
    plot([p,min(p+1/sqrt(3),17.5*0.1/sqrt(3))],[0,min(1,(L-p)*sqrt(3))],'k');
end
for p=0:0.1/sqrt(3):1;
    plot([0,p],[p*sqrt(3),0],'k');
end
for p=0:9;
    plot([L-[0.05+p/10]/sqrt(3),L],[1,1-[0.05+p/10]],'k');
end
for p=0:0.05:1;
    plot([0,L],[p,p],'k');
end
po=plot(0.8/sqrt(3),0.5,'r.','markersize',24);
pz=0.8/sqrt(3)+0.5i; % the position of read point
A=pi/3*2;            % the movement direction of read point

gc=gca;
a1=axes('Position',[0.7,0.5,0.25,0.3]);
axis square;hold on;axis([0,1,0,1]);
plot([0.5+0.5i,(1+i)/2+0.4*exp(i*pi/3*2)]);
plot([0.5+0.5i,(1+i)/2+0.4*exp(i*pi/3)]);
plot([0.3,0.7],[0.5,0.5]);
text(0.2,0.8,'Y','fontsize',14);
text(0.73,0.8,'X','fontsize',14);
text(0.2,0.4,'Z','fontsize',14);
axes(gc);
dt=0.1/sqrt(3); k=0;

ses=['while k;',...
    'pz=pz+dt*exp(i*A);',...
    'if imag(pz)>0.99 | imag(pz)<0.01;',...        
    '    A=-A;',...
    'end;',...
    'if real(pz)>0.99 | real(pz)<0.01;',...
    '    A=-A-pi;',...
    'end;',...
    'set(po,''XData'',real(pz),''YData'',imag(pz));',...
    'pause(0.2);',...
    'end;'];
po1=uicontrol(gcf,'style','push',...
    'unit','normalized','position',[0.74,0.87,0.1,0.08],...
    'string','start','fontsize',18,'callback',[]);
set(po1,'callback',['k=~k;if k==1;',...
        'set(po1,''string'',''stop'');',...
        'else set(po1,''string'',''start'');',...
        'end;',ses]);

file 5:
% DLA
%%%%%来源：萝卜驿站 http://luobo.ycool.com/
clc;clear;close all;
S=ones(40,100);% state matrix
S(end,:)=0; % initial sttae
Ss=zeros(size(S)+[1,0]); % top line is origin of particle
Ss(2:end,:)=S; % showing matrix
N=size(S,2);
II=imagesc(Ss);axis equal;colormap(gray)
set(gcf,'DoubleBuffer','on');
while sum(1-S(1,:))<0.5;
    y=1;
    x=round(rand*[N-1]+1); % random position
    D=0;
    while D<0.5; % random travel
        r=rand;        
        if abs(x-1)<0.1;
            SL=1;
        else
            SL=S(y,x-1);
        end
        if abs(x-N)<0.1;
            SR=1;
        else
            SR=S(y,x+1);
        end
        if SL+SR+S(y+1,x)<2.5; % check the neighbor: left, right, under            
            D=1;
            S(y,x)=0; % stop in the position
        end
        if r<=1/3; % travel randomly
            x=x-1;
        elseif r<=2/3;
            x=x+1;
        else
            y=y+1;
        end
        Ss(2:end,:)=S;
        if x<0.5|x>N+0.5;
            D=1; % out of the range
        else            
            Ss(y,x)=0; % to show the moving particle
        end
        set(II,'CData',Ss); % to show
        pause(0.1);
    end
end

file 6:
function sands(N);
% 砂堆规则
% 参考书目：
% 物理系统的元胞自动机模拟
% 作者:(英国)肖帕德等著、祝玉学等译 

close all
figure;
set(gcf,'Doublebuffer','on');
D=ones(N);
D1=D;
[X,Y]=meshgrid(1:N);
Z=2*X-Y;
p=fix(9.5*N/21);
D(Z>p & Z<9+p)=0;
D(fix(end/2)+1:end,:)=1;
D=min(D,flipud(D).*D1);
D=min(D,fliplr(D).*D1);
D(end,fix(end/4.13):end-fix(end/4.13))=0;
D(end-1,fix(end/4.12):end-fix(end/4.12))=0;
D(end-2,fix(end/4.1):end-fix(end/4.1))=0;
% imshow(D,[])
 
% 以上是生成装砂的瓶子
B=ones(N);
B(Z>9+p)=0;
B(fix(end/2)+1:end,:)=1;
B(:,fix(end/2)+1:end)=1;
B=min(B,fliplr(B));
B(1:3,:)=1;
% figure;
set(gcf,'Doublebuffer','on');
% imshow(B,[])
% mov = avifile('example2900.avi');
kk=3800;
for k=1:kk;
    [B,Nu]=duisha(D,B);
    Bk=min(D,B);
    imshow(Bk,[])
    Ha(k)=Nu;
%     F = getframe(gca);
%     mov = addframe(mov,F);
end
% mov = close(mov);
figure;
plot(Ha)

function [Y,Nu]=duisha(D,B);
Dq=10*(1-D);
Bg=1-B+Dq;
% 研究砂子下落
S=zeros(size(B));
S1=S;
S2=S;
S(2:end,:)=Bg(2:end,:)-Bg(1:end-1,:);
S1(S==-1)=1;
S2(1:end-1,:)=S1(2:end,:);
Bg(S1==1)=~Bg(S1==1);
Bg(S2==1)=~Bg(S2==1);
% 研究砂子倾倒
clear S
clear S1
clear S2
S=zeros(size(B));
S1=S;
S2=S;
S(1:end-1,2:end-1)=Bg(1:end-1,2:end-1)+Bg(2:end,2:end-1)-Bg(2:end,1:end-2);
S1(S==2)=1;
S2(2:end,1:end-2)=S1(1:end-1,2:end-1);
Bg(S1==1)=0;
Bg(S2==1)=1;

clear S
clear S1
clear S2
S=zeros(size(B));
S1=S;
S2=S;
S(1:end-1,2:end-1)=Bg(1:end-1,2:end-1)+Bg(2:end,2:end-1)-Bg(2:end,3:end);
S1(S==2)=1;
S2(2:end,3:end)=S1(1:end-1,2:end-1);
Bg(S1==1)=0;
Bg(S2==1)=1;

Y=(1-Bg).*D;
Nu=prod(size(find(Y==0)));

file 7:
function CA_sim_cloud; 
% 使用元胞自动机模拟地球卫星的云图 
% 
% reference: 
% Piazza, E.; Cuccoli, F.; 
% Cellular Automata Simulation of Clouds in Satellite Images, 
% Geoscience and Remote Sensing Symposium, 2001. IGARSS '01. 
% IEEE 2001 International Volume 4,  9-13 July 2001 Page(s): 
% 1722 - 1724 vol.4 Digital Object Identifier 10.1109/IGARSS. 
% 2001.977050 
time=500;       % 程序执行步数 
M=240; 
N=320; 
S=zeros(M,N); 
p=[1,2,1,6,6,1,2,1]; 
p=sum(tril(meshgrid(p)),2)/20; 
rand('state',0); 
SS=S; 
R=1-S; 
G=S; 
B=S; 
C=cat(3,R,G,B); 
figure; 
cc=imshow(C,[]); 
x=round(M/2);y=(1:3)+round(N/3); 
q=0; 
while q<time;           
   SS=zeros(M,N); 
   for k=1:15; 
       r=rand(M,N);   % 生成几率r         
       K=zeros(M+2,N+2); 
       T=(S-k>=0);    % 粒子数矩阵 
       K(2:end-1,2:end-1)=T; 
       SS=K(1:end-2,1:end-2).*(r<p(1))+... 
           K(1:end-2,2:end-1).*(r<p(2) & r>=p(1))+... 
           K(1:end-2,3:end).*(r<p(3) & r>=p(2))+... 
           K(2:end-1,1:end-2).*(r<p(4) & r>=p(3))+... 
           K(2:end-1,3:end).*(r<p(5) & r>=p(4))+... 
           K(3:end,1:end-2).*(r<p(6) & r>=p(5))+... 
           K(3:end,2:end-1).*(r<p(7) & r>=p(6))+... 
           K(3:end,3:end).*(r>=p(7))+SS; 
   end 
   S=SS;   %SS是粒子扩散后的分布 
   S(S>15)=15; 
   S(x,y)=15; % 粒子源赋值 
   G=(S<=10); 
   B=(S>5); 
   R=(S>5 & S<=10); 
   C=double(cat(3,R,G,B)); 
   set(cc,'CData',C); 
   q=q+1; 
   pause(0.2); 
   title(['q=',num2str(q)]); 
   Nu(q)=sum(S(1:end)); 
end 
figure; 
plot(Nu) 
 


file 8:
生命游戏 (Came of Life)是J. H. Conway在20世纪60年代末设计的一种单人玩的计算机游戏(Garclner，M.，1970、1971)。他与现代的围棋游戏在某些特征上略有相似：围棋中有黑白两种棋子。生命游戏中的元胞有{"生"，"死"}两个状态 {0，1};围棋的棋盘是规则划分的网格，黑白两子在空间的分布决定双方的死活，而生命游戏也是规则划分的网格(元胞似国际象棋分布在网格内。而不象围棋的棋子分布在格网交叉点上)。根据元胞的局部空间构形来决定生死。只不过规则更为简单。下面介绍生命游戏的构成及规则: 
(1)元胞分布在规则划分的网格上； 
(2)元胞具有0，1两种状态，0代表"死"，l代表"生"； 
(3)元胞以相邻的8个元胞为邻居。即Moore邻居形式； 
(4)一个元胞的生死由其在该时刻本身的生死状态和周围八个邻居的状态 (确切讲是状态的和)决定: 
·在当前时刻，如果一个元胞状态为"生"，且八个相邻元胞中有两个或三个的状态为"生"，则在下--时刻该元胞继续保持为"生"，否则"死"去； 
·在当前时刻。如果一个元胞状态为"死"。且八个相邻元胞中正好有三个为"生"。则该元胞在下一时刻 "复活"。否则保持为"死"。 
尽管它的规则看上去很简单。但生命游戏是具有产生动态图案和动态结构能力的元胞自动机模型。它能产生丰富的、有趣的图案。生命游戏的优化与初始元胞状态值的分布有关，给定任意的初始状态分布。经过若干步的运算，有的图案会很快消失。而有的图案则固定不动，有的周而复始重复两个或几个图案，有的婉蜒而行。有的则保持图案定向移动，形似阅兵阵……，其中最为著名的是"滑翔机 (叫Glider)"的图案。 

matlab程序如下： 
% 其中黑点表示活着 
% 白点表示死亡状态 

function Game_of_Life(n) 
% 生命游戏 
% Example: 
%   Game_of_Life(100); 
if nargin==0; 
   n=100; 
end 
B=round(rand(n+2)); 
Z=B(2:end-1,2:end-1); 
H=imshow(Z,[]); 
set(gcf,'position',[241 132 560 420]) 
set(gcf,'doublebuffer','on'); 
xlabel('Please press "space" key and stop this program!',... 
 'fontsize',12,'color','r'); 
k=1; 
title('Game of life','color','b'); 
while k; 
  s=get(gcf,'currentkey'); 
  if strcmp(s,'space'); 
      clc;k=0; 
  end 
  A=sumfun(B); 
  X=zeros(n); 
  X(Z==1 & (A==2 | A==3))=1; 
  X(Z==0 & A==3)=1; 
  B(2:end-1,2:end-1)=X; 
  Z=X; 
  set(H,'CData',1-X); 
  pause(0.5); 
end 
figure(gcf); 
function S=sumfun(B); 
% 周围8个位置的和 
S=B(1:end-2,2:end-1)+... 
   B(3:end,2:end-1)+... 
   B(2:end-1,1:end-2)+... 
   B(2:end-1,3:end)+... 
   B(2:end-1,1:end-2)+... 
   B(1:end-2,3:end)+... 
   B(3:end,1:end-2)+... 
   B(3:end,3:end); 
 
file 9:
如果x([i-1,i,i+1],t)等于[0 0 1]或者[1 0 0]时，x(i,t+1)才等于1，其他情况x(i,t+1)等于0。 
也就是: 
本行      0 0 1     1 0 0    其它 
下一行      1          1         0 


function sierpinski3_by_CA(n); 
% 使用元胞自动机生成sierpinski直角垫片 
% Example: 
%     sierpinski3_by_CA(256); 
% %算法见:孙博文,《分形算法与程序设计：用Visual C++实现》 
if nargin==0; 
   n=256; 
end 
X=zeros(n); 
X(1,round(n/2))=1; 
H=imshow(X,[]); 
set(gcf,'doublebuffer','on'); 
k=1; 
while k<round(n/2); 
   X(k+1,2:end-1)=and(xor(X(k,1:end-2),X(k,3:end)),... 
       ~X(k,2:end-1)); 
   set(H,'CData',1-X); 
   pause(0.05); 
   k=k+1; 
end 
nm=round(n/2); 
k=1; 
while k<nm; 
   X(nm+k,1:end)=X(nm-k,1:end); 
   set(H,'CData',1-X); 
   pause(0.05); 
   k=k+1; 
end 
 
file 10:

function sierpinski(n); 
% 使用元胞自动机生成sierpinski直角垫片 
% Example: 
%     sierpinski(256); 
% %算法见:孙博文,《分形算法与程序设计：用Visual C++实现》 
if nargin==0; 
   n=256; 
end 
X=ones(n); 
X(1,n-1)=0; 
H=imshow(X,[]); 
set(gcf,'doublebuffer','on'); 
k=1; 
while k<n; 
   X(k+1,1:end-1)=xor(X(k,1:end-1),X(k,2:end)); 
   X(k+1,n)=1; 
   set(H,'CData',X); 
   pause(0.1); 
   k=k+1; 
end 

file 11:
function Clumsychild(c1,m); 
% 实现元胞以固定的概率向相邻的4个元胞扩散 
% Example: 
%    Clumsychild(0.1,0.1); 
% Author's email:zjliu2001@163.com 
N=100;rand('state',0); 
A=randperm(N^2); 
S=zeros(N); 
S(A(1:3000))=3;      % 30%的位置是状态3 
S(A(3001:5000))=1;   % 20%的位置是状态1 
S(A(5001:6000))=2;   % 10%的位置是状态2 
clear A;close all; 
figure('position',[159 42 567 427]); 
imagesc([1:4]') 
set(gca,'YAxisLocation','right'); 
set(gca,'YAxisLocation','right'); 
set(gca,'position',[0.8,0.1,0.1,0.8]) 
set(gca,'position',[0.84,0.12,0.1,0.8]) 
set(gca,'xtick',[]); 
set(gca,'ytick',[1:4]); 
set(gca,'yticklabel',num2str([0:3]')); 
axes('position',[0.06,0.12,0.7,0.8]); 
H=imagesc(S); 
set(gcf,'position',[159 42 485 427]); 
set(gcf,'doublebuffer','on'); 
xlabel('Please press "space" key and stop this program!',... 
 'fontsize',12,'color','r'); 
title(['c1=',num2str(c1),'  m=',num2str(m)]); 
k=1; 
while k 
  pause(0.5); 
  s=get(gcf,'currentkey'); 
  if strcmp(s,'space'); 
      clc;k=0; 
  end 
  S=evolvement(S,c1,m); 
  set(H,'CData',S); 
end 
figure(gcf); 

function S=evolvement(S,c1,m); 
P=zeros(size(S)); 
Da=rand(size(S)); 
Da(Da>1-c1)=1; 
Da(Da<1-c1)=0; 
P(S==1 | S==2)=1; 
R=round(rand(size(S))+1); 
P=P.*R.*Da; 
V=round(rand(size(S))*3)+1; 
V=V.*P; % V是速度方向: 
                 %   1 --- up 
                 %   2 --- down 
                 %   3 --- left 
                 %   4 --- right 
V(1,V(1,1:end)==1)=0; 
V(end,V(end,1:end)==2)=0; 
V(V(1:end,1)==3,1)=0; 
V(V(1:end,end)==4,end)=0; 
% 产生后代 
[x,y]=find(V==1); 
DD=zeros(size(S)); 
DD(x-1,y)=P(x-1,y); 
S(S==0 | S==2 & DD==1)=1; 
S(S==0 & DD==2)=2; 

[x,y]=find(V==2); 
DD=zeros(size(S)); 
DD(x+1,y)=P(x+1,y); 
S(S==0 | S==2 & DD==1)=1; 
S(S==0 & DD==2)=2; 

[x,y]=find(V==3); 
DD=zeros(size(S)); 
DD(x,y-1)=P(x,y-1); 
S(S==0 | S==2 & DD==1)=1; 
S(S==0 & DD==2)=2; 

[x,y]=find(V==4); 
DD=zeros(size(S)); 
DD(x,y+1)=P(x,y+1); 
S(S==0 | S==2 & DD==1)=1; 
S(S==0 & DD==2)=2; 

Dr=rand(size(S)); 
S(S<3 & Dr<m)=0; 

file 12:
实现元胞以固定的概率向相邻的4个元胞扩散 zz问题，元胞自动机模拟地球卫星的云图 元胞以固定的概率向相邻的4个元胞扩散 zz问题，元胞自动机模拟地球卫星的云图 
萝卜 @ 2005-06-16 08:36

这个完整的元胞自动机模型如下： 
定义一个100×100的格子，每个元胞都有4个状态，即0，1，2，和3。其中如果处于0状态的 
话，我们认为这个格子是空白，且可以居住的。如果处于1状态，我们认为该点为强物种1所 
占有，如果处于2状态，我们认为该点为弱物种2所占有。而状态3表明了是一个被破坏了的地 
点，不能被任何物种占有。 
1）  如果处于状态1（或者2），那么该点的个体以c1（或者c2）的速度产生后代。 
2）  物种i的后代随机地到达上下左右四个元胞，如果这个后代是物种1的，那么他可以扩 
散到可以居住的元胞上（为空的元胞或者是被物种2所占有的元胞，即状态为0或者2）如果 
这个后代是物种2的，那么他只能扩散到空白且可以居住的元胞中。而如果后代扩散到被毁 
坏的元胞（状态为3）的，那么将会失败。 
3）  如果一个元胞处于1或者2的状态，这个元胞将以m的概率灭绝。 
也就是说，强物种以c1的速度产生后代，并将这个后代随机地发送到相邻的元胞中，强物种 
1的可以入侵到空白的元胞中，或者被弱物种2所占的地方。弱物种2以c2的速度产生后代， 
并把后代随机的送入其相邻的元胞中，弱物种的后代只能入侵到空白的元胞中（状态为0）。 
如果这个后代入侵到毁坏的元胞中（状态为3），那么这个入侵不成功，后代将灭绝。另外， 
对于2个物种来说，个体都有一个密度依赖的死亡率。 
对于元胞得初始状态，我们定义为： 
有D＝0.3的栖息地遭受破坏，也就是30％的格子（元胞）不能为物种所占领，即他们的状态 
为3，赋值为3。另外物种1的比例为0.2，即有20％的格子为物种1所占领，状态为1；物种2 
的比例为0.1，即有10％的格子为物种2所占领，状态为2；而空白的格子为0.4，即有40％的 
格子可供物种居住，但尚未被占领，其状态为0。
 

file 13:
仿真移动机器人避障的实验
萝卜 @ 2006-02-07 13:32


% 仿真移动机器人避障的实验
close all;clc;
axes('position',[0.1,0.15,0.56,0.7]);
% Author's email: zjliu2001@163.com
set(gcf,'DoubleBuffer','on');
N=50;
A=ones(N,N,3);
xn=round((N+1)/2);
yn=xn;
A(xn,yn,:)=0;
A(10:13,10:13,2:3)=0;
A(40:43,10:13,2:3)=0;
A(10:13,40:43,2:3)=0;
A(40:43,40:43,2:3)=0;
H=imshow(A);
k=0;
p=[1,-1,i,-i];
ss=['while k==1;',...
        't=round(3*rand)+1;x=real(p(t));',...
        'y=imag(p(t));A(xn,yn,:)=1;',...
        'xn=xn+x;yn=yn+y;',...
        'if xn<1 | xn>N;xn=mod(xn,N)+1;end;',...
        'if yn<1 | yn>N;yn=mod(xn,N)+1;end;',...
        'if A(xn,yn,2)==0;',...
        'xn=xn-x;yn=yn-y;A(xn,yn,:)=0;',...
        'else A(xn,yn,:)=0;end;',...
        'set(H,''CData'',A);',...
        'pause(0.2);end;'];
po1=uicontrol(gcf,'style','push',...
    'unit','normalized','position',[0.74,0.6,0.2,0.08],...
    'string','start','fontsize',12,'callback',[]);
set(po1,'callback',['k=~k;if k==1;',...
        'set(po1,''string'',''stop'');',...
        'else set(po1,''string'',''start'');',...
        'end;',ss]);
````

</details>

#### DCT_BASIC_FUNCTION · MATLAB · 052221c2

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`11b4ca79bccac1245c67ce2b7f1f5d49ff9f08ea09700b46d1c3e50a1726a74d`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/DCT_BASIC_FUNCTION.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear, T=dctmtx(8); %8×8的DCT变换矩阵
colormap('gray'); %设置颜色映射矩阵
for m = 1:8
for n = 1:8
subplot(8,8,(m-1)*8+n);
Y=zeros(8); Y(m,n)=1; %8×8矩阵中，只有第m行第n列为1，其余元素都为0
X = T'*Y*T; %做逆DCT变换
imagesc(X); %显示图像
axis square %画图区域是方形
axis off %不显示轴线和标号
end
end
````

</details>

#### anli13_1 · MATLAB · 40fba3c9

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`74e6360728375fb8a3e8628c97d9a081cb7a3da76f188695a95f64e50539d91a`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/anli13_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
a=imread('tu8.bmp'); ws1=size(a);    %读入保密图像，并计算维数
b=imread('tu9.bmp'); ws2=size(b);   %读入载体图像，并计算维数
nb=imresize(b,ws1(1:2));  %把载体图像变换成与保密图像同样大小
key=-0.400001;  %给出密钥，即混沌序列的初始值
L=max(ws1); x(1)=key; y(1)=key; alpha=1.4; beta=0.3;
for i=1:L-1     %生成两个混沌序列
     x(i+1)=1-alpha*x(i)^2+y(i); y(i+1)=beta*x(i);
end
x(ws1(1,1)+1:end)=[]; %删除x后面一部分元素
[sx,ind1]=sort(x); [sy,ind2]=sort(y); %对混沌序列按照从小到大排序
ea(ind1,ind2,:)=a; %打乱保密图像的行序和列序，生成加密图像矩阵ea
imshow(ea) %显示保密图像加密后得到的图像
nb2=bitand(nb,240); %载体图像与11110000(（二进制）=240(十进制）)逐位与运算
ea2=bitand(ea,240); %加密图像与11110000逐位与运算
ea2=ea2/16; %加密图像高4位移到低4位
da=bitor(nb2,ea2); %把加密图像嵌入载体图像的低4位，构造合成图像
da2=bitand(da,15)*16; %这里15（十进制）=00001111,提取加密图像的高4位，
da3=da2(ind1,ind2,:); %对加密图像进行解密
figure, subplot(1,2,1), imshow(da3) %显示提取的并解密以后的原图像
subplot(1,2,2),imshow(da) %显示嵌入加密图像的合成图像
````

</details>

#### ex13_1 · MATLAB · dc6b4ad9

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`2d406a1682a49422cb8fac547c4ad6ec6ade4ea8ed86133250e439f84b6422af`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
f=imread('tu1.bmp');  %读原图像
g=imadjust(f,[0; 1],[1; 0]); %进行图像翻转
subplot(1,2,1), imshow(f) %显示原图像
subplot(1,2,2), imshow(g) %显示翻转图像
````

</details>

#### ex13_3 · MATLAB · c6358084

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`f8a3d17f4f444eaa66efba4b2cd1afc94aca3584597bcd33db491cbc4ee3af6f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
f=imread('Lena.bmp'); %读原图像
f1=imnoise(f,'salt & pepper',0.02); %加椒盐噪声
g=medfilt2(f1); %进行中值滤波
subplot(1,3,1),imshow(f),title('原图像')
subplot(1,3,2),imshow(f1),title('被椒盐噪声污染的图像')
subplot(1,3,3),imshow(g),title('中值滤波图像')
````

</details>

#### ex13_4 · MATLAB · 6a4ec28a

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`07bd695fc05cc04de90d6c07013340961e71b2db769ebc94c49d7fb50b095b21`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_4.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
cm=imread('cameraman.tif'); %读入Matlab的内置图像文件
[n,m]=size(cm); %计算图像的维数
cf=fft2(cm); %进行傅氏变换
cf=fftshift(cf); %进行中心变换
u=[-floor(m/2):floor((m-1)/2)] %水平频率
v=[-floor(n/2):floor((n-1)/2)] %垂直频率
[uu,vv]=meshgrid(u,v); %频域平面上的网格结点
bl=1./(1+(sqrt(uu.^2+vv.^2)/15).^2); %构造1阶巴特沃兹低通滤波器
cfl=bl.*cf; %逐点相乘，进行低通滤波
cml=real(ifft2(cfl)); %进行逆傅氏变换，并取实部
%cml=ifftshift(cml);
cml=uint8(cml); %必须进行数据格式转换
subplot(1,2,1), imshow(cm)  %显示原图像
subplot(1,2,2), imshow(cml) %显示滤波后的图像
````

</details>

#### ex13_5 · MATLAB · 47bdb164

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`485e0df17a8a1923f2d936dae2a8c6fedd467103e46f006a6b5e91675bacd383`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_5.m`

<details>
<summary>展开原始代码</summary>

````matlab
I = imread('cameraman.tif'); %cameraman.tif是Matlab自带的图像文件
I = im2double(I); %数据转换成double类型
T = dctmtx(8); %T为8×8的DCT变换矩阵
dct = @(block_struct) T * block_struct.data * T'; %定义正DCT变换的隐函数，这里block_struct是Matlab内置的结构变量
B = blockproc(I,[8 8],dct); %做正DCT变换
mask = [1 1 1 1 0 0 0 0
1 1 1 0 0 0 0 0
1 1 0 0 0 0 0 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0]; %给出掩膜矩阵
B2 = blockproc(B,[8 8],@(block_struct) mask .* block_struct.data); %提取低频系数
invdct = @(block_struct) T' * block_struct.data * T; %定义逆DCT变换的隐函数
I2 = blockproc(B2,[8 8],invdct); %做逆DCT变换
subplot(1,2,1), imshow(I) %显示原图像
subplot(1,2,2), imshow(I2) %显示变换后的图像
````

</details>

#### ex13_6 · MATLAB · e6161b9c

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`4308f5b8184c442e6df74e75e1a1ee0cf6221783d80e4ecd1c4cf86ab95f91f6`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_6.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
f0=imread('tu3.bmp'); %读入图像
f1=double(f0); %数据转换成double类型
for k=1:3
g(:,:,k)=dct2(f1(:,:,k));  %对R，G，B各个分量分别作离散余弦变换
end
g(abs(g)<0.1)=0;  %把DCT系数小于0.1的变成0
for k=1:3
f2(:,:,k)=idct2(g(:,:,k)); %作逆DCT变换
end
f2=uint8(f2); %把数据转换成uint8格式
imwrite(f2,'tu4.bmp'); %把f2保存成bmp文件
subplot(1,2,1),imshow(f0)
subplot(1,2,2),imshow(f2)
````

</details>

#### ex13_7 · MATLAB · 061e20d7

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：使用奇异值分解提取低维结构；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`ec3edfba139b77703b8843e473ae0e6aa81e727eda04f6e73142f25145d9fc42`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_7.m`

<details>
<summary>展开原始代码</summary>

````matlab
f=imread('Lena.bmp');
f=double(f)   %uint8类型数据无法做奇异值分解，必须转换成double类型
[u,s,v]=svd(f); %进行奇异值分解,这里s为对角矩阵
s=diag(s); %提出对角矩阵的对角线元素，得到一个向量
smax=max(s), smin=min(s) %求最大奇异值和最小奇异值
s1=s; s1(21:end)=0; %只保留前20个大的奇异值，其它奇异值置0
s1=diag(s1);  %把向量变成对角矩阵
g=u*s1*v';    %计算压缩以后的图像矩阵
g=uint8(g);   %必须转换成原数据类，即转换成uint8格式
imwrite(g,'Lena2.bmp') %把压缩后的图像矩阵保存成bmp文件
subplot(1,2,1), imshow('Lena.bmp') %显示原图像
subplot(1,2,2), imshow(g) %显示压缩后的图像
figure, plot(s,'.','Color','k') %画出奇异值对应的点
````

</details>

#### ex13_8 · MATLAB · 41dc07aa

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：使用奇异值分解提取低维结构；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`1a02217e382436243525b36f538a1866abc7806a573f72bf130a8a7ae419ef60`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_8.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
A=imread('tu5.bmp'); %读入载体文件
W=imread('tu6.bmp');  %读入水印文件
[m1,m2,m3]=size(W);  %给出矩阵W的维数
A0=A([1:m1],[1:m2],:); %在矩阵A的左上角选取与W同样大小的子块
A0=double(A0); W=double(W); %进行数据类型转换
a=0.05; %嵌入强度因子为0.05
for i=1:3
    [U1{i},S1{i},V1{i}]=svd(A0(:,:,i)); %对载体R，G，B层分别进行奇异值分解
    A1(:,:,i)=S1{i}+a*W(:,:,i);  %计算A1矩阵
    [U2{i},S2{i},V2{i}]=svd(A1(:,:,i)); %对A1的各层进行奇异值分解
    A2(:,:,i)=U1{i}*S2{i}*V1{i}'; %计算A2矩阵
end
AW=A;  %整体水印合成图片初始化
AW([1:m1],[1:m2],:)=A2; %左上角替换成水印合成子块，水印嵌入完成
AW=uint8(AW); W=uint8(W); %变换回原来的数据类型
subplot(1,3,1), imshow(A) %显示载体图片
subplot(1,3,2), imshow(W) %显示水印图片
subplot(1,3,3), imshow(AW) %显示嵌入水印的合成图片
%以下是水印的提出
AWstar=imnoise(AW,'gaussian',0,0.01); %加入高斯噪声
A2star=AWstar([1:m1],[1:m2],:);  %提出子块
A2star=double(A2star); %进行数据类型转换
for i=1:3
    [U3{i},S2star{i},V3{i}]=svd(A2star(:,:,i)); %奇异值分解
    A1star(:,:,i)=U2{i}*S2star{i}*V2{i}';  %计算A1*
    Wstar(:,:,i)=(A1star(:,:,i)-S1{i})/a;  %计算W*
end
for i=1:3
Wstar(:,:,i)=medfilt2(Wstar(:,:,i));  %对提取水印的R,G,B层分别进行中值滤波
end
Wstar=uint8(Wstar); %进行类型转换
figure, subplot(1,2,1), imshow(AWstar) %显示被噪声污染的合成图片
subplot(1,2,2), imshow(Wstar) %显示提出的水印图片
````

</details>

#### ex13_9 · MATLAB · 7aee10ff

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`cda49005ea1c54f739270219ab2d58a7c6f21a58f58f371c6a42a9cfef7e78be`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/13第13章/ex13_9.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear 
a=imread('Lena.bmp'); %读入载体图像,图像的长和高都必须化成8的整数倍 
[M1,N1]=size(a); %计算载体图像的大小
a=im2double(a); %数据转换成double类型
knum1=M1/8; knum2=N1/8; %把载体图像划分成8×8的子块，高和长方向划分的块数
b0=imread('tu7.bmp'); %读入水印图像
b=im2double(b0); %数据转换成double类型
subplot(1,2,1), imshow(a)  %显示载体图像
subplot(1,2,2), imshow(b)  %显示水印图像
mask1=[1 1 1 1 0 0 0 0
       1 1 1 0 0 0 0 0
       1 1 0 0 0 0 0 0
       1 0 0 0 0 0 0 0
       0 0 0 0 0 0 0 0
       0 0 0 0 0 0 0 0
       0 0 0 0 0 0 0 0
       0 0 0 0 0 0 0 0]; %给出低频的掩膜矩阵
ind1=find(mask1==1); %低频系数的位置
mask2=[0 0 0 0 1 1 0 0
       0 0 0 1 1 0 0 0
       0 0 1 1 0 0 0 0
       0 1 1 0 0 0 0 0
       1 1 0 0 0 0 0 0
       1 0 0 0 0 0 0 0
       0 0 0 0 0 0 0 0
       0 0 0 0 0 0 0 0]; %给出中频的掩膜矩阵
ind2=find(mask2==1); %中频系数的位置，总共11个 
[M2,N2]=size(b); %计算水印图像的大小
L=M2*N2; %计算水印图像的像素个数
knum3=ceil(M2*N2/11); %水印图像按照11个元素1块，分的块数
b=b(:); b(L+1:11*knum3)=0; %水印图像数据变成列向量，后面不足一块的元素补0
T=dctmtx(8); %给出8×8的DCT变换矩阵 
ab=zeros(M1,N1); %合成图像的初始值 
k=0; %嵌入水印块计数器的初始值
for i=0:knum1-1  %该两层循环进行水印嵌入
    for j=0:knum2-1
        xa=a([8*i+1:8*i+8],[8*j+1:8*j+8]);  %提取载体图像的子块
        ya=T*xa*T';  %载体图像子块做DCT变换
        coef1=(mask1+mask2).*ya; %提取低频和中频系数，作为合成子块的初始值
        if k<knum3
        coef1(ind2)=coef1(ind2)+0.05*b(11*k+1:11*k+11); %在中频系数上嵌入水印子块的信息
        end
        ab([8*i+1:8*i+8],[8*j+1:8*j+8])=T'*coef1*T;%对合成子块进行逆DCT变换
        k=k+1;
    end
end
acha=ab-a; %提取合成图像和原图像的差图像；
k=0; tb=zeros(11*knum3,1); %提取水印图像的初始值
for i=0:knum1-1  %该两层循环进行水印提取
    for j=0:knum2-1
        xa2=acha([8*i+1:8*i+8],[8*j+1:8*j+8]);  %提取差图像的子块
        ya2=T*xa2*T';  %差图像子块做DCT变换
        coef2=mask2.*ya2; %提取差图像中频DCT系数
        if k<knum3
        tb(11*k+1:11*k+11)=20*coef2(ind2); %提取水印图像的像素值
        end
        k=k+1;
    end
end
tb(L+1:end)=[]; %把水印图像列向量的后面补的0删除
tb=reshape(tb,[M2,N2]); %把列向量变成矩阵
figure, subplot(1,2,1), imshow(ab) %显示水印合成图像
subplot(1,2,2), imshow(tb) %显示提取的水印图像
````

</details>

#### exA_35 · MATLAB · 894f1d1f

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`cd17ec586cbb29dde404cf0657960f5a1643a49ec61eb262bd2082871789526f`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/16附录A/exA_35.m`

<details>
<summary>展开原始代码</summary>

````matlab
a=imread('data6.bmp');
imshow(a)
imwrite(a,'data7.jpg');
figure, imshow('data7.jpg')
````

</details>

#### Pex20_1 · Python · 83f2b8f9

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`ad7ea9b499c6749a2507ef323622943cf0108a7e9350ad132fafc823e6f804df`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_1.py
import cv2
img=cv2.imread("Lena.bmp")
cv2.imshow('image',img)
cv2.imwrite('Lena.jpg',img)
````

</details>

#### Pex20_10 · Python · 4a6da3c1

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`186a0cb95cd22cc1fe39d18bcda0747ca5d687eb869dd1fa563b42976a3b88ad`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_10.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_10.py
from PIL import Image
a=Image.open('flower.jpg')  #读入图像
b=Image.open('logo.jpg')
print(a.size,b.size)  #显示图像的大小
c=b.resize((50,50))  #把图像缩小
a.paste(c,(20,20)); a.show()  #粘贴图像并显示
````

</details>

#### Pex20_11 · Python · db76d40f

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`6edc0a06cf5e21eff13089a87bae2621aa22b4c1251a6368a11787a7b8a3eb32`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_11.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_11.py
from PIL import Image
from numpy import array
a=Image.open('flower.jpg')  #读入图像
position=(100,100); b1=a.getpixel(position)  #读取像素
a.putpixel(position,tuple(array(b1)//2))  #修改像素
print(b1,a.getpixel(position))  #显示修改前后的像素值
````

</details>

#### Pex20_12 · Python · 1bcb3eff

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`d9de7d2a96b77ad5befe8bf69a43ad226b357d833c7e61c8927ba83eb3cf029b`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_12.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_12.py
from PIL import Image,ImageDraw
from numpy import array
a=Image.open('flower.jpg')  #读入图像
w,h=a.size  #读入图像的宽度和高度
b=ImageDraw.Draw(a)  #实例化Draw类
b.line(((0,0),(w-1,h-1)),fill=(255,0,0))
b.line(((w-1,0),(0,h-1)),fill=(255,0,0))
b.arc((0,0,w-1,h-1),0,360,fill=(255,0,0))
a.show(); a.save("figure20_12.png")  #显示并保存图像
````

</details>

#### Pex20_13 · Python · 46e3c249

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`624d9b652436e18ffde27a75e1e320f25436941d91ab13d3017cd837e18be44c`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_13.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_13.py
from PIL import Image,ImageDraw, ImageFont
a=Image.open('flower.jpg')  #读入图像
b=ImageDraw.Draw(a) #实例化Draw类
myfont=ImageFont.truetype("c:\\Windows\\Fonts\\simsun.ttc",48)
b.text((20,20),"美丽的花",font=myfont,fill=(255,0,0))
a.show(); a.save("figure20_13.png")
````

</details>

#### Pex20_14 · Python · f6cfb981

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e6491963ed207a28390d63b1ea429bcf861c4c9824a0183465d570598c603fbb`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_14.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_14.py
from PIL import Image,ImageFilter
from pylab import subplot, show, imshow
a=Image.open('flower.jpg')  #读入图像
b=a.filter(ImageFilter.CONTOUR)  #使用轮廓滤镜
subplot(121); imshow(a)
subplot(122); imshow(b); show()
````

</details>

#### Pex20_15 · Python · 20f6974c

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：重复随机采样并汇总模拟结果。
- **调用方式**：优先调用 `createLines`、`createPoints`、`drawStr`、`rndChar`、`rndColor`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、控制台/过程输出、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径；含随机过程但未发现固定随机种子。

- SHA-256：`82b349dd59be0d4a9f0f87e536c88f978533a58eb5c8b9dc5c59c01b8dafe4f8`
- 语言：Python
- 符号：`createLines`, `createPoints`, `drawStr`, `rndChar`, `rndColor`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_15.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_15.py
from PIL import Image,ImageDraw,ImageFont
from numpy.random import randint,random

def rndChar():  #产生随机字符
    s="abcdefghjkmnpqrstuwxyABCDEFGHJKMNPRSTUWXY23456789@#$%&"
    #去除易混淆的字符
    return s[randint(0,len(s))]

def rndColor():  #生成随机颜色
    return tuple(randint(64,256,3))

w=50*6; h=60  #设置图像的宽度和高度
a=Image.new('RGB',(w,h),(255,255,255))
font=ImageFont.truetype("c:\\Windows\\Fonts\\simsun.ttc",48)
b=ImageDraw.Draw(a)  #创建Draw对象

def createLines(n):  #绘制干扰线
    for i in range(n):
        begin=(randint(0,w),randint(0,h))  #起始点
        end=(randint(0,w),randint(0,h))    #结束点
        b.line([begin,end],fill=rndColor(),width=2)

def createPoints(rate):  #绘制干扰点
    for x in range(w):
        for y in range(h):
            if random(1)<=rate:
                b.point((x,y),fill=rndColor())

def drawStr():  #绘制字符
    Str=''
    for t in range(6):
        Chr=rndChar(); Str=Str+Chr
        b.text((50*t+10,5),Chr,font=font,fill=rndColor())
    print(Str)

createLines(6); createPoints(0.15); drawStr()
a.show(); a.save("figure20_15.png")





        
````

</details>

#### Pex20_16 · Python · 4cfc8822

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`da5d1410e979344ddb47aee63e1c829a988202fcdb6bc41e0ef690cf90df6c9b`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_16.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_16.py
from PIL import Image,ImageFont,ImageDraw
a=Image.open("玉龙雪山.jpg").convert('RGBA')
b=Image.new('RGBA',a.size, (0,0,0,0)) #(0,0,0,0)透明
fnt=ImageFont.truetype("simsun.ttc", 120) #设置字体
c=ImageDraw.Draw(b) #将新建的图像添入画板
c.text((b.size[0]-500,b.size[1]-150), "玉龙雪山",font=fnt,
  fill=(255,255,255,255))  #(255,255,255,255)为白色，不透明
d=Image.alpha_composite(a, b)  #合并两个图像
d.show(); d.save("figure20_16.png")
````

</details>

#### Pex20_17 · Python · c594e990

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`c96cff86f6cbbce5541c7b9bbf595a951ed07cf740d6987e41468c0f3afefa90`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_17.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_17.py
from PIL import Image
base=Image.open("flower.jpg").convert("RGBA")
watermark=Image.open("logo.jpg").convert("RGBA").resize((100,100))
width,height=base.size
mark_width,mark_height=watermark.size
position=(width-mark_width,height-mark_height)
transparent=Image.new('RGBA',(width, height),(0,0,0,0))
transparent.paste(base,(0,0))
transparent.paste(watermark,position,mask=watermark)
transparent.show()
transparent.save("figure20_17.png")
````

</details>

#### Pex20_18 · Python · d59c9380

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`4bbadca550cf847ec33e1ceda09606b0f184e0a905ca365b3f9c3c5dd0dddbaf`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_18.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_18.py
import qrcode
qr=qrcode.QRCode(
    version=1, #二维码的尺寸大小，取值范围为1-40
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  #二维码里每个格子的像素大小
    border=5  #边框的格子厚度，默认是4
)
qr.add_data("https://www.python.org/")  #设置二维码数据
qr.make(fit=True)  #启用二维码颜色设置
img=qr.make_image(fill_color="green", back_color="white")
img.show(); img.save("figure20_17.png")  #显示并保存二维码
````

</details>

#### Pex20_19 · Python · d5b3e407

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`3b792b378d7810fe00e395a24bb0538e53cbed604cc959a167c511c8551a8956`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_19.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_19.py
from PIL import Image
import qrcode
qr=qrcode.QRCode(
    version=2, 
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  
    border=1
)
qr.add_data("https://www.python.org/") 
qr.make(fit=True) 
img=qr.make_image().convert("RGBA")
w1,h1=img.size
factor=4; w2=w1//factor; h2=h1//factor

icon=Image.open("logo.jpg")
w3,h3=icon.size
if w3>w2: w3=w2
if h3>w2: h3=h2
icon=icon.resize((w3,h3))  #更改图标的尺寸
w4=(w1-w3)//2; h4=(h1-h3)//2
img.paste(icon,(w4,h4))  #将图标粘贴到二维码的中心位置
img.show(); img.save("figure20_19.png")
    
````

</details>

#### Pex20_2 · Python · 821c9290

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形、文件结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`35a2ce8cde94c052ee4d65eaf83bcfd0241279d6d7bbd75a4dbf8a356d4327d0`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_2.py
import cv2,os
os.mkdir("source")  #在当前目录下创建新目录source
video=cv2.VideoCapture("test.avi")
L=int(video.get(cv2.CAP_PROP_FRAME_COUNT))  #计算视频的帧数
for i in range(L-1):
    ret,frame=video.read()
    cv2.imshow('Frame',frame); cv2.waitKey(2)  #停顿2毫秒
    cv2.imwrite("source\\"+str(i)+".jpg",frame)
````

</details>

#### Pex20_20 · Python · 0e0b95ba

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e7688cc0d54a623299ee9f8f01f9d49ef789927da0b01c328e5c8ecedcf66a29`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_20.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_20.py
import glob, numpy as np
from PIL import Image
f = glob.glob("附件1\\*.bmp")  #读入附件1下所有bmp文件名称
n = len(f); a = np.array(Image.open(f[0]))
a = a.astype(float); jj = np.arange(1,n)
L1 = a[:,0]; L2 = a[:,-1]  #拼接的大图像左边界和右边界初始化

tind = [0]
cont_img = a
for i in range(n - 1):
    tcha1 = [];     tcha2 = []
    for j in jj:
        a2 = np.array(Image.open(f[j])).astype(float)
        e1 = a2[:, 0]; e2 = a2[:, -1]
        cha1 = abs(L1 - e2).sum(); cha2 = abs(L2 - e1).sum()
        tcha1.append(cha1) ; tcha2.append(cha2)  #左右边界的差异
    m1 = np.array(tcha1).min(); m2 = np.array(tcha2).min()

    if abs(L1 - 255.).sum() < 1:
        ind = np.where(tcha2 == m2)
        tind=np.hstack((tind, jj[ind]))  # 右拼接
        tt = np.array(Image.open(f[jj[ind[0][0]]])).astype(float)
        cont_img = np.hstack((cont_img, tt))
        L2 = tt[:, -1]; np.delete(jj, ind)
    elif abs(L2 - 255.).sum() < 1:
        ind = np.where(tcha1 == m1)
        tind = np.hstack((jj[ind], tind)) # 左拼接
        tt = np.array(Image.open(f[jj[ind[0][0]]])).astype(float)
        cont_img = np.hstack((tt,cont_img))
        L1 = tt[:, 0]; np.delete(jj, ind)
    elif m1 < m2:
        ind = np.where(tcha1 == m1)
        tind = np.hstack((jj[ind], tind)) # 左拼接
        tt = np.array(Image.open(f[jj[ind[0][0]]])).astype(float)
        cont_img = np.hstack((tt, cont_img))
        L1 = tt[:, 0]; np.delete(jj, ind)
    else:
        ind = np.where(tcha2 == m2)
        tind=np.hstack((tind, jj[ind]))  # 右拼接
        tt = np.array(Image.open(f[jj[ind[0][0]]])).astype(float)
        cont_img = np.hstack((cont_img, tt))
        L2 = tt[:, -1]; np.delete(jj, ind)
print(tind)  #显示各个图像的拼接排列次序
Image.fromarray(cont_img).show()
````

</details>

#### Pex20_3 · Python · c87fb291

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`46f7ec0e0643790d2e3ab7e9e00b6bad6f84e80392364e41114677c02541988e`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_3.py
import matplotlib.pyplot as plt, cv2 
img_BGR = cv2.imread('peppers.png')  # BGR 
plt.subplot(3,3,1); plt.imshow(img_BGR)
plt.axis('off'); plt.title('BGR')
img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
plt.subplot(3,3,2); plt.imshow(img_RGB)
plt.axis('off'); plt.title('RGB')
img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
plt.subplot(3,3,3); plt.imshow(img_GRAY)
plt.axis('off'); plt.title('GRAY')
img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
plt.subplot(3,3,4); plt.imshow(img_HSV)
plt.axis('off');plt.title('HSV')
img_YcrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)
plt.subplot(3,3,5); plt.imshow(img_YcrCb)
plt.axis('off'); plt.title('YcrCb')
img_HLS = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS)
plt.subplot(3,3,6); plt.imshow(img_HLS)
plt.axis('off'); plt.title('HLS')
img_XYZ = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ)
plt.subplot(3,3,7); plt.imshow(img_XYZ)
plt.axis('off'); plt.title('XYZ')
img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB)
plt.subplot(3,3,8); plt.imshow(img_LAB)
plt.axis('off'); plt.title('LAB')
img_YUV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)
plt.subplot(3,3,9); plt.imshow(img_YUV);
plt.axis('off'); plt.title('YUV') ; plt.show()
````

</details>

#### Pex20_4 · Python · b1e1a6cc

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`6a90f06b59b972f62f9f8f3c9544eaef85127a3332d10a7429e14b535bcf63fc`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_4.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_4.py
from PIL import Image
from numpy import array
import pylab as plt  #加载Matplotlib的Pylab接口
a=Image.open("empire.jpg")  #返回一个PIL图像对象
b=a.convert("L")  #转换为灰度图像对象
b.save("empire2.jpg")  #把灰度图像保存到empire2.jpg
aa=array(a)  #把图像对象转换为数组
print(aa.shape)  #显示图像的大小
#左上角为坐标原点，下面裁剪左上右下指定区域
c=a.crop((100,100,400,400)) 
d=a.rotate(45)  #图像旋转45度
plt.rc('font',family="SimHei")
plt.subplot(221); plt.imshow(a); plt.title("原图")
plt.subplot(222); plt.imshow(b); plt.title("灰度图")
plt.subplot(223); plt.imshow(c); plt.title("剪裁图像")
plt.subplot(224); plt.imshow(d); plt.title("旋转图像"); plt.show()
````

</details>

#### Pex20_5 · Python · 77c97e09

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`2b606bd0e1ab839f7a0342d8b772c27eb1850cbd0fae7912d1d2a0de51d4f9d1`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_5.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_5.py
from PIL import Image
from numpy import array
import pylab as plt  #加载Matplotlib的Pylab接口
#下面读取图像到数组中
a=array(Image.open("empire.jpg").convert('L'))
plt.rc('font',size=16)
plt.subplot(121); plt.contour(a,origin='image')  #轮廓图
plt.subplot(122); plt.hist(a.flatten(),128); plt.show()
````

</details>

#### Pex20_6 · Python · 3e4a9cc2

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e31c74a65fe17fc1edb9b05b46f074f8d962e008bd0c6c7a054afaa3b97088a5`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_6.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_6.py
from PIL import Image
a=Image.open('flower.jpg')  #读入图像
a.show()  #显示图片
print(a.mode, a.size, a.format) #显示图片信息
a.save("flower2.png")  #另存为另一文件
````

</details>

#### Pex20_7 · Python · 57408dee

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`6ec5503ab2185d97fd730aceffd07442aa0cbe1698457a4895023ddd906495f8`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_7.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_7.py
from PIL import Image
a=Image.new("RGB",(640,480),(50,50,100,0))  #创建新图像 
a.save("figure20_7.jpg")  #保存图像
a.show()  #显示图像
````

</details>

#### Pex20_8 · Python · a50f99fd

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`1495258830f6ba86cc1945190f97e94b1d2292d209937d84c2cbfe77b94d8219`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_8.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_8.py
from PIL import Image
from pylab import subplot,imshow,show
a=Image.open('flower.jpg')  #读入图像
b=a.resize((128,128))  #改变图像尺寸
c=b.convert('CMYK')  #转换为CMYK模式
subplot(121); imshow(b)
subplot(122); imshow(c); show()
````

</details>

#### Pex20_9 · Python · 01952774

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e024a1a983e5df5730b88dd5b61c1bb60c082f1b1e39939ae024cee499b563c2`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pex20_9.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex20_8.py
from PIL import Image
from pylab import subplot,imshow,show
a=Image.open('flower.jpg')  #读入图像
ra,ga,ba=a.split()  #图像分割成R、G、B三个通道
c=Image.merge('RGB',(ra,ga,ba)) #三个通道合成一张彩色图像
subplot(221); imshow(ra); subplot(222); imshow(ga)
subplot(223); imshow(ba); subplot(224); imshow(c); show()
````

</details>

#### Pz20_1 · Python · 113d9a74

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：导入依赖后执行数值变换、模型计算和结果输出。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`09930f38a218937bd6caffe96ca80aa4fbd3655a53639e93869b3178fdbd1127`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/20第20章  数字图像处理(Python 程序及数据)/Pz20_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pz20_1.py
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
````

</details>

#### NaSchr · MATLAB · bb67a358

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：执行归一化或标准化以统一变量尺度；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：存在同目录辅助函数调用，需要一起迁移。

- SHA-256：`3be45ef0cabf25b4b699223c5809d68b6fd8c07edc467febe47ce639395e3d08`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/元胞自动机代码可直接运行（建议学会基本原理再用）/NaSchr.m`
- 同目录代码调用：
  - 被调用代码：`00-Inbox/Downloaded/数学建模程序代码资料合集/元胞自动机代码可直接运行（建议学会基本原理再用）/ts.m`

<details>
<summary>展开原始代码</summary>

````matlab
% Nagel Schreckenberg model simulation
%Written by Alexander Farley
%Feb 6 2012
%alexander.farley at utoronto.ca
%This script implements the Nagel Schreckenberg cellular automata based
%traffic model. Flow vs density curves are displayed.
%
%
%Update June 5 2012: Fixed problem in vehicle velocity updates
%Update Jan 13 2013: Fixed problem with vmax=1 showing no flow
%Update June 12 2013: Corrected calculation of flow rate for FD plot
%


%Parameters
vmax = 10;
p = 0.6;%原始数据0.8
road_length = 1000;
simulation_steps = 1000;
render_on = 0;
pause_on = 0;
delay_on = 0;
delay_length = 0.02; %10 FPS

road = zeros(1,road_length);       %Contains occupation state
road_next = road;
velocities = zeros(1,road_length); %Contains velocity state
velocities_next = velocities;

%Sampling
num_samples = 2000;
samples = zeros(2,num_samples); %Contains density and flow rate
density_step = 1/num_samples;

history = zeros(simulation_steps, road_length);
velocity_history = zeros(simulation_steps, road_length);

figure

for g=1:num_samples;
    
    %Generate traffic
    road = zeros(1,road_length);       %Contains occupation state
    road_next = road;
    density = g/num_samples;
    
    %Generate traffic
    
    for i=1:road_length
        if rand < density
            road(i) = 1;
        end
    end
    
    if render_on
        imshow(road);
        drawnow
    end
    
    %Run simulation
    for i=1:simulation_steps
        history(i, :) = road;
        velocity_history(i,:) = velocities;
        %--------------------Velocity update ------------------------%
        for j=1:road_length
            if road(j) == 1
                distance = 0;
                %Seek vmax ahead
                bf = 0;
                for k=1:vmax
                    distance = k;
                    
                    if j+k <= road_length %The index is the "cell under consideration" - is it safe to land here?
                        index = j+k;
                    else
                        index = j+k-road_length; %Deal with wrapping
                    end
                    
                    if road(index) == 1
                        bf = 1;
                    end
                    
                    if bf == 1, break, end
                end
                
                if velocities(j) < vmax %Acceleration
                    velocities(j) = velocities(j) + 1;
                end
                
                if (velocities(j) > distance - 1) && bf == 1 %Collision avoidance
                    velocities(j) = distance - 1;
                end
                
                if rand < p && velocities(j) > 0 %Random braking
                    velocities(j) = velocities(j) - 1;
                end
                
                
            end
        end
        
        %--------------------Movement -------------------------------%
        for j=1:road_length
            if road(j) ==1
                if j+velocities(j) <= road_length
                    index = j+velocities(j);
                else
                    index = j+velocities(j) - road_length; %Deal with wrapping
                end
                %Collision detection
                if road_next(index) == 1
                    disp('Collision detected')
                end
                road_next(index) = 1;
                velocities_next(index) = velocities(j);
            end
        end
        
        velocities = velocities_next;
        
        road = road_next;
        road_next = zeros(1,road_length);
        
        if render_on
            imshow(road);
            drawnow
        end
        
        if pause_on
            pause
        end
        
        if delay_on
            pause(delay_length)
        end
        
    end
    
    %Record density and flow rate
    velocity_history = velocity_history.*history;
    samples(:,g) = [mean2(history) (sum(velocity_history(:))/sum(history(:)))*mean2(history)];
    
    disp('Sample step:')
    g
end

scatter(samples(1,:), samples(2,:));
axis([0 1 0 1]);
xlabel('Density')
ylabel('Flow (normalized)')
title('Flow-density Curve')

%imshow(history)
% ts(simulation_steps,history)
````

</details>

#### 元胞自动机代码演示案例 · MATLAB · f7cd6cf4

- 归属算法：数字图像处理
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：含随机过程但未发现固定随机种子。

- SHA-256：`af0fb280fd7b9f4c439497434fabf57f72da000ddb2844c1baaec254171f9b88`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/元胞自动机代码演示案例.txt`

<details>
<summary>展开原始代码</summary>

````matlab
对元胞自动机的初步认识
元胞自动机（CA）是一种用来仿真局部规则和局部联系的方法。典型的元
胞自动机是定义在网格上的，每一个点上的网格代表一个元胞与一种有限的状
态。变化规则适用于每一个元胞并且同时进行。
元胞的变化规则&元胞状态
典型的变化规则，决定于元胞的状态，以及其（ 4 或 8 ）邻居的状态。
元胞自动机的应用
元胞自动机已被应用于物理模拟，生物模拟等领域。
元胞自动机的matlab编程
结合以上，我们可以理解元胞自动机仿真需要理解三点。一是元胞，在matlab中可以理解为矩阵中的一点或多点组成的方形块，一般我们用矩阵中的一点代表一个元胞。二是变化规则，元胞的变化规则决定元胞下一刻的状态。三是元胞的状态，元胞的状态是自定义的，通常是对立的状态，比如生物的存活状态或死亡状态，红灯或绿灯，该点有障碍物或者没有障碍物等等。



案例一
生命游戏是英国数学家约翰·何顿·康威在1970年发明的细胞自动机。它包括一个二维矩形世界，这个世界中的每个方格居住着一个活着的或死了的细胞。一个细胞在下一个时刻生死取决于相邻八个方格中活着的或死了的细胞的数量。通常情况，游戏的规则就是：当一个方格周围有2或3个活细胞时，方格中的活细胞在下一个时刻继续存活；即使这个时刻方格中没有活细胞，在下一个时刻也会“诞生”活细胞。
听说许多程序猿都喜欢玩这个
规则是：
? 对周围的 8 个近邻的元胞状态求和
? 如果总和为 2 的话，则下一时刻的状态不改变
? 如果总和为 3 ，则下一时刻的状态为 1
? 否则状态= 0
元胞的邻居定义通常有以下三种范式，这里采用第二种，认为其周围八个点为邻居。

代码：

%% 设置GUI按键
plotbutton=uicontrol('style','pushbutton','string','运行', 'fontsize',12, 'position',[150,400,50,20], 'callback', 'run=1;');
erasebutton=uicontrol('style','pushbutton','string','停止','fontsize',12,'position',[250,400,50,20],'callback','freeze=1;');
quitbutton=uicontrol('style','pushbutton','string','退出','fontsize',12,'position',[350,400,50,20],'callback','stop=1;close;');
number = uicontrol('style','text','string','1','fontsize',12, 'position',[20,400,50,20]);
%% 元胞自动机设置
n=200;
%初始化各元胞状态
z = zeros(n,n);
sum = z;
cells = (rand(n,n))<.6;
% 建立图像句柄
imh = image(cat(3,cells,z,z));
set(imh, 'erasemode', 'none')
% 元胞更新的行列数设置
x = 2:n-1;
y = 2:n-1;
% 主事件循环
stop= 0; run = 0;freeze = 0; 
while stop==0
    if run==1
        % 计算邻居存活的总数
        sum(x,y) = cells(x,y-1) + cells(x,y+1) + cells(x-1, y) + cells(x+1,y)...
            + cells(x-1,y-1) + cells(x-1,y+1) + cells(x+1,y-1) + cells(x+1,y+1);
        % 按照规则更新
        cells = (sum==3) | (sum==2 & cells);
        set(imh, 'cdata', cat(3,cells,z,z) )
        stepnumber = 1 + str2double(get(number,'string'));
        set(number,'string',num2str(stepnumber))
    end
    if freeze==1
        run = 0;
        freeze = 0;
    end
    drawnow
end

案例二
规则，先把中间点置为1，每一时间步对每一点，如果周围
八个点和为偶数，则变为0，为奇数则变为 1

% 颜色控制
Map = [1 1 1; 0 0 0];
colormap(Map);
% 设置网格大小
S = 121;
L = zeros(S);
% 把中间一个数设置为 1 作为元胞种子
M = (S+1)/2;
L(M, M) = 1;
Temp = L;
imagesc(L);
% 计算层数
Layer = (S-1)/2 + 1;

for t=2:Layer
    for x=M-t+1:M+t-1
       if x==M-t+1 || x==M+t-1

          for y=M-t+1:M+t-1
            SUM = 0;
            for m=-1:1
               for n=-1:1
                  if x+m>0 && x+m<=S && y+n>0 && y+n<=S
                     SUM = SUM + L(x+m, y+n); 
                  end
               end
            end
            SUM = SUM - L(x, y);
            Temp(x, y) = mod(SUM, 2);
          end
          
       else
            y = M-t+1;
            SUM = 0;
            for m=-1:1
               for n=-1:1
                  if x+m>0 && x+m<=S && y+n>0 && y+n<=S
                     SUM = SUM + L(x+m, y+n); 
                  end
               end
            end
            SUM = SUM - L(x, y);
            Temp(x, y) = mod(SUM, 2);
            
            y = M+t-1;
            SUM = 0;
            for m=-1:1
               for n=-1:1
                  if x+m>0 && x+m<=S && y+n>0 && y+n<=S
                     SUM = SUM + L(x+m, y+n); 
                  end
               end
            end
            SUM = SUM - L(x, y);
            Temp(x, y) = mod(SUM, 2);
       end
    end
    L = Temp;
    imagesc(L);
    % 速度控制
    pause(0.2);
end

案例三 元胞自动机在交通流领域的模拟
第一步，先将这个函数放到matlab函数库种
function [ v, d, p ] = multi_driveway_with_crossroad_exit( nl,...
    nc,dt,fp,nt,chance,chance1)
% fp:车道入口处新进入车辆的概率向量（2,3,5 车道）——输入参数
% chance:交叉口处车辆行为的概率向量(5 车道右转,3车道右转）——输入参数
 %构造元胞矩阵
 B=ones(nc+1+nl/2,nl+3);
 %不可行车道
 B(nc/2+1,[1:nl/2 nl/2+4:nl+3])=1.2;   
 B(nc+2:nc+1+nl/2,[1:nl/2 nl/2+4:nl+3])=1.2;
 %初始化仿真元胞状态（1 为无车，0 为有车）
 bb1=B([1:nc/2 nc/2+2:nc+1],:);bb2=B(:,nl/2+3);bb3=B(:,nl/2+1);
 bb1(bb1~=0)=1;
 bb2(bb2~=0)=1;
 bb3(bb3~=0)=1;
 B([1:nc/2 nc/2+2:nc+1],:)=bb1;B(:,nl/2+3)=bb2;B(:,nl/2+1)=...
     bb3;B(1:nc+1,nl/2+1:nl/2+3)=1;
 B(1:nc/2,end)=0;B(nc/2+2:nc+1,1)=0;B(end,nl/2+3)=0;
 %显示初始交通流图
 figure();
 H=imshow(B,[]);
 set(gcf,'position',[241 132 560 420]) ;%241 132 560 420
 set(gcf,'doublebuffer','on'); %241
 title('cellular-automation to traffic modeling','color','b');
 %初始化化存储元胞上车辆状态的矩阵
 S(1:nc*2+2,nl/2-2) = 0;
 Q(1:nc*2+2,1:2) = 0;
 C=zeros(nc+1,3);
 %初始化换道频率、平均速度、车流密度相关变量
 ad = 0;
 av(1:nt) = 0;
 ap(1:nt) = 0;
 s = 1;flag= 0;flag1=0;%flag、flag1 用于标示小区出口的车是否为左转车辆
 flag2=0;
 for n = 1:nt
%六个路段的长度。
A=[
B(1:nc/2,nl/2 :-1:1);
B(nc/2+2:nc+1,1:nl/2);
B(1:nc/2,nl+3:-1:nl/2+4);
B(nc/2+2:nc+1,nl/2+4:nl+3);
B(nc+1+nl/2:-1:nc+2,nl/2+3)';
B(nc+2:1:nc+1+nl/2,nl/2+1)'
];
c=B(1:nc+1,nl/2+1:nl/2+3);
 %确定前 n-2 个车辆的状态
 S(:,:) = 0;
 S(A(:,1:end-2)==0&A(:,2:end-1)==1&A(:,3:end)==1)=2;%快速行驶的车
 S(A(:,1:end-2)==0&A(:,2:end-1)==0)=3;%停车的车
 S(A(:,1:end-2)==0&A(:,2:end-1)==1&A(:,3:end)==0)=1;%慢速行驶的车
 %确定最后两个元胞的状态
 Q(:,:)= 0;
 Q(A(:,end-1)==0&A(:,end)==0) = 3;
 Q(A(:,end-1)==0&A(:,end)==1) = 1;
 if c(3,1)==0
     if rand<chance1
         flag2=1;
         c(3,1)=1;
     end
 end   
 if A(1,end)==0
 Q(1,end)=1;
 end
 if A(4,end)==0
 Q(4,end)=1;
 end
 if A(6,end)==0
 Q(6,end)=1;
 end
 if rem(floor(n/50),2)==0 %此时左右向为绿灯
 if A(2,end)==0
 if c(nc/2+2:nc+1,1)==0
 Q(2,end)=3;
 else
     Q(2,end)=1;
 end 
 end
 if A(3,end)==0
 if c(1,3)==0
 Q(3,end)=3;
 else
 Q(3,end)=1;
 end
 end
 %按照既定规则行驶（5 车道右转）
 if A(5,end)==0
 if flag==0
 if rand<chance %路口车右转
 if c(nc/2+2:nc+1,:)==1
 Q(5,end)=1;  
 else
 Q(5,end)=3;
 end
 end
 else %第一辆车为左转车，需要等待                                  
 end
 end
 if c(1,2)==0
 if c(1,1)==1%3道口左转的思路：规避。
 C(1,2)=1;
 else
 C(1,2)=3;
 end
 if c(2,1)==0                
 C(1,2)=3;
 end
 end
 if c(1,3)==0
 if c(1,2)==1
 C(1,3)=1;
 else
 C(1,3)=3;
 end
 end
 if c(3,1)==0
 if c(3,2)==1
 C(3,1)=1;
 else
 C(3,1)=3;
 end
 end
 if c(3,2)==0
 if c(3,3)==1
 C(3,2)=1;
 else
 C(3,2)=3;
 end
 end
 if rem(n,20)==0&&c(3,2)==0%小区出来的车还遗留在路口，特殊处理先行
 if c(2,1)==1
 C(3,2)=5; %特殊的等待状态（小区出来的车）
 else
 C(3,2)=3;
 end
 end
 if c(2,1)==0
 if A(1:nc/2,1)==0
 C(2,1)=3;
 else
 C(2,1)=1;
 end
 end
 if c(1,1)==0
 if A(1,1)==0
 C(1,1) = 3;
 else
 C(1,1) = 1;
 end
 end
 if c(3,3)==0
 if A(nc*3/2+1:2*nc,1)==0
 C(3,3) = 3;
 else
 C(3,3) = 1;
 end
 end
 else %此时小区出入向为绿灯
 Q(2,end)=3;Q(3,end)=3;
 if c(3,2)==0
 if flag1==1
 if c(2,1)==1
 C(3,2)=5;flag1=0;
 else
 C(3,2)=3;
 end
 else
 if c(3,3)==1
 C(3,2)=1;
 else
 C(3,2)=3;
 end
 end
 end
 if c(2,1)==0
 if A(1:nc/2,1)==1&&c(1,1)==1
 C(2,1)=1;
 else
 C(2,1)=3;
 end
 end
 if A(5,end)==0
 if flag==0
 if rand<chance
 if c(nc/2+2:nc+1,:)==1
 Q(5,end)=1;
 else
 Q(5,end)=3;
 end
 else
 if c(nc/2+2:nc+1,1)==1&&c(nc/2+2:nc+1,2)==1
 Q(5,end)=5;flag=0;flag1=1; %小区的左转前进，用以区分右转车辆
 else
 Q(5,end)=3;flag=1;
 end
 end
 else
 if c(nc/2+2:nc+1,1)==1&&c(nc/2+2:nc+1,2)==1
 Q(5,end)=5;flag=0;flag1=1; %小区的左转前进，用以区分右转车辆
 else
 Q(5,end)=3;flag=1;
 end
 end
 end
 if c(1,2)==0
 if c(1,1)==1
 C(1,2)=1;
 else
 C(1,2)=3;
 end
 end
 if c(1,3)==0
 if c(1,2)==1
 C(1,3)=1;
 else
 C(1,3)=3;
 end
 end
 if c(3,1)==0
 if c(3,2)==1
 C(3,1)=1;
 else
 C(3,1)=3;
 end
 end
 if c(1,1)==0
 if A(1:nc/2,1)==0
 C(1,1) = 3;
 else
 C(1,1) = 1;
 end
 end
 if c(3,3)==0
 if A(nc*3/2+1:2*nc,1)==0
 C(3,3) = 3;
 else
 C(3,3) = 1;
 end
 end
 end
 %获得所有元胞上车辆的状态
 Acc = [ S Q ];
 %根据当前状态改变元胞位置
 %路口附近的车辆的行驶控制
 if C(3,2)==5
 c(2,1)=0;
 c(3,2)=1;
 flag=0;
 C(3,2)=0;
 elseif C(3,2)==1
 c(3,3)=0;
 c(3,2)=1;
 C(3,2)=0;
 end
 if C(2,1)==1
 A(1,1)=0;
 c(2,1)=1;
 C(2,1)=0;
 end
 if Acc(3,end)==1
 c(1,3)=0;
 A(3,end)=1;
 Acc(3,end)=0;
 end
 if Acc(2,end)==1
 c(3,1)=0;
 A(2,end)=1;
 Acc(2,end)=0;
 end
 if C(3,1)==1
 c(3,2)=0;
 c(3,1)=1;
 C(3,1)=0;
 end
 if C(1,3)==1
 c(1,2)=0;
 c(1,3)=1;
 C(1,3)=0;
 end
 if C(1,2)==1
 c(1,1)=0;
 c(1,2)=1;
 C(1,2)=0;
 end
 if C(1,1)==1
 A(1,1)=0;
 c(1,1)=1;
 C(1,1)=0;
 end
 if C(3,3)==1
 A(4,1)=0;
 c(3,3)=1;
 C(3,3)=0;
 end
 %慢速运行车辆向前走 1 格
 A( Acc(:,1:end)==1 )=1;
 A( [ zeros(nc*3,1) Acc(:,1:end-1)]==1 ) = 0;
 %高速运行车辆向前走 2 格
 A( Acc(:,1:end)==2) = 1;
 A( [ zeros(nc*3,2) Acc(:,1:end-2)]==2) = 0;
 if Acc(1,1)==1||Acc(1,1)==2
 A(1,1)=1;
 end
 if Acc(4,1)==1||Acc(4,1)==2
 A(4,1)=1;
 end
 if Acc(5,end)==5
 c(3,2)=0;flag=0;
 A(5,end)=1;
 elseif Acc(5,end)==1
 c(3,3)=0;
 A(5,end)=1;
 end
 if Acc(3,end)==1
 c(1,3)=0;
 A(3,end)=1;
 end
 if Acc(2,end)==1
 c(3,1)=0;
 A(2,end)=1;
 end
 if Acc(4,1)==1||Acc(4,1)==2
 A(4,1)=1;
 end
 if Acc(1,1)==1||Acc(1,1)==2
 A(1,1)=1;
 end
 %计算平均速度、换道频率、车流密度等参数
 %获得运行中的车辆数目 N
 matN = A<1;
 N = sum(sum(matN));
 %获得运行中的车辆速度之和 V
 E = S((S==1)|(S==2));
 V = sum(E);
 %计算此时刻的车流密度并保存
 ap(n) = N/( (nc*3)*(nl/2)+9 );
 %计算此时刻的平均速率并保存
 if(N~=0&&n>nl/2)
 av(s) = V/N;
 s = s+1;
 end
 %在车道入口处随机引入新的车辆
 A([2;3;5],1)=(round(fp.*rand(3,1))&A([2;3;5],1));
 A(A~=0)=1;
 if flag2==1
     A(6,1)=0;
     flag2=0;
 end
 %将新的车辆加入元胞矩阵中
 B(1,1:nl/2)=A(1:nc/2,end:-1:1);
 B(3,1:nl/2)=A(nc/2+1:nc,:);
 B(1,nl/2+4:nl+3)=A(nc+1:nc*3/2,end:-1:1);
 B(3,nl/2+4:nl+3)=A(nc*3/2+1:2*nc,:);
 B(nc+2:nc+1+nl/2,nl/2+3)=A(2*nc+1,end:-1:1)';
 B(nc+2:nc+1+nl/2,nl/2+1)=A(3*nc,:)';
 B(1:3,nl/2+1:nl/2+3)=c(:,:);
 %显示交通流图
 set(H,'CData',B);
%计算这个时间段每个时间点的指标（速度与车流量）。
 d = ad;
 p = mean(ap);
 v = sum(av)/s;
 disp([v,p])
%仿真步长
 pause(dt);
 end
end

第二步骤将下列代码放入命令行
% 车流密度不变下的双向两车道仿真（T 字形路口）
% v:平均速度，d:换道次数（1000 次）p:车流密度
nl = 80 ;% 车道长度（偶数）
nc = 2; % nc:双向车道数目
dt= 0.01; % 仿真步长时间
fp = 20; % 车道入口处新进入车辆的概率（列向量）
nt=10000;% 仿真步长数目
chance=0.5;
chance1=0.5;
[ v, d, p ] = multi_driveway_with_crossroad_exit ( nl,nc,dt,fp,nt,chance,chance1);
````

</details>

#### 小波特征提取算法代码 · MATLAB · 781278b4

- 归属算法：数字图像处理
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于数字图像处理中的“核心算法与辅助函数”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `tezhengtiqu`；先核对参数顺序和返回值。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`6fbe1a96d0f7af464602675f011b7ff64fe5c20e62b1bd34edffb83c21a3c794`
- 语言：MATLAB
- 符号：`tezhengtiqu`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/小波特征提取算法代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
function   tezhengtiqu
%新归一化方法小波矩特征提取----------------------------------------------------------


F=imread('a1.bmp');
F=im2bw(F);
F=imresize(F,[128 128]);
%求取最上点
for i=1:128
    for j=1:128
        if (F(i,j)==1)
            ytop=i;
            xtop=j;
            break;
        end
    end
    if(F(i,j)==1)
        break;
    end
end
%求取最下点
for i=1:128
    for j=1:128
        if (F(129-i,j)==1)
            ybottom=129-i;
            xbottom=j;
            break;
        end
    end
    if(F(129-i,j)==1)
        break;
    end
end
%求取最左点
for i=1:128
    for j=1:128
        if (F(j,i)==1)
            yleft=j;
            xleft=i;
            break;
        end
    end
    if(F(j,i)==1)
        break;
    end
end
%求取最右点
for i=1:128
    for j=1:128
        if (F(j,129-i)==1)
            yright=j;
            xright=129-i;
            break;
        end
    end
    if(F(j,129-i)==1)
        break;
    end
end
%求取中心点
x0=(xright-xleft)/2+xleft;
y0=(ybottom-ytop)/2+ytop;
x0=round(x0);
y0=round(y0);
%图像平移
F=double(F);
[M,N]=size(F);
F1=zeros(M,N);
M0=M/2;
N0=N/2;
for i=1:M
  for j=1:N
        if F(i,j)==1
           F1(i+M0-y0,j+N0-x0)=1;
        end
    end
end
figure,imshow(F1);
%图像缩放
max=0;
for i=1:128
    for j=1:128
        if(F(i,j)==1)
            d=sqrt((i-y0)^2+(j-x0)^2);
            if(max<d)
                max=d;
            end
        end
    end
end
%max=round(max);
a=200.0/(max*2);
F2=imresize(F1,a);
figure,imshow(F2);
%将所有图像均复制到500*500的图像的大小
[M,N]=size(F2);
m0=M/2;
m0=round(m0);
n0=N/2;
n0=round(n0);
f3=zeros(500,500);
y1=round((500-M)/2);
x1=round((500-N)/2);
for i=1:M
    for j=1:N
        if(F2(i,j)==1)
            f3(y1+i,x1+j)=1;
        end
    end
end
figure,imshow(f3);
%图像从笛卡儿坐标转换为极坐标------------------------------------------------------------
%角度间隔为2*pi/(128*128),128个像素长设为图像的单位圆半径
%f1矩阵里面放着对应极半径和角度的值
f1=zeros(128,16384);
%直角坐标与极坐标建立起一一对应的关系           
for i=1:128
    for j=1:16384
        a=j*2*pi/16384.0;
        r=i;
        y=round(r*sin(a));
        x=round(r*cos(a));
       if (f3(250+x,250+y)==1)
            f1(i,j)=1;
        end
    end
end
F3=zeros(512,512);
%将极坐标转换后的图像显示出来
for i=1:128
    for j=1:16384
        if  f1(i,j)==1
            a=j*2*pi/16384.0;
            x=round(i*cos(a));
            y=round(i*sin(a));
            F3(256+x,256+y)=1;
        end
    end
end
F3(256,256)=1;
figure,imshow(F3);
%小波矩特征提取-------------------------------------------------------------------
%进行角度积分得到Sq(r)------------------
N=16384;
Sq=zeros(128,4);
for r=1:128
    for q=1:4
        for m=1:N          
             Sq(r,q)=(f1(r,m)*exp(-j*2.0*pi*(m-1)*(q-1)/N))+Sq(r,q);
        end
       Sq(r,q)=1.0/N*Sq(r,q);
    end
end
%小波矩特征提取-------------------------
x=3;
a=0.697066;
f0=0.409177;
w=sqrt(0.561145);
F1=zeros(3,9,4);
 tt=4*a^(x+1)/sqrt(2*pi*(x+1))*w;
for q=1:4
    for m=1:3
        rr=2^m+1;
        for n=1:rr
            for r=1:128
               %pp=2*(2^(m-1)*(r-1)/128.0-(n-1))-1;
               pp=2*(2^(m-1)*r/128.0-(n-1))-1;
               cc=cos(2*pi*f0*pp)*exp(-1.0*pp^2/(2*(w^2)*(x+1)));
               fan=2^((m-1)/2)*tt*cc;
               %Fmnq(m,n,q)=abs(Sq(r,q)*fan*(r-1)/128)+Fmnq(m,n,q);
               F1(m,n,q)=abs(Sq(r,q)*fan*r)+F1(m,n,q);
            end
        end
    end
end
  F1
````

</details>

#### 神经网络图像分类代码 · MATLAB · 57f7ab43

- 归属算法：数字图像处理
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“预测与推断”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`06712e199c2834a3e3d4f1495acdc9ed1069f4bfc224359304d25683bc962ec4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/神经网络图像分类代码.txt`

<details>
<summary>展开原始代码</summary>

````matlab
神经网络图像分类基本步骤
第一步：找到需要分类的图像，如下方的10.jpg
第二步：找到样本数据，分类是需要有样本数据的，数据集中已经给出
第三步：替换掉下方的代码数据即可

代码
clear all;
%读入样本10,即遥感图像的背景
I=imread('10.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
%初始化输入矢量P和输出矢量T
P=[];
T=[];
P=[R;G;B];
T=[0;0;0];
[m n]=size(P);
T=concur(T,n);

%读入样本图像0
I=imread('0.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.1;0.3;0.5];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像1
I=imread('1.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.2;0.4;0.6];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像2
I=imread('2.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.3;0.2;0.7];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像3
I=imread('3.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.4;0.4;0.7];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像4
I=imread('4.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.5;0.5;0.4];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像5
I=imread('5.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.6;0.9;0.2];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像6
I=imread('6.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.7;0.2;0.8];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像7
I=imread('7.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.8;0.3;0.5];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像8
I=imread('8.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.9;0.2;0.1];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像9
I=imread('9.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[1;0.5;0.6];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%创建一个前向神经网络
net=newff(minmax(P),[5,3],{'logsig','purelin'},'traingdx');
%设置训练参数
net.trainParam.show=50;
net.trainParam.epochs=1000;   %最大训练步数为1000
net.trainParam.goal=0.001;
net=init(net);
%对BP网络进行训练
net=train(net,P,T);

for j=1:2
    if j==1
        var=input('是否对2000年崇明东滩遥感影像进行分类（是:输入1 ，否:输入2）');
    elseif j==2
        var=input('是否对2003年崇明东滩遥感影像进行分类（是:输入1 ，否:输入2）');
    end

%读入待分类遥感图像
if var==1
    if j==1 
    I=imread('tm2000mask.jpg');
    elseif j==2
    I=imread('tm2003mask.jpg');
    end
  %将彩色图像降维
  R=I(:,:,1);
  G=I(:,:,2);
  B=I(:,:,3);
  %将灰度值归一化处理
  R=im2double(R);
  G=im2double(G);
  B=im2double(B);
  [M,N]=size(R);
  R=reshape(R',[1 M*N]);
  G=reshape(G',[1 M*N]);
  B=reshape(B',[1 M*N]);
  p=[R;G;B];
  %对BP网络进行仿真
  Y=sim(net,p);
  R=Y(1,:);
  X=R;              
  classR=[];    
  for i=0:(M-1)
      classR=[classR;R((i*N+1):(i*N+N))];
  end
  G=Y(2,:);
  classG=[];
  for i=0:(M-1)
      classG=[classG;G((i*N+1):(i*N+N))];
  end
  B=Y(3,:);
  classB=[];
  for i=0:(M-1)
      classB=[classB;B((i*N+1):(i*N+N))];
  end

  R=abs(classR)*255;
  R=uint8(R);
  G=abs(classG)*255;
  G=uint8(G);
  B=abs(classB)*255;
  B=uint8(B);
  classify=cat(3,R,G,B);
  figure,imshow(classify);
  if j==1
      title('2000年崇明东滩遥感图像分类图');
  elseif j==2
      title('2003年崇明东滩遥感图像分类图');
  end

  %计算各类地物面积
  X=abs(X)*255;
  [M,N]=size(X);
  t10=0;t0=0;t1=0;t2=0;t3=0;t4=0;t5=0;t6=0;t7=0;t8=0;t9=0;

  for i=1:N
      if X(1,i)==0
          t10=t10+1;
      elseif X(1,i)<26
          t0=t0+1;
      elseif X(1,i)<52
          t1=t1+1;
      elseif X(1,i)<=76
          t2=t2+1;
      elseif X(1,i)<=102
          t3=t3+1;
      elseif X(1,i)<=127
          t4=t4+1;
      elseif X(1,i)<=153
          t5=t5+1;
      elseif X(1,i)<=178
          t6=t6+1;
      elseif X(1,i)<204
          t7=t7+1;
      elseif X(1,i)<=229
          t8=t8+1;
      else t9=t9+1;
      end
  end
  
  var=input('是否以饼状图显示地物比例(是:输入1 ,否:输入2)');
  if var==1
  %绘制地物面积饼状图
  t=[t0,t1,t2,t3,t4,t5,t6,t7,t8,t9];
  figure;
  pie(t);
  legend('海水','农地','绿林地','房屋','养殖场','芦苇','互花米草','海三棱藨草','光滩','未利用地',-1);            %标注图例
  end
  
  var=input('是否以直方图显示地物比例(是:输入1 ,否:输入2 )');
  if var==1
  %绘制地物面积柱状图
  y=[t0,t1,t2,t3,t4,t5,t6,t7,t8,t9];  
  x=1:10;
  figure;
  bar(x,y);colormap summer;         %绘制柱状图且返回图形句柄
  end
end
end

var=input('是否对2005年遥感图像进行预测(是：输入1 否：输入2)');
if var==1
%<----------------------------!运用2000年和2003年图像预测2005年图像------------------>
%读入2000年遥感数据
I=imread('tm2000mask.jpg');
%将图像数据降维
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
%初始化输入向量
P=[];
P=[R;G;B];

%初始化输出向量
%读入2003年遥感数据
I=imread('tm2003mask.jpg');
%将图像数据降维
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
T=[];
T=[R;G;B];

%创建一个前向神经网络
net=newff(minmax(P),[5 3],{'logsig','purelin'},'traingdx');
%设置训练参数
net.trainParam.show=50;
net.trainParam.epochs=1000;
net.trainParam.goal=0.001;
%对BP网络进行训练
net=train(net,P,T);

%预测2005年遥感图像
%对BP网络进行仿真
Y=sim(net,T);
  R=Y(1,:);              
  R2005=[];    
  for i=0:(M-1)
      R2005=[R2005;R((i*N+1):(i*N+N))];
  end
  G=Y(2,:);
  G2005=[];
  for i=0:(M-1)
      G2005=[G2005;G((i*N+1):(i*N+N))];
  end
  B=Y(3,:);
  B2005=[];
  for i=0:(M-1)
      B2005=[B2005;B((i*N+1):(i*N+N))];
  end
  
  R=abs(R2005)*255;
  R=uint8(R);
  G=abs(G2005)*255;
  G=uint8(G);
  B=abs(B2005)*255;
  B=uint8(B);
  T2005=cat(3,R,G,B);
  figure;imshow(T2005);
end
````

</details>

#### LiChen · MATLAB · 3977419c

- 归属算法：数字图像处理
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#数字图像处理 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于数字图像处理中的“预测与推断”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`f3a47f111c8031e3943b73a885f752d3abeecc72090bbfb23c8f98c143092064`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模程序代码资料合集/神经网络图像分类代码（可直接运行）/LiChen.m`

<details>
<summary>展开原始代码</summary>

````matlab
clear all;

%<----------------------------!运用BP网络进行图像分类--------------------------->
%读入样本10,即遥感图像的背景
I=imread('10.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
%初始化输入矢量P和输出矢量T
P=[];
T=[];
P=[R;G;B];
T=[0;0;0];
[m n]=size(P);
T=concur(T,n);

%读入样本图像0
I=imread('0.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.1;0.3;0.5];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像1
I=imread('1.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.2;0.4;0.6];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像2
I=imread('2.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.3;0.2;0.7];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像3
I=imread('3.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.4;0.4;0.7];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像4
I=imread('4.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.5;0.5;0.4];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像5
I=imread('5.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.6;0.9;0.2];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像6
I=imread('6.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.7;0.2;0.8];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像7
I=imread('7.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.8;0.3;0.5];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像8
I=imread('8.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[0.9;0.2;0.1];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%读入样本图像9
I=imread('9.jpg');
%将样本图像降维处理
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
P1=[R;G;B];
T1=[1;0.5;0.6];
P=[P,P1];
[m n]=size(P1);
T1=concur(T1,n);
T=[T,T1];

%创建一个前向神经网络
net=newff(minmax(P),[5,3],{'logsig','purelin'},'traingdx');
%设置训练参数
net.trainParam.show=50;
net.trainParam.epochs=1000;   %最大训练步数为1000
net.trainParam.goal=0.001;
net=init(net);
%对BP网络进行训练
net=train(net,P,T);

for j=1:2
    if j==1
        var=input('是否对2000年崇明东滩遥感影像进行分类（是:输入1 ，否:输入2）');
    elseif j==2
        var=input('是否对2003年崇明东滩遥感影像进行分类（是:输入1 ，否:输入2）');
    end

%读入待分类遥感图像
if var==1
    if j==1 
    I=imread('tm2000mask.jpg');
    elseif j==2
    I=imread('tm2003mask.jpg');
    end
  %将彩色图像降维
  R=I(:,:,1);
  G=I(:,:,2);
  B=I(:,:,3);
  %将灰度值归一化处理
  R=im2double(R);
  G=im2double(G);
  B=im2double(B);
  [M,N]=size(R);
  R=reshape(R',[1 M*N]);
  G=reshape(G',[1 M*N]);
  B=reshape(B',[1 M*N]);
  p=[R;G;B];
  %对BP网络进行仿真
  Y=sim(net,p);
  R=Y(1,:);
  X=R;              
  classR=[];    
  for i=0:(M-1)
      classR=[classR;R((i*N+1):(i*N+N))];
  end
  G=Y(2,:);
  classG=[];
  for i=0:(M-1)
      classG=[classG;G((i*N+1):(i*N+N))];
  end
  B=Y(3,:);
  classB=[];
  for i=0:(M-1)
      classB=[classB;B((i*N+1):(i*N+N))];
  end

  R=abs(classR)*255;
  R=uint8(R);
  G=abs(classG)*255;
  G=uint8(G);
  B=abs(classB)*255;
  B=uint8(B);
  classify=cat(3,R,G,B);
  figure,imshow(classify);
  if j==1
      title('2000年崇明东滩遥感图像分类图');
  elseif j==2
      title('2003年崇明东滩遥感图像分类图');
  end

  %计算各类地物面积
  X=abs(X)*255;
  [M,N]=size(X);
  t10=0;t0=0;t1=0;t2=0;t3=0;t4=0;t5=0;t6=0;t7=0;t8=0;t9=0;

  for i=1:N
      if X(1,i)==0
          t10=t10+1;
      elseif X(1,i)<26
          t0=t0+1;
      elseif X(1,i)<52
          t1=t1+1;
      elseif X(1,i)<=76
          t2=t2+1;
      elseif X(1,i)<=102
          t3=t3+1;
      elseif X(1,i)<=127
          t4=t4+1;
      elseif X(1,i)<=153
          t5=t5+1;
      elseif X(1,i)<=178
          t6=t6+1;
      elseif X(1,i)<204
          t7=t7+1;
      elseif X(1,i)<=229
          t8=t8+1;
      else t9=t9+1;
      end
  end
  
  var=input('是否以饼状图显示地物比例(是:输入1 ,否:输入2)');
  if var==1
  %绘制地物面积饼状图
  t=[t0,t1,t2,t3,t4,t5,t6,t7,t8,t9];
  figure;
  pie(t);
  legend('海水','农地','绿林地','房屋','养殖场','芦苇','互花米草','海三棱藨草','光滩','未利用地',-1);            %标注图例
  end
  
  var=input('是否以直方图显示地物比例(是:输入1 ,否:输入2 )');
  if var==1
  %绘制地物面积柱状图
  y=[t0,t1,t2,t3,t4,t5,t6,t7,t8,t9];  
  x=1:10;
  figure;
  bar(x,y);colormap summer;         %绘制柱状图且返回图形句柄
  end
end
end

var=input('是否对2005年遥感图像进行预测(是：输入1 否：输入2)');
if var==1
%<----------------------------!运用2000年和2003年图像预测2005年图像------------------>
%读入2000年遥感数据
I=imread('tm2000mask.jpg');
%将图像数据降维
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
%初始化输入向量
P=[];
P=[R;G;B];

%初始化输出向量
%读入2003年遥感数据
I=imread('tm2003mask.jpg');
%将图像数据降维
R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);
%灰度值归一化
R=im2double(R);
G=im2double(G);
B=im2double(B);
[M N]=size(R);
R=reshape(R',[1 M*N]);
G=reshape(G',[1 M*N]);
B=reshape(B',[1 M*N]);
T=[];
T=[R;G;B];

%创建一个前向神经网络
net=newff(minmax(P),[5 3],{'logsig','purelin'},'traingdx');
%设置训练参数
net.trainParam.show=50;
net.trainParam.epochs=1000;
net.trainParam.goal=0.001;
%对BP网络进行训练
net=train(net,P,T);

%预测2005年遥感图像
%对BP网络进行仿真
Y=sim(net,T);
  R=Y(1,:);              
  R2005=[];    
  for i=0:(M-1)
      R2005=[R2005;R((i*N+1):(i*N+N))];
  end
  G=Y(2,:);
  G2005=[];
  for i=0:(M-1)
      G2005=[G2005;G((i*N+1):(i*N+N))];
  end
  B=Y(3,:);
  B2005=[];
  for i=0:(M-1)
      B2005=[B2005;B((i*N+1):(i*N+N))];
  end
  
  R=abs(R2005)*255;
  R=uint8(R);
  G=abs(G2005)*255;
  G=uint8(G);
  B=abs(B2005)*255;
  B=uint8(B);
  T2005=cat(3,R,G,B);
  figure;imshow(T2005);
end
````

</details>

### 未标注例程·结果绘图与展示 · 实现

#### exA_14 · MATLAB · 43849aa9

- 归属算法：未标注例程·结果绘图与展示
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#未标注例程·结果绘图与展示 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·结果绘图与展示中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c2b6a5e90e47c2cff625543380684587a29c098fdf8a95d35ba0c6e58d3dde2e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/16附录A/exA_14.m`

<details>
<summary>展开原始代码</summary>

````matlab
syms x
y=x^3+6*x^2+8*x-1; dy=diff(y);
dy_zero=solve(dy), dy_zero_num=double(dy_zero)  %变成数值类型
ezplot(y)  %符号函数画图
````

</details>

#### exA_1_1 · MATLAB · 41dbe94d

- 归属算法：未标注例程·结果绘图与展示
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#未标注例程·结果绘图与展示 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·结果绘图与展示中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8666f50377ea8dea5f553ad53c474e7b66ce6bf7f77b8e7240622f53b4991b71`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/16附录A/exA_1_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
fplot('Afun1',[-3,3])
````

</details>

#### exA_1_2 · MATLAB · cefb12ba

- 归属算法：未标注例程·结果绘图与展示
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#未标注例程·结果绘图与展示 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·结果绘图与展示中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c2ef6bd1fb1185a370747273eb8a333b45efac98b35a7eb5dc7290c9c3e26e53`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/16附录A/exA_1_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
Afun2=@(x) (x+1)*(x<1)+(1+1/x)*(x>=1);
fplot(Afun2,[-3,3])
````

</details>

#### exA_2 · MATLAB · ea17f298

- 归属算法：未标注例程·结果绘图与展示
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#未标注例程·结果绘图与展示 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·结果绘图与展示中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4270bd74e27afdfd910ddfec7b11a24102c7e4fe87e6a0215660076a14918026`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/16附录A/exA_2.m`

<details>
<summary>展开原始代码</summary>

````matlab
ezplot('tan(x)')
````

</details>

#### exA_3 · MATLAB · 9f1a474a

- 归属算法：未标注例程·结果绘图与展示
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#未标注例程·结果绘图与展示 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·结果绘图与展示中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e0ec59971e74712bebdf7278ab6586f1711ea4d4d31a13eea835e400a75160d1`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/16附录A/exA_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
ezplot('x^2+y^2/4=1')
````

</details>

#### exA_5 · MATLAB · de652f6a

- 归属算法：未标注例程·结果绘图与展示
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#未标注例程·结果绘图与展示 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于未标注例程·结果绘图与展示中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a6255727cca7c780d36e5c71c60099d316b5457df7b66ebcc006eaf753e03aa5`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/16附录A/exA_5.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=-3:0.1:3;y=-5:0.1:5;
x1=ones(size(y'))*x;y1=y'*ones(size(x));
[x2,y2]=meshgrid(x,y);
z1=(sin(x1.*y1)+eps)./(x1.*y1+eps);
z2=(sin(x2.*y2)+eps)./(x2.*y2+eps);
subplot(1,2,1),mesh(x1,y1,z1)
subplot(1,2,2),mesh(x2,y2,z2)
````

</details>

### 绘图可视化 · 实现

#### fun8 · MATLAB · 3733f154

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`230bc6dd89005654324a05ffa0e300db73d18871fe358051e70f091e1fd00419`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/03第3章/fun8.m`

<details>
<summary>展开原始代码</summary>

````matlab
function [c,ceq,k1,k2,s]=fun8(x,s);
c=[];ceq=[];
if isnan(s(1,1))
    s=[0.2,0;0.2 0];
end
%取样值
w1=1:s(1,1):100;
w2=1:s(2,1):100;
%半无穷约束
k1=sin(w1*x(1)).*cos(w1*x(2))-1/1000*(w1-50).^2-sin(w1*x(3))-x(3)-1;
k2=sin(w2*x(2)).*cos(w2*x(1))-1/1000*(w2-50).^2-sin(w2*x(3))-x(3)-1;
%画出半无穷约束的图形
plot(w1,k1,'-',w2,k2,'+');
````

</details>

#### anli5_1_3 · MATLAB · 044faa12

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`f664285fc4f7fa67c282f931eb3a5eb1ff903b62e872d6d462173bbdd4cec8d4`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/05第5章/anli5_1_3.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
load data3.txt  %把表5.8中的日期和时间数据行删除，余下的数据保存在纯文本文件
liu=data3([1,3],:); liu=liu'; liu=liu(:);  %提出水流量并按照顺序变成列向量
sha=data3([2,4],:); sha=sha'; sha=sha(:); %提出含沙量并按照顺序变成列向量
y=sha.*liu;   %计算排沙量，这里是列向量
subplot(1,2,1), plot(liu(1:11),y(1:11),'*')
subplot(1,2,2), plot(liu(12:24),y(12:24),'*')
````

</details>

#### ex5_1 · MATLAB · c892c6fa

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：执行插值或参数拟合并评价曲线；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9b250b68a1b9f2a05737d9e281bd27e336edfc6f81e2034cd851fbe640560ee6`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/05第5章/ex5_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
x0=[0   3   5   7   9   11   12   13   14  15];
y0=[0  1.2  1.7  2.0  2.1  2.0  1.8  1.2   1.0  1.6];
x=0:0.1:15;
y1=interp1(x0,y0,x);
y2=interp1(x0,y0,x,'spline');
pp1=csape(x0,y0);
y3=ppval(pp1,x);
pp2=csape(x0,y0,'second');
y4=ppval(pp2,x);
[x',y1',y2',y3',y4']
subplot(1,3,1)
plot(x0,y0,'+',x,y1)
title('Piecewise linear')
subplot(1,3,2)
plot(x0,y0,'+',x,y2)
title('Spline1')
subplot(1,3,3)
plot(x0,y0,'+',x,y3)
title('Spline2')
dx=diff(x);
dy=diff(y3);
dy_dx=dy./dx;
dy_dx0=dy_dx(1)
ytemp=y3(131:151);
ymin=min(ytemp);
index=find(y3==ymin);
xmin=x(index);
[xmin,ymin]
````

</details>

#### 相似实现组 · MATLAB · c7871534

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 变体 1：ex5_5.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a2ed80556ab559a3dbda85f3fcaac5f278f852f9c35af09f0cf3f95751e58f29`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/05第5章/ex5_5.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=[19     25    31     38    44]';
y=[19.0   32.3   49.0   73.3   97.8]';
r=[ones(5,1),x.^2];
ab=r\y
x0=19:0.1:44;
y0=ab(1)+ab(2)*x0.^2;
plot(x,y,'o',x0,y0,'r')
````

</details>

##### 变体 2：ex5_7.m

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`215e824ae48106ac9df6abe5834ee1f6264091ea40dc45823c4bb519591d8daa`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/05第5章/ex5_7.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=[19     25    31     38    44]';
y=[19.0   32.3   49.0   73.3   97.8]';
r=[ones(5,1),x.^2];
ab=lsqlin(r,y)
x0=19:0.1:44;
y0=ab(1)+ab(2)*x0.^2;
plot(x,y,'o',x0,y0,'r')
````

</details>

#### ex5_6_1 · MATLAB · 96614c0e

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1e2200b104515513ed311e386511aa7f111c9b62c28115c7f664abe8bf9f78fb`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/05第5章/ex5_6_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
x0=[1990  1991  1992  1993  1994  1995  1996];
y0=[70   122   144   152   174   196   202];
plot(x0,y0,'*')
````

</details>

#### ex6_12 · MATLAB · f9c026e1

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`d282b35ce8cf4881cc3f795054c75a81d194881f46c5b81216db106bc07bec11`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_12.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
eq=@(x,y,mu)[y(2);-mu*y(1)]; %定义一阶方程组的匿名函数
bd=@(ya,yb,mu)[ya(1);ya(2)-1;yb(1)+yb(2)];  %定义边值条件的匿名函数
guess=@(x)[sin(2*x);2*cos(2*x)]; %定义初始猜测解的匿名函数
guess_structure=bvpinit(linspace(0,1,10),guess,5); %给出初始猜测解的结构,mu=5
sol=bvp4c(eq,bd,guess_structure); %计算数值解
plot(sol.x,sol.y(1,:),'-',sol.x,sol.yp(1,:),'--','LineWidth',2)
xlabel('x','FontSize',12)
legend('y_1','y_2')
````

</details>

#### ex6_13 · MATLAB · 44203e58

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8b1ba2a56451afdf3a005758270056325ce9f5471f81c123d7f8a6bad0447acd`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_13.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
eq=@(x,y)[0.5*y(1)*(y(3)-y(1))/y(2)
          -0.5*(y(3)-y(1))
          (0.9-1000*(y(3)-y(5))-0.5*y(3)*(y(3)-y(1)))/y(4)
          0.5*(y(3)-y(1))
          100*(y(3)-y(5))]; %定义一阶方程组的匿名函数
bd=@(ya,yb)[ya(1)-1;ya(2)-1;ya(3)-1;ya(4)+10;yb(3)-yb(5)]; %定义边值条件的匿名函数
guess=@(x)[1;1;-4.5*x.^2+8.91*x+1;-10;-4.5*x.^2+9*x+0.91]; %定义初始猜测解的匿名函数
guess_structure=bvpinit(linspace(0,1,5),guess); %给出初始猜测解的结构
sol=bvp4c(eq,bd,guess_structure); %计算数值解
plot(sol.x,sol.y(1,:),'-*',sol.x,sol.y(2,:),'-D',sol.x,sol.y(3,:),':S',sol.x,sol.y(4,:),'-.O',sol.x,sol.y(5,:),'--P') %画出5条解曲线
legend('u','v','w','z','y',3)  %图注标注在左下角
````

</details>

#### ex6_9 · MATLAB · 00cb045f

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1db7888163707d333b98ed36f660c3c37b2659b64686451110f4363c85bf0201`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/06第6章/ex6_9.m`

<details>
<summary>展开原始代码</summary>

````matlab
dy=@(t,y) [y(2);1000*(1-y(1)^2)*y(2)-y(1)]; %定义匿名函数
[t,y]=ode15s(dy,[0 3000],[2;0]);  %求数值解
plot(t,y(:,1),'*')
title('Solution of van der Pol Equation,mu=1000');
xlabel('time t');
ylabel('solution y');
````

</details>

#### ex8_4 · MATLAB · c8f07094

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形、文件结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`dbb7d0c6b2233cf72b626e487be781ec5f83197be61e840d660feee4e3929036`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/08第8章/ex8_4.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc,clear
yt=load('touzi.txt'); %原始投资总额数据以列向量的方式存放在纯文本文件中
n=length(yt); alpha=0.3; st0=mean(yt(1:3));
st1(1)=alpha*yt(1)+(1-alpha)*st0;
st2(1)=alpha*st1(1)+(1-alpha)*st0;
st3(1)=alpha*st2(1)+(1-alpha)*st0;
for i=2:n
    st1(i)=alpha*yt(i)+(1-alpha)*st1(i-1);
    st2(i)=alpha*st1(i)+(1-alpha)*st2(i-1);
    st3(i)=alpha*st2(i)+(1-alpha)*st3(i-1);
end
xlswrite('touzi.xls',[st1',st2',st3'])  %把数据写在前三列
at=3*st1-3*st2+st3;
bt=0.5*alpha/(1-alpha)^2*((6-5*alpha)*st1-2*(5-4*alpha)*st2+(4-3*alpha)*st3);
ct=0.5*alpha^2/(1-alpha)^2*(st1-2*st2+st3);
yhat=at+bt+ct;
xlswrite('touzi.xls',yhat','Sheet1','D2')  %把数据写在第4列第2行开始的位置
plot(1:n,yt,'D',2:n,yhat(1:end-1),'*')
legend('实际值','预测值',2)  %图注显示在左上角
xishu=[ct(end),bt(end),at(end)]; %二次预测多项式的系数向量
yhat1990=polyval(xishu,2)  %求预测多项式m=2时的值
````

</details>

#### ex10_20 · MATLAB · 1610d943

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：进行特征分解以获得权重、主成分或稳定性信息；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9ef8ba9144be0f0eb9550fc1a83bc36291f86860752449feb90ffe63b74b83d7`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/10第10章/ex10_20.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
D=[0, 1, sqrt(3), 2, sqrt(3), 1, 1; zeros(1,2),1, sqrt(3), 2, sqrt(3), 1
   zeros(1,3),1, sqrt(3), 2, 1;zeros(1,4), 1, sqrt(3), 1
   zeros(1,5), 1, 1; zeros(1,6), 1; zeros(1,7)]  %原始距离矩阵的上三角元素
d=D+D'; %构造完整的距离矩阵
%d=nonzeros(D')'; %转换成pdist函数输出格式的数据
[y,eigvals]=cmdscale(d) %求经典解，d可以为实对称矩阵或pdist函数的行向量输出
plot(y(:,1),y(:,2),'o','Color','k','LineWidth',1.3)   %画出点的坐标
%下面我们通过求特征值求经典解
D2=D+D'; %构造对称距离矩阵  
A=-D2.^2/2;   %构造A矩阵
n=size(A,1);
H=eye(n)-ones(n)/n;  %构造H矩阵
B=H*A*H   %构造B矩阵
[vec1,val1]=eig(B);  %求B矩阵的特征向量vec1和特征值val1
[val2,ind]=sort(diag(val1),'descend') %把特征按从大到小排列
vec2=vec1(:,ind)  %相应地把特征向量也重新排序
vec3=orth(vec2(:,[1,2])); %构造正交特征向量
point=[vec3(:,1)*sqrt(val2(1)),vec3(:,2)*sqrt(val2(2))] %求点的坐标
hold on
plot(point(:,1),point(:,2),'D','Color','k','LineWidth',1.3)   %验证得到的解和Matlab不一致
theta=-0.42;      %旋转的角度
T=[cos(theta),-sin(theta);sin(theta),cos(theta)];
Tpoint=point*T;   %把特征向量进行一个正交变换
plot(Tpoint(:,1),Tpoint(:,2),'+','Color','k','LineWidth',1.3)  %验证这样得到的解和Matlab一致
legend('Matlab命令cmdscale求得的解','按照算法求得的一个解','正交变换后得到的与cmdscale相同的解',0)
````

</details>

#### ex10_21 · MATLAB · 79039445

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`56b16fb48b8246f536ae4dab560e5920e8db2f2fa6c6f0a9627d4a0a4e536889`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/10第10章/ex10_21.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
d=textread('d.txt');   %把原始数据保存在纯文本文件d.txt中
d=nonzeros(d)'; %按照列顺提出矩阵d中的非零元素,再化成行向量
cities={'1.阿伯瑞斯吹','2.布莱顿','3.卡里斯尔','4.多佛','5.爱塞特',...
'6.格拉斯哥','7.赫尔','8.印威内斯','9.里兹','10.伦敦',...
'11.纽加塞耳','12.挪利其'}  %构造细胞数组
[y,eigvals]=cmdscale(d)   %求经典解，这里d为实对称阵或pdist格式的行向量
plot(y(:,1),y(:,2),'o','Color','k','LineWidth',1.5)   %画出点的坐标
text(y(:,1)-18,y(:,2)+10,cities); %对点进行标注
````

</details>

#### anli12_1 · MATLAB · a35e22ea

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`b22c2ffc23fb4fd4ccdc1cc3a9291b3aaa17d2132fb27c2e2c09380c34ef075e`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/司守奎数学建模算法课件/程序及数据/12第12章/anli12_1.m`

<details>
<summary>展开原始代码</summary>

````matlab
clc, clear
sj0=load('sj.txt');    %加载100个目标的数据，数据按照表格中的位置保存在纯文本文件sj.txt中
x=sj0(:,[1:2:8]);x=x(:);
y=sj0(:,[2:2:8]);y=y(:);
sj=[x y]; d1=[70,40]; 
sj=[d1;sj;d1]; sj=sj*pi/180; %角度化成弧度
d=zeros(102); %距离矩阵d初始化
for i=1:101
   for j=i+1:102
d(i,j)=6370*acos(cos(sj(i,1)-sj(j,1))*cos(sj(i,2))*cos(sj(j,2))+sin(sj(i,2))*sin(sj(j,2)));
   end
end
d=d+d';
path=[];long=inf; %巡航路径及长度初始化
rand('state',sum(clock));  %初始化随机数发生器
for j=1:1000  %求较好的初始解
    path0=[1 1+randperm(100),102]; temp=0;
    for i=1:101
        temp=temp+d(path0(i),path0(i+1));
    end
    if temp<long
        path=path0; long=temp;
    end
end
e=0.1^30;L=20000;at=0.999;T=1;
for k=1:L  %退火过程
c=2+floor(100*rand(1,2));  %产生新解
c=sort(c); c1=c(1);c2=c(2);
  %计算代价函数值的增量
df=d(path(c1-1),path(c2))+d(path(c1),path(c2+1))-d(path(c1-1),path(c1))-d(path(c2),path(c2+1));
  if df<0 %接受准则
  path=[path(1:c1-1),path(c2:-1:c1),path(c2+1:102)]; long=long+df;
  elseif exp(-df/T)>rand
  path=[path(1:c1-1),path(c2:-1:c1),path(c2+1:102)]; long=long+df;
  end
  T=T*at;
   if T<e
       break;
   end
end
path, long % 输出巡航路径及路径长度
xx=sj(path,1);yy=sj(path,2);
plot(xx,yy,'-*') %画出巡航路径
````

</details>

#### liti2 · MATLAB · ed56a96d

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`b6d302e33cde87465d35c2d80902f7b729ac7fd345c23a8263ca215a252808af`
- 语言：MATLAB
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/数据的统计处理/第10讲 数据的统计描述与分析/liti2.m`

<details>
<summary>展开原始代码</summary>

````matlab
x=-6:0.01:6; 
y=normpdf(x); z=normpdf(x,0,2);
plot(x,y,x,z)
````

</details>

#### 第01章例题程序 · SAS · 7fac2ab9

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC CAPABILITY`、`PROC CORR`、`PROC MEANS`、`PROC PRINT`、`PROC UNIVARIATE`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`5b1488a93a836082a76fd31ec1f826ba4f0d7aa66122644fd5fbee9de67081dd`
- 语言：SAS
- 符号：`PROC CAPABILITY`, `PROC CORR`, `PROC MEANS`, `PROC PRINT`, `PROC UNIVARIATE`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/00预备知识 SAS软件简介/第01章例题程序.txt`

<details>
<summary>展开原始代码</summary>

````sas
例
libname a 'e:\data\';
data a.student;
infile 'e:\data\student.txt';
input name$ height weight;
run;





例一
data li11;
input x @@;
cards;
9.89 8.00 6.40 6.17 5.39 7.27 9.08 9.24 7.75 6.20
8.95 8.33 10.40 11.20 8.75 6.45 11.90 10.30 9.58
;
proc means n mean var std cv skew kurt;
var x;
run;
proc print;
run;
补充课本例2
data li12;
input x @@;
cards;
74.3 78.8 68.8 78.0 70.4 80.5 80.5 69.7 71.2 73.5
79.5 75.6 75.0 78.8 72.0 72.0 72.0 74.3 71.2 72.0 
75.0 73.5 78.8 74.3 75.8 65.0 74.3 71.2 69.7 68.0 
73.5 75.0 72.0 64.3 75.8 80.3 69.7 74.3 73.5 73.5
75.8 75.8 68.8 76.5 70.4 71.2 81.2 75.0 70.4 68.0
70.4 72.0 76.5 74.3 76.5 77.6 67.3 72.0 75.0 74.3
73.5 79.5 73.5 74.7 65.0 76.5 81.6 75.4 72.7 72.7
67.2 76.5 72.7 70.4 77.2 68.8 67.3 67.3 67.3 72.7
75.8 73.5 75.0 73.5 73.5 73.5 72.7 81.6 70.3 74.3
73.5 79.5 70.4 76.5 72.7 77.2 84.3 75.0 76.5 70.4
;
proc means n mean var std cv skew kurt;
var x;
run;
proc print;
run;
例二
data li13;
input aa bb;
cards;
5.75 4
6.25 3
6.75 15
7.25 42
7.75 49
8.25 78
8.75 50
9.25 31
9.75 5
;
proc means n mean var std cv skew kurt;
freq bb;
var aa;
run;
例三
data p9;
   do g=1 to 2;
   input n;
   do i=1 to n;
   input x@ @;output;
   end;end;
  Cards;
  11 
  0.84 1.05 1.20 1.20 1.39 1.53 1.67 1.80 1.87 2.07 2.11
  13
  0.54 0.64 0.64 0.75 0.76 0.81 1.16 1.20 1.34 1.35 1.48 1.58 1.87
  ;
  proc means;
  var x;
  by g;
  run;
注：求标准正态分布分位数的程序
data;
x=probit(0.75);  /*0.75分位数*/
put x;
run;
注；求数据落在上下阶段点之外的概率
data;
y1=probnorm(-2.698);
y2=probnorm(2.698);
z=y1+1-y2;
put z;
run;



例
data shiyan;
input x @@;
cards;
5 3 11 3 1 7 8 
;
proc means data=shiyan madian range;
run;
proc means data=shiyan q3 q1 p99 p95 p90 p10 p5 p1;
run;


例4：
data li11;
input x @@;
cards;
9.89 8.00 6.40 6.17 5.39 7.27 9.08 9.24 7.75 6.20
8.95 8.33 10.40 11.20 8.75 6.45 11.90 10.30 9.58
;
proc means median q1 q3 p99 p90 p10 p5 p1 range qrange;
run;
proc univariate ;
var x;
run;
补充课本例1.8
data li12;
input x @@;
cards;
74.3 78.8 68.8 78.0 70.4 80.5 80.5 69.7 71.2 73.5
79.5 75.6 75.0 78.8 72.0 72.0 72.0 74.3 71.2 72.0 
75.0 73.5 78.8 74.3 75.8 65.0 74.3 71.2 69.7 68.0 
73.5 75.0 72.0 64.3 75.8 80.3 69.7 74.3 73.5 73.5
75.8 75.8 68.8 76.5 70.4 71.2 81.2 75.0 70.4 68.0
70.4 72.0 76.5 74.3 76.5 77.6 67.3 72.0 75.0 74.3
73.5 79.5 73.5 74.7 65.0 76.5 81.6 75.4 72.7 72.7
67.2 76.5 72.7 70.4 77.2 68.8 67.3 67.3 67.3 72.7
75.8 73.5 75.0 73.5 73.5 73.5 72.7 81.6 70.3 74.3
73.5 79.5 70.4 76.5 72.7 77.2 84.3 75.0 76.5 70.4
;
proc univariate ;
var x;
run;
例5 、
data li12;
input x @@;
cards;
74.3 78.8 68.8 78.0 70.4 80.5 80.5 69.7 71.2 73.5
79.5 75.6 75.0 78.8 72.0 72.0 72.0 74.3 71.2 72.0 
75.0 73.5 78.8 74.3 75.8 65.0 74.3 71.2 69.7 68.0 
73.5 75.0 72.0 64.3 75.8 80.3 69.7 74.3 73.5 73.5
75.8 75.8 68.8 76.5 70.4 71.2 81.2 75.0 70.4 68.0
70.4 72.0 76.5 74.3 76.5 77.6 67.3 72.0 75.0 74.3
73.5 79.5 73.5 74.7 65.0 76.5 81.6 75.4 72.7 72.7
67.2 76.5 72.7 70.4 77.2 68.8 67.3 67.3 67.3 72.7
75.8 73.5 75.0 73.5 73.5 73.5 72.7 81.6 70.3 74.3
73.5 79.5 70.4 76.5 72.7 77.2 84.3 75.0 76.5 70.4
;
proc capability graphics;
histogram x/normal;
cdfplot x/normal;
qqplot x/normal;
run;
引例1 程序
data li111;
input x @@;
cards;
25 45 50 54 55 61 64 68 72 75 75 78 79 81 83 84 
84 84 85 86 86 86 87 89 89 89 90 91 91 92 100
;
proc univariate plot normal;
run;
例六
data li112;
input x @@;
cards;
53.0 70.2 84.3 55.3 78.5 63.5 71.4 53.4 82.5 67.3
69.5 73.0 55.7 85.8 95.4 51.1 74.4 54.1 77.8 52.4 
69.1 53.5 64.3 82.7 55.7 70.5 87.5 50.7 72.3 59.5
;
proc univariate plot;
run;
例七
程序见引例1。
例八
data li11;
input x @@;
cards;
9.89 8.00 6.40 6.17 5.39 7.27 9.08 9.24 7.75 6.20
8.95 8.33 10.40 11.20 8.75 6.45 11.90 10.30 9.58
;
proc univariate normal;
var x;
run;
例1.21
data li121;
input x y;
cards;
67 24
54 15
72 23
64 19
39 16
22 11
58 20
43 16
46 17
34 13
;
proc corr pearson spearman;
var x y;
run;
````

</details>

#### ch13_SGPANEL · SAS · e5b4b06a

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC FORMAT`、`PROC SGPANEL`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`cddf56e158122a324918e7c8b77a38a86f3c45b9b29ace15c872e54d5149c663`
- 语言：SAS
- 符号：`PROC FORMAT`, `PROC SGPANEL`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch13_SGPANEL.sas`

<details>
<summary>展开原始代码</summary>

````sas
data wings;
infile 'c:\MyRawData\Birds.dat';
input Name $12. Type $ Length Wingspan @@;
run;
* Plot Wingspan by Length;
proc format;
value $birdtype
'S' = 'Songbirds'
'R' = 'Raptors';
run;
proc sgpanel data = wings;
panelby Type / NOVARNAME SPACING = 5;
scatter X = Wingspan Y = Length;
format Type $birdtype.;
title 'Comparison of Wingspan vs. Length';
run;
````

</details>

#### ch13_she_zhi_tu_xing_shu_chu · SAS · 719257e7

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC SGPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`6c2e4f03f5f76c74c8934dc833011538f651512a48bf82913d881329ee845973`
- 语言：SAS
- 符号：`PROC SGPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch13_she_zhi_tu_xing_shu_chu.sas`

<details>
<summary>展开原始代码</summary>

````sas
data wings;
infile 'c:\MyRawData\Birds.dat';
input Name $12. Type $ Length Wingspan @@;
run;
* Plot Wingspan by Length;
ODS LISTING GPATH ='c:\MyGraphs' STYLE = JOURNAL;
ODS GRAPHICS / RESET
imagename = 'BirdGraph'
outputfmt = BMP
HEIGHT = 2IN WIDTH = 3IN;
proc sgplot data = wings;
scatter X =Wingspan Y = Length;
title 'Comparison of ''Wingspan vs. Length';
run;
````

</details>

#### ch14_box_plots · SAS · 76e3329c

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC SGPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`01594e2396f099f2bb2e85c808164b1c1c45a9f43caaea181b1fa6afcba7fe68`
- 语言：SAS
- 符号：`PROC SGPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch14_box_plots.sas`

<details>
<summary>展开原始代码</summary>

````sas
data bikerace;
infile 'c:\MyRawData\Criterium.dat';
input Division $ NumberLaps @@;
run;
* Create box plot;
proc sgplot data = bikerace;
vbox NumberLaps / CATEGORY = Division;
title 'Bicycle Criterium Results by Division';
run;
````

</details>

#### ch15_scatter · SAS · b4d24175

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC FORMAT`、`PROC SGPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`3454c01d7c523f002a6bf7c62db28f660439479cb0bc55027e2a9ba6a86569f9`
- 语言：SAS
- 符号：`PROC FORMAT`, `PROC SGPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch15_scatter.sas`

<details>
<summary>展开原始代码</summary>

````sas
data wings;
infile 'c:\MyRawData\Birds.dat';
input Name $12. Type $ Length Wingspan @@;
run;
* Plot Wingspan by Length;
proc format;
value $birdtype
'S' = 'Songbirds'
'R' = 'Raptors';
run;
proc sgplot data = wings;
scatter X = Wingspan Y = Length / GROUP = Type 
MARKERATTRS = (SYMBOL = PLUS SIZE = 2MM);
format Type $birdtype.;
title 'Comparison of Wingspan vs. Length';
run;
````

</details>

#### ch15_series_plot · SAS · 6aa29539

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按温度和接受概率进行模拟退火搜索。
- **调用方式**：优先调用 `PROC SGPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；包含绝对路径，必须改为项目相对路径。

- SHA-256：`1a078d98473c059ef1a95e1cc90f90f3502155d7c372d1461c9946e302d19403`
- 语言：SAS
- 符号：`PROC SGPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch15_series_plot.sas`

<details>
<summary>展开原始代码</summary>

````sas
data electricity;
infile 'c:\MyRawData\Hourly.dat';
input Time kWh @@;
run;
* Plot temperatures by time;
proc sgplot data = electricity;
series X = Time Y = kWh / MARKERS;
REFLINE 0.5 / LABEL = ('0.5 kWh') TRANSPARENCY = 0.5;
xaxis values = (0 TO 24 BY 1);
yaxis label = 'Electricity (kWh)';
title 'Hourly Use of Electricity';
run;
````

</details>

#### ch27_fei_xian_xing_hui_gui3 · SAS · 605522b3

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`、`PROC NLIN`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7c7647b08f8f2be41251025b3a86036975cd5d90c2a1c56ede060e631da5964d`
- 语言：SAS
- 符号：`PROC GPLOT`, `PROC NLIN`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch27_fei_xian_xing_hui_gui3.sas`

<details>
<summary>展开原始代码</summary>

````sas
data expd;
input x y @@;
datalines;
020 0.57 030 0.72 040 0.81 050 0.87 060 0.91 070 0.94
080 0.95 090 0.97 100 0.98 110 0.99 120 1.00 130 0.99
140 0.99 150 1.00 160 1.00 170 0.99 180 1.00 190 1.00
200 0.99 210 1.00
;
proc nlin data = expd best = 10 method = gauss;
parms b0=0 to 2 by 0.5 b1=0.01 to 0.09 by 0.01;
model y=b0*(1-exp(-b1*x));
der.b0=1-exp(-b1*x);
der.b1=b0*x*exp(-b1*x);
output out = expout p = ygs;
run;
goptions reset = global gunit = pct cback = white border
         htitle = 6 htext = 3 ftext = swissb colors = (back);
proc gplot data = expout;
plot y*x ygs*x /haxis=axis1 vaxis=axis2 overlay;
symbol1 i=none v=plus cv=red h=2.5 w=2;
symbol2 i=join v=none l=1 h=2.5 w=2;
axis1 order=20 to 210 by 10;
axis2 order=0.5 to 1.1 by 0.05;
title1 'y=b0*(1-exp(-b1*x)';
title2 'proc nlin method=gauss';
run;
````

</details>

#### 例3.1 · SAS · 6f94f36f

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`7e1847c3eeecd6d6560058e5d4f5c4550c39883b9db47dcb2c7d09712e6ad9d1`
- 语言：SAS
- 符号：`PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
x1_0=0;
x2_0=0;
x3_0=0;
x3_1=0;
x4_0=0;
x4_1=0;
do t=-10 to 100;
e=rannor(12345);
x1=0.8*x1_0+e;
x2=-1.1*x2_0+e;
x3=x3_0-0.5*x3_1+e;
x4=x4_0+0.5*x4_1+e;
x1_0=x1;
x2_0=x2;
x3_1=x3_0;
x4_1=x4_0;
x3_0=x3;
x4_0=x4;
if t>0 then output ;
end;
data a;
set a;
keep t x1 x2 x3 x4;
proc gplot;
plot x1*t x2*t x3*t x4*t;
symbol c=black i=jion v=none;
run;
````

</details>

#### example5_2 · SAS · 2b427676

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC AUTOREG`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a909ce8d72c72dc5c1be97043b906221e8f6fba999786cc8847b474932db9f17`
- 语言：SAS
- 符号：`PROC AUTOREG`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/example5_2.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data example5_2;
input x@@;
lagx=lag(x);   
t=_n_;
cards;
3.03 	8.46 	10.22 	9.80 	11.96 	2.83 
8.43 	13.77 	16.18 	16.84 	19.57 	13.26 
14.78 	24.48 	28.16 	28.27 	32.62 	18.44 
25.25 	38.36 	43.70 	44.46 	50.66 	33.01 
39.97 	60.17 	68.12 	68.84 	78.15 	49.84 
62.23 	91.49 	103.20 	104.53 	118.18 	77.88 
94.75 	138.36 	155.68 	157.46 	177.69 	117.15 
;
proc gplot data=example5_2;
plot x*t=1;
symbol1 c=black i=join v=star;
proc autoreg data=example5_2;
model x=t/ dwprob ;
proc autoreg data=example5_2;                                                                                                              
model x=t/nlag=5 backstep method=ml noint ;                                                                                             
output out=out p=xp pm=trend;                                                                                                           
proc gplot data=out;                                                                                                                    
plot x*t=2 xp*t=3 trend*t=4 / overlay ;                                                                                                 
symbol2  v=star i=none c=black;                                                                                                        
symbol3  v=none i=join c=red w=2;                                                                                                   
symbol4  v=none i=join c=green w=2;                                                                                                     
proc autoreg data=example5_2;                                                                                                              
model x=lagx/lagdep=lagx;  
model x=lagx/lagdep=lagx noint; 
output out=out p=xp;                                                                                                           
proc gplot data=out;                                                                                                                    
plot x*t=2 xp*t=3 / overlay ;                                                                                                 
run;
````

</details>

#### example5_3 · SAS · 6662a80c

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC AUTOREG`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e59a1bff1d753a548daffa7e44736a1bc0b1d6959eb5ea9b113e5c31596a446c`
- 语言：SAS
- 符号：`PROC AUTOREG`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/example5_3.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example5_3;
input x@@;
t=_n_;
cards;
10.77	13.30	16.64	19.54	18.97	20.52	24.36
23.51	27.16	30.80	31.84	31.63	32.68	34.90
33.85	33.09	35.46	35.32	39.94	37.47	35.24
33.03	32.67	35.20	32.36	32.34	38.45	38.17
32.14	39.70	49.42	47.86	48.34	62.50	63.56
67.61	64.59	66.17	67.50	76.12	79.31	78.85
81.34	87.06	86.41	93.20	82.95	72.96	61.10
61.27	71.58	88.34	98.70	97.31	97.17	91.17
80.20	85.12	81.40	70.87	57.75	52.35	67.50
87.95	85.46	84.55	98.16	102.42	113.02	119.95
122.37	126.96	122.79	127.96	139.20	141.05	140.87
137.08	145.53	145.59	134.36	122.54	106.92	97.23
110.39	132.40	152.30	154.91	152.69	162.67	160.31
142.57	146.54	153.83	141.81	157.83	161.79	142.07
139.43	140.92	154.61	172.33	191.78	199.27	197.57
189.29	181.49	166.84	154.28	150.12	165.17	170.32
；
proc gplot data=example5_3;
plot x*t=1;
symbol1 c=black i=join v=star;
proc autoreg data=example5_3;
model x=t/nlag=5  dwprob archtest;
model x=t/nlag=2 noint garch=(p=1,q=1);
output out=out p=xp;
proc gplot data=out;
plot x*t=2 xp*t=3/overlay;
symbol2  v=star i=none c=black;
symbol3  v=none i=join c=red w=2;
run;
````

</details>

#### 例5.1 · SAS · b34cc207

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`080fdcd2954a0047722fe59787352bfce36f5003e1bdcfc4925167c090344b5b`
- 语言：SAS
- 符号：`PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input year sha;
dif=dif(sha);
cards;
1964	97
1965	130
1966	156.5
1967	135.2
1968	137.7
1969	180.5
1970	205.2
1971	190
1972	188.6
1973	196.7
1974	180.3
1975	210.8
1976	196
1977	223
1978	238.2
1979	263.5
1980	292.6
1981	317
1982	335.4
1983	327
1984	321.9
1985	353.5
1986	397.8
1987	436.8
1988	465.7
1989	476.7
1990	462.6
1991	460.8
1992	501.8
1993	501.5
1994	489.5
1995	542.3
1996	512.2
1997	559.8
1998	542
1999	567
;
proc gplot;
plot sha*year dif*year;
symbol v=star c=red i=join;
run;
````

</details>

#### 例5.12 · SAS · b7517368

- 归属算法：绘图可视化
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC AUTOREG`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`f3ffe0e5c15804aa9bc69cf5fbc4de3dfed22505cde27c7455439bfee6a7310c`
- 语言：SAS
- 符号：`PROC AUTOREG`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.12.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input a@@;
laga=lag(a);
t=_n_;
cards;
143.1	140.3	139.4	140.7	139.6	140.4	141.2	140.9	141.3	141.7	142.8	144.7
144.4	140.9	139.5	140.8	138.7	139	140	140.4	141.6	142.3	143.4	145.7
145.7	142.8	141.8	143.5	141.8	142.4	142.8	142.7	144.3	145.7	147.6	150.5
150.2	146.9	146	148	145.8	146.2	146.4	145.8	146.9	148.4	150.2	153.3
153.6	150.1	149.3	151.5	149.3	151.4	151.3	150.9	152.5	154.4	156.7	159
159.4	155.4	154.6	156.8	154.2	155.5	157.1	157	159.4	161.3	163.1	166.4
166.9	161.9	161.5	164.2	160.3	162.2	163.5	162.8	165.6	168.2	169.9	174.4
175.6	170.3	170.4	174.1	169.6	171.7	171	170	172.7	173.4	174.6	178.6
178.4	173.4	174.6	176.6	174.1	177.4	179.1	179	181.7	183.9	185.7	190.3
189	184.9	185.4	189.3	186.5	190.2	191.9	191.4	193.9	196.3	199.6	204.8
205.9	199.3	199.8	203.6	199.4	202.3	203.3	201.5	203.2	205	207	211.4
212.9	204	205.5	210.1	206.2	208.9	210.1	210	212.8	214.4	216.7	222.2
222.6	216.6	218.6	223.7	221.1	225.2	227.5	225.9	227.7	229.1	231.2	236.9
237.5	231.4	234.2	239.5	234.7	238.8	241.8	241.3	244.5	247	250.5	258.9
259.4	251.2	251.6	257	253.6	259.3	261.1	258.6	259.5	261.4	265.6	273.3
271.8	264.1	266.5	271.6	266.3	271.5	273.5	271	272.6	274.8	278.8	285.2
281.8	273.3	276.4	281.4	278.1	286	288	286.3	287.8	288.5	293.5	299
296.8	289	291.4	299.9	295.1	299.4	302.3	301	302.5	307	309.7	318.6
317.7	309	312.2	322.7	315.6	321.7	326.3	324.3	327.7	332	335.4	344.1
343.4	332	334.9	347.5	342.4	349.4	353.9	351.7	357	359.4	362.9	372.5
367.8	356.4	360.8	376.2	367.1	376.7	383.3	381.9	385.6	387.7	389.8	398.6
390.7	380.9	382.4	387.1	377.8	387.6	394.8	398.5	404.9	411	416.1	419.8
416.5	405.7	412.5	431.3	418.6	423	427.9	426.1	427.3	429.8	435.2	447.2
448.7	432.6	435.8	451.3	441.1	446.5	449.6	450	456.4	466	474.5	486
483	474.2	482.9	498.7	494.1	503.7	510.7	508.5	511.5	517.4	522.1	533.4
530.4	517.6	524.2	539.2	530.8	541.4	543.3	539	542.5	542.1	549.6	564.5
561.1	551.9	558.3	575	569.4	585.2	592	594.8	602.2	605.5	615.1	633.5
626.8	613.1	624.6	647.2	645.7	663.5	674	679.1	685.2	692.8	709.5	740.6
737.5	717.1	723.5	752.5	739.9	744.4	746.8	745	745.2	753.7	756	765.9
764.7	745	752.1	778.3	763.8	778.8	785.6	781.3	780	780.8	787.1	803.2
793	772.3	775.2	791.3	767.2	773.8	781.7	777.4	778.5	784.5	791.4	811.9
802.4	788.3	796.2	818	797.3	810.8	812.9	814.5	818.9	817.6	826.1	844.3
833.2	823.4	835	852.9	841.9	857.8	861.9	864.2	867.3	875	893.4	916.8
918.1	916.5										
;
proc gplot;
plot a*T;
symbol v=none i=join c=black;
proc autoreg;
model a=laga/lagdep=laga nlag=2 garch=(p=1,q=1);
output out=out p=forecast ;
proc gplot;
plot a*t=1 forecast*t=2 /overlay;
symbol1 c=black v=star i=none h=0.1;
symbol2 c=red v=none i=join;
run;
````

</details>

#### 例5.2 · SAS · f9f2c651

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`83688c42cdd4caee988218d069f15ff2ddb55ada8974aa8f4015dd844d002854`
- 语言：SAS
- 符号：`PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input year x;
dif1=dif(x);
dif2=dif(dif1);
cards;
1950	5.43
1951	6.19
1952	6.63
1953	7.18
1954	8.95
1955	10.14
1956	11.74
1957	12.6
1958	17.26
1959	21.07
1960	22.38
1961	24
1962	24.8
1963	26.13
1964	27.61
1965	29.95
1966	33.92
1967	33.21
1968	34.8
1969	37.16
1970	42.41
1971	49.44
1972	57.74
1973	67.27
1974	78.57
1975	91.71
1976	106.7
1977	119.93
1978	135.84
1979	155.49
1980	178.29
1981	199.14
1982	215.75
1983	232.63
1984	260.41
1985	321.12
1986	361.95
1987	408.07
1988	464.38
1989	511.32
1990	551.36
1991	606.11
1992	691.74
1993	817.58
1994	941.95
1995	1040
1996	1100.08
1997	1219.09
1998	1319.3
1999	1452.94
;
proc gplot;
plot x*year dif1*year dif2*year;
symbol v=star c=red i=join;
run;
````

</details>

#### 例5.3 · SAS · 1f4a6f29

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fb1fc6fb1dce621db1b8262c67acbf9a5c291ada0a06cd5b322a0c2bec939745`
- 语言：SAS
- 符号：`PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.3.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input milk@@;
time=intnx('month','1jan1962'd,_n_-1);
format time year4.;
dif1=dif(milk);
dif1_12=dif12(dif1);
cards;
589	561	640	656	727	697	640	599
568	577	553	582	600	566	653	673
742	716	660	617	583	587	565	598
628	618	688	705	770	736	678	639
604	611	594	634	658	622	709	722
782	756	702	653	615	621	602	635
677	635	736	755	811	798	735	697
661	667	645	688	713	667	762	784
837	817	767	722	681	687	660	698
717	696	775	796	858	826	783	740
701	706	677	711	734	690	785	805
871	845	801	764	725	723	690	734
750	707	807	824	886	859	819	783
740	747	711	751	804	756	860	878
942	913	869	834	790	800	763	800
826	799	890	900	961	935	894	855
809	810	766	805	821	773	883	898
957	924	881	837	784	791	760	802
828	778	889	902	969	947	908	867
815	812	773	813	834	782	892	903
966	937	896	858	817	827	797	843
;
proc gplot;
plot milk*time dif1*time dif1_12*time;
symbol v=star c=red i=join;
run;
````

</details>

#### 例5.5 · SAS · e44f1b25

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`163f5a95ab9c94b9e90b1d2bce8da2c717847b31de5a1ae46f07ad8d7df9151e`
- 语言：SAS
- 符号：`PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.5.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
x0=0;
do t=-10 to 1000;
rand=10*rannor(12345);
x=x0+rand;
x0=x;
if t>0 then output;
end;
proc gplot;
plot x*t;
symbol v=none c=black i=join;
run;
````

</details>

#### example4_1 · SAS · 5201a1fa

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC AUTOREG`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`30c81dee30adeda2bbbd5d37a83d9b786757aab8602bedd70e010a4d2f65c3ff`
- 语言：SAS
- 符号：`PROC AUTOREG`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第四章/example4_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
 data example4_1;
input x@@;
t=_n_;
cards;
12.79 	14.02 	12.92 	18.27 	21.22 	18.81 
25.73 	26.27 	26.75 	28.73 	31.71 	33.95 
;
proc autoreg  data=example4_1;
model x=t;
output out=result p=xcap;
proc gplot data=result;
plot x*t=1 xcap*t=2/overlay;
symbol1 c=black v=star i=none;
symbol2 c=red v=none i=join;
run;
````

</details>

#### example4_2 · SAS · dbbc54d8

- 归属算法：绘图可视化
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“预测与推断”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`、`PROC NLIN`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`5b15293401992ba05a9f0c1b1ad8fe4ef7ed0dc62c78f8e4ad6293bccee8efdf`
- 语言：SAS
- 符号：`PROC GPLOT`, `PROC NLIN`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第四章/example4_2.sas`

<details>
<summary>展开原始代码</summary>

````sas
 data example4_2;
input x@@;
t=_n_;
cards;
1.85 	7.48 	14.29 	23.02 	37.42 	74.27 	140.72 
265.81 	528.23 	1040.27 	2064.25 	4113.73 	8212.21 	16405.95 
；
proc nlin;   
model x=a*t+b**t;                                                                                                                       
parameters  a=0.1  b=0.1;                                                                                                                 
der.a=t;                                                                                                                                
der.b=log(b)*b**t;                                                                                                                      
output  predicted=xhat out=result;                                                                                                                                                                                                             
proc gplot data=result;                                                                                                                    
plot x*t=1 xhat*t=2/overlay;                                                                                                            
symbol1 c=black i=none v=star;                                                                                                          
symbol2 c=red i=join v=none;                                                                                                            
run;  
````

</details>

#### example4_3 · SAS · 20e774ba

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`、`PROC X11`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`1c98a0f26d6bcf7206001806a124833ad33a361f38a702e7c6a1b62ac6ec6861`
- 语言：SAS
- 符号：`PROC GPLOT`, `PROC X11`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第四章/example4_3.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example4_3;                                                                                                                             
input x@@;                                                                                                                              
t=intnx('quarter','1jan1978'd,_n_-1);                                                                                                   
format t yyq4.;                                                                                                                         
cards;                                                                                                                                  
40777      41778      43160      45897                                                                                                  
41947      44061      44378      47237                                                                                                  
43315      43396      44843      46835                                                                                                  
42833      43548      44637      47107                                                                                                  
42552      43526      45039      47940                                                                                                  
43740      45007      46667      49325                                                                                                  
44878      46234      47055      50318                                                                                                  
46354      47260      48883      52605                                                                                                  
48527      50237      51592      55152                                                                                                  
50451      52294      54633      58802                                                                                                  
53990      55477      57850      61978                                                                                                  
;                                                                                                                                       
proc x11 data=example4_3;                                                                                                                               
quarterly date=t;                                                                                                                       
var x;                                                                                                                                  
output  out=out  b1=x d10=season d11=adjusted d12=trend d13=irr;                                                                                                      
proc gplot data=out;  
plot season*t=2 trend*t=2 irr*t=2;  
plot x*t=1 adjusted*t=2/overlay; 
symbol1 c=black i=join v=star;                                                                                                          
symbol2 c=red i=join v=none w=2;                                                                                                            
run; 
````

</details>

#### 例4.5 · SAS · 34c42c69

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`939ab492f44a9a9c5df8f163980a106526d4f5daa9ab547797fc771774c16484`
- 语言：SAS
- 符号：`PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第四章/例4.5.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input year circu circup;
cards;
1980    75095   46449.4
1981    78371   50457.61
1982    78984   54725.55
1983    86499   58799.93
1984    98628   63693.16
1985    99941   70013.85
1986    103630  76012.59
1987    109547  82023.81
1988    113375  88344.98
1989    82999   94610.2
1990    87489   95660.72
1991    94339   97037.23
1992    114824  99091.54
1993    127791  103839.2
1994    114373  109984.5
1995    112577  113462.4
1996    136308  116162.9
1997    130754  121964.1
1998    140870  126277.3
1999    148039  131528
2000    146395  137206.6
;
proc gplot;
plot circu*year=1 circup*year=2/overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例4_7（续） · SAS · c9bb1935

- 归属算法：绘图可视化
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“核心算法与辅助函数”。
- **执行主线**：按DATA/PROC流程完成统计计算并输出过程结果。
- **调用方式**：优先调用 `PROC GPLOT`、`PROC X11`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c924eaf1c54df1379c44cb342c4c2e795e2b02fe73d6977a129b9eb897c043c9`
- 语言：SAS
- 符号：`PROC GPLOT`, `PROC X11`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第四章/例4_7（续）.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;                                                                                                                             
input x@@;                                                                                                                              
t=intnx('month','1jan1993'd,_n_-1);                                                                                                   
format t year4.;                                                                                                                         
cards;                                                                                                                                  
977.5	892.5	942.3	941.3	962.2	1005.7	963.8	959.8	1023.3	1051.1	1102	1415.5
1192.2	1162.7	1167.5	1170.4	1213.7	1281.1	1251.5	1286	1396.2	1444.1	1553.8	1932.2
1602.2	1491.5	1533.3	1548.7	1585.4	1639.7	1623.6	1637.1	1756	1818	1935.2	2389.5
1909.1	1911.2	1860.1	1854.8	1898.3	1966	1888.7	1916.4	2083.5	2148.3	2290.1	2848.6
2288.5	2213.5	2130.9	2100.5	2108.2	2164.7	2102.5	2104.4	2239.6	2348	2454.9	2881.7
2549.5	2306.4	2279.7	2252.7	2265.2	2326	2286.1	2314.6	2443.1	2536	2652.2	3131.4
2662.1	2538.4	2403.1	2356.8	2364	2428.8	2380.3	2410.9	2604.3	2743.9	2781.5	3405.7
2774.7	2805	2627	2572	2637	2645	2597	2636	2854	3029	3108	3680
;                                                       
proc x11 data=a;                                                                                                                               
monthly date=t;                                                                                                                       
var x;                                                                                                                                  
output  out=out  b1=x d10=season d11=adjusted d12=trend d13=irr;                                                                                                      
proc gplot data=out;  
plot season*t=2 adjusted*t=2 trend*t=2 irr*t=2;  
plot x*t=1 adjusted*t=2/overlay; 
symbol1 c=black i=join v=star;                                                                                                          
symbol2 c=red i=join v=none w=2;                                                                                                            
run; 
````

</details>

#### Pex3_16 · Python · ebdaa1ba

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：优先调用 `fac`、`item`、`mysin`；先核对参数顺序和返回值。
- **主要输出**：函数返回值、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`1c4758c24811ecfbf5ebffdd7468bce0fca73a2dd08deb656402db4b4bf24abb`
- 语言：Python
- 符号：`fac`, `item`, `mysin`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/03第3章  Python在高等数学和工程数学的应用(Python 程序及数据)/Pex3_16.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex3_16.py
import numpy as np
import matplotlib.pyplot as plt
def fac(n): return (1 if n<1 else n*fac(n-1))
def item(n,x): return (-1)**n*x**(2*n+1)/fac(2*n+1)
def mysin(n,x): return (0 if n<0 else mysin(n-1,x)+item(n,x))
x=np.linspace(-2*np.pi,2*np.pi,101)
plt.plot(x,np.sin(x),'*-')
str=['v-','H--','-.']
for n in [1,2,3]: plt.plot(x,mysin(2*n-1,x),str[n-1])
plt.legend(['sin','n=1','n=3','n=5'])
plt.savefig('figure3_16.png',dpi=500); plt.show()
````

</details>

#### Pex3_17 · Python · 0b7a24e6

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`b320036cf558ff6cbbf6c94bc4b8370696a646476366336cc21f54c446409b2d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/03第3章  Python在高等数学和工程数学的应用(Python 程序及数据)/Pex3_17.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex3_17.py
import numpy as np, numpy.linalg as ng
import matplotlib.pyplot as plt
N=4; v=1.0; d=200.0; time=400.0; divs=201
xy=np.array([[-d,d],[d,d],[d,-d],[-d,-d]])
T=np.linspace(0,time,divs); dt=T[1]-T[0]
xyn=np.empty((4,2)); Txy=xy
for n in range(1,len(T)):
    for i in [0,1,2,3]:
        j=(i+1)%4; dxy=xy[j]-xy[i]
        dd=dxy/ng.norm(dxy) #单位化向量
        xyn[i]=xy[i]+v*dt*dd; #计算下一步的位置
    Txy=np.c_[Txy,xyn]; xy=xyn
for i in range(N):plt.plot(Txy[i,::2],Txy[i,1::2])
plt.savefig("figure3_17.png",dpi=500); plt.show()
````

</details>

#### Pex3_3 · Python · 44bd9066

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a763203f1247fe6db6edf9e8cfd11f6d0318f03e5c7d2bcbe1511bdf25efd8d5`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/03第3章  Python在高等数学和工程数学的应用(Python 程序及数据)/Pex3_3.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex3_3.py
from sympy.plotting import plot
from sympy.abc import x,pi   #引进符号变量x及常量pi
from sympy.functions import sin,cos
plot((2*sin(x),(x,-6,6)),(cos(x+pi/4),(x,-5,5)))
````

</details>

#### Pex3_42 · Python · 1a40adc6

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`7ce5b9f3d0836bfc4ee87d858ed04f682fb11f6b87e9e19ef540d573027c64a0`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/03第3章  Python在高等数学和工程数学的应用(Python 程序及数据)/Pex3_42.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex3_42.py
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
t = np.arange(8)
y=np.array([27.0,26.8,26.5,26.3,26.1,25.7,25.3,24.8]) 
A = np.c_[t, np.ones_like(t)]
ab = LA.lstsq(A, y, rcond=None)[0]  #返回值为向量
print(ab); plt.rc('font',size=16)
plt.plot(t, y, 'o', label='Original data', markersize=5)
plt.plot(t, A.dot(ab), 'r', label='Fitted line')
plt.legend(); plt.savefig("figure3_42.png",dpi=500); plt.show()
````

</details>

#### Pex3_9 · Python · 03f71b1f

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`46490f1d56ec1b1c624e2588b3fc22486f28c6d2bca8952b2f640bec9f66915e`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/03第3章  Python在高等数学和工程数学的应用(Python 程序及数据)/Pex3_9.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex3_9.py
from pylab import rc
from sympy import *
rc('font',size=16); rc('text',usetex=True)
x=symbols('x'); y=sin(x)
for k in range(3,8,2): print(y.series(x,0,k))  #等价于print(series(y,x,0,k))
plot(y,series(y,x,0,3).removeO(),series(y,x,0,5).removeO(),
     series(y,x,0,7).removeO(),(x,0,2),xlabel='$x$',ylabel='$y$')
````

</details>

#### Pex4_12 · Python · ff46ac66

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`a559bdfc57f00252763cb14102f2d100e6862577bcb3b5dc8baed61d452f9c90`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/04第4章  概率论与数理统计(Python 程序及数据)/Pex4_12.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex4_12.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, probplot
a=np.loadtxt("Pdata4_6_2.txt")
h=a[:,::2]; h=h.flatten()
mu=np.mean(h); s=np.std(h); print([mu,s])
sh=np.sort(h) #按从小到大排序
n=len(sh); xi=(np.arange(1,n+1)-1/2)/n
yi=norm.ppf(xi,mu,s)
plt.rc('font',size=16);plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False) #用来正常显示负号
plt.subplot(121); plt.plot(yi, sh, 'o', label='QQ图');
plt.plot([155,185],[155,185],'r-',label='参照直线')
plt.legend(); plt.subplot(122)
res = probplot(h,plot=plt)
plt.savefig("figure4_12.png",dpi=500); plt.show()
````

</details>

#### Pex4_2 · Python · 69edb010

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`d479ba8553c2af6358277551c13c6ebe1a6dfc2ffc7900e5b638135fa4fe0e74`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/04第4章  概率论与数理统计(Python 程序及数据)/Pex4_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex4_2.py
from scipy.stats import norm
from pylab import plot,fill_between,show,text,savefig,rc 
from numpy import array, linspace, zeros
alpha=array([0.001, 0.005, 0.01, 0.025, 0.05, 0.10])
za=norm.ppf(1-alpha,0,1)  #求上alpha分位数
print("上alpha分位数分别为", za)
x=linspace(-4, 4, 100); y=norm.pdf(x, 0, 1)
rc('font',size=16); rc('text',usetex=True)
plot(x,y)  #画标准正态分布密度曲线
x2=linspace(za[-1],4,100); y2=norm.pdf(x2);
y1=[0]*len(x2)
fill_between(x2, y1, y2, color='r')  #y1,y2对应的点之间填充
plot([-4,4],[0,0])  #画水平线
text(1.9, 0.07, "$\\leftarrow\\alpha$=0.1")  #标注
savefig("figure4_2.png", dpi=500); show()
````

</details>

#### Pex8_12 · Python · fd7e3e17

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4da19b4195ec73dbec805fc3ffc2c3e63435a6f65e0912afae2b40a9cc5ef20c`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/08第8章  微分方程模型(Python 程序及数据)/Pex8_12.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex8_12.py
import sympy as sp
import pylab as plt
import numpy as np
sp.var('t',positive=True); sp.var('s')  #定义符号变量
sp.var('X,Y',cls=sp.Function)  #定义符号函数
g=40*sp.sin(3*t)
Lg=sp.laplace_transform(g,t,s)  
eq1=2*s**2*X(s)+6*X(s)-2*Y(s)
eq2=s**2*Y(s)-2*X(s)+2*Y(s)-Lg[0]
eq=[eq1,eq2]    #定义取拉氏变换后的代数方程组
XYs=sp.solve(eq,(X(s),Y(s)))  #求像函数
Xs=XYs[X(s)]; Ys=XYs[Y(s)]
Xs=sp.factor(Xs); Ys=sp.factor(Ys)
xt=sp.inverse_laplace_transform(Xs,s,t)
yt=sp.inverse_laplace_transform(Ys,s,t)
print("x(t)=",xt); print("y(t)=",yt)
fx=sp.lambdify(t,xt,'numpy')  #转换为匿名函数
fy=sp.lambdify(t,yt,'numpy')
t=np.linspace(-5,5,100)
plt.rc('text',usetex=True)
plt.plot(t,fx(t),'*-k',label='$x(t)$')
plt.plot(t,fy(t),'.-r',label='$y(t)$')
plt.xlabel('$t$'); plt.legend(); plt.show()
````

</details>

#### Pex10_18 · Python · 2a662637

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`e3d250da14fad648d30791af8885aad4101d4458e093d7baeede7f0939d3c10d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/10第10章  图论模型(Python 程序及数据)/Pex10_18.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex10_18.py
import numpy as np,networkx as nx
import pylab as plt
from scipy.sparse.linalg import eigs
L=[(1,2),(2,3),(2,4),(3,4),(3,5),(3,6),
   (4,1),(5,6),(6,1)]
G=nx.DiGraph()
G.add_nodes_from(range(1,7))  #添加顶点集
G.add_edges_from(L)  #添加边集
B=np.array(nx.to_numpy_matrix(G))  #提取邻接矩阵
plt.rc('font',size=16); pos=nx.shell_layout(G)
nx.draw(G,pos,node_size=280,font_weight='bold',
        node_color='r',with_labels=True)
plt.savefig("figure10_18_1.png")
A=B/np.tile(B.sum(axis=1,keepdims=True),(1,B.shape[1]))
A=0.15/B.shape[0]+0.85*A  #计算状态转移概率矩阵
print("A=",A)
W,V=eigs(A.T,1); V=V.real
V=V.flatten(); #展开成（n,)形式的数组
V=V/V.sum(); print("V=",V); plt.figure(2)
plt.bar(range(1,B.shape[0]+1),V, width=0.6, color='b')
plt.savefig("figure10_18_2.png"); plt.show()
````

</details>

#### Pex17_1 · Python · 66882e7e

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`373fcb07c3ae8545ed96084b7e630c9e8bc6fa9634223809c4601a9669a4e567`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/17第17章  智能算法(Python 程序及数据)/Pex17_1.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex17_1.py
from numpy import loadtxt,radians,sin,cos,inf,exp
from numpy import array,r_,c_,arange,savetxt
from numpy.lib.scimath import arccos
from numpy.random import shuffle,randint,rand
from matplotlib.pyplot import plot, show, rc
a=loadtxt("Pdata17_1.txt")
x=a[:,::2]. flatten(); y=a[:,1::2]. flatten()
d1=array([[70,40]]); xy=c_[x,y]
xy=r_[d1,xy,d1]; N=xy.shape[0]
t=radians(xy)  #转化为弧度
d=array([[6370*arccos(cos(t[i,0]-t[j,0])*cos(t[i,1])*cos(t[j,1])+
  sin(t[i,1])*sin(t[j,1])) for i in range(N)]
       for j in range(N)]).real
savetxt('Pdata17_2.txt',c_[xy,d])  #把数据保存到文本文件，供下面使用
path=arange(N); L=inf
for j in range(1000):
    path0=arange(1,N-1); shuffle(path0)
    path0=r_[0,path0,N-1]; L0=d[0,path0[1]]  #初始化
    for i in range(1,N-1):L0+=d[path0[i],path0[i+1]]
    if L0<L: path=path0; L=L0
print(path,'\n',L)        
e=0.1**30; M=20000; at=0.999; T=1
for k in range(M):
    c=randint(1,101,2); c.sort()
    c1=c[0]; c2=c[1]
    df=d[path[c1-1],path[c2]]+d[path[c1],path[c2+1]]-\
    d[path[c1-1],path[c1]]-d[path[c2],path[c2+1]]  #续行
    if df<0:
        path=r_[path[0],path[1:c1],path[c2:c1-1:-1],path[c2+1:102]]; L=L+df
    else:
        if exp(-df/T)>=rand(1):
            path=r_[path[0],path[1:c1],path[c2:c1-1:-1],path[c2+1:102]]
            L=L+df
    T=T*at
    if T<e: break
print(path,'\n',L)  #输出巡航路径及路径长度
xx=xy[path,0]; yy=xy[path,1]; rc('font',size=16)
plot(xx,yy,'-*'); show()  #画巡航路径
````

</details>

#### Pex17_2 · Python · e8d8d24e

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：重复随机采样并汇总模拟结果；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数；含随机过程但未发现固定随机种子。

- SHA-256：`5581560057b240cc1402b94709bee2c0d4a80fe1f21f2239249f693fb5870e49`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/17第17章  智能算法(Python 程序及数据)/Pex17_2.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex17_2.py
import numpy as np
from numpy.random import randint, rand, shuffle
from matplotlib.pyplot import plot, show, rc
a=np.loadtxt("Pdata17_2.txt")
xy,d=a[:,:2],a[:,2:]; N=len(xy)
w=50; g=10  #w为种群的个数，g为进化的代数
J=[]; 
for i in np.arange(w):
    c=np.arange(1,N-1); shuffle(c)
    c1=np.r_[0,c,101]; flag=1
    while flag>0:
        flag=0
        for m in np.arange(1,N-3):
            for n in np.arange(m+1,N-2):
                if d[c1[m],c1[n]]+d[c1[m+1],c1[n+1]]<\
                   d[c1[m],c1[m+1]]+d[c1[n],c1[n+1]]:
                    c1[m+1:n+1]=c1[n:m:-1]; flag=1
    c1[c1]=np.arange(N); J.append(c1)
J=np.array(J)/(N-1)
for k in np.arange(g):
    A=J.copy()
    c1=np.arange(w); shuffle(c1) #交叉操作的染色体配对组
    c2=randint(2,100,w)  #交叉点的数据
    for i in np.arange(0,w,2):
        temp=A[c1[i],c2[i]:N-1]  #保存中间变量
        A[c1[i],c2[i]:N-1]=A[c1[i+1],c2[i]:N-1]
        A[c1[i+1],c2[i]:N-1]=temp
    B=A.copy()
    by=[]  #初始化变异染色体的序号
    while len(by)<1: by=np.where(rand(w)<0.1)
    by=by[0]; B=B[by,:]
    G=np.r_[J,A,B]
    ind=np.argsort(G,axis=1)  #把染色体翻译成0,1，…，101
    NN=G.shape[0]; L=np.zeros(NN)
    for j in np.arange(NN):
        for i in np.arange(101):
            L[j]=L[j]+d[ind[j,i],ind[j,i+1]]
    ind2=np.argsort(L)
    J=G[ind2,:]
path=ind[ind2[0],:]; zL=L[ind2[0]]
xx=xy[path,0]; yy=xy[path,1]; rc('font',size=16)
plot(xx,yy,'-*'); show()  #画巡航路径
print("所求的巡航路径长度为：",zL)
````

</details>

#### Pex17_5 · Python · 0fb0a875

- 归属算法：绘图可视化
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[#绘图可视化 · 复习]]
- 验证状态：`raw-unverified`；自动归类不代表算法或结果已经验证。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于绘图可视化中的“结果绘图与展示”。
- **执行主线**：估计回归系数并生成拟合/预测；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`677e0c5787a700e369ce9304a2526aa1f9dd76323943977a126b72e893b40b7d`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/17第17章  智能算法(Python 程序及数据)/Pex17_5.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex17_5.py
from sklearn.neural_network import MLPRegressor
from numpy import array, loadtxt
from pylab import subplot, plot, show, xticks,rc,legend
rc('font',size=15); rc('font',family='SimHei')
a=loadtxt("Pdata17_5.txt"); x0=a[:,:3]; y1=a[:,3]; y2=a[:,4];
md1=MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=10)
md1.fit(x0, y1); x=array([[73.39,3.9635,0.988],[75.55,4.0975,1.0268]])
pred1=md1.predict(x); print(md1.score(x0,y1)); 
print("客运量的预测值为：",pred1,'\n----------------'); 
md2=MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=10)
md2.fit(x0, y2); pred2=md2.predict(x); print(md2.score(x0,y2)); 
print("货运量的预测值为：",pred2); yr=range(1990,2010)
subplot(121); plot(yr,y1,'o'); plot(yr,md1.predict(x0),'-*')
xticks(yr,rotation=55); legend(("原始数据","网络输出客运量"))
subplot(122); plot(yr,y2,'o'); plot(yr,md2.predict(x0),'-*')
xticks(yr,rotation=55)
legend(("原始数据","网络输出货运量"),loc='upper left'); show()
````

</details>

<!-- END AUTO-INTEGRATED-CODE -->
