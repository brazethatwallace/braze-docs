## Voraussetzungen {#prerequisites}

{% tabs local %}
{% tab iOS %}
Bevor Sie Deeplinking in Ihrer Flutter-iOS-App implementieren können, konfigurieren Sie Ihre URL-Schemata in Ihrer `Info.plist`-Datei. Weitere Informationen finden Sie unter [Deeplinking für iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#url-schemes).
{% endtab %}

{% tab Android %}
Für Flutter Android ist kein zusätzliches natives Setup erforderlich, wenn Sie Deeplinks auf der Dart-Ebene verarbeiten. Die in diesem Artikel gezeigte minimale Implementierung ist für die meisten Flutter-Apps ausreichend.

{% alert warning %}
Das native Flag `com_braze_handle_push_deep_links_automatically` von Braze ist auf Android standardmäßig auf `false` gesetzt. Ohne es in Ihrer `braze.xml` auf `true` zu setzen, wird Ihre App nicht automatisch in den Vordergrund gebracht oder zum Deeplink-Ziel weitergeleitet, wenn Nutzer:innen auf eine Push-Benachrichtigung tippen, obwohl ein `push_opened`-Ereignis dennoch Ihren Dart-Listener erreicht. Weitere Informationen finden Sie unter [Deeplinks hinzufügen (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android).
{% endalert %}

Wenn Sie eine erweiterte Linkverarbeitung auf nativer Ebene benötigen (z. B. angepasste `IBrazeDeeplinkHandler`-Implementierungen), lesen Sie bitte [Deeplinking für Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android).
{% endtab %}
{% endtabs %}

## Deeplinking implementieren {#implementing-deep-linking}

### 1. Schritt: Flutters integrierte Verarbeitung einrichten {#step-1-set-up-flutters-built-in-handling}

{% tabs %}
{% tab iOS %}
1. Öffnen Sie in Ihrem Xcode-Projekt die Datei `Info.plist`.
2. Fügen Sie ein neues Schlüssel-Wert-Paar hinzu.
3. Setzen Sie den Schlüssel auf `FlutterDeepLinkingEnabled`.
4. Setzen Sie den Typ auf `Boolean`.
5. Setzen Sie den Wert auf `YES`.
    ![Die Info.plist-Datei eines Beispielprojekts mit dem hinzugefügten Schlüssel-Wert-Paar.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File"){: width="501" height="118"}
{% endtab %}

{% tab Android %}
1. Öffnen Sie in Ihrem Android-Studio-Projekt die Datei `AndroidManifest.xml`.
2. Suchen Sie `.MainActivity` in Ihren `activity`-Tags.
3. Fügen Sie innerhalb des `activity`-Tags das folgende `meta-data`-Tag hinzu:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### 2. Schritt: Daten an die Dart-Schicht weiterleiten (optional) {#step-2-forward-data-to-the-dart-layer-optional}

Sie können native, eigene oder Drittanbieter-Linkverarbeitung für komplexe Anwendungsfälle verwenden, z. B. um Nutzer:innen an einen bestimmten Ort in Ihrer App zu leiten oder eine bestimmte Funktion aufzurufen.

#### Beispiel: Deeplinking zu einem Alert-Dialog {#example-deep-linking-to-an-alert-dialog}

{% alert note %}
Obwohl das folgende Beispiel keine zusätzlichen Pakete erfordert, können Sie einen ähnlichen Ansatz verwenden, um native, eigene oder Drittanbieter-Pakete zu implementieren, wie z. B. [`go_router`](https://pub.dev/packages/go_router). Zusätzlicher Dart-Code kann erforderlich sein.
{% endalert %}

Zunächst wird ein Method Channel in der nativen Schicht verwendet, um die URL-String-Daten des Deeplinks an die Dart-Schicht weiterzuleiten.

{% tabs %}
{% tab iOS %}
```swift
extension AppDelegate {

  // Delegate method for handling custom scheme links.
  override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    forwardURL(url)
    return true
  }

  // Delegate method for handling universal links.
  override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
      return false
    }
    forwardURL(url)
    return true
  }

  private func forwardURL(_ url: URL) {
    guard let controller: FlutterViewController = window?.rootViewController as? FlutterViewController else { return }
    let deepLinkChannel = FlutterMethodChannel(name: "deepLinkChannel", binaryMessenger: controller.binaryMessenger)
    deepLinkChannel.invokeMethod("receiveDeepLink", arguments: url.absoluteString)
  }

}
```
{% endtab %}

{% tab Android %}
```kotlin
class MainActivity : FlutterActivity() {

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    handleDeepLink(intent)
  }

  override fun onNewIntent(intent: Intent) {
      super.onNewIntent(intent)
    handleDeepLink(intent)
  }

  private fun handleDeepLink(intent: Intent) {
    val binaryMessenger = flutterEngine?.dartExecutor?.binaryMessenger
    if (intent?.action == Intent.ACTION_VIEW && binaryMessenger != null) {
      MethodChannel(binaryMessenger, "deepLinkChannel")
        .invokeMethod("receivedDeepLink", intent?.data.toString())
    }
  }

}
```
{% endtab %}
{% endtabs %}

Anschließend wird eine Callback-Funktion in der Dart-Schicht verwendet, um einen Alert-Dialog mit den zuvor gesendeten URL-String-Daten anzuzeigen.

```dart
MethodChannel('deepLinkChannel').setMethodCallHandler((call) async {
  deepLinkAlert(call.arguments, context);
});

void deepLinkAlert(String link, BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text("Deep Link Alert"),
        content: Text("Opened with deep link: $link"),
        actions: <Widget>[
          TextButton(
            child: Text("Close"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}
```
