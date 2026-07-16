---
nav_title: "GET: 세그먼트 목록 내보내기"
article_title: "GET: 세그먼트 목록 내보내기"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 세그먼트 목록 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 세그먼트 목록 내보내기 {#export-segment-list}
{% apimethod get %}
/segments/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 세그먼트 목록을 내보낼 수 있으며, 각 세그먼트에는 이름, Segment API 식별자, 분석 추적 활성화 여부가 포함됩니다.

세그먼트는 생성 시간별로 정렬된 100개 그룹으로 반환됩니다(기본값은 가장 오래된 것부터 최신 순). 아카이브된 세그먼트는 포함되지 않습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `segments.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `page` | 선택 사항 | 정수 | 반환할 세그먼트 페이지이며, 기본값은 0입니다(최대 100개의 첫 번째 세트를 반환). |
| `sort_direction` | 선택 사항 | 문자열 | - 생성 시간을 최신에서 오래된 순으로 정렬: `desc` 값을 전달합니다.<br> - 생성 시간을 가장 오래된 것부터 최신 순으로 정렬: `asc` 값을 전달합니다. <br><br>`sort_direction`이 포함되지 않은 경우 기본 순서는 가장 오래된 것부터 최신 순입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답 {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}

{% endapi %}