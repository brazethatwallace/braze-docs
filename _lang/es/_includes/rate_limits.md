<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
Aplicamos el límite de velocidad predeterminado de Braze de 250 000 solicitudes por hora a este endpoint, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
Este endpoint tiene un límite de velocidad de 20 000 solicitudes por día y empresa. Este límite de velocidad se comparte con los endpoints GET, DELETE y POST de `/scim/v2/Users/`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
Este endpoint tiene un límite de velocidad de 20 000 solicitudes por día y empresa. Este límite de velocidad se comparte con los endpoints PUT, GET, DELETE y POST de `/scim/v2/Users/`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
Este endpoint tiene un límite de velocidad de 20 000 solicitudes por día y empresa. Este límite de velocidad se comparte con los endpoints PUT, GET y POST de `/scim/v2/Users/`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
Este endpoint tiene un límite de velocidad de 20 000 solicitudes por día y empresa. Este límite de velocidad se comparte con los endpoints PUT, GET y DELETE de `/scim/v2/Users/`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
Este endpoint tiene un límite de velocidad de 20 000 solicitudes por día y empresa. Este límite de velocidad se comparte con los endpoints PUT, GET, DELETE y POST de `/scim/v2/Users/`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
Aplicamos un límite de velocidad de 1000 solicitudes por minuto a este endpoint, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
Los límites de velocidad de este endpoint varían en función de tu contrato. Para los clientes con puntos de datos en su modelo de precios, Braze aplica un límite de ráfaga de 3000 solicitudes por cada tres segundos. Para el resto de clientes, los límites se configuran de acuerdo con los términos de tu contrato. Los límites actuales de tu cuenta se pueden consultar en el panel en **Configuración** > **API e identificadores** > **Panel de uso de la API**.

Cada solicitud `/users/track` puede contener hasta 75 objetos en total combinados entre `attributes`, `events` y `purchases`. Cada objeto puede actualizar un usuario. Un único perfil de usuario puede ser actualizado por varios objetos.

Para los clientes que han adquirido Monthly Active Users CY 24-25, Universal MAU, Web MAU o Mobile MAU, se aplican límites de velocidad adicionales. Para más información, consulta [Límites de Monthly Active Users CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau).

{% details Límites de velocidad heredados %}
Para los clientes con límites de velocidad heredados, cada solicitud `/users/track` puede contener hasta 75 objetos de atributo, 75 objetos de evento y 75 objetos de compra. Cada objeto puede actualizar un usuario, para un máximo combinado de hasta 225 objetos por solicitud. Un único perfil de usuario puede ser actualizado por varios objetos.
{% enddetails %}

Para más información, consulta [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits). Ponte en contacto con tu CSM para solicitar un aumento.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
Si te incorporaste a Braze a partir del 22 de agosto de 2024, este endpoint tiene un límite de velocidad de 250 solicitudes por minuto, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

También puedes aumentar el límite de velocidad de este endpoint a 40 solicitudes por segundo si cumples los siguientes requisitos:

- Tu espacio de trabajo tiene habilitado el límite de velocidad predeterminado (250 solicitudes por minuto). Ponte en contacto con tu director de cuentas de Braze para obtener más ayuda sobre cómo eliminar cualquier límite de velocidad preexistente que puedas tener.
- Tu solicitud incluye el parámetro `fields_to_export` para enumerar todos los campos que deseas recibir.

{% alert important %}
Si incluyes `canvases_received` o `campaigns_received` en el parámetro `fields_to_export`, tu solicitud no será elegible para el límite de velocidad más rápido. Recomendamos incluir estos elementos en tu solicitud solo si tienes un caso de uso específico para ellos.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
Aplicamos un límite de velocidad compartido de 20 000 solicitudes por minuto a este endpoint. Este límite de velocidad se comparte con los endpoints `/users/alias/new`, `/users/identify`, `/users/merge` y `/users/alias/update`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
Aplicamos un límite de velocidad compartido de 20 000 solicitudes por minuto a este endpoint. Este límite de velocidad se comparte con los endpoints `/users/delete`, `/users/identify`, `/users/merge` y `/users/alias/update`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
Aplicamos un límite de velocidad compartido de 20 000 solicitudes por minuto a este endpoint. Este límite de velocidad se comparte con los endpoints `/users/delete`, `/users/alias/new`, `/users/identify` y `/users/merge`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Aplicamos un límite de velocidad compartido de 20 000 solicitudes por minuto a este endpoint. Este límite de velocidad se comparte con los endpoints `/users/delete`, `/users/alias/new`, `/users/merge` y `/users/alias/update`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
Aplicamos un límite de velocidad compartido de 20 000 solicitudes por minuto a este endpoint. Este límite de velocidad se comparte con los endpoints `/users/delete`, `/users/alias/new`, `/users/identify` y `/users/alias/update`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
Aplicamos un límite de velocidad compartido de 1000 solicitudes por hora a este endpoint. Este límite de velocidad se comparte con los endpoints `/events`, `/events/list` y `/purchases/product_list`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/events-->

{% elsif include.endpoint == "events" %}
Aplicamos un límite de velocidad compartido de 1000 solicitudes por hora a este endpoint. Este límite de velocidad se comparte con los endpoints `/custom_attributes`, `/events/list` y `/purchases/product_list`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
Aplicamos un límite de velocidad compartido de 1000 solicitudes por hora a este endpoint. Este límite de velocidad se comparte con los endpoints `/custom_attributes`, `/events` y `/purchases/product_list`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
Aplicamos un límite de velocidad compartido de 1000 solicitudes por hora a este endpoint. Este límite de velocidad se comparte con los endpoints `/custom_attributes`, `/events` y `/events/list`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
Cuando utilizas filtros de audiencia conectada en tu solicitud, aplicamos un límite de velocidad de 250 solicitudes por minuto a este endpoint. De lo contrario, si se especifica un `external_id`, este endpoint tiene un límite de velocidad predeterminado de 250 000 solicitudes por hora compartido entre los endpoints documentados en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits).

Los endpoints de Braze admiten [solicitudes de API por lotes]({{site.baseurl}}/api/api_limits#batching-api-requests). Una única solicitud a los endpoints de mensajería puede alcanzar cualquiera de los siguientes:

- Hasta 50 `external_ids` específicos, cada uno con parámetros de mensaje individuales
- Un segmento de audiencia de cualquier tamaño, definido en la solicitud como un objeto de [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience)

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
El endpoint `/transactional/v1/campaigns/{campaign_id}/send` es un endpoint de pago por unidades por hora (por ejemplo, 50 000 por hora, dependiendo de tu paquete). No hay un límite de velocidad por endpoint independiente: puedes enviar más allá del volumen asignado, pero solo el volumen asignado está cubierto por el SLA. Las solicitudes a este endpoint cuentan para tu [límite de velocidad de API externa general]({{site.baseurl}}/api/api_limits). Si superas ese límite (por ejemplo, 250 000 solicitudes por hora en todos los endpoints), Braze devuelve 429 y las solicitudes se limitan. El recuento del volumen transaccional se restablece cada hora, por lo que, transcurrida una hora, hay disponible otra asignación. Dentro del volumen cubierto por el SLA, el 99,9 % de los correos electrónicos se enviarán en menos de un minuto.

<!---POST /preference_center/v1 and PUT /preference_center/v1/{preferenceCenterExternalID}-->
{% elsif include.endpoint == "post or put preference center" %}
Este endpoint tiene un límite de velocidad de 10 solicitudes por minuto, por espacio de trabajo, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---GET /preference_center/v1-->
{% elsif include.endpoint == "get preference center" %}
Este endpoint tiene un límite de velocidad de 1000 solicitudes por minuto, por espacio de trabajo, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
Puedes crear hasta 100 identificadores de envío personalizados al día utilizando este endpoint para un espacio de trabajo determinado. Cada combinación de `send_id` y `campaign_id` que crees contará para tu límite diario. Los encabezados de respuesta de cualquier solicitud válida incluyen el estado actual del límite de velocidad. Consulta [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits) para obtener más información.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
Este endpoint tiene un límite de velocidad de 5000 solicitudes por minuto compartido entre los endpoints `/subscription/status/set` y `/v2/subscription/status/set`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
Este endpoint tiene un límite de velocidad de 50 solicitudes por minuto.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
Este endpoint tiene un límite de velocidad de 20 solicitudes por minuto.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
Este endpoint tiene un límite de velocidad de 100 solicitudes por minuto.

<!---/media_library/create, /media_library/replace_file--->
{% elsif include.endpoint == "media_library" %}
Este endpoint tiene un límite de velocidad de 100 solicitudes por hora, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Los endpoints de Braze admiten [solicitudes de API por lotes]({{site.baseurl}}/api/api_limits#batching-api-requests). Una única solicitud a los endpoints de mensajería puede alcanzar cualquiera de los siguientes:

- Hasta 50 `external_ids` específicos, cada uno con parámetros de mensaje individuales
- Un segmento de cualquier tamaño creado en el panel de Braze, especificado por su `segment_id`
- Un segmento de audiencia de cualquier tamaño, definido en la solicitud como un objeto de [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience)

{% endif %}

{% if include.category == "send messages endpoints" %}

Los endpoints de Braze admiten [solicitudes de API por lotes]({{site.baseurl}}/api/api_limits#batching-api-requests). Una única solicitud a los endpoints de mensajería puede alcanzar cualquiera de los siguientes:

- Hasta 50 `external_ids` específicos, cada uno con parámetros de mensaje individuales
- Un segmento de audiencia de cualquier tamaño, definido en la solicitud como un objeto de [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience)

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

Este endpoint tiene un límite de velocidad de 250 000 solicitudes por minuto.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Los endpoints de Braze admiten [solicitudes de API por lotes]({{site.baseurl}}/api/api_limits#batching-api-requests). Una única solicitud a los endpoints de mensajería puede alcanzar cualquiera de los siguientes:

- Hasta 50 `external_ids` específicos
- Un segmento de cualquier tamaño creado en el panel de Braze, especificado por su `segment_id`
- Un segmento de audiencia de cualquier tamaño, definido en la solicitud como un objeto de [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience)

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

Este endpoint tiene un límite de velocidad compartido de 16 000 solicitudes por minuto entre todos los endpoints de elementos de catálogo asíncronos, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

Este endpoint tiene un límite de velocidad compartido de 50 solicitudes por minuto entre todos los endpoints de elementos de catálogo síncronos, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

Este endpoint tiene un límite de velocidad compartido de 50 solicitudes por minuto entre todos los endpoints de catálogo síncronos, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

Este endpoint tiene un límite de velocidad compartido de 50 solicitudes por minuto entre todos los endpoints asíncronos de campos y selecciones de catálogo, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits).

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

Este endpoint tiene un límite de velocidad de 50 000 solicitudes por minuto.

{% endif %}