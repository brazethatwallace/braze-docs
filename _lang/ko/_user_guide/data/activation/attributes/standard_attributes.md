---
nav_title: 표준 속성
article_title: 표준 속성
page_order: 0.5
page_type: reference
description: "이 참조 문서에서는 Braze의 표준 사용자 속성(예약 키)과 각 속성의 구문 요구 사항을 설명합니다."
---

# 표준 속성 {#standard-attributes}

> 표준 속성은 Braze가 모든 고객 프로필에서 인식하는 사전 정의된 필드입니다. 이 페이지에서 각 표준 속성의 필드 이름, 데이터 유형, 예상 형식을 빠르게 확인할 수 있습니다.

표준 속성(*기본 속성* 또는 *예약 키*라고도 함)은 비즈니스에 고유한 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)과 다릅니다. 이 페이지에 나열된 필드 이름으로 Braze에 데이터를 전송하면, Braze는 새 커스텀 속성을 생성하는 대신 사전 정의된 프로필 필드에 데이터를 저장합니다.

다음 방법 중 하나를 통해 표준 속성을 설정할 수 있습니다.

- [Braze SDK]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)
- [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)의 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object)
- [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)

{% alert important %}
표준 속성 이름은 대소문자를 구분합니다. 항상 소문자를 사용하세요(예: `First_Name`이 아닌 `first_name`). 철자나 대소문자가 정확히 일치하지 않으면 Braze는 해당 값을 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)으로 저장합니다.
{% endalert %}

## 식별자 {#identifiers}

식별자는 Braze에 업데이트하거나 생성할 고객 프로필을 알려줍니다. 모든 API 요청과 CSV 행에는 하나 이상의 식별자가 포함되어야 합니다. 올바른 식별자를 선택하는 방법에 대한 자세한 내용은 [식별자 확인]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution)을 참조하세요.

| 필드 | 데이터 유형 | 형식 및 참고 사항 |
|---|---|---|
| `external_id` | 문자열 | 사용자가 할당하는 고유 사용자 식별자입니다. 프로필에 설정된 후 Braze는 이를 사용하여 기기 간에 사용자를 인식합니다. 추가된 후에는 제거할 수 없습니다. |
| `braze_id` | 문자열 | SDK가 기기를 처음 감지할 때 생성되는 Braze 할당 식별자입니다. 읽기 전용이며 편집할 수 없습니다. |
| `user_alias` | 오브젝트 | `alias_name`(문자열)과 `alias_label`(문자열)을 포함하는 오브젝트로, `external_id` 없이 사용자를 식별하는 데 사용됩니다. 동일한 요청에서 `external_id`와 함께 사용할 수 없습니다. |
| `email` | 문자열 | `external_id`와 `user_alias`가 없을 때 식별자로 사용할 수 있습니다. 둘 다 전송된 경우 `phone`보다 우선합니다. |
| `phone` | 문자열 | `external_id`, `user_alias`, `email`이 없을 때 식별자로 사용할 수 있습니다. [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format) 형식을 사용하세요(예: `+14155552671`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 프로필 필드 {#profile-fields}

이 필드는 사용자의 인구 통계, 연락처, 로케일 데이터를 캡처합니다.

| 필드 | 데이터 유형 | 형식 및 참고 사항 |
|---|---|---|
| `first_name` | 문자열 | 사용자의 이름(예: `Jane`). |
| `last_name` | 문자열 | 사용자의 성(예: `Doe`). |
| `email` | 문자열 | 사용자의 이메일 주소(예: `jane.doe@braze.com`). |
| `phone` | 문자열 | 사용자의 전화번호. [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format) 형식을 사용하세요(예: `+14155552671`). |
| `dob` | 문자열 | `YYYY-MM-DD` 형식의 생년월일(예: `1988-02-14`). 생일 기반 타겟팅이 가능합니다. |
| `gender` | 문자열 | `M`, `F`, `O`(기타), `N`(해당 없음), `P`(밝히고 싶지 않음), 또는 `null`(알 수 없음) 중 하나. |
| `country` | 문자열 | [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1) 형식의 국가 코드(예: `US`, `GB`). CSV 가져오기 또는 API를 통해 `country`를 설정하면 SDK가 자동으로 캡처하지 않습니다. |
| `home_city` | 문자열 | 사용자의 거주 도시(예: `London`). |
| `language` | 문자열 | [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 형식의 언어 코드(예: `en`). [지원되는 언어 목록]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes)을 참조하세요. CSV 가져오기 또는 API를 통해 `language`를 설정하면 SDK가 자동으로 캡처하지 않습니다. |
| `time_zone` | 문자열 | [IANA 시간대 데이터베이스](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)의 시간대 이름(예: `America/New_York` 또는 `Eastern Time (US & Canada)`). |
| `current_location` | 오브젝트 | `longitude`와 `latitude`를 포함하는 오브젝트(예: `{"longitude": -73.991443, "latitude": 40.753824}`). |
| `image_url` | 문자열 | 사용자 프로필 이미지의 URL. 최대 1,024자. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 구독 및 동의 {#subscription-and-consent}

이 필드는 사용자가 채널별로 메시지를 수신하는 방식을 관리합니다. 이 필드를 업데이트해도 데이터 포인트 사용량에 포함되지 않습니다.

| 필드 | 데이터 유형 | 형식 및 참고 사항 |
|---|---|---|
| `email_subscribe` | 문자열 | `opted_in`(이메일 수신을 명시적으로 등록), `unsubscribed`(이메일 수신을 명시적으로 거부), 또는 `subscribed`(수신 동의도 거부도 하지 않음) 중 하나. |
| `push_subscribe` | 문자열 | `opted_in`, `unsubscribed`, 또는 `subscribed` 중 하나. `email_subscribe`와 동일한 정의입니다. |
| `subscription_groups` | 오브젝트 배열 | 각 오브젝트에 `subscription_group_id`(문자열)와 `subscription_state`(`subscribed` 또는 `unsubscribed`)가 포함된 배열. 예: `[{"subscription_group_id": "abc-123", "subscription_state": "subscribed"}]`. |
| `email_open_tracking_disabled` | 부울 | `true` 또는 `false`. 이 사용자에 대해 이메일 열람 추적 픽셀을 비활성화하려면 `true`로 설정합니다. SparkPost 및 SendGrid에서만 사용 가능합니다. |
| `email_click_tracking_disabled` | 부울 | `true` 또는 `false`. 이 사용자에 대해 이메일 클릭 추적을 비활성화하려면 `true`로 설정합니다. SparkPost 및 SendGrid에서만 사용 가능합니다. |
| `marked_email_as_spam_at` | 문자열 | 사용자의 이메일이 스팸으로 표시된 타임스탬프. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 형식을 사용합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

구독 그룹 설정에 대한 자세한 내용은 [구독 그룹]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)을 참조하세요.

## 세션 및 인게이지먼트 {#sessions-and-engagement}

이 필드는 사용자가 앱을 처음 또는 마지막으로 사용한 시점을 캡처합니다. SDK가 자동으로 기록하며, 일반적으로 다른 플랫폼에서 마이그레이션할 때만 API 또는 CSV를 통해 설정합니다.

| 필드 | 데이터 유형 | 형식 및 참고 사항 |
|---|---|---|
| `date_of_first_session` | 문자열 | 사용자가 앱을 처음 사용한 날짜. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 형식 또는 다음 형식 중 하나를 사용합니다: `yyyy-MM-ddTHH:mm:ss:SSSZ`, `yyyy-MM-ddTHH:mm:ss`, `yyyy-MM-dd HH:mm:ss`, `yyyy-MM-dd`, `MM/dd/yyyy`, 또는 `ddd MM dd HH:mm:ss.TZD YYYY`. |
| `date_of_last_session` | 문자열 | 사용자가 앱을 마지막으로 사용한 날짜. `date_of_first_session`과 동일한 형식을 사용합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 푸시 토큰 {#push-tokens}

다른 플랫폼에서 푸시 토큰을 마이그레이션할 때 이 필드를 사용합니다. Braze SDK를 통합한 후에는 푸시 토큰이 자동으로 캡처됩니다. 마이그레이션 안내는 [푸시 토큰 마이그레이션]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)을 참조하세요.

| 필드 | 데이터 유형 | 형식 및 참고 사항 |
|---|---|---|
| `push_tokens` | 오브젝트 배열 | 각 오브젝트에 `app_id`(문자열)와 `token`(문자열)이 포함된 배열. 선택적으로 `device_id`(문자열)를 포함할 수 있습니다. 예: `[{"app_id": "YOUR_APP_ID", "token": "abcd", "device_id": "optional_device_id"}]`. |
| `push_token_import` | 부울 | 최상위 플래그(`attributes`에 중첩되지 않음). `external_id`가 없는 익명 사용자의 레거시 푸시 토큰을 가져오려면 `true`로 설정합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 소셜 프로필 {#social-profile}

이 필드는 소셜 네트워크 통합의 데이터를 저장합니다.

| 필드 | 데이터 유형 | 형식 및 참고 사항 |
|---|---|---|
| `facebook` | 오브젝트 | `id`(문자열), `likes`(문자열 배열), 또는 `num_friends`(정수)를 포함할 수 있는 오브젝트. |
| `twitter` | 오브젝트 | `id`(정수), `screen_name`(문자열, X 핸들), `followers_count`(정수), `friends_count`(정수), 또는 `statuses_count`(정수)를 포함할 수 있는 오브젝트. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## API 예시 {#api-example}

다음 요청은 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통해 두 명의 사용자에게 표준 속성을 설정합니다.

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
    {
      "external_id": "user1",
      "first_name": "Alex",
      "last_name": "Doe",
      "email": "jane.doe@example.com",
      "country": "US",
      "language": "en",
      "time_zone": "America/New_York",
      "dob": "1988-02-14",
      "email_subscribe": "opted_in"
    },
    {
      "external_id": "user2",
      "first_name": "Alex",
      "phone": "+14155552671",
      "current_location": {
        "longitude": -73.991443,
        "latitude": 40.753824
      },
      "subscription_groups": [
        {
          "subscription_group_id": "abc-123",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```

전체 API 계약에 대한 자세한 내용은 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object)를 참조하세요.

## CSV 예시 {#csv-example}

다음 CSV는 두 명의 사용자에 대한 표준 속성을 업데이트합니다. 열 헤더는 이 문서의 필드 이름과 정확히 일치해야 합니다. 일치하지 않는 헤더(예: `first_name` 대신 `First_name`)는 커스텀 속성으로 가져옵니다.

```plaintext
external_id,first_name,last_name,email,country,language,dob,email_subscribe
user1,Jane,Doe,jane.doe@example.com,US,en,1988-02-14,opted_in
user2,Alex,Smith,alex.smith@example.com,GB,en,1992-09-30,subscribed
```

일부 표준 속성은 CSV 가져오기를 통해 설정할 수 없습니다. 배열, 푸시 토큰, 중첩 오브젝트는 API 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 통해 전송해야 합니다. CSV 지원 필드의 전체 목록과 가져오기 단계는 [기본 속성]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#default-attributes)을 참조하세요.

## 고려 사항 {#considerations}

표준 속성을 사용할 때 다음 사항을 고려하세요.

- **필드 이름은 대소문자를 구분합니다.** 항상 소문자를 사용하세요. 표준 속성 이름과 정확히 일치하지 않는 헤더나 키는 커스텀 속성으로 처리됩니다.
- **API 또는 CSV를 통해 값을 설정하면 SDK 자동 캡처가 중지됩니다.** API 또는 CSV를 통해 `country` 또는 `language`를 설정하면, Braze는 해당 사용자에 대해 SDK에서 해당 필드를 자동으로 캡처하지 않습니다.
- **`null`은 값을 제거합니다.** 표준 속성을 `null`로 설정하면 프로필에서 해당 값이 제거됩니다. `external_id` 및 `user_alias`를 포함한 일부 필드는 설정된 후 제거할 수 없습니다.
- **빈 CSV 값은 덮어쓰지 않습니다.** CSV 가져오기에서 빈 셀은 프로필의 기존 값을 유지합니다. 값을 지우려면 API를 사용하세요.
- **시간대 기본값은 UTC입니다.** 오프셋이 없는 날짜 문자열은 UTC 자정으로 해석되며 워크스페이스의 시간대로 표시됩니다. 시간대를 지정하려면 UTC 오프셋을 추가하세요(예: `2024-11-10T18:00:00-05:00`).

## 관련 페이지 {#related-pages}

- [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object) — 속성 오브젝트의 전체 API 계약.
- [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track) — 고객 프로필을 생성하고 업데이트하는 REST 엔드포인트.
- [사용자 속성 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes) — 표준 및 커스텀 속성을 설정하는 SDK 메서드.
- [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) — CSV 파일을 통해 표준 속성을 업로드합니다.
- [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) — 비즈니스에 고유한 속성을 정의합니다.
- [데이터 유형]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types) — 지원되는 데이터 유형에 대한 참조.