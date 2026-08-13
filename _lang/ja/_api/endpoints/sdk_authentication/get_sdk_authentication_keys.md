---
nav_title: "GET: SDK認証キーの一覧"
article_title: "GET: SDK認証キーの一覧"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「SDK認証キーの一覧」Brazeエンドポイントの詳細について説明します。"
---

{% api %}
# SDK認証キーの一覧 {#list-sdk-authentication-keys}
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> このエンドポイントを使用して、アプリのすべてのSDK認証キーを取得します。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`sdk_authentication.keys` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 必須 | 文字列 | アプリのAPI識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス {#response}

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

## レスポンスパラメーター {#response-parameters}

| パラメーター | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `keys` | 配列 | SDK認証キーオブジェクトの配列。 |
| `keys[].id` | 文字列 | SDK認証キーのID。 |
| `keys[].rsa_public_key` | 文字列 | RSA公開キーの文字列。 |
| `keys[].description` | 文字列 | SDK認証キーの説明。 |
| `keys[].is_primary` | ブール値 | このキーがプライマリSDK認証キーであるかどうか。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスパラメーター" }

### バリデーションルール {#validation-rules}

このエンドポイントには以下のバリデーションルールがあります。

- `app_id` パラメーターは有効なアプリAPI識別子である必要があります。
- アプリはワークスペースに存在している必要があります。

{% endapi %}