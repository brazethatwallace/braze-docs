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

RCS 설정은 SMS 설정만큼 간단합니다. 풍부하고 인터랙티브한 메시지를 보내는 방법을 알아보려면 계속 읽어보세요.

## 1단계: 자격 기준 충족 {#step-1-meet-the-eligibility-criteria}

Braze에서 RCS를 발송하려면 비즈니스가 세 가지 기준을 사전에 충족해야 합니다.

1. 현재 Braze 계약에 메시지 또는 액션 크레딧이 포함되어 있어야 합니다.
2. RCS 메시지를 다음 Braze 지원 국가 중 하나로 발송해야 합니다.
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
3. 계약에 RCS SKU를 확보해야 합니다.

## 2단계: RCS 인증 발신자 등록 {#step-2-register-an-rcs-verified-sender}

RCS 메시지를 보내려면 먼저 RCS 인증 발신자를 등록해야 합니다. 이는 사용자가 모바일 기기에서 보게 되는 브랜드 표현으로, 브랜드 이름, 로고, 인증 배지, 그리고 선택적 태그라인이 포함됩니다. RCS 인증 발신자는 고객 신뢰를 강화하고 메시지가 인증된 소스에서 발송되었음을 확인해 줍니다.

!["Cat Failz Cafe"라는 RCS 메시지의 RCS 인증 발신자 예시.]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

주문서에 RCS SKU를 추가하면 Braze에 알림이 전달되며, RCS 발신자 등록 정보를 안내해 드립니다. 양식의 형식은 RCS 메시지를 발송하려는 국가에 따라 달라집니다.

작성된 양식을 Braze에 제출하면, Braze가 대신 등록 절차를 완료해 드립니다.

### 2.1단계: RCS 구독 그룹에 대한 SMS 대체 설정 {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

현재 이동통신사 커버리지는 국가별로 다르고, 사용자의 하드웨어 및 소프트웨어 지원도 개인마다 다르기 때문에 SMS 대체는 오늘날 성공적인 RCS 프로그램의 핵심 구성요소입니다. SMS 대체를 설정하는 것을 권장합니다. 이동통신사가 RCS를 지원하지 않거나 사용자의 기기가 RCS 메시지를 수신할 수 없는 경우, SMS 대체가 메시지를 발송하여 사용자와의 중요한 순간을 놓치지 않도록 합니다.

첫 번째 RCS Campaign을 배포하기 전에 현재 SMS 옵트인 경험, 구독 그룹, 오디언스 세분화를 검토하는 것을 강력히 권장합니다. 필요한 경우, 고객 성공 매니저가 항상 안내를 제공하고 설정 과정을 도와드릴 수 있습니다.

#### SMS 대체가 이벤트 및 세분화와 작동하는 방식 {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab 이벤트 동작 %}

RCS에서 SMS 대체를 사용할 때, 이벤트 동작은 메시지가 RCS를 통해 성공적으로 발송되었는지 또는 SMS로 대체되었는지에 따라 달라집니다.

- **RCS 발송이 성공한 경우:** RCS 발송 이벤트와 RCS 전달 이벤트를 수신합니다.
- **RCS 발송이 SMS로 대체된 경우:** RCS 발송 이벤트, RCS 거부 이벤트, SMS 전달 이벤트를 수신합니다. SMS 전달 이벤트에는 `IS_SMS_FALLBACK=TRUE`가 포함됩니다.

{% endtab %}
{% tab 세분화 동작 %}

SMS 및 RCS의 경우, 수신 메시지 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)(예: [Campaign에서 메시지 수신]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-campaign) 및 [캔버스 단계에서 메시지 수신]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step))은 메시지가 사용자의 기기에 도달할 때가 아니라 발송될 때 평가됩니다. SMS 대체가 활성화된 경우, RCS 메시지가 거부되어 SMS로 대체되거나 대체 SMS가 사용자의 기기에 전달되지 않더라도 사용자는 여전히 이러한 필터에 매칭될 수 있습니다.

{% endtab %}
{% endtabs %}

### 이동통신사 승인 일정 {#timeline-for-carrier-approval}

이동통신사 승인 일정은 국가별로 다르며, 같은 국가 내에서도 달라질 수 있습니다. RCS 시장은 아직 초기 단계이므로 이동통신사 및 어그리게이터 프로세스가 빠르게 변화하고 있다는 점을 유의하세요. 미국의 경우, Braze는 RCS 인증 발신자에 대한 이동통신사 승인 소요 시간이 일반적으로 4~6주 범위이며, 테스트 발신자는 보통 1주 이내에 승인되는 것으로 추정합니다.

RCS 인증 발신자가 승인되면, 운영팀이 구독 그룹을 필요에 따라 업데이트하여 RCS 발신자가 포함되어 있는지 확인합니다.

## 3단계: 구독 그룹 설정 {#step-3-set-up-subscription-groups}

통합 방식에 따라 Braze는 기존 SMS 구독 그룹에 RCS 인증 발신자를 추가하거나 새로운 구독 그룹을 설정할 수 있습니다. 자세한 설정 안내는 [SMS 및 RCS 구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups)을 참조하세요.

## SMS 트래픽을 RCS로 마이그레이션 {#migrating-sms-traffic-to-rcs}

별도의 SMS 및 RCS 구독 그룹이 있는 경우, 한 단계 Canvas를 사용하여 사용자를 SMS에서 RCS로 마이그레이션할 수 있습니다.

Braze는 처음에 소규모 사용자에게 RCS 발송을 테스트하고, 시간이 지남에 따라 더 많은 사용자를 RCS 구독 그룹으로 마이그레이션하는 것을 권장합니다. 예를 들어, SMS 구독 그룹에 1,000,000명의 사용자가 가입되어 있다면, 먼저 모든 사용자를 새 구독 그룹으로 마이그레이션한 다음 50,000~100,000명(5~10%)의 소규모 오디언스로 세분화하여 RCS 메시지를 테스트하는 방식이 될 수 있습니다.

### 1단계: Canvas를 생성하고 진입 스케줄 작성 {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Canvas를 생성하고 쉽게 식별할 수 있는 이름을 지정합니다(예: "SMS-RCS 구독 그룹 사용자 이전"). 그런 다음 편리한 시간에 Campaign을 스케줄합니다.

### 2단계: 오디언스 정의 {#step-2-define-your-audience}

다음 방법 중 하나를 사용하여 오디언스를 정의합니다. 그런 다음 **발송 설정** 단계로 이동하여 **가입되었거나 옵트인한 사용자**를 선택합니다.

| 방법 | 설명 |
|------|------|
| **Segment 생성** | 구독 그룹의 모든 사용자 또는 세분화 필터를 사용한 하위 집합(예: 무작위 5~10%)을 포함하는 Segment를 구축합니다. Segment는 각 발송 전에 업데이트되어 현재 사용자 기반을 반영합니다. |
| **Campaign 또는 Canvas 필터 적용** | Campaign 또는 Canvas의 **타겟 오디언스** 단계에서 오디언스를 세분화합니다. 페이지를 벗어나지 않고 타겟팅 옵션을 조정하여 유연성을 높일 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 오디언스 정의" }

### 3단계: 사용자 업데이트 단계 구성 {#step-3-configure-a-user-update-step}

Canvas에 사용자 업데이트 단계를 추가합니다. 해당 단계에서 **Advanced JSON Editor**를 열고 다음을 입력합니다(고유 사용자 식별자 필드의 경우 `braze_id` 필드를 사용하는 것을 권장합니다).

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

![앞서 언급한 JSON 코드가 포함된 사용자 업데이트 오브젝트.]({% image_buster /assets/img/sms/user_update_object.png %})

### 4단계: Canvas 테스트 {#step-4-test-the-canvas}

더 넓은 오디언스에 발송하기 전에 [Canvas를 테스트]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases)하여 예상대로 작동하는지 확인하는 것을 강력히 권장합니다.

### 5단계: Canvas 시작 {#step-5-launch-your-canvas}

Canvas를 성공적으로 테스트한 후, 사용자 하위 집합에 대해 시작하세요!

사용자가 성공적으로 마이그레이션되었는지 확인하려면, 업데이트된 개별 사용자 프로필 몇 개를 확인하는 것을 권장합니다. **참여** 탭에서 **연락처 설정**을 찾아 스크롤하여 사용자가 가입된 구독 그룹을 확인합니다. RCS 구독 그룹 토글이 켜져 있어야 합니다.