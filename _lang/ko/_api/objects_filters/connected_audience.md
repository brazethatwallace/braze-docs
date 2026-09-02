---
nav_title: "연결된 오디언스 필터 및 오브젝트"
article_title: API 연결된 오디언스 오브젝트
page_order: 3
page_type: reference
description: "이 문서에서는 연결된 오디언스 오브젝트의 작동 방식, 사용 사례, 그리고 이를 구성하는 다양한 필터에 대해 설명합니다."
---

# 연결된 오디언스 오브젝트 {#connected-audience-object}

> 연결된 오디언스는 API 요청 내에서 인라인으로 정의하는 동적 오디언스 필터로, Braze 대시보드에서 Segment를 생성하거나 관리하지 않고도 발송 시점에 적합한 사용자를 타겟팅할 수 있습니다.

가능한 모든 오디언스 조합에 대해 Segment를 미리 만드는 대신, API 호출에 필터 기준을 직접 전달합니다. 엔드포인트에 따라 이 오브젝트는 `audience` 또는 `custom_audience`로 전달됩니다. Braze는 각 사용자를 해당 기준에 따라 실시간으로 평가하고, 조건에 일치하는 사용자에게만 메시지를 전달합니다. 즉, 단일 Campaign, Canvas 또는 API 전용 메시지 정의로 비즈니스 로직에 따라 무제한의 오디언스 변형을 처리할 수 있습니다.

## 작동 방식 {#how-it-works}

1. Braze 대시보드에서 API 트리거 Campaign 또는 Canvas를 생성하여 메시지를 정의하거나, API 요청의 [메시징 오브젝트]({{site.baseurl}}/api/objects_filters#messaging-objects)를 사용하여 메시지 콘텐츠를 전적으로 인라인으로 정의합니다. 동적 개인화를 위해 [트리거 속성]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 또는 [Canvas 컨텍스트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)를 사용합니다.
2. 지원되는 엔드포인트를 호출하고, `audience` 파라미터(또는 `/messages/live_activity/start`의 경우 `custom_audience`)에 연결된 오디언스 필터를 포함합니다. 커스텀 속성, 푸시 구독 상태, 이메일 구독 상태, 마지막 앱 사용 시간 기준으로 필터링할 수 있습니다.
3. Braze가 전송 시점에 필터를 평가하여, 기준에 맞는 사용자에게만 메시지를 전달합니다.

{% alert tip %}
`audience` 파라미터를 사용할 때는 `campaign_id`가 필수가 아닙니다. [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) 및 [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) 엔드포인트를 사용하면 사전 생성된 Campaign 없이도 메시지 콘텐츠를 인라인으로 정의할 수 있습니다. 그러나 대시보드에서 Campaign 수준의 측정기준(예: 전송, 클릭 또는 반송)을 추적하려면 `campaign_id`를 포함하세요.
{% endalert %}

오디언스가 요청별로 정의되므로, 백엔드 시스템에서 대시보드 개입 없이 비즈니스 이벤트(가격 변동, 기상 경보, 실시간 스코어 업데이트 등)에 대응하여 상황별로 관련성 있는 메시지를 트리거할 수 있습니다.

### 호환 엔드포인트 {#compatible-endpoints}

다음 엔드포인트에서 연결된 오디언스 오브젝트를 사용할 수 있습니다.

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) (`custom_audience` 사용)

`audience` 파라미터는 오브젝트 배열을 지원하지 않습니다.

## 사용 사례 {#use-cases}

커넥티드 오디언스는 백엔드 시스템이 이벤트를 감지하고 동적으로 결정된 사용자 집합에 알림을 보내야 하는 시나리오에서 사용합니다.

| 카테고리 | 예시 |
| --- | --- |
| 날씨 알림 | 날씨 데이터 제공업체가 심각한 기상 이벤트를 감지하고, `preferred_city` 속성이 영향을 받는 지역과 일치하는 사용자에게 푸시 알림을 보냅니다. |
| 스포츠 및 실시간 이벤트 | 스포츠 앱이 `favorite_team` 속성이 경기 중인 팀 중 하나와 일치하는 사용자에게 실시간 스코어 업데이트 또는 경기 알림을 보냅니다. |
| 콘텐츠 및 엔터테인먼트 | 스트리밍 서비스가 새 에피소드가 공개될 때마다 `favorite_shows` 배열에 해당 시리즈 제목이 포함된 사용자에게 알림을 보냅니다. |
| 이커머스 | 온라인 소매업체가 `wishlisted_products` 배열에 관련 제품 ID가 포함된 사용자에게 가격 인하 또는 재입고 알림을 보냅니다. |
| 여행 | 여행 앱이 `booked_flight` 속성이 영향을 받는 항공편 번호와 일치하는 사용자에게 항공편 지연 알림을 보냅니다. |
| 금융 서비스 | 트레이딩 플랫폼이 `watchlist` 배열에 가격 임계값을 넘은 주식 종목 코드가 포함된 사용자에게 알림을 보냅니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 사례" }

각 경우에 단일 Campaign 또는 API 전용 메시지 정의가 모든 변형을 처리합니다. 백엔드에서 필터 값을 결정하고 API 요청에 전달하므로, 각 제품, 프로그램, 팀 또는 위치별로 별도의 Segment나 Campaign을 만들 필요가 없습니다.

## 요청 예시 {#example-request}

다음 예시에서는 [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) 엔드포인트를 사용하여 특정 프로그램을 즐겨찾기에 추가하고 푸시 알림 수신에 옵트인한 사용자를 타겟팅합니다.

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## 오브젝트 본문 {#object-body}

연결된 오디언스 오브젝트는 단일 연결된 오디언스 필터 또는 `AND` 및 `OR` 연산자로 결합된 여러 연결된 오디언스 필터로 구성됩니다.

**다중 필터 예시:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## 연결된 오디언스 필터 {#connected-audience-filters}

여러 필터를 `AND` 및 `OR` 연산자와 결합하여 연결된 오디언스 필터를 만들 수 있습니다.

### 고려 사항 {#considerations}

연결된 오디언스는 다음 기준으로 사용자를 필터링할 수 없습니다:

 - 기본 속성
 - 커스텀 이벤트
 - Segments
 - 메시지 인게이지먼트 이벤트
 - 중첩 커스텀 속성

이러한 필터를 사용하려면 오디언스 Segment에 포함한 다음, [`/messages/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)의 `segment_id` 파라미터에 해당 Segment를 지정하는 것이 좋습니다. 다른 엔드포인트를 사용하는 경우, 먼저 Braze 대시보드에서 API 트리거 Campaign 또는 Canvas에 Segment를 추가해야 합니다. 중첩 속성으로 필터링해야 하는 경우, 대신 [표준 Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)를 사용하세요.


### 커스텀 속성 필터 {#custom-attribute-filter}

이 필터를 사용하면 사용자의 커스텀 속성을 기준으로 세분화할 수 있습니다. 이 필터에는 최대 세 개의 필드가 포함됩니다:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### 데이터 유형별 허용 비교 {#allowed-comparisons-by-data-type}

커스텀 속성의 데이터 유형에 따라 지정된 필터에 유효한 비교가 결정됩니다.

| 커스텀 속성 유형 | 허용되는 비교 |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="데이터 유형별 허용 비교" }

#### 속성 비교 시 주의 사항 {#attribute-comparison-caveats}

| 비교 | 추가 고려 사항 |
| --- | --- |
| `value` | `exists` 또는 `does_not_exist` 비교를 사용하는 경우 `value`는 필수가 아닙니다. `before` 및 `after` 비교를 사용하는 경우 `value`는 ISO 8601 날짜/시간 문자열이어야 합니다. |
| `matches_regex` | `matches_regex` 비교를 사용하는 경우, 전달되는 값은 문자열이어야 합니다. Braze에서 정규표현식을 사용하는 방법에 대한 자세한 내용은 [정규표현식]({{site.baseurl}}/user_guide/audience/segments/regex) 및 [커스텀 속성 데이터 유형]({{site.baseurl}}/developer_guide/analytics#custom-attribute-data-types)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="속성 비교 시 주의 사항" }

#### 다중 값 비교 {#multi-value-comparisons}

`is_any_of`와 `is_none_of` 모두 단일 비교에서 여러 값과 매칭을 지원합니다. 이러한 비교는 문자열과 배열 커스텀 속성 모두에서 사용할 수 있습니다.

- `is_any_of`: 속성 값이 제공된 값 중 하나와 일치하는 사용자를 매칭합니다. `value`는 단일 문자열 또는 문자열 배열일 수 있습니다.
- `is_none_of`: 속성 값이 제공된 값 중 어느 것과도 일치하지 않는 사용자를 매칭합니다. `value`는 단일 문자열 또는 문자열 배열일 수 있습니다. 프로필에 해당 속성이 없는 사용자는 항상 이 비교에 부합합니다.

배열 속성의 경우:

- `includes_value`는 사용자의 배열에 지정된 값 중 하나라도 포함되어 있는지 확인하기 위해 값 배열도 허용할 수 있습니다.
- 배열 속성에서 `is_any_of` 또는 `is_none_of`를 사용하면 각각 `includes_value` 및 `does_not_include_value`와 동일하게 작동합니다.

{% alert tip %}
다중 값 매칭의 경우, `includes_value` 대신 `is_any_of`를 사용하세요.
{% endalert %}

#### 커스텀 속성 예시 {#custom-attribute-examples}

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```

#### 다중 값 비교 예시 {#multi-value-comparison-examples}

##### 문자열 배열을 사용한 `is_any_of` {#is_any_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_color",
    "comparison": "is_any_of",
    "value": ["red", "blue", "green"]
  }
}
```

##### 문자열 배열을 사용한 `is_none_of` {#is_none_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscription_tier",
    "comparison": "is_none_of",
    "value": ["bronze", "silver"]
  }
}
```

##### 배열을 사용한 `includes_value` (배열 속성) {#includes_value-with-an-array-array-attribute}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscribed_products",
    "comparison": "includes_value",
    "value": ["1001", "1002", "1003"]
  }
}
```

이는 `subscribed_products` 배열에 `"1001"`, `"1002"` 또는 `"1003"` 값 중 하나라도 포함된 사용자를 매칭합니다.

### 푸시 구독 필터 {#push-subscription-filter}

이 필터를 사용하면 사용자의 푸시 구독 상태를 기준으로 세분화할 수 있습니다.

#### 필터 본문 {#filter-body}

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **허용되는 비교:** `is`, `is_not`
- **허용되는 값:** `opted_in`, `subscribed`, `unsubscribed`

### 이메일 구독 필터 {#email-subscription-filter}

이 필터를 사용하면 사용자의 이메일 구독 상태를 기준으로 세분화할 수 있습니다.

#### 필터 본문

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **허용되는 비교:** `is`, `is_not`
- **허용되는 값:** `opted_in`, `subscribed`, `unsubscribed`

### 마지막 앱 사용 필터 {#last-used-app-filter}

이 필터를 사용하면 사용자가 마지막으로 앱을 사용한 시점을 기준으로 세분화할 수 있습니다. 이 필터에는 두 개의 필드가 포함됩니다:

#### 필터 본문

```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **허용되는 비교:** `after`, `before`
- **허용되는 값:** datetime (ISO 8601 문자열)