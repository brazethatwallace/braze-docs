---
nav_title: Set 커스텀 속성
article_title: Windows 유니버설용 커스텀 속성 설정
platform: Windows Universal
page_order: 3
description: "이 참조 문서에서는 Windows 유니버설 플랫폼에서 커스텀 속성을 설정하는 방법을 설명합니다."
hidden: true
---

# 커스텀 속성 설정 {#set-custom-attributes}
{% multi_lang_include archive/windows_deprecation.md %}

Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

구현하기 전에 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예시를 [모범 사례]({{site.baseurl}}/developer_guide/analytics#best-practices)에서 검토하세요.

사용자 속성은 현재 `IAppboyUser`에 할당할 수 있습니다. 현재 `IAppboyUser`에 대한 참조를 얻으려면 `Appboy.SharedInstance.AppboyUser`를 호출합니다.

## 기본 사용자 속성 할당하기 {#assigning-default-user-attributes}

다음 속성은 `IAppboyUser`의 프로퍼티로 정의해야 합니다:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**구현 예시**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## 커스텀 사용자 속성 할당하기 {#assigning-custom-user-attributes}

기본 사용자 속성 외에도 Braze에서는 다양한 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있습니다. 세분화 옵션과 각 속성이 미치는 영향에 대한 자세한 내용은 [모범 사례]({{site.baseurl}}/hidden/archive_docs/windows_universal/analytics/setting_user_ids#user-id-integration-best-practices-and-notes)를 참조하세요.

### 커스텀 속성 값 설정하기 {#setting-custom-attribute-values}

{% tabs %}
{% tab Boolean %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab Integer %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab Double or Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze는 데이터베이스 내에서 FLOAT 값과 DOUBLE 값을 동일하게 처리합니다.
{% endtab %}
{% tab String %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab Date %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Braze에 전달되는 날짜는 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식(예: `2013-07-16T19:20:30+01:00`) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식(예: `2016-12-14T13:32:31.601-0800`)이어야 합니다.
{% endtab %}
{% tab Array %}
```csharp
// Setting a custom attribute with an array value
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### 커스텀 속성 증가/감소 {#incrementingdecrementing-custom-attributes}

이 코드는 커스텀 속성을 증가시키는 예시입니다. 커스텀 속성 값은 양의 정수 또는 음의 정수 값으로 증가시킬 수 있습니다.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### 커스텀 속성 해제하기 {#unsetting-a-custom-attribute}

커스텀 속성은 다음 메서드를 사용하여 해제할 수도 있습니다:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### REST API를 통한 커스텀 속성 설정 {#setting-a-custom-attribute-via-the-rest-api}

REST API를 사용하여 사용자 속성을 설정할 수도 있습니다. 자세한 내용은 [사용자 API]({{site.baseurl}}/api/endpoints/user_data) 설명서를 참조하세요.

### 커스텀 속성 값 제한 {#custom-attribute-value-limits}

커스텀 속성 값의 최대 길이는 255자입니다. 이보다 긴 값은 잘립니다.

## 알림 구독 상태 관리 {#managing-notification-subscription-statuses}

사용자에 대한 구독(이메일 또는 푸시)을 설정하려면 `IAppboyUser`의 프로퍼티로 다음 구독 상태를 설정할 수 있습니다. Braze의 구독 상태는 이메일과 푸시 모두에 대해 세 가지 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `OptedIn` | 가입하고 명시적으로 옵트인함 |
| `Subscribed` | 가입했지만 명시적으로 옵트인하지 않음 |
| `UnSubscribed` | 탈퇴 및/또는 명시적으로 옵트아웃함 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="알림 구독 상태 관리" }

- `EmailNotificationSubscriptionType`
  - 유효한 이메일 주소를 수신하면 사용자가 자동으로 `Subscribed`로 설정되지만, 명시적인 옵트인 프로세스를 수립하고 사용자로부터 명시적인 동의를 받은 후 이 값을 `OptedIn`으로 설정하는 것을 권장합니다.
- `PushNotificationSubscriptionType`
  - 유효한 푸시 등록 시 사용자가 자동으로 `Subscribed`로 설정되지만, 명시적인 옵트인 프로세스를 수립하고 사용자로부터 명시적인 동의를 받은 후 이 값을 `OptedIn`으로 설정하는 것을 권장합니다.

> 이러한 타입은 `AppboyPlatform.PCL.Models.NotificationSubscriptionType`에 포함됩니다. 자세한 내용은 [사용자 구독 관리]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)를 참조하세요.