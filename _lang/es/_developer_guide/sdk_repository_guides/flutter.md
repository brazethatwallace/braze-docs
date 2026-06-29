---
nav_title: Flutter SDK
article_title: Guía del repositorio del Flutter SDK
page_order: 6
description: "Referencia del README del SDK de Flutter de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Acerca del SDK de Flutter de Braze {#about-the-braze-flutter-sdk}

El SDK de Flutter de Braze te ayuda a integrar las capacidades de mensajería, análisis e interacción con los usuarios de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze]({{site.baseurl}}/user_guide/introduction/)
- [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=flutter)

## Inicio rápido {#quickstart}

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

Consulta [la guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=flutter) para opciones de integración avanzadas.

## Compatibilidad de versiones {#version-support}

| Herramienta                                                  | Versión mínima compatible |
| :----------------------------------------------------------- | :------------------------ |
| Dart                                                         | 2.17.0+                   |
| Flutter (integración vía CocoaPods)                          | 1.10.0+                   |
| Flutter (integración vía CocoaPods o Swift Package Manager)  | 3.24.0+                   |
| Objetivo de despliegue de iOS                                | 12.0+                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Compatibilidad de versiones" }

Este SDK también hereda los requisitos de los SDK nativos subyacentes de Braze. Asegúrate de cumplir también con la información de compatibilidad de versiones definida en [braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk) y [braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).

## Aplicación de ejemplo {#sample-app}

La carpeta [`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) contiene una aplicación de ejemplo que ilustra cómo integrar y utilizar las API de este paquete.

## Ponte en contacto {#contact}

Si tienes preguntas, ponte en contacto con [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Para detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk).