---
nav_title: Currents 이벤트 체인지로그
page_order: 6
description: "이 페이지에는 각 Currents 릴리스에 대한 이벤트 변경 사항이 포함되어 있습니다."
tool: Currents
---

# Currents 체인지로그 {#currents-changelog}

## 버전 12의 변경 사항 (출시일 2026-09-02) {#changes-in-version-12-release-date-2026-09-02}

### Storage 변경 사항: {#changes-for-storage}

* 이벤트 유형 `users.messages.email.Abort`의 필드 변경 사항:
    * 새 `string` 필드 `message_extras` 추가: [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열

* 이벤트 유형 `users.messages.email.Bounce`의 필드 변경 사항:
    * 새 `int` 필드 `send_time` 추가: 해당 전송 이벤트의 시간

* 이벤트 유형 `users.messages.email.Click`의 필드 변경 사항:
    * 새 `int` 필드 `send_time` 추가: 해당 전송 이벤트의 시간(초 단위)
    * 새 `boolean` 필드 `has_url_parameters` 추가: 클릭된 URL에 쿼리 파라미터가 포함되어 있는지 여부
    * 새 `boolean` 필드 `link_aliasing_enabled` 추가: 이 클릭이 처리될 때 워크스페이스에 링크 별칭 지정이 활성화되어 있었는지 여부

* 이벤트 유형 `users.messages.email.Deferral`의 필드 변경 사항:
    * 새 `int` 필드 `send_time` 추가: 해당 전송 이벤트의 시간

* 이벤트 유형 `users.messages.email.Delivery`의 필드 변경 사항:
    * 새 `int` 필드 `send_time` 추가: 해당 전송 이벤트의 시간

* 이벤트 유형 `users.messages.email.MarkAsSpam`의 필드 변경 사항:
    * 새 `int` 필드 `send_time` 추가: 해당 전송 이벤트의 시간

* 이벤트 유형 `users.messages.email.Open`의 필드 변경 사항:
    * 새 `int` 필드 `send_time` 추가: 해당 전송 이벤트의 시간

* 이벤트 유형 `users.messages.email.SoftBounce`의 필드 변경 사항:
    * 새 `int` 필드 `send_time` 추가: 해당 전송 이벤트의 시간

* 이벤트 유형 `users.messages.line.Abort`의 필드 변경 사항:
    * 새 `string` 필드 `message_extras` 추가: [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열

* 이벤트 유형 `users.messages.pushnotification.Abort`의 필드 변경 사항:
    * 새 `string` 필드 `message_extras` 추가: [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열

* 이벤트 유형 `users.messages.rcs.Abort`의 필드 변경 사항:
    * 새 `string` 필드 `message_extras` 추가: [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열

* 이벤트 유형 `users.messages.sms.Abort`의 필드 변경 사항:
    * 새 `string` 필드 `message_extras` 추가: [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열

* 이벤트 유형 `users.messages.webhook.Abort`의 필드 변경 사항:
    * 새 `string` 필드 `message_extras` 추가: [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열

* 이벤트 유형 `users.messages.whatsapp.Abort`의 필드 변경 사항:
    * 새 `string` 필드 `message_extras` 추가: [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열

## 버전 11의 변경 사항 (릴리스 날짜 2026-08-05) {#changes-in-version-11-release-date-2026-08-05}

### 스토리지 변경 사항:

* 새 이벤트 유형 `contentoptimizer.ComponentStore`가 추가되었습니다.

* 새 이벤트 유형 `users.canvas.costep.Conversion`이 추가되었습니다.

* 새 이벤트 유형 `users.messages.landingpage.Click`이 추가되었습니다.

* 새 이벤트 유형 `users.messages.landingpage.FormSubmission`이 추가되었습니다.

* 새 이벤트 유형 `users.messages.landingpage.Impression`이 추가되었습니다.

* 새 이벤트 유형 `users.messages.survey.Response`가 추가되었습니다.

* 이벤트 유형 `agentconsole.AgentExecuted`의 필드 변경 사항:
    * 새 `string` 필드 `thinking_level`이 추가되었습니다: 요청에 사용된 사고/추론 수준

* 이벤트 유형 `users.messages.banner.Click`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_unique`가 추가되었습니다: 해당 메시지 배리에이션에 대한 사용자의 첫 번째 클릭인지 여부로, 고유 클릭 통계에 반영됩니다

* 이벤트 유형 `users.messages.banner.Dismiss`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_unique`가 추가되었습니다: 해당 메시지 배리에이션에 대한 사용자의 첫 번째 닫기인지 여부로, 고유 닫기 통계에 반영됩니다

* 이벤트 유형 `users.messages.banner.Impression`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_unique`가 추가되었습니다: 해당 메시지 배리에이션에 대한 사용자의 첫 번째 노출인지 여부로, 고유 노출 횟수 통계에 반영됩니다

* 이벤트 유형 `users.messages.contentcard.Click`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_unique`가 추가되었습니다: 해당 메시지 배리에이션에 대한 사용자의 첫 번째 클릭인지 여부로, 고유 클릭 통계에 반영됩니다

* 이벤트 유형 `users.messages.contentcard.Dismiss`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_unique`가 추가되었습니다: 해당 메시지 배리에이션에 대한 사용자의 첫 번째 닫기인지 여부로, 고유 닫기 통계에 반영됩니다

* 이벤트 유형 `users.messages.contentcard.Impression`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_unique`가 추가되었습니다: 해당 메시지 배리에이션에 대한 사용자의 첫 번째 노출인지 여부로, 고유 노출 횟수 통계에 반영됩니다

* 이벤트 유형 `users.messages.featureflag.Impression`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_unique`가 추가되었습니다: 해당 기능 플래그에 대한 사용자의 첫 번째 노출인지 여부로, 고유 노출 횟수 통계에 반영됩니다

## 버전 10 변경 사항 (릴리스 날짜: 2026-07-01) {#changes-in-version-10-release-date-2026-07-01}

### Storage 변경 사항:

* 새 이벤트 유형 `users.canvas.costep.Send`가 추가되었습니다.

* 새 이벤트 유형 `users.UserDeleteRequest`가 추가되었습니다.

* 새 이벤트 유형 `users.UserOrphan`이 추가되었습니다.

* 이벤트 유형 `users.messages.rcs.Abort`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Click`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Delivery`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.InboundReceive`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Read`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Rejection`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Send`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

## 버전 9의 변경 사항 (릴리스 날짜 2026-06-03) {#changes-in-version-9-release-date-2026-06-03}

### Storage 변경 사항:

* 이벤트 유형 `users.messages.email.Send`의 필드 변경 사항:
    * 새 `string` 필드 `from_domain` 추가: 이메일의 발신 도메인

## 버전 8 변경 사항 (릴리스 날짜 2026-05-06) {#changes-in-version-8-release-date-2026-05-06}

### 스토리지 관련 변경 사항:

* 새로운 이벤트 유형 `users.messages.banner.Dismiss`가 추가되었습니다.

* 이벤트 유형 `users.messages.whatsapp.Abort`의 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid`가 추가되었습니다: 이 이벤트와 관련된 수신자의 WhatsApp 비즈니스 범위 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Delivery`의 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid`가 추가되었습니다: 이 이벤트와 관련된 수신자의 WhatsApp 비즈니스 범위 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Failure`의 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid`가 추가되었습니다: 이 이벤트와 관련된 수신자의 WhatsApp 비즈니스 범위 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.InboundReceive`의 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid`가 추가되었습니다: 메시지를 수신한 사용자의 WhatsApp 비즈니스 범위 사용자 ID입니다.
    * 필드 `user_phone_number`이 이제 *선택 사항*입니다.

* 이벤트 유형 `users.messages.whatsapp.Read`의 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid`가 추가되었습니다: 이 이벤트와 관련된 수신자의 WhatsApp 비즈니스 범위 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Retry`의 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid`가 추가되었습니다: 이 이벤트와 관련된 수신자의 WhatsApp 비즈니스 범위 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Send`의 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid`가 추가되었습니다: 이 이벤트와 관련된 수신자의 WhatsApp 비즈니스 범위 사용자 ID입니다.

## 버전 7 변경 사항 (릴리스 날짜 2026-04-01) {#changes-in-version-7-release-date-2026-04-01}

### Storage 변경 사항:

* 새로운 이벤트 유형 `users.profile.Update`가 추가되었습니다.

* 이벤트 유형 `users.messages.banner.Abort`의 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: Canvas의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 수신한 Canvas 배리에이션의 이름
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID
    * 새로운 `string` 필드 `canvas_step_id` 추가: 이 이벤트가 속한 캔버스 단계의 API ID
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 수신한 캔버스 단계 메시지 배리에이션의 API ID
    * 새로운 `string` 필드 `canvas_variation_id` 추가: 이 이벤트가 속한 Canvas 배리에이션의 API ID

* 이벤트 유형 `users.messages.banner.Click`의 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID
    * 새로운 `string` 필드 `canvas_step_id` 추가: 이 이벤트가 속한 캔버스 단계의 API ID
    * 새로운 `string` 필드 `canvas_name` 추가: Canvas의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 수신한 캔버스 단계 메시지 배리에이션의 API ID
    * 새로운 `string` 필드 `canvas_variation_id` 추가: 이 이벤트가 속한 Canvas 배리에이션의 API ID
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 수신한 Canvas 배리에이션의 이름

* 이벤트 유형 `users.messages.banner.Impression`의 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID
    * 새로운 `string` 필드 `canvas_step_id` 추가: 이 이벤트가 속한 캔버스 단계의 API ID
    * 새로운 `string` 필드 `canvas_name` 추가: Canvas의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 수신한 캔버스 단계 메시지 배리에이션의 API ID
    * 새로운 `string` 필드 `canvas_variation_id` 추가: 이 이벤트가 속한 Canvas 배리에이션의 API ID
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 수신한 Canvas 배리에이션의 이름

## 버전 6의 변경 사항 (릴리스 날짜 2026-03-04) {#changes-in-version-6-release-date-2026-03-04}

### 스토리지 변경 사항:

* 이벤트 유형 `agentconsole.AgentExecuted`의 필드 변경 사항:
    * 새로운 `string` 필드 `error` 추가: 오류 설명

* 이벤트 유형 `agentconsole.ToolInvocation`의 필드 변경 사항:
    * 새로운 `string` 필드 `request_id` 추가: 이 전체 LLM 요청 및 완전한 실행에 대한 고유 ID

* 이벤트 유형 `users.messages.rcs.InboundReceive`의 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 수신한 Canvas 배리에이션의 이름

## 버전 5 변경 사항 (릴리스 날짜 2026-02-04) {#changes-in-version-5-release-date-2026-02-04}

### Storage 변경 사항:

* 새 이벤트 유형 `agentconsole.AgentExecuted`가 추가되었습니다.

* 새 이벤트 유형 `agentconsole.ToolInvocation`이 추가되었습니다.

* 새 이벤트 유형 `users.messages.email.Retry`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.line.Retry`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.pushnotification.Retry`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.sms.Retry`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.webhook.Retry`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.whatsapp.Retry`가 추가되었습니다.

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`의 필드 변경 사항:
    * 새 `long` 필드 `time_ms`가 추가되었습니다: 이벤트가 발생한 시간(밀리초)

## 버전 4의 변경 사항 (출시일 2026-01-07) {#changes-in-version-4-release-date-2026-01-07}

### 스토리지 관련 변경 사항:

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`의 필드 변경 사항:
    * 새 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.pushnotification.Bounce`의 필드 변경 사항:
    * 새 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.pushnotification.Send`의 필드 변경 사항:
    * 새 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.rcs.Click`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 수신한 Canvas 배리에이션의 이름
    * 필드 `user_phone_number`이 이제 *선택 사항*입니다.

* 이벤트 유형 `users.messages.rcs.InboundReceive`의 필드 변경 사항:
    * 필드 `user_id`가 이제 *선택 사항*입니다.

* 이벤트 유형 `users.messages.rcs.Rejection`의 필드 변경 사항:
    * 새 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 수신한 캔버스 단계 메시지 배리에이션의 API ID

## 버전 3 변경 사항 (릴리스 날짜 2025-10-08) {#changes-in-version-3-release-date-2025-10-08}

### Storage 변경 사항:

* 새 이벤트 유형 `users.messages.line.Abort`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.line.Click`이 추가되었습니다.

* 새 이벤트 유형 `users.messages.line.InboundReceive`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.line.Send`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.rcs.Abort`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.rcs.Click`이 추가되었습니다.

* 새 이벤트 유형 `users.messages.rcs.Delivery`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.rcs.InboundReceive`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.rcs.Read`가 추가되었습니다.

* 새 이벤트 유형 `users.messages.rcs.Rejection`이 추가되었습니다.

* 새 이벤트 유형 `users.messages.rcs.Send`가 추가되었습니다.

* 이벤트 유형 `users.messages.sms.Delivery`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_sms_fallback` 추가: 거부된 RCS 메시지로 인해 단문 메시지 서비스 대체 메시지가 전송되었음을 나타냅니다. 이 메시지는 전달, 전달 실패 또는 거부가 될 수 있습니다. 전송 ID 및 디스패치 ID를 통해 RCS Rejection 이벤트와 연결할 수 있습니다.

* 이벤트 유형 `users.messages.sms.DeliveryFailure`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_sms_fallback` 추가: 거부된 RCS 메시지로 인해 단문 메시지 서비스 대체 메시지가 전송되었음을 나타냅니다. 이 메시지는 전달, 전달 실패 또는 거부가 될 수 있습니다. 전송 ID 및 디스패치 ID를 통해 RCS Rejection 이벤트와 연결할 수 있습니다.

* 이벤트 유형 `users.messages.sms.Rejection`의 필드 변경 사항:
    * 새 `boolean` 필드 `is_sms_fallback` 추가: 거부된 RCS 메시지로 인해 단문 메시지 서비스 대체 메시지가 전송되었음을 나타냅니다. 이 메시지는 전달, 전달 실패 또는 거부가 될 수 있습니다. 전송 ID 및 디스패치 ID를 통해 RCS Rejection 이벤트와 연결할 수 있습니다.

* 이벤트 유형 `users.messages.whatsapp.Delivery`의 필드 변경 사항:
    * 새 `string` 필드 `flow_id` 추가: WhatsApp 매니저에서 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하기 위한 CTA가 포함된 경우 존재합니다.
    * 새 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 전송하는 경우 존재합니다.
    * 새 `string` 필드 `message_id` 추가: Meta에서 이 메시지에 대해 생성한 고유 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Failure`의 필드 변경 사항:
    * 새 `string` 필드 `message_id` 추가: Meta에서 이 메시지에 대해 생성한 고유 ID입니다.
    * 새 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 전송하는 경우 존재합니다.
    * 새 `string` 필드 `flow_id` 추가: WhatsApp 매니저에서 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하기 위한 CTA가 포함된 경우 존재합니다.

* 이벤트 유형 `users.messages.whatsapp.InboundReceive`의 필드 변경 사항:
    * 새 `string` 필드 `catalog_id` 추가: 인바운드 메시지에서 제품이 참조된 경우 해당 제품의 카탈로그 ID입니다. 그렇지 않으면 비어 있습니다.
    * 새 `string` 필드 `product_id` 추가: 인바운드 메시지에서 제품이 참조된 경우 해당 제품의 SKU입니다. 그렇지 않으면 비어 있습니다.
    * 새 `string` 필드 `flow_id` 추가: WhatsApp 매니저에서 Flow의 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 존재합니다.
    * 새 `string` 필드 `flow_response_json` 추가: [PII] 사용자가 응답한 양식 값입니다. 사용자가 WhatsApp Flow에 응답하는 경우 존재합니다.
    * 새 `string` 필드 `message_id` 추가: Meta에서 이 메시지에 대해 생성한 고유 ID입니다.
    * 새 `string` 필드 `in_reply_to` 추가: 이 메시지가 답장한 원본 메시지의 message_id입니다.

* 이벤트 유형 `users.messages.whatsapp.Read`의 필드 변경 사항:
    * 새 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 전송하는 경우 존재합니다.
    * 새 `string` 필드 `message_id` 추가: Meta에서 이 메시지에 대해 생성한 고유 ID입니다.
    * 새 `string` 필드 `flow_id` 추가: WhatsApp 매니저에서 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하기 위한 CTA가 포함된 경우 존재합니다.

* 이벤트 유형 `users.messages.whatsapp.Send`의 필드 변경 사항:
    * 새 `string` 필드 `flow_id` 추가: WhatsApp 매니저에서 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하기 위한 CTA가 포함된 경우 존재합니다.
    * 새 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 전송하는 경우 존재합니다.
    * 새 `string` 필드 `message_id` 추가: Meta에서 이 메시지에 대해 생성한 고유 ID입니다.

## 버전 2 변경 사항 (출시일 미정) {#changes-in-version-2-release-date-null}

### Storage 변경 사항:

* 새로운 이벤트 유형 `users.behaviors.app.FirstSession`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.app.SessionEnd`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.app.SessionStart`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.CustomEvent`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.InstallAttribution`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.liveactivity.PushToStartTokenChange`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.liveactivity.UpdateTokenChange`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Location`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Purchase`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.subscription.GlobalStateChange`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.subscriptiongroup.StateChange`가 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Uninstall`이 추가되었습니다.

* 새로운 이벤트 유형 `users.campaigns.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.campaigns.EnrollInControl`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.Entry`가 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.exit.MatchedAudience`가 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.exit.PerformedEvent`가 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.experimentstep.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.experimentstep.SplitEntry`가 추가되었습니다.

* 새로운 이벤트 유형 `users.canvasstep.Progression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Dismiss`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Bounce`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Deferral`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Delivery`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.MarkAsSpam`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Open`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.SoftBounce`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Unsubscribe`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.featureflag.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.liveactivity.Outcome`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.liveactivity.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Bounce`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.IosForeground`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Open`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.CarrierSend`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Delivery`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.DeliveryFailure`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.InboundReceive`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Rejection`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.ShortLinkClick`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Failure`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Delivery`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Failure`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.InboundReceive`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Read`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.RandomBucketNumberUpdate`가 추가되었습니다.