---
nav_title: "POST: 전송 ID 생성"
article_title: "POST: 전송 ID 생성"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 전송 ID 생성 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 전송 ID 생성 {#create-send-ids}
{% apimethod post %}
/sends/id/create
{% endapimethod %}

> 이 엔드포인트를 사용하면 각 전송에 대한 Campaign을 만들지 않고도 프로그래밍 방식으로 메시지를 전송하고 메시지 성과를 추적하는 데 사용할 수 있는 전송 ID를 생성할 수 있습니다.

전송 식별자를 사용하여 메시지를 추적하고 전송하는 것은 프로그래밍 방식으로 콘텐츠를 생성하고 전송하려는 경우에 유용합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `sends.id.create` 권한으로 API 키를 생성해야 합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 필수 | 문자열 | [Campaign 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하세요. |
| `send_id` | 선택 사항 | 문자열 | [전송 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## 응답 {#response}

### 성공 응답 예시 {#example-success-response}

```json
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}