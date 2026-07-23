* イベントタイプ `users.behaviors.pushnotification.TokenStateChange` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加: イベントのプッシュトークン
* イベントタイプ `users.messages.pushnotification.Bounce` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加: イベントのプッシュトークン
* イベントタイプ `users.messages.pushnotification.Send` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加: イベントのプッシュトークン
* イベントタイプ `users.messages.rcs.Click` のフィールド変更:
    * 新しい `string` フィールド `canvas_variation_name` を追加: このユーザーが受信したキャンバスバリエーションの名前
    * フィールド `user_phone_number` が*オプション*になりました。
* イベントタイプ `users.messages.rcs.InboundReceive` のフィールド変更:
    * フィールド `user_id` が*オプション*になりました。
* イベントタイプ `users.messages.rcs.Rejection` のフィールド変更:
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加: このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID