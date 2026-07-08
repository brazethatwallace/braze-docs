---
nav_title: "POST: Update push credentials"
article_title: "POST: Update Push Credentials"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the Update push credentials Braze endpoint."
---

{% api %}
# Update push credentials
{% apimethod post core_endpoint|/docs/core_endpoints %}
/apps/push_credential/update
{% endapimethod %}

> Use this endpoint to programmatically update the push credentials for a single app, so you can manage credentials without using the dashboard UI.

Each request updates the push credentials for one app and one push platform. Credential files, such as the iOS authentication key or the Firebase service account, are passed as [Base64](https://en.wikipedia.org/wiki/Base64)-encoded strings inside the JSON request body.

This endpoint supports the following push platforms:

| Platform | Credentials |
|---|---|
| iOS (APNs) | `.p8` authentication key only. `.p12` and `.pem` certificates aren't supported by this endpoint. |
| Android (Firebase Cloud Messaging) | Service account JSON |
| Android (Huawei Mobile Services) | App ID and app secret |
| Kindle (Amazon Device Messaging) | Client ID and client secret |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported push platforms" }

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key) with the `apps.push_credential` permission.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Include one platform object per request: `apple`, `firebase`, `huawei`, or `kindle`.

{% tabs %}
{% tab iOS (APNs) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "apple": {
    "certificate": (required, string) the Base64-encoded .p8 authentication key,
    "jwt_key_id": (required, string) the key ID for the .p8 authentication key,
    "jwt_team_id": (required, string) your Apple Developer team ID,
    "jwt_bundle_id": (required, string) your app's bundle ID,
    "apns_gateway": (required, string) either "prod" or "dev"
  }
}
```
{% endtab %}
{% tab Android (Firebase Cloud Messaging) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "firebase": {
    "credential": (required, string) the Base64-encoded Firebase service account JSON
  }
}
```
{% endtab %}
{% tab Android (Huawei Mobile Services) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "huawei": {
    "app_id": (required, string) your Huawei app ID,
    "app_secret": (required, string) your Huawei app secret
  }
}
```
{% endtab %}
{% tab Kindle (Amazon Device Messaging) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "kindle": {
    "client_id": (required, string) your Amazon Device Messaging client ID,
    "client_secret": (required, string) your Amazon Device Messaging client secret
  }
}
```
{% endtab %}
{% endtabs %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| [`app_id`]({{site.baseurl}}/api/identifier_types#app-identifier) | Required | String | The app identifier API key for the app you want to update. Find it in the dashboard under **Settings** > **App Settings**, next to the **API Key** field. |
| `apple` | Required* | Object | The iOS (APNs) credentials. |
| `firebase` | Required* | Object | The Android (Firebase Cloud Messaging) credentials. |
| `huawei` | Required* | Object | The Android (Huawei Mobile Services) credentials. |
| `kindle` | Required* | Object | The Kindle (Amazon Device Messaging) credentials. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

\* Include exactly one platform object per request.

### iOS (APNs) parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `certificate` | Required | String | The Base64-encoded `.p8` authentication key. Only `.p8` authentication keys are supported; `.p12` and `.pem` certificates aren't supported by this endpoint. |
| `jwt_key_id` | Required | String | The key ID for the `.p8` authentication key. |
| `jwt_team_id` | Required | String | Your Apple Developer team ID. |
| `jwt_bundle_id` | Required | String | Your app's bundle ID. |
| `apns_gateway` | Required | String | The APNs environment. Available values are `prod` and `dev`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="iOS (APNs) parameters" }

### Android (Firebase Cloud Messaging) parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `credential` | Required | String | The Base64-encoded Firebase service account JSON. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Android (Firebase Cloud Messaging) parameters" }

### Android (Huawei Mobile Services) parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `app_id` | Required | String | Your Huawei app ID. |
| `app_secret` | Required | String | Your Huawei app secret. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Android (Huawei Mobile Services) parameters" }

### Kindle (Amazon Device Messaging) parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `client_id` | Required | String | Your Amazon Device Messaging client ID. |
| `client_secret` | Required | String | Your Amazon Device Messaging client secret. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Kindle (Amazon Device Messaging) parameters" }

## Example requests

### iOS (APNs)

The `apple.certificate` value must be Base64-encoded, and `apple.apns_gateway` must be set to either `prod` or `dev`.

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "apple": {
    "certificate": "{BASE64_ENCODED_STRING}",
    "jwt_key_id": "{YOUR_KEY_ID}",
    "jwt_team_id": "{YOUR_TEAM_ID}",
    "jwt_bundle_id": "{YOUR_BUNDLE_ID}",
    "apns_gateway": "prod"
  }
}'
```

### Android (Firebase Cloud Messaging)

The `firebase.credential` value must be Base64-encoded.

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "firebase": {
    "credential": "{BASE64_ENCODED_STRING}"
  }
}'
```

### Android (Huawei Mobile Services)

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "huawei": {
    "app_id": "{YOUR_HUAWEI_APP_ID}",
    "app_secret": "{YOUR_HUAWEI_APP_SECRET}"
  }
}'
```

### Kindle (Amazon Device Messaging)

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "kindle": {
    "client_id": "{YOUR_ADM_CLIENT_ID}",
    "client_secret": "{YOUR_ADM_CLIENT_SECRET}"
  }
}'
```

## Example response

If the credentials are updated successfully, you'll receive a response with the status code `201`.

```json
{
  "message": "success"
}
```

{% endapi %}
