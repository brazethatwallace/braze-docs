---
page_order: 10.9
nav_title: 문제 해결
article_title: Braze SDK의 푸시 알림 문제 해결
description: "증상 색인, 표준 조사 경로 및 플랫폼별 SDK 점검을 사용하여 푸시 알림 전달 및 표시 문제를 진단합니다."
channel:
  - push notifications
---

# 푸시 알림 문제 해결 {#troubleshoot-push-notifications}

> 이 페이지를 사용하여 기기에서 푸시 알림 전달 및 표시 문제를 진단하세요. 대시보드 측 전달 점검(구독 상태, Segment, 한도)에 대해서는 [푸시 문제 해결]({{site.baseurl}}/user_guide/channels/push/troubleshooting)을 참조하세요.

디버깅하기 전에 [테스트 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)로 자신을 추가하고 [테스트 메시지 발송]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages)을 검토하세요.

## 시작하기: 증상 매칭 {#start-here-match-your-symptom}

아래 표에서 겪고 있는 증상을 찾아 해당 섹션의 단계를 따르세요. 어느 섹션에 해당하는지 확실하지 않은 경우 [표준 조사 경로](#standard-investigation-path)를 사용하세요.

| 증상 | 이동 |
| --- | --- |
| 특정 플랫폼에서 푸시가 수신되지 않음 | [플랫폼별 문제 해결](#platform-specific-troubleshooting)에서 SDK 탭을 선택하세요 |
| Liquid 태그 주변의 줄바꿈이 저장 시 잘못 표시됨 | [푸시 알림의 줄바꿈](#push-linebreaks) |
| 대시보드 전달 확인(가입, Segment, 한도) | [푸시 문제 해결]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| 푸시의 딥링크가 올바르게 열리지 않음 | [딥링킹 문제 해결]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| 일반적인 푸시 오류 코드 | [일반적인 푸시 오류 메시지]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 SDK 증상" }

## 표준 조사 경로 {#standard-investigation-path}

모든 푸시 알림 인시던트에 대해 이 워크플로를 사용하세요. 1단계부터 시작하세요.

1. 기기에 유효한 푸시 토큰이 있고 기기 설정에서 푸시 권한이 허용되어 있는지 확인하세요.
2. 대시보드에서 테스트 사용자가 Campaign 또는 Canvas [Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment)에 해당하고 [대조군]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status)에 포함되어 있지 않은지 확인하세요.
3. 테스트 기기로 [테스트 푸시]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages)를 발송하세요.
4. [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)하고, 문제를 재현한 다음, [SDK 탭](#platform-specific-troubleshooting)에서 플랫폼별 안내를 확인하세요.
5. 문제가 지속되면 상세 로그, 플랫폼, SDK 버전, Campaign 또는 Canvas ID를 첨부하여 [Braze 고객지원]({{site.baseurl}}/braze_support)에 문의하세요.

## 플랫폼별 문제 해결 {#platform-specific-troubleshooting}

SDK 탭을 선택하여 플랫폼별 설정 및 표시 확인 사항을 확인하세요.

{% sdktabs %}
{% sdktab web %}
## 문제 해결 {#troubleshooting}

푸시 알림 설정 후 문제가 발생하는 경우 다음 사항을 확인하세요:

- 웹 푸시 알림을 사용하려면 사이트가 HTTPS여야 합니다.
- 모든 브라우저가 푸시 메시지를 수신할 수 있는 것은 아닙니다. 브라우저에서 `braze.isPushSupported()`가 `true`를 반환하는지 확인하세요.
- Firefox 등 일부 브라우저는 푸시 알림에 이미지를 표시하지 않습니다. 브라우저 지원에 대한 자세한 내용은 [MDN Notification 이미지 문서](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image)를 참조하세요.
- 사용자가 사이트의 푸시 접근을 거부한 경우, 브라우저 환경설정에서 거부 상태를 제거하지 않는 한 권한 요청 프롬프트가 다시 표시되지 않습니다.

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
## Braze/APN 워크플로 이해 {#understanding-the-brazeapns-workflow}

Apple 푸시 알림 서비스(APN)는 Apple 플랫폼에서 실행되는 애플리케이션에 푸시 알림을 전송하기 위한 인프라입니다. 다음은 사용자의 기기에 대해 푸시 알림이 활성화되고 Braze가 푸시 알림을 전송하는 간략한 구조입니다:

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### 1단계: 푸시 인증서 및 프로비저닝 프로필 구성 {#step-1-configuring-the-push-certificate-and-provisioning-profile}

앱을 개발하려면 푸시 알림을 활성화하기 위한 SSL 인증서를 생성해야 합니다. 이 인증서는 앱이 빌드되는 프로비저닝 프로필에 포함되며, Braze 대시보드에도 업로드해야 합니다. 이 인증서를 통해 Braze는 사용자를 대신하여 푸시 알림을 전송할 권한이 있음을 APN에 알릴 수 있습니다.

[프로비저닝 프로필](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) 및 인증서에는 개발용과 배포용 두 가지 유형이 있습니다. 혼동을 피하기 위해 배포 프로필과 인증서만 사용하는 것을 권장합니다. 개발용과 배포용으로 다른 프로필과 인증서를 사용하는 경우, 대시보드에 업로드된 인증서가 현재 사용 중인 프로비저닝 프로필과 일치하는지 확인하세요.

{% alert warning %}
푸시 인증서 환경(개발 대 프로덕션)을 변경하지 마세요. 푸시 인증서를 잘못된 환경으로 변경하면 사용자의 푸시 토큰이 실수로 제거되어 푸시로 도달할 수 없게 될 수 있습니다.
{% endalert %}

### 2단계: 기기가 APN에 등록하고 Braze에 푸시 토큰 제공 {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

사용자가 앱을 열면 푸시 알림을 수락하라는 프롬프트가 표시됩니다. 이 프롬프트를 수락하면 APN이 해당 기기에 대한 푸시 토큰을 생성합니다. Swift SDK는 기본 [자동 플러시 정책]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing)을 사용하는 앱에 대해 즉시 비동기적으로 푸시 토큰을 전송합니다. 푸시 토큰이 사용자와 연결되면, 대시보드의 고객 프로필 **인게이지먼트** 탭에서 "푸시 등록됨"으로 표시되며 Braze Campaigns에서 푸시 알림을 받을 수 있게 됩니다.

{% alert note %}
macOS 13부터 특정 기기에서는 Xcode 14에서 실행되는 iOS 16 시뮬레이터에서 푸시 알림을 테스트할 수 있습니다. 자세한 내용은 [Xcode 14 릴리스 노트](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)를 참조하세요.
{% endalert %}

#### 푸시 토큰 생성 관련 고려 사항 {#considerations-for-push-token-generation}

- 사용자가 다른 기기에 앱을 설치하면 Braze는 같은 방식으로 다른 토큰을 생성하고 캡처합니다.
- 사용자가 앱을 재설치하면 SDK가 새 토큰을 생성하여 Braze에 전달합니다. 그러나 APN과 Braze는 원래 토큰을 여전히 유효한 것으로 기록할 수 있습니다.
- 사용자가 앱을 삭제하면 Braze는 즉시 알림을 받지 못하며, APN이 해당 토큰을 폐기할 때까지 토큰은 유효한 것으로 나타납니다.
- 어느 시점에서 APN이 오래된 토큰을 폐기합니다. Braze는 이 과정을 제어하거나 확인할 수 없습니다.

### 3단계: Braze 푸시 Campaign 실행 {#step-3-launching-a-braze-push-campaign}

푸시 Campaign이 실행되면 Braze는 메시지를 전달하기 위해 APN에 요청합니다. 구체적으로, **사용자의 가장 최근 기기로 전송**이 선택되지 않는 한 각 현재 유효한 푸시 토큰에 대해 요청이 APN으로 전달됩니다. Braze가 APN으로부터 성공 응답을 받으면 고객 프로필에 성공적인 전달을 기록하지만, 다음과 같은 이유로 사용자가 실제 메시지를 받지 못할 수 있습니다:
- 기기의 전원이 꺼져 있는 경우.
- 기기가 인터넷(Wi-Fi 또는 셀룰러)에 연결되어 있지 않은 경우.
- 최근에 앱을 삭제한 경우.

Braze는 대시보드에 업로드된 SSL 푸시 인증서를 사용하여 인증하고 제공된 푸시 토큰에 대해 푸시 알림을 전송할 권한이 있는지 확인합니다. 기기가 온라인 상태이면 Campaign이 전송된 후 얼마 지나지 않아 알림을 수신해야 합니다. Braze는 기본 APN [만료 날짜](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)를 알림에 대해 30일로 설정합니다.

### 4단계: 유효하지 않은 토큰 제거 {#step-4-removing-invalid-tokens}

[APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)이 메시지를 전송하려던 푸시 토큰 중 유효하지 않은 것이 있다고 알려주면, 해당 토큰을 연결된 고객 프로필에서 제거합니다.

{% alert note %}
토큰이 등록 해제되었더라도 APN이 처음에는 성공 상태를 반환하는 것은 정상입니다. APN은 토큰 무효화 이벤트를 즉시 보고하지 않기 때문입니다. APN은 사용자 개인정보를 보호하고 앱 삭제 추적을 방지하기 위해 무작위 일정에 따라 유효하지 않은 토큰에 대한 `410` 상태 반환을 의도적으로 지연합니다. APN이 `410` 상태를 반환할 때까지 등록 해제된 토큰으로 알림을 계속 전송할 수 있습니다.
{% endalert %}

## 푸시 오류 로그 사용 {#using-the-push-error-logs}

[메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab)를 통해 Campaign 및 발송과 관련된 메시지(특히 오류 메시지)를 확인할 수 있으며, 푸시 알림 오류도 포함됩니다. 이 오류 로그는 Campaign이 예상대로 작동하지 않는 이유를 파악하는 데 매우 유용한 다양한 경고를 제공합니다. 오류 메시지를 선택하면 특정 인시던트를 해결하는 데 도움이 되는 관련 설명서로 리디렉션됩니다.

![오류가 발생한 시간, 앱 이름, 채널, 오류 유형 및 오류 메시지를 표시하는 푸시 오류 로그.]({% image_buster /assets/img_archive/message_activity_log.png %})

여기에서 볼 수 있는 일반적인 오류에는 ["등록 해제된 푸시 토큰으로 전송 수신"](#swift_received-unregistered-sending)과 같은 사용자별 알림이 포함됩니다.

또한, Braze는 고객 프로필의 **인게이지먼트** 탭에서 푸시 체인지로그도 제공합니다. 이 체인지로그는 토큰 무효화, 푸시 등록 오류, 토큰이 새 사용자에게 이동되는 것 등 푸시 등록 동작에 대한 인사이트를 제공합니다.

![Braze 고객 프로필 인게이지먼트 탭에서 푸시 등록 체인지로그를 표시합니다.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### 메시지 활동 로그 오류 {#message-activity-log-errors}

#### 등록 해제된 푸시 토큰으로 전송 수신 {#received-unregistered-sending}

- `AppDelegate.braze?.notifications.register(deviceToken:)` 메서드에서 Braze로 전송되는 푸시 토큰이 유효한지 확인하세요. **메시지 활동 로그**에서 푸시 토큰을 확인할 수 있습니다. `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`와 같이 문자와 숫자가 혼합된 긴 문자열이어야 합니다. 푸시 토큰이 다르게 보이면 Braze에 푸시 토큰을 전송하는 [코드]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-32-register-push-tokens-with-braze)를 확인하세요.
- 푸시 프로비저닝 프로필이 테스트 중인 환경과 일치하는지 확인하세요. 유니버설 인증서는 Braze 대시보드에서 개발 또는 프로덕션 APN 환경 중 하나로 전송하도록 구성할 수 있습니다. 프로덕션 앱에 개발 인증서를 사용하거나 개발 앱에 프로덕션 인증서를 사용하면 동작하지 않습니다.
 - Braze에 업로드한 푸시 토큰이 푸시 토큰을 전송한 앱을 빌드할 때 사용한 프로비저닝 프로필과 일치하는지 확인하세요.

#### 토픽에 해당하지 않는 기기 토큰 {#device-token-not-for-topic}

APN은 푸시 토큰이 자격 증명에 구성된 토픽(번들 ID)과 일치하지 않을 때 `DeviceTokenNotForTopic`(HTTP 상태 400)을 반환합니다. Braze는 이를 **메시지 활동 로그** 또는 푸시 전달 로그에서 `DeviceTokenNotForTopic`으로 표시할 수 있습니다.

불일치를 해결하려면:

1. 앱의 **번들 ID**가 Braze의 **앱 번들 ID**와 일치하는지 확인하세요(**설정** > **앱 설정** > **푸시 알림 설정**).
2. 앱을 빌드하는 데 사용한 프로비저닝 프로필에 해당 번들 ID에 대한 푸시 기능이 포함되어 있는지 확인하세요.
3. Braze에 업로드된 푸시 자격 증명이 앱의 환경(개발 대 프로덕션)과 일치하는지 확인하세요.
4. `.p8` 키의 경우, Braze의 **Team ID**와 **Key ID**가 Apple Developer 계정과 일치하는지 확인하세요.
5. 자격 증명이 교체되었거나 취소된 경우 유효한 `.p8` 키 또는 `.p12` 인증서를 다시 업로드하세요.

가능하면 `.p8` 인증 키를 사용하는 것을 권장합니다. 자격 증명 유형 및 대시보드 상태 표시기에 대해서는 [.p8 인증 키로 마이그레이션]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key)을 참조하세요.

#### 푸시 토큰으로 전송 시 BadDeviceToken {#baddevicetoken-sending-to-push-token}

`BadDeviceToken`은 APN 오류 코드이며 Braze에서 발생하는 것이 아닙니다. 이 응답이 반환되는 데는 다음과 같은 여러 가지 이유가 있을 수 있습니다:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## 푸시 등록 문제 {#push-registration-issues}

### 푸시 등록 프롬프트가 표시되지 않음 {#no-push-registration-prompt}

애플리케이션이 푸시 알림 등록을 요청하는 프롬프트를 표시하지 않는 경우, 푸시 등록 통합에 문제가 있을 수 있습니다. [설명서]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)를 따르고 푸시 등록을 올바르게 통합했는지 확인하세요. 코드에 브레이크포인트를 설정하여 푸시 등록 코드가 실행되고 있는지 확인할 수도 있습니다.

### 대시보드에 "푸시 등록됨" 사용자가 표시되지 않음(메시지 전송 전) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

앱이 푸시 알림을 허용하도록 올바르게 구성되어 있는지 확인하세요. 확인해야 할 일반적인 실패 지점은 다음과 같습니다:

- 앱이 푸시 알림 허용 프롬프트를 표시하는지 확인하세요. 일반적으로 이 프롬프트는 앱을 처음 열 때 나타나지만, 다른 곳에서 나타나도록 프로그래밍할 수도 있습니다. 예상하는 위치에 나타나지 않으면 앱의 푸시 기능 기본 구성에 문제가 있을 수 있습니다.
  - [푸시 통합]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 단계가 성공적으로 완료되었는지 확인하세요.
  - 앱이 빌드된 프로비저닝 프로필에 푸시 권한이 포함되어 있는지 확인하세요. Apple 개발자 계정에서 사용 가능한 모든 프로비저닝 프로필을 가져오고 있는지 확인하세요. 이를 확인하려면 다음 단계를 수행하세요:
    1. Xcode에서 **Preferences > Accounts**로 이동하세요(또는 키보드 단축키 <kbd>Command</kbd>+<kbd>,</kbd> 사용).
    2. 개발자 계정에 사용하는 Apple ID를 선택하고 **View Details**를 클릭하세요.
    3. 다음 페이지에서 **<i class="fas fa-redo-alt" aria-label="새로고침"></i> Refresh**를 클릭하고 사용 가능한 모든 프로비저닝 프로필을 가져오고 있는지 확인하세요.
- 앱에서 [푸시 기능을 올바르게 활성화]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities)했는지 확인하세요.
- 푸시 프로비저닝 프로필이 테스트 중인 환경과 일치하는지 확인하세요. 유니버설 인증서는 Braze 대시보드에서 개발 또는 프로덕션 APN 환경 중 하나로 전송하도록 구성할 수 있습니다. 프로덕션 앱에 개발 인증서를 사용하거나 개발 앱에 프로덕션 인증서를 사용하면 동작하지 않습니다.
- 코드에 브레이크포인트를 설정하여 `registerPushToken` 메서드를 호출하고 있는지 확인하세요.
- 기기를 사용하여 테스트하고 있는지(푸시는 시뮬레이터에서 동작하지 않음) 네트워크 연결이 양호한지 확인하세요.

## 푸시 알림이 전송되었지만 사용자 기기에 표시되지 않음 {#push-notifications-sent-but-not-displayed-on-users-devices}

### "푸시 등록됨" 사용자가 메시지 전송 후 더 이상 활성화되지 않음 {#push-registered-users-no-longer-enabled-after-sending-messages}

사용자의 푸시 토큰이 유효하지 않을 가능성이 높습니다. 이는 여러 가지 이유로 발생할 수 있습니다:

#### 대시보드와 앱 인증서 불일치 {#dashboard-and-app-certificate-mismatch}

대시보드에 업로드한 푸시 인증서가 앱이 빌드된 프로비저닝 프로필에 있는 것과 동일하지 않으면 APN이 토큰을 거부합니다. 올바른 인증서를 업로드했는지 확인하고 다른 테스트 알림을 시도하기 전에 앱에서 다른 세션을 완료하세요.

#### 애플리케이션이 삭제됨 {#application-was-uninstalled}

사용자가 애플리케이션을 삭제한 경우, 푸시 토큰이 유효하지 않게 되며 다음 전송 시 제거됩니다.

#### 프로비저닝 프로필 재생성 {#regenerating-your-provisioning-profile}

최후의 수단으로, 처음부터 새로 시작하여 완전히 새로운 프로비저닝 프로필을 생성하면 여러 환경, 프로필 및 앱을 동시에 작업할 때 발생하는 구성 오류를 해결할 수 있습니다. 푸시 알림 설정에는 많은 "움직이는 부분"이 있으므로 때로는 처음부터 다시 시도하는 것이 가장 좋습니다. 이렇게 하면 문제 해결을 계속해야 하는 경우 문제를 격리하는 데도 도움이 됩니다.

### "푸시 등록됨" 사용자에게 메시지가 전달되지 않음 {#messages-not-delivered-to-push-registered-users}

#### 앱이 포그라운드에 있음 {#app-is-foregrounded}

`UserNotifications` 프레임워크를 통해 푸시를 통합하지 않은 iOS 버전에서는 푸시 메시지가 수신될 때 앱이 포그라운드에 있으면 표시되지 않습니다. 테스트 메시지를 전송하기 전에 테스트 기기에서 앱을 백그라운드로 전환해야 합니다.

#### 테스트 알림이 잘못 예약됨 {#test-notification-scheduled-incorrectly}

테스트 메시지에 설정한 스케줄을 확인하세요. 현지 시간대 전달 또는 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing)으로 설정된 경우, 아직 메시지를 받지 못했을 수 있습니다(또는 메시지를 받았을 때 앱이 포그라운드에 있었을 수 있습니다).

### 테스트 중인 앱에 대해 사용자가 "푸시 등록됨" 상태가 아님 {#user-not-push-registered-for-the-app-being-tested}

테스트 메시지를 전송하려는 사용자의 고객 프로필을 확인하세요. **인게이지먼트** 탭에 "푸시 가능한 앱" 목록이 있어야 합니다. 테스트 메시지를 전송하려는 앱이 이 목록에 있는지 확인하세요. 사용자는 워크스페이스의 어떤 앱에 대해서든 푸시 토큰이 있으면 "푸시 등록됨"으로 표시되므로 이는 일종의 거짓 양성일 수 있습니다.

다음은 푸시 등록에 문제가 있거나 사용자의 토큰이 푸시 후 APN에 의해 유효하지 않은 것으로 반환되었음을 나타냅니다:

![연락처 설정을 표시하는 고객 프로필. 푸시 아래에 "앱 없음"이 표시됩니다.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## 푸시 클릭이 기록되지 않음 {#push-clicks-not-logged}

- [푸시 통합 단계]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling)를 따랐는지 확인하세요.
- Braze는 포그라운드에서 자동으로 수신된 푸시 알림을 처리하지 않습니다(`UserNotifications` 프레임워크 이전의 기본 포그라운드 푸시 동작). 이는 링크가 열리지 않고 푸시 클릭이 기록되지 않음을 의미합니다. 앱이 아직 `UserNotifications` 프레임워크를 통합하지 않은 경우, 애플리케이션 상태가 `UIApplicationStateActive`일 때 Braze는 푸시 알림을 처리하지 않습니다. 앱이 [푸시 처리 메서드]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) 호출을 지연하지 않는지 확인하세요. 그렇지 않으면 Swift SDK가 푸시 알림을 자동 포그라운드 푸시 이벤트로 처리하고 핸들링하지 않을 수 있습니다.

## 딥링크가 작동하지 않음 {#deep-links-not-working}

유니버설 링크, 커스텀 스킴, 이메일 및 Branch와 같은 서드파티 제공업체를 포함한 모든 채널에 대한 종합적인 문제 해결은 [딥링킹 문제 해결]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)을 참조하세요.

### 푸시 클릭의 웹 링크가 열리지 않음 {#web-links-from-push-clicks-not-opening}

푸시 알림의 링크가 웹 뷰에서 열리려면 ATS를 준수해야 합니다. 웹 링크가 HTTPS를 사용하는지 확인하세요. 자세한 내용은 [ATS 준수]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats)를 참조하세요.

### 푸시 클릭의 딥링크가 열리지 않음 {#deep-links-from-push-clicks-not-opening}

딥링크를 처리하는 대부분의 코드는 푸시 오픈도 처리합니다. 먼저 푸시 오픈이 기록되고 있는지 확인하세요. 기록되지 않는다면 해당 문제를 해결하세요(해결 방법이 링크 처리도 함께 해결하는 경우가 많습니다).

오픈이 기록되고 있다면 딥링크 자체의 문제인지 아니면 딥링킹 푸시 클릭 처리의 문제인지 확인하세요. 이를 위해 인앱 메시지 클릭에서 딥링크가 작동하는지 테스트하세요.

### Push Stories 이미지 탭이 동작하지 않음 {#push-story-image-taps-do-nothing}

Push Stories 이미지를 탭해도 아무 동작이 없는 경우, Notification Content Extension의 `Info.plist`를 열어 `UNNotificationExtensionUserInteractionEnabled`가 `YES`인지 확인하세요. Swift SDK의 `BrazePushStory` 모듈은 확장이 탭을 수신하기 위해 해당 키가 필요합니다. [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift)를 참조하세요.

{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
## 문제 해결

### 태스크 스위처에서 앱을 닫은 후 푸시가 표시되지 않음 {#push-doesnt-appear-after-app-is-closed-from-task-switcher}

태스크 스위처에서 앱을 닫은 후 푸시 알림이 더 이상 나타나지 않는 경우, 앱이 디버그 모드일 가능성이 높습니다. .NET MAUI는 디버그 모드에서 프로세스가 종료된 후 앱이 푸시를 수신하지 못하게 하는 스캐폴딩을 추가합니다. 릴리스 모드에서 앱을 실행하면 태스크 스위처에서 앱을 닫은 후에도 푸시를 받을 수 있습니다.

### 커스텀 알림 팩토리가 올바르게 설정되지 않음 {#custom-notification-factory-not-being-set-correctly}

커스텀 알림 팩토리(및 모든 델리게이트)는 C#과 Java 간에 올바르게 작동하려면 [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/)를 확장해야 합니다. 자세한 내용은 Java 인터페이스 구현에 대한 [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) 문서를 참조하세요.

{% endsdktab %}
{% endsdktabs %}

## 푸시 알림의 줄 바꿈 {#push-linebreaks}

Liquid 태그를 사용하여 푸시 알림을 작성할 때, Liquid 태그에 인접한 줄 바꿈은 메시지가 전송되기 전에 자동으로 제거됩니다. [푸시 알림 작성기]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)에서는 편집 중 메시지의 가독성을 유지하기 위해 이러한 줄 바꿈이 다시 추가됩니다. 메시지를 저장할 때 Liquid 태그 주변에 줄 바꿈이 표시되는 경우, 이는 정상적인 동작입니다.