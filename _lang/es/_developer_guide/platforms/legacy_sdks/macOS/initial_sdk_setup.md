---
nav_title: Configuración inicial del SDK or kit de desarrollo de software
article_title: Configuración inicial del SDK or kit de desarrollo de software para MacOS
platform: MacOS
page_order: 0
page_type: reference
description: "En este artículo de referencia se proporcionan recursos para la integración inicial del SDK or kit de desarrollo de software de Braze en macOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración inicial del SDK or kit de desarrollo de software {#initial-sdk-setup}

> En este artículo de referencia se explica cómo instalar el SDK or kit de desarrollo de software de Braze para MacOS.

A partir de la versión [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0), el SDK or kit de desarrollo de software de Braze es compatible con macOS para aplicaciones que utilicen [Mac Catalyst](https://developer.apple.com/mac-catalyst/) al integrarse a través de Swift Package Administrador. Actualmente, el SDK or kit de desarrollo de software no es compatible con Mac Catalyst cuando se utilizan CocoaPods o Carthage.

{% alert note %}
Para crear tu aplicación con Mac Catalyst, consulta <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">la documentación de Apple</a>.
{% endalert %}

Una vez que tu aplicación sea compatible con Catalyst, sigue [estas instrucciones para utilizar Swift Package Administrador]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=swift%20package%20manager/) para importar el SDK or kit de desarrollo de software de Braze a tu aplicación.

## Características compatibles {#supported-features}

Braze es compatible con [notificaciones push]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Content Cards]({{site.baseurl}}/developer_guide/content_cards?sdktab=swift), [mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift) y [recopilación automática de ubicación]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift) cuando se ejecuta en Mac Catalyst.

Ten en cuenta que Push Stories, las notificaciones push enriquecidas y las geovallas no son compatibles en macOS.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/