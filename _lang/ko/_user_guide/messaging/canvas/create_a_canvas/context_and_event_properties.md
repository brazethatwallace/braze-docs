---
nav_title: 컨텍스트 및 이벤트 속성정보
article_title: 컨텍스트 및 이벤트 속성정보
page_order: 4.2
page_type: reference
description: "이 참조 문서에서는 컨텍스트와 이벤트 속성정보의 차이점과 각 속성정보를 사용해야 하는 시점에 대해 설명합니다."
tool: Canvas
---

# 컨텍스트 및 이벤트 속성정보 {#context-and-event-properties}

> 이 참조 문서에서는 `context`와 `event_properties`에 대한 정보를 다루며, 각 속성정보를 사용해야 하는 시점과 동작의 차이점을 설명합니다. <br><br> 커스텀 이벤트 속성정보에 대한 일반적인 정보는 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)를 확인하세요.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

컨텍스트 속성정보와 이벤트 속성정보는 Canvas 워크플로 내에서 서로 다르게 작동합니다. 사용자의 Canvas 진입을 트리거하는 이벤트 또는 API 호출의 속성정보를 `context`라고 합니다. 사용자가 Canvas 여정 내에서 이동할 때 발생하는 이벤트의 속성정보를 `event_properties`라고 합니다. 핵심 차이점은 `context`가 단순히 이벤트뿐만 아니라 API 트리거 Canvases의 진입 페이로드 속성정보에도 접근할 수 있다는 것입니다.

컨텍스트와 이벤트 속성정보의 차이점 요약은 다음 표를 참조하세요.

| | 컨텍스트 속성정보 | 이벤트 속성정보 |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **지속성** | Canvas를 사용하여 구축된 Canvas 기간 동안 모든 [메시지]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) 단계에서 참조할 수 있습니다. | - 한 번만 참조할 수 있습니다. <br> - 이후 메시지 단계에서는 참조할 수 없습니다. |
| **Canvas 동작** | Canvas의 모든 단계에서 `context`를 참조할 수 있습니다. 시작 후 동작에 대해서는 [시작 후 Canvas 편집]({{site.baseurl}}/post-launch_edits#canvas-entry-properties)을 참조하세요. | - [행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) 단계 **이후** 첫 번째 메시지 단계에서 `event_properties`를 참조할 수 있으며, 수행된 동작이 커스텀 이벤트 또는 구매 이벤트인 경우에 해당합니다. <br> - 행동 경로 단계의 다른 모든 사용자 경로 이후에는 사용할 수 없습니다. <br> - 행동 경로와 메시지 단계 사이에 다른 비메시지 구성요소가 있을 수 있습니다. 이러한 비메시지 구성요소 중 하나가 행동 경로 단계인 경우, 사용자는 해당 행동 경로의 다른 모든 사용자 경로를 통과할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="컨텍스트 및 이벤트 속성정보" }

{% details 기존 Canvas 편집기 세부 정보 %}

더 이상 기존 편집기를 사용하여 Canvas를 생성하거나 복제할 수 없습니다. Canvas 컨텍스트는 기존 Canvas 편집기에서 지원되지 않으므로, 이 섹션은 이전 Canvas 워크플로에서 Canvas 진입 속성정보와 이벤트 속성정보를 사용할 때 참조용으로 제공됩니다.

**Canvas 진입 속성정보:**
- 영구 진입 속성정보가 활성화되어 있어야 합니다.
- Canvas의 첫 번째 전체 단계에서만 `canvas_entry_properties`를 참조할 수 있습니다. Canvas는 실행 기반 또는 API 트리거 방식이어야 합니다.

**진입 속성정보:**
- Canvas에서 실행 기반 전달을 사용하는 모든 전체 단계에서 `event_properties`를 참조할 수 있습니다.
- 실행 기반 Canvas의 첫 번째 전체 단계를 제외한 스케줄된 전체 단계에서는 사용할 수 없습니다. 그러나 사용자가 [Canvas 구성요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)를 사용하는 경우, 동작은 `event_properties`에 대한 현재 Canvas 워크플로 규칙을 따릅니다.

**이벤트 속성정보:**
- 첫 번째 메시지 단계에서는 `event_properties`를 사용할 수 없습니다. 대신 `canvas_entry_properties`를 사용하거나 `event_properties`를 포함하는 메시지 단계 **이전에** 해당 이벤트가 포함된 행동 경로 단계를 추가해야 합니다.

{% enddetails %}

## 알아두어야 할 사항 {#things-to-know}

- 컨텍스트는 Liquid에서 참조할 때만 사용할 수 있습니다. Canvas 내에서 속성정보를 기준으로 필터링하려면 [이벤트 속성정보 세분화]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)를 대신 사용하세요.
- 인앱 메시지 채널의 경우, Canvas에서 `context`와 `event_properties`를 참조할 수 있습니다. `event_properties`는 트리거 기반이므로 첫 번째 캔버스 단계에 포함된 경우 접근할 수 있습니다.
- 첫 번째 메시지 단계에서는 `event_properties`를 사용할 수 없습니다. 대신 `context`를 사용하거나 `event_properties`를 포함하는 메시지 단계 **이전에** 해당 이벤트가 포함된 행동 경로 단계를 추가할 수 있습니다.
- 행동 경로 단계에 "SMS 인바운드 메시지 전송" 또는 "WhatsApp 인바운드 메시지 전송" 트리거가 포함된 경우, 후속 캔버스 단계에 SMS 또는 WhatsApp Liquid 속성정보를 포함할 수 있습니다. 이는 Canvases에서 이벤트 속성정보가 작동하는 방식과 동일합니다. 이를 통해 메시지를 활용하여 고객 프로필에 퍼스트파티 데이터를 저장하고 참조하며 대화형 메시징을 구현할 수 있습니다.

{% alert note %}
오디언스 자격은 Canvas 진입 시 한 번 평가됩니다. 진입 중에 사용자가 병합되면, 식별된 사용자는 Canvas를 계속 진행하며 Canvas Segment 기준에 대해 재평가되지 않습니다.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### 트리거의 타임스탬프 {#timestamps-for-triggers}

실행 기반 Canvases를 트리거하는 이벤트에서 [datetime 유형]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)의 타임스탬프를 사용하고 [컨텍스트]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)를 통해 참조하는 경우, 타임스탬프는 UTC로 정규화됩니다.

이러한 동작을 고려하여, Braze는 메시지가 [선호하는 시간대]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#time-zone-filter)로 전송되도록 다음 예시와 같은 Liquid 시간대 필터를 사용할 것을 강력히 권장합니다.

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

## 사용 사례 {#use-case}

![위시리스트에 아이템을 추가한 사용자를 위한 행동 경로 단계, 지연 단계, 메시지 단계와 다른 모든 사용자를 위한 경로.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

`context`와 `event_properties`의 차이점을 더 잘 이해하기 위해, 사용자가 "위시리스트에 아이템 추가" 커스텀 이벤트를 수행할 때 실행 기반 Canvas에 진입하는 시나리오를 살펴보겠습니다.

컨텍스트는 Canvas 생성의 [진입 스케줄]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) 단계에서 구성되며, 사용자가 Canvas에 진입하는 시점에 해당합니다. 컨텍스트는 모든 메시지 단계에서도 참조할 수 있습니다.

이 Canvas에는 사용자가 위시리스트에 아이템을 추가했는지 여부를 판단하는 행동 경로 단계로 시작하는 사용자 여정이 있습니다. 여기서 사용자가 아이템을 추가한 경우, 지연을 거친 후 메시지 단계에서 "위시리스트에 새 아이템이 추가되었습니다!"라는 메시지를 받게 됩니다.

사용자 여정의 첫 번째 메시지 단계는 행동 경로 단계의 커스텀 `event_properties`에 접근할 수 있습니다. 이 경우, 메시지 콘텐츠의 일부로 이 메시지 단계에 ``{% raw %} {{event_properties.${property_name}}} {% endraw %}``를 포함할 수 있습니다. 사용자가 위시리스트에 아이템을 추가하지 않은 경우, 다른 모든 사용자 경로를 통과하게 되며, 이는 `event_properties`를 참조할 수 없고 잘못된 설정 오류가 표시됨을 의미합니다.

메시지 단계가 행동 경로 단계의 다른 모든 사용자가 아닌 경로로 추적될 수 있는 경우에만 `event_properties`에 접근할 수 있습니다. 메시지 단계가 다른 모든 사용자 경로에 연결되어 있지만 사용자 여정에서 행동 경로 단계로 추적될 수 있는 경우에도 여전히 `event_properties`에 접근할 수 있습니다. 이러한 동작에 대한 자세한 내용은 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)를 참조하세요.