---
nav_title: 무작위 버킷 번호
article_title: 무작위 버킷 번호
page_order: 2
page_type: reference
description: "이 문서에서는 무작위 버킷 번호의 개념과 이를 사용하여 배리언트 및 대조군을 만드는 방법을 설명합니다."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# 무작위 버킷 번호 {#random-bucket-numbers}

> 무작위 버킷 번호는 균일하게 분포된 무작위 사용자 Segment를 만드는 데 사용할 수 있는 사용자 속성입니다.

## 개요 {#overview}

Braze에서 고객 프로필이 생성되면 해당 사용자에게 0에서 9999 사이(양 끝값 포함)의 무작위 버킷 번호가 자동으로 할당됩니다. 이러한 Segment를 사용하여 시간 경과에 따라 사용자 그룹에 대한 여러 Campaigns 또는 Canvases의 효과를 테스트할 수 있습니다.

### 글로벌 컨트롤 그룹 사용 {#global-control-group-usage}

무작위 버킷 번호는 글로벌 컨트롤 그룹&#8212;Campaign이나 Canvas를 수신하지 않는 사용자 그룹에서 사용됩니다. Braze는 무작위 버킷 번호의 여러 범위를 무작위로 선택하고 해당 선택된 버킷의 사용자를 포함합니다. 무작위 버킷 번호는 가중치나 최근 할당된 번호에 대한 고려 없이 할당됩니다.

{% alert note %}
사용자가 삭제된 후 다시 생성되면 새로운 사용자로 간주되므로 다른 무작위 버킷 번호가 할당됩니다.
{% endalert %}

글로벌 컨트롤 그룹이 설정되어 있고 다른 사용 사례에 무작위 버킷 번호를 사용하려면 [주의할 사항]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for)을 확인하세요.

### 무작위 버킷 번호를 사용해야 하는 경우 {#when-to-use-random-bucket-numbers}

시간 경과에 따라 여러 Campaigns 또는 Canvases의 효과에 대한 장기 테스트를 수행하려면 무작위 버킷 번호를 사용하여 사용자를 세분화할 수 있습니다.

### 다른 방법을 사용해야 하는 경우 {#when-to-use-something-else}

단일 Campaign 또는 단일 Canvas 내에서 테스트를 위해 사용자를 세분화하려면 Campaign의 경우 [A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests)를 사용하세요. Canvas의 경우 여정 수준 테스트를 위해 다양한 [배리언트]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-21-add-a-variant)를 만들거나, 단계 수준 테스트를 위해 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)를 사용할 수 있습니다.

## 무작위 버킷 번호를 사용하여 Segment 생성 {#create-segments-using-random-bucket-numbers}

[Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)할 때 "Random Bucket #" 필터를 추가하세요. 그런 다음 Segment에 포함할 번호 또는 번호 범위를 지정합니다.

![무작위 버킷 번호가 "3000" 이하인 Segment 필터.]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

세 가지 배리언트의 테스트를 실행하면서 대조군도 포함하려는 경우 이러한 유형의 Segment를 사용할 수 있습니다. 세 가지 배리언트와 대조군에 대해 동일한 크기의 Segment를 만드는 다음 샘플 계획을 참고하세요:

- 버킷 번호 0~2499는 대조 Segment에 해당합니다
- 버킷 번호 2500~4999는 배리언트 1을 수신할 Segment에 해당합니다
- 버킷 번호 5000~7499는 배리언트 2를 수신할 Segment에 해당합니다
- 버킷 번호 7500~9999는 배리언트 3을 수신할 Segment에 해당합니다

원하는 Segment 수와 각 Segment 내 사용자 분포에 따라 계획이 달라질 수 있습니다.

대조군을 포함한 각 무작위 버킷 번호 Segment에 대해 [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)을 켜세요. 대조군 대비 배리언트의 성공을 평가할 때 [커스텀 이벤트]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) 페이지로 이동하여 각 Segment가 특정 커스텀 이벤트를 완료한 빈도를 확인할 수 있습니다.

{% alert tip %}
Canvas에서 무작위 버킷 번호 Segment를 사용할 때, 예를 들어 [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) 단계의 필터로 사용하는 경우, Canvas의 [종료 기준]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria), 오디언스 필터 및 업스트림 단계가 버킷 범위 중 하나와 겹치는 Segment를 타겟팅하지 않는지 확인하세요. 겹치는 경우 해당 범위의 사용자가 분할에 도달하기 전에 불균형하게 제거되어 경로 간 분포가 불균등해질 수 있습니다.
{% endalert %}

### 무작위 버킷 번호를 사용한 무작위 오디언스 재진입 {#random-audience-re-entry-using-random-bucket-numbers}

무작위 오디언스 재진입은 [A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing/faq#what-is-the-difference-between-ab-testing-and-multivariate-testing) 또는 Campaigns에서 특정 사용자 그룹을 타겟팅하는 데 유용할 수 있습니다. 무작위 버킷 번호를 사용하여 무작위 오디언스 재진입을 수행하려면 다음을 수행하세요:

1. [Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)합니다.
2. 무작위 버킷을 정의합니다. Campaign 또는 Canvas에서 무작위 버킷 필터를 사용하여 오디언스를 여러 그룹으로 나눕니다. 예를 들어, 오디언스를 나누기 위해 정확히 두 개의 무작위 버킷을 지정할 수 있습니다(버킷당 사용자의 50%).
3. Campaign 또는 Canvas의 **Target Audiences** 섹션에서 무작위 버킷 설정을 지정합니다. 이를 통해 Braze가 정의된 비율에 따라 사용자를 적절한 버킷에 자동으로 할당할 수 있습니다.
4. 사용자가 Segment에 재진입할 수 있는 로직을 설정합니다. 예를 들어, 15일 동안 앱에 참여하지 않은 사용자가 Segment에 재진입할 수 있도록 허용할 수 있습니다.
5. Campaign을 시작하고 각 버킷의 성과를 모니터링합니다. 참여율 및 전환율과 같은 측정기준을 분석하여 무작위 오디언스 재진입이 사용 사례에 얼마나 효과적인지 판단할 수 있습니다.