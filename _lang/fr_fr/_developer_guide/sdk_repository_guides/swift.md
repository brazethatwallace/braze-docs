---
nav_title: Swift SDK
article_title: Guide du dépôt Swift SDK
page_order: 3
description: "Référence du README du SDK Braze Swift, miroir depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guide du dépôt Swift SDK {#swift-sdk-repository-guide}

## À propos du SDK Braze Swift {#about-the-braze-swift-sdk}

Le SDK Braze Swift vous aide à intégrer les fonctionnalités de communication, d'analyse et d'engagement utilisateur de Braze dans votre application.

Pour commencer, consultez les ressources suivantes :

- [Guide de l'utilisateur Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guide du développeur Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)

## Démarrage rapide {#quickstart}

Les extraits de code suivants montrent la configuration minimale requise pour ajouter le SDK Braze Swift à votre application.

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

Pour plus d'informations sur les options d'intégration avancées, consultez le [Guide du développeur Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift).

## Prise en charge des versions {#version-support}

Le tableau suivant répertorie les versions minimales prises en charge pour les outils utilisés par le SDK Braze Swift.

Outil | Version minimale prise en charge
:----|:----
iOS|12.0+
Mac Catalyst|16.0+
tvOS|12.0+
visionOS|1.0+
Xcode|26.0+ (17A324)

## Gestionnaires de paquets {#package-managers}
- Gestionnaire de paquets Swift
- CocoaPods

## Bibliothèques {#libraries}

Le tableau suivant décrit chaque bibliothèque du SDK Braze Swift.

<!-- Table generated with https://www.tablesgenerator.com/markdown_tables -->

|                                                                                                                                          | iOS |     tvOS      | macCatalyst |   visionOS    |
|------------------------------------------------------------------------------------------------------------------------------------------|:---:|:-------------:|:-----------:|:-------------:|
| **BrazeKit**<br/> _Bibliothèque principale du SDK fournissant la prise en charge de l'[analyse] et des [notifications push]._           |  ✅  | ✅<sup>1</sup> |      ✅      |       ✅       |
| **BrazeUI**<br/> _Bibliothèque d'interface utilisateur fournie par Braze pour les [In-App Messages] et les [Content Cards]._            |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazeLocation**<br/> _Bibliothèque de localisation fournissant la prise en charge de l'[analyse de localisation et du géorepérage]._  |  ✅  | ✅<sup>2</sup> |      ✅      | ✅<sup>2</sup> |
| **BrazeNotificationService**<br/> _Bibliothèque d'extension de service de notification fournissant la prise en charge des [notifications push riches]._ |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazePushStory**<br/> _Bibliothèque d'extension de contenu de notification fournissant la prise en charge des [Push Stories]._        |  ✅  |      n/a      |      ✅      |       ✅       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Bibliothèques" }

<sup>1</sup> _Notifications push non prises en charge sur tvOS_<br/>
<sup>2</sup> _Surveillance du géorepérage non prise en charge sur tvOS et visionOS_

[analyse]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/
[notifications push]: https://www.braze.com/docs/user_guide/message_building_by_channel/push
[In-App Messages]: https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages
[Content Cards]: https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards
[analyse de localisation et du géorepérage]: https://www.braze.com/docs/user_guide/engagement_tools/locations_and_geofences
[notifications push riches]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/ios/rich_notifications/
[Push Stories]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/

## Exemples {#examples}

Explorez notre [projet d'exemples](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples), qui présente des exemples d'intégrations pour plusieurs fonctionnalités.

## Dépôts alternatifs {#alternative-repositories}

| Variante                              |                                        Dépôt | Tickets GH, infos SDK |
|---------------------------------------|-----------------------------------------------:|--------------------:|
| → **Sources et XCFrameworks statiques** |                    [braze-inc/braze-swift-sdk] |                   ✓ |
| XCFrameworks statiques                |    [braze-inc/braze-swift-sdk-prebuilt-static] |                   ✗ |
| XCFrameworks dynamiques               |   [braze-inc/braze-swift-sdk-prebuilt-dynamic] |                   ✗ |
| XCFrameworks fusionnables             | [braze-inc/braze-swift-sdk-prebuilt-mergeable] |                   ✗ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dépôts alternatifs" }

## Contact {#contact}

Pour toute question, contactez le support technique de Braze pour obtenir de l'aide.

[braze-inc/braze-swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
[braze-inc/braze-swift-sdk-prebuilt-static]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-static
[braze-inc/braze-swift-sdk-prebuilt-dynamic]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic
[braze-inc/braze-swift-sdk-prebuilt-mergeable]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les exemples de projets, consultez [https://github.com/braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).