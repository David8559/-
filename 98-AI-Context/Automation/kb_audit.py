#!/usr/bin/env python3
"""Audit duplicates, conflicts, naming, empties, junk, links, and orphans."""

from __future__ import annotations

import datetime as dt
import hashlib
import re
from collections import defaultdict
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
REPORT = VAULT / "98-AI-Context" / "Knowledge Base Audit Report.md"
IGNORE_DIRS = {".git", ".trash", "__pycache__", ".cache"}
JUNK_NAMES = {"thumbs.db", ".ds_store", "desktop.ini"}
JUNK_SUFFIXES = {".tmp", ".bak", ".swp", ".part", ".pyc"}
INVALID = re.compile(r'[<>:"|?*]|[ .]$')


def is_pipeline_copy(path: Path) -> bool:
    """Inbox working copies are expected lifecycle artifacts, not canonical notes."""
    return rel(path).startswith(("00-Inbox/Downloaded/", "00-Inbox/Cleaned/"))


def all_files() -> list[Path]:
    return [p for p in VAULT.rglob("*") if p.is_file() and not any(part in IGNORE_DIRS for part in p.parts)]


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def section(title: str, items: list[str], ok: str = "未发现问题。") -> list[str]:
    return [f"## {title}", ""] + ([f"- {item}" for item in items] if items else [f"- {ok}"]) + [""]


def main() -> int:
    files = all_files()
    md_files = [p for p in files if p.suffix.lower() == ".md" and p != REPORT]
    digest_map: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        if is_pipeline_copy(path):
            continue
        if path.stat().st_size:
            digest_map[hashlib.sha256(path.read_bytes()).hexdigest()].append(path)
    duplicates = [", ".join(f"`{rel(p)}`" for p in paths) for paths in digest_map.values() if len(paths) > 1]
    bad_names = [f"`{rel(p)}`" for p in files if INVALID.search(p.name) or p.stem.lower() in {"untitled", "未命名", "新建笔记"}]
    empty_dirs = [f"`{rel(p)}`" for p in VAULT.rglob("*") if p.is_dir() and not any(part in IGNORE_DIRS for part in p.parts) and not any(p.iterdir())]
    junk = [f"`{rel(p)}`" for p in files if p.name.lower() in JUNK_NAMES or p.suffix.lower() in JUNK_SUFFIXES or p.name.startswith("~$")]

    stem_index: dict[str, list[Path]] = defaultdict(list)
    for p in md_files:
        if is_pipeline_copy(p):
            continue
        stem_index[p.stem.lower()].append(p)
    ambiguous = [f"名称 `{name}`：" + ", ".join(f"`{rel(p)}`" for p in paths) for name, paths in stem_index.items() if len(paths) > 1 and name not in {"readme", "agents", "project-status"}]

    link_targets = CounterLike()
    outbound: dict[Path, list[str]] = {}
    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        links = [m.split("|")[0].split("#")[0].strip() for m in re.findall(r"\[\[([^\]]+)\]\]", text)]
        outbound[path] = [item for item in links if item]
        for item in outbound[path]:
            link_targets.add(Path(item).name.lower())
    orphans = []
    for path in md_files:
        if path.name in {"知识库首页.md", "Topic Index.md"} or path.name.endswith("Template.md") or path.name == "Readme.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        has_tag = bool(re.search(r"(?m)^tags:\s*", text))
        if not outbound[path] and not link_targets.contains(path.stem.lower()) and not has_tag:
            orphans.append(f"`{rel(path)}`")

    conflicts = []
    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"(?m)^category:\s*(.+)$", text)
        if match and ("," in match.group(1) or match.group(1).strip().startswith("[")):
            conflicts.append(f"`{rel(path)}`：category 不是单一值")

    unresolved = []
    known_stems = set(stem_index)
    known_paths = {p.relative_to(VAULT).with_suffix("").as_posix().lower() for p in md_files}
    known_names = {p.name.lower() for p in files}
    known_stems.update(p.stem.lower() for p in files)
    known_paths.update(p.relative_to(VAULT).with_suffix("").as_posix().lower() for p in files)
    known_stems.add(REPORT.stem.lower())
    known_paths.add(REPORT.relative_to(VAULT).with_suffix("").as_posix().lower())
    for path, links in outbound.items():
        if path.name == "欢迎.md" or "90-Templates" in path.parts:
            continue
        for item in links:
            normalized = item.replace("\\", "/").lower()
            if normalized not in known_paths and Path(normalized).name not in known_names and Path(normalized).stem not in known_stems:
                unresolved.append(f"`{rel(path)}` → `[[{item}]]`")

    issue_count = sum(map(len, [duplicates, bad_names, empty_dirs, junk, ambiguous, orphans, conflicts, unresolved]))
    score = max(0, 100 - len(duplicates) * 5 - len(bad_names) * 2 - len(empty_dirs) - len(junk) * 3 - len(orphans) * 2 - len(conflicts) * 4 - len(unresolved))
    lines = [
        "---", "type: audit-report", "tags: [system/audit]", "---", "", "# Knowledge Base Audit Report", "",
        f"- 时间：{dt.datetime.now().astimezone().isoformat(timespec='seconds')}", f"- 文件：{len(files)}（Markdown {len(md_files)}）",
        f"- 问题项：{issue_count}", f"- 结构健康评分：{score}/100", "",
    ]
    lines += section("重复内容", duplicates)
    lines += section("分类冲突", conflicts)
    lines += section("异常或含糊文件名", bad_names + ambiguous)
    lines += section("空目录", empty_dirs)
    lines += section("垃圾文件", junk)
    lines += section("孤立文件", orphans)
    lines += section("未解析内部链接", unresolved)
    lines += ["## 结论", "", "评分只反映结构卫生，不代表研究内容深度。新建 Vault 的主要薄弱项通常是真实研究材料和项目尚未导入，而不是目录缺失。", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"files={len(files)} markdown={len(md_files)} issues={issue_count} score={score}")
    return 0


class CounterLike:
    def __init__(self) -> None:
        self._items: set[str] = set()

    def add(self, item: str) -> None:
        self._items.add(item)

    def contains(self, item: str) -> bool:
        return item in self._items


if __name__ == "__main__":
    raise SystemExit(main())
