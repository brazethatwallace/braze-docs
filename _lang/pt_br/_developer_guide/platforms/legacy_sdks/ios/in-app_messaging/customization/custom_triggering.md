---
nav_title: Disparo personalizado
article_title: Personalize o disparo de mensagens no app para iOS
platform: iOS
page_order: 7
description: "Este artigo de referência cobre o disparo personalizado de mensagens no app para seu aplicativo iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Disparo personalizado de mensagem no app {#custom-in-app-message-triggering}

Por padrão, mensagens no app são disparadas por tipos de eventos registrados pelo SDK. Se você quiser disparar mensagens no app por eventos enviados pelo servidor, também é possível.

Para ativar esse recurso, você enviaria um push silencioso para o dispositivo, o que permite que o dispositivo registre um evento baseado em SDK. Esse evento do SDK, por sua vez, dispararia a mensagem no app voltada para o usuário.

## Etapa 1: Lidar com push silencioso e pares chave-valor {#step-1-handle-silent-push-and-key-value-pairs}

Adicione o seguinte código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

Quando o push silencioso é recebido, um evento registrado pelo SDK "in-app message trigger" será registrado no perfil de usuário. Note que essas mensagens no app só serão disparadas se o push silencioso for recebido enquanto o aplicativo estiver em primeiro plano.

## Etapa 2: Criar uma campanha push {#step-2-create-a-push-campaign}

Crie uma campanha de push silenciosa que é disparada pelo evento enviado pelo servidor. Para saber como criar uma campanha de push silenciosa, consulte [notificações por push silenciosas]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications).

![Uma campanha de mensagem no app com entrega baseada em ação que será entregue a usuários que realizarem o evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

A campanha de push precisa incluir extras de pares chave-valor, que indicam que essa campanha de push é enviada para registrar um evento personalizado do SDK. Esse evento será usado para disparar a mensagem no app:

![Uma campanha de mensagem no app com entrega baseada em ação que possui dois pares chave-valor. "CAMPAIGN_NAME" definido como "In-app message name example", e "IS_SERVER_EVENT" definido como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

O código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` verifica a chave `IS_SERVER_EVENT` e registra um evento personalizado do SDK se ela estiver presente.

Você pode alterar o nome do evento ou as propriedades do evento enviando o valor desejado dentro dos extras de pares chave-valor da carga útil push. Ao registrar o evento personalizado, esses extras podem ser usados como parâmetro do nome do evento ou como uma propriedade do evento.

## Etapa 3: Criar uma campanha de mensagem no app {#step-3-create-an-in-app-message-campaign}

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Essa campanha deve ter uma entrega baseada em ação e ser disparada a partir do evento personalizado registrado dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

No exemplo a seguir, a mensagem no app específica a ser disparada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de mensagem no app com entrega baseada em ação que será entregue a usuários que realizarem o evento personalizado "In-app message trigger" onde "campaign_name" é igual a "In-app message name example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

Como uma notificação por push é usada para registrar um evento personalizado registrado pelo SDK, a Braze precisará armazenar um token por push para cada usuário para ativar essa solução. Para iOS e Android, a Braze só armazenará um token a partir do momento em que o usuário tiver recebido o prompt de push do sistema operacional. Antes disso, o usuário não estará acessível usando push, e a solução anterior não será possível.