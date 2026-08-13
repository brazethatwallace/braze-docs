---
nav_title: データウェアハウスの連携
article_title: データウェアハウスの連携
alias: /partners/databricks/
description: "このページでは、Brazeのクラウドデータ取り込みを使用して、関連するデータをSnowflake、Redshift、BigQuery、およびDatabricksの連携と同期する方法について説明します。"
page_order: 3
page_type: reference

---

# データウェアハウスストレージの連携 {#data-warehouse-storage-integrations}

> このページでは、Brazeのクラウドデータ取り込み（CDI）を使用して、関連するデータをSnowflake、Redshift、BigQuery、およびDatabricksの連携と同期する方法について説明します。

## データウェアハウス統合の設定 {#setting-up-data-warehouse-integrations}

クラウドデータ取り込み統合には、Braze側とデータウェアハウスインスタンスの両方でいくつかの設定が必要です。以下のステップに従って統合を設定してください。

{% tabs %}
{% tab Snowflake %}
1. Snowflakeインスタンスで、Brazeに同期するテーブルまたはビューを設定します。
2. Brazeダッシュボードで新しいSnowflakeソースを作成します。
3. Brazeダッシュボードで提供される公開キーを取得し、[認証のためにSnowflakeユーザーに追加](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)します。
4. Brazeダッシュボードで同期を作成し、統合をテストして、同期を開始します。

{% alert tip %}
[Snowflakeクイックスタートガイド](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)では、サンプルコードを提供し、Snowflake StreamsとCDIを使用してBrazeにデータを同期する自動パイプラインを作成するために必要なステップを説明しています。
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. 同期したいRedshiftテーブルへのBrazeアクセスが許可されていることを確認します。BrazeはインターネットからRedshiftに接続します。
2. Redshiftインスタンスで、Brazeに同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 統合をテストして、同期を開始します。

{% alert note %}
同期ごとに処理される行数は、ウェアハウスのパフォーマンス、ネットワークレイテンシー、および同期クエリに一致する新しいデータの量に依存します。ダッシュボードの統合**同期履歴**を使用して、最近の実行の所要時間と行数を確認できます。
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. サービスアカウントを作成し、同期したいデータを含むBigQueryプロジェクトとデータセットへのアクセスを許可します。
2. BigQueryアカウントで、Brazeに同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 統合をテストして、同期を開始します。
{% endtab %}
{% tab Databricks %}
1. サービスアカウントを作成し、同期したいデータを含むDatabricksプロジェクトとデータセットへのアクセスを許可します。
2. Databricksアカウントで、Brazeに同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 統合をテストして、同期を開始します。

{% alert important %}
BrazeがClassicおよびPro SQLインスタンスに接続する際、2〜5分のウォームアップ時間が発生する場合があり、接続の設定やテスト中、およびスケジュールされた同期の開始時に遅延が生じることがあります。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリスループットが向上しますが、統合コストがわずかに高くなる場合があります。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、Fabric APIへのアクセスを許可します。
2. 共有ワークスペースを設定し、サービスプリンシパルにアクセスを許可します。
3. 共有Fabricワークスペースで、Brazeに同期するテーブルまたはビューを設定します。
4. Brazeダッシュボードで新しいソースと同期を作成します。
5. 統合をテストして、同期を開始します。
{% endtab %}
{% endtabs %}

### ステップ1: テーブルまたはビューを設定する {#step-1-set-up-tables-or-views}

開始する前に、[クラウドデータ取り込みのテーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)を確認して、ソーステーブルの要件と`PAYLOAD`のフォーマット要件を比較してください。

{% alert note %}
ソーステーブルまたはビューには、次のセクションのタブでウェアハウスごとにリストされていないカラムを含めることができます（例：監査やハッシュ用）。Brazeはそれらのタブに記載されたカラムのみを読み取ります。その他のカラムはクラウドデータ取り込み同期中に使用されません。
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

データベース、スキーマ、テーブルの名前は自由に設定できますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には1つの識別子のみを含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新したいユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これら2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに1つの`alias_name`のみです。
    - `BRAZE_ID` - Brazeユーザー識別子です。Braze SDKによって生成され、クラウドデータ取り込みを通じてBraze IDを使用して新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話番号の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期したいフィールドのJSON文字列です。

#### ステップ1.2: ロールとデータベース権限を設定する {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

必要に応じて名前を更新しますが、権限は上記の例と一致させる必要があります。

#### ステップ1.3: ウェアハウスを設定し、Brazeロールにアクセスを許可する {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスには**auto-resume**フラグがオンになっている必要があります。オンになっていない場合、クエリ実行時にBrazeがウェアハウスをオンにできるよう、ウェアハウスに対する追加の`OPERATE`権限をBrazeに付与してください。
{% endalert %}

#### ステップ1.4: ユーザーを設定する {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このステップの後、接続情報をBrazeと共有して、ユーザーに追加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じSnowflakeアカウントに接続する場合、統合を作成する各Brazeワークスペースに対して一意のユーザーを作成する必要があります。ワークスペース内では、統合間で同じユーザーを再利用できますが、同じSnowflakeアカウント上のユーザーがワークスペース間で重複している場合、統合の作成は失敗します。
{% endalert %}

#### ステップ1.5: SnowflakeネットワークポリシーでBraze IPを許可する（オプション） {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Snowflakeアカウントの設定によっては、Snowflakeネットワークポリシーで以下のIPアドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関するSnowflakeの関連ドキュメントを参照してください。

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

データベース、スキーマ、テーブルの名前は自由に設定できますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には1つの識別子のみを含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新したいユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これら2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに1つの`alias_name`のみです。
    - `BRAZE_ID` - Brazeユーザー識別子です。Braze SDKによって生成され、クラウドデータ取り込みを通じてBraze IDを使用して新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話番号の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期したいフィールドのJSON文字列です。

#### ステップ1.2: ユーザーを作成し、権限を付与する {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

これらはこのユーザーに必要な最小限の権限です。複数のCDI統合を作成する場合は、スキーマに対する権限を付与するか、グループを使用して権限を管理することをお勧めします。

#### ステップ1.3: Braze IPへのアクセスを許可する {#step-13-allow-access-to-braze-ips}

ファイアウォールやその他のネットワークポリシーがある場合、RedshiftインスタンスへのネットワークアクセスをBrazeに許可する必要があります。RedshiftのURLエンドポイントの例は「example-cluster.ap-northeast-2.redshift.amazonaws.com」です。

知っておくべき重要な点：
- セキュリティグループを変更して、BrazeがRedshiftのデータにアクセスできるようにする必要がある場合もあります。
- テーブル内のIPと、Redshiftクラスターのクエリに使用するポート（デフォルトは5439）でインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートでのRedshift TCP接続を明示的に許可する必要があります。
- Redshiftクラスターのエンドポイントは、Brazeがクラスターに接続するためにパブリックにアクセス可能である必要があります。
     - Redshiftクラスターをパブリックにアクセス可能にしたくない場合は、VPCとEC2インスタンスを設定してSSHトンネルを使用してRedshiftデータにアクセスできます。詳細については、[AWSナレッジセンターの記事](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。

Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### ステップ1.1: テーブルを設定する

オプションで、ソーステーブルを格納する新しいプロジェクトまたはデータセットを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

以下のフィールドを持つCDI統合用のテーブルを1つ以上作成します。

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

プロジェクト、データセット、テーブルの名前は自由に設定できますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には1つの識別子のみを含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新したいユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これら2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに1つの`alias_name`のみです。
    - `BRAZE_ID` - Brazeユーザー識別子です。Braze SDKによって生成され、クラウドデータ取り込みを通じてBraze IDを使用して新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話番号の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期したいフィールドのJSON文字列です。

{% alert important %}
**BigQueryパーティショニング**

CDIはBigQueryのパーティションをサポートしています。`UPDATED_AT`の関数でパーティションを設定すると（例：データセットのサイズに応じて日、週、または時間の粒度で）、BigQueryはスキャンする必要のあるデータを削減できます。これにより、非常に大きなテーブルのパフォーマンスと効率が向上します。

他のフィールドでパーティションを設定しないでください。さまざまな設定をテストして、特定のデータに最適なセットアップを見つけてください。

すべてのCDIクエリは`UPDATED_AT`でフィルタリングしますが、この動作は変更される可能性があります。クエリにこの句を含めることを*必須としない*ようにテーブルスキーマを設計してください。

詳細については、[BigQueryパーティショニングのドキュメント](https://docs.cloud.google.com/bigquery/docs/partitioned-tables)を参照してください。
{% endalert %}

#### ステップ1.2: サービスアカウントを作成し、権限を付与する {#step-12-create-a-service-account-and-grant-permissions}

GCPでBrazeがテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには以下の権限が必要です。

- **BigQuery Connection User:** Brazeが接続を確立できるようにします。
- **BigQuery User:** クエリの実行、データセットメタデータの読み取り、テーブルの一覧表示へのアクセスをBrazeに提供します。
- **BigQuery Data Viewer:** データセットとその内容を表示するアクセスをBrazeに提供します。
- **BigQuery Job User:** ジョブを実行するアクセスをBrazeに提供します。

サービスアカウントを作成して権限を付与した後、JSONキーを生成します。詳細については、[サービスアカウントキーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。このキーは後のステップでBrazeダッシュボードにアップロードします。

#### ステップ1.3: Braze IPへのアクセスを許可する

ネットワークポリシーが設定されている場合、BigQueryインスタンスへのネットワークアクセスをBrazeに許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### ステップ1.1: テーブルを設定する

オプションで、ソーステーブルを格納する新しいカタログまたはスキーマを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

以下のフィールドを持つCDI統合用のテーブルを1つ以上作成します。


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

スキーマとテーブルの名前は自由に設定できますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には1つの識別子のみを含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新したいユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これら2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに1つの`alias_name`のみです。
    - `BRAZE_ID` - Brazeユーザー識別子です。Braze SDKによって生成され、クラウドデータ取り込みを通じてBraze IDを使用して新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話番号の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期したいフィールドの文字列またはstructです。

#### ステップ1.2: アクセストークンを作成する {#step-12-create-an-access-token}

BrazeがDatabricksにアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricksワークスペースで、上部バーのDatabricksユーザー名を選択し、ドロップダウンから**User Settings**を選択します。
2. アクセストークンタブで、**Generate new token**を選択します。
3. このトークンを識別するのに役立つコメント（「Braze CDI」など）を入力し、Lifetime (days)ボックスを空白のままにしてトークンの有効期限を無期限に変更します。
4. **Generate**を選択します。
5. 表示されたトークンをコピーし、**Done**を選択します。

認証情報の作成ステップでBrazeダッシュボードに入力する必要があるまで、トークンを安全な場所に保管してください。

#### ステップ1.3: Braze IPへのアクセスを許可する

ネットワークポリシーが設定されている場合、DatabricksインスタンスへのネットワークアクセスをBrazeに許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ1.1: サービスプリンシパルを設定し、アクセスを許可する {#step-11-set-up-the-service-principal-and-grant-access}
BrazeはEntra ID認証を使用するサービスプリンシパルを使用してFabricウェアハウスに接続します。Brazeが使用する新しいサービスプリンシパルを作成し、必要に応じてFabricリソースへのアクセスを許可します。Brazeが接続するには以下の詳細が必要です。

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azureではサービスプリンシパルシークレットに無期限の有効期限を設定できません。Brazeへのデータフローを維持するために、認証情報の有効期限が切れる前に更新することを忘れないでください。
{% endalert %}

#### ステップ1.2: Fabricリソースへのアクセスを許可する {#step-12-grant-access-to-fabric-resources}
BrazeがFabricインスタンスに接続するためのアクセスを提供します。Fabric管理ポータルで、**Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**に移動します。

* **Developer settings**で、**Service principals can use Fabric APIs**を有効にして、BrazeがMicrosoft Entra IDを使用して接続できるようにします。
* **OneLake settings**で、**Users can access data stored in OneLake with apps external to Fabric**を有効にして、サービスプリンシパルが外部アプリからデータにアクセスできるようにします。

#### ステップ1.3: 共有ワークスペースを設定し、アクセスを許可する {#step-13-set-up-a-shared-workspace-and-grant-access}

Brazeに接続したいFabricリソースは、共有ワークスペースに配置する必要があります。デフォルトの**My Workspace**のみを使用していた場合は、新しい共有ワークスペースを作成します。

1. ナビゲーションメニューで**Workspaces**を選択し、**+ New workspace**を選択します。
2. ワークスペースの**Name**を入力し、**Apply**を選択します。

共有ワークスペースを作成したら、サービスプリンシパルにアクセスを許可します。

1. ワークスペースを選択し、**Manage Access**を選択します。
2. **+ Add people or groups**を選択します。
3. ステップ1.1で作成したサービスプリンシパルの名前を検索して選択します。表示されない場合は、ステップ1.2で**Service principals can use Fabric APIs**設定を有効にしたことを確認してください。
4. ロールのドロップダウンで、**Contributor**を選択します。

これで、サービスプリンシパルはSQLエンドポイントを通じてこのワークスペース内のFabricウェアハウスリソース（Brazeに使用するウェアハウスを含む）にアクセスできるようになります。

#### ステップ1.4: テーブルを設定する {#step-14-set-up-the-table}
BrazeはFabric Warehouseのテーブルとビューの両方をサポートしています。新しいウェアハウスを作成する必要がある場合は、ステップ1.3の共有ワークスペース内に作成します。Fabricコンソールで**Create > Data Warehouse > Warehouse**に移動します。

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

ウェアハウス、スキーマ、テーブルまたはビューの名前は自由に設定できますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルに更新または追加された時刻です。Brazeは`UPDATED_AT`が最後に同期された値より後の行を同期します。同じタイムスタンプを共有する新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には1つの識別子のみを含める必要があります（`external_id`、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新したいユーザーを識別します。Brazeで使用される`external_id`の値と一致する必要があります。
    - `ALIAS_NAME`と`ALIAS_LABEL` - これら2つのカラムはユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子であり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに1つの`alias_name`のみです。
    - `BRAZE_ID` - Brazeユーザー識別子です。Braze SDKによって生成され、クラウドデータ取り込みを通じてBraze IDを使用して新しいユーザーを作成することはできません。新しいユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。メールと電話番号の両方を含める場合、メールがプライマリ識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが更新の優先対象となります。
- `PAYLOAD` - Brazeのユーザーに同期したいフィールドのJSON文字列です。


#### ステップ1.5: ウェアハウスの接続文字列を取得する {#step-15-get-warehouse-connection-string}
ウェアハウスのSQLエンドポイントを取得するには、Fabricの**ワークスペース**に移動し、アイテムリストのウェアハウス名にカーソルを合わせて、**Copy SQL connection string**を選択します。

![Microsoft AzureのFabricコンソールページ。ユーザーはここでSQL接続文字列を取得します。]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### ステップ1.6: ファイアウォールでBraze IPを許可する（オプション） {#step-16-allow-braze-ips-in-firewall-optional}

Microsoft Fabricアカウントの設定によっては、Brazeからのトラフィックを許可するためにファイアウォールで以下のIPアドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[Entra条件付きアクセス](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)に関する関連ドキュメントを参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ2: Brazeダッシュボードで新しいソースを作成する {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

Brazeダッシュボードで、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択してから、**Snowflake**を選択します。

#### ステップ2.1: Snowflake接続情報を追加する {#step-21-add-snowflake-connection-information}

ソースの名前を選択し、Snowflakeの認証情報と設定を入力してから、次のステップに進みます。

続行する前に、**Snowflake Account Locator**に入力する値を確認してください。

**Snowflake Account Locator**フィールドには、Snowflakeの[アカウント識別子](https://docs.snowflake.com/en/user-guide/admin-account-identifier)を入力します。`myorganization-myaccount`のようなアカウント識別子の値のみを入力してください。`https://`、`.snowflakecomputing.com`、またはパスは含めないでください。

Snowflakeアカウント識別子を見つけるには：

1. Snowsightで、アカウントメニューを選択します。
2. **View account details**を選択します。
3. **Account identifier**の値をコピーします。
4. SnowflakeのURLからコピーする場合は、`.snowflakecomputing.com`の前の値のみを使用してください。

#### ステップ2.2: Brazeユーザーに公開キーを追加する {#step-22-add-a-public-key-to-the-braze-user}

認証情報と設定を入力した後、**Save credentials**をクリックしてRSAキーを生成し、Snowflakeに戻って設定を完了します。ダッシュボードに表示される公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加します。

この方法の詳細については、[Snowflakeのドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。キーをローテーションしたい場合、Brazeは新しいキーペアを生成し、新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Brazeダッシュボードで、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択してから、**Amazon Redshift**を選択します。

#### ステップ2.1: Redshift接続情報とソーステーブルを追加する {#step-21-add-redshift-connection-information-and-source-table}

ソースの名前を選択し、Redshiftの認証情報と設定を入力します。プライベートネットワークトンネルを使用している場合は、スライダーを切り替えてトンネル情報を入力します。次に、次のステップに進みます。

{% alert note %}
Brazeダッシュボードの**Database name**フィールドは、Amazon Redshiftがデータベース識別子で追加の文字をサポートしている場合でも、文字（A〜Z、a〜z）、数字（0〜9）、アンダースコア（_）のみを受け付けます。
{% endalert %}

#### ステップ2.2: 接続をテストしてソースに接続する {#step-22-test-connection-and-connect-to-source}

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

#### トラブルシューティング: 無効なスナップショット識別子 {#troubleshooting-invalid-snapshot-identifier}

**Test connection**または同期設定中にBrazeが`Invalid snapshot identifier`エラーを返す場合、ソースオブジェクトがクエリされる際に使用されるスナップショット参照をRedshiftが解決できません。

Redshiftでは、スナップショットはクラスターのポイントインタイムバックアップです。各スナップショットには、Redshiftがそのバックアップ状態を参照するために使用する一意の識別子があります。詳細については、[Amazon Redshiftのスナップショットとバックアップ](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)を参照してください。

このエラーは、Brazeがソースオブジェクトを検証している間にメタデータが変更された場合（スナップショットのコピー、復元、またはレプリケーション関連の操作中など）に発生する可能性があります。詳細については、[別のAWSリージョンへのスナップショットのコピー](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html)および[スナップショットからのクラスターの復元](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html)を参照してください。

トラブルシューティングの手順：

1. クラスターエンドポイント、データベース、スキーマ、オブジェクト名を含むBrazeのソース設定を確認します。
2. Redshiftで直接同じクエリを実行して、テーブルまたはビューが読み取り可能で安定していることを確認します。
3. アクティブなスナップショット、復元、リサイズ、またはレプリケーションアクティビティが完了した後に再試行します。
4. 問題が解決しない場合は、頻繁に変更されるベーステーブルの代わりにマテリアライズドビューをクエリします。

マテリアライズドビューは、スケジュールに従って更新できる事前計算されたクエリ結果を保存するため、CDI同期の読み取りをより安定させることができます。詳細については、[Amazon Redshiftのマテリアライズドビュー](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html)を参照してください。

例：

```sql
CREATE MATERIALIZED VIEW ingestion.users_attributes_mv AS
SELECT updated_at, external_id, alias_label, alias_name, braze_id, email, phone, payload
FROM ingestion.users_attributes_sync;

REFRESH MATERIALIZED VIEW ingestion.users_attributes_mv;
```

マテリアライズドビューを作成した後、ベーステーブルの代わりにマテリアライズドビュー名をBraze CDI同期のソースオブジェクトとして使用します。
{% endtab %}
{% tab BigQuery %}

Brazeダッシュボードで、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択してから、**Google BigQuery**を選択します。

#### ステップ2.1: BigQuery接続情報とソーステーブルを追加する {#step-21-add-bigquery-connection-information-and-source-table}

ソースの名前を選択します。次に、JSONキーをアップロードし、サービスアカウントの名前を入力します。その後、残りの設定フィールドを入力します。

#### ステップ2.2: 接続をテストしてソースに接続する

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% endtab %}
{% tab Databricks %}

Brazeダッシュボードで、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択してから、**Databricks**を選択します。

#### ステップ2.1: Databricks接続情報とソーステーブルを追加する {#step-21-add-databricks-connection-information-and-source-table}

ソースの名前を選択し、Databricksの認証情報と設定を入力します。次に、次のステップに進みます。

#### ステップ2.2: 接続をテストしてソースに接続する

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
ソースを作成する前に、接続テストに成功する必要があります。作成ページを閉じると、ソースは保存されません。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

Brazeダッシュボードで、データ設定 > クラウドデータ取り込み > ソースに移動し、**データソースを追加**を選択してから、**Microsoft Fabric**を選択します。

#### ステップ2.1: クラウドデータ取り込み同期を設定する {#step-21-set-up-a-cloud-data-ingestion-sync}

ソースの名前を選択し、Microsoft Fabricの認証情報と設定を入力します。
- **Credentials Name**はBrazeでのこれらの認証情報のラベルです。ここにわかりやすい値を設定できます。
- テナントID、プリンシパルID、クライアントシークレット、接続文字列の取得方法の詳細については、セクション1のステップを参照してください。

#### ステップ2.2: 接続をテストしてソースに接続する

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
ソースを作成する前に、接続テストに成功する必要があります。作成ページを閉じると、ソースは保存されません。
{% endalert %}

{% endtab %}

{% endtabs %}

### ステップ3: Brazeダッシュボードで新しい同期を作成する {#step-3-create-a-new-sync-in-the-braze-dashboard}
**データ設定** > **クラウドデータ取り込み** > **同期**に移動し、**データ同期を作成**を選択します。

{% tabs %}
{% tab Snowflake %}

#### ステップ3.1: 同期の詳細を設定し、接続をテストする {#step-31-configure-sync-details-and-test-connection}
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存してください。
{% endalert %}

#### ステップ3.2: 通知設定を追加する {#step-32-add-notification-preferences}
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題などのグローバルまたは同期レベルのエラーの通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には以下が含まれます：

- 接続の問題
- リソースの不足
- 権限の問題
- （カタログ同期のみ）カタログティアの容量不足

#### ステップ3.3: スケジューリング {#step-33-scheduling}
最後に、同期を非定期または定期として設定します。

非定期同期は手動またはAPIを介してトリガーできます。

定期同期は15分ごとから月1回までの頻度で設定できます。Brazeは定期同期をUTCタイムゾーンでスケジュールします。

{% endtab %}

{% tab Redshift %}

#### ステップ3.1: 同期の詳細を設定し、接続をテストする
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存してください。
{% endalert %}

#### ステップ3.2: 通知設定を追加する
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題などのグローバルまたは同期レベルのエラーの通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には以下が含まれます：

- 接続の問題
- リソースの不足
- 権限の問題

（カタログ同期のみ）カタログティアの容量不足

#### ステップ3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期同期は手動またはAPIを介してトリガーできます。

定期同期は15分ごとから月1回までの頻度で設定できます。Brazeは定期同期をUTCタイムゾーンでスケジュールします。

{% endtab %}

{% tab BigQuery %}

#### ステップ3.1: 同期の詳細を設定し、接続をテストする
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存してください。
{% endalert %}

#### ステップ3.2: 通知設定を追加する
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題などのグローバルまたは同期レベルのエラーの通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には以下が含まれます：

- 接続の問題
- リソースの不足
- 権限の問題

（カタログ同期のみ）カタログティアの容量不足

#### ステップ3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期同期は手動またはAPIを介してトリガーできます。

定期同期は15分ごとから月1回までの頻度で設定できます。Brazeは定期同期をUTCタイムゾーンでスケジュールします。

{% endtab %}

{% tab Databricks %}

#### ステップ3.1: 同期の詳細を設定し、接続をテストする
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存してください。
{% endalert %}

#### ステップ3.2: 通知設定を追加する
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題などのグローバルまたは同期レベルのエラーの通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には以下が含まれます：
- 接続の問題
- リソースの不足
- 権限の問題

（カタログ同期のみ）カタログティアの容量不足

#### ステップ3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期同期は手動またはAPIを介してトリガーできます。

定期同期は15分ごとから月1回までの頻度で設定できます。Brazeは定期同期をUTCタイムゾーンでスケジュールします。

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ3.1: 同期の詳細を設定し、接続をテストする

同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進む前に、同期のテストに成功する必要があります。同期作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保存してください。
{% endalert %}

#### ステップ3.2: 通知設定を追加する
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルアクセスの予期しない喪失などの統合エラーに関する通知を送信します。

連絡先メールは、テーブルの欠落、権限の問題などのグローバルまたは同期レベルのエラーの通知のみを受信します。行レベルの問題は受信しません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には以下が含まれます：

- 接続の問題
- リソースの不足
- 権限の問題

（カタログ同期のみ）カタログティアの容量不足

#### ステップ3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期同期は手動またはAPIを介してトリガーできます。

定期同期は15分ごとから月1回までの頻度で設定できます。Brazeは定期同期をUTCタイムゾーンでスケジュールします。

{% endtab %}
{% endtabs %}

{% alert note %}
統合を下書きからアクティブ状態に移行するには、統合のテストに成功する必要があります。作成ページを閉じた場合、統合は保存され、詳細ページに戻って変更やテストを行うことができます。
{% endalert %}

## 追加の統合またはユーザーの設定（オプション） {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Brazeとの統合は複数設定できますが、各統合はそれぞれ異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じSnowflakeアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーとロールを再利用する場合、公開キーを再度追加する必要はありません。
{% endtab %}
{% tab Redshift %}
Brazeとの統合は複数設定できますが、各統合はそれぞれ異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じSnowflakeまたはRedshiftアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーを再利用する場合、そのユーザーがすべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。
{% endtab %}
{% tab BigQuery %}

Brazeとの統合は複数設定できますが、各統合はそれぞれ異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じBigQueryアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーを再利用する場合、そのユーザーがすべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Databricks %}

Brazeとの統合は複数設定できますが、各統合はそれぞれ異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じDatabricksアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーを再利用する場合、そのユーザーがすべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Microsoft Fabric %}

Brazeとの統合は複数設定できますが、各統合はそれぞれ異なるテーブルを同期するように構成する必要があります。追加の同期を作成する際、同じFabricアカウントに接続する場合は既存の認証情報を再利用できます。

統合間で同じユーザーを再利用する場合、そのユーザーがすべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% endtabs %}

## 同期の実行 {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
有効化すると、設定時に構成されたスケジュールに従って同期が実行されます。通常のテストスケジュール外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、定期的にスケジュールされた今後の同期には影響しません。

{% endtab %}
{% tab Redshift %}
有効化すると、設定時に構成されたスケジュールに従って同期が実行されます。通常のテストスケジュール外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、定期的にスケジュールされた今後の同期には影響しません。

{% endtab %}
{% tab BigQuery %}

有効化すると、設定時に構成されたスケジュールに従って同期が実行されます。通常のテストスケジュール外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、定期的にスケジュールされた今後の同期には影響しません。

{% endtab %}
{% tab Databricks %}

有効化すると、設定時に構成されたスケジュールに従って同期が実行されます。通常のテストスケジュール外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、定期的にスケジュールされた今後の同期には影響しません。

{% endtab %}
{% tab Microsoft Fabric %}

有効化すると、設定時に構成されたスケジュールに従って同期が実行されます。通常のテストスケジュール外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now** を選択してください。この実行は、定期的にスケジュールされた今後の同期には影響しません。

{% endtab %}

{% endtabs %}