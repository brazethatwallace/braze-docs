---
nav_title: Registrar eventos de eCommerce
article_title: Registrar eventos de eCommerce pelo SDK da Braze
page_order: 3.25
description: "Saiba como registrar eventos recomendados de eCommerce pelos SDKs Android, Swift e Web da Braze usando classes de eventos tipadas e logEcommerceEvent."
platform:
  - Android
  - Swift
  - Web
---

# Registrar eventos de eCommerce {#log-ecommerce-events}

> Saiba como registrar [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) pelos SDKs Android, Swift e Web da Braze usando classes de eventos tipadas e `logEcommerceEvent`. Para esquemas de propriedades de eventos, recursos da plataforma e validação de ingestão, consulte [Eventos recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events) e [Validação de eventos e solução de problemas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting).

{% alert note %}
Para wrapper SDKs não listados, use o método nativo Android ou Swift correspondente.
{% endalert %}

## Esquemas de eventos {#event-schemas}

Os seis eventos recomendados de eCommerce compartilham um esquema em nível de pedido em todas as plataformas. Use as tabelas de propriedades a seguir ao construir a carga útil de cada evento. Para o esquema canônico com comportamento completo de validação e exemplos de REST API, consulte [Eventos recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas). Para recursos da plataforma como segmentação, modelos de Canvas e relatórios, consulte [Como usar eventos de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

{% tabs local %}
{% tab product_viewed %}

Dispare quando um usuário visualizar uma página de detalhes do produto.

**Propriedades do evento**

| Nome da propriedade | Tipo de dados | Obrigatória | Descrição |
| ------------- | --------- | -------- | ----------- |
| `product_id` | String | Sim | Identificador único do produto (por exemplo, SKU ou ID do item). |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante do produto (por exemplo, `shirt_medium_blue`). |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto para mais detalhes. |
| `price` | Float | Sim | Preço unitário da variante no momento da visualização. |
| `currency` | String | Sim | Código ISO 4217 de três letras (por exemplo, `USD` ou `EUR`). |
| `source` | String | Sim | Origem do evento (por exemplo, `web`, `ios` ou `android`). |
| `type` | Array de strings | Não | Obrigatória para usar os recursos de gatilho de catálogo da Braze para alertas de volta ao estoque e queda de preço. Valores aceitos: `"price_drop"`, `"back_in_stock"`. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `sku` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento product viewed" }

{% endtab %}
{% tab cart_updated %}

Dispare sempre que o conteúdo do carrinho de um usuário mudar. Use substituição completa do carrinho (omita `action` ou defina como `replace`) ou atualizações incrementais (`add` ou `remove`).

**Propriedades do evento**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `cart_id` | String | Sim | Identificador único do carrinho. Compartilhado entre eventos de carrinho, checkout e pedido para o mapeamento do carrinho do usuário. |
| `action` | String | Não | `add` (incrementar quantidade ou adicionar um item), `remove` (decrementar quantidade; item removido em `0`) ou `replace` (substituição completa do carrinho, igual a omitir `action`). |
| `total_value` | Float | Condicional | Obrigatória quando `action` é omitida ou `replace`. Opcional quando `action` é `add` ou `remove`. |
| `subtotal_value` | Float | Não | Valor do subtotal do carrinho (pós-desconto, pré-imposto/frete). |
| `tax` | Float | Não | Total de impostos aplicados ao carrinho. |
| `shipping` | Float | Não | Custo total de frete do carrinho. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `products` | Array | Sim | Itens de linha desta atualização. Consulte a tabela de propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis para dados adicionais em nível de evento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento cart updated" }

**Propriedades do produto (`products[]`)**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Para substituição completa, unidades no carrinho para este item. Para `add` ou `remove`, quantas unidades adicionar ou remover. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto do evento cart updated" }

{% endtab %}
{% tab checkout_started %}

Dispare quando o usuário iniciar o fluxo de checkout.

**Propriedades do evento**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `checkout_id` | String | Sim | Identificador único da sessão de checkout. |
| `cart_id` | String | Não | Identificador do carrinho. Compartilhado entre eventos de carrinho, checkout e pedido para o mapeamento do carrinho do usuário. |
| `total_value` | Float | Sim | Valor monetário total do checkout. |
| `subtotal_value` | Float | Não | Valor do subtotal (pós-desconto, pré-imposto/frete). |
| `tax` | Float | Não | Total de impostos aplicados ao checkout. |
| `shipping` | Float | Não | Custo total de frete. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `products` | Array | Sim | Itens sendo processados no checkout. Consulte a tabela de propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `checkout_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento checkout started" }

**Propriedades do produto (`products[]`)**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Número de unidades no carrinho. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto do evento checkout started" }

{% endtab %}
{% tab order_placed %}

Dispare quando um pedido for concluído com sucesso ou o pagamento for confirmado.

**Propriedades do evento**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Sim | Identificador único do pedido. |
| `cart_id` | String | Não | Identificador do carrinho. Compartilhado entre eventos de carrinho, checkout e pedido para o mapeamento do carrinho do usuário. |
| `total_value` | Float | Sim | Valor monetário total do pedido. |
| `subtotal_value` | Float | Não | Valor do subtotal (pós-desconto, pré-imposto/frete). |
| `tax` | Float | Não | Total de impostos aplicados ao pedido. |
| `shipping` | Float | Não | Custo total de frete. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `total_discounts` | Float | Não | Valor total de descontos aplicados ao pedido. |
| `discounts` | Array | Não | Lista detalhada de descontos aplicados. Cada objeto de desconto suporta `code` (String), `amount` (Float) e `type` (String). |
| `products` | Array | Sim | Itens do pedido. Consulte a tabela de propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento order placed" }

**Propriedades do produto (`products[]`)**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Número de unidades no pedido. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto do evento order placed" }

{% endtab %}
{% tab order_cancelled %}

Dispare quando um pedido for cancelado.

**Propriedades do evento**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Sim | Identificador único do pedido. |
| `total_value` | Float | Sim | Valor monetário total do pedido sendo cancelado. Envie o valor absoluto (maior ou igual a `0`); a Braze cuida do decremento. |
| `subtotal_value` | Float | Não | Valor do subtotal (pós-desconto, pré-imposto/frete). |
| `tax` | Float | Não | Total de impostos aplicados ao pedido. |
| `shipping` | Float | Não | Custo total de frete. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `total_discounts` | Float | Não | Valor total de descontos aplicados ao pedido. |
| `discounts` | Array | Não | Lista detalhada de descontos aplicados. |
| `cancel_reason` | String | Sim | Motivo do cancelamento do pedido. |
| `products` | Array | Sim | Itens do pedido cancelado. Consulte a tabela de propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento order cancelled" }

**Propriedades do produto (`products[]`)**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Número de unidades no pedido. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto do evento order cancelled" }

{% endtab %}
{% tab order_refunded %}

Dispare quando um reembolso total ou parcial for emitido. Para reembolsos parciais, defina `total_value` apenas com o valor reembolsado, não com o total original do pedido.

**Propriedades do evento**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Sim | Identificador único do pedido original. |
| `total_value` | Float | Sim | Valor monetário total do reembolso. Envie o valor absoluto (maior ou igual a `0`); a Braze cuida do ajuste de receita. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `total_discounts` | Float | Não | Valor total de descontos originalmente aplicados. |
| `discounts` | Array | Não | Lista detalhada de descontos. |
| `products` | Array | Sim | Itens sendo reembolsados. Consulte a tabela de propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento order refunded" }

**Propriedades do produto (`products[]`)**

| Propriedade | Tipo de dados | Obrigatória | Descrição |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Número de unidades reembolsadas. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Objeto | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto do evento order refunded" }

{% endtab %}
{% endtabs %}

## Android

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

### Blocos de construção compartilhados {#shared-building-blocks}

- `EcommerceProduct`: Itens de linha para eventos de carrinho, checkout e pedido.
  - Obrigatórios: `productId`, `productName`, `variantId`, `price`, `quantity` (`Long` não negativo)
  - Opcionais: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: `metadata` no nível do evento ou do produto. As chaves devem ser strings não vazias com no máximo 255 caracteres e sem cifrão ($) no início.

### Validação no lado do cliente {#client-side-validation}

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

### Exemplos de código {#code-examples}

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

## iOS

O SDK Swift fornece classes de eventos de eCommerce tipadas — `ProductViewedEvent`, `CartUpdatedEvent`, `CheckoutStartedEvent` e `OrderPlacedEvent` — que você constrói e passa para `logEcommerceEvent`. Use `ProductLineItem` para os produtos em eventos de carrinho, checkout e pedido. Cada inicializador pode lançar exceção, então envolva-o em `try?` e registre o evento somente quando a construção for bem-sucedida.
Disponível a partir da versão `15.0.0` do SDK Swift.

`ecommerce.order_cancelled` e `ecommerce.order_refunded` não estão disponíveis como classes tipadas do SDK Swift. Registre-os com `logCustomEvent`.

### Exemplos de código

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

A Braze não fornece uma classe tipada do SDK para este evento. Use `logCustomEvent` com uma carga útil que corresponda ao esquema do evento `ecommerce.order_cancelled`.

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

A Braze não fornece uma classe tipada do SDK para este evento. Use `logCustomEvent` com uma carga útil que corresponda ao esquema do evento `ecommerce.order_refunded`.

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

No SDK Web [6.8.0+](https://github.com/braze-inc/braze-web-sdk), chame `logEcommerceEvent` com um `name` de evento e `properties`. Em versões anteriores do SDK, chame `logCustomEvent` com o nome do evento e um objeto de propriedades. `ecommerce.order_cancelled` e `ecommerce.order_refunded` usam `logCustomEvent`.

### Exemplos de código

{% tabs local %}
{% tab product_viewed %}

{% sdk_min_versions web:6.8.0 %}

Em versões mais recentes do SDK, chame `logEcommerceEvent()`:

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

Em versões anteriores do SDK, chame `logCustomEvent()`:

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

Em versões mais recentes do SDK, chame `logEcommerceEvent()`:

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

Em versões anteriores do SDK, chame `logCustomEvent()`:

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

Em versões mais recentes do SDK, chame `logEcommerceEvent()`:

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

Em versões anteriores do SDK, chame `logCustomEvent()`:

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

Em versões mais recentes do SDK, chame `logEcommerceEvent()`:

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

Em versões anteriores do SDK, chame `logCustomEvent()`:

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

## Registro manual com `logCustomEvent` {#manual-logging-with-logcustomevent}

Para registrar manualmente um evento recomendado, chame `logCustomEvent` com o nome exato do evento (por exemplo, `ecommerce.product_viewed`) e uma carga útil `BrazeProperties` ou `JSONObject` construída manualmente. O SDK não valida esquemas de eventos recomendados para chamadas manuais. A Braze valida essas cargas úteis durante a ingestão:

- Cargas úteis válidas são processadas como eventos recomendados com pós-processamento completo.
- Cargas úteis inválidas (campos obrigatórios ausentes, tipos incorretos, propriedades extras no nível superior) são descartadas após a ingestão. As falhas aparecem no registro de processamento do SDK do espaço de trabalho e no [e-mail de resumo de falhas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#find-failures).

Use `logEcommerceEvent` sempre que possível para detectar dados inválidos antes que saiam do app. Para o uso geral de `logCustomEvent`, consulte [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android).