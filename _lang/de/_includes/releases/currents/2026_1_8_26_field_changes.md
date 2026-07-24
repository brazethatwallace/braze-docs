* Feldänderungen am Ereignistyp `users.behaviors.pushnotification.TokenStateChange`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Ereignisses
* Feldänderungen am Ereignistyp `users.messages.pushnotification.Bounce`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Ereignisses
* Feldänderungen am Ereignistyp `users.messages.pushnotification.Send`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Ereignisses
* Feldänderungen am Ereignistyp `users.messages.rcs.Click`:
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
    * Feld `user_phone_number` ist jetzt *optional*.
* Feldänderungen am Ereignistyp `users.messages.rcs.InboundReceive`:
    * Feld `user_id` ist jetzt *optional*.
* Feldänderungen am Ereignistyp `users.messages.rcs.Rejection`:
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat