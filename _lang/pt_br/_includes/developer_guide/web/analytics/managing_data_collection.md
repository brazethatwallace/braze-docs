## Desabilitando o rastreamento de dados {#disabling-data-tracking}

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab implementação padrão %}
Para desabilitar a atividade de rastreamento de dados no SDK para web, use o método [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). Isso sincronizará todos os dados registrados antes da chamada de `disableSDK()` e fará com que todas as chamadas subsequentes ao SDK da Braze para web nesta página e em carregamentos futuros sejam ignoradas.
{% endtab %}

{% tab Google Tag Manager %}
Use o tipo de tag **Disable Tracking** ou **Resume Tracking** para desabilitar ou reabilitar o rastreamento web, respectivamente. Essas duas opções chamam [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) e [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Práticas recomendadas {#best-practices}

Para oferecer aos usuários a opção de interromper o rastreamento, recomendamos criar uma página simples com dois links ou botões: um que chama `disableSDK()` ao ser clicado e outro que chama `enableSDK()` para permitir que os usuários optem por participar novamente. Você pode usar esses controles para iniciar ou interromper o rastreamento por meio de outros subprocessadores de dados também.

{% alert note %}
O SDK da Braze não precisa ser inicializado para chamar `disableSDK()`, o que permite desabilitar o rastreamento para usuários totalmente anônimos. Por outro lado, `enableSDK()` não inicializa o SDK da Braze, então você também precisa chamar `initialize()` em seguida para ativar o rastreamento.
{% endalert %}

## Retomando o rastreamento de dados {#resuming-data-tracking}

Para retomar a coleta de dados, você pode usar o método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

## Logout e cancelamento de registro de push {#logout-and-unregister-push}

O SDK da Braze fornece métodos para parar de direcionar um dispositivo quando um usuário cancela o registro de notificações por push ou faz logout. Esses métodos removem os dados de registro de push do usuário atual no servidor da Braze e no SDK, de modo que a Braze não envia mais Campaigns de notificação por push futuras para esse usuário.

### Logout {#logout}

Quando um usuário faz logout de um aplicativo, chame o método `logout` do SDK para remover o registro de push do dispositivo do usuário atual e executar automaticamente ações de limpeza no SDK. O método `logout` executa o seguinte:

- Cancela o registro do token por push do dispositivo do usuário atual no servidor da Braze.
- Se a chamada de cancelamento de registro for bem-sucedida, o SDK apaga os dados do SDK armazenados localmente e desabilita o SDK.
- Em caso de falha, invoca o `errorCallback` para permitir que o integrador tome uma ação.

O exemplo a seguir mostra o tratamento de `logout` baseado em retorno de chamada. Use-o quando precisar de tratamento imediato de sucesso e erro, e substitua o registro de log pelo fluxo do seu app.

```javascript
import { logout } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully logged out');
};

const errorCallback = () => {
  console.log('Failed to log out');
};

logout(successCallback, errorCallback);
```

#### Reativar o rastreamento e push após `logout` {#re-enable-tracking-and-push-after-logout}

Após um `logout` bem-sucedido, chame [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) e, em seguida, registre-se novamente para notificações com seu sistema operacional (SO) ou provedor de push seguindo a [configuração de web push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

#### Evite chamadas imediatas de cancelamento de registro {#avoid-immediate-unregister-calls}

Evite chamar `logout` ou `unregisterPush` diretamente após registrar-se para notificações por push com o SO ou provedor de push. Devido ao processamento assíncrono do servidor, isso pode, raramente, readicionar o token por push ao usuário da Braze.

### Cancelar registro de push {#unregister-push}

Para parar de enviar push para um dispositivo sem limpeza automatizada adicional, use o método `unregisterPush`. Isso remove o token por push do dispositivo do usuário atual no servidor da Braze e limpa o token armazenado localmente.

O exemplo a seguir mostra o tratamento de `unregisterPush` baseado em retorno de chamada. Use-o quando precisar de tratamento imediato de sucesso e erro, e substitua o registro de log pelo fluxo do seu app.

```javascript
import { unregisterPush } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully unregistered from push');
};

const errorCallback = () => {
  console.log('Failed to unregister from push');
};

unregisterPush(successCallback, errorCallback);
```

#### Registrar-se novamente para push após `unregisterPush` {#re-register-push-after-unregisterpush}

Após chamar `unregisterPush`, registre-se novamente para notificações com seu SO ou provedor de push seguindo a [configuração de web push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) antes de enviar notificações por push da Braze novamente.

{% alert note %}
Em navegadores compatíveis, quando existe uma inscrição de push ativa, `unregisterPush` também cancela o registro do service worker gerenciado pela Braze após cancelar a inscrição da API Push do navegador. Se você definir `manageServiceWorkerExternally` como `true`, o SDK não cancela o registro do service worker para você.
{% endalert %}

#### Evite chamadas imediatas de cancelamento de registro

Evite chamar `logout` ou `unregisterPush` diretamente após registrar-se para notificações por push com o SO ou provedor de push. Devido ao processamento assíncrono do servidor, isso pode, raramente, readicionar o token por push ao usuário da Braze.