{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Attributs par défaut de l'utilisateur {#default-user-attributes}

### Méthodes prédéfinies {#predefined-methods}

Braze propose des méthodes prédéfinies pour définir les attributs utilisateur suivants à l'aide de l'objet `BrazeBinding`. Pour plus d'informations, consultez le [fichier de déclaration de Braze Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- Prénom
- Nom
- Adresse e-mail de l'utilisateur
- Genre
- Date de naissance
- Pays de l'utilisateur
- Ville de résidence de l'utilisateur
- Abonnement de l'utilisateur aux e-mails
- Abonnement de l'utilisateur aux notifications push
- Numéro de téléphone de l'utilisateur

### Définition des attributs par défaut {#setting-default-attributes}

Pour définir un attribut par défaut, appelez la méthode correspondante sur l'objet `BrazeBinding`.

{% tabs local %}
{% tab First name %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Last name %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab Email %}
```csharp
BrazeBinding.SetUserEmail("user@example.com");
```
{% endtab %}
{% tab Gender %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Birth date %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab Country %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Home city %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Email subscription %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Push subscription %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Phone number %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### Réinitialisation des attributs par défaut {#unsetting-default-attributes}

Pour réinitialiser un attribut par défaut de l'utilisateur, passez `null` à la méthode correspondante.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Attributs utilisateur personnalisés {#custom-user-attributes}

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données. Pour plus d'informations sur les options de segmentation de chaque attribut, consultez [Collecte de données utilisateur]({{site.baseurl}}/developer_guide/analytics).

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
Les dates transmises à Braze doivent être au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (par exemple `2013-07-16T19:20:30+01:00`) ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (par exemple `2016-12-14T13:32:31.601-0800`).
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
{% endtabs %}

{% alert important %}
Les valeurs d'attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.
{% endalert %}

### Suppression des attributs personnalisés {#unsetting-custom-attributes}

Pour supprimer un attribut personnalisé, transmettez la clé de l'attribut concerné à la méthode `UnsetCustomUserAttribute`.

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Utiliser la REST API {#using-the-rest-api}

Vous pouvez également utiliser la REST API pour définir ou supprimer les attributs des utilisateurs. Pour plus d'informations, reportez-vous aux [endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Configurer les abonnements des utilisateurs {#setting-user-subscriptions}

Pour configurer un abonnement e-mail ou push pour vos utilisateurs, appelez l'une des fonctions suivantes.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Les deux fonctions prennent comme argument `Appboy.Models.AppboyNotificationSubscriptionType`, qui comporte trois états différents :

| État de l'abonnement | Définition |
| ------------------- | ---------- |
| `OPTED_IN` | Abonné et explicitement inscrit |
| `SUBSCRIBED` | Abonné, mais pas explicitement inscrit |
| `UNSUBSCRIBED` | Désabonné et/ou explicitement désinscrit |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurer les abonnements des utilisateurs" }

{% alert note %}
Windows ne requiert aucun abonnement explicite pour envoyer des notifications push aux utilisateurs. Lorsqu'un utilisateur est enregistré pour les notifications push, il est défini sur `SUBSCRIBED` plutôt que `OPTED_IN` par défaut. Pour en savoir plus, consultez notre documentation sur [l'implémentation des abonnements et des inscriptions explicites]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions).
{% endalert %}

| Type d'abonnement | Description |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType` | Les utilisateurs sont automatiquement définis sur `SUBSCRIBED` à la réception d'une adresse e-mail valide. Nous vous recommandons toutefois de mettre en place un processus d'inscription explicite et de définir cette valeur sur `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez notre documentation [Modification des abonnements utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions). |
| `PushNotificationSubscriptionType` | Les utilisateurs sont automatiquement définis sur `SUBSCRIBED` après une inscription valide aux notifications push. Nous vous recommandons toutefois de mettre en place un processus d'inscription explicite et de définir cette valeur sur `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez notre documentation [Modification des abonnements utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurer les abonnements des utilisateurs" }

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
