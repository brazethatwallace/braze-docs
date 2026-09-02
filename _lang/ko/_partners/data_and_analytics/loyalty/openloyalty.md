---
nav_title: Open Loyalty
article_title: Open Loyalty
description: "Braze와 Open Loyalty 통합을 통해 포인트 잔액, 등급 변경, 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화할 수 있습니다."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Open Loyalty

> [Open Loyalty](https://www.openloyalty.io/)는 고객 로열티 및 리워드 프로그램을 구축하고 관리할 수 있는 클라우드 기반 로열티 프로그램 플랫폼입니다. Braze와 Open Loyalty 통합은 포인트 잔액, 등급 변경, 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화합니다. 이를 통해 사용자의 로열티 상태가 변경되면 개인화된 메시지(이메일, 푸시, SMS)를 트리거할 수 있습니다.

_이 통합은 Open Loyalty에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

이 통합은 Braze 데이터 변환을 사용하여 Open Loyalty에서 웹훅을 캡처하고 이를 Braze 고객 프로필에 매핑합니다.

* **실시간 업데이트**: 로열티 이벤트(포인트 획득, 등급 업그레이드)를 Braze에 푸시합니다.
* **개인화**: Braze 템플릿에서 로열티 속성(현재 잔액, 다음 등급 이름)을 사용합니다.
* **양방향**: Braze 인게이지먼트 데이터를 기반으로 Open Loyalty 고객 커스텀 속성을 업데이트합니다.

## 사용 사례 {#use-cases}

이 통합에는 다음과 같은 데이터 흐름이 포함됩니다:

1. **이벤트를 Braze에 동기화(인바운드)**: 포인트 변경, 등급 업그레이드 또는 리워드 사용을 추적하기 위해 Open Loyalty에서 Braze로 데이터를 전송합니다. 데이터 변환은 이 데이터를 사용자 이벤트로 변환합니다.
2. **Open Loyalty 회원 수정(아웃바운드)**: "VIP" 라벨을 추가하거나 커스텀 속성을 업데이트하는 등 Braze의 사용자 동작에 따라 Open Loyalty에서 회원 데이터를 자동으로 업데이트합니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
| :--- | :--- |
| Open Loyalty 계정 | 이 파트너십을 활용하려면 Open Loyalty 테넌트의 관리자 계정이 필요합니다. |
| Open Loyalty REST API 키 | Open Loyalty REST API 키(Braze에서 Open Loyalty로 데이터를 전송하는 통합용). <br><br> **Settings > Admins > API Keys**에서 생성합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 이 키를 생성합니다. |
| Braze 데이터 변환 | 웹훅 리스너를 구성하려면 Braze의 "데이터 설정" 탭에 대한 접근 권한이 필요합니다. |
| 일치하는 ID | Braze의 사용자 `external_id`는 Open Loyalty의 `loyaltyCardNumber`(또는 다른 기본 식별자)와 일치해야 합니다. |
| 테넌트 ID | Open Loyalty 테넌트 ID(아웃바운드 업데이트에 필요). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

기본 통합은 데이터 변환을 사용하여 Open Loyalty 웹훅 이벤트를 Braze에 동기화합니다.

### 1단계: Braze에서 웹훅 URL 생성하기 {#step-1-generate-the-webhook-url-in-braze}

먼저 Braze에서 데이터 변환을 생성하여 데이터를 수신하기 위한 고유 URL을 생성합니다.

1.  Braze에서 **데이터 설정 > 데이터 변환**을 엽니다.
2.  **변환 만들기**를 클릭합니다.
3.  다음 필드를 작성합니다:
     * **변환 이름**: 설명이 포함된 이름을 입력합니다(예: "Open Loyalty 포인트 업데이트 이벤트").
     * **대상 선택**: **POST: Track users**를 선택합니다.
4.  **변환 만들기**를 클릭합니다.
5.  세부 정보 패널에서 **웹훅 URL**을 찾아 **복사**를 클릭합니다.

{% alert important %}
이 URL은 다음 단계에 필요하므로 안전하게 보관하세요.
{% endalert %}

### 2단계: Open Loyalty에서 웹훅 구독 만들기 {#step-2-create-the-webhook-subscription-in-open-loyalty}

Open Loyalty에 방금 생성한 URL로 특정 이벤트를 보내도록 설정합니다.

1.  Open Loyalty 관리자 패널에 로그인합니다.
2.  **General > Webhooks**로 이동합니다.
3.  **Add new webhook**을 클릭하고 구독을 구성합니다:
    * **eventName**: 추적하려는 이벤트를 선택합니다(예: `AvailablePointsAmountChanged`, `CustomerLevelChanged` 또는 `CampaignEffectWasApplied`).
    * **url**: 1단계의 Braze 웹훅 URL을 붙여넣습니다.
    * 다음 헤더를 추가합니다:
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  웹훅 구독을 저장합니다.

### 3단계: 데이터 변환 구성하기 {#step-3-configure-the-data-transformation}

수신되는 Open Loyalty 페이로드를 Braze 속성에 매핑하는 JavaScript 로직을 Braze에서 작성합니다.

1.  Braze에서 1단계에서 만든 데이터 변환을 엽니다.
2.  Open Loyalty에서 이벤트를 트리거하여(예: 회원의 포인트 변경 또는 등급 할당) **웹훅 세부 정보** 창에 샘플 페이로드를 생성합니다.
3.  **변환 코드** 편집기에서 수신 데이터를 매핑하는 스크립트를 작성합니다. 다음 예시를 참고하세요:

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,

      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",

      // timestamp
      "time": new Date().toISOString(),

      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4. **유효성 검사**를 클릭하여 코드가 샘플 페이로드에 대해 실행되는지 확인한 다음 **활성화**를 클릭합니다.


## Braze에서 Open Loyalty 사용하기 {#using-open-loyalty-with-braze}

인바운드 통합을 완료한 후 **아웃바운드 업데이트**를 구성하여 Braze 동작에 따라 Open Loyalty 회원을 수정합니다.

### 1단계: Braze 웹훅 Campaign 구성하기 {#step-1-configure-braze-webhook-campaign}

이 프로세스는 Braze 웹훅을 사용하여 Open Loyalty 회원 API로 `PATCH` 요청을 전송합니다(예: "VIP" 라벨 추가).

1.  Braze에서 새 **웹훅 Campaign**을 만들거나 Canvas 내에서 웹훅을 사용합니다.
2.  **웹훅 작성**을 클릭합니다.
3.  **웹훅 URL**: Open Loyalty 인스턴스, 테넌트 ID, 사용자 ID에 대한 Braze Liquid 변수를 사용하여 URL을 구성합니다.
    * 형식:
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. 다음 필드를 작성합니다:
    * **요청 방법**: `PATCH`
    * **요청 헤더**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **요청 본문**: `Raw text`를 선택하고 페이로드를 붙여넣습니다:

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### 2단계: 트리거 구성하기 {#step-2-configure-the-trigger}

1.  **전달** 또는 **진입 스케줄** 탭으로 이동합니다.
2.  다음 필드를 작성합니다:
    * **전달 방법**: 액션 기반.
    * **트리거**: 관련 트리거를 정의합니다(예: 사용자가 Braze에서 특정 Segment에 진입하는 경우).
    * **시작**: Campaign을 활성화합니다.

## 문제 해결 {#troubleshooting}

### 인바운드 이벤트 확인 {#verify-inbound-events}
데이터 변환이 활성화되면 데이터가 Braze에 커스텀 이벤트로 표시됩니다. **커스텀 이벤트 수행** 트리거가 있는 Campaign을 생성하고 정의한 이벤트(예: `Loyalty Event Triggered`)를 사용할 수 있는지 확인하여 이를 검증합니다.

### 아웃바운드 웹훅 확인 {#verify-outbound-webhooks}
Braze에서 메시지 활동 로그를 확인하여 웹훅이 `200 OK` 상태를 반환했는지 확인합니다.
* **401 오류**: Open Loyalty API 토큰을 확인하세요.
* **404 오류**: Braze의 사용자 ID가 Open Loyalty에 존재하지 않습니다.