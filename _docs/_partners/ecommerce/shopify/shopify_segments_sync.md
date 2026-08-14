---
nav_title: Shopify segments sync
article_title: Shopify segments sync
alias: /shopify_segments_sync/
page_order: 8
description: "This reference article explains how to sync Shopify segments into Braze as cohorts for unified audience management and targeting."
---

# Shopify segments sync

> The Shopify segments sync extends your Shopify store into Braze, giving your marketing team direct access to richer user data that lives in Shopify, including signals that aren't captured by the standard Braze Shopify integration. By syncing Shopify segments as cohorts, you align audience definitions across both platforms and deliver consistent, coordinated user experiences whether you target them in Shopify or reach them through a Braze campaign.

{% alert important %}
The Shopify segments sync is currently in beta. To request access, contact your customer success manager.
{% endalert %}

## Prerequisites

| Requirement | Description |
| --- | --- |
| Braze Shopify integration | The Braze Shopify app must be installed on your Shopify store and connected to a Braze workspace. For setup instructions, see [Shopify Standard Integration Setup]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) or [Shopify Custom Integration Setup]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/). |
| Shopify user permission | The Shopify user initiating the segment sync must have the **Export** permission to export user data. For more information on Shopify permissions, see [Shopify's store permissions documentation](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## How it works

The Shopify segments sync works in two phases.

1. **Initial backfill:** When you first sync a segment, Braze backfills all current members and creates a corresponding cohort in Braze. The backfill runs asynchronously and may take a few moments to complete.
2. **Ongoing sync:** After the initial backfill, Braze also subscribes to Shopify webhooks so membership stays synced in near real-time.

| Webhook topic | Effect in Braze |
| --- | --- |
| `customer.joined_segment` | The user is added to the corresponding Braze cohort. |
| `customer.left_segment` | The user is removed from the corresponding Braze cohort. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook topic" }

If a sync fails, the action extension modal displays an error banner explaining what happened and how to proceed. Some errors offer a **Retry sync** action. Others require an admin or configuration change.

## Data import integration

### Step 1: Select a Shopify segment to sync

In Shopify, go to **Customers** > **Segments**, and select the segment you want to sync to Braze. You can sync any segment built using Shopify's native segmentation, including segments based on order history, product purchases, customer tags, lifetime spend, and metafields.

![Segments panel with list of Shopify segments.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Step 2: Initiate the sync

1. On Shopify's segment detail page, open the **Use segment** dropdown and select **Braze Segment Sync**.

![Segment detail page with a "Use segment" dropdown that has a "Braze Segment Sync" option.]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. The Braze action extension modal opens, displaying the segment name and audience size. Select **Sync with Braze** to begin the import.

![Modal with a button to sync with Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. The modal transitions to a syncing state and shows a progress banner while Braze imports the members.

![Modal showing sync in progress.]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. Select **Close**. The sync continues in the background. Closing the modal doesn't stop it.

To check whether the sync has completed, close and reopen the modal. When the sync finishes, the modal opens with a success banner.

![Modal confirming sync is active.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Step 3: Create a Braze segment with the Cohort Membership filter

In Braze, go to **Audience** > **Segments**, and create a new segment. In **Add Filter**, select the **Cohort Membership** filter and select your synced Shopify segment from the dropdown. After saving, you can reference this Braze segment when targeting users in a campaign or Canvas.

![Segment builder with the "Shopify Cohorts" filter.]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Re-syncing a segment

After a segment is synced, you can refresh cohort membership at any time from the same action extension.

1. In Shopify, open the synced segment and select **Use segment** > **Braze Segment Sync**.
2. In the modal, select **Sync now**.
3. In the confirmation dialog, select **Sync now** to start the re-sync.

Re-syncing is additive: users who match the current Shopify segment are added to the cohort, but users who no longer match remain in the cohort.

## Segment updates in Shopify

### Renaming a segment

When you rename a Shopify segment, Braze updates the corresponding cohort's display name automatically. No re-sync is required.

### Changing segment criteria

Changes to a Shopify segment's criteria don't propagate automatically. To pick up users who newly match the criteria, re-sync the segment from the action extension. Users who no longer match remain in the cohort because re-sync doesn't remove members. For details, see [Re-syncing a segment](#re-syncing-a-segment).

## User matching

Users synced from Shopify segments are matched to Braze user profiles using the `shopify_customer_id` alias that is set as part of the Braze Shopify integration. Users without a matching Braze user profile are skipped during sync.

For details on how the Shopify integration identifies and aliases users, see [Shopify Data Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

Braze matches synced users against existing Braze user profiles regardless of how those profiles were created, including through the Shopify historical backfill, your own data platform (such as Snowflake or another data warehouse), or direct API imports. If your cohort is smaller than your Shopify segment, it means some segment members don't yet have a matching Braze profile. To increase match coverage, populate Braze user profiles through your preferred method before syncing.

## Limitations

- **One-way sync.** Segment membership flows from Shopify to Braze only. Changes to cohort membership made directly in Braze are not pushed back to Shopify.
- **No profile creation.** Only Shopify customers who already have a Braze user profile are added to the cohort.
- **No undoing syncs.** When a Shopify segment is synced, it cannot be undone.
- **Re-sync only adds members.** Re-syncing a segment adds newly matching users to the cohort but doesn't remove users who are no longer in the Shopify segment.
