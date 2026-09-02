---
nav_title: Suporte para smart TV
article_title: Suporte para smart TV para o SDK or kit de desenvolvimento de software Web da Braze
platform: Web
page_order: 30
description: "Este artigo aborda como usar o SDK or kit de desenvolvimento de software da Braze para Web para integrar com smart TVs (Samsung e LG)."

---

# Suporte para smart TV {#smart-tv-support}

> O SDK or kit de desenvolvimento de software da Braze para Web permite que você colete análises de dados e exiba mensagens rich no app e mensagens de Content Cards para usuários de smart TV, incluindo [TVs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) e [TVs LG (webOS)](https://webostv.developer.lge.com/discover). Este artigo aborda como usar o SDK or kit de desenvolvimento de software da Braze para Web para integrar com smart TVs.

{% alert tip %}
Para uma referência técnica completa, confira nossa [Documentação JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) ou nossos [apps de exemplo](https://github.com/Appboy/smart-tv-sample-apps) para ver o Web SDK or kit de desenvolvimento de software rodando em uma TV.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Configurando o SDK or kit de desenvolvimento de software Web da Braze {#configuring-the-web-braze-sdk}

Existem duas mudanças necessárias ao integrar com smart TVs:

1. Ao baixar ou importar o Web SDK or kit de desenvolvimento de software, use o pacote "core" (disponível em `https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js`, onde `x.y` é a versão desejada). Recomendamos usar a versão CDN do nosso Web SDK or kit de desenvolvimento de software, já que a versão NPM é escrita em módulos ES nativos, enquanto a versão CDN é transpilada para ES5. Se você preferir usar a [versão NPM](https://www.npmjs.com/package/@braze/web-sdk), certifique-se de usar um empacotador como o webpack que removerá o código não utilizado e de que o código seja transpilado para ES5.
2. Ao inicializar o Web SDK or kit de desenvolvimento de software, você precisa definir as opções de inicialização `disablePushTokenMaintenance` e `manageServiceWorkerExternally` para `true`.

## Análise de dados {#analytics}

Todos os mesmos métodos do Web SDK or kit de desenvolvimento de software para análise de dados podem ser usados em smart TVs. Para um guia completo sobre rastreamento de eventos personalizados, atributos personalizados e mais, veja [Análise de dados]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).

## Mensagens no app e Content Cards {#in-app-messages-and-content-cards}

O SDK or kit de desenvolvimento de software da Braze para Web aceita tanto [mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=web) quanto [Content Cards]({{site.baseurl}}/developer_guide/content_cards?sdktab=web) em smart TVs. Note que você deve usar o [Web SDK or kit de desenvolvimento de software "Core"](https://www.npmjs.com/package/@braze/web-sdk), pois a renderização de mensagens no app e Content Cards não é suportada usando nossa exibição padrão de UI e deve ser personalizada pelo seu app para se adequar à experiência do seu app de TV.

Para saber mais sobre como seu app de smart TV pode receber e exibir mensagens no app, veja [Disparando mensagens]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web).