# Style QA on changed prose (pre-PR gate)

Non-interactive self-check for agents finishing `_docs/` or root `_includes/`
markdown edits. Use this when `create-pr` Step 0 or feedback-handler requires
Style QA — not the full interactive `braze-docs` Review conversation.

## Load

1. [writing-style.md](../references/writing-style.md)
2. [glossary.md](../references/glossary.md)

Canonical human guide when a rule is ambiguous:
[`docs/contributing/style_guide/writing_style_guide.md`](../../../../docs/contributing/style_guide/writing_style_guide.md).

## Scope

1. Diff the branch against `develop` (or the PR base).
2. Review **only added and modified lines** in `_docs/**/*.md` and root
   `_includes/**/*.md`. Do not restyle unchanged prose.
3. Fix violations in those lines before opening or updating the PR.
4. Skip files that are code/markup-only with no editorial prose change.

## Checklist (changed lines only)

- [ ] **Bold = UI only** — Bold dashboard labels the reader interacts with.
      Remove bold used for emphasis, importance, or scanning.
- [ ] **Glossary casing** — Common product concepts stay lowercase mid-sentence
      unless matching a capitalized UI label: `campaign` / `campaigns`,
      `segment` (audience), `catalog`, `workspace`, `custom attributes`,
      `custom events`. Keep proper product names capitalized (`Canvas`,
      `Currents`, `Liquid`, `Content Blocks`).
- [ ] **Voice** — Active voice, present tense, second person; no "simple" /
      "simply" / "just" / "easy" in instructions; no banned glossary terms
      (`via`, `e.g.`, `i.e.`, `whitelist`, `app group`).
- [ ] **Headings** — Sentence case; no skipped heading levels in edited regions.
- [ ] **Links** — Descriptive link text; no "here" / "click here" / "Learn more"
      as the sole link text in new or edited links.
- [ ] **No drive-by restyles** — Do not "improve" nearby sentences that the
      change did not touch.

## Protected page

**Do not edit** `_docs/_hidden/other/support_contact.md` during Style QA or any
universal casing/style pass. That hidden Support Contact page is fragile;
drive-by or bulk edits can break it. Only touch it when the ticket or task is
explicitly about that page.

## Done when

Every checklist item passes on the prose diff, or remaining issues are called
out in the PR description for the human reviewer (with file and line).
