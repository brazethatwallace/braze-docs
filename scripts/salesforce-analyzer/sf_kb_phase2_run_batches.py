#!/usr/bin/env python3
"""
Phase 2: open PRs by `doc_path` (`gh`, optional Jira).

Reads `kb_articles.csv` (read-only). Skips batches that fail the overlap scan (open/draft/merged
PRs, ``article_id`` claims, ``develop`` content, remote ``sf-cursor-*`` branches). Appends full
``suggested_change`` (strong draft, not shorthand) between HTML markers; commits `_docs/` /
`_includes/` only.

Needs `gh`. Optional: `JIRA_USER_EMAIL`, `JIRA_API_TOKEN`.

Usage:
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --dry-run
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --limit 5
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --doc-path '_docs/.../faq.md'
  python3 scripts/salesforce-analyzer/sf_kb_overlap_scan.py
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = REPO_ROOT / "_data" / "kb_articles.csv"
ASSIGNEES_PATH = REPO_ROOT / ".github" / "support_analyzer_doc_assignees.csv"
REPO = "braze-inc/braze-docs"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_kb_phase1_outputs import doc_path_branch_slug, product_vertical_hint  # noqa: E402
from sf_kb_jira_ticket import (  # noqa: E402
    SUGGESTED_CHANGE_PREFIX_RE,
    build_sf_kb_github_pr_body,
    create_bd6308_task_prep,
    format_sf_kb_pr_title,
    update_bd6308_task_pr_link,
)
from sf_kb_overlap_scan import OverlapScanner, format_scan_summary  # noqa: E402

INTERNAL_TITLE_RE = re.compile(r"\*INTERNAL\*", re.I)
MARKER = "<!-- sf-kb-phase2-batch -->"
END_MARKER = "<!-- /sf-kb-phase2-batch -->"
# Safety cap per backlog row (very large CSV cells are truncated at a paragraph boundary).
MAX_SUGGESTED_CHARS_PER_ROW = 25_000
VAGUE_STARTERS = (
    "might ",
    "may ",
    "consider reviewing",
    "review ",
    "tbd",
    "unclear",
    "needs investigation",
)


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(
            f"Command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stderr or proc.stdout}"
        )
    return proc


def assert_commit_docs_only() -> None:
    """Abort if the last commit touches `_data/`."""
    proc = run(["git", "show", "--name-only", "--format=", "HEAD"], check=True)
    bad = [p for p in proc.stdout.splitlines() if p.strip().startswith("_data/")]
    if bad:
        raise RuntimeError(
            "Phase 2 commit must not include `_data/` files: "
            + ", ".join(bad)
        )


def load_csv_rows() -> list[dict[str, str]]:
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def lookup_assignee(doc_path: str) -> str | None:
    if not ASSIGNEES_PATH.is_file():
        return None
    best_len = -1
    best_user: str | None = None
    with ASSIGNEES_PATH.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            page = (row.get("Page Path") or row.get("page path") or "").strip()
            user = (row.get("GitHub Username") or row.get("github username") or "").strip()
            if not page or not user or user.startswith("@"):
                continue
            if doc_path.startswith(page) and len(page) > best_len:
                best_len = len(page)
                best_user = user
    return best_user


def batch_theme(doc_path: str, rows: list[dict[str, str]]) -> str:
    stem = Path(doc_path).stem.replace("_", " ")
    if "faq" in doc_path.lower():
        return f"{stem} FAQ updates"
    if "troubleshooting" in doc_path.lower():
        return f"{stem} troubleshooting updates"
    return f"{stem} Salesforce KB updates"


def print_overlap_skip(doc_path: str, report) -> None:
    if report.blocked:
        summary = "overlap scan blocked this batch"
    else:
        summary = "overlap scan reported warnings (re-run with --ignore-warnings to proceed)"
    print(f"SKIP {doc_path}: {summary}", file=sys.stderr)
    for line in report.format_lines(indent="  "):
        print(line, file=sys.stderr)


def should_skip_for_overlap(report, *, ignore_warnings: bool) -> bool:
    if report.blocked:
        return True
    return bool(report.warnings) and not ignore_warnings


def is_actionable_row(row: dict[str, str]) -> bool:
    title = (row.get("title") or "").strip()
    if INTERNAL_TITLE_RE.search(title):
        return False
    suggested = (row.get("suggested_change") or "").strip()
    if not suggested:
        return False
    first = suggested.split("\n", 1)[0].strip().lower()
    if any(first.startswith(v) for v in VAGUE_STARTERS):
        return False
    cr = (row.get("conflict_resolution") or "").lower()
    if "human review" in cr or "no source" in cr:
        return False
    return True


def normalized_suggested_change(suggested: str) -> str:
    """Strip common ``suggested_change`` prefixes; cap length."""
    text = (suggested or "").strip()
    text = SUGGESTED_CHANGE_PREFIX_RE.sub("", text).strip().strip("'\"")
    if not text:
        return ""
    if len(text) <= MAX_SUGGESTED_CHARS_PER_ROW:
        return text
    head = text[: MAX_SUGGESTED_CHARS_PER_ROW - 1]
    cut = head.rsplit("\n", 1)[0].rstrip()
    return cut + "\n\n…"


def draft_section(rows: list[dict[str, str]]) -> str:
    """Insert full ``suggested_change`` per row between MARKER / END_MARKER (idempotent re-runs)."""
    blocks: list[str] = []
    for row in rows:
        title = (row.get("title") or "").strip()
        suggested = (row.get("suggested_change") or "").strip()
        if not title or not suggested:
            continue
        body = normalized_suggested_change(suggested)
        if body:
            blocks.append(body)
    inner = "\n\n---\n\n".join(blocks)
    return f"{MARKER}\n\n{inner}\n\n{END_MARKER}\n"


def apply_doc_edit(doc_path: str, rows: list[dict[str, str]]) -> bool:
    full = REPO_ROOT / doc_path
    if not full.is_file():
        print(f"SKIP missing file: {doc_path}", file=sys.stderr)
        return False
    text = full.read_text(encoding="utf-8")
    section = draft_section(rows)
    if MARKER in text:
        if END_MARKER in text:
            pattern = re.compile(
                re.escape(MARKER) + r"[\s\S]*?" + re.escape(END_MARKER),
                re.MULTILINE,
            )
        else:
            # Legacy: open marker only (no END_MARKER)
            pattern = re.compile(
                re.escape(MARKER) + r"[\s\S]*?(?=\n## |\n{% api %}|\Z)",
                re.MULTILINE,
            )
        if pattern.search(text):
            text = pattern.sub(section.rstrip() + "\n", text, count=1)
        else:
            return False
    else:
        text = text.rstrip() + "\n\n" + section
    if text == full.read_text(encoding="utf-8"):
        return False
    full.write_text(text, encoding="utf-8")
    return True


def process_batch(
    doc_path: str,
    rows: list[dict[str, str]],
    *,
    dry_run: bool,
    scanner: OverlapScanner,
    ignore_warnings: bool,
) -> dict | None:
    actionable = [r for r in rows if is_actionable_row(r)]
    skipped_internal = [r for r in rows if r not in actionable]
    if not actionable:
        print(f"SKIP {doc_path}: no actionable rows ({len(skipped_internal)} skipped)", file=sys.stderr)
        return None

    article_ids = [r["article_id"].strip() for r in actionable]
    overlap = scanner.check_batch(doc_path, article_ids)
    if should_skip_for_overlap(overlap, ignore_warnings=ignore_warnings):
        print_overlap_skip(doc_path, overlap)
        return None
    if overlap.warnings:
        print(f"WARN {doc_path}: overlap warnings (continuing)", file=sys.stderr)
        for line in overlap.format_lines(indent="  "):
            print(line, file=sys.stderr)

    theme = batch_theme(doc_path, actionable)
    ymd = datetime.now(timezone.utc).strftime("%Y%m%d")
    branch = f"sf-cursor-{doc_path_branch_slug(doc_path)}-{ymd}"
    assignee = lookup_assignee(doc_path)

    articles = [
        (r["article_id"].strip(), (r.get("title") or "").strip())
        for r in actionable
    ]

    if dry_run:
        print(f"DRY-RUN {doc_path}: {len(actionable)} articles → branch {branch}")
        return {"doc_path": doc_path, "mode": "dry_run", "branch": branch, "articles": articles}

    run(["git", "fetch", "origin", "develop"])
    run(["git", "checkout", "origin/develop", "-B", branch])

    if not apply_doc_edit(doc_path, actionable):
        print(f"SKIP {doc_path}: no edit applied", file=sys.stderr)
        run(["git", "checkout", "develop"], check=False)
        return None

    run(["git", "add", doc_path])
    run(
        [
            "git",
            "commit",
            "-m",
            f"SF KB: {theme}\n\nSalesforce Knowledge batch for `{doc_path}`.",
        ]
    )
    assert_commit_docs_only()
    run(["git", "push", "-u", "origin", branch, "--force-with-lease"])

    issue_key: str | None = None
    pr_title = f"[SF KB] {theme}"
    try:
        issue_key = create_bd6308_task_prep(
            ticket_name=theme,
            articles=articles,
            doc_path=doc_path,
            product_vertical=product_vertical_hint(doc_path),
        )
        pr_title = format_sf_kb_pr_title(issue_key, theme)
    except Exception as exc:  # noqa: BLE001
        print(f"WARN Jira prep failed for {doc_path}: {exc}", file=sys.stderr)

    skipped = [
        (
            r["article_id"].strip(),
            r.get("title", "").strip(),
            "INTERNAL or non-actionable",
        )
        for r in skipped_internal
    ]
    body = build_sf_kb_github_pr_body(
        doc_path=doc_path,
        product_vertical=product_vertical_hint(doc_path),
        articles=articles,
        backlog_rows=actionable,
        skipped=skipped or None,
    )

    pr_cmd = [
        "gh",
        "pr",
        "create",
        "--repo",
        REPO,
        "--base",
        "develop",
        "--head",
        branch,
        "--title",
        pr_title,
        "--body",
        body,
        "--label",
        "salesforce migration",
    ]
    if assignee:
        pr_cmd.extend(["--assignee", assignee])
    pr_proc = run(pr_cmd)
    pr_url = (pr_proc.stdout or "").strip().splitlines()[-1]

    if issue_key:
        try:
            update_bd6308_task_pr_link(
                issue_key,
                pr_url=pr_url,
                pr_title=pr_title,
                articles=articles,
                doc_path=doc_path,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"WARN Jira link update failed: {exc}", file=sys.stderr)

    return {
        "doc_path": doc_path,
        "mode": "opened",
        "pr_url": pr_url,
        "jira": issue_key,
        "branch": branch,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="Max batches (0 = all)")
    parser.add_argument("--doc-path", action="append", default=[], help="Only this doc_path")
    parser.add_argument(
        "--ignore-warnings",
        action="store_true",
        help="Open PRs even when overlap scan reports non-blocking warnings",
    )
    args = parser.parse_args()

    csv_rows = load_csv_rows()

    pending: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in csv_rows:
        dp = (row.get("doc_path") or "").strip()
        if not dp:
            continue
        if args.doc_path and dp not in args.doc_path:
            continue
        pending[dp].append(row)

    scanner = OverlapScanner()
    scanner.refresh()
    if scanner.available:
        print(format_scan_summary(
            scanner.scan_batches(
                [
                    (
                        doc_path,
                        [r["article_id"].strip() for r in rows if is_actionable_row(r)],
                    )
                    for doc_path, rows in pending.items()
                ]
            )
        ))
    else:
        print(f"WARN overlap scan unavailable: {scanner.error}", file=sys.stderr)

    batches = sorted(pending.items(), key=lambda kv: -len(kv[1]))
    opened = 0

    for doc_path, rows in batches:
        if args.limit and opened >= args.limit:
            break
        result = process_batch(
            doc_path,
            rows,
            dry_run=args.dry_run,
            scanner=scanner,
            ignore_warnings=args.ignore_warnings,
        )
        if not result:
            continue
        if result.get("mode") == "opened":
            opened += 1
            print(f"OK {doc_path} → {result.get('pr_url')} ({result.get('jira')})")

    print(f"Done. {opened} PR(s) opened.")


if __name__ == "__main__":
    main()
