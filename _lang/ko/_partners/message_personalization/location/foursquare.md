---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "이 참고 문서에서는 위치를 기반으로 실시간 이벤트 트리거를 제공하는 Braze와 위치 데이터 플랫폼인 Foursquare의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/)는 Braze Campaigns에서 위치 데이터 타겟팅을 제공하는 위치 데이터 플랫폼입니다. iOS 및 Android 앱에서 Foursquare의 Pilgrim SDK를 사용하여 위치를 기반으로 실시간 이벤트 트리거를 제공하면, Foursquare의 강력한 지리적 타겟팅 기능을 활용하여 Braze에서 관련성 높은 개인화된 메시징을 전송할 수 있습니다.

_이 통합은 Foursquare에서 유지 관리합니다._

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Foursquare 계정 | 이 파트너십을 활용하려면 Foursquare 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 워크스페이스 및 앱 ID | Braze 워크스페이스 및 앱 ID는 [개발자 콘솔]({{site.baseurl}}/api/basics)에서 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

두 플랫폼을 통합하려면 두 SDK를 통합하고 일치하는 사용자 필드를 매핑해야 합니다. Pilgrim SDK를 통합하면 기기 또는 웹훅을 통해 위치 이벤트를 수신하게 됩니다.

### 1단계: 사용자 ID 필드 매핑 {#step-1-map-user-id-fields}

두 SDK 간의 필드를 올바르게 매핑하려면 Braze SDK의 [`changeUser` 메서드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#setting-user-ids)와 Pilgrim SDK의 [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data)에 있는 `setUserId` 메서드를 사용하여 두 시스템에서 동일한 사용자 ID를 설정합니다.

### 2단계: Pilgrim 콘솔 구성 {#step-2-configure-pilgrim-console}
![그룹 ID, Android 앱 ID, iOS 앱 ID를 입력하도록 요청하는 Pilgrim 콘솔 이미지]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Braze 개발자 콘솔에서 워크스페이스 및 앱 ID를 찾습니다. 그런 다음 Braze REST API 키와 앱 ID를 Foursquare Pilgrim 콘솔에 입력합니다.

Pilgrim 콘솔을 구성하면 Pilgrim SDK가 위치 이벤트를 기록하고 Braze로 전달하므로, 자격을 갖춘 고객을 리타겟팅하고 세분화할 수 있습니다. 자세한 내용은 [Foursquare 개발자 사이트](https://developer.foursquare.com/)를 참조하세요.

{% alert important %}
Pilgrim SDK를 사용하려면 위치 서비스를 활성화해야 합니다.
{% endalert %}

## 메시지 트리거 {#triggering-messages}

통합이 설정되면, Pilgrim SDK에서 생성된 위치 이벤트를 기반으로 동작하는 Campaign 또는 Canvas를 설정할 수 있습니다. 이 통합 경로는 사용자가 관심 장소에 입장한 직후의 실시간 메시징이나, 감사 메시지 또는 리마인더와 같이 장소를 떠난 후의 지연 후속 커뮤니케이션에 이상적입니다.

설정된 위치를 기반으로 메시지를 보내는 Campaign을 전송하려면:
- **실행 기반 전달**로 전송하는 Braze Campaign 또는 Canvas를 생성합니다.
- 트리거로 `arrival` 커스텀 이벤트를 사용하고, 다음 스크린샷과 같이 `locationType`에 대한 이벤트 속성정보 필터를 설정합니다.

![전달 단계에서 "커스텀 이벤트 수행" 옵션으로 "arrival"이 선택되고, "locationType"이 "home"과 같음으로 설정된 실행 기반 Campaign.]({% image_buster /assets/img_archive/action-based-campaign.png %})

## 리타겟팅 {#retargeting}

사용자를 리타겟팅하려면 Pilgrim SDK를 사용하여 Braze 사용자의 고객 프로필에 `last_location` 커스텀 속성을 설정하세요. 그런 다음 `matches regex` 비교를 사용하여 실제 세계에서 특정 위치를 방문한 사용자를 리타겟할 수 있습니다. 예를 들어, 최근에 피자 가게를 방문한 모든 사용자를 세분화할 수 있습니다.

![실행 기반 Campaign의 타겟 사용자 단계에서 "last_location"이 "Pizza Place"와 같다고 표시된 화면]({% image_buster /assets/img_archive/last-location-segment.png %})

또한 Foursquare의 `primaryCategoryId`를 기반으로 특정 시간 범위 내에 특정 유형의 장소를 방문한 사용자를 Braze에서 세분화할 수도 있습니다. 리타겟팅 사용 사례에 이 데이터 포인트를 활용하려면 오디언스 세분화 과정에서 `primaryCategoryId`를 이벤트 속성정보로 기록하세요. Foursquare API 및 Pilgrim SDK에서 사용하는 사용자와 속성정보를 확인하려면 [Foursquare 개발자 사이트](https://developer.foursquare.com/)를 참조하세요.