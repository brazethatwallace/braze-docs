---
nav_title: "Subscriptions"
article_title: "Subscriptions"
page_order: 5
description: "This reference article covers the different user subscription states, how to manage email subscriptions, and how to segment users based on their subscriptions."
channel:
  - email

---

# Email subscriptions

> Learn about global email subscription states, footers and unsubscribe pages, preference centers, and campaign targeting. For subscription groups across all channels, see [Subscription groups]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

This document is for informational purposes only. It is not intended to provide, nor may it be relied upon as providing legal advice in any capacity. Sending marketing and transactional emails may be subject to specific legal requirements. To ensure that you are doing so in compliance with all applicable laws, rules, and regulations specific to your company, you should seek the advice of your legal counsel and/or regulatory compliance team.

## Subscription states {#subscription-states}

Braze has three global subscription states for email users. These states gate your messages from users. For example, users in the `unsubscribed` state don't receive messages targeted at `subscribed` or `opted-in`.

| State | Definition |
| ----- | ---------- |
| Opted-in | A user has explicitly confirmed they want to receive email. We recommend an explicit opt-in process to get consent from users to send emails. |
| Subscribed | A user has neither unsubscribed nor explicitly opted-in to receive emails. This is the default subscription state when a user profile is created. |
| Unsubscribed | A user has explicitly unsubscribed from your emails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription states #subscription-states" }

{% alert note %}
Braze does not count subscription state changes against your data points, globally, and around subscription groups.
{% endalert %}

### Unsubscribed email addresses

Braze automatically unsubscribes any user who manually unsubscribes through a [custom footer]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer). If the user updates their email address and **Resubscribe users when they update their email** is enabled in **Sending Configuration**, normal sending resumes.

If a user marks one or more of your emails as spam, Braze sends only transactional emails to that user. Transactional emails refer to the **Send to all users including unsubscribed users** option in **Target Audience**.

{% alert tip %}
Refer to our [IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) best practices for guidance on how to re-engage your users effectively.
{% endalert %}

### Bounces and invalid emails

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

When an email address hard bounces, Braze doesn't automatically set the user's subscription state to "unsubscribed". If an address hard bounces (invalid or doesn't exist), Braze marks it invalid and doesn't attempt further sends. If the user changes their email address, Braze resumes sending. Braze retries soft bounces for 72 hours.

### Updating email subscription states

There are four ways to update a user's email subscription state:

#### SDK integration

Use the Braze SDK to update a user's subscription state.

#### REST API

Use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track) to update the [`email_subscribe` attribute]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) for a user. For example, to set a user's email subscription state to unsubscribed when they use a custom unsubscribe link, include `email_subscribe: "unsubscribed"` in the user attributes in your request.

#### User profile

1. Find the user through **Search Users**. 
2. Under **Engagement**, select **Unsubscribed**, **Subscribed**, or **Opted In** to change the user's subscription status. 

The user profile also displays a timestamp for when the user's subscription was last changed. A timestamp is recorded when the state is **Opted-in** or **Unsubscribed**, but not when the state is **Subscribed** — for example, a newly created profile that has never explicitly opted in or out has no subscription timestamp.

#### Preference center

Include [Preference center](#email-preference-center) Liquid at the bottom of your emails to let users opt in or out. Braze manages subscription state updates from the preference center.

### Checking email subscription state

![User profile for John Doe with their email subscription state set to Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Use any of the following methods to check a user's email subscription state:

1. **REST API export:** Use the [Export users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) or [Export users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) endpoints to export individual user profiles in JSON format.
2. **User profile:** Find the user's profile on the [Search Users]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) page, then select the **Engagement** tab to view and manually update a user's subscription state.

When a user updates their email address, their subscription state is set to subscribed. If the updated email address already exists elsewhere in a Braze workspace, the user inherits the subscription state from that existing user unless **Resubscribe users when they update their email setting** is turned on in **Sending Configuration**.

To troubleshoot subscription state changes, review **Email Subscription-State Changes** in the user profile logs for the history and source. The following sources can trigger an email subscription state change:

| Source | Description |
| ------ | ----------- |
| SDK | User attribute update sent through a Braze SDK |
| REST API | User attribute update sent through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) endpoint |
| Dashboard | Subscription state changed manually on the user profile page |
| CSV Import | Subscription state set during a user CSV import |
| Preference Center | User updated their preference from a Braze-hosted preference center |
| Subscription Page | User selected an unsubscribe link in an email and landed on the Braze subscription page |
| List-Unsubscribe | User unsubscribed through the email client's native list-unsubscribe header |
| Canvas User Update Step | Subscription state updated by a [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update) in a Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email subscription state update sources" }

When a user's global email subscription state changes, Braze propagates that state to other profiles that share the same email address, up to 100 profiles per change. Braze does not guarantee propagation when more than 100 profiles share the same email address. If users who share an email show different subscription states, contact Braze Support.

## Subscription groups

Email subscription groups let users opt in or out of specific email categories (such as newsletters or promotions) without changing their global email subscription state. Groups you create are available to add to your [preference center]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

To learn how subscription groups work across Braze—including creating groups, segmenting, archiving, and channel-specific behavior—see [Subscription groups]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups).

## Email preference center

The email preference center lets you manage which users receive subscription group newsletters. Find it in the dashboard under **Subscription Groups**. Each subscription group you create is added to the preference center list. 

To learn more about how to add or customize a preference center, refer to [Preference center]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).


## Changing email subscriptions {#changing-email-subscriptions}

In most cases, users manage their email subscription through links included in the emails they receive. Insert a legally compliant footer with an unsubscribe link at the bottom of every email. When users select the unsubscribe URL, Braze unsubscribes them and shows a landing page confirming the change. Include this Liquid tag: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

{% alert note %}
You can use the {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%} Liquid tag only in email campaigns and Canvases. You cannot use this tag in other messaging channels.
{% endalert %}

When a user selects "Unsubscribe from all of the listed types of emails" in the preference center, Braze sets their global email subscription status to `unsubscribed` and unsubscribes them from all groups.

### Creating custom footers {#custom-footer}

If you don't want to use the default footer, create a workspace-wide custom email footer and template it into every email using {% raw %}`{{${email_footer}}}`{% endraw %}.

This lets you avoid creating a new footer for every email template or email campaign. For steps, see [Custom email footer]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer).

#### Managing subscription states for Chinese IP addresses

If you anticipate Chinese IP addresses, don't rely solely on an unsubscribe link to maintain `unsubscribed` lists. Provide alternate unsubscribe paths such as a support ticket or customer representative email. 

### Creating a custom unsubscribe page

When users select an unsubscribe URL in an email, they open a default landing page that confirms the subscription change.

To use a custom landing page instead:

1. Go to **Email Preferences** > **Subscription Pages and Footers**.
2. Add the HTML for your custom page.

Include a resubscribe link (for example {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) so users can undo an accidental unsubscribe. Like {% raw %}`${set_user_to_unsubscribed_url}`{% endraw %}, you can use this tag in only email campaigns and Canvases.

You can also send users to your site and update status with the Braze REST API (for example link with {% raw %}`?user_id={{${user_id}}}`{% endraw %} and then call [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status).

{% alert note %}
If you use the dashboard footer instead of only an HTML content block, the template must still contain {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} to save. To use a different unsubscribe URL temporarily, you can comment out the default tag. An example is: {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}.
{% endalert %}

![Custom unsubscribe page with a preview "Sorry to see you go!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Creating a custom opt-in page

Use a custom opt-in page to let users acknowledge and control notification preferences before subscription. This additional communication can help email campaigns stay out of spam folders.

1. Go to **Settings** > **Email Preferences**.
2. Select **Subscription Pages and Footers**.
3. Customize the styling in the **Custom opt-in page** section to see how that indicates to your users that they've been subscribed.

Users reach this page through the {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} tag. Like other email subscription Liquid tags, you can use this tag in only email campaigns and Canvases.

{% alert tip %}
Use a double opt-in process to improve outreach. Braze sends an additional confirmation email where a user confirms notification preferences via a link. After confirmation, the user is opted in.
{% endalert %}

![Custom opt-in email with a message "Glad to see you still want to hear from us".]({% image_buster /assets/img/custom_optin.png %})

## Subscriptions and campaign targeting {#subscriptions-and-campaign-targeting}

By default, Braze targets campaigns with push or email messages at users who are subscribed or opted in. Change this in **Target Audience** by selecting the dropdown next to **Send to these users:**.

Braze supports three targeting states:

- Users who are subscribed or opted-in (default).
- Only users who are opted-in.
- All users, including those who have unsubscribed.

{% alert important %}
It's your responsibility to comply with any applicable [spam laws]({{site.baseurl}}/help/best_practices/spam_regulations#spam-regulations) when using these targeting settings.
{% endalert %}

## Segmenting by user subscriptions {#segmenting-by-user-subscriptions}

Use the "Email Subscription Status" and "Push Subscription Status" filters to segment users by subscription status.

Use this to target users who have neither opted in nor out and encourage an explicit opt in. Create a segment with the filter "Email/Push Subscription Status is Subscribed" and send campaigns to users who are subscribed but not opted in.

![Email Subscription Status used as a segment filter.]({% image_buster /assets/img_archive/not_optin.png %})

