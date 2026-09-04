---
nav_title: "POST: スケジュールされたAPIトリガーキャンバスを更新する"
article_title: "POST: スケジュールされたAPIトリガーキャンバスを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「スケジュールされたAPIトリガーキャンバスを更新」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされたAPIトリガーキャンバスを更新する {#update-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成されたスケジュール済みAPIトリガーキャンバスを更新します。

これにより、どのアクションがメッセージ送信のトリガーになるかを決めることができます。Brazeがメッセージ自体にテンプレート化する`trigger_properties`を渡すことができます。

このエンドポイントを使用してメッセージを送信するには、[キャンバス]({{site.baseurl}}/api/identifier_types#canvas-identifier)を構築するときに作成されたキャンバスIDが必要です。

スケジュールは、スケジュール作成リクエストや以前のスケジュール更新リクエストで提供したものを完全に上書きします。
  - たとえば、最初に`"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}`を指定し、更新で`"schedule" : {"time" : "2015-02-20T14:14:47"}`を指定した場合、Brazeはユーザーのローカル時間ではなく、UTCで指定した時間にメッセージを送信します。
  - 送信予定時刻に近い、または送信予定時刻中に更新されたスケジュール済みトリガーはベストエフォートで更新されるため、Brazeはターゲットユーザーの全員、一部、またはいずれにも直前の変更を適用する可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`canvas.trigger.schedule.update`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [キャンバス識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| `schedule_id` | オプション | 文字列 | 更新する`schedule_id`（スケジュール作成のレスポンスから取得）。 |
| `schedule` | 必須 | オブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}