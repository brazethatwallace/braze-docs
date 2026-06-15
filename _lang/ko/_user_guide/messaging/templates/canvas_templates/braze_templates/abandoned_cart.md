---
nav_title: 유기한 의도
article_title: 유기한 의도
page_order: 1
page_type: reference
description: "이 문서에서는 Braze Canvas 템플릿을 사용하여 사용자와 실시간으로 소통하고 구매를 완료하도록 유도하는 방법을 설명합니다."
tool: Canvas
---

# 유기한 의도 {#abandoned-intent}

> 제품이 아직 기억에 남아 있을 때 사용자와 실시간으로 소통하여 구매를 완료하도록 유도하세요. 이 API 트리거 템플릿은 사용자가 장바구니를 유기하는 즉시 진입시키고, 최적의 채널(이메일, SMS 또는 인앱)로 시의적절한 리마인더를 보내며, 여정의 두 지점에서 구매 완료 여부를 확인하고, 전환하지 않은 사용자를 리타겟팅을 위해 광고 오디언스에 동기화합니다.

이 문서에서는 사용자 라이프사이클의 고려 단계를 위한 **Abandoned Intent** 템플릿의 사용 사례를 안내합니다. 이 문서를 마치면 장바구니에 상품을 추가한 후 구매를 완료하지 않은 사용자에게 구매를 유도하는 사용자 여정을 커스텀할 수 있습니다.

{% alert tip %}
[BrazeAI Operator<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/operator/)를 사용하여 이 템플릿을 설정하고 커스텀하세요. Canvas를 생성하거나 편집하는 동안 사용자 프로필 옆에 있는 **BrazeAI Operator<sup>TM</sup>**를 선택합니다. 그런 다음 "장바구니를 유기한 사용자를 다시 참여시키기 위해 Abandoned Intent 템플릿을 구성하는 것을 도와주세요"와 같이 목표를 설명합니다.
{% endalert %}

## 필수 조건 {#prerequisites}

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 이 Canvas에서 구매가 이루어지면 사용자가 Canvas를 종료하므로, 별도의 구매 후 사용자 여정 Canvas가 필요합니다.
- 사용하는 파트너 및 오디언스와 함께 [Braze 오디언스 동기화]({{site.baseurl}}/partners/canvas_audience_sync/)가 구성되어 있어야 합니다.

## 필요에 맞게 템플릿 조정하기 {#tailoring-the-template-to-your-needs}

주방용품 전문 소매 브랜드인 Kitchenerie에서 일하고 있으며, 최신 제품 "Enormous Paper Plate"를 장바구니에 추가했지만 구매를 완료하지 않은 사용자를 다시 참여시키는 것이 목표라고 가정해 보겠습니다.

Canvas를 만들기 전에 [Braze 오디언스 동기화 to Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) 통합을 설정하여 Braze의 사용자 데이터를 Facebook 오디언스에 추가하고 행동 트리거, 세분화 등을 기반으로 광고를 보낼 수 있도록 합니다.

**Abandoned Intent** 템플릿은 다음과 같은 흐름을 따릅니다: 구매 확인, 즉시 리마인더 발송, 대기, 최적 채널로 라우팅, 후속 메시지, 재확인, 비전환자 리타겟팅. 다음 단계가 포함됩니다:

| 캔버스 단계 | 템플릿 단계 이름 | 목적 |
|---|---|---|
| 행동 경로 | Made purchase? | 첫 번째 완료 확인으로, 이미 구매한 사용자는 Canvas를 종료합니다. |
| 메시지 | Itemized Reminder | 진입 직후 발송되는 즉시 장바구니 리마인더입니다. |
| 지연 | Delay | 제품이 아직 기억에 남아 있을 때 후속 메시지가 도착하도록 30분 대기합니다. |
| 오디언스 경로 | Intelligent Channel split | [인텔리전트 채널]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/) 순위에 따라 사용자를 이메일 또는 SMS로 라우팅합니다. |
| 메시지 | Abandoned Cart Email, Abandoned Cart SMS, Abandoned Cart In-App Message | 채널별 후속 메시지입니다. 인텔리전트 채널이 이메일과 SMS 중 선택하며, 인앱 메시지는 템플릿에서 별도의 경로로 발송됩니다. |
| 행동 경로 | Made purchase? (2) | 리타겟팅 전 두 번째 완료 확인입니다. |
| 오디언스 동기화 | Ad Retargeting | 비전환자를 광고 오디언스(예: Facebook)에 동기화하여 오프채널 리타겟팅을 수행합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Abandoned Intent 템플릿 단계" }

### 1단계: 세부 정보 설정하기 {#step-1-set-up-the-details}

Canvas 템플릿을 적용하고 목표에 맞게 세부 정보를 업데이트해 보겠습니다.

1. **메시징** > **Canvas**로 이동합니다.
2. **Canvas 생성** > **Canvas 템플릿 사용**을 선택합니다.
3. **Braze 템플릿** 탭을 선택한 다음 **Abandoned Intent** 옆에 있는 **템플릿 적용**을 선택합니다.
4. 설명을 업데이트하여 최신 시즌 주방용품 출시에서 사용자가 구매를 완료하도록 유도하기 위한 Canvas임을 명시합니다.
5. **Intent** 태그를 추가하여 Canvas 홈 페이지에서 필터링할 수 있도록 합니다.

![Canvas의 새 이름, 설명 및 태그.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### 2단계: 전환 이벤트 할당하기 {#step-2-assign-your-conversion-events}

템플릿은 **주요 전환 이벤트 - A**를 **Makes Purchase (Legacy)**로 설정하며, 기본적으로 **Make any purchase (Legacy)**가 선택되어 있습니다. "Enormous Paper Plate" 제품에 초점을 맞추고 있으므로 전환 이벤트를 다음과 같이 커스텀합니다:

1. **Make a specific purchase (Legacy)**를 선택합니다.
2. **Product name**에 **Enormous Paper Plate**를 입력합니다.

![전환 유형이 "Makes Purchase"이고 제품 이름이 "Enormous Paper Plate"인 주요 전환 이벤트 - A. 3일의 전환 기한이 있습니다.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

{% alert note %}
워크스페이스에서 **Places order** 전환 이벤트를 사용하는 경우, 구매 관련 옵션이 레이블에 **(Legacy)**로 표시될 수 있습니다. 이 문서의 단계에서는 레거시 구매 전환 흐름을 사용합니다.
{% endalert %}

### 3단계: 진입 스케줄 설정하기 {#step-3-set-an-entry-schedule}

**Abandoned Intent** 템플릿은 **API 트리거** 진입 스케줄을 사용하므로 사용자가 장바구니를 유기하는 즉시 Canvas에 진입시킬 수 있습니다. 제품이 아직 기억에 남아 있을 때 대응하고자 하므로 이 사용 사례에 적합합니다.

1. 진입 스케줄 유형을 **API 트리거**로 유지합니다.
2. Canvas ID를 확인하고 [`/canvas/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)를 사용하여 앱이나 웹사이트에서 유기한 장바구니를 감지했을 때 사용자를 추가합니다.
3. 선택적으로 [컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)(예: 제품 이름 또는 장바구니 세부 정보)를 전달하여 후속 메시지를 개인화할 수 있습니다.

동작 기반 진입을 선호하는 경우 **동작 기반**을 선택하고 브랜드에서 유기한 장바구니를 추적하는 방식에 맞는 트리거를 선택합니다. 예를 들어 기록된 `abandoned_cart` 이벤트에 대해 **커스텀 이벤트 수행**을 선택할 수 있습니다.

### 4단계: Canvas에 진입할 사용자 결정하기 {#step-4-determine-who-enters-the-canvas}

다음으로 타겟 오디언스를 지난 90일 동안 온라인에서만 쇼핑한 사용자로 정의해 보겠습니다. 이렇게 하면 제품에 참여하고 있는 사용자로 오디언스를 좁힐 수 있습니다.

![이 Canvas에서 타겟팅할 사용자 Segment로 "Online Shoppers Segment - 90 Days".]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

진입 제어는 그대로 두어 사용자가 이 Canvas에 재진입할 수 없도록 하고, 잠재적으로 이 Canvas에 진입할 수 있는 인원 수에 제한을 두지 않습니다.

템플릿은 기본적으로 글로벌 종료 기준을 설정하지 않습니다. 대신 사용자는 **Made purchase?** 행동 경로 단계에서 구매를 완료하면 종료되며, 이는 6단계에서 커스텀합니다.

### 5단계: 발송 설정 선택하기 {#step-5-select-your-send-settings}

기본 구독 설정을 유지하여 메시지나 알림 수신에 가입했거나 옵트인한 사용자에게만 발송하고, 나머지 설정은 그대로 둡니다.

### 6단계: Canvas 커스텀하기 {#step-6-customize-your-canvas}

사용자가 경험하는 순서대로 캔버스 단계를 커스텀합니다:

#### 진입 시 구매 확인 {#check-for-purchase-at-entry}

1. **Made purchase?** 행동 경로 단계를 선택한 다음 **Made purchase** 동작 그룹을 선택합니다.
2. **Make Purchase**에서 **Make a specific purchase (Legacy)**를 선택하고 제품으로 **Enormous Paper Plate**를 선택합니다. 이 제품을 구매한 사용자는 Canvas를 종료합니다.

#### 즉시 리마인더 발송 {#send-the-immediate-reminder}

1. **Itemized Reminder** 메시지 단계를 선택한 다음 **메시지 편집**을 선택하여 첫 번째 리마인더 이메일을 커스텀합니다. 이 메시지는 지연 전, 진입 직후에 발송됩니다.
2. **Delay** 단계는 그대로 둡니다. 템플릿은 후속 메시지 발송 전 30분 지연을 사용하여 제품이 아직 기억에 남아 있을 때 사용자가 결제를 완료할 시간을 줍니다.

{% alert tip %}
[Canvas 컨텍스트 등록정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)를 사용하여 참조하는 제품에 따라 Canvas의 메시지를 커스텀할 수 있습니다.
{% endalert %}

#### 최적 채널로 라우팅 {#route-to-the-optimal-channel}

1. **Intelligent Channel split** 오디언스 경로 단계를 검토합니다. 이 단계는 [인텔리전트 채널]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/) 순위에 따라 사용자를 **Abandoned Cart Email** 또는 **Abandoned Cart SMS**로 라우팅합니다. 필요에 따라 경로를 조정합니다.
2. **Abandoned Cart Email**, **Abandoned Cart SMS**, **Abandoned Cart In-App Message** 단계를 커스텀합니다. 각 단계에서 **메시지 편집**을 선택하여 해당 채널의 문구와 메시지를 업데이트합니다. 인앱 메시지는 인텔리전트 채널 분할과 별도의 경로에서 실행되며 인텔리전트 채널 순위에 의해 선택되지 않습니다.

#### 비전환자 리타겟팅 {#retarget-non-converters}

1. **Made purchase? (2)** 행동 경로 단계를 선택한 다음 **Made purchase** 동작 그룹을 선택합니다.
2. **Make a specific purchase (Legacy)**를 선택하고 제품으로 **Enormous Paper Plate**를 선택합니다. 여기서 구매한 사용자는 리타겟팅에 도달하기 전에 Canvas를 종료합니다.
3. **Ad Retargeting** 오디언스 동기화 단계를 선택하고 Facebook에 동기화하도록 구성합니다. 이 단계에 도달한 사용자는 구매하지 않은 사용자이므로 오프채널 리타겟팅을 위해 광고 오디언스에 동기화합니다.

### 7단계: Canvas 테스트 및 시작하기 {#step-7-test-and-launch-the-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **Canvas 시작**을 선택하여 Canvas를 시작합니다. 이제 장바구니에 추가한 제품의 결제를 유도하는 개인화된 사용자 여정으로 사용자를 세심하게 타겟팅할 수 있습니다!

{% alert tip %}
Canvas를 시작하기 전후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)를 확인하세요.
{% endalert %}