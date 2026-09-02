---
nav_title: Actualización de usuario
article_title: Actualización de usuario
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Este artículo de referencia cubre el componente Actualización de usuario y cómo usarlo en tus Canvas."
tool: Canvas
---

# Actualización de usuario {#user-update}

> El componente Actualización de usuario te permite actualizar los atributos, eventos y compras de un usuario en un editor JSON, por lo que no es necesario incluir información sensible como claves de API.

## Cómo funciona este componente {#how-this-component-works}

![Un paso de actualización de usuario llamado "Update loyalty" que actualiza un atributo "Is Premium Member" a "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Cuando usas este componente en tu Canvas, las actualizaciones no cuentan para tu límite de velocidad de solicitudes por minuto de `/users/track`. En su lugar, estas actualizaciones se agrupan en lotes para que Braze pueda procesarlas de forma más eficiente que un webhook de Braze a Braze. Ten en cuenta que este componente no registra [puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points) cuando se utiliza para actualizar puntos de datos no facturables (como los grupos de suscripción).

Después de que los usuarios entran en el paso de actualización de usuario y se completa el procesamiento, avanzan al siguiente paso. Esto significa que cualquier mensajería posterior que dependa de estas actualizaciones de usuario estará al día cuando se ejecute el siguiente paso.

## Creación de una actualización de usuario {#creating-a-user-update}

Arrastra y suelta el componente desde la barra lateral, o selecciona el botón de signo más <i class="fas fa-plus-circle"></i> en la parte inferior de la variante o paso y selecciona **User Update**.

Hay tres opciones que te permiten actualizar la información existente del perfil de usuario, añadir información nueva o eliminar información del perfil de usuario. En conjunto, los pasos de User Update en un espacio de trabajo pueden actualizar hasta 200 000 perfiles de usuario por minuto.

{% alert tip %}
También puedes probar los cambios realizados con este componente buscando un usuario y aplicándole el cambio. Esto actualizará al usuario.
{% endalert %}

## Actualización de atributos personalizados {#updating-custom-attributes}

Para actualizar o eliminar un atributo personalizado, selecciona un nombre de atributo de tu lista de atributos e introduce el valor.

![Paso de actualización de usuario que actualiza los dos atributos "Loyalty Member" y "Loyalty Program" a "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Eliminar atributos personalizados {#removing-custom-attributes}

Para eliminar un atributo personalizado, selecciona un nombre de atributo con el menú desplegable. Puedes cambiar al [editor JSON avanzado](#advanced-json-editor) para seguir editando.

![Paso de actualización de usuario que elimina un atributo "Loyalty Member".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Aumentar y disminuir valores {#increasing-and-decreasing-values}

El paso de actualización de usuario puede aumentar o disminuir el valor de un atributo. Selecciona el atributo, selecciona **Increment By** o **Decrement By** e introduce un número.

#### Seguimiento del progreso semanal {#track-weekly-progress}

Al incrementar un atributo personalizado que hace seguimiento de un evento, puedes rastrear el número de clases que un usuario ha tomado en una semana. Con este componente, el recuento de clases puede reiniciarse al inicio de la semana y comenzar a hacer seguimiento de nuevo.

![Paso de actualización de usuario que incrementa el atributo "class_count" en uno.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Actualizar una matriz de objetos {#updating-an-array-of-objects}

Una [matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) es un atributo personalizado rico en datos almacenado en el perfil de un usuario. Puedes usarla para crear un historial de las interacciones del usuario con tu marca y para crear segmentos basados en un campo calculado, como el historial de compras o el LTV total.

Con la opción **Advanced JSON Editor**, puedes insertar JSON para añadir o eliminar elementos de esta matriz de objetos.

#### Caso de uso: actualizar la lista de deseos de un usuario {#use-case-updating-a-users-wishlist}

Haz seguimiento de la lista de deseos de un usuario para que puedas segmentar o personalizar en función de sus artículos guardados.

1. Crea un atributo personalizado que sea una matriz de objetos, por ejemplo `wishlist`. Cada objeto puede incluir campos como `product_id`, `product_name` y `added_at`.
2. En el paso de actualización de usuario, selecciona **Advanced JSON Editor**. A continuación, en la sección **Compose**, usa la operación `$add` para añadir un elemento o la operación `$remove` para eliminar un elemento por valor.

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

#### Caso de uso: calcular el total del carrito de compras {#use-case-calculating-the-shopping-cart-total}

Haz seguimiento de cuándo un usuario tiene artículos en su carrito de compras, cuándo añade nuevos artículos o los elimina, y cuál es el valor total del carrito de compras.

1. Crea una matriz personalizada de objetos llamada `shopping_cart`. El siguiente ejemplo muestra cómo puede verse este atributo. Cada artículo tiene un `product_id` único que contiene datos adicionales en su propia matriz anidada de objetos, incluyendo `price`.

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
2. Crea un [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) llamado `add_item_to_cart` que se registre cuando un usuario añade un artículo a la cesta.
3. Crea un Canvas que se dirija a los usuarios que realizan este evento personalizado. Ahora, cuando un usuario añade un artículo a su carrito, este Canvas se activa. Luego puedes dirigir la mensajería directamente a ese usuario, ofreciendo códigos de cupón cuando alcance un gasto determinado, abandone su carrito durante cierto tiempo, o cualquier otra acción que se alinee con tu caso de uso.

El atributo `shopping_cart` contiene el total de muchos eventos personalizados: el coste total de todos los artículos, el número total de artículos en el carrito, si el carrito de compras contiene un regalo, y más. Esto puede verse algo así:

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

## Configurar la propiedad de entrada de Canvas como un atributo {#setting-canvas-entry-property-as-an-attribute}

Puedes usar el paso de actualización de usuario para conservar una `canvas_entry_property`. Supongamos que tienes un evento que se desencadena cuando se añade un artículo al carrito. Puedes almacenar el ID del artículo más reciente añadido al carrito y utilizarlo para una campaña de remarketing. Usa la característica de personalización para recuperar una propiedad de entrada de Canvas y almacenarla en un atributo.

![Paso de actualización de usuario que actualiza el atributo "most_recent_cart_item" con un ID de artículo.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalización {#personalization}

Para almacenar la propiedad del evento desencadenante de un Canvas como un atributo, usa el modal de personalización para extraer y almacenar la propiedad de entrada de Canvas. La actualización de usuario también es compatible con las siguientes características de personalización:

* [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
* [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
* [Propiedades de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)
* Lógica de Liquid (incluida la [cancelación de mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages))
* Múltiples actualizaciones de atributos o eventos por objeto

{% alert warning %}
Recomendamos usar con precaución la personalización con Liquid de contenido conectado en los pasos de actualización de usuario, ya que este tipo de paso tiene un límite de velocidad de 200 000 solicitudes por minuto. Este límite de velocidad anula el límite de velocidad de Canvas.
{% endalert %}

## Editor JSON avanzado {#advanced-json-editor}

Añade un objeto JSON de atributo, evento o compra de hasta 65 536 caracteres al editor JSON. También se puede configurar el estado de la [suscripción global]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) y del [grupo de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups) de un usuario.

![Añade un objeto JSON de atributo, evento o compra de hasta 65 536 caracteres al editor JSON. También se puede configurar el estado de la suscripción global y del grupo de suscripción de un usuario.]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Con el editor JSON, también puedes previsualizar y probar que el perfil de usuario se actualice con tus cambios en la pestaña **Vista previa y prueba**. Puedes seleccionar un usuario aleatorio o buscar un usuario específico. Después de enviar una prueba a un usuario, consulta el perfil de usuario mediante el enlace generado.

![Con el editor JSON, también puedes previsualizar y probar que el perfil de usuario se actualice con tus cambios en la pestaña Vista previa y prueba. Puedes seleccionar un usuario aleatorio o buscar un usuario específico. Después de enviar una prueba a un usuario, consulta el perfil de usuario mediante el enlace generado.]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Consideraciones {#considerations}

No necesitas incluir datos confidenciales como tu clave de API al usar el editor JSON, ya que la plataforma los proporciona automáticamente. Los siguientes campos no deben incluirse en el editor JSON:
* ID de usuario externo
* Clave de API
* URL del clúster de Braze
* Campos relacionados con la importación de tokens de notificaciones push

{% alert important %}
Las propiedades de Canvas (como las etiquetas de Liquid `canvas_id`, `canvas_name` y `canvas_variant_name`) no son compatibles con los pasos de actualización de usuario.
{% endalert %}

{% raw %}
### Registrar eventos personalizados {#log-custom-events}

Con el editor JSON, también puedes registrar eventos personalizados. Ten en cuenta que esto requiere una marca de tiempo en formato ISO, por lo que es necesario asignar una hora y fecha con Liquid al principio. Considera este ejemplo que registra un evento con una hora.

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

El siguiente ejemplo vincula un evento a una aplicación específica mediante un evento personalizado con propiedades opcionales y el `app_id`.

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

### Editar el estado de suscripción {#edit-subscription-state}

Dentro del editor JSON, también puedes editar el estado de suscripción de un usuario. Por ejemplo, a continuación se muestra el estado de suscripción de un usuario actualizado a `opted_in`.

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Actualizar grupos de suscripción {#update-subscription-groups}

También puedes actualizar grupos de suscripción con este paso en Canvas. El siguiente ejemplo muestra cómo actualizar uno o más grupos de suscripción.

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