---
nav_title: Flutter SDK or kit de desenvolvimento de software
article_title: Guia do repositório do Flutter SDK or kit de desenvolvimento de software
page_order: 6
description: "Referência do README do Braze Flutter SDK or kit de desenvolvimento de software espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do Flutter SDK or kit de desenvolvimento de software {#flutter-sdk-repository-guide}

## Sobre o Braze Flutter SDK or kit de desenvolvimento de software {#about-the-braze-flutter-sdk}

O Braze Flutter SDK or kit de desenvolvimento de software ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu aplicativo.

Para começar, consulte os seguintes recursos:

- [Guia do Usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter)

## Início rápido {#quickstart}

Os snippets a seguir mostram a configuração mínima necessária para adicionar o Braze Flutter SDK or kit de desenvolvimento de software ao seu app.

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

Para saber mais sobre opções avançadas de integração, consulte o [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter).

## Suporte de versão {#version-support}

A tabela a seguir lista as versões mínimas suportadas para as ferramentas usadas pelo Braze Flutter SDK or kit de desenvolvimento de software.

| Ferramenta                                                   | Versão mínima suportada   |
| :----------------------------------------------------------- | :------------------------ |
| Dart                                                         | 2.17.0+                   |
| Flutter (integração via CocoaPods)                           | 1.10.0+                   |
| Flutter (integração via CocoaPods ou Swift Package Manager)  | 3.24.0+                   |
| iOS Deployment Target                                        | 12.0+                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suporte de versão" }

Este SDK or kit de desenvolvimento de software também herda os requisitos dos SDKs nativos da Braze subjacentes. Para saber mais, consulte [braze-inc/braze-android-SDK or kit de desenvolvimento de software](https://github.com/braze-inc/braze-android-sdk) e [braze-inc/braze-swift-SDK or kit de desenvolvimento de software](https://github.com/braze-inc/braze-swift-sdk).

## App de exemplo {#sample-app}

A pasta [`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) contém um app de exemplo que ilustra como integrar e usar as APIs deste pacote.

## Fale conosco {#contact}

Se você tiver dúvidas, entre em contato com o suporte técnico da Braze para obter assistência.
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk).