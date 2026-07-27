---
nav_title: "GET: 캠페인 목록 내보내기"
article_title: "GET: 캠페인 목록 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 캠페인 목록 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 캠페인 목록 내보내기 {#export-campaigns-list}
{% apimethod get %}
/campaigns/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인 목록을 내보낼 수 있으며, 각 캠페인에는 이름, Campaign API 식별자, API 캠페인 여부, 캠페인에 연결된 태그가 포함됩니다.

캠페인은 생성 시간순으로 정렬된 100개 단위의 그룹으로 반환됩니다(기본값은 가장 오래된 것부터 최신 순).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `campaigns.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `page` | 선택 사항 | 정수 | 반환할 캠페인 페이지이며, 기본값은 0입니다(최대 100개의 첫 번째 세트를 반환). |
| `include_archived` | 선택 사항 | 부울 | 아카이브된 캠페인을 포함할지 여부이며, 기본값은 false입니다. |
| `sort_direction` | 선택 사항 | 문자열 | - 생성 시간을 최신에서 오래된 순으로 정렬: `desc` 값을 전달합니다.<br> - 생성 시간을 오래된 것부터 최신 순으로 정렬: `asc` 값을 전달합니다. <br><br>`sort_direction`이 포함되지 않은 경우 기본 순서는 오래된 것부터 최신 순입니다. |
| `last_edit.time[gt]` | 선택 사항 | 시간 | 결과를 필터링하여 지정된 시간 이후에 편집된 캠페인만 반환합니다. 형식은 `yyyy-MM-DDTHH:mm:ss`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답 {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "campaigns" : [
        {
            "id" : (string) the Campaign API identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message
            "name" : (string) the campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
            "tags" : (array) the tag names associated with the campaign formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움이 필요하면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}

{% endapi %}