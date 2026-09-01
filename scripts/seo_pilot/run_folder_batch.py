#!/usr/bin/env python3
"""Run SEO audit + no-approval apply for one _docs/ top-level folder."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from meta_exempt import skips_seo_audit

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = REPO_ROOT / "_docs"
TEMP = REPO_ROOT / "scripts/temp"


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(cmd), flush=True)
    return subprocess.run(cmd, cwd=REPO_ROOT, check=check, text=True)


def folder_pages(folder: str) -> Path:
    pages_file = TEMP / f"pages-{folder}.txt"
    pages_file.parent.mkdir(parents=True, exist_ok=True)
    paths = sorted(
        p
        for p in (DOCS_ROOT / folder).rglob("*.md")
        if not skips_seo_audit(str(p.relative_to(REPO_ROOT)))
    )
    pages_file.write_text("\n".join(str(p.relative_to(REPO_ROOT)) for p in paths) + "\n", encoding="utf-8")
    return pages_file


def audit_folder(folder: str) -> tuple[Path, Path]:
    pages_file = folder_pages(folder)
    link_csv = TEMP / f"link-fix-{folder}.csv"
    rec_dir = TEMP / f"recommendations-{folder}"
    if rec_dir.exists():
        shutil.rmtree(rec_dir)

    run(
        [
            sys.executable,
            "scripts/seo_pilot/link_fix_table.py",
            "--pages-file",
            str(pages_file),
            "--out",
            str(link_csv),
            "--scan-all",
        ]
    )
    run(
        [
            sys.executable,
            "scripts/seo_pilot/page_audit.py",
            "--pages-file",
            str(pages_file),
            "--link-fix-csv",
            str(link_csv),
            "--out-dir",
            str(rec_dir),
        ]
    )
    run(
        [
            sys.executable,
            "scripts/seo_pilot/apply_wave2_no_approval.py",
            "--recommendations",
            str(rec_dir),
            "--link-fix-csv",
            str(link_csv),
        ]
    )
    shutil.rmtree(rec_dir)
    return pages_file, link_csv


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit one _docs top-level folder")
    parser.add_argument("folder", help="Top-level folder name under _docs (e.g. _api)")
    args = parser.parse_args()
    folder = args.folder
    if not (DOCS_ROOT / folder).is_dir():
        print(f"Not a folder: _docs/{folder}", file=sys.stderr)
        return 1
    pages_file, link_csv = audit_folder(folder)
    print(f"Pages: {pages_file}")
    print(f"Link fixes: {link_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
