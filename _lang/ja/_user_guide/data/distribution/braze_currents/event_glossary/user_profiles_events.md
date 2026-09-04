---
nav_title: ユーザープロファイル
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "この用語集では、Brazeが追跡し、Currentsを使用して選択したデータウェアハウスに送信できるユーザープロファイルの更新を一覧にしています。"
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert tip %}
これらのイベントは、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)、および[Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)でSQLテーブルとしても利用できます。SQLテーブルスキーマとカラムの詳細については、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)を参照してください。Snowflakeデータ共有のユーザープロファイル属性ビューのスキーマについては、[ユーザープロファイル属性]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes)を参照してください。
{% endalert %}

追加のイベントエンタイトルメントへのアクセスが必要な場合は、Brazeの担当者に連絡するか、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を開いてください。このページで必要な情報が見つからない場合は、[顧客行動イベントライブラリ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)、[メッセージエンゲージメントイベントライブラリ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、または[Currentsサンプルデータの例](https://github.com/Appboy/currents-examples/tree/master/sample-data)を参照してください。

{% details ユーザープロファイル更新イベント構造の説明 %}

### イベント構造 {#event-structure}

この顧客行動およびユーザーイベントの内訳は、ユーザープロファイル更新イベントに一般的に含まれる情報の種類を示しています。そのコンポーネントをしっかり理解することで、開発者やビジネスインテリジェンス戦略チームは、受信したCurrentsイベントデータを使用してデータドリブン型のレポートやチャートを作成し、その他の貴重なデータ指標を活用できます。

{% alert important %}
ストレージスキーマは、Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storageなどのデータウェアハウスストレージパートナーに送信されるフラットファイルイベントデータに適用されます。ここに記載されているイベントと送信先の組み合わせの一部は、まだ一般提供されていません。パートナーごとのサポート対象イベントについては、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)および関連するパートナーページを参照してください。

Currentsは、ペイロードが900 KBを超えるイベントをドロップします。
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->


{% api %}
## ユーザー削除リクエストイベント {#user-delete-request-events}

{% apitags %}
User Delete Request
{% endapitags %}

顧客のリクエストによりユーザーが削除された場合に発生します。

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
## ユーザーオーファンイベント {#user-orphan-events}

{% apitags %}
User Orphan
{% endapitags %}

ユーザーがオーファン化された場合、つまりユーザーが別のユーザーのプロファイルにマージされた場合に発生します。

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
## ユーザープロファイル更新イベント {#user-profile-update-events}

{% apitags %}
Profile
{% endapitags %}

これはユーザーのプロファイル更新を表します。

{% alert important %}
ユーザープロファイル更新イベントはベータ版です。アクセスするには、カスタマーサクセスマネージャーまたはアカウントマネージャーにお問い合わせください。
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

{% tab Shopify %}
```json
// User Profile Update (users.profile.Update)

{
  "variables" : {
    "identifier" : {
      "customId" : {
        "key" : "user_id",
        "namespace" : "braze",
        "value" : "(required, string) [PII] Braze user ID of the user who performed this event"
      }
    },
    "input" : {
      "email" : "(optional, string) [PII] Email address of the user",
      "firstName" : "(optional, string) [PII] First name of the user",
      "lastName" : "(optional, string) [PII] Last name of the user",
      "locale" : "(optional, string) [PII] Language of the user",
      "phone" : "(optional, string) [PII] Phone number of the user in e.164 format"
    }
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}