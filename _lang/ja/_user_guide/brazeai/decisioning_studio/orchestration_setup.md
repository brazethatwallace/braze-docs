---
nav_title: オーケストレーションの設定
article_title: オーケストレーションの設定
page_order: 4
page_type: reference
description: "この記事では、BrazeAI Decisioning Studioのオーケストレーション設定方法について説明します。CEPの選択、必要な認証情報の収集、統合の構成などを含みます。"
toc_headers: h2
---

# オーケストレーションの設定 {#set-up-orchestration}

> AI意思決定エージェントは、顧客データを取り込み1:1レベルでパーソナライズした後、コミュニケーションをオーケストレーションするためにカスタマーエンゲージメントプラットフォーム（CEP）に接続する必要があります。この記事では、準備に必要なものと、サポートされている各CEPの統合を構成する方法について説明します。

## オーケストレーションとは {#what-is-orchestration}

オーケストレーションとは、Decisioning Studioとカスタマーエンゲージメントプラットフォーム（CEP）間の接続です。AI意思決定エージェントが各顧客に最適なアクションを決定すると、オーケストレーションがCEPを通じてパーソナライズされたコミュニケーションをトリガーすることで、その決定を実行します。

次のように考えてください：

- **Decisioning Studio**は*何を*送信するか、*いつ*送信するかを決定します
- **CEP**は*どのように*送信するかを処理します

## CEPの選択 {#choose-your-cep}

最初のステップは、Decisioning Studioで使用するCEPを選択することです。選択によって、設定の複雑さと利用可能な機能が異なります。

### サポートされているCEP {#supported-ceps}

| CEP | 統合タイプ | 設定の複雑さ |
|-----|-----------------|------------------|
| **Braze** | ネイティブAPI統合（推奨） | 低 |
| **Salesforce Marketing Cloud** | APIイベント + Journey Builder | 中 |
| **その他のCEP** | カスタム（レコメンデーションファイル） | 高 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Supported CEPs" }

{% alert tip %}
すでにBrazeをCEPとして使用している場合は、最もスムーズな設定体験のためにネイティブBraze統合を使用することをお勧めします。
{% endalert %}

## 前提条件 {#prerequisites}

オーケストレーションを設定する前に、選択したCEPに基づいて以下の項目を準備してください。

{% tabs %}
{% tab Braze %}

| 要件 | 説明 |
|------|-------------|
| **REST APIキー** | ユーザーデータ、メッセージ、キャンペーン、キャンバス、セグメント、テンプレートの権限を持つ新しいAPIキー。 |
| **BrazeダッシュボードURL** | BrazeインスタンスURL（例：`https://dashboard-01.braze.com`）。 |
| **アプリID** | トラッキングしたいアプリに関連付けられたAPIキー（**設定** > **アプリ設定**で確認できます）。 |
| **メール表示名とアドレス** | キャンペーンに使用する送信者情報（**設定** > **メール設定**で確認できます）。 |
| **ベーステンプレート** | エージェントがオーケストレーションに使用するメッセージテンプレート。各テンプレートに対してAPIトリガーキャンペーンを作成します。 |
| **テストユーザーID** | 起動前に統合をテストするためのユーザーID。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| 要件 | 説明 |
|------|-------------|
| **アプリパッケージ認証情報** | サーバー間API統合を持つインストール済みパッケージからのクライアントID、クライアントシークレット、認証ベースURI、RESTベースURI、SOAPベースURI。 |
| **API権限** | チャネル、アセット、オートメーション、ジャーニー、コンタクト、データエクステンション、トラッキングイベントのスコープ。 |
| **データエクステンション** | サブスクライバーデータ、エンゲージメントデータ、レコメンデーション用のデータエクステンションが必要です。 |
| **メールテンプレート** | Decisioning Studioで使用するテンプレートと、各テンプレートのテンプレートID。 |
| **Journey Builderアクセス** | APIイベントエントリソースを使用したマルチステップジャーニーの作成とアクティベーションへのアクセス。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% endtab %}
{% tab その他のCEP %}

BrazeまたはSalesforce Marketing Cloud以外のCEPを使用している場合、Decisioning Studioはレコメンデーションファイルアプローチを通じて統合できます：

| 項目 | 説明 |
|------|-------------|
| **データ取り込み機能** | CEPは、各顧客のパーソナライズされた決定を含むレコメンデーションファイル（通常CSVまたはJSON）を取り込める必要があります。 |
| **ダイナミックコンテンツサポート** | キャンペーンはレコメンデーションデータに基づいてフィールドを動的に入力できる必要があります。 |
| **カスタムエンジニアリングリソース** | チームがレコメンデーションファイルを読み取り、コミュニケーションをトリガーする統合を構築する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% endtab %}
{% endtabs %}

## キャンペーンの計画 {#plan-your-campaigns}

オーケストレーションを設定する前に、以下の詳細を検討してください：

### ベーステンプレート {#base-templates}

ベーステンプレートとは、AI意思決定エージェントが使用する可能性のあるメッセージテンプレートです。以下を検討してください：

- **テンプレートの数は？** エージェントは1つのテンプレートでも複数のテンプレートでも動作できます。複数の場合、エージェントは各顧客が受け取るテンプレートをパーソナライズできます。
- **どのチャネル？** メール、プッシュ、SMS、またはそれらの組み合わせです。各チャネルには個別のテンプレートとキャンペーンが必要になる場合があります。
- **どのダイナミック要素？** エージェントがパーソナライズするメッセージの部分（件名、CTA、オファー、タイミングなど）を特定します。これらはAPIトリガープロパティまたはダイナミックプレースホルダーになります。

### 再適格性設定 {#re-eligibility-settings}

キャンペーンでは、ユーザーが複数回メッセージを受信できるようにする必要があります：

- テスト時には、同じキャンペーンを同じユーザーに繰り返し送信する必要があります
- 本番環境では、エージェントが連続する日に同じキャンペーンがユーザーにとって最適であると判断する場合があります

{% alert note %}
テスト用に再適格性を設定する場合でも、Decisioning Studioエージェントはフリークエンシーキャップを尊重するように設計されており、本番環境では同じキャンペーンを1日に1回以上ユーザーに送信することはありません。
{% endalert %}

### APIトリガープロパティ {#api-trigger-properties}

Braze統合の場合、エージェントが最適化するディメンションを計画します。これらはキャンペーンにダイナミックな値を渡すAPIトリガープロパティになります：

| ディメンションの例 | APIトリガープロパティ |
|-------------------|---------------------|
| 件名 | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| コールトゥアクション | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| オファー | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| 割引額 | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API trigger properties" }

## 統合の設定 {#integration-setup}

以下からCEPを選択して、統合の設定を開始してください。

{% tabs %}
{% tab Braze %}

## Braze統合の設定 {#set-up-braze-integration}

以下の手順に従って、Decisioning StudioエージェントをBrazeのオーケストレーション機能と統合します（Brazeのサービスチームがサポートいたします）：

### ステップ 1: APIキーの作成 {#step-1-create-an-api-key}

**設定** > **APIキー**に移動し、以下の権限を持つ新しいキーを作成します：

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### ステップ 2: APIトリガーキャンペーンの設定 {#step-2-set-up-api-triggered-campaigns}

各ベーステンプレートに対して、すべての最適化ディメンションのAPIトリガープロパティを含むAPIトリガーキャンペーンを設定します。

ベーステンプレートとは、AI意思決定エージェントがメッセージのオーケストレーションに使用する可能性のあるテンプレートです。AI意思決定エージェントは1つのベーステンプレートを持つ場合も複数を持つ場合もあり、複数の場合は各顧客に適切なベーステンプレートを選択することがエージェントのパーソナライズする決定の1つになります。

### ステップ 3: 再適格性の構成 {#step-3-configure-re-eligibility}

すべてのAPIトリガーキャンペーンで、ユーザーが15分以内に再適格になるように設定します。

![Decisioning Studioのフリークエンシーキャップ設定図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Decisioning Studioエージェントは同じキャンペーンを1日に1回以上送信することはありませんが、テスト目的で同じキャンペーンを1日に複数回送信できるようにしておく必要があります。
{% endalert %}

### ステップ 4: ダイナミックプレースホルダーの追加 {#step-4-add-dynamic-placeholders}

これらは、Decisioning Studioエージェントが最適化する決定のダイナミックプレースホルダーとして機能します。

#### 例1：メールキャンペーン {#example-1-email-campaign}

Decisioning Studioエージェントがメールキャンペーンを最適化しているとします。次のように構成される場合があります：

![Decisioning Studioのメール設定例1]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

エージェントがテンプレートの選択とコールトゥアクション（CTA）メッセージを最適化している場合、各テンプレートに対してAPIトリガーキャンペーンを作成し、1つのテンプレートのCTAセクションは次のようになります：

![Decisioning StudioのメールCTA設定例2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### 例2：プッシュキャンペーン {#example-2-push-campaign}

Decisioning Studioエージェントがプッシュキャンペーンのメッセージを最適化しているとします。次のように構成される場合があります：

![Decisioning Studioのプッシュ設定例1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Decisioning Studioのプッシュ設定例2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

結果として次のメッセージが表示されます：

![Decisioning Studioのプッシュメッセージ結果例3]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### 例3：SMS キャンペーン {#example-3-sms-campaign}

Decisioning StudioエージェントがSMS キャンペーンのフィールドを最適化しているとします。次のように構成される場合があります：

![Decisioning StudioのSMS設定例1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Decisioning StudioのSMS設定例2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

結果として次のメッセージが表示されます：

![Decisioning StudioのSMSメッセージ結果例3]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC統合の設定 {#set-up-sfmc-integration}

Decisioning StudioはSalesforce Marketing Cloudとのネイティブ統合をサポートしています。Decisioning Studioは、ダイナミック要素を入力するために必要なデータを含むAPIイベントをジャーニーにトリガーします。

SFMC統合を構成する詳細な手順については、Decisioning Studio Goドキュメントの[SFMC手順]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)を参照してください。

{% endtab %}
{% tab その他のCEP %}

## その他のCEP統合の設定 {#set-up-other-cep-integrations}

Decisioning Studioは任意のカスタマーエンゲージメントプラットフォームと統合できます。ただし、Decisioning Studioはコミュニケーションを直接トリガーできないため、チームによるカスタムエンジニアリング作業が必要になる場合があります。

このシナリオでは、エージェントは「レコメンデーションファイル」を配信します。このファイルには各顧客の行が含まれ、その顧客に対するすべてのパーソナライズされた決定を示す列があります。

例えば、次のレコメンデーションファイル：

![Decisioning Studioのカスタム統合レコメンデーションファイル例]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

次のようなメールキャンペーンを最適化するために使用される場合があります：

![Decisioning Studioのカスタム統合メール例]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## ベストプラクティス {#best-practices}

オーケストレーションの準備にあたって、以下のベストプラクティスを念頭に置いてください：

1. **狭い範囲から始めましょう。** まず1つのチャネルと1〜2つのテンプレートを使用します。何が効果的かを学んでから拡張できます。
2. **徹底的にテストしましょう。** 起動前に、少数のユーザーセットで統合をテストし、ダイナミックコンテンツが正しく入力されることを確認します。
3. **設定を文書化しましょう。** キャンペーン ID、テンプレートID、APIキー、その他の識別子を記録しておきます。Decisioning Studioポータルでこれらを参照する必要があります。
4. **チームと連携しましょう。** オーケストレーションの設定には、マーケティング、エンジニアリング、データチームが関与する場合があります。プロセスにおける各自の役割を全員が理解していることを確認してください。
5. **フィードバックデータを計画しましょう。** オーケストレーションにはメッセージの送信と、エージェントの学習に役立つエンゲージメントおよびコンバージョンデータの収集が含まれます。詳細については、[データの準備]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/)を参照してください。

## 次のステップ {#next-steps}

オーケストレーションの設定後、エージェントの設計に進みます：

- [AI意思決定エージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents/)