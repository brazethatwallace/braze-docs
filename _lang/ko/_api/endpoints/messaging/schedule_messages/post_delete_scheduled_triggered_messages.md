---
nav_title: "POST: 예약된 API 트리거 캠페인 삭제"
article_title: "POST: 예약된 API 트리거 캠페인 삭제"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 예약된 API 트리거 캠페인 삭제 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 예약된 API 트리거 캠페인 삭제 {#delete-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> 이 엔드포인트를 사용하여 이전에 API 트리거를 통해 예약한 캠페인 메시지가 전송되기 전에 취소할 수 있습니다.

예약된 메시지 또는 트리거가 전송 예정 시간에 가까워지거나 전송 중에 삭제되는 경우, Braze는 최선을 다해 업데이트하므로 타겟팅된 사용자 전체, 일부 또는 아무에게도 마지막 순간의 삭제가 적용되지 않을 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `campaigns.trigger.schedule.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 필수 | 문자열 | [캠페인 식별자]({{site.baseurl}}/api/identifier_types)를 참조하세요. |
| `schedule_id` | 필수 | 문자열 | 삭제할 `schedule_id`(스케줄 생성 응답에서 얻은 값)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }


## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}