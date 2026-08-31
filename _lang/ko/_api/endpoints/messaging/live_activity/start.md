---
nav_title: "POST: 라이브 활동 시작"
article_title: "POST: 라이브 활동 시작"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 라이브 활동 시작 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 라이브 활동 시작 {#start-live-activity}
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> 이 엔드포인트를 사용하여 iOS 앱에 표시되는 [라이브 활동]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?sdktab=swift)을 원격으로 시작할 수 있습니다. 이 엔드포인트에는 추가 설정이 필요합니다.

라이브 활동을 생성한 후에는 세그먼트, 연결된 오디언스 또는 특정 사용자를 타겟팅하도록 POST 요청을 수행합니다. 외부 사용자 ID, 사용자 별칭 또는 두 가지 모두를 사용하여 특정 사용자를 식별합니다. Apple의 라이브 활동에 대한 자세한 내용은 [ActivityKit 푸시 알림으로 라이브 활동 시작 및 업데이트](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications)를 참조하세요.

`content-available`이 설정되지 않은 경우 기본 Apple 푸시 알림 서비스(APNs) 우선순위는 10입니다. `content-available`이 설정된 경우 이 우선순위는 5입니다. 자세한 내용은 [Apple 푸시 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/apple_object)를 참조하세요.

{% alert tip %}
라이브 활동을 종료하려면 [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) 엔드포인트에서 `end_activity`를 `true`로 설정하여 사용하세요.
{% endalert %}

## 자동 해제 설정 {#arranging-automatic-dismissal}

라이브 활동이 시작된 후 자동 해제를 설정하려면 백엔드에서 업데이트 엔드포인트로 후속 요청을 스케줄하세요.

1. 나중에 재사용할 수 있는 `activity_id`와 함께 `/messages/live_activity/start` 요청을 보냅니다.
2. 해당 `activity_id`와 목표 종료 시간을 백엔드 스케줄러에 저장합니다.
3. 목표 종료 시간에 `end_activity`를 `true`로 설정하여 `/messages/live_activity/update` 요청을 보냅니다.
4. 동일한 업데이트 요청에서 해제 동작을 구성합니다. 자세한 내용은 [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) 엔드포인트를 참조하세요.
5. [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 전송 및 성과 이벤트를 확인합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 다음을 완료해야 합니다:

- `messages.live_activity.start` 권한으로 API 키를 생성합니다.
- Braze Swift SDK를 사용하여 [라이브 활동을 생성합니다]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?tab=local&sdktab=swift#swift_create-an-activity).

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
특정 사용자를 타겟팅할 때 Braze는 기존 사용자로 확인되는 `external_user_ids` 및 `user_aliases`에 대해서만 라이브 활동을 시작합니다.
{% endalert %}

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. Use this ID to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app.",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Include `notification.alert.title` and `notification.alert.body`.",
  // Include one targeting method:
  // 1. "external_user_ids", "user_aliases", or both (combined maximum 50)
  // 2. "custom_audience"
  // 3. "segment_id"
  "external_user_ids": "(optional, array of strings) see external user identifier",
  "user_aliases": "(optional, array of user alias objects) see user alias object",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|-----------|----------|----------|--------------|
| `app_id` | 필수 | 문자열 | [API 키]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) 페이지에서 가져온 앱 [API 식별자]({{site.baseurl}}/api/identifier_types#app-identifier)입니다. |
| `activity_id` | 필수 | 문자열 | 커스텀 문자열을 `activity_id`로 정의합니다. 이 ID를 사용하여 라이브 활동에 업데이트 또는 종료 이벤트를 보냅니다. |
| `activity_attributes_type` | 필수 | 문자열 | 앱의 `liveActivities.registerPushToStart` 내에서 정의하는 활동 속성 유형입니다. |
| `activity_attributes` | 필수 | 오브젝트 | 활동 유형에 대한 정적 속성 값(예: 변경되지 않는 스포츠 팀 이름)입니다. |
| `content_state` | 필수 | 오브젝트 | 라이브 활동을 생성할 때 `ContentState` 매개변수를 정의합니다. 이 오브젝트를 사용하여 `ContentState`의 업데이트된 값을 전달합니다.<br><br>이 요청의 형식은 처음에 정의한 형태와 일치해야 합니다. |
| `stale_date` | 선택 사항 | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 이 매개변수는 라이브 활동 콘텐츠가 사용자 UI에서 오래된 것으로 표시되는 시점을 시스템에 알려줍니다. |
| `notification` | 필수 | 오브젝트 | [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object) 오브젝트를 포함하여 푸시 알림을 정의합니다. 이 푸시 알림의 동작은 사용자가 활성 상태인지 또는 프록시 기기를 사용 중인지에 따라 다릅니다. {::nomarkdown}<ul><li><code>notification</code>이 포함되어 있고 업데이트가 전달될 때 사용자가 iPhone에서 활성 상태이면, 업데이트된 라이브 활동 UI가 아래로 슬라이드되어 푸시 알림처럼 표시됩니다.</li><li><code>notification</code>이 포함되어 있고 사용자가 iPhone에서 활성 상태가 아니면, 잠금 화면에 업데이트된 라이브 활동 UI가 표시되도록 화면이 켜집니다.</li><li><code>notification alert</code>는 표준 푸시 알림으로 표시되지 않습니다. 또한 사용자에게 Apple Watch와 같은 프록시 기기가 있는 경우에는 <code>alert</code>가 해당 기기에 표시됩니다.</li></ul>{:/} |
| `external_user_ids` | `user_aliases`, `segment_id` 또는 `custom_audience` 제공 시 선택 사항 | 문자열 배열 | [외부 사용자 ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)를 참조하세요. |
| `user_aliases` | `external_user_ids`, `segment_id` 또는 `custom_audience` 제공 시 선택 사항 | 사용자 별칭 오브젝트 배열 | [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object)를 참조하세요. |
| `segment_id` | `external_user_ids`, `user_aliases` 또는 `custom_audience` 제공 시 선택 사항 | 문자열 | [세그먼트 식별자]({{site.baseurl}}/api/identifier_types)를 참조하세요. |
| `custom_audience` | `external_user_ids`, `user_aliases` 또는 `segment_id` 제공 시 선택 사항 | 연결된 오디언스 오브젝트 | [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="요청 매개변수" }

동일한 요청에 `external_user_ids`와 `user_aliases`를 포함할 수 있습니다. 두 배열의 합산 길이는 50을 초과할 수 없습니다. Braze는 두 매개변수 중 하나와 일치하는 사용자를 타겟팅하며, 여러 식별자가 동일한 사용자로 확인되는 경우 한 번만 전송합니다.

`external_user_ids` 또는 `user_aliases`를 `segment_id` 또는 `custom_audience`와 함께 사용하지 마세요. 이 엔드포인트에서는 `custom_audience`를 사용하여 연결된 오디언스 필터를 전달합니다.

## 요청 예시 {#example-request}

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR_REST_API_KEY}' \
--data-raw '{
  "app_id": "{YOUR_APP_API_IDENTIFIER}",
  "activity_id": "football-chiefs-bills-2024-01-21",
  "content_state": {
    "teamOneScore": 0,
    "teamTwoScore": 0
  },
  "activity_attributes_type": "FootballActivity",
  "activity_attributes": {
    "team1Name": "Chiefs",
    "team2Name": "Bills"
  },
  "stale_date": "2024-01-22T16:55:49+0000",
  "notification": {
    "alert": {
      "body": "The game is starting! Tune in soon!",
      "title": "Chiefs v. Bills"
    }
  },
  "external_user_ids": ["user-id1", "user-id2"],
  "user_aliases": [
    {
      "alias_name": "user-name",
      "alias_label": "user-label"
    }
  ]
}'
```

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `201`과 `4XX` 두 가지입니다.

### 성공 응답 예시 {#example-success-response}

요청 형식이 올바르게 지정되어 Braze가 수신한 경우 `201` 상태 코드가 반환됩니다. `201` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답 예시 {#example-error-response}

`4XX` 상태 코드 클래스는 클라이언트 오류를 나타냅니다. 발생할 수 있는 오류에 대한 자세한 내용은 [API 오류 및 응답 문서]({{site.baseurl}}/api/errors)를 참조하세요.

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}