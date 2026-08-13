---
nav_title: TV e OTT
article_title: Integrações de TV e OTT para a Braze
page_order: 15

description: "Este artigo detalha os recursos de TV e OTT da Braze, integrações, plataformas disponíveis e outras funcionalidades."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# Integrações de TV e OTT {#tv-and-ott-integrations}

> À medida que a tecnologia evolui para novas plataformas e dispositivos, o seu envio de mensagens também pode evoluir com a Braze! A Braze oferece diferentes canais de engajamento para vários sistemas operacionais de TV e métodos de entrega de conteúdo Over-the-Top (OTT).

## Plataformas e recursos {#platforms-and-features}

A tabela a seguir resume o suporte a canais de envio de mensagens para plataformas comuns de TV e OTT. Todas as plataformas também suportam dados e análise de dados, Canvas e Feature Flags. Para o Kindle Fire, use as mesmas orientações do Amazon Fire TV. Para o Apple Vision Pro, consulte o [suporte ao visionOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/visionos).

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center;
    vertical-align: middle;
    word-break: normal;
    overflow-wrap: normal;
    hyphens: none;
}

#tv-feature-table td:first-child,
#tv-feature-table th:first-child {
    text-align: left;
}

</style>
<table aria-label="Suporte a canais de envio de mensagens para TV e OTT" id="tv-feature-table">
  <caption>Suporte a canais de envio de mensagens para TV e OTT</caption>
    <thead>
        <tr>
            <th>Tipo de dispositivo</th>
            <th>SDK</th>
            <th>Mensagens no app</th>
            <th>Content Cards</th>
            <th>Notificações por push</th>
            <th>Banners</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td><a href="https://github.com/braze-inc/braze-vega-sdk">Vega SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Suportado</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Suportado</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Suportado</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td><a href="https://github.com/braze-inc/braze-android-sdk">Android SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Suportado</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Suportado</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Suportado</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Não suportado pela plataforma OTT</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Não suportado pela plataforma OTT</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td><a href="https://github.com/braze-inc/braze-roku-sdk">Roku SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Não suportado pela Braze</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Não suportado pela plataforma OTT</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Não suportado pela Braze</span></td>
        </tr>
        <tr>
            <td>Apple TV OS (tvOS)</td>
            <td><a href="https://github.com/braze-inc/braze-swift-sdk">Swift SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Não suportado pela Braze</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Apenas headless</span></td>
        </tr>
    </tbody>
</table>

- <span aria-hidden="true">✅</span> = Suportado
- <span aria-hidden="true">🔧</span> = Apenas headless (você precisará criar uma interface personalizada)
- <span aria-hidden="true">➖</span> = Não suportado pela plataforma OTT
- <span aria-hidden="true">❌</span> = Não suportado pela Braze

## Guias de integração {#integration-guides}

### Amazon Fire TV {#fire-tv}

Use o SDK Braze Fire OS para integrar com dispositivos Amazon Fire TV.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Notificações por push (conhecidas como ["Heads Up Notifications"](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - A prioridade deve ser definida como "HIGH" para que elas apareçam. Todas as notificações aparecem no menu de configurações do Fire TV.
- Content Cards
- Feature Flags
- Mensagens no app
  - Para exibir mensagens HTML em ambientes sem toque, como TVs, defina `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` como `false` (disponível a partir do [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app Fire TV.

Para saber mais, visite o [guia de integração do Fire OS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Kindle Fire {#kindle-fire}

Use o SDK Braze Fire OS para integrar com dispositivos Amazon Kindle Fire.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Notificações por push
- Content Cards
- Feature Flags
- Mensagens no app
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu Kindle Fire.

Para saber mais, visite o [guia de integração do Fire OS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Android TV {#android-tv}

Use o SDK Braze Android para integrar com dispositivos Android TV.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Content Cards
- Feature Flags
- Mensagens no app
  - Para exibir mensagens HTML em ambientes sem toque, como TVs, defina `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` como `false` (disponível a partir do [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- &#42; Notificações por push (integração manual necessária)
  - Notificações por push não são suportadas nativamente no Android TV. Para saber o motivo, consulte as [Diretrizes de design](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) do Google. No entanto, você pode **fazer uma integração manual da interface de notificação por push para conseguir isso**. Consulte nossa [documentação]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android%20tv) sobre como configurar isso.
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app Android TV.

Para saber mais, visite o [guia de integração do SDK Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

{% alert note %}
Crie um novo app Android no dashboard para a sua integração Android OTT.
{% endalert %}

### LG webOS {#lg-webos}

Use o SDK Braze Web para integrar com [TVs LG webOS](https://webostv.developer.lge.com/discover).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- Mensagens no app (via [Headless UI](#custom-ui))
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app webOS.

Para saber mais, visite o [guia de integração da Web Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Samsung Tizen {#tizen}

Use o SDK Braze Web para integrar com as [TVs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- Mensagens no app (via [Headless UI](#custom-ui))
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app Tizen.

Para saber mais, visite o [guia de integração da Web Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Roku {#roku}

Use o SDK Braze Roku para integrar com [TVs Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Mensagens no app (via [Headless UI](#custom-ui))
  - A plataforma Roku não é compatível com webviews, portanto mensagens HTML no app não são suportadas.
- Feature Flags

Para saber mais, acesse o [guia de integração do Roku]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=roku).

### Apple TV OS {#tvos}

Use o SDK Braze Swift para integrar com o tvOS. Lembre-se de que o SDK Swift não inclui nenhuma interface ou visualização padrão para tvOS, então você precisará implementar a sua própria.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- Mensagens no app (via [Headless UI](#custom-ui))
  - A plataforma tvOS não é compatível com webviews, portanto mensagens HTML no app não são suportadas.
  - Veja nosso [app de exemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) para saber mais sobre como usar uma Headless UI para envio de mensagens personalizadas no tvOS.
- Notificações por push silenciosas e atualização de badging
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app tvOS.

Para saber mais, acesse o [guia de integração do SDK Swift para iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Para evitar exibir mensagens no app para dispositivos móveis aos seus usuários de TV, configure o [direcionamento de app](#app-targeting) ou use pares de chave-valor para filtrar mensagens. Por exemplo, exiba mensagens do tvOS apenas se elas contiverem um par de chave-valor especial `tv = true`.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Use o SDK Braze Swift para integrar com o visionOS. A maioria dos recursos disponíveis no iOS também está disponível no visionOS, incluindo:

- Análise de dados (sessões, eventos personalizados, compras, etc.)
- Mensagens no app (modelos de dados e UI)
- Content Cards (modelos de dados e UI)
- Notificações por push (visíveis ao usuário com botões de ação e notificações silenciosas)
- Feature Flags
- Análise de dados de localização
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app visionOS.

Para saber mais, acesse o [guia de integração do SDK Swift para iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Alguns recursos do iOS são parcialmente compatíveis ou incompatíveis. Para a lista completa, consulte o [suporte ao visionOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/visionos).
{% endalert %}

## Direcionamento de apps {#app-targeting}

Para direcionar apps OTT para envio de mensagens, recomendamos criar um segmento específico para o seu app OTT.

![Um segmento criado usando o app Android OTT.]({% image_buster /assets/img/android_ott.png %})

## Headless UI {#custom-ui}

{% alert important %}
Plataformas que suportam mensagens no app ou Content Cards por meio de Headless UI **não** incluem nenhuma interface ou visualização padrão. Crie sua própria interface personalizada (como para mensagens no app) e use os modelos de dados fornecidos pelo SDK para preencher essas interfaces.
{% endalert %}

Com a Headless UI, a Braze fornecerá um modelo de dados, como JSON, que seu app pode ler e usar dentro de uma interface controlada pelo seu app. Esses dados conterão os campos configurados no dashboard (título, corpo, texto do botão, cores, etc.) que seu app pode ler e exibir de acordo. Para saber mais sobre o tratamento personalizado de mensagens, consulte:

**Android SDK**
- [Personalização de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android#android_setting-custom-manager-listeners)
- [Personalização de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)

**Swift SDK**
- [Personalização de mensagens no app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [App de exemplo de Headless UI](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Personalização de Content Cards](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**SDK Web**
- [Personalização de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web)
- [Personalização de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)