---
nav_title: "Objet Achat"
article_title: Objet Achat de l'API
page_order: 8
page_type: reference
description: "Cet article de référence explique les différents composants d'un objet Achat, comment l'utiliser correctement et des exemples dont vous pouvez vous inspirer."

---

# Objet Achat {#purchase-object}

> Cet article explique les différents composants d'un objet Achat, comment l'utiliser correctement, les bonnes pratiques et des exemples dont vous pouvez vous inspirer.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## Qu'est-ce qu'un objet Achat ? {#what-is-a-purchase-object}

Un objet Achat est un objet transmis via l'API lorsqu'un achat a été effectué. Chaque objet Achat se trouve dans un tableau d'achats, et chaque objet représente un achat unique réalisé par un utilisateur donné à un moment donné. L'objet Achat comporte de nombreux champs qui permettent au backend de Braze de stocker et d'exploiter ces informations à des fins de personnalisation et de collecte de données.

### Corps de l'objet {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [ID utilisateur externe]({{site.baseurl}}/api/basics/#user-ids)
- [Identifiant d'application]({{site.baseurl}}/api/identifier_types/)
- [Code des devises ISO 4217 Wiki](http://en.wikipedia.org/wiki/ISO_4217)
- [Code temporel ISO 8601 Wiki](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Certaines paires d'identifiants ne peuvent pas être utilisées conjointement, et `email` a priorité sur `phone` lorsque les deux sont fournis. Pour plus de détails, consultez la section [Résolution des identifiants]({{site.baseurl}}/api/objects_filters/user_attributes_object/#identifier-resolution).
{% endalert %}

## ID du produit d'achat {#purchase-product-id}

Dans l'objet Achat, le `product_id` est un identifiant pour l'achat (tel que `Product Name` ou `Product Category`) :

- Braze vous permet de stocker jusqu'à 5 000 `product_id` dans le tableau de bord.
- Le `product_id` peut contenir jusqu'à 255 caractères.

### Conventions de nommage {#naming-conventions}

Chez Braze, nous proposons des conventions générales de nommage pour le `product_id` de l'objet Achat. Lorsque vous choisissez un `product_id`, Braze suggère d'utiliser des noms simples tels que le nom du produit ou la catégorie de produit (au lieu des unités de gestion des stocks) dans l'intention de regrouper tous les éléments enregistrés par ce `product_id`.

Cela facilite l'identification des produits à des fins de segmentation et de déclenchement.

### Journaliser les achats au niveau de la commande {#log-purchases-at-the-order-level}

Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id` (par exemple `Online Order` ou `Completed Order`).

Par exemple, pour enregistrer des achats au niveau de la commande dans le SDK Web :

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## Objet propriétés d'achat {#purchase-properties-object}

{% include data_activation/purchase_event_property_data_types.md %}

Pour une référence consolidée des types de données à travers les attributs personnalisés, les propriétés d'événement et les catalogues, consultez [Types de données]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#purchase-event-property-data-types).

### Propriétés d'achat {#purchase-properties}

Les [propriétés d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) peuvent être utilisées pour déclencher des messages et pour la personnalisation à l'aide de Liquid, ce qui vous permet également de segmenter en fonction de ces propriétés.

#### Conventions de nommage {#naming-conventions}

Il est important de noter que cette fonctionnalité est activée **par produit**, et non par achat. Par exemple, si vous avez un volume élevé de produits distincts, mais que chacun d'entre eux possède les mêmes propriétés, la segmentation peut s'avérer superflue.

Dans ce cas, nous recommandons d'utiliser les noms de produits au niveau du groupe plutôt que les identifiants au niveau des transactions lors de la configuration des structures de données. Par exemple, une société de vente de billets de train devrait avoir des produits pour « voyage simple », « voyage aller-retour », « multi-villes », et non des transactions spécifiques telles que « transaction 123 » ou « transaction 046 ». Autre exemple, pour l'événement d'achat « nourriture », il serait préférable que les propriétés soient « gâteau » et « sandwich ».

{% alert important %}
Notez que les produits peuvent être ajoutés via la REST API de Braze. Par exemple, si vous envoyez un appel à l'endpoint `/users/track` et incluez un nouvel ID d'achat, Braze crée automatiquement un produit dans la section **Paramètres des données** > **Produits** du tableau de bord.
{% endalert %}

### Exemple d'objet Achat {#example-purchase-object}

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### Objets Achat, objets d'événement et webhooks {#purchase-objects-event-objects-and-webhooks}

À l'aide de l'exemple fourni, nous pouvons voir que quelqu'un a acheté un sac à dos avec les propriétés suivantes : couleur, monogramme, durée de paiement, taille et marque. Nous pouvons ensuite créer des segments avec ces propriétés en utilisant les [propriétés d'événement d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) ou envoyer des messages personnalisés par le biais d'un canal à l'aide de Liquid. Par exemple : « Bonjour **Ann F.**, merci d'avoir acheté ce **sac à dos rouge de taille moyenne** pour **40,00 $** ! Merci d'avoir fait vos achats chez **Backpack Locker** ! »

Si vous souhaitez enregistrer, stocker et suivre les propriétés pour segmenter, vous devez les configurer comme attributs personnalisés. Pour ce faire, vous pouvez utiliser les [Extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension/), qui vous permettent de cibler les utilisateurs en fonction d'un événement personnalisé ou d'un comportement d'achat stocké pendant toute la durée de vie de ce profil utilisateur.