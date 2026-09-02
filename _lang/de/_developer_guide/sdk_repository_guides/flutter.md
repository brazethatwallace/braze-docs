---
nav_title: Flutter SDK or Software-Development-Kit
article_title: Leitfaden zum Flutter SDK or Software-Development-Kit-Repository
page_order: 6
description: "Braze Flutter SDK or Software-Development-Kit README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Leitfaden zum Flutter SDK or Software-Development-Kit-Repository {#flutter-sdk-repository-guide}

## Über das Braze Flutter SDK or Software-Development-Kit {#about-the-braze-flutter-sdk}

Das Braze Flutter SDK or Software-Development-Kit hilft Ihnen, Braze-Messaging, Analytics und Nutzer:innen-Engagement-Funktionen in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze-Benutzerhandbuch](https://www.braze.com/docs/user_guide/introduction/)
- [Braze-Entwicklerhandbuch](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter)

## Schnellstart {#quickstart}

Die folgenden Snippets zeigen die Mindestkonfiguration, die erforderlich ist, um das Braze Flutter SDK or Software-Development-Kit zu Ihrer App hinzuzufügen.

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

Weitere Informationen zu erweiterten Integrationsoptionen finden Sie im [Braze-Entwicklerhandbuch](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter).

## Versionsunterstützung {#version-support}

Die folgende Tabelle listet die mindestens unterstützten Versionen für Tools auf, die vom Braze Flutter SDK or Software-Development-Kit verwendet werden.

| Tool                                                         | Mindestens unterstützte Version |
| :----------------------------------------------------------- | :------------------------ |
| Dart                                                         | 2.17.0+                   |
| Flutter (Integration über CocoaPods)                         | 1.10.0+                   |
| Flutter (Integration über CocoaPods oder Swift-Paketmanager) | 3.24.0+                   |
| iOS-Bereitstellungsziel                                      | 12.0+                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Versionsunterstützung" }

Dieses SDK or Software-Development-Kit übernimmt zusätzlich die Anforderungen der zugrunde liegenden nativen Braze SDKs. Weitere Informationen finden Sie unter [braze-inc/braze-android-SDK or Software-Development-Kit](https://github.com/braze-inc/braze-android-sdk) und [braze-inc/braze-swift-SDK or Software-Development-Kit](https://github.com/braze-inc/braze-swift-sdk).

## Beispiel-App {#sample-app}

Der Ordner [`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) enthält eine Beispiel-App, die zeigt, wie Sie die APIs dieses Pakets integrieren und verwenden können.

## Kontakt {#contact}

Bei Fragen wenden Sie sich bitte an den technischen Support von Braze.
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte besuchen Sie [https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk).