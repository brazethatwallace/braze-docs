---
nav_title: Mensagens de gatilho
article_title: "Disparar mensagens no app"
page_order: 0.2
description: "Aprenda como disparar mensagens no app através do SDK da Braze, incluindo encadeamento de mensagens em uma sessão e substituição do limite de frequência padrão."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Disparar mensagens no app {#trigger-in-app-messages}

> Aprenda como disparar mensagens no app através do SDK da Braze.

## Gatilhos e entrega de mensagens {#message-triggers-and-delivery}

As mensagens no app são disparadas quando o SDK registra um dos seguintes tipos de eventos personalizados: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase` e `Custom Event` (os dois últimos contêm filtros de propriedade robustos).

No início da sessão de um usuário, a Braze entrega todas as mensagens no app elegíveis ao dispositivo dele, enquanto simultaneamente faz o pré-carregamento de ativos para minimizar a latência de exibição. Se o evento-gatilho tiver mais de uma mensagem no app elegível, apenas a mensagem com a prioridade mais alta é entregue. Para saber mais, consulte [Ciclo de vida da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions).

{% alert note %}
As mensagens no app não podem ser disparadas por meio da API ou por eventos de API&#8212;apenas por eventos personalizados registrados pelo SDK. Para saber mais sobre registro, consulte [Registrando eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events).
{% endalert %}

## Tipos de mensagens no app {#types-of-in-app-messages}

A Braze envia os seguintes tipos de mensagens no app para os dispositivos dos usuários no início da sessão: `inapp` e `templated_iam`. Como usuário do dashboard, você não vê os diferentes tipos, mas a Braze os trata de maneira diferente dependendo da configuração e do conteúdo.

### `inapp` (padrão) {#inapp-standard}

Uma mensagem no app `inapp` (ou "[padrão]({{site.baseurl}}/user_guide/channels/in_app_messages)") já vem modelada com as informações necessárias, como atributos personalizados que a Braze já conhece. Geralmente, quando a mensagem no app é baixada para o dispositivo, o evento-gatilho faz com que o SDK exiba a mensagem no app `inapp` mesmo quando o dispositivo está offline ou em modo avião.

### `templated_iam` (modelada) {#templated_iam-templated}

Uma mensagem no app `templated_iam` (ou "modelada") ainda não foi modelada com as informações necessárias. A Braze precisa fazer outra solicitação para obter as informações antes que a mensagem possa ser exibida.

As mensagens no app são entregues como mensagens no app modeladas quando **Reavaliar a elegibilidade da campanha antes de exibir** está selecionado ou se qualquer uma das seguintes Liquid tags existir na mensagem:

- `canvas_entry_properties`
- `connected_content`
- Variáveis de SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Isso significa que, durante o início da sessão, o dispositivo recebe o gatilho daquela mensagem no app em vez da mensagem inteira. Quando o usuário dispara a mensagem no app, o dispositivo do usuário faz uma solicitação de rede para buscar a mensagem real.

{% alert note %}
A mensagem não será entregue se o dispositivo não tiver acesso à internet. A mensagem pode não ser entregue se a lógica Liquid demorar muito para ser resolvida.
{% endalert %}

## Pares chave-valor {#key-value-pairs}

Ao criar uma Campaign na Braze, você pode definir pares chave-valor como `extras`, que o objeto de mensagem no app pode usar para enviar dados ao seu app.

{% tabs %}
{% tab web %}
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
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Para saber mais, consulte o [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab swift %}
O exemplo a seguir usa lógica personalizada para definir a apresentação de uma mensagem no app com base em seus pares chave-valor em `extras`. Para um exemplo completo de personalização, confira [nosso app de exemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Desativando disparos automáticos {#disabling-automatic-triggers}

Por padrão, as mensagens no app são disparadas automaticamente. Para desativar isso:

{% tabs %}

{% tab web %}
Remova a chamada para `braze.automaticallyShowInAppMessages()` dentro do seu snippet de carregamento e crie uma lógica personalizada para controlar a exibição ou não de uma mensagem no app.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message

  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }

  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Se você chamar `braze.showInAppMessage` sem remover `braze.automaticallyShowInAppMessages()`, as mensagens poderão ser exibidas duas vezes.
{% endalert %}

Para um controle mais avançado sobre o tempo de exibição das mensagens, incluindo o adiamento e a restauração de mensagens disparadas, consulte nosso [Tutorial: Adiando e restaurando mensagens disparadas]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab android %}
1. Implemente o [`IInAppMessageManagerListener`]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener) para definir um listener personalizado.
2. Atualize seu método [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) para retornar [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html).

Para um controle mais avançado sobre o tempo de exibição das mensagens, incluindo exibição posterior e reenfileiramento, consulte nossa página [Personalizando mensagens]({{site.baseurl}}/developer_guide/in_app_messages/customization?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener).
{% endtab %}

{% tab swift %}
1. Implemente o delegate `BrazeInAppMessageUIDelegate` no seu app. Para um passo a passo completo, consulte [Tutorial: Interface de mensagem no app](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Atualize seu método de delegate `inAppMessage(_:displayChoiceForMessage:)` para retornar `.discard`.

Para um controle mais avançado sobre o tempo de exibição das mensagens, incluindo o adiamento e a restauração de mensagens disparadas, consulte nosso [Tutorial: Adiando e restaurando mensagens disparadas]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab flutter %}
1. Verifique se você está usando o inicializador de integração automática, que é ativado por padrão nas versões `2.2.0` e posteriores.
2. Defina a operação padrão de mensagem no app como `DISCARD` adicionando a seguinte linha ao seu arquivo `braze.xml`.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
Para Android, desmarque **Automatically Display In-App Messages** no editor de configuração da Braze. Alternativamente, você pode definir `com_braze_inapp_show_inapp_messages_automatically` como `false` no arquivo `braze.xml` do seu projeto Unity.

A operação inicial de exibição de mensagem no app pode ser configurada nas configurações da Braze usando "In App Message Manager Initial Display Operation".
{% endsubtab %}

{% subtab iOS %}
Para iOS, defina os listeners de game object no editor de configuração da Braze e certifique-se de que **Braze Displays In-App Messages** não esteja selecionado.

A operação inicial de exibição de mensagem no app pode ser configurada nas configurações da Braze usando "In App Message Manager Initial Display Operation".
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Encadeando duas mensagens no app em uma sessão {#chaining-two-in-app-messages-in-one-session}

Você pode disparar uma mensagem no app a partir do início da sessão e, em seguida, disparar uma segunda mensagem no app após um botão ser pressionado na primeira. Para isso, registre um evento personalizado para o clique do botão que disparará a segunda mensagem. O disparo da segunda mensagem já deve estar no dispositivo (o usuário já deve ser elegível para a segunda mensagem) e deve ocorrer no lado do dispositivo (o SDK da Braze não detectará mudanças de atributos personalizados que ocorrem nos servidores da Braze). O intervalo padrão de 30 segundos entre disparos de mensagens no app deve ser alterado para exibir várias mensagens no app em rápida sucessão. Para configuração específica por plataforma, consulte [Substituindo o limite de frequência padrão](#overriding-the-default-rate-limit).

## Substituindo o limite de frequência padrão {#overriding-the-default-rate-limit}

Por padrão, o SDK limita a frequência de In-App Messages disparadas a uma vez a cada 30 segundos. Para substituir esse comportamento, adicione a seguinte propriedade ao seu arquivo de configuração antes que a instância da Braze seja inicializada. Esse valor é usado como o novo limite de frequência em segundos.

Para apps em produção, não defina esse valor abaixo de 10 segundos, para que os usuários não sejam sobrecarregados com In-App Messages consecutivas. Para testes e fluxos de apps de exemplo, 5 segundos é uma configuração comum.

Você pode definir esse intervalo como `0` para testes. No entanto, um intervalo de `0` segundo não força várias In-App Messages a aparecerem ao mesmo tempo. Se uma mensagem no app já estiver visível, outra mensagem disparada não será exibida até que a mensagem atual seja fechada.

{% tabs %}
{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}

{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Disparando mensagens manualmente {#manually-triggering-messages}

Por padrão, as mensagens no app são disparadas automaticamente quando o SDK registra um evento personalizado. No entanto, além disso, você pode disparar mensagens manualmente usando os seguintes métodos.

### Usando um evento do lado do servidor {#using-a-server-side-event}

{% tabs %}
{% tab web %}
No momento, o SDK da Braze para web não oferece suporte ao disparo manual de mensagens usando eventos do lado do servidor.
{% endtab %}

{% tab android %}
Para disparar uma mensagem no app usando um evento enviado pelo servidor, envie uma notificação por push silenciosa para o dispositivo, permitindo que um retorno de chamada de push personalizado registre um evento baseado no SDK. Esse evento então disparará a mensagem no app visível ao usuário.

#### Etapa 1: Criar um retorno de chamada de push para receber a push silenciosa {#step-1-create-a-push-callback-to-receive-the-silent-push}

Registre seu retorno de chamada de push personalizado para ouvir uma notificação por push silenciosa específica. Para saber mais, consulte [Configurando notificações por push]({{site.baseurl}}/developer_guide/push_notifications#android_setting-up-push-notifications).

Dois eventos serão registrados para que a mensagem no app seja entregue: um pelo servidor e outro de dentro do seu retorno de chamada de push personalizado. Para garantir que o mesmo evento não seja duplicado, o evento registrado de dentro do seu retorno de chamada de push deve seguir uma convenção de nomenclatura genérica, por exemplo, "evento de disparo de mensagem no app", e não o mesmo nome do evento enviado pelo servidor. Se isso não for feito, a segmentação e os dados de usuários podem ser afetados por eventos duplicados sendo registrados para uma única ação do usuário.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### Etapa 2: Criar uma Campaign de push {#step-2-create-a-push-campaign}

Crie uma [Campaign de push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android) disparada pelo evento enviado pelo servidor.

![Etapa de entrega de uma Campaign de push silenciosa configurada para entrega baseada em ação com um evento personalizado server_event como gatilho.]({% image_buster /assets/img_archive/serverSentPush.png %})

A Campaign de push deve incluir extras de pares chave-valor que indiquem que essa Campaign de push é enviada para registrar um evento personalizado do SDK. Esse evento será usado para disparar a mensagem no app.

![Dois conjuntos de pares chave-valor: IS_SERVER_EVENT definido como "true" e CAMPAIGN_NAME definido como "example campaign name".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

O código de exemplo de retorno de chamada de push anterior reconhece os pares chave-valor e registra o evento personalizado do SDK apropriado.

Se você quiser incluir propriedades de evento para anexar ao seu evento de "disparo de mensagem no app", pode fazer isso passando-as nos pares chave-valor da carga útil do push. Neste exemplo, o nome da Campaign da mensagem no app subsequente foi incluído. Seu retorno de chamada de push personalizado pode então passar o valor como parâmetro da propriedade do evento ao registrar o evento personalizado.

#### Etapa 3: Criar uma Campaign de mensagem no app {#step-3-create-an-in-app-message-campaign}

Crie sua Campaign de mensagem no app visível ao usuário no dashboard da Braze. Essa Campaign deve ter entrega baseada em ação e ser disparada pelo evento personalizado registrado de dentro do seu retorno de chamada de push personalizado.

No exemplo a seguir, a mensagem no app específica a ser disparada foi configurada enviando a propriedade do evento como parte da push silenciosa inicial.

![Uma Campaign de entrega baseada em ação onde uma mensagem no app será disparada quando "campaign_name" for igual a "IAM campaign name example."]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Se um evento enviado pelo servidor for registrado enquanto o app não estiver em primeiro plano, o evento será registrado, mas a mensagem no app não será exibida. Se você quiser que o evento seja postergado até que o aplicativo esteja em primeiro plano, uma verificação deve ser incluída no seu receptor de push personalizado para descartar ou postergar o evento até que o app entre em primeiro plano.
{% endtab %}

{% tab swift %}
#### Etapa 1: Tratar push silenciosa e pares chave-valor {#step-1-handle-silent-push-and-key-value-pairs}

Implemente a seguinte função e chame-a dentro do método [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didreceiveremotenotification:fetchcompletionhandler:)):

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

Quando a push silenciosa é recebida, um evento registrado pelo SDK "disparo de mensagem no app" será registrado no perfil de usuário.

{% alert important %}
Como uma notificação por push está sendo usada para registrar um evento personalizado do SDK, a Braze precisará armazenar um token por push para cada usuário para habilitar esta solução. Para usuários iOS, a Braze só armazenará um token a partir do momento em que o usuário receber o prompt de push do sistema operacional. Antes disso, o usuário não será alcançável via push, e a solução anterior não será possível.
{% endalert %}

#### Etapa 2: Criar uma Campaign de push silenciosa {#step-2-create-a-silent-push-campaign}

Crie uma [Campaign de push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) que é disparada pelo evento enviado pelo servidor.

![Uma Campaign de mensagem no app com entrega baseada em ação que será entregue aos usuários cujos perfis possuem o evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

A Campaign de push deve incluir extras de pares chave-valor, que indicam que essa Campaign de push é enviada para registrar um evento personalizado do SDK. Esse evento será usado para disparar a mensagem no app.

![Uma Campaign de mensagem no app com entrega baseada em ação que possui dois pares chave-valor. "CAMPAIGN_NAME" definido como "In-app message name example" e "IS_SERVER_EVENT" definido como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

O código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` verifica a chave `IS_SERVER_EVENT` e registrará um evento personalizado do SDK se ela estiver presente.

Você pode alterar o nome do evento ou as propriedades do evento enviando o valor desejado dentro dos extras de pares chave-valor da carga útil do push. Ao registrar o evento personalizado, esses extras podem ser usados como parâmetro do nome do evento ou como uma propriedade do evento.

#### Etapa 3: Criar uma Campaign de mensagem no app

Crie sua Campaign de mensagem no app visível ao usuário no dashboard da Braze. Essa Campaign deve ter entrega baseada em ação e ser disparada pelo evento personalizado registrado de dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

No exemplo a seguir, a mensagem no app específica a ser disparada foi configurada enviando a propriedade do evento como parte da push silenciosa inicial.

![Uma Campaign de mensagem no app com entrega baseada em ação que será entregue aos usuários que realizarem o evento personalizado "In-app message trigger" onde "campaign_name" for igual a "IAM Campaign Name Example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Essas mensagens no app só serão disparadas se a push silenciosa for recebida enquanto o aplicativo estiver em primeiro plano.
{% endalert %}
{% endtab %}
{% endtabs %}

### Exibindo uma mensagem predefinida {#displaying-a-pre-defined-message}

Para exibir manualmente uma mensagem no app predefinida, use o seguinte método:

{% tabs %}
{% tab web %}
Para o SDK para web, use `braze.showInAppMessage(inAppMessage)` para exibir qualquer mensagem no app. Para detalhes e um exemplo, consulte [Exibindo uma mensagem em tempo real](#displaying-a-message-in-real-time).
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}
{% endtabs %}

### Exibindo uma mensagem em tempo real {#displaying-a-message-in-real-time}

Você também pode criar e exibir mensagens no app locais em tempo real, usando as mesmas opções de personalização disponíveis no dashboard. Para fazer isso:

{% tabs %}
{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Não exiba mensagens no app quando o teclado virtual estiver exibido na tela, pois a renderização é indefinida nessa circunstância.
{% endalert %}
{% endtab %}

{% tab swift %}
Chame manualmente o método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) no seu `inAppMessagePresenter`. Por exemplo:

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Ao criar sua própria mensagem no app, você opta por não usar o rastreamento de análise de dados e precisará gerenciar manualmente o registro de cliques e impressões usando o `message.context`.
{% endalert %}
{% endtab %}

{% tab unity %}
Para exibir a próxima mensagem na pilha, use o método `DisplayNextInAppMessage()`. As mensagens serão salvas nessa pilha se `DISPLAY_LATER` ou `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` for escolhido como a ação de exibição da mensagem no app.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Causas de atrasos em mensagens no app {#causes-of-in-app-message-delays}

Se você receber uma campanha de mensagem no app alguns segundos após o início da sessão, o atraso pode ter sido causado por:

- Um atraso no disparo da campanha
- Personalizações
- O evento-gatilho sendo registrado mais tarde do que o esperado (como no caso de um `templated_iam`)

## Mensagens de intenção de saída para Web {#exit-intent-messages-for-web}

Mensagens de intenção de saída são In-App Messages não intrusivas usadas para comunicar informações importantes aos visitantes antes que eles saiam do seu website.

Para configurar disparadores para esses tipos de mensagem no SDK para web, implemente uma biblioteca de intenção de saída no seu website (como a [biblioteca open-source do ouibounce](https://github.com/carlsednaoui/ouibounce)) e, em seguida, use o código a seguir para registrar `'exit intent'` como um evento personalizado na Braze. Assim, suas futuras campanhas de mensagens no app poderão usar esse tipo de mensagem como um evento-gatilho personalizado.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
