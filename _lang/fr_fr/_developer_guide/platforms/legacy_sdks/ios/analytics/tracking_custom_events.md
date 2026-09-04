---
nav_title: Suivre les événements personnalisés
article_title: Suivi des événements personnalisés pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence explique comment ajouter et suivre des événements personnalisés pour votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Suivre les événements personnalisés pour iOS {#track-custom-events-for-ios}

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d'utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord.

Avant le déploiement, n'oubliez pas de consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [bonnes pratiques]({{site.baseurl}}/developer_guide/analytics), ainsi que nos notes sur les [conventions d'appellation des événements]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

## Ajout d'un événement personnalisé {#adding-a-custom-event}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("YOUR_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### Ajout de propriétés {#adding-properties}

Vous pouvez ajouter des métadonnées aux événements personnalisés en passant un `NSDictionary` contenant des valeurs `NSNumber`, `NSString` ou `NSDate`.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR-EVENT-NAME"
                         withProperties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent(
  "YOUR-EVENT-NAME",
  withProperties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```

{% endtab %}
{% endtabs %}

Consultez notre [documentation de classe](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79) pour plus d'informations.

### Clés réservées {#event-reserved-keys}

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d'événement personnalisé :

- `time`
- `event_name`

## Ressources supplémentaires {#additional-resources}

- Consultez la déclaration de la méthode dans le [fichier](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.
- Reportez-vous à la documentation de [`logCustomEvent`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa) pour plus d'informations.