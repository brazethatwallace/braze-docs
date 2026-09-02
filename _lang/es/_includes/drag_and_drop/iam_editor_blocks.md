## Bloques de editor de mensajes dentro de la aplicación {#in-app-message-editor-blocks}

Los bloques de editor se encuentran en la sección **Build** para los mensajes dentro de la aplicación. Arrastra un bloque dentro de una columna; se ajustará automáticamente al ancho de la columna. Selecciona un bloque para editar su configuración en el panel de la derecha.

Para más información sobre cómo crear mensajes dentro de la aplicación en el **editor de arrastrar y soltar**, consulta [Crear un mensaje dentro de la aplicación con arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop).

### Título y párrafo {#title-and-paragraph}

Añade texto de título o párrafo al mensaje.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botón {#button}

Añade un botón estándar con estilo, enlaces y análisis configurables.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamiento al hacer clic {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Botón de radio {#radio-button}

Añade una lista de opciones entre las que los usuarios pueden seleccionar una. Cuando se envía, el perfil de usuario registra el [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) asociado, que debe ser una cadena para poder guardarse. Los atributos personalizados con otros tipos de datos no se guardan en el perfil de usuario.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Imagen {#image}

Inserta una imagen de la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

Para conocer las especificaciones de las imágenes, consulta nuestras [especificaciones de imágenes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#in-app-messages).

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Enlace {#link}

Inserta un hipervínculo en el que los usuarios pueden hacer clic para navegar a una URL específica. Se puede integrar en el texto o utilizarse de forma independiente.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaciador {#spacer}

Añade espacio o relleno entre otros bloques.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado {#custom-code}

Inserta HTML, CSS o JavaScript personalizados para una personalización avanzada.

| Propiedad | Descripción |
| --- | --- |
| Código personalizado | Te permite añadir, editar o eliminar HTML, CSS y JavaScript para un mensaje dentro de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

### Captura de teléfono {#phone-capture}

Inserta un campo de formulario para números de teléfono. Cuando se envía, el usuario queda suscrito al [grupo de suscripción de SMS]({{site.baseurl}}/sms_rcs_subscription_groups) o al [grupo de suscripción de WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups).

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Captura de correo electrónico {#email-capture}

Inserta un campo de formulario para direcciones de correo electrónico. Cuando se envía, la dirección de correo electrónico se añade al perfil de ese usuario en Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texto corto {#short-text}

Inserta un campo de formulario que admite atributos estándar (como nombre y apellido) o una cadena de atributo personalizado de tu elección.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Desplegable {#dropdown}

Inserta un menú desplegable con una lista predefinida de elementos entre los que los usuarios pueden seleccionar uno. Puedes añadir cualquier cadena de atributos personalizados a la lista.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Casilla de verificación {#checkbox}

Inserta una casilla de verificación. Si el usuario marca la casilla, el [atributo personalizado booleano]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) del bloque se establece en `true`. Si no se marca, su atributo se establece en `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Grupo de casillas de verificación {#checkbox-group}

Los usuarios pueden seleccionar entre varias opciones. Los valores se establecen o se añaden a un [atributo personalizado de matriz]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) definido.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texto largo {#long-text}

Campo de texto multilínea para flujos de tipo cuestionario. Si no ves este bloque, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) o con tu CSM de Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze CSM.
-->

## Cosas que debes saber {#things-to-know}

- **Video:** El creador estándar no incluye un bloque de video dedicado. Usa **Código personalizado** para insertar un reproductor si es necesario. Para más información, consulta [Mensajes dentro de la aplicación: preguntas frecuentes]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).