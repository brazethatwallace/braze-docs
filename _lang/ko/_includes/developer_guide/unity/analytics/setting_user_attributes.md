{% multi_lang_include developer_guide/prerequisites/unity.md %}

## 기본 사용자 속성 {#default-user-attributes}

### 미리 정의된 메서드 {#predefined-methods}

Braze는 `BrazeBinding` 오브젝트를 사용하여 다음 사용자 속성을 설정하기 위한 미리 정의된 메서드를 제공합니다. 자세한 내용은 [Braze Unity 선언 파일](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)을 참조하세요.

- 이름
- 성
- 사용자 이메일
- 성별
- 생년월일
- 사용자 국가
- 사용자 거주 도시
- 사용자 이메일 가입
- 사용자 푸시 가입
- 사용자 전화번호

### 기본 속성 설정 {#setting-default-attributes}

기본 속성을 설정하려면 `BrazeBinding` 오브젝트에서 관련 메서드를 호출하세요.

{% tabs local %}
{% tab First name %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Last name %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab Email %}
```csharp
BrazeBinding.SetUserEmail("user@example.com");
```
{% endtab %}
{% tab Gender %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Birth date %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab Country %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Home city %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Email subscription %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Push subscription %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Phone number %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### 기본 속성 해제 {#unsetting-default-attributes}

기본 사용자 속성을 해제하려면 관련 메서드에 `null`을 전달하세요.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## 커스텀 사용자 속성 {#custom-user-attributes}

기본 사용자 속성 외에도 Braze는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있도록 허용합니다. 각 속성의 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/analytics)을 참조하세요.

### 커스텀 속성 설정 {#setting-custom-attributes}

커스텀 속성을 설정하려면 속성 유형에 해당하는 메서드를 사용하세요:

{% tabs %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Integer %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Float %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom float attribute key", 'float value');
```

{% endtab %}

{% tab Boolean %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Braze에 전달되는 날짜는 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식(예: `2013-07-16T19:20:30+01:00`) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식(예: `2016-12-14T13:32:31.601-0800`)이어야 합니다.
{% endalert %}

{% endtab %}

{% tab Array %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}

{% tab 중첩 오브젝트 %}

중첩 오브젝트를 포함하는 커스텀 속성을 설정할 수 있습니다(Unity SDK 5.1.0 이상에서 사용 가능). 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)을 참조하세요.
다음 예제에서는 중첩 오브젝트 속성을 설정하고, 기존 오브젝트에 업데이트를 병합하고, 중첩 오브젝트 배열을 설정하는 방법을 보여줍니다.

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>));
```

기존 중첩 오브젝트를 업데이트하려면 merge 매개변수를 사용하세요:

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>), merge(bool));
```

중첩 오브젝트 배열을 설정할 수도 있습니다:

```csharp
AppboyBinding.SetCustomUserAttribute("custom object array attribute key", list(List<Dictionary<string, object>>));
```

{% endtab %}
{% endtabs %}

{% alert important %}
커스텀 속성 값의 최대 길이는 255자이며, 이를 초과하는 값은 잘립니다.
{% endalert %}

### 커스텀 속성 해제 {#unsetting-custom-attributes}

커스텀 속성을 해제하려면 관련 속성 키를 `UnsetCustomUserAttribute` 메서드에 전달하세요.

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### REST API 사용 {#using-the-rest-api}

REST API를 사용하여 사용자 속성을 설정하거나 해제할 수도 있습니다. 자세한 내용은 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)를 참조하세요.

## 사용자 가입 설정 {#setting-user-subscriptions}

사용자의 이메일 또는 푸시 가입을 설정하려면 다음 함수 중 하나를 호출하세요.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

두 함수 모두 `Appboy.Models.AppboyNotificationSubscriptionType`을 인수로 사용하며, 세 가지 상태가 있습니다:

| 가입 상태 | 정의 |
| ------------------- | ---------- |
| `OPTED_IN` | 가입 상태이며, 명시적으로 옵트인함 |
| `SUBSCRIBED` | 가입 상태이지만, 명시적으로 옵트인하지 않음 |
| `UNSUBSCRIBED` | 탈퇴 상태이거나 명시적으로 옵트아웃함 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 가입 설정" }

{% alert note %}
Windows에서는 사용자에게 푸시 알림을 보내기 위해 명시적인 옵트인이 필요하지 않습니다. 사용자가 푸시에 등록되면 기본적으로 `OPTED_IN`이 아닌 `SUBSCRIBED`로 설정됩니다. 자세한 내용은 [가입 및 명시적 옵트인 구현]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions) 설명서를 참조하세요.
{% endalert %}

| 가입 유형 | 설명 |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType` | 유효한 이메일 주소를 수신하면 사용자가 자동으로 `SUBSCRIBED`로 설정됩니다. 그러나 명시적인 옵트인 프로세스를 구축하고 사용자로부터 명시적인 동의를 받은 후 이 값을 `OPTED_IN`으로 설정하는 것을 권장합니다. 자세한 내용은 [사용자 가입 변경]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions) 문서를 참조하세요. |
| `PushNotificationSubscriptionType` | 유효한 푸시 등록 시 사용자가 자동으로 `SUBSCRIBED`로 설정됩니다. 그러나 명시적인 옵트인 프로세스를 구축하고 사용자로부터 명시적인 동의를 받은 후 이 값을 `OPTED_IN`으로 설정하는 것을 권장합니다. 자세한 내용은 [사용자 가입 변경]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions) 문서를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 가입 설정" }

{% alert note %}
이러한 유형은 `Appboy.Models.AppboyNotificationSubscriptionType`에 속합니다.
{% endalert %}

### 이메일 가입 설정 {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### 푸시 알림 가입 설정 {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
