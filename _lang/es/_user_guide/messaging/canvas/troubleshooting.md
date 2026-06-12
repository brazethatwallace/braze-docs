---
nav_title: Solución de problemas
article_title: Solución de problemas de Canvas
page_order: 7
page_type: reference
description: "Esta página proporciona pasos de solución de problemas para Canvas."
tool: Canvas
---

# Solución de problemas de Canvas {#troubleshoot-canvases}

> Esta página te ayuda a solucionar problemas con tus Canvas.

## Error «Demasiadas ramas en Canvas» {#too-many-canvas-branches-error}

Si ves un error «Demasiadas ramas en Canvas» al lanzar un Canvas planificado, la combinación de ramificación de pasos y el tamaño de la audiencia de entrada puede crear problemas de rendimiento en el clúster de Braze que impidan el envío de mensajes.

Braze muestra este mensaje cuando lanzas un Canvas con una entrada planificada, no cuando guardas un borrador. Para resolverlo, intenta lo siguiente:

- Reduce la ramificación de pasos en el Canvas.
- Reduce el tamaño de la audiencia de entrada.
- Usa [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) para consolidar la ramificación en lugar de muchas rutas paralelas.
- Si tu Canvas usa el editor original, [clónalo a Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/) y reconstrúyelo con componentes de Canvas.

Si aún necesitas lanzar el Canvas sin cambios y no puedes migrar a Canvas Flow, ponte en contacto con [Soporte]({{site.baseurl}}/support_contact/).

## ¿Por qué un usuario no recibió un paso en Canvas desencadenado? {#why-did-a-user-not-receive-a-triggered-canvas-step}

Primero, confirma que el evento personalizado se está enviando a Braze. Ve a **Analytics** > **Informe de eventos personalizados** y selecciona el evento personalizado y el rango de fechas correspondientes. Si el evento no aparece, confirma que está configurado correctamente y que el usuario realizó la acción correcta.

Si el evento personalizado aparece, continúa con la solución de problemas haciendo lo siguiente:

- Revisa la descarga del perfil del usuario para confirmar que desencadenó el evento y cuándo lo hizo. Si el evento fue desencadenado, compara la marca de tiempo de cuándo se desencadenó el evento con el momento en que el Canvas se activó. Es posible que el evento se haya desencadenado antes de que el Canvas estuviera en vivo.
- Revisa los registros de cambios del Canvas y de cualquier Segment utilizado en la segmentación para determinar si el usuario estaba en el Segment cuando se desencadenó su evento personalizado. Si no estaba en el Segment, no habría recibido el paso en Canvas.
- Verifica si el usuario fue incluido en un grupo de control a través de la segmentación y, en consecuencia, se le impidió recibir el paso en Canvas.
- Si hay un retraso planificado, comprueba si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se desencadenó antes del retraso, no habría recibido el paso en Canvas.

{% alert note %}
Los mensajes dentro de la aplicación solo pueden desencadenarse con eventos enviados a través del SDK, no de la REST API.
{% endalert %}

## ¿Por qué mi Canvas no se envía como se esperaba? {#why-isnt-my-canvas-sending-as-expected}

Los Canvas son robustos y complejos, y sabemos que dedicas tiempo y cuidado al crearlos. Así que, si descubres que tu Canvas no se envía como deseas, te recomendamos revisar la planificación de tu Canvas, la audiencia de entrada y la configuración de entrada, y repasar los pasos para [crear un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

### Planificación {#schedule}

- ¿Está el Canvas [planificado correctamente]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types)?
- ¿Has seleccionado la fecha y hora correctas?
- Para la [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types), ¿los usuarios han realizado las acciones especificadas desde que lanzaste el Canvas?

### Configuración de entrada {#entry-settings}

La [configuración de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=basics#selecting-entry-controls) es importante para entender cómo se envían tus Canvas. Comprueba si has limitado el número de personas que potencialmente entrarán en el Canvas.

Los usuarios también pueden salir de un Canvas si ya no son elegibles para recibir mensajes. Por ejemplo, si el Canvas solo contiene notificaciones push y un usuario cancela la suscripción a push después de recibir el primer paso, ese usuario abandonaría el Canvas. Considera usar [diferentes pasos en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/) para añadir recorridos de usuario alternativos.

### Segmentar tu audiencia {#segmenting-your-audience}

Considera las siguientes preguntas para tu audiencia objetivo:

- ¿Has seleccionado el Segment correcto?
- ¿Cómo está configurado el Segment?
- ¿Has confirmado que el Segment contiene usuarios?
- ¿Has añadido filtros adicionales que limiten el número de usuarios que entran en el Canvas?
- ¿Los usuarios califican para recibir el primer paso de tus variantes? Por ejemplo, si el primer paso de tu Canvas es una notificación push, pero la audiencia de entrada tiene push deshabilitado, entonces ningún usuario recibirá mensajes.

## ¿Por qué los envíos o entregas son menores que el tamaño de mi audiencia objetivo? {#why-are-sends-or-deliveries-lower-than-my-target-audience-size}

El número de mensajes enviados o entregados a menudo difiere de la audiencia estimada o del recuento de destinatarios. Las razones comunes incluyen:

- **Reevaluación de la audiencia:** Los usuarios pueden salir del Segment entre el momento en que entran a un paso y el momento en que se envía el mensaje.
- **Elegibilidad del canal:** Es posible que a los usuarios les falten direcciones de correo electrónico, tokens de notificaciones push o el estado de suscripción requerido para ese canal en ese paso.
- **Grupos de control:** Un grupo de control global o de Canvas puede excluir a usuarios de la mensajería.
- **Horas tranquilas, Intelligent Timing y límites de velocidad:** Estas configuraciones pueden diferir o suprimir envíos.
- **Pasos de mensajes dentro de la aplicación:** Los mensajes dentro de la aplicación pueden mostrar cero _Envíos_ mientras existen impresiones. Esto es esperado porque la entrega de mensajes dentro de la aplicación funciona de manera diferente a las notificaciones push o el correo electrónico. Consulta [¿Por qué un Canvas puede mostrar cero envíos aunque se registren impresiones?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged) en las preguntas frecuentes de Canvas.

Para correo electrónico y otros canales, aplican muchos de los mismos factores que para las Campaigns. Para una lista detallada, consulta [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size).

## ¿Por qué ningún usuario entró en mi Canvas planificado diariamente el día del cambio de horario? {#why-did-no-users-enter-my-daily-scheduled-canvas-on-daylight-saving-time-day}

En los días de transición del horario de verano (DST), los Canvas planificados diariamente pueden ejecutarse hasta una hora antes o después de lo habitual. Si tus criterios de entrada dependen de atributos personalizados o eventos con marcas de tiempo que caen dentro de una hora del horario de entrada planificado, es posible que los usuarios aún no califiquen en el día del DST porque el atributo o evento no se ha registrado.

Por ejemplo, supongamos que los usuarios normalmente reciben una actualización de atributo personalizado a las 3:00 p.m. en la zona horaria de tu Canvas y tu Canvas se ejecuta diariamente a las 3:30 p.m. en esa misma zona horaria. En un día de adelanto de reloj por DST, el Canvas puede evaluar a los usuarios hasta una hora antes de lo habitual en relación con esa actualización de atributo, antes de que el atributo se haya registrado. Si la reelegibilidad está desactivada, los usuarios que entraron en días anteriores no pueden volver a entrar, lo que resulta en cero entradas para ese día.

Para evitar esto, asegúrate de que las actualizaciones de tus atributos personalizados o eventos ocurran más de una hora antes del horario de entrada planificado del Canvas.

## ¿Por qué mi audiencia no se dividió equitativamente entre el grupo de control y el grupo de variante? {#why-didnt-my-audience-split-evenly-between-the-control-group-and-variant-group}

Al crear tu Canvas, es posible que hayas esperado que tu audiencia se dividiera equitativamente entre tu grupo de control y tu grupo de variante, como en el siguiente [caso de uso](#use-case). Analicemos por qué sucede esto y cómo solucionarlo.

El grupo al que se une un usuario depende de su configuración. Puede ser el grupo de control o el grupo de variante. Un usuario entrará en un Canvas cuando cumpla con todos los criterios definidos en el [paso de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule). Al configurar tu Canvas, defines qué porcentaje de usuarios entrará en cada variante y en el grupo de control.

Si tu grupo de control es grande en comparación con tu grupo de variante (y esta no es tu intención), te recomendamos lo siguiente:
1. Configura tu filtro de audiencia de entrada como **is Foreground Push Enabled**.
2. Configura tu filtro de audiencia de entrada para **Push Subscription Status**, **Email Subscription Status**, o ambos como **Opted In** o **Subscribed**.

Al crear un Canvas con un grupo de control, confirma que todos los usuarios en la audiencia de entrada puedan recibir mensajes dentro del Canvas (por ejemplo, si el Canvas contiene mensajes push y de correo electrónico).

### Caso de uso {#use-case}

Imaginemos el siguiente escenario:
- Un Canvas tiene una sola variante y un grupo de control.
- El primer paso de la variante es una notificación push.
- El 90 % de los usuarios fueron seleccionados para entrar en la variante y el 10 % para entrar en el grupo de control.

![Ejemplo de Canvas con 90 % de variante y 10 % de grupo de control.]({% image_buster /assets/img_archive/trouble15.png %})

En este escenario, el 90 % de los usuarios que entran en el Canvas entrarán en la variante.

Si revisamos los usuarios activos, podemos ver que aunque contiene 29,8k usuarios, solo el 64 % de ellos tienen push habilitado:

![Segment con el filtro «Push Enabled» configurado como «true» y usuarios estimados de 29,8k.]({% image_buster /assets/img_archive/trouble16.png %})

Esto significa que, aunque especificamos que el 90 % de los usuarios entraran en la variante, no todos esos usuarios pueden realmente recibir una notificación push. Estos usuarios que no pueden recibir una notificación push seguirán entrando en la variante de todos modos.

## ¿Por qué el editor de Canvas se congela o no carga? {#why-is-the-canvas-editor-freezing-or-not-loading}

Si estás haciendo ediciones en Canvas grandes o complejos con muchas ramas o variantes, muchos pasos o flujos muy amplios, el editor puede no cargar o congelarse. En este caso, te recomendamos lo siguiente:

- Limpia la caché y las cookies del navegador, y luego recarga la página. Si usas algún bloqueador de anuncios de empresa o extensiones del navegador, esto puede interferir con la plataforma Braze.
- Usa los controles de zoom del Canvas para reducir la vista al 25 % o al 10 %. Esto reduce la cantidad de interfaz que el navegador debe renderizar a la vez.
- Prueba con un navegador web diferente.