---
nav_title: "POST: Change email subscription status"
article_title: "POST: Change Email Subscription Status"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "This article outlines the details about the Change user's email subscription status Braze endpoint."

---
{% api %}
# Change email subscription status
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Use this endpoint to set the global email subscription state for your users.

Users can be `opted_in`, `unsubscribed`, or `subscribed` (not specifically opted in or out).

{% alert note %}
This endpoint updates the user's global email subscription state, which is different from subscription group status. The global subscription state applies across all emails, while [subscription groups]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) allow more granular control over specific types of emails. When a user is globally unsubscribed, they won't receive emails regardless of their subscription group status. To query subscription group status, use the [List user's subscription group status endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status).
{% endalert %}

You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded is automatically set.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key) with the `email.status` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@example.com",
  "subscription_state": "subscribed"
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `email` | Required | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
| `subscription_state` | Required | String | Either "subscribed", "unsubscribed", or "opted_in". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## Troubleshooting SendGrid email blocks

When SendGrid blocks a recipient, update subscription status with this endpoint and review engagement with segment filters. Use [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) soft-bounce events for deliverability monitoring, and confirm subscription state before retrying sends.

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@example.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}
