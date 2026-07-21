---
nav_title: "POST: API 트리거 전송을 사용하여 캠페인 보내기"
article_title: "POST: API 트리거 전송을 사용하여 캠페인 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 트리거 전송을 사용하여 캠페인을 보내는 Braze 엔드포인트에 대해 자세히 설명합니다."

---
{% api %}
# API 트리거 전송을 사용하여 Campaign 메시지 보내기 {#send-campaign-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> 이 엔드포인트를 사용하면 API 트리거 전송을 통해 지정된 사용자에게 즉각적인 일회성 메시지를 보낼 수 있습니다.

API 트리거 전송을 사용하면 메시지 콘텐츠를 Braze 대시보드 내에 보관하면서 API를 사용하여 메시지 전송 시기와 수신자를 지정할 수 있습니다.

Segment를 타겟팅하는 경우, 요청 기록이 [개발자 콘솔](https://dashboard.braze.com/app_settings/developer_console/activitylog/)에 저장됩니다. 이 엔드포인트로 메시지를 보내려면 [API 트리거 Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)을 구축할 때 생성한 [Campaign ID]({{site.baseurl}}/api/identifier_types)가 있어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `campaigns.trigger.send` 권한이 있는 API 키를 생성해야 합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 필수 | 문자열 | [Campaign 식별자]({{site.baseurl}}/api/identifier_types)를 참조하세요. |
| `send_id` | 선택 사항 | 문자열 | [전송 식별자]({{site.baseurl}}/api/identifier_types)를 참조하세요. |
| `trigger_properties` | 선택 사항 | 오브젝트 | [트리거 속성]({{site.baseurl}}/api/objects_filters/trigger_properties_object)을 참조하세요. 개인화 키-값 페어는 이 요청의 모든 사용자에게 적용됩니다. |
| `broadcast` | 선택 사항 | 부울 | Braze 대시보드에서 Campaign의 타겟 오디언스로 구성된 전체 Segment에 메시지를 전송할 때 `broadcast`를 true로 설정해야 합니다. 이 매개변수는 기본적으로 false로 설정됩니다(2017년 8월 31일 기준). <br><br> `broadcast`가 true로 설정되면 `recipients` 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 오디언스에게 메시지를 보낼 수 있으므로 `broadcast: true`를 설정할 때는 주의하세요. |
| `audience` | 선택 사항 | 연결된 오디언스 오브젝트 | [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience)를 참조하세요. `audience`를 포함하면, 커스텀 속성 및 구독 상태와 같은 정의된 필터와 일치하는 사용자에게만 메시지가 전송됩니다. |
| `recipients` | 선택 사항 | 배열 | [수신자 오브젝트]({{site.baseurl}}/api/objects_filters/recipient_object)를 참조하세요.<br><br>`send_to_existing_only`가 `false`인 경우 `attributes` 오브젝트를 포함해야 합니다.<br><br>중첩된 `attributes` 오브젝트에 `subscription_groups`를 포함하여 사용자의 구독 그룹 상태를 업데이트할 수 있습니다. 자세한 내용은 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object)를 참조하세요.<br><br>`recipients`가 제공되지 않고 `broadcast`가 true로 설정된 경우, Braze 대시보드에서 Campaign의 타겟 오디언스로 구성된 전체 Segment에 메시지가 전송됩니다.<br><br>`email`이 식별자인 경우 수신자 오브젝트에 [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)을 포함해야 합니다. |
| `attachments` | 선택 사항 | 배열 | `broadcast`가 true로 설정되어 있으면 `attachments` 목록을 포함할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

### 수신자 확인 동작 {#recipient-resolution-behavior}

이 섹션에서는 Braze가 전송할 고객 프로필을 선택하는 방법과 프로필이 선택되지 않을 때 어떤 일이 발생하는지 설명합니다.

사용자의 구독 그룹 상태는 `attributes` 오브젝트 내에 `subscription_groups` 매개변수를 포함하여 업데이트할 수 있습니다. 자세한 내용은 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)를 참조하세요.

#### 수신자 제한 및 프로필 생성 {#recipient-limits-and-profile-creation}

이 엔드포인트의 수신자 제한 및 프로필 생성 작동 방식에 대해 자세히 알아보세요.

- `recipients` 배열에는 최대 50개의 오브젝트가 포함될 수 있으며, 각 오브젝트에는 단일 `external_user_id` 문자열과 `trigger_properties` 오브젝트가 포함됩니다.
- `send_to_existing_only`가 `true`(기본값)일 때, Braze는 기존 사용자에게만 메시지를 전송합니다.
- `send_to_existing_only`가 `false`이고 `attributes` 오브젝트가 제공되면, Braze는 사용자가 존재하지 않을 경우 새 사용자를 생성합니다.
- **신규 프로필에는 `send_to_existing_only: false`와 함께 `attributes`가 필요합니다.** Braze는 동일한 수신자 내의 `attributes` 오브젝트에서 전송 전 생성 또는 업데이트를 실행합니다. `send_to_existing_only`를 `false`로 설정하되 `attributes`를 생략하거나 빈 오브젝트를 전송하면, Braze는 동일한 방식으로 프로필 데이터를 채우지 않으므로 이 패턴이 의도하는 "사용자 생성 또는 업데이트 후 전송" 동작을 얻을 수 없습니다.
- **이메일 및 SMS 주소 지정.** 아직 Braze에 없는 사용자에게 대부분의 이메일 또는 SMS API 트리거 전송을 하려면, `attributes` 내에 필요한 전달 필드(예: `email` 또는 워크스페이스에서 SMS에 사용하는 전화 속성)를 포함하세요. 동일한 호출에서 옵트인 상태를 변경해야 하는 경우 구독 그룹 멤버십 또는 구독 상태도 설정할 수 있습니다.
- **Campaign 적격성.** 프로필이 존재하거나 업데이트된 후에도 해당 사용자는 Campaign의 대시보드 타겟 오디언스 및 채널 전송 규칙(예: 이메일 옵트인)과 일치해야 합니다. 그렇지 않으면 Braze는 메시지를 전송하지 않습니다.
- `send_to_existing_only`를 `false`로 설정하는 것은 사용자 별칭에 대해 지원되지 않습니다. 새 별칭 전용 사용자는 이 엔드포인트를 통해 생성할 수 없습니다. 별칭 전용 사용자에게 전송하려면, 해당 사용자가 이미 Braze에 존재해야 합니다.

#### 이메일 식별자 및 우선순위 동점 {#email-identifier-and-prioritization-ties}

이메일로 수신자를 식별할 때, Braze는 `prioritization`을 사용합니다. Braze는 `prioritization`이 하나의 프로필을 반환할 때만 전송합니다.

- `email`을 식별자로 사용하는 경우, Braze는 `prioritization`을 사용하여 수신자를 확인합니다.
- `prioritization`이 동점을 반환하면, Braze는 전송하지 않습니다.
- 동점이 해소되고 `prioritization`이 하나의 프로필을 반환하면 Braze가 전송합니다. 예를 들어, 프로필 업데이트로 인해 한 사용자의 정렬 필드가 변경되면, `prioritization`이 프로필을 고유하게 식별할 수 있게 된 후 Braze가 전송합니다([재시도 동작 및 `send_to_existing_only`](#retry-behavior-and-send_to_existing_only) 참조).
- `prioritization`이 프로필을 반환하지 않는 경우에도 Braze는 전송하지 않습니다.

#### 재시도 동작 및 send_to_existing_only {#retry-behavior-and-send_to_existing_only}

`prioritization`이 정확히 하나의 프로필을 반환하지 않을 때 어떤 일이 발생하는지 알아보세요.

- `prioritization`이 정확히 하나의 고객 프로필을 반환하지 않으면, Braze는 최대 40회까지 확인을 재시도합니다. 이 재시도 동작은 예상된 것입니다.
- `send_to_existing_only` 설정은 `prioritization` 동점 동작을 변경하지 않습니다. 이 설정이 `true`이든 `false`이든 동일한 동점 및 재시도 동작이 적용됩니다.

`external_user_id` 또는 `user_alias`로 식별된 수신자에 대해 이메일 전용 Campaign을 트리거했는데, 해당 고객 프로필에 호출 시점에 이메일 주소가 없는 경우, Braze는 약 2시간 동안 전송을 재시도합니다. 이는 사용자를 생성하고 이메일 주소를 연속적으로 설정하는 일반적인 패턴을 처리합니다. 지연 없이 전송하려면, `recipients[].attributes` 내에 `email` 속성을 포함하여 트리거와 동일한 호출에서 주소를 설정하세요.

{% alert note %}
이 엔드포인트에서는 `segment_id` 매개변수가 지원되지 않습니다. Segment를 타겟팅하려면, Braze 대시보드에서 Campaign의 타겟 오디언스 설정에서 Segment를 구성하고 `"broadcast": true`를 사용하거나, [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience) 필터와 함께 `audience` 매개변수를 사용하세요.
{% endalert %}

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
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
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## 응답 세부 정보 {#response-details}

메시지 전송 엔드포인트 응답에는 메시지 발송을 참조할 수 있도록 메시지의 `dispatch_id`가 포함됩니다. `dispatch_id`는 메시지 발송의 ID로, Braze에서 전송하는 각 전송에 대한 고유 ID입니다. 이 엔드포인트를 사용하면 전체 배치 사용자 집합에 대해 단일 `dispatch_id`를 받게 됩니다. `dispatch_id`에 대한 자세한 내용은 [디스패치 ID 동작]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) 설명서를 참조하세요.

요청에 심각한 오류가 발생하면 오류 코드와 설명은 [오류 및 응답]({{site.baseurl}}/api/errors#fatal-errors)을 참조하세요.

## Campaign용 속성 오브젝트 {#attributes-object-for-campaigns}

Braze에는 `attributes`라는 메시징 오브젝트가 있어, API 트리거 Campaign을 전송하기 전에 사용자의 속성과 값을 추가, 생성 또는 업데이트할 수 있습니다. `campaign/trigger/send` 엔드포인트를 사용하면 이 API 호출이 사용자 속성 오브젝트를 먼저 처리한 후 Campaign을 처리하고 전송합니다. 이를 통해 [경합 조건]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)으로 인해 발생할 수 있는 문제의 위험을 최소화할 수 있습니다.

{% alert tip %}
이 엔드포인트의 Canvas 버전을 찾고 계신가요? [API 트리거 전송을 사용하여 Canvas 메시지 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)를 확인하세요.
{% endalert %}

### JSON 본문에 Liquid를 직접 넣으면 왜 렌더링되지 않나요? {#why-doesnt-liquid-render-when-i-put-it-directly-in-my-json-body}

요청 본문이 유효한 JSON이면, Braze는 서버에서 페이로드 내의 모든 Liquid를 평가합니다. Liquid를 원시 문자열로 포함하는 경우, 본문이 유효한 JSON으로 유지되도록 해당 문자열을 따옴표로 감싸고 이스케이프 처리하세요. 예를 들어, 문자열 내의 큰따옴표를 이스케이프 처리합니다. 본문이 JSON 파싱에 실패하면, Braze는 Liquid를 평가하기 전에 `400`을 반환합니다. 지원되는 경우, 페이로드에 Liquid를 직접 포함하는 대신 [`trigger_properties`]({{site.baseurl}}/api/objects_filters/trigger_properties_object)를 통해 동적 값을 전달하세요.

{% endapi %}