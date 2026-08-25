---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 Segment와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment](https://segment.com)는 고객 데이터를 수집, 정리 및 활성화하는 데 도움이 되는 고객 데이터 플랫폼입니다.

Braze와 Segment 통합을 통해 사용자를 추적하고 다양한 사용자 분석 제공업체로 데이터를 라우팅할 수 있습니다. Segment를 사용하면 다음을 수행할 수 있습니다:

- [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage)를 Braze에 동기화하여 Braze Campaign 및 Canvas 세분화에 활용합니다.
- [두 플랫폼 간에 데이터를 가져옵니다](#integration-options). Android, iOS 및 웹 애플리케이션을 위한 병렬 SDK 통합과 Braze REST API로 데이터를 동기화하는 서버 간 통합을 제공합니다.
- [Currents를 통해 Segment에 데이터를 연결합니다]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents).

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Segment 계정 | 이 파트너십을 활용하려면 [Segment 계정](https://app.segment.com/login)이 필요합니다. |
| 설치된 소스 및 Segment 소스 [라이브러리](https://segment.com/docs/sources/) | 모바일 앱, 웹사이트 또는 백엔드 서버 등 Segment로 전송되는 모든 데이터의 출처입니다.<br><br>성공적인 `Source > Destination` 흐름을 설정하려면 먼저 앱, 사이트 또는 서버에 라이브러리를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Braze와 Segment를 통합하려면 [선택한 통합 유형](#integration-options)(연결 모드)에 따라 [Braze를 대상으로 설정](#connection-settings)해야 합니다. Braze를 처음 사용하는 고객인 경우 [Segment 리플레이](#segment-replays)를 사용하여 과거 데이터를 Braze에 전달할 수 있습니다. 그런 다음 [매핑](#methods)을 설정하고 [통합을 테스트](#step-4-test-your-integration)하여 Braze와 Segment 간의 원활한 데이터 흐름을 보장해야 합니다.

### 1단계: Braze 대상 생성 {#connection-settings}

소스를 성공적으로 설정한 후 각 소스(iOS, Android, 웹 등)에 대해 Braze를 [대상](https://segment.com/docs/destinations/)으로 구성해야 합니다. 연결 설정을 사용하여 Braze와 Segment 간의 데이터 흐름을 커스터마이즈할 수 있는 다양한 옵션이 있습니다.

### 2단계: 대상 프레임워크 및 연결 유형 선택 {#integration-options}

Segment에서 **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**으로 이동합니다.

![소스 설정 페이지. 이 페이지에는 대상 프레임워크를 'actions' 또는 'classic'으로 설정하고 연결 모드를 'cloud mode' 또는 'device mode'로 설정하는 설정이 포함되어 있습니다.]({% image_buster /assets/img/segment/setup.png %})

Segment의 웹 소스(Analytics.js)와 네이티브 클라이언트 측 라이브러리를 병렬(디바이스 모드) 통합 또는 서버 간(클라우드 모드) 통합을 사용하여 Braze와 통합할 수 있습니다.

연결 모드의 선택은 대상이 구성된 소스 유형에 따라 결정됩니다.

| 통합 | 상세 내용 |
| ----------- | ------- |
| [병렬<br>(디바이스 모드)](#side-by-side-sdk-integration) | Segment의 SDK를 사용하여 이벤트를 Braze 네이티브 호출로 변환하여, 서버 간 통합보다 더 심층적인 기능과 더 포괄적인 Braze 활용을 가능하게 합니다.<br><br>Segment가 모든 Braze 메서드(예: Content Cards)를 지원하지는 않습니다. 해당 매핑을 통해 매핑되지 않은 Braze 메서드를 사용하려면 코드베이스에 네이티브 Braze 코드를 추가하여 해당 메서드를 호출해야 합니다. |
| [서버 간<br>(클라우드 모드)](#server-to-server-integration) | Segment에서 Braze REST API 엔드포인트로 데이터를 전달합니다.<br><br>인앱 메시지, Content Cards 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다. 또한 이 방법으로는 기기 수준 필드와 같은 자동으로 캡처되는 데이터를 사용할 수 없습니다.<br><br>이러한 기능을 사용하려면 병렬 통합을 고려하세요.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 대상 프레임워크 및 연결 유형 선택" }

{% alert note %}
두 가지 통합 옵션(연결 모드)과 각각의 이점에 대해 자세히 알아보려면 [Segment](https://segment.com/docs/destinations/#connection-modes)를 방문하세요.
{% endalert %}

#### 병렬 SDK 통합 {#side-by-side-sdk-integration}

디바이스 모드라고도 하는 이 통합은 Segment의 SDK와 [메서드](#methods)를 Braze SDK에 매핑하여 푸시, 인앱 메시지 및 Braze 고유의 기타 메서드와 같은 SDK가 제공하는 모든 기능에 접근할 수 있게 합니다.

{% alert note %}
Segment의 디바이스 모드를 사용할 때는 Segment가 Braze를 초기화하도록 하세요. 앱에서 Braze SDK를 별도로 초기화하지 마세요. 대상 플러그인이 Braze를 구성하고 세션을 시작하므로, 두 번째 네이티브 init은 중복 세션을 기록할 수 있습니다. Segment `identify`를 사용하여 사용자 ID를 설정하세요. 플러그인은 해당 호출을 `changeUser()`에 매핑합니다.
{% endalert %}

{% alert important %}
모바일에서의 디바이스 모드 통합의 경우, Segment 대시보드에서 대상을 구성하는 것 외에도 앱에 Braze 대상 플러그인을 추가해야 합니다. Segment SDK는 기본적으로 Braze 플러그인을 포함하지 않으며, 이 플러그인이 없으면 Segment SDK가 Braze로 데이터나 매핑된 메서드 호출을 전달할 수 없고, 푸시, 인앱 메시지, Content Cards와 같은 기능이 작동하지 않습니다. 설치 지침은 이 섹션의 플랫폼별 탭을 참조하세요.
{% endalert %}

디바이스 모드 연결을 사용하면 Braze SDK를 네이티브로 통합하는 것과 마찬가지로, Braze SDK가 모든 사용자에게 `device_id`와 백엔드 식별자인 `braze_id`를 할당합니다. 이를 통해 Braze는 `userId` 대신 이러한 식별자를 매칭하여 기기의 익명 활동을 캡처할 수 있습니다.

{% alert note %}
디바이스 모드(Kotlin 또는 Swift) 대상에서 [대상 필터](https://segment.com/docs/connections/destinations/destination-filters/)를 사용하는 경우 필터 지원이 활성화된 상태로 대상 플러그인을 구성해야 합니다. 지원되는 플러그인 버전에 대한 자세한 내용은 Segment의 [대상 필터 설명서](https://segment.com/docs/connections/destinations/destination-filters/)를 참조하세요.
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
Android 디바이스 모드 통합의 소스 코드는 Braze에서 유지 관리하며 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

<br>
사용할 Braze SDK는 어떤 Segment SDK를 사용하느냐에 따라 달라집니다:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| 권장 | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| 레거시 | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="병렬 SDK 통합" }


{% endalert %}

Braze를 Android 소스의 디바이스 모드 대상으로 설정하려면 **Destination framework**로 **Actions**를 선택한 다음 **Save**를 선택하세요.

병렬 통합을 완료하려면 Android 앱에 [Braze Kotlin 대상 플러그인](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/)을 추가해야 합니다. 이 플러그인은 Segment SDK와 Braze SDK를 연결하여 디바이스 모드 데이터가 Braze로 전달되도록 합니다. Segment 설치 지침에 따라 플러그인 의존성을 추가하고 Segment 분석 인스턴스로 초기화하세요.

[Android 디바이스 모드](https://github.com/braze-inc/braze-segment-kotlin) 통합의 소스 코드는 Braze에서 유지 관리하며 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

{% endtab %}
{% tab iOS %}

{% alert important %}
iOS 디바이스 모드 통합의 소스 코드는 Braze에서 유지 관리하며 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

<br>
사용할 Braze SDK는 어떤 Segment SDK를 사용하느냐에 따라 달라집니다:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| 권장 | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| 레거시 | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="병렬 SDK 통합" }
{% endalert %}

Braze를 iOS 소스의 디바이스 모드 대상으로 설정하려면 **Destination framework**로 **Actions**를 선택한 다음 **Save**를 선택하세요.

병렬 통합을 완료하려면 iOS 앱에 [Braze Swift 대상 플러그인](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/)을 추가해야 합니다. 이 플러그인은 Segment SDK와 Braze SDK를 연결하여 디바이스 모드 데이터가 Braze로 전달되도록 합니다. Segment 설치 지침에 따라 플러그인 의존성(스위프트 패키지 매니저 또는 CocoaPods 사용)을 추가하고 Segment 분석 인스턴스로 초기화하세요.

[iOS 디바이스 모드](https://github.com/braze-inc/braze-segment-swift) 통합의 소스 코드는 Braze에서 유지 관리하며 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

{% endtab %}
{% tab 웹 또는 JavaScript %}

Segment의 Braze 웹 모드(Actions) 프레임워크는 웹 소스에 대해 Braze를 디바이스 모드 대상으로 설정하는 데 권장됩니다.

Segment에서 대상 프레임워크로 **Actions**를 선택하고 연결 모드로 **Device Mode**를 선택하세요.

![Actions 프레임워크와 Device Mode가 선택된 Segment 대상 설정.]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
[React Native Braze 플러그인](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze)의 소스 코드는 Segment에서 유지 관리하며 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

React Native Segment 소스를 Braze에 연결할 때 운영 체제별로 소스와 대상을 설정해야 합니다. 예를 들어 iOS 대상과 Android 대상을 설정해야 합니다.

앱 코드베이스 내에서 각 앱과 관련된 소스 쓰기 키를 사용하여 기기 유형별로 조건부로 Segment SDK를 초기화합니다.

기기에서 푸시 토큰이 등록되어 Braze로 전송되면 SDK 초기화 시 사용된 앱 식별자와 연결됩니다. 기기 유형 조건부 초기화는 Braze로 전송되는 모든 푸시 토큰이 관련 앱과 연결되도록 확인하는 데 도움이 됩니다.

{% alert important %}
React Native 앱이 모든 기기에 대해 동일한 Braze 앱 식별자로 Braze를 초기화하면 모든 React Native 사용자가 Braze에서 Android 또는 iOS 사용자로 간주되며 모든 푸시 토큰이 해당 운영 체제와 연결됩니다.
{% endalert %}

각 소스에 대해 Braze를 디바이스 모드 대상으로 설정하려면 **Destination framework**로 **Actions**를 선택한 다음 **Save**를 선택하세요.

{% endtab %}
{% endtabs %}

#### 서버 간 통합 {#server-to-server-integration}

클라우드 모드라고도 하는 이 통합은 Segment에서 Braze REST API로 데이터를 전달합니다. Segment의 [Braze 클라우드 모드(Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) 프레임워크를 사용하여 모든 소스에 대한 클라우드 모드 대상을 설정하세요.

병렬 통합과 달리 서버 간 통합은 인앱 메시지, Content Cards 또는 자동 푸시 토큰 등록과 같은 Braze UI 기능을 지원하지 않습니다. 또한 클라우드 모드에서는 [자동으로 캡처되는]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection#user-data-collection) 데이터(익명 사용자 및 기기 수준 필드 등)를 사용할 수 없습니다.

이 데이터와 기능을 사용하려면 병렬(디바이스 모드) SDK 통합을 사용하는 것을 고려하세요.

[Braze 클라우드 모드(Actions) 대상](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze)의 소스 코드는 Segment에서 유지 관리합니다.

### 3단계: 설정 {#step-3-settings}

대상에 대한 설정을 정의합니다. 모든 설정이 모든 대상 유형에 적용되는 것은 아닙니다.

{% tabs local %}
{% tab 모바일 디바이스 모드 %}

| 설정 | 설명 |
| ------- | ----------- |
| 앱 식별자 | 특정 앱을 참조하는 데 사용되는 앱 식별자입니다. Braze 대시보드의 **설정 관리**에서 확인할 수 있습니다. |
| 커스텀 API 엔드포인트<br>(SDK 엔드포인트) | 인스턴스에 해당하는 Braze SDK 엔드포인트입니다(예: `sdk.iad-01.braze.com`). |
| 엔드포인트 리전 | Braze 인스턴스입니다(예: US 01, US 02, EU 01 등). |
| 자동 인앱 메시지 등록 활성화 | 인앱 메시지를 수동으로 등록하려면 이 옵션을 비활성화하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: 설정" }

{% endtab %}
{% tab 웹 디바이스 모드 %}

| 설정 | 설명 |
| ------- | ----------- |
| 앱 식별자 | 특정 앱을 참조하는 데 사용되는 앱 식별자입니다. Braze 대시보드의 **설정 관리**에서 확인할 수 있습니다. |
| 커스텀 API 엔드포인트<br>(SDK 엔드포인트) | 인스턴스에 해당하는 Braze SDK 엔드포인트입니다(예: `sdk.iad-01.braze.com`). |
| Safari 웹사이트 푸시 ID | Safari 푸시를 지원하는 경우 Safari 푸시 인증서를 생성할 때 Apple에 제공한 웹사이트 푸시 ID를 이 옵션에 지정해야 합니다(`web`으로 시작, 예: `web.com.example.domain`). |
| Braze 웹 SDK 버전 | 사용하려는 Braze 웹 SDK 버전입니다. |
| 인앱 메시지 자동 전송 | 기본적으로 사용자가 수신할 자격이 있는 모든 인앱 메시지가 자동으로 사용자에게 전달됩니다. 인앱 메시지를 수동으로 표시하려면 이 옵션을 비활성화하세요. |
| Font Awesome 로드하지 않기 | Braze는 인앱 메시지 아이콘에 Font Awesome를 사용합니다. 기본적으로 Braze는 FontAwesome CDN에서 FontAwesome를 자동으로 로드합니다. 이 동작을 비활성화하려면(예: 사이트에서 커스터마이즈된 버전의 FontAwesome을 사용하는 경우) 이 옵션을 `TRUE`로 설정하세요. 이렇게 하면 사이트에서 FontAwesome이 로드되도록 하는 것은 사용자의 책임이며, 그렇지 않으면 인앱 메시지가 올바르게 렌더링되지 않을 수 있습니다. |
| HTML 인앱 메시지 활성화 | 이 옵션을 활성화하면 Braze 대시보드 사용자가 HTML 인앱 메시지를 사용할 수 있습니다. |
| 새 탭에서 인앱 메시지 열기 | 기본적으로 인앱 메시지 클릭의 링크는 대시보드에서 메시지별로 지정한 대로 현재 탭 또는 새 탭에서 로드됩니다. 인앱 메시지 클릭의 모든 링크를 새 탭이나 창에서 열도록 강제하려면 이 옵션을 `TRUE`로 설정하세요. |
| 인앱 메시지 z-index | 이 옵션에 값을 제공하면 Braze 기본 z-index를 재정의합니다. |
| 인앱 메시지의 명시적 해제 요구 | 기본적으로 인앱 메시지가 표시되면 Escape 키를 누르거나 페이지의 회색 배경을 클릭하면 메시지가 해제됩니다. 이 동작을 방지하고 메시지를 해제하려면 명시적인 버튼 클릭이 필요하도록 하려면 이 옵션을 true로 설정하세요. |
| 트리거 동작 간 최소 간격(초) | 기본값: 30.<br>기본적으로 트리거 동작은 마지막 트리거 동작 이후 최소 30초가 경과한 경우에만 실행됩니다. 이 기본값을 자체 값으로 재정의하려면 이 구성 옵션에 값을 제공하세요. 사용자에게 알림 스팸을 보내지 않으려면 이 값을 10 미만으로 설정하지 않는 것이 좋습니다. |
| 서비스 종사자 위치 | 기본적으로 사용자를 웹 푸시 알림에 등록할 때 Braze는 웹 서버의 루트 디렉토리인 `/service-worker.js`에서 필요한 서비스 종사자 파일을 찾습니다. 서버의 다른 경로에서 서비스 종사자를 호스팅하려면 파일의 절대 경로를 이 옵션의 값으로 제공하세요(예: `/mycustompath/my-worker.js`). 여기에 값을 설정하면 사이트의 푸시 알림 범위가 제한됩니다. 예를 들어 이 예에서는 서비스 종사자 파일이 `/mycustompath/` 디렉토리 내에 있으므로 `requestPushPermission`은 `http://yoursite.com/mycustompath/`로 시작하는 웹 페이지에서만 호출할 수 있습니다. |
| 푸시 토큰 유지 비활성화 | 기본적으로 이미 웹 푸시 권한을 부여한 사용자는 새 세션에서 전달 가능성을 보장하기 위해 Braze 백엔드와 자동으로 푸시 토큰을 동기화합니다. 이 동작을 비활성화하려면 이 옵션을 `FALSE`로 설정하세요. |
| 서비스 종사자 외부 관리 | 등록하고 수명 주기를 제어하는 자체 서비스 종사자가 있는 경우 이 옵션을 `TRUE`로 설정하면 Braze SDK는 서비스 종사자를 등록하거나 등록 해제하지 않습니다. 이 옵션을 `TRUE`로 설정하는 경우 푸시가 올바르게 작동하려면 `requestPushPermission`을 호출하기 전에 서비스 종사자를 직접 등록하고 `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');`를 사용하거나 해당 파일의 내용을 직접 포함하여 Braze 서비스 종사자 코드가 포함되어 있는지 확인해야 합니다. 이 옵션이 `TRUE`이면 `serviceWorkerLocation` 옵션은 무관하며 무시됩니다. |
| 콘텐츠 보안 논스 | 이 옵션에 값을 제공하면 Braze SDK는 SDK에서 생성하는 모든 `<script>` 및 `<style>` 요소에 논스를 추가합니다. 이를 통해 Braze SDK가 웹사이트의 콘텐츠 보안 정책과 함께 작동할 수 있습니다. 이 논스를 설정하는 것 외에도 FontAwesome 로드를 허용해야 할 수 있으며, 이를 위해 콘텐츠 보안 정책 허용 목록에 `use.fontawesome.com`을 추가하거나 `doNotLoadFontAwesome` 옵션을 사용하고 수동으로 로드할 수 있습니다. |
| 크롤러 활동 허용 | 기본적으로 Braze 웹 SDK는 사용자 에이전트 문자열을 기반으로 Google과 같은 알려진 스파이더 또는 웹 크롤러의 활동을 무시합니다. 이렇게 하면 데이터 포인트가 절약되고 분석이 더 정확해지며 페이지 순위가 향상될 수 있습니다. 그러나 Braze가 이러한 크롤러의 활동을 대신 기록하도록 하려면 이 옵션을 `TRUE`로 설정할 수 있습니다. |
| 로깅 활성화 | 기본적으로 로깅을 활성화하려면 `TRUE`로 설정하세요. 이 경우 Braze는 모든 사용자에게 표시되는 JavaScript 콘솔에 로그를 기록합니다. 페이지를 프로덕션에 릴리스하기 전에 이를 제거하거나 `setLogger`를 사용하여 대체 로거를 제공해야 합니다. |
| 사용자 제공 JavaScript 허용 | 기본적으로 Braze 웹 SDK는 Braze 대시보드 사용자가 사이트에서 JavaScript를 실행할 수 있도록 허용하므로 사용자 제공 JavaScript 클릭 액션을 허용하지 않습니다. Braze 대시보드 사용자가 악의적이지 않은 JavaScript 클릭 액션을 작성한다고 신뢰한다면 이 속성을 `TRUE`로 설정하세요. `enableHtmlInAppMessages`가 `TRUE`이면 이 옵션도 `TRUE`로 설정됩니다. |
| 앱 버전 | 이 옵션에 값을 제공하면 Braze로 전송되는 사용자 이벤트가 주어진 버전과 연결되며 사용자 세분화에 사용할 수 있습니다. |
| 세션 타임아웃(초) | 기본값: 30.<br>기본적으로 세션은 30분 동안 비활성 상태이면 타임아웃됩니다. 이 기본값을 자체 값으로 재정의하려면 이 구성 옵션에 값을 제공하세요. |
| 기기 속성 허용 목록 | 기본적으로 Braze SDK는 `DeviceProperties`의 모든 기기 속성을 자동으로 감지하고 수집합니다. 이 동작을 재정의하려면 `DeviceProperties` 배열을 제공하세요. 일부 속성이 없으면 모든 기능이 제대로 작동하지 않을 수 있습니다. 예를 들어 시간대 없이는 로컬 시간대 전달이 작동하지 않습니다. |
| 현지화 | 기본적으로 SDK에서 생성한 모든 사용자 표시 메시지는 사용자의 브라우저 언어로 표시됩니다. 이 동작을 재정의하고 특정 언어를 강제하려면 이 옵션에 값을 제공하세요. 이 옵션의 값은 ISO 639-1 언어 코드여야 합니다. |
| 쿠키 없음 | 기본적으로 Braze SDK는 쿠키에 소량의 데이터(사용자 ID, 세션 ID)를 저장합니다. 이는 사이트의 다양한 하위 도메인에서 Braze가 사용자와 세션을 인식할 수 있도록 하기 위한 것입니다. 이것이 문제가 되는 경우 이 옵션에 `TRUE`를 전달하여 쿠키 저장을 비활성화하고 HTML 5 localStorage에 전적으로 의존하여 사용자와 세션을 식별하세요. |
| 모든 페이지 추적 | **클래식 대상 웹 디바이스 모드(유지 관리) 전용**<br><br>Segment는 이 설정을 [매핑을 통해 활성화](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)할 수 있는 웹 Actions 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>모든 [page 호출](https://segment.com/docs/spec/page/)을 "Loaded/Viewed a Page" 이벤트로 Braze에 전송합니다. |
| 이름이 지정된 페이지만 추적 | **클래식 대상 웹 디바이스 모드(유지 관리) 전용**<br><br>Segment는 이 설정을 [매핑을 통해 활성화](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)할 수 있는 웹 Actions 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>이름이 연결된 page 호출만 Braze에 전송합니다. |
| 매출이 있을 때 구매 기록 | **클래식 대상 웹 디바이스 모드(유지 관리) 전용**<br><br>Segment는 이 설정을 [매핑을 통해 활성화](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)할 수 있는 웹 Actions 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>이 옵션이 활성화되면 revenue 속성이 있는 모든 Track 호출이 구매 이벤트를 트리거합니다. |
| 알려진 사용자만 추적 | **클래식 대상 웹 디바이스 모드(유지 관리) 전용**<br><br>Segment는 매핑을 통해 이 설정을 활성화할 수 있는 웹 Actions 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>활성화하면 이 새 설정은 유효한 `userId`가 있을 때까지 `window.braze.initialize` 호출을 지연시킵니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: 설정" }

{% endtab %}
{% tab 클라우드 모드 %}

| 설정 | 설명 |
| ------- | ----------- |
| 앱 식별자 | 특정 앱을 참조하는 데 사용되는 앱 식별자입니다. Braze 대시보드의 **설정 관리**에서 확인할 수 있습니다. |
| REST API 키 | Braze 대시보드의 **설정** > **API 키**에서 확인할 수 있습니다. |
| 커스텀 REST API 엔드포인트 | 인스턴스에 해당하는 Braze REST 엔드포인트입니다(예: rest.iad-01.braze.com). |
| 기존 사용자만 업데이트 | **클래식 대상 클라우드 모드(유지 관리) 전용**<br><br>Segment는 이 설정을 [매핑을 통해 활성화](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)할 수 있는 클라우드 Actions 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>기존 사용자만 업데이트할지 여부를 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: 설정" }

{% endtab %}
{% endtabs %}

### 4단계: 메서드 매핑 {#methods}

Braze는 Segment의 [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) 및 [Track](https://segment.com/docs/spec/track/) 메서드를 지원합니다. 이러한 메서드 내에서 사용되는 식별자 유형은 데이터가 서버 간(클라우드 모드) 통합을 통해 전송되는지 또는 병렬(디바이스 모드) 통합을 통해 전송되는지에 따라 달라집니다. Braze 웹 모드 Actions 및 클라우드 모드 Actions 대상에서는 [Segment alias 호출](https://segment.com/docs/connections/spec/alias/)에 대한 매핑도 설정할 수 있습니다.

{% alert note %}
사용자 별칭이 Braze 클라우드 모드(Actions) 대상에서 식별자로 지원되지만, Segment의 alias 호출은 Braze 사용자 별칭과 직접적인 관련이 없다는 점에 유의하세요.
{% endalert %}

| 식별자 유형 | 지원되는 대상 |
| --------------- | --------------------- |
| `userId` (`external_id`) | 모두 |
| 익명 사용자 | 디바이스 모드 대상 |
| 사용자 별칭 | 클라우드 모드 대상 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="4단계: 메서드 매핑" }

클라우드 모드(Actions) 대상은 별칭 전용 사용자를 생성하거나 기존 `external_id` 프로필에 별칭을 추가하는 데 사용할 수 있는 [Create Alias 액션](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias)을 제공합니다. [Identify User 액션](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user)은 Create Alias 액션과 함께 사용하여 사용자에게 `external_id`가 사용 가능해진 후 별칭 전용 사용자를 `external_id`와 병합할 수 있습니다.

클라우드 모드에서 `braze_id`를 사용하여 익명 사용자 데이터를 전송하는 우회 방법을 구현할 수도 있습니다. 이를 위해서는 모든 Segment API 호출에 사용자의 `braze_id`를 수동으로 포함해야 합니다. 이 우회 방법의 설정에 대한 자세한 내용은 [Segment 설명서](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users)에서 확인할 수 있습니다.

Braze로 전송되는 대상 데이터는 클라우드 모드 Actions 내에서 일괄 처리할 수 있습니다. 배치 크기는 75개 이벤트로 제한되며 이러한 배치는 30초 동안 누적된 후 플러시됩니다. 요청 일괄 처리는 액션별로 수행됩니다. 예를 들어 Identify 호출(속성)은 하나의 요청으로 일괄 처리되고 Track 호출(커스텀 이벤트)은 두 번째 요청으로 일괄 처리됩니다. Braze는 이 기능을 활성화할 것을 권장합니다. 이렇게 하면 Segment에서 Braze로 전송되는 요청 수가 줄어들고, 대상이 Braze 사용량 제한에 도달하여 요청을 재시도하는 위험이 줄어듭니다.

Braze 대상 > **Mappings**로 이동하여 액션에 대한 일괄 처리를 활성화할 수 있습니다. 거기에서 매핑 옆의 점 3개 아이콘을 클릭하고 **Edit Mapping**을 선택합니다. **Select mappings** 섹션 하단으로 스크롤하여 **Batch Data to Braze**가 **Yes**로 설정되어 있는지 확인하세요.


{% tabs local %}
{% tab Identify %}
#### Identify

[Identify](https://segment.com/docs/spec/identify/) 호출을 사용하면 사용자를 동작에 연결하고 사용자에 대한 속성을 기록할 수 있습니다.

특정 Segment 특수 트레이트는 Braze의 표준 속성 프로필 필드에 매핑됩니다:

| Segment 특수 트레이트 | Braze 표준 속성 |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identify" }

`email_subscribe` 및 `push_subscribe`와 같은 기타 예약된 Braze 프로필 필드는 이러한 필드에 대한 Braze 명명 규칙을 사용하고 identify 호출 내에서 트레이트로 전달하여 보낼 수 있습니다.

##### 구독 그룹에 사용자 추가 {#adding-a-user-to-a-subscription-group}

트레이트 매개변수에서 다음 필드를 사용하여 지정된 구독 그룹에서 사용자를 구독하거나 구독을 취소할 수도 있습니다.

`braze_subscription_groups`라는 예약된 Braze 프로필 필드를 사용하며, 이 필드는 객체 배열과 연결할 수 있습니다. 배열의 각 객체에는 두 개의 예약된 키가 있어야 합니다:

1. `subscription_group_state`: 사용자가 특정 구독 그룹에 `"subscribed"` 또는 `"unsubscribed"` 상태인지를 나타냅니다.
2. `subscription_group_id`: 구독 그룹의 고유 ID를 나타냅니다. 이 ID는 Braze 대시보드의 **Subscription Group Management**에서 확인할 수 있습니다.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### 커스텀 속성 {#custom-attributes}

다른 모든 트레이트는 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)으로 기록됩니다.

| Segment 메서드 | Braze 메서드 | 예시 |
|---|---|---|
| 사용자 ID로 Identify | 외부 ID 설정 | Segment: `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| 예약된 트레이트로 Identify | 사용자 속성 설정 | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| 커스텀 트레이트로 Identify | 커스텀 속성 설정 | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| 사용자 ID 및 트레이트로 Identify | Segment: 외부 ID 및 속성 설정 | 위의 메서드를 결합합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="커스텀 속성" }

[웹 모드 Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) 및 [클라우드 모드 Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile) 대상에서는 사용자 프로필 업데이트 액션을 사용하여 이러한 매핑을 설정할 수 있습니다.

{% alert important %}
사용자 속성 데이터를 전달할 때 마지막 업데이트 이후 변경된 속성에 대한 값만 전달하는지 확인하세요. 이렇게 하면 불필요하게 데이터 포인트를 소모하지 않습니다. 클라이언트 측 소스의 경우 Segment의 오픈소스 [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) 도구를 사용하여 Segment의 중복 `identify()` 호출을 디바운싱하여 통합을 최적화하고 데이터 포인트 사용량을 제한할 수 있습니다.

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

이벤트를 추적하면 제공된 이름을 사용하여 해당 이벤트를 [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events)로 기록합니다.

Track 호출의 properties 객체 내에서 전송된 메타데이터는 연결된 이벤트의 커스텀 이벤트 속성정보로 Braze에 기록됩니다. 모든 [커스텀 이벤트 속성정보 데이터 유형]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)이 지원됩니다.

[웹 모드 Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) 및 [클라우드 모드 Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event) 대상에서는 Track Event 액션을 사용하여 이러한 매핑을 설정할 수 있습니다.

| Segment 메서드 | Braze 메서드 | 예시 |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events)로 기록됨. | Segment: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [속성정보가 있는 Track](https://segment.com/docs/spec/track/) | [이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)로 기록됨. | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [제품이 있는 Track](https://segment.com/docs/spec/track/) | [구매 이벤트]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)로 기록됨. | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### 주문 완료 {#order-completed}

Segment의 [이커머스 API](https://segment.com/docs/spec/ecommerce/v2/)에 설명된 형식을 사용하여 `Order Completed`라는 이름으로 이벤트를 추적하면 나열한 제품이 [구매]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data)로 기록됩니다.

[웹 모드 Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) 및 [클라우드 모드 Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase) 대상에서 Track Purchase 액션을 통해 기본 매핑을 커스터마이즈할 수 있습니다.

{% endtab %}

{% tab Page %}
#### Page {#page}

[Page](https://segment.com/docs/spec/page/) 호출을 사용하면 사용자가 웹사이트의 페이지를 볼 때마다 해당 페이지에 대한 선택적 속성정보와 함께 기록할 수 있습니다.

이 이벤트 유형은 웹 모드 Actions 및 클라우드 Actions 대상에서 Braze에 커스텀 이벤트를 기록하는 트리거로 사용할 수 있습니다.
{% endtab %}

{% endtabs %}

### 5단계: 통합 테스트 {#step-5-test-your-integration}

병렬(디바이스 모드) 통합을 사용할 때 [개요]({{site.baseurl}}/user_guide/analytics/dashboards/home) 측정기준(전체 세션, MAU, DAU, 사용자 고착도, 일일 세션 및 MAU당 일일 세션)을 사용하여 Braze가 Segment에서 데이터를 수신하고 있는지 확인할 수 있습니다.

[커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data#custom-event-data) 또는 [매출]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) 페이지에서 데이터를 보거나 [Segment를 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment)하여 데이터를 확인할 수 있습니다. 대시보드의 **커스텀 이벤트** 페이지에서 시간 경과에 따른 커스텀 이벤트 횟수를 확인할 수 있습니다. 서버 간(클라우드 모드) 통합을 사용할 때는 MAU 및 DAU 통계를 포함하는 [수식]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula#creating-a-formula)을 사용할 수 없습니다.

구매 데이터를 Braze에 전송하는 경우([3단계](#methods)의 **Track** 탭에서 주문 완료 참조) [매출]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) 페이지에서 특정 기간의 매출 또는 구매 데이터나 앱의 전체 매출을 확인할 수 있습니다.

[Segment 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment)을 사용하면 커스텀 이벤트 및 속성 데이터를 기반으로 사용자를 필터링할 수 있습니다.

{% alert important %}
서버 간 통합(클라우드 모드)을 사용하는 경우 자동으로 수집된 세션 데이터와 관련된 필터(예: "처음 앱을 사용한 날" 및 "마지막으로 앱을 사용한 날")가 작동하지 않습니다. Segment 및 Braze 통합에서 이러한 기능을 사용하려면 병렬 통합(디바이스 모드)을 사용하세요.
{% endalert %}

## 사용자 삭제 및 억제 {#user-deletion-and-suppression}

사용자를 삭제하거나 억제해야 하는 경우, [Segment의 사용자 삭제 기능](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to)이 Braze [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)에 매핑**되어 있다**는 점에 유의하세요. 이러한 삭제의 확인에는 최대 30일이 소요될 수 있습니다.

Braze와 Segment 간에 공통 사용자 식별자(`external_id` 등)를 선택해야 합니다. Segment에서 삭제 요청을 시작한 후에는 Segment 대시보드의 삭제 요청 탭에서 상태를 확인할 수 있습니다.

## Segment 리플레이 {#segment-replays}

Segment는 클라이언트에게 모든 과거 데이터를 새로운 기술 파트너에게 "리플레이"하는 서비스를 제공합니다. 모든 관련 과거 데이터를 가져오고자 하는 신규 Braze 고객은 Segment를 통해 이를 수행할 수 있습니다. 관심이 있으시면 Segment 담당자에게 문의하세요.

Segment는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)에 연결하여 사용자 데이터를 대신 Braze로 가져옵니다.

{% alert important %}
클라우드 모드 액션 대상에서 지원되는 모든 식별자는 Segment 리플레이의 일부로 지원됩니다.
{% endalert %}

## 모범 사례 {#best-practices}

{% details 데이터 초과를 방지하기 위해 사용 사례를 검토하세요. %}

Segment는 클라이언트가 전송하는 데이터 요소의 수를 제한하지 **않습니다**. Segment를 사용하면 모든 이벤트를 전송하거나 Braze로 보낼 이벤트를 선택할 수 있습니다. Segment를 사용하여 모든 이벤트를 전송하는 대신, 마케팅 및 편집 팀과 함께 사용 사례를 검토하여 데이터 초과를 방지하기 위해 Braze로 보낼 이벤트를 결정하는 것을 권장합니다.

{% enddetails %}

{% details 모바일 기기 모드 대상 설정에서 커스텀 API 엔드포인트와 커스텀 REST API 엔드포인트의 차이를 이해하세요. %}

| Braze 용어 | Segment 대응 용어 |
| ----------------- | ------------------ |
| Braze SDK 엔드포인트 | 커스텀 API 엔드포인트 |
| Braze REST 엔드포인트 | 커스텀 REST API 엔드포인트 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="모범 사례" }

Braze API 엔드포인트(Segment에서 "커스텀 API 엔드포인트"라고 불림)는 Braze가 SDK를 위해 설정하는 SDK 엔드포인트입니다(예: `sdk.iad-03.braze.com`). Braze REST API 엔드포인트(Segment에서 "커스텀 REST API 엔드포인트"라고 불림)는 REST API 엔드포인트입니다(예: `https://rest.iad-03.braze.com`).
{% enddetails %}

{% details 커스텀 API 엔드포인트가 모바일 기기 모드 대상 설정에 올바르게 입력되었는지 확인하세요. %}

| Braze 용어 | Segment 대응 용어 |
| ----------------- | ------------------ |
| Braze SDK 엔드포인트 | 커스텀 API 엔드포인트 |
| Braze REST 엔드포인트 | 커스텀 REST API 엔드포인트 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="모범 사례" }

Braze SDK 엔드포인트를 올바르게 입력하려면 적절한 형식을 따라야 합니다. Braze SDK 엔드포인트에는 `https://`를 포함하지 않아야 합니다(예: `sdk.iad-03.braze.com`). 그렇지 않으면 Braze 통합이 중단됩니다. 이는 Segment가 자동으로 엔드포인트 앞에 `https://`를 추가하기 때문에, Braze가 유효하지 않은 엔드포인트 `https://https://sdk.iad-03.braze.com`으로 초기화되기 때문입니다.

{% enddetails %}

{% details 데이터 매핑 세부 사항. %}

데이터가 예상대로 전달되지 않는 시나리오:

1. 중첩 커스텀 속성
  - [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)은 기술적으로 Segment를 통해 Braze로 전송할 수 있지만, 매번 **전체 페이로드**가 전송됩니다. 이 경우 페이로드가 전송될 때마다 중첩 객체에 포함된 키당 [데이터 포인트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#data-points)가 발생합니다.<br><br> 페이로드 전송 시 데이터 포인트의 일부만 사용하려면 Segment가 소유하는 커스텀 [대상 함수](https://segment.com/docs/connections/functions/destination-functions/) 기능을 사용할 수 있습니다. Segment 플랫폼의 이 기능을 사용하면 다운스트림 대상으로 데이터가 전송되는 방식을 커스터마이즈할 수 있습니다.

  {% alert note %}
  커스텀 대상 함수는 Segment 내에서 제어되며, Braze는 외부에서 구성된 함수에 대한 가시성이 제한됩니다.
  {% endalert %}

{: start="2"}
2. 서버 간 익명 데이터 전달.
  - 고객은 Segment의 서버 간 라이브러리를 사용하여 익명 데이터를 다른 시스템으로 전달할 수 있습니다. 서버 간(클라우드 모드) 통합을 통해 `external_id`가 없는 사용자를 Braze로 전송하는 방법에 대해 자세히 알아보려면 매핑 메서드 섹션을 참조하세요.

{% enddetails %}

{% details Braze 초기화 커스터마이즈. %}

Braze를 커스터마이즈하는 방법에는 푸시, 인앱 메시지, Content Cards, 초기화 등 여러 가지가 있습니다. 병렬 통합을 사용하면 직접 Braze를 통합하는 것과 마찬가지로 푸시, 인앱 메시지, Content Cards를 커스터마이즈할 수 있습니다.

그러나 Braze SDK가 통합되는 시점을 커스터마이즈하거나 초기화 구성을 지정하는 것은 어렵거나 때로는 불가능할 수 있습니다. 이는 Segment 초기화가 발생할 때 Segment가 Braze SDK를 대신 초기화하기 때문입니다.

{% enddetails %}

{% details Braze에 델타만 전송하세요. %}

사용자 속성 데이터를 전달할 때 마지막 업데이트 이후 변경된 속성 값만 전달하는지 확인하세요. 이렇게 하면 불필요한 데이터 포인트 기록을 방지할 수 있습니다. 클라이언트 측 소스의 경우, Segment의 오픈 소스 [미들웨어](https://github.com/segmentio/segment-braze-mobile-middleware) 도구를 사용하여 통합을 최적화하고 Segment에서 중복 `identify()` 호출을 디바운싱하여 데이터 포인트 사용량을 제한하세요.

{% enddetails %}

{% details 올바른 Braze 데이터 센터를 사용하세요. %}

Segment는 Braze 데이터 센터를 사용하여 서버 간 호출을 위한 적절한 Braze REST 엔드포인트(예: `https://rest.iad-01.braze.com`)를 가져옵니다.

{% enddetails %}

{% details Segment의 이벤트 테스터를 사용할 때 커스텀 REST API 엔드포인트를 제거하세요. %}

Segment의 이벤트 테스터는 Braze `/users/track` REST API 엔드포인트로 이벤트를 전송하며, Braze 대상 설정에 커스텀 REST API 엔드포인트가 설정되어 있으면 해당 엔드포인트가 올바르더라도 `401 Invalid API Key` 오류를 발생시킵니다. 이벤트 테스터가 정상적으로 작동하도록 Segment에서 커스텀 REST API 엔드포인트 값을 제거하세요.

{% enddetails %}

{% details 새 소스를 구성한 후 업데이트에 시간이 필요합니다. %}

Segment는 구성 설정을 오랫동안 캐시에 보관하므로, 새 소스를 구성할 때(예: 클라우드 모드에서 기기 모드로 전환) 캐시가 갱신될 때까지 앱에 새로운 동작이나 데이터가 표시되지 않을 수 있습니다. 소스를 추가할 계획을 세울 때 이 지연을 유의하세요.

{% enddetails %}