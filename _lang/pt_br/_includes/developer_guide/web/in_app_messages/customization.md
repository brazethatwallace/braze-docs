{% multi_lang_include developer_guide/prerequisites/web.md %}

## Estilos personalizados {#custom-styles}

Os elementos da interface do usuário da Braze vêm com uma aparência padrão que cria uma experiência neutra de mensagens no app e visa à consistência com outras plataformas móveis da Braze. Os estilos padrão da Braze são definidos em CSS no SDK or kit de desenvolvimento de software da Braze.

### Definição de um estilo padrão {#setting-a-default-style}

Ao substituir estilos selecionados em seu aplicativo, você pode personalizar nossos tipos de mensagem no app padrão com suas próprias imagens de fundo, famílias de fontes, estilos, tamanhos, animações e muito mais.

Por exemplo, a seguir há uma substituição que fará com que os cabeçalhos de uma mensagem no app apareçam em itálico:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

Consulte os [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para saber mais.

### Personalização do z-index {#customizing-the-z-index}

Por padrão, as mensagens no app são exibidas usando `z-index: 9001`. Isso pode ser configurado usando a [opção de inicialização](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `inAppMessageZIndex `, caso seu site estilize elementos com valores mais altos do que esse.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Esse recurso está disponível apenas para o Web Braze SDK or kit de desenvolvimento de software v3.3.0 e posterior.
{% endalert %}

## Personalização do descarte de mensagens {#customizing-message-dismissals}

Por padrão, quando uma mensagem no app estiver sendo exibida, pressionar o botão de escape ou clicar no fundo acinzentado da página descartará a mensagem. Configure a [opção de inicialização](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` para `true` para evitar esse comportamento e exigir um clique explícito no botão para descartar as mensagens.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Personalização do tempo de exibição {#customizing-display-timing}

Para substituir o tempo de exibição padrão, remova as chamadas a `braze.automaticallyShowInAppMessages()` e manipule as mensagens em `braze.subscribeToInAppMessage()`. Registre seu retorno de chamada antes de `braze.openSession()`, para que você possa interceptar mensagens de início de sessão e decidir se deseja exibir ou adiar cada mensagem.

Por padrão, a Braze exibe mensagens no app quando elas são disparadas e estão elegíveis para exibição. Se você precisar de um comportamento diferente para a experiência do seu app, use um retorno de chamada personalizado para adiar ou exibir mensagens com base na sua própria lógica.

O exemplo a seguir mostra como se inscrever em mensagens no app disparadas, adiar mensagens selecionadas e exibir mensagens adiadas posteriormente:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT"
});

braze.subscribeToInAppMessage(function (message) {
    // Control-group messages should always be "shown" to log analytics.
    if (message.isControl || message instanceof braze.ControlMessage) {
        braze.showInAppMessage(message);
        return;
    }

    const shouldDefer = true; // Replace with your own display logic

    if (shouldDefer) {
        braze.deferInAppMessage(message);
        return;
    }

    braze.showInAppMessage(message);
});

braze.openSession();

// Later, when your app is ready to display a deferred message:
const deferredMessage = braze.getDeferredInAppMessage();
if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
}
```

Para orientações relacionadas à personalização de entrega, consulte:

- [Referência Web `deferInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)
- [Referência Web `subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)

## Abrir links em uma nova guia {#opening-links-in-a-new-tab}

Para configurar os links das mensagens no app para abrirem em uma nova guia, defina a opção `openInAppMessagesInNewTab` como `true` para forçar todos os links de cliques em mensagens no app a abrirem em uma nova guia ou janela.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
