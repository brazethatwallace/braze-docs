{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Standard-Nutzerattribute {#default-user-attributes}

### Vordefinierte Methoden {#predefined-methods}

Braze stellt vordefinierte Methoden zur Verfügung, um die folgenden Nutzerattribute mithilfe des `BrazeBinding`-Objekts festzulegen. Weitere Informationen finden Sie in der [Braze Unity-Deklarationsdatei](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- Vorname
- Nachname
- E-Mail-Adresse
- Geschlecht
- Geburtsdatum
- Land
- Heimatort
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
BrazeBinding.SetUserEmail("email@email.com");
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

Zusätzlich zu den Standard-Nutzerattributen ermöglicht Braze auch die Definition angepasster Attribute mit verschiedenen Datentypen. Weitere Informationen zu den Segmentierungsoptionen der einzelnen Attribute finden Sie unter [Datenerfassung]({{site.baseurl}}/developer_guide/analytics/).

### Angepasste Attribute festlegen {#setting-custom-attributes}

Um ein angepasstes Attribut festzulegen, verwenden Sie die entsprechende Methode für den jeweiligen Attributtyp:

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
Datumsangaben, die an Braze übergeben werden, müssen entweder im [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)-Format (z. B. `2013-07-16T19:20:30+01:00`) oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (z. B. `2016-12-14T13:32:31.601-0800`) vorliegen.
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
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.
{% endalert %}

### Angepasste Attribute zurücksetzen {#unsetting-custom-attributes}

Um ein angepasstes Attribut zurückzusetzen, übergeben Sie den entsprechenden Attributschlüssel an die Methode `UnsetCustomUserAttribute`.

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### REST API verwenden {#using-the-rest-api}

Sie können auch unsere REST API verwenden, um Nutzerattribute zu setzen oder zu entfernen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Abos für Nutzer:innen einrichten {#setting-user-subscriptions}

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
| `UNSUBSCRIBED` | Abgemeldet und/oder ausdrücklich abbestellt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abos für Nutzer:innen einrichten" }

{% alert note %}
Unter Windows ist kein explizites Opt-in erforderlich, um Nutzer:innen Push-Benachrichtigungen zu senden. Wenn Nutzer:innen für Push registriert sind, werden sie standardmäßig auf `SUBSCRIBED` statt auf `OPTED_IN` gesetzt. Mehr erfahren Sie in unserer Dokumentation zur [Implementierung von Abos und expliziten Opt-ins]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

| Abo-Typ | Beschreibung |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType` | Nutzer:innen werden beim Empfang einer gültigen E-Mail-Adresse automatisch auf `SUBSCRIBED` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert auf `OPTED_IN` zu setzen, sobald Sie die ausdrückliche Zustimmung erhalten haben. Weitere Details finden Sie in unserer Dokumentation zum [Ändern von Nutzer-Abos]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions). |
| `PushNotificationSubscriptionType` | Nutzer:innen werden bei einer gültigen Push-Registrierung automatisch auf `SUBSCRIBED` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert auf `OPTED_IN` zu setzen, sobald Sie die ausdrückliche Zustimmung erhalten haben. Weitere Details finden Sie in unserer Dokumentation zum [Ändern von Nutzer-Abos]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abos für Nutzer:innen einrichten" }

{% alert note %}
Diese Typen gehören zu `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### E-Mail-Abos einrichten {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Push-Benachrichtigungs-Abos einrichten {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
