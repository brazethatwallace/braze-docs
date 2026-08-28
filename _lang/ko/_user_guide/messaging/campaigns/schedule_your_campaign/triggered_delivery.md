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

## 트리거 캠페인 설정하기 {#setting-up-a-triggered-campaign}

### 1단계: 트리거 이벤트 선택 {#step-1-select-a-trigger-event}

트리거 이벤트를 선택합니다. 이벤트는 카테고리별로 구성되어 있으며, 워크스페이스와 활성화된 채널에 따라 사용할 수 있습니다.

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
    - **Send an SMS inbound message**
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

**이커머스** 그룹에는 **Perform Product Viewed Event**, **Perform Order Cancelled Event**, **Perform Order Refunded Event** 등 권장 이커머스 이벤트도 표시됩니다. 이 옵션들은 이벤트 이름이 미리 채워진 **Perform Custom Event**를 사용합니다.

인앱 메시지 캠페인은 더 제한된 트리거 세트를 지원합니다: **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event**, **Interact With Campaign**. 인앱 메시지 캠페인의 경우, **Interact With Campaign**은 모든 캠페인 또는 특정 캠페인에서 푸시 알림을 여는 것만 포함합니다. 아래 캠페인 상호작용 목록은 포함하지 않습니다.

인앱 메시지 이외의 캠페인에서 **Interact With Campaign**, **Interact With Step** 또는 **Interact with Landing Page**를 선택하면 트리거할 상호작용을 선택합니다. 각 트리거는 고유한 상호작용을 제공하며, 사용 가능한 상호작용은 활성화된 채널에 따라 달라집니다.

{% details Interact With Campaign의 상호작용 %}

- **인앱 메시지 조회**
- **인앱 메시지 클릭**
- **인앱 메시지 버튼 1 클릭**
- **인앱 메시지 버튼 2 클릭**
- **인앱 메시지 설문조사 제출**
- **이메일 클릭**
- **이메일 열기**
- **이메일 열기(머신 열람)**
- **이메일 열기(기타 열람)**
- **이메일 내 별칭 클릭**
- **모든 캠페인 또는 캔버스 단계에서 별칭 클릭**
- **푸시 알림 직접 열기**
- **푸시 알림 버튼 클릭**
- **Push Stories 페이지 클릭**
- **전환 이벤트 수행**
- **이메일 수신**
- **푸시 알림 수신**
- **웹훅 수신**
- **SMS 수신**
- **단축 SMS 링크 클릭**
- **콘텐츠 카드 조회**
- **콘텐츠 카드 클릭**
- **콘텐츠 카드 닫기**
- **배너 조회**
- **배너 클릭**
- **배너 닫기**
- **추적된 WhatsApp 링크 클릭**
- **추적된 LINE 링크 클릭**
- **추적된 KakaoTalk 링크 클릭**
- **대조군에 등록됨**

{% enddetails %}

{% details Interact With Step의 상호작용 %}

- **인앱 메시지 조회**
- **인앱 메시지 노출 가능 기간 시작**
- **인앱 메시지 설문조사 제출**
- **이메일 클릭**
- **이메일 열기**
- **이메일 열기(머신 열람)**
- **이메일 열기(기타 열람)**
- **이메일 내 별칭 클릭**
- **모든 캠페인 또는 캔버스 단계에서 별칭 클릭**
- **푸시 알림 직접 열기**
- **푸시 알림 버튼 클릭**
- **Push Stories 페이지 클릭**
- **이메일 수신**
- **푸시 알림 수신**
- **웹훅 수신**
- **SMS 수신**
- **단축 SMS 링크 클릭**
- **콘텐츠 카드 조회**
- **콘텐츠 카드 클릭**
- **콘텐츠 카드 닫기**
- **배너 조회**
- **배너 클릭**
- **배너 닫기**
- **추적된 WhatsApp 링크 클릭**
- **추적된 LINE 링크 클릭**
- **추적된 KakaoTalk 링크 클릭**

{% enddetails %}

{% details Interact with Landing Page의 상호작용 %}

- **양식 제출**
- **설문조사 제출**

{% enddetails %}

Braze [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events)를 통해 트리거 이벤트를 추가로 필터링할 수도 있습니다. 이를 통해 커스텀 이벤트 및 인앱 구매에 대한 이벤트 속성정보를 사용자 지정할 수 있습니다. 이 기능을 사용하면 커스텀 이벤트의 특정 속성을 기반으로 메시지를 수신할 사용자를 더욱 세밀하게 맞춤 설정할 수 있어, 더 높은 수준의 캠페인 개인화와 더 정교한 데이터 수집이 가능합니다.

예를 들어, "장바구니 가치" 속성정보 필터로 추가 타겟팅된 유기한 장바구니 커스텀 이벤트가 있는 캠페인이 있다고 가정해 보겠습니다. 이 캠페인은 장바구니에 $100에서 $200 사이의 상품을 남긴 사용자에게만 도달합니다.

![장바구니 가치가 $100에서 $200 사이인 커스텀 이벤트 속성정보로 필터링된 유기한 장바구니 캠페인.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
트리거 이벤트 **Start Session**은 캠페인의 Segment가 신규 사용자에게 적용되는 경우(예: Segment가 세션이 없는 사용자로 구성된 경우) 사용자의 맨 첫 앱 열기가 될 수 있습니다.
{% endalert %}

트리거된 캠페인은 여전히 특정 Segment의 사용자에게 보낼 수 있으므로, Segment에 속하지 않는 사용자는 트리거 이벤트를 완료하더라도 캠페인을 수신하지 않습니다.

사용자가 프로필에 이메일 주소를 추가하는 트리거 이벤트와 관련하여 다음 규칙이 적용됩니다:

- 트리거 이벤트는 사용자 프로필 속성이 업데이트된 후에 실행됩니다. 이는 캠페인의 Segment 및 필터 평가가 속성 업데이트 이후에 이루어진다는 것을 의미합니다. 이를 통해 "이메일 주소가 gmail.com과 일치" 같은 필터를 설정하여 Gmail 사용자에게만 전송하고, 이메일 주소를 추가하는 즉시 실행되는 트리거 캠페인을 만들 수 있습니다.
- 트리거 이벤트는 사용자 프로필에 이메일 주소가 추가될 때 실행됩니다. 동일한 이메일 주소로 여러 고객 프로필을 생성한 경우, 캠페인은 각 고객 프로필에 대해 한 번씩 여러 번 실행될 수 있습니다.

또한 트리거된 인앱 메시지는 여전히 인앱 메시지 전달 규칙을 따르며 앱 세션 시작 시 표시됩니다.

### 2단계: 지연 시간 선택 {#step-2-select-delay-length}

트리거 조건이 충족된 후 캠페인을 발송하기까지 대기할 시간을 선택합니다. 선택한 지연 시간이 메시지의 발송 가능 기간보다 긴 경우, 캠페인을 수신하는 사용자가 없습니다.

인앱 메시지 캠페인은 트리거 이벤트 후 최대 2시간(7,200초)까지 전달을 지연할 수 있습니다. 지연 옵션은 **즉시**와 **지연 후**입니다. 더 긴 대기가 필요한 경우, Canvas에서 인앱 메시지 단계 앞에 [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) 단계를 추가하세요.

{% alert important %}
Braze는 실행 기반 캠페인의 지연을 평가하기 위해 커스텀 이벤트와 함께 전송된 타임스탬프를 사용합니다. 해당 타임스탬프가 과거 시간으로 설정된 경우, Braze는 지연이 이미 경과한 것으로 처리하여 메시지를 즉시 또는 예상보다 일찍 발송할 수 있습니다. 의도치 않은 전달 타이밍을 방지하려면 커스텀 이벤트 타임스탬프를 현재 시간으로 전송하세요.
{% endalert %}

또한 캠페인이 시작된 후 트리거 이벤트를 완료한 사용자가 지연 시간이 경과하면 가장 먼저 메시지를 수신합니다. 캠페인 시작 전에 트리거 이벤트를 완료한 사용자는 캠페인 수신 자격이 없습니다.

**다음 요일에** 를 선택하여 특정 요일에 캠페인을 보내거나, **캘린더 일수 후에**를 선택하여 지정된 일수 후에 보낼 수도 있습니다. 또는 수동으로 전달 시간을 선택하는 대신 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)을 사용하여 메시지를 보낼 수 있습니다.

### 3단계: 예외 이벤트 선택 {#step-3-select-exception-events}

이 캠페인을 수신할 자격에서 사용자를 제외하는 예외 이벤트를 선택합니다. 트리거된 메시지가 시간 지연 후에 발송되는 경우에만 이 작업을 수행할 수 있습니다. [예외 이벤트]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events)는 구매 완료, 세션 시작, 캠페인의 지정된 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) 중 하나 수행, 또는 커스텀 이벤트 수행이 될 수 있습니다.

사용자가 트리거 이벤트를 완료했지만 시간 지연으로 인해 메시지가 발송되기 전에 예외 이벤트를 완료한 경우, 해당 사용자는 캠페인을 수신하지 않습니다. 예외 이벤트로 인해 캠페인을 수신하지 못한 사용자는 [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 설정하지 않더라도 다음에 트리거 이벤트를 완료하면 자동으로 수신 자격이 부여됩니다.

예외 이벤트 사용에 대한 자세한 내용은 [예시](#examples)를 참조하세요.

트리거 이벤트가 예외 이벤트와 일치하는 캠페인을 보내면, Braze는 해당 캠페인을 취소하고 예외 이벤트의 메시지 전달 시간에 기반하여 새 캠페인을 자동으로 재스케줄합니다. 예를 들어, 첫 번째 트리거 이벤트가 5분에 시작하고 예외 이벤트가 10분에 시작하는 경우, 예외 이벤트의 10분이 공식 캠페인의 메시지 전달 시간이 됩니다.

{% alert note %}
"세션 시작"을 캠페인의 트리거 이벤트와 예외 이벤트로 동시에 사용할 수 없습니다. 그러나 이 옵션 외에 다른 커스텀 이벤트를 항상 선택할 수 있습니다.
{% endalert %}

### 4단계: 기간 지정 {#step-4-assign-duration}

캠페인의 시작 시간과 선택적으로 종료 시간을 지정하여 캠페인 기간을 설정합니다.

사용자가 지정된 시간 범위 내에 트리거 이벤트를 완료했지만 스케줄된 지연으로 인해 시간 범위 밖에서 메시지 자격이 부여되는 경우, 해당 사용자는 캠페인을 수신하지 않습니다. 따라서 메시지의 시간 범위보다 긴 시간 지연을 설정하면 캠페인을 수신하는 사용자가 없습니다. 또한 사용자의 [현지 시간대]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns)에 맞춰 메시지를 보내도록 설정할 수 있습니다.

### 5단계: 시간 범위 선택 {#step-5-select-time-frame}

사용자가 하루 중 특정 시간대에 캠페인을 수신할지 선택합니다. 메시지에 시간 범위를 설정한 경우, 사용자가 시간 범위 밖에서 트리거 이벤트를 완료하거나 메시지 지연으로 인해 시간 범위를 놓치면 기본적으로 사용자는 메시지를 수신하지 않습니다.

사용자가 시간 범위 내에 트리거 이벤트를 완료했지만 메시지 지연으로 인해 시간 범위를 벗어나는 경우, **전달 시간이 지정된 시간대를 벗어나면 다음 가능한 시간에 보내기** 체크박스를 선택하면 해당 사용자가 여전히 캠페인을 수신할 수 있습니다.

사용자가 시간 범위를 놓쳐서 메시지를 수신하지 못한 경우에도, [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 설정하지 않았더라도 다음에 트리거 이벤트를 완료하면 수신 자격이 부여됩니다. 재자격을 설정한 경우, 사용자는 지정된 시간 범위 내에 자격을 충족하는 한 트리거 이벤트를 완료할 때마다 캠페인을 수신할 수 있습니다.

캠페인에 특정 기간도 설정한 경우, 사용자는 기간과 특정 시간대 모두에서 자격을 충족해야 메시지를 수신합니다.

### 6단계: 재자격 결정 {#step-6-determine-re-eligibility}

사용자가 캠페인에 대해 [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 받을 수 있는지 결정합니다. 사용자에게 재자격을 허용하는 경우, 사용자가 캠페인을 다시 수신하기까지의 시간 지연을 지정할 수 있습니다. 이를 통해 트리거된 캠페인이 "스팸"처럼 되는 것을 방지할 수 있습니다.

## 예시 {#examples}

트리거 캠페인은 트랜잭션 기반 또는 목표 달성 기반 메시지에 매우 효과적입니다.

트랜잭션 캠페인에는 사용자가 구매를 완료하거나 장바구니에 항목을 추가한 후에 전송되는 메시지가 포함됩니다. 후자의 경우는 예외 이벤트를 활용하면 좋은 캠페인의 대표적인 예입니다. 사용자가 장바구니에 담아 두었지만 아직 구매하지 않은 항목을 리마인드하는 캠페인을 예로 들어 보겠습니다. 이 경우 예외 이벤트는 사용자가 장바구니에 있는 제품을 구매하는 것입니다. 목표 달성 기반 캠페인의 경우, 사용자가 전환을 완료하거나 게임 레벨을 클리어한 후 5분 뒤에 메시지를 보낼 수 있습니다.

또한, 웰컴 캠페인을 만들 때 사용자가 등록하거나 계정을 설정한 후에 메시지가 전송되도록 트리거할 수 있습니다. 등록 이후 다른 날짜에 걸쳐 메시지를 순차적으로 보내면 체계적인 온보딩 프로세스를 구성할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 인앱 메시지 캠페인에서 트리거 후 최대 지연 시간은 얼마인가요? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

2시간(7,200초)입니다. 사용 가능한 지연 옵션과 더 긴 대기 시간을 설정하는 방법은 [2단계: 지연 시간 선택](#step-2-select-delay-length)을 참조하세요.

### 사용자가 트리거된 Campaign을 수신하지 못하는 이유는 무엇인가요? {#why-did-a-user-not-receive-my-triggered-campaign}

다음 중 하나라도 해당되면, 트리거 이벤트를 완료한 사용자가 Campaign을 수신하지 못할 수 있습니다:

- 시간 지연이 완전히 경과하기 전에 사용자가 예외 이벤트를 완료한 경우.
- Liquid [`abort_message` 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)이 사용되었고 `abort_message` 로직이나 규칙에 따라 메시지가 중단된 경우.
- 시간 지연으로 인해 캠페인 기간이 종료된 후에야 사용자가 수신 자격을 갖게 된 경우.
- 시간 지연으로 인해 지정된 하루 중 시간대 외에 사용자가 수신 자격을 갖게 된 경우.
- 사용자가 이미 Campaign을 수신한 경우(공유 채널 식별자를 통한 기여도 포함—예를 들어, 해당 Campaign을 수신, 열람 또는 클릭한 다른 사용자와 이메일을 공유하는 경우), 그리고 사용자가 다시 수신 자격을 얻지 못하는 경우.
- 사용자가 Campaign을 다시 수신할 수 있는 자격이 있지만 일정 기간 후에만 다시 트리거할 수 있으며, 해당 기간이 아직 경과하지 않은 경우.

트리거된 Campaign을 이벤트 시점에 기록된 사용자 데이터로 [세분화]({{site.baseurl}}/user_guide/audience/segments)하면 [경합 조건]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions)이 발생할 수 있습니다. 이는 Campaign이 세분화 기준으로 사용하는 사용자 속성이 변경되었지만, Campaign이 전송될 때 해당 변경 사항이 사용자에게 아직 처리되지 않은 경우에 발생합니다. Campaign은 진입 시 Segment 멤버십을 확인하므로, 이로 인해 사용자가 Campaign을 수신하지 못할 수 있습니다.

예를 들어, 방금 등록한 남성 사용자에게 이벤트 트리거 Campaign을 보내려 한다고 가정해 보겠습니다. 사용자가 등록하면 커스텀 이벤트 `registration`을 기록하고 동시에 사용자의 `gender` 속성을 설정합니다. Braze가 사용자의 성별을 처리하기 전에 이벤트가 Campaign을 트리거할 수 있으며, 이 경우 사용자가 Campaign을 수신하지 못하게 됩니다.

모범 사례로, Campaign이 세분화 기준으로 사용하는 속성이 이벤트보다 먼저 Braze 서버에 플러시되도록 해야 합니다. 이것이 불가능한 경우, 전달을 보장하는 가장 좋은 방법은 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)를 사용하여 관련 사용자 속성을 이벤트에 첨부하고, 세분화 필터 대신 특정 이벤트 속성정보에 대한 속성정보 필터를 적용하는 것입니다. 위 예시의 경우, 커스텀 이벤트 `registration`에 `gender` 속성정보를 추가하면 Campaign이 트리거될 때 필요한 데이터가 Braze에 확실히 전달됩니다.

또한, Campaign이 실행 기반이고 지연이 있는 경우 **전송 시 Segment 멤버십 재평가** 옵션을 선택하여 메시지가 전송될 때 사용자가 여전히 타겟 오디언스에 포함되어 있는지 확인할 수 있습니다.

#### 오디언스 기준 평가 {#audience-criteria-evaluation}

전송 전 지연이 포함된 Campaign(사용량 제한, 현지 시간대, Intelligent Timing 또는 트리거 스케줄 포함)의 경우, Segment가 재평가되는 시점은 Campaign 유형과 설정에 따라 다릅니다.

지연이 있는 실행 기반 Campaign에서 **전송 시 Segment 멤버십 재평가**를 선택하면, 메시지가 전송되기 전에 사용자가 재평가되므로, 전송 시점에 Segment 기준을 여전히 충족하는 사용자만 메시지를 수신합니다.

Campaign이 특정 커스텀 이벤트에 의해 트리거되고 오디언스로 Segment를 선택한 경우, 사용자는 해당 Segment에 포함되려면 동일한 커스텀 이벤트를 수행해야 합니다. 즉, 실행 기반 Campaign이 트리거되려면 사용자가 먼저 오디언스의 일부여야 합니다. 트리거된 Campaign의 일반적인 워크플로는 다음과 같습니다:

1. **오디언스에 합류:** 사용자가 커스텀 이벤트를 수행하면 Campaign의 타겟 오디언스에 추가됩니다.
2. **이메일 트리거:** 이메일을 전송하려면 사용자가 먼저 오디언스에 포함되어야 하므로, 커스텀 이벤트를 다시 수행해야 이메일이 트리거됩니다.

타겟 오디언스를 모든 사용자로 변경하거나, 이벤트를 수행할 것으로 예상되는 사용자가 이미 Campaign의 오디언스에 포함되어 있는지 확인하여 메시지가 트리거되도록 하는 것을 권장합니다.

![오디언스 기준 평가와 관련된 스크린샷.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### 커스텀 이벤트 문제 해결 {#troubleshooting-custom-events}

먼저, 커스텀 이벤트가 Braze로 전달되고 있는지 확인합니다. **Analytics** > **커스텀 이벤트 보고서**로 이동한 다음 해당 커스텀 이벤트와 기간을 선택합니다. 이벤트가 표시되지 않으면 올바르게 설정되었는지, 사용자가 올바른 작업을 수행했는지 확인합니다.

커스텀 이벤트가 표시되면, 다음을 수행하여 추가 문제 해결을 합니다:

- 사용자의 프로필 다운로드를 확인하여 이벤트를 트리거했는지와 트리거 시점을 확인합니다. 이벤트가 트리거된 경우, 이벤트 트리거 타임스탬프를 Campaign이 라이브된 시간과 비교합니다. Campaign이 라이브되기 전에 이벤트가 트리거되었을 수 있습니다.
- Campaign과 타겟팅에 사용된 Segments의 체인지로그를 검토하여 커스텀 이벤트가 트리거된 시점에 사용자가 해당 Segment에 있었는지 확인합니다. Segment에 없었다면 Campaign을 수신하지 못합니다.
- 사용자가 세분화를 통해 대조군에 편입되어 Campaign 수신이 차단되었는지 확인합니다.
- 스케줄된 지연이 있는 경우, 사용자의 커스텀 이벤트가 지연 전에 트리거되었는지 확인합니다. 지연 전에 이벤트가 트리거되었다면 Campaign을 수신하지 못합니다.

{% alert note %}
인앱 메시지는 SDK를 통해 전송된 이벤트로만 트리거할 수 있으며, REST API로는 트리거할 수 없습니다.
{% endalert %}

### 실행 기반 Campaign은 언제 오디언스 멤버십을 평가하나요? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze는 트리거 이벤트를 처리할 때, 메시지가 전송되기 전에 오디언스 멤버십을 평가합니다. 기본적으로 Braze는 대기열 등록 시점에 사용자가 타겟 오디언스에 해당하는지 확인합니다. Campaign에 지연이 있는 경우, **전송 시 Segment 멤버십 재평가**를 선택하여 전송 직전에 오디언스 기준을 다시 확인할 수 있습니다—예를 들어, 사용자가 트리거 작업을 수행한 후 전송이 완료되기 전에 오디언스에서 이탈할 수 있는 경우에 유용합니다.

자세한 내용은 [오디언스 기준 평가](#audience-criteria-evaluation)를 참조하세요.