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

## 「CDI同期でエラーが発生しました」というメールが届いたのはなぜですか？ {#why-was-i-emailed-error-in-cdi-sync}

このタイプのメールは通常、CDIの設定に問題があることを意味します。一般的な問題とその解決方法を以下に示します。

### CDIが認証情報を使用してデータウェアハウスまたはテーブルにアクセスできない {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

CDIの認証情報が正しくないか、データウェアハウスで正しく設定されていない可能性があります。詳細については、[データウェアハウス連携]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照してください。

### テーブルが見つからない {#the-table-cannot-be-found}

正しいデータベース設定で連携を更新するか、`database/table`などの一致するリソースをデータウェアハウスに作成してください。

### カタログが見つからない {#the-catalog-cannot-be-found}

連携で設定されたカタログがBrazeカタログに存在しません。連携の設定後にカタログが削除された可能性があります。この問題を解決するには、別のカタログを使用するように連携を更新するか、連携のカタログ名と一致する新しいカタログを作成してください。

## 「CDI同期の行エラー」というメールが届いたのはなぜですか？ {#why-was-i-emailed-row-errors-in-your-cdi-sync}

このタイプのメールは、同期中に一部のデータを処理できなかったことを意味します。具体的なエラーを確認するには、Brazeで**CDI** > **同期ログ**に移動してログを確認してください。

## CDI設定で「Time must be string in ISO8601 Format」エラーを修正するには？ {#how-do-i-fix-time-must-be-string-in-iso8601-format-in-cdi-setup}

このエラーは、CDIペイロード内のイベント`time`の値がサポートされている日時形式ではないことを意味します。

イベントおよび購入ペイロードの場合、`time`を以下のいずれかの形式でフォーマットしてください。

- ISO 8601文字列
- `yyyy-MM-dd'T'HH:mm:ss:SSSZ`

`time`が省略された場合、Brazeはイベント時刻として`UPDATED_AT`を使用します。

ペイロード要件の詳細については、[Cloud Data Ingestionのテーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)を参照してください。

## 接続テストやサポートメールのエラーを修正するにはどうすればよいですか？ {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### 接続テストの実行が遅い {#test-connection-runs-slow}

接続テストはデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすと速度が改善される場合があります。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間を最小限に抑え、クエリスループットを向上させることができますが、統合コストがわずかに高くなる可能性があります。

### Snowflakeインスタンスへの接続エラー：Incoming request with IP is not allowed to access Snowflake {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Braze公式IPをIP許可リストに追加してみてください。詳細については、[データウェアハウス統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照するか、該当するIPを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### 顧客設定によるSQL実行エラー：002003 (42S02): SQL compilation error: does not exist or not authorized {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

テーブルが存在しない場合は、テーブルを作成してください。テーブルが存在する場合は、ユーザーとロールにテーブルからの読み取り権限があることを確認してください。

### スキーマを使用できない {#could-not-use-schema}

このエラーが表示された場合は、指定されたユーザーまたはロールにそのスキーマへのアクセスを許可してください。

### ロールを使用できない {#could-not-use-role}

このエラーが表示された場合は、そのユーザーに指定されたロールの使用を許可してください。

### ユーザーアクセスが無効化されている {#user-access-disabled}

このエラーが表示された場合は、そのユーザーにSnowflakeアカウントへのアクセスを許可してください。

### 現在のキーと古いキーでSnowflakeインスタンスに接続するエラー {#error-connecting-to-snowflake-instance-with-current-and-old-key}

このエラーが表示された場合は、Brazeダッシュボードに表示されている現在の公開キーをユーザーが使用していることを確認してください。
{% endtab %}

{% tab Redshift %}
### 接続テストの実行が遅い

接続テストはデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすと速度が改善される場合があります。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間を最小限に抑え、クエリスループットを向上させることができますが、統合コストがわずかに高くなる可能性があります。

### Permission denied for relation {table_name} {#permission-denied-for-relation-table_name}

このエラーが表示された場合：

  - そのユーザーにスキーマの`usage`権限を付与してください。
  - そのユーザーにテーブルの`select`権限を付与してください。

### 接続作成エラー {#create-connection-error}

このエラーが表示された場合は、Redshiftのエンドポイントとポートが正しいことを確認してください。

### SSHトンネル作成エラー {#create-ssh-tunnel-error}

このエラーが表示された場合：

  - Brazeダッシュボードの公開キーが、SSHトンネリングに使用するEC2ホストに登録されていることを確認してください。
  - ユーザー名が正しいことを確認してください。
  - SSHトンネルが正しいことを確認してください。
{% endtab %}

{% tab BigQuery %}
### 接続テストの実行が遅い

接続テストはデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすと速度が改善される場合があります。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間を最小限に抑え、クエリスループットを向上させることができますが、統合コストがわずかに高くなる可能性があります。

### ユーザーにテーブルのクエリ権限がない {#user-does-not-have-permission-to-query-table}

このエラーが表示された場合は、テーブルのクエリ権限をユーザーに追加してください。

### カスタムクォータを超過した {#your-usage-exceeded-the-custom-quota}

このエラーが表示された場合は、現在の速度で同期を続けるためにクォータを更新する必要があります。

### テーブルがロケーション {region} に見つからない {#table-was-not-found-in-location-region-location}

このエラーが表示された場合は、テーブルが正しいプロジェクトとデータセットにあることを確認してください。

### 無効なJWT署名 {#invalid-jwt-signature}

このエラーが表示された場合は、アカウントでBigQuery APIサービスが有効になっていることを確認してください。
{% endtab %}

{% tab Databricks %}
### 接続テストの実行が遅い

接続テストはデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすと速度が改善される場合があります。Databricksの場合、BrazeがClassicおよびPro SQLインスタンスに接続する際に2〜5分のウォームアップ時間が発生することがあり、接続の設定やテスト、およびスケジュールされた同期の開始時に遅延が生じます。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間を最小限に抑え、クエリスループットを向上させることができますが、統合コストがわずかに高くなる可能性があります。

### ウェアハウスが停止しているためコマンドが失敗した {#command-failed-because-warehouse-was-stopped}

このエラーが表示された場合は、Databricksウェアハウスが実行中であることを確認してください。

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

このエラーが表示された場合は、[Databricks: S3データへのアクセス時のForbiddenエラー](https://kb.databricks.com/security/forbidden-access-to-s3-data)を参照してください。
{% endtab %}
{% endtabs %}

## CDI統合のメールアラート設定を更新するにはどうすればよいですか？ {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

各統合には独自の通知設定があります。CDIページに移動し、更新したい統合名を選択します。**通知設定**セクションで、選択した統合に関するアラートの受信方法を更新できます。

## 「Incorrect Integration Object」エラーが表示されるのはなぜですか？ {#why-am-i-seeing-an-incorrect-integration-object-error}

このエラーは、CDI統合の通知設定を更新しようとした際に、2つ以上のワークスペースが同じクラウドストレージバケットまたはフォルダーを指す統合を持っている場合に発生します。各クラウドストレージの場所は、一度に1つの統合でのみ使用できます。

これを解決するには：

1. 同じストレージの場所を使用しているCDI統合が他のどのワークスペースにあるかを特定します。
2. 他のワークスペースで競合している統合を削除または再設定します。
3. 競合を解消した後、通知設定を更新できます。

エラーが表示されなくなり、通知設定を正常に更新できるようになります。問題が解決しない場合は、[サポートチケットを送信]({{site.baseurl}}/user_guide/administer/personal/braze_support)してください。

## 将来の`UPDATED_AT`が統合で同期された場合はどうなりますか？ {#what-happens-if-a-future-updated_at-gets-synced-with-an-integration}

CDIは`UPDATED_AT`を使用して、どのデータが新しいかを判断します。将来の`UPDATED_AT`が同期された後、その将来の日時より前のデータは処理されません。これを修正するには、以下の手順を実行してください。

1. `UPDATED_AT`を修正します。
2. Brazeと既に同期された古いデータを削除します。
3. そのテーブルを再度処理するための新しい統合を作成します。

## 「同期された行数」がデータウェアハウスの数と一致しないのはなぜですか？ {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDIは`UPDATED_AT`を使用して、同期中にどのレコードを取得するかを決定します。その仕組みについては[こちらの図解]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion#how-it-works)をご覧ください。同期実行の開始時に、CDIはデータウェアハウスにクエリを実行し、以前に処理された`UPDATED_AT`の値よりも後の`UPDATED_AT`を持つすべてのレコードを取得します。新しい行が同じタイムスタンプを共有している場合、境界タイムスタンプにあるレコードも再同期される場合があります。クエリが実行された時点で取得されたレコードはすべてBrazeに同期されます。レコードが同期されない一般的なケースは以下のとおりです。

- すでに処理済みの`UPDATED_AT`値を持つレコードをテーブルに追加している場合。
- 同期で処理された後にレコードの値を更新しているが、`UPDATED_AT`を変更していない場合。
- 同期の進行中にレコードを追加または更新している場合。CDIクエリの実行タイミングによっては、レコードが取得されない競合が発生する可能性があります。

{% alert tip %}
今後これらの動作を回避するため、単調増加する`UPDATED_AT`値を使用し、スケジュールされた同期実行中にテーブルを更新しないことをお勧めします。
{% endalert %}

## 大規模なCDIインポートでは、`UPDATED_AT` の値がほぼ一意である必要がありますか？ {#do-i-need-mostly-distinct-updated_at-values-for-large-cdi-imports}

はい。大量のデータ（たとえば約1,000万行を超える場合）を処理する際は、ソースデータの `UPDATED_AT` 値がほぼ一意であることを確認してください。同じタイムスタンプを共有する行が多すぎると、CDIが後続の実行で境界タイムスタンプの行を再選択する可能性が高くなります。これにより、重複同期やデータポイントの消費が増加する可能性があります。

CDIの境界動作の詳細については、[重複タイムスタンプを持つ行の再同期を回避する]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。

### これらのSQLチェックはどこで実行しますか？ {#where-do-i-run-these-sql-checks}

CDI統合で使用しているものと同じテーブルまたはビューに対して、データウェアハウスのSQLエディターで直接チェックを実行してください。

- Snowflake: **Projects** > **Worksheets**（詳細については、[Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs)を参照してください）
- Redshift: Query Editor v2（詳細については、[Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)を参照してください）
- BigQuery: BigQuery Studio SQLワークスペース（詳細については、[BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction)を参照してください）
- Databricks: SQLエディター（SQLウェアハウス）（詳細については、[Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/)を参照してください）
- Fabric: SQLクエリエディター

大規模な同期を有効化またはスケールする前に、以下のプロセスを使用してください。

1. 検証したいCDIソーステーブルまたはビューと同期ウィンドウを特定します。
2. データウェアハウスのSQLエディターを開き、CDIが使用しているものと同じデータベースおよびスキーマを選択し、ソーステーブルまたはビューへの読み取りアクセス権を持つロールを使用します。
3. 一意のタイムスタンプ数カウントクエリを実行し、そのウィンドウ内に存在する `UPDATED_AT` の一意の値の数を測定します。
4. `UPDATED_AT` でグループ化して行数をカウントするクエリを実行し、異常に多い行数を持つタイムスタンプを特定します。
5. 同一のタイムスタンプを共有する行が多い場合は、連続するバッチがより新しい `UPDATED_AT` 値を使用するようにインジェストプロセスを調整するか、タイムスタンプの精度を上げて行がより分散するようにします。
6. 集中が軽減されるまで両方のクエリを再実行し、その後同期を開始またはスケールします。
7. 開始後、**CDI** > **Sync Log** で境界タイムスタンプにおける予期しない再同期量を監視します。

データウェアハウスで以下のようなチェックを使用してください。

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

データウェアハウスが `LIMIT` をサポートしていない場合（たとえばFabric）、`TOP` などの同等の構文を使用してください。

## 少数の行のCDI同期でも数分かかるのはなぜですか？ {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

CDI同期には、行の処理が始まる前に固定の起動期間があります。この起動時間は同期サイズに関係なくほぼ同じであるため、少数の行の同期でも数分かかることがあり、1分あたりの行数で見ると遅く感じられる場合があります。同期の合計時間は、ソースクエリの複雑さ、データの形状、およびデータウェアハウスの利用可能な容量に依存します。詳細については、[データウェアハウス統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照してください。

## 同期中に複数のレコードが同じIDを共有している場合、順序は保持されますか？ {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

処理順序は100%予測可能ではありません。たとえば、同期中にテーブルに同じ`EXTERNAL_ID`を持つ複数の行がある場合、最終的なプロファイルにどの値が反映されるかを保証することはできません。同じ`EXTERNAL_ID`に対してペイロード列で異なる属性を更新している場合、同期が完了した時点ですべての変更が反映されます。

## CDI同期から新しいユーザーが作成されないのはなぜですか？ {#why-are-new-users-not-being-created-from-my-cdi-sync}

CDI統合で**既存ユーザーのみ更新**オプションが有効になっている場合、Brazeに既に存在するユーザーのみが更新され、新しいユーザーは作成されません。つまり、同期テーブルの行が既存のBrazeユーザーと一致しない`EXTERNAL_ID`を参照している場合、その行はスキップされます。

CDIを通じて新しいユーザーを作成するには、統合設定で**既存ユーザーのみ更新**トグルをオフにしてください。**データ設定** > **Cloud Data Ingestion**に移動し、統合を選択します。

## CDIのセキュリティ対策について {#what-are-the-security-measures-for-cdi}

### Braze側の対策 {#our-measures}

Brazeでは、CDIに関して以下の対策を実施しています。

- すべての認証情報はデータベース内で暗号化されており、認証されたアクセス権を持つ特定の従業員のみがアクセスできます。
- 顧客のデータウェアハウスへのデータ転送には暗号化された接続を使用しています。
- Braze APIエンドポイントへのリクエストには、お客様にも推奨しているものと同じAPIキーおよびTLS接続を使用しています。
- ライブラリを定期的に更新し、セキュリティパッチを適用しています。

### お客様側の対策 {#your-measures}

お客様側では、以下のセキュリティ対策を設定することを推奨します。

- 認証情報のアクセスを、CDIの運用に必要な最小限の範囲に制限してください。これは、特定のテーブルやビューに対してselect（およびcount）を実行できる必要があるためです。
- テーブルにアクセスできるIPを、公式に公開されている[Braze IP]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)に制限してください。