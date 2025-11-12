from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import re

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def sanitize_stem(stem: str) -> str:
    s = re.sub(r"\s+", "_", stem)
    s = re.sub(r"[^A-Za-z0-9_\-]", "", s)
    return s or "slides"

def iter_shape_text(shape):
    if hasattr(shape, "has_text_frame") and shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            level = getattr(para, "level", 0)
            text = "".join(run.text for run in para.runs) or para.text or ""
            if text and text.strip():
                yield level, text.strip()
    elif shape.shape_type == MSO_SHAPE_TYPE.GROUP:
        for shp in shape.shapes:
            yield from iter_shape_text(shp)
    elif hasattr(shape, "has_table") and shape.has_table:
        table = shape.table
        for r in table.rows:
            cells = [c.text.strip() for c in r.cells]
            row_text = " | ".join(t for t in cells if t)
            if row_text:
                yield 0, row_text

def slide_text(slide):
    for shape in slide.shapes:
        yield from iter_shape_text(shape)

def extract_one(pptx_path: Path, out_dir: Path):
    prs = Presentation(str(pptx_path))
    stem = sanitize_stem(pptx_path.stem)
    out_path = out_dir / f"{stem}.md"

    lines = [f"# {pptx_path.name}", ""]
    for i, slide in enumerate(prs.slides, start=1):
        lines.append(f"## Slide {i}")
        any_text = False
        for level, text in slide_text(slide):
            any_text = True
            indent = "  " * min(level, 4)
            lines.append(f"{indent}- {text}")
        if not any_text:
            lines.append("_(tidak ada teks terdeteksi di slide ini)_")
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")

def main():
    repo_root = Path(__file__).resolve().parents[1]
    out_dir = repo_root / "docs"
    ensure_dir(out_dir)

    pptx_files = sorted(repo_root.rglob("*.pptx"))
    if not pptx_files:
        print("No PPTX files found.")
        return

    for f in pptx_files:
        if "docs" in f.parts:
            continue
        extract_one(f, out_dir)

if __name__ == "__main__":
    main()
