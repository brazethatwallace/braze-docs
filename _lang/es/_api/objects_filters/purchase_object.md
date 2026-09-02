---
nav_title: "Objeto de compra"
article_title: "Objeto de compra"
page_order: 8
page_type: reference
description: "Este artículo de referencia explica los distintos componentes de un objeto de compra, cómo utilizarlo correctamente y ejemplos en los que inspirarse."
---

# Objeto de compra {#purchase-object}

> Este artículo explica los distintos componentes de un objeto de compra, cómo utilizarlo correctamente, las mejores prácticas y ejemplos en los que inspirarse.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## ¿Qué es un objeto de compra? {#what-is-a-purchase-object}

Un objeto de compra es un objeto que se transmite a través de la API cuando se ha realizado una compra. Cada objeto de compra se encuentra dentro de una matriz de compras, y cada objeto representa una compra individual realizada por un usuario concreto en un momento determinado. El objeto de compra tiene muchos campos diferentes que permiten al backend de Braze almacenar y utilizar esta información para la personalización, la recopilación de datos y la personalización.

### Cuerpo del objeto {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

{% alert note %}
Las compras con marcas de tiempo en el futuro se asignan de forma predeterminada a la hora actual. Esto garantiza que los eventos de compra se registren con una temporización precisa.
{% endalert %}

- [ID de usuario externo]({{site.baseurl}}/api/basics#user-ids)
- [Identificador de aplicación]({{site.baseurl}}/api/identifier_types)
- [Wiki de códigos de divisa ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)
- [Wiki de códigos de tiempo ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Algunos pares de identificadores no se pueden utilizar juntos, y `email` tiene prioridad sobre `phone` cuando se proporcionan ambos. Para obtener todos los detalles, consulta [Resolución de identificadores]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).
{% endalert %}

## ID de producto de compra {#purchase-product-id}

Dentro del objeto de compra, el `product_id` es un identificador para la compra (como `Product Name` o `Product Category`):

- Braze te permite almacenar hasta 5000 `product_id` en el panel.
- El `product_id` puede tener hasta 255 caracteres.

### Convenciones de nomenclatura {#naming-conventions}

En Braze, ofrecemos algunas convenciones generales de nomenclatura para el `product_id` del objeto de compra. Al elegir el `product_id`, Braze sugiere usar nombres sencillos como el nombre del producto o la categoría del producto (en lugar de SKU) con la intención de agrupar todos los artículos registrados por este `product_id`.

Esto facilita la identificación de productos para la segmentación y la activación.

### Registrar compras a nivel de pedido {#log-purchases-at-the-order-level}

Si quieres registrar compras a nivel de pedido en lugar de a nivel de producto, puedes usar el nombre del pedido o la categoría del pedido como `product_id` (como `Online Order` o `Completed Order`).

Por ejemplo, para registrar compras a nivel de pedido en el SDK or kit de desarrollo de software Web:

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## Objeto de propiedades de compra {#purchase-properties-object}

{% include data_activation/purchase_event_property_data_types.md %}

Para una referencia consolidada de los tipos de datos en atributos personalizados, propiedades del evento y catálogos, consulta [Tipos de datos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#purchase-event-property-data-types).

### Propiedades de la compra {#purchase-properties}

[Las propiedades de la compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) pueden utilizarse para desencadenar mensajes y para la personalización mediante Liquid, permitiéndote también segmentar en función de estas propiedades.

{% include data_activation/segmentable_purchase_properties_keys_note.md %}

#### Convenciones de denominación

Es importante tener en cuenta que esta característica se activa **por producto**, no por compra. Por ejemplo, si tienes un gran volumen de productos distintos, pero todos tienen las mismas propiedades, la segmentación puede resultar innecesaria.

En este caso, recomendamos utilizar nombres de productos a «nivel de grupo» en lugar de identificadores a nivel de transacción al configurar las estructuras de datos. Por ejemplo, una empresa de billetes de tren debería tener productos para "viaje de ida", "viaje de vuelta", "multiciudad", y no transacciones específicas como "transacción 123" o "transacción 046". Como otro ejemplo, con el evento de compra «comida», lo mejor sería establecer las propiedades como «pastel» y «sándwich».

{% alert important %}
Ten en cuenta que los productos se pueden añadir a través de la REST or transferencia de estado representacional API de Braze. Por ejemplo, si envías una llamada al endpoint `/users/track` e incluyes un nuevo ID de compra, Braze crea automáticamente un producto en la sección **Configuración de datos** > **Productos** del panel.
{% endalert %}

### Ejemplo de objeto de compra {#example-purchase-object}

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### Objetos de compra, objetos de evento y webhooks {#purchase-objects-event-objects-and-webhooks}

Utilizando el ejemplo proporcionado, podemos ver que alguien compró una mochila con las propiedades: color, monograma, duración de la compra, tamaño y marca. A continuación, podemos crear segmentos con estas propiedades utilizando [las propiedades del evento de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) o enviar mensajes personalizados a través de un canal utilizando Liquid. Por ejemplo: "Hola, **Ann F.**, gracias por comprar esa **mochila roja mediana** por **40,00 $**. ¡Gracias por comprar en **Backpack Locker**!"

Si quieres guardar, almacenar y hacer un seguimiento de las propiedades para segmentar, tienes que configurarlas como atributos personalizados. Esto puede hacerse utilizando [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension), que te permiten dirigirte a los usuarios basándote en un evento personalizado o en el comportamiento de compra almacenado durante toda la vida de ese perfil de usuario.