---
nav_title: "POST: ライブアクティビティを更新"
article_title: "POST: ライブアクティビティを更新"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、ライブアクティビティを更新するエンドポイントについて詳しく説明します。"

---
{% api %}
# ライブアクティビティを更新 {#update-live-activity}
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> このエンドポイントを使用して、iOSアプリが表示する[ライブアクティビティ]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?sdktab=swift)を更新および終了します。このエンドポイントには追加のセットアップが必要です。

ライブアクティビティを登録した後、Apple Push Notification service（APNs）を更新するためにJSONペイロードを渡すことができます。詳しくは、[プッシュ通知ペイロードを使ったライブアクティビティの更新](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications)に関するAppleのドキュメントを参照してください。

`content-available`が設定されていない場合、Apple Push Notification service（APNs）のデフォルトの優先度は10です。`content-available`が設定されている場合、この優先度は5になります。詳細は[Appleプッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object)を参照してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、以下を完了する必要があります。

- `messages.live_activity.update`権限を持つAPIキーを生成します。
- Braze Swift SDKを使用して、[リモート]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?tab=remote&sdktab=swift)または[ローカル]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?tab=local&sdktab=swift)でライブアクティビティを登録します。

{% multi_lang_include api/payload_size_alert.md %}

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```json
{
   "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
   "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
   "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
   "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
   "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
   "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
   "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
 }
 ```

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `app_id` | Required | String | App [API identifier]({{site.baseurl}}/api/identifier_types#the-app-identifier) retrieved from the [API Keys]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) page.  |
| `activity_id` | Required | String | When you register your Live Activity using [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class), you use the `pushTokenTag` parameter to name the Activity's push token to a custom string.<br><br>Set `activity_id` to this custom string to define which Live Activity you want to update. |
| `content_state` | Required | Object | You define the `ContentState` parameters when you create your Live Activity. Pass the updated values for your `ContentState` using this object.<br><br>The format of this request must match the shape you initially defined. |
| `end_activity` | Optional | Boolean | If `true`, this request ends the Live Activity. |
| `dismissal_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter defines the time to remove the Live Activity from the user's UI. If this time is in the past and `end_activity` is `true`, the Live Activity will be removed immediately.<br><br> If `end_activity` is `false` or omitted, this parameter only updates the Live Activity.|
| `stale_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter tells the system when the Live Activity content is marked as outdated in the user's UI. |
| `notification` | Optional | Object | Include an [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object) object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. {::nomarkdown}<ul><li>If a <code>notification</code> is included and the user is active on their iPhone when the update is delivered, the updated Live Activity UI will slide down and display like a push notification.</li><li>If a <code>notification</code> is included and the user is not active on their iPhone, their screen will light up to display the updated Live Activity UI on their lock screen.</li><li>The <code>notification alert</code> will not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the <code>alert</code> will be displayed there.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Example request

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It's halftime! Let's look at the scores",
            "title": "Halftime"
        }
    }
}'
```

## 応答 {#response}

このエンドポイントには`201`と`4XX`の2つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

リクエストが正しくフォーマットされ、受信された場合、`201`ステータスコードが返されます。ステータスコード`201`は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例 {#example-error-response}

`4XX`クラスのステータスコードはクライアントエラーを示します。発生する可能性のあるエラーの詳細については、[APIエラーと応答の記事]({{site.baseurl}}/api/errors)を参照してください。

ステータスコード`400`は、次の応答本文を返す可能性があります。

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}