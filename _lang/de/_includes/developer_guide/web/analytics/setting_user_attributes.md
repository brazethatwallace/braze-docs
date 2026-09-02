{% multi_lang_include developer_guide/prerequisites/web.md %}

## Standard-Nutzerattribute {#default-user-attributes}

### Vordefinierte Methoden {#predefined-methods}

Braze bietet vordefinierte Methoden zum Festlegen der folgenden Nutzer:innen-Attribute innerhalb der [`User`-Klasse](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html):

- Vorname
- Nachname
- Sprache
- Land
- Geburtsdatum
- E-Mail
- Geschlecht
- Heimatstadt
- Telefonnummer

### Standardattribute festlegen {#setting-default-attributes}

{% tabs %}
{% tab Methoden verwenden %}
Um ein Standardattribut für eine:n Nutzer:in festzulegen, rufen Sie die Methode `getUser()` auf Ihrer Braze-Instanz auf, um eine Referenz auf die:den aktuelle:n Nutzer:in Ihrer App zu erhalten. Anschließend können Sie Methoden aufrufen, um ein Nutzerattribut festzulegen.

{% subtabs local %}
{% subtab Vorname %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Geschlecht %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Geburtsdatum %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag Manager %}
Bei Verwendung von Google Tag Manager sollten Standard-Nutzerattribute (z. B. der Vorname) auf die gleiche Weise protokolliert werden wie angepasste Nutzerattribute. Stellen Sie sicher, dass die übergebenen Werte für Standardattribute dem erwarteten Format entsprechen, das in der Dokumentation der [`User`-Klasse](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) angegeben ist.

Beispielsweise kann das Geschlechtsattribut einen der folgenden Werte annehmen: `"m" | "f" | "o" | "u" | "n" | "p"`. Um das Geschlecht einer:eines Nutzer:in als weiblich festzulegen, erstellen Sie ein Custom-HTML-Tag mit folgendem Inhalt:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Standardattribute zurücksetzen {#unsetting-default-attributes}

Sie können ein Nutzerattribut über Ihren App-Code, eine REST-API-Anfrage oder einen [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Canvas-Schritt entfernen oder zurücksetzen. Verwenden Sie für Array- und boolesche Attribute `null`. Für andere Datentypen verwenden Sie einen leeren String (`""`).

Um ein Standard-Nutzerattribut mit dem Web SDK zurückzusetzen, übergeben Sie `null` an die entsprechende Methode. Zum Beispiel:

{% tabs local %}
{% tab Vorname %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Geschlecht %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Geburtsdatum %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Angepasste Nutzerattribute {#custom-user-attributes}

### Angepasste Attribute festlegen {#setting-custom-attributes}

{% tabs %}
{% tab using methods %}
Zusätzlich zu den Standard-Nutzerattribut-Methoden können Sie auch [angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attribute-data-types) für Ihre Nutzer:innen festlegen. Die vollständigen Methodenspezifikationen finden Sie in [unseren JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
So legen Sie ein angepasstes Attribut mit einem `string`-Wert fest:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
So legen Sie ein angepasstes Attribut mit einem `integer`-Wert fest:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

{% endsubtab %}
{% subtab Date %}
So legen Sie ein angepasstes Attribut mit einem `date`-Wert fest:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```

{% endsubtab %}
{% subtab Array %}

Die standardmäßige und maximale Höchstzahl an Elementen in einem Array beträgt 500. Sie können die Höchstzahl an Elementen im Braze-Dashboard unter **Data Settings** > **Custom Attributes** aktualisieren. Arrays, die die Höchstzahl an Elementen überschreiten, werden auf die Höchstzahl an Elementen gekürzt.


So legen Sie ein angepasstes Attribut mit einem `array`-Wert fest:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
An Braze übergebene Datumsangaben müssen JavaScript-Date-Objekte sein.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Schlüssel und Werte angepasster Attribute dürfen maximal 255 Zeichen lang sein. Weitere Informationen zu gültigen Werten für angepasste Attribute finden Sie in der [Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab google tag manager %}
Angepasste Nutzerattribute sind aufgrund einer Einschränkung in der Skriptsprache von Google Tag Manager nicht verfügbar. Um angepasste Attribute zu protokollieren, erstellen Sie ein Custom-HTML-Tag mit dem folgenden Inhalt:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
Das GTM-Template unterstützt keine verschachtelten Eigenschaften bei Ereignissen oder Käufen. Sie können das obige HTML verwenden, um Ereignisse oder Käufe zu protokollieren, die verschachtelte Eigenschaften erfordern.
{% endalert %}
{% endtab %}
{% endtabs %}

### Angepasste Attribute zurücksetzen {#unsetting-custom-attributes}

Um ein angepasstes Attribut zurückzusetzen, übergeben Sie `null` an die zugehörige Methode.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Verschachtelte angepasste Attribute {#nesting-custom-attributes}

Sie können auch Eigenschaften innerhalb angepasster Attribute verschachteln. Im folgenden Beispiel wird ein `favorite_book`-Objekt mit verschachtelten Eigenschaften als angepasstes Attribut im Nutzerprofil festgelegt. Weitere Details finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### REST API verwenden {#using-the-rest-api}

Sie können auch unsere REST API verwenden, um Nutzerattribute festzulegen oder zurückzusetzen. Weitere Informationen finden Sie unter [Nutzerdaten-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Nutzer:innen-Abos festlegen {#setting-user-subscriptions}

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder E-Mail oder Push), rufen Sie die Funktionen `setEmailNotificationSubscriptionType()` bzw. `setPushNotificationSubscriptionType()` auf. Beide Funktionen nehmen den `enum`-Typ `braze.User.NotificationSubscriptionTypes` als Argumente entgegen. Dieser Typ hat drei verschiedene Zustände:

| Abo-Status | Definition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Abonniert und explizites Opt-in |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Abonniert, aber kein explizites Opt-in |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Abgemeldet und/oder explizites Opt-out |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen-Abos festlegen" }

Wenn sich Nutzer:innen für Push registrieren, fordert der Browser sie auf, Benachrichtigungen zuzulassen oder zu blockieren. Wenn sie Push zulassen, werden sie standardmäßig auf `OPTED_IN` gesetzt.

Weitere Informationen zur Implementierung von Abos und expliziten Opt-ins finden Sie unter [Nutzer:innen-Abos verwalten]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions).

### Nutzer:in von E-Mail abmelden {#unsubscribing-a-user-from-email}

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Nutzer:in von Push abmelden {#unsubscribing-a-user-from-push}

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
