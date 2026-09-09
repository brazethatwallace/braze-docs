---
nav_title: "POST:ライブアクティビティを開始"
article_title: "POST:ライブアクティビティを開始"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「ライブアクティビティを開始」エンドポイントの詳細について説明します。"

---
{% api %}
# ライブアクティビティを開始 {#start-live-activity}
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> このエンドポイントを使用して、iOSアプリに表示される[ライブアクティビティ]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift)をリモートで開始します。このエンドポイントには追加の設定が必要です。

ライブアクティビティを作成した後、セグメント、接続オーディエンス、または特定のユーザーをターゲットにするPOSTリクエストを送信します。特定のユーザーは、外部ユーザーID、ユーザーエイリアス、またはその両方で識別します。Appleのライブアクティビティの詳細については、[Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications)を参照してください。

`content-available` が設定されていない場合、Appleプッシュ通知サービス（APNs）のデフォルトの優先度は10です。`content-available` が設定されている場合、この優先度は5です。詳細については、[Appleプッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object)を参照してください。

{% alert tip %}
ライブアクティビティを終了するには、[`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)エンドポイントで `end_activity` を `true` に設定して使用します。
{% endalert %}

## 自動非表示の設定 {#arranging-automatic-dismissal}

ライブアクティビティの開始後に自動非表示を設定するには、バックエンドから更新エンドポイントへのフォローアップリクエストをスケジュールします。

1. 後で再利用できる `activity_id` を含む `/messages/live_activity/start` リクエストを送信します。
2. その `activity_id` とターゲット終了時間をバックエンドスケジューラーに保存します。
3. ターゲット終了時間に、`end_activity` を `true` に設定した `/messages/live_activity/update` リクエストを送信します。
4. 同じ更新リクエストで非表示の動作を設定します。詳細については、[`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)エンドポイントを参照してください。
5. [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)で送信イベントと結果イベントを確認します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、以下の前提条件を満たしてください。

- `messages.live_activity.start` 権限を持つAPIキーを生成します。
- Braze Swift SDKを使用して[ライブアクティビティを作成]({{site.baseurl}}/developer_guide/live_notifications/live_activities?tab=local&sdktab=swift#create-an-activity)します。

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
特定のユーザーをターゲットにする場合、Brazeは既存のユーザーに解決される `external_user_ids` および `user_aliases` に対してのみライブアクティビティを開始します。
{% endalert %}

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. Use this ID to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app.",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Include `notification.alert.title` and `notification.alert.body`.",
  // Include one targeting method:
  // 1. "external_user_ids", "user_aliases", or both (combined maximum 50)
  // 2. "custom_audience"
  // 3. "segment_id"
  "external_user_ids": "(optional, array of strings) see external user identifier",
  "user_aliases": "(optional, array of user alias objects) see user alias object",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|-----------|----------|----------|--------------|
| `app_id` | 必須 | 文字列 | [APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)ページから取得したアプリ[API識別子]({{site.baseurl}}/api/identifier_types#app-identifier)。 |
| `activity_id` | 必須 | 文字列 | カスタム文字列を `activity_id` として定義します。このIDは、ライブアクティビティに更新または終了イベントを送信する際に使用します。 |
| `activity_attributes_type` | 必須 | 文字列 | アプリ内の `liveActivities.registerPushToStart` で定義するアクティビティ属性タイプ。 |
| `activity_attributes` | 必須 | オブジェクト | アクティビティタイプの静的属性値（スポーツチームの名前など、変更されないもの）。 |
| `content_state` | 必須 | オブジェクト | ライブアクティビティを作成する際に `ContentState` パラメーターを定義します。このオブジェクトを使用して、`ContentState` の更新された値を渡します。<br><br>このリクエストの形式は、最初に定義した形状と一致している必要があります。 |
| `stale_date` | オプション | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | このパラメーターは、ライブアクティビティのコンテンツがユーザーのUIで古いものとしてマークされる時間をシステムに通知します。 |
| `notification` | 必須 | オブジェクト | プッシュ通知を定義する[`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object)オブジェクトを含めます。このプッシュ通知の動作は、ユーザーがアクティブかどうか、またはユーザーがプロキシデバイスを使用しているかどうかによって異なります。{::nomarkdown}<ul><li><code>notification</code> が含まれており、更新が配信されたときにユーザーがiPhoneでアクティブである場合、更新されたライブアクティビティUIがスライドダウンしてプッシュ通知のように表示されます。</li><li><code>notification</code> が含まれており、ユーザーがiPhoneでアクティブでない場合、ロック画面に更新されたライブアクティビティUIを表示するために画面が点灯します。</li><li><code>notification alert</code> は、標準のプッシュ通知として表示されません。さらに、ユーザーがApple Watchのようなプロキシデバイスを持っている場合、<code>alert</code> がそこに表示されます。</li></ul>{:/} |
| `external_user_ids` | `user_aliases`、`segment_id`、または `custom_audience` が提供されている場合はオプション | 文字列の配列 | [外部ユーザーID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)を参照してください。 |
| `user_aliases` | `external_user_ids`、`segment_id`、または `custom_audience` が提供されている場合はオプション | ユーザーエイリアスオブジェクトの配列 | [ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object)を参照してください。 |
| `segment_id` | `external_user_ids`、`user_aliases`、または `custom_audience` が提供されている場合はオプション | 文字列 | [セグメント識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| `custom_audience` | `external_user_ids`、`user_aliases`、または `segment_id` が提供されている場合はオプション | 接続オーディエンスオブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

同じリクエストに `external_user_ids` と `user_aliases` を含めることができます。結合された配列の長さは50を超えることはできません。Brazeはいずれかのパラメーターに一致するユーザーをターゲットにし、複数の識別子が同じユーザーに解決される場合は1回だけ送信します。

`external_user_ids` または `user_aliases` を `segment_id` や `custom_audience` と組み合わせないでください。このエンドポイントでは、`custom_audience` を使用して接続オーディエンスフィルターを渡します。

## リクエスト例 {#example-request}

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR_REST_API_KEY}' \
--data-raw '{
  "app_id": "{YOUR_APP_API_IDENTIFIER}",
  "activity_id": "football-chiefs-bills-2024-01-21",
  "content_state": {
    "teamOneScore": 0,
    "teamTwoScore": 0
  },
  "activity_attributes_type": "FootballActivity",
  "activity_attributes": {
    "team1Name": "Chiefs",
    "team2Name": "Bills"
  },
  "stale_date": "2024-01-22T16:55:49+0000",
  "notification": {
    "alert": {
      "body": "The game is starting! Tune in soon!",
      "title": "Chiefs v. Bills"
    }
  },
  "external_user_ids": ["user-id1", "user-id2"],
  "user_aliases": [
    {
      "alias_name": "user-name",
      "alias_label": "user-label"
    }
  ]
}'
```

## レスポンス {#response}

このエンドポイントには `201` と `4XX` の2つのステータスコードレスポンスがあります。

### 成功レスポンスの例 {#example-success-response}

リクエストが正しくフォーマットされ、Brazeが受信した場合、`201` ステータスコードが返されます。ステータスコード `201` は、次のレスポンス本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラーレスポンスの例 {#example-error-response}

`4XX` クラスのステータスコードはクライアントエラーを示します。発生する可能性のあるエラーの詳細については、[APIエラーとレスポンスの記事]({{site.baseurl}}/api/errors)を参照してください。

ステータスコード `400` は、次のレスポンス本文を返す可能性があります。

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}