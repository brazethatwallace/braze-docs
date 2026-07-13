---
nav_title: "PUT: 여러 카탈로그 항목 교체"
article_title: "PUT: 여러 카탈로그 항목 교체"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "이 문서에서는 여러 카탈로그 항목 교체 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 항목 교체 {#replace-catalog-items}
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그의 여러 항목을 교체할 수 있습니다.

카탈로그 항목이 존재하지 않는 경우 이 엔드포인트가 카탈로그에 항목을 생성합니다. 각 요청은 최대 50개의 카탈로그 항목을 지원할 수 있습니다. 이 엔드포인트는 비동기식입니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `catalogs.replace_items` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## 경로 매개변수 {#path-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `catalog_name` | 필수 | 문자열 | 카탈로그의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="경로 매개변수" }

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `items` | 필수 | 배열 | 항목 오브젝트가 포함된 배열입니다. 각 오브젝트에는 ID가 있어야 합니다. 항목 오브젝트에는 카탈로그에 존재하는 필드가 포함되어야 합니다. 요청당 최대 50개의 항목 오브젝트가 허용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

{% alert note %}
`Location` 필드는 `geo` 데이터 유형을 사용하며, `[longitude, latitude]` 형식의 배열을 기대합니다.
{% endalert %}

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `202`, `400`, `404`의 세 가지가 있습니다.

{% alert note %}
회사가 카탈로그 스토리지 한도에 도달한 경우에도 시스템이 `400` 응답을 반환할 수 있습니다. 카탈로그 무료 버전은 100&nbsp;MB로 제한됩니다. 스토리지 티어 및 업그레이드 방법에 대한 자세한 내용은 [데이터 스토리지 제한]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations)을 참조하세요.
{% endalert %}

### 성공 응답 예시 {#example-success-response}

`202` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답 예시 {#example-error-response}

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결](#troubleshooting)을 참조하세요.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## 문제 해결 {#troubleshooting}

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인합니다. |
| `company-size-limit-already-reached` | 카탈로그 스토리지 크기 한도에 도달했습니다. 스토리지 티어에 대한 자세한 내용은 [데이터 스토리지 제한]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations)을 참조하세요. |
| `company-size-limit-surge` | 요청이 회사의 남은 카탈로그 스토리지를 초과합니다. 더 작은 업데이트로 다시 시도하세요. 스토리지 티어에 대한 자세한 내용은 [데이터 스토리지 제한]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations)을 참조하세요. |
| `ids-not-string` | 각 항목 ID가 문자열인지 확인합니다. |
| `ids-not-unique` | 각 항목 ID가 고유한지 확인합니다. |
| `ids-too-large` | 각 항목 ID의 글자 수 제한은 250자입니다. |
| `item-array-invalid` | `items`는 오브젝트의 배열이어야 합니다. |
| `items-missing-ids` | 일부 항목에 항목 ID가 없습니다. 각 항목에 ID가 있는지 확인합니다. |
| `items-too-large` | 항목 값은 5,000자를 초과할 수 없습니다. |
| `invalid-ids` | 항목 ID 이름에 지원되는 문자는 문자, 숫자, 하이픈, 밑줄입니다. |
| `invalid-fields` | API 요청에서 전송하려는 모든 필드가 카탈로그에 이미 존재하는지 확인합니다. 이는 오류에 언급된 ID 필드와는 관련이 없습니다. |
| `invalid-keys-in-value-object` | 항목 오브젝트 키에는 `.` 또는 `$`를 포함할 수 없습니다. |
| `too-deep-nesting-in-value-object` | 항목 오브젝트는 50개 이상의 중첩 레벨을 가질 수 없습니다. |
| `request-includes-too-many-items` | 요청에 항목이 너무 많습니다. 요청당 항목 한도는 50개입니다. |
| `unable-to-coerce-value` | 항목 유형은 변환할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }

{% endapi %}