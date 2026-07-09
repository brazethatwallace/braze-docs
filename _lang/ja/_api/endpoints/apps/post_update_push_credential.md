---
nav_title: "POST: プッシュ認証情報の更新"
article_title: "POST: プッシュ認証情報の更新"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、プッシュ認証情報の更新 Braze エンドポイントについて詳しく説明します。"
---

{% api %}
# プッシュ認証情報の更新 {#update-push-credentials}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/apps/push_credential/update
{% endapimethod %}

> このエンドポイントを使用して、単一アプリのプッシュ認証情報をプログラムで更新できます。これにより、ダッシュボードUIを使用せずに認証情報を管理できます。

各リクエストは、1つのアプリと1つのプッシュプラットフォームのプッシュ認証情報を更新します。iOS認証キーやFirebaseサービスアカウントなどの認証情報ファイルは、JSONリクエストボディ内で [Base64](https://en.wikipedia.org/wiki/Base64) エンコードされた文字列として渡されます。

このエンドポイントは以下のプッシュプラットフォームをサポートしています。

| プラットフォーム | 認証情報 |
|---|---|
| iOS (APNs) | `.p8` 認証キーのみ。`.p12` および `.pem` 証明書はこのエンドポイントではサポートされていません。 |
| Android (Firebase Cloud Messaging) | サービスアカウントJSON |
| Android (Huawei Mobile Services) | アプリIDとアプリシークレット |
| Kindle (Amazon Device Messaging) | クライアントIDとクライアントシークレット |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サポートされているプッシュプラットフォーム" }

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`apps.push_credential` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## リクエストボディ {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

リクエストごとに1つのプラットフォームオブジェクト（`apple`、`firebase`、`huawei`、または `kindle`）を含めてください。

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

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| [`app_id`]({{site.baseurl}}/api/identifier_types#app-identifier) | 必須 | String | 更新するアプリのアプリ識別子APIキー。ダッシュボードの**設定** > **アプリ設定**で、**APIキー**フィールドの横に表示されます。 |
| `apple` | 必須* | Object | iOS (APNs) の認証情報。 |
| `firebase` | 必須* | Object | Android (Firebase Cloud Messaging) の認証情報。 |
| `huawei` | 必須* | Object | Android (Huawei Mobile Services) の認証情報。 |
| `kindle` | 必須* | Object | Kindle (Amazon Device Messaging) の認証情報。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

\* リクエストごとにプラットフォームオブジェクトを1つだけ含めてください。

### iOS (APNs) パラメーター {#ios-apns-parameters}

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `certificate` | 必須 | String | Base64エンコードされた `.p8` 認証キー。`.p8` 認証キーのみサポートされています。`.p12` および `.pem` 証明書はこのエンドポイントではサポートされていません。 |
| `jwt_key_id` | 必須 | String | `.p8` 認証キーのキーID。 |
| `jwt_team_id` | 必須 | String | Apple DeveloperチームID。 |
| `jwt_bundle_id` | 必須 | String | アプリのバンドルID。 |
| `apns_gateway` | 必須 | String | APNs環境。使用可能な値は `prod` と `dev` です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="iOS (APNs) パラメーター" }

### Android (Firebase Cloud Messaging) パラメーター {#android-firebase-cloud-messaging-parameters}

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `credential` | 必須 | String | Base64エンコードされたFirebaseサービスアカウントJSON。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Android (Firebase Cloud Messaging) パラメーター" }

### Android (Huawei Mobile Services) パラメーター {#android-huawei-mobile-services-parameters}

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `app_id` | 必須 | String | HuaweiアプリID。 |
| `app_secret` | 必須 | String | Huaweiアプリシークレット。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Android (Huawei Mobile Services) パラメーター" }

### Kindle (Amazon Device Messaging) パラメーター {#kindle-amazon-device-messaging-parameters}

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `client_id` | 必須 | String | Amazon Device MessagingクライアントID。 |
| `client_secret` | 必須 | String | Amazon Device Messagingクライアントシークレット。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Kindle (Amazon Device Messaging) パラメーター" }

## リクエスト例 {#example-requests}

### iOS (APNs)

`apple.certificate` の値はBase64エンコードされている必要があり、`apple.apns_gateway` は `prod` または `dev` に設定する必要があります。

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

`firebase.credential` の値はBase64エンコードされている必要があります。

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

## レスポンス例 {#example-response}

認証情報が正常に更新された場合、ステータスコード `201` のレスポンスが返されます。

```json
{
  "message": "success"
}
```

{% endapi %}