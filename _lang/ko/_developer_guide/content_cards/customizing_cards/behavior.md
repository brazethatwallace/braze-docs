---
nav_title: 동작
article_title: Content Cards의 동작 커스터마이즈
page_order: 2
description: "이 구현 가이드에서는 Content Cards의 동작 변경, 페이로드에 키-값 페어와 같은 추가 항목 추가, 일반적인 커스터마이즈 레시피에 대해 설명합니다."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards의 동작 커스터마이즈 {#customize-the-behavior-of-content-cards}

> 이 구현 가이드에서는 Content Cards의 동작 변경, 페이로드에 키-값 페어와 같은 추가 항목 추가, 일반적인 커스터마이즈 레시피에 대해 설명합니다. 콘텐츠 카드 유형의 전체 목록은 [Content Cards 정보]({{site.baseurl}}/developer_guide/content_cards)를 참조하세요.

## 키-값 페어 {#key-value-pairs}

Braze를 사용하면 키-값 페어를 통해 Content Cards로 사용자 기기에 추가 데이터 페이로드를 전송할 수 있습니다. 이를 통해 내부 측정기준을 추적하고, 앱 콘텐츠를 업데이트하며, 속성정보를 커스텀할 수 있습니다. [대시보드를 사용하여 키-값 페어를 추가]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#step-4-configure-additional-settings-optional)하세요.

{% alert note %}
키-값 페어로 중첩된 JSON 값을 전송하는 것은 권장하지 않습니다. 대신 전송하기 전에 JSON을 평탄화하세요.
{% endalert %}

{% tabs %}
{% tab 웹 %}

키-값 페어는 <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> 객체에 `extras`로 저장됩니다. 이를 사용하여 카드와 함께 데이터를 전송하고 애플리케이션에서 추가 처리를 할 수 있습니다. 이 값에 접근하려면 `card.extras`를 호출하세요.

{% endtab %}
{% tab Android %}

키-값 페어는 <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> 객체에 `extras`로 저장됩니다. 이를 사용하여 카드와 함께 데이터를 전송하고 애플리케이션에서 추가 처리를 할 수 있습니다. 이 값에 접근하려면 <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> 를 호출하세요.

{% endtab %}
{% tab SWIFT %}

키-값 페어는 <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> 객체에 `extras`로 저장됩니다. 이를 사용하여 카드와 함께 데이터를 전송하고 애플리케이션에서 추가 처리를 할 수 있습니다. 이 값에 접근하려면 <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> 를 호출하세요.

{% endtab %}
{% endtabs %}

{% alert tip %}
마케팅 팀과 개발자 팀이 사용할 키-값 페어(예: `feed_type = brand_homepage`)에 대해 사전에 조율하는 것이 중요합니다. 마케터가 Braze 대시보드에 입력하는 키-값 페어는 개발자가 앱 로직에 구축한 키-값 페어와 정확히 일치해야 합니다.
{% endalert %}

## 보충 콘텐츠로서의 Content Cards {#content-cards-as-supplemental-content}

![로컬 데이터와 Braze Content Cards를 혼합한 하이브리드 리스트가 포함된 피드.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Content Cards를 기존 피드에 자연스럽게 통합하여 여러 피드의 데이터를 동시에 로드할 수 있습니다. 이를 통해 Braze Content Cards와 기존 피드 콘텐츠가 조화롭고 일관된 경험을 제공합니다.

함께 제공된 예시는 로컬 데이터와 Braze 기반 Content Cards로 채워진 항목의 하이브리드 리스트가 포함된 피드를 보여줍니다. 이 방식을 사용하면 Content Cards가 기존 콘텐츠와 구분되지 않을 정도로 자연스럽게 표시될 수 있습니다.

### API 트리거 키-값 페어 {#api-triggered-key-value-pairs}

[API 트리거 캠페인]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)은 카드의 값이 외부 요인에 따라 사용자에게 표시할 콘텐츠를 결정해야 하는 경우에 활용하기 좋은 전략입니다. 예를 들어, 보충 콘텐츠를 표시하려면 Liquid를 사용하여 키-값 페어를 설정합니다. `class_type`은 설정 시점에 미리 정해져 있어야 합니다.

![보충 Content Cards 사용 사례를 위한 키-값 페어. 이 예시에서는 "tile_id", "tile_deeplink", "tile_title"과 같은 카드의 다양한 요소가 Liquid를 사용하여 설정되어 있습니다.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## 인터랙티브 콘텐츠로서의 Content Cards {#content-cards-as-interactive-content}
![화면 왼쪽 하단에 50퍼센트 프로모션을 보여주는 인터랙티브 콘텐츠 카드. 클릭하면 장바구니에 프로모션이 적용됩니다.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Content Cards를 레버리지하여 사용자에게 동적이고 인터랙티브한 경험을 제공할 수 있습니다. 함께 제공된 예시에서는 결제 시 콘텐츠 카드 팝업이 나타나 사용자에게 막바지 프로모션을 제공합니다. 이처럼 적절한 위치에 배치된 카드는 사용자가 특정 행동을 취하도록 "넛지"를 주는 훌륭한 방법입니다.

이 사용 사례의 키-값 페어에는 원하는 할인 금액으로 설정된 `discount_percentage`와 `coupon_code`로 설정된 `class_type`이 포함됩니다. 이러한 키-값 페어를 사용하면 결제 화면에서 유형별 Content Cards를 필터링하고 표시할 수 있습니다. 키-값 페어를 사용하여 여러 피드를 관리하는 방법에 대한 자세한 내용은 [기본 콘텐츠 카드 피드 커스터마이징]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds)을 참조하세요.
<br>
<br>

![결제 프로모션을 보여주는 인터랙티브 콘텐츠 카드.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Content Cards 배지 {#content-card-badges}

![Swifty라는 이름의 Braze 샘플 앱이 표시된 iPhone 홈 화면으로, 숫자 7이 표시된 빨간색 배지가 보입니다]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

배지는 사용자의 주의를 끌기에 이상적인 작은 아이콘입니다. 배지를 사용하여 새로운 Content Cards 콘텐츠에 대해 사용자에게 알리면 사용자가 앱으로 다시 돌아오게 하고 세션을 늘릴 수 있습니다.

### 읽지 않은 Content Cards 수를 배지로 표시하기 {#displaying-the-number-of-unread-content-cards-as-a-badge}

읽지 않은 Content Cards 수를 앱 아이콘의 배지로 표시할 수 있습니다.

{% tabs %}
{% tab 웹 %}

다음을 호출하여 언제든지 읽지 않은 카드 수를 요청할 수 있습니다:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

그런 다음 이 정보를 사용하여 읽지 않은 Content Cards 수를 나타내는 배지를 표시할 수 있습니다. 자세한 내용은 <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDK 참조 문서</a> 를 확인하세요.

{% endtab %}
{% tab Android %}

다음을 호출하여 언제든지 읽지 않은 카드 수를 요청할 수 있습니다:

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

그런 다음 이 정보를 사용하여 읽지 않은 Content Cards 수를 나타내는 배지를 표시할 수 있습니다. 자세한 내용은 <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDK 참조 문서</a> 를 확인하세요.


{% endtab %}
{% tab SWIFT %}

다음 샘플은 `braze.contentCards`를 사용하여 읽지 않은 Content Cards 수를 요청하고 표시합니다. 앱이 닫히고 사용자의 세션이 종료된 후, 이 코드는 `viewed` 속성정보를 기반으로 카드 수를 필터링하여 카드 개수를 요청합니다.

[`UIScene` 생명 주기](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)를 채택한 앱([Xcode 27 이상](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)으로 빌드된 앱의 경우 필수)은 `AppDelegate.swift`의 `applicationDidEnterBackground(_:)` 대신 `SceneDelegate.swift`의 `sceneDidEnterBackground(_:)`에서 이를 구현해야 합니다.

{% subtabs %}
{% subtab Swift %}

```swift
func sceneDidEnterBackground(_ scene: UIScene)
```

이 메서드 내에서 다음 코드를 구현하면, 주어진 세션 동안 사용자가 카드를 볼 때 배지 수를 실시간으로 업데이트합니다:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)sceneDidEnterBackground:(UIScene *)scene
```

이 메서드 내에서 다음 코드를 구현하면, 주어진 세션 동안 사용자가 카드를 볼 때 배지 수를 실시간으로 업데이트합니다:

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}