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

## Making changes

Docs changes should **only** change the "Field description" field--while other EMS properties are reflected in the generated docs, changing them would cause structural changes to delivered events too.

Field descriptions have a default for the field name and an optional per-event override; you can find the default doc at https://event-modeling-service.k8s.tools-001.d-use-1.braze.com/fields/${FIELD_NAME}. New overrides and modifications to them can be made through the UI; changes to the default must be made by the Currents team. Changes should be made at the correct level--don't use an override to correct a mistake in the default because then other events will pick up the old doc.
- If the field doc is already overridden, use the UI to update it.
- If the default doc is generally correct but some events need a different/more specific doc, use the UI to add overrides to those events.
- If the default doc is deficient in all cases (e.g. due to inaccuracies or spelling/grammatical errors), contact the Currents team to request a change.
- If the default doc is overly-specific and some events need a more general form (e.g. the default specifies a particular channel and the field has been added to events from other channels), as the Currents team to change the default to the more general form. Specify any events that should retain the more-specific form.

## Requesting a change

File a ticket in the **DI** Jira project, or post in **#docs-currents-collab**. Include:

- The **event type** (the full dotted string, such as `users.behaviors.pushnotification.TokenStateChange`)
- The **field name**, exactly as it appears in the JSON
- **What it says now** and **what it should say**
- The docs page and section, so the requester can see the rendered context

## A caution on this page

The EMS UI is owned by the Currents team and changes without reference to braze-docs. If the labels or flows mentioned here do not seem to correspond to the EMS UI, post in **#docs-currents-collab** so the Currents team can update this skill.