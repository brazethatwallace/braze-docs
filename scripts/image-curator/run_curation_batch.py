#!/usr/bin/env python3
"""Apply one maintenance batch of redundant-image removals for CI draft PRs.

Reads high-confidence candidates from find_redundant_image_candidates.py and
removes image references from English docs. Does **not** merge alt text into
prose — agents follow the alt merge gate in .github/skills/image-curator/ for
the rare cases where prose needs a manual update.

Requires IMAGE_CURATION_DELETE_FORCE=1.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from find_redundant_image_candidates import (  # noqa: E402
    PR_LABEL,
    PR_TITLE_PREFIX,
    REPO_ROOT,
    collect_candidates,
    load_candidates_from_csv,
    pr_title,
)

DEFAULT_MAX_EDITS = 15


def _run_gh(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


def has_open_ic_pr() -> bool:
    listed = _run_gh(["pr", "list", "--state", "open", "--json", "title", "--limit", "200"])
    if listed.returncode != 0:
        return False
    try:
        titles = [item["title"] for item in json.loads(listed.stdout or "[]")]
    except json.JSONDecodeError:
        return False
    return any(title.startswith(PR_TITLE_PREFIX) for title in titles)


def _path_in_line_pattern(image_path: str) -> str:
    """Regex fragment for image_path with optional leading slash."""
    path = image_path.replace("\\", "/").lstrip("/")
    return rf"/?{re.escape(path)}"


def strip_image_markup_by_path(line: str, image_path: str) -> tuple[str, bool]:
    """Remove image markup containing image_path; leave other line content intact."""
    if not image_path.strip():
        return line, False

    path_pat = _path_in_line_pattern(image_path)
    patterns = (
        rf"!\[[^\]]*\]\(\s*(?:\{{%[^%]*image_buster\s+)?{path_pat}[^)]*\)",
        rf"\{{%[^%]*image_buster\s+{path_pat}[^%]*%\}}",
        rf"<img\b[^>]*\bsrc=[\"'][^\"']*?{path_pat}[^\"']*[\"'][^>]*>",
    )

    new_line = line
    removed = False
    for pattern in patterns:
        new_line, count = re.subn(pattern, "", new_line, count=1, flags=re.I)
        if count:
            removed = True
            break

    if not removed:
        return line, False

    new_line = re.sub(r"\s*<br\s*/?>\s*$", "", new_line.rstrip(), flags=re.I)
    new_line = re.sub(r"\s*<br\s*/?>\s*(?=\s*$)", "", new_line, flags=re.I)
    return new_line.rstrip(), True


def _trim_trailing_break(line: str) -> str:
    line = re.sub(r"\s*<br\s*/?>\s*$", "", line.rstrip(), flags=re.I)
    return re.sub(r"\s*<br\s*/?>\s*(?=\s*$)", "", line, flags=re.I).rstrip()


def _write_line_after_removal(
    lines: list[str], idx: int, original_line: str, new_line: str
) -> str:
    if not new_line.strip():
        del lines[idx]
    else:
        lines[idx] = new_line + ("\n" if original_line.endswith("\n") else "")
    return "".join(lines)


def find_image_line_index(
    lines: list[str],
    match_line: str,
    image_path: str,
    *,
    hint_line_number: int | None = None,
) -> int | None:
    """Return 0-based index of the image reference line, or None if not found."""
    target = match_line.strip()
    path_fragment = image_path.replace("\\", "/")

    exact: list[int] = []
    fuzzy: list[int] = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == target:
            exact.append(i)
        elif target and target in stripped:
            fuzzy.append(i)
        elif path_fragment and path_fragment in stripped:
            fuzzy.append(i)

    candidates = exact or fuzzy
    if not candidates:
        return None
    if len(candidates) == 1 or hint_line_number is None:
        return candidates[0]

    hint_idx = hint_line_number - 1
    return min(candidates, key=lambda i: abs(i - hint_idx))


def remove_image_line(
    content: str,
    match_line: str,
    image_path: str,
    *,
    hint_line_number: int | None = None,
) -> tuple[str, bool]:
    """Remove image reference only; never modify other prose on the line."""
    lines = content.splitlines(keepends=True)
    idx = find_image_line_index(
        lines, match_line, image_path, hint_line_number=hint_line_number
    )
    if idx is None:
        return content, False

    line = lines[idx]
    target = match_line.strip()

    if line.strip() == target:
        del lines[idx]
        return "".join(lines), True

    new_line, removed = strip_image_markup_by_path(line, image_path)
    if removed:
        return (
            _write_line_after_removal(
                lines, idx, line, _trim_trailing_break(new_line)
            ),
            True,
        )

    if target and target in line:
        new_line = line.replace(target, "", 1)
        # Empty markdown shell when target was image_buster inside ![alt](...).
        new_line = re.sub(r"!\[[^\]]*\]\(\s*\)", "", new_line, count=1)
        return (
            _write_line_after_removal(
                lines, idx, line, _trim_trailing_break(new_line)
            ),
            True,
        )

    return content, False


def sort_batch_for_processing(batch: list) -> list:
    """Bottom-up within each file so earlier edits do not shift later match lines."""
    return sorted(batch, key=lambda r: (r.source_file, -r.line_number))


def image_still_referenced(rel_path: str) -> bool:
    """True if any file in the repo still references rel_path."""
    needle = rel_path.replace("\\", "/")
    fragments = {needle, needle.split("assets/", 1)[-1] if "assets/" in needle else needle}
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            if name.endswith(
                (
                    ".svg",
                    ".md",
                    ".html",
                    ".htm",
                    ".yml",
                    ".yaml",
                    ".js",
                    ".css",
                    ".scss",
                    ".rb",
                    ".liquid",
                    ".json",
                )
            ):
                path = Path(root) / name
                try:
                    text = path.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                if any(frag in text for frag in fragments):
                    return True
    return False


def write_github_output(path: Path, data: dict[str, str]) -> None:
    with path.open("a", encoding="utf-8") as fh:
        for key, value in data.items():
            fh.write(f"{key}={value}\n")


def write_pr_body(
    path: Path,
    *,
    scan_date: str,
    run_url: str,
    edited: list[dict],
    deleted_images: list[str],
    skipped: list[str],
) -> None:
    edited_lines = "\n".join(
        f"- `{e['source_file']}:{e['line_number']}` — `{e['image_path']}` ({', '.join(e['reasons'])})"
        for e in edited[:30]
    )
    if len(edited) > 30:
        edited_lines += f"\n- ... and {len(edited) - 30} more"

    deleted_lines = "\n".join(f"- `{p}`" for p in deleted_images[:20])
    if len(deleted_images) > 20:
        deleted_lines += f"\n- ... and {len(deleted_images) - 20} more"

    skipped_lines = "\n".join(f"- {s}" for s in skipped[:10])
    if len(skipped) > 10:
        skipped_lines += f"\n- ... and {len(skipped) - 10} more"

    body = f"""## Image Pruning

This **draft** pull request was opened automatically by the [Image curator (maintenance)]({run_url}) workflow.

**Human review required** before merge. This batch removes **redundant image references** from English docs (`_docs/`, `_includes/`) per the [writing style guide](docs/contributing/style_guide/writing_style_guide.md) and [image style guide](docs/contributing/style_guide/image_style_guide.md). Image references were deleted only; alt text was **not** auto-merged into prose.

| Metric | Value |
|--------|-------|
| Scan date | {scan_date} |
| References removed | {len(edited)} |
| Image files deleted (unreferenced after edit) | {len(deleted_images)} |
| Skipped | {len(skipped)} |

### Edited references

{edited_lines or "_None_"}

### Deleted image files

{deleted_lines or "_None — locales or other pages may still reference these binaries._"}

### Skipped

{skipped_lines or "_None_"}

## Scan

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py --csv candidates.csv --min-confidence high
IMAGE_CURATION_DELETE_FORCE=1 python3 scripts/image-curator/run_curation_batch.py --limit 15 --csv candidates.csv
```

English-only edits. Prose updates after removal require manual review via `@image-curator`.
"""
    path.write_text(body, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_MAX_EDITS)
    parser.add_argument(
        "--csv",
        type=Path,
        help="Reuse scan CSV from find_redundant_image_candidates.py (skips OCR rescan)",
    )
    parser.add_argument("--skip-if-open-ic-pr", action="store_true")
    parser.add_argument("--scan-date", default="")
    parser.add_argument("--run-url", default="")
    parser.add_argument("--github-output", type=Path)
    parser.add_argument("--pr-body", type=Path)
    args = parser.parse_args()

    if os.environ.get("IMAGE_CURATION_DELETE_FORCE") != "1":
        print("ERROR: Set IMAGE_CURATION_DELETE_FORCE=1 to apply edits.", file=sys.stderr)
        return 1

    if args.skip_if_open_ic_pr and has_open_ic_pr():
        msg = "open_ic_pr"
        print(f"SKIP: An open {PR_TITLE_PREFIX} PR already exists.")
        if args.github_output:
            write_github_output(
                args.github_output,
                {
                    "skip_reason": msg,
                    "edited_count": "0",
                    "deleted_image_count": "0",
                    "skipped_count": "0",
                    "pr_title": "",
                },
            )
        return 0

    if args.csv:
        if not args.csv.is_file():
            print(f"ERROR: CSV not found: {args.csv}", file=sys.stderr)
            return 1
        candidates = load_candidates_from_csv(args.csv, min_confidence="high")
    else:
        candidates = collect_candidates(min_confidence="high", use_ocr=True)
    batch = sort_batch_for_processing(candidates[: args.limit])

    edited: list[dict] = []
    deleted_images: list[str] = []
    skipped: list[str] = []

    file_idx = 0
    while file_idx < len(batch):
        source_file = batch[file_idx].source_file
        file_refs: list = []
        while file_idx < len(batch) and batch[file_idx].source_file == source_file:
            file_refs.append(batch[file_idx])
            file_idx += 1

        file_path = REPO_ROOT / source_file
        if not file_path.is_file():
            for ref in file_refs:
                skipped.append(f"{ref.source_file}:{ref.line_number} (file missing)")
            continue

        content = file_path.read_text(encoding="utf-8")
        file_edited = False
        deleted_candidates: list[str] = []

        for ref in file_refs:
            image_path = ref.normalized_path()
            hint = ref.line_number

            content, removed = remove_image_line(
                content,
                ref.match_line,
                image_path,
                hint_line_number=hint,
            )
            if not removed:
                skipped.append(f"{ref.source_file}:{ref.line_number} (line not found)")
                continue

            file_edited = True
            edited.append(
                {
                    "source_file": ref.source_file,
                    "line_number": ref.line_number,
                    "image_path": image_path,
                    "reasons": ref.reasons,
                }
            )

            if image_path.startswith("assets/img/"):
                deleted_candidates.append(image_path)

        if file_edited:
            file_path.write_text(content, encoding="utf-8")

        for image_path in deleted_candidates:
            disk = REPO_ROOT / image_path
            if disk.is_file() and not image_still_referenced(image_path):
                disk.unlink()
                deleted_images.append(image_path)

    title = pr_title(len(edited)) if edited else ""
    outputs = {
        "edited_count": str(len(edited)),
        "deleted_image_count": str(len(deleted_images)),
        "skipped_count": str(len(skipped)),
        "pr_title": title,
        "skip_reason": "",
    }

    if args.github_output:
        write_github_output(args.github_output, outputs)

    if args.pr_body and edited:
        write_pr_body(
            args.pr_body,
            scan_date=args.scan_date or "unknown",
            run_url=args.run_url or "",
            edited=edited,
            deleted_images=deleted_images,
            skipped=skipped,
        )

    print(f"Edited {len(edited)} reference(s); deleted {len(deleted_images)} image file(s).")
    if skipped:
        print(f"Skipped {len(skipped)} candidate(s).")
    if title:
        print(f"Suggested PR title: {title}")
        print(f"Suggested label: {PR_LABEL}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
