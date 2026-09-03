---
nav_title: "POST: スケジュールされたメッセージを削除する"
article_title: "POST: スケジュールされたメッセージを削除する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、スケジュールされたメッセージを削除するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされたメッセージを削除する {#delete-scheduled-messages}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/messages/schedule/delete
{% endapimethod %}

> このエンドポイントを使用して、以前にスケジュールしたメッセージを送信前にキャンセルできます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`messages.schedule.delete` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | 必須 | 文字列 | 削除する `schedule_id`（スケジュール作成のレスポンスから取得）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}