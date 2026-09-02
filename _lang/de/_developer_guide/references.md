---
nav_title: Referenzen und Beispiel-Apps
article_title: "Braze SDK Referenzen, Repositories und Beispiel-Apps"
page_order: 5.5
description: "Dies ist eine Liste der Referenzdokumentationen, GitHub-Repositories und Beispiel-Apps, die zu jedem Braze SDK gehören."
toc_headers: h2
---

# Referenzen, Repositories und Beispiel-Apps {#references-repositories-and-sample-apps}

> Dies ist eine Liste der Referenzdokumentationen, GitHub-Repositories und Beispiel-Apps, die zu jedem Braze SDK gehören. In der Referenzdokumentation eines SDKs finden Sie die verfügbaren Klassen, Typen, Funktionen und Variablen. Das GitHub-Repository bietet Insights zu den Funktions- und Attribut-Deklarationen, Code-Änderungen und der Versionierung des SDKs. Jedes Repository enthält außerdem vollständig kompilierbare Beispielanwendungen, mit denen Sie die Features von Braze testen oder neben Ihren eigenen Anwendungen implementieren können.

Gespiegelte Repository-README-Inhalte in der Dokumentation finden Sie unter [Repository-Leitfäden]({{site.baseurl}}/developer_guide/sdk_repository_guides).

## Liste der Ressourcen {#list-of-resources}

{% alert note %}
Derzeit verfügen einige SDKs noch nicht über eine eigene Referenzdokumentation&#8212;wir arbeiten jedoch aktiv daran.
{% endalert %}

| Plattform          | Referenz                                                                                                                                    | Repository                                                                 | Beispiel-App                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [Referenzdokumentation](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [GitHub-Repository](https://github.com/braze-inc/braze-android-sdk)      | [Beispiel-App](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| Swift SDK         | [Referenzdokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [GitHub-Repository](https://github.com/braze-inc/braze-swift-sdk)            | [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| Internet SDK           | [Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [GitHub-Repository](https://github.com/braze-inc/braze-web-sdk)              | [Beispiel-App](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Javascript SDK           | [Referenzdokumentation](https://braze-inc.github.io/braze-javascript-sdk/)                                                               | [GitHub-Repository](https://github.com/braze-inc/braze-javascript-sdk/tree/main)              | N/A              |
| Cordova SDK       | [Deklarationsdatei](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [GitHub-Repository](https://github.com/braze-inc/braze-cordova-sdk)      | [Beispiel-App](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| Flutter SDK       | [Referenzdokumentation](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [GitHub-Repository](https://github.com/braze-inc/braze-flutter-sdk)      | [Beispiel-App](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| React Native SDK  | [Referenzdokumentation](https://braze-inc.github.io/braze-react-native-sdk/)                                                                   | [GitHub-Repository](https://github.com/braze-inc/braze-react-native-sdk) | [Beispiel-App](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Vega SDK          | [Referenzdokumentation](https://braze-inc.github.io/braze-vega-sdk/)                                                                           | [GitHub-Repository](https://github.com/braze-inc/braze-vega-sdk)         | N/A                                                                                       |
| Roku SDK          | N/A                                                                                                                                                         | [GitHub-Repository](https://github.com/braze-inc/braze-roku-sdk)            | [Beispiel-App](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [Deklarationsdatei](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [GitHub-Repository](https://github.com/braze-inc/braze-unity-sdk)          | [Beispiel-App](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| .NET MAUI SDK (ehemals Xamarin)      | N/A                                                                                                                                                         | [GitHub-Repository](https://github.com/braze-inc/braze-xamarin-sdk)      | [Beispiel-App](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Liste der Ressourcen" }

## Erstellen einer Beispiel-App {#building-a-sample-app}

{% tabs %}
{% tab android %}
### „Droidboy“ erstellen {#building-droidboy}

Unsere Testanwendung im [Android SDK GitHub-Repository](https://github.com/braze-inc/braze-android-sdk) heißt Droidboy. Befolgen Sie diese Anweisungen, um eine voll funktionsfähige Kopie neben Ihrem Projekt zu erstellen.

1. Erstellen Sie einen neuen [Workspace]({{site.baseurl}}/user_guide/get_started/workspaces) und notieren Sie sich den Braze-API-Bezeichnerschlüssel.<br><br>
2. Kopieren Sie Ihre FCM-Sender-ID und den Braze-API-Bezeichnerschlüssel an die entsprechenden Stellen in `/droidboy/res/values/braze.xml` (zwischen die Tags für die Strings mit den Namen `com_braze_push_fcm_sender_id` bzw. `com_braze_api_key`).<br><br>
3. Kopieren Sie Ihren FCM-Serverschlüssel und Ihre Server-ID in Ihre Workspace-Einstellungen unter **Einstellungen verwalten**.<br><br>
4. Um die Droidboy-APK zu erstellen, führen Sie `./gradlew assemble` im SDK-Verzeichnis aus. Verwenden Sie unter Windows `gradlew.bat`.<br><br>
5. Um die Droidboy-APK automatisch auf einem Testgerät zu installieren, führen Sie `./gradlew installDebug` im SDK-Verzeichnis aus:

### „Hello Braze“ erstellen {#building-hello-braze}

Die Hello-Braze-Testanwendung zeigt einen minimalen Anwendungsfall des Braze SDK und demonstriert zusätzlich, wie das Braze SDK einfach in ein Gradle-Projekt integriert werden kann.

1. Kopieren Sie Ihren API-Bezeichnerschlüssel von der Seite **Einstellungen verwalten** in Ihre `braze.xml`-Datei im Ordner `res/values`.
![Screenshot zum Erstellen von „Hello Braze“.]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Um die Beispiel-App auf einem Gerät oder Emulator zu installieren, führen Sie den folgenden Befehl im SDK-Verzeichnis aus:
```
./gradlew installDebug
```
Wenn Ihre `ANDROID_HOME`-Variable nicht korrekt gesetzt ist oder Sie keinen `local.properties`-Ordner mit einem gültigen `sdk.dir`-Ordner haben, installiert dieses Plugin auch das Basis-SDK für Sie. Weitere Informationen finden Sie im [Plugin-Repository](https://github.com/JakeWharton/sdk-manager-plugin).

Weitere Informationen zum Android-SDK-Build-System finden Sie in der [GitHub-Repository-README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).
{% endtab %}

{% tab swift %}
### Swift-Test-Apps erstellen {#building-swift-test-apps}

Befolgen Sie diese Anweisungen, um unsere Testanwendungen zu erstellen und auszuführen.

1. Erstellen Sie einen neuen [Workspace]({{site.baseurl}}/user_guide/get_started/workspaces) und notieren Sie sich den App-Bezeichner-API-Schlüssel und den Endpunkt.
2. Wählen Sie basierend auf Ihrer Integrationsmethode (Swift-Paketmanager, CocoaPods, manuell) die entsprechende `xcodeproj`-Datei zum Öffnen aus.
3. Geben Sie Ihren API-Schlüssel und Ihren Endpunkt in das entsprechende Feld in der `Credentials`-Datei ein.
{% endtab %}
{% endtabs %}

{% alert note %}
Verwenden Sie bei der Qualitätssicherung Ihrer SDK-Integration den [SDK-Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging), um Probleme zu beheben, ohne die ausführliche Protokollierung für Ihre App zu aktivieren.
{% endalert %}