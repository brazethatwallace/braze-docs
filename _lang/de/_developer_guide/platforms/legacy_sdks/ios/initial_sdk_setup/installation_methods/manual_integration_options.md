---
nav_title: Manuell
article_title: Manuelle Integrationsmöglichkeiten für iOS
platform: iOS
page_order: 4
description: "Dieser Referenzartikel zeigt, wie Sie das Braze SDK für iOS manuell integrieren."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Manuelle Integration {#manual-integration}

{% alert tip %}
Wir empfehlen Ihnen dringend, das SDK über einen Paketmanager wie [Swift-Paketmanager](../swift_package_manager/), [CocoaPods](../cocoapods/) oder [Carthage](../carthage_integration/) zu implementieren. Damit sparen Sie viel Zeit und können einen Großteil des Prozesses automatisieren. Wenn Sie dazu jedoch nicht in der Lage sind, können Sie die Integration auch manuell vornehmen, indem Sie die Anweisungen befolgen.
{% endalert %}

## 1. Schritt: Herunterladen des Braze SDK {#step-1-downloading-the-braze-sdk}

### Option 1: Dynamisches XCFramework {#option-1-dynamic-xcframework}

1. Laden Sie `Appboy_iOS_SDK.xcframework.zip` von der [Release-Seite](https://github.com/appboy/appboy-ios-sdk/releases) herunter und extrahieren Sie die Datei.
2. Ziehen Sie dieses `.xcframework` in Xcode per Drag-and-Drop in Ihr Projekt.
3. Wählen Sie auf dem Tab **Allgemein** des Projekts **Embed & Sign** für `Appboy_iOS_SDK.xcframework` aus.

### Option 2: Statisches XCFramework für statische Integration {#option-2-static-xcframework-for-static-integration}

1. Laden Sie `Appboy_iOS_SDK.zip` von der [Release-Seite](https://github.com/appboy/appboy-ios-sdk/releases) herunter.<br><br>
2. Wählen Sie in Xcode im Projektnavigator das Zielprojekt oder die Zielgruppe für Braze aus.<br><br>
3. Navigieren Sie zu **File > Add Files > Project_Name**.<br><br>
4. Fügen Sie die Ordner `AppboyKit` und `AppboyUI` als Gruppe zu Ihrem Projekt hinzu.
	- Vergewissern Sie sich, dass die Option **Copy items into destination group's folder** ausgewählt ist, wenn Sie die Integration zum ersten Mal vornehmen. Erweitern Sie **Options** in der Dateiauswahl und wählen Sie **Copy items if needed** und **Create groups**.
	- Löschen Sie die Verzeichnisse `AppboyKit/include` und `AppboyUI/include`.<br><br>
5. (Optional) Wenn einer der folgenden Punkte auf Sie zutrifft:
  - Sie möchten nur die wichtigsten Analytics-Features des SDK nutzen und keine UI-Features (z. B. In-App-Nachrichten oder Content Cards).
  - Sie verfügen über ein angepasstes UI für Braze-UI-Features und kümmern sich selbst um das Herunterladen von Bildern.<br><br>Sie können die Kernversion des SDK verwenden, indem Sie die Dateien `ABKSDWebImageProxy.m` und `Appboy.bundle` entfernen. Dadurch werden die Abhängigkeit vom `SDWebImage`-Framework und alle UI-bezogenen Ressourcen (z. B. Nib-Dateien, Bilder, Lokalisierungsdateien) aus dem SDK entfernt.

{% alert warning %}
Wenn Sie versuchen, die Kernversion des SDK ohne Braze-UI-Features zu verwenden, werden In-App-Nachrichten nicht angezeigt. Der Versuch, die Braze Content-Cards-UI mit der Kernversion anzuzeigen, führt zu unvorhersehbarem Verhalten.
{% endalert %}

## 2. Schritt: Hinzufügen der erforderlichen iOS-Bibliotheken {#step-2-adding-required-ios-libraries}

1. Klicken Sie auf das Target für Ihr Projekt (über die Navigation auf der linken Seite) und wählen Sie den Tab **Build Phases**.<br><br>
2. Klicken Sie auf den Button <i class="fas fa-plus" aria-label="Hinzufügen"></i> unter **Link Binary With Libraries**.<br><br>
3. Wählen Sie im Menü `SystemConfiguration.framework` aus.<br><br>
4. Markieren Sie diese Bibliothek als erforderlich, indem Sie das Pulldown-Menü neben `SystemConfiguration.framework` verwenden.<br><br>
5. Wiederholen Sie den Vorgang, um jedes der folgenden erforderlichen Frameworks zu Ihrem Projekt hinzuzufügen, und markieren Sie jedes als „erforderlich“.
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. Fügen Sie die folgenden Frameworks hinzu und markieren Sie sie als optional:
	- `CoreTelephony.framework`<br><br>
7. Wählen Sie den Tab **Build Settings**. Suchen Sie im Abschnitt **Linking** die Einstellung **Other Linker Flags** und fügen Sie das Flag `-ObjC` hinzu.<br><br>
8. Das Framework `SDWebImage` wird benötigt, damit Content Cards und In-App-Nachrichten richtig funktionieren. `SDWebImage` wird für das Herunterladen und Anzeigen von Bildern, einschließlich GIFs, verwendet. Wenn Sie Content Cards oder In-App-Nachrichten verwenden möchten, folgen Sie den Schritten zur Integration von SDWebImage.

### SDWebImage-Integration {#sdwebimage-integration}

Um `SDWebImage` zu installieren, folgen Sie den [Anweisungen](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework) des Herstellers und ziehen Sie das resultierende `XCFramework` per Drag-and-Drop in Ihr Projekt.

### Optionales Standort-Tracking {#optional-location-tracking}

1. Fügen Sie das `CoreLocation.framework` hinzu, um das Standort-Tracking zu aktivieren.
2. Sie müssen den Standort für Ihre Nutzer:innen über `CLLocationManager` in Ihrer App autorisieren.

## 3. Schritt: Objective-C-Bridging-Header {#step-3-objective-c-bridging-header}

{% alert note %}
Wenn Ihr Projekt nur Objective-C verwendet, überspringen Sie diesen Schritt.
{% endalert %}

Wenn Ihr Projekt Swift verwendet, benötigen Sie eine Bridging-Header-Datei.

Wenn Sie keine Bridging-Header-Datei haben, erstellen Sie eine und nennen Sie sie `your-product-module-name-Bridging-Header.h`, indem Sie **File > New > File > (iOS oder OS X) > Source > Header File** wählen. Fügen Sie dann die folgende Code-Zeile an den Anfang Ihrer Bridging-Header-Datei hinzu:
```
#import "AppboyKit.h"
```

Fügen Sie in den **Build Settings** Ihres Projekts den relativen Pfad Ihrer Header-Datei zur Build-Einstellung `Objective-C Bridging Header` unter `Swift Compiler - Code Generation` hinzu.

## Nächste Schritte {#next-steps}

Folgen Sie den Anweisungen, um [die Integration abzuschließen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).