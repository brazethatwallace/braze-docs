---
nav_title: 카탈로그 항목을 속성 배열에 매칭
article_title: 카탈로그 항목을 커스텀 속성 배열에 매칭
page_order: 2
page_type: reference
description: "카탈로그 셀렉션과 Liquid를 사용하여 위시리스트와 같은 커스텀 속성 배열에 이름이나 ID가 포함된 카탈로그 행을 표시합니다."
---

# 카탈로그 항목을 커스텀 속성 배열에 매칭 {#match-catalog-items-to-a-custom-attribute-array}

> 각 사용자가 프로필에 저장된 제품 이름 목록을 보유하고 있을 때, 카탈로그 셀렉션과 Liquid를 사용하여 해당 목록에 포함된 카탈로그 행만 표시할 수 있습니다. 예를 들어, 위시리스트 이메일에 활용할 수 있습니다.

## 이 예시에 대해 {#about-this-example}

Flash & Thread는 각 고객의 저장된 제품 이름을 문자열 배열 커스텀 속성(`saved_product_names`)에 저장합니다. 카탈로그에는 전체 제품 세부 정보(카테고리, 가격, 이미지 URL, 재고)가 포함되어 있습니다.

카탈로그 셀렉션은 정적 값이나 Liquid 값(카탈로그 행의 배열 필드 포함)을 기준으로 카탈로그 열을 필터링할 수 있습니다. 그러나 고객 프로필 배열에 저장된 값을 기준으로 카탈로그 행을 필터링하지는 않습니다. 사용자의 목록을 기반으로 개인화하려면, 셀렉션으로 광범위한 카탈로그 항목 세트를 반환한 다음 Liquid를 사용하여 프로필 배열과 일치하는 행만 유지합니다.

이 패턴은 다음과 같습니다:

1. 사용자의 배열 커스텀 속성을 Liquid 변수에 할당합니다.
2. 사전 필터링된 카탈로그 셀렉션에 대해 `catalog_selection_items`를 호출합니다(최대 50개 항목).
3. `items`를 반복하면서 `contains`를 사용하여 각 카탈로그 필드(예: `name` 또는 `id`)를 배열과 매칭합니다.

{% alert important %}
이 패턴은 셀렉션의 결과 세트(최대 50개 카탈로그 행)가 각 사용자의 저장된 항목을 포함할 수 있는 경우에만 작동합니다. 예를 들어, 소규모 카탈로그이거나 필터가 셀렉션을 충분히 좁혀 일반적인 목록을 커버할 수 있는 카탈로그에 적합합니다. 사용자의 저장된 항목이 반환된 50개 행 밖에 있으면, 루프에서 일치하는 항목을 찾지 못하고 해당 항목에 대해 메시지가 아무것도 렌더링하지 않습니다. 셀렉션이 사용자의 프로필 배열과 매칭할 수 없기 때문에 일반적인 경우에는 이를 해결할 필터가 없습니다.
{% endalert %}

## 고려 사항 {#considerations}

- 고객에게 발송하기 전에 스테이징 워크스페이스에서 Liquid와 카탈로그 데이터를 테스트하세요.
- 셀렉션은 최대 50개의 카탈로그 행을 반환하므로, 각 사용자의 저장된 항목이 해당 결과 세트 내에 포함되도록 필터(예: 재고 있음, 활성 카테고리, 가격대)를 추가하세요.
- 이 예시에서는 고객 프로필의 문자열 배열을 사용합니다.
- 객체 배열의 경우, 각 객체 내부의 속성정보(예: `product_id`)를 기준으로 매칭하고 `contains` 검사를 조정하거나 객체에 대해 `for` 루프를 사용하세요. [객체 배열]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)을 참조하세요.
- `contains` 동작은 속성 유형에 따라 달라집니다. 배열의 경우 `==` 대신 `contains`를 사용하세요. [조건 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)을 참조하세요.
- 제품 이름이 변경되거나 중복될 수 있는 경우 안정적인 식별자(예: 카탈로그 `id`)를 기준으로 매칭하세요.
- 이 문서의 Liquid 스니펫은 예시입니다. 채널(이메일 HTML, 푸시 등)에서 렌더링을 검증하세요.

## 설정 {#setup}

이 예시에서는 다음을 가정합니다:

| 에셋 | 세부 정보 |
| --- | --- |
| 커스텀 속성 | `saved_product_names` — 문자열 배열(예: `["linen_shirt", "trail_jacket", "canvas_tote"]`) |
| 카탈로그 | `apparel_products` — `id`, `category`, `name`, `price`, `inventory`, `image_url` 열 포함 |
| 셀렉션 | `apparel_products`의 `in_stock_apparel`, 결과 제한 50개, 관련 없는 행을 제외하는 필터 포함(예: `inventory`가 `0`보다 큰 경우) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="설정" }

### 1단계: 카탈로그 및 셀렉션 생성 {#step-1-create-the-catalog-and-selection}

1. `apparel_products`라는 이름의 카탈로그에 제품 행을 가져오거나 동기화합니다.
2. 50개 항목 제한까지 필요한 만큼 관련 행을 반환하는 셀렉션(예: `in_stock_apparel`)을 생성합니다.
3. 메시지에 포함하지 않을 행(재고 없음, 잘못된 카테고리 등)을 제거하는 셀렉션 필터를 추가합니다.

셀렉션 설정에 대해서는 [셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 참조하세요.

### 2단계: 메시지에 Liquid 추가 {#step-2-add-liquid-in-your-message}

프로필 배열을 할당하고, 셀렉션을 로드한 다음 `contains`로 루프를 실행합니다:

{% raw %}
```liquid
{% assign saved_product_names = custom_attribute.${saved_product_names} %}
{% catalog_selection_items apparel_products in_stock_apparel %}
{% for item in items %}
{% if saved_product_names contains item.name %}
Product: {{ item.name }}
Category: {{ item.category }}
Price: ${{ item.price }}
Image: {{ item.image_url }}
{% endif %}
{% endfor %}
```
{% endraw %}

배열이 표시 이름 대신 ID를 저장하는 경우 `item.name`을 `item.id`(또는 다른 열)로 바꾸세요. 채널에 맞게 필드 사이에 간격이나 HTML을 추가하세요. {% raw %}`${{ item.price }}`{% endraw %}에서 `$`는 Liquid 출력 앞에 표시되는 리터럴 통화 기호이며, Braze의 {% raw %}`${}`{% endraw %} 개인화 구문의 일부가 아닙니다.

이 Liquid를 자동으로 생성하려면 **개인화 추가** Modal(**카탈로그 항목** > **셀렉션 사용**)을 여세요. [카탈로그 사용]({{site.baseurl}}/user_guide/data/activation/catalogs/use)을 참조하세요.

### 3단계: 미리보기 및 테스트 {#step-3-preview-and-test}

다양한 `saved_product_names` 값을 가진 프로필로 테스트 메시지를 발송합니다. 일치하는 카탈로그 행만 표시되는지, 빈 배열에서는 제품 행이 생성되지 않는지 확인합니다.

## 관련 문서 {#related-articles}

- [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [카탈로그 사용]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
- [조건 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)
- [Liquid 사용 사례 라이브러리 — 배열 내 문자열 찾기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#misc-string-in-array)