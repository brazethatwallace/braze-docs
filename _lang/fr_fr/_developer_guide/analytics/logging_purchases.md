---
nav_title: Enregistrer les achats
article_title: Enregistrer les achats via le SDK Braze
page_order: 3.2
description: "Découvrez comment enregistrer des achats via le SDK Braze."

---

# Enregistrer les achats {#log-purchases}

> Découvrez comment enregistrer les achats in-app via le SDK Braze, afin de pouvoir déterminer vos chiffres d'affaires au fil du temps et selon les différentes sources. Vous pourrez ainsi segmenter les utilisateurs [en fonction de leur valeur vie client]({{site.baseurl}}/developer_guide/analytics#purchase-events--revenue-tracking) à l'aide d'événements personnalisés, d'attributs personnalisés et d'événements d'achat.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

Toute devise autre que l'USD sera affichée dans Braze en USD, sur la base du taux de change en vigueur à la date de déclaration. Afin d'éviter toute conversion monétaire, définissez la devise en USD de manière fixe.

## Enregistrement des achats et des chiffres d'affaires {#logging-purchases-and-revenue}

Pour enregistrer les achats et les chiffres d'affaires, appelez `logPurchase()` après un achat réussi dans votre application. Si l'identifiant du produit est vide, l'achat ne sera pas enregistré dans Braze.

{% tabs %}
{% tab web %}
Pour une implémentation standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Si vous souhaitez utiliser Google Tag Manager à la place, vous pouvez utiliser le type d'étiquette **Purchase** pour appeler la [méthode `logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase). Utilisez cette étiquette pour suivre les achats dans Braze, en incluant éventuellement des propriétés d'achat. Pour ce faire :

1. Les champs **Product ID** et **Price** sont requis.
2. Utilisez le bouton **Add Row** pour ajouter des propriétés d'achat.

![Boîte de dialogue affichant les paramètres de configuration de l'étiquette d'action Braze. Les paramètres inclus sont « tag type », « external ID », « price », « currency code », « quantity » et « purchase properties ».]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab react native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab unity %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID` ne peut contenir plus de 255 caractères. De plus, si l'identifiant du produit est vide, l'achat ne sera pas enregistré dans Braze.
{% endalert %}

### Ajouter des propriétés {#adding-properties}

Vous pouvez ajouter des métadonnées sur les achats en transmettant un dictionnaire contenant des valeurs `Int`, `Double`, `String`, `Bool` ou `Date`.

{% tabs %}
{% tab web %}
Pour une implémentation standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Si votre site enregistre les achats à l'aide de l'élément de couche de données d'[événement e-commerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) standard dans Google Tag Manager, vous pouvez utiliser le type d'étiquette **E-commerce Purchase**. Ce type d'action enregistre un « achat » séparé dans Braze pour chaque article envoyé dans la liste de `items`.

Vous pouvez également spécifier des noms de propriétés supplémentaires à inclure comme propriétés d'achat en indiquant leurs clés dans la liste des propriétés d'achat. Notez que Braze recherchera dans l'`item` individuel en cours d'enregistrement toute propriété d'achat que vous ajoutez à la liste.

Par exemple, avec le payload e-commerce suivant :

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Si vous souhaitez transmettre uniquement `item_brand` et `item_name` comme propriétés d'achat, il vous suffit d'ajouter ces deux champs au tableau des propriétés d'achat. Si vous ne fournissez aucune propriété, aucune propriété d'achat ne sera envoyée dans l'appel [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) à Braze.
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
let purchaseProperties = ["key": "value"]
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price, properties: purchaseProperties)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
NSDictionary *purchaseProperties = @{@"key": @"value"};
[AppDelegate.braze logPurchase:@"product_id"
                      currency:@"USD"
                         price:price
                   properties:purchaseProperties];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab react native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

{% endtab %}

{% tab unity %}

```csharp
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
    { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);
```

{% endtab %}
{% endtabs %}

### Ajouter une quantité {#adding-quantity}

Par défaut, `quantity` est défini sur `1`. Toutefois, vous pouvez ajouter une quantité à vos achats si les clients effectuent le même achat plusieurs fois lors d'un même passage en caisse. Pour ajouter une quantité, transmettez une valeur `Int` à `quantity`.

### Utiliser la REST API {#using-the-rest-api}

Vous pouvez également utiliser notre REST API pour enregistrer les achats. Pour plus d'informations, consultez les [endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Enregistrement des commandes {#logging-orders}

Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, consultez les [spécifications de l'objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object#product-id-naming-conventions).

## Clés réservées {#reserved-keys}

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d'achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Devises prises en charge {#supported-currencies}

Braze prend en charge les symboles monétaires suivants. Tout autre symbole monétaire que vous fournissez génère un avertissement et l'achat n'est pas enregistré dans Braze.

- `AED`, `AFN`, `ALL`, `AMD`, `ANG`, `AOA`, `ARS`, `AUD`, `AWG`, `AZN`
- `BAM`, `BBD`, `BDT`, `BGN`, `BHD`, `BIF`, `BMD`, `BND`, `BOB`, `BRL`
- `BSD`, `BTC`, `BTN`, `BWP`, `BYR`, `BZD`
- `CAD`, `CDF`, `CHF`, `CLF`, `CLP`, `CNY`, `COP`, `CRC`, `CUC`, `CUP`, `CVE`, `CZK`
- `DJF`, `DKK`, `DOP`, `DZD`
- `EEK`, `EGP`, `ERN`, `ETB`, `EUR`
- `FJD`, `FKP`
- `GBP`, `GEL`, `GGP`, `GHS`, `GIP`, `GMD`, `GNF`, `GTQ`, `GYD`
- `HKD`, `HNL`, `HRK`, `HTG`, `HUF`
- `IDR`, `ILS`, `IMP`, `INR`, `IQD`, `IRR`, `ISK`
- `JEP`, `JMD`, `JOD`, `JPY`
- `KES`, `KGS`, `KHR`, `KMF`, `KPW`, `KRW`, `KWD`, `KYD`, `KZT`
- `LAK`, `LBP`, `LKR`, `LRD`, `LSL`, `LTL`, `LVL`, `LYD`
- `MAD`, `MDL`, `MGA`, `MKD`, `MMK`, `MNT`, `MOP`, `MRO`, `MTL`, `MUR`, `MVR`, `MWK`, `MXN`, `MYR`, `MZN`
- `NAD`, `NGN`, `NIO`, `NOK`, `NPR`, `NZD`
- `OMR`
- `PAB`, `PEN`, `PGK`, `PHP`, `PKR`, `PLN`, `PYG`
- `QAR`
- `RON`, `RSD`, `RUB`, `RWF`
- `SAR`, `SBD`, `SCR`, `SDG`, `SEK`, `SGD`, `SHP`, `SLL`, `SOS`, `SRD`, `STD`, `SVC`, `SYP`, `SZL`
- `THB`, `TJS`, `TMT`, `TND`, `TOP`, `TRY`, `TTD`, `TWD`, `TZS`
- `UAH`, `UGX`, `USD`, `UYU`, `UZS`
- `VEF`, `VND`, `VUV`
- `WST`
- `XAF`, `XAG`, `XAU`, `XCD`, `XDR`, `XOF`, `XPD`, `XPF`, `XPT`
- `YER`
- `ZAR`, `ZMK`, `ZMW`, `ZWL`