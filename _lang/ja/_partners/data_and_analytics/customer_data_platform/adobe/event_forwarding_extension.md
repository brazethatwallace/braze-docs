---
nav_title: イベント転送拡張機能
article_title: Adobe
description: "このリファレンス記事では、Adobe Experience Platform Edge Networkでキャプチャされたデータを利用して、サーバーサイドのイベントの形式でBrazeに送信できるBrazeイベント転送拡張機能について説明します。"
page_type: partner
page_order: 2
search_tag: Partner
---

# Track Events APIイベント転送拡張機能 {#track-events-api-event-forwarding-extension}

> Braze Track Events APIの[イベント転送](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en)拡張機能を使用すると、Adobe Experience Platform Edge Networkでキャプチャされたデータを利用して、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) APIを使用してサーバーサイドのイベントの形式でBrazeに送信できます。

このドキュメントでは、拡張機能のユースケース、イベント転送ライブラリへのインストール方法、およびイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)でその機能を使用する方法について説明します。

{% alert note %}
Adobeイベント転送を使用すると、Brazeのデータポイント使用量が増加する可能性があります。詳細については、[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#billable-data-points)に関するBrazeのドキュメントを参照してください。
{% endalert %}

## ユースケース {#use-cases}

この拡張機能は、Brazeの顧客分析とターゲティング機能を活用するために、Edge Networkのデータを使用します。

例えば、マルチチャネル（Webサイトとモバイル）を展開する小売企業が、Webサイトやモバイルプラットフォームからトランザクションデータや会話データをイベントデータとして収集しているケースを考えてみましょう。

さまざまな[タグ](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en)ルールを使用して、このデータはリアルタイムでEdge Networkに送信されます。ここから、Brazeイベント転送拡張機能がサーバーサイドで関連するイベントを自動的にBrazeに送信します。

## レート制限 {#rate-limits}

| API | レート制限 |
| --- | --- |
| User Track | 1分あたり50,000リクエスト。<br><br>詳細については、[User Track APIドキュメント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit)を参照してください。
{: .reset-td-br-1 .reset-td-br-2 aria-label="レート制限" }

## インテグレーション {#integration}

### ステップ1:必要な設定情報を収集する {#step-1-gather-required-configuration-details}

Edge Network を Braze に接続するには、以下の情報が必要です。

| キーの種類 | 説明 |
| --- | --- |
| Braze インスタンス | Braze インスタンスは、Braze オンボーディングマネージャーから取得できます。また、[API 概要ページ]({{site.baseurl}}/api/basics#endpoints)で確認することもできます。 |
| Braze REST APIキー | すべての権限を持つ Braze REST APIキー。<br><br>これは Braze ダッシュボードの**設定** > **APIキー**から作成できます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1:必要な設定情報を収集する" }

### ステップ2:シークレットを作成する {#step-2-create-a-secret}

新しい[イベント転送シークレット](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en)を作成し、値を [Braze APIキー](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details)に設定します。これにより、値を安全に保ちながら、アカウントへの接続を認証できます。

### ステップ3:Braze 拡張機能をインストールして設定する {#step-3-install-and-configure-the-braze-extension}

1. 拡張機能をインストールするには、[イベント転送プロパティを作成する](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties)か、編集する既存のプロパティを選択します。
2. 次に、左側のナビゲーションで**Extensions**を選択します。**Catalog**タブで、Braze 拡張機能のカードの**Install**を選択します。
3. 次の画面で REST インスタンスと APIキーを入力し、完了したら**Save**を選択します。

### ステップ4:イベント送信ルールを作成する {#step-4-create-a-send-event-rule}

拡張機能をインストールしたら、新しいイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)を作成し、必要に応じて条件を設定します。ルールのアクションを設定する際、**Braze** 拡張機能を選択し、次にアクションタイプとして**Send Event**を選択します。

![Braze Send Event を使用するように設定された Adobe イベント転送ルールアクション。]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab ユーザー識別 %}

| 入力 | 説明 |
| --- | --- |
| 外部ユーザー ID | 長く、ランダムで、十分に分散された UUID または GUID。ユーザー ID の命名に別の方法を選択する場合も、長く、ランダムで、十分に分散されている必要があります。[推奨されるユーザー ID の命名規則]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices)について詳しくはこちらをご覧ください。 |
| Braze ユーザー ID | Braze ユーザー識別子。 |
| ユーザーエイリアス | エイリアスは、代替の一意のユーザー識別子として機能します。コアユーザー ID とは異なる次元でユーザーを識別するためにエイリアスを使用します。<br><br>ユーザーエイリアスオブジェクトは、識別子自体の `alias_name` とエイリアスの種類を示す `alias_label` の2つの部分で構成されます。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに1つの `alias_name` のみ設定できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ4:イベント送信ルールを作成する" }

{% alert note %}
イベントをユーザーに紐付けるには、`External User ID` フィールド、`Braze User Identifier` フィールド、または `User Alias` セクションのいずれかを入力する必要があります。
{% endalert %}

{% endtab %}
{% tab イベントデータ %}

| 入力 | 説明 | 必須 |
| --- | --- | --- |
| イベント名 | イベントの名前。 | はい |
| イベント時刻 | ISO 8601 形式または `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式の日時文字列。 | はい |
| アプリ識別子 | アプリ識別子（`app_id`）は、ワークスペース内の特定のアプリにアクティビティを関連付けるパラメーターです。ワークスペース内のどのアプリとやり取りしているかを指定します。 | いいえ |
| イベントプロパティ | イベントのカスタムプロパティを含む JSON オブジェクト。 | いいえ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ4:イベント送信ルールを作成する" }

{% alert note %}
**Braze Send Event** アクションでは、**Event Name**と**Event Time**のみが必須ですが、カスタムプロパティフィールドにできるだけ多くの情報を含めることをお勧めします。詳細については、[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object)を参照してください。
{% endalert %}

{% endtab %}
{% tab ユーザー属性 %}

ユーザー属性は、指定されたユーザープロファイルに対して、指定された名前と値で属性を作成または更新するフィールドを含む JSON オブジェクトです。以下のプロパティがサポートされています。

| ユーザー属性 | 説明 |
| --- | --- |
| 名 | ユーザーの名。 |
| 姓 | ユーザーの姓。 |
| 電話番号 | ユーザーの電話番号。 |
| メール | ユーザーのメールアドレス。 |
| 性別 | 次の文字列のいずれか:「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（回答しない）。 |
| 市区町村 | ユーザーの市区町村。 |
| 国 | [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 形式の文字列によるユーザーの国。 |
| 言語 | [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 形式の文字列によるユーザーの言語。 |
| 生年月日 | 「YYYY-MM-DD」形式の文字列によるユーザーの生年月日（例:1980-12-21）。 |
| タイムゾーン | [IANA タイムゾーン](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)データベースのタイムゾーン名（例:「America/New_York」または「Eastern Time (US & Canada)」）。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| Twitter | id（整数）、`screen_name`（文字列、X（旧 Twitter）ハンドル）、`followers_count`（整数）、`friends_count`（整数）、`statuses_count`（整数）のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ4:イベント送信ルールを作成する" }

{% alert note %}
設定内で追加されたすべての属性は、属性の値が変更されたかどうかに関係なく、イベントが Braze に送信されるたびに送信されます。ユーザー属性を設定する際は、これがデータポイント使用量にどのように影響するかを必ず把握しておいてください。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ5:購入イベント送信ルールを作成する {#step-5-create-a-send-purchase-event-rule}

拡張機能をインストールしたら、新しいイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)を作成し、必要に応じて条件を設定します。ルールのアクションを設定する際、**Braze** 拡張機能を選択し、次にアクションタイプとして**Send Purchase Event**を選択します。

![Braze Send Purchase Event を使用するように設定された Adobe イベント転送ルールアクション。]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab ユーザー識別 %}

| 入力 | 説明 |
| --- | --- |
| 外部ユーザー ID | 長く、ランダムで、十分に分散された UUID または GUID。ユーザー ID の命名に別の方法を選択する場合も、長く、ランダムで、十分に分散されている必要があります。[推奨されるユーザー ID の命名規則]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices)について詳しくはこちらをご覧ください。 |
| Braze ユーザー ID | Braze ユーザー識別子。 |
| ユーザーエイリアス | エイリアスは、代替の一意のユーザー識別子として機能します。コアユーザー ID とは異なる次元でユーザーを識別するためにエイリアスを使用します。<br><br>ユーザーエイリアスオブジェクトは、識別子自体の `alias_name` とエイリアスの種類を示す `alias_label` の2つの部分で構成されます。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに1つの `alias_name` のみ設定できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ5:購入イベント送信ルールを作成する" }

{% alert note %}
イベントをユーザーにリンクするには、`External User ID` フィールド、`Braze User Identifier` フィールド、または `User Alias` セクションのいずれかを入力する必要があります。
{% endalert %}

{% endtab %}
{% tab 購入データ %}

| 入力 | 説明 | 必須 |
| --- | --- | --- |
| 商品 ID | 購入の識別子（例:商品名または商品カテゴリ）。 | はい |
| 購入時刻 | ISO 8601 形式または `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式の日時文字列。 | はい |
| 通貨 | [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) アルファベット通貨コード形式の文字列による通貨。 | はい |
| 価格 | オブジェクトの価格。 | はい |
| 数量 | 購入数量。指定しない場合、デフォルト値は1になります。最大値は100未満である必要があります。 | いいえ |
| アプリ識別子 | アプリ識別子（`app_id`）は、ワークスペース内の特定のアプリにアクティビティを関連付けるパラメーターです。ワークスペース内のどのアプリとやり取りしているかを指定します。 | いいえ |
| 購入プロパティ | 購入のカスタムプロパティを含む JSON オブジェクト。 | いいえ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ5:購入イベント送信ルールを作成する" }

{% alert note %}
**Send Purchase Event** アクションでは、`Product ID`、`Purchase Time`、`Currency`、`Price` のみが必須ですが、購入プロパティフィールドにできるだけ多くの情報を含めることをお勧めします。詳細については、[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)を参照してください。
{% endalert %}

{% endtab %}
{% tab ユーザー属性 %}

設定ビュー内で、各イベントとともに属性を送信するかどうかを選択できます。

ユーザー属性は、指定されたユーザープロファイルに対して、指定された名前と値で属性を作成または更新するフィールドを含む JSON オブジェクトです。以下のプロパティがサポートされています。

| ユーザー属性 | 説明 |
| --- | --- |
| 名 | ユーザーの名。 |
| 姓 | ユーザーの姓。 |
| 電話番号 | ユーザーの電話番号。 |
| メール | ユーザーのメールアドレス。 |
| 性別 | 次の文字列のいずれか:「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（回答しない）。 |
| 市区町村 | ユーザーの市区町村。 |
| 国 | [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 形式の文字列によるユーザーの国。 |
| 言語 | [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 形式の文字列によるユーザーの言語。 |
| 生年月日 | 「YYYY-MM-DD」形式の文字列によるユーザーの生年月日（例:1980-12-21）。 |
| タイムゾーン | [IANA タイムゾーン](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)データベースのタイムゾーン名（例:「America/New_York」または「Eastern Time (US & Canada)」）。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| Twitter | id（整数）、`screen_name`（文字列、X（旧 Twitter）ハンドル）、`followers_count`（整数）、`friends_count`（整数）、`statuses_count`（整数）のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ5:購入イベント送信ルールを作成する" }

{% alert note %}
設定内で追加されたすべての属性は、属性の値が変更されたかどうかに関係なく、イベントが Braze に送信されるたびに送信されます。ユーザー属性を設定する際は、これがデータポイント使用量にどのように影響するかを必ず把握しておいてください。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ6:Braze 内でデータを検証する {#step-6-validate-data-within-braze}

イベント収集と Adobe Experience Platform のインテグレーションが成功した場合、[ユーザープロファイルの表示]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)時に Braze コンソール内でイベントを確認できます。具体的には、Braze に送信された新しいイベントデータは、特定のユーザーの[概要タブ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#overview-tab)の**Purchases**または**Custom Events**セクションに反映されます。