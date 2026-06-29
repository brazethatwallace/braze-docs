## Voraussetzungen {#prerequisites}

{% tabs local %}
{% tab iOS %}
Bevor Sie Deeplinking in Ihre Flutter-iOS-App implementieren können, konfigurieren Sie Ihre URL-Schemata in Ihrer `Info.plist`-Datei. Weitere Informationen finden Sie unter [Deeplinking für iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#url-schemes).
{% endtab %}

{% tab Android %}
Für Flutter Android ist kein zusätzliches natives Setup erforderlich, wenn Sie Deeplinks auf der Dart-Schicht verarbeiten. Die in diesem Artikel gezeigte minimale Implementierung ist für die meisten Flutter-Apps ausreichend.

Wenn Sie eine erweiterte Linkverarbeitung auf nativer Ebene benötigen (z. B. angepasste `IBrazeDeeplinkHandler`-Implementierungen), lesen Sie [Deeplinking für Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android).
{% endtab %}
{% endtabs %}

## Deeplinking implementieren {#implementing-deep-linking}

### 1. Schritt: Die in Flutter integrierte Verarbeitung einrichten {#step-1-set-up-flutters-built-in-handling}

{% tabs %}
{% tab iOS %}
1. Öffnen Sie in Ihrem Xcode-Projekt die Datei `Info.plist`.
2. Fügen Sie ein neues Schlüssel-Wert-Paar hinzu.
3. Setzen Sie den Schlüssel auf `FlutterDeepLinkingEnabled`.
4. Setzen Sie den Typ auf `Boolean`.
5. Setzen Sie den Wert auf `YES`.
    ![Die `Info.plist`-Datei eines Beispielprojekts mit dem hinzugefügten Schlüssel-Wert-Paar.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. Öffnen Sie in Ihrem Android Studio-Projekt die Datei `AndroidManifest.xml`.
2. Suchen Sie `.MainActivity` in Ihren `activity`-Tags.
3. Fügen Sie innerhalb des `activity`-Tags den folgenden `meta-data`-Tag hinzu:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### 2. Schritt: Daten an die Dart-Schicht weiterleiten (optional) {#step-2-forward-data-to-the-dart-layer-optional}

Sie können native Linkverarbeitung, Erstanbieter- oder Drittanbieter-Linkverarbeitung für komplexe Anwendungsfälle verwenden, z. B. um Nutzer:innen an einen bestimmten Ort in Ihrer App zu schicken oder eine bestimmte Funktion aufzurufen.

#### Beispiel: Deeplinking zu einem Warndialog {#example-deep-linking-to-an-alert-dialog}

{% alert note %}
Das folgende Beispiel basiert zwar nicht auf zusätzlichen Paketen, aber Sie können einen ähnlichen Ansatz verwenden, um native Pakete, Erstanbieter- oder Drittanbieter-Pakete zu implementieren, wie z. B. [`go_router`](https://pub.dev/packages/go_router). Zusätzlicher Dart-Code kann erforderlich sein.
{% endalert %}

Zunächst wird im nativen Layer ein Methodenkanal verwendet, um die URL-String-Daten des Deeplinks an den Dart-Layer weiterzuleiten.

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

Als Nächstes wird eine Callback-Funktion im Dart-Layer verwendet, um einen Warndialog mit den zuvor gesendeten URL-String-Daten anzuzeigen.

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
