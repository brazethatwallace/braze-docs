## Android TV용 푸시 알림 정보 {#about-push-notifications-for-android-tv}

![Android TV 푸시 알림 가이드에 사용되는 Android TV 기기 일러스트레이션.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

기본 기능은 아니지만 Braze Android SDK와 Firebase Cloud Messaging을 활용하여 Android TV용 푸시 토큰을 등록하면 Android TV 푸시 통합이 가능합니다. 그러나 알림 페이로드가 수신된 후 이를 표시하는 UI를 빌드해야 합니다.

## 필수 조건 {#prerequisites}

이 기능을 사용하려면 다음을 완료해야 합니다:

- [Braze Android SDK 통합]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Braze Android SDK용 푸시 알림 설정]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## 푸시 알림 설정하기 {#setting-up-push-notifications}

Android TV용 푸시 알림을 설정하려면 다음과 같이 하세요:

1. 앱에서 커스텀 뷰를 만들어 알림을 표시하세요.
2. [커스텀 알림 팩토리]({{site.baseurl}}/developer_guide/push_notifications/customization#customization-display)를 만듭니다. 이렇게 하면 기본 SDK 동작이 재정의되고 알림을 수동으로 표시할 수 있습니다. `null`을 반환하면 SDK가 처리하지 않으며, 알림을 표시하려면 커스텀 코드가 필요합니다. 이 단계가 완료되면 Android TV로 푸시 전송을 시작할 수 있습니다!<br><br>
3. (선택 사항) 클릭 분석을 효과적으로 추적하려면 클릭 분석 추적을 설정하세요. Braze 푸시 열람 및 수신 인텐트를 수신 대기하도록 [푸시 콜백]({{site.baseurl}}/developer_guide/push_notifications/customization#push-callback)을 생성하면 됩니다.

{% alert note %}
이러한 알림은 **지속되지 않으며** 기기가 해당 알림을 표시할 때만 사용자에게 표시됩니다. 이는 Android TV의 알림 센터가 과거 알림 기록을 지원하지 않기 때문입니다.
{% endalert %}

## Android TV 푸시 알림 테스트하기 {#testing-android-tv-push-notifications}

푸시 구현이 성공적인지 테스트하려면 평소 Android 기기에서와 마찬가지로 Braze 대시보드에서 알림을 보냅니다.

- **애플리케이션이 닫혀 있는 경우**: 푸시 메시지가 화면에 토스트 알림으로 표시됩니다.
- **애플리케이션이 열려 있는 경우**: 자체 호스팅 UI에 메시지를 표시할 수 있습니다. Android 모바일 SDK 인앱 메시지의 UI 스타일을 따르는 것이 좋습니다.

## 모범 사례 {#best-practices}

Braze를 사용하는 마케터의 경우, Android TV에 Campaign을 시작하는 것은 Android 모바일 앱에 푸시를 시작하는 것과 동일합니다. 이러한 기기만 독점적으로 타겟팅하려면 세분화에서 Android TV 앱을 선택하는 것이 좋습니다.

FCM이 반환하는 전달 및 클릭 응답은 모바일 Android 기기와 동일한 규칙을 따르므로 모든 오류는 메시지 활동 로그에서 확인할 수 있습니다.