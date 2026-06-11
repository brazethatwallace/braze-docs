---
nav_title: 標準属性項目
article_title: 標準属性項目
page_order: 0.5
page_type: reference
description: "このリファレンス記事では、Brazeの標準ユーザー属性（予約キー）と各属性の構文要件を一覧で紹介します。"
---

# 標準属性項目 {#standard-attributes}

> 標準属性項目は、Brazeがすべてのユーザープロファイルで認識する定義済みのフィールドです。このページでは、各標準属性項目のフィールド名、データタイプ、想定されるフォーマットをクイックリファレンスとして確認できます。

標準属性項目（*デフォルト属性*や*予約キー*とも呼ばれます）は、ビジネス固有の[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)とは異なります。このページに記載されているフィールド名でBrazeにデータを送信すると、Brazeは新しいカスタム属性を作成する代わりに、定義済みのプロファイルフィールドにデータを保存します。

標準属性項目は、以下のいずれかの方法で設定できます。

- [Braze SDK]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)
- [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)の[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)
- [CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)
- [クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)

{% alert important %}
標準属性項目の名前は大文字と小文字が区別されます。常に小文字を使用してください（例：`First_Name`ではなく`first_name`）。スペルや大文字小文字が正確に一致しない場合、Brazeはその値を[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)として保存します。
{% endalert %}

## 識別子 {#identifiers}

識別子は、Brazeにどのユーザープロファイルを更新または作成するかを伝えます。すべてのAPIリクエストとCSV行には、少なくとも1つの識別子を含める必要があります。適切な識別子の選択方法については、[識別子の解決]({{site.baseurl}}/api/objects_filters/user_attributes_object/#identifier-resolution)を参照してください。

| フィールド | データタイプ | フォーマットと注意事項 |
|---|---|---|
| `external_id` | 文字列 | ユーザーに割り当てる一意の識別子です。プロファイルに設定されると、Brazeはこの識別子を使用してデバイス間でユーザーを認識します。追加後は削除できません。 |
| `braze_id` | 文字列 | SDKが初めてデバイスを検出したときに作成される、Brazeが割り当てる識別子です。読み取り専用で、編集できません。 |
| `user_alias` | オブジェクト | `alias_name`（文字列）と`alias_label`（文字列）を含むオブジェクトで、`external_id`を持たないユーザーを識別するために使用します。同じリクエスト内で`external_id`とは相互排他的です。 |
| `email` | 文字列 | `external_id`と`user_alias`がない場合に識別子として使用できます。両方が送信された場合、`phone`よりも優先されます。 |
| `phone` | 文字列 | `external_id`、`user_alias`、`email`がない場合に識別子として使用できます。[E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#recommended-format)形式を使用してください（例：`+14155552671`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## プロファイルフィールド {#profile-fields}

これらのフィールドは、ユーザーのデモグラフィック、連絡先、ロケールデータを取得します。

| フィールド | データタイプ | フォーマットと注意事項 |
|---|---|---|
| `first_name` | 文字列 | ユーザーの名（例：`Jane`）。 |
| `last_name` | 文字列 | ユーザーの姓（例：`Doe`）。 |
| `email` | 文字列 | ユーザーのメールアドレス（例：`jane.doe@braze.com`）。 |
| `phone` | 文字列 | ユーザーの電話番号。[E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#recommended-format)形式を使用してください（例：`+14155552671`）。 |
| `dob` | 文字列 | 生年月日。`YYYY-MM-DD`形式で指定します（例：`1988-02-14`）。誕生日によるターゲティングが可能になります。 |
| `gender` | 文字列 | `M`、`F`、`O`（その他）、`N`（該当なし）、`P`（回答しない）、または`null`（不明）のいずれかです。 |
| `country` | 文字列 | [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1)形式の国コード（例：`US`、`GB`）。CSVインポートまたはAPIで`country`を設定すると、SDKによる自動取得が無効になります。 |
| `home_city` | 文字列 | ユーザーの居住都市（例：`London`）。 |
| `language` | 文字列 | [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)形式の言語コード（例：`en`）。[対応言語の一覧]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes/)を参照してください。CSVインポートまたはAPIで`language`を設定すると、SDKによる自動取得が無効になります。 |
| `time_zone` | 文字列 | [IANAタイムゾーンデータベース](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)のタイムゾーン名（例：`America/New_York`または`Eastern Time (US & Canada)`）。 |
| `current_location` | オブジェクト | `longitude`と`latitude`を含むオブジェクト（例：`{"longitude": -73.991443, "latitude": 40.753824}`）。 |
| `image_url` | 文字列 | ユーザーのプロファイル画像のURL。最大1,024文字です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## サブスクリプションと同意 {#subscription-and-consent}

これらのフィールドは、ユーザーがチャネル間でメッセージを受信する方法を管理します。これらのフィールドを更新しても、データポイント使用量にはカウントされません。

| フィールド | データタイプ | フォーマットと注意事項 |
|---|---|---|
| `email_subscribe` | 文字列 | `opted_in`（メール受信を明示的に登録）、`unsubscribed`（メールを明示的にオプトアウト）、または`subscribed`（オプトインもオプトアウトもしていない）のいずれかです。 |
| `push_subscribe` | 文字列 | `opted_in`、`unsubscribed`、または`subscribed`のいずれかです。定義は`email_subscribe`と同じです。 |
| `subscription_groups` | オブジェクトの配列 | 各オブジェクトに`subscription_group_id`（文字列）と`subscription_state`（`subscribed`または`unsubscribed`）を含む配列です。例：`[{"subscription_group_id": "abc-123", "subscription_state": "subscribed"}]`。 |
| `email_open_tracking_disabled` | ブール値 | `true`または`false`。`true`に設定すると、このユーザーのメール開封トラッキングピクセルが無効になります。SparkPostとSendGridでのみ利用可能です。 |
| `email_click_tracking_disabled` | ブール値 | `true`または`false`。`true`に設定すると、このユーザーのメールクリックトラッキングが無効になります。SparkPostとSendGridでのみ利用可能です。 |
| `marked_email_as_spam_at` | 文字列 | ユーザーのメールがスパムとしてマークされたタイムスタンプです。[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)形式を使用してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

サブスクリプショングループの設定の詳細については、[サブスクリプショングループ]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-groups)を参照してください。

## セッションとエンゲージメント {#sessions-and-engagement}

これらのフィールドは、ユーザーが最初または最後にアプリを利用した日時を記録します。SDKが自動的に記録するため、通常は別のプラットフォームから移行する場合にのみAPIまたはCSVで設定します。

| フィールド | データタイプ | フォーマットと注意事項 |
|---|---|---|
| `date_of_first_session` | 文字列 | ユーザーが初めてアプリを使用した日付です。[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)形式、または次のいずれかの形式を使用します：`yyyy-MM-ddTHH:mm:ss:SSSZ`、`yyyy-MM-ddTHH:mm:ss`、`yyyy-MM-dd HH:mm:ss`、`yyyy-MM-dd`、`MM/dd/yyyy`、`ddd MM dd HH:mm:ss.TZD YYYY`。 |
| `date_of_last_session` | 文字列 | ユーザーが最後にアプリを使用した日付です。`date_of_first_session`と同じ形式を使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## プッシュトークン {#push-tokens}

これらのフィールドは、別のプラットフォームからプッシュトークンを移行する際に使用します。Braze SDKを統合すると、プッシュトークンは自動的に取得されます。移行のガイダンスについては、[プッシュトークンの移行]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens)を参照してください。

| フィールド | データタイプ | フォーマットと注意事項 |
|---|---|---|
| `push_tokens` | オブジェクトの配列 | 各オブジェクトに`app_id`（文字列）と`token`（文字列）を含む配列です。オプションで`device_id`（文字列）を含めることもできます。例：`[{"app_id": "YOUR_APP_ID", "token": "abcd", "device_id": "optional_device_id"}]`。 |
| `push_token_import` | ブール値 | トップレベルのフラグです（`attributes`内にネストしません）。`external_id`を持たない匿名ユーザーのレガシープッシュトークンをインポートする場合に`true`に設定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ソーシャルプロファイル {#social-profile}

これらのフィールドは、ソーシャルネットワーク統合からのデータを保存します。

| フィールド | データタイプ | フォーマットと注意事項 |
|---|---|---|
| `facebook` | オブジェクト | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むオブジェクトです。 |
| `twitter` | オブジェクト | `id`（整数）、`screen_name`（文字列、Xハンドル）、`followers_count`（整数）、`friends_count`（整数）、`statuses_count`（整数）のいずれかを含むオブジェクトです。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## APIの例 {#api-example}

以下のリクエストは、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を通じて2人のユーザーに標準属性項目を設定します。

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
    {
      "external_id": "user1",
      "first_name": "Jane",
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

完全なAPIコントラクトについては、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を参照してください。

## CSVの例 {#csv-example}

以下のCSVは、2人のユーザーの標準属性項目を更新します。列ヘッダーは、この記事のフィールド名と正確に一致する必要があります。一致しないヘッダー（例：`first_name`ではなく`First_name`）は、カスタム属性としてインポートされます。

```plaintext
external_id,first_name,last_name,email,country,language,dob,email_subscribe
user1,Jane,Doe,jane.doe@example.com,US,en,1988-02-14,opted_in
user2,Alex,Smith,alex.smith@example.com,GB,en,1992-09-30,subscribed
```

一部の標準属性項目はCSVインポートでは設定できません。配列、プッシュトークン、ネストされたオブジェクトは、APIまたは[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)を通じて送信する必要があります。CSVでサポートされるフィールドの完全なリストとインポート手順については、[デフォルト属性]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/#default-attributes)を参照してください。

## 注意事項 {#considerations}

標準属性項目を使用する際は、以下の点を考慮してください。

- **フィールド名は大文字と小文字が区別されます。** 常に小文字を使用してください。標準属性項目名と正確に一致しないヘッダーやキーは、カスタム属性として扱われます。
- **APIまたはCSVで値を設定すると、SDKの自動取得が無効になります。** APIまたはCSVで`country`や`language`を設定すると、Brazeはそのユーザーについて、SDKからのこれらのフィールドの自動取得を停止します。
- **`null`は値を削除します。** 標準属性項目を`null`に設定すると、プロファイルから削除されます。`external_id`や`user_alias`など、一部のフィールドは設定後に削除できません。
- **CSVの空白値は上書きしません。** CSVインポートの空白セルは、プロファイルの既存の値を保持します。値をクリアするには、APIを使用してください。
- **タイムゾーンのデフォルトはUTCです。** オフセットのない日付文字列はUTCの午前0時として解釈され、ワークスペースのタイムゾーンで表示されます。タイムゾーンを指定するには、UTCオフセットを追加してください（例：`2024-11-10T18:00:00-05:00`）。

## 関連ページ {#related-pages}

- [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/) — 属性オブジェクトの完全なAPIコントラクト。
- [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) — ユーザープロファイルの作成と更新を行うRESTエンドポイント。
- [ユーザー属性の設定]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/) — 標準属性項目とカスタム属性を設定するためのSDKメソッド。
- [CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/) — CSVファイルを通じて標準属性項目をアップロードします。
- [カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) — ビジネス固有の属性を定義します。
- [データタイプ]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/) — サポートされるデータタイプのリファレンス。