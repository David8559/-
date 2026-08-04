"""2026 全国大学生数学建模竞赛论文排版常量（电子版口径）。

每项常量的出处见同目录 SPEC_2026.md：A=官方强制（2026 规范）、
B=项目默认样式（官方未统一规定时选用）、T=技术实现约束。

本模块为纯数据，不导入 python-docx，便于在无 Word 依赖的环境复用。
"""

from __future__ import annotations

# ---- 页面（A4，官方电子稿口径）----
PAGE_WIDTH_CM = 21.0          # A: A4 宽度
PAGE_HEIGHT_CM = 29.7         # A: A4 高度
MARGIN_CM = 2.5               # A: 页边距不少于 2.5 cm
HEADER_FOOTER_DISTANCE_CM = 1.25  # B: 页眉页脚距离
PAGE_NUMBER_FONT_SIZE_PT = 9  # B: 页脚页码字号

# ---- 正文样式（官方未统一规定，采用项目默认 B 级样式）----
FONT_CN = "宋体"              # B: 中文正文字体
FONT_LATIN = "Times New Roman"  # B: 西文正文字体
FONT_SIZE_PT = 10.5           # B: 正文字号（小五？实测 10.5pt 为项目样式）
LINE_SPACING = 1.18           # B: 行距倍数
FIRST_LINE_INDENT_CM = 0.74   # B: 首行缩进
HEADING_FONT_CN = "黑体"      # B: 标题字体
HEADING_LEVELS = (            # B: (级别, 字号, 段前, 段后)
    (1, 14, 10, 5),
    (2, 12, 8, 4),
    (3, 10.5, 6, 3),
)
TITLE_FONT_SIZE_PT = 18       # B: 论文大标题字号
TITLE_SPACE_AFTER_PT = 12     # B: 大标题后间距

# ---- 表格（项目样式 B 级）----
TABLE_HEADER_FILL = "D9E2F3"  # B: 表头底色
TABLE_FONT_SIZE_PT = 8.5      # B: 表内字号
CELL_MARGIN_DXA = (60, 80, 60, 80)  # B: 单元格内边距 (top, start, bottom, end)

# ---- 公式（技术实现约束 T 级）----
EQUATION_TAB_CM = 15.4        # T: 编号右对齐制表位
EQUATION_WIDTH_MAX_CM = 13.8  # T: 公式图最大宽度
EQUATION_WIDTH_MIN_CM = 3.0   # T: 公式图最小宽度
EQUATION_FONT_SIZE_PT = 10.5  # B: 公式与编号字号

# ---- 图片（T: Word 2016 稳定导入）----
IMAGE_MAX_PX = (2400, 1800)   # T: 图片像素上限（长≤2400，宽≤1800）
IMAGE_DPI = 300               # T: 输出分辨率
IMAGE_QUALITY = 95            # T: JPEG 质量
FIGURE_WIDTH_CM = 14.8        # B: 正文图宽
CAPTION_FONT_SIZE_PT = 9      # B: 图题字号

# ---- AI 标注（A: 官方要求如实标注；样式 B 级）----
AI_ANNOTATION_RGB = (89, 89, 89)  # B: 灰斜体
AI_ANNOTATION_SIZE_PT = 9     # B: 标注字号

# ---- 交付约束（官方）----
MAX_FILE_SIZE_MB = 20         # A: 电子稿/支撑材料上限
MAX_BODY_PAGES = 30           # A: 正文不超过 30 页（人工检查项，见 paper_qa）

# ---- 行内 LaTeX → Unicode 映射（T: 正文基线可读性）----
INLINE_LATEX_MAP = {
    r"\ldots": "…",
    r"\lambda": "λ",
    r"\theta": "θ",
    r"\Omega": "Ω",
    r"\phi": "φ",
    r"\tau": "τ",
    r"\mu": "μ",
    r"\pi": "π",
    r"\Delta": "Δ",
    r"\forall": "∀",
    r"\exists": "∃",
    r"\approx": "≈",
    r"\times": "×",
    r"\cap": "∩",
    r"\cup": "∪",
    r"\subseteq": "⊆",
    r"\leq": "≤",
    r"\geq": "≥",
    r"\le": "≤",
    r"\ge": "≥",
    r"\in": "∈",
    r"\min": "min",
    r"\max": "max",
    r"\sum": "Σ",
    r"\|": "‖",
    r"\{": "{",
    r"\}": "}",
    r"\,": " ",
}
