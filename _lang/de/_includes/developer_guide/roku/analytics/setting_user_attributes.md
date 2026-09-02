{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Standard-Nutzerattribute {#default-user-attributes}

### Vordefinierte Methoden {#predefined-methods}

Braze bietet vordefinierte Methoden zum Festlegen der folgenden Nutzer:innen-Attribute unter Verwendung des `m.Braze`-Objekts.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### Standardattribute festlegen {#setting-default-attributes}

Um ein Standardattribut festzulegen, rufen Sie die entsprechende Methode für das `m.Braze`-Objekt auf.

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

## Angepasste Nutzerattribute {#custom-user-attributes}

Zusätzlich zu den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung verschiedener Datentypen definieren.

### Angepasste Attribute festlegen {#settings-custom-attributes}

{% tabs %}
{% tab String %}
So legen Sie für ein angepasstes Attribut einen `string`-Wert fest:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Integer %}
So legen Sie ein angepasstes Attribut mit einem `integer`-Wert fest:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Floating-points %}
Braze behandelt die Werte von `float` und `double` genau gleich. So legen Sie ein angepasstes Attribut mit einem der beiden Werte fest:

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Boolean %}
So legen Sie ein angepasstes Attribut mit einem `boolean`-Wert fest:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Date %}
So legen Sie ein angepasstes Attribut mit einem `date`-Wert fest:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Array %}
So legen Sie ein angepasstes Attribut mit einem `array`-Wert fest:

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
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.
{% endalert %}

### Inkrementieren und Dekrementieren von angepassten Attributen {#incrementing-and-decrementing-custom-attributes}

Dieser Code ist ein Beispiel für ein inkrementierendes angepasstes Attribut. Sie können den Wert eines angepassten Attributs um jeden positiven oder negativen ganzzahligen Wert erhöhen.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Angepasste Attribute zurücksetzen {#unsetting-custom-attributes}

Um ein angepasstes Attribut zurückzusetzen, übergeben Sie den entsprechenden Attributschlüssel an die Methode `unsetCustomAttribute`.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Verwendung der Representational State Transfer API {#using-the-rest-api}

Sie können auch unsere Representational State Transfer API verwenden, um Nutzer:innen-Attribute zu setzen oder zu löschen. Weitere Informationen finden Sie unter [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## E-Mail-Abonnements einstellen {#setting-email-subscriptions}

Sie können die folgenden E-Mail-Abo-Status für Ihre Nutzer:innen programmatisch über das SDK or Software-Development-Kit einstellen.

| Abostatus | Definition |
| ------------------- | ---------- |
| `OptedIn` | Abonniert und ausdrücklich angemeldet |
| `Subscribed` | Abonniert, aber nicht explizit angemeldet |
| `UnSubscribed` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Diese Typen fallen unter `BrazeConstants().SUBSCRIPTION_STATES`.
{% endalert %}

Die Methode zum Einstellen des E-Mail-Abo-Status lautet `setEmailSubscriptionState()`. Nutzer:innen werden bei Erhalt einer gültigen E-Mail-Adresse automatisch auf `Subscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein explizites Opt-in-Verfahren einzurichten und diesen Wert bei Erhalt einer ausdrücklichen Zustimmung Ihrer Nutzer:innen auf `OptedIn` zu setzen. Weitere Informationen finden Sie unter [Verwalten von Nutzer:innen-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```
