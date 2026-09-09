---
nav_title: Angepasste Attribute festlegen
article_title: Angepasste Attribute für iOS festlegen
platform: iOS
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Attribute in Ihrer iOS-Anwendung festlegen."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Angepasste Attribute für iOS festlegen {#set-custom-attributes-for-ios}

Braze bietet Methoden für die Zuweisung von Attributen an Nutzer:innen. Im Dashboard können Sie Ihre Nutzer:innen nach diesen Attributen filtern und segmentieren.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die angepasste Events, angepasste Attribute und Kauf-Events bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/analytics) sowie unsere Hinweise zu den [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

## Zuweisen von Standard-Nutzerattributen {#assigning-default-user-attributes}

Um Nutzerattribute zuzuweisen, müssen Sie das entsprechende Feld auf dem gemeinsam genutzten `ABKUser`-Objekt festlegen.

Das Folgende ist ein Beispiel für das Festlegen des Vorname-Attributs:

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

Die folgenden Attribute sollten auf dem `ABKUser`-Objekt festgelegt werden:

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

## Zuweisen von angepassten Nutzerattributen {#assigning-custom-user-attributes}

Neben den Standard-Nutzerattributen können Sie in Braze auch angepasste Attribute unter Verwendung verschiedener Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen, die Ihnen die einzelnen Attribute bieten, finden Sie in unserer [Nutzerdatenerfassung]({{site.baseurl}}/developer_guide/analytics).

### Angepasstes Attribut mit einem String-Wert {#custom-attribute-with-a-string-value}

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

### Angepasstes Attribut mit einem ganzzahligen Wert {#custom-attribute-with-an-integer-value}

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

### Angepasstes Attribut mit einem Double-Wert {#custom-attribute-with-a-double-value}

Braze behandelt `float`- und `double`-Werte in der Datenbank identisch.

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

### Angepasstes Attribut mit einem booleschen Wert {#custom-attribute-with-a-boolean-value}

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

### Angepasstes Attribut mit einem Datumswert {#custom-attribute-with-a-date-value}

Datumsangaben, die mit dieser Methode an Braze übergeben werden, müssen entweder im [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601)-Format (z. B. `2013-07-16T19:20:30+01:00`) oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (`2016-12-14T13:32:31.601-0800`) vorliegen.

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

### Angepasstes Attribut mit einem Array-Wert {#custom-attribute-with-an-array-value}

Die standardmäßige und maximale Höchstzahl an Elementen in einem Array beträgt 500. Sie können die maximale Anzahl von Arrays im Braze-Dashboard unter **Dateneinstellungen** > **Angepasste Attribute** aktualisieren. Arrays, die die Höchstzahl an Elementen überschreiten, werden auf die Höchstzahl an Elementen gekürzt.


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

### Zurücksetzen eines angepassten Attributs {#unsetting-a-custom-attribute}

Angepasste Attribute können auch mit der folgenden Methode zurückgesetzt werden:

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

### Inkrementieren/Dekrementieren von angepassten Attributen {#incrementingdecrementing-custom-attributes}

Dieser Code ist ein Beispiel für ein inkrementierendes angepasstes Attribut. Sie können den Wert eines angepassten Attributs um einen beliebigen positiven oder negativen Integer- oder Long-Wert erhöhen:

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

### Festlegen eines angepassten Attributs über die REST API {#setting-a-custom-attribute-via-the-rest-api}

Sie können auch unsere REST API verwenden, um Nutzerattribute festzulegen. Weitere Informationen finden Sie in der [Nutzer-API-Dokumentation]({{site.baseurl}}/api/endpoints/user_data).

### Wertbegrenzungen für angepasste Attribute {#custom-attribute-value-limits}

Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.

#### Zusätzliche Informationen {#additional-information}

- Weitere Details finden Sie in der [`ABKUser.h`-Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Weitere Informationen finden Sie in der [`ABKUser`-Dokumentation](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html).

## Abos für Nutzer:innen einrichten {#setting-up-user-subscriptions}

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder E-Mail oder Push), rufen Sie die Funktionen `setEmailNotificationSubscriptionType` bzw. `setPushNotificationSubscriptionType` auf. Beide Funktionen nehmen den Enum-Typ `ABKNotificationSubscriptionType` als Argument entgegen. Dieser Typ hat drei verschiedene Zustände:

| Abo-Status | Definition |
| ------------------- | ---------- |
| `ABKOptedin` | Abonniert und explizites Opt-in erteilt |
| `ABKSubscribed` | Abonniert, aber kein explizites Opt-in erteilt |
| `ABKUnsubscribed` | Abgemeldet und/oder explizites Opt-out erteilt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abos für Nutzer:innen einrichten" }

Nutzer:innen, die einer App die Erlaubnis erteilen, ihnen Push-Benachrichtigungen zu senden, erhalten standardmäßig den Status `ABKOptedin`, da iOS ein explizites Opt-in erfordert.

Nutzer:innen werden beim Empfang einer gültigen E-Mail-Adresse automatisch auf `ABKSubscribed` gesetzt. Wir empfehlen jedoch, einen expliziten Opt-in-Prozess einzurichten und diesen Wert bei Erhalt einer ausdrücklichen Zustimmung Ihrer Nutzer:innen auf `OptedIn` zu setzen. Weitere Informationen finden Sie unter [Nutzerabos verwalten]({{site.baseurl}}/user_guide/channels/email/subscriptions).

### E-Mail-Abos festlegen {#setting-email-subscriptions}

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

### Push-Benachrichtigungsabos festlegen {#setting-push-notification-subscriptions}

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

Weitere Informationen finden Sie unter [Nutzerabos verwalten]({{site.baseurl}}/user_guide/channels/email/subscriptions).