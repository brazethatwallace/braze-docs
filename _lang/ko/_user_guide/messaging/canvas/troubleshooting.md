---
nav_title: 문제 해결
article_title: Canvas 문제 해결
page_order: 7
page_type: reference
description: "이 페이지에서는 Canvas의 문제 해결 단계를 안내합니다."
tool: Canvas
---

# Canvas 문제 해결 {#troubleshoot-canvases}

> 이 페이지에서는 Canvases 관련 문제를 해결하는 방법을 안내합니다.

## "Canvas 분기가 너무 많음" 오류 {#too-many-canvas-branches-error}

스케줄된 Canvas를 시작할 때 "Canvas 분기가 너무 많음" 오류가 표시되면, 단계 분기와 진입 오디언스 크기의 조합이 Braze 클러스터 성능 문제를 일으켜 메시지 발송이 차단될 수 있습니다.

Braze는 초안을 저장할 때가 아니라 스케줄된 진입이 있는 Canvas를 시작할 때 이 메시지를 표시합니다. 이를 해결하려면 다음을 시도하세요:

- Canvas의 단계 분기를 줄이세요.
- 진입 오디언스 크기를 줄이세요.
- 많은 병렬 경로 대신 [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/)를 사용하여 분기를 통합하세요.
- Canvas가 기존 편집기를 사용하는 경우, [Canvas Flow로 복제]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/)하고 Canvas 구성요소로 다시 구축하세요.

변경 없이 Canvas를 시작해야 하고 Canvas Flow로 전환할 수 없는 경우, [고객지원]({{site.baseurl}}/support_contact/)에 문의하세요.

## 사용자가 트리거된 캔버스 단계를 받지 못한 이유는 무엇인가요? {#why-did-a-user-not-receive-a-triggered-canvas-step}

먼저 커스텀 이벤트가 Braze로 전달되고 있는지 확인하세요. **Analytics** > **사용자 지정 이벤트 보고서**로 이동한 다음 해당 커스텀 이벤트와 날짜 범위를 선택합니다. 이벤트가 표시되지 않으면 올바르게 설정되어 있는지, 사용자가 올바른 동작을 수행했는지 확인하세요.

커스텀 이벤트가 표시되는 경우 다음을 수행하여 추가로 문제를 해결하세요:

- 사용자의 프로필 다운로드를 확인하여 이벤트를 트리거했는지, 언제 트리거했는지 확인합니다. 이벤트가 트리거된 경우, 이벤트가 트리거된 타임스탬프와 Canvas가 활성화된 시간을 비교하세요. Canvas가 활성화되기 전에 이벤트가 트리거되었을 수 있습니다.
- Canvas 및 타겟팅에 사용된 Segment의 체인지로그를 검토하여 커스텀 이벤트가 트리거되었을 때 사용자가 해당 Segment에 포함되어 있었는지 확인합니다. Segment에 포함되어 있지 않았다면 캔버스 단계를 받지 못했을 것입니다.
- 사용자가 Canvas 진입 시 대조군에 할당되어 캔버스 단계를 받지 못하게 되었는지 확인합니다.
- 스케줄된 지연이 있는 경우, 사용자의 커스텀 이벤트가 지연 전에 트리거되었는지 확인합니다. 지연 전에 이벤트가 트리거되었다면 캔버스 단계를 받지 못했을 것입니다.

{% alert note %}
인앱 메시지는 SDK를 통해 전송된 이벤트로만 트리거할 수 있으며, REST API로는 트리거할 수 없습니다.
{% endalert %}

## Canvas가 예상대로 발송되지 않는 이유는 무엇인가요? {#why-isnt-my-canvas-sending-as-expected}

Canvases는 강력하고 복잡하며, 생성할 때 많은 시간과 노력을 기울이신다는 것을 알고 있습니다. Canvas가 원하는 대로 발송되지 않는 경우, Canvas의 스케줄, 진입 오디언스, 진입 설정을 확인하고 [Canvas 생성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) 단계를 검토하는 것을 권장합니다.

### 스케줄 {#schedule}

- Canvas가 [올바르게 스케줄]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types)되어 있나요?
- 올바른 날짜와 시간을 선택했나요?
- [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types)의 경우, Canvas를 시작한 이후 사용자가 지정된 동작을 수행했나요?

### 진입 설정 {#entry-settings}

[진입 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=basics#selecting-entry-controls)은 Canvases가 어떻게 발송되는지 이해하는 데 중요합니다. Canvas에 진입할 수 있는 사용자 수를 제한했는지 확인하세요.

사용자는 더 이상 메시지를 받을 자격이 없는 경우 Canvas에서 이탈할 수도 있습니다. 예를 들어, Canvas에 푸시 알림만 포함되어 있고 사용자가 첫 번째 단계를 받은 후 푸시를 수신 거부하면 해당 사용자는 Canvas에서 이탈합니다. 대체 사용자 여정을 추가하려면 [다양한 캔버스 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/)를 사용하는 것을 고려하세요.

### 오디언스 세분화 {#segmenting-your-audience}

타겟 오디언스에 대해 다음 질문을 고려하세요:

- 올바른 Segment를 선택했나요?
- Segment가 어떻게 설정되어 있나요?
- Segment에 사용자가 포함되어 있는지 확인했나요?
- Canvas에 진입하는 사용자 수를 제한하는 추가 필터를 추가했나요?
- 사용자가 배리언트의 첫 번째 단계를 받을 자격이 있나요? 예를 들어, Canvas의 첫 번째 단계가 푸시 알림인데 진입 오디언스가 모두 푸시 비활성화 상태라면 어떤 사용자도 메시지를 받지 못합니다.

## 발송 또는 전달 수가 타겟 오디언스 크기보다 적은 이유는 무엇인가요? {#why-are-sends-or-deliveries-lower-than-my-target-audience-size}

발송 또는 전달된 메시지 수는 예상 오디언스 또는 수신자 수와 다른 경우가 많습니다. 일반적인 이유는 다음과 같습니다:

- **오디언스 재평가:** 사용자가 단계에 진입한 시점과 메시지가 발송되는 시점 사이에 Segment에서 이탈할 수 있습니다.
- **채널 자격:** 사용자에게 해당 단계의 채널에 필요한 이메일 주소, 푸시 토큰 또는 구독 상태가 없을 수 있습니다.
- **대조군:** 글로벌 또는 Canvas 대조군이 사용자의 메시지 수신을 보류할 수 있습니다.
- **방해금지 시간, Intelligent Timing 및 사용량 제한:** 이러한 설정으로 인해 발송이 지연되거나 억제될 수 있습니다.
- **인앱 메시지 단계:** 인앱 메시지는 노출 횟수가 존재하는데도 _발송_ 수가 0으로 표시될 수 있습니다. 이는 인앱 전달이 푸시 알림이나 이메일과 다르게 작동하기 때문에 예상되는 동작입니다. Canvas FAQ의 [Canvas에서 노출 횟수가 기록되었는데 발송 수가 0으로 표시되는 이유는 무엇인가요?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged)를 참조하세요.

이메일 및 기타 채널의 경우, Campaigns와 동일한 요인이 많이 적용됩니다. 자세한 목록은 [발송 수가 예상 오디언스 크기보다 적은 이유는 무엇인가요?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size)를 참조하세요.

## 일광 절약 시간제 전환일에 매일 스케줄된 Canvas에 사용자가 진입하지 않은 이유는 무엇인가요? {#why-did-no-users-enter-my-daily-scheduled-canvas-on-daylight-saving-time-day}

일광 절약 시간제(DST) 전환일에는 매일 스케줄된 Canvas가 평소보다 최대 1시간 일찍 또는 늦게 실행될 수 있습니다. 진입 기준이 스케줄된 진입 시간으로부터 1시간 이내의 타임스탬프를 가진 커스텀 속성이나 이벤트에 의존하는 경우, 속성이나 이벤트가 아직 기록되지 않아 DST 전환일에 사용자가 자격을 충족하지 못할 수 있습니다.

예를 들어, 사용자가 일반적으로 Canvas의 시간대 기준 오후 3시에 커스텀 속성 업데이트를 받고, Canvas가 같은 시간대의 오후 3시 30분에 매일 실행된다고 가정합니다. 봄철 시간 앞당김 DST 전환일에는 Canvas가 해당 속성 업데이트 기준으로 평소보다 최대 1시간 일찍 사용자를 평가할 수 있으며, 이는 속성이 기록되기 전입니다. 재진입 자격이 꺼져 있으면 이전에 진입한 사용자는 다시 진입할 수 없어 해당 날의 진입 수가 0이 됩니다.

이를 방지하려면 커스텀 속성 또는 이벤트 업데이트가 Canvas의 스케줄된 진입 시간보다 1시간 이상 전에 발생하도록 하세요.

## 대조군과 배리언트 그룹 간에 오디언스가 균등하게 분할되지 않은 이유는 무엇인가요? {#why-didnt-my-audience-split-evenly-between-the-control-group-and-variant-group}

Canvas를 생성할 때 다음 [사용 사례](#use-case)처럼 오디언스가 대조군과 배리언트 그룹 간에 균등하게 분할될 것으로 예상했을 수 있습니다. 그 이유와 해결 방법을 알아보겠습니다!

대조군 및 배리언트 할당은 Segment 필터가 아니라 빌더에서 설정한 비율에 따라 Canvas 진입 시 이루어집니다. 사용자는 [진입 단계]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule)에서 정의한 모든 기준에 부합할 때 Canvas에 진입합니다.

사용자가 배리언트에 진입했지만 채널 자격이 없어 메시지를 받지 못하는 경우, **타겟 오디언스**에 채널 필터를 추가하는 대신 각 단계의 [발송 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-14-select-your-send-settings)(예: **구독 설정**을 옵트인한 사용자로만 설정)을 사용하세요. 멀티채널 Canvas의 경우, 진입 오디언스를 단일 채널(예: **Foreground Push Enabled**)로 제한하지 마세요.

특정 채널을 수신할 수 없는 사용자도 여전히 배리언트에 진입할 수 있습니다. 각 메시지 유형을 수신하는 사용자를 제한하려면 진입 오디언스 필터 대신 단계별 발송 설정을 사용하세요.

### 사용 사례 {#use-case}

다음 시나리오를 가정해 보겠습니다:
- Canvas에 단일 배리언트와 대조군이 있습니다.
- 배리언트의 첫 번째 단계는 푸시 알림입니다.
- 90%의 사용자가 배리언트에 진입하도록, 10%가 대조군에 진입하도록 선택되었습니다.

![90% 배리언트와 10% 대조군이 있는 Canvas 예시.]({% image_buster /assets/img_archive/trouble15.png %})

이 시나리오에서는 Canvas에 진입하는 사용자의 90%가 배리언트에 진입합니다.

활성 사용자를 다시 살펴보면, 29.8k명의 사용자가 포함되어 있지만 그 중 64%만 푸시가 활성화되어 있음을 알 수 있습니다:

!["Push Enabled" 필터가 "true"로 설정되어 있고 예상 사용자가 29.8k인 Segment.]({% image_buster /assets/img_archive/trouble16.png %})

이는 90%의 사용자가 배리언트에 진입하도록 지정했더라도 해당 사용자 모두가 실제로 푸시 알림을 받을 수 있는 것은 아니라는 것을 의미합니다. 푸시 알림을 받을 수 없는 사용자도 여전히 배리언트에 진입하게 됩니다.

## 실행 기반 단계와 커스텀 이벤트 등록정보 {#action-based-steps-and-custom-event-properties}

실행 기반 Canvas 또는 행동 경로가 예상대로 발송되지 않는 경우, 고객 프로필의 커스텀 이벤트가 등록정보 필터를 포함한 트리거 구성과 일치하는지 확인하세요. Braze는 이벤트와 함께 전송된 정확한 등록정보를 평가하며, 등록정보가 누락되었거나 값이 필터와 일치하지 않으면 사용자가 진행되지 않습니다.

사용자가 오디언스 자격을 충족하기 전이나 너무 일찍 발생한 이벤트는 해당 단계를 트리거하지 않으므로, Canvas 시작 시점, [진입 스케줄]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types), 그리고 단계 전 스케줄된 지연을 기준으로 이벤트의 타임스탬프를 확인하세요.

{% alert note %}
Canvas의 인앱 메시지는 SDK의 이벤트로만 트리거할 수 있으며, REST API로는 트리거할 수 없습니다. [사용자가 트리거된 캔버스 단계를 받지 못한 이유는 무엇인가요?](#why-did-a-user-not-receive-a-triggered-canvas-step)를 참조하세요.
{% endalert %}

## Canvas 편집기가 멈추거나 로드되지 않는 이유는 무엇인가요? {#why-is-the-canvas-editor-freezing-or-not-loading}

많은 분기나 배리언트, 많은 단계 또는 매우 넓은 플로우가 있는 크고 복잡한 Canvas를 편집하는 경우 편집기가 로드되지 않거나 멈출 수 있습니다. 이 경우 다음을 권장합니다:

- 브라우저 캐시와 쿠키를 지운 다음 페이지를 새로고침하세요. 회사 광고 차단기나 브라우저 확장 프로그램을 사용하는 경우 Braze 플랫폼에 간섭할 수 있습니다.
- Canvas 확대/축소 컨트롤을 사용하여 보기를 25% 또는 10%로 줄이세요. 이렇게 하면 브라우저가 한 번에 렌더링해야 하는 UI의 양이 줄어듭니다.
- 다른 웹 브라우저를 사용해 보세요.