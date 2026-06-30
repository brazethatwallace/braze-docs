---
nav_title: BrazeでCurrentsを使用する方法
article_title: BrazeでCurrentsを使用する方法
page_order: 6
page_type: tutorial
description: "このCurrentsのハウツー記事では、イベントデータの適切な取り込みを設定するための基本的なプロセスと、それをデータベースやビジネスインテリジェンス (BI) ツールに移動する方法を順に説明します。"
tool: Currents

---

# BrazeでCurrentsを使用する方法 {#how-braze-uses-currents}

> Brazeは選択した[パートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)とともに、社内でCurrentsを使用しています。

弊社ではメールやプッシュのCampaignから得たデータをフィルターにかけ、ビジネスインサイトツールであるLookerに取り込んでいますが、そこにたどり着くまでには少し異なるルートがあります。弊社ではETL（Extract, Transform, Load）手法の逆バージョンを使用しています。つまり、順序をELT（Extract, Load, Transform）に切り替えるのです。

## ステップ 1: イベントデータの取り込みと集約 {#step-1-intake-and-aggregate-event-data}

エンゲージメントツール（CampaignやCanvasなど）を使用してCampaignを開始した後、独自のシステムとメールパートナーからのデータを使用してイベントデータを追跡します。このデータの一部は集計されてダッシュボードに表示されますが、さらに詳細を調べたいと考えました。

## ステップ 2: データストレージパートナーへのイベントデータの送信 {#step-2-send-event-data-to-a-data-storage-partner}

保存と抽出の目的で、BrazeのイベントデータをAmazon S3に送信するようにCurrentsを設定しました。[Athena](https://aws.amazon.com/athena/)を使用してS3の上でクエリを実行できることはわかっています。これは短期的に優れたソリューションです。しかし、弊社ではリレーショナルデータベースとビジネスインテリジェンス/分析ツールを使用する長期的なソリューションを求めていました。（これはお客様にも推奨するソリューションです。）

S3はデータの移動、ピボット、分析のための柔軟なストレージとルーティングオプションを提供します。S3ではデータを変換しません。特定の構造を維持するためです。

## ステップ 3: リレーショナルデータベースでのイベントデータの変換 {#step-3-transform-event-data-with-a-relational-database}

S3からウェアハウス（弊社の場合では[Snowflakeデータ共有](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE)またはSnowflake Reader Accounts）を選択します。そこでデータを変換してからLookerに移動します。Lookerでは、データを構造化して整理するブロックを設定しています。

ウェアハウスの選択肢はSnowflakeのみに限りません。他にも[Redshift](https://aws.amazon.com/redshift/)、[Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE)などがあります。

### Snowflake Reader Accounts {#snowflake-reader-accounts}

Snowflake Reader Accountsは、SnowflakeアカウントやSnowflakeとの顧客関係を必要とせずに、[Snowflakeデータ共有]({{site.baseurl}}/partners/snowflake)と同じデータおよび機能へのアクセスをユーザーに提供します。Reader Accountsでは、Brazeがアカウントを作成してデータを共有し、ログインしてデータにアクセスするための認証情報を提供します。これにより、すべてのデータ共有と使用料金の請求は完全にBrazeが処理します。

詳細については、カスタマーサクセスマネージャーにお問い合わせください。

#### その他のリソース {#additional-resources}
使用状況の監視に役立つリソースについては、Snowflakeの[Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors.html)および[Viewing Warehouse Credit Usage](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account)の記事をご確認ください。

## ステップ 4: ビジネスインテリジェンス (BI) ツールを使用してデータを操作する {#step-4-use-a-business-intelligence-bi-tool-to-manipulate-your-data}

最後に、BIツールを使用してデータを分析し、チャートやその他のビジュアルツールに変換します。[LookerとLooker Blocks](https://www.marketplace.looker.com/)を使用することで、Currentsからデータが移動するたびにETLやELTを行う必要がなくなります。

同じことをやってみたいと思いましたか？以下のドキュメントをチェックして、これらの詳細情報と、データベースの構築にどのように活用できるかをご確認ください。

- [User Behavior Block](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Message Engagement Block](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)