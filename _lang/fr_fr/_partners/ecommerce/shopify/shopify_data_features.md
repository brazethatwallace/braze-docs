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

L'intégration Shopify utilise les [événements recommandés pour l'eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) pour capturer les principaux comportements d'achat. Pour des exemples de mise en œuvre et des stratégies marketing utilisant ces événements, consultez les [cas d'utilisation eCommerce]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/).

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
{% subtabs global %}
{% subtab Product viewed %}
**Événement** : `ecommerce.product_viewed`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsqu'un client consulte une page produit<br>
**Source de données** : SDK Braze<br>
**Cas d'utilisation** : Abandon de navigation

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
**Déclenché** : Lorsqu'un client ajoute, supprime ou met à jour un article dans son panier<br>
**Source de données** : SDK Braze<br>
**Cas d'utilisation** : Abandon de panier

Pour les Canvas d'abandon de panier, vous devez d'abord ajouter l'étiquette Liquid du panier d'achat initial afin de disposer du contexte du panier dans votre message.

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

Vous pouvez ensuite ajouter les étiquettes Liquid de panier d'achat suivantes dans votre message.

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
Pour en savoir plus sur la création d'une boucle Liquid `for` permettant d'ajouter dynamiquement tous les produits dans votre e-mail, consultez la section [Personnalisation des produits du panier abandonné pour les e-mails]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart).
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Événement** : `ecommerce.checkout_started`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsqu'un utilisateur accède à la page de paiement<br>
**Source de données** : REST API Braze<br>
**Cas d'utilisation** : Abandon du paiement

{% alert important %}
Si un client utilise Shop Pay comme option de paiement accéléré, Shopify peut contourner certains événements de paiement standard (comme le webhook Shopify checkout started). Braze risque alors de ne pas recevoir les données nécessaires pour ajouter l'alias du jeton de paiement, ce qui peut impacter le suivi de l'abandon de paiement et la réconciliation des profils utilisateurs.
{% endalert %}

Pour les Canvas d'abandon de paiement, vous devez d'abord utiliser l'étiquette Liquid suivante :

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

Vous pouvez ensuite ajouter les étiquettes Liquid suivantes dans votre message pour référencer les produits de votre panier au moment du paiement.

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
**Cas d'utilisation** : Confirmation de commande, reciblage post-achat, ventes incitatives ou croisées

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
Le webhook checkout completed de Shopify ne contient pas d'URL de produits ni d'URL d'images. Vous devez donc utiliser la personnalisation Liquid via les Catalogues, comme décrit dans la section [Personnalisation des produits du panier abandonné pour les e-mails]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey).
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Événement** : `shopify_fulfilled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**Déclenché** : Lorsque la commande d'un utilisateur est exécutée et prête à être expédiée<br>
**Source de données** : REST API Braze<br>
**Cas d'utilisation** : (Transactionnel) Mise à jour de l'exécution

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Événement** : `shopify_partially_fulfilled_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**Déclenché** : Lorsqu'une partie de la commande d'un utilisateur est exécutée et prête à être expédiée<br>
**Source de données** : REST API Braze<br>
**Cas d'utilisation** : (Transactionnel) Mise à jour de l'exécution

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Événement** : `shopify_paid_order`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**Déclenché** : Lorsque la commande d'un utilisateur est marquée comme payée dans Shopify<br>
**Source de données** : REST API Braze<br>
**Cas d'utilisation** : (Transactionnel) Confirmation de paiement

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Événement** : `ecommerce.order_cancelled`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsque la commande d'un utilisateur est annulée<br>
**Source de données** : REST API Braze<br>
**Cas d'utilisation** : (Transactionnel) Confirmation d'annulation de commande

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillments | `{{event_properties.${fulfillments}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Fulfillment Status | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Événement** : `ecommerce.order_refunded`<br>
**Type** : Événement recommandé<br>
**Déclenché** : Lorsque la commande d'un utilisateur est remboursée<br>
**Source de données** : REST API Braze<br>
**Cas d'utilisation** : (Transactionnel) Confirmation de remboursement

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Order Note | `{event_properties.${note}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Événement** : `shopify_account_login`<br>
**Type** : [Événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**Déclenché** : Lorsqu'un utilisateur se connecte à son compte<br>
**Source de données** : REST API Braze<br>
**Cas d'utilisation** : Série de bienvenue

{% raw %}
| Variable | Modèle Liquid |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Événements Shopify suivis" }
{% endraw %}

{% alert note %}
L'intégration Shopify ne prend actuellement pas en charge le remplissage de l'[événement d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-events) Braze. Par conséquent, les filtres d'achat, les étiquettes Liquid, les déclencheurs basés sur l'action et les analyses doivent utiliser l'événement `ecommerce.order_placed`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Attributs personnalisés Shopify pris en charge {#supported-shopify-custom-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab Exemple de payload %}
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
{% tab Attributs personnalisés Shopify %}
| Nom de l'attribut | Description |
| --- | --- |
| `shopify_total_spent` | Le montant total dépensé par le client sur l'ensemble de son historique de commandes. |
| `shopify_order_count` | Le nombre de commandes associées à ce client. Les commandes test et archivées ne sont pas comptabilisées. |
| `shopify_last_order_id` | L'ID de la dernière commande du client. |
| `shopify_last_order_name` | Le nom de la dernière commande du client. Correspond directement au champ `name` de la ressource de commande. |
| `shopify_zipcode` | Le code postal du client issu de son adresse par défaut. |
| `shopify_province` | La province du client issue de son adresse par défaut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés Shopify pris en charge" }

{% alert important %}
Un problème connu avec la version actuelle de l'API Shopify empêche l'attribut utilisateur `shopify_last_order_name` de se remplir correctement. Voici l'impact sur les utilisateurs :<br><br>

- **Utilisateurs existants :** Pour tout utilisateur ayant déjà une valeur pour `shopify_last_order_name`, cette valeur persiste mais n'est pas mise à jour par les commandes suivantes.
- **Nouveaux utilisateurs :** Pour les nouveaux utilisateurs, le champ ne se remplit pas et reste vide ou nul.

Cette page sera mise à jour dès que Shopify aura résolu ce problème.
{% endalert %}

### Personnalisation Liquid {#liquid-personalization}

Pour ajouter une personnalisation Liquid à vos attributs personnalisés Shopify, sélectionnez **+ Personalization**. Sélectionnez ensuite **Custom Attributes** comme type de personnalisation.

![La section « Add Personalization » avec la liste déroulante « Attribute » étendue.]({% image_buster /assets/img/shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Après avoir sélectionné votre attribut personnalisé, saisissez une valeur par défaut et copiez l'extrait de code Liquid dans votre message.

![Collage d'un extrait de code Liquid dans un message.]({% image_buster /assets/img/shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## Attributs standard Shopify pris en charge {#supported-shopify-standard-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- E-mail
- Prénom
- Nom de famille
- Téléphone
- Ville
- Pays

{% alert note %}
Braze ne met à jour les attributs personnalisés Shopify et les attributs standard Braze que lorsqu'il détecte une différence par rapport aux données du profil utilisateur existant. Par exemple, si les données entrantes de Shopify contiennent le prénom « Bob » et que « Bob » est déjà enregistré comme prénom sur le profil utilisateur Braze, aucune mise à jour n'est déclenchée et aucun point de donnée ne vous est facturé.
{% endalert %}

## Collecte de données SDK {#sdk-data-collection}

Pour plus d'informations sur les données collectées par les SDK Braze, consultez la section [Collecte de données SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

## Backfill historique {#historical-backfill}

> Les données historiques Shopify sont importées avant la connexion de Braze : les événements de commande des 90 derniers jours et les données clients de l'année écoulée. Les deux périodes sont calculées à partir de la date à laquelle vous finalisez votre intégration.

Via la [configuration de l'intégration standard Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) ou la [configuration de l'intégration personnalisée Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/), vous pouvez activer le backfill historique pour cibler vos anciens clients. Cette fonctionnalité importe vos commandes Shopify (événements liés aux commandes) des 90 derniers jours et les profils utilisateurs de l'année écoulée. Les deux périodes sont calculées à partir de la date à laquelle vous finalisez votre intégration.

Lorsque Braze importe vos clients Shopify, le type d'`external_id` que vous avez choisi dans vos paramètres de configuration leur est attribué.

{% alert note %}
Si vous êtes déjà client Braze avec des Campaigns ou des Canvas actifs, vérifiez l'impact des clients et événements de commande importés sur vos Segments et parcours avant d'activer le backfill historique.
{% endalert %}

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

### Mise en place du backfill historique Shopify {#setting-up-shopify-historical-backfill}

1. Activez le backfill historique dans l'étape **Track Shopify data**.

![L'étape « Track Shopify data » de l'intégration Shopify montrant le backfill historique sélectionné.]({% image_buster /assets/img/shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. Une fois la configuration de votre intégration terminée, Braze lance la synchronisation initiale des données. Vous pouvez suivre la progression dans l'onglet **Shopify Data** de vos paramètres d'intégration.

![La page des paramètres d'intégration Shopify avec un indicateur de chargement montrant que les événements sont en cours de synchronisation.]({% image_buster /assets/img/shopify/historical_data_backfill_syncing.png %})

### Données synchronisées {#synced-data}

Lors de la synchronisation initiale, Braze importe les événements de commande des 90 derniers jours et les profils utilisateurs de l'année écoulée, chaque période étant calculée à partir de la date à laquelle vous finalisez votre intégration. Lorsque Braze importe vos clients Shopify, le type d'`external_id` que vous avez choisi dans vos paramètres de configuration leur est attribué.

Le tableau suivant résume les données incluses dans ce chargement initial.

| Événements recommandés Braze | Événements personnalisés Shopify | Attributs standard Braze | Statuts d'abonnement Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li><li>Order cancelled</li><li>Order refunded</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Prénom</li><li>Nom de famille</li><li>Téléphone</li><li>Ville</li><li>Pays</li><li>Chiffre d'affaires total</li><li>Remboursements totaux</li><li>Total des commandes</li></ul>{:/} | {::nomarkdown}<ul><li>Abonnements marketing par e-mail associés à cette boutique Shopify</li><li>Abonnements marketing par SMS associés à cette boutique Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Données synchronisées" }