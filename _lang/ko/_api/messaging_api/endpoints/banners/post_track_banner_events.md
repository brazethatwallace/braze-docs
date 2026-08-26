---
nav_title: "POST: 배너 분석 이벤트 추적"
article_title: "POST: 배너 분석 이벤트 추적"
permalink: /api/device_messaging_api/endpoints/banners/post_track_banner_events
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 엔드포인트를 사용하여 배너의 노출 횟수 및 클릭 이벤트를 추적합니다."
hidden: true
---

{% api %}
# 배너 분석 이벤트 추적 {#track-banner-analytics-events}
{% apimethod post %}
/v1/device-messaging/banners/track
{% endapimethod %}

{% alert important %}
이 페이지는 베타 버전입니다. Device Messaging API의 기능 및 설명서는 변경될 수 있습니다.
{% endalert %}

> 이 엔드포인트를 사용하여 배너의 노출 횟수 및 클릭 이벤트를 기록합니다.

Braze는 각 이벤트를 개별적으로 검증합니다. 요청에 유효한 이벤트와 유효하지 않은 이벤트가 모두 포함된 경우, Braze는 유효한 이벤트를 처리하고 건너뛴 이벤트에 대한 세부 정보를 `errors` 배열에 반환합니다. 유효한 이벤트가 없는 경우, Braze는 `400` 상태 코드를 반환합니다.

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 다음이 필요합니다:

- 배너가 활성화된 워크스페이스
- `banners.track` 권한이 있는 [클라이언트 측 REST API 키]({{site.baseurl}}/api/device_messaging_api/authentication)
- Braze 인스턴스의 [REST 엔드포인트]({{site.baseurl}}/api/basics#endpoints)
- [사용자의 배너 조회 엔드포인트]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)에서 반환된 배너 `id`

클라이언트 측 REST API 키를 `Authorization` 헤더에 베어러 토큰으로 포함하세요.

## 사용량 제한 {#rate-limit}

사용량 제한은 워크스페이스별로 적용됩니다. 사용량 제한을 초과하면 Braze는 `429` 상태 코드를 반환합니다. 가능한 경우 `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `X-RateLimit-Retry-After` 응답 헤더를 사용하여 사용량을 모니터링하고 재시도 시점을 결정하세요.

자세한 내용은 [Device Messaging API 사용량 제한]({{site.baseurl}}/api/device_messaging_api/rate_limits)을 참조하세요.

## 요청 본문 {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "{BANNER_ID}",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    }
  ]
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 | 예시 |
|---|---|---|---|---|
| `external_user_id` | 필수 | 문자열 | 요청의 모든 이벤트와 연결된 사용자의 외부 ID입니다. UTF-8 인코딩 값은 987바이트 미만이어야 합니다. | `user_abc123` |
| `app_id` | 필수 | 문자열 | [앱 API 식별자]({{site.baseurl}}/api/identifier_types#app-identifier)입니다. 인증된 워크스페이스의 앱을 식별해야 합니다. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | 필수 | 문자열 | 호스트 앱의 버전입니다. 255자를 초과할 수 없습니다. | `1.0.0` |
| `events` | 필수 | 객체 배열 | 기록할 하나 이상의 배너 분석 이벤트입니다. | `[{"id":"bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E","event_type":"impression","timestamp":"2026-04-09T12:00:00Z"}]` |
| `events[].id` | 필수 | 문자열 | 사용자의 배너 조회 엔드포인트에서 반환된 배너 `id`입니다. Braze가 이벤트를 올바른 Campaign 및 배리언트에 귀속시킬 수 있도록 `placement_id`가 아닌 배너 ID를 사용하세요. | `bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E` |
| `events[].event_type` | 필수 | 문자열 | 이벤트 유형입니다. 가능한 값은 `impression` 및 `click`입니다. | `impression` |
| `events[].timestamp` | 필수 | 문자열 | 이벤트가 발생한 날짜 및 시간으로, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열 형식입니다. | `2026-04-09T12:00:00Z` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}

*`YOUR_REST_API_URL`*을 Braze 인스턴스의 [REST 엔드포인트]({{site.baseurl}}/api/basics#endpoints)로 대체하세요.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/track' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    },
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "click",
      "timestamp": "2026-04-09T12:00:05Z"
    }
  ]
}'
```

## 응답 매개변수 {#response-parameters}

| 매개변수 | 데이터 유형 | 설명 |
|---|---|---|
| `events_processed` | 정수 | Braze가 검증하고 대기줄에 넣은 이벤트 수입니다. |
| `message` | 문자열 | 수락된 이벤트 배치의 상태입니다. |
| `errors` | 객체 배열 | Braze가 건너뛴 이벤트에 대한 세부 정보입니다. Braze가 모든 이벤트를 처리한 경우 이 배열은 없습니다. |
| `errors[].type` | 문자열 | 건너뛴 이벤트의 검증 오류입니다. |
| `errors[].index` | 정수 | 요청의 `events` 배열에서 건너뛴 이벤트의 0 기반 인덱스입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="응답 매개변수" }

## 응답 예시 {#example-responses}

### 모든 이벤트 처리됨 {#all-events-processed}

Braze가 모든 이벤트를 수락하면 `202` 상태 코드를 반환합니다.

```json
{
  "events_processed": 2,
  "message": "success"
}
```

### 일부 이벤트 건너뜀 {#some-events-skipped}

Braze는 유효한 이벤트를 하나 이상 수락한 경우에도 `202` 상태 코드를 반환합니다. 응답에는 건너뛴 이벤트가 표시됩니다.

```json
{
  "events_processed": 2,
  "message": "success",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click.",
      "index": 2
    }
  ]
}
```

### 유효한 이벤트 없음 {#no-valid-events}

Braze가 이벤트를 처리할 수 없는 경우 `400` 상태 코드를 반환합니다.

```json
{
  "message": "No valid events provided.",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click.",
      "index": 0
    },
    {
      "type": "'timestamp' is required",
      "index": 1
    }
  ]
}
```

## 상태 코드 {#status-codes}

| 상태 코드 | 설명 |
|---|---|
| `202` | Braze가 하나 이상의 이벤트를 수락했습니다. 응답에 건너뛴 이벤트가 나열됩니다. |
| `400` | 요청 형식이 잘못되었거나, 필수 필드가 유효하지 않거나, 유효한 이벤트가 없습니다. |
| `401` | 클라이언트 측 REST API 키가 누락되었거나 유효하지 않습니다. |
| `403` | 클라이언트 측 REST API 키에 `banners.track` 권한이 없습니다. |
| `404` | 워크스페이스에 배너 기능이 활성화되어 있지 않습니다. |
| `429` | 워크스페이스가 사용량 제한을 초과했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="상태 코드" }

자세한 내용은 [Device Messaging API 오류 처리 및 재시도]({{site.baseurl}}/api/device_messaging_api/error_handling)를 참조하세요.

{% endapi %}