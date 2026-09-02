---
nav_title: "GET: 날짜별 일일 활성 사용자 내보내기"
article_title: "GET: 날짜별 일일 활성 사용자 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 일일 활성 사용자 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 날짜별 일일 활성 사용자 내보내기 {#export-daily-active-users-by-date}
{% apimethod get %}
/KPI or 핵심 성과 지표(KPI)/일일 활성 사용자/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 각 날짜의 총 고유 활성 사용자 수에 대한 일일 시계열을 검색할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `kpi.dau.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `length` | 필수 | 정수 | 반환된 시리즈에 포함할 `ending_at` 이전 최대 일수. 1에서 100 사이여야 합니다(포함). |
| `ending_at` | 선택 사항 | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 시리즈가 종료되어야 하는 날짜. 기본값은 요청 시점입니다. |
| `app_id` | 선택 사항 | 문자열 | [API 키]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) 페이지에서 가져온 앱 API 식별자. 제외하면 워크스페이스의 모든 앱에 대한 결과가 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/dau/data_series?length=10&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답 {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "dau" : (int) the number of daily active users
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}

{% endapi %}