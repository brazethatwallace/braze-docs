* Modifications de champs pour le type d'événement `users.behaviors.pushnotification.TokenStateChange` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement
* Modifications de champs pour le type d'événement `users.messages.pushnotification.Bounce` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement
* Modifications de champs pour le type d'événement `users.messages.pushnotification.Send` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement
* Modifications de champs pour le type d'événement `users.messages.rcs.Click` :
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variation Canvas reçue par cet utilisateur
    * Le champ `user_phone_number` est désormais *facultatif*.
* Modifications de champs pour le type d'événement `users.messages.rcs.InboundReceive` :
    * Le champ `user_id` est désormais *facultatif*.
* Modifications de champs pour le type d'événement `users.messages.rcs.Rejection` :
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variation de message de l'étape du Canvas reçue par cet utilisateur