---
nav_title: 고객 행동 및 사용자 이벤트
article_title: 고객 행동 및 사용자 이벤트
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 Currents를 사용하여 추적하고 선택한 데이터 웨어하우스로 전송할 수 있는 다양한 고객 행동 및 사용자 이벤트가 나열되어 있습니다."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details 스키마 범위 및 관련 리소스 %}

저장 스키마는 데이터 웨어하우스 저장 파트너(Google Cloud Storage, Amazon S3 및 Microsoft Azure Blob Storage)로 전송하는 플랫 파일 이벤트 데이터에 적용됩니다. 여기에 나열된 일부 이벤트와 대상 조합은 아직 일반적으로 사용할 수 없습니다. 다양한 파트너가 지원하는 이벤트에 대한 자세한 내용은 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) 목록을 참조하여 각 페이지를 확인하세요.

{% alert tip %}
이러한 이벤트는 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder), [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)에서 SQL 테이블로도 사용할 수 있습니다. SQL 테이블 스키마 및 열 세부 정보는 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)를 참조하세요.
{% endalert %}

추가 이벤트 자격에 대한 액세스가 필요한 경우 Braze 담당자에게 문의하거나 [고객지원 티켓]({{site.baseurl}}/braze_support)을 개설하세요. 이 페이지에서 필요한 정보를 찾을 수 없다면 [메시지 인게이지먼트 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 또는 [Currents 샘플 데이터 예시](https://github.com/Appboy/currents-examples/tree/master/sample-data)를 확인하세요.

{% enddetails %}

{% details 고객 행동 및 사용자 이벤트 구조와 플랫폼 값 설명 %}

## 이벤트 구조 {#event-structure}

이 고객 행동 및 사용자 이벤트 분석은 일반적으로 고객 행동 또는 사용자 이벤트에 어떤 유형의 정보가 포함되는지 보여줍니다. 구성요소에 대한 확실한 이해를 바탕으로 개발자와 비즈니스 인텔리전스 전략 팀은 수신되는 Currents 이벤트 데이터를 사용하여 데이터 중심 보고서와 차트를 만들고 다른 유용한 데이터 측정기준을 활용할 수 있습니다.

![사용자별 속성정보, 행동별 속성정보 및 기기별 속성정보로 그룹화된 구매 이벤트를 보여주는 사용자 이벤트 분류]({% image_buster /assets/img/customer_engagement_event.png %})

고객 행동 및 사용자 이벤트는 **사용자별** 속성정보, **행동별** 속성정보, **기기별** 속성정보로 구성됩니다.

### 플랫폼 값 {#platform-values}

특정 이벤트는 사용자 기기의 플랫폼을 지정하는 `platform` 값을 반환합니다.
<br>다음 표에서는 반환 가능한 값을 자세히 설명합니다:

| 사용자 기기 | 플랫폼 값 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| 웹 | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="플랫폼 값" }

{% enddetails %}

{% details 고객 행동 및 사용자 이벤트에 대한 고려 사항 %}

- Currents는 페이로드가 900&nbsp;KB를 초과하는 지나치게 큰 이벤트는 삭제합니다.
- 이 용어집의 많은 이벤트는 SDK에서 시작됩니다. `token_state_change`와 같은 일부 이벤트는 SDK 또는 백엔드에서 시작될 수 있습니다(예: 푸시 반송에 대한 응답으로). `sdk_version`, `gender`, `language`, `country` 필드는 SDK에서 시작된 이벤트에만 설정됩니다. 백엔드에서 시작된 이벤트이거나 해당 정보를 사용할 수 없거나 사용자에 대해 설정되지 않은 경우, 이러한 필드는 `null`일 수 있습니다.

{% enddetails %}

</div>

<!--overview-end-->

{% api %}
## 무작위 버킷 번호 업데이트 이벤트 {#random-bucket-number-update-events}

{% apitags %}
Random Bucket Number
{% endapitags %}

이 사용자 이벤트는 워크스페이스 내에서 새 사용자가 생성될 때마다 발생합니다. 이 이벤트 동안 각 신규 사용자에게 무작위 버킷 번호가 할당되며, 이를 사용하여 무작위 사용자의 균일하게 분포된 세그먼트를 생성할 수 있습니다. 이를 사용하여 무작위 버킷 번호 값의 범위를 그룹화하고 Campaigns 및 캠페인 배리언트 간의 성능을 비교할 수 있습니다.

{% alert important %}
이 Currents 이벤트는 "모든 이벤트 커넥터"를 구매한 고객만 사용할 수 있으며, Amazon S3, Microsoft Azure 및 Google Cloud Storage와 같은 저장 이벤트 커넥터에만 사용할 수 있습니다.
<br><br>이 이벤트를 활성화하고 워크스페이스에서 기존 사용자의 무작위 버킷 번호에 대한 백필을 스케줄하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.RandomBucketNumberUpdate

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "prev_random_bucket_number" : "(optional, int) Previous random bucket number",
  "random_bucket_number" : "(required, int) New random bucket number",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 커스텀 이벤트 {#custom-events}

{% apitags %}
Custom Events
{% endapitags %}

이 이벤트는 특정 커스텀 이벤트가 트리거될 때 발생합니다. 이를 사용하여 사용자가 애플리케이션에서 커스텀 이벤트를 수행하는 시기를 추적할 수 있습니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.CustomEvent

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "name" : "(required, string) Name of the custom event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.CustomEvent

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "name" : "(required, string) Name of the custom event",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// users.behaviors.CustomEvent

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "name" : "(required, string) Name of the custom event"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### 속성정보 세부 정보 {#property-details}

- 커스텀 이벤트의 경우, 페이로드에는 해당 이벤트와 연결된 모든 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)도 포함됩니다.
- `ad_id`, `ad_id_type`, `ad_tracking_enabled`의 경우, 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. 자세한 내용은 여기에서 확인하세요: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_google-advertising-id).
- Kafka를 사용하여 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 데이터를 수집하는 경우, 고객 성공 매니저 또는 계정 매니저에게 연락하여 `ad_id` 전송을 위한 기능 플리퍼를 활성화하세요.

{% endapi %}

{% api %}
## 설치 경로 이벤트 {#install-attribution-events}

{% apitags %}
Attribution
{% endapitags %}

이 이벤트는 앱 설치가 소스에 기여도가 부여될 때 발생합니다. 이를 사용하여 앱 설치의 출처를 추적할 수 있습니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.InstallAttribution

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "source" : "(required, string) The source of the attribution",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "source" : "(optional, string) The source of the attribution"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.InstallAttribution

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "source" : "(optional, string) The source of the attribution"
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

{% tab Mixpanel %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "source" : "(optional, string) The source of the attribution",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "source" : "(required, string) The source of the attribution"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 위치 이벤트 {#location-events}

{% apitags %}
Locations
{% endapitags %}

이 이벤트는 사용자가 지정된 위치를 방문할 때 트리거됩니다. 이를 사용하여 앱에서 위치 이벤트를 트리거하는 사용자를 추적할 수 있습니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.Location

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
  "altitude" : "(optional, float) [PII] Altitude of recorded location",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "latitude" : "(required, float) [PII] Latitude of recorded location",
  "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
  "longitude" : "(required, float) [PII] Longitude of recorded location",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Location (users.behaviors.Location)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.Location

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
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

{% tab Mixpanel %}
```json
// Location (users.behaviors.Location)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Location (users.behaviors.Location)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### 속성정보 세부 정보

- `ad_id`, `ad_id_type`, `ad_tracking_enabled`의 경우, 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. 자세한 내용은 여기에서 확인하세요: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_google-advertising-id).
- Kafka를 사용하여 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 데이터를 수집하는 경우, 고객 성공 매니저 또는 계정 매니저에게 연락하여 `ad_id` 전송을 위한 기능 플리퍼를 활성화하세요.

{% endapi %}

{% api %}
## 구매 이벤트 {#purchase-events}

{% apitags %}
Purchases
{% endapitags %}

이 이벤트는 사용자가 구매할 때 발생합니다. 이 데이터를 사용하여 사용자가 애플리케이션에서 상품을 구매한 시점을 추적합니다.

{% alert tip %}
구매는 특별한 커스텀 이벤트이며, 커스텀 이벤트와 동일한 방식으로 JSON으로 인코딩된 커스텀 이벤트 속성정보 문자열이 함께 제공됩니다.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.Purchase

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "currency" : "(required, string) Currency of the purchase",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "price" : "(required, float) Price of the purchase",
  "product_id" : "(required, string) ID of the product purchased",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Purchase (users.behaviors.Purchase)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "price" : "(required, float) Price of the purchase",
  "productId" : "(required, string) ID of the product purchased",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.Purchase

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased"
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

{% tab Mixpanel %}
```json
// Purchase (users.behaviors.Purchase)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Purchased (users.behaviors.Purchase)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### 속성정보 세부 정보

- 구매 이벤트의 경우, 페이로드에는 해당 이벤트와 연결된 모든 [구매 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#purchase-properties)도 포함됩니다.
- `ad_id`, `ad_id_type`, `ad_tracking_enabled`의 경우, 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. 자세한 내용은 여기에서 확인하세요: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_google-advertising-id).
- Kafka를 사용하여 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 데이터를 수집하는 경우, 고객 성공 매니저 또는 계정 매니저에게 연락하여 `ad_id` 전송을 위한 기능 플리퍼를 활성화하세요.

{% endapi %}

{% api %}
## 첫 세션 이벤트 {#first-session-events}

{% apitags %}
Sessions
{% endapitags %}

이 이벤트는 사용자가 애플리케이션에서 첫 세션을 시작할 때 발생합니다. 이 데이터를 사용하여 사용자가 세션을 시작하는 시점을 추적합니다.

{% alert tip %}
사용자가 첫 세션을 시작하면 `FirstSession` 이벤트와 `SessionStart` 이벤트가 모두 발생합니다.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.FirstSession

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "country" : "(optional, string) [DEPRECATED]",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [DEPRECATED]",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [DEPRECATED]",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "sdk_version" : "(optional, string) [DEPRECATED]",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.app.FirstSession

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 세션 종료 이벤트 {#session-end-events}

{% apitags %}
Sessions
{% endapitags %}

이 이벤트는 사용자가 애플리케이션을 종료하여 현재 세션이 종료될 때 발생합니다. 이 데이터를 사용하여 세션이 종료되는 시점을 추적하고, 적절한 세션 시작 이벤트와 함께 세션의 지속 시간을 계산합니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionEnd

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "duration" : "(optional, float) Duration of the session in seconds",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.app.SessionEnd

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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

{% tab Mixpanel %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "duration" : "(optional, float) Duration of the session in seconds",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Session Ended (users.behaviors.app.SessionEnd)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "duration" : "(optional, float) Duration of the session in seconds",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 세션 시작 이벤트 {#session-start-events}

{% apitags %}
Sessions
{% endapitags %}

이 이벤트는 사용자가 세션을 시작할 때 발생합니다. 이 데이터를 사용하여 사용자가 세션을 시작하는 시점을 추적합니다.

{% alert tip %}
사용자가 첫 세션을 시작하면 `FirstSession` 이벤트와 `SessionStart` 이벤트가 모두 발생합니다.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionStart

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.app.SessionStart

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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

{% tab Mixpanel %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Session Started (users.behaviors.app.SessionStart)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 라이브 활동 푸시 시작 토큰 변경 이벤트 {#live-activity-push-to-start-token-change-events}

{% apitags %}
Live Activity, Push To Start Token
{% endapitags %}

이 이벤트는 Braze가 사용자와 라이브 활동 푸시 시작 토큰을 동기화할 때 발생합니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.PushToStartTokenChange

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.liveactivity.PushToStartTokenChange

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
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

{% tab Mixpanel %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Push To Start Token Changed (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### 속성정보 세부 정보

- Braze는 익명 사용자가 동일한 프로필에서 식별되고 기존 iOS 라이브 활동 푸시 시작 토큰이 해당 프로필에 유지될 때 `push_token_state_change_type`이 `"update"`로 설정된 "update" 이벤트를 발생시킵니다. 이 경우 `user_id`는 변경되지 않으며, `external_user_id`는 식별된 사용자의 외부 ID로 설정됩니다. 여기에는 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 엔드포인트를 통한 식별과 SDK `changeUser`가 기기의 익명 프로필에 외부 ID를 할당하는 경우가 포함됩니다.

{% endapi %}

{% api %}
## 라이브 활동 업데이트 토큰 변경 이벤트 {#live-activity-update-token-change-events}

{% apitags %}
Live Activity, Update Token
{% endapitags %}

이 이벤트는 Braze가 사용자와 라이브 활동 업데이트 토큰을 동기화할 때 발생합니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.UpdateTokenChange

{
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.liveactivity.UpdateTokenChange

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
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

{% tab Mixpanel %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Update Token Changed (users.behaviors.liveactivity.UpdateTokenChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 푸시 알림 토큰 상태 변경 이벤트 {#push-notification-token-state-change-events}

{% apitags %}
Push, Token State Change
{% endapitags %}

이 이벤트는 푸시 토큰이 삽입, 업데이트 또는 제거될 때 발생합니다. 이를 사용하여 푸시 토큰의 상태를 추적할 수 있습니다.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.pushnotification.TokenStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "platform" : "(optional, string) Platform of the device",
  "push_token" : "(optional, string) Push token of the event",
  "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
  "push_token_device_id" : "(optional, string) Device id of the push token",
  "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
  "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "time_ms" : "(optional, long) Time in milliseconds when the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
  "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
  "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time_ms" : "(optional, long) Time in milliseconds when the event happened",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab 커스텀 HTTP 커넥터 %}
```json
// users.behaviors.pushnotification.TokenStateChange

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time_ms" : "(optional, long) Time in milliseconds when the event happened",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "time_ms" : "(optional, long) Time in milliseconds when the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Token State Changed (users.behaviors.pushnotification.TokenStateChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time_ms" : "(optional, long) Time in milliseconds when the event happened",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### 속성정보 세부 정보

- `push_token_foreground_push_disabled` 필드는 푸시 토큰이 포그라운드 또는 백그라운드 푸시를 받을 수 있는지를 나타냅니다.
  - 사용자가 기기에서 푸시 알림 권한을 명시적으로 허용한 경우, 이 값은 `false`이며 토큰은 포그라운드 푸시 알림을 받을 수 있습니다.
  - 사용자가 기기에서 푸시 알림 권한을 명시적으로 거부한 경우, 이 값은 `true`이며 토큰은 백그라운드 푸시 알림만 허용됩니다.
  - 푸시 권한이 아직 결정되지 않은 경우(예: 사용자가 OS 프롬프트에 응답하지 않은 경우), 이 값은 `true`이며 토큰은 백그라운드 푸시 알림만 허용됩니다.
  - 이 필드는 아직 권한 상태를 보고하지 않은 이전 SDK 토큰 등록 및 웹 푸시 토큰의 경우 `null`(또는 대상 형식에 따라 비어 있음)일 수 있습니다. `null`은 `false`(포그라운드 푸시 가능)와 동일하게 처리하세요. Braze는 여전히 해당 토큰에 포그라운드 푸시 알림을 전송하려고 시도하기 때문입니다.
  - 푸시 전송 시도는 이 필드를 업데이트하지 않습니다. 전송이 성공하면 `TokenStateChange` 이벤트가 발생하지 않습니다. 토큰이 유효하지 않아 전송이 반송되면, Braze는 "remove" 이벤트를 발생시키고 토큰을 삭제합니다.
  - 이 필드는 SDK에서 토큰 상태 업데이트를 수집할 때만 변경됩니다(예: 푸시 권한 상태를 보고하는 이후 세션 동기화).
- `push_token_provisionally_opted_in` 필드는 iOS 푸시 토큰에만 적용됩니다.
  - [임시 승인]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push)이 설정되어 있으면, 임시 토큰은 이 필드가 `true`로 설정됩니다. 다른 모든 푸시 토큰은 `false`가 됩니다.
- `sdk_version` 필드는 토큰 상태 변경이 SDK에 의해 시작된 경우에만 채워집니다.
  - 토큰이 한 사용자에서 다른 사용자로 이동하도록 트리거하는 `changeUser` SDK 이벤트가 있는 경우, `sdk_version` 필드가 채워집니다.
  - 푸시 반송이 발생하면(예: 제거로 인한 경우), `sdk_version` 필드는 비어 있습니다.
- 푸시 토큰이 Braze에 들어올 때마다 생애 주기 이벤트가 기록됩니다. `push_token_state_change_type` 필드에는 세 가지 유형의 토큰 변경 이벤트("add", "update", "remove")가 기록됩니다.

#### 이벤트 유형 {#event-types}

##### 추가 {#add}

새 토큰이 등록될 때 "add" 이벤트가 수집됩니다. 사용자가 새 기기에서 앱을 처음 열거나, 이전에 토큰이 없었던 사용자에 대해 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 통해 `push_tokens`로 토큰이 설정될 때 발생합니다. `time_ms` 필드는 추가 이벤트가 발생한 시점을 나타냅니다.

{% alert note %}
iOS Swift SDK 13.3.0 이상 및 Android SDK 40.0.0 이상에서는 푸시 권한 상태와 푸시 토큰이 함께 전송됩니다. 이러한 SDK의 새 등록에서는 "add" 이벤트에 `push_token_foreground_push_disabled`가 채워집니다(일반적으로 알림이 활성화된 경우 `false`).<br><br>

이전 토큰 등록에서는 SDK가 나중에 푸시 권한 상태를 보고할 때까지 이 필드가 `null`일 수 있습니다. 웹 푸시 토큰도 설계상 이 필드가 `null`일 수 있습니다.
{% endalert %}

##### 업데이트 {#update}

기존 토큰의 속성정보가 변경되지만 토큰 문자열 자체는 변경되지 않을 때 "update" 이벤트가 수집됩니다. 토큰은 동일한 문자열, 동일한 사용자 및 동일한 앱을 가지지만, 다음 필드 중 하나 이상이 변경되었습니다: `foreground_push_disabled`, APNs 게이트웨이, 웹 푸시 키, `provisionally_opted_in` 또는 `device_id`. 이러한 업데이트는 토큰 상태 동기화 이벤트(예: SDK가 새 권한 상태를 보고할 때)에서 발생하며, 푸시 전송 결과에서 발생하지 않습니다. `time_ms` 필드는 업데이트 이벤트가 발생한 시점을 나타냅니다.

Braze는 또한 익명 사용자가 동일한 프로필에서 식별되고 기존 푸시 토큰이 해당 프로필에 유지될 때 `push_token_state_change_type`이 `"update"`로 설정된 "update" 이벤트를 발생시킵니다. 이 경우 `user_id`는 변경되지 않으며, `external_user_id`는 식별된 사용자의 외부 ID로 설정됩니다. 여기에는 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 엔드포인트를 통한 식별과 SDK `changeUser`가 기기의 익명 프로필에 외부 ID를 할당하는 경우가 포함됩니다.

{% alert note %}
대부분의 경우, 앱 재설치 또는 백업 복원은 새로운 `push_token`과 새로운 `device_id`를 가진 새로운 "add" 이벤트를 발생시킵니다(SDK가 새로운 `device_id`를 생성하고 OS가 새로운 푸시 토큰 문자열을 제공하기 때문입니다). 이로 인해 사용자 프로필에 두 개의 별도 토큰 및 기기 항목이 생성되며, 이전 항목은 제거 추적 또는 Campaign 전송을 통해 나중에 정리됩니다.<br><br>

`push_token`은 변경되지 않고 `device_id`만 변경되는 경우는 극히 드뭅니다(이 경우 OS가 재설치 후 동일한 토큰 문자열을 반환해야 합니다).
{% endalert %}

##### 제거 {#remove}

Braze가 토큰을 제거할 때 독립적인 "remove" 이벤트가 수집됩니다. 이는 여러 가지 이유로 발생할 수 있습니다:

- 푸시 반송(APNs, FCM 또는 HMS가 토큰을 유효하지 않거나 만료된 것으로 보고함)
- 사일런트 푸시를 통한 제거 감지
- REST API 또는 APNs 피드백 서비스를 통해 토큰이 제거됨

푸시 반송으로 인해 토큰이 제거되면, Braze는 해당 토큰에 대해 `push_token_state_change_type = "remove"`를 발생시킵니다. `push_token_foreground_push_disabled`를 변경하는 "update" 이벤트는 발생시키지 않습니다.

`time_ms` 필드는 제거 이벤트가 발생한 시점을 나타냅니다.

{% alert note %}
"remove" 이벤트의 경우, 다음 토큰 속성정보 필드는 채워지지 않습니다: `push_token_created_at`, `push_token_updated_at`, `push_token_foreground_push_disabled`, `push_token_provisionally_opted_in`, `ios_push_token_apns_gateway`, `web_push_token_public_key`, `web_push_token_user_auth`, `web_push_token_vapid_public_key`.
{% endalert %}

##### 추가 및 제거 쌍 {#add-and-remove-pairs}

추가 및 제거 쌍 이벤트는 동일한 전환에 대한 두 개의 연결된 토큰 상태 이벤트로, 하나의 "add" 이벤트와 하나의 "remove" 이벤트로 구성됩니다.
추가 및 제거 쌍은 두 가지 범주로 나뉩니다:

**토큰 문자열 새로고침(동일한 사용자):** OS가 동일한 기기에서 토큰 문자열을 회전시킵니다(예: APNs 또는 FCM 토큰 회전). "add" 이벤트(새 토큰)와 "remove" 이벤트(이전 토큰)는 동일한 `user_id`, 동일한 `device_id`, 다른 `push_token`, 그리고 동일한 `time_ms`를 가집니다.

**토큰이 사용자 간에 이동:** 토큰이 한 사용자에서 다른 사용자로 이동합니다. "add" 이벤트(새 사용자)와 "remove" 이벤트(이전 사용자)는 다른 `user_id`, 동일한 `device_id`, 동일한 `push_token`, 그리고 다른 `time_ms`를 가집니다(일반적으로 100밀리초 미만의 간격). 다음 중 하나에 의해 트리거됩니다:

- SDK가 익명 프로필에서 식별된 프로필로 `changeUser`를 호출합니다. "remove" 이벤트는 빈 `external_user_id`를 가집니다.
- SDK가 한 식별된 프로필에서 다른 식별된 프로필로 `changeUser`를 호출합니다. 두 이벤트 모두 비어 있지 않은 `external_user_id`를 가집니다.
- [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) 엔드포인트 또는 중복 사용자 정리가 고아 사용자의 토큰을 생존 사용자에게 이동시킵니다.

{% alert note %}
REST [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 또는 SDK [`changeUser`]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles)를 통한 동일 프로필 식별은 `user_id`를 변경하지 않고 익명 프로필에 외부 ID를 할당할 수 있습니다.
이 경우 Braze는 [추가 및 제거 쌍 이벤트](#add-and-remove-pairs)를 발생시키지 않습니다.
대신 Braze는 기존 각 푸시 토큰에 대해 "update" 이벤트를 발생시키고 `external_user_id`를 식별된 사용자의 외부 ID로 설정합니다.
`changeUser`가 토큰을 한 사용자 프로필에서 다른 프로필로 이동시키는 경우, Braze는 [추가 및 제거 쌍](#add-and-remove-pairs) 섹션에서 설명한 [추가 및 제거 쌍 이벤트](#add-and-remove-pairs)를 여전히 발생시킵니다.
{% endalert %}

#### 최신 활성 토큰 상태 쿼리 {#querying-for-the-latest-active-token-state}

각 사용자의 현재 푸시 토큰 상태를 확인하려면, 토큰 상태 변경 이벤트를 `push_token`, `user_id`, `app_id`로 파티션한 다음 `time_ms`를 내림차순으로 정렬하고 "remove" 이벤트를 필터링합니다. 내부적으로 토큰은 사용자당 토큰 문자열과 `app_id`로 키가 지정됩니다. `device_id`를 파티션 키로 사용하는 것은 권장되지 않습니다. `device_id`는 변경 가능한 속성이며, 이를 기준으로 파티션을 나누면 단일 토큰의 생애 주기가 여러 파티션에 걸쳐 분할될 수 있기 때문입니다.

다음 SQL 쿼리는 Snowflake에서 사용자별로 최신 활성 토큰 상태를 반환합니다:

```sql
WITH latest_token_state AS (
  SELECT *,
    ROW_NUMBER() OVER (
      PARTITION BY PUSH_TOKEN, USER_ID, APP_ID
      ORDER BY COALESCE(TIME_MS, TIME * 1000) DESC
    ) AS rn
  FROM USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE
)
SELECT
  PUSH_TOKEN, USER_ID, EXTERNAL_USER_ID, PUSH_TOKEN_DEVICE_ID,
  PUSH_TOKEN_STATE_CHANGE_TYPE, PUSH_TOKEN_FOREGROUND_PUSH_DISABLED,
  TIME_MS, PLATFORM, APP_ID
FROM latest_token_state
WHERE rn = 1
  AND PUSH_TOKEN_STATE_CHANGE_TYPE != 'remove';
```


{% endapi %}