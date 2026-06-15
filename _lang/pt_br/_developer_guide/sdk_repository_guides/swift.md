---
nav_title: Swift SDK
article_title: Guia do repositório do Swift SDK
page_order: 3
description: "Referência do README do Braze Swift SDK espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Sobre o Braze Swift SDK {#about-the-braze-swift-sdk}

O Braze Swift SDK ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu aplicativo.

Para começar, consulte os seguintes recursos:

- [Guia do Usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)

## Início rápido {#quickstart}

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

Consulte o [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift) para opções avançadas de integração.

## Suporte de versão {#version-support}

Ferramenta | Versão mínima suportada
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

<!-- Table generated with https://www.tablesgenerator.com/markdown_tables -->

|                                                                                                                                                  | iOS |     tvOS      | macCatalyst |   visionOS    |
|--------------------------------------------------------------------------------------------------------------------------------------------------|:---:|:-------------:|:-----------:|:-------------:|
| **BrazeKit**<br/> _Biblioteca principal do SDK com suporte para [análise de dados] e [notificações por push]._                                   |  ✅  | ✅<sup>1</sup> |      ✅      |       ✅       |
| **BrazeUI**<br/> _Biblioteca de interface do usuário fornecida pela Braze para [In-App Messages] e [Content Cards]._                             |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazeLocation**<br/> _Biblioteca de localização com suporte para [análise de local e monitoramento de geofence]._                              |  ✅  | ✅<sup>2</sup> |      ✅      | ✅<sup>2</sup> |
| **BrazeNotificationService**<br/> _Biblioteca de extensão de serviço de notificação com suporte para [notificações por push avançadas]._         |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazePushStory**<br/> _Biblioteca de extensão de conteúdo de notificação com suporte para [Push Stories]._                                     |  ✅  |      n/a      |      ✅      |       ✅       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Bibliotecas" }

<sup>1</sup> _Notificações por push não são suportadas no tvOS_<br/>
<sup>2</sup> _Monitoramento de geofence não é suportado no tvOS e no visionOS_

[análise de dados]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/
[notificações por push]: https://www.braze.com/docs/user_guide/message_building_by_channel/push
[In-App Messages]: https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages
[Content Cards]: https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards
[análise de local e monitoramento de geofence]: https://www.braze.com/docs/user_guide/engagement_tools/locations_and_geofences
[notificações por push avançadas]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/ios/rich_notifications/
[Push Stories]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/

## Exemplos {#examples}

Explore nosso [projeto de exemplos](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples), que demonstra integrações de múltiplos recursos.

## Repositórios alternativos {#alternative-repositories}

| Variante                                     |                                     Repositório | Issues do GH, informações do SDK |
|----------------------------------------------|------------------------------------------------:|----------------------------------:|
| → **Fontes e XCFrameworks estáticos**        |                    [braze-inc/braze-swift-sdk] |                                 ✓ |
| XCFrameworks estáticos                       |    [braze-inc/braze-swift-sdk-prebuilt-static] |                                 ✗ |
| XCFrameworks dinâmicos                       |   [braze-inc/braze-swift-sdk-prebuilt-dynamic] |                                 ✗ |
| XCFrameworks combináveis (acesso antecipado) | [braze-inc/braze-swift-sdk-prebuilt-mergeable] |                                 ✗ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Repositórios alternativos" }

## Contato {#contact}

Se você tiver dúvidas, entre em contato pelo e-mail [support@braze.com](mailto:support@braze.com).

[braze-inc/braze-swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
[braze-inc/braze-swift-sdk-prebuilt-static]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-static
[braze-inc/braze-swift-sdk-prebuilt-dynamic]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic
[braze-inc/braze-swift-sdk-prebuilt-mergeable]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).