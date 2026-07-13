#!/usr/bin/env python3
"""Build domain Topic Hubs and a frequency-based knowledge map."""

from __future__ import annotations

import datetime as dt
import re
from collections import Counter, defaultdict
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
RESEARCH = VAULT / "04-Research"
HUBS = RESEARCH / "00-Topic-Hubs"
REPORT = VAULT / "98-AI-Context" / "Current Knowledge Map.md"

TOPICS = {
    "数学建模 Hub": ("topic/数学建模", ["数学建模", "建模竞赛", "模型选择"]),
    "评价模型 Hub": ("topic/评价模型", ["ahp", "topsis", "熵权", "模糊综合评价", "灰色关联"]),
    "预测模型 Hub": ("topic/预测模型", ["预测", "回归", "arima", "指数平滑", "lstm", "gm(1,1)"]),
    "优化模型 Hub": ("topic/优化模型", ["规划", "优化", "目标函数", "约束"]),
    "图论网络 Hub": ("topic/图论网络", ["图论", "最短路径", "生成树", "最大流", "排队论"]),
    "微分方程动力学 Hub": ("topic/动力学模型", ["微分方程", "sir", "sis", "logistic", "扩散"]),
    "智能优化 Hub": ("topic/智能优化", ["遗传算法", "粒子群", "模拟退火", "蚁群"]),
    "数据处理 Hub": ("topic/数据处理", ["数据清洗", "缺失值", "异常值", "标准化", "插值"]),
    "Python Hub": ("tool/python", ["python", "pandas", "numpy", "scipy", "matplotlib"]),
    "MATLAB Hub": ("tool/matlab", ["matlab", "optimization toolbox"]),
    "可视化 Hub": ("topic/可视化", ["绘图", "可视化", "图表", "matplotlib"]),
    "论文写作 Hub": ("topic/论文写作", ["论文", "摘要", "假设", "结果分析", "排版"]),
    "模型检验 Hub": ("topic/模型检验", ["灵敏度", "敏感性", "稳定性", "鲁棒性", "误差"]),
}

GROUPS = {
    "工具": ["python", "matlab", "pandas", "numpy", "scipy", "matplotlib", "git", "github", "obsidian"],
    "工作流": ["清洗", "复现", "检验", "可视化", "论文写作", "项目", "版本控制"],
    "商业模式": ["课程", "咨询", "商业化", "订阅", "开源", "付费", "产品化"],
    "平台": ["github", "obsidian", "kaggle", "知乎", "bilibili", "youtube", "微信"],
}


def note_link(path: Path) -> str:
    return path.relative_to(VAULT).with_suffix("").as_posix()


def main() -> int:
    HUBS.mkdir(parents=True, exist_ok=True)
    notes = [p for p in RESEARCH.rglob("*.md") if HUBS not in p.parents and p.name != "Readme.md"]
    matches: dict[str, list[tuple[Path, int]]] = defaultdict(list)
    group_counts: dict[str, Counter[str]] = {name: Counter() for name in GROUPS}
    topic_counts = Counter()
    for path in notes:
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        searchable = path.stem.lower() + "\n" + text
        for hub, (_, keys) in TOPICS.items():
            score = sum(searchable.count(key.lower()) for key in keys)
            if score:
                matches[hub].append((path, score))
                topic_counts[hub] += score
        for group, terms in GROUPS.items():
            for term in terms:
                count = searchable.count(term.lower())
                if count:
                    group_counts[group][term] += count

    for hub, (tag, keys) in TOPICS.items():
        rows = sorted(matches.get(hub, []), key=lambda item: (-item[1], str(item[0])))
        content = [
            "---", "type: topic-hub", f"topic_tag: {tag}",
            "keywords: [" + ", ".join(keys) + "]", f"tags: [system/topic-hub, {tag}]", "---", "",
            f"# {hub}", "", f"> 自动更新：{dt.date.today().isoformat()} · 匹配笔记：{len(rows)}", "",
            "## 相关笔记", "",
        ]
        content += [f"- [[{note_link(path)}]] — 相关度 {score}" for path, score in rows] or ["- 暂无真实研究笔记；等待导入。"]
        content += ["", "## 邻接主题", "", "- [[Topic Index]]", ""]
        (HUBS / f"{hub}.md").write_text("\n".join(content), encoding="utf-8")

    report = [
        "---", "type: knowledge-map-report", "tags: [system/knowledge-graph]", "---", "",
        "# Current Knowledge Map", "", f"> 扫描时间：{dt.datetime.now().astimezone().isoformat(timespec='seconds')} · 真实研究笔记：{len(notes)}", "",
        "## 高频主题", "", "| 主题 | 词频 | Hub |", "|---|---:|---|",
    ]
    report += [f"| {hub.removesuffix(' Hub')} | {count} | [[{hub}]] |" for hub, count in topic_counts.most_common()] or ["| 暂无 | 0 | 等待真实资料 |"]
    for group, counter in group_counts.items():
        report += ["", f"## 高频{group}", ""]
        report += [f"- {term}：{count}" for term, count in counter.most_common(15)] or [f"- 当前 `04-Research` 中没有形成可判定的高频{group}。"]
    report += ["", "## 结构关系", "", "基础理论 → 模型库 → 数据处理与代码实现 → 模型检验 → 论文写作与复现；竞赛真题通过 Topic Hub 横向连接模型、工具和检验方法。", ""]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"research_notes={len(notes)} hubs={len(TOPICS)} report={REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
