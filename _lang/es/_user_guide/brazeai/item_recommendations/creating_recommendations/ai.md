---
nav_title: Recomendaciones de IA
article_title: Crear recomendaciones de elementos de IA
description: "Este artículo de referencia explica cómo crear una recomendación de elementos de IA para los elementos de un catálogo."
page_order: 1
---

# Crear recomendaciones de elementos de IA {#create-ai-item-recommendations}

> Aprende a crear una herramienta de recomendaciones basada en inteligencia artificial a partir de los elementos de tu catálogo.

## Acerca de las recomendaciones de elementos de IA {#about-ai-item-recommendations}

Utiliza las recomendaciones de elementos de IA para calcular los productos más populares o crear recomendaciones personalizadas basadas en IA para un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) específico. Después de crear tu recomendación, puedes utilizar la personalización para insertar esos productos en tus mensajes.

{% alert tip %}
[Las recomendaciones AI Personalizado](#recommendation-types) funcionan mejor con al menos unos cientos de elementos del catálogo, como máximo 100.000 elementos del catálogo y, normalmente, al menos 30.000 usuarios con datos de compra o interacción. Esto es solo una guía aproximada y puede variar. Los otros tipos de recomendación pueden funcionar con menos datos, incluso cuando se utiliza **Más popular** como alternativa.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Crear una recomendación de elementos de IA {#creating-an-ai-item-recommendation}

### Requisitos previos {#prerequisites}

Antes de empezar, necesitas lo siguiente:

- Al menos un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) para poder utilizar cualquiera de los tipos de recomendaciones que se describen a continuación.
- Datos de compra o evento en Braze (eventos personalizados, el evento de pedido realizado o el objeto de compra) que incluyan una referencia al elemento y coincidan con los ID de los elementos del catálogo.

### Paso 1: Crear una nueva recomendación {#step-1-create-a-new-recommendation}

Puedes crear una recomendación de elementos de IA desde cualquiera de los dos lugares del panel:

{% tabs local %}
{% tab Desde el menú de navegación %}
1. Ve a **Analytics** > **AI Item Recommendation**.
2. Selecciona **Create Prediction** > **AI Item Recommendation**.
{% endtab %}

{% tab Desde un catálogo %}
También puedes optar por crear una recomendación directamente desde un catálogo individual. Selecciona tu catálogo en la página **Catalogs** y, a continuación, selecciona **Create Recommendation**.
{% endtab %}
{% endtabs %}

### Paso 2: Añadir detalles de la recomendación {#step-2-add-recommendation-details}

Dale a tu recomendación un nombre y una descripción opcional.

![Paso "Detalles de la recomendación" con los campos de nombre y descripción.]({% image_buster /assets/img/item_recs_1.png %})

### Paso 3: Define tu recomendación {#recommendation-type}

Selecciona un tipo de recomendación. Cada tipo utiliza los datos de interacción con los elementos de los últimos seis meses, como datos de compras, pedidos realizados o eventos personalizados. Para obtener información más detallada y casos de uso de cada uno, consulta [Tipos y casos de uso]({{site.baseurl}}/user_guide/brazeai/item_recommendations).

{% alert tip %}
Al utilizar **Más reciente** o **AI Personalizado**, los usuarios con datos insuficientes para crear recomendaciones individualizadas recibirán los elementos **Más populares** como alternativa. Puedes ver una aproximación de la proporción de usuarios que reciben la alternativa **Más popular** en la página de **Analytics**. La alternativa **Más popular** solo devuelve elementos que existen en el catálogo vinculado.
{% endalert %}

#### Paso 3.1: Excluir compras o interacciones anteriores (opcional) {#step-31-exclude-prior-purchases-or-interactions-optional}

Para evitar sugerir elementos que un usuario ya haya comprado o con los que ya haya interactuado, selecciona **Do not recommend items users have previously interacted with**. Esta opción solo está disponible cuando el **Type** de recomendación está configurado como **AI Personalized**.

![Paso "Define tu recomendación" con "AI Personalized" como tipo y la opción "Do not recommend items users have previously interacted with" seleccionada.]({% image_buster /assets/img/item_recs_2-3.png %})

Esta configuración impide que los mensajes reutilicen los elementos que un usuario ya ha comprado o con los que ya ha interactuado, siempre que la recomendación se haya actualizado recientemente. Los elementos comprados o con los que se haya interactuado entre las actualizaciones de las recomendaciones pueden seguir apareciendo. En la versión gratuita de las recomendaciones de elementos, las actualizaciones son semanales. Para la versión pro de las recomendaciones de elementos de IA, las actualizaciones se producen cada 24 horas.

Por ejemplo, al utilizar la versión pro de las recomendaciones de elementos de IA, si un usuario compra algo y luego recibe un correo electrónico de marketing en 30 minutos, es posible que el elemento que acaba de comprar no se excluya del correo electrónico a tiempo. Sin embargo, los mensajes enviados después de 24 horas no incluirán ese elemento.

#### Paso 3.2: Seleccionar un catálogo {#step-32-select-a-catalog}

Si aún no está rellenado, selecciona el [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) del que esta recomendación extraerá los elementos.

#### Paso 3.3: Añadir una selección (opcional) {#step-33-add-a-selection-optional}

Si quieres tener más control sobre tu recomendación, elige una [selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para aplicar filtros personalizados. Las selecciones filtran las recomendaciones por columnas específicas de tu catálogo, como marca, tamaño o ubicación. Las selecciones que contienen Liquid no pueden utilizarse en tu recomendación.

![Un ejemplo de la selección "en stock" elegida para la recomendación.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Si no puedes encontrar tu selección, asegúrate de que esté configurada en tu catálogo.
{% endalert %}

### Paso 4: Seleccionar la interacción para impulsar las recomendaciones {#step-4-select-the-interaction-to-drive-recommendations}

Selecciona el evento para el que quieres que se optimice esta recomendación. Este evento suele ser una compra, pero también puede ser cualquier interacción con un elemento.

{% alert tip %}
Al configurar las recomendaciones de elementos de IA, tu elección de evento es importante. Tu evento desencadenante determina quién recibe una recomendación generada por IA: las recomendaciones de elementos de IA se generan para los usuarios que han completado el evento que configures, por lo que esta elección determina directamente quién recibe recomendaciones. Selecciona un evento que cubra todo el segmento de audiencia al que quieres llegar.<br><br> Al mismo tiempo, equilibra la cobertura con la relevancia. Los eventos de la parte superior del embudo (como Producto visto) tienden a captar una audiencia más amplia pero están menos conectados con los resultados de negocio, mientras que los eventos de la parte inferior del embudo (como Comprado) tienden a producir recomendaciones más específicas y relevantes para el negocio. El mejor evento es aquel que equilibra la cobertura con la influencia en los resultados finales.
{% endalert %}

Puedes optimizar para:

- Eventos de compra con el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object)
- Eventos personalizados que representan una compra
- Eventos personalizados que representen cualquier otra interacción con elementos (como vistas de productos, clics o reproducciones multimedia)
- Pedidos realizados con el [evento de pedido realizado]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)

Si eliges **Custom Event**, selecciona tu evento de la lista.

![El evento personalizado "purchase" seleccionado como la forma en que se realiza actualmente el seguimiento de los eventos.]({% image_buster /assets/img/item_recs_3.png %})

{% alert note %}
Los eventos personalizados deben tener datos suficientes antes de aparecer en la lista de eventos. Si tu evento personalizado no aparece, puede ser porque el backend de Braze aún no lo ha procesado o porque no hay datos suficientes para el entrenamiento del modelo. Las recomendaciones de IA se basan en datos históricos para generar información, por lo que los eventos recién creados o que se desencadenan con poca frecuencia no estarán disponibles hasta que se recopilen más datos.
{% endalert %}

### Paso 5: Elegir el nombre de la propiedad correspondiente {#property-name}

Para crear una recomendación, tienes que indicarle a Braze qué campo de tu evento de interacción (evento de pedido realizado, objeto de compra o evento personalizado) tiene el identificador único que coincide con el campo `id` de un elemento en el catálogo. ¿No estás seguro? [Ver requisitos](#requirements).

Selecciona este campo para **Property Name**.

El campo **Property Name** se rellenará previamente con una lista de campos enviados a través del SDK a Braze. Si se proporcionan datos suficientes, estas propiedades también se clasificarán por orden de probabilidad de ser la propiedad correcta. Selecciona la que corresponda al campo `id` del catálogo.

![El nombre de la propiedad "purchase_item" seleccionado que corresponde a los ID de los elementos del catálogo.]({% image_buster /assets/img/item_recs_4.png %})

#### Requisitos {#requirements}

Hay algunos requisitos para seleccionar tu propiedad:

- Debe mapearse al campo `id` de tu catálogo seleccionado.
- **Si seleccionaste el evento de pedido realizado o estás utilizando [eventos de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) para entrenar recomendaciones de elementos:** Introduce `products.product_id` para el ID del producto.
  - El campo puede estar dentro de una matriz de productos o terminar con una matriz de ID. En cualquier caso, cada ID de producto se tratará como un evento independiente y secuencial con la misma marca de tiempo.
- **Si seleccionaste objeto de compra:** Debe ser el `product_id` o un campo de `properties` de tu evento de interacción.
- **Si seleccionaste evento personalizado:** Debe ser un campo de `properties` de tu evento personalizado.
- Los campos anidados deben escribirse en el desplegable **Property Name** en notación de puntos con el formato `event_property.nested_property`. Por ejemplo, si seleccionas la propiedad anidada `district_name` dentro de la propiedad de evento `location`, introducirías `location.district_name`.

#### Ejemplos de mapeados {#example-mappings}

Los siguientes ejemplos de mapeados hacen referencia a este catálogo de muestra:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table aria-label="Ejemplos de mapeados" class="tg">
  <caption>Ejemplos de mapeados</caption>
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

Supongamos que quieres utilizar el evento personalizado `added_to_cart` para poder recomendar productos similares antes de que el cliente pase por caja. El evento `added_to_cart` tiene una propiedad de evento `product_sku`.

Entonces la propiedad `product_sku` debe incluir al menos uno de los valores de la columna `id` del catálogo de muestra: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" o "ADI-PP-10". No necesitas eventos para cada elemento del catálogo, pero sí algunos para que la herramienta de recomendaciones tenga suficiente contenido con el que trabajar.

##### Ejemplo de objeto de evento personalizado {#example-custom-event-object}

Este evento tiene `"product_sku": "ADI-BL-7"`, que coincide con el primer elemento del catálogo de muestra.

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

##### Ejemplo de objeto de evento personalizado con una matriz de productos {#example-custom-event-object-with-an-array-of-products}

Si las propiedades de tu evento contienen varios productos en una matriz, cada ID de producto se tratará como un evento independiente y secuencial. Este evento puede utilizar la propiedad `products.sku` para coincidir con el primer y el tercer elemento del catálogo de muestra.

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

##### Ejemplo de objeto de evento personalizado con un objeto anidado que contiene una matriz de ID de producto {#example-custom-event-object-with-a-nested-object-containing-a-product-id-array}

Si los ID de tus productos son valores en una matriz en lugar de objetos, puedes utilizar la misma notación y cada ID de producto se tratará como un evento secuencial independiente. Esto puede combinarse de forma flexible con objetos anidados en el siguiente evento configurando la propiedad como `purchase.product_skus` para coincidir con el primer y el tercer elemento del catálogo de muestra.

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

Se pasa un objeto de compra a través de la API cuando se ha realizado una compra.

En cuanto al mapeado, para los objetos de compra se aplica una lógica similar a la de los eventos personalizados, con la diferencia de que puedes elegir entre utilizar el `product_id` del objeto de compra o un campo del objeto `properties`.

Recuerda que no necesitas eventos para cada elemento del catálogo, pero sí algunos de ellos para que la herramienta de recomendaciones tenga suficiente contenido con el que trabajar.

##### Ejemplo de objeto de compra mapeado a ID de producto {#example-purchase-object-mapped-to-product-id}

Este evento tiene `"product_id": "ADI-BL-7"`, que se mapea al primer elemento del catálogo.

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

Este evento tiene una propiedad `"sku": "ADI-RD-8"`, que se mapea al segundo elemento del catálogo.

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

##### Ejemplo de objeto de pedido realizado mapeado a ID de producto {#example-order-placed-object-mapped-to-product-id}

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

Cuando estés listo, selecciona **Create Recommendation**. Este proceso puede durar entre 10 minutos y 36 horas. Recibirás una actualización por correo electrónico cuando la recomendación se haya entrenado correctamente o una explicación de por qué puede haber fallado la creación.

Puedes encontrar la recomendación en la página **Predictions**, donde luego puedes editarla o archivarla según necesites. Las recomendaciones se volverán a entrenar automáticamente una vez a la semana (de pago) o al mes (gratis).