---
nav_title: 선택
article_title: 선택
page_order: 5
alias: /catalog_selections/
description: "이 참조 문서에서는 카탈로그를 사용하여 Braze Campaigns에서 데이터를 참조하기 위해 선택 항목을 생성하고 사용하는 방법을 다룹니다."
---

# 선택 {#selections}

> 이 페이지에서는 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/)를 사용하여 선택 항목을 생성하고 사용하는 방법을 다룹니다.

## 작동 방식 {#how-it-works}

선택 항목은 Campaign에서 각 사용자에게 메시지를 개인화하는 데 사용할 수 있는 데이터 그룹입니다. 선택을 사용하면 본질적으로 카탈로그의 특정 열을 기반으로 커스텀 필터를 설정하는 것입니다. 여기에는 브랜드, 크기, 위치, 추가된 날짜 등에 대한 필터가 포함될 수 있습니다. 항목이 먼저 충족해야 하는 기준을 정의할 수 있으므로 사용자에게 표시하는 콘텐츠를 제어할 수 있습니다.

카탈로그를 생성한 후, Braze Campaigns이나 추천에 선택 항목을 통합하여 카탈로그 데이터를 추가로 참조할 수 있습니다.

![예제 카탈로그의 선택 섹션입니다.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## 알아야 할 사항 {#things-to-know}

- 카탈로그당 최대 30개의 선택 항목을 만들 수 있습니다.
- 선택당 최대 10개의 필터를 추가할 수 있습니다.
- 선택은 Braze 카탈로그 데이터에서 추천을 세분화하는 데 유용합니다. 영감이 필요하다면 [아이템 추천 소개]({{site.baseurl}}/user_guide/brazeai/item_recommendations/)에서 활용 사례를 확인해 보세요.

## 지원되는 연산자 {#supported-operators}

선택 필터를 생성할 때 사용 가능한 연산자는 선택한 필드 유형에 따라 달라집니다.

| 필드 유형 | 사용 가능한 연산자 |
| --- | --- |
| 문자열 | `equals`, `does not equal`, `is any of`, `is none of` |
| 숫자 | `equals`, `does not equal`, `greater than`, `less than` |
| 부울 | `is` |
| 시간 | `before`, `after` |
| 배열 | `includes value`, `does not include value` |
| 지리 | `geo within`, `geo outside` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported operators" }

`is any of` 및 `is none of` 연산자는 문자열 필드에 사용할 수 있으며 각각 최대 10개의 값을 지원합니다.

## 선택 만들기 {#creating-a-selection}

선택을 만들려면 다음을 수행합니다.

1. **Catalogs**로 이동하여 목록에서 카탈로그를 선택합니다.
2. **Selection** 탭을 선택하고 **Create Selection**을 클릭합니다.
3. 선택 항목에 이름과 선택적 설명을 지정합니다.
4. **Filter Field**에서 필터링할 카탈로그 열을 선택합니다. 1,000자 이상의 문자열 필드는 필터에 선택할 수 없습니다.
5. 관련 연산자와 속성을 선택하여 필터 기준 정의를 완료합니다. 필드 유형별 전체 연산자 목록은 [지원되는 연산자](#supported-operators)를 참조하세요.
6. **Sort type** 섹션에서 결과가 정렬되는 방식을 결정합니다. 기본값으로 결과는 특정한 순서 없이 반환됩니다. 특정 필드로 정렬을 지정하려면 **Randomize Sort Order**를 끄고 **Sort Field** 및 **Sort Order**(오름차순 또는 내림차순)를 지정합니다.
7. **Results limit** 섹션에 결과 수를 입력합니다(최대 50개).
8. **Create Selection**을 선택합니다.

### 테스트 및 미리보기 {#test-and-preview}

선택을 만든 후, **Preview for user** 섹션을 사용하여 무작위 사용자 또는 특정 사용자에 대해 선택이 반환할 내용을 확인할 수 있습니다. 개인화를 사용하는 선택의 경우, 사용자를 선택한 후에만 미리보기를 볼 수 있습니다.

### 선택 결과에서의 Liquid {#liquid-in-selection-results}

카탈로그에서 커스텀 속성 및 커스텀 이벤트와 같은 Liquid를 사용하면 선택 항목에서 각 사용자에 대해 반환되는 결과가 다를 수 있습니다.

{% alert note %}
연결된 콘텐츠 Liquid는 이러한 필터 설정에서 지원되지 않습니다.
{% endalert %}

![속성이 Liquid 커스텀 속성으로 설정된 카탈로그 선택의 필터 설정입니다.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## 메시징에서 선택 사용 {#using-selections-in-messaging}

선택을 만든 후, Liquid를 사용하여 해당 카탈로그에서 필터링된 항목을 삽입하여 메시지를 개인화합니다. 메시지 작성기에 있는 개인화 창에서 Braze가 Liquid를 자동으로 생성하도록 할 수 있습니다.

1. 개인화를 지원하는 메시지 작성기에서 <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Add personalization"></i>를 선택하여 개인화 창을 엽니다.
2. **Personalization Type**에서 **Catalog Items**를 선택합니다.
3. 카탈로그 이름을 선택합니다.
4. **Item selection method**에서 **Use a selection**을 선택합니다.
4. 목록에서 선택 항목을 선택합니다.
5. **Information to Display**에서 각 항목에 포함할 카탈로그 필드를 선택합니다.
6. **Copy** 아이콘을 선택하고 메시지에서 필요한 위치에 Liquid를 붙여넣습니다.

!["Personalization Type"은 "Catalog Items", "Catalog Name"은 "Games", "Selection Type"은 "Selections", "Selection"은 "game_selection", "Information to Display"는 "title"과 "description_en"이 선택된 개인화 추가 모달입니다.]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## 활용 사례 {#use-case}

식사 배달 서비스를 운영하고 있으며, 사용자가 가장 최근에 본 음식 카테고리를 기반으로 특정 식사 선호도를 가진 사용자에게 개인화된 메시지를 보내고 싶다고 가정해 보겠습니다.

식사 이름, 가격, 이미지 및 식사 카테고리에 대한 식사 배달 서비스 정보가 포함된 카탈로그를 사용하여, 사용자가 가장 최근에 본 카테고리를 기반으로 세 가지 식사를 추천하는 선택을 만들 수 있습니다.

![식사 배달 서비스에 대한 선택 예시로, 두 가지 필터가 있습니다. 하나는 제품 유형을 식사로 식별하고, 다른 하나는 카테고리를 가장 최근에 본 것으로 식별합니다. 선택은 세 가지 결과가 반환되는 순서를 무작위로 설정합니다.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Campaign에서 이 카탈로그와 선택 항목을 사용하려면, Campaign 작성의 메시지 구성 섹션에서 **Add Personalization** 모달을 사용합니다. 이 예시에서는 식사 배달 서비스 정보가 포함된 카탈로그와 가장 최근에 본 카테고리를 기반으로 한 식사 추천 선택을 선택했습니다. 이를 통해 식사 이름과 가격을 표시할 수 있습니다. 메시지를 더욱 풍부하게 만들려면 선택 항목을 사용하여 첫 번째 추천 식사의 이미지를 추가할 수도 있습니다.

![메시지 구성 섹션에서 "recommendations_be_recent_category" 선택이 적용된 "You will LOVE these highly rated meals!"라는 헤더가 있는 콘텐츠 카드입니다.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

예를 들어, 사용자가 가장 최근에 본 카테고리가 "치킨"이라고 가정합니다. 설정된 개인화와 콘텐츠 카드 캠페인을 사용하여 이 사용자에게 치킨이 포함된 세 가지 식사 추천을 보낼 수 있습니다.

![숯불 레몬 치킨 이미지가 포함된 콘텐츠 카드와 사용자가 가장 최근에 본 카테고리를 기반으로 치킨이 포함된 세 가지 식사 추천 목록입니다.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

동일한 개인화를 사용하여 가장 최근에 본 카테고리가 "소고기"인 사용자에게도 세 가지 식사 추천을 보낼 수 있습니다.

![소고기 스트로가노프 이미지가 포함된 콘텐츠 카드와 사용자가 가장 최근에 본 카테고리를 기반으로 소고기가 포함된 두 가지 식사 추천 목록입니다.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}