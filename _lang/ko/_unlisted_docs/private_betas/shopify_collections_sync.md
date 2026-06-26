---
nav_title: Shopify 컬렉션 동기화
article_title: Shopify 컬렉션 동기화
permalink: "/shopify_collections_sync/"
description: "이 참조 문서에서는 Shopify 컬렉션 동기화를 설정하는 방법을 다루며, 이를 통해 제품을 컬렉션으로 그룹화하여 고객이 카테고리별로 제품을 찾을 수 있도록 합니다."
hidden: true
---

# Shopify 컬렉션 동기화 베타 {#shopify-collections-sync-beta}

> Shopify 컬렉션 동기화를 사용하면 제품을 컬렉션으로 그룹화하여 고객이 카테고리별로 제품을 찾을 수 있습니다. 보다 원활한 쇼핑 경험을 위해 Braze 메시징에 쇼핑몰 컬렉션 내 항목을 포함할 수 있습니다.

{% alert important %}
Shopify 컬렉션 동기화는 현재 베타 버전입니다. 베타에 참여하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## Shopify 컬렉션 동기화 설정 {#setting-up-shopify-collections-sync}

Shopify 스토어의 제품을 Braze에 동기화하려면 [Shopify 통합]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#setting-up-shopify-in-braze)의 **제품 동기화** 단계에서 **Shopify 컬렉션 동기화** 체크박스를 선택합니다.<br><br>![Shopify 제품 동기화의 4단계에서 "Shopify 컬렉션 동기화" 체크박스가 선택된 모습.][1]

제품이 동기화되면 Shopify 카탈로그를 확인하여 어떤 제품이 컬렉션에 연결되어 있는지 볼 수 있습니다. <br><br>![카탈로그 테이블 행에 "best-sellers" 및 "front page" 컬렉션에 포함된 제품이 표시된 모습.][2]

Shopify 카탈로그에서 **Selections** 탭을 통해 Shopify 컬렉션을 확인할 수 있습니다. <br><br>!["best-sellers"와 "front page" 두 개의 컬렉션 목록이 표시된 Selections 탭.][3]

### 베타 기능 {#beta-functionality}

- Braze는 최대 30개의 컬렉션을 지원합니다.
- 컬렉션의 정렬 순서는 현재 유지되거나 지원되지 않습니다. 현재 정렬 순서는 다음을 기반으로 합니다:
    - 컬렉션에 가장 최근에 추가된 항목.
    - 지속적인 동기화 중 항목이 업데이트되는 순서.
    - Shopify 컬렉션의 Selections 탭에서 선택한 순서.

## Shopify 컬렉션 사용 {#using-shopify-collections}

Shopify 컬렉션을 사용하여 Campaign(캠페인)의 각 사용자에게 맞춤 메시지를 개인화할 수 있으며, [Braze Selection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)을 사용하는 방식과 유사합니다.

{% alert warning %}
베타에서 다음 동작에 유의하세요: <br><br>Shopify 컬렉션 설명이나 필터 설정을 업데이트하면 Shopify 컬렉션 동기화가 중단됩니다. 그 결과 Shopify 컬렉션이 예상대로 작동하지 않습니다.
{% endalert %}

### 1단계: Shopify 컬렉션의 정렬 순서 구성 {#step-1-configure-the-sort-order-of-your-shopify-collection}

1. Shopify 컬렉션의 Selections 탭에서 **Sort Order**를 선택하여 Shopify 컬렉션 결과가 반환되는 순서를 지정합니다. 정렬 순서를 무작위로 설정하는 옵션도 포함되어 있습니다.
2. **Limit number**에 최대 결과 수(최대 50)를 입력합니다.
3. **Update Selection**을 선택합니다.

![필터 설정, 정렬 유형 및 결과 제한을 선택할 수 있는 Selection 편집 페이지.][4]

### 2단계: Campaign에서 컬렉션 사용 {#step-2-use-the-collection-in-a-campaign}

1. Campaign을 생성한 다음 메시지 작성기에서 **+ Personalization**을 선택합니다.
2. 다음을 선택합니다:<br>- **개인화 유형**으로 **Catalog Items**<br>- 카탈로그 이름<br>- 항목 선택 방법<br>- Selection 이름(Shopify 컬렉션 이름) <br>- 메시지에 표시할 정보

{: start="3"}
3. 메시지에서 정보를 표시할 위치에 Liquid 스니펫을 복사하여 붙여넣습니다.

![카탈로그, 항목 선택 방법 및 표시할 정보를 선택하는 필드가 있는 "Add Personalization" 섹션.][5]{: style="max-width:30%;"}

#### Selection 결과의 Liquid {#liquid-in-selection-results}

커스텀 속성 및 커스텀 이벤트와 같은 카탈로그의 결과를 사용하면 Selection에서 각 사용자에 대해 다른 결과가 반환될 수 있습니다.

[1]: {% image_buster /assets/unlisted_docs/img/shopify/sync_products.png %}
[2]: {% image_buster /assets/unlisted_docs/img/shopify/view_catalog.png %}
[3]: {% image_buster /assets/unlisted_docs/img/shopify/selections_tab.png %}
[4]: {% image_buster /assets/unlisted_docs/img/shopify/edit_selection.png %}
[5]: {% image_buster /assets/unlisted_docs/img/shopify/add_personalization.png %}