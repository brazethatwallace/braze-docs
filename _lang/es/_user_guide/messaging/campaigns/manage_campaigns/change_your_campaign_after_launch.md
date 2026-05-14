---
nav_title: Editar tu campaña después del lanzamiento
article_title: Editar tu campaña después del lanzamiento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artículo de referencia ofrece un resumen de los resultados de editar ciertos aspectos de una campaña después de su lanzamiento."

---

# Editar tu campaña después del lanzamiento

> Este artículo ofrece un resumen de los resultados de editar ciertos aspectos de una campaña después de su lanzamiento.

## Detener tu campaña

Para detener una campaña, abre la página **Detalles de la campaña** y selecciona **Detener campaña**. Cuando se detiene una campaña:

- Los mensajes programados para enviarse se cancelarán.
- Las pruebas A/B en las que ya se haya enviado la prueba inicial se cancelarán permanentemente.
- Los eventos de los mensajes que ya se hayan enviado (por ejemplo, clics de apertura) seguirán siendo rastreados.

Para reiniciar tu campaña, selecciona **Reanudar**. Tu campaña continuará enviando mensajes y pruebas A/B, pero los mensajes perdidos no se volverán a enviar ni a programar.

## Campañas desencadenadas

Todos los cambios en las campañas de entrega basada en acciones y en las campañas de entrega desencadenadas por API surten efecto inmediatamente para los envíos futuros.

Si estas campañas se han desencadenado pero aún no se han enviado (por ejemplo, una campaña de entrega basada en acciones con un retraso de 1 día se edita durante el período de retraso de 1 día), consulta la siguiente orientación para campañas planificadas.

### Campañas planificadas

Si necesitas hacer cambios en una campaña después de su lanzamiento, ten en cuenta los siguientes puntos al editar tu campaña para verificar que tus cambios tengan los efectos deseados.

### Contenido del mensaje

Cualquier cambio en el contenido del mensaje (incluidos títulos, cuerpos e imágenes) surte efecto inmediatamente al guardar para todos los envíos de mensajes futuros. No es posible cambiar el contenido de los mensajes que ya se han enviado.

### Planificación y audiencia

Si editas la hora de envío planificada de tu campaña o su audiencia, esos cambios se reflejan en la campaña real de inmediato.

#### Consideraciones

Si tu campaña utiliza Intelligent Timing o entrega en zona horaria local, las ediciones a la hora de envío planificada no se reflejarán si la edición se realiza dentro de las 24 horas previas a la hora de envío original. Esto se debe a que:

- **Intelligent Timing:** Braze comienza a calcular la hora de envío óptima a medianoche, hora de Samoa. Si este momento ya ha pasado, el mensaje habrá comenzado a procesarse. Para más información, consulta [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).
- **Entrega en zona horaria local:** Editar una campaña de zona horaria local que está planificada con menos de 24 horas de antelación no alterará la planificación del mensaje. Para más información, consulta [¿Cómo planifico una campaña de zona horaria local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign).

### Tasa de envío

Al usar un límite de velocidad de envío, Braze "planifica" tus mensajes en intervalos de tiempo con granularidad de minutos, así que si deseas cambiar la tasa de envío de mensajes, sigue el siguiente proceso para realizar cambios inmediatos.

## Realizar cambios inmediatos

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

Para volver a una campaña activa, selecciona **Modificar borrador** desde la vista de análisis o la vista de la campaña activa.

### Priorización de mensajes dentro de la aplicación

La prioridad de los mensajes dentro de la aplicación se actualizará inmediatamente (antes de que se lance el borrador) cuando selecciones **Establece la prioridad exacta** y especifiques la prioridad en relación con otras campañas o Canvas.