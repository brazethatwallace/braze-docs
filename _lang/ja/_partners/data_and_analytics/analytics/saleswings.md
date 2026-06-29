---
nav_title: SalesWings
article_title: SalesWings
description: "このリファレンス記事では、BrazeとSalesWingsのパートナーシップについて説明します。SalesWingsは、Braze向けのセールス＆マーケティングオペレーションソリューションで、リードやアカウントの適格性評価を支援し、SalesforceなどのCRM内でセールスインサイトやアラート、B2Bアトリビューションレポートを提供します。Braze内の興味やエンゲージメントを活用して、キャンバスでのパーソナライゼーションやセグメンテーションを行うことができます。SalesWingsは、Digiohと同様にWebサイトからリードを生成する方法も提供しています。"
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs)は、B2B SaaSのセールスおよびマーケティングオペレーションソリューションです。総合的なリードスコアリングとグレーディングを通じてリードとアカウントの適格性管理を支援し、セールスインサイトとアラート、B2Bアトリビューションレポートを提供するとともに、Salesforce CRMとの緊密な統合を実現します。Digiohと同様のWebサイトエンゲージメントアドオンを使えば、Webサイト上でリードを生成できます。Braze内の興味やエンゲージメントを活用して、キャンバスでのパーソナライゼーションやセグメンテーションを行うことができます。

_この統合はSalesWingsによって管理されています。_

## 統合について {#about-the-integration}

SalesWingsでは、マーケティングチームとマーケティングオペレーションマネージャーが、営業チームのためにリードとアカウントの適格性を評価できます。これは、営業とマーケティングの連携とオペレーションの効率化に不可欠です。さらに、SalesWingsはBrazeとともに、リードとアカウントの完全なカスタマージャーニーとBrazeマーケティングキャンペーンのエンゲージメントデータを営業担当者に表示できるため、より精度の高い会話によってリードの認定率を向上させることができます。SalesWingsは、他のシグナルとともにニーズと関心を識別し、CRM内の営業チームに適格なバイヤーを自動的に引き渡すことを可能にします。特定されたニーズ、興味、販売準備状況を、パーソナライゼーションやセグメンテーションのためのBrazeユーザー属性として使用できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| SalesWingsアカウント | このパートナーシップを活用するには、[SalesWingsアカウント](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs)が必要です。 |
| Braze REST APIキー | `users.export.ids`の権限を持つBraze REST APIキー（SalesWingsのインサイトプッシュ機能を使用する場合は`users.track`も必要）。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**で作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存します。 |
| セグメント.comアカウント（オプション） | セグメント.comをご利用の場合は、リードプロファイリングのために、すべてのリードエンゲージメントおよびプロファイルデータの送信とイベントの識別をセグメント.com経由で行うことができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース {#use-cases}

{% tabs %}
{% tab リードとアカウントのスコアリング %}

SalesWingsは、最先端のリードグレーディング機能と[リードスコアリング機能により、リード、取引先責任者、アカウントを選別する柔軟な方法](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs)をBrazeのお客様に提供します。すべてのリードクオリフィケーションデータは、Salesforce CRMや、リード、取引先責任者、アカウント、商談を管理およびレポートするその他のシステムにネイティブにプッシュされます。

![SalesWingsにおけるシンプルなclick-not-codeリードスコアリングモデルの例]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_SalesWingsのシンプルなclick-not-codeリードスコアリングモデルの例_
{% endtab %}
{% tab セールスとマーケティングの連携 %}
SalesWingsでは、マーケティングチームがマーケティング対象として適格なリードを追跡、選別し、営業チームに受け渡すことができます。SalesWingsのデータはすべてSalesforceにネイティブにプッシュされ、既存のプロセスを微調整したり、リスト、レポート、フローなどを使って新しいプロセスを作成したりするのに活用できます。

![SalesWingsのリードスコアリングがSalesforce内でリードやコンタクトのリストに優先順位をつける例]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_SalesWingsリードスコアリングにより、Salesforce内部でネイティブにリードまたは取引先担当者のリストを優先順位付けする方法の例_

![SalesWingsのリードスコアリングがSalesforceのアカウントリストに優先順位をつける例]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_SalesWingsリードスコアリングにより、Salesforce内部でネイティブにアカウントのリストを優先順位付けする方法の例_
{% endtab %}
{% tab リードとアカウントのグレーディング %}
SalesWingsでは、Brazeのお客様がプロファイルデータ（通常はCRMデータ）に基づいてリードとアカウントを選別できます。これは「リードグレーディング」、「フィットスコアリング」、「ファームグラフィックスコアリング」とも呼ばれます。Brazeのお客様は、属性データを直接SalesWingsに送信できます。SalesWingsは、総合的なプロファイルスコアリングのためにSalesforce CRMの標準オブジェクトまたはカスタムオブジェクトのデータとレコードを読み取ることができます。
{% endtab %}
{% tab 営業担当者向けセールスインサイト %}
SalesWingsでは、リード、取引先担当者、アカウントに関するセールスインサイトを営業担当者に対して表示できます（Marketo Sales Insightsの代替）。基本的には、BrazeおよびWebエンゲージメントデータを営業チームに対して表示できます。インサイトはSalesforce CRMにネイティブに組み込まれ、他のCRMやシステムにプッシュするか、Brazeのメールで「セールスアラート」として送信することができます。

![Salesforce内の営業担当者向けセールスインサイトビューの例（他のCRMシステムでも利用可能）]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Salesforce内の営業担当者向けセールスインサイトビューの例（他のCRMシステムでも利用可能）_
{% endtab %}
{% tab セールスアラート %}
SalesWingsは、ネイティブメールとSlackアラートを提供します。Salesforceでレポートサブスクリプションを設定することで、営業チームが日次、週次、月次のメールレポートを取得できます。さらにZapierとの統合により、SalesWingsのリードクオリフィケーションデータに基づいた追加ワークフローを作成できます。

![Slackチャンネルを通じたセールスアラートの例]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Slackチャンネルを使ったセールスアラートの例_
{% endtab %}
{% tab Salesforce CRMでのレポート %}
SalesWingsとSalesforceのネイティブ統合により、WebエンゲージメントデータとBraze Currentsのネイティブ統合によるあらゆるBraze キャンペーンエンゲージメントに基づいて、リード、取引先責任者、取引先、および商談に関する自動レポートを構築できます。例えば、特定のメールキャンペーンをクリックした人、アプリやWebサイトで特定のアクションを行った人など、ホットリードのリストを営業チームに表示することができます。

![BrazeのメールおよびマーケティングエンゲージメントにリンクしたSalesforce内のダッシュボード例。Braze キャンペーンがセールスの結果や成果に与える影響を確認できます]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_BrazeのメールおよびマーケティングエンゲージメントにリンクしたSalesforce内のダッシュボード例。Braze キャンペーンがセールスの結果や成果に与える影響を確認できます_
{% endtab %}
{% endtabs %}

## 統合 {#integration}

### ステップ1: SalesWingsアカウントと設定 {#step-1-saleswings-account-and-configuration}

SalesWingsについて詳しく知るために、フレンドリーなSalesWingsチームとの[デモをスケジュール](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs)してください。

### ステップ2: Webサイトやアプリに行動トラッキングを設置する {#step-2-installing-behavioral-tracking-on-your-website-or-app}

SalesWingsでリードおよびアカウントスコアリング、バイヤーインテントの特定、セールスインサイトのために行動データを収集する方法はいくつかあります。
* リードを追跡して特定したいWebサイトやアプリに、[SalesWingsトラッキングJavaScriptを導入する](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script)
* イベントプロパティとともにBrazeイベントをBraze Currents経由でSalesWingsに取り込む
* [SalesWingsとセグメントの統合](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)を介して行動リードアクティビティデータ（およびリードプロファイルデータ）を送信する
* サードパーティのソリューションからSalesWings [API](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings)に直接データを送信する

### ステップ3: SalesWingsとBrazeを接続する {#step-3-connecting-saleswings-to-braze}

[**SalesWings Integrations**ページ](https://helium.saleswings.pro/integrations)に移動し、**Braze Integration**セクションを展開します。

![SalesWings設定ページのBraze Integrationセクション]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

新しく作成したキーの**Identifier**列の値をコピーし、SalesWingsの**Braze Integration**セクションにある**Braze API key**フィールドにペーストします。

[APIとSDKのエンドポイントの記事]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)の説明に従ってBraze APIエンドポイントを追加し、**Braze API endpoint**フィールドに入力します。**REST Endpoint**列の値をコピーし、SalesWingsの**Braze Integration**セクションにある**Braze API endpoint**フィールドに入力します。

次に、**Save**を選択します。

### ステップ4: SalesWingsのインサイトをBrazeにプッシュできるようにする（オプション） {#step-4-enable-saleswings-insights-push-to-braze-optional}

セグメンテーション、パーソナライゼーション、またはキャンバスジャーニーのオーケストレーションのために、BrazeユーザープロファイルでSalesWingsインサイトを利用できるようにしたい場合は、[**SalesWings Integrations**ページ](https://helium.saleswings.pro/integrations)にアクセスし、**Braze Integration**セクションを展開してください。

**SalesWings-to-Braze insights data push**の下にある**Start data push**をクリックします。

### ステップ5: SalesWingsへのCurrentsカスタムエクスポートの設定（オプション） {#step-5-set-up-a-custom-currents-export-to-saleswings-optional}

[ユーザー行動]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)や[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)のイベントを、行動インテリジェンス、リードやアカウントのスコアリング、セールスインサイトの作成、CRMでのレポート作成に使用したい場合は、[**SalesWings Integrations**ページ](https://helium.saleswings.pro/integrations)に移動し、**Braze Integration**セクションを展開します。

**Generate an API token to setup a Custom Currents Export**の下にある**Generate**を選択します。

次に、[Currentを新規作成し]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/)、Currentタイプとして**Custom Currents Export**を選択します。

Current作成フォームの**Credentials**セクションで、[**SalesWings Integrations**ページ](https://helium.saleswings.pro/integrations)で生成したAPIトークンを**Bearer Token**に、`https://helium.saleswings.pro/api/braze/currents/events`を**Endpoint**に入力します。

### ステップ6: Braze用のSalesWingsリードおよびアカウントスコアリング、CRM統合などを設定する {#step-6-configuring-saleswings-lead-and-account-scoring-for-braze-crm-integration-and-more}

完全なオンボーディングサポートについては、[Webサイト](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs)からSalesWingsのサービスチームにお問い合わせください。

## この統合を使う {#using-this-integration}

行動データやその他のデータをリードやアカウントに紐付けるためには、SalesWingsがWebサイトやアプリで、またはサードパーティの統合を通じて、ユーザーを識別する必要があります。これは次の方法で行われます。

- **フォームの送信:** ユーザーがWebフォームを送信すると、SalesWingsはすべてのWebフォームタイプ（ログイン、ダウンロード、お問い合わせなど）を自動的に識別し、フォームの送信時にユーザーの身元を特定します。
- **Braze IDまたはexternal IDを持つURLクリック:** ユーザーがBrazeのマーケティングアクション（通常、メールクリック、バナークリックなど）をクリックし、SalesWingsでトラッキングしているページに誘導されます。
- **Braze Currentsイベント（オプション）:** カスタムCurrentsのSalesWingsへのエクスポートが設定されている場合、SalesWingsは、Currentに送信されるイベントを持つメールアドレス付きのすべてのBrazeユーザーに対して識別済みプロファイルを作成します。
- **GmailとOutlookのプラグインによるセールスメールのトラッキング（オプション）:** 営業担当者にメール追跡プラグインを導入すれば、追跡可能なリンクを送信することで、ユーザーの完全なWebサイトトラッキングが可能になります。
- **セグメント.com識別イベント（オプション）:** セグメント.comユーザーの場合は、セグメント.comの統合でユーザーの身元を特定することもできます。

### URLクリックからユーザーを特定する {#identifying-users-from-url-clicks}

追跡可能なURL（例えば、メール一斉送信やURL付きバナー）をクリックしたユーザーを自動的に特定できます。URLを追跡可能にするには、メール、バナー、SMSでWebサイトのURLを修正する2つの方法があり、リンクの末尾にパラメータとIDを追加します。

1. `?braze_id=`の後に{% raw %}`{{${braze_id}}}`{% endraw %}を付加する
  - **リンクの例:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. `?br_user_id=`の後に{% raw %}`{{${user_id}}}`{% endraw %}を付加する
  - **リンクの例:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

`braze_id`変数には、Brazeにより生成されたユーザーの識別子が設定されます。この変数はいつでも使用できます。`br_user_id`変数には、システム内のユーザーの識別子が設定されます。この変数は、特定の状況（Braze SDKにより作成された匿名ユーザーなど）では使用されない可能性があります。リンクに`braze_id`と`br_user_id`の両方が使用されている場合、SalesWingsは`braze_id`パラメータのみを考慮します。

### SalesWingsのインサイトをBrazeにプッシュする {#pushing-saleswings-insights-to-braze}

BrazeへのSalesWingsインサイトプッシュを有効にすると、SalesWingsは以下の[カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/)でBrazeユーザープロファイルを更新します。

| カスタム属性 | タイプ | 説明 |
| ----------- | ----------- | ----------- |
| `sw_favorite` | ブール値 | リードがSalesWingsまたはSalesforce CRMでお気に入りとしてマークされているかどうか |
| `sw_last_active_at` | date | リードがWebサイトで最後に活動した時点 |
| `sw_lead_link_open` | 文字列 | SalesWingsのリードプロファイルにアクセスするためのリンク（SalesWingsのダッシュボードアカウントなし） |
| `sw_lead_link_protected` | 文字列 | SalesWingsのリードプロファイルにアクセスするためのリンク（SalesWingsのダッシュボードアカウントが必要） |
| `sw_lead_owner` | 文字列 | SalesWingsまたはSalesforce CRMでリードに設定された所有者 |
| `sw_lead_score` | float | SalesWings[ルールエンジン](https://helium.saleswings.pro/falcon)で設定されたメインのSalesWingsリードスコアの値 |
| `sw_predictive_score` | 文字列 | SalesWingsの[予測スコア](https://support.saleswingsapp.com/en/articles/581795-the-predictive-lead-score)の値で、トラッキングされたアクティビティの回数と新しさに基づいてリードのエンゲージメントを評価します。設定可能な値は`HOT`、`WARM`、`NORMAL`、`COLD`または`FROZEN`です |
| `sw_salesforce_record_id` | 文字列 | Salesforce CRMのリードまたはコンタクトレコードのID |
| `sw_salesforce_record_url` | 文字列 | Salesforce CRMのリードまたはコンタクトレコードのURL |
| `sw_session_count` | 整数 | このリードのWebサイトでのトラッキングセッション数 |
| `sw_tags` | 文字列の配列 | SalesWingsが識別したニーズと興味で、「タグ」として表されます。このリードに適用される、SalesWings[ルールエンジン](https://helium.saleswings.pro/falcon)で設定されたSalesWingsタグの名前です |
| その他のリードスコア属性 | float | SalesWings[ルールエンジン](https://helium.saleswings.pro/falcon)で設定された追加のリードスコアごとに1つのカスタム属性。属性名はSalesWingsのスコア名から派生します。例えば、`Likeliness to meet`というスコアはカスタム属性`sw_likeliness_to_meet`として送信されます。スコアの作成後に名前を変更した場合、SalesWingsは最初のカスタム属性名で同期を継続します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

プッシュを有効にすると、SalesWingsのリードプロファイルで基礎となるデータポイントが変更されると、SalesWingsは即座にBrazeへのカスタム属性の送信を開始し、新しい更新がなくても、すべての既存リードを徐々に同期します。

SalesWingsは、SalesWingsのリードプロファイルのメールアドレスと一致するメールを持つすべてのBrazeユーザーを更新します。Brazeに一致するユーザーがいない場合、SalesWingsは新しいユーザーを作成しません。

### CRMでBraze Currentsイベントを使用する {#using-braze-currents-events-in-your-crm}

Braze CurrentをSalesWingsに接続すると、SalesWingsは、メールアドレスを持つすべてのBrazeユーザーの識別済みリードプロファイルを作成し、サポートされているBrazeイベントをリードアクティビティとして記録します。CRMでは、すべてのデータをリードのアカウントレベルで自動的に集計できます。記録されたアクティビティやデータは、SalesWingsのトラッキングスクリプトやセグメント.comで収集された行動データ、または他のデータをSalesWings APIに送信することで、さらに組み合わせることができます。また、見込み顧客のニーズや購入意欲を特定し、リードおよびアカウント管理プロセスに活用できます。

次の表は、SalesWingsがサポートするBrazeイベントタイプと、SalesWingsのリードアクティビティ履歴およびルールエンジンにおけるそれらの表現を示します。

| イベントカテゴリー | イベントタイプ | SalesWingsのイベント名 |
| ----------- | ----------- | ----------- |
| キャンバスイベント | エントリー | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| 顧客行動イベント | カスタムイベント | `[Custom Event tracked] $name` |
| 顧客行動イベント | 初回セッション | `[User Action] Today marks the user's first session` |
| 顧客行動イベント | インストールアトリビューション | `[User Action] User installed app from $source` |
| 顧客行動イベント | 購入イベント | `[Purchase] Customer purchased $product_id for $price $currency` |
| メッセージイベント | コンテンツカードのクリック | `[Content Card engagement] Clicked on $campaign_name content card` |
| メッセージイベント | メールバウンス | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| メッセージイベント | メールのクリック | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| メッセージイベント | メール配信 | `[Nurturing] Received email $campaign_name` |
| メッセージイベント | メール開封 | `[Email campaign engagement] Opened email $campaign_name` |
| メッセージイベント | メールの配信停止 | `[Subscription status change] Unsubscribed from $campaign_name` |
| メッセージイベント | アプリ内メッセージのクリック | `[In-app campaign engagement] Clicked on message $campaign_name` |
| メッセージイベント | プッシュオープン | `[Push notification engagement] Clicked on notification $campaign_name` |
| メッセージイベント | SMS/MMSインバウンド受信 | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| メッセージイベント | SMS/MMS短縮リンクのクリック | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| メッセージイベント | WhatsAppインバウンド受信 | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| メッセージイベント | WhatsApp既読 | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| サブスクリプション | グローバルサブスクリプションステータスの変更 | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| サブスクリプション | サブスクリプショングループステータスの変更 | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

次に、上の表のSalesWingsイベント名に対して、SalesWingsタグおよびスコアの**カスタムイベント** > **イベント名**および**カスタムイベント** > **イベントプロパティ**条件を設定できます。条件に対して使用可能なイベントプロパティのリストは、よく使用されるエントリがあらかじめ入力されており、[ルールエンジン設定ページ](https://helium.saleswings.pro/falcon)の**イベントプロパティ**セクションでいつでも新しいものを追加できます。

![イベント名の条件例]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

設定とトラブルシューティングの詳細については、[SalesWingsサービスチーム](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs)に連絡して、オンボーディングサポートを受けてください。