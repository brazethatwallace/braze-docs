---
nav_title: 오디언스 경로
article_title: 오디언스 경로
alias: /audience_paths/
page_order: 3
page_type: reference
description: "이 참조 문서에서는 Canvas에서 오디언스 경로를 사용하여 각 사용자를 첫 번째로 일치하는 분기로 보내 대규모로 직관적으로 사용자를 필터링하고 세분화하는 방법을 설명합니다."
tool: Canvas

---

# 오디언스 경로 {#audience-paths}

> Canvas 오디언스 경로를 사용하면 각 사용자를 기준에 맞는 첫 번째 경로로 보내 대규모로 직관적으로 사용자를 필터링하고 세분화할 수 있습니다.

이 Canvas 구성요소는 과도한 오디언스 기반 전체 단계를 만들 필요를 없애주며, 여덟 개의 전체 구성요소를 하나로 결합할 수 있습니다. 이를 통해 사용자 타겟팅을 간소화하고 Canvases에서 불필요한 복잡성을 줄일 수 있습니다.

## 작동 방식 {#how-it-works}

![두 개의 그룹(참여 사용자와 나머지 모든 사용자)이 있는 오디언스 경로.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

사용자는 기준을 충족하는 첫 번째 브랜치로 진행하므로, 가장 중요한 경로를 먼저 배치하세요. 이렇게 하면 사용자가 어디로 이동하고 어떤 메시지를 받는지에 대한 모호함이 줄어듭니다. 이 순서는 [출시 후에는 편집할 수 없습니다]({{site.baseurl}}/post-launch_edits).

오디언스 경로를 사용하면 다음을 수행할 수 있습니다:

- 오디언스 기준에 따라 사용자를 서로 다른 Canvas 경로로 보낼 수 있습니다.
- 가장 중요한 오디언스 그룹을 먼저 배치할 수 있습니다. 사용자는 자격을 충족하는 첫 번째 경로로 이동합니다.
- 대규모로 사용자를 정밀하게 타겟팅할 수 있습니다.
  - 오디언스 경로 단계당 최대 8개의 오디언스 그룹(기본 2개 및 추가 6개)을 만들 수 있지만, 사용자를 더 세분화하기 위해 여러 오디언스 경로 단계를 연결할 수도 있습니다.

단일 오디언스 경로 단계 내에서 사용자는 오디언스 그룹에 대해 순서대로 평가되며, 자격을 충족하는 첫 번째 경로로 이동합니다. Canvas에서 여러 오디언스 경로 단계를 연결하면, 사용자는 새로운 오디언스 경로 단계에 도달할 때마다 다시 평가됩니다.

### 사용자 평가 방식 {#how-users-are-evaluated}

![메시지 단계 후 24시간 지연이 있고, 그 뒤에 오디언스 경로가 이어지는 Canvas.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

사용자는 Canvas에 진입한 시점이 아니라 **오디언스 경로 단계에 도달하는 시점**에 필터 및 Segment 멤버십에 대해 평가됩니다. 평가 후 사용자는 즉시 일치하는 경로로 진행합니다. 사용자가 오디언스 그룹에 배치되면, 이후 고객 프로필이 변경되더라도 해당 그룹에 유지됩니다.

<div style="clear: both;"></div>

{% alert important %}
오디언스 경로는 평가 시점의 사용자 현재 속성, 필터 및 Segment 멤버십을 기반으로 평가합니다. Canvas 진입을 트리거한 특정 이벤트를 기반으로 평가하지 않습니다. 사용자가 수행한 행동(예: 커스텀 이벤트)을 기반으로 사용자를 라우팅하려면 대신 [행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)를 사용하세요.
{% endalert %}

### 사용자 평가를 위한 시간 확보 {#allowing-time-for-user-evaluations}

평가가 즉시 이루어지므로, 경로 기준이 이전 단계와의 사용자 상호작용에 의존하는 경우 오디언스 경로 앞에 지연을 추가하는 것이 중요합니다.

예를 들어, 사용자에게 메시지 A를 보내고 다음 단계가 해당 메시지와 상호작용했는지 평가하는 오디언스 경로인 경우, 모든 사용자가 메시지와 상호작용하지 않은 사용자를 위한 단계로 진행하게 됩니다. 이는 사용자가 메시지와 상호작용할 시간 없이 즉시 오디언스 경로 단계로 진행했기 때문입니다. 즉, 사용자는 메시지가 전송된 직후 거의 즉시 메시지 상호작용 여부에 대해 평가됩니다.

전송된 메시지와 상호작용할 시간을 사용자에게 주려면, 메시지 단계와 오디언스 경로 사이에 지연을 추가하세요. 예를 들어, 24시간 지연을 설정하면 사용자가 평가 전에 메시지 A와 상호작용할 수 있는 24시간의 시간이 주어집니다.

## 오디언스 경로 만들기 {#creating-an-audience-path}

오디언스 경로 단계를 추가하려면 다음을 수행하세요:

1. Canvas에 단계를 추가합니다.
2. 사이드바에서 컴포넌트를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> **추가**를 선택한 다음 **오디언스 경로**를 선택합니다.

기본 오디언스 경로 컴포넌트에는 **그룹 1**과 **기타 모든 사용자**라는 두 개의 기본 오디언스 그룹이 포함되어 있습니다. **기타 모든 사용자** 그룹에는 정의된 오디언스 그룹에 해당하지 않는 모든 사용자가 포함됩니다. 이 그룹은 항상 순서에서 마지막에 위치합니다.

### 오디언스 그룹 정의하기 {#defining-audience-groups}

다음 스크린샷은 확장된 오디언스 경로 단계의 레이아웃을 보여줍니다. 여기에서 최대 8개의 오디언스 그룹(1개의 프리셋 및 7개의 커스텀 그룹)을 정의할 수 있습니다. 오디언스 그룹을 정의하려면 오디언스 경로 편집기에서 그룹 이름을 선택합니다. 오디언스 그룹의 이름을 변경하고, 그룹에 적용할 필터와 Segments를 선택하며, 그룹을 추가하거나 삭제할 수 있습니다. 예를 들어, 특정 사용자 그룹에 온보딩 메시징을 타겟팅하려면 "이메일을 클릭함" 및 "인앱 메시지를 클릭함"과 같은 리타겟팅 필터를 선택할 수 있습니다.

![아시아 요리 선호, 라틴 요리 선호, 유럽 요리 선호, 기타 모든 사용자 그룹이 포함된 확장된 오디언스 경로.]({% image_buster /assets/img/audience_path/audience_path3.png %})

오디언스 경로 단계가 완료되면 각 오디언스 그룹에 별도의 브랜치가 생성됩니다. 오디언스 경로를 계속 사용하여 오디언스를 추가로 필터링하거나, 표준 캔버스 단계로 Canvas 여정을 계속할 수 있습니다.

![인게이지먼트에 따라 다른 그룹이 있는 두 개의 오디언스 경로.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### 컨텍스트 변수와 비교 필터 사용하기 {#using-comparison-filters-with-context-variables}

날짜를 포함하는 컨텍스트 변수로 분할할 때, 올바른 비교 유형을 선택하려면 [날짜 컨텍스트 변수에 대한 연중 일자 및 시간 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables)를 참조하세요.

### 오디언스 그룹 테스트하기 {#testing-audience-groups}

오디언스에 Segments와 필터를 추가한 후, [사용자 조회]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)를 통해 오디언스 그룹이 예상대로 설정되었는지 테스트하여 오디언스 기준에 부합하는지 확인할 수 있습니다.

![사용자 조회 섹션.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## 오디언스 경로 사용하기 {#using-audience-paths}

오디언스 경로의 진정한 강점은 가장 중요한 경로를 **먼저** 배치하는 데 있습니다. 이 기능을 반드시 전략적으로 사용할 필요는 없지만, 일부 마케터는 스페셜 상품이나 한정판 출시와 같은 특정 제품을 사용자에게 푸시하는 데 활용할 수 있습니다.

해당 Segments를 목록의 맨 앞에 배치하면, 특정 필터와 Segments에 해당하는 사용자를 타겟팅하면서도 해당 기준에 맞지 않는 사용자까지 모두 하나의 캔버스 단계에서 타겟팅할 수 있습니다.

![「Likes Big Brand Shoes」, 「Likes Big Brand」, 「Everyone Else」 그룹이 있는 오디언스 경로.]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

예를 들어, 사용자 그룹에게 신제품 광고를 보내고 싶다고 가정해 보겠습니다. 먼저 해당 제품에 해당하는 필터를 오디언스 경로에서 **먼저** 배치합니다. "Big Brand"라는 회사를 위한 마케팅 Campaign을 만들고 새로운 소매 브랜드가 출시되었다면, "Likes Big Brand Shoes"나 "Likes Big Brand Bags"와 같은 필터를 선택하고, 해당 필터 그룹에 따라 서로 다른 이메일 메시지를 보낼 수 있습니다.

사용자가 이 오디언스 경로 구성 요소에 진입하면, 먼저 목록의 첫 번째 경로인 오디언스 그룹 1 "Likes Big Brand Shoes"에 대해 평가됩니다. 해당되면 Canvas에서 정의한 다음 구성 요소로 진행합니다. "Like Big Brand Shoes"에 해당하지 않으면, 다음 오디언스 그룹인 오디언스 그룹 2 "Likes Big Brand Bags"에 대해 평가되며, 기준을 충족하면 다음 단계로 진행합니다. 마지막으로, 이전 그룹에 해당하지 않는 사용자는 "Everybody Else" 그룹에 포함되어 해당 경로에 대해 정의한 다음 캔버스 단계로 진행합니다.

[Canvas 분석]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization)을 사용하여 이 단계의 성능을 확인할 수도 있습니다.

### 무작위 버킷 번호로 오디언스 경로 세분화하기 {#segmenting-audience-paths-with-random-bucket-numbers}

Canvas에서 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)(예: Canvas를 수신할 전체 사용자 수 제한)을 사용하는 경우, Braze는 무작위 버킷 번호를 사용하여 오디언스 경로를 세분화하지 않는 것을 권장합니다.

[무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)는 균일하게 분포된 무작위 사용자 Segments를 생성하는 데 사용할 수 있는 사용자 속성입니다. Braze는 Canvas 진입의 세분화 단계에서 무작위 버킷 번호를 사용하여 사용자를 그룹화하며, 각 그룹은 별도로 처리됩니다. 어떤 그룹이 먼저 처리를 완료하느냐에 따라, 사용량 제한으로 인해 일부 사용자가 진입 시 제한될 수 있으며, 이로 인해 오디언스 경로 단계에 도달하는 사용자의 분포가 불균등해질 수 있습니다.

이 경우에는 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)를 대신 사용해 보세요.

### 오디언스 경로에서 인텔리전트 채널 필터 사용하기 {#using-intelligent-channel-filter-with-audience-paths}

오디언스 경로 단계와 인텔리전트 채널 필터를 조합하면, 각 사용자의 선호도와 행동에 맞게 메시징 경험을 맞춤 설정할 수 있습니다. 이를 통해 사용자는 적절한 채널을 통해 가장 관련성 높은 메시지를 받게 됩니다.

예를 들어, 오디언스 경로 단계에서 이메일, 모바일 푸시, Everyone Else의 세 가지 오디언스를 만들 수 있습니다. 이메일 오디언스에는 `Intelligent Channel is Email` 필터를 추가합니다. 모바일 푸시 오디언스에는 `Intelligent Channel is Mobile Push` 필터를 추가합니다. 그런 다음 각 오디언스 경로에 메시지 단계를 추가하여 개인화된 관련 메시지를 전달할 수 있습니다.

{% alert tip %}
[Braze Canvas 템플릿]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)에서 이러한 사전 제작 템플릿을 활용하여 맞춤 설정하는 방법에 대한 예시를 확인해 보세요.
{% endalert %}