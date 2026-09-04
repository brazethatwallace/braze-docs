---
nav_title: TV 및 OTT
article_title: Braze를 위한 TV 및 OTT 통합
page_order: 15

description: "이 문서에서는 Braze TV 및 OTT 기능, 통합, 사용 가능한 플랫폼 및 기타 기능에 대해 자세히 설명합니다."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# TV 및 OTT 통합 {#tv-and-ott-integrations}

> 기술이 새로운 플랫폼과 기기로 발전함에 따라 Braze를 사용한 메시징도 함께 발전할 수 있습니다! Braze는 다양한 TV 운영 체제 및 OTT(Over-the-Top) 콘텐츠 전달 방법을 위한 여러 인게이지먼트 채널을 제공합니다.

## 플랫폼 및 기능 {#platforms-and-features}

다음 표는 주요 TV 및 OTT 플랫폼의 메시징 채널 지원 현황을 요약합니다. 모든 플랫폼은 데이터 및 분석, Canvas, Feature Flags도 지원합니다. Kindle Fire의 경우 Amazon Fire TV와 동일한 안내를 참고하세요. Apple Vision Pro의 경우 [visionOS 지원]({{site.baseurl}}/developer_guide/platforms/swift/visionos)을 참조하세요.

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center;
    vertical-align: middle;
    word-break: normal;
    overflow-wrap: normal;
    hyphens: none;
}

#tv-feature-table td:first-child,
#tv-feature-table th:first-child {
    text-align: left;
}

</style>
<table aria-label="TV 및 OTT 메시징 채널 지원" id="tv-feature-table">
  <caption>TV 및 OTT 메시징 채널 지원</caption>
    <thead>
        <tr>
            <th>기기 유형</th>
            <th>SDK</th>
            <th>인앱 메시지</th>
            <th>Content Cards</th>
            <th>푸시 알림</th>
            <th>배너</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td><a href="https://github.com/braze-inc/braze-vega-sdk">Vega SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">지원됨</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">지원됨</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">지원됨</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td><a href="https://github.com/braze-inc/braze-android-sdk">Android SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">지원됨</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">지원됨</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">지원됨</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">OTT 플랫폼 미지원</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">OTT 플랫폼 미지원</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td><a href="https://github.com/braze-inc/braze-roku-sdk">Roku SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Braze 미지원</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">OTT 플랫폼 미지원</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Braze 미지원</span></td>
        </tr>
        <tr>
            <td>Apple TV OS (tvOS)</td>
            <td><a href="https://github.com/braze-inc/braze-swift-sdk">Swift SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">Braze 미지원</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">헤드리스만 지원</span></td>
        </tr>
    </tbody>
</table>

- <span aria-hidden="true">✅</span> = 지원됨
- <span aria-hidden="true">🔧</span> = 헤드리스만 지원 (커스텀 UI를 직접 구축해야 합니다)
- <span aria-hidden="true">➖</span> = OTT 플랫폼에서 미지원
- <span aria-hidden="true">❌</span> = Braze에서 미지원

## 통합 가이드 {#integration-guides}

### Amazon Fire TV {#fire-tv}

Braze Fire OS SDK를 사용하여 Amazon Fire TV 기기와 통합합니다.

기능들:

- 크로스채널 인게이지먼트를 위한 데이터 및 분석 수집
- 푸시 알림(["헤드업 알림"](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup)이라고도 함)
  - 이 알림이 표시되려면 우선순위를 "HIGH"로 설정해야 합니다. 모든 알림은 Fire TV 설정 메뉴에 나타납니다.
- Content Cards
- 기능 플래그
- 인앱 메시지
  - TV와 같은 비터치 환경에서 HTML 메시지를 표시하려면 `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages`를 `false`로 설정합니다([Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310)부터 사용 가능)
- 배너
  - [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)를 사용하여 Fire TV 앱에 직접 메시지를 임베드합니다.

자세한 내용은 [Fire OS 통합 가이드]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android)를 참조하세요.

### Kindle Fire {#kindle-fire}

Braze Fire OS SDK를 사용하여 Amazon Kindle Fire 기기와 통합합니다.

기능들:

- 크로스채널 인게이지먼트를 위한 데이터 및 분석 수집
- 푸시 알림
- Content Cards
- 기능 플래그
- 인앱 메시지
- 배너
  - [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)를 사용하여 Kindle Fire에 직접 메시지를 임베드합니다.

자세한 내용은 [Fire OS 통합 가이드]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android)를 참조하세요.

### Android TV {#android-tv}

Braze Android SDK를 사용하여 Android TV 기기와 통합합니다.

기능들:

- 크로스채널 인게이지먼트를 위한 데이터 및 분석 수집
- Content Cards
- 기능 플래그
- 인앱 메시지
  - TV와 같은 비터치 환경에서 HTML 메시지를 표시하려면 `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages`를 `false`로 설정합니다([Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310)부터 사용 가능)
- &#42; 푸시 알림(수동 통합 필요)
  - 푸시 알림은 Android TV에서 기본적으로 지원되지 않습니다. 그 이유를 알아보려면 Google의 [디자인 가이드라인](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html)을 참조하세요. 다만, **푸시 알림 UI를 수동으로 통합하여 이를 구현할 수 있습니다**. 설정 방법은 [설명서]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android%20tv)를 참조하세요.
- 배너
  - [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)를 사용하여 Android TV 앱에 직접 메시지를 임베드합니다.

자세한 내용은 [Android SDK 통합 가이드]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android)를 참조하세요.

{% alert note %}
Android OTT 통합을 위해 대시보드에서 새 Android 앱을 생성해야 합니다.
{% endalert %}

### LG webOS {#lg-webos}

Braze 웹 SDK를 사용하여 [LG webOS TV](https://webostv.developer.lge.com/discover)와 통합합니다.

기능들:

- 크로스채널 인게이지먼트를 위한 데이터 및 분석 수집
- Content Cards([헤드리스 UI](#custom-ui)를 통해)
- 기능 플래그
- 인앱 메시지([헤드리스 UI](#custom-ui)를 통해)
- 배너
  - [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)를 사용하여 webOS 앱에 직접 메시지를 임베드합니다.

자세한 내용은 [웹 스마트 TV 통합 가이드]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs)를 참조하세요.

### Samsung Tizen {#tizen}

Braze 웹 SDK를 사용하여 [Samsung Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html)와 통합합니다.

기능들:

- 크로스채널 인게이지먼트를 위한 데이터 및 분석 수집
- Content Cards([헤드리스 UI](#custom-ui)를 통해)
- 기능 플래그
- 인앱 메시지([헤드리스 UI](#custom-ui)를 통해)
- 배너
  - [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)를 사용하여 Tizen 앱에 직접 메시지를 임베드합니다.

자세한 내용은 [웹 스마트 TV 통합 가이드]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs)를 참조하세요.

### Roku {#roku}

Braze Roku SDK를 사용하여 [Roku TV](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)와 통합합니다.

기능들:

- 크로스채널 인게이지먼트를 위한 데이터 및 분석 수집
- 인앱 메시지([헤드리스 UI](#custom-ui)를 통해)
  - 웹뷰는 Roku 플랫폼에서 지원되지 않으므로 HTML 인앱 메시지도 지원되지 않습니다.
- 기능 플래그

자세한 내용은 [Roku 통합 가이드]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=roku)를 참조하세요.

### Apple TV OS {#tvos}

Braze Swift SDK를 사용하여 tvOS와 통합합니다. Swift SDK에는 tvOS용 기본 UI나 뷰가 포함되어 있지 않으므로 직접 구현해야 합니다.

기능들:

- 크로스채널 인게이지먼트를 위한 데이터 및 분석 수집
- Content Cards([헤드리스 UI](#custom-ui)를 통해)
- 기능 플래그
- 인앱 메시지([헤드리스 UI](#custom-ui)를 통해)
  - 웹뷰는 tvOS 플랫폼에서 지원되지 않으므로 HTML 인앱 메시지도 지원되지 않습니다.
  - tvOS에서 커스터마이즈된 메시징을 위해 헤드리스 UI를 사용하는 방법에 대해 자세히 알아보려면 [샘플 앱](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)을 참조하세요.
- 사일런트 푸시 알림 및 배지 업데이트
- 배너
  - [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)를 사용하여 tvOS 앱에 직접 메시지를 임베드합니다.

자세한 내용은 [iOS Swift SDK 통합 가이드](https://github.com/braze-inc/braze-swift-sdk)를 참조하세요.

{% alert note %}
TV 사용자에게 모바일 인앱 메시지가 표시되지 않도록 하려면 [앱 타겟팅](#app-targeting)을 설정하거나 키-값 페어를 사용하여 메시지를 필터링하세요. 예를 들어, 특별한 `tv = true` 키-값 페어가 포함된 경우에만 tvOS 메시지를 표시할 수 있습니다.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Braze Swift SDK를 사용하여 visionOS와 통합합니다. iOS에서 사용 가능한 대부분의 기능은 visionOS에서도 사용할 수 있으며, 다음을 포함합니다:

- 분석(세션, 커스텀 이벤트, 구매 등)
- In-App Messages(데이터 모델 및 UI)
- Content Cards(데이터 모델 및 UI)
- 푸시 알림(실행 버튼 및 사일런트 알림이 포함된 사용자 표시 알림)
- 기능 플래그
- 위치 분석
- 배너
  - [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)를 사용하여 visionOS 앱에 직접 메시지를 임베드합니다.

자세한 내용은 [iOS Swift SDK 통합 가이드](https://github.com/braze-inc/braze-swift-sdk)를 참조하세요.

{% alert important %}
일부 iOS 기능은 부분적으로 지원되거나 지원되지 않습니다. 전체 목록은 [visionOS 지원]({{site.baseurl}}/developer_guide/platforms/swift/visionos)을 참조하세요.
{% endalert %}

## 앱 타겟팅 {#app-targeting}

메시징을 위해 OTT 앱을 타겟팅하려면 OTT 앱 전용 세그먼트를 생성하는 것이 좋습니다.

![Android OTT 앱을 사용하여 생성한 세그먼트.]({% image_buster /assets/img/android_ott.png %})

## 헤드리스 UI {#custom-ui}

{% alert important %}
헤드리스 UI를 통해 인앱 메시지 또는 Content Cards를 지원하는 플랫폼에는 기본 UI나 뷰가 포함되어 있지 **않습니다**. 커스텀 UI(예: 인앱 메시지용)를 직접 구축한 다음 SDK에서 제공하는 데이터 모델을 사용하여 해당 UI를 채우세요.
{% endalert %}

헤드리스 UI를 사용하면 Braze는 앱이 제어하는 UI 내에서 앱이 읽고 사용할 수 있는 JSON과 같은 데이터 모델을 전달합니다. 이 데이터에는 대시보드에서 구성한 필드(제목, 본문, 버튼 텍스트, 색상 등)가 포함되며, 앱이 이를 읽고 적절히 표시할 수 있습니다. 커스텀 메시지 처리에 대한 자세한 내용은 다음을 참조하세요.

**Android SDK**
- [인앱 메시지 커스터마이징]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android#android_setting-custom-manager-listeners)
- [Content Cards 커스터마이징]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)

**Swift SDK**
- [인앱 메시지 커스터마이징](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [헤드리스 UI 샘플 앱](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Content Cards 커스터마이징](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**웹 SDK**
- [인앱 메시지 커스터마이징]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web)
- [Content Cards 커스터마이징]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)