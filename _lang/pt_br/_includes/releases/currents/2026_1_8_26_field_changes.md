* Alterações de campo no tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adicionado novo campo `string` `push_token`: token por push do evento
* Alterações de campo no tipo de evento `users.messages.pushnotification.Bounce`:
    * Adicionado novo campo `string` `push_token`: token por push do evento
* Alterações de campo no tipo de evento `users.messages.pushnotification.Send`:
    * Adicionado novo campo `string` `push_token`: token por push do evento
* Alterações de campo no tipo de evento `users.messages.rcs.Click`:
    * Adicionado novo campo `string` `canvas_variation_name`: nome da variação do Canvas que este usuário recebeu
    * O campo `user_phone_number` agora é *opcional*.
* Alterações de campo no tipo de evento `users.messages.rcs.InboundReceive`:
    * O campo `user_id` agora é *opcional*.
* Alterações de campo no tipo de evento `users.messages.rcs.Rejection`:
    * Adicionado novo campo `string` `canvas_step_message_variation_id`: ID de API or interface de programação do aplicativo (API) da variação de mensagem da etapa do Canvas que este usuário recebeu