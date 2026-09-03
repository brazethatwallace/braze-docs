---
nav_title: Filter by date range
article_title: Filter catalog items by date range
page_order: 1
page_type: reference
description: "Use catalog selections with Liquid date expressions to surface catalog items within a rolling time window, such as events in the next seven days."
---

# Filter catalog items by date range

> This example shows how a fictional ticket marketplace uses catalog selections and Liquid date expressions to email consumers only events that are upcoming within the next seven days from send time. You create a selection with rolling time filters, then render the matching catalog items in a campaign or Canvas message.

## About this example

MovieCanon, a fictional ticket marketplace, uses this pattern to ensure email campaigns list only time-relevant concerts and shows.

The pattern uses two Braze features together:

- A [catalog selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) with `time` field filters whose values are Liquid snippets that compute a rolling time window at send time
- The {% raw %}`{% catalog_selection_items %}`{% endraw %} Liquid tag in the message body to render matching catalog rows

## Considerations

- Create a catalog `time` field for the datetime column you filter on, not a string field. Store values in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, such as `2026-06-20T19:30:00Z`. For supported types, see [Supported data types]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#supported-data-types).
- The `before` and `after` operators use strict comparisons. Events exactly equal to a bound timestamp may be excluded. Use full timestamps when you need the window to start at send time. Date-only `YYYY-MM-DD` values coerce to midnight UTC on that day.
- Liquid in selection filters is evaluated at send time. The `'now'` variable reflects when the message is rendered, typically in UTC. Confirm the resulting window matches your intent across time zones.
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/), catalog tags, and `abort_message` are not supported in catalog selection filter values. If a filter includes a disallowed tag, the selection returns no items without raising an error.
- You can add up to 10 filters per selection and return up to 50 items. Adjust the seven-day window by changing the seconds added to `'now'` (`604800` = 7 days multiplied by `86400` seconds per day).
- Catalog selection result arrays are zero-indexed (`items[0]` is the first item).
- Test filter Liquid, message Liquid, and abort logic outside your production workspace before sending to production audiences.

## Setup

This example assumes a catalog named `live_events` with these fields:

| Field | Type | Example value |
| ----- | ---- | ------------- |
| `id` | String | `show-1042` |
| `event_name` | String | `Summer Jazz Night` |
| `event_date_time` | Time | `2026-06-20T19:30:00Z` |
| `ticket_price` | Number | `45` |
| `city` | String | `Austin` |
| `venue` | String | `Riverside Amphitheater` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Catalog fields" }

If you don't have a similar catalog yet, [create a catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) and upload or sync your event data first.

### Step 1: Create the catalog selection

1. Go to **Data Settings** > **Catalogs** and select the `live_events` catalog.
2. Open the **Selection** tab and select **Create Selection**.
3. Name the selection `seven_day_window` and add an optional description, such as "Events occurring within the next seven days."
4. Set a **Results limit** for the maximum number of events to return (up to 50).
5. Don't save yet. Add the date filters in the next steps.

### Step 2: Add the upper-bound filter

Add a filter on the `event_date_time` field:

| Setting | Value |
| ------- | ----- |
| **Filter field** | `event_date_time` |
| **Operator** | `before` |
| **Value** | Liquid snippet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Upper-bound filter settings" }

In the filter value field, enter this Liquid snippet. It calculates a timestamp seven days from send time:

{% raw %}
```liquid
{% assign seven_days = 'now' | date: '%s' | plus: 604800 %}{{ seven_days | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

This sets the upper bound of the window so only events before that timestamp are included.

### Step 3: Add the lower-bound filter

Add a second filter on the same field:

| Setting | Value |
| ------- | ----- |
| **Filter field** | `event_date_time` |
| **Operator** | `after` |
| **Value** | Liquid snippet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lower-bound filter settings" }

Enter this Liquid snippet for the lower bound. It uses the current send time so events that have already started are excluded:

{% raw %}
```liquid
{{ 'now' | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Together, the two filters return catalog items where `event_date_time` is after the current send time and before seven days from send time. Select **Create Selection** to save.

### Step 4: Reference the selection in a message

In your campaign or Canvas message, insert Liquid that pulls items from the selection. You can use **Add personalization** (**Catalog Items** > **Use a selection**) or paste the tag manually:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
Here are some upcoming events:

{{ items[0].event_name }} — ${{ items[0].ticket_price }}
{{ items[0].city }} · {{ items[0].venue }}

{{ items[1].event_name }} — ${{ items[1].ticket_price }}
{{ items[1].city }} · {{ items[1].venue }}
```
{% endraw %}

Replace hard-coded array indexes with a loop if you need to render a variable number of results.

### Step 5: Handle empty results

When no catalog items match the selection, the `items` array is empty and the tagged block renders nothing. To skip the send or show fallback copy, wrap the tag in a conditional:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
{% if items.size == 0 %}
{% abort_message('Catalog selection returned 0 items') %}
{% endif %}

Here are some upcoming events:
{{ items[0].event_name }}
```
{% endraw %}

For more information, see [Aborting messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/).

## Related articles

- [Create a catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)
- [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)
- [Using catalogs in campaigns]({{site.baseurl}}/user_guide/data/activation/catalogs/use/)
- [Liquid `date` filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#date-filter)
- [Liquid use case library]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/)
