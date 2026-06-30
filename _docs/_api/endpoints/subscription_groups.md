---
nav_title: Subscription groups
article_title: Subscription Group Endpoints
page_order: 7
layout: dev_guide

#Required
description: "This landing page explains and lists the Braze subscription groups endpoints for email and SMS."
page_type: landing
search_tag: Endpoint

guide_top_header: "Subscription Groups Endpoints"
guide_top_text: "Use the Subscription Group REST APIs to programmatically manage the subscription groups that you have stored on the Braze dashboard, on the **Subscription Group** page. This applies to both SMS and email subscription groups.<br><br> Looking for guidance on creating subscription groups? Check out our articles for <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>SMS subscription groups</a> and <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>email subscription groups</a>."

guide_featured_title: ""
guide_featured_list:
  - name: "GET: List User's Subscription Group Status"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: List User's Subscription Groups"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Update User's Subscription Group Status"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
    image: /assets/img/braze_icons/user-plus-01.svg
  - name: "POST: Update User's Subscription Group Status V2"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/
    image: /assets/img/braze_icons/user-edit.svg
---
<br>
<br>


## Understand subscription group timeseries

On the **Subscription Group** page, timeseries charts report:

- **Subscription Group Size**—users subscribed to that group on a given date
- **Subscription Group Unsubscribed Size**—users unsubscribed from that group on a given date

For dashboard guidance, see [Viewing subscription group sizes]({{site.baseurl}}/user_guide/channels/email/subscriptions/#viewing-subscription-group-sizes).

These metrics are group-specific. They can differ from the segment filter **Email Subscription Status is Unsubscribed**, which reflects global email subscription state rather than a single subscription group. For very large workspaces, Braze may display estimated counts when exact counts are unavailable.

## Avoiding duplicate users from email capture forms

Before you create a user from an email capture form, call [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) to check whether the profile already exists. If the response is **User not found**, create the user with [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Otherwise, update the existing profile instead of creating a duplicate.

## Snowflake `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` events

The `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` Snowflake table logs message-level email unsubscribes originating from the recipient's side—clicking an unsubscribe link, the email client's one-click List-Unsubscribe, preference center submissions, and ESP-reported unsubscribes. Unsubscribes made through the REST API are not included in this table; those emit [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events) or [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#global-subscription-state-change-events) events instead.

## SMS test messages and subscription groups

Users must belong to the SMS subscription group you select when you send an SMS test message to receive that test.
