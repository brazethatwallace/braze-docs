---
nav_title: "GET: Search existing dashboard user account by email"
article_title: "GET: Search Existing Dashboard User Account by Email"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Search for an existing dashboard user account by email Braze endpoint."
---

{% api %}
# Search existing dashboard user account by email
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> Use this endpoint to look up an existing dashboard user account by specifying their email in the filter query parameter.

Note that when the query parameter is URL encoded, it reads like this:

`/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Prerequisites

To use this endpoint, you'll need a SCIM token. You'll use your service origin as the `X-Request-Origin` header. For more information, refer to [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning).

## Rate limit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Query parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `filter` | Required | String | SCIM filter expression to search by email. Braze supports `userName eq "user@example.com"` only. The email value must be wrapped in double quotes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Query parameters" }

{% alert important %}
Braze only supports exact-match filters on `userName` using the `eq` operator. Other SCIM filter fields or operators return a `400` response.
{% endalert %}

## Request parameters

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
If you receive a `401` response, confirm you're using a SCIM token (not a REST API key), that `X-Request-Origin` matches your service origin, and that your IP address is on the SCIM allowlist. For details, refer to [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning).
{% endalert %}

## Example request
```bash
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Response
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@example.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
            "name": {
                "givenName": "Test",
                "familyName": "User"
            },
            "department": "finance",
            "createdAt": "2024 Nov 11, 4:20 PM",
            "lastSignInAt": "N/A",
            "permissions": {
                "companyPermissions": ["manage_company_settings"],
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Test Workspace",
                        "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                        "team": [
                            {
                                "teamId": "241adcd25789fabcded",
                                "teamName": "Test Team",
                                "teamPermissions": ["admin"]
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

## Response parameters

| Parameter | Data type | Description |
|---|---|---|
| `schemas` | Array of strings | SCIM list response schema. |
| `totalResults` | Integer | Number of matching dashboard users (0 if no match). |
| `Resources` | Array | Array of user objects. Each object uses the same fields as [GET: Look up an existing dashboard user account]({{site.baseurl}}/get_see_user_account_information). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response parameters" }

### User object fields

| Parameter | Data type | Description |
|---|---|---|
| `id` | String | The user's resource ID. |
| `userName` | String | The user's email address. |
| `name` | Object | Contains `givenName` and `familyName`. |
| `department` | String | The user's department, if set. |
| `createdAt` | String | When the user account was created. Returns `N/A` when unset; otherwise formatted as `YYYY Mon DD, H:MM AM/PM`. |
| `lastSignInAt` | String | When the user last signed in. Returns `N/A` if the user has not signed in; otherwise formatted as `YYYY Mon DD, H:MM AM/PM`. |
| `permissions` | Object | Company, workspace, team, and role permissions. See the [permissions object]({{site.baseurl}}/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User object fields" }

### Error states

If the `filter` parameter is missing or malformed, the endpoint returns:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 400,
  "detail": "Request is unparsable, syntactically incorrect, or violates schema."
}
```

{% endapi %}

