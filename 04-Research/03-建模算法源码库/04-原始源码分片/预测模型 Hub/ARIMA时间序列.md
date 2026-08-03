---
type: generated-code-shard
status: generated
topic_hub: 预测模型 Hub
algorithm: ARIMA时间序列
tags: [area/数学建模, workflow/源码索引, status/待运行验证]
---

<!-- GENERATED-CODE-SHARD: DO NOT EDIT BY HAND -->

# ARIMA时间序列 · 原始源码实现

> [!warning] 使用边界
> 本页由本地目录自动生成，保留源码、SHA-256 与原始路径。静态检查不等于运行正确；正式调用前必须补齐依赖、最小样例和结果检验。

- 领域入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub|预测模型 Hub]]
- 独立实现：28
- 原始来源：28
- 逐文件状态：[[04-Research/03-建模算法源码库/代码验证报告|代码验证报告]]

利用差分、自回归和移动平均结构进行时间序列建模与预测。

#### ch37_chun_sui_ji_xing_jian_yan1 · SAS · ac6519cb

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`859aa72cdaf6864683948d1882f779efeff8fc8b11773f2e2fa43113b86303ff`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch37_chun_sui_ji_xing_jian_yan1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data ex1;
input price @@;
time=intnx('week','13oct2006'd,_n_-1);
format time date7.;
cards;
10.3000 8.5269 9.0421 10.1727 9.9079 8.9714 9.0145 9.4738 9.5258 9.7017
10.0582 9.5292 8.9786 9.1743 9.8478 9.6218 9.0342 9.1891 9.6062 9.8946 
9.4853 9.2557 9.2805 9.5258 10.1192 9.6384 8.8495 9.2644 9.4939 9.6623
9.4212 9.5570 9.7627 9.5639 8.7962 9.1777 10.2288 10.3722 9.0861 8.8148  
9.2055 9.4473 9.2903 9.5358 9.5294 9.5368 9.4168 9.3237 9.5939 9.8874  
10.3007 9.3051 8.6804 9.5337 9.8757 9.2799 9.3030 10.0135 10.1025 10.1310
9.6605 9.8175 9.4935 9.0052 9.2178 10.0131 9.6019 9.4843 9.2807 9.4567
;
run;
proc gplot;
plot price*time/ vaxis=8.5 to 10.5 by 0.1;
symbol i=join v=star cv=red ci=green;
run;
/*proc arima data=ex1;
identify var=price;
run;*/
/*proc arima data=ex1;
identify var=price minic p=(0:6) q=(0:6);
run;*/
proc arima data=ex1;
identify var=price;
estimate p=2 method=ml;
run;
````

</details>

#### ch37_chun_sui_ji_xing_jian_yan2 · SAS · 6319fb79

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`762d9b4ef5a7b3909f7fb8ac4bcf20a28ee760d25f0f8a2e074f4baad0a562b6`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch37_chun_sui_ji_xing_jian_yan2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data datas1;
  input x_t @@;
  time=intnx('day','01jan2014'd,_n_-1);
  format time monyy.;
  cards;
    10	15	10	10	12	10	7	7	10	14	8	17
    14	18	3	9	11	10	6	12	14	10	25	29
    33	33	12	19	16	19	19	12	34	15	36	29
    26	21	17	19	13	20	24	12	6	14	6	12
    9	11	17	12	8	14	14	12	5	8	10	3
    16	8	8	7	12	6	10	8	10	5		
;
run;
proc gplot data = datas1;
plot x_t*time;
symbol i=join v=star cv=red ci=green;
run;
proc arima data = datas1;
identify var=x_t nlag=24; 
run;
data datas2;
set datas1;
y_t = dif1(x_t);
run;
proc gplot data = datas2;
plot y_t*time;
symbol i=join v=star cv=red ci=green;
run;
proc arima data = datas2;
identify var=y_t nlag=24; 
run;
````

</details>

#### ch38_yue_du_shu_ju_ji_jie_tiao_zheng · SAS · d31e3107

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC PRINT`、`PROC SGPLOT`、`PROC X11`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`125956ed3cebb0d08ffb48e3eaa440557690966ce3e6750932178bb85b5867a8`
- 语言：SAS
- 符号：`PROC PRINT`, `PROC SGPLOT`, `PROC X11`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch38_yue_du_shu_ju_ji_jie_tiao_zheng.sas`

<details>
<summary>展开原始代码</summary>

````sas
data sales;
input sales @@;
date = intnx( 'month', '01jan1993'd, _n_-1 );
format date monyy5.;
datalines;
977.5	892.5	942.3	941.3	962.2	1005.7	963.8	959.8	1023.3	1051.1	1102	1415.5
1192.2	1162.7	1167.5	1170.4	1213.7	1281.1	1251.5	1286	1396.2	1444.1	1553.8	1932.2
1602.2	1491.5	1533.3	1548.7	1585.4	1639.7	1623.6	1637.1	1756	1818	1935.2	2389.5
1909.1	1911.2	1860.1	1854.8	1898.3	1966	1888.7	1916.4	2083.5	2148.3	2290.1	2848.6
2288.5	2213.5	2130.9	2100.5	2108.2	2164.7	2102.5	2104.4	2239.6	2348	2454.9	2881.7
2549.5	2306.4	2279.7	2252.7	2265.2	2326	2286.1	2314.6	2443.1	2536	2652.2	3131.4
2662.1	2538.4	2403.1	2356.8	2364	2428.8	2380.3	2410.9	2604.3	2743.9	2781.5	3405.7
2774.7	2805	2627	2572	2637	2645	2597	2636	2854	3029	3108	3680
;
run;
proc x11 data=sales;
monthly date=date;
var     sales;
arima   maxit=60;
tables  d11;
output  out=out b1=series d10=season d11=adjusted d12=trend d13=irr;
proc print data=out;
run ;
title 'Monthly Retail Sales Data';
proc sgplot data=out;
series x=date y=series / markers
markerattrs=(color=red symbol='asterisk')
lineattrs=(color=red)
legendlabel="original" ;
series x=date y=adjusted / markers
markerattrs=(color=blue symbol='circle')
lineattrs=(color=blue)
legendlabel="adjusted" ;
yaxis label='Original and Seasonally Adjusted Time Series';
run;
title 'Monthly Seasonal Factors (in percent)';
proc sgplot data=out;
series x=date y=season / markers markerattrs=(symbol=CircleFilled) ;
run;
title 'Monthly Retail Sales Data (in $1000)';
proc sgplot data=out;
series x=date y=trend / markers markerattrs=(symbol=CircleFilled) ;
run;
title 'Monthly Irregular Factors (in percent)';
proc sgplot data=out;
series x=date y=irr / markers markerattrs=(symbol=CircleFilled) ;
run;
````

</details>

#### ch39_ARIMA_sui_ji_fen_xi · SAS · fa831ed1

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`、`PROC PRINT`、`PROC SGPLOT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`77b91776c73b4e70492d08d66e645cccb67f4ac4f079191d9bc9bb0c91f778f6`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`, `PROC PRINT`, `PROC SGPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/张敬信-SAS学习系列/代码实例/ch39_ARIMA_sui_ji_fen_xi.sas`

<details>
<summary>展开原始代码</summary>

````sas
data arimad01;
date=intnx('month','31dec1948'd,_n_);
input x @@;
format date monyy5.;
datalines;
112	118	132	129	121	135	148	148	136	119	104	118
115	126	141	135	125	149	170	170	158	133	114	140
145	150	178	163	172	178	199	199	184	162	146	166
171	180	193	181	183	218	230	242	209	191	172	194
196	196	236	235	229	243	264	272	237	211	180	201
204	188	235	227	234	264	302	293	259	229	203	229
242	233	267	269	270	315	364	347	312	274	237	278
284	277	317	313	318	374	413	405	355	306	271	306
315	301	356	348	355	422	465	467	404	347	305	336
340	318	362	348	363	435	491	505	404	359	310	337
360	342	406	396	420	472	548	559	463	407	362	405
417	391	419	461	472	535	622	606	408	461	390	432
;
run;
proc sgplot data=arimad01;
series x=date y=x / markers;
run;
proc arima data=arimad01;
identify var=x;
run;
data arimad02;
set arimad01 ;
xlog=log(x);
run;
proc print data = arimad02;
run;
goptions reset=global gunit=pct cback=white border
             htitle=6 htext=3 ftext=swissb colors=(black);
proc gplot data=arimad02 ;
plot  xlog*date  / vaxis=axis1 haxis=axis2 
href='31dec1949'd to '1jan61'd by year;
plot2   x*date  /vaxis=axis3 vref=100;
symbol1 i=join v=c h=3 l=1 r=1 font=swissb c=green;
symbol2 i=join v=c h=3 l=1 r=1 font=swissb c=blue;
    axis1   label=('Log')       order=(4.5 to 6.5 by 0.5) offset=(0,45);
axis2   label=('12 Month')  order=('1jan49'd to '1jan61'd by year);
axis3   label=('Passenger') order=(100 to 700 by 100) offset=(23,0);
format  date monyy. ;
title1 'Time Serial Log Chart';
run;
data arimad03;
set arimad02;
dif12=dif1(xlog)-(lag1(xlog)-lag12(xlog));
run;
proc gplot data=arimad03 ;
plot    xlog*date   /vaxis=axis1 haxis=axis2 
href='31dec1949'd to '1jan61'd by year;
plot2   dif12*date  /vaxis=axis3 vref=-1;
symbol1 i=join v=c h=3 l=1 r=1 font=swissb c=green;
symbol2 i=join v=c h=3 l=1 r=1 font=swissb c=blue;
axis1   label=('Log')      order=(4.5 to 6.5 by 0.5) offset=(0,45);
axis2   label=('12 Month') order=('1jan49'd to '1jan61'd by year);
axis3   label=('Dif1-12')  order=(-1 to 1 by 0.2) offset=(23,0);
format  date monyy. ;
title1 'Time Serial Dif Chart';
run;
proc arima data=arimad02;
identify  var=xlog(1,12) nlag=15;
run;
proc arima data=arimad03;
identify var=xlog(1,12) nlag=15;
estimate q=(1)(12) p=(1)(12) noconstant outmodel=xmode;
run;
proc arima data=arimad03;
identify  var=xlog(1,12) nlag=15;
estimate  q=(1)(12)  noconstant outmodel=xmode;
forecast lead=12 interval=month id=date out=forxlog;
run;
proc print data=forxlog;
run;
data arimad04;
set forxlog;
x=exp(xlog);
forecast=exp(forecast);
l95=exp(l95);
u95=exp(u95);
proc print data=arimad04;
run;
proc gplot data=arimad04;
where date>='1jan57'd;
plot x*date forecast*date l95*date u95*date /overlay vaxis=axis1 haxis=axis2 href='31dec60'd ;
symbol1 i=join  v=C h=2.5 l=1 font=swissb c=red;
symbol2 i=join  v=F h=3   l=1 font=swissb c=blue;
symbol3 i=join  l=1 font=swissb c=green;
symbol4 i=join  l=1 font=swissb c=green;
axis1   label=('Passenger') order=(250 to 800 by 50);
axis2   label=('Month')     order=('1jan57'd to '1jan62'd by year);
format  date monyy. ;
title1 'Forecast Chart';
title2 'C--x';
title3 'F--forecast';
title4 'None--u95 and l95';
run;
````

</details>

#### 相似实现组 · SAS · 306693de

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：2
- 原始来源文件：2
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 变体 1：example3_1.sas

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`9d5cf548b36f9252c43073104f5736cc6f24bb5eeb50381a07c8467ca3b6a7f4`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/example3_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example3_1;                                                                                                                           
input x@@;                                                                                                                              
time=_n_;                                                                                                                               
cards;                                                                                                                                  
0.30	-0.45	0.36	0.00	0.17	0.45	2.15
4.42	3.48	2.99	1.74	2.40	0.11	0.96
0.21	-0.10	-1.27	-1.45	-1.19	-1.47	-1.34
-1.02	-0.27	0.14	-0.07	0.10	-0.15	-0.36
-0.50	-1.93	-1.49	-2.35	-2.18	-0.39	-0.52
-2.24	-3.46	-3.97	-4.60	-3.09	-2.19	-1.21
0.78	0.88	2.07	1.44	1.50	0.29	-0.36
-0.97	-0.30	-0.28	0.80	0.91	1.95	1.77
1.80	0.56	-0.11	0.10	-0.56	-1.34	-2.47
0.07	-0.69	-1.96	0.04	1.59	0.20	0.39
1.06	-0.39	-0.16	2.07	1.35	1.46	1.50
0.94	-0.08	-0.66	-0.21	-0.77	-0.52	0.05
； 
proc gplot data=example3_1;
plot x*time=1;
symbol1 c=red I=join v=star;   
proc arima data= example3_1;                                                                                                                             
identify var=x nlag=8;   
estimate q=4;
forecast lead=5 id=time out=results;
proc gplot data=results;                                                                                                                
plot x*time=1 forecast*time=2 l95*time=3 u95*time=3/overlay;                                                                            
symbol1 c=black i=none v=star;                                                                                                          
symbol2 c=red i=join v=none;                                                                                                            
symbol3 c=green i=join v=none l=2;                                                                                                          
run;
````

</details>

##### 变体 2：example6_1.sas

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`、`PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`82492837cfac22b87203b5a2ab63b676d37b6962cddef885d5fb1b1c77c3ba0f`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`, `PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第六章/example6_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
  data example6_1;                                                                                                                           
input x y@@;                                                                                                                              
t=_n_;                                                                                                                                  
cards;
-2.94 	9.83 	-2.14 	12.63 	1.01 	14.77 
2.84 	17.29 	-0.79 	18.07 	1.46 	17.38 
5.44 	19.17 	1.65 	9.12 	6.53 	22.82 
8.93 	23.58 	8.67 	15.19 	8.36 	22.43 
9.79 	17.83 	11.67 	25.49 	9.70 	28.40 
9.18 	23.15 	11.13 	19.70 	9.39 	22.32 
12.89 	30.01 	8.45 	21.27 	6.66 	11.52 
4.15 	15.57 	2.57 	9.91 	2.29 	23.28 
-3.28 	13.75 	-5.21 	3.38 	-3.74 	15.81 
-8.73 	12.41 	-15.89 	5.54 	-12.15 	4.83 
-10.86 	14.79 	-17.16 	4.14 	-18.55 	-5.36 
-11.42 	4.79 	-16.02 	0.91 	-14.36 	-5.49 
-17.98 	6.01 	-16.94 	2.78 	-17.52 	-2.49 
-13.44 	10.30 	-14.11 	-0.32 	-15.16 	2.35 
;
proc gplot data=example6_1;
plot x*t=1 y*t=2/overlay;
symbol1 c=black i=join v=none;
symbol2 c=red i=join v=none w=2 l=2;
proc arima data=example6_1;
identify var=x stationarity=(adf=1);                                                                                                                                                                                                 
identify var=y stationarity=(adf=1); 
proc reg data= example6_1;
model y=x;
output out=out residual=residual;
proc arima data=out;
identify var=residual stationarity=(adf);
proc arima data=example6_1;
identify var=y crosscorr=x;  
estimate input=x plot;
forecast lead=5 id=t out=result;
proc gplot data=result;
plot y*t=1 forecast*t=2 l95*t=3 u95*t=3/overlay;
symbol1 c=black i=none v=star;
symbol2 c=rd i=join v=none;
symbol3 c=green i=join v=none;
run;
````

</details>

#### 例3.13 · SAS · 1704e4ef

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`35617dc49dec4e4c11673954c52881e34bffb5c7863186b9c63a30ccdbaf509b`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.13.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input yield @@;
time=_n_;
cards;
47	64	23	71	38	64	55	41	59	48	71	35	57	40
58	44	80	55	37	74	51	57	50	60	45	57	50	45
25	59	50	71	56	74	50	58	45	54	36	54	48	55
45	57	50	62	44	64	43	52	38	59	55	41	53	49
34	35	54	45	68	38	50	60	39	59	40	57	54	23
;
proc gplot;
plot yield*time;
symbol v=star i=join c=red;
proc arima data=a;
identify var=yield nlag=18;
run;
````

</details>

#### 例3.5 · SAS · 74ad697c

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fb03732356fca16a9db7c5814e699c0c7bcf350c39b9e86cdf84cab6249ae753`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.5.sas`

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
do t=-100 to 1000;
e=rannor(12345);
x1=0.8*x1_0+e;
x2=-0.8*x2_0+e;
x3=x3_0-0.5*x3_1+e;
x4=-x4_0-0.5*x4_1+e;
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
proc arima;
identify var=x1 nlag=20 outcov=out1;
identify var=x2 nlag=20 outcov=out2;
identify var=x3 nlag=20 outcov=out3;
identify var=x4 nlag=20 outcov=out4;
proc gplot data=out1;
plot corr*lag ;
proc gplot data=out2;
plot corr*lag ;
proc gplot data=out3;
plot corr*lag ;
proc gplot data=out4;
plot corr*lag ;
proc gplot data=out1;
plot partcorr*lag ;
proc gplot data=out2;
plot partcorr*lag ;
proc gplot data=out3;
plot partcorr*lag ;
proc gplot data=out4;
plot partcorr*lag ;
symbol c=red i=needle v=none;
run;
````

</details>

#### 例3.6 · SAS · bb373875

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`2e11630e779f22dd44134ec46155253fbd3f140ded5f25fa7110a81d3ce12232`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.6.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
e_1=0;
e_2=0;
do t=-100 to 1000;
e=rannor(12345);
x1=e-2*e_1;
x2=e-0.5*e_1;
x3=e-4/5*e_1+16/25*e_2;
x4=e-5/4*e_1+25/16*e_2;
e_2=e_1;
e_1=e;
if t>0 then output ;
end;
data a;
set a;
keep t x1 x2 x3 x4;
proc arima;
identify var=x1 nlag=20 outcov=out1;
identify var=x2 nlag=20 outcov=out2;
identify var=x3 nlag=20 outcov=out3;
identify var=x4 nlag=20 outcov=out4;
proc gplot data=out1;
plot corr*lag ;
proc gplot data=out2;
plot corr*lag ;
proc gplot data=out3;
plot corr*lag ;
proc gplot data=out4;
plot corr*lag ;
proc gplot data=out1;
plot partcorr*lag ;
proc gplot data=out2;
plot partcorr*lag ;
proc gplot data=out3;
plot partcorr*lag ;
proc gplot data=out4;
plot partcorr*lag ;
symbol c=red i=needle v=none;
run;
````

</details>

#### 例3.7 · SAS · 54dbb8b0

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e6b67c23f61c5002a4999bddffe0b48161b112eeb5ef4cf714dfa9d89e5b720e`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.7.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
x_1=0;
e_1=0;
do t=-100 to 1000;
e=rannor(12345);
x=0.5*x_1+e-0.8*e_1;
x_1=x;
e_1=e;
if t>0 then output ;
end;
data a;
set a;
keep t x;
proc arima;
identify var=x nlag=20 outcov=out;
proc gplot data=out;
plot corr*lag partcorr*lag ;
symbol c=red i=needle v=none;
run;
````

</details>

#### 例3.8 · SAS · 54228bd3

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4e9479a3845ebe8f50bb9b7e9207d87ebeb1fa585d333895a5c27af2818f1263`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.8.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm;
data a;
input overshort@@;
day=_n_;
cards;
78	-58	53	-63	13	-6	-16	-14
3	-74	89	-48	-14	32	56	-86
-66	50	26	59	-47	-83	2	-1
124	-106	113	-76	-47	-32	39	-30
6	-73	18	2	-24	23	-38	91
-56	-58	1	14	-4	77	-127	97
10	-28	-17	23	-2	48	-131	65
-17							
;
proc gplot;
plot overshort*day;
symbol v=diamond i=join c=red;
proc arima data=a;
identify var=overshort;
estimate q=1;
run;
````

</details>

#### 例3.9 · SAS · e521ea2b

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`、`PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a145a8f0b96d6dc4f5d1e5df941091af67ad78a226c0aeac26db1737a2e34b3a`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`, `PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第三章/例3.9.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data a;
input change_temp@@;
dif=dif(change_temp);
year=1880+_n_-1;
cards;
-.40    -.37    -.43    -.47    -.72    -.54    -.47    -.54    -.39    -.19
-.40    -.44    -.44    -.49    -.38    -.41    -.27    -.18    -.38    -.22
-.03    -.09    -.28    -.36    -.49    -.25    -.17    -.45    -.32    -.33
-.32    -.29    -.32    -.25    -.05    -.01    -.26    -.48    -.37    -.20
-.15    -.08    -.14    -.13    -.12    -.10     .13    -.01     .06    -.17
-.01     .09     .05    -.16     .05    -.02     .04     .17     .19     .05
 .15     .13     .09     .04     .11    -.03     .03     .15     .04    -.02
-.13     .02     .07     .20    -.03    -.07    -.19     .09     .11     .06
 .01     .08     .02     .02    -.27    -.18    -.09    -.02    -.13     .02
 .03    -.12    -.08     .17    -.09    -.04    -.24    -.16    -.09     .12
 .27     .42     .02     .30     .09     .05
;
proc print;
proc gplot;
plot dif*year;
symbol v=star i=join c=black;
proc arima data=a;
identify var=dif nlag=12;
estimate p=1 q=1;
run;
````

</details>

#### example2_1 · SAS · 00fbc0b6

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6109a0cb018578784a2f1304713b299e0a52c81ce285e0bbcd30ebc3ecb431f6`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/example2_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example2_2;
input  freq@@;
year=intnx('year','1jan1970'd,_n_-1);
format year year4.;
cards;
97 154 101 149 221 157 128 215 129 239 155 238 276
204 136 296 176 307 154 227 200 291 233 356 221 309
321 156 234 432 278 356 254 349 322 254 327 432 401
;
proc gplot;
plot freq*year;
symbol v=square c=red i=join;
proc arima data= example2_2;
identify var=freq nlag=22;
run;
````

</details>

#### example2_2 · SAS · 50bfb197

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`52be3f09feb2b5abfcaf3dfeba9a5d132dd32433f3d4090eab24798a7f426c0e`
- 语言：SAS
- 符号：`PROC ARIMA`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/example2_2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example2_2;
input  freq@@;
year=intnx('year','1jan1970'd,_n_-1);
format year year4.;
cards;
97 154 137.7 149 164 157 188 204 179 210 202 218 209
204 211 206 214 217 210 217 219 211 233 316 221 239
215 228 219 239 224 234 227 298 332 245 357 301 389
;
proc arima data= example2_2;
identify var=freq ;
run;
````

</details>

#### 例2.1 · SAS · 8d5286b4

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a92aefeae37123b98d9e30e744f0794416e3b27650ef4844150e95f4d739aec4`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.1.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=10cm hsize=10cm;
data a;
input  sha@@;
year=intnx('year','1jan1964'd,_n_-1);
format year year4.;
dif=dif(sha);
cards;
97 130 156.5 135.2 137.7 180.5 205.2 190 188.6 196.7
180.3 210.8 196 223 238.2 263.5 292.6 317 335.4 327
321.9 353.5 397.8 436.8 465.7 476.7 462.6 460.8
501.8 501.5 489.5 542.3 512.2 559.8 542 567
;
run;
proc gplot;
plot sha*year=1 dif*year=2;
symbol1 v=circle i=join c=black;
symbol2 v=star i=join c=red;
proc arima data=a;
identify var=sha nlag=22;
run;
````

</details>

#### 例2.2 · SAS · 690eaff6

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`e7ee5e7e691eb67d7a89e1858d89e392823e3f78bcaba00a4a8a1ed2baf944ed`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input  milk@@;
time=intnx('month','1jan1962'd,_n_-1);
format time date.;
cards;
589   561   640   656   727   697   640   599
568   577   553   582   600   566   653   673
742   716   660   617   583   587   565   598
628   618   688   705   770   736   678   639
604   611   594   634   658   622   709   722
782   756   702   653   615   621   602   635
677   635   736   755   811   798   735   697
661   667   645   688   713   667   762   784
837   817   767   722   681   687   660   698
717   696   775   796   858   826   783   740
701   706   677   711   734   690   785   805
871   845   801   764   725   723   690   734
750   707   807   824   886   859   819   783
740   747   711   751   804   756   860   878
942   913   869   834   790   800   763   800
826   799   890   900   961   935   894   855
809   810   766   805   821   773   883   898
957   924   881   837   784   791   760   802
828   778   889   902   969   947   908   867
815   812   773   813   834   782   892   903
966   937   896   858   817   827   797   843
;
run;
proc gplot;
plot milk*time;
symbol v=square i=join c=red;
proc arima data=a;
identify var=milk nlag=22;
run;
````

</details>

#### 例2.3 · SAS · b6770e1a

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`53ba4700eddccb1eb80598060a38e54725e424b5ba8bb2bff51d7c153e0abb4e`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.3.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input  time hign;
cards;
1949	38.8
1950	35.6
1951	38.3
1952	39.6
1953	37.0
1954	33.4
1955	39.6
1956	34.6
1957	36.2
1958	37.6
1959	36.8
1960	38.1
1961	40.6
1962	37.1
1963	39.0
1964	37.5
1965	38.5
1966	37.5
1967	35.8
1968	40.1
1969	35.9
1970	35.3
1971	35.2
1972	39.5
1973	37.5
1974	35.8
1975	38.4
1976	35.0
1977	34.1
1978	37.5
1979	35.9
1980	35.1
1981	38.1
1982	37.3
1983	37.2
1984	36.1
1985	35.1
1986	38.5
1987	36.1
1988	38.1
1989	35.8
1990	37.5
1991	35.7
1992	37.5
1993	35.8
1994	37.2
1995	35.0
1996	36.0
1997	38.2
1998	37.2
;
run;
proc gplot;
plot hign*time;
symbol v=square i=join c=red;
proc arima data=a;
identify var=hign nlag=22;
run;
````

</details>

#### 例2.4 · SAS · b21a0312

- 归属算法：ARIMA时间序列
- 用途：核心算法与辅助函数
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“核心算法与辅助函数”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`c41b4382e2cda15d3a3ba6e66d5c9ec505da39d95707e24d58a68cf3c7506f4d`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.4.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
do time=-50 to 1000 by 1;
noise=rannor(12345);
if time>0 then output;
end;
proc gplot;
plot noise*time;
symbol v=none i=join c=red;
proc arima data=a;
identify var=noise;
run;
````

</details>

#### 例2.5 · SAS · 2f5f258b

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8f768fbb252a39438177684bf56238bad0199d30815ba8c3c4e97afc6a9c42fa`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第二章/例2.5.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input year prop;
cards;
1950	83.5
1951	63.1
1952	71
1953	76.3
1954	70.5
1955	80.5
1956	73.6
1957	75.2
1958	69.1
1959	71.4
1960	73.6
1961	78.8
1962	84.4
1963	84.1
1964	83.3
1965	83.1
1966	81.6
1967	81.4
1968	84
1969	82.9
1970	83.5
1971	83.2
1972	82.2
1973	83.2
1974	83.5
1975	83.8
1976	84.5
1977	84.8
1978	83.9
1979	83.9
1980	81
1981	82.2
1982	82.7
1983	82.3
1984	80.9
1985	80.3
1986	81.3
1987	81.6
1988	83.4
1989	88.2
1990	89.6
1991	90.1
1992	88.2
1993	87
1994	87
1995	88.3
1996	87.8
1997	84.7
1998	80.2
;
proc gplot;
plot prop*year=1;
symbol1 v=diamond i=join c=red;
proc arima data=a;
identify var=prop;
estimate p=1 method=ml;
forecast id=year lead=5 out=out;
proc gplot data=out;
plot prop*year=2 forecast*year=3 l95*year=4 u95*year=4/overlay;
symbol2 v=star i=none c=black ;
symbol3 v=none i=join c=red w=2;
symbol4 v=none i=join c=green l=2 ;
run;
````

</details>

#### example5_1 · SAS · e9bb9d94

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`abe10bc1450201363fb21ed4e737ac642cff63514e6928703621afa807e9ea99`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/example5_1.sas`

<details>
<summary>展开原始代码</summary>

````sas
data example5_1;
input x@@;
difx=dif(x);
t=_n_;
cards;
1.05 	-0.84 	-1.42 	0.20 	2.81 	6.72 	5.40 	4.38 
5.52 	4.46 	2.89 	-0.43 	-4.86 	-8.54 	-11.54 	-16.22 
-19.41 	-21.61 	-22.51 	-23.51 	-24.49 	-25.54 	-24.06 	-23.44 
-23.41 	-24.17 	-21.58 	-19.00 	-14.14 	-12.69 	-9.48 	-10.29 
-9.88 	-8.33 	-4.67 	-2.97 	-2.91 	-1.86 	-1.91 	-0.80 
;
proc gplot;
plot x*t difx*t;
symbol v=star c=black i=join;
proc arima;
identify var=x(1);
estimate p=1;
forecast lead=5 id=t out=out;
proc gplot data=out;
plot x*t=1 forecast*t=2 l95*t=3 u95*t=3/overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
symbol3 c=green I=join v=none;
run;
````

</details>

#### 例5.10 · SAS · 06859043

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`45fb5ceb4d84d71c9c803fb6001a1290c123763bccb613fd5da9d8f3ed12d30a`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.10.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input x@@;
dif1_12=dif12(dif(x));
time=intnx('month','1jan1948'd,_n_-1);
format time year4.;
cards;
446	650	592	561	491	592	604	635	580
510	553	554	628	708	629	724	820	865
1007	1025	955	889	965	878	1103	1092	978
823	827	928	838	720	756	658	838	684
779	754	794	681	658	644	622	588	720
670	746	616	646	678	552	560	578	514
541	576	522	530	564	442	520	484	538
454	404	424	432	458	556	506	633	708
1013	1031	1101	1061	1048	1005	987	1006	1075
854	1008	777	982	894	795	799	781	776
761	839	842	811	843	753	848	756	848
828	857	838	986	847	801	739	865	767
941	846	768	709	798	831	833	798	806
771	951	799	1156	1332	1276	1373	1325	1326
1314	1343	1225	1133	1075	1023	1266	1237	1180
1046	1010	1010	1046	985	971	1037	1026	947
1097	1018	1054	978	955	1067	1132	1092	1019
1110	1262	1174	1391	1533	1479	1411	1370	1486
1451	1309	1316	1319	1233	1113	1363	1245	1205
1084	1048	1131	1138	1271	1244	1139	1205	1030
1300	1319	1198	1147	1140	1216	1200	1271	1254
1203	1272	1073	1375	1400	1322	1214	1096	1198
1132	1193	1163	1120	1164	966	1154	1306	1123
1033	940	1151	1013	1105	1011	963	1040	838
1012	963	888	840	880	939	868	1001	956
966	896	843	1180	1103	1044	972	897	1103
1056	1055	1287	1231	1076	929	1105	1127	988
903	845	1020	994	1036	1050	977	956	818
1031	1061	964	967	867	1058	987	1119	1202
1097	994	840	1086	1238	1264	1171	1206	1303
1393	1463	1601	1495	1561	1404	1705	1739	1667
1599	1516	1625	1629	1809	1831	1665	1659	1457
1707	1607	1616	1522	1585	1657	1717	1789	1814
1698	1481	1330	1646	1596	1496	1386	1302	1524
1547	1632	1668	1421	1475	1396	1706	1715	1586
1477	1500	1648	1745	1856	2067	1856	2104	2061
2809	2783	2748	2642	2628	2714	2699	2776	2795
2673	2558	2394	2784	2751	2521	2372	2202	2469
2686	2815	2831	2661	2590	2383	2670	2771	2628
2381	2224	2556	2512	2690	2726	2493	2544	2232
2494	2315	2217	2100	2116	2319	2491	2432	2470
2191	2241	2117	2370	2392	2255	2077	2047	2255
2233	2539	2394	2341	2231	2171	2487	2449	2300
2387	2474	2667	2791	2904	2737	2849	2723	2613
2950	2825	2717	2593	2703	2836	2938	2975	3064
3092	3063	2991						

;
proc gplot;
plot x*time dif1_12*time;
symbol c=black i=join v=none;
proc arima;
identify var=x(1,12);
estimate p=1 q=(1)(12) noint;
forecast lead=0 id=time out=out;
proc gplot data=out;
plot x*time=1 forecast*time=2 /overlay;
symbol1 c=black i=none v=dot h=0.2;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例5.11 · SAS · 983295c0

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`0a7e3a541d9a303c721f8b21cbfb1b1a92c8efde6608b10b696a3aa200a95627`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.11.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input returns@@;
dif=dif(returns);
r2=dif**2;
y=log(returns);
dify=dif(y);
time=intnx('month','1apr1963'd,_n_-1);
format time year4.;
cards;
0.00238	0.00238	0.00236	0.0025	0.00254	0.0026	0.00285	0.00281
0.00241	0.00288	0.00287	0.00292	0.00294	0.00273	0.00271	0.00282
0.00267	0.00273	0.00293	0.00285	0.00296	0.00281	0.00326	0.00321
0.00315	0.00319	0.00313	0.00313	0.00319	0.00313	0.0033	0.00319
0.00315	0.00355	0.0037	0.00371	0.00364	0.00381	0.00372	0.00368
0.00374	0.00389	0.00415	0.00389	0.00343	0.00377	0.00368	0.00364
0.00338	0.00283	0.00271	0.003	0.00309	0.00317	0.00343	0.00347
0.00355	0.0036	0.00398	0.00385	0.00389	0.00444	0.00453	0.00444
0.00432	0.00406	0.00432	0.00461	0.00398	0.005	0.00487	0.0047
0.00432	0.00508	0.00478	0.00508	0.00593	0.0055	0.00593	0.00542
0.0054	0.0054	0.00631	0.00534	0.00546	0.00542	0.00546	0.00495
0.005	0.00508	0.00483	0.00444	0.00377	0.00355	0.00338	0.00264
0.00283	0.00305	0.00338	0.00406				
;
proc gplot;
plot returns*time dif*time r2*time y*time dify*time;
symbol c=black i=join v=none;
proc arima;
identify var=returns ;
identify var=y(1);
estimate p=0 q=0 noint;
forecast lead=0 id=time  out=out;
data out;
merge a out;
by time;
estimate=exp(y);
proc gplot;
plot returns*time=1 estimate*time=2 /overlay;
symbol1 c=black i=none v=star h=0.5;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例5.6 · SAS · 0cb94755

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC AUTOREG`、`PROC GPLOT`、`PROC PRINT`；先核对参数顺序和返回值。
- **主要输出**：控制台/过程输出
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`6397f4ac81313250518c147676c252b4df0e65bd5d60e43aea3a3fd0c1414021`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC AUTOREG`, `PROC GPLOT`, `PROC PRINT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.6.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data na_in;
t=_n_;
time=intnx('year','1jan1952'd,_n_-1);
format time year4.;
input agric     indus   cons    trans   commer;
dif=dif(agric) ;
keep time agric dif;
cards;
100     100     100     100     100
101.6   133.6   138.1   12      133
103.3   159.1   133.3   136     136.4
111.5   169.1   152.4   140     137.5
116.5   219.1   261.9   164     146.6
120.1   244.5   242.9   176     146.6
120.3   383.5   367     270.8   155.9
100.6   501.5   388.6   356.5   170.3
83.6    541.4   394     383.6   164.1
84.7    315.9   129.5   221.1   130.1
88.7    267.4   161.9   171.5   117.7
98.9    300.7   205.1   176     120.8
111.9   374.9   259     198.6   123.9
122.9   477.7   286     261.7   128
131.9   598.5   313     297.8   155.9
134.2   504.3   296.8   239.2   164.1
131.6   458.6   237.5   225.6   151.8
132.2   622.3   323.8   284.3   179.6
139.8   863     421     343     199.2
142     979     468.3   370.8   201.2
140.5   1043.5  452.5   389.3   208
153.1   1134.3  457.8   412.5   224.5
159.2   1128.9  484.1   394     220.6
162.3   1297.3  542     444.9   220.6
159.1   1249.2  568.3   426.4   214.8
155.1   1434    578.8   491.3   242
161.2   1679.1  573.5   546.9   296.4
171.5   1814.7  584.1   560.8   316.8
168.4   2012.7  757.7   584     318.8
180.4   2046.8  770     607.2   379.4
201.6   2170.1  806.9   681.3   397.5
218.7   2383.7  954.3   755.5   449.1
247     2738.8  1056.7  852.8   499.5
253.7   3275.2  1310.6  1024.3  593.7
261.4   3590.6  1540    1140.2  636.3
273.2   4058.8  1744.8  1269.9  715
279.4   4765    1884    1413.6  760.8
;
proc print;
proc gplot;
plot agric*time=1 dif*time=1;
symbol1 c=red i=join v=square;
proc arima;
identify var=agric(1) stationarity=(adf) nlag=18;
estimate q=1;
forecast lead=10 id=time interval=year out=out;
proc print data=out;
proc gplot;
where time>='1jan1955'd;
plot agric*time=2 forecast*time=3 (l95 u95)*time=4/overlay;
symbol2 c=black i=none v=star;
symbol3 c=red i=join v=none;
symbol4 c=green i=join v=none l=3 w=1;
proc autoreg data=na_in;
model agric=t/nlag=2 method=ml dwprob;
output out=p p=a1 pm=a2 lcl=lcl ucl=ucl;
proc gplot data=p;
where time>='1jan1955'd;
plot agric*time=2 a1*time=3 lcl*time=4 ucl*time=4/overlay;
proc autoreg data=na_in;
model agric=dif/LAGDEP=DIF nlag=1 method=ml noint;
output out=p p=b1 pm=b2 lcl=lcl ucl=ucl;
proc gplot data=p;
where time>='1jan1955'd;
plot agric*time=2 b1*time=3 lcl*time=4 ucl*time=4/overlay;
run;
````

</details>

#### 例5.8 · SAS · 7f49d74b

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`8cf212db6ccda7b3f65fe8873aeab79d7145a6222bddd62c3ae507b270f80fac`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.8.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data a;
input year x@@;
dif=dif(x);
cards;
1917	183.1
1918	183.9
1919	163.1
1920	179.5
1921	181.4
1922	173.4
1923	167.6
1924	177.4
1925	171.7
1926	170.1
1927	163.7
1928	151.9
1929	145.4
1930	145
1931	138.9
1932	131.5
1933	125.7
1934	129.5
1935	129.6
1936	129.5
1937	132.2
1938	134.1
1939	132.1
1940	137.4
1941	148.1
1942	174.1
1943	174.7
1944	156.7
1945	143.3
1946	189.7
1947	212
1948	200.4
1949	201.8
1950	200.7
1951	215.6
1952	222.5
1953	231.5
1954	237.9
1955	244
1956	259.4
1957	268.8
1958	264.3
1959	264.5
1960	268.1
1961	264
1962	252.8
1963	240
1964	229.1
1965	204.8
1966	193.3
1967	179
1968	178.1
1969	181.1
1970	165.6
1971	159.8
1972	136.1
1973	126.3
1974	123.3
1975	118.5
;
proc gplot;
plot x*year dif*year;
symbol c=black i=join v=square;
proc arima;
identify var=x(1);
estimate p=(1 4) noint;
forecast lead=5 id=year out=out;
proc gplot data=out;
plot x*year=1 forecast*year=2 l95*year=3 u95*year=3/overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
symbol3 c=green i=join v=none;
run;
````

</details>

#### 例5.9 · SAS · 94c5884f

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`a2ca740bf2707bc669131dc724b574359e21b16ca2cfa6a5bf9561b5af5d8748`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第五章/例5.9.sas`

<details>
<summary>展开原始代码</summary>

````sas
goptions vsize=7cm hsize=10cm;
data a;
input x@@;
dif1_4=dif4(dif(x));
time=intnx('quarter','1jan1962'd,_n_-1);
format time year4.;
cards;
1.1	0.5	0.4	0.7	1.6	0.6	0.5	0.7
1.3	0.6	0.5	0.7	1.2	0.5	0.4	0.6
0.9	0.5	0.5	1.1	2.9	2.1	1.7	2
2.7	1.3	0.9	1	1.6	0.6	0.5	0.7
1.1	0.5	0.5	0.6	1.2	0.7	0.7	1
1.5	1	0.9	1.1	1.5	1	1	1.6
2.6	2.1	2.3	3.6	5	4.5	4.5	4.9
5.7	4.3	4	4.4	5.2	4.3	4.2	4.5
5.2	4.1	3.9	4.1	4.8	3.5	3.4	3.5
4.2	3.4	3.6	4.3	5.5	4.8	5.4	6.5
8	7	7.4	8.5	10.1	8.9	8.8	9
10	8.7	8.8	8.9	10.4	8.9	8.9	9
10.2	8.6	8.4	8.4	9.9	8.5	8.6	8.7
9.8	8.6	8.4	8.2	8.8	7.6	7.5	7.6
8.1	7.1	6.9	6.6	6.8	6	6.2	6.2
;
proc gplot;
plot x*time dif1_4*time;
symbol c=black i=join v=star;
proc arima;
identify var=x(1,4);
estimate p=2 noint;
forecast lead=0 id=time out=out;
proc gplot data=out;
plot x*time=1 forecast*time=2 /overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例6.1 · SAS · 959a8745

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`4dd48668e66f85fb7a8da39c911a5c592e4bd8bee8bd3a00cb75fee7911235c5`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第六章/例6.1.sas`

<details>
<summary>展开原始代码</summary>

````sas
 data b_j_seriesj;
   input x y @@;
   label x = 'Input Gas Rate'
         y = 'Output CO2';
		 t=_n_;
cards;
-0.109  53.8  0.000  53.6  0.178  53.5  0.339  53.5
 0.373  53.4  0.441  53.1  0.461  52.7  0.348  52.4
 0.127  52.2 -0.180  52.0 -0.588  52.0 -1.055  52.4
-1.421  53.0 -1.520  54.0 -1.302  54.9 -0.814  56.0
-0.475  56.8 -0.193  56.8  0.088  56.4  0.435  55.7
 0.771  55.0  0.866  54.3  0.875  53.2  0.891  52.3
 0.987  51.6  1.263  51.2  1.775  50.8  1.976  50.5
 1.934  50.0  1.866  49.2  1.832  48.4  1.767  47.9
 1.608  47.6  1.265  47.5  0.790  47.5  0.360  47.6
 0.115  48.1  0.088  49.0  0.331  50.0  0.645  51.1
 0.960  51.8  1.409  51.9  2.670  51.7  2.834  51.2
 2.812  50.0  2.483  48.3  1.929  47.0  1.485  45.8
 1.214  45.6  1.239  46.0  1.608  46.9  1.905  47.8
 2.023  48.2  1.815  48.3  0.535  47.9  0.122  47.2
 0.009  47.2  0.164  48.1  0.671  49.4  1.019  50.6
 1.146  51.5  1.155  51.6  1.112  51.2  1.121  50.5
 1.223  50.1  1.257  49.8  1.157  49.6  0.913  49.4
 0.620  49.3  0.255  49.2 -0.280  49.3 -1.080  49.7
-1.551  50.3 -1.799  51.3 -1.825  52.8 -1.456  54.4
-0.944  56.0 -0.570  56.9 -0.431  57.5 -0.577  57.3
-0.960  56.6 -1.616  56.0 -1.875  55.4 -1.891  55.4
-1.746  56.4 -1.474  57.2 -1.201  58.0 -0.927  58.4
-0.524  58.4  0.040  58.1  0.788  57.7  0.943  57.0
 0.930  56.0  1.006  54.7  1.137  53.2  1.198  52.1
 1.054  51.6  0.595  51.0 -0.080  50.5 -0.314  50.4
-0.288  51.0 -0.153  51.8 -0.109  52.4 -0.187  53.0
-0.255  53.4 -0.229  53.6 -0.007  53.7  0.254  53.8
 0.330  53.8  0.102  53.8 -0.423  53.3 -1.139  53.0
-2.275  52.9 -2.594  53.4 -2.716  54.6 -2.510  56.4
-1.790  58.0 -1.346  59.4 -1.081  60.2 -0.910  60.0
-0.876  59.4 -0.885  58.4 -0.800  57.6 -0.544  56.9
-0.416  56.4 -0.271  56.0  0.000  55.7  0.403  55.3
 0.841  55.0  1.285  54.4  1.607  53.7  1.746  52.8
 1.683  51.6  1.485  50.6  0.993  49.4  0.648  48.8
 0.577  48.5  0.577  48.7  0.632  49.2  0.747  49.8
 0.900  50.4  0.993  50.7  0.968  50.9  0.790  50.7
 0.399  50.5 -0.161  50.4 -0.553  50.2 -0.603  50.4
-0.424  51.2 -0.194  52.3 -0.049  53.2  0.060  53.9
 0.161  54.1  0.301  54.0  0.517  53.6  0.566  53.2
 0.560  53.0  0.573  52.8  0.592  52.3  0.671  51.9
 0.933  51.6  1.337  51.6  1.460  51.4  1.353  51.2
 0.772  50.7  0.218  50.0 -0.237  49.4 -0.714  49.3
-1.099  49.7 -1.269  50.6 -1.175  51.8 -0.676  53.0
 0.033  54.0  0.556  55.3  0.643  55.9  0.484  55.9
 0.109  54.6 -0.310  53.5 -0.697  52.4 -1.047  52.1
-1.218  52.3 -1.183  53.0 -0.873  53.8 -0.336  54.6
 0.063  55.4  0.084  55.9  0.000  55.9  0.001  55.2
 0.209  54.4  0.556  53.7  0.782  53.6  0.858  53.6
 0.918  53.2  0.862  52.5  0.416  52.0 -0.336  51.4
-0.959  51.0 -1.813  50.9 -2.378  52.4 -2.499  53.5
-2.473  55.6 -2.330  58.0 -2.053  59.5 -1.739  60.0
-1.261  60.4 -0.569  60.5 -0.137  60.2 -0.024  59.7
-0.050  59.0 -0.135  57.6 -0.276  56.4 -0.534  55.2
-0.871  54.5 -1.243  54.1 -1.439  54.1 -1.422  54.4
-1.175  55.5 -0.813  56.2 -0.634  57.0 -0.582  57.3
-0.625  57.4 -0.713  57.0 -0.848  56.4 -1.039  55.9
-1.346  55.5 -1.628  55.3 -1.619  55.2 -1.149  55.4
-0.488  56.0 -0.160  56.5 -0.007  57.1 -0.092  57.3
-0.620  56.8 -1.086  55.6 -1.525  55.0 -1.858  54.1
-2.029  54.3 -2.024  55.3 -1.961  56.4 -1.952  57.2
-1.794  57.8 -1.302  58.3 -1.030  58.6 -0.918  58.8
-0.798  58.8 -0.867  58.6 -1.047  58.0 -1.123  57.4
-0.876  57.0 -0.395  56.4  0.185  56.3  0.662  56.4
 0.709  56.4  0.605  56.0  0.501  55.2  0.603  54.0
 0.943  53.0  1.223  52.0  1.249  51.6  0.824  51.6
 0.102  51.1  0.025  50.4  0.382  50.0  0.922  50.0
 1.032  52.0  0.866  54.0  0.527  55.1  0.093  54.5
-0.458  52.8 -0.748  51.4 -0.947  50.8 -1.029  51.2
-0.928  52.0 -0.645  52.8 -0.424  53.8 -0.276  54.5
-0.158  54.9 -0.033  54.9  0.102  54.8  0.251  54.4
 0.280  53.7  0.000  53.3 -0.493  52.8 -0.759  52.6
-0.824  52.6 -0.740  53.0 -0.528  54.3 -0.204  56.0
 0.034  57.0  0.204  58.0  0.253  58.6  0.195  58.5
 0.131  58.3  0.017  57.8 -0.182  57.3 -0.262  57.0
;

proc arima data=b_j_seriesj;
identify var=x nlag=10;
estimate p=3;
identify var=y nalg=10;
estimate p=(1 2 4);
forecast lead=10 id=t out=out1;
identify var=y crosscorr=(x) nlag=10;
estimate input=( 3$ (1,2)/(1,2) x ) plot;
estimate p=2 input=( 3$ (1,2)/(1) x );
forecast lead=10 id=t out=out2;
proc gplot data=out1;
plot y*t=1 forecast1*t=2 /overlay;
proc gplot data=out2;
plot y*t=1 forecast2*t=2 /overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
run;
````

</details>

#### 例6.2 · SAS · 69f74e3e

- 归属算法：ARIMA时间序列
- 用途：预测与推断
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：函数/类型实现，可优先封装复用；当前用于ARIMA时间序列中的“预测与推断”。
- **执行主线**：识别并拟合时间序列滞后结构；估计回归系数并生成拟合/预测。
- **调用方式**：优先调用 `PROC ARIMA`、`PROC GPLOT`、`PROC REG`；先核对参数顺序和返回值。
- **主要输出**：工作区变量或求解器结果
- **调用风险**：未发现明显静态风险，但仍需运行测试和结果校验。

- SHA-256：`fbd199d2ec63c58b0bda11e9703bd7d6e4b7deaa378bb9a10a3fa6923f538650`
- 语言：SAS
- 符号：`PROC ARIMA`, `PROC GPLOT`, `PROC REG`
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/6.数学建模模型算法大全/统计分析/时间序列/时间序列课件/时间序列/程序/第六章/例6.2.sas`

<details>
<summary>展开原始代码</summary>

````sas
data a;
input year x y;
lnx=log(x);
lny=log(y);
cards;
1978	133.6	116.1
1979	160.7	134.5
1980	191.3	162.2
1981	223.4	190.8
1982	270.1	220.2
1983	309.8	248.3
1984	355.3	273.8
1985	397.6	317.4
1986	423.8	357
1987	462.6	398.3
1988	544.9	476.7
1989	601.5	535.4
1990	686.3	584.6
1991	708.6	619.8
1992	784	659.8
1993	921.6	769.7
1994	1221	1016.8
1995	1577.7	1310.4
1996	1926.1	1572.1
1997	2090.1	1617.2
1998	2162	1590.3
1999	2210.3	1577.4
2000	2253.4	1670.1
2001	2366.4	1741
2002	2476	1834
;
proc gplot data=a;
plot lnx*year=1 lny*year=2/overlay;
symbol1 c=black i=join v=circle;
symbol2 c=black i=join v=star;
proc arima data=a;
identify var=lnx stationarity=(adf);
identify var=lny stationarity=(adf);
identify var=lnx(1) stationarity=(adf);
identify var=lny(1) stationarity=(adf);
identify var=lnx(1) stationarity=(pp);
identify var=lny(1) stationarity=(pp);
proc reg;
model lny=lnx /noint;
output out=out residual=residual;
proc arima data=out;
identify var=residual stationarity=(adf);
proc arima data=a;
identify var=lny crosscorr=(lnx);
estimate p=1 input=lnx noint;
forecast lead=10 id=year out=result;
data result;
set result;
y=exp(lny);
estimate=exp(forecast);
proc gplot data=result;
plot lny*year=1 forecast*year=2 /overlay;
plot y*year=1 estimate*year=2 /overlay;
symbol1 c=black i=none v=star;
symbol2 c=red i=join v=none;
data b;
set a;
ecm=lny-0.96832*lnx;
lag_ecm=lag(ecm);
dif_lnx=dif(lnx);
dif_lny=dif(lny);
proc reg data=b;
model dif_lny=dif_lnx lag_ecm /noint;
run;
````

</details>

#### Pex18_6 · Python · c754bf31

- 归属算法：ARIMA时间序列
- 用途：结果绘图与展示
- 独立实现变体：1
- 原始来源文件：1
- 复习入口：[[04-Research/02-经典建模模型库/02-预测类模型/预测模型 Hub#ARIMA时间序列 · 复习|ARIMA时间序列 · 复习]]
- 验证状态：`python-ast-pass` + `source-traced`；尚未运行；自动归类不代表算法或结果正确。

##### 代码理解与调用

- **定位**：脚本型示例，适合学习后重构；当前用于ARIMA时间序列中的“结果绘图与展示”。
- **执行主线**：识别并拟合时间序列滞后结构；把计算结果转换为二维、三维或图像表达。
- **调用方式**：不要直接复制整段到项目；先把硬编码参数移到函数入口，再用最小样例调用。
- **主要输出**：控制台/过程输出、图形
- **调用风险**：原实现含外部输入，复用时应改成显式函数参数。

- SHA-256：`2e263117c42c6348c0a0d0765d5029a3327ecd00963d3beb58553ff5765866c4`
- 语言：Python
- 符号：未自动识别
- 原始路径：
  - 源文件：`00-Inbox/Downloaded/数学建模Python相关/数学建模常用算法（Python 程序及数据）/程序及数据/18第18章  时间序列分析(Python 程序及数据)/Pex18_6.py`

<details>
<summary>展开原始代码</summary>

````python
#程序文件Pex18_6.py
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import pylab as plt
from statsmodels.tsa.arima_model import ARIMA

plt.rc('axes',unicode_minus=False)
plt.rc('font',size=16); plt.rc('font',family='SimHei')
df=pd.read_csv('austa.csv')
plt.subplot(121); plt.plot(df.value.diff())
plt.title('一次差分')
ax2=plt.subplot(122)
plot_acf(df.value.diff().dropna(), ax=ax2,title='自相关')

md=ARIMA(df.value, order=(2,1,0))
mdf=md.fit(disp=0)
print(mdf.summary())

residuals = pd.DataFrame(mdf.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="残差", ax=ax[0])
residuals.plot(kind='kde', title='密度', ax=ax[1])
plt.legend(''); plt.ylabel('')          

mdf.plot_predict()  #原始数据与预测值对比图
plt.show()
````

</details>
