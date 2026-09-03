---
nav_title: Unity SDK
article_title: Unity SDK – Repository-Leitfaden
page_order: 9
description: "Braze Unity SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Unity SDK – Repository-Leitfaden {#unity-sdk-repository-guide}

## Über das Unity Braze SDK {#about-the-braze-unity-sdk}

Das Unity Braze SDK hilft Ihnen, Braze-Messaging, Analytics und Funktionen zur Nutzer:innen-Interaktion in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)
- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=unity)

## Plugin-Einrichtung {#plugin-setup}

Bevor Sie Braze in Unity-Skripten verwenden können, müssen Sie die Plugin-Dateien in Ihr Unity-Projekt importieren.

**Empfohlen:** Die Android- und iOS-Plugins sind als Unity-Paket gebündelt und können von der [SDK-Release-Seite][1] heruntergeladen werden.

**Manuelle Plugin-Einrichtung:** Alternativ können Sie die Plugins in Ihr Unity-Projekt kopieren:
  1. Klonen Sie zunächst dieses Repo.
  2. Wenn Sie keine anderen Plugins verwenden, müssen Sie lediglich das Verzeichnis `Plugins` aus diesem Repo in den Ordner `Assets` Ihres Unity-Projekts kopieren.
  3. Wenn Sie bereits ein Verzeichnis `/<your-project>/Assets/Plugins` haben (wahrscheinlich, weil Sie bereits ein anderes Plugin verwenden), kopieren Sie `Plugins/Appboy/AppboyBinding.cs` nach `/<your-project>/Assets/Plugins`. Kopieren Sie dann den Inhalt von `Plugins/iOS` und `Plugins/Android` aus diesem Repo in `/<your-project>/Assets/Plugins/iOS` bzw. `/<your-project>/Assets/Plugins/Android`.

## Einrichtung der Integration {#integration-setup}

Um Braze in Ihre Unity-Anwendung zu integrieren, folgen Sie den Anweisungen unter [Integration des Unity Braze SDK][2].

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=unity

## Kontakt {#contact}

Bei Fragen wenden Sie sich an den technischen Support von Braze.
<!-- END GENERATED README CONTENT -->

Details zum Repository und Beispielprojekte finden Sie unter [https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk).