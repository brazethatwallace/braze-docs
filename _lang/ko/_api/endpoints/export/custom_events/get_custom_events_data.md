---
nav_title: "GET: 커스텀 이벤트 내보내기"
article_title: "GET: 커스텀 이벤트 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 커스텀 이벤트 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 커스텀 이벤트 내보내기 {#export-custom-events}
{% apimethod get %}
/events
{% endapimethod %}

> 이 엔드포인트를 사용하여 앱에 대해 기록된 커스텀 이벤트 목록을 내보낼 수 있습니다. 이벤트는 알파벳순으로 정렬된 50개 그룹으로 반환됩니다.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `events.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='events' %}

## 쿼리 매개변수 {#query-parameters}

이 엔드포인트를 호출할 때마다 50개의 이벤트가 반환됩니다. 이벤트가 50개 이상인 경우 다음 예제 응답에 표시된 것처럼 `Link` 헤더를 사용하여 다음 페이지에서 데이터를 검색하세요.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `cursor` | 선택 사항 | 문자열 | 커스텀 이벤트의 페이지 매김을 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="쿼리 매개변수" }

## 요청 예시 {#example-requests}

### 커서 없음 {#without-cursor}

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### 커서 포함 {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답 {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### 심각한 오류 응답 코드 {#fatal-export}

요청에 심각한 오류가 발생할 경우 반환되는 상태 코드 및 관련 오류 메시지는 [심각한 오류]({{site.baseurl}}/api/errors#fatal-errors)를 참조하세요.

{% alert tip %}
CSV 및 API 내보내기에 대한 도움이 필요하면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 방문하세요.
{% endalert %}

{% endapi %}