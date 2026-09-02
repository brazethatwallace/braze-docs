---
nav_title: Okendo
article_title: Okendo
description: "Okendo와 Braze를 통합하는 방법을 알아보세요."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/)는 옹호를 육성하고, 입소문을 확장하고, LTV or 생애주기 가치를 극대화하여 고객을 동원해 더 빠르고 효율적인 성장을 이끌어내는 도구를 제공하는 통합 고객 마케팅 플랫폼입니다.

*이 통합은 Okendo에서 유지 관리합니다.*

## 통합 정보 {#about-the-integration}

Braze와 Okendo의 통합은 리뷰, 로열티, 추천, 설문조사, 퀴즈 등 Okendo 플랫폼의 여러 제품에서 작동합니다. Okendo는 커스텀 이벤트 및 사용자 속성을 Braze에 전송하며, 이를 통해 메시지를 개인화하고 트리거할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|------------------------|-----------------------------------------------------------------------------|
| Okendo 계정 | 이 파트너십을 이용하려면 Okendo 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Okendo에서 Braze 커넥터 설정하기 {#step-1-set-up-braze-connector-in-okendo}

1. Okendo에서 **Settings** > **Integrations** > **Email & 단문 메시지 서비스** > **Braze**로 이동합니다.
2. **Integration** 설정에 API 엔드포인트와 API 키를 추가합니다.

### 2단계: 식별자 구성하기 {#step-2-configure-your-identifier}

`external_id` 필드는 각 이벤트와 연결된 사용자를 식별하는 데 사용됩니다. 필드를 Shopify 고객 ID와 연결하려면 **Use Shopify Customer ID for Braze user identification**을 토글합니다. 그렇지 않으면 토글을 해제하여 각 사용자의 이메일 주소와 연결합니다.

## Okendo 이벤트와 속성을 Braze에 동기화하기 {#syncing-okendo-events-and-attributes-to-braze}

### 커스텀 이벤트 {#custom-events}

{% alert note %}
샘플 이벤트 데이터는 [Okendo 설명서](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c)를 참조하세요.
{% endalert %}

#### 리뷰 이벤트 {#review-events}

- Okendo Review Created
- Okendo Review Request

#### 추천 이벤트 {#referral-events}

- Sent Okendo Referral
- Opted In to Okendo Referrals
- Okendo Referral Invitation
- Received Okendo Referral Coupon
- Redeemed Okendo Referral Coupon
- Okendo Referral Rejected

#### 로열티 이벤트 {#loyalty-events}

- Enrolled in Okendo Loyalty
- Okendo Loyalty Points Awarded
- Okendo Loyalty Points Redeemed
- Okendo Loyalty Tier Changed
- Okendo Loyalty Points Adjusted

#### 설문조사 이벤트 {#survey-event}

- Submitted Okendo Survey

#### 퀴즈 이벤트 {#quiz-event}

- Submitted Okendo Quiz

### 커스텀 속성 {#custom-attributes}

Okendo는 사용자 프로필 데이터를 Braze에서 커스텀 속성으로 전송하며, 이를 통해 오디언스 세그먼트를 생성할 수 있습니다. 예를 들면 다음과 같습니다:

- 나이, 생일, 피부 타입, 머리 색깔 등 설문조사 및 리뷰 제출 시 묻는 프로필 질문
- *평균 리뷰 평점* 및 *평균 리뷰 감정*과 같은 리뷰 측정기준
- *포인트 잔액* 및 *VIP 등급*과 같은 로열티 측정기준
- *성공한 추천 횟수* 및 *총 추천 매출*과 같은 추천 측정기준
- 설문조사에서 수집한 순고객추천지수 점수

## Okendo 제품과 함께 Braze 사용하기 {#using-braze-with-okendo-products}

Okendo 제품에 따라 Braze와 Okendo를 함께 사용하려면 추가 단계를 완료해야 합니다. 자세한 내용은 다음 문서를 참조하세요:

- [리뷰와 Braze 통합하기](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [로열티와 Braze 통합하기](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [추천과 Braze 통합하기](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [설문조사와 Braze 통합하기](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [퀴즈와 Braze 통합하기](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
통합 구성에 대한 도움이 필요하면 Okendo 지원팀에 문의하세요.
{% endalert %}