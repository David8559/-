---
type: research-method
status: active
topic: TOPSIS优劣解距离法
updated: 2026-07-26
tags: [area/数学建模, topic/评价模型, method/TOPSIS]
---

# TOPSIS优劣解距离法

> [!summary] 30 秒复习
> TOPSIS 同时比较方案到正理想解和负理想解的距离。贴近度越大越优；结果依赖指标正负向、归一化、权重和方案集合。

## 什么时候用

- 多方案、多指标排序，指标可转为单调的效益型或成本型。
- 适合与 [[04-Research/02-经典建模模型库/01-评价类模型/AHP层次分析法/Readme|AHP层次分析法]]、[[04-Research/02-经典建模模型库/01-评价类模型/熵权法/Readme|熵权法]] 组合赋权。
- 当指标强相关、极端值明显或距离度量缺乏业务意义时应谨慎。

## 核心数学

向量归一化并加权得到 $z_{ij}$，取正/负理想点 $z^+,z^-$：

$$D_i^+=\sqrt{\sum_j(z_{ij}-z_j^+)^2},\quad
D_i^-=\sqrt{\sum_j(z_{ij}-z_j^-)^2},\quad
C_i=\frac{D_i^-}{D_i^++D_i^-}.$$

$C_i\in[0,1]$，越大表示越接近正理想且远离负理想。

## 算法步骤

1. 明确每列的效益/成本/区间/中间型属性，先统一方向。
2. 选择归一化方法并说明理由；常用向量归一化。
3. 加权后确定正、负理想解，计算两类距离和贴近度。
4. 给出排序，并做权重、归一化方式和异常值敏感性分析。
5. 对新增/删除方案引起的逆序现象进行检查。

## 代码入口

- [Python：`topsis`](../../../03-建模算法源码库/01-Python实现代码/模型完整代码/evaluation_models.py)
- [MATLAB：`evaluation_models("topsis", X, w, benefitMask)`](../../../03-建模算法源码库/02-MATLAB实现代码/拟合与预测脚本/evaluation_models.m)

## 检验与解释

- 确认 $0\le C_i\le1$、方向转换正确、权重和为 1。
- 用等权、AHP 权重、熵权三种情景比较排序稳定性；报告临界翻转点。
- TOPSIS 给的是相对排序，不自动给出“合格/不合格”的绝对阈值。

## 常见错误

- 忘记成本型指标转向；先加权后错误归一化。
- 直接拼接量纲差异很大的指标；忽略高度相关列重复计分。
- 仅报告名次，不报告贴近度、权重与稳健性。

## 来源

- Hwang, C. L. & Yoon, K. (1981), *Multiple Attribute Decision Making: Methods and Applications*。
- [pyDecision 开源实现](https://github.com/Valdecy/pyDecision)

## 关联

[[评价模型 Hub]] · [[04-Research/02-经典建模模型库/01-评价类模型/AHP层次分析法/Readme|AHP层次分析法]] · [[04-Research/02-经典建模模型库/01-评价类模型/熵权法/Readme|熵权法]] · [[04-Research/02-经典建模模型库/01-评价类模型/灰色关联分析/Readme|灰色关联分析]]
