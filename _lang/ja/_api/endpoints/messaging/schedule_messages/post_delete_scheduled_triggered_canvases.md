---
nav_title: "POST:スケジュールされたAPIトリガーキャンバスを削除"
article_title: "POST:スケジュールされたAPIトリガーキャンバスを削除"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「スケジュールされたAPIトリガーキャンバスを削除」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされたAPIトリガーキャンバスを削除 {#delete-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> 「スケジュールを削除」エンドポイントを使用すると、以前にスケジュールしたAPIトリガーキャンバスのメッセージを、送信前にキャンセルできます。

スケジュールされたメッセージやトリガーが、送信予定時刻の間近またはその最中に削除された場合、ベストエフォートで更新されます。そのため、Brazeは対象ユーザーの全員、一部、またはゼロ人に対して直前の削除を適用する可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`canvas.trigger.schedule.delete` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `canvas_id`| 必須 | 文字列 | [Canvas識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `schedule_id` | 必須 | 文字列 | 削除する`schedule_id`（スケジュール作成のレスポンスから取得）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }


## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}