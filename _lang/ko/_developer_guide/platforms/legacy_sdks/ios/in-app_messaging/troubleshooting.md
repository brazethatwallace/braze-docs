---
nav_title: 문제 해결
article_title: iOS용 인앱 메시징 문제 해결
platform: iOS
page_order: 7
description: "이 참조 문서에서는 잠재적인 iOS 인앱 메시지 문제 해결 주제를 다룹니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 인앱 메시지 문제 해결 {#troubleshoot-in-app-messages}

## 노출 횟수 {#impressions}

### 노출 또는 클릭 분석이 기록되지 않음 {#impression-or-click-analytics-arent-being-logged}

인앱 메시지 델리게이트를 설정하여 메시지 표시 또는 클릭 액션을 수동으로 처리하는 경우, 인앱 메시지에서 클릭과 노출 횟수를 수동으로 기록해야 합니다.

#### 노출 횟수가 예상보다 낮음 {#impressions-are-lower-than-expected}

트리거는 세션 시작 시 기기에 동기화되는 데 시간이 걸리므로, 사용자가 세션을 시작한 직후 이벤트나 구매를 기록하면 경합 조건이 발생할 수 있습니다. 한 가지 해결 방법은 Campaign의 트리거를 세션 시작으로 변경한 다음 원하는 이벤트 또는 구매를 기준으로 Segment를 구성하는 것입니다. 이 경우 인앱 메시지는 이벤트가 발생한 후 다음 세션 시작 시 전달됩니다.

## 예상한 인앱 메시지가 표시되지 않음 {#expected-in-app-message-did-not-display}

대부분의 인앱 메시지 문제는 전달과 표시라는 두 가지 주요 범주로 나눌 수 있습니다. 예상한 인앱 메시지가 기기에 표시되지 않는 이유를 해결하려면, 먼저 [인앱 메시지가 기기에 전달되었는지](#troubleshooting-in-app-message-delivery) 확인한 다음 [메시지 표시 문제를 해결](#troubleshooting-in-app-message-display)해야 합니다.

### 인앱 메시지 전달 {#troubleshooting-in-app-message-delivery}

SDK는 세션 시작 시 Braze 서버에 인앱 메시지를 요청합니다. 인앱 메시지가 기기에 전달되고 있는지 확인하려면, SDK에서 인앱 메시지를 요청하고 있고 Braze 서버에서 반환하고 있는지 모두 확인해야 합니다.

#### 메시지가 요청되고 반환되는지 확인 {#check-if-messages-are-requested-and-returned}

1. 대시보드에서 자신을 [테스트 사용자]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users)로 추가합니다.
2. 사용자를 타겟팅하는 인앱 메시지 Campaign을 설정합니다.
3. 앱에서 새 세션이 시작되도록 합니다.
4. [이벤트 사용자 로그]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)를 사용하여 기기가 세션 시작 시 인앱 메시지를 요청하고 있는지 확인합니다. 테스트 사용자의 세션 시작 이벤트와 관련된 SDK 요청을 찾으세요.
  - 앱이 트리거된 인앱 메시지를 요청하도록 설정된 경우, **Response Data** 아래의 **Requested Responses** 필드에 `trigger`가 표시되어야 합니다.
  - 앱이 원래 인앱 메시지를 요청하도록 설정된 경우, **Response Data** 아래의 **Requested Responses** 필드에 `in_app`이 표시되어야 합니다.
5. [이벤트 사용자 로그]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)를 사용하여 올바른 인앱 메시지가 응답 데이터에 반환되고 있는지 확인합니다.<br>![인앱 메시지 요청에 대한 이벤트 사용자 로그 항목.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### 메시지가 요청되지 않는 경우 문제 해결 {#troubleshoot-messages-not-being-requested}

인앱 메시지가 요청되지 않는 경우, 인앱 메시지는 세션 시작 시 새로고침되므로 앱이 세션을 올바르게 추적하지 못하고 있을 수 있습니다. 또한 앱의 세션 타임아웃 설정에 따라 실제로 세션이 시작되고 있는지 확인하세요.

![성공적인 세션 시작 이벤트를 표시하는 이벤트 사용자 로그의 SDK 요청.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### 메시지가 반환되지 않는 경우 문제 해결 {#troubleshoot-messages-not-being-returned}

인앱 메시지가 반환되지 않는 경우, Campaign 타겟팅 문제가 발생하고 있을 수 있습니다.

- Segment에 사용자가 포함되어 있지 않습니다.
  - 사용자의 [**인게이지먼트**]({{ site.baseurl }}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) 탭에서 **Segments** 아래에 올바른 Segment가 표시되는지 확인하세요.
- 사용자가 이전에 인앱 메시지를 받았으며 다시 받을 자격이 없습니다.
  - **Campaign Composer**의 **Delivery** 단계에서 [Campaign 재자격 설정]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/)을 확인하고, 재자격 설정이 테스트 설정과 일치하는지 확인하세요.
- 사용자가 Campaign의 빈도 제한에 도달했습니다.
  - Campaign [빈도 제한 설정]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)을 확인하고 테스트 설정과 일치하는지 확인하세요.
- Campaign에 대조군이 있는 경우, 사용자가 대조군에 배정되었을 수 있습니다.
  - 수신된 캠페인 배리언트 필터가 포함된 Segment를 생성하고, 캠페인 배리언트를 **Control**로 설정한 다음, 사용자가 해당 Segment에 포함되는지 확인하여 이 상황이 발생했는지 확인할 수 있습니다.
  - 통합 테스트 목적으로 Campaign을 생성할 때는 대조군 추가를 선택 해제하세요.

### 인앱 메시지 표시 {#troubleshooting-in-app-message-display}

앱이 인앱 메시지를 성공적으로 요청하고 수신하고 있지만 표시되지 않는 경우, 기기 측 로직이 표시를 방해하고 있을 수 있습니다.

- 트리거된 인앱 메시지는 [트리거 간 최소 시간 간격]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/in-app_message_delivery#minimum-time-interval-between-triggers)에 따라 속도가 제한되며, 기본값은 30초입니다.
- 인앱 메시지 처리를 커스터마이즈하기 위해 델리게이트를 설정한 경우, 델리게이트가 인앱 메시지 표시에 영향을 주고 있지 않은지 확인하세요.
- 이미지 다운로드에 실패하면 이미지가 포함된 인앱 메시지가 표시되지 않습니다. `SDWebImage` 프레임워크가 올바르게 통합되지 않은 경우 이미지 다운로드는 항상 실패합니다. 기기 로그를 확인하여 이미지 다운로드가 실패하고 있지 않은지 확인하세요.
- 기기 방향이 인앱 메시지에 지정된 방향과 일치하지 않으면 인앱 메시지가 표시되지 않습니다. 기기가 올바른 방향인지 확인하세요.