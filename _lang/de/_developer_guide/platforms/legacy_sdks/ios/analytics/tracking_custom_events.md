---
nav_title: Angepasste Events verfolgen
article_title: Angepasste Events für iOS verfolgen
platform: iOS
page_order: 2
description: "Dieser referenzierende Artikel beschreibt, wie Sie angepasste Events für Ihre iOS-Anwendung hinzufügen und tracken können."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Angepasste Events für iOS verfolgen {#track-custom-events-for-ios}

Sie können angepasste Events in Braze aufzeichnen, um mehr über das Nutzungsverhalten Ihrer App zu erfahren und Ihre Nutzer:innen nach ihren Aktionen auf dem Dashboard zu segmentieren.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsmöglichkeiten durch angepasste Events, angepasste Attribute und Kauf-Events in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) sowie unsere Hinweise zu den [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions/).

## Hinzufügen eines angepassten Events {#adding-a-custom-event}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("YOUR_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### Hinzufügen von Eigenschaften {#adding-properties}

Sie können Metadaten zu angepassten Events hinzufügen, indem Sie ein `NSDictionary` mit den Werten `NSNumber`, `NSString` oder `NSDate` übergeben.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR-EVENT-NAME"
                         withProperties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent(
  "YOUR-EVENT-NAME",
  withProperties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```

{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie in unserer [Dokumentation zu den Klassen](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79).

### Reservierte Schlüssel {#event-reserved-keys}

Die folgenden Schlüssel sind reserviert und können nicht als Event-Eigenschaften für angepasste Events verwendet werden:

- `time`
- `event_name`

## Zusätzliche Ressourcen {#additional-resources}

- Siehe die Methodendeklaration in der `Appboy.h`-[Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Weitere Informationen finden Sie in der Dokumentation zu [`logCustomEvent`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa).