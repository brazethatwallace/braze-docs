---
nav_title: Flutter SDK
article_title: Leitfaden zum Flutter SDK-Repository
page_order: 6
description: "Braze Flutter SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Über das Braze Flutter SDK {#about-the-braze-flutter-sdk}

Das Braze Flutter SDK hilft Ihnen, Braze-Messaging, Analytics und Nutzer:innen-Engagement-Funktionen in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze-Benutzerhandbuch]({{site.baseurl}}/user_guide/introduction)
- [Braze-Entwicklerhandbuch]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter)

## Schnellstart {#quickstart}

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

Weitere Informationen zu erweiterten Integrationsoptionen finden Sie im [Braze-Entwicklerhandbuch]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter).

## Versionsunterstützung {#version-support}

| Tool                                                         | Mindestens unterstützte Version |
| :----------------------------------------------------------- | :------------------------ |
| Dart                                                         | 2.17.0+                   |
| Flutter (Integration über CocoaPods)                         | 1.10.0+                   |
| Flutter (Integration über CocoaPods oder Swift-Paketmanager) | 3.24.0+                   |
| iOS-Bereitstellungsziel                                      | 12.0+                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Versionsunterstützung" }

Dieses SDK übernimmt zusätzlich die Anforderungen der zugrunde liegenden nativen Braze SDKs. Beachten Sie auch die Informationen zur Versionsunterstützung in [braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk) und [braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).

## Beispiel-App {#sample-app}

Der Ordner [`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) enthält eine Beispiel-App, die zeigt, wie Sie die APIs dieses Pakets integrieren und verwenden können.

## Kontakt {#contact}

Wenn Sie Fragen haben, kontaktieren Sie bitte [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte besuchen Sie [https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk).