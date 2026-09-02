{% multi_lang_include developer_guide/prerequisites/roku.md %} Además, los mensajes dentro de la aplicación solo se enviarán a dispositivos Roku que ejecuten la versión mínima compatible del SDK or kit de desarrollo de software:

{% sdk_min_versions roku:0.1.2 %}

## Tipos de mensajes {#message-types}

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Habilitar mensajes dentro de la aplicación {#enabling-in-app-messages}

### Paso 1: Añadir un observador {#step-1-add-an-observer}

Para procesar mensajes dentro de la aplicación, puedes añadir un observador en `BrazeTask.BrazeInAppMessage`:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### Paso 2: Acceder a mensajes desencadenados {#step-2-access-triggered-messages}

Después, dentro de tu controlador, tendrás acceso al mensaje dentro de la aplicación de mayor prioridad que hayan desencadenado tus campañas:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Campos de mensaje {#message-fields}

### Manejo {#handling}

A continuación se enumeran los campos que necesitarás para gestionar tus mensajes dentro de la aplicación:

| Campos | Descripción |
| ------ | ----------- |
| `buttons` | Lista de botones (puede ser una lista vacía). |
| `click_action` | `"URI"` o `"NONE"`. Utiliza este campo para indicar si el mensaje dentro de la aplicación debe abrirse con un enlace URI o cerrar el mensaje al hacer clic. Cuando no hay botones, esto debería ocurrir cuando el usuario hace clic en "Aceptar" cuando se muestra el mensaje dentro de la aplicación. |
| `dismiss_type` | `"AUTO_DISMISS"` o `"SWIPE"`. Utiliza este campo para indicar si tu mensaje dentro de la aplicación se descartará automáticamente o si será necesario deslizar para descartarlo. |
| `display_delay` | Cuánto tiempo (segundos) hay que esperar hasta que aparezca el mensaje dentro de la aplicación. |
| `duration` | Cuánto tiempo (milisegundos) debe mostrarse el mensaje cuando `dismiss_type` está configurado en `"AUTO_DISMISS"`. |
| `extras` | Pares clave-valor. |
| `header` | El texto del encabezado. |
| `id` | El ID utilizado para registrar impresiones o clics. |
| `image_url` | URL de la imagen del mensaje dentro de la aplicación. |
| `message` | Texto del cuerpo del mensaje. |
| `uri` | La URI a la que se enviará a los usuarios en función de tu `click_action`. Este campo debe incluirse cuando `click_action` es `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Handling" }

{% alert important %}
Para los mensajes dentro de la aplicación que contengan botones, el `click_action` del mensaje también se incluirá en la carga útil final si la acción de clic se añade antes de añadir el texto del botón.
{% endalert %}

### Estilo {#styling}

También hay varios campos de estilo que puedes utilizar desde el dashboard:

| Campos | Descripción |
| ------ | ----------- |
| `bg_color` | Color de fondo. |
| `close_button_color` | Color del botón de cierre. |
| `frame_color` | El color de la superposición de la pantalla de fondo. |
| `header_text_color` | Color del texto del encabezado. |
| `message_text_color` | Color del texto del mensaje. |
| `text_align` | "START", "CENTER" o "END". La alineación de texto seleccionada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Styling" }

Alternativamente, puedes implementar el mensaje dentro de la aplicación y darle estilo dentro de tu aplicación Roku utilizando una paleta estándar:

### Botones {#buttons}

| Campos | Descripción |
| ------ | ----------- |
| `click_action` | `"URI"` o `"NONE"`. Utiliza este campo para indicar si el mensaje dentro de la aplicación debe abrirse con un enlace URI o cerrar el mensaje al hacer clic. |
| `id` | El valor de ID del propio botón. |
| `text` | El texto que se mostrará en el botón. |
| `uri` | La URI a la que se enviará a los usuarios en función de tu `click_action`. Este campo debe incluirse cuando `click_action` es `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buttons" }