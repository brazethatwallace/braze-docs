---
nav_title: 커스텀 이벤트 기록
article_title: 커스텀 이벤트 기록
page_order: 3.1
description: "Braze SDK를 통해 커스텀 이벤트를 기록하는 방법을 알아보세요."
---

# 커스텀 이벤트 기록 {#log-custom-events}

> Braze SDK를 통해 커스텀 이벤트를 기록하는 방법을 알아보세요.

{% alert note %}
목록에 없는 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

이커머스 권장 이벤트에 대해서는 [이커머스 이벤트 기록]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)을 참조하세요.

## 커스텀 이벤트 로깅하기 {#logging-a-custom-event}

커스텀 이벤트를 로깅하려면 다음 이벤트 로깅 메서드를 사용합니다.

{% tabs %}
{% tab 웹 %}
표준 웹 SDK 구현의 경우 다음 메서드를 사용할 수 있습니다:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Google Tag Manager를 대신 사용하려면 **커스텀 이벤트** 태그 유형을 사용하여 [`logCustomEvent` 메서드](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)를 호출하고 커스텀 이벤트를 Braze로 전송할 수 있으며, 선택적으로 커스텀 이벤트 속성정보를 포함할 수 있습니다. 이를 위해 다음을 수행합니다:

1. 변수를 사용하거나 이벤트 이름을 직접 입력하여 **이벤트 이름**을 입력합니다.
2. **행 추가** 버튼을 사용하여 이벤트 속성정보를 추가합니다.

![Braze 액션 태그 구성 설정을 보여주는 대화 상자. 포함된 설정은 '태그 유형'(커스텀 이벤트), '이벤트 이름'(버튼 클릭) 및 '이벤트 속성정보'입니다.]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab Android %}
네이티브 Android의 경우 다음 메서드를 사용할 수 있습니다:

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab Cordova %}
Braze Cordova 플러그인 메서드를 사용합니다:

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

`logCustomEvent` API는 다음을 허용합니다:
- `eventName` (필수 문자열): 최대 255자까지 사용합니다. 이름을 `$`로 시작하지 마세요. 영숫자 문자와 구두점을 사용합니다.
- `eventProperties` (선택적 객체): 이벤트 메타데이터를 위한 키-값 페어를 추가합니다. 키는 최대 255자까지 사용하며, 키를 `$`로 시작하지 마세요.

속성정보 값에는 `string`(최대 255자), `numeric`, `boolean`, 배열 또는 중첩된 JSON 객체를 사용합니다.

구현 세부 사항은 Braze Cordova SDK 소스를 참조하세요:
- [`www/BrazePlugin.js` `logCustomEvent` 메서드 (138-140행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [`www/BrazePlugin.js` JSDoc (128-140행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Android 핸들러 `src/android/BrazePlugin.kt` (108-115행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [iOS 핸들러 `src/ios/BrazePlugin.m` (308-313행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [iOS 메서드 선언 `src/ios/BrazePlugin.h` (24행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
{% endtab %}

{% tab infillion %}
Android 앱에 [Infillion Beacons](https://infillion.com/software/beacons/)를 통합한 경우, 선택적으로 `visit.getPlace()`를 사용하여 위치별 이벤트를 로깅할 수 있습니다. `requestImmediateDataFlush`는 앱이 백그라운드에 있더라도 이벤트가 로깅되도록 보장합니다.

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## 메타데이터 속성정보 추가하기 {#adding-metadata-properties}

커스텀 이벤트를 기록할 때 이벤트와 함께 속성정보 객체를 전달하여 해당 커스텀 이벤트에 대한 메타데이터를 추가할 수 있습니다. 속성정보는 키-값 페어로 정의됩니다. 키는 문자열이며, 값은 `string`, `numeric`, `boolean`, [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) 객체, 배열 또는 중첩된 JSON 객체가 될 수 있습니다.

메타데이터 속성정보를 추가하려면 다음 이벤트 로깅 메서드를 사용합니다.

{% tabs %}
{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can",
  pass: false,
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab cordova %}
속성정보 객체와 함께 커스텀 이벤트를 기록합니다:

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

인라인으로 속성정보를 전달할 수도 있습니다:

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

공식 Cordova 샘플 앱에는 문자열, 숫자, 불리언, 배열 및 중첩 객체 속성정보가 포함되어 있습니다:
- [`sample-project/www/js/index.js` (230-251행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

샘플 프로젝트 발췌:

```javascript
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
  "Cart Value": 4.95,
  "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
  "array key": [1, "2", false],
  "object key": {
    "k1": "1",
    "k2": 2,
    "k3": false,
  },
  "deep key": {
    "key": [1, "2", true]
  }
});
```

API 및 네이티브 브릿지에 대한 자세한 내용은 다음을 참조하세요:
- [`www/BrazePlugin.js` JSDoc (128-140행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [`src/android/BrazePlugin.kt`의 Android 핸들러 (108-115행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [`src/ios/BrazePlugin.m`의 iOS 핸들러 (308-313행)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
`time` 및 `event_name` 키는 예약되어 있으며 커스텀 이벤트 속성정보로 사용할 수 없습니다.
{% endalert %}

## 모범 사례 {#best-practices}

커스텀 이벤트 속성정보가 예상대로 기록되도록 하기 위해 수행해야 할 세 가지 중요한 확인 사항이 있습니다:

* [기록되는 이벤트 확인](#verify-events)
* [로그 확인](#verify-log)
* [값 확인](#verify-values)

커스텀 이벤트가 기록될 때마다 여러 속성정보가 함께 기록될 수 있습니다.

### 이벤트 확인 {#verify-events}

개발자에게 어떤 이벤트 속성정보가 추적되고 있는지 확인하세요. 모든 이벤트 속성정보는 대소문자를 구분한다는 점에 유의하세요. 커스텀 이벤트 추적에 대한 자세한 내용은 플랫폼에 따라 다음 문서를 참조하세요:

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
* [웹]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### 로그 확인 {#verify-log}

이벤트 속성정보가 성공적으로 추적되고 있는지 확인하려면 **커스텀 이벤트** 페이지에서 모든 이벤트 속성정보를 조회할 수 있습니다.

1. **데이터 설정** > **커스텀 이벤트**로 이동합니다.
2. 목록에서 해당 커스텀 이벤트를 찾습니다.
3. 해당 이벤트에서 **속성정보 관리**를 선택하여 이벤트에 연결된 속성정보의 이름을 확인합니다.

### 값 확인 {#verify-values}

[사용자를 테스트 사용자로 추가]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)한 후, 다음 단계에 따라 값을 확인합니다:

1. 앱 내에서 해당 커스텀 이벤트를 수행합니다.
2. 데이터가 전송될 때까지 약 10초간 기다립니다.
3. [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)를 새로고침하여 커스텀 이벤트와 함께 전달된 이벤트 속성정보 값을 확인합니다.

## 커스텀 이벤트 문제 해결 {#troubleshooting-custom-events}

다음 시나리오를 활용하여 SDK 전반의 커스텀 이벤트 로깅 문제를 해결하세요.

### 커스텀 이벤트 트리거 확인 {#verifying-the-custom-event-trigger}

커스텀 이벤트가 나타나지 않는 경우, 앱에서 추적 중인 액션이 테스트하려는 액션과 일치하지 않을 수 있습니다.

- 개발자 팀에 어떤 앱 액션이 커스텀 이벤트를 트리거하는지 확인하세요.
- SDK 업그레이드 후 `braze` 대신 `appboy`를 참조하는 등 더 이상 사용되지 않는 코드 경로가 있는지 확인하세요.

### 익명 프로필에 커스텀 이벤트가 로깅되는 경우 {#custom-events-are-logged-to-an-anonymous-profile}

커스텀 이벤트를 로깅하기 전에 사용자를 식별하지 않으면, Braze가 해당 이벤트를 익명 프로필에 연결할 수 있습니다.

- 커스텀 이벤트를 수행하기 전에 `changeUser()`를 호출하여 Braze가 식별된 고객 프로필에 이벤트를 로깅하도록 하세요.
- 식별된 테스트 사용자로 테스트한 후 [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)를 확인하세요.

### 커스텀 이벤트 로깅 설정 확인 {#verifying-custom-event-logging-setup}

커스텀 이벤트가 예상대로 나타나지 않는 경우, 개발자 팀이 올바른 앱 액션에 대해 커스텀 이벤트 로깅을 구현했는지 확인하세요.

- 개발자 팀에 이벤트가 올바르게 로깅되고 예상된 사용자 액션에서 트리거되는지 확인을 요청하세요.
- 팀이 Braze 지원팀에 티켓을 접수할 때 [상세 로그]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)와 관련 코드 스니펫을 포함하세요.
- 앱이 Swift 또는 Android를 사용하는 경우, 개발자 팀이 [SDK 디버거 사전 요구 사항]({{site.baseurl}}/developer_guide/sdk_integration/debugging#prerequisites)을 활용하여 상세 로그를 생성할 수 있습니다.
- 개발자 팀이 문제를 파악할 수 없는 경우, [Braze 지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 접수하세요.