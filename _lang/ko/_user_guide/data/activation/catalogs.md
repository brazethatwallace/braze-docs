---
nav_title: 카탈로그
article_title: 카탈로그
page_order: 3
layout: dev_guide

guide_top_header: "카탈로그"
guide_top_text: "카탈로그는 Liquid를 통해 커스텀 속성이나 커스텀 이벤트 속성정보에 액세스하는 방법과 유사하게, 가져온 CSV 파일 및 API 엔드포인트의 데이터에 액세스하여 메시지를 보강합니다."

description: "이 랜딩 페이지는 카탈로그에 대한 페이지입니다. 카탈로그와 필터링된 세트를 사용하여 Braze Campaign에서 비사용자 데이터를 활용해 개인화된 메시지를 보낼 수 있습니다."

guide_featured_title: "섹션 문서"
guide_featured_list:
- name: 카탈로그 생성
  link: /docs/user_guide/data/activation/catalogs/create
  image: /assets/img/braze_icons/users-01.svg
- name: 카탈로그 사용
  link: /docs/user_guide/data/activation/catalogs/use
  image: /assets/img/braze_icons/users-01.svg
- name: 재입고 알림
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 가격 인하 알림
  link: /docs/price_drop_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 선택
  link: /docs/user_guide/data/activation/catalogs/selections
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "기타 문서"
guide_menu_list:
- name: 카탈로그 API 엔드포인트
  link: /docs/api/endpoints/catalogs
  image: /assets/img/braze_icons/server-01.svg
- name: 드래그 앤 드롭 제품 블록
  link: /docs/dnd_product_blocks
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## 카탈로그 사용 사례 {#catalog-use-cases}

모든 유형의 데이터를 카탈로그로 가져올 수 있습니다. 일반적으로 이 데이터는 제품, 할인, 프로모션, 이벤트 등과 같은 오퍼링에 대한 메타데이터입니다. 이 데이터를 사용하여 관련성이 높은 메시지로 사용자를 타겟팅하는 방법에 대한 몇 가지 예는 아래 사용 사례를 참조하세요.

### 소매 및 이커머스 {#retail-and-ecommerce}

- **시즌별 프로모션:** 시즌별 제품 컬렉션을 가져오고 최신 트렌드를 반영하여 메시지를 개인화하세요.
- **현지화된 메시지:** 실제 위치 주소, 영업시간, 서비스를 가져온 다음 사용자 위치를 기반으로 알림을 개인화하세요.
- **재입고 알림:** 재고 수량이 포함된 제품 정보를 가져온 다음, [재입고 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)과 Braze 커스텀 이벤트를 사용하여 제품이 재입고되었음을 사용자에게 알리는 Campaign 또는 Canvas를 트리거하세요.
- **가격 인하 알림:** 제품 가격이 포함된 제품 정보를 가져온 다음, [가격 인하 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications)과 Braze 커스텀 이벤트를 사용하여 제품 가격이 인하되었음을 사용자에게 알리는 Canvas를 트리거하세요.

### 엔터테인먼트 {#entertainment}

- **구독 요금제:** 구독 요금제를 가져오고 사용 패턴과 가장 자주 소비하는 콘텐츠 유형에 따라 사용자에게 추가 기능을 홍보하세요.
- **예정된 이벤트:** 예정된 이벤트 목록과 해당 위치 및 오디언스 연령을 가져온 다음, 해당 지역 범위 내에 있고 타겟 연령대에 해당하는 사용자에게 개인화된 알림을 보내세요.
- **미디어 선호도:** 영화와 프로그램에 대한 정보를 가져온 다음, 사용자가 즐겨찾기한 타이틀과 가장 많이 시청한 장르를 기반으로 콘텐츠를 추천하세요.

### 여행 및 접객업 {#travel-and-hospitality}

- **여행지:** 여행지와 가장 인기 있는 명소, 레스토랑, 액티비티를 가져온 다음, 이전 여행을 기반으로 사용자에게 개인화된 추천을 제공하세요.
- **숙박 시설:** 호텔 숙소와 편의시설, 객실 유형 및 가격을 가져온 다음, 선택한 선호도에 따라 사용자에게 프로모션을 전송하세요.
- **여행 수단:** 항공편, 기차, 렌터카 등 여행 수단에 대한 특가 및 프로모션을 가져온 다음, 최근 검색 기록을 기반으로 사용자에게 전송하세요.
- **식사 선호도:** 식사 오퍼링에 대한 정보를 가져오고 [선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 사용하여 가장 최근에 본 음식 카테고리를 기반으로 특정 식사 선호도를 가진 사용자에게 개인화된 메시지를 보내세요.

## 카탈로그와 Liquid가 함께 작동하는 방식 {#how-catalogs-and-liquid-work-together}

카탈로그는 데이터 저장 기능입니다. 개인화를 위해 메시지에서 참조할 수 있는 대규모 데이터 세트가 포함되어 있습니다. 실제로 데이터를 참조하려면 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 템플릿 언어로 사용합니다. 즉, 카탈로그는 데이터가 보관되는 저장소이고, Liquid는 저장소에서 관련 데이터를 가져오는 언어입니다.

Liquid를 사용하여 카탈로그 정보를 가져오는 방법에 대한 예는 [카탈로그 생성]({{site.baseurl}}/user_guide/data/activation/catalogs/create#additional-use-cases)의 추가 사용 사례를 참조하세요.

## 데이터 저장 제한 {#data-storage-limitations}

카탈로그의 데이터 저장 용량은 카탈로그 항목의 크기에 따라 제한되며, 업로드된 CSV 파일의 크기와 다를 수 있습니다.

카탈로그 무료 버전의 경우 허용되는 저장 용량은 최대 500&nbsp;MB입니다. 저장 공간이 500&nbsp;MB를 초과하지 않는 한 항목 수에는 제한이 없습니다.

Catalogs Pro의 경우 저장 용량 옵션은 5&nbsp;GB, 10&nbsp;GB, 15&nbsp;GB 또는 50&nbsp;GB입니다. 무료 버전의 저장 용량(500&nbsp;MB)은 각 요금제에 포함되어 있습니다.

카탈로그 저장 용량을 업그레이드해야 하는 경우 Braze 계정 매니저에게 문의하세요. 요금제 세부 정보 및 자격 참고 사항은 [카탈로그 저장 용량]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers)을 참조하세요.