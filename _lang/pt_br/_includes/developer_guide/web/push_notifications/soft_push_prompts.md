{% multi_lang_include developer_guide/prerequisites/web.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

Se você estiver integrando a Braze por meio do kit incorporado da mParticle na web, consulte a [Etapa 3 na integração de eventos Web da Braze na mParticle](https://docs.mparticle.com/integrations/braze/event/#web) para obter instruções sobre como implementar prompts de soft push.

## Sobre prompts de soft push {#about-soft-push-prompts}

Geralmente é uma boa ideia implementar um prompt de push "suave" no seu site, no qual você prepara o usuário e apresenta seus argumentos para o envio de notificações por push antes de solicitar a permissão de push. Isso é útil porque o navegador limita a frequência com que você pode solicitar permissão diretamente ao usuário e, se o usuário negar a permissão, você não poderá perguntar novamente.

Como alternativa, se você quiser incluir um tratamento personalizado especial, em vez de chamar `requestPushPermission()` diretamente, conforme descrito na [integração padrão de web push]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-2-browser-registration), use nossas [mensagens no app disparadas]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).

{% alert tip %}
Isso pode ser feito sem personalização do SDK usando nosso novo [push primer sem código]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).
{% endalert %}

## Configurando prompts de soft push {#setting-up-soft-push-prompts}

{% multi_lang_include archive/web-v4-rename.md %}

### Etapa 1: Criar uma campanha de push primer {#step-1-create-a-push-primer-campaign}

Primeiro, você deve criar uma campanha de mensagens no app "Prime for Push" no dashboard da Braze:

1. Crie uma mensagem no app **Modal** com o texto e o estilo que desejar.
2. Em seguida, defina o comportamento ao clicar como **Fechar mensagem**. Esse comportamento será personalizado posteriormente.
3. Adicione um par chave-valor à mensagem em que a chave é `msg-id` e o valor é `push-primer`.
4. Atribua uma ação-gatilho de evento personalizado (como "prime-for-push") à mensagem. Você pode criar o evento personalizado manualmente pelo dashboard, se necessário.

### Etapa 2: Remover chamadas {#step-2-remove-calls}

Na sua integração SDK da Braze, encontre e remova todas as chamadas para `automaticallyShowInAppMessages()` do seu snippet de carregamento.

### Etapa 3: Atualizar a integração {#step-3-update-integration}

Por fim, substitua a chamada removida pelo snippet a seguir. Chame `subscribeToInAppMessage()` antes de chamar `openSession()`. Isso garante que o listener de mensagens no app seja registrado a tempo de receber a mensagem de push primer.

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

Quando quiser exibir o prompt de soft push para o usuário, chame `braze.logCustomEvent` com o nome de evento que dispara essa mensagem no app.