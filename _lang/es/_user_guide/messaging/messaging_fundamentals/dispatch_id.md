---
nav_title: Comportamiento del ID de envío
article_title: Comportamiento del ID de envío
page_order: 5.2
page_type: reference
description: "En este artículo de referencia se describe el comportamiento del ID de envío para Campaigns, Canvas, Liquid y Currents."
---

# Comportamiento del ID de envío {#dispatch-id-behavior}

> El `dispatch_id` es un ID único para cada envío de mensaje, o "transmisión", enviado desde Braze.

## Comportamiento del ID de envío en Campaigns {#dispatch-id-behavior-in-campaigns}

Los mensajes de Campaigns programados reciben el mismo `dispatch_id`. Los mensajes de Campaigns basados en acciones o desencadenados por la API pueden tener un `dispatch_id` único por usuario, o el `dispatch_id` puede ser el mismo para varios usuarios cuando se envían muy cerca o en la misma llamada a la API. Por ejemplo, dos usuarios de la audiencia de tu campaña programada tendrán el mismo `dispatch_id` cada vez que se programe la campaña. Sin embargo, dos usuarios de la audiencia de una campaña desencadenada por la API pueden tener ID de envío diferentes si las campañas se enviaron en llamadas a la API separadas y no muy cerca una de otra.

Las Campaigns multicanal tienen el mismo comportamiento para su tipo de entrega.

{% alert warning %}
Se genera un `dispatch_id` de forma aleatoria para todos los pasos en Canvas porque Braze trata los pasos en Canvas como eventos desencadenados, incluso cuando están "programados". Esto puede dar lugar a inconsistencias al generar los ID. A veces, un componente de Canvas tiene un `dispatch_id` único por usuario por envío, o puede tener ID de envío compartidos entre usuarios por envío.
{% endalert %}

## Incluir el ID de envío en los mensajes con Liquid {#template-dispatch-id-into-messages-with-liquid}

Si quieres rastrear el envío de un mensaje desde dentro del propio mensaje (en una URL, por ejemplo), puedes incluir el `dispatch_id` mediante una plantilla. Puedes encontrar el formato para esto en Atributos de Canvas en la lista de [etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

Esto se comporta como `api_id`: dado que el `api_id` no está disponible en el momento de la creación de la campaña, Braze lo incluye como un marcador de posición que se previsualiza como `dispatch_id_for_unsent_campaign`. El ID se genera antes de que se envíe el mensaje y se incluye en el momento del envío.

{% alert warning %}
La plantilla Liquid de `dispatch_id_for_unsent_campaign` no funciona con mensajes dentro de la aplicación, ya que los mensajes dentro de la aplicación no tienen un `dispatch_id`.
{% endalert %}

## Campo de ID de envío en Currents para correo electrónico {#dispatch-id-currents-field-for-email}

El campo `dispatch_id` está disponible en los eventos de correo electrónico de Currents en todos los tipos de conector. El `dispatch_id` es el ID único generado para cada transmisión, o envío, realizado desde la plataforma Braze.

Mientras que todos los clientes a los que se envía un mensaje programado reciben el mismo `dispatch_id`, los clientes que reciben mensajes basados en acciones o desencadenados por la API reciben un `dispatch_id` único por mensaje. El campo `dispatch_id` te permite identificar qué instancia de una campaña recurrente es responsable de la conversión, para que puedas ver qué tipos de campañas generan resultados.

Puedes usar `dispatch_id` como una [etiqueta de personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#supported-personalization-tags), en [eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/), o cuando uses [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) o [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) para Currents.