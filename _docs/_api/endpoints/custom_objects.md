---
nav_title: Custom Objects
article_title: Custom Objects Endpoints
search_tag: Endpoint
page_order: 9.5
layout: dev_guide
page_type: landing
description: "This landing page lists the Braze Custom Objects endpoints."
needs_mermaid: true

guide_top_header: "Custom Objects Endpoints"
guide_top_text: "Use these endpoints to list custom object types, manage custom object records, and manage object and user relationships."
guide_top_alert: "Custom Objects is currently in early access. Your workspace must be enabled before the Custom Objects API key permissions appear on **Settings** > **API Keys**."

guide_featured_title: "Type endpoints"
guide_featured_list:
  - name: "GET: List Custom Object Types"
    link: /docs/api/endpoints/custom_objects/types/get_list_custom_object_types
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Get Custom Object Type"
    link: /docs/api/endpoints/custom_objects/types/get_custom_object_type
    image: /assets/img/braze_icons/search-md.svg
  - name: "GET: List User Relationship Types"
    link: /docs/api/endpoints/custom_objects/types/get_list_user_relationship_types
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: List Object Relationship Types"
    link: /docs/api/endpoints/custom_objects/types/get_list_object_relationship_types
    image: /assets/img/braze_icons/link-external-01.svg

guide_menu_title: "Object endpoints"
guide_menu_list:
  - name: "GET: List Custom Objects"
    link: /docs/api/endpoints/custom_objects/objects/get_list_custom_objects
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Get Custom Object"
    link: /docs/api/endpoints/custom_objects/objects/get_custom_object
    image: /assets/img/braze_icons/search-md.svg
  - name: "POST: Create Custom Object"
    link: /docs/api/endpoints/custom_objects/objects/post_create_custom_object
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Replace Custom Object"
    link: /docs/api/endpoints/custom_objects/objects/put_replace_custom_object
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Update Custom Object"
    link: /docs/api/endpoints/custom_objects/objects/patch_update_custom_object
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Delete Custom Object"
    link: /docs/api/endpoints/custom_objects/objects/delete_custom_object
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title2: "Object relationship endpoints"
guide_menu_list2:
  - name: "GET: List Object Relationships"
    link: /docs/api/endpoints/custom_objects/object_relationships/get_list_object_relationships
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Create Object Relationship"
    link: /docs/api/endpoints/custom_objects/object_relationships/post_create_object_relationship
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Replace Object Relationship"
    link: /docs/api/endpoints/custom_objects/object_relationships/put_replace_object_relationship
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Update Object Relationship"
    link: /docs/api/endpoints/custom_objects/object_relationships/patch_update_object_relationship
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Delete Object Relationship"
    link: /docs/api/endpoints/custom_objects/object_relationships/delete_object_relationship
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title3: "User relationship endpoints"
guide_menu_list3:
  - name: "GET: List User Relationships"
    link: /docs/api/endpoints/custom_objects/user_relationships/get_list_user_relationships
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Create User Relationship"
    link: /docs/api/endpoints/custom_objects/user_relationships/post_create_user_relationship
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Replace User Relationship"
    link: /docs/api/endpoints/custom_objects/user_relationships/put_replace_user_relationship
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Update User Relationship"
    link: /docs/api/endpoints/custom_objects/user_relationships/patch_update_user_relationship
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Delete User Relationship"
    link: /docs/api/endpoints/custom_objects/user_relationships/delete_user_relationship
    image: /assets/img/braze_icons/edit-05.svg
---

## Base URL and authentication

Use your workspace REST endpoint and send `Authorization: Bearer YOUR_REST_API_KEY`. This section explains where Custom Objects endpoints are hosted and how requests are authenticated.

- For endpoint hosts, refer to [Braze API overview]({{site.baseurl}}/api/basics#endpoints).
- All request and response payloads are JSON.
- Requests are scoped to the workspace that owns the API key.
- If the key has an IP allowlist, non-allowlisted IP addresses return `403`.

## API key permissions

This section maps each endpoint to its required permission so you can scope API keys safely.

| Permission | Endpoint group |
|---|---|
| `custom_objects.read` | Type and object reads, and object relationship reads |
| `custom_objects.create` | Object create |
| `custom_objects.update` | Object replace and update |
| `custom_objects.delete` | Object delete |
| `custom_objects.user_relationships.read` | User relationship reads |
| `custom_objects.user_relationships.create` | User relationship create |
| `custom_objects.user_relationships.update` | User relationship replace and update |
| `custom_objects.user_relationships.delete` | User relationship delete |
| `custom_objects.object_relationships.create` | Object relationship create |
| `custom_objects.object_relationships.update` | Object relationship replace and update |
| `custom_objects.object_relationships.delete` | Object relationship delete |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom Objects permission groups" }

{% alert note %}
Object relationship reads use `custom_objects.read`. There is no `custom_objects.object_relationships.read` permission.
{% endalert %}

## Rate limits

This section explains default request quotas and response headers for both read and write traffic.

| Bucket | Default limit |
|---|---|
| Custom Objects reads | 50 requests per minute |
| Custom Objects writes | 50 requests per minute |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom Objects default rate limits" }

Every response includes `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset`.

For throttled requests, Braze returns `429` and an error payload with `id` and `message`.

```json
{
  "errors": [
    {
      "id": "rate-limit-exceeded",
      "message": "You have exceeded your limit of 50 requests per minute."
    }
  ]
}
```

## Core concepts

This section defines the key identifiers used across all Custom Objects endpoints.

- `type_name`: The custom object type machine name, unique within a workspace.
- `external_id`: Your object identifier, unique within a type.
- `braze_id`: The Braze user ID used on user-relationship endpoints.
- `attributes`: Field-name-keyed object or relationship data validated against the configured schema.

## How relationships work

This section explains relationship types, relationship edges, and `anchor` behavior before you use the endpoint reference pages.

### Relationship model at a glance

Use this diagram to see how types, records, and relationships fit together, and what linking them lets you do in Braze. You define the types in the dashboard, then write the records and the links between them through these endpoints.

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 400}} }%%
flowchart LR
  subgraph define["Set up in the dashboard"]
    objtype["Custom object types define<br/>the fields a record has"]
    reltype["Relationship types determine<br/>which links are allowed"]
  end

  subgraph write["Write with the API"]
    person["A person you<br/>send messages to"]
    record["A business record<br/>they belong to"]
    related["Another record<br/>connected to it"]
    person -- "A user relationship links<br/>a person to a record" --> record
    record -- "An object relationship links<br/>one record to another" --> related
  end

  subgraph unlock["What it unlocks"]
    segment["Segment people by the<br/>records they belong to"]
    liquid["Personalize messages with<br/>data from those records"]
  end

  define -- "decides what you<br/>are allowed to link" --> write
  write -- "makes these<br/>possible" --> unlock
```

### Types and edges are separate

- Relationship types define which links are valid and are managed in the dashboard.
- Relationship edges are the actual links between records and are created, updated, and deleted through these API endpoints.
- Before writing relationships, list valid `rel_kind` values with:
  - `GET /custom_objects/types/{type_name}/user_relationship_types`
  - `GET /custom_objects/types/{type_name}/object_relationship_types`

### Why object relationships require `related_type_name`

- `rel_kind` is not globally unique across all object type pairs. For example, `rel_kind` can be `subaccount` for one pair of object types and `partner_account` for another.
- Object relationship writes therefore require both `rel_kind` and `related_type_name` to identify the intended relationship type along with the other type of object in the association.
- If the `related_type_name` does not match the relationship type for that `rel_kind`, the request returns `400`.

### `anchor` controls relationship direction

Object relationships are directional. The URL object is interpreted based on `anchor`.

| `anchor` | URL object role | Related object key in responses |
|---|---|---|
| `source` (default) | From side (outgoing edge) | `to_custom_object` |
| `target` | To side (incoming edge) | `from_custom_object` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Anchor behavior for object relationships" }

Creating the same edge from the opposite anchor perspective still targets one underlying relationship. A second create call for the same edge returns `409` (`duplicate-object-relationship`).

### Path asymmetry for user relationships

User relationship reads and writes intentionally use different endpoint paths:

- Read: `GET /custom_objects/objects/{type_name}/{external_id}/user_relationships`
- Write: `POST|PUT|PATCH|DELETE /custom_objects/objects/{type_name}/{external_id}/users`

### Relationship attributes are separate from object attributes

- Relationship endpoints return edge-level attributes in the top-level `attributes` field.
- Object attributes stay nested under `to_custom_object` or `from_custom_object`.
- `PUT` replaces relationship `attributes`, and `PATCH` merges relationship `attributes`.

### Worked example

This example shows a common account workflow:

1. Create `account/acct-123`.
2. Create `account/acct-456` as a child account.
3. Link a user to `acct-123` with `rel_kind: account_user`.
4. Link `acct-123` to `acct-456` with `rel_kind: subaccount`.

To read back the links:

- `GET /custom_objects/objects/account/acct-123/user_relationships` for linked users
- `GET /custom_objects/objects/account/acct-123/object_relationships` for outgoing object links
- `GET /custom_objects/objects/account/acct-456/object_relationships?anchor=target` for incoming object links

{% alert note %}
The `DELETE` endpoints for object relationships and user relationships require a JSON request body.
{% endalert %}

## Pagination and data freshness

This section covers list pagination behavior and expected data visibility timing after writes.

- List endpoints support `limit` and `offset`.
- `limit` defaults to `100` and is clamped to `1` through `250`.
- `offset` defaults to `0`, and negative values are floored to `0`.
- Writes are immediately visible to reads and Liquid personalization.
- Segment membership based on custom objects can lag by up to one hour because calculated filters refresh hourly.

## Error behavior

This section summarizes status and error response patterns used across the Custom Objects endpoints.

- `404`, `409`, `422`, and `429` return an `errors` array with `id` and `message`.
- `400`, `401`, and `403` return a single `error` string.
- Contract-based `422` limits vary by company.
