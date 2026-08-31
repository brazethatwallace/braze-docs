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

### ¿Existen límites de tamaño para las propiedades de entrada de Canvas? {#are-there-size-limits-for-canvas-entry-properties}

Sí. El [objeto de contexto de Canvas]({{site.baseurl}}/api/objects_filters/context_object) (propiedades de entrada de Canvas) tiene un tamaño máximo de 50&nbsp;KB. Mantén las cargas útiles lo más pequeñas posible dentro de ese límite. Para saber cómo funcionan las propiedades de entrada y de evento en Canvas, consulta [Propiedades de contexto y evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).

### ¿Por qué veo un error de "Too many Canvas branches"? {#why-do-i-see-a-too-many-canvas-branches-error}

Este error aparece cuando la combinación de ramificaciones de pasos y el tamaño del público de entrada puede crear problemas de rendimiento del clúster que impidan el envío de mensajes. Para conocer los pasos de resolución, incluido el uso de [rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), la reducción de ramificaciones o del tamaño del público y la reconstrucción en Canvas Flow, consulta [Error de "Too many Canvas branches"]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error).

### ¿Puedo usar Optimize with BrazeAI<sup>TM</sup> con la reelegibilidad en un Canvas? {#can-i-use-optimize-with-brazeai-with-re-eligibility-in-a-canvas}

Sí. Los Canvas pueden usar [Optimize with BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai) cuando la reelegibilidad está habilitada. Braze no puede garantizar la misma variante en la reentrada porque la asignación cambia con el tiempo. Campaigns requiere una ventana de reelegibilidad de 24 horas o más cuando **Optimize with BrazeAI<sup>TM</sup>** está activado.

### ¿Cuál es la diferencia entre un componente y un paso? {#whats-the-difference-between-a-component-and-a-step}

Un [componente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about) es una parte individual de tu Canvas que puedes usar para determinar la efectividad de tu Canvas. Los componentes pueden incluir acciones como dividir el recorrido del usuario, añadir un retraso e incluso probar múltiples rutas de Canvas. Un paso en Canvas se refiere al recorrido personalizado del usuario en las ramas de tu Canvas. Esencialmente, tu Canvas está compuesto por componentes individuales que crean pasos para el recorrido de tu usuario.

### ¿Puedo lanzar un Canvas con pasos desconectados? {#can-i-launch-a-canvas-with-disconnected-steps}

Sí. También puedes guardar Canvas después del lanzamiento con pasos desconectados.

### ¿Adónde van los usuarios cuando llegan a un paso desconectado? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Si un usuario se encuentra en un paso desconectado del flujo de trabajo de tu Canvas, avanzará al paso siguiente si existe uno, y la configuración del paso determinará cómo debe avanzar el usuario. Esto tiene como objetivo permitir a los usuarios realizar cambios en los pasos sin tener que conectarlos directamente al resto del Canvas. Esto también te da margen para realizar pruebas antes de publicar de inmediato, lo que permite guardar un borrador de forma efectiva.

Te recomendamos revisar la vista de análisis para ver los usuarios pendientes en un paso de Canvas antes de desconectar un paso.

### ¿Qué sucede si el público y la hora de envío son idénticos para un Canvas que tiene una variante, pero múltiples ramas? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Ponemos en cola un trabajo para cada paso: se ejecutan aproximadamente al mismo tiempo y uno de ellos "gana". En la práctica, esto puede distribuirse de manera algo equitativa, pero es probable que haya al menos un ligero sesgo hacia el paso que se creó primero.

Además, no podemos garantizar exactamente cómo será esa distribución. Si deseas una división equitativa, añade un filtro de [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers).

### ¿Cómo se evalúan los públicos de Canvas? {#how-are-canvas-audiences-evaluated}

De forma predeterminada, los filtros y Segments para pasos completos en el Canvas se verifican en el momento del envío. El paso de división de decisiones realiza una evaluación justo después de recibir un paso anterior (o antes de un retraso).

### ¿Cuándo se activa un evento de excepción? {#when-does-an-exception-event-trigger}

Los eventos de excepción solo se activan mientras el usuario espera recibir el componente de Canvas con el que está asociado. Si un usuario realiza una acción con anticipación, el evento de excepción no se activará. Si deseas excluir a los usuarios que han realizado un determinado evento con anticipación, utiliza [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) en su lugar.

### ¿Cómo afecta la edición de un Canvas a los usuarios que ya están en el Canvas? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Si editas algunos de los pasos de un Canvas de varios pasos, los usuarios que ya estaban en el público pero no han recibido los pasos recibirán la versión actualizada del mensaje. Ten en cuenta que esto solo sucederá si aún no han sido evaluados para el paso.

Para obtener más información sobre lo que puedes editar después del lanzamiento, consulta [Cambiar tu Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits).

### ¿Qué sucede cuando detienes un Canvas? {#what-happens-when-you-stop-a-canvas}

Cuando detienes un Canvas, se aplica lo siguiente:

- Se impedirá que los usuarios entren al Canvas.
- No se enviarán más mensajes, independientemente de dónde se encuentre el usuario en el flujo.
- **Excepción:** Los Canvas con correos electrónicos no se detendrán de inmediato. Una vez que las solicitudes de envío llegan a SendGrid, no hay nada que podamos hacer para evitar que se entreguen al usuario.

### ¿Debería crear un solo Canvas o Canvas separados por ciclo de vida del usuario? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Dependiendo de lo que quieras lograr con tu Canvas, es posible que necesites diferentes enfoques para construir el recorrido del usuario. La flexibilidad de Canvas te permite mapear los recorridos del usuario para cualquier etapa del ciclo de vida del usuario. Consulta nuestras [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para ver varios ejemplos de enfoques optimizados para crear recorridos de usuario efectivos.

## Mensajes y entrega {#messages-and-delivery}

### ¿Cuándo se envían los mensajes dentro de la aplicación en Canvas? {#when-are-in-app-messages-in-canvas-sent}

Los mensajes dentro de la aplicación se envían en el siguiente inicio de sesión. Esto significa que, si el usuario entra en el paso de Canvas antes de que se detenga el Canvas, seguirá recibiendo el mensaje dentro de la aplicación en su siguiente inicio de sesión, siempre y cuando el mensaje dentro de la aplicación no haya expirado todavía.

Es posible que un usuario inicie una sesión antes de que se detenga el Canvas, pero no se le muestre el mensaje dentro de la aplicación de inmediato. Esto puede ocurrir si el mensaje dentro de la aplicación se desencadena por un evento personalizado o tiene un retraso. Esto significa que es posible que un usuario registre una impresión de mensaje dentro de la aplicación y "reciba" el mensaje dentro de la aplicación después de que se detenga el Canvas. Sin embargo, el usuario tendría que haber iniciado la sesión antes de que se detuviera el Canvas, pero **después** de recibir el paso de Canvas.

{% alert note %}
Detener un Canvas no hará que los usuarios que están esperando recibir mensajes salgan del recorrido de usuario. Si reactivas el Canvas y los usuarios aún están esperando el mensaje, lo recibirán (a menos que el momento en que debería haberse enviado el mensaje ya haya pasado, en cuyo caso no lo recibirán).
{% endalert %}

### ¿Por qué un Canvas puede mostrar cero envíos aunque se registren impresiones? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Si los _Mensajes enviados_ siempre son cero para un Canvas que contiene un paso de mensaje dentro de la aplicación, esto se debe a que la entrega de mensajes dentro de la aplicación funciona de manera diferente a otros canales de mensajería.

Los mensajes dentro de la aplicación son "extraídos" por el SDK, en lugar de ser "enviados" desde Braze. Los mensajes dentro de la aplicación para usuarios elegibles se entregan automáticamente al inicio de la sesión y "esperan" al evento desencadenante antes de mostrarse. Dado que los usuarios elegibles reciben el mensaje cuando inician una sesión, Braze no registra esto como un evento de envío. Cuando los usuarios realizan el evento desencadenante, el mensaje se muestra y Braze registra una impresión y marca el paso de Canvas (o Campaign) como recibido en el perfil de usuario. En consecuencia, el total de _Envíos_ es cero para los mensajes dentro de la aplicación.

### ¿Por qué los usuarios no recibieron mi mensaje dentro de la aplicación después de un retraso largo o una rama? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

Después de que se completen los pasos de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) upstream y las comprobaciones de audiencia, los usuarios se vuelven elegibles para un mensaje dentro de la aplicación solo cuando llegan al paso de Mensaje. Si el mensaje expira en una fecha del calendario o en una ventana corta de **duración después de que el paso esté disponible**, los usuarios en ramas más lentas pueden llegar después de la expiración y nunca ver el mensaje. Alinea la expiración con los retrasos de recorrido más largos y realistas. Para más información y ejemplos, consulta [Expiración de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration).

### ¿Por qué veo "Canvas Entry Properties may not be used in In-App Messages."? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

Este mensaje aparece cuando la personalización hace referencia a campos que los mensajes dentro de la aplicación no pueden resolver en Canvas. Usa el objeto `context` como se describe en [Propiedades de contexto y eventos]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) y [Paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). El namespace Liquid heredado `canvas_entry_properties` tiene restricciones diferentes a las de `context`. Si necesitas que los valores persistan a lo largo de varios pasos, revisa las [propiedades persistentes en el editor original de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) con tu equipo de Braze. Los valores almacenados se borran cuando un usuario sale del Canvas antes de que el dispositivo descargue la carga útil del mensaje dentro de la aplicación.

### ¿Dónde puedo encontrar los clics en botones para mensajes dentro de la aplicación de arrastrar y soltar en Canvas? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

Las métricas a nivel de botón para mensajes dentro de la aplicación de arrastrar y soltar aparecen en la tarjeta de análisis del paso de **Mensaje** en **Detalles del Canvas**, no solo en el resumen de alto nivel del Canvas. Abre el Canvas, selecciona el paso de Mensaje y revisa la participación del mensaje dentro de la aplicación allí. Para conceptos de informes, consulta [Medición y pruebas con análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### ¿Puedo programar diferentes horarios de envío para cada variante en el mismo paso de Mensaje de Canvas o envío multivariante? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

No. Las variantes en la misma configuración multivariante o paso de Mensaje comparten un programa de entrega. No puedes asignar una variante para que se envíe a las 6 pm y otra a las 7 pm para el mismo envío programado.

Para escalonar los envíos o usar diferentes horarios por recorrido, prueba los siguientes métodos:

- Separa los pasos de Mensaje con pasos de Retraso entre ellos para que cada mensaje tenga su propio programa.
- Usa ramas o un paso de [Recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que los usuarios sigan recorridos con diferente sincronización.
- Usa Campaigns separadas si el caso de uso no necesita permanecer dentro de un solo Canvas.

Para conceptos multivariantes y de pruebas A/B en Campaigns, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

### ¿Qué sucede si un usuario tiene limitación de frecuencia global en un paso de Mensaje de Canvas? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

No recibe ese envío para el canal limitado, pero los pasos de Mensaje aún avanzan a los usuarios cuando un mensaje no se envía debido a la limitación de frecuencia global. Para los casos de avance paso a paso, consulta [Cómo avanzan los usuarios]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). La limitación de frecuencia global por sí sola no saca a los usuarios de un Canvas; ese comportamiento es independiente de las **Validaciones de entrega** en un paso de Mensaje. Para más detalles, consulta [Límite de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### ¿Por qué los envíos son menores que el tamaño estimado de la audiencia? {#why-are-sends-lower-than-the-estimated-audience-size}

Los envíos pueden ser menores que la **Audiencia estimada** por muchas de las mismas razones que en las [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size), incluyendo limitaciones de frecuencia, filtros estrictos de dispositivo o navegador, ventanas de reelegibilidad, límites de velocidad y exclusiones a nivel de canal (por ejemplo, alcanzabilidad push o comprobaciones de suscripción y capacidad de entrega de correo electrónico).

Los factores específicos de Canvas también aplican:

- **Entrada basada en acciones o activada por API:** Los usuarios solo entran (y reciben pasos) después de realizar el comportamiento de entrada, por lo que los envíos realizados van por detrás de la estimación inicial hasta que se produzcan esas acciones.
- **Rutas de audiencia:** Los usuarios son dirigidos a la rama de mayor prioridad para la que califican, por lo que las ramas posteriores pueden recibir menos usuarios de lo que sugiere un conteo plano de Segment.
- **Comprobaciones de audiencia y hora de envío:** Los pasos completos reevalúan los filtros en el momento del envío a menos que lo configures de otra manera. Los usuarios que calificaban cuando se creó el Canvas pueden caer antes de que se envíe un mensaje.
- **Grupos de control:** Los grupos de control global o de Canvas retienen una parte de los ingresantes de la mensajería.
- **Horas tranquilas y retrasos:** Los mensajes pueden ser retenidos o reprogramados, desplazando los envíos fuera de la ventana de informes que estás visualizando.
- **Límites máximos de entrada o audiencia:** Los límites de entrada o envío detienen a los usuarios adicionales incluso cuando el Segment subyacente es mayor.
- **Ventana de informes:** El rango de análisis puede no incluir todos los envíos que estás comparando con la estimación.

### ¿Por qué la audiencia estimada y los recuentos de usuarios de Canvas no coinciden? {#why-dont-estimated-audience-and-canvas-user-counts-match}

La **Audiencia estimada** refleja quién coincide con tu Segment y los filtros de entrada cuando se ejecuta la estimación. Después de ese momento, las entradas retrasadas o basadas en acciones, la reelegibilidad, los desencadenantes por API o el enrutamiento de ramas pueden aumentar la cantidad de perfiles que interactúan con el recorrido en comparación con la instantánea. Los usuarios también pueden caer cuando los filtros del momento de envío fallan, lo que reduce las entradas o envíos realizados. Compara la sincronización, los límites y la configuración de evaluación junto con [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?](#why-are-sends-lower-than-the-estimated-audience-size).

### ¿Por qué los _Destinatarios únicos_ son más que el número de usuarios que segmenté? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

Los _Destinatarios únicos_ pueden ser más que la audiencia que esperabas porque Braze rastrea los **destinatarios únicos diarios** para los informes de Canvas y Campaign. Esto permite una atribución de conversión precisa cada vez que un usuario recibe un mensaje en el recorrido.

Por ejemplo, si un usuario recibe un paso de Canvas el lunes y de nuevo el viernes y convierte después de cada envío, Braze puede contar dos filas de destinatarios y dos conversiones dentro del alcance. Con entradas recurrentes o reelegibilidad, el mismo conjunto pequeño de perfiles puede producir múltiples _Destinatarios únicos_ a lo largo de varios días.

### ¿Por qué mi Canvas tiene tasas de envío más bajas? {#why-is-my-canvas-experiencing-lower-send-rates}

Si descubres que los envíos diarios programados de tu Canvas llegan a menos usuarios con el tiempo, verifica lo siguiente:

- **Comprueba si la reelegibilidad está activada:** Sin reelegibilidad, Braze ingresa a cada usuario en el Canvas solo una vez. En Canvas con programación diaria, solo los usuarios que coinciden con la audiencia y que aún no han ingresado al Canvas son elegibles para cada entrada. A medida que más usuarios ingresan, cada entrada posterior tiene menos usuarios elegibles, por lo que el volumen de entrada disminuye.
- **Comprueba si la audiencia tiene membresía fija:** Las audiencias construidas a partir de una lista de usuarios fija (como una [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) utilizada como filtro de Segment) no ganan nuevos miembros automáticamente. Sin nuevos ingresantes, el volumen de entrada no puede recuperarse a medida que los usuarios ingresan al Canvas.

Para [límites de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) y otros factores que reducen los envíos en una sola ocurrencia, consulta [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?](#why-are-sends-lower-than-the-estimated-audience-size).

### ¿Por qué un Segment de grupo de control pequeño muestra cambios en la membresía histórica? {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

Los gráficos de membresía histórica utilizan muestras estimadas, por lo que los Segments pequeños, incluidos los Segments de [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group), pueden mostrar movimientos diarios incluso cuando la audiencia subyacente es estable. Para saber cómo funcionan las estimaciones y por qué los gráficos pueden fluctuar, consulta [Visualización del tamaño histórico de membresía de Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size).

## Análisis y conversiones {#analytics-and-conversions}

### ¿Cómo atribuye el panel de Conversiones las conversiones de Canvas? {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

El [panel de Conversiones]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) atribuye las conversiones de Canvas según el [método de atribución]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods) que selecciones (por ejemplo, **Upon Receipt**, **Upon Send**, **Upon Open** o **Upon Click**). Para que un usuario aparezca en el informe, debe entrar en el Canvas o Campaign, registrar el método de atribución seleccionado y realizar el evento de conversión dentro de la configuración de tu informe.

Para las reglas de conversión a nivel de paso y a nivel de variante en los análisis de Canvas, consulta [¿Cómo se rastrean las conversiones de usuario en un Canvas?](#how-are-user-conversions-tracked-in-a-canvas).

### ¿Cómo se rastrean las conversiones de usuario en un Canvas? {#how-are-user-conversions-tracked-in-a-canvas}

Un usuario solo puede convertir una vez por entrada al Canvas. Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El bloque de resumen al inicio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, independientemente de si recibieron un mensaje o no. Cada paso posterior solo mostrará las conversiones que ocurrieron mientras ese era el paso más reciente que el usuario recibió.

{% alert note %}
Cuando un usuario vuelve a entrar en un Canvas, los eventos de conversión solo se rastrean para la entrada más reciente. Los eventos de conversión no se registran para entradas anteriores, incluso si el evento de conversión se rellena de forma retroactiva.
{% endalert %}

{% details Expande para ver ejemplos %}

**Ejemplo 1**

Hay una ruta de Canvas con 10 notificaciones push y el evento de conversión es "inicio de sesión" ("Abre la aplicación"):

- El usuario A abre la aplicación después de entrar pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

**Resultado:** El resumen mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión de uno en el primer paso y cero en todos los pasos siguientes.

{% alert note %}
Si las horas tranquilas están activas cuando ocurre el evento de conversión, se aplican las mismas reglas.
{% endalert %}

**Ejemplo 2**

Hay un Canvas de un solo paso con horas tranquilas habilitadas:

1. El usuario entra en el Canvas.
2. El primer paso no tiene un retraso, pero está dentro de las horas tranquilas configuradas, por lo que el mensaje se suprime.
3. El usuario realiza el evento de conversión.

**Resultado:** El usuario contará como convertido en la variante general del Canvas, pero no en el paso, ya que no recibió el paso.

{% enddetails %}

### ¿Cuál es la diferencia entre los distintos tipos de tasa de conversión? {#whats-the-difference-between-the-different-conversion-rate-types}

- Las conversiones totales de Canvas reflejan cuántos usuarios únicos completaron un evento de conversión, no cuántas conversiones completó cada uno.
- La tasa de conversión de la variante o el bloque de resumen al inicio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, independientemente de si recibieron un mensaje, como un total agregado.
- La tasa de conversión del paso refleja cuántas personas recibieron ese paso del mensaje y completaron cualquiera de los eventos de conversión descritos.

### ¿Por qué la tasa de conversión de mi paso de Canvas no es igual a la tasa de conversión total de mi variante de Canvas? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Es habitual que el total de conversiones de una variante de Canvas sea mayor que la suma del total de sus pasos. Esto ocurre porque un usuario puede realizar un evento de conversión para una variante tan pronto como entra en ella. Sin embargo, ese mismo evento de conversión no cuenta para un paso de Canvas. Así, cualquier usuario que entre en el Canvas y realice el evento de conversión antes de recibir el primer paso de Canvas se cuenta para el total de conversiones de la variante y no para el total del paso. Lo mismo aplica para un usuario que entra en el Canvas pero sale antes de recibir algún paso.

Ten en cuenta que también es posible que un usuario entre en una variante, no reciba ningún mensaje de un paso y luego convierta. En este caso, no se registra una conversión a nivel de paso. Sin embargo, dado que el usuario técnicamente convirtió, se registra una conversión a nivel de Canvas.

### ¿Cómo puedo confirmar si mis usuarios recibieron un Canvas activado por API? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Puedes [crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) usando un filtro de Canvas para confirmar si los usuarios entraron en el Canvas o recibieron un paso específico de Canvas. Por ejemplo, usa un filtro de entrada al Canvas si quieres confirmar que los usuarios entraron en el Canvas activado por API, o un filtro de paso recibido si quieres confirmar que recibieron un mensaje del Canvas. Luego, usa el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para exportar los usuarios de ese segmento.

### ¿Puedo eliminar un Canvas? {#can-i-delete-a-canvas}

No, pero puedes [archivar un Canvas]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### ¿Cómo reanudo un Canvas o Campaign archivado? {#how-do-i-resume-an-archived-canvas-or-campaign}

Los mensajes archivados no se envían hasta que los devuelvas a un estado editable. [Desarchiva]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving) el Campaign o Canvas, configura el calendario de entrada o la hora de envío en una ventana futura (o duplica el recorrido si necesitas una copia limpia), y luego selecciona **Resume** o lanza según sea necesario. Consulta [Archivar Campaigns y Canvas]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### ¿Por qué mi Canvas no se guarda cuando no aparece ningún error? {#why-doesnt-my-canvas-save-when-no-error-appears}

Los filtros vacíos de **Custom attribute** en la audiencia o en los filtros a nivel de paso pueden bloquear el guardado sin un mensaje de validación detallado. Abre cada tarjeta de filtro, elimina las reglas de atributos personalizados incompletas o introduce tanto el nombre del atributo como el valor, y luego selecciona **Save** de nuevo.

### ¿Por qué desapareció una etiqueta de mi Canvas o Campaign? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

Cuando se elimina una [etiqueta]({{site.baseurl}}/user_guide/messaging/governance/tags) de tu espacio de trabajo, Braze la elimina de cada Campaign y Canvas que la referenciaba. Esa limpieza no siempre genera su propia línea en el registro de cambios del Canvas.

### ¿Cómo puedo ver los análisis de cada uno de mis componentes de Canvas? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Para ver los análisis de un componente de Canvas, ve a tu Canvas y desplázate hacia abajo en la página de **Canvas Details**. Aquí podrás ver los análisis de cada componente. Consulta [Análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) para más detalles.

### ¿Cuándo es visible la participación de un paso de Canvas en el perfil de usuario? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

Filtros como `Received Message from Canvas Step` se actualizan después de que Braze registra el evento correspondiente de envío, recepción o participación para ese paso. Los mensajes dentro de la aplicación pueden registrar impresiones de forma separada de las métricas de tipo envío. Consulta [¿Por qué un Canvas puede mostrar cero envíos aunque se registren impresiones?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged). Esos mismos eventos aparecen en las métricas del paso en **Canvas Details**.

### Al observar el número de usuarios únicos, ¿qué es más preciso: los análisis de Canvas o el segmentador? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

El segmentador es una estadística más precisa para los datos de usuarios únicos en comparación con las estadísticas de Canvas o Campaign. Esto se debe a que las estadísticas de Canvas y Campaign son números que Braze incrementa cuando algo sucede, lo que significa que hay variables que podrían hacer que este número sea diferente al del segmentador. Por ejemplo, los usuarios pueden convertir más de una vez para un Canvas o Campaign.

### ¿Por qué el número de usuarios que entran en un Canvas no coincide con el número esperado? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

El número de usuarios que entran en un Canvas puede diferir de tu número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, la audiencia se evalúa antes del desencadenante (a menos que se use un desencadenante de [cambio en atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Esto hará que los usuarios salgan del Canvas si no forman parte de tu audiencia seleccionada antes de que se evalúen las acciones desencadenantes.

### ¿Qué sucede con los usuarios anónimos durante su recorrido en Canvas? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Aunque los usuarios anónimos pueden entrar y salir de Canvas, sus acciones no se asocian con un perfil de usuario específico hasta que se identifican, por lo que sus interacciones pueden no rastrearse completamente en tus análisis. Puedes usar el [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para generar un informe de estas métricas.

{% alert tip %}
Para obtener ayuda adicional con la solución de problemas de Canvas, asegúrate de contactar con el soporte de Braze dentro de los 30 días posteriores a la ocurrencia de tu problema, ya que solo disponemos de los últimos 30 días de registros de diagnóstico.
{% endalert %}

### ¿Puedo excluir a los usuarios que están actualmente en un recorrido de Canvas de un Campaign o Segment? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Usa [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) como `Entered Canvas Variation`, `In Canvas Control Group` o `Received Message from Canvas Step` para segmentar usuarios según la entrada al Canvas, la asignación de variante o la participación en un paso. Estos filtros evalúan el historial de entradas e interacciones; no indican si un usuario aún está progresando a través de un recorrido activo.

Para incluir o excluir usuarios según la participación activa en Canvas, añade pasos de [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) en la entrada y salida del Canvas para establecer y borrar atributos personalizados, y luego filtra por esos atributos en Campaigns o Segments.

## Segmentación {#segmentation}

### ¿Cuál es la diferencia entre "Has not entered Canvas variation" y "Is not in Canvas control group"? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) para ver las definiciones completas de los filtros.

#### Has not entered Canvas variation {#has-not-entered-canvas-variation}

El usuario nunca entró en una ruta de variante de un Canvas específico. Todos los usuarios que no están en el grupo de control están incluidos, independientemente de si han entrado en el Canvas. Esto incluye a los usuarios que entraron en otra variante y a los usuarios que no han entrado en ninguna variante.

#### Is not in Canvas control group {#is-not-in-canvas-control-group}

El usuario entró en el Canvas, pero no está en el grupo de control y, en consecuencia, recibió una variante. Esto solo incluye a los usuarios que entraron en el Canvas.

Ten en cuenta que la asignación de variantes ocurre en el momento de la entrada al Canvas. Si un usuario no ha entrado en un Canvas, no se le asignará ninguna variante. Es decir, no estará en el grupo de control ni en una variante.

## Editor de Canvas original {#original-canvas-editor}

{% details Ampliar para ver las preguntas frecuentes del editor de Canvas original %}

### ¿Cómo convierto un Canvas existente del editor original al editor actual? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Puedes [clonar tu Canvas]({{site.baseurl}}/cloning_canvases). Esto crea una copia de tu Canvas original en el flujo de trabajo de Canvas más reciente.

### ¿Cuáles son las principales diferencias entre los editores de Canvas actual y original? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Barra de herramientas de componentes de Canvas {#canvas-component-toolbar}

Anteriormente, con el editor de Canvas original, se añadía un paso completo de forma predeterminada cada vez que creabas cualquier paso en el recorrido del usuario. Estos pasos completos se reemplazan por diferentes componentes de Canvas, lo que te ofrece mayor visibilidad y personalización en tu experiencia de edición. Puedes ver inmediatamente todos los componentes de Canvas desde la barra de herramientas de pasos en Canvas.

#### Comportamiento de los pasos {#step-behavior}

Anteriormente, cada paso completo incluía información como la configuración de retraso y programación, eventos de excepción, filtros de audiencia, configuración de mensajes y opciones de avance de mensajes, todo en un solo componente. En el editor actual, estas son configuraciones separadas que hacen tu experiencia de creación de Canvas más personalizable e introducen algunas diferencias en la funcionalidad.

#### Avance del componente de mensaje {#message-component-advancement}

Los [componentes de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hacen avanzar a todos los usuarios que entran en el paso. No es necesario especificar el comportamiento de avance de mensajes, lo que simplifica la configuración general del paso. Si deseas implementar la opción **Avanzar cuando se envíe el mensaje**, añade una ruta de audiencia separada para filtrar a los usuarios que no recibieron el paso anterior.

#### Comportamiento de retraso "en" {#delay-in-behavior}

Los [componentes de retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) esperarán todo el tiempo de retraso antes de pasar al siguiente paso.

Supongamos que el 12 de abril tenemos un componente de retraso configurado para enviar a tu usuario al siguiente paso en un día a las 2 p. m. Un usuario entra en el componente a las 2:01 p. m. del 13 de abril.
- Con el flujo de trabajo original, el usuario avanzaría al siguiente paso a las 2 p. m. del 14 de abril, que es menos de un día desde el momento de entrada.
- En el editor actual, el usuario avanzaría al siguiente paso a las 2 p. m. del 15 de abril. Ten en cuenta que es la misma hora, pero más de un día desde el momento de entrada.

#### Comportamiento de la sincronización inteligente {#intelligent-timing-behavior}

Dado que la [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) se almacena en el componente de mensaje, los retrasos se aplicarán antes de los cálculos de sincronización inteligente. Esto significa que, dependiendo de cuándo un usuario entre en el componente, puede recibir el mensaje más tarde de lo que lo haría en un Canvas creado con el flujo de trabajo de Canvas original.

Supongamos que tu retraso está configurado en 2 días, la sincronización inteligente está activada y ha determinado que la mejor hora para enviar tu mensaje es a las 2 p. m. Un usuario entra en el paso de retraso a las 2:01 p. m.
- **Flujo de trabajo actual:** El retraso tardará 48 horas en completarse, por lo que el usuario recibe el mensaje el tercer día a las 2 p. m.
- **Flujo de trabajo original:** El usuario recibe el mensaje el segundo día a las 2 p. m.

Ten en cuenta que si la sincronización inteligente está activada, el mensaje se enviará dentro de las 24 horas posteriores a que el usuario entre en el componente de mensaje a la hora inteligente identificada (incluso si no hay ningún componente de retraso involucrado).

#### Eventos de excepción {#exception-events}

##### Horas tranquilas {#quiet-hours}

El evento de excepción se aplica mediante Rutas de Acción, que están separadas de los pasos de mensaje. Las horas tranquilas se aplican en el componente de mensaje. Esto significa que si un usuario ya pasó la ruta de acción (y no fue excluido con el evento de excepción), luego se encuentra con las horas tranquilas cuando llega al componente de mensaje y tiene su Canvas configurado de tal manera que el mensaje se reenvía después del periodo de horas tranquilas, el evento de excepción ya no se aplicará. Ten en cuenta que este caso de uso no es común.

Para Segments y filtros, el paso de mensaje tiene validaciones de entrega que permiten a los usuarios configurar Segments y filtros adicionales que se validan en el momento del envío. Esto evita el caso límite de las horas tranquilas mencionado anteriormente.

##### Configuración de programación "en" o "en el próximo" {#in-or-on-the-next-schedule-setting}

Los eventos de excepción se crean mediante Rutas de Acción. Las Rutas de Acción solo admiten "después de una ventana de tiempo X" y no "en X tiempo" o "en el próximo X tiempo".

{% enddetails %}

### ¿Qué debo incluir al enviar un ticket de soporte por un error "Request Timed Out"? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Si encuentras un error "Request Timed Out" al editar un Canvas y necesitas contactar con el [soporte de Braze]({{site.baseurl}}/braze_support), incluye la siguiente información para ayudar a agilizar la resolución:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Entrega y solución de problemas de Canvas {#canvas-delivery-and-troubleshooting}

### ¿Los usuarios huérfanos son elegibles para recibir mensajes de Canvas? {#are-orphaned-users-eligible-to-receive-canvas-messages}

No. Los [usuarios huérfanos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users) no son elegibles para recibir mensajes. Si un perfil queda huérfano mientras un usuario está en un recorrido de Canvas, sale silenciosamente del flujo. Es posible que los análisis no siempre muestren un evento **Exited** para esa salida, y el resumen del flujo de trabajo puede incluir un `partial_update_token` sin `exited_date` ni `exit_reason`.

Para más información sobre fusiones y perfiles huérfanos, consulta [Fusionar usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

### Si detengo un Canvas o una Campaign activa, ¿los mensajes ya enviados al ESP se entregan de todas formas? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Sí. Después de que Braze envía una solicitud a tu proveedor de servicios de correo electrónico (ESP), Braze no puede retirar ese envío. Detener un Canvas o una Campaign evita nuevas solicitudes de envío, pero los mensajes ya transferidos al ESP pueden seguir entregándose e incrementar los conteos de envío a medida que el ESP los procesa.

Este es el mismo comportamiento descrito para [detener un Canvas](#what-happens-when-you-stop-a-canvas): los envíos de correo electrónico en tránsito no se detienen de inmediato.

### ¿Cómo puedo confirmar que un paso webhook de Canvas se ejecutó sin contenido visible para el usuario? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze registra los **envíos** de webhooks y los resultados de entrega relacionados para los pasos de [Webhook]({{site.baseurl}}/user_guide/channels/webhooks) en Campaigns y Canvas. Usa los análisis del paso, los [informes de webhook]({{site.baseurl}}/user_guide/channels/webhooks/reporting), o los eventos de webhook de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para confirmar que el paso se ejecutó. Los registros de solicitudes de tu endpoint proporcionan una confirmación adicional cuando necesitas una prueba de recepción del lado del servidor.

Braze no incluye un píxel de seguimiento invisible incorporado para los pasos de webhook. Confía en las métricas de webhook de Braze y en los registros de tu endpoint en lugar de solicitudes de imagen de un píxel personalizadas.

### ¿Por qué mi paso webhook no tiene campo de cuerpo? {#why-does-my-webhook-step-have-no-body-field}

Los pasos webhook usan un cuerpo de solicitud para `POST`, `PUT`, `PATCH` y `DELETE`. Si cambias el método a `GET`, Braze elimina el campo de cuerpo porque las solicitudes GET no admiten un cuerpo de solicitud. Cambia de nuevo a un método que admita cuerpo si necesitas enviar JSON o datos de formulario. Para más detalles sobre los métodos, consulta [Crear un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method).

### ¿Cómo uso spacer.gif en un paso webhook? {#how-do-i-use-spacergif-in-a-webhook-step}

Braze aloja una imagen de marcador de posición `spacer.gif` en `cdn.braze.com` y `braze-images.com`. Algunos equipos apuntan la URL de un webhook a esta imagen cuando un paso debe ejecutarse sin llamar a un endpoint externo. Los pasos webhook estándar deben llamar a un endpoint real. Usa los [informes de webhook]({{site.baseurl}}/user_guide/channels/webhooks/reporting) y los registros de tu endpoint para confirmar la entrega, como se describe en [¿Cómo puedo confirmar que un paso webhook de Canvas se ejecutó sin contenido visible para el usuario?](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content).

### ¿Por qué mi Canvas no carga con un error "invalid next-step-id"? {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

Este error de consola significa que al menos un paso apunta a un paso siguiente faltante o inválido, por ejemplo, después de una eliminación parcial, clonación o importación. Abre el Canvas en el editor, reconecta los pasos huérfanos o elimina los pasos que ya no tienen una ruta descendente válida. Si el Canvas sigue sin cargar, contacta con el [soporte de Braze]({{site.baseurl}}/braze_support) con el ID del Canvas y una captura de pantalla del error de consola.

### ¿Por qué una marca de tiempo de conversión de Canvas en Currents difiere de mis análisis de Canvas? {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currents registra las conversiones de Canvas como eventos [`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events). El `time` del evento es el momento en que ocurrió el evento de conversión. El campo `conversion_behavior` en ese evento describe la definición de la conversión (tipo y ventana). Los análisis de Canvas también pueden agrupar las conversiones en relación con la entrada al Canvas dentro de la ventana de conversión. Al reconciliar exportaciones, compara el `time` de Currents con la marca de tiempo del evento de conversión y la configuración de la ventana de conversión de tu Canvas.

### ¿Por qué `canvas_step_name` es nulo en Currents? {#why-is-canvas_step_name-null-in-currents}

Los campos de nombre de Campaign y Canvas como `canvas_step_name` pueden ser `null` cuando un evento de Currents se envía antes de que Braze termine de propagar los metadatos del paso, por ejemplo, después de crear o renombrar un paso. Para más detalles, consulta [¿Por qué el nombre de la campaña o el nombre del paso en Canvas es `NULL` en mis datos de Currents?]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data).

### ¿Por qué mi array no se actualiza en un paso de actualización de usuario? {#why-isnt-my-array-updating-in-a-user-update-step}

Revisa el JSON en tu paso de [actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Las actualizaciones de arrays y atributos anidados necesitan rutas y valores válidos para el atributo que estás modificando. No incluyas campos que el paso proporciona automáticamente, como el ID de usuario externo. Usa la pestaña **Preview and test** del paso para confirmar la carga útil antes del lanzamiento.

### ¿Puedo enviar mensajes de Canvas a usuarios sin un `external_id`? {#can-i-send-canvas-messages-to-users-without-an-external_id}

Sí, si ya existe un perfil de usuario en Braze. Los usuarios sin un `external_id` son [usuarios anónimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) y se pueden referenciar con un `braze_id` o un [alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases). Crea o actualiza el perfil con el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) o tu SDK antes de la entrada al Canvas, y luego usa la [entrada basada en acciones o activada por API]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule). La segmentación estándar de Canvas sigue requiriendo un perfil de usuario en Braze: no puedes enviar mensajes de Canvas a una dirección de correo electrónico sola sin perfil.

### ¿Por qué un usuario entró a un Canvas menos veces de las que realizó el evento desencadenante? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Para Canvas basados en acciones y activados por API, Braze deduplica los eventos desencadenantes para que un usuario pueda entrar como máximo **una vez por segundo** aproximadamente para el mismo Canvas. Si un usuario realiza el mismo desencadenante varias veces en un segundo, solo se procesa una entrada.

Para permitir múltiples entradas en el mismo segundo, espacia los eventos desencadenantes al menos 1,1 segundos (por ejemplo, cuando controlas la sincronización de eventos desde tu servidor). Para un comportamiento de tipo Campaign que permita múltiples desencadenantes en el mismo segundo, compara tu caso de uso con [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) con la programación y configuración de re-elegibilidad adecuadas.

### ¿Cuándo se deduplican los usuarios en Canvas activados por API? {#when-are-users-de-duplicated-in-api-triggered-canvases}

Si un usuario reingresa a un Canvas activado por API y llega a un paso de retraso donde ya está en cola por una entrada anterior para un mensaje idéntico, Braze deduplica al usuario para evitar envíos duplicados. La segunda instancia del Canvas sale, por lo que el número de entradas puede exceder el número de envíos.

### ¿Por qué una notificación push de prueba va a la aplicación incorrecta, pero los envíos en vivo se ven correctos? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

**Test push** en un perfil de usuario se entrega a todos los dispositivos con push habilitado para ese perfil. Cuando varias aplicaciones están instaladas en un dispositivo, el sistema operativo normalmente entrega la notificación de prueba a la primera aplicación disponible, que puede no ser la aplicación que deseas validar.

Para confirmar la segmentación específica de la aplicación, envía un mensaje en vivo o de prueba a través de una Campaign o Canvas con una audiencia reducida (por ejemplo, filtra por `external_id`) en lugar de confiar únicamente en **Test push** del perfil.

Para los pasos de mensaje de **Canvas** con varias aplicaciones, activa **Validate audience at message send** en el paso de mensaje para que las verificaciones de Segment y filtros se ejecuten en el momento del envío. Para más información, consulta [Paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

Para el comportamiento general de push de prueba, consulta [Envío de mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) y [Preguntas frecuentes sobre push]({{site.baseurl}}/user_guide/channels/push/faqs).

### ¿Cómo depuro Push Stories en iOS y Android? {#how-do-i-debug-push-stories-on-ios-and-android}

Comienza con [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) para los requisitos de configuración y creativos. Para la implementación y el manejo de notificaciones enriquecidas, consulta [Notificaciones enriquecidas]({{site.baseurl}}/developer_guide/push_notifications/rich) y [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories) en la Guía del desarrollador.

### ¿Quién recibe el correo electrónico "Canvas Messages Delayed 24+ Hours"? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze envía esta notificación cuando los mensajes de Canvas se retrasan por limitación de velocidad durante 24 horas o más. El correo electrónico se envía a los usuarios del panel que previamente realizaron cambios en el Canvas afectado (basándose en los registros de cambios del Canvas). Si Braze no puede determinar esos destinatarios, el correo se envía a los **administradores de la empresa** del espacio de trabajo.

### ¿Cuándo deja un usuario de recibir mensajes después de un evento de excepción? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze registra la salida tan pronto como ocurre el evento de excepción, pero los usuarios pueden permanecer dentro de un paso hasta que los temporizadores finalicen, lo cual es más visible en los pasos de retraso. El comportamiento también difiere entre los pasos programados y los pasos activados por eventos. Para cronogramas, ejemplos y matices de análisis, consulta [Criterios de salida]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

### ¿Por qué mi paso de Rutas de Acción muestra un error cuando selecciono una interacción de alias de enlace? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

Los grupos de acción que usan desencadenantes de interactividad de correo electrónico (por ejemplo, **Click alias in email** o **Clicked alias in any campaign or Canvas step**) necesitan un paso de mensaje que ya haya enviado el mensaje que contiene ese enlace. Añade o reordena los pasos para que el correo electrónico se envíe antes de que el paso de Rutas de Acción evalúe el clic, o elige una interacción que coincida con un mensaje que el usuario ya recibió en este Canvas. Para la lista completa de desencadenantes de interacción, consulta [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

### ¿Cómo afectan las marcas de tiempo históricas de eventos personalizados a los Canvas y Campaigns basados en acciones? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze evalúa los recorridos basados en acciones cuando los eventos que califican se ingieren y el usuario cumple con tus reglas de audiencia. Si un evento llega al perfil fuera de la ventana en que tu Canvas o Campaign estaba activa, o antes de que el usuario coincidiera con tu audiencia, la entrada o los envíos posteriores pueden no ocurrir como se espera. Compara las marcas de tiempo de los eventos con los tiempos de activación y la pertenencia al Segment usando el registro de actividad del perfil de usuario y los pasos de solución de problemas en [Solución de problemas de eventos personalizados]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events). Si el comportamiento sigue sin coincidir con lo esperado, contacta con el [soporte de Braze]({{site.baseurl}}/braze_support).