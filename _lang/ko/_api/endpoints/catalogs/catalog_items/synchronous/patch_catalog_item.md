---
nav_title: "PATCH: 카탈로그 항목 편집"
article_title: "PATCH: 카탈로그 항목 편집"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 항목 편집 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 항목 편집 {#edit-catalog-item}
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그의 기존 항목을 편집할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `catalogs.update_item` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## 경로 매개변수 {#path-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `catalog_name` | 필수 | 문자열 | 카탈로그의 이름입니다. |
| `item_id` | 필수 | 문자열 | 카탈로그 항목의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="경로 매개변수" }

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `items` | 필수 | 배열 | 항목 오브젝트가 포함된 배열입니다. 항목 오브젝트에는 `id` 필드를 제외하고 카탈로그에 있는 필드가 포함되어야 합니다. 요청당 하나의 항목 오브젝트만 허용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
- `Location` 필드는 `geo` 데이터 유형을 사용하며, `[경도, 위도]` 형식의 배열을 기대합니다.
- `$add` 및 `$remove` 연산자는 배열 유형 필드에만 적용 가능하며 PATCH 엔드포인트에서만 지원됩니다.
{% endalert %}

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`의 세 가지가 있습니다.

### 성공 응답 예시 {#example-success-response}

`200` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

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
| `arbitrary-error` | 임의의 오류가 발생했습니다. 다시 시도하거나 [고객지원]({{site.baseurl}}/support_contact)에 문의하세요. |
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인하세요. |
| `filtered-set-field-too-long` | 필드 값이 항목의 글자 수 제한을 초과하는 필터링된 집합에서 사용되고 있습니다. |
| `id-in-body` | 카탈로그에 항목 ID가 이미 존재합니다. |
| `ids-too-large` | 각 항목 ID의 글자 수 제한은 250자입니다. |
| `invalid-ids` | 항목 ID 이름에 지원되는 문자는 문자, 숫자, 하이픈, 밑줄입니다. |
| `invalid-fields` | 요청의 필드가 카탈로그에 존재하는지 확인하세요. |
| `invalid-keys-in-value-object` | 항목 오브젝트 키에는 `.` 또는 `$`를 포함할 수 없습니다. |
| `item-not-found` | 해당 항목이 카탈로그에 있는지 확인하세요. |
| `item-array-invalid` | `items`는 오브젝트의 배열이어야 합니다. |
| `items-too-large` | 각 항목의 글자 수 제한은 5,000자입니다. |
| `request-includes-too-many-items` | 요청당 하나의 카탈로그 항목만 편집할 수 있습니다. |
| `too-deep-nesting-in-value-object` | 항목 오브젝트는 50개 이상의 중첩 레벨을 가질 수 없습니다. |
| `unable-to-coerce-value` | 항목 유형은 변환할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }

{% endapi %}