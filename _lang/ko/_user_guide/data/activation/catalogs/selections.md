---
nav_title: 선택
article_title: 선택
page_order: 5
alias: /catalog_selections/
description: "이 참조 문서에서는 카탈로그를 사용하여 Braze Campaign에서 데이터를 참조하기 위해 선택 항목을 생성하고 사용하는 방법을 다룹니다."
---

# 선택 {#selections}

> 선택 항목은 Campaign에서 각 사용자에게 메시지를 개인화하는 데 사용할 수 있는 데이터 그룹입니다. 선택을 사용하면 본질적으로 카탈로그의 특정 열을 기반으로 커스텀 필터를 설정하는 것입니다. 여기에는 브랜드, 크기, 위치, 추가된 날짜 등에 대한 필터가 포함될 수 있습니다. 항목이 먼저 충족해야 하는 기준을 정의할 수 있으므로 사용자에게 표시하는 콘텐츠를 제어할 수 있습니다.<br><br>이 페이지에서는 카탈로그를 사용하여 선택 항목을 생성하고 사용하는 방법을 다룹니다.

[카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)를 생성한 후, Braze Campaign이나 추천에 선택 항목을 통합하여 카탈로그 데이터를 추가로 참조할 수 있습니다.

![예제 카탈로그의 선택 섹션.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## 알아두어야 할 사항 {#things-to-know}

- 카탈로그당 최대 30개의 셀렉션을 만들 수 있습니다.
- 셀렉션당 최대 10개의 필터를 추가할 수 있습니다.
- 셀렉션은 Braze 카탈로그 데이터에서 추천 항목을 정제하는 데 유용합니다. 영감이 필요하다면 [아이템 추천 정보]({{site.baseurl}}/user_guide/brazeai/item_recommendations)에서 사용 사례 예시를 확인해 보세요.

## 지리 위치 필터 {#geolocation-filters}

카탈로그에 [지리 위치 필드 유형]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types)이 포함되어 있는 경우, 선택 항목에서 지리 위치 기반 필터를 사용하여 지리적 지점과의 근접성에 따라 카탈로그 항목을 표시할 수 있습니다.

두 가지 지리 위치 연산자를 사용할 수 있습니다.

| 연산자 | 설명 |
| -------- | ----------- |
| `geo within` | 지리 위치 필드가 중심점의 지정된 반경 내에 있는 항목을 반환합니다. |
| `geo outside` | 지리 위치 필드가 중심점의 지정된 반경 밖에 있는 항목을 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

지리 위치 필터가 적용되면, 결과는 가장 가까운 항목이 먼저 오도록 거리순으로 정렬됩니다.

### Liquid로 중심점 설정하기 {#setting-the-center-point-with-liquid}

Liquid를 사용하여 중심점을 동적으로 설정할 수 있습니다. 예를 들어, 각 사용자의 가장 최근 위치를 기준으로 항목을 필터링하려면 {% raw %}`{{${most_recent_location}}}`{% endraw %} 속성을 필터 값으로 사용합니다.

{% raw %}
```
{{${most_recent_location}}}
```
{% endraw %}

### 사용 사례: 가장 가까운 매장 위치 표시하기 {#use-case-show-the-nearest-store-locations}

카탈로그에 지리 위치 유형의 `store_location` 필드가 포함되어 있다고 가정합니다. `geo within` 연산자를 사용하여 각 사용자의 가장 최근 위치로부터 설정된 반경 내의 매장 위치를 반환하는 선택 항목을 만들 수 있습니다. 필터 값을 {% raw %}`{{${most_recent_location}}}`{% endraw %}로 설정하면 중심점이 사용자마다 업데이트됩니다. 결과는 거리순으로 정렬되므로, 처음 반환되는 항목이 항상 가장 가까운 매장입니다.

## 셀렉션 만들기 {#creating-a-selection}

셀렉션을 만들려면 다음과 같이 하세요.

1. **카탈로그**로 이동하여 목록에서 카탈로그를 선택합니다.
2. **셀렉션** 탭을 선택하고 **Create Selection**을 클릭합니다.
3. 셀렉션에 이름과 선택적 설명을 입력합니다.
4. **Filter Field**에서 필터링할 카탈로그 열을 선택합니다. 1,000자를 초과하는 문자열 필드는 필터로 선택할 수 없습니다.
5. 관련 연산자(예: "equals" 또는 "does not equal")와 속성을 선택하여 필터 기준 정의를 완료합니다.
6. **Sort type** 섹션에서 결과 정렬 방식을 결정합니다. 기본적으로 결과는 특정 순서 없이 반환됩니다. 특정 필드로 정렬하려면 **Randomize Sort Order**를 끄고 **Sort Field**와 **Sort Order**(오름차순 또는 내림차순)를 지정합니다.
7. **Results limit** 섹션에서 결과 수를 입력합니다(최대 50개).
8. **Create Selection**을 선택합니다.

### 테스트 및 미리보기 {#test-and-preview}

셀렉션을 만든 후 **Preview for user** 섹션을 사용하여 임의의 사용자 또는 특정 사용자에 대해 셀렉션이 반환하는 내용을 확인할 수 있습니다. 개인화를 사용하는 셀렉션의 경우, 사용자를 선택한 후에만 미리보기를 확인할 수 있습니다.

### 셀렉션 결과에서의 Liquid {#liquid-in-selection-results}

카탈로그에서 커스텀 속성 및 커스텀 이벤트와 같은 Liquid를 사용하면 셀렉션의 각 사용자에 대해 반환되는 결과가 달라질 수 있습니다.

{% alert note %}
연결된 콘텐츠 Liquid는 이러한 필터 설정에서 지원되지 않습니다.
{% endalert %}

![속성이 Liquid 커스텀 속성으로 설정된 카탈로그 셀렉션의 필터 설정.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## 메시징에서 셀렉션 사용하기 {#using-selections-in-messaging}

셀렉션을 생성한 후, Liquid를 사용하여 해당 카탈로그에서 필터링된 항목을 메시지에 삽입하여 개인화할 수 있습니다. 메시지 작성기의 개인화 창에서 Braze가 자동으로 Liquid를 생성하도록 할 수 있습니다:

1. 개인화를 지원하는 메시지 작성기에서 <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="개인화 추가"></i> **개인화 추가**를 선택하여 개인화 창을 엽니다.
2. **개인화 유형**에서 **카탈로그 항목**을 선택합니다.
3. 카탈로그 이름을 선택합니다.
4. **항목 선택 방법**에서 **셀렉션 사용**을 선택합니다.
4. 목록에서 셀렉션을 선택합니다.
5. **표시할 정보**에서 각 항목에 포함할 카탈로그 필드를 선택합니다.
6. **복사** 아이콘을 선택하고 메시지에서 필요한 위치에 Liquid를 붙여넣습니다.

![개인화 추가 Modal에 다음 항목이 선택되어 있습니다: '개인화 유형'에 'Catalog Items', '카탈로그 이름'에 'Games', '셀렉션 유형'에 'Selections', '셀렉션'에 'game_selection', '표시할 정보'에 'title'과 'description_en'.]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

{% alert note %}
Liquid 작성 패널의 개인화 미리보기에는 설정한 결과 제한과 관계없이 최대 3개의 카탈로그 셀렉션이 표시됩니다. 이는 정상적인 동작이며, 사용자에게 실제로 전송되는 메시지는 설정된 결과 제한을 따릅니다.
{% endalert %}

## 사용 사례 {#use-case}

식사 배달 서비스를 운영하고 있으며, 사용자가 가장 최근에 본 음식 카테고리를 기반으로 특정 식사 선호도가 있는 사용자에게 개인화된 메시지를 보내고 싶다고 가정해 보겠습니다.

식사 배달 서비스의 식사 이름, 가격, 이미지, 식사 카테고리 정보가 포함된 카탈로그를 사용하여, 사용자가 가장 최근에 본 카테고리를 기반으로 세 가지 식사를 추천하는 셀렉션을 만들 수 있습니다.

![제품 유형이 식사인 것과 카테고리가 가장 최근에 본 것인 두 개의 필터가 있는 식사 배달 서비스용 셀렉션 예시. 셀렉션은 세 가지 결과가 반환되는 순서를 무작위로 설정합니다.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

이 카탈로그와 셀렉션을 Campaign에서 사용하려면, Campaign 작성 시 메시지 작성 섹션에서 **개인화 추가** Modal을 사용하세요. 이 예시에서는 식사 배달 서비스 정보가 포함된 카탈로그와 가장 최근에 본 카테고리 기반 식사 추천 셀렉션을 선택했습니다. 이를 통해 식사 이름과 가격을 표시할 수 있습니다. 메시지를 더 풍부하게 구성하기 위해, 셀렉션을 사용하여 첫 번째 추천 식사의 이미지도 추가할 수 있습니다.

![헤더가 '이 인기 식사를 정말 좋아하실 거예요!'인 콘텐츠 카드와 메시지 작성 섹션에 'recommendations_be_recent_category' 셀렉션이 표시된 모습.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

예를 들어, 가장 최근에 본 카테고리가 "치킨"인 사용자가 있다고 가정해 보겠습니다. 설정된 개인화와 콘텐츠 카드 캠페인을 사용하면, 이 사용자에게 치킨이 포함된 세 가지 식사 추천을 보낼 수 있습니다.

![숯불 레몬 치킨 이미지가 있는 콘텐츠 카드와 사용자가 가장 최근에 본 카테고리를 기반으로 치킨이 포함된 세 가지 식사 추천 목록.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

동일한 개인화를 사용하여, 가장 최근에 본 카테고리가 "소고기"인 사용자에게도 세 가지 식사 추천을 보낼 수 있습니다.

![비프 스트로가노프 이미지가 있는 콘텐츠 카드와 사용자가 가장 최근에 본 카테고리를 기반으로 소고기가 포함된 두 가지 식사 추천 목록.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}