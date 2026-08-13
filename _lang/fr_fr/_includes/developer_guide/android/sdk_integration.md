## Intégration du SDK Android {#integrating-the-android-sdk}

### Étape 1 : Mettre à jour votre configuration de compilation Gradle {#step-1-update-your-gradle-build-configuration}

Dans la configuration du dépôt de votre projet (par exemple, `settings.gradle`, `settings.gradle.kts` ou le fichier `build.gradle` de niveau supérieur), ajoutez [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) à votre liste de dépôts. Cette syntaxe est identique pour Groovy et Kotlin DSL.

```groovy
repositories {
  mavenCentral()
}
```

Ensuite, ajoutez Braze à vos dépendances. Dans les exemples suivants, remplacez `SDK_VERSION` par la version actuelle de votre SDK Android Braze. Pour obtenir la liste complète des versions, consultez les [journaux des modifications]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

{% alert note %}
- Pour Kotlin DSL (`build.gradle.kts`), utilisez la syntaxe `implementation("...")`.
- Pour Groovy (`build.gradle`), utilisez la syntaxe `implementation '...'`.
- Pour les [catalogues de versions](https://developer.android.com/build/migrate-to-catalogs), ajoutez des entrées à votre fichier `gradle/libs.versions.toml` et référencez-les à l'aide des accesseurs générés.
{% endalert %}

{% tabs local %}
{% tab base only %}
Si vous ne prévoyez pas d'utiliser les composants d'interface Braze, ajoutez les éléments suivants à vos dépendances.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-base:SDK_VERSION") // (Required) Adds dependencies for the base Braze SDK.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
Dans votre fichier `gradle/libs.versions.toml` :

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Ensuite, dans votre fichier `build.gradle` ou `build.gradle.kts`, ajoutez les dépendances suivantes. Cette syntaxe est identique pour Groovy et Kotlin DSL.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.base) // (Required) Adds dependencies for the base Braze SDK.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab with ui components %}
Si vous prévoyez d'utiliser les composants d'interface Braze, ajoutez les éléments suivants à vos dépendances.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-ui:SDK_VERSION") // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
Dans votre fichier `gradle/libs.versions.toml` :

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Ensuite, dans votre fichier `build.gradle` ou `build.gradle.kts`, ajoutez les dépendances suivantes. Cette syntaxe est identique pour Groovy et Kotlin DSL.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.ui) // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 2 : Configurer votre `braze.xml` {#step-2-configure-your-brazexml}

{% alert note %}
À partir de décembre 2019, les endpoints personnalisés ne sont plus fournis. Si vous disposez d'un endpoint personnalisé préexistant, vous pouvez continuer à l'utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste d'endpoints disponibles</a>.
{% endalert %}

Créez un fichier `braze.xml` dans le dossier `res/values` de votre projet. Si vous êtes sur un cluster de données spécifique ou disposez d'un endpoint personnalisé préexistant, vous devez également spécifier l'endpoint dans votre fichier `braze.xml`.

Le contenu de ce fichier devrait ressembler à l'extrait de code suivant. Veillez à remplacer `YOUR_APP_IDENTIFIER_API_KEY` par l'identifiant figurant dans la page **Gérer les paramètres** du tableau de bord de Braze. Connectez-vous à [dashboard.braze.com](https://dashboard.braze.com) pour trouver [l'adresse de votre cluster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints).

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Étape 3 : Ajouter des autorisations à `AndroidManifest.xml` {#step-3-add-permissions-to-androidmanifestxml}

Ensuite, ajoutez les autorisations suivantes à votre `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Avec la sortie d'Android M, Android est passé d'un modèle d'autorisations à l'installation à un modèle d'autorisations à l'exécution. Cependant, ces deux autorisations sont des autorisations normales et sont accordées automatiquement si elles sont répertoriées dans le manifeste de l'application. Pour plus d'informations, consultez la [documentation sur les autorisations](https://developer.android.com/training/permissions/index.html) d'Android.
{% endalert %}

### Étape 4 : Activer l'initialisation différée (facultatif) {#step-4-enable-delayed-initialization-optional}

Pour utiliser l'initialisation différée, la version minimale requise du SDK Braze est la suivante :

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Lorsque l'initialisation différée est activée, toutes les connexions réseau sont annulées, empêchant le SDK d'envoyer des données aux serveurs Braze.
{% endalert %}

#### Étape 4.1 : Mettre à jour votre `braze.xml` {#step-41-update-your-brazexml}

L'initialisation différée est désactivée par défaut. Pour l'activer, utilisez l'une des options suivantes :

{% tabs %}
{% tab Braze XML file %}
Dans le fichier `braze.xml` de votre projet, définissez `com_braze_enable_delayed_initialization` sur `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
Pour activer l'initialisation différée à l'exécution, utilisez la méthode suivante.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert note %}
Lorsque l'initialisation différée est activée et qu'une notification push contient une action de deep link, le deep link ne se résout pas.
{% endalert %}

#### Étape 4.2 : Configurer les analyses push (facultatif) {#step-42-configure-push-analytics-optional}

Lorsque l'initialisation différée est activée, les analyses push sont mises en file d'attente par défaut. Cependant, vous pouvez choisir de [mettre explicitement en file d'attente](#explicitly-queue-push-analytics) ou de [supprimer](#drop-push-analytics) les analyses push.

##### Mettre explicitement en file d'attente {#explicitly-queue-push-analytics}

Pour mettre explicitement en file d'attente les analyses push, choisissez l'une des options suivantes :

{% tabs %}
{% tab Braze XML file %}
Dans votre fichier `braze.xml`, définissez `com_braze_delayed_initialization_analytics_behavior` sur `QUEUE` :

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
Ajoutez `QUEUE` à votre méthode [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) :

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Supprimer {#drop-push-analytics}

Pour supprimer les analyses push, choisissez l'une des options suivantes :

{% tabs %}
{% tab Braze XML file %}
Dans votre fichier `braze.xml`, définissez `com_braze_delayed_initialization_analytics_behavior` sur `DROP` :

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
Ajoutez `DROP` à la méthode [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) :

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Étape 4.3 : Initialiser manuellement le SDK {#step-43-manually-initialize-the-sdk}

Une fois le délai souhaité écoulé, utilisez la méthode [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) pour initialiser manuellement le SDK.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### Étape 5 : Activer le suivi des sessions utilisateur {#step-5-enable-user-session-tracking}

Lorsque vous activez le suivi des sessions utilisateur, les appels à `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) et l'enregistrement de `InAppMessageManager` peuvent être gérés automatiquement.

Pour enregistrer les rappels du cycle de vie de l'activité, ajoutez le code suivant à la méthode `onCreate()` de votre classe `Application`.

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

Pour obtenir la liste des paramètres disponibles, consultez [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Tester le suivi de session {#testing-session-tracking}

{% alert tip %}
Vous pouvez également utiliser l'[outil de débogage du SDK]({{site.baseurl}}/developer_guide/debugging) pour diagnostiquer les problèmes liés au SDK.
{% endalert %}

Si vous rencontrez des problèmes lors des tests, activez la [journalisation détaillée](#android_enabling-logs), puis utilisez logcat pour détecter les appels `openSession` et `closeSession` manquants dans vos activités.

1. Dans Braze, accédez à **Overview**, sélectionnez votre application, puis choisissez **Today** dans le menu déroulant **Display Data For**.
    ![La page « Overview » dans Braze, avec le champ « Display Data For » réglé sur « Today ».]({% image_buster /assets/img_archive/android_sessions.png %})
2. Ouvrez votre application, puis actualisez le tableau de bord de Braze. Vérifiez que vos indicateurs ont augmenté de 1.
3. Naviguez dans votre application et vérifiez qu'une seule session a été enregistrée dans Braze.
4. Mettez l'application en arrière-plan pendant au moins 10 secondes, puis ramenez-la au premier plan. Vérifiez qu'une nouvelle session a été enregistrée.

## Configurations optionnelles {#optional-configurations}

### Configuration à l'exécution {#runtime-configuration}

Pour définir vos options Braze dans le code plutôt que dans votre fichier `braze.xml`, utilisez la [configuration à l'exécution](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Si une valeur existe aux deux endroits, la valeur définie à l'exécution sera utilisée à la place. Une fois tous les paramètres requis fournis à l'exécution, vous pouvez supprimer votre fichier `braze.xml`.

Dans l'exemple suivant, un [objet builder](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) est créé puis transmis à [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Notez que seules certaines des options d'exécution disponibles sont affichées&#8212;consultez notre [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) pour obtenir la liste complète.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Vous cherchez un autre exemple ? Consultez notre [application exemple Hello Braze](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).
{% endalert %}

### Identifiant publicitaire Google {#google-advertising-id}

L'[identifiant publicitaire Google (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) est un identifiant facultatif, spécifique à l'utilisateur, anonyme, unique et réinitialisable, destiné à la publicité et fourni par les services Google Play. Le GAID permet aux utilisateurs de réinitialiser leur identifiant, de désactiver les publicités ciblées par centres d'intérêt dans les applications Google Play et offre aux développeurs un système simple et standard pour continuer à monétiser leurs applications.

L'identifiant publicitaire Google n'est pas automatiquement collecté par le SDK Braze et doit être défini manuellement via la méthode [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google exige que l'identifiant publicitaire soit collecté sur un thread non-UI.
{% endalert %}


### Suivi de la localisation {#location-tracking}

Pour activer la collecte de localisation Braze, définissez `com_braze_enable_location_collection` sur `true` dans votre fichier `braze.xml` :

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
À partir de la version 3.6.0 du SDK Android Braze, la collecte de localisation Braze est désactivée par défaut.
{% endalert %}

### Journalisation {#logging}

Par défaut, le niveau de journalisation du SDK Android Braze est défini sur `INFO`. Vous pouvez [supprimer ces journaux](#android_suppressing-logs) ou [définir un niveau de journalisation différent](#android_enabling-logs), tel que `VERBOSE`, `DEBUG` ou `WARN`.

#### Activer les journaux {#android_enabling-logs}

Pour faciliter la résolution des problèmes dans votre application ou réduire les délais de traitement avec l'assistance Braze, vous pouvez activer les journaux détaillés pour le SDK. Lorsque vous envoyez des journaux détaillés à l'assistance Braze, assurez-vous qu'ils commencent dès le lancement de votre application et se terminent bien après l'apparition de votre problème. Pour un aperçu centralisé, consultez la [journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Pour apprendre à interpréter la sortie des journaux, consultez la [lecture des journaux détaillés]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

Gardez à l'esprit que les journaux détaillés ne sont destinés qu'à votre environnement de développement et que vous devez les désactiver avant de publier votre application.

{% alert important %}
Activez les journaux détaillés avant tout autre appel dans `Application.onCreate()` pour vous assurer que vos journaux sont aussi complets que possible.
{% endalert %}

{% tabs local %}
{% tab Application %}
Pour activer les journaux directement dans votre application, ajoutez ce qui suit à la méthode `onCreate()` de votre application avant toute autre méthode.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Remplacez `MIN_LOG_LEVEL` par la **constante** du niveau de journalisation que vous souhaitez définir comme niveau minimum. Tous les journaux d'un niveau `>=` au `MIN_LOG_LEVEL` défini seront transmis à la méthode [`Log`](https://developer.android.com/reference/android/util/Log) par défaut d'Android. Tous les journaux d'un niveau `<` au `MIN_LOG_LEVEL` défini seront ignorés.

| Constante   | Valeur         | Description                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Enregistre les messages les plus détaillés pour le débogage et le développement.            |
| `DEBUG`     | 3              | Enregistre des messages descriptifs pour le débogage et le développement.                  |
| `INFO`      | 4              | Enregistre des messages d'information pour les faits marquants.                       |
| `WARN`      | 5              | Enregistre des messages d'avertissement pour identifier les situations potentiellement dangereuses.     |
| `ERROR`     | 6              | Enregistre des messages d'erreur pour indiquer les échecs de l'application ou les problèmes graves. |
| `ASSERT`    | 7              | Enregistre des messages d'assertion lorsque les conditions sont fausses pendant le développement.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Activation des journaux" }

Par exemple, le code suivant transmettra les niveaux de journalisation `2`, `3`, `4`, `5`, `6` et `7` à la méthode `Log`.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
Pour activer les journaux dans le fichier `braze.xml`, ajoutez ce qui suit à votre fichier :

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Remplacez `MIN_LOG_LEVEL` par la **valeur** du niveau de journalisation que vous souhaitez définir comme niveau minimum. Tous les journaux d'un niveau `>=` au `MIN_LOG_LEVEL` défini seront transmis à la méthode [`Log`](https://developer.android.com/reference/android/util/Log) par défaut d'Android. Tous les journaux d'un niveau `<` au `MIN_LOG_LEVEL` défini seront ignorés.

| Constante   | Valeur         | Description                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Enregistre les messages les plus détaillés pour le débogage et le développement.            |
| `DEBUG`     | 3              | Enregistre des messages descriptifs pour le débogage et le développement.                  |
| `INFO`      | 4              | Enregistre des messages d'information pour les faits marquants.                       |
| `WARN`      | 5              | Enregistre des messages d'avertissement pour identifier les situations potentiellement dangereuses.     |
| `ERROR`     | 6              | Enregistre des messages d'erreur pour indiquer les échecs de l'application ou les problèmes graves. |
| `ASSERT`    | 7              | Enregistre des messages d'assertion lorsque les conditions sont fausses pendant le développement.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Activation des journaux" }

Par exemple, le code suivant transmettra les niveaux de journalisation `2`, `3`, `4`, `5`, `6` et `7` à la méthode `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Vérifier les journaux détaillés {#verifying-verbose-logs}

Pour vérifier que vos journaux sont définis sur `VERBOSE`, vérifiez si `V/Braze` apparaît quelque part dans vos journaux. Si c'est le cas, les journaux détaillés ont été activés avec succès. Par exemple :

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Supprimer les journaux {#android_suppressing-logs}

Pour supprimer tous les journaux du SDK Android Braze, définissez le niveau de journalisation sur `BrazeLogger.SUPPRESS` dans la méthode `onCreate()` de votre application _avant_ toute autre méthode.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### Clés API multiples {#multiple-api-keys}

Le cas d'usage le plus courant pour les clés API multiples est la séparation des clés API entre les variantes de compilation de débogage et de production.

Pour basculer facilement entre plusieurs clés API dans vos compilations, nous vous recommandons de créer un fichier `braze.xml` distinct pour chaque [variante de compilation](https://developer.android.com/studio/build/build-variants.html) pertinente. Une variante de compilation est une combinaison du type de compilation et de la variété du produit. Par défaut, les nouveaux projets Android sont configurés avec les [types de compilation `debug` et `release`](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) et aucune variété de produit.

Pour chaque variante de compilation pertinente, créez un nouveau fichier `braze.xml` dans le répertoire `src/<build variant name>/res/values/`. Lorsque la variante de compilation est compilée, elle utilisera la nouvelle clé API.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Pour savoir comment configurer la clé API dans votre code, consultez la [configuration à l'exécution]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#runtime-configuration).
{% endalert %}

### TalkBack exclusif pour les messages in-app {#exclusive-in-app-message-talkback}

Conformément aux [directives d'accessibilité Android](https://developer.android.com/guide/topics/ui/accessibility), le SDK Android Braze propose Android TalkBack par défaut. Pour garantir que seul le contenu des messages in-app soit lu à voix haute, sans inclure d'autres éléments de l'écran tels que la barre de titre de l'application ou la navigation, vous pouvez activer le mode exclusif pour TalkBack.

Pour activer le mode exclusif pour les messages in-app :

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 et ProGuard {#r8-and-proguard}

La configuration de la [réduction du code](https://developer.android.com/build/shrink-code) est automatiquement incluse dans votre intégration Braze.

Les applications clientes qui obfusquent le code Braze doivent stocker les fichiers de mappage de version pour que Braze puisse interpréter les traces de pile. Si vous souhaitez conserver l'intégralité du code Braze, ajoutez ce qui suit à votre fichier ProGuard :

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
