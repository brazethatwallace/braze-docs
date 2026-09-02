---
nav_title: Notificaciones de reposición de existencias
article_title: Configurar notificaciones de reposición de existencias
page_order: 2
description: "Aprende a configurar notificaciones de reposición de existencias utilizando tu catálogo y eventos personalizados, para que puedas suscribir automáticamente a los clientes para que reciban notificaciones cuando un artículo vuelva a estar disponible."
---

# Notificaciones de reposición de existencias {#back-in-stock-notifications}

> Aprende a configurar notificaciones de reposición de existencias utilizando tu catálogo y eventos personalizados, para que puedas suscribir automáticamente a los clientes para que reciban notificaciones cuando un artículo vuelva a estar disponible. Ten en cuenta que esto solo se aplica a los usuarios que ya han aceptado recibir notificaciones.

## Cómo funciona {#how-it-works}

Puedes configurar un evento personalizado para usarlo como evento de suscripción, como un evento `product_clicked`. Este evento debe contener una propiedad del ID del artículo (IDs de artículos del catálogo). Te sugerimos incluir un nombre de catálogo, pero no es obligatorio. También proporcionarás el nombre de un campo de cantidad de inventario, que debe ser un tipo de dato numérico.

Ten en cuenta que el stock de un artículo del catálogo debe estar en cero para que un usuario pueda suscribirse a él correctamente. Cuando un artículo tiene una cantidad de inventario mayor que cero, Braze buscará a todos los usuarios suscritos a ese artículo y enviará un evento personalizado que puedes usar para desencadenar una Campaign o un Canvas.

Las propiedades del evento se envían junto con tu usuario, por lo que puedes usar plantillas para incluir los detalles del artículo en la Campaign o el Canvas que se envía.

## Configuración de notificaciones de vuelta en existencia {#setting-up-back-in-stock-notifications}

Sigue estos pasos para configurar las notificaciones de vuelta en existencia en un catálogo específico.

1. Ve a tu catálogo y selecciona la pestaña **Configuración**.
2. Selecciona el alternar **Vuelta en existencia**.
3. Si la configuración global de vuelta en existencia no se ha configurado, se te pedirá que configures los eventos personalizados y las propiedades que se utilizarán para desencadenar las notificaciones de vuelta en existencia:
    <br> ![Panel de configuración del catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Catálogo alternativa** Es el catálogo que se utilizará para la suscripción de vuelta en existencia, si no hay una propiedad `catalog_name` presente en el evento personalizado.
    - **Evento personalizado para suscripciones** es el evento personalizado de Braze que se utilizará para suscribir a un usuario a las notificaciones de vuelta en existencia. Cuando ocurra este evento, el usuario que lo realizó quedará suscrito.
    - **Evento personalizado para cancelar suscripción** es el evento personalizado de Braze que se utilizará para cancelar la suscripción de un usuario a las notificaciones de vuelta en existencia. Este evento es opcional. Si el usuario no realiza este evento, se cancelará su suscripción después de 90 días o cuando se desencadene el evento de vuelta en existencia, lo que ocurra primero.
    - **Propiedad del evento de ID de artículo** es la propiedad del evento personalizado mencionado anteriormente en esta sección que se utilizará para determinar el artículo para una suscripción o cancelación de suscripción de vuelta en existencia. Esta propiedad del evento personalizado debe contener un ID de artículo (`id`) que esté presente en un catálogo. El ID del artículo debe enviarse como una cadena para que coincida con el tipo de datos `id` almacenado en el catálogo de destino. El evento personalizado también debe contener una propiedad `catalog_name` para especificar en qué catálogo se encuentra este artículo.

    - El siguiente ejemplo muestra un evento personalizado de muestra enviado a través de la REST or transferencia de estado representacional API:

```json
{
    "events": [
        {
            "external_id": "<external_id>",
            "name": "subscription",
            "time": "2024-04-15T19:22:28Z",
            "properties": {
                "id": "shirt-xl",
                "catalog_name": "on_sale_products",
                "type": ["back_in_stock"]
            }
        }
    ]
}
```

Para rastrear el mismo evento de suscripción usando los SDK or kit de desarrollo de software de Braze, utiliza el siguiente código:

{% tabs %}
{% tab Web SDK or kit de desarrollo de software %}

```javascript
import { logCustomEvent } from "@braze/web-sdk";

logCustomEvent("subscription", {
  id: "shirt-xl",
  catalog_name: "on_sale_products",
  type: ["back_in_stock"]
});
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.logCustomEvent(
  name: "subscription",
  properties: [
    "id": "shirt-xl",
    "catalog_name": "on_sale_products",
    "type": ["back_in_stock"]
  ]
)
```

{% endtab %}
{% tab Android %}

```kotlin
Braze.getInstance(context).logCustomEvent(
  "subscription",
  BrazeProperties(
    JSONObject()
      .put("id", "shirt-xl")
      .put("catalog_name", "on_sale_products")
      .put("type", JSONArray().put("back_in_stock")),
  ),
)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Los desencadenadores de vuelta en existencia y de bajada de precio utilizan el mismo evento para suscribir al usuario a la notificación, por lo que puedes usar la propiedad `type` para configurar tanto las notificaciones de bajada de precio como las de vuelta en existencia en el mismo evento. Ten en cuenta que la propiedad `type` debe ser un arreglo.
{% endalert %}

{: start="4"}
4. Selecciona **Guardar** y continúa a la página de **Configuración** del catálogo.
5. Configura tu regla de notificación. Hay dos opciones:
    - **Notificar a todos los usuarios suscritos** notifica a todos los clientes que están esperando cuando el artículo vuelve a estar en existencia.
    - **Establecer límites de notificación** notifica a un número específico de clientes cada 10 minutos. Braze notificará al número especificado de clientes en incrementos hasta que no haya más clientes que notificar o hasta que el artículo se agote. Tu tasa de notificación no puede exceder la notificación de 10,000 usuarios por minuto.
6. Configura el **Campo de inventario en el catálogo**. Este campo del catálogo se utilizará para determinar si el artículo está agotado. El campo debe ser de tipo numérico.
7. Selecciona **Guardar configuración**.

![Configuración del catálogo que muestra la característica de vuelta en existencia activada. Las reglas de notificación son notificar a mil usuarios cada diez minutos.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Las reglas de notificación en esta configuración no reemplazan la configuración de notificaciones de Canvas, como las horas tranquilas.
{% endalert %}

## Uso de notificaciones de vuelta en existencia en un Canvas {#using-back-in-stock-notifications-in-a-canvas}

Después de configurar la característica de vuelta en existencia en un catálogo, sigue estos pasos para usarla con Canvas.

1. Configura un Canvas basado en acciones.
2. Selecciona **Vuelta en existencia** como desencadenante.
3. Selecciona el nombre del catálogo con las notificaciones de vuelta en existencia.
4. Continúa [configurando]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) tu Canvas como lo harías normalmente.

Ahora, tus clientes pueden recibir notificaciones cuando un artículo vuelva a estar en existencia.

### Uso de Liquid {#using-liquid}

Para incluir detalles sobre el artículo del catálogo que volvió a estar en existencia, puedes usar la etiqueta de Liquid `context` para acceder al `item_id`.

Usar {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} devolverá el ID del artículo que volvió a estar en existencia. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} devolverá el valor de inventario del artículo antes de la actualización, y {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} devolverá el nuevo valor de inventario después de la actualización.

Usa la etiqueta de Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} en la parte superior de tu mensaje, y luego usa {%raw%}``{{ items[0].<field_name> }}``{%endraw%} para acceder a los datos de ese artículo a lo largo del mensaje.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Consideraciones {#considerations}

- Los usuarios solo están suscritos durante 90 días. Si el artículo no vuelve a estar en stock en 90 días, se cancela la suscripción del usuario.
- Al usar la regla de notificación **Notificar a todos los usuarios suscritos**, Braze notificará a 100 000 usuarios en 10 minutos.
- Braze admite hasta 50 000 artículos actualizados diariamente que son elegibles para desencadenar notificaciones de vuelta en stock. Puedes tener hasta 100 millones de suscripciones activas en un momento dado, donde cada suscripción representa un perfil de usuario suscrito para seguir un artículo del catálogo.