---
nav_title: "POST: 예약된 API 트리거 Canvases 업데이트"
article_title: "POST: 예약된 API 트리거 Canvases 업데이트"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 예약된 API 트리거 Canvases 업데이트 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 예약된 API 트리거 Canvases 업데이트 {#update-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 대시보드에서 생성된 예약된 API 트리거 Canvases를 업데이트할 수 있습니다.

이를 통해 메시지 전송을 트리거하는 동작을 결정할 수 있습니다. 메시지 자체에 Braze가 템플릿으로 사용하는 `trigger_properties`를 전달할 수 있습니다.

이 엔드포인트로 메시지를 보내려면 [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)를 구축할 때 생성된 Canvas ID가 있어야 합니다.

모든 스케줄은 스케줄 생성 요청 또는 이전 스케줄 업데이트 요청에서 제공한 스케줄을 완전히 덮어씁니다.
  - 예를 들어, 원래 `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}`을 제공한 다음 업데이트에서 `"schedule" : {"time" : "2015-02-20T14:14:47"}`을 제공하면, Braze는 사용자의 현지 시간이 아닌 제공된 시간(UTC)에 메시지를 보냅니다.
  - 전송 예정 시간에 가까워지거나 전송 예정 시간 중에 업데이트된 예약 트리거는 최선의 노력으로 업데이트되므로, Braze는 타겟팅된 사용자 전체, 일부 또는 아무에게도 마지막 순간 변경 사항을 적용할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `canvas.trigger.schedule.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | 필수 | 문자열 | [Canvas 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하세요. |
| `schedule_id` | 선택 사항 | 문자열 | 업데이트할 `schedule_id`(스케줄 생성 응답에서 얻은 값)입니다. |
| `schedule` | 필수 | 오브젝트 | [스케줄 오브젝트]({{site.baseurl}}/api/objects_filters/schedule_object/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}