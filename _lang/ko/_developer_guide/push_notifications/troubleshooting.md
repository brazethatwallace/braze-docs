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

아래 표에서 겪고 있는 문제를 찾아 해당 섹션의 단계를 따르세요. 어떤 섹션이 해당되는지 확실하지 않은 경우 [표준 조사 경로](#standard-investigation-path)를 사용하세요.

| 증상 | 이동 |
| --- | --- |
| 특정 플랫폼에서 푸시가 수신되지 않음 | [플랫폼별 문제 해결](#platform-specific-troubleshooting)에서 SDK 탭을 선택하세요 |
| 저장 시 Liquid 태그 주위의 줄바꿈이 잘못 표시됨 | [푸시 알림의 줄바꿈](#push-linebreaks) |
| 대시보드 전달 확인(가입, Segment, 한도) | [푸시 문제 해결]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| 푸시의 딥링크가 올바르게 열리지 않음 | [딥링킹 문제 해결]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| 일반적인 푸시 오류 코드 | [일반적인 푸시 오류 메시지]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 SDK 증상" }

## 표준 조사 경로 {#standard-investigation-path}

모든 푸시 알림 인시던트에 대해 이 워크플로를 사용하세요. 1단계부터 시작하세요.

1. 기기에 유효한 푸시 토큰이 있고 기기 설정에서 푸시 권한이 허용되어 있는지 확인하세요.
2. 대시보드에서 테스트 사용자가 Campaign 또는 Canvas [Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment)에 해당하며 [대조군]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status)에 포함되어 있지 않은지 확인하세요.
3. 테스트 기기에 [테스트 푸시]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages)를 발송하세요.
4. [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)하고, 문제를 재현한 후 [SDK 탭](#platform-specific-troubleshooting)에서 플랫폼별 가이드를 확인하세요.
5. 문제가 지속되면 상세 로그, 플랫폼, SDK 버전, Campaign 또는 Canvas ID를 포함하여 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.

## 푸시 클릭이 기록되지 않음 {#push-clicks-not-logged}

- [푸시 통합 단계]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling)를 따랐는지 확인하세요.
- Braze는 포그라운드에서 자동으로 수신된 푸시 알림을 처리하지 않습니다(`UserNotifications` 프레임워크 이전의 기본 포그라운드 푸시 동작). 이는 링크가 열리지 않고 푸시 클릭이 기록되지 않음을 의미합니다. 앱이 아직 `UserNotifications` 프레임워크를 통합하지 않은 경우, 애플리케이션 상태가 `UIApplicationStateActive`일 때 Braze는 푸시 알림을 처리하지 않습니다. 앱이 [푸시 처리 메서드]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) 호출을 지연하지 않는지 확인하세요. 그렇지 않으면 Swift SDK가 푸시 알림을 자동 포그라운드 푸시 이벤트로 처리하고 핸들링하지 않을 수 있습니다.

## 푸시 알림의 줄 바꿈 {#push-linebreaks}

Liquid 태그를 사용하여 푸시 알림을 작성할 때, Liquid 태그에 인접한 줄 바꿈은 메시지가 전송되기 전에 자동으로 제거됩니다. [푸시 알림 작성기]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)에서는 편집 중 메시지의 가독성을 유지하기 위해 이러한 줄 바꿈이 다시 추가됩니다. 메시지를 저장할 때 Liquid 태그 주변에 줄 바꿈이 표시되는 경우, 이는 정상적인 동작입니다.