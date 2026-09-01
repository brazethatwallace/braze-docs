---
nav_title: FAQ
article_title: Canvas FAQ
page_order: 8
alias: "/canvas_v2_101/"
description: "이 문서에서는 Canvas에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
tool: Canvas
toc_headers: h2

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 Canvas에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## Canvas 빌드 및 편집 {#building-and-editing-canvas}

### Canvas에 포함할 수 있는 단계는 몇 개인가요? {#how-many-steps-i-can-include-in-a-canvas}

Canvas에는 최대 200개의 단계를 추가할 수 있습니다.

### Canvas 항목 속성정보에 크기 제한이 있나요? {#are-there-size-limits-for-canvas-entry-properties}

네. [Canvas 컨텍스트 오브젝트]({{site.baseurl}}/api/objects_filters/context_object)(Canvas 항목 속성정보)의 최대 크기는 50&nbsp;KB입니다. 이 제한 내에서 페이로드를 가능한 한 작게 유지하세요. Canvas에서 항목 및 이벤트 속성정보가 작동하는 방식에 대해서는 [컨텍스트 및 이벤트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)를 참조하세요.

### "Too many Canvas branches" 오류가 표시되는 이유는 무엇인가요? {#why-do-i-see-a-too-many-canvas-branches-error}

이 오류는 단계 분기와 진입 오디언스 크기의 조합이 클러스터 성능 문제를 일으켜 메시지 전송이 방해될 수 있을 때 나타납니다. 해결 단계(예: [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 사용, 분기 또는 오디언스 크기 줄이기, Canvas Flow에서 재구축)는 ["Too many Canvas branches" 오류]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error)를 참조하세요.

### Canvas에서 재자격과 함께 BrazeAI<sup>TM</sup>로 최적화를 사용할 수 있나요? {#can-i-use-optimize-with-brazeai-with-re-eligibility-in-a-canvas}

네. Canvas에서 재자격이 활성화된 경우 [BrazeAI<sup>TM</sup>로 최적화]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai)를 사용할 수 있습니다. Braze는 할당이 시간이 지남에 따라 변동하므로 재진입 시 동일한 배리언트를 보장할 수 없습니다. Campaigns에서는 **BrazeAI<sup>TM</sup>로 최적화**가 활성화된 경우 재자격 기간이 24시간 이상이어야 합니다.

### 컴포넌트와 단계의 차이점은 무엇인가요? {#whats-the-difference-between-a-component-and-a-step}

[컴포넌트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)는 Canvas의 효과를 판단하는 데 사용할 수 있는 Canvas의 개별 구성 요소입니다. 컴포넌트에는 사용자 여정 분할, 지연 추가, 여러 Canvas 경로 테스트 등의 동작이 포함될 수 있습니다. Canvas의 단계는 Canvas 분기에서의 개인화된 사용자 여정을 의미합니다. 기본적으로, Canvas는 사용자 여정의 단계를 구성하는 개별 컴포넌트로 이루어져 있습니다.

### 연결이 끊어진 단계가 있는 Canvas를 실행할 수 있나요? {#can-i-launch-a-canvas-with-disconnected-steps}

네. 실행 후에도 연결이 끊어진 단계가 있는 Canvases를 저장할 수 있습니다.

### 사용자가 연결이 끊어진 단계에 도달하면 어떻게 되나요? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

사용자가 Canvas 워크플로의 연결이 끊어진 단계에 있는 경우, 후속 단계가 있으면 해당 단계로 진행하며, 단계 설정에 따라 사용자의 진행 방식이 결정됩니다. 이는 사용자가 나머지 Canvas에 직접 연결하지 않고도 단계를 변경할 수 있도록 하기 위한 것입니다. 또한 즉시 실행하기 전에 테스트할 여유를 제공하여 사실상 초안 저장이 가능합니다.

단계를 연결 해제하기 전에 Canvas 단계에서 대기 중인 사용자에 대한 분석 뷰를 확인하는 것을 권장합니다.

### 하나의 배리언트에 여러 분기가 있는 Canvas에서 오디언스와 전송 시간이 동일하면 어떻게 되나요? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

각 단계에 대해 작업이 대기줄에 추가됩니다. 거의 동시에 실행되며, 그중 하나가 "선택"됩니다. 실제로는 어느 정도 균등하게 분배될 수 있지만, 먼저 생성된 단계 쪽으로 약간의 편향이 있을 가능성이 높습니다.

또한, 이 분배가 정확히 어떻게 이루어질지에 대해서는 보장할 수 없습니다. 균등한 분할을 원하시면 [무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) 필터를 추가하세요.

### Canvas 오디언스는 어떻게 평가되나요? {#how-are-canvas-audiences-evaluated}

기본적으로, Canvas 전체 단계의 필터와 Segments는 전송 시점에 확인됩니다. 결정 분할 단계는 이전 단계를 수신한 직후(또는 지연 전)에 평가를 수행합니다.

### 예외 이벤트는 언제 트리거되나요? {#when-does-an-exception-event-trigger}

예외 이벤트는 사용자가 연결된 Canvas 컴포넌트를 수신하기 위해 대기하는 동안에만 트리거됩니다. 사용자가 미리 동작을 수행한 경우 예외 이벤트가 트리거되지 않습니다. 특정 이벤트를 미리 수행한 사용자를 제외하려면 [필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 대신 사용하세요.

### Canvas를 편집하면 이미 Canvas에 있는 사용자에게 어떤 영향을 미치나요? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

다단계 Canvas의 일부 단계를 편집하면, 이미 오디언스에 있지만 아직 해당 단계를 수신하지 않은 사용자는 업데이트된 버전의 메시지를 수신합니다. 단, 이는 해당 단계에 대해 아직 평가되지 않은 경우에만 해당됩니다.

실행 후 편집할 수 있는 내용에 대한 자세한 정보는 [실행 후 Canvas 변경]({{site.baseurl}}/post-launch_edits)을 참조하세요.

### Canvas를 중지하면 어떻게 되나요? {#what-happens-when-you-stop-a-canvas}

Canvas를 중지하면 다음이 적용됩니다:

- 사용자가 Canvas에 진입하지 못하게 됩니다.
- 사용자가 흐름의 어디에 있든 더 이상 메시지가 전송되지 않습니다.
- **예외:** 이메일이 포함된 Canvases는 즉시 중지되지 않습니다. 전송 요청이 SendGrid로 전달된 후에는 사용자에게 전달되는 것을 막을 수 없습니다.

### 하나의 Canvas를 구축해야 하나요, 아니면 사용자 라이프사이클 단계별로 별도의 Canvases를 구축해야 하나요? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Canvas로 달성하고자 하는 목표에 따라 사용자 여정을 구축하는 접근 방식이 달라질 수 있습니다. Canvas의 유연성을 통해 사용자 라이프사이클의 모든 단계에 대한 사용자 여정을 설계할 수 있습니다. 효과적인 사용자 여정을 만들기 위한 다양한 간소화된 접근 방식의 예시는 [Braze Canvas 템플릿]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)을 확인해 보세요.

## 메시지 및 전달 {#messages-and-delivery}

### Canvas에서 인앱 메시지는 언제 전송되나요? {#when-are-in-app-messages-in-canvas-sent}

인앱 메시지는 다음 세션 시작 시 전송됩니다. 즉, 사용자가 Canvas가 중지되기 전에 Canvas 단계에 진입했다면, 인앱 메시지가 아직 만료되지 않은 한 다음 세션 시작 시 해당 인앱 메시지를 수신합니다.

사용자가 Canvas가 중지되기 전에 세션을 시작했지만 인앱 메시지가 즉시 표시되지 않을 수도 있습니다. 이는 인앱 메시지가 커스텀 이벤트에 의해 트리거되거나 지연된 경우에 발생할 수 있습니다. 따라서 Canvas가 중지된 후에도 사용자가 인앱 메시지 노출을 기록하고 인앱 메시지를 "수신"할 수 있습니다. 다만 사용자는 Canvas가 중지되기 전에 세션을 시작했어야 하며, 캔버스 단계를 수신한 **이후**여야 합니다.

{% alert note %}
Canvas를 중지해도 메시지를 기다리고 있는 사용자가 사용자 여정에서 퇴장하지는 않습니다. Canvas를 다시 활성화하고 사용자가 여전히 메시지를 기다리고 있다면 해당 메시지를 수신합니다(메시지가 전송되었어야 할 시간이 이미 지난 경우에는 수신하지 않습니다).
{% endalert %}

### Canvas에서 노출 횟수가 기록되었는데도 전송 수가 0으로 표시되는 이유는 무엇인가요? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

인앱 메시지 단계가 포함된 Canvas에서 _전송된 메시지_가 항상 0이라면, 이는 인앱 메시지 전달 방식이 다른 메시징 채널과 다르기 때문입니다.

인앱 메시지는 Braze에서 "푸시"되는 것이 아니라 SDK에 의해 "풀"됩니다. 적격 사용자를 위한 인앱 메시지는 세션 시작 시 자동으로 전달되며 트리거 이벤트가 발생할 때까지 "대기"합니다. 적격 사용자가 세션을 시작할 때 메시지를 수신하므로 Braze는 이를 전송 이벤트로 보고하지 않습니다. 사용자가 트리거 이벤트를 수행하면 메시지가 표시되고 Braze는 노출을 기록하며 고객 프로필에서 해당 캔버스 단계(또는 Campaign)를 수신됨으로 표시합니다. 따라서 인앱 메시지의 _전송_ 합계는 0입니다.

### 긴 지연이나 분기 이후 사용자가 인앱 메시지를 수신하지 못한 이유는 무엇인가요? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

업스트림 [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) 단계 및 오디언스 확인이 완료된 후, 사용자는 메시지 단계에 도달해야만 인앱 메시지를 받을 수 있습니다. 메시지가 캘린더 날짜 또는 짧은 **단계가 제공된 후 기간** 기준으로 만료되는 경우, 느린 분기의 사용자는 만료 후에 도착하여 메시지를 볼 수 없게 됩니다. 만료 시간을 가장 긴 현실적인 경로 지연과 맞추세요. 자세한 내용과 예시는 [인앱 메시지 만료]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration)를 참조하세요.

### "Canvas Entry Properties may not be used in In-App Messages."라는 메시지가 표시되는 이유는 무엇인가요? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

이 메시지는 개인화가 인앱 메시지가 Canvas에서 해석할 수 없는 필드를 참조할 때 나타납니다. [컨텍스트 및 이벤트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) 및 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)에 설명된 대로 `context` 오브젝트를 사용하세요. 레거시 Liquid 네임스페이스 `canvas_entry_properties`는 `context`와 다른 제약 조건을 가지고 있습니다. 여러 단계에 걸쳐 값을 유지해야 하는 경우, Braze 팀과 함께 [오리지널 Canvas 편집기의 영구 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)를 검토하세요. 저장된 값은 기기가 인앱 페이로드를 다운로드하기 전에 사용자가 Canvas를 퇴장하면 삭제됩니다.

### Canvas에서 드래그 앤 드롭 인앱 메시지의 버튼 클릭은 어디에서 확인할 수 있나요? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

드래그 앤 드롭 인앱 메시지의 버튼 수준 측정기준은 Canvas 요약이 아닌 **Canvas 세부 정보**의 **메시지** 단계 분석 카드에 표시됩니다. Canvas를 열고 메시지 단계를 선택한 다음 해당 위치에서 인앱 인게이지먼트를 확인하세요. 리포팅 개념에 대해서는 [Canvas 분석으로 측정 및 테스트]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)를 참조하세요.

### 같은 Canvas 메시지 단계나 다변량 전송에서 각 배리언트에 대해 다른 전송 시간을 예약할 수 있나요? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

아니요. 같은 다변량 구성이나 메시지 단계의 배리언트는 하나의 전달 스케줄을 공유합니다. 같은 예약된 전송에서 한 배리언트를 오후 6시에, 다른 배리언트를 오후 7시에 보내도록 지정할 수 없습니다.

전송을 분산하거나 경로별로 다른 시간을 사용하려면 다음 방법을 시도하세요:

- 별도의 메시지 단계 사이에 지연 단계를 배치하여 각 메시지가 자체 스케줄을 갖도록 합니다.
- 분기 또는 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) 단계를 사용하여 사용자가 다른 타이밍의 경로를 따르도록 합니다.
- 사용 사례가 하나의 Canvas 안에 있을 필요가 없다면 별도의 Campaign으로 분리합니다.

Campaign에서의 다변량 및 A/B 개념에 대해서는 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

### Canvas 메시지 단계에서 사용자가 글로벌 최대 게재빈도 설정에 걸리면 어떻게 되나요? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

해당 채널의 전송은 수신하지 못하지만, 글로벌 최대 게재빈도 설정으로 인해 메시지가 전송되지 않은 경우에도 메시지 단계는 사용자를 계속 진행시킵니다. 단계별 진행 사례에 대해서는 [사용자 진행 방식]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance)을 참조하세요. 글로벌 최대 게재빈도 설정만으로는 사용자가 Canvas에서 퇴장하지 않습니다. 이 동작은 메시지 단계의 **전달 유효성 검사**와 별개입니다. 자세한 내용은 [사용량 제한조치 및 최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)을 참조하세요.

### 전송 수가 예상 오디언스 크기보다 낮은 이유는 무엇인가요? {#why-are-sends-lower-than-the-estimated-audience-size}

전송 수는 최대 게재빈도 설정, 엄격한 기기 또는 브라우저 필터, 재적격 기간, 사용량 제한조치, 채널 수준 제외(예: 푸시 도달 가능성 또는 이메일 구독 및 전달 가능성 확인) 등 [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)과 동일한 여러 이유로 **예상 오디언스**보다 낮을 수 있습니다.

Canvas 고유 요인도 적용됩니다:

- **실행 기반 또는 API 트리거 진입:** 사용자는 진입 행동을 수행한 후에만 진입(및 단계 수신)하므로, 해당 행동이 발생할 때까지 실제 전송은 사전 추정치에 뒤처집니다.
- **오디언스 경로:** 사용자는 자격이 있는 가장 높은 우선순위의 분기로 라우팅되므로, 하위 분기는 단순 Segment 수가 시사하는 것보다 적은 사용자를 받을 수 있습니다.
- **오디언스 및 전송 시간 확인:** 전체 단계는 별도로 구성하지 않는 한 전송 시점에 필터를 다시 평가합니다. Canvas가 구축될 때 적격했던 사용자가 메시지 전송 전에 탈락할 수 있습니다.
- **대조군:** 글로벌 또는 Canvas 대조군은 진입자의 일부를 메시징에서 제외합니다.
- **방해금지 시간 및 지연:** 메시지가 보류되거나 재예약되어 확인 중인 리포팅 기간 밖으로 전송이 이동할 수 있습니다.
- **최대 진입 또는 오디언스 한도:** 기본 Segment가 더 크더라도 진입 또는 전송 한도가 추가 사용자를 중지시킵니다.
- **리포팅 기간:** 분석 범위가 추정치와 비교하는 모든 전송을 포함하지 않을 수 있습니다.

### 예상 오디언스와 Canvas 사용자 수가 일치하지 않는 이유는 무엇인가요? {#why-dont-estimated-audience-and-canvas-user-counts-match}

**예상 오디언스**는 추정이 실행될 때 Segment 및 진입 필터와 일치하는 사용자를 반영합니다. 그 시점 이후 지연 또는 실행 기반 진입, 재적격, API 트리거 또는 분기 라우팅으로 인해 스냅샷보다 더 많은 프로필이 여정에 접촉할 수 있습니다. 또한 전송 시간 필터가 실패하면 사용자가 탈락하여 실제 진입 또는 전송이 줄어들 수 있습니다. 타이밍, 한도 및 평가 설정을 [전송 수가 예상 오디언스 크기보다 낮은 이유는 무엇인가요?](#why-are-sends-lower-than-the-estimated-audience-size)와 함께 비교하세요.

### _고유 수신자_가 타겟팅한 사용자 수보다 높은 이유는 무엇인가요? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_고유 수신자_가 예상보다 높을 수 있는 이유는 Braze가 Canvas 및 Campaign 리포팅에서 **일별 고유 수신자**를 추적하기 때문입니다. 이를 통해 사용자가 여정에서 메시지를 수신할 때마다 정확한 전환 기여도 분석을 지원합니다.

예를 들어, 사용자가 월요일에 캔버스 단계를 수신하고 금요일에 다시 수신하여 각 전송 후 전환한 경우, Braze는 두 개의 수신자 행과 두 개의 범위 내 전환을 카운트할 수 있습니다. 반복 진입 또는 재적격을 사용하면 동일한 소규모 프로필 집합이 여러 일에 걸쳐 여러 _고유 수신자_를 생성할 수 있습니다.

### Canvas의 전송률이 낮아지는 이유는 무엇인가요? {#why-is-my-canvas-experiencing-lower-send-rates}

일일 예약 Canvas의 전송 사용자 수가 시간이 지남에 따라 줄어든다면 다음을 확인하세요:

- **재적격이 활성화되어 있는지 확인:** 재적격이 없으면 Braze는 각 사용자를 Canvas에 한 번만 진입시킵니다. 일일 예약 Canvases에서는 오디언스와 일치하고 아직 Canvas에 진입하지 않은 사용자만 각 진입에 적격합니다. 더 많은 사용자가 진입할수록 이후 진입에는 적격 사용자가 줄어들므로 진입 규모가 감소합니다.
- **오디언스가 고정된 멤버십을 가지고 있는지 확인:** 고정된 사용자 목록(예: Segment 필터로 사용된 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import))으로 구축된 오디언스는 자동으로 새 멤버를 얻지 않습니다. 새 진입자가 없으면 사용자가 Canvas에 진입함에 따라 진입 규모가 회복될 수 없습니다.

[전달 속도 사용량 제한조치]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) 및 단일 발생의 전송을 줄이는 기타 요인에 대해서는 [전송 수가 예상 오디언스 크기보다 낮은 이유는 무엇인가요?](#why-are-sends-lower-than-the-estimated-audience-size)를 참조하세요.

### 소규모 대조군 Segment에서 과거 멤버십 변동이 표시되는 이유는 무엇인가요? {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

과거 멤버십 차트는 추정 샘플을 사용하므로, [글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/audience/global_control_group) Segment를 포함한 소규모 Segment는 기본 오디언스가 안정적이더라도 일별 변동을 보일 수 있습니다. 추정 방식과 차트가 변동할 수 있는 이유에 대해서는 [과거 Segment 멤버십 크기 보기]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size)를 참조하세요.

## 분석 및 전환 {#analytics-and-conversions}

### 전환 대시보드는 Canvas 전환을 어떻게 기여도 분석하나요? {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

[전환 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/conversions)는 선택한 [기여도 분석 방법]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods)(예: **수신 시**, **발송 시**, **열람 시**, **클릭 시**)에 따라 Canvas 전환을 기여도 분석합니다. 보고서에 사용자가 표시되려면 해당 사용자가 Canvas 또는 Campaign에 진입하고, 선택한 기여도 분석 방법을 기록하고, 보고서 설정 내에서 전환 이벤트를 수행해야 합니다.

Canvas 분석에서 단계 수준 및 배리언트 수준 전환 규칙에 대해서는 [Canvas에서 사용자 전환은 어떻게 추적되나요?](#how-are-user-conversions-tracked-in-a-canvas)를 참조하세요.

### Canvas에서 사용자 전환은 어떻게 추적되나요? {#how-are-user-conversions-tracked-in-a-canvas}

사용자는 Canvas 진입당 한 번만 전환할 수 있습니다. 전환은 해당 진입에 대해 사용자가 가장 최근에 수신한 메시지에 할당됩니다. Canvas 시작 부분의 요약 블록은 메시지 수신 여부와 관계없이 해당 경로 내에서 사용자가 수행한 모든 전환을 반영합니다. 이후 각 단계는 해당 단계가 사용자가 수신한 가장 최근 단계였을 때 발생한 전환만 표시합니다.

{% alert note %}
사용자가 Canvas에 재진입하면 전환 이벤트는 가장 최근 진입에 대해서만 추적됩니다. 전환 이벤트가 백필되더라도 이전 진입에 대해서는 전환 이벤트가 기록되지 않습니다.
{% endalert %}

{% details 예시를 확인하려면 펼치세요 %}

**예시 1**

10개의 푸시 알림이 포함된 Canvas 경로가 있고 전환 이벤트가 "세션 시작"("앱 열기")인 경우:

- 사용자 A는 진입 후 첫 번째 메시지를 수신하기 전에 앱을 열었습니다.
- 사용자 B는 각 푸시 알림 후에 앱을 열었습니다.

**결과:** 요약에는 2건의 전환이 표시되고, 개별 단계에서는 첫 번째 단계에서 1건의 전환이, 이후 모든 단계에서는 0건의 전환이 표시됩니다.

{% alert note %}
전환 이벤트가 발생할 때 방해금지 시간이 활성화되어 있어도 동일한 규칙이 적용됩니다.
{% endalert %}

**예시 2**

방해금지 시간이 활성화된 단일 단계 Canvas가 있는 경우:

1. 사용자가 Canvas에 진입합니다.
2. 첫 번째 단계에 지연이 없지만 설정된 방해금지 시간 내에 있으므로 메시지가 억제됩니다.
3. 사용자가 전환 이벤트를 수행합니다.

**결과:** 사용자는 전체 Canvas 배리언트에서 전환으로 집계되지만, 해당 단계를 수신하지 않았으므로 단계에서는 전환으로 집계되지 않습니다.

{% enddetails %}

### 각 전환율 유형의 차이점은 무엇인가요? {#whats-the-difference-between-the-different-conversion-rate-types}

- 총 Canvas 전환은 전환 이벤트를 완료한 고유 사용자 수를 반영하며, 각 사용자가 완료한 전환 횟수를 반영하지 않습니다.
- 배리언트 전환율 또는 Canvas 시작 부분의 요약 블록은 메시지 수신 여부와 관계없이 해당 경로 내에서 사용자가 수행한 모든 전환을 총합으로 반영합니다.
- 단계 전환율은 해당 메시지 단계를 수신하고 설정된 전환 이벤트 중 하나를 완료한 사람 수를 반영합니다.

### Canvas 단계 전환율이 Canvas 배리언트 총 전환율과 같지 않은 이유는 무엇인가요? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Canvas 배리언트의 전환 합계가 해당 단계 합계의 총합보다 큰 것은 일반적인 현상입니다. 이는 사용자가 배리언트에 진입하자마자 전환 이벤트를 수행할 수 있기 때문입니다. 그러나 이 동일한 전환 이벤트는 Canvas 단계에는 집계되지 않습니다. 따라서 Canvas에 진입하고 첫 번째 Canvas 단계를 수신하기 전에 전환 이벤트를 수행한 사용자는 배리언트 전환 합계에는 집계되지만 단계 합계에는 집계되지 않습니다. Canvas에 진입했지만 어떤 단계도 수신하기 전에 Canvas를 종료한 사용자도 마찬가지입니다.

사용자가 배리언트에 진입하고 단계에서 메시지를 발송받지 않은 후 전환하는 것도 가능합니다. 이 경우 단계 수준에서는 전환이 기록되지 않습니다. 그러나 사용자가 기술적으로 전환했으므로 Canvas 수준에서는 전환이 기록됩니다.

### API 트리거 Canvas를 사용자가 수신했는지 어떻게 확인할 수 있나요? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Canvas 필터를 사용하여 [Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)하면 사용자가 Canvas에 진입했는지 또는 특정 Canvas 단계를 수신했는지 확인할 수 있습니다. 예를 들어, 사용자가 API 트리거 Canvas에 진입했는지 확인하려면 Canvas 진입 필터를 사용하고, 사용자가 Canvas에서 메시지를 수신했는지 확인하려면 수신 단계 필터를 사용하세요. 그런 다음 [`/users/export/segment` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)를 사용하여 해당 Segment의 사용자를 내보낼 수 있습니다.

### Canvas를 삭제할 수 있나요? {#can-i-delete-a-canvas}

아니요, 하지만 [Canvas를 보관]({{site.baseurl}}/user_guide/messaging/governance/archiving)할 수 있습니다.

### 보관된 Canvas 또는 Campaign을 재개하려면 어떻게 하나요? {#how-do-i-resume-an-archived-canvas-or-campaign}

보관된 메시지는 편집 가능한 상태로 되돌리기 전까지 발송되지 않습니다. Campaign 또는 Canvas를 [보관 해제]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving)하고, 진입 스케줄 또는 발송 시간을 미래 기간으로 설정한 다음(깨끗한 사본이 필요한 경우 여정을 복제) **재개**를 선택하거나 필요에 따라 시작하세요. [Campaign 및 Canvas 보관]({{site.baseurl}}/user_guide/messaging/governance/archiving)을 참조하세요.

### 오류가 나타나지 않는데 Canvas가 저장되지 않는 이유는 무엇인가요? {#why-doesnt-my-canvas-save-when-no-error-appears}

오디언스 또는 단계 수준 필터에서 비어 있는 **커스텀 속성** 필터가 상세한 유효성 검사 메시지 없이 저장을 차단할 수 있습니다. 각 필터 카드를 열고, 불완전한 커스텀 속성 규칙을 제거하거나 속성 이름과 값을 모두 입력한 다음 **저장**을 다시 선택하세요.

### Canvas 또는 Campaign에서 태그가 사라진 이유는 무엇인가요? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

워크스페이스에서 [태그]({{site.baseurl}}/user_guide/messaging/governance/tags)를 삭제하면 Braze는 해당 태그를 참조하는 모든 Campaign 및 Canvas에서 해당 태그를 제거합니다. 이 정리 작업이 Canvas 변경 로그에 항상 별도의 항목으로 생성되지는 않습니다.

### 각 Canvas 구성 요소의 분석을 어떻게 볼 수 있나요? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Canvas 구성 요소의 분석을 보려면 Canvas로 이동하여 **Canvas 세부 정보** 페이지를 아래로 스크롤하세요. 여기에서 각 구성 요소의 분석을 볼 수 있습니다. 자세한 내용은 [Canvas 분석]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)을 확인하세요.

### Canvas 단계의 인게이지먼트는 고객 프로필에서 언제 표시되나요? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

`Received Message from Canvas Step`과 같은 필터는 Braze가 해당 단계에 대한 발송, 수신 또는 인게이지먼트 이벤트를 기록한 후에 업데이트됩니다. 인앱 메시지는 발송 형식의 측정기준과 별도로 노출 횟수를 기록할 수 있습니다. [Canvas에서 노출 횟수가 기록되는데 발송이 0으로 표시되는 이유는 무엇인가요?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged)를 참조하세요. 이러한 동일한 이벤트는 **Canvas 세부 정보**의 단계 측정기준에 표시됩니다.

### 고유 사용자 수를 볼 때 Canvas 분석과 세그멘터 중 어느 것이 더 정확한가요? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

세그멘터가 Canvas 또는 Campaign 통계보다 고유 사용자 데이터에 대해 더 정확한 통계입니다. 이는 Canvas 및 Campaign 통계가 무언가가 발생할 때 Braze가 증가시키는 숫자이기 때문입니다. 즉, 이 숫자가 세그멘터의 숫자와 다를 수 있는 변수가 있습니다. 예를 들어, 사용자는 Canvas 또는 Campaign에 대해 두 번 이상 전환할 수 있습니다.

### Canvas에 진입하는 사용자 수가 예상 수와 다른 이유는 무엇인가요? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

Canvas에 진입하는 사용자 수는 오디언스와 트리거가 평가되는 방식으로 인해 예상 수와 다를 수 있습니다. Braze에서는 트리거 전에 오디언스를 평가합니다([속성 변경]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value) 트리거를 사용하는 경우 제외). 이로 인해 트리거 동작이 평가되기 전에 선택한 오디언스에 해당하지 않는 사용자가 Canvas에서 이탈하게 됩니다.

### Canvas 여정 중 익명 사용자에게는 어떤 일이 발생하나요? {#what-happens-to-anonymous-users-during-their-canvas-journey}

익명 사용자도 Canvas에 진입하고 종료할 수 있지만, 식별되기 전까지 해당 사용자의 행동은 특정 고객 프로필과 연결되지 않으므로 분석에서 상호작용이 완전히 추적되지 않을 수 있습니다. [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)를 사용하여 이러한 측정기준에 대한 보고서를 생성할 수 있습니다.

{% alert tip %}
Canvas 문제 해결에 대한 추가 지원이 필요한 경우, 문제 발생일로부터 30일 이내에 Braze 지원팀에 문의하세요. 최근 30일간의 진단 로그만 보유하고 있습니다.
{% endalert %}

### 현재 Canvas 여정에 있는 사용자를 Campaign 또는 Segment에서 제외할 수 있나요? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

`Entered Canvas Variation`, `In Canvas Control Group` 또는 `Received Message from Canvas Step`과 같은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 사용하여 Canvas 진입, 배리언트 할당 또는 단계 인게이지먼트를 기준으로 사용자를 타겟팅할 수 있습니다. 이러한 필터는 진입 기록과 상호작용을 평가하며, 사용자가 활성 여정을 아직 진행 중인지 여부를 나타내지는 않습니다.

활성 Canvas 참여를 기준으로 사용자를 포함하거나 제외하려면 Canvas 진입 및 종료 지점에 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계를 추가하여 커스텀 속성을 설정하고 지운 다음, Campaign 또는 Segment에서 해당 속성을 기준으로 필터링하세요.

## 세분화 {#segmentation}

### "캔버스 배리언트에 진입하지 않음"과 "Canvas 대조군에 속하지 않음"의 차이점은 무엇인가요? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

전체 필터 정의는 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.

#### 캔버스 배리언트에 진입하지 않음 {#has-not-entered-canvas-variation}

사용자가 특정 Canvas의 배리언트 경로에 진입한 적이 없습니다. 대조군에 속하지 않은 모든 사용자가 포함되며, Canvas에 진입했는지 여부는 관계없습니다. 여기에는 다른 배리언트에 진입한 사용자와 어떤 배리언트에도 진입하지 않은 사용자가 모두 포함됩니다.

#### Canvas 대조군에 속하지 않음 {#is-not-in-canvas-control-group}

사용자가 Canvas에 진입했지만 대조군에 속하지 않아 배리언트를 수신한 경우입니다. 이 필터에는 Canvas에 진입한 사용자만 포함됩니다.

배리언트 할당은 Canvas 진입 시점에 이루어집니다. 사용자가 Canvas에 진입하지 않은 경우에는 어떤 배리언트도 할당되지 않습니다. 즉, 대조군에도, 배리언트에도 속하지 않습니다.

## 기존 Canvas 에디터 {#original-canvas-editor}

{% details 기존 Canvas 에디터 FAQ 펼치기 %}

### 기존 에디터에서 현재 에디터로 기존 Canvas를 어떻게 변환하나요? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

[Canvas를 복제]({{site.baseurl}}/cloning_canvases)할 수 있습니다. 이렇게 하면 최신 Canvas 워크플로우에서 기존 Canvas의 사본이 생성됩니다.

### 현재 Canvas 에디터와 기존 Canvas 에디터의 주요 차이점은 무엇인가요? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Canvas 구성 요소 툴바 {#canvas-component-toolbar}

이전에는 기존 Canvas 에디터에서 사용자 여정의 단계를 생성할 때마다 기본적으로 전체 단계가 추가되었습니다. 이러한 전체 단계는 다양한 Canvas 구성 요소로 대체되어 편집 경험의 가시성과 커스텀 설정이 향상되었습니다. Canvas 단계 툴바에서 모든 Canvas 구성 요소를 바로 확인할 수 있습니다.

#### 단계 동작 {#step-behavior}

이전에는 각 전체 단계에 지연 및 스케줄 설정, 예외 이벤트, 오디언스 필터, 메시지 구성, 메시지 진행 옵션 등의 정보가 하나의 구성 요소에 모두 포함되어 있었습니다. 현재 에디터에서는 이러한 설정이 분리되어 Canvas 구축 경험이 더욱 커스텀 가능하며 기능상 일부 차이가 있습니다.

#### 메시지 구성 요소 진행 {#message-component-advancement}

[메시지 구성 요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)는 단계에 진입하는 모든 사용자를 진행시킵니다. 메시지 진행 동작을 별도로 지정할 필요가 없으므로 전체 단계 설정이 더 간단해집니다. **메시지 전송 시 진행** 옵션을 구현하려면 별도의 오디언스 경로를 추가하여 이전 단계를 수신하지 못한 사용자를 필터링하세요.

#### 지연 "이내" 동작 {#delay-in-behavior}

[지연 구성 요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)는 다음 단계로 진행하기 전에 전체 지연 시간을 대기합니다.

예를 들어 4월 12일에 지연 구성 요소가 있고, 지연이 1일 후 오후 2시에 사용자를 다음 단계로 보내도록 설정되어 있다고 가정합니다. 사용자가 4월 13일 오후 2시 1분에 구성 요소에 진입합니다.
- 기존 워크플로우에서는 사용자가 4월 14일 오후 2시에 다음 단계로 진행하며, 이는 진입 시간으로부터 1일 미만입니다.
- 현재 에디터에서는 사용자가 4월 15일 오후 2시에 다음 단계로 진행합니다. 동일한 시간이지만 진입 시간으로부터 1일 이상입니다.

#### Intelligent Timing 동작 {#intelligent-timing-behavior}

[Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)은 메시지 구성 요소에 저장되므로, 지연이 Intelligent Timing 계산 전에 적용됩니다. 이는 사용자가 구성 요소에 진입하는 시점에 따라 기존 Canvas 워크플로우로 구축된 Canvas보다 메시지를 더 늦게 받을 수 있음을 의미합니다.

지연이 2일로 설정되어 있고, Intelligent Timing이 켜져 있으며, 메시지 전송 최적 시간이 오후 2시로 결정되었다고 가정합니다. 사용자가 오후 2시 1분에 지연 단계에 진입합니다.
- **현재 워크플로우:** 지연이 48시간 경과해야 하므로, 사용자는 3일째 오후 2시에 메시지를 받습니다.
- **기존 워크플로우:** 사용자는 2일째 오후 2시에 메시지를 받습니다.

Intelligent Timing이 켜져 있는 경우, 메시지는 사용자가 메시지 구성 요소에 진입한 후 24시간 이내에 식별된 최적 시간에 전송됩니다(지연 구성 요소가 없더라도).

#### 예외 이벤트 {#exception-events}

##### 방해금지 시간 {#quiet-hours}

예외 이벤트는 메시지 단계와 별도인 작업 경로를 사용하여 적용됩니다. 방해금지 시간은 메시지 구성 요소에서 적용됩니다. 즉, 사용자가 이미 작업 경로를 통과하고(예외 이벤트로 제외되지 않은 상태에서), 메시지 구성 요소에 도달했을 때 방해금지 시간에 해당하며, Canvas가 방해금지 시간 이후에 메시지를 재전송하도록 구성된 경우, 예외 이벤트는 더 이상 적용되지 않습니다. 이 사용 사례는 일반적이지 않습니다.

Segment 및 필터의 경우, 메시지 단계에는 전송 시점에 검증되는 추가 Segment 및 필터를 구성할 수 있는 전달 유효성 검사가 있습니다. 이를 통해 앞서 언급한 방해금지 시간 엣지 케이스를 방지할 수 있습니다.

##### "이내" 또는 "다음" 스케줄 설정 {#in-or-on-the-next-schedule-setting}

예외 이벤트는 작업 경로를 사용하여 생성됩니다. 작업 경로는 "X 시간 경과 후"만 지원하며 "X 시간 이내" 또는 "다음 X 시간에"는 지원하지 않습니다.

{% enddetails %}

### "요청 시간 초과" 오류에 대한 지원 티켓을 제출할 때 어떤 정보를 포함해야 하나요? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Canvas 편집 중 "요청 시간 초과" 오류가 발생하여 [Braze 지원팀]({{site.baseurl}}/braze_support)에 문의해야 하는 경우, 빠른 해결을 위해 다음 정보를 포함해 주세요:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Canvas 전달 및 문제 해결 {#canvas-delivery-and-troubleshooting}

### 분리된 사용자도 Canvas 메시지를 수신할 수 있나요? {#are-orphaned-users-eligible-to-receive-canvas-messages}

아니요. [분리된 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)는 메시지를 수신할 수 없습니다. 사용자가 Canvas 여정에 있는 동안 프로필이 분리되면 해당 사용자는 흐름에서 조용히 퇴장합니다. 분석에서 해당 퇴장에 대한 **퇴장** 이벤트가 항상 표시되지는 않으며, 워크플로 요약에 `exited_date` 또는 `exit_reason` 없이 `partial_update_token`이 포함될 수 있습니다.

병합 및 분리된 프로필에 대한 자세한 내용은 [중복 사용자 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)을 참조하세요.

### 활성 Canvas 또는 Campaign을 중지하면 이미 ESP로 전송된 메시지도 전달되나요? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

네. Braze가 이메일 서비스 공급자(ESP)에 요청을 보낸 후에는 해당 발송을 회수할 수 없습니다. Canvas 또는 Campaign을 중지하면 새로운 발송 요청이 차단되지만, 이미 ESP에 전달된 메시지는 여전히 전송될 수 있으며 ESP가 처리하는 동안 발송 수가 계속 증가할 수 있습니다.

이는 [Canvas를 중지하면 어떻게 되나요?](#what-happens-when-you-stop-a-canvas)에서 설명한 것과 동일한 동작입니다. 전송 중인 이메일은 즉시 중단되지 않습니다.

### Canvas 웹훅 단계가 사용자에게 표시되는 콘텐츠 없이 실행되었는지 확인하려면 어떻게 해야 하나요? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze는 Campaigns 및 Canvases의 [웹훅]({{site.baseurl}}/user_guide/channels/webhooks) 단계에 대한 웹훅 **발송** 및 관련 전달 결과를 추적합니다. 단계 분석, [웹훅 리포팅](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content) 또는 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 웹훅 이벤트를 사용하여 단계가 실행되었는지 확인하세요. 서버 측 수신 증명이 필요한 경우 엔드포인트의 요청 로그에서 추가 확인을 할 수 있습니다.

Braze는 웹훅 단계에 대한 내장 비가시 추적 픽셀을 포함하지 않습니다. 커스텀 1픽셀 이미지 요청 대신 Braze 웹훅 측정기준과 엔드포인트 로깅을 활용하세요.

### 웹훅 단계에 본문 필드가 없는 이유는 무엇인가요? {#why-does-my-webhook-step-have-no-body-field}

웹훅 단계는 `POST`, `PUT`, `PATCH`, `DELETE`에 대해 요청 본문을 사용합니다. 메서드를 `GET`으로 변경하면 GET 요청은 요청 본문을 지원하지 않으므로 Braze가 본문 필드를 제거합니다. JSON 또는 폼 데이터를 전송해야 하는 경우 본문을 지원하는 메서드로 다시 전환하세요. 메서드에 대한 자세한 내용은 [웹훅 만들기]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method)를 참조하세요.

### 웹훅 단계에서 spacer.gif를 어떻게 사용하나요? {#how-do-i-use-spacergif-in-a-webhook-step}

Braze는 `cdn.braze.com` 및 `braze-images.com`에 `spacer.gif` 플레이스홀더 이미지를 호스팅합니다. 일부 팀은 외부 엔드포인트를 호출하지 않고 단계를 실행해야 할 때 웹훅 URL을 이 이미지로 지정합니다. 표준 웹훅 단계는 실제 엔드포인트를 호출해야 합니다. [Canvas 웹훅 단계가 사용자에게 표시되는 콘텐츠 없이 실행되었는지 확인하려면 어떻게 해야 하나요?]({{site.baseurl}}/user_guide/channels/webhooks/reporting)에서 설명한 대로 [웹훅 리포팅]({{site.baseurl}}/user_guide/channels/webhooks/reporting)과 엔드포인트 로그를 사용하여 전달을 확인하세요.

### "invalid next-step-id" 오류로 Canvas가 로드되지 않는 이유는 무엇인가요? {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

이 콘솔 오류는 하나 이상의 단계가 누락되었거나 유효하지 않은 다음 단계를 가리키고 있음을 의미합니다. 예를 들어 부분 삭제, 복제 또는 가져오기 후에 발생할 수 있습니다. 편집기에서 Canvas를 열고 분리된 단계를 다시 연결하거나 유효한 다운스트림 경로가 없는 단계를 제거하세요. Canvas가 여전히 로드되지 않으면 Canvas ID와 콘솔 오류 스크린샷을 첨부하여 [Braze 지원팀]({{site.baseurl}}/braze_support)에 문의하세요.

### Currents의 Canvas 전환 타임스탬프가 Canvas 분석과 다른 이유는 무엇인가요? {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currents는 Canvas 전환을 [`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events) 이벤트로 기록합니다. 이벤트 `time`은 전환 이벤트가 발생한 시점입니다. 해당 이벤트의 `conversion_behavior` 필드는 전환 정의(유형 및 기간)를 설명합니다. Canvas 분석은 전환 기간 내에서 Canvas 진입을 기준으로 전환을 집계할 수도 있습니다. 내보내기를 비교할 때 Currents `time`을 전환 이벤트 타임스탬프 및 Canvas 전환 기간 설정과 비교하세요.

### Currents에서 `canvas_step_name`이 null인 이유는 무엇인가요? {#why-is-canvas_step_name-null-in-currents}

`canvas_step_name`과 같은 Campaign 및 Canvas 이름 필드는 Braze가 단계 메타데이터 전파를 완료하기 전에 Currents 이벤트가 전송될 때 `null`일 수 있습니다. 예를 들어 단계를 생성하거나 이름을 변경한 후에 발생할 수 있습니다. 자세한 내용은 [Currents 데이터에서 Campaign 이름 또는 Canvas 단계 이름이 `NULL`인 이유는 무엇인가요?]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data)를 참조하세요.

### 사용자 업데이트 단계에서 배열이 업데이트되지 않는 이유는 무엇인가요? {#why-isnt-my-array-updating-in-a-user-update-step}

[사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계의 JSON을 확인하세요. 배열 및 중첩 속성 업데이트에는 변경하려는 속성에 대한 유효한 경로와 값이 필요합니다. 외부 사용자 ID 등 단계가 자동으로 제공하는 필드를 포함하지 마세요. 출시 전에 단계의 **미리보기 및 테스트** 탭을 사용하여 페이로드를 확인하세요.

### `external_id`가 없는 사용자에게 Canvas 메시지를 보낼 수 있나요? {#can-i-send-canvas-messages-to-users-without-an-external_id}

네, Braze 고객 프로필이 이미 존재하는 경우 가능합니다. `external_id`가 없는 사용자는 [익명 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles)이며 `braze_id` 또는 [사용자 별칭]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)으로 참조할 수 있습니다. Canvas 진입 전에 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 또는 SDK를 사용하여 프로필을 생성하거나 업데이트한 다음, [실행 기반 또는 API 트리거 진입]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)을 사용하세요. 표준 Canvas 타겟팅에는 여전히 Braze 고객 프로필이 필요합니다. 프로필이 없는 이메일 주소만으로는 Canvas 메시지를 보낼 수 없습니다.

### 사용자가 트리거 이벤트를 수행한 횟수보다 Canvas에 진입한 횟수가 적은 이유는 무엇인가요? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

실행 기반 및 API 트리거 Canvases의 경우, Braze는 트리거 이벤트를 중복 제거하여 사용자가 동일한 Canvas에 대해 약 **초당 최대 1회**만 진입할 수 있도록 합니다. 사용자가 1초 이내에 동일한 트리거를 여러 번 수행하면 하나의 진입만 처리됩니다.

동일한 초 내에 여러 진입을 허용하려면 트리거 이벤트 간격을 최소 1.1초로 설정하세요(예: 서버에서 이벤트 타이밍을 제어하는 경우). 동일한 초에 여러 트리거를 허용하는 Campaign 스타일 동작의 경우, 적절한 스케줄링 및 재적격성 설정이 포함된 [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns)와 사용 사례를 비교하세요.

### API 트리거 Canvases에서 사용자가 중복 제거되는 시점은 언제인가요? {#when-are-users-de-duplicated-in-api-triggered-canvases}

사용자가 API 트리거 Canvas에 재진입하여 이전 진입에서 동일한 메시지에 대해 이미 대기 중인 지연 단계에 도달하면, Braze는 중복 발송을 방지하기 위해 사용자를 중복 제거합니다. 두 번째 Canvas 인스턴스는 퇴장하므로 진입 수가 발송 수를 초과할 수 있습니다.

### 테스트 푸시가 잘못된 앱으로 전송되는데 실제 발송은 정상인 이유는 무엇인가요? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

고객 프로필의 **테스트 푸시**는 해당 프로필의 모든 푸시 활성화 기기로 전달됩니다. 여러 앱이 기기에 설치되어 있으면 OS는 일반적으로 첫 번째 사용 가능한 앱에 테스트 알림을 전달하며, 이는 확인하려는 앱이 아닐 수 있습니다.

앱별 타겟팅을 확인하려면 프로필 **테스트 푸시**에만 의존하는 대신 좁은 오디언스(예: `external_id` 필터)가 있는 Campaign 또는 Canvas를 통해 라이브 또는 테스트 메시지를 전송하세요.

여러 앱이 포함된 **Canvas** 메시지 단계의 경우, 메시지 단계에서 **메시지 전송 시 오디언스 검증**을 활성화하여 전송 시점에 Segment 및 필터 검사가 실행되도록 하세요. 자세한 내용은 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)를 참조하세요.

일반적인 테스트 푸시 동작에 대해서는 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) 및 [푸시 FAQ]({{site.baseurl}}/user_guide/channels/push/faqs)를 참조하세요.

### iOS 및 Android에서 Push Stories를 디버그하려면 어떻게 해야 하나요? {#how-do-i-debug-push-stories-on-ios-and-android}

설정 및 크리에이티브 요구 사항은 [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)를 참조하세요. 구현 및 리치 알림 처리에 대해서는 개발자 가이드의 [리치 알림]({{site.baseurl}}/developer_guide/push_notifications/rich) 및 [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories)를 참조하세요.

### "Canvas Messages Delayed 24+ Hours" 이메일은 누가 수신하나요? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze는 Canvas 메시지가 사용량 제한조치로 인해 24시간 이상 지연될 때 이 알림을 전송합니다. 이 이메일은 영향을 받는 Canvas에 이전에 변경을 가한 대시보드 사용자(Canvas 변경 로그 기반)에게 전달됩니다. Braze가 해당 수신자를 확인할 수 없는 경우 이메일은 워크스페이스의 **회사 관리자**에게 전달됩니다.

### 예외 이벤트 발생 후 사용자가 메시지 수신을 중단하는 시점은 언제인가요? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze는 예외 이벤트가 발생하는 즉시 퇴장을 기록하지만, 타이머가 완료될 때까지 사용자가 단계 내에 남아 있을 수 있습니다. 이는 지연 단계에서 가장 눈에 띄게 나타납니다. 예약된 단계와 이벤트 트리거 단계 간의 동작도 다릅니다. 타임라인, 예시 및 분석 세부 사항은 [퇴장 기준]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)을 참조하세요.

### 링크 별칭 인터랙션을 선택할 때 작업 경로 단계에 오류가 표시되는 이유는 무엇인가요? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

이메일 인터랙션 트리거(예: **이메일에서 별칭 클릭** 또는 **Campaign 또는 Canvas 단계에서 별칭 클릭**)를 사용하는 작업 그룹은 해당 링크가 포함된 메시지를 이미 전송한 메시지 단계가 필요합니다. 작업 경로 단계가 클릭을 평가하기 전에 이메일이 전송되도록 단계를 추가하거나 순서를 변경하거나, 사용자가 이 Canvas에서 이미 수신한 메시지와 일치하는 인터랙션을 선택하세요. 전체 인터랙션 트리거 목록은 [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)을 참조하세요.

### 과거 커스텀 이벤트 타임스탬프가 실행 기반 Canvases 및 Campaigns에 어떤 영향을 미치나요? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze는 적격한 이벤트가 수집되고 사용자가 오디언스 규칙을 충족할 때 실행 기반 여정을 평가합니다. Canvas 또는 Campaign이 활성 상태였던 기간 밖에서 이벤트가 프로필에 도달하거나 사용자가 오디언스와 일치하기 전에 도달한 경우 진입 또는 다운스트림 발송이 예상대로 발생하지 않을 수 있습니다. 고객 프로필 활동 로그를 사용하여 이벤트 타임스탬프를 시작 시점 및 Segment 멤버십과 비교하고, [커스텀 이벤트 문제 해결]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events)의 문제 해결 단계를 참조하세요. 동작이 여전히 예상과 일치하지 않으면 [Braze 지원팀]({{site.baseurl}}/braze_support)에 문의하세요.