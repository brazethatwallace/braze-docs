---
nav_title: "PUT: Replace an asset in the media library"
article_title: "PUT: Replace an asset in the media library"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "This article outlines details about the `PUT /media_library/replace_file` endpoint."
---

{% api %}
# Replace an asset in the media library
{% apimethod put %}
/media_library/replace_file
{% endapimethod %}

> Use this endpoint to replace the file of an existing asset in the [Braze media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library) while preserving its asset ID and URL. You can provide the replacement file using either an externally hosted URL (`asset_url`) or binary file data sent in the request body (`asset_file`).

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key) with the `media_library.replace` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## Request body

When you include `asset_url`, the endpoint downloads the file from the URL. When you include `asset_file`, the endpoint uses the binary data in the request body.

Example request body for `asset_url`:

```json
{
  "asset_id": "your-asset-id",
  "asset_url": "https://cdn.example.com/assets/cat.jpg"
}
```

Example request body for `asset_file`:

```json
{
  "asset_id": "your-asset-id",
  "asset_file": <BINARY FILE DATA>
}
```

The request body includes the following parameters:

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `asset_id` | Required | String | The ID of the asset to replace. |
| `asset_url` | Optional | String | A publicly accessible URL for the replacement file. |
| `asset_file` | Optional | Binary | Binary file data for the replacement file. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request body" }

{% alert important %}
`asset_url` and `asset_file` are mutually exclusive, you must only include one of them in your API request.
{% endalert %}

### Replacement file requirements

- The replacement file's extension must exactly match the extension of the existing asset. For example, you cannot replace a `.png` asset with a `.jpg` file.
- File replacement is supported for images, SVGs, documents, fonts, contact cards, and code files. Video assets cannot be replaced.

## Example request

This section includes two example `curl` requests, one for replacing an asset using a URL and another using binary file data.

This request shows an example of replacing an asset in the media library using an `asset_url`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_url": "https://cdn.example.com/assets/cat.jpg"}'
```

This request shows an example of replacing an asset in the media library using an `asset_file`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_file":<BINARY FILE DATA>}'
```

### Error responses

This section lists potential errors and their corresponding messages and descriptions.

#### Validation errors

Validation errors return a structure like this:

```json
{
  "message": (String) Human-readable error description
}
```

This table lists possible validation errors.

| HTTP Status | Message | Description |
| --- | --- | --- |
| 400 | "asset_id is required." | No asset ID was provided in the request. |
| 400 | "Either file or asset_url is required." | Neither `asset_file` nor `asset_url` was provided; one is required. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Validation errors" }

#### Processing errors

Processing errors return a different response with error codes:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

This table lists possible processing errors.

| Error Code | HTTP Status | Description |
| --- | --- | --- |
| `ASSET_NOT_FOUND` | 404 | No asset with the given `asset_id` exists in this workspace. The `meta` object includes `asset_id`. |
| `INVALID_ASSET_URL` | 400 | The `asset_url` value is not a valid URI. The `meta` object includes `asset_url`. |
| `EXTENSION_MISMATCH` | 400 | The replacement file's extension does not match the existing asset's extension. The `meta` object includes `expected_extension` and `received_extension`. |
| `UNSUPPORTED_ASSET_TYPE_FOR_REPLACE` | 400 | File replacement is not supported for this asset type (for example, video). The `meta` object includes `asset_type`. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | The file exceeds the maximum allowed size. The `meta` object includes `size_limit_bytes` and `file_size_bytes`. |
| `CORRUPT_FILE` | 400 | The image file is corrupted or unreadable. The `meta` object includes `file_name`. |
| `GENERIC_ERROR` | 500 | An unexpected error occurred during file replacement. The `meta` object includes `original_error` for debugging. Try again or contact [Support]({{site.baseurl}}/support_contact). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Processing errors" }

## Response

There are five status code responses for this endpoint: `200`, `400`, `404`, `429`, and `500`.

The following JSON shows the expected shape of the response.

```json
{
  "info": "Asset file updated successfully.",
  "new_image_asset": {
    "name": (String) the name of the asset,
    "size": (Integer) the byte size of the asset,
    "url": (String) the URL to access the asset,
    "ext": (String) the file extension (e.g., "png", "jpg", "gif")
  }
}
```

{% endapi %}
