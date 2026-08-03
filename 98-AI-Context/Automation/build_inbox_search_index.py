#!/usr/bin/env python3
"""Build Obsidian-searchable indexes for Python sources and Inbox archives.

Original files under ``00-Inbox/Downloaded`` are read-only.  This script only
creates derived Markdown/CSV inventories under ``00-Inbox/Cleaned``.
"""

from __future__ import annotations

import csv
import hashlib
import subprocess
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path, PurePosixPath


VAULT = Path(__file__).resolve().parents[2]
INBOX = VAULT / "00-Inbox"
DOWNLOADED = INBOX / "Downloaded"
PYTHON_ROOT = DOWNLOADED / "数学建模Python相关"
CLEANED = INBOX / "Cleaned"
PYTHON_INDEX = CLEANED / "数学建模Python相关-源码索引.md"
ARCHIVE_INDEX = CLEANED / "Inbox-压缩包清点索引.md"
ARCHIVE_CSV = CLEANED / "Inbox-压缩包清单.csv"
MEMBER_ROOT = CLEANED / "Inbox-压缩包成员索引"
SOURCE_SHARDS = VAULT / "04-Research" / "03-建模算法源码库" / "04-原始源码分片"

ARCHIVE_EXTENSIONS = {".zip", ".rar", ".7z"}
RISK_EXTENSIONS = {".exe", ".com", ".bat", ".cmd", ".ps1", ".msi", ".scr", ".jar"}
MAX_MEMBER_LINES_PER_SHARD = 1_000


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def wiki(path: Path, label: str | None = None) -> str:
    relative = path.relative_to(VAULT).as_posix().replace("|", "-")
    return f"[[{relative}|{label or path.name}]]"


def decode_listing(raw: bytes) -> str:
    for encoding in ("utf-8", "gb18030", "cp437"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def list_archive(path: Path) -> tuple[str, list[str], str]:
    with path.open("rb") as stream:
        signature = stream.read(16)
    if signature.startswith(b"kZ"):
        return "专有格式待工具", [], "文件头为快压 KZ，不是标准 ZIP；需快压或兼容工具只读清点"
    try:
        result = subprocess.run(
            ["tar", "-tf", str(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=90,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as error:
        return "无法清点", [], type(error).__name__
    members = [line.strip() for line in decode_listing(result.stdout).splitlines() if line.strip()]
    if result.returncode != 0:
        detail = decode_listing(result.stderr).strip().replace("\n", " ")[:160]
        return "清点失败", members, detail or f"tar exit {result.returncode}"
    return "成员已索引", members, ""


def member_risks(members: list[str]) -> tuple[int, int, int]:
    nested = risky = traversal = 0
    for member in members:
        normalized = member.replace("\\", "/")
        suffix = PurePosixPath(normalized).suffix.lower()
        nested += suffix in ARCHIVE_EXTENSIONS
        risky += suffix in RISK_EXTENSIONS
        traversal += normalized.startswith("/") or "../" in f"/{normalized}"
    return nested, risky, traversal


def source_trace_paths() -> set[str]:
    traced: set[str] = set()
    if not SOURCE_SHARDS.exists():
        return traced
    for note in SOURCE_SHARDS.rglob("*.md"):
        for line in note.read_text(encoding="utf-8", errors="replace").splitlines():
            marker = "源文件：`00-Inbox/Downloaded/"
            if marker not in line:
                continue
            value = line.split(marker, 1)[1].split("`", 1)[0]
            traced.add(value)
    return traced


def build_python_index() -> dict[str, int]:
    files = sorted(PYTHON_ROOT.rglob("*.py"))
    traced = source_trace_paths()
    rows = []
    hashes: defaultdict[str, list[Path]] = defaultdict(list)
    for path in files:
        digest = sha256(path)
        hashes[digest].append(path)
        source_relative = path.relative_to(DOWNLOADED).as_posix()
        rows.append((path, source_relative, digest, source_relative in traced))

    duplicate_files = sum(len(paths) for paths in hashes.values() if len(paths) > 1)
    lines = [
        "---",
        "type: inbox-index",
        "status: generated-reviewed",
        f"updated: {datetime.now().date().isoformat()}",
        "tags: [area/数学建模, tool/python, workflow/inbox-归档]",
        "---",
        "",
        "# 数学建模 Python 相关 · 源码索引",
        "",
        "> [!summary] 检索结论",
        f"> 原件共 **{len(files)}** 个 `.py` 文件；精确去重后 **{len(hashes)}** 个实现；"
        f"已有 **{sum(row[3] for row in rows)}/{len(files)}** 条来源路径写入可搜索源码分片。",
        "> 本页是只读原件的派生索引，不移动、不改写 `00-Inbox/Downloaded`。语法通过不等于运行或数值验证通过。",
        "",
        "关联：[[04-Research/03-建模算法源码库/代码资料索引]] · "
        "[[04-Research/03-建模算法源码库/代码验证报告]] · [[Inbox-压缩包清点索引]]",
        "",
    ]
    grouped: defaultdict[str, list[tuple[Path, str, str, bool]]] = defaultdict(list)
    for row in rows:
        relative_inside = row[0].relative_to(PYTHON_ROOT)
        chapter = relative_inside.parts[0] if len(relative_inside.parts) > 1 else "根目录"
        grouped[chapter].append(row)
    for chapter, chapter_rows in grouped.items():
        lines.extend(
            [
                f"## {chapter}",
                "",
                "| # | 原始文件 | 相对路径 | SHA-256 | Hub 来源追踪 |",
                "|---:|---|---|---|---|",
            ]
        )
        for index, (path, source_relative, digest, is_traced) in enumerate(chapter_rows, 1):
            display_path = source_relative.replace("|", "-")
            lines.append(
                f"| {index} | {wiki(path)} | `{display_path}` | `{digest}` | "
                f"{'已收录' if is_traced else '待补'} |"
            )
        lines.append("")
    PYTHON_INDEX.write_text("\n".join(lines), encoding="utf-8")
    return {
        "files": len(files),
        "unique": len(hashes),
        "duplicate_files": duplicate_files,
        "traced": sum(row[3] for row in rows),
    }


def write_member_shards(inventories: list[dict[str, object]]) -> list[Path]:
    MEMBER_ROOT.mkdir(parents=True, exist_ok=True)
    generated: list[Path] = []
    shard_lines: list[str] = []
    shard_number = 0

    def flush() -> None:
        nonlocal shard_lines, shard_number
        if not shard_lines:
            return
        shard_number += 1
        path = MEMBER_ROOT / f"压缩包成员-{shard_number:03d}.md"
        header = [
            "---",
            "type: inbox-archive-member-index",
            "status: generated-reviewed",
            f"updated: {datetime.now().date().isoformat()}",
            "tags: [area/数学建模, workflow/inbox-归档, system/index]",
            "---",
            "",
            f"# 压缩包成员索引 {shard_number:03d}",
            "",
            "返回 [[Inbox-压缩包清点索引]]。以下仅为成员名称清单，未解压、未运行。",
            "",
        ]
        path.write_text("\n".join(header + shard_lines).rstrip() + "\n", encoding="utf-8")
        generated.append(path)
        shard_lines = []

    for item in inventories:
        members = item["members"]
        if not members:
            continue
        offset = 0
        while offset < len(members):
            header_size = 5
            capacity = MAX_MEMBER_LINES_PER_SHARD - len(shard_lines) - header_size
            if capacity < 100:
                flush()
                continue
            chunk = members[offset:offset + capacity]
            first = offset + 1
            last = offset + len(chunk)
            shard_lines.extend(
                [
                    f"## {item['relative_path']} · 成员 {first}-{last}/{len(members)}",
                    "",
                    f"原件：{wiki(item['path'])}",
                    "",
                ]
            )
            shard_lines.extend(f"- `{member.replace('`', 'ˋ')}`" for member in chunk)
            shard_lines.append("")
            offset = last
            if len(shard_lines) >= MAX_MEMBER_LINES_PER_SHARD:
                flush()
    flush()
    return generated


def build_archive_index() -> dict[str, int]:
    paths = sorted(
        path for path in DOWNLOADED.rglob("*")
        if path.is_file() and path.suffix.lower() in ARCHIVE_EXTENSIONS
    )
    inventories: list[dict[str, object]] = []
    hash_groups: defaultdict[str, list[Path]] = defaultdict(list)
    for index, path in enumerate(paths, 1):
        digest = sha256(path)
        hash_groups[digest].append(path)
        status, members, detail = list_archive(path)
        nested, risky, traversal = member_risks(members)
        relative_path = path.relative_to(DOWNLOADED).as_posix()
        sibling = path.with_suffix("")
        inventories.append(
            {
                "index": index,
                "path": path,
                "relative_path": relative_path,
                "extension": path.suffix.lower(),
                "bytes": path.stat().st_size,
                "sha256": digest,
                "status": status,
                "detail": detail,
                "members": members,
                "member_count": len(members),
                "nested_archives": nested,
                "risky_members": risky,
                "traversal_members": traversal,
                "same_name_directory": sibling.is_dir(),
            }
        )

    duplicate_ids: dict[str, str] = {}
    duplicate_number = 0
    for digest, group in hash_groups.items():
        if len(group) < 2:
            continue
        duplicate_number += 1
        duplicate_ids[digest] = f"ARCH-DUP-{duplicate_number:03d}"

    member_shards = write_member_shards(inventories)
    fieldnames = [
        "relative_path", "extension", "bytes", "sha256", "duplicate_group",
        "status", "member_count", "nested_archives", "risky_members",
        "traversal_members", "same_name_directory", "detail",
    ]
    with ARCHIVE_CSV.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for item in inventories:
            writer.writerow({
                key: duplicate_ids.get(str(item["sha256"]), "") if key == "duplicate_group" else item[key]
                for key in fieldnames
            })

    ext_counts = Counter(str(item["extension"]) for item in inventories)
    status_counts = Counter(str(item["status"]) for item in inventories)
    lines = [
        "---",
        "type: inbox-index",
        "status: generated-reviewed",
        f"updated: {datetime.now().date().isoformat()}",
        "tags: [area/数学建模, workflow/inbox-归档, system/index]",
        "---",
        "",
        "# Inbox 压缩包清点索引",
        "",
        "> [!summary] 清点边界",
        f"> 已清点 **{len(inventories)}** 个压缩包（RAR {ext_counts['.rar']}、ZIP {ext_counts['.zip']}）；"
        f"总计 **{sum(int(item['bytes']) for item in inventories) / 1024**3:.2f} GiB**。",
        f"> 可列出成员的压缩包 **{status_counts['成员已索引']}** 个，成员名已写入 "
        f"**{len(member_shards)}** 个 Markdown 分片，因此可被 Obsidian 全文检索。",
        f"> 发现 **{len(duplicate_ids)}** 个精确重复压缩包组、"
        f"**{sum(int(item['risky_members']) for item in inventories)}** 个可执行/脚本类风险成员；"
        f"路径穿越成员 **{sum(int(item['traversal_members']) for item in inventories)}** 个。",
        "> 唯一未能列出成员的是伪装成 `.zip` 的快压 KZ 专有格式文件："
        "`6.数学建模模型算法大全/蒙特卡罗算法/蒙特卡罗模拟.zip`。",
        "> 本轮只读取目录和哈希，不解压、不运行、不删除。`同名目录存在` 只是冗余候选，不等于可以删除。",
        "",
        "关联：[[数学建模Python相关-源码索引]] · [[04-Research/03-建模算法源码库/代码资料索引]]",
        "",
        "完整机器清单：[[Inbox-压缩包清单.csv]]",
        "",
        "## 成员索引分片",
        "",
    ]
    lines.extend(f"- {wiki(path)}" for path in member_shards)
    lines.extend(
        [
            "",
            "## 压缩包总表",
            "",
            "| # | 原件 | 类型 | 大小 MiB | SHA-256 | 重复组 | 成员 | 嵌套包 | 风险成员 | 同名目录 | 状态 |",
            "|---:|---|---|---:|---|---|---:|---:|---:|---|---|",
        ]
    )
    for item in inventories:
        digest = str(item["sha256"])
        lines.append(
            f"| {item['index']} | {wiki(item['path'])} | `{item['extension']}` | "
            f"{int(item['bytes']) / 1024**2:.2f} | `{digest}` | {duplicate_ids.get(digest, '')} | "
            f"{item['member_count']} | {item['nested_archives']} | {item['risky_members']} | "
            f"{'是' if item['same_name_directory'] else '否'} | {item['status']} |"
        )
    lines.extend(
        [
            "",
            "## 删除决策门槛",
            "",
            "只有同时满足以下条件才可另行申请删除：SHA-256 精确重复、成员清单一致、没有唯一文件、"
            "配套相对路径已验证、用户明确批准。本索引本身不授权删除。",
            "",
        ]
    )
    ARCHIVE_INDEX.write_text("\n".join(lines), encoding="utf-8")
    return {
        "archives": len(inventories),
        "listed": status_counts["成员已索引"],
        "members": sum(int(item["member_count"]) for item in inventories),
        "duplicate_groups": len(duplicate_ids),
        "member_shards": len(member_shards),
        "risk_members": sum(int(item["risky_members"]) for item in inventories),
    }


def main() -> None:
    CLEANED.mkdir(parents=True, exist_ok=True)
    python_stats = build_python_index()
    archive_stats = build_archive_index()
    print(f"python={python_stats}")
    print(f"archives={archive_stats}")


if __name__ == "__main__":
    main()
