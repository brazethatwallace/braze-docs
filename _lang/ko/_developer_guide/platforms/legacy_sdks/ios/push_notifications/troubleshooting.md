---
nav_title: 문제 해결
article_title: iOS용 푸시 알림 문제 해결
platform: iOS
page_order: 30
description: "이 참조 문서에서는 iOS 푸시 구현 시 잠재적인 문제 해결 주제를 다룹니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 문제 해결 {#push-troubleshooting}

## Braze/APNs 워크플로 이해하기 {#understanding-the-brazeapns-workflow}

Apple Push Notification service(APNs)는 iOS 및 OS X 애플리케이션에 푸시 알림을 전송하기 위한 Apple의 인프라입니다. 다음은 사용자의 기기에서 푸시 알림이 활성화되는 방법과 Braze가 푸시 알림을 전송하는 방법에 대한 간략한 구조입니다.

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### 1단계: 푸시 인증서 및 프로비저닝 프로필 구성 {#step-1-configuring-the-push-certificate-and-provisioning-profile}

앱을 개발할 때 푸시 알림을 활성화하기 위한 SSL 인증서를 생성합니다. 이 인증서는 앱이 빌드될 때 사용되는 프로비저닝 프로필에 포함되며, Braze 대시보드에도 업로드해야 합니다. 이 인증서를 통해 Braze가 APNs에 사용자를 대신하여 푸시 알림을 보낼 수 있는 권한이 있음을 알릴 수 있습니다.

[프로비저닝 프로필](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html)과 인증서에는 개발용과 배포용 두 가지 유형이 있습니다. 혼동을 피하기 위해 배포용 프로필과 인증서만 사용하는 것을 권장합니다. 개발용과 배포용에 서로 다른 프로필과 인증서를 사용하는 경우, 대시보드에 업로드된 인증서가 현재 사용 중인 프로비저닝 프로필과 일치하는지 확인하세요.

{% alert warning %}
푸시 인증서 환경(개발용 vs 프로덕션)을 변경하지 마세요. 푸시 인증서를 잘못된 환경으로 변경하면 사용자의 푸시 토큰이 실수로 제거되어 푸시를 통해 도달할 수 없게 될 수 있습니다.
{% endalert %}

#### 2단계: 기기가 APNs에 등록하고 Braze에 푸시 토큰을 제공 {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

사용자가 앱을 열면 푸시 알림 수락 여부를 묻는 메시지가 표시됩니다. 이 메시지를 수락하면 APNs가 해당 기기에 대한 푸시 토큰을 생성합니다. iOS SDK는 기본 [자동 플러시 정책]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing)을 사용하는 앱에 대해 즉시 비동기적으로 푸시 토큰을 전송합니다. 사용자와 연결된 푸시 토큰이 확보되면 대시보드의 고객 프로필에서 **인게이지먼트** 탭 아래에 "Push Registered"로 표시되며, Braze Campaigns에서 푸시 알림을 받을 수 있게 됩니다.

{% alert note %}
Xcode 14부터 iOS 시뮬레이터에서 원격 푸시 알림을 테스트할 수 있습니다.
{% endalert %}

#### 3단계: Braze 푸시 Campaign 시작 {#step-3-launching-a-braze-push-campaign}

푸시 Campaign이 시작되면 Braze가 APNs에 메시지 전달을 요청합니다. Braze는 대시보드에 업로드된 SSL 푸시 인증서를 사용하여 제공된 푸시 토큰에 푸시 알림을 보낼 수 있는 권한이 있는지 인증하고 확인합니다. 기기가 온라인 상태인 경우 Campaign이 발송된 직후 알림을 수신해야 합니다. Braze는 알림의 기본 APNs [만료 날짜](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)를 30일로 설정합니다.

#### 4단계: 유효하지 않은 토큰 제거 {#step-4-removing-invalid-tokens}

[APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)가 메시지를 전송하려던 푸시 토큰 중 유효하지 않은 토큰이 있다고 알려주면, 해당 토큰을 연결된 고객 프로필에서 제거합니다.

## 푸시 오류 로그 활용하기 {#utilizing-the-push-error-logs}

Braze는 **메시지 활동 로그**에서 푸시 알림 오류 로그를 제공합니다. 이 오류 로그는 Campaigns이 예상대로 작동하지 않는 이유를 파악하는 데 매우 유용한 다양한 경고를 제공합니다. 오류 메시지를 선택하면 특정 인시던트를 해결하는 데 도움이 되는 관련 설명서로 리디렉션됩니다.

![오류 발생 시간, 앱 이름, 채널, 오류 유형 및 오류 메시지를 표시하는 푸시 오류 로그.]({% image_buster /assets/img_archive/message_activity_log.png %})

여기에서 볼 수 있는 일반적인 오류에는 ["Received Unregistered Sending to Push Token"](#received-unregistered-sending)과 같은 사용자별 알림이 포함됩니다.

또한 Braze는 고객 프로필의 **인게이지먼트** 탭에서 푸시 체인지로그도 제공합니다. 이 체인지로그는 토큰 무효화, 푸시 등록 오류, 토큰이 새 사용자로 이동되는 것 등 푸시 등록 동작에 대한 인사이트를 제공합니다.

![푸시 체인지로그 애니메이션 예시.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## 푸시 등록 문제 {#push-registration-issues}

앱의 푸시 등록 로직에 검증을 추가하려면 [푸시 단위 테스트]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests)를 구현하세요.

### 푸시 등록 프롬프트가 표시되지 않음 {#no-push-registration-prompt}

앱에서 푸시 알림 등록 프롬프트가 표시되지 않는 경우, 푸시 등록 통합에 문제가 있을 가능성이 높습니다. [설명서]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)를 따랐는지 확인하고 푸시 등록이 올바르게 통합되었는지 확인하세요. 코드에 중단점을 설정하여 푸시 등록 코드가 실행되고 있는지 확인할 수도 있습니다.

#### 대시보드에 "푸시 등록됨" 사용자가 표시되지 않음 {#no-push-registered-users-showing-in-the-dashboard}

- 앱에서 푸시 알림을 허용하라는 프롬프트가 표시되는지 확인하세요. 일반적으로 이 프롬프트는 앱을 처음 열 때 나타나지만, 다른 위치에서 나타나도록 프로그래밍할 수도 있습니다. 프롬프트가 표시되어야 할 위치에 나타나지 않는 경우, 앱의 푸시 기능 기본 구성에 문제가 있을 수 있습니다.
  - [푸시 통합]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) 단계가 성공적으로 완료되었는지 확인하세요.
  - 앱이 빌드된 프로비저닝 프로필에 푸시 권한이 포함되어 있는지 확인하세요. Apple 개발자 계정에서 사용 가능한 모든 프로비저닝 프로필을 가져오고 있는지 확인하세요. 이를 확인하려면 다음 단계를 수행하세요:
    1. Xcode에서 **Preferences > Accounts**로 이동합니다(또는 키보드 단축키 <kbd>Command</kbd>+<kbd>,</kbd>를 사용합니다).
    2. 개발자 계정에 사용하는 Apple ID를 선택하고 **View Details**를 클릭합니다.
    3. 다음 페이지에서 **<i class="fas fa-redo-alt"></i> Refresh**를 클릭하고 사용 가능한 모든 프로비저닝 프로필을 가져오고 있는지 확인합니다.
- 앱에서 [푸시 기능을 올바르게 활성화]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-2-enable-push-capabilities)했는지 확인하세요.
- 푸시 프로비저닝 프로필이 테스트 중인 환경과 일치하는지 확인하세요. 유니버설 인증서는 Braze 대시보드에서 개발 또는 프로덕션 APN 환경 중 하나로 보내도록 구성할 수 있습니다. 프로덕션 앱에 개발 인증서를 사용하거나 개발 앱에 프로덕션 인증서를 사용하면 작동하지 않습니다.
- 코드에 중단점을 설정하여 `registerPushToken` 메서드를 호출하고 있는지 확인하세요.
- 기기에서 테스트하고 있는지(시뮬레이터에서는 푸시가 작동하지 않습니다) 네트워크 연결 상태가 양호한지 확인하세요.

## 기기에서 푸시 알림을 받지 못하는 경우 {#devices-not-receiving-push-notifications}

### 푸시 알림 발송 후 사용자가 더 이상 "푸시 등록됨" 상태가 아닌 경우 {#users-no-longer-push-registered-after-sending-a-push-notification}

이는 사용자의 푸시 토큰이 유효하지 않음을 나타낼 가능성이 높습니다. 이 문제는 여러 가지 이유로 발생할 수 있습니다.

#### 대시보드와 앱 인증서 불일치 {#dashboard-and-app-certificate-mismatch}

대시보드에 업로드한 푸시 인증서가 앱을 빌드할 때 사용한 프로비저닝 프로필의 인증서와 동일하지 않으면, APN이 토큰을 거부합니다. 올바른 인증서를 업로드했는지 확인하고, 다른 테스트 알림을 시도하기 전에 앱에서 다른 세션을 완료하세요.

##### 앱 삭제 {#uninstalls}

사용자가 앱을 삭제한 경우, 해당 사용자의 푸시 토큰은 유효하지 않게 되며 다음 발송 시 제거됩니다.

##### 프로비저닝 프로필 재생성 {#regenerating-your-provisioning-profile}

최후의 수단으로, 처음부터 다시 시작하여 완전히 새로운 프로비저닝 프로필을 생성하면 여러 환경, 프로필 및 앱을 동시에 작업할 때 발생하는 구성 오류를 해결할 수 있습니다. iOS 앱의 푸시 알림 설정에는 많은 "움직이는 부분"이 있으므로, 때로는 처음부터 다시 시도하는 것이 가장 좋습니다. 이렇게 하면 추가 문제 해결이 필요한 경우 문제를 분리하는 데에도 도움이 됩니다.

#### 푸시 알림 발송 후에도 사용자가 여전히 "푸시 등록됨" 상태인 경우 {#users-still-push-registered-after-sending-a-push-notification}

##### 앱이 포그라운드 상태 {#app-is-foregrounded}

`UserNotifications` 프레임워크를 통해 푸시를 통합하지 않은 iOS 버전에서는 푸시 메시지가 수신될 때 앱이 포그라운드에 있으면 알림이 표시되지 않습니다. 테스트 메시지를 보내기 전에 테스트 기기에서 앱을 백그라운드로 전환해야 합니다.

##### 테스트 알림 스케줄이 잘못 설정됨 {#test-notification-scheduled-incorrectly}

테스트 메시지에 설정한 스케줄을 확인하세요. 현지 시간대 전달 또는 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)으로 설정된 경우, 메시지를 아직 받지 못했거나 수신 시 앱이 포그라운드 상태였을 수 있습니다.

#### 테스트 중인 앱에 대해 사용자가 "푸시 등록됨" 상태가 아닌 경우 {#user-not-push-registered-for-the-app-being-tested}

테스트 메시지를 보내려는 사용자의 고객 프로필을 확인하세요. **인게이지먼트** 탭 아래에 "푸시 가능한 앱" 목록이 표시됩니다. 테스트 메시지를 보내려는 앱이 이 목록에 있는지 확인하세요. 사용자가 워크스페이스의 아무 앱에 대한 푸시 토큰이 있으면 "푸시 등록됨"으로 표시되므로, 이는 일종의 거짓 양성일 수 있습니다.

다음과 같은 경우는 푸시 등록에 문제가 있거나, 푸시 발송 후 사용자의 토큰이 APN에 의해 유효하지 않은 것으로 반환되었음을 나타냅니다.

![사용자의 연락처 설정을 표시하는 고객 프로필. 여기에서 푸시가 등록된 앱을 확인할 수 있습니다.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## 푸시 메시지가 발송되지 않음 {#push-messages-not-sending}

발송되지 않는 푸시 알림을 해결하려면 [푸시 문제 해결]({{site.baseurl}}/user_guide/channels/push/troubleshooting)을 참조하세요.

## 메시지 활동 로그 오류 {#message-activity-log-errors}

### 등록되지 않은 푸시 토큰으로 발송 수신됨 {#received-unregistered-sending}

- `[[Appboy sharedInstance] registerPushToken:]` 메서드에서 Braze로 전송되는 푸시 토큰이 유효한지 확인하세요. **메시지 활동 로그**에서 푸시 토큰을 확인할 수 있습니다. 푸시 토큰은 `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`과 같이 문자와 숫자가 혼합된 긴 문자열이어야 합니다. 푸시 토큰이 이와 다르게 보인다면, Braze에 푸시 토큰을 전송하는 [코드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze)를 확인하세요.
- 푸시 프로비저닝 프로필이 테스트 중인 환경과 일치하는지 확인하세요. 유니버설 인증서는 Braze 대시보드에서 개발 또는 프로덕션 APN 환경으로 발송하도록 구성할 수 있습니다. 프로덕션 앱에 개발 인증서를 사용하거나 개발 앱에 프로덕션 인증서를 사용하면 작동하지 않습니다.
 - Braze에 업로드한 푸시 토큰이 푸시 토큰을 전송한 앱을 빌드하는 데 사용한 프로비저닝 프로필과 일치하는지 확인하세요.

#### Device token not for topic {#device-token-not-for-topic}

이 오류는 앱의 푸시 인증서와 번들 ID가 일치하지 않음을 나타냅니다. Braze에 업로드한 푸시 인증서가 푸시 토큰을 전송한 앱을 빌드하는 데 사용한 프로비저닝 프로필과 일치하는지 확인하세요.

#### BadDeviceToken 푸시 토큰 발송 오류 {#baddevicetoken-sending-to-push-token}

`BadDeviceToken`은 APN 오류 코드이며 Braze에서 발생하는 것이 아닙니다. 이 응답이 반환되는 데는 다음을 포함하여 여러 가지 이유가 있을 수 있습니다:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## 푸시 전달 후 발생하는 문제 {#issues-after-push-delivery}

앱의 푸시 처리를 검증하려면 [푸시 단위 테스트]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests)를 구현하세요.

### 푸시 클릭이 기록되지 않음 {#push-clicks-not-logged}

- iOS 10에서만 발생하는 경우, [iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling)용 푸시 통합 단계를 따랐는지 확인하세요.
- Braze는 포그라운드에서 자동으로 수신된 푸시 알림을 처리하지 않습니다(예: `UserNotifications` 프레임워크 이전의 기본 포그라운드 푸시 동작). 이 경우 링크가 열리지 않고 푸시 클릭도 기록되지 않습니다. 앱이 아직 `UserNotifications` 프레임워크를 통합하지 않은 경우, 앱 상태가 `UIApplicationStateActive`일 때 Braze는 푸시 알림을 처리하지 않습니다. 앱이 [푸시 처리 메서드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling) 호출을 지연시키지 않도록 해야 합니다. 그렇지 않으면 iOS SDK가 푸시 알림을 무음 포그라운드 푸시 이벤트로 취급하여 처리하지 않을 수 있습니다.

#### 푸시 클릭의 웹 링크가 열리지 않음 {#web-links-from-push-clicks-not-opening}

iOS 9 이상에서는 웹 뷰에서 열리려면 링크가 ATS를 준수해야 합니다. 웹 링크에 HTTPS를 사용하고 있는지 확인하세요. 자세한 내용은 [ATS 준수]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#app-transport-security-ats) 문서를 참조하세요.

#### 푸시 클릭의 딥링크가 열리지 않음 {#deep-links-from-push-clicks-not-opening}

딥링크를 처리하는 코드 대부분은 푸시 열람도 함께 처리합니다. 먼저 푸시 열람이 기록되고 있는지 확인하세요. 기록되지 않으면 [해당 문제를 해결](#push-clicks-not-logged)하세요(해당 수정이 링크 처리 문제도 함께 해결하는 경우가 많습니다).

열람이 기록되고 있다면, 딥링크 자체의 문제인지 딥링킹 푸시 클릭 처리의 문제인지 확인하세요. 이를 확인하려면 인앱 메시지 클릭에서 딥링크가 작동하는지 테스트하세요.

#### 직접 열람이 거의 없거나 전혀 없음 {#few-or-no-direct-opens}

한 명 이상의 사용자가 iOS 푸시 알림을 열었지만 Braze에 *직접 열람*이 거의 또는 전혀 기록되지 않는 경우, [SDK 통합]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)에 문제가 있을 수 있습니다. *직접 열람*은 테스트 발송이나 무음 푸시 알림에 대해서는 기록되지 않는다는 점을 기억하세요.

- 메시지가 [무음 푸시 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications#sending-silent-push-notifications)으로 발송되고 있지 않은지 확인하세요. 무음으로 간주되지 않으려면 메시지의 제목이나 본문에 텍스트가 포함되어야 합니다.
- [푸시 통합 가이드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)에서 다음 단계를 다시 확인하세요:
   - [푸시 등록]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns): 모든 앱 실행 시, 가급적 `application:didFinishLaunchingWithOptions:` 내에서 3단계의 코드가 실행되어야 합니다. `UNUserNotificationCenter.current()`의 delegate 속성정보가 `UNUserNotificationCenterDelegate`를 구현하고 `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` 메서드를 포함하는 객체에 할당되어야 합니다.
   - [푸시 처리 활성화]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling): `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` 메서드가 구현되었는지 확인하세요.

### Push Stories 이미지 클릭이 작동하지 않음 {#push-story-image-clicks-do-nothing}

이 섹션은 OBJECTIVE-C SDK Push Stories 통합에 적용됩니다. SWIFT SDK `BrazePushStory` 모듈을 사용하는 경우 `UNNotificationExtensionUserInteractionEnabled`를 `YES`로 설정하세요. [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift)를 참조하세요.

Push Stories 이미지를 탭해도 예상 동작이 실행되지 않는 경우, Notification Content Extension `Info.plist`를 열고 [Push Stories 설정]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/push_story)의 키와 일치시키세요:

- `UNNotificationExtensionCategory` = `ab_cat_push_story_v2`
- `UNNotificationExtensionDefaultContentHidden` = `YES`
- `UNNotificationExtensionInitialContentSizeRatio` = `0.65`

해당 plist에 `UNNotificationExtensionUserInteractionEnabled`가 있으면 제거하세요. OBJECTIVE-C Push Stories 설정에는 해당 키가 포함되지 않습니다.