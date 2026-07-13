---
nav_title: SDK Flutter
article_title: Guide du dépôt du SDK Flutter
page_order: 6
description: "Référence du README du SDK Flutter Braze, miroir depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guide du dépôt du SDK Flutter {#flutter-sdk-repository-guide}

## À propos du SDK Flutter Braze {#about-the-braze-flutter-sdk}

Le SDK Flutter Braze vous aide à intégrer les fonctionnalités d'envoi de messages, d'analyse et d'engagement utilisateur de Braze dans votre application.

Pour commencer, consultez les ressources suivantes :

- [Guide utilisateur Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guide développeur Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter)

## Démarrage rapide {#quickstart}

Les extraits de code suivants montrent la configuration minimale requise pour ajouter le SDK Flutter Braze à votre application.

``` bash
flutter pub add braze_plugin
```

### Android

``` xml
<!-- android/res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### iOS

``` swift
// AppDelegate.swift
import BrazeKit
import braze_plugin

class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
  ) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
      apiKey: "<BRAZE_API_KEY>",
      endpoint: "<BRAZE_ENDPOINT>"
    )
    // - Enable logging or customize configuration here
    configuration.logger.level = .info
    let braze = BrazePlugin.initBraze(configuration)
    AppDelegate.braze = braze

    return true
  }
}
```

### Dart

``` dart
import 'package:braze_plugin/braze_plugin.dart';

// ...
_braze = new BrazePlugin();

// ...
_braze.changeUser("Jane Doe");
```

Pour plus d'informations sur les options d'intégration avancées, consultez le [guide développeur Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter).

## Versions prises en charge {#version-support}

Le tableau suivant répertorie les versions minimales prises en charge pour les outils utilisés par le SDK Flutter Braze.

| Outil                                                        | Version minimale prise en charge |
| :----------------------------------------------------------- | :------------------------------- |
| Dart                                                         | 2.17.0+                          |
| Flutter (intégration via CocoaPods)                          | 1.10.0+                          |
| Flutter (intégration via CocoaPods ou gestionnaire de paquets Swift) | 3.24.0+                   |
| Cible de déploiement iOS                                     | 12.0+                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Versions prises en charge" }

Ce SDK hérite également des exigences des SDK natifs Braze sous-jacents. Pour plus d'informations, consultez [braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk) et [braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).

## Exemple d'application {#sample-app}

Le dossier [`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) contient un exemple d'application illustrant comment intégrer et utiliser les API de ce package.

## Contact {#contact}

Si vous avez des questions, contactez le support technique Braze pour obtenir de l'aide.
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les exemples de projets, consultez [https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk).