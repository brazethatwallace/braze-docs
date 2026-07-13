---
nav_title: Editar tu campaña después del lanzamiento
article_title: Editar tu campaña después del lanzamiento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artículo de referencia ofrece un resumen de los resultados de editar ciertos aspectos de una campaña después de su lanzamiento, incluyendo cómo se propagan los cambios en las campañas de mensajes dentro de la aplicación."

---

# Editar tu campaña después del lanzamiento {#edit-your-campaign-after-launch}

> Este artículo ofrece un resumen de los resultados de editar ciertos aspectos de una campaña después de su lanzamiento.

## Por qué deberías detener una campaña antes de editarla {#risks-of-editing-live}

{% alert important %}
Braze recomienda detener una campaña antes de realizar cambios, en lugar de editarla mientras está en vivo. Editar una campaña en vivo sin detenerla primero puede provocar un comportamiento inesperado, incluyendo que los usuarios reciban el mensaje dos veces.
{% endalert %}

Cuando se lanza una campaña, todos los usuarios elegibles se ponen en cola para recibir el mensaje. Sin embargo, un usuario no se marca como receptor de la campaña hasta que el mensaje se entrega realmente, no cuando se pone en cola. Si editas una campaña en vivo sin detenerla primero, Braze vuelve a poner en cola a los usuarios elegibles para la versión actualizada mientras la cola original aún se está procesando. Los usuarios que aún no han recibido el mensaje original estarán en ambas colas, lo que puede resultar en:

- Usuarios que reciben la campaña dos veces (la versión original y la actualizada), incluso si la reelegibilidad está desactivada.
- La versión original de la campaña aún se entrega a los usuarios en la primera cola.
- Recuentos de audiencia inesperados en los análisis de la campaña.

Esto es más probable que ocurra con campañas que se dirigen a una audiencia grande y están programadas para enviarse de inmediato, ya que hay una gran cola de usuarios procesándose a la vez. Para campañas basadas en acciones con desencadenantes graduales (como eventos de registro), el riesgo es menor porque solo un pequeño número de usuarios suele estar en cola en un momento dado.

Para realizar cambios de forma segura, detén la campaña primero y luego edita la campaña detenida o [duplícala](#making-immediate-changes) con tus cambios.

## Detener tu campaña {#stopping-your-campaign}

Para detener una campaña, abre la página **Detalles de la campaña** y selecciona **Detener campaña**. Cuando se detiene una campaña:

- Los mensajes programados para enviarse se cancelarán.
- Las pruebas A/B en las que ya se haya enviado la prueba inicial se cancelarán permanentemente.
- Los eventos de los mensajes que ya se hayan enviado (por ejemplo, clics de apertura) seguirán siendo rastreados.

Para reiniciar tu campaña, selecciona **Reanudar**. Tu campaña continuará enviando mensajes y pruebas A/B, pero los mensajes perdidos no se volverán a enviar ni a programar.

### Detener tu campaña durante el envío {#stopping-your-campaign-during-sending}

Para campañas con una audiencia más grande y límites de velocidad, Braze divide y planifica lotes de mensajes para enviarlos en diferentes momentos. Cuando se detiene una campaña, los envíos no se cancelan de inmediato. En su lugar, se cancelan cuando comienzan a ejecutarse y detectan que la campaña ha sido detenida.

Por ejemplo, si inicias una campaña de correo electrónico con límite de velocidad, la pausas durante unas horas y luego la reanudas, todos los mensajes que estaban programados para enviarse durante las horas de pausa se cancelan y nunca se envían. Los mensajes restantes programados después de que se reanude la campaña continúan enviándose. Si la reelegibilidad está habilitada para la campaña, los usuarios pueden volver a ser elegibles para recibir la campaña además de cualquier mensaje que ya estuviera en cola antes de que se detuviera la campaña.

## Campañas de mensajes dentro de la aplicación {#in-app-message-campaigns}

A diferencia de push o correo electrónico, los mensajes dentro de la aplicación se entregan a los dispositivos al inicio de la sesión y se almacenan en caché localmente hasta que se activa el desencadenante. Cuando editas una campaña de mensajes dentro de la aplicación en vivo —como detenerla, establecer una [fecha de finalización]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-a-trigger), activar **Reevaluar la elegibilidad de la campaña antes de mostrar**, actualizar el contenido, cambiar el desencadenante del mensaje o actualizar el público objetivo— la configuración actualizada se propaga cuando los dispositivos obtienen los desencadenantes en su siguiente inicio de sesión.

Ten en cuenta lo siguiente:

- Los dispositivos que no hayan iniciado una nueva sesión desde tu cambio pueden seguir usando la configuración anterior hasta que sincronicen los desencadenantes de nuevo.
- Los dispositivos que inicien una sesión después de tu cambio reciben la configuración más reciente.

### Detener un lanzamiento erróneo {#stop-a-mistaken-launch}

Si lanzaste la campaña de mensajes dentro de la aplicación incorrecta, selecciona **Detener campaña** en la página **Detalles de la campaña**. Esta es la forma más rápida de evitar que nuevas sesiones descarguen el mensaje. Los usuarios que ya almacenaron en caché la carga útil antes de que detuvieras la campaña aún pueden verlo cuando cumplan las condiciones del desencadenante, hasta que su dispositivo sincronice los desencadenantes actualizados en una sesión posterior.

[Archivar]({{site.baseurl}}/user_guide/messaging/governance/archiving) y las fechas de finalización siguen las mismas reglas de propagación: detienen la entrega para sincronizaciones futuras, pero no eliminan los mensajes ya almacenados en caché en los dispositivos. Si necesitas revisar, duplicar o editar la campaña, detenla primero y archívala después cuando hayas terminado.

### Limitar entregas obsoletas {#limit-stale-deliveries}

Selecciona **Reevaluar la elegibilidad de la campaña antes de mostrar** en la configuración de entrega de tu campaña para que Braze confirme la pertenencia a la audiencia y el estado de la campaña justo antes de cada visualización. Esto ayuda a prevenir impresiones después de que una campaña se haya detenido, archivado o superado su fecha de finalización. Puedes activar o desactivar esta configuración después del lanzamiento, pero sigue las mismas reglas de propagación que otros cambios: los dispositivos no reciben la configuración actualizada hasta su siguiente sincronización de desencadenantes.

Para más información, consulta [Elegir usuarios a los que dirigirse]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-users-to-target) y [¿Por qué mi campaña de mensajes dentro de la aplicación archivada sigue entregando impresiones de mensajes dentro de la aplicación?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions).

## Campañas desencadenadas {#triggered-campaigns}

Todos los cambios en las campañas de entrega basada en acciones y en las campañas de entrega desencadenadas por API surten efecto inmediatamente para los envíos futuros.

Si estas campañas se han desencadenado pero aún no se han enviado (por ejemplo, una campaña de entrega basada en acciones con un retraso de 1 día se edita durante el período de retraso de 1 día), consulta la siguiente orientación para campañas planificadas.

### Campañas planificadas {#scheduled-campaigns}

Si necesitas hacer cambios en una campaña después de su lanzamiento, ten en cuenta los siguientes puntos al editar tu campaña para verificar que tus cambios tengan los efectos deseados.

### Contenido del mensaje {#message-content}

Cualquier cambio en el contenido del mensaje (incluidos títulos, cuerpos e imágenes) surte efecto inmediatamente al guardar para todos los envíos de mensajes futuros. No es posible cambiar el contenido de los mensajes que ya se han enviado.

### Planificación y audiencia {#scheduling-and-audience}

Si editas la hora de envío planificada de tu campaña o su audiencia, esos cambios se reflejan en la campaña real de inmediato.

#### Consideraciones {#considerations}

Si tu campaña utiliza sincronización inteligente o entrega en zona horaria local, las ediciones a la hora de envío planificada no se reflejarán si la edición se realiza dentro de las 24 horas previas a la hora de envío original. Esto se debe a que:

- **Sincronización inteligente:** Braze comienza a calcular la hora de envío óptima a medianoche, hora de Samoa. Si este momento ya ha pasado, el mensaje habrá comenzado a procesarse. Para más información, consulta [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).
- **Entrega en zona horaria local:** Editar una campaña de zona horaria local que está planificada con menos de 24 horas de antelación no alterará la planificación del mensaje. Para más información, consulta [¿Cómo planifico una campaña de zona horaria local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign).

### Tasa de envío {#send-rate}

Al usar un límite de velocidad de envío, Braze "planifica" tus mensajes en intervalos de tiempo con granularidad de minutos, así que si deseas cambiar la tasa de envío de mensajes, sigue el siguiente proceso para realizar cambios inmediatos.

#### Pausar campañas con limitación de velocidad de entrega {#pausing-campaigns-with-delivery-speed-rate-limiting}

Cuando pausas una campaña que utiliza [limitación de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), Braze distribuye los envíos en intervalos basados en minutos. **Reanudar** no reenvía los mensajes de los intervalos que se cancelaron mientras la campaña estaba pausada, y no todos los mensajes se envían necesariamente cuando se reanuda la campaña.

Si algunos usuarios no recibieron mensajes porque la campaña estuvo pausada, duplica la campaña y dirige el envío solo a esos usuarios en lugar de depender de **Reanudar** para entregar los mensajes perdidos.

## Realizar cambios inmediatos {#making-immediate-changes}

Si necesitas que los cambios surtan efecto de inmediato, haz lo siguiente:

1. Detén la campaña afectada.
2. Duplica la campaña.
3. Realiza las ediciones en la campaña duplicada.

{% alert important %}
Esto restablece la elegibilidad para las personas que ya recibieron la campaña original, por lo que es posible que necesites filtrar la campaña duplicada para las personas que no recibieron la original.
{% endalert %}

## Guardar borradores de campañas activas {#campaign-drafts}

Los borradores son ideales para realizar cambios a gran escala en campañas activas. Al crear un borrador, puedes probar los cambios planificados antes de tu próximo lanzamiento.

{% alert note %}
Una campaña solo puede tener un borrador a la vez. Además, los análisis no están disponibles ya que los cambios del borrador aún no se han lanzado.
{% endalert %}

Para crear un borrador, haz lo siguiente:

1. Ve a tu campaña activa.
2. Realiza tus cambios.
3. Selecciona **Guardar como borrador**. Ten en cuenta que después de crear un borrador, no puedes editar la campaña activa hasta que lances o descartes tu borrador.

![Un borrador de una campaña activa con la opción de ver la campaña activa.]({% image_buster /assets/img/campaign_draft.png %})

Mientras realizas ediciones en el borrador, también puedes consultar la campaña activa en el encabezado del borrador de la campaña o en el pie de página de los análisis de la campaña.

Para volver a una campaña activa, selecciona **Editar borrador** desde la vista de análisis o la vista de la campaña activa.

### Priorización de mensajes dentro de la aplicación {#in-app-message-prioritization}

La prioridad de los mensajes dentro de la aplicación se actualizará inmediatamente (antes de que se lance el borrador) cuando selecciones **Establecer prioridad exacta** y especifiques la prioridad en relación con otras campañas o Canvas.