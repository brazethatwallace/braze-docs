---
nav_title: データウェアハウスの連携
article_title: データウェアハウスストレージの連携
alias: /partners/databricks/
description: "このページでは、Brazeのクラウドデータ取り込みを使用して、関連するデータをSnowflake、Redshift、BigQuery、およびDatabricksの連携と同期する方法について説明します。"
page_order: 3
page_type: reference
---

# データウェアハウスストレージの連携 {#data-warehouse-storage-integrations}

> このページでは、Brazeのクラウドデータ取り込み（CDI）を使用して、関連するデータをSnowflake、Redshift、BigQuery、およびDatabricksの連携と同期する方法について説明します。

## データウェアハウス統合の設定 {#setting-up-data-warehouse-integrations}

Cloud Data Ingestion の統合には、Braze側とデータウェアハウスインスタンスの両方でいくつかの設定が必要です。以下のステップに従って統合を設定してください。

{% tabs %}
{% tab Snowflake %}
1. Snowflakeインスタンスで、Brazeに同期するテーブルまたはビューを設定します。
2. Brazeダッシュボードで新しいSnowflakeソースを作成します。
3. Brazeダッシュボードで提供される公開キーを取得し、[認証用のSnowflakeユーザーに追加](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)します。
4. Brazeダッシュボードで同期を作成し、統合をテストして、同期を開始します。

{% alert tip %}
[Snowflakeクイックスタートガイド](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)では、Snowflake StreamsとCDIを使用してBrazeにデータを同期する自動化パイプラインの作成に必要なサンプルコードとステップを説明しています。
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. 同期したいRedshiftテーブルへのBrazeのアクセスが許可されていることを確認してください。BrazeはインターネットからRedshiftに接続します。
2. Redshiftインスタンスで、Brazeに同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 統合をテストして同期を開始します。

{% alert note %}
同期ごとに処理される行数は、データウェアハウスのパフォーマンス、ネットワークレイテンシー、および同期クエリに一致する新しいデータの量によって異なります。統合の**同期履歴**をダッシュボードで使用して、最近の実行の所要時間と行数を確認できます。
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. サービスアカウントを作成し、同期したいデータを含むBigQueryプロジェクトとデータセットへのアクセスを許可します。
2. BigQueryアカウントで、Brazeに同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 統合をテストして同期を開始します。
{% endtab %}
{% tab Databricks %}
1. サービスアカウントを作成し、同期したいデータを含むDatabricksプロジェクトとデータセットへのアクセスを許可します。
2. Databricksアカウントで、Brazeに同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 統合をテストして同期を開始します。

{% alert important %}
BrazeがClassicおよびPro SQLインスタンスに接続する際、2〜5分のウォームアップ時間がかかる場合があり、接続の設定やテスト時、またスケジュールされた同期の開始時に遅延が発生する可能性があります。サーバーレスSQLインスタンスを使用するとウォームアップ時間が最小化され、クエリスループットが向上しますが、統合コストがわずかに高くなる場合があります。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、Fabric APIへのアクセスを付与します。
2. 共有ワークスペースを設定し、サービスプリンシパルにアクセスを付与します。
3. 共有Fabricワークスペースで、Brazeに同期するテーブルまたはビューを設定します。
4. Brazeダッシュボードで新しいソースと同期を作成します。
5. 統合をテストして同期を開始します。
{% endtab %}
{% endtabs %}

### ステップ1: テーブルまたはビューを設定する {#step-1-set-up-tables-or-views}

開始する前に、[Cloud Data Ingestionのテーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)を確認し、ソーステーブルの要件と`PAYLOAD`のフォーマット要件を比較してください。

{% alert note %}
ソーステーブルまたはビューには、次のセクションのタブでデータウェアハウスごとにリストされていないカラムを含めることができます（例：監査やハッシュ用のカラム）。Brazeはこれらのタブに記載されたカラムのみを読み取り、その他のカラムはCloud Data Ingestionの同期中に使用されません。
{% endalert %}

{% tabs %}
{% tab Snowflake %}

#### ステップ1.1: テーブルを設定する {#step-11-set-up-the-table}

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

データベース、スキーマ、テーブルの名前は自由に付けられますが、カラム名は上記の定義と一致する必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、正確な境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新するユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これらの2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つだけです。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成され、Cloud Data Ingestionを通じてBraze IDで新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期するフィールドのJSON文字列です。

#### ステップ1.2: ロールとデータベース権限を設定する {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

必要に応じて名前を変更できますが、権限は上記の例と一致する必要があります。

#### ステップ1.3: データウェアハウスを設定しBrazeロールにアクセスを付与する {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
データウェアハウスには**auto-resume**フラグがオンになっている必要があります。オンでない場合は、クエリ実行時にBrazeがオンにできるよう、データウェアハウスに対して追加の`OPERATE`権限をBrazeに付与してください。
{% endalert %}

#### ステップ1.4: ユーザーを設定する {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このステップの後、接続情報をBrazeと共有し、ユーザーに追加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じSnowflakeアカウントに接続する場合、統合を作成する各Brazeワークスペースに対して一意のユーザーを作成する必要があります。ワークスペース内では、統合間で同じユーザーを再利用できますが、同じSnowflakeアカウント上のユーザーがワークスペース間で重複すると、統合の作成が失敗します。
{% endalert %}

#### ステップ1.5: SnowflakeネットワークポリシーでBraze IPを許可する（オプション） {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Snowflakeアカウントの設定によっては、Snowflakeネットワークポリシーで以下のIPアドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関するSnowflakeドキュメントを参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### ステップ1.1: テーブルを設定する

オプションで、ソーステーブルを格納する新しいデータベースとスキーマを設定します。
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
CDI統合に使用するテーブル（またはビュー）を作成します。
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

データベース、スキーマ、テーブルの名前は自由に付けられますが、カラム名は上記の定義と一致する必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、正確な境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新するユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これらの2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つだけです。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成され、Cloud Data Ingestionを通じてBraze IDで新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期するフィールドのJSON文字列です。

#### ステップ1.2: ユーザーを作成し権限を付与する {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

このユーザーに必要な最小限の権限です。複数のCDI統合を作成する場合、スキーマへの権限を付与するか、グループを使用して権限を管理することをお勧めします。

#### ステップ1.3: Braze IPへのアクセスを許可する {#step-13-allow-access-to-braze-ips}

ファイアウォールやその他のネットワークポリシーがある場合、RedshiftインスタンスへのネットワークアクセスをBrazeに付与する必要があります。RedshiftのURLエンドポイントの例は「example-cluster.ap-northeast-2.redshift.amazonaws.com」です。

知っておくべき重要な点:
- セキュリティグループの変更が必要な場合もあり、RedshiftのデータにBrazeがアクセスできるようにする必要があります。
- テーブルのIPおよびRedshiftクラスターのクエリに使用するポート（デフォルトは5439）でのインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートでのRedshift TCP接続を明示的に許可する必要があります。
- Redshiftクラスターのエンドポイントは、Brazeがクラスターに接続できるようにパブリックにアクセス可能である必要があります。
     - Redshiftクラスターをパブリックにアクセス可能にしたくない場合は、SSHトンネルを使用するVPCとEC2インスタンスを設定してRedshiftデータにアクセスできます。詳細については、[AWSナレッジセンターの記事](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。

Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### ステップ1.1: テーブルを設定する

オプションで、ソーステーブルを格納する新しいプロジェクトまたはデータセットを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

以下のフィールドでCDI統合に使用する1つ以上のテーブルを作成します。

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ1.1: テーブルを設定する" }

プロジェクト、データセット、テーブルの名前は自由に付けられますが、カラム名は上記の定義と一致する必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、正確な境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新するユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これらの2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つだけです。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成され、Cloud Data Ingestionを通じてBraze IDで新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期するフィールドのJSON文字列です。

{% alert important %}
**BigQueryのパーティショニング**

CDIはBigQueryのパーティションをサポートしています。`UPDATED_AT`の関数でパーティションを分割する場合（例：データセットのサイズに応じて日、週、または時間の粒度で）、BigQueryはスキャンが必要なデータを絞り込むことができます。これにより、非常に大きなテーブルのパフォーマンスと効率が向上します。

他のフィールドでパーティションを分割しないでください。特定のデータに最適な設定を見つけるために、異なる構成をテストしてください。

すべてのCDIクエリは`UPDATED_AT`でフィルタリングしますが、この動作は変更される可能性があります。クエリにこの句を含める必要がない前提でテーブルスキーマを設計してください。

詳細については、[BigQueryのパーティショニングに関するドキュメント](https://docs.cloud.google.com/bigquery/docs/partitioned-tables)を参照してください。
{% endalert %}

#### ステップ1.2: サービスアカウントを作成し権限を付与する {#step-12-create-a-service-account-and-grant-permissions}

Brazeがテーブルに接続してデータを読み取るために使用するサービスアカウントをGCPで作成します。サービスアカウントには以下の権限が必要です。

- **BigQuery Connection User:** Brazeが接続を行えるようにします。
- **BigQuery User:** クエリの実行、データセットメタデータの読み取り、テーブルの一覧表示のためのアクセスをBrazeに提供します。
- **BigQuery Data Viewer:** データセットとその内容を表示するためのアクセスをBrazeに提供します。
- **BigQuery Job User:** ジョブを実行するためのアクセスをBrazeに提供します。

サービスアカウントを作成して権限を付与した後、JSONキーを生成します。詳細については、[サービスアカウントキーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。このキーを後のステップでBrazeダッシュボードにアップロードします。

#### ステップ1.3: Braze IPへのアクセスを許可する

ネットワークポリシーが設定されている場合、BigQueryインスタンスへのネットワークアクセスをBrazeに付与する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### ステップ1.1: テーブルを設定する

オプションで、ソーステーブルを格納する新しいカタログまたはスキーマを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

以下のフィールドでCDI統合に使用する1つ以上のテーブルを作成します。


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT, or MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ1.1: テーブルを設定する" }

スキーマとテーブルの名前は自由に付けられますが、カラム名は上記の定義と一致する必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、正確な境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新するユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これらの2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つだけです。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成され、Cloud Data Ingestionを通じてBraze IDで新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期するフィールドの文字列または構造体です。

#### ステップ1.2: アクセストークンを作成する {#step-12-create-an-access-token}

BrazeがDatabricksにアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricksワークスペースで、上部のバーにあるDatabricksユーザー名を選択し、ドロップダウンから**User Settings**を選択します。
2. アクセストークンタブで、**Generate new token**を選択します。
3. このトークンを識別するためのコメント（「Braze CDI」など）を入力し、Lifetime (days)ボックスを空白のままにしてトークンの有効期限を無期限に変更します。
4. **Generate**を選択します。
5. 表示されたトークンをコピーし、**Done**を選択します。

認証情報作成ステップでBrazeダッシュボードに入力する必要があるまで、トークンを安全な場所に保管してください。

#### ステップ1.3: Braze IPへのアクセスを許可する

ネットワークポリシーが設定されている場合、DatabricksインスタンスへのネットワークアクセスをBrazeに付与する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ1.1: サービスプリンシパルを設定しアクセスを付与する {#step-11-set-up-the-service-principal-and-grant-access}
BrazeはEntra ID認証を使用するサービスプリンシパルでFabricデータウェアハウスに接続します。Brazeが使用する新しいサービスプリンシパルを作成し、必要に応じてFabricリソースへのアクセスを付与してください。Brazeが接続するには以下の情報が必要です。

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azureではサービスプリンシパルシークレットに無制限の有効期限を設定できません。Brazeへのデータフローを維持するために、有効期限が切れる前に認証情報を更新してください。
{% endalert %}

#### ステップ1.2: Fabricリソースへのアクセスを付与する {#step-12-grant-access-to-fabric-resources}
Brazeがあなたのデータに接続できるようにFabricインスタンスへのアクセスを提供します。Fabric管理ポータルで、**Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**に移動します。

* **Developer settings**で、**Service principals can use Fabric APIs**を有効にして、BrazeがMicrosoft Entra IDを使用して接続できるようにします。
* **OneLake settings**で、**Users can access data stored in OneLake with apps external to Fabric**を有効にして、サービスプリンシパルが外部アプリからデータにアクセスできるようにします。

#### ステップ1.3: 共有ワークスペースを設定しアクセスを付与する {#step-13-set-up-a-shared-workspace-and-grant-access}

Brazeに接続するFabricリソースは、共有ワークスペースに配置する必要があります。デフォルトの**My Workspace**のみを使用していた場合は、新しい共有ワークスペースを作成してください。

1. ナビゲーションメニューで**Workspaces**を選択し、**+ New workspace**を選択します。
2. ワークスペースの**Name**を入力し、**Apply**を選択します。

共有ワークスペースができたら、サービスプリンシパルにアクセスを付与します。

1. ワークスペースを選択し、**Manage Access**を選択します。
2. **+ Add people or groups**を選択します。
3. ステップ1.1で作成したサービスプリンシパルの名前を検索して選択します。表示されない場合は、ステップ1.2で**Service principals can use Fabric APIs**の設定が有効になっていることを確認してください。
4. ロールのドロップダウンで**Contributor**を選択します。

これでサービスプリンシパルは、SQLエンドポイントを通じてこのワークスペースのFabricデータウェアハウスリソースにアクセスできるようになります。Brazeに使用するデータウェアハウスも含まれます。

#### ステップ1.4: テーブルを設定する {#step-14-set-up-the-table}
BrazeはFabric Warehouseのテーブルとビューをサポートしています。新しいデータウェアハウスを作成する必要がある場合は、ステップ1.3の共有ワークスペース内に作成してください。FabricコンソールでCreate **> Data Warehouse > Warehouse**に移動します。

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

データウェアハウス、スキーマ、テーブルまたはビューの名前は自由に付けられますが、カラム名は上記の定義と一致する必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、正確な境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新するユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これらの2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つだけです。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成され、Cloud Data Ingestionを通じてBraze IDで新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期するフィールドのJSON文字列です。


#### ステップ1.5: データウェアハウスの接続文字列を取得する {#step-15-get-warehouse-connection-string}
データウェアハウスのSQLエンドポイントを取得するには、Fabricの**ワークスペース**に移動し、アイテムリストでデータウェアハウス名にカーソルを合わせ、**Copy SQL connection string**を選択します。

![Microsoft AzureのFabricコンソールページ。SQL接続文字列を取得する場所です。]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### ステップ1.6: ファイアウォールでBraze IPを許可する（オプション） {#step-16-allow-braze-ips-in-firewall-optional}

Microsoft Fabricアカウントの設定によっては、Brazeからのトラフィックを許可するために、ファイアウォールで以下のIPアドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[Entra条件付きアクセス](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)に関するドキュメントを参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ2: Brazeダッシュボードで新しいソースを作成する {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Snowflake**を選択します。

#### ステップ2.1: Snowflake接続情報を追加する {#step-21-add-snowflake-connection-information}

ソースの名前を選択し、Snowflakeの認証情報と設定を入力して、次のステップに進みます。

続行する前に、**Snowflake Account Locator**に入力する値を確認してください。

**Snowflake Account Locator**フィールドには、Snowflakeの[アカウント識別子](https://docs.snowflake.com/en/user-guide/admin-account-identifier)を入力します。`myorganization-myaccount`のようなアカウント識別子の値のみを入力してください。`https://`、`.snowflakecomputing.com`、またはパスを含めないでください。

Snowflakeアカウント識別子を見つけるには:

1. Snowsightでアカウントメニューを選択します。
2. **View account details**を選択します。
3. **Account identifier**の値をコピーします。
4. Snowflake URLからコピーする場合は、`.snowflakecomputing.com`の前の値のみを使用してください。

#### ステップ2.2: Brazeユーザーに公開キーを追加する {#step-22-add-a-public-key-to-the-braze-user}

認証情報と設定を入力した後、**Save credentials**をクリックしてRSAキーを生成し、Snowflakeに戻って設定を完了します。ダッシュボードに表示される公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加します。

この方法の詳細については、[Snowflakeドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。キーをローテーションする場合、Brazeは新しいキーペアを生成し、新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Amazon Redshift**を選択します。

#### ステップ2.1: Redshift接続情報とソーステーブルを追加する {#step-21-add-redshift-connection-information-and-source-table}

ソースの名前を選択し、Redshiftの認証情報と設定を入力します。プライベートネットワークトンネルを使用する場合は、スライダーを切り替えてトンネル情報を入力します。その後、次のステップに進みます。

{% alert note %}
Brazeダッシュボードの**Database name**フィールドは、Amazon Redshiftがデータベース識別子で追加の文字をサポートしているにもかかわらず、文字（A–Z、a–z）、数字（0–9）、およびアンダースコア（_）のみを受け付けます。
{% endalert %}

#### ステップ2.2: 接続をテストしてソースに接続する {#step-22-test-connection-and-connect-to-source}

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

#### トラブルシューティング: 無効なスナップショット識別子 {#troubleshooting-invalid-snapshot-identifier}

**Test connection**または同期設定中にBrazeが`Invalid snapshot identifier`エラーを返した場合、ソースオブジェクトがクエリされる際に使用されるスナップショット参照をRedshiftが解決できません。

Redshiftでは、スナップショットはクラスターのポイントインタイムバックアップです。各スナップショットにはRedshiftがそのバックアップ状態を参照するために使用する一意の識別子があります。詳細については、[Amazon Redshiftスナップショットとバックアップ](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)を参照してください。

このエラーは、Brazeがソースオブジェクトを検証している間にメタデータが変更された場合に発生する可能性があります。例えば、スナップショットのコピー、復元、またはレプリケーション関連の操作中などです。詳細については、[別のAWSリージョンへのスナップショットのコピー](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html)と[スナップショットからのクラスターの復元](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html)を参照してください。

トラブルシューティングの手順:

1. クラスターエンドポイント、データベース、スキーマ、オブジェクト名を含むBrazeのソース設定を確認します。
2. Redshiftで直接同じクエリを実行して、テーブルまたはビューが読み取り可能で安定していることを確認します。
3. アクティブなスナップショット、復元、リサイズ、またはレプリケーションアクティビティが完了した後に再試行します。
4. 問題が解決しない場合は、頻繁に変更されるベーステーブルの代わりにマテリアライズドビューをクエリします。

マテリアライズドビューは、スケジュールに従って更新できる事前計算されたクエリ結果を保存するため、CDI同期の読み取りをより安定させることができます。詳細については、[Amazon Redshiftのマテリアライズドビュー](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html)を参照してください。

例:

```sql
CREATE MATERIALIZED VIEW ingestion.users_attributes_mv AS
SELECT updated_at, external_id, alias_label, alias_name, braze_id, email, phone, payload
FROM ingestion.users_attributes_sync;

REFRESH MATERIALIZED VIEW ingestion.users_attributes_mv;
```

マテリアライズドビューを作成した後、Braze CDI同期のソースオブジェクトとしてベーステーブルの代わりにマテリアライズドビュー名を使用してください。
{% endtab %}
{% tab BigQuery %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Google BigQuery**を選択します。

#### ステップ2.1: BigQuery接続情報とソーステーブルを追加する {#step-21-add-bigquery-connection-information-and-source-table}

ソースの名前を選択します。次に、JSONキーをアップロードし、サービスアカウントの名前を入力します。その後、残りの設定フィールドを入力します。

#### ステップ2.2: 接続をテストしてソースに接続する

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% endtab %}
{% tab Databricks %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Databricks**を選択します。

#### ステップ2.1: Databricks接続情報とソーステーブルを追加する {#step-21-add-databricks-connection-information-and-source-table}

ソースの名前を選択し、Databricksの認証情報と設定を入力します。その後、次のステップに進みます。

#### ステップ2.2: 接続をテストしてソースに接続する

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
ソースを作成する前に、正常にテストする必要があります。作成ページを閉じると、ソースは保存されません。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

Brazeダッシュボードで、Data Settings > Cloud Data Ingestion > Sourcesに移動し、**Add data source**を選択して、**Microsoft Fabric**を選択します。

#### ステップ2.1: Cloud Data Ingestion同期を設定する {#step-21-set-up-a-cloud-data-ingestion-sync}

ソースの名前を選択し、Microsoft Fabricの認証情報と設定を入力します。
- **Credentials Name**はBrazeにおけるこの認証情報のラベルです。わかりやすい値を設定できます。
- テナントID、プリンシパルID、クライアントシークレット、および接続文字列の取得方法については、セクション1のステップを参照してください。

#### ステップ2.2: 接続をテストしてソースに接続する

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
ソースを作成する前に、正常にテストする必要があります。作成ページを閉じると、ソースは保存されません。
{% endalert %}

{% endtab %}

{% endtabs %}

### ステップ3: Brazeダッシュボードで新しい同期を作成する {#step-3-create-a-new-sync-in-the-braze-dashboard}
**Data Settings** > **Cloud Data Ingestion** > **Syncs**に移動し、**Create data sync**を選択します。

{% tabs %}
{% tab Snowflake %}

#### ステップ3.1: 同期の詳細を設定して接続をテストする {#step-31-configure-sync-details-and-test-connection}
同期の名前を選択します。次に、アクティブなソースを選択し、同期用のソーステーブルを入力します。データタイプを選択して**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存できます。
{% endalert %}

#### ステップ3.2: 通知設定を追加する {#step-32-add-notification-preferences}
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題など、グローバルまたは同期レベルのエラー通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には以下が含まれます:

- 接続の問題
- リソースの不足
- 権限の問題
- （カタログ同期のみ）カタログの階層がスペース不足

#### ステップ3.3: スケジューリング {#step-33-scheduling}
最後に、同期を非繰り返しまたは繰り返しとして設定します。

非繰り返し同期は、手動またはAPI経由でトリガーできます。

繰り返し同期は、15分ごとから月1回までの頻度を設定できます。Brazeは繰り返し同期をUTCタイムゾーンでスケジュールします。

{% endtab %}

{% tab Redshift %}

#### ステップ3.1: 同期の詳細を設定して接続をテストする
同期の名前を選択します。次に、アクティブなソースを選択し、同期用のソーステーブルを入力します。データタイプを選択して**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存できます。
{% endalert %}

#### ステップ3.2: 通知設定を追加する
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題など、グローバルまたは同期レベルのエラー通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には以下が含まれます:

- 接続の問題
- リソースの不足
- 権限の問題

（カタログ同期のみ）カタログの階層がスペース不足

#### ステップ3.3: スケジューリング
最後に、同期を非繰り返しまたは繰り返しとして設定します。

非繰り返し同期は、手動またはAPI経由でトリガーできます。

繰り返し同期は、15分ごとから月1回までの頻度を設定できます。Brazeは繰り返し同期をUTCタイムゾーンでスケジュールします。

{% endtab %}

{% tab BigQuery %}

#### ステップ3.1: 同期の詳細を設定して接続をテストする
同期の名前を選択します。次に、アクティブなソースを選択し、同期用のソーステーブルを入力します。データタイプを選択して**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存できます。
{% endalert %}

#### ステップ3.2: 通知設定を追加する
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題など、グローバルまたは同期レベルのエラー通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には以下が含まれます:

- 接続の問題
- リソースの不足
- 権限の問題

（カタログ同期のみ）カタログの階層がスペース不足

#### ステップ3.3: スケジューリング
最後に、同期を非繰り返しまたは繰り返しとして設定します。

非繰り返し同期は、手動またはAPI経由でトリガーできます。

繰り返し同期は、15分ごとから月1回までの頻度を設定できます。Brazeは繰り返し同期をUTCタイムゾーンでスケジュールします。

{% endtab %}

{% tab Databricks %}

#### ステップ3.1: 同期の詳細を設定して接続をテストする
同期の名前を選択します。次に、アクティブなソースを選択し、同期用のソーステーブルを入力します。データタイプを選択して**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存できます。
{% endalert %}

#### ステップ3.2: 通知設定を追加する
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題など、グローバルまたは同期レベルのエラー通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には以下が含まれます:
- 接続の問題
- リソースの不足
- 権限の問題

（カタログ同期のみ）カタログの階層がスペース不足

#### ステップ3.3: スケジューリング
最後に、同期を非繰り返しまたは繰り返しとして設定します。

非繰り返し同期は、手動またはAPI経由でトリガーできます。

繰り返し同期は、15分ごとから月1回までの頻度を設定できます。Brazeは繰り返し同期をUTCタイムゾーンでスケジュールします。

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ3.1: 同期の詳細を設定して接続をテストする

同期の名前を選択します。次に、アクティブなソースを選択し、同期用のソーステーブルを入力します。データタイプを選択して**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存できます。
{% endalert %}

#### ステップ3.2: 通知設定を追加する
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題など、グローバルまたは同期レベルのエラー通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には以下が含まれます:

- 接続の問題
- リソースの不足
- 権限の問題

（カタログ同期のみ）カタログの階層がスペース不足

#### ステップ3.3: スケジューリング
最後に、同期を非繰り返しまたは繰り返しとして設定します。

非繰り返し同期は、手動またはAPI経由でトリガーできます。

繰り返し同期は、15分ごとから月1回までの頻度を設定できます。Brazeは繰り返し同期をUTCタイムゾーンでスケジュールします。

{% endtab %}
{% endtabs %}

{% alert note %}
統合が下書きからアクティブ状態に移行するには、テストに成功する必要があります。作成ページを閉じた場合、統合は保存されるため、詳細ページに戻って変更やテストを行うことができます。
{% endalert %}

## 追加の統合またはユーザーの設定（オプション） {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Brazeとの統合は複数設定できますが、各統合は異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じSnowflakeアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーとロールを再利用する場合、公開キーを再度追加する必要はありません。
{% endtab %}
{% tab Redshift %}
Brazeとの統合は複数設定できますが、各統合は異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じSnowflakeまたはRedshiftアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーを再利用する場合、そのユーザーがすべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。
{% endtab %}
{% tab BigQuery %}

Brazeとの統合は複数設定できますが、各統合は異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じBigQueryアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーを再利用する場合、そのユーザーがすべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Databricks %}

Brazeとの統合は複数設定できますが、各統合は異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じDatabricksアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーを再利用する場合、そのユーザーがすべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Microsoft Fabric %}

Brazeとの統合は複数設定できますが、各統合は異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じFabricアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーを再利用する場合、そのユーザーがすべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% endtabs %}

## 同期の実行 {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
有効化すると、設定時に構成されたスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、通常スケジュールされている今後の同期には影響しません。

{% endtab %}
{% tab Redshift %}
有効化すると、設定時に構成されたスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、通常スケジュールされている今後の同期には影響しません。

{% endtab %}
{% tab BigQuery %}

有効化すると、設定時に構成されたスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、通常スケジュールされている今後の同期には影響しません。

{% endtab %}
{% tab Databricks %}

有効化すると、設定時に構成されたスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、通常スケジュールされている今後の同期には影響しません。

{% endtab %}
{% tab Microsoft Fabric %}

有効化すると、設定時に構成されたスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、通常スケジュールされている今後の同期には影響しません。

{% endtab %}

{% endtabs %}