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
    * Se añadió un nuevo campo `string` `canvas_step_message_variation_id`: ID de API de la variación de mensaje del paso en Canvas que recibió este usuario