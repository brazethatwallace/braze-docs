---
nav_title: 실행 기반 전달
article_title: 실행 기반 전달
page_order: 1
page_type: reference
description: "이 참조 문서에서는 사용자가 특정 이벤트를 완료한 후 Campaign 발송을 트리거하는 방법을 설명합니다."
tool: Campaigns
local_redirect:
  use-cases: '/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#examples'

---

# 실행 기반 전달 {#action-based-delivery}

> 실행 기반 전달 Campaign 또는 이벤트 트리거 Campaign은 트랜잭션 또는 성과 기반 메시지에 매우 효과적입니다. 특정 날짜에 Campaign을 발송하는 대신, 사용자가 특정 이벤트를 완료한 후 발송되도록 트리거할 수 있습니다.

## 트리거 Campaign 설정하기 {#setting-up-a-triggered-campaign}

### 1단계: 트리거 이벤트 선택 {#step-1-select-a-trigger-event}

트리거 이벤트를 선택합니다. 이벤트는 카테고리별로 정리되어 있으며, 워크스페이스 및 활성화된 채널에 따라 사용 가능합니다.

- **이커머스**
    - **Place Order**
    - **Perform Cart Updated Event**
    - **Perform Checkout Started Event**
    - **Perform Checkout Completed Event**
    - **Make Purchase**
- **일반 활동**
    - **Interact With Campaign**
    - **Interact With Step**
    - **Interact with Landing Page**
    - **Perform Conversion Event**
    - **Perform Custom Event**
    - **Perform Exception Event For Campaign**
    - **Start Session**
- **인바운드 메시징**
    - **Send an 단문 메시지 서비스 inbound message**
    - **Send a WhatsApp inbound message**
    - **Send a LINE inbound message**
- **위치**
    - **Enter a Location**
    - **Trigger a Geofence**
- **프로필 업데이트**
    - **Add an Email Address**
    - **Change Custom Attribute Value**
    - **Update Subscription Status**
    - **Update Subscription Group Status**

**이커머스** 그룹에는 **Perform Product Viewed Event**, **Perform Order Cancelled Event**, **Perform Order Refunded Event** 등 권장 이커머스 이벤트도 나열됩니다. 이러한 옵션은 이벤트 이름이 미리 입력된 **Perform Custom Event**를 사용합니다.

인앱 메시지 Campaign은 더 적은 트리거 세트를 지원합니다: **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event**, **Interact With Campaign**. 인앱 메시지 Campaign의 경우 **Interact With Campaign**은 모든 Campaign 또는 특정 Campaign에서 푸시를 여는 것만 포함합니다. 아래의 Campaign 상호작용 목록은 포함되지 않습니다.

비인앱 메시지 Campaign의 경우, **Interact With Campaign**, **Interact With Step** 또는 **Interact with Landing Page**를 선택하면 트리거할 상호작용을 선택합니다. 각 트리거는 고유한 상호작용을 제공하며, 사용 가능한 상호작용은 활성화된 채널에 따라 다릅니다.

{% details Interact With Campaign의 상호작용 %}

- **View in-app message**
- **Click in-app message**
- **Click in-app message button 1**
- **Click in-app message button 2**
- **Submit in-app message survey**
- **Click email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Click alias in email**
- **Clicked Alias in any campaign or canvas step**
- **Directly open push notification**
- **Click push notification button**
- **Click push story page**
- **Perform conversion event**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive 단문 메시지 서비스**
- **Click shortened 단문 메시지 서비스 link**
- **View content card**
- **Click content card**
- **Dismiss content card**
- **View banner**
- **Click banner**
- **Dismiss banner**
- **Click tracked WhatsApp link**
- **Click tracked LINE link**
- **Click tracked KakaoTalk link**
- **Are enrolled in control group**

{% enddetails %}

{% details Interact With Step의 상호작용 %}

- **View in-app message**
- **Start in-app message availability window**
- **Submit in-app message survey**
- **Click email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Click alias in email**
- **Clicked Alias in any campaign or canvas step**
- **Directly open push notification**
- **Click push notification button**
- **Click push story page**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive 단문 메시지 서비스**
- **Click shortened 단문 메시지 서비스 link**
- **View content card**
- **Click content card**
- **Dismiss content card**
- **View banner**
- **Click banner**
- **Dismiss banner**
- **Click tracked WhatsApp link**
- **Click tracked LINE link**
- **Click tracked KakaoTalk link**

{% enddetails %}

{% details Interact with Landing Page의 상호작용 %}

- **Submit form**
- **Submit survey**

{% enddetails %}

Braze [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events)를 통해 트리거 이벤트를 추가로 필터링할 수도 있으며, 커스텀 이벤트 및 인앱 구매에 대한 맞춤형 이벤트 속성정보를 허용합니다. 이 기능을 사용하면 커스텀 이벤트의 특정 속성을 기반으로 메시지를 받는 사용자를 더 세밀하게 조정할 수 있어 Campaign 개인화가 강화되고 더 정교한 데이터 수집이 가능합니다.

예를 들어, "장바구니 금액" 속성정보 필터로 추가 타겟팅된 유기한 장바구니 커스텀 이벤트가 있는 Campaign이 있다고 가정합니다. 이 Campaign은 장바구니에 $100에서 $200 사이의 상품을 남겨둔 사용자에게만 도달합니다.

![장바구니 금액이 $100에서 $200 사이인 커스텀 이벤트 속성정보로 필터링된 유기한 장바구니 Campaign.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
트리거 이벤트 **Start Session**은 Campaign의 Segment가 신규 사용자에게 적용되는 경우(예: Segment가 세션이 없는 사용자로 구성된 경우) 사용자의 첫 앱 실행이 될 수 있습니다.
{% endalert %}

트리거 Campaign을 특정 사용자 Segment에 보낼 수 있으므로, Segment에 속하지 않은 사용자는 트리거 이벤트를 완료하더라도 Campaign을 받지 않습니다.

사용자가 프로필에 이메일 주소를 추가할 때의 트리거 이벤트와 관련하여 다음 규칙이 적용됩니다:

- 트리거 이벤트는 고객 프로필 속성이 업데이트된 후에 실행됩니다. 즉, Campaign의 Segment 및 필터 평가는 속성 업데이트 이후에 이루어집니다. 이는 "이메일 주소가 gmail.com과 일치"와 같은 필터를 설정하여 Gmail 사용자에게만 보내고 이메일 주소를 추가하는 즉시 실행되는 트리거 Campaign을 만들 수 있으므로 유용합니다.
- 트리거 이벤트는 고객 프로필에 이메일 주소가 추가될 때 실행됩니다. 동일한 이메일 주소로 여러 고객 프로필을 생성한 경우, 각 고객 프로필에 대해 한 번씩 Campaign이 여러 번 실행될 수 있습니다.

또한, 트리거된 인앱 메시지는 여전히 인앱 메시지 전달 규칙을 따르며 앱 세션 시작 시 표시됩니다.

### 2단계: 지연 시간 선택 {#step-2-select-delay-length}

트리거 조건이 충족된 후 Campaign을 보내기까지 대기할 시간을 선택합니다. 선택한 지연 시간이 메시지의 발송 기간보다 길면 해당 Campaign을 받는 사용자가 없습니다.

인앱 메시지 Campaign은 트리거 이벤트 후 최대 2시간(7,200초)까지 전달을 지연할 수 있습니다. 지연 옵션은 **즉시**와 **지연 후**입니다. 더 긴 대기 시간이 필요하면 Canvas에서 인앱 메시지 단계 앞에 [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) 단계를 추가하세요.

{% alert important %}
Braze는 커스텀 이벤트와 함께 전송된 타임스탬프를 사용하여 실행 기반 Campaign의 지연을 평가합니다. 해당 타임스탬프가 과거 날짜인 경우, Braze는 지연이 이미 경과한 것으로 처리하여 메시지를 즉시 또는 예상보다 일찍 보낼 수 있습니다. 의도하지 않은 전달 타이밍을 방지하려면 커스텀 이벤트 타임스탬프를 현재 시간으로 전송하세요.
{% endalert %}

또한, Campaign이 시작된 후 트리거 이벤트를 완료한 사용자가 지연이 경과한 후 가장 먼저 메시지를 받습니다. Campaign 시작 전에 트리거 이벤트를 완료한 사용자는 해당 Campaign을 받을 자격이 없습니다.

**다음 요일에**를 선택하여 특정 요일에 Campaign을 보내거나, **특정 일수 후에**를 선택하여 미래의 정해진 일수 후에 보낼 수도 있습니다. 또는 수동으로 전달 시간을 선택하는 대신 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)을 사용하여 메시지를 보낼 수 있습니다.

### 3단계: 예외 이벤트 선택 {#step-3-select-exception-events}

사용자가 이 Campaign을 받지 못하도록 하는 예외 이벤트를 선택합니다. 트리거된 메시지가 시간 지연 후에 전송되는 경우에만 이 작업을 수행할 수 있습니다. [예외 이벤트]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events)는 구매 수행, 세션 시작, Campaign에 지정된 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) 수행 또는 커스텀 이벤트 수행이 될 수 있습니다.

사용자가 트리거 이벤트를 완료한 후 시간 지연으로 인해 메시지가 전송되기 전에 예외 이벤트를 완료하면, 해당 사용자는 Campaign을 받지 않습니다. 예외 이벤트로 인해 Campaign을 받지 못한 사용자는 다음에 트리거 이벤트를 완료하면 자동으로 수신 자격이 부여되며, 사용자의 [재적격성]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 설정하지 않았더라도 마찬가지입니다.

예외 이벤트 사용에 대한 자세한 내용은 [예시](#examples)를 참조하세요.

트리거 이벤트와 일치하는 예외 이벤트가 있는 Campaign을 보내면, Braze는 해당 Campaign을 취소하고 예외 이벤트의 메시지 전달 시간에 기반하여 자동으로 새 Campaign을 재예약합니다. 예를 들어, 첫 번째 트리거 이벤트가 5분에 시작되고 예외 이벤트가 10분에 시작되면, 예외 이벤트의 10분이 공식 Campaign의 메시지 전달 시간이 됩니다.

{% alert note %}
Campaign의 트리거 이벤트와 예외 이벤트를 모두 "세션 시작"으로 설정할 수는 없습니다. 하지만 이 옵션 외에 다른 커스텀 이벤트를 선택할 수는 있습니다.
{% endalert %}

### 4단계: 기간 지정 {#step-4-assign-duration}

시작 시간과 선택적 종료 시간을 지정하여 Campaign의 기간을 지정합니다.

사용자가 지정된 시간 내에 트리거 이벤트를 완료하지만 예약된 지연으로 인해 시간 범위 밖에서 메시지 수신 자격을 얻으면, 해당 사용자는 Campaign을 받지 않습니다. 따라서 시간 지연을 메시지의 시간 범위보다 길게 설정하면 Campaign을 받는 사용자가 없습니다. 또한 사용자의 [현지 시간대]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns)로 메시지를 보낼 수 있습니다.

### 5단계: 시간대 선택 {#step-5-select-time-frame}

사용자가 하루 중 특정 시간대에 Campaign을 받을지 선택합니다. 메시지에 시간대를 설정한 경우, 사용자가 시간대 밖에서 트리거 이벤트를 완료하거나 메시지 지연으로 인해 시간대를 놓치면 기본적으로 사용자는 메시지를 받지 않습니다.

사용자가 시간대 내에서 트리거 이벤트를 완료했지만 메시지 지연으로 인해 시간대를 벗어나는 경우, **전달 시간이 지정된 시간대를 벗어나면 다음 가용 시간에 전송** 체크박스를 선택하여 해당 사용자가 여전히 Campaign을 받을 수 있도록 할 수 있습니다.

사용자가 시간대를 놓쳐서 메시지를 받지 못한 경우, 사용자의 [재적격성]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 설정하지 않았더라도 다음에 트리거 이벤트를 완료하면 수신 자격이 유지됩니다. 사용자의 재적격성을 설정한 경우, 사용자는 지정된 시간대 내에 자격을 충족할 때마다 트리거 이벤트를 완료할 때 Campaign을 받을 수 있습니다.

Campaign에 특정 기간도 지정한 경우, 메시지를 받으려면 사용자가 해당 기간과 특정 시간대 모두에서 자격을 충족해야 합니다.

### 6단계: 재적격성 결정 {#step-6-determine-re-eligibility}

사용자가 Campaign에 [재적격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)할 수 있는지 여부를 결정합니다. 사용자의 재적격성을 허용하면 사용자가 Campaign을 다시 받기 전 시간 지연을 지정할 수 있습니다. 이를 통해 트리거 Campaign이 "스팸성"으로 되는 것을 방지할 수 있습니다.

## 예시 {#examples}

트리거된 캠페인은 트랜잭션 기반 또는 성과 기반 메시지에 매우 효과적입니다.

트랜잭션 캠페인에는 사용자가 구매를 완료하거나 장바구니에 항목을 추가한 후 전송되는 메시지가 포함됩니다. 후자의 경우는 예외 이벤트의 장점을 활용하는 캠페인의 좋은 예입니다. 예를 들어, 사용자가 장바구니에 담아두고 아직 구매하지 않은 항목을 알려주는 캠페인이 있다고 가정해 보겠습니다. 이 경우 예외 이벤트는 사용자가 장바구니에 있는 제품을 구매하는 것입니다. 성과 기반 캠페인의 경우, 사용자가 전환을 완료하거나 게임 레벨을 클리어한 후 5분 뒤에 메시지를 보낼 수 있습니다.

또한 웰컴 캠페인을 만들 때 사용자가 등록하거나 계정을 설정한 후 메시지를 트리거하여 전송할 수 있습니다. 등록 후 여러 날에 걸쳐 메시지를 분산하여 전송하면 체계적인 온보딩 프로세스를 구성할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 인앱 메시지 캠페인의 트리거 이후 최대 지연 시간은 얼마인가요? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

2시간(7,200초)입니다. 사용 가능한 지연 옵션과 더 긴 대기 시간 설정 방법은 [2단계: 지연 시간 선택](#step-2-select-delay-length)을 참조하세요.

### 사용자가 트리거된 캠페인을 수신하지 못한 이유는 무엇인가요? {#why-did-a-user-not-receive-my-triggered-campaign}

다음 중 하나의 이유로 트리거 이벤트를 완료한 사용자가 캠페인을 수신하지 못할 수 있습니다:

- 시간 지연이 완전히 경과하기 전에 사용자가 예외 이벤트를 완료한 경우.
- Liquid [`abort_message` 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)이 사용되었으며, `abort_message` 로직이나 규칙에 따라 메시지가 중단된 경우.
- 시간 지연으로 인해 캠페인 기간이 종료된 후에 사용자가 수신 자격을 갖추게 된 경우.
- 시간 지연으로 인해 지정된 시간대 외에 사용자가 캠페인 수신 자격을 갖추게 된 경우.
- 사용자가 이미 해당 캠페인을 수신한 경우(공유 채널 식별자를 통한 기여도 포함—예를 들어, 수신, 열람 또는 클릭한 다른 사용자와 이메일을 공유하는 경우)이며, 사용자가 재수신 자격을 얻지 못하는 경우.
- 사용자가 캠페인 재수신 자격이 있지만 일정 기간이 경과한 후에만 다시 트리거할 수 있으며, 해당 기간이 아직 경과하지 않은 경우.

트리거된 캠페인을 이벤트 발생 시점에 기록된 사용자 데이터로 [세분화]({{site.baseurl}}/user_guide/audience/segments)하면 [경합 조건]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)이 발생할 수 있습니다. 이는 캠페인이 세분화의 기준으로 사용하는 사용자 속성이 변경되었지만, 캠페인이 발송될 때 해당 변경 사항이 아직 사용자에 대해 처리되지 않은 경우에 발생합니다. 캠페인은 진입 시 세그먼트 멤버십을 확인하므로, 사용자가 캠페인을 수신하지 못하는 결과가 발생할 수 있습니다.

예를 들어, 방금 등록한 남성 사용자에게 이벤트 트리거 캠페인을 보내려고 한다고 가정해 보겠습니다. 사용자가 등록하면 커스텀 이벤트 `registration`을 기록하고 동시에 사용자의 `gender` 속성을 설정합니다. 이 이벤트가 Braze가 사용자의 성별을 처리하기 전에 캠페인을 트리거할 수 있으며, 이로 인해 사용자가 캠페인을 수신하지 못할 수 있습니다.

모범 사례로, 캠페인이 세분화의 기준으로 사용하는 속성이 이벤트 전에 Braze 서버로 전송되도록 해야 합니다. 이것이 불가능한 경우, 전달을 보장하는 가장 좋은 방법은 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)를 사용하여 관련 사용자 속성을 이벤트에 첨부하고, 세분화 필터 대신 특정 이벤트 속성정보에 대한 속성정보 필터를 적용하는 것입니다. 예시의 경우, 커스텀 이벤트 `registration`에 `gender` 속성정보를 추가하면, 캠페인이 트리거될 때 Braze에 필요한 데이터가 있음을 보장할 수 있습니다.

또한, 캠페인이 실행 기반이고 지연이 있는 경우, **발송 시점에 세그먼트 멤버십을 재평가** 옵션을 선택하여 메시지가 발송될 때 사용자가 여전히 타겟 오디언스에 속하는지 확인할 수 있습니다.

#### 오디언스 기준 평가 {#audience-criteria-evaluation}

발송 전 지연이 포함된 캠페인(사용량 제한, 현지 시간대, Intelligent Timing 또는 트리거 스케줄 포함)의 경우, 세그먼트가 재평가되는 시점은 캠페인 유형과 설정에 따라 다릅니다.

지연이 있는 실행 기반 캠페인에서 **발송 시점에 세그먼트 멤버십을 재평가**를 선택하면, 메시지가 발송되기 전에 사용자가 재평가되므로, 발송 시점에 세그먼트 기준을 여전히 충족하는 사용자만 메시지를 수신합니다.

캠페인이 특정 커스텀 이벤트에 의해 트리거되고 세그먼트를 오디언스로 선택한 경우, 사용자가 해당 세그먼트에 포함되려면 동일한 커스텀 이벤트를 수행해야 합니다. 이는 실행 기반 캠페인이 트리거되기 전에 사용자가 오디언스에 포함되어 있어야 함을 의미합니다. 트리거된 캠페인의 일반적인 워크플로는 다음과 같습니다:

1. **오디언스 가입:** 사용자가 커스텀 이벤트를 수행하면 캠페인의 타겟 오디언스에 추가됩니다.
2. **이메일 트리거:** 이메일이 발송되기 전에 사용자가 오디언스에 포함되어 있어야 하므로, 이메일을 트리거하려면 사용자가 커스텀 이벤트를 다시 수행해야 합니다.

타겟 오디언스를 모든 사용자를 포함하도록 변경하거나, 이벤트를 수행할 것으로 예상되는 사용자가 메시지가 트리거되기 위해 이미 캠페인의 오디언스에 포함되어 있는지 확인하는 것을 권장합니다.

![오디언스 기준 평가와 관련된 스크린샷.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### 커스텀 이벤트 문제 해결 {#troubleshooting-custom-events}

먼저, 커스텀 이벤트가 Braze로 전달되고 있는지 확인합니다. **Analytics** > **커스텀 이벤트 보고서**로 이동한 후, 해당 커스텀 이벤트와 날짜 범위를 선택합니다. 이벤트가 표시되지 않으면, 올바르게 설정되었는지와 사용자가 올바른 동작을 수행했는지 확인합니다.

커스텀 이벤트가 표시되면, 다음을 수행하여 추가로 문제를 해결합니다:

- 사용자의 프로필 다운로드를 확인하여 이벤트를 트리거했는지와 트리거한 시점을 확인합니다. 이벤트가 트리거되었다면, 이벤트가 트리거된 타임스탬프를 캠페인이 활성화된 시점과 비교합니다. 캠페인이 활성화되기 전에 이벤트가 트리거되었을 수 있습니다.
- 캠페인 및 타겟팅에 사용된 세그먼트의 체인지로그를 검토하여, 커스텀 이벤트가 트리거되었을 때 사용자가 세그먼트에 속해 있었는지 확인합니다. 세그먼트에 속하지 않았다면 캠페인을 수신하지 못했을 것입니다.
- 세분화를 통해 사용자가 대조군에 배정되어 캠페인 수신이 차단되었는지 확인합니다.
- 스케줄된 지연이 있는 경우, 사용자의 커스텀 이벤트가 지연 시작 전에 트리거되었는지 확인합니다. 지연 전에 이벤트가 트리거되었다면 캠페인을 수신하지 못했을 것입니다.

{% alert note %}
인앱 메시지는 SDK를 통해 전송된 이벤트로만 트리거할 수 있으며, REST API로는 트리거할 수 없습니다.
{% endalert %}

### 실행 기반 캠페인은 오디언스 멤버십을 언제 평가하나요? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze는 메시지가 발송되기 전에 트리거 이벤트를 처리할 때 오디언스 멤버십을 평가합니다. 기본적으로 Braze는 큐 등록 시점에 사용자가 타겟 오디언스와 일치하는지 확인합니다. 캠페인에 지연이 있는 경우, **발송 시점에 세그먼트 멤버십을 재평가**를 선택하여 발송 직전에 오디언스 기준을 다시 확인할 수 있습니다—예를 들어, 사용자가 트리거 동작을 수행한 후 발송이 완료되기 전에 오디언스에서 이탈할 수 있는 경우에 유용합니다.

자세한 내용은 [오디언스 기준 평가](#audience-criteria-evaluation)를 참조하세요.