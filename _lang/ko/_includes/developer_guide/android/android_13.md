# Android 13으로 업그레이드하기 {#upgrading-to-android-13}

> 이 가이드에서는 Android 13(2022)에 도입된 관련 변경 사항과 Braze Android SDK 통합에 필요한 업그레이드 단계에 대해 설명합니다.

전체 마이그레이션 가이드는 [Android 13 개발자 설명서](https://developer.android.com/about/versions/13)를 참조하세요.

## Android 13 Braze SDK

Android 13에 대비하려면 Braze SDK를 [최신 버전(v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300)으로 업그레이드하세요. 이렇게 하면 새로운 ['코드 없는' 푸시 프라이머 기능]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)에 액세스할 수 있습니다.

## Android 13의 변경 사항 {#changes-in-android-13}

### 푸시 권한 {#push-permission}

Android 13에서는 푸시 알림을 보내는 앱을 관리하는 방식에 [주요 변경 사항](https://developer.android.com/about/versions/13/changes/notification-permission)을 도입했습니다. Android 13에서는 푸시 알림을 표시하기 전에 앱이 권한을 얻어야 합니다.

![메시지 하단에 "허용" 및 "허용 안 함" 버튼이 두 개 있는 "Kitchenerie에서 알림을 보내도록 허용하시겠습니까?"라고 묻는 Android 푸시 메시지입니다.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

이 새로운 권한은 권한을 얻기 위해 한 번만 시도할 수 있는 iOS 및 웹 푸시와 유사한 패턴을 따릅니다. 사용자가 `Don't Allow`를 선택하거나 프롬프트를 무시하면 앱에서 다시 권한을 요청할 수 없습니다.

앱에서는 Android 13으로 업데이트하기 전에 이전에 푸시 알림을 활성화한 사용자를 [면제](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility)합니다. 이러한 사용자는 권한을 요청하지 않고도 Android 13으로 업데이트할 때 푸시를 [계속 수신할 자격](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps)이 유지됩니다.

#### 권한 프롬프트 타이밍 {#push-permission-timing}

**Android 13 타겟팅**

Android 13을 타겟팅하는 앱은 권한을 요청하고 네이티브 푸시 프롬프트를 표시할 시기를 제어할 수 있습니다.

사용자가 Android 12에서 13으로 업그레이드하고, 앱이 이전에 설치되어 있었으며, 이미 푸시를 보내고 있었다면 시스템이 자격이 있는 모든 앱에 새 알림 권한을 자동으로 사전 부여합니다. 즉, 이러한 앱은 사용자에게 계속 알림을 보낼 수 있으며, 사용자에게 런타임 권한 프롬프트가 표시되지 않습니다.

자세한 내용은 Android 개발자 설명서의 [기존 앱 업데이트에 미치는 영향](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps)을 참조하세요.

**Android 12 이하 타겟팅**

앱이 아직 Android 13을 타겟팅하지 않는 경우, Android 13을 사용하는 신규 사용자가 앱을 설치하면 앱이 첫 번째 알림 채널을 생성할 때(`notificationManager.createNotificationChannel` 사용) 자동으로 푸시 권한 프롬프트가 표시됩니다. 이미 앱을 설치한 후 Android 13으로 업그레이드하는 사용자에게는 프롬프트가 표시되지 않으며 자동으로 푸시 권한이 부여됩니다.

{% alert note %}
Braze SDK v23.0.0은 푸시 알림 수신 시 기본 알림 채널이 아직 존재하지 않으면 자동으로 생성합니다. Android 13을 타겟팅하지 않는 경우, 알림을 표시하는 데 필요한 푸시 권한 프롬프트가 표시됩니다.
{% endalert %}

## Android 13 준비 {#next-steps}

앱이 Android 13을 타겟으로 설정하여 사용자에게 푸시 권한을 요청하는 시점을 제어하는 것을 강력히 권장합니다.

이를 통해 보다 적절한 시점에 사용자에게 프롬프트를 표시하여 [푸시 옵트인 비율](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps)을 최적화할 수 있으며, 앱이 푸시 권한을 요청하는 방법과 시점에 대한 사용자 경험을 개선할 수 있습니다.

새로운 ['코드 없는' 푸시 프라이머 기능]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)을 사용하려면 Android SDK를 [최신 버전(v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300)으로 업그레이드하세요.