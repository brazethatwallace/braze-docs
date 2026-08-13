---
nav_title: アカウントデータの同期と削除
article_title: CDIを使ってアカウントデータを同期する
page_order: 5
page_type: reference
description: "CDIを使ってBrazeアカウントデータを同期する方法を学習します。"

---

# CDIを使ってアカウントデータを同期する {#sync-account-data-using-cdi}

> CDIを使ってBrazeアカウントデータを同期する方法を学習します。

## 前提条件 {#prerequisites}

{% alert note %}
データウェアハウスのデータとBrazeのスキーマ間の競合を避けるため、アカウントスキーマの更新は同期が一時停止中またはスケジュールされていないときにのみ行ってください。
{% endalert %}

## 同期の仕組み {#how-syncing-works}

- 各同期では、`UPDATED_AT`が最後に同期されたタイムスタンプより後の行がインポートされます。境界のタイムスタンプと同じタイムスタンプを持つ新しい行がある場合、そのタイムスタンプの行が再同期されることがあります。詳細については、[重複するタイムスタンプを持つ行の再同期を避ける]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。
- 統合からのデータは、提供された`id`に基づいてアカウントを作成または更新します。
- `DELETED`が`true`の場合、アカウントは削除されます。
- 同期ではデータポイントは記録されませんが、同期されたすべてのデータは合計アカウント使用量にカウントされ、保存データの合計で測定されます。変更されたデータのみに制限する必要はありません。
- アカウントスキーマにないフィールドは破棄されます。新しいフィールドを同期する前にスキーマを更新してください。
- 同期名にカーソルを合わせて該当するアクションを選択することで、同期の更新、再開、または一時停止ができます。

## アカウントデータを同期する {#sync-your-account-data}

CDI を使用して、データウェアハウスまたはファイルストレージ経由でアカウントデータを同期できます。

{% tabs local %}
{% tab データウェアハウス %}
データソースをデータウェアハウスと統合するには:

{% subtabs %}
{% subtab Snowflake %}

1. Snowflake でソーステーブルを作成します。例の名前を使用するか、独自のデータベース名、スキーマ名、テーブル名を選択してください。テーブルの代わりにビューまたはマテリアライズドビューを使用することもできます。
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the account to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Name of the account to be created or updated
         NAME VARCHAR(16777216) NOT NULL,
         --Account fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The account associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. ロール、ウェアハウス、ユーザーを作成し、権限を付与します。別の同期の認証情報がすでにある場合は再利用できます。アカウントテーブルへのアクセス権があることを確認してください。
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. ネットワークポリシーを使用している場合は、CDI サービスが接続できるように Braze の IP をホワイトリストに追加してください。IP の一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。
4. Braze ダッシュボードで、**データ設定** > **クラウドデータ取り込み**に移動し、新しい同期を作成します。
5. 接続の詳細を入力（または既存のものを再利用）し、ソーステーブルを追加します。
6. 同期タイプとして**Accounts**を選択し、統合名とスケジュールを入力します。
7. 同期頻度を選択します。
8. ダッシュボードの公開キーを、作成したユーザーに追加します。これには Snowflake で `SECURITYADMIN` 以上のアクセス権を持つユーザーが必要です。
9. **接続テスト**を選択して設定を確認します。
10. 完了したら、同期を保存します。

{% endsubtab %}
{% subtab Redshift %}

1. Redshift でソーステーブルを作成します。例の名前を使用するか、独自のデータベース名、スキーマ名、テーブル名を選択してください。テーブルの代わりにビューまたはマテリアライズドビューを使用することもできます。
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the account to be created or updated
       id varchar not null,
       --Name of the account to be created or updated
       name varchar not null,
       --Account fields and values that should be added or updated
       payload varchar(max),
       --The account associated with this ID should be deleted
       deleted boolean
    )
    ```
2. ユーザーを作成し、権限を付与します。別の同期の認証情報がすでにある場合は再利用できます。アカウントテーブルへのアクセス権があることを確認してください。
    {% raw %}
    ```sql
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE ACCOUNTS_SYNC TO braze_user;
    ```
    {% endraw %}
3. ファイアウォールまたはネットワークポリシーがある場合は、Braze が Redshift インスタンスにアクセスできるようにしてください。IP の一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endsubtab %}
{% subtab BigQuery %}

1. （オプション）ソーステーブル用に新しいプロジェクトまたはデータセットを作成します。
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. CDI 統合用のソーステーブルを作成します。
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp,
      id STRING,
      name STRING,
      payload JSON,
      deleted BOOLEAN
    );
    ```

    ソーステーブルを作成する際は、以下を参照してください。

    | フィールド名 | 型 | 必須 |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | はい |
    | `PAYLOAD` | JSON | はい |
    | `ID` | String | はい |
    | `NAME` | String | はい |
    | `DELETED` | Boolean | オプション |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="アカウントデータを同期する" }

{:start="3"}
3. ユーザーを作成し、権限を付与します。別の同期の認証情報がすでにある場合は、アカウントテーブルへのアクセス権がある限り再利用できます。

    | 権限 | 目的 |
    |------------|---------|
    | BigQuery Connection User | Brazeが接続できるようにします。 |
    | BigQuery User | Brazeがクエリの実行、メタデータの読み取り、テーブルの一覧表示を行えるようにします。 |
    | BigQuery Data Viewer | Brazeがデータセットとその内容を表示できるようにします。 |
    | BigQuery Job User | Brazeがジョブを実行できるようにします。 |
    {: .reset-td-br-1 .reset-td-br-2 aria-label="アカウントデータを同期する" }

    権限を付与した後、JSON キーを生成します。手順については、[Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) を参照してください。後で Braze ダッシュボードにアップロードします。

{:start="4"}
4. ネットワークポリシーを使用している場合は、Braze の IP が BigQuery インスタンスにアクセスできるようにしてください。IP の一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endsubtab %}
{% subtab Databricks %}

1. ソーステーブル用のカタログまたはスキーマを作成します。
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. CDI 統合用のソーステーブルを作成します。
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp(),
      id STRING,
      name STRING,
      payload STRING, STRUCT, or MAP,
      deleted BOOLEAN
    );
    ```

    ソーステーブルを作成する際は、以下を参照してください。

    | フィールド名 | 型 | 必須 |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | はい |
    | `PAYLOAD` | String、Struct、または Map | はい |
    | `ID` | String | はい |
    | `NAME` | String | はい |
    | `DELETED` | Boolean | オプション |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="アカウントデータを同期する" }

{:start="3"}
3. Databricks で個人アクセストークンを作成します。
    1. ユーザー名を選択し、**User Settings** を選択します。
    2. **Access tokens** タブで、**Generate new token** を選択します。
    3. トークンを識別するためのコメントを追加します（例：「Braze CDI」）。
    4. 有効期限を設定しない場合は **Lifetime (days)** を空白のままにし、**Generate** を選択します。
    5. トークンをコピーし、Braze ダッシュボードで使用するために安全に保存します。

{:start="4"}
4. ネットワークポリシーを使用している場合は、Braze の IP が Databricks インスタンスにアクセスできるようにしてください。IP の一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endsubtab %}
{% subtab Microsoft Fabric %}

1. CDI 統合用に以下のフィールドを持つテーブルを1つ以上作成します。
    ```sql
    CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
    (
      UPDATED_AT DATETIME2(6) NOT NULL,
      PAYLOAD VARCHAR NOT NULL,
      ID VARCHAR NOT NULL,
      NAME VARCHAR NOT NULL,
      DELETED BIT
    )
    GO
    ```

{:start="2"}
2. サービスプリンシパルを作成し、権限を付与します。別の同期の認証情報がすでにある場合は再利用できます。アカウントテーブルへのアクセス権があることを確認してください。

{:start="3"}
3. ネットワークポリシーを使用している場合は、Braze の IP が Microsoft Fabric インスタンスにアクセスできるようにしてください。IP の一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ファイルストレージ %}
ファイルストレージからアカウントデータを同期するには、以下のフィールドを含むソースファイルを作成します。

| フィールド | 必須 | 説明 |
| --- | --- | --- |
| `ID` | はい | 更新または作成するアカウントの ID |
| `NAME` | はい | アカウントの名前 |
| `PAYLOAD` | はい | Brazeのアカウントに同期するフィールドの JSON 文字列 |
| `DELETED` | オプション | Brazeからアカウントを削除することを示すブール値 |
| `UPDATED_AT` | *未サポート* | ファイルストレージでは `UPDATED_AT` 列はサポートされていません |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="アカウントデータを同期する" }

{% alert note %}
ファイル名は AWS のルールに従い、一意である必要があります。一意性を確保するためにタイムスタンプを付加してください。Amazon S3 同期の詳細については、[ファイルストレージ統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)を参照してください。
{% endalert %}

以下の例は、ファイルストレージからアカウントデータを同期するための有効な JSON および CSV 形式を示しています。

{% subtabs %}
{% subtab JSON Accounts %}
```jsonl
{"id":"s3-qa-0","name":"account0","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"id":"s3-qa-1","name":"account1","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":true}
{"id":"s3-qa-2","name":"account2","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":false}
{"id":"s3-qa-3","name":"account3","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
```

{% alert important %}
ソースファイルの各行には有効な JSON が含まれている必要があります。そうでない場合、ファイルはスキップされます。
{% endalert %}
{% endsubtab %}
{% subtab CSV Accounts with Delete %}
```plaintext
ID,NAME,PAYLOAD,DELETED
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}",TRUE
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}",FALSE
```
{% endsubtab %}
{% subtab CSV Accounts without Delete %}
```plaintext
ID,NAME,PAYLOAD
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}"
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}"
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 同期ビューの作成 {#create-a-sync-view}

データウェアハウスに同期ビューを作成すると、追加のクエリを書き直すことなくソースを自動的に更新できます。

たとえば、`account_id`、`account_name`、および3つの追加属性を持つ `account_details_1` というアカウントデータのテーブルがある場合、次のような同期ビューを作成できます。

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [BRAZE_CLOUD_PRODUCTION].[INGESTION].[ACCOUNTS_SYNC]
AS SELECT
    account_id as ID,
    account_name as NAME,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[account_details_1] ;
```
{% endtab %}
{% endtabs %}