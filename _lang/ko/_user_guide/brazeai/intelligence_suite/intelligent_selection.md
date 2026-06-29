---
nav_title: 지능형 선택
article_title: 지능형 선택
page_order: 1.0
description: "이 문서에서는 하루에 두 번 반복 Campaign 또는 Canvas의 성과를 분석하여 각 메시지 배리언트를 수신하는 사용자의 비율을 자동으로 조정하는 기능인 지능형 선택에 대해 설명합니다."
search_rank: 10
toc_headers: h2
---

# 지능형 선택 {#intelligent-selection}

> 지능형 선택은 하루에 두 번 반복되는 Campaign 또는 Canvas의 성과를 분석하여 각 메시지 배리언트를 수신하는 사용자의 비율을 자동으로 조정하는 기능입니다.

## 필수 조건 {#prerequisites}

{% tabs %}
{% tab Campaign %}
Campaign에 지능형 선택을 추가하기 전에 다음 사항이 올바르게 설정되어 있는지 확인하세요:

- Campaign이 반복 스케줄로 발송됩니다. 단일 발송 Campaign은 지원되지 않습니다.
- 최소 두 개의 메시지 배리언트를 추가했습니다.
- 배리언트 간 성과를 측정할 전환 이벤트를 정의했습니다.
- 재자격 기간이 24시간 이상으로 설정되어 있습니다. 더 짧은 기간은 대조군 배리언트의 무결성에 영향을 미칠 수 있으므로 지원되지 않습니다. 자세한 내용은 [이 FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection)를 참조하세요.
{% endtab %}

{% tab Canvas %}
Canvas에서 지능형 선택을 사용하려면 다음을 확인하세요:
- Canvas에 메시지 단계에서 최소 두 개의 메시지 배리언트가 포함되어 있습니다.
- 최소 하나의 전환 이벤트를 추가했습니다.
{% endtab %}
{% endtabs %}

## 지능형 선택 소개 {#about-intelligent-selection}

다른 배리언트보다 성과가 더 좋은 것으로 보이는 배리언트는 더 많은 사용자에게 발송되고, 성과가 저조한 배리언트는 더 적은 수의 사용자에게 타겟팅됩니다. 각 조정은 Braze가 단순한 우연이 아닌 실제 성과 차이에 따라 조정하고 있는지 확인하는 [통계 알고리즘](https://en.wikipedia.org/wiki/Multi-armed_bandit)을 사용하여 이루어집니다.

![지능형 선택이 활성화된 Campaign의 A/B 테스트 섹션.]({% image_buster /assets/img/intelligent_selection1.png %})

지능형 선택의 기능:
- 성과 데이터를 반복적으로 살펴보고 Campaign 트래픽을 점차적으로 위닝 배리언트로 전환합니다.
- 통계적 신뢰도를 유지하면서 더 많은 사용자가 가장 성과가 좋은 배리언트를 받을 수 있도록 합니다.
- 성과가 저조한 배리언트를 제외하고 [기존 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing/)보다 빠르게 고성과 배리언트를 식별합니다.
- 사용자가 최상의 메시지를 볼 수 있도록 더 자주, 더 높은 신뢰도로 테스트합니다.

지능형 선택은 두 번 이상 발송하는 Campaign에서 가장 잘 작동합니다. 최적화를 시작하려면 초기 성과 데이터가 필요하므로 단일 발송 Campaign에는 적합하지 않습니다. 이러한 Campaign의 경우 기존 [A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing/)를 사용하는 것을 권장합니다.


Campaign과 Canvases에 지능형 선택을 추가할 수 있습니다.

{% tabs %}
{% tab Campaign %}
지능형 선택은 Braze Campaign 작성기의 **타겟 오디언스** 단계에서 다중 발송 Campaign에 추가할 수 있습니다. 한 번만 발송하는 Campaign은 이 기능을 활용할 수 없습니다.

{% alert note %}
지능형 선택은 재자격 기간이 24시간 미만인 Campaign에서는 사용할 수 없습니다. 대조군 배리언트의 무결성에 영향을 미칠 수 있기 때문입니다. 자세한 내용은 [인텔리전스 FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection)를 참조하세요.
{% endalert %}
{% endtab %}

{% tab Canvas %}
Canvas에 최소 하나의 전환 이벤트와 두 개의 배리언트를 추가하세요. 그런 다음 빌드 단계에서 배리언트 비율 중 하나를 선택합니다.

![두 개의 배리언트가 있는 Canvas에서 각각 50%의 배리언트 분포로 설정하여 지능형 선택을 활성화할 수 있습니다.]({% image_buster /assets/img/intelligent_selection.png %})

이를 통해 배리언트 분포를 편집하고 지능형 선택을 켤 수 있습니다.

![Canvas에 대해 지능형 선택 옵션이 켜진 상태]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

아직 Canvas에 전환 이벤트를 추가하지 않았거나 Canvas가 단독 배리언트로 구성된 경우에는 지능형 선택을 사용할 수 없습니다.

{% alert note %}
Canvases는 재자격이 활성화된 상태에서 지능형 선택을 사용할 수 있지만, 최적 할당이 시간이 지남에 따라 변경되므로 Braze는 사용자가 재진입 시 동일한 배리언트를 받을 것이라고 보장할 수 없습니다. Campaign은 지능형 선택이 켜져 있을 때 24시간 이상의 재자격 기간이 필요합니다. 자세한 내용은 [지능형 선택과 결합할 때 24시간 미만의 재자격이 불가능한 이유는 무엇인가요?](#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection)를 참조하세요.
{% endalert %}
{% endtab %}
{% endtabs %}

## 실행 시간 {#run-time}

Campaign 및 Canvases의 경우, 지능형 선택은 배리언트의 "실제" 전환율에 대한 충분한 증거를 수집할 때까지 실행됩니다. "충분함"은 "후회(regret)"라는 특별한 측정기준에 의해 결정됩니다. 어떤 배리언트가 가장 적합한지 알 수 있는 충분한 데이터가 확보되면 지능형 선택이 자동으로 꺼진다는 점에서 신뢰도와 비슷하다고 생각하면 됩니다.

대부분의 경우 지능형 선택은 배리언트 중 하나를 위닝 배리언트로 선택합니다. 이 배리언트는 향후 발송 시 100%의 오디언스에게 제공됩니다.

{% alert note %}
지능형 선택은 확실한 위너를 하나도 선택하지 않고 최적화를 중단할 수 있습니다. 지능형 선택은 실험을 계속해도 전환율이 현재 전환율의 1% 이상 개선되지 않을 것이라는 95%의 확신이 들면 최적화를 중지합니다.
{% endalert %}

## 지능형 선택 배리언트 분포 {#intelligent-selection-variant-distribution}

지능형 선택은 Campaign 전환의 현재 상태를 기반으로 배리언트 분포를 결정합니다. 훈련 기간이 끝난 후에만 최종 분포를 결정합니다.

이는 Campaign의 초기 단계에서 99%와 1% 지능형 선택이 거의 동일한 발송을 받을 수 있지만, 배리언트 할당의 최종 비율은 99%–1%로 설정될 수 있음을 의미합니다.

Campaign의 초기 단계에서 지능형 선택이 50/50으로 발송되는 것을 원하지 않는 경우, 고정된 배리언트를 사용한 기존 A/B 테스트를 사용하는 것이 좋습니다.

## 자주 묻는 질문 {#faq}

### 지능형 선택과 결합할 때 24시간 미만의 재자격이 불가능한 이유는 무엇인가요? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection}

지능형 선택 Campaign에서 너무 짧은 기간의 재자격을 허용하지 않는 이유는 대조군 배리언트의 무결성에 영향을 미칠 수 있기 때문입니다. 24시간의 간격을 두면 알고리즘이 통계적으로 유효한 데이터셋으로 작업할 수 있도록 보장합니다.

일반적으로 재자격이 있는 Campaign은 사용자가 이전에 받은 것과 동일한 배리언트에 다시 진입하게 됩니다. 지능형 선택을 사용하면 이 기능의 최적 할당 측면으로 인해 배리언트 분포가 변경되었을 수 있으므로 Braze는 사용자가 동일한 캠페인 배리언트를 받을 것이라고 보장할 수 없습니다. 지능형 선택이 배리언트 성과를 재검토하기 전에 사용자가 다시 진입할 수 있도록 허용하면 재진입한 사용자로 인해 데이터가 왜곡될 수 있습니다.

예를 들어, Campaign이 다음 배리언트를 사용하는 경우:

- 배리언트 A: 20%
- 배리언트 B: 20%
- 대조군: 60%

두 번째 라운드에서 배리언트 분포는 다음과 같을 수 있습니다:

- 배리언트 A: 15%
- 배리언트 B: 25%
- 대조군: 60%

### Campaign 초기 단계에서 지능형 선택 배리언트가 동일한 발송량을 보이는 이유는 무엇인가요? {#why-are-my-intelligent-selection-variants-showing-equal-sends-during-the-early-stages-of-my-campaign}

지능형 선택은 Campaign 전환의 현재 상태를 기반으로 발송할 배리언트를 할당합니다. 훈련 기간 동안 배리언트 간에 균등하게 발송된 후에만 최종 배리언트 할당을 결정합니다. Campaign의 초기 단계에서 지능형 선택이 균등하게 발송되는 것을 원하지 않는 경우, 기존 A/B 테스트를 위해 고정된 배리언트를 사용하세요.

### 지능형 선택이 확실한 위너를 선택하지 않고 최적화를 중단하나요? {#will-intelligent-selection-stop-optimizing-without-picking-a-clear-winner}

지능형 선택은 실험을 계속해도 전환율이 현재 전환율의 1% 이상 개선되지 않을 것이라는 95%의 확신이 들면 최적화를 중지합니다.

### Canvas 또는 Campaign에서 지능형 선택을 활성화할 수 없는 이유는 무엇인가요(회색으로 표시됨)? {#why-cant-i-enable-intelligent-selection-in-my-canvas-or-campaign-grayed-out}

다음과 같은 경우 지능형 선택을 사용할 수 없습니다:

- Campaign 또는 Canvas에 전환 이벤트를 추가하지 않은 경우
- 단일 발송 Campaign을 생성하는 경우
- 24시간 미만의 기간으로 재자격을 활성화한 Campaign인 경우
- Canvas가 추가 배리언트나 대조군 없이 단일 배리언트로 구성된 경우
- Canvas가 배리언트 없이 단일 대조군으로 구성된 경우