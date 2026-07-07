## Integration des Swift SDK {#integrating-the-swift-sdk}

Sie können das Braze Swift SDK mithilfe des Swift-Paketmanagers (SPM), CocoaPods oder manueller Integrationsmethoden integrieren und anpassen. Weitere Informationen über die verschiedenen SDK-Symbole finden Sie in der [Braze Swift-Referenzdokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/).

### Voraussetzungen {#prerequisites}

Bevor Sie beginnen, überprüfen Sie, ob Ihre Umgebung von der [neuesten Braze Swift SDK-Version](https://github.com/braze-inc/braze-swift-sdk#version-information) unterstützt wird.

### 1. Schritt: Installieren Sie das Braze Swift SDK {#step-1-install-the-braze-swift-sdk}

Wir empfehlen die Verwendung des [Swift-Paketmanagers (SwiftPM)](https://swift.org/package-manager/) oder [CocoaPods](http://cocoapods.org/) zur Installation des Braze Swift SDK. Alternativ können Sie das SDK auch manuell installieren.

{% tabs local %}
{% tab Swift Package Manager %}
#### Schritt 1.1: SDK-Version importieren {#step-11-import-sdk-version}

Öffnen Sie Ihr Projekt und navigieren Sie zu den Einstellungen Ihres Projekts. Wählen Sie den Tab **Swift Packages** und klicken Sie auf die Schaltfläche <i class="fas fa-plus"></i> unterhalb der Paketliste.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
Ab Version 7.4.0 verfügt das Braze Swift SDK über zusätzliche Verteilungskanäle als [statische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) und [dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Wenn Sie stattdessen eines dieser Formate verwenden möchten, folgen Sie den Installationsanweisungen des jeweiligen Repositorys.
{% endalert %}

Geben Sie die URL unseres iOS Swift SDK-Repositorys `https://github.com/braze-inc/braze-swift-sdk` in das Textfeld ein. Wählen Sie unter dem Abschnitt **Dependency Rule** die SDK-Version aus. Klicken Sie abschließend auf **Add Package**.

![]({% image_buster /assets/img/importsdk_example.png %})

#### Schritt 1.2: Wählen Sie Ihre Pakete aus {#step-12-select-your-packages}

Das Braze Swift SDK teilt Features in eigenständige Bibliotheken auf, um Entwickler:innen mehr Kontrolle darüber zu geben, welche Features sie in ihre Projekte importieren möchten.

| Paket           | Details                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | Haupt-SDK-Bibliothek mit Unterstützung für Analytics und Push-Benachrichtigungen.                                                                               |
| `BrazeLocation` | Standortbibliothek mit Unterstützung für Standortanalysen und Geofence-Überwachung.                                                                            |
| `BrazeUI`       | Von Braze bereitgestellte Benutzeroberflächen-Bibliothek für In-App-Nachrichten, Content Cards und Banner. Importieren Sie diese Bibliothek, wenn Sie die Standard-UI-Komponenten verwenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1.2: Select your packages" }

{: .ws-td-nw-1}

##### Über die Erweiterungsbibliotheken {#about-extension-libraries}

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) und [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sind Erweiterungsmodule, die zusätzliche Funktionen bieten und nicht direkt zu Ihrem Hauptanwendungsziel hinzugefügt werden sollten. Folgen Sie stattdessen den verlinkten Anleitungen, um sie separat in ihre jeweiligen Zielerweiterungen zu integrieren.
{% endalert %}

| Paket                      | Details                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | Erweiterungsbibliothek für Benachrichtigungsdienste mit Unterstützung für Rich-Push-Benachrichtigungen. |
| `BrazePushStory`           | Erweiterungsbibliothek für Benachrichtigungsinhalte mit Unterstützung für Push Stories. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="About Extension libraries" }

{: .ws-td-nw-1}

Wählen Sie das Paket, das Ihren Anforderungen am besten entspricht, und klicken Sie auf **Add Package**. Stellen Sie sicher, dass Sie mindestens `BrazeKit` auswählen.

![]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### Schritt 1.1: CocoaPods installieren {#step-11-install-cocoapods}

Eine vollständige Anleitung finden Sie im [CocoaPods-Handbuch „Erste Schritte“](https://guides.cocoapods.org/using/getting-started.html). Ansonsten können Sie den folgenden Befehl ausführen, um schnell loszulegen:

```bash
$ sudo gem install cocoapods
```

Wenn Sie nicht weiterkommen, lesen Sie die [CocoaPods-Anleitung zur Fehlerbehebung](http://guides.cocoapods.org/using/troubleshooting.html).

#### Schritt 1.2: Erstellen des Podfiles {#step-12-constructing-the-podfile}

Erstellen Sie als Nächstes in Ihrem Xcode-Projektverzeichnis eine Datei namens `Podfile`.

{% alert note %}
Ab Version 7.4.0 verfügt das Braze Swift SDK über zusätzliche Verteilungskanäle als [statische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) und [dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Wenn Sie stattdessen eines dieser Formate verwenden möchten, folgen Sie den Installationsanweisungen des jeweiligen Repositorys.
{% endalert %}

Fügen Sie die folgende Zeile in Ihr Podfile ein:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` enthält die Haupt-SDK-Bibliothek mit Unterstützung für Analytics und Push-Benachrichtigungen.

Wir empfehlen Ihnen, Braze so zu versionieren, dass Pod-Updates automatisch alles erfassen, was kleiner als ein Minor-Versionsupdate ist. Dies sieht folgendermaßen aus: `pod 'BrazeKit' ~> Major.Minor.Build`. Wenn Sie die neueste Version des Braze SDK auch bei größeren Änderungen automatisch integrieren möchten, können Sie `pod 'BrazeKit'` in Ihrem Podfile verwenden.

##### Über zusätzliche Bibliotheken {#about-additional-libraries}

Das Braze Swift SDK teilt Features in eigenständige Bibliotheken auf, um Entwickler:innen mehr Kontrolle darüber zu geben, welche Features sie in ihre Projekte importieren möchten. Zusätzlich zu `BrazeKit` können Sie die folgenden Bibliotheken zu Ihrem Podfile hinzufügen:

| Bibliothek            | Details                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | Standortbibliothek mit Unterstützung für Standortanalysen und Geofence-Überwachung.                                                                            |
| `pod 'BrazeUI'`       | Von Braze bereitgestellte Benutzeroberflächen-Bibliothek für In-App-Nachrichten, Content Cards und Banner. Importieren Sie diese Bibliothek, wenn Sie die Standard-UI-Komponenten verwenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="About additional libraries" }

{: .ws-td-nw-1}

###### Erweiterungsbibliotheken {#extension-libraries}

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) und [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sind Erweiterungsmodule, die zusätzliche Funktionen bieten und nicht direkt zu Ihrem Hauptanwendungsziel hinzugefügt werden sollten. Stattdessen müssen Sie für jedes dieser Module eigene Erweiterungs-Targets erstellen und die Braze-Module in ihre entsprechenden Targets importieren.

| Bibliothek                       | Details                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | Erweiterungsbibliothek für Benachrichtigungsdienste mit Unterstützung für Rich-Push-Benachrichtigungen. |
| `pod 'BrazePushStory'`           | Erweiterungsbibliothek für Benachrichtigungsinhalte mit Unterstützung für Push Stories. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Extension libraries" }

{: .ws-td-nw-1}

#### Schritt 1.3: Installieren Sie das SDK {#step-13-install-the-sdk}

Um das Braze SDK CocoaPod zu installieren, navigieren Sie in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen Sie den folgenden Befehl aus:
```
pod install
```

Jetzt sollten Sie den von CocoaPods erstellten neuen Xcode-Projektarbeitsbereich öffnen können. Stellen Sie sicher, dass Sie diesen Xcode-Workspace anstelle Ihres Xcode-Projekts verwenden.

![Ein Braze-Beispielordner, der erweitert wurde, um den neuen „BrazeExample.workspace“ anzuzeigen.]({% image_buster /assets/img/braze_example_workspace.png %})

#### Update des SDK mit CocoaPods {#updating-the-sdk-using-cocoapods}

Um ein CocoaPod zu aktualisieren, führen Sie einfach den folgenden Befehl in Ihrem Projektverzeichnis aus:

```
pod update
```
{% endtab %}

{% tab Manuell %}
#### Schritt 1.1: Laden Sie das Braze SDK herunter {#step-11-download-the-braze-sdk}

Rufen Sie die [Braze SDK Release-Seite auf GitHub](https://github.com/braze-inc/braze-swift-sdk/releases) auf und laden Sie `braze-swift-sdk-prebuilt.zip` herunter.

![„Die Braze SDK-Release-Seite auf GitHub.“]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### Schritt 1.2: Wählen Sie Ihre Frameworks aus {#step-12-choose-your-frameworks}

Das Braze Swift SDK enthält eine Vielzahl von eigenständigen XCFrameworks, die Ihnen die Freiheit geben, nur die gewünschten Features zu integrieren&#8212;ohne alle integrieren zu müssen. Verwenden Sie die folgende Tabelle, um Ihre XCFrameworks auszuwählen:

| Paket                      | Erforderlich? | Beschreibung                                                                                                                                                                                                                                                                                                                         |
| -------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Ja            | Haupt-SDK-Bibliothek mit Unterstützung für Analytics und Push-Benachrichtigungen.                                                                                                                                                                                                                                                    |
| `BrazeLocation`            | Nein          | Standortbibliothek mit Unterstützung für Standortanalysen und Geofence-Überwachung.                                                                                                                                                                                                                                                 |
| `BrazeUI`                  | Nein          | Von Braze bereitgestellte Benutzeroberflächen-Bibliothek für In-App-Nachrichten, Content Cards und Banner. Importieren Sie diese Bibliothek, wenn Sie die Standard-UI-Komponenten verwenden möchten.                                                                                                                                 |
| `BrazeNotificationService` | Nein          | Erweiterungsbibliothek für Benachrichtigungsdienste mit Unterstützung für Rich-Push-Benachrichtigungen. Fügen Sie diese Bibliothek nicht direkt zu Ihrem Hauptanwendungsziel hinzu, sondern [fügen Sie die `BrazeNotificationService`-Bibliothek separat hinzu](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications). |
| `BrazePushStory`           | Nein          | Erweiterungsbibliothek für Benachrichtigungsinhalte mit Unterstützung für Push Stories. Fügen Sie diese Bibliothek nicht direkt zu Ihrem Hauptanwendungsziel hinzu, sondern [fügen Sie die `BrazePushStory`-Bibliothek separat hinzu](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                   |
| `BrazeKitCompat`           | Nein          | Kompatibilitätsbibliothek mit allen `Appboy`- und `ABK*`-Klassen und -Methoden, die in der `Appboy-iOS-SDK` Version 4.X.X verfügbar waren. Einzelheiten zur Verwendung finden Sie im minimalen Migrationsszenario im [Migrationshandbuch](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `BrazeUICompat`            | Nein          | Kompatibilitätsbibliothek mit allen `ABK*`-Klassen und -Methoden, die in der `AppboyUI`-Bibliothek der `Appboy-iOS-SDK` Version 4.X.X verfügbar waren. Einzelheiten zur Verwendung finden Sie im minimalen Migrationsszenario im [Migrationshandbuch](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | Nein          | Abhängigkeit, die nur von `BrazeUICompat` im minimalen Migrationsszenario verwendet wird.                                                                                                                                                                                                                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 1.2: Choose your frameworks" }

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 aria-label="Step 1.2: Choose your frameworks" }

#### Schritt 1.3: Bereiten Sie Ihre Dateien vor {#step-13-prepare-your-files}

Entscheiden Sie, ob Sie **statische** oder **dynamische** XCFrameworks verwenden möchten, und bereiten Sie dann Ihre Dateien vor:

1. Erstellen Sie ein temporäres Verzeichnis für Ihre XCFrameworks.
2. Öffnen Sie in `braze-swift-sdk-prebuilt` das Verzeichnis `dynamic` und verschieben Sie `BrazeKit.xcframework` in Ihr Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Verschieben Sie jedes der von Ihnen [gewählten XCFrameworks](#swift_step-2-choose-your-frameworks) in Ihr temporäres Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### Schritt 1.4: Integrieren Sie Ihre Frameworks {#step-14-integrate-your-frameworks}

Als Nächstes integrieren Sie die **dynamischen** oder **statischen** XCFrameworks, die Sie [zuvor vorbereitet haben](#swift_step-3-prepare-your-files):

Wählen Sie in Ihrem Xcode-Projekt Ihr Build-Target und dann **General**. Ziehen Sie die [zuvor vorbereiteten Dateien](#swift_step-3-prepare-your-files) per Drag-and-Drop unter **Frameworks, Libraries, and Embedded Content**.

![„Ein Beispiel-Xcode-Projekt, bei dem jede Braze-Bibliothek auf „Embed & Sign“ eingestellt ist."]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
Ab dem Swift SDK 12.0.0 sollten Sie für die Braze XCFrameworks stets **Embed & Sign** sowohl für die statische als auch für die dynamische Variante auswählen. Dadurch wird sichergestellt, dass die Ressourcen des Frameworks ordnungsgemäß in Ihr App-Bundle eingebettet werden.
{% endalert %}

{% alert tip %}
Um die GIF-Unterstützung zu aktivieren, fügen Sie `SDWebImage.xcframework` hinzu, das sich entweder in `braze-swift-sdk-prebuilt/static` oder `braze-swift-sdk-prebuilt/dynamic` befindet.
{% endalert %}

#### Häufige Fehler bei Objective-C-Projekten {#common-errors-for-objective-c-projects}

Wenn Ihr Xcode-Projekt nur Objective-C-Dateien enthält, erhalten Sie möglicherweise „Missing Symbol“-Fehler, wenn Sie versuchen, Ihr Projekt zu erstellen. Um diese Fehler zu beheben, öffnen Sie Ihr Projekt und fügen Sie eine leere Swift-Datei zu Ihrem Dateibaum hinzu. Dadurch wird Ihre Build-Toolchain gezwungen, [Swift Runtime](https://support.apple.com/kb/dl1998) einzubetten und während der Build-Zeit eine Verbindung zu den entsprechenden Frameworks herzustellen.

```bash
FILE_NAME.swift
```

Ersetzen Sie `FILE_NAME` durch einen beliebigen String ohne Leerzeichen. Ihre Datei sollte etwa so aussehen:

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### 2. Schritt: Verzögerte Initialisierung einrichten (optional) {#step-2-set-up-delayed-initialization-optional}

Sie haben die Möglichkeit, die Initialisierung des Braze Swift SDK zu verzögern. Dies ist nützlich, wenn Ihre App vor dem Start des SDK eine Konfiguration laden oder auf die Zustimmung der Nutzer:innen warten muss. Die verzögerte Initialisierung stellt sicher, dass Braze-Push-Benachrichtigungen und Push-Token, die vor der SDK-Initialisierung empfangen wurden, in die Warteschlange gestellt und nach der Initialisierung des SDK verarbeitet werden.

Um die verzögerte Initialisierung zu verwenden, ist die folgende Mindestversion des Braze SDK erforderlich:
{% sdk_min_versions swift:11.2.0 %}

#### Schritt 2.1: Vorbereitung auf die verzögerte Initialisierung {#step-21-prepare-for-delayed-initialization}

Rufen Sie `Braze.prepareForDelayedInitialization()` so früh wie möglich im Lebenszyklus Ihrer App auf, idealerweise in oder vor `application(_:didFinishLaunchingWithOptions:)`. Dadurch wird sichergestellt, dass Push-Benachrichtigungen, die vor der SDK-Initialisierung empfangen wurden, ordnungsgemäß erfasst und später verarbeitet werden.

{% alert note %}
Dies gilt ausschließlich für Push-Benachrichtigungen von Braze. Andere Push-Benachrichtigungen werden normal von Systemdelegierten verarbeitet.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];

  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

Bei Verwendung der verzögerten Initialisierung wird die Push-Automatisierung implizit aktiviert. Sie können [die Push-Automatisierungskonfiguration anpassen](#swift_step-23-customize-push-automation-optional), indem Sie einen `pushAutomation`-Parameter übergeben.

#### Schritt 2.2: Konfigurieren Sie das Verhalten der Push-Analytics (optional) {#step-22-configure-push-analytics-behavior-optional}

Wenn die verzögerte Initialisierung aktiviert ist, werden Push-Analytics standardmäßig in eine Warteschlange gestellt. Sie können jedoch auch explizit festlegen, dass Push-Analytics in die Warteschlange gestellt oder verworfen werden sollen.

##### Explizit in die Warteschlange stellen {#explicitly-queue}

Um Push-Analytics explizit in die Warteschlange zu stellen (Standardverhalten), übergeben Sie `.queue` an den `analyticsBehavior`-Parameter. Push-Analytics-Ereignisse, die vor der Initialisierung in die Warteschlange gestellt wurden, werden bei der Initialisierung verarbeitet und an den Server gesendet.

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .queue)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

##### Verwerfen {#drop}

Um Push-Analytics zu verwerfen, die vor der SDK-Initialisierung empfangen wurden, übergeben Sie `.drop` an den `analyticsBehavior`-Parameter. Mit dieser Option werden alle Push-Analytics-Ereignisse, die auftreten, während das SDK nicht initialisiert ist, ignoriert.

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .drop)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorDrop];
```
{% endtab %}
{% endtabs %}

#### Schritt 2.3: Push-Automatisierung anpassen (optional) {#step-23-customize-push-automation-optional}

Sie können die Push-Automatisierungskonfiguration anpassen, indem Sie einen `pushAutomation`-Parameter übergeben. Standardmäßig sind alle Automatisierungs-Features aktiviert, mit Ausnahme von `requestAuthorizationAtLaunch`.

{% tabs local %}
{% tab SWIFT %}
```swift
// Enable all push automation
featuresBraze.prepareForDelayedInitialization(pushAutomation: true)

// Or customize specific automation options
let automation = Braze.Configuration.Push.Automation()
automation.automaticSetup = true
automation.requestAuthorizationAtLaunch = false
Braze.prepareForDelayedInitialization(pushAutomation: automation)
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
// Enable all push automation features
[Braze prepareForDelayedInitializationWithPushAutomation:[[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES]];

// Or customize specific automation options
BRZConfigurationPushAutomation *automation = [[BRZConfigurationPushAutomation alloc] init];
automation.automaticSetup = YES;
automation.requestAuthorizationAtLaunch = NO;
[Braze prepareForDelayedInitializationWithPushAutomation:automation analyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

#### Schritt 2.4: Initialisieren Sie das SDK {#step-24-initialize-the-sdk}

Nach Ablauf der von Ihnen gewählten Verzögerungszeit (beispielsweise nach dem Abrufen der Konfiguration von einem Server oder nach der Zustimmung der Nutzer:innen) initialisieren Sie das SDK wie gewohnt:

{% tabs local %}
{% tab SWIFT %}
```swift
func initializeBraze() {
  let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")

  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = true
  let braze = Braze(configuration: configuration)

  // Store the Braze instance for later use
  AppDelegate.braze = braze
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (void)initializeBraze {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"YOUR-API-KEY" endpoint:@"YOUR-ENDPOINT"];

  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  Braze *braze = [[Braze alloc] initWithConfiguration:configuration];

  // Store the Braze instance for later use
  AppDelegate.braze = braze;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
Bei der Initialisierung des SDK werden alle in der Warteschlange befindlichen Push-Benachrichtigungen, Push-Token und Deeplinks automatisch verarbeitet.
{% endalert %}

### 3. Schritt: Aktualisieren Sie Ihren App-Delegierten {#step-3-update-your-app-delegate}

{% alert important %}
Im Folgenden wird davon ausgegangen, dass Sie bereits einen `AppDelegate` zu Ihrem Projekt hinzugefügt haben (dieser wird nicht standardmäßig generiert) und dass Sie das Feature zur verzögerten Initialisierung nicht verwenden. Falls Sie keinen `AppDelegate` verwenden möchten, stellen Sie sicher, dass Sie das Braze SDK so früh wie möglich initialisieren, beispielsweise beim Start der App. Wenn Sie das Feature zur verzögerten Initialisierung verwenden, lesen Sie [Schritt 2.4](#swift_step-24-initialize-the-sdk) zur Initialisierung des SDK und überspringen Sie diesen Schritt.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
Fügen Sie die folgende Codezeile in Ihre `AppDelegate.swift`-Datei ein, um die im Braze Swift SDK enthaltenen Features zu importieren:

```swift
import BrazeKit
```

Als Nächstes fügen Sie der Klasse `AppDelegate` eine statische Eigenschaft hinzu, um während der gesamten Lifetime Ihrer Anwendung eine starke Referenz auf die Braze-Instanz zu behalten:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

Das SDK erfordert, dass Ihre Anwendung während der gesamten Nutzung eine starke Referenz auf die Braze-Instanz behält. Um unerwartete Nebeneffekte zu vermeiden, stellen Sie sicher, dass Sie diese Referenz vollständig erfasst haben, bevor Sie auf Eigenschaften oder Methoden der Braze-Instanz zugreifen oder diese ändern.

Fügen Sie schließlich in `AppDelegate.swift` das folgende Snippet zu Ihrer Methode `application:didFinishLaunchingWithOptions:` hinzu:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

Aktualisieren Sie `YOUR-APP-IDENTIFIER-API-KEY` und `YOUR-BRAZE-ENDPOINT` mit dem korrekten Wert von Ihrer **App-Einstellungen**-Seite. Sehen Sie sich unsere [API-Bezeichner-Typen]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) an, um mehr darüber zu erfahren, wo Sie Ihren App-Bezeichner-API-Schlüssel finden.

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Fügen Sie die folgende Codezeile in Ihre `AppDelegate.m`-Datei ein:

```objc
@import BrazeKit;
```

Als Nächstes fügen Sie eine statische Variable in Ihre `AppDelegate.m`-Datei ein, um während der gesamten Lifetime Ihrer Anwendung eine Referenz auf die Braze-Instanz zu behalten:

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

Das SDK erfordert, dass Ihre Anwendung während der gesamten Nutzung eine starke Referenz auf die Braze-Instanz behält. Um unerwartete Nebeneffekte zu vermeiden, stellen Sie sicher, dass Sie diese Referenz vollständig erfasst haben, bevor Sie auf Eigenschaften oder Methoden der Braze-Instanz zugreifen oder diese ändern.

Fügen Sie schließlich in Ihrer `AppDelegate.m`-Datei das folgende Snippet zur Methode `application:didFinishLaunchingWithOptions:` hinzu:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

Aktualisieren Sie `YOUR-APP-IDENTIFIER-API-KEY` und `YOUR-BRAZE-ENDPOINT` mit dem richtigen Wert von Ihrer Seite **Einstellungen verwalten**. In unserer [API-Dokumentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) finden Sie weitere Informationen darüber, wo Sie den API-Schlüssel für Ihre App-Kennung finden.

{% endsubtab %}
{% endsubtabs local %}

## Optionale Konfigurationen {#optional-configurations}

### Protokollierung {#logging}

Für eine zentralisierte Übersicht über alle Plattformen hinweg siehe [Ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/). Informationen zum Interpretieren der Protokollausgabe finden Sie unter [Ausführliche Protokolle lesen]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs/).

#### Protokollstufen {#log-levels}

Die Standard-Protokollstufe für das Braze Swift SDK ist `.error`&#8212;dies ist auch die minimal unterstützte Stufe, wenn die Protokollierung aktiviert ist. Dies ist die vollständige Liste der Protokollstufen:

| Swift       | Objective-C              | Beschreibung                                                       |
| ----------- | ------------------------ | ------------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | Debugging-Informationen protokollieren + `.info` + `.error`.       |
| `.info`     | `BRZLoggerLevelInfo`     | Allgemeine SDK-Informationen protokollieren (Nutzer:innen-Änderungen usw.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Fehler protokollieren.                                             |
| `.disabled` | `BRZLoggerLevelDisabled` | Es erfolgt keine Protokollierung.                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Log levels" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Log levels" }

#### Einstellen der Protokollstufe {#setting-the-log-level}

Sie können die Protokollstufe zur Laufzeit in Ihrem `Braze.Configuration`-Objekt zuweisen. Ausführliche Informationen zur Verwendung finden Sie unter [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}