---
nav_title: Lanzar con Canvas Flow
article_title: Lanzar con Canvas Flow
page_order: 3
description: "Este artículo de referencia explica cómo preparar y probar un Canvas creado con Canvas Flow antes de su lanzamiento."
page_type: reference
tool: Canvas
---

# Lanzar con Canvas Flow

> Este artículo de referencia explica cómo preparar y probar un Canvas creado con Canvas Flow antes de su lanzamiento. Esto incluye identificar puntos de control importantes del Canvas, como las condiciones de entrada, los resúmenes de audiencia y los segmentos de usuarios.

Mientras te preparas para lanzar tu Canvas, Braze recomienda que lo revises en cada etapa del creador de Canvas en busca de configuraciones que puedan afectar el envío de tus mensajes, incluyendo:
* [Condiciones de carrera](#race-conditions)
* [Tiempos de entrega](#delivery-times)
* [Segmentos de usuarios](#segment-users)

## Condiciones de carrera

Considera las [condiciones de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/) que pueden ocurrir antes de lanzar tu Canvas.

Para entrar en un Canvas, los usuarios deben estar en la audiencia de entrada antes de que ocurra el horario de entrada, independientemente de si el Canvas es planificado, basado en acciones o desencadenado por API.

![Un Canvas basado en acciones que permite la entrada de usuarios cuando realizan cualquier compra durante la hora local del usuario desde el 30 de abril de 2025 a las 12 pm hasta el 7 de mayo de 2025 a las 12 pm.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Ten en cuenta que los usuarios que califiquen para tu audiencia de entrada después de que se lance el Canvas no entrarán en él.

{% alert tip %}
Consulta [Tipos de horario de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule) para obtener orientación y detalles sobre cuándo usar la entrega planificada, basada en acciones o desencadenada por API para tu Canvas.
{% endalert %}

### Revisar los filtros de audiencia de entrada

En general, evita configurar un Canvas basado en acciones o desencadenado por API con el mismo desencadenante que el filtro de audiencia. Por ejemplo, después de que se lance un Canvas, los usuarios que realicen una acción específica se incluirán en la audiencia de entrada, por lo que no es necesario añadir el evento como filtro de audiencia.

Para más detalles sobre los filtros de segmentación disponibles para segmentar tu audiencia, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

### Agrupar múltiples solicitudes de API

Realiza tus solicitudes en la misma llamada a la API, en lugar de múltiples llamadas, para confirmar que el perfil de usuario se crea o actualiza primero. Consulta [Uso de múltiples puntos de conexión]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#using-multiple-api-endpoints) para más ejemplos.

### Añadir un retraso

Otra opción para evitar condiciones de carrera es usar el paso de Retraso (idealmente configurado en 5 minutos) como primer paso de tu Canvas.

Esto permite que los atributos, las direcciones de correo electrónico y los tokens de notificaciones push se procesen en los nuevos perfiles de usuario antes de que sean objetivo de los pasos siguientes del Canvas. Sin este paso de Retraso, es posible que se envíe un correo electrónico a un usuario cuya dirección de correo electrónico aún no se ha actualizado.

## Tiempos de entrega

Configurar un tiempo de entrega del Canvas en tiempo real puede aumentar las tasas de interacción y conversión. Toma nota del tiempo de entrega que has configurado para tu Canvas. Para ayudar a aumentar las tasas de interacción y conversión, es mejor desencadenar los Canvas en tiempo real en lugar de hacerlo de forma planificada y recurrente.

Si seleccionaste una entrega planificada para tu Canvas, Braze recomienda planificar tu Canvas al menos 24 horas antes de que quieras lanzarlo para permitir cualquier ajuste.

## Segmentos de usuarios

Antes de saturar el recorrido de usuario de tu Canvas Flow con componentes, considera cómo podrías mantener un recorrido de usuario simple. Usa la vista simplificada en el editor de Canvas para tener una mejor idea de cómo se ramifica tu recorrido de usuario.

Hay cuatro componentes principales que puedes usar para segmentar a tus usuarios de manera simple y efectiva:

* [Rutas de audiencia](#audience-paths)
* [División de decisiones](#decision-split)
* [Rutas de acción](#action-paths)
* [Recorridos de experimentos](#experiment-paths)

### Rutas de audiencia

Usa los pasos de [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) para segmentar usuarios dentro del Canvas basándote en atributos personalizados, eventos personalizados y datos de interacción con mensajes anteriores de los perfiles de usuario.

### División de decisiones

El paso de [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) te permite enviar a tus usuarios por diferentes recorridos basándote en sus respuestas a una pregunta polar.

### Rutas de acción

Las [Rutas de acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/) se centran en segmentar usuarios basándose en comportamientos en tiempo real, como eventos personalizados, eventos de compra y cambios en atributos personalizados.

### Recorridos de experimentos

De manera similar a las Rutas de acción, puedes aprovechar los pasos de [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) en tu Canvas para probar múltiples rutas de Canvas entre sí, junto con un grupo de control. Esto rastrea el rendimiento de las rutas, permitiéndote tomar decisiones informadas al construir el recorrido de tu Canvas.

## Pruebas antes del lanzamiento

Después de revisar los detalles más finos de tu Canvas, consulta [Enviar Canvas de prueba]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases/) para conocer los diferentes métodos que puedes aprovechar para probar tu Canvas con usuarios de prueba.

## Lista de verificación de lanzamiento

### Verificar la disponibilidad de los usuarios

- Asegúrate de que tus usuarios cumplan con tus criterios de segmentación.
- Confirma que su estado de suscripción sea "suscrito" u "opted-in" y que su token de notificaciones push exista. Si añadiste estas como reglas de entrada del Canvas, es posible que los usuarios hayan cancelado su suscripción entre el momento de entrar en tu Canvas y recibir el paso de mensaje.
- Confirma que coincidan con tus ajustes de envío del Canvas. (Si los usuarios están "suscritos" pero la configuración es "Opted-in", los usuarios no estarán habilitados para el canal.)
- Si la limitación de frecuencia global está habilitada para tu Canvas, verifica si tus reglas están limitando cuántas veces cada usuario puede recibir un mensaje de un canal específico.
- Si las horas tranquilas están habilitadas, el tiempo de envío de tu mensaje podría verse afectado, lo que significa que tu mensaje podría enviarse en el siguiente horario disponible (cuando terminen las horas tranquilas) o cancelarse por completo.
- Verifica la disponibilidad de los usuarios para filtros adicionales en tu paso en Canvas.

### Confirmar que realizaron el evento personalizado o la compra como prerrequisito

- Verifica si hay una condición de carrera, que afecta los mensajes que reciben los usuarios si desencadenan múltiples acciones al mismo tiempo.
- Asegúrate de que no haya filtros específicos en el paso que puedan haber bloqueado a los usuarios de recibir el mensaje.
- Busca conflictos entre diferentes pasos dentro del mismo Canvas. Por ejemplo, los usuarios que no recibieron el mensaje podrían estar detenidos por un filtro que requiere la finalización de otro paso en una rama diferente.
- Confirma que los usuarios cumplan con las reglas de validación adicionales.
- Confirma que el paso en Canvas estaba conectado al paso anterior en el momento del envío.

### Confirmar que tu Canvas se guarda correctamente y que todos los pasos son válidos

Si tu Canvas no carga y no avanza, esto puede deberse a que una versión anterior del Canvas no se guardó correctamente y contiene pasos no válidos. Puedes duplicar el Canvas desde el dashboard. Si el problema persiste, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

## Solución de problemas

{% details ¿Por qué mis usuarios no están recibiendo mis mensajes de Canvas? %}
**Verificar la disponibilidad de los usuarios**
- Asegúrate de que cumplan con tus criterios de segmentación.
- Confirma que su estado de suscripción push sea "suscrito" u "opted-in" **y** que su estado de **Push habilitado** esté configurado como "true". Si añadiste estas como reglas de entrada del Canvas, es posible que los usuarios hayan cancelado su suscripción entre el momento de entrar en tu Canvas y recibir el paso de mensaje.
- Confirma que coincidan con tus ajustes de envío del Canvas. (Si los usuarios están "suscritos" pero la configuración es "Opted-in", los usuarios no estarán habilitados para el canal.)
- Si la limitación de frecuencia global está habilitada para tu Canvas, verifica si tus reglas están limitando cuántas veces cada usuario puede recibir un mensaje de un canal específico.
- Si las horas tranquilas están habilitadas, el tiempo de envío de tu mensaje podría verse afectado, lo que significa que tu mensaje podría enviarse en el siguiente horario disponible (cuando terminen las horas tranquilas) o cancelarse por completo.

**Verificar la disponibilidad de los usuarios para filtros adicionales en tu paso en Canvas**
- Confirma que realizaron el evento personalizado o la compra como prerrequisito.
- Verifica si hay una [condición de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/), que afecta los mensajes que reciben los usuarios si desencadenan múltiples acciones al mismo tiempo.
- Asegúrate de que no haya filtros específicos en el paso que puedan haber bloqueado a los usuarios de recibir el mensaje.
- Busca conflictos entre diferentes pasos dentro del mismo Canvas. Por ejemplo, los usuarios que no recibieron el mensaje podrían estar detenidos por un filtro que requiere la finalización de otro paso en una rama diferente.
- Confirma que los usuarios cumplan con las reglas de validación adicionales.
- Confirma que el paso en Canvas estaba conectado al paso anterior en el momento del envío.
{% enddetails %}