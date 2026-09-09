---
nav_title: Lanzar con Canvas Flow
article_title: Lanzar con Canvas Flow
page_order: 3
description: "Este artículo de referencia explica cómo preparar y probar un Canvas creado con Canvas Flow antes de su lanzamiento."
page_type: reference
tool: Canvas
---

# Lanzar con Canvas Flow {#launch-with-canvas-flow}

> Este artículo de referencia explica cómo preparar y probar un Canvas creado con Canvas Flow antes de su lanzamiento. Esto incluye identificar puntos de control importantes del Canvas, como las condiciones de entrada, los resúmenes de audiencia y los segmentos de usuarios.

Mientras te preparas para lanzar tu Canvas, Braze recomienda que lo revises en cada etapa del creador de Canvas en busca de configuraciones que puedan afectar el envío de tus mensajes, incluyendo:
* [Condiciones de carrera](#race-conditions)
* [Tiempos de entrega](#delivery-times)
* [Segmentos de usuarios](#segment-users)

## Condiciones de carrera {#race-conditions}

Considera las [condiciones de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) que pueden ocurrir antes de lanzar tu Canvas.

Para entrar en un Canvas, los usuarios deben estar en el público de entrada antes de que se produzca la programación de entrada, independientemente de si el Canvas es programado, basado en acciones o activado por API.

![Un Canvas basado en acciones que ingresa a los usuarios cuando realizan cualquier compra durante la hora local del usuario desde el 30 de abril de 2025 a las 12 pm hasta el 7 de mayo de 2025 a las 12 pm.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Ten en cuenta que los usuarios que califiquen para tu público de entrada después de que se lance el Canvas no entrarán en el Canvas.

{% alert tip %}
Consulta los [tipos de programación de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) para obtener orientación y detalles sobre cuándo usar la entrega programada, basada en acciones o activada por API para tu Canvas.
{% endalert %}

### Revisar los filtros del público de entrada {#review-entry-audience-filters}

En general, evita configurar un Canvas basado en acciones o activado por API con el mismo desencadenante que el filtro de audiencia. Por ejemplo, después de que se lanza un Canvas, los usuarios que realizan una acción específica se incluirán en el público de entrada, por lo que no es necesario añadir el evento como filtro de audiencia.

Para más detalles sobre los filtros de segmentación disponibles para segmentar tu audiencia, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Agrupar múltiples solicitudes de API {#batch-multiple-api-requests}

Realiza tus solicitudes en la misma llamada a la API, en lugar de múltiples llamadas, para confirmar que el perfil de usuario se crea o actualiza primero. Consulta [Uso de múltiples endpoints]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-2-using-multiple-api-endpoints) para más ejemplos.

### Añadir un retraso {#add-a-delay}

Otra opción para evitar condiciones de carrera es usar el paso de Retraso (idealmente configurado para 5 minutos) como primer paso de tu Canvas.

Esto permite que los atributos, las direcciones de correo electrónico y los tokens de notificaciones push se procesen en los nuevos perfiles de usuario antes de que sean segmentados para los siguientes pasos en Canvas. Sin este paso de Retraso, es posible que se envíe un correo electrónico a un usuario cuyo correo electrónico aún no se ha actualizado.

## Tiempos de entrega {#delivery-times}

Configurar un tiempo de entrega de Canvas en tiempo real puede aumentar la participación y las tasas de conversión. Toma nota de qué tiempo de entrega has configurado para tu Canvas. Para ayudar a aumentar la participación y las tasas de conversión, es mejor desencadenar Canvas en tiempo real en lugar de hacerlo de forma programada y recurrente.

Si seleccionaste una entrega programada para tu Canvas, Braze recomienda programar tu Canvas al menos 24 horas antes de que quieras lanzarlo, para permitir cualquier ajuste en tu Canvas.

## Segments de usuarios {#user-segments}

Antes de saturar tu recorrido de usuario en Canvas Flow con componentes, piensa en cómo podrías mantener un recorrido de usuario sencillo. Usa la vista simplificada en el editor de Canvas para tener una mejor idea de cómo se ramifica tu recorrido de usuario.

Hay cuatro componentes principales que puedes utilizar para segmentar a tus usuarios de forma sencilla y eficaz:

* [Rutas de audiencia](#audience-paths)
* [División de decisiones](#decision-split)
* [Rutas de Acción](#action-paths)
* [Recorridos de experimentos](#experiment-paths)

### Rutas de audiencia {#audience-paths}

Usa los pasos de [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) para segmentar a los usuarios dentro del Canvas en función de atributos personalizados, eventos personalizados y datos de participación con mensajes anteriores de los perfiles de usuario.

### División de decisiones {#decision-split}

El paso de [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) te permite enviar a tus usuarios por diferentes recorridos en función de sus respuestas a una pregunta polar.

### Rutas de Acción {#action-paths}

Las [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) se centran en segmentar a los usuarios en función de comportamientos en tiempo real, como eventos personalizados, eventos de compra y cambios en atributos personalizados.

### Recorridos de experimentos {#experiment-paths}

De forma similar a las Rutas de Acción, puedes aprovechar los pasos de [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) en tu Canvas para probar múltiples recorridos de Canvas entre sí, junto con un grupo de control. Esto realiza un seguimiento del rendimiento de los recorridos, lo que te permite tomar decisiones informadas al construir tu recorrido en Canvas.

## Pruebas antes del lanzamiento {#testing-before-launch}

Después de revisar los detalles más específicos de tu Canvas, consulta [Envío de Canvas de prueba]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) para conocer los diferentes métodos que puedes aprovechar para probar tu Canvas con usuarios de prueba.

## Lista de verificación de lanzamiento {#launch-checklist}

### Comprueba la disponibilidad de los usuarios {#check-user-availability}

- Asegúrate de que tus usuarios cumplen tus criterios de segmentación.
- Confirma que su estado de suscripción sea "subscribed" u "opted-in" y que exista su token de notificaciones push. Si añadiste estas como reglas de entrada de Canvas, es posible que los usuarios hayan cancelado su suscripción entre el momento en que entraron a tu Canvas y la recepción del paso de mensaje.
- Confirma que coincidan con la configuración de envío de tu Canvas. (Si los usuarios están "subscribed" pero la configuración está en "Opted-in", los usuarios no estarán habilitados para el canal).
- Si la limitación de frecuencia global está habilitada para tu Canvas, comprueba si tus reglas están limitando cuántas veces cada usuario puede recibir un mensaje de un canal específico.
- Si las horas tranquilas están habilitadas, la hora de envío de tu mensaje podría verse afectada, lo que significa que tu mensaje puede enviarse en el próximo horario disponible (cuando terminen las horas tranquilas) o cancelarse por completo.
- Comprueba la disponibilidad de los usuarios para filtros adicionales en tu paso en Canvas.

### Confirma que realizaron el evento personalizado o la compra de requisito previo {#confirm-that-they-performed-the-prerequisite-custom-event-or-purchase}

- Comprueba si hay una condición de carrera, que afecta los mensajes que reciben los usuarios si desencadenan múltiples acciones al mismo tiempo.
- Asegúrate de que no haya filtros específicos en el paso que puedan haber bloqueado a los usuarios para recibir el mensaje.
- Busca conflictos entre diferentes pasos dentro del mismo Canvas. Por ejemplo, los usuarios que no recibieron el mensaje podrían estar detenidos por un filtro que requiere la finalización de otro paso en una rama diferente.
- Confirma que los usuarios cumplen las reglas de validación adicionales.
- Confirma que el paso en Canvas estaba conectado al paso anterior en el momento del envío.

### Confirma que tu Canvas se guarda correctamente y que todos los pasos son válidos {#confirm-your-canvas-saves-correctly-and-all-steps-are-valid}

Si tu Canvas no se carga y no avanza, esto puede deberse a que una versión anterior del Canvas no se guardó correctamente y contiene pasos no válidos. Puedes duplicar el Canvas desde el panel. Si el problema persiste, abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Solución de problemas {#troubleshooting}

{% details ¿Por qué mis usuarios no reciben mis mensajes de Canvas? %}
**Comprueba la disponibilidad del usuario**
- Asegúrate de que cumplen tus criterios de segmentación.
- Confirma que su estado de suscripción push es "subscribed" u "opted-in" **y** que su estado de **Push Enabled** está configurado como "true". Si añadiste estas como reglas de entrada de Canvas, es posible que los usuarios hayan cancelado su suscripción entre el momento en que entraron a tu Canvas y la recepción del paso de mensaje.
- Confirma que coinciden con la configuración de envío de tu Canvas. (Si los usuarios están "subscribed" pero la configuración es "Opted-in", los usuarios no estarán habilitados para el canal).
- Si la limitación de frecuencia global está habilitada para tu Canvas, comprueba si tus reglas están limitando cuántas veces cada usuario puede recibir un mensaje de un canal específico.
- Si las horas tranquilas están habilitadas, la hora de envío de tu mensaje podría verse afectada, lo que significa que tu mensaje puede enviarse en el siguiente horario disponible (cuando terminen las horas tranquilas) o cancelarse por completo.

**Comprueba la disponibilidad del usuario para filtros adicionales en tu paso en Canvas**
- Confirma que realizaron el evento personalizado o la compra de requisito previo.
- Comprueba si hay una [condición de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions), que afecta los mensajes que reciben los usuarios si desencadenan múltiples acciones al mismo tiempo.
- Asegúrate de que no haya filtros específicos en el paso que puedan haber bloqueado a los usuarios de recibir el mensaje.
- Busca conflictos entre diferentes pasos dentro del mismo Canvas. Por ejemplo, los usuarios que no recibieron el mensaje podrían estar detenidos por un filtro que requiere la finalización de otro paso en una rama diferente.
- Confirma que los usuarios cumplen las reglas de validación adicionales.
- Confirma que el paso en Canvas estaba conectado al paso anterior en el momento del envío.
{% enddetails %}