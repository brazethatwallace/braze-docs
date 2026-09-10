---
date_published: "2026-09-08"
nav_title: GrowSurf
article_title: GrowSurf
description: "This reference article outlines the partnership between Braze and GrowSurf, a referral and affiliate program platform that syncs participant data to Braze for segmentation and Liquid personalization."
alias: /partners/growsurf/
page_type: partner
search_tag: Partner
---

# GrowSurf

> [GrowSurf](https://www.growsurf.com/) sends referral program and affiliate program participant data to Braze user profiles. The integration adds referral links, participant details, referral counts, invite counts, impression counts, and milestone progress as custom attributes you can use for Braze segmentation and Liquid personalization.

_This integration is maintained by GrowSurf._

## About the integration

GrowSurf is referral and affiliate program software. The one-way integration keeps GrowSurf participant referral data available in Braze so you can segment participants, personalize messages with referral links and progress, and send timely program communications from Braze.

## Use cases

- Add each participant's referral link to Braze messages.
- Build segments from referral status, referral counts, and milestone progress.
- Personalize campaigns and Canvases with participant and referrer attributes.

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A GrowSurf account | A GrowSurf paid plan is required for this integration. |
| A Braze REST API key | A Braze REST API key with `users.track` permissions. Create this key in the Braze dashboard from **Settings** > **APIs and Identifiers** > **API Keys**. For more information, see [Creating REST API keys]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| A Braze REST endpoint | Your Braze REST endpoint URL (for example, `https://rest.iad-01.braze.com`). For more information, see [REST API endpoints]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

Follow these steps to connect a GrowSurf program to Braze. For step-by-step instructions, see the [GrowSurf Braze integration documentation](https://docs.growsurf.com/integrations/braze).

### Step 1: Create a Braze REST API key

1. In Braze, go to **Settings** > **APIs and Identifiers** > **API Keys**.
2. Create a REST API key with `users.track` permissions.
3. Copy the API key and note the REST endpoint for the same Braze workspace.

### Step 2: Connect Braze in GrowSurf

1. In GrowSurf, go to **Program Editor** > **4. Options** > **Integrations** > **Braze**.
2. Select the matching Braze REST endpoint.
3. Enter the REST API key and select **Submit**.

### Step 3: Verify the first participant sync

1. Add or update a test participant in GrowSurf.
2. In Braze, go to **Audience** > **User Search** and search by email to open the matching user profile.
3. Confirm the `grsf_` custom attributes appear on the profile.

## GrowSurf attributes in Braze

GrowSurf makes 15 referral attributes available in Braze. The first sync sends the full set. After that, GrowSurf sends updates when participant data changes. If a value is removed in GrowSurf, the corresponding Braze attribute is also cleared. Count values are sent as numbers.

### String attributes

| Custom attribute | Description |
| --- | --- |
| `grsf_share_url` | The participant's referral share URL. |
| `grsf_participant_id` | The participant's GrowSurf ID. |
| `grsf_referral_status` | The participant's referral status. |
| `grsf_participant_first_name` | The participant's first name. |
| `grsf_participant_last_name` | The participant's last name. |
| `grsf_referrer_first_name` | The referrer's first name. |
| `grsf_referrer_last_name` | The referrer's last name. |
| `grsf_referrer_email` | The referrer's email address. |
| `grsf_next_milestone` | The next milestone the participant is working toward. |
| `grsf_next_monthly_milestone` | The next monthly milestone the participant is working toward. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="String attributes" }

### Number attributes

| Custom attribute | Description |
| --- | --- |
| `grsf_total_referral_count` | The participant's total referral count. |
| `grsf_monthly_referral_count` | The participant's referral count for the current month. |
| `grsf_prev_monthly_referral_count` | The participant's referral count for the previous month. |
| `grsf_total_invite_count` | The participant's total invite count. |
| `grsf_total_impression_count` | The participant's total referral link impression count. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Number attributes" }

## Use GrowSurf with Braze

Use GrowSurf referral attributes for Braze segmentation and Liquid personalization. GrowSurf updates these attributes when a participant is added or their referral data changes. You can also sync participants who were already in your program.

### Step 1: Build segments

1. In Braze, create a segment with the relevant `grsf_` custom attributes.
2. Target or exclude participants by referral status, referral counts, or milestone progress.

### Step 2: Personalize messages

1. Add the `grsf_share_url` custom attribute to a Braze message with Liquid: {% raw %}`{{custom_attribute.${grsf_share_url}}}`{% endraw %}.

{: start="2"}
2. Use other `grsf_` attributes to personalize referral status, counts, and milestone progress.

## Considerations

- GrowSurf sends custom attributes only. It does not send custom events, purchases, or subscription changes.
- GrowSurf identifies Braze profiles by participant email. If no matching profile exists, Braze creates an email-only profile.
- If the same email belongs to participants in more than one connected GrowSurf program, the most recently synced program data appears on that Braze profile.
- Connect Braze before importing participants. To sync existing participants, use GrowSurf's existing-participant sync option.

## Troubleshooting

- Confirm the Braze REST API key has `users.track` permissions and the selected REST endpoint belongs to the same Braze workspace.
- If one participant fails to sync, verify that the participant has a valid email address.
- Check the participant's GrowSurf activity logs for the sync result.
- GrowSurf automatically retries temporary Braze errors. If GrowSurf cannot confirm an update, it sends all referral attributes the next time that Braze profile syncs. If the API key or REST endpoint is invalid, correct the settings and reconnect the integration.

For more troubleshooting details, see the [GrowSurf Braze integration documentation](https://docs.growsurf.com/integrations/braze#troubleshooting).
