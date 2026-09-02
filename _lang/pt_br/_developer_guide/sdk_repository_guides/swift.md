---
nav_title: Swift SDK or kit de desenvolvimento de software
article_title: Guia do repositório do Swift SDK or kit de desenvolvimento de software
page_order: 3
description: "Referência do README do Braze Swift SDK or kit de desenvolvimento de software espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do Swift SDK or kit de desenvolvimento de software {#swift-sdk-repository-guide}

## Sobre o Braze Swift SDK or kit de desenvolvimento de software {#about-the-braze-swift-sdk}

O Braze Swift SDK or kit de desenvolvimento de software ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu aplicativo.

Para começar, consulte os seguintes recursos:

- [Guia do Usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)

## Início rápido {#quickstart}

Os snippets a seguir mostram a configuração mínima necessária para adicionar o Braze Swift SDK or kit de desenvolvimento de software ao seu app.

``` swift
// AppDelegate.swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  // ...
  static var braze: Braze? = nil

  // ...
   func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // ...
        let configuration = Braze.Configuration(
            apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
            endpoint: "YOUR-BRAZE-ENDPOINT"
        )
        let braze = Braze(configuration: configuration)

        AppDelegate.braze = braze
        // ...
    }
}
```

``` swift
AppDelegate.braze?.changeUser(userId: "Jane Doe")
```

Para saber mais sobre opções avançadas de integração, consulte o [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift).

## Suporte a versões {#version-support}

A tabela a seguir lista as versões mínimas compatíveis com as ferramentas usadas pelo SDK or kit de desenvolvimento de software Swift da Braze.

Ferramenta | Versão mínima compatível
:----|:----
iOS|12.0+
Mac Catalyst|16.0+
tvOS|12.0+
visionOS|1.0+
Xcode|26.0+ (17A324)

## Gerenciadores de pacotes {#package-managers}
- Swift Package Manager
- CocoaPods

## Bibliotecas {#libraries}

A tabela a seguir descreve cada biblioteca no Braze Swift SDK or kit de desenvolvimento de software.

<!-- Table generated with https://www.tablesgenerator.com/markdown_tables -->

|                                                                                                                                          | iOS |     tvOS      | macCatalyst |   visionOS    |
|------------------------------------------------------------------------------------------------------------------------------------------|:---:|:-------------:|:-----------:|:-------------:|
| **BrazeKit**<br/> _Biblioteca principal do SDK or kit de desenvolvimento de software com suporte para [análise de dados] e [notificações por push]._                           |  ✅  | ✅<sup>1</sup> |      ✅      |       ✅       |
| **BrazeUI**<br/> _Biblioteca de interface do usuário fornecida pela Braze para [In-App Messages] e [Content Cards]._                     |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazeLocation**<br/> _Biblioteca de localização com suporte para [análise de dados de local e monitoramento de geofence]._             |  ✅  | ✅<sup>2</sup> |      ✅      | ✅<sup>2</sup> |
| **BrazeNotificationService**<br/> _Biblioteca de extensão de serviço de notificação com suporte para [notificações por push avançadas]._ |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazePushStory**<br/> _Biblioteca de extensão de conteúdo de notificação com suporte para [Push Stories]._                             |  ✅  |      n/a      |      ✅      |       ✅       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Bibliotecas" }

<sup>1</sup> _Notificações por push não são compatíveis com tvOS_<br/>
<sup>2</sup> _Monitoramento de geofence não é compatível com tvOS e visionOS_

[análise de dados]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/
[notificações por push]: https://www.braze.com/docs/user_guide/message_building_by_channel/push
[In-App Messages]: https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages
[Content Cards]: https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards
[análise de dados de local e monitoramento de geofence]: https://www.braze.com/docs/user_guide/engagement_tools/locations_and_geofences
[notificações por push avançadas]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/ios/rich_notifications/
[Push Stories]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/

## Exemplos {#examples}

Explore nosso [projeto de exemplos](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples), que apresenta integrações de exemplo para vários recursos.

## Repositórios alternativos {#alternative-repositories}

| Variante                              |                                    Repositório | Issues no GH, info do SDK or kit de desenvolvimento de software |
|---------------------------------------|-----------------------------------------------:|--------------------------:|
| → **Sources and Static XCFrameworks** |                    [braze-inc/braze-swift-SDK or kit de desenvolvimento de software] |                         ✓ |
| Static XCFrameworks                   |    [braze-inc/braze-swift-SDK or kit de desenvolvimento de software-prebuilt-static] |                         ✗ |
| Dynamic XCFrameworks                  |   [braze-inc/braze-swift-SDK or kit de desenvolvimento de software-prebuilt-dynamic] |                         ✗ |
| Mergeable XCFrameworks                | [braze-inc/braze-swift-SDK or kit de desenvolvimento de software-prebuilt-mergeable] |                         ✗ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Repositórios alternativos" }

## Contato {#contact}

Para dúvidas, entre em contato com o suporte técnico da Braze para obter assistência.

[braze-inc/braze-swift-SDK or kit de desenvolvimento de software]: https://github.com/braze-inc/braze-swift-sdk
[braze-inc/braze-swift-SDK or kit de desenvolvimento de software-prebuilt-static]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-static
[braze-inc/braze-swift-SDK or kit de desenvolvimento de software-prebuilt-dynamic]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic
[braze-inc/braze-swift-SDK or kit de desenvolvimento de software-prebuilt-mergeable]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).