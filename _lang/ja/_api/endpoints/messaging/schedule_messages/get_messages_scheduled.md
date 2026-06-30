---
nav_title: "GET: スケジュールされた今後のキャンペーンとキャンバスを一覧表示する"
article_title: "GET: スケジュールされた今後のキャンペーンとキャンバスを一覧表示する"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "この記事では、「スケジュールされた今後のキャンペーンとキャンバスを一覧表示する」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされた今後のキャンペーンとキャンバスを一覧表示する {#list-upcoming-scheduled-campaigns-and-canvases}
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> このエンドポイントを使用して、現在からリクエストで指定された `end_time` までのスケジュールされたキャンペーンとエントリキャンバスに関する情報のJSONリストを返します。

毎日繰り返されるメッセージは、次回の発生時に1回だけ表示されます。このエンドポイントで返される結果には、Brazeダッシュボードで作成およびスケジュールされたキャンペーンとキャンバスが含まれます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`messages.schedule_broadcasts` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `end_time` | 必須 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列 | スケジュールされた今後のキャンペーンとキャンバスを取得する範囲の終了日。これはAPIによってUTC時間の午前0時として扱われます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

```json
{
  "scheduled_broadcasts": [
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone
    }
  ]
}
```

{% endapi %}