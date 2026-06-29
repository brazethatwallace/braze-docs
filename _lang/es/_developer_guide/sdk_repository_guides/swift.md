---
nav_title: Swift SDK
article_title: Guía del repositorio del Swift SDK
page_order: 3
description: "Referencia del README del SDK Swift de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Acerca del SDK Swift de Braze {#about-the-braze-swift-sdk}

El SDK Swift de Braze te ayuda a integrar las capacidades de mensajería, análisis e interacción con los usuarios de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze]({{site.baseurl}}/user_guide/introduction)
- [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift)

## Inicio rápido {#quickstart}

Los siguientes fragmentos de código muestran la configuración mínima necesaria para añadir el SDK Swift de Braze a tu aplicación.

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

Para obtener más información sobre las opciones de integración avanzadas, consulta la [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift).

## Compatibilidad de versiones {#version-support}

La siguiente tabla enumera las versiones mínimas compatibles de las herramientas utilizadas por el SDK Swift de Braze.

Herramienta | Versión mínima compatible
:----|:----
iOS|12.0+
Mac Catalyst|16.0+
tvOS|12.0+
visionOS|1.0+
Xcode|26.0+ (17A324)

## Gestores de paquetes {#package-managers}
- Swift Package Manager
- CocoaPods

## Bibliotecas {#libraries}

La siguiente tabla describe cada biblioteca del SDK Swift de Braze.

<!-- Table generated with https://www.tablesgenerator.com/markdown_tables -->

|                                                                                                                                                    | iOS |     tvOS      | macCatalyst |   visionOS    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|:---:|:-------------:|:-----------:|:-------------:|
| **BrazeKit**<br/> _Biblioteca principal del SDK que proporciona soporte para [análisis] y [notificaciones push]._                                   |  ✅  | ✅<sup>1</sup> |      ✅      |       ✅       |
| **BrazeUI**<br/> _Biblioteca de interfaz de usuario proporcionada por Braze para [In-App Messages] y [Content Cards]._                              |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazeLocation**<br/> _Biblioteca de ubicación que proporciona soporte para [análisis de ubicación y monitoreo de geovallas]._                      |  ✅  | ✅<sup>2</sup> |      ✅      | ✅<sup>2</sup> |
| **BrazeNotificationService**<br/> _Biblioteca de extensión del servicio de notificaciones que proporciona soporte para [notificaciones push enriquecidas]._ |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazePushStory**<br/> _Biblioteca de extensión de contenido de notificaciones que proporciona soporte para [Push Stories]._                       |  ✅  |      n/a      |      ✅      |       ✅       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Bibliotecas" }

<sup>1</sup> _Las notificaciones push no son compatibles con tvOS_<br/>
<sup>2</sup> _El monitoreo de geovallas no es compatible con tvOS ni visionOS_

[análisis]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/
[notificaciones push]: {{site.baseurl}}/user_guide/message_building_by_channel/push
[In-App Messages]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages
[Content Cards]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards
[análisis de ubicación y monitoreo de geovallas]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences
[notificaciones push enriquecidas]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/
[Push Stories]: {{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/

## Ejemplos {#examples}

Explora nuestro [proyecto de ejemplos](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples), que muestra integraciones de múltiples características.

## Repositorios alternativos {#alternative-repositories}

| Variante                                     |                                     Repositorio | Issues de GH, info del SDK |
|----------------------------------------------|------------------------------------------------:|---------------------------:|
| → **Fuentes y XCFrameworks estáticos**       |                    [braze-inc/braze-swift-sdk] |                          ✓ |
| XCFrameworks estáticos                       |    [braze-inc/braze-swift-sdk-prebuilt-static] |                          ✗ |
| XCFrameworks dinámicos                       |   [braze-inc/braze-swift-sdk-prebuilt-dynamic] |                          ✗ |
| XCFrameworks combinables (acceso anticipado) | [braze-inc/braze-swift-sdk-prebuilt-mergeable] |                          ✗ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Repositorios alternativos" }

## Contacto {#contact}

Si tienes preguntas, ponte en contacto con [support@braze.com](mailto:support@braze.com).

[braze-inc/braze-swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
[braze-inc/braze-swift-sdk-prebuilt-static]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-static
[braze-inc/braze-swift-sdk-prebuilt-dynamic]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic
[braze-inc/braze-swift-sdk-prebuilt-mergeable]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable
<!-- END GENERATED README CONTENT -->

Para obtener detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).