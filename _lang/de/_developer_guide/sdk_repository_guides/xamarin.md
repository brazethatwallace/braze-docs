---
nav_title: .NET MAUI (Xamarin) SDK or Software-Development-Kit
article_title: .NET MAUI (Xamarin) SDK or Software-Development-Kit Repository-Leitfaden
page_order: 10
description: "Braze .NET MAUI (Xamarin) SDK or Software-Development-Kit README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# .NET MAUI (Xamarin) SDK or Software-Development-Kit Repository-Leitfaden {#net-maui-xamarin-sdk-repository-guide}

## Über das Braze .NET MAUI (Xamarin) SDK or Software-Development-Kit {#about-the-braze-net-maui-xamarin-sdk}

Das Braze .NET MAUI (Xamarin) SDK or Software-Development-Kit hilft Ihnen, Braze Messaging-, Analytics- und Nutzer:innen-Engagement-Funktionen in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)
- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=xamarin)

## Komponenten {#components}

Das Format dieses Repositorys entspricht dem einer Xamarin-Komponente: Unter `appboy-component` finden Sie die Verzeichnisse `src`,
`libs`, `component`, `nuget` und `samples`. `libs`, `src` und `samples` enthalten jeweils zwei Verzeichnisse, eines für Android und eines für iOS. Die Verzeichnisse
enthalten:

- `libs`: Die kompilierten DLL-Bindings für die Braze SDKs.
- `src`: Die Xamarin-Binding-Projekte, die die DLLs im Ordner `libs` generiert haben.
- `samples`: Xamarin-Anwendungen, die zeigen, wie Sie die Bindings nutzen können, um auf den Braze-Funktionsumfang zuzugreifen.
- `nuget`: Nuspec-Dateien für unsere Xamarin-NuGet-Pakete.

## Versionierung {#versioning}

### Native Bindings {#native-bindings}

Die folgende Tabelle listet die unterstützten Frameworks und nativen Braze-Framework-Versionen für jedes Xamarin-Binding auf.

| Name der Binding-Datei                     | Unterstützte Xamarin-Frameworks                           | Natives Braze-Framework                             | Braze Xamarin SDK or Software-Development-Kit-Version |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK or Software-Development-Kit 43.1.1+                                 | 10.0.0+                   |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 und früher | Android SDK or Software-Development-Kit 23.3.0 und früher                       | 1.26.0 und früher         |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK or Software-Development-Kit 18.2.0+                                   | 10.0.0+                   |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 und früher     | `Appboy_iOS_SDK.framework` Version 4.4.1 und früher | 1.27.0 und früher         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Native Bindings" }

### Xamarin & Xamarin.Forms {#xamarin-xamarinforms}

Seit dem 1. Mai 2024 hat [Microsoft das Ende des Supports für Xamarin und Xamarin.Forms angekündigt](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

Das Braze SDK or Software-Development-Kit hat die Unterstützung für Xamarin & Xamarin.Forms ab Version `4.0.0` eingestellt und stattdessen Unterstützung für [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui) hinzugefügt.

## Fragen? {#questions}

Bei Fragen wenden Sie sich an den technischen Support von Braze.
<!-- END GENERATED README CONTENT -->

Details zum Repository und Beispielprojekte finden Sie unter [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk).