---
nav_title: "POST: 사용자 생성 및 업데이트 (동기)"
article_title: "POST: 사용자 생성 및 업데이트 (동기)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "이 문서에서는 동기식 사용자 추적 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 생성 및 업데이트 (동기) {#create-and-update-users-synchronous}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> 이 엔드포인트를 사용하여 커스텀 이벤트와 구매를 기록하고 사용자 프로필 속성을 동기식으로 업데이트할 수 있습니다. 이 엔드포인트는 비동기식으로 사용자 프로필을 업데이트하는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)와 유사하게 작동합니다.

{% alert important %}
이 엔드포인트는 현재 **제한된 베타** 상태입니다. 현재 베타에 새로운 고객을 추가하고 있지 않지만, 이 기능이 Braze 통합에 유용할 것 같다면 Braze 계정 매니저에게 알려주세요.
{% endalert %}

## 동기 및 비동기 API 호출 {#synchronous-and-asynchronous-api-calls}

비동기 호출에서 API는 상태 코드 `201`을 반환하여 요청이 성공적으로 수신되고 이해되었으며 수락되었음을 나타냅니다. 그러나 이것이 요청이 완전히 완료되었다는 것을 의미하지는 않습니다.

동기 호출에서 API는 상태 코드 `201`을 반환하여 요청이 성공적으로 수신되고 이해되었으며 수락되고 완료되었음을 나타냅니다. 호출 응답은 작업 결과로 선택된 사용자 프로필 필드를 보여줍니다.

이 엔드포인트는 `/users/track` 엔드포인트보다 사용량 제한이 낮습니다([사용량 제한](#rate-limit) 참조). 각 `/users/track/sync` 요청에는 하나의 이벤트 오브젝트, 하나의 속성 오브젝트 **또는** 하나의 구매 오브젝트만 포함할 수 있습니다. 이 엔드포인트는 동기 호출이 필요한 사용자 프로필 업데이트를 위해 예약해야 합니다. 건전한 구현을 위해 `/users/track/sync`와 `/users/track`을 함께 사용하는 것을 권장합니다.

예를 들어 동일한 사용자에 대해 짧은 시간 동안 연속적인 요청을 보내는 경우 비동기식 `/users/track` 엔드포인트에서는 경합 조건이 발생할 수 있지만, `/users/track/sync` 엔드포인트를 사용하면 `2XX` 응답을 받은 후 각 요청을 순차적으로 보낼 수 있습니다.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.track.sync` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key)가 필요합니다.

서버 간 호출에 API를 사용하는 고객이 방화벽 뒤에 있는 경우 `rest.iad-01.braze.com`을 허용 목록에 추가해야 할 수 있습니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/sync" %}

모든 고객에 대해 이 엔드포인트에 분당 500건의 기본 속도 제한을 적용합니다. 각 `/users/track/sync` 요청에는 최대 하나의 이벤트 오브젝트, 하나의 속성 오브젝트 또는 하나의 구매 오브젝트가 포함될 수 있습니다. 각 오브젝트(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있습니다.

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### 요청 매개변수 {#request-parameters}

{% alert important %}
다음 표에 나열된 각 요청 구성요소에 대해 `external_id`, `user_alias`, `braze_id`, `email` 또는 `phone` 중 하나를 포함해야 합니다.
{% endalert %}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `attributes` | 선택 사항 | 하나의 속성 오브젝트 | [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens) 보기 |
| `events` | 선택 사항 | 하나의 이벤트 오브젝트 | [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object) 보기 |
| `purchases` | 선택 사항 | 하나의 구매 오브젝트 | [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object) 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 응답 {#responses}

이 엔드포인트의 [요청 매개변수](#request-parameters)를 사용할 때 성공 메시지 또는 심각한 오류가 있는 메시지 중 하나의 응답을 받게 됩니다.

### 성공 메시지 {#successful-message}

성공 메시지는 Braze가 업데이트한 사용자 프로필 데이터에 대한 정보를 포함하는 다음 응답을 반환합니다.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Braze lists only custom attributes from the request,
        "custom_events": (optional, object), the custom events as a result of the request. Braze lists only custom events from the request,
        "purchase_events": (optional, object), the purchase events as a result of the request. Braze lists only purchase events from the request,
    },
    "message": "success"
```

### 심각한 오류가 있는 메시지 {#message-with-fatal-errors}

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

## 요청 및 응답 예시 {#example-requests-and-responses}

### 외부 ID로 커스텀 속성 업데이트 {#update-a-custom-attribute-by-external-id}

#### 요청 {#request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### 응답 {#response}

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
```

### 이메일로 커스텀 이벤트 업데이트 {#update-a-custom-event-by-email}

#### 요청

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "events": [
        {
            "email": "test@example.com",
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

#### 응답

```
{
    "users": [
        {
            "email": "test@example.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
```

### 사용자 별칭으로 구매 이벤트 업데이트 {#update-a-purchase-event-by-user-alias}

#### 요청

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### 응답

```
{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
```

## 자주 묻는 질문 {#frequently-asked-questions}

### 비동기식 엔드포인트와 동기식 엔드포인트 중 무엇을 사용해야 하나요? {#should-i-use-the-asynchronous-or-synchronous-endpoint}

대부분의 프로필 업데이트의 경우 `/users/track` 엔드포인트가 더 높은 사용량 제한과 요청을 배치할 수 있는 유연성 덕분에 가장 적합합니다. 그러나 `/users/track/sync` 엔드포인트는 동일한 사용자에 대한 빠른 연속 요청으로 인해 경합 조건이 발생하는 경우 유용합니다.

### 응답 시간이 `/users/track` 엔드포인트와 다른가요? {#does-the-response-time-differ-from-the-userstrack-endpoint}

동기 호출에서는 API가 Braze가 요청을 완료할 때까지 기다린 후 응답을 반환합니다. 그 결과, 동기 요청은 평균적으로 `/users/track`에 대한 비동기 요청보다 더 오래 걸립니다. 대부분의 요청에 대해 몇 초 내에 응답을 받을 수 있습니다.

### 동시에 여러 요청을 보낼 수 있나요? {#can-i-send-multiple-requests-at-the-same-time}

예, 요청이 서로 다른 사용자를 대상으로 하거나 각 요청이 한 사용자에 대해 서로 다른 속성, 이벤트, 구매를 업데이트하는 경우에 가능합니다.

동일한 속성, 이벤트 또는 구매에 대해 한 사용자에게 여러 요청을 보내는 경우, Braze는 경합 조건이 발생하지 않도록 각 요청 사이에 성공 응답을 기다릴 것을 권장합니다.

동일한 사용자에 대해 `/users/track`을 빠르게 연속 호출할 때 여전히 일관되지 않은 프로필 상태가 나타나면, 해당 업데이트를 `/users/track/sync`로 전환하고 한 번에 하나의 요청을 보내면서 다음 요청 전에 각 `2XX` 응답을 기다리세요. 이 순서가 긴밀한 루프나 병렬 워커 간의 읽기-후-쓰기 경합 조건을 방지하는 지원되는 방법입니다.

### 응답 값이 원래 요청의 값과 일치하지 않는 이유는 무엇인가요? {#why-doesnt-the-response-value-match-the-one-in-my-original-request}

요청이 완료되었더라도 커스텀 속성 값이 업데이트되지 않았을 수 있습니다. 이는 커스텀 속성 업데이트가 최대 문자 수를 초과하거나, 배열 제한을 초과하거나, 사용자가 Braze에 존재하지 않는데 `_update_existing_only = true`로 설정된 경우에 발생할 수 있습니다.

이러한 경우 응답을 요청이 완료되었지만 원하는 업데이트가 이루어지지 않았다는 표시로 간주하세요. [응답 값이 원래 요청의 값과 일치하지 않는 이유는 무엇인가요?](#why-doesnt-the-response-value-match-the-one-in-my-original-request)에 나열된 이유를 참고하여 문제를 해결하세요.

{% endapi %}