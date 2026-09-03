---
nav_title: Guía de preparación
article_title: Guía de preparación de mensajes dentro de la aplicación
page_order: 0.5

page_type: reference
description: "Este artículo cubre preguntas y mejores prácticas a considerar antes de crear mensajes dentro de la aplicación, incluyendo segmentación, planificación, contenido, rendimiento y conversiones."
channel: in-app messages
toc_headers: h2
---

# Guía de preparación de mensajes dentro de la aplicación {#in-app-message-prep-guide}

> Antes de crear tus mensajes dentro de la aplicación, considera los siguientes temas para que el proceso sea más eficiente.

## Consideraciones generales {#general-considerations}

- Si estás creando una Campaign, ¿cuántas variantes de este mensaje te gustaría mostrar? Para ideas sobre pruebas de variantes, consulta [Consejos para diferentes canales]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- Si estás creando un Canvas, ¿se combinará este mensaje con otros canales de mensajería en ese paso?
- ¿Cuándo te gustaría que [tu mensaje expire]({{site.baseurl}}/canvas_in-app_messages)?

## Consideraciones de segmentación {#targeting-considerations}

- Los mensajes dentro de la aplicación funcionan mejor para usuarios que visitan tu aplicación con regularidad. ¿Estás incluyendo a esta audiencia?
- ¿Dónde quieres que tus usuarios vean tu mensaje? ¿En tu aplicación Web? ¿En tu aplicación móvil?
- ¿Qué evento debería desencadenar este mensaje?
- ¿Alguno de tus usuarios utiliza versiones antiguas de tu aplicación? Si es así, es posible que no puedan ver algunos elementos de tu mensaje.
- ¿Para qué tipo de dispositivo o dispositivos estás creando este mensaje? Recuerda que puedes obtener una vista previa de tu mensaje usando el cuadro **Vista previa** o la pestaña **Prueba**. Consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) para más información.

## Programación, retrasos e inicios de sesión {#scheduling-delays-and-session-starts}

Cuando una campaña de mensajes dentro de la aplicación tiene un **Retraso de programación** con un desencadenante de inicio de sesión, un usuario que inicie una sesión y luego cierre la aplicación antes de que se muestre el mensaje dentro de la aplicación puede seguir recibiendo ese mensaje en el siguiente inicio de sesión, después de que expire el retraso.

Las campañas de mensajes dentro de la aplicación pueden retrasar la entrega después del desencadenante hasta dos horas. Para una espera más larga, añade un paso de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de un paso de mensaje dentro de la aplicación en un Canvas. Para la configuración del retraso, consulta [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-2-select-delay-length).

Ese tiempo puede producir un comportamiento de visualización inesperado, especialmente si no se selecciona **Reevaluar la elegibilidad de la campaña antes de mostrar** en la campaña.

Por ejemplo, un usuario podría recibir un mensaje dentro de la aplicación con un retraso de ocho segundos un mes después del lanzamiento de la campaña. Eso puede suceder si inició una sesión, terminó la sesión de inmediato, inició una sesión un mes después y luego, ocho segundos más tarde, recibió el mensaje dentro de la aplicación. Si sale de la aplicación sin cerrarla, el mensaje dentro de la aplicación se muestra cuando regresa a la aplicación.

## Consideraciones de contenido {#content-considerations}

- ¿Qué idiomas utilizarás en este mensaje?
- ¿Cuál es el texto de tu encabezado y cuerpo? ¿Son llamativos y relevantes para tu usuario?
- Los mensajes dentro de la aplicación solo aparecen durante un período determinado. ¿Tu texto es conciso y memorable?
- ¿Utilizarás [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para agregar texto personalizado?
- ¿Los usuarios necesitan copiar el texto del mensaje (como un código de descuento o cupón)? En iOS y Android, los usuarios pueden mantener presionado el texto o los campos de entrada de texto para copiar contenido. Mantener presionado no funciona en imágenes, así que usa texto o campos de entrada de texto en lugar de imágenes que contengan códigos u otro texto que los usuarios puedan necesitar copiar.
- Para mensajes dentro de la aplicación a pantalla completa, ¿tu imagen u otro contenido multimedia está dentro de la [zona segura]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- Para mensajes dentro de la aplicación de cuestionario, ¿deseas registrar atributos o envíos? ¿Has configurado tu página de confirmación?
- Para mensajes dentro de la aplicación HTML personalizados, ¿tu HTML incluye codificación UTF-8 para mostrar correctamente los caracteres especiales? Consulta [Mensajes dentro de la aplicación HTML personalizados]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) para más detalles.
- Si incluyes video en tu mensaje dentro de la aplicación: si bien Braze no impone un límite técnico en el tamaño de archivo de video para la reproducción local en el dispositivo, ten en cuenta que los usuarios pueden tener conexiones lentas, planes de datos costosos o almacenamiento limitado. Optimiza los archivos de video para equilibrar calidad y tamaño de archivo.

## Optimizar el rendimiento de los mensajes dentro de la aplicación {#optimize-in-app-message-performance}

Braze entrega los desencadenadores elegibles de mensajes dentro de la aplicación al usuario al inicio de la sesión. Preparar muchos mensajes con Liquid puede retrasar el inicio de la sesión y afectar el rendimiento de la aplicación.

Si este proceso tarda más de unos pocos segundos, Braze puede diferir el renderizado restante de Liquid. Cada mensaje se renderiza cuando se desencadena y se obtiene bajo demanda. Esta [entrega con plantilla]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages) protege a tus usuarios de un rendimiento deficiente de la aplicación causado por una mayor latencia en la respuesta.

Sigue estas prácticas recomendadas para acelerar la entrega de tus mensajes:

- Dirígete solo a los usuarios que puedan realizar el desencadenador de la Campaign. Una segmentación demasiado amplia puede provocar que los usuarios reciban un desencadenador de mensaje dentro de la aplicación que nunca podrán activar. Por ejemplo, un mensaje dentro de la aplicación desencadenado por una Campaign push específica puede reducirse en alcance para que utilice el mismo público objetivo. Esto se puede aplicar de forma similar a otros tipos de Campaigns, Canvas, eventos personalizados que solo pueden ser desencadenados por ciertos usuarios, y más.
- Establece una fecha de finalización para las Campaigns con límite de tiempo. Detén las Campaigns cuando ya no esperes que reciban impresiones.
- Evita insertar hojas de estilo estáticas grandes, scripts o activos multimedia codificados en base64 directamente en el mensaje o a través de un bloque de contenido. Utiliza la [biblioteca multimedia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) en su lugar para reducir el tiempo de renderizado de tu mensaje.
- Reduce la lógica Liquid compleja con ramificaciones o bucles.
- Solo habilita la reelegibilidad cuando los usuarios deban recibir un mensaje varias veces. Si la reelegibilidad se deja desactivada, Braze deja de entregar el desencadenador del mensaje dentro de la aplicación después de que el usuario lo vea. Para más información, consulta [Reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Asigna una prioridad más alta a las Campaigns importantes. Braze renderiza primero los mensajes elegibles de mayor prioridad, lo que hace menos probable la entrega con plantilla cuando un usuario califica para muchas Campaigns. Para más información, consulta [Elegir una prioridad]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority).

### Separar el código estático y los activos {#separate-static-code-and-assets}

Mantén los valores personalizados y las reglas condicionales en el mensaje. Aloja el CSS, JavaScript y los activos multimedia reutilizables en la [biblioteca multimedia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), y luego enlázalos.

No es necesario hacer esto para todos los scripts y estilos. Esto es principalmente útil para reducir el exceso de activos grandes como estilos de marca compartidos y scripts complejos como widgets interactivos.

Las hojas de estilo y los scripts de la biblioteca multimedia no evalúan Liquid, lo que permite que el dispositivo del usuario los almacene en caché. El siguiente ejemplo mantiene los valores dinámicos en línea y carga el código reutilizable desde archivos estáticos:

{% raw %}

```liquid
<head>
  <style>
    /* Select a hero image URL based on the user's subscription tier. */
    {% capture hero_image_url %}
      {% if custom_attribute.${subscription_tier} == 'premium' %}
        https://braze-images.com/path/to/premium/hero.jpg
      {% else %}
        https://braze-images.com/path/to/standard/hero.jpg
      {% endif %}
    {% endcapture %}
    /* Assigning to a CSS variable so it can be used inside our stylesheet. */
    :root {
      --hero-image: url("{{ hero_image_url | url_escape }}");
    }
  </style>
  <script>
    // Assigning to the global window object so the value can be referenced in our script.
    window.brandConfig = {
      subscriptionTier: "{{custom_attribute.${subscription_tier} | json_escape }}"
    };
  </script>
  <!-- Linking to a stylesheet from the Braze media library. -->
  <link rel="stylesheet" href="https://braze-images.com/path/to/media/library/asset.css">
  <!-- Linking to a script from the Braze media library. -->
  <script src="https://braze-images.com/path/to/other/media/library/asset.js" defer></script>
</head>

<body>
  <div class="hero"></div>
  <div class="user-styles" data-subscription-tier="{{custom_attribute.${subscription_tier} | escape}}">
    ...
  </div>
</body>
```

{% endraw %}

La hoja de estilos de la biblioteca multimedia puede hacer referencia a las variables CSS y definir otros estilos reutilizables:

```css
.hero {
  background-image: var(--hero-image);
}

.user-styles {
  /* styles for all users */
}

.user-styles[data-subscription-tier="premium"] {
  /* premium subscription tier user styles, color scheme, etc */
}

.user-styles[data-subscription-tier="standard"] {
  /* standard subscription tier user styles, color scheme, etc */
}
```

El script de la biblioteca multimedia puede utilizar las variables JavaScript en línea para añadir comportamiento reutilizable:

```javascript
const config = window.brandConfig || {};

if (config.subscriptionTier === "standard") {
  // add some sort of logic to show a "subscribe to premium" button
} else if (config.subscriptionTier === "premium") {
  // thank the user for being a premium user
}
```

## Consideraciones sobre conversión {#conversion-considerations}

- ¿Cuál es tu objetivo con este mensaje? ¿Cómo puedes representarlo en tu mensaje?
- ¿Tus botones ofrecen opciones que tengan sentido para tu usuario? ¿Cuál es tu [llamada a la acción principal]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- ¿Estás usando [vínculos profundos a contenido dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? ¿Estás usando este mensaje dentro de la aplicación para enviar y aceptar una [solicitud de permiso o de preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices)?
- ¿Tienes una opción de salida del mensaje? Si no, siempre puedes copiar y pegar este fragmento de código para crear un botón rápido:
  ```html
  <a href="appboy://close">X</a>
  ```

## Consideraciones del editor de arrastrar y soltar {#drag-and-drop-editor-considerations}

### Agregar vínculos profundos para diferentes dispositivos {#adding-deep-links-for-different-devices}

El editor de arrastrar y soltar no admite agregar diferentes vínculos profundos para diferentes dispositivos (a diferencia del editor tradicional).

### Ajustar la opacidad de la imagen de fondo {#adjusting-background-image-opacity}

La configuración de opacidad no permite la transparencia completa de las imágenes de fondo (a diferencia del editor de IAM tradicional). Puedes usar la configuración de opacidad para que el color de fondo del mensaje sea completamente transparente.

### Establecer el ancho máximo {#setting-the-maximum-width}

El ancho máximo en el editor de arrastrar y soltar está limitado a 325 px; esto está pensado principalmente para adaptarse a la vista previa del panel. Los mensajes pueden mostrarse correctamente en dispositivos con pantallas más pequeñas.

### Seleccionar diferentes fondos para diferentes plataformas {#selecting-different-backgrounds-for-different-platforms}

No es posible mostrar dos fondos diferentes para el mismo mensaje en diferentes plataformas (como web y móvil).

### Aplicar estilos de mensaje {#applying-message-styles}

Las imágenes de fondo se aplican al mensaje completo y no se pueden personalizar por página. Los estilos de mensaje se aplican al mensaje completo, no a páginas individuales.

### Medir la altura de los bloques separadores {#measuring-spacer-blocks-height}

La unidad de medida para los bloques separadores es píxeles (px) y no se puede cambiar.

### Formatos compatibles {#supported-formats}

Actualmente, solo se admiten los mensajes dentro de la aplicación de tipo modal y pantalla completa en el editor de arrastrar y soltar.

### Ajustar al tamaño y la relación de aspecto {#adjusting-to-size-and-aspect-ratio}

La imagen de fondo estirará el mensaje dentro de la aplicación, ya que el modal se ajusta para adaptarse al tamaño y la relación de aspecto de la imagen de fondo; puedes ajustar la relación según sea necesario.

### Imágenes de fondo y comportamiento de clic {#background-images-and-on-click-behavior}

Estos se mantienen entre páginas. Para mensajes dentro de la aplicación de varias páginas con diferentes imágenes completas en cada página, agrega un botón para permitir que los usuarios hagan clic para ir a la página siguiente.