---
nav_title: Canvas Flow로 시작하기
article_title: Canvas Flow로 시작하기
page_order: 3
description: "이 참조 문서에서는 Canvas Flow로 구축한 Canvas를 시작하기 전에 준비하고 테스트하는 방법을 다룹니다."
page_type: reference
tool: Canvas
---

# Canvas Flow로 시작하기 {#launch-with-canvas-flow}

> 이 참조 문서에서는 Canvas Flow를 사용하여 구축한 Canvas를 시작하기 전에 준비하고 테스트하는 방법을 다룹니다. 여기에는 Canvas 진입 조건, 오디언스 요약, 사용자 세그먼트 등 중요한 Canvas 체크포인트를 확인하는 방법이 포함됩니다.

Canvas를 시작할 준비를 할 때, Braze는 메시지 발송에 영향을 줄 수 있는 설정을 Canvas 빌더의 각 단계에서 확인할 것을 권장합니다. 여기에는 다음이 포함됩니다:
* [경합 조건](#race-conditions)
* [전달 시간](#delivery-times)
* [사용자 세그먼트](#segment-users)

## 경합 조건 {#race-conditions}

Canvas를 시작하기 전에 발생할 수 있는 [경합 조건]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)을 고려하세요.

Canvas에 진입하려면, Canvas가 스케줄 기반이든, 행동 기반이든, API 트리거 기반이든 관계없이 사용자가 진입 스케줄이 발생하기 전에 진입 오디언스에 포함되어 있어야 합니다.

![사용자의 현지 시간 기준으로 2025년 4월 30일 오후 12시부터 2025년 5월 7일 오후 12시까지 구매를 할 때 사용자를 진입시키는 행동 기반 Canvas.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Canvas가 시작된 후에 진입 오디언스 자격을 갖추게 된 사용자는 Canvas에 진입하지 않습니다.

{% alert tip %}
Canvas에 스케줄 기반, 행동 기반 또는 API 트리거 전달을 언제 사용해야 하는지에 대한 안내와 세부 정보는 [진입 스케줄 유형]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)을 확인하세요!
{% endalert %}

### 진입 오디언스 필터 검토 {#review-entry-audience-filters}

일반적으로 행동 기반 또는 API 트리거 Canvas에서 오디언스 필터와 동일한 트리거를 설정하는 것은 피하세요. 예를 들어, Canvas가 시작된 후 특정 행동을 수행한 사용자는 진입 오디언스에 포함되므로, 해당 이벤트를 오디언스 필터로 추가할 필요가 없습니다.

오디언스를 타겟팅하는 데 사용할 수 있는 세분화 필터에 대한 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.

### 여러 API 요청을 일괄 처리 {#batch-multiple-api-requests}

고객 프로필이 먼저 생성되거나 업데이트되었는지 확인하려면, 여러 번의 호출 대신 동일한 API 호출에서 요청을 수행하세요. 더 많은 예시는 [여러 엔드포인트 사용]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-2-using-multiple-api-endpoints)을 참조하세요.

### 지연 추가 {#add-a-delay}

경합 조건을 피하기 위한 또 다른 방법은 Canvas의 첫 번째 단계로 지연 단계(5분으로 설정하는 것이 이상적)를 사용하는 것입니다.

이렇게 하면 속성, 이메일 주소, 푸시 토큰이 새 고객 프로필에 처리된 후 다음 캔버스 단계의 타겟이 될 수 있는 시간이 확보됩니다. 이 지연 단계가 없으면, 이메일 주소가 아직 업데이트되지 않은 사용자에게 이메일이 발송될 수 있습니다.

## 전달 시간 {#delivery-times}

Canvas 전달 시간을 실시간으로 설정하면 인게이지먼트와 전환율을 높일 수 있습니다. Canvas에 설정한 전달 시간을 확인하세요. 인게이지먼트와 전환율을 높이려면, 스케줄 기반의 반복 발송보다 실시간으로 Canvas를 트리거하는 것이 좋습니다.

Canvas에 스케줄 전달을 선택한 경우, Braze는 Canvas를 시작하려는 시점보다 최소 24시간 전에 스케줄을 설정하여 조정할 여유를 두는 것을 권장합니다.

## 사용자 세그먼트 {#user-segments}

Canvas Flow 사용자 여정에 구성요소를 과도하게 추가하기 전에, 사용자 여정을 간단하게 유지할 수 있는 방법을 고려하세요. Canvas 편집기의 간소화된 보기를 사용하여 사용자 여정이 어떻게 분기되는지 더 잘 파악하세요.

사용자를 간단하고 효과적으로 세분화하는 데 사용할 수 있는 네 가지 주요 구성요소가 있습니다:

* [오디언스 경로](#audience-paths)
* [결정 분할](#decision-split)
* [행동 경로](#action-paths)
* [실험 경로](#experiment-paths)

### 오디언스 경로 {#audience-paths}

[오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 단계를 사용하여 고객 프로필의 커스텀 속성, 커스텀 이벤트, 이전 메시지 참여 데이터를 기반으로 Canvas 내에서 사용자를 세분화하세요.

### 결정 분할 {#decision-split}

[결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) 단계를 사용하면 양자택일 질문에 대한 답변을 기반으로 사용자를 서로 다른 사용자 여정 경로로 보낼 수 있습니다.

### 행동 경로 {#action-paths}

[행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)는 커스텀 이벤트, 구매 이벤트, 커스텀 속성 변경 등 실시간 동작을 기반으로 사용자를 세분화하는 데 중점을 둡니다.

### 실험 경로 {#experiment-paths}

행동 경로와 유사하게, Canvas에서 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) 단계를 활용하여 여러 Canvas 경로를 대조군과 함께 서로 비교 테스트할 수 있습니다. 이를 통해 경로 성과를 추적하여 Canvas 여정을 구축할 때 정보에 기반한 결정을 내릴 수 있습니다.

## 시작 전 테스트 {#testing-before-launch}

Canvas의 세부 사항을 검토한 후, 테스트 사용자를 사용하여 Canvas를 테스트할 수 있는 다양한 방법은 [테스트 Canvas 발송]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases)을 확인하세요.

## 시작 체크리스트 {#launch-checklist}

### 사용자 가용성 확인 {#check-user-availability}

- 사용자가 세분화 기준을 충족하는지 확인하세요.
- 가입 상태가 "subscribed" 또는 "opted-in"이고 푸시 토큰이 존재하는지 확인하세요. 이를 Canvas 진입 규칙으로 추가한 경우, 사용자가 Canvas에 진입한 후 메시지 단계를 수신하기 전에 구독을 취소했을 수 있습니다.
- Canvas 발송 설정과 일치하는지 확인하세요. (사용자가 "subscribed"이지만 설정이 "opted-in"인 경우, 사용자는 해당 채널에 대해 활성화되지 않습니다.)
- Canvas에 글로벌 최대 게재빈도 설정이 활성화된 경우, 규칙이 각 사용자가 특정 채널에서 메시지를 받을 수 있는 횟수를 제한하고 있는지 확인하세요.
- 방해금지 시간이 활성화된 경우, 메시지 발송 시간이 영향을 받을 수 있으며, 이는 메시지가 다음 가능한 시간(방해금지 시간이 끝날 때)에 발송되거나 완전히 취소될 수 있음을 의미합니다.
- 캔버스 단계의 추가 필터에 대한 사용자 가용성을 확인하세요.

### 사전 필수 커스텀 이벤트 또는 구매 수행 여부 확인 {#confirm-that-they-performed-the-prerequisite-custom-event-or-purchase}

- 사용자가 동시에 여러 행동을 트리거할 때 수신하는 메시지에 영향을 미치는 경합 조건이 있는지 확인하세요.
- 단계에 사용자가 메시지를 수신하지 못하게 차단할 수 있는 특정 필터가 없는지 확인하세요.
- 동일한 Canvas 내 서로 다른 단계 간의 충돌을 검색하세요. 예를 들어, 메시지를 수신하지 못한 사용자가 다른 분기의 다른 단계 완료를 요구하는 필터에 의해 중단되었을 수 있습니다.
- 사용자가 추가 유효성 검사 규칙을 충족하는지 확인하세요.
- 발송 시점에 캔버스 단계가 이전 단계에 연결되어 있었는지 확인하세요.

### Canvas가 올바르게 저장되고 모든 단계가 유효한지 확인 {#confirm-your-canvas-saves-correctly-and-all-steps-are-valid}

Canvas가 로드되지 않고 진행되지 않는 경우, 이전 버전의 Canvas가 제대로 저장되지 않아 유효하지 않은 단계가 포함되어 있을 수 있습니다. 대시보드에서 Canvas를 복제할 수 있습니다. 문제가 지속되면 [고객지원 티켓]({{site.baseurl}}/braze_support)을 열어주세요.

## 문제 해결 {#troubleshooting}

{% details 사용자가 Canvas 메시지를 수신하지 못하는 이유는 무엇인가요? %}
**사용자 가용성 확인**
- 세분화 기준을 충족하는지 확인하세요.
- 푸시 가입 상태가 "subscribed" 또는 "opted-in"이고 **푸시 활성화** 상태가 "true"로 설정되어 있는지 확인하세요. 이를 Canvas 진입 규칙으로 추가한 경우, 사용자가 Canvas에 진입한 후 메시지 단계를 수신하기 전에 구독을 취소했을 수 있습니다.
- Canvas 발송 설정과 일치하는지 확인하세요. (사용자가 "subscribed"이지만 설정이 "opted-in"인 경우, 사용자는 해당 채널에 대해 활성화되지 않습니다.)
- Canvas에 글로벌 최대 게재빈도 설정이 활성화된 경우, 규칙이 각 사용자가 특정 채널에서 메시지를 받을 수 있는 횟수를 제한하고 있는지 확인하세요.
- 방해금지 시간이 활성화된 경우, 메시지 발송 시간이 영향을 받을 수 있으며, 이는 메시지가 다음 가능한 시간(방해금지 시간이 끝날 때)에 발송되거나 완전히 취소될 수 있음을 의미합니다.

**캔버스 단계의 추가 필터에 대한 사용자 가용성 확인**
- 사전 필수 커스텀 이벤트 또는 구매를 수행했는지 확인하세요.
- 사용자가 동시에 여러 행동을 트리거할 때 수신하는 메시지에 영향을 미치는 [경합 조건]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)이 있는지 확인하세요.
- 단계에 사용자가 메시지를 수신하지 못하게 차단할 수 있는 특정 필터가 없는지 확인하세요.
- 동일한 Canvas 내 서로 다른 단계 간의 충돌을 검색하세요. 예를 들어, 메시지를 수신하지 못한 사용자가 다른 분기의 다른 단계 완료를 요구하는 필터에 의해 중단되었을 수 있습니다.
- 사용자가 추가 유효성 검사 규칙을 충족하는지 확인하세요.
- 발송 시점에 캔버스 단계가 이전 단계에 연결되어 있었는지 확인하세요.
{% enddetails %}