---
nav_title: "ユーザー属性オブジェクト"
article_title: "ユーザー属性オブジェクト"
page_order: 11
page_type: reference
description: "このリファレンス記事では、ユーザー属性オブジェクトのさまざまなコンポーネントについて説明します。"
---

# ユーザー属性オブジェクト {#user-attributes-object}

> 属性オブジェクトにフィールドを含むAPIリクエストは、指定されたユーザープロファイルに指定された値で、その名前の属性を作成または更新します。

Brazeユーザープロファイルフィールド名（以下にリストされているもの、または[Brazeユーザープロファイルフィールド](#braze-user-profile-fields)のセクションにリストされているもの）を使用して、ダッシュボードのユーザープロファイル上の特別な値を更新するか、独自のカスタム属性データをユーザーに追加します。

## オブジェクト本体 {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
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
  // Array of objects custom attribute
  "my_array_of_objects_attribute": [{"key": "value"}, {"key": "value"}],
  // Adding to an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$add": [{"key": "value"}] },
  // Removing from an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$remove": [{"$identifier_key": "key", "$identifier_value": "value"}] },
}
```

- [External user ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

{% alert note %}
通常の配列カスタム属性には、`add` と `remove`（`$` なし）を使用します。

オブジェクト配列（階層化カスタム属性）には、`/users/track` リクエストペイロードで `$add`、`$remove`、`$update` を使用します。これらの演算子は、識別子（`$identifier_key` と `$identifier_value`）によるマッチングでオブジェクトレベルの変更を適用し、`$new_object` を使用したインプレース更新もサポートします。

このフォーマットは、配列の残りの状態を保持しながら、既存の配列内のオブジェクトを追加、削除、または更新する必要がある場合に使用します。リクエストの完全な例については、[オブジェクト配列の API の例]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example)と[オブジェクト配列のSDKの例]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example)を参照してください。
{% endalert %}

プロファイル属性を削除するには、`null` に設定します。`external_id` や `user_alias` などの一部のフィールドは、ユーザープロファイルに追加された後は削除できません。

### 識別子の解決 {#identifier-resolution}

[匿名プッシュトークンのインポート](#push-token-import)を行う場合を除き、各ユーザー属性オブジェクトには少なくとも1つの識別子（`external_id`、`user_alias`、`braze_id`、`email`、`phone`）を含める必要があります。可能な場合は、どのユーザープロファイルが更新または作成されるかの曖昧さを避けるため、オブジェクトごとに識別子を1つだけ含めてください。

識別子を使用する際は、以下の点に注意してください。

- **`external_id` と `user_alias` は相互排他的です。** 同一のユーザー属性オブジェクトに両方を含めるとエラーが返されます。すでに `external_id` を持つユーザーにエイリアスを追加するには、[`/users/alias/new` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_alias)を使用してください。
- **`email` は `phone` よりも優先されます。** 同一オブジェクトに `email` と `phone` の両方が含まれている場合、Brazeは `email` を識別子として使用します。つまり、電話番号が別のプロファイルに属している場合でも、属性はそのメールアドレスに関連付けられたユーザープロファイルに適用されます。

{% alert important %}
予期しない動作を避けるため、ユーザー属性オブジェクトごとに単一の識別子を使用してください。異なるユーザープロファイルを参照する複数の識別子を提供すると、属性が間違ったプロファイルに適用される可能性があります。
{% endalert %}

#### 既存プロファイルのみ更新する {#update-existing-profiles-only}

Brazeで既存のユーザープロファイルのみを更新したい場合は、リクエストの本文で `_update_existing_only` キーに `true` の値を渡す必要があります。この値が省略されると、`external_id` がまだ存在しない場合、Brazeは新しいユーザープロファイルを作成します。

{% alert note %}
`/users/track` エンドポイントを介してエイリアスのみのユーザープロファイルを作成する場合は、`_update_existing_only` を `false` に設定する必要があります。この値を省略すると、Brazeはエイリアスのみのプロファイルを作成しません。
{% endalert %}

#### プッシュトークンのインポート {#push-token-import}

プッシュトークンをBrazeにインポートする前に、それが必要かどうかを再確認してください。Braze SDKを導入すると、APIを通じてアップロードする必要なく、プッシュトークンを自動的に処理します。

APIを通じてアップロードする必要がある場合、識別済みのユーザーまたは匿名ユーザーのいずれかに対してアップロードできます。これは、`external_id` が存在するか、匿名ユーザーの `push_token_import` フラグが `true` に設定されている必要があることを意味します。

{% alert note %}
他のシステムからプッシュトークンをインポートする場合、`external_id` が常に利用可能とは限りません。Brazeへの移行期間中にこれらのユーザーとの通信を維持するには、`push_token_import` を `true` に指定することで、`external_id` を提供せずに匿名ユーザー用のレガシートークンをインポートできます。
{% endalert %}

`push_token_import` を `true` に指定する場合：

* `external_id` と `braze_id` は指定**しないでください**
* 属性オブジェクトにはプッシュトークンを**含める必要があります**
* トークンがすでにBrazeに存在する場合、リクエストは無視されます。存在しない場合、Brazeはトークンごとに一時的な匿名ユーザープロファイルを作成し、これらの個人に引き続きメッセージを送信できるようにします

インポート後、各ユーザーがBraze対応バージョンのアプリを起動すると、BrazeはインポートされたプッシュトークンをユーザーのBrazeユーザープロファイルに自動的に移動し、一時プロファイルをクリーンアップします。

Brazeは月に1回チェックを行い、`push_token_import` フラグが設定されているがプッシュトークンを持たない匿名プロファイルを検索します。匿名プロファイルにプッシュトークンがなくなった場合、Brazeはそのプロファイルを削除します。ただし、匿名プロファイルにまだプッシュトークンがある場合（実際のユーザーがそのプッシュトークンを持つデバイスでまだログインしていないことを示しています）、Brazeは何も行いません。

詳細については、[プッシュトークンの移行](#migrate-push-tokens)を参照してください。

#### カスタム属性のデータ型 {#custom-attribute-data-types}

以下のデータ型をカスタム属性として保存できます。

| データ型 | 注記 |
| --- | --- |
| 配列 | カスタム属性の配列がサポートされています。要素を追加すると、配列の末尾に追加されます。要素がすでに存在する場合は、現在の位置から末尾に移動されます。<br><br>一意の値のみが保存されます。例えば、`['hotdog','hotdog','hotdog','pizza']` をインポートすると、`['hotdog', 'pizza']` になります。<br><br>配列を直接設定する（例：`"my_array_custom_attribute":[ "Value1", "Value2" ]`）か、`"my_array_custom_attribute" : { "add" : ["Value3"] }` で既存の配列に追加するか、`"my_array_custom_attribute" : { "remove" : [ "Value1" ]}` で値を削除できます。<br><br>配列のデフォルトおよび最大要素数は500です。最大配列数はBrazeダッシュボードの**データ設定** > **カスタム属性**で更新できます。詳細については、[配列]({{site.baseurl}}/developer_guide/analytics#arrays)を参照してください。 |
| オブジェクト配列 | オブジェクト配列を使用して、各オブジェクトが属性のセットを含むオブジェクトのリストを定義します。この型を使用して、ホテルの宿泊、購入履歴、好みなど、ユーザーの関連データの複数のセットを保存できます。<br><br>例えば、ユーザープロファイルに `hotel_stays` というカスタム属性を配列として定義し、各オブジェクトが `hotel_name`、`check_in_date`、`nights_stayed` などの属性を持つ個別の宿泊を表すようにします。<br><br>オブジェクト配列はアイテム数に制限はありませんが、最大サイズは100&nbsp;KBです。更新によって配列がこの制限を超える場合、Brazeは更新を破棄し、属性は変更されません。<br><br>`/users/track` およびSDKペイロードでは、オブジェクト配列操作に `$add`、`$remove`、`$update` を使用します。スカラー値を含む通常の配列カスタム属性には、`add` と `remove`（`$` なし）を使用します。詳細については、[オブジェクト配列の API の例]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example)、[オブジェクト配列のSDKの例]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example)、および[オブジェクト配列の例](#array-of-objects-example)を参照してください。 |
| ブール値 | `true` または `false` |
| 日付 | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 形式（推奨）または以下のいずれかの形式で日付を保存します：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>「T」は時間指定子であり、プレースホルダーではないため、変更または削除しないでください。<br><br>リストされている形式のいずれにも一致しない日付値は、Time データ型ではなく文字列としてユーザープロファイルに保存されます。これは、時間ベースのセグメンテーションフィルター（「前」「後」「過去 X 日間」など）がこれらの属性に対して機能しないことを意味します。例えば、`Mar 26 2026 06:12 PM +00:00` はサポートされている形式に一致しないため、文字列として保存されます。これを避けるには、ISO 8601 形式（例：`2026-03-26T18:12:00Z`）を使用してください。<br><br>タイムゾーンのない時間属性は、デフォルトで UTC の深夜になります（ダッシュボードでは会社のタイムゾーンでの UTC 深夜に相当する形式で表示されます）。タイムゾーンを指定するには、タイムスタンプに UTC オフセットを追加します（例：EST の場合 `2024-11-10T18:00:00-05:00`）。タイムゾーンオフセットが欠落しているか、形式が正しくない場合、値はデフォルトで UTC になります。<br><br>時間はダッシュボードで会社のタイムゾーンで表示されます。例えば、`2024-11-10T18:00:00-05:00`（EST 午後6:00）は、会社の設定されたタイムゾーンで同等の時間として表示されます。<br><br>将来のタイムスタンプを持つイベントは、デフォルトで現在の時間になります。<br><br>通常のカスタム属性の場合、年が0未満または3000を超えると、Brazeはその値を文字列としてユーザープロファイルに保存します。 |
| 浮動小数点数 | 浮動小数点数のカスタム属性は、小数点を持つ正または負の数値です。例えば、浮動小数点数を使用して口座残高やユーザーの製品・サービスの評価を保存できます。 |
| 整数 | 「inc」フィールドと加算する量を持つオブジェクトを割り当てることで、整数カスタム属性をインクリメントできます。<br><br>例：`"my_custom_attribute_2" : {"inc" : int_value},`|
| 階層化カスタム属性 | 階層化カスタム属性は、別の属性のプロパティとして属性のセットを定義します。カスタム属性オブジェクトを定義する際に、そのオブジェクトに属性のセットを追加します。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)を参照してください。 |
| 文字列 | 文字列カスタム属性は、テキストデータを保存するために使用される文字のシーケンスです。例えば、文字列を使用して姓名、メールアドレス、または好みを保存できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタム属性のデータ型" }

{% alert tip %}
カスタムイベントとカスタム属性のどちらを使用すべきかについてのガイダンスは、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)と[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)を参照してください。
{% endalert %}

##### オブジェクト配列の例 {#array-of-objects-example}

このオブジェクト配列を使用すると、宿泊内の特定の条件に基づいてセグメントを作成し、Liquid テンプレートを使用して各宿泊のデータでメッセージをパーソナライズできます。

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

`$add`、`$remove`、`$update` を使用したオブジェクト配列の例については、[オブジェクト配列の API の例]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example)と[オブジェクト配列のSDKの例]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example)を参照してください。

#### Brazeユーザープロファイルフィールド {#braze-user-profile-fields}

{% alert important %}
以下のユーザープロファイルフィールドは大文字と小文字を区別するため、必ず小文字で参照してください。
{% endalert %}

{% alert tip %}
カテゴリ別に整理され、SDK、API、CSV、Cloud Data Ingestion のガイダンスを含む顧客向けの標準属性リファレンスについては、[標準属性]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes)を参照してください。
{% endalert %}

| ユーザープロファイルフィールド | データ型の仕様 |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | (string、オプション) ユーザープロファイルがSDKによって認識されると、関連する `braze_id` を持つ匿名ユーザープロファイルが作成されます。`braze_id` はBrazeによって自動的に割り当てられ、編集できず、デバイス固有です。 |
| country | (string) 国コードは [ISO-3166-1 alpha-2 標準](http://en.wikipedia.org/wiki/ISO_3166-1)でBrazeに渡す必要があります。APIは異なる形式で受信した国のマッピングにベストエフォートで対応します。例えば、「Australia」は「AU」にマッピングされる場合があります。ただし、入力が指定された [ISO-3166-1 alpha-2 標準](http://en.wikipedia.org/wiki/ISO_3166-1)に一致しない場合、国の値は `NULL` に設定されます。<br><br>CSVインポートまたはAPIによってユーザーに `country` を設定すると、BrazeはSDKを通じてこの情報を自動的にキャプチャしなくなります。 |
| current_location | (object) {"longitude": -73.991443, "latitude": 40.753824} の形式 |
| date_of_first_session | (ユーザーが最初にアプリを使用した日付) ISO 8601 形式または以下のいずれかの形式の文字列：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (ユーザーが最後にアプリを使用した日付) ISO 8601 形式または以下のいずれかの形式の文字列：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (生年月日) 「YYYY-MM-DD」形式の文字列（例：1980-12-21）。 |
| email | (string) |
| email_subscribe | (string) 使用可能な値は「opted_in」（メールメッセージの受信を明示的に登録）、「unsubscribed」（メールメッセージを明示的にオプトアウト）、「subscribed」（オプトインもオプトアウトもしていない）です。 |
| email_open_tracking_disabled | (boolean) `true` または `false` を受け入れます。`true` に設定すると、このユーザーに送信される今後すべてのメールに開封トラッキングピクセルが追加されなくなります。|
| email_click_tracking_disabled | (boolean) `true` または `false` を受け入れます。`true` に設定すると、このユーザーに送信される今後のメール内のすべてのリンクのクリックトラッキングが無効になります。|
| external_id | (string) ユーザープロファイルの一意の識別子です。`external_id` が割り当てられると、Brazeはユーザーのデバイス間でユーザープロファイルを識別します。未知のユーザープロファイルに初めて external_id を割り当てると、Brazeは既存のすべてのユーザープロファイルデータを新しいユーザープロファイルに移行します。 |
| facebook | `id`（string）、`likes`（文字列の配列）、`num_friends`（integer）のいずれかを含むハッシュ。 |
| first_name | (string) |
| gender | (string) 「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（回答しない）、または null（不明）。 |
| home_city | (string) |
| language | (string) 言語は [ISO-639-1 標準](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)でBrazeに渡す必要があります。サポートされている言語については、[受け入れ可能な言語の一覧]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes)を参照してください。<br><br>CSVインポートまたはAPIによってユーザーに `language` を設定すると、BrazeはSDKを通じてこの情報を自動的にキャプチャしなくなります。 |
| last_name | (string) |
| marked_email_as_spam_at | (string) ユーザーのメールがスパムとしてマークされた日付。ISO 8601 形式または以下のいずれかの形式で表示されます：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (string) 電話番号は [E.164](https://en.wikipedia.org/wiki/E.164) 形式で提供することを推奨します。詳細については、[ユーザーの電話番号]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format)を参照してください。|
| push_subscribe | (string) 使用可能な値は「opted_in」（プッシュメッセージの受信を明示的に登録）、「unsubscribed」（プッシュメッセージを明示的にオプトアウト）、「subscribed」（オプトインもオプトアウトもしていない）です。 |
| push_tokens | `app_id` と `token` の文字列を持つオブジェクトの配列。オプションで、このトークンに関連付けられたデバイスの `device_id` を提供できます。例：`[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`。`device_id` が提供されない場合、ランダムに生成されます。 |
| subscription_groups | `subscription_group_id` と `subscription_state` の文字列を持つオブジェクトの配列。例：`[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`。`subscription_state` の使用可能な値は「subscribed」と「unsubscribed」です。|
| time_zone | (string) [IANA タイムゾーンデータベース](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)のタイムゾーン名（例：「America/New_York」または「Eastern Time (US & Canada)」）。有効なタイムゾーン値のみが設定されます。 |
| twitter | `id`（integer）、`screen_name`（string、X（旧 Twitter）ハンドル）、`followers_count`（integer）、`friends_count`（integer）、`statuses_count`（integer）のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeユーザープロファイルフィールド" }

このAPIを通じて明示的に設定された言語値は、Brazeがデバイスから自動的に受信するロケール情報よりも優先されます。

#### ユーザー属性のリクエスト例 {#user-attribute-example-request}

この例には、API 呼び出しごとに許可される最大75個の属性オブジェクトのうち、4つのユーザー属性オブジェクトが含まれています。

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Alex",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Lee",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Yuri",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## プッシュトークンの移行 {#migrate-push-tokens}

Braze統合前にプッシュ通知を送信していた場合（自社で送信していた場合や他のプロバイダーを利用していた場合）、プッシュトークンの移行を行うことで、登録済みのプッシュトークンを持つユーザーに引き続きプッシュ通知を送信できます。

### SDKによる自動移行 {#automatic-migration-through-sdk}

[Braze SDKを統合]({{site.baseurl}}/developer_guide/sdk_integration)すると、オプトイン済みユーザーのプッシュトークンは次回アプリを開いた際に自動的に移行されます。それまでは、Brazeを通じてこれらのユーザーにプッシュ通知を送信することはできません。

あるいは、[プッシュトークンを手動で移行](#manual-migration-through-api)することで、ユーザーにより迅速にリエンゲージメントできます。

#### Webトークンに関する考慮事項 {#web-token-considerations}

Webプッシュトークンの特性上、Webプッシュを実装する際は以下の点を考慮してください。

|考慮事項|詳細|
|----------------------|------------|
| **サービスワーカー**  | デフォルトでは、Web SDKは`./service-worker`でサービスワーカーを検索します。ただし、`manageServiceWorkerExternally`や`serviceWorkerLocation`など別のオプションが指定されている場合は除きます。サービスワーカーが適切に設定されていない場合、ユーザーのプッシュトークンが期限切れになる可能性があります。 |
| **期限切れトークン**   | ユーザーが60日以内にWebセッションを開始しなかった場合、プッシュトークンは期限切れになります。Brazeは期限切れのプッシュトークンを移行できないため、[プッシュプライマー]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を送信してリエンゲージメントする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webトークンに関する考慮事項" }

### APIによる手動移行 {#manual-migration-through-api}

プッシュトークンの手動移行とは、過去に作成されたキーをAPIを通じてBrazeプラットフォームにインポートするプロセスです。

[`users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、iOS（APNs）およびAndroid（FCM）トークンをプログラムでプラットフォームに移行できます。識別済みユーザー（external IDが関連付けられているユーザー）と匿名ユーザー（external IDのないユーザー）の両方を移行できます。

プッシュトークン移行時にアプリの`app_id`を指定して、適切なプッシュトークンを適切なアプリに関連付けます。各アプリ（iOS、Androidなど）には固有の`app_id`があり、[APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)ページの**識別**セクションで確認できます。正しいプラットフォームの`app_id`を使用してください。

{% alert important %}
APIを通じてWebプッシュトークンを移行することはできません。Webプッシュトークンは他のプラットフォームと同じスキーマに準拠していないためです。

<br>Webプッシュトークンをプログラムで移行しようとすると、次のようなエラーが表示される場合があります：`Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
APIの移行の代替として、SDKを統合してトークンベースを自然に再構築することをお勧めします。
{% endalert %}

{% tabs local %}
{% tab External IDあり %}
識別済みユーザーの場合、`push_token_import`フラグを`false`に設定（またはパラメーターを省略）し、ユーザー`attributes`オブジェクトで`external_id`、`app_id`、`token`の値を指定します。

例：

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab External IDなし %}
他のシステムからプッシュトークンをインポートする場合、`external_id`が常に利用できるとは限りません。この場合、`push_token_import`フラグを`true`に設定し、`app_id`と`token`の値を指定します。Brazeは各トークンに対して一時的な匿名ユーザープロファイルを作成し、引き続きこれらの個人にメッセージを送信できるようにします。トークンがBrazeに既に存在する場合、リクエストは無視されます。

例：

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

インポート後、匿名ユーザーがBraze対応バージョンのアプリを起動すると、Brazeはインポートされたプッシュトークンを自動的にそのBrazeユーザープロファイルに移動し、一時プロファイルをクリーンアップします。

Brazeは月に1回、`push_token_import`フラグが設定されているがプッシュトークンを持たない匿名プロファイルがないかチェックします。匿名プロファイルにプッシュトークンがなくなった場合、Brazeはそのプロファイルを削除します。ただし、匿名プロファイルにまだプッシュトークンがある場合（実際のユーザーがそのプッシュトークンを持つデバイスにまだログインしていないことを示しています）、Brazeは何もしません。
{% endtab %}
{% endtabs %}

### iOSプッシュトークンのインポート {#import-ios-push-tokens}

`/users/track`でiOSプッシュトークンを移行する場合、プッシュトークンに`gateway`フィールドは設定されません。Brazeは、APIを通じてインポートされたトークンを有効なフォアグラウンドプッシュトークンとみなしますが、そのトークンがどのAPNs環境に属するかは判断できません。

gatewayフィールドがない場合、Brazeはプッシュ通知を送信する際にアプリの設定済みフォールバック環境設定を使用します。トークンの実際の環境が設定済みフォールバックと異なる場合、`BadDeviceToken`エラーが発生する可能性があります。例えば、開発用トークンが本番用ゲートウェイを通じて送信された場合、失敗します。

配信の問題を避けるために：

- Brazeダッシュボードのアプリ環境設定が、インポートするトークンと一致していることを確認してください。
- 本番アプリの場合、本番用トークンのみをインポートしてください。
- テスト環境の場合、アプリの構成とインポートするトークンの両方が開発環境を使用していることを確認してください。

{% alert note %}
Braze SDKを通じて登録されたトークンには、SDKがアプリのエンタイトルメントから環境を検出するため、gatewayフィールドが自動的に含まれます。
{% endalert %}

### Androidプッシュトークンのインポート {#import-android-push-tokens}

{% alert important %}
以下の考慮事項はAndroidアプリにのみ適用されます。iOSアプリではこれらのステップは不要です。iOSにはプッシュを表示するフレームワークが1つしかなく、Brazeが必要なプッシュトークンと証明書を持っている限り、プッシュ通知はすぐにレンダリングされるためです。
{% endalert %}

Braze SDKの統合が完了する前にユーザーにAndroidプッシュ通知を送信する必要がある場合は、キーと値のペアを使用してプッシュ通知を検証します。

プッシュペイロードを処理および表示するレシーバーが必要です。プッシュペイロードをレシーバーに通知するには、プッシュキャンペーンに必要なキーと値のペアを追加します。これらのペアの値は、Braze以前に使用していた特定のプッシュパートナーによって異なります。

{% alert note %}
一部のプッシュ通知プロバイダーでは、Brazeがキーと値のペアを適切に解釈できるようにフラット化する必要があります。特定のAndroidアプリのキーと値のペアをフラット化するには、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### スパムとして扱われているユーザーやメッセージングからブロックされているユーザーを見つけるにはどうすればよいですか？ {#how-do-i-find-users-treated-as-spam-or-blocked-from-messaging}

Brazeはダッシュボードに専用のスパムリストを提供していません。Brazeは、500万を超えるセッション、20,000を超える個別のカスタムイベント名、または購入における20,000を超える個別の製品名を持つ個々のユーザープロファイル（「ダミーユーザー」）をブロックし、SDKとREST APIの両方からそのプロファイルのすべての受信データの取り込みを停止します。識別子がブロックされている場合、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)はエラー`"provided external_id is blacklisted and disallowed"`を返すことがあります。この文言はAPIレスポンスからそのまま引用されたものです。過剰なセッションによりブロックされたプロファイルを見つけるには、**セッション数**フィルターを**5,000,000より多い**に設定した[セグメント]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)を作成し、セグメントをCSVとしてエクスポートして、**エンゲージメント** > **ユーザー検索**またはは[`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)エンドポイントでプロファイルフィールドを照合します。個別のカスタムイベント名や製品名に対する同等のフィルターはないため、それらの理由でブロックされたプロファイルを特定するには、Brazeアカウントマネージャーにお問い合わせください。詳細については、[スパムブロック]({{site.baseurl}}/user_archival)を参照してください。