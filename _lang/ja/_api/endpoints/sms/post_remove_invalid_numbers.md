---
nav_title: "POST:無効な電話番号を削除する"
article_title: "POST:無効な電話番号を削除する"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、無効な電話番号を削除するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# 無効な電話番号を削除する {#remove-invalid-phone-numbers}
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> このエンドポイントを使用して、「無効な」電話番号を無効リストから削除します。

これを使用して、無効とマークされた電話番号を再検証できます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`sms.invalid_phone_numbers.remove` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ----------|-----------| ---------|------ |
| `phone_number` | 必須 | e.164 形式の文字列の配列 | 変更する最大50件の電話番号の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}