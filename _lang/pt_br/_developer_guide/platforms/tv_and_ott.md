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

A tabela a seguir resume o suporte dos canais de envio de mensagens para as plataformas comuns de TV e OTT. Todas as plataformas também oferecem suporte a dados e análise de dados, Canvas e Feature Flags. Para o Kindle Fire, siga as mesmas orientações do Amazon Fire TV. Para o Apple Vision Pro, consulte o [suporte ao visionOS]({{site.baseurl}}/developer_guide/platforms/swift/visionos).

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
            <th>In-App Messages</th>
            <th>Content Cards</th>
            <th>Notificações por push</th>
            <th>Banners</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td><a href="https://github.com/braze-inc/braze-vega-sdk">Vega SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatível</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatível</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatível</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td><a href="https://github.com/braze-inc/braze-android-sdk">Android SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatível</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatível</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatível</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Sem suporte da plataforma OTT</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Sem suporte da plataforma OTT</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td><a href="https://github.com/braze-inc/braze-roku-sdk">Roku SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Sem suporte da Braze</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">Sem suporte da plataforma OTT</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Sem suporte da Braze</span></td>
        </tr>
        <tr>
            <td>Apple TV OS (tvOS)</td>
            <td><a href="https://github.com/braze-inc/braze-swift-sdk">Swift SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Sem suporte da Braze</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Somente headless</span></td>
        </tr>
    </tbody>
</table>

- <span aria-hidden="true">✅</span> = Compatível
- <span aria-hidden="true">🔧</span> = Somente headless (você precisará criar uma interface personalizada)
- <span aria-hidden="true">➖</span> = Sem suporte da plataforma OTT
- <span aria-hidden="true">❌</span> = Sem suporte da Braze

## Guias de integração {#integration-guides}

### Amazon Fire TV {#fire-tv}

Use o SDK Braze Fire OS para integração com dispositivos Amazon Fire TV.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Notificações por push (conhecidas como ["Heads Up Notifications"](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - A prioridade deve ser definida como "HIGH" para que elas apareçam. Todas as notificações aparecem no menu de configurações do Fire TV.
- Content Cards
- Feature Flags
- Mensagens no app
  - Para exibir mensagens HTML em ambientes não sensíveis ao toque, como TVs, defina `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` como `false` (disponível a partir do [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app Fire TV.

Para saber mais, consulte o [guia de integração Fire OS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Kindle Fire {#kindle-fire}

Use o SDK Braze Fire OS para integração com dispositivos Amazon Kindle Fire.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Notificações por push
- Content Cards
- Feature Flags
- Mensagens no app
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu Kindle Fire.

Para saber mais, consulte o [guia de integração Fire OS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Android TV {#android-tv}

Use o SDK Braze Android para integração com dispositivos Android TV.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Content Cards
- Feature Flags
- Mensagens no app
  - Para exibir mensagens HTML em ambientes não sensíveis ao toque, como TVs, defina `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` como `false` (disponível a partir do [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- &#42; Notificações por push (integração manual necessária)
  - As notificações por push não são compatíveis nativamente com o Android TV. Para saber o motivo, consulte as [diretrizes de design](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) do Google. No entanto, é possível **fazer uma integração manual da interface de notificação por push para alcançar isso**. Consulte nossa [documentação]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android%20tv) sobre como configurar isso.
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app Android TV.

Para saber mais, consulte o [guia de integração do SDK Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

{% alert note %}
Certifique-se de criar um novo app Android no dashboard para a sua integração Android OTT.
{% endalert %}

### LG webOS {#lg-webos}

Use o SDK Braze Web para integração com [TVs LG webOS](https://webostv.developer.lge.com/discover).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Content Cards (via [interface headless](#custom-ui))
- Feature Flags
- Mensagens no app (via [interface headless](#custom-ui))
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app webOS.

Para saber mais, consulte o [guia de integração Web Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Samsung Tizen {#tizen}

Use o SDK Braze Web para integração com [TVs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Content Cards (via [interface headless](#custom-ui))
- Feature Flags
- Mensagens no app (via [interface headless](#custom-ui))
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app Tizen.

Para saber mais, consulte o [guia de integração Web Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Roku {#roku}

Use o Roku SDK da Braze para integração com [TVs Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Mensagens no app (via [interface headless](#custom-ui))
  - As webviews não são compatíveis com a plataforma Roku, portanto, mensagens HTML no app não são compatíveis.
- Feature Flags

Para saber mais, consulte o [guia de integração Roku]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=roku).

### Apple TV OS {#tvos}

Use o SDK Braze Swift para integração com tvOS. Tenha em mente que o SDK Swift não inclui nenhuma interface ou visualização padrão para tvOS, então você precisará implementar a sua própria.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento entre canais
- Content Cards (via [interface headless](#custom-ui))
- Feature Flags
- Mensagens no app (via [interface headless](#custom-ui))
  - As webviews não são compatíveis com a plataforma tvOS, portanto, mensagens HTML no app não são compatíveis.
  - Veja nosso [app de exemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) para saber mais sobre como usar uma interface headless para mensagens personalizadas no tvOS.
- Notificações por push silenciosas e atualização de badges
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app tvOS.

Para saber mais, consulte o [guia de integração do SDK iOS Swift](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Para evitar que mensagens no app para dispositivos móveis sejam exibidas para os usuários da sua TV, configure o [direcionamento por app](#app-targeting) ou use pares de chave-valor para filtrar mensagens. Por exemplo, exibindo mensagens do tvOS apenas se elas contiverem um par de chave-valor especial `tv = true`.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Use o SDK Braze Swift para integração com visionOS. A maioria dos recursos disponíveis no iOS também está disponível no visionOS, incluindo:

- Análise de dados (sessões, eventos personalizados, compras, etc.)
- In-App Messages (modelos de dados e interface)
- Content Cards (modelos de dados e interface)
- Notificações por push (visíveis para o usuário com botões de ação e notificações silenciosas)
- Feature Flags
- Análise de localização
- Banners
  - Use [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements) para incorporar mensagens diretamente no seu app visionOS.

Para saber mais, consulte o [guia de integração do SDK iOS Swift](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Alguns recursos do iOS são parcialmente compatíveis ou não são compatíveis. Para a lista completa, consulte [compatibilidade com visionOS]({{site.baseurl}}/developer_guide/platforms/swift/visionos).
{% endalert %}

## Direcionamento de apps {#app-targeting}

Para direcionar apps OTT para envio de mensagens, recomendamos criar um Segment específico para o seu app OTT.

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