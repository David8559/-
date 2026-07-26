---
type: research-method
status: active
topic: 模糊综合评价
updated: 2026-07-26
tags: [area/数学建模, topic/评价模型, method/模糊综合评价]
---

# 模糊综合评价

> [!summary] 30 秒复习
> 把“好、较好、一般”等模糊判断表示成隶属度，用权重向量与模糊关系矩阵合成。难点在隶属函数和权重的依据，不在矩阵乘法。

## 模型结构

因素集 $U=\{u_1,\ldots,u_m\}$，评价集 $V=\{v_1,\ldots,v_n\}$，权重 $W$，隶属度矩阵 $R$：

$$B=W\circ R.$$

常用加权平均算子时 $B=WR$。若需转成总分，可用等级分值 $s$ 得 $F=Bs^\mathsf T$，但必须说明等级间距的含义。

## 算法步骤

1. 定义互斥且覆盖充分的评价等级。
2. 基于标准、问卷频率或有依据的隶属函数构造 $R$。
3. 用 AHP、熵权或组合权重获得 $W$，并保证和为 1。
4. 选择合成算子，计算 $B$；用最大隶属原则或加权分值解释。
5. 改变隶属函数、权重和等级边界，检查结论是否稳定。

## 代码入口

- [Python：`fuzzy_comprehensive_evaluation`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/evaluation_models.py)
- [MATLAB：`evaluation_models("fuzzy", w, R)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/evaluation_models.m)

## 常见错误

- 每行隶属度不为 1；把概率和隶属度混为一谈。
- 隶属函数阈值完全主观却写成“客观结果”。
- 多级评价时层次权重重复使用，造成重复计分。

## 来源

- Zadeh, L. A. (1965), “Fuzzy Sets”, *Information and Control*, 8(3), 338–353。
- [scikit-fuzzy 官方 GitHub](https://github.com/scikit-fuzzy/scikit-fuzzy)

## 关联

[[评价模型 Hub]] · [[04-Research/02-经典建模模型库/01-评价类模型/AHP层次分析法/Readme|AHP层次分析法]] · [[04-Research/02-经典建模模型库/01-评价类模型/熵权法/Readme|熵权法]]
