---
nav_title: 이커머스 활용 사례
article_title: 이커머스 활용 사례
alias: /ecommerce_use_cases/
page_order: 4
description: "이 참조 문서에서는 이커머스 마케터를 위해 특별히 설계된 여러 사전 구축 Braze 템플릿을 다루며, 필수 전략을 더 쉽게 구현할 수 있도록 합니다."
toc_headers: h2
---

# 이커머스 추천 이벤트 사용 방법 {#how-to-use-ecommerce-recommended-events}

> 이 페이지에서는 Braze 이커머스 Canvas 템플릿 사용 방법을 포함하여, 플랫폼 전반에서 이커머스 추천 이벤트를 사용하는 방법과 위치를 다룹니다.

{% alert note %}
새로운 Shopify 커넥터를 사용하고 있다면, 이커머스 추천 이벤트가 통합을 통해 자동으로 제공됩니다.
{% endalert %}

## Canvas 템플릿 사용하기 {#using-a-canvas-template}

Canvas 템플릿을 사용하려면:
1. **메시징** > **Canvas**로 이동합니다.
2. **Canvas 만들기** > **Canvas 템플릿 사용**을 선택합니다.
3. **Braze 템플릿** 탭에서 사용하려는 템플릿을 찾습니다. 템플릿 이름을 선택하면 미리보기할 수 있습니다.
4. 사용하려는 템플릿에 대해 **템플릿 적용**을 선택합니다.<br><br>!["Canvas 템플릿" 페이지가 "Braze 템플릿" 탭으로 열려 있으며, 최근 사용한 템플릿 목록과 선택 가능한 Braze 템플릿이 표시됩니다.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## 이커머스 Canvas 템플릿 {#ecommerce-canvas-templates}

Braze는 네 가지 이커머스 Canvas 템플릿을 제공합니다.

{% multi_lang_include canvas/ecommerce_templates.md %}

## 메시지 개인화 {#message-personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)는 Braze에서 사용하는 강력한 템플릿 언어로, 고객을 위한 동적이고 개인화된 콘텐츠를 만들 수 있습니다. Liquid 태그를 사용하면 고객 데이터, 제품 정보 및 기타 변수를 기반으로 메시지를 커스터마이즈하여 쇼핑 경험을 향상시키고 인게이지먼트를 유도할 수 있습니다.

### Liquid의 주요 기능 {#key-features-of-liquid}

- **동적 콘텐츠:** 이름, 주문 세부 정보, 선호도 등 고객별 정보를 메시지에 삽입합니다.
- **조건 로직:** if/else 문을 사용하여 특정 조건(예: 고객 위치 및 구매 이력)에 따라 다른 콘텐츠를 표시합니다.
- **루프:** 제품 또는 고객 데이터 컬렉션을 반복(Iterate)하여 항목의 목록이나 그리드를 표시합니다.

### Liquid 시작하기 {#getting-started-with-liquid}

Liquid 태그를 사용하여 메시지를 개인화하려면 다음 리소스를 참조하세요:

- 사전 정의된 Liquid 태그가 포함된 <a href="/docs/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events">Shopify 데이터</a> 참조
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)

## 세분화 {#segmentation}

Braze Segments를 사용하여 특정 속성과 동작을 기반으로 타겟 고객 세그먼트를 만들고, 개인화된 메시징과 Campaigns를 전달하세요. 이 강력한 기능을 통해 적절한 오디언스에게 적절한 메시지를 적절한 시간에 전달하여 고객과 효과적으로 소통할 수 있습니다.

Segments 시작에 대한 자세한 내용은 [Braze Segments 소개]({{site.baseurl}}/user_guide/audience/segments#about-braze-segments)를 확인하세요.

### 추천 이벤트 {#recommended-events}

이커머스 이벤트는 [추천 이벤트]({{site.baseurl}}/recommended_events)를 기반으로 합니다.
추천 이벤트는 더 구체적인 커스텀 이벤트이므로, [커스텀 이벤트 필터]({{site.baseurl}}/user_guide/data/activation/events/custom_events#segmentation-filters)를 선택하여 추천 이커머스 이벤트 이름을 검색할 수 있습니다.

### 이커머스 필터 {#ecommerce-filters}

세그먼터 내의 **Ecommerce** 섹션으로 이동하여 **Ecommerce Source** 및 **Total Revenue**와 같은 이커머스 필터로 사용자를 세분화하세요.

이커머스 필터 목록과 정의에 대해서는 [Segment 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하고 "eCommerce" 검색 카테고리를 선택하세요.

!["Ecommerce" 필터가 표시된 Segment 필터 드롭다운.]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## 중첩된 이벤트 속성정보 {#nested-event-properties}

중첩된 이벤트 속성정보로 세분화하려면 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension#why-use-segment-extensions)을 활용할 수 있습니다. 예를 들어, 세그먼트 확장을 사용하여 지난 90일 동안 "SKU-123" 제품을 구매한 사용자를 찾을 수 있습니다.

## 분석 {#analytics}

### 커스텀 이벤트 보고서 {#custom-events-report}

[커스텀 이벤트 보고서]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics)에서 이커머스 추천 이벤트 볼륨을 추적할 수 있습니다. **Perform Custom Event**로 필터한 다음, [이커머스 추천 이벤트 이름]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)을 지정하여 시간에 따른 성능을 확인하세요.

![선택된 6개 이벤트의 결과를 표시하는 커스텀 이벤트 차트.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### 대시보드 {#dashboards}

#### 전환 대시보드 {#conversions-dashboard}

"Places Order" 전환 이벤트를 사용하여 Campaign 또는 Canvas를 시작한 후, 해당 [전환 보고서]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#setting-up-your-report)를 생성하여 성능을 추적할 수 있습니다.

![Campaigns 및 Canvases와 관련 전환 통계가 포함된 전환 세부 정보 테이블.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### 이커머스 매출 대시보드 {#ecommerce-revenue-dashboard}

사용자가 주문하기 전에 마지막으로 상호작용한 Campaign 또는 Canvas에 기여된 매출에 대한 인사이트를 얻으려면, [이커머스 매출 대시보드]({{site.baseurl}}/ecommerce_revenue_dashboard)를 사용하고 전환 기간을 선택하세요.

### 매출 보고서 {#revenue-report}

이러한 새 이벤트의 데이터를 분석하려면 [대시보드 빌더]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)로 이동하여 [**eCommerce Revenue - Last Touch Attribution** 대시보드]({{site.baseurl}}/ecommerce_revenue_dashboard)를 확인하세요.