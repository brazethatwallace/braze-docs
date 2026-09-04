---
nav_title: Définir des attributs personnalisés
article_title: Définir des attributs personnalisés pour Windows Universal
platform: Windows Universal
page_order: 3
description: "Cet article de référence explique comment définir des attributs personnalisés sur la plateforme Windows Universal."
hidden: true
---

# Définir des attributs personnalisés {#set-custom-attributes}
{% multi_lang_include archive/windows_deprecation.md %}

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs depuis le tableau de bord.

Avant de procéder à l'implémentation, pensez à consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [bonnes pratiques]({{site.baseurl}}/developer_guide/analytics#best-practices).

Les attributs utilisateur peuvent être attribués au `IAppboyUser` actuel. Pour obtenir une référence au `IAppboyUser` actuel, appelez `Appboy.SharedInstance.AppboyUser`.

## Affecter des attributs utilisateur par défaut {#assigning-default-user-attributes}

Les attributs suivants doivent être définis en tant que propriétés de l'objet `IAppboyUser` :

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**Exemple de mise en œuvre**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## Affecter des attributs utilisateur personnalisés {#assigning-custom-user-attributes}

Au-delà des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés à l'aide de différents types de données. Pour plus d'informations sur les options de segmentation et l'impact de chacun de ces attributs, consultez nos [bonnes pratiques]({{site.baseurl}}/hidden/archive_docs/windows_universal/analytics/setting_user_ids#user-id-integration-best-practices-and-notes).

### Définir des valeurs d'attribut personnalisé {#setting-custom-attribute-values}

{% tabs %}
{% tab Boolean %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab Integer %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab Double or Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze traite les valeurs FLOAT et DOUBLE exactement de la même manière dans sa base de données.
{% endtab %}
{% tab String %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab Date %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Les dates transmises à Braze doivent être au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601), par exemple `2013-07-16T19:20:30+01:00`, ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`, par exemple `2016-12-14T13:32:31.601-0800`
{% endtab %}
{% tab Array %}
```csharp
// Setting a custom attribute with an array value
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### Incrémenter/décrémenter des attributs personnalisés {#incrementingdecrementing-custom-attributes}

Ce code est un exemple d'incrémentation d'un attribut personnalisé. Vous pouvez incrémenter la valeur d'un attribut personnalisé par n'importe quelle valeur entière positive ou négative.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Annuler la définition d'un attribut personnalisé {#unsetting-a-custom-attribute}

Les attributs personnalisés peuvent également être réinitialisés à l'aide de la méthode suivante :

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Définir un attribut personnalisé via la REST API {#setting-a-custom-attribute-via-the-rest-api}

Vous pouvez également utiliser notre REST API pour définir des attributs utilisateur. Consultez la documentation de l'[API utilisateurs]({{site.baseurl}}/api/endpoints/user_data) pour plus de détails.

### Limites de valeur des attributs personnalisés {#custom-attribute-value-limits}

Les valeurs des attributs personnalisés ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.

## Gestion des statuts d'abonnement aux notifications {#managing-notification-subscription-statuses}

Pour configurer un abonnement pour vos utilisateurs (e-mail ou notification push), vous pouvez définir les statuts d'abonnement suivants en tant que propriétés de `IAppboyUser`. Les statuts d'abonnement dans Braze comportent trois états différents pour les e-mails et les notifications push :

| Statut d'abonnement | Définition |
| ------------------- | ---------- |
| `OptedIn` | Abonné, et explicitement inscrit |
| `Subscribed` | Abonné, mais pas explicitement inscrit |
| `UnSubscribed` | Désabonné et/ou explicitement désinscrit |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestion des statuts d'abonnement aux notifications" }

- `EmailNotificationSubscriptionType`
  - Les utilisateurs seront automatiquement définis sur `Subscribed` dès réception d'une adresse e-mail valide. Cependant, nous vous recommandons de mettre en place un processus d'abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur.
- `PushNotificationSubscriptionType`
  - Les utilisateurs seront automatiquement définis sur `Subscribed` dès un enregistrement push valide. Cependant, nous vous recommandons de mettre en place un processus d'abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur.

>  Ces types appartiennent à `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Consultez [Gestion des abonnements utilisateur]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) pour plus de détails.