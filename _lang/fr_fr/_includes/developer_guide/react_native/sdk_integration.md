## À propos du SDK Braze pour React Native {#about-the-react-native-braze-sdk}

L'intégration du SDK Braze pour React Native fournit des fonctionnalités d'analyse de base et vous permet d'intégrer des In-App Messages et des Content Cards pour iOS et Android avec une seule base de code.

## Compatibilité avec la nouvelle architecture {#new-architecture-compatibility}

La version minimale suivante du SDK est compatible avec toutes les applications utilisant la [nouvelle architecture de React Native](https://reactnative.dev/docs/the-new-architecture/landing-page) :

{% sdk_min_versions reactnative:2.0.1 %}

À partir de la version 6.0.0 du SDK, Braze utilise un Turbo Module React Native, compatible à la fois avec la nouvelle architecture et l'architecture bridge héritée. Aucune configuration supplémentaire n'est donc nécessaire.

{% alert warning %}
Si votre application iOS est conforme à `RCTAppDelegate` et suit notre précédente configuration `AppDelegate`, consultez les exemples dans [Configuration native complète](#reactnative_step-2-complete-native-setup) pour éviter les plantages lors de l'abonnement aux événements dans le Turbo Module.
{% endalert %}

## Exigences de version pour React et React Native {#react-and-react-native-version-requirements}

Braze ne publie pas de versions minimales de React distinctes au-delà de ce que le SDK React Native prend en charge. Pour intégrer le SDK, utilisez React Native version 0.71 ou ultérieure. Pour consulter la liste complète des versions de React Native prises en charge, reportez-vous au [dépôt GitHub du SDK React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

Lorsque vous mettez à jour React, React Native ou le SDK Braze, consultez le [journal des modifications](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) du SDK pour vérifier les changements majeurs avant de déployer.

## Intégrer le SDK React Native {#integrating-the-react-native-sdk}

### Conditions préalables {#prerequisites}

Pour connaître les versions de React Native prises en charge et les instructions de mise à niveau, consultez [Exigences de version React et React Native](#react-and-react-native-version-requirements).

### Étape 1 : Intégrer la bibliothèque Braze {#step-1-integrate-the-braze-library}

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

<a id="step-2-choose-a-setup-option"></a>
<a id="reactnative_step-2-complete-native-setup"></a>
### Étape 2 : Effectuer la configuration native {#step-2-complete-native-setup}

Si votre application utilise Expo, consultez [Utiliser le plugin Expo](#reactnative-using-the-expo-plugin). Si votre application utilise React Native pur, consultez [Utiliser React Native CLI](#reactnative-using-react-native-cli).
Choisissez une méthode de configuration dans chaque onglet de version : plugin Expo ou React Native CLI.

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### Méthode 1 : Utiliser le plugin Expo {#reactnative-using-the-expo-plugin}

##### 2.1 Installer le plugin Braze Expo {#21-install-the-braze-expo-plugin}

Assurez-vous que votre version du plugin Braze Expo est au moins 4.1.0. Pour la liste complète des versions prises en charge, consultez le [dépôt du plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

L'extrait de code suivant montre la commande pour installer le plugin Braze Expo :

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 Ajouter le plugin à votre app.json {#22-add-the-plugin-to-your-appjson}

Dans votre `app.json`, ajoutez le plugin Braze Expo. La clé API et l'endpoint ne sont plus définis ici. Fournissez-les au moment de l'exécution via `Braze.initialize()` depuis JavaScript. Ajoutez les paramètres de configuration optionnels suivants en fonction des besoins de votre déploiement :

| Méthode                                       | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | boolean | iOS uniquement. Indique s'il faut utiliser Braze pour gérer les notifications push sur iOS.                       |
| `enableFirebaseCloudMessaging`                | boolean | Android uniquement. Indique s'il faut utiliser Firebase Cloud Messaging pour les notifications push.             |
| `firebaseCloudMessagingSenderId`              | string  | Android uniquement. Votre identifiant d'expéditeur Firebase Cloud Messaging.                                    |
| `sessionTimeout`                              | integer | Le délai d'expiration de session Braze pour votre application, en secondes.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Indique s'il faut activer la fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).      |
| `logLevel`                                    | integer | Le niveau de journalisation pour votre application. Le niveau par défaut est 8 et enregistre un minimum d'informations. Pour activer la journalisation détaillée pour le débogage, utilisez le niveau 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | L'intervalle de temps minimum en secondes entre les déclencheurs. Par défaut : 30 secondes.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Indique si la collecte automatique de la localisation est activée (si l'utilisateur l'autorise).                                                                                  |
| `enableGeofence`                              | boolean | Indique si les géorepérages sont activés.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Indique si les requêtes de géorepérage doivent être effectuées automatiquement.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOS uniquement. Indique si un message in-app modal est fermé lorsque l'utilisateur clique en dehors du message in-app.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Android uniquement. Indique si le SDK Braze doit gérer automatiquement les deep links des notifications push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Android uniquement. Définit si le contenu textuel d'une notification push doit être interprété et rendu en HTML à l'aide de `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Android uniquement. Définit la couleur d'accentuation des notifications Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Android uniquement. Définit la grande icône des notifications Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Android uniquement. Définit la petite icône des notifications Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOS uniquement. Indique si l'utilisateur doit être automatiquement invité à accorder les autorisations push au lancement de l'application.                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOS uniquement. Indique s'il faut activer les fonctionnalités de push riche pour iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOS uniquement. Indique s'il faut activer Braze Push Stories pour iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOS uniquement. Le groupe d'applications utilisé pour iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | iOS uniquement. Indique si l'identifiant de l'appareil utilise un UUID généré aléatoirement.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | iOS uniquement. Indique si le SDK doit automatiquement reconnaître et transmettre les liens universels aux méthodes système (par défaut : `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2.2 Ajouter le plugin à votre app.json" }

L'extrait de code suivant montre un exemple de configuration `app.json` :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ]
    ]
  }
}
```

###### Configurer les icônes de notification push Android {#android-push-icons}

Lorsque vous utilisez `androidNotificationLargeIcon` et `androidNotificationSmallIcon`, suivez ces bonnes pratiques pour un affichage correct des icônes :

**Emplacement et format des icônes**

Pour utiliser des icônes de notification push personnalisées avec le plugin Braze Expo :

1. Créez vos fichiers d'icônes en respectant les exigences listées dans la section Exigences relatives aux icônes.
2. Placez-les dans les répertoires natifs Android de votre projet à l'emplacement `android/app/src/main/res/drawable-<density>/`.
   Par exemple, utilisez `android/app/src/main/res/drawable-mdpi/` et `android/app/src/main/res/drawable-hdpi/`.
3. Alternativement, si vous gérez les ressources dans votre répertoire React Native, vous pouvez utiliser la [configuration d'icône app.json d'Expo](https://docs.expo.dev/versions/latest/config/app/#icon) ou créer un [plugin de configuration Expo](https://docs.expo.dev/config-plugins/introduction/) pour copier les icônes dans les dossiers drawable Android lors du prebuild.

Le plugin Braze Expo référence ces icônes en utilisant le système de ressources drawable d'Android.

**Exigences relatives aux icônes**

- **Petite icône :** doit être une silhouette blanche sur fond transparent (c'est une exigence de la plateforme Android).
- **Grande icône :** peut être une image en couleur.
- **Format :** le format PNG est recommandé.
- **Nommage :** utilisez uniquement des lettres minuscules, des chiffres et des underscores (par exemple, `my_large_icon.png`).

**Configuration dans app.json**

L'extrait de code suivant montre comment référencer les icônes de notification Android dans `app.json` en utilisant le préfixe `@drawable/` :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
N'utilisez pas de chemins de fichiers relatifs (tels que `src/assets/images/icon.png`) et n'incluez pas l'extension de fichier lorsque vous référencez des icônes. Le plugin Expo nécessite le préfixe `@drawable/` pour localiser correctement les icônes dans les dossiers natifs Android après le processus de prebuild.
{% endalert %}

**Fonctionnement**

Le plugin Braze Expo référence vos fichiers d'icônes depuis les répertoires `drawable` Android. Lorsque vous exécutez `npx expo prebuild`, Expo génère la structure du projet natif Android. Vos icônes doivent être présentes dans les dossiers `drawable` Android (placées manuellement ou copiées via un plugin de configuration) avant le processus de build. Le plugin configure ensuite le SDK Braze pour utiliser ces ressources drawable par leur nom (sans chemin ni extension), c'est pourquoi le préfixe `@drawable/` est requis dans votre configuration.

Pour plus d'informations sur les icônes de notification Android, consultez les [directives d'icônes de notification Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### 2.3 Compiler et exécuter votre application {#23-build-and-run-your-application}

Le prebuild de votre application génère les fichiers natifs nécessaires au fonctionnement du plugin Braze Expo.

L'extrait de code suivant montre la commande pour effectuer le prebuild de votre application :

```bash
npx expo prebuild
```

Exécutez votre application comme indiqué dans la [documentation Expo](https://docs.expo.dev/workflow/customizing/). Si vous apportez des modifications aux options de configuration, effectuez à nouveau le prebuild et l'exécution de l'application.

#### Méthode 2 : Utiliser React Native CLI {#reactnative-using-react-native-cli}

##### Configurer Android {#set-up-android}

**2.1 Ajouter le plugin Kotlin Gradle**

L'extrait de code suivant montre comment ajouter le plugin Kotlin Gradle dans le fichier `build.gradle` de niveau supérieur de votre projet, sous `buildscript` > `dependencies` :

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Cela ajoute Kotlin à votre projet.

**2.2 Configurer le SDK Braze**

Créez un fichier `braze.xml` dans le dossier `res/values` de votre projet. La clé API et l'endpoint sont fournis au moment de l'exécution depuis JavaScript, ils ne sont donc pas requis dans ce fichier. L'extrait de code suivant montre comment activer l'initialisation différée avec `com_braze_enable_delayed_initialization` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
Vous pouvez toujours ajouter d'autres valeurs de configuration natives dans `braze.xml` (telles que les paramètres de push, de délai d'expiration de session et de journalisation). Celles-ci sont appliquées automatiquement lorsque `Braze.initialize()` est appelé depuis JavaScript.
{% endalert %}

L'extrait de code suivant montre les autorisations requises pour votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
À partir de la version 12.2.0 du SDK Android de Braze, vous pouvez importer automatiquement la bibliothèque android-sdk-location en définissant `importBrazeLocationLibrary=true` dans votre fichier `gradle.properties`.
{% endalert %}

**2.3 Implémenter le suivi des sessions utilisateur**

Les appels à `openSession()` et `closeSession()` sont gérés automatiquement.
L'extrait de code suivant montre ce qu'il faut ajouter à la méthode `onCreate()` de votre classe `MainApplication` :

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**2.4 Gérer les mises à jour d'intent**

Si votre MainActivity a `android:launchMode` défini sur `singleTask`, l'extrait de code suivant montre ce qu'il faut ajouter à votre classe `MainActivity` :

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### Configurer iOS {#set-up-ios}

**2.5 (Optionnel) Configurer le Podfile pour les XCFrameworks dynamiques**

Pour importer certaines bibliothèques Braze, telles que BrazeUI, dans un fichier Objective-C++, vous devez utiliser la syntaxe `#import`. À partir de la version `7.4.0` du SDK Swift de Braze, les binaires disposent d'un [canal de distribution optionnel sous forme de XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), compatibles avec cette syntaxe.

Si vous souhaitez utiliser ce canal de distribution, remplacez manuellement les emplacements source CocoaPods dans votre Podfile. Référencez cet exemple et remplacez `{your-version}` par la version souhaitée :

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Installer les pods**

Étant donné que React Native lie automatiquement les bibliothèques à la plateforme native, vous pouvez installer le SDK à l'aide de CocoaPods.

L'extrait de code suivant montre comment installer les pods depuis le dossier racine du projet :

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Configurer le SDK Braze**

Utilisez `BrazeReactInitializer.configure` dans votre `AppDelegate` pour enregistrer la configuration native. Les closures que vous fournissez sont stockées et appliquées ultérieurement lorsque `Braze.initialize(apiKey, endpoint)` est appelé depuis JavaScript.

{% subtabs local %}
{% subtab SWIFT %}

L'extrait de code suivant montre comment importer le SDK Braze en haut du fichier `AppDelegate.swift` :

```swift
import BrazeKit
import braze_react_native_sdk
```

Dans la méthode `application(_:didFinishLaunchingWithOptions:)`, enregistrez votre configuration native à l'aide de `BrazeReactInitializer.configure`. Ne définissez pas la clé API ni l'endpoint ici. Ils sont fournis depuis JavaScript via `Braze.initialize()`.

- **Closure `configure`** : reçoit un objet `Braze.Configuration` et vous permet de définir les propriétés de configuration natives (journalisation, push, sessions, etc.).
- **Closure `postInitialization`** _(optionnelle)_ : reçoit l'instance `Braze` active après sa création, pour les configurations nécessitant l'instance (par exemple, stocker une référence ou définir des délégués).

L'extrait de code suivant montre un exemple d'implémentation `AppDelegate.swift` utilisant `BrazeReactInitializer.configure` :

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    BrazeReactInitializer.configure { configuration in
      configuration.logger.level = .info
      configuration.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup

    return true
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

L'extrait de code suivant montre comment importer le SDK Braze en haut du fichier `AppDelegate.m` :

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

Dans la méthode `application:didFinishLaunchingWithOptions:`, enregistrez votre configuration native à l'aide de `BrazeReactInitializer`. Ne définissez pas la clé API ni l'endpoint ici. Ils sont fournis depuis JavaScript via `Braze.initialize()`.

L'extrait de code suivant montre un exemple d'implémentation `AppDelegate.m` utilisant `BrazeReactInitializer` :

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazeReactInitializer configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  } postInitialization:^(Braze *braze) {
    // Store the Braze instance for later use.
  }];

  /* Other configuration */

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazeReactInitializer.configure()` ne fait que stocker votre configuration. Aucune instance Braze n'existe tant que `Braze.initialize()` n'est pas appelé depuis JavaScript. N'appelez donc aucune méthode du SDK Braze dans l'AppDelegate après `configure()`.
Lorsque vous appelez à nouveau `Braze.initialize()`, les mêmes blocs `configure` et `postInitialization` sont appliqués à la nouvelle instance Braze.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 et antérieur %}

#### Méthode 1 : Utiliser le plugin Expo {#method-1-using-the-expo-plugin}

##### Étape 2.1 : Installer le plugin Braze Expo {#step-21-install-the-braze-expo-plugin}

Assurez-vous que votre version du SDK React Native de Braze est au moins 1.37.0. Pour la liste complète des versions prises en charge, consultez le [dépôt React Native de Braze](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

L'extrait de code suivant montre la commande pour installer le plugin Braze Expo :

```bash
npx expo install @braze/expo-plugin
```

##### Étape 2.2 : Ajouter le plugin à votre app.json {#step-22-add-the-plugin-to-your-appjson}

Dans votre `app.json`, ajoutez le plugin Braze Expo. Vous pouvez fournir les options de configuration suivantes :

| Méthode                                       | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Requis. La [clé API]({{site.baseurl}}/api/identifier_types) pour votre application Android, située dans votre tableau de bord de Braze sous **Gérer les paramètres**. |
| `iosApiKey`                                   | string  | Requis. La [clé API]({{site.baseurl}}/api/identifier_types) pour votre application iOS, située dans votre tableau de bord de Braze sous **Gérer les paramètres**.     |
| `baseUrl`                                     | string  | Requis. L'[endpoint SDK]({{site.baseurl}}/api/basics#endpoints) pour votre application, situé dans votre tableau de bord de Braze sous **Gérer les paramètres**.    |
| `enableBrazeIosPush`                          | boolean | iOS uniquement. Indique s'il faut utiliser Braze pour gérer les notifications push sur iOS. Introduit dans le SDK React Native v1.38.0 et le plugin Expo v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Android uniquement. Indique s'il faut utiliser Firebase Cloud Messaging pour les notifications push. Introduit dans le SDK React Native v1.38.0 et le plugin Expo v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Android uniquement. Votre identifiant d'expéditeur Firebase Cloud Messaging. Introduit dans le SDK React Native v1.38.0 et le plugin Expo v0.4.0.                                    |
| `sessionTimeout`                              | integer | Le délai d'expiration de session Braze pour votre application, en secondes.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Indique s'il faut activer la fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).      |
| `logLevel`                                    | integer | Le niveau de journalisation pour votre application. Le niveau par défaut est 8 et enregistre un minimum d'informations. Pour activer la journalisation détaillée pour le débogage, utilisez le niveau 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | L'intervalle de temps minimum en secondes entre les déclencheurs. Par défaut : 30 secondes.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Indique si la collecte automatique de la localisation est activée (si l'utilisateur l'autorise).                                                                                  |
| `enableGeofence`                              | boolean | Indique si les géorepérages sont activés.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Indique si les requêtes de géorepérage doivent être effectuées automatiquement.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOS uniquement. Indique si un message in-app modal est fermé lorsque l'utilisateur clique en dehors du message in-app.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Android uniquement. Indique si le SDK Braze doit gérer automatiquement les deep links des notifications push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Android uniquement. Définit si le contenu textuel d'une notification push doit être interprété et rendu en HTML à l'aide de `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Android uniquement. Définit la couleur d'accentuation des notifications Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Android uniquement. Définit la grande icône des notifications Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Android uniquement. Définit la petite icône des notifications Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOS uniquement. Indique si l'utilisateur doit être automatiquement invité à accorder les autorisations push au lancement de l'application.                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOS uniquement. Indique s'il faut activer les fonctionnalités de push riche pour iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOS uniquement. Indique s'il faut activer Braze Push Stories pour iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOS uniquement. Le groupe d'applications utilisé pour iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | iOS uniquement. Indique si l'identifiant de l'appareil utilisera un UUID généré aléatoirement.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | iOS uniquement. Indique si le SDK doit automatiquement reconnaître et transmettre les liens universels aux méthodes système (par défaut : `false`). Lorsque cette option est activée, le SDK transmet automatiquement les liens universels aux méthodes système définies dans [Prise en charge des liens universels dans votre application](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introduit dans le SDK React Native v11.1.0 et le plugin Expo v3.2.0. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2.2 : Ajouter le plugin à votre app.json" }

L'extrait de code suivant montre un exemple de configuration `app.json` :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

###### Configurer les icônes de notification push Android {#configuring-android-push-notification-icons}

Lorsque vous utilisez `androidNotificationLargeIcon` et `androidNotificationSmallIcon`, suivez ces bonnes pratiques pour un affichage correct des icônes :

**Emplacement et format des icônes**

Pour utiliser des icônes de notification push personnalisées avec le plugin Braze Expo :

1. Créez vos fichiers d'icônes en respectant les exigences listées dans la section Exigences relatives aux icônes.
2. Placez-les dans les répertoires natifs Android de votre projet à l'emplacement `android/app/src/main/res/drawable-<density>/` (par exemple, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/`, ou similaire).
3. Alternativement, si vous gérez les ressources dans votre répertoire React Native, vous pouvez utiliser la [configuration d'icône app.json d'Expo](https://docs.expo.dev/versions/latest/config/app/#icon) ou créer un [plugin de configuration Expo](https://docs.expo.dev/config-plugins/introduction/) pour copier les icônes dans les dossiers drawable Android lors du prebuild.

Le plugin Braze Expo référence ces icônes en utilisant le système de ressources drawable d'Android.

**Exigences relatives aux icônes**

- **Petite icône :** doit être une silhouette blanche sur fond transparent (c'est une exigence de la plateforme Android).
- **Grande icône :** peut être une image en couleur.
- **Format :** le format PNG est recommandé.
- **Nommage :** utilisez uniquement des lettres minuscules, des chiffres et des underscores (par exemple, `my_large_icon.png`).

**Configuration dans app.json**

L'extrait de code suivant montre comment référencer les icônes de notification Android dans `app.json` en utilisant le préfixe `@drawable/` :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
N'utilisez pas de chemins de fichiers relatifs (tels que `src/assets/images/icon.png`) et n'incluez pas l'extension de fichier lorsque vous référencez des icônes. Le plugin Expo nécessite le préfixe `@drawable/` pour localiser correctement les icônes dans les dossiers natifs Android après le processus de prebuild.
{% endalert %}

**Fonctionnement**

Le plugin Braze Expo référence vos fichiers d'icônes depuis les répertoires `drawable` Android. Lorsque vous exécutez `npx expo prebuild`, Expo génère la structure du projet natif Android. Vos icônes doivent être présentes dans les dossiers `drawable` Android (placées manuellement ou copiées via un plugin de configuration) avant le processus de build. Le plugin configure ensuite le SDK Braze pour utiliser ces ressources drawable par leur nom (sans chemin ni extension), c'est pourquoi le préfixe `@drawable/` est requis dans votre configuration.

Pour plus d'informations sur les icônes de notification Android, consultez les [directives d'icônes de notification Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### Étape 2.3 : Compiler et exécuter votre application {#step-23-build-and-run-your-application}

Le prebuild de votre application génère les fichiers natifs nécessaires au fonctionnement du plugin Braze Expo.

L'extrait de code suivant montre la commande pour effectuer le prebuild de votre application :

```bash
npx expo prebuild
```

Exécutez votre application comme indiqué dans la [documentation Expo](https://docs.expo.dev/workflow/customizing/). Gardez à l'esprit que si vous apportez des modifications aux options de configuration, vous devrez effectuer à nouveau le prebuild et l'exécution de l'application.

#### Méthode 2 : Utiliser React Native CLI {#method-2-using-react-native-cli}

##### Configurer Android

**Étape 2.1 : Ajouter le plugin Kotlin Gradle**

L'extrait de code suivant montre comment ajouter le plugin Kotlin Gradle dans le fichier `build.gradle` de niveau supérieur de votre projet, sous `buildscript` > `dependencies` :

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Cela ajoute Kotlin à votre projet.

**Étape 2.2 : Configurer le SDK Braze**

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `res/values` de votre projet. L'extrait de code suivant montre un exemple de configuration `braze.xml`. Remplacez la [clé]({{site.baseurl}}/api/identifier_types) API et l'[endpoint]({{site.baseurl}}/api/basics#endpoints) par vos valeurs :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

L'extrait de code suivant montre les autorisations requises pour votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
À partir de la version 12.2.0 du SDK Android de Braze, vous pouvez importer automatiquement la bibliothèque android-sdk-location en définissant `importBrazeLocationLibrary=true` dans votre fichier `gradle.properties`.
{% endalert %}

**Étape 2.3 : Implémenter le suivi des sessions utilisateur**

Les appels à `openSession()` et `closeSession()` sont gérés automatiquement.
L'extrait de code suivant montre ce qu'il faut ajouter à la méthode `onCreate()` de votre classe `MainApplication` :

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**Étape 2.4 : Gérer les mises à jour d'intent**

Si votre MainActivity a `android:launchMode` défini sur `singleTask`, l'extrait de code suivant montre ce qu'il faut ajouter à votre classe `MainActivity` :

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### Configurer iOS

**Étape 2.5 : (Optionnel) Configurer le Podfile pour les XCFrameworks dynamiques**

Pour importer certaines bibliothèques Braze, telles que BrazeUI, dans un fichier Objective-C++, vous devez utiliser la syntaxe `#import`. À partir de la version `7.4.0` du SDK Swift de Braze, les binaires disposent d'un [canal de distribution optionnel sous forme de XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), compatibles avec cette syntaxe.

Si vous souhaitez utiliser ce canal de distribution, remplacez manuellement les emplacements source CocoaPods dans votre Podfile. L'extrait de code suivant montre un exemple de remplacement. Remplacez `{your-version}` par la version souhaitée :

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**Étape 2.6 : Installer les pods**

Étant donné que React Native lie automatiquement les bibliothèques à la plateforme native, vous pouvez installer le SDK à l'aide de CocoaPods.

L'extrait de code suivant montre comment installer les pods depuis le dossier racine du projet :

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**Étape 2.7 : Configurer le SDK Braze**

{% subtabs local %}
{% subtab SWIFT %}

L'extrait de code suivant montre comment importer le SDK Braze en haut du fichier `AppDelegate.swift` :
```swift
import BrazeKit
import braze_react_native_sdk
```

Dans la méthode `application(_:didFinishLaunchingWithOptions:)`, remplacez la [clé]({{site.baseurl}}/api/identifier_types) API et l'[endpoint]({{site.baseurl}}/api/basics#endpoints) par les valeurs de votre application. Ensuite, créez l'instance Braze à l'aide de la configuration et créez une propriété statique sur l'`AppDelegate` pour un accès facile.

{% alert note %}
Notre exemple suppose une implémentation de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), qui fournit un certain nombre d'abstractions dans la configuration React Native. Si vous utilisez une configuration différente pour votre application, veillez à adapter votre implémentation en conséquence.
{% endalert %}

L'extrait de code suivant montre un exemple de configuration `AppDelegate.swift` :

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

L'extrait de code suivant montre comment importer le SDK Braze en haut du fichier `AppDelegate.m` :
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

Dans la méthode `application:didFinishLaunchingWithOptions:`, remplacez la [clé]({{site.baseurl}}/api/identifier_types) API et l'[endpoint]({{site.baseurl}}/api/basics#endpoints) par les valeurs de votre application. Ensuite, créez l'instance Braze à l'aide de la configuration et créez une propriété statique sur l'`AppDelegate` pour un accès facile.

{% alert note %}
Notre exemple suppose une implémentation de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), qui fournit un certain nombre d'abstractions dans la configuration React Native. Si vous utilisez une configuration différente pour votre application, veillez à adapter votre implémentation en conséquence.
{% endalert %}

L'extrait de code suivant montre un exemple de configuration `AppDelegate.m` :

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### Étape 3 : Initialiser le SDK {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

L'extrait de code suivant montre comment importer la bibliothèque dans votre code React Native :

```javascript
import Braze from "@braze/react-native-sdk";
```

{% alert note %}
Le SDK React Native 19.2.0+ prend en charge l'initialisation de Braze depuis la couche React Native ou depuis les couches natives iOS et Android. Initialisez depuis la couche React Native pour utiliser l'[initialisation différée](#delayed-initialization), qui démarre le SDK après un événement tel qu'un consentement ou une connexion. Si votre application initialise Braze dans les couches natives aujourd'hui, vous pouvez conserver cette configuration lors de la mise à niveau. Pour vérifier le comportement des notifications dans chaque configuration, consultez [Notifications push au démarrage à froid](#push-notifications-on-cold-start).
{% endalert %}

Ensuite, appelez `Braze.initialize()` avec votre clé API d'identifiant d'application et l'endpoint SDK pour créer l'instance Braze. Consultez les options suivantes pour savoir où appeler cette méthode dans le flux de votre application.

#### Initialisation standard {#standard-initialization}

L'extrait de code suivant montre comment initialiser le SDK au démarrage de votre application en appelant `Braze.initialize()` dans un `useEffect` :

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
  }, []);

  return (
    // Your app components
  );
};
```

#### Initialisation différée {#delayed-initialization}

L'extrait de code suivant montre comment différer l'initialisation du SDK à un moment ultérieur de la session. Par exemple, après que l'utilisateur a donné son consentement ou s'est connecté :

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
Sur iOS, les notifications push reçues avant `Braze.initialize()` sont mises en file d'attente et traitées après l'initialisation. Sur Android, Braze ne résout pas les deep links des notifications push tant que le SDK attend d'être initialisé. Pour que les notifications continuent de fonctionner lorsque l'une d'elles lance votre application, consultez [Notifications push au démarrage à froid](#push-notifications-on-cold-start).
{% endalert %}

#### Clés API spécifiques à la plateforme {#platform-specific-api-keys}

L'extrait de code suivant montre comment utiliser la détection de plateforme lorsque vos applications Android et iOS utilisent des clés API différentes :

```javascript
import { Platform } from "react-native";
import Braze from "@braze/react-native-sdk";

const apiKey = Platform.select({
  android: "YOUR-ANDROID-API-KEY",
  ios: "YOUR-IOS-API-KEY",
}) ?? "";

Braze.initialize(apiKey, "YOUR-SDK-ENDPOINT");
```

#### Réinitialisation {#re-initialization}

Vous pouvez appeler `Braze.initialize()` plusieurs fois pour réinitialiser le SDK avec une clé API et un endpoint différents en cours de session. Chaque appel détruit l'instance Braze précédente et en crée une nouvelle.

{% alert important %}
Tous les appels de méthodes SDK effectués avant `Braze.initialize()` sont ignorés sur iOS. Appelez donc `Braze.initialize()` avant d'utiliser toute autre méthode Braze.
{% endalert %}

#### Notifications push au démarrage à froid {#push-notifications-on-cold-start}

Lorsqu'une notification lance votre application depuis un état terminé, Braze stocke le payload de la notification dans la couche native avant le chargement de React Native. De ce fait, l'initialisation depuis la couche React Native ne modifie pas la réception du payload par votre application. Pour gérer ces notifications, ajoutez les hooks natifs, puis lisez le payload dans votre code React Native.

Sur Android, appelez `BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)` dans la méthode `onCreate()` de votre classe `MainActivity` :

```kotlin
import com.braze.reactbridge.BrazeReactUtils

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
}
```

Sur iOS, appelez `populateInitialPayload(fromLaunchOptions:)` dans la méthode `application(_:didFinishLaunchingWithOptions:)` de votre `AppDelegate` :

```swift
if let launchOptions {
  BrazeReactUtils.sharedInstance().populateInitialPayload(fromLaunchOptions: launchOptions)
}
```

Ensuite, lisez le payload dans votre code React Native :

```javascript
Braze.getInitialPushPayload((pushPayload) => {
  if (pushPayload) {
    // Handle the notification, such as navigating to the pushPayload.url value
  }
});
```

{% alert important %}
Lorsque l'initialisation différée est activée sur Android, Braze ouvre votre activité principale au lieu de résoudre le deep link de la notification, puis transmet les données de la notification à cette activité. Gérez la navigation dans votre code React Native en utilisant la valeur `url` de `Braze.getInitialPushPayload()`.
{% endalert %}

Vos paramètres d'enregistrement push restent dans votre configuration native pour les deux emplacements d'initialisation, et Braze les applique lorsque `Braze.initialize()` s'exécute :

- Sur Android, définissez `com_braze_firebase_cloud_messaging_registration_enabled` et `com_braze_firebase_cloud_messaging_sender_id` dans `braze.xml`.
- Sur iOS, définissez les propriétés `push` sur l'objet de configuration dans la closure `configure` que vous passez à `BrazeReactInitializer.configure`.

Si votre application dépend des deep links provenant de notifications qui la lancent depuis un état terminé, utilisez le SDK React Native 21.1.0 ou ultérieur. Ces versions incluent des correctifs pour la capture du payload push initial et la résolution des deep links push sur Android. Pour la liste complète des modifications, consultez le [journal des modifications du SDK React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md).

{% endtab %}
{% tab React Native SDK 19.1.0 et antérieur %}

Pour le SDK React Native 19.1.0 et antérieur, l'initialisation native s'effectue à l'étape 2. Importez la bibliothèque dans votre code React Native pour appeler les méthodes Braze. Pour plus de détails, consultez notre [projet d'exemple](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject).

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### Étape 4 : Tester l'intégration (optionnel) {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

Vous pouvez vérifier que le SDK est intégré en consultant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur l'une ou l'autre plateforme, vous devriez voir une nouvelle session dans le tableau de bord (dans la section **Aperçu**).

L'extrait de code suivant montre comment ouvrir une session pour un utilisateur particulier dans votre application :

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

Recherchez l'utilisateur avec `{some-user-id}` dans le tableau de bord sous **Audience** > **Rechercher des utilisateurs**. Vous pouvez y vérifier que les données de session et d'appareil ont été enregistrées.

{% endtab %}
{% tab React Native SDK 19.1.0 et antérieur %}

Pour tester votre intégration SDK, l'extrait de code suivant montre comment démarrer une nouvelle session sur l'une ou l'autre plateforme pour un utilisateur.

```javascript
Braze.changeUser("userId");
```

L'extrait de code suivant montre un exemple d'attribution de l'identifiant utilisateur au démarrage de l'application :

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Dans le tableau de bord de Braze, accédez à [Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) et recherchez l'utilisateur dont l'identifiant correspond à `some-user-id`. Vous pouvez y vérifier que les données de session et d'appareil ont été enregistrées.

{% endtab %}
{% endtabs %}

## Étapes suivantes {#next-steps}

Après avoir intégré le SDK Braze, vous pouvez commencer à implémenter les fonctionnalités de communication courantes :

- [Notifications push]({{site.baseurl}}/developer_guide/push_notifications) : Configurez et envoyez des notifications push à vos utilisateurs.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages) : Affichez des messages contextuels dans votre application.
- [Bannières]({{site.baseurl}}/developer_guide/banners) : Affichez des bannières persistantes dans l'interface de votre application.