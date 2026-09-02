---
nav_title: Carthage
article_title: Carthage-Integration für iOS
platform: iOS
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie das Braze SDK or Software-Development-Kit mit Carthage für iOS integrieren."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Carthage-Integration {#carthage-integration}

## SDK or Software-Development-Kit importieren {#import-the-sdk}

Ab Version `4.4.0` unterstützt das Braze SDK or Software-Development-Kit bei der Integration über Carthage XCFrameworks. Um das vollständige SDK or Software-Development-Kit zu importieren, fügen Sie diese Zeilen in Ihre `Cartfile` ein:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Ziehen Sie für weitere Anweisungen zum Importieren des SDK or Software-Development-Kit die [Schnellstartanleitung für Carthage](https://github.com/Carthage/Carthage#quick-start) zurate.

Wenn Sie von einer Version vor `4.4.0` migrieren, folgen Sie dem [Carthage-Migrationsleitfaden für XCFrameworks](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks).

{% alert note %}
Weitere Informationen zur Syntax der `Cartfile` oder zu Features wie dem Version-Pinning finden Sie in der [Carthage-Dokumentation](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile).
Informationen zur plattformspezifischen Verwendung von Carthage entnehmen Sie bitte dem [Nutzer:innenhandbuch](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).
{% endalert %}

### Frühere Versionen {#previous-versions}

Fügen Sie für die Versionen `3.24.0` bis `4.3.4` Folgendes in Ihre `Cartfile` ein:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

Um Versionen vor `3.24.0` zu importieren, fügen Sie Folgendes in Ihre `Cartfile` ein:
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

Stellen Sie sicher, dass Sie `<BRAZE_IOS_SDK_VERSION>` durch die [entsprechende Version](https://github.com/Appboy/appboy-ios-sdk/releases) des Braze iOS SDK or Software-Development-Kit im Format „x.y.z“ ersetzen.

## Nächste Schritte {#next-steps}

Folgen Sie den Anweisungen, um [die Integration abzuschließen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).

## Nur-Core-Integration {#core-only-integration}

Wenn Sie das Core SDK or Software-Development-Kit ohne UI-Komponenten oder Abhängigkeiten verwenden möchten, installieren Sie die Core-Version des Braze Carthage Frameworks, indem Sie die folgende Zeile in Ihre `Cartfile` einfügen:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

