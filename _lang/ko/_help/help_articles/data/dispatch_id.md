---
nav_title: 디스패치 ID 동작
article_title: 디스패치 ID 동작
page_order: 0

page_type: solution
description: "이 도움말 문서에서는 사용 방법, 의미 및 제한 사항 등 디스패치 ID 동작에 대해 설명합니다."
---

# 디스패치 ID 동작 {#dispatch-id-behavior}

`dispatch_id`는 메시지 발송의 ID로, Braze에서 보낸 각 "전송"에 대한 고유 ID입니다. 예약 메시지를 받은 사용자에게는 동일한 `dispatch_id`가 전송됩니다. 일반적으로 액션 기반 또는 API 트리거된 메시지는 사용자당 고유한 `dispatch_id`를 수신하지만, 서로 가까운 시간에 전송된 메시지는 여러 사용자 간에 동일한 `dispatch_id`를 공유할 수 있습니다.

따라서 메시지가 서로 다른 시간에 전송된 경우 단일 Campaign에 대해 두 명의 사용자가 서로 다른 디스패치 ID를 갖게 될 수 있습니다. 이는 API 요청이 개별적으로 이루어졌기 때문인 경우가 많습니다. 두 사용자가 단일 전송에서 동일한 Campaign 오디언스에 속해 있다면 두 사용자의 디스패치 ID는 동일합니다.

## Campaigns의 디스패치 ID 동작 {#dispatch-id-behavior-in-campaigns}

예약된 Campaign 메시지는 동일한 `dispatch_id`를 갖습니다. 액션 기반 또는 API 트리거 Campaign 메시지는 사용자당 고유한 `dispatch_id`를 받거나, 위에서 설명한 대로 근접한 시간에 또는 동일한 API 호출로 전송되는 경우 여러 사용자에게 동일한 `dispatch_id`가 부여될 수 있습니다. 예를 들어, 예약된 Campaign 오디언스에 속한 두 명의 사용자는 Campaign이 예약될 때마다 동일한 `dispatch_id`를 갖게 됩니다. 그러나 API 트리거 Campaign의 오디언스에 있는 두 사용자가 서로 가까운 시간이 아닌 별도의 API 호출을 통해 전송된 경우 서로 다른 디스패치 ID를 가질 수 있습니다.

멀티채널 Campaigns는 전달 유형에 대해 설명한 것과 동일한 동작을 갖습니다.

{% alert warning %}
`dispatch_id`는 모든 캔버스 단계에 대해 무작위로 생성되는데, 이는 Braze가 캔버스 단계를 "예약된" 경우에도 트리거된 이벤트로 취급하기 때문입니다. 이로 인해 ID 생성에 불일치가 발생할 수 있습니다. 때때로 Canvas 구성요소는 전송당 사용자당 고유한 `dispatch_id`를 갖거나, 전송당 사용자 간에 공유 디스패치 ID를 가질 수 있습니다.
{% endalert %}

## Liquid를 사용하여 디스패치 ID를 메시지에 템플릿화 {#template-dispatch-id-into-messages-with-liquid}

메시지 내에서 메시지 발송을 추적하려면(예: URL) `dispatch_id`를 템플릿으로 삽입할 수 있습니다. [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) 목록의 Canvas 속성에서 이에 대한 형식을 확인할 수 있습니다.

Campaign 생성 시 `api_id`를 사용할 수 없으므로 입력 안내로 템플릿이 지정되고 `dispatch_id_for_unsent_campaign`으로 미리보기된다는 점에서 `api_id`와 동일하게 작동합니다. ID는 메시지가 전송되기 전에 생성되며 전송 시간에 포함됩니다.

{% alert warning %}
인앱 메시지에는 `dispatch_id`가 없으므로 `dispatch_id_for_unsent_campaign`의 Liquid 템플릿은 인앱 메시지에서 작동하지 않습니다.
{% endalert %}

## 이메일용 디스패치 ID Currents 필드 {#dispatch-id-currents-field-for-email}

Currents 기능을 지속적으로 개선하기 위해 모든 커넥터 유형에 걸쳐 Currents 이메일 이벤트에 `dispatch_id` 필드를 추가했습니다. `dispatch_id`는 Braze 플랫폼에서 전송되는 각 전송 또는 디스패치에 대해 생성된 고유 ID입니다.

예약 메시지를 받는 모든 고객은 동일한 `dispatch_id`를 받지만, 액션 기반 또는 API 트리거된 메시지를 받는 고객은 메시지당 고유한 `dispatch_id`를 받습니다. `dispatch_id` 필드를 사용하면 어떤 반복 Campaign 인스턴스가 전환을 담당하는지 식별할 수 있으므로, 어떤 유형의 Campaigns가 비즈니스 목표를 달성하는 데 도움이 되는지에 대한 더 많은 인사이트와 정보를 얻을 수 있습니다.

`dispatch_id`를 [개인화 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)로 사용하거나, [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)에서, 또는 Currents용 [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events), [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/)를 사용할 때 활용할 수 있습니다.

_마지막 업데이트: 2021년 7월 15일_