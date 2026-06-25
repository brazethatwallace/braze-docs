---
nav_title: SDK .NET MAUI (Xamarin)
article_title: Guide du dépôt du SDK .NET MAUI (Xamarin)
page_order: 10
description: "Référence du README du SDK .NET MAUI (Xamarin) de Braze, miroir depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## À propos du SDK .NET MAUI (Xamarin) de Braze {#about-the-braze-net-maui-xamarin-sdk}

Le SDK .NET MAUI (Xamarin) de Braze vous aide à intégrer les fonctionnalités d'envoi de messages, d'analyse et d'engagement utilisateur de Braze dans votre application.

Pour commencer, consultez les ressources suivantes :

- [Guide de l'utilisateur Braze]({{site.baseurl}}/user_guide/introduction/)
- [Guide du développeur Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=xamarin)

## Composants {#components}

Le format de ce dépôt est celui d'un composant Xamarin : sous `appboy-component`, vous trouverez les répertoires `src`,
`libs`, `component`, `nuget` et `samples`. `libs`, `src` et `samples` contiennent chacun deux répertoires, un pour Android et un pour iOS. Les répertoires
contiennent :

- `libs` : les liaisons DLL compilées pour les SDK Braze.
- `src` : les projets de liaisons Xamarin qui ont généré les DLL présentes dans le dossier libs.
- `samples` : des applications Xamarin montrant comment utiliser les liaisons pour accéder à l'ensemble des fonctionnalités de Braze.
- `nuget` : les fichiers Nuspec pour nos packages NuGet Xamarin.

## Versionnement {#versioning}

### Liaisons natives {#native-bindings}

| Nom du fichier de liaison                  | Frameworks Xamarin pris en charge                         | Framework natif Braze                               | Version du SDK Xamarin Braze |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK 41.0.0+                                 | 9.0.0+                    |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 et antérieur | Android SDK 23.3.0 et antérieur                     | 1.26.0 et antérieur       |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK 14.0.1+                                   | 9.0.0+                    |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 et antérieur   | `Appboy_iOS_SDK.framework` version 4.4.1 et antérieure | 1.27.0 et antérieur     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Liaisons natives" }

### Xamarin et Xamarin.Forms {#xamarin-xamarinforms}

Depuis le 1er mai 2024, [Microsoft a annoncé la fin de la prise en charge de Xamarin et Xamarin.Forms](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

Le SDK Braze a abandonné la prise en charge de Xamarin et Xamarin.Forms à partir de la version `4.0.0` et a ajouté la prise en charge de [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui).

## Des questions ? {#questions}

Si vous avez des questions, veuillez contacter [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les exemples de projets, consultez [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk).