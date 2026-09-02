인앱 메시지는 **표시 전 Campaign 자격 재평가**가 선택되어 있거나 메시지에 다음 Liquid 태그 중 하나라도 포함되어 있는 경우 템플릿 인앱 메시지로 전달됩니다:

- `canvas_entry_properties`
- `connected_content`
- {% raw %}`{sms.${*}}`{% endraw %}와 같은 단문 메시지 서비스 변수
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

이 경우 세션 시작 시 기기는 전체 메시지 대신 해당 인앱 메시지의 트리거를 수신합니다. 사용자가 인앱 메시지를 트리거하면 사용자의 기기가 네트워크 요청을 보내 실제 메시지를 가져옵니다.

{% alert note %}
기기가 인터넷에 연결되어 있지 않으면 메시지가 전달되지 않습니다. Liquid 로직을 처리하는 데 시간이 너무 오래 걸리면 메시지가 전달되지 않을 수 있습니다.
{% endalert %}