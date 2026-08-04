#!/usr/bin/env python3
"""
Detect duplicate Salesforce KB migration work before Phase 2.

Checks open/draft/merged PRs (any label), ``article_id`` claims in PR bodies, ``develop``
content (phase-2 marker + recent SF KB commits), and in-flight ``sf-cursor-*`` branches.

Usage:
  python3 scripts/salesforce-analyzer/sf_kb_overlap_scan.py
  python3 scripts/salesforce-analyzer/sf_kb_overlap_scan.py --doc-path '_docs/.../faq.md'
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable

REPO = "braze-inc/braze-docs"
REPO_ROOT = Path(__file__).resolve().parents[2]
SF_KB_LABEL = "salesforce migration"
PHASE2_MARKER = "<!-- sf-kb-phase2-batch -->"
DOC_PREFIXES = ("_docs/", "_includes/")
ARTICLE_ID_RE = re.compile(r"`(ka[^`]+)`")
SF_KB_COMMIT_RE = re.compile(r"\bSF KB\b|Salesforce KB", re.I)
OPEN_PR_LIMIT = 500
MERGED_PR_LIMIT = 400
MERGED_LOOKBACK_DAYS = 180
DEVELOP_SF_COMMIT_LOOKBACK = 10

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_kb_phase1_outputs import doc_path_branch_slug  # noqa: E402

GhJsonFn = Callable[[list[str]], object]


@dataclass(frozen=True)
class PrRef:
    number: int
    state: str
    is_draft: bool
    title: str
    url: str
    labels: tuple[str, ...]
    merged_at: str | None = None

    def label(self) -> str:
        draft = " draft" if self.is_draft else ""
        return f"#{self.number}{draft} ({self.state})"


@dataclass
class OverlapHit:
    kind: str
    message: str
    prs: tuple[PrRef, ...] = ()
    blocking: bool = True

    def summary(self) -> str:
        if self.prs:
            refs = ", ".join(p.label() for p in self.prs)
            return f"{self.message} [{refs}]"
        return self.message


@dataclass
class BatchOverlapReport:
    doc_path: str
    article_ids: tuple[str, ...]
    hits: list[OverlapHit] = field(default_factory=list)

    @property
    def blocked(self) -> bool:
        return any(h.blocking for h in self.hits)

    @property
    def warnings(self) -> list[OverlapHit]:
        return [h for h in self.hits if not h.blocking]

    def status_label(self) -> str:
        if self.blocked:
            return "blocked"
        if self.warnings:
            return "warning"
        return "clear"

    def format_lines(self, *, indent: str = "") -> list[str]:
        if not self.hits:
            return [f"{indent}- **Clear** — no overlap detected."]
        lines: list[str] = []
        for hit in self.hits:
            level = "BLOCK" if hit.blocking else "WARN"
            lines.append(f"{indent}- **{level}** ({hit.kind}): {hit.summary()}")
        return lines


def default_gh_json(args: list[str]) -> object:
    proc = subprocess.run(
        ["gh", *args, "--repo", REPO],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gh failed: {' '.join(args)}\n{proc.stderr or proc.stdout}")
    return json.loads(proc.stdout or "null")


def run_git(args: list[str], *, repo_root: Path = REPO_ROOT) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"git failed ({proc.returncode}): {' '.join(args)}\n{proc.stderr or proc.stdout}"
        )
    return proc.stdout


def is_doc_path(path: str) -> bool:
    return any(path.startswith(prefix) for prefix in DOC_PREFIXES)


def parse_pr(raw: dict) -> PrRef:
    labels = tuple(l.get("name", "") for l in (raw.get("labels") or []))
    return PrRef(
        number=int(raw["number"]),
        state=(raw.get("state") or "").lower(),
        is_draft=bool(raw.get("isDraft")),
        title=(raw.get("title") or "").strip(),
        url=(raw.get("url") or "").strip(),
        labels=labels,
        merged_at=(raw.get("mergedAt") or None),
    )


def merged_within_lookback(pr: PrRef, *, days: int = MERGED_LOOKBACK_DAYS) -> bool:
    if not pr.merged_at:
        return True
    try:
        merged = datetime.fromisoformat(pr.merged_at.replace("Z", "+00:00"))
    except ValueError:
        return True
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    return merged >= cutoff


class OverlapScanner:
    """Caches GitHub + develop lookups for batch overlap checks."""

    def __init__(
        self,
        *,
        repo_root: Path = REPO_ROOT,
        gh_json: GhJsonFn = default_gh_json,
        fetch_develop: bool = True,
    ) -> None:
        self.repo_root = repo_root
        self.gh_json = gh_json
        self.fetch_develop = fetch_develop
        self._loaded = False
        self._path_prs: dict[str, list[PrRef]] = {}
        self._article_prs: dict[str, list[PrRef]] = {}
        self._develop_text: dict[str, str | None] = {}
        self._scan_error: str | None = None

    def refresh(self) -> None:
        self._loaded = False
        self._path_prs = {}
        self._article_prs = {}
        self._develop_text = {}
        self._scan_error = None
        try:
            if self.fetch_develop:
                subprocess.run(
                    ["git", "fetch", "origin", "develop"],
                    cwd=self.repo_root,
                    text=True,
                    capture_output=True,
                    check=False,
                )
            self._load_pr_index()
            self._loaded = True
        except Exception as exc:  # noqa: BLE001
            self._scan_error = str(exc)

    @property
    def available(self) -> bool:
        return self._loaded and self._scan_error is None

    @property
    def error(self) -> str | None:
        return self._scan_error

    def _list_prs(self, state: str, *, limit: int) -> list[dict]:
        return self.gh_json(
            [
                "pr",
                "list",
                "--state",
                state,
                "--limit",
                str(limit),
                "--json",
                "number,title,url,isDraft,labels,files,state,mergedAt,body",
            ]
        )

    def _load_pr_index(self) -> None:
        path_prs: dict[str, list[PrRef]] = {}
        all_prs: dict[int, PrRef] = {}
        pr_bodies: dict[int, str] = {}

        for state, limit in (("open", OPEN_PR_LIMIT), ("merged", MERGED_PR_LIMIT)):
            for raw in self._list_prs(state, limit=limit):
                pr = parse_pr(raw)
                all_prs[pr.number] = pr
                pr_bodies[pr.number] = raw.get("body") or ""
                for file_entry in raw.get("files") or []:
                    path = (file_entry.get("path") or "").strip()
                    if is_doc_path(path):
                        path_prs.setdefault(path, []).append(pr)

        body_pr_numbers: set[int] = {
            num for num, pr in all_prs.items() if pr.state == "open"
        }
        for num, pr in all_prs.items():
            if SF_KB_LABEL in pr.labels:
                body_pr_numbers.add(num)

        article_prs: dict[str, list[PrRef]] = {}
        for num in sorted(body_pr_numbers):
            pr = all_prs[num]
            body = pr_bodies.get(num, "")
            for article_id in ARTICLE_ID_RE.findall(body):
                article_prs.setdefault(article_id, []).append(pr)

        self._path_prs = path_prs
        self._article_prs = article_prs

    def _develop_text_for(self, doc_path: str) -> str | None:
        if doc_path not in self._develop_text:
            proc = subprocess.run(
                ["git", "show", f"origin/develop:{doc_path}"],
                cwd=self.repo_root,
                text=True,
                capture_output=True,
            )
            self._develop_text[doc_path] = proc.stdout if proc.returncode == 0 else None
        return self._develop_text[doc_path]

    def _remote_sf_branches(self, doc_path: str) -> list[str]:
        slug = doc_path_branch_slug(doc_path)
        prefix = f"sf-cursor-{slug}-"
        proc = subprocess.run(
            ["git", "ls-remote", "--heads", "origin", f"{prefix}*"],
            cwd=self.repo_root,
            text=True,
            capture_output=True,
        )
        if proc.returncode != 0:
            return []
        branches: list[str] = []
        for line in proc.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 2 and parts[1].startswith("refs/heads/"):
                branches.append(parts[1].removeprefix("refs/heads/"))
        return branches

    def _recent_develop_sf_commits(self, doc_path: str) -> list[str]:
        proc = subprocess.run(
            [
                "git",
                "log",
                "origin/develop",
                f"-n{DEVELOP_SF_COMMIT_LOOKBACK}",
                "--format=%h %s",
                "--",
                doc_path,
            ],
            cwd=self.repo_root,
            text=True,
            capture_output=True,
        )
        if proc.returncode != 0:
            return []
        return [
            line.strip()
            for line in proc.stdout.splitlines()
            if line.strip() and SF_KB_COMMIT_RE.search(line)
        ]

    def check_batch(self, doc_path: str, article_ids: list[str]) -> BatchOverlapReport:
        report = BatchOverlapReport(
            doc_path=doc_path,
            article_ids=tuple(article_ids),
        )
        if not self.available:
            report.hits.append(
                OverlapHit(
                    kind="scan_unavailable",
                    message=self.error or "overlap scan unavailable",
                    blocking=False,
                )
            )
            return report

        open_hits: list[PrRef] = []
        merged_hits: list[PrRef] = []
        for pr in self._path_prs.get(doc_path, []):
            if pr.state == "open":
                open_hits.append(pr)
            elif pr.state == "merged" and merged_within_lookback(pr):
                merged_hits.append(pr)

        if open_hits:
            drafts = [p for p in open_hits if p.is_draft]
            ready = [p for p in open_hits if not p.is_draft]
            if ready:
                report.hits.append(
                    OverlapHit(
                        kind="open_pr",
                        message=f"Open PR(s) already edit `{doc_path}`",
                        prs=tuple(ready),
                        blocking=True,
                    )
                )
            if drafts:
                report.hits.append(
                    OverlapHit(
                        kind="draft_pr",
                        message=f"Draft PR(s) already edit `{doc_path}`",
                        prs=tuple(drafts),
                        blocking=True,
                    )
                )

        article_hits: dict[str, list[PrRef]] = {}
        for article_id in article_ids:
            for pr in self._article_prs.get(article_id, []):
                article_hits.setdefault(article_id, []).append(pr)

        for article_id, prs in sorted(article_hits.items()):
            open_or_merged = [p for p in prs if p.state in ("open", "merged")]
            if not open_or_merged:
                continue
            report.hits.append(
                OverlapHit(
                    kind="article_id",
                    message=f"`{article_id}` already claimed in a PR body",
                    prs=tuple(open_or_merged),
                    blocking=True,
                )
            )

        develop_text = self._develop_text_for(doc_path)
        if develop_text and PHASE2_MARKER in develop_text:
            report.hits.append(
                OverlapHit(
                    kind="develop_marker",
                    message=f"`develop` already contains a Phase 2 batch marker in `{doc_path}`",
                    blocking=True,
                )
            )

        sf_commits = self._recent_develop_sf_commits(doc_path)
        if sf_commits:
            report.hits.append(
                OverlapHit(
                    kind="develop_sf_commit",
                    message=(
                        f"Recent Salesforce KB commit(s) on `develop` for `{doc_path}`: "
                        + "; ".join(sf_commits[:3])
                    ),
                    blocking=False,
                )
            )

        if merged_hits and not any(h.kind == "article_id" for h in report.hits):
            report.hits.append(
                OverlapHit(
                    kind="merged_pr",
                    message=(
                        f"Merged PR(s) touched `{doc_path}` in the last {MERGED_LOOKBACK_DAYS} days "
                        "(different articles may still be valid — verify before opening a new PR)"
                    ),
                    prs=tuple(merged_hits),
                    blocking=False,
                )
            )

        remote_branches = self._remote_sf_branches(doc_path)
        if remote_branches:
            report.hits.append(
                OverlapHit(
                    kind="remote_branch",
                    message=(
                        "Remote `sf-cursor-*` branch(es) exist for this doc path: "
                        + ", ".join(f"`{b}`" for b in remote_branches[:5])
                    ),
                    blocking=True,
                )
            )

        return report

    def scan_batches(
        self, batches: list[tuple[str, list[str]]]
    ) -> dict[str, BatchOverlapReport]:
        if not self._loaded:
            self.refresh()
        return {
            doc_path: self.check_batch(doc_path, article_ids)
            for doc_path, article_ids in batches
        }


def format_scan_summary(reports: dict[str, BatchOverlapReport]) -> str:
    blocked = sum(1 for r in reports.values() if r.blocked)
    warned = sum(1 for r in reports.values() if r.warnings and not r.blocked)
    clear = sum(1 for r in reports.values() if r.status_label() == "clear")
    return f"overlap scan: {clear} clear, {warned} warning, {blocked} blocked (of {len(reports)} batches)"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--doc-path",
        action="append",
        default=[],
        help="Only scan these `_docs/` or `_includes/` paths",
    )
    parser.add_argument(
        "--no-fetch",
        action="store_true",
        help="Skip `git fetch origin develop` before scanning",
    )
    args = parser.parse_args()

    import csv

    csv_path = REPO_ROOT / "_data" / "kb_articles.csv"
    if not csv_path.is_file():
        print(f"Missing {csv_path}", file=sys.stderr)
        sys.exit(1)

    batches: dict[str, list[str]] = {}
    with csv_path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            doc_path = (row.get("doc_path") or "").strip()
            article_id = (row.get("article_id") or "").strip()
            if not doc_path:
                continue
            if args.doc_path and doc_path not in args.doc_path:
                continue
            batches.setdefault(doc_path, []).append(article_id)

    scanner = OverlapScanner(fetch_develop=not args.no_fetch)
    scanner.refresh()
    reports = scanner.scan_batches(sorted(batches.items()))

    print(format_scan_summary(reports))
    for doc_path in sorted(reports):
        report = reports[doc_path]
        print(f"\n## `{doc_path}` — **{report.status_label()}**")
        for line in report.format_lines():
            print(line)

    if any(r.blocked for r in reports.values()):
        sys.exit(2)


if __name__ == "__main__":
    main()
