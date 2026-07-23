* Field changes to event type `users.behaviors.pushnotification.TokenStateChange`:
    * Added new `string` field `push_token`: Push token of the event
* Field changes to event type `users.messages.pushnotification.Bounce`:
    * Added new `string` field `push_token`: Push token of the event
* Field changes to event type `users.messages.pushnotification.Send`:
    * Added new `string` field `push_token`: Push token of the event
* Field changes to event type `users.messages.rcs.Click`:
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Field `user_phone_number` is now *optional*.
* Field changes to event type `users.messages.rcs.InboundReceive`:
    * Field `user_id` is now *optional*.
* Field changes to event type `users.messages.rcs.Rejection`:
    * Added new `string` field `canvas_step_message_variation_id`: API ID of the Canvas step message variation this user received
