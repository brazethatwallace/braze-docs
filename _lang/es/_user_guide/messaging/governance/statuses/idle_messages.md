---
nav_title: Campaigns y Canvas inactivos
article_title: Campaigns y Canvas inactivos
page_order: 1
page_type: reference
alias: /idle_campaigns/
description: "Este artículo de referencia cubre el estado inactivo de Campaigns y Canvas, incluyendo los criterios de detención automática y las preguntas frecuentes."
toc_headers: h2
---

# Campaigns y Canvas inactivos {#idle-campaigns-and-canvases}

> Campaigns y Canvas se vuelven inactivos cuando dejan de enviar mensajes o de dar entrada a usuarios durante un periodo definido.

Braze detiene automáticamente Campaigns y Canvas inactivos en sus fechas de detención asociadas. Permanecen activos hasta que Braze los detiene. Los envíos únicos y la mensajería con fechas de finalización se vuelven inactivos cuando esa fecha pasa, y luego se detienen automáticamente después de siete días. La mensajería sin fecha de finalización se vuelve inactiva después de 11 meses sin actividad y se detiene automáticamente después de un año.

## Campaigns inactivas {#idle-campaigns}

Braze detiene las Campaigns inactivas que cumplan cualquiera de estos criterios:

- Un envío único programado ha superado su fecha de envío en siete días
- Una Campaign programada o basada en acciones con fecha de finalización ha superado su fecha de finalización en siete días
- Una Campaign sin fecha de finalización no ha enviado un mensaje, inscrito a un usuario en un grupo de control ni sido editada en un año

Para Campaigns sin fecha de finalización, un envío, inscripción en grupo de control o edición reinicia la cuenta regresiva de un año. Cuando Braze detiene Campaigns, notifica a los usuarios de la empresa en el panel y por correo electrónico.

Braze detiene las Campaigns en la fecha más tardía entre la fecha de detención predeterminada y un día después de la fecha límite de la última conversión. Los envíos desde una variante ganadora o personalizada se tratan como envíos programados, y Braze los detiene siete días después de que esa variante se envíe. Las Campaigns se detienen a las 4 am UTC cada día.

Las Content Cards no se detienen hasta su fecha límite de expiración, y también siguen los criterios de detención de Campaigns inactivas y la regla de la fecha límite de conversión. Para más detalles, consulta [¿Cómo funciona la detención de Content Cards?](#how-does-stopping-content-cards-work).

Usa esta tabla para mantener activa una Campaign inactiva. El estado inactivo y la detención automática usan ventanas diferentes: una Campaign sin fecha de finalización se vuelve inactiva después de 11 meses sin actividad, y Braze la detiene automáticamente después de un año.

| Motivo del estado inactivo | Pasos para activar la Campaign |
|---|---|
| El envío único programado ha superado la fecha de envío | Programa un envío futuro |
| La Campaign programada o basada en acciones tiene una fecha de finalización que ha pasado | Extiende la fecha de finalización |
| La Campaign sin fecha de finalización no ha enviado un mensaje, inscrito a un usuario en un grupo de control ni sido editada en 11 meses | Envía un mensaje o edita la Campaign |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cómo mantener activa una Campaign inactiva" }

Las Campaigns de conmutador de características y los experimentos de conmutador de características no se vuelven inactivos ni se detienen automáticamente.

### Campaigns de mensajes dentro de la aplicación {#in-app-message-campaigns}

Las Campaigns de mensajes dentro de la aplicación basadas en acciones se vuelven inactivas después de 30 días sin un envío, inscripción en grupo de control o edición. Una Campaign de mensajes dentro de la aplicación inactiva continúa entregando según su configuración. Dependiendo de tu espacio de trabajo, Braze puede entregarla como un [mensaje dentro de la aplicación con plantilla]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages).

Un envío, inscripción en grupo de control o edición devuelve la Campaign al estado activo y reinicia la ventana de 30 días. La detención automática sigue las reglas de siete días y un año en [Campaigns inactivas](#idle-campaigns), no la ventana de inactividad de 30 días.

## Canvas inactivos {#idle-canvases}

Braze detiene los Canvas inactivos que cumplan cualquiera de estos criterios:

- Un envío único programado ha superado su fecha de envío y [duración máxima]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#maximum-duration) en más de siete días
- Un Canvas programado o basado en acciones con fecha de finalización ha superado su fecha de finalización y duración máxima en más de siete días
- Un Canvas sin fecha de finalización no ha dado entrada a usuarios ni sido editado en más de 12 meses más su duración máxima

Para Canvas sin fecha de finalización, una entrada de usuario o edición reinicia la cuenta regresiva de un año. Cuando Braze detiene Canvas, notifica a los usuarios de la empresa en el panel y por correo electrónico.

La duración máxima de un Canvas es el tiempo más largo posible que un usuario puede tardar en completar ese Canvas. Esta duración incluye las expiraciones de Content Cards y mensajes dentro de la aplicación.

Usa esta tabla para mantener activo un Canvas inactivo. El estado inactivo y la detención automática usan ventanas diferentes: un Canvas sin fecha de finalización se vuelve inactivo después de 11 meses más su duración máxima sin actividad, y Braze lo detiene automáticamente después de 12 meses más su duración máxima.

| Motivo del estado inactivo | Pasos para activar el Canvas |
|---|---|
| El envío único programado ha superado la fecha de envío y la duración máxima | Programa un envío futuro |
| El Canvas programado o basado en acciones tiene una fecha de finalización y duración máxima que han pasado | Extiende la fecha de finalización |
| El Canvas sin fecha de finalización no ha dado entrada a usuarios ni sido editado en 11 meses más su duración máxima | Da entrada a un usuario o edita el Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cómo mantener activo un Canvas inactivo" }

Los Canvas con pasos de conmutador de características no se vuelven inactivos ni se detienen automáticamente.

Para datos de interacción de mensajería en Campaigns y Canvas detenidos, consulta [Acerca de la disponibilidad de datos de interacción de mensajería]({{site.baseurl}}/messaging_interaction_data).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿A qué Campaigns o Canvas se aplica esto? {#what-campaigns-or-canvases-does-this-apply-to}

Esto se aplica a Campaigns y Canvas que ya cumplen los criterios de este artículo, y a los que los cumplan en el futuro.

### ¿Cómo sé si una Campaign o un Canvas está inactivo? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Para encontrar Campaigns y Canvas inactivos, ve a la página de **Campaigns** o **Canvas** y filtra por **Idle**. La fecha en que Braze detendrá la Campaign o el Canvas aparece como una columna en la lista.

![El filtro "Idle" en la página de Campaigns.]({% image_buster /assets/img/idle_filter.png %}){: style="max-width:80%;"}

### ¿Qué sucede si se actualiza una Campaign o un Canvas inactivo? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Si actualizas una Campaign que no ha enviado un mensaje o un Canvas que no ha dado entrada a usuarios, la cuenta regresiva se reinicia.

### ¿Qué sucede con las Campaigns que no han enviado un mensaje en un año (o los Canvas que no han dado entrada a usuarios en un año), pero tienen una fecha de finalización en el futuro? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Braze detiene estas Campaigns y Canvas siete días después de la fecha de finalización a las 4 am UTC.

### ¿Puedo evitar que las Campaigns se detengan automáticamente? {#can-i-prevent-campaigns-from-auto-stopping}

No. La detención automática mantiene activas solo las Campaigns necesarias, lo que reduce el desorden en el panel y mejora el rendimiento. Si necesitas una lista de todas las Campaigns detenidas automáticamente, [envía un ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### ¿Quién recibe notificaciones por correo electrónico sobre Campaigns y Canvas detenidos? {#who-receives-email-notifications-about-stopped-campaigns-and-canvases}

De forma predeterminada, todos los usuarios con permisos de administrador están suscritos a las notificaciones por correo electrónico sobre Campaigns y Canvas detenidos automáticamente. El creador de la Campaign o del Canvas siempre recibe una notificación cuando se detiene. Para gestionar destinatarios, ve a **Configuración** > **Configuración de administrador** > **Preferencias de notificaciones**, luego agrega o elimina destinatarios de **Campaign Automatically Stopped** y **Canvas Automatically Stopped**.

### ¿Cómo funciona la detención de Content Cards? {#how-does-stopping-content-cards-work}

Las Content Cards en Campaigns no se detienen hasta su fecha límite de expiración y el periodo de espera correspondiente. Braze las detiene en la fecha más tardía entre el periodo de espera (envío único, fecha de finalización o sin fecha de finalización) y la fecha límite de expiración.

Por ejemplo, si una Content Card expira el 1 de abril, es un envío único y tiene una fecha límite de conversión de 10 días, Braze la detiene el 12 de abril (10 días después de la fecha límite de conversión, más un día). Si una Content Card expira el 1 de abril, es activada por API y no ha enviado mensajes desde el 15 de marzo, expira el 15 de marzo del año siguiente.

Los Canvas se detienen solo después de que sus Content Cards se detengan, lo que significa que su duración máxima ha pasado.

### Tengo un experimento de conmutador de características en mi Canvas. Después de configurar mi conmutador de características, ¿el Canvas permanece activo? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-does-the-canvas-remain-active}

Sí. Los Canvas con pasos de conmutador de características no se detienen automáticamente ni se vuelven inactivos. Las Campaigns de conmutador de características y los experimentos de conmutador de características siguen la misma excepción.

### ¿Por qué aparecen Campaigns inactivas cuando filtro la lista de Campaigns solo por activas? {#why-do-idle-campaigns-appear-when-i-filter-the-campaign-list-to-active-only}

Las Campaigns inactivas se consideran activas hasta que se detienen.

### ¿Una Campaign está inactiva si todavía envía notificaciones push? {#is-a-campaign-idle-if-its-still-sending-push-notifications}

No. Una Campaign aparece como inactiva cuando ya no está enviando mensajes de forma activa.