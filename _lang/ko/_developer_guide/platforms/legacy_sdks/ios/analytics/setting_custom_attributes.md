---
nav_title: Set 커스텀 속성
article_title: iOS용 커스텀 속성 설정
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 애플리케이션에서 커스텀 속성을 설정하는 방법을 보여줍니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS용 커스텀 속성 설정 {#set-custom-attributes-for-ios}

Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

구현하기 전에 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예시를 [모범 사례]({{site.baseurl}}/developer_guide/analytics)에서 검토하고, [이벤트 명명 규칙]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)에 대한 참고 사항도 확인하세요.

## 기본 사용자 속성 할당하기 {#assigning-default-user-attributes}

사용자 속성을 할당하려면 공유 `ABKUser` 객체에서 적절한 필드를 설정해야 합니다.

다음은 이름 속성을 설정하는 예시입니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

다음 속성은 `ABKUser` 객체에서 설정해야 합니다:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `userID`
- `gender`

## 커스텀 사용자 속성 할당하기 {#assigning-custom-user-attributes}

기본 사용자 속성 외에도 Braze에서는 다양한 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있습니다. 각 속성이 제공하는 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/analytics)을 참조하세요.

### 문자열 값을 가진 커스텀 속성 {#custom-attribute-with-a-string-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### 정수 값을 가진 커스텀 속성 {#custom-attribute-with-an-integer-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### 더블 값을 가진 커스텀 속성 {#custom-attribute-with-a-double-value}

Braze는 데이터베이스 내에서 `float` 값과 `double` 값을 동일하게 처리합니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### 부울 값을 가진 커스텀 속성 {#custom-attribute-with-a-boolean-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### 날짜 값을 가진 커스텀 속성 {#custom-attribute-with-a-date-value}

이 메서드를 사용하여 Braze에 전달하는 날짜는 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식(예: `2013-07-16T19:20:30+01:00`) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식(`2016-12-14T13:32:31.601-0800`)이어야 합니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### 배열 값을 가진 커스텀 속성 {#custom-attribute-with-an-array-value}

배열의 기본 및 최대 요소 개수는 500개입니다. Braze 대시보드의 **데이터 설정** > **커스텀 속성**에서 배열의 최대 요소 개수를 업데이트할 수 있습니다. 최대 요소 개수를 초과하는 배열은 최대 요소 개수만큼 잘립니다.


{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[[Appboy sharedInstance].user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
Appboy.sharedInstance()?.user.setCustomAttributeArrayWithKey("array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
Appboy.sharedInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Removing a value from an array type custom attribute
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", value: "value2")
```

{% endtab %}
{% endtabs %}

### 커스텀 속성 해제하기 {#unsetting-a-custom-attribute}

커스텀 속성은 다음 메서드를 사용하여 해제할 수도 있습니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### 커스텀 속성 증가/감소 {#incrementingdecrementing-custom-attributes}

이 코드는 커스텀 속성을 증가시키는 예시입니다. 커스텀 속성 값을 양의 정수, 음의 정수 또는 long 값만큼 증가시킬 수 있습니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### REST API를 통한 커스텀 속성 설정 {#setting-a-custom-attribute-via-the-rest-api}

REST API를 사용하여 사용자 속성을 설정할 수도 있습니다. 자세한 내용은 [사용자 API 설명서]({{site.baseurl}}/api/endpoints/user_data)를 참조하세요.

### 커스텀 속성 값 제한 {#custom-attribute-value-limits}

커스텀 속성 값의 최대 길이는 255자이며, 이를 초과하는 값은 잘립니다.

#### 추가 정보 {#additional-information}

- 자세한 내용은 [`ABKUser.h` 파일](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)에서 확인할 수 있습니다.
- 자세한 내용은 [`ABKUser` 설명서](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html)를 참조하세요.

## 사용자 가입 설정 {#setting-up-user-subscriptions}

사용자 가입(이메일 또는 푸시)을 설정하려면 각각 `setEmailNotificationSubscriptionType` 또는 `setPushNotificationSubscriptionType` 함수를 호출합니다. 이 두 함수 모두 열거형 타입 `ABKNotificationSubscriptionType`을 인수로 사용합니다. 이 타입에는 세 가지 상태가 있습니다:

| 가입 상태 | 정의 |
| ------------------- | ---------- |
| `ABKOptedin` | 가입 완료, 명시적으로 옵트인 |
| `ABKSubscribed` | 가입 완료, 명시적으로 옵트인하지 않음 |
| `ABKUnsubscribed` | 탈퇴 및/또는 명시적으로 옵트아웃 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 가입 설정" }

앱에 푸시 알림 전송 권한을 부여한 사용자는 기본적으로 `ABKOptedin` 상태로 설정됩니다. iOS에서는 명시적 옵트인이 필요하기 때문입니다.

사용자는 유효한 이메일 주소를 수신하면 자동으로 `ABKSubscribed`로 설정됩니다. 그러나 명시적 옵트인 프로세스를 구축하고 사용자의 명시적 동의를 받은 후 이 값을 `OptedIn`으로 설정하는 것을 권장합니다. 자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/channels/email/subscriptions)를 참조하세요.

### 이메일 가입 설정 {#setting-email-subscriptions}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### 푸시 알림 가입 설정 {#setting-push-notification-subscriptions}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/channels/email/subscriptions)를 참조하세요.