---
nav_title: カタログデータの同期と削除
article_title: カタログデータの同期と削除
page_order: 6
page_type: reference
description: "このページでは、カタログデータの同期方法の概要を説明します。"

---

# カタログデータの同期と削除 {#sync-and-delete-catalog-data}

> このページでは、カタログデータの同期方法について説明します。

## ステップ1：新しいカタログを作成する {#step-1-create-a-new-catalog}

[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)用の新しいクラウドデータ取り込み（CDI）連携を作成する前に、新しいカタログを作成するか、連携に使用する既存のカタログを特定する必要があります。新しいカタログを作成するにはいくつかの方法があり、いずれもCDI連携に使用できます。
- [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/create)をアップロードする
- [Brazeダッシュボード]({{site.baseurl}}/user_guide/data/activation/catalogs/create)またはCDIの設定中にカタログを作成する
- [カタログ作成エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)を使用してカタログを作成する

カタログスキーマの変更（新しいフィールドの追加やフィールドタイプの変更など）は、更新データがCDIを通じて同期される前に、カタログダッシュボードで行う必要があります。データウェアハウスのデータとBrazeのスキーマの間の競合を避けるために、同期が一時停止中または実行がスケジュールされていないときにこれらの更新を行うことをお勧めします。

## ステップ2: クラウドデータ取り込みをカタログデータと統合する {#step-2-integrate-cloud-data-ingestion-with-catalog-data}
カタログ同期の設定は、[ユーザーデータのCDI統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)のプロセスとほぼ同じです。

{% tabs %}
{% tab Snowflake %}

1. Snowflakeでソーステーブルを設定します。以下の例の名前を使用することも、独自のデータベース名、スキーマ名、テーブル名を選択することもできます。テーブルの代わりにビューやマテリアライズドビューを使用することもできます。
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
2. ロール、ウェアハウス、ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報がある場合はそれを再利用できますが、カタログソーステーブルへのアクセスを拡張してください。
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
3. Snowflakeアカウントにネットワークポリシーがある場合は、CDIサービスが接続できるようにBrazeのIPを許可リストに追加してください。IPの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。
4. Brazeダッシュボードで、**テクノロジーパートナー** > **Snowflake**に移動し、新しい同期を作成します。
5. 接続の詳細（または既存の認証情報を再利用）とソーステーブルを入力します。
6. 設定フローのステップ2に進み、「Catalogs」同期タイプを選択して、統合名とスケジュールを入力します。統合名は、以前に作成したカタログの名前と**完全に一致する**必要があります。
7. 同期頻度を選択し、次のステップに進みます。
8. ダッシュボードに表示される公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加します。このステップを完了するには、Snowflakeで`SECURITYADMIN`以上のアクセス権を持つユーザーが必要です。
9. **接続テスト**を選択して、すべてが期待どおりに動作することを確認します。
10. 同期を保存し、同期されたカタログデータをすべてのパーソナライゼーションのユースケースに活用します。
{% endtab %}
{% tab Redshift %}

1. Redshiftでソーステーブルを設定します。以下の例の名前を使用することも、独自のデータベース名、スキーマ名、テーブル名を選択することもできます。テーブルの代わりにビューやマテリアライズドビューを使用することもできます。
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
2. ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報がある場合はそれを再利用できますが、カタログソーステーブルへのアクセスを拡張してください。
    {% raw %}
    ```sql
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. ファイアウォールやその他のネットワークポリシーがある場合は、RedshiftインスタンスへのネットワークアクセスをBrazeに許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。IPの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab BigQuery %}

1. 必要に応じて、ソーステーブルを保持する新しいプロジェクトまたはデータセットを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

以下のフィールドを使用して、CDI統合に使用するテーブルを1つ以上作成します。

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: クラウドデータ取り込みをカタログデータと統合する" }

{:start="2"}

2. ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報がある場合はそれを再利用できますが、カタログソーステーブルへのアクセスを拡張してください。
サービスアカウントには、以下のセクションの権限が必要です。
- BigQuery Connection User: Brazeが接続を確立できるようにします。
- BigQuery User: Brazeにクエリの実行、データセットメタデータの読み取り、テーブルの一覧表示へのアクセスを提供します。
- BigQuery Data Viewer: Brazeにデータセットとその内容の表示アクセスを提供します。
- BigQuery Job User: Brazeにジョブの実行アクセスを提供します。<br><br>サービスアカウントを作成して権限を付与した後、JSONキーを生成します。詳細については、[キーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。これは後でBrazeダッシュボードに更新します。

{:start="3"}
3. ネットワークポリシーがある場合は、BigQueryインスタンスへのネットワークアクセスをBrazeに許可する必要があります。IPの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

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
| PAYLOAD | STRING, STRUCT, or MAP | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: クラウドデータ取り込みをカタログデータと統合する" }

{:start="2"}

2. Databricksワークスペースで個人アクセストークンを作成します。

- a. Databricksのユーザー名を選択し、ドロップダウンメニューから**User Settings**を選択します。
- b. **Access tokens**タブで、**Generate new token**を選択します。
- c. このトークンを識別するのに役立つコメント（「Braze CDI」など）を入力します。
- d. **Lifetime (days)**ボックスを空白のままにして、トークンの有効期間を無期限に変更します。**Generate**を選択します。
- e. 表示されたトークンをコピーし、**Done**を選択します。
- f. Brazeダッシュボードの認証情報作成ステップで入力する必要があるまで、トークンを安全な場所に保管してください。

{:start="3"}
3. ネットワークポリシーがある場合は、DatabricksインスタンスへのネットワークアクセスをBrazeに許可する必要があります。IPの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)のページを参照してください。

{% endtab %}
{% tab Microsoft Fabric %}

以下のフィールドを使用して、CDI統合に使用するテーブルを1つ以上作成します。

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

2. サービスプリンシパルを設定し、適切な権限を付与します。既存の同期の認証情報がある場合はそれを再利用できますが、カタログソーステーブルへのアクセスを拡張してください。新しいサービスプリンシパルと認証情報の作成方法については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)のページを参照してください。

{:start="3"}
3. ネットワークポリシーがある場合は、Microsoft FabricインスタンスへのネットワークアクセスをBrazeに許可する必要があります。IPの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab S3 %}
JSONまたはCSV形式でS3にソースファイルを作成します。各ファイルには以下のフィールドを含める必要があります。

| フィールド | 必須？ | 説明 |
| --- | --- | --- |
| `ID` | はい | 作成または更新するカタログアイテムのIDです。 |
| `PAYLOAD` | はい | Brazeのカタログアイテムに同期するフィールドのJSON文字列です。 |
| `DELETED` | 任意 | `true`に設定すると、対応するカタログアイテムがカタログから削除されます。 |
| `UPDATED_AT` | *非対応* | ファイルストレージでは`UPDATED_AT`列はサポートされていません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: クラウドデータ取り込みをカタログデータと統合する" }

{% alert note %}
ファイル名はAWSのルールに従い、一意である必要があります。一意性を確保するためにタイムスタンプを付加してください。
{% endalert %}

S3の完全な設定には、S3バケット、Amazon SQSキュー、AWS IAMロールとポリシーが必要です。Brazeは同期が作成された後にアップロードされたファイルのみを処理するため、取り込みたい既存のファイルは再アップロードしてください。

S3の完全な設定フローについては、[ファイルストレージ統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)、特に以下を参照してください。

- [AWSでのクラウドデータ取り込みの設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-aws)
- [Brazeでのクラウドデータ取り込みの設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze)
- [トラブルシューティング]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#troubleshooting)

AWS側の通知や権限に関する一般的な問題については、[宛先にイベント通知メッセージを公開する権限の付与](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)を参照してください。

以下の例は、ファイルストレージからカタログデータを同期するための有効なJSONおよびCSV形式を示しています。

{% subtabs %}
{% subtab JSON Catalogs %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"86","payload":"{\"product_name\":\"Product 86\",\"price\":86.86}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```

{% alert important %}
ソースファイルの各行は有効なJSONである必要があります。そうでない場合、ファイルはスキップされます。
{% endalert %}
{% endsubtab %}
{% subtab CSV Catalogs with Delete %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
86,"{""product_name"": ""Product 86"", ""price"": 86.86}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% subtab CSV Catalogs without Delete %}
```plaintext
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
86,"{""product_name"": ""Product 86"", ""price"": 86.86}"
```
{% endsubtab %}
{% endsubtabs %}

その他のファイル例については、[ファイルストレージ統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)を参照してください。

{% endtab %}
{% endtabs %}

## 連携の仕組み {#how-the-integration-works}

{% alert note %}
このセクションの同期ビューは、データウェアハウス連携にのみ適用されます。S3ファイルストレージの場合、Brazeはバケットにアップロードされた新しいファイルを検出して処理します。詳細については、[ファイルストレージ連携]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)を参照してください。
{% endalert %}

同期が実行されるたびに、Brazeは`UPDATED_AT`が最後に同期された値よりも後のすべての行を取り込みます。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。データウェアハウスのカタログデータからビューを作成し、同期が実行されるたびに完全にリフレッシュされるソーステーブルを設定することをお勧めします。ビューを使用すれば、毎回クエリを書き直す必要がありません。

たとえば、`product_id`と3つの追加属性を含む商品データテーブル（`product_catalog_1`）がある場合、以下のビューを同期できます。

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

- 連携から取得されたデータは、提供された`id`に基づいてターゲットカタログ内のアイテムを作成または更新するために使用されます。
- DELETEDが`true`に設定されている場合、対応するカタログアイテムが削除されます。
- 同期ではデータポイントは記録されませんが、同期されたすべてのデータはカタログ使用量の合計にカウントされます。この使用量は保存されたデータの合計に基づいて測定されるため、変更されたデータのみを同期することを心配する必要はありません。