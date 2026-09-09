---
nav_title: 문제 해결
article_title: Canvas 문제 해결
page_order: 7
page_type: reference
description: "표준 조사 경로, 증상 색인, 메시징 기록 및 메시징 진단 대시보드 링크를 사용하여 Canvas 진입, 발송 및 분석 문제를 진단합니다."
tool: Canvas
---

# Canvas 문제 해결 {#troubleshoot-canvases}

> 이 페이지를 사용하여 Canvas 진입, 발송 및 분석 문제를 진단하세요. 정의 및 심층 분석은 [Canvas FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs)를 참조하세요.

{% alert note %}
**메시징 기록** 및 **메시징 진단** 로그는 이벤트 발생 후 최대 **30일** 동안 사용할 수 있습니다. 특정 인시던트 조사에 도움이 필요한 경우 해당 기간 내에 [Braze 고객지원](#standard-investigation-path)에 문의하세요.
{% endalert %}

## 시작하기: 증상 매칭 {#start-here-match-your-symptom}

| 증상 | 이동 |
| --- | --- |
| 사용자가 Canvas에 진입하지 않음 | [사용자가 Canvas에 진입하지 않음](#user-didnt-enter-the-canvas) |
| 사용자가 진입했지만 메시지나 단계를 받지 못함 | [사용자가 Canvas 메시지 또는 단계를 받지 못함](#user-didnt-receive-a-canvas-message-or-step) |
| 예상보다 적거나 아무도 진입하지 않음 | [Canvas 진입 수가 낮거나 0임](#low-or-zero-canvas-entries) |
| 발송 또는 전달 수가 예상 오디언스보다 적음 | [예상보다 낮은 발송 수](#lower-sends-than-expected) |
| Canvas 분석이 잘못됨 (대조군, 전환, 발송 0건) | [Canvas 분석 불일치](#canvas-analytics-mismatches) |
| 분석에서 진입 수보다 발송 수가 많거나 종료 수가 많게 표시됨 | [날짜 범위 필터링으로 인해 예기치 않은 수치가 표시될 수 있음](#date-range-filtering-can-show-unexpected-numbers) |
| Canvas가 저장되지 않거나 편집기가 멈춤 | [편집기 및 저장 문제](#editor-and-save-issues) |
| 캔버스 배리언트를 삭제할 수 없음 | [보관된 Segment로 인해 캔버스 배리언트를 삭제할 수 없음](#cant-delete-a-canvas-variant-because-of-an-archived-segment) |
| Canvas를 중지했지만 메시지가 계속 발송됨 | [중지된 Canvas 동작](#stopped-canvas-behavior) |
| 시작 시 "Too many Canvas branches" 오류 발생 | ["Too many Canvas branches" 오류](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas 증상" }

## 표준 조사 경로 {#standard-investigation-path}

이 워크플로를 사용하여 특정 사용자 또는 종합적인 발송 문제를 조사하세요. 모든 인시던트에 대해 1단계부터 시작하세요.

1. Canvas가 활성 상태인지 확인하세요(초안, 중지됨 또는 보관됨이 아닌지).
2. 진입 스케줄(예약된 기간, 시간대, 실행 기반 트리거 또는 API 트리거 진입)이 사용자가 진입할 것으로 예상하는 시점과 일치하는지 확인하세요.
3. **오디언스** > **사용자 검색**으로 이동하여 프로필을 열고 **메시징 기록**(최근 30일)을 선택하여 사용자의 메시징 기록을 확인하세요.
   - 예상 발송 시간에 대한 기록이 없으면 문제는 메시지가 아니라 진입에 있습니다. [사용자가 Canvas에 진입하지 않음](#user-didnt-enter-the-canvas)으로 이동하세요.
4. Canvas **체인지로그** 및 타겟팅에 사용된 Segment의 체인지로그를 확인하세요. 인시던트 중에 오디언스, 단계 또는 발송 설정이 변경되지 않았는지 확인하세요.
5. [메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)를 열고 중단 및 드롭 사유를 검토하여 Canvas 분석 페이지에서 종합 결과를 확인하세요.
   - 인식할 수 없는 결과가 보이면 진단 문서의 [중단 결과]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes)를 참조하세요.
   - 단계에 진입 수가 0(발송 수가 0이 아닌)으로 표시되면 이전 단계 유형([행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 또는 [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split))을 확인하세요.
6. 여전히 해결되지 않으면 Canvas ID, 영향을 받은 사용자 ID, 타임스탬프(시간대 포함), 메시징 기록 또는 메시징 진단의 스크린샷과 함께 30일 이내에 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.

출시 전에 [테스트 Canvas 발송]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) 및 [사용자 경로 미리보기]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)를 사용하여 설정을 검증하세요.

## 사용자가 Canvas에 진입하지 않은 경우 {#user-didnt-enter-the-canvas}

**증상:** 예상한 시점에 사용자가 Canvas에 진입하지 않았거나, 트리거 이벤트 수에 비해 진입한 사용자가 더 적습니다.

사용자는 Braze가 진입 트리거를 평가하기 전에 **타겟 오디언스**에 일치해야 합니다([속성 변경]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value) 트리거 제외). 트리거만으로는 평가 시점에 사용자가 오디언스에 포함되어 있지 않으면 진입이 보장되지 않습니다.

재자격과 재진입은 [진입 제어 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)에서 별도로 제어됩니다:

- **재자격:** 사용자가 Canvas를 종료한 후 다시 진입할 수 있는지 여부를 결정합니다(시간 창 및 **사용자가 Canvas에 다시 진입할 수 있도록 허용** 설정).
- **재진입:** 현재 Canvas 내에 있는 사용자가 동시에 다른 경로에 진입할 수 있는지 여부를 결정합니다.

사용자가 재자격이 있더라도 아직 Canvas 내에 있어서 차단될 수 있고, Canvas를 종료했더라도 재자격 기간 이내에 있을 수 있습니다. 사용자가 Canvas에 다시 진입하지 못하는 경우 두 설정을 모두 확인하세요.

다음 사항을 확인하세요:

- **진입 스케줄 및 시간대:** Canvas가 활성 상태였는지, 사용자가 [진입 기간]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) 중에 트리거를 수행했는지 확인하세요.
- **평가 시점의 타겟 오디언스:** Segment 및 필터 변경 로그를 검토하세요. [사용자 조회]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)는 일부 필터 유형(예: 문자열 형식의 날짜 속성)에서 오탐(false positive)을 표시할 수 있습니다.
- **진입 상한:** [최대 진입 수]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) 또는 오디언스 상한에 도달했을 수 있습니다.
- **글로벌 컨트롤 그룹:** [글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/audience/global_control_group)에 포함된 사용자는 메시징 Canvases에 진입하지 않습니다.
- **Canvas 대조군:** 진입 시 Canvas 대조군에 배정된 사용자는 배리언트 메시지를 수신하지 않습니다. 배리언트 배정은 Segment 필터가 아닌 진입 시점에 이루어집니다. [Canvas 분석 불일치](#canvas-analytics-mismatches)를 참조하세요.
- **이탈 기준:** 사용자가 진입 전 또는 진입 중에 [이탈 기준]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)에 일치했을 수 있습니다. 진입과 이탈에 동일한 이벤트를 사용하는 경우, [진입 및 이탈 기준 매칭]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria)을 참조하세요.
- **API 트리거 진입:** [`/canvas/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)로 사용자가 추가되었는지 확인하세요. Canvas 진입 필터로 [Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)하고 [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)로 사용자를 내보낼 수 있습니다.

### 트리거 이벤트 수가 Canvas 진입 수보다 많은 경우 {#trigger-event-count-is-higher-than-canvas-entries}

**증상:** 트리거 이벤트 수가 Canvas 진입 수보다 많습니다.

Braze는 동일한 순간에 발생하는 여러 진입 시도를 중복 제거하므로, 트리거 이벤트 수보다 Canvas 진입 수가 적을 수 있습니다. 여러 진입을 테스트하려면 트리거 이벤트 간격을 최소 1초 이상 두세요.

사용자가 1초 이내에 동일한 트리거를 여러 번 수행하면 Braze는 한 번의 진입만 처리합니다. 재진입 또는 재자격 규칙이 적용되는 경우 메시징 진단에서 **사용자 재자격 없음** 등의 결과를 확인하세요.

{% details 일광 절약 시간(DST)과 일별 예약 Canvases %}

일광 절약 시간(DST) 전환일에는 일별 예약 Canvases가 평소보다 최대 1시간 일찍 또는 늦게 실행될 수 있습니다. 진입 기준이 예약 진입 시간에서 1시간 이내의 타임스탬프를 가진 커스텀 속성 또는 이벤트에 의존하는 경우, 해당 속성이나 이벤트가 아직 기록되지 않아 DST 전환일에 사용자가 자격을 갖추지 못할 수 있습니다.

예를 들어, 사용자가 보통 Canvas 시간대 기준 오후 3시에 커스텀 속성 업데이트를 받고, Canvas가 동일한 시간대에서 매일 오후 3시 30분에 실행된다고 가정합니다. 봄철 DST 전환일에는 Canvas가 해당 속성 업데이트 대비 평소보다 최대 1시간 일찍 사용자를 평가할 수 있으며, 이때 속성이 아직 기록되지 않은 상태입니다. 재자격이 비활성화된 경우 이전에 진입한 사용자는 다시 진입할 수 없어 해당 날의 진입 수가 0이 될 수 있습니다.

이를 방지하려면 커스텀 속성 또는 이벤트 업데이트가 Canvas의 예약 진입 시간보다 1시간 이상 전에 발생하도록 하세요.

{% enddetails %}

## 사용자가 Canvas 메시지 또는 단계를 받지 못한 경우 {#user-didnt-receive-a-canvas-message-or-step}

**증상:** 사용자가 Canvas에 진입했지만 예상되는 메시지나 단계를 받지 못했습니다.

해당 Canvas 단계와 타임스탬프에 대해 사용자의 [**메시징 기록**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)을 확인하세요. 기록이 없으면 [사용자가 Canvas에 진입하지 못한 경우](#user-didnt-enter-the-canvas)로 돌아가세요.

그런 다음 트리거 또는 단계 유형별로 다음을 확인하세요:

- **커스텀 이벤트 또는 구매 트리거:** **Analytics** > **Custom Events Report**(구매의 경우 **Revenue**)에서 이벤트가 표시되는지 확인하세요. 이벤트 타임스탬프를 Canvas가 활성화된 시점 및 해당 단계에 설정된 예약 지연과 비교하세요.
- **API 트리거 진입:** [사용자가 Canvas에 진입하지 못한 경우](#user-didnt-enter-the-canvas)에 설명된 대로 Canvas Segment 필터 및 내보내기를 사용하여 진입을 확인하세요.
- **작업 경로 또는 메시지 단계 트리거:** 사용자가 필수 이벤트를 수행했으며 해당 단계에서 [이벤트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties)를 사용할 수 있는지 확인하세요.
- **인앱 메시지 단계:** 인앱 메시지는 사용자가 단계에 진입한 후 다음 세션 시작 시 발송되며, SDK 이벤트에서만 발송됩니다(REST API에서는 발송되지 않음). Canvas FAQ의 [Canvas에서 인앱 메시지는 언제 발송되나요?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent)를 참조하세요.
- **Canvas 대조군:** 사용자가 진입 시 Canvas 대조군에 배정되지 않았는지 확인하세요.
- **채널 자격 및 발송 설정:** 구독 상태, 푸시 활성화 상태, 단계별 [발송 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)(예: **Subscription Settings**가 수신 동의한 사용자로만 설정)을 확인하세요. 멀티 채널 Canvases의 **타겟 오디언스**에 단일 채널 필터를 추가하지 마세요.
- **전달 유효성 검사:** 메시지 단계에서 **발송 시 오디언스 검증**을 활성화한 경우, 발송 시점에 더 이상 필터에 일치하지 않는 사용자는 메시지를 받지 못합니다. [전달 유효성 검사]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)를 참조하세요.
- **방해금지 시간, Intelligent Timing, 빈도 제한 및 사용량 제한:** 이러한 설정은 발송을 지연, 억제 또는 중단시킬 수 있습니다. 방해금지 시간으로 인해 발송이 중단된 후에도 사용자가 Canvas에 남아 있을 수 있습니다.
- **경합 조건:** 사용자가 여러 작업을 동시에 트리거한 경우 [경합 조건]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)을 참조하세요.

{% alert important %}
Canvas 메시지 단계에서 발송이 중단되더라도 사용자는 다음 단계로 계속 진행합니다. Canvas는 중단 시에도 진행하여 이후의 지연 및 작업 경로 단계가 영구적으로 차단되지 않도록 합니다. [사용자가 진행하는 방법]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) 및 [중단 결과]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes)를 참조하세요.
{% endalert %}

단계 수준 필터, 브랜치 간 충돌 및 인앱 메시지 브랜치 동작에 대해서는 [Canvas Flow로 실행 — 문제 해결]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) 및 [Canvas FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery)를 참조하세요.

{% alert important %}
실행 기반 Canvas가 예상보다 일찍 메시지를 발송하는 경우, 커스텀 이벤트 타임스탬프가 소급된 시간이 아닌 현재 시간을 사용하는지 확인하세요. Braze는 이벤트와 함께 전송된 타임스탬프를 기준으로 지연을 평가합니다. [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)을 참조하세요.
{% endalert %}

## Canvas 진입 수가 낮거나 0인 경우 {#low-or-zero-canvas-entries}

**증상:** Canvas에 아무도 진입하지 않거나 예상보다 적은 사용자가 진입했습니다.

[Canvas Flow 출시 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist)부터 시작한 다음 다음 사항을 확인하세요:

- Canvas가 활성 상태이고 현재 시간이 예약된 진입 기간 내에 있는지 확인합니다.
- [진입 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)(재적격성, 최대 진입 수, 진입 한도)이 진입을 기대하는 사용자를 허용하는지 확인합니다.
- 타겟 오디언스 및 Segment 필터가 출시 이후에도 여전히 기대하는 사용자와 일치하는지 확인합니다.
- 글로벌 및 Canvas 대조군 비율을 통해 사용자가 각 경로에 진입하는 비율과 메시지를 수신하는 비율을 확인합니다.
- 워크스페이스 사용량 제한 또는 진입 대기줄이 사용자가 자격을 충족하는 시점과 실제로 단계에 진입하거나 진행하는 시점 사이에 지연을 추가할 것으로 예상되는지 확인합니다.

단일 사용자의 경우 [표준 조사 경로]({{site.baseurl}}/user_guide/administer/personal/braze_support)를 따르세요. DST 관련 진입 0건 문제는 [사용자가 Canvas에 진입하지 않음](#user-didnt-enter-the-canvas)에서 접기 섹션을 참조하세요.

## 예상보다 낮은 발송 수 {#lower-sends-than-expected}

**증상:** Canvas 단계에서 발송 또는 전달 수가 예상 오디언스보다 낮습니다.

일반적인 원인으로는 발송 시점의 오디언스 재평가, 채널 자격, 대조군, 방해금지 시간, Intelligent Timing, 사용량 제한, 인앱 메시지 전달 동작(인앱 메시지의 경우 노출 횟수가 있으면서 _발송_ 수가 0인 것은 정상입니다) 등이 있습니다.

메시지 단계에서 많은 사용자가 진입했지만 발송 수가 적은 경우, Liquid `abort_message()`가 발송을 취소했는지 확인하세요. 메시지 활동 로그 확인, 누락된 속성, 테스트 발송에 대해서는 [높은 중단율 문제 해결]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates)을 참조하세요.

자세한 목록은 Canvas FAQ의 [발송 수가 예상 오디언스 크기보다 낮은 이유는 무엇인가요?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) 및 Campaigns에 대한 [발송 수가 예상 오디언스 크기보다 낮은 이유는 무엇인가요?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)를 참조하세요.

[메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)를 사용하여 단계 수준에서 중단 및 드롭 사유를 확인하세요.

## Canvas 분석 불일치 {#canvas-analytics-mismatches}

**증상:** Canvas 분석이 잘못된 것처럼 보입니다(대조군 분할, 전환 또는 발송 건수 0).

대조군 및 배리언트 배정은 빌더에서 설정한 비율을 기반으로 Canvas 진입 시 이루어지며, Segment 필터를 통해 수행되지 않습니다. 특정 채널을 수신할 수 없는 사용자도 배리언트에 진입할 수 있습니다. 채널 필터로 **타겟 오디언스**를 좁히는 대신 단계별 [발송 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)을 사용하여 각 메시지 유형을 수신할 사용자를 제한하세요.

Canvas 대조군을 [글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/audience/global_control_group)과 구별하세요. 필터 정의에 대해서는 Canvas FAQ의 ["Canvas 배리언트에 진입하지 않음"과 "Canvas 대조군에 속하지 않음"의 차이점은 무엇인가요?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group)를 참조하세요.

{% details 배리언트 발송 건수가 배리언트 비율보다 낮을 수 있는 이유 %}

다음과 같은 시나리오를 가정해 보겠습니다:

- Canvas에 단일 배리언트와 대조군이 있습니다.
- 배리언트의 첫 번째 단계는 푸시 알림입니다.
- 90%의 사용자가 배리언트에 진입하도록 선택되었고, 10%가 대조군에 진입하도록 선택되었습니다.

![90% 배리언트와 10% 대조군이 있는 Canvas 예시.]({% image_buster /assets/img_archive/trouble15.png %})

이 시나리오에서 Canvas에 진입하는 사용자의 90%가 배리언트에 진입합니다.

활성 사용자 Segment를 보면, 29.8k명의 사용자가 포함되어 있지만 그 중 64%만 푸시가 활성화되어 있는 것을 확인할 수 있습니다:

![푸시 활성화 필터가 true로 설정되어 있고 추정 사용자가 29.8k인 Segment.]({% image_buster /assets/img_archive/trouble16.png %})

즉, 사용자의 90%가 배리언트에 진입하도록 지정했더라도 모든 사용자가 푸시 알림을 수신할 수 있는 것은 아닙니다. 푸시를 수신할 수 없는 사용자도 배리언트에 진입합니다. 발송 건수는 진입 시 배리언트 배정이 아닌 해당 단계에서의 채널 수신 자격을 반영합니다.

{% enddetails %}

### 날짜 범위 필터링으로 인해 예상치 못한 수치가 표시될 수 있음 {#date-range-filtering-can-show-unexpected-numbers}

**증상:** Canvas 또는 단계 분석에서 진입 수보다 훨씬 많은 발송 건수가 표시되거나, 진입한 사용자보다 더 많은 사용자가 단계를 이탈하는 등 예상치 못하거나 비합리적인 수치가 나타납니다.

이는 Canvas 분석 페이지 상단의 날짜 범위 캘린더 필터를 사용할 때 발생할 수 있습니다. 일부 사용자 행동이 제외되는 날짜 범위를 선택하면, 표시되는 측정기준이 각 사용자 여정의 일부만 보여줄 수 있습니다.

예를 들어:
- 날짜 범위가 대부분의 사용자가 진입한 이후부터 시작하지만 메시지를 수신한 시점을 포함하는 경우, 100건의 진입에 8,000건의 발송이 표시될 수 있습니다.
- 날짜 범위가 이탈만 캡처하고 이전 진입을 포함하지 않는 경우, 이전 단계에 진입한 것보다 더 많은 사용자가 다음 단계로 이동한 것처럼 보일 수 있습니다.

이를 해결하려면 Canvas가 시작된 날부터 현재까지의 모든 날짜를 포함하도록 날짜 범위를 조정하거나, 필요한 측정기준과 관련된 전체 기간을 포괄하는 범위를 선택하세요.

전환율 정의 및 단계별 분석에 대해서는 Canvas FAQ의 [분석 및 전환]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions)을 참조하세요.

## 편집기 및 저장 문제 {#editor-and-save-issues}

**증상:** Canvas 편집기가 로드되지 않거나, 멈추거나, 변경 사항이 저장되지 않습니다.

| 증상 | 가장 가능성 높은 원인 |
| --- | --- |
| 저장 버튼이 오류 없이 무한으로 회전함 | Canvas 오디언스 또는 단계 필터에 비어 있거나 불완전한 커스텀 속성 필터가 있음 — 필터를 제거하거나 유효한 속성을 선택하세요 |
| 편집 중 "Request Timed Out" 오류 | 브라우저 확장 프로그램 간섭, 광고 차단기 또는 만료된 세션 — 시크릿 창이나 다른 브라우저에서 시도하세요 |
| 배리언트를 보관한 후 저장할 수 없음 | 보관된 배리언트가 다운스트림에서 여전히 참조되고 있음; 단계 연결을 검토하고 해당 배리언트를 복원하거나 교체하세요 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="편집기 증상" }

대규모이거나 복잡한 Canvas에서 편집기가 멈추는 경우, 다음을 시도해 보세요:

- 브라우저 캐시와 쿠키를 삭제한 후 페이지를 다시 로드하세요. 회사 광고 차단기나 브라우저 확장 프로그램이 Braze 플랫폼을 방해할 수 있습니다.
- Canvas 확대/축소 컨트롤을 사용하여 보기를 25% 또는 10%로 줄여 브라우저가 렌더링해야 하는 UI 양을 줄이세요.
- 다른 웹 브라우저를 사용해 보세요.

Canvas가 로드되지 않고 진행되지 않는 경우, 이전 버전이 올바르게 저장되지 않았으며 유효하지 않은 단계를 포함하고 있을 수 있습니다. 대시보드에서 Canvas를 복제하세요. 문제가 지속되면 [고객지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 열어 주세요.

"Request Timed Out" 고객지원 티켓을 제출할 때는 화면 녹화, 타임스탬프와 시간대, 브라우저 및 버전, 재현 단계, 그리고 선택적으로 브라우저 개발자 도구에서 생성한 HAR 로그를 포함하세요. Canvas FAQ의 ["Request Timed Out" 오류에 대한 고객지원 티켓을 제출할 때 무엇을 포함해야 하나요?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error)를 참조하세요.

{% multi_lang_include audience/segments.md section='Canvas variant archived segment' %}

## 중지된 Canvas 동작 {#stopped-canvas-behavior}

**증상:** Canvas를 중지했지만 사용자가 여전히 메시지를 수신합니다.

Canvas를 중지하면 사용자는 더 이상 진입할 수 없으며, Canvas 흐름에서 추가 메시지가 발송되지 않습니다. 이미 이메일 서비스 공급자에게 전달된 이메일 발송은 회수할 수 없습니다.

지연 또는 행동 경로 단계에서 대기 중인 사용자는 Canvas를 중지할 때 여정에서 자동으로 제거되지 않습니다. 예약된 발송 시간이 경과하기 전에 Canvas를 다시 활성화하면 대기 중인 단계가 계속 발송될 수 있습니다.

자세한 내용은 Canvas FAQ의 [Canvas를 중지하면 어떻게 되나요?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas)를 참조하세요.

## "Too many Canvas branches" 오류 {#too-many-canvas-branches-error}

**증상:** 예약된 Canvas를 시작할 때 "Too many Canvas branches" 오류가 표시됩니다.

이 오류는 단계 분기와 진입 오디언스 크기의 조합이 클러스터 성능 문제를 일으켜 메시지 발송을 방해할 수 있을 때 나타납니다. Braze는 예약된 진입이 있는 Canvas를 시작할 때 이 메시지를 표시하며, 초안을 저장할 때는 나타나지 않습니다.

해결 방법:

- Canvas에서 단계 분기를 줄이세요.
- 진입 오디언스 크기를 줄이세요.
- 여러 병렬 경로 대신 [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)를 사용하여 분기를 통합하세요.
- Canvas가 기존 편집기를 사용하는 경우, [Canvas Flow로 복제]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)하고 Canvas 구성 요소로 다시 구축하세요.

변경 없이 Canvas를 시작해야 하고 Canvas Flow로 전환할 수 없는 경우, [고객지원]({{site.baseurl}}/support_contact)에 문의하세요.

## 지원팀에 문의해야 할 때 {#when-to-contact-support}

[표준 조사 경로](#standard-investigation-path)를 완료한 후에도 도움이 필요한 경우, 문제 발생 후 30일 이내에 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.

다음 정보를 포함하세요:

- Canvas ID 및 영향을 받은 사용자 ID(외부 ID 또는 Braze ID)
- 시간대가 포함된 타임스탬프
- **Messaging History** 또는 **Messaging Diagnostics**의 스크린샷 또는 내보내기
- 편집기 "Request Timed Out" 오류의 경우, [편집기 및 저장 문제](#editor-and-save-issues)에 나열된 세부 정보