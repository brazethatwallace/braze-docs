---
nav_title: 현지화된 카탈로그 콘텐츠
article_title: Braze 카탈로그로 현지화된 콘텐츠 관리하기
page_order: 3
page_type: reference
description: "현지화된 제품 문구, 가격, 이미지 URL을 Braze 카탈로그에 저장하고 발송 시 올바른 언어로 해석합니다."
---

# Braze 카탈로그로 현지화된 콘텐츠 관리하기 {#manage-localized-content-with-braze-catalogs}

> 현지화된 문자열과 URL을 카탈로그에 저장하면 로케일별 배리언트를 별도로 만들지 않고도 단일 Campaign 또는 Canvas에서 각 사용자에게 해당 언어의 문구를 전달할 수 있습니다.

## 이 예시에 대하여 {#about-this-example}

PantsLabyrinth는 가상의 의류 소매업체로, 북미와 유럽 전역에 제품을 판매하고 있습니다. 제품명, 가격, 히어로 이미지는 언어별로 다르지만, 마케팅 팀은 발송 시 개인화되는 하나의 이메일 또는 푸시 템플릿을 원합니다.

이 예시에서는 SDK가 기기 로케일에서 수집하는 사용자의 {% raw %}`${language}`{% endraw %} [표준 속성]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)을 읽는 세 가지 카탈로그 패턴을 다룹니다.

- JSON 오브젝트 필드: 항목당 하나의 행에 모든 로케일 포함
- 언어별 플랫 컬럼: `header_en`, `header_fr` 등
- 언어별 별도 카탈로그: `pantslabyrinth-promo-en`과 같은 동적 카탈로그 이름

현지화된 콘텐츠가 구조화된 데이터(제품, 프로모션, 이미지 URL)일 때 카탈로그를 사용하세요. 이메일이나 푸시에서 자유 형식 메시지 문구를 사용하려면, 채널에서 지원하는 경우 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 사용하는 것이 좋습니다. 현지화 패턴을 더 넓게 비교하려면 [번역 관리]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management)를 참조하세요.

## 고려 사항 {#considerations}

- 예시는 설명을 위한 것입니다. 카탈로그 키나 접미사를 지정하기 전에 사용자 기반에서 {% raw %}`${language}`{% endraw %}의 대소문자와 형식을 확인하세요.
- 방법 1과 2의 경우, {% raw %}`${language}`{% endraw %}가 비어 있거나 카탈로그 키 또는 필드와 일치하지 않으면 현지화된 출력이 비어 있을 수 있습니다. 각 필드를 독립적으로 확인하고 기본값(예: 영어)으로 대체하세요.
- 방법 3의 경우, 카탈로그 이름을 작성하기 전에 지원되는 언어 코드를 허용 목록에 추가하세요. 카탈로그가 없으면 메시지가 중단됩니다.
- 카탈로그의 [JSON 오브젝트]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types)는 API 또는 [카탈로그용 클라우드 데이터 수집(CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)을 통해 생성하거나 업데이트할 수 있으며, CSV 업로드로는 불가합니다.
- 방법 2는 CSV 유지보수를 지원하지만 언어가 늘어남에 따라 컬럼이 증가합니다. CSV 파일은 최대 [1,000개의 컬럼]({{site.baseurl}}/user_guide/data/activation/catalogs/create#step-1-review-your-csv-file)을 지원합니다.
- 방법 3에서는 `catalog_items` 태그에 도달하는 모든 언어 코드에 대해 카탈로그가 필요합니다. 카탈로그가 존재하지 않으면 Braze가 메시지를 중단합니다. 기존 카탈로그에서 항목 ID가 없으면 빈 항목 배열이 반환됩니다.
- 카탈로그 Liquid 태그는 [재귀적으로]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid) 사용할 수 없습니다.
- [카탈로그 셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)은 최대 10개의 필터를 지원하며 최대 50개의 항목을 반환합니다. 카탈로그 스키마에 대해 필터를 검증하세요.
- 대규모 다국어 제품 피드를 유지하는 경우 [카탈로그 스토리지 티어]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers)를 검토하세요.

## 설정 {#setup}

### 1단계: 카탈로그 구조 선택하기 {#step-1-choose-a-catalog-structure}

다음 표를 참고하여 카탈로그 구조를 선택하세요.

| 방법 | 적합한 경우 | 단점 |
| --- | --- | --- |
| JSON 오브젝트 필드 | 중간 규모 카탈로그; 항목당 하나의 행; API 또는 CDI를 통한 업데이트 | 언어를 추가하면 API를 통해 모든 항목을 업데이트해야 함; JSON 필드에는 CSV 사용 불가 |
| 언어별 플랫 필드 | 언어와 필드 수가 적음; 비엔지니어링 팀이 CSV 사용 | 새 언어를 추가할 때마다 컬럼 증가; 필드 명명을 일관되게 유지해야 함 |
| 언어별 카탈로그 | 로케일별 대규모 피드 또는 별도의 로케일 담당자; 언어별 CSV | 허용 목록에 있는 모든 언어 코드에 카탈로그 필요; 카탈로그가 없으면 발송 중단 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="카탈로그 구조 선택하기" }

### 2단계: 카탈로그 및 항목 생성하기 {#step-2-create-the-catalog-and-items}

1. **데이터 설정** > **카탈로그**로 이동하여 카탈로그를 생성합니다(방법 3의 경우 여러 카탈로그 생성).
2. 선택한 구조에 따라 필드와 항목을 추가합니다. [카탈로그 만들기]({{site.baseurl}}/user_guide/data/activation/catalogs/create)를 참조하세요.
3. (선택 사항) [카탈로그 셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 생성하여 항목을 필터링합니다. 예를 들어 사용자 커스텀 속성과 일치하는 `category`로 필터링할 수 있습니다.

{% tabs local %}
{% tab 방법 1: JSON 필드 %}
카탈로그 `PantsLabyrinth_Product_Copy`의 예시 항목:

| 항목 | 값 |
| --- | --- |
| `id` | `trail-runner-001` |
| `name` | `{"EN":"Trail Runner","FR":"Chaussure de trail","DE":"Trailrunner"}` |
| `category` | `footwear` |
| `url` | `https://pantslabyrinth.shop/products/trail-runner-001` |
| `price` | `{"EN":"$120 USD","FR":"112 EUR","DE":"112 EUR"}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON 로케일 필드가 포함된 카탈로그 항목 예시" }

{% endtab %}
{% tab 방법 2: 플랫 필드 %}
카탈로그 `PantsLabyrinth_Promo_Copy`의 예시 항목:

| 항목 | 값 |
| --- | --- |
| `id` | `spring-sale` |
| `header_en` | `Spring trail sale` |
| `header_fr` | `Soldes de printemps` |
| `body_en` | `Save on trail runners this week.` |
| `body_fr` | `Économisez sur les chaussures de trail cette semaine.` |
| `cta_text_en` | `Shop now` |
| `cta_text_fr` | `Acheter` |
| `img_src_en` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
| `img_src_fr` | `https://cdn.pantslabyrinth.shop/fr/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="언어별 플랫 필드가 포함된 카탈로그 항목 예시" }

{% endtab %}
{% tab 방법 3: 언어별 카탈로그 %}
동일한 필드를 가진 언어별 카탈로그를 하나씩 생성합니다. 예를 들어, `pantslabyrinth-promo-fr`과 `pantslabyrinth-promo-de`에 동일한 `id`와 필드를 현지화된 값으로 반복합니다.

`pantslabyrinth-promo-en`의 예시 항목:

| 항목 | 값 |
| --- | --- |
| `id` | `spring-sale` |
| `header` | `Spring trail sale` |
| `body` | `Save on trail runners this week.` |
| `cta_text` | `Shop now` |
| `img_src` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="영어 언어별 카탈로그의 예시 항목" }

{% endtab %}
{% endtabs %}

### 3단계: 메시지에 Liquid 추가하기 {#step-3-add-liquid-to-your-message}

1단계에서 선택한 카탈로그 구조에 맞는 Liquid 패턴을 선택하세요.

{% tabs local %}
{% tab 방법 1: JSON 필드 %}
단일 카탈로그 행의 JSON 오브젝트 필드에 모든 로케일을 저장한 다음, `property_accessor` 필터를 사용하여 {% raw %}`${language}`{% endraw %}(대문자로 정규화)와 일치하는 `name` 및 `price` 키를 읽습니다. 각 필드를 독립적으로 확인하고 해당 필드가 비어 있으면 `EN`으로 대체하여, 이름은 있지만 가격이 없는 로케일에서도 영어 가격이 표시되도록 합니다.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Product_Copy trail-runner-001 %}
{% assign lang = ${language} | upcase %}
{% assign localized_name = items[0].name | property_accessor: lang %}
{% assign localized_price = items[0].price | property_accessor: lang %}
{% if localized_name == blank %}
  {% assign localized_name = items[0].name | property_accessor: 'EN' %}
{% endif %}
{% if localized_price == blank %}
  {% assign localized_price = items[0].price | property_accessor: 'EN' %}
{% endif %}
Product: {{ localized_name }}
Price: {{ localized_price }}
```
{% endraw %}

[Property accessor 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter)를 참조하세요.
{% endtab %}
{% tab 방법 2: 플랫 필드 %}
{% raw %}`${language}`{% endraw %}(소문자로 정규화)를 사용하여 동적 필드 이름을 구성한 다음, 대괄호 조회를 통해 항목에서 해당 필드를 읽습니다. 예를 들어, {% raw %}`items[0][header_field]`{% endraw %}는 해석된 언어의 헤더를 읽습니다. 각 필드를 독립적으로 확인하고 해당 필드가 비어 있으면 영어 컬럼으로 대체하여, 헤더는 있지만 본문이 없는 로케일에서도 영어 본문이 표시되도록 합니다.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Promo_Copy spring-sale %}
{% assign lang = ${language} | downcase %}
{% assign header_field = 'header_' | append: lang %}
{% assign body_field = 'body_' | append: lang %}
{% assign cta_field = 'cta_text_' | append: lang %}
{% assign img_field = 'img_src_' | append: lang %}
{% assign header_val = items[0][header_field] %}
{% assign body_val = items[0][body_field] %}
{% assign cta_val = items[0][cta_field] %}
{% assign img_val = items[0][img_field] %}
{% if header_val == blank %}
  {% assign header_val = items[0].header_en %}
{% endif %}
{% if body_val == blank %}
  {% assign body_val = items[0].body_en %}
{% endif %}
{% if cta_val == blank %}
  {% assign cta_val = items[0].cta_text_en %}
{% endif %}
{% if img_val == blank %}
  {% assign img_val = items[0].img_src_en %}
{% endif %}
<img src="{{ img_val }}" alt="" />
<h2>{{ header_val }}</h2>
<p>{{ body_val }}</p>
<a href="#">{{ cta_val }}</a>
```
{% endraw %}
{% endtab %}
{% tab 방법 3: 언어별 카탈로그 %}
{% alert warning %}
`catalog_items`에 전달한 카탈로그 이름이 존재하지 않으면 Braze가 메시지를 중단합니다. 카탈로그 이름을 작성하기 전에 지원되는 언어 코드를 허용 목록에 추가하세요. 기존 카탈로그에서 항목 ID가 없으면 빈 항목 배열이 반환되며, 이 경우에만 영어 카탈로그로 대체할 수 있습니다.
{% endalert %}

일치하는 카탈로그가 있는 언어 코드(여기서는 `en`, `fr`, `de`)를 허용 목록에 추가하고, 지원되지 않거나 비어 있는 값은 `en`으로 기본 설정한 다음 항목을 조회합니다. 해당 카탈로그에 항목 ID가 없으면 영어 카탈로그로 대체합니다.

{% raw %}
```liquid
{% assign lang = ${language} | downcase %}
{% assign supported = 'en,fr,de' | split: ',' %}
{% if supported contains lang %}{% else %}{% assign lang = 'en' %}{% endif %}
{% assign theCatalog = 'pantslabyrinth-promo-' | append: lang %}
{% catalog_items {{ theCatalog }} spring-sale %}
{% if items[0] == blank %}
  {% catalog_items pantslabyrinth-promo-en spring-sale %}
{% endif %}
<img src="{{ items[0].img_src }}" alt="" />
<h2>{{ items[0].header }}</h2>
<p>{{ items[0].body }}</p>
<a href="#">{{ items[0].cta_text }}</a>
```
{% endraw %}

[카탈로그 이름에 템플릿 사용하기]({{site.baseurl}}/user_guide/data/activation/catalogs/create#template-catalog-names) 및 [메시지 중단하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)를 참조하세요.
{% endtab %}
{% endtabs %}

#### 카테고리별 선택적 카탈로그 셀렉션 {#optional-catalog-selection-by-category}

개인화 전에 항목을 필터링합니다. 예를 들어 `preferred_category = footwear`인 사용자를 위한 신발 프로모션:

{% raw %}
```liquid
{% catalog_selection_items PantsLabyrinth_Product_Copy footwear_promos %}
{% for item in items %}
  {{ item.name }}
{% endfor %}
```
{% endraw %}

대시보드에서 `category` 컬럼에 대한 필터와 필요에 따라 사용자 속성을 사용하여 셀렉션을 정의하세요.

### 4단계: 미리보기 및 테스트 {#step-4-preview-and-test}

1. {% raw %}`${language}`{% endraw %} 값이 다른 고객 프로필로 **사용자로 미리보기**를 사용합니다.
2. 부분적인 로케일(예: 이름은 있지만 가격이 없는 경우)을 포함하여 언어가 누락되었거나 지원되지 않을 때 대체 문구가 올바르게 표시되는지 확인합니다.
3. 방법 3의 경우, 허용 목록에 있는 모든 언어에 일치하는 카탈로그가 있는지, 지원되지 않는 언어 코드가 발송을 중단하지 않고 기본 카탈로그로 매핑되는지 확인합니다.

## 관련 문서 {#related-articles}

- [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [카탈로그 사용하기]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [카탈로그 만들기]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [고급 Liquid 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter)
- [현지화]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [카탈로그 데이터 동기화 및 삭제]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)
- [Liquid 메시지 중단하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)