---
nav_title: "POST: Create new user alias"
article_title: "POST: Create New User Alias"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the Create new user alias Braze endpoint."
---
{% api %}
# Create new user alias
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Use this endpoint to add new user aliases for existing identified users, or to create new unidentified users.

Up to 50 user aliases may be specified per request.

**Adding a user alias for an existing user** requires an `external_id` to be included in the new user alias object. If the `external_id` is present in the object but there is no user with that `external_id`, the alias will not be added to any users. If an `external_id` is not present, a user will still be created but will need to be identified later. You can do this using the "Identifying Users" and the `users/identify` endpoint.

**Creating a new alias-only user** requires the `external_id` to be omitted from the new user alias object. After the user is created, use the `/users/track` endpoint to associate the alias-only user with attributes, events, and purchases, and the `/users/identify` endpoint to identify the user with an `external_id`.

You can send API-triggered campaigns to users by `user_alias` using the [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) endpoint.

## When `alias_label` and `alias_name` already exist

The combination of `alias_label` and `alias_name` must be unique across your user base. For more information, see [User aliases]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases).

If you send a request where the `alias_label` and `alias_name` pair already exists for any user (whether on the same user or another), the endpoint still returns a successful response (for example, `"aliases_processed": 1`, `"message": "success"`). In that case, no new alias is added to the user in the request. Because the `alias_label` and `alias_name` pair is already in use, the request does not make any changes, and it can appear that the alias was never added to the user in question.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics) with the `users.alias.new` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Required | Array of new user alias objects | See [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object).<br><br> For more information on `alias_name` and `alias_label`, check out our [User Aliases]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) documentation.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

### Endpoint request body with new user alias object specification

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Response

When an alias is skipped because the same `alias_label` and `alias_name` already exist for a user, the response body may still indicate success. See [When the alias label and name already exist](#when-the-alias-label-and-name-already-exist) for details.

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

## Troubleshooting

### Why are my attributes not updating after I create a user alias using this endpoint?

This usually happens when `/users/alias/new` is followed by a separate `/users/track` request that tries to update attributes by alias. The track request can be processed before Braze can consistently resolve the new `alias_label` and `alias_name` pair to a profile, so attributes do not land on the user you expect.

**Recommended approach:** Use a single [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) call only when you want to create an alias-only profile or update a profile by an alias that already exists. In the `attributes` array, put `user_alias` and your profile fields in the same [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/) so Braze resolves the user and applies the update in one step.

Set `_update_existing_only` to `false` when you may need to create an alias-only profile from that object. If you omit it while using `user_alias`, Braze defaults to update-only behavior and does not create the alias-only profile. If the alias already exists on a user in your workspace, the same request updates that profile with your new attributes.

You can't use `/users/track` to add a new alias to an existing user identified by `external_id`. In a user attributes object, `external_id` and `user_alias` are mutually exclusive. To add an alias to an identified user, first call `/users/alias/new`. After the alias is attached, you can update that profile with `/users/track` by `external_id` or by the existing alias.

For example, the following `/users/track` body creates an alias-only profile if the alias doesn't exist yet, or updates the existing profile that already has that alias:
```json
{
  "attributes": [
    {
      "user_alias": {
        "alias_name": "example@example.com",
        "alias_label": "email"
      },
      "_update_existing_only": false,
      "string_attribute": "test_alias_only_update"
    }
  ]
}
```

{% endapi %}
