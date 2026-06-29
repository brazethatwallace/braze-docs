---
nav_title: "POST:スケジュールされたメッセージを更新する"
article_title: "POST:スケジュールされたメッセージを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「スケジュールされたメッセージの更新」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされたメッセージを更新する {#update-scheduled-messages}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/messages/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、スケジュールされたメッセージを更新します。

このエンドポイントは、`schedule` または `messages` パラメーターのいずれか、あるいはその両方に対する更新を受け入れます。リクエストには、これら2つのキーのうち、少なくとも1つが含まれている必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`messages.schedule.update` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see available messaging objects documentation
  }
}
```
## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | 必須 | 文字列 | 更新する `schedule_id`（スケジュール作成のレスポンスから取得）。 |
| `schedule` | オプション | オブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object)を参照してください。 |
| `messages` | オプション | オブジェクト | [利用可能なメッセージングオブジェクト]({{site.baseurl}}/api/objects_filters#messaging-objects)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
    "apple_push": {
      "alert": "Updated Message!",
      "badge": 1
    },
    "android_push": {
      "title": "Updated title!",
      "alert": "Updated message!"
    },
    "sms": {
      "subscription_group_id": "subscription_group_identifier",
      "message_variation_id": "message_variation_identifier",
      "body": "This is my SMS body.",
      "app_id": "app_identifier"
    }
  }
}'
```

{% endapi %}