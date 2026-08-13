---
nav_title: "POST: SDK認証キーを作成する"
article_title: "POST: SDK認証キーを作成"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "この記事では、「SDK認証キーを作成」Brazeエンドポイントの詳細について説明します。"
---

{% api %}
# SDK認証キーを作成 {#create-sdk-authentication-key}
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> このエンドポイントを使用して、アプリ用の新しいSDK認証キーを作成します。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`sdk_authentication.create` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API identifier",
  "rsa_public_key_str": "RSA public key string",
  "description": "description",
  "make_primary": false
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 必須 | 文字列 | アプリのAPI識別子。 |
| `rsa_public_key_str` | 必須 | 文字列 | RSA公開キーの文字列。有効なRSA公開キーでなければならず、そうでない場合はエラーを返します。 |
| `description` | 必須 | 文字列 | SDK認証キーの説明。 |
| `make_primary` | オプション | ブール値 | `true` に設定すると、作成時にこのキーがプライマリSDK認証キーになります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
  "description": "SDK Authentication Key for iOS App",
  "make_primary": false
}'
```

## レスポンス {#response}
```json
{
  "id": "key id"
}
```

## レスポンスパラメーター {#response-parameters}

| パラメーター | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `id` | 文字列 | 新しく作成されたSDK認証キーのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスパラメーター" }

### バリデーションルール {#validation-rules}

このエンドポイントには以下のバリデーションルールがあります。

- 1つのアプリにつきSDK認証キーは最大3つまで保持できます。
- RSA公開キー文字列は、適切な形式の有効なRSA公開キーでなければなりません。
- `app_id` は有効なアプリAPI識別子でなければなりません。
- 説明を空にすることはできません。

{% endapi %}