## Pré-requisitos {#prerequisites}

{% tabs local %}
{% tab iOS %}
Antes de implementar deep linking no seu app Flutter para iOS, configure seus esquemas de URL no arquivo `Info.plist`. Para saber mais, consulte [Deep linking para iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#url-schemes).
{% endtab %}

{% tab Android %}
Para Flutter Android, nenhuma configuração nativa adicional é necessária se você estiver lidando com deep links na camada Dart. A implementação mínima mostrada neste artigo é suficiente para a maioria dos apps Flutter.

{% alert warning %}
A flag nativa `com_braze_handle_push_deep_links_automatically` da Braze tem o valor padrão `false` no Android. Sem defini-la como `true` no seu `braze.xml`, o app não é automaticamente trazido para o primeiro plano nem direcionado ao destino do deep link quando um usuário toca em uma notificação por push, mesmo que um evento `push_opened` ainda chegue ao seu listener Dart. Para saber mais, consulte [Adicionar deep links (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android).
{% endalert %}

Se você precisar de tratamento avançado de links na camada nativa (como implementações personalizadas de `IBrazeDeeplinkHandler`), consulte [Deep linking para Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android).
{% endtab %}
{% endtabs %}

## Implementando deep linking {#implementing-deep-linking}

### Etapa 1: Configurar o tratamento nativo do Flutter {#step-1-set-up-flutters-built-in-handling}

{% tabs %}
{% tab iOS %}
1. No seu projeto Xcode, abra o arquivo `Info.plist`.
2. Adicione um novo par chave-valor.
3. Defina a chave como `FlutterDeepLinkingEnabled`.
4. Defina o tipo como `Boolean`.
5. Defina o valor como `YES`.
    ![Exemplo do arquivo Info.plist de um projeto com o par chave-valor adicionado.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. No seu projeto Android Studio, abra o arquivo `AndroidManifest.xml`.
2. Localize `.MainActivity` nas tags `activity`.
3. Dentro da tag `activity`, adicione a seguinte tag `meta-data`:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### Etapa 2: Encaminhar dados para a camada Dart (opcional) {#step-2-forward-data-to-the-dart-layer-optional}

Você pode usar o tratamento de links nativo, próprio ou de terceiros para casos de uso complexos, como enviar um usuário para um local específico no seu app ou chamar uma função específica.

#### Exemplo: Deep linking para uma caixa de diálogo de alerta {#example-deep-linking-to-an-alert-dialog}

{% alert note %}
Embora o exemplo a seguir não dependa de pacotes adicionais, você pode usar uma abordagem semelhante para implementar pacotes nativos, próprios ou de terceiros, como [`go_router`](https://pub.dev/packages/go_router). Código Dart adicional pode ser necessário.
{% endalert %}

Primeiro, um canal de método é usado na camada nativa para encaminhar os dados da string de URL do deep link para a camada Dart.

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

Em seguida, uma função de retorno de chamada é usada na camada Dart para exibir uma caixa de diálogo de alerta usando os dados da string de URL enviados anteriormente.

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
