---
nav_title: Événements recommandés
article_title: Événements recommandés
alias: /recommended_events/
page_order: 2
page_type: reference
description: "Cet article de référence décrit les événements recommandés, qui sont des recommandations fournies par Braze pour les événements eCommerce."
---

# Événements recommandés {#recommended-events}

> Les événements recommandés reposent sur un framework qui envoie des événements personnalisés standardisés avec des schémas JSON définis. Lorsque vous envoyez un événement recommandé, Braze le valide par rapport à son schéma lors de l'ingestion et applique un traitement spécialisé, comme le calcul automatique de champs ou la gestion du panier, que les événements personnalisés génériques ne reçoivent pas. Pour certains ensembles d'événements sectoriels, Braze prend également en charge un traitement spécial, comme des déclencheurs basés sur l'action dédiés pour les Campaigns et les Canvas.

## Événements recommandés pour le commerce électronique {#ecommerce-recommended-events}

Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/ecommerce_events) couvrent six étapes du parcours d'achat : `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled` et `order_refunded`. Lorsque vous envoyez ces événements avec succès, Braze valide les données et les rend disponibles pour un ensemble croissant de fonctionnalités de la plateforme.

Ces fonctionnalités incluent des modèles Canvas pour les flux de navigation abandonnée, de panier abandonné, de paiement abandonné et de confirmation de commande ; le reporting eCommerce ; et des champs calculés sur le profil utilisateur pour le _chiffre d'affaires total_, le _nombre total de commandes_ et le _total des remboursements_. Vous pouvez également créer des Segments à l'aide du filtrage par propriétés de produit imbriquées via les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension), personnaliser les messages de panier abandonné avec l'étiquette Liquid {% raw %}`{% shopping_cart %}`{% endraw %}, et alimenter les fonctionnalités BrazeAI<sup>TM</sup> telles que les [événements prédictifs]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), la [prédiction du taux d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) et les [recommandations d'articles]({{site.baseurl}}/user_guide/brazeai/item_recommendations), ainsi que d'autres fonctionnalités.

Comme ces événements suivent un schéma défini, chaque fonctionnalité prise en charge peut lire les données structurées sans mappage de propriétés personnalisé ni configuration spécifique à chaque fonctionnalité de votre côté.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

### Fonctionnement des événements eCommerce {#how-ecommerce-events-work}

Les événements eCommerce sont des événements personnalisés avec des noms et des schémas de propriétés prédéfinis. Vous les envoyez à l'aide du [SDK Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events), de l'[endpoint REST API `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou de l'[ingestion de données cloud (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), et Braze valide chaque événement par rapport à son schéma lors de l'ingestion. Lorsque la validation réussit, Braze applique automatiquement un post-traitement spécifique à ce type d'événement, comme le calcul des champs de chiffre d'affaires et la gestion de l'état du panier sur les profils utilisateur.

{% alert note %}
Les imports CSV ne prennent pas en charge les événements eCommerce. Utilisez le SDK, `/users/track` ou CDI pour envoyer ces événements.
{% endalert %}

Les événements eCommerce fonctionnent partout où les autres événements personnalisés sont utilisés : déclencheurs et filtres pour les événements personnalisés effectués, reporting des événements personnalisés, et plus encore. Cependant, leur validation de schéma débloque des fonctionnalités supplémentaires, notamment :

- Les actions de déclenchement « Passe une commande » dans les Campaigns, Canvas, parcours d'action, déclencheurs de messages in-app et suppression de Content Cards
- Les champs calculés eCommerce sur le profil utilisateur (**Chiffre d'affaires total**, **Nombre total de commandes**, **Total des remboursements**)
- La gestion de l'état du panier pour les flux de panier abandonné
- Des données plus riches pour les fonctionnalités BrazeAI<sup>TM</sup> comme les événements prédictifs, la prédiction du taux d'attrition et les recommandations d'articles

Vous pouvez également référencer les événements eCommerce par leur nom partout où la plateforme prend en charge les événements personnalisés. Par exemple, vous pouvez déclencher une Campaign basée sur une action avec les événements `ecommerce.product_viewed`, créer un Segment filtrant sur les événements `ecommerce.checkout_started`, ou exporter les événements `ecommerce.order_placed` via Currents.

#### Nommage des événements {#event-naming}

Les noms d'événements sont exacts, sensibles à la casse et délimités par des points. Utilisez toujours le format canonique. Si un nom d'événement ne correspond pas exactement à l'un des six noms canoniques, Braze le traite comme un événement personnalisé standard et aucun post-traitement eCommerce n'est effectué.

Vous ne pouvez pas personnaliser ni renommer les événements.

- **Correct :** `ecommerce.order_placed`
- **Incorrect :** `order.placed`, `eCommerce_order_placed`, `Order_Placed`

#### Schémas d'événements {#event-schemas}

Les six événements recommandés pour le commerce électronique correspondent aux étapes du parcours d'achat. Déclenchez chaque événement au moment où l'utilisateur effectue l'action correspondante.

![Diagramme du parcours utilisateur à travers les six événements recommandés pour le commerce électronique : product_viewed, cart_updated, checkout_started, order_placed, order_cancelled et order_refunded.]({% image_buster /assets/img/shopify/event_schemas.png %})

{% alert tip %}
Les exemples suivants montrent le payload de la REST API pour chaque événement.
Pour la journalisation côté client, `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started` et `ecommerce.order_placed` utilisent les API d'événements eCommerce du SDK lorsqu'elles sont disponibles, tandis que `ecommerce.order_cancelled` et `ecommerce.order_refunded` utilisent `logCustomEvent`. Pour des exemples d'implémentation spécifiques à chaque plateforme, consultez [Journaliser les événements eCommerce via le SDK Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).
{% endalert %}

{% tabs %}
{% tab ecommerce.product_viewed %}

Se déclenche lorsqu'un utilisateur consulte une page de détail produit. Cet événement est compatible avec les [notifications de retour en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) et les [notifications de baisse de prix]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) du catalogue Braze.

#### Implémentation côté client {#client-side-implementation}

Utilisez les API d'événements eCommerce du SDK lorsqu'elles sont disponibles. Pour des exemples d'implémentation spécifiques à chaque plateforme, consultez [Journaliser les événements eCommerce via le SDK Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

#### Propriétés d'événement {#event-properties}

| Nom de la propriété | Type de données | Obligatoire | Description |
| -------------- | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product_id`   | String           | Oui      | Identifiant unique du produit (par exemple, SKU ou ID d'article). |
| `product_name` | String           | Oui      | Nom d'affichage du produit. |
| `variant_id`   | String           | Oui      | Identifiant de la variante du produit (par exemple, `shirt_medium_blue`). |
| `image_url`    | String           | Non      | URL de l'image du produit. |
| `product_url`  | String           | Non      | URL vers la page du produit pour plus de détails. |
| `price`        | Float            | Oui      | Prix unitaire de la variante au moment de la consultation. |
| `currency`     | String           | Oui      | Code ISO 4217 à trois lettres (par exemple, `USD` ou `EUR`). |
| `source`       | String           | Oui      | Source d'origine de l'événement (par exemple, `web`, `ios` ou `android`). |
| `type`         | Array of strings | Non      | Obligatoire pour utiliser les fonctionnalités de déclenchement par catalogue de Braze pour les alertes de retour en stock et de baisse de prix. Valeurs acceptées : `"price_drop"`, `"back_in_stock"` |
| `metadata`     | Object           | Non      | Paires clé-valeur flexibles (par exemple, `category` ou `brand`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés d'événement" }

#### Exemple REST API {#rest-api-example}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.product_viewed",
      "time": "2026-04-28T14:22:11Z",
      "properties": {
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
        "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
        "price": 189.99,
        "currency": "USD",
        "source": "web",
        "type": ["price_drop", "back_in_stock"],
        "metadata": {
          "category": "Running Shoes",
          "brand": "Shoe Brand"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.cart_updated %}

Se déclenche chaque fois que le contenu du panier d'un utilisateur change.

#### Implémentation côté client

Utilisez les API d'événements eCommerce du SDK lorsqu'elles sont disponibles. Pour des exemples d'implémentation spécifiques à chaque plateforme, consultez [Journaliser les événements eCommerce via le SDK Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

Vous pouvez envoyer cet événement de deux manières :

- **Remplacement complet du panier :** Omettez `action` ou définissez `action` sur `replace`. Incluez l'ensemble complet des lignes d'articles dans `products` avec des quantités absolues (nombre total d'unités par variante dans le panier). Vous devez inclure `total_value`.
- **Mises à jour incrémentales du panier :** Définissez `action` sur `add` ou `remove`. Incluez uniquement les lignes d'articles qui ont changé. Chaque `quantity` correspond au nombre d'unités à ajouter ou à retirer, et non à la quantité totale dans le panier. Pour `add`, Braze augmente la quantité de la ligne ou ajoute une nouvelle ligne. Pour `remove`, Braze diminue la quantité de la ligne et supprime la ligne lorsque la quantité atteint `0`. `total_value` est optionnel pour `add` et `remove`.

{% alert warning %}
Utilisez soit les mises à jour incrémentales du panier (`add` ou `remove`), soit le remplacement complet (pas d'`action` ou `replace`) pour un panier donné. Mélanger les deux approches pour le même `cart_id` n'est pas recommandé et peut entraîner un état de panier incohérent dans Braze.
{% endalert %}

Pour déclencher l'envoi de messages à partir de cet événement, utilisez le déclencheur **Effectuer un événement de mise à jour du panier** dans Canvas et les Campaigns. Ce déclencheur inclut un traitement spécial pour empêcher le panier de progresser dans l'entonnoir d'achat.

{% alert tip %}
Le panier crée un objet de mappage de paniers sur le profil utilisateur qui alimente l'étiquette Liquid {% raw %}`{% shopping_cart %}`{% endraw %}. Le panier expire après 30 jours sans mise à jour. Si deux profils utilisateur fusionnent, Braze conserve les deux paniers.
{% endalert %}

#### Propriétés d'événement

| Propriété       | Type de données | Obligatoire | Description |
|-----------------|-----------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| `cart_id`       | String    | Oui      | Identifiant unique du panier. Partagé entre les événements de panier, de paiement et de commande pour le mappage du panier de l'utilisateur. |
| `action`        | String    | Non      | `add` (augmenter la quantité ou ajouter une ligne), `remove` (diminuer la quantité ; la ligne est supprimée à `0`) ou `replace` (remplacement complet du panier, identique à l'omission d'`action`). |
| `total_value`   | Float     | Conditionnel | Obligatoire lorsque `action` est omis ou `replace`. Optionnel lorsque `action` est `add` ou `remove`. |
| `subtotal_value`| Float     | Non      | Sous-total du panier (après remise, avant taxes/livraison). |
| `tax`           | Float     | Non      | Total des taxes appliquées au panier. |
| `shipping`      | Float     | Non      | Coût total de livraison du panier. |
| `currency`      | String    | Oui      | Code ISO 4217 à trois lettres. |
| `products`      | Array     | Oui      | Lignes d'articles pour cette mise à jour. Pour le remplacement complet (pas d'`action` ou `replace`), incluez le panier complet avec les quantités absolues. Pour `add` ou `remove`, incluez uniquement les lignes modifiées ; voir les propriétés de produit. |
| `source`        | String    | Oui      | Source d'origine de l'événement. |
| `metadata`      | Object    | Non      | Paires clé-valeur flexibles pour des données supplémentaires au niveau de l'événement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés d'événement" }

#### Propriétés de produit (`products[]`) {#product-properties-products}

| Propriété       | Type de données | Obligatoire | Description |
|-----------------|-----------|----------|-------------------------------------------------|
| `product_id`    | String    | Oui      | Identifiant unique du produit. |
| `product_name`  | String    | Oui      | Nom d'affichage du produit. |
| `variant_id`    | String    | Oui      | Identifiant de la variante. |
| `image_url`     | String    | Non      | URL de l'image du produit. |
| `product_url`   | String    | Non      | URL vers la page du produit. |
| `quantity`      | Integer   | Oui      | Pour le remplacement complet (pas d'`action` ou `replace`), nombre d'unités dans le panier pour cette ligne. Pour `add` ou `remove`, nombre d'unités à ajouter ou à retirer. |
| `price`         | Float     | Oui      | Prix unitaire de la variante. |
| `metadata`      | Object    | Non      | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de produit (products[])" }

{% comment %}

{% subtabs local %}
{% subtab Web %}

##### `add`

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "add",
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-RUN-4821",
      product_name: "Ultraboost Running Shoe",
      variant_id: "UB-BLK-11",
      quantity: 1,
      price: 189.99,
    },
  ],
});
```
##### `remove`

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "remove",
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-SOC-1102",
      product_name: "Performance Running Socks",
      variant_id: "SOC-WHT-L",
      quantity: 1,
      price: 14.99,
    },
  ],
});
```

##### `replace`

`replace` (or omit `action`) sends the full cart. `total_value` is required.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "replace",
  total_value: 234.96,
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-RUN-4821",
      product_name: "Ultraboost Running Shoe",
      variant_id: "UB-BLK-11",
      image_url: "https://cdn.example.com/shoes/ub-blk-11.jpg",
      product_url: "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
      quantity: 1,
      price: 189.99,
    },
    {
      product_id: "SKU-SOC-1102",
      product_name: "Performance Running Socks",
      variant_id: "SOC-WHT-L",
      image_url: "https://cdn.example.com/socks/soc-wht-l.jpg",
      product_url: "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
      quantity: 2,
      price: 14.99,
    },
  ],
});
```

{% endsubtab %}
{% subtab Android %}

##### Add

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

```text
Kotlin

// add — units to add
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "add")
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
  ),
)

JavaScript

// add — units to add
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "add")
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

##### Remove

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

```text
Kotlin

// remove — units to remove
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "remove")
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray().put(
          JSONObject()
            .put("product_id", "SKU-SOC-1102")
            .put("product_name", "Performance Running Socks")
            .put("variant_id", "SOC-WHT-L")
            .put("quantity", 1)
            .put("price", 14.99),
        ),
      ),
  ),
)

JavaScript

// remove — units to remove
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "remove")
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-SOC-1102")
                .put("product_name", "Performance Running Socks")
                .put("variant_id", "SOC-WHT-L")
                .put("quantity", 1)
                .put("price", 14.99)))));
```

##### Replace

`replace` (or omit `action`) sends the full cart. `total_value` is required.

```text
Kotlin

// replace — full cart; total_value required
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "replace")
      .put("total_value", 234.96)
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray()
          .put(
            JSONObject()
              .put("product_id", "SKU-RUN-4821")
              .put("product_name", "Ultraboost Running Shoe")
              .put("variant_id", "UB-BLK-11")
              .put("quantity", 1)
              .put("price", 189.99),
          )
          .put(
            JSONObject()
              .put("product_id", "SKU-SOC-1102")
              .put("product_name", "Performance Running Socks")
              .put("variant_id", "SOC-WHT-L")
              .put("quantity", 2)
              .put("price", 14.99),
          ),
      ),
  ),
)

JavaScript

// replace — full cart; total_value required
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "replace")
        .put("total_value", 234.96)
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99))
            .put(new JSONObject()
                .put("product_id", "SKU-SOC-1102")
                .put("product_name", "Performance Running Socks")
                .put("variant_id", "SOC-WHT-L")
                .put("quantity", 2)
                .put("price", 14.99)))));
```

{% endsubtab %}
{% subtab Swift %}

##### Add

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

```text
Swift

// add — units to add
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "add",
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "quantity": 1,
        "price": 189.99,
      ],
    ],
  ]
)

Objective-C

// add — units to add
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"add",
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[@{
    @"product_id": @"SKU-RUN-4821",
    @"product_name": @"Ultraboost Running Shoe",
    @"variant_id": @"UB-BLK-11",
    @"quantity": @1,
    @"price": @189.99,
  }],
}];
```

##### Remove

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

```text
Swift

// remove — units to remove
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "remove",
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-SOC-1102",
        "product_name": "Performance Running Socks",
        "variant_id": "SOC-WHT-L",
        "quantity": 1,
        "price": 14.99,
      ],
    ],
  ]
)

Objective-C

// remove — units to remove
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"remove",
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[@{
    @"product_id": @"SKU-SOC-1102",
    @"product_name": @"Performance Running Socks",
    @"variant_id": @"SOC-WHT-L",
    @"quantity": @1,
    @"price": @14.99,
  }],
}];
```

##### Replace

`replace` (or omit `action`) sends the full cart. `total_value` is required.

```text
Swift

// replace — full cart; total_value required
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "replace",
    "total_value": 234.96,
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "quantity": 1,
        "price": 189.99,
      ],
      [
        "product_id": "SKU-SOC-1102",
        "product_name": "Performance Running Socks",
        "variant_id": "SOC-WHT-L",
        "quantity": 2,
        "price": 14.99,
      ],
    ],
  ]
)

Objective-C

// replace — full cart; total_value required
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"replace",
  @"total_value": @234.96,
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[
    @{
      @"product_id": @"SKU-RUN-4821",
      @"product_name": @"Ultraboost Running Shoe",
      @"variant_id": @"UB-BLK-11",
      @"quantity": @1,
      @"price": @189.99,
    },
    @{
      @"product_id": @"SKU-SOC-1102",
      @"product_name": @"Performance Running Socks",
      @"variant_id": @"SOC-WHT-L",
      @"quantity": @2,
      @"price": @14.99,
    },
  ],
}];
```

{% endsubtab %}
{% subtab REST API %}

##### `add`

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:25:33Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "add",
        "currency": "USD",
        "source": "web",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99
          }
        ]
      }
    }
  ]
}
```

##### `remove`

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:26:10Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "remove",
        "currency": "USD",
        "source": "web",
        "products": [
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "quantity": 1,
            "price": 14.99
          }
        ]
      }
    }
  ]
}
```

##### `replace`

`replace` (or omit `action`) sends the full cart. `total_value` is required.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:27:00Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "replace",
        "total_value": 234.96,
        "subtotal_value": 219.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "cart_source": "product_page_atc_button"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endcomment %}

{% endtab %}
{% tab ecommerce.checkout_started %}

Se déclenche lorsque l'utilisateur initie le processus de paiement (par exemple, sélectionne « Paiement » ou arrive sur la page de paiement).

#### Implémentation côté client

Utilisez les API d'événements eCommerce du SDK lorsqu'elles sont disponibles. Pour des exemples d'implémentation spécifiques à chaque plateforme, consultez [Journaliser les événements eCommerce via le SDK Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

#### Propriétés d'événement

| Propriété      | Type    | Obligatoire | Description |
|----------------|---------|----------|------------------------------------------------------------------------------------------------------------------|
| checkout_id    | String  | Oui      | Identifiant unique de la session de paiement. |
| cart_id        | String  | Non      | Identifiant du panier. Partagé entre les événements de panier, de paiement et de commande pour le mappage du panier de l'utilisateur. |
| total_value    | Float   | Oui      | Valeur monétaire totale du paiement. |
| subtotal_value | Float   | Non      | Sous-total (après remise, avant taxes/livraison). |
| tax            | Float   | Non      | Total des taxes appliquées au paiement. |
| shipping       | Float   | Non      | Coût total de livraison. |
| currency       | String  | Oui      | Code ISO 4217 à trois lettres. |
| products       | Array   | Oui      | Articles en cours de paiement. Voir le sous-tableau des propriétés de produit. |
| source         | String  | Oui      | Source d'origine de l'événement. |
| metadata       | Object  | Non      | Paires clé-valeur flexibles. Sous-propriété reconnue : `checkout_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés d'événement" }

#### Propriétés de produit (`products[]`)

| Propriété      | Type de données | Obligatoire | Description |
|----------------|-----------|----------|----------------------------------------------------------|
| `product_id`   | String    | Oui      | Identifiant unique du produit. |
| `product_name` | String    | Oui      | Nom d'affichage du produit. |
| `variant_id`   | String    | Oui      | Identifiant de la variante. |
| `image_url`    | String    | Non      | URL de l'image du produit. |
| `product_url`  | String    | Non      | URL vers la page du produit. |
| `quantity`     | Integer   | Oui      | Nombre d'unités dans le panier. |
| `price`        | Float     | Oui      | Prix unitaire de la variante. |
| `metadata`     | Object    | Non      | Paires clé-valeur flexibles (par exemple, couleur, taille). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de produit (products[])" }

#### Exemple REST API

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.checkout_started",
      "time": "2026-04-28T14:30:05Z",
      "properties": {
        "checkout_id": "chk_88291",
        "cart_id": "cart_abc123",
        "total_value": 234.96,
        "subtotal_value": 219.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "checkout_url": "https://www.example.com/checkout/chk_88291",
          "checkout_type": "express"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_placed %}

Se déclenche lorsqu'une commande est finalisée avec succès ou que le paiement est confirmé.

#### Implémentation côté client

Utilisez les API d'événements eCommerce du SDK lorsqu'elles sont disponibles. Pour des exemples d'implémentation spécifiques à chaque plateforme, consultez [Journaliser les événements eCommerce via le SDK Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Cet événement est le principal moteur de chiffre d'affaires. Il incrémente `total_revenue` de la valeur de `total_value` et incrémente `total_orders` de 1 sur le profil utilisateur.
{% endalert %}

#### Propriétés d'événement

| Propriété       | Type de données | Obligatoire | Description |
|-----------------|-----------|----------|-----------------------------------------------------------------------------------------------|
| `order_id`      | String    | Oui      | Identifiant unique de la commande. |
| `cart_id`       | String    | Non      | Identifiant du panier. Partagé entre les événements de panier, de paiement et de commande pour le mappage du panier de l'utilisateur. |
| `total_value`   | Float     | Oui      | Valeur monétaire totale de la commande. |
| `subtotal_value`| Float     | Non      | Sous-total (après remise, avant taxes/livraison). |
| `tax`           | Float     | Non      | Total des taxes appliquées à la commande. |
| `shipping`      | Float     | Non      | Coût total de livraison. |
| `currency`      | String    | Oui      | Code ISO 4217 à trois lettres. |
| `total_discounts`| Float    | Non      | Montant total des remises appliquées à la commande. |
| `discounts`     | Array     | Non      | Liste détaillée des remises appliquées. |
| `products`      | Array     | Oui      | Articles de la commande. Voir le sous-tableau des propriétés de produit. |
| `source`        | String    | Oui      | Source d'origine de l'événement. |
| `metadata`      | Object    | Non      | Paires clé-valeur flexibles. Sous-propriété reconnue : `order_status_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés d'événement" }

#### Propriétés de produit (`products[]`)

| Propriété       | Type de données | Obligatoire | Description |
|-----------------|-----------|----------|---------------------------------------------|
| `product_id`    | String    | Oui      | Identifiant unique du produit. |
| `product_name`  | String    | Oui      | Nom d'affichage du produit. |
| `variant_id`    | String    | Oui      | Identifiant de la variante. |
| `image_url`     | String    | Non      | URL de l'image du produit. |
| `product_url`   | String    | Non      | URL vers la page du produit. |
| `quantity`      | Integer   | Oui      | Nombre d'unités dans le panier. |
| `price`         | Float     | Oui      | Prix unitaire de la variante. |
| `metadata`      | Object    | Non      | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de produit (products[])" }

#### Exemple REST API

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_placed",
      "time": "2026-04-28T14:35:42Z",
      "properties": {
        "order_id": "ord_77821",
        "cart_id": "cart_abc123",
        "total_value": 224.96,
        "subtotal_value": 209.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "total_discounts": 10.0,
        "discounts": [
          {
            "code": "SPRING10",
            "amount": 10.0,
            "type": "percentage"
          }
        ],
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_cancelled %}

Se déclenche lorsqu'une commande est annulée.

#### Implémentation côté client

Utilisez `logCustomEvent`. Pour des exemples d'implémentation spécifiques à chaque plateforme, consultez [Journaliser les événements eCommerce via le SDK Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Cet événement décrémente `total_orders` de 1 sur le profil utilisateur. Il n'affecte pas `total_revenue` ; utilisez `order_refunded` pour ajuster le chiffre d'affaires.
{% endalert %}

#### Propriétés d'événement

| Propriété        | Type    | Obligatoire | Description |
|------------------|---------|----------|--------------------------------------------------------------------------------------------------|
| `order_id`       | String  | Oui      | Identifiant unique de la commande. |
| `total_value`    | Float   | Oui      | Valeur monétaire totale de la commande annulée. Doit être ≥ 0 — envoyez le montant absolu ; Braze gère la décrémentation. |
| `subtotal_value` | Float   | Non      | Sous-total (après remise, avant taxes/livraison). |
| `tax`            | Float   | Non      | Total des taxes appliquées à la commande. |
| `shipping`       | Float   | Non      | Coût total de livraison. |
| `currency`       | String  | Oui      | Code ISO 4217 à trois lettres. |
| `total_discounts`| Float   | Non      | Montant total des remises appliquées à la commande. |
| `discounts`      | Array   | Non      | Liste détaillée des remises appliquées. |
| `cancel_reason`  | String  | Oui      | Raison de l'annulation de la commande. |
| `products`       | Array   | Oui      | Articles de la commande annulée. Voir le sous-tableau des propriétés de produit. |
| `source`         | String  | Oui      | Source d'origine de l'événement. |
| `metadata`       | Object  | Non      | Paires clé-valeur flexibles. Sous-propriété reconnue : `order_status_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés d'événement" }

#### Propriétés de produit (`products[]`)

| Propriété      | Type de données | Obligatoire | Description |
|----------------|-----------|----------|-----------------------------------------------|
| `product_id`   | String    | Oui      | Identifiant unique du produit. |
| `product_name` | String    | Oui      | Nom d'affichage du produit. |
| `variant_id`   | String    | Oui      | Identifiant de la variante. |
| `image_url`    | String    | Non      | URL de l'image du produit. |
| `product_url`  | String    | Non      | URL vers la page du produit. |
| `quantity`     | Integer   | Oui      | Nombre d'unités dans le panier. |
| `price`        | Float     | Oui      | Prix unitaire de la variante. |
| `metadata`     | Object    | Non      | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de produit (products[])" }

#### Exemple REST API

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_cancelled",
      "time": "2026-04-28T16:10:00Z",
      "properties": {
        "order_id": "ord_77821",
        "total_value": 224.96,
        "subtotal_value": 209.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "total_discounts": 10.0,
        "cancel_reason": "customer_request",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_refunded %}

Se déclenche lorsqu'un remboursement total ou partiel est émis.

#### Implémentation côté client

Utilisez `logCustomEvent`. Pour des exemples d'implémentation spécifiques à chaque plateforme, consultez [Journaliser les événements eCommerce via le SDK Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Cet événement décrémente `total_revenue` de la valeur de `total_value` et incrémente `total_refunds` sur le profil utilisateur. Pour les remboursements partiels, définissez `total_value` sur le montant remboursé uniquement, et non sur le total de la commande d'origine.
{% endalert %}

#### Propriétés d'événement

| Propriété         | Type de données | Obligatoire | Description |
|-------------------|-----------|----------|------------------------------------------------------------------------------------------------------|
| `order_id`        | String    | Oui      | Identifiant unique de la commande d'origine. |
| `total_value`     | Float     | Oui      | Valeur monétaire totale du remboursement. Doit être ≥ 0 — envoyez le montant absolu ; Braze gère l'incrémentation de total_refunds. |
| `currency`        | String    | Oui      | Code ISO 4217 à trois lettres. |
| `total_discounts` | Float     | Non      | Montant total des remises appliquées à l'origine. |
| `discounts`       | Array     | Non      | Liste détaillée des remises. |
| `products`        | Array     | Oui      | Articles remboursés. Voir le sous-tableau des propriétés de produit. |
| `source`          | String    | Oui      | Source d'origine de l'événement. |
| `metadata`        | Object    | Non      | Paires clé-valeur flexibles. Sous-propriété reconnue : `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés d'événement" }

#### Propriétés de produit (`products[]`)

| Propriété       | Type de données | Obligatoire | Description |
|-----------------|-----------|----------|-------------------------------------------------------|
| `product_id`    | String    | Oui      | Identifiant unique du produit. |
| `product_name`  | String    | Oui      | Nom d'affichage du produit. |
| `variant_id`    | String    | Oui      | Identifiant de la variante. |
| `image_url`     | String    | Non      | URL de l'image du produit. |
| `product_url`   | String    | Non      | URL vers la page du produit. |
| `quantity`      | Integer   | Oui      | Nombre d'unités dans le panier. |
| `price`         | Float     | Oui      | Prix unitaire de la variante. |
| `metadata`      | Object    | Non      | Paires clé-valeur flexibles (par exemple, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriétés de produit (products[])" }

#### Exemples REST API {#rest-api-examples}

{% subtabs %}
{% subtab Remboursement total %}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_refunded",
      "time": "2026-04-29T10:05:00Z",
      "properties": {
        "order_id": "ord_77821",
        "total_value": 189.99,
        "currency": "USD",
        "total_discounts": 0,
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11",
              "refund_reason": "size_mismatch"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```
{% endsubtab %}
{% subtab Remboursement partiel %}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_refunded",
      "time": "2026-05-02T11:08:30Z",
      "properties": {
        "order_id": "ORD-20260428-7891",
        "total_value": 29.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "refund_method": "store_credit",
          "initiated_by": "customer"
        }
      }
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Post-traitement des événements eCommerce {#ecommerce-event-post-processing}

Lorsque vous envoyez un événement eCommerce, Braze le valide par rapport au schéma attendu pour ce nom d'événement.

Le tableau suivant résume ce que Braze fait automatiquement pour chaque événement lorsque la validation réussit. Pour savoir ce qui se passe lorsque la validation échoue, consultez [Validation et résolution des problèmes des événements](#event-validation-and-troubleshooting).

| Événement | Ce que Braze fait automatiquement |
|------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `ecommerce.order_placed`     | Incrémente le **chiffre d'affaires total** de `total_value` et le **nombre total de commandes** de 1 sur le profil utilisateur. |
| `ecommerce.order_cancelled`  | Décrémente le **nombre total de commandes** de 1. |
| `ecommerce.order_refunded`   | Décrémente le **chiffre d'affaires total** de `total_value` et incrémente le **total des remboursements**. |
| `ecommerce.cart_updated`     | Crée ou met à jour l'objet de mappage de paniers sur le profil utilisateur (payloads de panier complets, ou mises à jour incrémentales du panier avec `action` optionnel : `add`, `remove` ou `replace`). Le panier expire après 30 jours sans mise à jour. |
| `ecommerce.product_viewed`   | Aucune modification du profil utilisateur. Disponible pour la segmentation, le déclenchement et les fonctionnalités BrazeAI<sup>TM</sup> (comme les recommandations d'articles). |
| `ecommerce.checkout_started` | Aucune modification du profil utilisateur. Disponible pour la segmentation et le déclenchement (par exemple, les flux de paiement abandonné). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Post-traitement des événements eCommerce" }

{% alert important %}
Les valeurs dans des devises autres que l'USD sont automatiquement converties en USD au taux de change du jour où l'événement est signalé. Si vous effectuez déjà vos rapports en USD, codez en dur `USD` comme devise pour éviter toute conversion involontaire.
{% endalert %}

## Détails de mise en œuvre {#implementation-details}

### Points de données et facturation {#data-points-and-billing}

Les événements eCommerce ne consomment pas de [points de données]({{site.baseurl}}/user_guide/data/infrastructure/data_points). Vous pouvez les enregistrer sans aucun impact sur votre utilisation de points de données.

### Limite de taille des événements {#event-size-limit}

Les propriétés d'événement envoyées à `/users/track` sont plafonnées à 102 400 octets (100 Ko) par événement. Pour les messages déclenchés de Campaign et de Canvas, les `trigger_properties` envoyées à [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) et [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) ont une limite par défaut plus stricte de 51 200 octets (50 Ko).

En bonne pratique, n'envoyez que les informations produit nécessaires pour déclencher, personnaliser ou attribuer l'événement. Stockez les détails produit plus riches — tels que les descriptions, les listes complètes de variantes, l'inventaire ou les images alternatives — dans les catalogues Braze. Référencez ces détails par `product_id` ou `variant_id` lors de l'envoi de messages. Utilisez l'objet `metadata` de manière sélective pour le contexte spécifique à la commande ou au produit que la communication utilisera.

### Gestion des devises {#currency-handling}

Braze convertit automatiquement les valeurs dans des devises autres que l'USD en USD en utilisant le taux de change à la date à laquelle l'événement est rapporté. Cette valeur convertie est celle qui apparaît dans les indicateurs de chiffre d'affaires.

{% alert tip %}
Si vous opérez uniquement en USD, codez en dur `"currency": "USD"` dans chaque événement pour éviter toute conversion inutile.
{% endalert %}

### Champ source {#source-field}

La propriété source est une chaîne de caractères obligatoire qui identifie l'origine de l'événement. Par exemple, `shopify`, `in-store POS` ou `custom_api`. Cela vous aide à distinguer les sources d'intégration lors de l'analyse des données dans les exports Currents ou du débogage des problèmes de validation.

### Flexibilité des métadonnées {#metadata-flexibility}

Les objets de métadonnées au niveau de l'événement et au niveau du produit acceptent des paires clé-valeur arbitraires, ce qui vous permet d'ajouter des dimensions personnalisées sans modifier le schéma principal. Parmi les exemples courants : `order_status_url`, `gift_wrapped`, `loyalty_points_earned` ou `warehouse_id`. Ces propriétés sont disponibles dans la personnalisation Liquid, les exports Currents et la segmentation via les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension).

{% alert important %}
Les événements recommandés utilisent un schéma strict. Par conséquent, l'ajout de propriétés personnalisées au niveau supérieur des propriétés échouera à la validation. Placez toutes les propriétés personnalisées dans l'objet `metadata` au niveau de l'événement ou dans l'objet `metadata` au niveau du produit à l'intérieur de `products[]`. Celles-ci restent disponibles pour Liquid, Currents et la segmentation, tout comme les champs de niveau supérieur.
{% endalert %}

## Validation et résolution des problèmes des événements {#event-validation-and-troubleshooting}

Lorsque vous envoyez un événement eCommerce recommandé via `/users/track` ou l'un des SDK Braze, Braze valide le payload par rapport au schéma JSON de l'événement lors du traitement de l'événement recommandé. La validation s'exécute automatiquement sur chaque événement dont le nom correspond exactement à un événement recommandé (par exemple, `ecommerce.order_placed` ou `ecommerce.cart_updated`).

### Ce que nous validons {#what-we-validate}

Pour chaque événement dont le nom correspond à un événement eCommerce recommandé, Braze vérifie :

| Vérification                     | Exemple                                                                                                                      |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Nom de l'événement               | Doit être exact. Par exemple, `ecommerce.cart_updated` est correct — pas `ecommerce.Cart_Updated`, `cartupdated` ou `cart_updated`. |
| Propriétés requises présentes    | `order_placed` nécessite `order_id`, `total_value`, `currency`, `products` et `source`.                                   |
| Types de données corrects        | `total_value` doit être un nombre ; `currency` doit être une chaîne de caractères ; `products` doit être un tableau.                                   |
| Pas de propriétés supplémentaires au niveau supérieur | Les champs personnalisés sous properties provoquent un échec. Utilisez l'objet `metadata` à la place.                                         |
| Contraintes de valeurs           | Les champs monétaires doivent être ≥ `0`. `currency` doit être une chaîne ISO 4217 valide.                                                  |
| Champs par produit               | Chaque élément dans `products[]` doit inclure `product_id`, `product_name`, `variant_id`, `quantity` et `price`.                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ce que nous validons" }

### Pourquoi nous validons {#why-we-validate}

Les événements eCommerce alimentent des fonctionnalités qui dépendent de données cohérentes et prévisibles, notamment le suivi du chiffre d'affaires, l'étiquette Liquid {% raw %}`{% shopping_cart %}`{% endraw %}, le déclencheur de panier abandonné et le reporting. Lorsque les payloads divergent du schéma, ces fonctionnalités produisent des inexactitudes silencieuses (totaux de chiffre d'affaires erronés, paniers manquants, déclencheurs défaillants). La validation impose le contrat en amont afin que les fonctionnalités en aval se comportent de manière prévisible.

### Lorsque la validation réussit {#when-validation-passes}

L'événement est traité comme un événement eCommerce recommandé avec tout le post-traitement associé. Consultez [Événements eCommerce recommandés](#event-schemas) pour la liste complète des comportements déclenchés par chaque type d'événement.

#### Vérifier un événement réussi {#verify-a-successful-event}

Après avoir envoyé un événement, vous pouvez confirmer qu'il a été accepté et traité correctement en utilisant l'une des méthodes suivantes :

- [Journal des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) : ouvrez le profil de l'utilisateur dans le tableau de bord et consultez son activité. Les événements recommandés apparaissent avec l'intégralité de leur payload de propriétés, ce qui vous permet de confirmer que l'événement a bien été reçu et que les valeurs correspondent à ce que vous avez envoyé.
- [Rapport d'événements personnalisés]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) : accédez à **Analytics** > **Custom Events Report** pour voir les comptages agrégés de chaque événement recommandé au fil du temps. Cela est utile pour confirmer que le trafic de production circule comme prévu lorsque votre intégration est en production.
- [Utilisateurs test]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups?utm_source=operator_user&utm_medium=dashboard#adding-test-users) : marquez un utilisateur dans votre espace de travail de développement comme utilisateur test, puis déclenchez des événements depuis votre intégration pour cet utilisateur. Les utilisateurs test sont signalés dans le tableau de bord, ce qui facilite l'isolation et l'inspection du comportement de bout en bout.

### Lorsque la validation échoue {#when-validation-fails}

L'événement n'est pas traité comme un événement recommandé. Plus précisément :

- **L'événement est entièrement rejeté.** Les événements eCommerce recommandés invalides n'apparaissent pas sur le profil utilisateur, ne figurent pas dans Currents et ne sont pas disponibles pour la segmentation.
- Les fonctionnalités en aval des événements recommandés ne s'exécutent pas, notamment :
  - Le suivi du chiffre d'affaires (reporting du chiffre d'affaires, champs calculés utilisateur comme `total_revenue`)
  - Les mises à jour de l'objet panier sur le profil utilisateur
  - Les déclencheurs « Perform Cart Updated Event » ou « Placed Order » dans Canvas et Campaigns

La manière dont les erreurs sont signalées dépend du chemin d'ingestion :

- **REST API (`/users/track`) :** chaque événement invalide est signalé dans le tableau d'erreurs de la réponse. Chaque entrée vous indique quel événement a échoué (index) et pourquoi (type). Le champ message de niveau supérieur indique toujours « success », ce qui signifie simplement que votre requête a atteint Braze, pas que chaque événement était valide. Vérifiez toujours la présence d'un tableau d'erreurs dans la réponse.
- **SDK Braze :** les appels SDK retournent immédiatement et la validation s'exécute en arrière-plan, de sorte que les erreurs ne sont pas renvoyées à votre application. Pour être informé des échecs de validation des événements eCommerce, surveillez l'e-mail récapitulatif des échecs (voir [Trouver les échecs](#find-failures)).

#### Exemple de réponse d'erreur API {#example-api-error-response}

L'endpoint `/users/track` renvoie des erreurs au niveau des champs indiquant quelles propriétés ont échoué et pourquoi. Notez que le `message` de niveau supérieur peut renvoyer `"success"` car l'événement a été accepté dans le pipeline ; le tableau `errors` vous indique quels champs ont échoué à la validation du schéma. Consultez l'exemple de réponse d'erreur suivant.

```json
{
 "message": "success",
 "errors": [{ "index": 0, "input_array": "purchases", "type": "'currency' must be an ISO 4217 currency" }]
}
```

Les échecs sont également classifiés en interne et agrégés pour l'e-mail récapitulatif des échecs :

| Type d'échec            | Signification                                     | Exemple                                                        |
|------------------------|---------------------------------------------------|----------------------------------------------------------------|
| `missing_property`     | Un champ requis est absent.                       | `order_placed` envoyé sans `order_id`.                        |
| `extra_property`       | Un champ a été ajouté que le schéma ne définit pas. | Un champ personnalisé `gift_wrapped` au niveau supérieur de `properties` au lieu d'être dans `metadata`. |
| `unexpected_data_type` | Un champ est du mauvais type.                     | `total_value: "29.99"` (chaîne de caractères) au lieu de `29.99` (nombre).   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemple de réponse d'erreur API" }

{% alert note %}
Les noms d'événements qui ne correspondent pas exactement à un événement recommandé (par exemple, `ecommerce.OrderPlaced`) ignorent entièrement la validation et sont enregistrés comme des événements personnalisés ordinaires. Ils apparaissent dans Currents et la segmentation sous le nom que vous avez envoyé, mais ne bénéficient d'aucun traitement d'événement recommandé et d'aucune entrée `errors` dans la réponse.
{% endalert %}

#### Trouver les échecs {#find-failures}

Braze envoie par e-mail à vos administrateurs d'espace de travail un récapitulatif des échecs de validation des événements recommandés afin que vous puissiez identifier et corriger les problèmes d'intégration sans surveiller manuellement chaque événement.

L'e-mail récapitulatif inclut :

- **Nombre total d'erreurs :** le nombre d'erreurs pour la période de reporting.
- **Erreurs par événement :** une ventilation du nombre d'événements ayant échoué pour chaque type d'événement recommandé (par exemple, `ecommerce.cart_updated` et `ecommerce.order_placed`). Utilisez cela pour identifier quels événements de votre intégration nécessitent une attention prioritaire.
- **Erreurs par source :** une répartition entre API et SDK, afin de pouvoir identifier quelle intégration génère les échecs.

Si vous ne recevez pas ces e-mails ou souhaitez vérifier la liste des destinataires, contactez votre équipe de compte Braze.

#### Diagnostiquer et corriger les échecs {#diagnose-and-fix-failures}

Lorsque vous recevez un e-mail récapitulatif des échecs :

1. **Identifiez l'événement en échec et sa source.** L'e-mail sépare les échecs par nom d'événement et source d'intégration (`sdk` versus `rest_api`), ce qui vous permet de cibler précisément quelle intégration nécessite la correction. Si vous avez plusieurs sources envoyant le même événement (par exemple, le SDK de votre vitrine et un webhook backend envoyant tous deux `cart_updated`), traitez-les indépendamment.
2. **Comparez votre payload au schéma** dans [Schémas d'événements](#event-schemas). La plupart des échecs correspondent à l'un des trois cas suivants :
   - `missing_property` : un champ requis est absent. Pour résoudre cela, ajoutez le champ requis.
   - `extra_property` : un champ personnalisé se trouve au niveau supérieur de `properties`. Pour résoudre cela, déplacez le champ personnalisé dans `metadata` (au niveau de l'événement) ou `products[].metadata` (par produit).
   - `unexpected_data_type` : une valeur est du mauvais type (par exemple, `total_value` envoyé comme chaîne de caractères). Pour résoudre cela, convertissez la valeur avant l'envoi.
3. **Testez le payload corrigé dans un espace de travail de développement** avant de le déployer en production. Envoyez un événement test connu pour un utilisateur test, puis vérifiez le comportement attendu de l'événement recommandé sur le profil de cet utilisateur (par exemple, l'objet panier se met à jour, le chiffre d'affaires s'incrémente ou le déclencheur de panier abandonné se déclenche).
4. **Surveillez le prochain e-mail d'échecs** pour confirmer que le nombre d'échecs pour cet événement, cette source et ce type tombe à zéro.

Pour les exigences complètes de propriétés par événement, consultez [Schémas d'événements](#event-schemas).