---
nav_title: Entrega de mensagem no app
article_title: Envio de mensagens no app para iOS
platform: iOS
page_order: 3
description: "Este artigo de referência aborda o envio de mensagens no app para iOS, listando diferentes tipos de disparo, semântica de entrega e etapas de disparo de eventos."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Envio de mensagens no app {#in-app-message-delivery}

## Tipos de gatilho {#trigger-types}

Nosso produto de In-App Messages permite disparar a exibição de mensagens no app como resultado de diversos tipos de evento: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` e `Push Click`. Além disso, os gatilhos `Specific Purchase` e `Custom Event` contam com filtros robustos de propriedades.

{% alert note %}
As mensagens no app disparadas só funcionam com eventos personalizados registrados por meio do SDK or kit de desenvolvimento de software da Braze. As mensagens no app não podem ser disparadas pela API or interface de programação do aplicativo (API) ou por eventos da API or interface de programação do aplicativo (API) (como eventos de compra). Se você está trabalhando com iOS, acesse nosso artigo sobre [rastreamento de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift) para saber mais.
{% endalert %}

## Semântica de entrega {#delivery-semantics}

Todas as mensagens no app para as quais um usuário é elegível são entregues ao dispositivo do usuário no início da sessão. Quando duas mensagens no app são disparadas por um mesmo evento, a mensagem no app com maior prioridade será exibida. Para saber mais sobre a semântica de início de sessão do SDK or kit de desenvolvimento de software, leia sobre nosso [ciclo de vida da sessão]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/analytics/tracking_sessions#session-lifecycle). Ao serem entregues, o SDK or kit de desenvolvimento de software fará o pré-carregamento dos ativos para que estejam disponíveis imediatamente no momento do disparo, minimizando a latência de exibição.

Quando um evento-gatilho tem mais de uma mensagem no app elegível associada a ele, apenas a mensagem no app com a maior prioridade será entregue.

Pode haver alguma latência para mensagens no app que são exibidas imediatamente na entrega (início de sessão, clique de push) devido aos ativos não terem sido pré-carregados.

## Intervalo mínimo de tempo entre disparos {#minimum-time-interval-between-triggers}

Por padrão, limitamos a frequência de In-App Messages para uma vez a cada 30 segundos, a fim de proporcionar uma experiência de qualidade ao usuário.

Você pode substituir esse valor por meio do `ABKMinimumTriggerTimeIntervalKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina o `ABKMinimumTriggerTimeIntervalKey` com o valor inteiro desejado como o tempo mínimo em segundos entre In-App Messages:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## Falha ao encontrar um gatilho correspondente {#failing-to-find-a-matching-trigger}

Quando a Braze não encontra um gatilho correspondente para um determinado evento, ela chama o método [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) do [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html). Implemente esse método na sua classe que adota o protocolo de delegado para lidar com esse cenário.

## Entrega local de mensagens no app {#local-in-app-message-delivery}

### A pilha de mensagens no app {#the-in-app-message-stack}

#### Exibindo mensagens no app {#showing-in-app-messages}

Quando um usuário é elegível para receber uma mensagem no app, o `ABKInAppMessageController` receberá a mensagem no app mais recente da pilha de mensagens no app. A pilha mantém apenas mensagens no app armazenadas em memória e é limpa entre inicializações do app a partir do modo suspenso.

{% alert important %}
Não exiba mensagens no app quando o teclado estiver visível na tela, pois a renderização é indefinida nessa circunstância.
{% endalert %}

#### Adicionando mensagens no app à pilha {#adding-in-app-messages-to-the-stack}

Os usuários são elegíveis para receber uma mensagem no app nas seguintes situações:

- Um evento-gatilho de mensagem no app é disparado
- Evento de início de sessão
- O app é aberto a partir de uma notificação por push

Mensagens no app disparadas são colocadas na pilha quando seu evento-gatilho é disparado. Se várias mensagens no app estiverem na pilha esperando para serem exibidas, a Braze exibirá primeiro a mensagem no app recebida mais recentemente (último a entrar, primeiro a sair).

#### Retornando mensagens no app à pilha {#returning-in-app-messages-to-the-stack}

Uma mensagem no app disparada pode ser retornada à pilha nas seguintes situações:

- A mensagem no app é disparada quando o app está em segundo plano.
- Outra mensagem no app está visível no momento.
- O método [delegado de UI]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) descontinuado `beforeInAppMessageDisplayed:withKeyboardIsUp:` não foi implementado e o teclado está sendo exibido no momento.
- O [método delegado]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` ou o [método delegado de UI]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) descontinuado `beforeInAppMessageDisplayed:withKeyboardIsUp:` retornou `ABKDisplayInAppMessageLater`.

#### Descartando mensagens no app {#discarding-in-app-messages}

Uma mensagem no app disparada será descartada nas seguintes situações:

- O [método delegado]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` ou o [método delegado de UI]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) descontinuado `beforeInAppMessageDisplayed:withKeyboardIsUp:` retornou `ABKDiscardInAppMessage`.
- O ativo (imagem ou arquivo ZIP) da mensagem no app falhou ao ser baixado.
- A mensagem no app está pronta para ser exibida, mas excedeu o tempo limite de duração.
- A orientação do dispositivo não corresponde à orientação da mensagem no app disparada.
- A mensagem no app é uma mensagem no app em tela cheia, mas não possui imagem.
- A mensagem no app é uma mensagem no app modal somente com imagem, mas não possui imagem.

#### Enfileirar manualmente a exibição de mensagens no app {#manually-queue-in-app-message-display}

Se você deseja exibir uma mensagem no app em outros momentos dentro do seu app, pode exibir manualmente a mensagem no app do topo da pilha chamando o seguinte método:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Criação e exibição de mensagens no app em tempo real {#real-time-in-app-message-creation-and-display}

Mensagens no app também podem ser criadas localmente dentro do app e exibidas pela Braze. Isso é particularmente útil para exibir mensagens que você deseja disparar dentro do app em tempo real. A Braze não oferece suporte a análise de dados em mensagens no app criadas localmente.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}