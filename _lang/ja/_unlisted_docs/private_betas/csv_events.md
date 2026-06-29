---
nav_title: ユーザーデータとCSVイベントのインポート
article_title: ユーザーデータとCSVイベントのインポート
permalink: "/csv_events/"
description: "このリファレンス記事では、ユーザーデータのインポート方法と、CSVファイルを使用したカスタムイベントのインポート方法について説明します。"
page_type: reference
---

# ユーザーデータのインポート（CSVイベント早期アクセス） {#importing-user-data-csv-events-early-access}

> Brazeは、プラットフォームにユーザーデータをインポートするためのさまざまな方法を提供しています。SDK、API、クラウドデータ取り込み、テクノロジーパートナー連携、CSVファイルなどです。この記事では、[CSVファイルによるカスタムイベントのインポート（早期アクセス）](#importing-custom-events)を含む、ユーザーデータのインポートに関する詳細な手順を説明します。

{% multi_lang_include channels/sms/email_via_sms_warning.md %}

先に進む前に、Brazeはインポート時にHTMLデータのサニタイズ（検証や適切なフォーマット）を行わないことに注意してください。つまり、Webパーソナライゼーション用のすべてのインポートデータからスクリプトタグを除去する必要があります。

## REST API

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、ユーザーのカスタムイベント、ユーザー属性、購入を記録できます。

## CSVインポート {#csv-import}

**オーディエンス** > **ユーザーをインポートする**から、CSVファイルを使用してユーザープロファイルをアップロードおよび更新できます。

CSVファイルを使用したユーザーデータのインポートでは、名やメールなどのユーザー属性に加え、靴のサイズなどのカスタム属性の記録と更新がサポートされています。CSVをインポートするには、2つのユニークなユーザー識別子のいずれかを指定します：`external_id`またはユーザーエイリアスです。

{% alert important %}
ユーザーインポートでは、ユーザーカスタムイベントの記録と更新もサポートされています。ユーザー属性と同様に、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`を使用してインポートできます。詳細については、[カスタムイベントのインポート](#importing-custom-events)を参照してください。
{% endalert %}

{% alert note %}
`external_id`を持つユーザーと持たないユーザーが混在している場合は、インポートごとに1つのCSVファイルを作成する必要があります。1つのCSVファイルに`external_ids`とユーザーエイリアスの両方を含めることはできません。
{% endalert %}

### external IDを使用したインポート {#importing-with-external-id}

顧客データをインポートする際には、各顧客のユニーク識別子（`external_id`とも呼ばれます）を指定する必要があります。CSVインポートを開始する前に、Brazeでユーザーがどのように識別されるかをエンジニアリングチームに確認することが重要です。通常、これは内部データベースIDです。これは、モバイルおよびWebでBraze SDKによってユーザーが識別される方法と一致する必要があり、各顧客がデバイス間でBraze内に単一のユーザープロファイルを持つように設計されています。Brazeの[ユーザープロファイルライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle)の詳細をご覧ください。

インポートで`external_id`を指定すると、Brazeは同じ`external_id`を持つ既存のユーザーを更新するか、見つからない場合はその`external_id`が設定された新しい識別済みユーザーを作成します。

- **ダウンロード：** [CSV属性インポートテンプレート][import_template]
- **ダウンロード：** [CSVイベントインポートテンプレート][events_template]

### ユーザーエイリアスを使用したインポート {#importing-with-user-alias}

`external_id`を持たないユーザーをターゲットにするには、ユーザーエイリアスを使用してユーザーのリストをインポートできます。エイリアスは代替のユニークユーザー識別子として機能し、サインアップやアプリでのアカウント作成を行っていない匿名ユーザーにマーケティングを行う場合に役立ちます。

エイリアスのみのユーザープロファイルをアップロードまたは更新する場合は、CSVに次の2つの列が必要です：

- `user_alias_name`：ユニークなユーザー識別子。`external_id`の代替です
- `user_alias_label`：ユーザーエイリアスをグループ化するための共通ラベル

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

インポートで`user_alias_name`と`user_alias_label`の両方を指定すると、Brazeは同じ`user_alias_name`と`user_alias_label`を持つ既存のユーザーを更新します。ユーザーが見つからない場合、Brazeはその`user_alias_name`が設定された新しい識別済みユーザーを作成します。

{% alert important %}
既に`external_id`を持つ既存のユーザーを`user_alias_name`で更新するためにCSVインポートを使用することはできません。代わりに、関連する`user_alias_name`を持つ新しいユーザープロファイルが作成されます。エイリアスのみのユーザーを`external_id`に関連付けるには、[ユーザー識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用してください。
{% endalert %}

- **ダウンロード：** [CSVエイリアス属性インポートテンプレート][template_alias_attributes]
- **ダウンロード：** [CSVエイリアスイベントインポートテンプレート][template_alias_events]

### Braze IDを使用したインポート {#importing-with-braze-id}

`external_id`や`user_alias_name`と`user_alias_label`の値の代わりに、内部のBraze ID値を使用してBrazeの既存のユーザープロファイルを更新するには、列ヘッダーとして`braze_id`を指定します。

これは、セグメンテーション内のCSVエクスポートオプションを使用してBrazeからユーザーデータをエクスポートし、それらの既存ユーザーに新しいカスタム属性を追加したい場合に役立ちます。

{% alert important %}
`braze_id`を使用してCSVインポートで新しいユーザーを作成することはできません。この方法は、Brazeプラットフォーム内の既存のユーザーを更新する場合にのみ使用できます。
{% endalert %}

{% alert tip %}
BrazeダッシュボードからのCSVエクスポートでは、`braze_id`の値が`Appboy ID`と表示される場合があります。このIDはユーザーの`braze_id`と同じであるため、CSVを再インポートする際にこの列の名前を`braze_id`に変更できます。
{% endalert %}

### デフォルト属性のインポート {#importing-default-attributes}

ユーザーのデフォルト属性をインポートするには、**ユーザーをインポートする** > **属性**に移動します。デフォルトのユーザー属性はBrazeの予約キーです。例えば、`first_name`や`email`などです。カスタム属性はビジネスに固有のものです。例えば、旅行予約アプリには`last_destination_searched`というカスタム属性がある場合があります。

{% alert important %}
顧客データを属性としてインポートする場合、使用する列ヘッダーはデフォルトのユーザー属性のスペルと大文字小文字に正確に一致する必要があります。一致しない場合、Brazeはそのユーザーのプロファイルにカスタム属性を自動的に作成します。
{% endalert %}

#### デフォルトのユーザーデータ列ヘッダー {#default-user-data-column-headers}

| ユーザープロファイルフィールド | データタイプ | 情報 | 必須 |
|---|---|---|---|
| `external_id` | 文字列 | 顧客のユニークなユーザー識別子。 | はい、[以下の注記](#about-external-ids)を参照してください。 |
| `user_alias_name` | 文字列 | 匿名ユーザーのユニークなユーザー識別子。`external_id`の代替です。 | いいえ、[以下の注記](#about-external-ids)を参照してください。 |
| `user_alias_label` | 文字列 | ユーザーエイリアスをグループ化するための共通ラベル。 | はい、`user_alias_name`を使用する場合。 |
| `first_name` | 文字列 | ユーザーが示した名（例：`Jane`）。 | いいえ |
| `last_name` | 文字列 | ユーザーが示した姓（例：`Doe`）。 | いいえ |
| `email` | 文字列 | ユーザーが示したメールアドレス（例：`jane.doe@braze.com`）。 | いいえ |
| `country` | 文字列 | 国コードはISO-3166-1 alpha-2規格でBrazeに渡す必要があります（例：`GB`）。 | いいえ |
| `dob` | 文字列 | 「YYYY-MM-DD」の形式で渡す必要があります（例：`1980-12-21`）。これにより、ユーザーの生年月日がインポートされ、誕生日が「今日」のユーザーをターゲットにできます。 | いいえ |
| `gender` | 文字列 | 「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（回答しない）、またはnil（不明）。 | いいえ |
| `home_city` | 文字列 | ユーザーが示した居住都市（例：`London`）。 | いいえ |
| `language` | 文字列 | 言語はISO-639-1規格でBrazeに渡す必要があります（例：`en`）。<br>[対応言語一覧]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes)を参照してください。 | いいえ |
| `phone` | 文字列 | ユーザーが示した電話番号。`E.164`形式（例：`+442071838750`）。<br>フォーマットのガイダンスについては、[ユーザーの電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers)を参照してください。 | いいえ |
| `email_open_tracking_disabled` | ブール値 | trueまたはfalseを受け付けます。trueに設定すると、このユーザーに送信される今後のすべてのメールに開封トラッキングピクセルが追加されなくなります。 | いいえ |
| `email_click_tracking_disabled` | ブール値 | trueまたはfalseを受け付けます。trueに設定すると、このユーザーに送信される今後のメール内のすべてのリンクのクリックトラッキングが無効になります。 | いいえ |
| `email_subscribe` | 文字列 | 使用可能な値は`opted_in`（メールメッセージの受信を明示的に登録）、`unsubscribed`（メールメッセージを明示的にオプトアウト）、`subscribed`（オプトインもオプトアウトもしていない）です。 | いいえ |
| `push_subscribe` | 文字列 | 使用可能な値は`opted_in`（プッシュメッセージの受信を明示的に登録）、`unsubscribed`（プッシュメッセージを明示的にオプトアウト）、`subscribed`（オプトインもオプトアウトもしていない）です。 | いいえ |
| `time_zone` | 文字列 | タイムゾーンはIANAタイムゾーンデータベースと同じ形式でBrazeに渡す必要があります（例：`America/New_York`または`Eastern Time (US & Canada)`）。 | いいえ |
| `date_of_first_session` <br><br> `date_of_last_session`| 文字列 | 以下のISO-8601形式のいずれかで渡すことができます：{::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS"（例：2019-11-20T18:38:57） </li> </ul> {:/} | いいえ |
| `subscription_group_id` | 文字列 | サブスクリプショングループの`id`。この識別子はダッシュボードのサブスクリプショングループページで確認できます。 | いいえ |
| `subscription_state` | 文字列 | `subscription_group_id`で指定されたサブスクリプショングループのサブスクリプション状態。許可される値は`unsubscribed`（サブスクリプショングループに含まれない）または`subscribed`（サブスクリプショングループに含まれる）です。 | いいえ、ただし`subscription_group_id`を使用する場合は強く推奨されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### external IDについて {#about-external-ids}

`external_id`は必須ではありませんが、以下のフィールドのいずれかを含める**必要があります**：
- `external_id`：顧客のユニークなユーザー識別子、**または**
- `braze_id`：既存のBrazeユーザーに対して取得されたユニークなユーザー識別子、**または**
- `user_alias_name`と`user_alias_label`：匿名ユーザーのユニークなユーザー識別子

### カスタム属性のインポート {#importing-custom-attributes}

**ユーザーをインポートする** > **属性**に移動して、ユーザーのカスタム属性をインポートできます。デフォルト属性と正確に一致しないヘッダーは、Braze内にカスタム属性を作成します。

ユーザーインポートでは、以下のデータタイプが受け付けられます：

| データタイプ | 説明 |
|-----------|-------------|
| 日時 | ISO-8601形式で保存する必要があります |
| ブール値 | TRUEまたはFALSE |
| 数値 | スペースやカンマのない整数または浮動小数点数。浮動小数点数はピリオド（.）を小数点区切りとして使用する必要があります |
| 文字列 | 列の値を二重引用符で囲んでいる限り、カンマを含めることができます |
| 空白 | 空白の値はユーザープロファイルの既存の値を上書きしません。CSVファイルに既存のすべてのユーザー属性を含める必要はありません |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
配列とプッシュトークンはユーザーインポートではサポートされていません。特に配列の場合、CSVファイル内のカンマは列区切りとして解釈されるため、値内のカンマはファイルの解析エラーを引き起こします。<br>この種の値をアップロードするには、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion)を使用してください。
{% endalert %}

### サブスクリプショングループのステータスの更新 {#updating-subscription-group-status}

ユーザーインポートを通じて、メールまたはSMSのサブスクリプショングループにユーザーを追加できます。これはSMSの場合に特に便利です。ユーザーがSMSチャネルでメッセージを受信するには、SMSサブスクリプショングループに登録されている必要があるためです。詳細については、[SMSサブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#subscription-group-mms-enablement)を参照してください。

サブスクリプショングループのステータスを更新する場合は、CSVに次の2つの列が必要です：

- `subscription_group_id`：[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups)の`id`。
- `subscription_state`：使用可能な値は`unsubscribed`（サブスクリプショングループに含まれない）または`subscribed`（サブスクリプショングループに含まれる）です。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="サブスクリプショングループのステータスの更新">
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
ユーザーインポートでは、1行につき1つの`subscription_group_id`のみ設定できます。異なる行には異なる`subscription_group_id`の値を設定できます。ただし、同じユーザーを複数のサブスクリプショングループに登録する必要がある場合は、複数回のインポートを行う必要があります。
{% endalert %}

### カスタムイベントのインポート（早期アクセス） {#importing-custom-events}

{% alert important %}
カスタムイベントのインポートは現在早期アクセス中です。早期アクセスへの参加に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

ユーザーのカスタムイベントをインポートするには、**ユーザーをインポートする** > **イベント**に移動します。

カスタムイベントはビジネスに固有のものです。例えば、ストリーミングアプリにはrented_movieというカスタムイベントがある場合があります。CSVには以下の列ヘッダーが必要です：

- 以下のいずれか：
  - `external_id`、**または**
  - `braze_id`、**または**
  - `user_alias_name`と`user_alias_label`
- Name
- Time

カスタムイベントにはイベントプロパティを含めることができます。例えば、カスタムイベントrented_movieにはtitleやgenreというプロパティがある場合があります。これらのイベントプロパティの列ヘッダーは`<event_name>.properties.<property name>`の形式にする必要があります。例えば`rented_movie.properties.title`です。

| ユーザープロファイルフィールド | データタイプ | 情報 | 必須 |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id` | 文字列 | ユーザーのユニークなユーザー識別子。 | はい、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`のいずれかが必須です。 |
| `braze_id` | 文字列 | Brazeが割り当てたユーザーの識別子。 | はい、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`のいずれかが必須です。 |
| `user_alias_name` | 文字列 | 匿名ユーザーのユニークなユーザー識別子。external_idの代替です。 | はい、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`のいずれかが必須です。 |
| `user_alias_label` | 文字列 | ユーザーエイリアスをグループ化するための共通ラベル。 | はい、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`のいずれかが必須です。 |
| `name` | 文字列 | ユーザーのカスタムイベント。 | はい |
| `time` | 文字列 | イベントの時刻。以下のISO-8601形式のいずれかで渡すことができます：{::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS"（例：2019-11-20T18:38:57） </li> </ul> {:/} | はい |
| `<event name>.properties.<property name>` | 複数 | カスタムイベントに関連するイベントプロパティ。例えば`rented_movie.properties.title`です。 | いいえ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
external_id自体は必須ではありませんが、以下のフィールドのいずれかを含める必要があります：<br>- `external_id`：顧客のユニークなユーザー識別子<br>- `braze_id`：既存のBrazeユーザーに対して取得されたユニークなユーザー識別子<br>- `user_alias_name`：匿名ユーザーのユニークなユーザー識別子
{% endalert %}

#### CSVサイズ {#csv-size}

Brazeは、最大500 MBのサイズの標準CSV形式のユーザーデータを受け付けます。CSVファイルテンプレートのダウンロードについては、[external IDを使用したインポート](#importing-with-external-id)または[ユーザーエイリアスを使用したインポート](#importing-with-user-alias)を参照してください。

#### データポイントに関する考慮事項 {#data-point-considerations}

CSVを介してインポートされた各顧客データは、ユーザープロファイルの既存の値を上書きし、external IDと空白の値を除いてデータポイントとしてカウントされます。

- CSVインポートを介してアップロードされたexternal IDはデータポイントを消費しません。external IDのみをアップロードして既存のBrazeユーザーをセグメント化するためにCSVファイルをアップロードする場合、データポイントを消費せずに行うことができます。インポートにユーザーのメールや電話番号などの追加データを含めた場合、既存のユーザーデータが上書きされ、データポイントが消費されます。
    - セグメンテーション目的のCSVインポート（`external_id`、`braze_id`、または`user_alias_name`のみをフィールドとして行われたインポート）はデータポイントを消費しません。
- 空白の値はユーザープロファイルの既存の値を上書きしません。CSVファイルに既存のすべてのユーザー属性やカスタムイベントを含める必要はありません。
- `email_subscribe`、`push_subscribe`、`subscription_group_id`、または`subscription_state`の更新はデータポイントの消費にカウントされません。

{% alert important %}
CSVインポートまたはAPIを介してユーザーの言語や国を設定すると、BrazeがSDKを介してこの情報を自動的にキャプチャすることが妨げられます。
{% endalert %}

## CSVのインポート {#importing-a-csv}

CSVファイルをインポートするには：
1. **オーディエンス** > **ユーザーをインポートする**に移動します。
2. **ファイルを参照**を選択してファイルを選択し、**インポートを開始**を選択します。Brazeがファイルをアップロードし、列ヘッダーと各列のデータタイプを確認します。

{% alert important %}
CSVインポートは大文字と小文字を区別します。つまり、CSVインポートで大文字を使用すると、フィールドが標準属性ではなくカスタム属性として書き込まれます。例えば、「email」は正しいですが、「Email」はカスタム属性として書き込まれます。
{% endalert %}

![インポートするユーザー情報のタイプとして「イベント」オプションが選択されている画面][5]

アップロードが完了すると、ファイルの内容のプレビューを表示できます。テーブルの情報は、CSVファイルの上位行の値に基づいています。

**ユーザーをインポートする**ページで進捗状況を追跡できます。このページは5秒ごとに更新されるか、**テーブルを更新**を選択すると更新されます。インポート中もBrazeダッシュボードの他の部分を引き続き使用でき、インポートの開始時と終了時に通知を受け取ります。

最新のインポート、ファイル名、CSVタイプ、ファイル内の行数、正常にインポートされた行数、各ファイルの合計行数、各インポートのステータスも表示できます。

複数のCSVファイルを同時にインポートできます。CSVインポートは同時に実行されるため、更新の順序がシリアルであることは保証されません。CSVインポートを順番に実行する必要がある場合は、CSVインポートが完了するまで待ってから2番目のファイルをアップロードしてください。

インポートプロセスでエラーが発生した場合、ファイルの合計行数の横に警告アイコンが表示されます。アイコンにカーソルを合わせると、特定の行が失敗した理由の詳細を確認できます。インポートが完了すると、すべてのデータが既存のプロファイルに追加されるか、新しいプロファイルが作成されます。

![1つの列にデータタイプが混在するエラーでCSVファイルのアップロードが完了した画面][4]{: style="max-width:70%"}

### 考慮事項 {#considerations}

アップロード中にBrazeがファイルの上位行に不正な形式を検出した場合、これらのエラーはサマリーとともに表示されます。例えば、ファイルに不正な形式の行が含まれている場合、ファイルをインポートする際のプレビューにこのエラーが表示されます。エラーがあってもファイルをインポートできますが、インポートを続行する前にファイル内のエラーを修正することをお勧めします。

さらに、Brazeはプレビュー用に入力ファイルのすべての行をスキャンするわけではないため、アップロード前にCSVファイル全体を確認することが重要です。つまり、Brazeがこのプレビューの生成中にキャッチしないエラーが存在する可能性があります。

不正な形式の行やexternal IDが欠落している行はインポートされません。その他のすべてのエラーはインポートできますが、セグメントを作成する際のフィルタリングに影響を与える可能性があります。詳細については、[トラブルシューティング](#troubleshooting)セクションに進んでください。

{% alert warning %}
エラーはデータタイプとファイル構造のみに基づいています。例えば、フォーマットが不適切なメールアドレスでも、文字列として解析できるため、インポートされます。
{% endalert %}

### LambdaユーザーCSVインポート {#lambda-user-csv-import}

サーバーレスのS3 Lambda CSVインポートスクリプトを使用して、ユーザー属性をプラットフォームにアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVをS3バケットにドロップすると、スクリプトがAPIを介してアップロードします。

100万行のファイルの推定実行時間は約5分です。詳細については、[ユーザー属性CSVからBrazeへのインポート]({{site.baseurl}}/user_csv_lambda)を参照してください。

## セグメンテーション {#segmenting}

ユーザーインポートはユーザープロファイルを作成および更新し、セグメントの作成にも使用できます。セグメントを作成するには、インポートを開始する前に**このCSVからインポートされたユーザーからセグメントを自動的に生成する**を選択します。

セグメントの名前を設定するか、デフォルト（ファイル名）を受け入れることができます。セグメントの作成に使用されたファイルには、インポートが完了した後にセグメントを表示するためのリンクが表示されます。

セグメントの作成に使用されるフィルターは、選択されたインポートで作成または更新されたユーザーを選択し、セグメント編集ページの他のすべてのフィルターとともに使用できます。

## トラブルシューティング {#troubleshooting}

### 行の欠落 {#missing-rows}

インポートされたユーザー数がCSVファイルの合計行数と一致しない理由はいくつかあります：

- **重複するexternal ID：** external IDの列が重複している場合、行が正しくフォーマットされていても、不正な形式またはインポートされない行が発生する可能性があります。場合によっては、特定のエラーが報告されないことがあります。CSVに重複するexternal IDがないか確認してください。ある場合は、重複を削除して再度アップロードしてみてください。
- **アクセント付き文字：** CSVファイルにアクセント付きの名前や属性が含まれている場合があります。問題を防ぐために、ファイルがUTF-8エンコードされていることを確認してください。

### 不正な形式の行 {#malformed-row}

データを正しくインポートするには、CSVファイルにヘッダー行を含める必要があります。各行はヘッダー行と同じ数のセルを持つ必要があります。ヘッダー行よりも値が多いまたは少ない行はインポートから除外されます。値内のカンマは区切り文字として解釈され、このエラーが発生する原因となります。さらに、すべてのデータはUTF-8エンコードされている必要があります。

CSVファイルに空白行があり、CSVファイルの合計行数よりも少ない行がインポートされた場合、空白行はインポートする必要がないため、インポートに問題があるとは限りません。正しくインポートされた行数を確認し、インポートしようとしているユーザー数と一致していることを確認してください。

### 複数のデータタイプ {#multiple-data-types}

Brazeは、列内の各値が同じデータタイプであることを期待しています。属性のデータタイプと一致しない値は、セグメンテーションでエラーを引き起こします。

### 不正なフォーマットの日付 {#incorrectly-formatted-dates}

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式でない日付は、インポート時に日時として読み取られません。

### 文字列の引用符 {#string-quotation}

シングルクォート（''）またはダブルクォート（""）で囲まれた値は、インポート時に文字列として読み取られます。

### カスタム属性としてインポートされたデータ {#data-imported-as-custom-attribute}

デフォルトのユーザーデータ（例：`email`や`first_name`）がカスタム属性としてインポートされている場合は、CSVファイルの大文字小文字とスペースを確認してください。例えば、`First_name`はカスタム属性としてインポートされますが、`first_name`はユーザーのプロファイルの「名」フィールドに正しくインポートされます。

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