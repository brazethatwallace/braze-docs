---
nav_title: Événements
article_title: Événements
page_order: 0
hidden: true
page_type: reference
description: "Cet article décrit les différents événements dans Braze — événements standard, événements d'achat et événements personnalisés — ainsi que leur utilité."
---

# Événements {#events}

> Cette page présente les différents événements dans Braze et leur utilité.

Braze utilise plusieurs types d'événements pour offrir une compréhension complète du comportement des utilisateurs et de leur engagement avec votre marque. Chaque type d'événement remplit un rôle spécifique :

- [Événements standard](#standard-events) : fournissent une compréhension de base de l'engagement des utilisateurs avec votre application ou votre site.
- [Événements d'achat](#purchase-events) : essentiels pour comprendre le comportement d'achat des utilisateurs et suivre le chiffre d'affaires.
- [Événements personnalisés](#custom-events) : offrent un aperçu plus approfondi des comportements utilisateurs propres à votre application ou à votre activité.

En suivant ces différents types d'événements, vous pouvez mieux comprendre vos utilisateurs, ce qui vous permet d'affiner vos stratégies marketing, d'optimiser votre application et de proposer une expérience utilisateur plus personnalisée. Voyons cela en détail !

## Événements standard {#standard-events}

Dans Braze, les événements standard sont des actions prédéfinies reconnues par la plateforme. Contrairement aux [événements personnalisés](#custom-events), vous n'avez pas besoin de créer ou de nommer les événements standard : ils sont intégrés nativement. Cependant, tous les événements standard ne sont pas suivis de la même manière.

Les événements suivants sont automatiquement suivis après l'intégration SDK :

- Début de session
- Fin de session

Les événements suivants nécessitent une configuration supplémentaire :

- [Événements d'achat](#purchase-events) : votre équipe de développement les enregistre à l'aide des méthodes d'achat du SDK. Pour en savoir plus, consultez la section Événements d'achat.
- Événements d'engagement e-mail (tels que les ouvertures d'e-mails et les clics sur les liens) : suivis par Braze lorsque vous configurez l'e-mail dans Braze et activez le suivi des e-mails.
- Événements d'engagement push (tels que les ouvertures et les clics sur les notifications push) : suivis après avoir configuré le push dans Braze et intégré la gestion du push avec le SDK Braze dans votre application.

En tant que marketeur, vous pouvez utiliser les événements standard pour comprendre le comportement et l'engagement des utilisateurs. Par exemple, les données de session montrent la fréquence à laquelle les utilisateurs ouvrent votre application ou votre site, tandis que les événements d'achat vous aident à suivre le chiffre d'affaires au fil du temps.

## Événements d'achat {#purchase-events}

Les événements d'achat enregistrent et suivent les achats effectués par vos utilisateurs. Après avoir intégré le SDK Braze, votre équipe de développement peut enregistrer les achats à l'aide des méthodes d'achat du SDK. Grâce aux événements d'achat, vous pouvez suivre votre chiffre d'affaires au fil du temps et selon différentes sources de revenus directement depuis Braze.

Les événements d'achat enregistrent les informations clés suivantes :

- ID du produit (généralement le nom ou la catégorie du produit)
- Devise
- Prix
- Quantité

Vous pouvez ensuite utiliser ces données pour segmenter vos utilisateurs en fonction de leur valeur vie client, de la fréquence d'achat, d'achats spécifiques, et bien plus encore.

Braze prend également en charge les achats dans plusieurs devises. Si un achat est enregistré dans une devise autre que l'USD, il sera affiché dans le tableau de bord de Braze en USD, sur la base du taux de change à la date à laquelle l'achat a été enregistré.

Pour en savoir plus, consultez notre article dédié aux [événements d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).

{% details Exemple d'implémentation %}

Notez que l'implémentation des événements d'achat nécessite des connaissances techniques, car elle implique l'intégration du SDK Braze avec votre application. Votre gestionnaire de la satisfaction client accompagnera votre équipe tout au long de ce processus dans le cadre de votre onboarding, mais voici les étapes générales :

1. **Intégrer le SDK Braze :** avant d'enregistrer un événement, vous devez intégrer le SDK Braze dans votre application.
2. **Enregistrer l'événement d'achat :** une fois le SDK intégré, vous pouvez enregistrer un événement d'achat chaque fois qu'un utilisateur effectue un achat dans votre application. Cela se fait généralement dans la fonction ou la méthode appelée lorsqu'un achat est finalisé.

Voici un exemple d'enregistrement d'un événement d'achat dans une application iOS avec Swift :

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

Dans cet exemple, "product_name" est le nom du produit acheté, "USD" est la devise de l'achat, "1.99" est le prix du produit et "1" est la quantité achetée.

{:start="3"}
3. **Consulter l'événement d'achat dans le tableau de bord de Braze :** une fois l'événement d'achat enregistré, vous pouvez le consulter dans le tableau de bord de Braze. Vous pouvez utiliser ces données pour analyser votre chiffre d'affaires, segmenter vos utilisateurs, et bien plus encore.

N'oubliez pas que l'implémentation exacte peut varier selon la plateforme (iOS, Android, Web) et les exigences spécifiques de votre application.

{% enddetails %}

## Événements personnalisés {#custom-events}

Les événements personnalisés sont des événements que vous définissez en fonction des actions spécifiques que vous souhaitez suivre dans votre application ou sur votre site. Braze ne les suit pas automatiquement : vous devez configurer manuellement ces événements dans votre implémentation du SDK Braze. Les événements personnalisés peuvent aller de la complétion d'un niveau dans un jeu à la mise à jour d'un profil utilisateur.

Voici un exemple d'enregistrement d'un événement personnalisé dans une application iOS avec Swift :

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

Dans cet exemple, "completed_level" est le nom de l'événement personnalisé enregistré lorsqu'un utilisateur termine un niveau dans un jeu. Cet événement personnalisé est ensuite enregistré dans le profil utilisateur dans Braze, ce qui vous permet de déclencher des campagnes et de personnaliser l'envoi de messages.

Pour en savoir plus, consultez notre article dédié aux [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events).

{% details Exemple d'implémentation %}

Comme pour les événements d'achat, les événements personnalisés nécessitent une configuration supplémentaire. Voici le processus général pour implémenter des événements personnalisés dans Braze :

1. **Intégrer le SDK Braze :** avant de pouvoir enregistrer un événement, vous devez intégrer le SDK Braze dans votre application.
2. **Définir votre événement personnalisé :** déterminez quelle action dans votre application vous souhaitez suivre en tant qu'événement personnalisé. Il peut s'agir de toute action significative pour votre application, comme la complétion d'un niveau dans un jeu, la mise à jour d'un profil ou un type d'achat spécifique.
3. **Enregistrer l'événement personnalisé :** une fois votre événement personnalisé défini, vous pouvez l'enregistrer dans le code de votre application. Cela se fait généralement dans la fonction ou la méthode appelée lorsque l'action se produit.

Voici un exemple d'enregistrement d'un événement personnalisé dans une application iOS avec Swift :

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

Dans cet exemple, "updated_profile" est le nom de l'événement personnalisé enregistré lorsqu'un utilisateur met à jour son profil.

{:start="4"}
4. **Ajouter des propriétés à votre événement personnalisé (facultatif) :** si vous souhaitez capturer des détails supplémentaires sur l'événement personnalisé, vous pouvez y ajouter des propriétés. Pour cela, passez un dictionnaire de propriétés lors de l'enregistrement de l'événement.

Voici un exemple d'enregistrement d'un événement personnalisé avec des propriétés dans une application iOS avec Swift :

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

Dans cet exemple, l'événement personnalisé possède une propriété appelée "Property Name" avec la valeur "Property Value".

{:start="5"}
5. **Consulter l'événement personnalisé dans le tableau de bord de Braze :** une fois l'événement personnalisé enregistré, vous pouvez le consulter dans le tableau de bord de Braze. Vous pouvez utiliser ces données pour analyser le comportement des utilisateurs, segmenter vos utilisateurs, et bien plus encore.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->