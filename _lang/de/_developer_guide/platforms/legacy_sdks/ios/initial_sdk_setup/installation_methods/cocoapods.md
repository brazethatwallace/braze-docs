---
nav_title: CocoaPods
article_title: CocoaPods-Integration für iOS
platform: iOS
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie das Braze SDK mit CocoaPods für iOS integrieren."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# CocoaPods-Integration {#cocoapods-integration}

## 1. Schritt: CocoaPods installieren {#step-1-install-cocoapods}

Die Installation des iOS SDK über [CocoaPods](http://cocoapods.org/) automatisiert den Großteil des Installationsprozesses für Sie. Bevor Sie mit diesem Vorgang beginnen, sollten Sie sicherstellen, dass Sie [Ruby Version 2.0.0](https://www.ruby-lang.org/en/installation/) oder höher verwenden. Für die Installation dieses SDK sind keine Kenntnisse der Ruby-Syntax erforderlich.

Führen Sie als Erstes folgenden Befehl aus:

```bash
$ sudo gem install cocoapods
```

Wenn Sie Probleme mit CocoaPods haben, lesen Sie bitte die [Anleitung zur Fehlerbehebung](http://guides.cocoapods.org/using/troubleshooting.html) für CocoaPods.

{% alert note %}
Wenn Sie aufgefordert werden, die ausführbare Datei `rake` zu überschreiben, finden Sie weitere Informationen in der Anleitung [„Erste Schritte“](http://guides.cocoapods.org/using/getting-started.html) auf CocoaPods.org.
{% endalert %}

## 2. Schritt: Erstellen des Podfile {#step-2-constructing-the-podfile}

Nachdem Sie den CocoaPods Ruby Gem installiert haben, müssen Sie in Ihrem Xcode-Projektverzeichnis eine Datei namens `Podfile` erstellen.

Fügen Sie die folgende Zeile in Ihr Podfile ein:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

Wir empfehlen Ihnen, Braze so zu versionieren, dass Pod-Updates automatisch alles erfassen, was kleiner als ein Minor-Versionsupdate ist. Dies sieht folgendermaßen aus: `pod 'Appboy-iOS-SDK' ~> Major.Minor.Build`. Wenn Sie die neueste Version des Braze SDK auch bei größeren Änderungen automatisch integrieren möchten, können Sie `pod 'Appboy-iOS-SDK'` in Ihrem Podfile verwenden.

#### Subspecs {#subspecs}

Wir empfehlen Integratoren, unser vollständiges SDK zu importieren. Wenn Sie jedoch sicher sind, dass Sie nur ein bestimmtes Feature von Braze integrieren möchten, können Sie anstelle des vollständigen SDK nur die gewünschte UI-Subspec importieren.

| Subspec | Details |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | Die Subspec `InAppMessage` enthält die In-App-Nachrichten-UI von Braze und das Core SDK. |
| `pod 'Appboy-iOS-SDK/ContentCards'` | Die Subspec `ContentCards` enthält die Content-Card-UI von Braze und das Core SDK. |
| `pod 'Appboy-iOS-SDK/NewsFeed'` | Die Subspec `NewsFeed` enthält das Braze Core SDK. |
| `pod 'Appboy-iOS-SDK/Core'` | Die Subspec `Core` enthält Unterstützung für Analytics, wie angepasste Events und Attribute. |
{: .ws-td-nw-1 aria-label="Subspecs" }

## 3. Schritt: Installieren des Braze SDK {#step-3-installing-the-braze-sdk}

Um die Braze SDK CocoaPods zu installieren, navigieren Sie in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen den folgenden Befehl aus:
```
pod install
```

Jetzt sollten Sie den von CocoaPods erstellten neuen Xcode-Projektarbeitsbereich öffnen können. Stellen Sie sicher, dass Sie diesen Xcode-Workspace anstelle Ihres Xcode-Projekts verwenden.

![Ein Appboy-Beispielordner, der erweitert wurde, um den neuen „AppbpyExample.workspace“ zu zeigen.]({% image_buster /assets/img_archive/podsworkspace.png %})

## Nächste Schritte {#next-steps}

Folgen Sie den Anweisungen, um [die Integration abzuschließen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/).

## Aktualisieren des Braze SDK über CocoaPods {#updating-the-braze-sdk-via-cocoapods}

Um einen CocoaPod zu aktualisieren, führen Sie einfach den folgenden Befehl in Ihrem Projektverzeichnis aus:

```
pod update
```

