---
nav_title: Talkable
article_title: Talkable
description: "This reference article outlines the partnership between Braze and Talkable, a referral marketing platform that syncs marketing email opt-ins from referral campaigns to Braze in real time."
alias: /partners/talkable/
page_type: partner
search_tag: Partner
---

# Talkable

> [Talkable](https://www.talkable.com/) helps consumer brands turn happy customers into a scalable referral channel. With the Braze integration, marketing email opt-ins captured in Talkable referral campaigns flow into Braze in real time, giving your team the consent, context, and campaign data you need to welcome, segment, and engage every new advocate and friend.

_This integration is maintained by Talkable._

## About the integration

Talkable brings advocate-led acquisition into the customer journey that Braze powers. The integration moves every referral opt-in Talkable captures into the matching Braze profile in real time, so welcome flows, referral journeys, segmentation, and lifecycle messaging can launch from trusted consent and referral context—all without manual list exports or batch syncs.

Talkable captures marketing opt-ins in two scenarios:

* **Advocate sign-up:** An advocate signs up for a Talkable referral campaign and consents to receive marketing email.
* **Friend email gating:** A friend completes Talkable's email-gating step and opts in to marketing email.

In either case, Talkable creates or updates the matching Braze user profile in real time and sets the user's email subscription state to **Opted In**.

### Default behavior

Talkable sends data to Braze only on a discrete opt-in event from someone who has explicitly consented in Talkable—either an advocate signing up for a campaign or a friend opting in during email gating. Talkable does not run nightly batches, full syncs, or implicit profile updates. Talkable never sends profiles that have not opted in to Braze.

## Use cases

- Trigger a Braze welcome Canvas the moment an advocate signs up for a Talkable referral campaign.
- Activate referred friends with a friend-specific Canvas and a personalized first-purchase offer as soon as a friend opts in.
- Segment by referral context using advocate and friend flags and campaign metadata sent as Braze custom attributes.
- Route referral opt-ins into a designated Braze subscription group for compliance-friendly newsletter sending.

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A Talkable account | A Talkable site with at least one campaign configured is required to take advantage of this partnership. |
| A Braze REST API key | A Braze REST API key with `users.track` permissions. Create this key in the Braze dashboard from **Settings** > **API Keys**. For more information, see [Creating REST API keys]({{site.baseurl}}/api/basics/#creating-rest-api-keys). |
| A Braze REST endpoint | Your Braze REST endpoint URL (for example, `https://rest.iad-01.braze.com`). Both US (`.com`) and EU (`.eu`) Braze clusters are supported. For more information, see [REST API endpoints]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Install the Braze app in Talkable

1. Sign in to your Talkable admin and open the menu, then go to **All Site Settings** > **App Store**.
2. Locate **Braze** and select **Install**.
3. Enter your Braze REST endpoint and a REST API key with `users.track` permissions, then select **Save**.

### Step 2: Configure the email opt-in action

1. In the Talkable Braze app, open the **Email opt-in** action.
2. (Optional) Enter a Braze subscription group identifier, add custom attributes, and/or configure a user alias. For more information, see [Customizing Talkable](#customizing-talkable).
3. Select **Save**. Leave the action disabled so you can verify the configuration with a test payload before any live opt-in events start syncing.

### Step 3: Test with a sample payload

1. In Talkable, select **Send sample payload** on the **Email opt-in** action to send a test request to Braze.
2. In Braze, go to **Audience** > **User Search** and search by the test email address.
3. Confirm the profile exists with **Email Subscribe** set to **Opted In** and that any custom attributes, subscription group enrollment, or user alias you configured appear as expected.

### Step 4: Enable the action for live traffic

When the test profile looks correct in Braze, return to Talkable and enable the **Email opt-in** action.

From this point, every Talkable opt-in event syncs the matching profile to Braze in real time.

## Default user attributes sent to Braze

On every opt-in event, Talkable creates or updates the matching Braze user profile with the following standard Braze user attributes. Empty values are omitted.

| Braze attribute | Type | Notes |
| --- | --- | --- |
| `email_subscribe` | String | Set to **Opted In** on every Talkable opt-in event. |
| `email` | String | Primary identifier used to match the Braze profile. |
| `phone` | String | Captured as a user attribute only. Braze expects E.164 format; sent as stored in Talkable. |
| `first_name` | String | The person's first name. |
| `last_name` | String | The person's last name. |
| Subscription group enrollment | Not applicable | Added only when a subscription group is configured. The user is enrolled as subscribed. |
| User alias | Not applicable | Added only when a user alias is configured. For more information, see [Customizing Talkable](#customizing-talkable). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Default user attributes sent to Braze" }

## Customize Talkable

The following optional customizations are available. Configure any combination; they are independent.

### Enroll opt-ins in a Braze subscription group

1. In Braze, copy a subscription group ID from **Audience** > **Subscription Group Management**. For more information, see [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).
2. In the Talkable **Email opt-in** action, paste it into the **Subscription group identifier** field.

Talkable enrolls each opt-in in that subscription group as subscribed, scoping referral opt-ins to that group instead of a global subscription. Talkable only adds subscriptions; it never removes them.

### Send custom attributes

Add any key-value pair to the action's payload editor. The key you enter becomes the attribute name on the Braze user profile.

Values are Liquid-templated. The following variables are available:

{% raw %}
| Variable | Contents |
| --- | --- |
| `{{ person }}` | The advocate or friend who opted in (`email`, `first_name`, `last_name`, `phone_number`, `username`, `is_advocate`, `custom_properties`, and more). |
| `{{ ip }}` | The IP address from which the opt-in occurred. |
| `{{ campaign }}` | The originating Talkable campaign (`name`, `type`, `tag_names`, and more). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid template variables" }
{% endraw %}

{% raw %}
Example: add `talkable_is_advocate` = `{{ person.is_advocate }}` and `talkable_campaign_name` = `{{ campaign.name }}` to segment by referral context in Braze.
{% endraw %}

### Identify users with Braze user aliases

In the payload editor, add `user_alias.alias_name` (for example, {% raw %}`{{ person.username }}`{% endraw %}) and `user_alias.alias_label` (for example, `username`). For more information, see [User alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/).

When both fields are present, the system identifies the user by the alias in addition to email, and Braze creates a new aliased profile if no match exists.

{% alert note %}
Both alias fields are required. If only one of `alias_name` or `alias_label` is set, Talkable does not send a user alias and the profile is matched by email only.
{% endalert %}

## Find and create users in Braze

* By default, Braze matches the profile by email address. If no matching profile exists, Braze creates a new one.
* When a user alias is configured, Braze matches on that alias as well and creates a new aliased profile if no match exists.
* External IDs are not used by this integration. To attach Talkable opt-ins to an existing externally identified profile, configure a user alias whose label matches that profile's known alias.

## Use Talkable with Braze

### Find a synced user

Go to **Audience** > **User Search** and search by email to view a profile Talkable created or updated.

Standard fields (email, phone, first name, or last name) and any custom attributes you configured appear on the profile; **Email Subscribe** shows **Opted In**.

### Build a referral segment

1. Create a segment filtered on **Email Subscribe** is **Opted In**.
2. Refine with the custom attributes Talkable sends—for example, `talkable_is_advocate` equals `true` to target advocates, or `talkable_campaign_name` equals your campaign to target a specific referral program.

### Trigger lifecycle messaging

1. Build a Canvas or campaign with action-based delivery. The following Braze trigger types work with this integration: 
* **Update Subscription Status** (for example, email subscription becomes **Opted In**)
* **Update Subscription Group Status** (when a subscription group is configured)
* **Change Custom Attribute Value** (for any Talkable custom attribute you send).
2. Personalize messages with the Talkable custom attributes on the profile (campaign name, reward value, referrer, and so on).

## Considerations

* **Email opt-in only:** Phone numbers are captured as a standard user attribute, but the integration does not set an SMS subscription state. Talkable does not sync SMS opt-ins.
* **Phone format:** Braze expects phone numbers in international (E.164) format.
* **Real-time, event-driven sync:** Talkable sends one request per opt-in event (one user per request). There is no batching and no periodic full sync; volume tracks your referral opt-in volume.
* **Reliable delivery:** If Braze temporarily returns an error, Talkable retries automatically. Persistent failures send an email alert to the site's administrator.

## Troubleshooting

| Error | Likely cause | Fix |
| --- | --- | --- |
| 401 Unauthorized | REST API key is missing the `users.track` permissions, or the endpoint points to the wrong cluster. | Re-issue the key with the `users.track` permissions and confirm the REST endpoint matches your Braze cluster. |
| REST endpoint rejected at install | The URL is not a Braze REST endpoint. | Use your cluster's REST endpoint, for example `https://rest.iad-01.braze.com`. A dashboard URL does not work. |
| Profile created but not in a subscription group | No subscription group ID configured. | Enter the subscription group ID on the **Email opt-in** action. |
| User alias not applied | Only one of the two alias fields (name or label) is filled in. | Enter both fields on the action: alias name and alias label. |
| Profile not appearing | Sample request not yet sent, or the action is disabled. | Select **Send sample payload** in Talkable and ensure the **Email opt-in** action is enabled. |
| Requests stopped sending after a key rotation | The stored API key was revoked or replaced in Braze. | In the Talkable **App Store**, open the Braze app, paste the new REST API key, and select **Save**; re-test with **Send sample payload**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Troubleshooting" }

For more information about the Talkable integration, see the [Talkable Braze integration documentation](https://docs.talkable.com/email_marketing_and_automation/braze/). To contact Talkable support, email [support@talkable.com](mailto:support@talkable.com).
