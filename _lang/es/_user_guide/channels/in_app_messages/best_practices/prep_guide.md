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
- Si estás creando un Canvas, ¿este mensaje se combinará con otros canales de mensajería en ese paso?
- ¿Cuándo te gustaría que [tu mensaje expire]({{site.baseurl}}/canvas_in-app_messages)?

## Consideraciones de segmentación {#targeting-considerations}

- Los mensajes dentro de la aplicación son ideales para usuarios que visitan tu aplicación con regularidad. ¿Estás incluyendo a esta audiencia?
- ¿Dónde quieres que tus usuarios vean tu mensaje? ¿En tu aplicación Web? ¿En tu aplicación móvil?
- ¿Qué evento debería desencadenar este mensaje?
- ¿Alguno de tus usuarios está usando versiones anteriores de tu aplicación? Si es así, es posible que no puedan ver algunos elementos de tu mensaje.
- ¿Para qué tipo de dispositivo o dispositivos estás creando este mensaje? Recuerda que puedes previsualizar tu mensaje usando el cuadro **Preview** o la pestaña **Test**. Consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) para más información.

## Planificación, demoras e inicios de sesión {#scheduling-delays-and-session-starts}

Cuando una Campaign de mensaje dentro de la aplicación tiene **Schedule Delay** con un desencadenante en el inicio de sesión, un usuario que inicia una sesión y luego cierra la aplicación antes de que se muestre el mensaje dentro de la aplicación aún puede recibir ese mensaje en el siguiente inicio de sesión, después de que expire la demora.

Ese comportamiento puede producir una visualización inesperada, especialmente si **Re-evaluate campaign eligibility before displaying** no está seleccionado en la Campaign.

Por ejemplo, un usuario podría recibir un mensaje dentro de la aplicación con una demora de ocho segundos un mes después del lanzamiento de la Campaign. Esto puede ocurrir si inició una sesión, terminó la sesión inmediatamente, inició una sesión un mes después y luego, ocho segundos más tarde, recibió el mensaje dentro de la aplicación. Si navega fuera de la aplicación sin cerrarla, el mensaje dentro de la aplicación se muestra cuando regresa a la aplicación.

## Consideraciones de contenido {#content-considerations}

- ¿Qué idiomas usarás en este mensaje?
- ¿Cuál es el texto de tu encabezado y cuerpo? ¿Son llamativos y relevantes para tu usuario?
- Los mensajes dentro de la aplicación solo aparecen durante un período de tiempo determinado. ¿Tu texto es conciso y memorable?
- ¿Usarás [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para agregar texto personalizado?
- ¿Los usuarios necesitan copiar el texto del mensaje (como un código de descuento o cupón)? En iOS y Android, los usuarios pueden mantener presionado el texto o los campos de entrada de texto para copiar contenido. Mantener presionado no funciona en imágenes, así que usa texto o campos de entrada de texto en lugar de imágenes que contengan códigos u otro texto que los usuarios puedan necesitar copiar.
- Para mensajes dentro de la aplicación de pantalla completa, ¿tu imagen u otro contenido multimedia está dentro de la [zona segura]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- Para mensajes dentro de la aplicación tipo cuestionario, ¿quieres registrar atributos o envíos? ¿Has configurado tu página de confirmación?

## Consideraciones de conversión {#conversion-considerations}

- ¿Cuál es tu objetivo para este mensaje? ¿Cómo puedes representarlo en tu mensaje?
- ¿Tus botones ofrecen opciones que tienen sentido para tu usuario? ¿Cuál es tu [llamada a la acción principal]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- ¿Estás usando [vínculos profundos a contenido dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? ¿Estás usando este mensaje dentro de la aplicación para enviar y aceptar una [solicitud de permiso o preparación push]({{site.baseurl}}/user_guide/channels/push/best_practices)?
- ¿Tienes una opción de salida del mensaje? Si no, siempre puedes copiar y pegar este fragmento de código para crear un botón rápido:
    ```html
    <a href="appboy://close">X</a>
    ```

## Consideraciones del editor de arrastrar y soltar {#drag-and-drop-editor-considerations}

### Agregar vínculos profundos para diferentes dispositivos {#adding-deep-links-for-different-devices}

El editor de arrastrar y soltar no admite agregar diferentes vínculos profundos para diferentes dispositivos (a diferencia del editor tradicional).

### Ajustar la opacidad de la imagen de fondo {#adjusting-background-image-opacity}

La configuración de opacidad no permite la transparencia completa de las imágenes de fondo (a diferencia del editor de IAM tradicional). Puedes usar la configuración de opacidad para hacer que el color de fondo del mensaje sea completamente transparente.

### Configurar el ancho máximo {#setting-the-maximum-width}

El ancho máximo en el editor de arrastrar y soltar está limitado a 325 px; esto está pensado principalmente para acomodar la vista previa del panel. Los mensajes pueden mostrarse correctamente en dispositivos con pantallas más pequeñas.

### Seleccionar diferentes fondos para diferentes plataformas {#selecting-different-backgrounds-for-different-platforms}

No es posible mostrar dos fondos diferentes para el mismo mensaje en diferentes plataformas (como Web y móvil).

### Aplicar estilos de mensaje {#applying-message-styles}

Las imágenes de fondo se aplican al mensaje completo y no se pueden personalizar por página. Los estilos de mensaje se aplican al mensaje completo, no a páginas individuales.

### Medir la altura de los bloques espaciadores {#measuring-spacer-blocks-height}

La unidad de medida para los bloques espaciadores es píxeles (px) y no se puede cambiar.

### Formatos compatibles {#supported-formats}

Actualmente, solo los mensajes dentro de la aplicación modales y de pantalla completa son compatibles con el editor de arrastrar y soltar.

### Ajustar al tamaño y la relación de aspecto {#adjusting-to-size-and-aspect-ratio}

La imagen de fondo estirará el mensaje dentro de la aplicación, ya que el modal se ajusta para adaptarse al tamaño y la relación de aspecto de la imagen de fondo; puedes ajustar la relación según sea necesario.

### Imágenes de fondo y comportamiento al hacer clic {#background-images-and-on-click-behavior}

Estos persisten entre páginas. Para mensajes dentro de la aplicación de varias páginas con diferentes imágenes completas en cada página, agrega un botón para permitir que los usuarios hagan clic para ir a la siguiente página.