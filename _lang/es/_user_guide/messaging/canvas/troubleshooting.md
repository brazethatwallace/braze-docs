---
nav_title: Solución de problemas
article_title: Solución de problemas de Canvas
page_order: 7
page_type: reference
description: "Diagnostica problemas de entrada, envío y análisis de Canvas utilizando una ruta de investigación estándar, un índice de síntomas y enlaces al historial de mensajes y al dashboard de diagnóstico de mensajería."
tool: Canvas
---

# Solución de problemas de Canvas {#troubleshoot-canvases}

> Usa esta página para diagnosticar problemas de entrada, envío y análisis de Canvas. Para definiciones y análisis detallados, consulta las [preguntas frecuentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs).

{% alert note %}
Los registros de **Messaging History** y **Messaging Diagnostics** están disponibles durante un máximo de **30 días** desde el evento. Ponte en contacto con [soporte de Braze]({{site.baseurl}}/braze_support) dentro de ese plazo si necesitas ayuda para investigar un incidente específico.
{% endalert %}

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

| Síntoma | Ir a |
| --- | --- |
| Un usuario no entró en el Canvas | [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas) |
| Un usuario entró pero no recibió un mensaje o paso | [El usuario no recibió un mensaje o paso en Canvas](#user-didnt-receive-a-canvas-message-or-step) |
| Nadie o menos usuarios de los esperados entraron | [Entradas bajas o nulas en Canvas](#low-or-zero-canvas-entries) |
| Los envíos o entregas son inferiores a la audiencia estimada | [Menos envíos de los esperados](#lower-sends-than-expected) |
| Los análisis de Canvas parecen incorrectos (grupo de control, conversiones, cero envíos) | [Discrepancias en los análisis de Canvas](#canvas-analytics-mismatches) |
| Los análisis muestran muchos más envíos que entradas o más salidas que entradas | [El filtrado por rango de fechas puede mostrar números inesperados](#date-range-filtering-can-show-unexpected-numbers) |
| El Canvas no se guarda o el editor se congela | [Problemas con el editor y el guardado](#editor-and-save-issues) |
| Detuve el Canvas pero los mensajes siguieron enviándose | [Comportamiento de Canvas detenido](#stopped-canvas-behavior) |
| Error «Too many Canvas branches» al lanzar | [Error «Too many Canvas branches»](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de Canvas" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo para investigar un usuario específico o un problema de envío agregado. Comienza en el paso 1 para cada incidente.

1. Confirma que el Canvas está activo (no en borrador, detenido ni archivado).
2. Confirma que la programación de entrada (ventana programada, zona horaria, desencadenante basado en acciones o entrada activada por API) coincide con el momento en que esperas que los usuarios entren.
3. Revisa el registro de mensajería de un usuario yendo a **Audiencia** > **Buscar usuarios**, abriendo el perfil y seleccionando **Historial de mensajes** (últimos 30 días).
   - Si no existe ningún registro para la hora de envío esperada, el problema está en la entrada, no en el mensaje. Ve a [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas).
4. Revisa el **Registro de cambios** del Canvas y los registros de cambios de cualquier Segment utilizado en la segmentación. Confirma que la audiencia, los pasos o la configuración de envío no se modificaron durante el incidente.
5. Revisa los resultados agregados en la página de análisis del Canvas abriendo el [panel de Diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) y revisando las razones de cancelación y descarte.
   - Si ves un resultado que no reconoces, consulta [Resultados de cancelación]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes) en la documentación de diagnóstico.
   - Si un paso muestra cero entradas (no cero envíos), revisa el tipo de paso anterior ([Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) o [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)).
6. Si sigues bloqueado, contacta con [soporte de Braze]({{site.baseurl}}/braze_support) dentro de los 30 días con el ID del Canvas, los ID de los usuarios afectados, las marcas de tiempo (con zona horaria) y capturas de pantalla del historial de mensajes o del diagnóstico de mensajería.

Antes de lanzar, usa [Enviar Canvas de prueba]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) y [Vista previa de rutas de usuario]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para validar tu configuración.

## El usuario no entró en el Canvas {#user-didnt-enter-the-canvas}

**Síntoma:** Un usuario no entró en el Canvas cuando esperabas que lo hiciera, o entraron menos usuarios de lo que sugieren tus eventos desencadenantes.

Los usuarios deben coincidir con el **público objetivo** antes de que Braze evalúe el desencadenante de entrada (excepto para los desencadenantes de [cambio en atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Un desencadenante por sí solo no garantiza la entrada si el usuario no estaba en la audiencia en el momento de la evaluación.

La reelegibilidad y la reentrada son controles separados en [Seleccionar controles de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls):

- **Reelegibilidad:** Determina si un usuario puede volver a entrar en el Canvas después de salir (ventana de tiempo y configuración de **Permitir a los usuarios volver a entrar en el Canvas**).
- **Reentrada:** Determina si un usuario que está actualmente dentro del Canvas puede entrar en una ruta concurrente.

Un usuario puede ser reelegible pero estar bloqueado porque todavía está en el Canvas, o puede haber salido pero aún estar fuera de la ventana de reelegibilidad. Verifica ambas configuraciones cuando un usuario no vuelve a entrar en un Canvas.

Verifica lo siguiente:

- **Programación de entrada y zona horaria:** Confirma que el Canvas estaba activo y que el usuario realizó el desencadenante durante la [ventana de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
- **Público objetivo en el momento de la evaluación:** Revisa los registros de cambios de Segments y filtros. [Búsqueda de usuarios]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) puede mostrar un falso positivo para algunos tipos de filtros (por ejemplo, atributos de fecha con formato de cadena).
- **Límites de entrada:** Es posible que se hayan alcanzado las [entradas máximas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) o los límites de audiencia.
- **Grupo de control global:** Los usuarios en el [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group) no entran en Canvas de mensajería.
- **Grupo de control del Canvas:** Los usuarios asignados al grupo de control del Canvas en la entrada no reciben mensajes de variante. La asignación de variantes ocurre en la entrada, no a través de filtros de Segments. Consulta [Discrepancias en los análisis de Canvas](#canvas-analytics-mismatches).
- **Criterios de salida:** Es posible que el usuario haya coincidido con los [criterios de salida]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) antes o durante la entrada. Si la entrada y la salida usan el mismo evento, consulta [Coincidencia de criterios de entrada y salida]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
- **Entrada activada por API:** Confirma que el usuario fue añadido con el [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Puedes [crear un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) con un filtro de entrada de Canvas y exportar usuarios con [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### El recuento de eventos desencadenantes es mayor que las entradas al Canvas {#trigger-event-count-is-higher-than-canvas-entries}

**Síntoma:** El volumen de eventos desencadenantes es mayor que el recuento de entradas al Canvas.

Braze deduplica múltiples intentos de entrada que ocurren en el mismo instante, por lo que puedes ver menos entradas al Canvas que eventos desencadenantes. Para probar múltiples entradas, espacia los eventos desencadenantes al menos un segundo entre sí.

Si un usuario realiza el mismo desencadenante varias veces en un segundo, Braze procesa solo una entrada. Verifica los Diagnósticos de mensajería para resultados como **Usuario no reelegible** cuando se aplican reglas de reentrada o reelegibilidad.

{% details Horario de verano y Canvas programados diariamente %}

En los días de transición del horario de verano (DST), los Canvas programados diariamente pueden ejecutarse hasta una hora antes o después de lo habitual. Si tus criterios de entrada dependen de atributos personalizados o eventos con marcas de tiempo que caen dentro de una hora del horario de entrada programado, es posible que los usuarios aún no califiquen en el día del DST porque el atributo o evento no se ha registrado.

Por ejemplo, supón que los usuarios normalmente reciben una actualización de atributo personalizado a las 3 pm en la zona horaria de tu Canvas y tu Canvas se ejecuta diariamente a las 3:30 pm en esa misma zona horaria. En un día de adelanto de reloj por DST, el Canvas puede evaluar a los usuarios hasta una hora antes de lo habitual en relación con esa actualización de atributo, antes de que el atributo se haya registrado. Si la reelegibilidad está desactivada, los usuarios que entraron en días anteriores no pueden volver a entrar, lo que resulta en cero entradas para ese día.

Para evitar esto, asegúrate de que las actualizaciones de tus atributos personalizados o eventos ocurran más de una hora antes del horario de entrada programado del Canvas.

{% enddetails %}

## El usuario no recibió un mensaje o paso de Canvas {#user-didnt-receive-a-canvas-message-or-step}

**Síntoma:** Un usuario entró en el Canvas pero no recibió el mensaje o paso esperado.

Consulta el [**historial de mensajes**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) del usuario para el paso de Canvas y la marca de tiempo. Si no existe ningún registro, vuelve a [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas).

Luego verifica lo siguiente según el tipo de desencadenador o paso:

- **Desencadenadores de eventos personalizados o compras:** Confirma que el evento aparece en **Analytics** > **Informe de eventos personalizados** (o **Ingresos** para compras). Compara la marca de tiempo del evento con el momento en que el Canvas se activó y con cualquier retraso programado en el paso.
- **Entrada desencadenada por API:** Confirma la entrada con un filtro de Segment de Canvas y una exportación, como se describe en [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas).
- **Rutas de Acción o desencadenadores de pasos de mensaje:** Confirma que el usuario realizó el evento previo y que las [propiedades del evento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties) están disponibles en el paso.
- **Pasos de mensajes dentro de la aplicación:** Los mensajes dentro de la aplicación se envían en el siguiente inicio de sesión después de que el usuario entra en el paso, y solo a partir de eventos del SDK (no de la REST API). Consulta [¿Cuándo se envían los mensajes dentro de la aplicación en Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) en las preguntas frecuentes de Canvas.
- **Grupo de control de Canvas:** Verifica que el usuario no fue asignado al grupo de control de Canvas en la entrada.
- **Elegibilidad de canal y configuración de envío:** Confirma el estado de suscripción, el estado de push habilitado y la [configuración de envío]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) por paso (por ejemplo, **Configuración de suscripción** establecida solo para usuarios que han optado por participar). No añadas filtros de un solo canal al **público objetivo** en Canvas multicanal.
- **Validaciones de entrega:** Si has habilitado **Validar audiencia en el envío del mensaje** en un paso de mensaje, los usuarios que ya no coincidan con los filtros en el momento del envío no recibirán el mensaje. Consulta [Validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Horas tranquilas, sincronización inteligente, límites de frecuencia y límites de velocidad:** Estos pueden diferir, suprimir o cancelar envíos. Los usuarios pueden permanecer en el Canvas después de una cancelación por horas tranquilas.
- **Condiciones de carrera:** Si el usuario desencadenó múltiples acciones a la vez, consulta [Condiciones de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert important %}
Cuando un paso de mensaje de Canvas cancela un envío, el usuario aún avanza al siguiente paso. Canvas avanza tras la cancelación para que los pasos posteriores de retraso y Rutas de Acción no queden bloqueados permanentemente. Consulta [Cómo avanzan los usuarios]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) y [Resultados de cancelación]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes).
{% endalert %}

Para filtros a nivel de paso, conflictos entre ramas y comportamiento de ramificación de IAM, consulta [Lanzar con Canvas Flow — Solución de problemas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) y las [preguntas frecuentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery).

{% alert important %}
Si tu Canvas basado en acciones envía mensajes antes de lo esperado, verifica que la marca de tiempo de tu evento personalizado use la hora actual, no una hora anterior. Braze evalúa los retrasos a partir de la marca de tiempo enviada con el evento. Consulta [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
{% endalert %}

## Entradas bajas o nulas en Canvas {#low-or-zero-canvas-entries}

**Síntoma:** Ningún usuario o menos usuarios de los esperados entraron en el Canvas.

Comienza con la [lista de verificación de lanzamiento con Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist) y luego confirma:

- El Canvas está activo y la hora actual se encuentra dentro de la ventana de entrada programada.
- La [configuración de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) (reelegibilidad, entradas máximas y límites de entrada) permite que los usuarios que esperas puedan entrar.
- El público objetivo y los filtros de Segment siguen coincidiendo con los usuarios que esperas después del lanzamiento.
- Los porcentajes del grupo de control global y de Canvas muestran qué proporción de usuarios entra en cada ruta frente a los que reciben mensajes.
- Se espera que los límites de velocidad del espacio de trabajo o las colas de entrada añadan retrasos entre el momento en que los usuarios califican y el momento en que entran o avanzan a un paso.

Para un solo usuario, sigue la [ruta de investigación estándar](#standard-investigation-path). Para entradas nulas relacionadas con el horario de verano (DST), consulta la sección desplegable en [El usuario no entró en el Canvas](#user-didnt-enter-the-canvas).

## Envíos menores de lo esperado {#lower-sends-than-expected}

**Síntoma:** Los envíos o entregas son menores que la audiencia estimada en un paso en Canvas.

Las causas comunes incluyen la reevaluación de la audiencia en el momento del envío, la elegibilidad del canal, los grupos de control, las horas tranquilas, la sincronización inteligente, los límites de velocidad y el comportamiento de entrega de los mensajes dentro de la aplicación (cero _Envíos_ con impresiones es lo esperado para los mensajes dentro de la aplicación).

Si un paso de Mensaje muestra que muchos usuarios entraron pero hay pocos envíos, comprueba si `abort_message()` de Liquid canceló el envío. Para verificaciones del registro de actividad de mensajes, atributos faltantes y envíos de prueba, consulta [Solución de problemas de tasas de cancelación altas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates).

Para una lista detallada, consulta [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) en las preguntas frecuentes de Canvas y [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size) para Campaigns.

Usa el [panel de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) para ver los motivos de cancelación y descarte a nivel de paso.

## Discrepancias en los análisis de Canvas {#canvas-analytics-mismatches}

**Síntoma:** Los análisis de Canvas parecen incorrectos (divisiones del grupo de control, conversiones o cero envíos).

La asignación del grupo de control y la variante ocurre en la entrada al Canvas según los porcentajes que configuras en el constructor, no a través de filtros de Segment. Los usuarios que no pueden recibir un canal específico aún pueden entrar en una variante; usa la [Configuración de envío]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) por paso para limitar quién recibe cada tipo de mensaje en lugar de restringir el **Público objetivo** con filtros de canal.

Distingue el grupo de control de Canvas del [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group). Para definiciones de filtros, consulta [¿Cuál es la diferencia entre «No ha entrado en la variante de Canvas» y «No está en el grupo de control de Canvas»?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group) en las preguntas frecuentes de Canvas.

{% details Por qué los envíos de una variante pueden ser menores que el porcentaje de la variante %}

Imaginemos el siguiente escenario:

- Un Canvas tiene una sola variante y un grupo de control.
- El primer paso de la variante es una notificación push.
- El 90 % de los usuarios fueron seleccionados para entrar en la variante y el 10 % para entrar en el grupo de control.

![Ejemplo de Canvas con 90 % de variante y 10 % de grupo de control.]({% image_buster /assets/img_archive/trouble15.png %})

En este escenario, el 90 % de los usuarios que entran al Canvas ingresan a la variante.

Cuando observas el Segment de usuarios activos, verás que aunque contiene 29,8 k usuarios, solo el 64 % de ellos tienen push habilitado:

![Segment con el filtro «Push habilitado» configurado en «verdadero» y un estimado de 29,8 k usuarios.]({% image_buster /assets/img_archive/trouble16.png %})

Esto significa que, aunque especificaste que el 90 % de los usuarios entraran en la variante, no todos pueden recibir una notificación push. Los usuarios que no pueden recibir push aún entran en la variante de todos modos: el recuento de envíos refleja la elegibilidad del canal en el paso, no la asignación de variante en la entrada.

{% enddetails %}

### El filtrado por rango de fechas puede mostrar números inesperados {#date-range-filtering-can-show-unexpected-numbers}

**Síntoma:** Los análisis de Canvas o de un paso muestran números inesperados o improbables, como muchos más envíos que entradas, o más usuarios saliendo de un paso de los que entraron.

Esto puede ocurrir cuando usas el filtro de calendario de rango de fechas en la parte superior de la página de análisis de Canvas. Si seleccionas un rango de fechas que excluye algunas acciones de los usuarios, las métricas mostradas pueden reflejar solo una parte del recorrido de cada usuario.

Por ejemplo:
- Puedes ver 100 entradas con 8000 envíos si tu rango de fechas comienza después de que la mayoría de los usuarios entraron, pero incluye el momento en que recibieron los mensajes.
- Puedes ver más usuarios avanzando al siguiente paso de los que entraron en el paso anterior si tu rango solo captura las salidas pero no las entradas anteriores.

Para resolver esto, ajusta el rango de fechas para incluir todas las fechas desde que se lanzó el Canvas hasta el presente, o selecciona un rango que cubra el período de tiempo completo relevante para las métricas que necesitas.

Para definiciones de tasas de conversión y análisis a nivel de paso, consulta [Análisis y conversiones]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions) en las preguntas frecuentes de Canvas.

## Problemas del editor y al guardar {#editor-and-save-issues}

**Síntoma:** El editor de Canvas no carga, se congela o no guarda tus cambios.

| Síntoma | Causa más probable |
| --- | --- |
| El botón de guardar gira indefinidamente sin error | Filtro de atributo personalizado vacío o incompleto en la audiencia del Canvas o en un filtro de paso: elimina el filtro o selecciona un atributo válido |
| Error "Request Timed Out" al editar | Interferencia de extensiones del navegador, bloqueadores de anuncios o una sesión obsoleta: prueba en una ventana de incógnito o en otro navegador |
| No se puede guardar después de archivar una variante | Una variante archivada todavía está referenciada más adelante; revisa las conexiones de los pasos y restaura o reemplaza la variante |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma del editor" }

Si el editor se congela en un Canvas grande o complejo, prueba lo siguiente:

- Borra la caché y las cookies del navegador y luego recarga la página. Los bloqueadores de anuncios corporativos o las extensiones del navegador pueden interferir con la plataforma Braze.
- Usa los controles de zoom de Canvas para reducir la vista al 25 % o al 10 % y disminuir la cantidad de interfaz que el navegador debe renderizar.
- Prueba con un navegador web diferente.

Si el Canvas no carga y no avanza, es posible que una versión anterior no se haya guardado correctamente y contenga pasos no válidos. Duplica el Canvas desde el panel. Si el problema persiste, abre un [ticket de soporte]({{site.baseurl}}/braze_support).

Para tickets de soporte por "Request Timed Out", incluye una grabación de pantalla, marca de tiempo y zona horaria, navegador y versión, pasos para reproducir el problema y, opcionalmente, un registro HAR de las herramientas de desarrollo de tu navegador. Consulta [¿Qué debo incluir al enviar un ticket de soporte por un error "Request Timed Out"?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error) en las preguntas frecuentes de Canvas.

## Comportamiento de un Canvas detenido {#stopped-canvas-behavior}

**Síntoma:** Detuviste el Canvas, pero los usuarios siguieron recibiendo mensajes.

Cuando detienes un Canvas, los usuarios no pueden entrar y no se envían más mensajes desde el flujo del Canvas. Los envíos de correo electrónico que ya se entregaron a tu proveedor de servicios de correo electrónico no se pueden recuperar.

Los usuarios que esperan en un paso de Retraso o Ruta de Acción no se eliminan automáticamente del recorrido cuando detienes el Canvas. Si vuelves a habilitar el Canvas antes de que pase su hora de envío programada, es posible que aún reciban los pasos pendientes.

Para más detalles, consulta [¿Qué sucede cuando detienes un Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) en las preguntas frecuentes de Canvas.

## Error "Demasiadas ramas en Canvas" {#too-many-canvas-branches-error}

**Síntoma:** Ves un error "Demasiadas ramas en Canvas" al lanzar un Canvas programado.

Este error aparece cuando la combinación de ramificación de pasos y el tamaño del público de entrada puede crear problemas de rendimiento del clúster que impidan el envío de mensajes. Braze muestra este mensaje cuando lanzas un Canvas con una entrada programada; no aparecerá cuando guardes un borrador.

Para resolverlo:

- Reduce la ramificación de pasos en el Canvas.
- Reduce el tamaño del público de entrada.
- Usa [Rutas de Audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) para consolidar la ramificación en lugar de muchas rutas paralelas.
- Si tu Canvas utiliza el editor original, [clónalo a Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) y reconstrúyelo con componentes de Canvas.

Si aún necesitas lanzar el Canvas sin cambios y no puedes migrar a Canvas Flow, contacta con [soporte de Braze]({{site.baseurl}}/support_contact).

## Cuándo contactar con soporte {#when-to-contact-support}

Contacta con [soporte de Braze]({{site.baseurl}}/braze_support) en un plazo de 30 días desde que se produjo el problema si has completado la [ruta de investigación estándar](#standard-investigation-path) y aún necesitas ayuda.

Incluye:

- ID de Canvas e IDs de usuarios afectados (ID externo o ID de Braze)
- Marcas de tiempo con zona horaria
- Capturas de pantalla o exportaciones del **historial de mensajes** o de **Messaging Diagnostics**
- Para errores de "Request Timed Out" en el editor, los detalles indicados en [Problemas del editor y de guardado](#editor-and-save-issues)