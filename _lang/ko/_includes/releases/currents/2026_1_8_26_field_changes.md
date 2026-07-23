* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`의 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.pushnotification.Bounce`의 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.pushnotification.Send`의 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.rcs.Click`의 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 수신한 Canvas 배리에이션의 이름
    * 필드 `user_phone_number`은 이제 *선택 사항*입니다.
* 이벤트 유형 `users.messages.rcs.InboundReceive`의 필드 변경 사항:
    * 필드 `user_id`는 이제 *선택 사항*입니다.
* 이벤트 유형 `users.messages.rcs.Rejection`의 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 수신한 캔버스 단계 메시지 배리에이션의 API ID