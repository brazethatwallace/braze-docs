---
nav_title: "GET: Canvas 목록 내보내기"
article_title: "GET: Canvas 목록 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 Canvas 목록 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# Canvas 목록 내보내기 {#export-canvas-list}
{% apimethod get %}
/canvas/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 이름, Canvas API 식별자 및 관련 태그를 포함한 Canvases 목록을 내보낼 수 있습니다.

Canvases는 생성 시간별로 정렬된 100개 그룹으로 반환됩니다(기본적으로 가장 오래된 것부터 최신 순).

아카이브된 Canvases는 `include_archived` 필드가 지정되지 않는 한 API 응답에 포함되지 않습니다. 그러나 중지되었지만 아카이브되지 않은 Canvases는 기본적으로 반환됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `canvas.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `page` | 선택 사항 | 정수 | 반환할 Canvases 페이지이며, 기본값은 `0`입니다(최대 100개의 첫 번째 세트를 반환). |
| `include_archived` | 선택 사항 | 부울 | 아카이브된 Canvases를 포함할지 여부이며, 기본값은 `false`입니다. |
| `sort_direction` | 선택 사항 | 문자열 | - 생성 시간을 최신에서 오래된 순으로 정렬: `desc` 값을 전달합니다.<br> - 생성 시간을 가장 오래된 것부터 최신 순으로 정렬: `asc` 값을 전달합니다. <br><br>`sort_direction`이 포함되지 않은 경우 기본 순서는 가장 오래된 것부터 최신 순입니다. |
| `last_edit.time[gt]` | 선택 사항 | 시간 | 결과를 필터링하여 제공된 시간 이후에 편집된 Canvases만 반환합니다. 형식은 `yyyy-MM-DDTHH:mm:ss`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답 {#response}

```json
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움이 필요하면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}

{% endapi %}