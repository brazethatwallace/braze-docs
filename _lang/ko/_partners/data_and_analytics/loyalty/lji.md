---
nav_title: GRAVTY®
article_title: GRAVTY® 로열티 플랫폼
description: "이 문서에서는 Braze와 GRAVTY® 간의 파트너십에 대해 설명합니다. GRAVTY®는 엔터프라이즈급 로열티 플랫폼으로, 브랜드가 데이터 중심 로열티 프로그램을 설계, 관리, 확장하여 고객 참여와 리텐션을 강화할 수 있도록 지원합니다."
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# GRAVTY® 로열티 플랫폼 {#gravty-loyalty-platform}

> [GRAVTY®](https://www.lji.io/)는 Loyalty Juggernaut Inc.(LJI)의 엔터프라이즈급 로열티 플랫폼으로, 리테일, 여행, 레스토랑(퀵서비스 레스토랑 포함), 금융 서비스 분야의 브랜드가 차세대 프로그램을 설계, 관리, 확장할 수 있도록 지원합니다. 개인화된 데이터 기반 경험을 통해 참여, 리텐션, 고객 LTV에서 측정 가능한 성장을 이끌어냅니다.

유연한 API 우선 아키텍처를 기반으로 구축된 GRAVTY®는 실시간 적립 및 사용, 파트너 에코시스템 관리, 채널 간 통합을 지원합니다. 팀은 프로그램을 더 빠르게 출시하고, 반복 개선하며, 대규모로 로열티 경험을 제공할 수 있습니다.

_이 통합은 LJI에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 GRAVTY® 통합은 두 플랫폼 간에 로열티 데이터와 메시징 트리거를 연결합니다. GRAVTY®는 사용자 데이터를 속성, 이벤트, 구매로 Braze에 전송합니다. Braze는 해당 데이터를 저장하고 SMS, 이메일, 푸시 알림 등의 채널을 통해 메시지를 전달합니다. 동기화된 데이터를 세분화, 개인화, 트리거에 활용할 수 있습니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
| :--- | :--- |
| GRAVTY® 계정 | 통합 구성 및 이벤트 구독 관리 권한이 있는 GRAVTY® 계정이 필요합니다. |
| Braze 계정 | API 접근이 활성화된 Braze 계정이 필요합니다. |
| Braze REST API 키 | `campaigns.trigger.send`, `canvas.trigger.send`, `users.track` 권한이 있는 REST API 키가 필요합니다.<br><br> Braze 대시보드에서 **Settings** > **API Keys**로 이동하여 이 키를 생성하세요. |
| Braze API 엔드포인트 | Braze REST 엔드포인트입니다(예: `https://rest.fra-01.braze.eu`). 자세한 내용은 [Braze 인스턴스 및 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 참조하세요. |
| Campaign 또는 Canvas ID | GRAVTY®에서 트리거하는 **Campaigns** 또는 **Canvas** 워크플로의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 활용 사례 {#use-cases}

이 통합은 다음과 같은 Braze 기능을 지원합니다:

- **사용자 데이터 동기화(`/users/track`):** 멤버 속성, 이벤트, 구매를 Braze에 동기화하여 세분화 및 개인화에 활용합니다.
- **Campaign 트리거(`/campaigns/trigger/send`):** Braze Campaigns를 사용하여 일회성 또는 트랜잭션 메시지를 트리거합니다.
- **Canvas 트리거(`/canvas/trigger/send`):** Braze **Canvas**를 사용하여 다단계 여정 및 라이프사이클 메시징을 시작합니다.
- **세분화 및 개인화:** 동기화된 데이터를 기반으로 타겟 오디언스를 구축하고 개인화된 커뮤니케이션을 전달합니다.

## 통합 {#integration}

GRAVTY®와 Braze 통합은 API 기반으로, GRAVTY®와 Braze 간의 실시간 데이터 동기화 및 커뮤니케이션 트리거를 지원합니다.

### 1단계: Braze와 GRAVTY® 연결 {#step-1-connect-braze-with-gravty}

1. GRAVTY®에서 **Subscriber Setup**으로 이동하여 외부 통합을 관리합니다.
2. **Add New Subscriber**를 선택합니다.
3. 통합 제공자로 **Braze**를 선택합니다.
4. 다음 정보를 입력합니다:
   * **API URL** (Braze REST 엔드포인트)
   * **API Key** (Braze REST API 키)
5. 구성을 저장하고 연결이 활성 상태인지 확인합니다.

![Braze가 선택되고 API URL 및 API 키 필드와 활성 구독자 토글이 있는 GRAVTY® Add Subscriber 양식.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### 2단계: 이벤트 트리거 구성 {#step-2-configure-event-trigger}

멤버 활동이 정의한 조건을 충족할 때 실행되는 이벤트를 GRAVTY®에서 생성합니다(예: 트랜잭션, 포인트 적립, 등급 변경, 프로그램 등록).

1. GRAVTY®에서 **Events** 섹션으로 이동합니다.
2. **Create Event**를 클릭합니다.
3. 이벤트 조건을 정의합니다(예: 트랜잭션 생성, 포인트 적립, 등급 업그레이드).
4. 이벤트가 트리거되어야 하는 시점을 결정하는 규칙을 구성합니다.
5. 커뮤니케이션 트리거를 활성화하기 위해 Braze 구독자를 이벤트에 연결합니다.
6. 이벤트 구성을 저장합니다.

다음은 멤버가 프로그램에 등록될 때 트리거되도록 구성된 이벤트 예시입니다:

![Braze가 구독자로 연결된 멤버 프로그램 등록용 GRAVTY® 이벤트 구성.]({% image_buster /assets/img/lji/event-configuration.png %})

### 3단계: 템플릿 속성 매핑 구성 {#step-3-configure-template-attribute-mapping}

이벤트를 구성한 후, 데이터 동기화 및 커뮤니케이션 트리거를 활성화하기 위해 구독자 구성을 완료합니다:

1. 구독자 드롭다운에서 1단계에서 생성한 **Braze 구독자**를 선택합니다.
2. 사용 사례에 따라 적절한 **채널**(**Campaign** 또는 **Canvas**)을 선택합니다. 데이터 동기화만 필요한 경우 채널을 선택하지 않아도 됩니다.
3. 해당하는 경우 **Template Name** 필드에 **Campaign ID** 또는 **Canvas ID**를 입력합니다.
4. 동기화 및/또는 트리거 기반 메시징을 지원하도록 커뮤니케이션 유형을 구성합니다.

GRAVTY®에서 필드 매핑을 구성하려면:

1. **Add New Field**를 클릭합니다.
2. 드롭다운에서 **GRAVTY® 속성**을 선택합니다.
3. 데이터가 매핑될 해당 **Braze 속성 이름**을 입력합니다.

{% alert important %}
`external_id`는 매핑할 필요가 없습니다. GRAVTY®는 멤버 ID(GRAVTY®의 고유 멤버 식별자)를 해싱하여 내부적으로 생성하며, Braze는 해당 해시 값을 고객 프로필의 `external_id`로 수신합니다.<br><br> 통합을 활성화하기 전에, 이 값이 현재 Braze에서 `external_id`를 설정하는 방식과 일치하는지 확인하세요. Braze에서 동일한 사용자에 대해 이미 다른 `external_id`를 사용하고 있다면, 데이터를 동기화하기 전에 LJI와 협력하여 식별자를 맞추세요.
{% endalert %}

{: start="4"}
4. 필요에 따라 **1~3**단계를 반복하여 추가 매핑을 설정합니다.
5. **Save**를 클릭하여 구성을 적용합니다.

![Braze 멤버 동기화를 위한 속성 매핑 구성.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
이 통합은 숫자(정수, 플로트), 문자열, 배열, 부울, 오브젝트, 오브젝트 배열, 날짜를 포함한 모든 Braze 커스텀 속성 데이터 유형을 지원합니다.
{% endalert %}

### 4단계: 통합 테스트 {#step-4-test-the-integration}

GRAVTY®에서 샘플 이벤트를 트리거하여 동기화, 커뮤니케이션 트리거, 전체 통합이 예상대로 작동하는지 확인합니다.

* 멤버 데이터가 Braze에 동기화되어 멤버 프로필에 반영됩니다.

![구성된 필드 매핑을 기반으로 데이터 필드가 채워진 화면.]({% image_buster /assets/img/lji/braze-member-profile.png %})

* 구성된 Campaign 또는 Canvas에 따라 커뮤니케이션이 트리거됩니다.

![Braze에서 트리거된 이메일 예시.]({% image_buster /assets/img/lji/braze-email-example.png %})

## 고객지원 {#support}

통합 지원 또는 문제 해결이 필요하면 [support@lji.io](mailto:support@lji.io)로 LJI에 문의하세요.