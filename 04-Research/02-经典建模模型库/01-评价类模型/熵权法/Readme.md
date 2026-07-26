---
type: research-method
status: active
topic: 熵权法
updated: 2026-07-26
tags: [area/数学建模, topic/评价模型, method/熵权法]
---

# 熵权法

> [!summary] 30 秒复习
> 熵权法按指标在样本中的离散程度赋权：差异越大，信息效用越高，权重越大。它是数据驱动权重，不等于业务重要性。

## 适用边界

- 多方案评价且样本足以反映指标差异；希望降低纯主观赋权影响。
- 若重要指标本身变化很小，熵权可能错误地给低权；异常值也可能放大权重。
- 所有指标需正向化并转成非负数，零值要按公式约定处理。

## 核心数学

$$p_{ij}=\frac{x_{ij}}{\sum_i x_{ij}},\qquad
e_j=-\frac{1}{\ln m}\sum_i p_{ij}\ln p_{ij},$$

$$d_j=1-e_j,\qquad w_j=\frac{d_j}{\sum_j d_j}.$$

约定 $0\ln0=0$。若所有 $d_j$ 接近 0，数据无法区分指标，应回到指标体系而不是强行赋权。

## 算法步骤

1. 判断指标类型并正向化；处理缺失、异常和量纲。
2. 计算比例矩阵 $P$、熵值 $e_j$、差异系数 $d_j$ 和权重。
3. 与等权、AHP/专家权重并列比较。
4. 对异常值截尾、不同标准化和样本子集做敏感性分析。

## 代码入口

- [Python：`entropy_weights`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/evaluation_models.py)
- [MATLAB：`evaluation_models("entropy", X)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/evaluation_models.m)

## 常见错误

- 将负数直接代入比例；遇到 0 直接计算 `log(0)`。
- 把“离散程度大”解释成“现实意义重要”。
- 样本极少或异常点主导时仍接受自动权重。

## 来源

- Shannon, C. E. (1948), “A Mathematical Theory of Communication”。
- [pyDecision：Entropy 与多种 MCDA 方法](https://github.com/Valdecy/pyDecision)

## 关联

[[评价模型 Hub]] · [[04-Research/02-经典建模模型库/01-评价类模型/AHP层次分析法/Readme|AHP层次分析法]] · [[04-Research/02-经典建模模型库/01-评价类模型/TOPSIS优劣解距离法/Readme|TOPSIS优劣解距离法]] · [[数据处理 Hub]]
