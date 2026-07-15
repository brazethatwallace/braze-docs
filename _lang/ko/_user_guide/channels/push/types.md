---
nav_title: "메시지 유형"
article_title: 푸시 메시지 유형
page_order: 3
page_type: reference
description: "이 참조 문서에서는 Braze를 통해 보낼 수 있는 다양한 푸시 알림 유형을 나열합니다."
channel: push
---

# 푸시 메시지 유형 {#push-message-types}

> 고객과 상호작용하는 데 사용할 수 있는 다양한 유형의 푸시 알림이 있습니다. 이러한 설정의 대부분은 푸시 Campaign에서 구성할 수 있지만, 일부는 설명에 명시된 대로 백엔드 구성이 필요합니다.

## 표준 푸시 {#standard-push}

가장 포괄적인 푸시 메시지입니다. 알림 소리와 함께 사용자의 기기에 표시되며, 메시지가 슬라이드되거나 알림 바 또는 스택에 나타납니다.

**지원 플랫폼:** 웹, Android, iOS

자세한 내용은 [푸시 메시지 만들기]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)를 참조하세요.

## 웹 푸시 {#web-push}

이 푸시 메시지는 웹 앱 또는 브라우저에 표시됩니다. 고객에게 도달하려면 권한이 필요합니다. 사용자가 숨김 브라우저를 사용하는 경우 웹 푸시는 작동하지 않습니다.

**지원 플랫폼:** 웹

자세한 내용은 [웹 푸시 알림]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)을 참조하세요.

## 푸시 프라이머 Campaign {#push-primer-campaigns}

사용자로부터 명시적인 푸시 옵트인 또는 옵트아웃 신호를 얻기 위해 사용되는 인앱 메시지 Campaign입니다. 프라이머를 통해 기기 설정에서 푸시를 끌 가능성이 높은 사용자에게 알림을 보내는 것을 방지할 수 있습니다. iOS의 경우, 사용자가 iOS의 기본 푸시 프롬프트에 명시적으로 옵트인할 때까지 포그라운드 푸시 알림(기기를 깨우는 알림 등)이 활성화되지 않으므로 푸시 Campaign이 중요합니다.

**지원 플랫폼:** 웹, Android, iOS

자세한 내용은 [푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)를 참조하세요.

## Push Stories

Push Stories는 캐러셀 형태의 시각적 여정을 통해 사용자를 안내하는 몰입형 메시지입니다. 모바일 기기에서만 사용할 수 있습니다.

**지원 플랫폼:** iOS, Android

자세한 내용은 [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)를 참조하세요.

## 푸시 실행 버튼 {#push-with-action-buttons}

푸시 실행 버튼은 사용자에게 옵션을 제공하고 여러 행동 유도를 할 수 있는 메시지입니다.

**지원 플랫폼:** 웹, Android, iOS

자세한 내용은 [푸시 실행 버튼]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons)을 참조하세요.

## 리치 푸시 알림 {#rich-push-notifications}

리치 푸시 알림은 아이콘과 행동 유도 텍스트를 넘어 확장할 수 있는 몰입형 이미지와 크리에이티브 콘텐츠가 포함된 알림입니다.

**지원 플랫폼:** iOS, Android

자세한 내용은 [iOS용 리치 알림 만들기]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications) 또는 [Android용 리치 알림 만들기]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications)를 참조하세요.

## iOS 임시 푸시 알림 {#provisional-push-notifications-for-ios}

Apple이 iOS 12에서 도입한 임시 승인은 iOS 앱 설치 시 자동으로 발생하며, 브랜드가 사용자에게 푸시 프롬프트를 표시하지 않고도 무음 알림을 보낼 수 있게 합니다. 무음 푸시가 전송되어 기기의 알림 트레이에서 확인되면, 사용자에게 푸시 알림을 허용하거나 중단할 수 있는 옵션이 제공됩니다.

**지원 플랫폼:** iOS

자세한 내용은 [iOS 알림 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push)을 참조하세요.

## HTML 푸시 알림 {#html-push-notifications}

HTML 푸시 알림은 Braze에서 제공하는 사전 설정된 푸시 템플릿을 사용하지 않고 HTML로 하드코딩된 푸시 메시지입니다. HTML 푸시 알림을 만들 수 있는 옵션을 통해 회사는 이러한 푸시 메시지의 외관에 대해 완전한 크리에이티브 자유와 일관된 브랜딩을 가질 수 있습니다.

**지원 플랫폼:** Android

## 알림 ID 및 채널 ID {#notification-ids-and-channel-ids}

알림 ID와 채널 ID를 사용하면 사용자가 이미 수신했지만 아직 열지 않은 푸시 알림을 교체하거나 업데이트할 수 있습니다.

**지원 플랫폼:** iOS, Android

자세한 내용은 [알림 채널]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels) 및 [고급 푸시 Campaign 설정]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings)을 참조하세요.

## 백그라운드 또는 무음 푸시 알림 {#background-push-notifications}

기기에 렌더링되지 않는 푸시 알림입니다. 일반적으로 백그라운드 프로세스 및 제거 추적을 위해 앱에 정보 패킷을 전송하는 데 사용됩니다. 백그라운드 또는 무음 푸시를 보내려면 백그라운드 지원 푸시 토큰이 필요합니다.

**지원 플랫폼:** 웹, Android, iOS

자세한 내용은 [무음 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent)을 참조하세요.

## 웨어러블 푸시 알림 {#wearable-push-notifications}

이 푸시 알림을 통해 브랜드는 Apple Watch와 같은 웨어러블 기기에 직접 메시지를 보낼 수 있습니다.

**지원 플랫폼:** iOS