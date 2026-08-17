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

- Calentar direcciones IP nuevas por primera vez
- Calentar nuevas unidades de negocio o marcas con nuevos subdominios
- Recalentar IPs existentes para mejorar la capacidad de entrega
- Recalentar para proveedores de buzón específicos para mejorar la capacidad de entrega

Para los pasos de configuración y requisitos previos, consulta [Calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming).

## ¿Con cuánta anticipación debe establecerse la fecha de inicio? {#how-far-in-advance-must-the-start-date-be}

La fecha de inicio debe ser mañana o posterior en la zona horaria de tu espacio de trabajo (o la zona horaria de la empresa si el espacio de trabajo no tiene una configuración personalizada).

Braze crea Campaigns a medianoche en esa zona horaria para el día actual y el día siguiente (de 0 a 1 días antes del envío). Lanzar un plan también crea las Campaigns próximas de inmediato.

## ¿Cuántas plantillas se necesitan? {#how-many-templates-are-required}

Braze calcula el mínimo a partir de los volúmenes de envío planificados y los usuarios con correo electrónico habilitado en los Segments seleccionados (no el tamaño total del Segment). Proporciona más plantillas que el mínimo para que el sistema pueda ajustarse ante problemas de capacidad de entrega sin detenerse. Para más detalles, consulta [Paso 3: Seleccionar los mensajes a enviar]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## ¿Puedo usar el mismo Segment para múltiples intentos de calentamiento? {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

Dentro de un solo plan activo, Braze excluye automáticamente a los usuarios que ya recibieron envíos previos de calentamiento de IP para la misma plantilla. Si detienes un plan e inicias uno nuevo que reutiliza los mismos Segments, añade un filtro para excluir a los usuarios que recibieron Campaigns del plan anterior.

## ¿Puedo iniciar el calentamiento de IP a mitad de la programación? {#can-i-start-ip-warming-mid-schedule}

El calentamiento de IP automatizado siempre construye la programación desde el inicio de la rampa. Para aproximar un inicio a mitad de la programación, establece **Volumen de envío diario actual** en un valor mayor que 0 que coincida con tu volumen actual. Cuando el volumen actual es mayor que 0, Braze no aplica el escalado por cantidad de IPs al día 1.

## ¿Qué zona horaria se usa para los envíos? {#what-time-zone-is-used-for-sending}

Los envíos usan la zona horaria del espacio de trabajo cuando se ha configurado una; de lo contrario, usan la zona horaria de la empresa. Las Campaigns no se crean en la zona horaria local de cada usuario. Para enviar en hora local, actualiza manualmente las Campaigns creadas por el plan.

## ¿Cuántos planes de calentamiento de IP pueden ejecutarse al mismo tiempo? {#how-many-ip-warming-plans-can-run-at-the-same-time}

Si tu espacio de trabajo admite múltiples planes, más de un plan puede ejecutarse de forma concurrente. Para más detalles, consulta [Calentamiento de IP múltiple]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming).

## ¿Cómo escala el volumen para pools de IP con múltiples IPs? {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

Cuando **Volumen de envío diario actual** es 0, el día 1 comienza con el menor entre 50 envíos por IP o 500 en total. Luego, el volumen crece aproximadamente 1,75 veces por día de envío, sujeto a las protecciones de la rampa. Por ejemplo, con 10 IPs: 500 → 875 → 1.532 → 2.681.

Si estableces un volumen actual personalizado mayor que 0, el escalado por cantidad de IPs no se aplica al día 1. Para más información sobre planes con múltiples IPs, consulta [Calentar múltiples IPs en un pool]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool).

## ¿El calentamiento de IP automatizado admite límites de velocidad por Campaign? {#does-automated-ip-warming-support-rate-limiting-per-campaign}

No. Cada Campaign se envía a la hora configurada sin un límite de velocidad por Campaign.

## ¿Cuándo retiene Braze el volumen durante el calentamiento de IP? {#when-does-braze-hold-volume-during-ip-warming}

Braze evalúa la capacidad de entrega de las Campaigns que se enviaron entre 12 y 20 horas antes. Si las tasas de entrega, apertura, rebote o informes de correos no deseados superan los puntos de referencia en [Durante el calentamiento de IP activo]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming), Braze retiene el volumen para el siguiente día de envío en lugar de aumentarlo.

## ¿Qué sucede cuando se retiene el volumen? {#what-happens-when-volume-is-held}

La retención de volumen es el ajuste automático que Braze aplica cuando se superan esos umbrales. El siguiente envío programado mantiene el mismo volumen en lugar de avanzar. Braze replanifica las entradas futuras de la programación, archiva las Campaigns futuras existentes del plan y crea nuevas Campaigns para la programación actualizada de inmediato. El plan puede tardar más en alcanzar el volumen objetivo.

## ¿Por qué las ediciones de Campaigns no aparecen en el rastreador de calentamiento de IP? {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

Los cambios que realizas en las Campaigns creadas por el calentamiento de IP automatizado (como programación, Segment o volumen) no se sincronizan de vuelta con el rastreador de calentamiento de IP. Para notas de configuración relacionadas, consulta [Paso 3: Seleccionar los mensajes a enviar]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## ¿Puedo detener un plan de calentamiento de IP? {#can-i-stop-an-ip-warming-plan}

Sí. Detener un plan lo finaliza de forma permanente: Braze desactiva las Campaigns vinculadas y no crea futuras. No puedes reanudar un plan detenido; crea un nuevo plan para continuar. Para los pasos a seguir después de una detención, consulta [Detener un plan de calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan).

## ¿Cuándo se marca un plan de calentamiento de IP como completado? {#when-is-an-ip-warming-plan-marked-as-complete}

El plan se marca como completado después de que finaliza el último día de envío programado, a medianoche en la zona horaria efectiva (espacio de trabajo o empresa). Por ejemplo, si la última Campaign se envía a las 8 pm, el plan se marca como completado a medianoche, cuatro horas después.

## ¿Qué datos puedo descargar? {#what-data-can-i-download}

La exportación CSV incluye filas por Campaign con métricas a nivel diario: *Sent*, *Delivered*, *Bounces*, *Spam Reports*, *Total opens*, *Unique Opens*, *Clicked* y *Unsubscribed*. La tabla del rastreador agrupa múltiples Campaigns del mismo día en una vista diaria. Para más información, consulta [Cuando se completa un calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes).