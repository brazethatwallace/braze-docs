---
nav_title: 사용자 데이터 및 CSV 이벤트 가져오기
article_title: 사용자 데이터 및 CSV 이벤트 가져오기
permalink: "/csv_events/"
description: "이 참조 문서에서는 사용자 데이터를 가져오는 방법과 CSV 파일을 사용하여 커스텀 이벤트를 가져오는 방법을 다룹니다."
page_type: reference
---

# 사용자 데이터 가져오기(CSV 이벤트 얼리 액세스) {#importing-user-data-csv-events-early-access}

> Braze는 플랫폼에 사용자 데이터를 가져오는 다양한 방법을 제공합니다: SDK, API, 클라우드 데이터 수집, 기술 파트너 통합, CSV 파일 등이 있습니다. 이 문서에서는 [CSV 파일을 통한 커스텀 이벤트 가져오기(얼리 액세스)](#importing-custom-events)를 포함하여 사용자 데이터를 가져오는 방법에 대한 자세한 안내를 제공합니다.

{% alert important %}
법적으로 필수인 트랜잭션 이메일을 SMS 게이트웨이로 보내지 마세요. 해당 이메일이 전달되지 않을 가능성이 높습니다.

전화번호와 통신사의 이메일-SMS 게이트웨이 도메인(MM3)을 사용하여 보내는 이메일은 SMS(문자) 메시지로 수신될 수 있지만, 일부 이메일 제공업체는 이 동작을 지원하지 않습니다. 예를 들어 T-Mobile 전화번호(예: "9999999999@tmomail.net")로 이메일을 보내면 T-Mobile 네트워크에서 해당 전화번호를 소유한 사람에게 SMS 메시지가 전송됩니다.

이러한 이메일이 SMS 게이트웨이로 전달되지 않더라도 이메일 요금 청구에는 포함됩니다. 지원되지 않는 게이트웨이로 이메일을 보내지 않으려면 [지원되지 않는 게이트웨이 도메인 이름 목록](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads)을 검토하세요.
{% endalert %}


진행하기 전에, Braze는 가져오기 중에 HTML 데이터를 정제(유효성 검사 또는 올바른 형식 지정)하지 않는다는 점에 유의하세요. 이는 웹 개인화를 위한 모든 가져오기 데이터에서 스크립트 태그를 제거해야 함을 의미합니다.

## REST API

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하여 사용자의 커스텀 이벤트, 사용자 속성 및 구매를 기록할 수 있습니다.

## CSV 가져오기 {#csv-import}

**오디언스** > **사용자 가져오기**에서 CSV 파일을 통해 사용자 프로필을 업로드하고 업데이트할 수 있습니다.

CSV 파일을 사용한 사용자 데이터 가져오기는 이름, 이메일 등의 사용자 속성과 신발 사이즈 같은 커스텀 속성의 기록 및 업데이트를 지원합니다. 두 가지 고유 사용자 식별자 중 하나를 지정하여 CSV를 가져올 수 있습니다: `external_id` 또는 사용자 별칭.

{% alert important %}
사용자 가져오기는 사용자 커스텀 이벤트의 기록 및 업데이트도 지원합니다. 사용자 속성과 유사하게, `external_id`, `braze_id`, 또는 `user_alias_name`과 `user_alias_label`을 사용하여 가져올 수 있습니다. 자세한 내용은 [커스텀 이벤트 가져오기](#importing-custom-events)를 참조하세요.
{% endalert %}

{% alert note %}
`external_id`가 있는 사용자와 없는 사용자를 혼합하여 업로드하는 경우, 각 가져오기에 대해 별도의 CSV 파일을 생성해야 합니다. 하나의 CSV 파일에 `external_ids`와 사용자 별칭을 모두 포함할 수 없습니다.
{% endalert %}

### 외부 ID로 가져오기 {#importing-with-external-id}

고객 데이터를 가져올 때 각 고객의 고유 식별자(`external_id`라고도 함)를 지정해야 합니다. CSV 가져오기를 시작하기 전에 엔지니어링 팀에서 Braze에서 사용자를 어떻게 식별할지 파악하는 것이 중요합니다. 일반적으로 이것은 내부 데이터베이스 ID입니다. 이는 모바일 및 웹에서 Braze SDK가 사용자를 식별하는 방식과 일치해야 하며, 각 고객이 기기 전체에서 Braze 내에 단일 고객 프로필을 갖도록 설계되었습니다. Braze [사용자 프로필 수명주기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle)에 대해 자세히 알아보세요.

가져오기에서 `external_id`를 제공하면 Braze는 동일한 `external_id`를 가진 기존 사용자를 업데이트하거나, 찾을 수 없는 경우 해당 `external_id`가 설정된 새로 식별된 사용자를 생성합니다.

- **다운로드:** [CSV 속성 가져오기 템플릿][import_template]
- **다운로드:** [CSV 이벤트 가져오기 템플릿][events_template]

### 사용자 별칭으로 가져오기 {#importing-with-user-alias}

`external_id`가 없는 사용자를 대상으로 하려면 사용자 별칭이 포함된 사용자 목록을 가져올 수 있습니다. 별칭은 대체 고유 사용자 식별자 역할을 하며, 가입하지 않았거나 앱에서 계정을 만들지 않은 익명 사용자에게 마케팅하려는 경우 유용할 수 있습니다.

별칭만 있는 사용자 프로필을 업로드하거나 업데이트하는 경우, CSV에 다음 두 열이 포함되어야 합니다:

- `user_alias_name`: 고유 사용자 식별자; `external_id`의 대안
- `user_alias_label`: 사용자 별칭을 그룹화하기 위한 공통 레이블

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

가져오기에서 `user_alias_name`과 `user_alias_label`을 모두 제공하면 Braze는 동일한 `user_alias_name` 및 `user_alias_label`을 가진 기존 사용자를 업데이트합니다. 사용자를 찾을 수 없는 경우 Braze는 해당 `user_alias_name`이 설정된 새로 식별된 사용자를 생성합니다.

{% alert important %}
이미 `external_id`가 있는 기존 사용자에게 `user_alias_name`을 업데이트하기 위해 CSV 가져오기를 사용할 수 없습니다. 대신 연결된 `user_alias_name`으로 새 사용자 프로필이 생성됩니다. 별칭만 있는 사용자를 `external_id`와 연결하려면 [사용자 식별 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)를 사용하세요.
{% endalert %}

- **다운로드:** [CSV 별칭 속성 가져오기 템플릿][template_alias_attributes]
- **다운로드:** [CSV 별칭 이벤트 가져오기 템플릿][template_alias_events]

### Braze ID로 가져오기 {#importing-with-braze-id}

`external_id` 또는 `user_alias_name`과 `user_alias_label` 값 대신 내부 Braze ID 값을 사용하여 Braze의 기존 사용자 프로필을 업데이트하려면 `braze_id`를 열 헤더로 지정하세요.

이는 세분화 내 CSV 내보내기 옵션을 통해 Braze에서 사용자 데이터를 내보낸 후 해당 기존 사용자에게 새 커스텀 속성을 추가하려는 경우 유용할 수 있습니다.

{% alert important %}
`braze_id`를 사용하여 CSV 가져오기로 새 사용자를 생성할 수 없습니다. 이 방법은 Braze 플랫폼 내 기존 사용자를 업데이트하는 데만 사용할 수 있습니다.
{% endalert %}

{% alert tip %}
Braze 대시보드의 CSV 내보내기에서 `braze_id` 값이 `Appboy ID`로 표시될 수 있습니다. 이 ID는 사용자의 `braze_id`와 동일하므로 CSV를 다시 가져올 때 이 열의 이름을 `braze_id`로 변경할 수 있습니다.
{% endalert %}

### 기본 속성 가져오기 {#importing-default-attributes}

사용자의 기본 속성을 가져오려면 **사용자 가져오기** > **속성**으로 이동하세요. 기본 사용자 속성은 Braze의 예약 키입니다. 예를 들어, `first_name` 또는 `email`이 있습니다. 커스텀 속성은 비즈니스에 맞게 커스텀됩니다. 예를 들어, 여행 예약 앱에는 `last_destination_searched`라는 커스텀 속성이 있을 수 있습니다.

{% alert important %}
고객 데이터를 속성으로 가져올 때 사용하는 열 헤더는 기본 사용자 속성의 철자와 대소문자가 정확히 일치해야 합니다. 그렇지 않으면 Braze가 해당 사용자 프로필에 커스텀 속성을 자동으로 생성합니다.
{% endalert %}

#### 기본 사용자 데이터 열 헤더 {#default-user-data-column-headers}

| 사용자 프로필 필드 | 데이터 유형 | 정보 | 필수 여부 |
|---|---|---|---|
| `external_id` | 문자열 | 고객의 고유 사용자 식별자. | 예, [다음 참고 사항](#about-external-ids)을 참조하세요. |
| `user_alias_name` | 문자열 | 익명 사용자의 고유 사용자 식별자. `external_id`의 대안. | 아니요, [다음 참고 사항](#about-external-ids)을 참조하세요. |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화하기 위한 공통 레이블. | 예, `user_alias_name`이 사용되는 경우. |
| `first_name` | 문자열 | 사용자가 표시한 이름(예: `Jane`). | 아니요 |
| `last_name` | 문자열 | 사용자가 표시한 성(예: `Doe`). | 아니요 |
| `email` | 문자열 | 사용자가 표시한 이메일(예: `jane.doe@braze.com`). | 아니요 |
| `country` | 문자열 | 국가 코드는 ISO-3166-1 alpha-2 표준으로 Braze에 전달해야 합니다(예: `GB`). | 아니요 |
| `dob` | 문자열 | "YYYY-MM-DD" 형식으로 전달해야 합니다(예: `1980-12-21`). 이렇게 하면 사용자의 생년월일이 가져와지며 생일이 "오늘"인 사용자를 타겟팅할 수 있습니다. | 아니요 |
| `gender` | 문자열 | "M", "F", "O"(기타), "N"(해당 없음), "P"(밝히고 싶지 않음) 또는 nil(알 수 없음). | 아니요 |
| `home_city` | 문자열 | 사용자가 표시한 거주 도시(예: `London`). | 아니요 |
| `language` | 문자열 | 언어는 ISO-639-1 표준으로 Braze에 전달해야 합니다(예: `en`). <br>[허용되는 언어 목록]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes)을 참조하세요. | 아니요 |
| `phone` | 문자열 | 사용자가 표시한 전화번호, `E.164` 형식(예: `+442071838750`). <br>서식 안내는 [사용자 전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers)를 참조하세요. | 아니요 |
| `email_open_tracking_disabled` | 불리언 | true 또는 false가 허용됩니다. true로 설정하면 이 사용자에게 향후 발송되는 모든 이메일에 오픈 추적 픽셀이 추가되지 않습니다. | 아니요 |
| `email_click_tracking_disabled` | 불리언 | true 또는 false가 허용됩니다. true로 설정하면 이 사용자에게 향후 발송되는 이메일의 모든 링크에 대한 클릭 추적이 비활성화됩니다. | 아니요 |
| `email_subscribe` | 문자열 | 사용 가능한 값: `opted_in`(이메일 메시지 수신에 명시적으로 등록), `unsubscribed`(이메일 메시지 수신을 명시적으로 거부), `subscribed`(수신 동의도 거부도 하지 않음). | 아니요 |
| `push_subscribe` | 문자열 | 사용 가능한 값: `opted_in`(푸시 메시지 수신에 명시적으로 등록), `unsubscribed`(푸시 메시지 수신을 명시적으로 거부), `subscribed`(수신 동의도 거부도 하지 않음). | 아니요 |
| `time_zone` | 문자열 | 시간대는 IANA 시간대 데이터베이스와 동일한 형식으로 Braze에 전달해야 합니다(예: `America/New_York` 또는 `Eastern Time (US & Canada)`). | 아니요 |
| `date_of_first_session` <br><br> `date_of_last_session`| 문자열 | 다음 ISO-8601 형식 중 하나로 전달할 수 있습니다: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (예: 2019-11-20T18:38:57) </li> </ul> {:/} | 아니요 |
| `subscription_group_id` | 문자열 | 구독 그룹의 `id`. 이 식별자는 대시보드의 구독 그룹 페이지에서 확인할 수 있습니다. | 아니요 |
| `subscription_state` | 문자열 | `subscription_group_id`에 지정된 구독 그룹의 구독 상태. 허용되는 값: `unsubscribed`(구독 그룹에 미포함) 또는 `subscribed`(구독 그룹에 포함). | 아니요, 그러나 `subscription_group_id`가 사용되는 경우 강력히 권장합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### 외부 ID에 대하여 {#about-external-ids}

`external_id`는 필수는 아니지만 다음 필드 중 하나를 **반드시** 포함해야 합니다:
- `external_id`: 고객의 고유 사용자 식별자, **또는**
- `braze_id`: 기존 Braze 사용자에 대해 가져온 고유 사용자 식별자, **또는**
- `user_alias_name` 및 `user_alias_label`: 익명 사용자의 고유 사용자 식별자

### 커스텀 속성 가져오기 {#importing-custom-attributes}

**사용자 가져오기** > **속성**으로 이동하여 사용자의 커스텀 속성을 가져올 수 있습니다. 기본 속성과 정확히 일치하지 않는 헤더는 Braze 내에서 커스텀 속성을 생성합니다.

사용자 가져오기에서 허용되는 데이터 유형은 다음과 같습니다:

| 데이터 유형 | 설명 |
|-----------|-------------|
| 날짜/시간 | ISO-8601 형식으로 저장해야 합니다 |
| 불리언 | TRUE 또는 FALSE |
| 숫자 | 공백이나 쉼표가 없는 정수 또는 플로트, 플로트는 마침표(.)를 소수점 구분자로 사용해야 합니다 |
| 문자열 | 열 값을 큰따옴표로 감싸면 쉼표를 포함할 수 있습니다 |
| 공란 | 공란 값은 고객 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 모든 기존 사용자 속성을 포함할 필요가 없습니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
배열과 푸시 토큰은 사용자 가져오기에서 지원되지 않습니다. 특히 배열의 경우 CSV 파일의 쉼표가 열 구분자로 해석되므로 값의 쉼표가 파일 파싱 오류를 유발합니다. <br>이러한 유형의 값을 업로드하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion)을 사용하세요.
{% endalert %}

### 구독 그룹 상태 업데이트 {#updating-subscription-group-status}

사용자 가져오기를 통해 이메일 또는 SMS 구독 그룹에 사용자를 추가할 수 있습니다. 이는 사용자가 SMS 채널로 메시지를 받으려면 SMS 구독 그룹에 등록되어야 하므로 SMS에 특히 유용합니다. 자세한 내용은 [SMS 구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#subscription-group-mms-enablement)을 참조하세요.

구독 그룹 상태를 업데이트하는 경우 CSV에 다음 두 열이 포함되어야 합니다:

- `subscription_group_id`: [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups)의 `id`.
- `subscription_state`: 사용 가능한 값: `unsubscribed`(구독 그룹에 미포함) 또는 `subscribed`(구독 그룹에 포함).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="구독 그룹 상태 업데이트">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
</tbody>
</table>

{% alert important %}
사용자 가져오기에서 행당 하나의 `subscription_group_id`만 설정할 수 있습니다. 행마다 다른 `subscription_group_id` 값을 가질 수 있습니다. 그러나 동일한 사용자를 여러 구독 그룹에 등록해야 하는 경우 여러 번 가져오기를 수행해야 합니다.
{% endalert %}

### 커스텀 이벤트 가져오기 (얼리 액세스) {#importing-custom-events}

{% alert important %}
커스텀 이벤트 가져오기는 현재 얼리 액세스 단계입니다. 얼리 액세스 참여에 관심이 있으시면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

사용자의 커스텀 이벤트를 가져오려면 **사용자 가져오기** > **이벤트**로 이동하세요.

커스텀 이벤트는 비즈니스에 맞게 커스텀됩니다. 예를 들어, 스트리밍 앱에는 rented_movie라는 커스텀 이벤트가 있을 수 있습니다. CSV에는 다음 열 헤더가 포함되어야 합니다:

- 다음 중 하나:
  - `external_id`, **또는**
  - `braze_id`, **또는**
  - `user_alias_name` 및 `user_alias_label`
- Name
- Time

커스텀 이벤트에는 이벤트 속성정보가 포함될 수 있습니다. 예를 들어, 커스텀 이벤트 rented_movie에는 title과 genre라는 속성정보가 있을 수 있습니다. 이러한 이벤트 속성정보의 열 헤더는 `<event_name>.properties.<property name>` 형식이어야 합니다. 예: `rented_movie.properties.title`.

| 사용자 프로필 필드 | 데이터 유형 | 정보 | 필수 여부 |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id` | 문자열 | 사용자의 고유 사용자 식별자. | 예, `external_id`, `braze_id`, 또는 `user_alias_name`과 `user_alias_label` 중 하나가 필요합니다. |
| `braze_id` | 문자열 | 사용자에 대해 Braze가 할당한 식별자. | 예, `external_id`, `braze_id`, 또는 `user_alias_name`과 `user_alias_label` 중 하나가 필요합니다. |
| `user_alias_name` | 문자열 | 익명 사용자의 고유 사용자 식별자. external_id의 대안. | 예, `external_id`, `braze_id`, 또는 `user_alias_name`과 `user_alias_label` 중 하나가 필요합니다. |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화하기 위한 공통 레이블. | 예, `external_id`, `braze_id`, 또는 `user_alias_name`과 `user_alias_label` 중 하나가 필요합니다. |
| `name` | 문자열 | 사용자의 커스텀 이벤트. | 예 |
| `time` | 문자열 | 이벤트 시간. 다음 ISO-8601 형식 중 하나로 전달할 수 있습니다: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (예: 2019-11-20T18:38:57) </li> </ul> {:/} | 예 |
| `<event name>.properties.<property name>` | 다양 | 커스텀 이벤트와 연결된 이벤트 속성정보. 예: `rented_movie.properties.title` | 아니요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
external_id 자체는 필수는 아니지만 다음 필드 중 하나를 반드시 포함해야 합니다: <br>- `external_id`: 고객의 고유 사용자 식별자 <br>- `braze_id`: 기존 Braze 사용자에 대해 가져온 고유 사용자 식별자 <br>- `user_alias_name`: 익명 사용자의 고유 사용자 식별자
{% endalert %}

#### CSV 크기 {#csv-size}

Braze는 최대 500 MB 크기의 파일에서 표준 CSV 형식의 사용자 데이터를 허용합니다. CSV 파일 템플릿을 다운로드하려면 [외부 ID로 가져오기](#importing-with-external-id) 또는 [사용자 별칭으로 가져오기](#importing-with-user-alias)를 참조하세요.

#### 데이터 포인트 고려사항 {#data-point-considerations}

CSV를 통해 가져온 각 고객 데이터는 고객 프로필의 기존 값을 덮어쓰며, 외부 ID와 공란 값을 제외하고 데이터 포인트로 계산됩니다.

- CSV 가져오기를 통해 업로드된 외부 ID는 데이터 포인트를 소비하지 않습니다. 외부 ID만 업로드하여 기존 Braze 사용자를 세분화하기 위해 CSV 파일을 업로드하는 경우, 데이터 포인트를 소비하지 않고 수행할 수 있습니다. 가져오기에서 사용자의 이메일이나 전화번호와 같은 추가 데이터를 추가하면 기존 사용자 데이터를 덮어쓰고 데이터 포인트를 소비합니다.
    - 세분화 목적의 CSV 가져오기(`external_id`, `braze_id` 또는 `user_alias_name`만을 유일한 필드로 사용한 가져오기)는 데이터 포인트를 소비하지 않습니다.
- 공란 값은 고객 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 모든 기존 사용자 속성이나 커스텀 이벤트를 포함할 필요가 없습니다.
- `email_subscribe`, `push_subscribe`, `subscription_group_id` 또는 `subscription_state`를 업데이트하는 것은 데이터 포인트 소비에 포함되지 않습니다.

{% alert important %}
CSV 가져오기 또는 API를 통해 사용자의 언어나 국가를 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 캡처하지 않습니다.
{% endalert %}

## CSV 가져오기 {#importing-a-csv}

CSV 파일을 가져오려면:
1. **오디언스** > **사용자 가져오기**로 이동합니다.
2. **파일 찾아보기**를 선택하고 원하는 파일을 선택한 다음 **가져오기 시작**을 선택합니다. Braze가 파일을 업로드하고 열 헤더와 각 열의 데이터 유형을 확인합니다.

{% alert important %}
CSV 가져오기는 대소문자를 구분합니다. CSV 가져오기에서 대문자를 사용하면 해당 필드가 기본 속성이 아닌 커스텀 속성으로 기록됩니다. 예를 들어 "email"은 올바르지만, "Email"은 커스텀 속성으로 기록됩니다.
{% endalert %}

![가져올 사용자 정보 유형으로 "이벤트" 옵션이 선택된 화면][5]

업로드가 완료되면 파일 내용의 미리보기를 확인할 수 있습니다. 표의 정보는 CSV 파일의 상위 행에 있는 값을 기반으로 합니다.

**사용자 가져오기** 페이지에서 진행 상황을 추적할 수 있으며, 이 페이지는 5초마다 새로고침되거나 **테이블 새로고침**을 선택하면 업데이트됩니다. 가져오기 중에도 Braze 대시보드의 나머지 기능을 계속 사용할 수 있으며, 가져오기가 시작되고 종료될 때 알림을 받게 됩니다.

또한 가장 최근 가져오기 내역, 파일 이름, CSV 유형, 파일의 총 행 수, 성공적으로 가져온 행 수, 각 파일의 전체 행 수, 각 가져오기의 상태를 확인할 수 있습니다.

동시에 두 개 이상의 CSV 파일을 가져올 수 있습니다. CSV 가져오기는 동시에 실행되므로 업데이트 순서가 순차적으로 보장되지 않습니다. CSV 가져오기를 순차적으로 실행해야 하는 경우, 두 번째 파일을 업로드하기 전에 첫 번째 CSV 가져오기가 완료될 때까지 기다려야 합니다.

가져오기 프로세스 중 오류가 발생하면 파일의 전체 행 수 옆에 경고 아이콘이 표시됩니다. 아이콘 위에 마우스를 올리면 특정 행이 실패한 이유에 대한 세부 정보를 확인할 수 있습니다. 가져오기가 완료되면 모든 데이터가 기존 프로필에 추가되거나 새 프로필이 생성됩니다.

![단일 열에서 혼합된 데이터 유형으로 인한 오류가 발생한 CSV 파일 업로드 완료 화면][4]{: style="max-width:70%"}

### 고려 사항 {#considerations}

업로드 중 Braze가 파일의 상위 행에서 형식 오류를 감지하면 해당 오류가 요약과 함께 표시됩니다. 예를 들어 파일에 잘못된 형식의 행이 포함되어 있으면, 파일을 가져올 때 미리보기에서 이 오류가 표시됩니다. 오류가 있는 파일도 가져올 수 있지만, 가져오기를 계속하기 전에 파일에서 해당 오류를 수정하는 것이 좋습니다.

또한 Braze는 미리보기를 위해 입력 파일의 모든 행을 스캔하지 않으므로, 업로드 전에 전체 CSV 파일을 검토하는 것이 중요합니다. 이는 Braze가 미리보기를 생성하는 동안 감지하지 못하는 오류가 존재할 수 있음을 의미합니다.

잘못된 형식의 행과 외부 ID가 없는 행은 가져오지 않습니다. 다른 모든 오류는 가져올 수 있지만, Segment를 생성할 때 필터링에 영향을 줄 수 있습니다. 자세한 내용은 [문제 해결](#troubleshooting) 섹션을 참조하세요.

{% alert warning %}
오류는 데이터 유형과 파일 구조에만 기반합니다. 예를 들어 형식이 잘못된 이메일 주소도 문자열로 파싱할 수 있으므로 그대로 가져오게 됩니다.
{% endalert %}

### Lambda 사용자 CSV 가져오기 {#lambda-user-csv-import}

서버리스 S3 Lambda CSV 가져오기 스크립트를 사용하여 사용자 속성을 플랫폼에 업로드할 수 있습니다. 이 솔루션은 CSV 업로더로 작동하며, S3 버킷에 CSV를 드롭하면 스크립트가 API를 통해 업로드합니다.

100만 행이 포함된 파일의 예상 실행 시간은 약 5분입니다. 자세한 내용은 [사용자 속성 CSV를 Braze로 가져오기]({{site.baseurl}}/user_csv_lambda)를 참조하세요.

## 세분화 {#segmenting}

사용자 가져오기는 고객 프로필을 생성 및 업데이트하며, Segments를 생성하는 데에도 사용할 수 있습니다. Segment를 생성하려면 가져오기를 시작하기 전에 **이 CSV에서 가져온 사용자로부터 자동으로 Segment 생성**을 선택하세요.

Segment의 이름을 설정하거나, 파일 이름인 기본값을 사용할 수 있습니다. Segment를 생성하는 데 사용된 파일은 가져오기가 완료된 후 해당 Segment를 볼 수 있는 링크가 표시됩니다.

Segment를 생성하는 데 사용되는 필터는 선택한 가져오기에서 생성되거나 업데이트된 사용자를 선택하며, Segment 편집 페이지에서 다른 모든 필터와 함께 사용할 수 있습니다.

## 문제 해결 {#troubleshooting}

### 누락된 행 {#missing-rows}

가져온 사용자 수가 CSV 파일의 총 행 수와 일치하지 않는 데에는 몇 가지 이유가 있습니다:

- **중복 외부 ID:** 중복된 외부 ID 열이 있으면 행이 올바르게 형식화되어 있더라도 형식이 잘못되거나 가져오지 않은 행이 발생할 수 있습니다. 경우에 따라 특정 오류가 보고되지 않을 수 있습니다. CSV에 중복된 외부 ID가 있는지 확인하세요. 있다면 중복을 제거하고 다시 업로드해 보세요.
- **악센트 문자:** CSV 파일에 악센트가 포함된 이름이나 속성이 있을 수 있습니다. 문제를 방지하려면 파일이 UTF-8로 인코딩되어 있는지 확인하세요.

### 형식이 잘못된 행 {#malformed-row}

데이터를 올바르게 가져오려면 CSV 파일에 헤더 행을 포함해야 합니다. 각 행은 헤더 행과 동일한 수의 셀을 가져야 합니다. 헤더 행보다 값이 많거나 적은 행은 가져오기에서 제외됩니다. 값에 포함된 쉼표는 구분자로 해석되어 이 오류가 발생할 수 있습니다. 또한 모든 데이터는 UTF-8로 인코딩되어야 합니다.

CSV 파일에 빈 행이 있고 CSV 파일의 총 줄 수보다 적은 행이 가져와진 경우, 빈 행은 가져올 필요가 없으므로 가져오기에 문제가 있음을 나타내지 않을 수 있습니다. 올바르게 가져온 줄 수를 확인하고 가져오려는 사용자 수와 일치하는지 확인하세요.

### 여러 데이터 유형 {#multiple-data-types}

Braze는 열의 각 값이 동일한 데이터 유형일 것으로 예상합니다. 속성의 데이터 유형과 일치하지 않는 값은 세분화 시 오류를 발생시킵니다.

### 잘못된 형식의 날짜 {#incorrectly-formatted-dates}

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식이 아닌 날짜는 가져오기 시 날짜/시간으로 읽히지 않습니다.

### 문자열 따옴표 {#string-quotation}

작은따옴표('') 또는 큰따옴표("")로 감싸진 값은 가져오기 시 문자열로 읽힙니다.

### 커스텀 속성으로 가져온 데이터 {#data-imported-as-custom-attribute}

기본 사용자 데이터(예: `email` 또는 `first_name`)가 커스텀 속성으로 가져와지는 경우 CSV 파일의 대소문자와 간격을 확인하세요. 예를 들어 `First_name`은 커스텀 속성으로 가져와지지만 `first_name`은 사용자 프로필의 "first name" 필드에 올바르게 가져와집니다.

[import_template]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/unlisted_docs/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/unlisted_docs/download_file/braze-events-csv-example-user-alias.csv %}
[3]: {% image_buster /assets/unlisted_docs/img/importcsv5.png %}
[4]: {% image_buster /assets/unlisted_docs/img/importcsv2.png %}
[5]: {% image_buster /assets/unlisted_docs/img/importcsv3.png %}
[7]: {% image_buster /assets/unlisted_docs/img/segment-imported-users.png %}
[8]: {% image_buster /assets/unlisted_docs/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/unlisted_docs/img/subscription_group_import.png %}