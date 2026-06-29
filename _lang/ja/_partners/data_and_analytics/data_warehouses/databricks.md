---
nav_title: Databricks
article_title: Databricks
description: "この記事では、BrazeとのDatabricks Delta Sharing（クローズドベータ）について説明します。これにより、Databricksアカウント内でBrazeのエンゲージメントデータやキャンペーンデータにアクセスできます。"
page_type: partner
search_tag: Partner
permalink: /databricks/
hidden: true
---

# Databricks

> [Databricks](https://www.databricks.com/)は、エンタープライズグレードのデータ、分析、AIソリューションを大規模に構築、デプロイ、共有、維持するための統合オープン分析プラットフォームです。Databricks Data Intelligence Platformは、クラウドアカウント内のクラウドストレージおよびセキュリティと統合し、クラウドインフラを管理・デプロイします。

{% alert important %}
BrazeとのDatabricks Delta Sharingは**クローズドベータ**です。利用可能なリージョン、サポート対象リージョン、製品の動作は変更される場合があります。参加を希望される場合や、お使いのワークスペースでこの機能が有効かどうかを確認するには、Brazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## Delta Sharing（BrazeからDatabricksへ） {#delta-sharing-braze-to-databricks}

Databricksの[Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html)を使用すると、データをコピーまたは複製することなく、クラウドやリージョンをまたいでビジネスユニットや子会社とデータを安全に共有できます。

**Delta Sharingは以下のような場合に使用します。**
- Databricks SQLを使用してBrazeのイベントデータやキャンペーンデータをクエリする
- 複雑なレポートを作成し、アトリビューションモデリングを実行する
- BrazeデータをDatabricksアカウント内の他のデータと結合する
- チャネル、業界、デバイスプラットフォーム全体でエンゲージメントデータをベンチマークする

セットアップ手順については、[Databricks Delta Sharing]({{site.baseurl}}/delta_sharing/)を参照してください。

DatabricksでのDelta Sharingの詳細については、[Delta Sharingとは？](https://www.databricks.com/product/delta-sharing)を参照してください。

## 前提条件 {#prerequisites}

この機能を使用する前に、以下を完了してください。

| 要件 | 説明 |
| ----------- | ----------- |
| Brazeへのアクセス | Brazeでこの機能にアクセスするには、Brazeアカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。 |
| Databricksアカウント | `admin`権限を持つDatabricksアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

共有の設定と共有データのクエリの準備ができたら、[Databricks Delta Sharing]({{site.baseurl}}/delta_sharing/)に進んでください。