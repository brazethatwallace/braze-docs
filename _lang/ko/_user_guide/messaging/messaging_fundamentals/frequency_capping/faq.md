---
nav_title: FAQ
article_title: 사용량 제한 및 최대 게재빈도 설정 FAQ
page_order: 0
page_type: FAQ
description: "이 문서에서는 사용량 제한 및 최대 게재빈도 설정에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
tool: Campaigns

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 사용량 제한 및 최대 게재빈도 설정에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

### 활성 Canvas에서 발송 스로틀을 변경하면 이미 Canvas에 있는 사용자에게 영향을 미치나요? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

네, Canvas 사용량 제한을 늘리거나 줄이면 업데이트된 제한이 새 메시지에 적용됩니다. 업데이트가 Canvas 전체에 반영되기까지 약간의 지연이 있을 수 있습니다.

### 사용자가 Canvas 메시지 단계에 도달했지만 글로벌 최대 게재빈도를 초과한 경우 어떻게 되나요? {#what-happens-if-a-user-reaches-a-canvas-message-step-but-is-over-the-global-frequency-cap}

해당 사용자는 제한된 채널에 대한 발송을 수신하지 않지만, 메시지 단계 진행 규칙은 계속 따릅니다. 메시지 단계는 글로벌 최대 게재빈도 설정으로 인해 메시지가 발송되지 않은 경우에도 사용자를 진행시키므로, 다음 캔버스 단계로 계속 이동합니다. 진행 사례의 전체 목록은 [사용자 진행 방식]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#how-users-advance)을 참조하세요.

### Canvas에서 최대 게재빈도가 적용된 사용자를 어떻게 식별할 수 있나요? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

최대 게재빈도가 적용된 사용자는 해당 단계에 대한 발송 이벤트를 생성하지 않습니다. 이러한 사용자를 식별하려면 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)를 사용하여 `abort_type`이 `frequency_capped`인 메시지 중단 이벤트를 추적할 수 있습니다. 또는 [Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)을 생성하여 Canvas에 진입했지만 예상 메시지를 수신하지 못한 사용자를 분석할 수 있습니다.

### "일별" 글로벌 최대 게재빈도에서 캘린더 일수와 시간대는 어떻게 사용되나요? {#how-are-calendar-days-and-time-zones-used-for-per-day-global-frequency-caps}

글로벌 최대 게재빈도 설정은 사용자의 시간대를 사용하며, 연속 24시간이 아닌 캘린더 일수 기준으로 계산합니다. 예시는 [전달 규칙]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules)을 참조하세요.

### 글로벌 최대 게재빈도 설정이 트리거된 인앱 메시지에 적용되나요? {#does-global-frequency-capping-apply-to-triggered-in-app-messages}

아니요, 글로벌 최대 게재빈도 설정은 푸시, 이메일, SMS, 웹훅, WhatsApp 및 LINE 메시지에만 적용됩니다.

### 최대 게재빈도 설정은 수신한 Campaign 수를 제한하나요, 아니면 발송 내 개별 메시지를 제한하나요? {#does-frequency-capping-limit-campaigns-received-or-individual-messages-inside-a-send}

최대 게재빈도 설정은 디스패치 단위로 적용됩니다. 각 Campaign 또는 캔버스 단계 발송이 제한에 포함되며, 발송 내 각 배리언트나 플랫폼이 아닙니다. 자세한 내용은 [전달 규칙]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules)을 참조하세요.

### 여러 메시지가 동시에 적격하고 일부만 제한 내에 해당하는 경우 어떤 메시지가 발송되나요? {#if-several-messages-are-eligible-at-the-same-time-and-only-some-fit-under-the-cap-which-messages-send}

Braze는 제한까지 발송합니다. 동일한 기간 내에 여러 발송이 경합하는 경우, 먼저 처리된 메시지가 제한에 포함됩니다. 해당 기간 내 나머지 발송은 제한이 적용됩니다.

### 실패한 웹훅이 글로벌 최대 게재빈도에 포함되나요? {#do-failed-webhooks-count-toward-the-global-frequency-cap}

아니요. 웹훅은 Braze가 성공적인 전달을 기록할 때 제한에 포함됩니다. 실패한 웹훅 응답(예: `4xx` 또는 `5xx` 상태 코드)은 제한에 포함되지 않습니다.