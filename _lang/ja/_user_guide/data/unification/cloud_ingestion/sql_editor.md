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

クラウドデータ取り込みのSQLエディターを使用すると、データウェアハウスに対してSQLクエリを直接記述して同期を作成できます。これにより、以前[データウェアハウス統合のステップ1.1]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)で必要だった専用のCDIテーブルの作成やメンテナンスが不要になります。

SQLエディターは、以下のような場合に使用します。

- アップストリームテーブルを変更せずにデータを同期したい場合
- データウェアハウス内の生データを操作したい場合
- `PAYLOAD`カラムの構築を避けたい場合
- SQLを使用してより複雑なデータユースケースを処理したい場合

{% alert important %}
クラウドデータ取り込みSQLエディターはベータ版です。アクセスについては、カスタマーサクセスマネージャーまたはアカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件と制限事項 {#prerequisites-and-limitations}

SQLエディターには以下の制限事項があります。

- データウェアハウスソースのみで利用可能：Snowflake、Redshift、BigQuery、Databricks、Fabric。
- 単一ステートメントの読み取り専用クエリのみがサポートされています。

{% alert note %}
Brazeはデータに対して読み取り専用クエリのみを実行し、基盤となるテーブルを変更しません。クエリ実行中に一時オブジェクトが作成される場合がありますが、永続化されることはありません。
{% endalert %}

## 新しいSQLエディター同期の作成 {#create-a-new-sql-editor-sync}

以下の手順に従って、まずソースを作成し、次にSQLエディターで同期を作成します。CDI用のソースをすでに設定している場合は、ステップ3に進んでください。

{% alert note %}
これらの手順では、例としてSnowflakeソースを使用しています。他のデータウェアハウスソースの設定プロセスも同様であり、[データウェアハウス統合の設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#setting-up-data-warehouse-integrations)ドキュメントの[ステップ2：Brazeダッシュボードで新しいソースを作成する]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-2-create-a-new-source-in-the-braze-dashboard)を参照してください。
{% endalert %}

### ステップ1：Snowflakeのロール、権限、ウェアハウス、ユーザーの設定 {#step-1-set-up-your-snowflake-role-permissions-warehouse-and-user}

CDIでSnowflakeソースを作成する前に、Brazeが使用するSnowflakeユーザーがクエリ対象のデータにアクセスでき、クエリを実行するためのウェアハウスを持っていることを確認してください。

#### ステップ1.1：（オプション）データベースとスキーマの作成 {#step-11-optional-create-a-database-and-schema}

必要に応じて、CDIデータ用の専用データベースとスキーマを作成します。

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### ステップ1.2：ロールとデータベース権限の設定 {#step-12-set-up-role-and-database-permissions}

同期するテーブルへのアクセスを付与します。

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.MY_USER_TABLE TO ROLE BRAZE_INGESTION_ROLE;
```

ユースケースに応じて、複数のテーブルや将来のテーブルへのアクセスを付与することもできます。たとえば、スキーマ内のすべての将来のテーブルへのアクセスを付与するには、以下のようにします。

```sql
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
```

#### ステップ1.3：ウェアハウスの設定とBrazeロールへのアクセス付与 {#step-13-set-up-the-warehouse-and-grant-access-to-the-braze-role}

Brazeがクエリを実行するためのウェアハウスを作成します。

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスでは自動再開フラグが有効になっている必要があります。有効になっていない場合は、クエリ実行時にBrazeがウェアハウスをオンにできるよう、ウェアハウスに対する追加の`OPERATE`権限をBrazeに付与してください。
{% endalert %}

#### ステップ1.4：Snowflakeユーザーの作成 {#step-14-create-a-snowflake-user}

Braze用のユーザーを作成し、ロールを割り当てます。

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このユーザーは、BrazeでSnowflakeソースを設定する際に使用します。

### ステップ2：Brazeダッシュボードでの新しいソースの作成 {#step-2-create-a-new-source-in-the-braze-dashboard}

このステップでは、BrazeでSnowflakeソースを作成し、接続を検証します。

#### ステップ2.1：Snowflakeソースの追加 {#step-21-add-a-snowflake-source}

1. Brazeダッシュボードで、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動します。
2. **データソースを追加**を選択します。
3. **Snowflake**を選択します。

#### ステップ2.2：接続情報の入力 {#step-22-enter-connection-details}

ソースの名前を選択し、Snowflakeの認証情報と設定を入力します。

{% alert note %}
**Snowflakeアカウントロケーター**フィールドには、Snowflakeの[アカウント識別子](https://docs.snowflake.com/en/user-guide/admin-account-identifier)を入力します。通常、`xy12345.us-east-1.aws`のような形式です。これはデータベース名やウェアハウス名とは異なります。
{% endalert %}

#### ステップ2.3：RSAキーの設定完了 {#step-23-complete-rsa-key-setup}

認証情報と設定を入力した後、**認証情報を保存**を選択してRSAキーを生成します。次に、Snowflakeに戻って設定を完了します。ダッシュボードに表示される公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加します。

詳細については、[Snowflakeキーペア認証](https://docs.snowflake.com/en/user-guide/key-pair-auth)を参照してください。キーをローテーションしたい場合、Brazeは新しいキーペアを生成し、新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

Brazeに戻り、**接続をテスト**を選択してソースへのアクセスを確認し、ソースを作成します。

### ステップ3：新しい同期の作成とSQLクエリの記述 {#step-3-create-a-new-sync-and-write-your-sql-query}

1. **データ設定** > **クラウドデータ取り込み** > **同期**に移動します。
2. **データ同期を作成**を選択します。
3. **データタイプ**で任意の同期を選択します。
4. ステップ2のソースを参照します。
5. **SQL**を選択し、データウェアハウスからユーザーデータを返すSQLクエリを記述します。SQLクエリは、Brazeに同期するデータを定義します。クエリ結果が同期のスキーマになります。

ソースエクスプローラーを使用して、同期元として利用可能なテーブルやビューを参照したり、AI SQLジェネレーターを使用してBraze OperatorにSQLクエリの支援を依頼したりできます。

{% alert note %}
`JOIN`句を含む読み取り専用クエリのみがサポートされています。詳細については、[SQLの制約](#sql-constraints)を参照してください。
{% endalert %}

### ステップ4：クエリのプレビューと検証 {#step-4-preview-and-validate-your-query}

**プレビューと検証**を選択してクエリを実行します。

プレビューでは以下が表示されます。

- テーブル形式での結果
- 最大100行
- 最大250カラム

検証を正常に完了するには、SQLクエリが以下の必須カラムを返す必要があります。

| 同期データタイプ | 必須カラム |
|---|---|
| 属性 | - ユーザー識別子（`external_id`、`braze_id`、`alias_name`と`alias_label`、メールまたは電話番号のいずれか）。<br>- `UPDATED_AT`。<br>- 同期する少なくとも1つの追加カラム（属性）。 |
| ユーザー削除 | - ユーザー識別子（`external_id`、`braze_id`、`alias_name`と`alias_label`、メールまたは電話番号のいずれか）。<br>- `UPDATED_AT`。 |
| Canvasトリガー | - ユーザー識別子（`external_id`、`braze_id`、`alias_name`と`alias_label`、メールまたは電話番号のいずれか）。<br>- `UPDATED_AT`。 |
| カスタムイベント | - ユーザー識別子（`external_id`、`braze_id`、`alias_name`と`alias_label`、メールまたは電話番号のいずれか）。<br>- `UPDATED_AT`。<br>- イベント名を表す`NAME`。<br>- イベント時刻を表す`TIME`。利用できない場合、CDIは代わりに`UPDATED_AT`を使用します。 |
| 購入イベント | - ユーザー識別子（`external_id`、`braze_id`、`alias_name`と`alias_label`、メールまたは電話番号のいずれか）。<br>- `UPDATED_AT`。<br>- `PRODUCT_ID`。<br>- `CURRENCY`。<br>- `PRICE`。<br>- 購入イベント時刻を表す`TIME`。利用できない場合、CDIは代わりに`UPDATED_AT`を使用します。 |
| カタログ | - カタログアイテム識別子を表す`ID`。<br>- `UPDATED_AT`。<br>- 同期する少なくとも1つの追加カラム（カタログフィールド）。 |
| アカウント | - アカウント識別子を表す`ID`。<br>- アカウント名を表す`NAME`。<br>- `UPDATED_AT`。<br>- 同期する少なくとも1つの追加カラム（アカウントフィールド）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ4：クエリのプレビューと検証" }

必須カラム以外の追加カラムは、それぞれ属性、Canvasコンテキストプロパティ、イベントプロパティ、カタログフィールド、アカウントフィールドとして同期されます。プレビューと検証のエラーおよびその修正方法に関する役立つヒントについては、[検証の動作](#validation-behavior)と[トラブルシューティング](#troubleshooting)を参照してください。

### ステップ5：属性マッピングの確認と同期の作成 {#step-5-review-attribute-mapping-and-create-sync}

検証が成功したら、**次へ：通知**に進み、同期を作成します。

{% alert important %}
不正確なSQL設定は、データポイントの過剰消費やより広範な運用リスクを含む、意図しない結果につながる可能性があります。クエリロジックが正しいことを確認する責任はお客様にあり、同期を有効化する前にすべての結果を慎重にプレビューしてください。
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

## `PAYLOAD`サポート（レガシー） {#payload-support-legacy}

SQLエディターは、`PAYLOAD`カラムが存在する[レガシーCDIテーブル]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-1-set-up-tables-or-views)をサポートしています。

クエリに以下が含まれている場合：

- 有効な識別子
- `UPDATED_AT`
- `PAYLOAD`カラム
- 追加カラム

その場合：

- Brazeは`PAYLOAD`カラムのみを同期します
- Brazeは追加カラムを無視します

## SQL同期の編集 {#edit-a-sql-sync}

既存の同期を編集する場合：

- SQLの変更には再検証が必要です
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

### 「同期する属性/カタログフィールド/アカウントフィールドがありません」 {#add-more-columns-there-are-no-attributescatalog-fieldsaccount-fields-to-sync}

識別子と`UPDATED_AT`以外に、少なくとも1つの追加カラムを追加してください。

### 「クエリの実行がタイムアウトしました」 {#query-execution-timed-out}

クエリを最適化するか、より大きなウェアハウスを使用してください。