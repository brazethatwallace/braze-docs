---
nav_title: "POST: 사용자 생성 및 업데이트 (대량)"
article_title: "POST: 사용자 생성 및 업데이트 (대량)"
search_tag: Endpoint
page_order: 4.25
layout: api_page
page_type: reference
alias:
  - /unlisted_docs/track_users_bulk_partners/
  - /api/endpoints/user_data/post_user_track_bulk_partners/
description: "이 문서에서는 대량 사용자 추적 엔드포인트에 대한 세부 정보를 설명합니다."
---
{% api %}
# 사용자 생성 및 업데이트 (대량) {#create-and-update-users-bulk}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

이 엔드포인트를 사용하여 커스텀 이벤트와 구매를 기록하고 사용자 프로필 속성을 대량으로 업데이트할 수 있습니다.

{% alert important %}
이 엔드포인트는 현재 **제한된 베타** 상태입니다. 현재 베타에 새로운 고객을 추가하고 있지는 않지만, 이 기능이 Braze 통합에 유용할 것으로 생각되시면 Braze 계정 매니저에게 알려주세요.
{% endalert %}

## 이 엔드포인트를 사용해야 하는 경우 {#when-to-use-this-endpoint}

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)와 마찬가지로, 이 엔드포인트를 사용하여 사용자 프로필을 업데이트할 수 있습니다. 이 엔드포인트는 대량 업데이트에 더 적합합니다:

- **더 큰 요청:** 요청당 최대 1,000명의 사용자를 전송할 수 있으므로, 대규모 백필 및 동기화 시 더 적은 요청으로 처리할 수 있습니다.
- **우선순위 지정:** 트래픽이 많은 상황에서 `/users/track` 요청이 `/users/track/bulk` 요청보다 우선적으로 처리됩니다.

온보딩 중 많은 사용자 프로필을 백필하거나, 일일 동기화의 일부로 대량의 프로필을 동기화할 때 이 엔드포인트를 사용하세요.

{% alert note %}
`/users/track` 엔드포인트 요청 오브젝트 제한은 요금제 모델 및 구성에 따라 다릅니다. 대량 수집에는 `/users/track/bulk`을 사용하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.track.bulk` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key)가 필요합니다.

방화벽 뒤에서 서버 간 호출을 수행하는 경우, Braze REST 엔드포인트(예: `rest.iad-01.braze.com`)를 허용 목록에 추가해야 할 수 있습니다. 자세한 내용은 [API 엔드포인트]({{site.baseurl}}/api/basics#api-definitions)를 참조하세요.

## 사용량 제한 {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/bulk" %}

대부분의 고객에게 이 엔드포인트의 기본 속도 제한은 초당 50건의 요청입니다.

최신 계약을 사용하는 고객은 계약된 월간 활성 사용자 수에 따라 버스트(초당) 및 정상(시간당) 제한이 적용될 수 있습니다.

각 `/users/track/bulk` 요청의 페이로드 제한은 2MB이며, 계정의 대량 사용량 제한 정책에 따라 속성, 이벤트, 구매 전체에 걸쳐 최대 1,000개의 오브젝트를 포함할 수 있습니다.

각 오브젝트는 한 명의 사용자를 업데이트할 수 있으므로, 단일 요청으로 계정의 요청 오브젝트 제한까지 서로 다른 사용자를 업데이트할 수 있습니다. 또한 각 요청에는 사용자 프로필당 속성, 이벤트, 구매 전체에 걸쳐 최대 100개의 오브젝트를 포함할 수 있습니다.

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object)
}
```

### 요청 매개변수 {#request-parameters}

{% alert important %}
각 요청 오브젝트에는 `external_id`, `user_alias`, `braze_id`, `email`, `phone` 중 하나를 포함해야 합니다.
{% endalert %}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `attributes` | 선택 사항 | 속성 오브젝트 배열 | [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object)를 참조하세요 |
| `events` | 선택 사항 | 이벤트 오브젝트 배열 | [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object)를 참조하세요 |
| `purchases` | 선택 사항 | 구매 오브젝트 배열 | [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object)를 참조하세요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-requests}

### 하나의 요청으로 사용자 프로필 대량 업데이트 {#bulk-update-user-profiles-in-one-request}

하나의 요청으로 계정의 요청 오브젝트 제한까지 사용자 프로필을 업데이트할 수 있습니다.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    },
    {
      "external_id": "user2",
      "string_attribute": "vegetables",
      "boolean_attribute_1": false,
      "integer_attribute": 25,
      "array_attribute": [
        "broccoli",
        "asparagus"
      ]
    }
  ]
}'
```

### 하나의 요청으로 속성과 이벤트 전송 {#send-attributes-and-events-in-one-request}

계정의 총 오브젝트 제한까지 동일한 요청에 속성과 이벤트를 포함할 수 있습니다.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    }
  ],
  "events": [
    {
      "external_id": "user2",
      "app_id": "your_app_identifier",
      "name": "rented_movie",
      "time": "2022-12-06T19:20:45+01:00",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}'
```

## 응답 {#responses}

### 성공 메시지 {#successful-message}

성공적인 메시지는 다음 응답을 반환합니다:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external IDs with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing
}
```

### 치명적이지 않은 오류가 포함된 성공 메시지 {#successful-message-with-non-fatal-errors}

요청이 성공했지만 치명적이지 않은 오류가 있는 경우(예: 대규모 배치에서 하나의 잘못된 이벤트 오브젝트), 다음 응답을 받게 됩니다:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

### 심각한 오류가 포함된 메시지 {#message-with-fatal-errors}

요청에 심각한 오류가 있는 경우, 다음 응답을 받게 됩니다:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### 심각한 오류 응답 코드 {#fatal-error-response-codes}

요청에 심각한 오류가 있을 때 Braze가 반환하는 상태 코드 및 관련 오류 메시지에 대해서는 [심각한 오류 및 응답]({{site.baseurl}}/api/errors#fatal-errors)을 참조하세요.

"provided external_id is blacklisted and disallowed" 오류가 발생하면, 요청에 "더미 사용자"가 포함되어 있을 수 있습니다. 자세한 내용은 [스팸 차단]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#spam-blocking)을 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 이 엔드포인트와 `/users/track` 중 어떤 것을 사용해야 하나요? {#should-i-use-this-endpoint-or-userstrack}

사용 사례에 따라 두 엔드포인트를 모두 사용하세요:

- 대규모 백필 및 동기화에는 `/users/track/bulk`을 사용하세요.
- 실시간 사용 사례에는 `/users/track`을 사용하세요.

### `/users/track/bulk`에서 어떤 식별자를 사용할 수 있나요? {#what-identifiers-can-i-use-in-userstrackbulk}

각 요청 오브젝트에 `external_id`, `braze_id`, `user_alias`, `email`, `phone` 중 하나를 포함하세요.

### 하나의 요청에 속성, 이벤트, 구매를 모두 포함할 수 있나요? {#can-i-include-attributes-events-and-purchases-in-one-request}

네. 계정의 결합된 요청 오브젝트 제한까지 속성, 이벤트, 구매를 자유롭게 조합하여 포함할 수 있습니다.

{% endapi %}