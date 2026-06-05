---
nav_title: eCommerce 이벤트 기록
article_title: Braze SDK를 통한 eCommerce 이벤트 기록
page_order: 3.25
description: "타입이 지정된 이벤트 클래스와 logEcommerceEvent를 사용하여 Braze Android, Swift 및 Web SDK를 통해 eCommerce 권장 이벤트를 기록하는 방법을 알아봅니다."
platform:
  - Android
  - Swift
  - Web
---

# eCommerce 이벤트 기록 {#log-ecommerce-events}

> 타입이 지정된 이벤트 클래스와 `logEcommerceEvent`를 사용하여 Braze Android, Swift 및 Web SDK를 통해 [eCommerce 권장 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/)를 기록하는 방법을 알아봅니다. 이벤트 속성정보 스키마, 플랫폼 기능 및 수집 유효성 검사에 대한 자세한 내용은 [권장 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) 및 [이벤트 유효성 검사 및 문제 해결]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting)을 참조하세요.

{% alert note %}
목록에 없는 래퍼 SDK의 경우, 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

## 이벤트 스키마 {#event-schemas}

6가지 eCommerce 권장 이벤트는 모든 플랫폼에서 주문 수준 스키마를 공유합니다. 각 이벤트 페이로드를 구축할 때 다음 속성정보 테이블을 사용하세요. 전체 유효성 검사 동작 및 REST API 예제가 포함된 정식 스키마는 [권장 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-schemas)를 참조하세요. 세분화, 캔버스 템플릿, 보고서 등 플랫폼 기능에 대한 자세한 내용은 [eCommerce 이벤트 사용 방법]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/)을 참조하세요.

{% tabs local %}
{% tab product_viewed %}

사용자가 제품 상세 페이지를 볼 때 트리거합니다.

**이벤트 속성정보**

| 속성정보 이름 | 데이터 유형 | 필수 | 설명 |
| ------------- | --------- | -------- | ----------- |
| `product_id` | 문자열 | 예 | 고유 제품 식별자(예: SKU 또는 항목 ID). |
| `product_name` | 문자열 | 예 | 제품 표시 이름. |
| `variant_id` | 문자열 | 예 | 제품 배리언트 식별자(예: `shirt_medium_blue`). |
| `image_url` | 문자열 | 아니요 | 제품 이미지 URL. |
| `product_url` | 문자열 | 아니요 | 제품 페이지 URL(상세 정보 확인용). |
| `price` | 플로트 | 예 | 조회 시점의 배리언트 단가. |
| `currency` | 문자열 | 예 | 3자리 ISO 4217 코드(예: `USD` 또는 `EUR`). |
| `source` | 문자열 | 예 | 이벤트가 발생한 소스(예: `web`, `ios` 또는 `android`). |
| `type` | 문자열 배열 | 아니요 | 재입고 및 가격 인하 알림을 위한 Braze 카탈로그 트리거 기능을 사용하려면 필수입니다. 허용 값: `"price_drop"`, `"back_in_stock"`. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어. 인식되는 하위 속성정보: `sku`(문자열). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="제품 조회 이벤트 속성정보" }

{% endtab %}
{% tab cart_updated %}

사용자의 장바구니 내용이 변경될 때마다 트리거합니다. 전체 장바구니 교체(`action`을 생략하거나 `replace`로 설정) 또는 증분 업데이트(`add` 또는 `remove`)를 사용합니다.

**이벤트 속성정보**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `cart_id` | 문자열 | 예 | 장바구니의 고유 식별자. 사용자의 장바구니 매핑을 위해 장바구니, 결제 및 주문 이벤트 간에 공유됩니다. |
| `action` | 문자열 | 아니요 | `add`(수량 증가 또는 라인 추가), `remove`(수량 감소, `0`에서 라인 제거) 또는 `replace`(전체 장바구니 교체, `action` 생략과 동일). |
| `total_value` | 플로트 | 조건부 | `action`이 생략되거나 `replace`일 때 필수. `action`이 `add` 또는 `remove`일 때 선택 사항. |
| `subtotal_value` | 플로트 | 아니요 | 장바구니 소계 값(할인 적용 후, 세금/배송비 적용 전). |
| `tax` | 플로트 | 아니요 | 장바구니에 적용된 총 세금. |
| `shipping` | 플로트 | 아니요 | 장바구니의 총 배송비. |
| `currency` | 문자열 | 예 | 3자리 ISO 4217 코드. |
| `products` | 배열 | 예 | 이 업데이트의 라인 항목. 제품 속성정보 테이블을 참조하세요. |
| `source` | 문자열 | 예 | 이벤트가 발생한 소스. |
| `metadata` | 오브젝트 | 아니요 | 추가 이벤트 수준 데이터를 위한 유연한 키-값 페어. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="장바구니 업데이트 이벤트 속성정보" }

**제품 속성정보(`products[]`)**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 문자열 | 예 | 고유 제품 식별자. |
| `product_name` | 문자열 | 예 | 제품 표시 이름. |
| `variant_id` | 문자열 | 예 | 배리언트 식별자. |
| `image_url` | 문자열 | 아니요 | 제품 이미지 URL. |
| `product_url` | 문자열 | 아니요 | 제품 페이지 URL. |
| `quantity` | 정수 | 예 | 전체 교체의 경우 이 라인의 장바구니 내 수량. `add` 또는 `remove`의 경우 추가하거나 제거할 수량. |
| `price` | 플로트 | 예 | 배리언트 단가. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어(예: `color` 또는 `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="장바구니 업데이트 제품 속성정보" }

{% endtab %}
{% tab checkout_started %}

사용자가 결제 플로우를 시작할 때 트리거합니다.

**이벤트 속성정보**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `checkout_id` | 문자열 | 예 | 결제 세션의 고유 식별자. |
| `cart_id` | 문자열 | 아니요 | 장바구니 식별자. 사용자의 장바구니 매핑을 위해 장바구니, 결제 및 주문 이벤트 간에 공유됩니다. |
| `total_value` | 플로트 | 예 | 결제의 총 금액. |
| `subtotal_value` | 플로트 | 아니요 | 소계 값(할인 적용 후, 세금/배송비 적용 전). |
| `tax` | 플로트 | 아니요 | 결제에 적용된 총 세금. |
| `shipping` | 플로트 | 아니요 | 총 배송비. |
| `currency` | 문자열 | 예 | 3자리 ISO 4217 코드. |
| `products` | 배열 | 예 | 결제 중인 항목. 제품 속성정보 테이블을 참조하세요. |
| `source` | 문자열 | 예 | 이벤트가 발생한 소스. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어. 인식되는 하위 속성정보: `checkout_url`(문자열). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="결제 시작 이벤트 속성정보" }

**제품 속성정보(`products[]`)**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 문자열 | 예 | 고유 제품 식별자. |
| `product_name` | 문자열 | 예 | 제품 표시 이름. |
| `variant_id` | 문자열 | 예 | 배리언트 식별자. |
| `image_url` | 문자열 | 아니요 | 제품 이미지 URL. |
| `product_url` | 문자열 | 아니요 | 제품 페이지 URL. |
| `quantity` | 정수 | 예 | 장바구니 내 수량. |
| `price` | 플로트 | 예 | 배리언트 단가. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어(예: `color` 또는 `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="결제 시작 제품 속성정보" }

{% endtab %}
{% tab order_placed %}

주문이 성공적으로 완료되거나 결제가 확인될 때 트리거합니다.

**이벤트 속성정보**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `order_id` | 문자열 | 예 | 주문의 고유 식별자. |
| `cart_id` | 문자열 | 아니요 | 장바구니 식별자. 사용자의 장바구니 매핑을 위해 장바구니, 결제 및 주문 이벤트 간에 공유됩니다. |
| `total_value` | 플로트 | 예 | 주문의 총 금액. |
| `subtotal_value` | 플로트 | 아니요 | 소계 값(할인 적용 후, 세금/배송비 적용 전). |
| `tax` | 플로트 | 아니요 | 주문에 적용된 총 세금. |
| `shipping` | 플로트 | 아니요 | 총 배송비. |
| `currency` | 문자열 | 예 | 3자리 ISO 4217 코드. |
| `total_discounts` | 플로트 | 아니요 | 주문에 적용된 총 할인 금액. |
| `discounts` | 배열 | 아니요 | 적용된 할인의 상세 목록. 각 할인 오브젝트는 `code`(문자열), `amount`(플로트), `type`(문자열)을 지원합니다. |
| `products` | 배열 | 예 | 주문 내 항목. 제품 속성정보 테이블을 참조하세요. |
| `source` | 문자열 | 예 | 이벤트가 발생한 소스. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어. 인식되는 하위 속성정보: `order_status_url`(문자열). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="주문 완료 이벤트 속성정보" }

**제품 속성정보(`products[]`)**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 문자열 | 예 | 고유 제품 식별자. |
| `product_name` | 문자열 | 예 | 제품 표시 이름. |
| `variant_id` | 문자열 | 예 | 배리언트 식별자. |
| `image_url` | 문자열 | 아니요 | 제품 이미지 URL. |
| `product_url` | 문자열 | 아니요 | 제품 페이지 URL. |
| `quantity` | 정수 | 예 | 주문 내 수량. |
| `price` | 플로트 | 예 | 배리언트 단가. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어(예: `color` 또는 `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="주문 완료 제품 속성정보" }

{% endtab %}
{% tab order_cancelled %}

주문이 취소될 때 트리거합니다.

**이벤트 속성정보**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `order_id` | 문자열 | 예 | 주문의 고유 식별자. |
| `total_value` | 플로트 | 예 | 취소되는 주문의 총 금액. 절대값(`0` 이상)을 전송하세요. Braze가 차감을 처리합니다. |
| `subtotal_value` | 플로트 | 아니요 | 소계 값(할인 적용 후, 세금/배송비 적용 전). |
| `tax` | 플로트 | 아니요 | 주문에 적용된 총 세금. |
| `shipping` | 플로트 | 아니요 | 총 배송비. |
| `currency` | 문자열 | 예 | 3자리 ISO 4217 코드. |
| `total_discounts` | 플로트 | 아니요 | 주문에 적용된 총 할인 금액. |
| `discounts` | 배열 | 아니요 | 적용된 할인의 상세 목록. |
| `cancel_reason` | 문자열 | 예 | 주문이 취소된 사유. |
| `products` | 배열 | 예 | 취소된 주문 내 항목. 제품 속성정보 테이블을 참조하세요. |
| `source` | 문자열 | 예 | 이벤트가 발생한 소스. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어. 인식되는 하위 속성정보: `order_status_url`(문자열). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="주문 취소 이벤트 속성정보" }

**제품 속성정보(`products[]`)**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 문자열 | 예 | 고유 제품 식별자. |
| `product_name` | 문자열 | 예 | 제품 표시 이름. |
| `variant_id` | 문자열 | 예 | 배리언트 식별자. |
| `image_url` | 문자열 | 아니요 | 제품 이미지 URL. |
| `product_url` | 문자열 | 아니요 | 제품 페이지 URL. |
| `quantity` | 정수 | 예 | 주문 내 수량. |
| `price` | 플로트 | 예 | 배리언트 단가. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어(예: `color` 또는 `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="주문 취소 제품 속성정보" }

{% endtab %}
{% tab order_refunded %}

전체 또는 부분 환불이 발생할 때 트리거합니다. 부분 환불의 경우 `total_value`를 원래 주문 총액이 아닌 환불 금액으로만 설정하세요.

**이벤트 속성정보**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `order_id` | 문자열 | 예 | 원래 주문의 고유 식별자. |
| `total_value` | 플로트 | 예 | 환불의 총 금액. 절대값(`0` 이상)을 전송하세요. Braze가 매출 조정을 처리합니다. |
| `currency` | 문자열 | 예 | 3자리 ISO 4217 코드. |
| `total_discounts` | 플로트 | 아니요 | 원래 적용된 총 할인 금액. |
| `discounts` | 배열 | 아니요 | 할인의 상세 목록. |
| `products` | 배열 | 예 | 환불되는 항목. 제품 속성정보 테이블을 참조하세요. |
| `source` | 문자열 | 예 | 이벤트가 발생한 소스. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어. 인식되는 하위 속성정보: `order_status_url`(문자열). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="주문 환불 이벤트 속성정보" }

**제품 속성정보(`products[]`)**

| 속성정보 | 데이터 유형 | 필수 | 설명 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 문자열 | 예 | 고유 제품 식별자. |
| `product_name` | 문자열 | 예 | 제품 표시 이름. |
| `variant_id` | 문자열 | 예 | 배리언트 식별자. |
| `image_url` | 문자열 | 아니요 | 제품 이미지 URL. |
| `product_url` | 문자열 | 아니요 | 제품 페이지 URL. |
| `quantity` | 정수 | 예 | 환불된 수량. |
| `price` | 플로트 | 예 | 배리언트 단가. |
| `metadata` | 오브젝트 | 아니요 | 유연한 키-값 페어(예: `color` 또는 `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="주문 환불 제품 속성정보" }

{% endtab %}
{% endtabs %}

## Android

Android SDK [42.3.0+](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0)는 생성 시 클라이언트 측 유효성 검사와 `Braze.logEcommerceEvent` 호출 시 자동 `snake_case` 직렬화를 제공하는 타입이 지정된 eCommerce 이벤트 클래스를 제공합니다.

| Android 클래스 | 이벤트 이름 | 참고 |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | 제품 필드를 `properties`의 최상위 수준으로 평탄화합니다(`products` 배열 없음). 이 클래스는 카탈로그 트리거를 위한 최상위 `type` 등록정보를 지원하지 않습니다. `type`이 필요한 경우 [`logCustomEvent`](#manual-logging-with-logcustomevent) 또는 REST API를 사용하세요. |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | `action` 등록정보에 `CartUpdatedAction`(`ADD`, `REMOVE`, `REPLACE`)을 사용합니다. |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | 선택 사항인 `cartId`, `totalDiscounts`, `discounts`를 지원합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android SDK eCommerce 이벤트 클래스" }

{% alert important %}
`ecommerce.order_cancelled` 및 `ecommerce.order_refunded`는 타입이 지정된 Android SDK 클래스로 제공되지 않습니다. [`logCustomEvent`](#manual-logging-with-logcustomevent) 또는 REST API를 사용하여 기록하세요.
{% endalert %}

### 공유 빌딩 블록 {#shared-building-blocks}

- `EcommerceProduct`: 장바구니, 결제 및 주문 이벤트의 라인 항목입니다.
  - 필수: `productId`, `productName`, `variantId`, `price`, `quantity`(음수가 아닌 `Long`)
  - 선택 사항: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: 이벤트 수준 또는 제품 수준의 `metadata`입니다. 키는 255자 이하의 비어 있지 않은 문자열이어야 하며 앞에 달러 기호($)가 올 수 없습니다.

### 클라이언트 측 유효성 검사 {#client-side-validation}

잘못된 페이로드는 이벤트 클래스를 생성할 때 `IllegalArgumentException`을 발생시키므로 이벤트가 대기줄에 추가되지 않습니다. 일반적인 규칙:

| 필드 또는 규칙 | 유효성 검사 |
| ------------ | ---------- |
| 문자열 ID 및 이름(`product_id`, `product_name`, `variant_id`, `cart_id`, `checkout_id`, `order_id`, `source`, 선택 사항 URL) | 비어 있지 않으며 최대 255자 |
| `price`, `total_value`, `total_discounts` | `0` 이상이어야 합니다 |
| `currency` | 유효한 ISO 4217 코드(SDK에서 공백 제거 후 대문자로 변환) |
| `products`(장바구니, 결제, 주문 이벤트) | 최소 하나의 `EcommerceProduct` |
| `quantity`(제품당) | 음수가 아닌 정수 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Android eCommerce 이벤트 클라이언트 측 유효성 검사 규칙" }

전송 시 직렬화된 등록정보가 SDK 크기 제한을 초과하면 `logEcommerceEvent`는 오류를 기록하고 이벤트를 전송하지 않습니다.

### 코드 예제 {#code-examples}

{% tabs local %}
{% tab Kotlin %}

{% subtabs local %}
{% subtab product_viewed %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.ProductViewedEvent

val metadata = BrazeProperties()
  .addProperty("sku", "SS-R-101")
  .addProperty("category", "Apparel")

val productViewedEvent = ProductViewedEvent(
  productId = "PROD101",
  productName = "Silk Scarf",
  variantId = "SCARF_RED_SILK",
  price = 150.00,
  currency = "EUR",
  source = "https://braze-fashion.eu",
  imageUrl = "https://braze-fashion.eu/images/scarf_red.jpg",
  productUrl = "https://braze-fashion.eu/products/scarf",
  metadata = metadata,
)

Braze.getInstance(context).logEcommerceEvent(productViewedEvent)
```

{% endsubtab %}
{% subtab cart_updated %}

`CartUpdatedAction`을 사용하여 `action`을 설정합니다:

| 값 | 와이어 값 | 설명 |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | 수량을 늘리거나 라인을 추가합니다. |
| `CartUpdatedAction.REMOVE` | `remove` | 수량을 줄이고, `0`에서 라인을 제거합니다. |
| `CartUpdatedAction.REPLACE` | `replace` | 전체 장바구니를 교체합니다(기본값). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ecommerce.cart_updated의 CartUpdatedAction 값" }

```kotlin
import com.braze.Braze
import com.braze.models.recommended.ecommerce.CartUpdatedAction
import com.braze.models.recommended.ecommerce.CartUpdatedEvent
import com.braze.models.recommended.ecommerce.EcommerceProduct

val product = EcommerceProduct(
  productId = "SKU-RUN-4821",
  productName = "Ultraboost Running Shoe",
  variantId = "UB-BLK-11",
  price = 189.99,
  quantity = 1,
)

val cartUpdatedEvent = CartUpdatedEvent(
  cartId = "cart_abc123",
  currency = "USD",
  source = "android",
  totalValue = 189.99,
  products = listOf(product),
  action = CartUpdatedAction.ADD,
)

Braze.getInstance(context).logEcommerceEvent(cartUpdatedEvent)
```

{% endsubtab %}
{% subtab checkout_started %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.CheckoutStartedEvent
import com.braze.models.recommended.ecommerce.EcommerceProduct

val products = listOf(
  EcommerceProduct(
    productId = "SKU-RUN-4821",
    productName = "Ultraboost Running Shoe",
    variantId = "UB-BLK-11",
    price = 189.99,
    quantity = 1,
  ),
)

val checkoutStartedEvent = CheckoutStartedEvent(
  checkoutId = "chk_88291",
  currency = "USD",
  source = "android",
  totalValue = 234.96,
  products = products,
  cartId = "cart_abc123",
  metadata = BrazeProperties().addProperty("checkout_url", "https://www.example.com/checkout/chk_88291"),
)

Braze.getInstance(context).logEcommerceEvent(checkoutStartedEvent)
```

{% endsubtab %}
{% subtab order_placed %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.EcommerceProduct
import com.braze.models.recommended.ecommerce.OrderPlacedEvent

val products = listOf(
  EcommerceProduct(
    productId = "SKU-RUN-4821",
    productName = "Ultraboost Running Shoe",
    variantId = "UB-BLK-11",
    price = 189.99,
    quantity = 1,
  ),
)

val orderPlacedEvent = OrderPlacedEvent(
  orderId = "ord_77821",
  currency = "USD",
  source = "android",
  totalValue = 224.96,
  products = products,
  cartId = "cart_abc123",
  totalDiscounts = 10.0,
  discounts = listOf(
    mapOf("code" to "SPRING10", "amount" to 10.0, "type" to "percentage"),
  ),
  metadata = BrazeProperties().addProperty("order_status_url", "https://www.example.com/orders/ord_77821/status"),
)

Braze.getInstance(context).logEcommerceEvent(orderPlacedEvent)
```

{% endsubtab %}
{% subtab order_cancelled %}

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_cancelled` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import org.json.JSONArray
import org.json.JSONObject

val properties = BrazeProperties(
  JSONObject()
    .put("order_id", "ord_77821")
    .put("total_value", 224.96)
    .put("currency", "USD")
    .put("cancel_reason", "customer_request")
    .put("source", "android")
    .put(
      "products",
      JSONArray().put(
        JSONObject()
          .put("product_id", "SKU-RUN-4821")
          .put("product_name", "Ultraboost Running Shoe")
          .put("variant_id", "UB-BLK-11")
          .put("quantity", 1)
          .put("price", 189.99),
      ),
    ),
)

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties)
```

{% endsubtab %}
{% subtab order_refunded %}

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_refunded` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import org.json.JSONArray
import org.json.JSONObject

val properties = BrazeProperties(
  JSONObject()
    .put("order_id", "ord_77821")
    .put("total_value", 189.99)
    .put("currency", "USD")
    .put("source", "android")
    .put(
      "products",
      JSONArray().put(
        JSONObject()
          .put("product_id", "SKU-RUN-4821")
          .put("product_name", "Ultraboost Running Shoe")
          .put("variant_id", "UB-BLK-11")
          .put("quantity", 1)
          .put("price", 189.99),
      ),
    ),
)

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties)
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Java %}

{% subtabs local %}
{% subtab product_viewed %}

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import com.braze.models.recommended.ecommerce.ProductViewedEvent;

BrazeProperties metadata = new BrazeProperties()
    .addProperty("sku", "SS-R-101")
    .addProperty("category", "Apparel");

ProductViewedEvent productViewedEvent = new ProductViewedEvent(
    /* productId */ "PROD101",
    /* productName */ "Silk Scarf",
    /* variantId */ "SCARF_RED_SILK",
    /* price */ 150.00,
    /* currency */ "EUR",
    /* source */ "https://braze-fashion.eu",
    /* imageUrl */ "https://braze-fashion.eu/images/scarf_red.jpg",
    /* productUrl */ "https://braze-fashion.eu/products/scarf",
    /* metadata */ metadata
);

Braze.getInstance(context).logEcommerceEvent(productViewedEvent);
```

{% endsubtab %}
{% subtab cart_updated %}

`CartUpdatedAction`을 사용하여 `action`을 설정합니다:

| 값 | 와이어 값 | 설명 |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | 수량을 늘리거나 라인을 추가합니다. |
| `CartUpdatedAction.REMOVE` | `remove` | 수량을 줄이고, `0`에서 라인을 제거합니다. |
| `CartUpdatedAction.REPLACE` | `replace` | 전체 장바구니를 교체합니다(기본값). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ecommerce.cart_updated의 CartUpdatedAction 값" }

```java
import com.braze.Braze;
import com.braze.models.recommended.ecommerce.CartUpdatedAction;
import com.braze.models.recommended.ecommerce.CartUpdatedEvent;
import com.braze.models.recommended.ecommerce.EcommerceProduct;
import java.util.Collections;

EcommerceProduct product = new EcommerceProduct(
    /* productId */ "SKU-RUN-4821",
    /* productName */ "Ultraboost Running Shoe",
    /* variantId */ "UB-BLK-11",
    /* price */ 189.99,
    /* quantity */ 1
);

CartUpdatedEvent cartUpdatedEvent = new CartUpdatedEvent(
    /* cartId */ "cart_abc123",
    /* currency */ "USD",
    /* source */ "android",
    /* totalValue */ 189.99,
    /* products */ Collections.singletonList(product),
    /* metadata */ null,
    /* action */ CartUpdatedAction.ADD
);

Braze.getInstance(context).logEcommerceEvent(cartUpdatedEvent);
```

{% endsubtab %}
{% subtab checkout_started %}

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import com.braze.models.recommended.ecommerce.CheckoutStartedEvent;
import com.braze.models.recommended.ecommerce.EcommerceProduct;
import java.util.Collections;

EcommerceProduct product = new EcommerceProduct(
    /* productId */ "SKU-RUN-4821",
    /* productName */ "Ultraboost Running Shoe",
    /* variantId */ "UB-BLK-11",
    /* price */ 189.99,
    /* quantity */ 1
);

BrazeProperties metadata = new BrazeProperties()
    .addProperty("checkout_url", "https://www.example.com/checkout/chk_88291");

CheckoutStartedEvent checkoutStartedEvent = new CheckoutStartedEvent(
    /* checkoutId */ "chk_88291",
    /* currency */ "USD",
    /* source */ "android",
    /* totalValue */ 234.96,
    /* products */ Collections.singletonList(product),
    /* cartId */ "cart_abc123",
    /* metadata */ metadata
);

Braze.getInstance(context).logEcommerceEvent(checkoutStartedEvent);
```

{% endsubtab %}
{% subtab order_placed %}

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import com.braze.models.recommended.ecommerce.EcommerceProduct;
import com.braze.models.recommended.ecommerce.OrderPlacedEvent;
import java.util.Collections;

EcommerceProduct product = new EcommerceProduct(
    /* productId */ "SKU-RUN-4821",
    /* productName */ "Ultraboost Running Shoe",
    /* variantId */ "UB-BLK-11",
    /* price */ 189.99,
    /* quantity */ 1
);

BrazeProperties metadata = new BrazeProperties()
    .addProperty("order_status_url", "https://www.example.com/orders/ord_77821/status");

OrderPlacedEvent orderPlacedEvent = new OrderPlacedEvent(
    /* orderId */ "ord_77821",
    /* currency */ "USD",
    /* source */ "android",
    /* totalValue */ 224.96,
    /* products */ Collections.singletonList(product),
    /* cartId */ "cart_abc123",
    /* totalDiscounts */ 10.0,
    /* discounts */ null,
    /* metadata */ metadata
);

Braze.getInstance(context).logEcommerceEvent(orderPlacedEvent);
```

{% endsubtab %}
{% subtab order_cancelled %}

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_cancelled` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import org.json.JSONArray;
import org.json.JSONObject;

Braze.getInstance(context).logCustomEvent(
    "ecommerce.order_cancelled",
    new BrazeProperties(new JSONObject()
        .put("order_id", "ord_77821")
        .put("total_value", 224.96)
        .put("currency", "USD")
        .put("cancel_reason", "customer_request")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99)))));
```

{% endsubtab %}
{% subtab order_refunded %}

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_refunded` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import org.json.JSONArray;
import org.json.JSONObject;

Braze.getInstance(context).logCustomEvent(
    "ecommerce.order_refunded",
    new BrazeProperties(new JSONObject()
        .put("order_id", "ord_77821")
        .put("total_value", 189.99)
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99)))));
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## iOS

Swift SDK는 타입이 지정된 eCommerce 이벤트 클래스(`ProductViewedEvent`, `CartUpdatedEvent`, `CheckoutStartedEvent`, `OrderPlacedEvent`)를 제공하며, 이를 빌드하여 `logEcommerceEvent`에 전달합니다. 장바구니, 결제 및 주문 이벤트의 제품에는 `ProductLineItem`을 사용합니다. 각 이니셜라이저는 throwing이므로 `try?`로 래핑하고 생성이 성공한 경우에만 이벤트를 기록합니다.
이 기능은 Swift SDK 버전 `15.0.0` 이상에서 사용할 수 있습니다.

`ecommerce.order_cancelled` 및 `ecommerce.order_refunded`는 타입이 지정된 Swift SDK 클래스로 제공되지 않습니다. `logCustomEvent`를 사용하여 기록하세요.

### 코드 예제

{% tabs local %}
{% tab product_viewed %}

```swift
if let productViewedEvent = try? Braze.Ecommerce.ProductViewedEvent(
    productId: "4111176",
    productName: "Torchie runners",
    variantId: "4111176700",
    imageUrl: "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    productUrl: "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    price: 85,
    currency: "GBP",
    source: "https://braze-apparel.com/",
    metadata: [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ],
    typeIdentifiers: ["price_drop", "back_in_stock"]
) {
    AppDelegate.braze?.logEcommerceEvent(productViewedEvent)
}
```

{% endtab %}
{% tab cart_updated %}

```swift
if let productLine = try? Braze.Ecommerce.ProductLineItem(
    productId: "8266836345064",
    productName: "Classic T-Shirt",
    variantId: "44610569208040",
    imageUrl: "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
    productUrl: "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
    quantity: 2,
    price: 99.99,
    metadata: [
        "sku": "TSH-BLU-M",
        "color": "BLUE",
        "size": "Medium",
        "brand": "Braze"
    ]
), let cartUpdatedEvent = try? Braze.Ecommerce.CartUpdatedEvent(
    cartId: "cart_12345",
    totalValue: 199.98,
    currency: "USD",
    products: [productLine],
    source: "https://braze-apparel.com",
    metadata: [:]
) {
    AppDelegate.braze?.logEcommerceEvent(cartUpdatedEvent)
}
```

{% endtab %}
{% tab checkout_started %}

```swift
if let productLine = try? Braze.Ecommerce.ProductLineItem(
    productId: "632910392",
    productName: "Wireless Headphones",
    variantId: "808950810",
    quantity: 1,
    price: 199.98,
    metadata: [
        "sku": "WH-BLK-PRO",
        "color": "Black",
        "brand": "BrazeAudio"
    ]
), let checkoutStartedEvent = try? Braze.Ecommerce.CheckoutStartedEvent(
    checkoutId: "checkout_abc123",
    cartId: "cart_12345",
    totalValue: 199.98,
    currency: "USD",
    products: [productLine],
    source: "https://braze-audio.com",
    metadata: [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
) {
    AppDelegate.braze?.logEcommerceEvent(checkoutStartedEvent)
}
```

{% endtab %}
{% tab order_placed %}

```swift
if let productLine = try? Braze.Ecommerce.ProductLineItem(
    productId: "632910392",
    productName: "Wireless Headphones",
    variantId: "808950810",
    quantity: 1,
    price: 199.98,
    metadata: [
        "sku": "WH-BLK-PRO",
        "color": "Black",
        "brand": "BrazeAudio"
    ]
), let orderPlacedEvent = try? Braze.Ecommerce.OrderPlacedEvent(
    orderId: "order_67890",
    cartId: "cart_12345",
    totalValue: 189.98,
    currency: "USD",
    totalDiscounts: 10.00,
    discounts: [.structured(code: "SAVE10", amount: 10.00, type: "fixed")],
    products: [productLine],
    source: "https://braze-audio.com",
    metadata: [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
) {
    AppDelegate.braze?.logEcommerceEvent(orderPlacedEvent)
}
```

{% endtab %}
{% tab order_cancelled %}

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_cancelled` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endtab %}
{% tab order_refunded %}

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_refunded` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endtab %}
{% endtabs %}

## Web

Web SDK [6.8.0+](https://github.com/braze-inc/braze-web-sdk)에서는 이벤트 `name`과 `properties`를 사용하여 `logEcommerceEvent`를 호출합니다. 이전 SDK 버전에서는 이벤트 이름과 속성정보 오브젝트를 사용하여 `logCustomEvent`를 호출합니다. `ecommerce.order_cancelled` 및 `ecommerce.order_refunded`는 `logCustomEvent`를 사용합니다.

### 코드 예제

{% tabs local %}
{% tab product_viewed %}

{% sdk_min_versions web:6.8.0 %}

최신 SDK 버전에서는 `logEcommerceEvent()`를 호출합니다:

```javascript
braze.logEcommerceEvent({
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
            "sku": "",
            "color": "ORANGE",
            "size": "6",
            "brand": "Braze"
        }
    }
});
```

이전 SDK 버전에서는 `logCustomEvent()`를 호출합니다:

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endtab %}
{% tab cart_updated %}

{% sdk_min_versions web:6.8.0 %}

최신 SDK 버전에서는 `logEcommerceEvent()`를 호출합니다:

```javascript
braze.logEcommerceEvent({
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "Classic T-Shirt",
                "variant_id": "44610569208040",
                "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
                "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
                "quantity": 2,
                "price": 99.99,
                "metadata": {
                    "sku": "TSH-BLU-M",
                    "color": "BLUE",
                    "size": "Medium",
                    "brand": "Braze"
                }
            }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
    }
});
```

이전 SDK 버전에서는 `logCustomEvent()`를 호출합니다:

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endtab %}
{% tab checkout_started %}

{% sdk_min_versions web:6.8.0 %}

최신 SDK 버전에서는 `logEcommerceEvent()`를 호출합니다:

```javascript
braze.logEcommerceEvent({
    "name": "ecommerce.checkout_started",
    "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "Wireless Headphones",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199.98,
                "metadata": {
                    "sku": "WH-BLK-PRO",
                    "color": "Black",
                    "brand": "BrazeAudio"
                }
            }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
            "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
    }
});
```

이전 SDK 버전에서는 `logCustomEvent()`를 호출합니다:

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endtab %}
{% tab order_placed %}

{% sdk_min_versions web:6.8.0 %}

최신 SDK 버전에서는 `logEcommerceEvent()`를 호출합니다:

```javascript
braze.logEcommerceEvent({
    "name": "ecommerce.order_placed",
    "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
            {
                "code": "SAVE10",
                "amount": 10.00
            }
        ],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "Wireless Headphones",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199.98,
                "metadata": {
                    "sku": "WH-BLK-PRO",
                    "color": "Black",
                    "brand": "BrazeAudio"
                }
            }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
            "order_status_url": "https://braze-audio.com/orders/67890/status",
            "order_number": "ORD-2024-001234",
            "tags": ["electronics", "audio"],
            "referring_site": "https://www.e-referrals.com",
            "payment_gateway_names": ["tap2pay", "dotcash"]
        }
    }
});
```

이전 SDK 버전에서는 `logCustomEvent()`를 호출합니다:

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endtab %}
{% tab order_cancelled %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endtab %}
{% tab order_refunded %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endtab %}
{% endtabs %}

## `logCustomEvent`를 사용한 수동 기록 {#manual-logging-with-logcustomevent}

권장 이벤트를 수동으로 기록하려면 정확한 이벤트 이름(예: `ecommerce.product_viewed`)과 수동으로 구성한 `BrazeProperties` 또는 `JSONObject` 페이로드를 사용하여 `logCustomEvent`를 호출합니다. SDK는 수동 호출에 대해 권장 이벤트 스키마를 유효성 검사하지 않습니다. Braze는 수집 중에 이러한 페이로드를 유효성 검사합니다:

- 유효한 페이로드는 전체 후처리가 적용된 권장 이벤트로 처리됩니다.
- 잘못된 페이로드(필수 필드 누락, 잘못된 유형, 추가 최상위 등록정보)는 수집 후 삭제됩니다. 실패 내역은 워크스페이스 SDK 처리 로그와 [실패 요약 이메일]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures)에 표시됩니다.

앱에서 잘못된 데이터가 전송되기 전에 포착할 수 있도록 가능하면 `logEcommerceEvent`를 사용하세요. 일반적인 `logCustomEvent` 사용법은 [커스텀 이벤트 기록]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)을 참조하세요.