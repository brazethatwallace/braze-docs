1. Canvas 작성기를 사용하여 [Canvas를 생성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)합니다.
2. Canvas를 설정한 후 Canvas 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 지정합니다.
3. [단계 스케줄]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types)을 선택하고 필요에 따라 지연을 지정합니다.{% if include.in_app_message %} 인앱 메시지를 포함하는 단계는 액션 기반으로 설정할 수 없습니다.{% endif %}
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. Segments를 지정하고 추가 필터를 적용하여 이 단계의 수신자를 더 세밀하게 조정할 수 있습니다. 오디언스 옵션은 지연 후 메시지가 전송되는 시점에 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)을 선택합니다.
6. 메시지와 함께 연결하려는 다른 메시징 채널을 선택합니다.