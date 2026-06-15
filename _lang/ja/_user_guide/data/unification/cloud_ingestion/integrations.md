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

## データウェアハウス連携の設定 {#setting-up-data-warehouse-integrations}

クラウドデータ取り込みの連携では、Braze側とデータウェアハウスインスタンス側でいくつかの設定が必要です。次のステップに従って、連携を設定します。

{% tabs %}
{% tab Snowflake %}
1. Snowflakeインスタンスで、Brazeと同期するテーブルまたはビューを設定します。
2. Brazeダッシュボードで新しいSnowflakeソースを作成します。
3. Brazeダッシュボードに表示された公開キーを取得し、[認証用としてSnowflakeユーザーに追加](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)します。
4. Brazeダッシュボードで同期を作成し、連携のテストを行い、同期を開始します。

{% alert tip %}
[Snowflakeクイックスタートガイド](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)では、サンプルコードを提供し、Snowflake StreamsとCDIを使用して自動パイプラインを作成し、Brazeにデータを同期するために必要なステップを説明しています。
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. 同期するRedshiftテーブルへのBrazeのアクセスが許可されていることを確認します。Brazeはインターネット経由でRedshiftに接続します。
2. Redshiftインスタンスで、Brazeと同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 連携のテストを行い、同期を開始します。

{% alert note %}
同期ごとに処理される行数は、ウェアハウスのパフォーマンス、ネットワークレイテンシー、および同期クエリに一致する新しいデータの量によって異なります。ダッシュボードの連携**同期履歴**を使用して、最近の実行の所要時間と行数を確認できます。
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. サービスアカウントを作成し、同期するデータを含むBigQueryのプロジェクトとデータセットへのアクセスを許可します。
2. BigQueryアカウントで、Brazeと同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 連携のテストを行い、同期を開始します。
{% endtab %}
{% tab Databricks %}
1. サービスアカウントを作成し、同期するデータを含むDatabricksのプロジェクトとデータセットへのアクセスを許可します。
2. Databricksアカウントで、Brazeと同期するテーブルまたはビューを設定します。
3. Brazeダッシュボードで新しいソースと同期を作成します。
4. 連携のテストを行い、同期を開始します。

{% alert important %}
BrazeがClassicおよびProのSQLインスタンスに接続する際、2〜5分のウォームアップ時間が発生することがあり、接続の設定やテスト中、およびスケジュールされた同期の開始時に遅延が生じる可能性があります。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、Fabric APIへのアクセスを許可します。
2. 共有ワークスペースを設定し、サービスプリンシパルにアクセスを許可します。
3. 共有Fabricワークスペースで、Brazeと同期するテーブルまたはビューを設定します。
4. Brazeダッシュボードで新しいソースと同期を作成します。
5. 連携のテストを行い、同期を開始します。
{% endtab %}
{% endtabs %}

### ステップ 1: テーブルまたはビューの設定 {#step-1-set-up-tables-or-views}

開始する前に、[クラウドデータ取り込みのテーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup/)を確認して、ソーステーブルの要件と`PAYLOAD`のフォーマット要件を理解してください。

{% alert note %}
ソーステーブルまたはビューには、以下のタブでお使いのウェアハウス向けにリストされていない列を含めることができます（例: 監査やハッシュ用の列）。Brazeはそれらのタブに記載されている列のみを読み取ります。その他の列はクラウドデータ取り込みの同期中に使用されません。
{% endalert %}

{% tabs %}
{% tab Snowflake %}

#### ステップ 1.1: テーブルの設定 {#step-11-set-up-the-table}

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

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Brazeは`UPDATED_AT`が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id`単独か、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`）を1つのみ含める必要があります。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これはBrazeで使用されている`external_id`値と一致する必要があります。
    - `ALIAS_NAME`および`ALIAS_LABEL` - この2列はユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子である必要があり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つしか持てません。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成されます。クラウドデータ取り込み経由でBraze IDを使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze内のユーザーと同期するフィールドのJSON文字列です。

#### ステップ 1.2: ロールとデータベース権限の設定 {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

必要に応じて名前を更新してください。ただし、権限は上記の例と一致する必要があります。

#### ステップ 1.3: ウェアハウスの設定とBrazeロールへのアクセス権の付与 {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスは**自動再開**フラグをオンにしておく必要があります。オンにしない場合は、Brazeがクエリの実行時にウェアハウスをオンにできるように、追加の`OPERATE`権限を付与する必要があります。
{% endalert %}

#### ステップ 1.4: ユーザーの設定 {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このステップの後、Brazeと接続情報を共有し、ユーザーに追加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じSnowflakeアカウントに接続する場合は、連携を作成するBrazeワークスペースごとに一意のユーザーを作成する必要があります。ワークスペース内では、複数の連携にわたって同じユーザーを再利用できますが、同じSnowflakeアカウントのユーザーが複数のワークスペースで重複すると、連携の作成に失敗します。
{% endalert %}

#### ステップ 1.5: SnowflakeネットワークポリシーでBraze IPを許可する（オプション） {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Snowflakeアカウントの設定によっては、Snowflakeのネットワークポリシーで以下のIPアドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関するSnowflakeの関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### ステップ 1.1: テーブルの設定

オプションで、ソーステーブルを保持する新規データベースとスキーマを設定します。
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
CDI連携に使用するテーブル（またはビュー）を作成します。
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

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Brazeは`UPDATED_AT`が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id`単独か、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`）を1つのみ含める必要があります。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これはBrazeで使用されている`external_id`値と一致する必要があります。
    - `ALIAS_NAME`および`ALIAS_LABEL` - この2列はユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子である必要があり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つしか持てません。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成されます。クラウドデータ取り込み経由でBraze IDを使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze内のユーザーと同期するフィールドのJSON文字列です。

#### ステップ 1.2: ユーザーの作成と権限の付与 {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

これらは、このユーザーに最低限必要な権限です。CDI連携を複数作成する場合は、スキーマに権限を付与したり、グループを使用して権限を管理したりすることもできます。

#### ステップ 1.3: Braze IPへのアクセスの許可 {#step-13-allow-access-to-braze-ips}

ファイアウォールや他のネットワークポリシーがある場合は、Redshiftインスタンスへの Brazeネットワークアクセスを許可する必要があります。RedshiftのURLエンドポイントの例は「example-cluster.ap-northeast-2.redshift.amazonaws.com」です。

知っておくべき重要な点がいくつかあります。
- Redshiftのデータへの Brazeのアクセスを許可するために、セキュリティグループの変更が必要になる場合もあります。
- テーブル内のIPとRedshiftクラスターへのクエリに使用するポート（デフォルトは5439）のインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートでのRedshiftのTCP接続を明示的に許可する必要があります。
- Brazeがクラスターに接続するには、Redshiftクラスターのエンドポイントがパブリックにアクセス可能である必要があります。
     - Redshiftクラスターにパブリックアクセスを許可しない場合は、SSHトンネルを使用してRedshiftデータにアクセスするようにVPCとEC2インスタンスを設定できます。詳細については、[AWSナレッジセンターの投稿](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。

Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### ステップ 1.1: テーブルの設定

オプションで、ソーステーブルを保持する新規のプロジェクトまたはデータセットを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ、CDI連携に使用するテーブルを1つ以上作成します。

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
| `UPDATED_AT` | TIMESTAMP | REQUIRED |
| `PAYLOAD` | JSON | REQUIRED |
| `EXTERNAL_ID` | STRING | NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
| `BRAZE_ID` | STRING | NULLABLE |
| `EMAIL` | STRING | NULLABLE |
| `PHONE` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 1.1: Set up the table" }

プロジェクト、データセット、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Brazeは`UPDATED_AT`が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id`単独か、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`）を1つのみ含める必要があります。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これはBrazeで使用されている`external_id`値と一致する必要があります。
    - `ALIAS_NAME`および`ALIAS_LABEL` - この2列はユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子である必要があり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つしか持てません。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成されます。クラウドデータ取り込み経由でBraze IDを使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze内のユーザーと同期するフィールドのJSON文字列です。

{% alert important %}
**BigQueryのパーティショニング**

CDIはBigQueryのパーティションをサポートしています。`UPDATED_AT`の関数によるパーティション分割（例えば、データセットのサイズに応じて日単位、週単位、時間単位の粒度で）を行うと、BigQueryはスキャンする必要のあるデータを絞り込めます。これにより、非常に大きなテーブルのパフォーマンスと効率が向上します。

他のフィールドでパーティション分割しないでください。さまざまな設定をテストして、ご自身のデータに最適な構成を見つけてください。

すべてのCDIクエリは`UPDATED_AT`でフィルターしますが、この動作は変更される可能性があります。テーブルスキーマを設計する際は、クエリにこの句を含めることを前提と_しない_ようにしてください。

詳細については、[BigQueryのパーティショニングに関するドキュメント](https://docs.cloud.google.com/bigquery/docs/partitioned-tables)を参照してください。
{% endalert %}

#### ステップ 1.2: サービスアカウントの作成と権限の付与 {#step-12-create-a-service-account-and-grant-permissions}

GCPで、Brazeがテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには次の権限が必要です。

- **BigQuery Connection User:** Brazeに接続を許可します。
- **BigQuery User:** クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスをBrazeに提供します。
- **BigQuery Data Viewer:** データセットとその内容を表示するためのアクセスをBrazeに提供します。
- **BigQuery Job User:** ジョブを実行するためのアクセスをBrazeに提供します。

サービスアカウントを作成して権限を付与したら、JSONキーを生成します。詳細については、[サービスアカウントキーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。このキーは後のステップでBrazeダッシュボードにアップロードします。

#### ステップ 1.3: Braze IPへのアクセスの許可

ネットワークポリシーを設定している場合は、BigQueryインスタンスへのBrazeネットワークアクセスを許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### ステップ 1.1: テーブルの設定

オプションで、ソーステーブルを保持する新しいカタログまたはスキーマを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ、CDI連携に使用するテーブルを1つ以上作成します。


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
| `UPDATED_AT` | TIMESTAMP | REQUIRED |
| `PAYLOAD` | STRING、STRUCT、またはMAP | REQUIRED |
| `EXTERNAL_ID` | STRING | NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
| `BRAZE_ID` | STRING | NULLABLE |
| `EMAIL` | STRING | NULLABLE |
| `PHONE` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 1.1: Set up the table" }

スキーマとテーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Brazeは`UPDATED_AT`が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id`単独か、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`）を1つのみ含める必要があります。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これはBrazeで使用されている`external_id`値と一致する必要があります。
    - `ALIAS_NAME`および`ALIAS_LABEL` - この2列はユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子である必要があり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つしか持てません。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成されます。クラウドデータ取り込み経由でBraze IDを使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Brazeでユーザーと同期するフィールドの文字列または構造体です。

#### ステップ 1.2: アクセストークンの作成 {#step-12-create-an-access-token}

BrazeがDatabricksにアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricksワークスペースで、上部バーにあるDatabricksユーザー名を選択し、ドロップダウンから**User Settings**を選択します。
2. [アクセストークン] タブで、**Generate new token**を選択します。
3. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、[有効期間（日）] ボックスを空（空白）のままにして、トークンの有効期間を無期限に変更します。
4. **Generate**を選択します。
5. 表示されたトークンをコピーして、**Done**を選択します。

認証情報の作成ステップでBrazeダッシュボードに入力する必要があるまで、トークンを安全な場所に保管してください。

#### ステップ 1.3: Braze IPへのアクセスの許可

ネットワークポリシーを設定している場合は、Databricksインスタンスへの Brazeネットワークアクセスを許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 1.1: サービスプリンシパルの設定とアクセスの許可 {#step-11-set-up-the-service-principal-and-grant-access}
BrazeはEntra ID認証でサービスプリンシパルを使用してFabricウェアハウスに接続します。Brazeが使用する新しいサービスプリンシパルを作成し、必要に応じてFabricリソースへのアクセスを許可します。Brazeの接続には以下の情報が必要です。

* Azureアカウントのテナント ID（ディレクトリとも呼ばれます）
* サービスプリンシパルのプリンシパル ID（アプリケーション IDとも呼ばれます）
* Brazeが認証するためのクライアントシークレット

1. Azure portalで、Microsoft Entra管理センター、[アプリの登録] の順に移動します。
2. **Identity** > **Applications** > **App registrations**で**+ New registration**を選択します。
3. 名前を入力し、サポートされているアカウントの種類として`Accounts in this organizational directory only`を選択します。次に、**Register**を選択します。
4. 作成したアプリケーション（サービスプリンシパル）を選択し、**Certificates & secrets** > **+ New client secret**に移動します。
5. シークレットの説明を入力し、有効期限を設定します。次に、**Add**を選択します。
6. Brazeのセットアップで使用するために、作成したクライアントシークレットをメモしてください。

{% alert note %}
Azureでは、サービスプリンシパルシークレットの有効期限を無制限に設定することはできません。Brazeへのデータフローを維持するために、認証情報が失効する前に忘れずに更新してください。
{% endalert %}

#### ステップ 1.2: Fabricリソースへのアクセスの許可 {#step-12-grant-access-to-fabric-resources}
BrazeがFabricインスタンスに接続するためのアクセスを提供します。Fabricの管理ポータルで、**Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**の順に移動します。

* **Developer settings**で、**Service principals can use Fabric APIs**を有効にして、BrazeがMicrosoft Entra IDを使用して接続できるようにします。
* **OneLake settings**で、**Users can access data stored in OneLake with apps external to Fabric**を有効にして、サービスプリンシパルが外部アプリからデータにアクセスできるようにします。

#### ステップ 1.3: 共有ワークスペースの設定とアクセスの許可 {#step-13-set-up-a-shared-workspace-and-grant-access}

Brazeに接続するFabricリソースは、共有ワークスペースに配置する必要があります。デフォルトの**My Workspace**のみを使用している場合は、新しい共有ワークスペースを作成してください。

1. ナビゲーションメニューで**Workspaces**を選択し、**+ New workspace**を選択します。
2. ワークスペースの**Name**を入力し、**Apply**を選択します。

共有ワークスペースを作成したら、サービスプリンシパルにアクセスを許可します。

1. ワークスペースを選択し、**Manage Access**を選択します。
2. **+ Add people or groups**を選択します。
3. ステップ 1.1で作成したサービスプリンシパルの名前を検索して選択します。表示されない場合は、ステップ 1.2で**Service principals can use Fabric APIs**の設定が有効になっていることを確認してください。
4. ロールのドロップダウンで**Contributor**を選択します。

これで、サービスプリンシパルはSQLエンドポイントを通じてこのワークスペース内のFabricウェアハウスリソース（Brazeで使用するウェアハウスを含む）にアクセスできるようになります。

#### ステップ 1.4: テーブルの設定 {#step-14-set-up-the-table}
BrazeはFabricウェアハウスのテーブルとビューの両方をサポートしています。新しいウェアハウスを作成する必要がある場合は、ステップ 1.3の共有ワークスペース内に作成してください。Fabricコンソールで**Create** > **Data Warehouse** > **Warehouse**と進みます。

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

ウェアハウス、スキーマ、テーブルまたはビューには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Brazeは`UPDATED_AT`が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id`単独か、`alias_name`と`alias_label`の組み合わせ、`braze_id`、`email`、または`phone`）を1つのみ含める必要があります。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これはBrazeで使用されている`external_id`値と一致する必要があります。
    - `ALIAS_NAME`および`ALIAS_LABEL` - この2列はユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子である必要があり、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つしか持てません。
    - `BRAZE_ID` - Brazeのユーザー識別子です。これはBraze SDKによって生成されます。クラウドデータ取り込み経由でBraze IDを使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザーIDまたはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze内のユーザーと同期するフィールドのJSON文字列です。


#### ステップ 1.5: ウェアハウスの接続文字列を取得する {#step-15-get-warehouse-connection-string}
ウェアハウスのSQLエンドポイントを取得するには、Fabricで**ワークスペース**に移動し、項目の一覧でウェアハウスの名前にカーソルを合わせ、**Copy SQL connection string**を選択します。

![Microsoft AzureのFabricコンソールページ。ユーザーはここでSQL接続文字列を取得します。]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### ステップ 1.6: ファイアウォールでBraze IPを許可する（オプション） {#step-16-allow-braze-ips-in-firewall-optional}

Microsoft Fabricアカウントの設定によっては、Brazeからのトラフィックを許可するために、ファイアウォールで以下のIPアドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ 2: Brazeダッシュボードで新しいソースを作成する {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Snowflake**を選択します。

#### ステップ 2.1: Snowflakeの接続情報の追加 {#step-21-add-snowflake-connection-information}

ソースの名前を選択し、Snowflakeの認証情報と設定を入力して、次のステップに進みます。

続行する前に、**Snowflake Account Locator**に入力する値を確認してください。

**Snowflake Account Locator**フィールドには、Snowflakeの[アカウント識別子](https://docs.snowflake.com/en/user-guide/admin-account-identifier)を入力します。`myorganization-myaccount`のようなアカウント識別子の値のみを入力してください。`https://`、`.snowflakecomputing.com`、またはパスは含めないでください。

Snowflakeのアカウント識別子を確認するには:

1. Snowsightで、アカウントメニューを選択します。
2. **View account details**を選択します。
3. **Account identifier**の値をコピーします。
4. SnowflakeのURLからコピーする場合は、`.snowflakecomputing.com`より前の値のみを使用してください。

#### ステップ 2.2: Brazeユーザーへの公開キーの追加 {#step-22-add-a-public-key-to-the-braze-user}

認証情報と設定を入力したら、**Save credentials**をクリックしてRSAキーを生成し、Snowflakeに戻って設定を完了します。ダッシュボードに表示されている公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加します。

その方法の詳細については、[Snowflakeのドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。任意の時点でキーをローテーションする場合は、Brazeが新しいキーペアを生成して新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Amazon Redshift**を選択します。

#### ステップ 2.1: Redshiftの接続情報とソーステーブルの追加 {#step-21-add-redshift-connection-information-and-source-table}

ソースの名前を選択し、Redshiftの認証情報と設定を入力します。プライベートネットワークトンネルを使用している場合は、スライダーを切り替えてトンネル情報を入力します。次のステップに進みます。

{% alert note %}
Brazeダッシュボードの**Database name**フィールドは、Amazon Redshiftがデータベース識別子で追加の文字をサポートしているにもかかわらず、英字（A–Z、a–z）、数字（0–9）、アンダースコア（_）のみを受け付けます。
{% endalert %}

#### ステップ 2.2: 接続のテストとソースへの接続 {#step-22-test-connection-and-connect-to-source}

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。
{% endtab %}
{% tab BigQuery %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Google BigQuery**を選択します。

#### ステップ 2.1: BigQueryの接続情報とソーステーブルの追加 {#step-21-add-bigquery-connection-information-and-source-table}

ソースの名前を選択します。次に、JSONキーをアップロードし、サービスアカウントの名前を入力して、残りの設定フィールドを入力します。

#### ステップ 2.2: 接続のテストとソースへの接続

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% endtab %}
{% tab Databricks %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Databricks**を選択します。

#### ステップ 2.1: Databricksの接続情報とソーステーブルの追加 {#step-21-add-databricks-connection-information-and-source-table}

ソースの名前を選択し、Databricksの認証情報と設定を入力します。次のステップに進みます。

#### ステップ 2.2: 接続のテストとソースへの接続

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
ソースを作成するには、テスト接続に成功する必要があります。作成ページを閉じると、ソースは保存されません。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

Brazeダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択して、**Microsoft Fabric**を選択します。

#### ステップ 2.1: クラウドデータ取り込みの同期を設定する {#step-21-set-up-a-cloud-data-ingestion-sync}

ソースの名前を選択し、Microsoft Fabricの認証情報と設定を入力します。
- **Credentials Name**は、Brazeにおけるこれらの認証情報のラベルです。わかりやすい値を設定してください。
- テナント ID、プリンシパル ID、クライアントシークレット、および接続文字列の取得方法については、セクション1のステップを参照してください。

#### ステップ 2.2: 接続のテストとソースへの接続

次に、**Test connection**を選択します。成功したら、残りの設定を確定し、**Connect to Source**をクリックします。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
ソースを作成するには、テスト接続に成功する必要があります。作成ページを閉じると、ソースは保存されません。
{% endalert %}

{% endtab %}

{% endtabs %}

### ステップ 3: Brazeダッシュボードで新しい同期を作成する {#step-3-create-a-new-sync-in-the-braze-dashboard}
**Data Settings** > **Cloud Data Ingestion** > **Syncs**に移動し、**Create data sync**を選択します。

{% tabs %}
{% tab Snowflake %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト {#step-31-configure-sync-details-and-test-connection}
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加 {#step-32-add-notification-preferences}
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング {#step-33-scheduling}
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動またはAPI経由でトリガーできます。

定期的な同期は、15分間隔から1か月に1回までの頻度で設定できます。Brazeダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}

{% tab Redshift %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題

（カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動またはAPI経由でトリガーできます。

定期的な同期は、15分間隔から1か月に1回までの頻度で設定できます。Brazeダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}

{% tab BigQuery %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題

（カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動またはAPI経由でトリガーできます。

定期的な同期は、15分間隔から1か月に1回までの頻度で設定できます。Brazeダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}

{% tab Databricks %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には、次のようなものがあります。
- 接続の問題
- リソース不足
- 権限の問題

（カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動またはAPI経由でトリガーできます。

定期的な同期は、15分間隔から1か月に1回までの頻度で設定できます。Brazeダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト

同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**をクリックします。

成功すると、データのプレビューが表示されます。**Next: Notifications**を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、**Save as draft**をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Brazeはこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。

このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題

（カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動またはAPI経由でトリガーできます。

定期的な同期は、15分間隔から1か月に1回までの頻度で設定できます。Brazeダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}
{% endtabs %}

{% alert note %}
連携を下書き状態からアクティブ状態に移行するには、テスト接続に成功する必要があります。作成ページを閉じた場合でも、連携は保存されるため、詳細ページに再度アクセスして変更やテストを行うことができます。
{% endalert %}

## 追加の連携またはユーザーの設定（オプション） {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Brazeとの連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じSnowflakeアカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーとロールを再利用する場合、公開キーを追加するステップを再度行う必要はありません。
{% endtab %}
{% tab Redshift %}
Brazeとの連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じSnowflakeまたはRedshiftアカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。
{% endtab %}
{% tab BigQuery %}

Brazeとの連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じBigQueryアカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Databricks %}

Brazeとの連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じDatabricksアカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Microsoft Fabric %}

Brazeとの連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じFabricアカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Brazeダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% endtabs %}

## 同期の実行 {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now**を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Redshift %}
有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now**を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab BigQuery %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now**を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Databricks %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now**を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Microsoft Fabric %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、**Sync Now**を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}

{% endtabs %}