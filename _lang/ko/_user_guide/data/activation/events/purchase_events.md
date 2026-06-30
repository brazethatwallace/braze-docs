---
nav_title: 구매 이벤트
article_title: 구매 이벤트
page_order: 3
page_type: reference
description: "이 참조 문서에서는 구매 이벤트 및 속성정보, 사용 방법, 세분화, 관련 분석을 볼 수 있는 위치 등에 대해 설명합니다."
search_rank: 3
---

# 구매 이벤트 {#purchase-events}

> 이 페이지에서는 구매 이벤트 및 속성정보, 사용 방법, 세분화, 관련 분석을 볼 수 있는 위치 등에 대해 설명합니다.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

구매 이벤트는 사용자가 수행한 구매 동작으로, 인앱 구매를 기록하고 각 고객 프로필의 생애주기 가치(LTV)를 설정하는 데 사용됩니다. 이러한 이벤트는 팀에서 설정해야 합니다. 구매 이벤트를 기록하면 수량 및 유형과 같은 속성정보를 추가할 수 있으므로 이러한 속성정보를 기반으로 사용자를 더욱 타겟팅할 수 있습니다.

## 구매 이벤트 기록 {#log-purchase-events}

구매를 기록하려면 [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object)를 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)로 전달하거나, 아래에 나열된 SDK 라이브러리 중 하나를 사용하세요.

{% alert note %}
구매 이벤트 속성정보는 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events#expected-format)와 동일한 데이터 유형을 사용합니다.
{% endalert %}

다음은 다양한 플랫폼에서 구매를 기록하는 데 사용되는 메서드를 나열한 것입니다. 이 페이지에서는 구매 이벤트에 속성정보 및 수량을 추가하는 방법에 대한 설명서도 확인할 수 있습니다. 이러한 속성정보를 기반으로 사용자를 추가로 타겟팅할 수 있습니다.

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=unity)
- [.NET MAUI(구 Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=roku)

## 구매 데이터 보기 {#view-purchase-data}

구매 이벤트를 설정하고 기록을 시작한 후, [개요 탭]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab)에서 사용자 프로필의 구매 데이터를 확인할 수 있습니다.

## 구매 데이터 사용 {#use-purchase-data}

Braze에서 구매 데이터를 사용하는 방법은 여러 가지가 있습니다:

- **[세분화](#purchase-event-segmentation):** 구매 데이터를 사용하여 구매 행동을 기반으로 사용자 Segment를 생성합니다.
- **[개인화](#personalization):** 구매 데이터를 사용하여 사용자에게 메시지를 개인화합니다.
- **[메시지 트리거](#trigger-messages):** 구매 이벤트를 기반으로 메시지가 트리거되도록 설정합니다.
- **[분석](#analytics):** 구매 데이터를 분석하여 사용자 행동과 마케팅 Campaign의 효과에 대한 인사이트를 얻습니다.

### 세분화 {#purchase-event-segmentation}

기록된 구매 이벤트를 기반으로 원하는 수와 유형의 후속 Campaign을 트리거할 수 있습니다. 예를 들어, 지난 30일 동안 구매한 사용자 Segment나 특정 금액 이상을 지출한 사용자 Segment를 생성할 수 있습니다.

사용자를 타겟팅할 때 다음과 같은 세분화 필터를 사용할 수 있습니다:

- First Made Purchase
- First Purchase For App
- Last Purchased Product
- Money Spent
- Purchased Product
- Total Number of Purchases
- X Money Spent in Y Days
- X Product Purchased in Y Days
- X Purchase Property in Y Days
- X Purchases in Last Y Days

각 필터에 대한 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) 용어집을 참조하고 "Purchase behavior"로 필터링하세요.

![정확히 3회 구매한 사용자 필터링]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
특정 구매가 발생한 횟수를 기준으로 세분화하려면, 해당 구매를 [증분 커스텀 속성]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#custom-attribute-storage)으로 개별적으로 기록하세요.
{% endalert %}

### 개인화 {#personalization}

사용자로부터 수집하는 다른 유형의 데이터와 마찬가지로, 구매 데이터를 사용하여 Liquid를 통해 메시징을 개인화할 수 있습니다. 예를 들어, 사용자가 방금 구매한 제품과 유사한 제품을 추천하는 개인화된 이메일을 보낼 수 있습니다.

사용자가 마지막으로 구매한 제품의 이름을 저장하는 `last_purchased_product`라는 구매 이벤트 속성정보가 있다고 가정해 보겠습니다. 이 속성정보를 사용하여 다음과 같이 이메일 메시지를 개인화할 수 있습니다:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

이 예시에서는 `last_purchased_product` 속성정보를 기반으로 메시지가 개인화됩니다. 사용자가 마지막으로 구매한 제품이 "Running Shoes"인 경우, 러닝 반바지와 물병을 추천하는 메시지를 받습니다. 마지막 제품이 "Yoga Mat"인 경우, 요가 블록과 스트랩을 추천하는 메시지를 받습니다. `last_purchased_product`가 다른 것인 경우, 일반적인 감사 메시지를 받습니다.

### 메시지 트리거 {#trigger-messages}

일반적인 사용 사례는 사용자가 구매할 때 이메일과 같은 메시지를 자동으로 보내는 것입니다. 예를 들어, 감사 메시지나 다음 구매를 위한 할인 코드를 보낼 수 있습니다.

이를 위해 실행 기반 Campaign 또는 Canvas를 생성한 다음, 트리거 동작을 **Make Purchase**로 설정합니다. 구매한 제품이나 구매 금액과 같은 트리거에 대한 추가 조건도 지정할 수 있습니다.

Liquid를 사용하여 트리거된 메시지를 개인화할 수도 있습니다. 다음 예시에서 `${purchase_product_name}`은 Braze 설정에서 구매한 제품의 이름을 저장하는 실제 속성 이름으로 대체해야 하는 커스텀 속성입니다.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### 분석 {#analytics}

세분화를 위한 구매 측정기준 추적 외에도, Braze는 각 제품의 구매 횟수와 시간에 따른 매출도 기록합니다. 이를 통해 가장 인기 있는 제품을 파악하거나 프로모션 Campaign이 매출에 미치는 영향을 측정하는 데 도움이 될 수 있습니다.

이 데이터는 [매출 보고서]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#revenue-data) 페이지에서 확인할 수 있습니다.

### 매출 계산 {#revenue-calculations}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="매출 계산">
  <caption>매출 계산</caption>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">Lifetime Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Lifetime Value Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">Average Daily Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">Daily Purchases</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">Daily Revenue Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### 통화 변환 {#currency-conversion}

구매 이벤트가 USD가 아닌 통화로 기록되면, Braze는 [Open Exchange Rates](http://openexchangerates.org)의 환율을 사용하여 금액을 USD로 변환합니다. 이 환율은 24시간마다 한 번 새로고침됩니다. 환율이 캐시되기 때문에, 특히 급격한 변동을 겪는 통화의 경우 실시간 시장 환율과 약간의 차이가 있을 수 있습니다.

#### 생애 매출 계산 {#lifetime-revenue-calculation}

Braze는 구매 이벤트를 사용하여 사용자의 생애 매출(생애주기 가치 또는 LTV라고도 함)을 계산합니다. 이는 고객과의 전체 미래 관계에서 발생할 순이익에 대한 예측입니다. 이를 통해 고객 확보 및 유지 전략에 대해 정보에 기반한 의사결정을 내릴 수 있습니다.

$$\text{평균 구매 금액} = \frac{\text{총 지출 금액(달러)}}{\text{총 구매 이벤트 수}}$$

Braze에서 사용자의 LTV를 파악할 수 있는 주요 위치는 두 곳입니다:

- 각 앱 및 사이트의 *생애 매출* 및 *사용자당 생애주기 가치*와 같은 전체 측정기준은 [매출 보고서]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#revenue-data)를 참조하세요.
- 특정 사용자의 생애 매출을 파악하려면 해당 [고객 프로필]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab)을 참조하세요.

##### 환불이 생애 매출에 미치는 영향 {#impact-of-refunds-on-lifetime-revenue}

구매 이벤트를 사용하여 구매 데이터를 추적할 때, 음수 `price` 속성정보를 가진 Braze 구매 이벤트를 기록하여 환불을 추적해야 합니다. 이 방법은 생애 매출의 정확한 합계를 유지합니다.

그러나 환불은 추가 구매 이벤트로 집계된다는 점을 유의하세요. 다음 예시를 살펴보겠습니다. Sam이 $12에 첫 구매를 했지만 구매의 일부를 반품하여 $5의 환불을 받았습니다. Sam의 프로필에는 다음과 같이 기록됩니다:

- $12 가격의 구매 1건
- -$5 가격의 구매 1건
- 생애 매출 $7

Sam의 프로필에는 두 건의 구매 이벤트가 있지만, 실제로는 한 번만 구매했습니다. 사용자의 구매 횟수를 기반으로 구축된 Segment나 사용 사례가 있는 경우 이 점을 고려하는 것이 중요합니다. 지속적인 환불은 사용자 프로필의 구매 횟수를 부풀릴 수 있습니다.

## 구매 이벤트 속성정보 {#purchase-properties}

구매 이벤트 속성정보를 사용하면 구매에 속성정보를 설정하여 트리거 조건을 더 세밀하게 지정하고, 메시징의 개인화를 높이며, 원시 데이터 내보내기를 통해 더 정교한 분석을 생성할 수 있습니다. 속성정보 값 유형(문자열, 숫자, 부울, 날짜)은 플랫폼에 따라 다르며, 일반적으로 키-값 페어로 할당됩니다.

{% alert warning %}
다음 키는 예약되어 있으며 구매 이벤트 속성정보 이름으로 사용할 수 없습니다: `time`, `product_id`, `quantity`, `event_name`, `price`, `currency`. `properties` 오브젝트에서 예약된 키를 사용하면 "Invalid 'properties' field" 오류가 반환됩니다.
{% endalert %}

예를 들어, 이커머스 애플리케이션이 있고 사용자가 구매한 후 메시지를 보내려는 경우, `brand_name`이라는 구매 이벤트 속성정보를 추가하여 타겟 오디언스를 개선하고 Campaign 개인화를 높일 수 있습니다.

**구매 이벤트 속성정보를 기반으로 트리거하는 예시:**

![브랜드 이름이 HeadphoneMart인 헤드폰을 구매한 사용자에게 Campaign을 보내는 실행 기반 전달 설정]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

자세한 내용은 [구매 속성정보 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-properties-object)를 참조하세요.

### 이벤트 속성정보 세분화 {#event-property-segmentation}

이벤트 속성정보 세분화를 사용하면 커스텀 이벤트뿐만 아니라 해당 이벤트와 관련된 속성정보를 기반으로도 사용자를 타겟팅할 수 있습니다. 이를 통해 구매 및 커스텀 이벤트를 세분화할 때 추가적인 필터링 옵션을 사용할 수 있습니다.

![구매 이벤트 속성정보에 대한 세분화 필터로, 특정 구매 이벤트 속성정보 값을 기반으로 사용자를 필터링하는 옵션을 표시합니다. 예를 들어, 설정된 기간 내에 특정 속성정보를 가진 제품을 구매한 사용자를 필터링합니다.]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

이러한 세분화 필터에는 다음이 포함됩니다:
- 최근 Y일 동안 속성정보 Y의 값이 V인 커스텀 이벤트를 X회 수행한 경우
- 최근 Y일 동안 속성정보 Y의 값이 V인 구매를 X회 한 경우
- 모든 구매, 이벤트, 구매 및 이벤트 내 속성정보에 대해 1~30일 세분화 추가

[세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)과 달리, 사용되는 Segment는 실시간으로 업데이트되고, 무제한의 Segment를 지원하며, 최대 30일의 조회 기록을 제공하고, 데이터 포인트가 발생합니다. 추가 데이터 포인트 비용이 발생하므로, 커스텀 이벤트에 대한 이벤트 속성정보를 활성화하려면 Braze 고객 성공 매니저에게 문의해야 합니다.

승인되면 **데이터 설정** > **커스텀 이벤트**에서 **등록정보 관리**를 선택하여 대시보드에서 추가 속성정보를 추가할 수 있습니다. 그런 다음 Campaign 또는 Canvas 빌더의 타겟 단계에서 이러한 이벤트 속성정보를 사용할 수 있습니다.

### Canvas 진입 속성정보 및 이벤트 속성정보 {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### 주문 수준에서 구매 기록 {#log-purchases-at-the-order-level}

제품 수준이 아닌 주문 수준에서 구매를 기록하려면, 주문 이름 또는 주문 카테고리를 `product_id`로 사용하세요. 자세한 내용은 [구매 오브젝트 사양]({{site.baseurl}}/api/objects_filters/purchase_object#product-id-naming-conventions)을 참조하세요.

### 제품 ID 명명 규칙 {#product-id-naming-conventions}

Braze에서는 구매 오브젝트 `product_id`에 대한 일반적인 명명 규칙을 제공합니다. `product_id`를 선택할 때, Braze는 이 `product_id`로 기록된 모든 항목을 그룹화할 목적으로 SKU 대신 제품 이름이나 제품 카테고리와 같은 간단한 이름을 사용할 것을 권장합니다.

이렇게 하면 세분화 및 트리거를 위해 제품을 쉽게 식별할 수 있습니다.

## 구매 이벤트 차단 목록 {#blocklist-purchase-events}

데이터 포인트를 너무 많이 기록하거나, 마케팅 전략에 더 이상 유용하지 않거나, 실수로 기록된 구매 이벤트를 발견할 수 있습니다. 이 데이터가 Braze로 전송되는 것을 중지하려면, 엔지니어링 팀이 앱 또는 웹사이트의 백엔드에서 제거하는 작업을 진행하는 동안 커스텀 데이터 오브젝트를 차단 목록에 추가할 수 있습니다.

Braze 대시보드에서 **데이터 설정** > **제품**으로 이동하여 차단 목록을 관리할 수 있습니다. 자세한 내용은 [커스텀 데이터 관리]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data)를 참조하세요.