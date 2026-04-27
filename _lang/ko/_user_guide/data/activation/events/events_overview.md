---
nav_title: 이벤트
article_title: 이벤트
page_order: 0
hidden: true
page_type: reference
description: "이 문서에서는 Braze의 다양한 이벤트(표준 이벤트, 구매 이벤트, 커스텀 이벤트)와 그 목적에 대해 설명합니다."
---

# 이벤트 {#events}

> 이 페이지에서는 Braze의 다양한 이벤트와 그 목적에 대해 다룹니다.

Braze는 사용자 동작과 브랜드 참여에 대한 포괄적인 이해를 제공하기 위해 몇 가지 이벤트 유형을 사용합니다. 각 이벤트 유형은 고유한 목적을 가지고 있습니다:

- [표준 이벤트](#standard-events): 앱 또는 사이트에 대한 사용자 참여의 기본적인 이해를 제공합니다.
- [구매 이벤트](#purchase-events): 사용자 구매 동작을 이해하고 매출을 추적하는 데 중요합니다.
- [커스텀 이벤트](#custom-events): 앱이나 비즈니스에 고유한 사용자 동작에 대한 더 깊은 인사이트를 제공합니다.

이러한 다양한 유형의 이벤트를 추적하면 사용자에 대한 더 깊은 이해를 얻을 수 있으며, 이를 통해 마케팅 전략을 수립하고, 앱을 최적화하며, 더 개인화된 사용자 경험을 제공할 수 있습니다. 자세히 살펴보겠습니다!

## 표준 이벤트 {#standard-events}

Braze에서 표준 이벤트는 플랫폼 전반에서 Braze가 인식하는 사전 정의된 동작입니다. [커스텀 이벤트](#custom-events)와 달리 표준 이벤트를 직접 생성하거나 이름을 지정할 필요가 없습니다. 기본으로 내장되어 있습니다. 다만, 모든 표준 이벤트가 동일한 방식으로 추적되는 것은 아닙니다.

다음 이벤트는 SDK 통합 후 자동으로 추적됩니다:

- 세션 시작
- 세션 종료

다음 이벤트는 추가 설정 후 추적됩니다:

- [구매 이벤트](#purchase-events): 개발팀이 SDK의 구매 메서드를 사용하여 기록합니다. 자세한 내용은 구매 이벤트 섹션을 참조하세요.
- 이메일 참여 이벤트(이메일 열기 및 링크 클릭 등): Braze 이메일을 구성하고 이메일 추적을 활성화하면 Braze에서 추적합니다.
- 푸시 참여 이벤트(푸시 알림 열기 및 클릭 등): Braze에서 푸시를 구성하고 앱에서 Braze SDK와 푸시 처리를 통합한 후 추적됩니다.

마케터로서 표준 이벤트를 사용하여 사용자 동작과 참여를 이해할 수 있습니다. 예를 들어, 세션 데이터는 사용자가 앱이나 사이트를 얼마나 자주 여는지 보여주고, 구매 이벤트는 시간에 따른 매출을 추적하는 데 도움이 됩니다.

## 구매 이벤트 {#purchase-events}

구매 이벤트는 사용자의 구매를 기록하고 추적합니다. Braze SDK를 통합한 후 개발팀이 SDK의 구매 메서드를 사용하여 구매를 기록할 수 있습니다. 구매 이벤트를 사용하여 구매를 추적하면 Braze에서 직접 시간에 따른 매출과 다양한 매출 소스를 모니터링할 수 있습니다.

구매 이벤트는 구매에 대한 다음 주요 정보를 기록합니다:

- 제품 ID(일반적으로 제품 이름 또는 카테고리)
- 통화
- 가격
- 수량

그런 다음 이 데이터를 사용하여 생애주기 가치, 구매 빈도, 특정 구매 등을 기반으로 사용자를 세그먼트할 수 있습니다.

Braze는 다중 통화 구매도 지원합니다. USD 이외의 통화로 구매가 보고된 경우, 구매가 보고된 날짜의 환율을 기준으로 Braze 대시보드에 USD로 표시됩니다.

자세한 내용은 전용 [구매 이벤트]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/) 문서를 참조하세요.

{% details 구현 예시 %}

구매 이벤트의 실제 구현에는 Braze SDK를 앱과 통합하는 과정이 포함되므로 기술적 지식이 필요합니다. 고객 성공 매니저가 온보딩의 일환으로 팀에게 이 과정을 안내해 드리지만, 일반적인 단계는 다음과 같습니다:

1. **Braze SDK 통합:** 이벤트를 기록하기 전에 Braze SDK를 앱에 통합해야 합니다.
2. **구매 이벤트 기록:** SDK가 통합된 후 사용자가 앱에서 구매할 때마다 구매 이벤트를 기록할 수 있습니다. 이는 일반적으로 구매가 완료될 때 호출되는 함수 또는 메서드에서 수행됩니다.

다음은 Swift를 사용하여 iOS 앱에서 구매 이벤트를 기록하는 예시입니다:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

이 예시에서 "product_name"은 구매한 제품의 이름이고, "USD"는 구매 통화이며, "1.99"는 제품 가격이고, "1"은 구매 수량입니다.

{:start="3"}
3. **Braze 대시보드에서 구매 이벤트 확인:** 구매 이벤트가 기록된 후 Braze 대시보드에서 확인할 수 있습니다. 이 데이터를 사용하여 매출을 분석하고, 사용자를 세그먼트하는 등의 작업을 수행할 수 있습니다.

실제 구현은 플랫폼(iOS, Android, 웹)과 앱의 특정 요구 사항에 따라 다를 수 있습니다.

{% enddetails %}

## 커스텀 이벤트 {#custom-events}

커스텀 이벤트는 앱이나 사이트 내에서 추적하려는 특정 동작을 기반으로 정의하는 이벤트입니다. Braze는 이를 자동으로 추적하지 않으므로 Braze SDK 구현에서 이러한 이벤트를 수동으로 설정해야 합니다. 커스텀 이벤트는 사용자가 게임에서 레벨을 완료하는 것부터 프로필 정보를 업데이트하는 것까지 다양할 수 있습니다.

다음은 Swift를 사용하여 iOS 앱에서 커스텀 이벤트를 기록하는 예시입니다:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

이 예시에서 "completed_level"은 사용자가 게임에서 레벨을 완료할 때 기록되는 커스텀 이벤트의 이름입니다. 해당 커스텀 이벤트는 Braze의 고객 프로필에 기록되며, 이를 사용하여 Campaign을 트리거하고 메시징을 개인화할 수 있습니다.

자세한 내용은 전용 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) 문서를 참조하세요.

{% details 구현 예시 %}

구매 이벤트와 마찬가지로 커스텀 이벤트도 추가 설정이 필요합니다. Braze에서 커스텀 이벤트를 구현하는 일반적인 과정은 다음과 같습니다:

1. **Braze SDK 통합:** 이벤트를 기록하기 전에 Braze SDK를 앱에 통합해야 합니다.
2. **커스텀 이벤트 정의:** 앱에서 커스텀 이벤트로 추적할 동작을 결정합니다. 사용자가 게임에서 레벨을 완료하거나, 프로필을 업데이트하거나, 특정 유형의 구매를 하는 등 앱에 중요한 모든 동작이 될 수 있습니다.
3. **커스텀 이벤트 기록:** 커스텀 이벤트를 정의한 후 앱 코드에서 기록할 수 있습니다. 이는 일반적으로 해당 동작이 발생할 때 호출되는 함수 또는 메서드에서 수행됩니다.

다음은 Swift를 사용하여 iOS 앱에서 커스텀 이벤트를 기록하는 예시입니다:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

이 예시에서 "updated_profile"은 사용자가 프로필을 업데이트할 때 기록되는 커스텀 이벤트의 이름입니다.

{:start="4"}
4. **커스텀 이벤트에 등록정보 추가(선택 사항):** 커스텀 이벤트에 대한 추가 세부 정보를 캡처하려면 등록정보를 추가할 수 있습니다. 이벤트를 기록할 때 등록정보 사전을 전달하여 수행합니다.

다음은 Swift를 사용하여 iOS 앱에서 등록정보가 포함된 커스텀 이벤트를 기록하는 예시입니다:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

이 예시에서 커스텀 이벤트에는 "Property Name"이라는 등록정보가 있으며 값은 "Property Value"입니다.

{:start="5"}
5. **Braze 대시보드에서 커스텀 이벤트 확인:** 커스텀 이벤트가 기록된 후 Braze 대시보드에서 확인할 수 있습니다. 이 데이터를 사용하여 사용자 동작을 분석하고, 사용자를 세그먼트하는 등의 작업을 수행할 수 있습니다.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->