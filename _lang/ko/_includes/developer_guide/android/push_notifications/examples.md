{% multi_lang_include developer_guide/prerequisites/android.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) 합니다.

## 커스텀 알림 레이아웃 {#custom-notification-layout}

Braze 알림은 [데이터 메시지](https://firebase.google.com/docs/cloud-messaging/concept-options)로 전송됩니다. 이는 앱이 백그라운드 상태에서도 항상 응답하고 그에 따른 동작을 수행할 기회를 가진다는 것을 의미합니다(앱이 백그라운드에 있을 때 시스템이 자동으로 처리할 수 있는 알림 메시지와는 대조적입니다). 따라서 알림 트레이에 전달되는 알림 내에 개인화된 UI 요소를 표시하는 등 애플리케이션에서 경험을 커스터마이즈할 수 있습니다. 이 방식으로 푸시를 구현하는 것이 낯설 수 있지만, Braze의 잘 알려진 기능 중 하나인 [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)는 커스텀 뷰 컴포넌트를 사용하여 매력적인 경험을 만드는 대표적인 예입니다!

{% alert important %}
Android는 커스텀 알림 뷰를 구현하는 데 사용할 수 있는 컴포넌트에 몇 가지 제한을 두고 있습니다. 알림 뷰 레이아웃은 [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) 프레임워크와 호환되는 View 객체_만_ 포함해야 합니다.
{% endalert %}

[`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) 인터페이스를 사용하여 Braze 푸시 알림이 표시되는 방식을 커스터마이즈할 수 있습니다. `BrazeNotificationFactory`를 확장하면, Braze는 알림이 사용자에게 표시되기 전에 팩토리의 `createNotification()` 메서드를 호출합니다. 그런 다음 Braze 대시보드 또는 REST API를 통해 전송된 커스텀 키-값 페어가 포함된 페이로드를 전달합니다.

이 섹션에서는 야생 동물 구조 팀이 올빼미를 가장 많이 구출하는 경쟁을 펼치는 새로운 게임 쇼의 진행자인 Superb Owl과 함께 작업합니다. Superb Owl은 Android 앱에서 실시간 업데이트 알림을 활용하여 진행 중인 경기의 상태를 표시하고 알림을 실시간으로 동적 업데이트하려고 합니다.

![Superb Owl이 보여주려는 실시간 업데이트로, 'Wild Bird Fund'와 'Owl Rescue' 간의 진행 중인 경기를 표시합니다. 현재 4쿼터이며 점수는 2-4로 OWL이 리드하고 있습니다.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

### 1단계: 커스텀 레이아웃 추가 {#step-1-add-a-custom-layout}

프로젝트에 하나 이상의 커스텀 알림 RemoteView 레이아웃을 추가할 수 있습니다. 이는 알림이 축소되거나 확장될 때 표시되는 방식을 처리하는 데 유용합니다. 디렉토리 구조는 다음과 유사해야 합니다:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

각 XML 파일에서 커스텀 레이아웃을 만듭니다. Superb Owl은 축소 및 확장 RemoteView 레이아웃에 대해 다음과 같은 레이아웃을 만들었습니다:

{% tabs local %}
{% tab 예제: 축소 레이아웃 %}
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

{% tab 예제: 확장 레이아웃 %}
{% details 샘플 코드 보기 %}
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

### 2단계: 커스텀 알림 팩토리 만들기 {#step-2-create-a-custom-notification-factory}

애플리케이션에서 [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)를 확장하는 `MyCustomNotificationFactory.kt`라는 새 파일을 만들어 커스텀 RemoteView 레이아웃이 표시되는 방식을 처리합니다.

다음 예제에서 Superb Owl은 진행 중인 경기를 위한 RemoteView 레이아웃을 표시하는 커스텀 알림 팩토리를 만들었습니다. [다음 단계](#android_step-3-map-custom-data)에서는 팀 데이터를 활동에 매핑하기 위해 `getTeamInfo`라는 새 메서드를 만듭니다.

{% details 샘플 코드 보기 %}
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

### 3단계: 커스텀 데이터 매핑 {#android_step-3-map-custom-data}

`MyCustomNotificationFactory.kt`에서 실시간 업데이트가 표시될 때 데이터를 처리하기 위한 새 메서드를 만듭니다.

Superb Owl은 각 팀의 이름과 로고를 확장된 실시간 업데이트에 매핑하기 위해 다음 메서드를 만들었습니다:

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

### 4단계: 커스텀 알림 팩토리 설정 {#step-4-set-the-custom-notification-factory}

애플리케이션 클래스에서 [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)를 사용하여 커스텀 알림 팩토리를 설정합니다.

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

### 5단계: 활동 전송 {#step-5-send-the-activity}

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST API 엔드포인트를 사용하여 사용자의 Android 기기에 푸시 알림을 전송할 수 있습니다.

#### curl 명령어 예제 {#example-curl-command}

Superb Owl은 다음 curl 명령어를 사용하여 요청을 전송했습니다:

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
curl 명령어는 테스트에 유용하지만, 이미 [iOS 실시간 활동]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)을 처리하고 있는 백엔드에서 이 호출을 처리하는 것을 권장합니다.
{% endalert %}

#### 요청 파라미터 {#request-parameters}

| 키 | 설명 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY` | `messages.send` 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| `BRAZE_REST_ENDPOINT` | REST 엔드포인트 URL입니다. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics#endpoints)에 따라 달라집니다. |
| `USER_ID` | 알림을 전송할 사용자의 ID입니다. |
| `messages.android_push.title` | 메시지 제목입니다. 기본적으로 커스텀 알림 팩토리의 실시간 알림에는 사용되지 않지만 대체 값으로 사용될 수 있습니다. |
| `messages.android_push.alert` | 메시지 본문입니다. 기본적으로 커스텀 알림 팩토리의 실시간 알림에는 사용되지 않지만 대체 값으로 사용될 수 있습니다. |
| `messages.extra` | 커스텀 알림 팩토리가 실시간 알림에 사용하는 키-값 페어입니다. 이 값에 임의의 문자열을 할당할 수 있습니다. 그러나 이 예제에서는 `live_updates`를 사용하여 기본 푸시 알림인지 실시간 푸시 알림인지를 결정합니다. |
| `ASSIGNED_NOTIFICATION_ID` | 선택한 사용자의 실시간 알림에 할당할 알림 ID입니다. 이 ID는 해당 게임에 고유해야 하며, 나중에 [기존 알림을 업데이트](#android_step-4-update-data-with-the-braze-rest-api)하려면 반드시 사용해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요청 파라미터" }

### 6단계: 활동 업데이트 {#step-6-update-the-activity}

기존 RemoteView 알림을 새 데이터로 업데이트하려면 `messages.extra`에 할당된 관련 키-값 페어를 수정한 다음, 동일한 `notification_id`를 사용하여 `/messages/send` 엔드포인트를 다시 호출합니다.

## 개인화된 푸시 알림 {#personalized-push-notifications}

푸시 알림은 커스텀 뷰 계층 구조 내에서 사용자별 정보를 표시할 수 있습니다. 다음 예제에서는 API 트리거를 사용하여 사용자에게 개인화된 푸시 알림을 전송하여, 앱에서 특정 작업을 완료한 후 현재 진행 상황을 확인할 수 있도록 합니다.

![개인화된 푸시 대시보드 예제]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

대시보드에서 개인화된 푸시를 설정하려면, 표시할 특정 카테고리를 등록한 다음 Liquid를 사용하여 표시하려는 관련 사용자 속성을 설정합니다.

![개인화된 푸시 대시보드 예제]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}