---
nav_title: "PUT: Replace multiple catalog items"
article_title: "PUT: Replace Multiple Catalog Items"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "This article outlines details about the Replace multiple catalog items Braze endpoint."

---
{% api %}
# Replace catalog items
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use this endpoint to replace multiple items in your catalog.

If a catalog item doesn't exist, this endpoint will create the item in your catalog. Each request can support up to 50 catalog items. This endpoint is asynchronous.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `catalogs.replace_items` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `catalog_name` | Required | String | Name of the catalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | An array that contains item objects. Each object must have an ID. The item objects should contain fields that exist in the catalog. Up to 50 item objects are allowed per request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Example request

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

{% alert note %}
The `Location` field uses the `geo` data type, which expects an array formatted as `[longitude, latitude]`.
{% endalert %}

## Response

There are three status code responses for this endpoint: `202`, `400`, and `404`.

{% alert note %}
The system can also return a `400` response if your company has reached its catalog storage limit. The free version of catalogs is capped at 100&nbsp;MB. For more information about storage tiers and how to upgrade, see [Data storage limitations]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations).
{% endalert %}

### Example success response

The status code `202` could return the following response body.

```json
{
  "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to [Troubleshooting](#troubleshooting) for more information about errors you may encounter.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `catalog-not-found` | Check that the catalog name is valid. |
| `company-size-limit-already-reached` | The catalog storage size limit is reached. To learn about storage tiers, see [Data storage limitations]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `company-size-limit-surge` | The request exceeds your company's remaining catalog storage. Try again with a smaller update. To learn about storage tiers, see [Data storage limitations]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `ids-not-string` | Confirm that each item ID is a string. |
| `ids-not-unique` | Check that each item ID is unique. |
| `ids-too-large` | Character limit for each item ID is 250 characters. |
| `item-array-invalid` | `items` must be an array of objects. |
| `items-missing-ids` | Some items don't have item IDs. Confirm that each item has an ID. |
| `items-too-large` | Item values can't exceed 5,000 characters. |
| `invalid-ids` | Supported characters for item ID names are letters, numbers, hyphens, and underscores. |
| `invalid-fields` | Confirm that all fields you are sending in the API request already exist in the catalog. This is not related to the ID field mentioned in the error. |
| `invalid-keys-in-value-object` | Item object keys can't include `.` or `$`. |
| `too-deep-nesting-in-value-object` | Item objects can't have more than 50 levels of nesting. |
| `request-includes-too-many-items` | Your request has too many items. The item limit per request is 50. |
| `unable-to-coerce-value` | Item types can't be converted. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}
