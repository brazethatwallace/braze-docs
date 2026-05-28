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
from pathlib import Path

REPO = os.environ.get("GITHUB_REPOSITORY", "braze-inc/braze-docs")
PR_NUMBER = os.environ.get("PR_NUMBER", "")
HEAD_SHA = os.environ.get("HEAD_SHA", "")
BASE_REF = os.environ.get("GITHUB_BASE_REF", "develop")
REVIEW_MODEL = os.environ.get("REVIEW_MODEL", "claude-sonnet-4-20250514")
MAX_INLINE = int(os.environ.get("MAX_INLINE_COMMENTS", "25"))
MAX_FILES = int(os.environ.get("MAX_STYLE_REVIEW_FILES", "25"))
MAX_DIFF_CHARS = int(os.environ.get("MAX_STYLE_DIFF_CHARS", "12000"))

REPO_ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd()))
STYLE_REF = REPO_ROOT / ".github/skills/braze-docs/references/writing-style.md"
GLOSSARY_REF = REPO_ROOT / ".github/skills/braze-docs/references/glossary.md"
SUMMARY_MARKER = "<!-- braze-docs-style-review -->"
SUMMARY_FILE = REPO_ROOT / "docs_style_review_summary.md"

MARKDOWN_PREFIXES = ("_docs/", "_includes/", "_lang/")

SYSTEM_PROMPT = """\
You are a senior technical editor reviewing Braze documentation pull requests.
Apply the Braze Docs Style Guide provided in the user message.

## Review scope

- Editorial quality: voice, tone, clarity, active voice, second person, present tense.
- Style guide compliance: headings, UI formatting, links, lists, numbers, alerts, inclusive language.
- Braze terminology: Canvas, workspace (not app group), customers (not clients), allowlist/blocklist, etc.
- Do NOT flag product behavior you cannot verify from the diff alone.
- Do NOT invent facts or suggest content unrelated to the change.

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

- "line" is the 1-based line number on the RIGHT (new) side of the diff.
- "suggested_line" must be the complete line after your edit (not a fragment).
- Only include inline items when you are confident and the fix is a single-line change.
- Prefer high-signal issues; omit nitpicks and subjective preferences.
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


def get_changed_markdown_files() -> list[str]:
    base = f"origin/{BASE_REF}"
    result = _run(
        ["git", "diff", "--name-only", "--diff-filter=ACMRT", f"{base}...HEAD", "--", *MARKDOWN_PREFIXES],
        check=False,
    )
    if result.returncode != 0:
        print(f"git diff warning: {result.stderr.strip()}", file=sys.stderr)
        return []
    files = []
    for line in result.stdout.splitlines():
        path = line.strip()
        if not path.endswith(".md"):
            continue
        if path.startswith("_docs/_hidden/"):
            continue
        files.append(path)
    return files[:MAX_FILES]


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


def build_user_prompt(files: list[str]) -> str:
    sections = [load_style_context(), f"## Pull request #{PR_NUMBER}\n"]
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
    current = lines[line - 1]
    if current.rstrip() == suggested.rstrip():
        return None
    return {
        "path": path,
        "line": line,
        "message": message.strip(),
        "suggested_line": suggested,
    }


def post_pull_request_review(inline: list[dict], summary_notes: list[str]) -> tuple[int, int]:
    """Returns (posted_inline, fallback_count)."""
    owner, repo = REPO.split("/", 1)
    review_comments = []
    fallback = []

    for item in inline[:MAX_INLINE]:
        body = (
            f"**Docs style review** — {item['message']}\n\n"
            f"```suggestion\n{item['suggested_line']}\n```"
        )
        review_comments.append(
            {
                "path": item["path"],
                "line": item["line"],
                "side": "RIGHT",
                "body": body,
            }
        )

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
        summary_lines.append("No style guide issues flagged for the changed Markdown in this PR.")
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
            single = subprocess.run(
                [
                    "gh",
                    "api",
                    "--method",
                    "POST",
                    f"repos/{owner}/{repo}/pulls/{PR_NUMBER}/comments",
                    "-f",
                    f"commit_id={HEAD_SHA}",
                    "-f",
                    f"path={c['path']}",
                    "-f",
                    f"line={c['line']}",
                    "-f",
                    "side=RIGHT",
                    "-f",
                    f"body={c['body']}",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )
            if single.returncode == 0:
                posted += 1
            else:
                fallback.append(c)
                print(
                    f"Could not post inline for {c['path']}:{c['line']}: {single.stderr}",
                    file=sys.stderr,
                )
        return posted, len(fallback)

    posted = len(review_comments)
    return posted, 0


def sync_summary_comment(
    posted: int,
    fallback: list[dict],
    summary_notes: list[str],
    files_reviewed: list[str],
) -> None:
    owner, repo = REPO.split("/", 1)
    lines = [
        SUMMARY_MARKER,
        "",
        "## Docs style review (automated)",
        "",
        f"- **Files reviewed:** {len(files_reviewed)}",
        f"- **Inline suggestions posted:** {posted}",
        f"- **Model:** `{REVIEW_MODEL}`",
        "",
    ]
    if posted:
        lines.append(
            "Use **Commit suggestion** or **Commit all suggestions** in the "
            "**Files changed** tab where inline comments appear."
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
    if not posted and not summary_notes and not fallback:
        lines.append("No style guide issues flagged for changed Markdown in this PR.")
        lines.append("")

    body = "\n".join(lines)

    list_result = subprocess.run(
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
    comments = json.loads(list_result.stdout)
    existing = next((c for c in comments if SUMMARY_MARKER in (c.get("body") or "")), None)

    if existing:
        subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "PATCH",
                f"repos/{owner}/{repo}/issues/comments/{existing['id']}",
                "--input",
                "-",
            ],
            input=json.dumps({"body": body}),
            cwd=REPO_ROOT,
            check=True,
        )
        print(f"Updated summary comment {existing['id']}")
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

    files = get_changed_markdown_files()
    print(f"Reviewing {len(files)} Markdown file(s) in PR #{PR_NUMBER}")
    if not files:
        sync_summary_comment(0, [], [], [])
        print("No eligible Markdown changes; posted neutral summary.")
        return

    user_prompt = build_user_prompt(files)
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

    summary_notes = data.get("summary") or []
    if not isinstance(summary_notes, list):
        summary_notes = []
    summary_notes = [str(s).strip() for s in summary_notes if str(s).strip()]

    print(f"Model returned {len(validated)} valid inline suggestion(s)")
    posted, fallback = post_pull_request_review(validated, summary_notes)
    sync_summary_comment(posted, fallback, summary_notes, files)
    print(f"Done. Posted {posted} inline suggestion(s).")


if __name__ == "__main__":
    main()
