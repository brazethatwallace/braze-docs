---
nav_title: 실험 경로
article_title: 실험 경로
alias: /experiment_step/
page_order: 4
page_type: reference
description: "이 문서에서는 사용자 여정의 어느 지점에서든 여러 Canvas 경로를 서로 비교하고 대조군과 비교할 수 있는 구성요소인 실험 경로에 대해 설명합니다."
tool: Canvas
---

# 실험 경로 {#experiment-paths}

> 실험 경로를 사용하면 사용자 여정의 어느 지점에서든 여러 Canvas 경로를 서로 비교하고 대조군과 비교할 수 있습니다. 이 구성요소를 사용하면 경로 성능을 추적하여 Canvas 여정에 대해 정보에 기반한 결정을 내릴 수 있습니다.

사용자 여정에 실험 경로 단계를 포함하면, 생성한 여러 경로(또는 선택적 대조군)에 사용자를 무작위로 할당합니다. 오디언스의 일부가 선택한 비율에 따라 서로 다른 경로에 할당되므로, 서로 다른 메시지나 경로를 비교하여 어떤 것이 가장 효과적인지 판단할 수 있습니다.

![경로 1, 경로 2, 대조군으로 분할되는 실험 경로 단계.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## 사전 요구 사항 {#prerequisites}

실험 경로를 사용하려면 Canvas에 전환 이벤트가 포함되어 있어야 합니다. Canvas가 시작된 후에는 전환 이벤트를 추가할 수 없지만, 시작된 Canvas를 복제하고 전환 이벤트를 추가하여 실험 경로를 추가할 수 있습니다.

## 사용 사례 {#use-cases}

실험 경로는 전달, 발송 주기, 메시지 문구, 채널 조합을 테스트하는 데 가장 적합합니다.

- **전달:** 서로 다른 시간 [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)을 적용한 메시지, 사용자 행동 기반([행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)), [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#step-1-add-intelligent-timing-1) 사용 메시지 간의 결과를 비교합니다.<br><br>
- **발송 주기:** 특정 기간에 걸쳐 여러 메시징 흐름을 테스트합니다. 예를 들어, 두 가지 온보딩 주기를 테스트할 수 있습니다:
    - 주기 1: 사용자의 첫 2주 동안 2개의 메시지 발송
    - 주기 2: 사용자의 첫 2주 동안 3개의 메시지 발송

    휴면 사용자를 타겟팅할 때, 일주일 동안 2개의 윈백 메시지를 보내는 것과 1개만 보내는 것의 효과를 비교 테스트할 수 있습니다.
- **메시지 문구:** 표준 [A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)와 마찬가지로, 어떤 문구가 더 높은 전환율을 가져오는지 확인하기 위해 서로 다른 메시지 문구를 테스트할 수 있습니다.<br><br>
- **채널 조합:** 서로 다른 메시지 채널 조합의 효과를 테스트합니다. 예를 들어, 이메일만 사용하는 경우와 이메일과 푸시를 결합하는 경우의 영향을 비교할 수 있습니다.

## 실험 경로 만들기 {#creating-an-experiment-path}

실험 경로 구성 요소를 만들려면 먼저 Canvas에 단계를 추가합니다. 사이드바에서 구성 요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하고 **실험 경로**를 선택합니다.

이 구성 요소의 기본 구성에는 **경로 1**과 **경로 2**, 두 개의 기본 경로가 있으며 오디언스의 50%가 각 경로로 전송됩니다. 구성 요소를 클릭하면 **실험 설정** 패널이 확장되며, 구성 요소의 설정 옵션을 확인할 수 있습니다.

### 1단계: 경로 수 및 오디언스 분배 선택 {#step-1-choose-the-number-of-paths-and-audience-distribution}

**경로 추가**를 클릭하여 최대 네 개의 경로를 추가할 수 있으며, **대조군 추가**를 체크하여 선택적으로 대조군을 추가할 수 있습니다. 각 경로의 백분율 상자를 사용하여 각 경로와 대조군에 배분할 오디언스의 백분율을 지정할 수 있습니다. 제공된 백분율의 합이 100%가 되어야 진행할 수 있습니다. 사용 가능한 모든 경로(및 대조군)를 동일한 백분율로 빠르게 설정하려면 **경로 균등 분배**를 클릭합니다.

또한 **대조군 동작**에서 대조군의 사용자가 Canvas를 계속 진행할지 또는 전환 추적 기간 이후 종료할지를 선택할 수 있습니다. 선택적으로, 이 실험 경로가 테스트하려는 내용을 다른 사람들에게 설명하거나 참고할 만한 추가 정보를 포함하는 설명을 추가할 수 있습니다.

![경로를 추가하고 각 경로에 사용자 백분율을 분배할 수 있는 실험 설정.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Canvas 재진입이 활성화된 경우, Canvas에 진입하여 무작위로 선택된 경로를 따라간 사용자는 재진입 자격을 얻어 Canvas에 다시 진입할 때 동일한 경로를 다시 따라갑니다. 이를 통해 실험과 관련 분석의 유효성이 유지됩니다. 사용자가 재진입할 때마다 경로 배정을 무작위로 하려면 **실험 경로에서 무작위 경로**를 선택합니다. 이 옵션은 위닝 경로를 사용할 때는 사용할 수 없습니다.
{% endalert %}

### 2단계: 위닝 경로 켜기(선택 사항) {#step-2}

실험을 최적화하려면 [위닝 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path)를 켭니다. 위닝 경로는 처음에 오디언스의 일부로 경로를 테스트합니다. 실험이 종료된 후, Braze는 나머지 및 후속 사용자를 가장 성과가 좋은 경로로 전송합니다.

{% alert note %}
개인화된 경로는 새로운 실험 경로 단계에서 사용할 수 없습니다. 개인화된 경로를 사용하는 기존 단계는 계속 실행됩니다.
{% endalert %}

### 3단계: 경로 만들기 {#step-3-create-paths}

마지막으로, 다운스트림 경로를 구축해야 합니다. **완료**를 선택하고 Canvas 빌더로 돌아갑니다. 각 경로 아래의 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하여 일반적인 Canvas 도구를 사용해 여정을 구축하고, 준비가 되면 Canvas를 시작합니다.

![실험 경로 구성 요소에서 분기되는 각 경로에 단계를 추가하는 모습.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

경로와 해당 다운스트림 단계는 생성된 후에는 Canvas에서 제거할 수 없다는 점을 유의하세요. 그러나 시작된 후에는 필요에 따라 경로 간 오디언스 분배를 수정할 수 있습니다. 예를 들어, Canvas를 시작한 지 하루 후에 분석 결과를 기반으로 하나의 경로가 나머지보다 우수하다고 판단되면 해당 경로를 100%로 설정하고 나머지를 0%로 설정할 수 있습니다. 또는 필요에 따라 여러 경로로 계속 사용자를 전송할 수도 있습니다.

{% alert important %}
실험 오염을 방지하기 위해, 진행 중인 위닝 경로 실험이 있는 활성 Canvas를 업데이트하면 실험이 종료됩니다. 이는 실험 경로 단계를 업데이트하지 않더라도 적용됩니다. 실험을 다시 시작하려면 기존 실험 경로를 연결 해제하고 새로운 실험 경로를 시작하거나, Canvas를 복제하여 복제본을 시작합니다. 실험 경로 단계가 있는 이미 활성화된 Canvas에서는 위닝 경로를 켤 수 없습니다.<br><br>자세한 내용은 [시작 후 Canvases 편집]({{site.baseurl}}/post-launch_edits)을 참조하세요.
{% endalert %}

## 성능 추적 {#tracking-performance}

**Canvas 분석** 페이지에서 실험 경로를 선택하면 **배리언트 분석** 탭과 동일한 [상세 표]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch)가 열리며, 경로 간의 상세 성능 및 전환 통계를 비교할 수 있습니다. CSV로 표를 내보낼 수도 있으며, 선택한 경로 또는 대조군을 기준으로 관심 측정기준의 변동률을 비교할 수 있습니다.

각 경로의 각 단계는 일반 캔버스 단계와 마찬가지로 [Canvas 분석]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) 뷰에 통계를 표시합니다. 다만 개별 단계 분석과 실험 경로 분석은 전환을 다르게 측정한다는 점을 유의하세요.

- **실험 경로 분석**은 사용자가 실험 경로 단계에 진입한 시점부터 전환을 추적합니다. 모든 경로가 동일한 시작점을 공유하므로, 경로 간 성능 비교에 가장 권장되는 뷰입니다.
- **개별 단계 분석**(예: 메시지 단계 분석)은 사용자가 해당 단계를 수신한 시점(예: 메시지가 발송된 시점)부터 전환을 추적합니다.

이러한 전환 기간은 시작점이 다르기 때문에, 동일한 경로에서도 다른 전환율을 보여줄 수 있습니다. 특히 실험 단계와 후속 메시지 사이에 지연이 있는 경우 더욱 그렇습니다. 경로 간 가장 신뢰할 수 있는 비교를 위해서는 실험 경로 분석을 사용하세요.

### 위닝 경로 성능 {#winning-path-performance}

위닝 경로를 사용하면 시간 경과에 따른 성능을 추적하고, 후속 사용자를 가장 성과가 좋은 경로로 자동 전송할 수 있습니다. 자세한 내용은 [위닝 경로 분석]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path#analytics)을 참고하세요.

위닝 측정기준과 실험 경로에 표시되는 분석은 다를 수 있습니다.

- **위닝 경로**에 구성한 전환 이벤트는 Braze가 실험 기간 동안 경로를 비교하고 우승자를 선정하는 방식을 결정합니다.
- 실험 경로 분석은 Canvas의 나머지 부분과 동일한 Canvas [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) 프레임워크를 따르며, [주요 전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#primary-conversion-event)도 포함됩니다. 따라서 대시보드에서 강조되는 측정기준이 위닝 측정기준과 일치하지 않을 수 있습니다.
- 푸시의 경우, *직접 열람*과 *총 열람*이 다릅니다. 자세한 내용은 [영향 받은 열람]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)을 참고하세요.

### 추가 설정 {#additional-settings}

실험 경로는 각 단계에 진입하고 할당된 경로에서 전환한 사용자를 기록합니다. 이 기능은 Canvas 설정에서 지정한 모든 전환 이벤트를 추적합니다. **추가 설정** 탭에서 이 실험이 전환을 추적할 기간을 1일에서 30일 사이로 입력하세요. 여기서 지정하는 기간은 Canvas 설정에서 선택한 전환 이벤트가 실험에 대해 추적되는 기간을 결정합니다. Canvas 설정에서 지정한 이벤트별 전환 기간은 이 단계의 추적에 적용되지 않으며, 이 전환 기간으로 대체됩니다.

전환 기간은 후속 메시지가 발송되는 시점이 아닌, 사용자가 실험 경로 단계에 진입한 시점부터 시작됩니다. 경로에 지연 단계나 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) 같은 지연이 포함된 경우, 해당 지연이 전환 기간의 일부를 소비합니다.

{% alert important %}
실험 경로 내 메시지 단계에 Intelligent Timing을 사용하는 경우, 실험 진입 시점과 실제 메시지 발송 시점 사이의 시간이 해당 경로의 유효 전환 기간을 줄입니다. 예를 들어 실험의 전환 기간이 5일이고 Intelligent Timing이 메시지를 2일 지연시키면, 해당 경로의 사용자는 실험 기간 내에 전환하기까지 메시지 수신 후 3일만 남게 됩니다. 이는 메시지 단계 자체 분석이 메시지 발송 시점부터 전환을 추적하더라도 마찬가지입니다.<br><br>더 깔끔한 실험 분석을 위해, 지연(예: 지연 단계)은 실험 경로 내부가 아닌 실험 경로 단계 **이전**에 배치하세요. 이렇게 하면 모든 경로가 동일한 시점에서 시작하며, 지연이 전환 기간을 소비하지 않습니다.
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 실험 분할이 균등한데 경로별 발송 수가 다른 이유는 무엇인가요? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

다운스트림 *발송*은 실험 경로의 비율 분할뿐만 아니라 각 경로의 단계, 지연, 채널 자격 조건, 콘텐츠에 따라 달라집니다. 예를 들어, 지연 시간, Intelligent Timing, 구독 상태가 서로 다르면 경로 할당이 균등하더라도 메시지를 수신하는 사용자 수가 달라질 수 있습니다. 경로 성과를 비교하려면 공통 진입 지점에서의 전환을 측정하는 [실험 경로 분석](#tracking-performance)을 사용하세요.

### 실험 전환 기간은 얼마나 지속되나요? {#how-long-does-the-experiment-conversion-window-last}

**추가 설정** 전환 기간(1~30일)은 사용자가 실험 경로 단계에 진입할 때 시작됩니다. 다운스트림 지연 단계에서 소요된 시간이나 Intelligent Timing 대기 시간도 해당 기간에 포함됩니다. 자세한 내용은 [성능 추적](#tracking-performance)을 참조하세요.