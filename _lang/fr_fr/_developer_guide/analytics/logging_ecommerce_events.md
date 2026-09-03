---
nav_title: Enregistrer des événements eCommerce
article_title: Enregistrer des événements eCommerce via le SDK Braze
page_order: 3.25
description: "Découvrez comment enregistrer des événements eCommerce recommandés via les SDK Android, Swift et Web de Braze à l'aide de classes d'événements typées et de logEcommerceEvent."
platform:
  - Android
  - Swift
  - Web
---

# Enregistrer des événements eCommerce {#log-ecommerce-events}

> Découvrez comment enregistrer des [événements eCommerce recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) via les SDK Android, Swift et Web de Braze à l'aide de classes d'événements typées et de `logEcommerceEvent`. Pour les schémas de propriétés d'événements, les fonctionnalités de la plateforme et la validation à l'ingestion, consultez [Événements recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events) et [Validation des événements et résolution des problèmes]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting).

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez la méthode native Android ou Swift correspondante à la place.
{% endalert %}

## Schémas d'événements {#event-schemas}

Les six événements eCommerce recommandés partagent un schéma au niveau de la commande sur toutes les plateformes. Utilisez les tableaux de propriétés suivants lorsque vous construisez le payload de chaque événement. Pour le schéma canonique avec le comportement de validation complet et des exemples de REST API, consultez [Événements recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas). Pour les fonctionnalités de la plateforme telles que la segmentation, les modèles Canvas et le reporting, consultez [Comment utiliser les événements eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

{% tabs local %}
{% tab product_viewed %}

Se déclenche lorsqu'un utilisateur consulte une page de détail produit.

**Propriétés de l'événement**

| Nom de la propriété | Type de données | Requis | Description |
| ------------- | --------- | -------- | ----------- |
| `product_id` | Chaîne de caractères | Oui | Identifiant unique du produit (par exemple, unité de gestion des stocks ou ID d'article). |
| `product_name` | Chaîne de caractères | Oui | Nom d'affichage du produit. |
| `variant_id` | Chaîne de caractères | Oui | Identifiant de la variante du produit (par exemple, `shirt_medium_blue`). |
| `image_url` | Chaîne de caractères | Non | URL de l'image du produit. |
| `product_url` | Chaîne de caractères | Non | URL vers la page du produit pour plus de détails. |
| `price` | Float | Oui | Prix unitaire de la variante au moment de la consultation. |
| `currency` | Chaîne de caractères | Oui | Code ISO 4217 à trois lettres (par exemple, `USD` ou `EUR`). |
| `source` | Chaîne de caractères | Oui | Source d'où provient l'événement (par exemple, `web`, `ios` ou `android`). |
| `type` | Tableau de chaînes de caractères | Non | Requis pour utiliser les fonctionnalités de déclenchement par catalogue Braze pour les alertes de retour en stock et de baisse de prix. Valeurs acceptées : `"price_drop"`, `"back_in_stock"`. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles (par exemple, `category` ou `brand`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de l'événement product_viewed" }

{% endtab %}
{% tab cart_updated %}

Se déclenche chaque fois que le contenu du panier d'un utilisateur change. Utilisez le remplacement complet du panier (omettez `action` ou définissez-le sur `replace`) ou les mises à jour incrémentales (`add` ou `remove`).

**Propriétés de l'événement**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `cart_id` | Chaîne de caractères | Oui | Identifiant unique du panier. Partagé entre les événements de panier, de paiement et de commande pour le mappage du panier de l'utilisateur. |
| `action` | Chaîne de caractères | Non | `add` (augmenter la quantité ou ajouter une ligne), `remove` (diminuer la quantité ; la ligne est supprimée à `0`) ou `replace` (remplacement complet du panier, identique à l'omission de `action`). |
| `total_value` | Float | Conditionnel | Requis lorsque `action` est omis ou vaut `replace`. Facultatif lorsque `action` est `add` ou `remove`. |
| `subtotal_value` | Float | Non | Sous-total du panier (après remise, avant taxes/livraison). |
| `tax` | Float | Non | Total des taxes appliquées au panier. |
| `shipping` | Float | Non | Coût total de livraison du panier. |
| `currency` | Chaîne de caractères | Oui | Code ISO 4217 à trois lettres. |
| `products` | Tableau | Oui | Éléments de ligne pour cette mise à jour. Voir le tableau des propriétés produit. |
| `source` | Chaîne de caractères | Oui | Source d'où provient l'événement. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles pour des données supplémentaires au niveau de l'événement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de l'événement cart_updated" }

**Propriétés produit (`products[]`)**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | Chaîne de caractères | Oui | Identifiant unique du produit. |
| `product_name` | Chaîne de caractères | Oui | Nom d'affichage du produit. |
| `variant_id` | Chaîne de caractères | Oui | Identifiant de la variante. |
| `image_url` | Chaîne de caractères | Non | URL de l'image du produit. |
| `product_url` | Chaîne de caractères | Non | URL vers la page du produit. |
| `quantity` | Entier | Oui | Pour un remplacement complet, nombre d'unités dans le panier pour cette ligne. Pour `add` ou `remove`, nombre d'unités à ajouter ou à retirer. |
| `price` | Float | Oui | Prix unitaire de la variante. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés produit de l'événement cart_updated" }

{% endtab %}
{% tab checkout_started %}

Se déclenche lorsque l'utilisateur initie le processus de paiement.

**Propriétés de l'événement**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `checkout_id` | Chaîne de caractères | Oui | Identifiant unique de la session de paiement. |
| `cart_id` | Chaîne de caractères | Non | Identifiant du panier. Partagé entre les événements de panier, de paiement et de commande pour le mappage du panier de l'utilisateur. |
| `total_value` | Float | Oui | Valeur monétaire totale du paiement. |
| `subtotal_value` | Float | Non | Sous-total (après remise, avant taxes/livraison). |
| `tax` | Float | Non | Total des taxes appliquées au paiement. |
| `shipping` | Float | Non | Coût total de livraison. |
| `currency` | Chaîne de caractères | Oui | Code ISO 4217 à trois lettres. |
| `products` | Tableau | Oui | Articles en cours de paiement. Voir le tableau des propriétés produit. |
| `source` | Chaîne de caractères | Oui | Source d'où provient l'événement. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles. Sous-propriété reconnue : `checkout_url` (chaîne de caractères). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de l'événement checkout_started" }

**Propriétés produit (`products[]`)**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | Chaîne de caractères | Oui | Identifiant unique du produit. |
| `product_name` | Chaîne de caractères | Oui | Nom d'affichage du produit. |
| `variant_id` | Chaîne de caractères | Oui | Identifiant de la variante. |
| `image_url` | Chaîne de caractères | Non | URL de l'image du produit. |
| `product_url` | Chaîne de caractères | Non | URL vers la page du produit. |
| `quantity` | Entier | Oui | Nombre d'unités dans le panier. |
| `price` | Float | Oui | Prix unitaire de la variante. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés produit de l'événement checkout_started" }

{% endtab %}
{% tab order_placed %}

Se déclenche lorsqu'une commande est finalisée avec succès ou que le paiement est confirmé.

**Propriétés de l'événement**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `order_id` | Chaîne de caractères | Oui | Identifiant unique de la commande. |
| `cart_id` | Chaîne de caractères | Non | Identifiant du panier. Partagé entre les événements de panier, de paiement et de commande pour le mappage du panier de l'utilisateur. |
| `total_value` | Float | Oui | Valeur monétaire totale de la commande. |
| `subtotal_value` | Float | Non | Sous-total (après remise, avant taxes/livraison). |
| `tax` | Float | Non | Total des taxes appliquées à la commande. |
| `shipping` | Float | Non | Coût total de livraison. |
| `currency` | Chaîne de caractères | Oui | Code ISO 4217 à trois lettres. |
| `total_discounts` | Float | Non | Montant total des remises appliquées à la commande. |
| `discounts` | Tableau | Non | Liste détaillée des remises appliquées. Chaque objet de remise prend en charge `code` (chaîne de caractères), `amount` (float) et `type` (chaîne de caractères). |
| `products` | Tableau | Oui | Articles de la commande. Voir le tableau des propriétés produit. |
| `source` | Chaîne de caractères | Oui | Source d'où provient l'événement. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles. Sous-propriété reconnue : `order_status_url` (chaîne de caractères). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de l'événement order_placed" }

**Propriétés produit (`products[]`)**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | Chaîne de caractères | Oui | Identifiant unique du produit. |
| `product_name` | Chaîne de caractères | Oui | Nom d'affichage du produit. |
| `variant_id` | Chaîne de caractères | Oui | Identifiant de la variante. |
| `image_url` | Chaîne de caractères | Non | URL de l'image du produit. |
| `product_url` | Chaîne de caractères | Non | URL vers la page du produit. |
| `quantity` | Entier | Oui | Nombre d'unités dans la commande. |
| `price` | Float | Oui | Prix unitaire de la variante. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés produit de l'événement order_placed" }

{% endtab %}
{% tab order_cancelled %}

Se déclenche lorsqu'une commande est annulée.

**Propriétés de l'événement**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `order_id` | Chaîne de caractères | Oui | Identifiant unique de la commande. |
| `total_value` | Float | Oui | Valeur monétaire totale de la commande annulée. Envoyez le montant absolu (supérieur ou égal à `0`) ; Braze gère la décrémentation. |
| `subtotal_value` | Float | Non | Sous-total (après remise, avant taxes/livraison). |
| `tax` | Float | Non | Total des taxes appliquées à la commande. |
| `shipping` | Float | Non | Coût total de livraison. |
| `currency` | Chaîne de caractères | Oui | Code ISO 4217 à trois lettres. |
| `total_discounts` | Float | Non | Montant total des remises appliquées à la commande. |
| `discounts` | Tableau | Non | Liste détaillée des remises appliquées. |
| `cancel_reason` | Chaîne de caractères | Oui | Raison de l'annulation de la commande. |
| `products` | Tableau | Oui | Articles de la commande annulée. Voir le tableau des propriétés produit. |
| `source` | Chaîne de caractères | Oui | Source d'où provient l'événement. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles. Sous-propriété reconnue : `order_status_url` (chaîne de caractères). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de l'événement order_cancelled" }

**Propriétés produit (`products[]`)**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | Chaîne de caractères | Oui | Identifiant unique du produit. |
| `product_name` | Chaîne de caractères | Oui | Nom d'affichage du produit. |
| `variant_id` | Chaîne de caractères | Oui | Identifiant de la variante. |
| `image_url` | Chaîne de caractères | Non | URL de l'image du produit. |
| `product_url` | Chaîne de caractères | Non | URL vers la page du produit. |
| `quantity` | Entier | Oui | Nombre d'unités dans la commande. |
| `price` | Float | Oui | Prix unitaire de la variante. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés produit de l'événement order_cancelled" }

{% endtab %}
{% tab order_refunded %}

Se déclenche lorsqu'un remboursement total ou partiel est émis. Pour les remboursements partiels, définissez `total_value` sur le montant remboursé uniquement, et non sur le total initial de la commande.

**Propriétés de l'événement**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `order_id` | Chaîne de caractères | Oui | Identifiant unique de la commande d'origine. |
| `total_value` | Float | Oui | Valeur monétaire totale du remboursement. Envoyez le montant absolu (supérieur ou égal à `0`) ; Braze gère l'ajustement du chiffre d'affaires. |
| `currency` | Chaîne de caractères | Oui | Code ISO 4217 à trois lettres. |
| `total_discounts` | Float | Non | Montant total des remises initialement appliquées. |
| `discounts` | Tableau | Non | Liste détaillée des remises. |
| `products` | Tableau | Oui | Articles remboursés. Voir le tableau des propriétés produit. |
| `source` | Chaîne de caractères | Oui | Source d'où provient l'événement. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles. Sous-propriété reconnue : `order_status_url` (chaîne de caractères). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de l'événement order_refunded" }

**Propriétés produit (`products[]`)**

| Propriété | Type de données | Requis | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | Chaîne de caractères | Oui | Identifiant unique du produit. |
| `product_name` | Chaîne de caractères | Oui | Nom d'affichage du produit. |
| `variant_id` | Chaîne de caractères | Oui | Identifiant de la variante. |
| `image_url` | Chaîne de caractères | Non | URL de l'image du produit. |
| `product_url` | Chaîne de caractères | Non | URL vers la page du produit. |
| `quantity` | Entier | Oui | Nombre d'unités remboursées. |
| `price` | Float | Oui | Prix unitaire de la variante. |
| `metadata` | Objet | Non | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés produit de l'événement order_refunded" }

{% endtab %}
{% endtabs %}

## Android

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

### Blocs de construction partagés {#shared-building-blocks}

- `EcommerceProduct` : éléments de ligne pour les événements de panier, de paiement et de commande.
  - Requis : `productId`, `productName`, `variantId`, `price`, `quantity` (`Long` non négatif)
  - Facultatif : `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties` : `metadata` au niveau de l'événement ou du produit. Les clés doivent être des chaînes de caractères non vides d'au maximum 255 caractères sans signe dollar ($) en début de chaîne.

### Validation côté client {#client-side-validation}

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

### Exemples de code {#code-examples}

{% tabs local %}
{% tab Kotlin %}

{% subtabs local %}
{% subtab product_viewed %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.ProductViewedEvent

val metadata = BrazeProperties()
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

## iOS

Le SDK Swift fournit des classes d'événements eCommerce typées — `ProductViewedEvent`, `CartUpdatedEvent`, `CheckoutStartedEvent` et `OrderPlacedEvent` — que vous construisez et transmettez à `logEcommerceEvent`. Utilisez `ProductLineItem` pour les produits dans les événements de panier, de paiement et de commande. Chaque initialiseur peut lever une exception : encapsulez-le donc dans `try?` et n'enregistrez l'événement que lorsque la construction réussit.
Cette fonctionnalité est disponible à partir de la version `15.0.0` du SDK Swift.

`ecommerce.order_cancelled` et `ecommerce.order_refunded` ne sont pas disponibles en tant que classes typées du SDK Swift. Enregistrez-les avec `logCustomEvent`.

### Exemples de code

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

Braze ne fournit pas de classe SDK typée pour cet événement. Utilisez `logCustomEvent` avec un payload correspondant au schéma de l'événement `ecommerce.order_cancelled`.

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

Braze ne fournit pas de classe SDK typée pour cet événement. Utilisez `logCustomEvent` avec un payload correspondant au schéma de l'événement `ecommerce.order_refunded`.

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

## Web {#web}

Avec le SDK Web [6.8.0+](https://github.com/braze-inc/braze-web-sdk), appelez `logEcommerceEvent` avec un `name` d'événement et des `properties`. Sur les versions antérieures du SDK, appelez `logCustomEvent` avec le nom de l'événement et un objet de propriétés. `ecommerce.order_cancelled` et `ecommerce.order_refunded` utilisent `logCustomEvent`.

### Exemples de code

{% tabs local %}
{% tab product_viewed %}

{% sdk_min_versions web:6.8.0 %}

Sur les versions récentes du SDK, appelez `logEcommerceEvent()` :

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
            "color": "ORANGE",
            "size": "6",
            "brand": "Braze"
        }
    }
});
```

Sur les versions antérieures du SDK, appelez `logCustomEvent()` :

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
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endtab %}
{% tab cart_updated %}

{% sdk_min_versions web:6.8.0 %}

Sur les versions récentes du SDK, appelez `logEcommerceEvent()` :

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

Sur les versions antérieures du SDK, appelez `logCustomEvent()` :

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

Sur les versions récentes du SDK, appelez `logEcommerceEvent()` :

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

Sur les versions antérieures du SDK, appelez `logCustomEvent()` :

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

Sur les versions récentes du SDK, appelez `logEcommerceEvent()` :

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

Sur les versions antérieures du SDK, appelez `logCustomEvent()` :

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

## Enregistrement manuel avec `logCustomEvent` {#manual-logging-with-logcustomevent}

Pour enregistrer manuellement un événement recommandé, appelez `logCustomEvent` avec le nom exact de l'événement (par exemple, `ecommerce.product_viewed`) et un payload `BrazeProperties` ou `JSONObject` construit manuellement. Le SDK ne valide pas les schémas d'événements recommandés pour les appels manuels. Braze valide ces payloads lors de l'ingestion :

- Les payloads valides sont traités comme des événements recommandés avec un post-traitement complet.
- Les payloads invalides (champs requis manquants, types incorrects, propriétés de niveau supérieur supplémentaires) sont rejetés après l'ingestion. Les échecs apparaissent dans le journal de traitement SDK de l'espace de travail et dans l'[e-mail récapitulatif des échecs]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#find-failures).

Utilisez `logEcommerceEvent` autant que possible afin de détecter les données invalides avant qu'elles ne quittent l'application. Pour l'utilisation générale de `logCustomEvent`, consultez [Enregistrer des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android).