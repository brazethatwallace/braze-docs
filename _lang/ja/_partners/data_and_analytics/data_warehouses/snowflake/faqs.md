---
nav_title: FAQ
article_title: Snowflake データ共有に関するよくある質問
page_order: 50
page_type: FAQ
description: "この記事では、Snowflake データ共有に関するよくある質問に回答します。"

---

# よくある質問 {#frequently-asked-questions}

## Snowflake データ共有を介して PII データを難読化することは可能ですか？ {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
いいえ、現時点ではサポートされていません。

## 同じリージョンのデータ共有が必要ですか、それともクロスリージョンのデータ共有が必要ですか？ {#do-i-need-data-share-for-the-same-region-or-cross-region}
以下のシナリオでは、同じリージョンのデータ共有を使用します。
- Snowflakeアカウントが US-EAST-1（AWS）にあり、Brazeダッシュボードのリージョンが米国にある場合。
- Snowflakeリージョンが EU-CENTRAL-1（AWS）にあり、Brazeダッシュボードのリージョンが EU にある場合。
- Snowflakeリージョンが AP-Northeast-1（AWS）にあり、Brazeダッシュボードのリージョンが日本にある場合。
- Snowflakeリージョンが AP-Southeast-2（AWS）にあり、Brazeダッシュボードのリージョンがオーストラリアにある場合。
- Snowflakeリージョンが AP-Southeast-3（AWS）にあり、Brazeダッシュボードのリージョンがインドネシアにある場合。

それ以外の場合は、クロスリージョンのデータ共有を使用します。

## 新しい Snowflake アカウントに切り替える場合、データ共有はどうすればよいですか？ {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
古い Snowflake アカウントに関連付けられている古いデータ共有を削除してから、新しいアカウント用に新しい共有を作成できます。すべての履歴データは新しい共有で利用可能になります。

## データ共有にデータが表示されないのはなぜですか？ {#why-dont-i-see-data-in-my-data-share}
データ共有の作成時に間違った Snowflake アカウント ID を使用した可能性があります。データ共有ダッシュボードのアカウント ID は、Snowflake アカウントの `CURRENT_ACCOUNT()` の出力と一致している必要があります。

共有がクロスリージョンの場合、データがすぐに利用可能にならないことがあります。データ量によっては、リージョンへのデータ同期に数時間かかる場合があります。

## データ共有の作成時に HIPAA コンプライアンスエラーが発生するのはなぜですか？ {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

指定されたアカウントがHIPAAに準拠していないか、[Snowflake Editions](https://docs.snowflake.com/en/user-guide/intro-editions) が Business Critical より低いエディションです。データ共有でHIPAAに準拠するには、Snowflake アカウントを Business Critical Edition にアップグレードする必要があります。アカウントのアップグレードに関する詳細については、Snowflake サポートにお問い合わせください。

## データ共有を削除した後に再作成できないのはなぜですか？ {#why-cant-i-recreate-a-data-share-after-deleting-one}

システムが以前のデータ共有の削除をまだ処理している可能性があります。プロビジョニング解除プロセスが完了するまで数分待ってから、新しいデータ共有の作成を再試行してください。

## 同じ Snowflake アカウントに複数のワークスペースがデータを共有している場合、`CREATE DATABASE` を何回実行する必要がありますか？ {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` は一度だけ実行する必要があります。異なるBrazeワークスペースからの複数のデータ共有が同じ Snowflake アカウントに共有されると、それらは自動的に同じ共有に統合されます。最初のデータベースを作成した後、追加のワークスペースからのデータは、追加の共有リクエストやデータベース作成ステップを必要とせずに、既存のデータベースに自動的に追加されます。

たとえば、ワークスペース A から Snowflake アカウント 123 へのデータ共有を作成した場合、共有リクエストを受け入れてデータベースを作成します。後でワークスペース B から同じ Snowflake アカウント 123 にデータ共有を作成した場合、新しい共有リクエストは送信されず、データは既存の共有に即座に追加され、以前に作成したデータベースで利用可能になります。

## 複数のワークスペースがある場合、1つのデータベースにすべてのワークスペースのデータが含まれますか？ {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

はい。複数のBrazeワークスペースから同じ Snowflake アカウントにデータを共有すると、すべてのデータが1つの共有にまとめられ、同じデータベースで利用可能になります。ワークスペースを区別するには、`app_group_id` でフィルターできます。

ベストプラクティスとして、将来に備えてクエリには常に `app_group_id` でフィルターをかけてください。これにより、将来ワークスペースを追加した場合でも、ダッシュボードやレポートの正確性が保たれます。このフィルターがないと、新しく追加されたワークスペースからのデータが指標に予期せず含まれてしまう可能性があります。

## Snowflake で複数のワークスペースからのデータを管理するための推奨アプローチは何ですか？ {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

すべてのBrazeデータを同じデータベースに送り、`app_group_id` でフィルターしてワークスペースを区別します。このアプローチにより、データ管理が簡素化され、組織全体で一貫性のあるレポートが確保されます。

## 複数のワークスペースに必要な Snowflake Data Share Connectorの数はいくつですか？ {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

必要なコネクターの数は、特定の設定とエンタイトルメントによって異なります。お客様のユースケースに適したエンタイトルメントについては、Brazeアカウントチームにお問い合わせください。

## 同じ Snowflake アカウント内で異なるワークスペースのデータを分離するにはどのようなオプションがありますか？ {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

各データ行がどのワークスペースに属するかを識別する `app_group_id` カラムを使用して、論理的に分離できます。最も一般的なアプローチは以下のとおりです。

- **ビュー（推奨）：** ワークスペースごとに `app_group_id` でフィルターしたビューを作成します。データを複製せずに、各チームやユースケースにワークスペースデータのクリーンでスコープされたビューを提供できます。
- **ローカルテーブルコピー：** `app_group_id` でフィルターした別々のテーブルにデータをコピーします。データが複製されるため、一般的にはビューアプローチが推奨されます。
- **行アクセスポリシーとロール：** Snowflake ネイティブの行アクセスポリシーとロールを組み合わせて、各ロールがクエリできる行を制限します。データを単一のテーブルに保持しながら、クエリ時にアクセスを制御できます。

これらはSnowflake アカウント内で設定します。

## 異なるワークスペースのデータを分離するために、別の Snowflake アカウントを使用できますか？ {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

はい。ワークスペース A がアカウント X に共有し、ワークスペース B がアカウント Y に共有する場合、各アカウントは個別のデータを持つ独立した共有を受け取ります。ただし、ほとんどの組織ではすべてのビジネスデータに単一の Snowflake アカウントを使用しています。そのため、このアプローチは運用上のオーバーヘッドが増える可能性があります。前のセクションで説明した論理的な分離アプローチと比較して、このトレードオフを検討してから選択してください。

## ワークスペースデータの分離は Snowflake データ共有でサポートされているユースケースですか？ {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

はい、前のセクションで説明した論理的な分離アプローチを通じてサポートされています。Brazeはワークスペースごとに個別の共有を作成しないため、ビュー、行アクセスポリシー、または個別のアカウントを使用して Snowflake レベルで分離を管理します。