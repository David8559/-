from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

import pymupdf


VAULT = Path(r"C:\Users\17888\Documents\0.数学建模知识库\0.数学建模")
PROJECT = VAULT / "06-Projects" / "优秀论文批量拆解"
MANIFEST = PROJECT / "Data" / "manifest.json"
OUT = PROJECT / "Data" / "ManualReview"
CACHE = PROJECT / "Data" / "Extracted"

TARGET_NOTES = {
    "G-2015-C-国一-“月上柳梢头，人约黄昏后”数学模型的建立.md",
    "G-2019-B-奖项待核-同心鼓“同心协力”策略探究.md",
    "G-2022-B-奖项待核-基于计算几何与带阈值启发式搜索的无人机无源定位模型.md",
    "G-2024-D-奖项待核-反潜航空深弹命中概率的优化问题.md",
    "G-2010-A-奖项待核-储油罐的变位识别与罐容表标定-2010-A-6d6d6.md",
    "G-2010-A-奖项待核-储油罐的变位识别与罐容表标定-2010-A-a730d.md",
    "G-2010-A-奖项待核-储油罐的变位识别与罐容表标定-2010-A-f0485.md",
    "G-2010-A-奖项待核-储油罐的变位识别与罐容表标定.md",
    "G-2010-A-奖项待核-基于数学建模的储油罐变形监测研究.md",
    "G-2016-C-国一-电池剩余放电时间预测-2016-C-5dab8.md",
    "G-2018-C-奖项待核-基于RFMS指标的大型百货商场会员画像数据挖掘.md",
    "G-2018-D-奖项待核-汽车总装线配置方案.md",
    "G-2020-D-奖项待核-接触式轮廓仪校准问题.md",
    "G-2021-D-奖项待核-连铸切割的在线优化-D034.md",
    "G-2022-D-奖项待核-气象报文信息卫星通信传输.md",
    "G-2025-B-奖项待核-碳化硅外延层厚度的双光束和多光束干涉法测量研究.md",
    "G-2012-A-国一-葡萄酒的评价.md",
}


def normalize(text: str) -> str:
    text = text.replace("\u3000", " ").replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def load_targets() -> list[dict]:
    records = json.loads(MANIFEST.read_text(encoding="utf-8"))
    selected = [r for r in records if Path(r["note"]).name in TARGET_NOTES]
    found = {Path(r["note"]).name for r in selected}
    missing = sorted(TARGET_NOTES - found)
    if missing:
        raise RuntimeError(f"Manifest missing target notes: {missing}")
    return sorted(selected, key=lambda r: Path(r["note"]).name)


def extract_record(record: dict, force: bool = False) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    dest = OUT / f"{record['sha256']}.json"
    if dest.exists() and not force:
        return dest

    source = Path(record["source"])
    doc = pymupdf.open(source)
    native = [normalize(page.get_text("text")) for page in doc]
    native_chars = sum(map(len, native))
    use_native = native_chars >= max(1200, len(doc) * 120)
    pages: list[dict] = []

    if use_native:
        pages = [{"page": i + 1, "text": text, "method": "embedded-text"} for i, text in enumerate(native)]
    else:
        os.environ["OMP_NUM_THREADS"] = "1"
        import numpy as np
        from rapidocr_onnxruntime import RapidOCR

        ocr = RapidOCR()
        for i, page in enumerate(doc):
            pix = page.get_pixmap(matrix=pymupdf.Matrix(1.55, 1.55), alpha=False)
            image = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
            result, _ = ocr(image)
            text = normalize("\n".join(item[1] for item in (result or [])))
            pages.append({"page": i + 1, "text": text, "method": "full-page-ocr"})
            print(f"[{Path(record['note']).name}] {i + 1}/{len(doc)}", flush=True)

    payload = {
        "note": record["note"],
        "title": record["title"],
        "source": record["source"],
        "sha256": record["sha256"],
        "pages_total": len(doc),
        "extraction_method": "embedded-text" if use_native else "full-page-ocr",
        "pages": pages,
    }
    dest.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return dest


def print_summary(record: dict) -> None:
    reviewed = OUT / f"{record['sha256']}.json"
    cached = CACHE / f"{record['sha256']}.json"
    source = reviewed if reviewed.exists() else cached
    payload = json.loads(source.read_text(encoding="utf-8"))
    print("\n" + "=" * 88)
    print(Path(record["note"]).name)
    print(record["source"])
    print(f"evidence-cache={source.name}")
    for page in payload["pages"][:3]:
        text = page["text"]
        print(f"\n--- PDF 第 {page['page']} 页 ---")
        print(text[:4500])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--match", default="")
    parser.add_argument("--sha", default="")
    args = parser.parse_args()
    records = [
        r for r in load_targets()
        if args.match in Path(r["note"]).name and (not args.sha or r["sha256"].startswith(args.sha))
    ]
    if args.summary:
        for record in records:
            print_summary(record)
        return
    for i, record in enumerate(records, 1):
        print(f"[{i}/{len(TARGET_NOTES)}] {Path(record['note']).name}", flush=True)
        print(extract_record(record, force=args.force), flush=True)


if __name__ == "__main__":
    main()
