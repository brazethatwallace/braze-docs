---
nav_title: 모범 사례
article_title: Canvas 모범 사례
page_order: 1
description: "이 문서에서는 Canvas 및 Canvas Flow를 사용하여 사용자 여정을 생성하고 커스터마이징하기 위한 몇 가지 모범 사례를 제공합니다."
tool: Canvas

---

# Canvas 모범 사례 {#canvas-best-practices}

> 이 문서에서는 Canvas 및 Canvas Flow를 사용하여 사용자 여정을 생성하고 커스터마이징하기 위한 몇 가지 모범 사례를 제공합니다.

## 목적 파악하기 {#identify-your-purpose}

무엇을, 누구를, 왜에 대해 깊이 생각해 보세요!
- 사용자가 무엇을 달성하도록 도우려 하나요?
- 도달하려는 사용자는 누구인가요?
- 이 Canvas를 구축하는 이유는 무엇인가요?

## 조합하기 {#mix-and-match}

[캔버스 구성요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/)를 활용하여 새로운 사용자 여정 조합을 만들어 보세요.
- [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)로 사용자를 분류하고 다양한 워크플로를 구축하세요.
- [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/) 단계로 사용자 여정에 간격을 두세요.
- Canvas 플로우 내 원하는 곳 어디에나 [독립형 메시지]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)를 추가하세요.

{% alert note %}
캔버스 단계는 사용자를 플로우 내에서 앞으로만 이동시킬 수 있습니다. 이전 단계로 연결하도록 Canvas를 구성할 수 없으며, 이는 사용자를 뒤로 보내는 것이기 때문입니다. 이 유효성 검사를 통해 사용자가 Canvas 내에서 한 방향으로만 진행하도록 보장합니다.
{% endalert %}

## 더 풍부한 메시지 만들기 {#create-richer-messages}

더 풍부한 메시지로 사용자의 관심을 끌어보세요.

- 온보딩 Canvases에 [인앱 메시지]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)를 구축하여 첫인상을 최대한 활용하세요.
- Canvas 여정에 [Content Cards]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/)를 도입하여 프로모션 제안과 푸시 알림을 활용하세요.

## 사용자 여정 테스트하기 {#test-your-user-journeys}

대조군을 포함하여 Canvas 메시징의 영향을 측정하세요. 이를 통해 Canvas가 어떻게 수신되었는지 이해할 수 있습니다!

- Canvas의 각 단계에 이름을 지정하여 사용자 여정을 식별하세요.
- 사용자 여정에서 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) 구성요소를 활용하여 생성한 다양한 경로에 사용자를 무작위로 할당하세요.
- 지연 및 메시지 단계로 사용자 여정을 다양화하여 가장 효과적인 경로를 파악하세요.
- [Canvas 분석]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)을 확인하여 사용자 여정 내 각 구성요소의 성과를 살펴보세요.
- 초기 시작 후 [Canvas를 편집]({{site.baseurl}}/post-launch_edits/)하세요.

## Canvas 스케줄 설정 {#scheduling-your-canvases}

{% alert note %}
Canvas는 이미 지난 시간으로 예약 발송을 설정하는 것을 방지합니다. 그러나 Campaign이 스케줄된 것과 정확히 같은 분(또는 그 직전 몇 초)에 Canvas를 시작하는 것은 가능합니다. 이 경우 Canvas가 예약된 진입 시간을 놓쳐 사용자가 Canvas에 진입하지 못할 수 있습니다. 예약 발송 시간 몇 분 이내에 Campaign이 편집된 경우에는 Canvases를 즉시 발송하는 것을 권장합니다.
{% endalert %}

{% alert important %}
예약된 진입 또는 발송 기간에 가까운 시점에 오디언스, 스케줄 또는 전달 설정을 변경하면, 일부 사용자가 이미 단계에서 대기 중이거나 이전 설정으로 평가되었을 수 있으므로 모든 사용자에게 변경 사항이 반영된다고 보장할 수 없습니다. 스케줄 변경, 오디언스 변경, **대기열 추가 시 평가**, 메시지 단계 전달 타이밍이 어떻게 상호작용하는지 확인하려면 [시작 후 Canvas 변경]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/)을 참조하세요. 확실하지 않은 경우 Canvas를 중지하고, 복제한 후 다시 시작하여 깨끗하게 재평가하세요.
{% endalert %}

캔버스 단계의 경우, Canvas 스케줄을 설정할 때 다음 사항을 고려하세요:

- 스케줄 변경은 해당 단계를 수신하기 위해 아직 대기 중이지 않은 사용자에게만 적용됩니다.
- 오디언스 변경은 기본적으로 모든 사용자에게 적용되지만, 해당 단계를 수신하기 위해 대기 중이지 않은 사용자에게만 적용되도록 스케줄할 수도 있습니다.
- 배포 즉시 전달되도록 스케줄된 Canvas를 편집하고 **업데이트**를 선택하면 본질적으로 즉시 발송됩니다.

### 시작 후 편집 {#post-launch-edits}

저장되지 않은 초안이 있는 상태에서 활성 Canvas를 중지하면 해당 초안이 삭제될 수 있습니다. 진행 중인 편집 내용을 유지해야 하는 경우 중지하기 전에 초안을 저장, 시작 또는 삭제하세요.

#### 오디언스 평가 타이밍 {#audience-evaluation-timing}

Braze는 Canvas 빌더와 개별 단계에서 서로 다른 시점에 오디언스를 평가합니다. 설정에 대한 자세한 내용은 다음을 참조하세요:

- Canvas를 생성할 때 [타겟 진입 오디언스 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-13-set-your-target-entry-audience) 및 [Canvas 진입 스케줄 결정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule)
- [타겟 오디언스와 진입 기준이 함께 작동하는 방식]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/#how-target-audience-and-entry-criteria-work-together)
- 메시지 단계의 [전달 설정 편집]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#step-2-edit-delivery-settings)
- 오디언스 경로 단계의 [사용자 평가 방식]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/#how-users-are-evaluated)

예약된 진입 또는 발송 기간에 가까운 시점에 라이브 Canvas를 편집하면, **메시지** 단계에 이미 대기열에 추가된 사용자에게는 변경 사항이 적용되지 않을 수 있습니다. 자세한 내용은 [시작 후 Canvas 편집]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/)을 참조하세요.