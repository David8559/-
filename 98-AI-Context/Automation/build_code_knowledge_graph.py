"""Analyze and cluster local modeling source for the low-node Hub integrator.

Raw files in 00-Inbox/Downloaded are read-only. Exact duplicates are collapsed,
highly similar implementations are grouped, and original source text is decoded
without changing program content. The command-line entry point now delegates to
``integrate_code_into_topic_hubs.py`` and does not create per-file graph nodes.
"""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import shutil
import warnings
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path


VAULT = Path(__file__).resolve().parents[2]
DOWNLOADED = VAULT / "00-Inbox" / "Downloaded"
LIBRARY = VAULT / "04-Research" / "03-建模算法源码库"
CODE_CATALOG = LIBRARY / "代码文件索引.csv"
ALL_CATALOG = LIBRARY / "基础资料文件清单.csv"
GRAPH_ROOT = LIBRARY / "00-代码知识图谱"

GENERATED_DIRS = (
    "Code Families",
    "Data Assets",
    "Models",
    "Languages",
    "Packages",
    "Topics",
)

DATA_EXTENSIONS = {
    ".csv", ".xls", ".xlsx", ".mat", ".npy", ".npz", ".wf1",
    ".dat", ".data", ".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff",
}

MODEL_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("AHP层次分析", ("层次分析", "ahp")),
    ("TOPSIS", ("topsis", "优劣解")),
    ("熵权法", ("熵权",)),
    ("模糊综合评价", ("模糊综合", "fuzzy evaluation")),
    ("灰色关联分析", ("灰色关联",)),
    ("主成分分析PCA", ("主成分", "pca")),
    ("线性规划", ("线性规划", "linprog")),
    ("整数规划", ("整数规划", "0-1规划", "01规划", "intlinprog")),
    ("非线性规划", ("非线性规划", "fmincon")),
    ("多目标规划", ("多目标", "pareto")),
    ("动态规划", ("动态规划",)),
    ("遗传算法GA", ("遗传算法", "genetic algorithm", "ga_", "ga.")),
    ("粒子群PSO", ("粒子群", "pso")),
    ("模拟退火SA", ("模拟退火", "anneal")),
    ("蚁群算法ACO", ("蚁群", "ant colony", "aco")),
    ("Dijkstra最短路", ("dijkstra",)),
    ("Floyd最短路", ("floyd",)),
    ("最小生成树", ("最小生成树", "prim", "kruskal")),
    ("网络流", ("最大流", "最小割", "network flow")),
    ("排队论", ("排队论", "queueing")),
    ("回归分析", ("回归", "regression")),
    ("ARIMA时间序列", ("arima",)),
    ("指数平滑", ("指数平滑", "exponential smoothing")),
    ("灰色预测GM", ("灰色预测", "gm(1,1)", "gm11")),
    ("LSTM预测", ("lstm",)),
    ("支持向量机SVM", ("支持向量", "svm")),
    ("RBF神经网络", ("rbf", "径向基")),
    ("神经网络", ("神经网络", "neural network")),
    ("KMeans聚类", ("k-means", "kmeans")),
    ("聚类分析", ("聚类", "cluster")),
    ("插值与拟合", ("插值", "拟合", "interpolation", "curve fit")),
    ("常微分方程", ("常微分", "ode", "runge", "龙格", "欧拉")),
    ("偏微分方程", ("偏微分", "pde", "有限差分")),
    ("差分方程", ("差分方程",)),
    ("Monte Carlo", ("蒙特卡罗", "monte carlo")),
    ("元胞自动机", ("元胞自动机", "cellular automata")),
    ("马尔可夫模型", ("马尔可夫", "markov")),
    ("博弈论", ("博弈", "对策论", "lingo")),
    ("数据预处理", ("数据处理", "数据清洗", "缺失值", "异常值", "标准化", "归一化")),
    ("绘图可视化", ("绘图", "可视化", "plot", "figure")),
    ("数字图像处理", ("图像处理", "image processing", "imread")),
)

MODEL_SUMMARIES = {
    "AHP层次分析": "通过成对比较矩阵、权重计算和一致性检验完成多准则决策。",
    "TOPSIS": "通过正负理想解距离计算方案相对贴近度，适合综合评价与排序。",
    "线性规划": "在满足线性约束的条件下优化线性目标函数。",
    "整数规划": "决策变量含整数或0-1约束，用于选择、分配和组合优化。",
    "遗传算法GA": "使用选择、交叉和变异搜索复杂或非凸优化问题的近似最优解。",
    "粒子群PSO": "使用群体位置与速度更新进行连续或组合空间搜索。",
    "模拟退火SA": "通过温度下降和概率接受劣解跳出局部最优。",
    "Dijkstra最短路": "求非负权图中单源最短路径。",
    "Floyd最短路": "用动态规划求图中任意两点之间的最短距离。",
    "ARIMA时间序列": "利用差分、自回归和移动平均结构进行时间序列建模与预测。",
    "灰色预测GM": "使用少量样本的累加生成与白化方程进行趋势预测。",
    "Monte Carlo": "通过随机抽样估计概率、期望、风险或复杂系统输出。",
    "马尔可夫模型": "以状态转移概率描述具有无后效性或近似无后效性的随机过程。",
    "元胞自动机": "通过局部状态和邻域规则模拟离散时空系统演化。",
    "博弈论": "分析多个决策主体相互影响下的策略、支付与均衡。",
}

LANGUAGE_FENCES = {
    "Python": "python",
    "Python/Jupyter": "json",
    "MATLAB": "matlab",
    "SAS": "sas",
    "LINGO": "text",
    "C++": "cpp",
    "C": "c",
    "C/C++ Header": "cpp",
    "Code Snippet": "text",
}


@dataclass
class SourceVariant:
    digest: str
    language: str
    topic: str
    collection: str
    paths: list[str]
    code: str
    models: list[str]
    tokens: set[str]
    simhash: int
    symbols: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    data_paths: list[str] = field(default_factory=list)
    unresolved_data: list[str] = field(default_factory=list)
    call_paths: list[str] = field(default_factory=list)

    @property
    def canonical_path(self) -> str:
        return min(self.paths, key=lambda value: (len(value), value))


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, value: int) -> int:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: int, right: int) -> None:
        a, b = self.find(left), self.find(right)
        if a != b:
            self.parent[b] = a


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def safe_name(value: str, limit: int = 72) -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .-") or "未命名"
    return value[:limit].rstrip(" .-")


def rtf_to_text(data: bytes) -> str:
    start = data.find(b"{\\rtf")
    if start < 0:
        return ""
    source = data[start:].decode("latin-1", errors="ignore")
    output = bytearray()
    skip_stack: list[bool] = [False]
    index = 0
    destinations = {"fonttbl", "colortbl", "stylesheet", "info", "pict", "generator"}
    while index < len(source):
        char = source[index]
        if char == "{":
            look = re.match(r"\{\\\*?\\?([A-Za-z]+)", source[index:])
            skip_stack.append(skip_stack[-1] or bool(look and look.group(1) in destinations))
            index += 1
            continue
        if char == "}":
            if len(skip_stack) > 1:
                skip_stack.pop()
            index += 1
            continue
        if char != "\\":
            if not skip_stack[-1] and ord(char) < 256:
                output.append(ord(char))
            index += 1
            continue
        if index + 3 < len(source) and source[index + 1] == "'":
            if not skip_stack[-1]:
                try:
                    output.append(int(source[index + 2:index + 4], 16))
                except ValueError:
                    pass
            index += 4
            continue
        symbol = source[index + 1:index + 2]
        if symbol in {"\\", "{", "}"}:
            if not skip_stack[-1]:
                output.extend(symbol.encode("latin-1"))
            index += 2
            continue
        match = re.match(r"\\([A-Za-z]+)(-?\d+)? ?", source[index:])
        if match:
            word, number = match.group(1), match.group(2)
            if not skip_stack[-1]:
                if word in {"par", "line"}:
                    output.extend(b"\n")
                elif word == "tab":
                    output.extend(b"\t")
                elif word == "u" and number is not None:
                    value = int(number)
                    if value < 0:
                        value += 65536
                    output.extend(chr(value).encode("utf-8"))
            index += match.end()
            continue
        index += 2
    try:
        return output.decode("gb18030").replace("\x00", "").strip()
    except UnicodeDecodeError:
        return output.decode("utf-8", errors="replace").replace("\x00", "").strip()


def normalize_newlines(value: str) -> str:
    """Use stable LF newlines without changing source characters or content."""
    return value.replace("\r\n", "\n").replace("\r", "\n")


def read_source(path: Path) -> str:
    raw = path.read_bytes()
    if path.suffix.lower() == ".lg4" and raw.startswith(bytes.fromhex("D0CF11E0")):
        extracted = rtf_to_text(raw)
        if extracted:
            return normalize_newlines(extracted)
    for encoding in ("utf-8-sig", "gb18030", "utf-16", "latin-1"):
        try:
            return normalize_newlines(raw.decode(encoding))
        except (UnicodeDecodeError, UnicodeError):
            continue
    return normalize_newlines(raw.decode("latin-1", errors="replace"))


def detect_models(path_text: str, code: str) -> list[str]:
    haystack = f"{path_text}\n{code[:80_000]}".lower()
    def matches(keyword: str) -> bool:
        lowered = keyword.lower()
        if re.fullmatch(r"[a-z0-9_.()+-]+", lowered):
            return bool(re.search(rf"(?<![a-z0-9_]){re.escape(lowered)}(?![a-z0-9_])", haystack))
        return lowered in haystack

    models = [name for name, keywords in MODEL_RULES if any(matches(word) for word in keywords)]
    return models[:6]


def code_tokens(code: str) -> set[str]:
    code = re.sub(r"%[^\n]*|//[^\n]*|#(?!include)[^\n]*", " ", code)
    tokens = re.findall(r"[A-Za-z_]\w+|[\u4e00-\u9fff]{2,}", code.lower())
    stop = {"for", "while", "if", "else", "end", "function", "return", "int", "double", "import", "from"}
    return {token for token in tokens if token not in stop and len(token) > 1}


def token_simhash(tokens: set[str]) -> int:
    vector = [0] * 64
    for token in tokens:
        value = int.from_bytes(hashlib.sha256(token.encode("utf-8")).digest()[:8], "big")
        for bit in range(64):
            vector[bit] += 1 if value & (1 << bit) else -1
    result = 0
    for bit, weight in enumerate(vector):
        if weight >= 0:
            result |= 1 << bit
    return result


def hamming(left: int, right: int) -> int:
    return (left ^ right).bit_count()


def extract_symbols(language: str, code: str) -> tuple[list[str], list[str]]:
    symbols: list[str] = []
    imports: list[str] = []
    if language == "Python":
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                tree = ast.parse(code)
            symbols = [node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.append(node.module)
        except SyntaxError:
            pass
    elif language == "MATLAB":
        symbols = re.findall(r"(?mi)^\s*function\s+(?:\[[^\]]+\]|\w+\s*=\s*)?([A-Za-z]\w*)", code)
    elif language == "SAS":
        symbols = [f"PROC {name.upper()}" for name in re.findall(r"(?i)\bproc\s+(\w+)", code)]
    elif language == "LINGO":
        symbols = re.findall(r"(?i)\b(?:sets|model|data)\b", code)
    return sorted(set(symbols))[:40], sorted(set(imports))[:40]


def extract_file_literals(code: str) -> list[str]:
    extension_pattern = "|".join(re.escape(ext.lstrip(".")) for ext in sorted(DATA_EXTENSIONS | {".txt"}))
    quoted = re.findall(rf"['\"]([^'\"\n]+\.(?:{extension_pattern}))['\"]", code, flags=re.I)
    matlab_load = re.findall(r"(?mi)^\s*load\s+([^\s;,%]+)", code)
    return sorted(set(value.strip().strip("'\"") for value in quoted + matlab_load))


def clean_generated_dirs() -> None:
    root = GRAPH_ROOT.resolve()
    GRAPH_ROOT.mkdir(parents=True, exist_ok=True)
    for name in GENERATED_DIRS:
        target = (GRAPH_ROOT / name).resolve()
        if target.parent != root or target.name != name:
            raise RuntimeError(f"unsafe generated path: {target}")
        if target.exists():
            if target.is_symlink():
                raise RuntimeError(f"refusing to remove symlink: {target}")
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)


def load_catalog(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def make_variants(code_rows: list[dict[str, str]]) -> list[SourceVariant]:
    grouped: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in code_rows:
        digest = row["sha256"] or hashlib.sha256(row["relative_path"].encode("utf-8")).hexdigest()
        grouped[digest].append(row)
    variants: list[SourceVariant] = []
    for digest, rows in grouped.items():
        paths = sorted(row["relative_path"] for row in rows)
        canonical = min(rows, key=lambda row: (len(row["relative_path"]), row["relative_path"]))
        code = read_source(DOWNLOADED / canonical["relative_path"])
        tokens = code_tokens(code)
        symbols, imports = extract_symbols(canonical["language"], code)
        variants.append(
            SourceVariant(
                digest=digest,
                language=canonical["language"] or "Code Snippet",
                topic=canonical["topic"],
                collection=canonical["collection"],
                paths=paths,
                code=code,
                models=detect_models("\n".join(paths), code),
                tokens=tokens,
                simhash=token_simhash(tokens),
                symbols=symbols,
                imports=imports,
            )
        )
    return sorted(variants, key=lambda item: (item.language, item.topic, item.canonical_path))


def cluster_similar(variants: list[SourceVariant]) -> list[list[int]]:
    union = UnionFind(len(variants))
    buckets: defaultdict[tuple[str, str], list[int]] = defaultdict(list)
    for index, item in enumerate(variants):
        model_or_topic = item.models[0] if item.models else item.topic
        buckets[(item.language, model_or_topic)].append(index)
    for indexes in buckets.values():
        bands: defaultdict[tuple[int, int], list[int]] = defaultdict(list)
        for index in indexes:
            item = variants[index]
            candidates: set[int] = set()
            for band in range(4):
                key = (band, (item.simhash >> (band * 16)) & 0xFFFF)
                candidates.update(bands[key])
            stem = Path(item.canonical_path).stem.lower()
            for other_index in candidates:
                other = variants[other_index]
                if not item.tokens or not other.tokens:
                    continue
                length_ratio = len(item.code) / max(1, len(other.code))
                if not 0.55 <= length_ratio <= 1.8:
                    continue
                overlap = len(item.tokens & other.tokens) / max(1, len(item.tokens | other.tokens))
                stem_ratio = SequenceMatcher(None, stem, Path(other.canonical_path).stem.lower()).ratio()
                if (hamming(item.simhash, other.simhash) <= 7 and overlap >= 0.62) or (
                    stem_ratio >= 0.9 and overlap >= 0.45
                ):
                    union.union(index, other_index)
            for band in range(4):
                key = (band, (item.simhash >> (band * 16)) & 0xFFFF)
                bands[key].append(index)
    groups: defaultdict[int, list[int]] = defaultdict(list)
    for index in range(len(variants)):
        groups[union.find(index)].append(index)
    return sorted(groups.values(), key=lambda group: variants[group[0]].canonical_path)


def resolve_data_and_calls(
    variants: list[SourceVariant],
    all_rows: list[dict[str, str]],
) -> tuple[dict[str, str], dict[str, list[str]]]:
    all_paths = {row["relative_path"] for row in all_rows}
    by_name: defaultdict[str, list[str]] = defaultdict(list)
    for relative in all_paths:
        by_name[Path(relative).name.lower()].append(relative)
    source_paths = {path for variant in variants for path in variant.paths}
    source_by_directory_stem: defaultdict[tuple[str, str], list[str]] = defaultdict(list)
    for relative in source_paths:
        source_by_directory_stem[(str(Path(relative).parent).lower(), Path(relative).stem.lower())].append(relative)
    referenced_assets: set[str] = set()
    unresolved_by_digest: dict[str, list[str]] = {}
    for variant in variants:
        data_paths: set[str] = set()
        unresolved: set[str] = set()
        for literal in extract_file_literals(variant.code):
            normalized = literal.replace("\\", "/")
            found = False
            for source_relative in variant.paths:
                candidate = (Path(source_relative).parent / normalized).as_posix()
                if candidate in all_paths:
                    data_paths.add(candidate)
                    found = True
            if not found:
                matches = by_name.get(Path(normalized).name.lower(), [])
                if len(matches) == 1:
                    data_paths.add(matches[0])
                    found = True
            if not found:
                unresolved.add(literal)
        call_paths: set[str] = set()
        if variant.language == "Python":
            names = {name.split(".")[0].lower() for name in variant.imports}
        elif variant.language == "MATLAB":
            names = set(re.findall(r"\b([A-Za-z]\w*)\s*\(", variant.code))
        else:
            names = set()
        for source_relative in variant.paths:
            directory = str(Path(source_relative).parent).lower()
            for name in names:
                for match in source_by_directory_stem.get((directory, name.lower()), []):
                    if match not in variant.paths:
                        call_paths.add(match)
        variant.data_paths = sorted(data_paths)
        variant.unresolved_data = sorted(unresolved)
        variant.call_paths = sorted(call_paths)
        referenced_assets.update(data_paths)
        unresolved_by_digest[variant.digest] = sorted(unresolved)
    return {path: "" for path in sorted(referenced_assets)}, unresolved_by_digest


def write_data_notes(all_rows: list[dict[str, str]], referenced: dict[str, str]) -> dict[str, str]:
    data_rows = {row["relative_path"]: row for row in all_rows if row["kind"] == "data"}
    for path in referenced:
        if path not in data_rows:
            source = DOWNLOADED / path
            data_rows[path] = {
                "relative_path": path,
                "extension": source.suffix.lower(),
                "size_kb": str(round(source.stat().st_size / 1024, 2)) if source.exists() else "",
                "topic": "本地数据依赖",
                "collection": path.split("/", 1)[0],
            }
    note_map: dict[str, str] = {}
    output = GRAPH_ROOT / "Data Assets"
    for relative, row in sorted(data_rows.items()):
        digest = hashlib.sha256(relative.encode("utf-8")).hexdigest()[:8]
        title = safe_name(f"DATA-{Path(relative).stem}-{digest}")
        note_map[relative] = title
        actual_link = f"[[00-Inbox/Downloaded/{relative}|{Path(relative).name}]]"
        content = f"""---
type: local-data-asset
status: local-only
extension: {yaml_string(row.get('extension', ''))}
size_kb: {row.get('size_kb', '') or 0}
topic: {yaml_string(row.get('topic', '本地数据依赖'))}
tags: [data/local, workflow/code-dependency]
---

# {title}

- 本地文件：{actual_link}
- 来源资料包：[[{safe_name(row.get('collection', '未知资料包'))} · Source Package Hub]]
- Vault 相对路径：`00-Inbox/Downloaded/{relative}`

> [!note]
> 数据保存在本地 Vault，未复制到 GitHub。字段、单位和质量尚未逐项验证。
"""
        (output / f"{title}.md").write_text(content, encoding="utf-8")
    return note_map


def family_title(group: list[int], variants: list[SourceVariant]) -> str:
    items = [variants[index] for index in group]
    models = [model for item in items for model in item.models]
    base = Counter(models).most_common(1)[0][0] if models else items[0].topic
    language = Counter(item.language for item in items).most_common(1)[0][0]
    stem = Path(items[0].canonical_path).stem
    digest = hashlib.sha256("|".join(sorted(item.digest for item in items)).encode("utf-8")).hexdigest()[:8]
    label = f"{base}-{language}-{'代码族' if len(items) > 1 else stem}-{digest}"
    return safe_name(label)


def write_family_notes(
    variants: list[SourceVariant],
    groups: list[list[int]],
    data_note_map: dict[str, str],
) -> tuple[dict[str, str], list[dict[str, object]]]:
    titles = {index: family_title(group, variants) for index, group in enumerate(groups)}
    path_to_group: dict[str, int] = {}
    for group_index, group in enumerate(groups):
        for index in group:
            for path in variants[index].paths:
                path_to_group[path] = group_index
    metadata: list[dict[str, object]] = []
    output = GRAPH_ROOT / "Code Families"
    for group_index, group in enumerate(groups):
        items = [variants[index] for index in group]
        title = titles[group_index]
        languages = sorted({item.language for item in items})
        topics = sorted({item.topic for item in items})
        models = sorted({model for item in items for model in item.models})
        collections = sorted({Path(path).parts[0] for item in items for path in item.paths})
        source_count = sum(len(item.paths) for item in items)
        data_paths = sorted({path for item in items for path in item.data_paths})
        call_groups = sorted(
            {
                path_to_group[path]
                for item in items
                for path in item.call_paths
                if path in path_to_group and path_to_group[path] != group_index
            }
        )
        primary_model = models[0] if models else topics[0]
        summary = MODEL_SUMMARIES.get(primary_model, f"该代码族归入“{primary_model}”，用于对应数学建模任务的计算或实验。")
        relationship_links = []
        relationship_links.extend(f"[[{safe_name(model)} · Model Code Hub]]" for model in models)
        relationship_links.extend(f"[[{safe_name(language)} · Code Language Hub]]" for language in languages)
        relationship_links.extend(f"[[{safe_name(topic)} · Code Topic Hub]]" for topic in topics)
        relationship_links.extend(f"[[{safe_name(collection)} · Source Package Hub]]" for collection in collections)
        body = [
            "---",
            "type: code-family",
            f"code_id: {yaml_string('CF-' + hashlib.sha256(title.encode('utf-8')).hexdigest()[:10])}",
            "status: source-traced",
            f"language: {yaml_string(', '.join(languages))}",
            f"topic: {yaml_string(', '.join(topics))}",
            f"variant_count: {len(items)}",
            f"source_count: {source_count}",
            "tags: [code/source, workflow/code-knowledge-graph]",
            "---",
            "",
            f"# {title}",
            "",
            "## 代码族总结",
            "",
            summary,
            "",
            f"- 独立实现变体：{len(items)}",
            f"- 原始来源文件：{source_count}",
            f"- 相似性结论：{'包含高度相似实现；以下分别保留原代码并列出来源。' if len(items) > 1 else '当前未发现达到阈值的相似实现。'}",
            "- 验证状态：未运行；自动归类不等于算法正确性证明。",
            "",
            "## 图谱关系",
            "",
            " · ".join(dict.fromkeys(relationship_links)) if relationship_links else "尚未自动识别模型关系。",
            "",
            "## 本地数据依赖",
            "",
        ]
        if data_paths:
            body.extend(f"- [[{data_note_map[path]}]]" for path in data_paths if path in data_note_map)
        else:
            body.append("- 未从源码中的文件字面量自动识别；不代表该代码一定无外部数据。")
        unresolved = sorted({value for item in items for value in item.unresolved_data})
        if unresolved:
            body.extend(["", "### 尚未解析的文件引用", ""])
            body.extend(f"- `{value}`" for value in unresolved)
        if call_groups:
            body.extend(["", "## 同目录代码调用", ""])
            body.extend(f"- [[{titles[index]}]]" for index in call_groups)
        body.extend(["", "## 原始实现", ""])
        for variant_number, item in enumerate(items, start=1):
            body.extend(
                [
                    f"### 变体 {variant_number}：{Path(item.canonical_path).name}",
                    "",
                    f"- SHA-256：`{item.digest}`",
                    f"- 语言：{item.language}",
                    f"- 自动识别符号：{', '.join(f'`{symbol}`' for symbol in item.symbols) if item.symbols else '未识别'}",
                    f"- 外部导入：{', '.join(f'`{name}`' for name in item.imports) if item.imports else '未识别或不适用'}",
                    "- 原始来源：",
                ]
            )
            body.extend(
                f"  - [[00-Inbox/Downloaded/{path}|{path}]]" for path in item.paths
            )
            fence = "````" if "````" not in item.code else "`````"
            body.extend(
                [
                    "",
                    f"{fence}{LANGUAGE_FENCES.get(item.language, 'text')}",
                    item.code.rstrip("\n"),
                    fence,
                    "",
                ]
            )
        (output / f"{title}.md").write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")
        metadata.append(
            {
                "title": title,
                "languages": languages,
                "topics": topics,
                "models": models,
                "collections": collections,
                "variants": len(items),
                "sources": source_count,
                "data": data_paths,
            }
        )
    return {path: titles[group_index] for path, group_index in path_to_group.items()}, metadata


def write_hubs(metadata: list[dict[str, object]], data_note_map: dict[str, str]) -> None:
    dimensions = (
        ("Models", "models", "Model Code Hub", "模型"),
        ("Languages", "languages", "Code Language Hub", "语言"),
        ("Packages", "collections", "Source Package Hub", "资料包"),
        ("Topics", "topics", "Code Topic Hub", "主题"),
    )
    for directory, key, suffix, label in dimensions:
        groups: defaultdict[str, list[dict[str, object]]] = defaultdict(list)
        for item in metadata:
            for value in item[key]:
                groups[str(value)].append(item)
        for value, items in sorted(groups.items()):
            title = safe_name(f"{value} · {suffix}")
            summary = MODEL_SUMMARIES.get(value, f"该 Hub 汇总与“{value}”相关的代码族。")
            lines = [
                "---",
                "type: code-hub",
                f"dimension: {yaml_string(label)}",
                f"value: {yaml_string(value)}",
                f"code_family_count: {len(items)}",
                "tags: [code/hub, topic/代码知识图谱]",
                "---",
                "",
                f"# {title}",
                "",
                summary,
                "",
                f"共 {len(items)} 个代码族。",
                "",
                "## 代码族",
                "",
            ]
            lines.extend(
                f"- [[{item['title']}]] — {item['variants']} 个变体，{item['sources']} 个来源"
                for item in sorted(items, key=lambda data: str(data["title"]))
            )
            (GRAPH_ROOT / directory / f"{title}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    data_groups: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)
    for relative, title in data_note_map.items():
        data_groups[Path(relative).suffix.lower() or "无扩展名"].append((relative, title))
    lines = [
        "---",
        "type: data-hub",
        "status: local-only",
        "tags: [data/local, topic/代码知识图谱]",
        "---",
        "",
        "# 本地数据资产 Hub",
        "",
        "这些数据保存在 `00-Inbox/Downloaded`，用于维持原始代码的相对路径和可复现条件，不进入 GitHub。",
        "",
    ]
    for extension, items in sorted(data_groups.items()):
        lines.extend([f"## {extension}（{len(items)}）", ""])
        lines.extend(f"- [[{title}]]" for _, title in sorted(items))
        lines.append("")
    (GRAPH_ROOT / "本地数据资产 Hub.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_overview(
    variants: list[SourceVariant],
    groups: list[list[int]],
    metadata: list[dict[str, object]],
    data_note_map: dict[str, str],
) -> None:
    similar_families = sum(1 for group in groups if len(group) > 1)
    exact_collapsed = sum(len(variant.paths) - 1 for variant in variants)
    model_counts = Counter(model for item in metadata for model in item["models"])
    top_models = model_counts.most_common(18)
    lines = [
        "---",
        "type: map-of-content",
        "title: 数学建模代码知识图谱",
        "status: generated",
        "tags: [area/数学建模, topic/代码知识图谱, workflow/代码整理]",
        "---",
        "",
        "# 数学建模代码知识图谱",
        "",
        "> [!summary] 生成口径",
        "> 原始代码逐字保留在代码族笔记中；完全重复内容只嵌入一次，高度相似实现合并为代码族。所有代码默认标记为“未运行验证”。",
        "",
        "## 规模",
        "",
        f"- 原始代码来源：{sum(len(item.paths) for item in variants)}",
        f"- 去除精确重复后的独立实现：{len(variants)}",
        f"- 合并后的代码族：{len(groups)}",
        f"- 含相似变体的代码族：{similar_families}",
        f"- 折叠的精确重复副本：{exact_collapsed}",
        f"- 本地数据资产节点：{len(data_note_map)}",
        "",
        "## 关系结构",
        "",
        "```mermaid",
        "flowchart LR",
        "  Q[数学建模问题] --> M[模型与算法 Hub]",
        "  M --> F[代码族笔记]",
        "  F --> V[原始实现变体]",
        "  F --> D[本地数据资产]",
        "  F --> L[Python / MATLAB / SAS / LINGO]",
        "  F --> P[原始资料包]",
        "  V --> O[结果、图表与论文]",
        "  D -.仅本地保存.-> F",
        "```",
        "",
        "## 高频模型入口",
        "",
    ]
    lines.extend(f"- [[{safe_name(model)} · Model Code Hub]]：{count} 个代码族" for model, count in top_models)
    lines.extend(
        [
            "",
            "## 多维入口",
            "",
            "- [[本地数据资产 Hub]]",
            "- [[代码聚类质量审计]]",
            "- `Models/`：按具体模型浏览",
            "- `Topics/`：按研究主题浏览",
            "- `Languages/`：按编程语言浏览",
            "- `Packages/`：按原始资料包浏览",
            "",
            "## 使用规则",
            "",
            "1. 先从模型 Hub 选择算法，再比较同一代码族的实现变体。",
            "2. 数据链接指向本地 Vault；GitHub 上只有笔记和嵌入的源码。",
            "3. 自动识别的数据依赖和相似关系属于 Agent 推断，运行前必须人工核对。",
            "4. 选定实现后复制到具体项目，补充环境、参数、字段说明、测试和结果。",
        ]
    )
    (GRAPH_ROOT / "代码知识图谱总览.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_similarity_audit(
    variants: list[SourceVariant],
    groups: list[list[int]],
    metadata: list[dict[str, object]],
) -> None:
    """Create a transparent review queue for every non-exact merge."""
    rows: list[tuple[str, int, int, str, float, int, str]] = []
    for group_index, group in enumerate(groups):
        if len(group) < 2:
            continue
        items = [variants[index] for index in group]
        overlaps: list[float] = []
        distances: list[int] = []
        for left_index, left in enumerate(items):
            for right in items[left_index + 1:]:
                overlaps.append(len(left.tokens & right.tokens) / max(1, len(left.tokens | right.tokens)))
                distances.append(hamming(left.simhash, right.simhash))
        minimum_overlap = min(overlaps, default=0.0)
        maximum_distance = max(distances, default=64)
        if minimum_overlap >= 0.62 and maximum_distance <= 7:
            review = "高一致性"
        elif minimum_overlap >= 0.45:
            review = "文件名/结构相似，建议抽查"
        else:
            review = "可能为传递聚类，优先人工复核"
        rows.append(
            (
                str(metadata[group_index]["title"]),
                len(items),
                sum(len(item.paths) for item in items),
                ", ".join(sorted({item.language for item in items})),
                minimum_overlap,
                maximum_distance,
                review,
            )
        )
    high = sum(row[-1] == "高一致性" for row in rows)
    inspect = sum(row[-1] != "高一致性" for row in rows)
    lines = [
        "---",
        "type: code-cluster-audit",
        "status: generated",
        "tags: [system/audit, code/similarity]",
        "---",
        "",
        "# 代码聚类质量审计",
        "",
        "> [!important] 结论边界",
        "> 精确重复由 SHA-256 判定；下表只审计非精确的相似合并。相似不等于算法正确，也不等于两个实现可以互换。",
        "",
        "## 验收摘要",
        "",
        f"- 相似代码族：{len(rows)}",
        f"- 高一致性：{high}",
        f"- 建议人工抽查：{inspect}",
        "- 跨语言合并：0（聚类前按语言隔离）",
        "- 阈值：SimHash 汉明距离不大于 7 且词元 Jaccard 不低于 0.62；或文件名相似度不低于 0.90 且 Jaccard 不低于 0.45。",
        "- 质量标记使用组内最弱一对指标，能暴露由传递闭包造成的宽松合并。",
        "",
        "## 全量复核队列",
        "",
        "| 代码族 | 变体 | 原始来源 | 语言 | 最低 Jaccard | 最大汉明距离 | 复核等级 |",
        "|---|---:|---:|---|---:|---:|---|",
    ]
    for title, item_count, source_count, language, overlap, distance, review in sorted(rows):
        lines.append(
            f"| [[{title}]] | {item_count} | {source_count} | {language} | {overlap:.3f} | {distance} | {review} |"
        )
    lines.extend(
        [
            "",
            "## 使用规则",
            "",
            "1. 优先检查标记为“可能为传递聚类”的代码族。",
            "2. 复核时比较输入字段、参数含义、目标函数、约束、输出及依赖数据，而不只看文件名。",
            "3. 如果实现目的不同，应调整分类规则并重新运行生成器，不直接手改生成笔记。",
            "",
        ]
    )
    (GRAPH_ROOT / "代码聚类质量审计.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    # Compatibility entry point.  Per-file graph nodes were retired because
    # they overwhelmed the research graph.  All source is now embedded into
    # the existing domain Topic Hubs.
    from integrate_code_into_topic_hubs import main as integrate_main

    raise SystemExit(integrate_main())


if __name__ == "__main__":
    main()
