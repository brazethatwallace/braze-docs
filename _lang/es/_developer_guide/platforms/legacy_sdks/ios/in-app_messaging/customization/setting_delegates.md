---
nav_title: Establecer delegados
article_title: Configurar delegados de mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 2
description: "Este artículo de referencia trata sobre la configuración de los delegados de mensajería dentro de la aplicación para tu aplicación de iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Establecer delegados {#set-delegates}

Las personalizaciones de la visualización y entrega de mensajes dentro de la aplicación pueden realizarse en código configurando nuestros delegados opcionales.

## Delegado de mensajes dentro de la aplicación {#in-app-message-delegate}

El delegado [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) puede utilizarse para recibir cargas útiles de mensajes dentro de la aplicación desencadenados para su posterior procesamiento, recibir eventos del ciclo de vida de la visualización y controlar el tiempo de visualización.

Configura tu objeto delegado `ABKInAppMessageUIDelegate` en la instancia de Braze llamando a:

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

Echa un vistazo a nuestra [aplicación de ejemplo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) de mensajes dentro de la aplicación para ver un ejemplo de implementación. Ten en cuenta que si no incluyes la biblioteca Braze UI en tu proyecto (poco común), este delegado no estará disponible.

## Delegado central de mensajes dentro de la aplicación {#core-in-app-message-delegate}

Si no incluyes la biblioteca Braze UI en tu proyecto y quieres recibir cargas útiles de mensajes dentro de la aplicación desencadenados para su posterior procesamiento o visualización personalizada en tu aplicación, implementa el protocolo [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates).

Configura tu objeto delegado `ABKInAppMessageControllerDelegate` en la instancia de Braze llamando a:

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

También puedes configurar tu delegado central de mensajes dentro de la aplicación en el momento de la inicialización a través de `appboyOptions` utilizando la clave `ABKInAppMessageControllerDelegateKey`:
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

## Declaraciones de métodos {#method-declarations}

Para más información, consulta los siguientes archivos de encabezado:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Muestras de implementación {#implementation-samples}

Consulta [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) en la aplicación de ejemplo de mensajes dentro de la aplicación.