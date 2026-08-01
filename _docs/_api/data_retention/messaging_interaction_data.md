---
nav_title: "Messaging Interaction Data"
article_title: "Messaging Interaction Data"
alias: "/messaging_interaction_data/"
page_order: 1
description: "This reference article covers campaign and Canvas interaction data and its availability."
page_type: reference
---

# About messaging interaction data availability

> Learn about messaging interaction data for campaigns and Canvases, including how long Braze keeps it and which features use it for retargeting.

## What is messaging interaction data?

Messaging interaction data refers to how a user interacts with a campaign or Canvas they received (for example, when a user opens campaign A or a user receives variant A). This data is used for retargeting.

## When is messaging interaction data available?

Interaction data is always available. For active campaigns and Canvases, interaction data is always available in real time. 

For stopped campaigns and Canvases, their interaction data expires after three months unless it's used in retargeting filters by active campaigns or Canvases. Expired interaction data is moved to long-term storage and is not available for use unless restored using the process described.

Expired interaction data is never deleted and can be restored at any time.

### Features that use interaction data

The following features use messaging interaction data:

- Retargeting filters that retarget on a specific campaign or Canvas
    - Clicked Alias in Campaign
    - Clicked Alias in Canvas Step
    - Clicked/Opened Campaign
    - Clicked/Opened Step
    - Converted From Campaign
    - Converted From Canvas
    - Entered Canvas Variation
    - In Campaign Control Group
    - In Canvas Control Group
    - Last Received Message from Specific Campaign
    - Last Received Message from Specific Canvas Step
    - Received Campaign Variant
    - Received Message from Campaign
    - Received Message from Canvas Step
- Retargeting filters that retarget on campaigns or Canvases of a certain tag
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- **Campaigns Received** and **Canvas Messages Received** lists on the user profile
- `/users/export` endpoint
- **User Data** CSV exports on campaign and Canvas summary pages

These features do not include expired interaction data in their results. To include expired interaction data in the results for these features, restore the campaign or Canvas with expired data. 

For example, Canvases can't be launched if the interaction data is expired, which means an edit like adding a team to the Canvas can't be saved.

### Features that don't use interaction data

The following features **do not** use messaging interaction data, meaning these features are unaffected by the expiration of messaging interaction data:

- Campaign and Canvas setup
- Campaign and Canvas analytics
- Analytics reports (such as Report Builder, Query Builder, and Engagement Reports)
- Currents
- Snowflake Data Share
- Segment Extensions
- Data points
- The following retargeting filters:
    - Clicked Alias in Any Campaign or Canvas Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from Campaign or Canvas Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email 
    - Last Received Push
    - Last Received SMS
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific SMS Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

## How do I restore messaging interaction data?

To restore your interaction data, follow these steps:

1. Go to the expired campaign or Canvas.
2. At the top of the campaign or Canvas landing page, select **Restore interaction data** in the banner.

You can also restore interaction data for multiple campaigns from the **Campaigns** page by selecting the campaigns, then selecting **Restore interaction data**.

The time for interaction data to restore can vary, but in most cases, this process can range from 5 to 15 minutes. After the restoration is complete, you will receive an email.

### Restoring by tag

You can also restore interaction data for expired campaigns or Canvases with a given tag.

1. Go to the **Campaigns** or **Canvas** page and search by the relevant tag.
2. Select your campaigns or Canvases.
3. Select **Restore interaction data** to restore the data for those campaigns or Canvases.

After another three months of inactivity, these campaigns or Canvases expire again.

### Retargeting by tag

Campaigns that use retargeting filters that are retargeting by tag are not exempt from expiration. Retargeting filters that are retargeting by tag include:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

## When was messaging interaction data available in the past?

Previously, message interaction data was deleted when a campaign or Canvas:

- Had not sent messages in 25 calendar months, AND
- Was not used for retargeting in any active campaigns, Canvases, or Content Cards.

Campaigns and Canvases with previously deleted messaging interaction data cannot be used in retargeting filters for campaigns, Canvases, and segments.

## Troubleshooting

### Why does a campaign or Canvas expiration date keep showing tomorrow?

If a stopped campaign or Canvas is still referenced by an active retargeting filter (for example, in an active segment, campaign, Canvas, or Content Card), Braze doesn't offload its interaction data yet.

In this case, the expiration date shown in the UI reflects the next scheduled cleanup run, so it can appear as "tomorrow" and continue moving forward while references still exist.

After you remove all active retargeting references, the interaction data is offloaded in the next cleanup cycle (typically the next day).

You might encounter the following error messages when trying to resume or unarchive campaigns, Canvases, or Content Cards with expired interaction data:

| Error message | When it appears | Troubleshooting |
| --- | --- | --- |
| "Can't resume Canvases because at least one Canvas is using filters or segments that have expired data. Remove these and try again." | When you try to resume one or more Canvases (bulk action) that use filters or segments with expired interaction data | [Restore interaction data](#how-do-i-restore-messaging-interaction-data) for the campaigns or Canvases referenced in the filters, or remove the affected filters from the Canvas |
| "Can't resume {name} because it is using filters or segments that have expired data. Remove these and try again." | When you try to resume a single Canvas that uses filters or segments with expired interaction data | [Restore interaction data](#how-do-i-restore-messaging-interaction-data) for the campaigns or Canvases referenced in the filters, or remove the affected filters from the Canvas |
| "Resume is only available for stopped Canvases with available interaction data" | When you try to resume a Canvas from the bulk action menu, but the Canvas has expired interaction data | [Restore interaction data](#how-do-i-restore-messaging-interaction-data) for the Canvas |
| "You can't resume these Campaigns. One or more Campaigns include expired filters." | When you try to resume one or more campaigns that use filters with expired interaction data | [Restore interaction data](#how-do-i-restore-messaging-interaction-data) for the campaigns or Canvases referenced in the filters, or remove the affected filters from the campaign |
| "You can't unarchive these Cards. One or more Cards include expired filters." | When you try to unarchive one or more Content Cards that use filters with expired interaction data | [Restore interaction data](#how-do-i-restore-messaging-interaction-data) for the campaigns or Canvases referenced in the filters, or remove the affected filters from the Card |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Common error messages" }