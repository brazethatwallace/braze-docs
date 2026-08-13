---
nav_title: Currents 이벤트 체인지로그
page_order: 6
description: "이 페이지에는 각 Currents 릴리스에 대한 이벤트 변경 사항이 포함되어 있습니다."
tool: Currents
---

# Currents 체인지로그 {#currents-changelog}

## 버전 11의 변경 사항 (릴리스 날짜 2026-08-05) {#changes-in-version-11-release-date-2026-08-05}

### 저장소에 대한 변경 사항: {#changes-for-storage}

* 새로운 이벤트 유형 `contentoptimizer.ComponentStore`가 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.costep.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.landingpage.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.landingpage.FormSubmission`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.landingpage.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.survey.Response`가 추가되었습니다.

* 이벤트 유형 `agentconsole.AgentExecuted`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `thinking_level` 추가: 요청에 사용된 사고 또는 추론 수준

* 이벤트 유형 `users.messages.banner.Click`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_unique` 추가: 해당 메시지 배리언트에 대한 사용자의 첫 번째 클릭인지 여부로, 고유 클릭 통계에 집계됩니다

* 이벤트 유형 `users.messages.banner.Dismiss`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_unique` 추가: 해당 메시지 배리언트에 대한 사용자의 첫 번째 닫기인지 여부로, 고유 닫기 통계에 집계됩니다

* 이벤트 유형 `users.messages.banner.Impression`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_unique` 추가: 해당 메시지 배리언트에 대한 사용자의 첫 번째 노출인지 여부로, 고유 노출 통계에 집계됩니다

* 이벤트 유형 `users.messages.contentcard.Click`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_unique` 추가: 해당 메시지 배리언트에 대한 사용자의 첫 번째 클릭인지 여부로, 고유 클릭 통계에 집계됩니다

* 이벤트 유형 `users.messages.contentcard.Dismiss`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_unique` 추가: 해당 메시지 배리언트에 대한 사용자의 첫 번째 닫기인지 여부로, 고유 닫기 통계에 집계됩니다

* 이벤트 유형 `users.messages.contentcard.Impression`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_unique` 추가: 해당 메시지 배리언트에 대한 사용자의 첫 번째 노출인지 여부로, 고유 노출 통계에 집계됩니다

* 이벤트 유형 `users.messages.featureflag.Impression`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_unique` 추가: 이 기능 플래그에 대한 사용자의 첫 번째 노출인지 여부로, 고유 노출 통계에 집계됩니다

## 버전 10의 변경 사항 (릴리스 날짜 2026-07-01) {#changes-in-version-10-release-date-2026-07-01}

### 저장소에 대한 변경 사항:

* 새로운 이벤트 유형 `users.canvas.costep.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.UserDeleteRequest`가 추가되었습니다.

* 새로운 이벤트 유형 `users.UserOrphan`이 추가되었습니다.

* 이벤트 유형 `users.messages.rcs.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Click`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Delivery`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.InboundReceive`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Read`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Rejection`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

* 이벤트 유형 `users.messages.rcs.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID

## 버전 9의 변경 사항 (릴리스 날짜 2026-06-03) {#changes-in-version-9-release-date-2026-06-03}

### 저장소에 대한 변경 사항:

* 이벤트 유형 `users.messages.email.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `from_domain` 추가: 이메일의 발송 도메인

## 버전 8의 변경 사항 (릴리스 날짜 2026-05-06) {#changes-in-version-8-release-date-2026-05-06}

### 저장소에 대한 변경 사항:

* 새로운 이벤트 유형 `users.messages.banner.Dismiss`가 추가되었습니다.

* 이벤트 유형 `users.messages.whatsapp.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid` 추가: 이 이벤트와 연결된 수신자의 WhatsApp Business-Scoped 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Delivery`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid` 추가: 이 이벤트와 연결된 수신자의 WhatsApp Business-Scoped 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Failure`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid` 추가: 이 이벤트와 연결된 수신자의 WhatsApp Business-Scoped 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.InboundReceive`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid` 추가: 메시지를 보낸 사용자의 WhatsApp Business-Scoped 사용자 ID입니다.
    * 필드 `user_phone_number`은 이제 *선택 사항*입니다.

* 이벤트 유형 `users.messages.whatsapp.Read`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid` 추가: 이 이벤트와 연결된 수신자의 WhatsApp Business-Scoped 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Retry`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid` 추가: 이 이벤트와 연결된 수신자의 WhatsApp Business-Scoped 사용자 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `bsuid` 추가: 이 이벤트와 연결된 수신자의 WhatsApp Business-Scoped 사용자 ID입니다.

## 버전 7의 변경 사항 (릴리스 날짜 2026-04-01) {#changes-in-version-7-release-date-2026-04-01}

### 저장소에 대한 변경 사항:

* 새로운 이벤트 유형 `users.profile.Update`가 추가되었습니다.

* 이벤트 유형 `users.messages.banner.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: Canvas의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 Canvas 배리언트의 이름
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID
    * 새로운 `string` 필드 `canvas_step_id` 추가: 이 이벤트가 속한 캔버스 단계의 API ID
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 받은 캔버스 단계 메시지 배리언트의 API ID
    * 새로운 `string` 필드 `canvas_variation_id` 추가: 이 이벤트가 속한 Canvas 배리언트의 API ID

* 이벤트 유형 `users.messages.banner.Click`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID
    * 새로운 `string` 필드 `canvas_step_id` 추가: 이 이벤트가 속한 캔버스 단계의 API ID
    * 새로운 `string` 필드 `canvas_name` 추가: Canvas의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 받은 캔버스 단계 메시지 배리언트의 API ID
    * 새로운 `string` 필드 `canvas_variation_id` 추가: 이 이벤트가 속한 Canvas 배리언트의 API ID
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 Canvas 배리언트의 이름

* 이벤트 유형 `users.messages.banner.Impression`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_id` 추가: 이 이벤트가 속한 Canvas의 API ID
    * 새로운 `string` 필드 `canvas_step_id` 추가: 이 이벤트가 속한 캔버스 단계의 API ID
    * 새로운 `string` 필드 `canvas_name` 추가: Canvas의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 받은 캔버스 단계 메시지 배리언트의 API ID
    * 새로운 `string` 필드 `canvas_variation_id` 추가: 이 이벤트가 속한 Canvas 배리언트의 API ID
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 Canvas 배리언트의 이름

## 버전 6의 변경 사항 (릴리스 날짜 2026-03-04) {#changes-in-version-6-release-date-2026-03-04}

### 저장소에 대한 변경 사항:

* 이벤트 유형 `agentconsole.AgentExecuted`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `error` 추가: 오류 설명

* 이벤트 유형 `agentconsole.ToolInvocation`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `request_id` 추가: 이 전체 LLM 요청 및 완전한 실행에 대한 고유 ID

* 이벤트 유형 `users.messages.rcs.InboundReceive`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 Canvas 배리언트의 이름

## 버전 5의 변경 사항 (릴리스 날짜 2026-02-04) {#changes-in-version-5-release-date-2026-02-04}

### 저장소에 대한 변경 사항:

* 새로운 이벤트 유형 `agentconsole.AgentExecuted`가 추가되었습니다.

* 새로운 이벤트 유형 `agentconsole.ToolInvocation`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Retry`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Retry`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Retry`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Retry`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Retry`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Retry`가 추가되었습니다.

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`에 대한 필드 변경 사항:
    * 새로운 `long` 필드 `time_ms` 추가: 이벤트가 발생한 시간(밀리초 단위)

## 버전 4의 변경 사항 (릴리스 날짜 2026-01-07) {#changes-in-version-4-release-date-2026-01-07}

### 저장소에 대한 변경 사항:

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.pushnotification.Bounce`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.pushnotification.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.rcs.Click`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 Canvas 배리언트의 이름
    * 필드 `user_phone_number`은 이제 *선택 사항*입니다.

* 이벤트 유형 `users.messages.rcs.InboundReceive`에 대한 필드 변경 사항:
    * 필드 `user_id`는 이제 *선택 사항*입니다.

* 이벤트 유형 `users.messages.rcs.Rejection`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 받은 캔버스 단계 메시지 배리언트의 API ID

## 버전 3의 변경 사항 (릴리스 날짜 2025-10-08) {#changes-in-version-3-release-date-2025-10-08}

### 저장소에 대한 변경 사항:

* 새로운 이벤트 유형 `users.messages.line.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.InboundReceive`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Send`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Abort`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Delivery`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.InboundReceive`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Read`가 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Rejection`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Send`가 추가되었습니다.

* 이벤트 유형 `users.messages.sms.Delivery`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_sms_fallback` 추가: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 디스패치 ID를 통해 RCS 거부 이벤트에 연결할 수 있습니다.

* 이벤트 유형 `users.messages.sms.DeliveryFailure`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_sms_fallback` 추가: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 디스패치 ID를 통해 RCS 거부 이벤트에 연결할 수 있습니다.

* 이벤트 유형 `users.messages.sms.Rejection`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_sms_fallback` 추가: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 디스패치 ID를 통해 RCS 거부 이벤트에 연결할 수 있습니다.

* 이벤트 유형 `users.messages.whatsapp.Delivery`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `flow_id` 추가: WhatsApp Manager의 Flow 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하기 위한 CTA가 포함된 경우 표시됩니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp Manager의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id` 추가: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Failure`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `message_id` 추가: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp Manager의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `flow_id` 추가: WhatsApp Manager의 Flow 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하기 위한 CTA가 포함된 경우 표시됩니다.

* 이벤트 유형 `users.messages.whatsapp.InboundReceive`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `catalog_id` 추가: 수신 메시지에 제품이 참조된 경우 해당 제품의 카탈로그 ID입니다. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 `product_id` 추가: 수신 메시지에 제품이 참조된 경우 제품 SKU입니다. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 `flow_id` 추가: WhatsApp Manager의 Flow 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `flow_response_json` 추가: [PII] 사용자가 응답한 양식 값입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id` 추가: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `in_reply_to` 추가: 이 메시지가 응답한 메시지의 message_id입니다.

* 이벤트 유형 `users.messages.whatsapp.Read`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp Manager의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id` 추가: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `flow_id` 추가: WhatsApp Manager의 Flow 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하기 위한 CTA가 포함된 경우 표시됩니다.

* 이벤트 유형 `users.messages.whatsapp.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `flow_id` 추가: WhatsApp Manager의 Flow 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하기 위한 CTA가 포함된 경우 표시됩니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp Manager의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id` 추가: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.

## 버전 2의 변경 사항 (릴리스 날짜 없음) {#changes-in-version-2-release-date-null}

### 저장소에 대한 변경 사항:

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