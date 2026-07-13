---
name: docs-discrepancies
description: >
  Verifies Braze docs against platform source code, finds gaps and discrepancies, drafts updates, and opens PRs.
  Use when asked to verify docs against source, find docs gaps, cross-reference docs with product behavior,
  or run docs discrepancy workflows on _docs markdown files.
---

# Identify and update docs discrepancies against source code

Verify Braze docs against source code to identify discrepancies and propose docs updates.

## Context
- Current branch: !`git branch --show-current`
- Modified files: !`git diff --name-only origin/develop...HEAD 2>/dev/null || git diff --name-only $(git merge-base HEAD $(git rev-parse --verify origin/develop 2>/dev/null || git rev-parse --verify develop 2>/dev/null || echo HEAD~1))..HEAD 2>/dev/null`
- Open PR: !`gh pr view --json number,title,body 2>/dev/null || echo "none"`

---

## Step 1: Doc page verification

For the .md file in `_docs/*`:
1. **Extract Product Behavior** - Distill the page down to a set of product and platform behaviors that need to be verified.
2. **Verify Product Behavior** — **REQUIRED SUB-SKILL:** Use [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) and cross-reference with source code (main product at `../platform`). Do not rely on other documentation to verify. Always cross-reference with source code. If you can verify the resolution against the source code, add a reference to the source file(s). If you cannot verify the resolution, say that you could not verify the resolution against the source code.
3. **Identify Target** - Which existing doc page should be updated? (or flag as new page)
4. **Suggest Changes** - Which changes should be made to the existing doc?

### Output format per page to `output.md` and chat console

```markdown
### Docs Update:
- **Category**: [Docs Gap | Docs Discrepancy]
- **Product Behavior**: [One-sentence summary]
- **Verified behavior**: [Complete answer]
- **Target Doc**: `_docs/_user_guide/path/to/file.md` (or "NEW: suggested_location")
- **Suggested Change**: [What to add/update]
```
---

## Step 2: Draft Updates

For each docs page:

1. Read the target file to understand existing structure
2. Draft changes following conventions in the codebase based on the style guides in `docs/contributing/style_guide/*`
3. When documenting a product limitation or enhancement ask, use `_includes/product_feedback_cta.md` per [Product feedback CTAs](docs/contributing/style_guide/product_feedback_ctas.md). Do not add ad hoc `portal.braze.com` or legacy portal links.


## Step 3: Create a Properly Named Branch
For each file that is changed in `_docs`, create a Branch with the naming convention: `[DD]-Cursor-<pagename>-update-<ddmmyyyy>-`  
Example: `[DD]-Cursor-liquid_use_cases-02122026`  

---

## Step 4: Commit and Push Changes
Stage and commit all changes in `_docs` with a meaningful message derived from the summary, then push your branch to the remote repository (for example, `git push -u origin <branch-name>`).

---

## Step 5: Open the pull request

**REQUIRED SUB-SKILL:** Use [create-pr](../create-pr/SKILL.md) (`braze-docs:create-pr`) for Steps 0–1, 3–4, quality checklist, and anti-patterns. **Override Step 2 only** as follows.

### Step 2 override (docs-discrepancies)

| Field | Value |
|-------|--------|
| **Title** | `[DD] <short summary>` (example: `[DD] Add FAQ entry about machine opens vs other opens`) |
| **Label** | `docs discrepancy` — `gh pr edit --add-label "docs discrepancy"` after create |

**Body** — use the create-pr template and include:

```markdown
### Why are you making this change? (required)

<What readers will see differently after this correction.>

### Related PRs, issues, or features (optional)

- [BD-1234](https://jira.atl.braze.com/browse/BD-1234) (if applicable)

### Approach

<What was wrong in the doc, how source code was used to verify, and why this target page.>

### Changes

- [List scope for reviewers — no internal repo paths]
- If this was a docs discrepancy, note to tag the Eng owner in the description.
- If verified: **Verified against Braze source code.** — do **not** paste `platform/` or SDK paths.

### Verification

<Manual checks on affected pages — see create-pr.>

### Contributor checklist

<Copy from create-pr Step 2.>
```

## Step 6: Assign reviewers

Identify owners from [`.github/CODEOWNERS`](.github/CODEOWNERS). If no owner is found for the changed paths, assign `braze-inc/docs-team` via `gh pr edit --add-reviewer`.


## Source Code References

| Resource | Path |
|----------|------|
| Docs repo | (current repo) |
| Main product | `../platform` |


## Example prompts

Natural-language example requests:

```
Identify discrepancies for each .md file in `_docs/*`
```

```
Identify discrepancies for ai.md
```
