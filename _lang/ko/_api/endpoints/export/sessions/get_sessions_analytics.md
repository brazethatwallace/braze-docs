---
nav_title: "GET: 시간별로 앱 세션 내보내기"
article_title: "GET: 시간별 앱 세션 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 시간별 앱 세션 분석 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 시간별로 앱 세션 내보내기 {#export-app-session-by-time}
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 기간 동안 앱의 세션 수 시리즈를 검색할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `sessions.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `length` | 필수 | 정수 | `ending_at` 이전에 반환된 시리즈에 포함할 최대 단위(일 또는 시간) 수입니다. 1에서 100 사이여야 합니다(포함). |
| `unit` | 선택 사항 | 문자열 | 데이터 포인트 간의 시간 단위입니다. `day` 또는 `hour`일 수 있으며 기본값은 `day`입니다. |
| `ending_at` | 선택 사항 | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 시리즈가 종료되어야 하는 날짜입니다. 요청 시점으로 기본 설정됩니다. |
| `app_id` | 선택 사항 | 문자열 | [API 키]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) 페이지에서 가져온 앱 API 식별자로, 특정 앱으로 분석을 제한할 수 있습니다. |
| `segment_id` | 선택 사항 | 문자열 | [Segment API 식별자]({{site.baseurl}}/api/identifier_types)를 참조하세요. 세션을 반환할 분석 활성화 Segment를 나타내는 Segment ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답 {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}

{% endapi %}