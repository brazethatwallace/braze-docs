---
nav_title: よくある質問
article_title: クラウドデータ取り込みに関する FAQ
page_order: 10
page_type: FAQ
description: "このページでは、クラウドデータ取り込みに関してよくある質問への回答を提供します。"
toc_headers: h2
---

# よくある質問 {#frequently-asked-questions}

> このページでは、クラウドデータ取り込みに関してよくある質問への回答を提供します。

## 「Error in CDI Sync」（CDI 同期のエラー）というメールが届いた理由は何ですか? {#why-was-i-emailed-error-in-cdi-sync}

この種のメールは通常、CDI の設定に問題があることを意味します。ここでは、よくある問題とその解決方法を紹介します。

### CDI がお客様の認証情報を使用してデータウェアハウスやテーブルにアクセスできない {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

CDI の認証情報が正しくないか、データウェアハウスの設定が正しくない可能性があります。詳細については、[データウェアハウスの統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照してください。

### テーブルが見つからない {#the-table-cannot-be-found}

正しいデータベース設定を使用して統合を更新するか、データウェアハウスに `database/table` などの一致するリソースを作成してください。

### カタログが見つからない {#the-catalog-cannot-be-found}

統合で設定されたカタログは、Brazeカタログには存在しません。カタログは、統合の設定後に削除された可能性があります。この問題を解決するには、別のカタログを使用するように統合を更新するか、統合のカタログ名と一致する新しいカタログを作成してください。

## 「Row errors in your CDI sync」（CDI 同期の行エラー）というメールが届いた理由は何ですか? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

この種のメールは、同期中にデータの一部が処理できなかったことを意味します。具体的なエラーを調べるには、Brazeで**CDI** > **同期ログ**に移動してログを確認できます。

## テスト接続とサポートメールのエラーを修正するには? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### テスト接続が遅い {#test-connection-runs-slow}

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことでスピードが向上する可能性があります。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、統合コストが若干高くなる場合があります。

### Snowflakeインスタンスへの接続エラー：IPを含む着信リクエストがSnowflakeへのアクセスを許可されていない {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

IP 許可リストにBrazeの公式 IP を追加してみてください。詳細については、[データウェアハウスの統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照するか、該当する IP を許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### 顧客設定による SQL 実行エラー：002003 (42S02): SQL コンパイルエラー：存在しないか、認証されていない {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

テーブルが存在しない場合は、テーブルを作成します。テーブルが存在する場合は、ユーザーとロールにテーブルからの読み取り権限があることを確認してください。

### スキーマを使用できなかった {#could-not-use-schema}

このエラーが発生した場合は、指定されたユーザーまたはロールにそのスキーマへのアクセスを許可してください。

### ロールを使用できなかった {#could-not-use-role}

このエラーが発生した場合は、そのユーザーに指定されたロールの使用を許可してください。

### ユーザーアクセスが無効 {#user-access-disabled}

このエラーが発生した場合は、そのユーザーにSnowflakeアカウントへのアクセスを許可してください。

### 現在のキーと古いキーでSnowflakeインスタンスに接続する際のエラー {#error-connecting-to-snowflake-instance-with-current-and-old-key}

このエラーが発生した場合は、ユーザーがBrazeダッシュボードに表示されている現在の公開キーを使用していることを確認してください。
{% endtab %}

{% tab Redshift %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことでスピードが向上する可能性があります。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、統合コストが若干高くなる場合があります。

### リレーションに対する権限が拒否された {table_name} {#permission-denied-for-relation-table_name}

このエラーが発生した場合:

  - そのユーザーのスキーマに `usage` 権限を付与します。
  - そのユーザーに、そのテーブルの `select` 権限を付与します。

### 接続作成エラー {#create-connection-error}

このエラーが発生した場合は、Redshiftのエンドポイントとポートが正しいことを確認してください。

### SSH トンネル作成エラー {#create-ssh-tunnel-error}

このエラーが発生した場合:

  - Brazeダッシュボードの公開キーが、SSH トンネリングに使用する EC2 ホスト上にあることを確認します。
  - ユーザー名が正しいことを確認します。
  - SSH トンネルが正しいことを確認します。
{% endtab %}

{% tab BigQuery %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことでスピードが向上する可能性があります。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、統合コストが若干高くなる場合があります。

### ユーザーにテーブルをクエリする権限がない {#user-does-not-have-permission-to-query-table}

このエラーが発生した場合は、ユーザー権限を追加してテーブルをクエリできるようにしてください。

### 使用量がカスタムクォータを超えた {#your-usage-exceeded-the-custom-quota}

このエラーが発生した場合は、現在のレートで同期を続けられるようにクォータを更新する必要があります。

### テーブルがロケーション {region} に見つからなかった {#table-was-not-found-in-location-region-location}

このエラーが発生した場合は、テーブルが正しいプロジェクトとデータセットにあることを確認してください。

### 無効な JWT 署名 {#invalid-jwt-signature}

このエラーが発生した場合は、アカウントで BigQuery API サービスが有効になっていることを確認してください。
{% endtab %}

{% tab Databricks %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことでスピードが向上する可能性があります。Databricksの場合、BrazeがClassic および Pro の SQL インスタンスに接続するときにウォームアップ時間が 2〜5 分かかることがあるため、接続の設定中やテスト中、およびスケジュールされた同期の開始時に遅延が発生します。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、統合コストが若干高くなる場合があります。

### ウェアハウスが停止していたためコマンドが失敗した {#command-failed-because-warehouse-was-stopped}

このエラーが発生した場合は、Databricksウェアハウスが実行されていることを確認してください。

### サービス：Amazon S3、ステータスコード：403、エラーコード：403 Forbidden {#service-amazon-s3-status-code-403-error-code-403-forbidden}

このエラーが発生した場合は、[Databricks: S3 データへのアクセス中の Forbidden エラー](https://kb.databricks.com/security/forbidden-access-to-s3-data)を参照してください。
{% endtab %}
{% endtabs %}

## CDI 統合のメールアラート設定を更新するには? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

各統合には、それぞれ独自の通知設定があります。CDI ページに移動し、更新したい統合名を選択してください。**通知設定**セクションで、選択した統合に関するアラートの受信方法を更新できます。

## 将来の UPDATED_AT が統合と同期されたらどうなりますか? {#what-happens-if-a-future-updated_at-gets-synced-with-an-integration}

CDI は `UPDATED_AT` を使用して、新しいデータを特定します。未来の `UPDATED_AT` を同期すると、その日時以前のデータは処理されません。これを修正するには、次の操作を行います。

1. `UPDATED_AT` を修正します。
2. Brazeと同期済みの古いデータを削除します。
3. そのテーブルを再び処理するために、新しい統合を作成します。

## なぜ「同期された行数」がウェアハウスの数値と一致しないのですか? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDI は `UPDATED_AT` を使用して、同期中に取得するレコードを決定します。どのように機能するかは、[このイラスト]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion#what-gets-synced)をご覧ください。同期処理の開始時、CDI はデータウェアハウスにクエリを実行し、前回処理した `UPDATED_AT` タイムスタンプ以降の `UPDATED_AT` を持つ全レコードを取得します。境界タイムスタンプと完全に一致するレコードも、新しい行がそのタイムスタンプを共有している場合は再同期される可能性があります。クエリ実行時にピックアップされたレコードはすべてBrazeに同期されます。以下は、レコードが同期されない可能性のある一般的なケースです。

- すでに処理済みの `UPDATED_AT` 値を持つレコードをテーブルに追加している。
- 同期によってレコードを処理した後に、それらのレコードの値を更新しているが、`UPDATED_AT` を変更していない。
- 同期の進行中にレコードの追加または更新を実行している。CDI クエリの実行タイミングによっては、レコードがピックアップされない競合が発生する可能性があります。

{% alert tip %}
今後、このような動作を回避するために、単調増加する `UPDATED_AT` 値を使用し、スケジュールされた同期実行中にはテーブルを更新しないことをお勧めします。
{% endalert %}

## 大規模な CDI インポートでは、`UPDATED_AT` 値がほぼ一意である必要がありますか? {#do-i-need-mostly-distinct-updated_at-values-for-large-cdi-imports}

はい。大量の行を処理する場合（例：約 1,000 万行以上）、ソースデータの `UPDATED_AT` 値がほぼ一意であることを確認してください。同じタイムスタンプを共有する行が多すぎると、CDI が後続の実行で境界タイムスタンプの行を再選択する可能性が高くなります。これにより、重複同期やデータポイントの消費が増加する可能性があります。

CDI の境界動作の詳細については、[重複タイムスタンプを持つ行の再同期を回避する]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。

### これらの SQL チェックはどこで実行しますか? {#where-do-i-run-these-sql-checks}

CDI 統合で使用しているのと同じテーブルまたはビューに対して、データウェアハウスの SQL エディターで直接チェックを実行してください。

- Snowflake：**Projects** > **Worksheets**（詳細については、[Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs) を参照）
- Redshift：Query Editor v2（詳細については、[Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html) を参照）
- BigQuery：BigQuery Studio SQL workspace（詳細については、[BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction) を参照）
- Databricks：SQL editor（SQL warehouse）（詳細については、[Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/) を参照）
- Fabric：SQL query editor

大規模な同期を有効化またはスケールする前に、以下のプロセスを使用してください。

1. 検証したい CDI ソーステーブルまたはビューと同期ウィンドウを特定します。
2. ウェアハウスの SQL エディターを開き、CDI が使用しているのと同じデータベースとスキーマを選択し、ソーステーブルまたはビューへの読み取りアクセス権を持つロールを使用します。
3. 一意のタイムスタンプ数クエリを実行して、そのウィンドウ内に存在する `UPDATED_AT` の一意の値の数を測定します。
4. `UPDATED_AT` でグループ化して行数をカウントするクエリを実行し、異常に多い行数を持つタイムスタンプを見つけます。
5. 同一のタイムスタンプを共有する行が多い場合は、連続するバッチがより新しい `UPDATED_AT` 値を使用するように取り込みプロセスを調整するか、タイムスタンプの精度を上げて行がより分散されるようにします。
6. 集中が軽減されるまで両方のクエリを再実行し、その後同期を起動またはスケールします。
7. 起動後、**CDI** > **同期ログ**で境界タイムスタンプにおける予期しない再同期量を監視します。

ウェアハウスで以下のようなチェックを使用してください。

```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT UPDATED_AT) AS distinct_timestamps,
  ROUND(COUNT(*) * 1.0 / NULLIF(COUNT(DISTINCT UPDATED_AT), 0), 2) AS avg_rows_per_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP);
```

```sql
SELECT
  UPDATED_AT,
  COUNT(*) AS rows_at_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP)
GROUP BY UPDATED_AT
ORDER BY rows_at_timestamp DESC
LIMIT 20;
```

ウェアハウスが `LIMIT` をサポートしていない場合（例：Fabric）、`TOP` などの同等の構文を使用してください。

## 少数の行の CDI 同期でも数分かかるのはなぜですか? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

CDI 同期には、行の処理が開始される前に固定のスタートアップ期間があります。このスタートアップ時間は同期サイズに関係なくほぼ同じであるため、少数の行の同期でも数分かかることがあり、1 分あたりの行数で見ると遅く見える場合があります。合計同期時間は、ソースクエリの複雑さ、データの形状、およびデータウェアハウスの利用可能な容量に依存します。詳細については、[データウェアハウスの統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照してください。

## 同期中、複数のレコードが同じ ID を共有する場合、順序は保持されますか? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

処理順序は 100% 予測できるものではありません。例えば、同期中にテーブル内に同じ `EXTERNAL_ID` を持つ複数の行がある場合、最終的にどの値がプロファイルに入るかは保証できません。同じ `EXTERNAL_ID` をペイロード列の異なる属性で更新している場合、同期が完了するとすべての変更が反映されます。

## なぜ CDI 同期から新規ユーザーが作成されないのですか? {#why-are-new-users-not-being-created-from-my-cdi-sync}

CDI 統合で**既存ユーザーのみ更新**オプションが有効になっている場合、Brazeに既に存在するユーザーのみが更新され、新規ユーザーは作成されません。これは、同期テーブルの行が既存のBrazeユーザーと一致しない `EXTERNAL_ID` を参照している場合、その行はスキップされることを意味します。

CDI を通じて新規ユーザーを作成するには、統合設定で**既存ユーザーのみ更新**トグルをオフにしてください。**データ設定** > **クラウドデータ取り込み**に移動し、統合を選択します。

## CDI のセキュリティ対策はどうなっていますか? {#what-are-the-security-measures-for-cdi}

### 当社の取り組み {#our-measures}

Brazeでは CDI に関して以下の対策を講じています。

- すべての認証情報はデータベース内で暗号化され、特定の社員のみが認証されたアクセス権を持ちます。
- 暗号化された接続を使用して、お客様のウェアハウスからデータを取得しています。
- Braze API エンドポイントへのリクエストは、当社がお客様に使用を推奨しているのと同じ API キーと TLS 接続を使用して行います。
- 定期的にライブラリを更新し、すべてのセキュリティパッチを取得しています。

### お客様の対策 {#your-measures}

お客様と社内チームで、以下のセキュリティ対策を講じることをお勧めします。

- 認証情報へのアクセスを、CDI の運用に必要な最小限に制限します。これは、特定のテーブルとビューに対して select（と count）を実行できるようにする必要があるためです。
- テーブルにアクセスできる IP を、正式に公開された [Braze IP]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views) に制限します。