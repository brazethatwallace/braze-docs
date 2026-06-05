---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre límites de velocidad y limitación de frecuencia
page_order: 0
page_type: FAQ
description: "Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los límites de velocidad y la limitación de frecuencia."
tool: Campaigns

---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los límites de velocidad y la limitación de frecuencia.

### Si cambio la limitación de envío en un Canvas activo, ¿afecta a los usuarios que ya están en el Canvas? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Sí, cuando aumentas o reduces un límite de velocidad de Canvas, el límite actualizado se aplica a los nuevos mensajes. Puede haber un breve retraso antes de que la actualización se refleje en todo el Canvas.

### ¿Qué ocurre si un usuario llega a un paso de mensaje en Canvas pero ha superado el límite de frecuencia global? {#what-happens-if-a-user-reaches-a-canvas-message-step-but-is-over-the-global-frequency-cap}

El usuario no recibe ese envío para el canal limitado, pero sigue las reglas de avance del paso de mensaje. Los pasos de mensaje hacen avanzar a los usuarios cuando un mensaje no se envía debido a la limitación de frecuencia global, de modo que continúan al siguiente paso en Canvas. Para ver la lista completa de casos de avance, consulta [Cómo avanzan los usuarios]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#how-users-advance).

### ¿Cómo puedo identificar a los usuarios que fueron limitados por frecuencia en un Canvas? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Los usuarios que son limitados por frecuencia no generan un evento de envío para ese paso. Para identificar a estos usuarios, puedes usar [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) para rastrear eventos de mensajes abortados donde `abort_type` sea `frequency_capped`. Alternativamente, puedes crear una [Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) para analizar a los usuarios que entraron en el Canvas pero no recibieron el mensaje esperado.

### ¿Cómo se usan los días del calendario y las zonas horarias para los límites de frecuencia global "por día"? {#how-are-calendar-days-and-time-zones-used-for-per-day-global-frequency-caps}

La limitación de frecuencia global utiliza la zona horaria del usuario y cuenta por día del calendario, no por periodos continuos de 24 horas. Para ver un ejemplo, consulta [Reglas de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules).

### ¿Se aplica la limitación de frecuencia global a los mensajes dentro de la aplicación desencadenados? {#does-global-frequency-capping-apply-to-triggered-in-app-messages}

No, la limitación de frecuencia global solo se aplica a mensajes push, correo electrónico, SMS, webhook, WhatsApp y LINE.

### ¿La limitación de frecuencia limita las campañas recibidas o los mensajes individuales dentro de un envío? {#does-frequency-capping-limit-campaigns-received-or-individual-messages-inside-a-send}

La limitación de frecuencia se aplica por despacho: cada envío de Campaign o paso en Canvas cuenta para tus límites, no cada variante o plataforma dentro de un envío. Para más información, consulta [Reglas de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules).

### Si varios mensajes son elegibles al mismo tiempo y solo algunos caben dentro del límite, ¿qué mensajes se envían? {#if-several-messages-are-eligible-at-the-same-time-and-only-some-fit-under-the-cap-which-messages-send}

Braze envía hasta el límite. Cuando varios envíos compiten en la misma ventana, los mensajes que se procesan primero son los que cuentan para el límite. Los envíos restantes en esa ventana quedan limitados.

### ¿Los webhooks fallidos cuentan para el límite de frecuencia global? {#do-failed-webhooks-count-toward-the-global-frequency-cap}

No. Un webhook cuenta para el límite cuando Braze registra una entrega exitosa. Las respuestas de webhook no exitosas (por ejemplo, códigos de estado `4xx` o `5xx`) no cuentan para el límite.