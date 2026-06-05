---
nav_title: Registrar eventos de eCommerce
article_title: Registrar eventos de eCommerce pelo SDK Android
page_order: 3.25
description: "Saiba como registrar eventos recomendados de eCommerce pelo SDK Android da Braze usando classes de eventos tipadas e logEcommerceEvent."
platform:
  - Android
---

# Registrar eventos de eCommerce {#log-ecommerce-events}

> Saiba como registrar [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) pelo SDK Android da Braze usando classes de eventos tipadas e `Braze.logEcommerceEvent`. Para esquemas de propriedades de eventos, recursos da plataforma e validação de ingestão, consulte [Eventos recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) e [Validação de eventos e solução de problemas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting).

{% alert note %}
Para wrapper SDKs não listados, use o método nativo Android correspondente.
{% endalert %}

O SDK Android [42.3.0+](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0) fornece classes de eventos de eCommerce tipadas com validação no lado do cliente no momento da construção e serialização automática em `snake_case` quando você chama `Braze.logEcommerceEvent`.

| Classe Android | Nome do evento | Notas |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | Nivela os campos do produto para o nível superior de `properties` (sem array `products`). Esta classe não suporta a propriedade `type` de nível superior para gatilhos de catálogo. Se você precisar de `type`, use [`logCustomEvent`](#manual-logging-with-logcustomevent) ou a REST API. |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | Use `CartUpdatedAction` (`ADD`, `REMOVE`, `REPLACE`) para a propriedade `action`. |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | Suporta `cartId`, `totalDiscounts` e `discounts` opcionais. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Classes de eventos de eCommerce do SDK Android" }

{% alert important %}
`ecommerce.order_cancelled` e `ecommerce.order_refunded` não estão disponíveis como classes tipadas do SDK Android. Registre-os com [`logCustomEvent`](#manual-logging-with-logcustomevent) ou a REST API.
{% endalert %}

## Blocos de construção compartilhados {#shared-building-blocks}

- `EcommerceProduct`: Itens de linha para eventos de carrinho, checkout e pedido.
  - Obrigatórios: `productId`, `productName`, `variantId`, `price`, `quantity` (`Long` não negativo)
  - Opcionais: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: `metadata` no nível do evento ou do produto. As chaves devem ser strings não vazias com no máximo 255 caracteres e sem cifrão ($) no início.

## Validação no lado do cliente {#client-side-validation}

Cargas úteis inválidas lançam `IllegalArgumentException` quando você constrói a classe do evento, então o evento nunca é enfileirado. Regras comuns:

| Campo ou regra | Validação |
| ------------ | ---------- |
| IDs e nomes em string (`product_id`, `product_name`, `variant_id`, `cart_id`, `checkout_id`, `order_id`, `source`, URLs opcionais) | Não vazio, até 255 caracteres |
| `price`, `total_value`, `total_discounts` | Deve ser maior ou igual a `0` |
| `currency` | Código ISO 4217 válido (aparado e convertido para maiúsculas pelo SDK) |
| `products` (eventos de carrinho, checkout e pedido) | Pelo menos um `EcommerceProduct` |
| `quantity` (por produto) | Inteiro não negativo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Regras de validação no lado do cliente do Android para eventos de eCommerce" }

No momento do envio, se as propriedades serializadas excederem o limite de tamanho do SDK, `logEcommerceEvent` registra um erro e não envia o evento.

## Exemplos de código {#code-examples}

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

Defina `action` usando `CartUpdatedAction`:

| Valor | Valor no protocolo | Descrição |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Aumenta a quantidade ou adiciona um item. |
| `CartUpdatedAction.REMOVE` | `remove` | Diminui a quantidade; remove o item quando chega a `0`. |
| `CartUpdatedAction.REPLACE` | `replace` | Substitui o carrinho inteiro (padrão). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Valores de CartUpdatedAction para ecommerce.cart_updated" }

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

A Braze não fornece uma classe tipada do SDK para este evento. Use `logCustomEvent` com uma carga útil que corresponda ao esquema do evento `ecommerce.order_cancelled`.

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

A Braze não fornece uma classe tipada do SDK para este evento. Use `logCustomEvent` com uma carga útil que corresponda ao esquema do evento `ecommerce.order_refunded`.

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

Defina `action` usando `CartUpdatedAction`:

| Valor | Valor no protocolo | Descrição |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Aumenta a quantidade ou adiciona um item. |
| `CartUpdatedAction.REMOVE` | `remove` | Diminui a quantidade; remove o item quando chega a `0`. |
| `CartUpdatedAction.REPLACE` | `replace` | Substitui o carrinho inteiro (padrão). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Valores de CartUpdatedAction para ecommerce.cart_updated" }

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

A Braze não fornece uma classe tipada do SDK para este evento. Use `logCustomEvent` com uma carga útil que corresponda ao esquema do evento `ecommerce.order_cancelled`.

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

A Braze não fornece uma classe tipada do SDK para este evento. Use `logCustomEvent` com uma carga útil que corresponda ao esquema do evento `ecommerce.order_refunded`.

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

## Registro manual com `logCustomEvent` {#manual-logging-with-logcustomevent}

Para registrar manualmente um evento recomendado, chame `logCustomEvent` com o nome exato do evento (por exemplo, `ecommerce.product_viewed`) e uma carga útil `BrazeProperties` ou `JSONObject` construída manualmente. O SDK não valida esquemas de eventos recomendados para chamadas manuais. A Braze valida essas cargas úteis durante a ingestão:

- Cargas úteis válidas são processadas como eventos recomendados com pós-processamento completo.
- Cargas úteis inválidas (campos obrigatórios ausentes, tipos incorretos, propriedades extras no nível superior) são descartadas após a ingestão. As falhas aparecem no registro de processamento do SDK do espaço de trabalho e no [e-mail de resumo de falhas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures).

Use `logEcommerceEvent` sempre que possível para detectar dados inválidos antes que saiam do app. Para o uso geral de `logCustomEvent`, consulte [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android).