## Requisitos previos {#prerequisites}

{% tabs local %}
{% tab iOS %}
Antes de que puedas implementar la vinculación en profundidad en tu aplicación Flutter para iOS, configura tus esquemas de URL en tu archivo `Info.plist`. Para más detalles, consulta [Vinculación en profundidad para iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#url-schemes).
{% endtab %}

{% tab Android %}
Para Flutter en Android, no se requiere configuración nativa adicional si gestionas los vínculos profundos en la capa Dart. La implementación mínima que se muestra en este artículo es suficiente para la mayoría de las aplicaciones Flutter.

Si necesitas una gestión avanzada de enlaces en la capa nativa (como implementaciones personalizadas de `IBrazeDeeplinkHandler`), consulta [Vinculación en profundidad para Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android).
{% endtab %}
{% endtabs %}

## Implementar la vinculación en profundidad {#implementing-deep-linking}

### Paso 1: Configurar el manejo integrado de Flutter {#step-1-set-up-flutters-built-in-handling}

{% tabs %}
{% tab iOS %}
1. En tu proyecto Xcode, abre tu archivo `Info.plist`.
2. Añade un nuevo par clave-valor.
3. Establece la clave como `FlutterDeepLinkingEnabled`.
4. Establece el tipo como `Boolean`.
5. Establece el valor como `YES`.
    ![Archivo `Info.plist` de un proyecto de ejemplo con el par clave-valor añadido.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. En tu proyecto de Android Studio, abre tu archivo `AndroidManifest.xml`.
2. Localiza `.MainActivity` en tus etiquetas `activity`.
3. Dentro de la etiqueta `activity`, añade la siguiente etiqueta `meta-data`:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### Paso 2: Reenviar los datos a la capa Dart (opcional) {#step-2-forward-data-to-the-dart-layer-optional}

Puedes utilizar la gestión de enlaces nativa, de origen o de terceros para casos de uso complejos, como enviar a un usuario a una ubicación concreta de tu aplicación o llamar a una función específica.

#### Ejemplo: vinculación en profundidad a un diálogo de alerta {#example-deep-linking-to-an-alert-dialog}

{% alert note %}
Aunque el siguiente ejemplo no depende de paquetes adicionales, puedes utilizar un enfoque similar para implementar paquetes nativos, de origen o de terceros, como por ejemplo [`go_router`](https://pub.dev/packages/go_router). Puede ser necesario código Dart adicional.
{% endalert %}

En primer lugar, se utiliza un canal de métodos en la capa nativa para reenviar los datos de la cadena URL del vínculo profundo a la capa Dart.

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

A continuación, se utiliza una función de devolución de llamada en la capa Dart para mostrar un diálogo de alerta utilizando los datos de la cadena URL enviados anteriormente.

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
