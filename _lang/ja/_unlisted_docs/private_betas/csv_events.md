---
nav_title: ユーザーデータとCSVイベントのインポート
article_title: ユーザーデータとCSVイベントのインポート
permalink: "/csv_events/"
description: "このリファレンス記事では、ユーザーデータのインポート方法と、CSVファイルを使用したカスタムイベントのインポート方法について説明します。"
page_type: reference
---

# ユーザーデータのインポート（CSVイベント早期アクセス） {#importing-user-data-csv-events-early-access}

> Brazeは、プラットフォームにユーザーデータをインポートするためのさまざまな方法を提供しています。SDK、API、クラウドデータ取り込み、テクノロジーパートナー連携、CSVファイルなどです。この記事では、[CSVファイルによるカスタムイベントのインポート（早期アクセス）](#importing-custom-events)を含む、ユーザーデータのインポートに関する詳細な手順を説明します。

{% alert important %}
法的に義務付けられたトランザクションメールをSMSゲートウェイに送信しないでください。これらのメールが配信されない可能性が高いためです。

電話番号とプロバイダーのメール-to-SMSゲートウェイドメイン（MM3）を使用して送信したメールは、SMS（テキスト）メッセージとして受信される場合がありますが、一部のメールプロバイダーはこの動作をサポートしていません。例えば、T-Mobileの電話番号（「9999999999@tmomail.net」など）にメールを送信した場合、SMSメッセージはT-Mobileネットワーク上でその電話番号を所有している人に送信されます。

これらのメールがSMSゲートウェイに配信されない場合でも、メールの課金対象としてカウントされます。サポートされていないゲートウェイへのメール送信を避けるには、[サポートされていないゲートウェイドメイン名のリスト](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads)を確認してください。
{% endalert %}


先に進む前に、Brazeはインポート時にHTMLデータのサニタイズ（検証や適切なフォーマット）を行わないことに注意してください。つまり、Webパーソナライゼーション用のすべてのインポートデータからスクリプトタグを除去する必要があります。

## REST API

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、ユーザーのカスタムイベント、ユーザー属性、購入を記録できます。

## CSVインポート {#csv-import}

CSVファイルを使用して、**オーディエンス** > **ユーザーをインポート**からユーザープロファイルをアップロードおよび更新できます。

CSVファイルを使用したユーザーデータのインポートでは、名やメールなどのユーザー属性に加え、靴のサイズなどのカスタム属性の記録と更新がサポートされています。CSVをインポートするには、2つの一意のユーザー識別子のいずれかを指定します：`external_id`またはユーザーエイリアスです。

{% alert important %}
ユーザーインポートでは、ユーザーのカスタムイベントの記録と更新もサポートされています。ユーザー属性と同様に、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`を使用してインポートできます。詳細については、[カスタムイベントのインポート](#importing-custom-events)を参照してください。
{% endalert %}

{% alert note %}
`external_id`を持つユーザーと持たないユーザーが混在している場合は、インポートごとに1つのCSVファイルを作成する必要があります。1つのCSVファイルに`external_ids`とユーザーエイリアスの両方を含めることはできません。
{% endalert %}

### external IDを使用したインポート {#importing-with-external-id}

顧客データをインポートする際には、各顧客の一意の識別子（`external_id`とも呼ばれます）を指定する必要があります。CSVインポートを開始する前に、Brazeでユーザーがどのように識別されるかを開発チームに確認することが重要です。通常、これは内部データベースIDです。これは、モバイルおよびWebでBraze SDKによってユーザーが識別される方法と一致する必要があり、各顧客がデバイス間でBraze内に単一のユーザープロファイルを持つように設計されています。Brazeの[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)について詳しくはこちらをご覧ください。

インポートで`external_id`を指定すると、Brazeは同じ`external_id`を持つ既存のユーザーを更新するか、見つからない場合はその`external_id`が設定された新しい識別済みユーザーを作成します。

- **ダウンロード：** [CSV属性インポートテンプレート][import_template]
- **ダウンロード：** [CSVイベントインポートテンプレート][events_template]

### ユーザーエイリアスを使用したインポート {#importing-with-user-alias}

`external_id`を持たないユーザーをターゲットにするには、ユーザーエイリアスを持つユーザーのリストをインポートできます。エイリアスは代替の一意のユーザー識別子として機能し、サインアップやアカウント作成をしていない匿名ユーザーに対してマーケティングを行う場合に役立ちます。

エイリアスのみのユーザープロファイルをアップロードまたは更新する場合は、CSVに以下の2つの列が必要です：

- `user_alias_name`：一意のユーザー識別子。`external_id`の代替です。
- `user_alias_label`：ユーザーエイリアスをグループ化するための共通ラベルです。

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

インポートで`user_alias_name`と`user_alias_label`の両方を指定すると、Brazeは同じ`user_alias_name`と`user_alias_label`を持つ既存のユーザーを更新します。ユーザーが見つからない場合、Brazeはその`user_alias_name`が設定された新しい識別済みユーザーを作成します。

{% alert important %}
既に`external_id`を持つ既存のユーザーを`user_alias_name`で更新するためにCSVインポートを使用することはできません。代わりに、関連付けられた`user_alias_name`を持つ新しいユーザープロファイルが作成されます。エイリアスのみのユーザーを`external_id`に関連付けるには、[ユーザー識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用してください。
{% endalert %}

- **ダウンロード：** [CSVエイリアス属性インポートテンプレート][template_alias_attributes]
- **ダウンロード：** [CSVエイリアスイベントインポートテンプレート][template_alias_events]

### Braze IDを使用したインポート {#importing-with-braze-id}

`external_id`や`user_alias_name`と`user_alias_label`の値の代わりに、内部のBraze ID値を使用してBraze内の既存のユーザープロファイルを更新するには、`braze_id`を列ヘッダーとして指定します。

これは、セグメンテーション内のCSVエクスポートオプションを使用してBrazeからユーザーデータをエクスポートし、既存のユーザーに新しいカスタム属性を追加したい場合に役立ちます。

{% alert important %}
`braze_id`を使用してCSVインポートで新しいユーザーを作成することはできません。この方法は、Brazeプラットフォーム内の既存のユーザーを更新するためにのみ使用できます。
{% endalert %}

{% alert tip %}
Brazeダッシュボードからのcsv CSVエクスポートでは、`braze_id`の値が`Appboy ID`とラベル付けされている場合があります。このIDはユーザーの`braze_id`と同じであるため、CSVを再インポートする際にこの列の名前を`braze_id`に変更できます。
{% endalert %}

### デフォルト属性のインポート {#importing-default-attributes}

ユーザーのデフォルト属性をインポートするには、**ユーザーをインポート** > **属性**に移動します。デフォルトのユーザー属性は、Brazeの予約キーです。例えば、`first_name`や`email`などがあります。カスタム属性はビジネスに固有のものです。例えば、旅行予約アプリには`last_destination_searched`というカスタム属性があるかもしれません。

{% alert important %}
顧客データを属性としてインポートする場合、使用する列ヘッダーはデフォルトのユーザー属性のスペルと大文字小文字が正確に一致する必要があります。一致しない場合、Brazeはそのユーザーのプロファイルにカスタム属性を自動的に作成します。
{% endalert %}

#### デフォルトのユーザーデータ列ヘッダー {#default-user-data-column-headers}

| ユーザープロファイルフィールド | データタイプ | 情報 | 必須 |
|---|---|---|---|
| `external_id` | String | 顧客の一意のユーザー識別子。 | はい、[以下の注記](#about-external-ids)を参照してください。 |
| `user_alias_name` | String | 匿名ユーザーの一意のユーザー識別子。`external_id`の代替です。 | いいえ、[以下の注記](#about-external-ids)を参照してください。 |
| `user_alias_label` | String | ユーザーエイリアスをグループ化するための共通ラベル。 | はい、`user_alias_name`を使用する場合。 |
| `first_name` | String | ユーザーが指定した名（例：`Jane`）。 | いいえ |
| `last_name` | String | ユーザーが指定した姓（例：`Doe`）。 | いいえ |
| `email` | String | ユーザーが指定したメールアドレス（例：`jane.doe@braze.com`）。 | いいえ |
| `country` | String | 国コードはISO-3166-1 alpha-2規格でBrazeに渡す必要があります（例：`GB`）。 | いいえ |
| `dob` | String | 「YYYY-MM-DD」形式で渡す必要があります（例：`1980-12-21`）。これによりユーザーの生年月日がインポートされ、誕生日が「今日」のユーザーをターゲットにできます。 | いいえ |
| `gender` | String | 「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（回答しない）、またはnil（不明）。 | いいえ |
| `home_city` | String | ユーザーが指定した居住都市（例：`London`）。 | いいえ |
| `language` | String | 言語はISO-639-1規格でBrazeに渡す必要があります（例：`en`）。<br>[受け入れ可能な言語のリスト]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes)を参照してください。 | いいえ |
| `phone` | String | ユーザーが指定した電話番号（`E.164`形式、例：`+442071838750`）。<br>フォーマットのガイダンスについては、[ユーザーの電話番号]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)を参照してください。 | いいえ |
| `email_open_tracking_disabled` | Boolean | trueまたはfalseを指定できます。trueに設定すると、このユーザーに送信されるすべての今後のメールに開封トラッキングピクセルが追加されなくなります。 | いいえ |
| `email_click_tracking_disabled` | Boolean | trueまたはfalseを指定できます。trueに設定すると、このユーザーに送信される今後のメール内のすべてのリンクのクリックトラッキングが無効になります。 | いいえ |
| `email_subscribe` | String | 使用可能な値は`opted_in`（メールメッセージの受信を明示的に登録）、`unsubscribed`（メールメッセージの受信を明示的に拒否）、`subscribed`（オプトインもオプトアウトもしていない）です。 | いいえ |
| `push_subscribe` | String | 使用可能な値は`opted_in`（プッシュメッセージの受信を明示的に登録）、`unsubscribed`（プッシュメッセージの受信を明示的に拒否）、`subscribed`（オプトインもオプトアウトもしていない）です。 | いいえ |
| `time_zone` | String | タイムゾーンはIANAタイムゾーンデータベースと同じ形式でBrazeに渡す必要があります（例：`America/New_York`または`Eastern Time (US & Canada)`）。 | いいえ |
| `date_of_first_session` <br><br> `date_of_last_session`| String | 以下のISO-8601形式のいずれかで渡すことができます：{::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS"（例：2019-11-20T18:38:57） </li> </ul> {:/} | いいえ |
| `subscription_group_id` | String | 購読グループの`id`。この識別子はダッシュボードの購読グループページで確認できます。 | いいえ |
| `subscription_state` | String | `subscription_group_id`で指定された購読グループの購読ステータス。許可される値は`unsubscribed`（購読グループに含まれない）または`subscribed`（購読グループに含まれる）です。 | いいえ、ただし`subscription_group_id`を使用する場合は強く推奨されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### external IDについて {#about-external-ids}

`external_id`は必須ではありませんが、以下のフィールドのいずれかを含める**必要があります**：
- `external_id`：顧客の一意のユーザー識別子、**または**
- `braze_id`：既存のBrazeユーザー用に取得される一意のユーザー識別子、**または**
- `user_alias_name`と`user_alias_label`：匿名ユーザーの一意のユーザー識別子

### カスタム属性のインポート {#importing-custom-attributes}

ユーザーのカスタム属性をインポートするには、**ユーザーをインポート** > **属性**に移動します。デフォルト属性と正確に一致しないヘッダーは、Braze内でカスタム属性として作成されます。

ユーザーインポートでは以下のデータタイプが受け入れられます：

| データタイプ | 説明 |
|-----------|-------------|
| Datetime | ISO-8601形式で保存する必要があります |
| Boolean | TRUEまたはFALSE |
| Number | スペースやカンマのない整数または浮動小数点数。浮動小数点数はピリオド（.）を小数点区切り文字として使用する必要があります |
| String | 列の値を囲む二重引用符がある限り、カンマを含むことができます |
| Blank | 空白の値はユーザープロファイルの既存の値を上書きしません。CSVファイルに既存のすべてのユーザー属性を含める必要はありません |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
配列とプッシュトークンはユーザーインポートではサポートされていません。特に配列の場合、CSVファイル内のカンマは列区切り文字として解釈されるため、値内のカンマはファイルの解析エラーを引き起こします。<br>この種の値をアップロードするには、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用してください。
{% endalert %}

### 購読グループステータスの更新 {#updating-subscription-group-status}

ユーザーインポートを通じて、ユーザーをメールまたはSMS購読グループに追加できます。これはSMSの場合に特に便利です。ユーザーがSMSチャネルでメッセージを受信するには、SMS購読グループに登録されている必要があるためです。詳細については、[SMS購読グループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#subscription-group-mms-enablement)を参照してください。

購読グループのステータスを更新する場合は、CSVに以下の2つの列が必要です：

- `subscription_group_id`：[購読グループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups)の`id`。
- `subscription_state`：使用可能な値は`unsubscribed`（購読グループに含まれない）または`subscribed`（購読グループに含まれる）です。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="購読グループステータスの更新">
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
ユーザーインポートでは、1行につき1つの`subscription_group_id`のみ設定できます。異なる行には異なる`subscription_group_id`の値を設定できます。ただし、同じユーザーを複数の購読グループに登録する必要がある場合は、複数回のインポートを行う必要があります。
{% endalert %}

### カスタムイベントのインポート（早期アクセス） {#importing-custom-events}

{% alert important %}
カスタムイベントのインポートは現在早期アクセス中です。早期アクセスへの参加にご興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

ユーザーのカスタムイベントをインポートするには、**ユーザーをインポート** > **イベント**に移動します。

カスタムイベントはビジネスに固有のものです。例えば、ストリーミングアプリにはrented_movieというカスタムイベントがあるかもしれません。CSVには以下の列ヘッダーが必要です：

- 以下のいずれか：
  - `external_id`、**または**
  - `braze_id`、**または**
  - `user_alias_name`と`user_alias_label`
- Name
- Time

カスタムイベントにはイベントプロパティを設定できます。例えば、カスタムイベントrented_movieにはtitleやgenreなどのプロパティがあるかもしれません。これらのイベントプロパティの列ヘッダーは`<event_name>.properties.<property name>`の形式にする必要があります。例：`rented_movie.properties.title`。

| ユーザープロファイルフィールド                      | データタイプ | 情報                                                                                                                                                                                                             | 必須                                                                                        |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | String    | ユーザーの一意のユーザー識別子。                                                                                                                                                                                 | はい、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`のいずれかが必要です。 |
| `braze_id`                              | String    | Brazeがユーザーに割り当てた識別子。                                                                                                                                                                              | はい、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`のいずれかが必要です。 |
| `user_alias_name`                       | String    | 匿名ユーザーの一意のユーザー識別子。external_idの代替です。                                                                                                                                        | はい、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`のいずれかが必要です。 |
| `user_alias_label`                      | String    | ユーザーエイリアスをグループ化するための共通ラベル。                                                                                                                                                                          | はい、`external_id`、`braze_id`、または`user_alias_name`と`user_alias_label`のいずれかが必要です。 |
| `name`                                  | String    | ユーザーのカスタムイベント。                                                                                                                                                                                           | はい                                                                                             |
| `time`                                  | String    | イベントの時間。以下のISO-8601形式のいずれかで渡すことができます：{::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS"（例：2019-11-20T18:38:57） </li> </ul> {:/} | はい                                                                                             |
| `<event name>.properties.<property name>` | Multiple  | カスタムイベントに関連するイベントプロパティ。例：`rented_movie.properties.title`                                                                                                                        | いいえ                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
external_id自体は必須ではありませんが、以下のフィールドのいずれかを含める必要があります：<br>- `external_id`：顧客の一意のユーザー識別子<br>- `braze_id`：既存のBrazeユーザー用に取得される一意のユーザー識別子<br>- `user_alias_name`：匿名ユーザーの一意のユーザー識別子
{% endalert %}

#### CSVサイズ {#csv-size}

Brazeは、最大500 MBのファイルから標準CSV形式のユーザーデータを受け入れます。CSVファイルテンプレートのいずれかをダウンロードするには、[external IDを使用したインポート](#importing-with-external-id)または[ユーザーエイリアスを使用したインポート](#importing-with-user-alias)を参照してください。

#### データポイントに関する考慮事項 {#data-point-considerations}

CSVを介してインポートされた顧客データの各項目は、ユーザープロファイルの既存の値を上書きし、データポイントとしてカウントされます。ただし、external IDと空白の値は除きます。

- CSVインポートを介してアップロードされたexternal IDは、データポイントを消費しません。既存のBrazeユーザーをセグメント化するためにexternal IDのみをアップロードしてCSVファイルをアップロードする場合、データポイントを消費せずに行えます。インポートでユーザーのメールや電話番号などの追加データを含めた場合、既存のユーザーデータが上書きされ、データポイントが消費されます。
    - セグメンテーション目的のCSVインポート（`external_id`、`braze_id`、または`user_alias_name`のみをフィールドとして行うインポート）は、データポイントを消費しません。
- 空白の値はユーザープロファイルの既存の値を上書きしません。CSVファイルに既存のすべてのユーザー属性やカスタムイベントを含める必要はありません。
- `email_subscribe`、`push_subscribe`、`subscription_group_id`、または`subscription_state`の更新は、データポイントの消費にカウントされません。

{% alert important %}
CSVインポートまたはAPIを介してユーザーの言語や国を設定すると、BrazeがSDKを通じてこの情報を自動的にキャプチャすることが妨げられます。
{% endalert %}

## CSVのインポート {#importing-a-csv}

CSVファイルをインポートするには:
1. **オーディエンス** > **ユーザーをインポート**に移動します。
2. **ファイルを参照**を選択してインポートしたいファイルを選び、**インポートを開始**を選択します。Brazeがファイルをアップロードし、列ヘッダーと各列のデータ型を確認します。

{% alert important %}
CSVインポートは大文字と小文字を区別します。つまり、CSVインポートで大文字を使用すると、そのフィールドは標準属性ではなくカスタム属性として書き込まれます。たとえば、「email」は正しいですが、「Email」はカスタム属性として書き込まれます。
{% endalert %}

![インポートするユーザー情報のタイプとして「イベント」オプションが選択されている画面。][5]

アップロードが完了すると、ファイルの内容のプレビューを確認できます。テーブルの情報は、CSVファイルの先頭行の値に基づいています。

**ユーザーをインポート**ページで進捗状況を確認できます。このページは5秒ごとに更新されるか、**テーブルを更新**を選択した時に更新されます。インポート中もBrazeダッシュボードの他の機能を引き続き使用でき、インポートの開始時と終了時に通知を受け取ります。

また、最近のインポート、ファイル名、CSVタイプ、ファイル内の行数、正常にインポートされた行数、各ファイルの合計行数、および各インポートのステータスを確認できます。

複数のCSVファイルを同時にインポートすることもできます。CSVインポートは並行して実行されるため、更新の順序がシリアルになることは保証されません。CSVインポートを順番に実行する必要がある場合は、CSVインポートが完了するまで待ってから2つ目をアップロードしてください。

インポートプロセスでエラーが発生した場合、ファイルの合計行数の横に警告アイコンが表示されます。アイコンにカーソルを合わせると、特定の行が失敗した理由の詳細を確認できます。インポートが完了すると、すべてのデータが既存のプロファイルに追加されるか、新しいプロファイルが作成されます。

![1つの列に混在するデータ型に関するエラーが発生したCSVファイルのアップロード完了画面][4]{: style="max-width:70%"}

### 注意事項 {#considerations}

アップロード時にBrazeがファイルの先頭行に不正な形式を検出した場合、これらのエラーは概要とともに表示されます。たとえば、ファイルに不正な形式の行が含まれている場合、ファイルをインポートする際のプレビューにこのエラーが表示されます。エラーがあるファイルでもインポートは可能ですが、インポートを続行する前にファイル内のエラーを修正することをお勧めします。

さらに、Brazeはプレビュー用に入力ファイルのすべての行をスキャンするわけではないため、アップロード前にCSVファイル全体を確認することが重要です。これは、プレビューの生成中にBrazeが検出しないエラーが存在する可能性があることを意味します。

不正な形式の行やexternal IDが欠落している行はインポートされません。その他のすべてのエラーはインポートできますが、セグメント作成時のフィルタリングに影響を与える場合があります。詳細については、[トラブルシューティング](#troubleshooting)セクションをご確認ください。

{% alert warning %}
エラーはデータ型とファイル構造のみに基づきます。たとえば、形式が正しくないメールアドレスでも、文字列として解析できるためインポートされます。
{% endalert %}

### Lambda ユーザーCSVインポート {#lambda-user-csv-import}

サーバーレスのS3 Lambda CSVインポートスクリプトを使用して、ユーザー属性をプラットフォームにアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVファイルをS3バケットにドロップすると、スクリプトがAPIを通じてアップロードします。

100万行のファイルの推定実行時間は約5分です。詳細については、[ユーザー属性CSVからBrazeへのインポート]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を参照してください。

## セグメンテーション {#segmenting}

ユーザーインポートはユーザープロファイルの作成と更新に使用でき、セグメントの作成にも利用できます。セグメントを作成するには、インポートを開始する前に**このCSVからインポートされるユーザーからセグメントを自動生成する**を選択します。

セグメントの名前を設定するか、デフォルトを使用できます。デフォルトはファイル名になります。セグメントの作成に使用されたファイルには、インポート完了後にセグメントを表示するためのリンクが表示されます。

セグメントの作成に使用されるフィルターは、選択されたインポートで作成または更新されたユーザーを選択するもので、セグメント編集ページの他のすべてのフィルターとともに利用できます。

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