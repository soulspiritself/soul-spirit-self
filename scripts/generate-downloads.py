#!/usr/bin/env python3
"""
Soul Spirit Self - Downloadable file generator

Reads a text MD file (or all text MDs), produces .txt/.pdf/.epub versions
in public/downloads/<slug>.{txt,pdf,epub}. Computes word count and
reading time and prints them so they can be added to frontmatter.

Setup:
  brew install pandoc
  pip install --break-system-packages markdown weasyprint pyyaml

Usage:
  python scripts/generate-downloads.py mandukya-karika
  python scripts/generate-downloads.py --all
  python scripts/generate-downloads.py --source-md path/to/full-text.md mandukya-karika

Notes:
  - The "preview" version of the MD on the web page is not the source for
    the downloadables. Pass --source-md if the full text lives elsewhere.
  - If --source-md is omitted, the script reads the body of the text MD
    file as the source content.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_ROOT / "src" / "content" / "texts"
DOWNLOADS_DIR = PROJECT_ROOT / "public" / "downloads"
DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)


def parse_md(md_path: Path):
    raw = md_path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.DOTALL)
    if not m:
        raise ValueError(f"No frontmatter in {md_path}")
    fm = yaml.safe_load(m.group(1))
    body = m.group(2).strip()
    return fm, body


def word_count(text: str) -> int:
    # Strip markdown headings/syntax for the count
    plain = re.sub(r"#+\s*", "", text)
    plain = re.sub(r"\*+", "", plain)
    plain = re.sub(r"`[^`]*`", "", plain)
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain)
    return len(re.findall(r"\b[\w'-]+\b", plain))


def reading_time(words: int, wpm: int = 220) -> int:
    return max(1, round(words / wpm))


# ── Output formats ─────────────────────────────────────────────

def write_txt(slug: str, fm: dict, body: str) -> Path:
    out = DOWNLOADS_DIR / f"{slug}.txt"
    lines = []
    lines.append(fm.get("title", slug).upper())
    if fm.get("subtitle"):
        lines.append("")
        lines.append(fm["subtitle"])
    lines.append("")
    if fm.get("translator"):
        attr = f"Translated by {fm['translator']}"
        if fm.get("translationYear"):
            attr += f" ({fm['translationYear']})"
        lines.append(attr)
    if fm.get("sourcePlatform"):
        lines.append(f"Source: {fm.get('sourcePlatform','')} — {fm.get('sourceUrl','')}")
    if fm.get("licenceNote"):
        lines.append("")
        lines.append(fm["licenceNote"])
    lines.append("")
    lines.append("=" * 70)
    lines.append("")

    # Convert markdown headings to plain headings
    plain_body = re.sub(r"^#\s+(.+)$", lambda m: "\n" + m.group(1).upper() + "\n" + "-" * len(m.group(1)), body, flags=re.MULTILINE)
    plain_body = re.sub(r"^##\s+(.+)$", r"[\1]", plain_body, flags=re.MULTILINE)
    plain_body = re.sub(r"^###\s+(.+)$", r"  \1", plain_body, flags=re.MULTILINE)
    # Strip markdown emphasis
    plain_body = re.sub(r"\*+([^*]+)\*+", r"\1", plain_body)
    plain_body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain_body)
    lines.append(plain_body)

    out.write_text("\n".join(lines))
    return out


def build_html(fm: dict, body_md: str) -> str:
    import markdown
    body_html = markdown.markdown(body_md, extensions=["extra"])
    title = fm.get("title", "")
    subtitle = fm.get("subtitle", "")
    translator = fm.get("translator", "")
    year = fm.get("translationYear", "")
    licence_note = fm.get("licenceNote", "")
    source_platform = fm.get("sourcePlatform", "")
    source_url = fm.get("sourceUrl", "")

    css = """
    @page { size: A4; margin: 22mm 20mm 22mm 20mm;
            @bottom-center { content: counter(page); font-family: 'Inter', sans-serif; font-size: 9pt; color: #777; }
    }
    body { font-family: 'Cormorant Garamond', 'Georgia', serif; font-size: 11.5pt; line-height: 1.55; color: #1a2030; }
    .title-page { page: title; text-align: center; padding: 40mm 0; page-break-after: always; }
    .title-page h1 { font-size: 36pt; font-weight: 400; letter-spacing: -0.01em; margin: 0 0 8mm 0; color: #1a4a65; }
    .title-page .subtitle { font-style: italic; font-size: 14pt; color: #555; margin-bottom: 24mm; }
    .title-page .accent { width: 40mm; border-top: 1pt solid #c9a96e; margin: 12mm auto; }
    .title-page .attribution { font-family: 'Inter', sans-serif; font-size: 9.5pt; line-height: 1.7; color: #444; max-width: 110mm; margin: 0 auto; }
    .title-page .attribution em { color: #c9a96e; font-style: normal; letter-spacing: 0.1em; text-transform: uppercase; font-size: 8pt; }
    h1 { font-size: 22pt; font-weight: 400; color: #1a4a65; margin: 30pt 0 12pt 0; page-break-before: always; page-break-after: avoid; }
    h1:first-of-type { page-break-before: auto; }
    h2 { font-size: 12pt; font-weight: 500; color: #c9a96e; font-family: 'Inter', sans-serif; letter-spacing: 0.1em; text-transform: uppercase; margin: 18pt 0 6pt 0; page-break-after: avoid; }
    p { margin: 0 0 8pt 0; text-align: justify; orphans: 3; widows: 3; }
    em { color: #555; }
    a { color: #1a4a65; text-decoration: none; }
    """

    attribution_lines = []
    if translator:
        attribution_lines.append(f"<em>Translation</em><br>{translator}{(' &middot; ' + year) if year else ''}")
    if source_platform and source_url:
        attribution_lines.append(f"<em>Source</em><br><a href=\"{source_url}\">{source_platform}</a>")
    if licence_note:
        attribution_lines.append(f"<em>Licence</em><br>{licence_note}")

    attribution = "<br><br>".join(attribution_lines)

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
</head><body>
<section class="title-page">
  <h1>{title}</h1>
  {f'<div class="subtitle">{subtitle}</div>' if subtitle else ''}
  <div class="accent"></div>
  <div class="attribution">{attribution}</div>
  <div class="accent"></div>
  <div class="attribution" style="margin-top: 28mm; font-size: 8pt; color: #888;">soulspiritself.com</div>
</section>
{body_html}
</body></html>"""
    return html


def write_pdf(slug: str, fm: dict, body: str) -> Path:
    from weasyprint import HTML
    out = DOWNLOADS_DIR / f"{slug}.pdf"
    html = build_html(fm, body)
    HTML(string=html).write_pdf(out)
    return out


def write_epub(slug: str, fm: dict, body: str) -> Path:
    out = DOWNLOADS_DIR / f"{slug}.epub"
    title = fm.get("title", slug)
    subtitle = fm.get("subtitle", "")
    translator = fm.get("translator", "Anonymous")
    # Compose the markdown source for pandoc
    md = f"""---
title: "{title}"
{f'subtitle: "{subtitle}"' if subtitle else ''}
author: "{translator}"
publisher: "Soul Spirit Self"
---

{body}
"""
    tmp = DOWNLOADS_DIR / f".{slug}.tmp.md"
    tmp.write_text(md)
    try:
        subprocess.run(
            ["pandoc", str(tmp), "-o", str(out), "--toc", "--toc-depth=2"],
            check=True,
            capture_output=True,
        )
    finally:
        tmp.unlink(missing_ok=True)
    return out


# ── Frontmatter injection ──────────────────────────────────────

def inject_frontmatter(md_path: Path, slug: str, words: int, minutes: int):
    """Update the text MD's frontmatter with downloadTxt/Pdf/Epub paths and word/reading-time."""
    raw = md_path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.DOTALL)
    if not m:
        return
    fm = yaml.safe_load(m.group(1))
    body = m.group(2)

    fm["downloadTxt"] = f"/downloads/{slug}.txt"
    fm["downloadPdf"] = f"/downloads/{slug}.pdf"
    fm["downloadEpub"] = f"/downloads/{slug}.epub"
    fm["wordCount"] = words
    fm["readingTimeMinutes"] = minutes

    new_fm = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=10000)
    md_path.write_text(f"---\n{new_fm}---\n{body}")


# ── Main ───────────────────────────────────────────────────────

def process(slug: str, source_md: Path | None = None, inject: bool = True):
    text_md = CONTENT_DIR / f"{slug}.md"
    if not text_md.exists():
        print(f"  [skip] {slug}: no MD found at {text_md}")
        return
    fm, body = parse_md(text_md)
    body_for_files = body
    if source_md:
        _src_fm, body_for_files = parse_md(source_md)

    words = word_count(body_for_files)
    minutes = reading_time(words)

    print(f"  {slug}: {words} words, ~{minutes} min")
    txt_p = write_txt(slug, fm, body_for_files)
    print(f"    txt  → {txt_p.relative_to(PROJECT_ROOT)}")
    pdf_p = write_pdf(slug, fm, body_for_files)
    print(f"    pdf  → {pdf_p.relative_to(PROJECT_ROOT)}")
    try:
        epub_p = write_epub(slug, fm, body_for_files)
        print(f"    epub → {epub_p.relative_to(PROJECT_ROOT)}")
    except Exception as e:
        print(f"    epub failed: {e}")

    if inject:
        inject_frontmatter(text_md, slug, words, minutes)
        print(f"    frontmatter updated with download links + word count")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--source-md", help="Path to full-text MD if different from the page MD")
    ap.add_argument("--no-inject", action="store_true", help="Do not modify the text MD frontmatter")
    args = ap.parse_args()

    if args.all:
        for p in sorted(CONTENT_DIR.glob("*.md")):
            process(p.stem, inject=not args.no_inject)
    elif args.slug:
        src = Path(args.source_md) if args.source_md else None
        process(args.slug, source_md=src, inject=not args.no_inject)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
