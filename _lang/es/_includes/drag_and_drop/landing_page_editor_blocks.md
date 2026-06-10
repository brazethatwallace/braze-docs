## Bloques del editor de páginas de inicio {#landing-page-editor-blocks}

Los bloques del editor para páginas de inicio se encuentran en la sección **Build** del **Editor de arrastrar y soltar**, en **Rows** y categorías de bloques. Arrastra un bloque a la columna de una fila; se ajusta automáticamente al ancho de la columna. Selecciona un bloque para editar su configuración en el panel de propiedades del lado derecho.

Para más información sobre cómo crear y publicar páginas de inicio, consulta [Crear páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

### Título y párrafo {#title-and-paragraph}

Añade texto de encabezado o cuerpo. Útil para estructurar secciones y mejorar la legibilidad.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botón {#button}

Añade un elemento sobre el que se puede hacer clic para acciones como abrir un enlace o enviar un formulario.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamiento al hacer clic {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
Si configuras un botón con **Submit form when button is clicked** y abres una URL web en una nueva pestaña, Safari en iOS puede bloquear la navegación. Abre la URL posterior al envío en la misma pestaña cuando envíes formularios. Para más información, consulta [Crear páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).
{% endalert %}

### Botón de opción {#radio-button}

Añade una lista de opciones de las cuales los usuarios pueden seleccionar una. Usa el panel de propiedades para configurar las opciones disponibles y el atributo personalizado que recibe el valor seleccionado. El perfil de usuario registra el valor seleccionado como un [atributo personalizado de cadena]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) cuando se envía el formulario. Los atributos personalizados con otros tipos de datos no se guardan en el perfil de usuario.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Imagen {#image}

Muestra una imagen desde una carga o una URL externa.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Enlace {#link}

Añade un hipervínculo que los usuarios pueden seleccionar para ir a una URL. Puede estar dentro de un texto o de forma independiente.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaciador {#spacer}

Añade espacio vertical entre elementos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado {#custom-code}

Inserta HTML, CSS o JavaScript personalizado para personalización avanzada, como [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages/#google-tag-manager).

| Propiedad | Descripción |
| --- | --- |
| Código personalizado | Te permite añadir, editar o eliminar HTML, CSS y JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Temporizador de cuenta regresiva {#countdown-timer}

Muestra una cuenta regresiva hasta una fecha y hora que establezcas. Si no ves este bloque, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) o tu administrador del éxito del cliente de Braze.

Después de añadir un bloque de **Temporizador de cuenta regresiva**, usa el panel de propiedades para establecer la fecha y hora objetivo, las etiquetas y el estilo.
-->

### Captura de correo electrónico {#email-capture}

Añade un campo de formulario para direcciones de correo electrónico. Al enviar, la dirección se guarda en el perfil de Braze del usuario.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Captura de teléfono {#phone-capture}

Añade un campo de formulario para números de teléfono. Al enviar, suscribe al usuario a tu grupo de suscripción de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) o [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) seleccionado.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Campo de entrada {#input-field}

Añade un campo de formulario para atributos estándar (por ejemplo, nombre o apellido) o una cadena de atributo personalizado.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Desplegable {#dropdown}

Una lista predefinida de elementos; los usuarios eligen uno. Puedes asignar valores a cadenas de atributos personalizados.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Casilla de verificación {#checkbox}

Cuando está marcada, establece el [atributo personalizado booleano]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) del bloque en `true`; cuando no está marcada, en `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Grupo de casillas de verificación {#checkbox-group}

Los usuarios eligen múltiples opciones; los valores establecen o se añaden a un [atributo personalizado de array]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) definido.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texto largo {#long-text}

Campo de texto multilínea para flujos de tipo cuestionario. Si no ves este bloque, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) o tu administrador del éxito del cliente de Braze. Este bloque no está disponible para páginas de inicio estándar.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Fila guardada {#saved-row}

Inserta una fila reutilizable que guardaste anteriormente como un Content Block de arrastrar y soltar. Las filas guardadas **no están vinculadas** al Content Block original: si el original se actualiza, tendrás que arrastrarlo de nuevo al editor para obtener la última versión. Para más información, consulta [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). Si no ves **Fila guardada** en **Rows**, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) o tu administrador del éxito del cliente de Braze.
-->

## Cosas que debes saber {#things-to-know}

- **Video:** El compositor estándar no incluye un bloque de video dedicado. Usa **Custom code** para insertar un reproductor si es necesario. Para más información, consulta [Páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/).