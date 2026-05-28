{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Attributs par défaut de l'utilisateur {#default-user-attributes}

### Méthodes prédéfinies {#predefined-methods}

Braze propose des méthodes prédéfinies pour définir les attributs utilisateur suivants à l'aide de l'objet `m.Braze`.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### Définition des attributs par défaut {#setting-default-attributes}

Pour définir un attribut par défaut, appelez la méthode correspondante sur l'objet `m.Braze`.

{% tabs local %}
{% tab First name %}
```brightscript
m.Braze.setFirstName("Alex")
```
{% endtab %}
{% tab Last name %}
```brightscript
m.Braze.setLastName("Smith")
```
{% endtab %}
{% tab Email %}
```brightscript
m.Braze.setEmail("alex@example.com")
```
{% endtab %}
{% tab Gender %}
```brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```
{% endtab %}
{% tab Birth date %}
```brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```
{% endtab %}
{% tab Country %}
```brightscript
m.Braze.setCountry("United States")
```
{% endtab %}
{% tab Language %}
```brightscript
m.Braze.setLanguage("en")
```
{% endtab %}
{% tab Home city %}
```brightscript
m.Braze.setHomeCity("New York")
```
{% endtab %}
{% tab Phone number %}
```brightscript
m.Braze.setPhoneNumber("+1234567890")
```
{% endtab %}
{% endtabs %}

## Attributs utilisateur personnalisés {#custom-user-attributes}

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données.

### Définition des attributs personnalisés {#settings-custom-attributes}

{% tabs %}
{% tab String %}
Pour définir un attribut personnalisé avec une valeur `string` :

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Integer %}
Pour définir un attribut personnalisé avec une valeur `integer` :

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Floating-points %}
Braze traite les valeurs `float` et `double` exactement de la même manière. Pour définir un attribut personnalisé avec l'une ou l'autre valeur :

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Boolean %}
Pour définir un attribut personnalisé avec une valeur `boolean` :

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Date %}
Pour définir un attribut personnalisé avec une valeur `date` :

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Array %}
Pour définir un attribut personnalisé avec une valeur `array` :

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
Les valeurs d'attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.
{% endalert %}

### Incrémentation et décrémentation des attributs personnalisés {#incrementing-and-decrementing-custom-attributes}

Ce code est un exemple d'incrémentation d'un attribut personnalisé. Vous pouvez augmenter la valeur d'un attribut personnalisé par n'importe quelle valeur entière positive ou négative.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Suppression des attributs personnalisés {#unsetting-custom-attributes}

Pour supprimer un attribut personnalisé, transmettez la clé de l'attribut concerné à la méthode `unsetCustomAttribute`.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Utiliser la REST API {#using-the-rest-api}

Vous pouvez également utiliser notre REST API pour définir ou supprimer les attributs des utilisateurs. Pour plus d'informations, reportez-vous aux [endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Définir les abonnements par e-mail {#setting-email-subscriptions}

Vous pouvez définir les statuts d'abonnement aux e-mails suivants pour vos utilisateurs par programmation via le SDK.

| Statut d'abonnement | Définition |
| ------------------- | ---------- |
| `OptedIn` | Abonné et explicitement inscrit |
| `Subscribed` | Abonné, mais pas explicitement inscrit |
| `UnSubscribed` | Désabonné et/ou explicitement désinscrit |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Ces types relèvent de `BrazeConstants().SUBSCRIPTION_STATES`.
{% endalert %}

La méthode de définition du statut d'abonnement aux e-mails est `setEmailSubscriptionState()`. Les utilisateurs seront automatiquement définis sur `Subscribed` dès réception d'une adresse e-mail valide. Cependant, nous vous suggérons d'établir un processus d'abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez la page [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```
