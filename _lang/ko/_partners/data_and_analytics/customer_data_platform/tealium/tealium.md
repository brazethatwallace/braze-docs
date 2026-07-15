---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "이 참조 문서에서는 모바일, 웹 및 대체 데이터를 다른 서드파티 소스에 연결할 수 있는 범용 데이터 허브인 Tealium과 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/)은 EventStream, AudienceStream, iQ 태그 관리로 구성된 범용 데이터 허브이자 고객 데이터 플랫폼으로, 서드파티 소스의 모바일, 웹 및 대체 데이터를 연결할 수 있습니다. Braze에 Tealium을 연결하면 커스텀 이벤트, 사용자 속성, 구매 데이터의 데이터 흐름을 통해 실시간으로 데이터에 기반한 조치를 취할 수 있습니다.

![다양한 Tealium 제품과 Braze 플랫폼이 어떻게 크로스채널 캠페인을 실시간으로 활성화하는지를 보여주는 Tealium 개요 그래픽.]({% image_buster /assets/img/tealium/tealium_overview.png %}){: style="border:0;"}

Braze와 Tealium의 통합을 통해 사용자를 추적하고 다양한 사용자 분석 제공업체로 데이터를 라우팅할 수 있습니다. Tealium을 사용하면 다음을 수행할 수 있습니다:
- Tealium 오디언스를 [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream)을 통해 Braze에 동기화하여 Braze Campaign 및 Canvases를 개인화하거나 Segments를 구축하는 데 사용할 수 있습니다.
- [플랫폼 간 데이터를 가져올 수 있습니다](#choose-your-integration-type). Braze는 Android, iOS 및 웹 애플리케이션을 위한 [병렬](#side-by-side-sdk-integration) SDK 통합과 이벤트 데이터를 보고할 수 있는 모든 플랫폼에서 사용할 수 있는 [서버 간](#server-to-server-integration) 통합을 모두 제공합니다.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream은 데이터의 중심에 위치하는 데이터 수집 및 API 허브입니다. EventStream은 설정 및 설치부터 수신 사용자 데이터의 식별, 유효성 검사 및 향상에 이르기까지 전체 데이터 공급망을 처리합니다. EventStream은 이벤트 피드와 커넥터를 통해 실시간 작업을 수행합니다. 다음은 [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/)을 구성하는 기능입니다.
- 데이터 소스(설치 및 데이터 수집)
- 라이브 이벤트(실시간 데이터 검사)
- 이벤트 사양 및 속성(데이터 레이어 요구 사항 및 유효성 검사)
- 이벤트 피드(필터링된 이벤트 유형)
- 이벤트 커넥터(API 허브 동작)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream은 옴니채널 고객 세분화 및 실시간 액션 엔진입니다. AudienceStream은 EventStream으로 유입되는 데이터를 가져와 브랜드에 대한 고객 인게이지먼트의 가장 중요한 속성을 나타내는 방문자 프로필을 생성합니다. 설정 단계는 [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream) 문서를 참조하세요.

{% endtab %}
{% tab iQ 태그 관리 %}
Tealium iQ를 사용하면 Tealium iQ 태그 관리 UI에서 태그를 사용하여 앱에서 코드를 트리거할 수 있습니다. 이 태그는 모바일 및 웹 플랫폼에서 이벤트 데이터를 수집, 제어 및 전달하여 앱에 Braze 전용 코드를 추가하지 않고도 네이티브 Braze 구현을 구성할 수 있습니다. 사용자는 iQ 태그 관리 또는 JSON 구성 파일(권장 Tealium 접근 방식)을 통해 모바일 원격 명령을 통합할 수 있습니다. Braze Web SDK를 사용하는 사용자는 웹 iQ 태그를 통해 통합해야 합니다.

각 방법의 장단점에 대해 자세히 알아보려면 다음 [Tealium iQ 태그 관리자](#mobile-remote-commands) 섹션을 참조하세요.
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium은 배치 및 비배치 커넥터 동작을 모두 제공합니다. 비배치 커넥터는 실시간 요청이 사용 사례에 중요하고 Braze API 사용량 제한 사양에 도달하는 것에 대한 우려가 없을 때 사용해야 합니다. 질문이 있으시면 Braze 고객지원 또는 고객 성공 매니저에게 문의하세요.<br><br>

배치 커넥터의 경우, 다음 임계값 중 하나가 충족될 때까지 요청이 대기줄에 추가됩니다:<br><br>
- 최대 요청 수: 75
- 가장 오래된 요청 이후 최대 시간: 10분
- 최대 요청 크기: 1 MB

Tealium은 기본적으로 동의 이벤트(구독 기본 설정) 또는 사용자 삭제 이벤트를 배치 처리하지 않습니다.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Tealium 계정 | 이 파트너십을 활용하려면 서버 및/또는 클라이언트 측 액세스 권한이 있는 [Tealium 계정](https://my.tealiumiq.com/)이 필요합니다. |
| 설치된 소스 및 Tealium 소스 [라이브러리](https://docs.tealium.com/platforms/) | 모바일 앱, 웹사이트 또는 백엔드 서버 등 Tealium으로 전송되는 모든 데이터의 출처입니다.<br><br>성공적인 Tealium 커넥터를 설정하려면 먼저 앱, 사이트 또는 서버에 라이브러리를 설치해야 합니다. |
| Braze REST 및 SDK 엔드포인트 | REST 또는 SDK 엔드포인트 URL입니다. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics#endpoints)에 따라 달라집니다. |
| Braze 앱 식별자 키(병렬 통합만 해당) | 앱 식별자 키입니다. <br><br>이 키는 **Braze 대시보드 > 설정 관리 > API 키**에서 찾을 수 있습니다. |
| 코드 버전(병렬 통합만 해당) | SDK 버전에 해당하며 major.minor 형식이어야 합니다(예: 3.0.1이 아닌 3.2). 코드 버전은 3.0 이상이어야 합니다. |
| REST API 키(서버 간 통합만 해당) | `users.track` 및 `users.delete` 권한이 있는 Braze REST API 키입니다. <br><br>이 키는 **Braze 대시보드 > 개발자 콘솔 > REST API 키 > 새 API 키 생성**에서 생성할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 유형 선택 {#choose-your-integration-type}

| 통합 | 세부 정보 |
| ----------- | ------- |
| [병렬](#side-by-side-sdk-integration) | Tealium의 SDK를 사용하여 이벤트를 Braze 네이티브 호출로 변환하여 서버 간 통합보다 더 깊은 기능과 더 포괄적인 Braze 사용에 액세스할 수 있습니다.<br><br>Braze 원격 명령을 사용할 계획이라면 Tealium이 모든 Braze 메서드를 지원하지 않는다는 점에 유의하세요(예: Content Cards). 해당 원격 명령을 통해 매핑되지 않은 Braze 메서드를 사용하려면 코드베이스에 네이티브 Braze 코드를 추가하여 메서드를 호출해야 합니다.|
| [서버 간](#server-to-server-integration) | Tealium에서 Braze REST API 엔드포인트로 데이터를 전달합니다.<br><br>인앱 메시징, Content Cards 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다. 또한 이 방법을 통해 사용할 수 없는 기기 수준 필드와 같은 자동 캡처 데이터도 있습니다.<br><br>이러한 기능을 사용하려면 병렬 통합을 고려하세요.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="통합 유형 선택" }

## 병렬 SDK 통합 {#side-by-side-sdk-integration}

### 원격 명령 {#remote-commands}

원격 명령은 Tealium iOS 및 Android 라이브러리의 기능으로, Tealium SDK에서 Braze 서버를 통해 Braze로 호출할 수 있습니다. Braze 원격 명령 모듈은 필요한 Braze 라이브러리를 자동으로 설치 및 빌드하고 모든 메시지 렌더링 및 분석 추적을 처리합니다. Braze 모바일 원격 명령을 사용하려면 앱에 Tealium 라이브러리가 설치되어 있어야 합니다.

Tealium은 모바일 원격 명령을 통합하는 두 가지 방법을 제공하며, 통합 유형 간에 기능 손실은 없고 기본 네이티브 코드는 동일합니다.

| 모바일 원격 명령 방법 | 장점 | 단점 |
| --- | --- | --- |
| **원격 명령 태그** | Tealium iQ UI를 사용하여 원격 명령으로 전송되는 매핑 및 데이터를 쉽게 수정할 수 있습니다.<br><br>이를 통해 앱이 이미 앱 스토어에 있는 상태에서 클라이언트가 앱을 업데이트하지 않고도 서드파티 SDK에 추가 데이터 또는 이벤트를 전송할 수 있습니다. | 앱의 태그 관리 모듈은 JavaScript를 처리하기 위해 숨겨진 웹뷰에 의존합니다. |
| **JSON 구성 파일**<br>([권장](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | JSON 방법을 사용하면 앱에 숨겨진 웹뷰가 필요 없어지고 메모리 소비가 크게 줄어듭니다.<br><br>JSON 파일은 원격으로 호스팅하거나 고객의 앱 내에 로컬로 호스팅할 수 있습니다. | 현재 이를 관리할 UI가 없으므로 약간의 추가 작업이 필요합니다.<br><br>참고: Tealium은 이 문제를 해결하고 iQ 태그 관리 버전과 동일한 수준의 유연성을 JSON 원격 명령에 제공할 관리 UI를 추가하는 작업을 진행 중입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="원격 명령" }

Braze 모바일 원격 명령 데이터 매핑을 사용하여 기본 사용자 속성 및 커스텀 속성을 설정하고 구매 및 커스텀 이벤트를 추적하세요. 해당 Braze 메서드는 다음 차트를 참조하세요.

| 원격 명령 | Braze 메서드 |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| emailnotification | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| initialize | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logPurchase() |
| pushnotification | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| useridentifier | changeUser() |
{: .reset-td-br-1 .reset-td-br-2 aria-label="원격 명령" }

Braze 모바일 원격 명령 설정 방법 및 지원되는 메서드 개요에 대한 자세한 내용은 Tealium 개발자 설명서에서 확인할 수 있습니다:
- [원격 명령](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [원격 명령 태그](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Braze 모바일 원격 명령은 모든 Braze 메서드 및 메시징 채널을 지원하지 않습니다(예: Content Cards). 해당 원격 명령을 통해 매핑되지 않은 Braze 메서드를 사용하려면 코드베이스에 네이티브 Braze 코드를 추가하여 메서드를 직접 호출해야 합니다.
{% endalert%}

### Braze Web SDK 태그 {#braze-web-sdk-tag}

Braze Web SDK 태그를 사용하여 웹사이트에 Braze Web SDK를 배포하세요. [Tealium iQ 태그 관리](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)를 통해 고객은 Tealium 대시보드 내에서 Braze를 태그로 추가하여 방문자 활동을 추적할 수 있습니다. 태그는 일반적으로 마케터가 온라인 광고, 이메일 마케팅 및 사이트 개인화의 효과를 이해하는 데 사용됩니다.

1. Tealium에서 **iQ > Tags > + Add Tag > Braze Web SDK**로 이동합니다.
2. 태그 구성 대화 상자에서 API 키(Braze 앱 식별자 키), 기본 URL(Braze SDK 엔드포인트) 및 [Braze Web SDK 코드 버전](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)을 입력합니다. 디버깅 목적으로 웹 콘솔에 정보를 기록하도록 로깅을 활성화할 수도 있습니다.
3. [로드 규칙](https://docs.tealium.com/iq-tag-management/load-rules/about/) 대화 상자에서 "모든 페이지에서 로드"를 선택하거나 **Create Rule**을 선택하여 사이트에서 이 태그의 인스턴스를 로드할 시기와 위치를 결정합니다.
4. **[Data Mappings](https://docs.tealium.com/iq-tag-management/data-mappings/about/)** 대화 상자에서 **Create Mappings**를 선택하여 Tealium 데이터를 Braze에 매핑합니다. Braze Web SDK 태그의 대상 변수는 태그의 **Data Mapping** 탭에 내장되어 있습니다. [다음 표](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)에서 사용 가능한 대상 카테고리를 나열하고 각 대상 이름을 설명합니다.
5. **Finish**를 선택합니다.

### 병렬 통합 리소스 {#side-by-side-integrations-resources}

- iOS 원격 명령: [Tealium 설명서](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub 리포지토리](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Android 원격 명령: [Tealium 설명서](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub 리포지토리](https://github.com/Tealium/tealium-android-braze-remote-command)
- Web SDK 태그: [Tealium 설명서](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## 서버 간 통합 {#server-to-server-integration}

이 통합은 Tealium에서 Braze REST API로 데이터를 전달합니다.

서버 간 통합은 인앱 메시징, Content Cards 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다. 또한 이 방법을 통해 사용할 수 없는 기기 수준 필드와 같은 자동 캡처 데이터도 있습니다.

이 데이터와 기능을 사용하려면 [병렬]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium#side-by-side-sdk-integration) SDK 통합을 고려하세요.

### 1단계: 소스 설정 {#step-1-set-up-a-source}

Tealium에서는 먼저 커넥터가 가져올 유효한 데이터 소스를 설정해야 합니다.
1. Tealium의 사이드바에서 **Server-Side** 아래의 **Sources > Data Sources > + Add Data Source**로 이동합니다.
2. 사용 가능한 카테고리에서 원하는 플랫폼을 찾고 소스 이름을 지정합니다. 이것은 필수 필드입니다.<br>![플랫폼 선택 및 소스 이름 필드가 있는 Tealium 데이터 소스 추가 대화 상자.]({% image_buster /assets/img/tealium/data_source.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. **Event Specifications** 옵션에서 포함할 [이벤트 사양](https://docs.tealium.com/server-side/event-specifications/about/)을 선택합니다. 이벤트 사양은 설치에서 추적할 이벤트 이름과 필수 속성을 식별하는 데 도움이 됩니다. 이러한 사양은 수신 이벤트에 적용됩니다.<br>![데이터 소스에 대한 Tealium 이벤트 사양 옵션.]({% image_buster /assets/img/tealium/event_specs.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>어떤 데이터가 가장 가치 있는지, 어떤 사양이 사용 사례에 가장 적합한지 시간을 들여 생각해 보세요. [커스텀 이벤트 사양](https://docs.tealium.com/iq-tag-management/events/about/)도 사용할 수 있습니다. <br>
4. 다음 대화 상자는 **Get Code** 단계로 진행됩니다. 여기에 제공된 기본 코드와 이벤트 추적 코드가 설치 가이드 역할을 합니다. 팀과 이 지침을 공유하려면 제공된 PDF를 다운로드하세요. 완료되면 **Save & Continue**를 선택합니다.<br>
5. 이제 저장된 소스를 확인하고 이벤트 사양을 추가하거나 제거할 수 있습니다. <br>![이벤트 사양 및 연결 세부 정보가 포함된 저장된 Tealium 데이터 소스.]({% image_buster /assets/img/tealium/braze_connection.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>상세 데이터 소스 보기에서 다음 작업을 수행할 수 있습니다:
- 데이터 소스 키 보기 및 복사
- 설치 지침 보기
- **Get Code** 페이지로 돌아가기
- 이벤트 사양 추가 또는 제거
- 이벤트 사양과 관련된 라이브 이벤트 보기로 이동
- 기타...<br>
6. 마지막으로 페이지 상단의 **Save / Publish**를 선택합니다. 소스를 게시하지 않으면 Braze 커넥터를 구성할 때 소스를 찾을 수 없습니다.

데이터 소스 설정 및 편집에 대한 추가 지침은 [데이터 소스](https://docs.tealium.com/server-side/data-sources/about-data-sources/)를 참조하세요.

### 2단계: 이벤트 커넥터 생성 {#step-2-create-an-event-connector}

커넥터는 데이터를 전송하는 데 사용되는 Tealium과 다른 벤더 간의 통합입니다. 이러한 커넥터에는 파트너가 지원하는 API를 나타내는 동작이 포함되어 있습니다.

1. Tealium의 사이드바에서 **Server-Side** 아래의 **EventStream > Event Connectors**로 이동합니다.
2. 파란색 **+ Add Connector** 버튼을 선택하여 커넥터 마켓플레이스를 탐색합니다. 나타나는 새 대화 상자에서 스포트라이트 검색을 사용하여 **Braze** 커넥터를 찾습니다.
3. 이 커넥터를 추가하려면 **Braze** 커넥터 타일을 클릭합니다. 클릭하면 연결 요약과 필수 정보, 지원되는 동작 및 구성 지침 목록을 볼 수 있습니다. 구성은 소스, 구성, 동작의 세 단계로 구성됩니다.

#### 소스 {#source}

소스가 구성된 후 **EventStream** > **Event Connectors** > **+ Add Connector** > **Braze** 아래의 Braze 커넥터 페이지로 돌아갑니다.

그런 다음 방금 만든 데이터 소스를 선택하고 **Event Feed** 아래에서 **All Events** 또는 특정 이벤트 사양을 선택합니다. 변경된 값만 Braze로 전송하는 권장 경로입니다. **Continue**를 선택합니다.

#### 구성 {#configuration}

다음으로 페이지 하단의 **Add Connector**를 선택합니다. 커넥터 이름을 지정하고 Braze API 엔드포인트와 Braze REST API 키를 입력합니다.

![API 엔드포인트 및 REST API 키 필드가 있는 Braze 커넥터 구성.]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%"}

이전에 커넥터를 생성한 적이 있다면 사용 가능한 커넥터 목록에서 기존 커넥터를 선택하고 연필 아이콘으로 수정하거나 휴지통 아이콘으로 삭제할 수 있습니다.

#### 동작 {#action}

다음으로 커넥터 동작의 이름을 지정하고 구성한 매핑에 따라 데이터를 전송할 동작 유형을 선택합니다. 여기에서 Braze 속성, 이벤트 및 구매를 Tealium 속성, 이벤트 및 구매 이름에 매핑합니다.

{% alert important %}
제공되는 모든 필드가 필수는 아닙니다.

![선택 사항 필드가 축소된 Tealium 커넥터 동작.]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab 사용자 추적 - 배치 및 비배치 %}

이 동작을 사용하면 사용자, 이벤트 및 구매 속성을 하나의 동작으로 모두 추적할 수 있습니다.

| 매개변수 | 설명 |
| ---------- | ----------- |
| 사용자 ID | 이 필드를 사용하여 Tealium 사용자 ID 필드를 Braze에 해당하는 필드에 매핑합니다. 하나 이상의 사용자 ID 속성을 매핑합니다. 여러 ID가 지정된 경우 다음 우선순위에 따라 첫 번째 비어 있지 않은 값이 선택됩니다: 외부 ID, Braze ID, 별칭 이름, 별칭 라벨.<br><br>\- 푸시 토큰을 가져오는 경우 외부 ID와 Braze ID를 지정하면 안 됩니다.<br>\- 사용자 별칭을 지정하는 경우 별칭 이름과 별칭 라벨을 모두 설정해야 합니다. <br><br>자세한 내용은 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 확인하세요. |
| 사용자 속성 | 기존 Braze 고객 프로필 필드 이름을 사용하여 Braze 대시보드에서 고객 프로필 값을 업데이트하거나 고객 프로필에 자체 커스텀 [사용자 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens) 데이터를 추가합니다.<br><br>\- 기본적으로 사용자가 존재하지 않으면 새 사용자가 생성됩니다.<br>\- **Update Existing Only**를 `true`로 설정하면 기존 사용자만 업데이트되고 새 사용자는 생성되지 않습니다.<br>\- Tealium 속성이 비어 있으면 null로 변환되어 Braze 고객 프로필에서 제거됩니다. 사용자 속성을 제거하기 위해 null 값을 Braze로 전송하지 않으려면 보강을 사용해야 합니다. |
| 사용자 속성 수정 | 이 필드를 사용하여 특정 사용자 속성을 증가 또는 감소시킵니다<br><br>\- 정수 속성은 양수 또는 음수 정수로 증가시킬 수 있습니다.<br>\- 배열 속성은 기존 배열에서 값을 추가하거나 제거하여 수정할 수 있습니다. |
| 이벤트 | 이벤트는 특정 사용자가 특정 타임스탬프에 수행한 커스텀 이벤트의 단일 발생을 나타냅니다. 이 필드를 사용하여 Braze [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object)의 이벤트 속성을 추적하고 매핑합니다. <br><br>\- 이벤트 속성 `Name`은 매핑된 모든 이벤트에 필수입니다.<br>\- 이벤트 속성 `Time`은 명시적으로 매핑되지 않는 한 자동으로 현재 시간으로 설정됩니다. <br>\- 기본적으로 이벤트가 존재하지 않으면 새 이벤트가 생성됩니다. `Update Existing Only`를 `true`로 설정하면 기존 이벤트만 업데이트되고 새 이벤트는 생성되지 않습니다.<br>\- 배열 유형 속성을 매핑하여 여러 이벤트를 추가합니다. 배열 유형 속성은 동일한 길이여야 합니다.<br>\- 단일 값 속성을 사용할 수 있으며 각 이벤트에 적용됩니다. |
| 이벤트 템플릿 | 본문 데이터에서 참조할 이벤트 템플릿을 제공합니다. 템플릿을 사용하여 Braze로 전송하기 전에 데이터를 변환할 수 있습니다. 자세한 내용은 Tealium의 [템플릿 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)를 참조하세요. |
| 이벤트 템플릿 변수 | 이벤트 템플릿 변수를 데이터 입력으로 제공합니다. 자세한 내용은 Tealium의 [템플릿 변수 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)를 참조하세요. |
| 구매 | 이 필드를 사용하여 Braze [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object)의 사용자 구매 속성을 추적하고 매핑합니다.<br><br>\- 구매 속성 `Product ID`, `Currency`, `Price`는 매핑된 모든 구매에 필수입니다.<br>\- 구매 속성 `Time`은 명시적으로 매핑되지 않는 한 자동으로 현재 시간으로 설정됩니다.<br>\- 기본적으로 구매가 존재하지 않으면 새 구매가 생성됩니다. `Update Existing Only`를 `true`로 설정하면 기존 구매만 업데이트되고 새 구매는 생성되지 않습니다.<br>\- 배열 유형 속성을 매핑하여 여러 구매 항목을 추가합니다. 배열 유형 속성은 동일한 길이여야 합니다.<br>\- 단일 값 속성을 사용할 수 있으며 각 항목에 적용됩니다.|
| 구매 템플릿 | 템플릿을 사용하여 Braze로 전송하기 전에 데이터를 변환할 수 있습니다.<br>\- 중첩된 오브젝트 지원이 필요한 경우 구매 템플릿을 정의합니다.<br>\- 구매 템플릿이 정의되면 동작의 구매 섹션에서 설정한 구성은 무시됩니다.<br>\- 자세한 내용은 Tealium의 [템플릿 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)를 참조하세요.|
| 구매 템플릿 변수 | 제품 템플릿 변수를 데이터 입력으로 제공합니다. 자세한 내용은 Tealium의 [템플릿 변수 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="동작" }

![사용자 속성, 이벤트 및 구매를 매핑하는 Tealium 사용자 추적 커넥터 동작.]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab 사용자 삭제 - 비배치 %}

이 동작을 사용하면 Braze 대시보드에서 사용자를 삭제할 수 있습니다.

| 매개변수 | 설명 |
| ---------- | ----------- |
| 사용자 ID | 이 필드를 사용하여 Tealium 사용자 ID 필드를 Braze에 해당하는 필드에 매핑합니다. <br><br>\- 하나 이상의 사용자 ID 속성을 매핑합니다. 여러 ID가 지정된 경우 다음 우선순위에 따라 첫 번째 비어 있지 않은 값이 선택됩니다: 외부 ID, Braze ID, 별칭 이름, 별칭 라벨.<br>\- 사용자 별칭을 지정하는 경우 별칭 이름과 별칭 라벨을 모두 설정해야 합니다.<br><br>자세한 내용은 Braze [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="동작" }

![사용자 ID 매핑이 포함된 Tealium 사용자 삭제 커넥터 동작.]({% image_buster /assets/img/tealium/track_user_delete.png %})

선택한 옵션을 수정하려면 **Back**을 선택하여 편집하거나 **Finish**를 선택하여 완료합니다.

{% endtab %}
{% endtabs %}

**Continue**를 선택합니다.

이제 커넥터가 Tealium 홈 페이지의 커넥터 목록에 표시됩니다. <br>![Braze를 포함한 구성된 커넥터가 나열된 Tealium 홈 페이지.]({% image_buster /assets/img/tealium/summary_list.png %}){: style="max-width:80%;"}

완료되면 커넥터에 대해 **Save / Publish**를 선택해야 합니다. 구성한 동작은 이제 트리거 연결이 충족되면 실행됩니다.

### 3단계: Tealium 커넥터 테스트 {#step-3-test-your-tealium-connector}

커넥터가 실행된 후 제대로 작동하는지 테스트해야 합니다. 가장 간단한 테스트 방법은 Tealium **Trace Tool**을 사용하는 것입니다. Trace를 사용하려면 Tealium Tools 브라우저 확장 프로그램이 추가되어 있는지 확인하세요.

1. 새 추적을 시작하려면 **Server-Side** 옵션 아래의 사이드바에서 **Trace**를 선택합니다. **Start**를 선택하고 Trace ID를 캡처합니다.
2. 브라우저 확장 프로그램을 열고 AudienceStream Trace에 Trace ID를 입력합니다.
3. 실시간 로그를 확인합니다.
4. 유효성을 검사할 동작을 **Actions Triggered** 항목을 선택하여 확장합니다.
5. 유효성을 검사할 동작을 찾고 로그 상태를 확인합니다.

Tealium의 Trace 도구 구현에 대한 자세한 지침은 Tealium의 [Trace 설명서](https://docs.tealium.com/server-side/connectors/trace/about/)를 참조하세요.

## 통합 데모 {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1mP84vVWifzNMN7eMYNORNy0y-WZurzBs/view?usp=sharing" title="Tealium 통합 데모" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 잠재적 데이터 포인트 초과 {#potential-data-point-overages}

Tealium을 통해 Braze를 통합할 때 실수로 불필요한 데이터 포인트를 기록할 수 있는 세 가지 주요 방법이 있습니다:

### 중복 데이터 전송 - 속성의 Braze 델타만 전송하세요 {#sending-duplicate-data-only-send-braze-deltas-of-attributes}

Tealium은 사용자 속성의 Braze 델타를 전송하지 않습니다. 예를 들어, 사용자의 이름, 이메일 및 휴대폰 번호를 추적하는 EventStream 동작이 있는 경우, Tealium은 동작이 트리거될 때마다 세 가지 속성을 모두 Braze로 전송합니다. Tealium은 변경되거나 업데이트된 내용을 확인하고 해당 정보만 전송하지 않습니다.

**해결 방법**: <br>백엔드를 확인하여 속성이 변경되었는지 여부를 평가하고, 변경된 경우 Tealium의 관련 메서드를 호출하여 고객 프로필을 업데이트할 수 있습니다. **이것은 Braze를 직접 통합하는 사용자가 일반적으로 수행하는 작업입니다.** <br>**또는**<br> 백엔드에 자체 고객 프로필 버전을 저장하지 않아 속성이 변경되었는지 여부를 알 수 없는 경우, AudienceStream을 사용하고 [보강을 생성](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/)하여 값이 변경된 경우에만 사용자 속성을 전송할 수 있습니다. Tealium의 [보강 규칙](https://docs.tealium.com/server-side-connectors/braze-connector/) 설명서를 참조하세요.

### 관련 없는 데이터 전송 또는 불필요한 데이터 덮어쓰기 {#sending-irrelevant-data-or-needlessly-overwriting-data}

동일한 이벤트 피드를 타겟팅하는 EventStream이 여러 개 있는 경우, **해당 커넥터에 활성화된 모든 동작은** 단일 동작이 트리거될 때마다 자동으로 실행됩니다. 이로 인해 Braze에서 데이터가 덮어쓰여지고 불필요한 데이터 포인트가 기록될 수 있습니다.

**해결 방법**: <br>각 동작을 추적하기 위해 별도의 이벤트 사양 또는 피드를 설정합니다. <br>**또는**<br> Tealium 대시보드의 토글을 사용하여 실행하지 않으려는 동작(또는 커넥터)을 비활성화합니다.

### Braze를 너무 일찍 초기화 {#initializing-braze-too-early}

Braze Web SDK 태그를 사용하여 Tealium과 통합하는 경우 MAU가 급격히 증가할 수 있습니다. **Braze가 페이지 로드 시 초기화되면, 웹 사용자가 처음으로 웹사이트를 방문할 때마다 Braze가 익명 프로필을 생성합니다.** 여기에는 봇 트래픽도 포함되어 활성 사용자 수가 부풀려질 수 있습니다. 일부 사용자는 MAU 수를 줄이기 위해 "로그인" 또는 "동영상 시청"과 같은 특정 동작을 완료한 경우에만 사용자 행동을 추적하고 싶을 수 있습니다.

**해결 방법**: <br>[로드 규칙](https://docs.tealium.com/iq-tag-management/load-rules/about/)을 설정하여 사이트에서 태그가 로드되는 시기와 위치를 정확히 결정합니다. 봇 트래픽 필터링 및 조건부 SDK 초기화에 대한 보다 포괄적인 가이드는 [봇 트래픽 필터링]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering)을 참조하세요.