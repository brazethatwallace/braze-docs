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

BrazeとAmazon Bedrockの連携により、Amazon Bedrockの認証情報をBrazeに接続して、カスタムAIエージェントを構築する際にBedrockでホストされたモデルを使用できます。この連携により、エージェントはAmazon Bedrockを通じて利用可能なモデルを使用して、パーソナライズされたコピーの生成、リアルタイムの意思決定、カタログフィールドの更新を行うことができます。

Amazon Bedrockを接続すると、Brazeはカスタムエージェント向けにキュレートされたBedrockモデルのセットを表示します。Brazeで利用可能なモデルは、AWSアカウントの完全なカタログとは異なる場合があります。

Brazeはこの連携にAmazon Bedrockの`bedrock-mantle`エンドポイントを使用します。Amazon Bedrockには、異なるモデルと機能をサポートする別の`bedrock-runtime`エンドポイントも文書化されています。そのため、AWSドキュメントで可用性や動作を確認する際は、[`bedrock-mantle`](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html)のガイダンスに従ってください。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Amazon Bedrock にアクセスできる AWS アカウント | モデルがホストされている AWS リージョンで Amazon Bedrock にアクセスできる AWS アカウント。サポートが必要な場合は、管理者または [AWS サポート](https://aws.amazon.com/support)にお問い合わせください。 |
| Amazon Bedrock モデルへのアクセス | 使用予定の Bedrock モデルへの AWS アカウントでのアクセス。Anthropic のモデルなど、一部のモデルでは AWS アカウントでアクセスの許可が必要です。すべてのモデルがすべての AWS リージョンで利用できるわけではありません。接続する前に、Amazon Bedrock コンソールまたは[モデル別のリージョン対応状況](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html)で各モデルのリージョン対応状況を確認してください。 |
| 認証情報 | 長期の [Amazon Bedrock API キー](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html)、またはワークスペースで IAM ロール認証が有効になっている場合は Braze が引き受けることができる IAM ロール。 |
| Braze インスタンス | Braze インスタンスは [API 概要ページ]({{site.baseurl}}/api/basics#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

Amazon BedrockをBrazeに接続するには：

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Amazon Bedrock**を検索して選択します。
2. **認証方法**で、**APIキー**または**AWS IAMロール**（利用可能な場合）を選択します。
3. 選択した方法に応じて設定を完了します：
   - **APIキー：** 長期**Amazon Bedrock APIキー**を入力します。Bedrockモデルがホストされている**AWSリージョン**を選択します。**保存**を選択します。
   - **AWS IAMロール：** Brazeに表示される値を使用してIAMロールの信頼ポリシーを設定し、Brazeにロールの詳細を入力します：
     1. **Braze AWSアカウントID**をコピーし、IAMロールの信頼ポリシーでそのアカウントを信頼します。
     2. **Braze external ID**をコピーし、ロールの信頼ポリシーで`sts:ExternalId`条件として要求します。新しい値が必要な場合は、**新しいexternal IDを生成**を選択します。
     3. Amazon Bedrockの権限を持つIAMロールの**AWSロールARN**を入力します。ARNは`arn:aws:iam::<account-id>:role/<role-name>`と一致する必要があります。
     4. Bedrockモデルがホストされている**AWSリージョン**を選択します。
     5. **保存**を選択します。

{% alert note %}
**AWS IAMロール**は、この認証オプションが有効になっているワークスペースでのみ表示されます。IAMロール認証では、Brazeがロールを引き受けて短期間有効なAmazon Bedrock認証情報を生成するため、長期APIキーは保存されません。
{% endalert %}

保存すると、Brazeに接続ステータスと接続日時が表示されます。エージェントコンソールで[カスタムエージェントを作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)する際に、Amazon Bedrockモデルを選択できます。

{% alert important %}
すべてのAmazon Bedrockモデルがすべての AWSリージョンで利用できるわけではありません。Brazeで**AWSリージョン**を選択する前に、Amazon Bedrockでモデルの詳細を開き、そのモデルが該当リージョンに対応していることを確認してください。接続されたリージョンで利用できないモデルは、エージェント呼び出し時にエラーを返します（例：モデルが存在しない、またはモデルが利用できなくなったなど）。詳細については、[モデル一覧](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html)を参照してください。
{% endalert %}

連携が正常に動作していることを確認するには、エージェントコンソールに移動し、Bedrockモデルのいずれかを使用してテストエージェントを作成します。「ジョークを教えて」などの指示を入力し、テスト呼び出しを実行してモデルが期待どおりに応答することを確認します。

連携を解除するには、**Amazon Bedrock連携**ページで**切断**を選択します。

Amazon Bedrockアカウントまたは認証情報に関する問題については、[AWSサポート](https://aws.amazon.com/support)にお問い合わせください。