---
nav_title: "POST: 사용자 추적 (대량) - Braze 파트너용"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk_partners/
description: "Braze 파트너인 경우 이 엔드포인트를 사용하여 커스텀 이벤트와 구매를 기록하고 고객 프로필 속성을 대량으로 업데이트할 수 있습니다."
---

{% api %}
# 사용자 추적 (대량) - Braze 파트너용 {#track-users-bulk-for-braze-partners}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Braze 파트너인 경우 이 엔드포인트를 사용하여 커스텀 이벤트와 구매를 기록하고 고객 프로필 속성을 대량으로 업데이트할 수 있습니다.

{% alert important %}
이 엔드포인트는 Braze 파트너가 Braze 통합에서 대량 사용 사례를 마이그레이션할 수 있도록 제공됩니다. 문의 사항이 있으면 [isv-support@braze.com](mailto:isv-support@braze.com)으로 연락해 주세요.
{% endalert %}

## 이 엔드포인트를 사용해야 하는 경우 {#when-to-use-this-endpoint}

[POST: 사용자 추적 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites)와 마찬가지로 이 엔드포인트를 사용하여 고객 프로필을 업데이트할 수 있습니다. 그러나 이 엔드포인트는 대량 업데이트에 더 적합합니다.

- **더 큰 요청:** 이 엔드포인트는 요청당 1,000명의 사용자를 허용하므로, 대량 업데이트 요구 사항을 충족하기 위해 더 적은 수의 요청을 보내면 됩니다.
- **우선순위 지정:** 트래픽이 많은 상황에서는 `/users/track`의 요청이 `/users/track/bulk`의 요청보다 우선 처리됩니다. 두 엔드포인트를 모두 사용하면 데이터 수집에 대한 더 많은 제어가 가능합니다.

온보딩 중 많은 고객 프로필을 백필하거나 일일 동기화의 일부로 대량의 고객 프로필을 동기화할 때 이 엔드포인트 사용을 고려해 보세요.

{% alert note %}
`/users/track/bulk` 사용을 권장하기 위해 `/users/track` 오브젝트 제한을 225에서 5로 줄일 계획입니다. Braze 통합이 향후 업데이트와 호환되도록 이 점을 유의해 주세요.
{% endalert %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.track` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다. 이 권한은 `/users/track`과 `/users/track/bulk` 모두에 대한 액세스를 제공합니다.

대부분의 공유 고객은 이미 Braze 파트너 통합에 `users.track` 권한이 있는 API 키를 사용하고 있으므로, 통합을 `/users/track/bulk`로 마이그레이션할 때 API 키를 변경할 필요가 없습니다.

고객이 서버 간 호출에 API를 사용하는 경우, 방화벽 뒤에 있다면 엔드포인트(예: `rest.iad-01.braze.com`)를 허용 목록에 추가해야 할 수 있습니다. 자세한 내용은 [인스턴스별 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 참조하세요.

## 사용량 제한 {#rate-limit}

대부분의 고객에게 이 엔드포인트에 대해 초당 50건의 기본 속도 제한이 적용됩니다.

그러나 최신 계약을 체결한 고객에게는 Braze와 계약한 MAU에 연동된 버스트(초당) 및 정상(시간당) 사용량 제한이 대신 적용될 수 있습니다.

API와의 실시간 상호작용을 개선하려면 [권장 응답 헤더]({{site.baseurl}}/api/api_limits/#monitoring-your-rate-limits)를 사용하세요.

각 `/users/track/bulk` 요청의 페이로드 제한은 2&nbsp;MB이며, 최대 1,000개의 이벤트, 속성 또는 구매 오브젝트를 포함할 수 있습니다.

각 오브젝트(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있으므로, 단일 요청에서 최대 1,000명의 서로 다른 사용자를 업데이트할 수 있습니다. 단일 고객 프로필은 단일 요청에서 최대 100개의 오브젝트를 업데이트할 수 있습니다.

## 요청 본문 {#request-body}


```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### 요청 매개변수 {#request-parameters}

{% alert important %}
다음 표에 나열된 각 요청 구성요소에는 `external_id`, `user_alias`, `braze_id`, `email` 또는 `phone` 중 하나가 필수입니다.
{% endalert %}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `attributes` | 선택 사항 | 속성 오브젝트 배열 | [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object/)를 참조하세요 |
| `events` | 선택 사항 | 이벤트 오브젝트 배열 | [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object/)를 참조하세요 |
| `purchases` | 선택 사항 | 구매 오브젝트 배열 | [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/)를 참조하세요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시 {#example-requests}

### 단일 요청으로 1,000개의 고객 프로필 대량 업데이트 {#bulk-update-1000-user-profiles-in-one-request}

`/users/track/bulk` 엔드포인트를 사용하여 최대 1,000개의 고객 프로필을 업데이트할 수 있습니다. 다음은 요청이 1,000개의 속성 오브젝트로 구성된 축약된 예시입니다.

```javascript
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
                "asparagus",
            ]
        },

...

        {
            "external_id": "user1000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

다음은 요청이 속성 오브젝트와 이벤트 오브젝트로 모두 구성된 예시입니다.

```javascript
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
        },
...
        {
            "external_id": "user1000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

### 성공 메시지 {#successful-messages}

성공한 메시지는 다음과 같은 응답을 반환합니다.

```javascript
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### 심각하지 않은 오류가 포함된 성공 메시지 {#successful-message-with-non-fatal-errors}

메시지가 성공했지만 긴 이벤트 목록 중 하나의 잘못된 이벤트 오브젝트와 같은 심각하지 않은 오류가 있는 경우 다음과 같은 응답을 받게 됩니다.

```javascript
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

메시지에 심각한 오류가 있는 경우 다음과 같은 응답을 받게 됩니다.

```javascript
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

#### 심각한 오류 응답 코드 {#fatal-error-response-codes}

요청에 심각한 오류가 발생한 경우 반환되는 상태 코드 및 관련 오류 메시지는 [심각한 오류 및 응답]({{site.baseurl}}/api/errors/#fatal-errors)을 참조하세요.

`provided external\_id is blacklisted and disallowed` 오류가 발생하면 요청에 `dummy user`가 포함되었을 수 있습니다. 자세한 내용은 [스팸 차단]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)을 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 이 엔드포인트를 사용해야 하나요, 아니면 `/users/track`을 사용해야 하나요? {#should-i-use-this-endpoint-or-userstrack}

두 가지 모두 사용하는 것을 권장합니다.

- 대규모 고객 프로필 백필 및 동기화에는 `/users/track/bulk` 엔드포인트를 사용하세요.
- 실시간 사용 사례에는 `/users/track` 엔드포인트를 사용하세요.

{% alert note %}
`/users/track/bulk` 사용을 권장하기 위해 `/users/track` 오브젝트 제한을 225에서 5로 줄일 계획입니다. Braze 통합이 향후 업데이트와 호환되도록 이 점을 유의해 주세요.
{% endalert %}

### `/users/track/bulk`에서 어떤 식별자를 사용할 수 있나요? {#what-identifiers-can-i-use-in-userstrackbulk}

`external\_id`, `braze\_id`, `user\_alias`, `email` 또는 `phone` 중 하나가 필수입니다. 자세한 예시는 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object/), [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object/) 또는 [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/) 설명서를 참조하세요.

### 하나의 요청에 속성, 이벤트, 구매를 모두 포함할 수 있나요? {#can-i-include-attributes-events-and-purchases-in-one-request}

네. 요청당 1,000개 오브젝트 제한까지 속성, 이벤트 및 구매 오브젝트를 원하는 만큼 조합하여 요청을 구성할 수 있습니다.

{% endapi %}