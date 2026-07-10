---
nav_title: 개인화된 경로
article_title: 실험 경로의 개인화된 경로
page_type: reference
description: "개인화된 경로를 사용하면 전환 가능성에 따라 개별 사용자에 맞게 Canvas 여정의 모든 지점을 개인화할 수 있습니다."
tool: Canvas
---

# 실험 경로의 개인화된 경로 {#personalized-paths-in-experiment-paths}

> 개인화된 경로는 Campaigns의 [개인화된 배리언트]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations#personalized-variant)와 유사하며, 전환 가능성에 따라 개별 사용자에 맞게 Canvas 여정의 모든 지점을 개인화할 수 있습니다.

## 개인화된 경로 작동 방식 {#how-personalized-paths-works}

실험 경로 단계에서 개인화된 경로를 켜면, Canvas가 단일 발송인지 반복 발송인지에 따라 동작이 약간 달라집니다.

- **단일 발송 Canvas:** 일부 사용자 그룹이 지연 그룹에 보류됩니다. 나머지 사용자는 초기 테스트에 진입하여 설정한 기간 동안 예측 모델을 학습시킵니다. 최상의 결과를 위해 최소 24시간이 권장됩니다. 테스트 후, 특정 경로에서 전환할 가능성이 더 높은 사용자 행동을 학습하는 모델이 생성됩니다. 마지막으로, 지연 그룹의 각 사용자는 자신이 보이는 행동과 초기 테스트에서 예측 모델이 학습한 내용을 기반으로 전환 가능성이 가장 높은 경로로 보내집니다.
- **반복, 액션 트리거 및 API 트리거 Canvases:** 지정된 기간 동안 실험 경로에 진입하는 모든 사용자에 대해 초기 실험이 수행됩니다. 실험의 무결성을 유지하기 위해, 기간이 끝나기 전에 사용자가 여러 메시지를 받는 경우 매번 동일한 배리언트에 할당됩니다. 실험 기간이 끝나면, 각 사용자는 자신에게 전환 가능성이 가장 높은 경로로 보내집니다.

## 개인화된 경로 사용하기 {#using-personalized-paths}

### 1단계: 실험 경로 추가 {#step-1-add-an-experiment-path}

Canvas에 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)를 추가한 다음 **개인화된 경로**를 켭니다.

![Canvas에 실험 경로를 추가한 다음 개인화된 경로를 켭니다.]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### 2단계: 개인화된 경로 설정 구성 {#step-2-configure-personalized-paths-settings}

우승자를 결정할 전환 이벤트를 지정합니다. 사용 가능한 전환 이벤트가 없는 경우, Canvas 설정의 첫 번째 단계로 돌아가서 [전환 이벤트를 할당]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events)하세요.

전환 이벤트로 열람 또는 클릭을 선택하는 경우, 경로의 첫 번째 단계가 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)인지 확인하세요. Braze는 각 경로의 첫 번째 메시지 단계에서의 인게이지먼트만 집계합니다. 경로가 다른 단계(예: 지연 또는 오디언스 경로 단계)로 시작하고 메시지가 나중에 오는 경우, 해당 메시지는 성능 평가 시 포함되지 않습니다.

그런 다음 **실험 기간**을 설정합니다. **실험 기간**은 지연 그룹의 각 사용자에게 최적의 경로를 선택하기 전에 모든 경로로 사용자를 보내는 기간을 결정합니다. 기간은 첫 번째 사용자가 단계에 진입할 때 시작됩니다.

![개인화된 경로 설정 구성과 관련된 스크린샷.]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### 3단계: 대체 방법 결정 {#step-3-determine-fallback}

기본적으로, 테스트 결과가 통계적으로 유의미한 우승자를 결정하기에 충분하지 않은 경우, 이후 모든 사용자는 단일 최고 성능 경로로 보내집니다.

또는 **이후 모든 사용자에게 경로 조합을 계속 발송**을 선택할 수 있습니다.

![이후 모든 사용자에게 경로 조합을 계속 발송을 선택할 수 있습니다.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

이 옵션은 실험 경로 배분에 지정된 비율에 따라 이후 사용자를 경로 조합으로 보냅니다.

![대체 방법 결정과 관련된 스크린샷.]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### 4단계: 경로 추가 및 Canvas 시작 {#step-4-add-your-paths-and-launch-the-canvas}

{% tabs local %}
{% tab 단일 발송 Canvas %}

단일 실험 경로 구성요소에는 최대 4개의 경로를 포함할 수 있습니다. 그러나 단일 발송 Canvas의 경우, 개인화된 경로가 켜져 있으면 최대 3개의 경로를 추가할 수 있습니다. 네 번째 경로는 Braze가 실험에 자동으로 추가하는 지연 그룹을 위해 예약되어야 합니다.

필요에 따라 Canvas 설정을 완료한 다음 시작합니다. 첫 번째 사용자가 실험에 진입하면, Canvas를 확인하여 분석 데이터가 들어오는 것을 보고 [실험 성능을 추적]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance)할 수 있습니다.

![경로를 추가하고 Canvas를 시작하는 것과 관련된 스크린샷.]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

실험 기간이 지나고 실험이 완료되면, Braze는 예측 모델의 추천을 기반으로 지연 그룹의 사용자를 개인화된 전환 가능성이 가장 높은 각각의 경로로 보냅니다.

![경로를 추가하고 Canvas를 시작하는 것과 관련된 스크린샷.]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab 반복 또는 액션 트리거 또는 API 트리거 Canvas %}

단일 실험 경로에서 최대 4개의 경로를 테스트할 수 있습니다. 경로를 추가하고 필요에 따라 Canvas 설정을 완료한 다음 시작합니다.

첫 번째 사용자가 실험에 진입하면, Canvas를 확인하여 분석 데이터가 들어오는 것을 보고 [실험 성능을 추적]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance)할 수 있습니다.

실험 기간이 지나고 실험이 완료되면, 이후 Canvas에 진입하는 모든 사용자는 자신에게 전환 가능성이 가장 높은 경로로 보내집니다.

![경로를 추가하고 Canvas를 시작하는 것과 관련된 스크린샷.]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## 분석 {#analytics}

개인화된 경로가 켜져 있고 충분한 결과가 나오면, 분석 보기가 **초기 실험**과 **개인화된 경로** 두 개의 탭으로 구분됩니다.

실험이 불충분한 결과로 완료되면, 모델이 개인화가 모든 사용자를 단일 최고 성능 경로로 보내는 것보다 나은 결과를 내지 못한다고 판단하기 때문에 **초기 실험** 탭만 표시됩니다. 이 경우 구성된 대체 동작이 적용되며, 개인화된 경로 분석은 제공되지 않습니다.

{% tabs local %}
{% tab 초기 실험 %}

**초기 실험** 탭은 실험 기간 동안 각 경로의 측정기준을 보여줍니다. 지정된 전환 이벤트에 대해 모든 경로가 어떻게 수행되었는지 요약을 확인할 수 있습니다.

![각 사용자에게 최적의 경로를 결정하기 위해 발송된 초기 실험의 결과. 테이블은 타겟 채널에 대한 다양한 측정기준을 기반으로 각 경로의 성능을 보여줍니다.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

기본적으로, 테스트는 사용자의 커스텀 이벤트와 경로 선호도, 즉 사용자가 가장 잘 반응하는 메시지 배리언트 간의 연관성을 찾습니다. 이 분석은 커스텀 이벤트가 특정 경로에 대한 반응 가능성을 높이는지 낮추는지를 감지합니다. 이러한 관계는 실험 기간이 지난 후 어떤 사용자에게 어떤 경로를 할당할지 결정하는 데 사용됩니다.

커스텀 이벤트와 경로 선호도 간의 관계는 **초기 실험** 탭의 테이블에 표시됩니다.

![분석과 관련된 스크린샷.]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

테스트가 커스텀 이벤트와 경로 선호도 간에 의미 있는 관계를 찾지 못하면, 세션 기반 분석 방법으로 대체되며 커스텀 이벤트 데이터 테이블은 표시되지 않습니다.

{% details 대체 분석 방법 %}

**세션 기반 분석 방법**<br>
개인화된 경로를 결정하는 데 대체 방법이 사용되면, **초기 실험** 탭에 특정 특성의 조합을 기반으로 사용자의 선호 배리언트 분류가 표시됩니다.

이러한 특성은 다음과 같습니다.

- **최근성:** 마지막 세션이 언제였는지
- **빈도:** 세션이 얼마나 자주 있는지
- **사용 기간:** 사용자가 된 지 얼마나 되었는지

![사용자 특성 테이블로, 최근성, 빈도, 사용 기간의 세 가지 버킷에 따라 어떤 사용자가 경로 1과 경로 2를 선호할 것으로 예측되는지 보여줍니다.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

최근성은 마지막 상호작용이 얼마나 최근인지, 빈도는 얼마나 자주 참여하는지, 사용 기간은 전체적으로 얼마나 오래 참여해 왔는지를 나타냅니다. 이 세 가지를 기반으로 사용자를 "버킷"으로 그룹화한 다음(**사용자 특성** 테이블에 설명된 대로), 어떤 버킷이 어떤 경로를 더 선호하는지 확인합니다. 마지막으로 쇼핑한 시기, 쇼핑 빈도, 고객이 된 기간을 기준으로 사용자를 수백 개의 다른 목록으로 분류하는 것과 같습니다.

사용자에게 메시지를 선택할 때, Braze는 해당 사용자가 속한 버킷을 검토합니다. 각 버킷은 사용자의 경로 선택에 고유한 영향을 미칩니다. 이 영향은 [로지스틱 회귀](https://en.wikipedia.org/wiki/Logistic_regression)라는 통계적 방법을 사용하여 정량화하며, 이는 과거 행동을 기반으로 미래 행동을 예측하는 방법입니다. 이 방법은 초기 메시지 발송 중 사용자 상호작용을 고려합니다. 이 테이블은 각 버킷의 사용자가 어떤 경로에 참여하는 경향이 있었는지를 표시하여 결과를 요약합니다.

궁극적으로, Braze는 이 모든 데이터를 결합하여 각 사용자에게 맞춤화된 메시지 경로를 선택하여 가능한 한 참여도가 높고 관련성 있는 경험을 제공합니다.

{% alert note %}
각 버킷의 시간 간격은 Canvas별 사용자 데이터를 기반으로 결정되며, Canvas마다 다를 수 있습니다.
{% endalert %}

**개인화된 경로 선택 방법**<br>
이 방법에서 개별 사용자의 추천 메시지는 해당 사용자의 특정 최근성, 빈도, 사용 기간의 효과를 합산한 것입니다. 최근성, 빈도, 사용 기간은 **사용자 특성** 테이블에 설명된 대로 버킷으로 나뉩니다. 각 버킷의 시간 범위는 개별 Canvas의 사용자 데이터에 의해 결정되며 Canvas마다 달라집니다.

각 버킷은 각 경로에 대해 서로 다른 기여도 또는 "추진력"을 가질 수 있습니다. 각 버킷의 추진력 강도는 [로지스틱 회귀](https://en.wikipedia.org/wiki/Logistic_regression)를 사용하여 초기 실험에서의 사용자 응답으로부터 결정됩니다. 이 테이블은 각 버킷의 사용자가 어떤 경로에 참여하는 경향이 있었는지를 표시하여 결과를 요약합니다. 개별 사용자의 실제 개인화된 경로는 해당 사용자가 속한 세 가지 버킷(각 특성당 하나)의 효과를 합산하여 결정됩니다.

{% enddetails %}

{% endtab %}
{% tab 개인화된 경로 %}

**개인화된 경로** 탭은 지연 그룹의 사용자가 자신에게 최적의 경로로 보내진 최종 실험의 결과를 보여줍니다.

이 페이지의 세 개 카드는 예상 향상도, 전체 결과, 그리고 우승 경로만 발송했을 경우의 예상 결과를 보여줍니다. 향상이 없는 경우(가끔 발생할 수 있음)에도 결과는 우승 경로만 발송하는 것(전통적인 A/B 테스트)과 동일합니다.

- **예상 향상도:** 모든 사용자를 전체 최고 성능 경로로 보내는 대신 개인화된 경로를 사용함으로써 선택한 전환 이벤트에서의 개선도입니다.
- **전체 결과:** 전환 이벤트를 기반으로 한 두 번째 발송의 결과입니다.
- **예상 결과:** 우승 배리언트만 발송했을 경우 선택한 최적화 측정기준을 기반으로 한 두 번째 발송의 예상 결과입니다.

![Canvas의 개인화된 경로 탭. 카드에는 예상 향상도, 전체 전환(개인화된 경로 사용), 예상 고유 열람(우승 경로 사용)이 표시됩니다.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## 현지 시간 전달과 함께 개인화된 경로 사용 {#using-personalized-paths-with-local-time-delivery}

개인화된 경로가 있는 Canvas에서 현지 시간 전달을 사용하는 것은 권장하지 않습니다. 실험 기간은 첫 번째 사용자가 통과할 때 시작되기 때문입니다. 매우 이른 시간대에 있는 사용자가 단계에 진입하여 예상보다 훨씬 일찍 실험 기간의 시작을 트리거할 수 있으며, 이로 인해 일반적인 시간대에 있는 대부분의 사용자가 Canvas에 진입하고 전환할 충분한 시간을 갖기 전에 실험이 종료될 수 있습니다.

대안으로, 현지 시간 전달을 사용하려면 24-48시간 이상의 실험 기간을 사용하세요. 이렇게 하면 이른 시간대의 사용자가 Canvas에 진입하여 실험 시작을 트리거하더라도 실험 기간에 충분한 시간이 남습니다. 늦은 시간대의 사용자도 실험 기간이 만료되기 전에 Canvas와 개인화된 경로가 있는 실험 단계에 진입하고 전환할 충분한 시간을 가질 수 있습니다.