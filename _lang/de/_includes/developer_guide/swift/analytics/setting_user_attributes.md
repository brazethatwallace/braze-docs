{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Standard-Nutzerattribute {#default-user-attributes}

### Unterstützte Attribute {#supported-attributes}

Die folgenden Attribute sollten auf dem `Braze.User`-Objekt festgelegt werden:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

### Standardattribute festlegen {#setting-default-attributes}

Um ein Standardattribut für eine:n Nutzer:in festzulegen, setzen Sie das entsprechende Feld auf dem gemeinsamen `Braze.User`-Objekt. Das folgende Beispiel zeigt, wie Sie das Vorname-Attribut festlegen:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### Standardattribute zurücksetzen {#unsetting-default-attributes}

Um ein Standardattribut zurückzusetzen, übergeben Sie `nil` an die entsprechende Methode.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## Angepasste Nutzerattribute {#custom-user-attributes}

Zusätzlich zu den Standardattributen ermöglicht Braze Ihnen auch, angepasste Attribute mit verschiedenen Datentypen zu definieren. Weitere Informationen zu den Segmentierungsoptionen der einzelnen Attribute finden Sie unter [Nutzerdatenerfassung]({{site.baseurl}}/developer_guide/analytics).

{% alert important %}
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten. Weitere Informationen finden Sie unter [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).
{% endalert %}

### Angepasste Attribute festlegen {#setting-custom-attributes}

{% tabs local %}
{% tab string %}
So legen Sie ein angepasstes Attribut mit einem `string`-Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab integer %}
So legen Sie ein angepasstes Attribut mit einem `integer`-Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab floating-points %}
Braze behandelt `float`- und `double`-Werte in der Datenbank identisch. So legen Sie ein angepasstes Attribut mit einem Double-Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab boolean %}
So legen Sie ein angepasstes Attribut mit einem `boolean`-Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab date %}
So legen Sie ein angepasstes Attribut mit einem `date`-Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab array %}
Die Standard- und Höchstzahl an Elementen in einem Array beträgt 500. Sie können die Höchstzahl der Arrays im Braze-Dashboard unter **Dateneinstellungen** > **Angepasste Attribute** Update or aktualisieren or aktualisieren. Arrays, die die Höchstzahl an Elementen überschreiten, werden auf die Höchstzahl an Elementen gekürzt.

So legen Sie ein angepasstes Attribut mit einem `array`-Wert fest:

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Angepasste Attribute inkrementieren oder dekrementieren {#incrementing-or-decrementing-custom-attributes}

Dieser Code ist ein Beispiel für ein inkrementierendes angepasstes Attribut. Sie können den Wert eines angepassten Attributs um jeden beliebigen `integer`- oder `long`-Wert erhöhen:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Angepasste Attribute zurücksetzen {#unsetting-custom-attributes}

{% tabs %}
{% tab swift %}
Um ein angepasstes Attribut zurückzusetzen, übergeben Sie den entsprechenden Attributschlüssel an die Methode `unsetCustomAttribute`.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
Um ein angepasstes Attribut zurückzusetzen, übergeben Sie den entsprechenden Attributschlüssel an die Methode `unsetCustomAttributeWithKey`.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Verschachtelte angepasste Attribute {#nesting-custom-attributes}

Sie können auch Eigenschaften innerhalb angepasster Attribute verschachteln. Im folgenden Beispiel wird ein `favorite_book`-Objekt mit verschachtelten Eigenschaften als angepasstes Attribut im Kundenprofil or Nutzerprofil festgelegt. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objective-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### Verwendung der Representational State Transfer API {#using-the-rest-api}

Sie können auch unsere Representational State Transfer API verwenden, um Nutzerattribute festzulegen oder zurückzusetzen. Weitere Informationen finden Sie unter [Nutzerdaten-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Abo-Status für Nutzer:innen festlegen {#setting-user-subscriptions}

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder E-Mail oder Push), rufen Sie die Funktionen `set(emailSubscriptionState:)` bzw. `set(pushNotificationSubscriptionState:)` auf. Beide Funktionen verwenden den Enum-Typ `Braze.User.SubscriptionState` als Argument. Dieser Typ hat drei verschiedene Status:

| Abo-Status | Definition |
| ------------------- | ---------- |
| `optedIn` | Abonniert und explizites Opt-in erteilt |
| `subscribed` | Abonniert, aber kein explizites Opt-in erteilt |
| `unsubscribed` | Abgemeldet und/oder explizites Opt-out erteilt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abo-Status für Nutzer:innen festlegen" }

Nutzer:innen, die einer App die Erlaubnis erteilen, ihnen Push-Benachrichtigungen zu senden, erhalten standardmäßig den Status `optedIn`, da iOS ein explizites Opt-in erfordert.

Nutzer:innen werden beim Erhalt einer gültigen E-Mail-Adresse automatisch auf `subscribed` gesetzt. Wir empfehlen Ihnen jedoch, einen expliziten Opt-in-Prozess einzurichten und diesen Wert bei ausdrücklicher Zustimmung Ihrer Nutzer:innen auf `optedIn` zu setzen. Weitere Informationen finden Sie unter [Nutzer:innen-Abos verwalten]({{site.baseurl}}/user_guide/channels/email/subscriptions).

### E-Mail-Abos festlegen {#setting-email-subscriptions}

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### Push-Benachrichtigungs-Abos festlegen {#setting-push-notification-subscriptions}

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie unter [Nutzer:innen-Abos verwalten]({{site.baseurl}}/user_guide/channels/email/subscriptions).