---
nav_title: Authentication and security
article_title: Device Messaging API authentication and security
permalink: /api/device_messaging_api/authentication
page_order: 1
page_type: reference
description: "Learn how to authenticate Device Messaging API requests securely."
hidden: true
---

# Device Messaging API authentication and security

{% alert important %}
This page is in beta. Features and documentation for the Device Messaging API are subject to change.
{% endalert %}

The Device Messaging API uses client-side REST API keys. These keys are distinct from the private REST API keys used for server-side Braze REST API requests.

## Client-side REST API keys

Client-side REST API keys are scoped to one workspace and restricted to Device Messaging API permissions. You can embed these keys in client applications.

{% alert important %}
Use only a client-side REST API key in a client application. Never expose a private server-side REST API key in client-side code.
{% endalert %}

To create a client-side REST API key:

1. Go to **Settings** > **APIs and Identifiers** > **API Keys** in the Braze dashboard.
2. Select **Create API Key**.
3. For **Key type**, select **Client**.
4. Assign the `banners.sync` permission to retrieve Banners, the `banners.track` permission to report Banner events, or both.

## Authenticating requests

Send the client-side REST API key as a bearer token in the `Authorization` header:

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

Use HTTPS and the [REST endpoint]({{site.baseurl}}/api/basics#endpoints) for your Braze instance.

## User identity

A client-side REST API key authenticates the calling application and workspace, not the user. The `external_user_id` in a request identifies the user associated with Banner content and events.

Apply your application's authorization controls before making Device Messaging API requests.

## Authentication errors

Authentication and permission failures can differ by endpoint. Refer to each endpoint's status-code table and [Device Messaging API error handling]({{site.baseurl}}/api/device_messaging_api/error_handling).
