## Bloques del editor de Banner {#banner-editor-blocks}

En el compositor de Banner, arrastra filas y bloques desde la sección **Build** al canvas para diseñar tu mensaje. Selecciona **Styles** para ajustar el estilo a nivel de página, o selecciona un bloque o fila para editar sus propiedades en el panel lateral.

Para ver el flujo completo de creación de un Banner, consulta [Crear un Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner).

El compositor de Banner ofrece los mismos tipos de bloques de diseño que otras superficies de arrastrar y soltar, pero no el conjunto completo de bloques de formulario (por ejemplo, no incluye bloques de botón de opción, texto corto, menú desplegable ni casilla de verificación). Puedes añadir bloques de **Phone capture** y **Email capture**; solo se permite **un** bloque de captura de teléfono y **un** bloque de captura de correo electrónico por mensaje.

### Título y párrafo {#title-and-paragraph}

Añade texto de encabezado o cuerpo con opciones de texto enriquecido.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botón {#button}

Añade un botón en el que se puede hacer clic. Puedes configurar enlaces y opciones de análisis en el panel de propiedades.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamiento de clic {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

Para más información, consulta [Definir el comportamiento de clic]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional) en el artículo de Banner.

### Imagen {#image}

Muestra una imagen desde una URL alojada. Configura las opciones de visualización en el panel de propiedades.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportamiento de clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Enlace {#link}

Inserta un hipervínculo que los usuarios pueden seleccionar.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamiento de clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaciador {#spacer}

Añade espacio vertical entre bloques.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado {#custom-code}

Inserta HTML personalizado para diseños avanzados o contenido incrustado (por ejemplo, video). Los clics dentro de HTML personalizado no se rastrean a menos que llames a `brazeBridge.logClick()` — consulta [Código personalizado y puente JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/).

| Propiedad | Descripción |
| --- | --- |
| Código personalizado | Añade o edita HTML (y activos relacionados) para el Banner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

### Captura de teléfono {#phone-capture}

Recopila un número de teléfono. Al enviar, suscribe al usuario a tu grupo de suscripción de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) o [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) seleccionado. Solo uno por Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Captura de correo electrónico {#email-capture}

Recopila una dirección de correo electrónico y la añade al perfil de Braze del usuario al enviar. Solo uno por Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texto largo {#long-text}

Campo de texto multilínea para flujos de tipo cuestionario. Si no ves este bloque, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) o tu administrador del éxito del cliente de Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Cosas que debes saber {#things-to-know}

- **Video:** El compositor estándar no incluye un bloque de video dedicado. Usa **Custom code** para incrustar un reproductor si es necesario. Para más información, consulta [Banners: preguntas frecuentes]({{site.baseurl}}/user_guide/channels/banners/faq/).
- **Liquid:** La mayoría de Liquid es compatible; hay excepciones como las etiquetas de rerenderizado de Catálogo. Para más información, consulta [Banners: preguntas frecuentes]({{site.baseurl}}/user_guide/channels/banners/faq/).