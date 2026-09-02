---
nav_title: SDK or kit de desarrollo de software de Roku
article_title: Guía del repositorio del SDK or kit de desarrollo de software de Roku
page_order: 8
description: "Referencia del README del SDK or kit de desarrollo de software de Roku de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del SDK or kit de desarrollo de software de Roku {#roku-sdk-repository-guide}

## Acerca del SDK or kit de desarrollo de software de Roku de Braze {#about-the-braze-roku-sdk}

El SDK or kit de desarrollo de software de Roku de Braze te ayuda a integrar las capacidades de mensajería, análisis y participación de usuarios de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guía del desarrollador de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=roku)

## Integración inicial del SDK or kit de desarrollo de software {#initial-sdk-integration}

El SDK or kit de desarrollo de software de Roku de Braze te proporcionará una API para reportar información que se utilizará en análisis, segmentación y participación.

## Paso 1: Añadir archivos {#step-1-add-files}

1. Añade `BrazeSDK.brs` a tu aplicación en el directorio `source`.
2. Añade `BrazeTask.brs` y `BrazeTask.xml` a tu aplicación en el directorio `components`.

## Paso 2: Añadir referencias {#step-2-add-references}

Añade una referencia a `BrazeSDK.brs` en tu escena principal utilizando el siguiente elemento `script`:

``` text
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Paso 3: Configurar {#step-3-configure}

En `main.brs`, establece la configuración de Braze en el nodo global:

``` text
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = "YOUR_API_KEY_HERE"
config[config_fields.ENDPOINT] = "YOUR_ENDPOINT_HERE (e.g. https://sdk.iad-01.braze.com/)"
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

## Paso 4: Inicializar Braze {#step-4-initialize-braze}

Inicializa la instancia de Braze:

``` text
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configuración de mensajes dentro de la aplicación {#in-app-message-setup}

Para procesar mensajes dentro de la aplicación, puedes añadir un observador en `BrazeTask.BrazeInAppMessage`:

``` text
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Después, dentro de tu controlador, tendrás acceso al mensaje dentro de la aplicación de mayor prioridad que hayan desencadenado tus campañas:

``` text
in_app_message = m.BrazeTask.BrazeInAppMessage
```

Luego puedes decidir qué hacer con el mensaje dentro de la aplicación. Algunos de los campos disponibles:

- `in_app_message.message` - El texto del cuerpo del mensaje dentro de la aplicación
- `in_app_message.buttons` - Lista de botones (podría ser una lista vacía).
- `in_app_message.id` - ID que se utiliza al registrar impresiones o clics
- `in_app_message.extras` - Pares clave/valor
- `in_app_message.image_url` - URL de la imagen
- `in_app_message.click_action` - Cuando no hay botones, esto es lo que debería ocurrir cuando el usuario hace clic en "OK" cuando se muestra el IAM. Puede ser "URI" o "NONE".
- `in_app_message.dismiss_type` - Puede ser "AUTO_DISMISS" o "SWIPE"
- `in_app_message.display_delay` - Cuánto tiempo (en segundos) esperar antes de mostrar el mensaje dentro de la aplicación
- `in_app_message.duration` - Cuánto tiempo (en milisegundos) debe mostrarse el mensaje cuando `dismiss_type` es "AUTO_DISMISS"
- `in_app_message.header` - El texto del encabezado del mensaje dentro de la aplicación
- `in_app_message.uri` - Cuando `click_action` es "URI", esto debería mostrarse

También hay varios campos de estilo que podrías elegir utilizar desde el panel. Alternativamente, podrías implementar el mensaje dentro de la aplicación y darle estilo dentro de tu aplicación Roku utilizando una paleta estándar.
- `in_app_message.bg_color` - Color de fondo
- `in_app_message.close_button_color` - Color del botón de cierre
- `in_app_message.frame_color` - El color de la superposición de la pantalla de fondo
- `in_app_message.header_text_color` - Color del texto del encabezado
- `in_app_message.message_text_color` - Color del texto del mensaje
- `in_app_message.text_align` - Puede ser "START", "CENTER" o "END"

Los campos de los botones incluyen:
- `buttons[0].click_action` - Puede ser "URI" para indicar que se abra el campo `uri`. Puede ser "NONE" para indicar que este botón debe cerrar el mensaje dentro de la aplicación.
- `buttons[0].id` - El valor del ID del propio botón
- `buttons[0].text` - El texto que se muestra en el botón
- `buttons[0].uri` - Cuando `click_action` es "URI", esto debería mostrarse
- `buttons[0].bg_color` - Color de fondo del botón
- `buttons[0].border_color` - Color del borde del botón
- `buttons[0].text_color` - Color del texto del botón

Cuando se muestra o se ve un mensaje, registra una impresión:

``` text
LogInAppMessageImpression(in_app_message.id, brazetask)
```

Una vez que un usuario hace clic en el mensaje, registra un clic:
``` text
LogInAppMessageClick(in_app_message.id, brazetask)
```
y luego procesa `in_app_message.click_action`

Si el usuario hace clic en un botón, registra el clic en el botón:

``` text
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```
y luego procesa `inappmessage.buttons[selected].click_action`

Después de procesar un mensaje dentro de la aplicación, debes borrar el campo:

``` text
m.BrazeTask.BrazeInAppMessage = invalid
```

## Integración básica del SDK or kit de desarrollo de software completada {#basic-sdk-integration-complete}

Braze debería estar recopilando datos de tu aplicación. Consulta nuestra documentación pública sobre cómo registrar atributos, eventos y compras en nuestro SDK or kit de desarrollo de software. La escena `MainScene.brs` de nuestra aplicación de ejemplo también contiene ejemplos de uso de la API.

`BrazeInAppMessage.brs` y `CustomSideBySideInAppMessage.brs` muestran ejemplos de manejo de In-App Messages. `onInAppMessageTriggered()` en `MainScene.brs` muestra cómo admitir múltiples diseños.

## Referencia adicional {#additional-reference}

El directorio `torchietv` contiene una aplicación de ejemplo con el SDK or kit de desarrollo de software de Braze integrado.
<!-- END GENERATED README CONTENT -->

Para detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-roku-sdk](https://github.com/braze-inc/braze-roku-sdk).