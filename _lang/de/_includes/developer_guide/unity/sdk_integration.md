## Über das Unity Braze SDK {#about-the-unity-braze-sdk}

Eine vollständige Liste der Typen, Funktionen, Variablen und mehr finden Sie in der [Unity-Deklarationsdatei](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs). Und wenn Sie Unity für iOS bereits manuell integriert haben, können Sie stattdessen [zu einer automatisierten Integration wechseln](#unity_automated-integration).

## Integration des Unity SDK {#integrating-the-unity-sdk}

### Voraussetzungen {#prerequisites}

Bevor Sie beginnen, überprüfen Sie, ob Ihre Umgebung von der [neuesten Braze Unity SDK-Version](https://github.com/braze-inc/braze-unity-sdk/releases) unterstützt wird.

### Schritt 1: Wählen Sie Ihr Braze Unity-Paket {#step-1-choose-your-braze-unity-package}

{% tabs %}
{% tab Android %}
Das Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) bündelt native Bindings für die Plattformen Android und iOS sowie eine C#-Schnittstelle.

Auf der [Braze Unity Releases-Seite](https://github.com/Appboy/appboy-unity-sdk/releases) stehen mehrere Braze Unity-Pakete zum Download zur Verfügung:

- `Appboy.unitypackage`
    - Dieses Paket bündelt die Braze Android- und iOS-SDKs sowie die [SDWebImage](https://github.com/SDWebImage/SDWebImage)-Abhängigkeit für das iOS-SDK, die für die ordnungsgemäße Funktionalität der In-App-Nachrichten und Content-Cards-Features von Braze auf iOS erforderlich ist. Das SDWebImage-Framework wird zum Herunterladen und Anzeigen von Bildern, einschließlich GIFs, verwendet. Wenn Sie die volle Funktionalität von Braze nutzen möchten, laden Sie dieses Paket herunter und importieren Sie es.
- `Appboy-nodeps.unitypackage`
    - Dieses Paket ähnelt dem `Appboy.unitypackage`, mit der Ausnahme, dass das [SDWebImage](https://github.com/SDWebImage/SDWebImage)-Framework nicht enthalten ist. Dieses Paket ist nützlich, wenn Sie das SDWebImage-Framework nicht in Ihrer iOS-App verwenden möchten.

{% alert note %}
Ab Unity 2.6.0 benötigt das gebündelte Braze Android SDK-Artefakt [AndroidX](https://developer.android.com/jetpack/androidx)-Abhängigkeiten. Wenn Sie zuvor ein `jetified` unitypackage verwendet haben, können Sie bedenkenlos auf das entsprechende `unitypackage` umsteigen.

Wenn Android-Builds mit der Meldung „This project uses AndroidX dependencies, but the 'android.useAndroidX' property is not enabled“ fehlschlagen, aktivieren Sie [Custom Gradle Properties Template](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) in Ihren Unity Publishing Settings. Öffnen Sie dann `Assets/Plugins/Android/gradleTemplate.properties` und setzen Sie `android.useAndroidX=true`. Ein funktionierendes Template finden Sie in der [Braze Unity-Beispiel-App](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples) und deren [`gradleTemplate.properties`](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/gradleTemplate.properties)-Datei.
{% endalert %}
{% endtab %}

{% tab Swift %}
Das Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) bündelt native Bindings für die Plattformen Android und iOS sowie eine C#-Schnittstelle.

Das Braze Unity-Paket steht auf der [Braze Unity Releases-Seite](https://github.com/Appboy/appboy-unity-sdk/releases) mit zwei Integrationsoptionen zum Download bereit:

1. Nur `Appboy.unitypackage`
  - Dieses Paket bündelt die Braze Android- und iOS-SDKs ohne zusätzliche Abhängigkeiten. Mit dieser Integrationsmethode funktionieren die In-App-Nachrichten und Content-Cards-Features von Braze auf iOS nicht ordnungsgemäß. Wenn Sie die volle Funktionalität von Braze ohne angepassten Code nutzen möchten, verwenden Sie stattdessen die nächste Option.
  - Um diese Integrationsoption zu nutzen, stellen Sie sicher, dass das Kästchen neben `Import SDWebImage dependency` in der Unity-UI unter „Braze Configuration“ *deaktiviert* ist.
2. `Appboy.unitypackage` mit `SDWebImage`
  - Diese Integrationsoption bündelt die Braze Android- und iOS-SDKs sowie die [SDWebImage](https://github.com/SDWebImage/SDWebImage)-Abhängigkeit für das iOS-SDK, die für die ordnungsgemäße Funktionalität der In-App-Nachrichten und Content-Cards-Features von Braze auf iOS erforderlich ist. Das `SDWebImage`-Framework wird zum Herunterladen und Anzeigen von Bildern, einschließlich GIFs, verwendet. Wenn Sie die volle Funktionalität von Braze nutzen möchten, laden Sie dieses Paket herunter und importieren Sie es.
  - Um `SDWebImage` automatisch zu importieren, müssen Sie das Kästchen neben `Import SDWebImage dependency` in der Unity-UI unter „Braze Configuration“ *aktivieren*.

{% alert note %}
Um zu prüfen, ob Sie die [SDWebImage](https://github.com/SDWebImage/SDWebImage)-Abhängigkeit für Ihr iOS-Projekt benötigen, besuchen Sie die [iOS In-App-Nachricht-Dokumentation]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).
{% endalert %}
{% endtab %}
{% endtabs %}

### Schritt 2: Paket importieren {#step-2-import-the-package}

{% tabs %}
{% tab Android %}
Importieren Sie das Paket im Unity-Editor in Ihr Unity-Projekt, indem Sie zu **Assets > Import Package > Custom Package** navigieren. Klicken Sie anschließend auf **Import**.

Alternativ folgen Sie den Anweisungen zum [Importieren von Unity-Assetpaketen](https://docs.unity3d.com/Manual/AssetPackages.html), um eine detailliertere Anleitung zum Importieren von angepassten Unity-Paketen zu erhalten.

{% alert note %}
Wenn Sie nur das iOS- oder Android-Plugin importieren möchten, heben Sie die Auswahl des Unterverzeichnisses `Plugins/Android` oder `Plugins/iOS` auf, wenn Sie das Braze `.unitypackage` importieren.
{% endalert %}
{% endtab %}

{% tab Swift %}
Importieren Sie das Paket im Unity-Editor in Ihr Unity-Projekt, indem Sie zu **Assets > Import Package > Custom Package** navigieren. Klicken Sie anschließend auf **Import**.

Alternativ folgen Sie den Anweisungen zum [Importieren von Unity-Assetpaketen](https://docs.unity3d.com/Manual/AssetPackages.html), um eine detailliertere Anleitung zum Importieren von angepassten Unity-Paketen zu erhalten.

{% alert note %}
Wenn Sie nur das iOS- oder Android-Plugin importieren möchten, heben Sie die Auswahl des Unterverzeichnisses `Plugins/Android` oder `Plugins/iOS` auf, wenn Sie das Braze `.unitypackage` importieren.
{% endalert %}
{% endtab %}
{% endtabs %}

### Schritt 3: SDK konfigurieren {#step-3-configure-the-sdk}

{% tabs %}
{% tab Android %}
#### Schritt 3.1: `AndroidManifest.xml` konfigurieren {#step-31-configure-androidmanifestxml}

Konfigurieren Sie [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html), damit das Braze SDK ordnungsgemäß funktioniert. Wenn Ihre App keine `AndroidManifest.xml` hat, können Sie das folgende Template als Vorlage verwenden. Wenn Sie bereits eine `AndroidManifest.xml` haben, stellen Sie sicher, dass die folgenden fehlenden Abschnitte zu Ihrer bestehenden `AndroidManifest.xml` hinzugefügt werden.

1. Gehen Sie in das Verzeichnis `Assets/Plugins/Android/` und öffnen Sie Ihre Datei `AndroidManifest.xml`. Dies ist der [Standardspeicherort im Unity-Editor](https://docs.unity3d.com/Manual/android-manifest.html).
2. Fügen Sie in Ihrer `AndroidManifest.xml` die erforderlichen Berechtigungen und Activities aus dem folgenden Template hinzu.
3. Wenn Sie fertig sind, sollte Ihre `AndroidManifest.xml` nur eine einzige Activity mit `"android.intent.category.LAUNCHER"` enthalten.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:theme="@style/UnityThemeSelector"
      android:label="@string/app_name"
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

{% alert important %}
Alle in Ihrer `AndroidManifest.xml`-Datei registrierten Activity-Klassen sollten vollständig in das Braze Android SDK integriert sein, da Ihre Analytics sonst nicht erfasst werden. Wenn Sie Ihre eigene Activity-Klasse hinzufügen, stellen Sie sicher, dass Sie [den Braze Unity-Player erweitern](#unity_extend-unity-player), um dies zu verhindern.
{% endalert %}

#### Schritt 3.2: `AndroidManifest.xml` mit Ihrem Paketnamen aktualisieren {#step-32-update-androidmanifestxml-with-your-package-name}

Um Ihren Paketnamen zu finden, klicken Sie auf **File > Build Settings > Player Settings > Android Tab**.

![Unity Player Settings Android-Tab mit dem Anwendungspaketnamen.]({% image_buster /assets/img_archive/UnityPackageName.png %})

In Ihrer `AndroidManifest.xml` sollten alle Instanzen von `REPLACE_WITH_YOUR_PACKAGE_NAME` durch Ihren `Package Name` aus dem vorherigen Schritt ersetzt werden.

#### Schritt 3.3: Gradle-Abhängigkeiten hinzufügen {#step-33-add-gradle-dependencies}

Um Gradle-Abhängigkeiten zu Ihrem Unity-Projekt hinzuzufügen, aktivieren Sie zunächst [„Custom Main Gradle Template“](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) in Ihren Publishing Settings. Dadurch wird eine Template-Gradle-Datei erstellt, die Ihr Projekt verwenden wird. Eine Gradle-Datei ist für das Setzen von Abhängigkeiten und andere Projekteinstellungen zur Build-Zeit zuständig. Weitere Informationen finden Sie in der Braze Unity-Beispiel-App unter [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle).

Die folgenden Abhängigkeiten sind erforderlich:

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

Sie können diese Abhängigkeiten auch mit dem [External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver) festlegen.

#### Schritt 3.4: Unity-Android-Integration automatisieren {#step-34-automate-the-unity-android-integration}

Braze bietet eine native Unity-Lösung für die Automatisierung der Unity-Android-Integration.

1. Öffnen Sie im Unity-Editor die Braze-Konfigurationseinstellungen, indem Sie zu **Braze > Braze Configuration** navigieren.
2. Aktivieren Sie das Kontrollkästchen **Automate Unity Android Integration**.
3. Geben Sie im Feld **Braze API Key** den API-Schlüssel Ihrer Anwendung ein, den Sie im Braze-Dashboard unter **Einstellungen verwalten** finden.

{% alert note %}
Diese automatische Integration sollte nicht mit einer manuell erstellten `braze.xml`-Datei verwendet werden, da die Konfigurationswerte bei der Projekterstellung in Konflikt geraten können. Wenn Sie eine manuelle `braze.xml`-Datei benötigen, deaktivieren Sie die automatische Integration.
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Schritt 3.1: API-Schlüssel festlegen {#step-31-set-your-api-key}

Braze bietet eine native Unity-Lösung für die Automatisierung der Unity-iOS-Integration. Diese Lösung modifiziert das erstellte Xcode-Projekt mit Unitys [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) und erstellt eine Unterklasse des `UnityAppController` mithilfe des Makros `IMPL_APP_CONTROLLER_SUBCLASS`.

1. Öffnen Sie im Unity-Editor die Braze-Konfigurationseinstellungen, indem Sie zu **Braze > Braze Configuration** navigieren.
2. Aktivieren Sie das Kontrollkästchen **Automate Unity iOS Integration**.
3. Geben Sie im Feld **Braze API Key** den API-Schlüssel Ihrer Anwendung ein, den Sie unter **Einstellungen verwalten** finden.

![Unity Braze-Konfigurationsfenster mit den Feldern „Automate Unity iOS Integration“ und „Braze API Key“.]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Wenn Ihre Anwendung bereits eine andere `UnityAppController`-Unterklasse verwendet, müssen Sie die Implementierung Ihrer Unterklasse mit `AppboyAppDelegate.mm` zusammenführen.
{% endtab %}
{% endtabs %}

## Unity-Paket anpassen {#customizing-the-unity-package}

### Schritt 1: Repository klonen {#step-1-clone-the-repository}

Klonen Sie in Ihrem Terminal das [Braze Unity SDK GitHub-Repository](https://github.com/braze-inc/braze-unity-sdk) und navigieren Sie dann zu diesem Ordner:

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### Schritt 2: Paket aus dem Repository exportieren {#step-2-export-package-from-repository}

Starten Sie zunächst Unity und lassen Sie es im Hintergrund laufen. Führen Sie dann im Stammverzeichnis des Repositorys den folgenden Befehl aus, um das Paket nach `braze-unity-sdk/unity-package/` zu exportieren.

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn nach der Ausführung dieser Befehle Probleme auftreten, lesen Sie [Unity: Befehlszeilenargumente](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html).
{% endalert %}

### Schritt 3: Paket in Unity importieren {#step-3-import-package-into-unity}

1. Importieren Sie in Unity das gewünschte Paket in Ihr Unity-Projekt, indem Sie zu **Assets** > **Import Package** > **Custom Package** navigieren.
2. Falls es Dateien gibt, die Sie nicht importieren möchten, deaktivieren Sie diese jetzt.
3. Passen Sie das exportierte Unity-Paket an, das sich unter `Assets/Editor/Build.cs` befindet.

## Zu einer automatisierten Integration wechseln (nur Swift) {#automated-integration}

Um die Vorteile der automatisierten iOS-Integration des Braze Unity SDK zu nutzen, befolgen Sie diese Schritte für den Übergang von einer manuellen zu einer automatisierten Integration.

1. Entfernen Sie den gesamten Braze-bezogenen Code aus der `UnityAppController`-Unterklasse Ihres Xcode-Projekts.
2. Entfernen Sie die Braze iOS-Bibliotheken aus Ihrem Unity- oder Xcode-Projekt (z. B. `Appboy_iOS_SDK.framework` und `SDWebImage.framework`).
3. Importieren Sie das Braze Unity-Paket erneut in Ihr Projekt. Eine vollständige Anleitung finden Sie unter [Schritt 2: Paket importieren](#unity_step-2-import-the-package).
4. Legen Sie Ihren API-Schlüssel erneut fest. Eine vollständige Anleitung finden Sie unter [Schritt 3.1: API-Schlüssel festlegen](#unity_step-31-set-your-api-key).

## Optionale Konfigurationen {#optional-configurations}

### Ausführliche Protokollierung {#verbose-logging}

Um die ausführliche Protokollierung im Unity-Editor zu aktivieren, gehen Sie wie folgt vor:

1. Öffnen Sie die Braze-Konfigurationseinstellungen, indem Sie zu **Braze** > **Braze Configuration** navigieren.
2. Klicken Sie auf das Dropdown-Menü **Show Braze Android Settings**.
3. Geben Sie im Feld **SDK Log Level** den Wert „0“ ein.

### Prime 31-Kompatibilität {#prime-31-compatibility}

Um das Braze Unity-Plugin mit Prime31-Plugins zu verwenden, bearbeiten Sie die `AndroidManifest.xml` Ihres Projekts, um die mit Prime31 kompatiblen Activity-Klassen zu verwenden. Ändern Sie alle Referenzen von
`com.braze.unity.BrazeUnityPlayerActivity` zu `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

### Amazon Device Messaging (ADM)

Braze unterstützt die Integration von [ADM Push](https://developer.amazon.com/public/apis/engage/device-messaging) in Unity-Apps. Wenn Sie ADM Push integrieren möchten, erstellen Sie eine Datei namens `api_key.txt`, die Ihren ADM-API-Schlüssel enthält, und legen Sie sie im Ordner `Plugins/Android/assets/` ab. Weitere Informationen zur Integration von ADM mit Braze finden Sie in unserer [Anleitung zur ADM-Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity).

### Braze Unity-Player erweitern (nur Android) {#extend-unity-player}

In der mitgelieferten Beispieldatei `AndroidManifest.xml` ist eine Activity-Klasse registriert: [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Diese Klasse ist in das Braze SDK integriert und erweitert `UnityPlayerActivity` um Sitzungsverarbeitung, In-App-Nachricht-Registrierung, Push-Benachrichtigungs-Analytics-Protokollierung und mehr. Weitere Informationen zur Erweiterung der Klasse `UnityPlayerActivity` finden Sie in der [Unity-Dokumentation](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html).

Wenn Sie Ihre eigene angepasste `UnityPlayerActivity` in einem Bibliotheks- oder Plugin-Projekt erstellen, müssen Sie unsere `BrazeUnityPlayerActivity` erweitern, um Ihre angepasste Funktionalität mit Braze zu integrieren. Bevor Sie mit der Erweiterung von `BrazeUnityPlayerActivity` beginnen, befolgen Sie unsere Anweisungen zur Integration von Braze in Ihr Unity-Projekt.

1. Fügen Sie das Braze Android SDK als Abhängigkeit zu Ihrem Bibliotheks- oder Plugin-Projekt hinzu, wie in den [Anweisungen zur Braze Android SDK-Integration]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) beschrieben.
2. Integrieren Sie unsere Unity-`.aar`-Datei, die unsere Unity-spezifische Funktionalität enthält, in Ihr Android-Bibliotheksprojekt, das Sie für Unity erstellen. Die `appboy-unity.aar` ist in unserem [öffentlichen Repository](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android) verfügbar. Nachdem unsere Unity-Bibliothek erfolgreich integriert wurde, ändern Sie Ihre `UnityPlayerActivity`, um `BrazeUnityPlayerActivity` zu erweitern.
3. Exportieren Sie Ihr Bibliotheks- oder Plugin-Projekt und legen Sie es wie gewohnt in `/<your-project>/Assets/Plugins/Android` ab. Fügen Sie keinen Braze-Quellcode in Ihre Bibliothek oder Ihr Plugin ein, da dieser bereits in `/<your-project>/Assets/Plugins/Android` vorhanden ist.
4. Bearbeiten Sie Ihre `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml`, um Ihre `BrazeUnityPlayerActivity`-Unterklasse als Hauptaktivität anzugeben.

Sie sollten nun in der Lage sein, eine `.apk` aus der Unity IDE zu erstellen, die vollständig in Braze integriert ist und Ihre angepasste `UnityPlayerActivity`-Funktionalität enthält.

## Fehlerbehebung {#troubleshooting}

### Fehler: „File could not be read“ {#error-file-could-not-be-read}

Fehler wie die folgenden können Sie getrost ignorieren. Apple-Software verwendet eine proprietäre PNG-Erweiterung namens CgBI, die von Unity nicht erkannt wird. Diese Fehler haben keinen Einfluss auf Ihren iOS-Build oder die korrekte Anzeige der zugehörigen Bilder im Braze-Bundle.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
