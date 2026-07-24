---
nav_title: "POST: メールのブロックリスト登録"
article_title: "POST: メールのブロックリスト登録"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "この記事では、メールのブロックリスト登録Brazeエンドポイントに関する詳細を説明します。"

---
{% api %}
# メールのブロックリスト登録 {#blocklist-emails}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> このエンドポイントを使用して、ユーザーのメール購読解除を行い、ハードバウンスとしてマークします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`email.blacklist` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blocklist_email1","blocklist_email2"]
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| -----------|----------| --------|------- |
| `email` | 必須 | 文字列または配列 | ブロックリストに追加するメールアドレスの文字列、またはブロックリストに追加する最大50件のメールアドレスの配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}