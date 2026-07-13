---
nav_title: 디스패치 ID
article_title: 디스패치 ID 동작
page_order: 5.2
page_type: reference
description: "이 참조 문서에서는 Campaign(캠페인), Canvas, Liquid 및 Currents에 대한 디스패치 ID 동작에 대해 설명합니다."
---

# 디스패치 ID 동작 {#dispatch-id-behavior}

> `dispatch_id`는 Braze에서 보낸 각 메시지 발송, 즉 "전송"에 대한 고유 ID입니다.

## Campaign의 디스패치 ID 동작 {#dispatch-id-behavior-in-campaigns}

예약된 Campaign 메시지는 동일한 `dispatch_id`를 갖습니다. 액션 기반 또는 API 트리거 Campaign 메시지는 사용자당 고유한 `dispatch_id`를 받거나, 근접한 시간에 또는 동일한 API 호출로 전송되는 경우 여러 사용자에게 동일한 `dispatch_id`가 부여될 수 있습니다. 예를 들어, 예약된 Campaign 오디언스에 속한 두 명의 사용자는 Campaign이 예약될 때마다 동일한 `dispatch_id`를 갖게 됩니다. 그러나 API 트리거 Campaign의 오디언스에 있는 두 사용자가 별도의 API 호출을 통해 서로 가까운 시간이 아닌 시점에 전송된 경우 서로 다른 디스패치 ID를 가질 수 있습니다.

멀티채널 Campaign은 전달 유형에 대해 설명한 것과 동일한 동작을 갖습니다.

{% alert warning %}
`dispatch_id`는 모든 캔버스 단계에 대해 무작위로 생성되는데, 이는 Braze가 캔버스 단계를 "예약된" 경우에도 트리거된 이벤트로 취급하기 때문입니다. 이로 인해 ID 생성에 불일치가 발생할 수 있습니다. 때때로 Canvas 구성요소는 전송당 사용자당 고유한 `dispatch_id`를 갖거나, 전송당 사용자 간에 공유 디스패치 ID를 가질 수 있습니다.
{% endalert %}

## Liquid를 사용하여 디스패치 ID를 메시지에 템플릿화 {#template-dispatch-id-into-messages-with-liquid}

메시지 내에서(예: URL) 메시지 발송을 추적하려면 `dispatch_id`를 템플릿으로 삽입할 수 있습니다. 이에 대한 형식은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) 목록의 Canvas 속성에서 확인할 수 있습니다.

이는 `api_id`와 동일하게 동작합니다. Campaign 생성 시 `api_id`를 사용할 수 없기 때문에 Braze는 이를 `dispatch_id_for_unsent_campaign`으로 미리보기되는 입력 안내로 템플릿화합니다. 이 ID는 메시지가 전송되기 전에 생성되며 전송 시점에 포함됩니다.

{% alert warning %}
인앱 메시지에는 `dispatch_id`가 없으므로 `dispatch_id_for_unsent_campaign`의 Liquid 템플릿화는 인앱 메시지에서 작동하지 않습니다.
{% endalert %}

## 이메일에 대한 디스패치 ID Currents 필드 {#dispatch-id-currents-field-for-email}

`dispatch_id` 필드는 모든 커넥터 유형에 걸쳐 Currents 이메일 이벤트에서 사용할 수 있습니다. `dispatch_id`는 Braze 플랫폼에서 보낸 각 전송 또는 발송에 대해 생성되는 고유 ID입니다.

예약된 메시지를 받은 모든 고객은 동일한 `dispatch_id`를 받지만, 액션 기반 또는 API 트리거된 메시지를 받은 고객은 메시지당 고유한 `dispatch_id`를 받습니다. `dispatch_id` 필드를 사용하면 반복 Campaign의 어떤 인스턴스가 전환에 기여했는지 식별할 수 있으므로, 어떤 유형의 Campaign이 결과를 이끌어내는지 확인할 수 있습니다.

`dispatch_id`는 [개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#supported-personalization-tags), [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 또는 Currents용 [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents#email-events), [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)를 사용할 때 활용할 수 있습니다.