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

Canvas에 진입하려면 Canvas가 예약 기반이든, 행동 기반이든, API 트리거 기반이든 관계없이 진입 스케줄이 발생하기 전에 사용자가 진입 오디언스에 포함되어 있어야 합니다.

![사용자의 현지 시간 기준으로 2025년 4월 30일 오후 12시부터 2025년 5월 7일 오후 12시까지 구매를 수행하면 사용자를 진입시키는 행동 기반 Canvas]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Canvas가 시작된 후에 진입 오디언스 자격을 충족하는 사용자는 Canvas에 진입하지 않습니다.

{% alert tip %}
Canvas에 예약 기반, 행동 기반, 또는 API 트리거 전달 중 어떤 것을 사용할지에 대한 안내와 자세한 내용은 [진입 스케줄 유형]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)을 확인하세요!
{% endalert %}

### 진입 오디언스 필터 검토 {#review-entry-audience-filters}

일반적으로 행동 기반 또는 API 트리거 Canvas에서 오디언스 필터와 동일한 트리거를 설정하지 않는 것이 좋습니다. 예를 들어, Canvas가 시작된 후 특정 행동을 수행하는 사용자는 진입 오디언스에 포함되므로 해당 이벤트를 오디언스 필터로 추가할 필요가 없습니다.

오디언스를 타겟팅할 수 있는 세분화 필터에 대한 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.

### 여러 API 요청 일괄 처리 {#batch-multiple-api-requests}

사용자 프로필이 먼저 생성되거나 업데이트되었는지 확인하려면 여러 번 호출하는 대신 동일한 API 호출에서 요청하세요. 더 많은 예제는 [여러 엔드포인트 사용]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-2-using-multiple-api-endpoints)을 참조하세요.

### 지연 추가 {#add-a-delay}

경합 조건을 방지하는 또 다른 옵션은 Canvas의 첫 번째 단계로 지연 단계(이상적으로 5분으로 설정)를 사용하는 것입니다.

이렇게 하면 새 사용자 프로필에 속성, 이메일 주소, 푸시 토큰이 처리될 시간이 확보된 후 이후 캔버스 단계의 타겟이 됩니다. 이 지연 단계가 없으면 이메일이 아직 업데이트되지 않은 사용자에게 이메일이 전송될 수 있습니다.

## 전달 시간 {#delivery-times}

Canvas 전달 시간을 실시간으로 설정하면 인게이지먼트 및 전환율을 높일 수 있습니다. Canvas에 설정한 전달 시간을 확인하세요. 인게이지먼트와 전환율을 높이려면 예약된 반복 기반이 아닌 실시간으로 Canvas를 트리거하는 것이 가장 좋습니다.

Canvas에 예약 전달을 선택한 경우, Braze에서는 Canvas 조정이 가능하도록 출시 희망 시점보다 최소 24시간 전에 Canvas를 예약할 것을 권장합니다.

## 사용자 세분화 {#user-segments}

Canvas Flow 사용자 여정에 너무 많은 구성 요소를 추가하기 전에, 사용자 여정을 간단하게 유지할 수 있는 방법을 고려해 보세요. Canvas 편집기의 간소화된 보기를 사용하면 사용자 여정이 어떻게 분기되는지 더 잘 파악할 수 있습니다.

간단하고 효과적인 방식으로 사용자를 세분화하는 데 사용할 수 있는 네 가지 주요 구성 요소가 있습니다:

* [오디언스 경로](#audience-paths)
* [결정 분할](#decision-split)
* [행동 경로](#action-paths)
* [실험 경로](#experiment-paths)

### 오디언스 경로 {#audience-paths}

[오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 단계를 사용하면 커스텀 속성, 커스텀 이벤트, 고객 프로필의 이전 메시지 인게이지먼트 데이터를 기반으로 Canvas 내에서 사용자를 세분화할 수 있습니다.

### 결정 분할 {#decision-split}

[결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) 단계를 사용하면 예/아니오 질문에 대한 답변에 따라 사용자를 서로 다른 여정 경로로 보낼 수 있습니다.

### 행동 경로 {#action-paths}

[행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)는 커스텀 이벤트, 구매 이벤트, 커스텀 속성 변경과 같은 실시간 행동을 기반으로 사용자를 세분화하는 데 중점을 둡니다.

### 실험 경로 {#experiment-paths}

행동 경로와 마찬가지로, Canvas에서 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) 단계를 활용하여 여러 Canvas 경로를 대조군과 함께 서로 비교 테스트할 수 있습니다. 이를 통해 경로 성능을 추적하고, Canvas 여정을 구축할 때 정보에 기반한 결정을 내릴 수 있습니다.

## 출시 전 테스트 {#testing-before-launch}

Canvas의 세부 사항을 검토한 후, [테스트 Canvases 보내기]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases)에서 테스트 사용자를 활용하여 Canvas를 테스트할 수 있는 다양한 방법을 확인하세요.

## 출시 체크리스트 {#launch-checklist}

### 사용자 가용성 확인 {#check-user-availability}

- 사용자가 세분화 기준을 충족하는지 확인합니다.
- 구독 상태가 "subscribed" 또는 "opted-in"이며 푸시 토큰이 존재하는지 확인합니다. 이러한 조건을 Canvas 진입 규칙으로 추가한 경우, 사용자가 Canvas에 진입한 후 메시지 단계를 수신하기 전에 구독을 해지했을 수 있습니다.
- 사용자가 Canvas 전송 설정과 일치하는지 확인합니다. (사용자가 "subscribed"이지만 설정이 "Opted-in"으로 되어 있는 경우, 해당 채널이 활성화되지 않습니다.)
- Canvas에 글로벌 최대 게재빈도 설정이 활성화되어 있는 경우, 각 사용자가 특정 채널에서 메시지를 수신할 수 있는 횟수를 규칙이 제한하고 있지 않은지 확인합니다.
- 방해금지 시간이 활성화되어 있으면 메시지 전송 시간이 영향을 받을 수 있으며, 이 경우 메시지가 다음 가능한 시간(방해금지 시간 종료 시)에 전송되거나 완전히 취소될 수 있습니다.
- 캔버스 단계의 추가 필터에 대한 사용자 가용성을 확인합니다.

### 사전 필수 커스텀 이벤트 또는 구매 수행 여부 확인 {#confirm-that-they-performed-the-prerequisite-custom-event-or-purchase}

- 사용자가 동시에 여러 작업을 트리거할 때 수신하는 메시지에 영향을 미치는 경합 조건이 있는지 확인합니다.
- 해당 단계에 사용자가 메시지를 수신하지 못하도록 차단했을 수 있는 특정 필터가 없는지 확인합니다.
- 동일한 Canvas 내 서로 다른 단계 간의 충돌이 없는지 검색합니다. 예를 들어, 메시지를 수신하지 못한 사용자가 다른 브랜치에서 다른 단계의 완료를 요구하는 필터에 의해 중단되었을 수 있습니다.
- 사용자가 추가 유효성 검사 규칙을 충족하는지 확인합니다.
- 전송 시점에 캔버스 단계가 이전 단계에 연결되어 있었는지 확인합니다.

### Canvas가 올바르게 저장되고 모든 단계가 유효한지 확인 {#confirm-your-canvas-saves-correctly-and-all-steps-are-valid}

Canvas가 로드되지 않고 진행되지 않는 경우, 이전 버전의 Canvas가 올바르게 저장되지 않아 유효하지 않은 단계가 포함되어 있기 때문일 수 있습니다. 대시보드에서 Canvas를 복제할 수 있습니다. 문제가 지속되면 [지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 제출하세요.

## 문제 해결 {#troubleshooting}

{% details 사용자가 Canvas 메시지를 받지 못하는 이유는 무엇인가요? %}
**사용자 가용성 확인**
- 세분화 기준을 충족하는지 확인하세요.
- 푸시 가입 상태가 "subscribed" 또는 "opted-in"이고 **푸시 활성화** 상태가 "true"로 설정되어 있는지 확인하세요. 이러한 조건을 Canvas 진입 규칙으로 추가한 경우, 사용자가 Canvas에 진입한 후 메시지 단계를 받기 전에 가입을 해지했을 수 있습니다.
- Canvas 전송 설정과 일치하는지 확인하세요. (사용자가 "subscribed" 상태이지만 설정이 "Opted-in"으로 되어 있으면 해당 채널에 대해 활성화되지 않습니다.)
- Canvas에 글로벌 최대 게재빈도 설정이 활성화되어 있는 경우, 각 사용자가 특정 채널에서 메시지를 받을 수 있는 횟수를 규칙이 제한하고 있는지 확인하세요.
- 방해금지 시간이 활성화되어 있는 경우, 메시지 전송 시간에 영향을 받아 다음 가능한 시간(방해금지 시간 종료 후)에 전송되거나 완전히 취소될 수 있습니다.

**캔버스 단계의 추가 필터에 대한 사용자 가용성 확인**
- 사전 요건인 커스텀 이벤트 또는 구매를 수행했는지 확인하세요.
- 사용자가 동시에 여러 작업을 트리거할 때 수신하는 메시지에 영향을 미치는 [경합 조건]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)이 있는지 확인하세요.
- 해당 단계에 사용자가 메시지를 받지 못하게 차단할 수 있는 특정 필터가 없는지 확인하세요.
- 동일한 Canvas 내 서로 다른 단계 간의 충돌을 검색하세요. 예를 들어, 메시지를 받지 못한 사용자가 다른 브랜치의 또 다른 단계 완료를 요구하는 필터에 의해 중지되었을 수 있습니다.
- 사용자가 추가 유효성 검사 규칙을 충족하는지 확인하세요.
- 전송 시점에 캔버스 단계가 이전 단계에 연결되어 있었는지 확인하세요.
{% enddetails %}