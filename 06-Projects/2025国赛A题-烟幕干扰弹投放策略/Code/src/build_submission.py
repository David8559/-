"""Build the Stage G competition paper and AI-usage detail document.

The source of truth remains the UTF-8 Markdown files in Paper/.  This builder
implements the official constraints that matter for the 2025 electronic paper:
A4, margins >= 2.5 cm, summary on page 1, page numbers from page 1, no cover,
no number/commitment pages, and no table of contents.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_ALIGN_VERTICAL, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
PAPER_MD = ROOT / "Paper" / "参赛论文-赛后复现稿.md"
AI_MD = ROOT / "Paper" / "AI工具使用详情.md"
OUT_DIR = ROOT / "Paper" / "submission"


def set_run_font(run, cn: str = "宋体", latin: str = "Times New Roman", size=10.5, bold=None):
    run.font.name = latin
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), cn)
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold


def set_cell_shading(cell, fill: str):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=60, start=80, bottom=60, end=80):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for edge, val in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{edge}"))
        if node is None:
            node = OxmlElement(f"w:{edge}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")


def set_repeat_table_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_cant_split(row):
    tr_pr = row._tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit")
    tr_pr.append(cant)


def add_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run()
    fld_char1 = OxmlElement("w:fldChar")
    fld_char1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld_char2 = OxmlElement("w:fldChar")
    fld_char2.set(qn("w:fldCharType"), "end")
    run._r.extend([fld_char1, instr, fld_char2])
    set_run_font(run, size=9)


def configure_document(doc: Document):
    section = doc.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.header_distance = Cm(1.25)
    section.footer_distance = Cm(1.25)
    section.different_first_page_header_footer = False
    add_page_number(section.footer.paragraphs[0])

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")
    normal.font.size = Pt(10.5)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    normal.paragraph_format.first_line_indent = Cm(0.74)
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    normal.paragraph_format.line_spacing = 1.18
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.widow_control = True

    for name, cn, size, before, after in (
        ("Heading 1", "黑体", 14, 10, 5),
        ("Heading 2", "黑体", 12, 8, 4),
        ("Heading 3", "黑体", 10.5, 6, 3),
    ):
        style = doc.styles[name]
        style.font.name = "Times New Roman"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), cn)
        style.font.size = Pt(size)
        style.font.bold = True
        pf = style.paragraph_format
        pf.keep_with_next = True
        pf.keep_together = True
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.first_line_indent = Cm(0)

    for style_name in ("List Bullet", "List Number"):
        style = doc.styles[style_name]
        style.font.name = "Times New Roman"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")
        style.font.size = Pt(10.5)
        style.paragraph_format.left_indent = Cm(0.74)
        style.paragraph_format.first_line_indent = Cm(-0.37)
        style.paragraph_format.space_after = Pt(0)
        style.paragraph_format.line_spacing = 1.15

    if "Caption CN" not in [s.name for s in doc.styles]:
        cap = doc.styles.add_style("Caption CN", WD_STYLE_TYPE.PARAGRAPH)
        cap.font.name = "Times New Roman"
        cap._element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")
        cap.font.size = Pt(9)
        cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.paragraph_format.keep_with_next = True
        cap.paragraph_format.space_before = Pt(2)
        cap.paragraph_format.space_after = Pt(5)
        cap.paragraph_format.first_line_indent = Cm(0)

    if "Equation CN" not in [s.name for s in doc.styles]:
        eq = doc.styles.add_style("Equation CN", WD_STYLE_TYPE.PARAGRAPH)
        eq.font.name = "Cambria Math"
        eq._element.rPr.rFonts.set(qn("w:eastAsia"), "Cambria Math")
        eq.font.size = Pt(10.5)
        eq.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        eq.paragraph_format.keep_together = True
        eq.paragraph_format.space_before = Pt(3)
        eq.paragraph_format.space_after = Pt(3)
        eq.paragraph_format.first_line_indent = Cm(0)


INLINE_PATTERN = re.compile(r"(\*\*.*?\*\*|`.*?`|\$.*?\$|\[[^\]]+\]\([^)]+\))")


def add_inline(paragraph, text: str, base_size=10.5):
    pos = 0
    for match in INLINE_PATTERN.finditer(text):
        if match.start() > pos:
            set_run_font(paragraph.add_run(text[pos : match.start()]), size=base_size)
        token = match.group(0)
        if token.startswith("**"):
            run = paragraph.add_run(token[2:-2])
            set_run_font(run, size=base_size, bold=True)
        elif token.startswith("`"):
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, cn="等线", latin="Consolas", size=max(base_size - 1, 8.5))
        elif token.startswith("$"):
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, cn="Cambria Math", latin="Cambria Math", size=base_size)
        else:
            label, url = re.match(r"\[([^\]]+)\]\(([^)]+)\)", token).groups()
            run = paragraph.add_run(f"{label}（{url}）")
            set_run_font(run, size=base_size)
            run.font.color.rgb = RGBColor(31, 78, 121)
        pos = match.end()
    if pos < len(text):
        set_run_font(paragraph.add_run(text[pos:]), size=base_size)


def clean_markdown_text(text: str) -> str:
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    return text.replace("\\_", "_")


def add_table(doc: Document, rows: list[list[str]]):
    if not rows:
        return
    cols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=cols)
    table.style = "Table Grid"
    table.alignment = 1
    table.autofit = True
    for r_idx, values in enumerate(rows):
        row = table.rows[r_idx]
        set_cant_split(row)
        if r_idx == 0:
            set_repeat_table_header(row)
        for c_idx in range(cols):
            cell = row.cells[c_idx]
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            if r_idx == 0:
                set_cell_shading(cell, "D9E2F3")
            para = cell.paragraphs[0]
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER if r_idx == 0 else (
                WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            )
            para.paragraph_format.first_line_indent = Cm(0)
            para.paragraph_format.space_after = Pt(0)
            para.paragraph_format.line_spacing = 1.0
            val = values[c_idx] if c_idx < len(values) else ""
            add_inline(para, val, base_size=8.5)
            if r_idx == 0:
                for run in para.runs:
                    run.bold = True
    after = doc.add_paragraph()
    after.paragraph_format.space_after = Pt(0)
    after.paragraph_format.line_spacing = 0.5


def normalized_image_path(image_path: Path) -> Path:
    """Flatten alpha and cap raster dimensions for stable Word 2016 import."""
    digest = hashlib.sha256(
        f"{image_path.resolve()}:{image_path.stat().st_mtime_ns}".encode("utf-8")
    ).hexdigest()[:16]
    target_dir = Path(tempfile.gettempdir()) / "codex-stage-g-docx-images"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{image_path.stem}-{digest}.jpg"
    if not target.exists():
        with Image.open(image_path) as image:
            image = image.convert("RGB")
            image.thumbnail((2400, 1800), Image.Resampling.LANCZOS)
            image.save(target, format="JPEG", quality=95, optimize=True, dpi=(300, 300))
    return target


def equation_image_path(latex: str) -> Path:
    """Render display math as a high-resolution image when OMML conversion is unavailable."""
    source = " ".join(part.strip() for part in latex.splitlines()).strip()
    source = source.replace(r"\boldsymbol ", " ")
    source = source.replace(r"\frac12", r"\frac{1}{2}")
    source = re.sub(r"\\le(?![A-Za-z])", r"\\leq", source)
    source = re.sub(r"\\ge(?![A-Za-z])", r"\\geq", source)
    source = source.replace(r"\mathsf T", r"\mathsf{T}")
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]
    target_dir = Path(tempfile.gettempdir()) / "codex-stage-g-equations"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"equation-{digest}.png"
    if not target.exists():
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig = plt.figure(figsize=(8, 0.55), dpi=300, facecolor="white")
        fig.text(
            0.5,
            0.5,
            f"${source}$",
            ha="center",
            va="center",
            fontsize=12,
            color="black",
        )
        fig.savefig(target, dpi=300, bbox_inches="tight", pad_inches=0.025, facecolor="white")
        plt.close(fig)
    return target


def add_equation(doc: Document, latex: str):
    p = doc.add_paragraph(style="Equation CN")
    p.paragraph_format.keep_together = True
    try:
        image_path = equation_image_path(latex)
        with Image.open(image_path) as image:
            native_width_cm = image.width / 300 * 2.54
        width = Cm(min(14.6, max(3.0, native_width_cm)))
        p.add_run().add_picture(str(image_path), width=width)
    except Exception:
        # Last-resort readable fallback; never silently drop a formula.
        fallback = " ".join(part.strip() for part in latex.splitlines())
        run = p.add_run(fallback)
        set_run_font(run, cn="Cambria Math", latin="Cambria Math", size=10.5)


def add_figure(doc: Document, image_path: Path, caption: str, figure_number: int):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run()
    run.add_picture(str(normalized_image_path(image_path)), width=Cm(14.8))
    cap = doc.add_paragraph(style="Caption CN")
    add_inline(cap, f"图 {figure_number}  {caption}", base_size=9)


def parse_table(lines: list[str], start: int):
    rows = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        raw = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if not all(re.fullmatch(r":?-{3,}:?", c or "") for c in raw):
            rows.append(raw)
        i += 1
    return rows, i


def build_from_markdown(
    md_path: Path,
    out_path: Path,
    *,
    ai_detail=False,
    include_images=True,
    image_limit: int | None = None,
):
    lines = md_path.read_text(encoding="utf-8").splitlines()
    doc = Document()
    configure_document(doc)

    # Remove YAML front matter when present.
    if lines and lines[0].strip() == "---":
        try:
            end = lines.index("---", 1)
            lines = lines[end + 1 :]
        except ValueError:
            pass

    in_equation = False
    equation_lines: list[str] = []
    in_code = False
    code_lines: list[str] = []
    figure_no = 0
    first_title = True
    skip_ai_template = False
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = clean_markdown_text(raw.strip())
        if ai_detail and line.startswith("### 记录 NNN"):
            skip_ai_template = True
            i += 1
            continue
        if skip_ai_template:
            if line.startswith("## 正文与参考文献待办"):
                skip_ai_template = False
            else:
                i += 1
                continue
        if line == "<!-- PAGEBREAK -->":
            doc.add_page_break()
            i += 1
            continue
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                p = doc.add_paragraph()
                p.paragraph_format.first_line_indent = Cm(0)
                p.paragraph_format.left_indent = Cm(0.6)
                p.paragraph_format.right_indent = Cm(0.4)
                p.paragraph_format.space_before = Pt(3)
                p.paragraph_format.space_after = Pt(3)
                for idx, code_line in enumerate(code_lines):
                    if idx:
                        p.add_run().add_break()
                    run = p.add_run(code_line)
                    set_run_font(run, cn="等线", latin="Consolas", size=8)
                in_code = False
            i += 1
            continue
        if in_code:
            code_lines.append(raw)
            i += 1
            continue
        if line == "$$":
            if not in_equation:
                in_equation = True
                equation_lines = []
            else:
                add_equation(doc, "\n".join(equation_lines))
                in_equation = False
            i += 1
            continue
        if in_equation:
            equation_lines.append(raw)
            i += 1
            continue
        if not line:
            i += 1
            continue
        if line.startswith("> [!"):
            i += 1
            continue
        if line.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            p.paragraph_format.right_indent = Cm(0.4)
            p.paragraph_format.first_line_indent = Cm(0)
            add_inline(p, line.lstrip("> ").strip())
            i += 1
            continue
        if line.startswith("# "):
            title = line[2:].strip()
            if first_title:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.first_line_indent = Cm(0)
                p.paragraph_format.space_before = Pt(10)
                p.paragraph_format.space_after = Pt(12)
                p.paragraph_format.keep_with_next = True
                run = p.add_run(title)
                set_run_font(run, cn="黑体", latin="Times New Roman", size=18, bold=True)
                first_title = False
            else:
                doc.add_heading(title, level=1)
            i += 1
            continue
        if line.startswith("## "):
            doc.add_heading(line[3:].strip(), level=1)
            i += 1
            continue
        if line.startswith("### "):
            doc.add_heading(line[4:].strip(), level=2)
            i += 1
            continue
        if line.startswith("#### "):
            doc.add_heading(line[5:].strip(), level=3)
            i += 1
            continue
        image_match = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", line)
        if image_match:
            figure_no += 1
            caption, rel = image_match.groups()
            image_path = (md_path.parent / rel).resolve()
            if include_images and (image_limit is None or figure_no <= image_limit):
                add_figure(doc, image_path, caption, figure_no)
            else:
                p = doc.add_paragraph(style="Caption CN")
                add_inline(p, f"图 {figure_no}  {caption}（调试构建未嵌图）", base_size=9)
            i += 1
            continue
        if line.startswith("|"):
            rows, i = parse_table(lines, i)
            add_table(doc, rows)
            continue
        num_match = re.match(r"^(\d+)\.\s+(.*)$", line)
        if num_match:
            # Preserve the source number explicitly. Word otherwise continues
            # one automatic list across unrelated sections (for example 7–10
            # instead of restarting a later four-step algorithm at 1).
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.74)
            p.paragraph_format.first_line_indent = Cm(-0.37)
            p.paragraph_format.line_spacing = 1.15
            add_inline(p, f"{num_match.group(1)}. {num_match.group(2)}")
            i += 1
            continue
        if line.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, line[2:])
            i += 1
            continue

        p = doc.add_paragraph()
        if line.startswith("**摘要：**") or line.startswith("**关键词：**") or line.startswith("**AI 辅助声明：**"):
            p.paragraph_format.first_line_indent = Cm(0)
        if line.startswith("AI辅助标注：") or line.startswith("AI 辅助标注："):
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.left_indent = Cm(0.5)
            p.paragraph_format.right_indent = Cm(0.5)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            for run in p.runs:
                run.font.color.rgb = RGBColor(89, 89, 89)
        add_inline(p, line)
        if line.startswith("AI辅助标注：") or line.startswith("AI 辅助标注："):
            for run in p.runs:
                run.font.color.rgb = RGBColor(89, 89, 89)
                run.italic = True
                run.font.size = Pt(9)
        i += 1

    # Metadata must be anonymous for competition submission artifacts.
    props = doc.core_properties
    props.title = "烟幕干扰弹协同投放策略研究" if not ai_detail else "AI 工具使用详情"
    props.author = ""
    props.last_modified_by = ""
    props.subject = "2025 全国大学生数学建模竞赛 A 题赛后复现"
    props.keywords = ""
    props.comments = ""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=OUT_DIR)
    parser.add_argument("--no-images", action="store_true")
    parser.add_argument("--image-limit", type=int)
    args = parser.parse_args()
    out_dir = args.output_dir.resolve()
    build_from_markdown(
        PAPER_MD,
        out_dir / "参赛论文.docx",
        include_images=not args.no_images,
        image_limit=args.image_limit,
    )
    build_from_markdown(AI_MD, out_dir / "AI工具使用详情.docx", ai_detail=True)
    print(out_dir / "参赛论文.docx")
    print(out_dir / "AI工具使用详情.docx")


if __name__ == "__main__":
    main()
