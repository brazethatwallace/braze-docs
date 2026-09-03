---
nav_title: Registro de cambios de eventos de Currents
page_order: 6
description: "Esta página incluye los cambios en los eventos para cada versión de Currents."
tool: Currents
---

# Registro de cambios de Currents {#currents-changelog}

## Cambios en la versión 12 (fecha de lanzamiento: 02-09-2026) {#changes-in-version-12-release-date-2026-09-02}

### Cambios para Storage: {#changes-for-storage}

* Cambios de campo en el tipo de evento `users.messages.email.Abort`:
    * Se añadió un nuevo campo `string` `message_extras`: [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid

* Cambios de campo en el tipo de evento `users.messages.email.Bounce`:
    * Se añadió un nuevo campo `int` `send_time`: Hora del evento de envío correspondiente

* Cambios de campo en el tipo de evento `users.messages.email.Click`:
    * Se añadió un nuevo campo `int` `send_time`: Hora en segundos del evento de envío correspondiente
    * Se añadió un nuevo campo `boolean` `has_url_parameters`: Si la URL en la que se hizo clic contenía parámetros de consulta
    * Se añadió un nuevo campo `boolean` `link_aliasing_enabled`: Si el aliasing de enlaces estaba habilitado para el espacio de trabajo cuando se procesó este clic

* Cambios de campo en el tipo de evento `users.messages.email.Deferral`:
    * Se añadió un nuevo campo `int` `send_time`: Hora del evento de envío correspondiente

* Cambios de campo en el tipo de evento `users.messages.email.Delivery`:
    * Se añadió un nuevo campo `int` `send_time`: Hora del evento de envío correspondiente

* Cambios de campo en el tipo de evento `users.messages.email.MarkAsSpam`:
    * Se añadió un nuevo campo `int` `send_time`: Hora del evento de envío correspondiente

* Cambios de campo en el tipo de evento `users.messages.email.Open`:
    * Se añadió un nuevo campo `int` `send_time`: Hora del evento de envío correspondiente

* Cambios de campo en el tipo de evento `users.messages.email.SoftBounce`:
    * Se añadió un nuevo campo `int` `send_time`: Hora del evento de envío correspondiente

* Cambios de campo en el tipo de evento `users.messages.line.Abort`:
    * Se añadió un nuevo campo `string` `message_extras`: [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid

* Cambios de campo en el tipo de evento `users.messages.pushnotification.Abort`:
    * Se añadió un nuevo campo `string` `message_extras`: [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid

* Cambios de campo en el tipo de evento `users.messages.rcs.Abort`:
    * Se añadió un nuevo campo `string` `message_extras`: [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid

* Cambios de campo en el tipo de evento `users.messages.sms.Abort`:
    * Se añadió un nuevo campo `string` `message_extras`: [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid

* Cambios de campo en el tipo de evento `users.messages.webhook.Abort`:
    * Se añadió un nuevo campo `string` `message_extras`: [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Abort`:
    * Se añadió un nuevo campo `string` `message_extras`: [PII] Una cadena JSON de los pares clave-valor etiquetados durante el renderizado de Liquid

## Cambios en la versión 11 (fecha de lanzamiento: 2026-08-05) {#changes-in-version-11-release-date-2026-08-05}

### Cambios en Storage:

* Se agregó el nuevo tipo de evento `contentoptimizer.ComponentStore`.

* Se agregó el nuevo tipo de evento `users.canvas.costep.Conversion`.

* Se agregó el nuevo tipo de evento `users.messages.landingpage.Click`.

* Se agregó el nuevo tipo de evento `users.messages.landingpage.FormSubmission`.

* Se agregó el nuevo tipo de evento `users.messages.landingpage.Impression`.

* Se agregó el nuevo tipo de evento `users.messages.survey.Response`.

* Cambios de campo en el tipo de evento `agentconsole.AgentExecuted`:
    * Se agregó el nuevo campo `string` `thinking_level`: el nivel de pensamiento/razonamiento utilizado para la solicitud

* Cambios de campo en el tipo de evento `users.messages.banner.Click`:
    * Se agregó el nuevo campo `boolean` `is_unique`: indica si este fue el primer clic del usuario en la variación del mensaje, contabilizado en las estadísticas de clics únicos

* Cambios de campo en el tipo de evento `users.messages.banner.Dismiss`:
    * Se agregó el nuevo campo `boolean` `is_unique`: indica si este fue el primer descarte del usuario de la variación del mensaje, contabilizado en las estadísticas de descartes únicos

* Cambios de campo en el tipo de evento `users.messages.banner.Impression`:
    * Se agregó el nuevo campo `boolean` `is_unique`: indica si esta fue la primera impresión del usuario de la variación del mensaje, contabilizada en las estadísticas de impresiones únicas

* Cambios de campo en el tipo de evento `users.messages.contentcard.Click`:
    * Se agregó el nuevo campo `boolean` `is_unique`: indica si este fue el primer clic del usuario en la variación del mensaje, contabilizado en las estadísticas de clics únicos

* Cambios de campo en el tipo de evento `users.messages.contentcard.Dismiss`:
    * Se agregó el nuevo campo `boolean` `is_unique`: indica si este fue el primer descarte del usuario de la variación del mensaje, contabilizado en las estadísticas de descartes únicos

* Cambios de campo en el tipo de evento `users.messages.contentcard.Impression`:
    * Se agregó el nuevo campo `boolean` `is_unique`: indica si esta fue la primera impresión del usuario de la variación del mensaje, contabilizada en las estadísticas de impresiones únicas

* Cambios de campo en el tipo de evento `users.messages.featureflag.Impression`:
    * Se agregó el nuevo campo `boolean` `is_unique`: indica si esta fue la primera impresión del usuario para este conmutador de características, contabilizada en las estadísticas de impresiones únicas

## Cambios en la versión 10 (fecha de lanzamiento: 01-07-2026) {#changes-in-version-10-release-date-2026-07-01}

### Cambios para Storage:

* Se añadió el nuevo tipo de evento `users.canvas.costep.Send`.

* Se añadió el nuevo tipo de evento `users.UserDeleteRequest`.

* Se añadió el nuevo tipo de evento `users.UserOrphan`.

* Cambios de campo en el tipo de evento `users.messages.rcs.Abort`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Click`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Delivery`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.InboundReceive`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Read`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Rejection`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Send`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

## Cambios en la versión 9 (fecha de lanzamiento 2026-06-03) {#changes-in-version-9-release-date-2026-06-03}

### Cambios para Storage:

* Cambios de campo en el tipo de evento `users.messages.email.Send`:
    * Se agregó un nuevo campo `string` `from_domain`: Dominio de envío del correo electrónico

## Cambios en la versión 8 (fecha de lanzamiento: 2026-05-06) {#changes-in-version-8-release-date-2026-05-06}

### Cambios para Storage:

* Se agregó el nuevo tipo de evento `users.messages.banner.Dismiss`.

* Cambios en los campos del tipo de evento `users.messages.whatsapp.Abort`:
    * Se agregó el nuevo campo `string` `bsuid`: El ID de usuario con ámbito empresarial de WhatsApp (WhatsApp Business-Scoped User ID) del destinatario asociado a este evento.

* Cambios en los campos del tipo de evento `users.messages.whatsapp.Delivery`:
    * Se agregó el nuevo campo `string` `bsuid`: El ID de usuario con ámbito empresarial de WhatsApp (WhatsApp Business-Scoped User ID) del destinatario asociado a este evento.

* Cambios en los campos del tipo de evento `users.messages.whatsapp.Failure`:
    * Se agregó el nuevo campo `string` `bsuid`: El ID de usuario con ámbito empresarial de WhatsApp (WhatsApp Business-Scoped User ID) del destinatario asociado a este evento.

* Cambios en los campos del tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Se agregó el nuevo campo `string` `bsuid`: El ID de usuario con ámbito empresarial de WhatsApp (WhatsApp Business-Scoped User ID) del usuario del que se recibió el mensaje.
    * El campo `user_phone_number` ahora es *opcional*.

* Cambios en los campos del tipo de evento `users.messages.whatsapp.Read`:
    * Se agregó el nuevo campo `string` `bsuid`: El ID de usuario con ámbito empresarial de WhatsApp (WhatsApp Business-Scoped User ID) del destinatario asociado a este evento.

* Cambios en los campos del tipo de evento `users.messages.whatsapp.Retry`:
    * Se agregó el nuevo campo `string` `bsuid`: El ID de usuario con ámbito empresarial de WhatsApp (WhatsApp Business-Scoped User ID) del destinatario asociado a este evento.

* Cambios en los campos del tipo de evento `users.messages.whatsapp.Send`:
    * Se agregó el nuevo campo `string` `bsuid`: El ID de usuario con ámbito empresarial de WhatsApp (WhatsApp Business-Scoped User ID) del destinatario asociado a este evento.

## Cambios en la versión 7 (fecha de lanzamiento: 01-04-2026) {#changes-in-version-7-release-date-2026-04-01}

### Cambios para Storage:

* Se añadió el nuevo tipo de evento `users.profile.Update`.

* Cambios de campo en el tipo de evento `users.messages.banner.Abort`:
    * Se añadió el nuevo campo `string` `canvas_name`: nombre del Canvas
    * Se añadió el nuevo campo `string` `canvas_step_name`: nombre del paso en Canvas
    * Se añadió el nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento
    * Se añadió el nuevo campo `string` `canvas_step_id`: ID de API del paso en Canvas al que pertenece este evento
    * Se añadió el nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
    * Se añadió el nuevo campo `string` `canvas_variation_id`: ID de API de la variación de Canvas a la que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.banner.Click`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento
    * Se añadió el nuevo campo `string` `canvas_step_id`: ID de API del paso en Canvas al que pertenece este evento
    * Se añadió el nuevo campo `string` `canvas_name`: nombre del Canvas
    * Se añadió el nuevo campo `string` `canvas_step_name`: nombre del paso en Canvas
    * Se añadió el nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
    * Se añadió el nuevo campo `string` `canvas_variation_id`: ID de API de la variación de Canvas a la que pertenece este evento
    * Se añadió el nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario

* Cambios de campo en el tipo de evento `users.messages.banner.Impression`:
    * Se añadió el nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento
    * Se añadió el nuevo campo `string` `canvas_step_id`: ID de API del paso en Canvas al que pertenece este evento
    * Se añadió el nuevo campo `string` `canvas_name`: nombre del Canvas
    * Se añadió el nuevo campo `string` `canvas_step_name`: nombre del paso en Canvas
    * Se añadió el nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación de mensaje del paso en Canvas que recibió este usuario
    * Se añadió el nuevo campo `string` `canvas_variation_id`: ID de API de la variación de Canvas a la que pertenece este evento
    * Se añadió el nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario

## Cambios en la versión 6 (fecha de lanzamiento: 04-03-2026) {#changes-in-version-6-release-date-2026-03-04}

### Cambios para Storage:

* Cambios de campo en el tipo de evento `agentconsole.AgentExecuted`:
    * Se añadió un nuevo campo `string` `error`: Descripción del error

* Cambios de campo en el tipo de evento `agentconsole.ToolInvocation`:
    * Se añadió un nuevo campo `string` `request_id`: ID único para esta solicitud LLM general y ejecución completa

* Cambios de campo en el tipo de evento `users.messages.rcs.InboundReceive`:
    * Se añadió un nuevo campo `string` `canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario

## Cambios en la versión 5 (fecha de lanzamiento 2026-02-04) {#changes-in-version-5-release-date-2026-02-04}

### Cambios para Storage:

* Se agregó el nuevo tipo de evento `agentconsole.AgentExecuted`.

* Se agregó el nuevo tipo de evento `agentconsole.ToolInvocation`.

* Se agregó el nuevo tipo de evento `users.messages.email.Retry`.

* Se agregó el nuevo tipo de evento `users.messages.line.Retry`.

* Se agregó el nuevo tipo de evento `users.messages.pushnotification.Retry`.

* Se agregó el nuevo tipo de evento `users.messages.sms.Retry`.

* Se agregó el nuevo tipo de evento `users.messages.webhook.Retry`.

* Se agregó el nuevo tipo de evento `users.messages.whatsapp.Retry`.

* Cambios de campo en el tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Se agregó el nuevo campo `long` `time_ms`: Tiempo en milisegundos en que ocurrió el evento

## Cambios en la versión 4 (fecha de lanzamiento 2026-01-07) {#changes-in-version-4-release-date-2026-01-07}

### Cambios para Storage:

* Cambios de campo en el tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Se ha añadido un nuevo campo `string` `push_token`: token de notificaciones push del evento

* Cambios de campo en el tipo de evento `users.messages.pushnotification.Bounce`:
    * Se ha añadido un nuevo campo `string` `push_token`: token de notificaciones push del evento

* Cambios de campo en el tipo de evento `users.messages.pushnotification.Send`:
    * Se ha añadido un nuevo campo `string` `push_token`: token de notificaciones push del evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Click`:
    * Se ha añadido un nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario
    * El campo `user_phone_number` ahora es *opcional*.

* Cambios de campo en el tipo de evento `users.messages.rcs.InboundReceive`:
    * El campo `user_id` ahora es *opcional*.

* Cambios de campo en el tipo de evento `users.messages.rcs.Rejection`:
    * Se ha añadido un nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación de mensaje del paso en Canvas que recibió este usuario

## Cambios en la versión 3 (fecha de lanzamiento 2025-10-08) {#changes-in-version-3-release-date-2025-10-08}

### Cambios para Storage:

* Se añadió un nuevo tipo de evento `users.messages.line.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.line.Click`.

* Se añadió un nuevo tipo de evento `users.messages.line.InboundReceive`.

* Se añadió un nuevo tipo de evento `users.messages.line.Send`.

* Se añadió un nuevo tipo de evento `users.messages.rcs.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.rcs.Click`.

* Se añadió un nuevo tipo de evento `users.messages.rcs.Delivery`.

* Se añadió un nuevo tipo de evento `users.messages.rcs.InboundReceive`.

* Se añadió un nuevo tipo de evento `users.messages.rcs.Read`.

* Se añadió un nuevo tipo de evento `users.messages.rcs.Rejection`.

* Se añadió un nuevo tipo de evento `users.messages.rcs.Send`.

* Cambios de campo en el tipo de evento `users.messages.sms.Delivery`:
    * Se añadió un nuevo campo `boolean` `is_sms_fallback`: Indica que se envió un mensaje SMS alternativo debido a un mensaje RCS rechazado. El mensaje puede resultar en entrega, fallo de entrega o rechazo. Se puede vincular al evento de rechazo de RCS mediante un ID de envío y un ID de despacho

* Cambios de campo en el tipo de evento `users.messages.sms.DeliveryFailure`:
    * Se añadió un nuevo campo `boolean` `is_sms_fallback`: Indica que se envió un mensaje SMS alternativo debido a un mensaje RCS rechazado. El mensaje puede resultar en entrega, fallo de entrega o rechazo. Se puede vincular al evento de rechazo de RCS mediante un ID de envío y un ID de despacho

* Cambios de campo en el tipo de evento `users.messages.sms.Rejection`:
    * Se añadió un nuevo campo `boolean` `is_sms_fallback`: Indica que se envió un mensaje SMS alternativo debido a un mensaje RCS rechazado. El mensaje puede resultar en entrega, fallo de entrega o rechazo. Se puede vincular al evento de rechazo de RCS mediante un ID de envío y un ID de despacho

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Delivery`:
    * Se añadió un nuevo campo `string` `flow_id`: El ID único del flujo en WhatsApp Administrador. Presente si el mensaje incluye un CTA para responder a un flujo de WhatsApp
    * Se añadió un nuevo campo `string` `template_name`: [PII] Nombre de la plantilla en WhatsApp Administrador. Presente si se envía un mensaje de plantilla
    * Se añadió un nuevo campo `string` `message_id`: El ID único generado por Meta para este mensaje

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Failure`:
    * Se añadió un nuevo campo `string` `message_id`: El ID único generado por Meta para este mensaje
    * Se añadió un nuevo campo `string` `template_name`: [PII] Nombre de la plantilla en WhatsApp Administrador. Presente si se envía un mensaje de plantilla
    * Se añadió un nuevo campo `string` `flow_id`: El ID único del flujo en WhatsApp Administrador. Presente si el mensaje incluye un CTA para responder a un flujo de WhatsApp

* Cambios de campo en el tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Se añadió un nuevo campo `string` `catalog_id`: ID del catálogo de un producto si se hace referencia a un producto en el mensaje entrante. De lo contrario, vacío.
    * Se añadió un nuevo campo `string` `product_id`: SKU del producto si se hace referencia a un producto en el mensaje entrante. De lo contrario, vacío.
    * Se añadió un nuevo campo `string` `flow_id`: El ID único del flujo en WhatsApp Administrador. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se añadió un nuevo campo `string` `flow_response_json`: [PII] Los valores del formulario con los que respondió el usuario. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se añadió un nuevo campo `string` `message_id`: El ID único generado por Meta para este mensaje
    * Se añadió un nuevo campo `string` `in_reply_to`: El message_id del mensaje al que este mensaje estaba respondiendo

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Read`:
    * Se añadió un nuevo campo `string` `template_name`: [PII] Nombre de la plantilla en WhatsApp Administrador. Presente si se envía un mensaje de plantilla
    * Se añadió un nuevo campo `string` `message_id`: El ID único generado por Meta para este mensaje
    * Se añadió un nuevo campo `string` `flow_id`: El ID único del flujo en WhatsApp Administrador. Presente si el mensaje incluye un CTA para responder a un flujo de WhatsApp

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Send`:
    * Se añadió un nuevo campo `string` `flow_id`: El ID único del flujo en WhatsApp Administrador. Presente si el mensaje incluye un CTA para responder a un flujo de WhatsApp
    * Se añadió un nuevo campo `string` `template_name`: [PII] Nombre de la plantilla en WhatsApp Administrador. Presente si se envía un mensaje de plantilla
    * Se añadió un nuevo campo `string` `message_id`: El ID único generado por Meta para este mensaje

## Cambios en la versión 2 (fecha de lanzamiento nula) {#changes-in-version-2-release-date-null}

### Cambios para Storage:

* Se añadió el nuevo tipo de evento `users.behaviors.app.FirstSession`.

* Se añadió el nuevo tipo de evento `users.behaviors.app.SessionEnd`.

* Se añadió el nuevo tipo de evento `users.behaviors.app.SessionStart`.

* Se añadió el nuevo tipo de evento `users.behaviors.CustomEvent`.

* Se añadió el nuevo tipo de evento `users.behaviors.InstallAttribution`.

* Se añadió el nuevo tipo de evento `users.behaviors.liveactivity.PushToStartTokenChange`.

* Se añadió el nuevo tipo de evento `users.behaviors.liveactivity.UpdateTokenChange`.

* Se añadió el nuevo tipo de evento `users.behaviors.Location`.

* Se añadió el nuevo tipo de evento `users.behaviors.Purchase`.

* Se añadió el nuevo tipo de evento `users.behaviors.pushnotification.TokenStateChange`.

* Se añadió el nuevo tipo de evento `users.behaviors.subscription.GlobalStateChange`.

* Se añadió el nuevo tipo de evento `users.behaviors.subscriptiongroup.StateChange`.

* Se añadió el nuevo tipo de evento `users.behaviors.Uninstall`.

* Se añadió el nuevo tipo de evento `users.campaigns.Conversion`.

* Se añadió el nuevo tipo de evento `users.campaigns.EnrollInControl`.

* Se añadió el nuevo tipo de evento `users.canvas.Conversion`.

* Se añadió el nuevo tipo de evento `users.canvas.Entry`.

* Se añadió el nuevo tipo de evento `users.canvas.exit.MatchedAudience`.

* Se añadió el nuevo tipo de evento `users.canvas.exit.PerformedEvent`.

* Se añadió el nuevo tipo de evento `users.canvas.experimentstep.Conversion`.

* Se añadió el nuevo tipo de evento `users.canvas.experimentstep.SplitEntry`.

* Se añadió el nuevo tipo de evento `users.canvasstep.Progression`.

* Se añadió el nuevo tipo de evento `users.messages.banner.Abort`.

* Se añadió el nuevo tipo de evento `users.messages.banner.Click`.

* Se añadió el nuevo tipo de evento `users.messages.banner.Impression`.

* Se añadió el nuevo tipo de evento `users.messages.contentcard.Abort`.

* Se añadió el nuevo tipo de evento `users.messages.contentcard.Click`.

* Se añadió el nuevo tipo de evento `users.messages.contentcard.Dismiss`.

* Se añadió el nuevo tipo de evento `users.messages.contentcard.Impression`.

* Se añadió el nuevo tipo de evento `users.messages.contentcard.Send`.

* Se añadió el nuevo tipo de evento `users.messages.email.Abort`.

* Se añadió el nuevo tipo de evento `users.messages.email.Bounce`.

* Se añadió el nuevo tipo de evento `users.messages.email.Click`.

* Se añadió el nuevo tipo de evento `users.messages.email.Deferral`.

* Se añadió el nuevo tipo de evento `users.messages.email.Delivery`.

* Se añadió el nuevo tipo de evento `users.messages.email.MarkAsSpam`.

* Se añadió el nuevo tipo de evento `users.messages.email.Open`.

* Se añadió el nuevo tipo de evento `users.messages.email.Send`.

* Se añadió el nuevo tipo de evento `users.messages.email.SoftBounce`.

* Se añadió el nuevo tipo de evento `users.messages.email.Unsubscribe`.

* Se añadió el nuevo tipo de evento `users.messages.featureflag.Impression`.

* Se añadió el nuevo tipo de evento `users.messages.inappmessage.Abort`.

* Se añadió el nuevo tipo de evento `users.messages.inappmessage.Click`.

* Se añadió el nuevo tipo de evento `users.messages.inappmessage.Impression`.

* Se añadió el nuevo tipo de evento `users.messages.liveactivity.Outcome`.

* Se añadió el nuevo tipo de evento `users.messages.liveactivity.Send`.

* Se añadió el nuevo tipo de evento `users.messages.pushnotification.Abort`.

* Se añadió el nuevo tipo de evento `users.messages.pushnotification.Bounce`.

* Se añadió el nuevo tipo de evento `users.messages.pushnotification.IosForeground`.

* Se añadió el nuevo tipo de evento `users.messages.pushnotification.Open`.

* Se añadió el nuevo tipo de evento `users.messages.pushnotification.Send`.

* Se añadió el nuevo tipo de evento `users.messages.sms.Abort`.

* Se añadió el nuevo tipo de evento `users.messages.sms.CarrierSend`.

* Se añadió el nuevo tipo de evento `users.messages.sms.Delivery`.

* Se añadió el nuevo tipo de evento `users.messages.sms.DeliveryFailure`.

* Se añadió el nuevo tipo de evento `users.messages.sms.InboundReceive`.

* Se añadió el nuevo tipo de evento `users.messages.sms.Rejection`.

* Se añadió el nuevo tipo de evento `users.messages.sms.Send`.

* Se añadió el nuevo tipo de evento `users.messages.sms.ShortLinkClick`.

* Se añadió el nuevo tipo de evento `users.messages.webhook.Abort`.

* Se añadió el nuevo tipo de evento `users.messages.webhook.Failure`.

* Se añadió el nuevo tipo de evento `users.messages.webhook.Send`.

* Se añadió el nuevo tipo de evento `users.messages.whatsapp.Abort`.

* Se añadió el nuevo tipo de evento `users.messages.whatsapp.Click`.

* Se añadió el nuevo tipo de evento `users.messages.whatsapp.Delivery`.

* Se añadió el nuevo tipo de evento `users.messages.whatsapp.Failure`.

* Se añadió el nuevo tipo de evento `users.messages.whatsapp.InboundReceive`.

* Se añadió el nuevo tipo de evento `users.messages.whatsapp.Read`.

* Se añadió el nuevo tipo de evento `users.messages.whatsapp.Send`.

* Se añadió el nuevo tipo de evento `users.RandomBucketNumberUpdate`.