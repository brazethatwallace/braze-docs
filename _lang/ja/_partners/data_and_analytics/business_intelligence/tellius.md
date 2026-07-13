---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "このリファレンス記事では、BrazeとTelliusのパートナーシップについて説明します。Telliusは、意思決定インテリジェンスおよび拡張分析のプラットフォームであり、BIエンジニアに依存せずにデータを活用してダッシュボードを構築し、マーケティングに関してより的確な決定を行うためのインサイトを生成することができます。"
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/)は意思決定インテリジェンスと拡張分析のプラットフォームであり、自然言語検索を使用してデータに関する質問に答え、AIを活用したガイド付きインサイトで「なぜ」を理解するためにさらに深く掘り下げることができます。

BrazeとTelliusの統合により、ユーザーはBIエンジニアに依存せずにデータを活用し、ダッシュボードを構築し、マーケティングに関してより的確な決定を行うためのインサイトを生成することができます。この統合には、BrazeのデータがSnowflakeに保存されている必要があり、Telliusはそこに直接接続し、ライブモード統合でクエリをプッシュダウンできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Telliusアカウント | このパートナーシップを活用するには、Telliusアカウントが必要です。[無料トライアル](https://www.tellius.com/free-trial/)でTelliusを利用してみることができます。|
| Snowflakeデータ共有プログラム | 現在Snowflakeをご利用のお客様は、BrazeのデータをSnowflakeインスタンスに取り込むためのSnowflakeデータ共有プログラムについて、Brazeの担当者にお問い合わせください。|
| Snowflake Readerアカウント | Snowflakeをご利用でないお客様は、お客様のBrazeデータにアクセスするためのSnowflake Readerアカウントのプロビジョニングについて、Brazeの担当者にお問い合わせください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1:Snowflake経由でBrazeへのアクセスを取得する {#step-1-obtain-access-to-braze-through-snowflake}

Brazeはきめ細かい顧客データをSnowflakeに保存しています。Braze Snowflakeデータ共有プログラムを利用するか、Snowflake Readerアカウントを取得することで、Brazeデータからインサイトを生成できます。

設定するには、[Snowflake統合]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)の手順に従ってください。

### ステップ2:SnowflakeでTelliusをBrazeデータに接続する {#step-2-connect-tellius-to-braze-data-in-snowflake}

次のいずれかの方法で、TelliusをSnowflakeのBrazeデータに接続します。

- 直接アクセス:Telliusにデータを読み込むには、[データセットの読み込み](https://help.tellius.com/article/jn6o59d5gk-load-datasets)の手順に従います。
- OAuthアクセス:SnowflakeへのOAuthアクセスの場合は、[OAuth認証](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake)の手順に従います。

### ステップ3:読み込んだデータからTelliusでビジネスビューを作成する {#step-3-create-business-view-in-tellius-from-loaded-data}

自然言語検索と自動化されたインサイトの利用を開始するには、[ビジネスビュー](https://help.tellius.com/article/hy9yvh5tom-create-business-view)を作成し、Snowflake接続からデータセットを選択します。

### ステップ4:Telliusを使ってデータの価値を最大限に引き出す {#step-4-get-the-most-value-out-of-your-data-using-tellius}

Telliusには、プラットフォームの機能についてウォークスルーを行うガイド付きインターフェイスがあります。その他の質問やウォークスルーについては、Telliusの[ナレッジベース](https://help.tellius.com/)を参照してください。