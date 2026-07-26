---
type: research-method
status: active
topic: AHP层次分析法
updated: 2026-07-26
tags: [area/数学建模, topic/评价模型, method/AHP]
---

# AHP层次分析法

> [!summary] 30 秒复习
> AHP 把复杂决策拆成“目标—准则—方案”层次，通过两两比较判断矩阵求主观权重。关键不是算特征向量，而是保证层次独立、判断有依据并通过一致性检验。

## 什么时候用

- 指标权重无法由客观数据直接给出，但专家能够比较两个指标的重要程度。
- 指标数较少、层次关系清楚。指标很多时两两比较负担为 $O(n^2)$，判断容易失真。
- 不适合把高度相关指标强行视为独立，也不应把“CR 合格”误当成专家判断正确。

## 核心数学

判断矩阵 $A=(a_{ij})$ 满足 $a_{ij}>0,\ a_{ji}=1/a_{ij}$。最大特征值对应向量归一化为权重：

$$Aw=\lambda_{\max}w,\qquad \sum_i w_i=1.$$

一致性指标 $CI=(\lambda_{\max}-n)/(n-1)$，一致性比率 $CR=CI/RI$；常用经验门槛为 $CR<0.10$。

## 算法步骤

1. 明确目标、准则和方案，避免层次间概念重叠。
2. 用 Saaty 1–9 标度构造正互反矩阵，并记录每个判断的证据。
3. 用最大特征根法求权重，计算 $CI$、$CR$。
4. 若不一致，回到判断来源修订，不要仅为“过检验”机械改数。
5. 合成各层权重，并对关键判断做扰动或情景敏感性分析。

## 代码入口

- [Python：`ahp_weights`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/evaluation_models.py)
- [MATLAB：`evaluation_models("ahp", A)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/evaluation_models.m)

## 论文必须报告

- 层次结构、专家/问卷来源、判断尺度、矩阵与 $CR$。
- 权重变化是否改变最终排序；多人判断矩阵采用何种聚合方式。

## 常见错误

- 判断矩阵不互反；把方案原始评分误当成 AHP 判断矩阵。
- 只给权重不报告一致性；指标重复导致某一信息被重复加权。
- 对排序结果作绝对化解释，而没有不确定性或敏感性分析。

## 来源

- Saaty, T. L. (1980), *The Analytic Hierarchy Process*, McGraw-Hill。
- [pyDecision：含 AHP/TOPSIS/Entropy/GRA 的开源 MCDA 实现](https://github.com/Valdecy/pyDecision)

## 关联

[[评价模型 Hub]] · [[04-Research/02-经典建模模型库/01-评价类模型/熵权法/Readme|熵权法]] · [[04-Research/02-经典建模模型库/01-评价类模型/TOPSIS优劣解距离法/Readme|TOPSIS优劣解距离法]] · [[模型检验 Hub]]
