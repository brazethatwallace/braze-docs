---
nav_title: SQLエディター
article_title: "クラウドデータ取り込み: SQLエディター"
description: "SQLクエリを使用してクラウドデータ取り込み同期を作成および検証する方法を説明します。"
page_order: 11
page_type: reference
toc_headers: h2
---

# クラウドデータ取り込み: SQLエディター {#cloud-data-ingestion-sql-editor}

> このページでは、Brazeクラウドデータ取り込み（CDI）SQLエディターを使用して、SQLクエリで同期を作成および検証する方法について説明します。

クラウドデータ取り込みのSQLエディターを使用すると、データウェアハウスに対してSQLクエリを直接記述して同期を作成できます。これにより、以前[データウェアハウス統合のステップ1.1]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)で必要だった専用のCDIテーブルの作成やメンテナンスが不要になります。

SQLエディターは、以下のような場合に使用します。

- アップストリームテーブルを変更せずにデータを同期したい場合
- データウェアハウス内の生データを操作したい場合
- `PAYLOAD`カラムの構築を避けたい場合
- SQLを使用してより複雑なデータユースケースを処理したい場合

## 前提条件と制限事項 {#prerequisites-and-limitations}

SQL エディターには以下の制限事項があります。

- データウェアハウスソースのみで利用可能: Snowflake、Redshift、BigQuery、Databricks、Fabric。
- 単一ステートメントの読み取り専用クエリのみがサポートされています。

{% alert note %}
Brazeはデータに対して読み取り専用クエリのみを実行し、基盤となるテーブルを変更することはありません。クエリ実行中に一時オブジェクトが作成される場合がありますが、永続化されることはありません。
{% endalert %}

## 新しい SQL エディター同期の作成 {#create-a-new-sql-editor-sync}

以下のステップに従って、まずソースを作成し、次に SQL エディターで同期を作成します。CDI のソースをすでに設定している場合は、ステップ 3 に進んでください。

{% alert note %}
これらのステップでは、Snowflake ソースを例として使用しています。他のデータウェアハウスソースの設定プロセスも同様であり、[データウェアハウス統合の設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations)ドキュメントの[ステップ 2: Braze ダッシュボードで新しいソースを作成する]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-2-create-a-new-source-in-the-braze-dashboard)に記載されています。
{% endalert %}

### ステップ 1: Snowflake のロール、権限、ウェアハウス、ユーザーを設定する {#step-1-set-up-your-snowflake-role-permissions-warehouse-and-user}

CDI で Snowflake ソースを作成する前に、Braze が使用する Snowflake ユーザーがクエリ対象のデータにアクセスでき、クエリを実行するためのウェアハウスがあることを確認してください。

#### ステップ 1.1: (オプション) データベースとスキーマを作成する {#step-11-optional-create-a-database-and-schema}

必要に応じて、CDI データ用の専用データベースとスキーマを作成します。

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### ステップ 1.2: ロールとデータベース権限を設定する {#step-12-set-up-role-and-database-permissions}

同期するテーブルへのアクセスを付与します。

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.MY_USER_TABLE TO ROLE BRAZE_INGESTION_ROLE;
```

ユースケースに応じて、複数のテーブルや将来のテーブルへのアクセスを付与することもできます。たとえば、スキーマ内のすべての将来のテーブルへのアクセスを付与するには、次のようにします。

```sql
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
```

#### ステップ 1.3: ウェアハウスを設定し、Braze ロールにアクセスを付与する {#step-13-set-up-the-warehouse-and-grant-access-to-the-braze-role}

Braze がクエリを実行するためのウェアハウスを作成します。

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスには自動再開フラグがオンになっている必要があります。オンになっていない場合は、クエリ実行時に Braze がウェアハウスをオンにできるよう、ウェアハウスに対する追加の `OPERATE` 権限を Braze に付与してください。
{% endalert %}

#### ステップ 1.4: Snowflake ユーザーを作成する {#step-14-create-a-snowflake-user}

Braze 用のユーザーを作成し、ロールを割り当てます。

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このユーザーは、Braze で Snowflake ソースを設定する際に使用します。

### ステップ 2: Braze ダッシュボードで新しいソースを作成する {#step-2-create-a-new-source-in-the-braze-dashboard}

このステップでは、Braze で Snowflake ソースを作成し、接続を検証します。

#### ステップ 2.1: Snowflake ソースを追加する {#step-21-add-a-snowflake-source}

1. Braze ダッシュボードで、**Data Settings** > **Cloud Data Ingestion** > **Sources** に移動します。
2. **Add data source** を選択します。
3. **Snowflake** を選択します。

#### ステップ 2.2: 接続の詳細を入力する {#step-22-enter-connection-details}

ソースの名前を選択し、Snowflake の認証情報と設定を入力します。

{% alert note %}
**Snowflake Account Locator** フィールドには、Snowflake の[アカウント識別子](https://docs.snowflake.com/en/user-guide/admin-account-identifier)を入力します。通常、`xy12345.us-east-1.aws` のような形式です。これはデータベース名やウェアハウス名とは異なります。
{% endalert %}

#### ステップ 2.3: RSA キーの設定を完了する {#step-23-complete-rsa-key-setup}

認証情報と設定を入力した後、**Save credentials** を選択して RSA キーを生成します。次に Snowflake に戻って設定を完了します。ダッシュボードに表示された公開キーを、Braze が Snowflake に接続するために作成したユーザーに追加します。

詳細については、[Snowflake キーペア認証](https://docs.snowflake.com/en/user-guide/key-pair-auth)を参照してください。キーをローテーションしたい場合、Braze は新しいキーペアを生成し、新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

Braze に戻り、**Test connection** を選択してソースへのアクセスを確認し、ソースを作成します。

### ステップ 3: 新しい同期を作成し、SQL クエリを記述する {#step-3-create-a-new-sync-and-write-your-sql-query}

1. **Data Settings** > **Cloud Data Ingestion** > **Syncs** に移動します。
2. **Create data sync** を選択します。
3. **Data Type** で任意の同期を選択します。
4. ステップ 2 のソースを参照します。
5. **SQL** を選択し、ウェアハウスからユーザーデータを返す SQL クエリを記述します。SQL クエリは Braze に同期するデータを定義します。クエリ結果が同期のスキーマになります。

Source Explorer を使用して同期元の利用可能なテーブルやビューを参照したり、AI SQL ジェネレーターを使用して SQL クエリについて Braze オペレーターの支援を受けたりできます。

{% alert note %}
`JOIN` 句を含む読み取り専用クエリのみがサポートされています。詳細については、[SQL の制約](#sql-constraints)を参照してください。
{% endalert %}

### ステップ 4: クエリをプレビューして検証する {#step-4-preview-and-validate-your-query}

**Preview and validate** を選択してクエリを実行します。

プレビューでは以下が表示されます。

- テーブル形式で結果を表示
- 最大 100 行を表示
- 最大 250 列を表示

検証を成功させるには、SQL クエリがさまざまな必須カラムを返す必要があります。

| 同期データタイプ | 必須カラム |
|---|---|
| 属性 | - ユーザー識別子。`external_id`、`braze_id`、`alias_name` と `alias_label`、メールまたは電話番号のいずれか。<br>- `UPDATED_AT`。<br>- 同期する追加カラム（属性）が少なくとも 1 つ。 |
| ユーザーの削除 | - ユーザー識別子。`external_id`、`braze_id`、`alias_name` と `alias_label`、メールまたは電話番号のいずれか。<br>- `UPDATED_AT`。 |
| キャンバストリガー | - ユーザー識別子。`external_id`、`braze_id`、`alias_name` と `alias_label`、メールまたは電話番号のいずれか。<br>- `UPDATED_AT`。 |
| カスタムイベント | - ユーザー識別子。`external_id`、`braze_id`、`alias_name` と `alias_label`、メールまたは電話番号のいずれか。<br>- `UPDATED_AT`。<br>- イベント名を表す `NAME`。<br>- イベント時刻を表す `TIME`。利用できない場合、CDI は代わりに `UPDATED_AT` を使用します。 |
| 購入イベント | - ユーザー識別子。`external_id`、`braze_id`、`alias_name` と `alias_label`、メールまたは電話番号のいずれか。<br>- `UPDATED_AT`。<br>- `PRODUCT_ID`。<br>- `CURRENCY`。<br>- `PRICE`。<br>- 購入イベント時刻を表す `TIME`。利用できない場合、CDI は代わりに `UPDATED_AT` を使用します。 |
| カタログ | - カタログアイテム識別子を表す `ID`。<br>- `UPDATED_AT`。<br>- 同期する追加カラム（カタログフィールド）が少なくとも 1 つ。 |
| アカウント | - アカウント識別子を表す `ID`。<br>- アカウント名を表す `NAME`。<br>- `UPDATED_AT`。<br>- 同期する追加カラム（アカウントフィールド）が少なくとも 1 つ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 4: クエリをプレビューして検証する" }

必須カラム以外の追加カラムは、それぞれ属性、キャンバスコンテキストプロパティ、イベントプロパティ、カタログフィールド、アカウントフィールドとして同期されます。プレビューと検証のエラーおよびその修正方法に関する役立つヒントについては、[検証の動作](#validation-behavior)と[トラブルシューティング](#troubleshooting)を参照してください。

### ステップ 5: 属性マッピングを確認して同期を作成する {#step-5-review-attribute-mapping-and-create-sync}

検証が成功したら、**Next: Notifications** に進み、同期を作成します。

{% alert important %}
不正確な SQL 設定は、データポイントの過剰消費やより広範な運用リスクを含む、意図しない結果につながる可能性があります。クエリロジックが正しいことを確認する責任はお客様にあり、同期を有効化する前にすべての結果を慎重にプレビューしてください。
{% endalert %}

## SQLの制約 {#sql-constraints}

### `SELECT`クエリのみを使用する {#use-select-queries-only}

読み取り専用クエリのみがサポートされています。

使用できるもの：

- `SELECT`
- `WITH`（CTE）
- `JOIN`

使用できないもの：

- `INSERT`、`UPDATE`、または`DELETE`
- `CREATE`または`DROP`
- `;`で区切られた複数のステートメント

### 単一のステートメントを使用する {#use-a-single-statement}

クエリは単一の実行可能なステートメントである必要があります。

## 検証の動作 {#validation-behavior}

SQLエディターは、続行を許可する前にクエリを検証します。

### SQLエラー {#sql-errors}

クエリに構文エラーが含まれている場合：

- 検証が失敗します
- プレビューは表示されません
- データウェアハウスからエラーメッセージが返されます

### コンパイルエラー {#compilation-errors}

クエリが無効なテーブル、カラム、または権限のないオブジェクトを参照している場合：

- 検証が失敗します
- プレビューは表示されません
- データウェアハウスからエラーメッセージが返されます

### 接続エラー {#connection-errors}

Brazeがデータウェアハウスに接続できない場合：

- 検証が失敗します
- プレビューは表示されません
- 接続エラーメッセージが表示されます

### クエリタイムアウト {#query-timeout}

クエリの実行時間が長すぎる場合：

- Brazeがクエリを終了します
- 検証が失敗します
- タイムアウトエラーが表示されます

### テーブルスキーマエラー {#table-schema-errors}

クエリがコンパイルされても、以下の場合は検証が失敗する可能性があります。

- 識別子カラムが見つからない
- `UPDATED_AT`が欠落している
- その他の必須カラムが欠落している

この場合、検証の成功に向けて役立つよう、プレビューは引き続き表示されます。各同期データタイプの必須カラムの詳細については、[前のセクションのステップ4](#step-4-preview-and-validate-your-query)を参照してください。

### ゼロ行の結果 {#zero-row-results}

クエリがゼロ行を返す場合：

- 検証は**合格**します
- 同期を作成できます
- 行が返されるまでユーザーは更新されません

## PAYLOADサポート（レガシー） {#payload-support-legacy}

SQL エディターは、`PAYLOAD` 列が存在する[レガシー CDI テーブル]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-1-set-up-tables-or-views)をサポートしています。

クエリに以下が含まれている場合:

- 有効な識別子
- `UPDATED_AT`
- `PAYLOAD` 列
- 追加の列

この場合:

- Brazeは`PAYLOAD` 列のみを同期します
- Brazeは追加の列を無視します

## SQL同期の編集 {#edit-a-sql-sync}

既存の同期を編集する場合:

- SQLの変更にはすべて再検証が必要です
- 無効な変更は保存できません
- 有効な変更は保存後に反映されます

同期の実行がすでに進行中の場合、変更は次回の実行時に反映されます。

## トラブルシューティング {#troubleshooting}

このセクションでは、一般的なエラーとそのトラブルシューティング方法について説明します。

### 「プレビューを利用できません」 {#no-preview-available}

「プレビューを利用できません」と表示された場合、以下のいずれかのエラータイプが原因である可能性があります。

| エラータイプ | 解決手順 |
|---|---|
| 「プレビューを利用できません」 | エラーバナーのヒントを確認してください。 |
| 「ソースに接続できません」 | 設定されたユーザー名、アカウントロケーター、RSAキーペア認証の設定を確認してください。<br>ウェアハウスが実行中であることを確認してください。<br>ネットワークアクセスを確認してください。 |
| 「SQL構文エラー」 | SQL構文を確認してください。 |
| 「オブジェクトが存在しないか、権限がありません」 | ロールがテーブルに対する`SELECT`アクセス権を持っていることを確認してください。<br>データベースとスキーマの権限を確認してください。<br>テーブル名のタイプミスを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="「プレビューを利用できません」" }

### 「識別子カラムが必要です」 {#identity-column-required}

クエリに`external_id`などの有効な識別子が含まれていることを確認してください。

### 「`UPDATED_AT`カラムがありません」 {#updated_at-column-is-missing}

増分同期用のタイムスタンプカラムを追加してください。

### 「カラムを追加してください...同期する属性/カタログフィールド/アカウントフィールドがありません」 {#add-more-columns-there-are-no-attributescatalog-fieldsaccount-fields-to-sync}

識別子と`UPDATED_AT`以外に、少なくとも1つの追加カラムを追加してください。

### 「クエリの実行がタイムアウトしました」 {#query-execution-timed-out}

クエリを最適化するか、より大きなウェアハウスを使用してください。