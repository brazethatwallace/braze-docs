{% multi_lang_include developer_guide/prerequisites/swift.md %}

{% alert tip %}
Für Unterstützung bei der Auswahl zwischen angepassten Schema-Deeplinks, universellen Links und „Open Web URL Inside App“ lesen Sie den [iOS-Deeplinking-Leitfaden]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Informationen zur Fehlerbehebung finden Sie unter [Fehlerbehebung bei Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).
{% endalert %}

## Handhabung von Deeplinks {#handling-deep-links}

### 1. Schritt: Ein Schema Registrierung or registrieren {#register-a-scheme}

Um Deeplinking zu ermöglichen, muss ein angepasstes Schema in Ihrer `Info.plist`-Datei angegeben sein. Die Navigationsstruktur wird durch ein Array von Wörterbüchern definiert. Jedes dieser Wörterbücher enthält ein String-Array.

Verwenden Sie Xcode, um Ihre `Info.plist`-Datei zu bearbeiten:

1. Fügen Sie einen neuen Schlüssel hinzu, `URL types`. Xcode macht daraus automatisch ein Array, das ein Wörterbuch namens `Item 0` enthält.
2. Fügen Sie innerhalb von `Item 0` einen Schlüssel `URL identifier` hinzu. Stellen Sie den Wert auf Ihr angepasstes Schema ein.
3. Fügen Sie innerhalb von `Item 0` einen Schlüssel `URL Schemes` hinzu. Dies wird automatisch ein Array sein, das einen `Item 0`-String enthält.
4. Stellen Sie `URL Schemes` >> `Item 0` auf Ihr angepasstes Schema ein.

Wenn Sie Ihre `Info.plist`-Datei direkt bearbeiten möchten, können Sie auch dieser Spezifikation folgen:

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

### 2. Schritt: Eine Schema-Allowlist hinzufügen {#step-2-add-a-scheme-allowlist}

Sie müssen die URL-Schemata, die Sie an `canOpenURL(_:)` übergeben möchten, deklarieren, indem Sie den Schlüssel `LSApplicationQueriesSchemes` in die Datei Info.plist Ihrer App einfügen. Der Versuch, Schemata außerhalb dieser Allowlist aufzurufen, führt dazu, dass das System einen Fehler in den Protokollen des Geräts aufzeichnet und der Deeplink nicht geöffnet wird. Ein Beispiel für diesen Fehler sieht wie folgt aus:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Wenn zum Beispiel eine In-App-Nachricht beim Antippen die Facebook-App öffnen soll, muss die App das angepasste Schema von Facebook (`fb`) in Ihrer Allowlist haben. Andernfalls wird das System den Deeplink ablehnen. Deeplinks, die auf eine Seite oder Ansicht innerhalb Ihrer eigenen App verweisen, erfordern nach wie vor, dass das angepasste Schema Ihrer App in der `Info.plist` Ihrer App aufgeführt ist.

Ihre Beispiel-Allowlist könnte etwa so aussehen:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

Weitere Informationen finden Sie in der [Dokumentation von Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) zum Schlüssel `LSApplicationQueriesSchemes`.

### 3. Schritt: Einen Handler implementieren {#step-3-implement-a-handler}

Apps, die mit Xcode 27 oder höher erstellt wurden, müssen den [`UIScene`-Lebenszyklus](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) übernehmen, sodass iOS angepasste Schema-URLs über [`scene:openURLContexts:`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:openurlcontexts:)) an Ihren `SceneDelegate` übergibt, anstatt an Ihren `AppDelegate`. Das wichtige Argument ist das [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL)-Objekt.

{% tabs %}
{% tab swift %}

```swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let url = URLContexts.first?.url else { return }
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSURL *url = URLContexts.allObjects.firstObject.URL;
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
}
```

{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Ihre App den `UIScene`-Lebenszyklus noch nicht übernommen hat, ruft iOS stattdessen [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc) auf Ihrem `AppDelegate` auf:

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```
{% endalert %}

## App Transport Security (ATS)

Laut [Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14) ist „App Transport Security ein Feature, das die Sicherheit der Verbindungen zwischen einer App und Webdiensten verbessert. Das Feature besteht aus Standard-Verbindungsanforderungen, die den Best Practices für sichere Verbindungen entsprechen. Apps können dieses Standardverhalten außer Kraft setzen und die Transportsicherheit deaktivieren.“

ATS wird standardmäßig angewendet. Es erfordert, dass alle Verbindungen HTTPS verwenden und mit TLS 1.2 mit Forward Secrecy verschlüsselt werden. Weitere Informationen finden Sie unter [Requirements for Connecting Using ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35). Alle Bilder, die von Braze an Endgeräte geliefert werden, werden von einem Content Delivery Network („CDN“) verarbeitet, das TLS 1.2 unterstützt und mit ATS kompatibel ist.

Sofern sie nicht als Ausnahmen in der `Info.plist` Ihrer Anwendung angegeben sind, schlagen Verbindungen, die diese Anforderungen nicht erfüllen, mit Fehlern fehl, die den folgenden ähneln.

**Beispielfehler 1:**

```bash
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

**Beispielfehler 2:**

```bash
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

Die ATS-Konformität wird für Links durchgesetzt, die innerhalb der mobilen App geöffnet werden (unsere Standardbehandlung von angeklickten Links), und gilt nicht für Websites, die extern über einen Webbrowser geöffnet werden.

### Arbeiten mit ATS {#working-with-ats}

Sie können ATS auf eine der folgenden Arten handhaben, aber wir empfehlen, **die ATS-Anforderungen zu erfüllen**.

{% tabs local %}
{% tab Einhalten %}
Ihre Braze-Integration kann die ATS-Anforderungen erfüllen, indem Sie sicherstellen, dass alle bestehenden Links, zu denen Sie Nutzer:innen weiterleiten (z. B. durch In-App-Nachrichten und Push-Campaigns), die ATS-Anforderungen erfüllen. Es gibt zwar Möglichkeiten, die ATS-Beschränkungen zu umgehen, aber unsere Empfehlung ist sicherzustellen, dass alle verlinkten URLs ATS-konform sind. Da Apple immer mehr Wert auf die Sicherheit von Anwendungen legt, werden die folgenden Ansätze zur Zulassung von ATS-Ausnahmen von Apple nicht garantiert unterstützt.
{% endtab %}

{% tab Teilweise deaktivieren %}
Sie können zulassen, dass eine Teilmenge von Links mit bestimmten Domains oder Schemata als Ausnahmen von den ATS-Regeln behandelt werden. Ihre Braze-Integration erfüllt die ATS-Anforderungen, wenn jeder Link, den Sie in einem Braze-Messaging-Kanal verwenden, entweder ATS-konform ist oder durch eine Ausnahme behandelt wird.

Um eine Domain als Ausnahme des ATS hinzuzufügen, fügen Sie Folgendes in die Datei `Info.plist` Ihrer App ein:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

Weitere Informationen finden Sie in Apples Artikel über [App-Transport-Sicherheitsschlüssel](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33).
{% endtab %}

{% tab Vollständig deaktivieren %}
Sie können ATS vollständig deaktivieren. Beachten Sie, dass dies aufgrund des verlorenen Sicherheitsschutzes und der zukünftigen iOS-Kompatibilität nicht empfohlen wird. Um ATS zu deaktivieren, fügen Sie Folgendes in die Datei `Info.plist` Ihrer App ein:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
{% endtab %}
{% endtabs %}

## URLs dekodieren {#decoding-urls}

Das SDK or Software-Development-Kit kodiert Links prozentual, um gültige `URL`s zu erstellen. Alle Link-Zeichen, die in einer korrekt geformten URL nicht zulässig sind, wie z. B. Unicode-Zeichen, werden prozentual escaped.

Um einen kodierten Link zu dekodieren, verwenden Sie die `String`-Eigenschaft [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding). Sie müssen außerdem `true` in `BrazeDelegate.braze(_:shouldOpenURL:)` zurückgeben. Ein Call-to-Action ist erforderlich, um die Verarbeitung der URL durch Ihre App zu Trigger or triggern or triggern. Zum Beispiel in Ihrem [`scene:openURLContexts:`](#step-3-implement-a-handler)-Handler aus [Schritt 3](#step-3-implement-a-handler):

{% tabs %}
{% tab swift %}

```swift
  func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    guard let url = URLContexts.first?.url else { return }
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSURL *url = URLContexts.allObjects.firstObject.URL;
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
}
```

{% endtab %}
{% endtabs %}

## Deeplinking zu App-Einstellungen {#deep-linking-to-app-settings}

Sie können `UIApplicationOpenSettingsURLString` nutzen, um Nutzer:innen über Push-Benachrichtigungen und In-App-Nachrichten von Braze einen Deeplink zu den Einstellungen Ihrer App zu setzen.

Um Nutzer:innen aus Ihrer App in die iOS-Einstellungen zu bringen:
1. Vergewissern Sie sich zunächst, dass Ihre Anwendung entweder für [schemabasierte Deeplinks](#swift_register-a-scheme) oder für [universelle Links](#swift_universal-links) eingerichtet ist.
2. Legen Sie eine URI für Deeplinking zur Seite **Einstellungen** fest (z. B. `myapp://settings` oder `https://www.braze.com/settings`).
3. Wenn Sie angepasste schemabasierte Deeplinks verwenden, fügen Sie den folgenden Code zu Ihrem `scene:openURLContexts:`-Handler hinzu:

{% tabs %}
{% tab swift %}

```swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let path = URLContexts.first?.url.path else { return }
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSString *path  = [URLContexts.allObjects.firstObject.URL path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
}
```

{% endtab %}
{% endtabs %}

## Anpassungsoptionen {#customization-options}

### Standard-WebView-Anpassung {#default-webview-customization}

Die Klasse `Braze.WebViewController` zeigt vom SDK or Software-Development-Kit geöffnete Web-URLs an, typischerweise wenn für einen Web-Deeplink „Open Web URL Inside App“ ausgewählt wurde.

Sie können den `Braze.WebViewController` über die Delegate-Methode [`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/) anpassen.

### Anpassung der Link-Handhabung {#linking-handling-customization}

Das Protokoll `BrazeDelegate` kann verwendet werden, um die Handhabung von URLs wie Deeplinks, Web-URLs und universellen Links anzupassen. Um den Delegaten während der Initialisierung von Braze zu setzen, setzen Sie ein Delegate-Objekt auf die `Braze`-Instanz. Braze ruft dann die Implementierung von `shouldOpenURL` in Ihrem Delegaten auf, bevor es URIs verarbeitet.

Wenn eine Push-Benachrichtigung oder In-App-Nachricht **Web-URL in der mobilen App öffnen** verwendet, übergibt Braze `context.useWebView == true` an [`Braze.URLContext`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/urlcontext). Wenn die Nachricht die URL stattdessen im Systembrowser öffnet, ist `useWebView` `false`. Prüfen Sie `context.useWebView` in `braze(_:shouldOpenURL:)`, um Ihre angepasste Handhabung zu verzweigen – zum Beispiel, um einen In-App-`WebViewController` nur dann zu öffnen, wenn die Campaign die In-App-Anzeige angefordert hat.

#### Universelle Links {#universal-links}

Braze unterstützt universelle Links in Push-Benachrichtigungen, In-App-Nachrichten und Content Cards. Um die Unterstützung für universelle Links zu aktivieren, muss [`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) auf `true` gesetzt sein.

Wenn diese Funktion aktiviert ist, leitet Braze universelle Links über die Methode [`scene:continue:`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:continue:)) an Ihren `SceneDelegate` weiter, wenn Ihre App den `UIScene`-Lebenszyklus übernommen hat (erforderlich für Apps, die mit Xcode 27 oder höher erstellt wurden), oder über [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) an Ihren `AppDelegate`.

Ihre Anwendung muss ebenfalls für den Umgang mit universellen Links eingerichtet sein. Lesen Sie die [Dokumentation von Apple](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app), um sicherzustellen, dass Ihre Anwendung korrekt für universelle Links konfiguriert ist.

{% alert warning %}
Die Weiterleitung universeller Links erfordert den Zugriff auf die Anwendungsberechtigungen. Wenn Sie die Anwendung in einem Simulator ausführen, sind diese Berechtigungen nicht direkt verfügbar und universelle Links werden nicht an die System-Handler weitergeleitet.
Um die Unterstützung für Simulator-Builds hinzuzufügen, können Sie die `.entitlements`-Datei der Anwendung in der Build-Phase _Copy Bundle Resources_ hinzufügen. Weitere Details finden Sie in der Dokumentation zu [`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks).
{% endalert %}

{% alert note %}
Das SDK or Software-Development-Kit fragt die `apple-app-site-association`-Datei Ihrer Domains nicht ab. Es unterscheidet zwischen universellen Links und regulären URLs, indem es nur den Domain-Namen betrachtet. Infolgedessen beachtet das SDK or Software-Development-Kit keine Ausschlussregel, die in der `apple-app-site-association` gemäß [Unterstützung zugehöriger Domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) definiert ist.
{% endalert %}

## Beispiele {#examples}

### BrazeDelegate

Hier ist ein Beispiel mit `BrazeDelegate`. Weitere Informationen finden Sie in der [Braze Swift SDK or Software-Development-Kit-Referenz](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate).

{% tabs %}
{% tab swift %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}