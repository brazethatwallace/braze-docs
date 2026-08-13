#!/usr/bin/env python3
"""
Phase 2: apply support_analyzer_phase2_rules.yml to the Support Cases CSV and
open one draft PR per rule that matches enough cases and has pending edits.

Designed for GitHub Actions after the Looker CSV export. Does not send case
text to external APIs.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from collections.abc import Iterable
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

_PHASE2_BRANCH_TZ = ZoneInfo("America/New_York")

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise SystemExit("PyYAML is required: pip install pyyaml") from e


CASE_ID_COL = "Support Cases Email Message Case ID"

# GitHub username: alphanumeric, single internal hyphens, 1–39 chars (conservative).
_GH_LOGIN_RE = re.compile(r"^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$")

# Rule ids become git ref segments; reject characters that break branch/PR creation.
_RULE_ID_RE = re.compile(r"^[a-zA-Z0-9](?:[a-zA-Z0-9_-]{0,126}[a-zA-Z0-9])?$")

_DOCS_DIR_PREFIX = "_docs/"


def _normalize_repo_relative_path(rel: str) -> str:
    return rel.strip().replace("\\", "/")


def _validate_docs_relative_path(rel: str, *, context: str) -> str:
    """Ensure edit targets stay under `_docs/` with no traversal."""
    norm = _normalize_repo_relative_path(rel)
    if not norm:
        raise SystemExit(f"{context}: empty file path")
    if norm.startswith("/") or Path(norm).is_absolute():
        raise SystemExit(f"{context}: absolute paths are not allowed: {rel!r}")
    if ".." in Path(norm).parts:
        raise SystemExit(f"{context}: path traversal is not allowed: {rel!r}")
    if not norm.startswith(_DOCS_DIR_PREFIX):
        raise SystemExit(f"{context}: path must be under {_DOCS_DIR_PREFIX!r}: {rel!r}")
    return norm


def _validate_rule_edit_paths(rule: dict[str, Any], rule_id: str) -> None:
    edits = rule.get("edits") or []
    for i, edit in enumerate(edits):
        rel = edit.get("file")
        if not rel:
            raise SystemExit(f"rule {rule_id}: edits[{i}] missing file")
        _validate_docs_relative_path(str(rel), context=f"rule {rule_id} edits[{i}].file")
        cross_refs = edit.get("skip_if_contains_in_files") or []
        for j, entry in enumerate(cross_refs):
            if not isinstance(entry, dict):
                continue
            other = entry.get("file")
            if other:
                _validate_docs_relative_path(
                    str(other),
                    context=f"rule {rule_id} edits[{i}].skip_if_contains_in_files[{j}].file",
                )


# Shown at the top of every Phase 2 draft PR body for tagged reviewers.
PHASE2_PR_STAKEHOLDER_NOTICE = """## For tagged reviewers and stakeholders

This pull request was **generated automatically** by the Braze Support analyzer workflow. That process reviews the latest **Braze Support** case export (Looker) and **proposes Braze Docs** changes from allowlisted rules in `.github/support_analyzer_phase2_rules.yml`. Treat this as a **draft** until a maintainer validates wording and behavior against product source.
"""


def _load_assignees_mapping(path: Path) -> list[tuple[str, str]]:
    """Load (doc_path_prefix, github_login) rows; longest path first for prefix matching."""
    if not path.is_file():
        return []
    rows: list[tuple[str, str]] = []
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return []
        lower_to_orig = {name.strip().lower(): name for name in reader.fieldnames}
        path_key = (
            lower_to_orig.get("page path")
            or lower_to_orig.get("path")
            or lower_to_orig.get("page_path")
        )
        user_key = (
            lower_to_orig.get("github username")
            or lower_to_orig.get("github_username")
            or lower_to_orig.get("github")
            or lower_to_orig.get("assignee")
        )
        if not path_key or not user_key:
            print(
                "assignees map: expected columns like 'page path' and 'github username'; "
                f"got {reader.fieldnames!r}",
                file=sys.stderr,
            )
            return []
        for row in reader:
            raw_p = (row.get(path_key) or "").strip().replace("\\", "/")
            raw_u = (row.get(user_key) or "").strip()
            if not raw_p or not raw_u or raw_p.startswith("#"):
                continue
            # Allow multiple assignees per path (comma-separated in the spreadsheet cell).
            login_parts = [p.strip() for p in raw_u.split(",") if p.strip()]
            for part in login_parts:
                if not _GH_LOGIN_RE.match(part):
                    print(
                        f"assignees map: skipping invalid GitHub Username {part!r} for path {raw_p!r}",
                        file=sys.stderr,
                    )
                    continue
                rows.append((raw_p, part))
    rows.sort(key=lambda t: len(t[0]), reverse=True)
    return rows


def _assignees_for_doc_paths(
    paths: Iterable[Path],
    *,
    root: Path,
    mapping: list[tuple[str, str]],
) -> list[str]:
    """GitHub logins for paths (stable order, unique).

    Longest matching path prefix wins. Multiple CSV rows (or comma-separated
    logins expanded at load) for the same winning prefix all contribute assignees.
    """
    if not mapping:
        return []
    ordered: dict[str, None] = {}
    root = root.resolve()
    for path in paths:
        rel = path.resolve().relative_to(root).as_posix()
        best_len = -1
        matched: list[str] = []
        for prefix, user in mapping:
            if not (rel == prefix or rel.startswith(prefix + "/")):
                continue
            plen = len(prefix)
            if plen > best_len:
                best_len = plen
                matched = [user]
            elif plen == best_len:
                matched.append(user)
        for login in matched:
            ordered.setdefault(login, None)
    return list(ordered.keys())


def _parse_gh_pr_create_stdout(stdout: str) -> str:
    lines = [ln.strip() for ln in (stdout or "").splitlines() if ln.strip()]
    if not lines:
        return ""
    last = lines[-1]
    return last if last.startswith("http") else ""


def _gh_pr_create(
    *,
    cmd_base: list[str],
    assignees: list[str],
    cwd: Path,
    rule_id: str,
) -> str:
    """Run gh pr create; return PR URL on success."""
    cmd = list(cmd_base)
    for login in assignees:
        cmd.extend(["--assignee", login])
    print("+", " ".join(cmd), file=sys.stderr)
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode == 0:
        return _parse_gh_pr_create_stdout(r.stdout)
    if not assignees:
        raise subprocess.CalledProcessError(r.returncode, cmd, r.stdout, r.stderr)
    print(
        f"rule {rule_id}: gh pr create failed with --assignee; retrying without assignees "
        "(check GitHub usernames and repo permissions)",
        file=sys.stderr,
    )
    if r.stderr:
        print(r.stderr, file=sys.stderr)
    print("+", " ".join(cmd_base), file=sys.stderr)
    r2 = subprocess.run(cmd_base, cwd=cwd, capture_output=True, text=True, check=True)
    return _parse_gh_pr_create_stdout(r2.stdout)


def _write_run_summary(
    *,
    path: Path,
    run_url: str,
    opened: list[dict[str, Any]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_url": run_url,
        "opened": opened,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _write_verification_report(
    *,
    root: Path,
    report_rel: Path,
    chunks: list[str],
    run_url: str,
) -> None:
    report_path = (root / report_rel).resolve() if not report_rel.is_absolute() else report_rel
    report_path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# Support analyzer Phase 2 — verification log\n\n"
        f"_Run: {run_url or 'local'}_\n\n"
    )
    body = (
        "\n".join(chunks).strip()
        if chunks
        else "_No `verification` blocks ran, or every check was skipped (e.g. missing `platform/` checkout)._"
    )
    report_path.write_text(header + body + "\n", encoding="utf-8")
    print(f"Wrote verification report {report_path}", file=sys.stderr)


def _load_rules(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "rules" not in data:
        raise SystemExit("Rules file must be a mapping with top-level 'rules' list")
    return data


def _combined_case_text(rows: list[dict[str, str]], fields: list[str]) -> dict[str, str]:
    """One combined text blob per case ID (lowercased for matching)."""
    by_case: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        cid = (row.get(CASE_ID_COL) or "").strip()
        if not cid:
            continue
        parts: list[str] = []
        for f in fields:
            parts.append(row.get(f) or "")
        blob = " ".join(parts).strip()
        if blob:
            by_case[cid].append(blob)
    return {cid: " ".join(parts).lower() for cid, parts in by_case.items()}


def _ensure_case_pattern_cache(rule: dict[str, Any]) -> None:
    """Compile case_text regexes once per rule (large CSVs call matching many times)."""
    if "_phase2_compiled_case_patterns" in rule:
        return
    cfg = rule.get("case_text") or {}
    patterns = cfg.get("patterns") or []
    mode = (cfg.get("match_mode") or "all_of").lower()
    rule["_phase2_compiled_case_patterns"] = [re.compile(p) for p in patterns]
    rule["_phase2_case_match_mode"] = mode


def _rule_matches_case(text: str, rule: dict[str, Any]) -> bool:
    _ensure_case_pattern_cache(rule)
    compiled: list[re.Pattern[str]] = rule["_phase2_compiled_case_patterns"]
    mode: str = rule["_phase2_case_match_mode"]
    if not compiled:
        return False
    if mode == "all_of":
        return all(p.search(text) for p in compiled)
    if mode == "any_of":
        return any(p.search(text) for p in compiled)
    raise SystemExit(f"Unknown match_mode: {mode}")


def _matching_case_ids(case_text: dict[str, str], rule: dict[str, Any]) -> list[str]:
    return [cid for cid, text in case_text.items() if _rule_matches_case(text, rule)]


def _insert_point_after_line(content: str, anchor: str) -> int | None:
    idx = content.find(anchor)
    if idx == -1:
        return None
    line_end = content.find("\n", idx + len(anchor))
    if line_end == -1:
        return len(content)
    # Insert after the newline that ends the anchor line
    return line_end + 1


def _insert_point_before_line(content: str, anchor: str) -> int | None:
    idx = content.find(anchor)
    if idx == -1:
        return None
    return idx


def _edit_already_applied(
    content: str,
    edit: dict[str, Any],
    *,
    root: Path | None = None,
) -> bool:
    """True when this edit is already on develop (skip phrases or legacy fingerprint comment)."""
    fp = (edit.get("fingerprint") or "").strip()
    if fp and f"<!-- {fp} -->" in content:
        return True
    for phrase in edit.get("skip_if_contains") or []:
        text = (phrase or "").strip()
        if text and text in content:
            return True
    for entry in edit.get("skip_if_contains_in_files") or []:
        if not isinstance(entry, dict):
            continue
        rel = (entry.get("file") or "").strip()
        phrases = entry.get("contains") or entry.get("phrases") or []
        if not rel or not root:
            continue
        other_path = root / rel
        if not other_path.is_file():
            continue
        other_content = other_path.read_text(encoding="utf-8")
        for phrase in phrases:
            text = (phrase or "").strip()
            if text and text in other_content:
                return True
    return False


def _open_phase2_pr_for_rule(rule_id: str, *, cwd: Path) -> str | None:
    """Return an open Phase 2 PR URL for this rule, if one exists."""
    prefix = f"support-analyzer/phase2-{rule_id}-"
    try:
        raw = _run_capture(
            [
                "gh",
                "pr",
                "list",
                "--state",
                "open",
                "--label",
                "support analyzer",
                "--json",
                "headRefName,url",
                "--limit",
                "100",
            ],
            cwd=cwd,
        )
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        raise SystemExit(
            f"rule {rule_id}: could not list open PRs for dedup (fail closed)"
            + (f": {detail}" if detail else "")
        ) from exc
    if not raw:
        return None
    try:
        prs = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(
            f"rule {rule_id}: could not parse gh pr list output for dedup (fail closed)"
        ) from exc
    for pr in prs:
        head = (pr.get("headRefName") or "").strip()
        if head.startswith(prefix):
            return (pr.get("url") or "").strip() or None
    return None


def _apply_edit(
    content: str,
    edit: dict[str, Any],
    *,
    root: Path | None = None,
) -> tuple[str, bool]:
    """
    Return (new_content, changed). Skip if fingerprint or skip_if_contains matches.
    """
    if _edit_already_applied(content, edit, root=root):
        return content, False

    anchor = edit.get("anchor_substring") or ""
    insert = edit.get("insert") or ""
    if not anchor or not insert:
        return content, False

    position = (edit.get("position") or "after").lower()
    if position == "before":
        pt = _insert_point_before_line(content, anchor)
        if pt is None:
            return content, False
        new_content = content[:pt] + insert + content[pt:]
        return new_content, True

    if position == "after":
        pt = _insert_point_after_line(content, anchor)
        if pt is None:
            return content, False
        new_content = content[:pt] + insert + content[pt:]
        return new_content, True

    raise SystemExit(f"Unknown position: {position}")


def _run(cmd: list[str], *, cwd: Path | None = None) -> None:
    print("+", " ".join(cmd), file=sys.stderr)
    subprocess.run(cmd, cwd=cwd, check=True)


def _run_capture(cmd: list[str], *, cwd: Path) -> str:
    print("+", " ".join(cmd), file=sys.stderr)
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)
    return (r.stdout or "").strip()


def _validate_edits_anchors(
    *,
    root: Path,
    edits: list[dict[str, Any]],
    rule_id: str,
    strict: bool,
) -> None:
    """Ensure anchors exist before applying; avoids silent no-op in CI."""
    problems: list[str] = []
    for edit in edits:
        rel = edit.get("file")
        if not rel:
            continue
        path = root / rel
        if not path.is_file():
            if strict:
                problems.append(f"{rel}: target file missing")
            continue
        content = path.read_text(encoding="utf-8")
        if _edit_already_applied(content, edit, root=root):
            continue
        anchor = (edit.get("anchor_substring") or "").strip()
        if anchor and anchor not in content:
            problems.append(f"{rel}: anchor not found (edit not already applied)")

    if not problems:
        return
    msg = f"rule {rule_id}: strict anchor check failed:\n" + "\n".join(f"  - {p}" for p in problems)
    if strict:
        raise SystemExit(msg)
    print(msg, file=sys.stderr)


def _run_rg_list_files(
    *,
    search_root: Path,
    glob_pat: str,
    pattern: str,
) -> list[str]:
    """Return paths (relative lines) from `rg -l`."""
    rg = shutil.which("rg")
    if not rg:
        raise SystemExit(
            "ripgrep (`rg`) is not on PATH. Install it (e.g. `apt-get install ripgrep`) "
            "or run without rule verification."
        )
    cmd = [
        rg,
        "-l",
        "--glob",
        glob_pat,
        "-e",
        pattern,
        ".",
    ]
    r = subprocess.run(
        cmd,
        cwd=search_root,
        capture_output=True,
        text=True,
        timeout=300,
    )
    if r.returncode not in (0, 1):
        raise SystemExit(
            f"rg failed (exit {r.returncode}) in {search_root}: {r.stderr.strip() or r.stdout.strip()}"
        )
    lines = [ln.strip() for ln in (r.stdout or "").splitlines() if ln.strip()]
    return lines


def _run_rule_verification(
    *,
    root: Path,
    rule: dict[str, Any],
    rule_id: str,
) -> tuple[bool, list[str]]:
    """
    Run optional `verification.checks` (e.g. ripgrep under a checked-out repo).

    Returns (failed_required, markdown_lines_for_report).
    If `failed_required` is True, the caller must abort the workflow.
    """
    ver = rule.get("verification")
    if not ver or not isinstance(ver, dict):
        return False, []

    checks = ver.get("checks") or []
    if not checks:
        return False, []

    required = bool(ver.get("required", False))
    lines: list[str] = [f"## Rule `{rule_id}`", ""]

    failed_required = False
    for i, ch in enumerate(checks):
        if not isinstance(ch, dict):
            lines.append(f"- Check {i + 1}: skipped (invalid entry)")
            continue
        typ = (ch.get("type") or "rg").lower()
        if typ != "rg":
            lines.append(f"- Check {i + 1}: skipped (unknown type `{typ}`)")
            continue

        rel_root = (ch.get("root") or "platform").strip().strip("/")
        pattern = (ch.get("pattern") or "").strip()
        glob_pat = (ch.get("glob") or "*").strip()
        min_hits = int(ch.get("min_hits", 1))

        if not pattern:
            lines.append(f"- Check {i + 1}: skipped (empty pattern)")
            continue

        abs_root = (root / rel_root).resolve()
        if not abs_root.is_dir():
            msg = (
                f"- Check {i + 1}: **SKIPPED** — `{rel_root}/` not found "
                f"(add a checkout step or set `verification.required: false`)."
            )
            lines.append(msg)
            if required:
                failed_required = True
            continue

        try:
            hits = _run_rg_list_files(
                search_root=abs_root, glob_pat=glob_pat, pattern=pattern
            )
        except SystemExit:
            raise
        except (OSError, subprocess.TimeoutExpired) as e:
            lines.append(f"- Check {i + 1}: **ERROR** — {e}")
            if required:
                failed_required = True
            continue

        n = len(hits)
        if n < min_hits:
            lines.append(
                f"- Check {i + 1}: **FAIL** — pattern `{pattern}` glob `{glob_pat}` "
                f"hits={n} (need >= {min_hits}) under `{rel_root}/`."
            )
            if required:
                failed_required = True
        else:
            lines.append(
                f"- Check {i + 1}: **OK** — `{pattern}` under `{rel_root}/` ({n} file(s))."
            )

    lines.append("")
    return failed_required, lines


def _phase2_run_date_ymd() -> str:
    """Eastern date stamp for branch names (matches workflow timezone)."""
    return datetime.now(_PHASE2_BRANCH_TZ).strftime("%Y-%m-%d")


def _phase2_branch_name(*, rule_id: str, run_id: str, ymd: str | None = None) -> str:
    """Unique branch per workflow run; date segment aids triage in the GitHub UI."""
    day = ymd or _phase2_run_date_ymd()
    return f"support-analyzer/phase2-{rule_id}-{day}-{run_id}"


def main() -> None:
    p = argparse.ArgumentParser(description="Support analyzer Phase 2 — rules to doc PRs")
    p.add_argument("input_csv", help="Path to Support Cases CSV")
    p.add_argument(
        "--rules",
        default=".github/support_analyzer_phase2_rules.yml",
        help="Path to rules YAML",
    )
    p.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Repository root (contains _docs)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions only; do not branch/commit/push/open PR",
    )
    p.add_argument(
        "--strict-anchors",
        action="store_true",
        help="Exit with error if a matched rule needs an edit but anchor text is missing in target file",
    )
    p.add_argument(
        "--verification-report",
        default=".github/support_analyzer_phase2_verification.md",
        help="Write a markdown verification log under the repo root (for CI artifacts)",
    )
    p.add_argument(
        "--assignees-map",
        default=".github/support_analyzer_doc_assignees.csv",
        help="CSV mapping doc paths (prefix or file) → GitHub username for gh pr create --assignee",
    )
    p.add_argument(
        "--run-summary",
        default=".github/support_analyzer_phase2_run_summary.json",
        help="Write JSON summary of opened Phase 2 PRs (for CI Slack notifications)",
    )
    args = p.parse_args()

    csv_path = Path(args.input_csv)
    root = args.root.resolve()
    rules_path = (root / args.rules).resolve() if not Path(args.rules).is_absolute() else Path(args.rules)
    assignees_map_path = (
        (root / args.assignees_map).resolve()
        if not Path(args.assignees_map).is_absolute()
        else Path(args.assignees_map).resolve()
    )

    if not csv_path.is_file():
        raise SystemExit(f"CSV not found: {csv_path}")
    if not rules_path.is_file():
        raise SystemExit(f"Rules not found: {rules_path}")

    assignees_mapping = _load_assignees_mapping(assignees_map_path)
    if not assignees_map_path.is_file():
        print(
            f"assignees: no map file at {assignees_map_path}; PRs will open without assignees",
            file=sys.stderr,
        )

    rules_doc = _load_rules(rules_path)
    rules: list[dict[str, Any]] = rules_doc.get("rules") or []

    with csv_path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    run_id = os.environ.get("GITHUB_RUN_ID", "local")
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    run_url = f"{server}/{repo}/actions/runs/{os.environ.get('GITHUB_RUN_ID', '')}" if repo else ""

    verification_report_chunks: list[str] = []
    opened_prs: list[dict[str, Any]] = []
    run_summary_path = (
        (root / args.run_summary).resolve()
        if not Path(args.run_summary).is_absolute()
        else Path(args.run_summary).resolve()
    )

    try:
        _phase2_process_rules(
            rules=rules,
            rows=rows,
            fieldnames=fieldnames,
            root=root,
            run_id=run_id,
            run_url=run_url,
            assignees_mapping=assignees_mapping,
            assignees_map_path=assignees_map_path,
            args=args,
            verification_report_chunks=verification_report_chunks,
            opened_prs=opened_prs,
        )
        _write_verification_report(
            root=root,
            report_rel=Path(args.verification_report),
            chunks=verification_report_chunks,
            run_url=run_url,
        )
    finally:
        _write_run_summary(path=run_summary_path, run_url=run_url, opened=opened_prs)


def _phase2_process_rules(
    *,
    rules: list[dict[str, Any]],
    rows: list[dict[str, str]],
    fieldnames: list[str],
    root: Path,
    run_id: str,
    run_url: str,
    assignees_mapping: list[tuple[str, str]],
    assignees_map_path: Path,
    args: argparse.Namespace,
    verification_report_chunks: list[str],
    opened_prs: list[dict[str, Any]],
) -> None:
    for rule in rules:
        if not rule.get("enabled", True):
            print(f"skip disabled rule {rule.get('id')}", file=sys.stderr)
            continue

        rid = rule.get("id") or "unnamed"
        if not _RULE_ID_RE.match(rid):
            raise SystemExit(
                f"rule id {rid!r} is invalid for git branch names; use only letters, digits, "
                "hyphens, and underscores (1–128 chars); must start and end with a letter or digit"
            )
        _validate_rule_edit_paths(rule, rid)
        _ensure_case_pattern_cache(rule)
        case_cfg = rule.get("case_text") or {}
        fields = case_cfg.get("fields") or []
        missing = [c for c in fields if c not in fieldnames]
        if missing:
            print(
                f"rule {rid}: skipping — missing CSV columns: {missing}. Available: {fieldnames[:20]}...",
                file=sys.stderr,
            )
            continue

        case_text = _combined_case_text(rows, fields)
        matches = _matching_case_ids(case_text, rule)
        min_n = int(rule.get("min_matching_cases") or 1)
        if len(matches) < min_n:
            print(
                f"rule {rid}: {len(matches)} matching cases (need {min_n}); skip",
                file=sys.stderr,
            )
            continue

        edits = rule.get("edits") or []
        if not edits:
            continue

        _validate_edits_anchors(
            root=root, edits=edits, rule_id=rid, strict=args.strict_anchors
        )

        v_failed, v_lines = _run_rule_verification(root=root, rule=rule, rule_id=rid)
        if v_lines:
            verification_report_chunks.extend(v_lines)
        if v_failed:
            _write_verification_report(
                root=root,
                report_rel=Path(args.verification_report),
                chunks=verification_report_chunks,
                run_url=run_url,
            )
            raise SystemExit(
                "Required rule verification failed:\n" + "\n".join(v_lines),
            )

        pending_files: dict[Path, str] = {}
        skip_rule = False
        for edit in edits:
            rel = edit.get("file")
            if not rel:
                continue
            rel_norm = _validate_docs_relative_path(
                str(rel), context=f"rule {rid} edits[].file"
            )
            path = root / rel_norm
            if not path.is_file():
                msg = f"rule {rid}: target missing {path}"
                if args.strict_anchors:
                    raise SystemExit(msg)
                print(f"{msg}; skip rule", file=sys.stderr)
                skip_rule = True
                break
            original = path.read_text(encoding="utf-8")
            updated, changed = _apply_edit(original, edit, root=root)
            if not changed:
                print(
                    f"rule {rid}: no change for {rel} (anchor, fingerprint, skip_if_contains, or skip_if_contains_in_files)",
                    file=sys.stderr,
                )
                continue
            pending_files[path] = updated

        if skip_rule:
            continue
        if not pending_files:
            print(f"rule {rid}: no file changes; skip PR", file=sys.stderr)
            continue

        pr_cfg = rule.get("pr") or {}
        ymd = _phase2_run_date_ymd()
        branch = _phase2_branch_name(rule_id=rid, run_id=run_id, ymd=ymd)
        title_base = pr_cfg.get("title") or f"[SA] Phase 2 — {rid}"
        title = title_base if ymd in title_base else f"{title_base} — {ymd}"
        draft = pr_cfg.get("draft", True)
        labels = pr_cfg.get("labels") or ["support analyzer"]
        note = (pr_cfg.get("verification_note") or "").strip()
        note_block = f"\n**Rule note:** {note}\n" if note else ""

        has_ver_checks = bool(
            isinstance(rule.get("verification"), dict)
            and (rule.get("verification") or {}).get("checks")
        )
        ver_artifact_block = (
            "\n**Automated source checks:** see workflow artifact **support-analyzer-phase2-verification** (internal; do not copy file paths into public-facing summaries).\n"
            if has_ver_checks
            else ""
        )

        case_lines = "\n".join(
            f"- https://braze.lightning.force.com/lightning/r/Case/{cid}/view" for cid in sorted(matches)[:50]
        )
        if len(matches) > 50:
            case_lines += f"\n- _…and {len(matches) - 50} more case(s)_"

        assignees_list = _assignees_for_doc_paths(
            pending_files.keys(),
            root=root,
            mapping=assignees_mapping,
        )
        assignee_block = ""
        if assignees_list:
            mentions = " ".join(f"@{login}" for login in assignees_list)
            assignee_block = (
                f"\n**Assignees:** {mentions} "
                f"(_matched from doc paths in `{assignees_map_path.relative_to(root)}`._)\n"
            )
        elif assignees_mapping and pending_files:
            rels = ", ".join(sorted(p.relative_to(root).as_posix() for p in pending_files))
            print(f"rule {rid}: no assignee map match for: {rels}", file=sys.stderr)

        body = f"""{PHASE2_PR_STAKEHOLDER_NOTICE}

Automated **Phase 2** doc proposal from `support_analyzer_phase2_rules.yml` (rule `{rid}`).

**Workflow run:** {run_url or "(local)"}

**Matching cases ({len(matches)}):**
{case_lines}
{note_block}{ver_artifact_block}{assignee_block}
**Verification:** This proposal is rule-driven. Before merge, confirm behavior against Braze product source. For **public** PR descriptions or external posts, use only the generic phrase **Verified against Braze source code.** Do not paste internal `platform` or SDK repository file paths into public-facing text (see Braze docs contributing guidance).
"""

        if args.dry_run:
            print(f"[dry-run] would create branch {branch} with {len(pending_files)} file(s)", file=sys.stderr)
            continue

        existing_pr = _open_phase2_pr_for_rule(rid, cwd=root)
        if existing_pr:
            print(
                f"rule {rid}: skip PR — open Phase 2 draft already exists: {existing_pr}",
                file=sys.stderr,
            )
            continue

        _run(["git", "fetch", "origin", "develop"], cwd=root)
        _run(["git", "checkout", "develop"], cwd=root)
        _run(["git", "reset", "--hard", "origin/develop"], cwd=root)

        _run(["git", "checkout", "-B", branch], cwd=root)
        for path, text in pending_files.items():
            path.write_text(text, encoding="utf-8")
            _run(["git", "add", "--", str(path.relative_to(root))], cwd=root)

        msg = f"docs(phase2): {rid}\n\nAutomated proposal from Support analyzer Phase 2."
        _run(["git", "commit", "-m", msg], cwd=root)
        _run(["git", "push", "-u", "origin", branch], cwd=root)

        cmd_base = [
            "gh",
            "pr",
            "create",
            "--base",
            "develop",
            "--head",
            branch,
            "--title",
            title,
            "--body",
            body,
        ]
        if draft:
            cmd_base.append("--draft")
        for lb in labels:
            cmd_base.extend(["--label", lb])

        pr_url = _gh_pr_create(
            cmd_base=cmd_base,
            assignees=assignees_list,
            cwd=root,
            rule_id=rid,
        )
        opened_prs.append(
            {
                "rule_id": rid,
                "title": title,
                "pr_url": pr_url,
                "assignees": assignees_list,
            }
        )
        if assignees_list:
            print(
                f"opened PR for rule {rid} branch {branch} assignees={assignees_list}",
                file=sys.stderr,
            )
        else:
            print(f"opened PR for rule {rid} branch {branch}", file=sys.stderr)

        _run(["git", "fetch", "origin", "develop"], cwd=root)
        _run(["git", "checkout", "develop"], cwd=root)
        _run(["git", "reset", "--hard", "origin/develop"], cwd=root)


if __name__ == "__main__":
    main()
