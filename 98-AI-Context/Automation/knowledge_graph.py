#!/usr/bin/env python3
"""Build domain Topic Hubs and a frequency-based knowledge map."""

from __future__ import annotations

import datetime as dt
import re
from collections import Counter, defaultdict
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
RESEARCH = VAULT / "04-Research"
INDEX_PATH = RESEARCH / "00-知识导航" / "Topic Index.md"
REPORT = VAULT / "98-AI-Context" / "Knowledge Map.md"
HUB_PATHS = {
    "数学建模 Hub": RESEARCH / "01-建模基础理论" / "数学建模 Hub.md",
    "评价模型 Hub": RESEARCH / "02-经典建模模型库" / "01-评价类模型" / "评价模型 Hub.md",
    "预测模型 Hub": RESEARCH / "02-经典建模模型库" / "02-预测类模型" / "预测模型 Hub.md",
    "优化模型 Hub": RESEARCH / "02-经典建模模型库" / "03-优化类模型" / "优化模型 Hub.md",
    "动态规划 Hub": RESEARCH / "02-经典建模模型库" / "03-优化类模型" / "动态规划" / "动态规划 Hub.md",
    "图论网络 Hub": RESEARCH / "02-经典建模模型库" / "04-图论与网络模型" / "图论网络 Hub.md",
    "微分方程动力学 Hub": RESEARCH / "02-经典建模模型库" / "05-微分方程动力学模型" / "微分方程动力学 Hub.md",
    "智能优化 Hub": RESEARCH / "02-经典建模模型库" / "06-智能优化算法" / "智能优化 Hub.md",
    "博弈论 Hub": RESEARCH / "02-经典建模模型库" / "07-随机决策与仿真模型" / "博弈论 Hub.md",
    "马尔可夫决策过程 Hub": RESEARCH / "02-经典建模模型库" / "07-随机决策与仿真模型" / "马尔可夫决策过程 Hub.md",
    "蒙特卡洛 Hub": RESEARCH / "02-经典建模模型库" / "07-随机决策与仿真模型" / "蒙特卡洛 Hub.md",
    "数据处理 Hub": RESEARCH / "05-数据处理方法" / "数据处理 Hub.md",
    "可视化 Hub": RESEARCH / "06-绘图可视化方法" / "可视化 Hub.md",
    "模型检验 Hub": RESEARCH / "07-模型检验与改进" / "模型检验 Hub.md",
    "论文写作 Hub": RESEARCH / "08-论文写作与复现" / "论文写作 Hub.md",
    "Python Hub": RESEARCH / "03-建模算法源码库" / "01-Python实现代码" / "Python Hub.md",
    "MATLAB Hub": RESEARCH / "03-建模算法源码库" / "02-MATLAB实现代码" / "MATLAB Hub.md",
}
CODE_SECTION_BEGIN = "<!-- BEGIN AUTO-INTEGRATED-CODE -->"
CODE_SECTION_END = "<!-- END AUTO-INTEGRATED-CODE -->"
LANGUAGE_INDEX_BEGIN = "<!-- BEGIN AUTO-LANGUAGE-CODE-INDEX -->"
LANGUAGE_INDEX_END = "<!-- END AUTO-LANGUAGE-CODE-INDEX -->"
STUDY_GUIDE_BEGIN = "<!-- BEGIN AUTO-HUB-STUDY-GUIDE -->"
STUDY_GUIDE_END = "<!-- END AUTO-HUB-STUDY-GUIDE -->"

TOPICS = {
    "数学建模 Hub": ("topic/数学建模", ["数学建模", "建模竞赛", "模型选择"]),
    "评价模型 Hub": ("topic/评价模型", ["ahp", "topsis", "熵权", "模糊综合评价", "灰色关联"]),
    "预测模型 Hub": ("topic/预测模型", ["预测", "回归", "arima", "指数平滑", "lstm", "gm(1,1)"]),
    "优化模型 Hub": ("topic/优化模型", ["规划", "优化", "目标函数", "约束"]),
    "动态规划 Hub": ("topic/动态规划", ["动态规划", "多阶段决策", "bellman"]),
    "马尔可夫决策过程 Hub": ("topic/马尔可夫决策", ["马尔可夫决策", "mdp", "状态转移概率", "动作价值"]),
    "博弈论 Hub": ("topic/博弈论", ["博弈", "纳什均衡", "支付矩阵", "混合策略", "占优策略"]),
    "蒙特卡洛 Hub": ("topic/蒙特卡洛", ["蒙特卡洛", "随机模拟", "抽样统计", "排队论"]),
    "图论网络 Hub": ("topic/图论网络", ["图论", "最短路径", "生成树", "最大流"]),
    "微分方程动力学 Hub": ("topic/动力学模型", ["微分方程", "sir", "sis", "logistic", "扩散"]),
    "智能优化 Hub": ("topic/智能优化", ["遗传算法", "粒子群", "模拟退火", "蚁群"]),
    "数据处理 Hub": ("topic/数据处理", ["数据清洗", "缺失值", "异常值", "标准化", "插值"]),
    "Python Hub": ("tool/python", ["python", "pandas", "numpy", "scipy", "matplotlib"]),
    "MATLAB Hub": ("tool/matlab", ["matlab", "optimization toolbox"]),
    "可视化 Hub": ("topic/可视化", ["绘图", "可视化", "图表", "matplotlib"]),
    "论文写作 Hub": ("topic/论文写作", ["论文", "摘要", "假设", "结果分析", "排版"]),
    "模型检验 Hub": ("topic/模型检验", ["灵敏度", "敏感性", "稳定性", "鲁棒性", "误差"]),
}

INDEX_GROUPS = {
    "总览": ["数学建模 Hub"],
    "经典模型": [
        "评价模型 Hub", "预测模型 Hub", "优化模型 Hub", "动态规划 Hub",
        "图论网络 Hub", "微分方程动力学 Hub", "智能优化 Hub",
        "博弈论 Hub", "马尔可夫决策过程 Hub", "蒙特卡洛 Hub",
    ],
    "研究流程": ["数据处理 Hub", "可视化 Hub", "模型检验 Hub", "论文写作 Hub"],
    "编程工具": ["Python Hub", "MATLAB Hub"],
}

GROUPS = {
    "工具": ["python", "matlab", "c++", "lingo", "pandas", "numpy", "scipy", "matplotlib", "git", "github", "obsidian"],
    "工作流": ["清洗", "复现", "检验", "可视化", "论文写作", "项目", "版本控制"],
    "商业模式": ["课程", "咨询", "商业化", "订阅", "开源", "付费", "产品化"],
    "平台": ["github", "obsidian", "kaggle", "知乎", "bilibili", "youtube", "微信"],
}

ADJACENCY = {
    "数学建模 Hub": ["评价模型 Hub", "预测模型 Hub", "优化模型 Hub", "论文写作 Hub"],
    "评价模型 Hub": ["数据处理 Hub", "模型检验 Hub", "可视化 Hub"],
    "预测模型 Hub": ["数据处理 Hub", "模型检验 Hub", "微分方程动力学 Hub"],
    "优化模型 Hub": ["动态规划 Hub", "智能优化 Hub", "图论网络 Hub"],
    "动态规划 Hub": ["优化模型 Hub", "马尔可夫决策过程 Hub", "博弈论 Hub"],
    "马尔可夫决策过程 Hub": ["动态规划 Hub", "蒙特卡洛 Hub", "博弈论 Hub"],
    "博弈论 Hub": ["优化模型 Hub", "动态规划 Hub", "蒙特卡洛 Hub"],
    "蒙特卡洛 Hub": ["模型检验 Hub", "数据处理 Hub", "微分方程动力学 Hub"],
    "图论网络 Hub": ["优化模型 Hub", "动态规划 Hub", "可视化 Hub"],
    "微分方程动力学 Hub": ["预测模型 Hub", "蒙特卡洛 Hub", "模型检验 Hub"],
    "智能优化 Hub": ["优化模型 Hub", "数据处理 Hub", "模型检验 Hub"],
    "数据处理 Hub": ["Python Hub", "MATLAB Hub", "可视化 Hub"],
    "Python Hub": ["数据处理 Hub", "可视化 Hub", "优化模型 Hub"],
    "MATLAB Hub": ["优化模型 Hub", "智能优化 Hub", "可视化 Hub"],
    "可视化 Hub": ["数据处理 Hub", "论文写作 Hub", "Python Hub", "MATLAB Hub"],
    "论文写作 Hub": ["可视化 Hub", "模型检验 Hub", "数学建模 Hub"],
    "模型检验 Hub": ["数据处理 Hub", "蒙特卡洛 Hub", "论文写作 Hub"],
}


def note_link(path: Path) -> str:
    return path.relative_to(VAULT).with_suffix("").as_posix()


def extract_generated_section(text: str, begin: str, end: str) -> str:
    if begin not in text or end not in text:
        return ""
    return begin + text.split(begin, 1)[1].split(end, 1)[0] + end


def preserved_generated_sections(path: Path) -> dict[str, str]:
    """Keep study/code sections embedded by the code integrator on refresh."""
    if not path.exists():
        return {"study": "", "code": "", "language": ""}
    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "study": extract_generated_section(text, STUDY_GUIDE_BEGIN, STUDY_GUIDE_END),
        "code": extract_generated_section(text, CODE_SECTION_BEGIN, CODE_SECTION_END),
        "language": extract_generated_section(text, LANGUAGE_INDEX_BEGIN, LANGUAGE_INDEX_END),
    }


def main() -> int:
    for path in HUB_PATHS.values():
        path.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    hub_files = set(HUB_PATHS.values()) | {INDEX_PATH}
    notes = [p for p in RESEARCH.rglob("*.md") if p not in hub_files and p.name != "Readme.md"]
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
        hub_path = HUB_PATHS[hub]
        preserved = preserved_generated_sections(hub_path)
        content = [
            "---", "type: topic-hub", f"topic_tag: {tag}",
            "keywords: [" + ", ".join(keys) + "]", f"tags: [system/topic-hub, {tag}]", "---", "",
            f"# {hub}", "",
        ]
        if preserved["study"]:
            content += [preserved["study"], ""]
        content += [f"> 自动更新：{dt.date.today().isoformat()} · 匹配笔记：{len(rows)}", "", "## 相关笔记", ""]
        content += [f"- [[{note_link(path)}]] — 相关度 {score}" for path, score in rows] or ["- 暂无真实研究笔记；等待导入。"]
        content += ["", "## 邻接主题", "", "- [[Topic Index]]"]
        content += [f"- [[{target}]]" for target in ADJACENCY.get(hub, [])]
        content += [""]
        for key in ("code", "language"):
            if preserved[key]:
                content += ["", preserved[key].rstrip(), ""]
        hub_path.write_text("\n".join(content), encoding="utf-8")

    index = [
        "---", "type: map-of-content", "tags: [system/topic-index, topic/knowledge-graph]", "---", "",
        "# Topic Index", "",
        "一个文件只有一个主分类目录，但可以通过多个主题标签和内部链接进入多个 Hub。", "",
    ]
    for group, hubs in INDEX_GROUPS.items():
        index += [f"## {group}", ""]
        index += [f"- [[{hub}]] — #{TOPICS[hub][0]}" for hub in hubs]
        index += [""]
    INDEX_PATH.write_text("\n".join(index), encoding="utf-8")

    report = [
        "---", "type: knowledge-map-report", "tags: [system/knowledge-graph]", "---", "",
        "# Knowledge Map", "", f"> 扫描时间：{dt.datetime.now().astimezone().isoformat(timespec='seconds')} · 真实研究笔记：{len(notes)}", "",
        "## 核心路径", "",
        "`[[知识库首页]] → [[Topic Index]] → 模型 Hub → 模型复习卡/代码实现 → 竞赛案例 → 项目复现`", "",
        "- 文件夹负责主分类，Hub 放回对应父目录；`00-知识导航` 只保存跨主题入口。",
        "- 新节点必须至少提供一种独有价值：知识结论、可执行流程、真实索引、复现证据或项目状态。", "",
        "## 高频主题", "", "| 主题 | 词频 | Hub |", "|---|---:|---|",
    ]
    report += [f"| {hub.removesuffix(' Hub')} | {count} | [[{hub}]] |" for hub, count in topic_counts.most_common()] or ["| 暂无 | 0 | 等待真实资料 |"]
    for group, counter in group_counts.items():
        report += ["", f"## 高频{group}", ""]
        report += [f"- {term}：{count}" for term, count in counter.most_common(15)] or [f"- 当前 `04-Research` 中没有形成可判定的高频{group}。"]
    report += [
        "", "## 结构关系", "",
        "- `01-建模基础理论`：建模总览与数学基础。",
        "- `02-经典建模模型库`：评价、预测、优化、图网络、动力学、智能优化、随机决策与仿真。",
        "- `03-建模算法源码库`：Python / MATLAB 语言入口与正式基础实现。",
        "- `04-竞赛真题研究`：竞赛流程、题目、论文和数据。",
        "- `05–08`：数据处理、可视化、模型检验、论文写作。",
        ""
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"research_notes={len(notes)} hubs={len(TOPICS)} report={REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
