---
nav_title: Buenas prácticas
article_title: Buenas prácticas de Canvas
page_order: 1
description: "Este artículo ofrece algunas buenas prácticas para crear y personalizar recorridos de usuario con Canvas y Canvas Flow."
tool: Canvas

---

# Buenas prácticas de Canvas {#canvas-best-practices}

> Este artículo ofrece algunas buenas prácticas para crear y personalizar recorridos de usuario con Canvas y Canvas Flow.

## Identifica tu propósito {#identify-your-purpose}

¡Profundiza en el qué, quién y por qué!
- ¿Qué intentas ayudar a lograr a los usuarios?
- ¿Quiénes son los usuarios a los que intentas llegar?
- ¿Por qué estás creando este Canvas?

## Combina y experimenta {#mix-and-match}

Desbloquea nuevas combinaciones de recorridos de usuario con los [componentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/).
- Divide a tus usuarios con la [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) y crea diferentes flujos de trabajo.
- Espacia tus recorridos de usuario con un paso de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/).
- Añade [mensajes independientes]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) en cualquier punto de tu flujo de Canvas.

{% alert note %}
Los pasos en Canvas solo pueden mover a los usuarios hacia adelante en el flujo. No puedes configurar un Canvas para vincular un paso a un paso anterior, ya que esto enviaría a los usuarios hacia atrás. Esta validación garantiza que los usuarios avancen en una sola dirección a través de tu Canvas.
{% endalert %}

## Crea mensajes más enriquecidos {#create-richer-messages}

Atrae a tus usuarios con mensajes más enriquecidos.

- Crea [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) para Canvas de incorporación y aprovecha al máximo tu primera impresión.
- Incorpora [Content Cards]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) en un recorrido de Canvas para ofertas promocionales y notificaciones push.

## Prueba tus recorridos de usuario {#test-your-user-journeys}

Determina el impacto de la mensajería de tu Canvas incorporando grupos de control. De esta forma, podrás comprender cómo fue recibido tu Canvas.

- Nombra cada paso de tu Canvas para identificar tu recorrido de usuario.
- Aprovecha el componente [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) en tu recorrido de usuario para asignar aleatoriamente a los usuarios a diferentes rutas que crees.
- Diversifica tus recorridos de usuario con pasos de Retraso y Mensaje para ayudar a descubrir qué ruta es más efectiva.
- Consulta los [análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para ver el rendimiento de cada componente en tu recorrido de usuario.
- [Edita tu Canvas]({{site.baseurl}}/post-launch_edits/) después del lanzamiento inicial.

## Planificación de tus Canvas {#scheduling-your-canvases}

{% alert note %}
Canvas te impedirá usar el envío planificado con una hora que ya haya pasado. Sin embargo, es posible lanzar un Canvas durante el mismo minuto exacto en que la campaña está planificada (o en los segundos anteriores). Esto puede provocar que el Canvas no alcance la hora de entrada planificada y que los usuarios no entren en el Canvas. Recomendamos enviar los Canvas inmediatamente en caso de que alguna campaña se edite dentro de los minutos previos a la hora de envío planificada.
{% endalert %}

{% alert important %}
La evaluación de la planificación y la audiencia puede diferir entre las entradas planificadas y las entradas de envío inmediato; por ejemplo, cuando los pasos utilizan opciones que se evalúan más cerca del momento de envío. Cuando edites la audiencia, la planificación o la configuración de entrega dentro de los minutos previos a una entrada planificada o una ventana de envío, confirma si los usuarios que ya están en cola para el siguiente paso reciben el cambio (consulta [Cambiar tu Canvas después del lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/)); en caso de duda, detén, duplica y relanza para una reevaluación limpia.
{% endalert %}

Para los pasos en Canvas, ten en cuenta los siguientes detalles al planificar tu Canvas:

- Los cambios de planificación solo se aplican a los usuarios que aún no estén esperando para recibir el paso.
- Los cambios de audiencia se aplican de forma predeterminada a todos los usuarios, a menos que programes los cambios para que se apliquen a los usuarios que no estén esperando para recibir el paso.
- Editar un Canvas que está planificado para entregarse tan pronto como se despliegue y seleccionar **Actualizar** hará que se envíe de forma efectiva.

### Ediciones posteriores al lanzamiento {#post-launch-edits}

Si detienes un Canvas activo mientras existe un borrador sin guardar, detenerlo puede descartar ese borrador. Guarda, lanza o descarta el borrador antes de detenerlo si necesitas conservar las ediciones en curso.

#### Momento de evaluación de la audiencia {#audience-evaluation-timing}

Braze evalúa las audiencias en diferentes puntos del constructor de Canvas y en los pasos individuales. Para obtener detalles de configuración, consulta:

- [Establece tu audiencia objetivo de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-13-set-your-target-entry-audience) y [Determina tu horario de entrada de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule) cuando crees un Canvas
- [Cómo funcionan juntos la audiencia objetivo y los criterios de entrada]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/#how-target-audience-and-entry-criteria-work-together)
- [Editar la configuración de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) para los pasos de Mensaje
- [Cómo se evalúan los usuarios]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/#how-users-are-evaluated) para los pasos de Rutas de audiencia

Si editas un Canvas en vivo cerca de una ventana de entrada o envío planificada, es posible que los usuarios que ya estén en cola para un paso de **Mensaje** no reciban tus cambios. Para más información, consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/).