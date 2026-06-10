#!/usr/bin/env python3
"""Find image files under assets/img/ unreferenced in docs articles or site chrome.

Scans _docs/, _includes/, and _lang/ for article references. Also scans layouts,
plugins, CSS/JS, and root config so layout-only assets are never deleted.

Never deletes files under assets/img/logos/, assets/img/braze_icons/, or assets/img/icons/.

Usage (from repo root):
  python3 scripts/image-pruner/find_unreferenced_images.py
  python3 scripts/image-pruner/find_unreferenced_images.py --csv scripts/image-pruner/unreferenced_images.csv
  python3 scripts/image-pruner/find_unreferenced_images.py --delete   # requires UNREFERENCED_IMAGE_DELETE_FORCE=1

Safety:
  - Default is report-only (no deletes).
  - --delete removes files only when UNREFERENCED_IMAGE_DELETE_FORCE=1.
  - If more than UNREFERENCED_IMAGE_MAX_DELETES (default 100) unreferenced files exist,
    --delete removes only the first N per run (re-run for additional batches).
  - With --delete, each candidate is verified with a secondary scan unless --no-verify.
  - assets/img/logos/, assets/img/braze_icons/, and assets/img/icons/ are never deleted.

Pull request (Image Pruning batches):
  - Title prefix: [IP]
  - Label: image pruning
  - Body must state the PR is for Image Pruning (see print_pr_guidance after --delete).
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[2]
IMG_ROOT = REPO_ROOT / "assets" / "img"

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}

ARTICLE_REFERENCE_DIRS = (
    "_docs",
    "_includes",
    "_lang",
)

# Contributing guides (repo-root docs/, not published site pages).
CONTRIBUTING_REFERENCE_DIRS = (
    "docs",
)

# Layouts, plugins, styles, and scripts — references here keep images from deletion.
SITE_CHROME_REFERENCE_DIRS = (
    "_layouts",
    "_plugins",
    "assets/css",
    "assets/js",
)

ARTICLE_SCAN_EXTENSIONS = {
    ".md",
    ".html",
    ".htm",
    ".yml",
    ".yaml",
}

SITE_CHROME_SCAN_EXTENSIONS = {
    ".html",
    ".htm",
    ".yml",
    ".yaml",
    ".json",
    ".rb",
    ".scss",
    ".css",
    ".js",
    ".liquid",
}

_ROOT_REFERENCE_FILES = (
    "_config.yml",
    "vercel.json",
    "package.json",
)


# Paths under assets/img/ referenced in scanned content.
_REF_PATTERNS = [
    re.compile(r"image_buster\s+/?assets/img/([^\s%}]+)", re.IGNORECASE),
    re.compile(r"(?:\.\./)+assets/img/([^\s'\"<>)\]}]+)", re.IGNORECASE),
    re.compile(r"/docs/assets/img/([^\s'\"<>)\]}]+)", re.IGNORECASE),
    re.compile(r"/assets/img/([^\s'\"<>)\]}]+)", re.IGNORECASE),
    re.compile(r"(?<![\w./])assets/img/([^\s'\"<>)\]}]+)", re.IGNORECASE),
]

# Liquid/Ruby interpolation in site chrome (e.g. message-#{icon_file}.png).
_DYNAMIC_CHROME_MARKERS = (
    re.compile(r"assets/img/message-\#\{"),
)

# Alert icons at assets/img/message-<type>.png (not message_foo screenshots).
_ALERT_ICON_PATH = re.compile(r"^assets/img/message-[a-z-]+\.png$")

# Never eligible for deletion (site chrome, landing icons, logos).
PROTECTED_IMG_PREFIXES = (
    "assets/img/logos/",
    "assets/img/braze_icons/",
    "assets/img/icons/",
)

_ALLOWLIST_PATH = REPO_ROOT / "_data" / "unreferenced_images_allowlist.txt"
DEFAULT_MAX_DELETES = 100

# Image Pruning pull request conventions (see .github/skills/image-pruner/SKILL.md).
PR_TITLE_PREFIX = "[IP]"
PR_LABEL = "image pruning"
PR_WORKFLOW_NAME = "Image Pruning"


def is_protected_image(rel_path: str) -> bool:
    rel_path = rel_path.replace("\\", "/")
    return any(rel_path.startswith(prefix) for prefix in PROTECTED_IMG_PREFIXES)


def _iter_files_in_dirs(rel_dirs: tuple[str, ...], extensions: set[str]) -> list[Path]:
    files: list[Path] = []
    for rel_dir in rel_dirs:
        root = REPO_ROOT / rel_dir
        if not root.is_dir():
            continue
        for dirpath, _, filenames in os.walk(root):
            for name in filenames:
                if Path(name).suffix.lower() in extensions:
                    files.append(Path(dirpath) / name)
    return files


def _iter_article_files() -> list[Path]:
    return _iter_files_in_dirs(ARTICLE_REFERENCE_DIRS, ARTICLE_SCAN_EXTENSIONS)


def _iter_contributing_files() -> list[Path]:
    return _iter_files_in_dirs(CONTRIBUTING_REFERENCE_DIRS, ARTICLE_SCAN_EXTENSIONS)


def _iter_site_chrome_files() -> list[Path]:
    files = _iter_files_in_dirs(SITE_CHROME_REFERENCE_DIRS, SITE_CHROME_SCAN_EXTENSIONS)
    for rel in _ROOT_REFERENCE_FILES:
        path = REPO_ROOT / rel
        if path.is_file():
            files.append(path)
    return files


def _iter_all_reference_files() -> list[Path]:
    return _iter_article_files() + _iter_contributing_files() + _iter_site_chrome_files()


def _normalize_ref(path_fragment: str) -> str | None:
    raw = unquote(path_fragment.strip().strip("'\""))
    raw = raw.split("?")[0].split("#")[0].rstrip(").,;")
    if not raw:
        return None
    rel = raw.lstrip("/")
    if rel.startswith("assets/img/"):
        key = rel
    else:
        key = f"assets/img/{rel}"
    suffix = Path(key).suffix.lower()
    if suffix not in IMAGE_SUFFIXES:
        return None
    return key.replace("\\", "/")


def _reference_needles(rel_path: str) -> list[str]:
    """Full-path fragments for secondary verification (no bare filenames)."""
    rel_path = rel_path.replace("\\", "/")
    return [
        rel_path,
        f"/{rel_path}",
        f"/docs/{rel_path}",
    ]


def find_secondary_references(rel_path: str) -> list[str]:
    """Return repo files (articles or site chrome) that still mention this image path."""
    hits: list[str] = []
    needles = _reference_needles(rel_path)
    for path in _iter_all_reference_files():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if any(needle in text for needle in needles):
            hits.append(path.relative_to(REPO_ROOT).as_posix())
    return hits


def _collect_referenced_images_from_files(files: list[Path]) -> set[str]:
    referenced: set[str] = set()
    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"WARN: could not read {path.relative_to(REPO_ROOT)}: {exc}", file=sys.stderr)
            continue
        for pattern in _REF_PATTERNS:
            for match in pattern.finditer(text):
                normalized = _normalize_ref(match.group(1))
                if normalized:
                    referenced.add(normalized)
    return referenced


def _collect_dynamic_chrome_refs() -> set[str]:
    """Images whose paths are built at build time from site-chrome templates."""
    referenced: set[str] = set()
    for path in _iter_site_chrome_files():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if not any(marker.search(text) for marker in _DYNAMIC_CHROME_MARKERS):
            continue
        for img in collect_image_files():
            if _ALERT_ICON_PATH.match(img):
                referenced.add(img)
    return referenced


def collect_referenced_images() -> tuple[set[str], set[str], set[str], set[str]]:
    """Return (article_refs, contributing_refs, site_chrome_refs, all_refs)."""
    article_refs = _collect_referenced_images_from_files(_iter_article_files())
    contributing_refs = _collect_referenced_images_from_files(_iter_contributing_files())
    chrome_refs = _collect_referenced_images_from_files(_iter_site_chrome_files())
    chrome_refs |= _collect_dynamic_chrome_refs()
    all_refs = article_refs | contributing_refs | chrome_refs
    return article_refs, contributing_refs, chrome_refs, all_refs


def collect_image_files() -> set[str]:
    images: set[str] = set()
    if not IMG_ROOT.is_dir():
        return images
    for dirpath, _, filenames in os.walk(IMG_ROOT):
        for name in filenames:
            if name.startswith("."):
                continue
            suffix = Path(name).suffix.lower()
            if suffix not in IMAGE_SUFFIXES:
                continue
            full = Path(dirpath) / name
            rel = full.relative_to(REPO_ROOT).as_posix()
            images.add(rel)
    return images


def collect_deletable_image_files() -> set[str]:
    """All image files except those under protected prefixes."""
    return {path for path in collect_image_files() if not is_protected_image(path)}


def load_allowlist() -> set[str]:
    if not _ALLOWLIST_PATH.is_file():
        return set()
    allowed: set[str] = set()
    for line in _ALLOWLIST_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.replace("\\", "/")
        if not line.startswith("assets/img/"):
            line = f"assets/img/{line.lstrip('/')}"
        allowed.add(line)
    return allowed


def file_size_bytes(rel_path: str) -> int:
    try:
        return (REPO_ROOT / rel_path).stat().st_size
    except OSError:
        return 0


def human_bytes(num: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if num < 1024 or unit == "GB":
            return f"{num:.1f} {unit}" if unit != "B" else f"{num} {unit}"
        num /= 1024
    return f"{num:.1f} GB"


def pr_title(deleted_count: int) -> str:
    return f"{PR_TITLE_PREFIX} Remove {deleted_count} unreferenced images from assets/img"


def print_pr_guidance(deleted_count: int, deleted_bytes: int) -> None:
    """Print Image Pruning PR title, label, and body template after a delete batch."""
    if deleted_count < 1:
        return
    print(f"\n{PR_WORKFLOW_NAME} — open a PR with only image deletions in this batch:")
    print(f"  Title:  {pr_title(deleted_count)}")
    print(f"  Label:  {PR_LABEL}")
    print(f"  Bytes:  {human_bytes(deleted_bytes)} reclaimed ({deleted_count} file(s))")
    print(
        "\n  Example:\n"
        f'  gh pr create --title "{pr_title(deleted_count)}" \\\n'
        f'    --label "{PR_LABEL}" \\\n'
        '    --body "$(cat <<\'EOF\'\n'
        "## Image Pruning\n"
        "\n"
        f"This PR is for **{PR_WORKFLOW_NAME}**: removes {deleted_count} unreferenced "
        f"image file(s) (~{human_bytes(deleted_bytes)}).\n"
        "\n"
        "## Scan\n"
        "\n"
        "```bash\n"
        "python3 scripts/image-pruner/find_unreferenced_images.py \\\n"
        "  --csv scripts/image-pruner/unreferenced_images.csv\n"
        "UNREFERENCED_IMAGE_DELETE_FORCE=1 python3 scripts/image-pruner/find_unreferenced_images.py --delete\n"
        "```\n"
        "\n"
        "Reference pass included `_lang/`, `docs/`, and site chrome. "
        "Excluded from deletion: `logos/`, `braze_icons/`, `icons/`.\n"
        "EOF\n"
        ')"'
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        metavar="PATH",
        help="Write unreferenced images to CSV (path, size_bytes).",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete unreferenced article images (requires UNREFERENCED_IMAGE_DELETE_FORCE=1).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        metavar="N",
        help=(
            "Max files to delete this run (default: UNREFERENCED_IMAGE_MAX_DELETES or "
            f"{DEFAULT_MAX_DELETES})."
        ),
    )
    parser.add_argument(
        "--no-verify",
        action="store_true",
        help="Skip secondary text search before each deletion (not recommended).",
    )
    args = parser.parse_args()

    (
        referenced_in_articles,
        referenced_in_contributing,
        referenced_in_site_chrome,
        referenced,
    ) = collect_referenced_images()
    all_images = collect_image_files()
    deletable_images = collect_deletable_image_files()
    allowlist = load_allowlist()

    unreferenced = sorted(deletable_images - referenced - allowlist)
    total_bytes = sum(file_size_bytes(p) for p in unreferenced)
    protected_count = len(all_images) - len(deletable_images)
    content_refs = referenced_in_articles | referenced_in_contributing
    chrome_only = referenced_in_site_chrome - content_refs
    contributing_only = referenced_in_contributing - referenced_in_articles

    report = {
        "image_files": len(all_images),
        "protected_images": protected_count,
        "deletable_images": len(deletable_images),
        "referenced_in_articles": len(referenced_in_articles),
        "referenced_in_contributing": len(referenced_in_contributing),
        "referenced_contributing_only": len(contributing_only),
        "referenced_in_site_chrome": len(referenced_in_site_chrome),
        "referenced_site_chrome_only": len(chrome_only),
        "referenced_images": len(referenced),
        "allowlisted_images": len(allowlist),
        "unreferenced_images": len(unreferenced),
        "unreferenced_bytes": total_bytes,
        "unreferenced_paths": unreferenced,
    }

    print("Unreferenced image scan (assets/img/)")
    print(f"  Image files on disk:               {report['image_files']}")
    print(
        "  Protected (never deleted):         "
        f"{report['protected_images']} (logos/, braze_icons/, icons/)"
    )
    print(f"  Eligible for cleanup:              {report['deletable_images']}")
    print(f"  Referenced in articles:            {report['referenced_in_articles']}")
    print(f"  Referenced in contributing (docs/): {report['referenced_in_contributing']}")
    print(f"  Referenced in site chrome only:    {report['referenced_site_chrome_only']}")
    print(f"  Referenced total (kept):           {report['referenced_images']}")
    print(f"  Allowlisted (skipped):           {report['allowlisted_images']}")
    print(f"  Unreferenced (deletable):        {report['unreferenced_images']} ({human_bytes(total_bytes)})")

    if args.csv:
        out = Path(args.csv)
        if not out.is_absolute():
            out = REPO_ROOT / out
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["path", "size_bytes"])
            for rel in unreferenced:
                writer.writerow([rel, file_size_bytes(rel)])
        print(f"  Wrote {out.relative_to(REPO_ROOT)}")

    if unreferenced:
        print("\nSample unreferenced paths (up to 25):")
        for rel in unreferenced[:25]:
            print(f"  - {rel}")
        if len(unreferenced) > 25:
            print(f"  ... and {len(unreferenced) - 25} more")

    if args.delete:
        force = os.environ.get("UNREFERENCED_IMAGE_DELETE_FORCE", "").lower() in {
            "1",
            "true",
            "yes",
        }
        max_deletes = int(
            os.environ.get("UNREFERENCED_IMAGE_MAX_DELETES", str(DEFAULT_MAX_DELETES))
        )
        batch_limit = args.limit if args.limit is not None else max_deletes
        if batch_limit < 1:
            print("Error: --limit must be at least 1.", file=sys.stderr)
            return 1
        if not force:
            print(
                "\nRefusing to delete: set UNREFERENCED_IMAGE_DELETE_FORCE=1 after review.",
                file=sys.stderr,
            )
            return 1

        batch = unreferenced[:batch_limit]
        skipped_verify: list[tuple[str, list[str]]] = []
        to_delete: list[str] = []

        if not args.no_verify:
            for rel in batch:
                secondary_hits = find_secondary_references(rel)
                if secondary_hits:
                    skipped_verify.append((rel, secondary_hits))
                else:
                    to_delete.append(rel)
        else:
            to_delete = batch

        if skipped_verify:
            print(
                f"\nSkipped {len(skipped_verify)} file(s) after secondary reference check:",
                file=sys.stderr,
            )
            for rel, hits in skipped_verify[:10]:
                print(f"  - {rel} (mentioned in {hits[0]})", file=sys.stderr)
            if len(skipped_verify) > 10:
                print(f"  ... and {len(skipped_verify) - 10} more", file=sys.stderr)

        deleted = 0
        deleted_bytes = 0
        for rel in to_delete:
            target = REPO_ROOT / rel
            try:
                deleted_bytes += file_size_bytes(rel)
                target.unlink()
                deleted += 1
            except OSError as exc:
                print(f"WARN: could not delete {rel}: {exc}", file=sys.stderr)

        remaining = len(unreferenced) - deleted
        print(f"\nDeleted {deleted} unreferenced image file(s) this run.")
        if remaining > 0:
            print(f"  {remaining} unreferenced image(s) remain — re-run scan and delete for next batch.")
        print_pr_guidance(deleted, deleted_bytes)
        if skipped_verify:
            print(
                "  Add false positives to _data/unreferenced_images_allowlist.txt or fix scanner gaps.",
                file=sys.stderr,
            )
            return 1 if deleted == 0 else 0
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
