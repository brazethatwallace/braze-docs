---
nav_title: Botões de ação
article_title: Botões de ação por push para iOS
platform: iOS
page_order: 1
description: "Este artigo de referência aborda como implementar botões de ação em suas notificações por push do iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Botões de ação {#push-action-buttons-integration}

O SDK da Braze para iOS aceita categorias de push padrão, incluindo suporte ao tratamento de URL para cada botão de ação por push. Atualmente, as categorias padrão têm quatro conjuntos de botões de ação por push: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel` e `More`.

![Um GIF de uma notificação por push sendo puxada para baixo para exibir dois botões de ação personalizáveis.]({% image_buster /assets/img_archive/iOS8Action.gif %})

Para registrar nossas categorias de push padrão, siga as instruções de integração:

## Etapa 1: Adicionando categorias de push padrão da Braze {#step-1-adding-braze-default-push-categories}

Use o código a seguir para registrar nossas categorias de push padrão ao [registrar para push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

Clicar nos botões de ação por push com modo de ativação em segundo plano apenas descartará a notificação, sem abrir o app. Na próxima vez que o usuário abrir o app, a análise de dados do clique no botão para essas ações será enviada ao servidor.

Se você quiser criar suas próprias categorias de notificação personalizadas, consulte [personalização de botões de ação]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons#push-category-customization).

## Etapa 2: Ativar o tratamento de push interativo {#step-2-enable-interactive-push-handling}

Se você usa o framework `UNNotification` e implementou os [delegates]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling) da Braze, esse método já deve estar integrado.

Para ativar o tratamento dos botões de ação por push, incluindo análise de dados de cliques e roteamento de URL, adicione o seguinte código ao método delegate `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` do seu app:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

Se você não estiver usando o framework UNNotification, precisará adicionar o seguinte código ao método `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` do seu app para ativar o tratamento dos botões de ação por push:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Recomendamos fortemente que quem usa `handleActionWithIdentifier` comece a utilizar o framework `UNNotification`. Essa recomendação se deve à descontinuação de [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Personalização de categorias de push {#push-category-customization}

Além de fornecer um conjunto de [categorias de push padrão]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons), a Braze oferece suporte a categorias e ações de notificação personalizadas. Depois de registrar as categorias no seu app, você pode usar o dashboard da Braze para enviar categorias de notificação aos seus usuários.

Se você não estiver usando o framework `UserNotifications`, consulte a documentação de [categorias alternativas](https://developer.apple.com/documentation/usernotifications/unnotificationcategory).

Essas categorias podem então ser atribuídas a notificações por push por meio do nosso dashboard para disparar as configurações de botões de ação do seu design. Veja um exemplo que utiliza a `LIKE_CATEGORY` exibida no dispositivo:

![Uma mensagem de push exibindo dois botões de ação por push: "unlike" e "like".]({% image_buster /assets/img_archive/push_example_category.png %})