---
nav_title: "POST: Start live activity"
article_title: "POST: Start Live Activity"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Start Live Activity endpoint."
---
{% api %}
# Start Live Activity
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Use this endpoint to remotely start [Live Activities]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift) displayed in your iOS app. This endpoint requires additional setup.

After you create a Live Activity, make a POST request to target a segment, a connected audience, or specific users. Identify specific users by external user ID, user alias, or both. For more information about Apple's Live Activities, see [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).

If `content-available` isn't set, the default Apple Push Notification service (APNs) priority is 10. If `content-available` is set, this priority is 5. For more information, see [Apple push object]({{site.baseurl}}/api/objects_filters/messaging/apple_object).

{% alert tip %}
To end a Live Activity, use the [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) endpoint with `end_activity` set to `true`.
{% endalert %}

## Arranging automatic dismissal

To arrange automatic dismissal after a Live Activity starts, schedule a follow-up request to the update endpoint from your backend.

1. Send a `/messages/live_activity/start` request with an `activity_id` you can reuse later.
2. Store that `activity_id` and your target end time in your backend scheduler.
3. At the target end time, send a `/messages/live_activity/update` request with `end_activity` set to `true`.
4. Configure dismissal behavior in the same update request. For details, see the [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) endpoint.
5. Verify send and outcome events in the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Prerequisites

To use this endpoint, complete the following prerequisites:

- Generate an API key with the `messages.live_activity.start` permission.
- [Create a Live Activity]({{site.baseurl}}/developer_guide/live_notifications/live_activities?tab=local&sdktab=swift#create-an-activity) using the Braze Swift SDK.

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
When you target specific users, Braze starts a Live Activity only for `external_user_ids` and `user_aliases` that resolve to existing users.
{% endalert %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

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

## Request parameters

| Parameter | Required | Data Type| Description  |
|-----------|----------|----------|--------------|
| `app_id` | Required | String | App [API identifier]({{site.baseurl}}/api/identifier_types#app-identifier) retrieved from the [API Keys]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) page.  |
| `activity_id` | Required | String  | Define a custom string as your `activity_id`. Use this ID to send update or end events to your Live Activity.  |
| `activity_attributes_type`  | Required | String | The activity attributes type you define within `liveActivities.registerPushToStart` in your app.  |
| `activity_attributes` | Required | Object  | The static attribute values for the activity type (such as the sports team names, which don't change). |
| `content_state` | Required | Object  | You define the `ContentState` parameters when you create your Live Activity. Pass the updated values for your `ContentState` using this object.<br><br>The format of this request must match the shape you initially defined. |
| `stale_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter tells the system when the Live Activity content is marked as outdated in the user's UI. |
| `notification` | Required | Object | Include an [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object) object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. {::nomarkdown}<ul><li>If a <code>notification</code> is included and the user is active on their iPhone when the update is delivered, the updated Live Activity UI slides down and displays like a push notification.</li><li>If a <code>notification</code> is included and the user is not active on their iPhone, their screen lights up to display the updated Live Activity UI on their lock screen.</li><li>The <code>notification alert</code> does not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the <code>alert</code> displays there.</li></ul>{:/} |
| `external_user_ids` | Optional if `user_aliases`, `segment_id`, or `custom_audience` is provided | Array of strings | See [external user ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields). |
| `user_aliases` | Optional if `external_user_ids`, `segment_id`, or `custom_audience` is provided | Array of user alias objects | See [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object). |
| `segment_id`  | Optional if `external_user_ids`, `user_aliases`, or `custom_audience` is provided | String    | See [segment identifier]({{site.baseurl}}/api/identifier_types). |
| `custom_audience` | Optional if `external_user_ids`, `user_aliases`, or `segment_id` is provided | Connected audience object  | See [connected audience]({{site.baseurl}}/api/objects_filters/connected_audience). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

You can include `external_user_ids` and `user_aliases` in the same request. Their combined array length can't exceed 50. Braze targets users who match either parameter and sends only once when multiple identifiers resolve to the same user.

Don't combine `external_user_ids` or `user_aliases` with `segment_id` or `custom_audience`. On this endpoint, use `custom_audience` to pass connected audience filters.

## Example request

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

## Response

There are two status code responses for this endpoint: `201` and `4XX`.

### Example success response

A `201` status code returns if the request is formatted correctly and Braze receives it. The status code `201` can return the following response body.

```json
{
  "message": "success"
}
```

### Example error response

The `4XX` class of status code indicates a client error. Refer to the [API errors and responses article]({{site.baseurl}}/api/errors) for more information about errors you may encounter.

The status code `400` could return the following response body.

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
