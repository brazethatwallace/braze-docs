---
nav_title: オーケストレーションの設定
article_title: オーケストレーションの設定
page_order: 4
page_type: reference
description: "この記事では、BrazeAI Decisioning Studioのオーケストレーション設定方法について説明します。CEPの選択、必要な認証情報の収集、統合の構成などを含みます。"
toc_headers: h2
---

# オーケストレーションの設定 {#set-up-orchestration}

> 意思決定エージェントは、顧客データを取り込み1:1レベルでパーソナライズした後、コミュニケーションをオーケストレーションするためにカスタマーエンゲージメントプラットフォーム（CEP）に接続する必要があります。この記事では、準備に必要なものと、サポートされている各CEPの統合を構成する方法について説明します。

## オーケストレーションとは？ {#what-is-orchestration}

オーケストレーションとは、Decisioning Studioとカスタマーエンゲージメントプラットフォーム（CEP）の間の接続のことです。意思決定エージェントが各顧客に最適なアクションを決定すると、オーケストレーションはCEPを通じてパーソナライズされたコミュニケーションをトリガーすることで、その決定を実行します。

次のように考えてください：

- **Decisioning Studio**は、*何を*送信するか、*いつ*送信するかを決定します
- **CEP**は、*どのように*送信するかを処理します

## CEPを選択する {#choose-your-cep}

最初のステップは、Decisioning Studioで使用するCEPを選択することです。選択によって、設定の複雑さと利用可能な機能が異なります。

### サポートされているCEP {#supported-ceps}

| CEP | 連携タイプ | 設定の複雑さ |
|-----|-----------------|------------------|
| **Braze** | ネイティブAPI連携（推奨） | 低 |
| **Salesforce Marketing Cloud** | APIイベント + Journey Builder | 中 |
| **その他のCEP** | カスタム（レコメンデーションファイル） | 高 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされているCEP" }

{% alert tip %}
すでにBrazeをCEPとして使用している場合は、最もスムーズな設定体験のために、ネイティブのBraze連携を使用することをお勧めします。
{% endalert %}

## 前提条件 {#prerequisites}

オーケストレーションを設定する前に、選択したCEPに基づいて以下の項目を準備してください。

{% tabs %}
{% tab Braze %}

| 要件 | 説明 |
|------|-------------|
| **REST APIキー** | ユーザーデータ、メッセージ、キャンペーン、キャンバス、セグメント、テンプレートの権限を持つ新しいAPIキー。 |
| **Brazeダッシュボード URL** | BrazeインスタンスのURL（例：`https://dashboard-01.braze.com`）。 |
| **アプリ ID** | トラッキングしたいアプリに関連付けられたAPIキー（**設定** > **アプリ設定**で確認できます）。 |
| **メール表示名とアドレス** | キャンペーンに使用する差出人情報（**設定** > **メール設定**で確認できます）。 |
| **ベーステンプレート** | エージェントがオーケストレーションに使用するメッセージテンプレート。各テンプレートに対してAPIトリガーキャンペーンを作成します。 |
| **テストユーザー ID** | ローンチ前にインテグレーションをテストするためのユーザー ID。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| 要件 | 説明 |
|------|-------------|
| **アプリパッケージ認証情報** | サーバー間APIインテグレーションを持つインストール済みパッケージのClient ID、Client Secret、Authentication Base URI、REST Base URI、SOAP Base URI。 |
| **API権限** | チャネル、アセット、オートメーション、ジャーニー、コンタクト、データエクステンション、トラッキングイベントのスコープ。 |
| **データエクステンション** | サブスクライバーデータ、エンゲージメントデータ、レコメンデーション用のデータエクステンションが必要です。 |
| **メールテンプレート** | Decisioning Studioで使用するテンプレートと、各テンプレートのテンプレートID。 |
| **Journey Builderアクセス** | APIイベントエントリソースを使用したマルチステップジャーニーを作成・有効化するためのアクセス権。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% endtab %}
{% tab その他のCEP %}

BrazeまたはSalesforce Marketing Cloud以外のCEPを使用している場合、Decisioning Studioはレコメンデーションファイルアプローチを通じてインテグレーションできます。

| 項目 | 説明 |
|------|-------------|
| **データ取り込み機能** | CEPが、各顧客向けのパーソナライズされた意思決定を含むレコメンデーションファイル（通常はCSVまたはJSON）を取り込める必要があります。 |
| **ダイナミックコンテンツサポート** | キャンペーンがレコメンデーションデータに基づいてフィールドをダイナミックに入力できる必要があります。 |
| **カスタム開発リソース** | レコメンデーションファイルを読み取り、コミュニケーションをトリガーするインテグレーションを構築するためのチームリソースが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% endtab %}
{% endtabs %}

## キャンペーンを計画する {#plan-your-campaigns}

オーケストレーションを設定する前に、以下の詳細を検討してください。

### ベーステンプレート {#base-templates}

ベーステンプレートとは、意思決定エージェントが使用する可能性のあるメッセージテンプレートのことです。以下を検討してください。

- **テンプレートの数は？** エージェントは1つのテンプレートでも複数のテンプレートでも動作します。複数の場合、エージェントは各顧客が受け取るテンプレートをパーソナライズできます。
- **どのチャネルを使用しますか？** メール、プッシュ、SMS、またはそれらの組み合わせです。チャネルごとに個別のテンプレートとキャンペーンが必要になる場合があります。
- **どのダイナミックな要素がありますか？** エージェントがパーソナライズするメッセージの部分（件名、CTA、オファー、タイミングなど）を特定してください。これらはAPIトリガープロパティまたはダイナミックプレースホルダーになります。

### 再エントリ設定 {#re-eligibility-settings}

キャンペーンでは、ユーザーが複数回メッセージを受信できるように設定する必要があります。

- テスト時には、同じキャンペーンを同じユーザーに繰り返し送信します
- 本番環境では、エージェントが連続する日にわたって同じキャンペーンがユーザーにとって最適であると判断する場合があります

{% alert note %}
テスト用に再エントリを設定する場合でも、Decisioning Studioエージェントはフリークエンシーキャップを遵守するように設計されており、本番環境では同じキャンペーンを1日に1回以上同じユーザーに送信することはありません。
{% endalert %}

### APIトリガープロパティ {#api-trigger-properties}

Brazeとの連携では、エージェントが最適化するディメンションを計画してください。これらはAPIトリガープロパティとなり、ダイナミックな値をキャンペーンに渡します。

| ディメンションの例 | APIトリガープロパティ |
|-------------------|---------------------|
| 件名 | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| コールトゥアクション | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| オファー | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| 割引額 | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="APIトリガープロパティ" }

## 連携の設定 {#integration-setup}

このリストからお使いのカスタマーエンゲージメントプラットフォームを選択して、連携の設定を開始してください。

{% tabs %}
{% tab Braze %}

## Braze連携の設定 {#set-up-braze-integration}

Decisioning StudioエージェントをBrazeのオーケストレーション機能と連携するには、以下のステップに従ってください（Brazeのサービスチームがサポートいたします）。

### ステップ1：APIキーを作成する {#step-1-create-an-api-key}

**設定** > **APIキー**に移動し、以下の権限を持つ新しいキーを作成します。

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### ステップ2：APIトリガーキャンペーンを設定する {#step-2-set-up-api-triggered-campaigns}

各ベーステンプレートに対して、最適化するすべてのディメンションのAPIトリガープロパティを含むAPIトリガーキャンペーンを設定します。

ベーステンプレートとは、意思決定エージェントがメッセージのオーケストレーションに使用する可能性のあるテンプレートのことです。意思決定エージェントは1つのベーステンプレートを持つ場合もあれば、複数持つ場合もあります。複数の場合、各顧客に適切なベーステンプレートを選択することが、エージェントがパーソナライズする意思決定の1つとなります。

### ステップ3：再適格性を設定する {#step-3-configure-re-eligibility}

すべてのAPIトリガーキャンペーンで、ユーザーが15分以内に再適格になるように設定してください。

![Decisioning Studioの頻度キャップ設定図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Decisioning Studioエージェントは同じキャンペーンを1日に2回以上送信することはありませんが、テスト目的で同じキャンペーンを1日に複数回送信できるようにしておく必要があります。
{% endalert %}

### ステップ4：ダイナミックプレースホルダーを追加する {#step-4-add-dynamic-placeholders}

これらは、Decisioning Studioエージェントが最適化する意思決定のダイナミックプレースホルダーとして機能します。

#### 例1：メールキャンペーン {#example-1-email-campaign}

Decisioning Studioエージェントがメールキャンペーンを最適化するとします。次のように設定できます。

![メールキャンペーンの設定例]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

エージェントがテンプレートの選択とコールトゥアクション（CTA）メッセージを最適化する場合、各テンプレートに対してAPIトリガーキャンペーンを作成し、1つのテンプレートのCTAセクションは次のようになります。

![メールテンプレートのCTAセクション例]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### 例2：プッシュキャンペーン {#example-2-push-campaign}

Decisioning Studioエージェントがプッシュキャンペーンのメッセージを最適化するとします。次のように設定できます。

![プッシュキャンペーンの設定例1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![プッシュキャンペーンの設定例2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

結果として、次のようなメッセージが生成されます。

![プッシュキャンペーンの結果メッセージ例]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### 例3：SMSキャンペーン {#example-3-sms-campaign}

Decisioning StudioエージェントがSMSキャンペーンのフィールドを最適化するとします。次のように設定できます。

![SMSキャンペーンの設定例1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![SMSキャンペーンの設定例2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

結果として、次のようなメッセージが生成されます。

![SMSキャンペーンの結果メッセージ例]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC連携の設定 {#set-up-sfmc-integration}

Decisioning StudioはSalesforce Marketing Cloudとのネイティブ連携をサポートしています。Decisioning Studioは、ダイナミック要素を入力するために必要なデータを含むAPIイベントをジャーニーにトリガーします。

{% alert important %}
ユースケースを設定する際、**API IDは大文字で入力する必要があります**。これにはジャーニーID、キャンペーンID、およびその他すべての識別子が含まれます。API IDを小文字で入力し、SFMCデータに大文字のUUIDが含まれている場合、イベントフィルターが一致せず、レポートの指標が正しく表示されません。
{% endalert %}

{% endtab %}
{% tab その他のCEP %}

## その他のCEP連携の設定 {#set-up-other-cep-integrations}

Decisioning Studioはあらゆるカスタマーエンゲージメントプラットフォームと連携できます。ただし、Decisioning Studioはコミュニケーションを直接トリガーできないため、チームによるカスタム開発作業が必要になる場合があります。

このシナリオでは、エージェントは「レコメンデーションファイル」を配信します。このファイルには各顧客の行が含まれ、その顧客に対するすべてのパーソナライズされた意思決定を示す列があります。

たとえば、次のようなレコメンデーションファイルがあるとします。

![レコメンデーションファイルの例]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

これを使用して、次のようなメールキャンペーンを最適化できます。

![最適化されたメールキャンペーンの例]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## ベストプラクティス {#best-practices}

オーケストレーションの準備にあたって、以下のベストプラクティスを念頭に置いてください。

1. **狭い範囲から始める：** まずは1つのチャネルと1～2つのテンプレートから始めましょう。効果がわかってきたら、後から拡張できます。
2. **十分にテストする：** 本番開始前に、少数のユーザーで統合をテストし、ダイナミックなコンテンツが正しく表示されることを確認してください。
3. **設定を記録する：** キャンペーンID、テンプレートID、APIキー、その他の識別子を記録しておきましょう。Decisioning Studioポータルで参照する際に必要になります。
4. **チームと連携する：** オーケストレーションの設定には、マーケティング、開発、データチームが関わることがあります。プロセスにおける各自の役割を全員が理解していることを確認してください。
5. **フィードバックデータを計画する：** オーケストレーションはメッセージを送信し、エージェントの学習に役立つエンゲージメントデータやコンバージョンデータを収集します。詳しくは[データを準備する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data)をご覧ください。

## 次のステップ {#next-steps}

オーケストレーションの設定が完了したら、エージェントの設計に進みます:

- [意思決定エージェントを設計する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)