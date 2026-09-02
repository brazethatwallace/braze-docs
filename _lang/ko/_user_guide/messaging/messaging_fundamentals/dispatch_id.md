---
nav_title: 디스패치 ID
article_title: 디스패치 ID 동작
page_order: 5.2
page_type: reference
description: "이 참조 문서에서는 Campaign, Canvas, Liquid 및 Currents에 대한 디스패치 ID 동작에 대해 설명합니다."
---

# 디스패치 ID 동작 {#dispatch-id-behavior}

> `dispatch_id`는 Braze에서 보낸 각 메시지 발송, 즉 "전송"에 대한 고유 ID입니다.

## Campaigns에서의 디스패치 ID 동작 {#dispatch-id-behavior-in-campaigns}

예약된 Campaign 메시지는 동일한 `dispatch_id`를 받습니다. 액션 기반 또는 API 트리거 Campaign 메시지는 사용자별로 고유한 `dispatch_id`를 받을 수도 있고, 근접한 시간 내에 전송되거나 동일한 API 호출로 전송된 경우 여러 사용자가 동일한 `dispatch_id`를 받을 수도 있습니다. 예를 들어, 예약된 Campaign 오디언스에 포함된 두 명의 사용자는 Campaign이 예약될 때마다 동일한 `dispatch_id`를 갖습니다. 그러나 API 트리거 Campaign의 오디언스에 포함된 두 명의 사용자는 별도의 API 호출로 전송되었고 서로 근접한 시간이 아닌 경우 서로 다른 디스패치 ID를 가질 수 있습니다.

멀티채널 Campaigns도 해당 전달 유형에 대해 동일한 동작을 합니다.

{% alert warning %}
Braze는 Canvas 단계를 "예약된" 경우에도 트리거된 이벤트로 취급하기 때문에, 모든 캔버스 단계에 대해 `dispatch_id`가 무작위로 생성됩니다. 이로 인해 ID 생성 시 불일치가 발생할 수 있습니다. 경우에 따라 Canvas 구성 요소가 전송당 사용자별로 고유한 `dispatch_id`를 가질 수도 있고, 전송당 사용자 간에 공유된 디스패치 ID를 가질 수도 있습니다.
{% endalert %}

## Liquid를 사용하여 메시지에 디스패치 ID 템플릿 삽입하기 {#template-dispatch-id-into-messages-with-liquid}

메시지 내부에서(예: URL에서) 메시지의 디스패치를 추적하려면 `dispatch_id`를 템플릿으로 삽입할 수 있습니다. 이에 대한 형식은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) 목록의 Canvas 속성에서 확인할 수 있습니다.

이 동작은 `api_id`와 유사합니다. Campaign 생성 시점에는 `api_id`를 사용할 수 없으므로, Braze는 이를 플레이스홀더로 템플릿 처리하며 `dispatch_id_for_unsent_campaign`으로 미리보기됩니다. 이 ID는 메시지가 전송되기 전에 생성되며, 전송 시점에 포함됩니다.

{% alert warning %}
`dispatch_id_for_unsent_campaign`의 Liquid 템플릿은 In-App Messages에서는 작동하지 않습니다. In-App Messages에는 `dispatch_id`가 없기 때문입니다.
{% endalert %}

## 이메일용 디스패치 ID Currents 필드 {#dispatch-id-currents-field-for-email}

`dispatch_id` 필드는 모든 커넥터 유형의 Currents 이메일 이벤트에서 사용할 수 있습니다. `dispatch_id`는 Braze 플랫폼에서 전송(디스패치)할 때마다 생성되는 고유 ID입니다.

스케줄된 메시지를 수신하는 모든 고객은 동일한 `dispatch_id`를 받지만, 액션 기반 또는 API 트리거된 메시지를 수신하는 고객은 메시지별로 고유한 `dispatch_id`를 받습니다. `dispatch_id` 필드를 사용하면 반복 Campaign의 어떤 인스턴스가 전환에 기여했는지 식별할 수 있으므로, 어떤 유형의 Campaign이 성과를 이끌어내는지 확인할 수 있습니다.

`dispatch_id`는 [개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)에서 사용하거나, Currents에 [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents), [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel#supported-currents-events) 또는 [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)를 사용할 때 활용할 수 있습니다.