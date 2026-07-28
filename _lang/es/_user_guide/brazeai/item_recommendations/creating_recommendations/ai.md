---
nav_title: Recomendaciones de IA
article_title: Crear recomendaciones de elementos de IA
description: "Este artículo de referencia explica cómo crear una recomendación de elementos de IA para los elementos de un catálogo."
page_order: 1
---

# Crear recomendaciones de elementos de IA {#create-ai-item-recommendations}

> Aprende a crear una herramienta de recomendaciones basada en inteligencia artificial a partir de los elementos de tu catálogo.

## Acerca de las recomendaciones de elementos de IA {#about-ai-item-recommendations}

Usa las recomendaciones de elementos de IA para calcular los productos más populares o crear recomendaciones de IA personalizadas para un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) específico. Después de crear tu recomendación, puedes usar la personalización para insertar esos productos en tus mensajes.

{% alert tip %}
Las [recomendaciones de AI Personalizado](#recommendation-types) funcionan mejor con al menos unos cientos de elementos del catálogo, como máximo 100.000 elementos del catálogo y, normalmente, al menos 30.000 usuarios con datos de compra o interacción. Esto es solo una guía aproximada y puede variar. Los otros tipos de recomendación pueden funcionar con menos datos, incluso cuando se usa **Más popular** como alternativa.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Crear una recomendación de artículos con IA {#creating-an-ai-item-recommendation}

### Requisitos previos {#prerequisites}

Antes de empezar, debes tener lo siguiente:

- Al menos un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) para usar cualquiera de los [tipos de recomendación]({{site.baseurl}}/user_guide/brazeai/item_recommendations).
- Datos de compras o eventos en Braze (eventos personalizados, el evento de pedido realizado o el objeto de compra) que incluyan una referencia al artículo y que coincidan con los ID de artículos del catálogo.

### Paso 1: Crear una nueva recomendación {#step-1-create-a-new-recommendation}

Puedes crear una recomendación de artículos con IA desde cualquiera de estos lugares en el panel:

{% tabs local %}
{% tab Desde el menú de navegación %}
1. Ve a **Analytics** > **AI Item Recommendation**.
2. Selecciona **Create Prediction** > **AI Item Recommendation**.
{% endtab %}

{% tab Desde un catálogo %}
También puedes crear una recomendación directamente desde un catálogo individual. Selecciona tu catálogo en la página **Catalogs** y luego selecciona **Create Recommendation**.
{% endtab %}
{% endtabs %}

### Paso 2: Añadir detalles de la recomendación {#step-2-add-recommendation-details}

Dale a tu recomendación un nombre y una descripción opcional.

![Paso "Detalles de la recomendación" con los campos de nombre y descripción.]({% image_buster /assets/img/item_recs_1.png %})

### Paso 3: Definir tu recomendación {#recommendation-type}

Selecciona un tipo de recomendación. Cada tipo utiliza los últimos seis meses de datos de interacción con artículos, como datos de compras, pedidos realizados o eventos personalizados. Para obtener información más detallada y ejemplos de cada tipo, consulta [Tipos y ejemplos]({{site.baseurl}}/user_guide/brazeai/item_recommendations).

{% alert tip %}
Cuando se usa **Más reciente** o **IA Personalizado**, los usuarios con datos insuficientes para crear recomendaciones individualizadas reciben artículos de **Más popular** como alternativa. La alternativa de **Más popular** solo devuelve artículos que existen en el catálogo vinculado.<br><br>Para las recomendaciones de **IA Personalizado**, consulta la **Tasa de personalización** en la página de **Analytics** para ver qué porcentaje de usuarios que realizaron el evento configurado en los últimos 24 meses tienen recomendaciones personalizadas almacenadas en su perfil. Para las recomendaciones de **Más reciente**, la página de **Analytics** muestra la proporción de usuarios que reciben recomendaciones de **Más reciente** frente a la alternativa de **Más popular**.
{% endalert %}

#### Paso 3.1: Excluir compras o interacciones anteriores (opcional) {#step-31-exclude-prior-purchases-or-interactions-optional}

Para evitar sugerir artículos que un usuario ya ha comprado o con los que ya ha interactuado, selecciona **Do not recommend items users have previously interacted with**. Esta opción solo está disponible cuando el **Tipo** de recomendación está configurado como **IA Personalizado**.

![Paso "Definir tu recomendación" con "IA Personalizado" como tipo y la opción "No recomendar artículos con los que los usuarios ya han interactuado" seleccionada.]({% image_buster /assets/img/item_recs_2-3.png %})

Esta configuración evita que los mensajes reutilicen los artículos que un usuario ya ha comprado o con los que ya ha interactuado, siempre que la recomendación se haya actualizado recientemente. Los artículos comprados o con los que se interactuó entre actualizaciones de recomendaciones pueden seguir apareciendo. Para la versión gratuita de las recomendaciones de artículos, las actualizaciones se realizan semanalmente. Para la versión pro de las recomendaciones de artículos con IA, las actualizaciones se realizan cada 24 horas.

Por ejemplo, cuando se usa la versión pro de las recomendaciones de artículos con IA, si un usuario compra algo y luego recibe un correo electrónico de marketing en 30 minutos, el artículo que acaba de comprar podría no excluirse del correo electrónico a tiempo. Sin embargo, cualquier mensaje enviado después de 24 horas no incluirá ese artículo.

#### Paso 3.2: Seleccionar un catálogo {#step-32-select-a-catalog}

Si no está ya rellenado, selecciona el [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) del que esta recomendación extraerá artículos.

#### Paso 3.3: Añadir una selección (opcional) {#step-33-add-a-selection-optional}

Si deseas más control sobre tu recomendación, elige una [selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para aplicar filtros personalizados. Las selecciones filtran las recomendaciones por columnas específicas de tu catálogo, como marca, talla o ubicación. Las selecciones que contienen Liquid no se pueden usar en tu recomendación.

![Un ejemplo de la selección "en stock" seleccionada para la recomendación.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Si no encuentras tu selección, asegúrate de que esté configurada primero en tu catálogo.
{% endalert %}

### Paso 4: Seleccionar la interacción para impulsar las recomendaciones {#step-4-select-the-interaction-to-drive-recommendations}

Selecciona el evento para el que deseas que esta recomendación se optimice. Este evento suele ser una compra, pero también puede ser cualquier interacción con un artículo.

{% alert tip %}
Al configurar las recomendaciones de artículos con IA, tu elección de evento es importante. Tu evento desencadenante determina quién recibe una recomendación generada por IA: las recomendaciones de artículos con IA se generan para los usuarios que han completado el evento que configures, por lo que esta elección determina directamente quién recibe recomendaciones. Selecciona un evento que cubra todo el Segment de audiencia al que deseas llegar.<br><br>Al mismo tiempo, equilibra la cobertura con la relevancia. Los eventos de la parte superior del embudo (como Producto visto) tienden a captar una audiencia más amplia pero están menos conectados con los resultados de negocio, mientras que los eventos de la parte inferior del embudo (como Comprado) tienden a producir recomendaciones más específicas y relevantes para el negocio. El mejor evento es aquel que equilibra la cobertura con la influencia en los resultados finales.
{% endalert %}

Puedes optimizar para:

- Eventos de compra con el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object)
- Eventos personalizados que representan una compra
- Eventos personalizados que representan cualquier otra interacción con artículos (como vistas de productos, clics o reproducciones de medios)
- Pedidos realizados con el [evento de pedido realizado]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)

Si eliges **Evento personalizado**, selecciona tu evento de la lista.

![El evento personalizado "purchase" seleccionado como la forma en que se rastrean actualmente los eventos.]({% image_buster /assets/img/item_recs_3.png %})

{% alert note %}
Los eventos personalizados deben tener datos suficientes antes de aparecer en la lista de eventos. Si tu evento personalizado no aparece, puede ser porque el backend de Braze aún no lo ha procesado o porque no tiene suficientes datos para el entrenamiento del modelo. Las recomendaciones de IA dependen de datos históricos para generar información, por lo que los eventos recién creados o que se desencadenan con poca frecuencia no estarán disponibles hasta que se recopilen más datos.
{% endalert %}

### Paso 5: Elegir el nombre de propiedad correspondiente {#property-name}

Para crear una recomendación, necesitas indicarle a Braze qué campo de tu evento de interacción (evento de pedido realizado, objeto de compra o evento personalizado) tiene el identificador único que coincide con el campo `id` de un artículo en el catálogo. ¿No estás seguro? [Consulta los requisitos](#requirements).

Selecciona este campo para el **Nombre de propiedad**.

El campo **Nombre de propiedad** se rellena previamente con una lista de campos enviados a través del SDK a Braze. Si se proporcionan suficientes datos, estas propiedades también se clasifican en orden de probabilidad de ser la propiedad correcta. Selecciona la que corresponda al campo `id` del catálogo.

![El nombre de propiedad "purchase_item" seleccionado que corresponde a los ID de artículos en el catálogo.]({% image_buster /assets/img/item_recs_4.png %})

#### Requisitos {#requirements}

Hay algunos requisitos para seleccionar tu propiedad:

- Debe mapearse al campo `id` de tu catálogo seleccionado.
- **Si seleccionaste el evento de pedido realizado o estás usando [eventos de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) para entrenar las recomendaciones de artículos:** Introduce `products.product_id` para el ID de producto.
  - El campo puede estar dentro de un array de productos o terminar con un array de ID. En cualquier caso, cada ID de producto se tratará como un evento separado y secuencial con la misma marca de tiempo.
- **Si seleccionaste el objeto de compra:** Debe ser el `product_id` o un campo de las `properties` de tu evento de interacción.
- **Si seleccionaste un evento personalizado:** Debe ser un campo de las `properties` de tu evento personalizado.
- Los campos anidados deben escribirse en el desplegable de **Nombre de propiedad** en notación de punto con el formato `event_property.nested_property`. Por ejemplo, si seleccionas la propiedad anidada `district_name` dentro de la propiedad del evento `location`, deberías introducir `location.district_name`.

#### Mapeados de ejemplo {#example-mappings}

Los siguientes mapeados de ejemplo hacen referencia a este catálogo de muestra:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table aria-label="Mapeados de ejemplo" class="tg">
  <caption>Mapeados de ejemplo</caption>
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Black Size 7</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Red Size 8</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas White Size 9</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Purple Size 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Evento personalizado %}

Supongamos que quieres usar el evento personalizado `added_to_cart` para poder recomendar productos similares antes de que el cliente finalice la compra. El evento `added_to_cart` tiene una propiedad de evento de `product_sku`.

Entonces la propiedad `product_sku` debe incluir al menos uno de los valores de la columna `id` en el catálogo de muestra: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" o "ADI-PP-10". No necesitas eventos para cada artículo del catálogo, pero sí necesitas algunos de ellos para que la herramienta de recomendaciones tenga suficiente contenido con el que trabajar.

##### Ejemplo de objeto de evento personalizado {#example-custom-event-object}

Este evento tiene `"product_sku": "ADI-BL-7"`, que coincide con el primer artículo del catálogo de muestra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Ejemplo de objeto de evento personalizado con un array de productos {#example-custom-event-object-with-an-array-of-products}

Si las propiedades de tu evento contienen múltiples productos en un array, cada ID de producto se tratará como un evento separado y secuencial. Este evento puede usar la propiedad `products.sku` para coincidir con el primer y tercer artículo del catálogo de muestra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Ejemplo de objeto de evento personalizado con un objeto anidado que contiene un array de ID de productos {#example-custom-event-object-with-a-nested-object-containing-a-product-id-array}

Si tus ID de productos son valores en un array en lugar de objetos, puedes usar la misma notación y cada ID de producto se tratará como un evento separado y secuencial. Esto se puede combinar de forma flexible con objetos anidados en el siguiente evento configurando la propiedad como `purchase.product_skus` para coincidir con el primer y tercer artículo del catálogo de muestra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Objeto de compra %}

Un objeto de compra se envía a través de la API cuando se ha realizado una compra.

En cuanto al mapeado, se aplica una lógica similar para los objetos de compra que para los eventos personalizados, excepto que puedes elegir entre usar el `product_id` del objeto de compra o un campo del objeto `properties`.

Recuerda que no necesitas eventos para cada artículo del catálogo, pero sí necesitas algunos de ellos para que la herramienta de recomendaciones tenga suficiente contenido con el que trabajar.

##### Ejemplo de objeto de compra mapeado al ID de producto {#example-purchase-object-mapped-to-product-id}

Este evento tiene `"product_id": "ADI-BL-7"`, que se mapea al primer artículo del catálogo.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Ejemplo de objeto de compra mapeado a un campo de propiedades {#example-purchase-object-mapped-to-a-properties-field}

Este evento tiene una propiedad de `"sku": "ADI-RD-8"`, que se mapea al segundo artículo del catálogo.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% tab Evento de pedido realizado %}

##### Ejemplo de objeto de pedido realizado mapeado al ID de producto {#example-order-placed-object-mapped-to-product-id}

```json
{
  "name": "ecommerce.order_placed",
  "properties": {
    "order_id": "order_123",
    "total_value": 200.0,
    "currency": "USD",
    "products": [
      {
        "product_id": "ADI-BL-7",
        "product_name": "Adidas Black Size 7",
        "variant_id": "ADI-BL-7-default",
        "quantity": 1,
        "price": 100.0
      }
    ],
    "source": "storefront"
  }
}
```

{% endtab %}
{% endtabs %}

### Paso 6: Entrenar la recomendación {#step-6-train-the-recommendation}

Cuando estés listo, selecciona **Create Recommendation**. Este proceso puede tardar entre 10 minutos y 36 horas en completarse. Recibirás una actualización por correo electrónico cuando la recomendación se haya entrenado correctamente o una explicación de por qué la creación pudo haber fallado.

Puedes encontrar la recomendación en la página de **Predictions**, donde podrás editarla o archivarla según sea necesario. Las recomendaciones se reentrenan automáticamente una vez a la semana (de pago) o al mes (gratuita).