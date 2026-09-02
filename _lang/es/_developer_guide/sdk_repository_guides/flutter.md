---
nav_title: Flutter SDK or kit de desarrollo de software
article_title: Guía del repositorio del Flutter SDK or kit de desarrollo de software
page_order: 6
description: "Referencia del README del SDK or kit de desarrollo de software de Flutter de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del Flutter SDK or kit de desarrollo de software {#flutter-sdk-repository-guide}

## Acerca del SDK or kit de desarrollo de software de Flutter de Braze {#about-the-braze-flutter-sdk}

El SDK or kit de desarrollo de software de Flutter de Braze te ayuda a integrar las capacidades de mensajería, análisis y participación de los usuarios de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guía del desarrollador de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter)

## Inicio rápido {#quickstart}

Los siguientes fragmentos de código muestran la configuración mínima necesaria para añadir el SDK or kit de desarrollo de software de Flutter de Braze a tu aplicación.

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

Para más información sobre opciones de integración avanzadas, consulta la [guía del desarrollador de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter).

## Compatibilidad de versiones {#version-support}

La siguiente tabla muestra las versiones mínimas compatibles de las herramientas utilizadas por el SDK or kit de desarrollo de software de Flutter de Braze.

| Herramienta                                                  | Versión mínima compatible |
| :----------------------------------------------------------- | :------------------------ |
| Dart                                                         | 2.17.0+                   |
| Flutter (integración vía CocoaPods)                          | 1.10.0+                   |
| Flutter (integración vía CocoaPods o Swift Package Administrador)  | 3.24.0+                   |
| Objetivo de despliegue de iOS                                | 12.0+                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Compatibilidad de versiones" }

Este SDK or kit de desarrollo de software también hereda los requisitos de los SDK or kit de desarrollo de software nativos subyacentes de Braze. Para más información, consulta [braze-inc/braze-android-SDK or kit de desarrollo de software](https://github.com/braze-inc/braze-android-sdk) y [braze-inc/braze-swift-SDK or kit de desarrollo de software](https://github.com/braze-inc/braze-swift-sdk).

## Aplicación de ejemplo {#sample-app}

La carpeta [`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) contiene una aplicación de ejemplo que ilustra cómo integrar y utilizar las API de este paquete.

## Contacto {#contact}

Si tienes preguntas, ponte en contacto con el soporte técnico de Braze para obtener ayuda.
<!-- END GENERATED README CONTENT -->

Para detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk).