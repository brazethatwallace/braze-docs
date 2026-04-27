{% multi_lang_include developer_guide/prerequisites/web.md %}

## Gatilhos de mensagem {#message-triggers}

## Tipos de disparo {#trigger-types}

As mensagens no app são acionadas automaticamente quando o SDK registra um dos seguintes tipos de evento personalizado: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` e `Push Click`. Observe que os gatilhos `Specific Purchase` e `Custom Event` também contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app não podem ser acionadas pela API ou por eventos da API&#8212;apenas por eventos personalizados registrados pelo SDK. Para saber mais sobre registro, consulte [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Semântica de entrega {#delivery-semantics}

Todas as mensagens no app elegíveis são entregues ao dispositivo do usuário no início da sessão. Quando entregues, o SDK faz o pré-carregamento dos ativos para que estejam disponíveis no momento do acionamento, minimizando a latência de exibição. Se o evento de gatilho tiver mais de uma mensagem no app elegível, apenas a mensagem com a maior prioridade será entregue.

Para saber mais sobre a semântica de início de sessão do SDK, consulte [Ciclo de vida da sessão]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/).

### Limite de taxa {#rate-limits}

Por padrão, o SDK limita o disparo de mensagens no app a uma vez a cada 30 segundos.

Para apps em produção, não defina esse valor abaixo de 10 segundos, para que os usuários não sejam sobrecarregados com mensagens no app consecutivas. Para testes e fluxos de apps de exemplo, 5 segundos é uma configuração comum.

Você pode definir esse intervalo como `0` para testes. No entanto, um intervalo de `0` segundos não força a exibição de várias mensagens no app ao mesmo tempo. Se outra mensagem no app modal ou em tela cheia já estiver visível, `braze.showInAppMessage` retornará `false` e a nova mensagem não será exibida.

Para substituir esse valor, adicione a seguinte propriedade à sua configuração da Braze&#8212;antes que a instância da Braze seja inicializada. Você pode definir qualquer número inteiro não negativo, que representa o intervalo mínimo de tempo em segundos. Por exemplo:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Pares de chave-valor {#key-value-pairs}

Ao criar uma campanha na Braze, você pode definir pares de chave-valor como `extras`, que o objeto de mensagem no app pode usar para enviar dados ao seu app. Por exemplo:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

## Desativando gatilhos automáticos {#disabling-automatic-triggers}

Para evitar que mensagens no app sejam acionadas automaticamente:

Remova a chamada para `braze.automaticallyShowInAppMessages()` do seu snippet de carregamento e crie uma lógica personalizada para controlar a exibição ou não das mensagens no app.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message

  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }

  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Se você não remover `braze.automaticallyShowInAppMessages()` do seu site e depois chamar `braze.showInAppMessage`, a mensagem poderá ser exibida várias vezes.
{% endalert %}

O parâmetro `inAppMessage` será uma subclasse de [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) ou um objeto [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html), cada um com diversos métodos de inscrição em eventos de ciclo de vida. Consulte a [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para a documentação completa.

Apenas uma mensagem no app [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) ou [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) pode ser exibida por vez. Se você tentar exibir uma segunda mensagem modal ou em tela cheia enquanto outra já estiver sendo exibida, `braze.showInAppMessage` retornará false e a segunda mensagem não será exibida.

## Acionando mensagens manualmente {#manually-triggering-messages}

### Exibindo uma mensagem em tempo real {#displaying-a-message-in-real-time}

As mensagens no app também podem ser criadas dentro do seu site e exibidas localmente em tempo real. Todas as opções de personalização disponíveis no dashboard também estão disponíveis localmente. Isso é particularmente útil para exibir mensagens que você deseja disparar no app em tempo real. No entanto, a análise de dados dessas mensagens criadas localmente não estará disponível no dashboard da Braze.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Acionando mensagens de intenção de saída {#triggering-exit-intent-messages}

Mensagens de intenção de saída são mensagens no app não intrusivas usadas para comunicar informações importantes aos visitantes antes que eles saiam do seu site.

Para configurar gatilhos para esses tipos de mensagem, implemente uma biblioteca de intenção de saída no seu site (como a [biblioteca de código aberto do ouibounce](https://github.com/carlsednaoui/ouibounce)) e use o código a seguir para registrar `'exit intent'` como um evento personalizado na Braze. Assim, suas futuras campanhas de mensagens no app poderão usar esse tipo de mensagem como um gatilho de evento personalizado.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
