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
| [`.github/hooks/pre-commit`](../../../.github/hooks/pre-commit) | Local gate on staged Markdown (install via `scripts/install_hooks.sh`) |

Editorial glossary source of truth: [`docs/contributing/style_guide/writing_style_guide.md`](../../../docs/contributing/style_guide/writing_style_guide.md) (#glossary).

## Enforcement

| Layer | Behavior | Install |
|-------|----------|---------|
| **This skill** | Proactive local/agent check before PR; very high-confidence typo fixes only | `/spell-check` |
| **Pre-commit hook** (local) | Runs `cspell lint` on staged `_docs/` and `_includes/` markdown (same config as CI). Skips if `node_modules/.bin/cspell` is missing. | `bash scripts/install_hooks.sh` then `npm ci --ignore-scripts` |
| **CI** (`cspell.yml`) | **Blocking** on PRs that change `_docs/` or `_includes/` markdown; posts or updates a PR comment on failure | Enabled by default |

**Skip the local hook in an emergency:** `SKIP_SPELL=1 git commit`

### Local enforcement decision (BD-6700)

| Option | Editor UX | Maintainer cost | Parity with CI | Outcome |
|--------|-----------|-----------------|----------------|---------|
| **Pre-commit** (`cspell lint` in existing hook) | Catches issues at commit for everyone who installs hooks; no new toolchain | Low — extend `.github/hooks/pre-commit` | Exact same CLI + `cspell.json` / `braze-dictionary.txt` | **Adopted** |
| ESLint `@cspell/eslint-plugin` | Inline squiggles in the editor | High — braze-docs has no ESLint today | Different runner; easy to drift from CI flags | Not adopted |
| MegaLinter cspell descriptor | Unified multi-linter dashboard | High — heavy for a single check | Possible, but overkill unless bundling more linters | Not adopted |

CI remains the required PR gate. The pre-commit hook and this skill complement it; they do not replace it.

## Examples

**Typical invocation:** `/spell-check` on a branch with two changed `_docs/` articles → runs cspell on those files only, auto-fixes `recieve` → `receive`, asks about an unknown product token.

**CI failure recovery:** User pastes cspell log → skill re-runs on flagged files, fixes clear typos, presents dictionary vs prose decisions for remaining hits.

**Clean pass:**
> Spell-check complete — no issues found in the 3 changed Markdown file(s).
