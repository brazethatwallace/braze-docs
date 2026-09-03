---
nav_title: DinMo
article_title: DinMo
description: "This reference article outlines the partnership between Braze and DinMo, a composable customer data platform that uses reverse ETL to sync warehouse data into Braze."
alias: /partners/dinmo/
page_type: partner
search_tag: Partner

---

# DinMo

> [DinMo](https://www.dinmo.com/) is a composable customer data platform (CDP) that connects your cloud data warehouse to Braze through reverse Extract, Transform, Load (ETL). Marketing teams can build audience segments from warehouse data, sync user attributes and events into Braze, and keep subscription statuses up to date without CSV uploads or engineering support.

_This integration is managed by DinMo._

The Braze and DinMo integration pushes segments and data models from your warehouse into Braze through the Braze REST API. When you connect a Braze destination in DinMo, activations send data from your models or segments to Braze.

## Prerequisites

| Requirement | Description |
| --- | --- |
| DinMo account | A [DinMo account](https://www.dinmo.com/) with permission to create destinations is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with the [permissions](#api-key-permissions) required for the destination services you plan to use. This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint depends on the [API endpoints]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) for your Braze instance. |
| Braze dashboard URL | Your Braze dashboard URL for your instance (for example, `https://dashboard.iad-01.braze.com`). For more information, see [Available SDK endpoints]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). |
| Data warehouse and data model | Before beginning the integration, connect your data warehouse in DinMo and define a model or segment for the data you want to sync to Braze. For more information, see [DinMo Braze integration guide](https://docs.dinmo.io/integrations/destination-platforms/braze). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Use cases

With this integration, you can:

* Sync user attributes from your warehouse into Braze to personalize campaigns and Canvases.
* Send custom events and purchase events from warehouse data into Braze for behavioral targeting.
* Keep Braze subscription group membership aligned with audience segments defined in DinMo.
* Export DinMo segments as Braze user attributes and build Braze segments from those attributes.

## API key permissions

Grant the following permissions on your Braze REST API key based on the destination services you use:

| Permission | Required for |
| --- | --- |
| `users.track` | Synchronizing user attributes, sending track events, and validating the destination connection |
| `users.export.ids` | Exporting user IDs for bulk operations |
| `users.alias.update` | Updating user aliases |
| `subscription.status.set` | Synchronizing subscription statuses |
| `users.delete` | Mirror sync mode only (optional for other destination services) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API key permissions" }

## Integration

### Step 1: Configure the Braze destination in DinMo

1. In DinMo, go to **Destinations** in the side navigation.
2. Select **Add a new destination** > **Connect a new platform** > **Braze**.
3. In the connection form, enter the following details:
   * **Platform Name**: For example, `Braze – Your Company`
   * **REST API URL**: Your instance REST endpoint (for example, `https://rest.eu-01.braze.com`)
   * **Dashboard URL**: Your instance dashboard URL (for example, `https://dashboard.eu-01.braze.com`)
   * **API Key**: The key you copied from Braze
4. Select **Connect** to validate your credentials.

{% alert note %}
You must specify both the REST API URL and the dashboard URL. Do not include a trailing slash on the REST API URL.
{% endalert %}

### Step 2: Verify the connection

After you save the destination, DinMo performs a test call (for example, `users.track`) to confirm that your API key and endpoint work.

If validation fails, confirm the following:

* The REST API URL is correct and has no trailing slash.
* The API key is valid and has the required permissions.
* If your Braze workspace uses an IP allowlist, DinMo's IP addresses are included.

## Supported destination services

Each destination service in DinMo follows the same general workflow: create a Braze destination, build a DinMo model or segment, then create an activation to send data to Braze. For step-by-step activation guidance, see [DinMo Braze destination services](https://docs.dinmo.io/integrations/destination-platforms/braze).

The following destination services are available:

| Destination service | Description |
| --- | --- |
| [Synchronize user attributes](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Update user profile attributes in Braze and optionally insert new users. |
| [Send track events](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | Send custom events and purchase events to Braze. |
| [Synchronize subscription statuses](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | Subscribe or unsubscribe users in a Braze subscription group based on DinMo segment membership. |
| [Export user lists](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | Sync segment membership to a Braze user attribute for use in Braze segmentation. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported destination services" }

### Synchronize user attributes

Use this destination service to update attributes on existing Braze user profiles and, optionally, insert new users.

When you run an activation:

* If you enable insert mode, new users in the model are created in Braze (UPSERT behavior).
* Changed attribute values since the last activation are updated in Braze.

If you do not enable insert mode, DinMo updates only users who already exist in Braze and have a matching external ID.

During activation setup, map the field in your DinMo model that corresponds to the user's [external ID]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) or Braze ID. Map each DinMo field to the exact attribute name in Braze. If an attribute does not exist in Braze, DinMo creates it.

The following sync modes are available for user attribute activations:

| Sync mode | Description |
| --- | --- |
| UPDATE | Updates changed records for users who already exist in Braze. Does not insert or delete records. |
| UPSERT | Inserts new records and updates changed records. Does not delete records. |
| MIRROR | Inserts, updates, and deletes records in Braze to mirror the source. Requires connector support for delete operations. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="User attribute sync modes" }

{% alert warning %}
Mirror sync mode permanently deletes records from Braze when they are no longer present in the DinMo source. Use mirror mode only when your warehouse is the single source of truth and deletions are intentional. Validate deletion rules before running mirror syncs in production.
{% endalert %}

### Send track events

Use this destination service to send custom events or purchase events from a DinMo event model or segment to Braze. DinMo treats custom events and purchases as separate destination services because Braze uses different APIs for each type.

Each record in the model represents a single event type (for example, `Purchase`). DinMo sends only new events on each activation run and does not update previously sent events.

During activation setup:

1. Specify the event name exactly as it should appear in Braze. If the event does not exist, DinMo creates it.
2. Map the required fields:
   * **Event time**: Timestamp when the event occurred
   * **External ID**: External ID of the user associated with the event
3. Map optional event properties to Braze attribute names.
4. Set the schedule for how often new events are sent to Braze.

### Synchronize subscription statuses

Use this destination service to keep a Braze subscription group aligned with a DinMo segment or model.

Before you activate this service:

1. Create the target subscription group (SMS or email) in Braze.
2. Build a DinMo model or segment containing the users who should belong to that subscription group.

During activation setup, enter the exact subscription group ID from Braze. To sync multiple subscription groups, create one activation per group.

When the activation runs:

* If users already exist in Braze, users who enter the DinMo segment are marked as subscribed to the target subscription group.
* Users who leave the DinMo segment are marked as unsubscribed from the subscription group.

DinMo does not modify users who were never part of the segment, and it does not create new Braze users in this destination service.

### Export user lists

Use this destination service to represent a DinMo segment as a Braze user attribute. Because of a Braze limitation, DinMo does not create a Braze list directly. Instead, it sets a user attribute to `true` for users in the segment and `false` for users who leave the segment.

During activation setup, specify the audience name. DinMo uses this name as the Braze attribute (spaces are replaced with underscores). Confirm that an attribute with the same name does not already exist in Braze. Map the DinMo field that corresponds to the user's external ID.

After the activation runs, create a Braze segment that filters users where the synced attribute equals `true`.

Only users with an external ID that matches an existing Braze user are updated. This destination service does not create new users.
