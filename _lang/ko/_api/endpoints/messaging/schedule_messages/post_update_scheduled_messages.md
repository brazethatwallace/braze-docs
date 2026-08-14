---
nav_title: "POST: 예약된 메시지 업데이트"
article_title: "POST: 예약된 메시지 업데이트"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 예약된 메시지 업데이트 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 예약된 메시지 업데이트 {#update-scheduled-messages}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/messages/schedule/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 예약된 메시지를 업데이트합니다.

이 엔드포인트는 `schedule` 또는 `messages` 매개변수 또는 둘 다에 대한 업데이트를 허용합니다. 요청에는 두 키 중 하나 이상이 포함되어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `messages.schedule.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see available messaging objects documentation
  }
}
```
## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | 필수 | 문자열 | 업데이트할 `schedule_id`(스케줄 생성 응답에서 얻은 값)입니다. |
| `schedule` | 선택 사항 | 오브젝트 | [스케줄 오브젝트]({{site.baseurl}}/api/objects_filters/schedule_object)를 참조하세요. |
| `messages` | 선택 사항 | 오브젝트 | [사용 가능한 메시징 오브젝트]({{site.baseurl}}/api/objects_filters#messaging-objects)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
    "apple_push": {
      "alert": "Updated Message!",
      "badge": 1
    },
    "android_push": {
      "title": "Updated title!",
      "alert": "Updated message!"
    },
    "sms": {
      "subscription_group_id": "subscription_group_identifier",
      "message_variation_id": "message_variation_identifier",
      "body": "This is my SMS body.",
      "app_id": "app_identifier"
    }
  }
}'
```

{% endapi %}