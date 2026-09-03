## 문제 해결 {#troubleshooting}

### 푸시 알림을 탭해도 앱이 열리지 않음 {#tapping-push-notification-doesnt-open-the-app}

Android에서 푸시 알림을 탭했을 때 앱이 자동으로 포그라운드로 전환되고 딥링크가 열리는지 여부는 네이티브 `com_braze_handle_push_deep_links_automatically` 플래그로 제어되며, 기본값은 `false`입니다.

기본값 `false`인 경우:

- 네이티브 SDK는 여전히 `BRAZE_PUSH_CLICKED` 브로드캐스트를 전송하며, Dart `push_opened` 리스너도 예상대로 실행됩니다.
- 네이티브 SDK가 `startActivity()`를 호출하지 않으므로, 앱이 포그라운드로 전환되지 않고 딥링크도 자동으로 열리지 않습니다.

이 두 가지 동작이 현재 겪고 있는 상황과 일치한다면, 플래그 설정이 원인일 가능성이 높습니다.
이를 확인하려면 기기 로그에서 `BrazePushReceiver`가 `com.braze.action.BRAZE_PUSH_CLICKED`를 처리하는 항목을 찾고, Flutter 로그에서 `push_opened` 이벤트가 기록되었지만 앱이 실행되지 않은 것을 확인하세요.

이 문제를 해결하려면 `braze.xml`에서 `com_braze_handle_push_deep_links_automatically`를 `true`로 설정하세요:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

자세한 내용은 Flutter 푸시 알림 가이드의 [딥링크 추가(Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android)를 참조하세요.

### 기타 푸시 전달 및 등록 문제 {#other-push-delivery-and-registration-issues}

Braze Flutter SDK for Android는 네이티브 Braze Android SDK 위에 구축되어 있으므로, 대부분의 푸시 전달, 등록 및 로깅 문제(발신자 ID 불일치, Google Play 서비스 누락, `BrazeFirebaseMessagingService` 미등록 등)가 Flutter 앱에도 동일하게 적용됩니다. 자세한 내용은 [네이티브 Android 문제 해결 가이드]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)를 참조하세요.