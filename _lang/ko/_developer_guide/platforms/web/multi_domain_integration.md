---
nav_title: 멀티 도메인 통합
article_title: Braze 웹 SDK 멀티 도메인 통합
platform: Web
page_order: 23
page_type: reference
description: "API 키 전략, 푸시 설정, 세션 동작 등 여러 도메인에서 Braze 웹 SDK를 구현하는 방법을 알아보세요."
---

# 멀티 도메인 통합 {#multi-domain-integration}

> 여러 웹 도메인에서 Braze 웹 SDK를 통합하는 방법을 알아보세요.

구현이 여러 도메인에 걸쳐 있는 경우, 브라우저 Origin 경계가 Braze 웹 SDK의 사용자 상태 저장 및 읽기 방식에 영향을 미칩니다.

## 앱 및 API 키 전략 선택 {#choose-an-app-and-api-key-strategy}

하나의 웹 SDK API 키를 여러 도메인에서 사용할 수 있지만, 대부분의 경우 동일한 워크스페이스 내에서 별도의 앱에 매핑된 별도의 API 키를 사용하는 것이 더 나은 제어를 제공합니다.

| 전략 | 권장 상황 | 트레이드오프 |
|---|---|---|
| **별도 앱 (권장)** | 도메인별로 독립적인 타겟팅, 리포팅, Campaign 제어가 필요한 경우 | 두 개의 앱 통합을 관리해야 합니다 |
| **단일 앱** | 두 도메인을 운영상 하나의 속성으로 취급하는 경우 | 세션 트리거와 도메인 수준 리포팅을 분리하기 어렵습니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="앱 및 API 키 전략 옵션" }

하나의 워크스페이스에서 별도의 앱을 사용하면, 앱 필터를 활용하여 도메인별로 더 깔끔한 세분화와 메시지 타겟팅이 가능합니다.

## 하나의 도메인에서 푸시 알림 구성 {#configure-push-notifications-on-one-domain}

별도의 루트 도메인의 경우, 웹 푸시 등록은 도메인별로 격리됩니다.

- 하나의 도메인을 푸시 알림 도메인으로 선택하세요.
- 동일한 사용자 여정에서 두 루트 도메인 모두에 푸시를 등록하지 마세요. 이렇게 하면 프롬프트 및 구독 동작이 충돌할 수 있습니다.

## 도메인 간 사용자를 일관되게 식별 {#identify-users-consistently-across-domains}

기본적으로 각 루트 도메인은 자체 SDK 상태를 저장합니다. 도메인 간 활동을 동일한 Braze 고객 프로필에 연결하려면 다음을 수행하세요.

- 로그인 후 각 도메인에서 동일한 `external_id`로 [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)를 호출하세요.
- 별도의 API 키를 사용하는 경우 두 앱을 동일한 워크스페이스에 유지하세요.

일반적인 사용자 ID 가이드는 [Braze SDK를 통한 사용자 ID 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)을 참조하세요.

## 도메인별 이벤트 및 트리거 동작 계획 {#plan-event-and-trigger-behavior-by-domain}

이벤트와 트리거를 모델링하는 방법은 앱 전략에 따라 달라집니다.

- **도메인 간 단일 앱:** 도메인별 커스텀 이벤트를 기록하여 세분화 및 트리거링에서 사이트별 동작을 구분할 수 있도록 하세요.
- **별도 앱:** 도메인별 타겟팅 및 분석을 위해 앱 필터를 사용하는 것이 좋습니다.

## 도메인 간 세션 동작 이해 {#understand-session-behavior-across-domains}

기본적으로 웹 SDK 세션 타임아웃은 비활성 상태 30분입니다. 하나의 앱/API 키를 사용하는 별도의 루트 도메인의 경우:

- 각 도메인은 독립적으로 세션을 시작하고 종료합니다.
- 두 도메인 간을 이동하는 사용자는 겹치는 세션을 생성할 수 있습니다.
- 세션 시작 트리거가 두 도메인 모두에서 실행될 수 있습니다.

기본 세션 수명 주기에 대한 자세한 내용은 [Braze SDK를 통한 세션 추적]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)을 참조하세요.