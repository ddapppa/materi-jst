from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import re, shutil
import zipfile

MEDIA_EXPORT_DIR = Path("docs/media")

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def sanitize_stem(stem: str) -> str:
    s = re.sub(r"\s+", "_", stem)
    s = re.sub(r"[^A-Za-z0-9_\-]", "", s)
    return s or "slides"

def get_alt_text(shape):
    try:
        # cNvPr node berisi atribut 'descr' (alt text) & 'name'
        cNvPr = shape._element.xpath(".//p:cNvPr")[0]
        alt = cNvPr.get("descr") or ""
        name = cNvPr.get("name") or ""
        return alt.strip() or name.strip()
    except Exception:
        return ""

def extract_media(pptx_path: Path):
    ensure_dir(MEDIA_EXPORT_DIR)
    # Langsung buka sebagai zip:
    with zipfile.ZipFile(pptx_path, 'r') as z:
        for f in z.namelist():
            if f.startswith("ppt/media/"):
                target = MEDIA_EXPORT_DIR / Path(f).name
                if not target.exists():
                    z.extract(f, MEDIA_EXPORT_DIR)
    return sorted([p.name for p in MEDIA_EXPORT_DIR.iterdir() if p.is_file()])

def iter_text(shape):
    if hasattr(shape, "has_text_frame") and shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            level = getattr(para, "level", 0)
            text = "".join(run.text for run in para.runs) or para.text or ""
            if text.strip():
                yield level, text.strip()

def slide_summary(slide):
    counts = {"picture":0,"table":0,"chart":0,"group":0,"other":0}
    pictures = []
    for sh in slide.shapes:
        st = sh.shape_type
        if st == MSO_SHAPE_TYPE.PICTURE:
            counts["picture"] += 1
            pictures.append(get_alt_text(sh))
        elif st == MSO_SHAPE_TYPE.TABLE:
            counts["table"] += 1
        elif st == MSO_SHAPE_TYPE.CHART:
            counts["chart"] += 1
        elif st == MSO_SHAPE_TYPE.GROUP:
            counts["group"] += 1
        else:
            if not (hasattr(sh,"has_text_frame") and sh.has_text_frame):
                counts["other"] += 1
    parts = [f"{k}:{v}" for k,v in counts.items() if v]
    return ", ".join(parts) if parts else "tidak ada shape non-teks", pictures

def get_notes(slide):
    try:
        n = slide.notes_slide.notes_text
        return n.strip() if n and n.strip() else ""
    except Exception:
        return ""

def process(pptx_path: Path):
    prs = Presentation(str(pptx_path))
    stem = sanitize_stem(pptx_path.stem)
    out = Path("docs") / f"{stem}.md"
    ensure_dir(out.parent)

    media_files = extract_media(pptx_path)

    lines = [f"# {pptx_path.name}", "", f"**Media diekstrak:** {len(media_files)} file"]
    if media_files:
        lines.append("")
        lines.append("Daftar media:")
        for m in media_files:
            lines.append(f"- {m}")
        lines.append("")

    for i, slide in enumerate(prs.slides, start=1):
        lines.append(f"## Slide {i}")
        any_text = False
        for shape in slide.shapes:
            for level, txt in iter_text(shape):
                any_text = True
                indent = "  " * min(level,4)
                lines.append(f"{indent}- {txt}")
        if not any_text:
            lines.append("_(tidak ada teks terdeteksi di slide ini)_")

        notes = get_notes(slide)
        if notes:
            lines.append("")
            lines.append("**Catatan (Notes):**")
            lines.append(f"> {notes}")

        summary, pictures_alt = slide_summary(slide)
        lines.append("")
        lines.append(f"**Ringkasan shape non-teks:** {summary}")

        if pictures_alt:
            lines.append("")
            lines.append("**Alt text / nama gambar terdeteksi:**")
            for idx, alt in enumerate(pictures_alt, start=1):
                display = alt if alt else "(alt text kosong)"
                lines.append(f"- Gambar {idx}: {display}")

        # Sisipkan referensi gambar sederhana jika 1 gambar dan file masih tersedia
        if "picture:" in summary and media_files:
            # Heuristik: ambil gambar pertama (atau sesuai indeks total)
            # (Versi dasar; pemetaan akurat antar slide butuh parsing relationship per slide)
            guessed_img = media_files[min(i-1, len(media_files)-1)]
            lines.append("")
            lines.append(f"![Gambar perkiraan slide {i}](media/{guessed_img})")

        if "picture:" in summary and not notes and not any_text:
            lines.append("")
            lines.append("_Rekomendasi: Tambahkan alt text atau Notes untuk memperjelas isi gambar._")

        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")

def main():
    for pptx in Path(".").glob("*.pptx"):
        process(pptx)

if __name__ == "__main__":
    main()
