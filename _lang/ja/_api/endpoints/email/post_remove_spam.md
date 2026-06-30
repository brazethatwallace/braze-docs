---
nav_title: "POST:スパムリストからメールアドレスを削除する"
article_title: "POST:スパムリストからメールアドレスを削除する"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "この記事では、スパムリストからメールアドレスを削除するBrazeエンドポイントについて詳しく説明します。"

---
{% api %}
# スパムリストからメールアドレスを削除する {#remove-email-addresses-from-spam-list}
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> このエンドポイントを使用して、Brazeのスパムリストおよびメールプロバイダーが管理するスパムリストからメールアドレスを削除します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`email.spam.remove` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストボディ {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@example.com"
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ----------|-----------| --------|------- |
| `email` | 必須 | 文字列または配列 | 変更するメールアドレスの文字列、または最大50件のメールアドレスの配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@example.com"
}'
```
{% endapi %}