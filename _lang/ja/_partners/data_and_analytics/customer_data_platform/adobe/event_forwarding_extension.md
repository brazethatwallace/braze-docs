---
nav_title: イベント転送拡張機能
article_title: Adobe
description: "このリファレンス記事では、Adobe Experience Platform Edge Networkでキャプチャされたデータを利用して、サーバーサイドのイベントの形式でBrazeに送信できるBrazeイベント転送拡張機能について説明します。"
page_type: partner
page_order: 2
search_tag: Partner

---

# Track Events APIイベント転送拡張機能 {#track-events-api-event-forwarding-extension}

> Braze Track Events APIの[イベント転送](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en)拡張機能を使用すると、Adobe Experience Platform Edge Networkでキャプチャされたデータを利用して、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) APIを使用してサーバーサイドのイベントの形式でBrazeに送信できます。

このドキュメントでは、拡張機能のユースケース、イベント転送ライブラリへのインストール方法、およびイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)でその機能を使用する方法について説明します。

{% alert note %}
Adobeイベント転送を使用すると、Brazeのデータポイント使用量が増加する可能性があります。詳細については、[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points)に関するBrazeのドキュメントを参照してください。
{% endalert %}

## ユースケース {#use-cases}

この拡張機能は、Brazeの顧客分析およびターゲティング機能を活用するために、Edge Networkからのデータを使用します。

たとえば、マルチチャネルプレゼンス（Webサイトとモバイル）を展開しており、Webサイトプラットフォームとモバイルプラットフォームからトランザクション入力や会話入力をイベントデータとして取得している小売組織について考えてみます。

さまざまな[タグ](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en)ルールを使用して、このデータはリアルタイムでEdge Networkに送信されます。ここからBrazeイベント転送拡張機能により、関連するイベントがサーバーサイドからBrazeへ自動的に送信されます。

## レート制限 {#rate-limits}

| API | レート制限 |
| --- | --- |
| User Track | 1分あたり50,000件のリクエスト。<br><br>詳細については、[User Track APIのドキュメント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#rate-limit)を参照してください。
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rate limits" }

## 統合 {#integration}

### ステップ1:必要な設定の詳細を収集する {#step-1-gather-required-configuration-details}

Edge NetworkをBrazeに接続するには、以下が必要です。

| キーのタイプ | 説明 |
| --- | --- |
| Brazeインスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから入手できます。また、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)でも確認できます。 |
| Braze REST APIキー | すべての権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**Settings** > **API Keys**から作成できます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Gather required configuration details" }

### ステップ2:シークレットを作成する {#step-2-create-a-secret}

新しい[イベント転送シークレット](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en)を作成し、値を[Braze APIキー](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details)に設定します。これは、アカウントへの接続を認証し、値を安全に保護するために使用されます。

### ステップ3:Braze拡張機能をインストールして設定する {#step-3-install-and-configure-the-braze-extension}

1. 拡張機能をインストールするには、[イベント転送プロパティを作成する](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties)か、既存のプロパティを編集することを選択します。
2. 次に、左側のナビゲーションで**Extensions**を選択します。**Catalog**タブで、Braze拡張機能のカードの**Install**を選択します。
3. 次の画面で、RESTインスタンスとAPIキーを入力し、完了したら**Save**を選択します。

### ステップ4:送信イベントルールを作成する {#step-4-create-a-send-event-rule}

拡張機能をインストールした後、新しいイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)を作成し、必要に応じてその条件を設定します。ルールのアクションを設定する際に、**Braze**拡張機能を選択し、アクションタイプとして**Send Event**を選択します。

![]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab User Identification %}

| 入力 | 説明 |
| --- | --- |
| 外部ユーザーID | 長く、ランダムで、よく分散されたUUIDまたはGUID。ユーザーIDの命名に別の方法を選択する場合、それらも長く、ランダムで、よく分散されている必要があります。[推奨されるユーザーID命名規則]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#suggested-user-id-naming-convention)について詳しく学びます。 |
| BrazeユーザーID | Brazeユーザー識別子。 |
| ユーザーエイリアス | エイリアスは、代替の一意のユーザー識別子として機能します。エイリアスを使用して、コアユーザーIDとは異なる次元でユーザーを識別します。<br><br>ユーザーエイリアスオブジェクトは2つの部分で構成されています。識別子自体の`alias_name`とエイリアスの種類を示す`alias_label`です。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_name`は`alias_label`ごとに1つしか持つことができません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Create a send event rule" }

{% alert note %}
イベントをユーザーに結びつけるには、`External User ID`フィールド、`Braze User Identifier`フィールド、または`User Alias`セクションのいずれかを入力する必要があります。
{% endalert %}

{% endtab %}
{% tab Event Data %}

| 入力 | 説明 | 必須 |
| --- | --- | --- |
| イベント名 | イベントの名前。 | はい |
| イベント時間 | ISO 8601または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の日付時刻文字列。 | はい |
| アプリ識別子 | アプリ識別子または`app_id`は、ワークスペース内の特定のアプリとアクティビティを関連付けるパラメーターです。ワークスペース内のどのアプリと対話するかを指定します。 | いいえ |
| イベントプロパティ | イベントのカスタムプロパティを含むJSONオブジェクト。 | いいえ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Create a send event rule" }

{% alert note %}
**Braze Send Event**アクションには**Event Name**と**Event Time**を指定するだけで済みますが、カスタムプロパティフィールドにはできるだけ多くの情報を含めるべきです。詳細については[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照してください。
{% endalert %}

{% endtab %}
{% tab User Attribute %}

ユーザー属性は、指定されたユーザープロファイル上の指定された名前と値で属性を作成または更新するフィールドを含むJSONオブジェクトにすることができます。次のプロパティがサポートされています。

| ユーザー属性 | 説明 |
| --- | --- |
| 名 | ユーザーの名。 |
| 姓 | ユーザーの姓。 |
| 電話 | ユーザーの電話番号。 |
| メール | ユーザーのメールアドレス。 |
| 性別 | 次の文字列のいずれか:「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（回答しない）。 |
| 市区町村 | ユーザーの市区町村。 |
| 国 | [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)形式の文字列としてのユーザーの国。 |
| 言語 | [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)形式の文字列としてのユーザーの言語。 |
| 生年月日 | 「YYYY-MM-DD」形式の文字列としてのユーザーの生年月日（例：1980-12-21）。 |
| タイムゾーン | [IANAタイムゾーンデータベース](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)からのタイムゾーン名（例：'America/New_York'または'Eastern Time (US & Canada)'）。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| Twitter | id（整数）、`screen_name`（文字列、X（旧Twitter）ハンドル）、`followers_count`（整数）、`friends_count`（整数）、`statuses_count`（整数）のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Create a send event rule" }

{% alert note %}
設定内で追加されたすべての属性は、属性の値が変更されたかどうかに関係なく、イベントがBrazeに送信されるたびに送信されます。ユーザー属性を設定する際には、これがデータポイント使用量にどのような影響を与えるかを確認してください。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ5:購入イベント送信ルールを作成する {#step-5-create-a-send-purchase-event-rule}

拡張機能をインストールした後、新しいイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)を作成し、必要に応じてその条件を設定します。ルールのアクションを設定する際に、**Braze**拡張機能を選択し、アクションタイプとして**Send Purchase Event**を選択します。

![]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab User Identification %}

| 入力 | 説明 |
| --- | --- |
| 外部ユーザーID | 長く、ランダムで、よく分散されたUUIDまたはGUID。ユーザーIDの命名に別の方法を選択する場合、それらも長く、ランダムで、よく分散されている必要があります。[推奨されるユーザーID命名規則]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#suggested-user-id-naming-convention)について詳しく学びます。 |
| BrazeユーザーID | Brazeユーザー識別子。 |
| ユーザーエイリアス | エイリアスは、代替の一意のユーザー識別子として機能します。エイリアスを使用して、コアユーザーIDとは異なる次元でユーザーを識別します。<br><br>ユーザーエイリアスオブジェクトは2つの部分で構成されています。識別子自体の`alias_name`とエイリアスの種類を示す`alias_label`です。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_name`は`alias_label`ごとに1つしか持つことができません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 5: Create a send purchase event rule" }

{% alert note %}
イベントをユーザーにリンクするには、`External User ID`フィールド、`Braze User Identifier`フィールド、または`User Alias`セクションのいずれかを入力する必要があります。
{% endalert %}

{% endtab %}
{% tab Purchase Data %}

| 入力 | 説明 | 必須 |
| --- | --- | --- |
| プロダクトID | 購入の識別子（例：製品名や製品カテゴリ）。 | はい |
| 購入時刻 | ISO 8601または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の日付時刻文字列。 | はい |
| 通貨 | [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)アルファベット通貨コード形式の文字列としての通貨。 | はい |
| 価格 | オブジェクトの価格。 | はい |
| 数量 | 購入数量。指定されていない場合、デフォルト値は1になります。最大値は100未満にする必要があります。 | いいえ |
| アプリ識別子 | アプリ識別子または`app_id`は、ワークスペース内の特定のアプリとアクティビティを関連付けるパラメーターです。ワークスペース内のどのアプリと対話するかを指定します。 | いいえ |
| 購入プロパティ | 購入のカスタムプロパティを含むJSONオブジェクト。 | いいえ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 5: Create a send purchase event rule" }

{% alert note %}
**Send Purchase Event**アクションには`Product ID`、`Purchase Time`、`Currency`、および`Price`のみを指定する必要がありますが、購入プロパティフィールドにはできるだけ多くの情報を含めるべきです。詳細については[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照してください。
{% endalert %}

{% endtab %}
{% tab User Attributes %}

設定ビュー内で各イベントに属性を送信するかどうかを選択できます。

ユーザー属性は、指定されたユーザープロファイル上の指定された名前と値で属性を作成または更新するフィールドを含むJSONオブジェクトにすることができます。次のプロパティがサポートされています。

| ユーザー属性 | 説明 |
| --- | --- |
| 名 | ユーザーの名。 |
| 姓 | ユーザーの姓。 |
| 電話 | ユーザーの電話番号。 |
| メール | ユーザーのメールアドレス。 |
| 性別 | 次の文字列のいずれか:「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（回答しない）。 |
| 市区町村 | ユーザーの市区町村。 |
| 国 | [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)形式の文字列としてのユーザーの国。 |
| 言語 | [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)形式の文字列としてのユーザーの言語。 |
| 生年月日 | 「YYYY-MM-DD」形式の文字列としてのユーザーの生年月日（例：1980-12-21）。 |
| タイムゾーン | [IANAタイムゾーンデータベース](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)からのタイムゾーン名（例：'America/New_York'または'Eastern Time (US & Canada)'）。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| Twitter | id（整数）、`screen_name`（文字列、X（旧Twitter）ハンドル）、`followers_count`（整数）、`friends_count`（整数）、`statuses_count`（整数）のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 5: Create a send purchase event rule" }

{% alert note %}
設定内で追加されたすべての属性は、属性の値が変更されたかどうかに関係なく、イベントがBrazeに送信されるたびに送信されます。ユーザー属性を設定する際には、これがデータポイント使用量にどのような影響を与えるかを確認してください。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ6:Braze内のデータを検証する {#step-6-validate-data-within-braze}

イベントコレクションとAdobe Experience Platformの統合が成功した場合、[ユーザープロファイルを表示する]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/)際にBrazeコンソール内にイベントが表示されます。具体的には、Brazeに送信された新しいイベントデータは、特定のユーザーの[概要タブ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab)の**Purchases**または**Custom Events**セクションに反映されます。