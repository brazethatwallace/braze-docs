{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Attributs par défaut de l'utilisateur {#default-user-attributes}

### Méthodes prédéfinies {#predefined-methods}

Braze fournit des méthodes prédéfinies pour définir les attributs utilisateur suivants à l'aide de l'objet `BrazeBinding`. Pour en savoir plus, consultez le [fichier de déclaration Braze Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- Prénom
- Nom
- E-mail de l'utilisateur
- Genre
- Date de naissance
- Pays de l'utilisateur
- Ville d'origine de l'utilisateur
- Abonnement e-mail de l'utilisateur
- Abonnement aux notifications push de l'utilisateur
- Numéro de téléphone de l'utilisateur

### Définition des attributs par défaut {#setting-default-attributes}

Pour définir un attribut par défaut, appelez la méthode correspondante sur l'objet `BrazeBinding`.

{% tabs local %}
{% tab Prénom %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Nom %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab E-mail %}
```csharp
BrazeBinding.SetUserEmail("user@example.com");
```
{% endtab %}
{% tab Genre %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Date de naissance %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab Pays %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Ville d'origine %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Abonnement e-mail %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Abonnement push %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Numéro de téléphone %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### Suppression des attributs par défaut {#unsetting-default-attributes}

Pour supprimer un attribut par défaut de l'utilisateur, passez `null` à la méthode correspondante.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Attributs utilisateur personnalisés {#custom-user-attributes}

En plus des attributs par défaut, Braze vous permet également de définir des attributs personnalisés à l'aide de plusieurs types de données. Pour plus d'informations sur les options de segmentation de chaque attribut, consultez la section [Collecte de données utilisateur]({{site.baseurl}}/developer_guide/analytics).

### Définition des attributs personnalisés {#setting-custom-attributes}

Pour définir un attribut personnalisé, utilisez la méthode correspondant au type d'attribut :

{% tabs %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Integer %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Float %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom float attribute key", 'float value');
```

{% endtab %}

{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab Boolean %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Les dates transmises à Braze doivent être au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (tel que `2013-07-16T19:20:30+01:00`) ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (tel que `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}

{% tab Array %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}

{% tab Objets imbriqués %}

Vous pouvez définir des attributs personnalisés contenant des objets imbriqués (disponible dans le SDK Unity 5.1.0 et versions ultérieures). Pour plus d'informations, consultez la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).
Les exemples suivants montrent comment définir un attribut d'objet imbriqué, fusionner des mises à jour dans un objet existant et définir un tableau d'objets imbriqués.

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>));
```

Pour mettre à jour un objet imbriqué existant, utilisez le paramètre de fusion :

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>), merge(bool));
```

Vous pouvez également définir un tableau d'objets imbriqués :

```csharp
AppboyBinding.SetCustomUserAttribute("custom object array attribute key", list(List<Dictionary<string, object>>));
```

{% endtab %}
{% endtabs %}

{% alert important %}
Les valeurs des attributs personnalisés ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.
{% endalert %}

### Suppression des attributs personnalisés {#unsetting-custom-attributes}

Pour supprimer un attribut personnalisé, transmettez la clé d'attribut correspondante à la méthode `UnsetCustomUserAttribute`.

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Utilisation de la REST API {#using-the-rest-api}

Vous pouvez également utiliser notre REST API pour définir ou supprimer des attributs utilisateur. Pour plus d'informations, consultez la section [Endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Définir les abonnements des utilisateurs {#setting-user-subscriptions}

Pour configurer un abonnement e-mail ou notification push pour vos utilisateurs, appelez l'une des fonctions suivantes.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Les deux fonctions prennent `Appboy.Models.AppboyNotificationSubscriptionType` comme argument, qui possède trois états différents :

| Statut d'abonnement | Définition |
| ------------------- | ---------- |
| `OPTED_IN` | Abonné et explicitement inscrit |
| `SUBSCRIBED` | Abonné, mais pas explicitement inscrit |
| `UNSUBSCRIBED` | Désabonné et/ou explicitement désinscrit |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définir les abonnements des utilisateurs" }

{% alert note %}
Aucun abonnement explicite n'est requis par Windows pour envoyer des notifications push aux utilisateurs. Lorsqu'un utilisateur est enregistré pour les notifications push, il est défini sur `SUBSCRIBED` plutôt que sur `OPTED_IN` par défaut. Pour en savoir plus, consultez notre documentation sur [la mise en œuvre des abonnements et des inscriptions explicites]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions).
{% endalert %}

| Type d'abonnement                        | Description |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Les utilisateurs seront automatiquement définis sur `SUBSCRIBED` à la réception d'une adresse e-mail valide. Cependant, nous vous recommandons de mettre en place un processus d'inscription explicite et de définir cette valeur sur `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Consultez notre documentation sur la [modification des abonnements des utilisateurs]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions) pour plus de détails. |
| `PushNotificationSubscriptionType`       | Les utilisateurs seront automatiquement définis sur `SUBSCRIBED` lors d'un enregistrement push valide. Cependant, nous vous recommandons de mettre en place un processus d'inscription explicite et de définir cette valeur sur `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Consultez notre documentation sur la [modification des abonnements des utilisateurs]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions) pour plus de détails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définir les abonnements des utilisateurs" }

{% alert note %}
Ces types relèvent de `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Définir les abonnements e-mail {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Définir les abonnements aux notifications push {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
