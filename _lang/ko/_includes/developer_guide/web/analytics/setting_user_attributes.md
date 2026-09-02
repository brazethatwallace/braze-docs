{% multi_lang_include developer_guide/prerequisites/web.md %}

## 기본 사용자 속성 {#default-user-attributes}

### 미리 정의된 메서드 {#predefined-methods}

Braze는 [`User` 클래스](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 내에서 다음 사용자 속성을 설정하기 위한 미리 정의된 메서드를 제공합니다:

- 이름
- 성
- 언어
- 국가
- 생년월일
- 이메일
- 성별
- 출생지
- 전화번호

### 기본 속성 설정 {#setting-default-attributes}

{% tabs %}
{% tab 메서드 사용 %}
사용자의 기본 속성을 설정하려면 Braze 인스턴스에서 `getUser()` 메서드를 호출하여 앱의 현재 사용자에 대한 참조를 가져옵니다. 그런 다음 메서드를 호출하여 사용자 속성을 설정할 수 있습니다.

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag 매니저 %}
Google Tag 매니저를 사용하는 경우, 표준 사용자 속성(예: 사용자의 이름)은 커스텀 사용자 속성과 동일한 방식으로 기록해야 합니다. 표준 속성에 전달하는 값이 [User 클래스](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 설명서에 지정된 예상 형식과 일치하는지 확인하세요.

예를 들어, 성별 속성은 다음 중 하나를 값으로 허용할 수 있습니다: `"m" | "f" | "o" | "u" | "n" | "p"`. 따라서 사용자의 성별을 여성으로 설정하려면 다음 내용이 포함된 Custom HTML 태그를 생성하세요:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### 기본 속성 해제 {#unsetting-default-attributes}

앱 코드, REST API 요청 또는 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) Canvas 단계를 통해 사용자 속성을 제거하거나 해제할 수 있습니다. 배열 및 부울 속성의 경우 `null`을 사용하세요. 다른 데이터 유형의 경우 빈 문자열(`""`)을 사용하세요.

웹 SDK로 기본 사용자 속성을 해제하려면 관련 메서드에 `null`을 전달하세요. 예를 들어:

{% tabs local %}
{% tab First name %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gender %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## 커스텀 사용자 속성 {#custom-user-attributes}

### 커스텀 속성 설정 {#setting-custom-attributes}

{% tabs %}
{% tab 메서드 사용 %}
기본 사용자 속성 메서드 외에도 사용자에 대한 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attribute-data-types)을 설정할 수 있습니다. 전체 메서드 사양은 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)를 참조하세요.

{% subtabs local %}
{% subtab String %}
`string` 값으로 커스텀 속성을 설정하려면:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
`integer` 값으로 커스텀 속성을 설정하려면:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

{% endsubtab %}
{% subtab Date %}
`date` 값으로 커스텀 속성을 설정하려면:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```

{% endsubtab %}
{% subtab Array %}

배열의 기본 및 최대 요소 개수는 500개입니다. Braze 대시보드의 **데이터 설정** > **커스텀 속성**에서 배열의 최대 개수를 업데이트할 수 있습니다. 최대 요소 개수를 초과하는 배열은 최대 요소 개수만큼 잘립니다.


`array` 값으로 커스텀 속성을 설정하려면:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
이 메서드를 통해 Braze에 전달하는 날짜는 JavaScript Date 객체여야 합니다.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
커스텀 속성 키와 값은 최대 255자까지만 허용됩니다. 유효한 커스텀 속성 값에 대한 자세한 내용은 [참조 설명서](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)를 확인하세요.
{% endalert %}
{% endtab %}

{% tab Google Tag 매니저 %}
Google Tag 매니저의 스크립팅 언어 제한으로 인해 커스텀 사용자 속성을 사용할 수 없습니다. 커스텀 속성을 로깅하려면 다음 내용으로 커스텀 HTML 태그를 생성하세요:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
GTM 템플릿은 이벤트 또는 구매에 대한 중첩 속성을 지원하지 않습니다. 중첩 속성이 필요한 이벤트 또는 구매를 로깅하려면 위의 HTML을 사용할 수 있습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

### 커스텀 속성 해제 {#unsetting-custom-attributes}

커스텀 속성을 해제하려면 관련 메서드에 `null`을 전달하세요.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### 중첩 커스텀 속성 {#nesting-custom-attributes}

커스텀 속성 내에 속성정보를 중첩할 수도 있습니다. 다음 예에서는 중첩 속성정보가 포함된 `favorite_book` 객체를 고객 프로필의 커스텀 속성으로 설정합니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)을 참조하세요.

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### REST API 사용 {#using-the-rest-api}

REST API를 사용하여 사용자 속성을 설정하거나 해제할 수도 있습니다. 자세한 내용은 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)를 참조하세요.

## 사용자 가입 설정 {#setting-user-subscriptions}

사용자의 가입(이메일 또는 푸시)을 설정하려면 각각 `setEmailNotificationSubscriptionType()` 또는 `setPushNotificationSubscriptionType()` 함수를 호출하세요. 두 함수 모두 열거형 타입 `braze.User.NotificationSubscriptionTypes`를 인수로 받습니다. 이 타입에는 세 가지 상태가 있습니다:

| 가입 상태 | 정의 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 가입 상태이며 명시적으로 옵트인함 |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 가입 상태이지만 명시적으로 옵트인하지 않음 |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 탈퇴 상태 및/또는 명시적으로 옵트아웃함 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 가입 설정" }

사용자가 푸시에 등록하면 브라우저에서 알림 허용 또는 차단을 선택하도록 요구하며, 사용자가 푸시를 허용하면 기본적으로 `OPTED_IN`으로 설정됩니다.

가입 구현 및 명시적 옵트인에 대한 자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions)를 참조하세요.

### 이메일에서 사용자 탈퇴 {#unsubscribing-a-user-from-email}

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### 푸시에서 사용자 탈퇴 {#unsubscribing-a-user-from-push}

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
