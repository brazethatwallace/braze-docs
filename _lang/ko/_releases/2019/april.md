---
nav_title: 4월
page_order: 9
noindex: true
page_type: update
description: "이 문서에는 2019년 4월의 릴리스 노트가 포함되어 있습니다."
---

# 2019년 4월 {#april-2019}

## 새로운 Currents 이벤트 및 필드 {#new-currents-events-fields}

섹션의 일부 수정 사항과 더불어, 메시지 참여 이벤트 페이지에 새로운 [구독 이벤트]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events)가 추가되었습니다.

이제 구독 그룹 상태 변경 데이터를 Braze에서 [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) 및 [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/)로 내보낼 수 있으며, [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)에서는 해당 데이터와 설치 경로 이벤트도 내보낼 수 있습니다.

또한 `canvas_step_id` 등록정보가 사용 가능한 [전환 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events)에 추가되었습니다.

{% alert important %}
이러한 업데이트를 활용하려면 Currents 커넥터 설정을 편집하고 사용하려는 이벤트를 활성화해야 합니다. 궁금한 점이 있으면 계정 매니저에게 문의하세요.
{% endalert %}

## 구독 그룹 아카이브 {#subscription-groups-archiving}

이제 [구독 그룹을 아카이브]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)할 수 있습니다! 아카이브된 구독 그룹은 편집할 수 없으며 Segment 필터에 더 이상 표시되지 않습니다. 이메일, Campaign 또는 Canvas에서 Segment 필터로 사용 중인 그룹을 아카이브하려고 하면, 해당 그룹의 모든 사용을 제거할 때까지 아카이브할 수 없다는 오류 메시지가 표시됩니다.