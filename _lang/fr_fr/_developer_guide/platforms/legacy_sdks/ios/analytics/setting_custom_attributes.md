---
nav_title: Définir des attributs personnalisés
article_title: Définir des attributs personnalisés pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence montre comment définir des attributs personnalisés dans votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Définir des attributs personnalisés pour iOS {#set-custom-attributes-for-ios}

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs depuis le tableau de bord.

Avant de procéder à l'implémentation, pensez à consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [bonnes pratiques]({{site.baseurl}}/developer_guide/analytics), ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

## Affecter des attributs utilisateur par défaut {#assigning-default-user-attributes}

Pour affecter des attributs utilisateur, vous devez définir le champ approprié sur l'objet partagé `ABKUser`.

Voici un exemple de définition de l'attribut prénom :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

Les attributs suivants doivent être définis sur l'objet `ABKUser` :

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `userID`
- `gender`

## Affecter des attributs utilisateur personnalisés {#assigning-custom-user-attributes}

En plus des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés en utilisant plusieurs types de données différents. Consultez notre documentation sur la [collecte de données utilisateur]({{site.baseurl}}/developer_guide/analytics) pour plus d'informations sur les options de segmentation offertes par chacun de ces attributs.

### Attribut personnalisé avec une valeur de chaîne de caractères {#custom-attribute-with-a-string-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur entière {#custom-attribute-with-an-integer-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur double {#custom-attribute-with-a-double-value}

Braze traite les valeurs `float` et `double` de la même manière dans sa base de données.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur booléenne {#custom-attribute-with-a-boolean-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur de date {#custom-attribute-with-a-date-value}

Les dates transmises à Braze avec cette méthode doivent être au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (par exemple `2013-07-16T19:20:30+01:00`) ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (`2016-12-14T13:32:31.601-0800`).

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur de tableau {#custom-attribute-with-an-array-value}

Le nombre maximum d'éléments par défaut dans un tableau est de 500. Vous pouvez modifier le nombre maximum d'éléments dans le tableau de bord de Braze, sous **Paramètres des données** > **Attributs personnalisés**. Les tableaux dépassant le nombre maximum d'éléments sont tronqués pour ne contenir que le nombre maximum d'éléments.


{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[[Appboy sharedInstance].user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
Appboy.sharedInstance()?.user.setCustomAttributeArrayWithKey("array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
Appboy.sharedInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Removing a value from an array type custom attribute
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", value: "value2")
```

{% endtab %}
{% endtabs %}

### Supprimer un attribut personnalisé {#unsetting-a-custom-attribute}

Les attributs personnalisés peuvent également être supprimés à l'aide de la méthode suivante :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### Incrémenter/décrémenter des attributs personnalisés {#incrementingdecrementing-custom-attributes}

Ce code est un exemple d'incrémentation d'un attribut personnalisé. Vous pouvez incrémenter la valeur d'un attribut personnalisé par n'importe quelle valeur entière ou longue, positive ou négative :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### Définir un attribut personnalisé via la REST API {#setting-a-custom-attribute-via-the-rest-api}

Vous pouvez également utiliser notre REST API pour définir des attributs utilisateur. Consultez la [documentation de l'API utilisateur]({{site.baseurl}}/api/endpoints/user_data) pour plus de détails.

### Limites de valeur des attributs personnalisés {#custom-attribute-value-limits}

Les valeurs des attributs personnalisés ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.

#### Informations complémentaires {#additional-information}

- Plus de détails sont disponibles dans le [fichier `ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Consultez la [documentation `ABKUser`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html) pour plus d'informations.

## Configurer les abonnements des utilisateurs {#setting-up-user-subscriptions}

Pour configurer un abonnement pour vos utilisateurs (e-mail ou notification push), appelez les fonctions `setEmailNotificationSubscriptionType` ou `setPushNotificationSubscriptionType`, respectivement. Ces deux fonctions prennent le type enum `ABKNotificationSubscriptionType` comme argument. Ce type possède trois états différents :

| Statut d'abonnement | Définition |
| ------------------- | ---------- |
| `ABKOptedin` | Abonné, et explicitement inscrit |
| `ABKSubscribed` | Abonné, mais pas explicitement inscrit |
| `ABKUnsubscribed` | Désabonné et/ou explicitement désinscrit |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurer les abonnements des utilisateurs" }

Les utilisateurs qui autorisent une application à leur envoyer des notifications push ont par défaut le statut `ABKOptedin`, car iOS exige un abonnement explicite.

Les utilisateurs seront automatiquement définis sur `ABKSubscribed` à la réception d'une adresse e-mail valide ; cependant, nous vous recommandons de mettre en place un processus d'abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur. Consultez [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/channels/email/subscriptions) pour plus de détails.

### Configurer les abonnements e-mail {#setting-email-subscriptions}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Configurer les abonnements aux notifications push {#setting-push-notification-subscriptions}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

Consultez [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/channels/email/subscriptions) pour plus de détails.