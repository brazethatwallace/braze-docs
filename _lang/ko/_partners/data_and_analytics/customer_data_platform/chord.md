---
nav_title: Chord
article_title: Chord
description: "Chord 고객 데이터 플랫폼(CDP)을 Braze에 연결하여 이커머스 이벤트와 ID 업데이트를 메시징, 세분화, 여정에 전달합니다."
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> [Chord](https://www.chord.co/)는 이커머스 스토어프론트에서 이벤트를 캡처하고 표준화하는 고객 데이터 플랫폼을 제공합니다. Chord를 Braze에 연결하면 구매 활동, 행동 이벤트, ID 업데이트가 Braze로 전달되어 파이프라인을 직접 구축하지 않고도 Campaign(캠페인)을 트리거하고 프로필을 최신 상태로 유지할 수 있습니다.

_이 통합은 Chord에서 유지 관리합니다._

설정, 연결 옵션, 필드 목록에 대한 자세한 내용은 [Chord Braze 통합](https://docs.chord.co/braze#chord-x-braze-integration)을 참조하세요.

## 통합 소개 {#about-the-integration}

Chord는 스토어와 Braze 사이의 데이터 레이어 역할을 합니다. Chord CDP에서 Braze를 대상으로 연결하면 Chord가 추적 계획의 이벤트를 Braze에 매핑합니다. 이 데이터를 Segments, Canvases, 메시지 개인화에 활용하여 소비자가 사이트에서 수행하는 활동을 반영할 수 있습니다.

## 필수 조건 {#prerequisites}

Chord와 Braze를 연결하기 전에 다음 사항을 확인하세요.

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Chord 계정 | 이 통합을 사용하려면 Chord 계정이 필요합니다. |
| Braze API 자격 증명 | 필요한 자격 증명은 [연결 모드](#connection-modes)에 따라 다릅니다. 클라우드 모드는 Braze REST API 키를 사용합니다. 디바이스 모드는 Braze SDK용 웹 채널 API 키를 사용하며, 이는 REST API 키와 별개입니다. |
| Braze REST 엔드포인트 | Chord는 서버 측 데이터를 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 및 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 엔드포인트로 전송합니다. 기본 URL은 Braze 인스턴스에 따라 달라집니다(예: `https://rest.iad-01.braze.com`). 자세한 내용은 [Braze REST API 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## 연결 모드 {#connection-modes}

Chord는 클라우드 모드(Braze REST API를 통한 서버 간 호출)와 디바이스 모드(Chord가 Braze 웹 SDK를 초기화하고 매핑된 호출을 전달)를 지원합니다. 전체 웹 SDK 기능(예: 인앱 메시지)이 필요한지 또는 서버 측 이벤트 전달만 필요한지에 따라 모드를 선택하세요.

### 클라우드 모드 {#cloud-mode}

1. Chord 데이터 플랫폼에서 CDP를 열고 **Destinations**로 이동합니다.
2. 대상 옆의 **Add**를 선택하고 카탈로그에서 **Braze**를 선택한 다음 대상 이름과 Braze REST API 키를 입력합니다.
3. 대상을 생성하여 연결을 완료합니다.

Braze 대시보드에서 **설정** > **API 키**로 이동하여 REST API 키를 생성합니다. 이전 탐색을 사용하는 경우 **개발자 콘솔** > **API 설정**으로 이동합니다. Chord에서 워크스페이스에 대해 다른 요구 사항을 문서화하지 않는 한, 키에는 `users.track` 및 `users.identify` 권한이 필요합니다. 자세한 내용은 [API 키]({{site.baseurl}}/api/api_key/)를 참조하세요.

### 디바이스 모드 {#device-mode}

1. Chord 데이터 플랫폼에서 CDP를 열고 **Destinations**로 이동합니다.
2. 대상 옆의 **Add**를 선택하고 카탈로그에서 **Braze (device mode)**를 선택한 다음 대상 이름과 웹 채널 API 키를 입력합니다.
3. 대상을 생성하여 연결을 완료합니다.

Braze 대시보드에서 **설정** > **앱 설정** > **Web** > **API Key**에서 웹 채널 API 키를 사용합니다. 디바이스 모드에는 REST API 키를 사용하지 마세요.

### 디바이스 모드 구성 {#device-mode-configuration}

Chord 대상 설정에서 다음을 구성합니다.

- **Braze 웹 SDK 버전:** Chord는 CDP에서 선택 가능한 SDK 버전을 제공합니다. 사용 가능한 범위는 Chord 설명서에서 확인하세요.
- **SDK 엔드포인트:** Braze 인스턴스와 일치해야 합니다. 자세한 내용은 [API 및 SDK 엔드포인트]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)를 참조하세요.
- **이벤트 및 SDK 옵션:** 예를 들어, 전송할 추적 또는 식별 동작, 페이지 이벤트 처리, 인앱 메시지 동작, SDK 초기화 타이밍, 동의 관련 설정 등이 있습니다.

## 이벤트 매핑(디바이스 모드) {#event-mapping-device-mode}

디바이스 모드를 사용하면 Chord가 다음 표와 같이 이벤트를 Braze에 매핑합니다.

| Chord | Braze |
| ----- | ----- |
| Order completed | `logPurchase` |
| 기타 `track` 이벤트 | `logCustomEvent` |
| Identify | 사용자 업데이트(예: SDK 사용자 오브젝트를 통한 속성) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Chord 추적 계획에 포함되고 Braze 대상에 대해 구성된 이벤트만 전달됩니다.

## 통합 사용 {#using-the-integration}

### 1단계: Braze에서 이벤트 확인 {#step-1-confirm-events-in-braze}

데이터가 전달되기 시작하면 Braze에서 고객 프로필 또는 이벤트 도구를 열어 이벤트와 속성이 예상대로 도착하는지 확인합니다.

### 2단계: 오디언스 및 여정 구축 {#step-2-build-audiences-and-journeys}

동기화된 이벤트와 속성을 [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), Campaign에서 활용하여 스토어 행동을 기반으로 소비자를 타겟팅합니다.

## 활용 사례 {#use-cases}

- **구매 후 메시징:** Chord가 완료된 주문을 수신하면 확인, 교차 판매 또는 리뷰 요청을 트리거합니다.
- **프로필 보강:** Chord의 최신 소비자 프로필 데이터로 Braze 속성을 동기화하여 더 깔끔한 세분화를 유지합니다.
- **행동 리타겟팅:** Chord 행동 이벤트를 사용하여 최근에 구매하지 않았거나 전환하지 않은 소비자를 다시 참여시킵니다.

## 고려 사항 {#considerations}

{% alert important %}
다른 도구가 이미 동일한 이벤트를 Braze에 전송하고 있는 경우, Chord CDP를 통해 Braze를 연결하기 전에 해당 통합의 담당자와 조율하세요. 병렬 대상을 실행하면 다운스트림에서 중복 이벤트가 발생할 수 있습니다.
{% endalert %}

## 문제 해결 {#troubleshooting}

이벤트가 Braze에 표시되지 않는 경우:

1. Chord CDP에서 소스로부터 라이브 이벤트가 도착하고 있는지 확인합니다.
2. Braze 대상이 인스턴스에 맞는 올바른 API 키, SDK 버전(디바이스 모드), REST 또는 SDK 엔드포인트를 사용하고 있는지 확인합니다.
3. 대상이 Chord에서 예상되는 소스에 연결되어 있는지 확인합니다.
4. Chord에서 API 대상 또는 함수 로그를 검토하여 `/users/track` 및 `/users/identify`에 대한 호출이 성공했는지 확인한 다음 Braze에서 다시 확인합니다.

Chord 관련 로그 위치 및 UI 단계에 대해서는 [Chord Braze 통합](https://docs.chord.co/braze#chord-x-braze-integration)을 참조하세요.