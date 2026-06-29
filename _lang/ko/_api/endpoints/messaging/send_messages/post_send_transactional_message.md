---
nav_title: "POST: API 트리거 전달을 사용하여 트랜잭션 이메일 보내기"
article_title: "POST: API 트리거 전달을 사용하여 트랜잭션 이메일 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 트리거 전달을 사용하여 트랜잭션 이메일 메시지 보내기 Braze 엔드포인트에 대해 자세히 설명합니다."

---

{% api %}
# API 트리거 전달을 사용하여 트랜잭션 이메일 보내기 {#send-transactional-emails-using-api-triggered-delivery}
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 사용자에게 즉각적인 일회성 트랜잭션 메시지를 보낼 수 있습니다.

이 엔드포인트는 Braze [트랜잭션 이메일 Campaign]({{site.baseurl}}/api/api_campaigns/transactional_campaigns/) 생성 및 해당 Campaign ID와 함께 사용됩니다.

{% alert important %}
트랜잭션 이메일은 현재 일부 Braze 패키지의 일부로 제공됩니다. 자세한 내용은 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

[트리거 Campaign 전송 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)와 마찬가지로, 이 Campaign 유형을 사용하면 메시지 콘텐츠를 Braze 대시보드 내에 보관하면서 API를 통해 메시지를 언제, 누구에게 보낼지 지정할 수 있습니다. 메시지를 보낼 오디언스 또는 Segment를 허용하는 트리거 Campaign 전송 엔드포인트와 달리, 이 Campaign 유형은 주문 확인 또는 비밀번호 재설정과 같은 1:1 알림 메시징을 위해 특별히 제작된 것이므로 이 엔드포인트에 대한 요청은 `external_user_id` 또는 `user_alias`로 단일 사용자를 지정해야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `transactional.send` 권한으로 API 키를 생성해야 합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## 경로 매개변수 {#path-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `campaign_id` | 필수 | 문자열 | Campaign의 ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `external_send_id` | 선택 사항 | 문자열 | Base64 호환 문자열입니다. 다음 정규식에 대해 유효성을 검사합니다.<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>이 선택적 필드를 사용하면 이 특정 전송에 대한 내부 식별자를 전달할 수 있으며, 이는 트랜잭션 HTTP 이벤트 포스트백에서 전송된 이벤트에 포함됩니다. 전달된 경우, 이 식별자는 중복 제거 키로도 사용되며, Braze는 이를 24시간 동안 저장합니다. <br><br>다른 요청에서 동일한 식별자를 전달하면 Braze에서 24시간 동안 새로운 전송 인스턴스가 생성되지 않습니다.|
| `trigger_properties` | 선택 사항 | 오브젝트 | [트리거 등록정보]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)를 참조하세요. 이 요청에서 사용자에게 적용되는 개인화 키-값 페어입니다. |
| `recipient` | 필수 | 오브젝트 | 이 메시지를 타겟팅하는 사용자입니다. `attributes` 및 단일 `external_user_id` 또는 `user_alias`를 포함할 수 있습니다.<br><br>Braze에 아직 존재하지 않는 외부 사용자 ID를 제공하는 경우, `attributes` 오브젝트에 필드를 전달하면 Braze에 이 고객 프로필이 생성되고 새로 생성된 사용자에게 이 메시지가 전송됩니다. <br><br>동일한 사용자에게 `attributes` 오브젝트에 서로 다른 데이터를 포함하여 여러 요청을 보내면 `first_name`, `last_name`, `email` 속성이 동기적으로 업데이트되고 메시지에 템플릿화됩니다. 커스텀 속성에는 이와 같은 보호 기능이 없으므로 이 API를 통해 사용자를 업데이트하고 서로 다른 커스텀 속성 값을 빠르게 연속해서 전달할 때는 주의해서 진행하세요.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## 예시 요청 {#example-request}

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## 응답 {#response}

트랜잭션 이메일 전송 엔드포인트는 이 메시지 전송의 인스턴스를 나타내는 메시지의 `dispatch_id`로 응답합니다. 이 식별자는 트랜잭션 HTTP 이벤트 포스트백의 이벤트와 함께 단일 사용자에게 전송된 개별 이메일의 상태를 추적하는 데 사용할 수 있습니다.

### 응답 예시 {#example-responses}

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## 문제 해결 {#troubleshooting}

엔드포인트는 경우에 따라 오류 코드와 사람이 읽을 수 있는 메시지를 반환할 수도 있으며, 대부분은 유효성 검사 오류입니다. 다음은 잘못된 요청을 할 때 발생할 수 있는 몇 가지 일반적인 오류입니다.

| 오류 | 문제 해결 |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | 제공된 Campaign ID는 트랜잭션 Campaign용이 아닙니다. |
| `The external reference has been queued.  Please retry to obtain send_id.` | 최근에 external_send_id가 생성되었습니다. 새 메시지를 전송하려는 경우 새 external_send_id를 시도하세요. |
| `Campaign does not exist` | 제공한 Campaign ID가 기존 Campaign과 일치하지 않습니다. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | 제공된 Campaign ID는 아카이브된 Campaign에 해당합니다. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | 제공된 Campaign ID는 일시 중지된 Campaign에 해당합니다. |
| `campaign_id must be a string of the campaign api identifier` | 제공한 Campaign ID가 올바른 형식이 아닙니다. |
| `Error authenticating credentials` | 제공된 API 키가 유효하지 않습니다. |
| `Invalid whitelisted IPs `| 요청을 전송하는 IP 주소가 IP 화이트리스트에 없습니다(사용 중인 경우). |
| `You do not have permission to access this resource` | 사용된 API 키에 이 작업을 수행할 수 있는 권한이 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

Braze의 대부분의 엔드포인트는 너무 많은 요청을 할 경우 429 응답 코드를 반환하는 사용량 제한 구현을 가지고 있습니다. 트랜잭션 전송 엔드포인트는 패키지에 따라 시간당 단위로 측정된 유료 시간 할당량을 가지고 있습니다(예: 시간당 50,000 단위). 이 엔드포인트에 대한 별도의 엔드포인트별 사용량 제한은 없습니다. 할당된 볼륨을 초과하여 전송할 수 있지만, SLA에 의해 보장되는 것은 할당된 볼륨만 해당됩니다. 그 할당량을 초과한 요청은 여전히 전송되지만 SLA에 의해 보장되지 않습니다. 이 엔드포인트에 대한 요청은 [전체 외부 API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 포함됩니다. 그 한도를 초과하면(예: 모든 엔드포인트에서 시간당 250,000 요청) Braze는 429를 반환하고 한도가 재설정될 때까지 요청을 제한합니다. 트랜잭션 볼륨 카운트는 매시간 재설정됩니다. 이 기능에 대한 추가 정보가 필요하면 Braze 고객지원팀에 문의하세요.

## 트랜잭션 HTTP 이벤트 포스트백 {#transactional-http-event-postback}

{% multi_lang_include channels/transactional_email/http_event_postback.md %}

{% endapi %}