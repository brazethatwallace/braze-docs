## Integration des Android SDK {#integrating-the-android-sdk}

### 1. Schritt: Aktualisieren Sie Ihre Gradle-Build-Konfiguration {#step-1-update-your-gradle-build-configuration}

Fügen Sie in der Repository-Konfiguration Ihres Projekts (z. B. `settings.gradle`, `settings.gradle.kts` oder `build.gradle` auf oberster Ebene) [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) zu Ihrer Liste der Repositorys hinzu. Diese Syntax ist sowohl für Groovy als auch für Kotlin DSL identisch.

```groovy
repositories {
  mavenCentral()
}
```

Fügen Sie als Nächstes Braze zu Ihren Abhängigkeiten hinzu. Ersetzen Sie in den folgenden Beispielen `SDK_VERSION` durch die aktuelle Version Ihres Android Braze SDK. Die vollständige Liste der Versionen finden Sie unter [Changelogs]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

{% alert note %}
- Für Kotlin DSL (`build.gradle.kts`) verwenden Sie die Syntax `implementation("...")`.
- Für Groovy (`build.gradle`) verwenden Sie die Syntax `implementation '...'`.
- Für [Versionskataloge](https://developer.android.com/build/migrate-to-catalogs) fügen Sie Einträge zu Ihrer Datei `gradle/libs.versions.toml` hinzu und referenzieren Sie diese mithilfe der generierten Zugriffsmethoden.
{% endalert %}

{% tabs local %}
{% tab base only %}
Falls Sie nicht vorhaben, Braze-UI-Komponenten zu verwenden, fügen Sie Folgendes zu Ihren Abhängigkeiten hinzu.

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
In Ihrer Datei `gradle/libs.versions.toml`:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Fügen Sie anschließend in Ihrer Datei `build.gradle` oder `build.gradle.kts` die folgenden Abhängigkeiten hinzu. Diese Syntax ist sowohl für Groovy als auch für Kotlin DSL identisch.

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
Wenn Sie die Verwendung von Braze-UI-Komponenten planen, fügen Sie Folgendes zu Ihren Abhängigkeiten hinzu.

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
In Ihrer Datei `gradle/libs.versions.toml`:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Fügen Sie anschließend in Ihrer Datei `build.gradle` oder `build.gradle.kts` die folgenden Abhängigkeiten hinzu. Diese Syntax ist sowohl für Groovy als auch für Kotlin DSL identisch.

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

### 2. Schritt: Konfigurieren Sie Ihre `braze.xml` {#step-2-configure-your-brazexml}

{% alert note %}
Ab Dezember 2019 werden keine benutzerdefinierten Endpunkte mehr vergeben. Wenn Sie einen bereits bestehenden benutzerdefinierten Endpunkt haben, können Sie diesen weiterhin verwenden. Weitere Einzelheiten finden Sie in unserer <a href="{{site.baseurl}}/api/basics/#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

Erstellen Sie eine Datei `braze.xml` im Ordner `res/values` Ihres Projekts. Wenn Sie mit einem bestimmten Daten-Cluster arbeiten oder einen zuvor angepassten Endpunkt verwenden, müssen Sie den Endpunkt ebenfalls in Ihrer Datei `braze.xml` angeben.

Der Inhalt dieser Datei sollte dem folgenden Code-Snippet ähneln. Stellen Sie sicher, dass Sie `YOUR_APP_IDENTIFIER_API_KEY` durch den Bezeichner ersetzen, den Sie auf der Seite **Einstellungen verwalten** des Braze-Dashboards finden. Melden Sie sich unter [dashboard.braze.com](https://dashboard.braze.com) an, um Ihre [Cluster-Adresse]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) zu finden.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### 3. Schritt: Berechtigungen zu `AndroidManifest.xml` hinzufügen {#step-3-add-permissions-to-androidmanifestxml}

Fügen Sie als Nächstes die folgenden Berechtigungen zu Ihrer `AndroidManifest.xml` hinzu:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Mit der Veröffentlichung von Android M wechselte Android von einem Installationszeit- zu einem Laufzeit-Berechtigungsmodell. Diese beiden Berechtigungen sind jedoch normale Berechtigungen und werden automatisch gewährt, wenn sie im App-Manifest aufgeführt sind. Weitere Informationen finden Sie in der [Dokumentation zu den Berechtigungen](https://developer.android.com/training/permissions/index.html) von Android.
{% endalert %}

### 4. Schritt: Verzögerte Initialisierung aktivieren (optional) {#step-4-enable-delayed-initialization-optional}

Um die verzögerte Initialisierung zu verwenden, ist die folgende Mindestversion des Braze SDK erforderlich:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Solange die verzögerte Initialisierung aktiviert ist, werden alle Netzwerkverbindungen unterbrochen, wodurch verhindert wird, dass das SDK Daten an die Braze-Server sendet.
{% endalert %}

#### Schritt 4.1: Aktualisieren Sie Ihre `braze.xml` {#step-41-update-your-brazexml}

Die verzögerte Initialisierung ist standardmäßig deaktiviert. Um sie zu aktivieren, verwenden Sie eine der folgenden Optionen:

{% tabs %}
{% tab Braze XML file %}
Setzen Sie in der Datei `braze.xml` Ihres Projekts `com_braze_enable_delayed_initialization` auf `true`.

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

Wenn die verzögerte Initialisierung aktiviert ist, werden Push-Analytics standardmäßig in eine Warteschlange gestellt. Sie können jedoch auch [explizit in die Warteschlange stellen](#explicitly-queue-push-analytics) oder Push-Analytics [verwerfen](#drop-push-analytics).

##### Explizit in die Warteschlange stellen {#explicitly-queue-push-analytics}

Um Push-Analytics explizit in die Warteschlange zu stellen, wählen Sie eine der folgenden Optionen:

{% tabs %}
{% tab Braze XML file %}
Setzen Sie in Ihrer Datei `braze.xml` den Wert `com_braze_delayed_initialization_analytics_behavior` auf `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
Fügen Sie `QUEUE` zu Ihrer Methode [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) hinzu:

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
Setzen Sie in Ihrer Datei `braze.xml` den Wert `com_braze_delayed_initialization_analytics_behavior` auf `DROP`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
Fügen Sie `DROP` zur Methode [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) hinzu:

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

#### Schritt 4.3: SDK manuell initialisieren {#step-43-manually-initialize-the-sdk}

Nach Ablauf der von Ihnen gewählten Verzögerungszeit verwenden Sie die Methode [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html), um das SDK manuell zu initialisieren.

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

### 5. Schritt: Tracking von Nutzer:innen-Sitzungen aktivieren {#step-5-enable-user-session-tracking}

Wenn Sie das Tracking von Nutzer:innen-Sitzungen aktivieren, können Aufrufe von `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) und die `InAppMessageManager`-Registrierung automatisch verarbeitet werden.

Um Callbacks für den Lebenszyklus einer Aktivität zu registrieren, fügen Sie den folgenden Code in die Methode `onCreate()` Ihrer Klasse `Application` ein.

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

## Testen des Sitzungs-Trackings {#testing-session-tracking}

{% alert tip %}
Sie können auch den [SDK-Debugger]({{site.baseurl}}/developer_guide/debugging/) verwenden, um Probleme mit dem SDK zu diagnostizieren.
{% endalert %}

Wenn Sie beim Testen auf Probleme stoßen, aktivieren Sie die [ausführliche Protokollierung](#android_enabling-logs) und verwenden Sie dann logcat, um fehlende `openSession`- und `closeSession`-Aufrufe in Ihren Aktivitäten zu erkennen.

1. Gehen Sie in Braze zu **Übersicht**, wählen Sie Ihre App aus und wählen Sie dann in der Dropdown-Liste **Daten anzeigen für** die Option **Heute**.
    ![Die Seite „Übersicht“ in Braze, wobei das Feld „Daten anzeigen für“ auf „Heute“ eingestellt ist.]({% image_buster /assets/img_archive/android_sessions.png %})
2. Öffnen Sie Ihre App und aktualisieren Sie dann das Braze-Dashboard. Überprüfen Sie, ob sich Ihre Metriken um 1 erhöht haben.
3. Navigieren Sie durch Ihre App und überprüfen Sie, ob nur eine Sitzung bei Braze protokolliert wurde.
4. Versetzen Sie die App für mindestens 10 Sekunden in den Hintergrund und holen Sie sie dann in den Vordergrund. Überprüfen Sie, ob eine neue Sitzung protokolliert wurde.

## Optionale Konfigurationen {#optional-configurations}

### Laufzeitkonfiguration {#runtime-configuration}

Um Ihre Braze-Optionen im Code statt in Ihrer Datei `braze.xml` festzulegen, verwenden Sie die [Laufzeitkonfiguration](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Wenn ein Wert an beiden Stellen vorhanden ist, wird stattdessen der Laufzeitwert verwendet. Nachdem alle erforderlichen Einstellungen zur Laufzeit vorgenommen wurden, können Sie Ihre Datei `braze.xml` löschen.

Im folgenden Beispiel wird ein [Builder-Objekt](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) erstellt und anschließend an [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) übergeben. Beachten Sie, dass nur einige der verfügbaren Laufzeitoptionen angezeigt werden&#8212;die vollständige Liste finden Sie in unserer [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html).

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
Suchen Sie ein weiteres Beispiel? Sehen Sie sich unsere [Hello Braze-Beispiel-App](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java) an.
{% endalert %}

### Google Advertising ID

Die [Google Advertising ID (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) ist eine optionale nutzerspezifische, anonyme, eindeutige und zurücksetzbare ID für Werbung, die von Google Play-Diensten bereitgestellt wird. GAID gibt Nutzer:innen die Möglichkeit, ihren Bezeichner zurückzusetzen, interessenbezogene Werbung in Google Play-Apps abzulehnen, und bietet Entwickler:innen ein einfaches, standardisiertes System, um ihre Apps weiterhin zu monetarisieren.

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
Google verlangt, dass die Advertising ID auf einem Nicht-UI-Thread erfasst wird.
{% endalert %}


### Standort-Tracking {#location-tracking}

Um die Erfassung von Braze-Standortdaten zu aktivieren, setzen Sie `com_braze_enable_location_collection` in Ihrer Datei `braze.xml` auf `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Ab Version 3.6.0 des Braze Android SDK ist die Braze-Standorterfassung standardmäßig deaktiviert.
{% endalert %}

### Protokollierung {#logging}

Standardmäßig ist die Protokollstufe des Braze Android SDK auf `INFO` eingestellt. Sie können [diese Protokolle unterdrücken](#android_suppressing-logs) oder [eine andere Protokollstufe festlegen](#android_enabling-logs), z. B. `VERBOSE`, `DEBUG` oder `WARN`.

#### Protokolle aktivieren {#enabling-logs}

Um Fehler in Ihrer App zu beheben oder die Bearbeitungszeiten mit dem Braze-Support zu verkürzen, können Sie ausführliche Protokolle für das SDK aktivieren. Wenn Sie ausführliche Protokolle an den Braze-Support senden, stellen Sie sicher, dass diese beginnen, sobald Sie Ihre Anwendung starten, und weit nach dem Auftreten des Problems enden. Eine zentralisierte Übersicht finden Sie unter [Ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/). Informationen zum Interpretieren der Protokollausgabe finden Sie unter [Ausführliche Protokolle lesen]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs/).

Beachten Sie, dass ausführliche Protokolle nur für Ihre Entwicklungsumgebung gedacht sind. Sie sollten sie daher deaktivieren, bevor Sie Ihre App veröffentlichen.

{% alert important %}
Aktivieren Sie ausführliche Protokolle vor allen anderen Aufrufen in `Application.onCreate()`, um sicherzustellen, dass Ihre Protokolle so vollständig wie möglich sind.
{% endalert %}

{% tabs local %}
{% tab Application %}
Um Protokolle direkt in Ihrer App zu aktivieren, fügen Sie der Methode `onCreate()` Ihrer Anwendung vor allen anderen Methoden Folgendes hinzu.

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

Ersetzen Sie `MIN_LOG_LEVEL` durch die **Konstante** der Protokollstufe, die Sie als minimale Protokollstufe festlegen möchten. Alle Protokolle auf der Ebene `>=` Ihrer eingestellten `MIN_LOG_LEVEL` werden an die standardmäßige [`Log`](https://developer.android.com/reference/android/util/Log)-Methode von Android weitergeleitet. Alle Protokolle `<` Ihrer eingestellten `MIN_LOG_LEVEL` werden verworfen.

| Konstante   | Wert           | Beschreibung                                                              |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Protokolliert die detailliertesten Nachrichten zur Fehlersuche und Entwicklung.            |
| `DEBUG`     | 3              | Protokolliert beschreibende Nachrichten zur Fehlersuche und Entwicklung.                  |
| `INFO`      | 4              | Protokolliert informative Nachrichten für allgemeine Highlights.                       |
| `WARN`      | 5              | Protokolliert Warnmeldungen zur Identifizierung potenziell schädlicher Situationen.     |
| `ERROR`     | 6              | Protokolliert Fehlermeldungen, die auf Anwendungsfehler oder schwerwiegende Probleme hinweisen. |
| `ASSERT`    | 7              | Protokolliert Assertion-Nachrichten, wenn Bedingungen während der Entwicklung falsch sind.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Enabling logs" }

Der folgende Code leitet zum Beispiel die Protokollstufen `2`, `3`, `4`, `5`, `6` und `7` an die Methode `Log` weiter.

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

Ersetzen Sie `MIN_LOG_LEVEL` durch den **Wert** der Protokollstufe, die Sie als minimale Protokollstufe festlegen möchten. Alle Protokolle auf der Ebene `>=` Ihrer eingestellten `MIN_LOG_LEVEL` werden an die standardmäßige [`Log`](https://developer.android.com/reference/android/util/Log)-Methode von Android weitergeleitet. Alle Protokolle `<` Ihrer eingestellten `MIN_LOG_LEVEL` werden verworfen.

| Konstante   | Wert           | Beschreibung                                                              |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Protokolliert die detailliertesten Nachrichten zur Fehlersuche und Entwicklung.            |
| `DEBUG`     | 3              | Protokolliert beschreibende Nachrichten zur Fehlersuche und Entwicklung.                  |
| `INFO`      | 4              | Protokolliert informative Nachrichten für allgemeine Highlights.                       |
| `WARN`      | 5              | Protokolliert Warnmeldungen zur Identifizierung potenziell schädlicher Situationen.     |
| `ERROR`     | 6              | Protokolliert Fehlermeldungen, die auf Anwendungsfehler oder schwerwiegende Probleme hinweisen. |
| `ASSERT`    | 7              | Protokolliert Assertion-Nachrichten, wenn Bedingungen während der Entwicklung falsch sind.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Enabling logs" }

Der folgende Code leitet zum Beispiel die Protokollstufen `2`, `3`, `4`, `5`, `6` und `7` an die Methode `Log` weiter.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Ausführliche Protokolle überprüfen {#verifying-verbose-logs}

Um zu überprüfen, ob Ihre Protokolle auf `VERBOSE` eingestellt sind, prüfen Sie, ob `V/Braze` irgendwo in Ihren Protokollen vorkommt. Wenn dies der Fall ist, wurden die ausführlichen Protokolle erfolgreich aktiviert. Zum Beispiel:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Protokolle unterdrücken {#suppressing-logs}

Um alle Protokolle für das Braze Android SDK zu unterdrücken, setzen Sie die Protokollstufe in der Methode `onCreate()` Ihrer Anwendung _vor_ allen anderen Methoden auf `BrazeLogger.SUPPRESS`.

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

Um in Ihren Builds einfach zwischen mehreren API-Schlüsseln wechseln zu können, empfehlen wir, für jede relevante [Build-Variante](https://developer.android.com/studio/build/build-variants.html) eine eigene Datei `braze.xml` zu erstellen. Eine Build-Variante ist eine Kombination aus Build-Typ und Produkt-Flavor. Standardmäßig werden neue Android-Projekte mit den [Build-Typen `debug` und `release`](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) und ohne Produkt-Flavors konfiguriert.

Erstellen Sie für jede relevante Build-Variante eine neue Datei `braze.xml` im Verzeichnis `src/<build variant name>/res/values/`. Wenn die Build-Variante kompiliert wird, verwendet sie den neuen API-Schlüssel.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Wie Sie den API-Schlüssel in Ihrem Code einrichten können, erfahren Sie unter [Laufzeitkonfiguration]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android).
{% endalert %}

### Exklusiver TalkBack für In-App-Nachrichten {#exclusive-in-app-message-talkback}

In Übereinstimmung mit den [Android-Richtlinien für Barrierefreiheit](https://developer.android.com/guide/topics/ui/accessibility) bietet das Braze Android SDK standardmäßig Android TalkBack. Um sicherzustellen, dass nur der Inhalt von In-App-Nachrichten laut vorgelesen wird – ohne andere Bildschirmelemente wie die Titelleiste der App oder die Navigation einzubeziehen – können Sie den Exklusivmodus für TalkBack aktivieren.

So aktivieren Sie den Exklusivmodus für In-App-Nachrichten:

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

Die [Code-Shrinking](https://developer.android.com/build/shrink-code)-Konfiguration ist automatisch in Ihrer Braze-Integration enthalten.

Client-Apps, die den Braze-Code verschleiern, müssen Release-Mapping-Dateien speichern, damit Braze die Stack-Traces interpretieren kann. Wenn Sie den gesamten Braze-Code beibehalten möchten, fügen Sie Folgendes in Ihre ProGuard-Datei ein:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
