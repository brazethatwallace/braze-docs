---
nav_title: "DELETE: SDK認証キーを削除する"
article_title: "DELETE: SDK認証キーを削除"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、「SDK認証キーを削除」Brazeエンドポイントの詳細について説明します。"
---

{% api %}
# SDK認証キーを削除 {#delete-sdk-authentication-key}
{% apimethod delete %}
/app_group/sdk_authentication/delete
{% endapimethod %}

> このエンドポイントを使用して、アプリのSDK認証キーを削除します。

{% alert important %}
プライマリキーは削除できません。プライマリキーを削除しようとすると、このエンドポイントはエラーを返します。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`sdk_authentication.delete` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API Identifier",
  "key_id": "key id"
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 必須 | 文字列 | アプリのAPI識別子。 |
| `key_id` | 必須 | 文字列 | 削除するSDK認証キーのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}

`````````bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
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
    }
  ]
}
```

## 応答パラメーター {#response-parameters}

| パラメーター | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `keys` | 配列 | 残りのSDK認証キーオブジェクトの配列。 |
| `keys[].id` | 文字列 | SDK認証キーのID。 |
| `keys[].rsa_public_key` | 文字列 | RSA公開キーの文字列。 |
| `keys[].description` | 文字列 | SDK認証キーの説明。 |
| `keys[].is_primary` | ブール値 | このキーがプライマリSDK認証キーであるかどうか。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response parameters" }

### バリデーションルール {#validation-rules}

このエンドポイントには以下のバリデーションルールがあります。

- `key_id` は有効なSDK認証キーIDである必要があります。
- `app_id` は有効なアプリAPI識別子である必要があります。
- SDK認証キーは、指定されたアプリに存在する必要があります。
- プライマリSDK認証キーは削除できません。

{% endapi %}