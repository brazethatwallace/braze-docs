{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 기본 사용자 속성 {#default-user-attributes}

### 지원되는 속성 {#supported-attributes}

다음 속성은 `Braze.User` 오브젝트에 설정해야 합니다:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

### 기본 속성 설정 {#setting-default-attributes}

기본 사용자 속성을 설정하려면 공유 `Braze.User` 오브젝트에서 적절한 필드를 설정하세요. 다음은 이름 속성을 설정하는 예시입니다:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### 기본 속성 해제 {#unsetting-default-attributes}

기본 사용자 속성을 해제하려면 관련 메서드에 `nil`을 전달하세요.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## 커스텀 사용자 속성 {#custom-user-attributes}

기본 사용자 속성 외에도 Braze는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있도록 허용합니다. 각 속성의 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/analytics)을 참조하세요.

{% alert important %}
커스텀 속성 값의 최대 길이는 255자이며, 이를 초과하는 값은 잘립니다. 자세한 내용은 [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class)를 참조하세요.
{% endalert %}

### 커스텀 속성 설정 {#setting-custom-attributes}

{% tabs local %}
{% tab string %}
`string` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab integer %}
`integer` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab floating-points %}
Braze는 데이터베이스 내에서 `float`과 `double` 값을 동일하게 처리합니다. double 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab boolean %}
`boolean` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab date %}
`date` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab array %}
배열의 기본 및 최대 요소 개수는 500개입니다. Braze 대시보드의 **데이터 설정** > **커스텀 속성**에서 배열의 최대 개수를 업데이트할 수 있습니다. 최대 요소 개수를 초과하는 배열은 최대 요소 개수에 맞게 잘립니다.

`array` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 커스텀 속성 증가 또는 감소 {#incrementing-or-decrementing-custom-attributes}

이 코드는 커스텀 속성을 증가시키는 예시입니다. `integer` 또는 `long` 값만큼 커스텀 속성 값을 증가시킬 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### 커스텀 속성 해제 {#unsetting-custom-attributes}

{% tabs %}
{% tab swift %}
커스텀 속성을 해제하려면 관련 속성 키를 `unsetCustomAttribute` 메서드에 전달하세요.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
커스텀 속성을 해제하려면 관련 속성 키를 `unsetCustomAttributeWithKey` 메서드에 전달하세요.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### 중첩 커스텀 속성 {#nesting-custom-attributes}

커스텀 속성 내에 속성을 중첩할 수도 있습니다. 다음 예시에서는 중첩 속성이 포함된 `favorite_book` 오브젝트를 고객 프로필의 커스텀 속성으로 설정합니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)을 참조하세요.

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objective-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### REST API 사용 {#using-the-rest-api}

REST API를 사용하여 사용자 속성을 설정하거나 해제할 수도 있습니다. 자세한 내용은 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)를 참조하세요.

## 사용자 가입 설정 {#setting-user-subscriptions}

사용자의 가입(이메일 또는 푸시)을 설정하려면 각각 `set(emailSubscriptionState:)` 또는 `set(pushNotificationSubscriptionState:)` 함수를 호출하세요. 두 함수 모두 열거형 타입 `Braze.User.SubscriptionState`를 인수로 사용합니다. 이 타입에는 세 가지 상태가 있습니다:

| 가입 상태 | 정의 |
| ------------------- | ---------- |
| `optedIn` | 가입하였으며, 명시적으로 옵트인함 |
| `subscribed` | 가입하였으나, 명시적으로 옵트인하지 않음 |
| `unsubscribed` | 탈퇴하였거나 명시적으로 옵트아웃함 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 가입 설정" }

앱에 푸시 알림 전송 권한을 부여한 사용자는 iOS에서 명시적인 옵트인을 요구하므로 기본적으로 `optedIn` 상태로 설정됩니다.

사용자는 유효한 이메일 주소를 수신하면 자동으로 `subscribed`로 설정됩니다. 하지만 명시적인 옵트인 프로세스를 구축하고, 사용자로부터 명시적인 동의를 받았을 때 이 값을 `optedIn`으로 설정하는 것을 권장합니다. 자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/channels/email/subscriptions)를 참조하세요.

### 이메일 가입 설정 {#setting-email-subscriptions}

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### 푸시 알림 가입 설정 {#setting-push-notification-subscriptions}

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/channels/email/subscriptions)를 참조하세요.