---
nav_title: "PUT: プライマリSDK認証キーを設定する"
article_title: "PUT: プライマリSDK認証キーを設定する"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、「プライマリSDK認証キーを設定する」Brazeエンドポイントの詳細について説明します。"
---

{% api %}
# プライマリSDK認証キーを設定する {#set-primary-sdk-authentication-key}
{% apimethod put %}
/app_group/sdk_authentication/primary
{% endapimethod %}

> このエンドポイントを使用して、SDK認証キーをアプリのプライマリキーとして設定します。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`sdk_authentication.primary` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

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
  "key_id": "key id"
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 必須 | 文字列 | アプリのAPI識別子。 |
| `key_id` | 必須 | 文字列 | プライマリとしてマークするSDK認証キーのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}
`````````bash
curl --location --request PUT 'https://rest.iad-01.braze.com/app_group/sdk_authentication/primary' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "abcdef12-3456-7890-abcd-ef1234567890"
}'
```

## 応答 {#response}
```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    },
    {
      "id": "fedcba98-7654-3210-fedc-ba9876543210",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nqWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for Android App",
      "is_primary": false
    }
  ]
}
```

## 応答パラメーター {#response-parameters}

| パラメーター | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `keys` | 配列 | すべてのSDK認証キーオブジェクトの配列。 |
| `keys[].id` | 文字列 | SDK認証キーのID。 |
| `keys[].rsa_public_key` | 文字列 | RSA公開キーの文字列。 |
| `keys[].description` | 文字列 | SDK認証キーの説明。 |
| `keys[].is_primary` | ブール値 | このキーがプライマリSDK認証キーであるかどうか。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response parameters" }

### バリデーションルール {#validation-rules}

このエンドポイントには以下のバリデーションルールがあります。

- `key_id` は有効なSDK認証キーIDである必要があります。
- `app_id` は有効なアプリAPI識別子である必要があります。
- SDK認証キーは、指定されたアプリに存在している必要があります。

{% endapi %}