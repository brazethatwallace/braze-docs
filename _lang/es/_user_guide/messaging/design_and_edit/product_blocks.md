---
nav_title: Bloques de producto
article_title: Bloques de producto de arrastrar y soltar
page_order: 5
description: "Este artículo de referencia trata sobre los bloques de producto de arrastrar y soltar, que permiten a los usuarios añadir y configurar rápidamente escaparates dinámicos o estáticos de artículos del catálogo."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Bloques de producto de arrastrar y soltar {#drag-and-drop-product-blocks}

> El editor de arrastrar y soltar te permite añadir y configurar rápidamente bloques de producto en tus mensajes para mostrar productos fácilmente, sin necesidad de crear código Liquid personalizado.

{% alert important %}
La característica de bloques de producto de arrastrar y soltar se encuentra en fase de acceso anticipado y, por el momento, solo está disponible para el correo electrónico. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos {#requirements}

| Requisito | Descripción |
| --- | --- |
| Eventos recomendados de comercio electrónico | Los [eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_events) proporcionan esquemas de datos estandarizados para eventos de comportamiento clave que se producen antes y después de realizar un pedido. Estos eventos acabarán sustituyendo al antiguo evento de compra de Braze y se convertirán en el estándar para el seguimiento del comportamiento relacionado con el comercio. <br><br> Los eventos recomendados de comercio electrónico son necesarios para los bloques de producto dinámicos. |
| Plantillas de Canvas de comercio electrónico | Los eventos recomendados de comercio electrónico son compatibles con plantillas prediseñadas, incluyendo plantillas de Canvas de comercio electrónico diseñadas para casos de uso esenciales como navegación abandonada, carritos abandonados y confirmaciones de pedido. <br><br>Si planeas implementar alguno de estos casos de uso esenciales de comercio electrónico utilizando las [plantillas de Canvas de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases), debes usar o seguir la plantilla de Canvas proporcionada. |
| Catálogo de Braze | Debes crear un catálogo de Braze que incluya los siguientes campos, que usarás en la configuración de tu bloque de producto:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| Selección de catálogo | Para los bloques de producto estáticos, debes crear una [selección de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para especificar qué productos incluir en tu bloque de producto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Tipos de bloques de producto de arrastrar y soltar {#types-of-drag-and-drop-product-blocks}

| Bloque de producto | Propósito | Casos de uso | Disponibilidad |
| --- | --- | --- | --- |
| Dinámico | Personaliza tu mensajería con un escaparate de productos basado en las interacciones del cliente utilizando [eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_events) y catálogos dentro de nuestras [plantillas de Canvas de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases). | {::nomarkdown}<ul><li>Navegación abandonada</li><li>Carrito abandonado</li><li>Pago abandonado</li><li>Confirmaciones de pedido</li></ul>{:/} | Disponible solo en Canvas. |
| Estático | Personaliza productos usando datos almacenados en un catálogo de Braze. Debes usar una [selección de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para especificar qué productos incluir. | Perfecto para presentar lanzamientos de nuevos productos u ofertas específicas por categoría. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tipos de bloques de producto de arrastrar y soltar" }

## Configuración de contenido del bloque de producto {#product-block-content-configuration}

Cada tipo de bloque tiene diferentes configuraciones de contenido.

### Campos de producto {#product-fields}

En la sección **Product Fields**, selecciona tu tipo de bloque de producto y luego activa los campos que deseas incluir para cada producto. Cada campo se obtiene de diferentes fuentes según el tipo de bloque de producto que selecciones.

#### Bloque de producto dinámico {#dynamic-product-block}

| Campo de producto | Fuente |
| --- | --- |
| Imagen de variante | Catálogos |
| Título del producto | Catálogos |
| Botón para URL del producto | Catálogos |
| Precio | Propiedad de evento recomendado de comercio electrónico |
| Cantidad | Propiedad de evento recomendado de comercio electrónico |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bloque de producto dinámico" }

![Campos de producto para un bloque de producto dinámico, que se dividen en datos de catálogo y datos de evento.]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Bloque de producto estático {#static-product-block}

| Campo de producto | Fuente |
| --- | --- |
| Imagen de variante | Catálogos |
| Título del producto | Catálogos |
| Botón para URL del producto | Catálogos |
| Precio | Catálogos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bloque de producto estático" }

![Campos de producto para un bloque de producto estático, que están todos categorizados como datos de catálogo.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Opciones de diseño {#layout-options}

Usa las opciones de diseño para personalizar cómo se muestran tus productos dentro de tu bloque de producto.

| Opción | Descripción |
| --- | --- |
| Orientación del producto | Elige cómo se orientan la imagen y los campos de producto dentro del bloque. |
| Alineación | Ajusta la alineación de los campos de texto y el botón dentro del bloque. |
| Máximo de productos por fila | Muestra hasta tres productos por fila, hasta 12 productos en total para bloques de producto estáticos y hasta 24 productos en total para bloques de producto dinámicos. |
| Espaciado entre productos | Establece el espaciado entre productos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Opciones de diseño" }

![Opciones de diseño para orientación del producto, alineación, máximo de productos por fila y espaciado entre productos.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Configuración global de estilo de correo electrónico {#global-email-style-settings}

La [configuración global de estilo de correo electrónico]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) te permite aplicar un estilo consistente a tus correos electrónicos dentro de Braze. Esto significa que puedes definir estilos específicos, como fuentes, colores y diseños de botones, que se aplicarán automáticamente a todos tus correos electrónicos.

#### Cómo funciona la configuración global de estilo de correo electrónico con los bloques de producto {#how-global-email-style-settings-work-with-product-blocks}

Los estilos existentes para párrafos y botones se aplican automáticamente a los elementos de texto y botón dentro del bloque de producto. Esto significa que tu bloque de producto utiliza de forma consistente cualquier formato que hayas establecido para párrafos y botones, manteniendo una apariencia cohesiva en todo tu correo electrónico.

## Configuración de bloques de producto {#setting-up-product-blocks}

### Configuración del catálogo {#catalog-setup}

{% alert important %}
Si estás usando la integración de Braze y Shopify para la [sincronización de productos]({{site.baseurl}}/shopify_catalogs), no necesitas realizar ningún paso adicional para usar los bloques de producto de arrastrar y soltar.<br><br> Si no tienes información de variantes de producto, necesitas duplicar la información del producto de nivel superior tanto en los campos de producto como en los campos de variante de producto dentro de las cargas útiles de eventos y catálogos. Esto significa que necesitas proporcionar los mismos detalles del producto para ambos identificadores a fin de mantener la consistencia y que el bloque de producto funcione correctamente.
{% endalert %}

Para usar los bloques de producto de arrastrar y soltar, necesitas configurar un catálogo de Braze que incluya valores de campos específicos. Usarás estos campos en la configuración de tu bloque de producto. Asegúrate de que tu catálogo incluya los siguientes campos:

| Campo | Descripción |
| --- | --- |
| `product_title` | El título del producto. |
| `product_url` | La URL donde los clientes pueden ver o comprar el producto. |
| `variant_image_url` | La URL de la imagen de la variante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración del catálogo" }

Empieza rápidamente trabajando con este [catálogo de productos de ejemplo](/docs/assets/download_file/ecommerce_product_catalog_sample.csv), que incluye los campos obligatorios.

![Un archivo CSV de ejemplo con los campos obligatorios además de otros.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### Mapeado a campos del catálogo {#mapping-to-catalog-fields}

En la pestaña **Configuración** de tu catálogo, puedes seleccionar el interruptor **Product blocks** para mapear a campos e información específicos en tu catálogo. Esto te permite seleccionar qué campos usar como título del producto, URL del producto y URL de la imagen. Ten en cuenta que los campos del catálogo de Shopify están mapeados de forma predeterminada y no se pueden cambiar.

{% alert note %}
Si no estás usando Shopify, puedes ponerte en contacto con tu director de cuentas para activar el mapeado de campos, lo que te permite conectar cualquier catálogo a los bloques de producto y mapear sus campos a `product_title`, `product_url` y `variant_image_url`.
{% endalert %}

## Creación de bloques de producto {#creating-product-blocks}

Esta guía te llevará a través de los pasos para crear, probar y asegurar la funcionalidad de un bloque de producto dinámico o estático usando nuestro editor de correo electrónico de arrastrar y soltar.

### Paso 1: Crea una Campaign de correo electrónico o un paso de correo electrónico en Canvas {#step-1-create-an-email-campaign-or-email-canvas-step}

#### Bloque de producto dinámico

{% alert note %}
Los bloques de producto dinámicos requieren [eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_events) y solo se pueden usar dentro de [Canvas]({{site.baseurl}}/ecommerce_use_cases). Para los usuarios de Braze con Shopify, estos eventos se incluyen automáticamente como parte de la integración. Para los usuarios que no usan Shopify, necesitas trabajar con tus desarrolladores para pasar estos eventos a Braze y asegurarte de que el identificador principal del producto dentro de los eventos se añada como el ID del artículo del catálogo.
{% endalert %}

Crea un nuevo Canvas que use una de las plantillas de Braze disponibles para tu caso de uso específico:
- Navegación abandonada
- Carrito abandonado
- Pago abandonado
- Confirmaciones de pedido

Para instrucciones detalladas sobre cómo crear tus Canvas de comercio electrónico, consulta [casos de uso de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases).

#### Bloque de producto estático

Crea una Campaign de correo electrónico de arrastrar y soltar, un Canvas basado en acciones o una plantilla que tenga un paso de mensaje de correo electrónico de arrastrar y soltar.

### Paso 2: Añade un bloque de producto {#step-2-add-a-product-block}

{% tabs %}
{% tab Bloque de producto dinámico %}

Dentro del paso de mensaje, crea un correo electrónico o modifica la plantilla existente usando el compositor de correo electrónico de arrastrar y soltar.
Arrastra un bloque de producto a tu mensaje de correo electrónico.
Confirma que el tipo de bloque dinámico está seleccionado.
Selecciona el catálogo de productos que deseas usar para la personalización. Asegúrate de que esté alineado con los productos de los eventos de entrada que estás segmentando.

{% endtab %}
{% tab Bloque de producto estático %}

Arrastra un bloque de producto a tu mensaje de correo electrónico y selecciona el tipo de bloque estático.
Selecciona el catálogo que deseas usar para tu bloque de producto. Debes seleccionar una selección de catálogo para especificar qué productos se muestran en tu bloque de producto.

{% endtab %}
{% endtabs %}

![La pestaña "Contenido" que contiene bloques de editor, como bloques de producto.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Paso 3: Configura los campos de producto {#step-3-configure-product-fields}

Selecciona qué [campos de producto](#product-fields) deben mostrarse en el bloque de producto. Selecciona **Apply Settings** después de cada cambio para ver las actualizaciones en el editor.

También puedes personalizar el texto antes de tus etiquetas de Liquid. Por ejemplo, puedes anteponer un signo de dólar ($) al precio de un artículo o actualizar el término de cantidad a "monto" u otra etiqueta preferida.

![Bloque de producto con un signo de dólar antepuesto al precio del artículo.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Paso 4: Configura los ajustes de diseño {#step-4-configure-layout-settings}

Cambia las [opciones de diseño](#layout-options) para actualizar cómo se muestran los productos dentro de tu bloque de producto, y asegúrate de seleccionar **Apply Settings** después de cada cambio.

### Paso 5: Previsualiza y prueba tu mensaje {#step-5-preview-and-test-your-message}

{% tabs %}
{% tab Bloque de producto dinámico %}

1. En la sección **vista previa & Test**, previsualiza el mensaje como un usuario personalizado.
2. Especifica cuántos artículos deseas renderizar en la vista previa.
3. Confirma que aparece el número correcto de artículos y que tus opciones de diseño se aplican correctamente. Ten en cuenta que los artículos que aparecen se seleccionan aleatoriamente.

![Pestaña "Vista previa como usuario" con una sección desplegable "Bloque de producto dinámico" que especifica mostrar 4 artículos.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Bloque de producto estático %}

Se generará una vista previa dentro del compositor de arrastrar y soltar cuando apliques cambios a tu bloque de producto.

![Compositor de correo electrónico de arrastrar y soltar mostrando un bloque de producto generado con diferentes mosaicos de artículos.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Cuando hayas terminado de crear tu mensaje y confirmes que se ve como esperabas, ¡estás listo para enviar!