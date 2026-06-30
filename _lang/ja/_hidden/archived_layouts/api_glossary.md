---
title: APIまたはコード用語集
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "これはGoogle検索の説明です。160文字を超えると切り捨てられるため、簡潔にしてください。"
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 メールテンプレートを作成する {#1-create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Post,Email,Create,Template,REST,API
{% endapitags %}

メールテンプレートREST APIを使用して、Brazeダッシュボードのテンプレートとメディアページに保存したメールテンプレートをプログラムで管理できます。Brazeは、メールテンプレートを作成および更新するための2つのエンドポイントを提供しています。

このエンドポイントからの応答には`email_template_id`フィールドが含まれており、後続のAPI呼び出しでテンプレートを更新するために使用できます。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文 {#request-body}
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### 応答の例 {#example-response}
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### パラメーターの詳細 {#parameter-details}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `modified_after`  | いいえ | ISO 8601形式の文字列 | 指定された時刻以降に更新されたテンプレートのみを取得します。 |
| `modified_before`  |  いいえ | ISO 8601形式の文字列 | 指定された時刻以前に更新されたテンプレートのみを取得します。 |
| `limit` | いいえ | 正の数値 | 取得するテンプレートの最大数。指定がない場合はデフォルトで100、許容される最大値は1000です。 |
| `offset`  |  いいえ | 正の数値 | 検索条件に一致する残りのテンプレートを返す前にスキップするテンプレートの数。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="パラメーターの詳細" }


{% endapi %}
{% api %}
## 2 利用可能なメールテンプレートの一覧 {#2-list-available-email-template}
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
Get,Email,Template,List,REST
{% endapitags %}

以下のエンドポイントを使用して、利用可能なテンプレートの一覧を取得します。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### 応答の例
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### パラメーターの詳細

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `email_template_id`  | はい | 文字列 | メールテンプレートのAPI識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="パラメーターの詳細" }

{% endapi %}


{% api %}
## 3 Campaignsトリガー送信 {#3-campaigns-trigger-send}
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}Post, Campaigns, Trigger,Send{% endapitags %}

APIトリガー配信を使用すると、メッセージのコンテンツをBrazeダッシュボード内に保存しながら、メッセージの送信タイミングと送信先をAPI経由で指定できます。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### 応答の例
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "context": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "context": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent context)
    },
    ...
  ]
}
```


#### パラメーターの詳細

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `email_template_id`  | はい | 文字列 | メールテンプレートのAPI識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="パラメーターの詳細" }

{% endapi %}


{% api %}
## 4 Campaignsトリガー送信 {#4-campaigns-trigger-send}
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, Campaigns, Trigger, Send{% endapitags %}

このエンドポイントは、カスタムイベント、ユーザー属性、およびユーザーの購入を記録するために使用できます。リクエストごとに最大75の属性、イベント、購入オブジェクトを含めることができます。つまり、一度に最大75人のユーザーの属性を投稿できますが、同じAPI呼び出しで最大75件のイベントと最大75件の購入も提供できます。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### 応答の例
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
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
}
```

#### パラメーターの詳細

| ユーザープロファイルフィールド | データタイプの仕様 |
| ---| --- |
| country | (文字列) 国コードは[ISO-3166-1 alpha-2規格][17]でBrazeに渡す必要があります。 |
| current_location | (オブジェクト) {"longitude": -73.991443, "latitude": 40.753824} の形式です。 |
| date_of_first_session | (ユーザーが初めてアプリを使用した日付) ISO 8601形式または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の文字列。 |
| date_of_last_session | (ユーザーが最後にアプリを使用した日付) ISO 8601形式または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の文字列。 |
| dob | (生年月日)「YYYY-MM-DD」形式の文字列。例: 1980-12-21。 |
| email | (文字列) |
| email_subscribe | (文字列) 利用可能な値は、"opted_in"(メールメッセージの受信を明示的に登録)、"unsubscribed"(メールメッセージの受信を明示的に拒否)、"subscribed"(受信登録も拒否もしていない)です。 |
| external_id | (文字列) 一意のユーザー識別子。 |
| facebook | `id`(文字列)、`likes`(文字列の配列)、`num_friends`(整数)のいずれかを含むハッシュ。 |
| first_name | (文字列) |
| gender | (文字列)「M」、「F」、「O」(その他)、「N」(該当なし)、「P」(回答しない)、またはnil(不明)。 |
| home_city | (文字列) |
| image_url | (文字列) ユーザープロファイルに関連付ける画像のURL。 |
| language | (文字列) 言語は[ISO-639-1規格][24]でBrazeに渡す必要があります。<br>[受け入れ可能な言語のリスト](/docs/user_guide/data_and_analytics/user_data_collection/language_codes/) |
| last_name | (文字列) |
| marked_email_as_spam_at | (文字列) ユーザーのメールがスパムとしてマークされた日付。ISO 8601形式またはyyyy-MM-dd'T'HH:mm:ss:SSSZ形式で表示されます。 |
| phone | (文字列) |
| push_subscribe | (文字列) 利用可能な値は、"opted_in"(プッシュメッセージの受信を明示的に登録)、"unsubscribed"(プッシュメッセージの受信を明示的に拒否)、"subscribed"(受信登録も拒否もしていない)です。 |
| push_tokens | `app_id`と`token`文字列を持つオブジェクトの配列です。このトークンが関連付けられているデバイスの`device_id`をオプションで提供できます。例: `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`。`device_id`が提供されない場合、ランダムに生成されます。 |
| time_zone | (文字列) [IANAタイムゾーンデータベース][26]のタイムゾーン名(例: "America/New_York" または "Eastern Time (US & Canada)")。有効なタイムゾーン値のみが設定されます。 |
| twitter | `id`(整数)、`screen_name`(文字列、X(旧Twitter)ハンドル)、`followers_count`(整数)、`friends_count`(整数)、`statuses_count`(整数)のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーターの詳細" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/