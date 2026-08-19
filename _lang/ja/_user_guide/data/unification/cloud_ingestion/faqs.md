---
nav_title: FAQ
article_title: クラウドデータ取り込みに関する FAQ
page_order: 10
page_type: FAQ
description: "このページでは、クラウドデータ取り込みに関してよくある質問への回答を提供します。"
toc_headers: h2
---

# よくある質問 {#frequently-asked-questions}

> このページでは、クラウドデータ取り込みに関してよくある質問への回答を提供します。

## 「CDI同期エラー」というメールが届いたのはなぜですか？ {#why-was-i-emailed-error-in-cdi-sync}

この種のメールは通常、CDIの設定に問題があることを意味します。一般的な問題とその解決方法を以下に示します。

### CDIが認証情報を使用してデータウェアハウスまたはテーブルにアクセスできない {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

CDIの認証情報が正しくないか、データウェアハウス側で正しく設定されていない可能性があります。詳細については、[データウェアハウス統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照してください。

### テーブルが見つからない {#the-table-cannot-be-found}

正しいデータベース設定で統合を更新するか、`database/table`などの一致するリソースをデータウェアハウス上に作成してください。

### カタログが見つからない {#the-catalog-cannot-be-found}

統合で設定されたカタログがBrazeカタログに存在しません。統合の設定後にカタログが削除された可能性があります。この問題を解決するには、統合を更新して別のカタログを使用するか、統合のカタログ名と一致する新しいカタログを作成してください。

## 「CDI同期の行エラー」というメールが届いたのはなぜですか？ {#why-was-i-emailed-row-errors-in-your-cdi-sync}

このタイプのメールは、同期中に一部のデータを処理できなかったことを意味します。具体的なエラーを確認するには、Brazeで**CDI** > **同期ログ**に移動してログを確認してください。

## CDI設定で「Time must be string in ISO8601 Format」エラーを修正するには？ {#how-do-i-fix-time-must-be-string-in-iso8601-format-in-cdi-setup}

このエラーは、CDIペイロード内のイベント`time`値がサポートされている日時形式ではないことを意味します。

イベントおよび購入ペイロードの場合、`time`を以下の形式でフォーマットしてください。

- ISO 8601文字列、または
- `yyyy-MM-dd'T'HH:mm:ss:SSSZ`

`time`が省略された場合、Brazeはイベント時刻として`UPDATED_AT`を使用します。

ペイロード要件の詳細については、[Cloud Data Ingestionのテーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)を参照してください。

## テスト接続やサポートメールのエラーを修正するにはどうすればよいですか？ {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### テスト接続が遅い {#test-connection-runs-slow}

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことで速度が改善される場合があります。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間を最小限に抑え、クエリスループットを向上させることができますが、統合コストがわずかに高くなる可能性があります。

### Snowflakeインスタンスへの接続エラー：受信リクエストのIPがSnowflakeへのアクセスを許可されていない {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Brazeの公式IPをIP許可リストに追加してみてください。詳細については、[データウェアハウス統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照するか、関連するIPを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### 顧客設定によるSQL実行エラー：002003 (42S02)：SQLコンパイルエラー：存在しないか権限がない {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

テーブルが存在しない場合は、テーブルを作成してください。テーブルが存在する場合は、ユーザーとロールにテーブルからの読み取り権限があることを確認してください。

### スキーマを使用できない {#could-not-use-schema}

このエラーが表示された場合は、指定されたユーザーまたはロールにそのスキーマへのアクセス権限を付与してください。

### ロールを使用できない {#could-not-use-role}

このエラーが表示された場合は、そのユーザーが指定されたロールを使用できるようにしてください。

### ユーザーアクセスが無効 {#user-access-disabled}

このエラーが表示された場合は、そのユーザーにSnowflakeアカウントへのアクセスを許可してください。

### 現在のキーと古いキーでSnowflakeインスタンスに接続できないエラー {#error-connecting-to-snowflake-instance-with-current-and-old-key}

このエラーが表示された場合は、ユーザーがBrazeダッシュボードに表示されている現在の公開キーを使用していることを確認してください。
{% endtab %}

{% tab Redshift %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことで速度が改善される場合があります。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間を最小限に抑え、クエリスループットを向上させることができますが、統合コストがわずかに高くなる可能性があります。

### リレーション {table_name} に対する権限が拒否されました {#permission-denied-for-relation-table_name}

このエラーが表示された場合：

  - そのユーザーにスキーマの`usage`権限を付与してください。
  - そのユーザーにテーブルの`select`権限を付与してください。

### 接続作成エラー {#create-connection-error}

このエラーが表示された場合は、Redshiftのエンドポイントとポートが正しいことを確認してください。

### SSHトンネル作成エラー {#create-ssh-tunnel-error}

このエラーが表示された場合：

  - Brazeダッシュボードの公開キーが、SSHトンネリングに使用されるEC2ホスト上にあることを確認してください。
  - ユーザー名が正しいことを確認してください。
  - SSHトンネルが正しいことを確認してください。
{% endtab %}

{% tab BigQuery %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことで速度が改善される場合があります。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間を最小限に抑え、クエリスループットを向上させることができますが、統合コストがわずかに高くなる可能性があります。

### ユーザーにテーブルをクエリする権限がない {#user-does-not-have-permission-to-query-table}

このエラーが表示された場合は、テーブルをクエリするためのユーザー権限を追加してください。

### 使用量がカスタムクォータを超えました {#your-usage-exceeded-the-custom-quota}

このエラーが表示された場合は、現在のレートで同期を継続できるようにクォータを更新する必要があります。

### テーブルがロケーション {region} で見つかりませんでした {#table-was-not-found-in-location-region-location}

このエラーが表示された場合は、テーブルが正しいプロジェクトとデータセットにあることを確認してください。

### 無効なJWT署名 {#invalid-jwt-signature}

このエラーが表示された場合は、アカウントでBigQuery APIサービスが有効になっていることを確認してください。
{% endtab %}

{% tab Databricks %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことで速度が改善される場合があります。Databricksの場合、BrazeがClassicおよびPro SQLインスタンスに接続する際に2〜5分のウォームアップ時間が発生する場合があり、接続の設定やテスト、およびスケジュールされた同期の開始時に遅延が生じます。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間を最小限に抑え、クエリスループットを向上させることができますが、統合コストがわずかに高くなる可能性があります。

### ウェアハウスが停止していたためコマンドが失敗しました {#command-failed-because-warehouse-was-stopped}

このエラーが表示された場合は、Databricksウェアハウスが実行中であることを確認してください。

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

このエラーが表示された場合は、[Databricks: S3データへのアクセス時のForbiddenエラー](https://kb.databricks.com/security/forbidden-access-to-s3-data)を参照してください。
{% endtab %}
{% endtabs %}

## CDI統合のメールアラート設定を更新するにはどうすればよいですか？ {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

各統合には独自の通知設定があります。CDIページに移動し、更新したい統合名を選択します。**通知設定**セクションで、選択した統合に関するアラートの受信方法を更新できます。

## 将来の`UPDATED_AT`が統合と同期された場合はどうなりますか？ {#what-happens-if-a-future-updated_at-gets-synced-with-an-integration}

CDIは`UPDATED_AT`を使用して、どのデータが新しいかを判断します。将来の`UPDATED_AT`が同期された場合、その将来の日時より前のデータは処理されません。これを修正するには、以下の手順を実行してください。

1. `UPDATED_AT`を修正します。
2. Brazeと既に同期された古いデータを削除します。
3. 新しい統合を作成して、そのテーブルを再度処理します。

## 「同期された行数」がデータウェアハウスの数と一致しないのはなぜですか？ {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDIは`UPDATED_AT`を使用して、同期中にどのレコードを取得するかを決定します。仕組みについては[こちらの図解]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion#how-it-works)をご覧ください。同期の実行開始時に、CDIはデータウェアハウスにクエリを実行し、以前に処理された`UPDATED_AT`の値よりも後の`UPDATED_AT`を持つすべてのレコードを取得します。境界のタイムスタンプと完全に一致するレコードも、新しい行が同じタイムスタンプを共有している場合は再同期される可能性があります。クエリ実行時に取得されたレコードはすべてBrazeに同期されます。レコードが同期されない一般的なケースは以下のとおりです。

- すでに処理済みの`UPDATED_AT`値を持つレコードをテーブルに追加している場合。
- 同期で処理された後にレコードの値を更新しているが、`UPDATED_AT`を変更していない場合。
- 同期の進行中にレコードを追加または更新している場合。CDIクエリの実行タイミングによっては、レコードが取得されない競合が発生する可能性があります。

{% alert tip %}
これらの動作を今後回避するために、単調増加する`UPDATED_AT`値を使用し、スケジュールされた同期の実行中にテーブルを更新しないことをお勧めします。
{% endalert %}

## 大規模CDIインポートでは`UPDATED_AT`の値をほぼ一意にする必要がありますか？ {#do-i-need-mostly-distinct-updated_at-values-for-large-cdi-imports}

はい。大量のデータを処理する場合（たとえば約1,000万行を超える場合）、ソースデータの`UPDATED_AT`の値がほぼ一意であることを確認してください。同じタイムスタンプを共有する行が多すぎると、CDIが後続の実行で境界タイムスタンプの行を再選択する可能性が高くなります。これにより、重複同期やデータポイントの消費が増加する可能性があります。

CDIの境界動作の詳細については、[重複タイムスタンプを持つ行の再同期を回避する]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。

### これらのSQLチェックはどこで実行しますか？ {#where-do-i-run-these-sql-checks}

CDI統合で使用しているのと同じテーブルまたはビューに対して、データウェアハウスのSQLエディターで直接チェックを実行します。

- Snowflake: **Projects** > **Worksheets**（詳細については、[Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs)を参照してください）
- Redshift: Query Editor v2（詳細については、[Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)を参照してください）
- BigQuery: BigQuery Studio SQLワークスペース（詳細については、[BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction)を参照してください）
- Databricks: SQLエディター（SQLウェアハウス）（詳細については、[Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/)を参照してください）
- Fabric: SQLクエリエディター

大規模な同期を有効化またはスケールする前に、以下のプロセスを使用してください。

1. 検証したいCDIソーステーブルまたはビューと同期ウィンドウを特定します。
2. ウェアハウスのSQLエディターを開き、CDIで使用しているのと同じデータベースとスキーマを選択し、ソーステーブルまたはビューへの読み取りアクセス権を持つロールを使用します。
3. 一意のタイムスタンプ数クエリを実行して、そのウィンドウ内に存在する`UPDATED_AT`の一意の値の数を測定します。
4. `UPDATED_AT`でグループ化して行数をカウントするクエリを実行し、異常に多い行数を持つタイムスタンプを見つけます。
5. 同一のタイムスタンプを共有する行が多い場合は、連続するバッチが段階的に新しい`UPDATED_AT`の値を使用するように取り込みプロセスを調整するか、タイムスタンプの精度を上げて行がより分散されるようにします。
6. 集中が軽減されるまで両方のクエリを再実行し、その後同期を起動またはスケールします。
7. 起動後、**CDI** > **Sync Log**で境界タイムスタンプにおける予期しない再同期ボリュームを監視します。

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

ウェアハウスが`LIMIT`をサポートしていない場合（たとえばFabric）、`TOP`などの同等の構文を使用してください。

## 少数の行のCDI同期でも数分かかることがあるのはなぜですか？ {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

CDI同期には、行の処理が開始される前に固定の起動時間が含まれます。この起動時間は同期のサイズに関係なくほぼ同じであるため、少数の行の同期でも数分かかることがあり、1分あたりの行数で見ると遅く感じられる場合があります。同期の合計時間は、ソースクエリの複雑さ、データの形状、およびデータウェアハウスの利用可能な容量によって異なります。詳細については、[データウェアハウス統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照してください。

## 同期中に複数のレコードが同じIDを共有している場合、順序は保持されますか？ {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

処理順序は100%予測可能ではありません。たとえば、同期中にテーブル内に同じ `EXTERNAL_ID` を持つ複数の行がある場合、最終的なプロファイルにどの値が反映されるかは保証できません。ペイロード列で同じ `EXTERNAL_ID` に対して異なる属性を更新している場合、同期が完了した時点ですべての変更が反映されます。

## CDI同期から新しいユーザーが作成されないのはなぜですか？ {#why-are-new-users-not-being-created-from-my-cdi-sync}

CDI統合で**既存のユーザーのみを更新**オプションが有効になっている場合、Brazeにすでに存在するユーザーのみが更新され、新しいユーザーは作成されません。つまり、同期テーブルの行が既存のBrazeユーザーと一致しない`EXTERNAL_ID`を参照している場合、その行はスキップされます。

CDIを通じて新しいユーザーを作成するには、統合設定で**既存のユーザーのみを更新**トグルをオフにします。**Data Settings** > **Cloud Data Ingestion**に移動し、統合を選択します。

## CDIのセキュリティ対策とは？ {#what-are-the-security-measures-for-cdi}

### Braze側の対策 {#our-measures}

Brazeでは、CDIに対して以下の対策を講じています。

- すべての認証情報はデータベース内で暗号化されており、認証されたアクセス権を持つ特定の従業員のみがアクセスできます。
- 顧客のデータウェアハウスへのデータ転送には暗号化された接続を使用しています。
- Braze APIエンドポイントへのリクエストには、お客様にも推奨しているものと同じAPIキーおよびTLS接続を使用しています。
- ライブラリを定期的に更新し、セキュリティパッチを適用しています。

### お客様側の対策 {#your-measures}

お客様およびチームの皆様には、以下のセキュリティ対策を設定することをお勧めします。

- 認証情報のアクセスを、CDIの運用に必要な最小限に制限してください。これは、特定のテーブルやビューに対してselect（およびcount）を実行できる必要があるためです。
- テーブルにアクセスできるIPを、公式に公開されている[Braze IP]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)に制限してください。