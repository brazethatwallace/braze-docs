---
nav_title: Amazon Bedrock
article_title: Amazon Bedrock
description: "このリファレンス記事では、BrazeとAmazon Bedrockのパートナーシップについて説明します。このパートナーシップにより、BedrockモデルをカスタムAIエージェントで使用するためにBrazeに接続できます。"
alias: /partners/amazon_bedrock/
page_type: partner
search_tag: Partner

---

# Amazon Bedrock

> [Amazon Bedrock](https://aws.amazon.com/bedrock/) は、統合APIを通じて主要なAI企業の基盤モデルへのアクセスを提供するフルマネージドAWSサービスです。ブランドはAWS上で生成AIアプリケーションを構築・スケーリングできます。

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Amazon Bedrock integration' %}

## 連携について {#about-the-integration}

BrazeとAmazon Bedrockの連携により、Amazon Bedrockの認証情報をBrazeに接続し、カスタムAIエージェントを構築する際にBedrockでホストされたモデルを使用できます。この連携により、エージェントはパーソナライズされたコピーの生成、リアルタイムの意思決定、またはAmazon Bedrockを通じて利用可能なモデルを使用したカタログフィールドの更新を行えます。

Amazon Bedrockを接続すると、Brazeはカスタムエージェント用にキュレートされたBedrockモデルのセットを表示します。Brazeで利用可能なモデルは、AWSアカウントの完全なカタログとは異なる場合があります。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Amazon Bedrockアクセス付きのAWSアカウント | モデルがホストされているAWSリージョンでAmazon BedrockにアクセスできるAWSアカウント。ヘルプが必要な場合は、管理者または[AWSサポート](https://aws.amazon.com/support)にお問い合わせください。 |
| Amazon Bedrockモデルアクセス | 使用予定のBedrockモデルへのAWSアカウントでのアクセス。Anthropicのモデルなど、一部のモデルはAWSアカウントでアクセスを許可する必要があります。すべてのモデルがすべてのAWSリージョンで利用できるわけではありません。 |
| 認証情報 | 長期の[Amazon Bedrock APIキー](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html)、またはワークスペースでIAMロール認証が有効な場合はBrazeが引き受けることができるIAMロール。 |
| Brazeインスタンス | Brazeインスタンスは[API概要ページ]({{site.baseurl}}/api/basics#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

Amazon BedrockをBrazeに接続するには：

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Amazon Bedrock**を検索して選択します。
2. **認証方法**で、**APIキー**または**AWS IAMロール**（利用可能な場合）を選択します。
3. 選択した方法の設定を完了します：
   - **APIキー：** 長期の**Amazon Bedrock APIキー**を入力します。Bedrockモデルがホストされている**AWSリージョン**を選択します。**保存**を選択します。
   - **AWS IAMロール：** Brazeが表示する値を使用してIAMロールの信頼ポリシーを設定し、Brazeにロールの詳細を入力します：
     1. **Braze AWSアカウントID**をコピーし、IAMロールの信頼ポリシーでそのアカウントを信頼します。
     2. **Braze external ID**をコピーし、`sts:ExternalId`条件でロールの信頼ポリシーに要求します。新しい値が必要な場合は**新しいexternal IDを生成**を選択します。
     3. Amazon Bedrock権限を持つIAMロールの**AWSロールARN**を入力します。ARNは`arn:aws:iam::<account-id>:role/<role-name>`と一致する必要があります。
     4. Bedrockモデルがホストされている**AWSリージョン**を選択します。
     5. **保存**を選択します。

{% alert note %}
**AWS IAMロール**は、この認証オプションが有効になっているワークスペースでのみ表示されます。IAMロール認証では、Brazeがロールを引き受けて短期間有効なAmazon Bedrock認証情報を生成するため、長期のAPIキーは保存されません。
{% endalert %}

保存後、Brazeは接続のステータスと接続日時を表示します。エージェントコンソールで[カスタムエージェントを作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)する際に、Amazon Bedrockモデルを選択できます。

{% alert note %}
すべてのAmazon BedrockモデルがすべてのAWSリージョンで利用できるわけではありません。使用予定のモデルをサポートするリージョンを選択してください。接続されたリージョンで利用できないモデルは、エージェント呼び出し時にエラーを返します。
{% endalert %}

連携が正常に動作していることを確認するには、エージェントコンソールに移動し、Bedrockモデルの1つを使用してテストエージェントを作成します。「ジョークを教えて」などの指示を入力し、テスト呼び出しを実行してモデルが期待どおりに応答することを確認します。

連携を削除するには、**Amazon Bedrock連携**ページで**切断**を選択します。

Amazon Bedrockアカウントまたは認証情報に関する問題については、[AWSサポート](https://aws.amazon.com/support)にお問い合わせください。