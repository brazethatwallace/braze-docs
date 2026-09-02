---
nav_title: Configuração inicial do SDK or kit de desenvolvimento de software
article_title: Configuração inicial do SDK or kit de desenvolvimento de software para MacOS
platform: MacOS
page_order: 0
page_type: reference
description: "Este artigo de referência oferece recursos para a integração inicial do SDK or kit de desenvolvimento de software da Braze no macOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuração inicial do SDK or kit de desenvolvimento de software {#initial-sdk-setup}

> Este artigo de referência ensina como instalar o SDK or kit de desenvolvimento de software da Braze para macOS.

A partir da versão [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0), o SDK or kit de desenvolvimento de software da Braze é compatível com macOS para apps que usam [Mac Catalyst](https://developer.apple.com/mac-catalyst/) com integração pelo Swift Package Manager. No momento, o SDK or kit de desenvolvimento de software não é compatível com o Mac Catalyst ao usar CocoaPods ou Carthage.

{% alert note %}
Para criar seu app com o Mac Catalyst, consulte a <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">documentação da Apple</a>.
{% endalert %}

Depois que seu app for compatível com o Catalyst, siga [estas instruções para usar o Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=swift%20package%20manager/) para importar o SDK or kit de desenvolvimento de software da Braze para o seu app.

## Recursos suportados {#supported-features}

A Braze oferece suporte a [notificações por push]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Content Cards]({{site.baseurl}}/developer_guide/content_cards?sdktab=swift), [mensagens no app]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift) e [coleta automática de localização]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift) ao executar no Mac Catalyst.

Observe que Push Stories, notificações por push avançadas e geofences não são suportados no macOS.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/