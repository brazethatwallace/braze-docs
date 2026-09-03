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

BrazeとMicrosoft Foundryの連携により、カスタムAIエージェントを構築する際に、Microsoft Foundryで管理されている生成AIモデルを使用できます。この連携では現在、gpt-5.4-miniとgpt-5.4-nanoの2つのモデルをサポートしています。この連携により、エージェントはパーソナライズされたコピーの生成、リアルタイムの意思決定、またはFoundryで管理されたモデルを使用したカタログフィールドの更新を行うことができます。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| アクティブなサブスクリプションを持つ Azure アカウント | ヘルプについては、管理者に連絡するか、[Azure アカウントオプション](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)を参照してください。 |
| Microsoft Foundry インスタンス | プロジェクトを作成するための Microsoft Foundry インスタンス。 |
| Microsoft Foundry プロジェクト | デプロイされたモデルを格納するための Foundry インスタンス内のプロジェクト。 |
| デプロイ済みモデル | Foundry プロジェクト内にデプロイされた、サポート対象モデルのうち少なくとも1つ。 |
| Braze インスタンス | Brazeインスタンスは、[API概要ページ]({{site.baseurl}}/api/basics#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Foundryでサポートされているモデルをデプロイする {#deploy-supported-models-in-foundry}

BrazeとMicrosoft Foundryの連携では、gpt-5.4-miniとgpt-5.4-nanoの2つのモデルがサポートされています。どちらもFoundryインスタンス内のFoundryプロジェクトにデプロイする必要があります。

Foundryプロジェクトを作成してモデルをデプロイするには、[Microsoft Foundryのドキュメント](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal)に従ってください。

1. Azureポータルから Microsoft Foundryにサインインします。
2. Microsoft Foundryで、Brazeと連携するモデルを格納するプロジェクトを作成します。
3. gpt-5.4-mini、gpt-5.4-nano、またはその両方のいずれを使用するかを決定します。
4. 使用するモデルごとに、Microsoft Foundryのドキュメントに従ってデプロイします。デフォルトのデプロイ名は変更しないでください。変更すると、そのモデルの連携が正常に動作しなくなる可能性があります。

## 連携 {#integration}

Foundry インスタンスをBrazeに接続するには、以下の手順に従います。

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Microsoft Foundry**を見つけます。
2. **Microsoft Foundry APIキー**を入力します。
3. **Microsoft Foundry インスタンス名**を入力します。これは `.services.ai.azure.com` の前のサブドメインです。
4. **保存**を選択します。

保存すると、Brazeは接続日時とともに接続済みステータスを表示します。エージェントコンソールで[カスタムエージェントを作成する]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)際に、Foundry モデルを選択できます。

{% alert important %}
gpt-5.4-mini または gpt-5.4-nano を使用するには、デフォルトのデプロイメント名を変更せずに、各モデルを Foundry プロジェクトにデプロイする必要があります。
{% endalert %}

連携が正常に動作していることを確認するには、エージェントコンソールに移動し、デプロイ済みモデルのいずれかを使用してテストエージェントを作成します。「ジョークを教えて」などの簡単な指示を入力し、テスト呼び出しを実行して、モデルが期待どおりに応答することを確認します。

連携を解除するには、**Microsoft Foundry Integration** ページで**切断**を選択します。

連携に関する問題や質問がある場合は、[Azure サポート](https://azure.microsoft.com/en-us/support/options/)にお問い合わせください。