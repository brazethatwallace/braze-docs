---
nav_title: Integração
article_title: Integração push para iOS
platform: iOS
page_order: 0
description: "Este artigo de referência aborda como integrar notificações por push em seu aplicativo iOS."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração push {#push-integration}

## Etapa 1: Faça upload do seu token de APNs {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

## Etapa 2: Ative as capacidades de push {#step-2-enable-push-capabilities}

Nas configurações do seu projeto, certifique-se de que, na guia **Capabilities**, a capacidade **Push Notifications** esteja ativada.

![Nas configurações do seu projeto, certifique-se de que, na guia Capabilities, a capacidade Push Notifications esteja ativada.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

Se você tiver certificados de push separados para desenvolvimento e produção, desmarque a caixa **Automatically manage signing** na guia **General**. Isso permitirá que você escolha perfis de provisionamento diferentes para cada configuração de compilação, já que o recurso de assinatura automática de código do Xcode faz apenas a assinatura de desenvolvimento.

![Configurações do projeto no Xcode mostrando a guia "general". Nessa guia, a opção "Automatically manage signing" está desmarcada.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## Etapa 3: Registrar-se para notificações por push {#step-3-register-for-push-notifications}

O trecho de código apropriado deve ser incluído no método delegado `application:didFinishLaunchingWithOptions:` do seu app para que os dispositivos dos seus usuários se registrem no APNs. Certifique-se de chamar todo o código de integração de push na thread principal do seu aplicativo.

A Braze também fornece categorias de push padrão para suporte a botões de ação por push, que devem ser adicionadas manualmente ao seu código de registro de push. Consulte [botões de ação por push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons) para etapas adicionais de integração.

{% alert warning %}
Se você implementou um prompt de push personalizado conforme descrito em nossas [melhores práticas de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting), certifique-se de que está chamando o código a seguir **toda vez que o app for executado** após o usuário conceder permissões de push ao seu app. **Os apps precisam se registrar novamente no APNs, pois os [tokens de dispositivo podem mudar arbitrariamente](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### Usando o framework UserNotification (iOS 10+) {#using-usernotification-framework-ios-10}

Se você está usando o framework `UserNotifications` (recomendado), introduzido no iOS 10, adicione o código a seguir ao método `application:didFinishLaunchingWithOptions:` do delegado do seu app.

{% alert important %}
O trecho de código a seguir inclui integração para autenticação de push provisória (linhas 5 e 6). Se você não planeja usar autorização provisória no seu app, pode remover as linhas de código que adicionam `UNAuthorizationOptionProvisional` às opções de `requestAuthorization`.<br>Visite [Opções de notificação do iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options) para saber mais sobre autenticação de push provisória.
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
Você deve atribuir o objeto delegado usando `center.delegate = self` de forma síncrona antes que o app termine de ser inicializado, preferencialmente em `application:didFinishLaunchingWithOptions:`. Caso contrário, seu app pode perder notificações por push recebidas. Visite a documentação da Apple sobre [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para saber mais.
{% endalert %}

### Sem o framework UserNotifications {#without-usernotifications-framework}

Se você não está usando o framework `UserNotifications`, adicione o código a seguir ao método `application:didFinishLaunchingWithOptions:` do delegado do seu app:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}

## Etapa 4: Registre tokens por push na Braze {#step-4-register-push-tokens-with-braze}

Após a conclusão do registro no APNs, o método a seguir deve ser alterado para passar o `deviceToken` resultante para a Braze, de modo que o usuário fique habilitado para notificações por push:

{% tabs %}
{% tab OBJECTIVE-C %}

Adicione o código a seguir ao seu método `application:didRegisterForRemoteNotificationsWithDeviceToken:`:

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

Adicione o código a seguir ao método `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` do seu app:

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
O método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` é chamado toda vez após `[[UIApplication sharedApplication] registerForRemoteNotifications]` ser chamado. Se você estiver migrando para a Braze a partir de outro serviço de push e o dispositivo do seu usuário já estiver registrado no APNs, esse método coletará tokens de registros existentes na próxima vez que for chamado, e os usuários não precisarão aceitar novamente as notificações por push.
{% endalert %}

## Etapa 5: Ativar o tratamento de push {#step-5-enable-push-handling}

O código a seguir encaminha as notificações por push recebidas para a Braze e é necessário para registrar análises de push e tratamento de links. Certifique-se de chamar todo o código de integração de push na thread principal do seu aplicativo.

### iOS 10+

Ao compilar para iOS 10+, recomendamos que você integre o framework `UserNotifications` e faça o seguinte:

{% tabs %}
{% tab OBJECTIVE-C %}

Adicione o seguinte código ao método `application:didReceiveRemoteNotification:fetchCompletionHandler:` do seu aplicativo:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Em seguida, adicione o seguinte código ao método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` do seu app:

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Tratamento de push em primeiro plano**

Para exibir uma notificação por push enquanto o app está em primeiro plano, implemente `userNotificationCenter:willPresentNotification:withCompletionHandler:`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

Se a notificação em primeiro plano for clicada, o delegate de push do iOS 10 `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` será chamado, e a Braze registrará um evento de clique de push.

{% endtab %}
{% tab swift %}

Adicione o seguinte código ao método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` do seu app:

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

Em seguida, adicione o seguinte código ao método `userNotificationCenter(_:didReceive:withCompletionHandler:)` do seu app:

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**Tratamento de push em primeiro plano**

Para exibir uma notificação por push enquanto o app está em primeiro plano, implemente `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

Se a notificação em primeiro plano for clicada, o delegate de push do iOS 10 `userNotificationCenter(_:didReceive:withCompletionHandler:)` será chamado, e a Braze registrará um evento de clique de push.

{% endtab %}
{% endtabs %}

### Anterior ao iOS 10 {#pre-ios-10}

O iOS 10 alterou o comportamento de modo que `application:didReceiveRemoteNotification:fetchCompletionHandler:` não é mais chamado quando um push é clicado. Por esse motivo, se você não atualizar para compilar com iOS 10+ e usar o framework `UserNotifications`, será necessário chamar a Braze a partir de ambos os delegates antigos, o que é uma mudança em relação à nossa integração anterior.

Para apps compilados com SDKs anteriores ao iOS 10, use as seguintes instruções:

{% tabs %}
{% tab OBJECTIVE-C %}

Para ativar o rastreamento de abertura em notificações por push, adicione o seguinte código ao método `application:didReceiveRemoteNotification:fetchCompletionHandler:` do seu app:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Para dar suporte à análise de push no iOS 10, você também deve adicionar o seguinte código ao método delegate `application:didReceiveRemoteNotification:` do seu app:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

Para ativar o rastreamento de abertura em notificações por push, adicione o seguinte código ao método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` do seu app:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

Para dar suporte à análise de push no iOS 10, você também deve adicionar o seguinte código ao método delegate `application(_:didReceiveRemoteNotification:)` do seu app:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Etapa 6: Deep linking {#step-6-deep-linking}

O deep linking de uma notificação por push para o app é tratado automaticamente por meio de nossa documentação padrão de integração de push. Se você quiser saber mais sobre como adicionar deep links a locais específicos do seu app, consulte nossos [casos de uso avançados]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#linking-handling-customization).

## Etapa 7: Testes unitários (opcional) {#step-7-unit-tests-optional}

Para adicionar cobertura de testes às etapas de integração que você acabou de seguir, implemente [testes unitários de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).