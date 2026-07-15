---
nav_title: Microsoft Foundry
article_title: Microsoft Foundry
description: "このリファレンス記事では、BrazeとMicrosoft Foundryのパートナーシップについて説明します。この連携により、Foundryで管理されたAIモデルをBrazeに接続し、カスタムAIエージェントで使用できます。"
alias: /partners/microsoft_foundry/
page_type: partner
search_tag: Partner

---

# Microsoft Foundry

> [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry)は、エンタープライズAIオペレーション、モデルビルダー、アプリケーション開発のための統合Azureプラットフォーム・アズ・ア・サービスです。

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Microsoft Foundry integration' %}

## 連携について {#about-the-integration}

BrazeとMicrosoft Foundryの連携により、カスタムAIエージェントを構築する際に、Microsoft Foundryで管理された生成AIモデルを使用できます。現在、この連携ではgpt-5.4-miniとgpt-5.4-nanoの2つのモデルをサポートしています。この連携により、エージェントはパーソナライズ済みのコピーを生成したり、リアルタイムの意思決定を行ったり、Foundryで管理されたモデルを使用してカタログフィールドを更新したりできます。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| アクティブなサブスクリプションを持つAzureアカウント | ヘルプが必要な場合は、管理者に連絡するか、[Azureアカウントオプション](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)を参照してください。 |
| Microsoft Foundryインスタンス | プロジェクトを作成するためのMicrosoft Foundryインスタンスです。 |
| Microsoft Foundryプロジェクト | デプロイ済みモデルを格納するためのFoundryインスタンス内のプロジェクトです。 |
| デプロイ済みモデル | Foundryプロジェクト内にデプロイされたサポート対象モデルが少なくとも1つ必要です。 |
| Brazeインスタンス | Brazeインスタンスは[API概要ページ]({{site.baseurl}}/api/basics#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Foundryでサポート対象モデルをデプロイする {#deploy-supported-models-in-foundry}

BrazeとMicrosoft Foundryの連携では、gpt-5.4-miniとgpt-5.4-nanoの2つのモデルをサポートしています。両方のモデルを、連携するFoundryインスタンス内のFoundryプロジェクトにデプロイする必要があります。

Foundryプロジェクトを作成してモデルをデプロイするには、[Microsoft Foundryドキュメント](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal)に従ってください。

1. AzureポータルからMicrosoft Foundryにサインインします。
2. Microsoft Foundryで、Brazeと連携するモデルを格納するプロジェクトを作成します。
3. gpt-5.4-mini、gpt-5.4-nano、またはその両方を使用するかを決定します。
4. 使用する各モデルについて、Microsoft Foundryドキュメントに従ってデプロイします。デフォルトのデプロイ名を変更しないでください。変更すると、そのモデルの連携が正常に動作しなくなる可能性があります。

## 連携 {#integration}

FoundryインスタンスをBrazeに接続するには：

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Microsoft Foundry**を見つけます。
2. **Microsoft Foundry APIキー**を入力します。
3. **Microsoft Foundryインスタンス名**を入力します。これは`.services.ai.azure.com`の前のサブドメインです。
4. **保存**を選択します。

保存後、Brazeは接続日時とともに接続済みステータスを表示します。エージェントコンソールで[カスタムエージェントを作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)する際に、Foundryモデルを選択できます。

{% alert important %}
gpt-5.4-miniまたはgpt-5.4-nanoを使用するには、デフォルトのデプロイ名を変更せずに、各モデルをFoundryプロジェクトにデプロイする必要があります。
{% endalert %}

連携が正常に動作していることを確認するには、エージェントコンソールに移動し、デプロイ済みモデルの1つを使用してテストエージェントを作成します。「ジョークを教えて」などの簡単な指示を入力し、テスト呼び出しを実行して、モデルが期待どおりに応答することを確認します。

連携を削除するには、**Microsoft Foundry連携**ページで**切断**を選択します。

連携に関する問題や質問がある場合は、[Azureサポート](https://azure.microsoft.com/en-us/support/options/)にお問い合わせください。