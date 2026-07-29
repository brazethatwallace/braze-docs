---
nav_title: Sincronización de productos de Shopify
article_title: Sincronización de productos de Shopify
alias: /shopify_catalogs/
page_order: 5
description: "Este artículo de referencia explica cómo importar tus productos de Shopify a los catálogos de Braze."
---

# Sincronización de productos de Shopify {#shopify-product-sync}

> Puedes sincronizar todos los productos de tu tienda Shopify con un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) de Braze para una personalización más profunda de la mensajería.

Los catálogos de Shopify se actualizarán casi en tiempo real a medida que realices ediciones y cambios en los productos de tu tienda Shopify. Puedes enriquecer tu carrito abandonado, la confirmación del pedido y mucho más con los detalles y la información más actualizados sobre los productos.

Además de admitir los [datos principales de productos de Shopify](#supported-shopify-catalog-data), puedes sincronizar colecciones de Shopify, etiquetas de productos y metacampos de productos con tu catálogo de Braze. Estos campos adicionales desbloquean una personalización más rica, selecciones de catálogo más precisas y una segmentación más potente a través de las [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension).

## Configura tu sincronización de productos de Shopify {#set-up}

Si ya has instalado tu tienda Shopify, puedes sincronizar tus productos siguiendo las instrucciones de esta sección.

### Paso 1: Activa la sincronización {#step-1-turn-on-the-sync}

Puedes sincronizar tus productos con un catálogo de Braze a través del flujo de instalación de Shopify o en la página del partner de Shopify.

![Paso 3 del proceso de configuración con "Shopify Variant ID" como "Catalog product identifier".]({% image_buster /assets/img/shopify/sync_products_step1.png %})

### Paso 2: Selecciona el identificador de tu producto {#step-2-select-your-product-identifier}

Selecciona el identificador de producto principal que se usará como ID del catálogo de Braze:

- **Shopify Variant ID** es una buena opción predeterminada cuando tus SKU faltan, están duplicados entre variantes o pueden contener caracteres como barras, puntos, espacios o ampersands. Los Variant ID son numéricos y siempre cumplen estos requisitos.
- **SKU** funciona bien cuando cada variante tiene un SKU único que sigue las mismas reglas de caracteres que Shopify Variant ID, y quieres que la mensajería o los análisis usen los SKU de comercio minorista como clave del catálogo.
  - Puedes usar SKU de texto libre que contengan caracteres no permitidos utilizando Shopify Variant ID en lugar de SKU.

El valor que selecciones se convierte en el `item_id` del catálogo y solo puede contener letras, números, guiones y guiones bajos.

{% alert note %}
Si usas SKU como ID del catálogo, asegúrate de que todos los productos y variantes de tu tienda tengan un SKU establecido y que sean únicos.<br><br>
- Si a un artículo le falta un SKU, Braze no puede sincronizar ese producto en el catálogo.
- Si tienes más de un producto con el mismo SKU, esto puede provocar un comportamiento inesperado o que la información del producto sea anulada involuntariamente.
{% endalert %}

### Paso 3: Configura datos de producto adicionales (opcional) {#step-3}

Opcionalmente, puedes habilitar la sincronización de etiquetas de productos, colecciones de Shopify y metacampos. Habilita o modifica estos ajustes después de la sincronización inicial desde la página del partner de Shopify.

{% alert note %}
Primero añade las etiquetas de productos, las colecciones de Shopify y los metacampos en Shopify. Si no existen en Shopify, no aparecerán en Braze.
{% endalert %}

![Configuración para sincronizar productos y variantes de Shopify con Braze.]({% image_buster /assets/img/shopify/additional_product_data.png %})

{% tabs global %}
{% tab Etiquetas de productos %}

1. En la página **Sync product data to Braze**, selecciona la casilla **Sync product tags** para abrir el modal **Select product tags**.
2. Selecciona hasta 20 etiquetas de productos para sincronizar con tu catálogo de Braze. Solo se sincronizarán las etiquetas que selecciones.

![Modal para seleccionar etiquetas de productos con una selección de etiquetas.]({% image_buster /assets/img/shopify/select_product_tags.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Metacampos de productos %}

1. Si tienes una integración de Shopify existente, vuelve a autorizar la aplicación Braze Shopify para instalar los nuevos permisos necesarios para sincronizar productos. Si eres un cliente nuevo, ve al siguiente paso.

![Banner que indica volver a autorizar la aplicación Braze Shopify.]({% image_buster /assets/img/shopify/banner_to_reauthorize.png %})

{: start="2"}
2. Selecciona **Sync product metafields** para abrir el modal de configuración de metacampos.

![Sección de sincronización de datos de productos con Braze con opciones para seleccionar entre múltiples configuraciones, incluidas las colecciones.]({% image_buster /assets/img/shopify/select_collections.png %})

{: start="3"}
3. Selecciona hasta 20 de los metacampos buscables para sincronizar. Cada uno se convierte en una columna separada en tu catálogo para usar en características como selecciones de catálogo o extensiones de segmento.
- Al nombrar metacampos, ten en cuenta que los espacios se convierten en "_" y todos los caracteres especiales se eliminan para cumplir con las restricciones de nomenclatura de campos de catálogo de Braze.

![Modal para seleccionar metacampos de productos.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

{% subtabs %}
{% subtab Metacampos compatibles %}

Braze admite los siguientes objetos de metacampos y algunos de sus tipos respectivos.

| Tipo de metacampo                                | Tipo de datos                                          |
|--------------------------------------------------|--------------------------------------------------------|
| `boolean`                                        | Booleano                                               |
| `color`, `list.color`                            | Cadena (color hexadecimal, como `#FFF123`), Matriz de cadenas |
| `date`, `list.date`                              | Cadena (fecha ISO 8601), Matriz de cadenas (fechas ISO 8601) |
| `date_time`, `list.date_time`                    | Cadena (fecha y hora ISO 8601), Matriz de cadenas (fechas y horas ISO 8601) |
| `id`, `list.id`                                  | Cadena, Matriz de cadenas                              |
| `multi_line_text_field`                          | Cadena                                                 |
| `number_decimal`                                 | Cadena                                                 |
| `number_integer`                                 | Entero                                                 |
| `single_line_text_field`, `list.single_line_text_field` | Cadena, Matriz de cadenas                       |
| `url`, `list.url`                                | Cadena (URL), Matriz de cadenas (URLs)                 |
| `metaobject_reference`, `list.metaobject_reference` | Cadena, Matriz de cadenas                          |
| `mixed_reference`, `list.mixed_reference`        | Cadena, Matriz de cadenas                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configura datos de producto adicionales (opcional)" }

{% endsubtab %}
{% subtab Metacampos no compatibles %}

Braze no admite objetos de metacampos, incluidos algunos tipos de lista respectivos:

- `dimension` (`list.dimension`)
- `weight` (`list.weight`)
- `link` (`list.link`)
- `json`
- `list.number_decimal`
- `list.number_integer`
- `money`
- `rating` (`list.rating`)
- `volume` (`list.volume`)
- `rich_text_field`

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Colecciones %}

1. Selecciona **Sync Shopify collections** para abrir el modal de configuración de colecciones.
2. Selecciona hasta 20 colecciones para sincronizar.
  - El modal proporciona una lista buscable de hasta 5000 de las colecciones creadas o actualizadas más recientemente de tu tienda Shopify.
  - Las colecciones seleccionadas previamente que ya no están entre las 5000 principales seguirán apareciendo en tu selección.

{% alert note %}
Braze utiliza el ID de colección de Shopify para identificar las colecciones sincronizadas, que luego se utilizan al crear selecciones de catálogo y filtros de segmento.
{% endalert %}

![Modal para seleccionar colecciones de un menú desplegable.]({% image_buster /assets/img/shopify/selected_collections.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{% alert tip %}
Para ver ejemplos de cómo usar cada tipo de datos de producto, consulta [Casos de uso de catálogos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/?tab=shopify%20product%20metafields#shopify-catalog-use-cases).
{% endalert %}

### Paso 4: Sigue el progreso de tu sincronización {#step-4-track-your-sync-progress}

Después de guardar tu configuración, Braze comenzará a sincronizar tus productos y actualizará el estado a **In Progress** en tu página del partner de Shopify. El tiempo de sincronización depende del número de productos y variantes en tu tienda.

Puedes salir de la página una vez que la sincronización esté en curso; Braze te enviará una notificación en el panel cuando la sincronización se complete. Después de completarse, el estado se actualizará a **Active** y podrás ver tus productos seleccionando el nombre del catálogo en tu página del partner de Shopify.

![Página de configuración de la integración con un estado de sincronización de productos.]({% image_buster /assets/img/shopify/track_sync_progress.png %})

También puedes ver las etiquetas de productos, metacampos y colecciones sincronizados dentro de tu catálogo de Shopify como nuevas columnas.

![Catálogo de Shopify con datos sincronizados.]({% image_buster /assets/img/shopify/synced_catalog.png %})

{% alert important %}
Si tu sincronización supera el límite de almacenamiento de tu catálogo, Braze dejará de sincronizar y las nuevas actualizaciones de productos ya no se reflejarán. Ponte en contacto con tu administrador de éxito de cliente para subir de nivel si es necesario.
{% endalert %}

### Paso 5: Administra tu configuración {#step-5-manage-your-configuration}

Cada tipo de sincronización tiene una tarjeta de resumen en la página del partner de Shopify que muestra el recuento total sincronizado, el estado actual y un enlace a tu catálogo. Selecciona el icono de vista para ver tu configuración activa y editarla.

Puedes modificar tu sincronización de productos de Shopify, incluida la administración de tus etiquetas de productos, colecciones y metacampos de productos en cualquier momento desde la página del partner de Shopify.

![Página de configuración de la integración con una sincronización de catálogo de productos activa.]({% image_buster /assets/img/shopify/active_catalog_sync.png %})

{% alert important %}
Cambiar tus selecciones sincronizadas puede afectar a Campaigns, Canvas o selecciones de catálogo activas que hagan referencia a ellas. Actualiza el contenido activo para que funcione correctamente cuando apliques los cambios.
{% endalert %}

## Datos de catálogo de Shopify compatibles {#supported-shopify-catalog-data}

| Campo                | Tipo de datos  | Ejemplos                                                                   |
|----------------------|----------------|-----------------------------------------------------------------------------------|
| `id`                 | cadena         | `45264808411274` cuando el identificador de producto del catálogo es **Shopify Variant ID**<br><br>`12345` cuando el identificador de producto del catálogo es **SKU** (coincide con el valor que seleccionaste en el [Paso 2](#step-2-select-your-product-identifier)) |
| `store_name`         | cadena         | "your-store" (subdominio de la tienda Shopify, sin `.myshopify.com`)                |
| `shopify_product_id` | número         | `7939032613002` (almacenado como número en tu catálogo de Braze; las API de Shopify pueden devolver este ID como cadena) |
| `shopify_variant_id` | número         | `45264808411274` (almacenado como número en tu catálogo de Braze; las API de Shopify pueden devolver este ID como cadena) |
| `product_title`      | cadena         | "Classic leather jacket"                                                      |
| `variant_title`      | cadena         | "Large / Red", "Medium" o "Default Title" para productos de una sola variante     |
| `status`             | cadena         | "active", "draft", "archived"                                                     |
| `product_image_url`  | cadena         | "https://cdn.shopify.com/s/files/1/0641/0970/7402/files/t_shir.jpg?v=1736538760" |
| `variant_image_url`  | cadena         | La misma URL de CDN que la imagen del producto cuando no existe imagen de variante; de lo contrario, una URL de imagen específica de la variante |
| `vendor`             | cadena         | "Flash and Thread", "PantsLabyrinth"                                            |
| `product_type`       | cadena         | "Outerwear", "T-Shirts" (del **Product type** del producto en Shopify)      |
| `product_url`        | cadena         | "https://your-store.myshopify.com/products/classic-leather-jacket"            |
| `product_handle`     | cadena         | "classic-leather-jacket"                                                          |
| `published_scope`    | cadena         | "web", "global"                                                                   |
| `price`              | número         | `10.00`, `24.99`<br><br>Shopify a menudo devuelve los precios como cadenas (por ejemplo, `"199.00"` en la API REST Admin). Braze los convierte a números para este campo del catálogo. |
| `compare_at_price`   | número         | `15.00` cuando **Compare at price** está configurado en Shopify<br><br>`0` cuando Shopify no tiene un precio de comparación. Las API de Shopify normalmente devuelven `null` para un precio de comparación no establecido; Braze almacena `0` en el catálogo para que el campo sea siempre numérico (este es un valor predeterminado de Braze, no un valor que Shopify envía como `0`). |
| `inventory_quantity` | número         | `20`, `0` o un valor negativo cuando se permite la sobreventa (por ejemplo, `-18`)   |
| `options`            | cadena         | "Size,Color"<br><br>Shopify permite hasta tres tipos de opciones por producto (por ejemplo, Size, Color, Material). El valor de `options` es una lista separada por comas de esos nombres. |
| `option_values`      | cadena         | "Medium,Red", "Large,Red"<br><br>Cada valor se corresponde con el mismo orden que `options` (hasta tres valores). |
| `sku`                | cadena         | "12345", "SKU-001-RED-L"                                                    |
| `product_tags`       | matriz         | `["Summer", "Sale", "New"]`<br><br>Requiere la sincronización de etiquetas de productos.                 |
| `collection_ids`     | matriz         | `[123456789012, 987654321098]` (IDs de colección de Shopify)<br><br>Requiere la sincronización de colecciones de Shopify. |
| `Metafield columns`  | Varía según el tipo | Cada metacampo sincronizado aparece como una columna separada nombrada por su clave. Consulta [Metacampos compatibles](#step-3) en la pestaña "Metacampos de productos" del paso 3 para más información. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Datos de catálogo de Shopify compatibles" }

{% alert warning %}
Tu catálogo de Shopify es administrado por Shopify. Para actualizar tu catálogo, realiza los cambios directamente en tu tienda Shopify y se sincronizarán automáticamente con Braze. Para eliminar tu catálogo de Shopify, ve a la página del partner de Shopify en Braze y [desactiva la sincronización](#deactivate).
{% endalert %}

## Casos de uso de catálogos de Shopify {#shopify-catalog-use-cases}

Estos casos de uso muestran cómo puedes utilizar los datos de tu catálogo de Shopify sincronizado para personalizar mensajes.

{% alert warning %}
Braze sincroniza hasta 250 variantes de cada producto de Shopify en tu catálogo. Las variantes que superen ese límite no se sincronizan. Si necesitas más de 250 variantes por producto, ponte en contacto con tu administrador de éxito de cliente de Braze.
{% endalert %}

{% tabs %}
{% tab Etiquetas de productos %}

Usa las etiquetas de productos para personalizar mensajes según cómo están categorizados tus productos en Shopify. Por ejemplo, puedes enviar una promoción con todos los productos etiquetados como "Summer Sale" a través de una [selección de catálogo]({{site.baseurl}}/catalog_selections), o crear un segmento de usuarios que compraron productos etiquetados como "Premium".

Las etiquetas de productos se almacenan como un campo de matriz en cada artículo del catálogo. Para configurar la sincronización de etiquetas de productos, consulta [Etiquetas de productos de Shopify](#shopify-product-tags).

### Selección de catálogo {#catalog-selection}

1. En Shopify, asigna a los productos relevantes la etiqueta de producto "Women's".

![Un tipo de producto "Women's - Sweaters" con las etiquetas "Women's", "Sweaters" y "Men".]({% image_buster /assets/img/shopify/product_tag_womens.png %}){: style="max-width:40%;"}

{: start="2"}
2. En Braze, habilita la sincronización de etiquetas y selecciona la etiqueta de producto "Women's".

![Modal para seleccionar etiquetas de productos de Shopify, con 15 etiquetas relacionadas con ropa seleccionadas, incluida "Women's".]({% image_buster /assets/img/shopify/select_product_tags_womens.png %}){: style="max-width:80%;"}

### Personalización {#personalization}

{% alert note %}
Al hacer referencia a etiquetas de productos o colecciones en selecciones de catálogo, usa solo el valor en sí sin los corchetes de matriz `[]` ni las comillas `""` que aparecen en los datos del catálogo. Por ejemplo, si una etiqueta de producto se muestra como `["Women's"]` en tu catálogo, escribe `Women's` en tu filtro de selección.
{% endalert %}

1. Crea una selección de catálogo que filtre los productos que tengan la etiqueta de producto correspondiente, como "Women's". Solo puedes usar un campo de matriz único dentro de una sola selección de catálogo, y hasta 50 productos en tu selección de catálogo.

![Una selección de catálogo que filtra por etiquetas de productos que tienen el atributo "Women's".]({% image_buster /assets/img/shopify/edit_product_tags_selection.png %})

{: start="2"}
2. En el creador de mensajes, añade la selección donde quieras incluir los productos de la selección de catálogo etiquetados con "Women's". Por ejemplo, podrías usar un bloque de producto HTML como este:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

O, si quieres mencionar productos específicos etiquetados con "Women's" en una notificación push, puedes usar la herramienta **Add Personalization** y especificar los artículos de tu catálogo.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Creador de notificaciones push con una selección de catálogo que incluye tres artículos con una etiqueta de producto.]({% image_buster /assets/img/shopify/add_personalization_product_tags.png %})

### Segmentación de catálogo (SQL) {#catalog-segmentation-sql}

Usa las [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para crear segmentos basados en usuarios que interactuaron con una etiqueta de producto. Por ejemplo, para encontrar usuarios que han interactuado con artículos del catálogo que contienen una etiqueta de producto específica, usa esta consulta:

{% raw %}
```liquid
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific product tag. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'product_tags' AND ARRAY_CONTAINS('<product_tag_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% tab Metacampos de productos %}

Usa los metacampos de productos para personalizar mensajes con detalles de productos personalizados más allá de los campos estándar de Shopify. Por ejemplo, incluye instrucciones de cuidado en una confirmación de pedido, muestra el país de origen en un correo electrónico de recomendación, o segmenta usuarios que compraron un material específico.

Cada metacampo sincronizado se convierte en una columna separada en tu catálogo, con el tipo de datos determinado por el tipo de metacampo. Para configurar la sincronización de metacampos, consulta [Metacampos de productos de Shopify](#shopify-product-metafields).

### Selección de catálogo

1. En Shopify, establece el metacampo de producto `seasonal` en los productos relevantes con el valor `summer` (este es un valor de metacampo, no una etiqueta de producto).

![Modal para añadir metacampos de productos, incluido el metacampo seasonal con el valor summer.]({% image_buster /assets/img/shopify/summer_product_metafield.png %}){: style="max-width:80%;"}

{: start="2"}
2. En Braze, habilita la sincronización de metacampos y selecciona `custom.seasonal` (o el espacio de nombres y la clave que coincidan con tu metacampo de Shopify).

![Modal para seleccionar metacampos de productos, con un menú desplegable expandido que tiene cuatro elementos seleccionados, incluido custom.seasonal.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

### Personalización

1. Crea una [selección de catálogo]({{site.baseurl}}/catalog_selections) que filtre por metacampos que incluyan el valor correspondiente.

![Una selección de catálogo que filtra por metacampos que tienen el atributo summer.]({% image_buster /assets/img/shopify/metafields_selection.png %})

{: start="2"}
2. En el creador de mensajes, añade la selección donde quieras incluir los metacampos de productos. Por ejemplo, podrías usar un bloque de producto HTML como este:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

O, si quieres mencionar productos específicos con un valor de metacampo específico en una notificación push, puedes usar la herramienta **Add Personalization** y especificar los artículos de tu catálogo.

{% raw %}
```liquid
Check out the latest summer products:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Creador de notificaciones push con una selección de catálogo que incluye tres artículos usando una selección basada en metacampos.]({% image_buster /assets/img/shopify/add_personalization_metafields.png %})

### Segmentación de catálogo (SQL)

Usa las [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para crear segmentos basados en usuarios que interactuaron con un metacampo de producto. Por ejemplo, para encontrar usuarios que desencadenaron un evento de comercio electrónico con un producto cuya matriz de metacampos contiene un valor específico, usa esta consulta:

{% raw %}
```sql
-- -----------------------------------------------------------------------------
-- When the metafield is stored as a JSON array in catalog field_value (for example,
-- '["winter","summer"]' or a list-type Shopify metafield serialized to JSON),
-- use ARRAY_CONTAINS like product_tags. Cast the element you search for to
-- VARIANT so types match the parsed array elements.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product whose
-- metafield array contains a specific value (for example, segment on "seasonal").
-- For a date range, add events.time >= $start_date AND events.time <= $end_date.
-- For first/last triggered, reuse the CTE pattern from Template 3 with this
-- ARRAY_CONTAINS predicate instead of items.field_value = '<metafield_value>'.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND ARRAY_CONTAINS('<array_element_value>'::VARIANT, TRY_PARSE_JSON(items.field_value));
```
{% endraw %}

Si quieres segmentar clientes que han realizado un pedido con metacampos de producto específicos, usa una de las siguientes plantillas SQL de extensiones de segmento (todo el tiempo, período de tiempo específico, primer o último evento desencadenado).

{% raw %}
```sql
-- =============================================================================
-- Segment Extension: Metafields × Ecommerce Events — Example SQL Templates
-- =============================================================================
-- Metafield column names in CATALOGS_ITEMS_SHARED follow:
--   field_name = 'metafield_<namespace>_<key>'
-- Replace placeholders: app_group_id, catalog_id, event name, and the metafield
-- field_name + value. For array-type metafield values, use ARRAY_CONTAINS
-- with TRY_PARSE_JSON(items.field_value) similar to the product_tags example.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Template 1: Map metafields to event triggers (all time)
-- -----------------------------------------------------------------------------
-- Users who have ever triggered the ecommerce event with a product that has
-- the given metafield value. Event-agnostic: change events.name for the
-- desired event (e.g. ecommerce.order_placed, ecommerce.product_viewed).
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who have engaged with catalog items that have a specific
-- product metafield. Joins the catalog to custom events by matching
-- events.properties.products (e.g. variant_id) to catalog items.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 2: Map metafields to event triggers (for a specific period)
-- -----------------------------------------------------------------------------
-- Same as Template 1, restricted to events within a time window. Use
-- $start_date and $end_date (Segment Extension parameters) or literal
-- Unix timestamps.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product that has
-- the given metafield value within the specified time range.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND events.time >= $start_date
    AND events.time <= $end_date
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 3: Map metafields — first or last triggered an event
-- -----------------------------------------------------------------------------
-- Users for whom the *first* (earliest) or *last* (most recent) matching
-- event (by time) involved a product with the given metafield. Switch
-- ORDER BY to time ASC for first, time DESC for last.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users whose first (or last) occurrence of the ecommerce event
-- involved a catalog item with the specified metafield value.
WITH events_with_catalog_metafield AS (
    SELECT
        events.user_id,
        events.time,
        events.id AS event_id,
        ROW_NUMBER() OVER (
            PARTITION BY events.user_id
            ORDER BY events.time ASC   -- use DESC for "last triggered"
        ) AS rn
    FROM
        USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
        LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
        JOIN CATALOGS_ITEMS_SHARED AS items ON (
            (
                items.field_name = 'id'
                AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
            items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
        )
    WHERE
        events.name = 'ecommerce.order_placed'
        AND events.app_group_id = '<app_group_id>'
        AND items.catalog_id = '<catalog_id>'
        AND items.field_name = '<metafield_name>'
        AND items.field_value = '<metafield_value>'
)
SELECT
    user_id
FROM
    events_with_catalog_metafield
WHERE
    rn = 1;
```
{% endraw %}

{% endtab %}
{% tab Colecciones %}

Usa las colecciones de Shopify para incluir agrupaciones de productos seleccionados en tus mensajes que también se utilizan en tu sitio y experiencias de la aplicación de Shopify. Por ejemplo, destaca "Novedades" en un correo electrónico promocional, realiza ventas cruzadas de "Los más vendidos" en un Canvas de carrito abandonado, o segmenta usuarios que navegaron por una colección de temporada.

### Selección de catálogo

1. En Shopify, crea una colección "New Women's Products - In Stock" con tus productos de mejor rendimiento.

![Lista de colecciones de Shopify, incluida "New Women's Products - In Stock".]({% image_buster /assets/img/shopify/shopify_collections.png %})

{: start="2"}
2. En Braze, habilita la sincronización de colecciones y selecciona "Women's Products - In Stock".

![Modal para seleccionar colecciones, con un menú desplegable expandido que selecciona cuatro colecciones.]({% image_buster /assets/img/shopify/select_collections_id.png %})

{% alert note %}
Para las colecciones de Shopify, debes usar el **Collection ID**, que se encuentra en la URL cuando ves la colección. Por ejemplo, una URL de `https://admin.shopify.com/store/se-team-ecommerce/collections/470645342446` tiene el Collection ID `470645342446`.
{% endalert %}

### Personalización

{% alert note %}
Al hacer referencia a IDs de colección en selecciones de catálogo, usa solo el valor numérico del ID sin los corchetes de matriz `[]` que aparecen en los datos del catálogo. Por ejemplo, si los IDs de colección se muestran como `[123456789012, 987654321098]` en tu catálogo, escribe solo el ID numérico (como `470645342446`) en tu filtro de selección.
{% endalert %}

1. Crea una selección de catálogo llamada "New Women's Products - In Stock" que esté filtrada con productos que tengan el ID de esa colección. Solo puedes usar un campo de matriz único dentro de una sola selección de catálogo, y hasta 50 productos en tu colección.
 - También puedes crear tus propias selecciones personalizadas filtrando con el campo **Collections**.

![Una selección de catálogo que filtra por colecciones que tienen el atributo de Collection ID "470645342446".]({% image_buster /assets/img/shopify/collections_selection.png %})

{: start="2"}
2. En tu mensaje, incluye tu colección usando la selección creada o haciendo referencia directa a la colección. Por ejemplo, podrías usar un bloque de producto HTML como este:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
      {% if url == blank %}
      <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      {% else %}
      <a href="{{ url }}" style="text-decoration:none;">
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      </a>
      {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

O, si quieres mencionar productos nuevos específicos en una notificación push, puedes usar la herramienta **Add Personalization** y especificar los artículos de tu catálogo.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Creador de notificaciones push con una selección de catálogo que incluye tres artículos con una etiqueta de producto.]({% image_buster /assets/img/shopify/add_personalization_collections.png %})

### Segmentación de catálogo (SQL)

Crea un segmento de usuarios que interactuaron con una colección. Usa las [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para crear segmentos basados en la pertenencia a una colección. Por ejemplo, para encontrar usuarios que compraron productos de una colección específica en el último año, usa esta consulta:

{% raw %}
```json
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific collection ID. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'collection_ids' AND ARRAY_CONTAINS('<collection_ids_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% endtabs %}

{% alert tip %}
También puedes configurar [notificaciones de bajada de precios]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) y [notificaciones de reposición de existencias]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications).<br><br> Ten en cuenta que para cada caso de uso, debes crear un evento personalizado que capture el estado de suscripción de un usuario en tu catálogo. El evento personalizado requiere una propiedad del evento que se corresponda con el <a href="/docs/partners/ecommerce/shopify/shopify_catalogs#step-2-select-your-product-identifier">SKU o el ID de variante de Shopify</a> que hayas seleccionado como parte de la sincronización de tu producto de Shopify.
{% endalert %}

## Desactivar la sincronización de productos {#deactivate}

Desactivar la característica de sincronización de productos de Shopify eliminará todo tu catálogo y productos. Esto también puede afectar a cualquier mensaje que pueda estar utilizando activamente los datos de producto de este catálogo. Confirma que has actualizado o pausado estas Campaigns o Canvas antes de la desactivación, ya que esto podría dar lugar al envío de mensajes sin detalles del producto. No elimines el catálogo de Shopify directamente en la página de catálogos.

## Solución de problemas {#troubleshooting}

Si la sincronización de tu producto de Shopify se encuentra con un error, podría ser el resultado de los siguientes errores. Sigue las instrucciones para corregir el problema y resolver la sincronización:

| Error | Causa | Solución |
| --- | --- | --- |
| Error del servidor | Esto ocurre si hay un error de servidor por parte de Shopify cuando intentamos sincronizar tus productos. | [Desactiva la sincronización](#deactivate) y vuelve a sincronizar todo tu inventario de productos. |
| SKU duplicado | Esto ocurre si utilizas un SKU como ID de artículo del catálogo y múltiples variantes comparten el mismo SKU. Cada `item_id` del catálogo debe ser único, por lo que los artículos afectados pueden no sincronizarse, acumular registros de error o tener información de producto anulada involuntariamente. | Audita tu lista completa de productos y variantes en Shopify para asegurarte de que no hay SKU duplicados. Si los hay, actualízalos para que sean SKU únicos solo en la cuenta de tu tienda Shopify. Una vez corregido esto, [desactiva la sincronización](#deactivate) y vuelve a sincronizar todo tu inventario de productos. |
| Límite de catálogo superado | Esto ocurre si superas el límite de tu catálogo. Braze no podrá finalizar la sincronización o mantenerla activa debido a que no hay más almacenamiento disponible. | Hay dos soluciones a este problema:<br><br>1. Ponte en contacto con tu director de cuentas para subir de nivel y aumentar el límite de tu catálogo.<br><br>2. Libera espacio de almacenamiento eliminando cualquiera de los siguientes elementos:<br>- Artículos de otros catálogos<br>- Otros catálogos<br>- Selecciones creadas<br><br> Después de utilizar cualquiera de las dos soluciones, hay que desactivar la sincronización y volver a sincronizarla. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solución de problemas" }

Para más detalles sobre la validación de artículos de catálogo, consulta [Solución de problemas]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk#troubleshooting) en la documentación de la API de catálogos.