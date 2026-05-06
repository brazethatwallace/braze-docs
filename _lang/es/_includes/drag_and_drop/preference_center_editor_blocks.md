## Bloques del editor del centro de preferencias {#preference-center-editor-blocks}

Arrastra bloques desde la sección **Crear** a una fila en el editor del centro de preferencias de arrastrar y soltar. Cada bloque tiene su propia configuración; el panel del lado derecho cambia a propiedades o estilo del elemento seleccionado.

Antes de editar bloques, añade grupos de suscripción y configura el **smart block** de suscripción (ver más abajo). Para el flujo de configuración completo, consulta [Crear un centro de preferencias de correo electrónico con arrastrar y soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/).

### Título y párrafo {#title-and-paragraph}

Añade encabezados o texto del cuerpo con opciones de texto enriquecido.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botón {#button}

Añade un botón interactivo (por ejemplo, **Guardar** o navegación).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Imagen {#image}

Muestra una imagen de la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) o de una URL.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Espaciador {#spacer}

Añade espacio vertical entre bloques.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Grupos de suscripción (smart block) {#subscription-groups-smart-block}

Añade un bloque de plantilla que enumera los grupos de suscripción, controles opcionales de **Subscribe to all** / **Unsubscribe from all**, y descripciones. Configúralo después de añadir grupos en el flujo de trabajo del centro de preferencias.

Después de [añadir grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-3-add-subscription-groups-to-the-preference-center), selecciona el smart block en el lienzo para:

- Reordenar grupos de suscripción
- Añadir o quitar grupos
- Añadir o quitar descripciones
- Alternar **Subscribe to all** y **Unsubscribe from all** para los grupos en ese bloque

El control **Unsubscribe from all** en la parte inferior de la plantilla predeterminada es obligatorio y realiza una [cancelación de suscripción global]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-states) del correo electrónico.

## Cosas que debes saber {#things-to-know}

- **Estilos comunes:** Puedes establecer valores predeterminados para toda la página en **Common Styles** antes de ajustar bloques individuales. Para más información, consulta [Personalizar el centro de preferencias con el editor de arrastrar y soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Página de confirmación:** Cambia a **Confirmation Page** en la parte superior del editor para dar estilo a la experiencia posterior al guardado usando los mismos tipos de bloques.