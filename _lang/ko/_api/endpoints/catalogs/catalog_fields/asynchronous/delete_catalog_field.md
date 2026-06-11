---
nav_title: "DELETE: 카탈로그 필드 삭제"
article_title: "DELETE: 카탈로그 필드 삭제"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 필드 삭제 Braze 엔드포인트에 대해 자세히 설명합니다."

---
{% api %}
# 카탈로그 필드 삭제 {#delete-catalog-field}
{% apimethod delete %}
/catalogs/{catalog_name}/fields/{field_name}
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그 필드를 삭제할 수 있습니다.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `catalogs.delete_fields` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## 경로 매개변수 {#path-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| -------------- | -------- | --------- | -------------------------- |
| `catalog_name` | 필수 | 문자열 | 카탈로그의 이름입니다. |
| `field_name` | 필수 | 문자열 | 카탈로그 필드의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="경로 매개변수" }

## 요청 예시 {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/fields/ratings' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `202`와 `404` 두 가지입니다.

### 성공 응답 예시 {#example-success-response}

`202` 상태 코드는 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답 예시 {#example-error-response}

`404` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결](#troubleshooting)을 참조하세요.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## 문제 해결 {#troubleshooting}

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| ------------------------------- | ---------------------------------------------------------------- |
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인하세요. |
| `field-referenced-by-selection` | 카탈로그 필드가 현재 선택 항목에서 사용 중인지 확인하세요. |
| `field-is-inventory` | 카탈로그 필드가 인벤토리 필드로 사용되고 있는지 확인하세요. |
| `invalid-field-name` | 카탈로그 필드 이름이 유효한지 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }

{% endapi %}