{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## 푸시 알림 설정하기 {#setting-up-push-notifications}

### 1단계: 초기 설정 완료하기 {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### 1.1단계: 푸시 등록하기 {#step-11-register-for-push}

Google의 Firebase Cloud Messaging(FCM) API를 사용하여 푸시를 등록합니다. 전체 안내는 [네이티브 Android 푸시 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/)의 다음 단계를 참조하세요.

1. [프로젝트에 Firebase 추가하기]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-1-add-firebase-to-your-project).
2. [종속성에 Cloud Messaging 추가하기]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-2-add-cloud-messaging-to-your-dependencies).
3. [서비스 계정 생성하기]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-3-create-a-service-account).
4. [JSON 자격 증명 생성하기]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-generate-json-credentials).
5. [Braze에 JSON 자격 증명 업로드하기]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-5-upload-your-json-credentials-to-braze).

#### 1.2단계: Google 발신자 ID 가져오기 {#step-12-get-your-google-sender-id}

먼저 Firebase 콘솔로 이동하여 프로젝트를 열고 <i class="fa-solid fa-gear" aria-label="설정"></i>&nbsp;**Settings** > **Project settings**를 선택합니다.

![설정 메뉴가 열린 Firebase 프로젝트.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**Cloud Messaging**을 선택한 다음, **Firebase Cloud Messaging API (V1)** 아래에서 **Sender ID**를 클립보드에 복사합니다.

![Sender ID가 강조 표시된 Firebase 프로젝트의 Cloud Messaging 페이지.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### 1.3단계: `braze.xml` 업데이트하기 {#step-13-update-your-brazexml}

`braze.xml` 파일에 다음을 추가합니다. `FIREBASE_SENDER_ID`를 이전에 복사한 발신자 ID로 교체합니다.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### 1.1단계: APNs 인증서 업로드하기 {#step-11-upload-apns-certificates}

Apple 푸시 알림 서비스(APNs) 인증서를 생성하고 Braze 대시보드에 업로드합니다. 전체 안내는 [APNs 인증서 업로드하기]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-upload-your-apns-certificate)를 참조하세요.

#### 1.2단계: 앱에 푸시 알림 지원 추가하기 {#step-12-add-push-notification-support-to-your-app}

[네이티브 iOS 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)를 따르세요.

{% endtab %}
{% endtabs %}

### 2단계: 푸시 알림 이벤트 수신하기(선택 사항) {#step-2-listen-for-push-notification-events-optional}

Braze가 감지하고 처리한 푸시 알림 이벤트를 수신하려면 `subscribeToPushNotificationEvents()`를 호출하고 실행할 인수를 전달합니다.

{% alert note %}
Braze 푸시 알림 이벤트는 Android와 iOS 모두에서 사용할 수 있습니다. 플랫폼 차이로 인해 iOS에서는 사용자가 알림과 상호작용한 경우에만 Braze 푸시 이벤트를 감지합니다.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### 푸시 알림 이벤트 필드 {#push-notification-event-fields}

{% alert note %}
iOS의 플랫폼 제한으로 인해 Braze SDK는 앱이 포그라운드에 있을 때만 푸시 페이로드를 처리할 수 있습니다. 리스너는 사용자가 푸시와 상호작용한 후에만 iOS에서 `push_opened` 이벤트 유형에 대해 트리거됩니다.
{% endalert %}

푸시 알림 필드의 전체 목록은 다음 표를 참조하세요.

| 필드 이름 | 유형 | 설명 |
| ------------------ | --------- | ----------- |
| `payloadType`     | String    | 알림 페이로드 유형을 지정합니다. Braze Flutter SDK에서 전송되는 두 가지 값은 `push_opened`와 `push_received`입니다. iOS에서는 `push_opened` 이벤트만 지원됩니다. |
| `url`              | String    | 알림에 의해 열린 URL을 지정합니다. |
| `useWebview`      | Boolean   | `true`이면 URL이 앱 내 모달 웹뷰에서 열립니다. `false`이면 URL이 기기 브라우저에서 열립니다. |
| `title`            | String    | 알림의 제목을 나타냅니다. |
| `body`             | String    | 알림의 본문 또는 콘텐츠 텍스트를 나타냅니다. |
| `summaryText`     | String    | 알림의 요약 텍스트를 나타냅니다. iOS에서는 `subtitle`에서 매핑됩니다. |
| `badgeCount`      | Number   | 알림의 배지 수를 나타냅니다. |
| `timestamp`        | Number | 애플리케이션에서 페이로드를 수신한 시간을 나타냅니다. |
| `isSilent`        | Boolean   | `true`이면 페이로드가 무음으로 수신됩니다. Android 무음 푸시 알림 전송에 대한 자세한 내용은 [Android 무음 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)을 참조하세요. iOS 무음 푸시 알림 전송에 대한 자세한 내용은 [iOS 무음 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)을 참조하세요. |
| `isBrazeInternal`| Boolean   | 기능 플래그 동기화 또는 제거 추적과 같은 내부 SDK 기능을 위해 알림 페이로드가 전송된 경우 `true`입니다. 페이로드는 사용자에게 무음으로 수신됩니다. |
| `imageUrl`        | String    | 알림 이미지와 연결된 URL을 지정합니다. |
| `brazeProperties` | Object    | Campaign과 연결된 Braze 속성(키-값 페어)을 나타냅니다. |
| `ios`              | Object    | iOS 전용 필드를 나타냅니다. |
| `android`          | Object    | Android 전용 필드를 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 알림 이벤트 필드" }

### 3단계: 푸시 알림 표시 테스트하기 {#step-3-test-displaying-push-notifications}

네이티브 레이어에서 푸시 알림을 구성한 후 통합을 테스트하려면 다음을 수행합니다.

1. Flutter 애플리케이션에서 활성 사용자를 설정합니다. 이를 위해 `braze.changeUser('your-user-id')`를 호출하여 플러그인을 초기화합니다.
2. **Campaigns**로 이동하여 새 푸시 알림 Campaign을 생성합니다. 테스트할 플랫폼을 선택합니다.
3. 테스트 알림을 작성하고 **Test** 탭으로 이동합니다. 테스트 사용자와 동일한 `user-id`를 추가하고 **Send Test**를 클릭합니다.
4. 곧 기기에서 알림을 수신해야 합니다. 알림이 표시되지 않으면 알림 센터를 확인하거나 설정을 업데이트해야 할 수 있습니다.

{% alert tip %}
Xcode 14부터 iOS 시뮬레이터에서 원격 푸시 알림을 테스트할 수 있습니다.
{% endalert %}

### 4단계: 딥링크 추가하기(Android) {#step-4-add-deep-links-android}

{% alert warning %}
Android에서 `com_braze_handle_push_deep_links_automatically`의 기본값은 `false`입니다. 기본값을 사용하면 푸시 알림을 탭해도 Dart 리스너에 `push_opened` 이벤트가 전송되지만, 네이티브 SDK가 앱을 포그라운드로 가져오거나 딥링크 대상을 자동으로 열지 않습니다. 알림을 탭해도 앱이 실행되지 않는 경우 이 플래그가 가장 가능성 높은 원인입니다.
{% endalert %}

푸시 알림을 탭할 때 Braze가 자동으로 앱과 딥링크를 열도록 하려면 `braze.xml`에서 `com_braze_handle_push_deep_links_automatically`를 `true`로 설정합니다.

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

이 플래그는 네이티브 Android 코드에서 [런타임 구성]({{site.baseurl}}/developer_guide/sdk_integration#android_runtime-configuration)을 통해서도 설정할 수 있습니다.

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

딥링크를 커스텀으로 처리하려면 2단계에서 설명한 `subscribeToPushNotificationEvents()` 리스너를 사용하여 `push_opened` 이벤트의 `url` 필드를 직접 라우팅합니다. 자세한 내용은 [딥링킹]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=flutter)을 참조하세요.