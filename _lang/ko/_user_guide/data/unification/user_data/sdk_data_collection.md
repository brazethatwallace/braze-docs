---
nav_title: SDK 데이터 수집
article_title: SDK 데이터 수집
page_order: 1
page_type: reference
description: "이 참조 문서는 개인화된 통합, 자동 수집 통합 및 최소 통합을 통해 SDK가 수집하는 데이터에 대해 다룹니다."

---

# SDK 데이터 수집 {#sdk-data-collection}

> Braze SDK를 앱 또는 사이트에 통합하면 Braze가 특정 유형의 데이터를 자동으로 수집합니다. 이 데이터 중 일부는 프로세스에 필수적이며, 일부 데이터는 필요에 따라 설정하거나 해제할 수 있습니다. 또한 세분화 및 메시징을 더욱 강화하기 위해 추가 유형의 데이터를 수집하도록 Braze를 구성할 수도 있습니다.

Braze는 유연한 데이터 수집이 가능하도록 설계되었으므로 다음과 같은 방법으로 Braze SDK를 통합할 수 있습니다:

- **[최소 통합](#minimum-integration):** Braze는 Braze 서비스와의 통신에 필요한 데이터를 자동으로 수집합니다.
- **[기본적으로 수집되는 선택적 데이터]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer#blocking-data-collection):** Braze는 대부분의 사용 사례에 광범위하게 유용한 일부 데이터를 자동으로 캡처합니다. Braze 서비스와의 통신에 필수적이지 않은 경우 이 데이터의 자동 수집을 비활성화할 수 있습니다.
- **[기본적으로 수집되지 않는 선택적 데이터](#data-not-collected-by-default):** Braze는 특정 사용 사례에 유용한 일부 데이터를 캡처하며, 광범위한 규정 준수를 위해 자동으로 수집을 활성화하지는 않습니다. 사용 사례에 적합한 경우 이 데이터를 수집하도록 선택할 수 있습니다.
- **[개인화된 통합](#personalized-integration):** Braze는 기본 선택적 데이터 외에도 추가 데이터를 유연하게 수집할 수 있는 기능을 제공합니다.

## 최소 통합 {#minimum-integration}

다음은 SDK를 초기화할 때 Braze에서 생성하고 수신하는 필수 데이터 목록입니다. 이 데이터는 구성할 수 없으며 핵심 플랫폼 기능에 필수적입니다. 세션 시작 및 세션 종료를 제외하고, 자동으로 추적되는 다른 모든 데이터는 데이터 포인트 사용량에 포함되지 않습니다.

| 속성 | 설명 | 수집 이유 |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | 가장 최근의 앱 버전 | 이 속성은 앱 버전 호환성과 관련된 메시지를 올바른 기기로 전송하는 데 사용됩니다. 서비스 중단이나 버그를 사용자에게 알리는 데 사용할 수 있습니다. |
| Country | IP 주소 지리 위치로 식별된 국가. IP 주소 지리 위치를 사용할 수 없는 경우 [기기 로캘](#optional-data-collected-by-default)로 식별됩니다. 이 값은 SDK가 `setCountry`로 직접 설정한 값일 수도 있지만, SDK 또는 API를 통해 속성 값을 전달하면 데이터 포인트가 기록됩니다. **국가가 수동으로 설정된 후(SDK 메서드, REST API 또는 CSV 업로드를 통해) SDK는 더 이상 이 값을 자동으로 업데이트하지 않습니다.**| 이 속성은 위치 기반으로 메시지를 타겟팅하는 데 사용됩니다. |
| Device ID | 기기 식별자, 무작위로 생성된 문자열 | 이 속성은 사용자의 기기를 구분하고 올바른 기기로 메시지를 전송하는 데 사용됩니다. |
| OS and OS version | 현재 보고된 기기 또는 브라우저 및 기기 또는 브라우저 버전 | 이 속성은 호환되는 기기에만 메시지를 전송하는 데 사용됩니다. 또한 세분화 내에서 사용자에게 앱 버전 업그레이드를 타겟팅하는 데 사용할 수 있습니다. |
| Session start and session end | 사용자가 통합된 앱 또는 사이트를 사용하기 시작할 때 | Braze SDK는 Braze 대시보드에서 사용자 인게이지먼트 및 사용자를 이해하는 데 필수적인 기타 분석을 계산하는 데 사용되는 세션 데이터를 보고합니다. 세션 시작 및 세션 종료가 앱 또는 사이트에서 호출되는 정확한 시점은 개발자가 구성할 수 있습니다([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [웹]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)). |
| SDK message interaction data | 푸시 직접 열람, 인앱 메시지 상호작용, Content Cards 상호작용 | 이 속성은 메시지가 수신되었는지, 전송이 중복되지 않았는지 확인하는 등 품질 관리 목적으로 사용됩니다. |
| SDK version | 현재 SDK 버전 | 이 속성은 호환되는 기기에만 메시지를 전송하고 서비스 중단을 방지하는 데 사용됩니다. |
| Session ID and session timestamp | 세션 식별자, 무작위로 생성된 문자열 및 세션 타임스탬프 | 사용자가 새 세션을 시작하는지 기존 세션을 계속하는지 판단하고, 해당 사용자를 대상으로 한 메시지의 재적격성을 결정하는 데 사용됩니다.<br><br>인앱 메시지 및 Content Cards와 같은 특정 메시징 채널은 세션 시작 시 기기에 동기화됩니다. 그런 다음 백엔드는 마지막으로 Braze 서버에 연결한 시점과 관련된 데이터(기기가 저장하고 다시 전송하는 데이터)를 사용하여 사용자가 새 메시지를 받을 자격이 있는지 확인합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="최소 통합" }

### 계산된 측정기준 {#calculated-metrics}

Braze는 세 가지 입력으로부터 계산된 측정기준을 생성합니다: [SDK 추적 데이터](#minimum-integration)(예: [세션 시작 및 세션 종료]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)), [비SDK 채널의 메시지 상호작용 데이터]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), 그리고 [Braze 파생 보고 필드]({{site.baseurl}}/user_guide/analytics/metrics_glossary). 이 값들은 Braze 서비스에 의해 생성되므로, 고객 프로필에는 SDK 추적 데이터와 Braze 생성 데이터가 모두 포함될 수 있습니다.

계산된 측정기준에는 채널 기반 측정기준([보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)에 나열됨)과 다음 속성이 포함됩니다.

| 속성                                      | 설명                                                          |
|------------------------------------------------|----------------------------------------------------------------------|
| First used app                                 | 시간                                                                 |
| Last used app                                  | 시간                                                                 |
| Total session count                            | 숫자                                                               |
| Clicked card                                   | 숫자                                                               |
| Last received any message                      | 시간                                                                 |
| Last received email campaign                   | 시간                                                                 |
| Last received push campaign                    | 시간                                                                 |
| Number of feedback items                       | 숫자                                                               |
| Number of sessions in the last Y days          | 숫자 및 시간                                                      |
| Received message from campaign                 | 불리언. 이 필터는 이전 Campaign을 수신했는지 여부에 따라 사용자를 타겟팅합니다. |
| Received message from campaign with tag        | 불리언. 이 필터는 현재 태그가 있는 Campaign을 수신했는지 여부에 따라 사용자를 타겟팅합니다. |
| Retarget campaign                              | 불리언. 이 필터는 과거에 특정 이메일, 푸시 또는 인앱 메시지를 열람하거나 클릭했는지 여부에 따라 사용자를 타겟팅합니다. |
| Uninstalled                                    | 불리언 및 시간                                                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="계산된 측정기준" }

최소 통합이란 [최소 통합](#minimum-integration)에 나열된 필수 데이터만 수집하고, [선택적 SDK 데이터 수집 차단](#optional-data-collected-by-default)을 통해 [기본적으로 수집되는 선택적 데이터](#optional-data-collected-by-default)를 옵트아웃하는 것을 의미합니다.

{% alert important %}
최소 통합을 원하면서 mParticle, Segment, Tealium 또는 GTM을 사용하는 경우 다음 사항에 유의하세요:
- **모바일 플랫폼**: 이러한 구성에 대해 코드를 수동으로 업데이트해야 합니다. mParticle과 Segment는 자체 플랫폼을 통해 이를 수행하는 방법을 제공하지 않습니다.
- **웹**: 최소 통합 구성을 허용하려면 Braze 통합을 네이티브로 수행해야 합니다. 태그 매니저는 자체 플랫폼을 통해 이를 수행하는 방법을 제공하지 않습니다.
{% endalert %}

## 기본적으로 수집되는 선택적 데이터 {#optional-data-collected-by-default}

최소 통합 데이터 외에도, SDK 통합을 초기화할 때 Braze에서 다음 속성을 자동으로 캡처합니다. 최소 통합을 위해 이러한 속성 수집을 [옵트아웃]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer#blocking-data-collection)할 수 있습니다.

| 속성               | 플랫폼          | 설명                                                                        | 수집 이유                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 브라우저 이름            | 웹               | 브라우저의 이름                                                                | 이 속성은 호환되는 브라우저에만 메시지를 보내는 데 사용됩니다. 브라우저 기반 세분화에도 사용할 수 있습니다.                                     |
| 기기 로캘           | Android, iOS, 웹 | 기기의 기본 로캘                                                   | 이 속성은 사용자가 선호하는 언어로 메시지를 번역하는 데 사용됩니다.                                                                                            |
| 가장 최근 기기 로캘           | Android, iOS, 웹 | 기기의 가장 최근 기본 로캘                                                   | 이 속성은 사용자의 기기 설정에서 가져오며, 사용자가 선호하는 언어로 메시지를 번역하는 데 사용됩니다. `Most Recent Location` 속성과는 독립적입니다.                                                                                            |
| 기기 모델            | Android, iOS      | 기기의 특정 하드웨어                                                | 이 속성은 호환되는 기기에만 메시지를 보내는 데 사용됩니다. 세분화에도 사용할 수 있습니다.                                                 |
| 기기 브랜드            | Android           | 기기의 브랜드(예: Samsung)                                         | 이 속성은 호환되는 기기에만 메시지를 보내는 데 사용됩니다.                                                                                          |
| 기기 무선 통신사 | Android, iOS      | 모바일 통신사                                                                 | 이 속성은 메시지 타겟팅에 선택적으로 사용됩니다.<br><br>**참고:** 이 필드는 iOS 16부터 더 이상 사용되지 않으며, 향후 iOS 버전에서는 기본값이 `--`로 설정됩니다. |
| 언어                | Android, iOS, 웹 | 기기 로캘에서 가져온 기기 또는 브라우저 언어                                                           | 이 속성은 사용자가 선호하는 언어로 메시지를 번역하는 데 사용됩니다. 기기 로캘을 기반으로 합니다.                                                                                            |
| 알림 설정   | Android, iOS, 웹 | 이 앱에서 푸시 알림이 활성화되어 있는지 여부                                   | 이 속성은 푸시 알림을 활성화하는 데 사용됩니다.                                                                                                                    |
| 해상도              | Android, iOS, 웹 | 기기 또는 브라우저 해상도                                                          | 기기 기반 메시지 타겟팅에 선택적으로 사용됩니다. 이 값의 형식은 "`<width>`x`<height>`"입니다.                                                                 |
| 시간대               | Android, iOS, 웹 | 기기 또는 브라우저 시간대                                                           | 이 속성은 각 사용자의 현지 시간대에 맞춰 적절한 시간에 메시지를 보내는 데 사용됩니다.                                                   |
| 사용자 에이전트              | 웹               | [사용자 에이전트](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | 이 속성은 호환되는 기기에만 메시지를 보내는 데 사용됩니다. 세분화에도 사용할 수 있습니다.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="기본적으로 수집되는 선택적 데이터" }

기기 수준 속성(기기 무선 통신사, 시간대, 해상도 등) 추적에 대해 자세히 알아보려면 플랫폼별 설명서를 참조하세요: [Android]({{site.baseurl}}/developer_guide/storage?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage?tab=swift), [웹]({{site.baseurl}}/developer_guide/storage#cookies).

## 기본적으로 수집되지 않는 데이터 {#data-not-collected-by-default}

기본적으로 다음 속성은 수집되지 않습니다. 각 속성은 수동으로 통합해야 합니다.

| 속성                  | 플랫폼     | 설명                                                                                                                                                                                                                                                                                                               | 수집되지 않는 이유                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 기기 광고 추적 활성화 | Android, iOS | iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | 이 속성에는 추가적인 앱 수준 권한이 필요하며, 통합 담당자가 해당 권한을 부여해야 합니다.                                                                                                                                                                                      |
| 기기 IDFA                | iOS          | 광고주를 위한 기기 식별자                                                                                                                                                                                                                                                                                         | 이 기능은 광고 추적 투명성 프레임워크가 필요하며, 앱 스토어에서 추가적인 개인정보 보호 심사가 진행됩니다. 자세한 내용은 [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:))를 참조하세요. |
| Google 광고 ID      | Android      | Google Play 앱 내 광고를 위한 식별자                                                                                                                                                                                                                                                                        | 이 기능은 앱에서 GAID를 가져와 Braze에 전달해야 합니다. 자세한 내용은 [선택적 Google 광고 ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id)를 참조하세요.                                         |
| 가장 최근 위치 | Android, iOS | 사용자 기기의 마지막으로 알려진 GPS 위치입니다. 세션 시작 시 업데이트되며 사용자 프로필에 저장됩니다. | 사용자가 앱에 위치 권한을 부여해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="기본적으로 수집되지 않는 데이터" }

{% alert note %}
Braze SDK는 IP 주소를 로컬에 저장하지 않습니다.
{% endalert %}

## 개인화된 통합 {#personalized-integration}

Braze를 최대한 활용하기 위해, SDK 통합 담당자들은 자동으로 수집되는 데이터 외에도 Braze SDK를 구현하고 비즈니스와 관련된 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes), [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events#logging-custom-events), [구매 이벤트]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#log-purchase-events)를 기록하는 경우가 많습니다.

개인화된 통합을 통해 사용자 경험에 맞는 맞춤형 커뮤니케이션이 가능합니다.

{% alert important %}
Braze는 세션이 5,000,000회를 초과하는 사용자("더미 사용자")를 차단하거나 블록하며, 해당 사용자의 SDK 이벤트를 더 이상 수집하지 않습니다. 자세한 내용은 <a href="/docs/user_archival#spam-blocking">스팸 차단</a> 을 참조하세요.
{% endalert %}