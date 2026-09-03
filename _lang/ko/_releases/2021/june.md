---
nav_title: 6월
page_order: 6
noindex: true
page_type: update
description: "이 문서에는 2021년 6월의 릴리스 노트가 포함되어 있습니다."
---

# 2021년 6월 {#june-2021}

## 트랜잭션 이메일 Campaigns {#transactional-email-campaigns}

트랜잭션 이메일은 발신자와 수신자 간에 합의된 거래를 원활하게 처리하기 위해 전송되는 이메일입니다. Braze의 [트랜잭션 이메일 Campaign]({{site.baseurl}}/api/api_campaigns/transactional_campaigns)은 주문 확인, 비밀번호 재설정, 결제 알림 또는 기타 비즈니스에 중요한 알림과 같은 자동화된 비프로모션 이메일 메시지를 전송하기 위해 특별히 설계되었습니다. 또한 해당하는 [트랜잭션 이메일 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)도 함께 생성되었습니다. 트랜잭션 이메일과 새로운 엔드포인트는 일부 Braze 패키지에서만 사용할 수 있습니다.

## 이벤트 속성정보에 대한 중첩 객체 지원 {#nested-object-support-for-event-properties}

Braze는 이제 커스텀 이벤트 및 구매 이벤트에 대한 [중첩 객체]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)를 지원합니다. 중첩 객체를 사용하면 데이터 배열을 커스텀 이벤트 및 구매의 속성정보로 전송할 수 있습니다. 이 중첩 데이터는 Liquid 및 점 표기법을 사용하여 API 트리거 메시지에서 개인화된 정보를 템플릿화하는 데 활용할 수 있습니다.

## 새로운 HMAC Liquid 필터 {#new-hmac-liquid-filters}

Braze 플랫폼에 새로운 [`hmac_sha1` 및 `hmac_sha256` Liquid 인코딩 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)가 추가되었습니다.

## 구매 이벤트 페이지 {#purchase-event-page}

Braze의 구매 이벤트에 대해 자세히 알고 싶으신가요? 전용 [구매 이벤트]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) 문서를 방문하여 자세히 알아보세요.

## 새로운 Braze 파트너십 {#new-braze-partnerships}

### Nexla - 워크플로우 자동화 {#nexla-workflow-automation}

[Nexla]({{site.baseurl}}/partners/nexla)는 통합 데이터 운영 분야의 선두주자이자 2021 Gartner Cool Vendor로 선정된 기업입니다. Currents를 사용하여 데이터 웨어하우스로 데이터를 전송하는 고객은 Nexla를 활용하여 해당 데이터를 추출, 변환 및 로드하여 다른 위치로 보낼 수 있으므로, 전체 에코시스템에서 데이터에 쉽게 접근할 수 있습니다. Nexla를 사용하면 Braze 커런츠를 활용하여 간단한 포인트 앤 클릭 방식으로 원하는 대상에 커스텀 형식의 데이터를 전달할 수 있습니다.

### Amperity - 고객 데이터 플랫폼 {#amperity-customer-data-platform}

[Amperity]({{site.baseurl}}/partners/amperity)는 브랜드가 고객을 더 잘 이해하고, 전략적 결정을 내리며, 소비자에게 더 나은 서비스를 제공하기 위해 일관되게 올바른 조치를 취할 수 있도록 돕는 종합 엔터프라이즈 고객 데이터 플랫폼입니다. Amperity는 고객 데이터 플랫폼와 Braze 전반에 걸쳐 고객에 대한 통합 뷰를 제공함으로써 Braze 플랫폼을 지원하며, 가치 있는 Amperity 데이터를 Braze로 전송할 수 있게 합니다.

### Digioh - 설문조사 {#digioh-surveys}

[Digioh]({{site.baseurl}}/partners/digioh)는 리스트를 확장하고, 퍼스트파티 데이터를 수집하며, 수집한 데이터를 Braze Campaigns에 활용할 수 있도록 도와줍니다. 드래그 앤 드롭 빌더를 사용하면 브랜드에 맞는 양식, 팝업, 선호도 센터, 랜딩 페이지 및 설문조사를 쉽게 만들어 고객과 연결할 수 있습니다.

### AppsFlyer Audiences - 기여도/분석 {#appsflyer-audiences-attributionanalytics}

[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer)는 마케팅 분석, 모바일 기여도 측정 및 딥링킹을 통해 앱을 분석하고 최적화할 수 있도록 도와주는 모바일 마케팅 분석 및 기여도 측정 플랫폼입니다. [AppsFlyer Audiences]({{site.baseurl}}/partners/appsflyer_audiences)를 사용하면 오디언스 세그먼트를 구축하고, 해당 세그먼트를 Braze에 직접 전달하여 강력한 고객 참여 Campaign을 생성할 수 있습니다.