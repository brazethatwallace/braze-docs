---
nav_title: 메시지
article_title: 메시지
alias: "/message_step/"
page_order: 11
page_type: reference
description: "이 참조 문서에서는 메시지 단계를 사용하여 독립형 메시지를 만드는 방법을 다룹니다."
tool: Canvas

---

# 메시지 {#message}

> 메시지 단계를 사용하면 Canvas에서 원하는 위치에 독립형 메시지를 추가할 수 있습니다.

![푸시 채널을 사용하는 "Lunch promo"라는 이름의 메시지 단계.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## 메시지 만들기 {#create-a-message}

메시지 구성요소를 만들려면 먼저 Canvas에 단계를 추가합니다. 사이드바에서 구성요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택한 다음 **메시지**를 선택합니다.

### 1단계: 메시징 채널 선택 {#step-1-select-your-messaging-channel}

다음 메시징 채널 중에서 선택할 수 있습니다:
- 배너
- Content Cards
- 이메일
- LINE
- 푸시 알림
- SMS/MMS/RCS
- 인앱 메시지
- 웹훅
- WhatsApp

![메시지 단계에서 선택할 수 있는 메시징 채널 목록.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### 2단계: 전달 설정 편집 {#step-2-edit-delivery-settings}

다음으로 Intelligent Timing, 방해금지 시간 재정의, 전달 유효성 검사에 대한 설정을 편집할 수 있습니다.

#### Intelligent Timing {#intelligent-timing}

사용자 프로필에 최적의 시간을 계산할 데이터가 충분하지 않을 때 대체 옵션과 함께 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)을 활성화할 수 있습니다. 사용자가 메시지 단계에 진입하는 시점과 실제 메시지 발송 사이의 지연에 대한 추가 확인으로 Intelligent Timing과 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#rate-limiting-and-frequency-capping)을 활성화하는 것을 권장합니다.

**전달 설정** 탭에서 **Intelligent Timing 사용**을 선택합니다. 여기에서 가장 인기 있는 시간 또는 특정 대체 시간을 선택할 수 있습니다. 방해금지 시간이 활성화된 경우, 메시지 단계에서 이 설정을 재정의할 수도 있습니다.

![메시지 구성요소 설정의 전달 설정 탭. 방해금지 시간이 활성화되어 있으며, Intelligent Timing 사용 체크박스가 선택되어 최적의 시간에 메시지를 전달합니다.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

#### 전달 유효성 검사 {#delivery-validations}

전달 유효성 검사는 메시지 발송 시 오디언스가 전달 기준을 충족하는지 확인하는 추가 검사를 제공합니다. 이 설정은 방해금지 시간, Intelligent Timing 또는 사용량 제한이 활성화된 경우 사용하는 것을 권장합니다. **메시지 발송 시 오디언스 유효성 검사**를 선택한 다음, Segment 또는 추가 필터를 추가합니다. 사용자가 유효성 검사를 충족하지 않는 경우, Canvas에서 나갈지 또는 다음 단계로 진행할지 선택합니다.

전달 유효성 검사는 발송 시점에 사용자 프로필 기준을 평가합니다. 앱 관련 필터는 사용자가 최근에 특정 앱을 사용했는지 또는 사용한 적이 있는지를 확인하지만, 현재 세션에서 사용자가 어떤 앱을 사용하고 있는지는 확인하지 않습니다.

워크스페이스에 여러 앱이 있고 메시지 단계가 특정 앱을 타겟팅해야 하는 경우, 다음 방법 중 하나를 대신 사용하세요:

- 메시지를 작성할 때 **모바일 앱** 또는 **웹 브라우저**와 같은 [전달 플랫폼을 지정]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#step-2-specify-delivery-platforms)합니다.
- Liquid를 사용하여 발송 시점에 타겟팅된 기기 또는 앱을 확인합니다:
  - {% raw %}`{{targeted_device.${platform}}}`{% endraw %}는 사용자의 현재 세션에 대한 플랫폼을 평가합니다. 자세한 내용은 [타겟팅된 기기 정보]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information)를 참조하세요.
  - {% raw %}`{{app.${api_id}}}`{% endraw %}는 메시지를 요청하는 앱을 평가합니다. 이 태그를 `abort_message()`와 결합하여 잘못된 앱으로의 발송을 방지할 수 있습니다. 자세한 내용은 [타겟팅된 앱 정보]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-app-information)를 참조하세요.

![메시지 발송 시 오디언스 유효성 검사가 활성화된 전달 유효성 검사. 전달 유효성 검사 진행 동작은 전달 유효성 검사가 충족되지 않을 경우 사용자를 Canvas의 다음 단계로 진행하도록 설정되어 있습니다.]({% image_buster /assets/img/canvas_components/message_step5.png %}){: style="max-width:90%;"}

## 사용자 진행 방식 {#how-users-advance}

메시지 단계에 진입한 모든 사용자는 다음 조건 중 하나가 충족되면 다음 단계로 진행합니다:

- 메시지가 발송됨
- 메시지가 빈도 제한에 걸려 발송되지 않음
- 메시지가 중단됨
- 사용자가 채널로 도달할 수 없어 메시지가 발송되지 않음
- 사용자가 **전달 유효성 검사**의 기준을 충족하지 않음

{% raw %}
실행 기반 Canvas가 인바운드 SMS 메시지에 의해 트리거되는 경우, 첫 번째 단계(메시지 단계) 또는 행동 경로 단계 아래에 중첩된 메시지 단계에서 SMS 등록정보를 참조할 수 있습니다. 예를 들어, 메시지 단계에서 `{{sms.${inbound_message_body}}}` 또는 `{{sms.${inbound_media_urls}}}`를 사용할 수 있습니다.
{% endraw %}

## 컨텍스트 등록정보 참조 {#reference-context-properties}

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

진입 등록정보는 Canvas 생성의 **진입 스케줄** 단계에서 구성되며, 사용자를 Canvas에 진입시키는 트리거를 나타냅니다. 이러한 등록정보는 API 트리거 Canvases에서 진입 페이로드의 등록정보에도 접근할 수 있습니다. `context` 오브젝트의 최대 크기 제한은 50 KB입니다.

진입 등록정보는 모든 메시지 단계에서 Liquid로 사용할 수 있습니다. 이러한 진입 등록정보를 참조할 때 다음 Liquid를 사용합니다: {% raw %}``{context.${property_name}}``{% endraw %}. 이벤트는 이 방식으로 사용하려면 커스텀 이벤트 또는 구매 이벤트여야 합니다.

{% alert note %}
인앱 메시지 채널의 경우, `context`는 Canvas에서만 참조할 수 있습니다.
{% endalert %}

이러한 진입 등록정보를 참조할 때 다음 Liquid를 사용합니다: {% raw %}``context.${property_name}``{% endraw %}. 이벤트는 이 방식으로 사용하려면 커스텀 이벤트 또는 구매 이벤트여야 합니다.

{% raw %}
예를 들어, 다음 요청을 생각해 보겠습니다: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Liquid `{{context.${product_name}}}`를 사용하여 메시지에 "shoes"라는 단어를 추가할 수 있습니다.
{% endraw %}

또한 Canvas 워크플로 전체에서 개인화된 단계를 통해 사용자를 안내하기 위해 모든 메시지 단계에서 [영구 진입 등록정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)를 활용할 수 있습니다.

### 이벤트 등록정보 {#event-properties}

이벤트 등록정보는 커스텀 이벤트 및 구매 이벤트에 대해 설정한 등록정보를 말합니다. 이러한 이벤트 등록정보는 실행 기반 전달이 있는 Campaigns과 Canvases에서 사용할 수 있습니다.

Canvas에서 커스텀 이벤트 및 구매 이벤트 등록정보는 [행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) 단계 다음에 오는 모든 메시지 단계에서 Liquid로 사용할 수 있습니다. 예를 들어, `event_properties`를 참조할 때 다음 Liquid 스니펫을 사용합니다: {% raw %}``{{event_properties.${property_name}}}``{% endraw %}

{% alert important %}
`event_properties`는 행동 경로 단계 없이 독립적으로 사용할 수 없습니다.
{% endalert %}

행동 경로 다음의 첫 번째 메시지 단계에서 해당 행동 경로에서 참조된 이벤트와 관련된 `event_properties`를 사용할 수 있습니다. 이 행동 경로 단계와 메시지 단계 사이에 다른 단계(다른 행동 경로 또는 메시지 단계가 아닌)가 있을 수 있습니다. 메시지 단계가 행동 경로 단계의 다른 모든 사용자 경로가 아닌 경로로 추적될 수 있는 경우에만 `event_properties`에 접근할 수 있습니다.

{% alert important %}
리드 메시지 단계에서는 `event_properties`를 사용할 수 없습니다. 대신 `context`를 사용하거나, `event_properties`를 포함하는 메시지 단계 앞에 해당 이벤트가 있는 행동 경로 단계를 추가해야 합니다.
{% endalert %}

{% details 원본 Canvas 편집기에 대해 펼치기 %}

원본 편집기를 사용하여 Canvases를 더 이상 만들거나 복제할 수 없습니다. 이 섹션은 참조용으로만 제공됩니다.

- `event_properties`는 예약된 전체 단계에서 사용할 수 없습니다. 그러나 실행 기반 Canvas의 첫 번째 전체 단계에서는 전체 단계가 예약된 경우에도 `event_properties`를 사용할 수 있습니다.
- `context`는 Canvas의 첫 번째 전체 단계에서만 참조할 수 있습니다.
- 인앱 메시지 채널의 경우, 이전 얼리 액세스의 일부로 영구 진입 등록정보가 활성화된 경우 원본 Canvas 편집기에서 `context`를 참조할 수 있습니다.

{% enddetails %}

## 분석 {#analytics}

메시지 구성요소 측정기준의 정의는 다음 표를 참조하세요:

| 측정기준 | 설명 |
| --- | --- |
| _진입_ | 단계에 진입한 횟수입니다. Canvas에 재자격이 있고 사용자가 메시지 단계에 두 번 진입하면 두 번의 진입이 기록됩니다. |
| _다음 단계로 진행_ | Canvas의 다음 단계로 진행한 진입 수입니다. |
| _발송_ | 단계에서 발송한 총 메시지 수입니다. Canvas 재자격이 있고 사용자가 메시지 단계에 두 번 진입하면 두 번의 진입이 기록됩니다. |
| _고유 수신자_ | 이 단계에서 메시지를 수신한 사용자 수입니다. |
| _주요 전환 이벤트_ | Braze Campaign에서 수신한 메시지를 보거나 상호작용한 후 정의된 이벤트가 발생한 횟수입니다. 이 이벤트는 Campaign을 구축할 때 정의합니다. |
| _매출_ | 설정된 주요 전환 기간 내 Campaign 수신자로부터 발생한 총 매출(달러)입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석" }