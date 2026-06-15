---
nav_title: Actualización de usuario
article_title: Actualización de usuario
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Este artículo de referencia cubre el componente Actualización de usuario y cómo usarlo en tus Canvas."
tool: Canvas
---

# Actualización de usuario

> El componente Actualización de usuario te permite actualizar los atributos, eventos y compras de un usuario en un editor JSON, por lo que no es necesario incluir información sensible como claves de API.

## Cómo funciona este componente

![Un paso de Actualización de usuario llamado "Update loyalty" que actualiza un atributo "Is Premium Member" a "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Cuando usas este componente en tu Canvas, las actualizaciones no cuentan para tu límite de velocidad de solicitudes por minuto de `/users/track`. En su lugar, estas actualizaciones se agrupan en lotes para que Braze pueda procesarlas de forma más eficiente que un webhook de Braze a Braze. Ten en cuenta que este componente no registra [puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) cuando se usa para actualizar puntos de datos no facturables (como grupos de suscripción).

Después de que los usuarios entran en el paso de Actualización de usuario y se completa el procesamiento, avanzan al siguiente paso. Esto significa que cualquier mensaje posterior que dependa de estas actualizaciones de usuario estará al día cuando se ejecute el siguiente paso.

## Crear una actualización de usuario

Arrastra y suelta el componente desde la barra lateral, o selecciona el botón de <i class="fas fa-plus-circle"></i> más en la parte inferior de la variante o paso y selecciona **Actualización de usuario**.

Hay tres opciones que te permiten actualizar la información existente del perfil de usuario, añadir nueva información o eliminar información del perfil de usuario. En conjunto, los pasos de Actualización de usuario en un espacio de trabajo pueden actualizar hasta 200 000 perfiles de usuario por minuto.

{% alert tip %}
También puedes probar los cambios realizados con este componente buscando un usuario y aplicándole el cambio. Esto actualizará al usuario.
{% endalert %}

## Actualizar atributos personalizados

Para actualizar o eliminar un atributo personalizado, selecciona un nombre de atributo de tu lista de atributos e introduce el valor.

![Paso de Actualización de usuario que actualiza los dos atributos "Loyalty Member" y "Loyalty Program" a "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Eliminar atributos personalizados

Para eliminar un atributo personalizado, selecciona un nombre de atributo usando el menú desplegable. Puedes cambiar al [editor JSON avanzado](#advanced-json-editor) para editar más.

![Paso de Actualización de usuario que elimina un atributo "Loyalty Member".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Incrementar y decrementar valores

El paso de Actualización de usuario puede incrementar o decrementar el valor de un atributo. Selecciona el atributo, selecciona **Incrementar en** o **Decrementar en** e introduce un número.

#### Seguimiento del progreso semanal

Al incrementar un atributo personalizado que rastrea un evento, puedes hacer seguimiento del número de clases que un usuario ha tomado en una semana. Usando este componente, el conteo de clases puede reiniciarse al inicio de la semana y comenzar a rastrear de nuevo.

![Paso de Actualización de usuario que incrementa el atributo "class_count" en uno.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Actualizar un array de objetos

Un [array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/) es un atributo personalizado rico en datos almacenado en el perfil de un usuario. Puedes usarlo para crear un historial de las interacciones del usuario con tu marca y para crear segmentos basados en un campo calculado, como el historial de compras o el valor de duración del ciclo de vida total.

Usando la opción **Editor JSON avanzado**, puedes insertar JSON para añadir o eliminar elementos de este array de objetos.

#### Caso de uso: Actualizar la lista de deseos de un usuario

Haz seguimiento de la lista de deseos de un usuario para que puedas segmentar o personalizar en función de sus artículos guardados.

1. Crea un atributo personalizado que sea un array de objetos, por ejemplo `wishlist`. Cada objeto puede incluir campos como `product_id`, `product_name` y `added_at`.
2. En el paso de Actualización de usuario, selecciona **Editor JSON avanzado**. Luego, en la sección **Redactar**, usa la operación `$add` para añadir un elemento o la operación `$remove` para eliminar un elemento por valor.

El siguiente es un ejemplo de cómo añadir un elemento a la lista de deseos:

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

Para eliminar un elemento, usa `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` con la misma estructura de objeto para que Braze pueda encontrarlo y eliminarlo.

#### Caso de uso: Calcular el total del carrito de compras

Haz seguimiento de cuándo un usuario tiene artículos en su carrito de compras, cuándo añade nuevos artículos o elimina artículos, y cuál es el valor total del carrito de compras.

1. Crea un array personalizado de objetos llamado `shopping_cart`. El siguiente ejemplo muestra cómo podría verse este atributo. Cada artículo tiene un `product_id` único que tiene datos adicionales en su propio array anidado de objetos, incluyendo `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2. Crea un [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) llamado `add_item_to_cart` que se registre cuando un usuario añade un artículo al carrito.
3. Crea un Canvas que se dirija a los usuarios que realizan este evento personalizado. Ahora, cuando un usuario añade un artículo a su carrito, se desencadena este Canvas. Luego puedes dirigir mensajes directamente a ese usuario, ofreciendo códigos de cupón cuando haya alcanzado un cierto gasto, haya abandonado su carrito durante un cierto período de tiempo, o cualquier otra cosa que se alinee con tu caso de uso.

El atributo `shopping_cart` contiene el total de muchos eventos personalizados: el costo total de todos los artículos, el número total de artículos en el carrito, si el carrito de compras contiene un regalo, y más. Esto puede verse algo así:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"],
         "gift": true,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Establecer una propiedad de entrada de Canvas como atributo

Puedes usar el paso de Actualización de usuario para persistir una `canvas_entry_property`. Supongamos que tienes un evento que se desencadena cuando se añade un artículo a un carrito. Puedes almacenar el ID del artículo más reciente añadido al carrito y usarlo para una campaña de remarketing. Usa la función de personalización para recuperar una propiedad de entrada de Canvas y almacenarla en un atributo.

![Paso de Actualización de usuario que actualiza el atributo "most_recent_cart_item" con un ID de artículo.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalización

Para almacenar la propiedad del evento desencadenante de un Canvas como atributo, usa el modal de personalización para extraer y almacenar la propiedad de entrada de Canvas. Actualización de usuario también admite las siguientes funciones de personalización:

* [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)
* [Bloques de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)
* [Propiedades de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/)
* Lógica de Liquid (incluyendo [cancelar mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/))
* Múltiples actualizaciones de atributos o eventos por objeto

{% alert warning %}
Recomendamos usar con cuidado la personalización de Liquid con Contenido conectado en los pasos de Actualización de usuario, ya que este tipo de paso tiene un límite de velocidad de 200 000 solicitudes por minuto. Este límite de velocidad anula el límite de velocidad de Canvas.
{% endalert %}

## Editor JSON avanzado

Añade un objeto JSON de atributo, evento o compra de hasta 65 536 caracteres al editor JSON. También se puede establecer el estado de [suscripción global]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) y de [grupo de suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) de un usuario.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Usando el editor JSON, también puedes previsualizar y probar que el perfil de usuario se actualiza con tus cambios en la pestaña **Vista previa y prueba**. Puedes seleccionar un usuario aleatorio o buscar un usuario específico. Luego, después de enviar una prueba a un usuario, visualiza el perfil de usuario usando el enlace generado.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Consideraciones

No necesitas incluir datos sensibles como tu clave de API al usar el editor JSON, ya que la plataforma los proporciona automáticamente. Los siguientes campos no deben incluirse en el editor JSON:
* ID de usuario externo
* Clave de API
* URL del clúster de Braze
* Campos relacionados con importaciones de tokens de notificaciones push

{% alert important %}
Las propiedades de Canvas (como las etiquetas de Liquid `canvas_id`, `canvas_name` y `canvas_variant_name`) no son compatibles con los pasos de Actualización de usuario.
{% endalert %}

{% raw %}
### Registrar eventos personalizados

Usando el editor JSON, también puedes registrar eventos personalizados. Ten en cuenta que esto requiere una marca de tiempo en formato ISO, por lo que es necesario asignar una hora y fecha con Liquid al principio. Considera este ejemplo que registra un evento con una hora.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

Este siguiente ejemplo vincula un evento a una aplicación específica usando un evento personalizado con propiedades opcionales y el `app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Editar el estado de suscripción

Dentro del editor JSON, también puedes editar el estado de suscripción de un usuario. Por ejemplo, lo siguiente muestra el estado de suscripción de un usuario actualizado a `opted_in`.

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Actualizar grupos de suscripción

También puedes actualizar grupos de suscripción usando este paso en Canvas. El siguiente ejemplo muestra cómo actualizar uno o más grupos de suscripción.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}