#!/usr/bin/env python3
"""Apply one maintenance batch of redundant-image removals for CI draft PRs.

Reads high-confidence candidates from find_redundant_image_candidates.py,
removes image references in English docs, merges alt text into prose when needed,
and deletes image binaries only when no references remain anywhere in the repo.

Intended for .github/workflows/image-curator-maintenance.yml — agents should
follow .github/skills/image-curator/SKILL.md for manual runs and medium-confidence
review.

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
    pr_title,
)

DEFAULT_MAX_EDITS = 25


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


def alt_to_prose_sentence(alt: str) -> str | None:
    alt = alt.strip()
    if not alt:
        return None
    alt = re.sub(r"^(?:a\s+)?(?:screenshot|image|picture)\s+of\s+", "", alt, flags=re.I)
    if not alt:
        return None
    if alt[-1] not in ".!?":
        alt += "."
    if alt[0].islower():
        alt = alt[0].upper() + alt[1:]
    return alt


def prose_already_has_alt(context: str, alt: str) -> bool:
    if not alt:
        return True
    alt_words = [w.lower() for w in re.findall(r"\w{4,}", alt)]
    if not alt_words:
        return False
    ctx = context.lower()
    hits = sum(1 for w in alt_words if w in ctx)
    return hits / len(alt_words) >= 0.6


def remove_image_line(content: str, line_number: int, match_line: str) -> tuple[str, bool]:
    lines = content.splitlines(keepends=True)
    idx = line_number - 1
    if idx < 0 or idx >= len(lines):
        return content, False
    if lines[idx].strip() != match_line.strip():
        # Fuzzy: remove line that contains the image path fragment
        target = match_line.strip()
        if target not in lines[idx]:
            return content, False
    del lines[idx]
    return "".join(lines), True


def merge_alt_into_previous_paragraph(content: str, line_number: int, alt: str) -> str:
    sentence = alt_to_prose_sentence(alt)
    if not sentence:
        return content
    lines = content.splitlines(keepends=True)
    idx = line_number - 1
    for prev in range(idx - 1, max(-1, idx - 6), -1):
        if prev < 0:
            break
        line = lines[prev]
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("|"):
            continue
        if stripped.startswith("{%") or stripped.startswith("<"):
            continue
        if stripped.endswith((".", "!", "?")):
            lines[prev] = line.rstrip("\n") + " " + sentence + "\n"
            return "".join(lines)
        lines[prev] = line.rstrip("\n") + " " + sentence + "\n"
        return "".join(lines)
    # Prepend before removed line position
    insert_at = max(0, idx)
    lines.insert(insert_at, sentence + "\n\n")
    return "".join(lines)


def image_still_referenced(rel_path: str) -> bool:
    """True if any file in the repo still references rel_path."""
    needle = rel_path.replace("\\", "/")
    fragments = {needle, needle.split("assets/", 1)[-1] if "assets/" in needle else needle}
    for root, _, files in os.walk(REPO_ROOT):
        if ".git" in root.split(os.sep):
            continue
        for name in files:
            if name.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".md", ".html", ".yml", ".yaml", ".js", ".css", ".rb", ".liquid", ".json")):
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

**Human review required** before merge. This batch removes **redundant image references** from English docs (`_docs/`, `_includes/`) per the [writing style guide](docs/contributing/style_guide/writing_style_guide.md) and [image style guide](docs/contributing/style_guide/image_style_guide.md). Alt text was merged into surrounding prose where the image was removed.

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
IMAGE_CURATION_DELETE_FORCE=1 python3 scripts/image-curator/run_curation_batch.py --limit 25
```

English-only prose edits. For medium-confidence candidates or nuanced UI screenshots, use `@image-curator` manually.
"""
    path.write_text(body, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_MAX_EDITS)
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
                {"skip_reason": msg, "edited_count": "0", "pr_title": ""},
            )
        return 0

    candidates = collect_candidates(min_confidence="high", use_ocr=True)
    batch = candidates[: args.limit]

    edited: list[dict] = []
    deleted_images: list[str] = []
    skipped: list[str] = []

    for ref in batch:
        file_path = REPO_ROOT / ref.source_file
        if not file_path.is_file():
            skipped.append(f"{ref.source_file}:{ref.line_number} (file missing)")
            continue

        content = file_path.read_text(encoding="utf-8")
        context = f"{ref.context_before}\n{ref.context_after}"

        if ref.alt_text and not prose_already_has_alt(context, ref.alt_text):
            content = merge_alt_into_previous_paragraph(content, ref.line_number, ref.alt_text)

        new_content, removed = remove_image_line(content, ref.line_number, ref.match_line)
        if not removed:
            skipped.append(f"{ref.source_file}:{ref.line_number} (line not found)")
            continue

        file_path.write_text(new_content, encoding="utf-8")
        edited.append(
            {
                "source_file": ref.source_file,
                "line_number": ref.line_number,
                "image_path": ref.normalized_path(),
                "reasons": ref.reasons,
            }
        )

        img_rel = ref.normalized_path()
        if img_rel.startswith("assets/img/"):
            disk = REPO_ROOT / img_rel
            if disk.is_file() and not image_still_referenced(img_rel):
                disk.unlink()
                deleted_images.append(img_rel)

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
