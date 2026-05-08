---
nav_title: 유기한 장바구니
article_title: 유기한 장바구니
page_order: 1
page_type: reference
description: "이 문서에서는 Braze Canvas 템플릿을 사용하여 사용자와 실시간으로 소통하고 구매를 완료하도록 유도하는 방법을 설명합니다."
tool: Canvas
---

# 유기한 장바구니 {#abandoned-cart}

> 사용자와 실시간으로 소통하여 구매를 완료하도록 유도하세요. 이 템플릿을 사용하면 유기한 장바구니를 상기시키는 시의적절하고 개인화된 메시지를 보내는 데 초점을 맞춘 사용자 여정을 만들 수 있습니다. 제품의 장점을 강조하고 할인 코드와 같은 인센티브를 제공할 수 있습니다.

이 문서에서는 사용자 라이프사이클의 고려 단계를 위한 **Abandoned Intent** 템플릿의 사용 사례를 안내합니다. 이 문서를 마치면 장바구니에 상품을 추가한 후 구매를 완료하지 않은 사용자에게 구매를 유도하는 사용자 여정을 커스텀할 수 있습니다.

## 필수 조건 {#prerequisites}

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 이 Canvas에서 구매가 이루어지면 사용자가 Canvas를 종료하므로, 별도의 구매 후 사용자 여정 Canvas가 필요합니다.
- 사용하는 파트너 및 오디언스와 함께 [Braze 오디언스 동기화]({{site.baseurl}}/partners/canvas_audience_sync/)가 구성되어 있어야 합니다.

## 필요에 맞게 템플릿 조정하기 {#tailoring-the-template-to-your-needs}

주방용품 전문 소매 브랜드인 Kitchenerie에서 일하고 있으며, 최신 제품 "Enormous Paper Plate"를 장바구니에 추가했지만 구매를 완료하지 않은 사용자를 다시 참여시키는 것이 목표라고 가정해 보겠습니다.

Canvas를 만들기 전에 [Braze 오디언스 동기화 to Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) 통합을 설정하여 Braze의 사용자 데이터를 Facebook 오디언스에 추가하고 행동 트리거, 세분화 등을 기반으로 광고를 보낼 수 있도록 합니다.

Abandoned Intent 템플릿에 접근하려면 새 Canvas를 만들 때 **Use a Canvas template** > **Braze templates**를 선택합니다. 그런 다음 **Abandoned Intent** 옆에 있는 **Apply Template**을 선택합니다. 이제 템플릿을 필요에 맞게 조정할 수 있습니다.

### 1단계: 세부 정보 설정하기 {#step-1-set-up-the-details}

Canvas 세부 정보를 목표에 맞게 조정해 보겠습니다.

1. 템플릿 이름 옆의 **Edit**를 선택합니다.

![Canvas의 현재 제목과 설명.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Canvas 이름을 업데이트하여 유기한 장바구니가 있는 사용자를 타겟팅하기 위한 Canvas임을 명시합니다.
3. 설명을 업데이트하여 최신 시즌 주방용품 출시에서 사용자가 구매를 완료하도록 유도하기 위한 Canvas임을 명시합니다.
4. **Abandon Cart** 태그를 추가하여 Canvas 홈 페이지에서 필터링할 수 있도록 합니다.

![Canvas의 새 이름, 설명 및 태그.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### 2단계: 전환 이벤트 할당하기 {#step-2-assign-your-conversion-events}

다음으로 전환 이벤트를 할당해 보겠습니다. "Enormous Paper Plate" 제품에 초점을 맞추고 있으므로 **주요 전환 이벤트 A**에 대해 다음을 수행합니다:

1. **전환 이벤트 유형**에서 **Makes Purchase**를 선택합니다.
2. **Make a specific purchase**를 선택합니다. 이렇게 하면 특정 제품 이름을 선택할 수 있습니다.
3. **Enormous Paper Plate**를 선택합니다.

![전환 유형이 "Makes Purchase"이고 제품 이름이 "Enormous Paper Plate"인 주요 전환 이벤트 - A. 3일의 전환 기한이 있습니다.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### 3단계: 진입 스케줄 설정하기 {#step-3-set-an-entry-schedule}

이 템플릿의 진입 스케줄은 **API-Triggered**로 설정되어 있지만, 장바구니를 유기한 사용자(이것은 동작입니다)에 초점을 맞추고 싶으므로 이 Canvas에는 동작 기반 진입이 더 적합합니다.

1. 진입 스케줄 유형으로 **Action-Based**를 선택합니다.
2. 트리거로 **Abandoned Cart**를 선택합니다.
3. 진입 기간에서 시작 시간 날짜를 선택합니다.
4. 사용자가 현지 시간대에 진입할 수 있도록 하는 옵션을 선택합니다. 이렇게 하면 메시지의 관련성을 유지하고 최적의 시간에 메시지를 보내 더 높은 참여를 이끌어낼 수 있습니다.

![유기한 장바구니가 있는 사용자를 타겟팅하는 동작 기반 Canvas. 진입 기간은 2024년 10월 15일 오후 3:20이며 사용자의 현지 시간대 기준입니다.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### 4단계: Canvas에 진입할 사용자 결정하기 {#step-4-determine-who-enters-the-canvas}

다음으로 타겟 오디언스를 지난 90일 동안 온라인에서만 쇼핑한 사용자로 정의해 보겠습니다. 이렇게 하면 제품에 참여하고 있는 사용자로 오디언스를 좁힐 수 있습니다.

![이 Canvas에서 타겟팅할 사용자 Segment로 "Online Shoppers Segment - 90 Days".]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

진입 제어는 그대로 두어 사용자가 이 Canvas에 재진입할 수 없도록 하고, 잠재적으로 이 Canvas에 진입할 수 있는 인원 수에 제한을 두지 않습니다.

종료 기준의 경우, "Enormous Paper Plate"를 구매한 사용자는 Canvas를 종료합니다. 이렇게 하면 이미 구매한 상품에 대한 추가 메시지를 받지 않게 됩니다.

![Enormous Paper Plate를 특정 구매한 사용자가 Canvas를 종료하도록 결정하는 종료 기준.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### 5단계: 발송 설정 선택하기 {#step-5-select-your-send-settings}

기본 구독 설정을 유지하여 메시지나 알림 수신에 가입했거나 옵트인한 사용자에게만 발송하고, 나머지 설정은 그대로 둡니다.

### 6단계: Canvas 커스텀하기 {#step-6-customize-your-canvas}

이제 템플릿 단계를 커스텀하여 Canvas를 구축해 보겠습니다:

1. 행동 경로 단계를 선택한 다음 **Made purchase** 동작 그룹 이름을 선택합니다.
2. **Make Purchase**에서 **Make A Specific Purchase**를 선택하고 제품으로 **Enormous Paper Plate**를 선택합니다. 종료 기준과 마찬가지로 이 제품을 구매한 사용자는 Canvas를 종료합니다.

![사용자가 Enormous Paper Plate를 구매하면 Canvas를 종료하는 "Made purchase" 동작 그룹.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3. 메시지 단계에서 **Edit message**를 선택하여 유기한 장바구니의 상품을 알리는 이메일을 커스텀합니다.
4. 지연 단계는 그대로 둡니다.
5. 오디언스 경로 단계 이후의 메시지 단계에서 사용자가 받을 이메일과 SMS 메시지를 커스텀합니다. 여기서 개인화된 메시지로 사용자에게 제품 구매를 유도합니다.

![사용자가 받을 SMS 메시지 미리보기: "안녕하세요, 장바구니에 Enormous Paper Plate가 남아 있어요! 지금 구매를 완료하고 호스팅 실력을 한 단계 업그레이드하세요. 결제 시 코드 MYPLATE를 사용하면 주문 금액의 20% 할인을 받을 수 있습니다!"]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6. 다음 행동 경로 단계에서 **Made purchase** 동작 그룹을 선택합니다. 그런 다음 **Make a specific purchase**를 선택하고 제품으로 **Enormous Paper Plate**를 선택합니다. 이 단계는 첫 번째 행동 경로 단계를 미러링하여 제품을 구매한 사용자를 종료시켜 추가 메시지를 받지 않도록 합니다.
7. 오디언스 동기화 단계가 Facebook에 동기화되도록 설정되어 있는지 확인합니다. 이렇게 하면 광고 리타겟팅에 더 도움이 됩니다.

{% alert tip %}
[Canvas 진입 등록정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)를 사용하여 참조하는 제품에 따라 Canvas의 메시지를 커스텀할 수 있습니다.
{% endalert %}

### 7단계: Canvas 테스트 및 시작하기 {#step-7-test-and-launch-the-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **Launch Canvas**를 선택하여 Canvas를 시작합니다. 이제 장바구니에 추가한 제품의 결제를 유도하는 개인화된 사용자 여정으로 사용자를 세심하게 타겟팅할 수 있습니다!

{% alert tip %}
Canvas를 시작하기 전후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)를 확인하세요.
{% endalert %}