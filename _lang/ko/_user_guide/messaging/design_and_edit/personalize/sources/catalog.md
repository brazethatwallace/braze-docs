---
nav_title: 카탈로그
article_title: 카탈로그
page_order: 2
description: "제품 세부 정보, 콘텐츠 피드, 가격 정보 등 비사용자 데이터로 Braze 메시지를 개인화하기 위한 데이터 소스로 카탈로그를 사용하는 방법을 알아보세요."
---

# 카탈로그 {#catalog}

> 카탈로그에 연결하여 메시지에서 비사용자 데이터를 참조하세요. 카탈로그는 제품 정보, 레스토랑 목록, 콘텐츠 피드 등 구조화된 데이터셋을 저장하며, Liquid를 통해 접근하여 모든 메시지를 개인화할 수 있습니다.

## 작동 방식 {#how-it-works}

{% raw %}
CSV 또는 API를 통해 카탈로그에 데이터를 가져온 후, `items` Liquid 태그를 사용하여 메시지에서 카탈로그 항목을 참조할 수 있습니다. 예를 들어, `products`라는 카탈로그에서 제품 이름을 가져오려면 다음과 같이 작성합니다:

```liquid
{% catalog_items products {{${product_id}}} %}
{{items[0].name}} is back in stock!
```
{% endraw %}

카탈로그는 항목당 최대 1,000개의 필드를 지원하며 수백만 개의 행을 저장할 수 있어, 대규모 제품 인벤토리와 콘텐츠 라이브러리에 적합합니다.

## 일반적인 활용 사례 {#common-use-cases}

| 활용 사례 | 설명 |
| --- | --- |
| 제품 세부 정보 | 제품 카탈로그에서 이름, 설명, 가격, 이미지를 삽입합니다 |
| 레스토랑 또는 매장 목록 | 위치별 세부 정보로 메시지를 개인화합니다 |
| 콘텐츠 추천 | 문서, 동영상 또는 기타 미디어 항목을 참조합니다 |
| 이벤트 정보 | 이벤트 날짜, 장소, 설명을 메시지에 가져옵니다 |
| 등급 기반 혜택 | 사용자의 멤버십 레벨 또는 Segment에 맞는 프로모션을 매칭합니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="일반적인 활용 사례" }

## 카탈로그 트리거 {#catalog-triggers}

카탈로그는 카탈로그 트리거를 통해 자동화된 메시징도 지원합니다. 재입고 알림과 가격 인하 알림을 설정하여 카탈로그 항목이 변경될 때 사용자에게 자동으로 메시지를 보낼 수 있습니다.

자세한 내용은 [카탈로그 트리거]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers)를 참조하세요.

## 선택 {#selections}

선택을 사용하여 정의한 필터로 카탈로그 항목을 그룹화할 수 있습니다. 예를 들어, $20 미만의 항목이나 특정 카테고리의 항목으로 선택을 만든 다음, 필터링된 세트를 메시지에서 참조할 수 있습니다.

자세한 내용은 [선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 참조하세요.

## 시작하기 {#getting-started}

카탈로그를 생성하고 관리하려면 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)를 참조하세요. 메시지에서 카탈로그 데이터를 참조하는 방법을 알아보려면 [메시지에서 카탈로그 사용하기]({{site.baseurl}}/user_guide/data/activation/catalogs/use)를 참조하세요.