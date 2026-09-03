---
nav_title: "Referencia de tablas SQL"
article_title: "Referencia de tablas SQL"
page_order: 3
page_type: reference
toc_headers: h2
description: "Esta página es una referencia de las tablas y columnas SQL de Snowflake utilizadas en el generador de consultas, las extensiones de segmento SQL y Snowflake Data Sharing."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# Referencia de tablas SQL {#sql-table-reference}

Esta página es una referencia de las tablas y columnas SQL de Snowflake disponibles en las siguientes herramientas de Braze:

- [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

La mayoría de las tablas están disponibles en las tres herramientas. Las tablas marcadas como **Solo Snowflake Data Sharing** son exclusivas de Snowflake Data Sharing y no son accesibles en el generador de consultas ni en las extensiones de segmento SQL.

{% alert tip %}
Estas tablas SQL corresponden a los eventos documentados en el [glosario de eventos de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events). Por ejemplo, la tabla SQL `USERS_MESSAGES_EMAIL_SEND_SHARED` corresponde al evento de Currents `users.messages.email.Send`. Si necesitas esquemas de eventos JSON o formatos específicos de partners (Amplitude, Mixpanel, Segment), consulta el glosario de Currents.
{% endalert %}

## Tabla de contenidos {#table-of-contents}

Tabla | Descripción
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | Cuando se ejecuta un agente de Agent Console (**solo Snowflake Data Sharing**)
[AGENTCONSOLE_RAWLLMREQUEST_SHARED](#AGENTCONSOLE_RAWLLMREQUEST_SHARED) | Información sin procesar de cada llamada a LLM (**solo Snowflake Data Sharing**)
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | Cuando se ejecuta una herramienta (**solo Snowflake Data Sharing**)
[USER_CUSTOM_ATTRIBUTES_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED) | Instantánea periódica de los atributos personalizados de perfil por usuario
[USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED) | Atributos predeterminados de perfil históricos con rangos de fechas de vigencia
[USER_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED) | Instantánea periódica de los atributos predeterminados de perfil por usuario
[USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED) | Atributos predeterminados de perfil por usuario en tiempo casi real
[USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED) | Atributos personalizados de perfil históricos con rangos de fechas de vigencia (**solo Snowflake Data Sharing**)
[USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED](#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED) | Atributos personalizados de perfil por usuario en tiempo casi real (**solo Snowflake Data Sharing**)
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Elementos de catálogo no eliminados
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | Cuando se modifica una Campaign (**solo Snowflake Data Sharing**)
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Cuando se modifica un Canvas (**solo Snowflake Data Sharing**)
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Cuando se modifica el grupo de control global
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Cuando un usuario realiza un evento personalizado
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Cuando un usuario instala una aplicación y la atribuimos a un partner
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Cuando un usuario registra una ubicación
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Cuando un usuario realiza una compra
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Cuando un usuario desinstala una aplicación
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Cuando un usuario actualiza la aplicación
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Cuando un usuario tiene su primera sesión
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Cuando un usuario ve el News Feed
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Cuando un usuario finaliza una sesión en una aplicación
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Cuando un usuario inicia una sesión en una aplicación
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Cuando un usuario activa un área de geovalla, por ejemplo, al entrar o salir de una geovalla. Este evento se agrupa con otros eventos y se recibe a través del endpoint de eventos estándar, por lo que puede no aparecer en tiempo real.<br><br>Para registrar la actividad de geovallas en esta tabla, selecciona **Enable Analytics for Enter** y **Enable Analytics for Exit** en la configuración avanzada de cada geovalla. Consulta el paso 3 en [Crear geovallas manualmente]({{site.baseurl}}/user_guide/audience/locations_and_geofences/creating_geofences#manually-create-geofences) para más detalles.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Cuando un usuario activa un área de geovalla (por ejemplo, cuando entra o sale de una geovalla). Este evento se recibió a través del endpoint dedicado de geovallas y, por lo tanto, se recibe en tiempo real en cuanto el dispositivo de un usuario detecta que ha activado una geovalla. <br><br>Además, debido a los límites de velocidad en el endpoint de geovallas, es posible que algunos eventos de geovalla no se reflejen como RecordEvent. Sin embargo, todos los eventos de geovalla están representados por DataEvent (aunque potencialmente con cierto retraso debido al procesamiento por lotes).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Cuando cambia un token push-to-start de Live Activity
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Cuando cambia un token de actualización de Live Activity
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Cuando cambia el estado de un token de notificación push
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Cuando un usuario se suscribe o cancela su suscripción globalmente a un canal como el correo electrónico
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Cuando un usuario se suscribe o cancela su suscripción a un grupo de suscripción
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Cuando un usuario convierte para una Campaign
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Cuando un usuario se inscribe en el grupo de control de una Campaign
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Cuando un usuario alcanza el límite de frecuencia para una Campaign
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Cuando un usuario genera ingresos dentro del periodo de conversión primaria
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Cuando un usuario avanza a un paso en Canvas
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Cuando un usuario convierte para un evento de conversión de Canvas
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Cuando un usuario entra en un Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Cuando un usuario sale de un Canvas porque coincide con los criterios de salida de audiencia
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Cuando un usuario sale de un Canvas porque realizó un evento de excepción
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Cuando un usuario convierte para un paso de experimento en Canvas
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Cuando un usuario entra en una ruta de paso de experimento
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Cuando un usuario alcanza el límite de frecuencia para un paso en Canvas
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Cuando un usuario genera ingresos dentro del periodo de evento de conversión primaria
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Un mensaje de banner programado originalmente fue cancelado por algún motivo
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Cuando un usuario hace clic en un banner
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Cuando un usuario ve un banner
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Un mensaje de Content Card programado originalmente fue cancelado por algún motivo.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Cuando un usuario hace clic en una Content Card
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Cuando un usuario descarta una Content Card
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Cuando un usuario ve una Content Card
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Cuando enviamos una Content Card a un usuario
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Un mensaje de correo electrónico programado originalmente fue cancelado por algún motivo.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Un proveedor de servicios de correo electrónico devolvió un rebote duro. Un rebote duro indica un fallo permanente de capacidad de entrega.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Cuando un usuario hace clic en un enlace en un correo electrónico
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Cuando un correo electrónico es diferido
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Cuando un correo electrónico es entregado
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Cuando un correo electrónico se marca como correo no deseado
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Cuando un usuario abre un correo electrónico
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Cuando enviamos un correo electrónico a un usuario
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Cuando un correo electrónico sufre un rebote blando
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Cuando un usuario cancela su suscripción al correo electrónico
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | Cuando un mensaje de correo electrónico se reintenta después de haber sido despriorizado o alcanzar el límite de frecuencia (**solo Snowflake Data Sharing**)
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Cuando un usuario ve un conmutador de características
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Un mensaje dentro de la aplicación programado originalmente fue cancelado por algún motivo.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Cuando un usuario hace clic en un mensaje dentro de la aplicación
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Cuando un usuario ve un mensaje dentro de la aplicación
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Cuando un mensaje de LINE programado no puede entregarse, antes de enviarse a LINE
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Cuando un usuario hace clic en un enlace en un mensaje de LINE
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Cuando se recibe un mensaje de LINE de un usuario
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Cuando se envía un mensaje de LINE a LINE
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | Cuando un mensaje de LINE se reintenta después de haber sido despriorizado o alcanzar el límite de frecuencia (**solo Snowflake Data Sharing**)
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Cuando una Live Activity tiene un evento de resultado
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Cuando se envía un mensaje de Live Activity
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Un mensaje de tarjeta de News Feed programado originalmente fue cancelado por algún motivo
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Cuando un usuario hace clic en una tarjeta de News Feed
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Cuando un usuario ve una tarjeta de News Feed
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Un mensaje de notificación push programado originalmente fue cancelado por algún motivo.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Cuando una notificación push rebota
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Cuando un usuario abre la aplicación después de recibir una notificación sin hacer clic en ella
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Cuando un usuario recibe una notificación push mientras la aplicación está abierta. <br><br>Este evento no es compatible con el [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) y está obsoleto en el [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk).
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Cuando un usuario abre una notificación push o hace clic en un botón de la notificación push (incluido un botón CERRAR que NO abre la aplicación). <br><br> Las acciones de los botones push tienen múltiples resultados. Las acciones No, Rechazar y Cancelar son "clics", y las acciones Aceptar son "aperturas". Ambas se representan en esta tabla, pero se pueden distinguir en la columna **BUTTON_ACTION_TYPE**. Por ejemplo, se puede usar una consulta para agrupar por un `BUTTON_ACTION_TYPE` que no sea No, Rechazar o Cancelar.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Cuando enviamos una notificación push a un usuario
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Cuando un envío de RCS se interrumpe debido a un error detectado dentro de Braze y el mensaje se descarta
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Cuando el usuario final interactúa con un mensaje RCS tocando o haciendo clic en un elemento de la interfaz
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Cuando un mensaje RCS se entrega correctamente al dispositivo móvil del usuario final
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Cuando Braze recibe un mensaje RCS que se origina desde el usuario final
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Cuando el usuario final abre un mensaje RCS en su dispositivo
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Cuando un mensaje RCS no se entrega debido a una intervención del operador
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Cuando un mensaje RCS se envía desde los sistemas de Braze a los socios de entrega de último tramo
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Un mensaje SMS programado originalmente fue cancelado por algún motivo.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Cuando un mensaje SMS se envía al operador
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Cuando un mensaje SMS es entregado
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Cuando Braze no puede entregar el mensaje SMS al proveedor de servicios SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Cuando se recibe un mensaje SMS de un usuario
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Cuando un mensaje SMS no se entrega a un usuario
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Cuando se envía un mensaje SMS
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Cuando un usuario hace clic en una URL acortada de Braze incluida en un mensaje SMS
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | Cuando un mensaje SMS se reintenta después de haber sido despriorizado o alcanzar el límite de frecuencia (**solo Snowflake Data Sharing**)
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Un mensaje de webhook programado originalmente fue cancelado por algún motivo
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Cuando un mensaje de webhook se entrega pero falla con una respuesta de error del endpoint
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Cuando enviamos un webhook para un usuario
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | Cuando un mensaje de webhook se reintenta después de haber sido despriorizado o alcanzar el límite de frecuencia (**solo Snowflake Data Sharing**)
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Un mensaje de WhatsApp programado originalmente fue cancelado por algún motivo
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Cuando un usuario hace clic en un enlace o botón en un mensaje de WhatsApp
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | Cuando un mensaje de WhatsApp es entregado
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Cuando un mensaje de WhatsApp no se entrega a un usuario
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Cuando se recibe un mensaje de WhatsApp de un usuario
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Cuando un usuario abre un mensaje de WhatsApp
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Cuando enviamos un mensaje de WhatsApp para un usuario
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | Cuando un mensaje de WhatsApp se reintenta después de haber sido despriorizado o alcanzar el límite de frecuencia (**solo Snowflake Data Sharing**)
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Cuando se cambia el número de contenedor aleatorio de un usuario
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Cuando un usuario es eliminado por solicitud de un cliente
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Cuando un usuario se fusiona con el perfil de otro usuario y el perfil original queda huérfano
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | Instantáneas de la aplicación (**solo Snowflake Data Sharing**)
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | Instantáneas de variantes de mensajes de Campaign (**solo Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | Instantáneas de pasos de Canvas Flow (**solo Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | Instantáneas de pasos en Canvas (**solo Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | Instantáneas de variantes de Canvas (**solo Snowflake Data Sharing**)
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | Instantáneas de pasos de experimento (**solo Snowflake Data Sharing**)

## Consola de Agente {#agent-console}

{% alert note %}
Las tablas de la Consola de Agente solo están disponibles en Snowflake Data Sharing.
{% endalert %}

### AGENTCONSOLE_AGENTEXECUTED_SHARED {#AGENTCONSOLE_AGENTEXECUTED_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`invocation_id` | `string` | ID globalmente único para este mensaje
`request_id` | `string` | ID único para esta solicitud LLM general y ejecución completa
`duration` | `int` | Duración de la sesión en segundos
`prompt_tokens` | `int` | Cuántos tokens de prompt utilizó esta solicitud
`completion_tokens` | `int` | Cuántos tokens de completado utilizó esta solicitud
`total_tokens` | `int` | Cuántos tokens totales utilizó esta solicitud
`cache_tokens` | `int` | Cuántos tokens en caché utilizó esta solicitud
`reasoning_tokens` | `int` | Cuántos tokens de razonamiento utilizó esta solicitud
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`agent_id` | `string` | ID BSON del CustomerDefinedAgent
`agent_name` | `string` | Nombre del CustomerDefinedAgent
`model_provider` | `string` | Nombre del proveedor del modelo LLM
`model_name` | `string` | Nombre del modelo LLM utilizado en esta solicitud
`provider_request_id` | `string` | Cualquier ID de solicitud proporcionado por el proveedor del modelo para la llamada a la API
`cache_hit` | `boolean` | Si esta solicitud utilizó la caché para devolver la respuesta
`llm_owned_by_customer` | `boolean` | Si es verdadero, se utilizó la clave de API del cliente; si es falso, se utilizó la clave de Braze
`is_error` | `boolean` | Si esta solicitud generó un error
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`user_id` | `string` | [PII] ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`input` | `null,`&nbsp;`string` | [PII] Entrada al LLM
`output` | `null,`&nbsp;`string` | [PII] Respuesta del LLM
`invocation_source` | `null,`&nbsp;`string` | Qué objeto Ruby invocó la solicitud LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Cuándo este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLEAGENTEXECUTEDSHARED #AGENTCONSOLEAGENTEXECUTEDSHARED" }

### AGENTCONSOLE_RAWLLMREQUEST_SHARED {#AGENTCONSOLE_RAWLLMREQUEST_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`invocation_id` | `string` | ID globalmente único para este mensaje
`request_id` | `string` | ID único para esta solicitud LLM general y ejecución completa
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este evento
`agent_id` | `string` | ID BSON del CustomerDefinedAgent
`agent_name` | `string` | Nombre del CustomerDefinedAgent
`model_provider` | `string` | Nombre del proveedor del modelo LLM
`model_name` | `string` | Nombre del modelo LLM utilizado en esta solicitud
`duration` | `int`,&nbsp;`null` | Duración de la sesión en segundos
`request` | `string` | [PII] Prompt utilizado en la solicitud
`http_status_code` | `int`,&nbsp;`null` | Código de estado HTTP de la respuesta
`response_body` | `string`,&nbsp;`null` | [PII] Respuesta del LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Cuándo este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLERAWLLMREQUESTSHARED #AGENTCONSOLERAWLLMREQUESTSHARED" }

### AGENTCONSOLE_TOOLINVOCATION_SHARED {#AGENTCONSOLE_TOOLINVOCATION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`tool_call_id` | `string` | ID globalmente único para esta llamada de herramienta
`duration` | `int` | Duración de la sesión en segundos
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`agent_id` | `string` | ID BSON del CustomerDefinedAgent
`agent_name` | `string` | Nombre del CustomerDefinedAgent
`is_error` | `boolean` | Si esta solicitud generó un error
`tool_name` | `string` | Nombre de la herramienta
`tool_arguments` | `null,`&nbsp;`string` | [PII] JSON de los argumentos de la herramienta
`invocation_source` | `null,`&nbsp;`string` | Qué objeto Ruby invocó la solicitud LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Cuándo este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLETOOLINVOCATIONSHARED #AGENTCONSOLETOOLINVOCATIONSHARED" }

## Vistas de atributos de perfil de usuario {#user-profile-attribute-views}

### USER_CUSTOM_ATTRIBUTES_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_id` | `string` | ID BSON del espacio de trabajo
`app_id` | `string` | ID BSON de la aplicación
`user_id` | `string` | [PII] ID de usuario de Braze
`time` | `int` | Marca de tiempo UNIX en segundos de la actualización del perfil (para filas rellenadas retroactivamente, la hora del relleno)
`time_ms` | `int` | Marca de tiempo UNIX en milisegundos de la actualización del perfil (para filas rellenadas retroactivamente, la hora del relleno)
`update_source` | `string` | Origen de la actualización del perfil
`sf_updated_at` | `timestamp` | Cuándo se actualizó esta fila en Snowflake
`custom_attributes` | `variant` | [PII] Atributos personalizados como objeto JSON
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED #USERCUSTOMATTRIBUTESVIEWSHARED" }

### USER_DEFAULT_ATTRIBUTES_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_id` | `string` | ID BSON del espacio de trabajo
`app_id` | `string` | ID BSON de la aplicación
`user_id` | `string` | [PII] ID de usuario de Braze
`time` | `int` | Marca de tiempo UNIX en segundos de la actualización del perfil (para filas rellenadas retroactivamente, la hora del relleno)
`time_ms` | `int` | Marca de tiempo UNIX en milisegundos de la actualización del perfil (para filas rellenadas retroactivamente, la hora del relleno)
`update_source` | `string` | Origen de la actualización del perfil
`sf_updated_at` | `timestamp` | Cuándo se actualizó esta fila en Snowflake
`external_user_id` | `string` | [PII] ID externo del usuario
`first_name` | `string` | [PII] Nombre
`last_name` | `string` | [PII] Apellido
`email_address` | `string` | [PII] Dirección de correo electrónico
`gender` | `string` | [PII] Género
`phone_number` | `string` | [PII] Número de teléfono
`dob` | `string` | [PII] Fecha de nacimiento
`TIME_ZONE` | `string` | [PII] Zona horaria
`home_city` | `string` | [PII] Ciudad de residencia
`country` | `string` | [PII] País
`language` | `string` | [PII] Idioma
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED #USERDEFAULTATTRIBUTESVIEWSHARED" }

### USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_id` | `string` | ID BSON del espacio de trabajo
`user_id` | `string` | [PII] ID de usuario de Braze
`app_id` | `string` | ID BSON de la aplicación
`time` | `int` | Marca de tiempo UNIX en segundos de la actualización del perfil (para filas rellenadas retroactivamente, la hora del relleno)
`time_ms` | `int` | Marca de tiempo UNIX en milisegundos de la actualización del perfil (para filas rellenadas retroactivamente, la hora del relleno)
`update_source` | `string` | Origen de la actualización del perfil
`sf_updated_at` | `timestamp` | Cuándo se actualizó esta fila en Snowflake
`external_user_id` | `string` | [PII] ID externo del usuario
`first_name` | `string` | [PII] Nombre
`last_name` | `string` | [PII] Apellido
`email_address` | `string` | [PII] Dirección de correo electrónico
`gender` | `string` | [PII] Género
`phone_number` | `string` | [PII] Número de teléfono
`dob` | `string` | [PII] Fecha de nacimiento
`TIME_ZONE` | `string` | [PII] Zona horaria
`home_city` | `string` | [PII] Ciudad de residencia
`country` | `string` | [PII] País
`language` | `string` | [PII] Idioma
`eff_dt` | `timestamp` | Inicio del intervalo en el que este estado de atributo estaba vigente
`end_dt` | `timestamp` | Fin de ese intervalo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED #USERDEFAULTATTRIBUTESHISTORYVIEWSHARED" }

### USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED {#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_id` | `string` | ID BSON del espacio de trabajo
`app_id` | `string` | ID BSON de la aplicación
`user_id` | `string` | [PII] ID de usuario de Braze
`time` | `int` | Marca de tiempo UNIX en segundos de la actualización del perfil (para filas rellenadas retroactivamente, la hora del relleno)
`time_ms` | `int` | Marca de tiempo UNIX en milisegundos de la actualización del perfil (para filas rellenadas retroactivamente, la hora del relleno)
`update_source` | `string` | Origen de la actualización del perfil
`sf_updated_at` | `timestamp` | Cuándo se actualizó esta fila en Snowflake
`external_user_id` | `string` | [PII] ID externo del usuario
`first_name` | `string` | [PII] Nombre
`last_name` | `string` | [PII] Apellido
`email_address` | `string` | [PII] Dirección de correo electrónico
`gender` | `string` | [PII] Género
`phone_number` | `string` | [PII] Número de teléfono
`dob` | `string` | [PII] Fecha de nacimiento
`home_city` | `string` | [PII] Ciudad de residencia
`country` | `string` | [PII] País
`language` | `string` | [PII] Idioma
`TIME_ZONE` | `string` | [PII] Zona horaria
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED #USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED" }

### USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="history" %}

Para obtener orientación de uso y consultas de ejemplo, consulta [Atributos de usuario de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#historical-change-logs).

### USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED {#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="latest" %}

Para obtener orientación de uso y consultas de ejemplo, consulta [Atributos de usuario de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#real-time-user-profile-views).

## Catálogos {#catalogs}

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Campo | Tipo | Descripción
------|------|------------
`catalog_id` | `string` | ID BSON del catálogo
`item_id` | `string` | ID BSON del elemento del catálogo
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones
`field_name` | `null,`&nbsp;`string` | Nombre del campo
`field_value` | `null,`&nbsp;`string` | Valor del campo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CATALOGSITEMSSHARED #CATALOGSITEMSSHARED" }

## Registros de cambios {#changelogs}

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`random_bucket_number` | `null, int` | Nuevo número de contenedor aleatorio
`global_control_group` | `null, boolean` | Con este cambio, el número de contenedor se incluye en el grupo de control global
`previous_global_control_group` | `null, boolean` | Antes de este cambio, el número de contenedor estaba incluido en el grupo de control global, pero ya no lo está
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSGLOBALCONTROLGROUPSHARED #CHANGELOGSGLOBALCONTROLGROUPSHARED" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`api_id` | `string` | ID de API de la Campaign
`name` | `null,`&nbsp;`string` | Nombre de la Campaign
`conversion_behaviors` | `null,`&nbsp;`string` | Comportamientos de conversión de la Campaign
`actions` | `null,`&nbsp;`string` | Acciones de la Campaign
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCAMPAIGNSHARED #CHANGELOGSCAMPAIGNSHARED" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`api_id` | `string` | ID de API del Canvas
`name` | `null,`&nbsp;`string` | Nombre del Canvas
`conversion_behaviors` | `null,`&nbsp;`string` | Comportamientos de conversión del Canvas
`variations` | `null,`&nbsp;`string` | Variaciones del Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCANVASSHARED #CHANGELOGSCANVASSHARED" }

## Comportamientos {#behaviors}

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó el evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo esta acción
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó el evento
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo el evento personalizado
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`name` | `string` | Nombre del evento personalizado
`properties` | `string` | Propiedades personalizadas del evento almacenadas como una cadena codificada en JSON
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador de publicidad
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado para el dispositivo
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSCUSTOMEVENTSHARED #USERSBEHAVIORSCUSTOMEVENTSHARED" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó la instalación
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó la instalación
`source` | `string` | Origen de la atribución
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSINSTALLATTRIBUTIONSHARED #USERSBEHAVIORSINSTALLATTRIBUTIONSHARED" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que registra la ubicación
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se registró esta ubicación
`time` | `int` | Marca de tiempo Unix en la que se registró la ubicación
`latitude` | `float` | [PII] Latitud de la ubicación registrada
`longitude` | `float` | [PII] Longitud de la ubicación registrada
`altitude` | `null, float` | [PII] Altitud de la ubicación registrada
`ll_accuracy` | `null, float` | Precisión de latitud y longitud de la ubicación registrada
`alt_accuracy` | `null, float` | Precisión de altitud de la ubicación registrada
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se registró la ubicación
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso cuando se registró la ubicación
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador de publicidad
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado para el dispositivo
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLOCATIONSHARED #USERSBEHAVIORSLOCATIONSHARED" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó una compra
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo la compra
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó la compra
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo la compra
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante la compra
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`product_id` | `string` | ID del producto comprado
`price` | `float` | Precio de la compra
`currency` | `string` | Moneda de la compra
`properties` | `string` | Propiedades personalizadas de la compra almacenadas como una cadena codificada en JSON
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador de publicidad
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` O `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado para el dispositivo
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPURCHASESHARED #USERSBEHAVIORSPURCHASESHARED" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que desinstaló
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación que fue desinstalada
`time` | `int` | Marca de tiempo Unix en la que el usuario desinstaló
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUNINSTALLSHARED #USERSBEHAVIORSUNINSTALLSHARED" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que actualizó la aplicación
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación que el usuario actualizó
`time` | `int` | Marca de tiempo Unix en la que el usuario actualizó la aplicación
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que el usuario actualizó la aplicación
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`old_app_version` | `null,`&nbsp;`string` | Versión anterior de la aplicación
`new_app_version` | `null,`&nbsp;`string` | Nueva versión de la aplicación
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUPGRADEDAPPSHARED #USERSBEHAVIORSUPGRADEDAPPSHARED" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realiza esta acción
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo esta sesión
`time` | `int` | Marca de tiempo Unix en la que comenzó la sesión
`session_id` | `string` | UUID de la sesión
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo la sesión
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante la sesión
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPFIRSTSESSIONSHARED #USERSBEHAVIORSAPPFIRSTSESSIONSHARED" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo este evento
`time` | `int` | Marca de tiempo UNIX en la que se produjo el evento
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED #USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realiza esta acción
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo esta sesión
`time` | `int` | Marca de tiempo Unix en la que finalizó la sesión
`duration` | `null, float` | Duración de la sesión en segundos
`session_id` | `string` | UUID de la sesión
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo la sesión
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante la sesión
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONENDSHARED #USERSBEHAVIORSAPPSESSIONENDSHARED" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realiza esta acción
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo esta sesión
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que comenzó la sesión
`session_id` | `string` | UUID de la sesión
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo la sesión
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante la sesión
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONSTARTSHARED #USERSBEHAVIORSAPPSESSIONSTARTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó el evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo esta acción
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó el evento
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo el evento personalizado
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`event_type` | `string` | Qué tipo de evento de geovalla se activó (por ejemplo, 'enter' o 'exit')
`location_set_id` | `string` | El ID del conjunto de ubicaciones de la geovalla que se activó
`geofence_id` | `string` | El ID de la geovalla que se activó
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCEDATAEVENTSHARED #USERSBEHAVIORSGEOFENCEDATAEVENTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó el evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo esta acción
`time` | `int` | Marca de tiempo Unix en la que el usuario realizó el evento
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo el evento personalizado
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`event_type` | `string` | Qué tipo de evento de geovalla se activó (por ejemplo, 'enter' o 'exit')
`location_set_id` | `string` | El ID del conjunto de ubicaciones de la geovalla que se activó
`geofence_id` | `string` | El ID de la geovalla que se activó
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCERECORDEVENTSHARED #USERSBEHAVIORSGEOFENCERECORDEVENTSHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`time` | `int` | Marca de tiempo UNIX en la que se produjo el evento
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`activity_attributes_type` | `null,`&nbsp;`string` | Tipo de atributo de Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Token push to start de Live Activity
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`ios_push_token_apns_gateway` | `null, int` | Puerta de enlace APN del token push, solo aplica a tokens push de iOS, 1 para desarrollo, 2 para producción
`push_token_state_change_type` | `null,`&nbsp;`string` | Descripción del tipo de cambio de estado del token push
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`time` | `int` | Marca de tiempo UNIX en la que se produjo el evento
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`activity_id` | `null,`&nbsp;`string` | Identificador de Live Activity
`update_token` | `null,`&nbsp;`string` | Token de actualización de Live Activity
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que se produjo el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`ios_push_token_apns_gateway` | `null, int` | Puerta de enlace APN del token push, solo aplica a tokens push de iOS, 1 para desarrollo, 2 para producción
`push_token_state_change_type` | `null,`&nbsp;`string` | Descripción del tipo de cambio de estado del token push
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que se produjo el evento
`time_ms` | `int` | Tiempo en milisegundos en el que se produjo el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`push_token` | `null,`&nbsp;`string` | Token push del evento
`push_token_created_at` | `null, int` | Marca de tiempo UNIX en la que se creó el token push
`push_token_updated_at` | `null, int` | Marca de tiempo UNIX en la que se actualizó por última vez el token push
`push_token_foreground_push_disabled` | `null, boolean` | Indicador de push en primer plano deshabilitado del token push
`push_token_device_id` | `null,`&nbsp;`string` | ID de dispositivo del token push
`push_token_provisionally_opted_in` | `null, boolean` | Indicador de adhesión voluntaria provisional del token push
`ios_push_token_apns_gateway` | `null, int` | Puerta de enlace APN del token push, solo aplica a tokens push de iOS, 1 para desarrollo, 2 para producción
`web_push_token_public_key` | `null,`&nbsp;`string` | Clave pública del token push, solo aplica a tokens push web
`web_push_token_user_auth` | `null,`&nbsp;`string` | Autenticación de usuario del token push, solo aplica a tokens push web
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | Clave pública VAPID del token push, solo aplica a tokens push web
`push_token_state_change_type` | `null,`&nbsp;`string` | Descripción del tipo de cambio de estado del token push
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que se produjo este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED #USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario afectado
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`email_address` | `null,`&nbsp;`string` | [PII] Dirección de correo electrónico del usuario
`state_change_source` | `null,`&nbsp;`string` | Origen del cambio de estado (REST, SDK, panel, etc.)
`subscription_status` | `string` | Estado de suscripción: 'Subscribed', 'Unsubscribed' u 'Opted In'
`channel` | `null,`&nbsp;`string` | Canal del estado de suscripción global, como correo electrónico
`time` | `int` | Marca de tiempo Unix en la que cambió el estado de suscripción
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación a la que pertenece el evento
`campaign_id` | `null,`&nbsp;`string` | ID interno de Braze de Campaign a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de Campaign a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje a la que pertenece este evento
`canvas_id` | `null,`&nbsp;`string` | ID interno de Braze del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje del que se originó esta acción de cambio de estado de suscripción
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`channel_identifier` | `null,`&nbsp;`string` | [PII] Identificador del usuario en el canal al que corresponde el evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario afectado
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`email_address` | `null,`&nbsp;`string` | [PII] Dirección de correo electrónico del usuario
`phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario en formato e164
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación a la que pertenece el evento
`campaign_id` | `null,`&nbsp;`string` | ID interno de Braze de Campaign a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de Campaign a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje a la que pertenece este evento
`canvas_id` | `null,`&nbsp;`string` | ID interno de Braze del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`channel` | `null,`&nbsp;`string` | Canal: 'email' o 'sms', dependiendo del tipo de canal del grupo de suscripción
`subscription_status` | `string` | Estado de suscripción: 'Subscribed', 'Unsubscribed' u 'Opted In'
`time` | `int` | Marca de tiempo Unix en la que cambió el estado de suscripción
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje del que se originó esta acción de cambio de estado de suscripción
`state_change_source` | `null,`&nbsp;`string` | Origen del cambio de estado (REST, SDK, panel, etc.)
`app_group_id` | `null,`&nbsp;`string` | BSON ID del grupo de aplicaciones al que pertenece este usuario
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`channel_identifier` | `null,`&nbsp;`string` | [PII] Identificador del usuario en el canal al que corresponde el evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED" }

## Campaigns {#campaigns}

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`conversion_behavior_index` | `null, int` | Índice del comportamiento de conversión
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSCONVERSIONSHARED #USERSCAMPAIGNSCONVERSIONSHARED" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSENROLLINCONTROLSHARED #USERSCAMPAIGNSENROLLINCONTROLSHARED" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`channel` | `null,`&nbsp;`string` | Canal al que pertenece este evento
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSFREQUENCYCAPSHARED #USERSCAMPAIGNSFREQUENCYCAPSHARED" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`revenue` | `long` | La cantidad de ingresos en USD generados, expresada en centavos
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSREVENUESHARED #USERSCAMPAIGNSREVENUESHARED" }

## Canvas {#canvas}

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Campo                                  | Tipo                     | Descripción                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalmente único para este evento                                                                           |
| `user_id`                              | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                                                                  |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                                                                    |
| `device_id`                            | `string`,&nbsp;`null`    | ID del dispositivo vinculado a este usuario, si el usuario es anónimo                                           |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario                                                 |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario                                                   |
| `time`                                 | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                                                                 |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento                                              |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                                                                |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento                                                |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID de API del paso en Canvas al que pertenece este evento                                                        |
| `progression_type`                     | `string`,&nbsp;`null`    | Tipo de evento de progresión de paso                                                                             |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Si se trata de una entrada a un primer paso en un Canvas                                                         |
| `exit_reason`                          | `string`,&nbsp;`null`    | Si se trata de una salida, la razón por la que el usuario salió del Canvas durante el paso                       |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Identificador único para esta instancia de un usuario en un Canvas                                               |
| `next_step_id`                         | `string`,&nbsp;`null`    | ID BSON del siguiente paso en el Canvas                                                                          |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | ID de API del siguiente paso en el Canvas                                                                        |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASSTEPPROGRESSIONSHARED #USERSCANVASSTEPPROGRESSIONSHARED" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Campo                                  | Tipo                     | Descripción                                                                                                           |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalmente único para este evento                                                                                 |
| `user_id`                              | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                                                                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                                                                          |
| `device_id`                            | `string`,&nbsp;`null`    | ID del dispositivo vinculado a este usuario, si el usuario es anónimo                                                 |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario                                                       |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario                                                         |
| `time`                                 | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                                                                       |
| `app_api_id`                           | `string`,&nbsp;`null`    | ID de API de la aplicación en la que ocurrió este evento                                                               |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento                                                    |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                                                                      |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento                                                      |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID de API del paso en Canvas al que pertenece este evento                                                              |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID de API de la variante de mensaje del paso en Canvas que recibió este usuario                                        |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | Tipo de evento de conversión que realizó el usuario, donde "0" es una conversión primaria y "1" es una conversión secundaria |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Género del usuario                                                                                              |
| `country`                              | `string`,&nbsp;`null`    | [PII] País del usuario                                                                                                |
| `timezone`                             | `string`,&nbsp;`null`    | Zona horaria del usuario                                                                                               |
| `language`                             | `string`,&nbsp;`null`    | [PII] Idioma del usuario                                                                                              |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASCONVERSIONSHARED #USERSCANVASCONVERSIONSHARED" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Campo                     | Tipo                     | Descripción                                                              |
| ------------------------- | ------------------------ | ------------------------------------------------------------------------ |
| `id`                      | `string`,&nbsp;`null`    | ID globalmente único para este evento                                    |
| `user_id`                 | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                           |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                             |
| `device_id`               | `string`,&nbsp;`null`    | ID del dispositivo vinculado a este usuario, si el usuario es anónimo    |
| `app_group_id`            | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario          |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario            |
| `time`                    | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                          |
| `canvas_id`               | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento       |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                         |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento         |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [Obsoleto] ID de API del paso en Canvas al que pertenece este evento      |
| `gender`                  | `string`,&nbsp;`null`    | [PII] Género del usuario                                                 |
| `country`                 | `string`,&nbsp;`null`    | [PII] País del usuario                                                   |
| `timezone`                | `string`,&nbsp;`null`    | Zona horaria del usuario                                                  |
| `language`                | `string`,&nbsp;`null`    | [PII] Idioma del usuario                                                 |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Verdadero si el usuario fue inscrito en el grupo de control              |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASENTRYSHARED #USERSCANVASENTRYSHARED" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Campo                     | Tipo                     | Descripción                                                              |
| ------------------------- | ------------------------ | ------------------------------------------------------------------------ |
| `id`                      | `string`,&nbsp;`null`    | ID globalmente único para este evento                                    |
| `user_id`                 | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                           |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                             |
| `app_group_id`            | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario          |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario            |
| `time`                    | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                          |
| `canvas_id`               | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento       |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                         |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento         |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID de API del paso en Canvas al que pertenece este evento                 |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED #USERSCANVASEXITMATCHEDAUDIENCESHARED" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Campo                     | Tipo                     | Descripción                                                              |
| ------------------------- | ------------------------ | ------------------------------------------------------------------------ |
| `id`                      | `string`,&nbsp;`null`    | ID globalmente único para este evento                                    |
| `user_id`                 | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                           |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                             |
| `app_group_id`            | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario          |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario            |
| `time`                    | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                          |
| `canvas_id`               | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento       |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                         |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento         |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID de API del paso en Canvas al que pertenece este evento                 |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITPERFORMEDEVENTSHARED #USERSCANVASEXITPERFORMEDEVENTSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Campo                       | Tipo                     | Descripción                                                                                                           |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | ID globalmente único para este evento                                                                                 |
| `user_id`                   | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                                                                        |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                                                                          |
| `app_group_id`              | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario                                                       |
| `time`                      | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                                                                       |
| `app_api_id`                | `string`,&nbsp;`null`    | ID de API de la aplicación en la que ocurrió este evento                                                               |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento                                                    |
| `canvas_api_id`             | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                                                                      |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento                                                      |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | ID de API del paso en Canvas al que pertenece este evento                                                              |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | ID de API del paso de experimento al que pertenece este evento                                                         |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | Tipo de evento de conversión que realizó el usuario, donde "0" es una conversión primaria y "1" es una conversión secundaria |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                                                                   |
| `experiment_split_api_id` | `string`,&nbsp;`null` | ID de API de la división de experimento en la que se inscribió el usuario |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED #USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Campo                     | Tipo                     | Descripción                                                              |
| ------------------------- | ------------------------ | ------------------------------------------------------------------------ |
| `id`                      | `string`,&nbsp;`null`    | ID globalmente único para este evento                                    |
| `user_id`                 | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                           |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                             |
| `app_group_id`            | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario          |
| `time`                    | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                          |
| `canvas_id`               | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento       |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                         |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento         |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID de API del paso en Canvas al que pertenece este evento                 |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | ID de API del paso de experimento al que pertenece este evento            |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Verdadero si el usuario fue inscrito en el grupo de control              |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

| `experiment_split_api_id` | `string`,&nbsp;`null` | ID de API de la división de experimento en la que se inscribió el usuario |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED #USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Campo                                  | Tipo                     | Descripción                                                              |
| -------------------------------------- | ------------------------ | ------------------------------------------------------------------------ |
| `id`                                   | `string`,&nbsp;`null`    | ID globalmente único para este evento                                    |
| `user_id`                              | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                           |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                             |
| `device_id`                            | `string`,&nbsp;`null`    | ID del dispositivo vinculado a este usuario, si el usuario es anónimo    |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario          |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario            |
| `time`                                 | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                          |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento       |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                         |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento         |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID de API del paso en Canvas al que pertenece este evento                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID de API de la variante de mensaje del paso en Canvas que recibió este usuario |
| `channel`                              | `string`,&nbsp;`null`    | Canal de mensajería al que pertenece este evento (correo electrónico, push, etc.) |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Género del usuario                                                 |
| `country`                              | `string`,&nbsp;`null`    | [PII] País del usuario                                                   |
| `timezone`                             | `string`,&nbsp;`null`    | Zona horaria del usuario                                                  |
| `language`                             | `string`,&nbsp;`null`    | [PII] Idioma del usuario                                                 |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASFREQUENCYCAPSHARED #USERSCANVASFREQUENCYCAPSHARED" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Campo                                  | Tipo                     | Descripción                                                              |
| -------------------------------------- | ------------------------ | ------------------------------------------------------------------------ |
| `id`                                   | `string`,&nbsp;`null`    | ID globalmente único para este evento                                    |
| `user_id`                              | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                           |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                             |
| `device_id`                            | `string`,&nbsp;`null`    | ID del dispositivo vinculado a este usuario, si el usuario es anónimo    |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario          |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario            |
| `time`                                 | `int`,&nbsp;`null`       | Marca de tiempo Unix en la que ocurrió el evento                          |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Solo para uso de Braze) ID del Canvas al que pertenece este evento       |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID de API del Canvas al que pertenece este evento                         |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID de API de la variante de Canvas a la que pertenece este evento         |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID de API del paso en Canvas al que pertenece este evento                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID de API de la variante de mensaje del paso en Canvas que recibió este usuario |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Género del usuario                                                 |
| `country`                              | `string`,&nbsp;`null`    | [PII] País del usuario                                                   |
| `timezone`                             | `string`,&nbsp;`null`    | Zona horaria del usuario                                                  |
| `language`                             | `string`,&nbsp;`null`    | [PII] Idioma del usuario                                                 |
| `revenue`                              | `int`,&nbsp;`null`       | Cantidad de ingresos generados en USD, expresada en centavos             |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe                     |
| `app_api_id` | `string`,&nbsp;`null` | ID de API de la aplicación en la que ocurrió este evento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASREVENUESHARED #USERSCANVASREVENUESHARED" }

## Mensajes {#messages}


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo - extraído de user_agent - en el que ocurrió la apertura
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador publicitario
`ad_id_type` | `null,`&nbsp;`string` | Uno de ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está habilitado para el dispositivo
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (hasta 128 caracteres)
`banner_placement_id` | `null,`&nbsp;`string` | ID de ubicación de banner especificado por el cliente
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERABORTSHARED #USERSMESSAGESBANNERABORTSHARED" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo - extraído de user_agent - en el que ocurrió la apertura
`button_id` | `null,`&nbsp;`string` | ID del botón en el que se hizo clic, si este clic representa un clic en un botón
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador publicitario
`ad_id_type` | `null,`&nbsp;`string` | Uno de ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está habilitado para el dispositivo
`banner_placement_id` | `null,`&nbsp;`string` | ID de ubicación de banner especificado por el cliente
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERCLICKSHARED #USERSMESSAGESBANNERCLICKSHARED" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo - extraído de user_agent - en el que ocurrió la apertura
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador publicitario
`ad_id_type` | `null,`&nbsp;`string` | Uno de ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está habilitado para el dispositivo
`banner_placement_id` | `null,`&nbsp;`string` | ID de ubicación de banner especificado por el cliente
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERIMPRESSIONSHARED #USERSMESSAGESBANNERIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (máximo 2000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDABORTSHARED #USERSMESSAGESCONTENTCARDABORTSHARED" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`content_card_id` | `string` | ID de la tarjeta que generó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador publicitario
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` o `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está habilitado para el dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDCLICKSHARED #USERSMESSAGESCONTENTCARDCLICKSHARED" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`content_card_id` | `string` | ID de la tarjeta que generó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador publicitario
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` o `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está habilitado para el dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDDISMISSSHARED #USERSMESSAGESCONTENTCARDDISMISSSHARED" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`content_card_id` | `string` | ID de la tarjeta que generó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador publicitario
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` o `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento publicitario está habilitado para el dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDIMPRESSIONSHARED #USERSMESSAGESCONTENTCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`content_card_id` | `string` | ID de la tarjeta que generó este evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,`&nbsp;`string` | [PII] Cadena JSON de los pares clave-valor etiquetados durante el renderizado Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDSENDSHARED #USERSMESSAGESCONTENTCARDSENDSHARED" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (máximo 2000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILABORTSHARED #USERSMESSAGESEMAILABORTSHARED" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`sending_ip` | `null,`&nbsp;`string` | Dirección IP desde la que se realizó el envío de correo electrónico
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`bounce_reason` | `null,`&nbsp;`string` | [PII] Código de razón SMTP y mensaje descriptivo recibidos para este evento de rebote
`esp` | `null,`&nbsp;`string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Dominio de envío del correo electrónico
`is_drop` | `null, boolean` | Indica que este evento cuenta como un evento de descarte
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILBOUNCESHARED #USERSMESSAGESEMAILBOUNCESHARED" }

{% alert note %}
Es posible que veas múltiples filas para el mismo usuario en torno a un solo rebote duro. Esto puede ocurrir cuando los eventos se procesan de forma asíncrona o cuando los envíos relacionados tienen valores de `dispatch_id` diferentes. Al deduplicar o analizar exportaciones, considera `dispatch_id`, `time` e `id` en conjunto.
{% endalert %}

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`url` | `null,`&nbsp;`string` | URL en la que el usuario hizo clic
`user_agent` | `null,`&nbsp;`string` | Agente de usuario en el que ocurrió el clic
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`link_id` | `null,`&nbsp;`string` | ID único para el enlace en el que se hizo clic, creado por Braze
`link_alias` | `null,`&nbsp;`string` | Alias asociado con este ID de enlace
`esp` | `null,`&nbsp;`string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Dominio de envío del correo electrónico
`is_amp` | `null, boolean` | Indica que se trata de un evento AMP
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_suspected_bot_click` | `null, boolean` | Si este evento fue procesado como un evento de bot
`suspected_bot_click_reason` | `null, object` | Por qué este evento fue clasificado como bot
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILCLICKSHARED #USERSMESSAGESEMAILCLICKSHARED" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`email_address` | `null,`&nbsp;`string` | [PII] Dirección de correo electrónico del usuario
`recipient_domain` | `null,`&nbsp;`string` | Dominio de correo electrónico del destinatario
`esp` | `null,`&nbsp;`string` | ESP relacionado con el evento (Sparkpost, Sendgrid o Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Dominio de envío del correo electrónico
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`sending_ip` | `null,`&nbsp;`string` | Dirección IP desde la que se realizó el envío de correo electrónico
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`deferral_reason` | `null,`&nbsp;`string` | [PII] Código de razón SMTP y mensaje descriptivo recibidos para este evento de aplazamiento
`attempt_count` | `null, int` | Número de intentos realizados para enviar el mensaje
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDEFERRALSHARED #USERSMESSAGESEMAILDEFERRALSHARED" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`sending_ip` | `null,`&nbsp;`string` | Dirección IP desde la que se envió el correo electrónico
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`esp` | `null,`&nbsp;`string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Dominio de envío del correo electrónico
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDELIVERYSHARED #USERSMESSAGESEMAILDELIVERYSHARED" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`user_agent` | `null,`&nbsp;`string` | Agente de usuario en el que se realizó el informe de correo no deseado
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`esp` | `null,`&nbsp;`string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Dominio de envío del correo electrónico
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILMARKASSPAMSHARED #USERSMESSAGESEMAILMARKASSPAMSHARED" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`user_agent` | `null,`&nbsp;`string` | Agente de usuario en el que ocurrió la apertura
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`machine_open` | `null,`&nbsp;`string` | Se establece como 'true' si el evento de apertura se activó sin interacción del usuario, por ejemplo, por un dispositivo Apple con la protección de la privacidad en los correos electrónicos habilitada. El valor puede cambiar con el tiempo para proporcionar mayor granularidad.
`esp` | `null,`&nbsp;`string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Dominio de envío del correo electrónico
`is_amp` | `null, boolean` | Indica que se trata de un evento AMP
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILOPENSHARED #USERSMESSAGESEMAILOPENSHARED" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`message_extras` | `null,`&nbsp;`string` | [PII] Cadena JSON de los pares clave-valor etiquetados durante el renderizado Liquid
`esp` | `null,`&nbsp;`string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Dominio de envío del correo electrónico
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSENDSHARED #USERSMESSAGESEMAILSENDSHARED" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`sending_ip` | `null,`&nbsp;`string` | Dirección IP desde la que se realizó el envío de correo electrónico
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`bounce_reason` | `null,`&nbsp;`string` | [PII] Código de razón SMTP y mensaje descriptivo recibidos para este evento de rebote
`esp` | `null,`&nbsp;`string` | ESP relacionado con el evento (SparkPost, SendGrid o Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Dominio de envío del correo electrónico
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSOFTBOUNCESHARED #USERSMESSAGESEMAILSOFTBOUNCESHARED" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Esta tabla registra las cancelaciones de suscripción a correo electrónico a nivel de mensaje desde el lado del destinatario: hacer clic en un enlace de cancelación de suscripción, la función List-Unsubscribe de un clic del cliente de correo electrónico, envíos del centro de preferencias y cancelaciones de suscripción reportadas por el ESP. No se incluyen las cancelaciones de suscripción realizadas a través de la REST API; esas emiten eventos [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) o [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events) en su lugar.

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID de usuario externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `string` | [PII] Dirección de correo electrónico del usuario
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el que se realizó el envío de correo electrónico
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILUNSUBSCRIBESHARED #USERSMESSAGESEMAILUNSUBSCRIBESHARED" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Este evento ocurre cuando un mensaje es despriorizado o tiene un límite de frecuencia aplicado y se reintenta más tarde dentro de la ventana de reintento configurada.

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | [PII] ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`retry_type` | `null,`&nbsp;`string` | Tipo de reintento
`retry_log` | `null,`&nbsp;`string` | Mensaje de registro que describe los detalles del reintento
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`email_address` | `null,`&nbsp;`string` | [PII] Dirección de correo electrónico del usuario
`ip_pool` | `null,`&nbsp;`string` | Pool de IP desde el cual se realizó el envío de correo electrónico
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILRETRYSHARED #USERSMESSAGESEMAILRETRYSHARED" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`feature_flag_id_name` | `null,`&nbsp;`string` | Identificador del despliegue del conmutador de características
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo, extraído de user_agent, en el que ocurrió la apertura
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED #USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`card_api_id` | `null,`&nbsp;`string` | ID de API de la tarjeta
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`version` | `string` | Versión del mensaje dentro de la aplicación, heredada o activada
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador de publicidad
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` o `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado para el dispositivo
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (máximo de 2000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEABORTSHARED #USERSMESSAGESINAPPMESSAGEABORTSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`card_api_id` | `null,`&nbsp;`string` | ID de API de la tarjeta
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`version` | `string` | Versión del mensaje dentro de la aplicación, heredada o activada
`button_id` | `null,`&nbsp;`string` | ID del botón pulsado, si este clic representa un clic en un botón
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador de publicidad
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` o `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado para el dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGECLICKSHARED #USERSMESSAGESINAPPMESSAGECLICKSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`card_api_id` | `null,`&nbsp;`string` | ID de API de la tarjeta
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`version` | `string` | Versión del mensaje dentro de la aplicación, heredada o activada
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador de publicidad
`ad_id_type` | `null,`&nbsp;`string` | Uno de `ios_idfa`, `google_ad_id`, `windows_ad_id` o `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado para el dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,`&nbsp;`string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid
`locale_key` | `null,`&nbsp;`string` | [PII] La clave correspondiente a las traducciones (por ejemplo, 'en-us') utilizada para componer este mensaje (nulo para el predeterminado).
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED #USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (hasta 128 caracteres)
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`line_channel_id` | `null,`&nbsp;`string` | El ID de canal de LINE al que se envió o desde el que se recibió el mensaje
`line_channel_name` | `null,`&nbsp;`string` | El nombre de canal de LINE al que se envió o desde el que se recibió el mensaje
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`native_line_id` | `null,`&nbsp;`string` | [PII] El ID de Line del usuario desde el que se envió o recibió el mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEABORTSHARED #USERSMESSAGESLINEABORTSHARED" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`native_line_id` | `null,`&nbsp;`string` | [PII] El ID de Line del usuario desde el que se envió o recibió el mensaje
`line_channel_id` | `null,`&nbsp;`string` | El ID de canal de LINE al que se envió o desde el que se recibió el mensaje
`line_channel_name` | `null,`&nbsp;`string` | El nombre de canal de LINE al que se envió o desde el que se recibió el mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`is_suspected_bot_click` | `null, boolean` | Si este evento fue procesado como un evento de bot
`short_url` | `null,`&nbsp;`string` | URL acortada que fue pulsada
`url` | `null,`&nbsp;`string` | URL en la que hizo clic el usuario
`user_agent` | `null,`&nbsp;`string` | User agent en el que ocurrió el informe de correo no deseado
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINECLICKSHARED #USERSMESSAGESLINECLICKSHARED" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`line_channel_id` | `null,`&nbsp;`string` | El ID de canal de LINE al que se envió o desde el que se recibió el mensaje
`line_channel_name` | `null,`&nbsp;`string` | El nombre de canal de LINE al que se envió o desde el que se recibió el mensaje
`media_id` | `null,`&nbsp;`string` | El ID generado por LINE que se puede usar para recuperar medios entrantes desde LINE
`message_body` | `null,`&nbsp;`string` | Respuesta escrita por el usuario
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`native_line_id` | `null,`&nbsp;`string` | [PII] El ID de Line del usuario desde el que se envió o recibió el mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEINBOUNDRECEIVESHARED #USERSMESSAGESLINEINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`line_channel_id` | `null,`&nbsp;`string` | El ID de canal de LINE al que se envió o desde el que se recibió el mensaje
`line_channel_name` | `null,`&nbsp;`string` | El nombre de canal de LINE al que se envió o desde el que se recibió el mensaje
`message_extras` | `null,`&nbsp;`string` | [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`native_line_id` | `null,`&nbsp;`string` | [PII] El ID de Line del usuario desde el que se envió o recibió el mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINESENDSHARED #USERSMESSAGESLINESENDSHARED" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Este evento ocurre cuando un mensaje es despriorizado o tiene un límite de frecuencia aplicado y se reintenta más tarde dentro de la ventana de reintento configurada.

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | [PII] ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`retry_type` | `null,`&nbsp;`string` | Tipo de reintento
`retry_log` | `null,`&nbsp;`string` | Mensaje de registro que describe los detalles del reintento
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`line_channel_id` | `null,`&nbsp;`string` | El ID de canal de LINE al que se envió o desde el que se recibió el mensaje
`line_channel_name` | `null,`&nbsp;`string` | El nombre de canal de LINE al que se envió o desde el que se recibió el mensaje
`native_line_id` | `null,`&nbsp;`string` | [PII] El ID de Line del usuario desde el que se envió o recibió el mensaje
`subscription_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de suscripción
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINERETRYSHARED #USERSMESSAGESLINERETRYSHARED" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`activity_id` | `null,`&nbsp;`string` | Identificador de Live Activity
`activity_attributes_type` | `null,`&nbsp;`string` | Tipo de atributo de Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Token push de inicio de Live Activity
`update_token` | `null,`&nbsp;`string` | Token de actualización de Live Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Tipo de evento de Live Activity. Uno de ['start', 'update', 'end']
`live_activity_event_outcome` | `null,`&nbsp;`string` | Resultado del evento de Live Activity
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYOUTCOMESHARED #USERSMESSAGESLIVEACTIVITYOUTCOMESHARED" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`activity_id` | `null,`&nbsp;`string` | Identificador de Live Activity
`activity_attributes_type` | `null,`&nbsp;`string` | Tipo de atributo de Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Token push de inicio de Live Activity
`update_token` | `null,`&nbsp;`string` | Token de actualización de Live Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Tipo de evento de Live Activity. Uno de ['start', 'update', 'end']
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYSENDSHARED #USERSMESSAGESLIVEACTIVITYSENDSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`card_api_id` | `null,`&nbsp;`string` | ID de API de la tarjeta
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo, extraído de user_agent, en el que ocurrió la apertura
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (hasta 128 caracteres)
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDABORTSHARED #USERSMESSAGESNEWSFEEDCARDABORTSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`card_api_id` | `null,`&nbsp;`string` | ID de API de la tarjeta
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo, extraído de user_agent, en el que ocurrió la apertura
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDCLICKSHARED #USERSMESSAGESNEWSFEEDCARDCLICKSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`card_api_id` | `null,`&nbsp;`string` | ID de API de la tarjeta
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo, extraído de user_agent, en el que ocurrió la apertura
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED #USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` al que se intentó realizar la entrega
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`platform` | `string` | Plataforma del dispositivo
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (máximo de 2000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONABORTSHARED #USERSMESSAGESPUSHNOTIFICATIONABORTSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`push_token` | `null,`&nbsp;`string` | Token de notificaciones push que rebotó
`device_id` | `null,`&nbsp;`string` | `device_id` al que se intentó realizar la entrega y que rebotó
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`ad_id` | `null,`&nbsp;`string` | [PII] Identificador de publicidad del dispositivo al que se intentó realizar la entrega
`ad_id_type` | `null,`&nbsp;`string` | Tipo del identificador de publicidad
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado o no
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED #USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del despacho al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por el Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Este evento no es compatible con el [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) y está obsoleto en el [SDK Obj-C](https://github.com/Appboy/appboy-ios-sdk).
{% endalert %}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`ad_id` | `null,`&nbsp;`string` | [PII] ID de publicidad del dispositivo al que se intentó realizar la entrega
`ad_id_type` | `null,`&nbsp;`string` | Tipo de ID de publicidad
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado o no
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED #USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`sdk_version` | `null,`&nbsp;`string` | Versión del SDK de Braze en uso durante el evento
`platform` | `null,`&nbsp;`string` | Plataforma del dispositivo
`os_version` | `null,`&nbsp;`string` | Versión del sistema operativo del dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo del dispositivo
`resolution` | `null,`&nbsp;`string` | Resolución del dispositivo
`carrier` | `null,`&nbsp;`string` | Operador del dispositivo
`browser` | `null,`&nbsp;`string` | Navegador del dispositivo
`button_string` | `null,`&nbsp;`string` | Identificador (button_string) del botón de la notificación push que se pulsó. null si no proviene de un clic en un botón
`button_action_type` | `null,`&nbsp;`string` | Tipo de acción del botón de la notificación push. Uno de [URI, DEEP_LINK, NONE, CLOSE]. null si no proviene de un clic en un botón
`slide_id` | `null,`&nbsp;`string` | Identificador de la diapositiva del carrusel push en la que el usuario hizo clic
`slide_action_type` | `null,`&nbsp;`string` | Tipo de acción de la diapositiva del carrusel push
`ad_id` | `null,`&nbsp;`string` | [PII] ID de publicidad del dispositivo al que se intentó realizar la entrega
`ad_id_type` | `null,`&nbsp;`string` | Tipo de ID de publicidad
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado o no
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID globalmente único para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`push_token` | `null,`&nbsp;`string` | Token de notificaciones push al que se intentó realizar la entrega
`device_id` | `null,`&nbsp;`string` | `device_id` al que se intentó realizar la entrega
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`app_api_id` | `null,`&nbsp;`string` | ID de API de la aplicación en la que ocurrió este evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`platform` | `string` | Plataforma del dispositivo
`ad_id` | `null,`&nbsp;`string` | [PII] ID de publicidad del dispositivo al que se intentó realizar la entrega
`ad_id_type` | `null,`&nbsp;`string` | Tipo de ID de publicidad
`ad_tracking_enabled` | `null, boolean` | Si el seguimiento de publicidad está habilitado o no
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,`&nbsp;`string` | [PII] Cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid
`is_sampled` | `null,`&nbsp;`string` | Indica si el envío push fue muestreado y se esperaba un evento de entrega
`locale_key` | `null,`&nbsp;`string` | [PII] Clave correspondiente a las traducciones (por ejemplo, 'en-us') utilizada para componer este mensaje (null para el predeterminado).
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONSENDSHARED #USERSMESSAGESPUSHNOTIFICATIONSENDSHARED" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID globalmente único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (hasta 128 caracteres)
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,`&nbsp;`string` | Nombre del Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nombre de la variante de Canvas que recibió este usuario
`message_variation_name` | `null,`&nbsp;`string` | Nombre de la variante del mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSABORTSHARED #USERSMESSAGESRCSABORTSHARED" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID globalmente único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,`&nbsp;`string` | Nombre del Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`is_suspected_bot_click` | `null, boolean` | Si este evento fue procesado como un evento de bot
`message_variation_name` | `null,`&nbsp;`string` | Nombre de la variante del mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`short_url` | `null,`&nbsp;`string` | URL acortada en la que se hizo clic
`suspected_bot_click_reason` | `null,`&nbsp;`string` | Razón por la que este evento fue clasificado como bot
`user_agent` | `null,`&nbsp;`string` | Agente de usuario en el que ocurrió el informe de correos no deseados
`user_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario desde el que se recibió el mensaje
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`interaction_type` | `null,`&nbsp;`string` | Tipo de interacción que generó el clic. Valores de cadena de ejemplo: Text URL, Reply, OpenURL
`element_label` | `null,`&nbsp;`string` | Detalles opcionales sobre el elemento en el que se hizo clic, como el texto de una respuesta sugerida o un botón
`element_type` | `null,`&nbsp;`string` | Especifica si un interaction_type común entre sugerencias y botones provino de una sugerencia o un botón. Ejemplos: Suggestion, Button
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`url` | `null,`&nbsp;`string` | URL en la que el usuario hizo clic
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`canvas_variation_name` | `null,`&nbsp;`string` | Nombre de la variante de Canvas que recibió este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSCLICKSHARED #USERSMESSAGESRCSCLICKSHARED" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID globalmente único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,`&nbsp;`string` | Nombre del Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nombre de la variante de Canvas que recibió este usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`message_variation_name` | `null,`&nbsp;`string` | Nombre de la variante del mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164 (por ejemplo, +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`from_rcs_sender` | `null,`&nbsp;`string` | ID del remitente RCS o nombre de agente utilizado para enviar el mensaje
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSDELIVERYSHARED #USERSMESSAGESRCSDELIVERYSHARED" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID globalmente único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`action` | `null,`&nbsp;`string` | Acción realizada en respuesta a este mensaje. (por ejemplo, Subscribed, Unsubscribed o None).
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,`&nbsp;`string` | Nombre del Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`media_urls` | `null,`&nbsp;`string` | URL de medios del usuario
`message_variation_name` | `null,`&nbsp;`string` | Nombre de la variante del mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`user_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario desde el que se recibió el mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`message_body` | `null,`&nbsp;`string` | Respuesta escrita del usuario
`to_rcs_sender` | `null,`&nbsp;`string` | Remitente RCS entrante al que se envió el mensaje
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSINBOUNDRECEIVESHARED #USERSMESSAGESRCSINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID globalmente único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,`&nbsp;`string` | Nombre del Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nombre de la variante de Canvas que recibió este usuario
`message_variation_name` | `null,`&nbsp;`string` | Nombre de la variante del mensaje
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164 (por ejemplo, +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREADSHARED #USERSMESSAGESRCSREADSHARED" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID globalmente único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,`&nbsp;`string` | Nombre del Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nombre de la variante de Canvas que recibió este usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`error` | `null,`&nbsp;`string` | Nombre del error
`from_rcs_sender` | `null,`&nbsp;`string` | ID del remitente RCS o nombre de agente utilizado para enviar el mensaje
`is_sms_fallback` | `null, boolean` | Indica si se intentó el respaldo por SMS para este mensaje RCS rechazado. Está vinculado/emparejado con el evento de entrega de SMS
`message_variation_name` | `null,`&nbsp;`string` | Nombre de la variante del mensaje
`provider_error_code` | `null,`&nbsp;`string` | Código de error del proveedor
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164 (por ejemplo, +14155552671)
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREJECTIONSHARED #USERSMESSAGESRCSREJECTIONSHARED" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`id` | `string` | ID globalmente único para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_name` | `null,`&nbsp;`string` | Nombre del Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nombre de la variante de Canvas que recibió este usuario
`category` | `null,`&nbsp;`string` | Nombre de la categoría de palabras clave, solo se completa para mensajes de respuesta automática: 'opt-in', 'opt-out', 'help' o valor personalizado
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`from_rcs_sender` | `null,`&nbsp;`string` | ID del remitente RCS o nombre de agente utilizado para enviar el mensaje
`message_extras` | `null,`&nbsp;`string` | Cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid
`message_variation_name` | `null,`&nbsp;`string` | Nombre de la variante del mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164 (por ejemplo, +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje que recibió este usuario
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante del mensaje del paso en Canvas que recibió este usuario
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSSENDSHARED #USERSMESSAGESRCSSENDSHARED" }

## Eventos de mensajes SMS y perfiles de usuario eliminados {#sms-message-events-and-deleted-user-profiles}

{% alert note %}
Para las tablas compartidas `USERS_MESSAGES_SMS_*` (incluidas [`USERS_MESSAGES_SMS_REJECTION_SHARED`](#USERS_MESSAGES_SMS_REJECTION_SHARED), [`USERS_MESSAGES_SMS_DELIVERY_SHARED`](#USERS_MESSAGES_SMS_DELIVERY_SHARED) y [`USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED`](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED)), Braze solo escribe una fila cuando el perfil de usuario de Braze aún existe en el espacio de trabajo en el momento en que el evento se procesa para Snowflake Data Sharing y Currents. Si ese usuario fue eliminado antes de que se complete el procesamiento, el evento no aparece en Snowflake ni en tu exportación de Currents, incluso cuando las métricas del espacio de trabajo de SMS en el panel aún reflejan los recuentos agregados de la ruta de informes de Braze. Para el comportamiento correspondiente en Currents, consulta [Eventos de rechazo de SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) y los tipos de eventos de SMS relacionados en el mismo glosario.
{% endalert %}

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo del grupo de suscripción
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (máximo de 2000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSABORTSHARED #USERSMESSAGESSMSABORTSHARED" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`from_phone_number` | `null,`&nbsp;`string` | Número de teléfono desde el que se envió el mensaje SMS
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo del grupo de suscripción
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSCARRIERSENDSHARED #USERSMESSAGESSMSCARRIERSENDSHARED" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`from_phone_number` | `null,`&nbsp;`string` | Número de teléfono desde el que se envió el mensaje SMS
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo del grupo de suscripción
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_sms_fallback` | `null, boolean` | Indica si se intentó un respaldo por SMS para este mensaje RCS rechazado. Está vinculado/emparejado con el evento de entrega de SMS
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYSHARED #USERSMESSAGESSMSDELIVERYSHARED" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo del grupo de suscripción
`error` | `null,`&nbsp;`string` | Nombre del error
`provider_error_code` | `null,`&nbsp;`string` | Código de error del proveedor de servicios SMS
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_sms_fallback` | `null, boolean` | Indica si se intentó un respaldo por SMS para este mensaje RCS rechazado. Está vinculado/emparejado con el evento de entrega de SMS
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYFAILURESHARED #USERSMESSAGESSMSDELIVERYFAILURESHARED" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `null,`&nbsp;`string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo asociado al número de teléfono entrante
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`user_phone_number` | `string` | [PII] Número de teléfono del usuario desde el que se recibió el mensaje
`subscription_group_id` | `null,`&nbsp;`string` | ID del grupo de suscripción al que se dirigió este mensaje SMS
`subscription_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de suscripción al que se dirigió este mensaje SMS
`inbound_phone_number` | `string` | Número entrante al que se envió el mensaje
`action` | `string` | Acción tomada en respuesta a este mensaje. Por ejemplo, `Subscribed`, `Unsubscribed` o `None`.
`message_body` | `string` | Respuesta del usuario
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL de medios del usuario
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje a la que pertenece este evento
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas a la que pertenece este evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSINBOUNDRECEIVESHARED #USERSMESSAGESSMSINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`from_phone_number` | `null,`&nbsp;`string` | Número de teléfono desde el que se envió el mensaje SMS
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo del grupo de suscripción
`error` | `null,`&nbsp;`string` | Nombre del error
`provider_error_code` | `null,`&nbsp;`string` | Código de error del proveedor de servicios SMS
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_sms_fallback` | `null, boolean` | Indica si se intentó un respaldo por SMS para este mensaje RCS rechazado. Está vinculado/emparejado con el evento de entrega de SMS
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSREJECTIONSHARED #USERSMESSAGESSMSREJECTIONSHARED" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo del grupo de suscripción
`category` | `null,`&nbsp;`string` | Nombre de la categoría de palabras clave, solo se completa para mensajes de respuesta automática: 'Opt-in', 'Opt-out', 'Help' o un valor personalizado
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,`&nbsp;`string` | [PII] Cadena JSON de los pares clave-valor etiquetados durante el renderizado con Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSENDSHARED #USERSMESSAGESSMSSENDSHARED" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `null,`&nbsp;`string` | ID de Braze del usuario al que se dirigió el short_url, nulo si short_url no utilizó seguimiento de clics de usuario
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario al que se dirigió el short_url si existe, nulo si short_url no utilizó seguimiento de clics de usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo utilizado para generar el short_url
`time` | `int` | Marca de tiempo Unix en la que se hizo clic en el short_url
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de la campaña para la que se generó el short_url, nulo si no proviene de una campaña
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña para la que se generó el short_url, nulo si no proviene de una campaña
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje para la que se generó el short_url, nulo si no proviene de una campaña
`canvas_id` | `null,`&nbsp;`string` | ID de Braze del Canvas para el que se generó el short_url, nulo si no proviene de un Canvas
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas para el que se generó el short_url, nulo si no proviene de un Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas para la que se generó el short_url, nulo si no proviene de un Canvas
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas para el que se generó el short_url, nulo si no proviene de un Canvas
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas para la que se generó el short_url, nulo si no proviene de un Canvas
`url` | `string` | URL original contenida en el mensaje a la que redirige el short_url
`short_url` | `string` | URL acortada en la que se hizo clic
`user_agent` | `null,`&nbsp;`string` | Agente de usuario que solicita el short_url
`user_phone_number` | `string` | [PII] Número de teléfono del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`is_suspected_bot_click` | `null, boolean` | Si este evento se procesó como un evento de bot
`suspected_bot_click_reason` | `null, object` | Motivo por el que este evento se clasificó como bot
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSHORTLINKCLICKSHARED #USERSMESSAGESSMSSHORTLINKCLICKSHARED" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Este evento ocurre cuando un mensaje se desprioriza o se limita por frecuencia y se reintenta posteriormente dentro de la ventana de reintentos configurada.

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | [PII] ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`subscription_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de suscripción
`retry_type` | `null,`&nbsp;`string` | Tipo de reintento
`retry_log` | `null,`&nbsp;`string` | Mensaje de registro que describe los detalles del reintento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSRETRYSHARED #USERSMESSAGESSMSRETRYSHARED" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (máximo de 2000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKABORTSHARED #USERSMESSAGESWEBHOOKABORTSHARED" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`http_status_code` | `null, int` | Código de estado HTTP de la respuesta
`endpoint_url` | `null,`&nbsp;`string` | URL del endpoint solicitado
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`content_length` | `null, int` | Longitud del contenido de la respuesta
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`host` | `null,`&nbsp;`string` | Host de la solicitud
`id` | `string` | ID único global para este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`raw_response` | `null,`&nbsp;`string` | Respuesta sin procesar truncada del endpoint
`retry_count` | `null, int` | Número de reintentos realizados
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`url_path` | `null,`&nbsp;`string` | Ruta de la URL solicitada
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`webhook_duration` | `null, int` | Duración total de esta solicitud en milisegundos
`webhook_failure_source` | `null,`&nbsp;`string` | Indica si el error fue generado por Braze o por el propio endpoint. El campo de origen puede ser External Endpoint, Treat no status code to host unreachable
`is_terminal` | `null, boolean` | Si este evento fue el intento final en un envío
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKFAILURESHARED #USERSMESSAGESWEBHOOKFAILURESHARED" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`campaign_name` | `null,`&nbsp;`string` | Nombre de la campaña
`message_variation_name` | `null,`&nbsp;`string` | Nombre de la variante de mensaje
`canvas_name` | `null,`&nbsp;`string` | Nombre del Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nombre de la variante de Canvas que recibió este usuario
`canvas_step_name` | `null,`&nbsp;`string` | Nombre del paso de Canvas
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`message_extras` | `null,`&nbsp;`string` | [PII] Cadena JSON de los pares clave-valor etiquetados durante el renderizado con Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKSENDSHARED #USERSMESSAGESWEBHOOKSENDSHARED" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Este evento ocurre cuando un mensaje se desprioriza o se limita por frecuencia y se reintenta posteriormente dentro de la ventana de reintentos configurada.

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | [PII] ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`gender` | `null,`&nbsp;`string` | [PII] Género del usuario
`country` | `null,`&nbsp;`string` | [PII] País del usuario
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`language` | `null,`&nbsp;`string` | [PII] Idioma del usuario
`retry_type` | `null,`&nbsp;`string` | Tipo de reintento
`retry_log` | `null,`&nbsp;`string` | Mensaje de registro que describe los detalles del reintento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKRETRYSHARED #USERSMESSAGESWEBHOOKRETRYSHARED" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`app_group_id` | `null,`&nbsp;`string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelación. Para ver una lista de valores, consulta [Tipos de cancelación](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Mensaje de registro que describe los detalles de la cancelación (máximo de 2000 caracteres)
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPABORTSHARED #USERSMESSAGESWHATSAPPABORTSHARED" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`url` | `null,`&nbsp;`string` | URL en la que hizo clic el usuario
`short_url` | `null,`&nbsp;`string` | URL acortada en la que se hizo clic
`user_agent` | `null,`&nbsp;`string` | Agente de usuario en el que se produjo el informe de correo no deseado
`user_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario desde el que se recibió el mensaje
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPCLICKSHARED #USERSMESSAGESWHATSAPPCLICKSHARED" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`from_phone_number` | `null,`&nbsp;`string` | Número de teléfono desde el que se envió el mensaje de WhatsApp
`app_group_id` | `null,`&nbsp;`string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`flow_id` | `null,`&nbsp;`string` | ID único del Flow en WhatsApp Manager. Presente si el usuario está respondiendo a un WhatsApp Flow.
`template_name` | `null,`&nbsp;`string` | [PII] Nombre de la plantilla en WhatsApp Manager. Presente si se envía un mensaje de plantilla
`message_id` | `null,`&nbsp;`string` | ID único generado por Meta para este mensaje
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPDELIVERYSHARED #USERSMESSAGESWHATSAPPDELIVERYSHARED" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`from_phone_number` | `null,`&nbsp;`string` | Número de teléfono desde el que se envió el mensaje de WhatsApp
`app_group_id` | `null,`&nbsp;`string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`provider_error_code` | `null,`&nbsp;`string` | Código de error de WhatsApp
`provider_error_title` | `null, `&nbsp;`string` | Título del error de WhatsApp
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`message_id` | `null,`&nbsp;`string` | ID único generado por Meta para este mensaje
`template_name` | `null,`&nbsp;`string` | [PII] Nombre de la plantilla en WhatsApp Manager. Presente si se envía un mensaje de plantilla
`flow_id` | `null,`&nbsp;`string` | ID único del Flow en WhatsApp Manager. Presente si el usuario está respondiendo a un WhatsApp Flow.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPFAILURESHARED #USERSMESSAGESWHATSAPPFAILURESHARED" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`user_phone_number` | `string` | [PII] Número de teléfono del usuario desde el que se recibió el mensaje
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`inbound_phone_number` | `string` | Número entrante al que se envió el mensaje
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`app_group_id` | `null,`&nbsp;`string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`message_body` | `string` | Respuesta del usuario
`quick_reply_text` | `string` | Texto del botón presionado por el usuario
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL de medios del usuario
`action` | `string` | Acción tomada en respuesta a este mensaje. Por ejemplo, `Subscribed`, `Unsubscribed` o `None`.
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
`catalog_id` | `null,`&nbsp;`string` | ID de catálogo de un producto si se hace referencia a un producto en el mensaje entrante. De lo contrario, vacío.
`product_id` | `null,`&nbsp;`string` | ID del producto comprado
`flow_id` | `null,`&nbsp;`string` | ID único del Flow en WhatsApp Manager. Presente si el usuario está respondiendo a un WhatsApp Flow.
`flow_response_json` | `null,`&nbsp;`string` | [PII] Valores del formulario con los que respondió el usuario. Presente si el usuario está respondiendo a un WhatsApp Flow.
`message_id` | `null,`&nbsp;`string` | ID único generado por Meta para este mensaje
`in_reply_to` | `null,`&nbsp;`string` | El message_id del mensaje al que este mensaje estaba respondiendo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED #USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del destinatario
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`from_phone_number` | `null,`&nbsp;`string` | Número de teléfono desde el que se envió el mensaje de WhatsApp
`app_group_id` | `null,`&nbsp;`string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`template_name` | `null,`&nbsp;`string` | [PII] Nombre de la plantilla en WhatsApp Manager. Presente si se envía un mensaje de plantilla
`message_id` | `null,`&nbsp;`string` | ID único generado por Meta para este mensaje
`flow_id` | `null,`&nbsp;`string` | ID único del Flow en WhatsApp Manager. Presente si el usuario está respondiendo a un WhatsApp Flow.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPREADSHARED #USERSMESSAGESWHATSAPPREADSHARED" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo Unix en la que ocurrió el evento
`to_phone_number` | `null,`&nbsp;`string`	| [PII] Número de teléfono del destinatario
`user_id` | `string` | ID de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuario si el usuario es anónimo
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`from_phone_number` | `null,`&nbsp;`string` | Número de teléfono desde el que se envió el mensaje de WhatsApp
`app_group_id` | `null,`&nbsp;`string` | ID del espacio de trabajo al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del espacio de trabajo al que pertenece este usuario
`subscription_group_api_id` | `string` | ID de API del grupo de suscripción
`campaign_id` | `null,`&nbsp;`string` | ID de Braze de uso interno de la campaña a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la campaña a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID de Braze de uso interno del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso de Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje del paso de Canvas que recibió este usuario
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`message_extras` | `null,`&nbsp;`string` | [PII] Cadena JSON de los pares clave-valor etiquetados durante el renderizado con Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que Snowpipe recogió este evento
`send_id` | `null,`&nbsp;`string` | ID de envío del mensaje al que pertenece este mensaje
`flow_id` | `null,`&nbsp;`string` | ID único del Flow en WhatsApp Manager. Presente si el usuario está respondiendo a un WhatsApp Flow.
`template_name` | `null,`&nbsp;`string` | [PII] Nombre de la plantilla en WhatsApp Manager. Presente si se envía un mensaje de plantilla
`message_id` | `null,`&nbsp;`string` | ID único generado por Meta para este mensaje
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPSENDSHARED #USERSMESSAGESWHATSAPPSENDSHARED" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Este evento ocurre cuando un mensaje es despriorizado o tiene un límite de frecuencia y se reintenta más tarde dentro de la ventana de reintento configurada.

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`user_id` | `string` | [PII] ID de usuario de Braze del usuario que realizó este evento
`external_user_id` | `null,`&nbsp;`string` | [PII] ID externo del usuario
`app_group_id` | `null,`&nbsp;`string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`app_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de aplicaciones al que pertenece este usuario
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`to_phone_number` | `null,`&nbsp;`string` | [PII] Número de teléfono del usuario que recibe el mensaje en formato e.164
`device_id` | `null,`&nbsp;`string` | ID del dispositivo en el que ocurrió el evento
`timezone` | `null,`&nbsp;`string` | Zona horaria del usuario
`subscription_group_api_id` | `null,`&nbsp;`string` | ID de API del grupo de suscripción
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la Campaign a la que pertenece este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID de API de la Campaign a la que pertenece este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variante de mensaje que recibió este usuario
`canvas_id` | `null,`&nbsp;`string` | ID BSON del Canvas al que pertenece este evento
`canvas_api_id` | `null,`&nbsp;`string` | ID de API del Canvas al que pertenece este evento
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación del Canvas a la que pertenece este evento
`canvas_step_api_id` | `null,`&nbsp;`string` | ID de API del paso en Canvas al que pertenece este evento
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
`dispatch_id` | `null,`&nbsp;`string` | ID del envío al que pertenece este mensaje
`retry_type` | `null,`&nbsp;`string` | Tipo de reintento
`retry_log` | `null,`&nbsp;`string` | Mensaje de registro que describe los detalles del reintento
`sf_created_at` | `timestamp`,&nbsp;`null` | Momento en que este evento fue recogido por Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPRETRYSHARED #USERSMESSAGESWHATSAPPRETRYSHARED" }

## Usuarios {#users}

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Campo                       | Tipo                     | Descripción                                                              |
| --------------------------- | ------------------------ | ------------------------------------------------------------------------ |
| `id`                        | `string`,&nbsp;`null`    | ID único global de este evento                                           |
| `app_group_id`              | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario         |
| `app_group_api_id`          | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario           |
| `user_id`                   | `string`,&nbsp;`null`    | ID de Braze del usuario que realizó este evento                          |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                             |
| `time`                      | `int`,&nbsp;`null`       | Marca de tiempo en formato Unix en la que se produjo el evento           |
| `random_bucket_number`      | `int`,&nbsp;`null`       | Número de contenedor aleatorio actual asignado al usuario                |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | Número de contenedor aleatorio anterior asignado al usuario              |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Momento en el que Snowpipe recogió este evento                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSRANDOMBUCKETNUMBERUPDATESHARED #USERSRANDOMBUCKETNUMBERUPDATESHARED" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Campo              | Tipo                     | Descripción                                                                        |
| ------------------ | ------------------------ | ---------------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | ID único global de este evento                                                     |
| `user_id`          | `string`,&nbsp;`null`    | ID de Braze del usuario que fue eliminado                                          |
| `app_group_id`     | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario                   |
| `app_group_api_id` | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario                     |
| `time`             | `int`,&nbsp;`null`       | Marca de tiempo en formato Unix en la que se procesó la solicitud de eliminación   |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Momento en el que Snowpipe recogió este evento                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERDELETEREQUESTSHARED #USERSUSERDELETEREQUESTSHARED" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Campo              | Tipo                     | Descripción                                                                                          |
| ------------------ | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | ID único global de este evento                                                                       |
| `user_id`          | `string`,&nbsp;`null`    | ID de Braze del usuario que quedó huérfano                                                           |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] ID externo del usuario                                                                         |
| `device_id`        | `string`,&nbsp;`null`    | ID del dispositivo vinculado a este usuario, si el usuario es anónimo                                |
| `app_group_id`     | `string`,&nbsp;`null`    | ID de Braze del espacio de trabajo al que pertenece este usuario                                     |
| `app_group_api_id` | `string`,&nbsp;`null`    | ID de API del espacio de trabajo al que pertenece este usuario                                       |
| `app_api_id`       | `string`,&nbsp;`null`    | ID de API de la aplicación a la que pertenecía el usuario huérfano                                   |
| `time`             | `int`,&nbsp;`null`       | Marca de tiempo en formato Unix en la que el usuario quedó huérfano                                  |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | ID de Braze del usuario cuyo perfil se fusionó con el perfil del usuario huérfano                    |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Momento en el que Snowpipe recogió este evento                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERORPHANSHARED #USERSUSERORPHANSHARED" }

## Instantáneas {#snapshots}

{% alert note %}
Las tablas de instantáneas solo están disponibles en Snowflake Data Sharing.
{% endalert %}

### SNAPSHOTS_APP_SHARED {#SNAPSHOTS_APP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`api_id` | `string` | ID de API de la aplicación
`name` | `null,`&nbsp;`string` | Nombre de la aplicación
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSAPPSHARED #SNAPSHOTSAPPSHARED" }

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`api_id` | `string` | ID de API de la variación de mensaje de Campaign
`name` | `null,`&nbsp;`string` | Nombre de la variación de mensaje de Campaign
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCAMPAIGNMESSAGEVARIATIONSHARED #SNAPSHOTSCAMPAIGNMESSAGEVARIATIONSHARED" }

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`type` | `null,`&nbsp;`string` | Tipo del paso de Canvas Flow
`api_step_id` | `string` | ID de API del paso en Canvas
`experiment_splits` | `null,`&nbsp;`string` | Divisiones de experimento para el paso
`conversion_behaviors` | `null,`&nbsp;`string` | Comportamientos de conversión para el paso
`name` | `null,`&nbsp;`string` | Nombre del paso de Canvas Flow
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASFLOWSTEPSHARED #SNAPSHOTSCANVASFLOWSTEPSHARED" }

### SNAPSHOTS_CANVAS_STEP_SHARED {#SNAPSHOTS_CANVAS_STEP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`api_id` | `string` | ID de API del paso en Canvas
`name` | `null,`&nbsp;`string` | Nombre del paso en Canvas
`actions` | `null,`&nbsp;`string` | Acciones para el paso en Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASSTEPSHARED #SNAPSHOTSCANVASSTEPSHARED" }

### SNAPSHOTS_CANVAS_VARIATION_SHARED {#SNAPSHOTS_CANVAS_VARIATION_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`api_id` | `string` | ID de API de la variación de Canvas
`name` | `null,`&nbsp;`string` | Nombre de la variación de Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASVARIATIONSHARED #SNAPSHOTSCANVASVARIATIONSHARED" }

### SNAPSHOTS_EXPERIMENT_STEP_SHARED {#SNAPSHOTS_EXPERIMENT_STEP_SHARED}

Campo | Tipo | Descripción
------|------|------------
`id` | `string` | ID único global para este evento
`time` | `int` | Marca de tiempo UNIX en la que ocurrió el evento
`app_group_id` | `string` | ID BSON del grupo de aplicaciones al que pertenece este usuario
`type` | `null,`&nbsp;`string` | Tipo del paso de experimento
`api_step_id` | `string` | ID de API del paso de experimento
`experiment_splits` | `null,`&nbsp;`string` | Divisiones de experimento para el paso
`conversion_behaviors` | `null,`&nbsp;`string` | Comportamientos de conversión para el paso
`name` | `null,`&nbsp;`string` | Nombre del paso de experimento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSEXPERIMENTSTEPSHARED #SNAPSHOTSEXPERIMENTSTEPSHARED" }

## Tipos de cancelación {#abort-types}

{% include currents/abort_types_reference.md combined_content_rendering=true %}