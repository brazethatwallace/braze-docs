---
nav_title: Databricks Mosaic
article_title: Databricks Mosaic
description: "このリファレンス記事では、BrazeとDatabricks Mosaicのパートナーシップについて説明します。この連携により、DatabricksモデルをBrazeに接続し、カスタムAIエージェントで使用できます。"
alias: /partners/databricks_mosaic/
page_type: partner
search_tag: Partner

---

# Databricks Mosaic

> [Databricks Mosaic AI](https://www.databricks.com/product/artificial-intelligence)は、Databricks Data Intelligence Platform上でAIおよび機械学習モデルを大規模に構築、デプロイ、管理するためのDatabricksの統合プラットフォームです。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_この連携はDatabricksによって管理されています。_

## 連携について {#about-the-integration}

BrazeとDatabricks Mosaicの連携により、DatabricksのトークンとワークスペースをBrazeに接続し、カスタムAIエージェントを構築する際にDatabricksモデルを使用できます。Brazeは、Databricks Mosaicの認証情報を使用して顧客向けのコンテンツを生成します。この連携により、エージェントはパーソナライズ済みのコピーを生成したり、リアルタイムの意思決定を行ったり、Databricksモデルを使用してカタログフィールドを更新したりできます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| 個人アクセストークン付きのDatabricksアカウント | [個人アクセストークン](https://docs.databricks.com/en/dev-tools/auth/pat.html)を持つDatabricksアカウント。ヘルプが必要な場合は、管理者または[Databricksサポート](https://help.databricks.com/)にお問い合わせください。 |
| Databricksワークスペース名 | Databricksアカウントのワークスペース名（またはインスタンス）。これは`.cloud.databricks.com`または`.azuredatabricks.net`の前のサブドメインです（例: `dbc-eb57d699-f22c`）。 |
| Brazeインスタンス | Brazeインスタンスは、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

Databricks Mosaicの認証情報をBrazeに接続するには:

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Databricks Mosaic Integration**を見つけます。
2. **Databricksトークン**を入力します。
3. **Databricksワークスペース名**を入力します。これは`.cloud.databricks.com`または`.azuredatabricks.net`の前のサブドメインです。
4. **保存**を選択します。

保存後、Brazeは接続日時とともに接続済みステータスを表示します。エージェントコンソールで[カスタムエージェントを作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)する際に、Databricksモデルを選択できます。

連携を削除するには、**Databricks Mosaic Integration**ページで**切断**を選択します。

連携に関する問題や質問がある場合は、[Databricksサポート](https://help.databricks.com/)にお問い合わせください。