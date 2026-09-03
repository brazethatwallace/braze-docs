---
nav_title: 푸시 알림
article_title: 푸시 알림
page_order: 2.3
description: "이 랜딩 페이지에서는 푸시 알림에 관한 모든 것을 확인할 수 있습니다."
---

# 푸시 알림 {#push-notifications}

> [푸시 알림]({{site.baseurl}}/user_guide/channels/push)을 사용하면 중요한 이벤트가 발생할 때 앱에서 알림을 보낼 수 있습니다. 전달할 새 인스턴트 메시지, 송출할 뉴스 속보 알림 또는 오프라인으로 시청할 수 있도록 다운로드할 준비가 된 사용자가 좋아하는 TV 프로그램의 최신 에피소드가 있을 때 푸시 알림을 전송할 수 있습니다. 또한 애플리케이션이 필요할 때만 실행되므로 백그라운드 가져오기보다 더 효율적입니다.

{% alert note %}
**웹 URL로 리디렉션**과 **앱 내에서 웹 URL 열기**가 선택되지 않았는데도 링크가 앱 내에서 열리는 경우, 앱이 해당 URL을 직접 처리하고 있을 수 있습니다(예: iOS의 유니버설 링크 또는 Android의 앱 링크). 브라우저에서 링크를 열려면, 사용자가 알림을 탭할 때 앱이 해당 URL을 시스템 브라우저로 위임하는지 확인하거나, 클릭 동작이 Braze 대시보드 설정과 일치하도록 앱의 URL 처리 방식을 조정하세요. 클릭 동작 및 URL 처리 구성 방법은 해당 플랫폼의 푸시 설명서를 참조하세요.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
## Android TV 푸시 알림 소개 {#about-push-notifications-for-android-tv}

![Android TV 푸시 알림 가이드에 사용되는 Android TV 기기 일러스트레이션.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

네이티브 기능은 아니지만, Braze Android SDK와 Firebase Cloud Messaging을 활용하여 Android TV용 푸시 토큰을 등록하면 Android TV 푸시 통합이 가능합니다. 다만, 알림 페이로드가 수신된 후 이를 표시할 UI를 직접 구축해야 합니다.

## 전제 조건 {#prerequisites}

이 기능을 사용하려면 다음을 완료해야 합니다.

- [Braze Android SDK 통합]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Braze Android SDK용 푸시 알림 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)

## 푸시 알림 설정하기 {#setting-up-push-notifications}

Android TV용 푸시 알림을 설정하려면 다음을 수행합니다.

1. 앱에서 알림을 표시할 커스텀 뷰를 만듭니다.
2. [커스텀 알림 팩토리]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display)를 만듭니다. 이렇게 하면 기본 SDK 동작이 재정의되어 알림을 수동으로 표시할 수 있습니다. `null`을 반환하면 SDK가 처리하지 않으므로 알림을 표시하려면 커스텀 코드가 필요합니다. 이 단계를 완료하면 Android TV로 푸시를 보낼 수 있습니다.<br><br>
3. (선택 사항) 클릭 분석을 효과적으로 추적하려면 클릭 분석 추적을 설정합니다. Braze 푸시 열람 및 수신 인텐트를 수신하는 [푸시 콜백]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback)을 만들어 이를 구현할 수 있습니다.

{% alert note %}
이러한 알림은 지속되지 않으며 기기가 표시하는 동안에만 사용자에게 보입니다. 이는 Android TV의 알림 센터가 알림 기록을 지원하지 않기 때문입니다.
{% endalert %}

## Android TV 푸시 알림 테스트하기 {#testing-android-tv-push-notifications}

푸시 구현이 성공적인지 테스트하려면 일반 Android 기기와 동일하게 Braze 대시보드에서 알림을 보냅니다.

- **애플리케이션이 닫혀 있는 경우**: 푸시 메시지가 화면에 토스트 알림으로 표시됩니다.
- **애플리케이션이 열려 있는 경우**: 자체 호스팅 UI에 메시지를 표시할 수 있습니다. Android 모바일 SDK 인앱 메시지의 UI 스타일을 따르세요.

## 모범 사례 {#best-practices}

Braze를 사용하는 마케터의 경우, Android TV로 Campaign을 시작하는 것은 Android 모바일 앱으로 푸시를 보내는 것과 동일합니다. 이러한 기기만 타겟팅하려면 세분화에서 Android TV 앱을 선택하세요.

FCM에서 반환하는 전달 및 클릭 응답은 모바일 Android 기기와 동일한 규칙을 따르므로, 오류는 메시지 활동 로그에서 확인할 수 있습니다.

{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}