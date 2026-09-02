---
nav_title: Swift-Paketmanager
article_title: Swift-Paketmanager-Integration für iOS
platform: iOS
page_order: 3
description: "Dieses Tutorial behandelt die Installation des Braze SDK or Software-Development-Kit mit dem Swift-Paketmanager für iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integration des Swift-Paketmanagers {#swift-package-manager-integration}

Die Installation des iOS SDK or Software-Development-Kit über den [Swift-Paketmanager](https://swift.org/package-manager/) (SPM) automatisiert den Großteil des Installationsprozesses für Sie. Bevor Sie mit diesem Vorgang beginnen, stellen Sie sicher, dass Sie Xcode 12 oder höher verwenden.

{% alert note %}
tvOS ist derzeit nicht über den Swift-Paketmanager verfügbar.
{% endalert %}

## Schritt 1: Hinzufügen der Abhängigkeit zu Ihrem Projekt {#step-1-adding-the-dependency-to-your-project}

### SDK or Software-Development-Kit-Version importieren {#import-sdk-version}

Öffnen Sie Ihr Projekt und navigieren Sie zu den Einstellungen Ihres Projekts. Wählen Sie den Tab **Swift Packages** und klicken Sie auf die Schaltfläche <i class="fas fa-plus" aria-label="Hinzufügen"></i> unterhalb der Paketliste.

![Xcode-Projekteinstellungen mit ausgewähltem Tab „Swift Packages“.]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

Wenn Sie SDK or Software-Development-Kit-Version `3.33.1` oder höher importieren, geben Sie die URL unseres iOS-SDK or Software-Development-Kit-Repository (`https://github.com/braze-inc/braze-ios-sdk`) in das Textfeld ein und klicken Sie auf **Next**.

Für die Versionen `3.29.0` bis `3.32.0` verwenden Sie die URL `https://github.com/Appboy/Appboy-ios-sdk`.

![Xcode-Dialog „Add Package“ für die Repository-URL des Braze iOS SDK.]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

Wählen Sie auf dem nächsten Bildschirm die SDK or Software-Development-Kit-Version aus und klicken Sie auf **Next**. Die Versionen `3.29.0` und höher sind mit dem Swift-Paketmanager kompatibel.

![Xcode-Paketversionsauswahl für das Braze iOS SDK.]({% image_buster /assets/img/ios/spm/select_version.png %})

### Pakete auswählen {#select-packages}

Wählen Sie das Paket, das Ihren Anforderungen am besten entspricht, und klicken Sie auf **Finish**. Stellen Sie sicher, dass Sie entweder `AppboyKit` oder `AppboyUI` auswählen. Die Einbeziehung beider Pakete kann zu unerwünschtem Verhalten führen:

- `AppboyUI`
  - Am besten geeignet, wenn Sie die von Braze bereitgestellten UI-Komponenten verwenden möchten.
  - Enthält `AppboyKit` automatisch.
- `AppboyKit`
  - Am besten geeignet, wenn Sie keine der von Braze bereitgestellten UI-Komponenten (z. B. Content Cards, In-App-Nachrichten usw.) verwenden müssen.
- `AppboyPushStory`
  - Fügen Sie dieses Paket hinzu, wenn Sie Push Stories in Ihre App integriert haben. Dies wird ab der Version `3.31.0` unterstützt.
  - Wählen Sie in der Dropdown-Liste unter `Add to Target` das Ziel für `ContentExtension` anstelle des Ziels Ihrer Hauptanwendung aus.

![Xcode-Bildschirm „Add Package“ zur Auswahl der Braze-SDK-Bibliotheksziele.]({% image_buster /assets/img/ios/spm/add_package.png %})

## Schritt 2: Ihr Projekt konfigurieren {#step-2-configuring-your-project}

Navigieren Sie als Nächstes zu den **Build-Einstellungen** Ihres Projekts und fügen Sie das `-ObjC`-Flag zur Einstellung **Other Linker Flags** hinzu. Dieses Flag muss hinzugefügt und eventuelle [Fehler](https://developer.apple.com/library/archive/qa/qa1490/_index.html) müssen behoben werden, um das SDK or Software-Development-Kit weiter integrieren zu können.

![Xcode-Build-Einstellungen mit dem Feld „Other Linker Flags“.]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
Wenn Sie das Flag `-ObjC` nicht hinzufügen, können Teile der API fehlen und das Verhalten ist nicht definiert. Es kann zu unerwarteten Fehlern (z. B. „unrecognized SELEKTOR sent to class“), Abstürzen der Anwendung und anderen Problemen kommen.
{% endalert %}

## Schritt 3: Schema des Ziels bearbeiten {#step-3-editing-the-targets-scheme}
{% alert important %}
Wenn Sie Xcode 12.5 oder eine neuere Version verwenden, überspringen Sie diesen Schritt.
{% endalert %}

Wenn Sie Xcode 12.4 oder eine ältere Version verwenden, bearbeiten Sie das Schema des Ziels, das das Appboy-Paket enthält (Menüpunkt **Product > Scheme > Edit Scheme**):
1. Erweitern Sie das Menü **Build** und wählen Sie **Post-actions**. Drücken Sie auf das Pluszeichen (+) und wählen Sie **New Run Script Action**.
2. Wählen Sie in der Dropdown-Liste **Provide build settings from** das Ziel Ihrer App aus.
3.  Kopieren Sie dieses Skript in das offene Feld:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![Xcode-Build-Phases-Menü zum Hinzufügen einer Run-Script-Build-Phase.]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## Nächste Schritte {#next-steps}

Folgen Sie den Anweisungen, um [die Integration abzuschließen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).