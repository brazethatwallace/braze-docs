---
nav_title: "알림 채널"
article_title: 푸시 알림 채널
page_order: 4
page_type: reference
description: "이 참조 문서에서는 Android O 전환, Braze에 채널 추가, 대체 채널 설정 등 Android 푸시 알림 채널 관련 주제를 다룹니다."
platform: Android
channel:
  - push

---

# 알림 채널 {#notification-channels}

> [알림 채널](https://www.braze.com/blog/android-o-push-notifications-channels/)은 Android O에서 추가된 푸시 알림을 정리하는 방법입니다. O부터 모든 푸시 알림에는 메시지 유형(예: "채팅 알림" 또는 "팔로우 알림")을 나타내는 알림 채널이 있어야 합니다. 사용자는 개별 채널을 기반으로 알림의 다양한 측면(예: 다시 알림, 소리/진동 설정, 수신 거부 등)을 제어할 수 있습니다.

알림 채널은 애플리케이션 코드에서만 생성할 수 있으며 Braze 대시보드에서 프로그래밍 방식으로 생성할 수 없습니다. 엔지니어링 팀이 마케터와 협력하여 원하는 알림 채널이 대시보드에 올바르게 추가되도록 하는 것을 권장합니다.

API 레벨 26(Android O)부터 푸시 알림을 표시하려면 유효한 채널이 필요합니다. 앱이 Android O 이상을 대상으로 하는 경우 Braze SDK 버전 2.1.0 이상을 사용해야 합니다. 개발 팀은 사용할 채널과 각 채널에 대한 권장 알림 설정(예: 중요도, 소리, 조명)을 애플리케이션 코드에서 정의해야 합니다. 자세한 내용은 [Android 개발자 설명서](https://developer.android.com/preview/features/notification-channels.html) 및 [Braze 개발자 설명서]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration#step-5-define-notification-channels)를 참조하세요.

{% alert note %}
Android는 채널 이름의 현지화를 지원하므로 애플리케이션 코드에서 하나의 채널 ID를 채널 이름의 여러 번역과 연결할 수 있습니다.
{% endalert %}

이러한 채널이 생성되면 엔지니어가 관련 채널 ID를 마케팅 팀에 전달해야 합니다. 팀은 Campaigns 및 Canvases에서 사용할 수 있도록 채널 이름과 채널 ID를 Braze 대시보드에 입력해야 합니다.

Braze 대시보드에 채널을 추가하려면 Android 푸시 작성기로 이동하여 알림 채널 필드를 선택한 다음 **채널 관리**를 선택합니다.
{% alert important %}
"앱 관리" 권한이 있는 사용자만 채널을 관리할 수 있습니다.
{% endalert %}

## SDK 기본 채널 {#sdk-default-channel}

Android는 API 레벨 26(Android O) 이상에서 푸시 알림을 표시하려면 유효한 채널이 필요합니다. Braze Android SDK 2.1.0에는 "General"이라는 기본 채널이 포함되어 있으며, 대시보드에서 추가 채널을 지정하지 않거나 유효하지 않은 채널로 발송을 시도하는 경우 이 채널이 생성되어 사용됩니다. SDK에서 이 레이블의 이름을 변경하고 채널에 대한 설명을 제공할 수 있습니다. 더 나은 사용자 경험을 제공하기 위해 이를 고려하는 것을 권장합니다.

채널이 애플리케이션에 추가되면 제거할 수 있습니다. 그러나 소비자는 항상 [제거된][3] 채널의 수를 볼 수 있습니다. Braze 대시보드에는 프로그래밍 방식으로 채널을 생성하는 기능이 포함되어 있지 않습니다. 원활한 경험을 제공하려면 채널을 애플리케이션 코드에서 생성하고 정의해야 합니다.

다시 한번, Android O 타겟팅으로의 원활한 전환을 위해 엔지니어링 팀과 조율하는 것을 권장합니다.

## 대시보드 대체 채널 {#dashboard-fallback-channel}

Braze에서는 대시보드 대체 채널을 지정할 수 있습니다. 대시보드 대체 채널의 목적은 명시적인 채널 선택이 없는 레거시 푸시 메시지에 채널 ID를 제공하는 것입니다. 채널 선택이란 Android 푸시 작성기에서 채널을 선택하는 것을 의미합니다.

채널이 선택되지 않은 메시지는 대시보드 대체 채널 ID로 발송됩니다. 대시보드 대체 채널을 변경하면 명시적으로 채널이 선택되지 않은 모든 메시지가 새 대체 채널의 ID로 발송됩니다.

다음은 대시보드 대체 채널의 예상 동작에 대한 예시입니다:

대시보드 대체 채널이 "Marketing"이고 채널을 선택한 적이 없는 Android 푸시 메시지가 10개 있습니다. 이 Campaigns는 "Marketing" 채널이 대시보드 대체 채널이기 때문에 "Marketing" 채널을 통해 발송됩니다.

또한 "Social Notifications" 채널을 통해 발송하도록 선택한 메시지가 15개, "Marketing" 채널을 통해 발송하도록 선택한 메시지가 5개 있습니다.

그런 다음 대시보드 기본 채널을 "Marketing"에서 "Updates"로 변경하기로 결정합니다.

이 상황에서 이전에 "Marketing" 채널을 통해 발송되던 채널 선택이 없는 10개의 Campaigns는 이제 "Updates" 채널을 통해 발송됩니다. 이러한 메시지는 대체 채널을 통해 발송되기 때문입니다. "Social Notifications" 채널을 통해 발송되던 15개의 메시지는 계속 "Social Notifications" 채널을 통해 발송됩니다. "Marketing" 채널을 통해 발송되던 5개의 메시지는 계속 "Marketing" 채널을 통해 발송됩니다.

Braze에 유효하지 않은 채널 ID가 제공된 경우(예: 개발자가 SDK에서 생성하지 않은 채널 ID를 제공한 경우), SDK 기본 채널을 통해 알림을 전달합니다. 따라서 개발 중에 Braze 대시보드를 통해 알림 채널을 테스트하는 것을 강력히 권장합니다.

채널의 예상 동작을 더 잘 이해하려면 다음 표를 참조하세요:

| 시나리오 | 결과 |
| --- | --- |
| **회사 ABC**가 Android O를 지원하는 SDK로 업데이트<br>**회사 ABC**가 Braze 대시보드에 채널을 추가하지 않음<br>**회사 ABC**가 SDK 기본 채널의 이름을 변경하지 않음 | Android O 기기로 발송된 푸시 알림은 "General"이라는 채널을 생성하고 알림은 "General" 채널을 통해 발송됩니다 |
| **회사 XYZ**가 Android O를 지원하는 SDK로 업데이트<br>**회사 XYZ**가 Braze 대시보드에 채널을 추가하지 않음<br>**회사 XYZ**가 SDK 기본 채널의 이름을 "Marketing"으로 변경 | Android O 기기로 발송된 푸시 알림은 "Marketing"이라는 채널을 생성하고 알림은 "Marketing" 채널을 통해 발송됩니다 |
| **회사 LMN**이 Android O를 지원하는 SDK로 업데이트<br>**회사 LMN**이 애플리케이션 코드에서 "Promotions"와 "Order Updates" 두 개의 채널을 정의<br>**회사 LMN**이 "Promotions"와 "Order Updates"의 채널 ID를 Braze 대시보드에 추가<br>**회사 LMN**이 "Promotions"를 대시보드 대체 채널로 지정<br>**회사 LMN**이 SDK 기본 채널의 이름을 "Marketing"으로 변경 | Android O 기기로 발송된 푸시 알림은 채널을 생성하지 않습니다<br><br>마케터가 알림을 "Order Updates" 또는 "Marketing" 채널을 통해 발송하도록 명시적으로 지정하지 않는 한, 채널이 대시보드에 추가되기 전에 생성된 모든 알림은 "Promotions" 채널을 통해 발송됩니다<br><br>SDK 기본 채널인 "Marketing"은 회사가 유효하지 않은 채널 ID로 알림을 발송하려고 하거나 명시적으로 선택한 경우에만 생성되어 사용됩니다 |
| **회사 HIJ**가 Android O로 업데이트했지만 Braze Android SDK를 2.1.0 이상으로 업데이트하지 않음 | Android O 이상을 실행하는 사용자에게 발송된 알림이 표시되지 않습니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="대시보드 대체 채널" }

## Braze 대시보드에 채널 추가 {#adding-channels-to-the-braze-dashboard}

1. Android 푸시를 포함하는 Campaign 또는 Canvas를 열거나 생성합니다.
2. Android 푸시 메시지 작성기로 이동합니다.
3. **Manage Notification Channels**를 선택합니다. 여기에 추가된 채널은 모든 Campaigns 및 Canvases에서 전역적으로 사용할 수 있습니다. 채널을 관리하려면 워크스페이스에 대한 "Manage Apps" [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 있어야 합니다.

특정 Campaign 또는 캔버스 단계에 알림 채널을 적용하면 **도달 가능 사용자** 수(타겟 오디언스 단계에 위치)가 Android 푸시에 대해 변경되지 않는 것처럼 보입니다. 그러나 선택한 알림 채널에 가입한 사용자만 메시지를 볼 수 있으며, Campaign 분석(예: 클릭)은 이 오디언스를 기반으로 측정됩니다.

![구성된 채널 목록과 Manage Notification Channels가 표시된 Android 푸시 작성기]({% image_buster /assets/img_archive/push_notification_channels.png %})

{:start="4"}
4. **Add Notification Channel**을 선택합니다.
5. 추가하려는 알림 채널의 이름과 ID를 입력합니다.<br><br>![채널 이름과 채널 ID 필드가 있는 Add Notification Channel 대화 상자]({% image_buster /assets/img_archive/push_notifications_channels_manage.png %})<br><br>
6. 추가하려는 각 알림 채널에 대해 4단계와 5단계를 반복합니다.
7. **Save**를 선택하여 변경 사항을 저장합니다.

## 대체 채널 지정 {#specifying-your-fallback-channel}

대체 채널은 메시지에 대한 채널을 선택하지 않은 경우 Braze가 Android 메시지를 발송하려고 시도하는 채널입니다. 채널 선택이 없는 Android 메시지가 있는 Campaigns 및 Canvases는 팀이 Braze 대시보드에 채널을 추가하기 전에 생성된 Campaigns 및 Canvases뿐입니다. 대체 채널을 변경하면 명시적인 채널 선택이 없는 모든 Campaigns 및 Canvases에 전역적으로 변경 사항이 적용됩니다.

1. 기존 Campaign 또는 Canvas를 엽니다.
2. Android 푸시 작성기로 이동합니다.
3. 알림 채널 옵션을 확장한 후 **Manage Notification Channels**를 선택합니다.
4. 대시보드에 채널을 추가합니다(아직 추가되지 않은 경우).
5. 대체 채널로 지정하려는 채널 옆의 라디오 버튼을 선택합니다.
6. 변경 사항을 저장합니다. 변경 사항은 전역적으로 적용됩니다.

## Android 푸시 메시지에 채널 추가 {#adding-channels-to-your-android-push-messages}

1. Campaign 또는 Canvas의 Android 푸시 작성기로 이동합니다.
2. 드롭다운에서 사용하려는 채널을 선택합니다. 드롭다운이 없고 다음과 같은 화면이 표시되는 경우, Campaigns에서 채널을 선택하기 전에 먼저 채널을 추가해야 합니다.

![푸시 알림 채널 작성기]({% image_buster /assets/img_archive/push_notifications_channels_composer.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels