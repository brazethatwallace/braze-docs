---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Este artículo ofrece respuestas a preguntas frecuentes sobre Canvas."
tool: Canvas
toc_headers: h2
---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre Canvas.

## Creación y edición de Canvas {#building-and-editing-canvas}

### ¿Cuántos pasos puedo incluir en un Canvas? {#how-many-steps-i-can-include-in-a-canvas}

Puedes añadir hasta 200 pasos en un Canvas.

### ¿Hay límites de tamaño para las propiedades de entrada de Canvas? {#are-there-size-limits-for-canvas-entry-properties}

Sí. El [objeto de contexto de Canvas]({{site.baseurl}}/api/objects_filters/context_object) (propiedades de entrada de Canvas) tiene un tamaño máximo de 50&nbsp;KB. Mantén las cargas útiles lo más pequeñas posible dentro de ese límite. Para saber cómo funcionan las propiedades de entrada y de evento en Canvas, consulta [Propiedades de contexto y de evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).

### ¿Por qué veo un error "Too many Canvas branches"? {#why-do-i-see-a-too-many-canvas-branches-error}

Este error aparece cuando la combinación de la ramificación de pasos y el tamaño de la audiencia de entrada puede provocar problemas de rendimiento del clúster que impidan el envío de mensajes. Para conocer los pasos de resolución, que incluyen el uso de [Rutas de Audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), la reducción de ramas o del tamaño de la audiencia y la reconstrucción en Canvas Flow, consulta [Error "Too many Canvas branches"]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error).

### ¿Puedo usar Optimize with BrazeAI<sup>TM</sup> con la reelegibilidad en un Canvas? {#can-i-use-optimize-with-brazeai-with-re-eligibility-in-a-canvas}

Sí. Los Canvas pueden usar [Optimize with BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai) cuando la reelegibilidad está habilitada. Braze no puede garantizar la misma variante en el reingreso porque la asignación cambia con el tiempo. Campaigns requieren una ventana de reelegibilidad de 24 horas o más cuando **Optimize with BrazeAI<sup>TM</sup>** está activado.

### ¿Cuál es la diferencia entre un componente y un paso? {#whats-the-difference-between-a-component-and-a-step}

Un [componente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about) es una parte individual de tu Canvas que puedes usar para determinar la efectividad de tu Canvas. Los componentes pueden incluir acciones como dividir el recorrido del usuario, añadir un retraso e incluso probar múltiples rutas de Canvas. Un paso en Canvas se refiere al recorrido personalizado del usuario en las ramas de tu Canvas. Esencialmente, tu Canvas está formado por componentes individuales que crean pasos para el recorrido del usuario.

### ¿Puedo lanzar un Canvas con pasos desconectados? {#can-i-launch-a-canvas-with-disconnected-steps}

Sí. También puedes guardar Canvas después del lanzamiento con pasos desconectados.

### ¿Adónde van los usuarios cuando han llegado a un paso desconectado? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Si un usuario se encuentra en un paso desconectado del flujo de trabajo de tu Canvas, avanzará al paso siguiente si existe uno, y la configuración del paso determinará cómo debe avanzar el usuario. El objetivo es permitir que los usuarios realicen cambios en los pasos sin tener que conectarlos directamente al resto del Canvas. Esto también te da margen para hacer pruebas antes de ponerlo en producción de inmediato, lo que efectivamente permite guardar un borrador.

Te recomendamos comprobar la vista de análisis de los usuarios pendientes en un paso de Canvas antes de desconectar un paso.

### ¿Qué ocurre si la audiencia y el tiempo de envío son idénticos para un Canvas que tiene una variante, pero múltiples ramas? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Se pone en cola un trabajo para cada paso: se ejecutan aproximadamente al mismo tiempo, y uno de ellos "gana". En la práctica, esto puede distribuirse de manera relativamente uniforme, pero es probable que haya al menos un ligero sesgo hacia el paso que se creó primero.

Además, no podemos garantizar exactamente cómo será esa distribución. Si quieres una división uniforme, añade un filtro de [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers).

### ¿Cómo se evalúan las audiencias de Canvas? {#how-are-canvas-audiences-evaluated}

De forma predeterminada, los filtros y Segments de los pasos completos en Canvas se comprueban en el momento del envío. El paso de división de decisiones realiza una evaluación justo después de recibir un paso anterior (o antes de un retraso).

### ¿Cuándo se activa un evento de excepción? {#when-does-an-exception-event-trigger}

Los eventos de excepción solo se activan mientras el usuario está esperando recibir el componente de Canvas con el que está asociado. Si un usuario realiza una acción con antelación, el evento de excepción no se activará. Si quieres excluir a los usuarios que hayan realizado un determinado evento con antelación, usa [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) en su lugar.

### ¿Cómo afecta la edición de un Canvas a los usuarios que ya están en el Canvas? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Si editas algunos de los pasos de un Canvas de varios pasos, los usuarios que ya estaban en la audiencia pero que aún no han recibido los pasos recibirán la versión actualizada del mensaje. Ten en cuenta que esto solo ocurrirá si aún no han sido evaluados para el paso.

Para más información sobre lo que puedes editar después del lanzamiento, consulta [Cambiar tu Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits).

### ¿Qué ocurre cuando detienes un Canvas? {#what-happens-when-you-stop-a-canvas}

Cuando detienes un Canvas, se aplica lo siguiente:

- Se impedirá que los usuarios entren en el Canvas.
- No se enviarán más mensajes, independientemente de en qué punto del flujo se encuentre un usuario.
- **Excepción:** los Canvas con correos electrónicos no se detendrán inmediatamente. Una vez que las solicitudes de envío llegan a SendGrid, no hay nada que podamos hacer para evitar que se entreguen al usuario.

### ¿Debo crear un solo Canvas o Canvas separados por ciclo de vida del usuario? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Dependiendo de lo que quieras lograr con tu Canvas, es posible que necesites diferentes enfoques para crear el recorrido del usuario. La flexibilidad de Canvas te permite trazar recorridos de usuario para cualquier etapa del ciclo de vida del usuario. Consulta nuestras [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para ver varios ejemplos de enfoques optimizados para crear recorridos de usuario efectivos.

## Mensajes y entrega {#messages-and-delivery}

### ¿Cuándo se envían los mensajes dentro de la aplicación en Canvas? {#when-are-in-app-messages-in-canvas-sent}

Los mensajes dentro de la aplicación se envían al inicio de la siguiente sesión. Esto significa que si el usuario entra en el paso de Canvas antes de que se detenga el Canvas, seguirá recibiendo el mensaje dentro de la aplicación en su siguiente inicio de sesión, siempre y cuando el mensaje no haya expirado aún.

Es posible que un usuario inicie una sesión antes de que se detenga el Canvas, pero no se le muestre el mensaje dentro de la aplicación de inmediato. Esto puede ocurrir si el mensaje dentro de la aplicación se desencadena por un evento personalizado o tiene un retraso. Esto significa que es posible que un usuario registre una impresión de mensaje dentro de la aplicación y "reciba" el mensaje después de que se detenga el Canvas. Sin embargo, el usuario habría tenido que iniciar la sesión antes de que se detuviera el Canvas, pero **después** de haber recibido el paso de Canvas.

{% alert note %}
Detener un Canvas no hará que los usuarios que están esperando recibir mensajes salgan del recorrido del usuario. Si reactivas el Canvas y los usuarios aún están esperando el mensaje, lo recibirán (a menos que el momento en que debían haber recibido el mensaje haya pasado, en cuyo caso no lo recibirán).
{% endalert %}

### ¿Por qué un Canvas puede mostrar cero envíos aunque se registren impresiones? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Si los _Mensajes enviados_ siempre son cero para un Canvas que contiene un paso de mensaje dentro de la aplicación, es porque la entrega de mensajes dentro de la aplicación funciona de manera diferente a otros canales de mensajería.

Los mensajes dentro de la aplicación son "solicitados" por el SDK, en lugar de ser "enviados" desde Braze. Los mensajes dentro de la aplicación para usuarios elegibles se entregan automáticamente al inicio de la sesión y "esperan" el evento desencadenante antes de mostrarse. Dado que los usuarios elegibles reciben el mensaje cuando inician una sesión, Braze no reporta esto como un evento de envío. Cuando los usuarios realizan el evento desencadenante, el mensaje se muestra y Braze registra una impresión y marca el paso de Canvas (o Campaign) como recibido en el perfil de usuario. En consecuencia, el total de _Envíos_ es cero para los mensajes dentro de la aplicación.

### ¿Por qué los usuarios no recibieron mi mensaje dentro de la aplicación después de un retraso largo o una rama? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

Después de que se completen los pasos de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) anteriores y las verificaciones de audiencia, los usuarios se vuelven elegibles para un mensaje dentro de la aplicación solo cuando llegan al paso de Mensaje. Si el mensaje expira en una fecha del calendario o en una ventana corta de **duración después de que el paso esté disponible**, los usuarios en ramas más lentas pueden llegar después de la expiración y nunca ver el mensaje. Alinea la expiración con los retrasos de ruta más largos que sean realistas. Para más información y ejemplos, consulta [Expiración de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration).

### ¿Por qué veo "Canvas Entry Properties may not be used in In-App Messages."? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

Este mensaje aparece cuando la personalización hace referencia a campos que los mensajes dentro de la aplicación no pueden resolver en Canvas. Usa el objeto `context` como se describe en [Propiedades de contexto y eventos]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) y [Paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). El espacio de nombres heredado de Liquid `canvas_entry_properties` tiene restricciones diferentes a `context`. Si necesitas que los valores persistan a lo largo de múltiples pasos, revisa [propiedades persistentes en el editor original de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) con tu equipo de Braze. Los valores almacenados se borran cuando un usuario sale del Canvas antes de que el dispositivo descargue la carga útil del mensaje dentro de la aplicación.

### ¿Dónde puedo encontrar los clics de botones para mensajes dentro de la aplicación de arrastrar y soltar en Canvas? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

Las métricas a nivel de botón para mensajes dentro de la aplicación de arrastrar y soltar aparecen en la tarjeta de análisis del paso de **Mensaje** en **Detalles de Canvas**, no solo en el resumen de alto nivel de Canvas. Abre el Canvas, selecciona el paso de Mensaje y revisa la participación del mensaje dentro de la aplicación allí. Para conceptos de informes, consulta [Medir y probar con análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### ¿Puedo programar diferentes horarios de envío para cada variante en el mismo paso de Mensaje de Canvas o envío multivariante? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

No. Las variantes en la misma configuración multivariante o paso de Mensaje comparten un mismo programa de entrega. No puedes asignar a una variante el envío a las 6 pm y a otra a las 7 pm para el mismo envío programado.

Para escalonar envíos o usar diferentes horarios por ruta, prueba los siguientes métodos:

- Pasos de Mensaje separados con pasos de Retraso entre ellos para que cada mensaje tenga su propio programa.
- Usa ramas o un paso de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que los usuarios sigan rutas con diferente sincronización.
- Campaigns separadas si el caso de uso no necesita permanecer dentro de un mismo Canvas.

Para conceptos multivariantes y de pruebas A/B en Campaigns, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

### ¿Qué sucede si un usuario tiene limitación de frecuencia global en un paso de Mensaje de Canvas? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

No recibe ese envío para el canal limitado, pero los pasos de Mensaje siguen avanzando a los usuarios cuando un mensaje no se envía debido a la limitación de frecuencia global. Para los casos de avance paso a paso, consulta [Cómo avanzan los usuarios]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). La limitación de frecuencia global por sí sola no saca a los usuarios de un Canvas; ese comportamiento es independiente de las **Validaciones de entrega** en un paso de Mensaje. Para más detalles, consulta [Límite de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### ¿Por qué los envíos son menores que el tamaño estimado de la audiencia? {#why-are-sends-lower-than-the-estimated-audience-size}

Los envíos pueden ser menores que la **Audiencia estimada** por muchas de las mismas razones que en las [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size), incluyendo límites de frecuencia, filtros estrictos de dispositivo o navegador, ventanas de reelegibilidad, límites de velocidad y exclusiones a nivel de canal (por ejemplo, alcanzabilidad push o verificaciones de suscripción y capacidad de entrega de correo electrónico).

También aplican factores específicos de Canvas:

- **Entrada basada en acciones o desencadenada por API:** Los usuarios solo entran (y reciben pasos) después de realizar el comportamiento de entrada, por lo que los envíos realizados van por detrás de la estimación inicial hasta que esas acciones ocurran.
- **Rutas de audiencia:** Los usuarios se dirigen a la rama de mayor prioridad para la que califican, por lo que las ramas posteriores pueden recibir menos usuarios de lo que sugiere un conteo plano de Segment.
- **Verificaciones de audiencia y hora de envío:** Los pasos completos reevalúan los filtros en el momento del envío a menos que lo configures de otra manera. Los usuarios que calificaban cuando se creó el Canvas pueden salir antes de que se envíe un mensaje.
- **Grupos de control:** Los grupos de control globales o de Canvas retienen una parte de los participantes de la mensajería.
- **Horas tranquilas y retrasos:** Los mensajes pueden retenerse o reprogramarse, desplazando los envíos fuera de la ventana de informes que estás viendo.
- **Límites máximos de entrada o audiencia:** Los límites de entrada o envío detienen a usuarios adicionales incluso cuando el Segment subyacente es más grande.
- **Ventana de informes:** El rango de análisis puede no incluir todos los envíos que estás comparando con la estimación.

### ¿Por qué la audiencia estimada y los conteos de usuarios de Canvas no coinciden? {#why-dont-estimated-audience-and-canvas-user-counts-match}

La **Audiencia estimada** refleja quién coincide con tu Segment y filtros de entrada en el momento en que se ejecuta la estimación. Después de ese momento, las entradas retrasadas o basadas en acciones, la reelegibilidad, los desencadenadores de API o el enrutamiento por ramas pueden aumentar la cantidad de perfiles que tocan el recorrido en comparación con la instantánea. Los usuarios también pueden salir cuando los filtros en el momento del envío fallan, lo que reduce las entradas o envíos realizados. Compara la sincronización, los límites y la configuración de evaluación junto con [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?](#why-are-sends-lower-than-the-estimated-audience-size).

### ¿Por qué _Destinatarios únicos_ es mayor que el número de usuarios que segmenté? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_Destinatarios únicos_ puede ser mayor que la audiencia esperada porque Braze rastrea **destinatarios únicos diarios** para los informes de Canvas y Campaign. Esto apoya la atribución precisa de conversiones cada vez que un usuario recibe un mensaje en el recorrido.

Por ejemplo, si un usuario recibe un paso de Canvas el lunes y nuevamente el viernes y convierte después de cada envío, Braze puede contar dos filas de destinatarios y dos conversiones dentro del alcance. Con entradas recurrentes o reelegibilidad, el mismo conjunto pequeño de perfiles puede producir múltiples _Destinatarios únicos_ a lo largo de varios días.

### ¿Por qué mi Canvas experimenta tasas de envío más bajas? {#why-is-my-canvas-experiencing-lower-send-rates}

Si descubres que tu Canvas programado diario envía a menos usuarios con el tiempo, verifica lo siguiente:

- **Verifica si la reelegibilidad está activada:** Sin reelegibilidad, Braze ingresa a cada usuario en el Canvas solo una vez. En Canvas con programación diaria, solo los usuarios que coinciden con la audiencia y que aún no han entrado al Canvas son elegibles para cada entrada. A medida que más usuarios entran, cada entrada posterior tiene menos usuarios elegibles, por lo que el volumen de entradas disminuye.
- **Verifica si la audiencia tiene membresía fija:** Las audiencias construidas a partir de una lista fija de usuarios (como una [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) usada como filtro de Segment) no ganan nuevos miembros automáticamente. Sin nuevos participantes, el volumen de entradas no puede recuperarse a medida que los usuarios entran al Canvas.

Para [límites de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) y otros factores que reducen los envíos para una ocurrencia única, consulta [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?](#why-are-sends-lower-than-the-estimated-audience-size).

### ¿Por qué un Segment de grupo de control pequeño muestra cambios en la membresía histórica? {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

Los gráficos de membresía histórica usan muestras estimadas, por lo que Segments pequeños —incluyendo los Segments del [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group)— pueden mostrar movimientos día a día incluso cuando la audiencia subyacente es estable. Para saber cómo funcionan las estimaciones y por qué los gráficos pueden fluctuar, consulta [Ver el tamaño histórico de la membresía de Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size).

## Análisis y conversiones {#analytics-and-conversions}

### ¿Cómo atribuye el panel de conversiones las conversiones de Canvas? {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

El [panel de conversiones]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) atribuye las conversiones de Canvas según el [método de atribución]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods) que selecciones (por ejemplo, **Upon Receipt**, **Upon Send**, **Upon Open** o **Upon Click**). Para que un usuario aparezca en el informe, debe entrar en el Canvas o Campaign, registrar el método de atribución seleccionado y realizar el evento de conversión dentro de la configuración de tu informe.

Para las reglas de conversión a nivel de paso y a nivel de variante en los análisis de Canvas, consulta [¿Cómo se hace seguimiento de las conversiones de usuarios en un Canvas?](#how-are-user-conversions-tracked-in-a-canvas).

### ¿Cómo se hace seguimiento de las conversiones de usuarios en un Canvas? {#how-are-user-conversions-tracked-in-a-canvas}

Un usuario solo puede convertir una vez por entrada en un Canvas. Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El bloque de resumen al inicio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de ese recorrido, independientemente de si recibieron un mensaje. Cada paso posterior solo mostrará las conversiones que ocurrieron mientras ese fue el paso más reciente que el usuario recibió.

{% alert note %}
Cuando un usuario vuelve a entrar en un Canvas, los eventos de conversión solo se rastrean para la entrada más reciente. Los eventos de conversión no se registran para entradas anteriores, incluso si el evento de conversión se rellena retroactivamente.
{% endalert %}

{% details Ampliar para ver ejemplos %}

**Ejemplo 1**

Hay un recorrido en Canvas con 10 notificaciones push y el evento de conversión es "inicio de sesión" ("Abre la aplicación"):

- El usuario A abre la aplicación después de entrar pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

**Resultado:** El resumen mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión de uno en el primer paso y cero en todos los pasos posteriores.

{% alert note %}
Si las horas tranquilas están activas cuando ocurre el evento de conversión, se aplican las mismas reglas.
{% endalert %}

**Ejemplo 2**

Hay un Canvas de un solo paso con horas tranquilas habilitadas:

1. El usuario entra en el Canvas.
2. El primer paso no tiene retraso, pero está dentro de las horas tranquilas configuradas, por lo que el mensaje se suprime.
3. El usuario realiza el evento de conversión.

**Resultado:** El usuario contará como convertido en la variante general del Canvas, pero no en el paso, ya que no recibió el paso.

{% enddetails %}

### ¿Cuál es la diferencia entre los distintos tipos de tasa de conversión? {#whats-the-difference-between-the-different-conversion-rate-types}

- El total de conversiones de Canvas refleja cuántos usuarios únicos completaron un evento de conversión, no cuántas conversiones completó cada uno.
- La tasa de conversión de variante o el bloque de resumen al inicio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de ese recorrido, independientemente de si recibieron un mensaje, como un total agregado.
- La tasa de conversión de paso refleja cuántas personas recibieron ese paso de mensaje y completaron cualquiera de los eventos de conversión descritos.

### ¿Por qué la tasa de conversión de mi paso en Canvas no es igual a la tasa de conversión total de mi variante en Canvas? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Es común que el total de conversiones de una variante en Canvas sea mayor que la suma del total de sus pasos. Esto ocurre porque un usuario puede realizar un evento de conversión para una variante tan pronto como entra en ella. Sin embargo, ese mismo evento de conversión no cuenta para un paso en Canvas. Por lo tanto, cualquier usuario que entre en el Canvas y realice el evento de conversión antes de recibir el primer paso en Canvas se cuenta en el total de conversión de la variante, pero no en el total del paso. Lo mismo aplica para un usuario que entra en el Canvas pero sale antes de recibir algún paso.

Ten en cuenta que también es posible que un usuario entre en una variante, no reciba ningún mensaje de un paso y luego convierta. En este caso, no se registra una conversión a nivel de paso. Sin embargo, dado que el usuario técnicamente sí convirtió, se registra una conversión a nivel de Canvas.

### ¿Cómo puedo confirmar si mis usuarios recibieron un Canvas activado por API? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Puedes [crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) usando un filtro de Canvas para confirmar si los usuarios entraron en el Canvas o recibieron un paso específico en Canvas. Por ejemplo, usa un filtro de entrada de Canvas si quieres confirmar que los usuarios entraron en el Canvas activado por API, o un filtro de paso recibido si quieres confirmar que recibieron un mensaje del Canvas. Luego, usa el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para exportar los usuarios de ese segmento.

### ¿Puedo eliminar un Canvas? {#can-i-delete-a-canvas}

No, pero puedes [archivar un Canvas]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### ¿Cómo retomo un Canvas o Campaign archivados? {#how-do-i-resume-an-archived-canvas-or-campaign}

Los mensajes archivados no se envían hasta que los devuelvas a un estado editable. [Desarchiva]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving) la Campaign o el Canvas, configura el calendario de entrada o la hora de envío en una ventana futura (o duplica el recorrido si necesitas una copia limpia) y luego selecciona **Reanudar** o lanza según sea necesario. Consulta [Archivar Campaigns y Canvas]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### ¿Por qué mi Canvas no se guarda cuando no aparece ningún error? {#why-doesnt-my-canvas-save-when-no-error-appears}

Los filtros de **atributo personalizado** vacíos en los filtros de audiencia o a nivel de paso pueden bloquear el guardado sin un mensaje de validación detallado. Abre cada tarjeta de filtro, elimina las reglas de atributo personalizado incompletas o ingresa tanto el nombre del atributo como el valor, y luego selecciona **Guardar** nuevamente.

### ¿Por qué desapareció una etiqueta de mi Canvas o Campaign? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

Cuando se elimina una [etiqueta]({{site.baseurl}}/user_guide/messaging/governance/tags) de tu espacio de trabajo, Braze la elimina de cada Campaign y Canvas que la referenciaba. Esa limpieza no siempre genera su propia línea en el registro de cambios de un Canvas.

### ¿Cómo puedo ver los análisis de cada uno de mis componentes de Canvas? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Para ver los análisis de un componente de Canvas, ve a tu Canvas y desplázate hacia abajo en la página **Canvas Details**. Aquí puedes ver los análisis de cada componente. Consulta [Análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) para más detalles.

### ¿Cuándo es visible la participación de un paso en Canvas en un perfil de usuario? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

Los filtros como `Received Message from Canvas Step` se actualizan después de que Braze registra el evento correspondiente de envío, recepción o participación para ese paso. Los mensajes dentro de la aplicación pueden registrar impresiones por separado de las métricas de tipo envío. Consulta [¿Por qué un Canvas puede mostrar cero envíos aunque se registren impresiones?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged). Esos mismos eventos aparecen en las métricas de paso en **Canvas Details**.

### Al observar el número de usuarios únicos, ¿son más precisos los análisis de Canvas o el segmentador? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

El segmentador es una estadística más precisa para datos de usuarios únicos en comparación con las estadísticas de Canvas o Campaign. Esto se debe a que las estadísticas de Canvas y Campaign son números que Braze incrementa cuando algo sucede, lo que significa que hay variables que podrían hacer que este número difiera del que muestra el segmentador. Por ejemplo, los usuarios pueden convertir más de una vez para un Canvas o Campaign.

### ¿Por qué el número de usuarios que entran en un Canvas no coincide con el número esperado? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

El número de usuarios que entran en un Canvas puede diferir del número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, una audiencia se evalúa antes del desencadenante (a menos que se use un desencadenante de [cambio en atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Esto hará que los usuarios abandonen el Canvas si no forman parte de tu audiencia seleccionada antes de que se evalúen las acciones desencadenantes.

### ¿Qué sucede con los usuarios anónimos durante su recorrido en Canvas? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Aunque los usuarios anónimos pueden entrar y salir de Canvas, sus acciones no se asocian con un perfil de usuario específico hasta que se identifiquen, por lo que sus interacciones pueden no rastrearse completamente en tus análisis. Puedes usar el [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para generar un informe de estas métricas.

{% alert tip %}
Para obtener más ayuda con la solución de problemas de Canvas, asegúrate de contactar al soporte de Braze dentro de los 30 días posteriores a la ocurrencia de tu problema, ya que solo contamos con los últimos 30 días de registros de diagnóstico.
{% endalert %}

### ¿Puedo excluir a usuarios que actualmente están en un recorrido de Canvas de una Campaign o Segment? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Usa [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) como `Entered Canvas Variation`, `In Canvas Control Group` o `Received Message from Canvas Step` para segmentar usuarios según la entrada en Canvas, la asignación de variante o la participación en un paso. Estos filtros evalúan el historial de entrada y las interacciones; no indican si un usuario aún está avanzando a través de un recorrido activo.

Para incluir o excluir usuarios según su participación activa en un Canvas, añade pasos de [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) en la entrada y salida del Canvas para configurar y borrar atributos personalizados, y luego filtra por esos atributos en Campaigns o Segments.

## Segmentación {#segmentation}

### ¿Cuál es la diferencia entre "No ha entrado en la variante de Canvas" y "No está en el grupo de control de Canvas"? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) para ver las definiciones completas de los filtros.

#### No ha entrado en la variante de Canvas {#has-not-entered-canvas-variation}

El usuario nunca entró en una ruta de variante de un Canvas específico. Se incluyen todos los usuarios que no están en el grupo de control, independientemente de si han entrado en el Canvas. Esto incluye a los usuarios que entraron en otra variante y a los usuarios que no han entrado en ninguna variante.

#### No está en el grupo de control de Canvas {#is-not-in-canvas-control-group}

El usuario entró en el Canvas, pero no está en el grupo de control y, en consecuencia, recibió una variante. Esto solo incluye a los usuarios que entraron en el Canvas.

Ten en cuenta que la asignación de variantes se produce en el momento de la entrada al Canvas. Si un usuario no ha entrado en un Canvas, no se le asignará ninguna variante. En otras palabras, no estará en el grupo de control ni en una variante.

## Editor de Canvas original {#original-canvas-editor}

{% details Ampliar para ver las preguntas frecuentes del editor de Canvas original %}

### ¿Cómo convierto un Canvas existente del editor original al editor actual? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Puedes [clonar tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases). Esto crea una copia de tu Canvas original en el flujo de trabajo de Canvas más actual.

### ¿Cuáles son las principales diferencias entre los editores de Canvas actual y original? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Barra de herramientas de componentes de Canvas {#canvas-component-toolbar}

Anteriormente, con el editor de Canvas original, se añadía un paso completo de forma predeterminada cada vez que creabas cualquier paso en el recorrido de tu usuario. Estos pasos completos se han sustituido por diferentes componentes de Canvas, lo que te ofrece el beneficio de una mayor visibilidad y personalización en tu experiencia de edición. Puedes ver de inmediato todos los componentes de Canvas desde la barra de herramientas de pasos de Canvas.

#### Comportamiento de los pasos {#step-behavior}

Anteriormente, cada paso completo incluía información como configuraciones de retraso y programación, eventos de excepción, filtros de audiencia, configuración de mensajes y opciones de avance de mensajes, todo en un solo componente. Estas son configuraciones separadas en el editor actual para hacer tu experiencia de creación de Canvas más personalizable e introduce algunas diferencias en la funcionalidad.

#### Avance del componente de mensaje {#message-component-advancement}

Los [componentes de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hacen avanzar a todos los usuarios que entran en el paso. No es necesario especificar el comportamiento de avance del mensaje, lo que simplifica la configuración del paso general. Si quieres implementar la opción **Avanzar cuando se envía el mensaje**, añade un paso separado de rutas de audiencia para filtrar a los usuarios que no recibieron el paso anterior.

#### Comportamiento "en" del retraso {#delay-in-behavior}

Los [componentes de retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) esperarán todo el tiempo de retraso antes de proceder al siguiente paso.

Supongamos que el 12 de abril tenemos un componente de retraso en el que el retraso está configurado para enviar al usuario al siguiente paso en un día a las 2 pm. Un usuario entra en el componente a las 2:01 pm del 13 de abril.
- En el flujo de trabajo original, el usuario procedería al siguiente paso a las 2 pm del 14 de abril, lo cual es menos de un día desde el momento de entrada.
- En el editor actual, el usuario procedería al siguiente paso a las 2 pm del 15 de abril. Ten en cuenta que esta es la misma hora, pero más de un día desde el momento de entrada.

#### Comportamiento de la sincronización inteligente {#intelligent-timing-behavior}

Dado que la [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) se almacena en el componente de mensaje, los retrasos se aplicarán antes de los cálculos de sincronización inteligente. Esto significa que, dependiendo de cuándo entre un usuario en el componente, puede recibir el mensaje más tarde de lo que lo haría en un Canvas construido con el flujo de trabajo de Canvas original.

Supongamos que tu retraso está configurado en 2 días, la sincronización inteligente está activada y ha determinado que la mejor hora para enviar tu mensaje es a las 2 pm. Un usuario entra en el paso de retraso a las 2:01 pm.
- **Flujo de trabajo actual:** Pasarán 48 horas para que se complete el retraso, por lo que el usuario recibe el mensaje el tercer día a las 2 pm.
- **Flujo de trabajo original:** El usuario recibe el mensaje el segundo día a las 2 pm.

Ten en cuenta que, si la sincronización inteligente está activada, el mensaje se enviará dentro de las 24 horas posteriores a la entrada del usuario en el componente de mensaje, en el momento inteligente identificado (incluso si no hay un componente de retraso involucrado).

#### Eventos de excepción {#exception-events}

##### Horas tranquilas {#quiet-hours}

El evento de excepción se aplica utilizando rutas de acción, que son independientes de los pasos de mensaje. Las horas tranquilas se aplican en el componente de mensaje. Esto significa que, si un usuario ya pasó la ruta de acción (y no fue excluido con el evento de excepción), luego se encuentra con las horas tranquilas al llegar al componente de mensaje, y tenía su Canvas configurado de modo que el mensaje se reenvíe después del período de horas tranquilas, el evento de excepción ya no se aplicará. Ten en cuenta que este caso de uso no es común.

Para Segments y filtros, el paso de mensaje tiene validaciones de entrega que permiten a los usuarios configurar Segments y filtros adicionales que se validan en el momento del envío. Esto previene el caso límite de las horas tranquilas mencionado anteriormente.

##### Configuración de programación "en" o "en el siguiente" {#in-or-on-the-next-schedule-setting}

Los eventos de excepción se crean utilizando rutas de acción. Las rutas de acción solo admiten "después de un período de tiempo X" y no "en X tiempo" ni "en el siguiente X tiempo".

{% enddetails %}

### ¿Qué debo incluir al enviar un ticket de soporte por un error "Request Timed Out"? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Si encuentras un error "Request Timed Out" al editar un Canvas y necesitas contactar con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support), incluye la siguiente información para ayudar a agilizar la resolución:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Entrega y solución de problemas de Canvas {#canvas-delivery-and-troubleshooting}

### ¿Son elegibles los usuarios huérfanos para recibir mensajes de Canvas? {#are-orphaned-users-eligible-to-receive-canvas-messages}

No. Los [usuarios huérfanos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users) no son elegibles para recibir mensajes. Si un perfil queda huérfano mientras un usuario se encuentra en un recorrido de Canvas, este sale silenciosamente del flujo. Es posible que los análisis no siempre muestren un evento **Exited** para esa salida, y el resumen del flujo de trabajo puede incluir un `partial_update_token` sin `exited_date` ni `exit_reason`.

Para más información sobre fusiones y perfiles huérfanos, consulta [Fusionar usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

### Si detengo un Canvas o una Campaign activa, ¿los mensajes ya enviados al ESP siguen entregándose? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Sí. Después de que Braze envía una solicitud a tu proveedor de servicios de correo electrónico (ESP), Braze no puede retirar ese envío. Detener un Canvas o una Campaign evita nuevas solicitudes de envío, pero los mensajes que ya se entregaron al ESP pueden seguir siendo enviados e incrementar los conteos de envío a medida que el ESP los procesa.

Este es el mismo comportamiento descrito en [detener un Canvas](#what-happens-when-you-stop-a-canvas): los envíos de correo electrónico en curso no se detienen de inmediato.

### ¿Cómo puedo confirmar que un paso de webhook en Canvas se ejecutó sin contenido visible para el usuario? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze registra los **envíos** de webhook y los resultados de entrega relacionados para los pasos de [Webhook]({{site.baseurl}}/user_guide/channels/webhooks) en Campaigns y Canvas. Usa los análisis del paso, los [informes de webhook]({{site.baseurl}}/user_guide/channels/webhooks/reporting) o los eventos de webhook de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para confirmar que el paso se ejecutó. Los registros de solicitudes de tu endpoint proporcionan confirmación adicional cuando necesitas prueba de recepción del lado del servidor.

Braze no incluye un píxel de seguimiento invisible integrado para los pasos de webhook. Confía en las métricas de webhook de Braze y en los registros de tu endpoint en lugar de solicitudes personalizadas de imágenes de un píxel.

### ¿Por qué mi paso de webhook no tiene campo de cuerpo? {#why-does-my-webhook-step-have-no-body-field}

Los pasos de webhook usan un cuerpo de solicitud para `POST`, `PUT`, `PATCH` y `DELETE`. Si cambias el método a `GET`, Braze elimina el campo de cuerpo porque las solicitudes GET no admiten un cuerpo de solicitud. Cambia de vuelta a un método que admita cuerpo si necesitas enviar datos JSON o de formulario. Para más detalles sobre los métodos, consulta [Crear un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method).

### ¿Cómo uso spacer.gif en un paso de webhook? {#how-do-i-use-spacergif-in-a-webhook-step}

Braze aloja una imagen de marcador de posición `spacer.gif` en `cdn.braze.com` y `braze-images.com`. Algunos equipos apuntan la URL de un webhook a esta imagen cuando un paso debe ejecutarse sin llamar a un endpoint externo. Los pasos estándar de webhook deben llamar a un endpoint real. Usa los [informes de webhook]({{site.baseurl}}/user_guide/channels/webhooks/reporting) y los registros de tu endpoint para confirmar la entrega, como se describe en [¿Cómo puedo confirmar que un paso de webhook en Canvas se ejecutó sin contenido visible para el usuario?](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content).

### ¿Por qué mi Canvas no carga con un error "invalid next-step-id"? {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

Este error de consola significa que al menos un paso apunta a un paso siguiente faltante o no válido, por ejemplo, después de una eliminación parcial, clonación o importación. Abre el Canvas en el editor, reconecta los pasos huérfanos o elimina los pasos que ya no tienen una ruta válida hacia adelante. Si el Canvas sigue sin cargar, contacta al [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) con el ID de Canvas y una captura de pantalla del error de consola.

### ¿Por qué la marca de tiempo de conversión de Canvas en Currents difiere de mis análisis de Canvas? {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currents registra las conversiones de Canvas como eventos [`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events). El `time` del evento es el momento en que ocurrió el evento de conversión. El campo `conversion_behavior` en ese evento describe la definición de conversión (tipo y ventana). Los análisis de Canvas también pueden agrupar conversiones en relación con la entrada al Canvas dentro de la ventana de conversión. Al reconciliar exportaciones, compara el `time` de Currents con la marca de tiempo del evento de conversión y la configuración de tu ventana de conversión de Canvas.

### ¿Por qué `canvas_step_name` es null en Currents? {#why-is-canvas_step_name-null-in-currents}

Los campos de nombre de Campaign y Canvas, como `canvas_step_name`, pueden ser `null` cuando un evento de Currents se envía antes de que Braze termine de propagar los metadatos del paso, por ejemplo, después de crear o renombrar un paso. Para más detalles, consulta [¿Por qué el nombre de la Campaign o el nombre del paso de Canvas es `NULL` en mis datos de Currents?]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data).

### ¿Por qué mi array no se actualiza en un paso de actualización de usuario? {#why-isnt-my-array-updating-in-a-user-update-step}

Verifica el JSON en tu paso de [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Las actualizaciones de arrays y atributos anidados necesitan rutas y valores válidos para el atributo que estás modificando. No incluyas campos que el paso proporciona automáticamente, como el ID de usuario externo. Usa la pestaña **Vista previa y prueba** del paso para confirmar la carga útil antes del lanzamiento.

### ¿Puedo enviar mensajes de Canvas a usuarios sin un `external_id`? {#can-i-send-canvas-messages-to-users-without-an-external_id}

Sí, si ya existe un perfil de usuario en Braze. Los usuarios sin un `external_id` son [usuarios anónimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) y se puede hacer referencia a ellos con un `braze_id` o un [alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases). Crea o actualiza el perfil con el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) o tu SDK antes de la entrada al Canvas, luego usa [entrada basada en acciones o activada por API]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule). La segmentación estándar de Canvas aún requiere un perfil de usuario en Braze: no puedes enviar mensajes de Canvas a una dirección de correo electrónico sin perfil.

### ¿Por qué un usuario entró a un Canvas menos veces de las que realizó el evento desencadenante? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Para Canvas basados en acciones y activados por API, Braze desduplica los eventos desencadenantes para que un usuario pueda entrar como máximo **una vez por segundo** para el mismo Canvas. Si un usuario realiza el mismo evento desencadenante varias veces en el mismo segundo, solo se procesa una entrada.

Para permitir múltiples entradas en el mismo segundo, separa los eventos desencadenantes por al menos 1,1 segundos (por ejemplo, cuando controlas el momento del evento desde tu servidor). Para un comportamiento similar al de una Campaign que permita múltiples desencadenamientos en el mismo segundo, compara tu caso de uso con [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) con la programación y configuración de reelegibilidad apropiadas.

### ¿Cuándo se desduplican los usuarios en Canvas activados por API? {#when-are-users-de-duplicated-in-api-triggered-canvases}

Si un usuario vuelve a entrar en un Canvas activado por API y llega a un paso de Retraso donde ya está en cola por una entrada anterior para un mensaje idéntico, Braze desduplica al usuario para evitar envíos duplicados. La segunda instancia de Canvas sale, por lo que el número de entradas puede superar el número de envíos.

### ¿Por qué un push de prueba va a la aplicación incorrecta, pero los envíos en vivo se ven correctos? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

El **push de prueba** en un perfil de usuario se entrega a todos los dispositivos habilitados para push de ese perfil. Cuando hay varias aplicaciones instaladas en un dispositivo, el sistema operativo normalmente entrega la notificación de prueba a la primera aplicación disponible, que puede no ser la aplicación que deseas validar.

Para confirmar la segmentación específica de la aplicación, envía un mensaje en vivo o de prueba a través de una Campaign o Canvas con una audiencia reducida (por ejemplo, filtra por `external_id`) en lugar de depender solo del **push de prueba** del perfil.

Para los pasos de mensaje de **Canvas** con múltiples aplicaciones, activa **Validar audiencia en el envío del mensaje** en el paso de mensaje para que las comprobaciones de Segment y filtros se ejecuten en el momento del envío. Para más información, consulta [Paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

Para el comportamiento general del push de prueba, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) y [Preguntas frecuentes sobre push]({{site.baseurl}}/user_guide/channels/push/faqs).

### ¿Cómo depuro Push Stories en iOS y Android? {#how-do-i-debug-push-stories-on-ios-and-android}

Comienza con [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) para los requisitos de configuración y creatividad. Para la implementación y el manejo de notificaciones enriquecidas, consulta [Notificaciones enriquecidas]({{site.baseurl}}/developer_guide/push_notifications/rich) y [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories) en la Guía del desarrollador.

### ¿Quién recibe el correo electrónico "Canvas Messages Delayed 24+ Hours"? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze envía esta notificación cuando los mensajes de Canvas se retrasan por límites de velocidad durante 24 horas o más. El correo electrónico se envía a los usuarios del panel que anteriormente realizaron cambios en el Canvas afectado (basándose en los registros de cambios del Canvas). Si Braze no puede determinar esos destinatarios, el correo electrónico se envía a los **administradores de la empresa** del espacio de trabajo.

### ¿Cuándo deja un usuario de recibir mensajes después de un evento de excepción? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze registra la salida tan pronto como ocurre el evento de excepción, pero los usuarios pueden permanecer dentro de un paso hasta que los temporizadores finalicen, algo más visible en los pasos de Retraso. El comportamiento también difiere entre pasos programados y pasos activados por eventos. Para cronologías, ejemplos y matices de los análisis, consulta [Criterios de salida]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

### ¿Por qué mi paso de Rutas de Acción muestra un error cuando selecciono una interacción de alias de enlace? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

Los grupos de acciones que usan desencadenantes de interactividad de correo electrónico (por ejemplo, **Click alias in email** o **Clicked alias in any campaign or Canvas step**) necesitan un paso de mensaje que ya haya enviado el mensaje que contiene ese enlace. Añade o reordena los pasos para que el correo electrónico se envíe antes de que el paso de Rutas de Acción evalúe el clic, o elige una interacción que coincida con un mensaje que el usuario ya recibió en este Canvas. Para la lista completa de desencadenantes de interacción, consulta [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

### ¿Cómo afectan las marcas de tiempo históricas de eventos personalizados a los Canvas y Campaigns basados en acciones? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze evalúa los recorridos basados en acciones cuando los eventos calificados se ingestan y el usuario cumple tus reglas de audiencia. Si un evento llega al perfil fuera de la ventana en la que tu Canvas o Campaign estaba activa, o antes de que el usuario coincidiera con tu audiencia, es posible que la entrada o los envíos posteriores no ocurran como se esperaba. Compara las marcas de tiempo de los eventos con los momentos de activación y la pertenencia al Segment usando el registro de actividad del perfil de usuario y los pasos de solución de problemas en [Solución de problemas de eventos personalizados]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events). Si el comportamiento sigue sin coincidir con las expectativas, contacta al [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).