---
nav_title: Enregistrer les achats
article_title: Enregistrer les achats pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence montre comment suivre les achats et les chiffres d'affaires in-app et attribuer des propriétés d'achat dans votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Enregistrer les achats pour iOS {#log-purchases-for-ios}

Enregistrez les achats in-app afin de pouvoir suivre vos chiffres d'affaires au fil du temps et selon les différentes sources, tout en segmentant vos utilisateurs par leur valeur vie client.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu'USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant le déploiement, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques]({{site.baseurl}}/developer_guide/analytics), ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

## Suivi des achats et du chiffre d'affaires {#tracking-purchases-and-revenue}

Pour utiliser cette fonctionnalité, ajoutez cet appel de méthode après un achat réussi dans votre application :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"))
```

{% endtab %}
{% endtabs %}

- Les symboles de devises pris en charge incluent : USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK, et bien d'autres.
  - Tout autre symbole de devise fourni générera un avertissement dans les logs, sans autre action de la part du SDK.
- L'identifiant du produit peut contenir au maximum 255 caractères.
- Notez que si l'identifiant du produit est vide, l'achat ne sera pas enregistré dans Braze.

### Ajout de propriétés {#properties-purchases}

Vous pouvez ajouter des métadonnées sur les achats en transmettant un [tableau de propriétés d'événement]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties#nested-objects) ou en transmettant un `NSDictionary` rempli de valeurs `NSNumber`, `NSString` ou `NSDate`.

Consultez la [documentation des classes iOS](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc) pour plus de détails.

### Ajout de quantité {#adding-quantity}
Vous pouvez ajouter une quantité à vos achats si les clients effectuent le même achat plusieurs fois au cours d'une même transaction. Pour ce faire, transmettez un `NSUInteger` pour la quantité.

* La valeur de la quantité doit être comprise entre [0, 100] pour que le SDK enregistre un achat.
* Les méthodes sans paramètre de quantité ont une valeur par défaut de 1.
* Les méthodes avec un paramètre de quantité n'ont pas de valeur par défaut et **doivent** recevoir une quantité pour que le SDK enregistre un achat.

Consultez la [documentation des classes iOS](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa) pour plus de détails.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]
withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"), withProperties: ["key1":"value1"])
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Si vous transmettez une valeur de 10 USD et une quantité de 3, cela sera enregistré dans le profil de l'utilisateur comme trois achats de 10 dollars, pour un total de 30 dollars.
{% endalert %}

### Enregistrer les achats au niveau de la commande {#log-purchases-at-the-order-level}
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de la commande comme `product_id`. Consultez notre [spécification de l'objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions) pour en savoir plus.

### Clés réservées {#reserved-keys}

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d'achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

Vous pouvez également utiliser notre REST API pour enregistrer des achats. Consultez la [documentation de l'API utilisateur]({{site.baseurl}}/api/endpoints/user_data) pour plus de détails.