## Intégration du SDK .NET MAUI {#integrating-the-net-maui-sdk}

L'intégration du SDK Braze .NET MAUI (anciennement Xamarin) vous fournira des fonctionnalités d'analyse de base ainsi que des messages in-app qui vous permettront d'interagir avec vos utilisateurs.

### Conditions préalables {#prerequisites}

Avant de pouvoir réaliser l'intégration du SDK Braze .NET MAUI, veuillez vous assurer que vous répondez aux exigences suivantes :

- À partir de la `version 3.0.0`, ce SDK nécessite l'utilisation de .NET 6+ et supprime la prise en charge des projets utilisant le framework Xamarin.
- À partir de la `version 4.0.0`, ce SDK a cessé de prendre en charge Xamarin et Xamarin.Forms et a ajouté la prise en charge de .NET MAUI. Consultez [la politique de Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) concernant la fin du support pour Xamarin.

### Étape 1 : Obtenir la liaison .NET MAUI {#step-1-get-the-net-maui-binding}

{% tabs %}
{% tab android %}
Une liaison .NET MAUI est un moyen d'utiliser des bibliothèques natives dans les applications .NET MAUI. L'implémentation d'une liaison consiste à créer une interface C# avec la bibliothèque, puis à utiliser cette interface dans votre application. Consultez la [documentation .NET MAUI](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/). Il existe deux façons d'inclure la liaison du SDK de Braze : en utilisant NuGet ou en compilant à partir de la source.

{% subtabs local %}
{% subtab NuGet %}
La méthode d'intégration la plus simple consiste à obtenir le SDK de Braze à partir du dépôt central [NuGet.org](https://www.nuget.org/). Dans la barre latérale de Visual Studio, faites un clic droit sur le dossier `Packages` et cliquez sur `Add Packages...`. Recherchez « Braze » et installez le package [`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) dans votre projet.

Pour utiliser les services de localisation et les géorepérages de Braze, installez également le package [`BrazePlatform.BrazeAndroidLocationBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidLocationBinding/).
{% endsubtab %}

{% subtab Source %}
La deuxième méthode d'intégration consiste à inclure la [source de liaison](https://github.com/braze-inc/braze-xamarin-sdk). Sous [`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding), vous trouverez notre code source de liaison ; l'ajout d'une référence de projet au fichier `BrazeAndroidBinding.csproj` dans votre application .NET MAUI entraînera la création de la liaison avec votre projet et vous donnera accès au SDK Android de Braze.

Pour utiliser les services de localisation et les géorepérages de Braze, ajoutez également une référence de projet au fichier `BrazeAndroidLocationBinding.csproj` situé sous [`appboy-component/src/androidnet6/BrazeAndroidLocationBinding`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidLocationBinding).
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
Les liaisons iOS pour le SDK .NET MAUI version 4.0.0 et ultérieure utilisent le [SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk/), tandis que les versions précédentes utilisent l'[ancien SDK AppboyKit](https://github.com/Appboy/Appboy-ios-sdk).
{% endalert %}

Une liaison .NET MAUI est un moyen d'utiliser des bibliothèques natives dans les applications .NET MAUI. L'implémentation d'une liaison consiste à créer une interface C# avec la bibliothèque, puis à utiliser cette interface dans votre application. Il existe deux façons d'inclure la liaison du SDK de Braze : en utilisant NuGet ou en compilant à partir de la source.

{% subtabs local %}
{% subtab NuGet %}
La méthode d'intégration la plus simple consiste à obtenir le SDK de Braze à partir du dépôt central [NuGet.org](https://www.nuget.org/). Dans la barre latérale de Visual Studio, faites un clic droit sur le dossier `Packages` et cliquez sur `Add Packages...`. Recherchez « Braze » et installez les derniers packages NuGet .NET MAUI iOS : [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit), [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI) et [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation) dans votre projet.

Nous fournissons également les packages de bibliothèques de compatibilité : [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) et [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat), pour faciliter votre migration vers .NET MAUI.
{% endsubtab %}

{% subtab Source %}
La deuxième méthode d'intégration consiste à inclure la [source de liaison](https://github.com/braze-inc/braze-xamarin-sdk). Sous [`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding), vous trouverez notre code source de liaison ; l'ajout d'une référence de projet au fichier `BrazeiOSBinding.csproj` dans votre application .NET MAUI entraînera la création de la liaison avec votre projet et vous donnera accès au SDK iOS de Braze. Assurez-vous que `BrazeiOSBinding.csproj` apparaît dans le dossier « Reference » de votre projet.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 2 : Configurez votre instance Braze {#step-2-configure-your-braze-instance}

{% tabs %}
{% tab android %}
#### Étape 2.1 : Configurez le SDK de Braze dans Braze.xml {#step-21-configure-the-braze-sdk-in-brazexml}

Maintenant que les bibliothèques ont été intégrées, vous devez créer un fichier `Braze.xml` dans le dossier `Resources/values` de votre projet. Le contenu de ce fichier devrait ressembler à l'extrait de code suivant :

{% alert note %}
Veillez à remplacer `YOUR_API_KEY` par la clé API qui se trouve dans **Paramètres** > **Clés API** dans le tableau de bord de Braze.
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
Si vous incluez manuellement la source de la liaison, retirez `<item>NUGET</item>` de votre code.

{% alert tip %}
Pour voir un exemple de `Braze.xml`, consultez notre [exemple d'application Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml).
{% endalert %}

#### Étape 2.2 : Ajouter les autorisations requises au manifeste Android {#step-22-add-required-permissions-to-android-manifest}

Maintenant que vous avez ajouté votre clé API, vous devez ajouter les autorisations suivantes à votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
Pour obtenir un exemple de votre `AndroidManifest.xml`, consultez l'exemple d'application [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml).

#### Étape 2.3 : Suivre les sessions utilisateur et s'enregistrer pour les messages in-app {#step-23-track-user-sessions-and-registering-for-in-app-messages}

Pour activer le suivi des sessions utilisateur et enregistrer votre application pour les messages in-app, ajoutez l'appel suivant à la méthode de cycle de vie `OnCreate()` de la classe `Application` dans votre application :

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Lors de la configuration de votre instance Braze, ajoutez l'extrait de code suivant pour configurer votre instance :

{% alert note %}
Veillez à remplacer `YOUR_API_KEY` par la clé API qui se trouve dans **Paramètres** > **Clés API** dans le tableau de bord de Braze.
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

Consultez le fichier `App.xaml.cs` dans l'exemple d'application [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs).
{% endtab %}
{% endtabs %}

### Étape 3 : Tester l'intégration {#step-3-test-the-integration}

{% tabs %}
{% tab android %}
Vous pouvez désormais lancer votre application et voir les sessions enregistrées dans le tableau de bord de Braze (ainsi que les informations relatives à l'appareil et d'autres données d'analyse). Pour une explication approfondie des bonnes pratiques pour l'intégration SDK de base, consultez les [instructions d'intégration Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
{% endtab %}

{% tab ios %}
Vous pouvez désormais lancer votre application et voir les sessions enregistrées dans le tableau de bord de Braze. Pour une explication approfondie des bonnes pratiques pour l'intégration SDK de base, consultez les [instructions d'intégration iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift).

{% alert important %}
Notre liaison publique .NET MAUI actuelle pour le SDK iOS ne se connecte pas au SDK Facebook iOS (liaison des données sociales) et n'inclut pas l'envoi de l'IDFA à Braze.
{% endalert %}
{% endtab %}
{% endtabs %}