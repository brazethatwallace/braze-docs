---
nav_title: "POST: APIトリガーキャンペーンのスケジュール"
article_title: "POST: APIトリガーキャンペーンのスケジュール"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「APIトリガーキャンペーンのスケジュール」Brazeエンドポイントについての詳細を概説します。"

---
{% api %}
# APIトリガーキャンペーンのスケジュール {#schedule-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/schedule/create
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成したキャンペーンメッセージをAPIトリガー配信で送信します。これにより、メッセージの送信をトリガーするアクションを決めることができます。

メッセージ自体にテンプレート化される `trigger_properties` を渡すことができます。

このエンドポイントを使用してメッセージを送信するには、[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)を構築する際に作成した[キャンペーンID]({{site.baseurl}}/api/identifier_types)が必要です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`campaigns.trigger.schedule.create` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' %}

## リクエストボディ {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the campaign
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 必須 | 文字列 | [キャンペーン識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| `send_id` | オプション | 文字列 | [送信識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| `recipients` | オプション | 受信者オブジェクトの配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)を参照してください。 |
| `audience` | オプション | 接続オーディエンスオブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience)を参照してください。 |
| `broadcast` | オプション | ブール値 | キャンペーンまたはキャンバスが対象とするセグメント全体にメッセージを送信する場合は、`broadcast` を true に設定する必要があります。このパラメーターはデフォルトで false です（2017年8月31日現在）。<br><br> `broadcast` が true に設定されている場合、`recipients` リストを含めることはできません。ただし、`broadcast: true` を設定する場合は注意が必要です。意図せずにこのフラグを設定すると、想定よりも大きなオーディエンスにメッセージが送信される可能性があります。 |
| `trigger_properties` | オプション | オブジェクト | この送信に含まれるすべてのユーザーのパーソナライゼーションキーと値のペア。[トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object)を参照してください。 |
| `schedule` | 必須 | スケジュールオブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "trigger_properties": {}
    }
  ],
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "broadcast": false,
  "trigger_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## 応答 {#response}

### 成功応答の例 {#example-success-response}

```json
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}