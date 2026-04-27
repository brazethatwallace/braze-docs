---
nav_title: "POST: API 트리거 전달을 사용하여 Canvas 메시지 보내기"
article_title: "POST: API 트리거 전달을 사용하여 Canvas 메시지 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 트리거 전달을 사용한 Canvas 보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# API 트리거 전달을 사용하여 Canvas 메시지 보내기 {#send-canvas-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> 이 엔드포인트를 사용하여 API 트리거 전달을 통해 Canvas 메시지를 전송할 수 있습니다.

API 트리거 전달을 사용하면 메시지 콘텐츠를 Braze 대시보드에 저장하는 동시에 API를 사용하여 메시지를 언제, 누구에게 보낼지 지정할 수 있습니다.

이 엔드포인트로 메시지를 보내려면 먼저 [Canvas ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)(Canvas를 구축할 때 생성됨)가 있어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `canvas.trigger.send` 권한으로 API 키를 생성해야 합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "context": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent `context`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | 필수 | 문자열 | [Canvas 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하세요. |
| `context` | 선택 사항 | 오브젝트 | Canvas 진입 등록정보를 포함합니다. 개인화 키-값 페어는 이 요청의 모든 사용자에게 적용됩니다. 컨텍스트 오브젝트는 최대 50KB까지 가능합니다. |
| `broadcast` | 선택 사항 | 부울 | Braze 대시보드에서 Canvas의 타겟 오디언스로 구성된 전체 Segment에 메시지를 보낼 때 `broadcast`를 true로 설정해야 합니다. 이 매개변수는 기본적으로 false로 설정됩니다(2017년 8월 31일 기준). <br><br> `broadcast`가 true로 설정되면 `recipients` 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 오디언스에게 메시지를 보낼 수 있으므로 `broadcast: true`를 설정할 때는 주의하세요. |
| `audience` | 선택 사항 | 연결된 오디언스 오브젝트 | [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/)를 참조하세요. `audience`를 포함하면 메시지는 커스텀 속성 및 구독 상태와 같은 정의된 필터와 일치하는 사용자에게만 전송됩니다. |
| `recipients` | 선택 사항 | 배열 | [수신자 오브젝트]({{site.baseurl}}/api/objects_filters/recipient_object/)를 참조하세요. <br><br>제공되지 않고 `broadcast`가 `true`로 설정된 경우, 메시지는 Braze 대시보드에서 Canvas의 타겟 오디언스로 구성된 전체 Segment에 전송됩니다.<br><br> `recipients` 배열에는 최대 50개의 오브젝트가 포함될 수 있으며, 각 오브젝트에는 하나의 `external_user_id` 문자열과 `canvas_entry_properties` 오브젝트가 포함됩니다. 이 호출에는 `external_user_id`, `user_alias` 또는 `email`이 필요합니다. 요청은 하나만 지정해야 합니다. <br><br> `email`이 식별자인 경우 수신자 오브젝트에 [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)을 포함해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
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
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## 응답 세부 정보 {#response-details}

메시지 전송 엔드포인트 응답에는 메시지의 `dispatch_id`가 포함되어 메시지 발송을 참조할 수 있습니다. `dispatch_id`는 메시지 발송의 ID(Braze 플랫폼에서 전송된 각 "전송"에 대한 고유 ID)입니다. 자세한 내용은 [디스패치 ID 동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)을 확인하세요.

### 성공 응답 예시 {#example-success-response}

`201` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. Canvas가 아카이브되거나 중지되거나 일시 중지된 경우, Canvas는 이 엔드포인트를 통해 전송되지 않습니다.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Canvas가 아카이브된 경우, 다음과 같은 `notice` 메시지가 표시됩니다: "The Canvas is archived. Unarchive the Canvas to ensure trigger requests will take effect." Canvas가 활성 상태가 아닌 경우, 다음과 같은 `notice` 메시지가 표시됩니다: "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect."

요청에 심각한 오류가 발생하면 오류 코드와 설명은 [오류 및 응답]({{site.baseurl}}/api/errors/#fatal-errors)을 참조하세요.

## 고려 사항 {#considerations}

API 트리거 전달을 사용하여 Canvas 메시지를 보내기 위한 API 호출 시 다음 사항을 고려하세요.

- **기존 사용자에게 전송**: `send_to_existing_only`가 `true`(기본값)로 설정된 경우, 메시지는 Braze의 기존 사용자에게만 전송됩니다.
- **새 사용자 생성**: `send_to_existing_only`가 `false`로 설정된 경우, `attributes` 오브젝트를 포함해야 합니다. 지정된 ID를 가진 사용자가 존재하지 않으면, Braze는 메시지를 전송하기 전에 해당 ID와 속성을 가진 사용자를 생성합니다.
- **사용자 별칭 제한**: `send_to_existing_only` 플래그는 사용자 별칭과 함께 사용할 수 없습니다. 별칭 전용 사용자에게 전송하려면, 사용자가 이미 Braze에 존재해야 합니다.
- **Segment 타겟팅**: `segment_id` 매개변수는 이 엔드포인트에서 지원되지 않습니다. Segment를 타겟팅하려면 Braze 대시보드의 Canvas 타겟 오디언스 설정에서 Segment를 구성하고 `broadcast: true`를 사용하거나, `audience` 매개변수를 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 필터와 함께 사용하세요.
- **결합된 타겟팅**: `recipients` 매개변수를 포함하고 대시보드에서 타겟 Segment를 구성하면, 메시지는 API 호출에서 지정된 고객 프로필 중 Segment의 필터와도 일치하는 사용자에게만 전송됩니다.
- **서버 간 호출**: 서버 간 호출을 하는 경우 방화벽 뒤에 있다면 적절한 API URL을 허용 목록에 추가해야 할 수 있습니다.

## Canvas용 속성 오브젝트 {#attributes-object-for-canvas}

메시징 오브젝트 `attributes`를 사용하여 `canvas/trigger/send` 엔드포인트를 통해 API 트리거 Canvas를 보내기 전에 사용자에 대한 속성 및 값을 추가, 생성 또는 업데이트하세요. 이 API 호출은 Canvas를 처리하고 전송하기 전에 사용자 속성 오브젝트를 처리합니다. 이렇게 하면 [경합 조건]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/)으로 인한 문제 발생 위험을 최소화할 수 있습니다. 그러나 기본적으로 구독 그룹은 이 방법으로 업데이트할 수 없습니다.

{% alert note %}
이 엔드포인트의 Campaign 버전을 찾고 계신가요? [API 트리거 전달을 사용하여 Campaign 메시지 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)를 확인하세요.
{% endalert %}

{% endapi %}