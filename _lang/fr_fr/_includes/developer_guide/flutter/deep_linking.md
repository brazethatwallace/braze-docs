## Prérequis {#prerequisites}

{% tabs local %}
{% tab iOS %}
Avant de pouvoir implémenter la création de liens profonds dans votre application Flutter iOS, configurez vos schémas d'URL dans votre fichier `Info.plist`. Pour plus de détails, consultez [Création de liens profonds pour iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#url-schemes).
{% endtab %}

{% tab Android %}
Pour Flutter Android, aucune configuration native supplémentaire n'est requise si vous gérez les liens profonds au niveau de la couche Dart. L'implémentation minimale présentée dans cet article est suffisante pour la plupart des applications Flutter.

{% alert warning %}
Le flag natif `com_braze_handle_push_deep_links_automatically` de Braze est défini par défaut sur `false` sous Android. Sans le définir sur `true` dans votre `braze.xml`, votre application n'est pas automatiquement mise au premier plan ni redirigée vers la destination du lien profond lorsqu'un utilisateur appuie sur une notification push, même si un événement `push_opened` atteint toujours votre listener Dart. Pour plus d'informations, consultez [Ajouter des liens profonds (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android).
{% endalert %}

Si vous avez besoin d'une gestion avancée des liens au niveau natif (comme des implémentations personnalisées de `IBrazeDeeplinkHandler`), consultez [Création de liens profonds pour Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android).
{% endtab %}
{% endtabs %}

## Déploiement de la création de liens profonds {#implementing-deep-linking}

### Étape 1 : Configurer la gestion intégrée de Flutter {#step-1-set-up-flutters-built-in-handling}

{% tabs %}
{% tab iOS %}
1. Dans votre projet Xcode, ouvrez votre fichier `Info.plist`.
2. Ajoutez une nouvelle paire clé-valeur.
3. Définissez la clé sur `FlutterDeepLinkingEnabled`.
4. Définissez le type sur `Boolean`.
5. Définissez la valeur sur `YES`.
    ![Exemple de fichier Info.plist d'un projet avec la paire clé-valeur ajoutée.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. Dans votre projet Android Studio, ouvrez votre fichier `AndroidManifest.xml`.
2. Localisez `.MainActivity` dans vos balises `activity`.
3. À l'intérieur de la balise `activity`, ajoutez la balise `meta-data` suivante :
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### Étape 2 : Transmettre les données à la couche Dart (facultatif) {#step-2-forward-data-to-the-dart-layer-optional}

Vous pouvez utiliser la gestion native, propriétaire ou tierce des liens pour des cas d'usage complexes, comme envoyer un utilisateur vers un emplacement spécifique dans votre application ou appeler une fonction spécifique.

#### Exemple : Deep link vers une boîte de dialogue d'alerte {#example-deep-linking-to-an-alert-dialog}

{% alert note %}
Bien que l'exemple suivant ne repose pas sur des packages supplémentaires, vous pouvez utiliser une approche similaire pour déployer des packages natifs, propriétaires ou tiers, tels que [`go_router`](https://pub.dev/packages/go_router). Du code Dart supplémentaire peut être nécessaire.
{% endalert %}

Tout d'abord, un canal de méthode est utilisé dans la couche native pour transmettre les données de la chaîne d'URL du deep link à la couche Dart.

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

Ensuite, une fonction de rappel est utilisée dans la couche Dart pour afficher une boîte de dialogue d'alerte à l'aide des données de la chaîne d'URL envoyées précédemment.

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
