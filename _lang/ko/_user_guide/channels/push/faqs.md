---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "이 문서에서는 푸시 Campaign을 설정할 때 자주 발생하는 질문에 대한 답변을 제공합니다."
page_type: FAQ
channel:
  - Push
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 푸시 채널에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 푸시 알림이 때때로 지연되는 이유는 무엇인가요? {#why-are-push-notifications-sometimes-delayed}

전달은 일반적으로 세 단계를 거칩니다: Braze **처리**(세분화, 스케줄링, 제공업체로의 전달), Braze에서 **APNs 또는 FCM**으로의 전송, 제공업체에서 **기기**로의 전달. 지연은 어느 단계에서든 발생할 수 있습니다. Braze는 제공업체 또는 기기 대기줄에 대한 가시성이 없으므로, 기기 측 타이밍을 좁혀야 할 때는 클라이언트에서 [상세 로깅]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs/)을 사용하세요.

## 여러 사용자가 하나의 기기에 로그인하면 어떻게 되나요? {#what-happens-when-multiple-users-log-into-a-single-device}

사용자가 기기 또는 웹사이트에서 로그아웃하면 다른 사용자가 로그인할 때까지 푸시로 도달할 수 있습니다. 다른 사용자가 로그인하면 푸시 토큰이 새 사용자에게 재할당됩니다. 이는 각 기기가 앱 또는 웹사이트당 하나의 활성 푸시 구독만 가질 수 있기 때문입니다.

푸시 토큰이 재할당되면 고객 프로필의 **푸시 체인지로그**에 변경 사항이 반영됩니다. 고객 프로필의 **참여** 탭에서 확인할 수 있습니다.

!["연락처 설정" 섹션의 "푸시 체인지로그".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

## 테스트 푸시를 보내면 모든 기기로 전송되나요? {#when-i-send-a-test-push-does-it-go-to-all-of-my-devices}

네. 테스트 푸시는 선택한 고객 프로필에 연결된 모든 푸시 활성화 기기로 전송됩니다. 동일한 사용자로 여러 휴대폰이나 태블릿에 로그인한 경우, 유효한 푸시 토큰이 있는 각 기기가 알림을 수신합니다.

테스트 푸시를 하나의 기기로만 보내려면 테스트 전에 고객 프로필에서 다른 기기의 푸시 토큰을 제거할 수 있습니다. 또는 [`/messages/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)로 전송하는 경우, `apple_push` 또는 `android_push` 오브젝트에서 `send_to_most_recent_device_only`를 `true`로 설정하면 가장 최근에 활성화된 기기만 푸시를 수신합니다.

## "페이로드가 유효하지 않아 푸시 전송 오류"는 무엇을 의미하나요? {#what-does-error-sending-push-because-the-payload-was-invalid-mean}

이 메시지는 APNs가 유효하지 않은 페이로드(예: 빈 페이로드 또는 너무 큰 페이로드)로 인해 푸시 요청을 거부했음을 나타냅니다.

자세한 내용과 다음 단계는 [일반적인 푸시 오류 메시지]({{site.baseurl}}/user_guide/channels/push/push_error_codes/)를 참조하세요.

## 옵트인한 사용자에게 푸시 토큰이 없는 이유는 무엇인가요? {#why-doesnt-an-opted-in-user-have-a-push-token}

이는 사용자의 푸시 토큰이 동일한 기기를 사용한 다른 사용자에게 재할당된 경우 발생할 수 있습니다.

1. 영향을 받은 사용자 프로필의 **참여** 탭에서 **푸시 체인지로그**로 이동합니다.
2. 푸시 토큰이 다른 사용자에게 이동되었다는 메시지를 찾습니다.
3. 푸시 토큰을 복사하여 사용자 검색 바에 붙여넣습니다.
4. 푸시 토큰이 아직 존재하면 해당 기기에서 가장 최근에 로그인한 사용자로 이동됩니다.

푸시 토큰을 원래 사용자에게 재할당하려면:

1. 원래 사용자가 누락된 푸시 토큰이 있는 프로필에 로그인하도록 합니다.
2. 새 푸시 전송을 트리거합니다. 기기 수준에서 푸시가 여전히 활성화되어 있으면 토큰이 해당 계정으로 다시 이동됩니다.

## 초안 Campaign을 테스트할 때 "모바일 앱 내에서 웹 URL 열기"가 항상 앱을 여는 이유는 무엇인가요? {#why-does-open-web-url-inside-mobile-app-always-open-the-app-when-im-testing-a-draft-campaign}

Campaign이 아직 **초안** 상태이고 테스트 푸시를 보내면, **모바일 앱 내에서 웹 URL 열기** 옵션의 선택 여부와 관계없이 알림을 탭하면 항상 앱이 먼저 열립니다. Campaign이 **라이브** 상태이면 클릭 시 동작이 설정대로 작동합니다.

**앱 내** 옵션 없이 **웹 URL 열기**를 선택한 경우, 링크는 기기의 기본 브라우저에서 직접 열립니다. **모바일 앱 내에서 웹 URL 열기**를 선택한 경우, 링크는 인앱 웹 뷰에서 열립니다.

## iOS 푸시 인증서에서 "프로덕션으로 전송"과 "개발로 전송"의 차이점은 무엇인가요? {#what-is-the-difference-between-send-to-production-and-send-to-development-for-ios-push-certificates}

Braze에서 Apple 푸시 인증서를 추가할 때, **프로덕션으로 전송**과 **개발로 전송** 옵션은 Braze가 푸시 알림을 전달하는 데 사용하는 APNs(Apple Push Notification service) 게이트웨이를 결정합니다.

- **개발로 전송:** 앱이 Xcode에서 개발 모드로 빌드되고 개발 프로비저닝 프로필로 서명된 경우 선택합니다. 푸시 알림은 Apple의 개발(샌드박스) 게이트웨이를 통해 라우팅됩니다.
- **프로덕션으로 전송:** 앱이 Apple의 TestFlight, App Store 또는 엔터프라이즈 배포를 통해 배포되는 경우 선택합니다. 푸시 알림은 Apple의 프로덕션 게이트웨이를 통해 라우팅됩니다.

잘못된 옵션을 선택하면 푸시 토큰 유형이 게이트웨이와 일치하지 않아 푸시 알림이 자동으로 실패합니다. 일반적으로 TestFlight 또는 App Store를 통해 배포된 앱은 **프로덕션으로 전송**을 사용해야 합니다.

## "포그라운드 푸시 활성화됨"과 "백그라운드 또는 포그라운드 푸시 활성화됨" 필터의 차이점은 무엇인가요? {#what-is-the-difference-between-the-foreground-push-enabled-and-background-or-foreground-push-enabled-filters}

이 세분화 필터는 서로 다른 조건을 확인합니다.

| 필터 | 확인 내용 | 사용 사례 |
|--------|---------------|----------|
| **포그라운드 푸시 활성화됨** | 사용자에게 유효한 포그라운드 푸시 토큰이 있고 **그리고** 푸시 구독 상태가 `Opted-In` 또는 `Subscribed`인 경우. | 표시되는 푸시 알림을 수신할 수 있는 사용자를 타겟팅합니다. |
| **백그라운드 또는 포그라운드 푸시 활성화됨** | 사용자에게 푸시 토큰(포그라운드 또는 백그라운드)이 있고 **그리고** 푸시 구독 상태가 `Opted-In` 또는 `Subscribed`인 경우. 여기에는 표시되는 푸시 알림을 비활성화했지만 백그라운드 푸시 토큰이 있는 사용자가 포함됩니다. | [제거 추적]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/), [사일런트 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent/), 지오펜싱에 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="포그라운드 푸시 활성화됨과 백그라운드 또는 포그라운드 푸시 활성화됨 필터의 차이점" }

사용자가 `포그라운드 푸시 활성화됨` 없이 `백그라운드 또는 포그라운드 푸시 활성화됨`일 수 있습니다. 이는 사용자가 기기 설정에서 표시되는 푸시 알림을 비활성화했지만 앱이 여전히 백그라운드 푸시 토큰을 보유하고 있는 경우 발생합니다. 자세한 내용은 [푸시 사용자 및 구독]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled)을 참조하세요.

## Braze는 푸시 메시지가 성공적으로 전송되었는지 어떻게 판단하나요? {#how-does-braze-determine-when-a-push-message-is-sent-successfully}

메시지는 푸시 서비스 제공업체가 수신하는 즉시 전송된 것으로 기록됩니다. 이는 사용자가 메시지를 수신하거나 확인했음을 반드시 의미하지는 않습니다.

iOS의 경우 푸시 서비스 제공업체는 Apple Push Notification Service(APNs)이고, Android의 경우 일반적으로 Firebase Cloud Messaging(FCM)입니다. 푸시 서비스 제공업체는 성공 또는 실패로 즉시 응답합니다. 실패에는 반송 또는 네트워크 장애로 인한 재시도가 포함될 수 있습니다.

성공 메시지가 반환되면 Braze에서 전송이 기록된 후, 푸시 서비스가 기기로 전달을 시도합니다. 기기에 즉시 도달할 수 없는 경우, 서비스는 Braze에서 설정된 만료 옵션(Android의 경우 **TTL**, iOS의 경우 **만료**)까지 재시도합니다. 메시지가 시간 초과되면 푸시 서비스가 푸시를 폐기하지만, 반송으로 간주되지는 않습니다.

- 실행 기반 전달 푸시 Campaign의 경우, 사용자가 Campaign을 트리거하는 동작을 수행하는 즉시 메시지 전송이 기록됩니다.
- 스케줄된 Campaign의 경우, 전송 시간은 메시지가 대기줄에 추가되어 푸시 서비스 제공업체에 전달된 시간입니다.
- 두 전달 유형 모두, 사용자가 아직 푸시를 보거나 수신하지 않았더라도 Braze 및 고객 프로필의 **수신한 Campaigns**에 "전송됨"으로 표시됩니다.

대시보드의 푸시 "전달" 측정기준은 페이지 로드 시 전송 수에서 반송 수를 뺀 값으로 계산됩니다.