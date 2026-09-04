---
nav_title: "이벤트 객체"
article_title: "이벤트 객체"
page_order: 6
page_type: reference
description: "이 참고 문서에서는 이벤트 객체의 정의와 이벤트 객체가 이벤트 기반 Campaign 전략에서 어떻게 중요한 역할을 하는지에 대해 설명합니다."
---

# 이벤트 객체 {#event-object}

> 이 문서에서는 이벤트 객체의 다양한 구성요소, 이 객체를 사용하는 방법 및 참고할 수 있는 예제에 대해 설명합니다.

## 이벤트 객체란 무엇인가요? {#what-is-an-event-object}

이벤트 객체는 특정 이벤트가 발생할 때 API를 통해 전달되는 객체입니다. 이벤트 객체는 이벤트 배열 안에 포함됩니다. 이벤트 배열의 각 이벤트 객체는 지정된 시간 값에서 특정 사용자가 수행한 커스텀 이벤트의 단일 발생을 나타냅니다. 이벤트 객체에는 메시지, 데이터 수집 및 개인화에서 이벤트 속성정보를 설정하고 사용하여 커스터마이즈할 수 있는 다양한 필드가 있습니다.

특정 플랫폼에 대한 커스텀 이벤트 설정 단계는 [개발자 가이드]({{site.baseurl}}/developer_guide/home)의 플랫폼 통합 가이드를 참조하세요. 플랫폼에 따라 관련 문서를 참조하세요:

- [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [웹]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### 객체 본문 {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

{% alert note %}
미래 타임스탬프가 있는 이벤트는 기본적으로 현재 시간으로 설정됩니다. 이를 통해 커스텀 이벤트가 정확한 타이밍으로 기록됩니다.
{% endalert %}

- [외부 사용자 ID]({{site.baseurl}}/api/basics#user-ids)
- [앱 식별자]({{site.baseurl}}/api/identifier_types)
- [ISO 8601 시간 코드](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
일부 식별자 조합은 단일 요청에서 함께 사용할 수 없습니다. `email`과 `phone`이 모두 제공되면 `email`이 `phone`보다 우선합니다. 자세한 내용은 [식별자 확인]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution)을 참조하세요.
{% endalert %}

#### 기존 프로필만 업데이트 {#update-existing-profiles-only}

Braze에서 기존 고객 프로필만 업데이트하려면 요청 본문에 `_update_existing_only` 키를 `true` 값으로 전달해야 합니다. 이 값이 생략되면 `external_id`가 아직 존재하지 않는 경우 Braze가 새 고객 프로필을 생성합니다.

{% alert note %}
`/users/track` 엔드포인트를 통해 별칭 전용 고객 프로필을 생성하는 경우 `_update_existing_only`를 `false`로 설정해야 합니다. 이 값이 생략되면 별칭 전용 프로필이 생성되지 않습니다.
{% endalert %}

## 이벤트 속성정보 객체 {#event-properties-object}

커스텀 이벤트와 구매에는 이벤트 속성정보가 포함될 수 있습니다. "properties" 값은 키가 속성정보 이름이고 값이 속성정보 값인 객체여야 합니다. 속성정보 이름은 255자 이하의 비어 있지 않은 문자열이어야 하며, 달러 기호($)로 시작할 수 없습니다.

속성정보 값은 다음 데이터 유형 중 하나일 수 있습니다:

| 데이터 유형 | 설명 |
| --- | --- |
| 숫자 | [정수](https://en.wikipedia.org/wiki/Integer) 또는 [플로트](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| 불리언 | `true` 또는 `false` |
| 날짜/시간 | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 형식의 문자열이거나 다음 형식 중 하나여야 합니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>배열 내에서는 지원되지 않습니다. <br><br>참고: "T"는 시간 지정자이며 입력 안내가 아니므로 변경하거나 제거하면 안 됩니다. <br><br>시간대가 없는 시간 속성은 기본적으로 자정 UTC로 설정되며(대시보드에서는 회사 시간대의 자정 UTC에 해당하는 값으로 표시됩니다). <br><br>미래의 타임스탬프가 있는 이벤트는 현재 시간으로 기본 설정됩니다. |
| 문자열 | 255자 이하. |
| 배열 | 배열에는 날짜/시간을 포함할 수 없습니다. |
| 객체 | 객체는 문자열로 수집됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이벤트 속성정보 객체" }

배열 또는 객체 값을 포함하는 이벤트 속성정보 객체의 이벤트 속성정보 페이로드는 최대 100&nbsp;KB까지 가능합니다.

### 예약 키 {#reserved-keys}

다음 키는 예약되어 있으며 커스텀 이벤트 속성정보로 사용할 수 없습니다:

- `time`
- `event_name`

{% alert important %}
예약 키를 커스텀 이벤트 속성정보 이름으로 사용하면 `/users/track` 엔드포인트에 요청을 보낼 때 API 오류가 발생합니다.
{% endalert %}

### 이벤트 속성정보 지속성 {#event-property-persistence}

이벤트 속성정보는 상위 이벤트에 의해 트리거된 메시지의 필터링 및 Liquid 개인화를 위해 설계되었습니다. 기본적으로 Braze 사용자 프로필에 유지되지 않습니다. 세분화에서 이벤트 속성정보 값을 사용하려면 이벤트 속성정보 값을 장기적으로 저장하는 다양한 접근 방식을 자세히 설명하는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)를 참조하세요.

#### 이벤트 예제 요청 {#event-example-request}

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [ISO 8601 시간 코드 위키](http://en.wikipedia.org/wiki/ISO_8601)

## 이벤트 오브젝트 {#event-objects}

제공된 예시를 사용하여 누군가가 최근 예고편을 시청한 후 영화를 대여한 것을 확인할 수 있습니다. Campaign에 들어가 이러한 속성정보를 기반으로 사용자를 세분화할 수는 없지만, 이러한 속성정보를 영수증 형태로 활용하여 Liquid를 사용해 채널을 통해 커스텀 메시지를 전송하는 데 전략적으로 사용할 수 있습니다. 예를 들어, "안녕하세요 **Alex**, **Alex Smith**의 **The Sad Egg**를 대여해 주셔서 감사합니다. 대여 내역을 기반으로 추천 영화를 소개해 드립니다..."