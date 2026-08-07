#!/usr/bin/env python3
"""
Phase 2: prepare Salesforce KB batches, then open PRs after polish (`gh`, optional Jira).

Reads `kb_articles.csv` (read-only). Skips batches that fail the overlap scan (open/draft/merged
PRs, ``article_id`` claims, ``develop`` content, remote ``sf-cursor-*`` branches).

**Default (`--prepare`):** requires reference-repo verification proof for `inconclusive`
articles **before** bulk-inserting CSV draft text (use `--verify-only` to check first).

**`--open-pr`:** validate polished docs (no phase-2 markers), push branch, open **draft** PR.

Needs `gh`. Optional: `JIRA_USER_EMAIL`, `JIRA_API_TOKEN`.

Usage:
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --verify-only --doc-path '_docs/.../faq.md'
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --prepare --doc-path '_docs/.../faq.md' \\
    --verification-file '.sf-kb-verification-faqs.md'
  python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --open-pr --doc-path '_docs/.../faq.md' \\
    --verification-file '.sf-kb-verification-faqs.md'
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
REPO = "braze-inc/braze-docs"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_kb_phase1_outputs import doc_path_branch_slug, infer_product_vertical_label  # noqa: E402
from sf_kb_article_ids import article_id_column, article_id_from_row  # noqa: E402
from sf_kb_assignees import assignees_for_doc_path  # noqa: E402
from sf_kb_jira_ticket import (  # noqa: E402
    SUGGESTED_CHANGE_PREFIX_RE,
    batch_has_reference_verify_rows,
    build_sf_kb_github_pr_body,
    create_bd6308_task_prep,
    format_sf_kb_pr_title,
    format_verification_required_message,
    pending_verification_titles,
    update_bd6308_task_pr_link,
)
from sf_kb_overlap_scan import OverlapScanner, format_scan_summary  # noqa: E402
from sf_kb_reference_verify import (  # noqa: E402
    format_reference_verify_report,
    merge_verification_lines,
    pull_reference_repo,
    verify_batch_references,
)
from sf_kb_suggested_change import (  # noqa: E402
    PHASE2_BATCH_END_MARKER,
    PHASE2_BATCH_MARKER,
    is_vague_suggested_change,
    validate_ship_ready_markdown,
)

INTERNAL_TITLE_RE = re.compile(r"\*INTERNAL\*", re.I)
MARKER = PHASE2_BATCH_MARKER
END_MARKER = PHASE2_BATCH_END_MARKER
# Safety cap per backlog row (very large CSV cells are truncated at a paragraph boundary).
MAX_SUGGESTED_CHARS_PER_ROW = 25_000
POLISH_INSTRUCTIONS = (
    "Next: replace the marker block with ship-ready prose (headings, links, style guide), "
    "then run --open-pr with the same --verification-file."
)


def read_verification_file(path: Path) -> list[str]:
    lines: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lines.append(stripped.lstrip("- ").strip())
    return lines


def default_verification_file_candidates(doc_path: str) -> list[Path]:
    slug = doc_path_branch_slug(doc_path)
    return [
        REPO_ROOT / f".sf-kb-verification-{slug}.md",
        REPO_ROOT / ".sf-kb-verification.md",
    ]


def load_verification_lines(
    *,
    inline: list[str],
    verification_file: str | None,
    doc_path: str | None = None,
) -> list[str]:
    lines = [item.strip() for item in inline if item.strip()]
    if verification_file:
        path = Path(verification_file)
        if not path.is_file():
            raise RuntimeError(f"Verification file not found: {verification_file}")
        lines.extend(read_verification_file(path))
        return lines
    if doc_path:
        for candidate in default_verification_file_candidates(doc_path):
            if candidate.is_file():
                lines.extend(read_verification_file(candidate))
                break
    return lines


def write_verification_file(path: Path, lines: list[str]) -> None:
    body = "\n".join(
        [
            "# Salesforce KB reference-repo verification (auto-generated)",
            "",
            *(f"- {line.lstrip('- ').strip()}" for line in lines if line.strip()),
        ]
    )
    path.write_text(body + "\n", encoding="utf-8")


def run_reference_verification(
    doc_path: str,
    actionable: list[dict[str, str]],
    verification_lines: list[str],
    *,
    require_verification: bool,
    pull_repos: bool,
    write_verification: bool,
    dry_run: bool,
) -> tuple[list[str], bool]:
    """
    Resolve CSV ``codebase_evidence`` against sibling repos; merge auto bullets.

    Returns ``(merged_verification_lines, ok_to_proceed)``.
    """
    if pull_repos and not dry_run:
        pull_err = pull_reference_repo("platform")
        if pull_err:
            print(f"WARN {pull_err}", file=sys.stderr)

    ref = verify_batch_references(
        actionable,
        require_inconclusive=require_verification,
        verification_lines=verification_lines,
    )
    for line in format_reference_verify_report(ref):
        if line.startswith("BLOCK"):
            print(line, file=sys.stderr)
        else:
            print(line)

    merged = merge_verification_lines(verification_lines, ref.auto_bullets)

    if write_verification and merged and not dry_run:
        out_path = default_verification_file_candidates(doc_path)[0]
        if not out_path.is_file():
            write_verification_file(out_path, merged)
            print(f"Wrote {out_path.relative_to(REPO_ROOT)}")

    if require_verification:
        if ref.blocking_errors:
            print(
                f"SKIP {doc_path}: fix reference-repo verification before drafting content.",
                file=sys.stderr,
            )
            return merged, False
        if batch_has_reference_verify_rows(actionable):
            pending = pending_verification_titles(actionable, verification_lines=merged)
            if pending:
                slug = doc_path_branch_slug(doc_path)
                print(format_verification_required_message(doc_path, pending, slug=slug), file=sys.stderr)
                print(
                    f"SKIP {doc_path}: fix reference-repo verification before drafting content.",
                    file=sys.stderr,
                )
                return merged, False
    return merged, True


def check_batch_verification(
    doc_path: str,
    actionable: list[dict[str, str]],
    *,
    verification_lines: list[str],
    require_verification: bool,
) -> bool:
    """
    Return True when the batch may proceed; print guidance and return False when blocked.
    """
    if not batch_has_reference_verify_rows(actionable):
        return True
    pending = pending_verification_titles(actionable, verification_lines=verification_lines)
    if not pending:
        return True
    slug = doc_path_branch_slug(doc_path)
    message = format_verification_required_message(doc_path, pending, slug=slug)
    if require_verification:
        print(f"SKIP {message}", file=sys.stderr)
        return False
    print(f"WARN {message}", file=sys.stderr)
    return True


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(
            f"Command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stderr or proc.stdout}"
        )
    return proc


def current_branch() -> str:
    proc = run(["git", "branch", "--show-current"])
    return (proc.stdout or "").strip()


def assert_commit_docs_only() -> None:
    """Abort if the last commit touches `_data/`."""
    proc = run(["git", "show", "--name-only", "--format=", "HEAD"], check=True)
    bad = [p for p in proc.stdout.splitlines() if p.strip().startswith("_data/")]
    if bad:
        raise RuntimeError(
            "Phase 2 commit must not include `_data/` files: "
            + ", ".join(bad)
        )


def load_csv_rows() -> tuple[list[dict[str, str]], str | None]:
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        id_column = article_id_column(reader.fieldnames)
        return list(reader), id_column


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
    if is_vague_suggested_change(suggested):
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


def batch_context(
    doc_path: str,
    rows: list[dict[str, str]],
    *,
    id_column: str | None,
    scanner: OverlapScanner,
    ignore_warnings: bool,
) -> dict | None:
    actionable = [r for r in rows if is_actionable_row(r)]
    skipped_internal = [r for r in rows if r not in actionable]
    if not actionable:
        print(f"SKIP {doc_path}: no actionable rows ({len(skipped_internal)} skipped)", file=sys.stderr)
        return None

    article_ids = [article_id_from_row(r, id_column=id_column) for r in actionable]
    article_ids = [aid for aid in article_ids if aid]
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
    doc_assignees = assignees_for_doc_path(doc_path)

    articles = [
        (article_id_from_row(r, id_column=id_column), (r.get("title") or "").strip())
        for r in actionable
        if article_id_from_row(r, id_column=id_column)
    ]

    skipped = [
        (
            article_id_from_row(r, id_column=id_column),
            r.get("title", "").strip(),
            "INTERNAL or non-actionable",
        )
        for r in skipped_internal
        if article_id_from_row(r, id_column=id_column)
    ]

    return {
        "doc_path": doc_path,
        "actionable": actionable,
        "articles": articles,
        "branch": branch,
        "theme": theme,
        "assignees": doc_assignees,
        "skipped": skipped,
    }


def prepare_batch(
    doc_path: str,
    rows: list[dict[str, str]],
    *,
    id_column: str | None,
    dry_run: bool,
    scanner: OverlapScanner,
    ignore_warnings: bool,
    verification_lines: list[str],
    require_verification: bool,
    pull_repos: bool,
    write_verification: bool,
) -> dict | None:
    ctx = batch_context(
        doc_path,
        rows,
        id_column=id_column,
        scanner=scanner,
        ignore_warnings=ignore_warnings,
    )
    if not ctx:
        return None

    verification_lines, ref_ok = run_reference_verification(
        doc_path,
        ctx["actionable"],
        verification_lines,
        require_verification=require_verification,
        pull_repos=pull_repos,
        write_verification=write_verification,
        dry_run=dry_run,
    )
    if not ref_ok:
        return None

    if not check_batch_verification(
        doc_path,
        ctx["actionable"],
        verification_lines=verification_lines,
        require_verification=require_verification,
    ):
        return None

    if dry_run:
        pending = pending_verification_titles(
            ctx["actionable"], verification_lines=verification_lines
        )
        verify_note = (
            f", {len(pending)} article(s) still need verification proof"
            if pending
            else ", verification proof OK"
        )
        print(
            f"DRY-RUN {doc_path}: {len(ctx['actionable'])} articles → branch {ctx['branch']} "
            f"(prepare{verify_note})"
        )
        return {"doc_path": doc_path, "mode": "dry_run", "branch": ctx["branch"], "articles": ctx["articles"]}

    run(["git", "fetch", "origin", "develop"])
    run(["git", "checkout", "origin/develop", "-B", ctx["branch"]])

    if not apply_doc_edit(doc_path, ctx["actionable"]):
        print(f"SKIP {doc_path}: no edit applied", file=sys.stderr)
        run(["git", "checkout", "develop"], check=False)
        return None

    run(["git", "add", doc_path])
    run(
        [
            "git",
            "commit",
            "-m",
            f"SF KB (prepare): {ctx['theme']}\n\n"
            f"Bulk insert for `{doc_path}`. Polish before opening PR.",
        ]
    )
    assert_commit_docs_only()

    print(f"PREPARED {doc_path} on {ctx['branch']}")
    print(f"  {POLISH_INSTRUCTIONS}")
    return {
        "doc_path": doc_path,
        "mode": "prepared",
        "branch": ctx["branch"],
    }


def assert_ship_ready_doc(doc_path: str) -> None:
    full = REPO_ROOT / doc_path
    if not full.is_file():
        raise RuntimeError(f"Missing doc file: {doc_path}")
    errors = validate_ship_ready_markdown(full.read_text(encoding="utf-8"))
    if errors:
        raise RuntimeError(
            f"{doc_path} is not ship-ready for a public PR: " + "; ".join(errors)
        )


def publish_batch(
    doc_path: str,
    rows: list[dict[str, str]],
    *,
    id_column: str | None,
    dry_run: bool,
    scanner: OverlapScanner,
    ignore_warnings: bool,
    verification_lines: list[str],
    require_verification: bool,
    pull_repos: bool,
    write_verification: bool,
) -> dict | None:
    ctx = batch_context(
        doc_path,
        rows,
        id_column=id_column,
        scanner=scanner,
        ignore_warnings=ignore_warnings,
    )
    if not ctx:
        return None

    verification_lines, ref_ok = run_reference_verification(
        doc_path,
        ctx["actionable"],
        verification_lines,
        require_verification=require_verification,
        pull_repos=pull_repos,
        write_verification=write_verification,
        dry_run=dry_run,
    )
    if not ref_ok:
        return None

    if not check_batch_verification(
        doc_path,
        ctx["actionable"],
        verification_lines=verification_lines,
        require_verification=require_verification,
    ):
        return None

    branch = current_branch()
    if not branch.startswith("sf-cursor-"):
        print(
            f"SKIP {doc_path}: checkout the prepared sf-cursor-* branch before --open-pr "
            f"(current: {branch or 'detached'})",
            file=sys.stderr,
        )
        return None

    try:
        assert_ship_ready_doc(doc_path)
    except RuntimeError as exc:
        print(f"SKIP {doc_path}: {exc}", file=sys.stderr)
        print(f"  {POLISH_INSTRUCTIONS}", file=sys.stderr)
        return None

    pending = pending_verification_titles(ctx["actionable"], verification_lines=verification_lines)
    if pending and not require_verification:
        print(
            f"WARN {doc_path}: opening PR with incomplete verification for: "
            + "; ".join(pending),
            file=sys.stderr,
        )

    if dry_run:
        print(f"DRY-RUN {doc_path}: ship-ready on {branch} → would open PR")
        return {"doc_path": doc_path, "mode": "dry_run", "branch": branch, "articles": ctx["articles"]}

    proc = run(["git", "status", "--porcelain", doc_path], check=True)
    if proc.stdout.strip():
        run(["git", "add", doc_path])
        run(
            [
                "git",
                "commit",
                "-m",
                f"SF KB: {ctx['theme']}\n\n"
                f"Ship-ready Salesforce Knowledge batch for `{doc_path}`.",
            ]
        )
        assert_commit_docs_only()

    run(["git", "push", "-u", "origin", branch, "--force-with-lease"])

    issue_key: str | None = None
    pr_title = f"[SF KB] {ctx['theme']}"
    try:
        issue_key = create_bd6308_task_prep(
            ticket_name=ctx["theme"],
            articles=ctx["articles"],
            doc_path=doc_path,
            product_vertical=infer_product_vertical_label(doc_path),
            assignee_account_id=ctx["assignees"].jira_account_id,
        )
        pr_title = format_sf_kb_pr_title(issue_key, ctx["theme"])
    except Exception as exc:  # noqa: BLE001
        print(f"WARN Jira prep failed for {doc_path}: {exc}", file=sys.stderr)

    body = build_sf_kb_github_pr_body(
        doc_path=doc_path,
        product_vertical=infer_product_vertical_label(doc_path),
        articles=ctx["articles"],
        backlog_rows=ctx["actionable"],
        skipped=ctx["skipped"] or None,
        verification_lines=verification_lines or None,
    )

    pr_cmd = [
        "gh",
        "pr",
        "create",
        "--draft",
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
    if ctx["assignees"].github_username:
        pr_cmd.extend(["--assignee", ctx["assignees"].github_username])
    pr_proc = run(pr_cmd)
    pr_url = (pr_proc.stdout or "").strip().splitlines()[-1]

    if issue_key:
        try:
            update_bd6308_task_pr_link(
                issue_key,
                pr_url=pr_url,
                pr_title=pr_title,
                articles=ctx["articles"],
                doc_path=doc_path,
                assignee_account_id=ctx["assignees"].jira_account_id,
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


def verify_batch(
    doc_path: str,
    rows: list[dict[str, str]],
    *,
    verification_lines: list[str],
    require_verification: bool,
    pull_repos: bool,
    write_verification: bool,
    dry_run: bool,
) -> str:
    """
    Print reference-repo verification status for a batch.

    Returns ``ok``, ``skip`` (no actionable rows), or ``fail`` (proof incomplete).
    Does not run overlap scan — verify-only checks proof, not batch eligibility.
    """
    actionable = [r for r in rows if is_actionable_row(r)]
    skipped_count = len(rows) - len(actionable)
    if not actionable:
        print(
            f"SKIP {doc_path}: no actionable rows ({skipped_count} skipped) — "
            "reference-repo verification not applicable.",
            file=sys.stderr,
        )
        return "skip"

    verification_lines, ref_ok = run_reference_verification(
        doc_path,
        actionable,
        verification_lines,
        require_verification=require_verification,
        pull_repos=pull_repos,
        write_verification=write_verification,
        dry_run=dry_run,
    )
    if not ref_ok:
        return "fail"

    if not batch_has_reference_verify_rows(actionable):
        print(f"OK {doc_path}: no `inconclusive` articles — reference-repo proof not required before prepare.")
        return "ok"

    pending = pending_verification_titles(actionable, verification_lines=verification_lines)
    slug = doc_path_branch_slug(doc_path)
    if not pending:
        print(f"OK {doc_path}: reference-repo verification proof recorded for all inconclusive articles.")
        return "ok"

    print(format_verification_required_message(doc_path, pending, slug=slug), file=sys.stderr)
    if require_verification:
        return "fail"
    print(f"WARN {doc_path}: proceeding with --allow-incomplete-verification.", file=sys.stderr)
    return "ok"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="Max batches (0 = all)")
    parser.add_argument("--doc-path", action="append", default=[], help="Only this doc_path")
    parser.add_argument(
        "--ignore-warnings",
        action="store_true",
        help="Proceed even when overlap scan reports non-blocking warnings",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--verify-only",
        action="store_true",
        help="Check reference-repo verification proof before prepare (requires --doc-path)",
    )
    mode.add_argument(
        "--prepare",
        action="store_true",
        help="Create branch and bulk-insert markers locally (default when other modes omitted)",
    )
    mode.add_argument(
        "--open-pr",
        action="store_true",
        help="Push ship-ready branch and open PR (requires polished prose; use with --doc-path)",
    )
    parser.add_argument(
        "--verification",
        action="append",
        default=[],
        metavar="LINE",
        help="Verification proof bullet (repeatable). Example: "
        "'Verified delayed-send alerts in `platform/.../rate_limit_mailer.rb`'",
    )
    parser.add_argument(
        "--verification-file",
        help="Markdown file with one verification bullet per line (lines starting with # ignored)",
    )
    parser.add_argument(
        "--allow-incomplete-verification",
        action="store_true",
        help="Allow --prepare/--open-pr when inconclusive articles lack explicit verification proof "
        "(draft will list incomplete checklist items)",
    )
    parser.add_argument(
        "--pull-reference-repos",
        action="store_true",
        help="Run `git pull --ff-only` in ../platform before reference verification",
    )
    parser.add_argument(
        "--write-verification",
        action="store_true",
        help="Write `.sf-kb-verification-<slug>.md` when auto-generated bullets are produced",
    )
    args = parser.parse_args()
    verify_only = args.verify_only
    open_pr = args.open_pr
    require_verification = not args.allow_incomplete_verification

    csv_rows, id_column = load_csv_rows()

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
                        [
                            article_id_from_row(r, id_column=id_column)
                            for r in rows
                            if is_actionable_row(r) and article_id_from_row(r, id_column=id_column)
                        ],
                    )
                    for doc_path, rows in pending.items()
                ]
            )
        ))
    else:
        print(f"WARN overlap scan unavailable: {scanner.error}", file=sys.stderr)

    if (verify_only or open_pr) and not args.doc_path:
        parser.error("--verify-only and --open-pr require at least one --doc-path")

    batches = sorted(pending.items(), key=lambda kv: -len(kv[1]))
    completed = 0
    if verify_only:
        result_label = "batch(es) verified"
    elif open_pr:
        result_label = "draft PR(s) opened"
    else:
        result_label = "batch(es) prepared"
    blocked = 0

    for doc_path, rows in batches:
        if args.limit and completed >= args.limit:
            break
        try:
            verification_lines = load_verification_lines(
                inline=args.verification,
                verification_file=args.verification_file,
                doc_path=doc_path,
            )
        except RuntimeError as exc:
            parser.error(str(exc))

        if verify_only:
            outcome = verify_batch(
                doc_path,
                rows,
                verification_lines=verification_lines,
                require_verification=require_verification,
                pull_repos=args.pull_reference_repos,
                write_verification=args.write_verification,
                dry_run=args.dry_run,
            )
            if outcome == "ok":
                completed += 1
            elif outcome == "fail":
                blocked += 1
            continue
        if open_pr:
            result = publish_batch(
                doc_path,
                rows,
                id_column=id_column,
                dry_run=args.dry_run,
                scanner=scanner,
                ignore_warnings=args.ignore_warnings,
                verification_lines=verification_lines,
                require_verification=require_verification,
                pull_repos=args.pull_reference_repos,
                write_verification=args.write_verification,
            )
        else:
            result = prepare_batch(
                doc_path,
                rows,
                id_column=id_column,
                dry_run=args.dry_run,
                scanner=scanner,
                ignore_warnings=args.ignore_warnings,
                verification_lines=verification_lines,
                require_verification=require_verification,
                pull_repos=args.pull_reference_repos,
                write_verification=args.write_verification,
            )
        if not result:
            continue
        if result.get("mode") in {"opened", "prepared"}:
            completed += 1
            if result.get("mode") == "opened":
                print(f"OK {doc_path} → {result.get('pr_url')} ({result.get('jira')})")

    if verify_only and blocked:
        print(f"Done. {completed} {result_label}; {blocked} blocked (add verification proof first).", file=sys.stderr)
        sys.exit(1)
    print(f"Done. {completed} {result_label}.")


if __name__ == "__main__":
    main()
