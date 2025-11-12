from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml.ns import qn
import re

DOCS_DIR = Path("docs")
MEDIA_DIR = DOCS_DIR / "media"

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def sanitize(s: str) -> str:
    s = re.sub(r"\s+", "_", s.strip())
    s = re.sub(r"[^A-Za-z0-9_\-\.]", "", s)
    return s or "untitled"

def get_notes(slide) -> str:
    try:
        txt = slide.notes_slide.notes_text
        return txt.strip() if txt and txt.strip() else ""
    except Exception:
        return ""

def iter_text(shape):
    if hasattr(shape, "has_text_frame") and shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            level = getattr(para, "level", 0)
            text = "".join(run.text for run in para.runs) or para.text or ""
            if text.strip():
                yield level, text.strip()

def get_alt_text(shape) -> str:
    try:
        # cNvPr berisi 'descr' (alt text) dan 'name'
        cNvPr = shape._element.xpath(".//p:cNvPr")[0]
        alt = cNvPr.get("descr") or ""
        name = cNvPr.get("name") or ""
        return (alt or name).strip()
    except Exception:
        return ""

def export_picture_from_shape(slide, shape, out_path: Path) -> Path | None:
    """
    Ambil file gambar yang direferensikan oleh shape PICTURE di slide ini,
    tulis ke out_path, dan kembalikan path file. Menggunakan relationship per slide (akurasi tinggi).
    """
    try:
        blip = shape._element.blipFill.blip  # <a:blip r:embed="rIdX">
        rel_id = blip.get(qn("r:embed"))
        if not rel_id:
            return None
        img_part = slide.part.related_part(rel_id)  # ImagePart
        ext = Path(img_part.filename).suffix or ".png"
        ensure_dir(out_path.parent)
        out_file = out_path.with_suffix(ext.lower())
        # tulis blob gambar
        out_file.write_bytes(img_part.blob)
        return out_file
    except Exception:
        return None

def process_pptx(pptx_path: Path):
    prs = Presentation(str(pptx_path))
    stem = sanitize(pptx_path.stem)
    md_path = DOCS_DIR / f"{stem}.md"
    ensure_dir(DOCS_DIR)
    ensure_dir(MEDIA_DIR)

    lines = [f"# {pptx_path.name}", ""]

    for i, slide in enumerate(prs.slides, start=1):
        lines.append(f"## Slide {i}")

        # 1) Teks
        any_text = False
        for sh in slide.shapes:
            for level, txt in iter_text(sh):
                any_text = True
                indent = "  " * min(level, 4)
                lines.append(f"{indent}- {txt}")
        if not any_text:
            lines.append("_(tidak ada teks terdeteksi di slide ini)_")

        # 2) Notes
        notes = get_notes(slide)
        if notes:
            lines.append("")
            lines.append("**Catatan (Notes):**")
            lines.append(f"> {notes}")

        # 3) Gambar per slide
        picture_count = 0
        alt_texts = []
        for idx, sh in enumerate(slide.shapes, start=1):
            if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
                picture_count += 1
                alt_texts.append(get_alt_text(sh))
                # nama file media per slide, per index
                base_name = sanitize(f"{stem}_slide{i}_img{picture_count}")
                out_path = MEDIA_DIR / base_name
                img_file = export_picture_from_shape(slide, sh, out_path)
                if img_file:
                    # sisipkan referensi gambar ke Markdown
                    alt_label = alt_texts[-1] or f"Gambar {picture_count}"
                    rel_path = img_file.relative_to(DOCS_DIR)
                    lines.append("")
                    lines.append(f"![{alt_label}]({rel_path.as_posix()})")

        # 4) Ringkasan shape non-teks + alt text
        if picture_count:
            lines.append("")
            lines.append(f"**Ringkasan shape non-teks:** picture:{picture_count}")
            if any(alt_texts):
                lines.append("")
                lines.append("**Alt text / nama gambar terdeteksi:**")
                for n, alt in enumerate(alt_texts, start=1):
                    lines.append(f"- Gambar {n}: {alt or '(alt text kosong)'}")
        else:
            # bisa tambahkan ringkasan lain (table/chart) jika diinginkan
            pass

        # Rekomendasi
        if picture_count and not notes and not any_text:
            lines.append("")
            lines.append("_Rekomendasi: Tambahkan alt text atau Notes untuk memperjelas isi gambar._")

        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {md_path}")

def main():
    for pptx in Path(".").glob("*.pptx"):
        process_pptx(pptx)

if __name__ == "__main__":
    main()
