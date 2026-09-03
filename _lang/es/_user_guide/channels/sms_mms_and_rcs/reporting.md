---
nav_title: "Informes"
article_title: "Informes"
page_order: 21
description: "Este artículo de referencia cubre las métricas de SMS, MMS y RCS utilizadas en Braze, así como cómo verlas en tus campañas de SMS, MMS y RCS."
alias: /sms_mms_rcs_reporting/
page_type: reference
tool:
  - Reports
channel:
  - SMS
  - MMS
  - RCS


---

# Informes de SMS, MMS y RCS {#reporting-for-sms-mms-and-rcs}

> Este artículo de referencia cubre las métricas de SMS, MMS y RCS utilizadas en Braze, así como cómo verlas en tus campañas de SMS, MMS y RCS.

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

{% alert note %}
Las métricas de clics del panel, como *Total de clics*, excluyen la actividad sospechosa de bots, pero Currents sigue exportando todos los eventos de clic con `is_suspected_bot_click` y `suspected_bot_click_reason` para la reconciliación en el almacén de datos. Para las métricas afectadas del panel, la segmentación y la orquestación, consulta [Filtrado de clics de bots para enlaces de SMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering).
{% endalert %}

## Rastrear adhesiones voluntarias y cancelaciones de suscripción de SMS {#track-sms-opt-ins-and-opt-outs}

Puedes rastrear las adhesiones voluntarias y cancelaciones de suscripción de SMS con los siguientes métodos:

| Método | Descripción |
|--------|-------------|
| Segmentador | El segmentador muestra el número de usuarios en un [grupo de suscripción]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group) específico. No deduplica por número de teléfono: si varios usuarios comparten el mismo número de teléfono, cada instancia se cuenta por separado. |
| Serie temporal del grupo de suscripción | Proporciona una instantánea diaria de las suscripciones para correo electrónico y números de teléfono. La serie temporal cuenta suscripciones, cancelaciones de suscripción y resuscripciones. Por ejemplo, si un usuario se suscribe, cancela su suscripción y luego se vuelve a suscribir, se cuenta como un usuario suscrito. |
| Currents | Usa Currents para exportar [eventos de suscripción y participación]({{site.baseurl}}/message_events_glossary) para tus propios informes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rastrear adhesiones voluntarias y cancelaciones de suscripción de SMS" }

{% alert note %}
Las estadísticas de _adhesión voluntaria_ y _cancelación de suscripción_ en el panel **SMS/MMS/RCS Performance** reflejan los usuarios que se suscriben o cancelan su suscripción a través de palabras clave entrantes (por ejemplo, enviar "START" para la adhesión voluntaria o "STOP" para la cancelación de suscripción). Estos números suelen ser más bajos que los que se muestran en el segmentador, ya que cuentan la cantidad de veces que se enviaron estas palabras clave, no el número total de usuarios suscritos a SMS.
{% endalert %}

### Rastrear cancelaciones de suscripción de SMS a nivel de campaña {#track-sms-campaign-opt-outs}

Rastrea las cancelaciones de suscripción de SMS a nivel de Campaign usando la tabla de recepción entrante en lugar de la tabla de cambio de estado del grupo de suscripción. Por ejemplo, en [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) o en tu almacén de datos, puedes ejecutar una consulta que haga referencia a la tabla `USERS_MESSAGES_SMS_INBOUNDRECEIVE` o [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED).

Esta consulta de ejemplo hace referencia a la tabla `USERS_MESSAGES_SMS_INBOUNDRECEIVE`:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

Esto devuelve los usuarios que cancelaron su suscripción a las comunicaciones por SMS para el espacio de trabajo y grupo de suscripción especificados, filtrados a los asociados con Campaigns o Canvas.

### Momento de la cancelación de suscripción {#opt-out-timing}

Los eventos de palabras clave y mensajes entrantes en Currents o en tu almacén de datos, como las marcas de tiempo en [`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) o los eventos de cambio de estado del grupo de suscripción, son la fuente autorizada del momento en que Braze registró la cancelación de suscripción.

{% alert note %}
Las marcas de tiempo de los eventos reflejan cuándo Braze recibió o procesó el mensaje entrante, no necesariamente cuándo el usuario envió el SMS o cuándo un operador o proveedor de SMS lo recibió. Si tu análisis trata las cancelaciones de suscripción como el momento en que Braze procesó la ruta de cancelación de suscripción entrante, estas marcas de tiempo coinciden con esa definición.
{% endalert %}

El perfil de usuario muestra el estado de suscripción actual, pero puede que no muestre un campo único de "SMS cancelado en" a menos que configures un [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) o similar al procesar las cancelaciones de suscripción.

## Cargos aplicados a los resultados del envío de SMS {#charges-applied-to-sms-sending-outcomes}

Esta tabla refleja la facturación de Braze, no la de tu proveedor. Los resultados que Braze no cobra pueden ser cobrados por tu proveedor.

| Resultado | Definición | Cobrado por Braze |
|--------|------------|--------|
| Enviado | Se ha lanzado o desencadenado un paso en Campaign o Canvas, y se ha enviado una carga útil del SMS al proveedor de SMS. | Sin cargo |
| Entrega fallida | La carga útil del SMS no pudo enviarse al proveedor de SMS. Esto puede ocurrir debido a colas desbordadas, cuentas suspendidas o errores de medios (en el caso de MMS). | Sin cargo |
| Entregado | El proveedor de SMS recibió confirmación de entrega del mensaje por parte del operador ascendente (y, cuando está disponible, del dispositivo de destino). | Cargo |
| Rechazado | El proveedor de SMS recibió un acuse de recibo de rechazo indicando que el mensaje no se entregó. Esto puede ocurrir por varias razones, como el filtrado de contenido del operador o la disponibilidad del dispositivo de destino. | Cargo |
| **Envíos al operador** | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} Obsoleto para paneles nuevos. Algunos paneles pueden seguir etiquetando esta métrica como **Sent to Carrier**. | Se pueden aplicar cargos según los resultados de envío de cada mensaje individual |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cargos aplicados a los resultados del envío de SMS" }

{% alert note %}
**Envíos al operador** está obsoleto para paneles nuevos. Utiliza **Sent**, **Confirmed Delivery**, **Delivery Failed** y **Rejections** para los informes actuales. Consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary) para ver las definiciones.
{% endalert %}

## Informes de alternativa de RCS y SMS {#rcs-and-sms-fallback-reporting}

Para conocer el comportamiento de los eventos de alternativa de SMS en RCS (incluido `IS_SMS_FALLBACK=TRUE`), consulta [Cómo funciona la alternativa de SMS con los eventos y la segmentación]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup#how-sms-fallback-works-with-events-and-segmentation).

{% alert note %}
Los análisis de Campaigns en el panel y las exportaciones de Snowflake pueden diferir ligeramente en temporización y agregación. Para la conciliación en el almacén de datos, considera los flujos de eventos de Snowflake o Currents como la fuente más granular cuando las métricas no coincidan exactamente con el panel.
{% endalert %}

## Reconciliar *Rechazos* con Snowflake o Currents {#reconcile-rejections-with-snowflake-or-currents}

La métrica *Rechazos* en el panel es un recuento agregado del espacio de trabajo. No es una exportación a nivel de fila, por lo que no siempre puedes hacer coincidir cada rechazo con una sola fila en Snowflake o con un solo evento `users.messages.sms.Rejection` en Currents. Por ejemplo, si el perfil de usuario se eliminó antes de que Braze terminara de procesar el rechazo para la exportación al almacén de datos, ese rechazo no aparece en tu tabla `USERS_MESSAGES_SMS_REJECTION_SHARED` ni en la carga útil de Currents, mientras que los informes agregados de SMS sí pueden reflejar el resultado. Para más información, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles) y los [eventos de rechazo de SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) en el glosario de eventos de Currents.