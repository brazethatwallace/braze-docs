---
nav_title: 시작 전후 체크리스트
article_title: 시작 전후 체크리스트
page_order: 2
description: "이 문서에서는 Canvas를 시작하기 전과 후에 확인해야 할 사항에 대한 가이드라인을 제공합니다."
tool: Canvas

---

# 시작 전후 체크리스트 {#pre-and-post-launch-checklist}

> 이 문서에서는 Canvas를 시작하기 전과 후에 확인해야 할 사항에 대한 가이드라인을 제공합니다.

## 출시 전 고려 사항 {#things-to-consider-before-launch}

Canvas를 출시하기 전에 메시징과 발송 시간이 오디언스의 선호도에 맞게 설정되어 있는지 확인할 수 있는 여러 세부 사항이 있습니다. 시간대 차이, 진입 설정 등을 고려해야 합니다. 이 체크리스트를 가이드로 활용하여 사용 사례에 맞게 이러한 영역을 미세 조정하면 Canvas의 성공에 기여할 수 있습니다.

### 시간대 설정 검토 {#review-time-zone-settings}

예약된 진입 스케줄을 사용하여 사용자의 현지 시간대에 따라 진입시키는 경우, 사용자가 Canvas에 진입하기를 원하는 시간보다 최소 24시간 전에 Canvas를 출시해야 합니다. 예를 들어, 출시와 예약된 진입 시간 사이에 충분한 시간을 두지 않은 Canvas가 있습니다. 이 시나리오에서는 특정 시간대에서 예약된 진입 시간이 이미 지났기 때문에 Canvas에 진입하지 못하는 사용자가 있을 수 있습니다.

{% alert tip %}
충분한 버퍼를 예약하지 않은 경우 알림이 표시됩니다. 빠른 해결 방법은 발송 시간을 조정하여 사용자가 전체 24시간 동안 대상 Segment에 남아 있을 수 있도록 하는 것입니다.
{% endalert %}

![2025년 4월 30일 오전 10시에 사용자의 현지 시간으로 한 번에 진입하도록 예약된 Canvas.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### 오디언스 필터에 정규표현식 사용 고려 {#consider-using-regular-expressions-for-audience-filters}

사용자가 Canvas에 진입해야 하는 시기에 대한 기본 세부 사항을 설정한 후, Canvas 구축의 **대상 오디언스** 단계에서 Segments 또는 필터를 확인하는 것이 좋습니다. 이 단계에서 **대상 집단** 요약을 검토하여 대상 오디언스가 어떻게 설정되었는지 확인할 수도 있습니다.

여기에서 오디언스 경로 단계의 Segments 또는 필터, 메시지 및 결정 분할 단계의 전달 유효성 검사 설정에 정규표현식을 사용하는 것을 고려해 보세요. [정규표현식]({{site.baseurl}}/user_guide/audience/segments/regex)(정규식이라고도 함)은 문자열로, 패턴을 인식하고 대소문자와 같은 것 대신 문자를 고려합니다. 즉, "같음 / 같지 않음"을 사용하면 단순한 구문 오류 때문에 오디언스 규모가 제한될 수 있습니다.

대상 오디언스가 예상보다 작다면 "같음" 또는 "같지 않음" 대신 "정규식 일치" 또는 "정규식 불일치"를 사용해 보세요. 이를 통해 누락된 사용자를 포함하고 더 큰 오디언스를 타겟팅할 수 있습니다.

### 진입 설정 및 경합 조건 식별 {#identify-entry-settings-and-race-conditions}

**진입 스케줄**과 **대상 오디언스** 설정 모두에서 동일한 진입 기준을 사용한 경우 경합 조건이 발생할 수 있습니다.

액션 기반 진입을 사용하는 경우, 대상 오디언스에서 사용한 것과 동일한 트리거 동작을 여기에서 사용하지 않았는지 확인하세요. 사용자가 트리거 이벤트를 수행하는 시점에 오디언스에 포함되어 있지 않아 Canvas에 진입하지 못하는 경합 조건이 발생할 수 있습니다.

{% alert tip %}
오디언스 필터와 동일한 트리거로 액션 기반 Canvas를 설정할 때 이러한 경합 조건을 방지하기 위한 [모범 사례]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-3-matching-action-based-triggers-and-audience-filters)를 확인하세요.
{% endalert %}

### Canvas 항목 속성정보와 이벤트 속성정보 확인 {#check-canvas-entry-properties-and-event-properties}

이름은 비슷하지만, [Canvas 항목 속성정보와 이벤트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)는 Canvas 워크플로 내에서 다르게 작동합니다. Canvas 항목 속성정보는 진입 설정에 연결되며, Canvas 전체의 모든 메시지 컴포넌트에서 참조할 수 있습니다. Canvas 항목 속성정보는 액션 기반 또는 API 트리거 진입 설정을 사용하여 사용자의 Canvas 진입을 트리거하는 이벤트 또는 API 호출의 속성정보입니다.

반면에 이벤트 속성정보는 행동 경로 단계 다음의 첫 번째 메시지 단계에서만 참조할 수 있습니다. 이벤트 속성정보는 행동 경로 단계의 평가 기간 동안 사용자가 수행한 커스텀 이벤트 또는 구매 이벤트의 속성정보이며, 정의된 행동 경로 중 하나를 따라 진행하도록 트리거합니다.

Canvas 항목 속성정보 또는 이벤트 속성정보를 참조하는 메시지 단계에 대해 메시지 미리보기를 확인하세요.

### 사용자 진행에 대한 메시지 단계 검토 {#review-message-steps-for-user-advancement}

기본적으로 사용자는 메시지를 수신했는지 여부와 관계없이 모든 메시지 단계를 통해 진행합니다. 특정 메시지를 수신한 사용자만 진행시키려면 메시지 컴포넌트 바로 뒤에 결정 분할 단계를 추가하면 됩니다. 추가 필터로 "Canvas 단계에서 메시지 수신" 필터를 추가한 다음, Canvas와 메시지 단계를 선택합니다.

인앱 메시지가 포함된 메시지 단계의 경우, 결정 분할 컴포넌트 대신 행동 경로 컴포넌트를 사용하는 것이 좋습니다. 이렇게 하면 사용자가 인앱 메시지를 조회했는지 여부에 따라 진행시킬 수 있습니다. "단계와 상호작용" 필터를 추가하고 **인앱 메시지 보기**를 선택하여 액션 그룹을 정의합니다. 그런 다음 단계의 평가 기간을 인앱 메시지의 만료 기간으로 설정합니다.

멀티채널 메시징의 메시지 컴포넌트의 경우, 다음을 권장합니다:
* 메시지와 결정 분할 단계 사이에 지연 단계를 포함하고, 지연을 최소 5초로 설정합니다
* 컴포넌트에 Intelligent Timing이 포함된 경우, 지연을 24시간으로 설정합니다
* 컴포넌트에 사용량 제한조치가 포함된 경우, 메시지를 여러 개의 단일 채널 메시지 단계로 분할하고 서로 연결합니다. 그런 다음 마지막 메시지 단계 바로 뒤에 결정 분할 단계를 연결하여 사용자가 메시지를 수신했는지 확인합니다. 이 방법을 Intelligent Timing이 포함된 멀티채널 메시지 단계의 대안으로도 사용할 수 있습니다.

## 런칭 후 고려 사항 {#things-to-consider-after-launch}

Canvas를 런칭했습니다! 이제 무엇을 해야 할까요? 이 체크리스트를 사용하여 런칭 후 발생하는 불일치 상황에 따라 Canvas를 검토하고 조정하는 방법을 확인하세요.

### 진입은 많지만 발송이 적은 경우 {#many-entries-but-few-sends}

예를 들어, 발송된 메시지 수와 총 진입 수 사이에 차이가 있는 것을 발견했다고 가정해 보겠습니다. 다음 핵심 영역을 점검하여 Canvas를 조정할 부분을 파악할 수 있습니다.

#### 진입 오디언스 {#entry-audience}

예약 발송 Campaign을 사용하는 경우, 대상 집단을 검토하여 타겟 오디언스를 다시 확인하세요. 채널별 수치는 어떻게 보이며, Canvas에서 사용한 채널과 어떤 관련이 있나요? 가장 낮은 수치가 Canvas에서 사용한 채널과 일치한다면 문제를 찾은 것일 수 있습니다.

#### Canvas의 첫 번째 구성 요소 {#first-component-of-the-canvas}

Canvas의 시작 구성 요소에서 사용된 오디언스 필터, 트리거 동작 또는 Segments를 검토하세요. Canvas가 올바르게 시작되지 못하게 하는 오타나 지나치게 엄격한 조건이 있나요? "Matches Regex"를 사용해야 하는 곳에서 "Equals"를 사용하고 있지는 않나요?

#### Canvas 대조군 {#canvas-control-group}

배리언트와 대조군 간의 사용자 분포를 검토하세요. 대조군이 의도한 것보다 크나요? 그렇다면 이 설정을 편집할 수 있습니다. **BrazeAI<sup>TM</sup>로 최적화**가 켜져 있고 대조군이 이기고 있다면, Canvas를 중지하고 새로운 접근 방식을 시도하는 것을 고려하세요.

### 총 오디언스가 비어 있는 경우 {#an-empty-total-audience}

Canvas에 대한 진입 데이터가 전혀 보이지 않는다면, 사용자가 Canvas에 진입하지 않는 이유는 경합 조건과 제한적인 오디언스 세분화 필터 때문일 수 있습니다.

진입 스케줄에서 행동 기반 진입을 사용하는 경우, **대상 오디언스**에서 동일한 트리거 동작을 사용하지 않았는지 확인하세요. 사용자가 트리거 이벤트를 수행하는 시점에 오디언스에 포함되지 않는 경합 조건이 발생하여 Canvas에 진입하지 못할 수 있습니다.

또한, **대상 오디언스** 설정에서 **대상 집단** 표를 검토하여 선택한 Segment에 사용자가 있는지 확인하세요. 이 숫자가 낮은 경우, 진입 설정을 어떻게 조정할 수 있는지 살펴보거나 선택한 Segments 또는 필터에 오류가 없는지 검토하세요.

### 단계 간 예상치 못한 이탈 {#unexpected-drop-off-between-steps}

Canvas를 조정할 부분을 파악하는 또 다른 명확한 방법은 한 캔버스 단계에서 다음 단계로 넘어갈 때 큰 이탈이 발생하는 경우입니다. 이 경우 오디언스 필터와 예외 이벤트에 오타나 대소문자 오류가 없는지 확인하세요. 그리고 항상 그렇듯이, 오디언스 필터가 대다수의 사용자가 Canvas에 진입하는 것을 제외할 만큼 너무 엄격하지 않은지 확인하세요.

다음으로, 메시지가 사용자에게 전송되는 시기와 여부에 영향을 미칠 수 있는 다음 설정을 파악하는 것이 중요합니다:
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
- [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- 전달 유효성 검사

일반적으로 Canvas에서는 Intelligent Timing이나 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) 중 하나를 선택하세요. 둘 다 사용하지 마세요. Intelligent Timing이나 [사용량 제한조치]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) 중 하나를 사용하는 것도 마찬가지입니다. Intelligence Suite를 가장 효과적으로 활용하는 방법에 대한 자세한 내용은 [Intelligence Suite 사용 사례]({{site.baseurl}}/user_guide/brazeai/intelligence_suite#use-cases)를 참조하세요.

### 경로 간 의심스러운 발송량 {#suspicious-send-volumes-between-paths}

두 개 이상의 경로(오디언스 경로 또는 작업 경로) 간 발송량이 예상과 다른 경우, 이는 Segments, 필터 또는 트리거 동작을 점검할 기회가 될 수 있습니다. 또한, 겹치는 필터를 반드시 확인하고 제거하세요.