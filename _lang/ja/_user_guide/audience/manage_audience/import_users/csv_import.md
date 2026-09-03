---
nav_title: CSVインポート
article_title: CSVインポート
description: "CSVインポートを使用してユーザー属性やカスタムイベントを記録・更新する方法を説明します。"
page_order: 1.2
---

# CSVインポート {#csv-import}

> CSVインポートを使用してユーザー属性やカスタムイベントを記録・更新する方法を説明します。

## CSVインポートについて {#about-csv-import}

CSVインポートを使用して、以下のユーザー属性とカスタムイベントを記録・更新できます。Brazeは、以下の表に示す最大サイズ以内の標準CSVファイルとしてこのデータを受け付けます。

|タイプ|定義|例|最大ファイルサイズ|
|---|---|---|---|
|デフォルト属性|Brazeが認識する予約済みユーザー属性。| `first_name`、`email`|500 MB|
|カスタム属性|ビジネスに固有のユーザー属性。| `last_destination_searched`|500 MB|
|カスタムイベント|ユーザーアクションを表す、ビジネスに固有のイベント。| `trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CSVインポートについて" }

## CSVインポートの使用 {#using-csv-import}

### ステップ1：CSVテンプレートをダウンロードする {#step-1-download-a-csv-template}

CSVインポートを開くには、**オーディエンス** > **ユーザーをインポート**に移動します。ここには、アップロード日、アップローダーの名前、ファイル名、ターゲティングの利用可否、インポートされた行数、インポートのステータスなど、最新のインポートに関する詳細を一覧表示するテーブルがあります。

まず、**属性**または**イベント**を選択し、アップロード用のCSVファイルを作成するための適切なテンプレートをダウンロードします。

![Brazeダッシュボードの「ユーザーをインポート」ページ。]({% image_buster /assets/img/csv_import/import_users_page.png %})

### ステップ2：識別子を選択する {#choose-an-identifier}

インポートするCSVファイルには、専用の識別子が必要です。インポートに使用する識別子タイプを以下から選択してください。

{% tabs local %}
<!-- TAB -->
{% tab external id %}
顧客データをインポートする際、各顧客の一意の識別子として`external_id`を使用できます。インポートで`external_id`を指定すると、Brazeは同じ`external_id`を持つ既存ユーザーを更新するか、該当する`external_id`が見つからない場合はその`external_id`が設定された新しい識別済みユーザーを作成します。

- ダウンロード：[CSV属性インポートテンプレート：External ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- ダウンロード：[CSVイベントインポートテンプレート：External ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
`external_id`を持つユーザーと持たないユーザーが混在する場合は、インポートごとに1つのCSVを作成する必要があります。1つのCSVに`external_id`とユーザーエイリアスの両方を含めることはできません。
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
`external_id`を持たないユーザーをターゲットにするには、ユーザーエイリアスを含むユーザーリストをインポートできます。エイリアスは代替の一意のユーザー識別子として機能し、サインアップやアカウント作成を行っていない匿名ユーザーにマーケティングを行う場合に役立ちます。

エイリアスのみのユーザープロファイルをアップロードまたは更新する場合、CSVに次の2つの列が必要です。

- `user_alias_name`：一意のユーザー識別子。`external_id`の代替です
- `user_alias_label`：ユーザーエイリアスをグループ化するための共通ラベル

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@example.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@example.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="ステップ2：識別子を選択する" }

インポートで`user_alias_name`と`user_alias_label`の両方を指定すると、Brazeは同じ`user_alias_name`と`user_alias_label`を持つ既存ユーザーを更新します。該当するユーザーが見つからない場合、Brazeはその`user_alias_name`が設定された新しい識別済みユーザーを作成します。

{% alert important %}
既に`external_id`を持つ既存ユーザーを`user_alias_name`でCSVインポートによって更新することはできません。代わりに、関連付けられた`user_alias_name`を持つ新しいユーザープロファイルが作成されます。エイリアスのみのユーザーを`external_id`に関連付けるには、[ユーザー識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用してください。
{% endalert %}

ダウンロード：[CSV属性インポートテンプレート：ユーザーエイリアス]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
`external_id`や`user_alias_name`と`user_alias_label`の値の代わりに、内部のBraze ID値を使用してBraze内の既存ユーザープロファイルを更新するには、列ヘッダーとして`braze_id`を指定します。

これは、セグメンテーション内のCSVエクスポートオプションを使用してBrazeからユーザーデータをエクスポートし、既存ユーザーに新しいカスタム属性を追加したい場合に便利です。

{% alert important %}
`braze_id`を使用してCSVインポートで新しいユーザーを作成することはできません。このメソッドは、Brazeプラットフォーム内の既存ユーザーの更新にのみ使用できます。
{% endalert %}

{% alert tip %}
Brazeダッシュボードからのエクスポートでは、`braze_id`の値が`Appboy ID`と表示されている場合があります。このIDはユーザーの`braze_id`と同じであるため、CSVを再インポートする際にこの列の名前を`braze_id`に変更できます。
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab メールアドレスと電話番号 %}
external IDやユーザーエイリアスを省略し、メールアドレスまたは電話番号を使用してユーザーをインポートできます。メールアドレスや電話番号を含むCSVファイルをインポートする前に、以下を確認してください。

- CSVファイルにこれらのプロファイルのexternal IDやユーザーエイリアスが含まれていないことを確認してください。含まれている場合、Brazeはプロファイルの識別にメールアドレスよりもexternal IDまたはユーザーエイリアスを優先します。
- CSVファイルが正しくフォーマットされていることを確認してください。

{% alert note %}
CSVファイルにメールアドレスと電話番号の両方が含まれている場合、プロファイルの検索時にメールアドレスが電話番号より優先されます。
{% endalert %}

該当するメールアドレスまたは電話番号を持つ既存のプロファイルがある場合、そのプロファイルが更新され、Brazeは新しいプロファイルを作成しません。同じメールアドレスを持つプロファイルが複数ある場合、Brazeは[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)と同じロジックを使用し、最後に更新されたプロファイルが更新されます。

該当するメールアドレスまたは電話番号を持つプロファイルが存在しない場合、Brazeはその識別子で新しいプロファイルを作成します。[`/users/identify`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用して、後からこのプロファイルを識別できます。ユーザープロファイルを削除するには、[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)エンドポイントも使用できます。
{% endtab %}
{% endtabs %}

### ステップ3：CSVファイルを作成する {#step-3-build-your-csv-file}

以下のいずれかのデータタイプを1つのCSVファイルとしてアップロードできます。複数のデータタイプをアップロードするには、複数のCSVファイルをアップロードしてください。

- **ユーザー属性：**デフォルトのユーザー属性とカスタム属性の両方が含まれます。デフォルトのユーザー属性はBrazeの予約キー（`first_name`や`email`など）であり、カスタム属性はビジネスに固有のユーザー属性（`last_destination_searched`など）です。
- **カスタムイベント：**ビジネスに固有で、旅行予約アプリでの`trip_booked`など、ユーザーが実行したアクションを反映するイベントです。

CSVファイルの作成を開始する準備ができたら、以下の情報を参照してください。

{% tabs local %}
<!-- TAB -->
{% tab ユーザー属性 %}
#### 必須の識別子 {#required-identifiers-attributes}

`external_id`は必須ではありませんが、CSVファイルには以下の識別子の**いずれか1つ**にマッピングできるユーザー識別子を含める必要があります。各識別子の詳細については、[識別子を選択する](#choose-an-identifier)を参照してください。

- `external_id`
- `braze_id`
- `user_alias_name` **と** `user_alias_label`
- `email`
- `phone`

#### カスタム属性 {#custom-attributes}

CSVインポートでは、以下のデータタイプをカスタム属性として使用できます。[デフォルト属性](#default-attributes)と完全に一致しない列ヘッダーは、マッピングステップで変更しない限り、Brazeにカスタム属性としてインポートされます。

| データタイプ | 説明 |
|---|---|
| Datetime | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式で保存する必要があります。 |
| Boolean | `true`または`false`を受け付けます。 |
| Number | スペースやカンマのない整数または浮動小数点数である必要があります。浮動小数点数はピリオド（`.`）を小数点区切りとして使用する必要があります。 |
| String | 値が二重引用符（`""`）で囲まれている場合、カンマを含めることができます。 |
| 空白 | 空白の値はユーザープロファイルの既存の値を上書きしません。CSVファイルに既存のすべてのユーザー属性を含める必要はありません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタム属性" }

{% alert important %}
配列、プッシュトークン、カスタムイベントのデータタイプはユーザーインポートではサポートされていません。CSVファイル内のカンマが列区切りとして解釈され、ファイルの解析中にエラーが発生するためです。<br><br>これらの種類の値をアップロードするには、代わりに[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用してください。
{% endalert %}

#### デフォルト属性 {#default-attributes}

{% alert important %}
デフォルト属性をインポートする際、使用する列ヘッダーはデフォルトのユーザー属性のスペルと大文字小文字が完全に一致する必要があります。一致しない場合、Brazeはこれらを代わりに[カスタム属性](#custom-attributes)として検出します。
{% endalert %}

{% alert tip %}
Brazeが認識する標準属性の完全なリスト（SDK、API、CSV、Cloud Data Ingestion全体）については、[標準属性]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes)を参照してください。以下のテーブルは、CSVインポートで設定できるサブセットのみを示しています。
{% endalert %}

ユーザーインポートでは、以下のデフォルト属性が利用可能です。

| ユーザープロファイルフィールド | データタイプ | 説明 | 必須？ |
| :---- | :---- | :---- | :---- |
| `external_id` | String | 顧客の一意のユーザー識別子。 | 条件付き。[必須の識別子](#required-identifiers-attributes)を参照してください。 |
| `user_alias_name` | String | `external_id`の代替となる匿名ユーザー用の一意のユーザー識別子。`user_alias_label`と一緒に使用する必要があります。 | 条件付き。[必須の識別子](#required-identifiers-attributes)を参照してください。 |
| `user_alias_label` | String | ユーザーエイリアスをグループ化するための共通ラベル。`user_alias_name`と一緒に使用する必要があります。 | 条件付き。[必須の識別子](#required-identifiers-attributes)を参照してください。 |
| `first_name` | String | ユーザーが示した名（例：`Jane`）。 | いいえ |
| `last_name` | String | ユーザーが示した姓（例：`Doe`）。 | いいえ |
| `email` | String | ユーザーが示したメールアドレス（例：`jane.doe@example.com`）。 | いいえ |
| `country` | String | 国コードはISO-3166-1 alpha-2標準でBrazeに渡す必要があります（例：`GB`）。 | いいえ |
| `dob` | String | "YYYY-MM-DD"形式で渡す必要があります（例：`1980-12-21`）。ユーザーの生年月日をインポートし、「今日」が誕生日のユーザーをターゲットにできます。 | いいえ |
| `gender` | String | "M"、"F"、"O"（その他）、"N"（該当なし）、"P"（回答しない）、またはnil（不明）。 | いいえ |
| `home_city` | String | ユーザーが示した居住都市（例：`London`）。 | いいえ |
| `language` | String | 言語はISO-639-1標準でBrazeに渡す必要があります（例：`en`）。[対応言語リスト]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes)を参照してください。 | いいえ |
| `phone` | String | ユーザーが示した電話番号。`E.164`形式（例：`+442071838750`）。フォーマットのガイダンスについては、[ユーザー電話番号]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)を参照してください。 | いいえ |
| `email_open_tracking_disabled` | Boolean | trueまたはfalseを受け付けます。trueに設定すると、このユーザーに送信される今後のすべてのメールに開封トラッキングピクセルが追加されなくなります。 | いいえ |
| `email_click_tracking_disabled` | Boolean | trueまたはfalseを受け付けます。trueに設定すると、このユーザーに送信される今後のメール内のすべてのリンクのクリックトラッキングが無効になります。 | いいえ |
| `email_subscribe` | String | 利用可能な値は`opted_in`（メールメッセージの受信を明示的に登録）、`unsubscribed`（メールメッセージの受信を明示的にオプトアウト）、`subscribed`（オプトインもオプトアウトもしていない）です。 | いいえ |
| `push_subscribe` | String | 利用可能な値は`opted_in`（プッシュメッセージの受信を明示的に登録）、`unsubscribed`（プッシュメッセージの受信を明示的にオプトアウト）、`subscribed`（オプトインもオプトアウトもしていない）です。 | いいえ |
| `time_zone` | String | タイムゾーンはIANAタイムゾーンデータベースと同じ形式でBrazeに渡す必要があります（例：`America/New_York`または`Eastern Time (US & Canada)`）。 | いいえ |
| `date_of_first_session`  `date_of_last_session` | String | 以下のISO 8601形式のいずれかで渡すことができます："YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS"（例：2019-11-20T18:38:57） | いいえ |
| `subscription_group_id` | String | 購読グループの`id`。この識別子はダッシュボードの購読グループページで確認できます。 | いいえ |
| `subscription_state` | String | `subscription_group_id`で指定された購読グループの購読ステータス。許可される値は`unsubscribed`（購読グループに含まれない）または`subscribed`（購読グループに含まれる）です。 | いいえ。ただし`subscription_group_id`を使用する場合は強く推奨されます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="デフォルト属性" }

#### 購読グループステータスの更新（任意） {#updating-subscription-group-status-optional}

さらに、ユーザーインポートを通じてメールまたはSMSの購読グループにユーザーを追加できます。これはSMSの場合に特に便利です。SMSチャネルでメッセージを送信するには、ユーザーがSMS購読グループに登録されている必要があるためです。詳細については、[SMS購読グループ]({{site.baseurl}}/sms_rcs_subscription_groups#subscription-group-mms-enablement)を参照してください。

購読グループのステータスを更新する場合、CSVに以下の2つの列が必要です。

- `subscription_group_id`：[購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)の`id`。
- `subscription_state`：利用可能な値は`unsubscribed`（購読グループに含まれない）または`subscribed`（購読グループに含まれる）です。

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="購読グループステータスの更新（任意）" }

{% alert note %}
ユーザーインポートでは、1行につき1つの`subscription_group_id`のみ設定できます。異なる行に異なる`subscription_group_id`の値を設定できます。ただし、同じユーザーを複数の購読グループに登録する必要がある場合は、複数回のインポートを行う必要があります。
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab カスタムイベント %}
#### 必須の識別子 {#required-identifiers-custom-events}

`external_id`は必須ではありませんが、CSVファイルには以下の識別子の**いずれか1つ**にマッピングできるユーザー識別子を含める必要があります。各識別子の詳細については、[識別子を選択する](#choose-an-identifier)を参照してください。

- `external_id`
- `braze_id`
- `user_alias_name` **と** `user_alias_label`
- `email`
- `phone`

#### カスタムイベントフィールド {#custom-event-fields}

以下のテーブルに記載されている標準フィールドに加えて、CSVにはイベントプロパティ用の追加列ヘッダーを含めることもできます。これらのプロパティの列ヘッダーは`<event_name>.properties.<property name>`または`<property name>`の形式にする必要があります。

たとえば、カスタムイベント`trip_booked`にプロパティ`destination`と`duration`がある場合、列ヘッダー`trip_booked.properties.destination`と`trip_booked.properties.duration`を使用してインポートできます。また、ヘッダーを`<property name>`として表すこともできます。Brazeは、対応するCSVセルに値があるかどうかに基づいて、各イベントの関連プロパティを検出します。

| ユーザープロファイルフィールド | データタイプ | 説明 | 必須？ |
| :---- | :---- | :---- | :---- |
| `external_id` | String | ユーザーの一意のユーザー識別子。 | 条件付き。[必須の識別子](#required-identifiers-custom-events)を参照してください。 |
| `braze_id` | String | ユーザーにBrazeが割り当てた識別子。 | 条件付き。[必須の識別子](#required-identifiers-custom-events)を参照してください。 |
| `user_alias_name` | String | `external_id`の代替となる匿名ユーザー用の一意のユーザー識別子。`user_alias_label`と一緒に使用する必要があります。 | 条件付き。[必須の識別子](#required-identifiers-custom-events)を参照してください。 |
| `user_alias_label` | String | ユーザーエイリアスをグループ化するための共通ラベル。`user_alias_name`と一緒に使用する必要があります。 | 条件付き。[必須の識別子](#required-identifiers-custom-events)を参照してください。 |
| `email` | String | ユーザーが示したメールアドレス（例：`jane.doe@example.com`）。 | いいえ。他の識別子がない場合にのみ使用できます。以下の注記を参照してください。 |
| `phone` | String | ユーザーが示した電話番号。`E.164`形式（例：`+442071838750`）。フォーマットのガイダンスについては、[ユーザー電話番号]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)を参照してください。 | いいえ。他の識別子がない場合にのみ使用できます。以下の注記を参照してください。 |
| `name` | String | ユーザーのカスタムイベント。 | はい |
| `time` | String | イベントの時刻。以下のISO-8601形式のいずれかで渡すことができます："YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS"（例：2019-11-20T18:38:57） | はい |
| `<event name>.properties.<property name>` | 複数 | カスタムイベントに関連付けられたイベントプロパティ。例：`trip_booked.properties.destination` | いいえ |
| `<property name>` | 複数 | 複数のイベントタイプで使用できるイベントプロパティ。例：`destination`。対応するCSVセルにnullでない値がある場合、このプロパティはイベントに関連付けられます。 | いいえ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムイベントフィールド" }

#### カスタムイベントのフォーマット要件 {#format-requirements-for-custom-events}

CSVを使用してカスタムイベントをインポートする場合、データのインポートを成功させるために以下の要件に従ってファイルをフォーマットする必要があります。

##### カスタムイベントのフォーマットについて {#understanding-custom-event-formatting}

ドット表記を使用するか、対応するセルにnullでない値を入力して、Brazeが各プロパティを最終イベントにマッピングできるようにCSVを正しくフォーマットしてください。フォーマットが正しくない場合、プロパティが失われたり、特に1つのファイルに複数のイベントタイプが含まれている場合にインポートが失敗する可能性があります。

##### イベントプロパティにドット表記を使用する {#use-dot-notation-for-event-properties}

ドット表記を使用して、カスタムイベントとそのプロパティの間の階層関係を定義します。このフォーマット規則により、各イベントの特定の属性を含む構造化されたイベントデータをインポートできます。

ドット表記の形式は次の構造に従います：`event_name.properties.property_name`

ドット表記は以下の順序で機能します：

1. 最初にイベント名
2. 次に`.properties.`で、その後に続くものがイベントプロパティであることを示す
3. 最後に、特定のプロパティ名

**例：**

`rented_movie`というカスタムイベントにプロパティ`movie_name`と`genre`がある場合、CSVの列ヘッダーは次のようになります。

- `rented_movie.properties.movie_name`
- `rented_movie.properties.genre`

この表記は、Brazeに`rented_movie`というカスタムイベントを作成し、その特定のイベントインスタンスにプロパティ`movie_name`と`genre`を付与するよう指示します。

ドット表記と非ドット表記を組み合わせてプロパティをインポートすると、Brazeが重複したヘッダーを検出するため、CSVのアップロードが失敗する場合があります。これは、同じファイル内に`rented_movie.properties.movie_name`と`movie_name`のヘッダーがある場合に発生します。これを避けるには、ヘッダーのプロパティには1つの形式のみを使用してください。

##### 1行につき1つのイベント {#one-event-per-row}

CSVの各行は、1人のユーザーの1つのカスタムイベントを表します。ユーザーに複数のイベントがある場合、同じユーザー識別子を共有していても、各イベントに別の行を含める必要があります。

{% alert important %}
行に特定のイベントのデータが含まれている場合、そのイベントのプロパティの列のみにデータを入力してください。他のイベントの列は空白のままにしてください。
{% endalert %}

##### CSVの構造例 {#example-csv-structure}

以下のテーブルは、プロパティを持つカスタムイベントをインポートするための正しいフォーマットを示しています。この例では、それぞれ異なるイベントを実行した2人のユーザーを示しています。1人は映画をレンタルし、もう1人は映画を購入しました。

| external_id | name | time | rented_movie.properties.movie_name | rented_movie.properties.genre | bought_movie.properties.movie_name | bought_movie.properties.genre |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 123 | rented_movie | 2024-06-10T12:00:00Z | Ghostbusters | Action | | |
| 456 | bought_movie | 2024-06-12T12:00:00Z | | | Ghostbusters | Action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="CSVの構造例" }

この例では：

- ユーザー`123`は、プロパティ`movie_name`（Ghostbusters）と`genre`（Action）を持つ`rented_movie`イベントをトリガーしました
- ユーザー`456`は、プロパティ`movie_name`（Ghostbusters）と`genre`（Action）を持つ`bought_movie`イベントをトリガーしました
- 各イベントは関連するプロパティ列のみにデータを入力し、他のイベントのプロパティ列は空白のままにしています

{% endtab %}
{% endtabs %}

### ステップ4：ファイルをアップロードする {#step-4-upload-your-file}

ファイルをアップロードするには、**属性**または**イベント**を選択し、**ファイルを参照**をクリックして、CSVをアップロードします。Brazeは最初の数行のプレビューと検出されたフィールドの概要を表示します。

大きなファイル（デフォルト属性とカスタム属性は最大500 MB、カスタムイベントは最大50 MB）の場合、ファイルのアップロードとBrazeのインポート計算中にダッシュボードが一時的に応答しなくなることがあります。これらのアップロードと計算は、小さなファイルよりも完了に時間がかかることがあります。このステップが完了するまでお待ちください。ファイルの制限とタイミングの詳細については、[CSVの構築]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)を参照してください。

CSVファイルをアップロードする前に、Brazeで表示したいインポート名にファイル名を変更してください。アップロード後にインポート名を編集することはできません。

{% alert note %}
ファイルプレビューにはファイルの最初の数行のみが表示されます。インポート前にすべての行を確認するには、[ファイルバリデーション](#file-validation)を使用してください。
{% endalert %}

{% alert important %}
CSVユーザーインポートは、アップロード後14日間ダッシュボードからダウンロードできます。この期間を過ぎると、ファイルはストレージから削除され、アクセスできなくなります。
{% endalert %}

### ステップ5：フィールドをマッピングする {#csv-data-mapping}

プレビュー後、CSVのヘッダーをBrazeの属性、イベント、またはイベントプロパティにマッピングできます。BrazeはCSVファイル内のフィールドを同じ名前の属性、イベント、またはイベントプロパティに自動的にマッピングし、必要に応じて新しいフィールドを作成します。また、提案を手動で調整したり、別の属性、イベント、またはプロパティを選択する柔軟性もあります。

イベントプロパティについては、CSVセルにnullでない値が含まれているかどうか、または`<event name>.properties.<property name>`形式のドット表記を使用するヘッダーに基づいて、Brazeがプロパティを検出し、関連するイベントに関連付けます。

![列マッピングページ。]({% image_buster /assets/img/csv_import/column_mapping_mapped.png %})

#### マッピングステータス {#mapping-statuses}

マッピングステータス列は、CSVファイルがインポートされた際に実行されるアクションを示し、以下のいずれかになります。

| マッピングステータス | 意味 |
|:---|:---|
| **マッピング済み** | フィールドが既存の属性、イベント、または識別子にマッピングされています。 |
| **新規属性**、**新規イベント**、または**新規イベントプロパティ** | Brazeがインポート時に新しい属性またはイベントを作成します。**新規属性を編集**、**新規イベントを編集**、または**新規プロパティを編集**ボタンを選択して編集できます。 |
| **データタイプの不一致** | CSV列の検出されたデータタイプが既存の属性、イベント、または識別子のデータタイプと一致しません。Brazeはインポート時にデータタイプを既存の属性に一致するよう変換を試みます。変換できない場合、Brazeはその値を削除します。 |
| **ブロックリスト属性**または**ブロックリストイベント** | CSVフィールドがブロックリストに登録された属性またはイベントの名前と一致しています。マッピングする別の属性またはイベントを選択してください。選択しない場合、インポートされません。 |
| **重複属性** | CSVファイルに同じ名前のフィールドが1つ以上あります。同名の列を異なる属性にマッピングしてください。マッピングしない場合、最初の列のみがインポートされます。 |
| **予約イベントキー** | イベントプロパティの名前がBrazeの予約イベントキー（`time`や`event_name`など）と一致しています。別の名前を入力するか、マッピングする別のプロパティを選択してください。選択しない場合、その値は削除されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="マッピングステータス" }


#### 新しい属性、イベント、プロパティの編集 {#editing-new-attributes-events-and-properties}

ワークスペースに一致する属性、イベント、またはイベントプロパティが存在しない場合、BrazeはCSVフィールドの名前と検出されたデータタイプを使用して、インポート時に新しい属性、イベント、またはプロパティの作成を試みます。マッピングステータスの横にある**新規属性を編集**、**新規イベントを編集**、または**新規プロパティを編集**ボタンを選択することで、インポート前にこの新しいフィールドを編集できます。

![列マッピングページの「新規属性を編集」ボタン。]({% image_buster /assets/img/csv_import/column_mapping_edit_attribute_button.png %})


{% alert note %}
識別子がマッピングされるまで、マッピングステップを先に進めることはできません。Brazeは可能な場合、識別子を自動的にマッピングします。カスタムイベントの場合、`name`と`time`の列もマッピングする必要があります。詳細については、**必須フィールド**のセクションを参照してください。
{% endalert %}

### ステップ6：ターゲティング設定を選択する {#targeting-preferences}

マッピング後、インポート設定ページで以下のターゲティング設定から選択できます。インポートから新しいターゲティングフィルターやセグメントを作成する必要がない場合は、**このリストをターゲティングフィルターとして利用可能にしない**を選択してください。

| オプション | 説明 |
|---|---|
| ターゲティングフィルター | CSVファイルをユーザーセグメント構築時のリターゲティングオプションに変換するには、**CSV からの更新/インポート**ドロップダウンからファイルを選択し、**ターゲティングフィルターを作成**を選択します。 |
| 新しいセグメント | 新しいターゲティングフィルターから新しいセグメントも作成するには、**ターゲティングフィルターを作成し、新しいセグメントに追加**を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ6：ターゲティング設定を選択する" }

![「CSVからの更新/インポート」フィルターを含むフィルターグループ。「Halloween season fun」というタイトルのCSVファイルが含まれています。]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### ステップ7：ファイルを検証する（任意） {#file-validation}

インポートを開始する前に、ファイルバリデーションを実行してすべての行のエラーや警告を確認できます。ファイルを検証するには、インポート設定ページで**インポート前にファイルを検証**を選択し、**次へ**を選択します。

バリデーションは、最大許容サイズのファイルで最大2分かかることがあります。バリデーション実行中に、**バリデーションをスキップ**を選択してバイパスし、すぐに進むこともできます。

#### バリデーション結果 {#validation-results}

バリデーションが完了すると、以下のいずれかの結果が表示されます。

| 結果 | 意味 | 次のステップ |
|---|---|---|
| **バリデーション完了** | 問題は見つかりませんでした。 | **データをインポート**を選択します。 |
| **問題が見つかりました** | 一部の行にエラーまたは警告があります。 | エラーレポートをダウンロードして確認し、**インポートを続行**を選択して進むか、**キャンセル**を選択してファイルを先に修正します。 |
| **バリデーションがタイムアウトしました** | バリデーションが時間切れになりました。チェックされた行には問題はありませんでした。 | **データをインポート**を選択します。完全なレポートが数分後に利用可能になります。 |
| **問題が見つかった状態でバリデーションがタイムアウトしました** | バリデーションが時間切れになり、チェックした行の一部にエラーが見つかりました。 | 部分レポートをダウンロードして発見された内容を確認し、**インポートを続行**または**キャンセル**を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="バリデーション結果" }

![問題が見つかったセクションを示すサマリーページ。エラーと警告のある行数のカウントと、戻る、エラーレポートのダウンロード、インポートの開始のオプションが表示されています。]({% image_buster /assets/img/csv_import/summary_page_validation_results.png %})

#### エラーレポートについて {#understanding-the-error-report}

エラーレポートは、フラグが付けられたすべての行と元のデータおよび問題の説明を含むCSVファイルです。

| 問題タイプ | 説明 |
|---|---|
| **エラー** | インポート中にその行は完全にスキップされます。 |
| **警告** | その行はインポートされますが、一部の値が削除されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エラーレポートについて" }

レポートを確認した後、元のファイルで問題を修正して再アップロードするか、インポートを続行して部分的な結果を受け入れることができます。



### ステップ8：CSVインポートを開始する {#step-8-start-your-csv-import}

準備ができたら、**インポートを開始**を選択します。**ユーザーをインポート**ページで現在の進捗状況を追跡できます。このページは5秒ごとに自動的に更新されます。
処理はCSVのサイズに応じて、数分から数時間かかることがあります。この間、ダッシュボードが応答しなくなったり、反応が遅くなったりすることがありますが、インポートは引き続き実行されています。

{% alert note %}
複数のCSVを同時にインポートできます。CSVインポートは同時に実行されるため、更新の順序がシリアルであることは保証されません。CSVインポートを順番に実行する必要がある場合は、CSVインポートが完了してから次のCSVをアップロードしてください。
{% endalert %}

#### インポートステータス {#import-statuses}

インポートを開始した後、**ユーザーをインポート**ページでステータスを確認できます。

| ステータス | 説明 |
|---|---|
| **完了** | すべての行が正常にインポートされました。 |
| **部分的に成功** | 一部の行が失敗しました。インポートの横にある三点メニューを選択して、エラーレポートまたは元のアップロードCSVをダウンロードします。 |
| **処理中** | インポートが現在実行中です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="インポートステータス" }

![「部分的に成功」のステータスが表示されたユーザーのインポートページ。コンテキストメニューが開いており、「エラーレポートをダウンロード」と「アップロード済みCSVをダウンロード」のオプションが表示されています。]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

インポート後のエラーレポートには、Brazeにユーザーが存在しない場合など、バリデーションではカバーされない理由で失敗した行が含まれています。

{% alert important %}
以前にアップロードされたCSVファイルは、アップロード日から14日間**ユーザーをインポート**ページからダウンロードできます。14日後、ファイルは完全に削除され、アクセスできなくなります。
{% endalert %}

## データポイントに関する注意事項 {#data-point-considerations}

CSVファイルからインポートされた顧客データは、ユーザープロファイル上の既存の値を上書きし、データポイントとして記録されます。ただし、external IDと空白の値は例外です。Brazeのデータポイントの詳細についてご不明な点がある場合は、Brazeのアカウントマネージャーにお問い合わせください。

| 注意事項 | 詳細 |
|---|---|
| External ID | `external_id` のみを含むCSVをアップロードしても、データポイントは記録されません。これにより、データ制限に影響を与えることなく既存のBrazeユーザーをセグメント化できます。ただし、`email` や `phone` などのフィールドを含めると、既存のユーザーデータが上書きされ、データポイントが記録**されます**。<br><br>`external_id`、`braze_id`、または `user_alias_name` のみを含むCSVインポートなど、セグメンテーションのみに使用されるCSVインポートではデータポイントは記録されません。 |
| 空白の値 | CSV内の空白の値は、既存のユーザープロファイルデータを上書きしません。インポート時にすべてのユーザー属性やカスタムイベントを含める必要はありません。 |
| 購読ステータス | `email_subscribe`、`push_subscribe`、`subscription_group_id`、または `subscription_state` の更新は、データポイント使用量としてカウント**されません**。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="データポイントに関する注意事項" }

{% alert important %}
CSVインポートまたはAPIを通じてユーザーの `language` や `country` を設定すると、BrazeがSDKを通じてこの情報を自動的に取得できなくなります。
{% endalert %}

## トラブルシューティング {#troubleshooting}

[ファイルバリデーション](#file-validation)を使用した場合は、エラーレポートから確認してください。フラグが付けられた各行の具体的な問題と修正方法の説明が含まれています。バリデーションではなくインポート中に失敗した行については、**Import Users** ページで行にカーソルを合わせ、<i class="fas fa-download" title="ダウンロード"></i> ボタンを選択してエラーレポートをダウンロードしてください。

CSVインポートのトラブルシューティングについては、以下のセクションで一般的な問題を確認してください。

### CSVインポートが「Calculating」のまま停止する {#csv-import-stuck-on-calculating}

**Import Users** で `Calculating` と表示されている場合、Brazeがまだファイルの処理準備を行っていることを意味します。このステップでは、準備が完了するまで行数が `0 / Calculating` と表示されることがあります。

インポートが「Calculating」のまま停止しているように見える場合は、以下を確認してください：

- インポートを続行させてください。Brazeサポートから指示がない限り、キャンセルして再アップロードしないでください。
- [CSVの構成]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#import-options)で、ファイルがサポートされている制限内であることを確認してください。
- [ステップ4：ファイルをアップロードする](#step-4-upload-your-file)および[ステップ8：CSVインポートを開始する](#step-8-start-your-csv-import)で、ダッシュボードの想定される動作と処理時間を確認してください。
- 上記を確認した上で、ファイルサイズに対して`Calculating`が予想以上に長く続く場合は、Brazeサポートに連絡してください。

### メールアドレスを`external_id`として使用する {#use-email-as-external_id}

Brazeでは、メールアドレスを`external_id`として使用することは推奨していません。メールアドレスを`external_id`として使用する場合は、ユーザーがメールチャネルでターゲット可能な状態を維持するために、CSVに`external_id`列と`email`列の両方を含めてください。列の区切り文字にはコンマ（`,`）を使用し、コロン（`:`）は使用しないでください。

### `external_id`値の引用符文字 {#quote-characters-in-external_id-values}

`external_id`セルにダブルクォーテーションマークが含まれている場合は、[エスケープされていない、またはバランスが取れていないダブルクォーテーションマーク](#missing-row)に記載されているように、文字を二重にする（`""`）ことでエスケープしてください。CSVインポートではバックスラッシュによるエスケープは使用しません。

### CSVインポートがセグメントフィルターとして利用できない {#csv-import-isnt-available-as-a-segment-filter}

CSVインポートをセグメントフィルターとして使用できるのは、アップロード時にターゲティング設定を有効にした場合のみです。

既存のインポートに対してターゲティングの利用可否が有効かどうかを確認するには：

1. **Import Users** ページでCSVインポートを見つけます。
2. そのインポートに対して**Go to セグメント** が表示されているか確認します。
3. **Go to セグメント** が表示されている場合、CSVは`Updated/Imported from CSV`セグメントフィルターで利用可能です。
4. **Go to セグメント** が表示されていない場合、そのインポートではターゲティングの利用可否が有効になっていません。

CSVのアップロード完了後にターゲティングの利用可否を有効にすることはできません。そのCSVをセグメントフィルターとして使用するには、ファイルを再アップロードし、[ステップ6：ターゲティング設定を選択する](#step-6-choose-targeting-preferences)で**Create targeting filter**または**Create targeting filter and add to new segment**を選択してください。

プロファイルデータを更新せずにセグメントを作成することが目的の場合は、識別子列のみ（例：`external_id`またはエイリアス識別子列）を含むCSVをアップロードし、**Create targeting filter and add to new segment**を選択してください。

### ファイルフォーマットの問題 {#file-formatting-issues}

#### 不正な行 {#malformed-row}

アップロードがエラーで完了した場合、CSVファイルに不正な行が含まれている可能性があります。

データを正しくインポートするには、ヘッダー行が必要です。各行はヘッダー行と同じ数のセルを持つ必要があります。ヘッダー行より多いまたは少ない値を持つ行は、インポートから除外されます。値内のコンマは区切り文字として解釈され、このエラーの原因となることがあります。

また、すべてのデータはUTF-8でエンコードされている必要があります。ファイルがレガシーエンコーディング（例：一部のExcelのデフォルト設定）で保存されている場合、セル内の特殊文字やURLが破損し、Brazeや送信されたメッセージ内で疑問符（`?`）として表示されることがあります。

CSVファイルに空白行があり、CSVファイルの総行数よりも少ない行がインポートされた場合、空白行はインポートする必要がないため、インポートに問題があるとは限りません。正しくインポートされた行数を確認し、インポートしようとしているユーザー数と一致するか確認してください。

#### 欠落した行 {#missing-row}

インポートされたユーザー数がCSVファイルの総行数と一致しない理由はいくつかあります：

| 問題 | 解決方法 |
|---|---|
| external ID、ユーザーエイリアス、Braze ID、メールアドレス、または電話番号の重複 | external IDの列に重複がある場合、行が正しくフォーマットされていても、不正な行やインポートされない行が発生する可能性があります。場合によっては、特定のエラーが報告されないこともあります。再アップロードする前に重複を確認し、削除してください。 |
| アクセント付き文字 | CSVにアクセント付きの名前や属性が含まれている場合があります。インポートの問題を防ぐために、ファイルがUTF-8でエンコードされていることを確認してください。 |
| Braze IDが孤立したユーザーに属している | ユーザーが別のユーザーにマージされ、BrazeがそのBraze IDを残りのプロファイルに関連付けられない場合、その行はインポートされません。 |
| 空の行 | CSV内の空白行は不正なデータエラーの原因となる可能性があります。ExcelやSheetsではなく、プレーンテキストエディタで確認してください。 |
| エスケープされていない、またはバランスが取れていないダブルクォーテーションマーク（`"`） | ダブルクォーテーションマークは、コンマを含む文字列値を囲みます。値自体にダブルクォーテーションマークが含まれている場合は、二重にする（`""`）ことでエスケープしてください。エスケープされていない、またはバランスが取れていないダブルクォーテーションマークは、不正な行の原因となります。 |
| 不整合な改行 | 改行の混在（例：`\n`と`\r\n`）により、データの最初の行がヘッダーの一部として扱われる場合があります。16進エディタまたは高度なテキストエディタを使用して確認し、修正してください。 |
| 誤ったエンコーディングのファイル | アクセントが許可されていても、ファイルはUTF-8でエンコードされている必要があります。他のエンコーディングは部分的に動作する可能性がありますが、完全にはサポートされていません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="欠落した行" }

#### 文字列のクォーテーション {#string-quotation}

シングルクォート（`''`）またはダブルクォート（`""`）で囲まれた値は、インポート時に文字列として読み取られます。

#### 不正なフォーマットの日付 {#incorrectly-formatted-dates}

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式でない日付は、インポート時に`datetimes`として読み取られません。

### データ構造の問題 {#data-structure-issues}

#### 無効なメールアドレス {#invalid-email-addresses}

アップロードがエラーで完了した場合、1つ以上の無効な暗号化メールアドレスがある可能性があります。Brazeにインポートする前に、すべてのメールアドレスが正しく暗号化されていることを確認してください。

- **Brazeで[メールアドレスを更新またはインポートする]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption#step-3-import-and-update-users)場合**、メールが含まれるすべての箇所でハッシュ化されたメール値を使用してください。これらのハッシュメール値は、社内チームによって提供されます。
- **新しいユーザーを作成する場合**、ユーザーの暗号化されたメール値を含む`email_encrypted`を追加する必要があります。そうしないと、Brazeはユーザーを作成しません。同様に、メールアドレスを持たない既存のユーザーにメールアドレスを追加する場合も、`email_encrypted`を追加する必要があります。そうしないと、Brazeはユーザーを更新しません。

#### データがカスタム属性としてインポートされた {#data-imported-as-custom-attribute}

デフォルトのユーザーデータ（`email`や`first_name`など）がカスタム属性としてインポートされた場合は、CSVファイルの大文字と小文字の区別およびスペースを確認してください。例えば、`First_name`はカスタム属性としてインポートされますが、`first_name`はユーザーのプロファイルの「名」フィールドに正しくインポートされます。

#### カスタム属性のデータ型を変更する {#change-a-custom-attributes-data-type}

既存のカスタム属性のデータ型を変更する必要がある場合（例：文字列からブーリアンへ）、CSVをインポートする前にダッシュボードの[**カスタム属性**]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data)ページでデータ型を更新してください。CSV内のデータ型が属性の現在定義されているデータ型と一致しない場合、インポートはエラーで失敗します。

#### 複数のデータ型 {#multiple-data-types}

Brazeでは、列内の各値が同じデータ型であることが期待されます。属性のデータ型と一致しない値は、セグメンテーションでエラーを引き起こします。

また、数値属性をゼロで始めると問題が発生します。ゼロで始まる数値は文字列として扱われるためです。Brazeがその文字列を変換する際、8進数値（0から7の数字を使用する）として扱われる場合があり、対応する10進数値に変換されます。例えば、CSVファイルの値が0130の場合、Brazeプロファイルには88と表示されます。この問題を防ぐには、文字列データ型の属性を使用してください。ただし、このデータ型はセグメンテーションの数値比較では使用できません。

#### デフォルト属性の型 {#default-attribute-types}

一部のデフォルト属性は、ユーザー更新に対して有効な値として特定の値のみを受け付ける場合があります。ガイダンスについては、[CSVの構成]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)を参照してください。

末尾のスペースや大文字と小文字の違いにより、値が無効として解釈される場合があります。例えば、以下のCSVファイルでは、受け付けられる値は`unsubscribed`、`subscribed`、`opted_in`であるため、最初の行のユーザー（`brazetest1`）のみがメールとプッシュのステータスを正常に更新されます。

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@example.com,unsubscribed,unsubscribed
brazetest2,test2@example.com,Unsubscribed,Unsubscribed
```

### 「Select CSV File」が動作しない {#select-csv-file-is-not-working}

**Select CSV File** ボタンが動作しない理由はいくつかあります：

| 問題 | 解決方法 |
|---|---|
| ポップアップブロッカー | ページの表示が妨げられている可能性があります。ブラウザがBrazeダッシュボードのWebサイトでポップアップを許可していることを確認してください。 |
| 古いブラウザ | ブラウザが最新であることを確認し、最新でない場合は最新バージョンに更新してください。 |
| バックグラウンドプロセス | すべてのブラウザインスタンスを閉じてから、コンピューターを再起動してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="「Select CSV File」が動作しない" }