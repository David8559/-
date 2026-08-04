"""国赛论文 docx 生成与机器 QA（2026 电子稿口径）。

- build_core.build_from_markdown: Markdown → docx（排版常量见 constants_2026）
- build_cli: 命令行入口（--paper-md/--out/--title/--problem-id/--year/...）
- paper_qa.run_qa: 14 项机器 QA（PASS/FAIL + 证据）

用法（在 0.数学建模 vault 根目录，PYTHONPATH 指向 00-公共复用模块/Python）：
    python -m mm_common.paper_build.build_cli --paper-md <md> --out <dir>
    python -m mm_common.paper_build.paper_qa <docx> --report-json qa.json
"""

from .build_core import build_from_markdown
from .paper_qa import CHECKS, run_qa

__all__ = ["CHECKS", "build_from_markdown", "run_qa"]
__version__ = "1.0.0"
