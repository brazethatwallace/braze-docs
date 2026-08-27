---
nav_title: "GET: Look up an existing dashboard user account"
article_title: "GET: Look Up an Existing Dashboard User Account"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Look up an existing dashboard user account resource ID Braze endpoint."
---

{% api %}
# Look up an existing dashboard user account by resource ID
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> Use this endpoint to look up an existing dashboard user account by specifying the resource `id` returned by the SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account) method.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Prerequisites

To use this endpoint, you'll need a SCIM token. You'll use your service origin as the `X-Request-Origin` header. For more information, refer to [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning).

## Rate limit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `id` | Required | String | The user's resource ID. This parameter is returned by the `POST` `/scim/v2/Users/` or `GET`  `/scim/v2/Users?filter=userName eq "user@example.com"` methods. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

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
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Response
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@example.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "2024 Nov 11, 4:20 PM",
    "createdAt": "2024 Nov 11, 4:20 PM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7",
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    }
                ]
            }
        ],
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
```

## Response parameters

| Parameter | Data type | Description |
|---|---|---|
| `schemas` | Array of strings | SCIM user schema. |
| `id` | String | The user's resource ID. |
| `userName` | String | The user's email address. |
| `name` | Object | Contains `givenName` and `familyName`. |
| `department` | String | The user's department, if set. |
| `createdAt` | String | When the user account was created. Returns `N/A` when unset; otherwise formatted as `YYYY Mon DD, H:MM AM/PM`. |
| `lastSignInAt` | String | When the user last signed in. Returns `N/A` if the user has not signed in; otherwise formatted as `YYYY Mon DD, H:MM AM/PM`. |
| `permissions` | Object | Company, workspace, team, and role permissions for the user. See the [permissions object]({{site.baseurl}}/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response parameters" }

### Error states

If no user exists for the provided resource `id`, the endpoint returns:

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 404,
  "detail": "Resource not found"
}
```

{% endapi %}