---
nav_title: Códigos de descuento únicos
article_title: Enviar códigos de descuento únicos
alias: /shopify_discount_codes/
page_order: 7
description: "Este artículo de referencia cubre un caso de uso enviado por la comunidad sobre el uso de códigos promocionales de Braze con el Bot de código de descuento masivo de Shopify para enviar códigos de descuento únicos a través de tus Campaigns y Canvas."
---

# Envía códigos de descuento únicos a través de Shopify {#send-unique-discount-codes-through-shopify}

> Este caso de uso enviado por la comunidad muestra cómo utilizar los [códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/) de Braze con el Bot de código de descuento masivo de Shopify para generar códigos de descuento únicos para tus Campaigns y Canvas. Los códigos de descuento únicos ayudan a evitar la explotación de códigos promocionales genéricos.

{% alert important %}
Se trata de una integración enviada por la comunidad y no está soportada directamente por Braze. El Bot de códigos de descuento masivo es compatible directamente con Shopify. Braze solo admite códigos promocionales de Braze.
{% endalert %}

## Requisitos {#requirements}

| Requisito | Descripción |
| --- | --- |
| Configurar una tienda Shopify | Confirma que ya has [configurado una tienda Shopify con Braze]({{site.baseurl}}/shopify_overview/). |
| Instalar la aplicación Bulk Discount Code Bot | Descarga la aplicación [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) en la tienda de aplicaciones de Shopify. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Generar códigos de descuento únicos {#generating-unique-discount-codes}

### Paso 1: Configura tus códigos de descuento {#step-1-configure-your-discount-codes}

Utiliza el Bot de códigos de descuento masivo para configurar tus códigos de descuento en función del número de códigos a generar, la longitud del código, el valor del descuento y mucho más.

![Las opciones de configuración de un conjunto de descuentos.][1]

### Paso 2: Exporta tus códigos {#step-2-export-your-codes}

Busca tu conjunto de descuentos en la barra de búsqueda del Bot de códigos de descuento masivo y, a continuación, selecciona **Export Codes** > **Download Codes** para descargar un archivo CSV a tu carpeta de descargas.

![Barra de búsqueda con un desplegable que muestra el conjunto de descuentos y una fila de botones para seleccionar.][2]{: style="max-width:70%;"}

En el archivo CSV, elimina la fila 1 para quitar el encabezado de columna "Promo". Esto evitará que "Promo" se convierta en un código de descuento en Braze.

![Diagrama de flujo que muestra la eliminación del encabezado de fila "Promo" en un archivo CSV.][3]{: style="max-width:60%;"}

### Paso 3: Añade tus códigos de descuento a Braze {#step-3-add-your-discount-codes-to-braze}

En Braze, ve a **Data Settings** > **Promotion Codes** > **Create Promotion Code List** y [configura tu lista de códigos de descuento]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/#creating-a-promotion-code-list). Asegúrate de que coincide con la fecha de caducidad configurada por el Bot de código de descuento masivo.

A continuación, carga tu archivo CSV y selecciona **Save List**.

### Paso 4: Añade tus códigos de descuento a una Campaign o un paso en Canvas de Braze {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

Si quieres utilizar tus códigos de descuento únicos en una Campaign de envío único, o no te importa que los usuarios reciban varios códigos únicos en diferentes Campaigns o pasos en Canvas, copia el fragmento de código Liquid de la lista de códigos promocionales que guardaste.

![Un fragmento de código Liquid con un botón para copiarlo.][4]{: style="max-width:60%;"}

Pega el fragmento de código Liquid en una Campaign o paso en Canvas.

![Un GIF que muestra el fragmento de código Liquid añadido a un paso en Canvas.][5]

Si quieres que los usuarios reciban un único código de descuento, independientemente de cuántas veces se haga referencia al código de descuento en Campaigns o Canvas, crea un paso de [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) directamente antes del primer paso de mensaje que asigne el código de descuento a un atributo personalizado, como "Promo Code".

{% alert tip %}
También puedes [crear un atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) yendo a **Data Settings** > **Custom Attributes**.
{% endalert %}

En el paso Actualización de usuario, haz lo siguiente para cada campo:
- **Attribute Name:** Selecciona **Promo Code**.
- **Action:** Selecciona **Update**.
- **Key Value:** Pega el fragmento de código Liquid.

![Un paso de Actualización de usuario que actualiza un atributo "Promo Code" con el fragmento de código Liquid.][6]

Ahora, puedes añadir el atributo personalizado {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} a cualquier mensaje, y el código de descuento se insertará automáticamente en la plantilla.

## Comportamiento del código de descuento {#discount-code-behavior}

{% details Campaign multicanal o paso en Canvas %}

Cuando se utiliza un fragmento de código de descuento en una Campaign multicanal o en un paso en Canvas, los usuarios siempre reciben un código único. Si un usuario es elegible para recibir un código a través de más de un canal, recibirá el mismo código a través de cada canal. En otras palabras, un usuario elegible solo recibiría un código en todos los mensajes enviados por esa Campaign o paso en Canvas.

{% enddetails %}

{% details Diferentes pasos en Canvas o Campaigns separadas %}

Cuando se hace referencia a un código de descuento mediante varios pasos en el mismo Canvas o mediante Campaigns separadas, un usuario elegible recibirá varios códigos promocionales únicos (un código por cada paso en Canvas o Campaign).

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}