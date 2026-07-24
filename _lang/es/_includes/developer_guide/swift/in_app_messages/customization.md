{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configuración del delegado de la interfaz de usuario (obligatorio) {#setting-up-the-ui-delegate-required}

Para personalizar la presentación de los mensajes dentro de la aplicación y reaccionar ante diversos eventos del ciclo de vida, deberás configurar [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). Este es un protocolo delegado que se utiliza para recibir y procesar cargas útiles de mensajes dentro de la aplicación desencadenados, recibir eventos del ciclo de vida de la pantalla y controlar la sincronización de la pantalla. Para utilizar `BrazeInAppMessageUIDelegate`, debes:
- Utilizar la implementación predeterminada [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) como tu `inAppMessagePresenter`.
- Incluir la biblioteca `BrazeUI` en tu proyecto.

### Paso 1: Implementar el protocolo `BrazeInAppMessageUIDelegate` {#step-1-implement-the-brazeinappmessageuidelegate-protocol}

Primero, implementa el protocolo `BrazeInAppMessageUIDelegate` y los métodos correspondientes que desees. En el siguiente ejemplo, este protocolo se implementa en la clase `AppDelegate` de la aplicación.

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### Paso 2: Asignar el objeto `delegate` {#step-2-assign-the-delegate-object}

Asigna el objeto `delegate` en la instancia `BrazeInAppMessageUI` antes de asignar esta interfaz de usuario de mensajes dentro de la aplicación como tu `inAppMessagePresenter`.

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
No todos los métodos de delegado están disponibles en Objective-C debido a la incompatibilidad de sus parámetros con el tiempo de ejecución del lenguaje.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Para una implementación paso a paso del delegado de interfaz de usuario de mensajes dentro de la aplicación, consulta este [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## Comportamiento al hacer clic {#on-click-behavior}

Cada objeto `Braze.InAppMessage` contiene un [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction) correspondiente, que define el comportamiento al hacer clic.

### Tipos de acción de clic {#click-action-types}

La propiedad `clickAction` de tu `Braze.InAppMessage` está predeterminada a `.none`, pero puede ajustarse a uno de los siguientes valores:

| `ClickAction` | Comportamiento al hacer clic |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Abre la URL dada en un navegador externo. Si `useWebView` está configurado en `true`, se abrirá en una vista Web. |
| `.none` | Al hacer clic en el mensaje, este se cerrará. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de acción de clic" }

{% alert important %}
Para los mensajes dentro de la aplicación que contengan botones, el mensaje `clickAction` también se incluirá en la carga útil final si la acción de clic se añade antes de añadir el texto del botón.
{% endalert %}

### Personalización del comportamiento al hacer clic {#customizing-on-click-behavior}

Para personalizar este comportamiento, puedes modificar la propiedad `clickAction` consultando el siguiente ejemplo:

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

El método `inAppMessage(_:prepareWith:)` no está disponible en Objective-C.

{% endtab %}
{% endtabs %}

### Manejo del comportamiento personalizado {#handling-the-custom-behavior}

El siguiente método delegado [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) se invoca cuando un usuario hace clic en un mensaje dentro de la aplicación. Esta devolución de llamada se activa para los clics iniciados por el usuario en los botones de mensajes dentro de la aplicación y en los botones de mensajes HTML dentro de la aplicación (enlaces), y se proporciona un ID de botón como parámetro opcional para estas interacciones. Esta devolución de llamada no se invoca para los clics programáticos desencadenados a través de `brazeBridge.logClick()`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

Este método devuelve un valor booleano para indicar si Braze debe seguir ejecutando la acción de clic.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }

    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Deslizar para descartar mensajes de deslizamiento hacia arriba {#swiping-to-dismiss-slideup-messages}

De forma predeterminada, los mensajes de deslizamiento hacia arriba dentro de la aplicación se pueden descartar con un gesto de deslizamiento. La dirección del deslizamiento depende de la posición del deslizamiento hacia arriba:

- **Deslizar hacia la izquierda o hacia la derecha:** cierra el deslizamiento hacia arriba independientemente de su posición.
- **Deslizamiento hacia arriba desde la parte inferior:** deslizar de arriba abajo descarta el mensaje. Deslizar de abajo hacia arriba no lo cierra.
- **Deslizamiento hacia arriba desde la parte superior:** deslizar de abajo hacia arriba descarta el mensaje. Deslizar de arriba abajo no lo cierra.

Este comportamiento de deslizamiento está integrado en la [`SlideupView`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview) predeterminada de `BrazeInAppMessageUI` y solo se aplica a los mensajes de deslizamiento hacia arriba dentro de la aplicación. Los mensajes modales y de pantalla completa dentro de la aplicación no admiten la función de deslizar para descartar. Para personalizar aún más la vista de deslizamiento hacia arriba, incluido el comportamiento al deslizar, puedes modificar [`SlideupView.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview/attributes-swift.struct) o proporcionar una vista personalizada mediante subclases.

{% alert note %}
Al pulsar fuera de un mensaje de deslizamiento hacia arriba, este no desaparece. Para los mensajes modales o de pantalla completa dentro de la aplicación, puedes habilitar el cierre mediante pulsación externa utilizando el atributo `dismissOnBackgroundTap` que se describe en la siguiente sección.
{% endalert %}

## Personalización de cierres modales {#customizing-modal-dismissals}

Para habilitar los descartes por toque externo, puedes modificar la propiedad `dismissOnBackgroundTap` en la estructura `Attributes` del tipo de mensaje dentro de la aplicación que desees personalizar.

Por ejemplo, si deseas habilitar esta característica para los mensajes dentro de la aplicación con imágenes modales, puedes configurar lo siguiente:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

La personalización a través de `Attributes` no está disponible en Objective-C.

{% endtab %}
{% endtabs %}

El valor predeterminado es `false`. Determina si el mensaje modal dentro de la aplicación se descartará cuando el usuario pulse fuera del mensaje dentro de la aplicación.

| `DismissModalOnOutsideTap` | Descripción |
|----------|-------------|
| `true`         | Los mensajes modales dentro de la aplicación se descartarán al tocar fuera.     |
| `false`        | Predeterminado, los mensajes modales dentro de la aplicación no se descartarán al tocar fuera. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalización de cierres modales" }

Para más detalles sobre la personalización de mensajes dentro de la aplicación, consulta este [artículo](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).

## Personalización de la orientación de los mensajes {#customizing-message-orientation}

Puedes personalizar la orientación de tus mensajes dentro de la aplicación. Puedes establecer una nueva orientación predeterminada para todos los mensajes o establecer una orientación personalizada para un solo mensaje.

{% tabs local %}
{% tab todos los mensajes %}
Para elegir una orientación predeterminada para todos los mensajes dentro de la aplicación, utiliza el método [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) para establecer la propiedad `preferredOrientation` en `PresentationContext`.

Por ejemplo, para establecer el modo vertical como orientación predeterminada:

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab mensaje único %}
Para establecer la orientación de un solo mensaje, modifica la propiedad `orientation` de `Braze.InAppMessage`:

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Después de que se muestre el mensaje dentro de la aplicación, cualquier cambio en la orientación del dispositivo mientras el mensaje sigue mostrándose hará que el mensaje gire con el dispositivo (siempre que lo permita la configuración `orientation` del mensaje).

La orientación del dispositivo también debe ser compatible con la propiedad `orientation` del mensaje dentro de la aplicación para que este se muestre. Además, la configuración de `preferredOrientation` solo se respetará si está incluida en las orientaciones de interfaz admitidas de tu aplicación en la sección **Deployment Info** de la configuración de tu objetivo en Xcode.

![Orientaciones compatibles en Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
La orientación solo se aplica a la presentación del mensaje. Cuando el dispositivo cambia de orientación, la vista de mensajes adopta una de las orientaciones que admite. En dispositivos más pequeños (iPhones, iPod Touch), establecer una orientación horizontal para un mensaje modal o de pantalla completa dentro de la aplicación puede provocar que el contenido quede truncado.
{% endalert %}

## Personalizar el tiempo de visualización {#customizing-display-timing}

Puedes controlar si un mensaje dentro de la aplicación disponible se mostrará durante ciertos momentos de la experiencia de usuario. Si hay situaciones en las que no quieres que aparezca el mensaje dentro de la aplicación, como durante un juego a pantalla completa o en una pantalla de carga, puedes retrasar o descartar los mensajes dentro de la aplicación pendientes. Para controlar la temporización del mensaje dentro de la aplicación, utiliza el [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` para establecer la propiedad `BrazeInAppMessageUI.DisplayChoice`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

Configura `BrazeInAppMessageUI.DisplayChoice` para que devuelva uno de los siguientes valores:

| Opción de visualización                      | Comportamiento                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | El mensaje se mostrará inmediatamente. Este es el valor predeterminado.                                                       |
| `.reenqueue`                        | El mensaje no se mostrará y volverá a colocarse en la parte superior de la pila.                                       |
| `.later`                            | El mensaje no se mostrará y volverá a colocarse en la parte superior de la pila. (Obsoleto, utiliza `.reenqueue`) |
| `.discard`                          | El mensaje se descartará y no se mostrará.                                                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalizar el tiempo de visualización" }

{% alert tip %}
Para ver un ejemplo de `InAppMessageUI`, consulta nuestro [repositorio Swift Braze SDK](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) y [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI).
{% endalert %}

## Ocultar la barra de estado {#hiding-the-status-bar}

Para los mensajes dentro de la aplicación `Full`, `FullImage` y `HTML`, el SDK ocultará la barra de estado de forma predeterminada. Para otros tipos de mensajes dentro de la aplicación, la barra de estado se deja intacta. Para configurar este comportamiento, utiliza el [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` para establecer la propiedad `statusBarHideBehavior` en `PresentationContext`. Este campo toma uno de los siguientes valores:

| Comportamiento de ocultación de la barra de estado            | Descripción                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | La vista de mensajes decide el estado oculto de la barra de estado.                                 |
| `.hidden`                           | Oculta siempre la barra de estado.                                                           |
| `.visible`                          | Muestra siempre la barra de estado.                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ocultar la barra de estado" }

## Desactivar el modo oscuro {#disabling-dark-mode}

Para evitar que los mensajes dentro de la aplicación adopten el estilo de modo oscuro cuando el dispositivo del usuario tiene habilitado el modo oscuro, implementa el [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`. El `PresentationContext` pasado al método contiene una referencia al objeto `InAppMessage` que se va a presentar. Cada `InAppMessage` tiene una propiedad `themes` que contiene un tema de modo `dark` y `light`. Si estableces la propiedad `themes.dark` en `nil`, Braze presentará automáticamente el mensaje dentro de la aplicación utilizando su tema claro.

Los tipos de mensaje dentro de la aplicación con botones tienen un objeto `themes` adicional en su propiedad `buttons`. Para evitar que los botones adopten el estilo de modo oscuro, puedes utilizar [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) para crear una nueva serie de botones con un tema `light` y sin tema `dark`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup

    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal

    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage

    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full

    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage

    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## Personalizar el mensaje de revisión de la tienda de aplicaciones {#customizing-the-app-store-review-prompt}

Puedes utilizar mensajes dentro de la aplicación en una Campaign para pedir a los usuarios que dejen una reseña en la App Store.

{% alert note %}
Dado que este aviso de ejemplo anula el comportamiento predeterminado de Braze, no podemos realizar un seguimiento automático de las impresiones si se implementa. Debes [registrar tus propios análisis]({{site.baseurl}}/developer_guide/analytics).
{% endalert %}

### Paso 1: Configura el delegado de mensajes dentro de la aplicación {#step-1-set-the-in-app-message-delegate}

Primero, configura [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_setting-up-the-ui-delegate-required) en tu aplicación.

### Paso 2: Desactiva el mensaje predeterminado de revisión de la App Store {#step-2-disable-the-default-app-store-review-message}

A continuación, implementa el [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` para desactivar el mensaje predeterminado de revisión de la App Store.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### Paso 3: Crear un vínculo profundo {#step-3-create-a-deep-link}

En tu controlador [`scene:openURLContexts:`]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#swift_step-3-implement-a-handler), añade el siguiente código para procesar el vínculo profundo `{YOUR-APP-SCHEME}:app-store-review`. Ten en cuenta que tendrás que importar `StoreKit` para utilizar `SKStoreReviewController`:

{% tabs %}
{% tab swift %}

```swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let url = URLContexts.first?.url else { return }
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSURL *url = URLContexts.allObjects.firstObject.URL;
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### Paso 4: Establece un comportamiento personalizado al hacer clic {#step-4-set-custom-on-click-behavior}

A continuación, crea una campaña de mensajería dentro de la aplicación con lo siguiente:

- El par clave-valor `"AppStore Review" : "true"`
- El comportamiento al hacer clic configurado a "Vínculo profundo dentro de la aplicación", utilizando el vínculo profundo `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple limita las solicitudes de revisión de la App Store a un máximo de tres veces al año por cada usuario, por lo que tu Campaign debe tener una [tasa limitada]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) a tres veces al año por usuario.<br><br>Los usuarios pueden desactivar los avisos de revisión de la App Store. En consecuencia, tu solicitud de revisión personalizada no debe prometer que aparecerá una solicitud de revisión nativa de la App Store ni pedir directamente una revisión.
{% endalert %}