---
nav_title: "POST:グローバルコントロールグループによるユーザープロファイルのエクスポート"
article_title: "POST:グローバルコントロールグループ別にユーザープロファイルをエクスポートする"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、「グローバルコントロールグループでのユーザーのエクスポート」Brazeエンドポイントについて詳しく説明します。"

---
{% api %}
# グローバルコントロールグループ別にユーザープロファイルをエクスポートする {#export-user-profile-by-global-control-group}
{% apimethod post %}
/users/export/global_control_group
{% endapimethod %}

> このエンドポイントを使用して、グローバルコントロールグループ内のすべてのユーザーをエクスポートします。

ユーザーデータは、改行で区切られたユーザーJSONオブジェクトの複数のファイルとしてエクスポートされます（1行に1つのJSONオブジェクトなど）。ファイルが生成されるたびに、グローバルコントロールグループのすべてのユーザーが含まれます。Brazeは、ユーザーがいつグローバルコントロールグループに追加または削除されたかの履歴を保存しません。

グローバルコントロールグループのセグメント識別子を確認するには、[API識別子タイプ]({{site.baseurl}}/api/identifier_types?tab=segments#segment-identifier)を参照してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.export.global_control_group` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 認証情報ベースのレスポンスの詳細 {#credentials-based-response-details}

それぞれの**テクノロジーパートナー**ページを通じてBrazeに[S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)または[Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)の認証情報を追加した場合、各ファイルはバケットにZIPファイルとしてアップロードされ、キー形式は `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip` のようになります。Azureを使用している場合は、BrazeのAzureパートナー概要ページで**これをデフォルトのデータエクスポート先にする**チェックボックスがオンになっていることを確認してください。

一般的に、処理を最適化するために5,000ユーザーごとに1つのファイルを作成します。大きなワークスペース内で小さなセグメントをエクスポートすると、複数のファイルが生成される場合があります。その後、ファイルを展開し、必要に応じてすべての `json` ファイルを1つのファイルに連結できます。`output_format` に `gzip` を指定した場合、ファイル拡張子は `.zip` ではなく `.gz` になります。

{% details ZIPのエクスポートパスの内訳 %}
**ZIP形式:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**ZIPの例:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| プロパティ | 詳細 | 例での表示 |
| ------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------- |
| `bucket-name` | バケット名に基づいて固定されます。 | `braze.docs.bucket` |
| `segment-export` | 固定。 | `segment-export` |
| `SEGMENT_ID` | エクスポートリクエストに含まれます。 | `abc56c0c-rd4a-pb0a-870pdf4db07q` |
| `YYYY-MM-dd` | コールバックが正常に受信された日付。 | `2019-04-25` |
| `RANDOM_UUID` | リクエスト時にBrazeによって生成されるランダムUUID。 | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | UTCでエクスポートが要求されたUnix時間（2017-01-01:00:00:00Zからの秒数）。 | `1556044807` |
| `filename` | ファイルごとにランダム。 | `114f0226319130e1a4770f2602b5639a` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Credentials-based response details" }

{% enddetails %}

このエンドポイントを使用する際は、エクスポートに独自のバケットポリシーを適用するために、自身のS3またはAzureの認証情報を設定することを強くお勧めします（**パートナー連携** > **テクノロジーパートナー** > パートナーページから設定できます）。

![AzureのテクノロジーパートナーページにAmazon S3用のタブが表示されている。]({% image_buster /assets/img/technology_partners_page.png %})

クラウドストレージの認証情報を提供していない場合、リクエストに対するレスポンスには、すべてのユーザーファイルを含むZIPをダウンロードできるURLが含まれます。URLはエクスポートの準備が完了してから初めて有効になります。

クラウドストレージの認証情報を提供しない場合、このエンドポイントからエクスポートできるデータ量に制限があることに注意してください。エクスポートするフィールドやユーザー数によっては、ファイルが大きすぎると転送が失敗する場合があります。ベストプラクティスは、`fields_to_export` を使用してエクスポートするフィールドを指定し、転送サイズを抑えるために必要なフィールドのみを指定することです。ファイルの生成でエラーが発生する場合は、ランダムバケット番号に基づいてユーザー群をより多くのセグメントに分割することを検討してください（たとえば、ランダムバケット番号が1,000未満、または1,000～2,000のセグメントを作成するなど）。

どちらのシナリオでも、オプションで `callback_endpoint` を指定して、エクスポートの準備が整ったときに通知を受け取ることができます。`callback_endpoint` が指定された場合、ダウンロードの準備が整った時点で、指定されたアドレスにPOSTリクエストを送信します。POSTの本文は `"success":true` です。クラウドストレージの認証情報をBrazeに追加していない場合、POSTの本文にはさらに `url` 属性が含まれ、その値としてダウンロードURLが設定されます。

ユーザー群が大きいほど、エクスポート時間が長くなります。たとえば、2,000万人のユーザーを持つアプリの場合、1時間以上かかることがあります。

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "callback_endpoint" : (optional, string) endpoint to post a download URL to when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, for example, ['first_name', 'email', 'purchases'],
  "output_format" : (optional, string) When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format
}
```

{% alert warning %}
個々のカスタム属性をエクスポートすることはできません。ただし、fields_to_export配列にcustom_attributesを含めることで、すべてのカスタム属性をエクスポートできます（例：`['first_name', 'email', 'custom_attributes']`）。
{% endalert %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ------------------- | --------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_endpoint` | オプション | 文字列 | エクスポートが利用可能になったときにダウンロードURLをPOSTするエンドポイント。 |
| `fields_to_export` | 必須* | 文字列の配列 | エクスポートするユーザーデータフィールドの名前。カスタム属性もエクスポートできます。<br><br>*2021年4月以降、新しいアカウントではエクスポートする特定のフィールドを指定する必要があります。 |
| `output_format` | オプション | 文字列 | 独自のS3バケットを使用する場合、ファイル形式を `zip` または `gzip` に指定できます。デフォルトはZIPファイル形式です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/global_control_group' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "callback_endpoint" : "",
  "fields_to_export" : ["email", "braze_id"],
  "output_format" : "zip"
}'
```

## エクスポートするフィールド {#fields-to-export}

以下は、有効な `fields_to_export` のリストです。`fields_to_export` を使用して返されるデータを最小限に抑えると、このAPIエンドポイントのレスポンスタイムが向上します。

| エクスポートするフィールド | データタイプ | 説明 |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps` | 配列 | このユーザーがセッションを記録したアプリ。以下のフィールドが含まれます。<br><br>- `name`: アプリ名<br>- `platform`: アプリプラットフォーム（iOS、Android、Webなど）<br>- `version`: アプリのバージョン番号または名前<br>- `sessions`: このアプリの総セッション数<br>- `first_used`: 初回セッションの日付<br>- `last_used`: 最終セッションの日付<br><br>すべてのフィールドは文字列です。 |
| `attributed_campaign` | 文字列 | [アトリビューション連携]({{site.baseurl}}/partners/message_orchestration)からのデータ（設定されている場合）。特定の広告キャンペーンの識別子。 |
| `attributed_source` | 文字列 | [アトリビューション連携]({{site.baseurl}}/partners/message_orchestration)からのデータ（設定されている場合）。広告が掲載されたプラットフォームの識別子。 |
| `attributed_adgroup` | 文字列 | [アトリビューション連携]({{site.baseurl}}/partners/message_orchestration)からのデータ（設定されている場合）。キャンペーンの下のオプションのサブグループの識別子。 |
| `attributed_ad` | 文字列 | [アトリビューション連携]({{site.baseurl}}/partners/message_orchestration)からのデータ（設定されている場合）。キャンペーンおよび広告グループの下のオプションのサブグループの識別子。 |
| `braze_id` | 文字列 | このユーザーに対してBrazeが設定したデバイス固有の一意のユーザー識別子。 |
| `country` | 文字列 | [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)標準を使用したユーザーの国。 |
| `created_at` | 文字列 | ユーザープロファイルが作成された日時（ISO 8601形式）。 |
| `custom_attributes` | オブジェクト | このユーザーのカスタム属性のキーと値のペア。 |
| `custom_events` | 配列 | 過去90日間にこのユーザーに帰属するカスタムイベント。 |
| `devices` | 配列 | ユーザーのデバイスに関する情報。プラットフォームに応じて以下が含まれます。<br><br>- `model`: デバイスのモデル名<br>- `os`: デバイスのオペレーティングシステム<br>- `carrier`: デバイスのサービスキャリア（利用可能な場合）<br>- `idfv`: (iOS) Brazeデバイス識別子、Apple Identifier for Vendor（存在する場合）<br>- `idfa`: (iOS) Identifier for Advertising（存在する場合）<br>- `device_id`: (Android) Brazeデバイス識別子<br>- `google_ad_id`: (Android) Google Play Advertising Identifier（存在する場合）<br>- `roku_ad_id`: (Roku) Roku Advertising Identifier<br>- `ad_tracking_enabled`: デバイスで広告トラッキングが有効かどうか（trueまたはfalse） |
| `dob` | 文字列 | `YYYY-MM-DD` 形式のユーザーの生年月日。 |
| `email` | 文字列 | ユーザーのメールアドレス。 |
| `external_id` | 文字列 | 識別済みユーザーの一意のユーザー識別子。 |
| `first_name` | 文字列 | ユーザーの名。 |
| `gender` | 文字列 | ユーザーの性別。可能な値は以下のとおりです。<br><br>- `M`: 男性<br>- `F`: 女性<br>- `O`: その他<br>- `N`: 該当なし<br>- `P`: 回答しない<br>- `nil`: 不明 |
| `home_city` | 文字列 | ユーザーの居住都市。 |
| `language` | 文字列 | ISO-639-1標準のユーザーの言語。 |
| `last_coordinates` | 浮動小数点の配列 | `[longitude, latitude]` 形式のユーザーの最新のデバイス位置。 |
| `last_name` | 文字列 | ユーザーの姓。 |
| `phone` | 文字列 | E.164形式のユーザーの電話番号。 |
| `purchase`s | 配列 | このユーザーが過去90日間に行った購入。 |
| `random_bucket` | 整数 | ユーザーの[ランダムバケット番号]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)。ランダムユーザーの均一分布セグメントを作成するために使用されます。 |
| `time_zone` | 文字列 | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン。 |
| `total_revenue` | 浮動小数点 | このユーザーに帰属する総収益。総収益は、ユーザーが受信したキャンペーンおよびキャンバスのコンバージョン期間中に行った購入に基づいて計算されます。 |
| `uninstalled_at` | タイムスタンプ | ユーザーがアプリをアンインストールした日時。アプリがアンインストールされていない場合は省略されます。 |
| `user_aliases` | オブジェクト | `alias_name` および `alias_label` を含む[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object)（存在する場合）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fields to export" }

## レスポンス {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "object_prefix": (required, string) the filename prefix that is used for the JSON file produced by this export, for example,'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

URLが公開された後、有効なのは数時間のみです。そのため、独自のS3認証情報をBrazeに追加することを強くお勧めします。

### ユーザーエクスポートファイル出力のサンプル {#example-user-export-file-output}

ユーザーエクスポートオブジェクト（最小限のデータのみを含みます。オブジェクトからフィールドが欠落している場合、そのフィールドはnullまたは空であると見なしてください）：

{% tabs %}
{% tab All fields %}

```json
{
    "created_at" : (string),
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
        "ad_tracking_enabled" : (bool)
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (string),
        "first_used" : (string) date,
        "last_used" : (string) date
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
    ]
}
```

{% endtab %}
{% endtabs %}

{% endapi %}