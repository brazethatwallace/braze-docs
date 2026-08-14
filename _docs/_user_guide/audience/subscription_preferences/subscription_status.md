---
nav_title: Subscription status
article_title: Subscription status
page_order: 0
page_type: reference
description: "Learn how Braze tracks subscription status across email, LINE, SMS, RCS, and WhatsApp, and how status gates message delivery."

---

# Subscription status

> Learn how Braze tracks subscription status across messaging channels, how global and subscription group status interact, and where channel-specific rules apply.

Subscription status tells Braze whether a user is eligible to receive messages on a channel. Status can gate campaign and Canvas targeting, segment filters, and whether Braze attempts delivery.

## How subscription status works in Braze

Braze tracks subscription status at two levels:

| Level | What it controls | Channels |
| ----- | ---------------- | -------- |
| Global subscription state | Whether a user can receive messages on that channel at all | Email, push |
| Subscription group status | Whether a user is opted in to a specific group within a channel | Email, SMS, MMS, RCS, WhatsApp, LINE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="How subscription status works in Braze" }

Global state and subscription group status work together. For email, a user who is globally unsubscribed won't receive email even if they're subscribed to a subscription group. For SMS, RCS, WhatsApp, and LINE, users must be subscribed to the relevant subscription group to receive messages from that group.

You can view and update subscription status on a user's profile in **Engagement** > **Contact settings**, through the REST API, SDK, CSV import, preference centers, and channel-specific opt-in flows. Braze doesn't count subscription state changes against your data points.

{% alert note %}
Subscription groups add granular opt-in within a channel (for example, promotional versus transactional SMS). Global email state and subscription group membership work together when deciding who is reachable.
{% endalert %}

## Email {#email}

Braze has three global subscription states for email. These states gate whether users receive messages targeted at subscribed or opted-in audiences. For example, users in the `unsubscribed` state don't receive messages targeted at `subscribed` or `opted-in` users.

| State | Definition |
| ----- | ---------- |
| Opted-in | A user has explicitly confirmed they want to receive email. Braze recommends an explicit opt-in process to get consent from users to send emails. |
| Subscribed | A user has neither unsubscribed nor explicitly opted in to receive emails. This is the default subscription state when a user profile is created. |
| Unsubscribed | A user has explicitly unsubscribed from your emails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email subscription states" }

### Email-specific behavior

- **Unsubscribes and spam reports:** Braze automatically unsubscribes users who unsubscribe through a [custom footer]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer). If a user marks an email as spam, Braze sends only transactional email (messages sent with **Send to all users including unsubscribed users**).
- **Hard bounces:** When an email address hard bounces, Braze doesn't automatically set the user's subscription state to `unsubscribed`. Braze marks the address invalid and stops sending until the user updates their email address.
- **Shared email addresses:** When a user's global email subscription state changes, Braze propagates that state to other profiles that share the same email address, up to 100 profiles per change.
- **Email address updates:** When a user updates their email address, their subscription state is set to `subscribed` unless the updated address already exists on another profile, in which case the user inherits that profile's state.

For updating subscription state, checking status, preference centers, and campaign targeting, see [Email subscriptions]({{site.baseurl}}/user_guide/channels/email/subscriptions).

## LINE {#line}

LINE is the source of truth for LINE subscription status. Even if a user profile has a `native_line_id`, Braze won't deliver LINE messages unless that user follows your LINE channel.

LINE subscription status is tracked by `native_line_id`, not `external_id`. If multiple profiles share the same `native_line_id`, they inherit the same LINE subscription status.

| State | Definition |
| ----- | ---------- |
| Subscribed | The user followed your LINE channel from within their LINE app. |
| Unsubscribed | The user hasn't followed your LINE channel, or explicitly unfollowed it. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE subscription states" }

### Subscription sync tool

After a successful LINE channel integration, Braze deploys a subscription sync tool to align existing Braze profiles with LINE follower data:

- Profiles with a `native_line_id` that follows your channel are updated to `subscribed`.
- Followers without a matching Braze profile get an anonymous profile with `native_line_id`, a `line_id` user alias, and `subscribed` status.

You can't set LINE subscription group state manually during integration—LINE controls status, and Braze syncs it.

### Follow and unfollow event updates

When Braze receives LINE webhook events for your integrated channel:

- **Follow:** All profiles with a matching `native_line_id` are set to `subscribed`. If no profile exists, Braze [creates an anonymous user]({{site.baseurl}}/user_guide/channels/line/message_users/user_management).
- **Unfollow:** All profiles with a matching `native_line_id` are set to `unsubscribed`.

For setup steps, user reconciliation, and use cases, see [LINE setup]({{site.baseurl}}/user_guide/channels/line/line_setup#user-setup) and [LINE subscription groups]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

## SMS and RCS {#sms-and-rcs}

SMS and RCS use subscription group status, not a separate global channel state. A user can be `subscribed` to a transactional group and `unsubscribed` from a promotional group at the same time.

| State | Definition |
| ----- | ---------- |
| Subscribed | The user is subscribed to receive SMS and RCS from a specific subscription group, either through the Braze subscription API, an opt-in keyword, or another supported method. When [double opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) is enabled, users must confirm opt-in before status updates to `Subscribed`. |
| Unsubscribed | The user opted out of that subscription group by texting an opt-out keyword or through the [Braze subscription API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS and RCS subscription states" }

### SMS and RCS-specific behavior

- **Phone number inheritance:** When a phone number is added or updated on a profile, the number inherits subscription group status from the profile or from any existing profile that already uses that number.
- **Keyword handling:** Users can opt in or out by texting default or custom [keywords]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout). Braze updates subscription state automatically.
- **Compliance:** Braze never sends SMS or RCS to users who aren't subscribed to the selected subscription group.

For setup, sending, and managing subscription groups, see [SMS, MMS, and RCS subscription groups]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

## WhatsApp {#whatsapp}

WhatsApp also uses subscription group status. Meta requires explicit [opt-in consent](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) before you send marketing messages.

| State | Definition |
| ----- | ---------- |
| Subscribed | The user explicitly confirmed they want WhatsApp messages from your business, through an opt-in flow or the Braze subscription API. |
| Unsubscribed | The user hasn't opted in, or their opt-in was removed. Unsubscribed users don't receive messages from phone numbers in that subscription group. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp subscription states" }

### Opt-in requirements

To message users on WhatsApp, provide Braze with an `external_id`, a [phone number]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers), and an updated subscription status for each user. Collect opt-ins on your website, app, SMS, in-app messages, inbound WhatsApp threads, or through a CSV import of users who already opted in elsewhere.

### Opt-out methods

Users can opt out through:

- **Inbound keyword workflows:** Canvases or campaigns triggered by opt-out keywords (for example, "STOP"), with a follow-up step that updates subscription status.
- **Marketing opt-out quick replies:** Message templates with Meta's marketing opt-out button, paired with a subscription group update step in your Canvas.
- **Blocks and reports:** If a user blocks your business, subsequent messages don't deliver and aren't billed, but Braze subscription status doesn't update. User reports don't change subscription status either.

### WhatsApp "Offers and Announcements" toggle

WhatsApp's native **Offers and Announcements** toggle is separate from Braze subscription groups. When a user turns it off in WhatsApp, Meta blocks marketing delivery even if Braze shows `subscribed`. The two layers don't sync automatically.

For step-by-step opt-in and opt-out workflows, see [WhatsApp opt-ins and opt-outs]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) and [WhatsApp subscription groups]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

## Segment and target by subscription status

Use subscription status filters in the segment builder to target or suppress audiences by channel—for example, **Email Subscription Status**, **Push Subscription Status**, and **Subscription Group** filters.

When building campaigns and Canvases, **Send Settings** and **Target Audience** options let you send only to users with a specific subscription status (such as subscribed and opted-in). For email and push filter definitions, see [Segmentation filters]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
