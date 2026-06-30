---
nav_title: CSV 가져오기
article_title: CSV 가져오기
description: "CSV 가져오기를 사용하여 사용자 속성과 커스텀 이벤트를 기록하고 업데이트하는 방법을 알아봅니다."
page_order: 1.2
---

# CSV 가져오기 {#csv-import}

> CSV 가져오기를 사용하여 사용자 속성과 커스텀 이벤트를 기록하고 업데이트하는 방법을 알아봅니다.

## CSV 가져오기 소개 {#about-csv-import}

CSV 가져오기를 사용하여 다음 사용자 속성과 커스텀 이벤트를 기록하고 업데이트할 수 있습니다. Braze는 다음 표에 나와 있는 최대 크기 이내의 표준 CSV 파일로 이 데이터를 수신합니다.

| 유형 | 정의 | 예시 | 최대 파일 크기 |
|---|---|---|---|
| 기본 속성 | Braze에서 인식하는 예약된 사용자 속성입니다. | `first_name`, `email` | 500 MB |
| 커스텀 속성 | 비즈니스에 고유한 사용자 속성입니다. | `last_destination_searched` | 500 MB |
| 커스텀 이벤트 | 사용자 행동을 나타내는 비즈니스 고유 이벤트입니다. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CSV 가져오기 소개" }

## CSV 가져오기 사용하기 {#using-csv-import}

### 1단계: CSV 템플릿 다운로드 {#step-1-download-a-csv-template}

CSV 가져오기를 열려면 **오디언스** > **사용자 가져오기**로 이동합니다. 여기에서 업로드 날짜, 업로더 이름, 파일 이름, 타겟팅 가용성, 가져온 행 수, 가져오기 상태 등 가장 최근 가져오기에 대한 세부 정보가 나열된 표를 확인할 수 있습니다.

시작하려면 **속성** 또는 **이벤트**를 선택한 다음 적절한 템플릿을 다운로드하여 업로드용 CSV 파일을 작성합니다.

![Braze 대시보드의 '사용자 가져오기' 페이지.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### 2단계: 식별자 선택 {#choose-an-identifier}

가져올 CSV 파일에는 전용 식별자가 필요합니다. 가져오기에 사용할 다음 식별자 유형 중 하나를 선택합니다:

{% tabs local %}
<!-- TAB -->
{% tab 외부 ID %}
고객 데이터를 가져올 때 `external_id`를 각 고객의 고유 식별자로 사용할 수 있습니다. 가져오기에서 `external_id`를 제공하면 Braze는 동일한 `external_id`를 가진 기존 사용자를 업데이트하거나, 해당 `external_id`가 없는 경우 해당 `external_id`가 설정된 새로 식별된 사용자를 생성합니다.

- 다운로드: [CSV 속성 가져오기 템플릿: 외부 ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- 다운로드: [CSV 이벤트 가져오기 템플릿: 외부 ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
`external_id`가 있는 사용자와 없는 사용자를 혼합하여 업로드하는 경우 각 가져오기에 대해 별도의 CSV를 만들어야 합니다. 하나의 CSV에 `external_ids`와 사용자 별칭을 모두 포함할 수 없습니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab 사용자 별칭 %}
`external_id`가 없는 사용자를 타겟팅하려면 사용자 별칭이 포함된 사용자 목록을 가져올 수 있습니다. 별칭은 대체 고유 사용자 식별자 역할을 하며, 가입하지 않았거나 앱에서 계정을 만들지 않은 익명 사용자에게 마케팅하려는 경우 유용할 수 있습니다.

별칭 전용 사용자 프로필을 업로드하거나 업데이트하는 경우 CSV에 다음 두 열이 있어야 합니다:

- `user_alias_name`: 고유 사용자 식별자로, `external_id`의 대안입니다.
- `user_alias_label`: 사용자 별칭을 그룹화하는 공통 레이블입니다.

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@example.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@example.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="2단계: 식별자 선택" }

가져오기에서 `user_alias_name`과 `user_alias_label`을 모두 제공하면 Braze는 동일한 `user_alias_name`과 `user_alias_label`을 가진 기존 사용자를 업데이트합니다. 사용자를 찾을 수 없는 경우 Braze는 해당 `user_alias_name`이 설정된 새로 식별된 사용자를 생성합니다.

{% alert important %}
이미 `external_id`가 있는 기존 사용자를 `user_alias_name`으로 업데이트하는 데 CSV 가져오기를 사용할 수 없습니다. 대신 연결된 `user_alias_name`으로 새 사용자 프로필이 생성됩니다. 별칭 전용 사용자를 `external_id`와 연결하려면 [사용자 식별 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)를 사용합니다.
{% endalert %}

다운로드: [CSV 속성 가져오기 템플릿: 사용자 별칭]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab Braze ID %}
`external_id` 또는 `user_alias_name`과 `user_alias_label` 값 대신 내부 Braze ID 값을 사용하여 Braze에서 기존 사용자 프로필을 업데이트하려면 `braze_id`를 열 헤더로 지정합니다.

이 방법은 세분화 내 CSV 내보내기 옵션을 통해 Braze에서 사용자 데이터를 내보낸 후 해당 기존 사용자에게 새 커스텀 속성을 추가하려는 경우 유용할 수 있습니다.

{% alert important %}
`braze_id`를 사용하여 CSV 가져오기로 새 사용자를 생성할 수 없습니다. 이 방법은 Braze 플랫폼 내의 기존 사용자를 업데이트하는 데만 사용할 수 있습니다.
{% endalert %}

{% alert tip %}
Braze 대시보드의 CSV 내보내기에서 `braze_id` 값이 `Appboy ID`로 표시될 수 있습니다. 이 ID는 사용자의 `braze_id`와 동일하므로 CSV를 다시 가져올 때 이 열의 이름을 `braze_id`로 변경할 수 있습니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab 이메일 주소 및 전화번호 %}
외부 ID 또는 사용자 별칭을 생략하고 이메일 주소 또는 전화번호를 사용하여 사용자를 가져올 수 있습니다. 이메일 주소 또는 전화번호가 포함된 CSV 파일을 가져오기 전에 다음 사항을 확인합니다:

- CSV 파일에 이러한 프로필에 대한 외부 ID 또는 사용자 별칭이 없는지 확인합니다. 있는 경우 Braze는 프로필을 식별할 때 이메일 주소보다 외부 ID 또는 사용자 별칭을 우선적으로 사용합니다.
- CSV 파일이 올바르게 포맷되었는지 확인합니다.

{% alert note %}
CSV 파일에 이메일 주소와 전화번호를 모두 포함하는 경우 프로필을 조회할 때 이메일 주소가 전화번호보다 우선합니다.
{% endalert %}

해당 이메일 주소 또는 전화번호를 가진 기존 프로필이 있으면 해당 프로필이 업데이트되며, Braze는 새 프로필을 생성하지 않습니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 Braze는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)와 동일한 로직을 사용하여 가장 최근에 업데이트된 프로필을 업데이트합니다.

해당 이메일 주소 또는 전화번호를 가진 프로필이 존재하지 않으면 Braze는 해당 식별자로 새 프로필을 생성합니다. [`/users/identify` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)를 사용하여 나중에 이 프로필을 식별할 수 있습니다. 사용자 프로필을 삭제하려면 [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) 엔드포인트를 사용할 수도 있습니다.
{% endtab %}
{% endtabs %}

### 3단계: CSV 파일 작성 {#step-3-build-your-csv-file}

다음 데이터 유형 중 하나를 단일 CSV 파일로 업로드할 수 있습니다. 둘 이상의 데이터 유형을 업로드하려면 여러 CSV 파일을 업로드합니다.

- **사용자 속성:** 기본 및 커스텀 사용자 속성을 모두 포함합니다. 기본 사용자 속성은 Braze의 예약 키(예: `first_name` 또는 `email`)이며, 커스텀 속성은 비즈니스에 고유한 사용자 속성(예: `last_destination_searched`)입니다.
- **커스텀 이벤트:** 비즈니스에 고유하며 사용자가 수행한 행동을 반영합니다. 예를 들어 여행 예약 앱의 경우 `trip_booked`가 있습니다.

CSV 파일 작성을 시작할 준비가 되면 다음 정보를 참조합니다:

{% tabs local %}
<!-- TAB -->
{% tab 사용자 속성 %}
#### 필수 식별자 {#required-identifiers-attributes}

`external_id`는 필수가 아니지만 CSV 파일에는 다음 식별자 중 **하나**에 매핑할 수 있는 사용자 식별자가 포함되어야 합니다. 각 식별자에 대한 자세한 내용은 [식별자 선택](#choose-an-identifier)을 참조합니다.

- `external_id`
- `braze_id`
- `user_alias_name` **및** `user_alias_label`
- `email`
- `phone`

#### 커스텀 속성 {#custom-attributes}

다음 데이터 유형을 CSV 가져오기의 커스텀 속성으로 사용할 수 있습니다. [기본 속성](#default-attributes)과 정확히 일치하지 않는 열 헤더는 매핑 단계에서 변경하지 않는 한 Braze에서 커스텀 속성으로 가져옵니다.

| 데이터 유형 | 설명 |
|---|---|
| 날짜/시간 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식으로 저장해야 합니다. |
| 부울 | `true` 또는 `false`를 허용합니다. |
| 숫자 | 공백이나 쉼표 없는 정수 또는 플로트여야 합니다. 플로트는 마침표(`.`)를 소수점 구분 기호로 사용해야 합니다. |
| 문자열 | 값이 큰따옴표(`""`)로 감싸져 있으면 쉼표를 포함할 수 있습니다. |
| 빈 값 | 빈 값은 사용자 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 모든 기존 사용자 속성을 포함할 필요가 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 속성" }

{% alert important %}
배열, 푸시 토큰 및 커스텀 이벤트 데이터 유형은 사용자 가져오기에서 지원되지 않습니다. CSV 파일의 쉼표가 열 구분 기호로 해석되어 파일 파싱 시 오류가 발생할 수 있기 때문입니다.<br><br>이러한 종류의 값을 업로드하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 대신 사용합니다.
{% endalert %}

#### 기본 속성 {#default-attributes}

{% alert important %}
기본 속성을 가져올 때 사용하는 열 헤더는 기본 사용자 속성의 철자와 대소문자가 정확히 일치해야 합니다. 그렇지 않으면 Braze는 이를 [커스텀 속성](#custom-attributes)으로 감지합니다.
{% endalert %}

{% alert tip %}
Braze가 인식하는 표준 속성의 전체 목록(SDK, API, CSV, 클라우드 데이터 수집 포함)은 [표준 속성]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes)을 참조합니다. 다음 표는 CSV 가져오기를 통해 설정할 수 있는 하위 집합만 다룹니다.
{% endalert %}

다음 기본 속성을 사용자 가져오기에 사용할 수 있습니다.

| 사용자 프로필 필드 | 데이터 유형 | 설명 | 필수 여부 |
| :---- | :---- | :---- | :---- |
| `external_id` | 문자열 | 고객의 고유 사용자 식별자입니다. | 조건부. [필수 식별자](#required-identifiers-attributes)를 참조합니다. |
| `user_alias_name` | 문자열 | `external_id`의 대안인 익명 사용자의 고유 사용자 식별자입니다. `user_alias_label`과 함께 사용해야 합니다. | 조건부. [필수 식별자](#required-identifiers-attributes)를 참조합니다. |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화하는 공통 레이블입니다. `user_alias_name`과 함께 사용해야 합니다. | 조건부. [필수 식별자](#required-identifiers-attributes)를 참조합니다. |
| `first_name` | 문자열 | 사용자가 표시한 이름입니다(예: `Jane`). | 아니요 |
| `last_name` | 문자열 | 사용자가 표시한 성입니다(예: `Doe`). | 아니요 |
| `email` | 문자열 | 사용자가 표시한 이메일입니다(예: `jane.doe@example.com`). | 아니요 |
| `country` | 문자열 | 국가 코드는 ISO-3166-1 alpha-2 표준으로 Braze에 전달해야 합니다(예: `GB`). | 아니요 |
| `dob` | 문자열 | "YYYY-MM-DD" 형식으로 전달해야 합니다(예: `1980-12-21`). 사용자의 생년월일을 가져오며 생일이 "오늘"인 사용자를 타겟팅할 수 있습니다. | 아니요 |
| `gender` | 문자열 | "M", "F", "O"(기타), "N"(해당 없음), "P"(밝히고 싶지 않음) 또는 nil(알 수 없음)입니다. | 아니요 |
| `home_city` | 문자열 | 사용자가 표시한 거주 도시입니다(예: `London`). | 아니요 |
| `language` | 문자열 | 언어는 ISO-639-1 표준으로 Braze에 전달해야 합니다(예: `en`). [허용되는 언어 목록]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes)을 참조합니다. | 아니요 |
| `phone` | 문자열 | 사용자가 표시한 전화번호로, `E.164` 형식입니다(예: `+442071838750`). 포맷 지침은 [사용자 전화번호]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)를 참조합니다. | 아니요 |
| `email_open_tracking_disabled` | 부울 | true 또는 false를 허용합니다. true로 설정하면 이 사용자에게 전송되는 모든 향후 이메일에 오픈 추적 픽셀이 추가되지 않습니다. SparkPost 및 SendGrid에서만 사용 가능합니다. | 아니요 |
| `email_click_tracking_disabled` | 부울 | true 또는 false를 허용합니다. true로 설정하면 이 사용자에게 전송되는 향후 이메일의 모든 링크에 대한 클릭 추적이 비활성화됩니다. SparkPost 및 SendGrid에서만 사용 가능합니다. | 아니요 |
| `email_subscribe` | 문자열 | 사용 가능한 값은 `opted_in`(이메일 메시지 수신에 명시적으로 등록), `unsubscribed`(이메일 메시지 수신을 명시적으로 거부), `subscribed`(수신 동의도 거부도 하지 않음)입니다. | 아니요 |
| `push_subscribe` | 문자열 | 사용 가능한 값은 `opted_in`(푸시 메시지 수신에 명시적으로 등록), `unsubscribed`(푸시 메시지 수신을 명시적으로 거부), `subscribed`(수신 동의도 거부도 하지 않음)입니다. | 아니요 |
| `time_zone` | 문자열 | 시간대는 IANA 시간대 데이터베이스와 동일한 형식으로 Braze에 전달해야 합니다(예: `America/New_York` 또는 `Eastern Time (US & Canada)`). | 아니요 |
| `date_of_first_session`  `date_of_last_session` | 문자열 | 다음 ISO 8601 형식 중 하나로 전달할 수 있습니다: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS"(예: 2019-11-20T18:38:57) | 아니요 |
| `subscription_group_id` | 문자열 | 구독 그룹의 `id`입니다. 이 식별자는 대시보드의 구독 그룹 페이지에서 찾을 수 있습니다. | 아니요 |
| `subscription_state` | 문자열 | `subscription_group_id`로 지정된 구독 그룹의 구독 상태입니다. 허용되는 값은 `unsubscribed`(구독 그룹에 없음) 또는 `subscribed`(구독 그룹에 있음)입니다. | 아니요, 하지만 `subscription_group_id`를 사용하는 경우 강력히 권장됩니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="기본 속성" }

#### 구독 그룹 상태 업데이트(선택 사항) {#updating-subscription-group-status-optional}

또한 사용자 가져오기를 통해 이메일 또는 SMS 구독 그룹에 사용자를 추가할 수 있습니다. 이는 SMS 채널로 메시지를 보내려면 사용자가 SMS 구독 그룹에 등록되어 있어야 하므로 SMS에 특히 유용합니다. 자세한 내용은 [SMS 구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups#subscription-group-mms-enablement)을 참조합니다.

구독 그룹 상태를 업데이트하는 경우 CSV에 다음 두 열이 있어야 합니다:

- `subscription_group_id`: [구독 그룹]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)의 `id`입니다.
- `subscription_state`: 사용 가능한 값은 `unsubscribed`(구독 그룹에 없음) 또는 `subscribed`(구독 그룹에 있음)입니다.

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="구독 그룹 상태 업데이트(선택 사항)" }

{% alert note %}
사용자 가져오기에서 행당 하나의 `subscription_group_id`만 설정할 수 있습니다. 행마다 다른 `subscription_group_id` 값을 가질 수 있습니다. 그러나 동일한 사용자를 여러 구독 그룹에 등록해야 하는 경우 여러 번 가져오기를 수행해야 합니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab 커스텀 이벤트 %}
#### 필수 식별자 {#required-identifiers-custom-events}

`external_id`는 필수가 아니지만 CSV 파일의 헤더에 다음 식별자 중 **하나**를 **반드시** 포함해야 합니다. 각 식별자에 대한 자세한 내용은 [식별자 선택](#choose-an-identifier)을 참조합니다.

- `external_id`
- `braze_id`
- `user_alias_name` **및** `user_alias_label`
- `email`
- `phone`

#### 커스텀 이벤트 필드 {#custom-event-fields}

다음 외에도 CSV에 이벤트 속성정보에 대한 추가 열 헤더를 포함할 수 있습니다. 이러한 속성정보의 열 헤더는 `<event_name>.properties.<property name>` 형식이어야 합니다.

예를 들어 커스텀 이벤트 `trip_booked`에 `destination`과 `duration` 속성정보가 있을 수 있습니다. 이는 열 헤더 `trip_booked.properties.destination`과 `trip_booked.properties.duration`을 사용하여 가져올 수 있습니다.

| 사용자 프로필 필드 | 데이터 유형 | 정보 | 필수 여부 |
| :---- | :---- | :---- | :---- |
| `external_id` | 문자열 | 사용자의 고유 사용자 식별자입니다. | 조건부. [필수 식별자](#required-identifiers-custom-events)를 참조합니다. |
| `braze_id` | 문자열 | 사용자에게 Braze가 할당한 식별자입니다. | 조건부. [필수 식별자](#required-identifiers-custom-events)를 참조합니다. |
| `user_alias_name` | 문자열 | `external_id`의 대안인 익명 사용자의 고유 사용자 식별자입니다. `user_alias_label`과 함께 사용해야 합니다. | 조건부. [필수 식별자](#required-identifiers-custom-events)를 참조합니다. |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화하는 공통 레이블입니다. `user_alias_name`과 함께 사용해야 합니다. | 조건부. [필수 식별자](#required-identifiers-custom-events)를 참조합니다. |
| `email` | 문자열 | 사용자가 표시한 이메일입니다(예: `jane.doe@example.com`). | 아니요, 다른 식별자가 없는 경우에만 사용할 수 있습니다. 다음 참고 사항을 참조합니다. |
| `phone` | 문자열 | 사용자가 표시한 전화번호로, `E.164` 형식입니다(예: `+442071838750`). 포맷 지침은 [사용자 전화번호]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)를 참조합니다. | 아니요, 다른 식별자가 없는 경우에만 사용할 수 있습니다. 다음 참고 사항을 참조합니다. |
| `name` | 문자열 | 사용자의 커스텀 이벤트입니다. | 예 |
| `time` | 문자열 | 이벤트 시간입니다. 다음 ISO-8601 형식 중 하나로 전달할 수 있습니다: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS"(예: 2019-11-20T18:38:57) | 예 |
| `<event name>.properties.<property name>` | 다중 | 커스텀 이벤트와 연결된 이벤트 속성정보입니다. 예시: `trip_booked.properties.destination` | 아니요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="커스텀 이벤트 필드" }

#### 커스텀 이벤트 포맷 요구 사항 {#format-requirements-for-custom-events}

CSV를 사용하여 커스텀 이벤트를 가져올 때 데이터 가져오기를 성공적으로 수행하려면 다음 요구 사항에 따라 파일을 포맷해야 합니다.

##### 커스텀 이벤트 포맷 이해하기 {#understanding-custom-event-formatting}

각 속성정보가 올바른 이벤트에 매핑되도록 점 표기법을 사용하여 커스텀 이벤트 CSV를 올바르게 포맷하는 것이 중요합니다. 포맷이 올바르지 않으면 속성정보가 누락되거나 가져오기가 실패할 수 있으며, 특히 하나의 파일에 여러 이벤트 유형이 포함된 경우 더욱 그렇습니다.

##### 이벤트 속성정보에 점 표기법 사용 {#use-dot-notation-for-event-properties}

점 표기법은 커스텀 이벤트와 해당 속성정보 간의 계층적 관계를 정의하는 데 사용됩니다. 이 포맷 규칙을 사용하면 각 이벤트에 대한 특정 속성을 포함하는 구조화된 이벤트 데이터를 가져올 수 있습니다.

점 표기법 형식은 다음 구조를 따릅니다: `event_name.properties.property_name`

점 표기법은 다음 순서로 작동합니다:

1. 이벤트 이름이 먼저 옵니다
2. 그 다음 `.properties.`가 와서 뒤따르는 것이 이벤트 속성정보임을 나타냅니다
3. 마지막으로 특정 속성정보 이름이 옵니다

**예시:**

`rented_movie`라는 커스텀 이벤트에 `movie_name`과 `genre` 속성정보가 있는 경우 CSV 열 헤더는 다음과 같습니다:

- `rented_movie.properties.movie_name`
- `rented_movie.properties.genre`

이 표기법은 Braze에 `rented_movie`라는 커스텀 이벤트를 생성하고 해당 특정 이벤트 인스턴스에 `movie_name`과 `genre` 속성정보를 첨부하도록 지시합니다.

##### 행당 하나의 이벤트 {#one-event-per-row}

CSV의 각 행은 단일 사용자에 대한 단일 커스텀 이벤트를 나타냅니다. 사용자에게 여러 이벤트가 있는 경우 동일한 사용자 식별자를 공유하더라도 각 이벤트에 대해 별도의 행을 포함해야 합니다.

{% alert important %}
행에 특정 이벤트에 대한 데이터가 포함된 경우 해당 이벤트의 속성정보 열만 채웁니다. 다른 이벤트의 열은 비워 둡니다.
{% endalert %}

##### CSV 구조 예시 {#example-csv-structure}

다음 표는 속성정보가 있는 커스텀 이벤트를 가져오기 위한 올바른 포맷을 보여줍니다. 이 예시에서는 각각 다른 이벤트를 수행한 두 명의 사용자를 보여줍니다: 한 명은 영화를 대여했고, 다른 한 명은 영화를 구매했습니다.

| external_id | name | time | rented_movie.properties.movie_name | rented_movie.properties.genre | bought_movie.properties.movie_name | bought_movie.properties.genre |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 123 | rented_movie | 2024-06-10T12:00:00Z | Ghostbusters | Action | | |
| 456 | bought_movie | 2024-06-12T12:00:00Z | | | Ghostbusters | Action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="CSV 구조 예시" }

이 예시에서:

- 사용자 `123`은 `movie_name`(Ghostbusters)과 `genre`(Action) 속성정보가 있는 `rented_movie` 이벤트를 트리거했습니다
- 사용자 `456`은 `movie_name`(Ghostbusters)과 `genre`(Action) 속성정보가 있는 `bought_movie` 이벤트를 트리거했습니다
- 각 이벤트는 관련 속성정보 열만 채우고 다른 이벤트 속성정보 열은 비워 둡니다

{% endtab %}
{% endtabs %}

### 4단계: 파일 업로드 {#step-4-upload-your-file}

파일을 업로드하려면 **속성** 또는 **이벤트**를 선택하고 **파일 찾기**를 클릭한 다음 CSV를 업로드합니다. Braze는 처음 몇 행의 미리보기와 감지된 필드의 요약을 표시합니다.

대용량 파일(기본 속성 및 커스텀 속성의 경우 최대 500 MB, 커스텀 이벤트의 경우 최대 50 MB)의 경우 파일이 업로드되고 Braze가 가져오기를 계산하는 동안 대시보드가 일시적으로 응답하지 않는 것처럼 보일 수 있습니다. 이러한 업로드 및 계산은 작은 파일보다 완료하는 데 더 오래 걸릴 수 있습니다. 이 단계가 완료될 때까지 기다립니다. 파일 제한 및 타이밍에 대한 자세한 내용은 [CSV 구성하기]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#constructing-your-csv)를 참조합니다.

**가져오기 이름** 필드에서 가져오기 이름을 변경할 수 있습니다. 기본적으로 파일 이름이 사용됩니다.

{% alert note %}
파일 미리보기는 파일의 처음 몇 행만 표시합니다. 가져오기 전에 모든 행을 확인하려면 [파일 유효성 검사](#file-validation)를 사용합니다.
{% endalert %}

### 5단계: 필드 매핑(속성의 경우) {#csv-data-mapping}

미리보기 후 CSV 헤더를 Braze 속성에 매핑할 수 있습니다. Braze는 CSV 파일의 필드를 동일한 이름의 속성에 자동으로 매핑하고 필요한 경우 새 속성을 생성합니다. 또한 제안을 수동으로 조정하거나 열에 대해 다른 속성을 선택할 수 있는 유연성도 있습니다.

![열 매핑 페이지.]({% image_buster /assets/img/csv_import/column_mapping_mapped.png %})

#### 매핑 상태 {#mapping-statuses}

매핑 상태 열은 CSV 파일을 가져올 때 발생하는 동작을 나타내며 다음 중 하나일 수 있습니다.

| 매핑 상태 | 의미 |
|:---|:---|
| **매핑됨** | 기존 속성 또는 식별자에 매핑된 필드입니다. |
| **새 속성** | Braze가 가져오기 시 새 속성을 생성합니다. **새 속성 편집** 버튼을 선택하여 이 속성을 편집할 수 있습니다. |
| **데이터 유형 불일치** | CSV 열의 감지된 데이터 유형이 기존 속성 또는 식별자의 데이터 유형과 일치하지 않습니다. Braze는 가져오기 시 기존 속성에 맞게 데이터 유형을 변환하려고 시도합니다. 변환이 불가능한 경우 값이 삭제됩니다. |
| **차단 목록 속성** | CSV 필드가 차단 목록에 있는 속성의 이름과 일치합니다. 매핑할 다른 속성을 선택하지 않으면 해당 열은 가져오지 않습니다. |
| **중복 속성** | CSV 파일에 동일한 이름의 필드가 하나 이상 있습니다. 동일한 이름의 열을 다른 속성에 매핑하지 않으면 첫 번째 열만 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="매핑 상태" }


#### 새 속성 편집 {#editing-new-attributes}

워크스페이스에 일치하는 속성이 없는 경우 Braze는 CSV 필드의 이름과 감지된 데이터 유형을 사용하여 가져오기 시 새 속성을 생성하려고 시도합니다. 매핑 상태 옆의 **새 속성 편집** 버튼을 선택하여 가져오기 전에 이 새 속성을 편집할 수 있습니다.

![열 매핑 페이지의 새 속성 편집 버튼.]({% image_buster /assets/img/csv_import/column_mapping_edit_attribute_button.png %})


{% alert note %}
식별자가 매핑될 때까지 매핑 단계를 넘어갈 수 없습니다. Braze는 가능한 경우 식별자를 자동으로 매핑합니다. 식별자가 매핑되었는지 확인하려면 **필수 필드** 섹션을 참조합니다.
{% endalert %}

### 6단계: 타겟팅 기본 설정 선택 {#targeting-preferences}

매핑 후 가져오기 설정 페이지에서 다음 타겟팅 기본 설정 중에서 선택할 수 있습니다. 가져오기에서 새 타겟팅 필터나 Segment를 만들 필요가 없는 경우 **이 목록을 타겟팅 필터로 사용하지 않음**을 선택합니다.

| 옵션 | 설명 |
|---|---|
| 타겟팅 필터 | CSV 파일을 사용자 Segment 구축 시 리타겟팅 옵션으로 변환하려면 **CSV에서 업데이트/가져오기** 드롭다운에서 파일을 선택한 다음 **타겟팅 필터 생성**을 선택합니다. |
| 새 Segment | 새 타겟팅 필터에서 새 Segment도 생성하려면 **타겟팅 필터 생성 및 새 Segment에 추가**를 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="6단계: 타겟팅 기본 설정 선택" }

!["Halloween season fun"이라는 CSV 파일이 포함된 "CSV에서 업데이트/가져오기" 필터가 있는 필터 그룹.]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### 7단계: 파일 유효성 검사(선택 사항) {#file-validation}

가져오기를 시작하기 전에 파일 유효성 검사를 실행하여 모든 행에서 오류와 경고를 확인할 수 있습니다. 파일의 유효성을 검사하려면 가져오기 설정 페이지에서 **가져오기 전 파일 유효성 검사**를 선택한 다음 **다음**을 선택합니다.

유효성 검사는 최대 허용 크기의 파일에 대해 최대 2분이 소요될 수 있습니다. 유효성 검사가 실행되는 동안 **유효성 검사 건너뛰기**를 선택하여 건너뛰고 즉시 진행할 수 있습니다.

#### 유효성 검사 결과 {#validation-results}

유효성 검사가 완료되면 다음 결과 중 하나가 나타납니다.

| 결과 | 의미 | 다음 단계 |
|---|---|---|
| **유효성 검사 완료** | 문제가 발견되지 않았습니다. | **데이터 가져오기**를 선택합니다. |
| **문제 발견** | 일부 행에 오류 또는 경고가 있습니다. | 오류 보고서를 다운로드하여 검토한 다음 **그래도 가져오기**를 선택하여 진행하거나 **취소**를 선택하여 파일을 먼저 수정합니다. |
| **유효성 검사 시간 초과** | 유효성 검사 시간이 초과되었습니다. 확인된 행에는 문제가 없었습니다. | **데이터 가져오기**를 선택합니다. 전체 보고서는 몇 분 후에 사용할 수 있습니다. |
| **문제가 있는 유효성 검사 시간 초과** | 유효성 검사 시간이 초과되었으며 확인된 일부 행에서 오류가 발견되었습니다. | 부분 보고서를 다운로드하여 발견된 내용을 검토한 다음 **그래도 가져오기** 또는 **취소**를 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="유효성 검사 결과" }

![오류 및 경고가 있는 행 수를 표시하고 뒤로 가기, 오류 보고서 다운로드 또는 가져오기 시작 옵션이 있는 문제 발견 섹션이 표시된 요약 페이지.]({% image_buster /assets/img/csv_import/summary_page_validation_results.png %})

#### 오류 보고서 이해하기 {#understanding-the-error-report}

오류 보고서는 플래그가 지정된 모든 행과 원본 데이터 및 문제 설명이 포함된 CSV 파일입니다.

| 문제 유형 | 설명 |
|---|---|
| **오류** | 가져오기 중 해당 행이 완전히 건너뛰어집니다. |
| **경고** | 해당 행은 가져오지만 일부 값이 삭제됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="오류 보고서 이해하기" }

보고서를 검토한 후 원본 파일에서 문제를 수정하고 다시 업로드하거나, 가져오기를 진행하고 부분 결과를 수락할 수 있습니다.



### 8단계: CSV 가져오기 시작 {#step-8-start-your-csv-import}

준비가 되면 **가져오기 시작**을 선택합니다. **사용자 가져오기** 페이지에서 현재 진행 상황을 추적할 수 있으며, 5초마다 자동으로 새로고침됩니다.
CSV 크기에 따라 처리에 몇 분에서 몇 시간이 걸릴 수 있습니다. 이 시간 동안 대시보드가 응답하지 않거나 느리게 응답할 수 있지만 가져오기는 계속 실행됩니다.

{% alert note %}
동시에 둘 이상의 CSV를 가져올 수 있습니다. CSV 가져오기는 동시에 실행되므로 업데이트 순서가 순차적으로 보장되지 않습니다. CSV 가져오기를 순차적으로 실행해야 하는 경우 두 번째 CSV를 업로드하기 전에 CSV 가져오기가 완료될 때까지 기다립니다.
{% endalert %}

#### 가져오기 상태 {#import-statuses}

가져오기를 시작한 후 **사용자 가져오기** 페이지에서 상태를 확인할 수 있습니다.

| 상태 | 설명 |
|---|---|
| **완료** | 모든 행이 성공적으로 가져와졌습니다. |
| **부분 성공** | 일부 행이 실패했습니다. 가져오기 옆의 점 세 개 메뉴를 선택하여 오류 보고서 또는 원본 업로드된 CSV를 다운로드합니다. |
| **진행 중** | 가져오기가 현재 실행 중입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="가져오기 상태" }

![부분 성공 상태가 표시된 사용자 가져오기 페이지에서 컨텍스트 메뉴가 열려 있고 오류 보고서 다운로드 및 업로드된 CSV 다운로드 옵션이 표시됩니다.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

가져오기 후 오류 보고서에는 유효성 검사에서 다루지 않는 이유로 실패한 행이 포함됩니다. 예를 들어 Braze에 사용자가 존재하지 않는 경우입니다.

{% alert important %}
이전에 업로드된 CSV 파일은 업로드 날짜로부터 14일 동안 **사용자 가져오기** 페이지에서 다운로드할 수 있습니다. 14일이 지나면 파일이 영구적으로 삭제되어 더 이상 액세스할 수 없습니다.
{% endalert %}

## 데이터 포인트 고려 사항 {#data-point-considerations}

CSV 파일에서 가져온 각 고객 데이터는 사용자 프로필의 기존 값을 덮어쓰고 데이터 포인트를 기록합니다. 단, 외부 ID와 빈 값은 예외입니다. Braze 데이터 포인트의 세부 사항에 대해 궁금한 점이 있으면 Braze 계정 매니저에게 문의할 수 있습니다.

| 고려 사항 | 세부 정보 |
|---|---|
| 외부 ID | `external_id`만 포함된 CSV를 업로드하면 데이터 포인트가 기록되지 않습니다. 이를 통해 데이터 제한에 영향을 주지 않고 기존 Braze 사용자를 세분화할 수 있습니다. 그러나 `email` 또는 `phone`과 같은 필드를 포함하면 기존 사용자 데이터를 덮어쓰고 데이터 포인트가 **기록됩니다**. <br><br>`external_id`, `braze_id` 또는 `user_alias_name`만 포함하는 세분화 전용 CSV 가져오기는 데이터 포인트를 기록하지 않습니다. |
| 빈 값 | CSV의 빈 값은 기존 사용자 프로필 데이터를 덮어쓰지 않습니다. 가져올 때 모든 사용자 속성이나 커스텀 이벤트를 포함할 필요가 없습니다. |
| 구독 상태 | `email_subscribe`, `push_subscribe`, `subscription_group_id` 또는 `subscription_state`를 업데이트해도 데이터 포인트 사용량에 **포함되지 않습니다**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="데이터 포인트 고려 사항" }

{% alert important %}
CSV 가져오기 또는 API를 통해 사용자에게 `language` 또는 `country`를 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 캡처하지 못하게 됩니다.
{% endalert %}

## 문제 해결 {#troubleshooting}

[파일 유효성 검사](#file-validation)를 사용한 경우 오류 보고서부터 시작합니다. 오류 보고서에는 플래그가 지정된 각 행에 대한 구체적인 문제와 수정 방법에 대한 설명이 포함되어 있습니다. 유효성 검사가 아닌 가져오기 중에 실패한 행의 경우 **사용자 가져오기** 페이지에서 행 위에 마우스를 올리고 <i class="fas fa-download" title="다운로드"></i> 버튼을 선택하여 오류 보고서를 다운로드합니다.

CSV 가져오기 문제 해결을 위해 아래의 일반적인 문제를 검토합니다.

### 이메일을 `external_id`로 사용 {#use-email-as-external_id}

Braze는 이메일 주소를 `external_id`로 사용하는 것을 권장하지 않습니다. 이메일을 `external_id`로 사용하는 경우 사용자가 이메일 채널에서 타겟팅 가능하도록 CSV에 `external_id`와 `email` 열을 모두 포함합니다. 열 구분 기호로 쉼표(`,`)를 사용하고 콜론(`:`)은 사용하지 않습니다.

### `external_id` 값의 따옴표 문자 {#quote-characters-in-external_id-values}

`external_id` 셀에 큰따옴표가 포함된 경우 [이스케이프되지 않거나 균형이 맞지 않는 큰따옴표](#missing-row)에 설명된 대로 문자를 두 번 입력하여(`""`) 이스케이프합니다. CSV 가져오기는 백슬래시 이스케이프를 사용하지 않습니다.

### Segment 필터로 CSV 가져오기를 사용할 수 없음 {#csv-import-isnt-available-as-a-segment-filter}

업로드 중에 타겟팅 기본 설정을 활성화한 경우에만 CSV 가져오기를 Segment 필터로 사용할 수 있습니다.

기존 가져오기에 대해 타겟팅 가용성이 활성화되어 있는지 확인하려면:

1. **사용자 가져오기** 페이지에서 CSV 가져오기를 찾습니다.
2. 해당 가져오기에 **Segment로 이동**이 표시되는지 확인합니다.
3. **Segment로 이동**이 표시되면 CSV를 `CSV에서 업데이트/가져오기` Segment 필터에서 사용할 수 있습니다.
4. **Segment로 이동**이 표시되지 않으면 해당 가져오기에 대해 타겟팅 가용성이 활성화되지 않은 것입니다.

CSV 업로드가 완료된 후에는 타겟팅 가용성을 활성화할 수 없습니다. 해당 CSV를 Segment 필터로 사용하려면 파일을 다시 업로드하고 [6단계: 타겟팅 기본 설정 선택](#step-6-choose-targeting-preferences)에서 **타겟팅 필터 생성** 또는 **타겟팅 필터 생성 및 새 Segment에 추가**를 선택합니다.

프로필 데이터를 업데이트하지 않고 Segment를 생성하는 것이 목표인 경우 식별자 열만 포함된 CSV(예: `external_id` 또는 별칭 식별자 열)를 업로드한 다음 **타겟팅 필터 생성 및 새 Segment에 추가**를 선택합니다.

### 파일 포맷 문제 {#file-formatting-issues}

#### 잘못된 형식의 행 {#malformed-row}

업로드가 오류와 함께 완료된 경우 CSV 파일에 잘못된 형식의 행이 있을 수 있습니다.

데이터를 올바르게 가져오려면 헤더 행이 있어야 합니다. 각 행은 헤더 행과 동일한 수의 셀을 가져야 합니다. 헤더 행보다 값이 많거나 적은 행은 가져오기에서 제외됩니다. 값 내의 쉼표는 구분 기호로 해석되어 이 오류를 유발할 수 있습니다.

또한 모든 데이터는 UTF-8로 인코딩되어야 합니다. 파일이 레거시 인코딩(예: 일부 Excel 기본값)으로 저장된 경우 셀의 특수 문자와 URL이 손상되어 Braze 또는 전송된 메시지에서 물음표(`?`)로 표시될 수 있습니다.

CSV 파일에 빈 행이 있고 CSV 파일의 총 줄 수보다 적은 행이 가져와진 경우 빈 행은 가져올 필요가 없으므로 가져오기에 문제가 있는 것이 아닐 수 있습니다. 올바르게 가져온 줄 수를 확인하고 가져오려는 사용자 수와 일치하는지 확인합니다.

#### 누락된 행 {#missing-row}

가져온 사용자 수가 CSV 파일의 총 행 수와 일치하지 않는 데에는 몇 가지 이유가 있습니다:

| 문제 | 해결 방법 |
|---|---|
| 중복된 외부 ID, 사용자 별칭, Braze ID, 이메일 주소 또는 전화번호 | 중복된 외부 ID 열이 있으면 행이 올바르게 포맷되어 있더라도 잘못된 형식이거나 가져오지 못한 행이 발생할 수 있습니다. 경우에 따라 특정 오류가 보고되지 않을 수 있습니다. 중복을 확인하고 다시 업로드하기 전에 제거합니다. |
| 악센트 문자 | CSV에 악센트가 있는 이름이나 속성이 포함될 수 있습니다. 가져오기 문제를 방지하려면 파일이 UTF-8로 인코딩되어 있는지 확인합니다. |
| Braze ID가 고아 사용자에 속함 | 사용자가 다른 사용자에 병합되어 Braze가 Braze ID를 남은 프로필과 연결할 수 없는 경우 해당 행은 가져오지 않습니다. |
| 빈 행 | CSV의 빈 행은 잘못된 형식의 데이터 오류를 유발할 수 있습니다. Excel이나 Sheets가 아닌 일반 텍스트 편집기를 사용하여 확인합니다. |
| 이스케이프되지 않거나 균형이 맞지 않는 큰따옴표(`"`) | 큰따옴표는 쉼표가 포함된 문자열 값을 감쌉니다. 값 자체에 큰따옴표가 포함된 경우 이를 두 번 입력하여(`""`) 이스케이프합니다. 이스케이프되지 않거나 균형이 맞지 않는 큰따옴표는 잘못된 형식의 행을 유발합니다. |
| 일관되지 않은 줄 바꿈 | 혼합된 줄 바꿈(예: `\n`과 `\r\n`)으로 인해 데이터의 첫 번째 행이 헤더의 일부로 처리될 수 있습니다. 16진수 또는 고급 텍스트 편집기를 사용하여 검사하고 수정합니다. |
| 잘못 인코딩된 파일 | 악센트가 허용되더라도 파일은 UTF-8로 인코딩되어야 합니다. 다른 인코딩은 부분적으로 작동할 수 있지만 완전히 지원되지는 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="누락된 행" }

#### 문자열 따옴표 {#string-quotation}

작은따옴표(`''`) 또는 큰따옴표(`""`)로 감싸진 값은 가져오기 시 문자열로 읽힙니다.

#### 잘못된 형식의 날짜 {#incorrectly-formatted-dates}

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식이 아닌 날짜는 가져오기 시 `datetimes`로 읽히지 않습니다.

### 데이터 구조 문제 {#data-structure-issues}

#### 잘못된 이메일 주소 {#invalid-email-addresses}

업로드가 오류와 함께 완료된 경우 하나 이상의 잘못된 암호화된 이메일 주소가 있을 수 있습니다. Braze로 가져오기 전에 모든 이메일 주소가 올바르게 암호화되었는지 확인합니다.

- **Braze에서 [이메일 주소를 업데이트하거나 가져올 때]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption#step-3-import-and-update-users)** 이메일이 포함된 모든 곳에서 해시된 이메일 값을 사용합니다. 이러한 해시 이메일 값은 내부 팀에서 제공합니다.
- **새 사용자를 생성할 때** 사용자의 암호화된 이메일 값과 함께 `email_encrypted`를 추가해야 합니다. 그렇지 않으면 Braze가 사용자를 생성하지 않습니다. 마찬가지로 이메일이 없는 기존 사용자에게 이메일 주소를 추가하는 경우 `email_encrypted`를 추가해야 합니다. 그렇지 않으면 Braze가 사용자를 업데이트하지 않습니다.

#### 커스텀 속성으로 가져온 데이터 {#data-imported-as-custom-attribute}

기본 사용자 데이터(예: `email` 또는 `first_name`)가 커스텀 속성으로 가져와진 경우 CSV 파일의 대소문자와 간격을 확인합니다. 예를 들어 `First_name`은 커스텀 속성으로 가져오지만 `first_name`은 사용자 프로필의 "이름" 필드에 올바르게 가져옵니다.

#### 커스텀 속성의 데이터 유형 변경 {#change-a-custom-attributes-data-type}

기존 커스텀 속성의 데이터 유형을 변경해야 하는 경우(예: 문자열에서 부울로) CSV를 가져오기 전에 대시보드의 [**커스텀 속성**]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) 페이지에서 데이터 유형을 업데이트합니다. CSV의 데이터 유형이 속성의 현재 정의된 데이터 유형과 일치하지 않으면 가져오기가 오류와 함께 실패합니다.

#### 여러 데이터 유형 {#multiple-data-types}

Braze는 열의 각 값이 동일한 데이터 유형일 것으로 예상합니다. 속성의 데이터 유형과 일치하지 않는 값은 세분화 시 오류를 유발합니다.

또한 숫자 속성을 0으로 시작하면 0으로 시작하는 숫자가 문자열로 간주되므로 문제가 발생합니다. Braze가 해당 문자열을 변환할 때 8진수 값(0에서 7까지의 숫자를 사용)으로 처리될 수 있으며, 이는 해당 10진수 값으로 변환됩니다. 예를 들어 CSV 파일의 값이 0130이면 Braze 프로필에는 88이 표시됩니다. 이 문제를 방지하려면 문자열 데이터 유형의 속성을 사용합니다. 그러나 이 데이터 유형은 세분화 숫자 비교에서 사용할 수 없습니다.

#### 기본 속성 유형 {#default-attribute-types}

일부 기본 속성은 사용자 업데이트에 유효한 특정 값만 허용할 수 있습니다. 지침은 [CSV 구성하기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)를 참조합니다.

후행 공백과 대소문자 차이로 인해 값이 유효하지 않은 것으로 해석될 수 있습니다. 예를 들어 다음 CSV 파일에서 첫 번째 행의 사용자(`brazetest1`)만 이메일 및 푸시 상태가 성공적으로 업데이트됩니다. 허용되는 값은 `unsubscribed`, `subscribed`, `opted_in`이기 때문입니다.

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@example.com,unsubscribed,unsubscribed
brazetest2,test2@example.com,Unsubscribed,Unsubscribed
```

### "CSV 파일 선택"이 작동하지 않음 {#select-csv-file-is-not-working}

**CSV 파일 선택** 버튼이 작동하지 않는 데에는 여러 가지 이유가 있습니다:

| 문제 | 해결 방법 |
|---|---|
| 팝업 차단기 | 페이지가 표시되지 않을 수 있습니다. 브라우저가 Braze 대시보드 웹사이트에서 팝업을 허용하고 있는지 확인합니다. |
| 오래된 브라우저 | 브라우저가 최신 상태인지 확인합니다. 최신 상태가 아니면 최신 버전으로 업데이트합니다. |
| 백그라운드 프로세스 | 모든 브라우저 인스턴스를 닫은 다음 컴퓨터를 다시 시작합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="'CSV 파일 선택'이 작동하지 않음" }