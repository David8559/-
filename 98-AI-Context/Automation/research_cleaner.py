#!/usr/bin/env python3
"""Lossless structural cleaner for Obsidian research imports.

Raw files are never overwritten. Cleaned copies receive classification, topic
tags, Hub links, normalized headings/lists, and source metadata.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
DOWNLOADED = VAULT / "00-Inbox" / "Downloaded"
CLEANED = VAULT / "00-Inbox" / "Cleaned"
RESEARCH = VAULT / "04-Research"
REPORT = VAULT / "98-AI-Context" / "Research Cleaner Report.md"

CATEGORY_RULES = [
    ("04-Research/02-经典建模模型库/01-评价类模型", ["ahp", "topsis", "熵权", "模糊综合评价", "灰色关联", "评价模型"]),
    ("04-Research/02-经典建模模型库/02-预测类模型", ["预测", "回归", "arima", "指数平滑", "lstm", "gm(1,1)", "时间序列"]),
    ("04-Research/02-经典建模模型库/03-优化类模型", ["线性规划", "整数规划", "0-1规划", "多目标", "动态规划", "目标函数", "约束条件"]),
    ("04-Research/02-经典建模模型库/04-图论与网络模型", ["图论", "最短路径", "dijkstra", "floyd", "生成树", "最大流", "最小割", "排队论"]),
    ("04-Research/02-经典建模模型库/05-微分方程动力学模型", ["微分方程", "sir", "sis", "logistic", "动力学", "扩散模型"]),
    ("04-Research/02-经典建模模型库/06-智能优化算法", ["遗传算法", "粒子群", "模拟退火", "蚁群", "ga算法", "pso", "aco"]),
    ("04-Research/05-数据处理方法", ["数据清洗", "缺失值", "异常值", "归一化", "标准化", "插值", "降维", "特征工程"]),
    ("04-Research/06-绘图可视化方法", ["可视化", "绘图", "matplotlib", "seaborn", "等高线", "三维曲面", "图表排版"]),
    ("04-Research/07-模型检验与改进", ["灵敏度", "敏感性", "稳定性", "鲁棒性", "误差分析", "模型检验", "模型比较"]),
    ("04-Research/08-论文写作与复现", ["论文写作", "摘要", "问题重述", "模型假设", "符号说明", "排版", "复现"]),
    ("04-Research/04-竞赛真题研究", ["国赛", "美赛", "mcm", "icm", "竞赛真题", "获奖论文"]),
    ("04-Research/03-建模算法源码库/01-Python实现代码", ["python", "pandas", "numpy", "scipy", "sklearn"]),
    ("04-Research/03-建模算法源码库/02-MATLAB实现代码", ["matlab", "optimization toolbox"]),
]

TOPICS = [
    ("topic/评价模型", "评价模型 Hub", ["ahp", "topsis", "熵权", "模糊综合评价", "灰色关联"]),
    ("topic/预测模型", "预测模型 Hub", ["预测", "回归", "arima", "指数平滑", "lstm", "gm(1,1)"]),
    ("topic/优化模型", "优化模型 Hub", ["规划", "优化", "目标函数", "约束"]),
    ("topic/图论网络", "图论网络 Hub", ["图论", "最短路径", "生成树", "最大流", "排队论"]),
    ("topic/动力学模型", "微分方程动力学 Hub", ["微分方程", "sir", "sis", "logistic", "扩散"]),
    ("topic/智能优化", "智能优化 Hub", ["遗传算法", "粒子群", "模拟退火", "蚁群"]),
    ("topic/数据处理", "数据处理 Hub", ["数据清洗", "缺失值", "异常值", "归一化", "标准化", "插值"]),
    ("tool/python", "Python Hub", ["python", "pandas", "numpy", "scipy", "matplotlib", "sklearn"]),
    ("tool/matlab", "MATLAB Hub", ["matlab", "optimization toolbox"]),
    ("topic/可视化", "可视化 Hub", ["绘图", "可视化", "图表", "matplotlib", "seaborn"]),
    ("topic/论文写作", "论文写作 Hub", ["论文", "摘要", "模型假设", "符号说明", "排版"]),
    ("topic/模型检验", "模型检验 Hub", ["灵敏度", "敏感性", "稳定性", "鲁棒性", "误差"]),
]


def read_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="replace")


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        return {}, normalized
    match = re.match(r"\A---\n(.*?)\n---\n?", normalized, flags=re.S)
    if not match:
        return {}, normalized
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if item:
            meta[item.group(1)] = item.group(2).strip().strip('"\'')
    return meta, normalized[match.end():]


def title_from(meta: dict[str, str], body: str, path: Path) -> str:
    if meta.get("title") and "{{" not in meta["title"]:
        return meta["title"]
    match = re.search(r"^#\s+(.+?)\s*$", body, flags=re.M)
    return match.group(1).strip() if match else path.stem


def safe_name(title: str) -> str:
    value = re.sub(r"[<>:\"/\\|?*\x00-\x1f]", "-", title)
    value = re.sub(r"\s+", " ", value).strip(" .-")
    return (value[:120] or "未命名研究资料") + ".md"


def classify(text: str) -> str:
    lowered = text.lower()
    scored = [(sum(lowered.count(k.lower()) for k in keys), category) for category, keys in CATEGORY_RULES]
    score, category = max(scored, default=(0, "04-Research/01-建模基础理论"))
    return category if score else "04-Research/01-建模基础理论"


def detect_topics(text: str) -> list[tuple[str, str]]:
    lowered = text.lower()
    found = []
    for tag, hub, keys in TOPICS:
        if any(key.lower() in lowered for key in keys):
            found.append((tag, hub))
    return found or [("topic/数学建模", "数学建模 Hub")]


def normalize_structure(body: str, title: str) -> str:
    lines = body.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    output: list[str] = []
    seen_h1 = False
    in_fence = False
    for raw in lines:
        line = raw.rstrip()
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence:
            line = re.sub(r"^(\s*)(\d+)[、．]\s*", r"\1\2. ", line)
            if re.match(r"^#\s+", line):
                if seen_h1:
                    line = "#" + line
                seen_h1 = True
            elif re.match(r"^(第[一二三四五六七八九十百\d]+[章节部分]|[一二三四五六七八九十]+、).{0,35}$", line):
                line = "## " + line
            if (re.match(r"^#{1,6}\s+", line) or re.match(r"^\s*(?:[-*+] |\d+\. )", line)) and output and output[-1] != "":
                output.append("")
        output.append(line)
    while output and not output[-1]:
        output.pop()
    if not seen_h1:
        output = [f"# {title}", ""] + output
    text = "\n".join(output)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def unique_target(folder: Path, name: str, content: str) -> Path:
    candidate = folder / name
    if not candidate.exists() or read_text(candidate) == content:
        return candidate
    stem, suffix = Path(name).stem, Path(name).suffix
    index = 2
    while (folder / f"{stem}-{index}{suffix}").exists():
        index += 1
    return folder / f"{stem}-{index}{suffix}"


def clean_one(path: Path, promote: bool) -> dict[str, str]:
    raw = read_text(path)
    meta, body = split_frontmatter(raw)
    title = title_from(meta, body, path)
    source_match = re.search(r"https?://[^\s>)\]}]+", raw)
    source = meta.get("source") or meta.get("url") or (source_match.group(0) if source_match else "")
    author = meta.get("author", "")
    category = classify(title + "\n" + body)
    topics = detect_topics(title + "\n" + body)
    captured = meta.get("captured") or dt.datetime.now().astimezone().isoformat(timespec="seconds")
    tags = ["area/数学建模", "status/cleaned"] + [tag for tag, _ in topics]
    hubs = [hub for _, hub in topics]
    yaml = [
        "---", "type: research-import", f'title: "{title.replace(chr(34), chr(39))}"',
        f'source: "{source}"', f'author: "{author.replace(chr(34), chr(39))}"',
        f'captured: "{captured}"', f'original_file: "{path.name}"',
        f'category: "{category}"', "tags:", *[f"  - {tag}" for tag in tags],
        "topic_hubs:", *[f'  - "[[{hub}]]"' for hub in hubs], "---", "",
    ]
    cleaned_body = normalize_structure(body, title)
    hub_block = "\n## 主题关联\n\n" + " · ".join(f"[[{hub}]]" for hub in hubs) + "\n"
    result = "\n".join(yaml) + cleaned_body + hub_block
    CLEANED.mkdir(parents=True, exist_ok=True)
    target = unique_target(CLEANED, safe_name(title), result)
    target.write_text(result, encoding="utf-8", newline="\n")
    promoted = ""
    if promote:
        folder = VAULT / category
        folder.mkdir(parents=True, exist_ok=True)
        promoted_target = unique_target(folder, target.name, result)
        shutil.copyfile(target, promoted_target)
        promoted = promoted_target.relative_to(VAULT).as_posix()
    return {"source": path.relative_to(VAULT).as_posix(), "cleaned": target.relative_to(VAULT).as_posix(), "category": category, "topics": ", ".join(tag for tag, _ in topics), "promoted": promoted}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--promote", action="store_true", help="Also copy cleaned notes into their proposed Research category.")
    parser.add_argument("--input", type=Path, default=DOWNLOADED)
    args = parser.parse_args()
    files = [p for p in args.input.rglob("*.md") if p.name.lower() != "readme.md"]
    rows, failures = [], []
    for path in files:
        try:
            rows.append(clean_one(path, args.promote))
        except Exception as exc:  # keep batch processing and report every failure
            failures.append((str(path), str(exc)))
    lines = ["---", "type: automation-report", "tags: [system/research-cleaner]", "---", "", "# Research Cleaner Report", "", f"- 时间：{dt.datetime.now().astimezone().isoformat(timespec='seconds')}", f"- 扫描：{len(files)}", f"- 成功：{len(rows)}", f"- 失败：{len(failures)}", f"- 自动提升到 Research：{'是' if args.promote else '否'}", ""]
    if rows:
        lines += ["## 处理结果", "", "| 原始文件 | 清洗副本 | 建议主分类 | 主题 |", "|---|---|---|---|"]
        lines += [f"| `{r['source']}` | `[[{r['cleaned'][:-3]}]]` | `{r['category']}` | {r['topics']} |" for r in rows]
    if failures:
        lines += ["", "## 失败", ""] + [f"- `{p}`：{error}" for p, error in failures]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"scanned={len(files)} cleaned={len(rows)} failed={len(failures)} promote={args.promote}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
