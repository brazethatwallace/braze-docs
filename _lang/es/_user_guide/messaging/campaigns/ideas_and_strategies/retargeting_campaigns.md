---
nav_title: Reorientación de campañas
article_title: Reorientar campañas
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo y por qué deberías considerar reorientar campañas basándote en los mensajes que reciben tus usuarios."
tool:
  - Campaigns

---

# Reorientar campañas {#retarget-campaigns}

> Al reorientar campañas basándote en las acciones previas del usuario, como si abrió o no un correo electrónico, puedes ayudar a reclasificar a tus usuarios, abriendo la puerta a un enfoque de marketing basado en datos eficaz.

Braze ofrece soporte para reorientar usuarios en función de los mensajes que han recibido. Puedes reorientar usuarios en función de sus interacciones con tus campañas y Canvas.

Cada uno de estos filtros de reorientación te ofrece varias opciones después de añadirlos. Para más información sobre cómo segmentar usuarios, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.

![Sección de detalles del segmento con el menú desplegable de los filtros disponibles.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Filtros de reorientación {#retargeting-filters}

Puedes usar los filtros de reorientación de esta sección para tus usuarios dentro de tus campañas y Canvas.

### Hizo clic/abrió Campaign {#clickedopened-campaign}

Usa este filtro para encontrar usuarios que han o no han:

- Hecho clic en un correo electrónico
- Hecho clic en un mensaje dentro de la aplicación
- Abierto directamente una notificación push
- Abierto un correo electrónico
- Visto un mensaje dentro de la aplicación

![Filtro Hizo clic/abrió Campaign con opciones de interacción de canal.]({% image_buster /assets/img_archive/clickedopened.png %})

Esto se puede especificar aún más seleccionando la campaña que deseas reorientar.

### Hizo clic o abrió Campaign o Canvas con etiqueta {#clicked-or-opened-campaign-or-canvas-with-tag}

Usa este filtro para encontrar usuarios que han o no han interactuado con campañas o Canvas con una etiqueta determinada:

- Hecho clic en un correo electrónico
- Hecho clic en un mensaje dentro de la aplicación
- Abierto directamente una notificación push
- Abierto un correo electrónico
- Visto un mensaje dentro de la aplicación

![Filtro Hizo clic o abrió Campaign o Canvas con etiqueta.]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Convirtió desde Campaign {#converted-from-campaign}

Usa este filtro para encontrar usuarios que han o no han convertido (basándose en la conversión primaria) en tu campaña objetivo.

Para campañas recurrentes, este filtro se refiere a si los usuarios han convertido en el mensaje más reciente de la campaña.

![Filtro Convirtió desde Campaign con selección de campaña.]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Convirtió desde Canvas {#converted-from-canvas}

Usa este filtro para encontrar usuarios que han o no han convertido (basándose en la conversión primaria) en tu Canvas objetivo.

Para Canvas recurrentes, este filtro se refiere a si los usuarios han convertido en algún momento durante su recorrido por el Canvas.

![Filtro Convirtió desde Canvas con selección de Canvas.]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### En grupo de control de Campaign {#in-campaign-control-group}

Usa este filtro para encontrar usuarios que están o no están en el grupo de control de tu campaña objetivo.

![Filtro En grupo de control de Campaign con selección de campaña.]({% image_buster /assets/img_archive/campaign_control_group.png %})

### En grupo de control de Canvas {#in-canvas-control-group}

Usa este filtro para encontrar usuarios que están o no están en el grupo de control de tu Canvas objetivo, que se puede seleccionar en el menú desplegable.

![Filtro En grupo de control de Canvas con selección de Canvas.]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Último mensaje recibido de una campaña específica {#last-received-message-from-specific-campaign}

Usa este filtro para encontrar usuarios que recibieron por última vez una campaña específica antes o después de una fecha o número de días determinado. Este filtro no tiene en cuenta cuándo los usuarios recibieron otras campañas.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![Filtro Último mensaje recibido de una campaña específica con opciones de fecha.]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Último mensaje recibido de Campaign o Canvas con etiqueta {#last-received-message-from-campaign-or-canvas-with-tag}

Usa este filtro para encontrar usuarios que recibieron por última vez una campaña o Canvas con una etiqueta determinada antes o después de una fecha o número de días determinado. Este filtro no tiene en cuenta cuándo los usuarios recibieron otras campañas o Canvas.

![Filtro Último mensaje recibido de Campaign o Canvas con etiqueta.]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Recibió mensaje de Campaign {#received-message-from-campaign}

Usa este filtro para encontrar usuarios que han o no han recibido tu campaña objetivo.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![Filtro Recibió mensaje de Campaign con selección de campaña.]({% image_buster /assets/img_archive/receivedcamp.png %})

### Recibió mensaje de Campaign o Canvas con etiqueta {#received-message-from-campaign-or-canvas-with-tag}

Usa este filtro para encontrar usuarios que han o no han recibido una campaña o Canvas que tiene tu etiqueta objetivo.

![Filtro Recibió mensaje de Campaign o Canvas con etiqueta.]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Ventajas de reorientar campañas {#advantages-with-retargeting-campaigns}

La reorientación es particularmente eficaz cuando el segmento original también incluía una acción específica que deseas que los usuarios realicen. Por ejemplo, supongamos que tienes una tarjeta dirigida a usuarios que nunca han realizado una compra. La tarjeta anuncia una promoción para una compra dentro de la aplicación con descuento. El segmento inicial se ve así:

- Dinero gastado en la aplicación es exactamente 0
- Última vez que usó la aplicación hace menos de 14 días

El número total de usuarios en el segmento es 100 000 y sabes por las estadísticas de tarjetas de contenido que 60 000 usuarios únicos vieron la tarjeta y 20 000 usuarios únicos hicieron clic en la tarjeta. A través del segmentador podemos ver cuántos de esos usuarios que hicieron clic en la tarjeta realmente realizaron una compra:

- Dinero gastado en la aplicación es más de 0
- Hizo clic en la tarjeta es Nombre de la tarjeta

Después de examinar esas estadísticas, podemos crear un segmento de usuarios que hicieron clic en la tarjeta, pero no realizaron una compra:

- Dinero gastado en la aplicación es exactamente 0
- Hizo clic en la tarjeta es Nombre de la tarjeta

Podemos reorientar este segmento con mensajería adicional sobre la promoción u otra compra dentro de la aplicación. La reorientación se puede hacer con una campaña de mensajería. Un enfoque multicanal te permite llegar a los usuarios donde es más probable que respondan, aumentando así la efectividad de tus campañas.