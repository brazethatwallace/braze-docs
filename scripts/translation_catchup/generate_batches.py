#!/usr/bin/env python3
"""
Generate all_paths.txt and ordered batch files for auto-translate catch-up.

Run from the repository root (or any directory; uses git -C repo_root).

Example:
  ./scripts/translation_catchup/generate_batches.py
  ./scripts/translation_catchup/generate_batches.py --base abc1234 --max-per-batch 30
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

# Last origin/develop commit strictly before 2026-03-31 23:59:59 UTC (catch-up baseline).
DEFAULT_BASE = "3e2a7ea3cac0f973b2cf6a901954739e285c512e"

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent


def run_git(args: list[str], *, cwd: Path) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True,
    )
    return r.stdout


def git_diff_paths(
    repo: Path, base: str, head: str, *, find_renames: bool
) -> list[str]:
    cmd = [
        "diff",
        "--name-only",
        "--diff-filter=ACMR",
    ]
    if find_renames:
        cmd.insert(1, "--find-renames")
    cmd += [base, head, "--", "_docs", "_includes"]
    out = run_git(cmd, cwd=repo)
    paths = [ln.strip() for ln in out.splitlines() if ln.strip()]
    return [p for p in paths if p.endswith(".md")]


def write_batches(
    label: str,
    paths: list[str],
    *,
    batches_dir: Path,
    max_per_batch: int,
    counter: list[int],
) -> list[Path]:
    """Write batch files; counter[0] is incremented once per batch file written."""
    written: list[Path] = []
    paths = sorted(paths)
    for i in range(0, len(paths), max_per_batch):
        chunk = paths[i : i + max_per_batch]
        counter[0] += 1
        n = counter[0]
        name = f"{label}_{n:03d}.txt"
        batch_path = batches_dir / name
        batch_path.write_text("\n".join(chunk) + "\n", encoding="utf-8")
        written.append(batch_path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate English .md path list and batches for auto-translate catch-up.",
    )
    parser.add_argument(
        "--base",
        default=DEFAULT_BASE,
        help=f"Start commit for git diff (default: {DEFAULT_BASE})",
    )
    parser.add_argument(
        "--head",
        default="HEAD",
        help="End ref for git diff (default: HEAD)",
    )
    parser.add_argument(
        "--repo",
        type=Path,
        default=REPO_ROOT,
        help=(
            "Git repository root; outputs are written under "
            "<repo>/scripts/translation_catchup/generated/"
        ),
    )
    parser.add_argument(
        "--max-per-batch",
        type=int,
        default=40,
        help="Maximum English paths per batch file",
    )
    parser.add_argument(
        "--no-find-renames",
        action="store_true",
        help="Omit --find-renames from git diff",
    )
    args = parser.parse_args()
    repo: Path = args.repo.resolve()

    catchup_dir = repo / "scripts" / "translation_catchup"
    generated = catchup_dir / "generated"
    batches_dir = generated / "batches"
    generated.mkdir(parents=True, exist_ok=True)
    batches_dir.mkdir(parents=True, exist_ok=True)

    paths = git_diff_paths(
        repo, args.base, args.head, find_renames=not args.no_find_renames
    )

    all_paths = generated / "all_paths.txt"
    all_paths.write_text("\n".join(paths) + "\n", encoding="utf-8")

    includes = [p for p in paths if p.startswith("_includes/")]
    user_guide = [p for p in paths if p.startswith("_docs/_user_guide/")]
    other_docs = [p for p in paths if p not in includes and p not in user_guide]

    # Sub-group _user_guide by first segment under _user_guide/
    ug_groups: dict[str, list[str]] = {}
    for p in user_guide:
        parts = p.split("/")
        if len(parts) > 3:
            sub = parts[3]
        else:
            sub = "_root"
        ug_groups.setdefault(sub, []).append(p)

    manifest_lines: list[str] = []
    manifest_lines.append(f"# base={args.base} head={args.head}")
    manifest_lines.append(f"# total_english_md={len(paths)}")
    manifest_lines.append("")

    counter = [0]
    all_batch_paths: list[Path] = []

    # Phase A — includes
    manifest_lines.append("## Phase A — _includes")
    batches = write_batches(
        "phase_a_includes_batch",
        includes,
        batches_dir=batches_dir,
        max_per_batch=args.max_per_batch,
        counter=counter,
    )
    for bp in batches:
        rel = bp.relative_to(repo)
        manifest_lines.append(str(rel))
        all_batch_paths.append(bp)

    # Phase B — _user_guide by subdirectory
    manifest_lines.append("")
    manifest_lines.append("## Phase B — _docs/_user_guide (by subdirectory)")
    for sub in sorted(ug_groups):
        manifest_lines.append(f"### {sub}")
        batches = write_batches(
            f"phase_b_user_guide_{sub}_batch",
            ug_groups[sub],
            batches_dir=batches_dir,
            max_per_batch=args.max_per_batch,
            counter=counter,
        )
        for bp in batches:
            rel = bp.relative_to(repo)
            manifest_lines.append(str(rel))
            all_batch_paths.append(bp)

    # Phase C — remaining _docs
    manifest_lines.append("")
    manifest_lines.append("## Phase C — other _docs")
    batches = write_batches(
        "phase_c_other_docs_batch",
        other_docs,
        batches_dir=batches_dir,
        max_per_batch=args.max_per_batch,
        counter=counter,
    )
    for bp in batches:
        rel = bp.relative_to(repo)
        manifest_lines.append(str(rel))
        all_batch_paths.append(bp)

    manifest_path = batches_dir / "MANIFEST.txt"
    manifest_path.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(paths)} paths to {all_paths.relative_to(repo)}")
    print(f"Wrote {len(all_batch_paths)} batch files under {batches_dir.relative_to(repo)}")
    print(f"Manifest: {manifest_path.relative_to(repo)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
