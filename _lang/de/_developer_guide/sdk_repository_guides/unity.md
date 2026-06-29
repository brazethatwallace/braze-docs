---
nav_title: Unity SDK
article_title: Unity SDK – Repository-Leitfaden
page_order: 9
description: "Braze Unity SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Über das Braze Unity SDK {#about-the-braze-unity-sdk}

Das Braze Unity SDK hilft Ihnen, Braze-Messaging, Analytics und Funktionen zum Nutzer:innen-Engagement in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze-Benutzerhandbuch]({{site.baseurl}}/user_guide/introduction/)
- [Braze-Entwicklerhandbuch]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unity)

## Plugin-Einrichtung {#plugin-setup}

Bevor Sie Braze in Unity-Skripten verwenden können, müssen Sie die Plugin-Dateien in Ihr Unity-Projekt importieren.

**Empfohlen:** Die Android- und iOS-Plugins sind als Unity-Paket gebündelt und können von der [SDK-Release-Seite][1] heruntergeladen werden.

**Manuelle Plugin-Einrichtung:** Alternativ können Sie die Plugins in Ihr Unity-Projekt kopieren:
  1. Klonen Sie zunächst dieses Repo.
  2. Wenn Sie keine anderen Plugins verwenden, müssen Sie lediglich das Verzeichnis `Plugins` aus diesem Repo in den Ordner `Assets` Ihres Unity-Projekts kopieren.
  3. Wenn Sie bereits ein Verzeichnis `/<your-project>/Assets/Plugins` haben (wahrscheinlich, weil Sie bereits ein anderes Plugin verwenden), kopieren Sie `Plugins/Appboy/AppboyBinding.cs` nach `/<your-project>/Assets/Plugins`. Kopieren Sie dann den Inhalt von `Plugins/iOS` und `Plugins/Android` aus diesem Repo nach `/<your-project>/Assets/Plugins/iOS` bzw. `/<your-project>/Assets/Plugins/Android`.

## Integrations-Einrichtung {#integration-setup}

Um Braze in Ihre Unity-Anwendung zu integrieren, folgen Sie unserer Anleitung zur [Integration des Braze Unity SDK][2].

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: {{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity

## Kontakt {#contact}

Wenn Sie Fragen haben, kontaktieren Sie bitte [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte besuchen Sie [https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk).