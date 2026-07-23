# EMS-owned content and how to get it changed

The Event Modeling Service (EMS) is the source of truth for the Currents event model. The generator reads it directly, so anything EMS owns cannot be durably fixed from braze-docs — an edit to the rendered page is overwritten at the next Currents release.

**EMS production UI:** <https://event-modeling-service.k8s.tools-001.d-use-1.braze.com/>

Access is internal and may require VPN. If the UI does not load, treat this whole page as background for writing a good handoff request rather than something you can act on.

## What EMS owns

| On the page | Owned by EMS |
|---|---|
| Everything inside the `{% tabs %}` JSON block | Field names, data types, array/optional status, per-field descriptions, sample values |
| Which destination tabs appear (Cloud Storage, Custom HTTP Connector, Snowflake Datashare / Datalake, Azure Blob Storage, and so on) | Per-destination schema configuration |
| The `## <Name> events` heading text and its anchor | The event's human-readable name |
| Every entry in `currents_changelogs.md` below the title | Generated from the EMS change history |
| An event's description **when `currents_events.yml` has no `description` key** | The event's documentation description |

That last row is the one exception worth remembering: a description is only EMS-owned by default. Adding a `description` key in `currents_events.yml` takes ownership of it permanently, and that is usually the faster fix. See [currents-events-yml.md](currents-events-yml.md).

Field descriptions have **no** braze-docs override. A wrong field description has to be fixed in EMS.

## Reading EMS

Useful before filing a request, to confirm what EMS actually says today and to name the exact field.

1. Open the production URL. The root page lists every event.
2. Narrow the list with **Search for an event name**, or the **Filter by Namespace**, **Filter by Owner**, and **Filter by Release Status** dropdowns. The list is paginated.
3. Click an event name to open its detail page. It shows **Event details** (name, owner, description) and two panels:
   - **Release Candidate (RC)** — the fields currently in production. This is what the docs generator will pick up at the next release.
   - **Pre-release Candidate (PRC)** — changes staged but not yet promoted. Content here is *not* in production and will not appear in docs until it is promoted and released.

If the field you are questioning appears only under PRC, the docs are not wrong — the change simply has not shipped yet.

## Requesting a change

File a ticket in the **DI** Jira project, or post in **#docs-currents-collab**. Include:

- The **event type** (the full dotted string, such as `users.behaviors.pushnotification.TokenStateChange`)
- The **destination tab** the problem appears on, if it is destination-specific
- The **field name**, exactly as it appears in the JSON
- **What it says now** and **what it should say**
- The docs page and section, so the requester can see the rendered context

A request naming the event type and field resolves far faster than one describing the symptom on the docs page, because EMS is not organized by docs page.

## What happens on the Currents side

Useful for setting expectations on timing, and to follow along if you have EMS access.

1. **Edit the event.** From the event detail page, **Edit event** opens the form. The description lives under **General details** as **Description for documentation**. Per-field text lives in the **Fields** section as **Field description** on each field row. A **Preview** panel shows the resulting Currents schema, Platform schema, and a sample event.

   Editing is blocked while a build, promotion, or discard is in progress — the UI says so explicitly.

2. **Promote.** Saving puts changes in the PRC panel and starts a build. Once the build completes, **Promote** moves the PRC changes to RC after a confirmation step. Until promotion succeeds, the change is not in production.

   Field edits are more constrained once a change reaches RC — fields can no longer be deleted there, though they can still be made optional and new ones added. A field *removal* is a breaking change to customer data pipelines and is not a documentation-level fix.

3. **Release.** The docs only change when the Currents team runs the generator as part of a Currents release, which regenerates all four pages against EMS. A description corrected in EMS today appears in braze-docs at the **next Currents release**, not immediately.

That lag is the reason for the dual-write pattern in [SKILL.md](../SKILL.md): for anything braze-docs *can* own, editing both the rendered page and `currents_events.yml` gets the fix in front of customers now and keeps it after the next regeneration.

## Interim wording while a request is open

If an EMS-owned error is actively misleading customers, do not edit the `{% tabs %}` JSON — the edit is guaranteed to be lost and reviewers cannot tell it is temporary. Instead, add a `property_details` bullet or an `alert_note` in `currents_events.yml` describing the correct behavior, with the matching edit to the rendered page. That is durable, survives regeneration, and can be removed once EMS is corrected.

## A caution on this page

The EMS UI is owned by the Currents team and changes without reference to braze-docs. Labels and flows described here can drift. The handoff path — a DI ticket or **#docs-currents-collab** — is the part that stays accurate.
