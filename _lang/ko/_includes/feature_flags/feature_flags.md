# 기능 플래그 {#feature-flags}

> 기능 플래그를 사용하면 특정 사용자나 무작위로 선택한 사용자에 대해 원격으로 기능을 활성화 또는 비활성화할 수 있습니다. 중요한 점은 추가 코드 배포나 앱 스토어 업데이트 없이 프로덕션 환경에서 기능을 켜고 끌 수 있다는 것입니다. 이를 통해 새로운 기능을 안심하고 안전하게 출시할 수 있습니다.

{% alert tip %}
나만의 기능 플래그를 만들 준비가 되었다면 [기능 플래그 생성]({{site.baseurl}}/developer_guide/feature_flags/create)을 참조하세요.
{% endalert %}

## 전제 조건 {#prerequisites}

기능 플래그를 사용하기 위해 필요한 최소 SDK 버전은 다음과 같습니다:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## 사용 사례 {#use-cases}

### 점진적 출시 {#gradual-rollouts}

기능 플래그를 사용하여 샘플 모집단에 점진적으로 기능을 활성화할 수 있습니다. 예를 들어, VIP 사용자에게 먼저 새로운 기능을 소프트 런칭할 수 있습니다. 이 전략은 모든 사용자에게 한꺼번에 새로운 기능을 배포하는 것과 관련된 위험을 완화하고 초기에 버그를 발견하는 데 도움이 됩니다.

![출시 트래픽 슬라이더가 0%에서 100%로 이동하는 애니메이션 이미지.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

예를 들어, 더 빠른 고객 서비스를 위해 앱에 새로운 "실시간 채팅 지원" 링크를 추가하기로 결정했다고 가정해 보겠습니다. 이 기능을 모든 고객에게 한꺼번에 출시할 수도 있습니다. 그러나 대규모 출시에는 다음과 같은 위험이 따릅니다:

* 지원팀이 아직 교육 중인데 출시 후 고객이 지원 티켓을 생성하기 시작합니다. 지원팀에 추가 시간이 필요한 경우를 대비한 여유가 없습니다.
* 새로운 지원 사례의 실제 볼륨을 확신할 수 없으므로 적절한 인력을 배치하지 못할 수 있습니다.
* 지원팀이 과부하 상태에 빠지면 이 기능을 빠르게 다시 끄는 전략이 없습니다.
* 채팅 위젯에 버그가 있을 수 있으며, 고객에게 부정적인 경험을 제공하고 싶지 않습니다.

Braze 기능 플래그를 사용하면 기능을 점진적으로 출시하여 이러한 모든 위험을 완화할 수 있습니다:

* 지원팀이 준비가 되었다고 말하면 "실시간 채팅 지원" 기능을 활성화합니다.
* 적절한 인력을 배치했는지 확인하기 위해 10%의 사용자에게만 이 새로운 기능을 활성화합니다.
* 버그가 있는 경우 새 릴리스를 서둘러 배포하는 대신 기능을 빠르게 비활성화할 수 있습니다.

이 기능을 점진적으로 출시하기 위해 "Live Chat Widget"이라는 이름으로 [기능 플래그를 생성]({{site.baseurl}}/developer_guide/feature_flags/create)할 수 있습니다.

![Live Chat Widget이라는 이름의 기능 플래그 상세 정보 예시. ID는 enable_live_chat이고, 기능 플래그 설명에는 실시간 채팅 위젯이 지원 페이지에 표시된다고 적혀 있습니다.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

앱 코드에서 Braze 기능 플래그가 활성화된 경우에만 **실시간 채팅 시작** 버튼을 표시합니다:

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

{% alert note %}
`braze.featureFlags.featureFlags` 또는 `braze.featureFlags.featureFlag(id:)`를 읽으면 SDK가 초기화 후 작업을 완료할 때까지 호출 스레드가 차단됩니다. 메인 스레드 또는 지연에 민감한 컨텍스트에서는 대신 [`getAllFeatureFlags(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/getallfeatureflags(_:))를 사용하세요.

```swift
// Non-blocking — completion handler always delivers on the main thread.
braze.featureFlags.getAllFeatureFlags { flags in
  let liveChatEnabled = flags.first(where: { $0.id == "enable_live_chat" })?.enabled ?? false
  liveChatView.isHidden = !liveChatEnabled
}
```

Objective-C의 경우:

```objc
[braze.featureFlags getAllFeatureFlagsWithCompletion:^(NSArray<BRZFeatureFlag *> *flags) {
  // Use `flags` here.
}];
```
{% endalert %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### 앱 변수 원격 제어 {#remotely-control-app-variables}

기능 플래그를 사용하여 프로덕션 환경에서 앱의 기능을 수정할 수 있습니다. 이는 앱 스토어 승인으로 인해 모든 사용자에게 빠르게 변경 사항을 배포하기 어려운 모바일 앱에서 특히 중요합니다.

예를 들어, 마케팅 팀이 앱의 내비게이션에 현재 세일 및 프로모션을 표시하고 싶다고 가정해 보겠습니다. 일반적으로 엔지니어링 팀은 변경 사항에 1주일의 리드 타임이 필요하고 앱 스토어 리뷰에 3일이 소요됩니다. 그런데 추수감사절, 블랙 프라이데이, 사이버 먼데이, 하누카, 크리스마스, 새해 첫날이 모두 두 달 안에 몰려 있으므로 이러한 빠듯한 일정을 맞추기 어렵습니다.

기능 플래그를 사용하면 Braze가 앱 내비게이션 링크의 콘텐츠를 제공할 수 있어, 마케팅 매니저가 며칠이 아닌 몇 분 만에 변경할 수 있습니다.

이 기능을 원격으로 설정하기 위해 `navigation_promo_link`라는 새 기능 플래그를 생성하고 다음 초기 속성정보를 정의합니다:

![일반 세일 페이지로 연결되는 링크 및 텍스트 속성정보가 있는 기능 플래그.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

앱에서 Braze의 getter 메서드를 사용하여 이 기능 플래그의 속성정보를 검색하고 해당 값을 기반으로 내비게이션 링크를 구축합니다:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

이제 추수감사절 전날, Braze 대시보드에서 해당 속성정보 값을 변경하기만 하면 됩니다.

![추수감사절 세일 페이지로 연결되는 링크 및 텍스트 속성정보가 있는 기능 플래그.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

결과적으로 다음에 누군가 앱을 로드하면 새로운 추수감사절 딜을 볼 수 있습니다.

### 메시지 조율 {#message-coordination}

기능 플래그를 사용하여 기능의 출시와 메시징을 동기화하고 제품팀과 마케팅 팀 간의 협업을 강화할 수 있습니다. 기능 플래그를 통해 기능 출시와 메시징을 조율하면 두 팀 모두 전략을 일치시키고 일관된 사용자 경험을 만들 수 있습니다.

예를 들어, 사용자를 위한 새로운 로열티 리워드 프로그램을 출시한다고 가정해 보겠습니다. 마케팅 팀과 제품팀이 프로모션 메시징의 타이밍을 기능 출시와 완벽하게 맞추기 어려울 수 있습니다. 그러나 Canvas의 기능 플래그를 사용하면 제품팀이 정교한 로직을 적용하여 특정 오디언스에 기능을 활성화하는 동시에 마케팅 팀이 동일한 사용자에게 관련 메시징을 관리할 수 있습니다.

기능 출시와 메시징을 효과적으로 조율하기 위해 `show_loyalty_program`이라는 새 기능 플래그를 생성합니다. 초기 단계적 출시에서는 Canvas가 기능 플래그의 활성화 시점과 대상을 제어하도록 합니다. 지금은 출시 비율을 0%로 두고 타겟 Segments를 선택하지 않습니다.

![Loyalty Rewards Program이라는 이름의 기능 플래그. ID는 show_loyalty_program이고, 설명에는 이 기능이 홈 화면과 프로필 페이지에 새로운 로열티 리워드 프로그램을 표시한다고 적혀 있습니다.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

그런 다음 Canvas에서 "고가치 고객" Segment에 대해 `show_loyalty_program` 기능 플래그를 활성화하는 [기능 플래그 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags)를 생성합니다:

![고가치 고객 Segment가 show_loyalty_program 기능 플래그를 활성화하는 오디언스 분할 단계가 포함된 Canvas 예시.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

이제 이 Segment의 사용자는 새로운 로열티 프로그램을 보기 시작하며, 활성화 후에는 이메일과 설문조사가 자동으로 발송되어 팀이 피드백을 수집하는 데 도움이 됩니다.

### 기능 실험 {#feature-experimentation}

기능 플래그를 사용하여 새로운 기능에 대한 가설을 실험하고 확인할 수 있습니다. 트래픽을 둘 이상의 그룹으로 나누면 그룹 간 기능 플래그의 영향을 비교하고 결과를 기반으로 최선의 조치를 결정할 수 있습니다.

기능 플래그 실험에서는 총 최대 9개 그룹을 사용할 수 있습니다: 하나의 대조군과 최대 8개의 배리언트.

[A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)는 변수의 여러 버전에 대한 사용자 반응을 비교하는 강력한 도구입니다.

이 예시에서 우리 팀은 이커머스 앱에 새로운 결제 흐름을 구축했습니다. 사용자 경험이 개선되고 있다고 확신하지만, 앱 매출에 미치는 영향을 측정하기 위해 A/B 테스트를 실행하고자 합니다.

시작하기 위해 `enable_checkout_v2`라는 새 기능 플래그를 생성합니다. 오디언스나 출시 비율을 추가하지 않습니다. 대신 기능 플래그 실험을 사용하여 트래픽을 분할하고, 기능을 활성화하며, 결과를 측정합니다.

앱에서 기능 플래그가 활성화되었는지 확인하고 응답에 따라 결제 흐름을 전환합니다:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

A/B 테스트를 [기능 플래그 실험]({{site.baseurl}}/developer_guide/feature_flags/experiments)에서 설정합니다.

이제 50%의 사용자에게는 기존 경험이 표시되고, 나머지 50%에게는 새로운 경험이 표시됩니다. 그런 다음 두 배리언트를 분석하여 어떤 결제 흐름이 더 높은 전환율을 달성했는지 확인할 수 있습니다. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![트래픽을 50% 두 그룹으로 나누는 기능 플래그 실험.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

위닝 배리언트를 결정한 후, 이 Campaign을 중지하고 엔지니어링 팀이 다음 앱 릴리스에 하드 코딩하는 동안 기능 플래그의 출시 비율을 모든 사용자에 대해 100%로 높일 수 있습니다.

### 세분화 {#segmentation}

**기능 플래그** 필터를 사용하여 기능 플래그가 활성화된 사용자를 기반으로 Segment를 생성하거나 메시징 대상을 지정할 수 있습니다. 예를 들어, 앱에서 프리미엄 콘텐츠를 제어하는 기능 플래그가 있다고 가정해 보겠습니다. 기능 플래그가 활성화되지 않은 사용자를 필터링하는 Segment를 생성한 다음, 해당 Segment에 프리미엄 콘텐츠를 보기 위해 계정을 업그레이드하도록 권유하는 메시지를 보낼 수 있습니다.

1. Segment 또는 메시지 오디언스를 엽니다.
2. **기능 플래그** 필터를 추가합니다.
3. 기능 플래그를 선택합니다.
4. 기능 플래그가 활성화된 사용자를 포함하려면 비교 연산자를 **is**로 설정하고, 활성화되지 않은 사용자를 포함하려면 **is not**으로 설정합니다.
![기능 플래그 활성화 값 필터를 사용하는 Braze Segment 빌더.]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Segments의 필터링에 대한 자세한 내용은 [Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)을 참조하세요.

{% alert note %}
재귀적 Segments를 방지하기 위해 다른 기능 플래그를 참조하는 Segment는 생성할 수 없습니다.
{% endalert %}

## 플랜 제한 사항 {#plan-limitations}

다음은 무료 및 유료 플랜의 기능 플래그 제한 사항입니다.

| 기능                                                                                                   | 무료 버전     | 유료 버전      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [활성 기능 플래그](#active-feature-flags)                                                                     | 워크스페이스당 10개 | 워크스페이스당 110개 |
| [활성 Campaign 실험]({{site.baseurl}}/developer_guide/feature_flags/experiments)          | 워크스페이스당 1개  | 워크스페이스당 100개 |
| [기능 플래그 캔버스 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) | 무제한        | 무제한         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="플랜 제한 사항" }

다음 조건 중 하나라도 해당되면 기능 플래그는 활성 상태로 간주되며 한도에 포함됩니다:

- 출시 비율이 0%를 초과하는 경우
- 활성 Canvas에서 사용 중인 경우
- 활성 실험에서 사용 중인 경우

동일한 기능 플래그가 여러 조건에 해당하더라도(예: Canvas에서 사용 중이면서 출시 비율이 50%인 경우), 한도에서 활성 기능 플래그 1개로만 계산됩니다.

{% alert note %}
유료 버전의 기능 플래그를 구매하려면 Braze 계정 매니저에게 문의하거나, Braze 대시보드에서 업그레이드를 요청하세요.
{% endalert %}