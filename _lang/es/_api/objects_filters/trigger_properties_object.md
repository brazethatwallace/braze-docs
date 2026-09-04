---
nav_title: "Objeto de propiedades de activación"
article_title: Objeto de propiedades de activación de API
page_order: 11
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto de propiedades de activación."
tool: Campaigns

---

# Objeto de propiedades de activación {#trigger-properties-object}

> Cuando utilices uno de los puntos de conexión para enviar una Campaign con entrega desencadenada por API, puedes proporcionar un mapeado de claves y valores para personalizar tu mensaje.

Si realizas una solicitud a la API que contenga un objeto en `trigger_properties`, los valores de ese objeto pueden referenciarse en tu plantilla de mensajes bajo el espacio de nombres `api_trigger_properties`. Por ejemplo, una solicitud con lo siguiente podría añadir la palabra `"shoes"` a un mensaje añadiendo {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}.

Ten en cuenta que, aunque las propiedades de activación pueden incluirse en plantillas de mensajes, no se almacenan automáticamente en el perfil de usuario de forma predeterminada.

{% alert note %}
El objeto `trigger_properties` y la sintaxis {% raw %}`api_trigger_properties.${product_name}`{% endraw %} solo se admiten en Campaigns. Para personalizar mensajes con claves y valores de una solicitud de activación de API para Canvas, utiliza el [objeto de propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context). El objeto `trigger_properties` tiene un límite de tamaño máximo de 50 KB.
{% endalert %}

## Cuerpo del objeto {#object-body}

El objeto `trigger_properties` admite cadenas, números, booleanos, fechas, objetos y matrices como tipos de datos.

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"],
    "line_items": [
      {
        "sku": "WH-9000",
        "name": "Wireless Headphones",
        "quantity": 1,
        "pricing": {
          "amount": 79.99,
          "currency": "USD"
        }
      },
      {
        "sku": "RS-450",
        "name": "Running Shoes",
        "quantity": 2,
        "pricing": {
          "amount": 129.99,
          "currency": "USD"
        }
      }
    ]
  }
}
```

## Ejemplos de plantillas Liquid {#liquid-templating-examples}

Haz referencia a las propiedades de desencadenamiento en tus plantillas de mensaje usando el espacio de nombres `api_trigger_properties`:

- Cadenas: {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} devuelve `"shoes"`
- Números: {% raw %}`{{api_trigger_properties.${product_price}}}`{% endraw %} devuelve `79.99`
- Objetos anidados: {% raw %}`{{api_trigger_properties.${details}.${color}}}`{% endraw %} devuelve `"red"`
- Elementos de matriz: {% raw %}`{{api_trigger_properties.${related_skus}[0]}}`{% endraw %} devuelve `"123"`
- Matrices de objetos complejas: {% raw %}`{{api_trigger_properties.${line_items}[0]}}`{% endraw %} devuelve el primer objeto de línea de pedido