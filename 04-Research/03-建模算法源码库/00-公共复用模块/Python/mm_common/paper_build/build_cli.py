"""国赛论文 docx 生成命令行入口。

示例（以 2025 复现稿为输入，输出到独立目录）：
    python -m mm_common.paper_build.build_cli \
        --paper-md "06-Projects/2025国赛A题-烟幕干扰弹投放策略/Paper/参赛论文-赛后复现稿.md" \
        --out "06-Projects/2025国赛A题-烟幕干扰弹投放策略/Paper/validation-2026-pipeline" \
        --title "参赛论文" --problem-id A --year 2025
"""

from __future__ import annotations

import argparse
from pathlib import Path

from .build_core import build_from_markdown


def main():
    parser = argparse.ArgumentParser(description="按 2026 国赛电子稿口径生成论文 docx")
    parser.add_argument("--paper-md", type=Path, required=True, help="论文 Markdown 路径（必填）")
    parser.add_argument("--out", type=Path, required=True, help="输出目录（或 .docx 文件路径）")
    parser.add_argument("--title", default=None, help="docx core 标题（默认匿名通用标题）")
    parser.add_argument("--problem-id", default="", help="赛题号，如 A（写入 subject 元数据）")
    parser.add_argument("--year", default="", help="赛年年份，如 2026（写入 subject 元数据）")
    parser.add_argument("--ai-detail-md", type=Path, default=None, help="可选：AI 使用详情 Markdown，一并生成")
    parser.add_argument("--no-images", action="store_true", help="不嵌入图片（调试构建）")
    parser.add_argument("--image-limit", type=int, default=None, help="只嵌入前 N 张图（调试构建）")
    parser.add_argument("--margin", type=float, default=None, help="覆盖页边距（cm）")
    args = parser.parse_args()

    out = args.out
    out_path = out if out.suffix.lower() == ".docx" else out / "参赛论文.docx"
    subject = "全国大学生数学建模竞赛"
    if args.year:
        subject += f" {args.year} 年"
    if args.problem_id:
        subject += f" {args.problem_id} 题赛后复现"

    built = [build_from_markdown(
        args.paper_md,
        out_path,
        ai_detail=False,
        include_images=not args.no_images,
        image_limit=args.image_limit,
        margin_cm=args.margin,
        title=args.title,
        subject=subject,
    )]
    if args.ai_detail_md is not None:
        ai_out = out if out.suffix.lower() == ".docx" else out / "AI工具使用详情.docx"
        built.append(build_from_markdown(
            args.ai_detail_md,
            ai_out,
            ai_detail=True,
            include_images=not args.no_images,
            margin_cm=args.margin,
            title="AI 工具使用详情",
            subject=subject,
        ))
    for path in built:
        print(path)


if __name__ == "__main__":
    main()
