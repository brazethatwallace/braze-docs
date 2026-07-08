---
name: spell-check
description: >
  Pre-PR spell-check gate for Braze Docs English markdown. Runs cspell on changed
  _docs/ and _includes/ files, auto-fixes only very high-confidence typos, and flags
  ambiguous unknown words for contributor review. Use when asked to "spell-check",
  "run cspell", or before opening a PR that touches documentation prose.
allowed-tools: Bash(git *), Bash(npm *), Bash(node_modules/.bin/cspell*), Read, Write, StrReplace, Grep
---

# Spell-check (cspell)

## Context

- Branch: !`git branch --show-current`
- Changed Markdown: !`git diff --name-only origin/develop...HEAD 2>/dev/null | grep -E '^(_docs|_includes)/.*\.md$' | grep -v '^_docs/_hidden/' || true`

## When to run

- Before opening a PR that changes English markdown under `_docs/` or `_includes/`
- When CI **Spellcheck** (`cspell.yml`) fails on a PR
- After drafting or revising documentation prose with an agent

`create-pr` invokes this skill as a **required pre-PR gate** when changed paths include `_docs/**` or root `_includes/**` markdown.

## Workflow

Load and follow [workflows/spell-check-changed-files.md](workflows/spell-check-changed-files.md).

## Config reference

| File | Role |
|------|------|
| [`cspell.json`](../../../cspell.json) | Ignore paths, regex skips (Liquid, URLs, code fences), dictionary wiring |
| [`config/cspell/braze-dictionary.txt`](../../../config/cspell/braze-dictionary.txt) | **Add accepted Braze/product terms here** (see file header) |
| [`.github/workflows/cspell.yml`](../../../.github/workflows/cspell.yml) | CI gate on PRs (changed Markdown only) |

Editorial glossary source of truth: [`docs/contributing/style_guide/writing_style_guide.md`](../../../docs/contributing/style_guide/writing_style_guide.md) (#glossary).

## Enforcement

| Layer | Behavior |
|-------|----------|
| **This skill** | Proactive local/agent check before PR; very high-confidence typo fixes only |
| **CI** (`cspell.yml`) | **Blocking** on PRs that change `_docs/` or `_includes/` markdown; posts or updates a PR comment on failure |

## Examples

**Typical invocation:** `/spell-check` on a branch with two changed `_docs/` articles → runs cspell on those files only, auto-fixes `recieve` → `receive`, asks about an unknown product token.

**CI failure recovery:** User pastes cspell log → skill re-runs on flagged files, fixes clear typos, presents dictionary vs prose decisions for remaining hits.

**Clean pass:**
> Spell-check complete — no issues found in the 3 changed Markdown file(s).
