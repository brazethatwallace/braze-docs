---
nav_title: 테스트 생성
article_title: 테스트 생성
page_order: 1
page_type: reference
description: "이 문서에서는 Braze를 사용하여 다변량 및 A/B 테스트를 생성하는 방법을 설명합니다."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/messaging/ab_testing/optimizations'
---

# 다변량 및 A/B 테스트 생성 {#creating-tests}

> 단일 채널을 타겟으로 하는 모든 Campaign에 대해 다변량 또는 A/B 테스트를 생성할 수 있습니다. 예를 들어, 푸시 Campaign에 다변량 또는 A/B 테스트를 사용하려면 동일한 Campaign에서 iOS와 Android 기기를 모두 타겟으로 지정할 수 있습니다.

!["캠페인 생성" 버튼을 선택하면 멀티채널 또는 단일 채널을 선택할 수 있는 드롭다운.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## 1단계: Campaign 생성 {#step-1-create-your-campaign}

1. **메시징** > **Campaigns**으로 이동합니다.
2. **캠페인 생성**을 선택하고 다변량 및 A/B 테스트를 허용하는 섹션에서 Campaign 채널을 선택합니다. 각 메시징 채널에 대한 자세한 설명서는 [캠페인 생성]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)을 참조하세요.

## 2단계: 배리언트 작성 {#step-2-compose-your-variants}

메시지의 배리언트를 최대 8개까지 생성할 수 있으며, 제목, 콘텐츠, 이미지 등을 다르게 설정할 수 있습니다. 메시지 간의 차이점 수에 따라 다변량 테스트인지 A/B 테스트인지가 결정됩니다. A/B 테스트는 하나의 변수를 변경했을 때의 효과를 검토하는 반면, 다변량 테스트는 두 개 이상의 변수를 검토합니다.

배리언트를 차별화하는 방법에 대한 아이디어는 [채널별 팁](#tips-different-channels)을 참조하세요.

![Campaign에서 "배리언트 추가"를 선택하는 화면.]({% image_buster /assets/img/ab_create_2.png %})

## 3단계: Campaign 스케줄 설정 {#step-3-schedule-your-campaign}

다변량 Campaign의 스케줄 설정은 다른 Braze Campaign의 스케줄 설정과 동일합니다. 모든 표준 [전달 유형]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/)을 사용할 수 있습니다.

다변량 테스트가 시작된 후에는 Campaign을 변경할 수 없습니다. 제목란이나 HTML 본문과 같은 매개변수를 변경하면 Braze는 실험이 손상된 것으로 간주하고 즉시 실험을 비활성화합니다.

{% alert important %}
[최적화]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/)(일부 채널에서 사용 가능)를 사용하려면 Campaign을 한 번만 전달하도록 스케줄을 설정하세요. 최적화는 반복 발송되거나 재적격성이 활성화된 Campaign에서는 사용할 수 없습니다.
{% endalert %}

## 4단계: Segment 선택 및 배리언트별 사용자 분배 {#step-4-choose-a-segment-and-distribute-your-users-across-variants}

타겟으로 할 Segment를 선택한 다음, 선택한 배리언트와 선택적 [대조군](#including-a-control-group)에 멤버를 분배합니다. 테스트할 Segment 선택에 대한 모범 사례는 [Segment 선택](#choosing-a-segment)을 참조하세요.

한 번만 발송하도록 스케줄된 푸시, 이메일, 웹훅 Campaign의 경우 [최적화]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/)를 사용할 수도 있습니다. 최적화는 타겟 오디언스의 일부를 A/B 테스트에서 보류하고, 첫 번째 테스트 결과를 기반으로 최적화된 두 번째 발송을 위해 해당 사용자를 유지합니다.

### 대조군 {#including-a-control-group}

타겟 오디언스의 일정 비율을 무작위 대조군으로 보류할 수 있습니다. 대조군의 사용자는 테스트를 수신하지 않지만, Braze는 Campaign 기간 동안 해당 사용자의 전환율을 모니터링합니다.

결과를 확인할 때, 배리언트의 전환율을 대조군이 제공하는 기준 전환율과 비교할 수 있습니다. 이를 통해 배리언트의 효과뿐만 아니라, 메시지를 전혀 보내지 않았을 때의 전환율과 비교하여 배리언트의 효과를 평가할 수 있습니다.

![대조군, 배리언트 1, 배리언트 2, 배리언트 3에 각각 25%씩 비율이 분배된 A/B 테스트 패널.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
*열기* 또는 *클릭*으로 우승 배리언트를 결정할 때 대조군을 사용하는 것은 권장되지 않습니다. 대조군은 메시지를 수신하지 않으므로 해당 사용자는 열기나 클릭을 수행할 수 없습니다. 따라서 해당 그룹의 전환율은 정의상 0%이며, 배리언트와의 의미 있는 비교가 되지 않습니다.
{% endalert %}

#### A/B 테스트에서의 대조군 {#control-groups-with-ab-testing}

A/B 테스트에서 사용량 제한을 사용하는 경우, 사용량 제한은 테스트 그룹과 동일한 방식으로 대조군에 적용되지 않으며, 이는 시간 편향의 잠재적 원인이 됩니다. 이 편향을 방지하려면 적절한 전환 기간을 사용하세요.

#### 지능형 선택에서의 대조군 {#control-groups-with-intelligent-selection}

[지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/)을 사용하는 Campaign의 대조군 크기는 배리언트 수에 따라 결정됩니다. 각 배리언트가 사용자의 20% 이상에게 발송되는 경우, 대조군은 20%이고 배리언트는 나머지 80%에서 균등하게 분배됩니다. 그러나 배리언트가 충분히 많아 각 배리언트가 사용자의 20% 미만에게 발송되는 경우, 대조군은 더 작아져야 합니다. 지능형 선택이 테스트 성과를 분석하기 시작하면, 대조군은 결과에 따라 커지거나 줄어듭니다.

## 5단계: 전환 이벤트 지정 (선택 사항) {#step-5-designate-a-conversion-event-optional}

Campaign에 전환 이벤트를 설정하면 해당 Campaign을 수신한 수신자 중 특정 행동을 수행한 사용자 수를 확인할 수 있습니다.

이는 이전 단계에서 **기본 전환율**을 선택한 경우에만 테스트에 영향을 미칩니다. 자세한 내용은 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)를 참조하세요.

## 6단계: 검토 및 시작 {#step-6-review-and-launch}

확인 페이지에서 다변량 Campaign의 세부 정보를 검토하고 테스트를 시작하세요! 다음으로 [테스트 결과 이해하기]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/)를 알아보세요.

## 알아두어야 할 사항 {#things-to-know}

실험이 이미 발송을 시작한 상태에서 메시지를 편집하면 실험이 무효화되고 모든 실험 결과가 제거됩니다.

- 예상되는 실험 동작에 대한 간섭을 방지하려면, 실험 Campaign 시작 후 1시간 이내에는 메시지를 편집하지 않는 것이 좋습니다.
- 실험이 완료된 후 발송 후에 메시지를 편집하면 실험 결과는 대시보드 분석에서 계속 확인할 수 있습니다. 그러나 Campaign을 다시 시작하면 실험 결과가 제거됩니다.

### 채널별 팁 {#tips-different-channels}

선택한 채널에 따라 메시지의 다양한 구성요소를 테스트할 수 있습니다. 예를 들어, 무엇을 테스트하고 무엇을 증명하고 싶은지에 대한 아이디어를 가지고 배리언트를 작성해 보세요. 어떤 요소를 조정할 수 있으며, 원하는 효과는 무엇인가요? 다변량 및 A/B 테스트로 조사할 수 있는 가능성은 수백만 가지이지만, 시작하는 데 도움이 될 몇 가지 제안을 드립니다:

| 채널 | 변경할 수 있는 메시지 요소 | 확인할 결과 |
| ---------------------| --------------- | ------------- |
| 푸시 | 문구 <br> 이미지 및 이모지 사용 <br> 딥링크  <br> 숫자 표현 (예: "3배" vs "200% 증가")  <br> 시간 표현 (예: "자정에 종료" vs "6시간 후 종료") | 열기  <br> 전환율 |
| 이메일 | 제목 <br> 표시 이름 <br> 인사말 <br> 본문 <br> 이미지 및 이모지 사용 <br> 숫자 표현 (예: "3배" vs "200% 증가") <br> 시간 표현 (예: "자정에 종료" vs "6시간 후 종료") | 열기  <br> 전환율 |
| 인앱 메시지 | "푸시"에 나열된 요소 <br> [인앱 메시지 이미지 사양]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#in-app-messages) | 클릭 <br> 전환율 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="채널별 팁" }

{% alert tip %}
A/B 테스트를 실행할 때, 각 배리언트가 전환 퍼널에 어떤 영향을 미쳤는지 이해할 수 있는 [퍼널 보고서]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/)를 생성하는 것을 잊지 마세요. 특히 비즈니스에서 "전환"이 여러 단계나 행동을 포함하는 경우에 유용합니다.
{% endalert %}

또한, 테스트의 이상적인 기간은 채널에 따라 달라질 수 있습니다. 대부분의 사용자가 각 채널에 참여하는 데 필요한 평균 시간을 고려하세요.

예를 들어, 푸시를 테스트하는 경우 사용자가 푸시를 즉시 확인하므로 이메일 테스트보다 더 빠르게 유의미한 결과를 얻을 수 있습니다. 이메일의 경우 사용자가 확인하거나 열기까지 며칠이 걸릴 수 있습니다. 인앱 메시지를 테스트하는 경우, 사용자가 Campaign을 보려면 앱을 열어야 하므로 가장 활발한 앱 사용자뿐만 아니라 일반적인 사용자로부터도 결과를 수집하기 위해 더 오래 기다려야 합니다.

테스트를 얼마나 오래 실행해야 할지 확실하지 않은 경우, [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/) 기능이 효율적으로 우승 배리언트를 찾는 데 유용할 수 있습니다.

### Segment 선택 {#choosing-a-segment}

사용자의 다양한 Segment가 메시징에 다르게 반응할 수 있으므로, 특정 메시지의 성공은 메시지 자체와 타겟 Segment 모두에 대해 시사하는 바가 있습니다. 따라서 타겟 Segment를 염두에 두고 테스트를 설계하세요.

예를 들어, 활성 사용자는 "이 혜택은 내일 만료됩니다!"와 "이 혜택은 24시간 후에 만료됩니다!"에 동일한 반응률을 보일 수 있지만, 일주일 동안 앱을 열지 않은 사용자는 더 큰 긴박감을 주는 후자의 문구에 더 반응할 수 있습니다.

또한, 테스트를 실행할 Segment를 선택할 때 해당 Segment의 크기가 테스트에 충분히 큰지 확인하세요. 일반적으로 배리언트가 많은 다변량 및 A/B 테스트는 통계적으로 유의미한 결과를 얻기 위해 더 큰 테스트 그룹이 필요합니다. 배리언트가 많을수록 각 개별 배리언트를 보는 사용자 수가 줄어들기 때문입니다.

{% alert tip %}
가이드로서, 테스트 결과에 대해 95% 신뢰도를 달성하려면 배리언트당(대조군 포함) 약 15,000명의 사용자가 필요합니다. 그러나 필요한 정확한 사용자 수는 특정 상황에 따라 이보다 많거나 적을 수 있습니다. 배리언트 표본 크기에 대한 보다 정확한 가이드는 [표본 크기 계산기](https://www.calculator.net/sample-size-calculator.html)를 참조하세요.
{% endalert %}

### 편향과 무작위화 {#bias-and-randomization}

대조군과 테스트 그룹 할당이 테스트에 편향을 도입할 수 있는지에 대한 질문이 자주 있습니다. 또한 이러한 할당이 진정으로 무작위인지 궁금해하는 경우도 있습니다.

사용자는 (무작위로 생성된) 사용자 ID와 (무작위로 생성된) Campaign 또는 Canvas ID를 연결하고, 해당 값의 100에 대한 나머지를 구한 다음, 대시보드에서 선택한 배리언트 및 선택적 대조군의 비율 할당에 해당하는 슬라이스로 사용자를 정렬하여 메시지 배리언트, 캔버스 배리언트 또는 해당 대조군에 할당됩니다. 따라서 특정 Campaign이나 Canvas를 생성하기 전의 사용자 행동이 배리언트와 대조군 간에 체계적으로 다를 수 있는 실질적인 방법은 없습니다. 또한 이 구현보다 더 무작위적(또는 더 정확히 말하면 의사 무작위적)으로 만드는 것도 실질적으로 불가능합니다.

#### 피해야 할 실수 {#mistakes-to-avoid}

오디언스가 올바르게 필터링되지 않은 경우 메시징 채널에 따른 차이가 있는 것처럼 보이는 몇 가지 일반적인 실수가 있습니다.

예를 들어, 대조군이 있는 넓은 오디언스에 푸시 메시지를 보내는 경우, 테스트 그룹은 푸시 토큰이 있는 사용자에게만 메시지를 보냅니다. 그러나 대조군에는 푸시 토큰이 있는 사용자와 없는 사용자가 모두 포함됩니다. 이 경우, Campaign 또는 Canvas의 초기 오디언스는 푸시 토큰 보유 여부로 필터링해야 합니다(`Foreground Push Enabled`가 `true`). 다른 채널에서 메시지를 수신할 자격에 대해서도 동일하게 적용해야 합니다: 수신 동의, 푸시 토큰 보유, 또는 가입됨.

대조군 배리언트에 Canvas 단계가 포함되지 않은 경우, 대조군 배리언트의 사용자에 대해서는 종료 기준 이벤트가 기록되지 않습니다.

{% alert note %}
대조군에 무작위 버킷 번호를 수동으로 사용하는 경우, 대조군에서 [주의해야 할 사항]({{site.baseurl}}/user_guide/audience/global_control_group/#things-to-watch-for)을 확인하세요.
{% endalert %}