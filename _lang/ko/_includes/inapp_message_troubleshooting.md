## 기본 점검 {#basic-checks}

### 한 사용자에 대한 인앱 메시지가 표시되지 않았습니다 {#my-in-app-message-wasnt-shown-for-one-user}

1. SDK가 새 인앱 메시지를 요청할 때 사용자가 세션 시작 시점에 Segment에 있었나요?
2. 사용자가 Campaign 타겟팅 규칙에 따라 인앱 메시지를 수신할 자격이 있거나 재자격이 있었나요?
3. 사용자가 빈도 제한의 영향을 받았나요?
4. 사용자가 대조군에 속해 있었나요? Campaign이 AB 테스트용으로 구성되어 있는지 확인하세요.
5. 예상 메시지 대신 다른 우선순위가 높은 인앱 메시지가 표시되었나요?
6. 내 기기가 Campaign에서 지정한 올바른 방향이었나요?
7. SDK에서 적용하는 트리거 간 기본 30초 최소 시간 간격으로 인해 메시지가 억제되었나요?

### 내 인앱 메시지가 이 플랫폼의 모든 사용자에게 표시되지 않았습니다 {#my-in-app-message-wasnt-shown-to-all-users-on-this-platform}

1. Campaign이 모바일 앱 또는 웹 브라우저를 적절하게 타겟팅하도록 구성되어 있나요? 예를 들어, Campaign이 웹 브라우저만 타겟팅하는 경우 Android 기기에는 전송되지 않습니다.
2. 커스텀 UI를 구현했으며 의도한 대로 작동하고 있나요? 표시를 방해할 수 있는 다른 앱 측의 커스텀 처리 또는 억제 기능이 있나요?
3. 이 특정 플랫폼 및 앱 버전에서 인앱 메시지를 성공적으로 표시한 적이 있나요?
4. 트리거가 기기에서 로컬로 발생했나요? REST 호출은 SDK에서 인앱 메시지를 트리거하는 데 사용할 수 없다는 점에 유의하세요.

### 내 인앱 메시지가 모든 사용자에게 표시되지 않음 {#my-in-app-message-wasnt-shown-for-all-users}

1. 트리거 동작이 대시보드와 앱 통합에서 올바르게 설정되었나요?
2. 예상 메시지 대신 다른 우선순위가 높은 인앱 메시지가 표시되었나요?
3. 최신 버전의 SDK를 사용 중이신가요? 일부 인앱 메시지 유형에는 SDK 버전 요구 사항이 있습니다.
4. 세션이 통합에 제대로 통합되었나요? 이 앱에서 세션 분석이 작동하나요?
5. 인앱 메시지 표시를 방해할 수 있는 커스텀 구성요소 라이브러리를 사용하고 있나요?

### 인앱 메시지가 표시되는 데 시간이 많이 걸렸습니다 {#my-in-app-message-took-a-lot-of-time-to-appear}

1. CDN에서 HTML 기반 인앱 메시지로 대용량 이미지 또는 동영상 파일을 전송하는 경우 파일이 최대한 작게 최적화되어 있는지, CDN의 성능이 정상인지 확인하세요.
2. 대시보드에서 인앱 메시지에 `delay`를 구성했는지 확인합니다.
{% case include.sdk %}
  {% when "iOS", "Android" %}
3. 상황에 따라 인앱 메시지는 표시되기 전에 디스크에서 관련 이미지를 다운로드하거나 로드합니다. 네트워크 연결 속도가 느리거나 성능이 매우 낮은 기기를 사용하는 경우 이 프로세스에 시간이 걸릴 수 있습니다. 이미지가 가능한 한 작게 최적화되었는지 확인하세요.
{% endcase %}

이러한 시나리오에 대해 자세히 알아보려면 <a id="troubleshooting-in-app-advanced">고급 문제 해결 섹션</a>을 참조하세요.

## 노출 횟수 및 클릭 분석 관련 문제 {#issues-with-impressions-and-click-analytics}

{% if include.sdk == "iOS" %}
### 노출 횟수 및 클릭 수가 기록되지 않습니다 {#impressions-and-clicks-arent-being-logged}

메시지 표시 또는 클릭 동작을 수동으로 처리하도록 인앱 메시지 델리게이트를 설정한 경우 인앱 메시지에 대한 [클릭](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) 및 [노출 횟수](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:))를 수동으로 기록해야 합니다.
{% elsif include.sdk == "Android" %}
### 노출 횟수 및 클릭 수가 기록되지 않습니다 {#impressions-and-clicks-arent-being-logged}
메시지 표시 또는 클릭 동작을 수동으로 처리하도록 인앱 메시지 델리게이트를 설정한 경우 인앱 메시지에 대한 클릭 및 노출 횟수를 수동으로 기록해야 합니다.
{% endif %}

### *노출 횟수*가 *고유 노출 횟수*보다 큽니다 {#impressions-are-greater-than-unique-impressions}

이는 예상되는 동작이며 다음과 같은 경우에 발생할 수 있습니다:

- 재자격이 꺼져 있더라도 Campaign을 수신한 사용자가 여러 기기를 가지고 있을 수 있습니다. Campaign 트리거는 다음 세션 시작 시 업데이트되므로, 사용자가 새 세션을 시작하기 전까지 한 기기는 다른 기기가 이미 Campaign을 트리거했는지 알 수 없습니다.
- 인앱 메시지에 트리거 이벤트 발생 후 몇 분의 스케줄된 지연이 있는 경우, 사용자가 메시지를 두 번 이상 수신했을 수 있습니다.

재자격에 대한 자세한 내용은 [Campaign 및 Canvas 재자격]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/)을 참조하세요.

### 노출 횟수가 예상보다 낮습니다 {#impressions-are-lower-than-expected}

1. 트리거는 세션 시작 시 기기와 동기화하는 데 시간이 걸리므로 사용자가 세션 시작 직후 이벤트 또는 구매를 기록하면 경합 조건이 발생할 수 있습니다. 한 가지 가능한 해결 방법은 세션 시작 시 트리거하도록 Campaign을 변경한 다음, 의도한 이벤트 또는 구매를 기준으로 세그먼트를 나누는 것입니다. 이렇게 하면 이벤트가 발생한 후 다음 세션이 시작될 때 인앱 메시지가 전달됩니다.

2. Campaign이 세션 시작 또는 커스텀 이벤트에 의해 트리거되는 경우, 이 이벤트 또는 세션이 메시지를 트리거할 수 있을 만큼 자주 발생하는지 확인해야 합니다. 이 데이터는 [개요]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data)(세션 데이터의 경우) 또는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting) 페이지에서 확인할 수 있습니다:

![한 달 동안 즐겨찾기에 추가 커스텀 이벤트가 발생한 횟수를 그래프로 보여주는 커스텀 이벤트 페이지]({% image_buster /assets/img_archive/trouble5.png %})

기타 이유는 다음과 같습니다:

- 사용자가 인앱 메시지를 보지 않아 노출 횟수가 기록되지 않았습니다.
- 여러 인앱 메시지가 서로 간섭하고 있습니다(예: 여러 높은 우선순위 메시지).
- 메시지가 Canvas에 있는 경우, 사용자가 인앱 메시지를 수신하기 전에 세션 타임아웃보다 긴 지연 단계에 진입할 수 있습니다.

### 노출 횟수가 이전보다 감소했습니다 {#impressions-are-lower-than-they-used-to-be}

1. 출시 이후 Segment나 Campaign을 의도치 않게 변경한 사람이 없는지 확인하세요. Segment 및 Campaign 체인지로그를 통해 변경된 사항, 변경을 수행한 사람, 변경이 발생한 시점에 대한 인사이트를 얻을 수 있습니다.

![사용자가 마지막으로 Campaign을 본 이후 7가지 변경 사항이 포함된 Campaign 세부 정보 페이지의 체인지로그 보기 링크]({% image_buster /assets/img_archive/trouble4.png %})

{: start="2"}
2. 별도의 인앱 메시지 Campaign에서 더 높은 우선순위를 가진 트리거 이벤트를 재사용하지 않았는지 확인하세요.

## 고급 문제 해결 {#troubleshooting-in-app-advanced}

대부분의 인앱 메시지 문제는 전달과 표시라는 두 가지 주요 카테고리로 분류할 수 있습니다. 예상 인앱 메시지가 기기에 표시되지 않는 문제를 해결하려면 <a id="troubleshooting-in-app-message-delivery">인앱 메시지가 기기에 전달되었는지</a> 확인한 다음 <a id="troubleshooting-in-app-message-display">메시지 표시 문제를 해결</a>하세요.

### 전달 문제 해결 {#troubleshooting-in-app-message-delivery}

SDK는 세션 시작 시 Braze 서버에 인앱 메시지를 요청합니다. 인앱 메시지가 기기에 전달되고 있는지 확인하려면 인앱 메시지가 SDK에 의해 요청되고 Braze 서버에 의해 반환되는지 확인해야 합니다.

#### 메시지 요청 및 반환 여부 확인 {#check-if-messages-are-requested-and-returned}

1. 대시보드에서 [테스트 사용자]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users)로 자신을 추가하세요.
2. 사용자를 대상으로 인앱 메시지 Campaign을 설정합니다.
3. 애플리케이션에서 새 세션이 발생하는지 확인합니다.
4. [이벤트 사용자 로그]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)를 사용하여 기기가 세션 시작 시 인앱 메시지를 요청하고 있는지 확인하세요. 테스트 사용자의 세션 시작 이벤트와 연결된 SDK 요청을 찾습니다.
  - 앱에서 트리거된 인앱 메시지를 요청하는 경우 **Response Data** 아래 **Requested Responses** 필드에 `trigger`가 표시되어야 합니다.
  - 앱에서 원본 인앱 메시지를 요청하는 경우 **Response Data** 아래 **Requested Responses** 필드에 `in_app`이 표시되어야 합니다.
5. [이벤트 사용자 로그]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)를 사용하여 응답 데이터에서 올바른 인앱 메시지가 반환되고 있는지 확인하세요.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### 요청되지 않는 메시지 문제 해결 {#troubleshoot-messages-not-being-requested}

인앱 메시지가 요청되지 않는 경우 앱이 세션을 올바르게 추적하지 않을 수 있습니다. 인앱 메시지는 세션 시작 시 새로고침되기 때문입니다. 또한 앱의 세션 타임아웃 설정에 따라 앱이 실제로 세션을 시작하고 있는지 확인해야 합니다:

![이벤트 사용자 로그에서 성공적인 세션 시작 이벤트를 표시하는 SDK 요청]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### 반환되지 않는 메시지 문제 해결 {#troubleshoot-messages-not-being-returned}

인앱 메시지가 반환되지 않는다면 Campaign 타겟팅에 문제가 있을 가능성이 높습니다:

1. Segment에 사용자가 포함되어 있지 않습니다.
  - 사용자의 [**참여**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) 탭을 확인하여 **Segments** 아래에 올바른 Segment가 나타나는지 확인하세요.
2. 사용자가 이전에 인앱 메시지를 받은 적이 있으며 다시 받을 자격이 없습니다.
  - **Campaign Composer**의 **Delivery** 단계에서 [Campaign 재자격 설정]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/)을 확인하고 재자격 설정이 테스트 설정과 일치하는지 확인하세요.
3. 사용자가 Campaign의 빈도 제한에 도달했습니다.
  - Campaign [빈도 제한 설정]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)을 확인하고 테스트 설정과 일치하는지 확인하세요.
4. Campaign에 대조군이 있는 경우 사용자가 대조군에 속했을 수 있습니다.
  - Campaign 배리언트가 **Control**로 설정된 수신된 캠페인 배리언트 필터로 Segment를 생성하고 사용자가 해당 Segment에 속하는지 확인하여 이 문제가 발생했는지 확인할 수 있습니다.
  - 통합 테스트 목적으로 Campaign을 생성할 때는 대조군 추가를 옵트아웃해야 합니다.


### 표시 문제 해결 {#troubleshooting-in-app-message-display}

앱에서 인앱 메시지를 성공적으로 요청하고 수신하고 있지만 표시되지 않는 경우 기기 측 로직으로 인해 표시가 차단되고 있을 수 있습니다:

1. 트리거 이벤트가 예상대로 실행되고 있나요? 이를 테스트하려면 세션 시작과 같은 다른 동작을 사용하여 메시지가 트리거되도록 구성하고 메시지가 표시되는지 확인합니다.
{% if include.sdk == "iOS" %}
2. 트리거된 인앱 메시지는 [트리거 간 최소 시간 간격]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% elsif include.sdk == "Android" %}
2. 트리거된 인앱 메시지는 [트리거 간 최소 시간 간격]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% elsif include.sdk == "Web" %}
2. 트리거된 인앱 메시지는 [트리거 간 최소 시간 간격]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% endif %}
3. 이미지 다운로드에 실패하면 이미지가 포함된 인앱 메시지가 표시되지 않습니다. 기기 로그를 확인하여 이미지 다운로드가 실패하지 않았는지 확인하세요. 메시지에서 이미지를 일시적으로 제거하여 메시지가 표시되는지 확인해 보세요.
{% case include.sdk %}
  {% when "iOS", "Android" %}
4. 인앱 메시지 처리를 커스텀하기 위해 델리게이트를 설정한 경우, 델리게이트가 인앱 메시지 표시를 방해하지 않는지 확인하세요.
  {% when "Web" %}
5. `braze.subscribeToInAppMessage` 또는 `appboy.subscribeToNewInAppMessages`를 통해 커스텀 인앱 메시지 처리를 하고 있는 경우 해당 구독을 확인하여 인앱 메시지 표시에 영향을 미치지 않는지 확인하세요.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. 기기 방향이 인앱 메시지에 지정된 방향과 일치하지 않으면 인앱 메시지가 표시되지 않습니다. 기기의 방향이 올바른지 확인하세요.
{% endcase %}
7. 인앱 메시지가 세션 시작 시 트리거되고 연장된 세션 타임아웃을 설정한 경우 메시지를 표시할 수 있는 속도에 영향을 미칩니다. 예를 들어 세션 타임아웃이 300초로 설정된 경우 이 시간 내에 앱을 닫았다가 다시 열면 세션이 새로고침되지 않으므로 세션 시작 시 트리거되는 인앱 메시지가 표시되지 않습니다.