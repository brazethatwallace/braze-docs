---
nav_title: Overview
article_title: Messaging API overview
page_order: 0
page_type: reference
description: "Learn about the Braze Messaging API and its early access capabilities."
hidden: true
---

# Messaging API overview

The Braze Messaging API is a set of REST endpoints for integrating Braze messaging capabilities without a Braze SDK. You can call these endpoints from client or server applications.

{% alert important %}
This page is in beta. Features and documentation for the Messaging API are subject to change. Contact your Braze account manager to request access.
{% endalert %}

## Supported capabilities

During early access, you can use the Messaging API to:

- [Retrieve eligible Banners]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners) for an external user ID and a set of placements
- [Report Banner impression and click events]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)

The Messaging API returns structured Banner properties so you can build a custom interface. It doesn't return rendered HTML.

## Integration requirements

To integrate the Messaging API, you need:

- A workspace with the Messaging API enabled
- A client-side REST API key for that workspace
- The REST endpoint for that workspace
- The external user ID for the user
- The API identifier for the app

For more information about credentials, see [Authentication and security]({{site.baseurl}}/api/messaging_api/authentication).

## Messaging API and REST API guidance

The Messaging API uses the same regional REST endpoints as the Braze REST API, but it has a separate authentication and response contract. General REST API guidance about private server-side keys, response bodies, errors, and rate limits doesn't apply unless a Messaging API article explicitly references it.

Use the Messaging API endpoint documentation as the source of truth for request fields, response bodies, status codes, and limits.
