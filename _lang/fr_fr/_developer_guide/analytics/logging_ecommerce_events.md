---
nav_title: Enregistrer des événements eCommerce
article_title: Enregistrer des événements eCommerce via le SDK Android
page_order: 3.25
description: "Découvrez comment enregistrer des événements eCommerce recommandés via le SDK Android de Braze à l'aide de classes d'événements typées et de logEcommerceEvent."
platform:
  - Android
---

# Enregistrer des événements eCommerce {#log-ecommerce-events}

> Découvrez comment enregistrer des [événements eCommerce recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) via le SDK Android de Braze à l'aide de classes d'événements typées et de `Braze.logEcommerceEvent`. Pour les schémas de propriétés d'événements, les fonctionnalités de la plateforme et la validation à l'ingestion, consultez [Événements recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) et [Validation des événements et résolution des problèmes]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting).

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez la méthode native Android correspondante à la place.
{% endalert %}

Le SDK Android [42.3.0+](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0) fournit des classes d'événements eCommerce typées avec validation côté client au moment de la construction et sérialisation automatique en `snake_case` lorsque vous appelez `Braze.logEcommerceEvent`.

| Classe Android | Nom de l'événement | Notes |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | Aplatit les champs du produit au niveau supérieur de `properties` (pas de tableau `products`). Cette classe ne prend pas en charge la propriété `type` de niveau supérieur pour les déclencheurs de catalogue. Si vous avez besoin de `type`, utilisez [`logCustomEvent`](#manual-logging-with-logcustomevent) ou la REST API. |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | Utilisez `CartUpdatedAction` (`ADD`, `REMOVE`, `REPLACE`) pour la propriété `action`. |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | Prend en charge les paramètres facultatifs `cartId`, `totalDiscounts` et `discounts`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Classes d'événements eCommerce du SDK Android" }

{% alert important %}
`ecommerce.order_cancelled` et `ecommerce.order_refunded` ne sont pas disponibles en tant que classes typées du SDK Android. Enregistrez-les avec [`logCustomEvent`](#manual-logging-with-logcustomevent) ou la REST API.
{% endalert %}

## Blocs de construction partagés {#shared-building-blocks}

- `EcommerceProduct` : éléments de ligne pour les événements de panier, de paiement et de commande.
  - Requis : `productId`, `productName`, `variantId`, `price`, `quantity` (`Long` non négatif)
  - Facultatif : `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties` : `metadata` au niveau de l'événement ou du produit. Les clés doivent être des chaînes de caractères non vides d'au maximum 255 caractères sans signe dollar ($) en début de chaîne.

## Validation côté client {#client-side-validation}

Les payloads invalides lèvent une `IllegalArgumentException` lorsque vous construisez la classe d'événement, de sorte que l'événement n'est jamais mis en file d'attente. Règles courantes :

| Champ ou règle | Validation |
| ------------ | ---------- |
| ID et noms de type chaîne (`product_id`, `product_name`, `variant_id`, `cart_id`, `checkout_id`, `order_id`, `source`, URL facultatives) | Non vide, jusqu'à 255 caractères |
| `price`, `total_value`, `total_discounts` | Doit être supérieur ou égal à `0` |
| `currency` | Code ISO 4217 valide (nettoyé et converti en majuscules par le SDK) |
| `products` (événements de panier, paiement, commande) | Au moins un `EcommerceProduct` |
| `quantity` (par produit) | Entier non négatif |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Règles de validation côté client Android pour les événements eCommerce" }

Au moment de l'envoi, si les propriétés sérialisées dépassent la limite de taille du SDK, `logEcommerceEvent` enregistre une erreur et n'envoie pas l'événement.

## Exemples de code {#code-examples}

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

Définissez `action` à l'aide de `CartUpdatedAction` :

| Valeur | Valeur transmise | Description |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Augmenter la quantité ou ajouter une ligne. |
| `CartUpdatedAction.REMOVE` | `remove` | Diminuer la quantité ; supprimer la ligne à `0`. |
| `CartUpdatedAction.REPLACE` | `replace` | Remplacer l'intégralité du panier (par défaut). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Valeurs CartUpdatedAction pour ecommerce.cart_updated" }

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

Braze ne fournit pas de classe SDK typée pour cet événement. Utilisez `logCustomEvent` avec un payload correspondant au schéma de l'événement `ecommerce.order_cancelled`.

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

Braze ne fournit pas de classe SDK typée pour cet événement. Utilisez `logCustomEvent` avec un payload correspondant au schéma de l'événement `ecommerce.order_refunded`.

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

Définissez `action` à l'aide de `CartUpdatedAction` :

| Valeur | Valeur transmise | Description |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Augmenter la quantité ou ajouter une ligne. |
| `CartUpdatedAction.REMOVE` | `remove` | Diminuer la quantité ; supprimer la ligne à `0`. |
| `CartUpdatedAction.REPLACE` | `replace` | Remplacer l'intégralité du panier (par défaut). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Valeurs CartUpdatedAction pour ecommerce.cart_updated" }

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

Braze ne fournit pas de classe SDK typée pour cet événement. Utilisez `logCustomEvent` avec un payload correspondant au schéma de l'événement `ecommerce.order_cancelled`.

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

Braze ne fournit pas de classe SDK typée pour cet événement. Utilisez `logCustomEvent` avec un payload correspondant au schéma de l'événement `ecommerce.order_refunded`.

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

## Enregistrement manuel avec `logCustomEvent` {#manual-logging-with-logcustomevent}

Pour enregistrer manuellement un événement recommandé, appelez `logCustomEvent` avec le nom exact de l'événement (par exemple, `ecommerce.product_viewed`) et un payload `BrazeProperties` ou `JSONObject` construit manuellement. Le SDK ne valide pas les schémas d'événements recommandés pour les appels manuels. Braze valide ces payloads lors de l'ingestion :

- Les payloads valides sont traités comme des événements recommandés avec un post-traitement complet.
- Les payloads invalides (champs requis manquants, types incorrects, propriétés de niveau supérieur supplémentaires) sont rejetés après l'ingestion. Les échecs apparaissent dans le journal de traitement SDK de l'espace de travail et dans l'[e-mail récapitulatif des échecs]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures).

Utilisez `logEcommerceEvent` autant que possible afin de détecter les données invalides avant qu'elles ne quittent l'application. Pour l'utilisation générale de `logCustomEvent`, consultez [Enregistrer des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android).