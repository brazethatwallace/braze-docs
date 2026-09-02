---
nav_title: Speicher
article_title: Speicher für iOS
platform: iOS
page_order: 8.9
page_type: reference
description: "Dieser Referenzartikel beschreibt die Eigenschaften auf Geräteebene, die vom Braze iOS SDK or Software-Development-Kit erfasst werden."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Speicher {#storage}

Dieser Artikel beschreibt die verschiedenen Eigenschaften auf Geräteebene, die bei der Verwendung des Braze iOS SDK or Software-Development-Kit erfasst werden.

## Geräteeigenschaften {#device-properties}

Standardmäßig erfasst Braze die folgenden [Eigenschaften auf Geräteebene](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181), um die Personalisierung von Nachrichten auf der Grundlage von Gerät, Sprache und Zeitzone zu ermöglichen:

* Geräteauflösung
* Netzbetreiber des Geräts
* Gebietsschema des Geräts
* Gerätemodell
* Betriebssystemversion des Geräts
* IDFV (optional mit [iOS SDK or Software-Development-Kit v5.7.0+](https://github.com/braze-inc/braze-swift-sdk))
* Push aktiviert
* Zeitzone des Geräts
* Push-Autorisierungsstatus
* Ad-Tracking aktiviert

{% alert note %}
Das Braze SDK or Software-Development-Kit erfasst IDFA nicht automatisch. Apps können optional IDFA an Braze weitergeben, indem sie unser `ABKIDFADelegate`-Protokoll implementieren. Apps müssen das ausdrückliche Opt-in der Endnutzer:innen für das Tracking über das App-Tracking-Transparenz-Framework einholen, bevor sie IDFA an Braze weitergeben.
{% endalert %}

Konfigurierbare Gerätefelder sind in der [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179)-enum definiert. Um das Gerätefeld, das Sie auf die Zulassungsliste setzen möchten, zu deaktivieren oder anzugeben, weisen Sie das bitweise `OR` der gewünschten Felder [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) in den `appboyOptions` von `startWithApiKey:inApplication:withAppboyOptions:` zu.

Um beispielsweise die Erfassung von Zeitzone und Gebietsschema zuzulassen, setzen Sie:
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

Standardmäßig sind alle Felder aktiviert. Beachten Sie, dass ohne einige Eigenschaften nicht alle Features ordnungsgemäß funktionieren. Zum Beispiel funktioniert die Zustellung zur Ortszeit nicht ohne die Zeitzone.

Weitere Informationen zu den automatisch erfassten Geräteeigenschaften finden Sie unter [SDK or Software-Development-Kit-Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).