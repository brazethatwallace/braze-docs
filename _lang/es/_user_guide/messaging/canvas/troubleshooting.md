---
nav_title: Solución de problemas
article_title: Solución de problemas de Canvas
page_order: 7
page_type: reference
description: "Diagnostica problemas de entrada, envío y análisis de Canvas utilizando una ruta de investigación estándar, un índice de síntomas y enlaces al historial de mensajes y al panel de diagnóstico de mensajería."
tool: Canvas
---

# Solución de problemas de Canvas {#troubleshoot-canvases}

> Usa esta página para diagnosticar problemas de entrada, envío y análisis de Canvas. Para definiciones y análisis detallados, consulta las [preguntas frecuentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs).

{% alert note %}
Los registros de **Messaging History** y **Messaging Diagnostics** están disponibles durante un máximo de **30 días** desde el evento. Ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) dentro de ese plazo si necesitas ayuda para investigar un incidente específico.
{% endalert %}

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

| Síntoma | Ir a |
| --- | --- |
| Un usuario no entró en el Canvas | [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas) |
| Un usuario entró pero no recibió un mensaje o paso | [El usuario no recibió un mensaje o paso del Canvas](#user-didnt-receive-a-canvas-message-or-step) |
| Nadie o menos usuarios de los esperados entraron | [Entradas bajas o nulas en Canvas](#low-or-zero-canvas-entries) |
| Los envíos o entregas son menores que la audiencia estimada | [Menos envíos de lo esperado](#lower-sends-than-expected) |
| Los análisis de Canvas parecen incorrectos (grupo de control, conversiones, envíos en cero) | [Discrepancias en los análisis de Canvas](#canvas-analytics-mismatches) |
| Los análisis muestran muchos más envíos que entradas o más salidas que entradas | [El filtrado por rango de fechas puede mostrar números inesperados](#date-range-filtering-can-show-unexpected-numbers) |
| Canvas no se guarda o el editor se congela | [Problemas con el editor y el guardado](#editor-and-save-issues) |
| No se puede eliminar una variante en Canvas | [No se puede eliminar una variante en Canvas debido a un Segment archivado](#cant-delete-a-canvas-variant-because-of-an-archived-segment) |
| Detuve el Canvas pero los mensajes siguieron enviándose | [Comportamiento de un Canvas detenido](#stopped-canvas-behavior) |
| Error "Demasiadas ramas de Canvas" al lanzar | [Error "Demasiadas ramas de Canvas"](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de Canvas" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo para investigar un usuario específico o un problema de envío agregado. Comienza en el paso 1 para cada incidente.

1. Confirma que el Canvas está activo (no en borrador, detenido ni archivado).
2. Confirma que la programación de entrada (ventana programada, zona horaria, desencadenante basado en acciones o entrada activada por API) coincide con el momento en que esperas que los usuarios entren.
3. Revisa el registro de mensajería de un usuario yendo a **Audiencia** > **Buscar usuarios**, abriendo el perfil y seleccionando **Historial de mensajes** (últimos 30 días).
   - Si no existe ningún registro para el momento de envío esperado, el problema está en la entrada, no en el mensaje. Ve a [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas).
4. Revisa el **Registro de cambios** del Canvas y los registros de cambios de cualquier Segment utilizado en la segmentación. Confirma que la audiencia, los pasos o la configuración de envío no se hayan modificado durante el incidente.
5. Revisa los resultados agregados en la página de análisis del Canvas abriendo el [panel de Diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) y revisando los motivos de cancelación y descarte.
   - Si ves un resultado que no reconoces, consulta [Resultados de cancelación]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes) en la documentación de diagnóstico.
   - Si un paso muestra cero entradas (no cero envíos), revisa el tipo de paso anterior ([Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) o [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)).
6. Si aún no puedes avanzar, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) dentro de los 30 días con el ID del Canvas, los ID de los usuarios afectados, las marcas de tiempo (con zona horaria) y capturas de pantalla del historial de mensajes o del diagnóstico de mensajería.

Antes del lanzamiento, usa [Enviar Canvas de prueba]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) y [Vista previa de rutas de usuario]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para validar tu configuración.

## El usuario no entró en el Canvas {#user-didnt-enter-the-canvas}

**Síntoma:** Un usuario no entró en el Canvas cuando esperabas que lo hiciera, o entraron menos usuarios de lo que sugieren tus eventos desencadenantes.

Los usuarios deben coincidir con el **Público objetivo** antes de que Braze evalúe el desencadenante de entrada (excepto para los desencadenantes de [cambio en atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Un desencadenante por sí solo no garantiza la entrada si el usuario no estaba en la audiencia en el momento de la evaluación.

La reelegibilidad y la reentrada son controles separados en [Selección de controles de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls):

- **Reelegibilidad:** Determina si un usuario puede volver a entrar en el Canvas después de salir (ventana de tiempo y configuración de **Permitir a los usuarios volver a entrar en Canvas**).
- **Reentrada:** Determina si un usuario que está actualmente dentro del Canvas puede entrar en una ruta concurrente.

Un usuario puede ser reelegible pero estar bloqueado porque todavía está en el Canvas, o puede haber salido pero aún estar fuera de la ventana de reelegibilidad. Verifica ambas configuraciones cuando un usuario no vuelve a entrar en un Canvas.

Verifica lo siguiente:

- **Horario de entrada y zona horaria:** Confirma que el Canvas estaba activo y que el usuario realizó el desencadenante durante la [ventana de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
- **Público objetivo en el momento de la evaluación:** Revisa los registros de cambios de Segments y filtros. [Búsqueda de usuarios]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) puede mostrar un falso positivo para algunos tipos de filtro (por ejemplo, atributos de fecha con formato de cadena).
- **Límites de entrada:** Es posible que se hayan alcanzado las [entradas máximas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) o los límites de audiencia.
- **Grupo de control global:** Los usuarios en el [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group) no entran en Canvas de mensajería.
- **Grupo de control de Canvas:** Los usuarios asignados al grupo de control de Canvas en la entrada no reciben mensajes de variante. La asignación de variante ocurre en la entrada, no a través de filtros de Segment. Consulta [Discrepancias en los análisis de Canvas](#canvas-analytics-mismatches).
- **Criterios de salida:** Es posible que el usuario haya coincidido con los [criterios de salida]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) antes o durante la entrada. Si la entrada y la salida usan el mismo evento, consulta [Coincidencia de criterios de entrada y salida]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
- **Entrada activada por API:** Confirma que el usuario fue añadido con el [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Puedes [crear un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) con un filtro de entrada de Canvas y exportar usuarios con [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### El recuento de eventos desencadenantes es mayor que las entradas en Canvas {#trigger-event-count-is-higher-than-canvas-entries}

**Síntoma:** El volumen de eventos desencadenantes es mayor que el recuento de entradas en Canvas.

Braze deduplica múltiples intentos de entrada que ocurren en el mismo instante, por lo que puedes ver menos entradas en Canvas que eventos desencadenantes. Para probar múltiples entradas, espacia los eventos desencadenantes con al menos un segundo de diferencia.

Si un usuario realiza el mismo desencadenante varias veces en un segundo, Braze procesa solo una entrada. Revisa los diagnósticos de mensajería para resultados como **El usuario no es reelegible** cuando se aplican reglas de reentrada o reelegibilidad.

{% details Horario de verano y Canvas programados diariamente %}

En los días de transición del horario de verano (DST), los Canvas programados diariamente pueden ejecutarse hasta una hora antes o después de lo habitual. Si tus criterios de entrada dependen de atributos personalizados o eventos con marcas de tiempo que caen dentro de una hora del horario de entrada programado, es posible que los usuarios aún no califiquen en el día del DST porque el atributo o evento no se ha registrado.

Por ejemplo, supón que los usuarios normalmente reciben una actualización de atributo personalizado a las 3 p. m. en la zona horaria de tu Canvas y tu Canvas se ejecuta diariamente a las 3:30 p. m. en esa misma zona horaria. En un día de DST con adelanto de reloj, el Canvas puede evaluar a los usuarios hasta una hora antes de lo habitual en relación con esa actualización de atributo, antes de que el atributo se haya registrado. Si la reelegibilidad está desactivada, los usuarios que entraron en días anteriores no pueden volver a entrar, lo que resulta en cero entradas para ese día.

Para evitar esto, asegúrate de que las actualizaciones de atributos personalizados o eventos ocurran más de una hora antes del horario de entrada programado del Canvas.

{% enddetails %}

## El usuario no recibió un mensaje o paso en Canvas {#user-didnt-receive-a-canvas-message-or-step}

**Síntoma:** Un usuario entró en el Canvas pero no recibió el mensaje o paso esperado.

Comprueba el [**historial de mensajes**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) del usuario para el paso en Canvas y la marca de tiempo. Si no existe ningún registro, vuelve a [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas).

A continuación, comprueba lo siguiente según el desencadenante o tipo de paso:

- **Desencadenantes de eventos personalizados o compras:** Confirma que el evento aparece en **Analytics** > **Custom Events Report** (o **Revenue** para compras). Compara la marca de tiempo del evento con el momento en que el Canvas se activó y con cualquier retraso programado en el paso.
- **Entrada activada por API:** Confirma la entrada con un filtro de Segment del Canvas y una exportación, como se describe en [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas).
- **Desencadenantes de Rutas de Acción o pasos de mensaje:** Confirma que el usuario realizó el evento previo requerido y que las [propiedades del evento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties) están disponibles en el paso.
- **Pasos de mensajes dentro de la aplicación:** Los mensajes dentro de la aplicación se envían en el siguiente inicio de sesión después de que el usuario entra en el paso, y solo a partir de eventos del SDK (no desde la REST API). Consulta [¿Cuándo se envían los mensajes dentro de la aplicación en Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) en las preguntas frecuentes de Canvas.
- **Grupo de control del Canvas:** Verifica que el usuario no fue asignado al grupo de control del Canvas al momento de la entrada.
- **Elegibilidad de canal y configuración de envío:** Confirma el estado de suscripción, el estado de push habilitado y la [Configuración de envío]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) de cada paso (por ejemplo, **Subscription Settings** configurado solo para usuarios que han optado por participar). No añadas filtros de un solo canal a **Target Audience** en Canvas multicanal.
- **Validaciones de entrega:** Si has habilitado **Validate audience at message send** en un paso de mensaje, los usuarios que ya no coinciden con los filtros en el momento del envío no reciben el mensaje. Consulta [Validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Horas tranquilas, sincronización inteligente, límites de frecuencia y límites de velocidad:** Estos pueden diferir, suprimir o cancelar envíos. Los usuarios pueden permanecer en el Canvas después de una cancelación por horas tranquilas.
- **Condiciones de carrera:** Si el usuario desencadenó varias acciones a la vez, consulta [Condiciones de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert important %}
Cuando un paso de mensaje en Canvas cancela un envío, el usuario aún avanza al siguiente paso. Canvas avanza tras una cancelación para que los pasos posteriores de retraso y Rutas de Acción no queden bloqueados permanentemente. Consulta [Cómo avanzan los usuarios]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) y [Resultados de cancelación]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes).
{% endalert %}

Para filtros a nivel de paso, conflictos entre ramas y comportamiento de ramificación de mensajes dentro de la aplicación, consulta [Lanzar con Canvas Flow — Solución de problemas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) y las [preguntas frecuentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery).

{% alert important %}
Si tu Canvas basado en acciones envía mensajes antes de lo esperado, comprueba que la marca de tiempo de tu evento personalizado utilice la hora actual y no una hora retroactiva. Braze evalúa los retrasos a partir de la marca de tiempo enviada con el evento. Consulta [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
{% endalert %}

## Entradas de Canvas bajas o nulas {#low-or-zero-canvas-entries}

**Síntoma:** Ningún usuario o menos usuarios de los esperados entraron en el Canvas.

Empieza con la [lista de verificación de lanzamiento con Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist) y luego confirma:

- El Canvas está activo y la hora actual se encuentra dentro de la ventana de entrada programada.
- Los [ajustes de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) (reelegibilidad, entradas máximas y límites de entrada) permiten que los usuarios que esperas puedan entrar.
- El público objetivo y los filtros de Segment siguen coincidiendo con los usuarios que esperas después del lanzamiento.
- Los porcentajes del grupo de control global y del grupo de control de Canvas muestran qué proporción de usuarios entra en cada ruta frente a los que reciben mensajes.
- Se espera que los límites de velocidad del espacio de trabajo o las colas de entrada añadan retrasos entre el momento en que los usuarios califican y el momento en que entran o avanzan a un paso.

Para un solo usuario, sigue la [ruta de investigación estándar](#standard-investigation-path). Para entradas nulas relacionadas con el horario de verano, consulta la sección desplegable en [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas).

## Envíos más bajos de lo esperado {#lower-sends-than-expected}

**Síntoma:** Los envíos o entregas son inferiores a la audiencia estimada en un paso en Canvas.

Las causas comunes incluyen la reevaluación de la audiencia en el momento del envío, la elegibilidad del canal, los grupos de control, las horas tranquilas, la sincronización inteligente, los límites de velocidad y el comportamiento de entrega de los mensajes dentro de la aplicación (cero _envíos_ con impresiones es lo esperado para los mensajes dentro de la aplicación).

Si un paso de mensaje muestra que muchos usuarios entraron pero hay pocos envíos, verifica si `abort_message()` de Liquid canceló el envío. Para verificaciones del registro de actividad de mensajes, atributos faltantes y envíos de prueba, consulta [Solución de problemas de tasas de cancelación altas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates).

Para una lista detallada, consulta [¿Por qué los envíos son inferiores al tamaño de audiencia estimado?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) en las preguntas frecuentes de Canvas y [¿Por qué los envíos son inferiores al tamaño de audiencia estimado?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size) para Campaigns.

Usa el [panel de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) para ver los motivos de cancelación y descarte a nivel de paso.

## Discrepancias en los análisis de Canvas {#canvas-analytics-mismatches}

**Síntoma:** Los análisis de Canvas se ven incorrectos (divisiones del grupo de control, conversiones o cero envíos).

La asignación al grupo de control y a las variantes ocurre en la entrada al Canvas según los porcentajes que configuras en el constructor, no a través de filtros de Segment. Los usuarios que no pueden recibir un canal específico pueden seguir entrando a una variante; usa la [Configuración de envío]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) a nivel de paso para limitar quién recibe cada tipo de mensaje, en lugar de restringir el **Público objetivo** con filtros de canal.

Distingue el grupo de control de Canvas del [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group). Para definiciones de filtros, consulta [¿Cuál es la diferencia entre "No ha entrado en variante de Canvas" y "No está en grupo de control de Canvas"?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group) en las preguntas frecuentes de Canvas.

{% details Por qué los envíos de una variante pueden ser menores que el porcentaje de la variante %}

Imaginemos el siguiente escenario:

- Un Canvas tiene una sola variante y un grupo de control.
- El primer paso de la variante es una notificación push.
- El 90 % de los usuarios fueron seleccionados para entrar en la variante y el 10 % para entrar en el grupo de control.

![Ejemplo de Canvas con 90 % de variante y 10 % de grupo de control.]({% image_buster /assets/img_archive/trouble15.png %})

En este escenario, el 90 % de los usuarios que entran al Canvas ingresan a la variante.

Cuando miras el Segment de usuarios activos, verás que, aunque contiene 29,8 k usuarios, solo el 64 % de ellos tienen push habilitado:

![Segment con el filtro "Push habilitado" configurado en "verdadero" y un estimado de 29,8 k usuarios.]({% image_buster /assets/img_archive/trouble16.png %})

Esto significa que, aunque especificaste que el 90 % de los usuarios entraran en la variante, no todos pueden recibir una notificación push. Los usuarios que no pueden recibir push siguen entrando en la variante de todos modos: el recuento de envíos refleja la elegibilidad del canal en el paso, no la asignación de variante en la entrada.

{% enddetails %}

### El filtrado por rango de fechas puede mostrar números inesperados {#date-range-filtering-can-show-unexpected-numbers}

**Síntoma:** Los análisis de Canvas o de pasos muestran números inesperados o improbables, como muchos más envíos que entradas, o más usuarios saliendo de un paso que los que entraron.

Esto puede ocurrir cuando usas el filtro de calendario de rango de fechas en la parte superior de la página de análisis de Canvas. Si seleccionas un rango de fechas que excluye algunas acciones de los usuarios, las métricas mostradas pueden reflejar solo una parte del recorrido de cada usuario.

Por ejemplo:
- Podrías ver 100 entradas con 8000 envíos si tu rango de fechas comienza después de que la mayoría de los usuarios entraron, pero incluye el momento en que recibieron mensajes.
- Podrías ver más usuarios avanzando al siguiente paso de los que entraron al paso anterior, si tu rango solo captura las salidas pero no las entradas previas.

Para resolver esto, ajusta el rango de fechas para incluir todas las fechas desde que se lanzó el Canvas hasta el presente, o selecciona un rango que cubra el periodo completo relevante para las métricas que necesitas.

Para definiciones de tasa de conversión y análisis a nivel de paso, consulta [Análisis y conversiones]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions) en las preguntas frecuentes de Canvas.

## Problemas del editor y guardado {#editor-and-save-issues}

**Síntoma:** El editor de Canvas no carga, se congela o no guarda los cambios.

| Síntoma | Causa más probable |
| --- | --- |
| El botón Guardar gira indefinidamente sin error | Filtro de atributo personalizado vacío o incompleto en la audiencia del Canvas o en un filtro de paso: elimina el filtro o selecciona un atributo válido |
| Error "Request Timed Out" al editar | Interferencia de extensiones del navegador, bloqueadores de anuncios o sesión obsoleta: prueba en una ventana de incógnito o en otro navegador |
| No se puede guardar después de archivar una variante | Una variante archivada sigue siendo referenciada aguas abajo; revisa las conexiones de los pasos y restaura o reemplaza la variante |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma del editor" }

Si el editor se congela en un Canvas grande o complejo, prueba lo siguiente:

- Borra la caché y las cookies del navegador y, a continuación, recarga la página. Los bloqueadores de anuncios de la empresa o las extensiones del navegador pueden interferir con la plataforma de Braze.
- Usa los controles de zoom del Canvas para reducir la vista al 25 % o al 10 % y disminuir la cantidad de interfaz que el navegador debe renderizar.
- Prueba con un navegador web diferente.

Si el Canvas no carga y no avanza, es posible que una versión anterior no se haya guardado correctamente y contenga pasos no válidos. Duplica el Canvas desde el panel. Si el problema persiste, abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

Para los tickets de soporte de "Request Timed Out", incluye una grabación de pantalla, marca de tiempo y zona horaria, navegador y versión, pasos para reproducir el problema y, opcionalmente, un registro HAR de las herramientas de desarrollador de tu navegador. Consulta [¿Qué debo incluir al enviar un ticket de soporte por un error "Request Timed Out"?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error) en las preguntas frecuentes de Canvas.

{% multi_lang_include audience/segments.md section='Canvas variant archived segment' %}

## Comportamiento de Canvas detenido {#stopped-canvas-behavior}

**Síntoma:** Detuviste el Canvas, pero los usuarios siguieron recibiendo mensajes.

Cuando detienes un Canvas, los usuarios no pueden entrar y no se envían más mensajes desde el flujo de Canvas. Los envíos de correo electrónico que ya se entregaron a tu proveedor de servicios de correo electrónico no se pueden recuperar.

Los usuarios que esperan en un paso de Retraso o Ruta de Acción no se eliminan automáticamente del recorrido cuando detienes el Canvas. Si vuelves a habilitar el Canvas antes de que pase su hora de envío programada, es posible que aún reciban los pasos pendientes.

Para obtener todos los detalles, consulta [¿Qué sucede cuando detienes un Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) en las preguntas frecuentes de Canvas.

## Error "Demasiadas ramas en Canvas" {#too-many-canvas-branches-error}

**Síntoma:** Ves un error "Too many Canvas branches" al lanzar un Canvas programado.

Este error aparece cuando la combinación de ramificación de pasos y el tamaño del público de entrada puede crear problemas de rendimiento del clúster que impiden el envío de mensajes. Braze muestra este mensaje cuando lanzas un Canvas con una entrada programada; no aparecerá cuando guardes un borrador.

Para resolverlo:

- Reduce la ramificación de pasos en el Canvas.
- Reduce el tamaño del público de entrada.
- Usa [Rutas de Audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) para consolidar la ramificación en lugar de muchas rutas paralelas.
- Si tu Canvas usa el editor original, [clónalo a Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) y reconstrúyelo con componentes de Canvas.

Si aún necesitas lanzar el Canvas sin cambios y no puedes migrar a Canvas Flow, contacta con [soporte de Braze]({{site.baseurl}}/support_contact).

## Cuándo contactar a soporte {#when-to-contact-support}

Contacta a [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) en un plazo de 30 días desde que ocurrió el problema si has completado la [ruta de investigación estándar](#standard-investigation-path) y aún necesitas ayuda.

Incluye:

- ID de Canvas e IDs de los usuarios afectados (ID externo o ID de Braze)
- Marcas de tiempo con zona horaria
- Capturas de pantalla o exportaciones del **historial de mensajes** o de **Diagnósticos de mensajería**
- Para errores de "Request Timed Out" en el editor, los detalles indicados en [Problemas del editor y de guardado](#editor-and-save-issues)