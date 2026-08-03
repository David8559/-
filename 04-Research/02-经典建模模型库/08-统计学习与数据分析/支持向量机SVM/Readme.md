---
type: model-card
status: reviewed-theory
created: 2026-08-03
updated: 2026-08-03
tags: [area/数学建模, topic/统计学习, model/SVM]
topic_hubs: [统计学习 Hub, 预测模型 Hub]
---

# 支持向量机 SVM

## 核心思想

分类 SVM 在特征空间中寻找最大间隔超平面；软间隔参数 $C$ 权衡间隔与错分，核函数处理非线性。回归 SVR 用 $\varepsilon$ 不敏感损失控制误差带。适合中小样本、高维特征，不适合未经缩放的大规模数据直接套用复杂核。

## 标准流程

先分训练/验证 → 在训练折内拟合标准化 → 以线性模型为基线 → 交叉验证选择核、$C$、$\gamma$ 或 $\varepsilon$ → 在独立验证集评价 → 检查支持向量比例和误分类样本。类别不平衡时使用分层切分、类别权重，并报告 PR/F1 或召回率而非只报准确率。

## 必做检验与边界

- 预处理必须置于交叉验证流水线，防止泄漏。
- 比较线性核和 RBF；若 RBF 增益很小，优先线性解释。
- 报告超参数搜索范围、评价指标、混淆矩阵或回归残差。
- SVM 分数不是天然概率；如需概率需单独校准并验证。

Python 优先 `sklearn.pipeline.Pipeline` + `SVC/SVR`。本库 Hub 中已有原始实现索引，但未全部运行验证。

## 来源与链接

- Cortes C, Vapnik V. Support-vector networks. *Machine Learning*, 1995, 20:273–297.
- [[统计学习 Hub]]；[[预测模型 Hub]]；[[模型检验实战清单]]。
