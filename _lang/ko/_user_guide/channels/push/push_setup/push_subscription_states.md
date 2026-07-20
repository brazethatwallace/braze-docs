---
nav_title: "푸시 구독 상태"
article_title: "푸시 구독 상태"
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze의 푸시 활성화 및 푸시 구독 상태 개념을 다루며, iOS, Android, 웹 간의 근본적인 동작 차이를 설명합니다."
channel:
  - push

---

# 푸시 활성화 및 푸시 구독 {#push-enablement-and-push-subscription}

> 이 참조 문서에서는 Braze의 푸시 활성화 및 푸시 구독 상태 개념을 다루며, iOS, Android, 웹 간의 근본적인 동작 차이를 설명합니다.

{% multi_lang_include push/subscription_states.md %}

## 푸시 등록 및 상태가 표시되는 위치 {#where-push-registration-and-status-appear}

Braze에서 푸시 구독 상태, 등록 및 활성화를 확인할 수 있는 주요 위치는 세 곳입니다:

1. **[사용자 프로필](#user-profiles-and-push-changelog)** - **Engagement** 탭
2. **[세분화](#segmentation-and-push-filters)** - Segment 빌더
3. **[Campaign 및 Canvas 분석](#campaign-and-canvas-analytics)** - 각 메시지의 분석 페이지

### 사용자 프로필 및 푸시 변경 로그 {#user-profiles-and-push-changelog}

사용자 프로필([**사용자 검색**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) > 사용자 선택 > **Engagement** 탭)에서 **Contact Settings**는 푸시 구독 상태를 나열하고, **Push Registered For**(Braze가 해당 프로필에 포그라운드 푸시를 보내는 데 사용할 수 있는 앱 및 플랫폼)와 토큰 이동, 오류 및 등록 업데이트에 대한 **Push Changelog**를 표시합니다. **Push Registered For** 및 포그라운드 대 백그라운드 승인을 읽는 방법에 대해서는 [푸시 등록 상태 확인]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status)을 참조하세요.

iOS 및 Android에서 기기가 포그라운드 푸시 승인에서 백그라운드 전용으로 전환되면(예: 사용자가 시스템 설정에서 알림을 끄고 SDK가 변경 사항을 보고한 후), 푸시 변경 로그에 "Push token was updated from foreground push enabled to foreground push disabled"와 같은 항목이 포함될 수 있습니다.

새 SDK 데이터를 기대하는 경우(예: 테스트 세션 직후), 값이 오래된 것처럼 보이면 사용자 프로필에서 **새로고침**을 선택하세요. SDK가 데이터를 플러시하고 프로필에 최신 푸시 등록이 반영되기까지 약간의 지연이 있을 수 있습니다.

[내부 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)에 추가한 사용자의 경우, 해당 그룹의 **Internal Group Settings**에서 **Record User Events for group members**를 선택하면 SDK 요청이 로그에 표시됩니다. 그런 다음 **설정** > **이벤트 사용자 로그**에서 [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)를 열고 사용자의 SDK 요청을 찾아 원시 페이로드를 확장합니다. 기기가 원격 알림을 활성화 또는 비활성화로 보고하는지 확인하면서 `remote_notification_enabled`와 같은 필드를 검사할 수 있습니다.

### 세분화 및 푸시 필터 {#segmentation-and-push-filters}

Segment 빌더에서 **`Foreground Push Enabled`**, **`Foreground Push Enabled for App`**, **`Background or Foreground Push Enabled`** 및 푸시 구독 필터와 같은 필터를 사용하여 선호도 및 기기 수준 승인별로 사용자를 타겟팅하거나 감사할 수 있습니다. iOS에서 이러한 필터가 특정 사용자에 대해 어떻게 읽히는지는 OS 프롬프트를 완료했는지, 설정을 변경했는지, 또는 [임시 승인](#provisional-push)을 사용하는지에 따라 달라집니다. [iOS 사용자 동작 및 푸시 상태](#ios-user-actions-push-status) 및 [기타 플랫폼별 시나리오](#foreground-push-enabled)를 참조하세요.

### Campaign 및 Canvas 분석 {#campaign-and-canvas-analytics}

푸시 **Campaign** 또는 **Canvas** 분석 페이지에서 *발송됨*, *반송*, *열람* 등의 측정기준은 해당 발송에 대한 전달 및 인게이지먼트를 반영합니다. 이러한 수치를 개별 프로필과 대조하려면 **Campaign Details** 또는 **Canvas Details**에서 **User Data**(CSV)를 사용하여 수신자를 내보내세요. 단계 및 권한에 대해서는 [Campaign 데이터 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data) 및 [Canvas 데이터 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)를 참조하세요. 분석과 내보내기 간의 수치가 일치하지 않는 경우, 내보내기 문제 해결의 [Campaign 및 Canvas 분석]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting#campaign-and-canvas-analytics)을 참조하세요.

## iOS 사용자 동작 및 푸시 상태 {#ios-user-actions-push-status}

다음 표는 다양한 사용자 동작이 Braze에서 iOS 푸시 활성화, 포그라운드 또는 백그라운드 푸시 등록, 푸시 구독 상태에 어떤 영향을 미치는지 보여줍니다. 사용자가 앱을 설치하고 첫 번째 세션을 시작하면, 일반적으로 첫 번째 행에 표시된 상태가 됩니다. 이후 각 동작은 이러한 값 중 일부를 업데이트할 수 있지만 다른 값은 업데이트하지 않을 수 있습니다.

| 사용자 동작 | `Foreground Push Enabled` | `Foreground Push Enabled for App` | 푸시 등록 유형 | 푸시 구독 상태 |
| --- | --- | --- | --- | --- |
| 사용자가 앱을 설치하고 세션을 기록함 | `false`* | 업데이트되지 않음 | 백그라운드 | `Subscribed` |
| 사용자가 iOS 기본 푸시 프롬프트를 받고 **Allow**를 선택함 | `true` | `true` | 포그라운드 | `Opted-In`** |
| 사용자가 iOS 기본 푸시 프롬프트를 받고 **Don't Allow**를 선택함 | `false` | 업데이트되지 않음 | 백그라운드 | 업데이트되지 않음 |
| 사용자가 기기 설정에서 푸시를 활성화하고 세션을 기록함 | `true` | `true` | 포그라운드 | `Opted-In`** |
| 사용자가 기기 설정에서 푸시를 비활성화하고 세션을 기록함 | `false` | `false` | 백그라운드 | 업데이트되지 않음 |
| 사용자가 앱을 삭제함 | 업데이트되지 않음 | 푸시 토큰 만료 시 업데이트됨 | 푸시 토큰 만료 시 업데이트됨 | 업데이트되지 않음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="iOS 사용자 동작 및 푸시 상태" }

<sup>* 앱이 임시 푸시를 사용하지 않는 경우, 사용자가 푸시 알림을 허용할 때까지 `Foreground Push Enabled`는 `false`입니다. 앱이 임시 푸시를 사용하는 경우, 첫 번째 세션 시작 시 `Foreground Push Enabled`는 `true`입니다. 자세한 내용은 [임시 승인 및 조용한 푸시](#provisional-push)를 참조하세요.</sup>

<sup>** [Braze Swift SDK 버전 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0)부터 `optInWhenPushAuthorized` 구성 속성이 푸시 권한이 승인될 때 푸시 구독 상태를 자동으로 `Opted-In`으로 설정할지 여부를 제어합니다. 자세한 내용은 [푸시 토큰](#push-tokens)을 참조하세요.</sup>

## 푸시 권한 {#push-permission}

모든 푸시 지원 플랫폼(iOS, 웹, Android)은 OS 수준의 시스템 프롬프트를 통한 명시적 옵트인을 요구하며, 다음 섹션에서 설명하는 약간의 차이가 있습니다.

사용자의 결정은 최종적이며 거부 후에는 다시 요청할 수 없으므로, [푸시 프라이머]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) 인앱 메시지를 사용하는 것이 옵트인율을 높이는 중요한 전략입니다.

**기본 OS 푸시 권한 프롬프트**

| 플랫폼 | 스크린샷 | 설명 |
|--|--|--|
| iOS | ![iOS 기본 푸시 프롬프트로 "My App would like to send you notifications"라는 메시지와 하단에 "Don't Allow"와 "Allow" 두 개의 버튼이 표시됩니다.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | [임시 푸시](#provisional-push) 권한을 요청할 때는 적용되지 않습니다. |
| Android | ![Android 푸시 메시지로 "Allow Kitchenerie to send you notifications?"라는 메시지와 하단에 "Allow"와 "Don't allow" 두 개의 버튼이 표시됩니다.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | 이 푸시 권한은 Android 13에서 도입되었습니다. Android 13 이전에는 푸시를 보내는 데 권한이 필요하지 않았습니다. |
| 웹 | ![웹 브라우저의 기본 푸시 프롬프트로 "Braze.com wants to show notification"이라는 메시지와 하단에 "Block"과 "Allow" 두 개의 버튼이 표시됩니다.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="푸시 권한" }

### Android

Android 13 이전에는 푸시 알림을 보내는 데 권한이 필요하지 않았습니다. Android 12 이하에서는 Braze가 자동으로 푸시 토큰을 요청할 때 첫 번째 세션에서 모든 사용자가 `Subscribed`로 간주됩니다. 이 시점에서 사용자는 해당 기기에 대한 유효한 푸시 토큰과 `Subscribed`의 기본 구독 상태로 **푸시 활성화** 상태가 됩니다.

[Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13)부터는 사용자에게 푸시 권한을 요청하고 승인을 받아야 합니다. 앱에서 적절한 시점에 사용자에게 수동으로 권한을 요청할 수 있지만, 그렇지 않으면 앱이 [알림 채널](https://developer.android.com/reference/android/app/NotificationChannel)을 생성할 때 자동으로 프롬프트가 표시됩니다.

### iOS

![시스템 알림 센터의 알림으로 하단에 "Keep receiving notifications from the Yachtr app?"이라는 메시지와 아래에 "Keep" 또는 "Turn Off" 두 개의 버튼이 표시됩니다.]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

앱에서 임시 푸시 또는 승인된 푸시를 요청할 수 있습니다.

승인된 푸시는 알림을 보내기 전에 사용자의 명시적 권한이 필요한 반면, [임시 푸시](https://www.braze.com/resources/articles/mastering-provisional-push)는 소리나 알림 없이 알림 센터에 직접 __조용히__ 알림을 보낼 수 있습니다.

#### 임시 승인 및 조용한 푸시 {#provisional-push}

iOS 12(2018년 출시) 이전에는 모든 사용자가 푸시 알림을 받으려면 명시적으로 옵트인해야 했습니다.

iOS 12에서 Apple은 [임시 승인](https://www.braze.com/resources/articles/mastering-provisional-push)을 도입하여, 브랜드가 사용자가 명시적으로 옵트인하기 전에 사용자의 알림 센터에 조용한 푸시 알림을 보낼 수 있게 했으며, 이를 통해 메시지의 가치를 일찍 보여줄 수 있는 기회를 제공합니다. 자세한 내용은 [임시 승인]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push)을 참조하세요.

### 웹 {#web}

웹의 경우, 기본 브라우저 권한 대화 상자를 통해 명시적인 사용자 옵트인을 요청해야 합니다.

앱에서 언제든지 권한 프롬프트를 표시할 수 있는 iOS 및 Android와 달리, 일부 최신 브라우저는 "사용자 제스처"(마우스 클릭 또는 키 입력)에 의해 트리거된 경우에만 프롬프트를 표시합니다. 사이트가 페이지 로드 시 푸시 알림 권한을 요청하려고 하면 브라우저에 의해 무시되거나 차단될 가능성이 높습니다.

따라서 페이지가 로드될 때 무작위로 요청하는 것이 아니라, 사용자가 웹사이트의 어딘가를 클릭할 때만 권한을 요청해야 합니다.

## 푸시 토큰 {#push-tokens}

[푸시 토큰]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle)은 사용자의 기기에서 생성되어 Braze로 전송되는 고유한 익명 식별자로, 각 수신자의 알림을 어디로 보낼지 식별하는 데 사용됩니다.

[푸시 토큰]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle)을 분류하는 두 가지 방법이 있으며, 이는 사용자에게 푸시 알림을 보내는 방법을 이해하는 데 필수적입니다.

1. **포그라운드 푸시**는 사용자 기기의 포그라운드에 일반적인 가시적 푸시 알림을 보내는 기능을 제공합니다.
2. **백그라운드 푸시**는 특정 기기가 해당 브랜드의 푸시 알림 수신을 옵트인했는지 여부에 관계없이 사용할 수 있습니다. 백그라운드 푸시를 통해 브랜드는 [제거 추적]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)과 같은 핵심 기능을 지원하기 위해 의도적으로 표시되지 않는 알림인 사일런트 푸시 알림을 기기에 보낼 수 있습니다.

사용자 프로필에 앱과 연결된 유효한 포그라운드 푸시 토큰이 있으면, Braze는 해당 사용자를 해당 앱에 대해 "푸시 등록됨"으로 간주합니다. 그러면 Braze는 이러한 사용자를 식별하는 데 도움이 되는 특정 세분화 필터인 `Foreground Push Enabled for App,`을 제공합니다.

{% alert note %}
`Foreground Push Enabled for App` 필터는 해당 앱에 대한 유효한 포그라운드 및 백그라운드 푸시 토큰의 존재만 고려합니다. 그러나 보다 일반적인 [`Foreground Push Enabled`](#foreground-push-enabled) 필터는 워크스페이스 내 모든 앱에 대해 푸시 알림을 명시적으로 활성화한 사용자를 세분화합니다. 이 수에는 포그라운드 푸시만 포함되며 구독을 취소한 사용자는 포함되지 않습니다. 이러한 필터 및 기타 필터에 대한 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.
{% endalert %}

### 하나의 기기에 여러 사용자 {#multiple-users-on-one-device}

푸시 토큰은 기기와 앱 모두에 고유하므로, 동일한 기기를 사용하는 여러 사용자를 구분하는 데 푸시 토큰을 사용할 수 없습니다.

예를 들어, Charlie와 Kim이라는 두 명의 사용자가 있다고 가정합니다. Charlie가 자신의 휴대폰에서 앱의 푸시 알림을 활성화한 상태에서 Kim이 Charlie의 휴대폰을 사용하여 Charlie의 프로필에서 로그아웃하고 자신의 프로필로 로그인하면, 푸시 토큰이 Kim의 프로필로 재할당됩니다. 그러면 Kim이 로그아웃하고 Charlie가 다시 로그인할 때까지 해당 기기에서 푸시 토큰은 Kim의 프로필에 할당된 상태로 유지됩니다.

앱이나 웹사이트는 기기당 하나의 푸시 구독만 가질 수 있습니다. 따라서 사용자가 기기나 웹사이트에서 로그아웃하고 새 사용자가 로그인하면, 푸시 토큰이 새 사용자에게 재할당됩니다. 이는 사용자 프로필의 **Engagement** 탭에 있는 **Contact Settings** 섹션에 반영됩니다:

![사용자 프로필의 Engagement 탭에 있는 푸시 토큰 변경 로그로, 푸시 토큰이 다른 사용자에게 이동된 시점과 해당 토큰이 무엇인지 나열합니다.]({% image_buster /assets/img/push_token_changelog.png %})

푸시 제공업체(APNs/FCM)가 하나의 기기에서 여러 사용자를 구분할 방법이 없기 때문에, 기기에서 푸시 대상으로 지정할 사용자를 결정하기 위해 마지막으로 로그인한 사용자에게 푸시 토큰을 전달합니다.

### 여러 기기와 한 명의 사용자 {#multiple-devices-and-one-user}

푸시 구독 상태는 사용자 기반이며 개별 앱에 특정되지 않습니다. 푸시 구독 상태는 마지막으로 설정된 값입니다. 따라서 사용자가 푸시 알림을 옵트인한 경우, 모든 적격 기기에서 푸시 구독 상태가 `Opted-In`이 됩니다. 사용자가 나중에 애플리케이션이나 브랜드가 제공하는 다른 방법을 통해 푸시 알림 구독을 명시적으로 취소하면, 푸시 구독 상태가 `Unsubscribed`로 업데이트되며 푸시 등록된 기기에서 푸시 알림을 받을 수 없습니다.

## Foreground Push Enabled 필터 {#foreground-push-enabled}

`Foreground Push Enabled`는 Braze의 세분화 필터로, 마케터가 Braze에서 푸시 알림을 보내도록 허용한 사용자와 푸시 알림을 받지 않겠다는 선호를 표현하지 않은 사용자를 쉽게 식별할 수 있게 합니다.

`Foreground Push Enabled` 필터는 다음을 고려합니다:
- Braze가 푸시 알림을 보낼 수 있는 능력(포그라운드 푸시 토큰)
- 사용자의 모든 기기에서 푸시를 받겠다는 전반적인 선호(푸시 구독 상태)

![대시보드에서 사용자가 "Push Registered for Marketing (iOS)"으로 표시된 스크린샷]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

사용자가 워크스페이스 내 앱에 대해 활성 포그라운드 푸시 토큰을 가지고 있으면 "푸시 활성화" 또는 "푸시 등록됨"으로 간주되며, 이는 푸시 활성화 상태가 앱별로 적용됨을 의미합니다.

{% alert note %}
푸시 등록 상태를 확인하는 방법에 대한 자세한 내용은 [푸시 등록 상태]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status)를 참조하세요.
{% endalert %}

## 푸시 등록 및 변경 로그 정보 찾기 {#finding-push-registration-and-changelog-information}

대시보드에서 푸시 등록 및 푸시 변경 로그에 대한 정보를 다음에서 확인할 수 있습니다:

- **세분화** – 사용자의 구독 상태, 활성화 상태, 포그라운드 및 백그라운드 활성화 상태별로 필터링합니다.
- **Campaign 분석** – 단일 Campaign 또는 Canvas에 대한 푸시 통계 및 피드백을 확인합니다.
- **사용자 프로필(Engagement 탭)** – 특정 사용자의 **Contact Settings** 및 푸시 변경 로그를 확인합니다.

푸시 활성화 상태를 검토할 때, **Push Registered for**는 Braze가 해당 사용자에게 포그라운드 푸시를 보낼 수 있는 플랫폼을 나타냅니다. iOS 및 Android에서 사용자가 포그라운드 푸시 활성화에서 백그라운드 푸시 활성화(`remote_notification_enabled`)로 전환된 경우, 푸시 변경 로그에 "Push token was updated from foreground push enabled to foreground push disabled."로 기록됩니다.

사용자가 테스트 사용자로 추가된 경우, **개발자 콘솔** > **이벤트 사용자 로그**에서 사용자 프로필에 `remote_notification_enabled`가 `true` 또는 `false`인 SDK 요청이 표시됩니다. SDK 업데이트가 사용자 프로필에 반영되기까지 약간의 지연이 있으므로, 업데이트를 확인하려면 사용자 프로필을 새로고침해야 할 수 있습니다.

**iOS 푸시 상태에 대한 세분화 필터:**

- **iOS 포그라운드 및 백그라운드 푸시 비활성화:** 사용자에게 아직 푸시 프롬프트가 표시되지 않았습니다.
- **iOS 백그라운드 활성화:** 사용자에게 푸시 프롬프트가 표시되었고 거부했거나, 수락한 후 나중에 기기 설정에서 푸시 알림을 끈 경우입니다(사용자가 세션을 가진 후 반영됨).
- **iOS 포그라운드 활성화:** 사용자에게 푸시 프롬프트가 표시되었고 포그라운드 푸시를 받을 수 있는 상태입니다.

Campaign 분석은 이 섹션의 앞부분에서 설명한 세부 사항에 맞춰 푸시 통계를 인라인으로 반영합니다. Campaign 또는 Canvas에 진입한 사용자 프로필을 다운로드하여 사용자 프로필을 교차 참조할 수도 있습니다.

## 기타 플랫폼별 시나리오 {#other-platform-specific-scenarios}

{% tabs %}
{% tab 웹 %}

사용자가 기본 푸시 권한 프롬프트를 수락하면, 구독 상태가 `opted in`으로 변경됩니다.

구독을 관리하려면 사용자 메서드 [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)을 사용하여 사이트에 선호 설정 페이지를 만든 다음, 대시보드에서 옵트아웃 상태별로 사용자를 필터링할 수 있습니다.

사용자가 브라우저에서 알림을 비활성화하면, 해당 사용자에게 보내는 다음 푸시 알림이 반송되며, Braze는 사용자의 푸시 토큰을 그에 맞게 업데이트합니다. 이는 푸시 활성화 필터(`Background or Foreground Push Enabled`, `Foreground Push Enabled` 및 `Foreground Push Enabled for App`)의 적격성을 관리하는 데 사용됩니다. 사용자 프로필에 설정된 구독 상태는 사용자 수준 설정이며 푸시가 반송될 때 변경되지 않습니다.

### 410 웹 푸시 토큰 오류 {#410-web-push-token-errors} {#410-web-push-token-errors}

`410: Gone` 오류가 발생하면, 사용자가 OS 설정의 브라우저에서 웹 푸시 알림을 비활성화했거나, 동일한 기기에서 다른 사용자로 로그인하고 있거나, 사용자가 한동안 웹사이트를 방문하지 않은 경우에 발생할 수 있습니다.

`410: Endpoint Not Valid` 오류가 발생하면, 웹 푸시 토큰(본질적으로 URL)이 만료되었음을 의미할 수 있습니다. 이는 사용자가 사이트를 다시 방문하지 않거나 브라우저가 토큰을 무효화한 경우에 발생할 수 있습니다. 또한 브라우저에 따라 주기적으로(보통 몇 개월마다) 발생할 수 있습니다. 사용자가 사이트를 다시 방문할 때 브라우저가 여전히 "허용"으로 설정되어 있으면, Braze는 해당 기기에 대한 새로운 토큰을 자동으로 수집합니다. 이는 SDK 초기화 중에 [`disablePushTokenMaintenance` 초기화 옵션](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions)이 사용되지 않는 것을 전제로 합니다.

{% alert note %}
웹 플랫폼은 백그라운드 또는 사일런트 푸시를 허용하지 않습니다.
{% endalert %}
{% endtab %}
{% tab Android %}

포그라운드 푸시가 활성화된 사용자가 OS 설정에서 푸시를 비활성화하면, 다음 세션 시작 시:
- Braze는 해당 사용자를 포그라운드 푸시 비활성화로 표시하고 더 이상 푸시 메시지를 보내려고 시도하지 않습니다.
- `Foreground Push Enabled for App (Android)` 필터와 `Foreground Push Enabled` 세분화 필터(사용자 프로필의 다른 앱에 유효한 포그라운드 푸시 토큰이 없는 경우)는 `false`를 반환합니다.

이 시나리오에서는 백그라운드 푸시 토큰이 여전히 존재하므로, 세분화 필터 `Background or Foreground Push Enabled = true`를 사용하여 백그라운드(사일런트) 푸시 알림을 계속 보낼 수 있습니다.

Android의 경우, Braze는 다음과 같은 경우 사용자를 푸시 비활성화로 간주합니다:

- 사용자가 기기에서 앱을 제거한 경우.
- 반송으로 인해 푸시 메시지 전달에 실패한 경우. 이는 주로 제거로 인해 발생하지만, 앱 업데이트, 새 푸시 토큰 버전 또는 형식으로 인해 발생할 수도 있습니다.
- Firebase Cloud Messaging에 대한 푸시 등록이 실패한 경우(네트워크 연결 불량 또는 FCM에 연결하거나 유효한 토큰을 반환하는 데 실패하여 발생하는 경우가 있음).
- 사용자가 기기 설정에서 앱의 푸시 알림을 차단한 후 세션을 기록한 경우.

{% alert note %}
앱이 포그라운드 또는 백그라운드(아직 실행 중)에 있을 때만 Android 푸시 알림을 가로챌 수 있습니다. 앱이 종료되었거나 완전히 종료된 경우에는 알림을 가로챌 수 없습니다.
{% endalert %}

{% endtab %}
{% tab iOS %}

사용자가 포그라운드 푸시 옵트인 프롬프트를 수락하는지 여부에 관계없이, Xcode에서 원격 알림이 활성화되어 있고 앱이 [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications)를 호출하면 백그라운드 푸시를 보낼 수 있습니다.

앱이 임시 승인을 받았거나 사용자가 푸시를 옵트인한 경우, 포그라운드 푸시 토큰을 받게 되어 모든 유형의 푸시를 보낼 수 있습니다. Braze에서는 포그라운드 푸시가 활성화된 iOS 사용자를 명시적(앱 수준) 또는 임시(기기 수준)로 푸시 활성화된 것으로 간주합니다.

사용자가 OS 수준에서 푸시 알림 수신을 거부하면, 푸시 구독 상태는 `Subscribed`가 되며 프로필에 포그라운드 푸시 토큰이 등록되었다고 표시되지 않습니다.

처음에 OS 수준에서 옵트인한 사용자가 OS 설정에서 푸시 알림을 비활성화하는 시나리오에서는, 다음 세션 시작 시 다음과 같은 일이 발생합니다:
- Braze는 해당 사용자를 포그라운드 푸시 비활성화로 표시하고 더 이상 푸시 메시지를 보내려고 시도하지 않습니다.
- `Foreground Push Enabled for App (iOS)` 필터와 `Foreground Push Enabled` 세분화 필터(사용자 프로필의 다른 앱에 유효한 포그라운드 푸시 토큰이 없는 경우)는 `false`를 반환합니다.

이 시나리오에서는 백그라운드 푸시 토큰이 여전히 존재하므로, 세분화 필터 `Background or Foreground Push Enabled = true`를 사용하여 백그라운드(사일런트) 푸시 알림을 계속 보낼 수 있습니다.

{% alert note %}
iOS는 푸시 알림이 표시되기 전에 앱이 푸시 알림을 가로채는 것을 허용하지 않습니다. 이는 앱(및 Braze)이 알림을 표시하거나 숨길 수 있는지에 대한 제어권이 없음을 의미합니다. 사용자는 기기 설정에서 앱의 푸시 알림을 옵트아웃할 수 있지만, 이는 운영 체제에 의해 제어됩니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## 모범 사례 {#best-practices}

Braze에서 푸시 사용을 최적화하는 방법에 대한 자세한 안내는 [푸시 모범 사례]({{site.baseurl}}/user_guide/channels/push/best_practices) 전용 문서를 참조하세요.