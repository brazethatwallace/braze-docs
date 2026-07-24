---
name: currents-glossary
description: >
  Update the generated Currents event glossary pages and the Currents changelog.
  These four pages are produced by an external generator that this repo cannot run,
  so every edit needs a matching change to its upstream source or the next release
  regeneration silently reverts it. Use when editing customer_behavior_events.md,
  message_engagement_events.md, user_profiles_events.md, or currents_changelogs.md;
  editing scripts/resources/currents_events.yml; adding property details, callouts,
  or API tags to a Currents event; or when a Currents event description, field, or
  schema looks wrong.
---

# Currents event glossary and changelog

Four pages under [`_docs/_user_guide/data/distribution/braze_currents/event_glossary/`](../../../_docs/_user_guide/data/distribution/braze_currents/event_glossary/) are **generated**, not hand-written:

- `customer_behavior_events.md`
- `message_engagement_events.md`
- `user_profiles_events.md`
- `currents_changelogs.md`

The generator lives outside this repo (in the Currents team's `data-infra-scripts`) and reads the Event Modeling Service (EMS) directly. **You cannot run it from braze-docs.** The Currents team runs it at each Currents release.

**This has one consequence that drives the whole skill:** an edit made only to a generated page looks correct until the next release, then disappears. An edit made only to the source doesn't appear until the next release. So most edits here are a **dual write** — change the rendered page *and* its upstream source in the same PR.

**Style, links, and Liquid conventions:** **REQUIRED SUB-SKILL:** [braze-docs](../braze-docs/SKILL.md).

## Context

- Branch: !`git branch --show-current`
- Generated pages changed: !`git diff --name-only HEAD -- _docs/_user_guide/data/distribution/braze_currents/event_glossary/ 2>/dev/null || true`
- Sources changed: !`git diff --name-only HEAD -- scripts/resources/currents_events.yml _includes/customer_behavior_glossary_template.md _includes/message_engagement_glossary_template.md _includes/user_profiles_glossary_template.md _includes/currents_changelogs_template.md 2>/dev/null || true`

---

## Step 1: Find who owns the thing you want to change

Every part of these pages is owned by exactly one layer. Find your change in this table before editing anything.

| What you want to change | Durable source | You can fix it in braze-docs |
|---|---|---|
| Intro prose, frontmatter, anything above the first `## … events` heading | `_includes/<page>_glossary_template.md` | **Yes** |
| An event's opening description paragraph | `currents_events.yml` → `description` | **Yes** |
| The API tag chips under a heading | `currents_events.yml` → `api_tags` | **Yes** |
| A tip / note / important callout below the description | `currents_events.yml` → `alert_tip`, `alert_note`, `alert_important` | **Yes** |
| The **Property details** bullet list | `currents_events.yml` → `property_details` | **Yes** |
| Long-form sections after Property details (event-type breakdowns, SQL examples) | `currents_events.yml` → `extra_details` | **Yes** |
| Field names, data types, optional/required, per-field descriptions — anything inside the `{% tabs %}` JSON | **EMS** | **No** — see [Step 4](#step-4-hand-off-what-braze-docs-cannot-own) |
| The `## <Name> events` heading text and its anchor | **EMS** event names | **No** |
| Which destinations get a tab | **EMS** | **No** |
| Changelog entries (everything below `# Currents changelog`) | **EMS** | **No** |
| Which of the three glossary pages an event lands on, and event ordering | Generator source | **No** |

**`api_tags` is required on every event** by the docs standard, and `currents_events.yml` is its only source — the generator renders an event fine without a tag block, so a missing one is a real gap to fill. Any event you touch should end up with `api_tags`; a brand-new event ships without it and needs it added.

The `description` row works differently: `currents_events.yml` **overrides** the description EMS supplies, but it is optional. If an event has no `description` key, the page shows the EMS text, which is a valid state — so a description fix is a docs-owned change either way, and adding the key is the fastest correct fix. The remaining keys (`alert_*`, `property_details`, `extra_details`) are optional too.

The `_lang/` copies of these pages are translations. Do not edit them; they re-sync from English.

## Step 2: Edit the upstream source

Full key-by-key syntax, including `property_details` nesting and the `extra_details` block scalar: **[references/currents-events-yml.md](references/currents-events-yml.md)**.

Quick orientation — `scripts/resources/currents_events.yml` is one top-level `event_documentation` map keyed by event type:

```yaml
event_documentation:
  users.behaviors.Purchase:
    description: This event occurs when a user makes a purchase.
    alert_tip: Purchases are special custom events.
    api_tags:
      - Purchases
    property_details:
      - For Purchase events, the payload also carries purchase properties.
```

For prose above the first event, edit the matching template instead:

| Page | Template |
|---|---|
| `customer_behavior_events.md` | `_includes/customer_behavior_glossary_template.md` |
| `message_engagement_events.md` | `_includes/message_engagement_glossary_template.md` |
| `user_profiles_events.md` | `_includes/user_profiles_glossary_template.md` |
| `currents_changelogs.md` | `_includes/currents_changelogs_template.md` |

These four templates hold the page's frontmatter and preamble. They are not referenced anywhere inside braze-docs, so tooling that hunts for unused includes will flag them — leave them alone.

## Step 3: Make the rendered page match, byte for byte

Apply the same change to the generated page. It has to match what the generator *would* emit, or the next release regeneration produces a confusing diff and a reviewer has to guess which side was intended.

Each event renders in this fixed order. Anything absent from the YAML is simply skipped — no blank placeholder is emitted:

```
{% api %}
## <Name> events {#<name>-events}

{% apitags %}
Tag One, Tag Two                      ← api_tags, comma-space joined
{% endapitags %}

<description>                          ← description, else the EMS text

{% alert tip %}                        ← alert_tip
…
{% endalert %}

{% alert note %}                       ← alert_note
…
{% endalert %}

{% alert important %}                  ← alert_important
…
{% endalert %}

{% tabs %}                             ← EMS schemas — never hand-edit
…
{% endtabs %}

### Property details

- first bullet                         ← property_details
  - nested bullet

<extra_details>                        ← extra_details, verbatim

{% endapi %}
```

Formatting rules the generator applies, worth copying exactly:

- The anchor is the heading name lowercased with spaces replaced by hyphens: `Session Start` → `{#session-start-events}`.
- `### Property details` appears **only** when `property_details` exists.
- Every block is separated by one blank line. `alert_*` and `extra_details` values are right-stripped, so no trailing blank line inside them.
- Events are ordered alphabetically by event type, and each event block is separated from the next by a blank line.
- The file ends with a single newline.

**Do not touch the `{% tabs %}` JSON.** It is regenerated wholesale from EMS every release, so an edit there is guaranteed to be lost and buys nothing in the meantime beyond a short-lived correction. If the schema is wrong, that is a Step 4 handoff.

## Step 4: Hand off what braze-docs cannot own

For the **No** rows in Step 1, the fix has to happen in EMS. What the docs team can do in braze-docs is limited and time-boxed:

- **A wrong or missing event description** — fix it in `currents_events.yml` with a `description` key. This is a real fix, not a stopgap; the override wins permanently.
- **A wrong field description, field name, type, or missing field** — braze-docs cannot hold this. Hand it off. Editing the rendered `{% tabs %}` block only masks the problem until the next release.

To hand off, file a ticket in the **DI** Jira project or post in **#docs-currents-collab** with the event type, the destination tab, the field, what's wrong, and what it should say.

What the Currents team does with it, and the EMS UI actions involved, are described in **[references/ems-actions.md](references/ems-actions.md)** — use that to write a specific request, or to follow along if you have EMS access yourself.

## Step 5: Verify before opening the PR

You cannot run the generator, so verification is by inspection:

1. **Both sides changed.** Every generated page in your diff has a matching source change, and vice versa. A one-sided diff is the mistake this skill exists to prevent — say so explicitly in the PR description if it's deliberate.
2. **The YAML parses and the key is on the right event.** Confirm your entry sits under the exact event type string (`users.behaviors.Purchase`, not `Purchase`) and is indented as a child of `event_documentation`.
3. **Every event you touched has `api_tags`.** It is required on all events. If you added or edited an event's entry — especially a newly shipped event — confirm the key is present; the generator won't flag its absence, but the docs standard requires it.
4. **The rendered edit is in the right slot** for the order shown in Step 3 — callouts above the schema tabs, property details below them.
5. **Liquid still balances** — every `{% alert %}`, `{% tabs %}`, `{% api %}` has its closing tag. A generated page that fails to build blocks the whole site.
6. **Preview the page locally** (`bundle exec jekyll serve`, or the repo's usual preview flow) and read the section you changed.

Then run the normal pre-PR gates: **REQUIRED SUB-SKILL:** [spell-check](../spell-check/SKILL.md), [check-accessibility](../check-accessibility/SKILL.md), and [create-pr](../create-pr/SKILL.md).

Call out the Currents coupling in the PR description and tag the Currents team — a reviewer who only sees the generated page cannot tell a durable edit from one that vanishes at the next release.

## Common mistakes

| Mistake | Consequence | Fix |
|---|---|---|
| Editing only the generated page | Reverted at the next Currents release, silently | Dual write — Step 2 and Step 3 |
| Editing only `currents_events.yml` | Correct, but invisible until the next release | Dual write |
| Editing the `{% tabs %}` JSON to fix a field | Always lost; the real problem never gets reported | Hand off (Step 4) |
| Adding a changelog entry by hand | Lost at the next release; the changelog body comes from EMS | Hand off (Step 4) |
| Rendered text not matching what the YAML would emit | Spurious diff at release; reviewer can't tell which side is right | Follow the emit order and formatting rules in Step 3 |
| Editing `_lang/` copies | Overwritten by translation sync | Edit English only |
| Deleting a `_includes/*_glossary_template.md` as unused | Breaks generation at the next release | Leave them; they are read from outside this repo |
| Putting an event entry under the wrong event type key | Silently renders nothing | Match the full dotted event type exactly |
