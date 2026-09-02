---
nav_title: Límites de velocidad
article_title: Límites de velocidad
page_order: 4.5
description: "Este artículo de referencia cubre los límites de velocidad de la API para la infraestructura de la API de Braze."
page_type: reference
---

# Límites de velocidad {#rate-limits}

> La infraestructura de la API de Braze está diseñada para gestionar grandes volúmenes de datos de toda nuestra base de clientes. Para ello, imponemos límites de velocidad de API por espacio de trabajo.

Un límite de velocidad es el número de solicitudes que puede recibir la API en un periodo de tiempo determinado. Muchos incidentes de denegación de servicio basados en la carga en grandes sistemas son involuntarios —causados por errores en el software o las configuraciones—, no ataques maliciosos. Los límites de velocidad comprueban que esos errores no priven a nuestros clientes de los recursos de la API de Braze. Si se envían demasiadas solicitudes en un periodo de tiempo determinado, es posible que veas respuestas de error con un código de estado `429`, que indica que se ha alcanzado el límite de velocidad.

{% alert warning %}
Los límites de velocidad de la API están sujetos a cambios en función del uso adecuado de nuestro sistema. Animamos a que se establezcan límites razonables al realizar una llamada a la API para evitar daños o usos indebidos.
{% endalert %}

## Límites de velocidad por tipo de solicitud {#rate-limits-by-request-type}

Consulta lo siguiente para conocer los límites de velocidad de API predeterminados de los diferentes tipos de solicitud. Estos límites predeterminados pueden aumentarse a solicitud. Contacta a tu CSM or administrador de éxito de cliente or administrador de éxito de cliente para más información.

### Solicitudes con diferentes límites de velocidad {#requests-with-different-rate-limits}

| Tipo de solicitud                                                                                                                                                                                                                                           | Límite de velocidad de API predeterminado                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)                                                                                                                                                                                                                                   | **Solicitudes:** Los límites de velocidad varían según tu contrato. Para clientes con puntos de datos en su modelo de precios, Braze aplica un límite de ráfaga de 3000 solicitudes cada tres segundos. Para todos los demás clientes, los límites se configuran según los términos de tu contrato. Contacta a soporte de Braze o a tu CSM or administrador de éxito de cliente or administrador de éxito de cliente si tienes preguntas sobre tus límites.<br><br>**Procesamiento en lotes:** Hasta 75 objetos totales combinados entre `attributes`, `events` y `purchases` por solicitud de API. Los clientes con límites de velocidad heredados pueden incluir hasta 75 objetos por array de forma independiente. Para más información, consulta [Procesamiento en lotes de solicitudes User Track](#batch-user-track).<br><br>**Límites para MAU or usuarios activos al mes or usuarios activos al mes CY 24-25, MAU or usuarios activos al mes universal, MAU or usuarios activos al mes Web y MAU or usuarios activos al mes móvil:** Consulta [Límites de MAU or usuarios activos al mes or usuarios activos al mes CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau). |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)                                                                                                                                                                                                                              | **Si te incorporaste a partir del 22 de agosto de 2024:** 250 solicitudes por minuto. <br><br> **Si te incorporaste antes del 22 de agosto de 2024:** 2500 solicitudes por minuto.                                                                                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)                                                                                                                    | 20 000 solicitudes por minuto, compartidas entre los endpoints.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)                                                                                                                                                                                                                      | 1000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)                                                                                                                                                                                                                      | 1000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events)                                                                                                                                                                                                                                   | 1000 solicitudes por hora, compartidas con el endpoint `/purchases/product_list`.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id)                                                                                                                                                                                                                        | 1000 solicitudes por hora, compartidas con el endpoint `/events/list`.                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)                                                                                                                                                                                                                       | 50 000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)<br>[`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)<br>[`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)                                                                                                                                                          | Para llamadas de difusión (que se dirigen de forma amplia a Segments, filtros o una audiencia conectada), 250 solicitudes por minuto entre todas las audiencias, y 10 solicitudes por minuto por [audiencia única]({{site.baseurl}}/api/api_limits#what-counts-as-the-same-unique-audience) (el límite que se alcance primero).<br><br>De lo contrario, cuando se dirige a destinatarios individuales, la solicitud se incluye en el [límite de velocidad compartido]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits) de 250 000 solicitudes por hora.                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)                                                                                                                                                                                                                               | 100 solicitudes por día.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)                                                                                                                                                                                                                       | 5000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center)                                                                            | 1000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center)                                                                                                                                                            | 10 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)                                                                                                                                                                             | 50 solicitudes por minuto compartidas entre los endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)                                                                                                                             | 16 000 solicitudes por minuto compartidas entre los endpoints.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | 50 solicitudes por minuto compartidas entre los endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 solicitudes por minuto compartidas entre los endpoints. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account)                                                                          | 5000 solicitudes por día, por empresa, compartidas entre los endpoints.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list)                                                                                                                                                                                                                              | 50 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status)                                                                                                                                                                                                        | 20 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync)                                                                                                                                                                                             | 100 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                  |
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | 100 solicitudes por hora. |
| [`/media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) | 100 solicitudes por hora. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solicitudes con diferentes límites de velocidad" }

### Solicitudes con límites de velocidad compartidos {#requests-with-shared-rate-limits}

Las siguientes solicitudes tienen un límite de velocidad de 250 000 solicitudes por hora, compartido entre ellas.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) (solo para llamadas que no son de difusión, es decir, aquellas que especifican `external_user_ids` o `aliases`)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) (solo para llamadas que no son de difusión)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) (solo para llamadas que no son de difusión)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) (solo para llamadas que no son de difusión)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) (solo para llamadas que no son de difusión)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

### ¿Qué cuenta como la misma audiencia única? {#what-counts-as-the-same-unique-audience}

Esto se aplica a los siguientes endpoints: [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases), [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) y [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases).

Para estos endpoints, las solicitudes de difusión se consideran dirigidas a la misma audiencia única cuando coinciden todos los siguientes criterios:

- La Campaign o Canvas que se está desencadenando (el `campaign_id` o `canvas_id` en tu solicitud de API, si se especifica)
- La audiencia a la que se dirige (los Segments o filtros, o para Campaigns de API, el `segment_id` en tu solicitud de API)
- Los filtros de audiencia conectada (el objeto `audience` en tu solicitud de API, si se especifica)

Cada combinación única de estos atributos cuenta como una audiencia distinta, por lo que el límite de velocidad adicional para cada audiencia única se aplica a cada combinación de forma independiente.

## Agrupación de solicitudes de API en lotes {#batching-api-requests}

Las API de Braze están diseñadas para admitir el procesamiento por lotes. Con el procesamiento por lotes, Braze puede recibir la mayor cantidad de datos posible en una sola llamada a la API, de modo que no necesites realizar muchas llamadas. Es más eficiente para Braze procesar datos en lotes que procesarlos de una llamada a la vez. Por ejemplo, gestionar 1,000 llamadas a la API en lotes requiere menos recursos que gestionar 75,000 llamadas individuales. El procesamiento por lotes es extremadamente importante para cualquier aplicación que pueda requerir más de 75,000 llamadas por hora.

{% alert note %}
Los aumentos en el límite de velocidad de la REST or transferencia de estado representacional API se consideran en función de la necesidad de los clientes que están utilizando las capacidades de procesamiento por lotes de la API.
{% endalert %}

### Agrupación en lotes de solicitudes para el endpoint de crear y actualizar usuarios {#batch-user-track}

Cada solicitud de `/users/track` puede contener hasta 75 objetos en total combinados entre `attributes`, `events` y `purchases`. Cada objeto puede actualizar un usuario. Un único perfil de usuario puede ser actualizado por múltiples objetos.

{% details Límites de velocidad heredados %}
Para los clientes con límites de velocidad heredados, cada array (`attributes`, `events` y `purchases`) puede contener hasta 75 objetos de forma independiente, para un máximo combinado de hasta 225 objetos por solicitud.
{% enddetails %}

Para obtener más información sobre los límites de velocidad de `/users/track`, consulta [POST: Crear y actualizar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Las solicitudes realizadas a este endpoint generalmente comienzan a procesarse en este orden:

1. Atributos
2. Eventos
3. Compras

### Agrupación en lotes de solicitudes a endpoints de mensajería {#batching-messaging-endpoint-requests}

Una sola solicitud a los [endpoints de mensajería]({{site.baseurl}}/api/endpoints/messaging) puede alcanzar cualquiera de los siguientes:

- Hasta 50 `external_ids` específicos, cada uno con parámetros de mensaje individuales
- Un Segment de cualquier tamaño creado en el panel de Braze, especificado por su `segment_id`
- Usuarios que coincidan con filtros de audiencia adicionales de cualquier tamaño, definidos en la solicitud como un objeto de [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience)

### Ejemplo de solicitud por lotes {#example-batch-request}

El siguiente ejemplo utiliza `external_id` para realizar una sola llamada a la API para correo electrónico y servicio de mensajes cortos.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@example.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@example.com"]
    }
  ]
}
```

## Monitorización de tus límites de velocidad {#monitoring-your-rate-limits}

Cada solicitud de API enviada a Braze devuelve la siguiente información en los encabezados de respuesta:

| Nombre del encabezado   | Descripción                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | El número máximo de solicitudes que puedes realizar en un intervalo especificado (tu límite de velocidad). |
| `X-RateLimit-Remaining` | El número de solicitudes restantes en la ventana actual de límite de velocidad.              |
| `X-RateLimit-Reset`     | La hora a la que se restablece la ventana actual de límite de velocidad en segundos epoch UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Monitorización de tus límites de velocidad" }

Esta información se incluye intencionalmente en el encabezado de la respuesta a la solicitud de API en lugar del panel de Braze. Esto permite que tu sistema reaccione mejor en tiempo real mientras interactúa con nuestra API. Por ejemplo, si el valor de `X-RateLimit-Remaining` cae por debajo de un determinado umbral, podrías querer ralentizar el envío para asegurarte de que todos los correos transaccionales se envíen. O, si llega a cero, podrías querer pausar todos los envíos hasta que transcurra el tiempo especificado en `X-RateLimit-Reset`.

{% alert note %}
Los encabezados HTTP se devolverán completamente en minúsculas. Este comportamiento se alinea con el protocolo HTTP/2, que exige que todos los nombres de campos de encabezado sean en minúsculas. Esto difiere de HTTP/1.X, donde los nombres de encabezado no distinguían entre mayúsculas y minúsculas, pero comúnmente se escribían con distintas capitalizaciones.
{% endalert %}

Si tienes preguntas sobre los límites de API, contacta a tu CSM or administrador de éxito de cliente or administrador de éxito de cliente o abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

{% alert tip %}
Puedes usar el [panel de uso de API]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage) para ver y comparar el tráfico entrante con tus límites de velocidad.
{% endalert %}

### Retraso óptimo entre endpoints {#optimal-delay-between-endpoints}

{% alert note %}
Recomendamos que permitas un retraso de 5 minutos entre llamadas consecutivas a endpoints para minimizar errores.
{% endalert %}

Comprender el retraso óptimo entre endpoints es crucial al realizar llamadas consecutivas a la API de Braze. Los problemas surgen cuando los endpoints dependen del procesamiento exitoso de otros endpoints y, si se llaman demasiado pronto, podrían generar errores. Por ejemplo, si estás asignando a los usuarios un alias a través de nuestro endpoint `/user/alias/new` y luego utilizas ese alias para enviar un evento personalizado a través de nuestro endpoint `/users/track`, ¿cuánto tiempo deberías esperar?

En condiciones normales, el tiempo para que ocurra la consistencia eventual de nuestros datos es de 10 a 100 ms (1/10 de segundo). Sin embargo, puede haber algunos casos en los que esa consistencia tarde más en producirse, por lo que recomendamos que permitas un retraso de 5 minutos entre llamadas posteriores para minimizar la probabilidad de error.

## Límites de tamaño de la carga útil {#payload-size-limits}

Las solicitudes a la API de Braze están sujetas a límites de tamaño de la carga útil, independientes de los límites de velocidad. La mayoría de los endpoints aceptan cuerpos de solicitud de hasta 4&nbsp;MB. Cuando una solicitud supera el límite aplicable, Braze puede rechazarla con HTTP `413 Request Entity Too Large` o HTTP `400 Bad Request`, según el endpoint.

El endpoint [`/users/track/bulk`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_bulk) tiene un límite de carga útil de 2&nbsp;MB y devuelve HTTP `400` cuando el cuerpo de la solicitud supera ese límite. Para conocer los límites específicos de cada endpoint y el manejo de errores, consulta [Endpoints de datos de usuario]({{site.baseurl}}/api/endpoints/user_data).

### Restablecimiento del límite de velocidad {#rate-limit-reset}

Los límites de velocidad se restablecen en la hora en punto, no en una ventana deslizante. Por ejemplo, si el límite es de 250.000 solicitudes por hora, podrías hacer 50.000 solicitudes entre las 10:00 PM y las 10:59 PM y otras 250.000 solicitudes entre las 11:00 PM y las 11:59 PM, porque el contador se restablece al inicio de cada hora.