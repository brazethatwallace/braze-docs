---
nav_title: Comportamiento personalizado al hacer clic
article_title: Personalizar el comportamiento al hacer clic en los mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 5
description: "Este artículo de referencia trata del comportamiento personalizado de la mensajería dentro de la aplicación al hacer clic para tu aplicación de iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personalizar el comportamiento de los mensajes dentro de la aplicación al hacer clic {#customize-in-app-message-behavior-on-click}

La propiedad `inAppMessageClickActionType` de `ABKInAppMessage` define el comportamiento de la acción después de hacer clic en el mensaje dentro de la aplicación. Esta propiedad es de solo lectura. Si quieres cambiar el comportamiento de clic del mensaje dentro de la aplicación, puedes llamar al siguiente método en `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

`inAppMessageClickActionType` puede establecerse en uno de los siguientes valores:

| `ABKInAppMessageClickActionType` | Comportamiento al hacer clic |
| -------------------------- | -------- |
| `ABKInAppMessageRedirectToURI` | La URI dada se mostrará cuando se haga clic en el mensaje, y este se descartará. Ten en cuenta que el parámetro `uri` no puede ser nulo. |
| `ABKInAppMessageNoneClickAction` | Al hacer clic en el mensaje, este se cerrará. Ten en cuenta que el parámetro `uri` se ignorará, y que la propiedad `uri` de `ABKInAppMessage` se establecerá en nulo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalizar el comportamiento de los mensajes dentro de la aplicación al hacer clic" }

{% alert important %}
Para los mensajes dentro de la aplicación que contengan botones, el `clickAction` del mensaje también se incluirá en la carga útil final si la acción de clic se añade antes de añadir el texto del botón.
{% endalert %}

## Personalizar los clics del cuerpo de los mensajes dentro de la aplicación {#customizing-in-app-message-body-clicks}

El siguiente método delegado de [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) se llama cuando se hace clic en un mensaje dentro de la aplicación:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## Personalizar los clics de los botones de mensajes dentro de la aplicación {#customizing-in-app-message-button-clicks}

Para los clics en botones de mensajes dentro de la aplicación y botones de mensajes HTML dentro de la aplicación (como enlaces), [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) incluye los siguientes métodos delegados:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Cada método devuelve un valor `BOOL` para indicar si Braze debe seguir ejecutando la acción de clic.

Para acceder al tipo de acción de clic de un botón en un método delegado, puedes utilizar el siguiente código:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

Cuando un mensaje dentro de la aplicación tiene botones, las únicas acciones de clic que se ejecutarán son las del modelo `ABKInAppMessageButton`. El cuerpo del mensaje dentro de la aplicación no será clicable, aunque al modelo `ABKInAppMessage` se le haya asignado la acción de clic predeterminada.

## Declaraciones de métodos {#method-declarations}

Para más información, consulta los siguientes archivos de encabezado:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)