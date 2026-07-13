---
nav_title: "POST: 예약된 API 트리거 캠페인 업데이트"
article_title: "POST: 예약된 API 트리거 캠페인 업데이트"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "이 문서에서는 예약된 API 트리거 캠페인 업데이트 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 예약된 API 트리거 캠페인 업데이트 {#update-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 대시보드에서 생성된 예약된 API 트리거 캠페인을 업데이트하고, 메시지 전송을 트리거할 동작을 결정할 수 있습니다.

메시지 자체에 Braze 템플릿으로 사용할 `trigger_properties`를 전달할 수 있습니다.

이 엔드포인트로 메시지를 보내려면 [API 트리거 Campaign]({{site.baseurl}}/api/api_campaigns)을 구축할 때 생성된 Campaign ID가 있어야 합니다.

모든 스케줄은 스케줄 생성 요청 또는 이전 스케줄 업데이트 요청에서 제공한 스케줄을 완전히 덮어씁니다. 예를 들어, 원래 스케줄을 `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}`로 설정했다가 나중에 `"schedule" : {"time" : "2015-02-20T14:14:47"}`로 업데이트하면, Braze는 사용자의 현지 시간이 아닌 UTC 기준 지정된 시간에 메시지를 보냅니다.

예약된 트리거가 전송 예정 시간에 가까워지거나 해당 시간에 업데이트되는 경우, Braze는 타겟팅된 사용자 전체, 일부 또는 아무에게도 마지막 변경 사항을 적용하지 못할 수 있으며, 최선을 다해 업데이트를 적용합니다. 원래 스케줄이 현지 시간을 사용했고 어떤 시간대에서든 원래 시간이 이미 지난 경우에는 업데이트가 적용되지 않습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `campaigns.trigger.schedule.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 필수 | 문자열 | [Campaign 식별자]({{site.baseurl}}/api/identifier_types) 참조 |
| `schedule_id` | 필수 | 문자열 | 업데이트할 `schedule_id` (스케줄 생성 응답에서 얻은 값) |
| `schedule` | 필수 | 오브젝트 | [스케줄 오브젝트]({{site.baseurl}}/api/objects_filters/schedule_object) 참조 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}