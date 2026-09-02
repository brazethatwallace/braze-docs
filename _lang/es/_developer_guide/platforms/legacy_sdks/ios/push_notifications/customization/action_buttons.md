---
nav_title: Botones de acción
article_title: Botones de acción push para iOS
platform: iOS
page_order: 1
description: "Este artículo de referencia explica cómo implementar botones de acción en tus notificaciones push de iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Botones de acción {#push-action-buttons-integration}

El SDK or kit de desarrollo de software de Braze para iOS es compatible con las categorías push predeterminadas, incluida la compatibilidad con la gestión de URL para cada botón de acción push. Actualmente, las categorías predeterminadas tienen cuatro conjuntos de botones de acción para push: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel` y `More`.

![Un GIF de un mensaje push que se desliza hacia abajo para mostrar dos botones de acción personalizables.]({% image_buster /assets/img_archive/iOS8Action.gif %})

Para registrar nuestras categorías push predeterminadas, sigue las instrucciones de integración:

## Paso 1: Añadir las categorías push predeterminadas de Braze {#step-1-adding-braze-default-push-categories}

Usa el siguiente código para registrar nuestras categorías push predeterminadas cuando te [registres para push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-4-register-push-tokens-with-braze):

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

Al hacer clic en los botones de acción push con modo de activación en segundo plano, solo se descartará la notificación y no se abrirá la aplicación. La próxima vez que el usuario abra la aplicación, los análisis de clics de botón para estas acciones se enviarán al servidor.

Si deseas crear tus propias categorías de notificación personalizadas, consulta [personalización de botones de acción]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons#push-category-customization).

## Paso 2: Habilitar el manejo interactivo de push {#step-2-enable-interactive-push-handling}

Si utilizas el framework `UNNotification` y has implementado los [delegados]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling) de Braze, ya deberías tener este método integrado.

Para habilitar el manejo de nuestros botones de acción para notificación push, incluyendo análisis de clics y enrutamiento de URL, añade el siguiente código al método delegado `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de tu aplicación:

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

Si no estás utilizando el framework UNNotification, tendrás que añadir el siguiente código al método `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` de tu aplicación para habilitar el manejo de nuestros botones de acción para notificación push:

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
Recomendamos encarecidamente que quienes utilicen `handleActionWithIdentifier` comiencen a usar el framework `UNNotification`. Lo recomendamos debido a la obsolescencia de [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Personalización de categorías push {#push-category-customization}

Además de proporcionar un conjunto de [categorías push predeterminadas]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons), Braze admite categorías y acciones de notificación personalizadas. Una vez que registres las categorías en tu aplicación, puedes usar el panel de Braze para enviar categorías de notificación a tus usuarios.

Si no estás utilizando el framework `UserNotifications`, consulta la documentación de [categorías alternativas](https://developer.apple.com/documentation/usernotifications/unnotificationcategory).

Estas categorías se pueden asignar a las notificaciones push a través de nuestro panel para activar las configuraciones de botones de acción de tu diseño. Aquí tienes un ejemplo que aprovecha la `LIKE_CATEGORY` mostrada en el dispositivo:

![Un mensaje push mostrando dos botones de acción push "unlike" y "like".]({% image_buster /assets/img_archive/push_example_category.png %})