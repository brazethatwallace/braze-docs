---
nav_title: Fonctionnalités des données de Shopify
article_title: Fonctionnalités des données de Shopify
description: "Cet article de référence couvre les fonctionnalités des données de Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 4
---

# Fonctionnalités des données de Shopify {#shopify-data-features}

> Cet article donne un aperçu de nos fonctionnalités Shopify, y compris les données Shopify suivies et des exemples de payloads, de backfill historique et de synchronisation des produits.

## Événements Shopify suivis {#tracked-shopify-events}

L'intégration Shopify utilise les [événements eCommerce recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) pour capturer les comportements d'achat clés. Pour des exemples de déploiement et des stratégies marketing utilisant ces événements, consultez les [cas d'usage eCommerce]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab Exemple de payload %}
{% subtabs global %}
{% subtab Product viewed %}
```json
{
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "12345",
        "product_name": "product",
        "variant_id": "123",
        "image_url": "www.image-url.com",
        "product_url": "mystorefront.myshopify.com/product",
        "price": 10,
        "currency": "USD",
        "source": "mystorefront.myshopify.com",
        "metadata": {
          "sku": "sku"
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
    }
}
```
{% endsubtab %}
{% subtab Cart updated %}
```json
{
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "Z2NwLXVzLWVhc3QxOjAxSjk3UFg4RlFZMjVTVkRHRlc1RlI3SlRY",
        "currency": "USD",
        "total_value": 2000000,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "PANTS!!!",
                "variant_id": "44610569208040",
                "image_url": "https://cdn.shopify.com/s/files/1/0604/4211/6328/files/1200px-Trousers-colourisolated.jpg?v=1689256168",
                "product_url": "https://test-store.myshopify.com/products/pants?variant=44610569208040",
                "quantity": 2,
                "price": 1000000,
                "metadata": {
                    "sku": "007"
                }
            }
        ],
        "source": "https://test-store.myshopify.com",
        "metadata": {}
    }
}
```
{% endsubtab %}
{% subtab Checkout started %}
```json
{
    "name": "ecommerce.checkout_started",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "checkout_id": "123123123",
        "metadata": {
            "checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token"
        }
    }
}
```
{% endsubtab %}
{% subtab Order placed %}
{% raw %}
```json
{
    "name": "ecommerce.order_placed",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": "1234",
            "tags": [
                "heavy",
                "heavy2"
            ],
            "referring_site": "https://www.google.com",
            "payment_gateway_names": [
                "visa",
                "bogus"
            ]
        }
    }
}
```
{% endraw %}
{% endsubtab %}
{% subtab Fulfilled order %}
```json
{
 "name": "shopify_fulfilled_order",
 "time": "2022-05-23T14:44:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
  "variant_id": 40094740549876,
       "variant_title": "Small Dark Denim Top",


       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": "2022-05-23T14:44:34-04:00",
   "fulfillment_status": "fulfilled",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "456",
       "tracking_numbers": [
         "456"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "Small Dark Denim Top",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Partially fulfilled order %}
```json
{
 "name": "shopify_partially_fulfilled_order",
 "time": "2022-05-23T14:43:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": null,
   "fulfillment_status": "partial",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "123",
       "tracking_numbers": [
         "123"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "properties": [],
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% subtab Paid order %}
```json
{
 "name": "shopify_paid_order",
 "time": "2022-05-23T13:52:38-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": null,
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ]
 }
}
```
{% endsubtab %}
{% subtab Order cancelled %}
```json
{
    "name": "ecommerce.order_cancelled",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cancel_reason": "no longer necessary",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": "1234",
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```
{% endsubtab %}
{% subtab Order refunded %}
```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "total_value": 421.88,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
		"order_note": "item was broken"
        }
    }
}
```
{% endsubtab %}
{% subtab Account login %}
```json
{
	"name": "shopify_account_login",
	"properties": {
	"source": "braze-mock-storefront.myshopify.com"
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Événements Shopify %}

{% alert note %}
Braze s'appuie sur Shopify pour fournir les propriétés d'événement requises (telles que `cart_id` ou `cart_token`) pour les événements eCommerce. Dans de rares cas, des problèmes temporaires avec Shopify peuvent empêcher la transmission de ces propriétés, ce qui peut entraîner la suppression des événements concernés.
{% endalert %}

{% subtabs global %}
{% subtab Product viewed %}
**Événement** : `ecommerce.product_viewed`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsqu'un client consulte une page produit<br>
**Source de données** : SDK Braze<br>
**Cas d'usage** : Abandon de navigation

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>Ajoutez le domaine de votre site Shopify avant l'URL. |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**Événement** : `ecommerce.cart_updated`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsqu'un client ajoute, supprime ou met à jour son panier<br>
**Source de données** : SDK Braze<br>
**Cas d'usage** : Abandon de panier

Pour les Canvas d'abandon de panier, vous devez d'abord ajouter l'étiquette Liquid initiale du panier pour accéder au contexte du panier dans votre message.

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

Vous pouvez ensuite ajouter les étiquettes Liquid de panier suivantes dans votre message.

{% raw %}
| Variable         | Modèle Liquid                                   |
|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata[0].sku }}`  |
| `source`           | `{{ shopping_cart.source }}`                        |
| `metadata (value)` | `{{ shopping_cart.metadata[0].<add_value_here> }}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% alert tip %}
Pour en savoir plus sur la création d'une boucle Liquid `for` permettant d'ajouter dynamiquement tous les produits dans votre e-mail, consultez [Personnalisation des produits d'abandon de panier pour les e-mails]({{site.baseurl}}/ecommerce_use_cases#abandoned-cart).
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Événement** : `ecommerce.checkout_started`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsqu'un utilisateur accède à la page de paiement<br>
**Source de données** : REST API Braze<br>
**Cas d'usage** : Abandon de paiement

{% alert important %}
Si un client utilise Shop Pay comme option de paiement accéléré, Shopify peut contourner certains événements de paiement standard (comme le webhook Shopify de début de paiement). Cela signifie que Braze peut ne pas recevoir les données nécessaires pour ajouter l'alias du jeton de paiement, ce qui peut impacter le suivi d'abandon de paiement et la réconciliation des profils utilisateurs.
{% endalert %}

Pour les Canvas d'abandon de paiement, vous devez d'abord utiliser l'étiquette Liquid suivante :

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

Vous pouvez ensuite ajouter les étiquettes Liquid suivantes dans votre message pour référencer les produits présents dans votre panier au moment du paiement.

{% raw %}
| Variable         | Modèle Liquid                                   |
|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata.sku }}`     |
| `source`           | `{{ shopping_cart.source }}`                        |
| `checkout_url`     | `{{ shopping_cart.metadata[0].checkout_url }}`     |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**Événement** : `ecommerce.order_placed`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsqu'un utilisateur finalise le processus de paiement et passe une commande<br>
**Source de données** : REST API Braze<br>
**Cas d'usage** : Confirmation de commande, reciblage post-achat, ventes incitatives ou ventes croisées

{% raw %}
| Variable                | Modèle Liquid                                   |
|-------------------------|-----------------------------------------------------|
| cart_id                 | `{{event_properties.${cart_id}}}`                   |
| currency                | `{{event_properties.${currency}}}`                  |
| discounts               | `{{event_properties.${discounts}}}`                 |
| order_id                | `{{event_properties.${order_id}}}`                  |
| product_id              | `{{event_properties.${products}[0].product_id}}`   |
| product_name            | `{{event_properties.${products}[0].product_name}}` |
| variant_id              | `{{event_properties.${products}[0].variant_id}}`   |
| quantity                | `{{event_properties.${products}[0].quantity}}`     |
| sku                     | `{{event_properties.${products}[0].metadata.sku}}` |
| total_discounts         | `{{event_properties.${total_discounts}}}`           |
| order_status_url        | `{{event_properties.${metadata}.order_status_url}}` |
| order_number            | `{{event_properties.${metadata}.order_number}}`     |
| tags                    | `{{event_properties.${metadata}.tags}}`             |
| referring_site          | `{{event_properties.${metadata}.referring_site}}`   |
| payment_gateway_names    | `{{event_properties.${metadata}.payment_gateway_names}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% alert tip %}
Le webhook de paiement finalisé de Shopify ne contient pas les URL de produits ni les URL d'images. Par conséquent, vous devez utiliser la personnalisation Liquid via les catalogues, comme indiqué dans [Personnalisation des produits d'abandon de panier pour les e-mails]({{site.baseurl}}/ecommerce_use_cases#order-confirmation-and-feedback-survey).
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Événement** : `shopify_fulfilled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Déclenché** : Lorsque la commande d'un utilisateur est exécutée et prête pour l'expédition<br>
**Source de données** : REST API Braze<br>
**Cas d'usage** : (Transactionnel) Mise à jour d'exécution

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Remises totales | `{{event_properties.${total_discounts}}}` |
| Statut de confirmation | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d'annulation | `{{event_properties.${cancelled_at}}}` |
| Horodatage de clôture | `{{event_properties.${closed_at}}}` |
| ID de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité de l'article | `{{event_properties.${line_items}[0].quantity}}` |
| UGS de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l'article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l'article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| Titre de l'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l'expédition | `{{event_properties.${shipping}[0].price}}` |
| Statut d'exécution | `{{event_properties.${fulfillment_status}}}` |
| Statut d'expédition de l'exécution | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Statut | `{{event_properties.${fulfillments}[0].status}}` |
| Transporteur de l'exécution | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Numéro de suivi de l'exécution | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Numéros de suivi de l'exécution | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| URL de suivi de l'exécution | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| URLs de suivi de l'exécution | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Statut d'exécution | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nom de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Prix de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID produit de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantité de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Expédition de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| UGS de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Titre de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fournisseur de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Événement** : `shopify_partially_fulfilled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Déclenché** : Lorsqu'une partie de la commande d'un utilisateur est exécutée et prête pour l'expédition<br>
**Source de données** : REST API Braze<br>
**Cas d'usage** : (Transactionnel) Mise à jour d'exécution

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Remises totales | `{{event_properties.${total_discounts}}}` |
| Statut de confirmation | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d'annulation | `{{event_properties.${cancelled_at}}}` |
| Horodatage de clôture | `{{event_properties.${closed_at}}}` |
| ID de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité de l'article | `{{event_properties.${line_items}[0].quantity}}` |
| UGS de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l'article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l'article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| Titre de l'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l'expédition | `{{event_properties.${shipping}[0].price}}` |
| Statut d'exécution | `{{event_properties.${fulfillment_status}}}` |
| Statut d'expédition de l'exécution | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Statut de l'exécution | `{{event_properties.${fulfillments}[0].status}}` |
| Transporteur de l'exécution | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Numéro de suivi de l'exécution | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Numéros de suivi de l'exécution | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| URL de suivi de l'exécution | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| URLs de suivi de l'exécution | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Statut d'exécution | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nom de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Prix de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID produit de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantité de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Expédition de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| UGS de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Titre de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fournisseur de l'exécution | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Événement** : `shopify_paid_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Déclenché** : Lorsque la commande d'un utilisateur est marquée comme payée dans Shopify<br>
**Source de données** : REST API Braze<br>
**Cas d'usage** : (Transactionnel) Confirmation de paiement

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Statut de confirmation | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d'annulation | `{{event_properties.${cancelled_at}}}` |
| Remises totales | `{{event_properties.${total_discounts}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Codes de réduction | `{{event_properties.${discount_codes}}}` |
| ID de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité de l'article | `{{event_properties.${line_items}[0].quantity}}` |
| UGS de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l'article | `{{event_properties.${line_items}[0].vendor}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| Titre de l'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l'expédition | `{{event_properties.${shipping}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Événement** : `ecommerce.order_cancelled`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsque la commande d'un utilisateur est annulée<br>
**Source de données** : REST API Braze<br>
**Cas d'usage** : (Transactionnel) Confirmation d'annulation de commande

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Prix total | `{{event_properties.${total_price}}}` |
| Remises totales | `{{event_properties.${total_discounts}}}` |
| Confirmé | `{{event_properties.${confirmed}}}` |
| URL du statut de la commande | `{{event_properties.${order_status_url}}}` |
| Numéro de commande | `{{event_properties.${order_number}}}` |
| Horodatage d'annulation | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Codes de réduction | `{{event_properties.${discount_codes}}}` |
| Statut d'exécution | `{{event_properties.${fulfillment_status}}}` |
| Exécutions | `{{event_properties.${fulfillments}}}` |
| ID de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité de l'article | `{{event_properties.${line_items}[0].quantity}}` |
| UGS de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l'article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l'article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Statut d'exécution | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Titre de l'expédition | `{{event_properties.${shipping}[0].title}}` |
| Prix de l'expédition | `{{event_properties.${shipping}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Événement** : `ecommerce.order_refunded`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsque la commande d'un utilisateur est remboursée<br>
**Source de données** : REST API Braze<br>
**Cas d'usage** : (Transactionnel) Confirmation de remboursement

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| ID de commande | `{{event_properties.${order_id}}}` |
| Note de commande | `{event_properties.${note}}}` |
| ID de l'article | `{{event_properties.${line_items}[0].product_id}}` |
| Quantité de l'article | `{{event_properties.${line_items}[0].quantity}}` |
| UGS de l'article | `{{event_properties.${line_items}[0].sku}}` |
| Titre de l'article | `{{event_properties.${line_items}[0].title}}` |
| Fournisseur de l'article | `{{event_properties.${line_items}[0].vendor}}` |
| Nom de l'article | `{{event_properties.${line_items}[0].name}}` |
| Propriétés de l'article | `{{event_properties.${line_items}[0].properties}}` |
| Prix de l'article | `{{event_properties.${line_items}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Titre de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Événement** : `shopify_account_login`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Déclenché** : Lorsqu'un utilisateur se connecte à son compte<br>
**Source de données** : REST API Braze<br>
**Cas d'usage** : Série de bienvenue

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% alert note %}
L'intégration Shopify ne prend actuellement pas en charge le remplissage de l'[événement d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) Braze. Par conséquent, les filtres d'achat, les étiquettes Liquid, les déclencheurs basés sur l'action et les analyses doivent utiliser l'événement `ecommerce.order_placed`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Attributs personnalisés Shopify pris en charge {#supported-shopify-custom-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab Example Payload %}
{% subtabs %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Shopify Custom Attributes %}
| Nom de l'attribut | Description |
| --- | --- |
| `shopify_total_spent` | Le montant total dépensé par le client sur l'ensemble de son historique de commandes. |
| `shopify_order_count` | Le nombre de commandes associées à ce client. Les commandes de test et archivées ne sont pas comptabilisées. |
| `shopify_last_order_id` | L'ID de la dernière commande du client. |
| `shopify_last_order_name` | Le nom de la dernière commande du client. Ce champ est directement lié au champ `name` de la ressource de commande. |
| `shopify_zipcode` | Le code postal du client issu de son adresse par défaut. |
| `shopify_province` | La province du client issue de son adresse par défaut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés Shopify pris en charge" }

{% alert important %}
Un problème connu avec la version actuelle de l'API Shopify empêche l'attribut utilisateur `shopify_last_order_name` de se remplir correctement. L'impact sur les utilisateurs est le suivant :<br><br>

- **Utilisateurs existants :** Pour tout utilisateur possédant déjà une valeur pour `shopify_last_order_name`, cette valeur est conservée mais n'est pas mise à jour par les commandes suivantes.
- **Nouveaux utilisateurs :** Pour tout nouvel utilisateur, le champ ne se remplit pas et reste vide ou nul.

Cette page sera mise à jour une fois que Shopify aura résolu ce problème.
{% endalert %}

### Personnalisation Liquid {#liquid-personalization}

Pour ajouter une personnalisation Liquid à vos attributs personnalisés Shopify, sélectionnez **+ Personalization**. Puis sélectionnez **Custom Attributes** comme type de personnalisation.

![La section « Add Personalization » avec le menu déroulant « Attribute » déplié.]({% image_buster /assets/img/shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Après avoir sélectionné votre attribut personnalisé, saisissez une valeur par défaut et copiez l'extrait de code Liquid dans votre message.

![Collage d'un extrait de code Liquid dans un message.]({% image_buster /assets/img/shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## Attributs standard Shopify pris en charge {#supported-shopify-standard-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- E-mail
- Prénom
- Nom
- Téléphone
- Ville
- Pays

{% alert note %}
Braze ne met à jour les attributs personnalisés Shopify pris en charge et les attributs standard Braze que s'il y a une différence dans les données par rapport au profil utilisateur existant. Par exemple, si les données entrantes de Shopify contiennent le prénom Bob et que Bob existe déjà comme prénom dans le profil utilisateur Braze, Braze ne déclenchera pas de mise à jour et aucun point de donnée ne vous sera facturé.
{% endalert %}

## Collecte de données par le SDK {#sdk-data-collection}

Pour plus d'informations sur les données collectées par les SDK de Braze, consultez [Collecte de données par le SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).

## Importation de données historiques {#historical-backfill}

> Les données historiques de Shopify sont importées avant que vous ne connectiez Braze : les événements de commande des 90 derniers jours et les données clients de l'année écoulée. Les deux périodes sont calculées à partir de la date à laquelle vous finalisez votre intégration.

Grâce à la [configuration de l'intégration standard Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou à la [configuration de l'intégration personnalisée Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration), vous pouvez activer l'importation de données historiques pour cibler vos anciens clients. Cela importe vos commandes Shopify (événements liés aux commandes) des 90 derniers jours et les profils utilisateur de l'année écoulée. Les deux périodes sont calculées à partir de la date à laquelle vous finalisez votre intégration.

Lorsque Braze importe vos clients Shopify, le type d'`external_id` que vous avez choisi dans vos paramètres de configuration leur est attribué.

{% alert note %}
Si vous êtes déjà client de Braze avec des Campaigns ou des Canvas actifs, vérifiez l'impact des clients et événements de commande importés sur vos Segments et parcours avant d'activer l'importation de données historiques.
{% endalert %}

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

### Configurer l'importation de données historiques Shopify {#setting-up-shopify-historical-backfill}

1. Activez l'importation de données historiques dans l'étape **Track Shopify data**.

![L'étape « Track Shopify data » de l'intégration Shopify montrant l'importation de données historiques sélectionnée.]({% image_buster /assets/img/shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. Une fois la configuration de votre intégration terminée, Braze lance la synchronisation initiale des données. Vous pouvez suivre la progression dans l'onglet **Shopify Data** de vos paramètres d'intégration.

![La page des paramètres d'intégration Shopify avec un indicateur de chargement montrant que les événements sont en cours de synchronisation.]({% image_buster /assets/img/shopify/historical_data_backfill_syncing.png %})

### Données synchronisées {#synced-data}

Lors de la synchronisation initiale des données, Braze importe les événements de commande des 90 derniers jours et les profils utilisateur de l'année écoulée, chaque période étant calculée à partir de la date à laquelle vous finalisez votre intégration. Lorsque Braze importe vos clients Shopify, le type d'`external_id` que vous avez choisi dans vos paramètres de configuration leur est attribué.

Le tableau suivant résume les données incluses dans ce chargement initial.

| Événements recommandés par Braze | Événements personnalisés Shopify | Attributs standard Braze | Statuts d'abonnement Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li><li>Order cancelled</li><li>Order refunded</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li><li>Total Revenue</li><li>Total Refunds</li><li>Total Orders</li></ul>{:/} | {::nomarkdown}<ul><li>Abonnements au marketing par e-mail associés à cette boutique Shopify</li><li>Abonnements au marketing par SMS associés à cette boutique Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Données synchronisées" }