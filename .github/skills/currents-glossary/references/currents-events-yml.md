# `currents_events.yml` syntax

Per-event documentation for the generated Currents glossary pages lives in [`scripts/resources/currents_events.yml`](../../../../scripts/resources/currents_events.yml).

The file is a single top-level `event_documentation` map. Each key is a full dotted event type; each value is a map of documentation keys.

**Documentation standard: every event must have `api_tags`.** The generator does not enforce this — it renders an event fine without a tag block — but the docs standard requires `api_tags` on every event, so treat a missing one as a gap to fill. `description` is optional: when it is absent the generator falls back to the description EMS supplies, which is a valid state. The remaining keys (`alert_*`, `property_details`, `extra_details`) are optional and used only where the event needs them.

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

Indentation is two spaces per level: event types at two, keys at four, list items at six.

## Keys

| Key | Required | Type | Renders as |
|---|---|---|---|
| `description` | No | string | The opening paragraph, replacing the description EMS supplies |
| `api_tags` | **Yes** | list of strings | An `{% apitags %}` block, joined with `, ` |
| `alert_tip` | No | string | `{% alert tip %}` callout |
| `alert_note` | No | string | `{% alert note %}` callout |
| `alert_important` | No | string | `{% alert important %}` callout |
| `property_details` | No | list (see below) | A `### Property details` heading and bullet list |
| `extra_details` | No | block scalar | Markdown appended verbatim after Property details |

Order on the page is fixed by the generator and does not follow the order of keys in the YAML: tags, description, tip, note, important, schema tabs, property details, extra details.

There is no key for field names, data types, or per-field descriptions — those come from EMS. See [ems-actions.md](ems-actions.md).

## `description`

Replaces the EMS description entirely. Prefer adding this key over asking for an EMS change when the wording is a docs concern; the override is permanent.

```yaml
    description: This event occurs when a user makes a purchase. Use this data to track when users purchase something in the application.
```

Keep it to a sentence or two. Liquid and Markdown both work, though links here are unusual — `property_details` is the better home for anything with caveats.

## `api_tags`

**Required on every event.** Feeds the tag chips under the heading. Follow the conventions already in the file: a domain plus an action (`Canvas`, `Conversion`), a channel plus `Sends` for send events, or a concept noun for top-level `users.*` events.

```yaml
    api_tags:
      - Live Activity
      - Update Token
```

An event with no `api_tags` entry renders without a tag block — visibly inconsistent with its neighbors and a violation of the docs standard. A newly shipped event arrives in exactly this state, so adding tags is the first thing to fix.

## `alert_tip`, `alert_note`, `alert_important`

Each becomes one callout, placed above the schema tabs. Use at most one of each per event.

```yaml
    alert_tip: Purchases are special custom events and come with a JSON encoded string of custom event properties.
```

For a multi-paragraph callout, use a block scalar and separate paragraphs with `<br><br>` — a bare blank line inside a Liquid alert does not render reliably:

```yaml
    alert_note: |
      First paragraph.<br><br>

      Second paragraph.
```

Trailing whitespace is stripped, so a trailing blank line in the block is harmless.

## `property_details`

A list rendered under a `### Property details` heading. The heading appears only when this key is present.

**Flat bullets** — each string becomes one `-` bullet:

```yaml
    property_details:
      - For Custom Events, the payload will also be populated with any custom event properties.
      - "If you're using Kafka to ingest Currents data, contact your customer success manager."
```

**Nested bullets** — a list item that is itself a list becomes one parent bullet with indented children. The first element is the parent; the rest are children:

```yaml
    property_details:
      -
        - "The `push_token_provisionally_opted_in` field only applies to iOS push tokens."
        - "If you have Provisional Authorization set up, provisional tokens have this field set to `true`."
        - "All other push tokens are `false`."
      - A following flat bullet.
```

Only one level of nesting is supported. A third level renders as flattened text, not a deeper bullet — if you need more structure, move the content to `extra_details`.

**Quoting.** Quote any string that starts with a backtick, or that contains a colon followed by a space — both are YAML syntax. Double quotes are the convention in this file. Inside double quotes, escape any literal double quote as `\"`.

```yaml
      - "The `sdk_version` field only populates if the token state change is initiated by SDK."
      - "Three types are recorded in the `push_token_state_change_type` field: \"add\", \"update\", and \"remove\"."
```

Markdown and Liquid both work in bullets, including `{{site.baseurl}}` links:

```yaml
      - "Learn more in the [iOS guide]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/)."
```

## `extra_details`

For content too long or too structured for a bullet — event-type breakdowns, worked SQL examples, multi-section explanations. It is appended **verbatim** after Property details, so it is raw Markdown and you control the whole block.

Always use a literal block scalar (`|`). The `|` preserves your line breaks; a folded scalar (`>`) would join lines and break Markdown structure.

```yaml
    extra_details: |
      #### Event types

      ##### Add

      An "add" event is ingested when a new token is registered.

      {% alert note %}
      Older token registrations can have this field as `null` until the SDK reports permission status.
      {% endalert %}

      #### Querying for the latest active token state

      ```sql
      SELECT * FROM push_token_state_change
      ```
```

Rules specific to this key:

- **Indent the body six spaces**, two past the `extra_details:` key. YAML strips that common indent; anything indented further is preserved, which is how nested code fences and lists keep their shape.
- **Start headings at `####`.** The event heading is `##` and Property details is `###`, so `####` is the first level that nests correctly. Use `#####` for subsections.
- **Blank lines are fine** — unlike inside a Liquid alert, this is ordinary Markdown.
- **Liquid works**: `{% alert %}` blocks, `{{site.baseurl}}` links, and fenced code blocks including ```` ```sql ````.
- **In-page anchors work.** A `#### Add and remove pairs` heading can be linked as `(#add-and-remove-pairs)` from elsewhere in the same event's content.
- **Trailing whitespace is stripped**, so a trailing newline in the block is harmless.
- No colon-quoting worries — a block scalar takes the text as-is, so `:` and `#` need no escaping.

Only two events currently use `extra_details`. Read them before writing a new one:

- `users.behaviors.pushnotification.TokenStateChange`
- `users.behaviors.subscriptiongroup.StateChange`

## Adding an entry for a new event

New events arrive on the page through EMS at a release, rendering with the EMS description and no tags — the missing tags put them below the docs standard until you complete the entry. To document one:

1. Find the exact event type string as it appears in the generated page's heading anchor or in the changelog entry that introduced it.
2. Add the key under `event_documentation`, in the position that keeps the file readable — the file is grouped loosely by event family, not strictly sorted.
3. Add `api_tags` — it is required on every event and is the most visible gap on a new one.
4. Add `description` only to override the EMS text. Leaving it out keeps the two in sync automatically.
5. Add `alert_*`, `property_details`, or `extra_details` only where the event needs them.
6. Mirror the result into the generated page, following the emit order in [SKILL.md](../SKILL.md) Step 3.

The event type also determines which page it lands on, and that routing is in the generator, not here:

| Event type | Page |
|---|---|
| `users.profile.*`, `users.UserDeleteRequest`, `users.UserOrphan` | `user_profiles_events.md` |
| `users.behaviors.*` except `users.behaviors.subscription*` and `users.behaviors.Uninstall`; plus `users.RandomBucketNumberUpdate` | `customer_behavior_events.md` |
| Everything else, including `users.messages.*`, `users.behaviors.subscription*`, and `users.behaviors.Uninstall` | `message_engagement_events.md` |

An event whose only destination is `Platform` is internal and renders on no page at all.
