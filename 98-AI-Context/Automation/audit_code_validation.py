#!/usr/bin/env python3
"""Build an evidence-based validation inventory for local modeling code."""

from __future__ import annotations

import ast
import csv
import datetime as dt
import importlib.util
import json
import os
import py_compile
import re
import subprocess
import sys
from pathlib import Path

import build_code_knowledge_graph as core

LIBRARY = core.VAULT / "04-Research" / "03-建模算法源码库"
PUBLIC_PYTHON = LIBRARY / "00-公共复用模块" / "Python"
PUBLIC_TESTS = PUBLIC_PYTHON / "tests"
CURATED_TESTS = LIBRARY / "03-验证测试"
STATUS_CSV = LIBRARY / "代码验证状态.csv"
REPORT = LIBRARY / "代码验证报告.md"
MATLAB_RESULT = CURATED_TESTS / "matlab_validation_result.json"

CURATED_FILES = [
    LIBRARY / "01-Python实现代码" / "模型完整代码" / "evaluation_models.py",
    LIBRARY / "01-Python实现代码" / "模型完整代码" / "forecast_models.py",
    LIBRARY / "01-Python实现代码" / "模型完整代码" / "network_dynamics_models.py",
    LIBRARY / "01-Python实现代码" / "优化求解代码" / "optimization_models.py",
    LIBRARY / "01-Python实现代码" / "优化求解代码" / "metaheuristics.py",
]

OPTIONAL_BRANCHES = {"statsmodels": 1, "networkx": 3, "scipy": 4}
DEPENDENCY_FREE_BRANCHES = 17


def run_suite(test_root: Path, *, python_path: Path | None = None) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    if python_path is not None:
        environment["PYTHONPATH"] = str(python_path)
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(test_root),
            "-p",
            "test_*.py",
            "-v",
        ],
        cwd=core.VAULT,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    rows = core.load_catalog(core.CODE_CATALOG)
    variants = core.make_variants(rows)
    inventory: list[dict[str, object]] = []
    python_checked = python_passed = 0
    failures: list[str] = []

    for item in sorted(variants, key=lambda value: value.canonical_path):
        static_status = "source-traced"
        detail = "源路径与 SHA-256 已核对；未执行"
        if item.language == "Python":
            python_checked += 1
            try:
                ast.parse(item.code)
            except SyntaxError as error:
                static_status = "python-ast-fail"
                detail = f"Python 语法解析失败：{error.msg}"
                failures.append(f"{item.canonical_path}: {error.msg}")
            else:
                python_passed += 1
                static_status = "python-ast-pass"
                detail = "源路径与 SHA-256 已核对；Python AST 解析通过；未执行"
        inventory.append(
            {
                "sha256": item.digest,
                "canonical_path": item.canonical_path,
                "language": item.language,
                "source_paths": len(item.paths),
                "static_status": static_status,
                "runtime_status": "not-run",
                "detail": detail,
            }
        )

    with STATUS_CSV.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(inventory[0]))
        writer.writeheader()
        writer.writerows(inventory)

    curated_compile_failures: list[str] = []
    for path in CURATED_FILES:
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as error:
            curated_compile_failures.append(f"{path.name}: {error.msg}")

    public_result = run_suite(PUBLIC_TESTS, python_path=PUBLIC_PYTHON)
    curated_result = run_suite(CURATED_TESTS)
    available_optional = {
        package: importlib.util.find_spec(package) is not None
        for package in OPTIONAL_BRANCHES
    }
    executed_branches = DEPENDENCY_FREE_BRANCHES + sum(
        count for package, count in OPTIONAL_BRANCHES.items() if available_optional[package]
    )
    blocked_branches = sum(
        count for package, count in OPTIONAL_BRANCHES.items() if not available_optional[package]
    )
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    optional_text = "；".join(
        f"{name}={'可用' if available else '缺失'}（{OPTIONAL_BRANCHES[name]} 分支）"
        for name, available in available_optional.items()
    )
    matlab_result = None
    matlab_error = ""
    if MATLAB_RESULT.exists():
        try:
            matlab_result = json.loads(MATLAB_RESULT.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as error:
            matlab_error = f"结果文件无法读取：{error}"
    if matlab_result:
        if int(matlab_result.get("failed", 0)) > 0:
            failures.append(f"MATLAB 精选模型库失败 {matlab_result['failed']} 个分支")
        matlab_summary = (
            f"MATLAB {matlab_result['matlab_version']}（{matlab_result['release']}）："
            f"精选模型库 {matlab_result['total_branches']} 个分支中，"
            f"通过 {matlab_result['passed']}、工具箱阻塞 {matlab_result['skipped']}、"
            f"失败 {matlab_result['failed']}"
        )
        matlab_boundary = (
            "MATLAB 原始 977 个脚本仍只做来源追踪；运行结论仅适用于正式源码库的统一入口和小规模基准输入。"
        )
    else:
        if matlab_error:
            failures.append(matlab_error)
        matlab_summary = f"MATLAB 精选模型库：未完成批处理验证{('；' + matlab_error) if matlab_error else ''}"
        matlab_boundary = "MATLAB 精选模型库尚无可读取的批处理结果；原始代码仅证明来源可追溯。"
    # 从 unittest 输出解析实际运行的测试数（"Ran N tests" 输出在 stderr）
    _ran = re.search(r"Ran (\d+) tests", (public_result.stdout or "") + (public_result.stderr or ""))
    public_test_count = int(_ran.group(1)) if _ran else 0
    report = f"""---
type: validation-report
status: {'pass-with-dependency-gaps' if not failures and public_result.returncode == 0 and curated_result.returncode == 0 and not curated_compile_failures else 'failed'}
updated: {now[:10]}
tags: [area/数学建模, workflow/代码验证, system/audit]
---

# 代码验证报告

- 生成时间：{now}
- Python：`{sys.version.split()[0]}`
- 原始源码独立实现：{len(variants)}；原始路径：{sum(len(item.paths) for item in variants)}
- Python 原始实现 AST：{python_passed}/{python_checked} 通过
- 公共复用模块：{public_test_count} 项单元测试，{'通过' if public_result.returncode == 0 else '失败'}
- 精选 Python 模型库：5 个文件语法检查 {'通过' if not curated_compile_failures else '失败'}；25 个可调用分支中，本环境执行 {executed_branches} 个、依赖阻塞 {blocked_branches} 个
- 可选依赖：{optional_text}
- Keras/LSTM：未安装、未执行，只保留语法检查
- {matlab_summary}

## 状态解释

| 状态 | 能证明什么 | 不能证明什么 |
|---|---|---|
| `source-traced` | 原路径、去重关系和 SHA-256 可追溯 | 语法与运行正确性 |
| `python-ast-pass` | Python 源码可被当前解释器解析 | 依赖可用、数值正确、适合具体赛题 |
| `runtime-smoke-tested` | 指定环境和基准输入下通过测试 | 全输入正确或全局最优 |
| `project-validated` | 在项目数据、参数和检验链下复现 | 可无条件迁移到其他项目 |

原始源码逐文件状态见 [[代码验证状态.csv]]。不得把 AST 通过写成运行通过；缺少依赖的 8 个分支必须在安装相应库后重跑本报告。

## 可复现命令

```powershell
$env:PYTHONPATH='04-Research/03-建模算法源码库/00-公共复用模块/Python'
python -m unittest discover -s '04-Research/03-建模算法源码库/00-公共复用模块/Python/tests' -p 'test_*.py' -v
python -m unittest discover -s '04-Research/03-建模算法源码库/03-验证测试' -p 'test_*.py' -v
matlab -batch "cd('04-Research/03-建模算法源码库/03-验证测试'); run_matlab_validation"
python '98-AI-Context/Automation/validate_integrated_code_hubs.py'
python '98-AI-Context/Automation/audit_code_validation.py'
```

## 当前边界

- {matlab_boundary}
- 原始资料中的脚本常含绝对路径、工作区变量或数据依赖；禁止因静态检查通过而直接复制进比赛项目。
- 精选模型库缺失的 SciPy、NetworkX、statsmodels 与 Keras 依赖未自行安装，等待用户环境准备后补测。

返回 [[04-Research/03-建模算法源码库/Readme|建模算法源码库]]、[[04-Research/03-建模算法源码库/00-公共复用模块/Readme|公共复用模块]]。
"""
    REPORT.write_text(report, encoding="utf-8")

    if public_result.returncode != 0:
        failures.append("公共复用模块测试失败")
    if curated_result.returncode != 0:
        failures.append("精选模型库测试失败")
    failures.extend(curated_compile_failures)
    print(
        f"raw_variants={len(variants)} python_ast={python_passed}/{python_checked} "
        f"public_tests={'PASS' if public_result.returncode == 0 else 'FAIL'} "
        f"curated_tests={'PASS' if curated_result.returncode == 0 else 'FAIL'} "
        f"executed_branches={executed_branches} blocked_branches={blocked_branches} "
        f"matlab={'RECORDED' if matlab_result else 'NOT_RECORDED'}"
    )
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
