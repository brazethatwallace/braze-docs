---
nav_title: Angepasste Attribute festlegen
article_title: Angepasste Attribute für Windows Universal festlegen
platform: Windows Universal
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Attribute auf der Windows Universal-Plattform festlegen."
hidden: true
---

# Angepasste Attribute festlegen {#set-custom-attributes}
{% multi_lang_include archive/windows_deprecation.md %}

Braze bietet Methoden für die Zuweisung von Attributen an Nutzer:innen. Im Dashboard können Sie Ihre Nutzer:innen nach diesen Attributen filtern und segmentieren.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die angepasste Events, angepasste Attribute und Kauf-Events bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

Nutzerattribute können dem aktuellen `IAppboyUser`-Objekt zugewiesen werden. Um einen Verweis auf das aktuelle `IAppboyUser`-Objekt zu erhalten, rufen Sie `Appboy.SharedInstance.AppboyUser` auf.

## Zuweisen von Standard-Nutzerattributen {#assigning-default-user-attributes}

Die folgenden Attribute sollten als Eigenschaften des `IAppboyUser`-Objekts definiert werden:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**Beispiel-Implementierung**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## Zuweisen von angepassten Nutzerattributen {#assigning-custom-user-attributes}

Neben den Standard-Nutzerattributen können Sie in Braze auch angepasste Attribute unter Verwendung verschiedener Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen und zu den Auswirkungen der einzelnen Attribute finden Sie in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes).

### Angepasste Attributwerte festlegen {#setting-custom-attribute-values}

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
Braze behandelt FLOAT- und DOUBLE-Werte in der Datenbank genau gleich.
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
>  An Braze übergebene Datumsangaben müssen entweder im [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601)-Format vorliegen, z. B. `2013-07-16T19:20:30+01:00`, oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`, z. B. `2016-12-14T13:32:31.601-0800`.
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

### Inkrementieren/Dekrementieren von angepassten Attributen {#incrementingdecrementing-custom-attributes}

Dieser Code ist ein Beispiel für ein inkrementierendes angepasstes Attribut. Sie können den Wert eines angepassten Attributs um jeden positiven oder negativen ganzzahligen Wert erhöhen.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Zurücksetzen eines angepassten Attributs {#unsetting-a-custom-attribute}

Angepasste Attribute können auch mit der folgenden Methode zurückgesetzt werden:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Festlegen eines angepassten Attributs über die REST API {#setting-a-custom-attribute-via-the-rest-api}

Sie können auch unsere REST API verwenden, um Nutzerattribute festzulegen. Einzelheiten finden Sie in der Dokumentation zur [Nutzer:innen-API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

### Wertgrenzen für angepasste Attribute {#custom-attribute-value-limits}

Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.

## Verwaltung des Abo-Status für Benachrichtigungen {#managing-notification-subscription-statuses}

Um ein Abo für Ihre Nutzer:innen einzurichten (entweder per E-Mail oder per Push), können Sie die folgenden Abo-Status als Eigenschaften des `IAppboyUser`-Objekts festlegen. Der Abo-Status in Braze hat drei verschiedene Zustände für E-Mail und Push:

| Abo-Status | Definition |
| ------------------- | ---------- |
| `OptedIn` | Abonniert und ausdrücklich angemeldet |
| `Subscribed` | Abonniert, aber nicht ausdrücklich angemeldet |
| `UnSubscribed` | Abbestellt und/oder ausdrücklich abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

- `EmailNotificationSubscriptionType`
  - Nutzer:innen werden bei Erhalt einer gültigen E-Mail-Adresse automatisch auf `Subscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein ausdrückliches Opt-in-Verfahren einzurichten und diesen Wert bei Erhalt einer ausdrücklichen Zustimmung Ihrer Nutzer:innen auf `OptedIn` zu setzen.
- `PushNotificationSubscriptionType`
  - Nutzer:innen werden bei einer gültigen Push-Registrierung automatisch auf `Subscribed` gesetzt. Wir empfehlen Ihnen jedoch, ein ausdrückliches Opt-in-Verfahren einzurichten und diesen Wert nach Erhalt der ausdrücklichen Zustimmung Ihrer Nutzer:innen auf `OptedIn` zu setzen.

>  Diese Typen fallen unter `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Weitere Informationen finden Sie unter [Verwalten von Nutzer:innen-Abos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).