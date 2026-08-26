---
nav_title: "카탈로그 선택 오브젝트"
article_title: API 카탈로그 선택 오브젝트
page_order: 12
page_type: reference
description: "이 참조 문서에서는 카탈로그 선택 오브젝트의 다양한 구성요소를 설명합니다."
tool: Catalogs

---

# 카탈로그 선택 오브젝트 {#catalog-selection-object}

> 카탈로그 선택을 생성할 때, 카탈로그에서 반환되는 항목에 대한 필터링, 정렬 및 제한 기준을 정의하기 위해 선택 오브젝트를 제공할 수 있습니다.

`selection` 오브젝트를 사용하면 필터를 기반으로 카탈로그에서 포함할 항목을 지정하고, 항목을 정렬하는 방법과 반환할 결과 수를 정의할 수 있습니다. API를 통해 카탈로그 선택을 생성할 때 이 오브젝트를 사용합니다.

## 객체 본문 {#object-body}

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## 객체 세부 정보 {#object-details}

| 키 | 필수 여부 | 데이터 유형 | 설명 |
| --- | -------- | --------- | ----------- |
| `name` | 필수 | 문자열 | 카탈로그 선택 항목의 이름입니다. |
| `description` | 선택 사항 | 문자열 | 카탈로그 선택 항목에 대한 설명입니다. |
| `external_id` | 선택 사항 | 문자열 | 선택 항목의 고유 식별자입니다. |
| `source` | 선택 사항 | 문자열 | 카탈로그 데이터의 소스입니다. Shopify 카탈로그의 경우 이 값을 `"Shopify"`로 설정합니다. 허용되는 값은 `"Shopify"` 및 `"Braze"`입니다. |
| `filters` | 필수 | 객체 배열 | 카탈로그 항목에 적용할 필터 객체의 배열입니다. 요청당 최대 10개의 필터를 지정할 수 있습니다. 빈 필터 배열이 제공되면 카탈로그의 모든 항목이 포함됩니다. |
| `results_limit` | 필수 | 정수 | 반환할 최대 결과 수입니다. 1에서 50 사이의 숫자여야 합니다. |
| `sort_field` | 선택 사항 | 문자열 | 결과를 정렬할 필드입니다. `sort_order`와 함께 사용해야 합니다. `sort_field`와 `sort_order`가 모두 없으면 결과는 랜덤 순서로 반환됩니다. |
| `sort_order` | 선택 사항 | 문자열 | 결과를 정렬할 순서입니다. 허용되는 값은 `"asc"`(오름차순) 또는 `"desc"`(내림차순)입니다. `sort_field`와 함께 사용해야 합니다. `sort_field`와 `sort_order`가 모두 없으면 결과는 랜덤 순서로 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="객체 세부 정보" }

### 필터 객체 {#filter-object}

`filters` 배열의 각 필터 객체에는 다음 표에 설명된 필드가 포함됩니다.

| 키 | 필수 여부 | 데이터 유형 | 설명 |
| --- | -------- | ------------------------------------------- | ----------- |
| `field` | 필수 | 문자열 | 필터링할 카탈로그 필드입니다. |
| `operator` | 필수 | 문자열 | 필터링에 사용할 비교 연산자입니다. 예를 들어 `"includes value"` 및 `"does not include value"`가 있습니다. |
| `value` | 필수 | 다양함(문자열, 숫자, 부울, 시간) | 비교할 값입니다. 기본 카탈로그 필드의 데이터 유형(예: 문자열, 숫자, 부울, 시간)과 일치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="필터 객체" }

{% alert note %}
API는 선택 요청당 최대 10개의 필터를 지원합니다. 필터는 배열에 나타나는 순서대로 적용됩니다.
{% endalert %}