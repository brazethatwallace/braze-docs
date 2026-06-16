#!/usr/bin/env python3
"""
Create a BD project Task under Epic BD-6308 after a Salesforce KB Phase 2 PR.

Description format matches existing epic children (for example BD-6402):
  ## GitHub PR
  ## Salesforce Knowledge articles
  ## Product vertical

Requires JIRA_USER_EMAIL and JIRA_API_TOKEN (same secrets as `.github/workflows/jira-pr-comment.yml`).
Optional: JIRA_BASE_URL (default https://jira.atl.braze.com), JIRA_ASSIGNEE_ACCOUNT_ID.

Usage:
  python3 scripts/salesforce-analyzer/sf_kb_jira_ticket.py \\
    --pr-url 'https://github.com/braze-inc/braze-docs/pull/123' \\
    --pr-title '[BD-6402](SF) Example title' \\
    --article-id ka0VP0000008kk1YAA \\
    --doc-path '_docs/_user_guide/messaging/design_and_edit/personalize/liquid/faq.md'

  python3 scripts/salesforce-analyzer/sf_kb_jira_ticket.py --dry-run ...
"""

from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = REPO_ROOT / "_data" / "kb_articles.csv"

EPIC_KEY = "BD-6308"
PROJECT_KEY = "BD"
ISSUE_TYPE = "Task"
EPIC_LINK_FIELD = "customfield_10014"

ARTICLE_ID_IN_BACKTICKS = re.compile(r"`(ka[^`]+)`")
JIRA_KEY_RE = re.compile(r"^BD-\d+$", re.I)
SF_KB_PR_TITLE_KEY_RE = re.compile(r"^\[(BD-\d+)\]\(SF\)\s+", re.I)
GITHUB_PR_URL_RE = re.compile(
    r"https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/pull/(?P<number>\d+)",
    re.I,
)

try:
    from generate_kb_phase1_outputs import product_vertical_hint
except ImportError:  # pragma: no cover
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from generate_kb_phase1_outputs import product_vertical_hint


class JiraTicketError(RuntimeError):
    pass


def _jira_base_url() -> str:
    return os.environ.get("JIRA_BASE_URL", "https://jira.atl.braze.com").rstrip("/")


def _jira_auth_header() -> dict[str, str]:
    email = os.environ.get("JIRA_USER_EMAIL", "").strip()
    token = os.environ.get("JIRA_API_TOKEN", "").strip()
    if not email or not token:
        raise JiraTicketError(
            "Set JIRA_USER_EMAIL and JIRA_API_TOKEN to create Jira issues "
            "(Atlassian API token with permission to create BD issues)."
        )
    encoded = base64.b64encode(f"{email}:{token}".encode()).decode("ascii")
    return {
        "Authorization": f"Basic {encoded}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def strip_legacy_sf_kb_title_prefixes(title: str) -> str:
    """Normalize PR/Jira theme text (strip legacy SF KB and Jira-key prefixes)."""
    theme = title.strip()
    theme = SF_KB_PR_TITLE_KEY_RE.sub("", theme)
    for prefix in ("[SF KB] ", "SF KB: ", "Salesforce KB batch - "):
        if theme.startswith(prefix):
            theme = theme[len(prefix) :].strip()
            break
    return theme


def format_sf_kb_pr_title(issue_key: str, ticket_name: str) -> str:
    """
    GitHub PR title for Jira–GitHub integration under Epic BD-6308.

    Format: ``[BD-####](SF) TICKET_NAME``
    """
    key = issue_key.strip().upper()
    if not JIRA_KEY_RE.match(key):
        raise JiraTicketError(f"Invalid Jira issue key: {issue_key!r}")
    name = strip_legacy_sf_kb_title_prefixes(ticket_name)
    if not name:
        raise JiraTicketError("ticket_name is empty after stripping prefixes")
    return f"[{key}](SF) {name}"


def parse_sf_kb_pr_title(pr_title: str) -> tuple[str | None, str]:
    """Return ``(issue_key or None, ticket_name)`` from a PR title."""
    m = SF_KB_PR_TITLE_KEY_RE.match(pr_title.strip())
    if m:
        return m.group(1).upper(), pr_title[m.end() :].strip()
    return None, strip_legacy_sf_kb_title_prefixes(pr_title)


def batch_summary_from_pr_title(pr_title: str) -> str:
    """Jira summary like BD-6402: Salesforce KB batch - <short theme>."""
    _, theme = parse_sf_kb_pr_title(pr_title)
    return f"Salesforce KB batch - {theme}"


def github_pr_number_from_url(pr_url: str) -> int:
    m = GITHUB_PR_URL_RE.search(pr_url.strip())
    if not m:
        raise JiraTicketError(f"Not a GitHub pull request URL: {pr_url!r}")
    return int(m.group("number"))


SUGGESTED_CHANGE_PREFIX_RE = re.compile(
    r"^(?:Add (?:to|documentation for)\s+[^:]{0,120}:|Consider adding[^:]*:)\s*",
    re.I,
)


def brief_from_suggested_change(suggested: str, *, max_len: int = 220) -> str:
    """First sentence/paragraph of CSV ``suggested_change``, trimmed for PR summaries."""
    text = (suggested or "").strip().split("\n\n", 1)[0].strip()
    text = SUGGESTED_CHANGE_PREFIX_RE.sub("", text).strip("'\"")
    if not text:
        return ""
    if len(text) <= max_len:
        return text
    trimmed = text[: max_len - 1].rsplit(" ", 1)[0]
    return (trimmed or text[: max_len - 1]).rstrip() + "…"


def summary_bullet_from_row(row: dict[str, str]) -> str:
    title = (row.get("title") or row.get("article_id") or "Untitled").strip()
    brief = brief_from_suggested_change(row.get("suggested_change") or "")
    if brief:
        return f"**{title}** — {brief}"
    return f"**{title}** — Adds public docs guidance from Salesforce Knowledge."


def build_pr_summary_section_lines(
    *,
    doc_path: str,
    backlog_rows: list[dict[str, str]],
    summary_bullets: list[str] | None = None,
) -> list[str]:
    """
    Markdown body lines for ``## Summary`` (heading excluded).

    Uses explicit ``summary_bullets`` when provided; otherwise derives one bullet
    per backlog row from ``title`` + ``suggested_change``.
    """
    if summary_bullets:
        bullets = [b.strip() for b in summary_bullets if b.strip()]
    else:
        bullets = [summary_bullet_from_row(row) for row in backlog_rows if row]

    lines = [
        f"Updates `{doc_path}` from Salesforce Knowledge:",
        "",
    ]
    if not bullets:
        lines.append(
            f"* Adds or refines public documentation in `{doc_path}` for the linked Salesforce Knowledge articles."
        )
        return lines

    if len(bullets) == 1:
        single = bullets[0]
        if single.startswith("**"):
            lines.append(single)
        else:
            lines.append(f"* {single}")
        return lines

    lines.extend(f"* {bullet}" for bullet in bullets)
    return lines


def build_change_detail_lines(doc_path: str, backlog_rows: list[dict[str, str]]) -> list[str]:
    """Markdown bullets for the ``## Changes`` section."""
    count = len(backlog_rows)
    lines = [f"* `{doc_path}` — Salesforce Knowledge batch ({count} article(s))"]
    evidence_paths: list[str] = []
    seen: set[str] = set()
    for row in backlog_rows:
        evidence = (row.get("codebase_evidence") or "").strip()
        for match in re.finditer(r"platform/[^\s,;\"']+", evidence):
            path = match.group(0).rstrip(".)")
            if path not in seen:
                seen.add(path)
                evidence_paths.append(path)
    for path in evidence_paths[:5]:
        lines.append(f"  * Verified against `{path}`")
    if len(evidence_paths) > 5:
        lines.append(f"  * …and {len(evidence_paths) - 5} more platform path(s) in CSV evidence")
    return lines


def build_sf_kb_github_pr_body(
    *,
    doc_path: str,
    product_vertical: str,
    articles: list[tuple[str, str]],
    backlog_rows: list[dict[str, str]] | None = None,
    summary_bullets: list[str] | None = None,
    skipped: list[tuple[str, str, str]] | None = None,
) -> str:
    """
    Standard Salesforce KB Phase 2 GitHub PR body.

    Section order: Product vertical → Summary → Changes → Salesforce Knowledge sources
    → optional Skipped → Test plan.
    """
    rows = backlog_rows if backlog_rows is not None else []
    if not rows and articles:
        rows = [{"article_id": aid, "title": title} for aid, title in articles]

    body_lines = [
        "## Product vertical",
        "",
        product_vertical,
        "",
        "## Summary",
        "",
        *build_pr_summary_section_lines(
            doc_path=doc_path,
            backlog_rows=rows,
            summary_bullets=summary_bullets,
        ),
        "",
        "## Changes",
        "",
        *build_change_detail_lines(doc_path, rows),
        "",
        "## Salesforce Knowledge sources",
        "",
    ]
    titles = load_kb_article_titles()
    for aid, fallback in articles:
        ttl = titles.get(aid, fallback)
        body_lines.append(f"* `{aid}` — {ttl}")

    if skipped:
        body_lines.extend(["", "## Skipped in this PR", ""])
        for article_id, title, reason in skipped:
            suffix = f" ({reason})" if reason else ""
            body_lines.append(f"* `{article_id}` — {title}{suffix}")

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
    return "\n".join(body_lines)


def build_description_markdown(
    *,
    pr_title: str | None,
    pr_url: str | None,
    articles: list[tuple[str, str]],
    product_vertical: str,
) -> str:
    lines: list[str] = []
    if pr_url and pr_title:
        lines.extend(
            [
                "## GitHub PR",
                "",
                f"[{pr_title}]({pr_url})",
                "",
            ]
        )
    lines.extend(
        [
            "## Salesforce Knowledge articles",
            "",
        ]
    )
    for article_id, title in articles:
        lines.append(f"* `{article_id}` — {title}")
    lines.extend(
        [
            "",
            "## Product vertical",
            "",
            product_vertical,
        ]
    )
    return "\n".join(lines)


def _adf_text(text: str) -> dict:
    return {"type": "text", "text": text}


def _adf_link(text: str, href: str) -> dict:
    return {
        "type": "text",
        "text": text,
        "marks": [{"type": "link", "attrs": {"href": href}}],
    }


def _adf_code(text: str) -> dict:
    return {"type": "text", "text": text, "marks": [{"type": "code"}]}


def _adf_heading(level: int, text: str) -> dict:
    return {
        "type": "heading",
        "attrs": {"level": level},
        "content": [_adf_text(text)],
    }


def _adf_paragraph(*nodes: dict) -> dict:
    return {"type": "paragraph", "content": list(nodes)}


def build_description_adf(
    *,
    pr_title: str | None,
    pr_url: str | None,
    articles: list[tuple[str, str]],
    product_vertical: str,
) -> dict:
    bullet_items = [
        {
            "type": "listItem",
            "content": [
                _adf_paragraph(
                    _adf_code(article_id),
                    _adf_text(" — "),
                    _adf_text(title),
                )
            ],
        }
        for article_id, title in articles
    ]
    content: list[dict] = []
    if pr_url and pr_title:
        content.extend(
            [
                _adf_heading(2, "GitHub PR"),
                _adf_paragraph(_adf_link(pr_title, pr_url)),
            ]
        )
    content.extend(
        [
            _adf_heading(2, "Salesforce Knowledge articles"),
            {"type": "bulletList", "content": bullet_items},
            _adf_heading(2, "Product vertical"),
            _adf_paragraph(_adf_text(product_vertical)),
        ]
    )
    return {
        "type": "doc",
        "version": 1,
        "content": content,
    }


def load_kb_article_titles() -> dict[str, str]:
    if not CSV_PATH.is_file():
        return {}
    titles: dict[str, str] = {}
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            aid = (row.get("article_id") or "").strip()
            title = (row.get("title") or "").strip()
            if aid and title:
                titles[aid] = title
    return titles


def resolve_article_titles(
    articles: list[tuple[str, str]],
    *,
    title_lookup: dict[str, str] | None = None,
) -> list[tuple[str, str]]:
    lookup = title_lookup if title_lookup is not None else load_kb_article_titles()
    resolved: list[tuple[str, str]] = []
    for article_id, fallback in articles:
        aid = article_id.strip()
        title = lookup.get(aid) or fallback.strip() or aid
        resolved.append((aid, title))
    return resolved


def articles_from_markdown_table(text: str) -> list[tuple[str, str]]:
    """Extract `article_id` values from a PR/Jira summary table; titles from CSV when possible."""
    ids = ARTICLE_ID_IN_BACKTICKS.findall(text)
    if not ids:
        return []
    lookup = load_kb_article_titles()
    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for aid in ids:
        if aid in seen:
            continue
        seen.add(aid)
        out.append((aid, lookup.get(aid, aid)))
    return out


def infer_product_vertical(*, doc_path: str | None, override: str | None) -> str:
    if override and override.strip():
        return override.strip()
    if doc_path and doc_path.strip():
        return product_vertical_hint(doc_path.replace("\\", "/").strip())
    return "Documentation"


def _jira_request(
    method: str,
    path: str,
    *,
    payload: dict | None = None,
    timeout: int = 60,
) -> dict | list | None:
    url = f"{_jira_base_url()}{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        headers=_jira_auth_header(),
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            if not raw.strip():
                return None
            return json.loads(raw)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise JiraTicketError(f"Jira API HTTP {exc.code} {method} {path}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise JiraTicketError(f"Jira API request failed: {exc}") from exc


def _create_bd6308_issue_fields(
    *,
    ticket_name: str,
    articles: list[tuple[str, str]],
    doc_path: str | None,
    product_vertical: str | None,
    pr_title: str | None,
    pr_url: str | None,
) -> dict:
    if not articles:
        raise JiraTicketError("At least one article_id is required")
    resolved_articles = resolve_article_titles(articles)
    vertical = infer_product_vertical(doc_path=doc_path, override=product_vertical)
    theme = strip_legacy_sf_kb_title_prefixes(ticket_name)
    if not theme:
        raise JiraTicketError("ticket_name is empty after stripping prefixes")
    summary = f"Salesforce KB batch - {theme}"
    description_adf = build_description_adf(
        pr_title=pr_title.strip() if pr_title else None,
        pr_url=pr_url.strip() if pr_url else None,
        articles=resolved_articles,
        product_vertical=vertical,
    )
    fields: dict = {
        "project": {"key": PROJECT_KEY},
        "issuetype": {"name": ISSUE_TYPE},
        "summary": summary,
        "description": description_adf,
        "parent": {"key": EPIC_KEY},
        EPIC_LINK_FIELD: EPIC_KEY,
        "priority": {"name": "P4"},
    }
    assignee = os.environ.get("JIRA_ASSIGNEE_ACCOUNT_ID", "").strip()
    if assignee:
        fields["assignee"] = {"accountId": assignee}
    return fields


def create_bd6308_task_prep(
    *,
    ticket_name: str,
    articles: list[tuple[str, str]],
    doc_path: str | None = None,
    product_vertical: str | None = None,
    dry_run: bool = False,
) -> str:
    """
    Create a BD-6308 Task before the GitHub PR exists (description omits PR link).
    Returns the new issue key (for example BD-6402).
    """
    fields = _create_bd6308_issue_fields(
        ticket_name=ticket_name,
        articles=articles,
        doc_path=doc_path,
        product_vertical=product_vertical,
        pr_title=None,
        pr_url=None,
    )
    if dry_run:
        print(json.dumps({"fields": fields}, indent=2))
        return "DRY-RUN"
    body = _jira_request("POST", "/rest/api/3/issue", payload={"fields": fields})
    key = (body or {}).get("key") if isinstance(body, dict) else None
    if not key:
        raise JiraTicketError(f"Jira API returned no issue key: {body!r}")
    return str(key)


def update_bd6308_task_pr_link(
    issue_key: str,
    *,
    pr_url: str,
    pr_title: str,
    articles: list[tuple[str, str]],
    doc_path: str | None = None,
    product_vertical: str | None = None,
    dry_run: bool = False,
) -> None:
    """Attach GitHub PR link and formatted PR title to an existing BD-6308 task."""
    fields = _create_bd6308_issue_fields(
        ticket_name=strip_legacy_sf_kb_title_prefixes(pr_title),
        articles=articles,
        doc_path=doc_path,
        product_vertical=product_vertical,
        pr_title=pr_title.strip(),
        pr_url=pr_url.strip(),
    )
    payload = {"fields": {"description": fields["description"]}}
    if dry_run:
        print(json.dumps(payload, indent=2))
        return
    _jira_request("PUT", f"/rest/api/3/issue/{issue_key.strip().upper()}", payload=payload)


def create_bd6308_task(
    *,
    pr_url: str,
    pr_title: str,
    articles: list[tuple[str, str]],
    doc_path: str | None = None,
    product_vertical: str | None = None,
    dry_run: bool = False,
) -> str:
    """
    Create a Task linked to Epic BD-6308 with PR link in the description.
    Returns the new issue key (for example BD-6402).
    """
    if not pr_url.strip():
        raise JiraTicketError("pr_url is required")
    if not pr_title.strip():
        raise JiraTicketError("pr_title is required")
    fields = _create_bd6308_issue_fields(
        ticket_name=pr_title,
        articles=articles,
        doc_path=doc_path,
        product_vertical=product_vertical,
        pr_title=pr_title.strip(),
        pr_url=pr_url.strip(),
    )
    if dry_run:
        print(json.dumps({"fields": fields}, indent=2))
        print()
        resolved = resolve_article_titles(articles)
        print(
            build_description_markdown(
                pr_title=pr_title.strip(),
                pr_url=pr_url.strip(),
                articles=resolved,
                product_vertical=infer_product_vertical(
                    doc_path=doc_path, override=product_vertical
                ),
            )
        )
        return "DRY-RUN"
    body = _jira_request("POST", "/rest/api/3/issue", payload={"fields": fields})
    key = (body or {}).get("key") if isinstance(body, dict) else None
    if not key:
        raise JiraTicketError(f"Jira API returned no issue key: {body!r}")
    return str(key)


def gh_pr_edit_title(
    pr_url: str,
    new_title: str,
    *,
    repo: str = "braze-inc/braze-docs",
    dry_run: bool = False,
) -> None:
    """Rename a GitHub PR (works for open and merged PRs)."""
    import subprocess

    number = github_pr_number_from_url(pr_url)
    cmd = ["gh", "pr", "edit", str(number), "--repo", repo, "--title", new_title]
    if dry_run:
        print(f"dry-run: {' '.join(cmd)}")
        return
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise JiraTicketError(
            f"gh pr edit failed for #{number}: {proc.stderr.strip() or proc.stdout.strip()}"
        )


def maybe_create_bd6308_task(
    *,
    pr_url: str,
    pr_title: str,
    articles: list[tuple[str, str]],
    doc_path: str | None = None,
    product_vertical: str | None = None,
    skip_jira: bool = False,
    dry_run: bool = False,
    rename_pr: bool = True,
) -> str | None:
    """
    Create Jira issue unless skipped; rename the PR to ``[BD-####](SF) TICKET_NAME`` when
    ``rename_pr`` is true (default) so Jira–GitHub integration can track the epic.
    """
    if skip_jira:
        return None
    ticket_name = strip_legacy_sf_kb_title_prefixes(pr_title)
    try:
        key = create_bd6308_task_prep(
            ticket_name=ticket_name,
            articles=articles,
            doc_path=doc_path,
            product_vertical=product_vertical,
            dry_run=dry_run,
        )
        if dry_run or key == "DRY-RUN":
            formatted = format_sf_kb_pr_title("BD-0000", ticket_name)
            print(f"dry-run PR title would be: {formatted}")
            return key
        formatted_title = format_sf_kb_pr_title(key, ticket_name)
        if rename_pr and formatted_title != pr_title.strip():
            gh_pr_edit_title(pr_url, formatted_title, dry_run=dry_run)
        update_bd6308_task_pr_link(
            key,
            pr_url=pr_url,
            pr_title=formatted_title,
            articles=articles,
            doc_path=doc_path,
            product_vertical=product_vertical,
            dry_run=dry_run,
        )
    except JiraTicketError as exc:
        print(f"WARN: Jira ticket not created: {exc}", file=sys.stderr)
        return None
    base = _jira_base_url()
    print(f"Jira {key}: {base}/browse/{key}")
    return key


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr-url", required=True)
    parser.add_argument("--pr-title", required=True)
    parser.add_argument(
        "--article-id",
        action="append",
        default=[],
        metavar="ID",
        help="Salesforce Knowledge article_id (repeatable)",
    )
    parser.add_argument(
        "--article",
        action="append",
        default=[],
        metavar="ID:TITLE",
        help="article_id and title, colon-separated (repeatable)",
    )
    parser.add_argument("--articles-from-summary", help="Markdown table with `article_id` backticks")
    parser.add_argument("--doc-path", help="Primary _docs path for product vertical inference")
    parser.add_argument("--product-vertical", help="Override inferred product vertical")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    articles: list[tuple[str, str]] = []
    for spec in args.article:
        if ":" in spec:
            aid, title = spec.split(":", 1)
            articles.append((aid.strip(), title.strip()))
        else:
            articles.append((spec.strip(), ""))
    for aid in args.article_id:
        articles.append((aid.strip(), ""))
    if args.articles_from_summary:
        articles.extend(articles_from_markdown_table(args.articles_from_summary))

    if not articles:
        parser.error("Provide --article-id, --article, or --articles-from-summary")

    key = create_bd6308_task(
        pr_url=args.pr_url,
        pr_title=args.pr_title,
        articles=articles,
        doc_path=args.doc_path,
        product_vertical=args.product_vertical,
        dry_run=args.dry_run,
    )
    if not args.dry_run:
        print(key)


if __name__ == "__main__":
    main()
