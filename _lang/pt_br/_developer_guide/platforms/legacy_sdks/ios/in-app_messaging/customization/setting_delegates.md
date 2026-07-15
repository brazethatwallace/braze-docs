---
nav_title: Definir delegados
article_title: Definir delegados de mensagem no app para iOS
platform: iOS
page_order: 2
description: "Este artigo de referência cobre a configuração de delegados de mensagens no app para seu aplicativo iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Definir delegados {#set-delegates}

A exibição e a entrega de mensagens no app podem ser personalizadas no código configurando nossos delegados opcionais.

## Delegado de mensagem no app {#in-app-message-delegate}

O delegado [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) pode ser usado para receber cargas úteis de mensagens no app disparadas para processamento adicional, receber eventos do ciclo de vida de exibição e controlar o tempo de exibição.

Defina seu objeto delegado `ABKInAppMessageUIDelegate` na instância da Braze chamando:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

Confira nosso [app de exemplo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) de mensagem no app para ver um exemplo de implementação. Note que, se você não estiver incluindo a biblioteca de interface do usuário da Braze em seu projeto (incomum), este delegado não estará disponível.

## Delegado principal de mensagem no app {#core-in-app-message-delegate}

Se você não estiver incluindo a biblioteca de interface do usuário da Braze em seu projeto e quiser receber cargas úteis de mensagens no app disparadas para processamento adicional ou exibição personalizada no seu app, implemente o protocolo [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates).

Defina seu objeto delegado `ABKInAppMessageControllerDelegate` na instância da Braze chamando:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

Você também pode definir seu delegado principal de mensagem no app no momento da inicialização via `appboyOptions` usando a chave `ABKInAppMessageControllerDelegateKey`:
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## Declarações de métodos {#method-declarations}

Para mais informações, consulte os seguintes arquivos de cabeçalho:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Exemplos de implementação {#implementation-samples}

Veja [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) no app de exemplo de mensagem no app.