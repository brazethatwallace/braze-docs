---
nav_title: "GET: 세그먼트 세부 정보 내보내기"
article_title: "GET: 세그먼트 세부 정보 내보내기"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 문서에서는 세그먼트 세부 정보 내보내기 Braze 엔드포인트에 대해 설명합니다."

---
{% api %}
# 세그먼트 세부 정보 내보내기 {#export-segment-details}
{% apimethod get %}
/segments/details
{% endapimethod %}

> 이 엔드포인트를 사용하여 `segment_id`로 식별할 수 있는 세그먼트에 대한 관련 정보를 조회합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `segments.details` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | 필수 | 문자열 | [세그먼트 API 식별자]({{site.baseurl}}/api/identifier_types)를 참조하세요.<br><br> 지정된 세그먼트의 `segment_id`는 Braze 계정 내 [API 키]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) 페이지에서 찾을 수 있으며, [세그먼트 목록 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/segments/get_segment)를 사용할 수도 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답 {#response}

```json
{
      "message": (string) returns 'success' when the request completes without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description,
      "tags" : (array) the tag names associated with the segment formatted as strings,
      "teams" : (array) the names of the Teams associated with the campaign
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}

{% endapi %}