---
nav_title: Flybuy
article_title: Flybuy
alias: /partners/flybuy/
description: "이 참조 문서에서는 위치 서비스 플랫폼인 Flybuy와 Braze 간의 파트너십을 설명하며, 운영 및 마케팅 역량에 위치 인텔리전스를 추가하는 방법을 안내합니다."
page_type: partner
search_tag: Partner

---

# Flybuy

> Radius Networks의 [Flybuy](https://www.flybuy.com/)는 AI 기반 기술을 활용하여 픽업, 배달, 드라이브스루, 매장 내 식사 전반에서 서비스 속도를 최적화하는 선도적인 옴니채널 위치 플랫폼입니다. 통합 마케팅 스위트를 통해 Flybuy는 브랜드가 초정밀 타겟팅된 순간 기반 메시지를 전달할 수 있도록 지원하여 참여를 유도하고, 주문 금액을 높이며, 더 넓은 로열티 이니셔티브를 지원합니다.

_이 통합은 Flybuy에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Flybuy는 풍부한 사용자 인텔리전스 이벤트를 Braze에 전달하여 브랜드가 최고 수준의 개인화로 초관련성 높은 위치 인식 메시지를 보낼 수 있도록 지원합니다. 사용자가 Flybuy에서 이벤트를 생성하면, 풍부한 사용자 속성이 포함된 커스텀 이벤트가 Braze에 전달됩니다. 이러한 이벤트와 속성은 옴니채널 운영을 강화하고 근접 기반 메시지를 트리거하는 데 사용할 수 있습니다.

## 필수 조건 {#prerequisites}

통합을 활성화하기 전에 다음 사항이 필요합니다.

| 요구 사항 | 설명 |
|---|---|
| Flybuy 계정 | 하나 이상의 프로젝트가 있는 Flybuy 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

통합을 활성화하려면 다음 단계를 완료합니다.

1. Flybuy 머천트 포털에서 **Project Info**로 이동한 후 **Events Engine**을 클릭합니다.
2. **Add a Destination**을 클릭한 다음 **Braze**를 선택합니다.
3. Braze API 키와 엔드포인트를 추가하고, 활성화할 이벤트를 선택합니다.
4. **Finish Setup**을 클릭합니다.

{% alert important %}
Flybuy는 로그인한 사용자에 대해 `loyalty_id`를 Braze `external_id`에 매핑합니다.
{% endalert %}

## 활용 사례 {#use-cases}

- [픽업](https://www.flybuy.com/flybuypickup)
- [배달](https://www.flybuy.com/flybuydelivery)
- [드라이브스루](https://www.flybuy.com/flybuydrivethru)
- [테이블 서비스](https://www.flybuy.com/flybuytableservice)
- [호텔 모바일 체크인 및 주문](https://www.flybuy.com/industries/hospitality)
- [마케팅 스위트](https://www.flybuy.com/flybuy-marketing-suite)

## 이벤트 및 속성 기반 트리거 예시 {#event-and-attribute-based-trigger-examples}

커스텀 이벤트와 커스텀 속성을 사용하여 다양한 개인화된 경험을 구현할 수 있습니다.

### 픽업 경험이 좋지 않았던 고객의 오디언스 세그먼트 구축 {#build-an-audience-segment-of-customers-who-had-a-bad-pickup-experience}

예를 들어, 픽업 경험을 별 5개 미만으로 평가한 모든 고객을 타겟팅합니다.

![좋지 않은 픽업 경험에 대한 세그먼트]({% image_buster /assets/img/flybuy/flybuy1.png %})

### 고객이 가상 픽업 구역에 진입할 때 알림 트리거 {#trigger-an-alert-when-a-customer-enters-a-virtual-pickup-area}

로열티 계정이 없는 고객을 타겟팅하여 앱을 다운로드하고 로열티 계정을 생성하도록 개인화된 SMS를 전송합니다.

![고객이 가상 픽업 구역에 진입할 때 알림 트리거]({% image_buster /assets/img/flybuy/flybuy2.png %})

![고객이 가상 픽업 구역에 진입할 때 알림 트리거 메시지]({% image_buster /assets/img/flybuy/flybuy2a.png %})

### 대기 시간이 길었던 고객의 오디언스 세그먼트 구축 {#build-an-audience-segment-of-customers-who-had-a-long-wait-time}

예를 들어, 가상 매장 구역을 나갈 때 대기 시간이 2분을 초과한 모든 고객을 타겟팅합니다.

![대기 시간이 길었던 고객의 오디언스 세그먼트 구축]({% image_buster /assets/img/flybuy/flybuy3.png %})

### 고객이 잘못된 위치로 향할 때 경로 수정 알림 트리거 {#trigger-a-course-correction-alert-when-a-customer-is-headed-to-the-wrong-location}

고객이 주문한 위치와 다른 곳으로 향하거나 도착했을 때 푸시 알림을 전송합니다.

### 방문 마일스톤에 따른 특별 혜택 전달 {#deliver-special-offers-based-on-trip-milestones}

예를 들어, VIP 고객이 자주 방문하는 위치에 도착했을 때 특별 혜택을 전송합니다.

### 주문에서 누락된 항목이 있었던 고객의 오디언스 세그먼트 구축 {#build-an-audience-segment-of-customers-who-were-missing-items-in-their-order}

예를 들어, 디지털 주문에서 항목이 누락되었다고 코멘트한 모든 고객을 타겟팅합니다.

API 및 SDK에 대한 자세한 내용은 [Flybuy 개발자 설명서](https://www.radiusnetworks.com/developers/flybuy/#/)를 참조하세요.