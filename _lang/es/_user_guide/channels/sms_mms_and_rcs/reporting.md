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
Las métricas de clics del panel, como **Total de clics**, excluyen la actividad sospechosa de bots. Para las métricas afectadas, la segmentación, la orquestación y los campos de reconciliación de Currents (`is_suspected_bot_click`, `suspected_bot_click_reason`), consulta [Filtrado de clics de bots para enlaces de SMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering).
{% endalert %}

## Seguimiento de adhesiones y cancelaciones de SMS {#track-sms-opt-ins-and-opt-outs}

Puedes hacer un seguimiento de las adhesiones y cancelaciones de SMS con los siguientes métodos:

| Método | Descripción |
|--------|-------------|
| Segmentador | El segmentador muestra el número de usuarios en un [grupo de suscripción]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group) específico. No deduplica por número de teléfono: si varios usuarios comparten el mismo número de teléfono, cada instancia se cuenta por separado. |
| Serie temporal de grupos de suscripción | Proporciona una instantánea diaria de las suscripciones para correos electrónicos y números de teléfono. La serie temporal cuenta suscripciones, cancelaciones de suscripción y resuscripciones. Por ejemplo, si un usuario se suscribe, cancela su suscripción y luego se vuelve a suscribir, se cuenta como un usuario suscrito. |
| Currents | Usa Currents para exportar [eventos de suscripción y participación]({{site.baseurl}}/message_events_glossary) para tus propios informes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Seguimiento de adhesiones y cancelaciones de SMS" }

{% alert note %}
Las estadísticas de _adhesión voluntaria_ y _cancelación de suscripción_ en el panel **SMS/MMS/RCS Performance** reflejan a los usuarios que se adhieren o cancelan mediante palabras clave entrantes (por ejemplo, enviar "START" para adherirse o "STOP" para cancelar). Estos números suelen ser más bajos que los que se muestran en el segmentador, ya que cuentan el número de veces que se enviaron estas palabras clave, no el número total de usuarios suscritos a SMS.
{% endalert %}

### Seguimiento de cancelaciones de SMS a nivel de campaña {#track-sms-campaign-opt-outs}

Haz un seguimiento de las cancelaciones de SMS a nivel de Campaign usando la tabla de recepción entrante en lugar de la tabla de cambio de estado del grupo de suscripción. Por ejemplo, en [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) o en tu almacén de datos, puedes ejecutar una consulta que haga referencia a la tabla `USERS_MESSAGES_SMS_INBOUNDRECEIVE` o [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED).

Esta consulta de ejemplo hace referencia a la tabla `USERS_MESSAGES_SMS_INBOUNDRECEIVE`:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

Esto devuelve los usuarios que cancelaron su suscripción a las comunicaciones SMS para el espacio de trabajo y grupo de suscripción indicados, filtrados a aquellos asociados con Campaigns o Canvas.

### Momento de la cancelación {#opt-out-timing}

Los eventos de palabras clave y mensajes entrantes en Currents o en tu almacén de datos, como las marcas de tiempo en [`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) o los eventos de cambio de estado del grupo de suscripción, son la fuente autorizada de cuándo Braze registró la cancelación.

{% alert note %}
Las marcas de tiempo de los eventos reflejan cuándo Braze recibió o procesó el mensaje entrante, no necesariamente cuándo el usuario envió el SMS o cuándo un operador o proveedor de SMS lo recibió. Si tu análisis trata las cancelaciones como el momento en que Braze procesó la ruta de cancelación entrante, estas marcas de tiempo coinciden con esa definición.
{% endalert %}

El perfil de usuario muestra el estado de suscripción actual, pero puede que no muestre un campo único de "SMS cancelado en" a menos que establezcas un [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes) o similar al procesar las cancelaciones.

## Cargos aplicados a los resultados de envío de SMS {#charges-applied-to-sms-sending-outcomes}

Esta tabla refleja la facturación de Braze, no la de tu proveedor. Los resultados que Braze no cobra pueden ser cobrados por tu proveedor.

| Resultado | Definición | Cobrado por Braze |
|--------|------------|--------|
| Enviado | Se ha lanzado o desencadenado una Campaign o un paso en Canvas, y se ha enviado una carga útil del SMS al proveedor de SMS. | Sin cargo |
| Entrega fallida | La carga útil del SMS no pudo enviarse al proveedor de SMS. Esto puede ocurrir debido a colas desbordadas, cuentas suspendidas o errores de medios (en el caso de MMS). | Sin cargo |
| Entregado | El proveedor de SMS recibió confirmación de entrega del mensaje por parte del operador ascendente (y, cuando está disponible, del dispositivo de destino). | Cargo |
| Rechazado | El proveedor de SMS recibió un acuse de rechazo indicando que el mensaje no fue entregado. Esto puede ocurrir por varias razones, como el filtrado de contenido del operador o la disponibilidad del dispositivo de destino. | Cargo |
| **Envíos al operador** | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} Obsoleto para paneles nuevos. Algunos paneles pueden seguir etiquetando esta métrica como **Sent to Carrier**. | Pueden aplicarse cargos según los resultados de envío de cada mensaje individual |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cargos aplicados a los resultados de envío de SMS" }

{% alert note %}
**Envíos al operador** está obsoleto para paneles nuevos. Utiliza **Sent**, **Confirmed Delivery**, **Delivery Failed** y **Rejections** para los informes actuales. Consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics) para ver las definiciones.
{% endalert %}

## Conciliar *Rechazos* con Snowflake o Currents {#reconcile-rejections-with-snowflake-or-currents}

La métrica *Rechazos* en el panel es un recuento agregado del espacio de trabajo. No es una exportación a nivel de fila, por lo que no siempre puedes hacer coincidir cada rechazo con una sola fila en Snowflake o un solo evento `users.messages.sms.Rejection` en Currents. Por ejemplo, si el perfil de usuario se eliminó antes de que Braze terminara de procesar el rechazo para la exportación al almacén de datos, ese rechazo no aparece en tu tabla `USERS_MESSAGES_SMS_REJECTION_SHARED` ni en la carga útil de Currents, mientras que los informes agregados de SMS aún pueden reflejar el resultado. Para más información, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles) y los [eventos de rechazo de SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) en el glosario de eventos de Currents.