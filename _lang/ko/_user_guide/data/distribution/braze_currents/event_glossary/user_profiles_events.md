---
nav_title: 고객 프로필
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "이 용어집은 Braze가 추적하고 Currents를 사용하여 선택한 데이터 웨어하우스로 전송할 수 있는 고객 프로필 업데이트를 나열합니다."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert tip %}
이러한 이벤트는 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder), [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)에서 SQL 테이블로도 사용할 수 있습니다. SQL 테이블 스키마 및 열 세부 정보는 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)를 확인하세요. Snowflake 데이터 공유의 고객 프로필 속성 뷰 스키마는 [고객 프로필 속성]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes)을 참조하세요.
{% endalert %}

추가 이벤트 권한에 대한 액세스가 필요한 경우 Braze 담당자에게 문의하거나 [고객지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 열어주세요. 이 페이지에서 필요한 정보를 찾을 수 없는 경우 [고객 행동 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [메시지 인게이지먼트 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 또는 [Currents 샘플 데이터 예시](https://github.com/Appboy/currents-examples/tree/master/sample-data)를 참조하세요.

{% details 고객 프로필 업데이트 이벤트 구조 설명 %}

### 이벤트 구조 {#event-structure}

이 고객 행동 및 사용자 이벤트 분석은 고객 프로필 업데이트 이벤트에 일반적으로 포함되는 정보 유형을 보여줍니다. 구성 요소를 확실히 이해하면 개발자와 비즈니스 인텔리전스 전략 팀이 수신되는 Currents 이벤트 데이터를 활용하여 데이터 중심 보고서와 차트를 만들고, 기타 유용한 데이터 측정기준을 활용할 수 있습니다.

{% alert important %}
스토리지 스키마는 Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage와 같은 데이터 웨어하우스 스토리지 파트너에게 전송되는 플랫 파일 이벤트 데이터에 적용됩니다. 여기에 나열된 일부 이벤트 및 대상 조합은 아직 일반적으로 제공되지 않습니다. 파트너별 지원 이벤트에 대한 정보는 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) 및 관련 파트너 페이지를 참조하세요.

Currents는 페이로드가 900KB보다 큰 이벤트를 삭제합니다.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->


{% api %}
## 사용자 삭제 요청 이벤트 {#user-delete-request-events}

{% apitags %}
User Delete Request
{% endapitags %}

고객 요청에 의해 사용자가 삭제될 때 발생합니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.UserDeleteRequest

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.UserDeleteRequest

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 사용자 고아 이벤트 {#user-orphan-events}

{% apitags %}
User Orphan
{% endapitags %}

사용자가 고아 상태가 될 때 발생하며, 이는 해당 사용자가 다른 사용자의 프로필과 병합되었음을 의미합니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.UserOrphan

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "orphaned_by_id" : "(required, string) BSON ID of the user whose profile was merged with the orphaned user's profile",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.UserOrphan

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "orphaned_by_id" : "(required, string) BSON ID of the user whose profile was merged with the orphaned user's profile"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 고객 프로필 업데이트 이벤트 {#user-profile-update-events}

{% apitags %}
Profile
{% endapitags %}

사용자의 프로필 업데이트를 나타냅니다.

{% alert important %}
고객 프로필 업데이트 이벤트는 베타 버전입니다. 액세스하려면 고객 성공 매니저 또는 계정 매니저에게 문의하세요.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.profile.Update

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
  "country" : "(optional, string) [PII] Country of the user",
  "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
  "dob" : "(optional, string) [PII] Date of birth of the user in ISO-8601 format",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "first_name" : "(optional, string) [PII] First name of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "home_city" : "(optional, string) [PII] Home city of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "last_name" : "(optional, string) [PII] Last name of the user",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "time_ms" : "(required, long) Time in milliseconds when the update happened",
  "timezone" : "(optional, string) Time zone of the user",
  "update_source" : "(required, string) The source of this update",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.profile.Update

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
    "country" : "(optional, string) [PII] Country of the user",
    "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
    "dob" : "(optional, string) [PII] Date of birth of the user in ISO-8601 format",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "first_name" : "(optional, string) [PII] First name of the user",
    "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
    "home_city" : "(optional, string) [PII] Home city of the user",
    "language" : "(optional, string) [PII] Language of the user",
    "last_name" : "(optional, string) [PII] Last name of the user",
    "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
    "time_ms" : "(required, long) Time in milliseconds when the update happened",
    "update_source" : "(required, string) The source of this update"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}