{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Standard-Nutzerattribute {#default-user-attributes}

### Vordefinierte Methoden {#predefined-methods}

Braze stellt vordefinierte Methoden zur Verfügung, um die folgenden Nutzerattribute mithilfe des `BrazeBinding`-Objekts festzulegen. Weitere Informationen finden Sie in der [Braze Unity-Deklarationsdatei](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Land
- Wohnort
- E-Mail-Abo
- Push-Abo
- Telefonnummer

### Standardattribute festlegen {#setting-default-attributes}

Um ein Standardattribut festzulegen, rufen Sie die entsprechende Methode auf dem `BrazeBinding`-Objekt auf.

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

### Standardattribute zurücksetzen {#unsetting-default-attributes}

Um ein Standardattribut zurückzusetzen, übergeben Sie `null` an die entsprechende Methode.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Angepasste Nutzerattribute {#custom-user-attributes}

Zusätzlich zu den Standardattributen ermöglicht Braze auch die Definition angepasster Attribute mit verschiedenen Datentypen. Weitere Informationen zu den Segmentierungsoptionen der einzelnen Attribute finden Sie unter [Nutzerdatenerfassung]({{site.baseurl}}/developer_guide/analytics).

### Angepasste Attribute festlegen {#setting-custom-attributes}

Um ein angepasstes Attribut festzulegen, verwenden Sie die entsprechende Methode für den Attributtyp:

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
An Braze übergebene Datumsangaben müssen entweder im [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601)-Format (z. B. `2013-07-16T19:20:30+01:00`) oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (z. B. `2016-12-14T13:32:31.601-0800`) vorliegen.
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

{% tab Verschachtelte Objekte %}

Sie können angepasste Attribute mit verschachtelten Objekten festlegen (verfügbar ab Unity SDK 5.1.0). Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).
Die folgenden Beispiele zeigen, wie Sie ein verschachteltes Objektattribut festlegen, Aktualisierungen in ein bestehendes Objekt zusammenführen und ein Array verschachtelter Objekte festlegen.

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>));
```

Um ein bestehendes verschachteltes Objekt zu aktualisieren, verwenden Sie den Merge-Parameter:

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>), merge(bool));
```

Sie können auch ein Array verschachtelter Objekte festlegen:

```csharp
AppboyBinding.SetCustomUserAttribute("custom object array attribute key", list(List<Dictionary<string, object>>));
```

{% endtab %}
{% endtabs %}

{% alert important %}
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.
{% endalert %}

### Angepasste Attribute zurücksetzen {#unsetting-custom-attributes}

Um ein angepasstes Attribut zurückzusetzen, übergeben Sie den entsprechenden Attributschlüssel an die Methode `UnsetCustomUserAttribute`.

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Verwendung der REST API {#using-the-rest-api}

Sie können auch unsere REST API verwenden, um Nutzerattribute festzulegen oder zurückzusetzen. Weitere Informationen finden Sie unter [Nutzerdaten-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Nutzer:innen-Abos festlegen {#setting-user-subscriptions}

Um ein E-Mail- oder Push-Abo für Ihre Nutzer:innen einzurichten, rufen Sie eine der folgenden Funktionen auf.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Beide Funktionen nehmen `Appboy.Models.AppboyNotificationSubscriptionType` als Argument entgegen, das drei verschiedene Zustände hat:

| Abo-Status | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Abonniert und ausdrücklich angemeldet |
| `SUBSCRIBED` | Abonniert, aber nicht ausdrücklich angemeldet |
| `UNSUBSCRIBED` | Abgemeldet und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen-Abos festlegen" }

{% alert note %}
Unter Windows ist kein ausdrückliches Opt-in erforderlich, um Nutzer:innen Push-Benachrichtigungen zu senden. Wenn eine Nutzer:in für Push registriert wird, wird sie standardmäßig auf `SUBSCRIBED` statt auf `OPTED_IN` gesetzt. Weitere Informationen finden Sie in unserer Dokumentation zum [Implementieren von Abos und ausdrücklichen Opt-ins]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions).
{% endalert %}

| Abo-Typ | Beschreibung |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType` | Nutzer:innen werden beim Erhalt einer gültigen E-Mail-Adresse automatisch auf `SUBSCRIBED` gesetzt. Wir empfehlen jedoch, einen ausdrücklichen Opt-in-Prozess einzurichten und diesen Wert bei ausdrücklicher Zustimmung Ihrer Nutzer:in auf `OPTED_IN` zu setzen. Weitere Details finden Sie in unserer Dokumentation zum [Ändern von Nutzer:innen-Abos]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions). |
| `PushNotificationSubscriptionType` | Nutzer:innen werden bei einer gültigen Push-Registrierung automatisch auf `SUBSCRIBED` gesetzt. Wir empfehlen jedoch, einen ausdrücklichen Opt-in-Prozess einzurichten und diesen Wert bei ausdrücklicher Zustimmung Ihrer Nutzer:in auf `OPTED_IN` zu setzen. Weitere Details finden Sie in unserer Dokumentation zum [Ändern von Nutzer:innen-Abos]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen-Abos festlegen" }

{% alert note %}
Diese Typen gehören zu `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### E-Mail-Abos festlegen {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Push-Benachrichtigungs-Abos festlegen {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
