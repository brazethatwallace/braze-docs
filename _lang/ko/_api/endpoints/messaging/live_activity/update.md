---
nav_title: "POST: 실시간 활동 업데이트"
article_title: "POST: 실시간 활동 업데이트"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 실시간 활동 업데이트 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 실시간 활동 업데이트 {#update-live-activity}
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 iOS 앱에 표시되는 [실시간 활동]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?sdktab=swift)을 업데이트하고 종료할 수 있습니다. 이 엔드포인트에는 추가 설정이 필요합니다.

실시간 활동을 등록한 후 JSON 페이로드를 전달하여 Apple 푸시 알림 서비스(APNs)를 업데이트할 수 있습니다. 자세한 내용은 [푸시 알림 페이로드로 실시간 활동 업데이트하기](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications)에 대한 Apple 설명서를 참조하세요.

`content-available`이 설정되지 않은 경우 기본 Apple 푸시 알림 서비스(APNs) 우선순위는 10입니다. `content-available`이 설정된 경우 이 우선순위는 5입니다. 자세한 내용은 [Apple 푸시 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/apple_object)를 참조하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 다음을 완료해야 합니다:

- `messages.live_activity.update` 권한으로 API 키를 생성합니다.
- Braze Swift SDK를 사용하여 실시간 활동을 [원격]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?tab=remote&sdktab=swift) 또는 [로컬]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?tab=local&sdktab=swift)로 등록합니다.

{% multi_lang_include api/payload_size_alert.md %}

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```json
{
   "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
   "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
   "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
   "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
   "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
   "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
   "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
 }
 ```

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `app_id` | Required | String | App [API identifier]({{site.baseurl}}/api/identifier_types#app-identifier) retrieved from the [API Keys]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) page.  |
| `activity_id` | Required | String | When you register your Live Activity using [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class), you use the `pushTokenTag` parameter to name the Activity's push token to a custom string.<br><br>Set `activity_id` to this custom string to define which Live Activity you want to update. |
| `content_state` | Required | Object | You define the `ContentState` parameters when you create your Live Activity. Pass the updated values for your `ContentState` using this object.<br><br>The format of this request must match the shape you initially defined. |
| `end_activity` | Optional | Boolean | If `true`, this request ends the Live Activity. |
| `dismissal_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter defines the time to remove the Live Activity from the user's UI. If this time is in the past and `end_activity` is `true`, the Live Activity will be removed immediately.<br><br> If `end_activity` is `false` or omitted, this parameter only updates the Live Activity.|
| `stale_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter tells the system when the Live Activity content is marked as outdated in the user's UI. |
| `notification` | Optional | Object | Include an [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object) object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. {::nomarkdown}<ul><li>If a <code>notification</code> is included and the user is active on their iPhone when the update is delivered, the updated Live Activity UI will slide down and display like a push notification.</li><li>If a <code>notification</code> is included and the user is not active on their iPhone, their screen will light up to display the updated Live Activity UI on their lock screen.</li><li>The <code>notification alert</code> will not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the <code>alert</code> will be displayed there.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Example request

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It's halftime! Let's look at the scores",
            "title": "Halftime"
        }
    }
}'
```

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `201`과 `4XX` 두 가지입니다.

### 성공 응답 예시 {#example-success-response}

요청 형식이 올바르게 지정되어 요청을 수신한 경우 `201` 상태 코드가 반환됩니다. `201` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

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