---
nav_title: "Campaigns y Canvas inactivos"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Campaigns y Canvas inactivos {#idle-campaigns-and-canvases}

> Este artículo de referencia explica el estado inactivo de Campaigns y Canvas y responde a las preguntas más frecuentes.

{% alert note %}
En 2024, los Canvas se marcarán como **Inactivos** y se detendrán, de forma similar a las Campaigns. Cuando los Canvas estén inactivos o detenidos, seguirán la lógica descrita en este documento.
{% endalert %}

A las Campaigns y los Canvas se les asigna un estado inactivo cuando no han enviado mensajes ni han ingresado usuarios durante un tiempo. Estas Campaigns y Canvas se detendrán automáticamente en sus fechas de detención asociadas. Puedes filtrar por Campaigns y Canvas inactivos para ayudarte a ordenar y gestionar tu lista de Campaigns y Canvas.

Las Campaigns y los Canvas con fechas de finalización y envíos únicos están inactivos durante 7 días antes de detenerse automáticamente. Las Campaigns y los Canvas que no han enviado un mensaje en 11 meses están inactivos durante 1 mes antes de detenerse automáticamente.

## Campaigns inactivas {#idle-campaigns}

De forma continua, las Campaigns inactivas que cumplan los siguientes criterios se detendrán:

- Un envío único planificado ha superado su fecha de envío en siete días
- Una Campaign planificada o basada en acciones con una fecha de finalización ha superado su fecha de finalización en siete días
- Una Campaign sin fecha de finalización que no ha enviado mensajes en un año

Para las Campaigns sin fechas de finalización, si se envía un mensaje o se actualiza la Campaign, la cuenta regresiva de un año para detener la Campaign se reiniciará. Cuando las Campaigns se detengan, Braze notificará a los clientes en su dashboard y por correo electrónico.

Las Campaigns se detendrán en la fecha más tardía entre la fecha de detención predeterminada y un día después de su último plazo de conversión vigente. Los envíos que son resultado de una variante ganadora o variante personalizada se tratan como envíos planificados y se detendrán siete días después de que se envíe la variante ganadora o personalizada. Todas las Campaigns se detendrán a las 4 am UTC todos los días para todos los usuarios de Braze.

Las Content Cards no se detendrán hasta su plazo de expiración, y también cumplirán con los criterios mencionados anteriormente, así como con la regla del plazo de conversión.

Consulta esta tabla para saber cómo mantener activa una Campaign inactiva:

| Motivo del estado inactivo                                                                              | Pasos para activar la Campaign                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Campaigns que son envíos únicos planificados y han superado la fecha de envío                 | Planifica un envío futuro                            |
| Campaigns que son planificadas o basadas en acciones, tienen fechas de finalización y han superado la fecha de finalización | Extiende la fecha de finalización                               |
| Campaigns sin fecha de finalización que no han enviado mensajes en un año                                | Envía un mensaje o realiza cualquier edición en la Campaign |
| Campaigns con fechas de finalización y envíos únicos | Planifica un envío futuro |
| Campaigns que no han enviado un mensaje en 11 meses | Envía un mensaje o realiza cualquier edición en la Campaign |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Campaigns de mensajes dentro de la aplicación {#in-app-message-campaigns}

Si una Campaign de mensajes dentro de la aplicación no tiene impresiones y no se ha editado durante más de 30 días, se convierte en una Campaign inactiva. Una Campaign de mensajes dentro de la aplicación inactiva continúa entregando según su configuración, pero el mensaje dentro de la aplicación se convierte en un mensaje dentro de la aplicación con plantilla.

Si tus usuarios desencadenan un evento de impresión o el especialista en marketing edita la Campaign, la Campaign vuelve al estado activo y el contador de 30 días se reinicia.

## Canvas inactivos {#idle-canvases}

De forma continua, los Canvas inactivos que cumplan los siguientes criterios se detendrán:

- Un envío único planificado ha superado su fecha de envío y duración máxima en más de 7 días
- Un Canvas planificado o basado en acciones con una fecha de finalización ha superado su fecha de finalización y duración máxima en más de 7 días
- Un Canvas sin fecha de finalización no ha ingresado usuarios ni se ha editado en más de 12 meses y su duración máxima

Para los Canvas sin fechas de finalización, si un usuario ingresa o el Canvas se actualiza, la cuenta regresiva de un año para detener el Canvas se reiniciará. Cuando los Canvas se detengan, Braze notificará a los clientes en su dashboard y por correo electrónico.

La [duración máxima](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) de un Canvas es el tiempo más largo posible que un usuario puede tardar en completar un Canvas determinado. Esta duración incluye las expiraciones de Content Cards y mensajes dentro de la aplicación.

Consulta esta tabla para saber cómo mantener activo un Canvas inactivo:

| Motivo del estado inactivo                                                                                                  | Pasos para activar el Canvas                     |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Canvas que son envíos únicos planificados y la duración máxima ha superado la fecha de envío                 | Planifica un envío futuro                          |
| Canvas que son planificados o basados en acciones, tienen fechas de finalización y la duración máxima ha superado la fecha de finalización | Extiende la fecha de finalización                             |
| Canvas sin fechas de finalización que no han enviado mensajes en un año                                                      | Envía un mensaje o realiza cualquier edición en el Canvas |
| Canvas con fechas de finalización y envíos únicos | Planifica un envío futuro |
| Canvas que no han enviado un mensaje en 11 meses | Envía un mensaje o realiza cualquier edición en el Canvas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si no hay una opción para restaurar los datos de interacción, esto puede deberse a que:

- La restauración u otra operación relacionada con datos de interacción está actualmente en curso.
- No existían datos de interacción para este Canvas.
- Si el Canvas se creó antes de 2021, los datos pueden haberse eliminado permanentemente según la política anterior.

## Preguntas frecuentes {#frequently-asked-questions}

#### ¿A qué Campaigns o Canvas se aplica esto? {#what-campaigns-or-canvases-does-this-apply-to}

Esto se aplicará a las Campaigns y los Canvas que ya cumplen con los criterios mencionados anteriormente, y a las Campaigns y los Canvas que cumplirán con los criterios en el futuro.

#### ¿Cómo sé si una Campaign o un Canvas está inactivo? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Las Campaigns y los Canvas inactivos se mostrarán en las páginas de lista de Campaigns y Canvas bajo la categoría **Inactivo**. La fecha en la que la Campaign o el Canvas se detendrá aparece como una columna en la lista.

![El filtro "Inactivo" en la página "Campaigns".][1]{: style="max-width:60%;"}

#### ¿Qué sucede si se actualiza una Campaign o un Canvas inactivo? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Si se actualiza una Campaign que no ha enviado un mensaje o un Canvas que no ha ingresado usuarios, la cuenta regresiva se reiniciará.

#### ¿Qué sucede con las Campaigns que no han enviado un mensaje en un año (o los Canvas que no han ingresado usuarios en un año), pero tienen una fecha de finalización en el futuro? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Detendremos estas Campaigns y Canvas siete días después de la fecha de finalización a las 4 am UTC.

##### ¿Puedo evitar que las Campaigns se detengan automáticamente? {#can-i-stop-campaigns-from-automatically-stopping}

No. Esto ayuda a mantener activas solo las Campaigns necesarias para que los dashboards estén menos saturados y mejorar el rendimiento. Si deseas una lista de todas las Campaigns detenidas automáticamente, [envía un ticket de soporte](https://www.braze.com/docs/help/support) para que te la proporcionen.

#### ¿Quién recibirá notificaciones por correo electrónico sobre las Campaigns y los Canvas detenidos? {#who-will-receive-email-notifications-about-stopped-campaigns-and-canvases}

De forma predeterminada, todos los usuarios con permisos de administrador están suscritos a las notificaciones por correo electrónico sobre la detención automática de Campaigns y Canvas. El creador de la Campaign o el Canvas siempre será notificado cuando se detenga. Los usuarios pueden gestionar las preferencias de notificación por correo electrónico yendo a **Configuración de empresa** > **Preferencias de notificación**, y luego añadiendo o eliminando destinatarios de la notificación **Campaign Automatically Stopped** y la notificación **Canvas Automatically Stopped**.

#### ¿Cómo funciona la detención de Content Cards? {#how-does-stopping-content-cards-work}

Las Content Cards en Campaigns no se detendrán hasta su plazo de expiración y el período de espera correspondiente. Se detendrán en la fecha más tardía entre el período de espera (correspondiente a si la Campaign es un envío único, tiene una fecha de finalización o no tiene una fecha de finalización) y el plazo de expiración.

Por ejemplo, si una Content Card expira el 1 de abril, es un envío único y tiene un plazo de conversión de 10 días, se detendrá el 12 de abril (10 días después del plazo de conversión, más un día). Si una Content Card expira el 1 de abril, se desencadena por API y no ha enviado mensajes desde el 15 de marzo, expirará el 15 de marzo del año siguiente.

Los Canvas solo se detienen después de que las Content Cards se detengan, lo que significa que su duración máxima ha pasado.

#### Tengo un experimento de conmutador de características en mi Canvas. Después de configurar mi conmutador de características, ¿el Canvas permanecerá activo? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-will-the-canvas-remain-active}

Los Canvas con pasos de conmutador de características no se detienen automáticamente y no se vuelven inactivos.

#### ¿Por qué veo Campaigns inactivas en mi lista de Campaigns cuando apliqué un filtro para mostrar solo las Campaigns activas? {#why-am-i-seeing-idle-campaigns-displayed-in-my-campaigns-list-when-i-applied-a-filter-to-show-active-campaigns-only}

Las Campaigns inactivas se consideran activas hasta que se detienen.

#### ¿Se listaría una Campaign como inactiva cuando todavía está enviando notificaciones push? {#would-a-campaign-be-listed-as-idle-when-its-still-sending-push-notifications}

No. Una Campaign se listará como inactiva cuando ya no esté enviando mensajes activamente.

[1]: {% image_buster /assets/unlisted_docs/img/idle_filter.png %}