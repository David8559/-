"""Build searchable catalogs for raw mathematical-modeling download packages."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


VAULT = Path(__file__).resolve().parents[2]
SOURCE = VAULT / "00-Inbox" / "Downloaded"
OUTPUT = VAULT / "04-Research" / "03-建模算法源码库"
ALL_CATALOG = OUTPUT / "基础资料文件清单.csv"
CODE_CATALOG = OUTPUT / "代码文件索引.csv"

CODE_EXTENSIONS = {".py", ".m", ".sas", ".lg4", ".ipynb", ".r", ".jl", ".cpp", ".c", ".h"}
DATA_EXTENSIONS = {".csv", ".xls", ".xlsx", ".mat", ".npy", ".npz", ".wf1"}
DOCUMENT_EXTENSIONS = {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".md", ".txt", ".htm", ".html", ".chm"}
ARCHIVE_EXTENSIONS = {".zip", ".rar", ".7z"}
RISK_EXTENSIONS = {".exe", ".jar", ".bin", ".pyc", ".chm"}

TOPIC_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("评价与决策", ("层次分析", "ahp", "topsis", "熵权", "综合评价", "模糊综合", "灰色关联", "主成分")),
    ("预测与时间序列", ("预测", "时间序列", "arima", "指数平滑", "回归", "灰色模型", "lstm")),
    ("优化与规划", ("规划", "最优化", "优化", "遗传算法", "粒子群", "模拟退火", "蚁群", "背包")),
    ("图论与排队", ("图论", "dijkstra", "floyd", "最短路径", "最小生成树", "排队论", "网络流")),
    ("微分与差分方程", ("微分方程", "差分方程", "龙格", "欧拉", "种群", "传染病")),
    ("统计与数据处理", ("统计", "数据处理", "聚类", "k-means", "插值", "拟合", "异常值", "降维")),
    ("机器学习与神经网络", ("神经网络", "svm", "支持向量", "机器学习", "rbf", "grnn", "小波神经")),
    ("仿真与随机模型", ("蒙特卡罗", "monte carlo", "元胞自动机", "随机", "马尔可夫")),
    ("博弈论", ("博弈", "对策论", "lingo", ".lg4")),
    ("可视化与图像", ("可视化", "绘图", "图像", "动画", "gui", "plot")),
    ("竞赛与论文写作", ("赛题", "论文", "经验", "竞赛", "写作", "格式")),
    ("数学基础", ("高等数学", "概率论", "线性代数", "数学基础")),
)


def classify_topic(relative_path: str) -> str:
    lowered = relative_path.lower()
    for topic, keywords in TOPIC_RULES:
        if any(keyword.lower() in lowered for keyword in keywords):
            return topic
    return "待人工分类"


def classify_kind(extension: str) -> str:
    if extension in CODE_EXTENSIONS:
        return "source-code"
    if extension in DATA_EXTENSIONS:
        return "data"
    if extension in DOCUMENT_EXTENSIONS:
        return "document"
    if extension in ARCHIVE_EXTENSIONS:
        return "archive"
    if extension in RISK_EXTENSIONS:
        return "executable-or-binary"
    return "other"


def read_text_sample(path: Path) -> str:
    for encoding in ("utf-8-sig", "gb18030", "utf-16", "latin-1"):
        try:
            return path.read_text(encoding=encoding)[:50_000]
        except (UnicodeDecodeError, UnicodeError):
            continue
    return ""


def looks_numeric_data(sample: str) -> bool:
    """Conservatively identify line-oriented numeric tables saved as .txt."""
    lines = [line.strip() for line in sample.splitlines() if line.strip()][:300]
    if len(lines) < 4:
        return False
    data_lines = 0
    for line in lines:
        numbers = re.findall(r"(?<![A-Za-z_])[-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?", line)
        residue = re.sub(r"[-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?", "", line)
        if len(numbers) >= 2 and not re.search(r"[A-Za-z_\u4e00-\u9fff]", residue):
            data_lines += 1
    return data_lines / len(lines) >= 0.7


def has_code_markers(sample: str) -> bool:
    patterns = (
        r"(?m)^\s*#\s*include\b|\bstd::",
        r"(?m)^\s*(?:def|class|from|import)\s+\w+",
        r"(?mi)^\s*(?:proc\s+\w+\s*;|data\s+\w+\s*;|run\s*;)",
        r"(?i)\b(?:model:|sets:|endsets|@for\s*\(|@sum\s*\()",
        r"(?mi)^\s*function\b|\b(?:clc|clear\s+all)\b|\b(?:plot|figure|zeros|ones)\s*\(",
        r"(?m)^\s*(?:for|while|if)\b[^\n]*(?:;|:)?\s*$.*?^\s*end\b",
    )
    return any(re.search(pattern, sample) for pattern in patterns)


def classify_text_file(relative_path: str, path: Path) -> str:
    """Separate source-like .txt files from local datasets and documents."""
    sample = read_text_sample(path)
    filename = path.stem.lower()
    data_named = any(keyword in filename for keyword in ("数据", "样本", "矩阵", "data", "dataset"))
    if looks_numeric_data(sample) or (data_named and not has_code_markers(sample)):
        return "data"
    if has_code_markers(sample):
        return "source-code"
    return "document"


def language(extension: str, path: Path) -> str:
    known = {
        ".py": "Python",
        ".ipynb": "Python/Jupyter",
        ".m": "MATLAB",
        ".sas": "SAS",
        ".lg4": "LINGO",
        ".r": "R",
        ".jl": "Julia",
        ".cpp": "C++",
        ".c": "C",
        ".h": "C/C++ Header",
    }.get(extension, "")
    if known or extension != ".txt":
        return known
    sample = read_text_sample(path).lower()
    if "#include" in sample or "std::" in sample:
        return "C++"
    if "def " in sample or "import numpy" in sample or "import pandas" in sample:
        return "Python"
    if "proc " in sample and ("data " in sample or "run;" in sample):
        return "SAS"
    if "@for(" in sample or "endsets" in sample or "model:" in sample:
        return "LINGO"
    if any(
        token in sample
        for token in (
            "clc", "clear all", "function ", "plot(", "zeros(", "ones(",
            "linprog(", "quadprog(", "fmincon(", "disp(", "eig(", "%",
        )
    ):
        return "MATLAB"
    return "Code Snippet"


def safety(extension: str) -> str:
    if extension in RISK_EXTENSIONS:
        return "运行前安全扫描"
    if extension in ARCHIVE_EXTENSIONS:
        return "解压前检查来源与嵌套文件"
    if extension in {".asv", ".autosave"}:
        return "临时/备份文件"
    return "normal"


def source_hash(path: Path, extension: str) -> str:
    if extension not in CODE_EXTENSIONS and extension != ".txt":
        return ""
    if path.stat().st_size > 10 * 1024 * 1024:
        return ""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    hashes: defaultdict[str, list[int]] = defaultdict(list)
    for path in sorted(SOURCE.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(SOURCE).as_posix()
        extension = path.suffix.lower()
        collection = relative.split("/", 1)[0]
        kind = classify_kind(extension)
        if extension == ".txt":
            kind = classify_text_file(relative, path)
        digest = source_hash(path, extension) if kind == "source-code" else ""
        row = {
            "relative_path": relative,
            "collection": collection,
            "topic": classify_topic(relative),
            "kind": kind,
            "language": language(extension, path) if kind == "source-code" else "",
            "extension": extension or "[none]",
            "size_kb": round(path.stat().st_size / 1024, 2),
            "safety": safety(extension),
            "sha256": digest,
            "duplicate_group": "",
        }
        rows.append(row)
        if digest:
            hashes[digest].append(len(rows) - 1)

    duplicate_groups = 0
    duplicate_files = 0
    for digest, indexes in hashes.items():
        if len(indexes) < 2:
            continue
        duplicate_groups += 1
        duplicate_files += len(indexes)
        group = f"DUP-{duplicate_groups:04d}"
        for index in indexes:
            rows[index]["duplicate_group"] = group

    fieldnames = list(rows[0]) if rows else []
    with ALL_CATALOG.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    code_rows = [row for row in rows if row["kind"] == "source-code"]
    with CODE_CATALOG.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(code_rows)

    summary = {
        "files": len(rows),
        "size_gb": round(sum(float(row["size_kb"]) for row in rows) / 1024 / 1024, 3),
        "code_files": len(code_rows),
        "collections": Counter(str(row["collection"]) for row in rows),
        "topics": Counter(str(row["topic"]) for row in rows),
        "languages": Counter(str(row["language"]) for row in code_rows),
        "kinds": Counter(str(row["kind"]) for row in rows),
        "duplicate_source_groups": duplicate_groups,
        "duplicate_source_files": duplicate_files,
        "safety_flagged": sum(row["safety"] != "normal" for row in rows),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
