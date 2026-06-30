---
nav_title: 문제 해결
article_title: Braze SDK 인앱 메시지 문제 해결
page_order: 50
description: "증상 색인, 표준 조사 경로, Canvas 인앱 메시지 참고 사항, 플랫폼별 SDK 점검을 통해 인앱 메시지가 전달되지 않거나 표시되지 않는 이유를 진단합니다."
channel:
  - in-app messages

---

# 인앱 메시지 문제 해결 {#troubleshoot-in-app-messages}

> 이 페이지를 사용하여 인앱 메시지가 기기에 전달되지 않거나 표시되지 않는 이유를 진단하세요. 대시보드 설정(우선순위, 트리거, Segment, 재자격)에 대해서는 [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)를 참조하세요.

디버깅을 시작하기 전에 자신을 [테스트 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)로 추가하고 [테스트 메시지 발송]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)을 검토하세요.

## 시작하기: 증상 매칭 {#start-here-match-your-symptom}

| 증상 | 이동 |
| --- | --- |
| 한 명의 사용자에게 인앱 메시지가 표시되지 않음 | [한 명의 사용자](#in-app-message-not-shown-for-one-user) |
| 하나의 플랫폼(Android, iOS 또는 Web)에서 인앱 메시지가 표시되지 않음 | [하나의 플랫폼](#in-app-message-not-shown-on-one-platform) |
| **Canvas** 단계의 인앱 메시지가 표시되지 않음 | [Canvas 인앱 메시지](#canvas-in-app-messages) |
| 인앱 메시지가 늦게 또는 지연 후에 표시됨 | [타이밍 및 지연 표시](#timing-and-delayed-display) |
| 노출 횟수 또는 클릭 수가 잘못 보임 | [노출 횟수 및 분석](#impressions-and-analytics) |
| 이벤트 사용자 로그에서 `triggers`가 누락되거나 비어 있음 | [전달 문제 해결](#delivery-troubleshooting) |
| 트리거가 반환되었지만 기기에 아무것도 표시되지 않음 | [플랫폼별 표시 문제 해결](#platform-specific-display-troubleshooting) |
| 인앱 메시지 자산 로드 실패(iOS, `NSURLError` -1008) | [자산 로드(Swift 탭)]({{site.baseurl}}/developer_guide/in_app_messages/troubleshooting?sdktab=swift#asset-loading) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="인앱 메시지 증상" }

## 표준 조사 경로 {#standard-investigation-path}

모든 인시던트에 대해 이 워크플로를 사용하세요. 1단계부터 시작합니다.

1. 테스트 기기에서 **세션 시작**이 기록되었는지 확인합니다. 인앱 메시지는 세션 시작 시 요청됩니다.
2. [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)를 열고 해당 세션 시작에 대한 SDK 요청을 찾습니다. **Response Data**에서:
   - 원시 JSON에서 `respond_with`에 `"triggers": true`가 포함되어 있는지 확인합니다.
   - **Requested Responses** 행에 **`triggers`**가 포함되어야 합니다.
   - **Trigger In-App Message** 행에 해당 요청에 대해 반환된 각 인앱 메시지가 나열됩니다.
   - `triggers` 키가 없거나 **Trigger In-App Message** 행이 없으면 [메시지가 요청되지 않는 문제 해결](#troubleshoot-messages-not-being-requested)로 이동하세요.
   - `triggers`가 있지만 비어 있으면(`[]`) [메시지가 반환되지 않는 문제 해결](#troubleshoot-messages-not-being-returned)로 이동하세요.
   - **Trigger In-App Message** 행이 있지만 아무것도 표시되지 않으면 [플랫폼별 표시 문제 해결](#platform-specific-display-troubleshooting)로 이동하세요.
   - 각 트리거 페이로드에는 `type`이 포함됩니다: `inapp`(표준) 또는 `templated_iam`(표시 전 템플릿 요청 필요). [인앱 메시지 유형]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages)을 참조하세요.
3. 대시보드 측 자격(Segment, 재자격, 빈도 제한, 우선순위, 대조군)에 대해서는 [전달 문제 해결](#delivery-troubleshooting) 및 [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)를 참조하세요.
4. 기기 측 표시 문제(델리게이트, 사용량 제한, 방향, 세션 타임아웃)에 대해서는 [플랫폼별 표시 문제 해결](#platform-specific-display-troubleshooting)에서 SDK 탭을 선택하세요.

## Canvas 인앱 메시지 {#canvas-in-app-messages}

**증상:** 사용자가 Canvas 인앱 메시지 단계에 진입했지만 예상 시점에 메시지가 표시되지 않았습니다.

대부분의 Canvas 및 인앱 메시지 티켓은 세 가지 동작에 의해 발생합니다:

1. **다음 세션 표시:** Canvas 인앱 메시지는 단계가 처리된 후 *다음* 세션 시작 시 자격이 부여됩니다. 세션 중간에 즉시 표시되지 않습니다. Canvas FAQ의 [Canvas에서 인앱 메시지는 언제 발송되나요?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent)를 참조하세요.
2. **단계 진입 시 전달 유효성 검사:** 메시지 단계에서 **메시지 발송 시 오디언스 유효성 검사**가 활성화된 경우, Segment 멤버십과 빈도 제한은 표시 시점이 아닌 사용자가 **단계에 진입할 때** 평가됩니다. [전달 유효성 검사]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)를 참조하세요.
3. **지연 및 세션 타임아웃:** 사용자가 SDK 세션 타임아웃보다 긴 지연 단계에 진입하면, 인앱 메시지 단계 전에 새 세션을 시작할 수 있습니다. 표시를 기대하는 세션 시작 시 메시지가 가져와지지 않을 수 있습니다.

가용 기간, 만료, Canvas 분석에서 _발송 수_ 0에 대해서는 Canvas FAQ의 [인앱 메시지 및 전달]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery)을 참조하세요.

{% alert important %}
Canvas의 인앱 메시지는 REST API가 아닌 SDK를 통해 전송된 이벤트에 의해서만 트리거될 수 있습니다.
{% endalert %}

## 한 명의 사용자에게 인앱 메시지가 표시되지 않음 {#in-app-message-not-shown-for-one-user}

**증상:** 한 명의 사용자가 예상된 인앱 메시지를 받지 못했으며, 다른 사용자는 영향을 받지 않을 수 있습니다.

다음 항목을 확인하세요:

- SDK가 새 인앱 메시지를 요청하는 **세션 시작** 시점에 사용자가 Segment에 포함되어 있었나요?
- Campaign 또는 Canvas 타겟팅 규칙에 따라 사용자가 자격이 있거나 재자격이 있었나요? [Campaign 및 Canvas 재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 참조하세요.
- [빈도 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)이 적용되었나요?
- 사용자가 Campaign 대조군에 포함되었나요? Campaign이 A/B 테스트로 구성되어 있는지 확인하세요.
- 더 높은 우선순위의 인앱 메시지가 대신 표시되었나요? 인앱 메시지 FAQ의 [같은 세션에서 여러 인앱 메시지가 표시될 수 있나요?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session)를 참조하세요.
- 기기가 Campaign에서 지정한 방향이었나요?
- 트리거 간 기본 30초 최소 간격에 의해 메시지가 억제되었나요? [기본 사용량 제한 재정의]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#overriding-the-default-rate-limit)를 참조하세요.

그런 다음 [표준 조사 경로](#standard-investigation-path)를 따르세요.

## 하나의 플랫폼에서 인앱 메시지가 표시되지 않음 {#in-app-message-not-shown-on-one-platform}

**증상:** Android, iOS 또는 Web에서 인앱 메시지가 표시되지 않지만 다른 플랫폼에서는 작동할 수 있습니다.

| 가능한 원인 | 확인 사항 |
| --- | --- |
| 잘못된 **Send To** 타겟 | Campaign 또는 Canvas 단계가 적절하게 **Mobile Apps** 또는 **Web Browsers**를 타겟으로 하는지 확인하세요. Web 전용 Campaign은 Android 기기에 발송되지 않습니다. |
| 커스텀 UI 또는 핸들러가 표시를 억제함 | 델리게이트(모바일) 또는 [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)(Web)를 검토하세요. [커스터마이징]({{site.baseurl}}/developer_guide/in_app_messages/customization) 및 아래 SDK 탭을 참조하세요. |
| 이 플랫폼에서 통합이 작동한 적이 없음 | 이 플랫폼과 앱 버전에서 이전에 인앱 메시지가 표시된 적이 있는지 확인하세요. |
| 기기에서 트리거가 실행되지 않음 | 트리거는 SDK를 통해 로컬에서 발생해야 합니다. REST API 호출로는 SDK에서 인앱 메시지를 트리거할 수 없습니다. [메시지 트리거]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages)를 참조하세요. |
| 이벤트 사용자 로그에서 `triggers`가 비어 있음 | Segment, 재자격, 빈도 제한 또는 대조군 문제입니다. [메시지가 반환되지 않는 문제 해결](#troubleshoot-messages-not-being-returned)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="플랫폼 증상 원인" }

## 모든 사용자에게 인앱 메시지가 표시되지 않음 {#in-app-message-not-shown-for-all-users}

**증상:** 인앱 메시지를 받은 사용자가 없거나 예상보다 적습니다.

다음 항목을 확인하세요:

- 대시보드와 앱 통합에서 트리거 동작이 올바르게 구성되어 있나요?
- 더 높은 우선순위의 인앱 메시지가 Campaign을 가로챘나요? [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session)를 참조하세요.
- 최신 SDK 버전을 사용하고 있나요? 일부 인앱 메시지 유형에는 최소 SDK 요구 사항이 있습니다.
- 세션이 올바르게 통합되어 있나요? 이 앱에서 세션 분석이 작동하는지 확인하세요.
- 커스터마이징된 UI 라이브러리가 표시를 방해하고 있나요? [커스터마이징]({{site.baseurl}}/developer_guide/in_app_messages/customization)을 참조하세요.

그런 다음 [표준 조사 경로](#standard-investigation-path)를 따르세요.

## 타이밍 및 지연 표시 {#timing-and-delayed-display}

**증상:** 인앱 메시지가 예상보다 늦게 표시되거나 새 세션이 시작될 때까지 표시되지 않았습니다.

일반적인 원인:

- **Campaign 세션 시작 프리페치:** 인앱 메시지는 세션 시작 시 캐시되고 트리거가 실행될 때 표시됩니다. 다음 세션 시작 전에 발생하는 트리거는 해당 세션까지 표시되지 않습니다. [메시지 트리거]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages)를 참조하세요.
- **Canvas 다음 세션 동작:** [Canvas 인앱 메시지](#canvas-in-app-messages)를 참조하세요.
- **스케줄된 대시보드 지연:** Campaign 또는 단계에 지연이 구성되어 있는지 확인하세요.
- **트리거 동기화 경합:** 사용자가 세션 시작 직후 이벤트를 기록하면 트리거가 아직 동기화되지 않았을 수 있습니다. 세션 시작으로 트리거하고 의도한 이벤트로 세분화하여 이벤트 이후 다음 세션에 전달되도록 하는 것을 고려하세요.
- **순차적 인앱 메시지:** 투어에서 메시지를 지연하거나 복원하는 경우 [트리거된 인앱 메시지 지연]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)을 참조하세요.
- **대용량 자산 또는 느린 CDN:** HTML 인앱 메시지의 이미지와 동영상을 최적화하세요. 모바일에서는 느린 네트워크에서 표시 전에 이미지가 다운로드될 수 있습니다. 플랫폼 참고 사항은 아래 SDK 탭을 선택하세요.

{% alert note %}
인앱 메시지가 세션 시작으로 트리거되고 연장된 세션 타임아웃을 설정한 경우, 해당 기간 내에 앱을 닫았다가 다시 열어도 세션이 새로고침되지 않습니다. 예를 들어, 300초 타임아웃의 경우 세션 시작 인앱 메시지는 세션이 실제로 새로고침될 때까지 표시되지 않습니다. 이것이 테스트에 영향을 미치는 경우 세션 타임아웃 또는 트리거 유형을 조정하세요.
{% endalert %}

## 전달 문제 해결 {#delivery-troubleshooting}

대부분의 인앱 메시지 문제는 **전달**(기기가 트리거를 수신하지 못함) 또는 **표시**(트리거가 도착했지만 표시되지 않음)입니다. 먼저 [전달](#troubleshooting-in-app-message-delivery)을 확인한 다음 [표시](#platform-specific-display-troubleshooting)를 점검하세요.

### 전달 문제 해결 {#troubleshooting-in-app-message-delivery}

SDK는 세션 시작 시 Braze 서버에 인앱 메시지를 요청합니다. SDK가 트리거를 요청하고 Braze가 이를 반환하는지 확인하세요.

#### 메시지가 요청되고 반환되는지 확인 {#check-if-messages-are-requested-and-returned}

1. 자신을 [테스트 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)로 추가합니다.
2. 사용자를 타겟으로 하는 인앱 메시지 Campaign을 설정합니다.
3. 애플리케이션에서 새 세션을 시작합니다.
4. [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)에서 세션 시작 이벤트에 대한 SDK 요청을 찾습니다. **Response Data**에서:
   - 원시 JSON에서 `respond_with`에 `"triggers": true`가 포함되어 있는지 확인합니다.
   - **Requested Responses** 행에 응답의 최상위 키가 나열됩니다. 인앱 메시지의 경우 **`triggers`**가 있어야 합니다.
   - **Trigger In-App Message** 행에 해당 요청에 대해 반환된 각 인앱 메시지가 나열됩니다.

   그런 다음 분류합니다:
   - `triggers` 키 또는 **Trigger In-App Message** 행이 없으면 [메시지가 요청되지 않는 문제 해결](#troubleshoot-messages-not-being-requested)을 참조하세요.
   - `triggers`가 있지만 비어 있으면(`[]`) [메시지가 반환되지 않는 문제 해결](#troubleshoot-messages-not-being-returned)을 참조하세요.
   - **Trigger In-App Message** 행이 있지만 기기에 아무것도 표시되지 않으면 [플랫폼별 표시 문제 해결](#platform-specific-display-troubleshooting)을 참조하세요.
   - 각 트리거 페이로드에는 `type`이 포함됩니다: `inapp`(표준) 또는 `templated_iam`(표시 전 템플릿 요청 필요). [인앱 메시지 유형]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages)을 참조하세요.
5. 응답 데이터에 올바른 인앱 메시지가 나타나는지 확인합니다.

![SDK 요청 및 응답 데이터가 포함된 이벤트 사용자 로그]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### 메시지가 요청되지 않는 문제 해결 {#troubleshoot-messages-not-being-requested}

인앱 메시지가 요청되지 않는 경우, 앱이 세션을 올바르게 추적하지 못하고 있을 수 있습니다. 인앱 메시지는 세션 시작 시 새로고침됩니다. 세션 타임아웃 의미론에 따라 앱이 세션을 시작하고 있는지 확인하세요:

![성공적인 세션 시작 이벤트를 표시하는 이벤트 사용자 로그의 SDK 요청]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### 메시지가 반환되지 않는 문제 해결 {#troubleshoot-messages-not-being-returned}

인앱 메시지가 반환되지 않는 경우, 타겟팅 또는 자격 문제일 가능성이 높습니다:

1. Segment에 사용자가 포함되어 있지 않습니다.
   - 사용자의 [**참여**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) 탭에서 예상 Segment를 확인하세요.
2. 사용자가 이미 메시지를 받았고 재자격이 없었습니다.
   - [재자격 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) 및 [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#campaigns)를 확인하세요.
3. 사용자가 빈도 제한에 도달했습니다.
   - [빈도 제한 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)을 확인하세요.
4. 사용자가 대조군에 포함되었습니다.
   - **Received campaign variant** 필터를 **Control**로 설정한 Segment를 생성하거나, 통합 테스트 중에는 대조군을 옵트아웃하세요.
5. 더 높은 우선순위의 인앱 메시지가 우선했습니다. [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session)를 참조하세요.

아카이브된 Campaign, 트리거 구성, 방해금지 시간에 대해서는 [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)를 참조하세요.

## 노출 횟수 및 분석 {#impressions-and-analytics}

**증상:** 노출 횟수 또는 클릭 수가 예상과 일치하지 않습니다.

- **_노출 횟수_가 _고유 노출 횟수_보다 큼:** 사용자가 여러 기기를 사용하거나 스케줄된 지연으로 인해 동일한 사용자가 두 번 이상 자격을 얻는 경우 예상되는 결과입니다. [Campaign 및 Canvas 재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 참조하세요.
- **노출 횟수가 예상보다 낮음:** 사용자가 메시지를 보지 않았을 수 있고(노출 횟수는 표시 시 기록됨), 여러 높은 우선순위 메시지가 서로를 가로챌 수 있으며, 트리거 동기화 경합이 적용될 수 있습니다. Canvas 인앱 메시지에 대해서는 [Canvas 인앱 메시지](#canvas-in-app-messages)를 참조하세요. 전체 측정기준 정의는 [인앱 메시지 보고]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) 및 [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)를 참조하세요.
- **노출 횟수가 이전보다 낮음:** Segment 및 Campaign 변경 로그를 검토하세요. 더 높은 우선순위의 Campaign에서 동일한 트리거 이벤트를 재사용하지 않았는지 확인하세요.

![사용자가 마지막으로 Campaign을 확인한 이후 7개의 변경 사항이 있는 Campaign 세부 정보 페이지의 변경 로그 보기 링크]({% image_buster /assets/img_archive/trouble4.png %})

델리게이트 또는 커스텀 핸들러를 사용하여 인앱 메시지를 수동으로 표시하는 경우, 노출 횟수와 클릭 수를 직접 기록해야 합니다. Swift 및 Android 세부 사항은 [플랫폼별 표시 문제 해결](#platform-specific-display-troubleshooting)에서 SDK 탭을 참조하고, Web의 경우 [인앱 메시지 데이터 기록]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data)을 참조하세요.

## 플랫폼별 표시 문제 해결 {#platform-specific-display-troubleshooting}

이벤트 사용자 로그에 **Trigger In-App Message** 행이 나타나지만 기기에 아무것도 표시되지 않는 경우, SDK 탭을 선택하여 표시 점검(델리게이트, 사용량 제한, 방향, 커스텀 핸들러)을 확인하세요.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}