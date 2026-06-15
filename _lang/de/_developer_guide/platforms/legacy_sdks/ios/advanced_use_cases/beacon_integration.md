---
nav_title: Beacon-Integration
article_title: Beacon-Integration für iOS
platform: iOS
page_order: 4
description: "Dieser Artikel behandelt die Protokollierung angepasster Events mit Infillion Beacons für iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Beacon-Integration {#beacon-integration}

Hier erfahren Sie, wie Sie bestimmte Arten von Beacons in Braze integrieren, um Segmentierung und Messaging zu ermöglichen.

## Infillion Beacons {#infillion-beacons}

Sobald Sie Ihre Infillion Beacons eingerichtet und in Ihre App integriert haben, können Sie angepasste Events protokollieren, z. B. den Beginn oder das Ende eines Besuchs oder die Sichtung eines Beacons. Sie können auch Eigenschaften für diese Events wie den Ortsnamen oder die Verweildauer protokollieren.

Um ein angepasstes Event zu protokollieren, wenn ein:e Nutzer:in einen Ort betritt, geben Sie diesen Code in die Methode `didBeginVisit` ein:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

`flushDataAndProcessRequestQueue` bestätigt, dass Ihr Event auch dann protokolliert wird, wenn sich die App im Hintergrund befindet. Der gleiche Prozess kann für das Verlassen eines Standorts implementiert werden. Beachten Sie, dass hierbei für jeden neuen Ort, den ein:e Nutzer:in betritt, ein eindeutiges angepasstes Event erstellt und inkrementiert wird. Wenn Sie voraussichtlich mehr als 50 Orte erstellen, empfehlen wir Ihnen, ein allgemeines angepasstes Event „Ort betreten“ zu erstellen und den Ortsnamen als Event-Eigenschaft aufzunehmen.