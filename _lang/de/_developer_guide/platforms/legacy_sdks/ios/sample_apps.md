---
nav_title: Beispiel-Apps
article_title: Beispiel-Apps für iOS
platform: iOS
page_order: 9
description: "Dieser Referenzartikel behandelt iOS-Beispiel-Apps."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Beispiel-Apps {#sample-apps}

Die Braze SDKs werden jeweils mit Beispielanwendungen im Repository geliefert. Jede dieser Apps ist vollständig lauffähig, sodass Sie die Features von Braze testen und gleichzeitig in Ihre eigenen Anwendungen implementieren können. Das Testen des Verhaltens in Ihrer eigenen Anwendung im Vergleich zum erwarteten Verhalten und zu den Codepfaden in den Beispielanwendungen ist eine hervorragende Möglichkeit zur Fehlersuche bei Problemen.

## Testanwendungen erstellen {#building-test-applications}
Im [iOS SDK or Software-Development-Kit GitHub-Repository](https://github.com/appboy/appboy-ios-sdk) sind mehrere Testanwendungen verfügbar. Befolgen Sie diese Anweisungen, um unsere Testanwendungen zu erstellen und auszuführen.

1. Erstellen Sie einen neuen [Workspace]({{site.baseurl}}/user_guide/get_started/workspaces) und notieren Sie sich den App-Bezeichner-API-Schlüssel.
2. Geben Sie Ihren API-Schlüssel in das entsprechende Feld in der Datei `AppDelegate.m` ein.

Push-Benachrichtigungen für die iOS-Testanwendung erfordern eine zusätzliche Konfiguration. Weitere Informationen finden Sie in unserer [iOS-Push-Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration).