---
nav_title: "POST: Track Users (Bulk) for Braze Partners"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk_partners/
description: "If you're a Braze partner, use this endpoint to record custom events and purchases and update user profile attributes in bulk."
---

{% api %}
# Track users (bulk) for Braze Partners
{% apimethod post core_endpoint|/docs/core_endpoints %} 
/users/track/bulk
{% endapimethod %}

> If you're a Braze partner, use this endpoint to record custom events and purchases and update user profile attributes in bulk.

{% alert important %}
This endpoint is available for Braze partners to migrate bulk use cases in their Braze integration. For questions, contact [isv-support@braze.com](mailto:isv-support@braze.com).
{% endalert %}

## When to use this endpoint

Similar to the [POST: Track users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), you can use this endpoint to update user profiles. However, this endpoint is better suited for making bulk updates:

- **Larger requests:** This endpoint allows for 1,000 users per request, meaning that you have to make fewer requests to achieve your bulk update needs.  
- **Prioritization:** During peak traffic conditions, requests from `/users/track` will be prioritized over requests from `/users/track/bulk`. Using both endpoints provides you with more control over data ingestion.

Consider using this endpoint when you're backfilling many user profiles during onboarding or syncing large amounts of user profiles as part of a daily sync.

{% alert note %}
We plan on decreasing the `/users/track` object limit from 225 to 5 in order to encourage using `/users/track/bulk` instead. Keep this in mind, so you can ensure your Braze integration remains compatible with future updates.
{% endalert %}

## Prerequisites

To use this endpoint, you’ll need an [API key]({{site.baseurl}}/api/api_key/) with the `users.track` permission. This permission provides access to both `/users/track` and `/users/track/bulk`.

Because most of our shared customers will already be using an API key with `users.track` permissions for their Braze partner integration, they won't need to change API keys as you migrate your integration to use `/users/track/bulk`.

If your customers are using the API for server-to-server calls, they may need to allowlist the endpoint (for example, `rest.iad-01.braze.com`) if you're behind a firewall. Refer to the [endpoints per instance]({{site.baseurl}}/api/basics#endpoints) for more information.

## Rate limit

For most customers, we apply a base speed limit of 50 requests per second to this endpoint. 

However, customers on newer contracts may be given a burst (per second) and steady (per hour) rate limit instead, which is tied to their contracted MAU with Braze.

To improve real-time interactions with our API, be sure to use our [recommended response headers]({{site.baseurl}}/api/api_limits/#monitoring-your-rate-limits). 

Each `/users/sync/bulk` request has a payload limit of 2&nbsp;MB, and may contain up to 1,000 event, attribute, or purchase objects.

Each object (event, attribute, and purchase arrays) can update one user each, meaning a maximum of 1,000 different users can be updated in a single request. A single user profile can update a maximum of 100 objects in a single request.

## Request body


```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Request parameters

{% alert important %}
For each request component listed in the following table, one of `external_id`, `user_alias`, `braze_id`, `email`, or `phone` is required.
{% endalert %}

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array of attributes objects | See [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Array of event objects | See [events object]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Array of purchase objects | See [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example requests

### Bulk update 1,000 user profiles in one request

You can update up to 1,000 user profiles using the `/users/track/bulk` endpoint. Here’s a truncated example where the request consists of 1,000 attribute objects:

```javascript
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",	
            ]
        },

...

        {
            "external_id": "user1000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Here’s an example where the request consists of both attribute and event objects:

```javascript
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "external_id": "user2",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
...
        {
            "external_id": "user1000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        }
    ]
}'
```

## Responses

### Successful messages

Successful messages will be met with the following response:

```javascript
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Successful message with non-fatal errors

If your message is successful but has non-fatal errors, such as one invalid event object out of a long list of events, then you will receive the following response:

```javascript
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

### Message with fatal errors

If your message has a fatal error, you will receive the following response:

```javascript
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

#### Fatal error response codes

For status codes and associated error messages that will be returned if your request encounters a fatal error, reference [Fatal errors and responses]({{site.baseurl}}/api/errors/#fatal-errors).

If you receive the error`provided external\_id is blacklisted and disallowed`, your request may have included a `dummy user.` For more information, refer to [Spam blocking]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Frequently asked questions

### Should I use this endpoint or `/users/track`?

We recommend using both.

- For large user profile backfills and syncs, use the `/users/track/bulk` endpoint.
- For real-time use cases, use the `/users/track` endpoint.

{% alert note %}
We plan on decreasing the `/users/track` object limit from 225 to 5 in order to encourage using `/users/track/bulk` instead. Keep this in mind, so you can ensure your Braze integration remains compatible with future updates.
{% endalert %}

### What identifiers can I use in `/users/track/bulk`?

One of `external\_id`, `braze\_id`, `user\_alias`, `email`, or `phone` is required. See our documentation for [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/), [events object]({{site.baseurl}}/api/objects_filters/event_object/), or [purchases object]({{site.baseurl}}/api/objects_filters/purchase_object/) for further examples. 

### Can I include attributes, events, and purchases in one request?

Yes. You can construct your request with any amount of attributes, events, and purchase objects up to the limit of 1000 objects per request.  

{% endapi %}
