---
nav_title: .NET MAUI (Xamarin) SDK
article_title: .NET MAUI (Xamarin) SDK Repository-Leitfaden
page_order: 10
description: "Braze .NET MAUI (Xamarin) SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Über das Braze .NET MAUI (Xamarin) SDK {#about-the-braze-net-maui-xamarin-sdk}

Das Braze .NET MAUI (Xamarin) SDK hilft Ihnen, Braze-Messaging, Analytics und Nutzer:innen-Engagement-Funktionen in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze-Benutzerhandbuch](https://www.braze.com/docs/user_guide/introduction/)
- [Braze-Entwicklerhandbuch](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=xamarin)

## Komponenten {#components}

Das Format dieses Repositorys entspricht dem einer Xamarin-Komponente: Unter `appboy-component` finden Sie die Verzeichnisse `src`,
`libs`, `component`, `nuget` und `samples`. `libs`, `src` und `samples` enthalten jeweils zwei Verzeichnisse, eines für Android und eines für iOS. Die Verzeichnisse
enthalten:

- `libs`: die kompilierten DLL-Bindings für die Braze SDKs.
- `src`: die Xamarin-Binding-Projekte, die die DLLs im libs-Ordner erzeugt haben.
- `samples`: Xamarin-Anwendungen, die zeigen, wie die Bindings verwendet werden, um auf den Braze-Funktionsumfang zuzugreifen.
- `nuget`: Nuspec-Dateien für unsere Xamarin-NuGet-Pakete.

## Versionierung {#versioning}

### Native Bindings {#native-bindings}

| Binding-Dateiname                          | Unterstützte Xamarin-Frameworks                           | Natives Braze-Framework                             | Braze Xamarin SDK-Version |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK 41.0.0+                                 | 9.0.0+                    |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 und früher | Android SDK 23.3.0 und früher                       | 1.26.0 und früher         |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK 14.0.1+                                   | 9.0.0+                    |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 und früher     | `Appboy_iOS_SDK.framework` Version 4.4.1 und früher | 1.27.0 und früher         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Native Bindings" }

### Xamarin und Xamarin.Forms {#xamarin-xamarinforms}

Seit dem 1. Mai 2024 hat [Microsoft das Ende des Supports für Xamarin und Xamarin.Forms angekündigt](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

Das Braze SDK hat die Unterstützung für Xamarin und Xamarin.Forms ab Version `4.0.0` eingestellt und Unterstützung für [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui) hinzugefügt.

## Fragen? {#questions}

Wenn Sie Fragen haben, kontaktieren Sie bitte [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte siehe [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk).