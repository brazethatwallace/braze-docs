#!/usr/bin/env python3
"""Delete one maintenance batch of unreferenced images for CI review PRs.

Excludes paths touched in open pull requests, applies secondary verification,
and deletes up to --limit files (default 100). Intended for
.github/workflows/image-pruner-maintenance.yml — not for ad-hoc local deletes
(use find_unreferenced_images.py --delete instead).

Requires UNREFERENCED_IMAGE_DELETE_FORCE=1.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from find_unreferenced_images import (  # noqa: E402
    DEFAULT_MAX_DELETES,
    REPO_ROOT,
    collect_deletable_image_files,
    collect_referenced_images,
    file_size_bytes,
    find_secondary_references,
    human_bytes,
    load_allowlist,
    pr_title,
)


def _run_gh(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


def collect_open_pr_asset_paths() -> set[str]:
    """Paths under assets/img/ changed in any open pull request."""
    listed = _run_gh(["pr", "list", "--state", "open", "--json", "number", "--limit", "200"])
    if listed.returncode != 0:
        print(f"WARN: gh pr list failed: {listed.stderr.strip()}", file=sys.stderr)
        return set()

    try:
        pr_numbers = [str(item["number"]) for item in json.loads(listed.stdout or "[]")]
    except json.JSONDecodeError:
        return set()

    excluded: set[str] = set()
    for number in pr_numbers:
        diff = _run_gh(["pr", "diff", number, "--name-only"])
        if diff.returncode != 0:
            continue
        for line in diff.stdout.splitlines():
            line = line.strip()
            if line.startswith("assets/img/"):
                excluded.add(line)
    return excluded


def has_open_ip_deletion_pr() -> bool:
    """True when another [IP] image-deletion PR is already open."""
    listed = _run_gh(["pr", "list", "--state", "open", "--json", "title", "--limit", "200"])
    if listed.returncode != 0:
        return False
    try:
        titles = [item["title"] for item in json.loads(listed.stdout or "[]")]
    except json.JSONDecodeError:
        return False
    prefix = "[IP] Remove"
    return any(title.startswith(prefix) for title in titles)


def write_github_output(path: Path, data: dict[str, str]) -> None:
    with path.open("a", encoding="utf-8") as fh:
        for key, value in data.items():
            fh.write(f"{key}={value}\n")


def write_pr_body(
    path: Path,
    *,
    scan_date: str,
    run_url: str,
    deleted: list[str],
    skipped: list[tuple[str, str]],
    deleted_bytes: int,
    unreferenced_count: int,
    excluded_count: int,
    remaining_count: int,
) -> None:
    skipped_lines = "\n".join(f"- `{rel}` (referenced in `{hit}`)" for rel, hit in skipped[:15])
    if len(skipped) > 15:
        skipped_lines += f"\n- ... and {len(skipped) - 15} more"

    body = f"""## Image Pruning

This **draft** pull request was opened automatically by the [Image pruner (maintenance)]({run_url}) workflow.

**Human review required** before merge. Review the deleted files in this diff; secondary verification skipped {len(skipped)} candidate(s) in this batch.

| Metric | Value |
|--------|-------|
| Scan date | {scan_date} |
| Unreferenced before batch | {unreferenced_count} |
| Deleted in this PR | {len(deleted)} (~{human_bytes(deleted_bytes)}) |
| Skipped (secondary verify) | {len(skipped)} |
| Excluded (open PRs) | {excluded_count} |
| Unreferenced remaining (estimate) | {remaining_count} |

## Scan

```bash
python3 scripts/image-pruner/find_unreferenced_images.py \\
  --csv scripts/image-pruner/unreferenced_images.csv
```

Reference pass included `_lang/`, `docs/`, and site chrome. Excluded from deletion: `logos/`, `braze_icons/`, `icons/`.

Paths in open pull requests were excluded from this batch. If more than 100 files remain, merge this PR and re-run the workflow (or use `@image-pruner`) for the next batch.

"""
    if skipped:
        body += f"""## Skipped by secondary verification

{skipped_lines}

"""
    path.write_text(body, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_MAX_DELETES,
        help=f"Max files to delete (default {DEFAULT_MAX_DELETES}).",
    )
    parser.add_argument(
        "--github-output",
        type=Path,
        metavar="PATH",
        help="Append step outputs (GITHUB_OUTPUT format).",
    )
    parser.add_argument(
        "--pr-body",
        type=Path,
        metavar="PATH",
        help="Write pull request body markdown to this file.",
    )
    parser.add_argument(
        "--scan-date",
        default="",
        help="Date stamp for PR body (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--run-url",
        default="",
        help="Workflow run URL for PR body.",
    )
    parser.add_argument(
        "--skip-if-open-ip-pr",
        action="store_true",
        help="Exit without deleting when another open [IP] deletion PR exists.",
    )
    args = parser.parse_args()

    force = os.environ.get("UNREFERENCED_IMAGE_DELETE_FORCE", "").lower() in {
        "1",
        "true",
        "yes",
    }
    if not force:
        print("Refusing to delete: set UNREFERENCED_IMAGE_DELETE_FORCE=1.", file=sys.stderr)
        return 1

    if args.skip_if_open_ip_pr and has_open_ip_deletion_pr():
        print("Skipping batch: an open [IP] deletion PR already exists.")
        outputs = {
            "deleted_count": "0",
            "skipped_count": "0",
            "remaining_count": "0",
            "deleted_bytes_human": "0 B",
            "pr_title": "",
            "skip_reason": "open_ip_pr",
        }
        if args.github_output:
            write_github_output(args.github_output, outputs)
        return 0

    excluded = collect_open_pr_asset_paths()
    _, _, _, referenced = collect_referenced_images()
    deletable = collect_deletable_image_files()
    allowlist = load_allowlist()
    unreferenced = sorted(deletable - referenced - allowlist)
    candidates = [path for path in unreferenced if path not in excluded][: args.limit]

    skipped_verify: list[tuple[str, str]] = []
    deleted: list[str] = []
    deleted_bytes = 0

    for rel in candidates:
        hits = find_secondary_references(rel)
        if hits:
            skipped_verify.append((rel, hits[0]))
            continue
        target = REPO_ROOT / rel
        if not target.is_file():
            continue
        deleted_bytes += file_size_bytes(rel)
        target.unlink()
        deleted.append(rel)

    remaining = max(0, len(unreferenced) - len(deleted))
    outputs = {
        "deleted_count": str(len(deleted)),
        "skipped_count": str(len(skipped_verify)),
        "remaining_count": str(remaining),
        "excluded_count": str(len(excluded)),
        "unreferenced_count": str(len(unreferenced)),
        "deleted_bytes_human": human_bytes(deleted_bytes),
        "pr_title": pr_title(len(deleted)) if deleted else "",
        "skip_reason": "",
    }

    print(f"Maintenance batch: deleted {len(deleted)}, skipped {len(skipped_verify)}")
    print(f"  Excluded {len(excluded)} path(s) from open PRs")
    print(f"  ~{human_bytes(deleted_bytes)} reclaimed; ~{remaining} unreferenced remain")

    if args.github_output:
        write_github_output(args.github_output, outputs)

    if args.pr_body and deleted:
        write_pr_body(
            args.pr_body,
            scan_date=args.scan_date,
            run_url=args.run_url,
            deleted=deleted,
            skipped=skipped_verify,
            deleted_bytes=deleted_bytes,
            unreferenced_count=len(unreferenced),
            excluded_count=len(excluded),
            remaining_count=remaining,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
