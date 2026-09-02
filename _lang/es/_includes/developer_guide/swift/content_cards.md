## Requisitos previos {#prerequisites}

Antes de poder usar Content Cards, necesitas integrar el [SDK or kit de desarrollo de software de Braze Swift]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) en tu aplicación. Sin embargo, no es necesaria ninguna configuración adicional.

## Contextos de controlador de vista {#view-controller-contexts}

La interfaz de usuario predeterminada de Content Cards puede integrarse desde la biblioteca `BrazeUI` del SDK or kit de desarrollo de software de Braze. Crea el controlador de vista de Content Cards utilizando la instancia `braze`. Si deseas interceptar y reaccionar al ciclo de vida de la interfaz de usuario de Content Cards, implementa [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) como delegado de tu `BrazeContentCardUI.ViewController`.

{% alert note %}
Para más información sobre las opciones del controlador de vista de iOS, consulta la [documentación para desarrolladores de Apple](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

La biblioteca `BrazeUI` del SDK or kit de desarrollo de software de Swift proporciona dos contextos predeterminados de controlador de vista: [navegación](#swift_navigation) o [modal](#swift_modal). Esto significa que puedes integrar Content Cards en estos contextos añadiendo unas pocas líneas de código a tu aplicación o sitio web. Ambas vistas ofrecen opciones de personalización y estilo, como se describe en la [guía de personalización]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios). También puedes crear un controlador de vista de tarjeta de contenido personalizado, en lugar de utilizar el estándar de Braze, para tener aún más opciones de personalización&#8212;consulta el [tutorial sobre la interfaz de usuario de Content Cards](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) para ver un ejemplo.

{% alert important %}
Para manejar Content Cards con variantes de control en tu interfaz de usuario personalizada, pasa tu objeto [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) y llama al método `logImpression` como harías con cualquier otro tipo de tarjeta de contenido. El objeto registrará implícitamente una impresión de control para informar a nuestros análisis de cuándo un usuario habría visto la tarjeta de control.
{% endalert %}

### Navegación {#navigation}

Un controlador de navegación es un controlador de vistas que gestiona uno o varios controladores de vistas hijos en una interfaz de navegación. A continuación se muestra un ejemplo de cómo hacer push de una instancia de `BrazeContentCardUI.ViewController` en un controlador de navegación:

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

### Modal

Utiliza presentaciones modales para crear interrupciones temporales en el flujo de trabajo de tu aplicación, como solicitar al usuario información importante. Esta vista modal tiene una barra de navegación en la parte superior y un botón **Done** en el lateral de la barra. A continuación se muestra un ejemplo de cómo presentar una instancia de `BrazeContentCard.ViewController` en un controlador modal:

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

Para ver ejemplos de uso de los controladores de vista `BrazeUI`, consulta los ejemplos de interfaz de usuario de Content Cards correspondientes en nuestra [aplicación de ejemplos](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Modelo de tarjeta base {#base-card-model}

El modelo de datos de Content Cards está disponible en el módulo `BrazeKit` del SDK or kit de desarrollo de software de Braze Swift. Este módulo contiene los siguientes tipos de Content Cards, que son una implementación del tipo `Braze.ContentCard`. Para obtener una lista completa de las propiedades de Content Cards y su uso, consulta la [clase `ContentCard`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

- Solo imagen
- Imagen con subtítulo
- Clásica
- Imagen clásica
- Control

Para acceder al modelo de datos de Content Cards, llama a `contentCards.cards` en tu instancia `braze`. Consulta [Registro de análisis]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) para obtener más información sobre cómo suscribirte a los datos de las tarjetas.

{% alert note %}
La lectura de `contentCards.cards`, `contentCards.unviewedCards` o `contentCards.lastUpdate` bloquea el hilo que realiza la llamada hasta que el SDK or kit de desarrollo de software haya completado sus operaciones posteriores a la inicialización. Para contextos en el hilo principal o sensibles a la latencia, utiliza las alternativas no bloqueantes [`getCachedContentCards(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getcachedcontentcards(_:)), [`getUnviewedCards(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getunviewedcards(_:)) o [`getLastUpdate(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getlastupdate(_:)).
{% endalert %}

{% alert note %}
Ten en cuenta que `BrazeKit` ofrece una clase alternativa [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) para compatibilidad con Objective-C.
{% endalert %}

## Métodos de tarjeta {#card-methods}

Cada tarjeta se inicializa con un objeto `Context`, que contiene varios métodos para gestionar el estado de tu tarjeta. Llama a estos métodos cuando quieras modificar la propiedad de estado correspondiente en un objeto tarjeta concreto.

| Método | Descripción |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()` | Registra el evento de impresión de la tarjeta de contenido. |
| `card.context?.logClick()` | Registra el evento de clic de la tarjeta de contenido. |
| `card.context?.processClickAction()` | Procesa una entrada [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) determinada. |
| `card.context?.logDismissed()` | Registra el evento de tarjeta de contenido descartada. |
| `card.context?.logError()` | Registra un error relacionado con la tarjeta de contenido. |
| `card.context?.loadImage()` | Carga una imagen de tarjeta de contenido determinada desde una URL. Este método puede ser nulo cuando la tarjeta de contenido no tiene imagen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de tarjeta" }

Para más detalles, consulta la [documentación de la clase `Context`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)