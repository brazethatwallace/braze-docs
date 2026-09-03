---
nav_title: "사용자 속성 오브젝트"
article_title: "사용자 속성 오브젝트"
page_order: 11
page_type: reference
description: "이 참조 문서에서는 사용자 속성 오브젝트의 다양한 구성요소에 대해 설명합니다."
---

# 사용자 속성 오브젝트 {#user-attributes-object}

> 속성 오브젝트의 필드가 포함된 API 요청은 지정된 고객 프로필에서 주어진 값으로 해당 이름의 속성을 생성하거나 업데이트합니다.

대시보드의 고객 프로필에서 특수 값을 업데이트하거나 커스텀 속성 데이터를 추가하려면 Braze 고객 프로필 필드 이름(아래에 나열되거나 [Braze 고객 프로필 필드](#braze-user-profile-fields) 섹션에 나열된 항목)을 사용하세요.

## 오브젝트 본문 {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
  // Braze User Profile Fields
  "first_name" : "Alex",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
  // Array of objects custom attribute
  "my_array_of_objects_attribute": [{"key": "value"}, {"key": "value"}],
  // Adding to an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$add": [{"key": "value"}] },
  // Removing from an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$remove": [{"$identifier_key": "key", "$identifier_value": "value"}] },
}
```

- [외부 사용자 ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [사용자 별칭]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

{% alert note %}
일반 배열 커스텀 속성에는 `add`와 `remove`(`$` 없이)를 사용합니다.

오브젝트 배열(중첩 커스텀 속성)에는 `/users/track` 요청 페이로드에서 `$add`, `$remove`, `$update`를 사용합니다. 이 연산자는 식별자(`$identifier_key` 및 `$identifier_value`)를 매칭하여 오브젝트 수준의 변경을 적용하며, `$new_object`를 통한 인플레이스 업데이트를 지원합니다.

기존 배열의 나머지 상태를 유지하면서 오브젝트를 추가, 제거 또는 업데이트해야 할 때 이 형식을 사용합니다. 전체 요청 예시는 [오브젝트 배열 API 예시]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) 및 [오브젝트 배열 SDK 예시]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example)를 참조하세요.
{% endalert %}

프로필 속성을 제거하려면 값을 `null`로 설정합니다. `external_id` 및 `user_alias`와 같은 일부 필드는 고객 프로필에 추가된 후에는 제거할 수 없습니다.

### 식별자 확인 {#identifier-resolution}

[익명 푸시 토큰 가져오기](#push-token-import)를 수행하는 경우가 아니라면, 각 사용자 속성 오브젝트에는 최소 하나의 식별자(`external_id`, `user_alias`, `braze_id`, `email` 또는 `phone`)가 포함되어야 합니다. 가능하면 오브젝트당 하나의 식별자만 포함하여 어떤 고객 프로필이 업데이트되거나 생성되는지에 대한 모호성을 방지하세요.

식별자를 사용할 때 다음 사항에 유의하세요:

- **`external_id`와 `user_alias`는 상호 배타적입니다.** 동일한 사용자 속성 오브젝트에 둘 다 포함하면 오류가 반환됩니다. 이미 `external_id`가 있는 사용자에게 별칭을 추가하려면 [`/users/alias/new` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_alias)를 사용하세요.
- **`email`이 `phone`보다 우선합니다.** 동일한 오브젝트에 `email`과 `phone`이 모두 포함된 경우, Braze는 `email`을 식별자로 사용합니다. 즉, 전화번호가 다른 프로필에 속하더라도 해당 이메일 주소와 연결된 고객 프로필에 속성이 적용됩니다.

{% alert important %}
예기치 않은 동작을 방지하려면 사용자 속성 오브젝트당 하나의 식별자만 사용하세요. 서로 다른 고객 프로필을 참조하는 여러 식별자를 제공하면 잘못된 프로필에 속성이 적용될 수 있습니다.
{% endalert %}

#### 기존 프로필만 업데이트 {#update-existing-profiles-only}

Braze에서 기존 고객 프로필만 업데이트하려면 요청 본문 내에서 `_update_existing_only` 키에 `true` 값을 전달해야 합니다. 이 값을 생략하면 `external_id`가 아직 존재하지 않는 경우 Braze가 새 고객 프로필을 생성합니다.

{% alert note %}
`/users/track` 엔드포인트를 통해 별칭 전용 고객 프로필을 생성하는 경우 `_update_existing_only`를 `false`로 설정해야 합니다. 이 값을 생략하면 Braze가 별칭 전용 프로필을 생성하지 않습니다.
{% endalert %}

#### 푸시 토큰 가져오기 {#push-token-import}

Braze로 푸시 토큰을 가져오기 전에 필요한지 다시 확인하세요. Braze SDK가 적용되면 API를 통해 업로드할 필요 없이 푸시 토큰을 자동으로 처리합니다.

API를 통해 업로드해야 하는 경우, 식별된 사용자 또는 익명 사용자에 대해 업로드할 수 있습니다. 이는 `external_id`가 있어야 하거나 익명 사용자에게 `push_token_import` 플래그를 `true`로 설정해야 함을 의미합니다.

{% alert note %}
다른 시스템에서 푸시 토큰을 가져올 때 `external_id`를 항상 사용할 수 있는 것은 아닙니다. Braze로의 전환 기간 동안 이러한 사용자와의 커뮤니케이션을 유지하려면 `push_token_import`를 `true`로 지정하여 `external_id`를 제공하지 않고 익명 사용자에 대한 레거시 토큰을 가져올 수 있습니다.
{% endalert %}

`push_token_import`를 `true`로 지정할 때:

* `external_id`와 `braze_id`를 지정하지 **않아야** 합니다
* 속성 오브젝트에 반드시 푸시 토큰이 포함되어 **있어야** 합니다
* 토큰이 이미 Braze에 존재하는 경우 요청이 무시됩니다. 그렇지 않으면 Braze가 각 토큰에 대해 임시 익명 고객 프로필을 생성하여 해당 개인에게 계속 메시지를 보낼 수 있도록 합니다

가져오기 후, 각 사용자가 Braze 지원 버전의 앱을 실행하면 Braze가 가져온 푸시 토큰을 해당 Braze 고객 프로필로 자동 이동하고 임시 프로필을 정리합니다.

Braze는 매월 한 번 `push_token_import` 플래그가 설정된 익명 프로필 중 푸시 토큰이 없는 프로필을 확인합니다. 익명 프로필에 더 이상 푸시 토큰이 없으면 Braze가 해당 프로필을 삭제합니다. 그러나 익명 프로필에 여전히 푸시 토큰이 있으면(실제 사용자가 해당 푸시 토큰이 있는 기기에서 아직 로그인하지 않았음을 의미) Braze는 아무 작업도 수행하지 않습니다.

자세한 내용은 [푸시 토큰 마이그레이션](#migrate-push-tokens)을 참조하세요.

#### 커스텀 속성 데이터 유형 {#custom-attribute-data-types}

다음 데이터 유형을 커스텀 속성으로 저장할 수 있습니다:

| 데이터 유형 | 참고 |
| --- | --- |
| 배열 | 커스텀 속성 배열이 지원됩니다. 요소를 추가하면 배열 끝에 추가됩니다. 요소가 이미 존재하는 경우 현재 위치에서 끝으로 이동됩니다.<br><br>고유한 값만 저장됩니다. 예를 들어, `['hotdog','hotdog','hotdog','pizza']`를 가져오면 `['hotdog', 'pizza']`가 됩니다.<br><br>배열을 직접 설정하거나(예: `"my_array_custom_attribute":[ "Value1", "Value2" ]`), 기존 배열에 `"my_array_custom_attribute" : { "add" : ["Value3"] }`으로 추가하거나, `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`으로 값을 제거할 수 있습니다.<br><br>배열의 기본 및 최대 요소 개수는 500입니다. Braze 대시보드의 **데이터 설정** > **커스텀 속성**에서 배열의 최대 개수를 업데이트할 수 있습니다. 자세한 내용은 [배열]({{site.baseurl}}/developer_guide/analytics#arrays)을 참조하세요. |
| 오브젝트 배열 | 오브젝트 배열을 사용하여 각 오브젝트에 일련의 속성이 포함된 오브젝트 목록을 정의합니다. 호텔 숙박, 구매 내역 또는 선호도와 같은 사용자의 여러 관련 데이터 세트를 저장하려면 이 유형을 사용합니다. <br><br>예를 들어, 고객 프로필에 `hotel_stays`라는 커스텀 속성을 배열로 정의하면 각 오브젝트가 `hotel_name`, `check_in_date`, `nights_stayed` 등의 속성을 가진 별도의 숙박을 나타냅니다.<br><br>오브젝트 배열은 항목 수에 제한이 없지만 최대 크기는 100&nbsp;KB입니다. 업데이트로 인해 배열이 이 제한을 초과하면 Braze가 업데이트를 삭제하고 속성은 변경되지 않습니다.<br><br>`/users/track` 및 SDK 페이로드의 경우 오브젝트 배열 작업에 `$add`, `$remove`, `$update`를 사용합니다. 스칼라 값을 포함하는 일반 배열 커스텀 속성에는 `add`와 `remove`(`$` 없이)를 사용합니다. 자세한 내용은 [오브젝트 배열 API 예시]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example), [오브젝트 배열 SDK 예시]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example), [오브젝트 배열 예시](#array-of-objects-example)를 참조하세요. |
| 부울 | `true` 또는 `false` |
| 날짜 | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 형식(권장) 또는 다음 형식 중 하나로 날짜를 저장합니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>"T"는 시간 구분자로 자리 표시자가 아니며 변경하거나 제거하지 않아야 합니다. <br><br>나열된 형식과 일치하지 않는 날짜 값은 Time 데이터 유형이 아닌 문자열로 고객 프로필에 저장됩니다. 이는 시간 기반 세분화 필터("이전", "이후" 또는 "최근 X일 이내" 등)가 해당 속성에 대해 작동하지 않음을 의미합니다. 예를 들어, `Mar 26 2026 06:12 PM +00:00`은 지원되는 형식과 일치하지 않으므로 문자열로 저장됩니다. 이를 방지하려면 ISO 8601 형식(예: `2026-03-26T18:12:00Z`)을 사용하세요. <br><br>시간대가 없는 시간 속성은 기본적으로 자정 UTC로 설정됩니다(대시보드에서는 회사 시간대의 자정 UTC 해당 시간으로 표시됩니다). 시간대를 지정하려면 타임스탬프에 UTC 오프셋을 추가하세요(예: EST의 경우 `2024-11-10T18:00:00-05:00`). 시간대 오프셋이 없거나 잘못된 형식인 경우 값은 기본적으로 UTC로 설정됩니다. <br><br>시간은 대시보드에서 회사의 시간대로 표시됩니다. 예를 들어, `2024-11-10T18:00:00-05:00`(오후 6:00 EST)은 회사가 설정한 시간대의 해당 시간으로 표시됩니다. <br><br>미래 타임스탬프가 있는 이벤트는 기본적으로 현재 시간으로 설정됩니다. <br><br>일반 커스텀 속성의 경우 연도가 0 미만이거나 3000을 초과하면 Braze는 값을 고객 프로필에 문자열로 저장합니다. |
| 플로트 | 플로트 커스텀 속성은 소수점이 있는 양수 또는 음수입니다. 예를 들어, 계정 잔액이나 제품 또는 서비스에 대한 사용자 평점을 저장하는 데 플로트를 사용할 수 있습니다. |
| 정수 | "inc" 필드와 추가할 양을 포함하는 오브젝트를 할당하여 정수 커스텀 속성을 증가시킬 수 있습니다. <br><br>예시: `"my_custom_attribute_2" : {"inc" : int_value},`|
| 중첩 커스텀 속성 | 중첩 커스텀 속성은 다른 속성의 속성정보로 속성 세트를 정의합니다. 커스텀 속성 오브젝트를 정의할 때 해당 오브젝트에 속성 세트를 추가합니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)을 참조하세요. |
| 문자열 | 문자열 커스텀 속성은 텍스트 데이터를 저장하는 데 사용되는 문자 시퀀스입니다. 예를 들어, 성과 이름, 이메일 주소 또는 선호도를 저장하는 데 문자열을 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 속성 데이터 유형" }

{% alert tip %}
커스텀 이벤트와 커스텀 속성을 언제 사용해야 하는지에 대한 지침은 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events) 및 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)을 참조하세요.
{% endalert %}

##### 오브젝트 배열 예시 {#array-of-objects-example}

이 오브젝트 배열을 사용하면 숙박 내의 특정 기준에 따라 Segments를 생성하고, Liquid 템플릿을 사용하여 각 숙박의 데이터로 메시지를 개인화할 수 있습니다.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

`$add`, `$remove`, `$update`를 사용하는 오브젝트 배열 예시는 [오브젝트 배열 API 예시]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) 및 [오브젝트 배열 SDK 예시]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example)를 참조하세요.

#### Braze 고객 프로필 필드 {#braze-user-profile-fields}

{% alert important %}
다음 고객 프로필 필드는 대소문자를 구분하므로 반드시 소문자로 참조하세요.
{% endalert %}

{% alert tip %}
카테고리별로 정리되어 있으며 SDK, API, CSV, Cloud Data Ingestion에 대한 지침을 포함하는 고객 대상 표준 속성 참조는 [표준 속성]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes)을 참조하세요.
{% endalert %}

| 고객 프로필 필드 | 데이터 유형 사양 |
| ---| --- |
| alias_name | (문자열) |
| alias_label | (문자열) |
| braze_id | (문자열, 선택 사항) SDK가 고객 프로필을 인식하면 연결된 `braze_id`를 가진 익명 고객 프로필이 생성됩니다. `braze_id`는 Braze에 의해 자동으로 할당되며 편집할 수 없고 기기별로 고유합니다. |
| country | (문자열) 국가 코드는 [ISO-3166-1 alpha-2 표준](http://en.wikipedia.org/wiki/ISO_3166-1)으로 Braze에 전달해야 합니다. API는 다른 형식으로 수신된 국가를 최선을 다해 매핑합니다. 예를 들어, "Australia"는 "AU"로 매핑될 수 있습니다. 그러나 입력이 [ISO-3166-1 alpha-2 표준](http://en.wikipedia.org/wiki/ISO_3166-1)과 일치하지 않으면 국가 값은 `NULL`로 설정됩니다. <br><br>CSV 가져오기 또는 API로 사용자에게 `country`를 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 캡처하지 않습니다. |
| current_location | (오브젝트) {"longitude": -73.991443, "latitude": 40.753824} 형식 |
| date_of_first_session | (사용자가 앱을 처음 사용한 날짜) ISO 8601 형식의 문자열 또는 다음 형식 중 하나: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (사용자가 앱을 마지막으로 사용한 날짜) ISO 8601 형식의 문자열 또는 다음 형식 중 하나: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (생년월일) "YYYY-MM-DD" 형식의 문자열(예: 1980-12-21). |
| email | (문자열) |
| email_subscribe | (문자열) 사용 가능한 값은 "opted_in"(이메일 메시지 수신에 명시적으로 등록), "unsubscribed"(이메일 메시지에서 명시적으로 탈퇴), "subscribed"(수신 동의도 탈퇴도 하지 않음)입니다.  |
| email_open_tracking_disabled |(부울) `true` 또는 `false`를 허용합니다. 이 사용자에게 전송되는 모든 향후 이메일에 열람 추적 픽셀 추가를 비활성화하려면 `true`로 설정합니다.|
| email_click_tracking_disabled |(부울) `true` 또는 `false`를 허용합니다. 이 사용자에게 전송되는 향후 이메일 내의 모든 링크에 대한 클릭 추적을 비활성화하려면 `true`로 설정합니다.|
| external_id | (문자열) 고객 프로필의 고유 식별자입니다. `external_id`가 할당되면 Braze는 사용자의 기기 전체에서 고객 프로필을 식별합니다. 알 수 없는 고객 프로필에 external_id를 처음 할당하면 Braze는 기존의 모든 고객 프로필 데이터를 새 고객 프로필로 마이그레이션합니다. |
| facebook | `id`(문자열), `likes`(문자열 배열), `num_friends`(정수) 중 하나를 포함하는 해시입니다. |
| first_name | (문자열) |
| gender | (문자열) "M", "F", "O"(기타), "N"(해당 없음), "P"(말하고 싶지 않음) 또는 null(알 수 없음). |
| home_city | (문자열) |
| language | (문자열) 언어는 [ISO-639-1 표준](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)으로 Braze에 전달해야 합니다. 지원되는 언어는 [허용된 언어 목록]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes)을 참조하세요.<br><br>CSV 가져오기 또는 API로 사용자에게 `language`를 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 캡처하지 않습니다. |
| last_name | (문자열) |
| marked_email_as_spam_at | (문자열) 사용자의 이메일이 스팸으로 표시된 날짜입니다. ISO 8601 형식 또는 다음 형식 중 하나로 표시됩니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (문자열) 전화번호는 [E.164](https://en.wikipedia.org/wiki/E.164) 형식으로 제공하는 것을 권장합니다. 자세한 내용은 [사용자 전화번호]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format)를 참조하세요.|
| push_subscribe | (문자열) 사용 가능한 값은 "opted_in"(푸시 메시지 수신에 명시적으로 등록), "unsubscribed"(푸시 메시지에서 명시적으로 탈퇴), "subscribed"(수신 동의도 탈퇴도 하지 않음)입니다.  |
| push_tokens | `app_id`와 `token` 문자열을 가진 오브젝트의 배열입니다. 이 토큰이 연결된 기기의 `device_id`를 선택적으로 제공할 수 있습니다. 예: `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. `device_id`가 제공되지 않으면 임의로 생성됩니다. |
| subscription_groups| `subscription_group_id`와 `subscription_state` 문자열을 가진 오브젝트의 배열입니다. 예: `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. `subscription_state`에 사용 가능한 값은 "subscribed"와 "unsubscribed"입니다.|
| time_zone | (문자열) [IANA 시간대 데이터베이스](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)의 시간대 이름(예: "America/New_York" 또는 "Eastern Time (US & Canada)"). 유효한 시간대 값만 설정됩니다. |
| twitter | `id`(정수), `screen_name`(문자열, X(구 Twitter) 핸들), `followers_count`(정수), `friends_count`(정수), `statuses_count`(정수) 중 하나를 포함하는 해시입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze 고객 프로필 필드" }

이 API를 통해 명시적으로 설정된 언어 값은 Braze가 기기에서 자동으로 수신하는 로캘 정보보다 우선합니다.

####  사용자 속성 예시 요청 {#user-attribute-example-request}

이 예시에는 API 호출당 허용되는 총 75개의 속성 오브젝트 중 4개의 사용자 속성 오브젝트가 포함되어 있습니다.

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Alex",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Lee",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Yuri",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## 푸시 토큰 마이그레이션 {#migrate-push-tokens}

Braze를 통합하기 전에 직접 또는 다른 제공업체를 통해 푸시 알림을 보내고 있었다면, 푸시 토큰 마이그레이션을 통해 등록된 푸시 토큰이 있는 사용자에게 계속 푸시 알림을 보낼 수 있습니다.

### SDK를 통한 자동 마이그레이션 {#automatic-migration-through-sdk}

[Braze SDK를 통합]({{site.baseurl}}/developer_guide/sdk_integration)한 후, 옵트인한 사용자의 푸시 토큰은 다음에 앱을 열 때 자동으로 마이그레이션됩니다. 그때까지는 Braze를 통해 해당 사용자에게 푸시 알림을 보낼 수 없습니다.

또는 [푸시 토큰을 수동으로 마이그레이션](#manual-migration-through-api)하여 사용자에게 더 빠르게 다시 참여시킬 수 있습니다.

#### 웹 토큰 고려 사항 {#web-token-considerations}

웹 푸시 토큰의 특성상, 웹에 대한 푸시를 구현할 때 다음 사항을 고려해야 합니다.

| 고려 사항 | 상세 내용 |
|----------------------|------------|
| **서비스 워커**  | 기본적으로, 웹 SDK는 `manageServiceWorkerExternally` 또는 `serviceWorkerLocation`과 같은 다른 옵션이 지정되지 않는 한 `./service-worker`에서 서비스 워커를 찾습니다. 서비스 워커가 제대로 설정되지 않으면 사용자의 푸시 토큰이 만료될 수 있습니다. |
| **만료된 토큰**   | 사용자가 60일 이내에 웹 세션을 시작하지 않으면 푸시 토큰이 만료됩니다. Braze는 만료된 푸시 토큰을 마이그레이션할 수 없으므로, [푸시 프라이머]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)를 보내 사용자에게 다시 참여시켜야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹 토큰 고려 사항" }

### API를 통한 수동 마이그레이션 {#manual-migration-through-api}

수동 푸시 토큰 마이그레이션은 이전에 생성된 키를 API를 통해 Braze 플랫폼으로 가져오는 프로세스입니다.

[`users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하여 iOS(APNs) 및 Android(FCM) 토큰을 프로그래밍 방식으로 플랫폼에 마이그레이션합니다. 식별된 사용자(연결된 외부 ID가 있는 사용자)와 익명 사용자(외부 ID가 없는 사용자) 모두 마이그레이션할 수 있습니다.

푸시 토큰 마이그레이션 시 앱의 `app_id`를 지정하여 적절한 푸시 토큰을 적절한 앱에 연결합니다. 각 앱(iOS, Android 등)에는 고유한 `app_id`가 있으며, [API 키]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) 페이지의 **Identification** 섹션에서 확인할 수 있습니다. 올바른 플랫폼의 `app_id`를 사용해야 합니다.

{% alert important %}
API를 통해 웹 푸시 토큰을 마이그레이션하는 것은 불가능합니다. 웹 푸시 토큰은 다른 플랫폼과 동일한 스키마를 따르지 않기 때문입니다.

<br>웹 푸시 토큰을 프로그래밍 방식으로 마이그레이션하려고 하면 다음과 같은 오류가 표시될 수 있습니다: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
API 마이그레이션의 대안으로, SDK를 통합하고 토큰 기반이 자연스럽게 다시 채워지도록 하는 것을 권장합니다.
{% endalert %}

{% tabs local %}
{% tab 외부 ID 있음 %}
식별된 사용자의 경우, `push_token_import` 플래그를 `false`로 설정하거나 매개변수를 생략하고 사용자 `attributes` 객체에서 `external_id`, `app_id`, `token` 값을 지정합니다.

예시:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab 외부 ID 없음 %}
다른 시스템에서 푸시 토큰을 가져올 때 `external_id`를 항상 사용할 수 있는 것은 아닙니다. 이 경우, `push_token_import` 플래그를 `true`로 설정하고 `app_id` 및 `token` 값을 지정합니다. Braze는 각 토큰에 대해 임시 익명 사용자 프로필을 생성하여 해당 개인에게 계속 메시지를 보낼 수 있도록 합니다. 토큰이 이미 Braze에 존재하는 경우 요청은 무시됩니다.

예시:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

가져오기 후, 익명 사용자가 Braze 지원 버전의 앱을 실행하면 Braze는 가져온 푸시 토큰을 해당 Braze 사용자 프로필로 자동 이동하고 임시 프로필을 정리합니다.

Braze는 매월 한 번 `push_token_import` 플래그가 있지만 푸시 토큰이 없는 익명 프로필을 확인합니다. 익명 프로필에 더 이상 푸시 토큰이 없으면 Braze는 해당 프로필을 삭제합니다. 그러나 익명 프로필에 아직 푸시 토큰이 있다면, 이는 실제 사용자가 아직 해당 푸시 토큰이 있는 기기에 로그인하지 않았음을 의미하며, Braze는 아무 조치도 하지 않습니다.
{% endtab %}
{% endtabs %}

### iOS 푸시 토큰 가져오기 {#import-ios-push-tokens}

`/users/track`으로 iOS 푸시 토큰을 마이그레이션할 때, 푸시 토큰에 `gateway` 필드가 설정되지 않습니다. Braze는 API를 통해 가져온 토큰이 유효한 포그라운드 푸시 토큰이라고 가정하지만, 토큰이 어떤 APNs 환경에 속하는지는 판단할 수 없습니다.

게이트웨이 필드가 없으면, Braze는 푸시 알림을 보낼 때 앱의 구성된 대체 환경 설정을 사용합니다. 이로 인해 토큰의 실제 환경이 구성된 대체 설정과 다른 경우 `BadDeviceToken` 오류가 발생할 수 있습니다. 예를 들어, 개발 토큰을 프로덕션 게이트웨이를 통해 보내면 실패합니다.

전달 문제를 방지하려면:

- Braze 대시보드에서 앱의 환경 설정이 가져오는 토큰과 일치하는지 확인합니다.
- 프로덕션 앱의 경우, 프로덕션 토큰만 가져옵니다.
- 테스트 환경의 경우, 앱 구성과 가져온 토큰 모두 개발 환경을 사용하는지 확인합니다.

{% alert note %}
Braze SDK를 통해 등록된 토큰에는 게이트웨이 필드가 자동으로 포함됩니다. SDK가 앱의 엔타이틀먼트에서 환경을 감지하기 때문입니다.
{% endalert %}

### Android 푸시 토큰 가져오기 {#import-android-push-tokens}

{% alert important %}
다음 고려 사항은 Android 앱에만 적용됩니다. iOS 앱은 푸시를 표시하는 프레임워크가 하나뿐이며, Braze에 필요한 푸시 토큰과 인증서가 있으면 푸시 알림이 즉시 렌더링되므로 이러한 단계가 필요하지 않습니다.
{% endalert %}

Braze SDK 통합이 완료되기 전에 사용자에게 Android 푸시 알림을 보내야 하는 경우, 키-값 페어를 사용하여 푸시 알림의 유효성을 검사합니다.

푸시 페이로드를 처리하고 표시할 수신기가 있어야 합니다. 수신기에 푸시 페이로드를 알리려면, 푸시 Campaign에 필요한 키-값 페어를 추가합니다. 이러한 페어의 값은 Braze 이전에 사용한 특정 푸시 파트너에 따라 다릅니다.

{% alert note %}
일부 푸시 알림 제공업체의 경우, Braze는 키-값 페어를 올바르게 해석할 수 있도록 플래트닝해야 합니다. 특정 Android 앱에 대한 키-값 페어를 플래트닝하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 스팸으로 처리되었거나 메시징이 차단된 사용자를 어떻게 찾나요? {#how-do-i-find-users-treated-as-spam-or-blocked-from-messaging}

Braze는 대시보드에 별도의 스팸 목록을 제공하지 않습니다. Braze는 세션이 500만 건을 초과하거나, 고유 커스텀 이벤트 이름이 20,000개를 초과하거나, 구매에서 고유 제품 이름이 20,000개를 초과하는 개별 고객 프로필("더미 사용자")을 차단하며, 해당 프로필에 대해 SDK와 REST API 모두에서 모든 인바운드 데이터 수집을 중단합니다. 식별자가 차단된 경우, [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)에서 `"provided external_id is blacklisted and disallowed"` 오류를 반환할 수 있습니다. 이 문구는 API 응답에서 그대로 가져온 것입니다. 과도한 세션으로 차단된 프로필을 찾으려면, **세션 수** 필터를 **5,000,000 초과**로 설정하여 [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)를 생성하고, Segment를 CSV로 내보낸 다음, **인게이지먼트** > **사용자 검색**에서 또는 [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) 엔드포인트를 통해 프로필 필드를 교차 확인합니다. 고유 커스텀 이벤트 이름이나 제품 이름에 대한 동등한 필터는 없으므로, 해당 이유로 차단된 프로필을 확인하려면 Braze 계정 매니저에게 문의하세요. 자세한 내용은 [스팸 차단]({{site.baseurl}}/user_archival)을 참조하세요.