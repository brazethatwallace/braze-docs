---
nav_title: Registro de cambios de eventos de Currents
page_order: 6
description: "Esta página incluye los cambios en los eventos para cada versión de Currents."
tool: Currents
---

# Registro de cambios de Currents {#currents-changelog}

## Cambios en la versión 10 (fecha de lanzamiento: 01-07-2026) {#changes-in-version-10-release-date-2026-07-01}

### Cambios en el almacenamiento: {#changes-for-storage}

* Se añadió un nuevo tipo de evento `users.canvas.costep.Send`.

* Se añadió un nuevo tipo de evento `users.UserDeleteRequest`.

* Se añadió un nuevo tipo de evento `users.UserOrphan`.

* Cambios de campo en el tipo de evento `users.messages.rcs.Abort`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Click`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Delivery`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.InboundReceive`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Read`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Rejection`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Send`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento

## Cambios en la versión 9 (fecha de lanzamiento: 03-06-2026) {#changes-in-version-9-release-date-2026-06-03}

### Cambios en el almacenamiento:

* Cambios de campo en el tipo de evento `users.messages.email.Send`:
    * Se añadió un nuevo campo `string` `from_domain`: dominio de envío del correo electrónico

## Cambios en la versión 8 (fecha de lanzamiento: 06-05-2026) {#changes-in-version-8-release-date-2026-05-06}

### Cambios en el almacenamiento:

* Se añadió un nuevo tipo de evento `users.messages.banner.Dismiss`.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Abort`:
    * Se añadió un nuevo campo `string` `bsuid`: el ID de usuario con ámbito de negocio de WhatsApp del destinatario asociado a este evento.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Delivery`:
    * Se añadió un nuevo campo `string` `bsuid`: el ID de usuario con ámbito de negocio de WhatsApp del destinatario asociado a este evento.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Failure`:
    * Se añadió un nuevo campo `string` `bsuid`: el ID de usuario con ámbito de negocio de WhatsApp del destinatario asociado a este evento.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Se añadió un nuevo campo `string` `bsuid`: el ID de usuario con ámbito de negocio de WhatsApp del usuario del que se recibió el mensaje.
    * El campo `user_phone_number` ahora es *opcional*.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Read`:
    * Se añadió un nuevo campo `string` `bsuid`: el ID de usuario con ámbito de negocio de WhatsApp del destinatario asociado a este evento.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Retry`:
    * Se añadió un nuevo campo `string` `bsuid`: el ID de usuario con ámbito de negocio de WhatsApp del destinatario asociado a este evento.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Send`:
    * Se añadió un nuevo campo `string` `bsuid`: el ID de usuario con ámbito de negocio de WhatsApp del destinatario asociado a este evento.

## Cambios en la versión 7 (fecha de lanzamiento: 01-04-2026) {#changes-in-version-7-release-date-2026-04-01}

### Cambios en el almacenamiento:

* Se añadió un nuevo tipo de evento `users.profile.Update`.

* Cambios de campo en el tipo de evento `users.messages.banner.Abort`:
    * Se añadió un nuevo campo `string` `canvas_name`: nombre del Canvas
    * Se añadió un nuevo campo `string` `canvas_step_name`: nombre del paso en Canvas
    * Se añadió un nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento
    * Se añadió un nuevo campo `string` `canvas_step_id`: ID de API del paso en Canvas al que pertenece este evento
    * Se añadió un nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación del mensaje del paso en Canvas que recibió este usuario
    * Se añadió un nuevo campo `string` `canvas_variation_id`: ID de API de la variación de Canvas a la que pertenece este evento

* Cambios de campo en el tipo de evento `users.messages.banner.Click`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento
    * Se añadió un nuevo campo `string` `canvas_step_id`: ID de API del paso en Canvas al que pertenece este evento
    * Se añadió un nuevo campo `string` `canvas_name`: nombre del Canvas
    * Se añadió un nuevo campo `string` `canvas_step_name`: nombre del paso en Canvas
    * Se añadió un nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación del mensaje del paso en Canvas que recibió este usuario
    * Se añadió un nuevo campo `string` `canvas_variation_id`: ID de API de la variación de Canvas a la que pertenece este evento
    * Se añadió un nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario

* Cambios de campo en el tipo de evento `users.messages.banner.Impression`:
    * Se añadió un nuevo campo `string` `canvas_id`: ID de API del Canvas al que pertenece este evento
    * Se añadió un nuevo campo `string` `canvas_step_id`: ID de API del paso en Canvas al que pertenece este evento
    * Se añadió un nuevo campo `string` `canvas_name`: nombre del Canvas
    * Se añadió un nuevo campo `string` `canvas_step_name`: nombre del paso en Canvas
    * Se añadió un nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación del mensaje del paso en Canvas que recibió este usuario
    * Se añadió un nuevo campo `string` `canvas_variation_id`: ID de API de la variación de Canvas a la que pertenece este evento
    * Se añadió un nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario

## Cambios en la versión 6 (fecha de lanzamiento: 04-03-2026) {#changes-in-version-6-release-date-2026-03-04}

### Cambios en el almacenamiento:

* Cambios de campo en el tipo de evento `agentconsole.AgentExecuted`:
    * Se añadió un nuevo campo `string` `error`: descripción del error

* Cambios de campo en el tipo de evento `agentconsole.ToolInvocation`:
    * Se añadió un nuevo campo `string` `request_id`: ID único para esta solicitud LLM general y ejecución completa

* Cambios de campo en el tipo de evento `users.messages.rcs.InboundReceive`:
    * Se añadió un nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario

## Cambios en la versión 5 (fecha de lanzamiento: 04-02-2026) {#changes-in-version-5-release-date-2026-02-04}

### Cambios en el almacenamiento:

* Se añadió un nuevo tipo de evento `agentconsole.AgentExecuted`.

* Se añadió un nuevo tipo de evento `agentconsole.ToolInvocation`.

* Se añadió un nuevo tipo de evento `users.messages.email.Retry`.

* Se añadió un nuevo tipo de evento `users.messages.line.Retry`.

* Se añadió un nuevo tipo de evento `users.messages.pushnotification.Retry`.

* Se añadió un nuevo tipo de evento `users.messages.sms.Retry`.

* Se añadió un nuevo tipo de evento `users.messages.webhook.Retry`.

* Se añadió un nuevo tipo de evento `users.messages.whatsapp.Retry`.

* Cambios de campo en el tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Se añadió un nuevo campo `long` `time_ms`: tiempo en milisegundos en el que ocurrió el evento

## Cambios en la versión 4 (fecha de lanzamiento: 07-01-2026) {#changes-in-version-4-release-date-2026-01-07}

### Cambios en el almacenamiento:

* Cambios de campo en el tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Se añadió un nuevo campo `string` `push_token`: token de notificaciones push del evento

* Cambios de campo en el tipo de evento `users.messages.pushnotification.Bounce`:
    * Se añadió un nuevo campo `string` `push_token`: token de notificaciones push del evento

* Cambios de campo en el tipo de evento `users.messages.pushnotification.Send`:
    * Se añadió un nuevo campo `string` `push_token`: token de notificaciones push del evento

* Cambios de campo en el tipo de evento `users.messages.rcs.Click`:
    * Se añadió un nuevo campo `string` `canvas_variation_name`: nombre de la variación de Canvas que recibió este usuario
    * El campo `user_phone_number` ahora es *opcional*.

* Cambios de campo en el tipo de evento `users.messages.rcs.InboundReceive`:
    * El campo `user_id` ahora es *opcional*.

* Cambios de campo en el tipo de evento `users.messages.rcs.Rejection`:
    * Se añadió un nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación del mensaje del paso en Canvas que recibió este usuario

## Cambios en la versión 3 (fecha de lanzamiento: 08-10-2025) {#changes-in-version-3-release-date-2025-10-08}

### Cambios en el almacenamiento:

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
    * Se añadió un nuevo campo `boolean` `is_sms_fallback`: indica que se envió un mensaje SMS alternativo debido al rechazo de un mensaje RCS. El mensaje puede resultar en entrega, fallo de entrega o rechazo. Se puede vincular al evento de rechazo RCS mediante un ID de envío y un ID de despacho.

* Cambios de campo en el tipo de evento `users.messages.sms.DeliveryFailure`:
    * Se añadió un nuevo campo `boolean` `is_sms_fallback`: indica que se envió un mensaje SMS alternativo debido al rechazo de un mensaje RCS. El mensaje puede resultar en entrega, fallo de entrega o rechazo. Se puede vincular al evento de rechazo RCS mediante un ID de envío y un ID de despacho.

* Cambios de campo en el tipo de evento `users.messages.sms.Rejection`:
    * Se añadió un nuevo campo `boolean` `is_sms_fallback`: indica que se envió un mensaje SMS alternativo debido al rechazo de un mensaje RCS. El mensaje puede resultar en entrega, fallo de entrega o rechazo. Se puede vincular al evento de rechazo RCS mediante un ID de envío y un ID de despacho.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Delivery`:
    * Se añadió un nuevo campo `string` `flow_id`: el ID único del flujo en el administrador de WhatsApp. Presente si el mensaje incluye una llamada a la acción para responder a un flujo de WhatsApp.
    * Se añadió un nuevo campo `string` `template_name`: [PII] nombre de la plantilla en el administrador de WhatsApp. Presente si se envía un mensaje de plantilla.
    * Se añadió un nuevo campo `string` `message_id`: el ID único generado por Meta para este mensaje.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Failure`:
    * Se añadió un nuevo campo `string` `message_id`: el ID único generado por Meta para este mensaje.
    * Se añadió un nuevo campo `string` `template_name`: [PII] nombre de la plantilla en el administrador de WhatsApp. Presente si se envía un mensaje de plantilla.
    * Se añadió un nuevo campo `string` `flow_id`: el ID único del flujo en el administrador de WhatsApp. Presente si el mensaje incluye una llamada a la acción para responder a un flujo de WhatsApp.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Se añadió un nuevo campo `string` `catalog_id`: ID de catálogo de un producto si se hace referencia a un producto en el mensaje de entrada. De lo contrario, vacío.
    * Se añadió un nuevo campo `string` `product_id`: SKU del producto si se hace referencia a un producto en el mensaje de entrada. De lo contrario, vacío.
    * Se añadió un nuevo campo `string` `flow_id`: el ID único del flujo en el administrador de WhatsApp. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se añadió un nuevo campo `string` `flow_response_json`: [PII] los valores del formulario con los que respondió el usuario. Presente si el usuario está respondiendo a un flujo de WhatsApp.
    * Se añadió un nuevo campo `string` `message_id`: el ID único generado por Meta para este mensaje.
    * Se añadió un nuevo campo `string` `in_reply_to`: el `message_id` del mensaje al que respondía este mensaje.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Read`:
    * Se añadió un nuevo campo `string` `template_name`: [PII] nombre de la plantilla en el administrador de WhatsApp. Presente si se envía un mensaje de plantilla.
    * Se añadió un nuevo campo `string` `message_id`: el ID único generado por Meta para este mensaje.
    * Se añadió un nuevo campo `string` `flow_id`: el ID único del flujo en el administrador de WhatsApp. Presente si el mensaje incluye una llamada a la acción para responder a un flujo de WhatsApp.

* Cambios de campo en el tipo de evento `users.messages.whatsapp.Send`:
    * Se añadió un nuevo campo `string` `flow_id`: el ID único del flujo en el administrador de WhatsApp. Presente si el mensaje incluye una llamada a la acción para responder a un flujo de WhatsApp.
    * Se añadió un nuevo campo `string` `template_name`: [PII] nombre de la plantilla en el administrador de WhatsApp. Presente si se envía un mensaje de plantilla.
    * Se añadió un nuevo campo `string` `message_id`: el ID único generado por Meta para este mensaje.

## Cambios en la versión 2 (fecha de lanzamiento: nula) {#changes-in-version-2-release-date-null}

### Cambios en el almacenamiento:

* Se añadió un nuevo tipo de evento `users.behaviors.app.FirstSession`.

* Se añadió un nuevo tipo de evento `users.behaviors.app.SessionEnd`.

* Se añadió un nuevo tipo de evento `users.behaviors.app.SessionStart`.

* Se añadió un nuevo tipo de evento `users.behaviors.CustomEvent`.

* Se añadió un nuevo tipo de evento `users.behaviors.InstallAttribution`.

* Se añadió un nuevo tipo de evento `users.behaviors.liveactivity.PushToStartTokenChange`.

* Se añadió un nuevo tipo de evento `users.behaviors.liveactivity.UpdateTokenChange`.

* Se añadió un nuevo tipo de evento `users.behaviors.Location`.

* Se añadió un nuevo tipo de evento `users.behaviors.Purchase`.

* Se añadió un nuevo tipo de evento `users.behaviors.pushnotification.TokenStateChange`.

* Se añadió un nuevo tipo de evento `users.behaviors.subscription.GlobalStateChange`.

* Se añadió un nuevo tipo de evento `users.behaviors.subscriptiongroup.StateChange`.

* Se añadió un nuevo tipo de evento `users.behaviors.Uninstall`.

* Se añadió un nuevo tipo de evento `users.campaigns.Conversion`.

* Se añadió un nuevo tipo de evento `users.campaigns.EnrollInControl`.

* Se añadió un nuevo tipo de evento `users.canvas.Conversion`.

* Se añadió un nuevo tipo de evento `users.canvas.Entry`.

* Se añadió un nuevo tipo de evento `users.canvas.exit.MatchedAudience`.

* Se añadió un nuevo tipo de evento `users.canvas.exit.PerformedEvent`.

* Se añadió un nuevo tipo de evento `users.canvas.experimentstep.Conversion`.

* Se añadió un nuevo tipo de evento `users.canvas.experimentstep.SplitEntry`.

* Se añadió un nuevo tipo de evento `users.canvasstep.Progression`.

* Se añadió un nuevo tipo de evento `users.messages.banner.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.banner.Click`.

* Se añadió un nuevo tipo de evento `users.messages.banner.Impression`.

* Se añadió un nuevo tipo de evento `users.messages.contentcard.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.contentcard.Click`.

* Se añadió un nuevo tipo de evento `users.messages.contentcard.Dismiss`.

* Se añadió un nuevo tipo de evento `users.messages.contentcard.Impression`.

* Se añadió un nuevo tipo de evento `users.messages.contentcard.Send`.

* Se añadió un nuevo tipo de evento `users.messages.email.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.email.Bounce`.

* Se añadió un nuevo tipo de evento `users.messages.email.Click`.

* Se añadió un nuevo tipo de evento `users.messages.email.Deferral`.

* Se añadió un nuevo tipo de evento `users.messages.email.Delivery`.

* Se añadió un nuevo tipo de evento `users.messages.email.MarkAsSpam`.

* Se añadió un nuevo tipo de evento `users.messages.email.Open`.

* Se añadió un nuevo tipo de evento `users.messages.email.Send`.

* Se añadió un nuevo tipo de evento `users.messages.email.SoftBounce`.

* Se añadió un nuevo tipo de evento `users.messages.email.Unsubscribe`.

* Se añadió un nuevo tipo de evento `users.messages.featureflag.Impression`.

* Se añadió un nuevo tipo de evento `users.messages.inappmessage.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.inappmessage.Click`.

* Se añadió un nuevo tipo de evento `users.messages.inappmessage.Impression`.

* Se añadió un nuevo tipo de evento `users.messages.liveactivity.Outcome`.

* Se añadió un nuevo tipo de evento `users.messages.liveactivity.Send`.

* Se añadió un nuevo tipo de evento `users.messages.pushnotification.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.pushnotification.Bounce`.

* Se añadió un nuevo tipo de evento `users.messages.pushnotification.IosForeground`.

* Se añadió un nuevo tipo de evento `users.messages.pushnotification.Open`.

* Se añadió un nuevo tipo de evento `users.messages.pushnotification.Send`.

* Se añadió un nuevo tipo de evento `users.messages.sms.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.sms.CarrierSend`.

* Se añadió un nuevo tipo de evento `users.messages.sms.Delivery`.

* Se añadió un nuevo tipo de evento `users.messages.sms.DeliveryFailure`.

* Se añadió un nuevo tipo de evento `users.messages.sms.InboundReceive`.

* Se añadió un nuevo tipo de evento `users.messages.sms.Rejection`.

* Se añadió un nuevo tipo de evento `users.messages.sms.Send`.

* Se añadió un nuevo tipo de evento `users.messages.sms.ShortLinkClick`.

* Se añadió un nuevo tipo de evento `users.messages.webhook.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.webhook.Failure`.

* Se añadió un nuevo tipo de evento `users.messages.webhook.Send`.

* Se añadió un nuevo tipo de evento `users.messages.whatsapp.Abort`.

* Se añadió un nuevo tipo de evento `users.messages.whatsapp.Click`.

* Se añadió un nuevo tipo de evento `users.messages.whatsapp.Delivery`.

* Se añadió un nuevo tipo de evento `users.messages.whatsapp.Failure`.

* Se añadió un nuevo tipo de evento `users.messages.whatsapp.InboundReceive`.

* Se añadió un nuevo tipo de evento `users.messages.whatsapp.Read`.

* Se añadió un nuevo tipo de evento `users.messages.whatsapp.Send`.

* Se añadió un nuevo tipo de evento `users.RandomBucketNumberUpdate`.