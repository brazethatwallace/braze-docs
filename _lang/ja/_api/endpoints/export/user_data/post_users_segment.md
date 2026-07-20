---
nav_title: "POST: セグメント別ユーザープロファイルのエクスポート"
article_title: "POST: セグメント別ユーザープロファイルのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「セグメント別ユーザーのエクスポート」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# セグメント別ユーザープロファイルのエクスポート {#export-user-profile-by-segment}
{% apimethod post %}
/users/export/segment
{% endapimethod %}

> このエンドポイントを使用して、セグメント内のすべてのユーザーをエクスポートします。

{% alert important %}
このエンドポイントを使用する場合は、次の点に注意してください。<br><br>1. このAPIリクエストの`fields_to_export`フィールドは**必須**です。<br>2. `custom_events`、`purchases`、`campaigns_received`、`canvases_received`のフィールドには、過去90日間のデータのみが含まれます。
{% endalert %}

ユーザーデータは、改行で区切られたユーザーJSONオブジェクトの複数のファイルとしてエクスポートされます（1行に1つのJSONオブジェクトなど）。データは、自動生成されたURL、またはこの統合がすでに設定されている場合はS3バケットにエクスポートされます。

{% alert important %}
**エクスポートの出力形式**: エクスポートが成功し、クラウドストレージ認証情報を設定していない場合、HTTPレスポンスには圧縮アーカイブ（ZIPまたはGZIPファイル）をダウンロードするためのURLが含まれます。クラウドストレージ認証情報（S3、Azure、またはGoogle Cloud Storage）が設定されている場合、Brazeはエクスポートをバケットに直接書き込み、レスポンスにはダウンロードURLは含まれません。エクスポートが失敗した場合は、代わりにメール通知が届きます。クラウドストレージ認証情報を設定すると、大規模なエクスポートで障害が発生する可能性が低くなります。
{% endalert %}

企業は、このエンドポイントを使用するセグメントごとに、特定の時点で最大1つのエクスポートを実行できます。エクスポートが完了するのを待ってから、再試行してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.export.segment`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 認証情報ベースのレスポンスの詳細 {#credentials-based-response-details}

[S3][1]、[Azure][2]、または[Google Cloud Storage][3]の認証情報をBrazeに追加した場合、各ファイルは`segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`のようなキー形式でZIPファイルとしてバケットにアップロードされます。Azureを使用している場合は、BrazeのAzureパートナー概要ページで**これをデフォルトのデータエクスポート先にする**チェックボックスがオンになっていることを確認してください。通常、Brazeは処理を最適化するために5,000ユーザーごとに1つのファイルを作成します。大きなワークスペース内で小さなセグメントをエクスポートすると、複数のファイルが生成される場合があります。その後、ファイルを展開し、必要に応じてすべての`json`ファイルを1つのファイルに連結できます。`output_format`に`gzip`を指定すると、ファイル拡張子は`.zip`ではなく`.gz`になります。

{% details ZIPのエクスポートパスの内訳 %}
**ZIP形式:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**ZIPの例:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| プロパティ | 詳細 | 例での表示 |
| ------------------------------- | ------------------------------------------------------------------------------------ | --- |
| `bucket-name` | バケット名に基づいて固定されます。 | `braze.docs.bucket` |
| `segment-export` | 固定。 | `segment-export` |
| `SEGMENT_ID` | エクスポートリクエストに含まれます。 | `abc56c0c-rd4a-pb0a-870pdf4db07q` |
| `YYYY-MM-dd` | コールバックが正常に受信された日付。 | `2019-04-25` |
| `RANDOM_UUID` | リクエスト時にBrazeによって生成されるランダムUUID。 | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | UTCでエクスポートが要求されたUnix時間（2017-01-01:00:00:00Zからの秒数）。 | `1556044807` |
| `filename` | ファイルごとにランダム。 | `114f0226319130e1a4770f2602b5639a` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="認証情報ベースのレスポンスの詳細" }

{% enddetails %}

このエンドポイントを使用する際にエクスポートに独自のバケットポリシーを適用するため、独自のS3またはAzure認証情報を設定することを強くお勧めします。クラウドストレージの認証情報がない場合は、リクエストへのレスポンスで、すべてのユーザーファイルを含むZIPファイルをダウンロードできるURLが提供されます。URLは、エクスポートの準備ができた後にのみ有効な場所になります。

クラウドストレージ認証情報を提供しない場合は、このエンドポイントからエクスポートできるデータ量に制限があることに注意してください。エクスポートするフィールドやユーザーの数によっては、ファイルが大きすぎるとファイル転送が失敗することがあります。ベストプラクティスは、`fields_to_export`を使用してエクスポートするフィールドを指定し、転送サイズを抑えるために必要なフィールドのみを指定することです。ファイルの生成でエラーが発生する場合は、ランダムバケット番号に基づいてユーザー群をより多くのセグメントに分割することを検討してください（たとえば、ランダムバケット番号が1,000未満、または1,000から2,000の間のセグメントを作成します）。

どちらのシナリオでも、オプションで`callback_endpoint`を指定して、エクスポートの準備が整ったときに通知を受け取ることができます。`callback_endpoint`が指定されている場合、Brazeはダウンロードの準備ができたときに、指定されたアドレスにPOSTリクエストを行います。POSTの本文は"success":trueです。S3認証情報をBrazeに追加していない場合、POSTの本文にはダウンロードURLを値として持つ属性`url`が追加されます。

ユーザー群が大きいほど、エクスポート時間が長くなります。たとえば、2,000万人のユーザーを持つアプリの場合、1時間以上かかることもあります。

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. New accounts must specify specific fields to export,
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ----------------------------- | --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `segment_id` | 必須 | 文字列 | エクスポートするセグメントの識別子。[セグメント識別子]({{site.baseurl}}/api/identifier_types)を参照してください。<br><br>特定のセグメントの`segment_id`は、Brazeアカウントの[APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)ページから確認できます。または、[セグメント一覧エンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment)を使用することもできます。 |
| `callback_endpoint` | オプション | 文字列 | エクスポートが利用可能になったときにダウンロードURLをPOSTするエンドポイント。 |
| `fields_to_export` | 必須* | 文字列の配列 | エクスポートするユーザーデータフィールドの名前。このパラメーターに`custom_attributes`を含めることで、すべてのカスタム属性をエクスポートすることもできます。エクスポートできるフィールドの完全なリストについては、[エクスポートするフィールド](#fields-to-export)を参照してください。 |
| `custom_attributes_to_export` | オプション | 文字列の配列 | エクスポートする特定のカスタム属性の名前（最大500個）。このパラメーターを使用する場合は、`fields_to_export`から`custom_attributes`を省略してください。省略しないと、Brazeはこのリストに関係なくすべてのカスタム属性をエクスポートします。ダッシュボードでカスタム属性を作成および管理するには、**データ設定** > **カスタム属性**に移動してください。 |
| `output_format` | オプション | 文字列 | ファイルの出力形式。デフォルトは`zip`ファイル形式です。独自のS3バケットを使用している場合は、`zip`または`gzip`を指定できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

{% alert note %}
`fields_to_export`パラメーターに`custom_attributes`が含まれている場合、`custom_attributes_to_export`の内容に関係なく、すべてのカスタム属性がエクスポートされます。特定の属性をエクスポートすることが目的の場合は、`custom_attributes`を`fields_to_export`パラメーターに含めないでください。代わりに、`custom_attributes_to_export`パラメーターを使用してください。
{% endalert %}

## すべてのカスタム属性をエクスポートするリクエスト例 {#example-request-to-export-all-custom-attributes}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases", "custom_attributes"],
  "output_format" : "zip"
}'
```

## 特定のカスタム属性をエクスポートするリクエスト例 {#example-request-to-export-specific-custom-attributes}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "custom_attributes_to_export" : ["allergies", "favorite_food"],
  "output_format" : "zip"
}'
```

## エクスポートするフィールド {#fields-to-export}

以下は、有効な`fields_to_export`のリストです。`fields_to_export`を使用して返されるデータを最小限に抑えると、このAPIエンドポイントのレスポンスタイムを改善できます。

| エクスポートするフィールド | データタイプ | 説明 |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps` | 配列 | このユーザーがセッションを記録したアプリ。次のフィールドが含まれます。<br><br>- `name`: アプリ名<br>- `platform`: アプリのプラットフォーム（iOS、Android、Webなど）<br>- `version`: アプリのバージョン番号または名前<br>- `sessions`: このアプリの総セッション数<br>- `first_used`: 初回セッションの日付<br>- `last_used`: 最終セッションの日付<br><br>すべてのフィールドは文字列です。 |
| `attributed_campaign` | 文字列 | [アトリビューション統合]({{site.baseurl}}/partners/message_orchestration)からのデータ（設定されている場合）。特定の広告キャンペーンの識別子。 |
| `attributed_source` | 文字列 | [アトリビューション統合]({{site.baseurl}}/partners/message_orchestration)からのデータ（設定されている場合）。広告が掲載されたプラットフォームの識別子。 |
| `attributed_adgroup` | 文字列 | [アトリビューション統合]({{site.baseurl}}/partners/message_orchestration)からのデータ（設定されている場合）。キャンペーンの下のオプションのサブグループの識別子。 |
| `attributed_ad` | 文字列 | [アトリビューション統合]({{site.baseurl}}/partners/message_orchestration)からのデータ（設定されている場合）。キャンペーンと広告グループの下のオプションのサブグループの識別子。 |
| `push_subscribe` | 文字列 | ユーザーのプッシュ通知の購読ステータス。 |
| `email_subscribe` | 文字列 | ユーザーのメール購読ステータス。 |
| `braze_id` | 文字列 | このユーザーに対してBrazeが設定したデバイス固有の一意のユーザー識別子。 |
| `country` | 文字列 | [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)標準を使用したユーザーの国。 |
| `created_at` | 文字列 | ユーザープロファイルが作成された日時（ISO 8601形式）。 |
| `created_from` | 文字列 | ユーザープロファイルの作成に使用された方法（例: SDK、REST API、CSVインポート）。 |
| `custom_attributes` | オブジェクト | このユーザーのカスタム属性のキーと値のペア。 |
| `custom_events` | 配列 | 過去90日間にこのユーザーに帰属するカスタムイベント。 |
| `devices` | 配列 | ユーザーのデバイスに関する情報。プラットフォームに応じて、次の情報が含まれる場合があります。<br><br>- `model`: デバイスのモデル名<br>- `os`: デバイスのオペレーティングシステム<br>- `carrier`: デバイスのサービスキャリア（利用可能な場合）<br>- `idfv`: (iOS) Brazeデバイス識別子、AppleのVendor用識別子（存在する場合）<br>- `idfa`: (iOS) 広告用識別子（存在する場合）<br>- `device_id`: (Android) Brazeデバイス識別子<br>- `google_ad_id`: (Android) Google Play広告識別子（存在する場合）<br>- `roku_ad_id`: (Roku) Roku広告識別子<br>- `ad_tracking_enabled`: デバイスで広告トラッキングが有効になっている場合、trueまたはfalse |
| `dob` | 文字列 | `YYYY-MM-DD`形式のユーザーの生年月日。 |
| `email` | 文字列 | ユーザーのメールアドレス。 |
| `external_id` | 文字列 | 識別済みユーザーの一意のユーザー識別子。 |
| `first_name` | 文字列 | ユーザーの名。 |
| `gender` | 文字列 | ユーザーの性別。可能な値は次のとおりです。<br><br>- `M`: 男性<br>- `F`: 女性<br>- `O`: その他<br>- `N`: 該当なし<br>- `P`: 回答しない<br>- `nil`: 不明 |
| `home_city` | 文字列 | ユーザーの居住都市。 |
| `language` | 文字列 | ISO-639-1標準のユーザーの言語。 |
| `last_coordinates` | 浮動小数点の配列 | `[longitude, latitude]`としてフォーマットされたユーザーの最新のデバイスの位置。 |
| `last_name` | 文字列 | ユーザーの姓。 |
| `phone` | 文字列 | Brazeにインポートされた形式のユーザーの電話番号。たとえば、電話番号を追加するリクエストが`1234567890`として送信された場合、同じ形式でエクスポートされます。 |
| `purchases` | 配列 | このユーザーが過去90日間に行った購入。 |
| `push_tokens` | 配列 | ユーザーのプッシュトークンに関する情報。 |
| `random_bucket` | 整数 | ユーザーの[ランダムバケット番号]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)。ランダムユーザーの均一分布セグメントを作成するために使用されます。 |
| `time_zone` | 文字列 | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン。 |
| `total_revenue` | 浮動小数点 | このユーザーに帰属する総収益。総収益は、受信したキャンペーンおよびキャンバスのコンバージョン期間中にユーザーが行った購入に基づいて計算されます。 |
| `uninstalled_at` | タイムスタンプ | ユーザーがアプリをアンインストールした日時。アプリがアンインストールされていない場合は省略されます。 |
| `user_aliases` | オブジェクト | `alias_name`および`alias_label`を含む[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object)（存在する場合）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="エクスポートするフィールド" }

## 重要な注意事項 {#important-reminders}

- `custom_events`、`purchases`、`campaigns_received`、および`canvases_received`のフィールドには、過去90日間のデータのみが含まれます。
- `custom_events`と`purchases`の両方に、`first`と`count`のフィールドが含まれています。これらのフィールドは両方とも全期間の情報を反映しており、過去90日間のデータに限定されません。たとえば、特定のユーザーが90日以上前にイベントを最初に実行した場合、これは`first`フィールドに正確に反映され、`count`フィールドは過去90日より前に発生したイベントも考慮します。
- 企業がエンドポイントレベルで実行できる同時セグメントエクスポートの数は100に制限されています。この制限を超えると、エラーが発生します。
- 最初のエクスポートジョブの実行中にセグメントを2回目にエクスポートしようとすると、429エラーが発生します。
- [`403 Forbidden`レスポンス]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting?sdktab=cloud%20storage%20connected#segment-export-api-downloads)は、多くの場合、エクスポートファイルがまだ準備できていないことを意味します。
- 購読グループのデータは、セグメントエクスポートでは利用できません。購読ステータスでユーザーを特定するには、購読グループのメンバーシップに基づいて別のセグメントを作成し、そのセグメントをエクスポートしてください。

## レスポンス {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that is used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

### `null` URL

レスポンスに`"url": null`が含まれている（またはダウンロードURLが省略されている）場合で、Amazon S3バケットやAzure Blob Storageコンテナなどの[クラウドストレージ統合]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)を設定している場合、BrazeはAPIレスポンスで一時的なダウンロードURLを返す代わりに、接続されたバケットまたはコンテナにエクスポートを書き込みます。接続されたクラウドストレージのバケットまたはコンテナからファイルを取得してください。

ダウンロードURLが返された場合、有効期間は数時間のみです。そのため、独自のS3認証情報をBrazeに追加することを強くお勧めします。

APIレスポンスに`object_prefix`が表示され、データをダウンロードするURLがない場合、このエンドポイント用にAmazon S3バケットがすでに設定されていることを意味します。このエンドポイントを使用してエクスポートされたデータは、S3バケットに直接送信されます。

## ユーザーエクスポートファイルの出力例 {#example-user-export-file-output}

ユーザーエクスポートオブジェクト（Brazeは可能な限り少ないデータを含めます&#8212;オブジェクトにフィールドがない場合は、nullまたは空であると見なされます）:

{% tabs %}
{% tab All fields %}

```json
{
    "created_at": (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether foreground push notifications are enabled for this token. `true` means foreground push is enabled for the token, and `false` means foreground push is disabled (for example, background-only). This is device-level and doesn't indicate the user's global push subscription status,
        "provisionally_opted_in": (boolean) included for iOS and Android tokens only. Indicates whether the token is in a provisional push authorization state. `true` means the token is provisionally opted in (notifications are delivered quietly), `false` means the token isn't provisional (the user has explicitly authorized or denied push), and `null` means provisional status isn't set. Provisional authorization applies to iOS; Android tokens report `null`
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" :
         {
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (boolean),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
}
```

{% endtab %}
{% tab Sample output %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Alex",
    "last_name" : "Smith",
    "email" : "example@example.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+15555550123",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in",
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
    "custom_attributes":
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Loyalty Acknowledgement",
        "first": "2021-06-28T17:02:43.032Z",
        "last": "2021-06-28T17:02:43.032Z",
        "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true,
        "provisionally_opted_in": null
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged":
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted":
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)」を参照してください。
{% endalert %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/

{% endapi %}