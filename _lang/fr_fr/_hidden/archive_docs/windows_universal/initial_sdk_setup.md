---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Windows Universal
platform: Windows Universal
page_order: 0
description: "Cet article de référence couvre les étapes initiales d'intégration SDK pour intégrer le SDK Braze sur votre plateforme Windows Universal."
search_rank: 1
hidden: true
---

# Intégration SDK initiale {#initial-sdk-integration}
{% multi_lang_include archive/windows_deprecation.md %}

Le SDK Braze vous fournira une API pour signaler les informations à utiliser pour l'analyse, la segmentation et l'engagement, ainsi que la possibilité d'enregistrer des utilisateurs pour les notifications push et les recevoir.

>  Le SDK Windows Universal est également compatible avec les applications Windows .NET MAUI.

## Étape 1 : Installer le SDK via le gestionnaire de packages NuGet {#step-1-install-the-sdk-via-the-nuget-package-manager}

Le SDK pour Windows Universal est installé à l'aide du [gestionnaire de packages NuGet](http://www.nuget.org/). Pour installer le SDK Braze pour Windows via NuGet :

1. Cliquez avec le bouton droit sur le fichier du projet
2. Cliquez sur « Manage NuGet Packages »
3. Cliquez sur « Online » dans le menu déroulant de gauche
4. Recherchez « Appboy » dans « NuGet.org »
5. Cliquez sur le paquet NuGet « AppboyPlatform.Universal.Release », puis cliquez sur **Install**

>  La bibliothèque Windows Universal doit être utilisée pour toutes les applications Windows 8.1, Windows Phone 8.1 et UWP.

## Étape 2 : Création et configuration de AppboyConfiguration.xml {#step-2-creation-and-configuration-of-appboyconfigurationxml}

Créez un fichier appelé `AppboyConfiguration.xml` dans le répertoire racine de votre projet et ajoutez l'extrait de code suivant dans ce fichier :

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  Veillez à mettre à jour `YOUR_API_KEY_HERE` avec votre clé API qui se trouve sur la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/).

Une fois que vous avez ajouté cet extrait de code, assurez-vous de modifier les propriétés de fichier suivantes pour `AppboyConfiguration.xml` :

1. Définissez **Build Action** sur `Content`
2. Définissez **Copy to Output Directory** sur `Copy Always`

## Étape 3 : Configuration de package.appxmanifest {#step-3-configuring-packageappxmanifest}

Dans l'onglet « Capabilities », assurez-vous que `Internet (Client)` est coché.
![]({% image_buster /assets/img_archive/internet_client.png %})

## Étape 4 : Modifier la classe de votre application {#step-4-editing-your-app-class}

- Ajoutez les éléments suivants aux `usings` de votre fichier `App.xaml.cs` :

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- Appelez les éléments suivants dans votre méthode de cycle de vie `OnLaunched` :

```csharp
Appboy.SharedInstance.OpenSession();
```

- Appelez les éléments suivants dans votre méthode de cycle de vie `OnSuspending` :

```csharp
Appboy.SharedInstance.CloseSession();
```

## Intégration SDK de base terminée {#basic-sdk-integration-complete}

Braze devrait maintenant collecter des données depuis votre application. Consultez les articles suivants pour savoir comment enregistrer des [attributs]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/), des [événements]({{site.baseurl}}/developer_guide/analytics/logging_events/) et des [achats]({{site.baseurl}}/developer_guide/analytics/logging_purchases/) dans notre SDK et comment instrumenter l'envoi de messages push.

>  Si vous utilisez le projet Unity de Braze dans la même application, il se peut que vous deviez qualifier entièrement les appels à Braze comme « AppboyPlatform.Universal.Appboy ».