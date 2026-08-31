---
nav_title: Rastrear sessões
article_title: Rastrear sessões
page_order: 3.3
description: "Saiba como rastrear sessões por meio do SDK da Braze."
---

# Rastrear sessões {#track-sessions}

> Saiba como rastrear sessões por meio do SDK da Braze.

{% alert note %}
Para wrapper SDKs não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Definindo inatividade {#defining-inactivity}

Entender como a inatividade é definida e medida é fundamental para gerenciar ciclos de vida de sessão de forma eficaz no Web SDK. Inatividade se refere a um período durante o qual o Braze Web SDK não detecta nenhum evento rastreado do usuário.

### Como a inatividade é medida {#how-inactivity-is-measured}

O Web SDK rastreia a inatividade com base em [eventos rastreados pelo SDK]({{site.baseurl}}/user_guide/data/activation/events/events_overview). O SDK mantém um temporizador interno que é reiniciado cada vez que um evento rastreado é enviado. Se nenhum evento rastreado pelo SDK ocorrer dentro do período de tempo limite configurado, a sessão é considerada inativa e encerrada.

Para saber mais sobre como o ciclo de vida da sessão é implementado no Web SDK, consulte o código-fonte de gerenciamento de sessões no [repositório do Braze Web SDK no GitHub](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**O que conta como atividade por padrão:**
- Abrir ou atualizar o app web
- Interagir com elementos de interface orientados pela Braze (como [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages) ou [Content Cards]({{site.baseurl}}/developer_guide/content_cards))
- Chamar métodos do SDK que enviam eventos rastreados (como [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events) ou [atualizações de atributos de usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes))

**O que não conta como atividade por padrão:**
- Alternar para uma guia diferente do navegador
- Minimizar a janela do navegador
- Eventos de foco ou desfoque do navegador
- Rolagem ou movimentos do mouse na página

{% alert note %}
O Web SDK não rastreia automaticamente alterações de visibilidade do navegador, troca de guias ou foco do usuário. No entanto, você pode rastrear essas interações no nível do navegador implementando ouvintes de eventos personalizados usando a [API de visibilidade de página](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) do navegador e enviando [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web) para a Braze. Para um exemplo de implementação, consulte [Rastreamento de inatividade personalizada](#tracking-custom-inactivity).
{% endalert %}

### Configuração do tempo limite da sessão {#session-timeout-configuration}

Por padrão, o Web SDK considera uma sessão inativa após 30 minutos sem nenhum evento rastreado. Você pode personalizar esse limite ao inicializar o SDK usando o parâmetro `sessionTimeoutInSeconds`. Para detalhes sobre como configurar esse parâmetro, incluindo exemplos de código, consulte [Alterando o tempo limite padrão da sessão](#changing-the-default-session-timeout).

### Exemplo: entendendo cenários de inatividade {#example-understanding-inactivity-scenarios}

Considere o seguinte cenário:

1. Um usuário abre seu website, e o SDK inicia uma sessão chamando [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession).
2. O usuário alterna para uma guia diferente do navegador para visualizar outro website por 30 minutos.
3. Durante esse tempo, nenhum evento rastreado pelo SDK ocorre no seu website.
4. Após 30 minutos de inatividade, a sessão é encerrada automaticamente.
5. Quando o usuário retorna à guia do seu website e dispara um evento do SDK (como visualizar uma página ou interagir com conteúdo), uma nova sessão é iniciada.

### Rastreamento de inatividade personalizada {#tracking-custom-inactivity}

Se você precisa rastrear inatividade com base na visibilidade do navegador ou na troca de guias, implemente ouvintes de eventos personalizados no seu código JavaScript. Use eventos do navegador como `visibilitychange` para detectar quando os usuários saem da sua página, e envie manualmente [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events) para a Braze ou chame [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) quando apropriado.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

Para saber mais sobre como registrar eventos personalizados, consulte [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events). Para detalhes sobre o ciclo de vida da sessão e configuração do tempo limite, consulte [Alterando o tempo limite padrão da sessão](#change-session-timeout).

## Assinando atualizações de sessão {#subscribing-to-session-updates}

### Etapa 1: Assinar atualizações {#step-1-subscribe-to-updates}

Para assinar atualizações de sessão, use o método `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
No momento, a assinatura de atualizações de sessão não é compatível com o SDK da Braze para web.
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
Se você registrar um retorno de chamada de encerramento de sessão, ele será disparado quando o app retornar ao primeiro plano. A duração da sessão é medida desde o momento em que o app é aberto ou entra em primeiro plano até o momento em que ele é fechado ou vai para segundo plano.

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

Para assinar um fluxo assíncrono, você pode usar [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream).

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
O SDK React Native não expõe um método para assinar atualizações de sessão diretamente. O ciclo de vida da sessão é gerenciado pelo SDK nativo subjacente. Portanto, para assinar atualizações, use a abordagem nativa da plataforma na guia **Android** ou **Swift**.
{% endtab %}
{% endtabs %}

### Etapa 2: Testar o rastreamento de sessão (opcional) {#step-2-test-session-tracking-optional}

Para testar o rastreamento de sessão, inicie uma sessão no seu dispositivo e abra o dashboard da Braze e busque pelo usuário relevante. No perfil do usuário, selecione **Sessions Overview**. Se as métricas forem atualizadas conforme esperado, o rastreamento de sessão está funcionando corretamente.

![A seção de visão geral de sessões de um perfil de usuário mostrando o número de sessões, a data do último uso e a data do primeiro uso.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Os detalhes específicos do app só são exibidos para usuários que usaram mais de um app.
{% endalert %}

## Alterando o tempo limite padrão da sessão {#change-session-timeout}

Você pode alterar a duração do tempo que passa antes que uma sessão expire automaticamente.

{% tabs %}
{% tab web %}
Por padrão, o tempo limite da sessão é definido como `30` minutos. Para alterar isso, passe a opção `sessionTimeoutInSeconds` para sua função [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize). Pode ser definido como qualquer inteiro maior ou igual a `1`.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
Por padrão, o tempo limite da sessão é definido como `10` segundos. Para alterar isso, abra seu arquivo `braze.xml` e adicione o parâmetro `com_braze_session_timeout`. Pode ser definido como qualquer inteiro maior ou igual a `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Por padrão, o tempo limite da sessão é definido como `10` segundos. Para alterar isso, defina `sessionTimeout` no objeto `configuration` que é passado para [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Pode ser definido como qualquer inteiro maior ou igual a `1`.

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
O SDK React Native depende dos SDKs nativos para gerenciar sessões. Para alterar o tempo limite padrão da sessão, configure-o na camada nativa:

- **Android:** Defina `com_braze_session_timeout` no seu arquivo `braze.xml`. Para detalhes, selecione a guia **Android**.
- **iOS:** Defina `sessionTimeout` no seu objeto `Braze.Configuration`. Para detalhes, selecione a guia **Swift**.
{% endtab %}
{% endtabs %}

{% alert note %}
Se você definir um tempo limite de sessão, todas as semânticas de sessão serão automaticamente estendidas para o tempo limite definido.
{% endalert %}

## Solução de problemas {#troubleshooting}

### O perfil de usuário tem 0 sessões {#user-profile-has-0-sessions}

Um perfil de usuário pode ter 0 sessões se o usuário foi criado fora do SDK:

- **Criado pela REST API:** Se um usuário é criado através do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) com um `app_id` na solicitação, o perfil aparece associado àquele app, mas não tem dados de sessão porque o SDK nunca foi inicializado para esse usuário.
- **Criado por importação CSV:** Se um usuário é importado via [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) sem valores para os campos de primeira ou última sessão, o perfil existe com 0 sessões.

### Alguns usuários não estão registrando sessões {#some-users-are-not-logging-sessions}

Como as sessões são rastreadas somente após a inicialização do SDK, usuários que não acionam a inicialização do SDK não registram nenhuma sessão. Isso geralmente acontece quando seu app utiliza lógica condicional antes de inicializar o SDK, como adiar a inicialização por trás de um fluxo de login, solicitação de consentimento ou Feature Flag. Para orientações de implementação, consulte [Inicialização atrasada]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift#step-2-set-up-delayed-initialization-optional). Nesses casos, qualquer usuário que não satisfaça a condição nunca inicia uma sessão.

Se alguns usuários estão registrando sessões e outros não, verifique o seguinte:

- **Verifique sua lógica de inicialização.** Confirme que o SDK é inicializado para todos os usuários e pontos de entrada do app, não apenas para alguns.
- **Procure por mudanças recentes no app.** Nova lógica condicional na inicialização do SDK pode causar uma queda repentina na contagem de sessões.
- **Compare usuários afetados e não afetados.** Identifique diferenças na versão do app, tipo de dispositivo ou fluxo de usuário que possam explicar por que a inicialização é ignorada para determinados usuários.

Se o problema persistir após verificar sua implementação, reproduza o problema e colete as seguintes informações antes de entrar em contato com o suporte:

- Etapas para reproduzir o problema
- A versão do app afetada
- [Logs detalhados do SDK]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), capturados enquanto o problema ocorre (ou por plataforma: [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_enabling-logs), [Swift]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift#swift_setting-the-log-level), [Web]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web#web_logging))
- O snippet de código para inicialização do SDK
- Um resumo de qualquer lógica condicional aplicada antes da inicialização