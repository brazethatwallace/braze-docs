---
nav_title: "POST: 사용자의 배너 조회"
article_title: "POST: 사용자의 배너 조회"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "이 엔드포인트를 사용하여 사용자에게 적합한 배너를 조회할 수 있습니다."
hidden: true
---

{% api %}
# 사용자의 배너 조회 {#retrieve-banners-for-a-user}
{% apimethod post %}
/v1/device-messaging/banners/sync
{% endapimethod %}

{% alert important %}
이 페이지는 베타 버전입니다. 메시징 API의 기능과 설명서는 변경될 수 있습니다.
{% endalert %}

> 이 엔드포인트를 사용하여 사용자에 대해 요청된 각 배치에 적합한 배너를 조회합니다.

응답에는 커스텀 인터페이스를 구축하는 데 사용할 수 있는 구조화된 배너 속성정보가 포함됩니다. 렌더링된 HTML은 포함되지 않습니다.

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 다음이 필요합니다.

- 배너가 활성화된 워크스페이스
- `banners.sync` 권한이 있는 [클라이언트 측 REST API 키]({{site.baseurl}}/api/messaging_api/authentication)
- Braze 인스턴스의 [REST 엔드포인트]({{site.baseurl}}/api/basics#endpoints)

클라이언트 측 REST API 키를 `Authorization` 헤더에 베어러 토큰으로 포함하세요.

## 사용량 제한 {#rate-limit}

사용량 제한은 워크스페이스별로 적용됩니다. 사용량 제한을 초과하면 Braze는 `429` 상태 코드를 반환합니다. 가능한 경우 `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` 응답 헤더를 사용하여 사용량을 모니터링하세요.

자세한 내용은 [메시징 API 사용량 제한]({{site.baseurl}}/api/messaging_api/rate_limits)을 참조하세요.

## 요청 본문 {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 | 예시 |
|---|---|---|---|---|
| `external_user_id` | 필수 | 문자열 | 사용자의 외부 ID입니다. | `user_abc123` |
| `app_id` | 필수 | 문자열 | [앱 API 식별자]({{site.baseurl}}/api/identifier_types#app-identifier)입니다. 인증된 워크스페이스의 앱을 식별해야 합니다. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | 필수 | 문자열 | 호스트 앱의 버전입니다. 255자를 초과할 수 없습니다. | `1.0.0` |
| `placements` | 필수 | 문자열 배열 | 배너를 조회할 하나 이상의 배치 ID입니다. 최소 하나의 배치 ID를 포함하세요. | `["home_hero", "sidebar_promo"]` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}

*`YOUR_REST_API_URL`*을 Braze 인스턴스의 [REST 엔드포인트]({{site.baseurl}}/api/basics#endpoints)로 바꾸세요.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/sync' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}'
```

## 응답 매개변수 {#response-parameters}

| 매개변수 | 데이터 유형 | 설명 |
|---|---|---|
| `banners` | 객체 | 요청된 각 배치 ID를 해당 배너로 매핑한 맵입니다. 배치에 적합한 배너가 없으면 값은 `null`입니다. |
| `banners.{placement_id}.id` | 문자열 | 고유 배너 식별자입니다. 이 값을 사용하여 노출 횟수 및 클릭 이벤트를 보고합니다. |
| `banners.{placement_id}.placement_id` | 문자열 | 배너에 매칭된 배치 ID입니다. |
| `banners.{placement_id}.is_control` | 불리언 | 배너가 대조군 배리언트인지 여부입니다. |
| `banners.{placement_id}.is_test_send` | 불리언 | 배너가 테스트 전송에서 온 것인지 여부입니다. 기본값은 `false`입니다. |
| `banners.{placement_id}.expires_at` | 정수 | 배너를 더 이상 표시하지 않아야 하는 unix 타임스탬프(초 단위)입니다. `-1` 값은 배너가 만료되지 않음을 의미합니다. |
| `banners.{placement_id}.properties` | 객체 또는 null | 마케터가 정의한 배너의 속성정보입니다. 각 속성정보에는 `type`과 `value`가 포함됩니다. |
| `banners.{placement_id}.properties.{property}.type` | 문자열 | 속성정보의 유형입니다. 가능한 값은 `number`, `string`, `boolean`, `image`, `jsonobject`, `datetime`입니다. |
| `banners.{placement_id}.properties.{property}.value` | 숫자, 문자열, 불리언 또는 객체 | 속성정보의 값입니다. JSON 유형은 `type`에 대응합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="응답 매개변수" }

## 응답 예시 {#example-response}

성공적인 요청은 `200` 상태 코드와 요청된 각 배치에 대해 확인된 배너를 반환합니다.

```json
{
  "banners": {
    "home_hero": {
      "id": "this_banner_is_a_stub_01",
      "placement_id": "home_hero",
      "is_control": false,
      "is_test_send": false,
      "expires_at": 1735689600,
      "properties": {
        "headline": {
          "type": "string",
          "value": "Level Up Your Game"
        },
        "cta_label": {
          "type": "string",
          "value": "Shop Now"
        }
      }
    },
    "sidebar_promo": null
  }
}
```

## 상태 코드 {#status-codes}

| 상태 코드 | 설명 |
|---|---|
| `200` | Braze가 요청된 각 배치에 대해 배너 데이터를 확인했습니다. |
| `400` | 요청에 누락되었거나 유효하지 않은 매개변수가 포함되어 있습니다. |
| `401` | 클라이언트 측 REST API 키가 누락되었거나, 유효하지 않거나, `banners.sync` 권한이 없습니다. |
| `404` | 엔드포인트를 사용할 수 없습니다. 이 응답은 누락되었거나 유효하지 않은 API 키와 비활성화된 배너 기능을 구분하지 않습니다. |
| `429` | 워크스페이스가 사용량 제한을 초과했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="상태 코드" }

자세한 내용은 [메시징 API 오류 처리 및 재시도]({{site.baseurl}}/api/messaging_api/error_handling)를 참조하세요.

{% endapi %}