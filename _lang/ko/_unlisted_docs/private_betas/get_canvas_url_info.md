---
nav_title: "GET: Canvas 링크 별칭 목록"
layout: api_page
page_type: reference
hidden: true
permalink: /get_canvas_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "이 문서에서는 Canvas 링크 별칭 목록 엔드포인트에 대한 세부 정보를 설명합니다."
---
{% api %}
# Canvas 링크 별칭 목록 {#list-link-alias-for-canvas}
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> 이 엔드포인트를 사용하여 특정 이메일 캔버스 단계에 설정된 링크 별칭을 나열할 수 있습니다.

{% apiref postman %}  {% endapiref %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `canvas_step_id` | 필수 | 문자열 | [캔버스 단계 API 식별자]({{site.baseurl}}/api/identifier_types#canvas-identifier)를 참조하세요. |
| `message_variation_id ` | 필수 | 문자열 | 메시지 배리언트 API 식별자(해당 단계의 이메일 메시지 배리언트용). **Canvas 세부 정보** 페이지에서 **배리언트 분석**을 클릭하면 확인할 수 있습니다. |
| `includes_link_id` | 선택 사항 | 문자열 | 특정 링크 식별자(Braze에서 할당) 또는 `null`. 결과를 특정 `link_id`로 필터링하는 데 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 요청 예시 {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답 {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### 문제 해결 {#troubleshooting}

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나열되어 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `Missing/Invalid Canvas ID` | Canvas API ID는 API 식별자여야 합니다. [Canvas 목록 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases)를 사용하거나 대시보드에 로그인하여 확인할 수 있습니다. |
| `Missing/Invalid Message Variant ID` | 메시지 배리언트 API ID는 API 식별자여야 합니다. [Canvas 세부 정보 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)를 사용하거나 대시보드에 로그인하여 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}