---
nav_title: 실행 기반 전달
article_title: 실행 기반 전달
page_order: 1
page_type: reference
description: "이 참조 문서에서는 사용자가 특정 이벤트를 완료한 후 Campaign 발송을 트리거하는 방법을 설명합니다."
tool: Campaigns

---

# 실행 기반 전달 {#action-based-delivery}

> 실행 기반 전달 Campaign 또는 이벤트 트리거 Campaign은 트랜잭션 또는 성과 기반 메시지에 매우 효과적입니다. 특정 날짜에 Campaign을 발송하는 대신, 사용자가 특정 이벤트를 완료한 후 발송되도록 트리거할 수 있습니다.

## 트리거 Campaign 설정 {#setting-up-a-triggered-campaign}

### 1단계: 트리거 이벤트 선택 {#step-1-select-a-trigger-event}

트리거 이벤트를 선택합니다. 다음 중 하나를 포함할 수 있습니다:
- 구매하기
- 세션 시작하기
- 커스텀 이벤트 수행하기
- Campaign의 주요 전환 이벤트 수행하기
- 고객 프로필에 이메일 주소 추가하기
- 커스텀 속성 값 변경하기
- 구독 상태 업데이트하기
- 구독 그룹 상태 업데이트하기
- 다른 Campaign과 상호작용하기
    - 인앱 메시지 보기
    - 인앱 메시지 클릭
    - 인앱 메시지 버튼 클릭
    - 이메일 클릭
    - 이메일에서 별칭 클릭
    - Campaign 또는 캔버스 단계에서 별칭 클릭
    - 이메일 열기
    - 이메일 열기(기계 열기)
    - 이메일 열기(기타 열기)
    - 푸시 알림 직접 열기
    - 푸시 알림 버튼 클릭
    - Push Stories 페이지 클릭
    - 전환 이벤트 수행
    - 이메일 수신
    - SMS 수신
    - 단축 SMS 링크 클릭
    - 푸시 알림 수신
    - 웹훅 수신
    - 대조군에 등록됨
    - 콘텐츠 카드 보기
    - 콘텐츠 카드 클릭
    - 콘텐츠 카드 닫기
- 위치 진입하기
- 다른 Campaign의 예외 이벤트 수행하기
- 캔버스 단계와 상호작용하기
- 지오펜스 트리거하기
- SMS 인바운드 메시지 보내기
- WhatsApp 인바운드 메시지 보내기

Braze [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events)를 통해 트리거 이벤트를 추가로 필터링할 수도 있습니다. 이를 통해 커스텀 이벤트 및 인앱 구매에 대한 사용자 지정 가능한 이벤트 속성정보를 사용할 수 있습니다. 이 기능을 사용하면 커스텀 이벤트의 특정 속성을 기반으로 메시지를 수신하는 사용자를 더 세밀하게 조정할 수 있어, Campaign 개인화를 강화하고 더 정교한 데이터 수집이 가능합니다.

예를 들어, "장바구니 금액" 속성정보 필터로 추가 타겟팅된 유기한 장바구니 커스텀 이벤트가 있는 Campaign이 있다고 가정해 보겠습니다. 이 Campaign은 장바구니에 $100에서 $200 사이의 상품을 남겨둔 사용자에게만 도달합니다.

![장바구니 금액이 $100에서 $200 사이인 커스텀 이벤트 속성정보로 필터링된 유기한 장바구니 Campaign.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
Campaign의 Segment가 신규 사용자에게 적용되는 경우, 트리거 이벤트 "세션 시작"은 사용자의 첫 번째 앱 열기가 될 수 있습니다. (예: Segment가 세션이 없는 사용자로 구성된 경우)
{% endalert %}

트리거 Campaign을 특정 Segment의 사용자에게 발송할 수 있으므로, Segment에 속하지 않는 사용자는 트리거 이벤트를 완료하더라도 Campaign을 수신하지 않습니다.

사용자가 프로필에 이메일 주소를 추가하는 트리거 이벤트와 관련하여 다음 규칙이 적용됩니다:

- 트리거 이벤트는 고객 프로필 속성이 업데이트된 후에 실행됩니다. 즉, Campaign의 Segment 및 필터 평가는 속성 업데이트 이후에 이루어집니다. 이는 "이메일 주소가 gmail.com과 일치" 같은 필터를 설정하여 Gmail 사용자에게만 발송하고 이메일 주소를 추가하는 즉시 실행되는 트리거 Campaign을 만들 수 있어 유용합니다.
- 트리거 이벤트는 고객 프로필에 이메일 주소가 추가될 때 실행됩니다. 동일한 이메일 주소로 여러 고객 프로필을 생성한 경우, Campaign이 각 고객 프로필에 대해 한 번씩 여러 번 실행될 수 있습니다.

또한, 트리거된 인앱 메시지는 여전히 인앱 메시지 전달 규칙을 따르며 앱 세션 시작 시 표시됩니다.

![트리거 이벤트 구성 옵션이 표시된 실행 기반 Campaign 전달 스케줄.]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### 2단계: 지연 시간 선택 {#step-2-select-delay-length}

트리거 조건이 충족된 후 Campaign을 발송하기까지 대기할 시간을 선택합니다. 선택한 지연 시간이 메시지의 발송 기간보다 긴 경우, Campaign을 수신하는 사용자가 없게 됩니다.

{% alert important %}
Braze는 실행 기반 Campaign의 지연을 평가하기 위해 커스텀 이벤트와 함께 전송된 타임스탬프를 사용합니다. 해당 타임스탬프가 과거 날짜인 경우, Braze는 지연이 이미 경과한 것으로 처리하여 메시지를 즉시 또는 예상보다 일찍 발송할 수 있습니다. 의도하지 않은 전달 타이밍을 방지하려면 커스텀 이벤트 타임스탬프를 현재 시간으로 전송하세요.
{% endalert %}

또한, Campaign이 시작된 후 트리거 이벤트를 완료한 사용자가 지연이 경과한 후 가장 먼저 메시지를 수신합니다. Campaign 시작 전에 트리거 이벤트를 완료한 사용자는 Campaign 수신 자격이 없습니다.

![2단계: 지연 시간 선택 관련 스크린샷.]({% image_buster /assets/img_archive/schedule_triggered22.png %})

특정 요일("다음" 선택 후 요일 선택) 또는 특정 일수 후("이후" 선택)에 Campaign을 발송하도록 선택할 수도 있습니다. 또는 전달 시간을 수동으로 선택하는 대신 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) 기능을 사용하여 메시지를 발송할 수 있습니다.

![특정 요일("다음" 선택 후 요일 선택) 또는 특정 일수 후("이후" 선택)에 Campaign을 발송하도록 선택할 수 있습니다. 또는 전달 시간을 수동으로 선택하는 대신 Intelligent Timing 기능을 사용하여 메시지를 발송할 수 있습니다.]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![특정 요일("다음" 선택 후 요일 선택) 또는 특정 일수 후("이후" 선택)에 Campaign을 발송하도록 선택할 수 있습니다. 또는 전달 시간을 수동으로 선택하는 대신 Intelligent Timing 기능을 사용하여 메시지를 발송할 수 있습니다.]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### 3단계: 예외 이벤트 선택 {#step-3-select-exception-events}

이 Campaign 수신에서 사용자를 제외할 예외 이벤트를 선택합니다. 트리거된 메시지가 시간 지연 후에 발송되는 경우에만 이 설정이 가능합니다. [예외 이벤트]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events)는 구매하기, 세션 시작하기, Campaign의 지정된 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) 중 하나 수행하기, 또는 커스텀 이벤트 수행하기가 될 수 있습니다. 사용자가 트리거 이벤트를 완료했지만 시간 지연으로 인해 메시지가 발송되기 전에 예외 이벤트를 완료하면, Campaign을 수신하지 않습니다. 예외 이벤트로 인해 Campaign을 수신하지 못한 사용자는 다음에 트리거 이벤트를 완료할 때 자동으로 수신 자격이 부여되며, 이는 사용자의 [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 선택하지 않은 경우에도 마찬가지입니다.

![이 Campaign 수신에서 사용자를 제외할 예외 이벤트를 선택합니다. 트리거된 메시지가 시간 지연 후에 발송되는 경우에만 이 설정이 가능합니다. 예외 이벤트는 구매하기, 세션 시작하기, Campaign의 지정된 전환 이벤트 중 하나 수행하기, 또는 커스텀 이벤트 수행하기가 될 수 있습니다. 사용자가 트리거 이벤트를 완료했지만 시간 지연으로 인해 메시지가 발송되기 전에 예외 이벤트를 완료하면, Campaign을 수신하지 않습니다. 예외 이벤트로 인해 Campaign을 수신하지 못한 사용자는 다음에 트리거 이벤트를 완료할 때 자동으로 수신 자격이 부여되며, 이는 사용자의 재자격을 선택하지 않은 경우에도 마찬가지입니다.]({% image_buster /assets/img_archive/schedule_triggered32.png %})

예외 이벤트 활용 방법에 대한 자세한 내용은 [사용 사례]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#use-cases) 섹션에서 확인할 수 있습니다.

> 트리거 이벤트와 일치하는 예외 이벤트가 있는 Campaign을 발송하면, Braze는 Campaign을 취소하고 예외 이벤트의 메시지 전달 시간을 기반으로 새 Campaign을 자동으로 다시 스케줄합니다. 예를 들어, 첫 번째 트리거 이벤트가 5분에 시작되고 예외 이벤트가 10분에 시작되는 경우, 예외 이벤트의 10분이 공식 Campaign 메시지 전달 시간으로 적용됩니다.

{% alert note %}
"세션 시작"을 Campaign의 트리거 이벤트와 예외 이벤트로 동시에 설정할 수 없습니다. 그러나 이 옵션 외에 다른 커스텀 이벤트를 항상 선택할 수 있습니다.
{% endalert %}

### 4단계: 기간 할당 {#step-4-assign-duration}

Campaign의 시작 시간과 선택적 종료 시간을 지정하여 Campaign 기간을 할당합니다.

![4단계: 기간 할당 관련 스크린샷.]({% image_buster /assets/img_archive/schedule_triggered43.png %})

사용자가 지정된 기간 내에 트리거 이벤트를 완료했지만 스케줄된 지연으로 인해 기간 외에 메시지 수신 자격을 얻게 되면, Campaign을 수신하지 않습니다. 따라서 메시지의 기간보다 긴 시간 지연을 설정하면 Campaign을 수신하는 사용자가 없게 됩니다. 또한, 사용자의 [현지 시간대]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns)에 맞춰 메시지를 발송하도록 선택할 수 있습니다.

### 5단계: 시간 범위 선택 {#step-5-select-time-frame}

사용자가 하루 중 특정 시간대에 Campaign을 수신할지 선택합니다. 메시지에 시간 범위를 지정했는데 사용자가 시간 범위 밖에서 트리거 이벤트를 완료하거나 메시지 지연으로 인해 시간 범위를 놓치면, 기본적으로 사용자는 메시지를 수신하지 않습니다.

![사용자가 하루 중 특정 시간대에 Campaign을 수신할지 선택합니다. 메시지에 시간 범위를 지정했는데 사용자가 시간 범위 밖에서 트리거 이벤트를 완료하거나 메시지 지연으로 인해 시간 범위를 놓치면, 기본적으로 사용자는 메시지를 수신하지 않습니다.]({% image_buster /assets/img_archive/schedule_triggered5.png %})

사용자가 시간 범위 내에서 트리거 이벤트를 완료했지만 메시지 지연으로 인해 시간 범위를 벗어나는 경우, 다음 체크박스를 선택하면 해당 사용자가 여전히 Campaign을 수신할 수 있습니다.

![5단계: 시간 범위 선택 관련 스크린샷.]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

사용자가 시간 범위를 놓쳐서 메시지를 수신하지 못한 경우에도, 사용자의 [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 선택하지 않았더라도 다음에 트리거 이벤트를 완료할 때 수신 자격이 유지됩니다. 사용자의 재자격을 선택한 경우, 사용자는 지정된 시간 범위 내에 자격을 충족할 때마다 트리거 이벤트를 완료할 때 Campaign을 수신할 수 있습니다.

Campaign에 특정 기간도 할당한 경우, 사용자는 메시지를 수신하려면 기간과 하루 중 특정 시간대 모두에서 자격을 충족해야 합니다.

### 6단계: 재자격 결정 {#step-6-determine-re-eligibility}

사용자가 Campaign에 대해 [재자격]({% image_buster /assets/img_archive/ReEligible.png %})을 얻을 수 있는지 결정합니다. 사용자의 재자격을 허용하는 경우, 사용자가 Campaign을 다시 수신하기 전 시간 지연을 지정할 수 있습니다. 이를 통해 트리거 Campaign이 스팸처럼 되는 것을 방지할 수 있습니다.

![6단계: 재자격 결정 관련 스크린샷.]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## 사용 사례 {#use-cases}

트리거 Campaign은 트랜잭션 또는 성과 기반 메시지에 매우 효과적입니다.

트랜잭션 Campaign에는 사용자가 구매를 완료하거나 장바구니에 상품을 추가한 후 발송되는 메시지가 포함됩니다. 후자의 경우는 예외 이벤트의 혜택을 받을 수 있는 Campaign의 좋은 예입니다. Campaign이 사용자에게 구매하지 않은 장바구니 내 상품을 알려준다고 가정해 보겠습니다. 이 경우 예외 이벤트는 사용자가 장바구니의 제품을 구매하는 것입니다. 성과 기반 Campaign의 경우, 사용자가 전환을 완료하거나 게임 레벨을 클리어한 후 5분 뒤에 메시지를 발송할 수 있습니다.

또한, 웰컴 캠페인을 만들 때 사용자가 등록하거나 계정을 설정한 후 메시지가 발송되도록 트리거할 수 있습니다. 등록 후 다른 날짜에 메시지를 순차적으로 발송하면 체계적인 온보딩 프로세스를 만들 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 사용자가 트리거 Campaign을 수신하지 못한 이유는? {#why-did-a-user-not-receive-my-triggered-campaign}

트리거 이벤트를 완료한 사용자가 Campaign을 수신하지 못하는 원인은 다음과 같습니다:

- 시간 지연이 완전히 경과하기 전에 사용자가 예외 이벤트를 완료했습니다.
- Liquid [`abort_message` 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)이 사용되었으며 `abort_message` 로직 또는 규칙에 따라 메시지가 중단되었습니다.
- 시간 지연으로 인해 기간이 종료된 후에 사용자가 Campaign 수신 자격을 얻게 되었습니다.
- 시간 지연으로 인해 하루 중 지정된 시간대 밖에서 사용자가 Campaign 수신 자격을 얻게 되었습니다.
- 사용자가 이미 Campaign을 수신했으며(공유 채널 식별자를 통한 기여도 포함—예: 이메일을 수신, 열기 또는 클릭한 다른 사람과 이메일을 공유하는 경우), 사용자가 재자격을 얻지 못합니다.
- 사용자가 Campaign에 대해 재자격이 있지만, 일정 기간이 지난 후에만 다시 트리거할 수 있으며 해당 기간이 아직 경과하지 않았습니다.

이벤트 발생 시점에 기록된 사용자 데이터를 기반으로 트리거 Campaign을 [세분화]({{site.baseurl}}/user_guide/audience/segments)하면 [경합 조건]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions)이 발생할 수 있습니다. 이는 Campaign이 세분화하는 사용자 속성이 변경되었지만 Campaign이 발송될 때 해당 변경이 사용자에게 아직 처리되지 않은 경우에 발생합니다. Campaign은 진입 시 Segment 멤버십을 확인하므로, 사용자가 Campaign을 수신하지 못하는 결과가 발생할 수 있습니다.

예를 들어, 방금 등록한 남성 사용자에게 이벤트 트리거 Campaign을 발송하려 한다고 가정해 보겠습니다. 사용자가 등록할 때 커스텀 이벤트 `registration`을 기록하고 동시에 사용자의 `gender` 속성을 설정합니다. Braze가 사용자의 성별을 처리하기 전에 이벤트가 Campaign을 트리거하여 사용자가 Campaign을 수신하지 못할 수 있습니다.

모범 사례로, Campaign이 세분화하는 속성이 이벤트 전에 Braze 서버로 플러시되도록 하세요. 이것이 불가능한 경우, 전달을 보장하는 가장 좋은 방법은 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties#custom-event-properties)를 사용하여 관련 사용자 속성정보를 이벤트에 첨부하고 세분화 필터 대신 특정 이벤트 속성정보에 대한 속성정보 필터를 적용하는 것입니다. 위 예시의 경우, 커스텀 이벤트 `registration`에 `gender` 속성정보를 추가하면 Campaign이 트리거될 때 Braze가 필요한 데이터를 확보할 수 있습니다.

또한, Campaign이 실행 기반이고 지연이 있는 경우, **발송 시 Segment 멤버십 재평가** 옵션을 선택하여 메시지가 발송될 때 사용자가 여전히 타겟 오디언스에 속하는지 확인할 수 있습니다.

#### 오디언스 기준 평가 {#audience-criteria-evaluation}

발송 전 지연이 포함된 Campaign(사용량 제한, 현지 시간대, Intelligent Timing 또는 트리거 스케줄 포함)의 경우, Segment가 재평가되는 시점은 Campaign 유형과 설정에 따라 달라집니다.

지연이 있는 실행 기반 Campaign에서 **발송 시 Segment 멤버십 재평가**를 선택하면, 메시지가 발송되기 전에 사용자가 재평가되므로 발송 시점에 Segment 기준을 여전히 충족하는 사용자만 메시지를 수신합니다.

Campaign이 특정 커스텀 이벤트에 의해 트리거되고 오디언스로 Segment를 선택한 경우, 사용자는 Segment에 포함되려면 동일한 커스텀 이벤트를 수행해야 합니다. 즉, 실행 기반 Campaign이 트리거되려면 사용자가 먼저 오디언스에 속해 있어야 합니다. 트리거 Campaign의 일반적인 워크플로는 다음과 같습니다:

1. **오디언스 참여:** 사용자가 커스텀 이벤트를 수행하면 Campaign의 타겟 오디언스에 추가됩니다.
2. **이메일 트리거:** 사용자가 이메일을 트리거하려면 커스텀 이벤트를 다시 수행해야 합니다. 이메일이 발송되려면 사용자가 먼저 오디언스에 속해 있어야 하기 때문입니다.

타겟 오디언스를 모든 사용자를 포함하도록 변경하거나, 이벤트를 수행할 것으로 예상되는 사용자가 이미 Campaign의 오디언스에 속해 있는지 확인하여 메시지가 트리거되도록 하는 것을 권장합니다.

![오디언스 기준 평가 관련 스크린샷.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### 커스텀 이벤트 문제 해결 {#troubleshooting-custom-events}

먼저 커스텀 이벤트가 Braze에 전달되고 있는지 확인합니다. **Analytics** > **커스텀 이벤트 보고서**로 이동한 다음 해당 커스텀 이벤트와 날짜 범위를 선택합니다. 이벤트가 표시되지 않으면 올바르게 설정되어 있는지, 사용자가 올바른 동작을 수행했는지 확인합니다.

커스텀 이벤트가 표시되는 경우, 다음을 수행하여 추가로 문제를 해결합니다:

- 사용자의 프로필 다운로드를 확인하여 이벤트를 트리거했는지와 트리거한 시점을 확인합니다. 이벤트가 트리거된 경우, 이벤트가 트리거된 타임스탬프와 Campaign이 시작된 시간을 비교합니다. 이벤트가 Campaign 시작 전에 트리거되었을 수 있습니다.
- Campaign 및 타겟팅에 사용된 Segment의 체인지로그를 검토하여 커스텀 이벤트가 트리거되었을 때 사용자가 Segment에 속해 있었는지 확인합니다. Segment에 속해 있지 않았다면 Campaign을 수신하지 못했을 것입니다.
- 세분화를 통해 사용자가 대조군에 배정되어 Campaign 수신이 차단되었는지 확인합니다.
- 스케줄된 지연이 있는 경우, 사용자의 커스텀 이벤트가 지연 전에 트리거되었는지 확인합니다. 이벤트가 지연 전에 트리거되었다면 Campaign을 수신하지 못했을 것입니다.

{% alert note %}
인앱 메시지는 REST API가 아닌 SDK를 통해 전송된 이벤트에 의해서만 트리거될 수 있습니다.
{% endalert %}

### 실행 기반 Campaign은 언제 오디언스 멤버십을 평가합니까? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze는 트리거 이벤트를 처리할 때 메시지가 발송되기 전에 오디언스 멤버십을 평가합니다. 기본적으로 Braze는 대기열에 추가되는 시점에 사용자가 타겟 오디언스와 일치하는지 확인합니다. Campaign에 지연이 있는 경우, **발송 시 Segment 멤버십 재평가**를 선택하여 발송 직전에 오디언스 기준을 다시 확인할 수 있습니다. 예를 들어, 사용자가 트리거 동작을 수행한 후 발송이 완료되기 전에 오디언스에서 이탈할 수 있는 경우에 유용합니다.

자세한 내용은 [오디언스 기준 평가](#audience-criteria-evaluation)를 참조하세요.