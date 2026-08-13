---
nav_title: Guía de preparación
article_title: Guía de preparación de mensajes dentro de la aplicación
page_order: 0.5

page_type: reference
description: "Este artículo cubre preguntas y mejores prácticas a considerar antes de crear mensajes dentro de la aplicación, incluyendo segmentación, planificación, contenido y conversiones."
channel: in-app messages
toc_headers: h2
---

# Guía de preparación de mensajes dentro de la aplicación {#in-app-message-prep-guide}

> Antes de crear tus mensajes dentro de la aplicación, deberías considerar algunos de los siguientes temas para que la creación de tu mensaje sea rápida y sencilla.

## Consideraciones generales {#general-considerations}

- Si estás creando una Campaign, ¿cuántas variantes de este mensaje te gustaría mostrar? Para ideas sobre pruebas de variantes, consulta [Consejos para diferentes canales]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- Si estás creando un Canvas, ¿se combinará este mensaje con otros canales de mensajería en ese paso?
- ¿Cuándo te gustaría que [tu mensaje expire]({{site.baseurl}}/canvas_in-app_messages)?

## Consideraciones de segmentación {#targeting-considerations}

- Los mensajes dentro de la aplicación son ideales para usuarios que visitan tu aplicación con regularidad. ¿Estás incluyendo a esta audiencia?
- ¿Dónde quieres que tus usuarios vean tu mensaje? ¿En tu aplicación Web? ¿En tu aplicación móvil?
- ¿Qué evento debería desencadenar este mensaje?
- ¿Alguno de tus usuarios utiliza versiones anteriores de tu aplicación? Si es así, es posible que no puedan ver algunos elementos de tu mensaje.
- ¿Para qué tipo de dispositivo o dispositivos estás creando este mensaje? Recuerda que puedes obtener una vista previa de tu mensaje usando el cuadro de **vista previa** o la pestaña **Test**. Consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) para más información.

## Programación, retrasos e inicios de sesión {#scheduling-delays-and-session-starts}

Cuando una campaña de mensajes dentro de la aplicación tiene un **Retraso de programación** con un desencadenante en el inicio de sesión, un usuario que inicia una sesión y luego cierra la aplicación antes de que se muestre el mensaje dentro de la aplicación puede seguir recibiendo ese mensaje en el siguiente inicio de sesión, después de que expire el retraso.

Ese comportamiento puede producir una visualización inesperada, especialmente si no se selecciona **Reevaluar la elegibilidad de la campaña antes de mostrar** en la Campaign.

Por ejemplo, un usuario podría recibir un mensaje dentro de la aplicación con un retraso de ocho segundos un mes después del lanzamiento de la Campaign. Esto puede ocurrir si inició una sesión, la finalizó de inmediato, inició una sesión un mes después y luego, ocho segundos más tarde, recibió el mensaje dentro de la aplicación. Si se aleja de la aplicación sin cerrarla, el mensaje dentro de la aplicación se muestra cuando regresa a la aplicación.

## Consideraciones de contenido {#content-considerations}

- ¿Qué idiomas usarás en este mensaje?
- ¿Cuál es el texto de tu encabezado y cuerpo? ¿Son llamativos y relevantes para tu usuario?
- Los mensajes dentro de la aplicación solo aparecen durante un tiempo determinado. ¿Tu texto es conciso y memorable?
- ¿Usarás [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para agregar texto personalizado?
- ¿Los usuarios necesitan copiar el texto del mensaje (como un código de descuento o cupón)? En iOS y Android, los usuarios pueden mantener presionado el texto o los campos de entrada de texto para copiar contenido. Mantener presionado no funciona en imágenes, así que usa texto o campos de entrada de texto en lugar de imágenes que contengan códigos u otro texto que los usuarios puedan necesitar copiar.
- Para mensajes dentro de la aplicación a pantalla completa, ¿tu imagen u otro contenido multimedia está dentro de la [zona segura]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- Para mensajes dentro de la aplicación de tipo cuestionario, ¿quieres registrar atributos o envíos? ¿Has configurado tu página de confirmación?
- Para mensajes dentro de la aplicación con HTML personalizado, ¿tu HTML incluye codificación UTF-8 para mostrar correctamente los caracteres especiales? Consulta [Mensajes dentro de la aplicación con HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) para más detalles.
- Si incluyes video en tu mensaje dentro de la aplicación: aunque Braze no impone un límite técnico en el tamaño del archivo de video para la reproducción local en el dispositivo, ten en cuenta que los usuarios pueden tener conexiones lentas, planes de datos costosos o almacenamiento limitado. Optimiza los archivos de video para equilibrar calidad y tamaño de archivo.

## Consideraciones de conversión {#conversion-considerations}

- ¿Cuál es tu objetivo con este mensaje? ¿Cómo puedes representarlo en tu mensaje?
- ¿Tus botones ofrecen opciones que tengan sentido para tu usuario? ¿Cuál es tu [llamada a la acción principal]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- ¿Estás usando [vínculos profundos a otro contenido dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? ¿Estás usando este mensaje dentro de la aplicación para enviar y aceptar una [solicitud de permiso o de preparación push]({{site.baseurl}}/user_guide/channels/push/best_practices)?
- ¿Tienes una opción de salida del mensaje? Si no, siempre puedes copiar y pegar este fragmento de código para crear un botón rápido:
    ```html
    <a href="appboy://close">X</a>
    ```

## Consideraciones del editor de arrastrar y soltar {#drag-and-drop-editor-considerations}

### Agregar vínculos profundos para diferentes dispositivos {#adding-deep-links-for-different-devices}

El editor de arrastrar y soltar no permite agregar diferentes vínculos profundos para diferentes dispositivos (a diferencia del editor tradicional).

### Ajustar la opacidad de la imagen de fondo {#adjusting-background-image-opacity}

La configuración de opacidad no permite la transparencia completa de las imágenes de fondo (a diferencia del editor tradicional de IAM). Puedes usar la configuración de opacidad para hacer que el color de fondo del mensaje sea completamente transparente.

### Configurar el ancho máximo {#setting-the-maximum-width}

El ancho máximo en el editor de arrastrar y soltar está limitado a 325 px; esto está pensado principalmente para adaptarse a la vista previa del panel. Los mensajes pueden mostrarse correctamente en dispositivos con pantallas más pequeñas.

### Seleccionar diferentes fondos para diferentes plataformas {#selecting-different-backgrounds-for-different-platforms}

No es posible mostrar dos fondos diferentes para el mismo mensaje en diferentes plataformas (como web y móvil).

### Aplicar estilos de mensaje {#applying-message-styles}

Las imágenes de fondo se aplican al mensaje completo y no se pueden personalizar por página. Los estilos de mensaje se aplican al mensaje completo, no a páginas individuales.

### Medir la altura de los bloques espaciadores {#measuring-spacer-blocks-height}

La unidad de medida para los bloques espaciadores es píxeles (px) y no se puede cambiar.

### Formatos compatibles {#supported-formats}

Actualmente, solo los mensajes dentro de la aplicación modales y de pantalla completa son compatibles con el editor de arrastrar y soltar.

### Ajustar al tamaño y la relación de aspecto {#adjusting-to-size-and-aspect-ratio}

La imagen de fondo estirará el mensaje dentro de la aplicación, ya que el modal se ajusta para adaptarse al tamaño y la relación de aspecto de la imagen de fondo; puedes ajustar la relación según sea necesario.

### Imágenes de fondo y comportamiento de clic {#background-images-and-on-click-behavior}

Estos persisten entre páginas. Para mensajes dentro de la aplicación de varias páginas con diferentes imágenes completas en cada página, agrega un botón para permitir que los usuarios hagan clic para ir a la página siguiente.