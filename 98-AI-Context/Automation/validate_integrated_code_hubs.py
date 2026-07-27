#!/usr/bin/env python3
"""Validate the low-node code integration against the local source catalog."""

from __future__ import annotations

import ast
import json
import re
import warnings

import build_code_knowledge_graph as core
import integrate_code_into_topic_hubs as integration


def balanced_fences(text: str) -> bool:
    active = ""
    for line in text.splitlines():
        match = re.match(r"^(`{3,}|~{3,})(.*)$", line)
        if not match:
            continue
        fence, suffix = match.groups()
        if not active:
            active = fence
        elif fence[0] == active[0] and len(fence) >= len(active) and not suffix.strip():
            active = ""
    return not active


def main() -> int:
    rows = core.load_catalog(core.CODE_CATALOG)
    variants = core.make_variants(rows)
    groups = core.cluster_similar(variants)
    failures: list[str] = []
    hubs = sorted({integration.destination([variants[index] for index in group]) for group in groups})
    hub_text = {
        hub: integration.hub_path(hub).read_text(encoding="utf-8")
        for hub in hubs
    }

    for hub, text in hub_text.items():
        if integration.BEGIN not in text or integration.END not in text:
            failures.append(f"missing generated markers: {hub}")
        if integration.STUDY_BEGIN not in text or integration.STUDY_END not in text:
            failures.append(f"missing study guide: {hub}")
        if not balanced_fences(text):
            failures.append(f"unbalanced code fence: {hub}")
        if "Source Package Hub" in text or "Code Families" in text:
            failures.append(f"obsolete node reference: {hub}")

    expected_study_cards = 0
    for hub in hubs:
        labels = {
            integration.primary_label([variants[index] for index in group])
            for group in groups
            if integration.destination([variants[index] for index in group]) == hub
        }
        expected_study_cards += len(labels)
        for label in labels:
            heading = f"#### {label} · 复习"
            if hub_text[hub].count(heading) != 1:
                failures.append(f"study card count != 1: {hub}/{label}")

    for language in ("Python", "MATLAB"):
        text = integration.hub_path(f"{language} Hub").read_text(encoding="utf-8")
        if integration.LANG_BEGIN not in text or integration.LANG_END not in text:
            failures.append(f"missing language navigation index: {language}")
        if integration.STUDY_BEGIN not in text or integration.STUDY_END not in text:
            failures.append(f"missing language study guide: {language}")

    source_traces = 0
    embedded_variants = 0
    for group in groups:
        items = [variants[index] for index in group]
        hub = integration.destination(items)
        text = hub_text[hub]
        for item in items:
            embedded_variants += 1
            if "\n" + item.code.rstrip("\n") + "\n" not in text:
                failures.append(f"source body mismatch: {item.canonical_path}")
            for path in item.paths:
                source_traces += 1
                origin = f"  - 源文件：`00-Inbox/Downloaded/{path.replace('`', 'ˋ')}`"
                if text.count(origin) != 1:
                    failures.append(f"source trace count != 1: {path}")

    combined_hub_text = "\n".join(hub_text.values())
    understanding_cards = combined_hub_text.count("##### 代码理解与调用")
    collapsed_sources = combined_hub_text.count("<summary>展开原始代码</summary>")
    study_cards = len(re.findall(r"(?m)^#### .+ · 复习$", combined_hub_text))
    if study_cards != expected_study_cards:
        failures.append(f"study cards: generated={study_cards} expected={expected_study_cards}")
    if understanding_cards != len(variants):
        failures.append(f"understanding cards: generated={understanding_cards} expected={len(variants)}")
    if collapsed_sources != len(variants):
        failures.append(f"collapsed source blocks: generated={collapsed_sources} expected={len(variants)}")
    if any(token in combined_hub_text for token in ("本地数据依赖：", "数据文件：", "尚未解析的数据字面量：")):
        failures.append("data dependency detail remains in reading hubs")

    python_checked = 0
    for item in variants:
        if item.language != "Python":
            continue
        python_checked += 1
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                ast.parse(item.code)
        except SyntaxError as error:
            failures.append(f"Python syntax: {item.canonical_path}: {error.msg}")

    obsolete_root = core.LIBRARY / "00-代码知识图谱"
    if obsolete_root.exists():
        failures.append("obsolete per-file graph directory still exists")

    result = {
        "status": "PASS" if not failures else "FAIL",
        "existing_topic_hubs_with_source_checked": len(hubs),
        "existing_language_hubs_checked": 2,
        "new_graph_nodes": 0,
        "source_files_traced": source_traces,
        "exact_unique_implementations_embedded": embedded_variants,
        "implementation_groups": len(groups),
        "algorithm_study_cards": study_cards,
        "code_understanding_cards": understanding_cards,
        "collapsed_source_blocks": collapsed_sources,
        "python_unique_files_syntax_checked": python_checked,
        "failures": failures[:100],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
