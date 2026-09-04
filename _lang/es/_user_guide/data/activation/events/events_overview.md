---
nav_title: Eventos
article_title: Eventos
page_order: 0
hidden: true
page_type: reference
description: "Este artículo describe los diferentes eventos en Braze: eventos estándar, eventos de compra y eventos personalizados, así como su propósito."
---

# Eventos {#events}

> Esta página cubre los diferentes eventos en Braze y su propósito.

Braze utiliza varios tipos de eventos para proporcionar una comprensión integral del comportamiento del usuario y su interacción con tu marca. Cada tipo de evento cumple un propósito único:

- [Eventos estándar](#standard-events): proporcionan una comprensión básica de la interacción del usuario con tu aplicación o sitio.
- [Eventos de compra](#purchase-events): son cruciales para entender el comportamiento de compra del usuario y para el seguimiento de ingresos.
- [Eventos personalizados](#custom-events): proporcionan información más profunda sobre comportamientos del usuario que son únicos de tu aplicación o empresa.

Al hacer seguimiento de estos diferentes tipos de eventos, puedes obtener una comprensión más profunda de tus usuarios, lo que puede informar tus estrategias de marketing, ayudarte a optimizar tu aplicación y permitirte ofrecer una experiencia de usuario más personalizada. ¡Vamos a ello!

## Eventos estándar {#standard-events}

En Braze, los eventos estándar son acciones predefinidas que Braze reconoce en toda su plataforma. A diferencia de los [eventos personalizados](#custom-events), no necesitas crear ni nombrar los eventos estándar, ya que están integrados. Sin embargo, no todos los eventos estándar se rastrean de la misma manera.

Los siguientes eventos se rastrean automáticamente después de la integración del SDK:

- Inicio de sesión
- Fin de sesión

Los siguientes eventos se rastrean después de una configuración adicional:

- [Eventos de compra](#purchase-events): tu equipo de desarrollo los registra usando los métodos de compra del SDK. Para más información, consulta la sección de eventos de compra.
- Eventos de interacción con correo electrónico (como aperturas de correo electrónico y clics en enlaces): Braze los rastrea cuando configuras el correo electrónico de Braze y habilitas el seguimiento de correo electrónico.
- Eventos de interacción push (como aperturas de notificaciones push y clics): se rastrean después de configurar push en Braze e integrar el manejo de push con el SDK de Braze en tu aplicación.

Como especialista en marketing, puedes usar los eventos estándar para entender el comportamiento y la interacción del usuario. Por ejemplo, los datos de sesión muestran con qué frecuencia los usuarios abren tu aplicación o sitio, mientras que los eventos de compra te ayudan a rastrear los ingresos a lo largo del tiempo.

## Eventos de compra {#purchase-events}

Los eventos de compra registran y rastrean las compras realizadas por tus usuarios. Después de integrar el SDK de Braze, tu equipo de desarrollo puede registrar compras usando los métodos de compra del SDK. Cuando usas eventos de compra para rastrear compras, puedes monitorear tus ingresos a lo largo del tiempo y a través de diferentes fuentes de ingresos directamente desde Braze.

Los eventos de compra registran la siguiente información clave sobre una compra:

- ID del producto (generalmente el nombre o categoría del producto)
- Moneda
- Precio
- Cantidad

Luego puedes usar estos datos para segmentar a tus usuarios según su LTV, frecuencia de compra, compras específicas y más.

Braze también admite compras en múltiples monedas. Si una compra se reporta en una moneda distinta a USD, se mostrará en el dashboard en USD, basándose en el tipo de cambio de la fecha en que se reportó la compra.

Para obtener más información, visita nuestro artículo dedicado sobre [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).

{% details Ejemplo de implementación %}

Ten en cuenta que la implementación real de los eventos de compra requerirá algunos conocimientos técnicos, ya que implica integrar el SDK de Braze con tu aplicación. Tu administrador del éxito del cliente guiará a tu equipo a través de este proceso como parte de tu incorporación, pero los pasos generales son los siguientes:

1. **Integra el SDK de Braze:** antes de registrar cualquier evento, necesitas integrar el SDK de Braze en tu aplicación.
2. **Registra el evento de compra:** después de integrar el SDK, puedes registrar un evento de compra cada vez que un usuario realice una compra en tu aplicación. Esto se hace típicamente en la función o método que se llama cuando se completa una compra.

Aquí tienes un ejemplo de cómo registrar un evento de compra en una aplicación iOS usando Swift:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

En este ejemplo, "product_name" es el nombre del producto que se compró, "USD" es la moneda de la compra, "1.99" es el precio del producto y "1" es la cantidad comprada.

{:start="3"}
3. **Visualiza el evento de compra en el dashboard:** después de registrar el evento de compra, puedes verlo en el dashboard. Puedes usar estos datos para analizar tus ingresos, segmentar a tus usuarios y más.

Recuerda que la implementación exacta puede variar dependiendo de la plataforma (iOS, Android, Web) y los requisitos específicos de tu aplicación.

{% enddetails %}

## Eventos personalizados {#custom-events}

Los eventos personalizados son eventos que defines en función de las acciones específicas que deseas rastrear dentro de tu aplicación o sitio. Braze no los rastrea automáticamente; debes configurar manualmente estos eventos en tu implementación del SDK de Braze. Los eventos personalizados pueden ser cualquier cosa, desde que un usuario complete un nivel en un juego hasta que actualice su información de perfil.

Aquí tienes un ejemplo de cómo registrar un evento personalizado en una aplicación iOS usando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

En este ejemplo, "completed_level" es el nombre del evento personalizado que se registra cuando un usuario completa un nivel en un juego. Ese evento personalizado se registra entonces en su perfil de usuario en Braze, que puedes usar para desencadenar campañas y personalizar la mensajería.

Para obtener más información, visita nuestro artículo dedicado sobre [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events).

{% details Ejemplo de implementación %}

Al igual que los eventos de compra, los eventos personalizados requieren configuración adicional. Aquí tienes un proceso general para implementar eventos personalizados en Braze:

1. **Integra el SDK de Braze:** antes de poder registrar cualquier evento, necesitas integrar el SDK de Braze en tu aplicación.
2. **Define tu evento personalizado:** decide qué acción en tu aplicación deseas rastrear como evento personalizado. Puede ser cualquier cosa significativa para tu aplicación, como que un usuario complete un nivel en un juego, actualice su perfil o realice un tipo específico de compra.
3. **Registra el evento personalizado:** después de definir tu evento personalizado, puedes registrarlo en el código de tu aplicación. Esto se hace típicamente en la función o método que se llama cuando ocurre la acción.

Aquí tienes un ejemplo de cómo registrar un evento personalizado en una aplicación iOS usando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

En este ejemplo, "updated_profile" es el nombre del evento personalizado que se registra cuando un usuario actualiza su perfil.

{:start="4"}
4. **Agrega propiedades a tu evento personalizado (opcional):** si deseas capturar detalles adicionales sobre el evento personalizado, puedes agregarle propiedades. Esto se hace pasando un diccionario de propiedades cuando registras el evento.

Aquí tienes un ejemplo de cómo registrar un evento personalizado con propiedades en una aplicación iOS usando Swift:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

En este ejemplo, el evento personalizado tiene una propiedad llamada "Property Name" con un valor de "Property Value".

{:start="5"}
5. **Visualiza el evento personalizado en el dashboard:** después de registrar el evento personalizado, puedes verlo en el dashboard. Puedes usar estos datos para analizar el comportamiento del usuario, segmentar a tus usuarios y más.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->