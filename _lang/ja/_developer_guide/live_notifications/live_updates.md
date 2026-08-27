---
nav_title: Android向けライブ更新
article_title: Android Braze SDKのライブ更新
page_order: 0.3
description: "Braze SDKでAndroidライブ更新を使用する方法について説明します。"
platform:
  - Android
hidden: true
---

# Android向けライブ更新 {#live-updates-for-android}

> Braze SDKでAndroidライブ更新（[Progress Centric Notifications](https://developer.android.com/about/versions/16/features/progress-centric-notifications)とも呼ばれます）を使用する方法について説明します。これらの通知は[Swift Braze SDKのライブアクティビティ]({{site.baseurl}}/developer_guide/live_notifications/live_activities)に似ており、インタラクティブなロック画面通知を表示できます。Android 16では進行状況を中心とした通知が導入され、ユーザーが開始した最初から最後までのジャーニーをシームレスに追跡できるようになります。

## 仕組み {#how-it-works}

[`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) インターフェイスを使用して、Brazeプッシュ通知の表示方法をカスタマイズできます。`BrazeNotificationFactory` を拡張することで、通知がユーザーに表示される前にBrazeがファクトリの `createNotification()` メソッドを呼び出します。その際、Brazeダッシュボードまたは REST APIを通じて送信されたカスタムキーと値のペアを含むペイロードが渡されます。

## Live Updateの表示 {#displaying-a-live-update}

このセクションでは、野生動物救助チームが最も多くのフクロウを救えるかを競い合う新しいゲームショーの司会者、Superb Owlと連携します。彼らはAndroidアプリでLive Updatesを活用し、進行中の試合のステータスを表示して、通知をリアルタイムでダイナミックに更新したいと考えています。

![AndroidのLive Updateの例]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

{% multi_lang_include developer_guide/prerequisites/android.md %}

### ステップ1:カスタム通知ファクトリーを作成する {#step-1-create-a-custom-notification-factory}

アプリケーションで、[`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)を拡張した`MyCustomNotificationFactory.kt`という新しいファイルを作成し、Braze Live Updatesの表示方法を処理します。

次の例では、Superb Owlが進行中の試合のLive Updateを表示するためにカスタム通知ファクトリーを作成しました。次のステップでは、チームのデータをアクティビティにマッピングする`getTeamInfo`という新しいメソッドを作成します。

```kotlin
class MyCustomNotificationFactory : IBrazeNotificationFactory {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        val notificationBuilder = populateNotificationBuilder(payload)
        val context = payload.context ?: return null

        if (notificationBuilder == null) {
            brazelog { "Notification could not be built. Returning null as created notification." }
            return null
        }
        notificationBuilder.setContentTitle("Android Live Updates").setContentText("Ongoing updates below")
        setProgressStyle(notificationBuilder, context)
        return notificationBuilder.build()
    }

    private fun setProgressStyle(notificationBuilder: NotificationCompat.Builder, context: Context) {
        val style = NotificationCompat.ProgressStyle()
            .setStyledByProgress(false)
            .setProgress(200)
            .setProgressTrackerIcon(IconCompat.createWithResource(context, R.drawable.notification_small_icon))
            .setProgressSegments(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Segment(1000).setColor(Color.GRAY),
                    NotificationCompat.ProgressStyle.Segment(200).setColor(Color.BLUE),
                )
            )
            .setProgressPoints(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Point(60).setColor(Color.RED),
                    NotificationCompat.ProgressStyle.Point(560).setColor(Color.GREEN)
                )
            )

        notificationBuilder.setStyle(style)
    }
}
```

### ステップ2:カスタムデータをマッピングする {#step-2-map-custom-data}

`MyCustomNotificationFactory.kt`で、Live Updateが表示される際のデータ処理用の新しいメソッドを作成します。

Superb Owlは、各チームの名前とロゴを展開されたLive Updateにマッピングするために以下のメソッドを作成しました:

```kotlin
class CustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Your existing code
        return super.createNotification(payload)
    }

    // Your new method
    private fun getTeamInfo(team: String?): Pair<String, Int> {
        return when (team) {
            "WBF" -> Pair("Wild Bird Fund", R.drawable.team_wbf)
            "OWL" -> Pair("Owl Rehab", R.drawable.team_owl)
            else  -> Pair("Unknown", R.drawable.notification_small_icon)
        }
    }
}
```

### ステップ3:カスタム通知ファクトリーを設定する {#step-3-set-the-custom-notification-factory}

アプリケーションクラスで、[`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)を使用して、カスタム通知ファクトリーを設定します。

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### ステップ4:アクティビティを送信する {#step-4-send-the-activity}

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST APIエンドポイントを使用して、ユーザーのAndroidデバイスにプッシュ通知を送信できます。

#### curlコマンドの例 {#example-curl-command}

Superb Owlは以下のcurlコマンドを使用してリクエストを送信しました:

```
curl -X POST "https://BRAZE_REST_ENDPOINT/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["USER_ID"],
    "messages": {
      "android_push": {
        "title": "WBF vs OWL",
        "alert": "2 to 4 1:33 Q4",
        "extra": {
          "live_update": "true",
          "team1": "WBF",
          "team2": "OWL",
          "score1": "2",
          "score2": "4",
          "time": "1:33",
          "quarter": "Q4"
        },
        "notification_id": "ASSIGNED_NOTIFICATION_ID"
      }
    }
  }'
```

{% alert tip %}
curlコマンドはテストに便利ですが、すでに[iOS Live Activities]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?sdktab=swift)を処理しているバックエンドでこの呼び出しを処理することをお勧めします。
{% endalert %}

#### リクエストパラメーター {#request-parameters}

| キー | 説明 |
|------------------------------|------------|
| `REST_API_KEY` | `messages.send`権限を持つBraze REST APIキーです。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| `BRAZE_REST_ENDPOINT` | REST エンドポイントURLです。エンドポイントは[お使いのインスタンスのBraze URL]({{site.baseurl}}/api/basics#endpoints)に依存します。 |
| `USER_ID` | 通知を送信するユーザーのIDです。 |
| `messages.android_push.title` | メッセージのタイトルです。デフォルトでは、カスタム通知ファクトリーのライブ通知には使用されませんが、フォールバックとして使用される場合があります。 |
| `messages.android_push.alert` | メッセージの本文です。デフォルトでは、カスタム通知ファクトリーのライブ通知には使用されませんが、フォールバックとして使用される場合があります。 |
| `messages.extra` | カスタム通知ファクトリーがライブ通知に使用するキーと値のペアです。この値には任意の文字列を割り当てることができますが、[curlコマンドの例](#example-curl-command)では、`live_updates`を使用してデフォルトのプッシュ通知かライブプッシュ通知かを判別しています。 |
| `ASSIGNED_NOTIFICATION_ID` | 選択したユーザーのライブ通知に割り当てる通知IDです。このIDはこのゲームに固有でなければならず、後で[既存の通知を更新する](#android_step-4-update-data-with-the-braze-rest-api)ために使用する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="リクエストパラメーター" }

### ステップ5:アクティビティを更新する {#step-5-update-the-activity}

既存のLive Updateを新しいデータで更新するには、`messages.extra`に割り当てられた関連するキーと値のペアを変更し、同じ`notification_id`を使用して`/messages/send`エンドポイントを再度呼び出します。