#!/usr/bin/env python3
"""
AI style review for Braze Docs pull requests (Copilot-style editorial feedback).

Fetches changed Markdown in a PR, sends diffs to Claude with the Braze writing
style reference, and posts a pull request review with inline suggestion comments
where GitHub allows one-click Commit.

Environment:
    PR_NUMBER          Required
    HEAD_SHA           PR head commit (for review comments)
    GITHUB_REPOSITORY  owner/repo
    GITHUB_BASE_REF    Base branch name (e.g. develop)
    ANTHROPIC_API_KEY  Required
    REVIEW_MODEL       Optional (default claude-sonnet-4-20250514)
    MAX_INLINE_COMMENTS Optional (default 25)
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import difflib
from pathlib import Path

REPO = os.environ.get("GITHUB_REPOSITORY", "braze-inc/braze-docs")
PR_NUMBER = os.environ.get("PR_NUMBER", "")
HEAD_SHA = os.environ.get("HEAD_SHA", "")
HEAD_REF = os.environ.get("GITHUB_HEAD_REF", "")
BASE_REF = os.environ.get("GITHUB_BASE_REF", "develop")
REVIEW_MODEL = os.environ.get("REVIEW_MODEL", "claude-sonnet-4-20250514")
MAX_INLINE = int(os.environ.get("MAX_INLINE_COMMENTS", "25"))
MAX_FILES = int(os.environ.get("MAX_STYLE_REVIEW_FILES", "25"))
MAX_DIFF_CHARS = int(os.environ.get("MAX_STYLE_DIFF_CHARS", "12000"))
NEARBY_LINE_WINDOW = int(os.environ.get("STYLE_REVIEW_NEARBY_LINE_WINDOW", "3"))
AUTO_TRANSLATE_BRANCH_PREFIX = "auto-translate/"

REPO_ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd()))
STYLE_REF = REPO_ROOT / ".github/skills/braze-docs/references/writing-style.md"
GLOSSARY_REF = REPO_ROOT / ".github/skills/braze-docs/references/glossary.md"
SUMMARY_MARKER = "<!-- braze-docs-style-review -->"
CODE_ONLY_SKIP_MARKER = "<!-- braze-docs-style-review:code-only -->"
SUMMARY_FILE = REPO_ROOT / "docs_style_review_summary.md"

MARKDOWN_PREFIXES = ("_docs/", "_includes/", "_lang/")

STYLE_REVIEW_INLINE_MARKER = "**Docs style review**"
REJECT_STYLE_REVIEW_MARKER = "<!-- reject-style-review -->"
REJECT_REPLY_PHRASES = (
    "reject",
    "/reject",
    "wontfix",
    "won't fix",
    "won’t fix",
)
DISMISS_INSTRUCTION_FOOTER = (
    "\n\n---\n"
    "If you disagree, **Resolve conversation** on this thread or reply `reject` "
    "— the bot won't suggest this again on this PR."
)
BOT_LOGINS = frozenset({"github-actions[bot]", "cursor[bot]"})

SYSTEM_PROMPT = """\
You are a senior technical editor reviewing Braze documentation pull requests.
Apply the Braze Docs Style Guide provided in the user message.

## Review scope

- Editorial quality: voice, tone, clarity, active voice, second person, present tense.
- Style guide compliance: headings, UI formatting, links, lists, numbers, alerts, inclusive language.
- Braze terminology: Canvas, workspace (not app group), customers (not clients), allowlist/blocklist, etc.
- Internal consistency within a file beats isolated style preferences (match dominant usage in the
  same article before suggesting a one-off change).
- Present tense: target future "will"/"would" for user-action outcomes—not a blanket ban on past
  tense or on "may"/"may have" for uncertainty. Past tense is appropriate when describing events
  that already occurred (troubleshooting, delivery logs, incident timelines). Do not rewrite table
  "Possible cause" rows from past to present tense solely for consistency.
- Do NOT flag product behavior you cannot verify from the diff alone.
- Do NOT invent facts or suggest content unrelated to the change.
- Do NOT suggest adding sections, alerts, FAQs, or blocks that already appear in the numbered
  file excerpt. Compare your suggestion to that excerpt before including an inline item.
- For `_lang/` locale files: review only editorial issues in changed lines. Do not infer missing
  content from the English site; if the excerpt already contains the passage, omit the item.
- Do NOT suggest removing `&nbsp;` between a number and a unit (for example `512&nbsp;MB`).
  Braze docs require non-breaking spaces for units of measurement; see the style reference.

## Output rules

Respond with ONLY valid JSON (no markdown fences). Schema:

{
  "inline": [
    {
      "path": "repo-relative/path.md",
      "line": 42,
      "message": "Short explanation for the author (one or two sentences).",
      "suggested_line": "Full replacement text for this single line on the NEW file side."
    }
  ],
  "summary": [
    "PR-level notes that are not tied to a single line (optional)."
  ]
}

- "message" must describe ONLY the specific edit you are making—the difference between
  the current line in the numbered excerpt and suggested_line. Name the exact word(s) or
  punctuation being changed (for example: `Replace "click" with "select" for the toolbar
  action.`). Do not restate a style rule that is not reflected in that diff.
- Do not mention "click", tense changes, "for example", or other issues unless
  suggested_line actually changes those words on that line. If the line already complies,
  omit the item.
- Use straight quotation marks and apostrophes in prose, not curly/smart typography.

- "line" is the 1-based line number on the RIGHT (new) side of the diff for the exact line you
  are replacing. It must match the numbered file excerpt (not a nearby blank line, Liquid tag,
  kramdown attribute line, or adjacent table row).
- For markdown table rows, anchor the comment on the row you are changing—verify the "Possible
  cause" cell in suggested_line matches that same row, not the row above or below.
- Only suggest lines that appear in the unified diff (added or context lines within a hunk).
  GitHub cannot attach inline comments to unchanged lines outside the PR diff.
- "suggested_line" must be the complete single-line replacement (not a fragment, not multiple lines).
- "suggested_line" must differ from the current text on that line number in the numbered excerpt.
  Do not suggest text that is already in the file.
- Only include inline items when you are confident and the fix is a single-line change.
- Prefer high-signal issues; omit nitpicks and subjective preferences.
- If prior automated suggestions on this PR are listed in the user message, do not contradict them
  on the same line (especially opposite capitalization or wording reversals).
- If dismissed suggestions are listed in the user message, do not repeat them on this PR.
- Maximum """ + str(MAX_INLINE) + """ inline items across the whole PR.
- Use an empty "inline" array if the diff looks compliant.
- Do not include customer PII or internal repo paths in messages.
"""


def _run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=check,
    )


def _is_auto_translate_pr() -> bool:
    return HEAD_REF.startswith(AUTO_TRANSLATE_BRANCH_PREFIX)


def get_changed_markdown_files() -> list[str]:
    base = f"origin/{BASE_REF}"
    result = _run(
        ["git", "diff", "--name-only", "--diff-filter=ACMRT", f"{base}...HEAD", "--", *MARKDOWN_PREFIXES],
        check=False,
    )
    if result.returncode != 0:
        print(f"git diff warning: {result.stderr.strip()}", file=sys.stderr)
        return []
    skip_lang = _is_auto_translate_pr()
    if skip_lang:
        print(
            "Auto-translate PR detected; skipping `_lang/` files "
            "(English source is reviewed separately)."
        )
    files = []
    for line in result.stdout.splitlines():
        path = line.strip()
        if not path.endswith(".md"):
            continue
        if skip_lang and path.startswith("_lang/"):
            continue
        files.append(path)
    return files[:MAX_FILES]


def get_pr_diff_paths() -> set[str]:
    """All paths changed in this PR (any file type), for stale-comment cleanup."""
    base = f"origin/{BASE_REF}"
    result = _run(
        ["git", "diff", "--name-only", "--diff-filter=ACMRTD", f"{base}...HEAD"],
        check=False,
    )
    if result.returncode != 0:
        print(f"git diff warning: {result.stderr.strip()}", file=sys.stderr)
        return set()
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def _is_bot_login(login: str) -> bool:
    return login in BOT_LOGINS or login.endswith("[bot]")


def _graphql(query: str, variables: dict) -> dict | None:
    result = subprocess.run(
        ["gh", "api", "graphql", "--input", "-"],
        input=json.dumps({"query": query, "variables": variables}),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        check=False,
    )
    if result.returncode != 0:
        print(f"GraphQL warning: {result.stderr.strip()}", file=sys.stderr)
        return None
    payload = json.loads(result.stdout)
    if payload.get("errors"):
        print(f"GraphQL errors: {payload['errors']}", file=sys.stderr)
        return None
    return payload.get("data")


def _fetch_review_threads() -> list[dict]:
    owner, repo = REPO.split("/", 1)
    threads: list[dict] = []
    cursor: str | None = None
    query = """
    query($owner: String!, $name: String!, $number: Int!, $after: String) {
      repository(owner: $owner, name: $name) {
        pullRequest(number: $number) {
          reviewThreads(first: 100, after: $after) {
            pageInfo { hasNextPage endCursor }
            nodes {
              id
              isResolved
              isOutdated
              path
              comments(first: 50) {
                nodes {
                  databaseId
                  body
                  author { login }
                }
              }
            }
          }
        }
      }
    }
    """
    while True:
        variables: dict = {
            "owner": owner,
            "name": repo,
            "number": int(PR_NUMBER),
        }
        if cursor:
            variables["after"] = cursor
        data = _graphql(query, variables)
        if not data:
            break
        review_threads = data["repository"]["pullRequest"]["reviewThreads"]
        threads.extend(review_threads["nodes"])
        page_info = review_threads["pageInfo"]
        if not page_info["hasNextPage"]:
            break
        cursor = page_info["endCursor"]
    return threads


def _is_our_style_thread(thread: dict) -> bool:
    nodes = thread.get("comments", {}).get("nodes", [])
    if not nodes:
        return False
    return STYLE_REVIEW_INLINE_MARKER in (nodes[0].get("body") or "")


def _thread_has_human_followup(thread: dict) -> bool:
    nodes = thread.get("comments", {}).get("nodes", [])
    for comment in nodes[1:]:
        login = (comment.get("author") or {}).get("login", "")
        if login and not _is_bot_login(login):
            return True
    return False


def _human_rejected_thread(thread: dict) -> bool:
    nodes = thread.get("comments", {}).get("nodes", [])
    for comment in nodes[1:]:
        login = (comment.get("author") or {}).get("login", "")
        if not login or _is_bot_login(login):
            continue
        body = (comment.get("body") or "").strip().lower()
        if REJECT_STYLE_REVIEW_MARKER in (comment.get("body") or ""):
            return True
        if body in REJECT_REPLY_PHRASES:
            return True
        if body.startswith("/reject"):
            return True
    return False


def _extract_style_review_message(body: str) -> str | None:
    if STYLE_REVIEW_INLINE_MARKER not in body:
        return None
    match = re.search(
        r"\*\*Docs style review\*\* — (.+?)(?:\n\n```|\Z)",
        body,
        re.DOTALL,
    )
    return match.group(1).strip() if match else None


def _parse_style_thread_first_comment(thread: dict) -> tuple[str, str | None, str | None] | None:
    """Return (path, suggested_line, message) from the bot's opening comment."""
    path = thread.get("path") or ""
    nodes = thread.get("comments", {}).get("nodes", [])
    if not path or not nodes:
        return None
    body = nodes[0].get("body") or ""
    if STYLE_REVIEW_INLINE_MARKER not in body:
        return None
    suggested = _parse_suggestion_body(body)
    message = _extract_style_review_message(body)
    if not suggested and not message:
        return None
    return path, suggested, message


def fetch_dismissed_style_suggestions() -> tuple[set[tuple[str, str]], set[tuple[str, str]]]:
    """
    Suggestions reviewers dismissed on this PR.

    Returns:
        dismissed_suggested: (path, suggested_line) pairs
        dismissed_message: (path, review_message) pairs
    """
    dismissed_suggested: set[tuple[str, str]] = set()
    dismissed_message: set[tuple[str, str]] = set()

    for thread in _fetch_review_threads():
        if not _is_our_style_thread(thread):
            continue
        rejected = _human_rejected_thread(thread)
        if not thread.get("isResolved") and not rejected:
            continue
        parsed = _parse_style_thread_first_comment(thread)
        if not parsed:
            continue
        path, suggested, message = parsed
        if suggested:
            dismissed_suggested.add((path, suggested.rstrip()))
        if message:
            dismissed_message.add((path, message.rstrip()))
        print(
            f"Honoring dismissed style review on `{path}` "
            f"(resolved={thread.get('isResolved')}, reject_reply={rejected})"
        )

    return dismissed_suggested, dismissed_message


def format_dismissed_section(
    dismissed_suggested: set[tuple[str, str]],
    dismissed_message: set[tuple[str, str]],
) -> str:
    if not dismissed_suggested and not dismissed_message:
        return ""
    lines = [
        "## Dismissed suggestions on this PR",
        "",
        "Reviewers resolved or rejected these. Do not suggest them again:",
        "",
    ]
    seen: set[tuple[str, str, str]] = set()
    for path, suggested in sorted(dismissed_suggested):
        key = (path, "suggested", suggested)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- `{path}`: `{suggested}`")
    for path, message in sorted(dismissed_message):
        key = (path, "message", message)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- `{path}`: _{message}_")
    lines.append("")
    return "\n".join(lines)


def filter_dismissed_suggestions(
    inline: list[dict],
    dismissed_suggested: set[tuple[str, str]],
    dismissed_message: set[tuple[str, str]],
) -> list[dict]:
    kept: list[dict] = []
    for item in inline:
        path = item["path"]
        suggested = item["suggested_line"].rstrip()
        message = item["message"].rstrip()
        if (path, suggested) in dismissed_suggested:
            print(f"Skipping dismissed suggestion on `{path}` (matched prior suggested line)")
            continue
        if (path, message) in dismissed_message:
            print(f"Skipping dismissed suggestion on `{path}` (matched prior review message)")
            continue
        kept.append(item)
    return kept


def filter_duplicate_prior_suggestions(
    inline: list[dict],
    prior_suggestions: dict[tuple[str, int], list[str]],
) -> list[dict]:
    """Skip exact suggested text already posted on this PR (even if line shifted)."""
    by_path: dict[str, set[str]] = {}
    for (path, _line), texts in prior_suggestions.items():
        by_path.setdefault(path, set()).update(text.rstrip() for text in texts)

    kept: list[dict] = []
    for item in inline:
        if item["suggested_line"].rstrip() in by_path.get(item["path"], set()):
            print(
                f"Skipping duplicate suggestion on `{item['path']}` "
                "(same suggested line already posted on this PR)"
            )
            continue
        kept.append(item)
    return kept


def _delete_review_comment(comment_id: int) -> bool:
    owner, repo = REPO.split("/", 1)
    result = subprocess.run(
        [
            "gh",
            "api",
            "--method",
            "DELETE",
            f"repos/{owner}/{repo}/pulls/comments/{comment_id}",
        ],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        print(
            f"DELETE comment {comment_id} failed: {result.stderr.strip()}",
            file=sys.stderr,
        )
        return False
    return True


def _resolve_review_thread(thread_id: str) -> bool:
    mutation = """
    mutation($threadId: ID!) {
      resolveReviewThread(input: {threadId: $threadId}) {
        thread { isResolved }
      }
    }
    """
    return _graphql(mutation, {"threadId": thread_id}) is not None


def cleanup_stale_style_review_comments() -> int:
    """Remove or resolve bot threads when the file leaves the PR or the comment is outdated."""
    diff_paths = get_pr_diff_paths()
    cleaned = 0

    for thread in _fetch_review_threads():
        if thread.get("isResolved"):
            continue
        if not _is_our_style_thread(thread):
            continue
        if _thread_has_human_followup(thread):
            continue

        path = thread.get("path") or ""
        is_outdated = bool(thread.get("isOutdated"))
        path_removed = path not in diff_paths
        if not is_outdated and not path_removed:
            continue

        nodes = thread.get("comments", {}).get("nodes", [])
        ours = [
            c
            for c in nodes
            if STYLE_REVIEW_INLINE_MARKER in (c.get("body") or "")
            or _is_bot_login((c.get("author") or {}).get("login", ""))
        ]
        deleted_all = bool(ours) and all(
            c.get("databaseId") and _delete_review_comment(int(c["databaseId"]))
            for c in ours
        )

        if deleted_all:
            cleaned += 1
            print(
                f"Deleted stale style review thread on `{path}` "
                f"(outdated={is_outdated}, path_removed={path_removed})"
            )
        elif _resolve_review_thread(thread["id"]):
            cleaned += 1
            print(
                f"Resolved stale style review thread on `{path}` "
                f"(outdated={is_outdated}, path_removed={path_removed})"
            )

    return cleaned


def file_diff(path: str) -> str:
    base = f"origin/{BASE_REF}"
    result = _run(
        ["git", "diff", f"{base}...HEAD", "--", path],
        check=False,
    )
    text = result.stdout if result.returncode == 0 else ""
    if len(text) > MAX_DIFF_CHARS:
        text = text[:MAX_DIFF_CHARS] + "\n\n…(diff truncated)\n"
    return text


# Per-file gate: run editorial review only when the diff includes user-facing copy.
# Skips diffs that touch only inline code, fenced blocks, CSS/HTML, Liquid, or markup
# (same non-prose categories called out in scripts/translation_prompt.md).
_PROSE_LETTERS = re.compile(
    r"[A-Za-zÀ-ÿ\u0400-\u04ff\u3040-\u30ff\u4e00-\u9fff]{4,}"
)
_CSS_PROPERTY_LINE = re.compile(r"^\s*[\w-]+\s*:\s*.+;\s*$")


def _strip_non_prose_fragments(line: str) -> str:
    text = line
    text = re.sub(r"\{%.*?%\}", "", text)
    text = re.sub(r"\{\{.*?\}\}", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\{:[^}]+\}", "", text)
    text = re.sub(r"\{#[^}]+\}", "", text)
    return text.strip()


def _line_is_inline_code_only(stripped: str) -> bool:
    """True when the line edits only backtick inline code (no surrounding prose)."""
    if "`" not in stripped:
        return False
    without_code = re.sub(r"`[^`]*`", "", stripped)
    without_code = re.sub(r"^\s*[-*+\d.]+\s*", "", without_code)
    without_code = re.sub(r"[|:\s]", "", without_code)
    return not without_code or not _PROSE_LETTERS.search(without_code)


def _line_is_css_like(stripped: str) -> bool:
    if _CSS_PROPERTY_LINE.match(stripped):
        return True
    if re.match(r"^\s*\}\s*,?\s*$", stripped):
        return True
    if re.match(r"^\s*[\w.#@][^{]*\{\s*$", stripped):
        return True
    if re.match(r"^\s*[\w.#][^;{]*,\s*$", stripped):
        return True
    if re.search(r":(?:focus|hover|not|visible|before|after|active)", stripped):
        if re.search(r"^\s*[\w.#\[]", stripped):
            return True
    return False


def _diff_line_likely_prose(line: str) -> bool:
    """True when a changed diff line probably edits user-facing copy."""
    stripped = line.rstrip()
    if not stripped:
        return False
    if _line_is_inline_code_only(stripped):
        return False
    if _line_is_css_like(stripped):
        return False
    if stripped.startswith("<!--") or stripped.startswith("{%") or stripped.startswith("{{"):
        return False
    if stripped.startswith("```") or stripped.startswith("~~~"):
        return False
    if re.match(r"^\s*\|[-: |]+\|\s*$", stripped):
        return False
    if re.match(r"^\s*---\s*$", stripped):
        return False
    lower = stripped.lower()
    if lower.startswith("<style") or lower.startswith("</style"):
        return False
    if stripped in {"}", "{", "};"}:
        return False
    remainder = _strip_non_prose_fragments(stripped)
    return bool(_PROSE_LETTERS.search(remainder))


def diff_has_prose_changes(path: str) -> bool:
    """True when the PR diff for this file includes user-facing copy edits."""
    diff = file_diff(path)
    if not diff.strip():
        return False

    in_style = False
    in_code_fence = False
    for raw in diff.splitlines():
        if raw.startswith("+++") or raw.startswith("---") or raw.startswith("@@"):
            continue
        if not raw.startswith(("+", "-")):
            continue
        line = raw[1:]

        lower = line.lower()
        if "<style" in lower:
            in_style = True
        if "</style>" in lower:
            in_style = False
            continue
        if in_style:
            continue

        if line.strip().startswith("```") or line.strip().startswith("~~~"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue

        if _diff_line_likely_prose(line):
            return True
    return False


def filter_files_with_prose_changes(files: list[str]) -> tuple[list[str], list[str]]:
    """Split changed markdown files into prose edits vs code/structure-only edits."""
    prose_files: list[str] = []
    code_only: list[str] = []
    for path in files:
        if diff_has_prose_changes(path):
            prose_files.append(path)
        else:
            code_only.append(path)
            print(f"Skipping `{path}` (diff changes code/markup only, not user-facing copy)")
    return prose_files, code_only


_HUNK_HEADER = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")


def get_diff_commentable_lines(path: str) -> set[int]:
    """RIGHT-side line numbers that GitHub allows inline review comments on."""
    commentable: set[int] = set()
    new_line = 0
    in_hunk = False
    for line in file_diff(path).splitlines():
        hunk = _HUNK_HEADER.match(line)
        if hunk:
            new_line = int(hunk.group(1))
            in_hunk = True
            continue
        if not in_hunk or line.startswith(("--- ", "+++ ")):
            continue
        if line.startswith("+") or line.startswith(" "):
            commentable.add(new_line)
            new_line += 1
        elif line.startswith("-"):
            continue
        else:
            in_hunk = False
    return commentable


def filter_to_diff_lines(inline: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split suggestions into postable (in diff) vs manual fallback (outside diff)."""
    lines_by_path: dict[str, set[int]] = {}
    in_diff: list[dict] = []
    outside_diff: list[dict] = []
    for item in inline:
        path = item["path"]
        if path not in lines_by_path:
            lines_by_path[path] = get_diff_commentable_lines(path)
        if item["line"] in lines_by_path[path]:
            in_diff.append(item)
        else:
            outside_diff.append(item)
            print(
                f"Skipping inline on `{path}` line {item['line']} "
                "(outside PR diff; will list in summary comment)"
            )
    return in_diff, outside_diff


def numbered_excerpt(path: str, max_lines: int = 120) -> str:
    p = REPO_ROOT / path
    if not p.exists():
        return ""
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(lines) <= max_lines:
        numbered = [f"{i + 1:5d}| {l}" for i, l in enumerate(lines)]
    else:
        numbered = [f"{i + 1:5d}| {l}" for i, l in enumerate(lines[:max_lines])]
        numbered.append(f"     | …({len(lines) - max_lines} more lines)")
    return "\n".join(numbered)


def load_style_context() -> str:
    parts = []
    if STYLE_REF.exists():
        parts.append("## Braze Docs style reference\n\n" + STYLE_REF.read_text(encoding="utf-8"))
    if GLOSSARY_REF.exists():
        glossary = GLOSSARY_REF.read_text(encoding="utf-8")
        if len(glossary) > 6000:
            glossary = glossary[:6000] + "\n\n…(glossary truncated)\n"
        parts.append("## Glossary excerpt\n\n" + glossary)
    return "\n\n".join(parts)


def build_user_prompt(
    files: list[str],
    prior_suggestions: dict[tuple[str, int], list[str]] | None = None,
    dismissed_suggested: set[tuple[str, str]] | None = None,
    dismissed_message: set[tuple[str, str]] | None = None,
) -> str:
    sections = [load_style_context(), f"## Pull request #{PR_NUMBER}\n"]
    if prior_suggestions:
        sections.append(format_prior_suggestions_section(prior_suggestions))
    if dismissed_suggested or dismissed_message:
        sections.append(
            format_dismissed_section(
                dismissed_suggested or set(),
                dismissed_message or set(),
            )
        )
    for path in files:
        diff = file_diff(path)
        if not diff.strip():
            continue
        sections.append(
            f"### File: `{path}`\n\n"
            f"#### Unified diff\n```diff\n{diff}\n```\n\n"
            f"#### New file (numbered)\n```\n{numbered_excerpt(path)}\n```\n"
        )
    sections.append(
        "\nReview only the files above. Return JSON per the schema."
    )
    return "\n".join(sections)


def call_claude(user_prompt: str) -> dict:
    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: pip install anthropic", file=sys.stderr)
        sys.exit(1)

    client = Anthropic()
    response = client.messages.create(
        model=REVIEW_MODEL,
        max_tokens=8192,
        temperature=0,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )
    text = response.content[0].text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON from model: {exc}", file=sys.stderr)
        print(text[:3000], file=sys.stderr)
        sys.exit(1)
    if not isinstance(data, dict):
        print("ERROR: expected JSON object", file=sys.stderr)
        sys.exit(1)
    data.setdefault("inline", [])
    data.setdefault("summary", [])
    return data


def _block_exists_in_file(suggested: str, file_lines: list[str]) -> bool:
    suggested_lines = [line.rstrip() for line in suggested.splitlines() if line.strip()]
    if not suggested_lines:
        return False
    if len(suggested_lines) == 1:
        target = suggested_lines[0]
        return any(line.rstrip() == target for line in file_lines)
    block_len = len(suggested_lines)
    for start in range(len(file_lines) - block_len + 1):
        if all(
            file_lines[start + offset].rstrip() == suggested_lines[offset]
            for offset in range(block_len)
        ):
            return True
    return False


def _table_row_first_cell(line: str) -> str:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return ""
    parts = [part.strip() for part in stripped.split("|")]
    return parts[1] if len(parts) > 2 else ""


def _normalize_cause_label(text: str) -> str:
    normalized = text.lower().replace("'", "")
    normalized = re.sub(r"[^\w\s]", " ", normalized)
    for word in (
        "the",
        "a",
        "an",
        "was",
        "were",
        "is",
        "are",
        "wasnt",
        "isnt",
        "has",
        "have",
        "had",
        "may",
        "might",
        "will",
        "would",
        "not",
    ):
        normalized = re.sub(rf"\b{re.escape(word)}\b", " ", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def _is_non_commentable_markdown_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith("{%") or stripped.startswith("{:"):
        return True
    if stripped in ("---", "|---|", "| --- |"):
        return True
    if re.fullmatch(r"\|[-:\s|]+\|?", stripped):
        return True
    return False


def _is_wrong_table_row_anchor(
    file_lines: list[str], line_num: int, suggested: str
) -> bool:
    """True when a table-row suggestion clearly belongs on the previous row."""
    if line_num < 2 or line_num > len(file_lines):
        return False
    current = file_lines[line_num - 1]
    previous = file_lines[line_num - 2]
    current_cell = _table_row_first_cell(current)
    previous_cell = _table_row_first_cell(previous)
    suggested_cell = _table_row_first_cell(suggested)
    if not current_cell or not previous_cell or not suggested_cell:
        return False
    current_norm = _normalize_cause_label(current_cell)
    previous_norm = _normalize_cause_label(previous_cell)
    suggested_norm = _normalize_cause_label(suggested_cell)
    if not suggested_norm:
        return False
    if suggested_norm == current_norm:
        return False
    return suggested_norm == previous_norm


_TENSE_NAG_MSG = re.compile(
    r"present tense|past tense|might not|'\bmay\b|'\bwas\b", re.IGNORECASE
)
_TROUBLESHOOTING_PAST_CAUSE = re.compile(
    r"\b(was|were|went|bounced|dropped|rejected|accepted|routed|prevented|aborted|"
    r"unreachable|didn't|did not)\b",
    re.IGNORECASE,
)


def filter_misapplied_tense_suggestions(inline: list[dict]) -> list[dict]:
    """Drop present-tense rewrites that misapply the style guide."""
    kept: list[dict] = []
    for item in inline:
        message = item.get("message", "")
        if not _TENSE_NAG_MSG.search(message):
            kept.append(item)
            continue

        path = item["path"]
        file_path = REPO_ROOT / path
        if not file_path.exists():
            kept.append(item)
            continue

        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
        line_num = item["line"]
        if line_num < 1 or line_num > len(lines):
            kept.append(item)
            continue

        current = lines[line_num - 1]
        suggested = item["suggested_line"].rstrip()
        current_cell = _table_row_first_cell(current) or current
        suggested_cell = _table_row_first_cell(suggested) or suggested

        if _normalize_cause_label(current_cell) == _normalize_cause_label(suggested_cell):
            print(
                f"Skipping tense-only rewrite on `{path}` line {line_num} "
                "(cause label unchanged aside from tense)"
            )
            continue

        if current.strip().startswith("|") and _TROUBLESHOOTING_PAST_CAUSE.search(
            current_cell
        ):
            print(
                f"Skipping present-tense rewrite on `{path}` line {line_num} "
                "(troubleshooting past-event cause row)"
            )
            continue

        if re.search(r"\bmay(?: have)?\b", current, re.IGNORECASE) and not re.search(
            r"\bmay(?: have)?\b", suggested, re.IGNORECASE
        ):
            print(
                f"Skipping may/may-have removal on `{path}` line {line_num} "
                "(epistemic hedging is allowed)"
            )
            continue

        kept.append(item)
    return kept


_CURLY_QUOTE_CHARS = frozenset("\u2018\u2019\u201c\u201d")
_STRAIGHT_APOSTROPHE = "'"
_STRAIGHT_DOUBLE = '"'

# Maps change topics to review messages when the model's message does not match the diff.
_DERIVED_REVIEW_MESSAGES: dict[str, str] = {
    "ui_click_select": 'Replace "click" with "select" when describing UI menu or toolbar actions.',
    "ui_check_select": 'Use "select" instead of "check" when referring to checkboxes.',
    "ui_uncheck_clear": 'Use "clear" instead of "uncheck" when referring to checkboxes.',
    "straighten_apostrophe": "Use a straight apostrophe (`'`) instead of a curly apostrophe.",
    "straighten_quotes": 'Use straight quotation marks (`"`) instead of curly quotation marks.',
    "remove_will": 'Use present tense instead of "will" for the result of user action.',
    "remove_would": 'Avoid hypothetical "would" when describing product behavior.',
    "latin_eg": 'Replace "e.g." with "for example" or "such as".',
    "for_example_to_such_as": 'Use "such as" instead of "for example" before a short list.',
    "such_as_to_for_example": 'Use "for example" instead of "such as" before a short list.',
}


def _significant_line_changes(current: str, suggested: str) -> list[tuple[str, str]]:
    matcher = difflib.SequenceMatcher(None, current, suggested)
    changes: list[tuple[str, str]] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        old = current[i1:i2]
        new = suggested[j1:j2]
        if old or new:
            changes.append((old, new))
    return changes


def _analyze_line_change(current: str, suggested: str) -> set[str]:
    """Return change-topic tags derived from the diff between current and suggested lines."""
    topics: set[str] = set()
    for old, new in _significant_line_changes(current, suggested):
        if _STRAIGHT_APOSTROPHE in old and any(ch in new for ch in _CURLY_QUOTE_CHARS):
            topics.add("introduced_curly_apostrophe")
        if any(ch in old for ch in _CURLY_QUOTE_CHARS) and _STRAIGHT_APOSTROPHE in new:
            topics.add("straighten_apostrophe")
        if _STRAIGHT_DOUBLE in old and any(ch in new for ch in _CURLY_QUOTE_CHARS):
            topics.add("introduced_curly_quotes")
        if any(ch in old for ch in _CURLY_QUOTE_CHARS) and _STRAIGHT_DOUBLE in new:
            topics.add("straighten_quotes")
        if re.search(r"\bclick\b", old, re.IGNORECASE) and re.search(
            r"\bselect\b", new, re.IGNORECASE
        ):
            topics.add("ui_click_select")
        if re.search(r"\bcheck\b", old, re.IGNORECASE) and re.search(
            r"\bselect\b", new, re.IGNORECASE
        ):
            topics.add("ui_check_select")
        if re.search(r"\buncheck\b", old, re.IGNORECASE) and re.search(
            r"\bclear\b", new, re.IGNORECASE
        ):
            topics.add("ui_uncheck_clear")
        if re.search(r"\bwill\b", old, re.IGNORECASE) and not re.search(
            r"\bwill\b", new, re.IGNORECASE
        ):
            topics.add("remove_will")
        if re.search(r"\bwould\b", old, re.IGNORECASE) and not re.search(
            r"\bwould\b", new, re.IGNORECASE
        ):
            topics.add("remove_would")
        if re.search(r"\be\.g\.\b", old, re.IGNORECASE) and not re.search(
            r"\be\.g\.\b", new, re.IGNORECASE
        ):
            topics.add("latin_eg")
        if re.search(r"\bfor example\b", old, re.IGNORECASE) and re.search(
            r"\bsuch as\b", new, re.IGNORECASE
        ):
            topics.add("for_example_to_such_as")
        if re.search(r"\bsuch as\b", old, re.IGNORECASE) and re.search(
            r"\bfor example\b", new, re.IGNORECASE
        ):
            topics.add("such_as_to_for_example")
    return topics


def _message_claim_topics(message: str) -> set[str]:
    """Topics the review message claims to address."""
    claims: set[str] = set()
    lower = message.lower()
    if "click" in lower and ("select" in lower or "ui" in lower or "menu" in lower):
        claims.add("ui_click_select")
    if "check" in lower and "select" in lower:
        claims.add("ui_check_select")
    if "uncheck" in lower and "clear" in lower:
        claims.add("ui_uncheck_clear")
    if "curly" in lower and ("apostrophe" in lower or "quote" in lower):
        if "straight" in lower or "instead" in lower:
            claims.add("straighten_apostrophe")
            claims.add("straighten_quotes")
    if "present tense" in lower or "past tense" in lower or "will" in lower:
        claims.add("remove_will")
        claims.add("remove_would")
    if "e.g." in lower or "latin" in lower:
        claims.add("latin_eg")
    if "for example" in lower and "such as" in lower:
        claims.add("for_example_to_such_as")
    return claims


def _message_mentions_change_tokens(message: str, current: str, suggested: str) -> bool:
    """True when the message quotes or names a token that actually changes."""
    for old, new in _significant_line_changes(current, suggested):
        for token in (old.strip(), new.strip()):
            if len(token) < 3:
                continue
            if token in message or token.lower() in message.lower():
                return True
    return False


def _derive_review_message(topics: set[str]) -> str | None:
    for topic in (
        "ui_click_select",
        "ui_check_select",
        "ui_uncheck_clear",
        "straighten_apostrophe",
        "straighten_quotes",
        "remove_will",
        "remove_would",
        "latin_eg",
        "for_example_to_such_as",
        "such_as_to_for_example",
    ):
        if topic in topics:
            return _DERIVED_REVIEW_MESSAGES[topic]
    return None


def filter_curly_typography_suggestions(inline: list[dict]) -> list[dict]:
    """Skip suggestions that introduce curly quotes or apostrophes (style guide requires straight)."""
    kept: list[dict] = []
    for item in inline:
        path = item["path"]
        file_path = REPO_ROOT / path
        if not file_path.exists():
            kept.append(item)
            continue
        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
        line_num = item["line"]
        if line_num < 1 or line_num > len(lines):
            kept.append(item)
            continue
        current = lines[line_num - 1]
        suggested = item["suggested_line"].rstrip()
        topics = _analyze_line_change(current, suggested)
        if "introduced_curly_apostrophe" in topics or "introduced_curly_quotes" in topics:
            print(
                f"Skipping curly typography on `{path}` line {line_num} "
                "(Braze docs require straight quotes and apostrophes)"
            )
            continue
        kept.append(item)
    return kept


def align_review_messages(inline: list[dict]) -> list[dict]:
    """Ensure each comment message describes the actual suggested_line diff."""
    kept: list[dict] = []
    for item in inline:
        path = item["path"]
        file_path = REPO_ROOT / path
        if not file_path.exists():
            kept.append(item)
            continue
        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
        line_num = item["line"]
        if line_num < 1 or line_num > len(lines):
            kept.append(item)
            continue

        current = lines[line_num - 1]
        suggested = item["suggested_line"].rstrip()
        topics = _analyze_line_change(current, suggested)
        message = item["message"].strip()
        claims = _message_claim_topics(message)

        if not topics:
            print(
                f"Skipping suggestion on `{path}` line {line_num}: "
                "unable to classify line diff for review message"
            )
            continue

        claim_overlap = claims & topics
        mentions_tokens = _message_mentions_change_tokens(message, current, suggested)
        if claim_overlap or (mentions_tokens and not claims - topics):
            kept.append(item)
            continue

        if claims and not claim_overlap:
            derived = _derive_review_message(topics)
            if derived:
                print(
                    f"Rewrote mismatched review message on `{path}` line {line_num} "
                    f"(was: {message[:60]}…)"
                )
                kept.append({**item, "message": derived})
                continue
            print(
                f"Skipping mismatched review message on `{path}` line {line_num}: "
                f"message mentions {sorted(claims)} but diff changes {sorted(topics)}"
            )
            continue

        derived = _derive_review_message(topics)
        if derived:
            kept.append({**item, "message": derived})
            continue

        kept.append(item)
    return kept


def validate_inline(item: dict) -> dict | None:
    path = item.get("path")
    line = item.get("line")
    message = item.get("message")
    suggested = item.get("suggested_line")
    if not all(isinstance(x, str) and x for x in (path, message, suggested)):
        return None
    if not isinstance(line, int) or line < 1:
        try:
            line = int(line)
        except (TypeError, ValueError):
            return None
    p = REPO_ROOT / path
    if not p.exists():
        return None
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    if line > len(lines):
        return None

    current_line = lines[line - 1]
    if _is_non_commentable_markdown_line(current_line):
        print(
            f"Skipping suggestion on `{path}` line {line}: "
            "non-prose markdown (Liquid, kramdown attrs, or table separator)"
        )
        return None

    suggested_norm = suggested.rstrip()
    if current_line.rstrip() == suggested_norm:
        print(
            f"Skipping no-op suggestion on `{path}` line {line}: "
            "suggested_line matches current line"
        )
        return None

    if _is_wrong_table_row_anchor(lines, line, suggested_norm):
        print(
            f"Skipping mis-anchored table suggestion on `{path}` line {line}: "
            "suggested row matches the previous table row"
        )
        return None

    if "\n" in suggested_norm:
        if _block_exists_in_file(suggested_norm, lines):
            print(
                f"Skipping no-op multi-line suggestion on `{path}` line {line}: "
                "block already in file"
            )
        else:
            print(
                f"Skipping multi-line suggestion on `{path}` line {line} "
                "(inline suggestions must be single-line)"
            )
        return None

    window_start = max(0, line - 1 - NEARBY_LINE_WINDOW)
    window_end = min(len(lines), line - 1 + NEARBY_LINE_WINDOW + 1)
    for idx in range(window_start, window_end):
        if lines[idx].rstrip() == suggested_norm:
            print(
                f"Skipping no-op suggestion on `{path}` line {line}: "
                f"text already on line {idx + 1}"
            )
            return None

    return {
        "path": path,
        "line": line,
        "message": message.strip(),
        "suggested_line": suggested,
    }


# Non-breaking space is required between numbers and units (and in a few UI/table patterns).
_NUMBER_UNIT_NBSP = re.compile(
    r"\d(?:,\d{3})*(?:\.\d+)?&nbsp;"
    r"(?:KB|MB|GB|TB|KiB|K\b|px|pt|em|rem|ms|sec|seconds?|minutes?|hours?|days?|"
    r"kg|lb|lbs|oz|°[CF]?|deg)",
    re.IGNORECASE,
)
_ICON_UI_NBSP = re.compile(r"</i>&nbsp;\*\*")
_SCHEMA_TYPE_NBSP = re.compile(r"`[^`]*`&nbsp;`")


def _line_has_required_nbsp(line: str) -> bool:
    return bool(
        _NUMBER_UNIT_NBSP.search(line)
        or _ICON_UI_NBSP.search(line)
        or _SCHEMA_TYPE_NBSP.search(line)
    )


def filter_nbsp_removal_suggestions(inline: list[dict]) -> list[dict]:
    """Skip suggestions that remove required &nbsp; (number+unit, icon+UI, schema types)."""
    kept: list[dict] = []
    for item in inline:
        path = item["path"]
        file_path = REPO_ROOT / path
        if not file_path.exists():
            kept.append(item)
            continue
        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
        line_num = item["line"]
        if line_num > len(lines):
            kept.append(item)
            continue
        current = lines[line_num - 1]
        suggested = item["suggested_line"].rstrip()
        if "&nbsp;" not in current or "&nbsp;" in suggested:
            kept.append(item)
            continue
        if not _line_has_required_nbsp(current):
            kept.append(item)
            continue
        if suggested == current.replace("&nbsp;", " ").rstrip():
            print(
                f"Skipping nbsp removal on `{path}` line {line_num} "
                "(required non-breaking space per style guide)"
            )
            continue
        kept.append(item)
    return kept


_SUGGESTION_BLOCK = re.compile(r"```suggestion\n([\s\S]*?)\n```")


def _parse_suggestion_body(body: str) -> str | None:
    match = _SUGGESTION_BLOCK.search(body)
    return match.group(1).rstrip() if match else None


def fetch_prior_style_suggestions() -> dict[tuple[str, int], list[str]]:
    """Earlier inline suggestions from this bot on the same PR (includes outdated comments)."""
    owner, repo = REPO.split("/", 1)
    result = subprocess.run(
        ["gh", "api", f"repos/{owner}/{repo}/pulls/{PR_NUMBER}/comments", "--paginate"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        check=False,
    )
    if result.returncode != 0:
        print(f"Pull comment fetch warning: {result.stderr.strip()}", file=sys.stderr)
        return {}

    prior: dict[tuple[str, int], list[str]] = {}
    for comment in json.loads(result.stdout):
        body = comment.get("body") or ""
        if STYLE_REVIEW_INLINE_MARKER not in body:
            continue
        login = (comment.get("user") or {}).get("login", "")
        if not _is_bot_login(login):
            continue
        suggested = _parse_suggestion_body(body)
        path = comment.get("path") or ""
        line = comment.get("line") or comment.get("original_line")
        if not suggested or not path or not line:
            continue
        key = (path, int(line))
        prior.setdefault(key, []).append(suggested)
    return prior


def format_prior_suggestions_section(
    prior_suggestions: dict[tuple[str, int], list[str]],
) -> str:
    lines = [
        "## Prior automated inline suggestions on this PR",
        "",
        "Do not contradict these on the same line. Prefer consistency within the file "
        "over reversing a prior suggestion.",
        "",
    ]
    for (path, line), suggestions in sorted(prior_suggestions.items()):
        for suggested in suggestions:
            lines.append(f"- `{path}` line {line}: `{suggested}`")
    lines.append("")
    return "\n".join(lines)


def _inline_to_review_comment(item: dict) -> dict:
    return {
        "path": item["path"],
        "line": item["line"],
        "side": "RIGHT",
        "body": (
            f"**Docs style review** — {item['message']}\n\n"
            f"```suggestion\n{item['suggested_line']}\n```"
            f"{DISMISS_INSTRUCTION_FOOTER}"
        ),
    }


def filter_conflicting_prior_suggestions(
    inline: list[dict],
    prior_suggestions: dict[tuple[str, int], list[str]],
) -> list[dict]:
    """Skip case-only or wording reversals on lines we already commented on."""
    kept: list[dict] = []
    for item in inline:
        key = (item["path"], item["line"])
        priors = prior_suggestions.get(key, [])
        new = item["suggested_line"].rstrip()
        conflict = False
        for prior in priors:
            if prior == new:
                continue
            if prior.lower() == new.lower():
                conflict = True
                break
        if conflict:
            print(
                f"Skipping conflicting suggestion on `{item['path']}` line {item['line']} "
                "(case-only change from a prior automated suggestion on this PR)"
            )
            continue
        kept.append(item)
    return kept


def _post_single_review_comment(owner: str, repo: str, comment: dict) -> bool:
    payload = {
        "commit_id": HEAD_SHA,
        "path": comment["path"],
        "line": comment["line"],
        "side": comment["side"],
        "body": comment["body"],
    }
    result = subprocess.run(
        [
            "gh",
            "api",
            "--method",
            "POST",
            f"repos/{owner}/{repo}/pulls/{PR_NUMBER}/comments",
            "--input",
            "-",
        ],
        input=json.dumps(payload),
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stderr.strip(), file=sys.stderr)
    return result.returncode == 0


def post_pull_request_review(inline: list[dict], summary_notes: list[str]) -> tuple[int, list[dict]]:
    """Returns (posted_inline, fallback_comments)."""
    owner, repo = REPO.split("/", 1)
    review_comments = [_inline_to_review_comment(item) for item in inline[:MAX_INLINE]]
    fallback: list[dict] = []

    summary_lines = [
        "## Docs style review (automated)\n",
        f"Model: `{REVIEW_MODEL}` · Inline suggestions: **{len(review_comments)}**",
        "",
    ]
    if review_comments:
        summary_lines.append(
            "Open the **Files changed** tab and use **Commit suggestion** or "
            "**Commit all suggestions** on inline comments where offered."
        )
        summary_lines.append("")
    if summary_notes:
        summary_lines.append("### Additional notes")
        summary_lines.append("")
        for note in summary_notes:
            summary_lines.append(f"- {note}")
        summary_lines.append("")
    if not review_comments and not summary_notes:
        summary_lines.append(
            "**No issues or errors found** for the changed Markdown in this PR."
        )
        summary_lines.append("")

    review_body = "\n".join(summary_lines).strip()

    payload: dict = {
        "commit_id": HEAD_SHA,
        "event": "COMMENT",
        "body": review_body,
    }
    if review_comments:
        payload["comments"] = review_comments

    result = subprocess.run(
        [
            "gh",
            "api",
            "--method",
            "POST",
            f"repos/{owner}/{repo}/pulls/{PR_NUMBER}/reviews",
            "--input",
            "-",
        ],
        input=json.dumps(payload),
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Review API error: {result.stderr}", file=sys.stderr)
        # Fall back to posting comments one at a time
        posted = 0
        for c in review_comments:
            if _post_single_review_comment(owner, repo, c):
                posted += 1
            else:
                fallback.append(c)
                print(
                    f"Could not post inline for {c['path']}:{c['line']}",
                    file=sys.stderr,
                )
        return posted, fallback

    posted = len(review_comments)
    return posted, []


def _has_style_findings(
    posted: int,
    fallback: list[dict],
    summary_notes: list[str],
) -> bool:
    return posted > 0 or bool(fallback) or bool(summary_notes)


def _list_pr_comments_with_marker() -> list[dict]:
    owner, repo = REPO.split("/", 1)
    result = subprocess.run(
        [
            "gh",
            "api",
            f"repos/{owner}/{repo}/issues/{PR_NUMBER}/comments",
            "--paginate",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    comments = json.loads(result.stdout)
    return [c for c in comments if SUMMARY_MARKER in (c.get("body") or "")]


def _existing_summary_is_code_only_pass() -> bool:
    """True when the PR already has a no-prose (code/markup-only) pass summary."""
    marked = _list_pr_comments_with_marker()
    if not marked:
        return False
    body = marked[-1].get("body") or ""
    if CODE_ONLY_SKIP_MARKER in body:
        return True
    return "did not edit user-facing copy" in body and not _has_style_findings(0, [], [])


def _delete_issue_comment(comment_id: int) -> None:
    owner, repo = REPO.split("/", 1)
    subprocess.run(
        [
            "gh",
            "api",
            "--method",
            "DELETE",
            f"repos/{owner}/{repo}/issues/comments/{comment_id}",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def sync_summary_comment(
    posted: int,
    fallback: list[dict],
    summary_notes: list[str],
    files_reviewed: list[str],
    *,
    skip_reason: str | None = None,
) -> None:
    owner, repo = REPO.split("/", 1)
    lines = [
        SUMMARY_MARKER,
        "",
        "## Braze Docs style guide review (automated)",
        "",
    ]

    if not _has_style_findings(posted, fallback, summary_notes):
        lines.extend(
            [
                "**No issues or errors found.** This PR is OK to merge from the "
                "automated style guide review.",
                "",
            ]
        )
        if not files_reviewed:
            if skip_reason == "code_only":
                lines.extend(
                    [
                        CODE_ONLY_SKIP_MARKER,
                        "_Changed Markdown in this PR did not edit user-facing copy "
                        "(only inline code, fenced blocks, CSS, Liquid, HTML, or structural "
                        "markup), so no editorial review was run._",
                        "",
                    ]
                )
            elif _is_auto_translate_pr():
                lines.extend(
                    [
                        "_This PR only updates `_lang/` locale files from the auto-translate "
                        "workflow. Those files are skipped here because English canonical docs "
                        "are reviewed separately when they change._",
                        "",
                    ]
                )
            else:
                lines.extend(
                    [
                        "_No Markdown under `_docs/`, `_includes/`, or `_lang/` was changed in "
                        "this PR, so no editorial review was run. This comment confirms the "
                        "check completed successfully._",
                        "",
                    ]
                )
    else:
        lines.append(
            "The automated style guide review found items to address before merge."
        )
        lines.append("")

    short_sha = HEAD_SHA[:7] if HEAD_SHA else "unknown"
    lines.extend(
        [
            f"- **Files reviewed:** {len(files_reviewed)}",
            f"- **Inline suggestions posted:** {posted}",
            f"- **Model:** `{REVIEW_MODEL}`",
            f"- **Last run (commit):** `{short_sha}`",
            "",
        ]
    )

    if posted:
        lines.append(
            "Use **Commit suggestion** or **Commit all suggestions** in the "
            "**Files changed** tab where inline comments appear."
        )
        lines.append("")
        lines.append(
            "To dismiss a suggestion you disagree with, **Resolve conversation** on that "
            "thread or reply `reject` — the bot won't suggest it again on this PR."
        )
        lines.append("")
    if fallback:
        lines.append(
            f"**{len(fallback)}** suggestion(s) could not be posted inline "
            "(line may be outside the diff). Apply manually:"
        )
        lines.append("")
        for c in fallback:
            lines.append(f"- `{c['path']}:{c['line']}` — {c['body'].split(chr(10))[0]}")
        lines.append("")
    if summary_notes:
        lines.append("### PR-level notes")
        lines.append("")
        for note in summary_notes:
            lines.append(f"- {note}")
        lines.append("")

    lines.append(
        "_This check does not replace human review, CODEOWNERS approval, or other required PR checks._"
    )
    lines.append("")

    body = "\n".join(lines)

    # One summary comment per PR: replace content on every run (pass ↔ findings).
    marked = _list_pr_comments_with_marker()
    if len(marked) > 1:
        marked.sort(key=lambda c: c["id"])
        for duplicate in marked[:-1]:
            _delete_issue_comment(duplicate["id"])
            print(f"Removed duplicate summary comment {duplicate['id']}")

    if marked:
        target = marked[-1]
        subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "PATCH",
                f"repos/{owner}/{repo}/issues/comments/{target['id']}",
                "--input",
                "-",
            ],
            input=json.dumps({"body": body}),
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"Updated summary comment {target['id']} (replaced prior message for this run)")
    else:
        subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "POST",
                f"repos/{owner}/{repo}/issues/{PR_NUMBER}/comments",
                "--input",
                "-",
            ],
            input=json.dumps({"body": body}),
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        print("Created summary comment")

    SUMMARY_FILE.write_text(body, encoding="utf-8")


def main() -> None:
    if not PR_NUMBER or not HEAD_SHA:
        print("ERROR: PR_NUMBER and HEAD_SHA are required", file=sys.stderr)
        sys.exit(1)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY is required", file=sys.stderr)
        sys.exit(1)

    removed = cleanup_stale_style_review_comments()
    if removed:
        print(f"Cleaned up {removed} stale style review thread(s) from earlier commits.")

    prior_suggestions = fetch_prior_style_suggestions()
    if prior_suggestions:
        print(
            f"Found {sum(len(v) for v in prior_suggestions.values())} prior inline "
            "suggestion(s) on this PR."
        )

    dismissed_suggested, dismissed_message = fetch_dismissed_style_suggestions()
    if dismissed_suggested or dismissed_message:
        print(
            f"Honoring {len(dismissed_suggested) + len(dismissed_message)} dismissed "
            "style review item(s) on this PR."
        )

    files = get_changed_markdown_files()
    files, code_only_files = filter_files_with_prose_changes(files)
    if code_only_files:
        print(
            f"Skipped {len(code_only_files)} file(s) whose diffs change code/markup only "
            "(no user-facing copy edits)."
        )
    print(f"Reviewing {len(files)} Markdown file(s) in PR #{PR_NUMBER}")
    if not files:
        skip_reason = "code_only" if code_only_files else None
        if skip_reason == "code_only" and _existing_summary_is_code_only_pass():
            print(
                "No user-facing prose changes; existing code-only pass summary unchanged "
                "(no new comment)."
            )
            return
        sync_summary_comment(0, [], [], [], skip_reason=skip_reason)
        if code_only_files:
            print(
                "No user-facing prose changes in eligible Markdown; posted pass summary."
            )
        else:
            print(
                "No eligible Markdown under _docs/, _includes/, or _lang/ in this PR diff; "
                "posted summary (workflow-only PRs still trigger this check)."
            )
        return

    user_prompt = build_user_prompt(
        files,
        prior_suggestions,
        dismissed_suggested,
        dismissed_message,
    )
    if len(user_prompt) > 180_000:
        user_prompt = user_prompt[:180_000] + "\n\n…(prompt truncated)\n"

    print("Calling Claude for style review…")
    data = call_claude(user_prompt)

    inline_raw = data.get("inline") or []
    if not isinstance(inline_raw, list):
        inline_raw = []
    validated: list[dict] = []
    for item in inline_raw:
        if not isinstance(item, dict):
            continue
        v = validate_inline(item)
        if v:
            validated.append(v)

    validated = filter_nbsp_removal_suggestions(validated)
    validated = filter_misapplied_tense_suggestions(validated)
    validated = filter_curly_typography_suggestions(validated)
    validated = align_review_messages(validated)
    validated = filter_dismissed_suggestions(
        validated, dismissed_suggested, dismissed_message
    )
    validated = filter_duplicate_prior_suggestions(validated, prior_suggestions)
    validated = filter_conflicting_prior_suggestions(validated, prior_suggestions)
    postable, outside_diff = filter_to_diff_lines(validated)

    summary_notes = data.get("summary") or []
    if not isinstance(summary_notes, list):
        summary_notes = []
    summary_notes = [str(s).strip() for s in summary_notes if str(s).strip()]

    print(f"Model returned {len(validated)} valid inline suggestion(s)")
    has_findings = bool(validated) or bool(summary_notes)
    if has_findings:
        posted, fallback = post_pull_request_review(postable, summary_notes)
        fallback.extend(_inline_to_review_comment(item) for item in outside_diff)
        print(f"Posted {posted} inline suggestion(s) on the PR diff.")
    else:
        posted, fallback = 0, []
        print("No findings; skipping PR review (pass/fail only in summary comment).")

    sync_summary_comment(posted, fallback, summary_notes, files)
    print("Summary comment updated for this commit.")


if __name__ == "__main__":
    main()
