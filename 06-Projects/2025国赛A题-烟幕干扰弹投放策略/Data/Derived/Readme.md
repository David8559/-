---
type: project-derived-data
status: active
---

# 派生数据

本目录只保存由 `Data/Raw/` 和项目代码生成的派生数据、结果模板副本与中间计算结果。每个文件必须能追溯到生成脚本、参数和源文件；禁止把原始附件直接改写后放回 `Raw/`。

## 当前文件

- `result1.xlsx`：问题 3 三枚干扰弹结果表，由 `Code/outputs/problem3_result.json` 写入 `Data/Raw/result1.xlsx` 的派生副本；原始模板 SHA-256 仍为 `AF04B16E6A4719628971BCF5A03D230C9DA6738E67EEBAC9276D254FDD4DF1A7`。
- `result2.xlsx`：问题 4 三架无人机各一枚干扰弹结果表，由 `Code/outputs/problem4_result.json` 写入 `Data/Raw/result2.xlsx` 的派生副本；原始模板 SHA-256 仍为 `C681D5E378538F71C77FCA199A3CA8303A04DBCFC7BD95F870AE22F01AB69F91`。
- `result3.xlsx`：问题 5 五架无人机对三枚导弹的 9 枚有效投放结果表，由 `Code/outputs/problem5_result.json` 写入 `Data/Raw/result3.xlsx` 的派生副本；未使用的 6 个预留投弹行保持空白；原始模板 SHA-256 仍为 `B648C82D63E459BA6E6B3711AE79875E373521CD543B45571C4D8FF1AD5EC54A`。
