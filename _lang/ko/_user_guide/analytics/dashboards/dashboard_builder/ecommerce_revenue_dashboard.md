---
nav_title: eCommerce 매출 대시보드
article_title: eCommerce 매출 대시보드
alias: "/ecommerce_revenue_dashboard/"
page_order: 1
description: "이 문서에서는 eCommerce 매출 - 라스트 터치 기여도 대시보드에 대한 개요를 제공합니다."
---

# eCommerce 매출 대시보드 {#ecommerce-revenue-dashboard}

> **eCommerce 매출 - 라스트 터치 기여도** 대시보드는 [eCommerce 권장 이벤트]({{site.baseurl}}/ecommerce_events)를 사용하여 Campaigns 및 Canvases의 라스트 터치 기여 매출을 추적합니다. 이 대시보드를 사용하여 어떤 메시지가 매출을 유도하는지 파악하고, 시간에 따른 전반적인 eCommerce 성과를 모니터링할 수 있습니다.

{% alert note %}
새로운 [Shopify 커넥터]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores?tab=shopify%20connector)를 사용하는 경우, eCommerce 권장 이벤트는 통합을 통해 자동으로 제공됩니다. 그렇지 않은 경우, 이 대시보드에 데이터가 표시되려면 먼저 이벤트를 구현해야 합니다.
{% endalert %}

eCommerce 매출 대시보드를 보려면 **Analytics** > **대시보드 빌더**로 이동한 다음 **eCommerce Revenue - Last Touch Attribution**을 선택합니다. 이 대시보드는 선택한 전환 기간 내에서 사용자가 주문하기 전에 마지막으로 상호작용한 Campaign 또는 Canvas에 기여된 매출을 보고합니다.

![eCommerce 매출 - 라스트 터치 기여도 대시보드에 eCommerce 매출, 일일 주문 수, 일일 평균 eCommerce 매출 통계와 시간별 eCommerce 매출 차트가 표시된 모습.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_dashboard.png %})

## 사용 가능한 측정기준 {#available-metrics}

| 측정기준 | 정의 |
| --- | --- |
| eCommerce 매출 | 선택한 날짜 범위 및 전환 기간을 기준으로 한 총 라스트 터치 기여 매출입니다. |
| 일일 주문 수 | 하루 평균 고유 주문 수입니다. |
| 일일 평균 eCommerce 매출 | 선택한 기간의 일일 평균 기여 매출입니다. |
| 시간별 eCommerce 매출 | 선택한 날짜 범위의 기여 매출 시계열입니다. |
| Campaign별 eCommerce 매출 | Campaign별로 분류된 기여 매출입니다. |
| Canvas별 eCommerce 매출 | Canvas별로 분류된 기여 매출입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 가능한 측정기준" }

![Campaign별 eCommerce 매출 및 Canvas별 eCommerce 매출 차트.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_charts.png %})

## 기여도 모델 {#attribution-model}

**eCommerce 매출 - 라스트 터치 기여도** 대시보드는 라스트 터치 기여도를 사용합니다. 이는 사용자가 주문하기 전에 가장 최근에 참여한 Braze Campaign 또는 Canvas에 매출이 기여된다는 것을 의미합니다.

다음 메시지 상호작용이 기여도의 터치 이벤트로 인정됩니다:

- 이메일 클릭
- 푸시 열기
- 콘텐츠 카드 클릭
- 인앱 메시지 클릭
- 단문 메시지 서비스 단축 링크 클릭
- WhatsApp 단축 링크 클릭

{% alert important %}
메시지 상호작용은 선택한 전환 기간 내에 발생해야 합니다. 전환 기간 내에 적격한 메시지 상호작용이 없는 주문은 기여되지 않습니다.
{% endalert %}

## 포함된 데이터 {#included-data}

**eCommerce 매출 - 라스트 터치 기여도** 대시보드는 eCommerce 권장 이벤트의 데이터를 가져옵니다:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

{% alert note %}
**eCommerce 매출 - 라스트 터치 기여도** 대시보드에 데이터가 표시되려면 `ecommerce.order_placed` 이벤트의 `total_value`, `product.price`, `product.quantity`가 `0` 이상이어야 합니다.
{% endalert %}

매출 및 주문 수는 Braze 표준화된 계산을 사용합니다.

| 측정기준 | 계산 |
| --- | --- |
| 총 매출 | 주문 금액 합계 − 환불 금액 합계 |
| 총 주문 수 | 고유 주문 수 − 고유 취소 주문 수 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="포함된 데이터" }

### 제외된 데이터 {#excluded-data}

레거시 구매 이벤트를 사용하여 기록된 구매는 포함되지 않습니다. **eCommerce 매출 - 라스트 터치 기여도** 대시보드는 현재 LTV 또는 Campaigns이나 Canvases 내 매출 보고서와 같은 레거시 구매 이벤트에 연결된 기능을 지원하지 않습니다.

## 통화 처리 {#currency-handling}

모든 매출은 USD로 표시됩니다. USD가 아닌 통화는 이벤트가 보고된 날짜의 환율을 사용하여 USD로 변환됩니다. 변환을 방지하려면 이벤트를 전송할 때 통화를 `USD`로 하드코딩하세요.