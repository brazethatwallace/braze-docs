{% multi_lang_include developer_guide/prerequisites/android.md %} また、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)も必要です。

## カスタム通知レイアウト {#custom-notification-layout}

Brazeの通知は[データメッセージ](https://firebase.google.com/docs/cloud-messaging/concept-options)として送信されます。つまり、アプリがバックグラウンドにある場合でも、アプリケーションは常に応答して適切な動作を実行する機会を持ちます（アプリがバックグラウンドにあるときにシステムによって自動的に処理される通知メッセージとは対照的です）。そのため、通知トレイに配信される通知内にパーソナライズされたUI要素を表示するなど、アプリケーションでエクスペリエンスをカスタマイズできます。この方法でプッシュを実装することに慣れていない方もいるかもしれませんが、Brazeでよく知られている機能の1つである[Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories)は、カスタムビューコンポーネントを使用して魅力的なエクスペリエンスを生み出す代表的な例です。

{% alert important %}
Androidでは、カスタム通知ビューを実装するために使用できるコンポーネントにいくつかの制限があります。通知ビューレイアウトには、[RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews)フレームワークと互換性のあるViewオブジェクト_のみ_を含める必要があります。
{% endalert %}

[`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)インターフェイスを使用して、Brazeプッシュ通知の表示方法をカスタマイズできます。`BrazeNotificationFactory`を拡張することで、通知がユーザーに表示される前にBrazeがファクトリーの`createNotification()`メソッドを呼び出します。その後、BrazeダッシュボードまたはREST APIを通じて送信されたカスタムのキーと値のペアを含むペイロードが渡されます。

このセクションでは、野生動物救助チームが誰が一番多くのフクロウを救えるかを競う新しいゲーム番組のホスト、Superb Owlとパートナーを組みます。彼らはAndroidアプリでライブ更新通知を活用し、進行中の試合のステータスを表示してリアルタイムでダイナミックな更新を行えるようにしたいと考えています。

![Superb Owlが表示したいライブ更新。Wild Bird FundとOwl Rescueの間で進行中の試合を表示しています。現在第4クォーターで、スコアは2-4でOWLがリードしています。]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

### ステップ1: カスタムレイアウトを追加する {#step-1-add-a-custom-layout}

1つ以上のカスタム通知RemoteViewレイアウトをプロジェクトに追加できます。これらは、通知が折りたたまれた状態や展開された状態でどのように表示されるかを処理するのに役立ちます。ディレクトリ構造は次のようになります。

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

各XMLファイルで、カスタムレイアウトを作成します。Superb Owlは、折りたたみ時と展開時のRemoteViewレイアウト用に次のレイアウトを作成しました。

{% tabs local %}
{% tab  Example: Collapsed layout %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/notification_title"
        style="@style/TextAppearance.Compat.Notification.Title"
        android:layout_width="wrap_content"
        android:layout_height="0dp"
        android:layout_weight="1" />
</LinearLayout>
```
{% endtab %}

{% tab Example: Expanded layout %}
{% details サンプルコードを表示 %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"

        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team1logo"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:layout_gravity="center"
            android:src="@drawable/team_default1"/>

        <TextView
            android:id="@+id/team1name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1.6"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/score"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="2-4"
            android:textColor="#555555"
            android:textAlignment="center"
            android:textSize="32sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/timeInfo"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>


    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team2logo"
            android:layout_gravity="center"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:src="@drawable/team_default2"/>

        <TextView
            android:id="@+id/team2name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>
</LinearLayout>
```
{% enddetails %}
{% endtab %}
{% endtabs %}

### ステップ2: カスタム通知ファクトリーを作成する {#step-2-create-a-custom-notification-factory}

アプリケーション内で、[`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)を拡張する`MyCustomNotificationFactory.kt`という名前の新しいファイルを作成し、カスタムRemoteViewレイアウトの表示方法を処理します。

次の例では、Superb Owlが進行中の試合のRemoteViewレイアウトを表示するカスタム通知ファクトリーを作成しました。[次のステップ](#android_step-3-map-custom-data)では、チームのデータをアクティビティにマッピングする`getTeamInfo`という新しいメソッドを作成します。

{% details サンプルコードを表示 %}
```kotlin
import android.app.Notification
import android.widget.RemoteViews
import androidx.core.app.NotificationCompat
import com.braze.models.push.BrazeNotificationPayload
import com.braze.push.BrazeNotificationFactory
import com.braze.push.BrazeNotificationUtils.getOrCreateNotificationChannelId
import com.braze.support.BrazeLogger.brazelog

class MyCustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        if (payload.extras.containsKey("live_update")) {
            val kvp = payload.extras
            val notificationChannelId = getOrCreateNotificationChannelId(payload)
            val context = payload.context

            if (context == null) {
                brazelog { "BrazeNotificationPayload has null context. Not creating notification" }
                return null
            }

            val team1 = kvp["team1"]
            val team2 = kvp["team2"]
            val score1 = kvp["score1"]
            val score2 = kvp["score2"]
            val time = kvp["time"]
            val quarter = kvp["quarter"]

            // Superb Owl will define the 'getTeamInfo' method in the next step.
            val (team1name, team1icon) = getTeamInfo(team1)
            val (team2name, team2icon) = getTeamInfo(team2)

            // Get the layouts to use in the custom notification.
            val notificationLayoutCollapsed = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_collapsed)
            val notificationLayoutExpanded = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_expanded)

            // Very simple notification for the small layout
            notificationLayoutCollapsed.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $quarter"
            )

            notificationLayoutExpanded.setTextViewText(R.id.score, "$score1 - $score2")
            notificationLayoutExpanded.setTextViewText(R.id.team1name, team1name)
            notificationLayoutExpanded.setTextViewText(R.id.team2name, team2name)
            notificationLayoutExpanded.setTextViewText(R.id.timeInfo, "$time - $quarter")
            notificationLayoutExpanded.setImageViewResource(R.id.team1logo, team1icon)
            notificationLayoutExpanded.setImageViewResource(R.id.team2logo, team2icon)

            val customNotification = NotificationCompat.Builder(context, notificationChannelId)
                .setSmallIcon(R.drawable.notification_small_icon)
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(notificationLayout)
                .setCustomBigContentView(notificationLayoutExpanded)
                .build()
            return customNotification
        } else {
            // Use the BrazeNotificationFactory for all other notifications
            return super.createNotification(payload)
        }
    }
}
```
{% enddetails %}

### ステップ3: カスタムデータをマッピングする {#step-3-map-custom-data}

`MyCustomNotificationFactory.kt`で、ライブ更新が表示されたときにデータを処理するための新しいメソッドを作成します。

Superb Owlは、各チームの名前とロゴを展開されたライブ更新にマッピングするために、次のメソッドを作成しました。

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

### ステップ4: カスタム通知ファクトリーを設定する {#step-4-set-the-custom-notification-factory}

アプリケーションクラスで[`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)を使用して、カスタム通知ファクトリーを設定します。

```kotlin
import com.braze.Braze

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### ステップ5: アクティビティを送信する {#step-5-send-the-activity}

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST APIエンドポイントを使用して、ユーザーのAndroidデバイスにプッシュ通知を送信できます。

#### curlコマンドの例 {#example-curl-command}

Superb Owlは次のcurlコマンドを使用してリクエストを送信しました。

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
curlコマンドはテストに役立ちますが、すでに[iOSライブアクティビティ]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)を処理しているバックエンドでこの呼び出しを処理することをおすすめします。
{% endalert %}

#### リクエストパラメーター {#request-parameters}

| キー | 説明 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY`                | `messages.send`権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。                                                                                                     |
| `BRAZE_REST_ENDPOINT`         | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics#endpoints)に応じて異なります。                                                                                                                  |
| `USER_ID`                     | 通知を送信するユーザーのID。                                                                                                                                                                                          |
| `messages.android_push.title` | メッセージのタイトル。デフォルトでは、カスタム通知ファクトリーのライブ通知には使用されませんが、フォールバックとして使用される場合があります。                                                                                                    |
| `messages.android_push.alert` | メッセージの本文。デフォルトでは、カスタム通知ファクトリーのライブ通知には使用されませんが、フォールバックとして使用される場合があります。                                                                                                     |
| `messages.extra`              | カスタム通知ファクトリーがライブ通知に使用するキーと値のペア。この値には任意の文字列を割り当てることができます。ただし、この例では`live_updates`を使用して、デフォルトのプッシュ通知かライブプッシュ通知かを判断しています。 |
| `ASSIGNED_NOTIFICATION_ID`    | 選択したユーザーのライブ通知に割り当てる通知ID。IDはこのゲームに対して一意である必要があり、後で[既存の通知を更新する](#android_step-4-update-data-with-the-braze-rest-api)ために使用する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="リクエストパラメーター" }

### ステップ6: アクティビティを更新する {#step-6-update-the-activity}

既存のRemoteView通知を新しいデータで更新するには、`messages.extra`に割り当てられた関連するキーと値のペアを変更し、同じ`notification_id`を使用して`/messages/send`エンドポイントを再度呼び出します。

## パーソナライズされたプッシュ通知 {#personalized-push-notifications}

プッシュ通知では、カスタムビュー階層内にユーザー固有の情報を表示できます。次の例では、APIトリガーを使用してパーソナライズされたプッシュ通知をユーザーに送信し、アプリで特定のタスクを完了した後に現在の進捗状況を確認できるようにしています。

![パーソナライズされたプッシュのダッシュボード例]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

ダッシュボードでパーソナライズされたプッシュを設定するには、表示する特定のカテゴリを登録し、Liquidを使用して表示する関連ユーザー属性を設定します。

![パーソナライズされたプッシュのダッシュボード例]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}