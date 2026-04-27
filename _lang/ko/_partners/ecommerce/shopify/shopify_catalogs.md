---
nav_title: Shopify 제품 동기화
article_title: Shopify 제품 동기화
alias: /shopify_catalogs/
page_order: 5
description: "이 참조 문서에서는 Shopify에서 Braze 카탈로그로 제품을 가져오는 방법을 다룹니다."
---

# Shopify 제품 동기화 {#shopify-product-sync}

> Shopify 스토어의 모든 제품을 Braze [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/)에 동기화하여 더 깊은 메시징 개인화를 구현할 수 있습니다.

Shopify 카탈로그는 Shopify 스토어에서 제품을 편집하고 변경할 때 거의 실시간으로 업데이트됩니다. 유기한 장바구니, 주문 확인 등에 최신 제품 세부 정보와 정보를 활용할 수 있습니다.

{% alert warning %}
Braze는 각 Shopify 제품의 배리언트를 최대 250개까지 카탈로그에 동기화합니다. 이 한도를 초과하는 배리언트는 동기화되지 않습니다. 제품당 250개 이상의 배리언트가 필요한 경우 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

## Shopify 제품 동기화 설정하기 {#setting-up}

이미 Shopify 스토어를 설치한 경우에도 아래 지침에 따라 제품을 동기화할 수 있습니다.

### 1단계: 동기화 켜기 {#step-1-turn-on-the-sync}

Shopify 설치 플로우 또는 Shopify 파트너 페이지를 통해 제품을 Braze 카탈로그에 동기화할 수 있습니다.

!["Shopify Variant ID"가 "Catalog product identifier"로 설정된 설정 프로세스의 3단계.]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Braze 카탈로그에 동기화된 제품은 [카탈로그 한도]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers)에 영향을 미칩니다.

### 2단계: 제품 식별자 선택 {#step-2-select-your-product-identifier}

카탈로그 ID로 사용할 제품 식별자를 선택합니다:
- Shopify Variant ID
- SKU

선택한 제품 식별자의 ID 및 헤더 값에는 문자, 숫자, 하이픈, 밑줄만 포함할 수 있습니다. 제품 식별자가 이 형식을 따르지 않으면 Braze가 카탈로그 동기화에서 해당 항목을 필터링합니다.

이것이 Braze 카탈로그 정보를 참조하는 데 사용하는 기본 식별자가 됩니다.

{% alert note %}
SKU를 카탈로그 ID로 선택하는 경우, 스토어의 모든 제품과 배리언트에 SKU가 설정되어 있고 고유한지 확인하세요.
- 항목에 SKU가 누락된 경우 Braze는 해당 제품을 카탈로그에 동기화할 수 없습니다.
- 동일한 SKU를 가진 제품이 두 개 이상인 경우 예기치 않은 동작이 발생하거나 중복 SKU로 인해 제품 정보가 의도치 않게 덮어쓰여질 수 있습니다.
{% endalert %}

### 3단계: 동기화 진행 중 {#step-3-sync-in-progress}

대시보드 알림을 받게 되며, 초기 동기화가 시작되었음을 나타내는 "진행 중" 상태가 표시됩니다. 동기화가 완료되는 데 걸리는 시간은 Braze가 Shopify에서 동기화해야 하는 제품 및 배리언트 수에 따라 달라집니다. 이 시간 동안 이 페이지를 떠나 대시보드 알림이나 이메일로 완료 알림을 기다릴 수 있습니다.

초기 동기화가 [카탈로그 한도]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers)를 초과하면 Braze는 더 이상 제품 동기화를 중단합니다. 시간이 지남에 따라 새 제품이 추가되어 동기화 성공 후 한도를 초과하면 동기화가 더 이상 활성 상태가 아닙니다. 두 경우 모두 Shopify의 제품 업데이트가 더 이상 Braze에 반영되지 않습니다. 티어 업그레이드를 고려하려면 계정 매니저에게 문의하세요.

### 4단계: 동기화 완료 {#step-4-sync-completed}

동기화가 성공하면 대시보드 알림과 이메일을 받게 됩니다. Shopify 파트너 페이지에서도 Shopify 카탈로그 아래의 상태가 "동기화 중"으로 업데이트됩니다. Shopify 파트너 페이지에서 카탈로그 이름을 클릭하여 제품을 확인할 수 있습니다.

카탈로그 데이터를 활용하여 메시지를 개인화하는 방법에 대해 자세히 알아보려면 [카탈로그 추가 활용 사례]({{site.baseurl}}/user_guide/data/activation/catalogs/use/)를 참조하세요.

#### 지원되는 Shopify 카탈로그 데이터 {#supported-shopify-catalog-data}

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Shopify 카탈로그를 어떤 방식으로든 수정하면 실시간 제품 동기화에 의도치 않게 간섭할 수 있습니다. Shopify 카탈로그를 편집하지 마세요. Shopify에 의해 덮어쓰여질 가능성이 있습니다. 대신 Shopify 인스턴스에서 필요한 제품 업데이트를 수행하세요.<br><br>Shopify 카탈로그를 삭제하려면 Shopify 페이지로 이동하여 동기화를 비활성화하세요. 카탈로그 페이지에서 직접 Shopify 카탈로그를 삭제하지 마세요.
{% endalert %}

## 재입고 및 가격 인하 사용 사례 {#back-in-stock-and-price-drop-use-cases}

재입고 알림을 설정하려면 [여기]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/)의 단계를 따르세요.

가격 인하 알림을 설정하려면 [여기]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/)의 단계를 따르세요.

Shopify 통합에서는 각 사용 사례에 대해 카탈로그에서 사용자의 구독 상태를 캡처하는 커스텀 이벤트를 생성해야 합니다. 커스텀 이벤트에는 Shopify 제품 동기화의 일부로 선택한 [SKU 또는 Shopify Variant ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/#step-2-select-your-product-identifier)에 매핑되는 이벤트 속성정보가 필요합니다.

## 카탈로그 ID 변경 {#changing-catalog-id}

Shopify 카탈로그의 제품 식별자를 변경하려면 동기화를 비활성화해야 합니다. 먼저 이 Shopify 카탈로그 데이터를 사용하는 메시지 발송을 중단했는지 확인하세요. Shopify 카탈로그 초기 동기화를 다시 실행하고 [제품 동기화](#setting-up) 단계에 따라 원하는 제품 식별자를 선택하세요.

## 제품 동기화 비활성화 {#deactivate}

Shopify 제품 동기화 기능을 비활성화하면 전체 카탈로그와 제품이 삭제됩니다. 이 카탈로그의 제품 데이터를 활발히 사용 중인 메시지에도 영향을 미칠 수 있습니다. 비활성화 전에 해당 Campaign 또는 Canvas를 업데이트하거나 일시 중지했는지 확인하세요. 그렇지 않으면 제품 세부 정보가 없는 메시지가 발송될 수 있습니다. 카탈로그 페이지에서 직접 Shopify 카탈로그를 삭제하지 마세요.

## 문제 해결 {#troubleshooting}
Shopify 제품 동기화에서 오류가 발생하면 다음 오류 중 하나가 원인일 수 있습니다. 문제를 수정하고 동기화를 해결하는 방법에 대한 지침을 따르세요:

| 오류 | 원인 | 해결 방법 |
| --- | --- | --- |
| 서버 오류 | 제품 동기화를 시도할 때 Shopify 측에서 서버 오류가 발생한 경우입니다. | [동기화를 비활성화](#deactivate)하고 전체 제품 인벤토리를 다시 동기화하세요. |
| 중복 SKU | SKU를 카탈로그 항목 ID로 사용하고 동일한 SKU를 가진 제품이 있는 경우 발생합니다. 카탈로그 항목 ID는 고유해야 하므로 모든 제품에 고유한 SKU가 있어야 합니다. | Shopify에서 전체 제품 및 배리언트 목록을 감사하여 중복 SKU가 없는지 확인하세요. 중복 SKU가 있는 경우 Shopify 스토어 계정에서만 고유한 SKU로 업데이트하세요. 수정 후 [동기화를 비활성화](#deactivate)하고 전체 제품 인벤토리를 다시 동기화하세요. |
| 카탈로그 한도 초과 | 카탈로그 한도를 초과한 경우 발생합니다. Braze는 더 이상 저장 공간이 없어 동기화를 완료하거나 동기화를 활성 상태로 유지할 수 없습니다. | 이 문제에 대한 두 가지 해결 방법이 있습니다:<br><br>1. 카탈로그 한도를 늘리려면 계정 매니저에게 문의하여 티어를 업그레이드하세요.<br><br>2. 다음 항목을 삭제하여 저장 공간을 확보하세요:<br>- 다른 카탈로그의 카탈로그 항목<br>- 다른 카탈로그<br>- 생성된 선택 항목<br><br> 두 해결 방법 중 하나를 사용한 후 동기화를 비활성화한 다음 다시 동기화해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }