---
nav_title: Compare data ingestion options
article_title: Compare persistent and zero-copy data ingestion options
page_order: 1
page_type: reference
description: "Compare Cloud Data Ingestion standard syncs, CDI Segments, CDI Canvas triggers, and the /users/track API to choose how warehouse or application data reaches Braze profiles, segments, and Canvases."
---

# Compare persistent and zero-copy data ingestion options

> Choose how data from your warehouse or applications reaches Braze—whether it is copied onto user profiles, queried in place for segmentation, or passed transiently into a Canvas—before you design your ingestion pipelines.

## About this example

MovieCanon is a fictional movie streaming service. It centralizes customer, ticket, and viewing data in a warehouse. The data team must decide how to feed Braze for three common needs:

- **Profile data:** Loyalty tier, lifetime value, and genre or format preference attributes that persist on Braze user profiles.
- **Audience building:** SQL-driven segments from warehouse tables without copying every column into Braze.
- **Triggered messaging:** Warehouse rows that should enter a Canvas with row-specific personalization that does not need to live on the profile.

Braze offers four primary ingestion paths. Standard Cloud Data Ingestion (CDI) syncs and the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) API both persist data on profiles. CDI Segments (Connected Sources) and CDI Canvas triggers are zero-copy options: warehouse data stays in your warehouse and is not written to Braze user profiles.

Use this comparison when you are planning architecture, sizing throughput, or explaining trade-offs to engineering and marketing stakeholders. It does not replace integration setup guides for each option.

## Considerations

- Cloud Data Ingestion is an umbrella feature. Standard CDI syncs copy data onto Braze profiles (similar to `/users/track`). CDI Segments and CDI Canvas triggers keep warehouse data in place without writing it to Braze user profiles.
- CDI recurring syncs can run from every 15 minutes to once per month. If you need a higher cadence than 15 minutes, contact your customer success manager or use REST API ingestion. See [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/).
- CDI Canvas triggers share the [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) REST API rate limit with other traffic to that endpoint. `/users/track` has its own limits and batching rules. Default limits can be raised. Go to **Settings** > **APIs and Identifiers** > **API Limits**, and see [API rate limits]({{site.baseurl}}/api/api_limits/).
- Connected Sources and CDI Segment Extensions run queries in your warehouse. You incur warehouse compute cost; Braze does not log data points for those queries. See [Connected sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/).

## Setup

### Step 1: Map your use case to an ingestion path

Match your goal to the recommended ingestion path and whether that path writes to Braze profiles.

| Your goal | Recommended path | Profile writes? |
| --- | --- | --- |
| Persist attributes, events, purchases, or catalog items from the warehouse | Standard CDI sync | Yes (data is copied to Braze profiles or catalogs) |
| Build audiences from warehouse SQL without copying source tables into Braze | CDI Segments (Connected Sources) | No (membership only) |
| Enter users into a Canvas with warehouse row context that should not persist on the profile | CDI Canvas triggers | No (transient Canvas context properties) |
| Push data from apps, servers, or streaming pipelines in near-real time | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) (or SDKs) | Yes (data persists on profiles) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Map your use case to an ingestion path" }

### Step 2: Compare persistence, latency, and throughput

Compare how each path handles data residency, latency, throughput, and user creation.

| Dimension | Standard CDI sync | CDI Segments | CDI Canvas triggers | `/users/track` |
| --- | --- | --- | --- | --- |
| What it does | Scheduled read of a warehouse table; writes attributes, events, purchases, user deletes, or catalogs | Braze queries your warehouse for SQL Segment Extensions | Warehouse rows trigger Canvas entry with row context as Canvas context properties | Apps, servers, or streaming pipelines write attributes, events, and purchases to profiles |
| Data residency | Copied and persisted on Braze profiles | Stays in your warehouse; nothing written to profiles | Canvas context properties are transient; not persisted on profiles | Copied and persisted on Braze profiles |
| Typical latency | Not real-time; minimum 15-minute sync cadence (warehouse freshness also applies) | Not real-time; refreshes on your Segment Extension schedule (membership does not update on every warehouse change) | Not real-time; bounded by sync schedule (minimum 15 minutes) | Near-real-time (async processing) |
| Throughput notes | Full query result per sync; Braze batches internally to `/users/track`, `/users/delete`, or Catalog endpoints | Query runtime cap of 60 minutes per connected source; no per-request object cap | Shares `/canvas/trigger/send` rate limit; approximately 3.75 million Canvas entries per hour per sync run | Up to 75 combined objects per request; see [API rate limits]({{site.baseurl}}/api/api_limits/) |
| Batch size | No per-object cap on the CDI side for warehouse reads | N/A (query output defines membership) | One Canvas entry per warehouse row per sync run | 75 attributes, events, and purchases combined per request (default) |
| User creation | Yes, unless update-existing-only is set | No (unknown users in query results are ignored) | No (only existing Braze users) | Yes, unless `_update_existing_only` is true |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Compare persistence, latency, and throughput" }

### Step 3: Compare schema and identifier requirements

Compare required columns and supported identifiers for each path. Configure one data type per standard CDI sync (for example, attributes in one integration and events in another).

| Dimension | Standard CDI sync | CDI Segments | CDI Canvas triggers | `/users/track` |
| --- | --- | --- | --- | --- |
| Required columns / shape | User identifier + `UPDATED_AT` + `PAYLOAD` (JSON) per row | SQL must output `external_user_id` only | Identifier + `UPDATED_AT` + `PROPERTIES` (JSON; use `{}` when empty) | Standard `/users/track` request body |
| Supported identifiers | `external_id`, user alias, `braze_id`, email, or phone | `external_user_id` only (string) | `external_id` or user alias only | `external_id`, user alias, `braze_id`, email, or phone |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Compare schema and identifier requirements" }

### Step 4: Implement the path you selected

- **Standard CDI sync:** Create a warehouse table or view, then follow [Cloud Data Ingestion integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) and [Table setup]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup/).
- **CDI Segments:** Add a [Connected source]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/), then create a [CDI Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/).
- **CDI Canvas triggers:** Set up a source table with `PROPERTIES`, build and launch a destination Canvas, then create a sync per [Zero-copy personalization using CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/).
- **`/users/track`:** Send requests from your application or middleware. Format payloads per [POST: Create and update users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

For MovieCanon, a common pattern is: standard CDI syncs for nightly profile enrichment, CDI Segments for warehouse-only audience rules, Canvas triggers for ticket-status or viewing journeys with row-level context, and `/users/track` for real-time app events.

## Related articles

- [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)
- [Connected sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/)
- [Zero-copy personalization using CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/)
- [CDI Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/)
- [Table setup for Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup/)
- [POST: Create and update users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- [API rate limits]({{site.baseurl}}/api/api_limits/)
