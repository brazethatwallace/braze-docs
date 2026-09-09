---
name: release-notes-community-post
description: >
  Turns a Braze release notes page into a succinct, ready-to-paste Braze Community
  post that highlights the highest-value updates and links back to the full notes.
  Reads the latest release from _docs/_releases/ by default. Use when drafting a
  Community announcement from release notes, generating a release highlights post,
  or when the user invokes /release-notes-community-post.
allowed-tools: Read, WebFetch
---

# Braze Release Notes → Community Post

Turns a Braze release notes page into a succinct, ready-to-paste Braze Community post that highlights the highest-value updates and links back to the full notes.

**Output:** Post the finished Community copy **directly in chat** — no file writes, no meta-commentary, no "Here's your post" wrapper.

## When to use this

You have a Braze release notes URL (e.g. `https://www.braze.com/docs/releases/2026/8_20_26`) — or want the **latest** release — and need a Community post that announces the release and teases a few highlights, not a full recap of everything in it.

## Resolve the release notes source

**Default (no URL given):** Use the latest release in this repo.

1. Read [`_docs/_releases/home.md`](../../../_docs/_releases/home.md). The first `{% details %}` block is the newest release; note its date label (for example `August 20, 2026`).
2. Confirm the canonical file path from the current year's landing page — for example [`_docs/_releases/2026.md`](../../../_docs/_releases/2026.md) — by taking the **last** entry in `guide_menu_list` and mapping its `link` to a file under `_docs/_releases/` (for example `/docs/releases/2026/8_20_26/` → `_docs/_releases/2026/8_20_26.md`).
3. Read that `.md` file. This is the authoritative source; prefer it over `home.md` when both exist.

**User supplies a URL:** Map `https://www.braze.com/docs/releases/YYYY/M_D_YY` to `_docs/_releases/YYYY/M_D_YY.md` and read that file. If the file is missing locally, fetch the public URL.

**Public link for the post:** `https://www.braze.com/docs/releases/YYYY/M_D_YY` (no trailing slash required).

## Steps

1. **Read the release notes page.** Pull every item, grouped by the page's own category headers (`##` sections), including each item's status tag (General Availability, Beta, Early Access, New) and description. Status tags appear in `{% multi_lang_include release_type.md release="..." %}` includes — read the `release=` value. Note the release date from the page title or URL.

2. **Select the high-value items.** Do not summarize everything — the page usually has 15-25 items across many categories, and the post should not. Pick roughly **4-6 items**, weighing:
   - *Reach*: does this affect a broad swath of customers/use cases, or a narrow edge case?
   - *Status*: General Availability items are usually safer bets than Early Access/Beta, since more readers can actually use them today — but a high-impact Early Access or Beta feature can still make the cut if it's a big unlock.
   - *Breaking changes / deprecations*: if the release includes SDK breaking changes, renamed events, or deprecations, always flag at least a brief mention — customers need to know even if it's not "exciting."
   - *New partner integrations*: new AI model providers, DAM/creative tools, or major channel additions are usually worth a line.
   - Skip minor UI polish, small bug fixes, and internal-only or admin-only tweaks unless the audience is specifically admins.

3. **Write the post** in this shape:
   - **Title**: something like "Braze Release Notes — [Month Day, Year]" (no emoji unless your Community's style uses them).
   - **One-sentence intro**: that new release notes are live, in plain friendly language (not "per the documentation...").
   - **Highlights**: one bolded feature name per line followed by a 1-2 sentence plain-language summary of *what it does and why it matters* — written for a Community reader (marketer/developer), not copy-pasted doc jargon. Include the status tag in parentheses if it's Beta or Early Access, since that changes availability.
   - **Breaking-change callout** (only if applicable): a short separate line flagging SDK/breaking changes so developers don't miss them, even if none made the main highlight list.
   - **Closing line + link**: invite readers to check out the full release notes, with the original URL.
   - Keep the whole post under ~200 words. Use light formatting only (bold feature names, simple line breaks) — assume the Community editor supports basic markdown, not rich HTML.

4. **Output the post as final, ready-to-paste text** — no meta-commentary about how the items were chosen, no headers like "Here's your post," just the post itself.

## Notes

- If a release has essentially no high-value items (a very light patch release), say so plainly rather than forcing 4-6 picks — a shorter post is better than padding.
- If given multiple release notes URLs, treat each as a separate post unless a combined one is requested.
- Default to plain Markdown with bold and line breaks for the post output, which works in almost any Community editor.
