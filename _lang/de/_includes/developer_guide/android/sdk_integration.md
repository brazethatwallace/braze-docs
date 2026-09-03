## Das Android SDK integrieren {#integrating-the-android-sdk}

### Schritt 1: Gradle-Build-Konfiguration aktualisieren {#step-1-update-your-gradle-build-configuration}

Fügen Sie im Repository-Konfigurationsbereich Ihres Projekts (z. B. `settings.gradle`, `settings.gradle.kts` oder der übergeordneten `build.gradle`) [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) zu Ihrer Liste der Repositories hinzu. Diese Syntax ist für Groovy und Kotlin DSL identisch.

```groovy
repositories {
  mavenCentral()
}
```

Fügen Sie anschließend Braze zu Ihren Abhängigkeiten hinzu. Ersetzen Sie in den folgenden Beispielen `SDK_VERSION` durch die aktuelle Version Ihres Android Braze SDK. Die vollständige Liste der Versionen finden Sie unter [Changelogs]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

{% alert note %}
- Für Kotlin DSL (`build.gradle.kts`) verwenden Sie die Syntax `implementation("...")`.
- Für Groovy (`build.gradle`) verwenden Sie die Syntax `implementation '...'`.
- Für [Version Catalogs](https://developer.android.com/build/migrate-to-catalogs) fügen Sie Einträge in Ihre `gradle/libs.versions.toml`-Datei ein und referenzieren Sie sie über die generierten Accessors.
{% endalert %}

{% tabs local %}
{% tab base only %}
Wenn Sie nicht vorhaben, Braze-UI-Komponenten zu verwenden, fügen Sie Folgendes zu Ihren Abhängigkeiten hinzu.

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
In Ihrer `gradle/libs.versions.toml`-Datei:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Fügen Sie anschließend in Ihrer `build.gradle`- oder `build.gradle.kts`-Datei die folgenden Abhängigkeiten hinzu. Diese Syntax ist für Groovy und Kotlin DSL identisch.

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
Wenn Sie vorhaben, Braze-UI-Komponenten zu verwenden, fügen Sie Folgendes zu Ihren Abhängigkeiten hinzu.

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
In Ihrer `gradle/libs.versions.toml`-Datei:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Fügen Sie anschließend in Ihrer `build.gradle`- oder `build.gradle.kts`-Datei die folgenden Abhängigkeiten hinzu. Diese Syntax ist für Groovy und Kotlin DSL identisch.

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

### Schritt 2: Ihre `braze.xml` konfigurieren {#step-2-configure-your-brazexml}

{% alert note %}
Seit Dezember 2019 werden keine angepassten Endpunkte mehr vergeben. Wenn Sie bereits über einen angepassten Endpunkt verfügen, können Sie diesen weiterhin verwenden. Weitere Details finden Sie in unserer <a href="{{site.baseurl}}/api/basics/#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

Erstellen Sie eine `braze.xml`-Datei im `res/values`-Ordner Ihres Projekts. Wenn Sie sich in einem bestimmten Daten-Cluster befinden oder bereits über einen angepassten Endpunkt verfügen, müssen Sie den Endpunkt ebenfalls in Ihrer `braze.xml`-Datei angeben.

Der Inhalt dieser Datei sollte dem folgenden Code-Snippet ähneln. Ersetzen Sie `YOUR_APP_IDENTIFIER_API_KEY` durch den Bezeichner, der auf der Seite **Einstellungen verwalten** im Braze-Dashboard zu finden ist. Melden Sie sich unter [dashboard.braze.com](https://dashboard.braze.com) an, um Ihre [Cluster-Adresse]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) zu ermitteln.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Schritt 3: Berechtigungen in `AndroidManifest.xml` hinzufügen {#step-3-add-permissions-to-androidmanifestxml}

Fügen Sie als Nächstes die folgenden Berechtigungen in Ihre `AndroidManifest.xml` ein:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Mit der Einführung von Android M hat Android vom Berechtigungsmodell bei der Installation auf ein Laufzeit-Berechtigungsmodell umgestellt. Beide oben genannten Berechtigungen sind jedoch normale Berechtigungen und werden automatisch gewährt, wenn sie im App-Manifest aufgeführt sind. Weitere Informationen finden Sie in der [Berechtigungsdokumentation](https://developer.android.com/training/permissions/index.html) von Android.
{% endalert %}

### Schritt 4: Verzögerte Initialisierung aktivieren (optional) {#step-4-enable-delayed-initialization-optional}

Für die verzögerte Initialisierung ist die folgende Mindestversion des Braze SDK erforderlich:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Während die verzögerte Initialisierung aktiviert ist, werden alle Netzwerkverbindungen abgebrochen, sodass das SDK keine Daten an die Braze-Server senden kann.
{% endalert %}

#### Schritt 4.1: Ihre `braze.xml` aktualisieren {#step-41-update-your-brazexml}

Die verzögerte Initialisierung ist standardmäßig deaktiviert. Verwenden Sie eine der folgenden Optionen, um sie zu aktivieren:

{% tabs %}
{% tab Braze XML file %}
Setzen Sie in der `braze.xml`-Datei Ihres Projekts `com_braze_enable_delayed_initialization` auf `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
Um die verzögerte Initialisierung zur Laufzeit zu aktivieren, verwenden Sie die folgende Methode.

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
Wenn die verzögerte Initialisierung aktiviert ist und eine Push-Benachrichtigung eine Deeplink-Aktion enthält, wird der Deeplink nicht aufgelöst.
{% endalert %}

#### Schritt 4.2: Push-Analytics konfigurieren (optional) {#step-42-configure-push-analytics-optional}

Wenn die verzögerte Initialisierung aktiviert ist, werden Push-Analytics standardmäßig in eine Warteschlange gestellt. Sie können sich jedoch dafür entscheiden, Push-Analytics [explizit in die Warteschlange zu stellen](#explicitly-queue-push-analytics) oder [zu verwerfen](#drop-push-analytics).

##### Explizit in die Warteschlange stellen {#explicitly-queue-push-analytics}

Um Push-Analytics explizit in die Warteschlange zu stellen, wählen Sie eine der folgenden Optionen:

{% tabs %}
{% tab Braze XML file %}
Setzen Sie in Ihrer `braze.xml`-Datei `com_braze_delayed_initialization_analytics_behavior` auf `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
Fügen Sie `QUEUE` zu Ihrer [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html)-Methode hinzu:

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

##### Verwerfen {#drop-push-analytics}

Um Push-Analytics zu verwerfen, wählen Sie eine der folgenden Optionen:

{% tabs %}
{% tab Braze XML file %}
Setzen Sie in Ihrer `braze.xml`-Datei `com_braze_delayed_initialization_analytics_behavior` auf `DROP`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
Fügen Sie `DROP` zur [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html)-Methode hinzu:

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

#### Schritt 4.3: Das SDK manuell initialisieren {#step-43-manually-initialize-the-sdk}

Verwenden Sie nach Ablauf der gewählten Verzögerungszeit die [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html)-Methode, um das SDK manuell zu initialisieren.

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

### Schritt 5: Tracking von Nutzer:innen-Sitzungen aktivieren {#step-5-enable-user-session-tracking}

Wenn Sie das Tracking von Nutzer:innen-Sitzungen aktivieren, können Aufrufe von `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) und die `InAppMessageManager`-Registrierung automatisch verarbeitet werden.

Um Activity-Lifecycle-Callbacks zu registrieren, fügen Sie den folgenden Code in die `onCreate()`-Methode Ihrer `Application`-Klasse ein.

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

Die Liste der verfügbaren Parameter finden Sie unter [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Sitzungs-Tracking testen {#testing-session-tracking}

{% alert tip %}
Sie können auch den [SDK-Debugger]({{site.baseurl}}/developer_guide/debugging) verwenden, um SDK-Probleme zu diagnostizieren.
{% endalert %}

Wenn beim Testen Probleme auftreten, aktivieren Sie die [ausführliche Protokollierung](#android_enabling-logs) und verwenden Sie dann Logcat, um fehlende `openSession`- und `closeSession`-Aufrufe in Ihren Activities zu erkennen.

1. Navigieren Sie in Braze zu **Übersicht**, wählen Sie Ihre App aus und wählen Sie dann im Dropdown **Daten anzeigen für** die Option **Heute**.
    ![Die Seite „Übersicht“ in Braze, mit dem Feld „Daten anzeigen für“ auf „Heute“ eingestellt.]({% image_buster /assets/img_archive/android_sessions.png %})
2. Öffnen Sie Ihre App und aktualisieren Sie dann das Braze-Dashboard. Überprüfen Sie, ob Ihre Metriken um 1 gestiegen sind.
3. Navigieren Sie durch Ihre App und überprüfen Sie, ob nur eine Sitzung in Braze protokolliert wurde.
4. Senden Sie die App für mindestens 10 Sekunden in den Hintergrund und bringen Sie sie dann wieder in den Vordergrund. Überprüfen Sie, ob eine neue Sitzung protokolliert wurde.

## Optionale Konfigurationen {#optional-configurations}

### Laufzeitkonfiguration {#runtime-configuration}

Um Ihre Braze-Optionen im Code statt in Ihrer `braze.xml`-Datei festzulegen, verwenden Sie die [Laufzeitkonfiguration](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Wenn ein Wert an beiden Stellen vorhanden ist, wird der Laufzeitwert verwendet. Nachdem alle erforderlichen Einstellungen zur Laufzeit bereitgestellt wurden, können Sie Ihre `braze.xml`-Datei löschen.

Im folgenden Beispiel wird ein [Builder-Objekt](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) erstellt und dann an [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) übergeben. Beachten Sie, dass nur einige der verfügbaren Laufzeitoptionen gezeigt werden&#8212;die vollständige Liste finden Sie in unserem [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html).

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
Sie suchen ein weiteres Beispiel? Sehen Sie sich unsere [Hello Braze Beispiel-App](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java) an.
{% endalert %}

### Google Advertising ID

Die [Google Advertising ID (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) ist eine optionale, nutzerspezifische, anonyme, eindeutige und zurücksetzbare ID für Werbung, die von den Google Play-Diensten bereitgestellt wird. Die GAID gibt Nutzer:innen die Möglichkeit, ihre Kennung zurückzusetzen, interessenbasierte Werbung in Google Play-Apps abzulehnen, und bietet Entwickler:innen ein einfaches, standardisiertes System, um ihre Apps weiterhin zu monetarisieren.

Die Google Advertising ID wird nicht automatisch vom Braze SDK erfasst und muss manuell über die Methode [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) festgelegt werden.

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
Google verlangt, dass die Advertising ID in einem Nicht-UI-Thread erfasst wird.
{% endalert %}


### Standort-Tracking {#location-tracking}

Um die Standorterfassung von Braze zu aktivieren, setzen Sie `com_braze_enable_location_collection` in Ihrer `braze.xml`-Datei auf `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Ab Braze Android SDK Version 3.6.0 ist die Standorterfassung von Braze standardmäßig deaktiviert.
{% endalert %}

### Protokollierung {#logging}

Standardmäßig ist die Protokollierungsstufe des Braze Android SDK auf `INFO` gesetzt. Sie können [diese Protokolle unterdrücken](#android_suppressing-logs) oder [eine andere Protokollierungsstufe festlegen](#android_enabling-logs), z. B. `VERBOSE`, `DEBUG` oder `WARN`.

#### Protokolle aktivieren {#enabling-logs}

Um bei der Fehlerbehebung in Ihrer App zu helfen oder die Bearbeitungszeiten beim Braze-Support zu verkürzen, können Sie ausführliche Protokolle für das SDK aktivieren. Wenn Sie ausführliche Protokolle an den Braze-Support senden, stellen Sie sicher, dass sie beginnen, sobald Sie Ihre Anwendung starten, und weit über das Auftreten Ihres Problems hinaus andauern. Einen zentralen Überblick finden Sie unter [Ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Um zu erfahren, wie Sie die Protokollausgabe interpretieren, lesen Sie [Ausführliche Protokolle lesen]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

Beachten Sie, dass ausführliche Protokolle nur für Ihre Entwicklungsumgebung vorgesehen sind, daher sollten Sie sie vor der Veröffentlichung Ihrer App deaktivieren.

{% alert important %}
Aktivieren Sie ausführliche Protokolle vor allen anderen Aufrufen in `Application.onCreate()`, um sicherzustellen, dass Ihre Protokolle so vollständig wie möglich sind.
{% endalert %}

{% tabs local %}
{% tab Application %}
Um Protokolle direkt in Ihrer App zu aktivieren, fügen Sie Folgendes vor allen anderen Methoden zur `onCreate()`-Methode Ihrer Anwendung hinzu.

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

Ersetzen Sie `MIN_LOG_LEVEL` durch die **Konstante** der Protokollierungsstufe, die Sie als Mindestprotokollierungsstufe festlegen möchten. Alle Protokolle auf einer Stufe `>=` Ihrer eingestellten `MIN_LOG_LEVEL` werden an die Standard-[`Log`](https://developer.android.com/reference/android/util/Log)-Methode von Android weitergeleitet. Alle Protokolle `<` Ihrer eingestellten `MIN_LOG_LEVEL` werden verworfen.

| Konstante   | Wert           | Beschreibung                                                              |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Protokolliert die detailliertesten Nachrichten für Debugging und Entwicklung. |
| `DEBUG`     | 3              | Protokolliert beschreibende Nachrichten für Debugging und Entwicklung.    |
| `INFO`      | 4              | Protokolliert informative Nachrichten für allgemeine Hinweise.            |
| `WARN`      | 5              | Protokolliert Warnmeldungen zur Identifikation potenziell schädlicher Situationen. |
| `ERROR`     | 6              | Protokolliert Fehlermeldungen bei Anwendungsfehlern oder schwerwiegenden Problemen. |
| `ASSERT`    | 7              | Protokolliert Assertion-Nachrichten, wenn Bedingungen bei der Entwicklung falsch sind. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Protokolle aktivieren" }

Der folgende Code leitet beispielsweise die Protokollierungsstufen `2`, `3`, `4`, `5`, `6` und `7` an die `Log`-Methode weiter.

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
Um Protokolle in der `braze.xml` zu aktivieren, fügen Sie Folgendes zu Ihrer Datei hinzu:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Ersetzen Sie `MIN_LOG_LEVEL` durch den **Wert** der Protokollierungsstufe, die Sie als Mindestprotokollierungsstufe festlegen möchten. Alle Protokolle auf einer Stufe `>=` Ihrer eingestellten `MIN_LOG_LEVEL` werden an die Standard-[`Log`](https://developer.android.com/reference/android/util/Log)-Methode von Android weitergeleitet. Alle Protokolle `<` Ihrer eingestellten `MIN_LOG_LEVEL` werden verworfen.

| Konstante   | Wert           | Beschreibung                                                              |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Protokolliert die detailliertesten Nachrichten für Debugging und Entwicklung. |
| `DEBUG`     | 3              | Protokolliert beschreibende Nachrichten für Debugging und Entwicklung.    |
| `INFO`      | 4              | Protokolliert informative Nachrichten für allgemeine Hinweise.            |
| `WARN`      | 5              | Protokolliert Warnmeldungen zur Identifikation potenziell schädlicher Situationen. |
| `ERROR`     | 6              | Protokolliert Fehlermeldungen bei Anwendungsfehlern oder schwerwiegenden Problemen. |
| `ASSERT`    | 7              | Protokolliert Assertion-Nachrichten, wenn Bedingungen bei der Entwicklung falsch sind. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Protokolle aktivieren" }

Der folgende Code leitet beispielsweise die Protokollierungsstufen `2`, `3`, `4`, `5`, `6` und `7` an die `Log`-Methode weiter.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Ausführliche Protokolle überprüfen {#verifying-verbose-logs}

Um zu überprüfen, ob Ihre Protokolle auf `VERBOSE` gesetzt sind, prüfen Sie, ob `V/Braze` irgendwo in Ihren Protokollen vorkommt. Wenn dies der Fall ist, wurden ausführliche Protokolle erfolgreich aktiviert. Beispiel:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Protokolle unterdrücken {#suppressing-logs}

Um alle Protokolle für das Braze Android SDK zu unterdrücken, setzen Sie die Protokollierungsstufe in der `onCreate()`-Methode Ihrer Anwendung _vor_ allen anderen Methoden auf `BrazeLogger.SUPPRESS`.

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

### Mehrere API-Schlüssel {#multiple-api-keys}

Der häufigste Anwendungsfall für mehrere API-Schlüssel ist die Trennung von API-Schlüsseln für Debug- und Release-Build-Varianten.

Um in Ihren Builds einfach zwischen mehreren API-Schlüsseln zu wechseln, empfehlen wir, für jede relevante [Build-Variante](https://developer.android.com/studio/build/build-variants.html) eine separate `braze.xml`-Datei zu erstellen. Eine Build-Variante ist eine Kombination aus Build-Typ und Product Flavor. Standardmäßig werden neue Android-Projekte mit den [`debug`- und `release`-Build-Typen](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) und ohne Product Flavors konfiguriert.

Erstellen Sie für jede relevante Build-Variante eine neue `braze.xml` im Verzeichnis `src/<build variant name>/res/values/`. Wenn die Build-Variante kompiliert wird, verwendet sie den neuen API-Schlüssel.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Um zu erfahren, wie Sie den API-Schlüssel in Ihrem Code festlegen, lesen Sie [Laufzeitkonfiguration]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#runtime-configuration).
{% endalert %}

### Exklusiver TalkBack-Modus für In-App-Nachrichten {#exclusive-in-app-message-talkback}

In Übereinstimmung mit den [Android-Barrierefreiheitsrichtlinien](https://developer.android.com/guide/topics/ui/accessibility) bietet das Braze Android SDK standardmäßig Android TalkBack an. Um sicherzustellen, dass nur der Inhalt von In-App-Nachrichten vorgelesen wird – ohne andere Bildschirmelemente wie die Titelleiste der App oder die Navigation einzubeziehen – können Sie den exklusiven Modus für TalkBack aktivieren.

So aktivieren Sie den exklusiven Modus für In-App-Nachrichten:

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

### R8 und ProGuard {#r8-and-proguard}

Die Konfiguration für [Code-Shrinking](https://developer.android.com/build/shrink-code) ist automatisch in Ihrer Braze-Integration enthalten.

Client-Apps, die Braze-Code verschleiern, müssen Release-Mapping-Dateien speichern, damit Braze Stack-Traces interpretieren kann. Wenn Sie den gesamten Braze-Code beibehalten möchten, fügen Sie Folgendes zu Ihrer ProGuard-Datei hinzu:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
