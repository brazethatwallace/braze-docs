---
nav_title: ゼロコピーパーソナライゼーション
article_title: CDI を用いたゼロコピーパーソナライゼーション
page_order: 7
page_type: reference
description: "このページでは、CDI を使用して Braze Canvasをトリガーする方法の概要を説明します。"
---

# CDI を用いたゼロコピーパーソナライゼーション {#zero-copy-personalization-using-cdi}

> CDI を使ってCanvasトリガーを同期し、ゼロコピーパーソナライゼーションを実現する方法を説明します。この機能は、データストレージソリューションからユーザー固有の情報にアクセスし、それを送信先のCanvasに渡します。キャンバスステップには、Braze ユーザープロファイルに永続化されないパーソナライゼーションフィールドをオプションで含めることができます。

## Canvasトリガーの同期 {#syncing-canvas-triggers}

### クイックスタートのステップ {#quick-start-steps}

Braze CDI に既に慣れている場合、Canvasトリガーの同期設定は[ユーザーデータ CDI 統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/)のプロセスとほぼ同様ですが、以下の注意点があります。

- external ID またはユーザーエイリアス識別子のみがサポートされています。メールと電話番号はサポートされていない識別子です。
- 既存の Braze ユーザーのみ同期できます。新規ユーザーは作成できません。
- `properties` が `payload` 列を置き換えます。これは、パーソナライゼーション用のCanvasエントリプロパティとして使用したいフィールドの JSON 文字列です。

始めるには、新しい同期を作成する際に **Canvas Triggers** データタイプを選択します。

### Canvasトリガーの使用 {#using-canvas-triggers}

#### ステップ 1: Canvasトリガー用のデータソースを設定する {#step-1-set-up-data-source-for-canvas-triggers}

{% tabs %}
{% tab Snowflake %}

##### ステップ 1.1: Snowflake でソーステーブルを設定する {#step-11-set-up-your-source-table-in-snowflake}

次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

データベース、スキーマ、テーブルの名前は自由に付けられますが、列名は前述の定義と一致させる必要があります。

* `UPDATED_AT`: この行が更新されたか、テーブルに追加された時刻です。Braze は `UPDATED_AT` が最後に同期された値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
* ユーザー識別子列として、`external_id` または `alias_name` と `alias_label` のいずれかを使用します。これらは、Canvasメッセージングをトリガーしたいユーザーを識別するものです。
  * `EXTERNAL_ID`: ユーザーを識別し、Canvasにエントリさせます。これは Braze で使用されている `external_id` 値と一致する必要があります。
  * `ALIAS_NAME` と `ALIAS_LABEL`: これらの列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子であるべきであり、`alias_label` はエイリアスの種類を指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに alias_name は1つしか持てません。
* `PROPERTIES`: Canvas内でパーソナライゼーションプロパティとして利用可能なフィールドの JSON 文字列です。ユーザー固有の情報を含める必要があります。

{% alert note %}
プロパティはすべての行やユーザーに対して必須ではありません。ただし、プロパティの値は有効な JSON 文字列でなければなりません。行にプロパティがない場合は空の `{}` 文字列を入力してください。
{% endalert %}

##### ステップ 1.2: 認証情報を設定する {#step-12-set-up-credentials}

ロール、ウェアハウス、ユーザーを設定し、適切な権限を付与します。既存の同期から認証情報を既に持っている場合、それを再利用できます。ただし、Canvasトリガーのソーステーブルへのアクセス権限を必ず拡張してください。

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

##### ステップ 1.3: ネットワークポリシーを設定する {#step-13-configure-network-policies}

アカウントにネットワークポリシーが設定されている場合、CDI サービス接続を有効にするために Braze の IP アドレスを許可リストに追加してください。IP アドレスの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional)を参照してください。

{% endtab %}
{% tab Redshift %}

##### ステップ 1.1: Redshift でソーステーブルを設定する {#step-11-set-up-your-source-table-in-redshift}

次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

データベース、スキーマ、テーブルの名前は自由に付けられますが、列名は前述の定義と一致させる必要があります。

* `UPDATED_AT`: この行が更新されたか、テーブルに追加された時刻です。Braze は `UPDATED_AT` が最後に同期された値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
* ユーザー識別子列として、`external_id` または `alias_name` と `alias_label` のいずれかを使用します。これらは、Canvasメッセージングをトリガーしたいユーザーを識別するものです。
  * `EXTERNAL_ID`: ユーザーを識別し、Canvasにエントリさせます。これは Braze で使用されている `external_id` 値と一致する必要があります。
  * `ALIAS_NAME` と `ALIAS_LABEL`: これらの列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子であるべきであり、`alias_label` はエイリアスの種類を指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つしか持てません。
* `PROPERTIES`: Canvas内でパーソナライゼーションプロパティとして利用可能なフィールドの JSON 文字列です。ユーザー固有の情報を含める必要があります。

{% alert note %}
プロパティはすべての行やユーザーに対して必須ではありません。ただし、プロパティの値は有効な JSON 文字列でなければなりません。行にプロパティがない場合は空の `{}` 文字列を入力してください。
{% endalert %}

##### ステップ 1.2: 認証情報を設定する

ロール、ウェアハウス、およびユーザーを設定し、適切な権限を付与します。既存の同期から認証情報を既に持っている場合、それを再利用できます。ただし、Canvasトリガーのソーステーブルへのアクセス権限を必ず拡張してください。

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### ステップ 1.3: ネットワークポリシーを設定する

アカウントにネットワークポリシーが設定されている場合、CDI サービス接続を有効にするために Braze の IP アドレスを許可リストに追加してください。IP アドレスの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips)を参照してください。

{% endtab %}
{% tab BigQuery %}

##### ステップ 1.1: ソーステーブル用の新しいプロジェクトまたはデータセットを作成する（オプション） {#step-11-create-a-new-project-or-dataset-for-your-source-table-optional}

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### ステップ 1.2: BigQuery でソーステーブルを設定する {#step-12-set-up-your-source-table-in-bigquery}
ソーステーブルを作成する際は、以下の内容を参照してください。

| フィールド名 | タイプ | 必須かどうか |
| :---- | :---- | :---- |
| **`UPDATED_AT`** | タイムスタンプ | はい |
| **`PROPERTIES`** | JSON | はい |
| **`EXTERNAL_ID`** | STRING | NULLABLE |
| **`ALIAS_NAME`** | STRING | NULLABLE |
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 1.2: BigQuery でソーステーブルを設定する" }

{% alert note %}
プロパティはすべての行やユーザーに対して必須ではありません。ただし、プロパティの値は有効な JSON 文字列でなければなりません。行にプロパティがない場合は空の `{}` 文字列を入力してください。
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

##### ステップ 1.3: 認証情報を設定する {#step-13-set-up-credentials}

ユーザーを作成し、権限を付与します。別の同期から既に認証情報を持っている場合、Canvasトリガーテーブルへのアクセス権がある限り、それらを再利用できます。

| 権限 | 目的 |
| :---- | :---- |
| BigQuery Connection User | Braze の接続を許可します。 |
| BigQuery User | Braze によるクエリの実行、メタデータの読み取り、テーブルの一覧表示を許可します。 |
| BigQuery Data Viewer | Braze によるデータセットとコンテンツの閲覧を許可します。 |
| BigQuery Job User | Braze によるジョブの実行を許可します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 1.3: 認証情報を設定する" }

権限を付与した後、JSON キーを生成します。手順については [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) を参照してください。後で Braze のダッシュボードにアップロードします。

##### ステップ 1.4: ネットワークポリシーを設定する {#step-14-configure-network-policies}
アカウントにネットワークポリシーが設定されている場合、CDI サービス接続を有効にするために Braze の IP アドレスを許可リストに追加してください。IP アドレスの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips)を参照してください。

{% endtab %}
{% tab Databricks %}

##### ステップ 1.1: ソーステーブルのカタログまたはスキーマを作成する {#step-11-create-a-catalog-or-schema-for-your-source-table}

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### ステップ 1.2: Databricks でソーステーブルを設定する {#step-12-set-up-your-source-table-in-databricks}

ソーステーブルを作成する際は、以下の内容を参照してください。

| フィールド名 | タイプ | 必須かどうか |
| :---- | :---- | :---- |
| `UPDATED_AT` | タイムスタンプ | はい |
| `PROPERTIES` | JSON | はい |
| `EXTERNAL_ID` | STRING |  NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ 1.2: Databricks でソーステーブルを設定する" }

スキーマとテーブルの名前は自由に付けられますが、列名は前述の定義と一致させる必要があります。

* `UPDATED_AT`: この行が更新されたか、テーブルに追加された時刻です。Braze は `UPDATED_AT` が最後に同期された値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
* ユーザー識別子列として、`external_id` または `alias_name` と `alias_label` のいずれかを使用します。これらは、Canvasメッセージングをトリガーしたいユーザーを識別するものです。
  * `EXTERNAL_ID`: ユーザーを識別し、Canvasにエントリさせます。これは Braze で使用されている `external_id` 値と一致する必要があります。
  * `ALIAS_NAME` と `ALIAS_LABEL`: これらの列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子であるべきであり、`alias_label` はエイリアスの種類を指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに alias_name は1つしか持てません。
* `PROPERTIES`: Canvas内でパーソナライゼーションプロパティとして利用可能にするフィールドの文字列または構造体です。ユーザー固有の情報を含める必要があります。

{% alert note %}
プロパティはすべての行やユーザーに対して必須ではありません。ただし、プロパティの値は有効な JSON 文字列でなければなりません。行にプロパティがない場合は空の `{}` 文字列を入力してください。
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

##### ステップ 1.3: 認証情報を設定する

Databricks で個人用アクセストークンを作成します。

1. ユーザー名を選択し、次に **User Settings** を選択します。
2. **Access tokens** タブで、**Generate new token** を選択します。
3. トークンを識別するためのコメントを追加します（例:「Braze CDI」）。
4. 有効期限を無期限にするには **Lifetime (days)** を空白のままにし、**Generate** を選択します。
5. トークンをコピーして安全に保存し、Braze ダッシュボードで使用します。

##### ステップ 1.4: ネットワークポリシーを設定する

アカウントにネットワークポリシーが設定されている場合、CDI サービス接続を有効にするために Braze の IP アドレスを許可リストに追加してください。IP アドレスの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips)を参照してください。

{% endtab %}
{% tab Fabric %}

##### ステップ 1.1: Fabric でソーステーブルを設定する {#step-11-set-up-your-source-table-in-fabric}

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

##### ステップ 1.2: 認証情報を設定する

サービスプリンシパルを作成し、権限を付与します。別の同期から既に認証情報を持っている場合、それを再利用できます。ただし、アカウントテーブルへのアクセス権があることを確認してください。

##### ステップ 1.3: ネットワークポリシーを設定する

アカウントにネットワークポリシーが設定されている場合、CDI サービス接続を有効にするために Braze の IP アドレスを許可リストに追加してください。IP アドレスの一覧については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional)を参照してください。

{% endtab %}
{% tab ファイルストレージ %}

ファイルストレージからCanvasトリガーを同期するには、以下のフィールドを含むソースファイルを作成します。

| フィールド | 必須 | 説明 |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | はい、`external_id` または `alias_name` と `alias_label` のいずれか | 更新したいユーザーを識別します。これは Braze で使用されている `external_id` 値と一致する必要があります。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | はい、`external_id` または `alias_name` と `alias_label` のいずれか | これら2つの列は、ユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子でなければならず、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つしか持てません。 |
| `PROPERTIES` | はい | Canvas内でパーソナライゼーションプロパティとして利用可能なフィールドの JSON 文字列です。ユーザー固有の情報を含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ 1.3: ネットワークポリシーを設定する" }

{% alert tip %}
ファイル名は AWS の規則に従い、一意でなければなりません。一意性を確保するためにタイムスタンプを追加してください。Amazon S3 の同期に関する詳細は、[ファイルストレージの統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/)を参照してください。
{% endalert %}

{% endtab %}
{% endtabs %}

#### ステップ 2: 送信先のCanvasを設定する {#step-2-configure-your-destination-canvas}

1. Canvasトリガー用の送信先Canvasを設定します。新しい API トリガー付きCanvasを作成するか、既存のものを選択します。API トリガーによる配信スケジュールタイプでCanvasを作成する方法については、[エントリスケジュールタイプ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types)を参照してください。
2. API トリガーによる配信スケジュールタイプを選択した後、Canvasの設定を続けてCanvasを構築します。Canvasは、単純な単一メッセージ送信から、複数のステップを含む複雑な顧客ワークフローまでさまざまです。
3. キャンバスステップ内で、ソーステーブルから同期する予定のプロパティフィールドを使って、[Canvasエントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)でメッセージをパーソナライズします。
  * 例えば、ステップ 1 でプロパティフィールドに `account_balance` を設定した場合、メッセージをパーソナライズするには以下の Liquid テンプレートを使用します: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`
5. Canvasを構築したら、起動して[ステップ 3](#step-3-create-your-zero-copy-sync)に進みます。

#### ステップ 3: ゼロコピー同期を作成する {#step-3-create-your-zero-copy-sync}

ソースの設定が完了し、送信先のCanvasが起動したら、新しいデータ同期を作成します。

1. Braze で、**データ設定** > **クラウドデータ取り込み**に移動します。
1. 接続の詳細を入力して（または既存の認証情報を再利用して）接続を設定し、[ステップ 1](#step-1-set-up-data-source-for-canvas-triggers) で指定したソーステーブルを指定します。
2. 統合に名前を付けます。
3. **Canvas Triggers** データタイプを選択します。
4. [ステップ 2](#step-2-configure-your-destination-canvas) で設定した送信先のCanvasを選択します。
5. 同期頻度を選択します。
6. 通知設定を行います。
7. **Test Connection** を選択して、すべてが期待通りに動作することを確認します。Snowflake に接続する場合、まずダッシュボードに表示されている公開キーを、Braze が Snowflake に接続するために作成したユーザーに追加してください。このステップを完了するには、Snowflake で **SECURITYADMIN** 以上のアクセス権限が必要です。
8. 同期を保存して、Canvasトリガーの同期を開始します。

同期が実行されると、ソーステーブルのユーザーがCanvasにエントリし始めます。Canvasの分析機能とクラウドデータ取り込みの同期ログページを使って、パフォーマンスを監視してください。

{% alert tip %}
予期しない送信を避けるため、設定全体（同期動作からCanvasの設定まで）を確認してください。レート制限、フリークエンシーキャップ、セグメンテーションフィルターなどのCanvas設定により、メッセージ配信をさらに精緻化できます。<br><br>本番環境でのユースケースを実装する前に、小規模なテストオーディエンスで試運転を行うことをお勧めします。
{% endalert %}

### 考慮事項 {#considerations}

CDI Canvasトリガーは、`/canvas/trigger/send` の REST API レート制限を利用します。このエンドポイントを CDI Canvasトリガーと REST API 統合で同時に使用する場合、その合計使用量がレート制限にカウントされることを想定してください。

各同期実行では、最大で1時間あたり約 375 万人のユーザーを、それぞれの送信先Canvasにエントリさせます。以下の場合には、ソースからCanvasへのエントリ時間が長くなることを想定してください。

* 1回の同期実行で 375 万人以上のユーザーを同期する場合。
* REST APIの [`/canvas/trigger/send` のレート制限]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit)が既に飽和状態にある場合に CDI Canvasトリガーを使用する場合。

メッセージのアーカイブが有効な場合のゼロコピー CDI について、以下の点を考慮してください。

* テーブルの結果は処理中に Braze に一時的に保存されます。また、同期された内容を正確に確認できるよう、Snowflake に 30 日間エクスポートされます。
* アーカイブされたメッセージは Braze 内のどこにも保存されません。コピーは、設定されたストレージにのみ保存されるよう送信されます。
* Canvasトリガーでゼロコピー CDI を使用する場合、Braze はデータウェアハウスからのクエリ結果のバックアップを保存せず、データはユーザープロファイルにコピーされません。
* Canvasコンテキストプロパティは、内部システムに最大 30 日間ログとして記録される場合があります。