---
nav_title: SDK 개요
article_title: 개발자용 SDK 개요
description: "이 온보딩 참조 문서에서는 Braze SDK 개발자를 위한 기술 개요를 제공합니다. SDK에서 추적하는 기본 분석에 대해 설명합니다."
page_order: 0
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}개발자용 SDK 개요 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdevelopersdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordersdk-overview-for-developers}

> Braze SDK 통합을 시작하기 전에 정확히 무엇을 구축하고 통합하는지 궁금할 수 있습니다. 요구 사항에 맞게 SDK를 추가로 커스터마이즈하는 방법도 궁금할 수 있습니다. 이 문서는 모든 SDK 관련 질문에 대한 답을 찾는 데 도움을 줄 수 있습니다.

SDK에 대한 기본적인 개요를 찾고 계신 마케터인가요? 대신 [마케터 개요]({{site.baseurl}}/user_guide/get_started/sdk_overview)를 확인하세요.

간단히 말해서, Braze SDK는:
* 사용자 데이터를 수집하고 통합된 고객 프로필로 동기화합니다
* 세션 데이터, 기기 정보, 푸시 토큰을 자동으로 수집합니다
* 마케팅 참여 데이터 및 비즈니스에 특화된 커스텀 데이터를 캡처합니다
* 푸시 알림, 인앱 메시지 및 콘텐츠 카드 메시징 채널을 지원합니다

Braze SDK 통합 기본 사항과 핵심 기능에 대한 간략한 소개는 다음 동영상을 시청하세요.

{% multi_lang_include video.html id="il152jayp0" source="wistia" %}

## 앱 성능 {#app-performance}

Braze는 앱 성능에 부정적인 영향을 미치지 않습니다.

Braze SDK는 매우 작은 용량을 차지합니다. 수동 네트워크 제어를 허용하는 것 외에도, 네트워크 품질에 따라 사용자 데이터를 플러시하는 속도를 자동으로 조절합니다. SDK에서 보내는 API 요청을 자동으로 일괄 처리하여 최대 네트워크 효율성을 유지하면서 데이터가 빠르게 기록되도록 합니다. 마지막으로, 각 API 호출 시 클라이언트에서 Braze로 전송되는 데이터의 양은 매우 적습니다.

## SDK 호환성 {#sdk-compatibility}

Braze SDK는 다른 SDK와 충돌하지 않도록 설계되어 있으며, 앱에 있는 다른 SDK에 간섭하지 않습니다. 다른 SDK와의 비호환성으로 인해 발생한 것으로 보이는 문제가 있는 경우, Braze 지원팀에 문의하세요.

## 기본 분석 및 세션 처리 {#default-analytics-and-session-handling}

특정 사용자 데이터는 SDK에 의해 자동으로 수집됩니다. 예를 들어 최초 앱 사용일, 최근 앱 사용일, 총 세션 수, 기기 OS 등이 있습니다. 통합 가이드를 따라 SDK를 구현하면 이러한 [기본 데이터 수집]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)을 활용할 수 있습니다. 이 목록을 확인하면 사용자에 대한 동일한 정보를 두 번 이상 저장하는 것을 방지할 수 있습니다. 세션 시작 및 세션 종료를 제외하고, 자동으로 추적되는 다른 모든 데이터는 데이터 포인트 사용량에 포함되지 않습니다.

{% alert note %}
모든 기능은 구성할 수 있지만, 기본 데이터 수집 모델을 완전히 구현하는 것이 좋습니다.

<br>사용 사례에 따라 필요한 경우, 통합이 완료된 후 [특정 데이터의 수집을 제한](#blocking-data-collection)할 수 있습니다.
{% endalert %}

## 데이터 업로드 및 다운로드 {#data-upload-and-download}

Braze SDK는 데이터(세션, 커스텀 이벤트 등)를 캐시하고 주기적으로 업로드합니다. 데이터가 업로드된 후에만 대시보드에서 값이 업데이트됩니다. 업로드 간격은 기기 상태를 고려하며 네트워크 연결 품질에 따라 결정됩니다.

|네트워크 연결 품질 |    데이터 플러시 간격|
|---|---|
|우수    |10초|
|양호    |30초|
|불량    |60초|
{: .reset-td-br-1 .reset-td-br-2 aria-label="데이터 업로드 및 다운로드" }

네트워크 연결이 없는 경우, 네트워크 연결이 다시 설정될 때까지 데이터는 기기에 로컬로 캐시됩니다. 연결이 다시 설정되면 데이터가 Braze로 업로드됩니다.

Braze는 세션 시작 시 사용자가 해당 세션 시점에 속해 있는 Segment를 기반으로 SDK에 데이터를 전송합니다. 새로운 인앱 메시지는 세션 중에 업데이트되지 않습니다. 그러나 세션 중 사용자 데이터는 클라이언트에서 전송되는 대로 계속 처리됩니다. 예를 들어, 이탈한 사용자(7일 이상 앱을 사용하지 않은 사용자)는 앱에 복귀한 첫 번째 세션에서 이탈 사용자를 대상으로 한 콘텐츠를 계속 수신합니다.

## 데이터 수집 차단 {#blocking-data-collection}

SDK 통합에서 특정 데이터의 자동 수집을 차단하거나, 이를 수행하는 프로세스를 허용 목록에 추가하는 것이 가능합니다(권장하지는 않습니다).

데이터 수집을 차단하는 것은 권장되지 않습니다. 분석 데이터를 제거하면 플랫폼의 개인화 및 타겟팅 역량이 저하되기 때문입니다. 예를 들어:

- SDK 중 하나에서 위치 정보를 완전히 통합하지 않으면, 언어 또는 위치를 기반으로 메시징을 개인화할 수 없습니다.
- 시간대를 통합하지 않으면, 사용자의 시간대에 맞춰 메시지를 보내지 못할 수 있습니다.
- 특정 기기 시각 정보를 통합하지 않으면, 메시지 콘텐츠가 해당 기기에 최적화되지 않을 수 있습니다.

제품의 기능을 최대한 활용하려면 SDK를 완전히 통합하는 것을 적극 권장합니다.

{% tabs %}
{% tab Web SDK %}

SDK의 특정 부분을 통합하지 않거나, 사용자에 대해 [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk)를 사용할 수 있습니다. 이 메서드는 `disableSDK()`가 호출되기 전에 기록된 데이터를 동기화하며, 이후 이 페이지 및 향후 페이지 로드에서 Braze 웹 SDK에 대한 모든 후속 호출이 무시됩니다. 나중에 데이터 수집을 재개하려면 [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) 메서드를 사용할 수 있습니다. 자세한 내용은 [웹 추적 비활성화]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=web) 문서를 참조하세요.

{% endtab %}
{% tab Android SDK %}

[`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder)를 사용하여 설정된 허용 목록에 따라 기기 객체 키 또는 값의 하위 집합만 전송하도록 SDK를 구성할 수 있습니다. 이 기능은 [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder)를 통해 활성화해야 합니다.

{% alert important %}
빈 허용 목록을 설정하면 Braze로 기기 데이터가 **전혀** 전송되지 않습니다.
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

`Braze.Configuration`의 [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist)에 적격 필드 세트를 할당하여 SDK가 수집하는 기기 필드의 허용 목록을 지정할 수 있습니다. 전체 필드 목록은 [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty)에 정의되어 있습니다. 모든 기기 필드 수집을 해제하려면 이 속성의 값을 빈 세트(`[]`)로 설정하세요.

{% alert important %}
기본적으로 Braze Swift SDK는 모든 필드를 수집합니다. 일부 기기 속성을 제거하면 SDK 기능이 비활성화될 수 있습니다.
{% endalert %}

자세한 사용 방법은 Swift SDK 설명서의 [스토리지]({{site.baseurl}}/developer_guide/storage?tab=swift)를 참조하세요.

{% endtab %}
{% endtabs %}

## 어떤 버전의 SDK를 사용하고 있습니까? {#what-version-of-the-sdk-am-i-on}

대시보드에서 **설정 > 앱 설정**으로 이동하여 특정 앱의 SDK 버전을 확인할 수 있습니다. **실시간 SDK 버전**은 사용자의 5% 이상이 사용하는 최신 라이브 애플리케이션에서 사용된 가장 높은 Braze SDK 버전을 표시합니다.

![워크스페이스에 있는 Swifty라는 앱. 실시간 SDK 버전은 6.6.0입니다.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"}

{% alert tip %}
iOS 앱이 있는 경우, **실시간 SDK 버전**이 5.0.0 이상이면 레거시 [Objective-C iOS SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) 대신 [Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift)를 사용하고 있는 것입니다. 5.0.0은 Swift SDK의 첫 번째 릴리스 버전이었습니다.
{% endalert %}