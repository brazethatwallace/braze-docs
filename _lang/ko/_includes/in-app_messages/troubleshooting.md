### 표시 문제 해결 {#troubleshooting-in-app-message-display}

앱에서 인앱 메시지를 요청하고 수신하고 있지만 표시되지 않는 경우, 기기 측 로직으로 인해 표시가 차단되고 있을 수 있습니다:

1. 트리거 이벤트가 예상대로 실행되고 있나요? 이를 테스트하려면 세션 시작과 같은 다른 동작으로 메시지가 트리거되도록 구성하고 메시지가 표시되는지 확인합니다.
{% if include.sdk == "iOS" %}
2. 트리거된 인앱 메시지는 [트리거 간 최소 시간 간격]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift#overriding-the-default-rate-limit)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% elsif include.sdk == "Android" %}
2. 트리거된 인앱 메시지는 [트리거 간 최소 시간 간격]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=android#overriding-the-default-rate-limit)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% elsif include.sdk == "Web" %}
2. 트리거된 인앱 메시지는 [트리거 간 최소 시간 간격]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web#overriding-the-default-rate-limit)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% endif %}
3. 이미지 다운로드에 실패하면 이미지가 포함된 인앱 메시지가 표시되지 않습니다. 기기 로그를 확인하여 다운로드 실패 여부를 확인하세요. 이미지를 일시적으로 제거하여 메시지가 표시되는지 확인해 보세요.
{% case include.sdk %}
  {% when "iOS" %}
4. 인앱 메시지 처리를 커스텀하기 위해 델리게이트를 설정한 경우, 델리게이트가 표시를 억제하고 있지 않은지 확인하세요. [커스터마이제이션]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift)을 참조하세요.
  {% when "Android" %}
4. 인앱 메시지 처리를 커스텀하기 위해 델리게이트를 설정한 경우, 델리게이트가 표시를 억제하고 있지 않은지 확인하세요. [커스터마이제이션]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)을 참조하세요.
  {% when "Web" %}
4. [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)를 통해 커스텀 인앱 메시지 처리를 사용하는 경우, 콜백이 표시를 억제하고 있지 않은지 확인하세요. [커스터마이제이션]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=web)을 참조하세요.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
5. 기기 방향이 인앱 메시지 설정과 일치하지 않으면 메시지가 표시되지 않습니다.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. 네트워크 상태에 따라 표시 전에 이미지가 다운로드되지 않을 수 있습니다. 느린 연결이나 저성능 기기에서는 추가 시간을 허용하거나 자산 크기를 최적화하세요.
{% endcase %}

{% if include.sdk == "iOS" %}
### 노출 횟수 및 클릭 수가 기록되지 않음 {#impressions-and-clicks-arent-being-logged}

메시지 표시 또는 클릭 동작을 수동으로 처리하도록 인앱 메시지 델리게이트를 설정한 경우, 인앱 메시지에 대한 [클릭](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) 및 [노출 횟수](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:))를 수동으로 기록해야 합니다.
{% elsif include.sdk == "Android" %}
### 노출 횟수 및 클릭 수가 기록되지 않음

메시지 표시 또는 클릭 동작을 수동으로 처리하도록 인앱 메시지 델리게이트를 설정한 경우, 인앱 메시지에 대한 클릭 및 노출 횟수를 수동으로 기록해야 합니다.
{% endif %}