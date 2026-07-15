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

## Canvas 구축 및 편집 {#building-and-editing-canvas}

### Canvas에 몇 개의 단계를 포함할 수 있나요? {#how-many-steps-i-can-include-in-a-canvas}

Canvas에 최대 200개의 단계를 추가할 수 있습니다.

### 구성요소와 단계의 차이점은 무엇인가요? {#whats-the-difference-between-a-component-and-a-step}

[구성요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)는 Canvas의 효과를 판단하는 데 사용할 수 있는 Canvas의 개별 부분입니다. 구성요소에는 사용자 여정 분할, 지연 추가, 여러 Canvas 경로 테스트 등의 동작이 포함될 수 있습니다. Canvas의 단계는 Canvas 브랜치에서 개인화된 사용자 여정을 의미합니다. 기본적으로 Canvas는 사용자 여정의 단계를 구성하는 개별 구성요소로 이루어져 있습니다.

### 연결이 끊긴 단계가 있는 Canvas를 시작할 수 있나요? {#can-i-launch-a-canvas-with-disconnected-steps}

네. 시작 후에도 연결이 끊긴 단계가 있는 Canvases를 저장할 수 있습니다.

### 사용자가 연결이 끊긴 단계에 도달하면 어디로 이동하나요? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

사용자가 Canvas 워크플로의 연결이 끊긴 단계에 있는 경우, 후속 단계가 있으면 해당 단계로 진행하며, 단계의 설정에 따라 사용자가 어떻게 진행할지 결정됩니다. 이는 사용자가 Canvas의 나머지 부분에 직접 연결하지 않고도 단계를 변경할 수 있도록 하기 위한 것입니다. 또한 즉시 라이브로 전환하기 전에 테스트할 수 있는 여유를 제공하여 초안 저장을 효과적으로 가능하게 합니다.

단계를 연결 해제하기 전에 캔버스 단계에서 대기 중인 사용자에 대한 분석 보기를 확인하는 것을 권장합니다.

### 하나의 배리언트에 여러 브랜치가 있는 Canvas에서 오디언스와 전송 시간이 동일한 경우 어떻게 되나요? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

각 단계에 대해 작업을 대기줄에 넣으며, 거의 동시에 실행되고 그 중 하나가 "선택"됩니다. 실제로는 다소 균등하게 분배될 수 있지만, 먼저 생성된 단계 쪽으로 약간의 편향이 있을 가능성이 높습니다.

또한 해당 분배가 정확히 어떤 모습일지 보장할 수 없습니다. 균등한 분할을 원한다면 [무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) 필터를 추가하세요.

### Canvas 오디언스는 어떻게 평가되나요? {#how-are-canvas-audiences-evaluated}

기본적으로 Canvas의 전체 단계에 대한 필터와 Segments는 전송 시점에 확인됩니다. 결정 분할 단계는 이전 단계를 수신한 직후(또는 지연 전)에 평가를 수행합니다.

### 예외 이벤트는 언제 트리거되나요? {#when-does-an-exception-event-trigger}

예외 이벤트는 사용자가 연결된 캔버스 구성요소를 수신하기 위해 대기하는 동안에만 트리거됩니다. 사용자가 미리 동작을 수행하면 예외 이벤트가 트리거되지 않습니다. 특정 이벤트를 미리 수행한 사용자를 제외하려면 대신 [필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 사용하세요.

### Canvas를 편집하면 이미 Canvas에 있는 사용자에게 어떤 영향을 미치나요? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

다단계 Canvas의 일부 단계를 편집하면, 이미 오디언스에 포함되어 있지만 아직 해당 단계를 수신하지 않은 사용자는 업데이트된 버전의 메시지를 받게 됩니다. 이는 해당 단계에 대해 아직 평가되지 않은 경우에만 발생합니다.

시작 후 편집할 수 있는 항목에 대한 자세한 내용은 [시작 후 Canvas 변경]({{site.baseurl}}/post-launch_edits)을 참조하세요.

### Canvas를 중지하면 어떻게 되나요? {#what-happens-when-you-stop-a-canvas}

Canvas를 중지하면 다음이 적용됩니다:

- 사용자가 Canvas에 진입하는 것이 차단됩니다.
- 사용자가 플로우의 어디에 있든 더 이상 메시지가 전송되지 않습니다.
- **예외:** 이메일이 포함된 Canvases는 즉시 중지되지 않습니다. 전송 요청이 SendGrid로 전달된 후에는 사용자에게 전달되는 것을 막을 수 없습니다.

### 사용자 라이프사이클별로 하나의 Canvas를 구축해야 하나요, 아니면 별도의 Canvases를 구축해야 하나요? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Canvas로 달성하려는 목표에 따라 사용자 여정을 구축하는 방법에 대해 다른 접근 방식이 필요할 수 있습니다. Canvas의 유연성을 통해 사용자 라이프사이클의 모든 단계에 대한 사용자 여정을 매핑할 수 있습니다. 효과적인 사용자 여정을 만들기 위한 간소화된 접근 방식의 여러 예시는 [Braze 캔버스 템플릿]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)을 확인하세요.

## 메시지 및 전달 {#messages-and-delivery}

### Canvas의 인앱 메시지는 언제 전송되나요? {#when-are-in-app-messages-in-canvas-sent}

인앱 메시지는 다음 세션 시작 시 전송됩니다. 즉, 사용자가 Canvas가 중지되기 전에 캔버스 단계에 진입하면, 인앱 메시지가 아직 만료되지 않은 한 다음 세션 시작 시 인앱 메시지를 받게 됩니다.

사용자가 Canvas가 중지되기 전에 세션을 시작했지만 인앱 메시지가 즉시 표시되지 않을 수 있습니다. 이는 인앱 메시지가 커스텀 이벤트에 의해 트리거되거나 지연되는 경우에 발생할 수 있습니다. 따라서 Canvas가 중지된 후에도 사용자가 인앱 메시지 노출 횟수를 기록하고 인앱 메시지를 "수신"할 수 있습니다. 그러나 사용자는 Canvas가 중지되기 전에, 그리고 캔버스 단계를 수신한 **이후에** 세션을 시작했어야 합니다.

{% alert note %}
Canvas를 중지해도 메시지 수신을 대기 중인 사용자가 사용자 여정에서 나가지는 않습니다. Canvas를 다시 활성화하고 사용자가 여전히 메시지를 기다리고 있다면 메시지를 받게 됩니다(메시지가 전송되었어야 할 시간이 지난 경우에는 받지 못합니다).
{% endalert %}

### 노출 횟수가 기록되었는데 Canvas에서 전송 수가 0으로 표시되는 이유는 무엇인가요? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

인앱 메시지 단계가 포함된 Canvas에서 _전송된 메시지_가 항상 0인 경우, 이는 인앱 메시지 전달이 다른 메시징 채널과 다르게 작동하기 때문입니다.

인앱 메시지는 Braze에서 "푸시"되는 것이 아니라 SDK에 의해 "풀"됩니다. 적격 사용자를 위한 인앱 메시지는 세션 시작 시 자동으로 전달되며 트리거 이벤트가 발생할 때까지 "대기"합니다. 적격 사용자가 세션을 시작할 때 메시지를 수신하므로 Braze는 이를 전송 이벤트로 보고하지 않습니다. 사용자가 트리거 이벤트를 수행하면 메시지가 표시되고 Braze는 노출 횟수를 기록하며 고객 프로필에서 캔버스 단계(또는 Campaign)를 수신됨으로 표시합니다. 따라서 인앱 메시지의 _전송_ 합계는 0이 됩니다.

### 긴 지연 또는 브랜치 후에 사용자가 인앱 메시지를 받지 못한 이유는 무엇인가요? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

업스트림 [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) 단계와 오디언스 확인이 완료된 후, 사용자는 메시지 단계에 도달해야만 인앱 메시지를 받을 수 있습니다. 메시지가 캘린더 날짜에 만료되거나 **단계가 사용 가능해진 후 짧은 기간** 내에 만료되는 경우, 느린 브랜치의 사용자는 만료 후에 도착하여 메시지를 볼 수 없습니다. 만료 시간을 가장 긴 현실적인 경로 지연에 맞추세요. 자세한 내용과 예시는 [인앱 메시지 만료]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration)를 참조하세요.

### "Canvas 진입 속성정보는 인앱 메시지에서 사용할 수 없습니다"라는 메시지가 표시되는 이유는 무엇인가요? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

이 메시지는 개인화가 인앱 메시지에서 Canvas 내에서 확인할 수 없는 필드를 참조할 때 나타납니다. [컨텍스트 및 이벤트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) 및 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)에 설명된 대로 `context` 오브젝트를 사용하세요. 레거시 Liquid 네임스페이스 `canvas_entry_properties`는 `context`와 다른 제약 조건이 있습니다. 여러 단계에 걸쳐 값을 유지해야 하는 경우, Braze 팀과 함께 [기존 Canvas 에디터의 영구 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)를 검토하세요. 저장된 값은 기기가 인앱 페이로드를 다운로드하기 전에 사용자가 Canvas를 나가면 지워집니다.

### Canvas에서 드래그 앤 드롭 인앱 메시지의 버튼 클릭은 어디에서 확인할 수 있나요? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

드래그 앤 드롭 인앱 메시지의 버튼 수준 측정기준은 상위 Canvas 요약이 아닌 **Canvas 세부 정보**의 **메시지** 단계 분석 카드에 표시됩니다. Canvas를 열고 메시지 단계를 선택한 후 인앱 참여를 확인하세요. 리포팅 개념에 대해서는 [Canvas 분석으로 측정 및 테스트]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)를 참조하세요.

### 동일한 Canvas 메시지 단계 또는 다변량 전송에서 각 배리언트에 대해 다른 전송 시간을 스케줄할 수 있나요? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

아니요. 동일한 다변량 구성 또는 메시지 단계의 배리언트는 하나의 전달 스케줄을 공유합니다. 동일한 스케줄 전송에서 하나의 배리언트를 오후 6시에, 다른 배리언트를 오후 7시에 전송하도록 할당할 수 없습니다.

전송을 시차를 두거나 경로별로 다른 시간을 사용하려면 다음 방법을 시도해 보세요:

- 각 메시지가 자체 스케줄을 갖도록 메시지 단계 사이에 지연 단계를 배치합니다.
- 브랜치 또는 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) 단계를 사용하여 사용자가 다른 타이밍의 경로를 따르도록 합니다.
- 사용 사례가 하나의 Canvas 안에 있을 필요가 없는 경우 별도의 Campaigns를 사용합니다.

Campaigns의 다변량 및 A/B 개념에 대해서는 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

### 사용자가 Canvas 메시지 단계에서 글로벌 최대 게재빈도 설정에 도달하면 어떻게 되나요? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

해당 채널에 대한 전송을 받지 못하지만, 메시지 단계는 글로벌 최대 게재빈도 설정으로 인해 메시지가 전송되지 않은 경우에도 사용자를 진행시킵니다. 단계별 진행 사례에 대해서는 [사용자 진행 방식]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance)을 참조하세요. 글로벌 최대 게재빈도 설정만으로는 사용자가 Canvas에서 나가지 않으며, 이 동작은 메시지 단계의 **전달 유효성 검사**와는 별개입니다. 자세한 내용은 [사용량 제한 및 최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)을 참조하세요.

### 전송 수가 예상 오디언스 크기보다 낮은 이유는 무엇인가요? {#why-are-sends-lower-than-the-estimated-audience-size}

전송 수는 [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)와 동일한 여러 이유로 **예상 오디언스**보다 낮을 수 있습니다. 여기에는 빈도 제한, 엄격한 기기 또는 브라우저 필터, 재적격 기간, 사용량 제한, 채널 수준 제외(예: 푸시 도달 가능성 또는 이메일 구독 및 전달 가능성 확인) 등이 포함됩니다.

Canvas 고유의 요인도 적용됩니다:

- **액션 기반 또는 API 트리거 진입:** 사용자는 진입 동작을 수행한 후에만 진입(및 단계 수신)하므로, 해당 동작이 발생할 때까지 실제 전송 수는 사전 추정치에 미치지 못합니다.
- **오디언스 경로:** 사용자는 자격을 충족하는 가장 높은 우선순위의 브랜치로 라우팅되므로, 하위 브랜치는 단순 Segment 수가 시사하는 것보다 적은 사용자를 받을 수 있습니다.
- **오디언스 및 전송 시간 확인:** 전체 단계는 별도로 구성하지 않는 한 전송 시점에 필터를 재평가합니다. Canvas가 구축될 때 자격을 충족한 사용자가 메시지 전송 전에 이탈할 수 있습니다.
- **대조군:** 글로벌 또는 Canvas 대조군은 진입자의 일부를 메시징에서 제외합니다.
- **방해금지 시간 및 지연:** 메시지가 보류되거나 재스케줄되어 보고 있는 리포팅 기간에서 전송이 이동할 수 있습니다.
- **최대 진입 또는 오디언스 제한:** 기본 Segment가 더 크더라도 진입 또는 전송 제한이 추가 사용자를 차단합니다.
- **리포팅 기간:** 분석 범위에 추정치와 비교하는 모든 전송이 포함되지 않을 수 있습니다.

### 예상 오디언스와 Canvas 사용자 수가 일치하지 않는 이유는 무엇인가요? {#why-dont-estimated-audience-and-canvas-user-counts-match}

**예상 오디언스**는 추정이 실행될 때 Segment 및 진입 필터와 일치하는 사용자를 반영합니다. 그 이후에 지연 또는 액션 기반 진입, 재적격, API 트리거 또는 브랜치 라우팅으로 인해 스냅샷과 비교하여 여정에 접촉하는 프로필 수가 증가할 수 있습니다. 전송 시점 필터가 실패하면 사용자가 이탈하여 실제 진입 또는 전송 수가 줄어들 수도 있습니다. 타이밍, 제한 및 평가 설정을 [전송 수가 예상 오디언스 크기보다 낮은 이유는 무엇인가요?](#why-are-sends-lower-than-the-estimated-audience-size)와 함께 비교하세요.

### _고유 수신자_가 타겟팅한 사용자 수보다 높은 이유는 무엇인가요? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_고유 수신자_는 Braze가 Canvas 및 Campaign 리포팅에서 **일별 고유 수신자**를 추적하기 때문에 예상보다 높을 수 있습니다. 이는 사용자가 여정에서 메시지를 수신할 때마다 정확한 전환 기여도를 지원합니다.

예를 들어, 사용자가 월요일에 캔버스 단계를 수신하고 금요일에 다시 수신한 후 각 전송 후에 전환하면, Braze는 두 개의 수신자 행과 두 건의 범위 내 전환을 집계할 수 있습니다. 반복 진입 또는 재적격을 사용하면 동일한 소수의 프로필이 여러 날에 걸쳐 여러 _고유 수신자_를 생성할 수 있습니다.

### Canvas의 전송 속도가 낮아지는 이유는 무엇인가요? {#why-is-my-canvas-experiencing-lower-send-rates}

일별 스케줄 Canvas의 전송 사용자 수가 시간이 지남에 따라 줄어드는 경우, 다음 사항을 확인하세요:

- **재적격이 켜져 있는지 확인하세요:** 재적격이 없으면 Braze는 각 사용자를 Canvas에 한 번만 진입시킵니다. 일별 스케줄 Canvases에서는 오디언스와 일치하고 아직 Canvas에 진입하지 않은 사용자만 각 진입에 적격합니다. 더 많은 사용자가 진입할수록 이후 진입에 적격한 사용자가 줄어들어 진입 볼륨이 감소합니다.
- **오디언스의 멤버십이 고정되어 있는지 확인하세요:** 고정된 사용자 목록(예: Segment 필터로 사용된 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import))으로 구축된 오디언스는 자동으로 새 멤버를 추가하지 않습니다. 새로운 진입자가 없으면 사용자가 Canvas에 진입함에 따라 진입 볼륨이 회복될 수 없습니다.

[전달 속도 사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) 및 단일 발생에 대한 전송을 줄이는 기타 요인에 대해서는 [전송 수가 예상 오디언스 크기보다 낮은 이유는 무엇인가요?](#why-are-sends-lower-than-the-estimated-audience-size)를 참조하세요.

## 분석 및 전환 {#analytics-and-conversions}

### Canvas에서 사용자 전환은 어떻게 추적되나요? {#how-are-user-conversions-tracked-in-a-canvas}

사용자는 Canvas 진입당 한 번만 전환할 수 있습니다. 전환은 해당 진입에 대해 사용자가 마지막으로 수신한 메시지에 할당됩니다. Canvas 시작 부분의 요약 블록은 메시지 수신 여부에 관계없이 해당 경로 내 사용자가 수행한 모든 전환을 반영합니다. 이후 각 단계는 해당 단계가 사용자가 수신한 가장 최근 단계였을 때 발생한 전환만 표시합니다.

{% alert note %}
사용자가 Canvas에 재진입하면 전환 이벤트는 가장 최근 진입에 대해서만 추적됩니다. 전환 이벤트가 소급 적용되더라도 이전 진입에 대해서는 전환 이벤트가 기록되지 않습니다.
{% endalert %}

{% details 예시 펼치기 %}

**예시 1**

10개의 푸시 알림이 있는 Canvas 경로가 있고 전환 이벤트가 "세션 시작"("앱 열기")인 경우:

- 사용자 A는 진입 후 첫 번째 메시지를 수신하기 전에 앱을 엽니다.
- 사용자 B는 각 푸시 알림 후에 앱을 엽니다.

**결과:** 요약에는 두 건의 전환이 표시되고, 개별 단계에서는 첫 번째 단계에서 한 건의 전환이, 이후 모든 단계에서는 0건의 전환이 표시됩니다.

{% alert note %}
전환 이벤트가 발생할 때 방해금지 시간이 활성화되어 있어도 동일한 규칙이 적용됩니다.
{% endalert %}

**예시 2**

방해금지 시간이 활성화된 단일 단계 Canvas가 있는 경우:

1. 사용자가 Canvas에 진입합니다.
2. 첫 번째 단계에는 지연이 없지만 설정된 방해금지 시간 내에 있어 메시지가 억제됩니다.
3. 사용자가 전환 이벤트를 수행합니다.

**결과:** 사용자는 전체 캔버스 배리언트에서는 전환으로 집계되지만, 해당 단계를 수신하지 않았으므로 단계에서는 전환으로 집계되지 않습니다.

{% enddetails %}

### 다양한 전환율 유형의 차이점은 무엇인가요? {#whats-the-difference-between-the-different-conversion-rate-types}

- 총 Canvas 전환은 각 사용자가 완료한 전환 수가 아니라 전환 이벤트를 완료한 고유 사용자 수를 반영합니다.
- 배리언트 전환율 또는 Canvas 시작 부분의 요약 블록은 메시지 수신 여부에 관계없이 해당 경로 내 사용자가 수행한 모든 전환을 총합으로 반영합니다.
- 단계 전환율은 해당 메시지 단계를 수신하고 설정된 전환 이벤트 중 하나를 완료한 개인의 수를 반영합니다.

### Canvas 단계 전환율이 Canvas 배리언트 총 전환율과 같지 않은 이유는 무엇인가요? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Canvas 배리언트의 전환 합계가 단계 합계의 합보다 큰 것은 일반적입니다. 이는 사용자가 배리언트에 진입하자마자 해당 배리언트에 대한 전환 이벤트를 수행할 수 있기 때문입니다. 그러나 이 동일한 전환 이벤트는 캔버스 단계에 대해서는 집계되지 않습니다. 따라서 Canvas에 진입하고 첫 번째 캔버스 단계를 수신하기 전에 전환 이벤트를 수행한 사용자는 배리언트 전환 합계에는 집계되지만 단계 합계에는 집계되지 않습니다. Canvas에 진입했지만 어떤 단계도 수신하기 전에 Canvas를 나간 사용자도 마찬가지입니다.

사용자가 배리언트에 진입하고 어떤 단계에서도 메시지를 받지 않았지만 전환하는 경우도 가능합니다. 이 경우 단계 수준에서는 전환이 기록되지 않습니다. 그러나 사용자가 기술적으로 전환했기 때문에 Canvas 수준에서는 전환이 기록됩니다.

### API 트리거 Canvas를 사용자가 수신했는지 어떻게 확인할 수 있나요? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Canvas 필터를 사용하여 [Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)하면 사용자가 Canvas에 진입했는지 또는 특정 캔버스 단계를 수신했는지 확인할 수 있습니다. 예를 들어, 사용자가 API 트리거 Canvas에 진입했는지 확인하려면 Canvas 진입 필터를 사용하고, Canvas에서 메시지를 수신했는지 확인하려면 수신 단계 필터를 사용하세요. 그런 다음 [`/users/export/segment` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)를 사용하여 해당 Segment의 사용자를 내보낼 수 있습니다.

### Canvas를 삭제할 수 있나요? {#can-i-delete-a-canvas}

아니요. 하지만 [Canvas를 아카이브]({{site.baseurl}}/user_guide/messaging/governance/archiving)할 수 있습니다.

### 아카이브된 Canvas 또는 Campaign을 다시 시작하려면 어떻게 하나요? {#how-do-i-resume-an-archived-canvas-or-campaign}

아카이브된 메시지는 편집 가능한 상태로 되돌리기 전까지 전송되지 않습니다. Campaign 또는 Canvas를 [아카이브 해제]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving)하고, 진입 스케줄 또는 전송 시간을 미래 기간으로 설정한 다음(또는 깨끗한 사본이 필요한 경우 여정을 복제한 다음), 필요에 따라 **재개** 또는 시작하세요. [Campaign 및 Canvases 아카이브]({{site.baseurl}}/user_guide/messaging/governance/archiving)를 참조하세요.

### 오류가 표시되지 않는데 Canvas가 저장되지 않는 이유는 무엇인가요? {#why-doesnt-my-canvas-save-when-no-error-appears}

오디언스 또는 단계 수준 필터에서 비어 있는 **커스텀 속성** 필터가 상세한 유효성 검사 메시지 없이 저장을 차단할 수 있습니다. 각 필터 카드를 열고 불완전한 커스텀 속성 규칙을 제거하거나 속성 이름과 값을 모두 입력한 다음 **저장**을 다시 선택하세요.

### Canvas 또는 Campaign에서 태그가 사라진 이유는 무엇인가요? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

워크스페이스에서 [태그]({{site.baseurl}}/user_guide/messaging/governance/tags)가 삭제되면, Braze는 해당 태그를 참조하는 모든 Campaign 및 Canvas에서 제거합니다. 이 정리 작업이 Canvas 변경 로그에 항상 별도의 항목으로 생성되지는 않습니다.

### 각 Canvas 구성요소의 분석을 어떻게 볼 수 있나요? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Canvas 구성요소의 분석을 보려면 Canvas로 이동하여 **Canvas 세부 정보** 페이지를 아래로 스크롤하세요. 여기에서 각 구성요소의 분석을 볼 수 있습니다. 자세한 내용은 [Canvas 분석]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)을 확인하세요.

### Canvas 단계의 참여가 고객 프로필에 언제 표시되나요? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

`Received Message from Canvas Step`과 같은 필터는 Braze가 해당 단계에 대한 전송, 수신 또는 참여 이벤트를 기록한 후에 업데이트됩니다. 인앱 메시지는 전송 스타일 측정기준과 별도로 노출 횟수를 기록할 수 있습니다. [노출 횟수가 기록되었는데 Canvas에서 전송 수가 0으로 표시되는 이유는 무엇인가요?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged)를 참조하세요. 동일한 이벤트가 **Canvas 세부 정보**의 단계 측정기준에도 표시됩니다.

### 고유 사용자 수를 볼 때 Canvas 분석과 세그먼터 중 어느 것이 더 정확한가요? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

세그먼터는 Canvas 또는 Campaign 통계보다 고유 사용자 데이터에 대해 더 정확한 통계입니다. 이는 Canvas 및 Campaign 통계가 무언가가 발생할 때 Braze가 증가시키는 숫자이기 때문입니다. 즉, 이 숫자가 세그먼터의 숫자와 다를 수 있는 변수가 존재합니다. 예를 들어, 사용자는 Canvas 또는 Campaign에 대해 두 번 이상 전환할 수 있습니다.

### Canvas에 진입하는 사용자 수가 예상 수와 다른 이유는 무엇인가요? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

Canvas에 진입하는 사용자 수는 오디언스와 트리거가 평가되는 방식 때문에 예상 수와 다를 수 있습니다. Braze에서는 오디언스가 트리거보다 먼저 평가됩니다([속성 변경]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value) 트리거를 사용하는 경우 제외). 이로 인해 트리거 동작이 평가되기 전에 선택한 오디언스에 포함되지 않은 사용자가 Canvas에서 이탈하게 됩니다.

### Canvas 여정 중 익명 사용자에게는 어떤 일이 발생하나요? {#what-happens-to-anonymous-users-during-their-canvas-journey}

익명 사용자는 Canvases에 진입하고 나갈 수 있지만, 식별될 때까지 해당 동작이 특정 고객 프로필과 연결되지 않으므로 분석에서 상호작용이 완전히 추적되지 않을 수 있습니다. [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)를 사용하여 이러한 측정기준에 대한 보고서를 생성할 수 있습니다.

{% alert tip %}
Canvas 문제 해결에 대한 추가 지원이 필요한 경우, 문제 발생 후 30일 이내에 Braze 고객지원에 문의하세요. 최근 30일간의 진단 로그만 보유하고 있습니다.
{% endalert %}

### 현재 Canvas 여정에 있는 사용자를 Campaign 또는 Segment에서 제외할 수 있나요? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

`Entered Canvas Variation`, `In Canvas Control Group`, `Received Message from Canvas Step` 등의 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 사용하여 Canvas 진입, 배리언트 할당 또는 단계 참여를 기준으로 사용자를 타겟팅할 수 있습니다. 이러한 필터는 진입 이력과 상호작용을 평가하며, 사용자가 현재 활성 여정을 진행 중인지 여부를 나타내지는 않습니다.

활성 Canvas 참여를 기준으로 사용자를 포함하거나 제외하려면 Canvas 진입 및 종료 시점에 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계를 추가하여 커스텀 속성을 설정하고 해제한 다음, Campaigns 또는 Segments에서 해당 속성을 기준으로 필터링하세요.

## 세분화 {#segmentation}

### "Canvas 배리언트에 진입하지 않음"과 "Canvas 대조군에 포함되지 않음"의 차이점은 무엇인가요? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

전체 필터 정의는 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.

#### Canvas 배리언트에 진입하지 않음 {#has-not-entered-canvas-variation}

사용자가 특정 Canvas의 배리언트 경로에 진입한 적이 없습니다. 대조군에 포함되지 않은 모든 사용자가 포함되며, Canvas에 진입했는지 여부와 관계없습니다. 여기에는 다른 배리언트에 진입한 사용자와 어떤 배리언트에도 진입하지 않은 사용자가 포함됩니다.

#### Canvas 대조군에 포함되지 않음 {#is-not-in-canvas-control-group}

사용자가 Canvas에 진입했지만 대조군에 포함되지 않아 배리언트를 수신했습니다. Canvas에 진입한 사용자만 포함됩니다.

배리언트 할당은 Canvas 진입 시 이루어집니다. 사용자가 Canvas에 진입하지 않은 경우 어떤 배리언트도 할당되지 않습니다. 즉, 대조군이나 배리언트에 포함되지 않습니다.

## 기존 Canvas 에디터 {#original-canvas-editor}

{% details 기존 Canvas 에디터 FAQ 펼치기 %}

### 기존 에디터의 Canvas를 현재 에디터로 어떻게 변환하나요? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

[Canvas를 복제]({{site.baseurl}}/cloning_canvases)할 수 있습니다. 이렇게 하면 최신 Canvas 워크플로에서 기존 Canvas의 사본이 생성됩니다.

### 현재 Canvas 에디터와 기존 Canvas 에디터의 주요 차이점은 무엇인가요? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Canvas 구성요소 도구 모음 {#canvas-component-toolbar}

이전에는 기존 Canvas 에디터에서 사용자 여정의 단계를 생성할 때마다 기본적으로 전체 단계가 추가되었습니다. 이러한 전체 단계는 다양한 Canvas 구성요소로 대체되어 편집 경험에 대한 가시성과 커스터마이징이 향상되었습니다. Canvas 단계 도구 모음에서 모든 Canvas 구성요소를 즉시 확인할 수 있습니다.

#### 단계 동작 {#step-behavior}

이전에는 각 전체 단계에 지연 및 스케줄 설정, 예외 이벤트, 오디언스 필터, 메시지 구성, 메시지 진행 옵션 등의 정보가 하나의 구성요소에 모두 포함되어 있었습니다. 현재 에디터에서는 이러한 설정이 분리되어 Canvas 구축 경험이 더 커스터마이징 가능하며 기능에 일부 차이가 있습니다.

#### 메시지 구성요소 진행 {#message-component-advancement}

[메시지 구성요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)는 단계에 진입하는 모든 사용자를 진행시킵니다. 메시지 진행 동작을 지정할 필요가 없어 전체 단계 구성이 더 간단해집니다. **메시지 전송 시 진행** 옵션을 구현하려면 이전 단계를 수신하지 않은 사용자를 필터링하기 위해 별도의 오디언스 경로를 추가하세요.

#### 지연 "이내" 동작 {#delay-in-behavior}

[지연 구성요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)는 다음 단계로 진행하기 전에 전체 지연 시간을 기다립니다.

예를 들어 4월 12일에 지연 구성요소가 있고 지연이 1일 후 오후 2시에 사용자를 다음 단계로 보내도록 설정되어 있다고 가정합니다. 사용자가 4월 13일 오후 2시 1분에 구성요소에 진입합니다.
- 기존 워크플로에서는 사용자가 4월 14일 오후 2시에 다음 단계로 진행하며, 이는 진입 시간으로부터 1일 미만입니다.
- 현재 에디터에서는 사용자가 4월 15일 오후 2시에 다음 단계로 진행합니다. 동일한 시간이지만 진입 시간으로부터 1일 이상입니다.

#### Intelligent Timing 동작 {#intelligent-timing-behavior}

[Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)은 메시지 구성요소에 저장되므로 Intelligent Timing 계산 전에 지연이 적용됩니다. 즉, 사용자가 구성요소에 진입하는 시점에 따라 기존 Canvas 워크플로로 구축된 Canvas보다 메시지를 늦게 받을 수 있습니다.

예를 들어 지연이 2일로 설정되어 있고 Intelligent Timing이 켜져 있으며 메시지를 보내기 가장 좋은 시간이 오후 2시로 결정되었다고 가정합니다. 사용자가 오후 2시 1분에 지연 단계에 진입합니다.
- **현재 워크플로:** 지연이 지나는 데 48시간이 걸리므로 사용자는 3일째 오후 2시에 메시지를 받습니다.
- **기존 워크플로:** 사용자는 2일째 오후 2시에 메시지를 받습니다.

Intelligent Timing이 켜져 있으면 메시지는 사용자가 메시지 구성요소에 진입한 후 24시간 이내에 식별된 최적 시간에 전송됩니다(지연 구성요소가 관련되지 않은 경우에도).

#### 예외 이벤트 {#exception-events}

##### 방해금지 시간 {#quiet-hours}

예외 이벤트는 메시지 단계와 별도인 행동 경로를 사용하여 적용됩니다. 방해금지 시간은 메시지 구성요소에서 적용됩니다. 즉, 사용자가 이미 행동 경로를 통과했고(예외 이벤트로 제외되지 않았으며), 메시지 구성요소에 도달했을 때 방해금지 시간에 해당하고, 방해금지 시간 이후에 메시지를 재전송하도록 Canvas가 구성된 경우 예외 이벤트가 더 이상 적용되지 않습니다. 이 사용 사례는 일반적이지 않습니다.

Segments와 필터의 경우, 메시지 단계에는 전송 시점에 검증되는 추가 Segments와 필터를 구성할 수 있는 전달 유효성 검사가 있습니다. 이를 통해 앞서 언급한 방해금지 시간 엣지 케이스를 방지할 수 있습니다.

##### "이내" 또는 "다음" 스케줄 설정 {#in-or-on-the-next-schedule-setting}

예외 이벤트는 행동 경로를 사용하여 생성됩니다. 행동 경로는 "X 시간 기간 후"만 지원하며 "X 시간 이내" 또는 "다음 X 시간에"는 지원하지 않습니다.

{% enddetails %}

### "요청 시간 초과" 오류에 대한 고객지원 티켓을 제출할 때 무엇을 포함해야 하나요? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Canvas를 편집하는 동안 "요청 시간 초과" 오류가 발생하여 [Braze 고객지원]({{site.baseurl}}/braze_support)에 문의해야 하는 경우, 해결 속도를 높이기 위해 다음 정보를 포함하세요:

- **화면 녹화:** 페이지 전환을 포함하여 오류가 표시되기 전에 수행한 단계의 녹화.
- **타임스탬프 및 시간대:** 오류가 발생한 정확한 시간과 시간대.
- **브라우저 및 버전:** 사용 중인 브라우저(예: Chrome 120, Safari 17)와 다른 브라우저에서 오류를 재현해 보았는지 여부.
- **재현 단계:** 오류를 트리거하는 동작에 대한 명확한 설명(관련된 특정 캔버스 단계 또는 구성 포함).
- **네트워크 로그(선택 사항):** 브라우저 개발자 도구(**네트워크** 탭)를 열고 오류를 재현한 후 네트워크 로그를 HTTP Archive(HAR) 로그 파일로 내보내세요. 이를 통해 고객지원 팀이 어떤 API 호출이 시간 초과되는지 식별하는 데 도움이 됩니다.

## Canvas 전달 및 문제 해결 {#canvas-delivery-and-troubleshooting}

### 고아 사용자는 Canvas 메시지를 수신할 수 있나요? {#are-orphaned-users-eligible-to-receive-canvas-messages}

아니요. [고아 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)는 메시지를 수신할 수 없습니다. 사용자가 Canvas 여정 중에 프로필이 고아 상태가 되면 플로우에서 자동으로 나가게 됩니다. 분석에서 해당 종료에 대한 **종료됨** 이벤트가 항상 표시되지는 않을 수 있으며, 워크플로 요약에 `exited_date` 또는 `exit_reason` 없이 `partial_update_token`이 포함될 수 있습니다.

병합 및 고아 프로필에 대한 자세한 내용은 [중복 사용자 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)을 참조하세요.

### 활성 Canvas 또는 Campaign을 중지하면 이미 ESP에 전송된 메시지가 여전히 전달되나요? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

네. Braze가 이메일 서비스 공급자(ESP)에 요청을 전송한 후에는 해당 전송을 회수할 수 없습니다. Canvas 또는 Campaign을 중지하면 새로운 전송 요청은 방지되지만, 이미 ESP에 전달된 메시지는 여전히 전달될 수 있으며 ESP가 처리하는 동안 전송 수가 증가할 수 있습니다.

이는 [Canvas를 중지할 때](#what-happens-when-you-stop-a-canvas) 설명된 것과 동일한 동작입니다. 전송 중인 이메일은 즉시 중단되지 않습니다.

### Canvas 웹훅 단계가 사용자에게 보이는 콘텐츠 없이 실행되었는지 어떻게 확인할 수 있나요? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze는 Campaigns 및 Canvases의 [웹훅]({{site.baseurl}}/user_guide/channels/webhooks) 단계에 대한 웹훅 **전송** 및 관련 전달 결과를 추적합니다. 단계 분석, [웹훅 리포팅]({{site.baseurl}}/user_guide/channels/webhooks/reporting) 또는 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 웹훅 이벤트를 사용하여 단계가 실행되었는지 확인하세요. 엔드포인트의 요청 로그는 서버 측 수신 증거가 필요할 때 추가 확인을 제공합니다.

Braze는 웹훅 단계에 대한 내장 비가시 추적 픽셀을 포함하지 않습니다. 커스텀 1픽셀 이미지 요청 대신 Braze 웹훅 측정기준과 엔드포인트 로깅에 의존하세요.

### 사용자가 트리거 이벤트를 수행한 횟수보다 Canvas에 적게 진입한 이유는 무엇인가요? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

액션 기반 및 API 트리거 Canvases의 경우, Braze는 트리거 이벤트를 중복 제거하여 사용자가 동일한 Canvas에 대해 **초당 최대 약 1회**만 진입할 수 있도록 합니다. 사용자가 1초 이내에 동일한 트리거를 여러 번 수행하면 하나의 진입만 처리됩니다.

동일한 초에 여러 진입을 허용하려면 트리거 이벤트 간격을 최소 1.1초로 설정하세요(예: 서버에서 이벤트 타이밍을 제어하는 경우). 동일한 초에 여러 트리거를 허용하는 Campaign 스타일 동작의 경우, 적절한 스케줄 및 재적격 설정이 있는 [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns)와 사용 사례를 비교하세요.

### 테스트 푸시가 잘못된 앱으로 전송되지만 라이브 전송은 정상인 이유는 무엇인가요? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

고객 프로필의 **테스트 푸시**는 해당 프로필에 대한 모든 푸시 활성화 기기로 전달됩니다. 기기에 여러 앱이 설치된 경우, OS는 일반적으로 첫 번째 사용 가능한 앱으로 테스트 알림을 전달하며, 이는 검증하려는 앱이 아닐 수 있습니다.

앱별 타겟팅을 확인하려면 프로필 **테스트 푸시**에만 의존하지 말고 좁은 오디언스(예: `external_id`로 필터링)를 사용하여 Campaign 또는 Canvas를 통해 라이브 또는 테스트 메시지를 전송하세요.

여러 앱이 있는 **Canvas** 메시지 단계의 경우, 메시지 단계에서 **메시지 전송 시 오디언스 검증**을 켜서 전송 시점에 Segment 및 필터 확인이 실행되도록 하세요. 자세한 내용은 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)를 참조하세요.

일반적인 테스트 푸시 동작에 대해서는 [테스트 메시지 전송]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) 및 [푸시 FAQ]({{site.baseurl}}/user_guide/channels/push/faqs)를 참조하세요.

### iOS 및 Android에서 Push Stories를 디버그하려면 어떻게 하나요? {#how-do-i-debug-push-stories-on-ios-and-android}

설정 및 크리에이티브 요구 사항은 [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)를 참조하세요. 구현 및 리치 알림 처리에 대해서는 개발자 가이드의 [리치 알림]({{site.baseurl}}/developer_guide/push_notifications/rich) 및 [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories)를 참조하세요.

### "Canvas 메시지 24시간 이상 지연" 이메일은 누가 수신하나요? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze는 Canvas 메시지가 사용량 제한으로 인해 24시간 이상 지연될 때 이 알림을 전송합니다. 이메일은 영향을 받는 Canvas에 이전에 변경을 가한 대시보드 사용자(Canvas 변경 로그 기준)에게 전송됩니다. Braze가 해당 수신자를 확인할 수 없는 경우, 이메일은 워크스페이스의 **회사 관리자**에게 전송됩니다.

### 예외 이벤트 후 사용자가 메시지 수신을 중단하는 시점은 언제인가요? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze는 예외 이벤트가 발생하는 즉시 종료를 기록하지만, 타이머가 완료될 때까지 사용자가 단계 내에 남아 있을 수 있습니다. 이는 지연 단계에서 가장 눈에 띕니다. 스케줄된 단계와 이벤트 트리거 단계 간에도 동작이 다릅니다. 타임라인, 예시 및 분석 세부 사항에 대해서는 [종료 기준]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)을 참조하세요.

### 링크 별칭 상호작용을 선택할 때 행동 경로 단계에 오류가 표시되는 이유는 무엇인가요? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

이메일 상호작용 트리거(예: **이메일에서 별칭 클릭** 또는 **Campaign 또는 Canvas 단계에서 별칭 클릭**)를 사용하는 행동 그룹은 해당 링크가 포함된 메시지를 이미 전송한 메시지 단계가 필요합니다. 행동 경로 단계가 클릭을 평가하기 전에 이메일이 전송되도록 단계를 추가하거나 순서를 변경하세요. 또는 사용자가 이 Canvas에서 이미 수신한 메시지와 일치하는 상호작용을 선택하세요. 상호작용 트리거의 전체 목록은 [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)을 참조하세요.

### 과거 커스텀 이벤트 타임스탬프가 액션 기반 Canvases 및 Campaigns에 어떤 영향을 미치나요? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze는 적격 이벤트가 수집되고 사용자가 오디언스 규칙을 충족할 때 액션 기반 여정을 평가합니다. Canvas 또는 Campaign이 활성화된 기간 외에 이벤트가 프로필에 도착하거나, 사용자가 오디언스와 일치하기 전에 이벤트가 도착하면 진입 또는 다운스트림 전송이 예상대로 발생하지 않을 수 있습니다. 고객 프로필 활동 로그와 [커스텀 이벤트 문제 해결]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events)의 문제 해결 단계를 사용하여 이벤트 타임스탬프를 라이브 시작 시간 및 Segment 멤버십과 비교하세요. 동작이 여전히 예상과 일치하지 않으면 [Braze 고객지원]({{site.baseurl}}/braze_support)에 문의하세요.