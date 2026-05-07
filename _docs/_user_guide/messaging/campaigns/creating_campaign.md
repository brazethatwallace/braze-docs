---
nav_title: Create a campaign
article_title: Create a campaign
page_order: 1
page_type: tutorial
description: "Learn how to create a Braze messaging campaign from compose through launch—including multichannel sends—and how to schedule delivery, target audiences, assign conversion events, send tests, and launch."
tool: Campaigns
---

# Create a campaign

> Use campaigns when you want to reach consumers with a single messaging step across one or more supported channels. For multi-step journeys, use [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/).

## Prerequisites

To create and launch a campaign, you need "Edit Campaigns" and "Launch Campaigns" permissions. For a full list of workspace permissions and how they appear in the dashboard, refer to [Permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).

### Before you begin

- Build or choose the [segments]({{site.baseurl}}/user_guide/audience/segments/) that define who should receive your messages.
- Review [Campaign basics]({{site.baseurl}}/user_guide/messaging/campaigns/campaign_basics/) so messaging channels, delivery types, and conversion goals align with your use case.
- For a guided walkthrough of delivery, targeting, and conversions, take the [Campaign Setup](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) Braze Learning course.

## Campaign composer

The campaign composer is where you define delivery, audiences, conversions, and launch settings. Decide whether you're creating a single-channel or multichannel campaign before you continue. 

{% tabs %}
{% tab Single channel %}

A single-channel campaign reaches users through one messaging channel per launch. 

### What's different

#### Control groups {#single-channel-control-groups}

Campaign control groups compare variants within your channel (for example, Email A versus Email B). Configure variants and holdouts with [A/B testing]({{site.baseurl}}/user_guide/messaging/ab_testing/). To orchestrate multiple channels or steps in one journey, use [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) instead.

#### Conversions and reporting {#single-channel-conversions}

For single-channel campaigns, Braze tracks [conversion events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) you assign to the campaign against sends from that channel. For attribution windows and counting rules, see [Conversion tracking rules]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#conversion-tracking-rules).

Workspace [frequency capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) and send limits still apply.

### Create a single-channel campaign {#create-a-single-channel-campaign}

To create a campaign:

1. Go to **Messaging** > **Campaigns**.
2. Select **Create campaign**.
3. Select the [channel]({{site.baseurl}}/user_guide/channels/) that fits your use case. 
4. On the [Compose step](#step-1-compose-messages), write and preview copy for that channel. 

Each campaign uses one channel type at a time. Add variants when you want to compare creative splits or run [A/B testing]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% endtab %}
{% tab Multichannel %}

A multichannel campaign reaches users through more than one messaging channel in a single launch. For example, send an email and push notification together.

{% alert note %}
[In-app messages]({{site.baseurl}}/user_guide/channels/in_app_messages/) aren't available in multichannel campaigns. Create a single-channel campaign or Canvas instead.
{% endalert %}

### What's different

#### Control groups {#multichannel-control-groups}

Campaign control groups compare variants within one channel (for example, Email A versus Email B). They aren't used to compare entire channels inside one multichannel campaign. To test channels, creative, or timing together across a journey, use [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/).

#### Conversions and reporting {#multichannel-conversions}

For multichannel campaigns, Braze tracks [conversion events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) per channel. When a user converts after receiving messages on more than one channel, Braze can attribute that conversion across those channels. Conversion counts may exceed *Unique Users*, and rates may exceed 100%. For full rules, see [Conversion tracking rules]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#conversion-tracking-rules).

Rate limits for sends that span channels are described in [Multichannel campaigns and Canvases]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases). For workspace-wide rules (including how multichannel sends count toward caps), refer to [Frequency capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).

### Create a multichannel campaign {#create-a-multichannel-campaign}

1. Go to **Messaging** > **Campaigns**.
2. Select **Create campaign**.
3. Select **Multichannel**.
4. On the [Compose step](#step-1-compose-messages), select **Add channel** and choose each channel you need. Select the channel icons to switch between composers while you write copy for each channel.

{% endtab %}
{% endtabs %}

## Step 1: Compose messages {#step-1-compose-messages}

### Campaign details

Use the following fields to record metadata that helps your team find and manage the campaign.

| Field | Purpose |
| --- | --- |
| Name | Use a clear name that reflects the campaign goal. |
| Description | Optional. Explain intent or links to briefs for collaborators. |
| Team | Optional. Assign [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) so the right groups can edit or report on this send. |
| Tags | Optional. Add [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) to filter in lists and tools such as [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder/). |
| Campaign ID | Where shown in the composer or summary, copy this identifier for API calls, reporting, and integrations that reference a specific campaign. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Channels and editors

Compose channel-specific content in this step. For detailed guidance, see [Channels]({{site.baseurl}}/user_guide/channels/) and open the article for the channel you selected. 

### Variants

Add variants when you want to compare creative or delivery splits. For background on experiments and controls, see [Multivariate and A/B testing]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
When each variant uses similar body content, compose the message **before** you add extra variants. Then use **Copy from Variant** from the **Add Variant** menu to reuse work across variants or channels.
{% endalert %}

## Step 2: Schedule delivery {#step-2-schedule-delivery}

Choose when users become eligible to receive the campaign:

| Delivery type | Summary |
| --- | --- |
| [Scheduled delivery]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery/) | Send at a specified time or cadence. |
| [Action-based delivery]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) | Send when users perform behaviors or meet conditions you define. |
| [API-triggered delivery]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) | Send when your systems call Braze to trigger the campaign for eligible users. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For scheduling concepts across Braze, see [Schedule your campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

### Delivery controls

Depending on delivery type, you can adjust **re-eligibility** (whether users may enter the campaign again) and respect workspace [frequency capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) rules. See [Re-eligibility]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) for campaign-level settings.

You may also configure [quiet hours]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#quiet-hours) so messages don't send during restricted windows.

## Step 3: Target audiences {#step-3-target-audiences}

On **Target Audiences**, define who is eligible to receive the campaign. For full targeting options, UI walkthroughs, and screenshots, see [Target users]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/).

### Segments and filters

Select saved segments, add **Additional filters** for a one-off audience, or combine both. Workspace [suppression lists]({{site.baseurl}}/user_guide/audience/suppression_lists/) automatically exclude listed users unless you allow an exception for this campaign.

### Audience summary

Review **Reachable users** and channel-level stats so you know who can actually receive this send. Reachable counts reflect your workspace data, channel setup, and filters. For very large audiences, Braze may show estimates until you calculate exact statistics.

### User Lookup

In **User Lookup**, search by **External User ID** or **Braze ID** to check whether someone matches your audience. You can't search by email address here.

### Channel-specific options

Channels that use subscriptions (email, SMS, and similar) include controls such as **Send to these users** so you only send to users with the subscription or opt-in states you want.

You can also set a **maximum send volume**, **delivery speed limits**, and [multivariate or A/B tests]({{site.baseurl}}/user_guide/messaging/ab_testing/) from this step.

## Step 4: Assign conversion events {#step-4-assign-conversion-events}

[Conversion events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) measure outcomes after a user receives your campaign (or enters the control group). Braze defaults to **Starts Session** within a short window (often three days). You can define conversion events that match your KPIs, up to four events per campaign.

{% alert important %}
You can't add or remove conversion events after the campaign launches. Confirm events before you launch.
{% endalert %}

## Step 5: Review summary and launch {#step-5-review-summary-and-launch}

The **Review Summary** step shows scheduling, audience, variants, and messaging choices.

Before you launch your campaign:

1. Confirm segments, variants, and delivery settings match your intent.
2. [Send test messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) to validate rendering and behavior on your test devices or internal recipients.

When you're ready, select **Launch Campaign**.

### Approvals

If your workspace uses approvals, a teammate with permission to approve campaigns must approve before launch. For more information, see [Approvals for campaigns and Canvases]({{site.baseurl}}/user_guide/messaging/governance/approvals/).

## Related articles

- [Design and edit]({{site.baseurl}}/user_guide/messaging/design_and_edit/)
- [A/B tests]({{site.baseurl}}/user_guide/messaging/ab_testing/)
- [Campaign analytics]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics/)