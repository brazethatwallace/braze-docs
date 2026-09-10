---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "この記事では、BrazeとSnowflakeのパートナーシップについて説明します。データ共有（BrazeからSnowflake）とクラウドデータ取り込みの両方を取り上げます。"
page_type: partner
search_tag: Partner
---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html)は、Software-as-a-Service（SaaS）として提供される専用SQLクラウドデータウェアハウスです。Snowflakeのデータウェアハウスは、従来のデータウェアハウス製品よりも高速で使いやすく、極めて高い柔軟性を備えています。Snowflake独自の特許取得済みアーキテクチャにより、すべてのデータを集約し、迅速な分析を可能にし、すべてのユーザーにデータドリブン型のインサイトを提供することが容易になります。

BrazeはSnowflakeとの2つの統合を提供しています。これらを組み合わせることで、BrazeとSnowflake環境間の完全な双方向データパイプラインを実現します。

## 統合の選択 {#choosing-an-integration}

### データ共有（BrazeからSnowflakeへ） {#data-sharing-braze-to-snowflake}

Snowflakeの[セキュアデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing)を使用すると、BrazeのエンゲージメントおよびキャンペーンデータにSnowflakeインスタンスから直接、安全かつリアルタイムにアクセスできます。アカウント間でデータがコピーまたは転送されることはなく、すべての共有はSnowflake独自のサービスレイヤーとメタデータストアを通じて行われます。

**データ共有は次のような場合に使用してください。**
- Snowflake SQLを使用してBrazeのイベントおよびキャンペーンデータをクエリする
- 複雑なレポートを作成し、アトリビューションモデリングを実行する
- BrazeデータをSnowflakeデータウェアハウス内の他のデータと結合する
- チャネル、業界、デバイスプラットフォーム全体でエンゲージメントデータをベンチマークする

設定手順については、[Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing)を参照してください。

### クラウドデータインジェスチョン（SnowflakeからBrazeへ） {#cloud-data-ingestion-snowflake-to-braze}

[クラウドデータインジェスチョン（CDI）]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用すると、Snowflakeインスタンスから直接Brazeにデータを同期できます。これにより、ユーザー属性、イベント、購入データを、信頼できるデータソースであるデータウェアハウスと常に同期した状態でBrazeに保持できます。

**クラウドデータインジェスチョンは次のような場合に使用してください。**
- Snowflakeからのユーザー属性をBrazeのユーザープロファイルに同期する
- Snowflakeからイベントまたは購入データをBrazeに送信する
- データウェアハウスで行われるデータ変換とBrazeを同期した状態に保つ
- SnowflakeからBrazeへのカスタムETLパイプラインの構築やメンテナンスを回避する

Snowflakeのデータ共有について詳しくは、[Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)を参照してください。

## 前提条件 {#prerequisites}

この機能を使用するには、以下を完了する必要があります。

| 要件 | 説明 |
| ----------- | ----------- |
| Brazeアクセス | Brazeでこの機能にアクセスするには、Brazeアカウントまたはカスタマーサクセスマネージャーに連絡する必要があります。 |
| Brazeワークスペース権限 | データ共有を表示するには、[Currents統合の表示]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)権限が必要です。データ共有の作成、更新、削除を行うには、[Currents統合の編集]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)権限が必要です。 |
| Snowflakeアカウント | `admin`権限を持つSnowflakeアカウントが必要です。HIPAA非対象の顧客の場合、Snowflake StandardまたはEnterprise Editionがサポートされています。HIPAA準拠のデータ共有には、Business Critical Editionが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## セキュアデータ共有の設定 {#setting-up-secure-data-sharing}

Snowflakeでは、データ共有は[データプロバイダー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)と[データコンシューマー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)の間で行われます。このコンテキストでは、Brazeアカウントがデータ共有を作成して送信するデータプロバイダーであり、Snowflakeアカウントがデータ共有を使用してデータベースを作成するデータコンシューマーです。詳細については、[Snowflake: 共有データの利用](https://docs.snowflake.com/en/user-guide/data-share-consumers)を参照してください。

### ステップ1:Brazeからデータ共有を送信する {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### ステップ2:Snowflakeでデータベースを作成する {#step-2-create-the-database-in-snowflake}

1. 数分後、Snowflakeアカウントにインバウンドデータ共有が届きます。
2. インバウンドデータ共有を使用して、テーブルを表示およびクエリするためのデータベースを作成します。例:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. 新しいデータベースをクエリするための権限を付与します。

{% alert warning %}
Brazeダッシュボードで共有を削除して再作成した場合、以前作成したデータベースをドロップし、`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` を使用して再作成する必要があります。
複数のワークスペースが同じSnowflakeアカウントにデータを共有している場合は、[Snowflakeデータ共有に関するFAQ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs)でマルチワークスペース構成の管理に関するガイダンスを参照してください。
{% endalert %}

## 使用方法と可視化 {#usage-and-visualization}

データ共有がプロビジョニングされたら、受信データ共有からデータベースを作成する必要があります。これにより、共有されたすべてのテーブルがSnowflakeインスタンスに表示され、インスタンスに保存されている他のデータと同様にクエリできるようになります。ただし、共有データは読み取り専用であり、クエリのみ可能で、変更や削除はできません。

Currentsと同様に、Snowflakeセキュアデータ共有を使用して次のことができます。

{% multi_lang_include partners/data_sharing_use_cases.md %}

利用可能なテーブルとカラムの完全なリストについては、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)を参照してください。Snowflakeデータ共有には、このリファレンスに記載されているすべてのテーブルに加え、スナップショット、キャンペーンおよびキャンバスの変更ログ、エージェントコンソールイベント、メッセージリトライイベント用のSnowflake専用テーブルが含まれます。

[生のテーブルスキーマ](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)をテキストファイルとしてダウンロードすることもできます。

### ユーザーIDスキーマ {#user-id-schema}

ユーザーIDに関するBrazeとSnowflakeの命名規則の違いに注意してください。

| Brazeスキーマ | Snowflakeスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられる一意の識別子です。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されるユーザープロファイルの一意の識別子です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーIDスキーマ" }

## 重要な情報と制限事項 {#important-information-and-limitations}

### 破壊的変更と非破壊的変更 {#breaking-versus-non-breaking-changes}

#### 非破壊的変更 {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
新しいカラムは非破壊的変更とみなされるため、Brazeでは各クエリで`SELECT *`クエリを使用する代わりに、対象のカラムを明示的にリストすることを強くお勧めします。または、カラムを明示的に指定するビューを作成し、テーブルを直接クエリする代わりにそのビューをクエリすることもできます。
{% endalert %}

#### 破壊的変更 {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Snowflakeリージョン {#snowflake-regions}

Brazeは現在、すべてのユーザーレベルのデータをSnowflake AWS US East-1、EU-Central（フランクフルト）、AP-Northeast-1（東京）、AP-Southeast-2（シドニー）、AP-Southeast-3（ジャカルタ）リージョンでホストしています。これらのリージョン以外のユーザーに対して、BrazeはAWS、Azure、またはGCPの任意のリージョンでSnowflakeインフラをホストしている共同顧客にデータ共有を提供できます。

### データリテンション {#data-retention}

#### リテンションポリシー {#retention-policy}

2年以上前のデータはすべてアーカイブされ、長期ストレージに移動されます。アーカイブプロセスの一環として、すべてのイベントは匿名化され、個人を特定できる情報（PII）に該当する機密フィールドは除去されます（これには`properties`などのオプションPIIフィールドも含まれます）。アーカイブされたデータには`user_id`フィールドが引き続き含まれるため、すべてのイベントデータにわたるユーザー単位の分析が可能です。

各イベントの対応する`USERS_*_SHARED`ビューで、直近2年間のデータをクエリできます。さらに、各イベントには`USERS_*_SHARED_ALL`ビューがあり、匿名化されたデータと匿名化されていないデータの両方を返すクエリが可能です。

#### 過去のデータ {#historical-data}

Snowflakeの過去のイベントデータのアーカイブは2019年4月まで遡ります。BrazeがSnowflakeにデータを保存し始めた最初の数か月間、プロダクトの変更が行われたため、一部のデータが若干異なって見えたり、一部のnull値が含まれている場合があります（当時はすべての利用可能なフィールドにデータを渡していなかったためです）。2019年8月以前のデータを含む結果は、想定と若干異なる可能性があることを前提としてください。

### 一般データ保護規則（GDPR）コンプライアンス {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### 共有データのクエリ：`TIME`とクエリパフォーマンス {#querying-shared-data-time-and-query-performance}

データ共有ビュー（例：`USERS_BEHAVIORS_CUSTOMEVENT_SHARED`）のイベントデータは、**`TIME`フィールドでクラスタリングされています**。**イベントが発生した時間**でフィルタリングする場合は、推奨フィルターとして**`TIME`**を使用してください。**`TIME`**で行を絞り込むクエリは、**`SF_CREATED_AT`**でフィルタリングするクエリよりも一般的に**パフォーマンスが高くなります**。これはクラスタリングがイベント時間に合わせて配置されているためです。

| フィールド | 意味 |
| ----- | ------- |
| `TIME` | イベントが発生した時刻のUnixタイムスタンプ。発生時刻でフィルタリングする場合はこちらを推奨します。 |
| `SF_CREATED_AT` | 行がSnowflakeに読み込まれた時刻のタイムスタンプ（取り込み時刻）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="共有データのクエリ：TIMEとクエリパフォーマンス" }

### クエリの速度、パフォーマンス、コスト {#speed-performance-cost-of-queries}

データに対して実行されるクエリの速度、パフォーマンス、コストは、データのクエリに使用するウェアハウスサイズによって決まります。場合によっては、分析のためにアクセスするデータ量に応じて、クエリを正常に実行するためにより大きなウェアハウスサイズを使用する必要があることがあります。Snowflakeには、最適なサイズの決定方法に関する優れたリソースが用意されています。[ウェアハウスの概要](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html)や[ウェアハウスに関する考慮事項](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)をご覧ください。

> Snowflakeの設定時に参照できるクエリの例については、[サンプルクエリ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries)および[ETLイベントパイプラインの設定]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup)の例をご確認ください。

設定手順については、[クラウドデータ取り込み：データウェアハウス統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照してください。