## À propos du SDK React Native Braze {#about-the-react-native-braze-sdk}

L'intégration du SDK React Native Braze fournit des fonctionnalités d'analyse de base et vous permet d'intégrer des messages in-app et des Content Cards pour iOS et Android à partir d'une seule base de code.

## Compatibilité avec la nouvelle architecture {#new-architecture-compatibility}

La version minimale suivante du SDK est compatible avec toutes les applications utilisant [la nouvelle architecture de React Native](https://reactnative.dev/docs/the-new-architecture/landing-page) :

{% sdk_min_versions reactnative:2.0.1 %}

À partir de la version 6.0.0 du SDK, Braze utilise un module React Native Turbo, compatible à la fois avec la nouvelle architecture et l'architecture pont héritée. Aucune configuration supplémentaire n'est donc nécessaire.

{% alert warning %}
Si votre application iOS est conforme à `RCTAppDelegate` et suit notre configuration `AppDelegate` précédente, consultez les exemples dans [Configuration native complète](#reactnative_step-2-complete-native-setup) pour éviter les plantages lors de l'abonnement à des événements dans le module Turbo.
{% endalert %}

## Exigences de version React et React Native {#react-and-react-native-version-requirements}

Braze ne publie pas de versions minimales de React distinctes au-delà de ce que le SDK React Native prend en charge. Pour intégrer le SDK, utilisez React Native version 0.71 ou ultérieure. Pour obtenir la liste complète des versions React Native prises en charge, consultez le [dépôt GitHub du SDK React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

Lorsque vous mettez à jour React, React Native ou le SDK Braze, consultez le [CHANGELOG](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) du SDK pour vérifier les changements incompatibles avant de déployer.

## Intégration du SDK React Native {#integrating-the-react-native-sdk}

### Conditions préalables {#prerequisites}

Pour les versions React Native prises en charge et les conseils de mise à jour, consultez [Exigences de version React et React Native](#react-and-react-native-version-requirements).

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
### Étape 2 : Configuration native complète {#step-2-complete-native-setup}

Si votre application utilise Expo, consultez [Utiliser le plugin Expo](#reactnative-using-the-expo-plugin). Si votre application utilise React Native pur, consultez [Utiliser React Native CLI](#reactnative-using-react-native-cli).
Choisissez une méthode de configuration dans chaque onglet de version : plugin Expo ou React Native CLI.

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### Méthode 1 : Utiliser le plugin Expo {#reactnative-using-the-expo-plugin}

##### 2.1 Installer le plugin Braze Expo {#21-install-the-braze-expo-plugin}

Assurez-vous que votre version du plugin Braze Expo est au minimum 4.1.0. Pour obtenir la liste complète des versions prises en charge, consultez le [dépôt du plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

L'extrait de code suivant montre la commande pour installer le plugin Braze Expo :

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 Ajouter le plugin à votre app.json {#22-add-the-plugin-to-your-appjson}

Dans votre `app.json`, ajoutez le plugin Braze Expo. La clé API et l'endpoint ne sont plus définis ici. Fournissez-les au moment de l'exécution via `Braze.initialize()` depuis JavaScript. Ajoutez les paramètres de configuration facultatifs suivants en fonction des besoins de votre implémentation :

| Méthode                                       | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | booléen | iOS uniquement. Détermine si Braze gère les notifications push sur iOS.                       |
| `enableFirebaseCloudMessaging`                | booléen | Android uniquement. Détermine si Firebase Cloud Messaging est utilisé pour les notifications push.             |
| `firebaseCloudMessagingSenderId`              | chaîne de caractères  | Android uniquement. Votre ID expéditeur Firebase Cloud Messaging.                                    |
| `sessionTimeout`                              | entier | Le délai d'expiration de session Braze pour votre application, en secondes.                                                                                               |
| `enableSdkAuthentication`                     | booléen | Détermine si la fonctionnalité [Authentification SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication) est activée.      |
| `logLevel`                                    | entier | Le niveau de journalisation pour votre application. Le niveau par défaut est 8 et enregistre un minimum d'informations. Pour activer la journalisation détaillée pour le débogage, utilisez le niveau 0.    |
| `minimumTriggerIntervalInSeconds`             | entier | L'intervalle minimum en secondes entre les déclenchements. 30 secondes par défaut.                                                                           |
| `enableAutomaticLocationCollection`           | booléen | Détermine si la collecte automatique de localisation est activée (si l'utilisateur l'autorise).                                                                                  |
| `enableGeofence`                              | booléen | Détermine si les géorepérages sont activés.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | booléen | Détermine si les demandes de géorepérage doivent être effectuées automatiquement.                                                                                                  |
| `dismissModalOnOutsideTap`                    | booléen | iOS uniquement. Détermine si un message in-app modal est fermé lorsque l'utilisateur clique en dehors du message.                                           |
| `androidHandlePushDeepLinksAutomatically`     | booléen | Android uniquement. Détermine si le SDK Braze doit gérer automatiquement les liens profonds des notifications push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | booléen | Android uniquement. Définit si le contenu textuel d'une notification push doit être interprété et rendu en HTML via `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | chaîne de caractères  | Android uniquement. Définit la couleur d'accentuation des notifications Android.                                                                                                |
| `androidNotificationLargeIcon`                | chaîne de caractères  | Android uniquement. Définit la grande icône des notifications Android.                                                                                                  |
| `androidNotificationSmallIcon`                | chaîne de caractères  | Android uniquement. Définit la petite icône des notifications Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | booléen | iOS uniquement. Détermine si l'utilisateur doit être automatiquement invité à autoriser les notifications push au lancement de l'application.                                                          |
| `enableBrazeIosRichPush`                      | booléen | iOS uniquement. Détermine si les fonctionnalités de push riche sont activées pour iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | booléen | iOS uniquement. Détermine si Braze Push Stories est activé pour iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | chaîne de caractères  | iOS uniquement. Le groupe d'applications utilisé pour iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | booléen | iOS uniquement. Détermine si l'ID de l'appareil utilise un UUID généré aléatoirement.                                                                                       |
| `iosForwardUniversalLinks`                    | booléen | iOS uniquement. Indique si le SDK doit automatiquement reconnaître et transmettre les liens universels aux méthodes système (par défaut : `false`). |
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

###### Configuration des icônes de notification push Android {#android-push-icons}

Lorsque vous utilisez `androidNotificationLargeIcon` et `androidNotificationSmallIcon`, suivez ces bonnes pratiques pour un affichage correct des icônes :

**Emplacement et format des icônes**

Pour utiliser des icônes de notification push personnalisées avec le plugin Braze Expo :

1. Créez vos fichiers d'icônes en respectant les exigences détaillées ci-dessous.
2. Placez-les dans les répertoires natifs Android de votre projet à l'emplacement `android/app/src/main/res/drawable-<density>/`.
   Par exemple, utilisez `android/app/src/main/res/drawable-mdpi/` et `android/app/src/main/res/drawable-hdpi/`.
3. Sinon, si vous gérez vos ressources dans votre répertoire React Native, vous pouvez utiliser la [configuration des icônes app.json](https://docs.expo.dev/versions/latest/config/app/#icon) d'Expo ou créer un [plugin de configuration Expo](https://docs.expo.dev/config-plugins/introduction/) pour copier les icônes dans les dossiers drawable Android pendant la précompilation.

Le plugin Braze Expo fait référence à ces icônes via le système de ressources drawable d'Android.

**Exigences relatives aux icônes**

- **Petite icône :** doit être une silhouette blanche sur fond transparent (exigence de la plateforme Android).
- **Grande icône :** peut être une image en couleur.
- **Format :** le format PNG est recommandé.
- **Nommage :** utilisez uniquement des lettres minuscules, des chiffres et des traits de soulignement (par exemple, `my_large_icon.png`).

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
N'utilisez pas de chemins d'accès relatifs (tels que `src/assets/images/icon.png`) et n'incluez pas l'extension de fichier lorsque vous référencez des icônes. Le plugin Expo nécessite le préfixe `@drawable/` pour localiser correctement les icônes dans les dossiers natifs Android après le processus de précompilation.
{% endalert %}

**Fonctionnement**

Le plugin Braze Expo fait référence à vos fichiers d'icônes depuis les répertoires `drawable` Android. Lorsque vous exécutez `npx expo prebuild`, Expo génère la structure native du projet Android. Vos icônes doivent être présentes dans les dossiers `drawable` Android (placées manuellement ou copiées via un plugin de configuration) avant le processus de build. Le plugin configure ensuite le SDK Braze pour utiliser ces ressources drawable par leur nom (sans chemin ni extension), c'est pourquoi le préfixe `@drawable/` est requis dans votre configuration.

Pour plus d'informations sur les icônes de notification Android, consultez les [directives relatives aux icônes de notification Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### 2.3 Compiler et exécuter votre application {#23-build-and-run-your-application}

La précompilation de votre application génère les fichiers natifs nécessaires au fonctionnement du plugin Braze Expo.

L'extrait de code suivant montre la commande pour précompiler votre application :

```bash
npx expo prebuild
```

Exécutez votre application comme indiqué dans la [documentation Expo](https://docs.expo.dev/workflow/customizing/). Si vous modifiez les options de configuration, précompilez et exécutez à nouveau l'application.

#### Méthode 2 : Utiliser React Native CLI {#reactnative-using-react-native-cli}

##### Configuration Android {#set-up-android}

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
Vous pouvez toujours ajouter d'autres valeurs de configuration natives dans `braze.xml` (comme les paramètres de push, de session et de journalisation). Elles sont appliquées automatiquement lorsque `Braze.initialize()` est appelé depuis JavaScript.
{% endalert %}

L'extrait de code suivant montre les autorisations requises pour votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Avec la version 12.2.0 ou ultérieure du SDK Android de Braze, vous pouvez intégrer automatiquement la bibliothèque android-sdk-location en définissant `importBrazeLocationLibrary=true` dans votre fichier `gradle.properties`.
{% endalert %}

**2.3 Implémenter le suivi de session utilisateur**

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

**2.4 Gérer les mises à jour d'intention**

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

##### Configuration iOS {#set-up-ios}

**2.5 (Facultatif) Configurer le Podfile pour les XCFrameworks dynamiques**

Pour importer certaines bibliothèques Braze, telles que BrazeUI, dans un fichier Objective-C++, vous devez utiliser la syntaxe `#import`. À partir de la version `7.4.0` du SDK Braze Swift, les binaires disposent d'un [canal de distribution facultatif sous forme de XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), compatibles avec cette syntaxe.

Si vous souhaitez utiliser ce canal de distribution, remplacez manuellement les emplacements des sources CocoaPods dans votre Podfile. Référez-vous à l'exemple ci-dessous et remplacez `{your-version}` par la version souhaitée :

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Installer les pods**

Comme React Native lie automatiquement les bibliothèques à la plateforme native, vous pouvez installer le SDK à l'aide de CocoaPods.

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
- **Closure `postInitialization`** *(facultatif)* : reçoit l'instance `Braze` active après sa création, pour les configurations nécessitant l'instance (par exemple, stocker une référence ou définir des délégués).

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

Assurez-vous que votre version du SDK React Native de Braze est au minimum 1.37.0. Pour obtenir la liste complète des versions prises en charge, consultez le [dépôt Braze React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

L'extrait de code suivant montre la commande pour installer le plugin Braze Expo :

```bash
npx expo install @braze/expo-plugin
```

##### Étape 2.2 : Ajouter le plugin à votre app.json {#step-22-add-the-plugin-to-your-appjson}

Dans votre `app.json`, ajoutez le plugin Braze Expo. Vous pouvez fournir les options de configuration suivantes :

| Méthode                                       | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | chaîne de caractères  | Requis. La [clé API]({{site.baseurl}}/api/identifier_types/) de votre application Android, située dans votre tableau de bord de Braze sous **Gérer les paramètres**. |
| `iosApiKey`                                   | chaîne de caractères  | Requis. La [clé API]({{site.baseurl}}/api/identifier_types/) de votre application iOS, située dans votre tableau de bord de Braze sous **Gérer les paramètres**.     |
| `baseUrl`                                     | chaîne de caractères  | Requis. L'[endpoint SDK]({{site.baseurl}}/api/basics/#endpoints) de votre application, situé dans votre tableau de bord de Braze sous **Gérer les paramètres**.    |
| `enableBrazeIosPush`                          | booléen | iOS uniquement. Détermine si Braze gère les notifications push sur iOS. Introduit dans le SDK React Native v1.38.0 et le plugin Expo v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | booléen | Android uniquement. Détermine si Firebase Cloud Messaging est utilisé pour les notifications push. Introduit dans le SDK React Native v1.38.0 et le plugin Expo v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | chaîne de caractères  | Android uniquement. Votre ID expéditeur Firebase Cloud Messaging. Introduit dans le SDK React Native v1.38.0 et le plugin Expo v0.4.0.                                    |
| `sessionTimeout`                              | entier | Le délai d'expiration de session Braze pour votre application, en secondes.                                                                                               |
| `enableSdkAuthentication`                     | booléen | Détermine si la fonctionnalité [Authentification SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication) est activée.      |
| `logLevel`                                    | entier | Le niveau de journalisation pour votre application. Le niveau par défaut est 8 et enregistre un minimum d'informations. Pour activer la journalisation détaillée pour le débogage, utilisez le niveau 0.    |
| `minimumTriggerIntervalInSeconds`             | entier | L'intervalle minimum en secondes entre les déclenchements. 30 secondes par défaut.                                                                           |
| `enableAutomaticLocationCollection`           | booléen | Détermine si la collecte automatique de localisation est activée (si l'utilisateur l'autorise).                                                                                  |
| `enableGeofence`                              | booléen | Détermine si les géorepérages sont activés.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | booléen | Détermine si les demandes de géorepérage doivent être effectuées automatiquement.                                                                                                  |
| `dismissModalOnOutsideTap`                    | booléen | iOS uniquement. Détermine si un message in-app modal est fermé lorsque l'utilisateur clique en dehors du message.                                           |
| `androidHandlePushDeepLinksAutomatically`     | booléen | Android uniquement. Détermine si le SDK Braze doit gérer automatiquement les liens profonds des notifications push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | booléen | Android uniquement. Définit si le contenu textuel d'une notification push doit être interprété et rendu en HTML via `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | chaîne de caractères  | Android uniquement. Définit la couleur d'accentuation des notifications Android.                                                                                                |
| `androidNotificationLargeIcon`                | chaîne de caractères  | Android uniquement. Définit la grande icône des notifications Android.                                                                                                  |
| `androidNotificationSmallIcon`                | chaîne de caractères  | Android uniquement. Définit la petite icône des notifications Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | booléen | iOS uniquement. Détermine si l'utilisateur doit être automatiquement invité à autoriser les notifications push au lancement de l'application.                                                          |
| `enableBrazeIosRichPush`                      | booléen | iOS uniquement. Détermine si les fonctionnalités de push riche sont activées pour iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | booléen | iOS uniquement. Détermine si Braze Push Stories est activé pour iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | chaîne de caractères  | iOS uniquement. Le groupe d'applications utilisé pour iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | booléen | iOS uniquement. Détermine si l'ID de l'appareil utilise un UUID généré aléatoirement.                                                                                       |
| `iosForwardUniversalLinks`                    | booléen | iOS uniquement. Indique si le SDK doit automatiquement reconnaître et transmettre les liens universels aux méthodes système (par défaut : `false`). Lorsque cette option est activée, le SDK transmet automatiquement les liens universels aux méthodes système définies dans [Prise en charge des liens universels dans votre application](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introduit dans le SDK React Native v11.1.0 et le plugin Expo v3.2.0. |
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

###### Configuration des icônes de notification push Android {#configuring-android-push-notification-icons}

Lorsque vous utilisez `androidNotificationLargeIcon` et `androidNotificationSmallIcon`, suivez ces bonnes pratiques pour un affichage correct des icônes :

**Emplacement et format des icônes**

Pour utiliser des icônes de notification push personnalisées avec le plugin Braze Expo :

1. Créez vos fichiers d'icônes en respectant les exigences détaillées ci-dessous.
2. Placez-les dans les répertoires natifs Android de votre projet à l'emplacement `android/app/src/main/res/drawable-<density>/` (par exemple, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/`, ou similaire).
3. Sinon, si vous gérez vos ressources dans votre répertoire React Native, vous pouvez utiliser la [configuration des icônes app.json](https://docs.expo.dev/versions/latest/config/app/#icon) d'Expo ou créer un [plugin de configuration Expo](https://docs.expo.dev/config-plugins/introduction/) pour copier les icônes dans les dossiers drawable Android pendant la précompilation.

Le plugin Braze Expo fait référence à ces icônes via le système de ressources drawable d'Android.

**Exigences relatives aux icônes**

- **Petite icône :** doit être une silhouette blanche sur fond transparent (exigence de la plateforme Android).
- **Grande icône :** peut être une image en couleur.
- **Format :** le format PNG est recommandé.
- **Nommage :** utilisez uniquement des lettres minuscules, des chiffres et des traits de soulignement (par exemple, `my_large_icon.png`).

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
N'utilisez pas de chemins d'accès relatifs (tels que `src/assets/images/icon.png`) et n'incluez pas l'extension de fichier lorsque vous référencez des icônes. Le plugin Expo nécessite le préfixe `@drawable/` pour localiser correctement les icônes dans les dossiers natifs Android après le processus de précompilation.
{% endalert %}

**Fonctionnement**

Le plugin Braze Expo fait référence à vos fichiers d'icônes depuis les répertoires `drawable` Android. Lorsque vous exécutez `npx expo prebuild`, Expo génère la structure native du projet Android. Vos icônes doivent être présentes dans les dossiers `drawable` Android (placées manuellement ou copiées via un plugin de configuration) avant le processus de build. Le plugin configure ensuite le SDK Braze pour utiliser ces ressources drawable par leur nom (sans chemin ni extension), c'est pourquoi le préfixe `@drawable/` est requis dans votre configuration.

Pour plus d'informations sur les icônes de notification Android, consultez les [directives relatives aux icônes de notification Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### Étape 2.3 : Compiler et exécuter votre application {#step-23-build-and-run-your-application}

La précompilation de votre application génère les fichiers natifs nécessaires au fonctionnement du plugin Braze Expo.

L'extrait de code suivant montre la commande pour précompiler votre application :

```bash
npx expo prebuild
```

Exécutez votre application comme indiqué dans la [documentation Expo](https://docs.expo.dev/workflow/customizing/). Notez que si vous modifiez les options de configuration, vous devrez précompiler et exécuter à nouveau l'application.

#### Méthode 2 : Utiliser React Native CLI {#method-2-using-react-native-cli}

##### Configuration Android

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

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `res/values` de votre projet. L'extrait de code suivant montre un exemple de configuration `braze.xml`. Remplacez la [clé]({{site.baseurl}}/api/identifier_types/) API et l'[endpoint]({{site.baseurl}}/api/basics/#endpoints) par vos valeurs :

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
Avec la version 12.2.0 ou ultérieure du SDK Android de Braze, vous pouvez intégrer automatiquement la bibliothèque android-sdk-location en définissant `importBrazeLocationLibrary=true` dans votre fichier `gradle.properties`.
{% endalert %}

**Étape 2.3 : Implémenter le suivi de session utilisateur**

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

**Étape 2.4 : Gérer les mises à jour d'intention**

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

##### Configuration iOS

**Étape 2.5 : (Facultatif) Configurer le Podfile pour les XCFrameworks dynamiques**

Pour importer certaines bibliothèques Braze, telles que BrazeUI, dans un fichier Objective-C++, vous devez utiliser la syntaxe `#import`. À partir de la version `7.4.0` du SDK Braze Swift, les binaires disposent d'un [canal de distribution facultatif sous forme de XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), compatibles avec cette syntaxe.

Si vous souhaitez utiliser ce canal de distribution, remplacez manuellement les emplacements des sources CocoaPods dans votre Podfile. L'extrait de code suivant montre un exemple de remplacement. Remplacez `{your-version}` par la version souhaitée :

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**Étape 2.6 : Installer les pods**

Comme React Native lie automatiquement les bibliothèques à la plateforme native, vous pouvez installer le SDK à l'aide de CocoaPods.

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

Dans la méthode `application(_:didFinishLaunchingWithOptions:)`, remplacez la [clé]({{site.baseurl}}/api/identifier_types/) API et l'[endpoint]({{site.baseurl}}/api/basics/#endpoints) par les valeurs de votre application. Ensuite, créez l'instance Braze à l'aide de la configuration et créez une propriété statique sur `AppDelegate` pour un accès facile.

{% alert note %}
Notre exemple suppose une implémentation de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), qui fournit un certain nombre d'abstractions dans la configuration de React Native. Si vous utilisez une configuration différente pour votre application, ajustez votre implémentation en conséquence.
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

Dans la méthode `application:didFinishLaunchingWithOptions:`, remplacez la [clé]({{site.baseurl}}/api/identifier_types/) API et l'[endpoint]({{site.baseurl}}/api/basics/#endpoints) par les valeurs de votre application. Ensuite, créez l'instance Braze à l'aide de la configuration et créez une propriété statique sur `AppDelegate` pour un accès facile.

{% alert note %}
Notre exemple suppose une implémentation de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), qui fournit un certain nombre d'abstractions dans la configuration de React Native. Si vous utilisez une configuration différente pour votre application, ajustez votre implémentation en conséquence.
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

Appelez ensuite `Braze.initialize()` avec votre clé API d'identifiant d'application et l'endpoint SDK pour créer l'instance Braze. Consultez les options ci-dessous pour savoir où appeler cette méthode dans votre application.

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

L'extrait de code suivant montre comment reporter l'initialisation du SDK à plus tard dans la session. Par exemple, après que l'utilisateur a donné son consentement ou s'est connecté :

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
Sur iOS, les notifications push reçues avant `Braze.initialize()` sont mises en file d'attente et traitées après l'initialisation. Sur Android, les liens profonds des notifications push ne sont pas résolus tant que le SDK attend d'être initialisé. Si votre application nécessite une gestion immédiate des liens profonds au lancement, utilisez plutôt l'[initialisation standard](#standard-initialization).
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

{% endtab %}
{% tab React Native SDK 19.1.0 et antérieur %}

Pour le SDK React Native 19.1.0 et antérieur, l'initialisation native se fait à l'étape 2. Importez la bibliothèque dans votre code React Native pour appeler les méthodes Braze. Pour plus de détails, consultez notre [exemple de projet](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject).

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### Étape 4 : Tester l'intégration (facultatif) {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

Vous pouvez vérifier que le SDK est bien intégré en consultant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur l'une ou l'autre plateforme, vous devriez voir une nouvelle session apparaître dans le tableau de bord (dans la section **Overview**).

L'extrait de code suivant montre comment ouvrir une session pour un utilisateur particulier dans votre application :

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

Recherchez l'utilisateur avec `{some-user-id}` dans le tableau de bord sous **Audience** > **Search Users**. Vous pouvez y vérifier que les données de session et d'appareil ont bien été enregistrées.

{% endtab %}
{% tab React Native SDK 19.1.0 et antérieur %}

Pour tester l'intégration du SDK, l'extrait de code suivant montre comment démarrer une nouvelle session sur l'une ou l'autre plateforme pour un utilisateur.

```javascript
Braze.changeUser("userId");
```

L'extrait de code suivant montre un exemple d'attribution de l'ID utilisateur au démarrage de l'application :

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

Dans le tableau de bord de Braze, accédez à [Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search) et recherchez l'utilisateur dont l'ID correspond à `some-user-id`. Vous pouvez y vérifier que les données de session et d'appareil ont bien été enregistrées.

{% endtab %}
{% endtabs %}

## Étapes suivantes {#next-steps}

Après l'intégration du SDK Braze, vous pouvez commencer à mettre en œuvre les fonctionnalités d'envoi de messages courantes :

- [Notifications push]({{site.baseurl}}/developer_guide/push_notifications/) : configurez et envoyez des notifications push à vos utilisateurs.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/) : affichez des messages contextuels au sein de votre application.
- [Bannières]({{site.baseurl}}/developer_guide/banners/) : affichez des bannières continuelles dans l'interface de votre application.