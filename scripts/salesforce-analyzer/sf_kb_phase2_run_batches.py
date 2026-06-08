#!/usr/bin/env python3
"""
Run Salesforce KB Phase 2 for all pending PR batches (grouped by doc_path).

For each primary `_docs/...` file with backlog rows not yet in `_data/kb_epic_bd6308.txt`:
  1. Skip if an open `salesforce migration` PR already modifies that file (tracker sync only).
  2. Append FAQ-style sections from CSV `suggested_change` (skips INTERNAL titles, empty briefs).
  3. Branch, commit, push, open PR (title `[BD-####](SF) …` when Jira succeeds).
  4. Remove actioned `article_id` values from `_data/kb_articles.csv` and append to epic tracker.

Requires: `gh` authenticated, optional JIRA_USER_EMAIL + JIRA_API_TOKEN for Jira tasks.

Usage (repo root):
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --dry-run
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --limit 5
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --doc-path '_docs/.../faq.md'
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --sync-open-prs-only
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
EPIC_PATH = REPO_ROOT / "_data" / "kb_epic_bd6308.txt"
ASSIGNEES_PATH = REPO_ROOT / ".github" / "support_analyzer_doc_assignees.csv"
REPO = "braze-inc/braze-docs"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_kb_phase1_outputs import doc_path_branch_slug, product_vertical_hint  # noqa: E402
from sf_kb_jira_ticket import (  # noqa: E402
    create_bd6308_task_prep,
    format_sf_kb_pr_title,
    load_kb_article_titles,
    update_bd6308_task_pr_link,
)

ARTICLE_ID_RE = re.compile(r"`(ka[^`]+)`")
INTERNAL_TITLE_RE = re.compile(r"\*INTERNAL\*", re.I)
MARKER = "<!-- sf-kb-phase2-batch -->"
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


def load_epic_ids() -> set[str]:
    if not EPIC_PATH.is_file():
        return set()
    return {
        line.strip()
        for line in EPIC_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def load_csv_rows() -> tuple[list[str], list[dict[str, str]]]:
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        return fieldnames, list(reader)


def write_csv(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)


def append_epic_ids(new_ids: set[str]) -> None:
    header: list[str] = []
    body: list[str] = []
    in_header = True
    for line in EPIC_PATH.read_text(encoding="utf-8").splitlines():
        if in_header and (line.startswith("#") or not line.strip()):
            header.append(line)
            continue
        in_header = False
        if line.strip():
            body.append(line.strip())
    merged = sorted(set(body) | new_ids)
    EPIC_PATH.write_text("\n".join(header + [""] + merged) + "\n", encoding="utf-8")


def lookup_assignee(doc_path: str) -> str | None:
    if not ASSIGNEES_PATH.is_file():
        return None
    best_len = -1
    best_user: str | None = None
    with ASSIGNEES_PATH.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            page = (row.get("page path") or "").strip()
            user = (row.get("GitHub Username") or "").strip()
            if not page or not user or user.startswith("@"):
                continue
            if doc_path.startswith(page) and len(page) > best_len:
                best_len = len(page)
                best_user = user
    return best_user


def open_pr_paths() -> dict[str, list[int]]:
    proc = run(
        [
            "gh",
            "pr",
            "list",
            "--repo",
            REPO,
            "--state",
            "open",
            "--label",
            "salesforce migration",
            "--limit",
            "100",
            "--json",
            "number,files",
        ]
    )
    out: dict[str, list[int]] = defaultdict(list)
    for pr in __import__("json").loads(proc.stdout or "[]"):
        num = pr["number"]
        for f in pr.get("files") or []:
            path = f.get("path") or ""
            if path.startswith("_docs/") or path.startswith("_includes/"):
                out[path].append(num)
    return out


def open_pr_article_ids() -> dict[str, list[int]]:
    proc = run(
        [
            "gh",
            "pr",
            "list",
            "--repo",
            REPO,
            "--state",
            "open",
            "--label",
            "salesforce migration",
            "--limit",
            "100",
            "--json",
            "number",
        ]
    )
    mapping: dict[str, list[int]] = defaultdict(list)
    for pr in __import__("json").loads(proc.stdout or "[]"):
        num = pr["number"]
        body_proc = run(["gh", "pr", "view", str(num), "--repo", REPO, "--json", "body"])
        body = __import__("json").loads(body_proc.stdout).get("body") or ""
        for aid in ARTICLE_ID_RE.findall(body):
            mapping[aid].append(num)
    return mapping


def batch_theme(doc_path: str, rows: list[dict[str, str]]) -> str:
    stem = Path(doc_path).stem.replace("_", " ")
    if "faq" in doc_path.lower():
        return f"{stem} FAQ updates"
    if "troubleshooting" in doc_path.lower():
        return f"{stem} troubleshooting updates"
    return f"{stem} Salesforce KB updates"


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


def draft_section(rows: list[dict[str, str]]) -> str:
    lines = [MARKER, "", "## Salesforce Knowledge updates", ""]
    for row in rows:
        title = (row.get("title") or "").strip()
        suggested = (row.get("suggested_change") or "").strip()
        if not title or not suggested:
            continue
        # Use first paragraph / sentence of suggested_change as body.
        body = suggested.split("\n\n", 1)[0].strip()
        body = re.sub(r"^Add (to|documentation for)\s+[^:]{0,120}:\s*", "", body, flags=re.I)
        body = body.strip("'\"")
        if len(body) > 600:
            body = body[:597].rstrip() + "…"
        lines.extend([f"### {title}", "", body, ""])
    return "\n".join(lines).rstrip() + "\n"


def apply_doc_edit(doc_path: str, rows: list[dict[str, str]]) -> bool:
    full = REPO_ROOT / doc_path
    if not full.is_file():
        print(f"SKIP missing file: {doc_path}", file=sys.stderr)
        return False
    text = full.read_text(encoding="utf-8")
    section = draft_section(rows)
    if MARKER in text:
        # Replace existing batch block
        pattern = re.compile(
            re.escape(MARKER) + r"[\s\S]*?(?=\n## |\n{% api %}|\Z)",
            re.MULTILINE,
        )
        if pattern.search(text):
            text = pattern.sub(section.rstrip() + "\n\n", text, count=1)
        else:
            return False
    else:
        text = text.rstrip() + "\n\n" + section
    if text == full.read_text(encoding="utf-8"):
        return False
    full.write_text(text, encoding="utf-8")
    return True


def sync_from_open_prs(
    *,
    epic_ids: set[str],
    csv_rows: list[dict[str, str]],
    dry_run: bool,
) -> set[str]:
    """Move article IDs referenced in open SF migration PRs into epic tracker."""
    pr_ids = open_pr_article_ids()
    synced: set[str] = set()
    for aid in pr_ids:
        if aid in epic_ids:
            continue
        if any(r.get("article_id", "").strip() == aid for r in csv_rows):
            synced.add(aid)
    if synced and not dry_run:
        append_epic_ids(synced)
    return synced


def process_batch(
    doc_path: str,
    rows: list[dict[str, str]],
    *,
    dry_run: bool,
    open_paths: dict[str, list[int]],
) -> dict | None:
    actionable = [r for r in rows if is_actionable_row(r)]
    skipped_internal = [r for r in rows if r not in actionable]
    if not actionable:
        print(f"SKIP {doc_path}: no actionable rows ({len(skipped_internal)} skipped)", file=sys.stderr)
        return None

    if doc_path in open_paths:
        prs = open_paths[doc_path]
        print(
            f"SYNC-ONLY {doc_path}: open PR(s) {prs} already touch file; "
            f"action {len(actionable)} articles via tracker when --sync-open-prs-only",
            file=sys.stderr,
        )
        return {
            "doc_path": doc_path,
            "mode": "sync_only",
            "article_ids": [r["article_id"].strip() for r in actionable],
            "open_prs": prs,
        }

    theme = batch_theme(doc_path, actionable)
    ymd = datetime.now(timezone.utc).strftime("%Y%m%d")
    branch = f"sf-cursor-{doc_path_branch_slug(doc_path)}-{ymd}"
    assignee = lookup_assignee(doc_path) or "lydia-xie"

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

    body_lines = [
        "## Product vertical",
        "",
        product_vertical_hint(doc_path),
        "",
        "## Changes",
        "",
        f"* `{doc_path}` — Salesforce Knowledge batch ({len(actionable)} article(s))",
        "",
        "## Salesforce Knowledge sources",
        "",
    ]
    titles = load_kb_article_titles()
    for aid, fallback in articles:
        ttl = titles.get(aid, fallback)
        body_lines.append(f"* `{aid}` — {ttl}")
    if skipped_internal:
        body_lines.extend(["", "## Skipped in this PR", ""])
        for r in skipped_internal:
            body_lines.append(
                f"* `{r['article_id'].strip()}` — {r.get('title', '').strip()} (INTERNAL or non-actionable)"
            )
    body_lines.extend(
        [
            "",
            "## Test plan",
            "",
            "- [ ] Preview changed page on a local docs build",
            "- [ ] Confirm prose against Braze Docs style guide",
            "",
            "Made with [Cursor](https://cursor.com)",
        ]
    )
    body = "\n".join(body_lines)

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
        "--assignee",
        assignee,
    ]
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

    actioned_ids = {aid for aid, _ in articles}
    return {
        "doc_path": doc_path,
        "mode": "opened",
        "pr_url": pr_url,
        "jira": issue_key,
        "article_ids": sorted(actioned_ids),
        "branch": branch,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="Max batches to open (0 = all)")
    parser.add_argument("--doc-path", action="append", default=[], help="Process only this doc_path")
    parser.add_argument(
        "--sync-open-prs-only",
        action="store_true",
        help="Only sync epic tracker from open PR article IDs; do not open new PRs",
    )
    args = parser.parse_args()

    fieldnames, csv_rows = load_csv_rows()
    epic_ids = load_epic_ids()

    if args.sync_open_prs_only or not args.dry_run:
        synced = sync_from_open_prs(epic_ids=epic_ids, csv_rows=csv_rows, dry_run=args.dry_run)
        if synced:
            epic_ids |= synced
            if not args.dry_run:
                csv_rows = [r for r in csv_rows if r.get("article_id", "").strip() not in synced]
                write_csv(fieldnames, csv_rows)
            print(f"Synced {len(synced)} article_id(s) from open PR bodies into epic tracker.")

    if args.sync_open_prs_only:
        run(["python3", "scripts/salesforce-analyzer/generate_kb_phase1_outputs.py", "--no-prune"])
        return

    pending: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in csv_rows:
        aid = (row.get("article_id") or "").strip()
        if aid in epic_ids:
            continue
        dp = (row.get("doc_path") or "").strip()
        if not dp:
            continue
        if args.doc_path and dp not in args.doc_path:
            continue
        pending[dp].append(row)

    open_paths = open_pr_paths()
    batches = sorted(pending.items(), key=lambda kv: -len(kv[1]))
    results: list[dict] = []
    opened = 0

    for doc_path, rows in batches:
        if args.limit and opened >= args.limit:
            break
        result = process_batch(doc_path, rows, dry_run=args.dry_run, open_paths=open_paths)
        if not result:
            continue
        results.append(result)
        if result.get("mode") in ("opened", "sync_only") and not args.dry_run:
            actioned = set(result["article_ids"])
            append_epic_ids(actioned)
            csv_rows = [r for r in csv_rows if r.get("article_id", "").strip() not in actioned]
            write_csv(fieldnames, csv_rows)
            if result.get("mode") == "opened":
                opened += 1
                print(f"OK {doc_path} → {result.get('pr_url')} ({result.get('jira')})")
            else:
                print(f"SYNC {doc_path}: {len(actioned)} article(s) → epic (open PR {result.get('open_prs')})")

    if not args.dry_run:
        run(["python3", "scripts/salesforce-analyzer/generate_kb_phase1_outputs.py", "--no-prune"])

    print(f"\nDone. Processed {len(results)} batch(es); opened {opened} new PR(s).")


if __name__ == "__main__":
    main()
