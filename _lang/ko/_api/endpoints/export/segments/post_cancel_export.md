---
nav_title: "POST: Segment별 내보내기 취소"
article_title: "POST: Segment별 내보내기 취소"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 Segment별 내보내기 취소 Braze 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# Segment별 내보내기 취소 {#cancel-exports-by-segment}
{% apimethod post %}
/export/segment/cancel
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 Segment ID로 진행 중인 모든 내보내기를 취소할 수 있습니다.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `segments.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `segment_id` | 필수 | 문자열 | 진행 중인 내보내기를 취소할 `segment_id`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}