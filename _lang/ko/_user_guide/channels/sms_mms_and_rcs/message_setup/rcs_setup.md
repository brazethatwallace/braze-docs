---
nav_title: "RCS 설정"
article_title: "RCS 설정"
page_order: 1
alias: /rcs_setup/
description: "이 참조 문서에서는 RCS를 시작하고 실행하는 데 필요한 요구 사항을 다룹니다."
page_type: reference
channel:
  - RCS
---

# RCS 설정 {#set-up-rcs}

> 이 문서에서는 RCS 채널을 시작하고 실행하는 데 필요한 요구 사항을 다룹니다.

RCS 설정은 단문 메시지 서비스 설정만큼 간단합니다. 풍부하고 인터랙티브한 메시지를 보내는 방법을 알아보려면 계속 읽어보세요.

## 1단계: 자격 기준 충족 {#step-1-meet-the-eligibility-criteria}

Braze에서 RCS를 전송하려면 비즈니스가 세 가지 기준을 사전에 충족해야 합니다.

1. 현재 Braze 계약에 메시지 또는 액션 크레딧이 포함되어 있어야 합니다.
2. RCS 메시지를 다음 Braze 지원 국가 중 하나로 전송해야 합니다.
- 미국
- 영국
- 독일
- 멕시코
- 스웨덴
- 스페인
- 싱가포르
- 브라질
- 프랑스
- 이탈리아
- 콜롬비아
3. 계약에 RCS SKU를 포함해야 합니다.

## 2단계: RCS 인증 발신자 등록 {#step-2-register-an-rcs-verified-sender}

RCS 메시지를 보내려면 먼저 RCS 인증 발신자를 등록해야 합니다. 이는 사용자의 모바일 기기에 표시되는 브랜드의 표현으로, 브랜드 이름, 로고, 인증 배지, 선택적 태그라인이 포함됩니다. RCS 인증 발신자는 고객 신뢰를 강화하고 메시지가 인증된 출처에서 발송되었음을 확인해 줍니다.

![RCS 메시지에서 "Cat Failz Cafe"라는 이름의 RCS 인증 발신자 예시.]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

주문서에 RCS SKU를 추가하면 Braze에 알림이 전달되고, Braze가 RCS 발신자 등록 정보를 안내합니다. 양식의 형식은 RCS 메시지를 보내려는 국가에 따라 달라집니다.

작성된 양식을 Braze에 제출하면, Braze가 대신 등록 절차를 완료합니다.

### 2.1단계: RCS 구독 그룹에 대한 단문 메시지 서비스 대체 설정 {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

현재 통신사 커버리지는 국가별로 다르고, 사용자의 하드웨어 및 소프트웨어 지원도 개인마다 다르기 때문에 단문 메시지 서비스 대체는 오늘날 성공적인 RCS 프로그램을 운영하는 데 핵심적인 요소입니다. 단문 메시지 서비스 대체를 설정하는 것을 권장합니다. 통신사가 RCS를 지원하지 않거나 사용자의 기기가 RCS 메시지를 수신할 수 없는 경우, 단문 메시지 서비스 대체가 메시지를 대신 전송하여 사용자와의 중요한 순간을 놓치지 않도록 합니다.

첫 번째 RCS Campaign을 배포하기 전에 현재 단문 메시지 서비스 옵트인 경험, 구독 그룹, 오디언스 세분화를 검토하는 것을 강력히 권장합니다. 필요한 경우, 고객 성공 매니저가 항상 안내를 제공하고 설정 과정을 도와드릴 수 있습니다.

#### 단문 메시지 서비스 대체가 이벤트 및 세분화와 작동하는 방식 {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab 이벤트 동작 %}

RCS에서 단문 메시지 서비스 대체를 사용할 때, 이벤트 동작은 메시지가 RCS를 통해 성공적으로 전송되었는지 또는 단문 메시지 서비스로 대체되었는지에 따라 달라집니다.

- **RCS 전송이 성공한 경우:** RCS 전송 이벤트와 RCS 전달 이벤트를 수신합니다.
- **RCS 전송이 단문 메시지 서비스로 대체된 경우:** RCS 전송 이벤트, RCS 거부 이벤트, 단문 메시지 서비스 전달 이벤트를 수신합니다. 단문 메시지 서비스 전달 이벤트에는 `IS_SMS_FALLBACK=TRUE`가 포함됩니다.

{% endtab %}
{% tab 세분화 동작 %}

단문 메시지 서비스 및 RCS의 경우, 수신된 메시지 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)([Campaign에서 메시지 수신]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-campaign) 및 [캔버스 단계에서 메시지 수신]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step) 등)는 메시지가 사용자의 기기에 도달할 때가 아니라 전송될 때 평가됩니다. 단문 메시지 서비스 대체가 활성화된 경우, RCS 메시지가 거부되어 단문 메시지 서비스로 대체되거나 대체 단문 메시지 서비스가 사용자의 기기에 전달되지 않더라도 사용자는 이러한 필터에 매칭될 수 있습니다.

{% endtab %}
{% endtabs %}

### 통신사 승인 일정 {#timeline-for-carrier-approval}

통신사 승인 일정은 국가별로 다르며, 같은 국가 내에서도 달라질 수 있습니다. RCS 시장은 아직 초기 단계에 있으므로 통신사 및 어그리게이터 프로세스가 빠르게 변화하고 있다는 점을 유의하세요. 미국의 경우, Braze는 RCS 인증 발신자에 대한 통신사 승인 소요 시간이 일반적으로 4~6주 범위이며, 테스트 발신자는 보통 1주 이내에 승인되는 것으로 추정합니다.

RCS 인증 발신자가 승인되면, 운영팀이 구독 그룹에 RCS 발신자가 포함되어 있는지 확인하고 필요에 따라 업데이트합니다.

## 3단계: 구독 그룹 설정 {#step-3-set-up-subscription-groups}

통합 방식에 따라 Braze는 RCS 인증 발신자를 기존 단문 메시지 서비스 구독 그룹에 추가하거나 새로운 구독 그룹을 설정할 수 있습니다. 자세한 설정 안내는 [단문 메시지 서비스 및 RCS 구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups)을 참조하세요.

## 단문 메시지 서비스 트래픽을 RCS로 마이그레이션하기 {#migrating-sms-traffic-to-rcs}

별도의 단문 메시지 서비스 및 RCS 구독 그룹이 있는 경우, 한 단계로 구성된 Canvas를 사용하여 사용자를 단문 메시지 서비스에서 RCS로 마이그레이션할 수 있습니다. 단계별 안내는 [단문 메시지 서비스 트래픽을 RCS로 마이그레이션하기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#migrate-sms-traffic-to-rcs)를 참조하세요.