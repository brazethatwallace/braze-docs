---
nav_title: カタログデータの同期と削除
article_title: カタログデータの同期と削除
page_order: 6
page_type: reference
description: "このページでは、カタログデータの同期方法の概要を説明します。"

---

# カタログデータの同期と削除 {#sync-and-delete-catalog-data}

> このページでは、カタログデータの同期方法について説明します。

## ステップ1:新規カタログの作成 {#step-1-create-a-new-catalog}

[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)用の新しいクラウドデータ取り込み（CDI）連携を作成する前に、新規カタログを作成するか、連携に使用する既存のカタログを特定する必要があります。新規カタログを作成する方法はいくつかあり、いずれもCDI連携に使用できます。
- [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/create#creating-a-catalog)をアップロードする
- [Brazeダッシュボード]({{site.baseurl}}/user_guide/data/activation/catalogs/create#creating-a-catalog)またはCDIセットアップ中にカタログを作成する
- [カタログ作成エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)を使用してカタログを作成する

カタログスキーマへの変更（例えば、新しいフィールドの追加やフィールドタイプの変更）は、更新されたデータがCDIを通じて同期される前に、カタログダッシュボードで行う必要があります。データウェアハウスのデータとBrazeのスキーマとの競合を避けるために、同期が一時停止されているとき、または実行がスケジュールされていないときにこれらの更新を行うことをお勧めします。

## ステップ2:クラウドデータ取り込みとカタログデータの連携 {#step-2-integrate-cloud-data-ingestion-with-catalog-data}
カタログ同期の設定は、[ユーザーデータCDI連携]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)のプロセスとほぼ同じです。

{% tabs %}
{% tab Snowflake %}

1. Snowflakeでソーステーブルを設定します。次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. ロール、ウェアハウス、ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報をすでに持っている場合はそれらを再利用できますが、必ずカタログソーステーブルへのアクセスを拡張してください。
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Snowflakeアカウントにネットワークポリシーがある場合は、CDIサービスが接続できるようにBrazeのIPを許可リストに追加してください。IPのリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。
4. Brazeダッシュボードで、**テクノロジーパートナー** > **Snowflake** に移動し、新しい同期を作成します。
5. 接続の詳細（または既存の認証情報を再利用）とソーステーブルを入力します。
6. セットアップフローのステップ2に進み、「Catalogs」同期タイプを選択し、連携名とスケジュールを入力します。連携名は、以前に作成したカタログの名前と**完全に一致する**必要があることに注意してください。
7. 同期頻度を選択し、次のステップに進みます。
8. ダッシュボードに表示された公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加します。このステップを完了するには、Snowflakeで `SECURITYADMIN` 以上のアクセス権を持つ担当者が必要です。
9. **Test Connection** を選択して、すべてが期待どおりに動作することを確認します。
10. 同期を保存し、同期されたカタログデータをすべてのパーソナライゼーションのユースケースに活用します。
{% endtab %}
{% tab Redshift %}

1. Redshiftでソーステーブルを設定します。次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報をすでに持っている場合はそれらを再利用できますが、必ずカタログソーステーブルへのアクセスを拡張してください。
    {% raw %}
    ```sql
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. ファイアウォールやその他のネットワークポリシーがある場合は、BrazeにRedshiftインスタンスへのネットワークアクセスを許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。IPのリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab BigQuery %}

1. 必要に応じて、ソーステーブルを格納する新しいプロジェクトまたはデータセットを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ、CDI連携に使用するテーブルを1つ以上作成します。

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| フィールド名 | タイプ | モード |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | JSON | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | OPTIONAL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2:クラウドデータ取り込みとカタログデータの連携" }

{:start="2"}

2. ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報をすでに持っている場合はそれらを再利用できますが、必ずカタログソーステーブルへのアクセスを拡張してください。
サービスアカウントには次のセクションの権限が必要です。
- BigQuery Connection User: Brazeに接続を許可します。
- BigQuery User: クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスをBrazeに提供します。
- BigQuery Data Viewer: データセットとその内容を表示するためのアクセスをBrazeに提供します。
- BigQuery Job User: ジョブを実行するためのアクセスをBrazeに提供します。<br><br>サービスアカウントを作成して権限を付与したら、JSONキーを生成します。詳細については、[Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) を参照してください。後でBrazeダッシュボードにアップロードします。

{:start="3"}
3. ネットワークポリシーを設定している場合は、BrazeにBigQueryインスタンスへのネットワークアクセスを許可する必要があります。IPのリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab Databricks %}

1. Databricksでソーステーブルを設定します。以下の例の名前を使用することも、独自のカタログ名、スキーマ名、テーブル名を選択することもできます。テーブルの代わりにビューやマテリアライズドビューを使用することもできます。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| フィールド名 | タイプ | モード |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | STRING、STRUCT、または MAP | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2:クラウドデータ取り込みとカタログデータの連携" }

{:start="2"}

2. Databricksワークスペースでパーソナルアクセストークンを作成します。

- a. Databricksユーザー名を選択し、ドロップダウンメニューから **User Settings** を選択します。
- b. **Access tokens** タブで、**Generate new token** を選択します。
- c.「Braze CDI」など、このトークンの識別に役立つコメントを入力します。
- d. **Lifetime (days)** ボックスを空白のままにして、トークンの有効期間を無期限に変更します。**Generate** を選択します。
- e. 表示されたトークンをコピーして、**Done** を選択します。
- f. Brazeダッシュボードの認証情報作成ステップで入力が必要になるまで、トークンを安全な場所に保管してください。

{:start="3"}
3. ネットワークポリシーを設定している場合は、BrazeにDatabricksインスタンスへのネットワークアクセスを許可する必要があります。IPのリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)のページを参照してください。

{% endtab %}
{% tab Microsoft Fabric %}

次のフィールドを持つ、CDI連携に使用するテーブルを1つ以上作成します。

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. サービスプリンシパルを設定し、適切な権限を付与します。既存の同期の認証情報をすでに持っている場合はそれらを再利用できますが、必ずカタログソーステーブルへのアクセスを拡張してください。新しいサービスプリンシパルと認証情報の作成方法については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)のページを参照してください。

{:start="3"}
3. ネットワークポリシーを設定している場合は、BrazeにMicrosoft Fabricインスタンスへのネットワークアクセスを許可する必要があります。IPのリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab S3 %}
JSONまたはCSV形式を使用してS3にソースファイルを作成します。各ファイルには次のフィールドを含める必要があります。

| フィールド | 必須？ | 説明 |
| --- | --- | --- |
| `ID` | はい | 作成または更新するカタログアイテムのID。 |
| `PAYLOAD` | はい | Brazeのカタログアイテムに同期するフィールドのJSON文字列。 |
| `DELETED` | オプション | `true` に設定すると、対応するカタログアイテムがカタログから削除されます。 |
| `UPDATED_AT` | *非対応* | ファイルストレージでは `UPDATED_AT` 列はサポートされていません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2:クラウドデータ取り込みとカタログデータの連携" }

{% alert note %}
ファイル名はAWSのルールに従い、一意である必要があります。一意性を確保するためにタイムスタンプを付加してください。
{% endalert %}

完全なS3セットアップには、S3バケット、Amazon SQSキュー、およびAWS IAMロールとポリシーが必要です。Brazeは同期が作成された後にアップロードされたファイルのみを処理するため、取り込みたい既存のファイルは再アップロードしてください。

完全なS3セットアップフローについては、[ファイルストレージの連携]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)を参照してください。特に以下をご覧ください。

- [AWSでのクラウドデータ取り込みの設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-aws)
- [Brazeでのクラウドデータ取り込みの設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze)
- [トラブルシューティング]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#troubleshooting)

AWS側の通知や権限に関する一般的な問題については、[Granting permissions to publish event notification messages to a destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html) を参照してください。

以下の例は、ファイルストレージからカタログデータを同期するための有効なJSONおよびCSV形式を示しています。

{% subtabs %}
{% subtab JSONカタログ %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"86","payload":"{\"product_name\":\"Product 86\",\"price\":86.86}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```

{% alert important %}
ソースファイルの各行には有効なJSONが含まれている必要があります。そうでない場合、ファイルはスキップされます。
{% endalert %}
{% endsubtab %}
{% subtab 削除ありのCSVカタログ %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
86,"{""product_name"": ""Product 86"", ""price"": 86.86}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% subtab 削除なしのCSVカタログ %}
```plaintext
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
86,"{""product_name"": ""Product 86"", ""price"": 86.86}"
```
{% endsubtab %}
{% endsubtabs %}

その他のファイル例については、[ファイルストレージの連携]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)を参照してください。

{% endtab %}
{% endtabs %}

## 連携の仕組み {#how-the-integration-works}

{% alert note %}
このセクションの同期ビューは、データウェアハウス連携にのみ適用されます。S3ファイルストレージの場合、Brazeはバケットにアップロードされた新しいファイルを処理します。詳細については、[ファイルストレージの連携]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)を参照してください。
{% endalert %}

同期が実行されるたびに、Brazeは `UPDATED_AT` が最後に同期された値より後のすべての行を取り込みます。境界のタイムスタンプと同じ値を持つ新しい行がある場合、そのタイムスタンプの行が再同期されることがあります。カタログデータからデータウェアハウスにビューを作成し、同期が実行されるたびに完全にリフレッシュされるソーステーブルを設定することをお勧めします。ビューを使用すれば、クエリを毎回書き直す必要はありません。

例えば、`product_id` と3つの追加属性を含む製品データテーブル（`product_catalog_1`）がある場合、以下のビューを同期できます。

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- 連携からフェッチされたデータは、指定された `id` に基づいて、ターゲットカタログ内のアイテムの作成または更新に使用されます。
- DELETEDが `true` に設定されている場合、対応するカタログアイテムが削除されます。
- 同期ではデータポイントは記録されませんが、同期されたすべてのデータはカタログ使用量の合計にカウントされます。この使用量は保存されたデータの総量に基づいて計測されるため、変更されたデータのみを同期することを心配する必要はありません。