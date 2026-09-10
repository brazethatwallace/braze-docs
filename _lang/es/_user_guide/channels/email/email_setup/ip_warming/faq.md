---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre el calentamiento de IP automatizado
channel: email
page_order: 3
description: "Respuestas a las preguntas frecuentes sobre el calentamiento de IP automatizado en Braze."
---

# Preguntas frecuentes sobre el calentamiento de IP automatizado {#automated-ip-warming-faq}

> Respuestas a las preguntas frecuentes sobre el [calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming). Para conceptos sobre el calentamiento de IP y programaciones manuales, consulta [Calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming).

## ¿Cuándo debo usar el calentamiento de IP automatizado? {#when-should-i-use-automated-ip-warming}

Usa el calentamiento de IP automatizado cuando necesites:

- Calentar nuevas direcciones IP por primera vez
- Calentar nuevas unidades de negocio o marcas con nuevos subdominios
- Recalentar IPs existentes para mejorar la capacidad de entrega
- Recalentar para proveedores de buzón de correo específicos para mejorar la capacidad de entrega

Para conocer los pasos de configuración y los requisitos previos, consulta [Calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming).

## ¿Con cuánta antelación debe establecerse la fecha de inicio? {#how-far-in-advance-must-the-start-date-be}

La fecha de inicio debe ser mañana o posterior en la zona horaria de tu espacio de trabajo (o la zona horaria de la empresa si el espacio de trabajo no tiene una anulación configurada).

Braze crea Campaigns a medianoche en esa zona horaria para el día actual y el día siguiente (de 0 a 1 días antes del envío). Lanzar un plan también crea las próximas Campaigns de forma inmediata.

## ¿Cuántas plantillas se necesitan? {#how-many-templates-are-required}

Braze calcula el mínimo a partir de los volúmenes de envío planificados y los usuarios con correo electrónico habilitado en los Segments seleccionados (no el tamaño total del Segment). Proporciona más plantillas que el mínimo para que el sistema pueda ajustarse ante problemas de capacidad de entrega sin detenerse. Para más detalles, consulta [Paso 3: Seleccionar los mensajes a enviar]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## ¿Puedo usar el mismo Segment para varios intentos de calentamiento? {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

Dentro de un único plan activo, Braze excluye automáticamente a los usuarios que ya recibieron envíos previos de calentamiento de IP para la misma plantilla. Si detienes un plan e inicias uno nuevo que reutiliza los mismos Segments, añade un filtro para excluir a los usuarios que recibieron Campaigns del plan anterior.

## ¿Puede un usuario recibir más de una plantilla de correo electrónico en el mismo día? {#can-a-user-receive-more-than-one-email-template-on-the-same-day}

Sí. Braze excluye a los usuarios que ya recibieron una plantilla determinada dentro del plan, pero los usuarios que recibieron una plantilla diferente siguen siendo elegibles. Cuando la audiencia disponible para la programación de un día se agota, el plan vuelve a recorrer tus plantillas y algunos usuarios reciben una segunda plantilla ese día.

Esto ocurre cuando el número total de usuarios a los que se les puede enviar correo electrónico en los Segments seleccionados es menor que tu **Volumen de envío objetivo**, lo cual suele suceder en el último día o los últimos días del plan. Por ejemplo, con 400.000 usuarios con correo electrónico disponible y un volumen de envío objetivo de 600.000, aproximadamente 200.000 usuarios reciben dos plantillas el último día. Para evitar esto, mantén tu número total de usuarios con correo electrónico disponible igual o superior a tu volumen de envío objetivo. Para más información, consulta [Tamaño de la audiencia y múltiples envíos por usuario]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#audience-size-and-multiple-sends-per-user).

## ¿Puedo iniciar el calentamiento de IP a mitad de la programación? {#can-i-start-ip-warming-mid-schedule}

El calentamiento de IP automatizado siempre construye la programación desde el inicio de la rampa. Para aproximar un inicio a mitad de la programación, establece **Volumen de envío diario actual** con un valor mayor que 0 para que coincida con tu volumen actual. Cuando el volumen actual es mayor que 0, Braze no aplica el escalado por número de IP al día 1.

## ¿Qué zona horaria se utiliza para los envíos? {#what-time-zone-is-used-for-sending}

Los envíos utilizan la zona horaria del espacio de trabajo cuando se ha configurado una; de lo contrario, utilizan la zona horaria de la empresa. Las Campaigns no se crean en la zona horaria local de cada usuario. Para enviar en la hora local, actualiza manualmente las Campaigns creadas por el plan.

## ¿Cuántos planes de calentamiento de IP pueden ejecutarse al mismo tiempo? {#how-many-ip-warming-plans-can-run-at-the-same-time}

Se puede ejecutar más de un plan de forma simultánea. Para más detalles, consulta [Calentamiento de IP múltiple]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming).

## ¿Cómo escala el volumen en los pools de IP con múltiples IP? {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

Cuando el **volumen de envío diario actual** es 0, el día 1 comienza con el menor entre 50 envíos por IP o 500 en total. Luego, el volumen crece aproximadamente 1,75 veces por día de envío, sujeto a las protecciones de rampa. Por ejemplo, con 10 IP: 500 → 875 → 1.532 → 2.681.

Si estableces un volumen actual personalizado mayor que 0, el escalado por cantidad de IP no se aplica al día 1. Para más información sobre planes con múltiples IP, consulta [Calentar múltiples IP en un solo pool]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool).

## ¿El calentamiento de IP automatizado admite límites de velocidad por Campaign? {#does-automated-ip-warming-support-rate-limiting-per-campaign}

No. Cada Campaign se envía en el momento configurado sin un límite de velocidad por Campaign.

## ¿Cuándo retiene Braze el volumen durante el calentamiento de IP? {#when-does-braze-hold-volume-during-ip-warming}

Braze evalúa la capacidad de entrega de las Campaigns enviadas entre 12 y 20 horas antes. Si las tasas de entrega, apertura, rebote o informes de correos no deseados superan los puntos de referencia en [Durante el calentamiento de IP activo]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming), Braze retiene el volumen para el siguiente día de envío en lugar de aumentarlo.

## ¿Qué sucede cuando se retiene el volumen? {#what-happens-when-volume-is-held}

La retención de volumen es el ajuste automático que Braze aplica cuando se superan esos umbrales. El siguiente envío programado mantiene el mismo volumen en lugar de avanzar. Braze replanifica las entradas futuras del calendario, archiva las Campaigns futuras existentes del plan y crea nuevas Campaigns para el calendario actualizado de inmediato. El plan puede tardar más en alcanzar el volumen objetivo.

## ¿Por qué las ediciones de las campañas no aparecen en el rastreador de calentamiento de IP? {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

Los cambios que realices en las campañas creadas por el calentamiento de IP automatizado (como la programación, el Segment o el volumen) no se sincronizan con el rastreador de calentamiento de IP. Para notas de configuración relacionadas, consulta el [Paso 3: Seleccionar los mensajes a enviar]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## ¿Puedo detener un plan de calentamiento de IP? {#can-i-stop-an-ip-warming-plan}

Sí. Detenerlo finaliza permanentemente el plan: Braze desactiva las Campaigns vinculadas y no crea futuras. No puedes reanudar un plan detenido; crea un nuevo plan para continuar. Para conocer los pasos a seguir después de una detención, consulta [Detener un plan de calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan).

## ¿Cuándo se marca como completado un plan de calentamiento de IP? {#when-is-an-ip-warming-plan-marked-as-complete}

El plan se marca como completado cuando termina el último día de envío programado, a medianoche en la zona horaria vigente (espacio de trabajo o empresa). Por ejemplo, si la última Campaign se envía a las 8 pm, el plan se marca como completado a medianoche, cuatro horas después.

## ¿Qué datos puedo descargar? {#what-data-can-i-download}

La exportación CSV incluye filas por Campaign con métricas a nivel diario: *Sent*, *Delivered*, *Bounces*, *Spam Reports*, *Total opens*, *Unique Opens*, *Clicked* y *Unsubscribed*. La tabla de seguimiento agrupa varias Campaigns del mismo día en una vista diaria. Para más información, consulta [Cuando se completa un calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes).