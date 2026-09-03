#!/usr/bin/env python3
"""
Reference-repo verification for Salesforce KB Phase 2.

Resolves ``codebase_evidence`` paths against sibling clones (``../platform``, SDK repos)
and optional keyword search before draft content is inserted.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from sf_kb_article_ids import article_id_from_row
from sf_kb_jira_ticket import _row_has_verification_proof, row_needs_reference_verify

REPO_ROOT = Path(__file__).resolve().parents[2]

REFERENCE_REPO_PREFIXES: tuple[str, ...] = (
    "platform",
    "unity-sdk",
    "swift-sdk",
    "braze-web-sdk",
    "braze-android-sdk",
    "braze-react-native-sdk",
    "braze-swift-sdk",
    "braze-flutter-sdk",
    "braze-unity-sdk",
    "braze-cordova-sdk",
    "braze-roku-sdk",
    "braze-unreal-sdk",
    "braze-expo-plugin",
    "braze-xamarin-sdk",
    "braze-shopify-app",
    "event-replay",
    "event-modeling-service",
    "liquid",
    "grapesjs",
)

# File path inside a reference repo (optional :line or :line-line suffix).
_REF_PATH_BODY = r"[\w./_-]+?\.(?:rb|jsx?|tsx?|json|yml|yaml|md|swift|kt|java|properties|gradle|strings|xml|cs)"
REFERENCE_FILE_RE = re.compile(
    rf"(?P<path>(?:{'|'.join(re.escape(p) for p in REFERENCE_REPO_PREFIXES)})/{_REF_PATH_BODY})"
    rf"(?::\d+(?:-\d+)?)?",
    re.IGNORECASE,
)
BRAZE_DOCS_EVIDENCE_RE = re.compile(
    r"braze-docs/(_docs|_includes)/[\w./_-]+\.(?:md|html?)",
    re.IGNORECASE,
)

STOPWORDS = frozenset(
    {
        "about",
        "after",
        "before",
        "braze",
        "canvas",
        "does",
        "from",
        "have",
        "into",
        "that",
        "their",
        "there",
        "this",
        "what",
        "when",
        "where",
        "which",
        "with",
        "your",
    }
)


@dataclass
class ResolvedEvidencePath:
    logical_path: str
    filesystem_path: Path | None
    repo_label: str


@dataclass
class RowReferenceVerifyResult:
    article_id: str
    title: str
    needs_verify: bool
    cited_paths: list[str] = field(default_factory=list)
    missing_paths: list[str] = field(default_factory=list)
    resolved_paths: list[ResolvedEvidencePath] = field(default_factory=list)
    keyword_hits: list[str] = field(default_factory=list)
    auto_bullets: list[str] = field(default_factory=list)
    blocking_reason: str | None = None


@dataclass
class BatchReferenceVerifyResult:
    row_results: list[RowReferenceVerifyResult] = field(default_factory=list)
    auto_bullets: list[str] = field(default_factory=list)
    missing_repo_roots: list[str] = field(default_factory=list)

    @property
    def blocking_errors(self) -> list[str]:
        return [r.blocking_reason for r in self.row_results if r.blocking_reason]

    @property
    def ok(self) -> bool:
        return not self.blocking_errors


def sibling_repo_roots() -> dict[str, Path]:
    parent = REPO_ROOT.parent
    return {name: parent / name for name in REFERENCE_REPO_PREFIXES}


def reference_paths_from_text(text: str) -> list[str]:
    """Extract resolvable reference-repo file paths from free text."""
    seen: set[str] = set()
    paths: list[str] = []
    for pattern in (REFERENCE_FILE_RE, BRAZE_DOCS_EVIDENCE_RE):
        for match in pattern.finditer(text or ""):
            raw = match.group("path") if "path" in match.groupdict() else match.group(0)
            path = raw.rstrip(".)`,")
            path = re.sub(r":\d+(?:-\d+)?$", "", path)
            if path and path not in seen:
                seen.add(path)
                paths.append(path)
    return paths


def resolve_logical_path(logical_path: str) -> ResolvedEvidencePath:
    normalized = logical_path.strip()
    if normalized.startswith("braze-docs/"):
        rel = normalized[len("braze-docs/") :].lstrip("/")
        fs = REPO_ROOT / rel
        return ResolvedEvidencePath(
            logical_path=normalized,
            filesystem_path=fs if fs.is_file() else None,
            repo_label="braze-docs",
        )

    for prefix, root in sibling_repo_roots().items():
        token = f"{prefix}/"
        if not normalized.lower().startswith(token):
            continue
        rel = normalized[len(prefix) + 1 :]
        fs = root / rel
        return ResolvedEvidencePath(
            logical_path=normalized,
            filesystem_path=fs if fs.is_file() else None,
            repo_label=prefix,
        )

    return ResolvedEvidencePath(logical_path=normalized, filesystem_path=None, repo_label="unknown")


def keywords_from_row(row: dict[str, str], *, max_terms: int = 6) -> list[str]:
    title = (row.get("title") or "").strip()
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{3,}", title)
    out: list[str] = []
    for word in words:
        low = word.lower()
        if low in STOPWORDS:
            continue
        if word not in out:
            out.append(word)
        if len(out) >= max_terms:
            break
    return out


def _search_keywords_in_file(path: Path, keywords: list[str]) -> list[str]:
    if not keywords or not path.is_file():
        return []
    hits: list[str] = []
    if shutil.which("rg"):
        for keyword in keywords:
            proc = subprocess.run(
                ["rg", "-F", "-i", "-m", "1", keyword, str(path)],
                capture_output=True,
                text=True,
            )
            if proc.returncode == 0 and (proc.stdout or "").strip():
                hits.append(keyword)
        return hits

    try:
        content = path.read_text(encoding="utf-8", errors="replace").lower()
    except OSError:
        return []
    for keyword in keywords:
        if keyword.lower() in content:
            hits.append(keyword)
    return hits


def pull_reference_repo(repo_name: str, *, dry_run: bool = False) -> str | None:
    """Run ``git pull --ff-only`` in a sibling repo. Returns error message or None."""
    root = sibling_repo_roots().get(repo_name)
    if not root or not (root / ".git").is_dir():
        return f"{repo_name} clone not found at {root}"
    cmd = ["git", "-C", str(root), "pull", "--ff-only"]
    if dry_run:
        return None
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        return f"git pull failed for {repo_name}: {detail}"
    return None


def verify_row_reference(
    row: dict[str, str],
    *,
    require_inconclusive: bool,
    verification_lines: list[str] | None = None,
) -> RowReferenceVerifyResult:
    aid = article_id_from_row(row) or ""
    title = (row.get("title") or "Untitled").strip()
    needs = row_needs_reference_verify(row)
    evidence = (row.get("codebase_evidence") or "").strip()
    cited = reference_paths_from_text(evidence)
    manual_lines = [line.strip() for line in (verification_lines or []) if line.strip()]
    manual_proof = bool(manual_lines) and _row_has_verification_proof(
        row, verification_lines=manual_lines
    )

    result = RowReferenceVerifyResult(
        article_id=aid,
        title=title,
        needs_verify=needs,
        cited_paths=cited,
    )

    if not cited and needs and require_inconclusive and not manual_proof:
        result.blocking_reason = (
            f"{title}: inconclusive row has no `codebase_evidence` reference paths — "
            "search reference repos manually (braze-docs:reference-repos)"
        )
        return result

    resolved: list[ResolvedEvidencePath] = []
    missing: list[str] = []
    for logical in cited:
        item = resolve_logical_path(logical)
        resolved.append(item)
        if item.filesystem_path is None:
            missing.append(logical)

    result.resolved_paths = resolved
    result.missing_paths = missing

    if missing and not manual_proof:
        result.blocking_reason = (
            f"{title}: reference file(s) not found on disk: " + "; ".join(missing)
        )
        return result

    keywords = keywords_from_row(row)
    for item in resolved:
        if not item.filesystem_path:
            continue
        hits = _search_keywords_in_file(item.filesystem_path, keywords)
        if hits:
            result.keyword_hits.extend(hits)
            result.auto_bullets.append(
                f"Verified **{title}** — found {', '.join(hits)} in `{item.logical_path}`"
            )
        else:
            result.auto_bullets.append(
                f"Verified `{item.logical_path}` exists on disk (CSV `codebase_evidence`)"
            )

    if needs and require_inconclusive and not result.auto_bullets and cited and not manual_proof:
        result.blocking_reason = (
            f"{title}: evidence paths exist but no verification bullets were generated"
        )

    return result


def verify_batch_references(
    rows: list[dict[str, str]],
    *,
    require_inconclusive: bool = True,
    verification_lines: list[str] | None = None,
) -> BatchReferenceVerifyResult:
    batch = BatchReferenceVerifyResult()
    seen_bullets: set[str] = set()

    roots = sibling_repo_roots()
    if not roots["platform"].is_dir():
        batch.missing_repo_roots.append("platform")

    for row in rows:
        row_result = verify_row_reference(
            row,
            require_inconclusive=require_inconclusive,
            verification_lines=verification_lines,
        )
        batch.row_results.append(row_result)
        for bullet in row_result.auto_bullets:
            if bullet not in seen_bullets:
                seen_bullets.add(bullet)
                batch.auto_bullets.append(bullet)

    return batch


def merge_verification_lines(
    manual_lines: list[str],
    auto_bullets: list[str],
) -> list[str]:
    merged: list[str] = []
    seen: set[str] = set()
    for line in [*manual_lines, *auto_bullets]:
        text = line.strip()
        if not text or text in seen:
            continue
        seen.add(text)
        merged.append(text)
    return merged


def format_reference_verify_report(result: BatchReferenceVerifyResult) -> list[str]:
    lines: list[str] = []
    if result.missing_repo_roots:
        lines.append(
            "WARN sibling repo(s) not cloned: "
            + ", ".join(result.missing_repo_roots)
            + " (open braze-workspace.code-workspace or clone siblings)"
        )
    for row in result.row_results:
        if row.blocking_reason:
            lines.append(f"BLOCK {row.blocking_reason}")
        elif row.auto_bullets:
            lines.append(f"OK {row.title}")
    return lines
