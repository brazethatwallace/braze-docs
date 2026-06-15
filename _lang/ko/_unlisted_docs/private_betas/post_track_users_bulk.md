---
nav_title: "POST: 사용자 추적 (대량)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "이 문서에서는 사용자 추적(대량) 엔드포인트에 대한 세부 정보를 설명합니다."
---

{% api %}
# 사용자 추적 (대량) {#track-users-bulk}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> 이 엔드포인트를 사용하여 커스텀 이벤트와 구매를 기록하고 사용자 프로필 속성을 대량으로 업데이트할 수 있습니다.

{% alert important %}
이 엔드포인트는 현재 베타 버전입니다. 베타 참여에 관심이 있으시면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 이 엔드포인트를 사용해야 하는 경우 {#when-to-use-this-endpoint}

[POST: 사용자 추적 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites)와 마찬가지로, 이 엔드포인트를 사용하여 사용자 프로필을 업데이트할 수 있습니다. 그러나 이 엔드포인트는 대량 업데이트에 더 적합합니다:

- **더 큰 요청:** 이 엔드포인트는 요청당 최대 10,000명의 사용자를 허용하므로, 대량 업데이트 요구 사항을 충족하기 위해 더 적은 수의 요청을 보내면 됩니다.
- **우선순위 지정:** 트래픽이 많은 상황에서는 `/users/track`의 요청이 `/users/track/bulk`의 요청보다 우선 처리됩니다. 두 엔드포인트를 모두 사용하면 데이터 수집에 대한 더 많은 제어가 가능합니다.

온보딩 중 많은 사용자 프로필을 백필하거나 일일 동기화의 일부로 대량의 사용자 프로필을 동기화할 때 이 엔드포인트 사용을 고려하세요.

{% alert note %}
2025년 5월 26일부터 이 엔드포인트를 사용하여 전환 측정기준을 추적하고, 예외 이벤트를 트리거하거나, 액션 기반 Campaigns 및 Canvases를 트리거할 수 있습니다. 이 동작은 다른 Braze 데이터 수집 방법과 유사합니다.
{% endalert %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.track.bulk` 권한이 있는 API 키가 필요합니다.

서버 간 호출에 API를 사용하는 경우, 방화벽 뒤에 있다면 엔드포인트(예: `rest.iad-01.braze.com`)를 허용 목록에 추가해야 할 수 있습니다. 자세한 내용은 [인스턴스별 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 참조하세요.

## 사용량 제한 {#rate-limit}

모든 고객에 대해 이 엔드포인트에 초당 5건의 기본 속도 제한이 적용됩니다.

각 `/users/track/bulk` 요청의 페이로드 제한은 4&nbsp;MB이며, 최대 10,000개의 이벤트, 속성 또는 구매 오브젝트를 포함할 수 있습니다.

각 오브젝트(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있으므로, 단일 요청에서 최대 10,000명의 서로 다른 사용자를 업데이트할 수 있습니다. 단일 사용자 프로필은 단일 요청에서 최대 100개의 오브젝트로 업데이트할 수 있습니다.

{% alert note %}
사용량 제한 증가가 필요한 경우 고객 성공 매니저에게 문의하세요.
{% endalert %}


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
다음 표에 나열된 각 요청 구성요소에 대해 `external_id`, `user_alias`, `braze_id`, `email` 또는 `phone` 중 하나가 필수입니다.
{% endalert %}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `attributes` | 선택 사항 | 속성 오브젝트 배열 | [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object/)를 참조하세요 |
| `events` | 선택 사항 | 이벤트 오브젝트 배열 | [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object/)를 참조하세요 |
| `purchases` | 선택 사항 | 구매 오브젝트 배열 | [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/)를 참조하세요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시 {#example-requests}

### 단일 요청으로 10,000개의 사용자 프로필 대량 업데이트 {#bulk-update-10000-user-profiles-in-one-request}

최대 10,000개의 사용자 프로필을 업데이트할 수 있습니다. 다음은 요청이 10,000개의 속성 오브젝트로 구성된 축약된 예시입니다:

```json
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
            "external_id": "user10000",
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

다음은 요청이 속성 오브젝트와 이벤트 오브젝트로 모두 구성된 예시입니다:

```json
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
            "external_id": "user10000",
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

성공한 메시지는 다음과 같은 응답을 반환합니다:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### 심각하지 않은 오류가 포함된 성공 메시지 {#successful-message-with-non-fatal-errors}

메시지가 성공했지만 심각하지 않은 오류가 있는 경우(예: 긴 이벤트 목록 중 하나의 잘못된 이벤트 오브젝트), 다음과 같은 응답을 받게 됩니다:

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

메시지에 심각한 오류가 있는 경우 다음과 같은 응답을 받게 됩니다:

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

#### 심각한 오류 응답 코드 {#fatal-error-response-codes}

요청에 심각한 오류가 발생한 경우 반환되는 상태 코드 및 관련 오류 메시지에 대해서는 [심각한 오류 및 응답]({{site.baseurl}}/api/errors/#fatal-errors)을 참조하세요.

`provided external_id is blacklisted and disallowed` 오류가 발생하면 요청에 "더미 사용자"가 포함되었을 수 있습니다. 자세한 내용은 [스팸 차단]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)을 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 이 엔드포인트를 사용해야 하나요, 아니면 일반 `/users/track`을 사용해야 하나요? {#should-i-use-this-endpoint-or-regular-userstrack}

두 가지 모두 사용하는 것을 권장합니다.

- 대규모 사용자 프로필 백필 및 동기화에는 `/users/track/bulk` 엔드포인트를 사용하세요.
- 실시간 사용 사례에는 `/users/track` 엔드포인트를 사용하세요.

### /users/track/bulk에서 어떤 식별자를 사용할 수 있나요? {#what-identifiers-can-i-use-in-userstrackbulk}

`external_id`, `braze_id`, `user_alias`, `email` 또는 `phone` 중 하나가 필수입니다. 더 많은 예시는 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object/), [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object/) 또는 [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/) 설명서를 참조하세요.

### 하나의 요청에 속성, 이벤트, 구매를 모두 포함할 수 있나요? {#can-i-include-attributes-events-and-purchases-in-one-request}

네. 요청당 최대 10,000개의 오브젝트까지 속성, 이벤트 및 구매 오브젝트를 원하는 만큼 조합하여 요청을 구성할 수 있습니다.


{% endapi %}