---
nav_title: FAQ
article_title: Snowflake データ共有に関するよくある質問
page_order: 50
page_type: FAQ
description: "この記事では、Snowflake データ共有に関するよくある質問に回答します。"

---

# よくある質問 {#frequently-asked-questions}

## Snowflakeデータ共有を通じてPIIデータを難読化することは可能ですか？ {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
いいえ、現時点ではサポートされていません。

## 同一リージョンのデータ共有とクロスリージョンのデータ共有のどちらが必要ですか？ {#do-i-need-data-share-for-the-same-region-or-cross-region}
以下のシナリオでは、同一リージョンのデータ共有を使用してください。
- Snowflakeアカウントが US-EAST-1（AWS）にあり、Brazeダッシュボードのリージョンが US の場合。
- Snowflakeリージョンが EU-CENTRAL-1（AWS）にあり、Brazeダッシュボードのリージョンが EU の場合。
- Snowflakeリージョンが AP-Northeast-1（AWS）にあり、Brazeダッシュボードのリージョンが日本の場合。
- Snowflakeリージョンが AP-Southeast-2（AWS）にあり、Brazeダッシュボードのリージョンがオーストラリアの場合。
- Snowflakeリージョンが AP-Southeast-3（AWS）にあり、Brazeダッシュボードのリージョンがインドネシアの場合。

上記以外の場合は、クロスリージョンのデータ共有を使用してください。

## 新しいSnowflakeアカウントに切り替える際、データ共有はどうすればよいですか？ {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}

古いSnowflakeアカウントに関連付けられた古いデータ共有を削除し、新しいアカウント用に新しい共有を作成できます。すべての履歴データは新しい共有で利用可能になります。

## 新しいBrazeワークスペースにデータ共有を切り替えるとどうなりますか？ {#what-happens-if-i-switch-my-data-share-to-a-new-braze-workspace}

既存のデータ共有統合を別のBrazeワークスペースを使用するように再構成すると、Snowflakeでテーブルをクエリする際に次のエラーが表示されることがあります。

> Shared database is no longer available for use. It will need to be re-created if and when the publisher makes it available again.

この問題を解決するには、Snowflake内で共有をドロップして再作成する必要があります。

1. 以前の共有で作成されたデータベースをドロップします。
2. [統合手順]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake#step-2-create-the-database-in-snowflake)に従ってデータベースを再作成します。
3. 新しいデータベースに必要なアクセス権限を再付与します。
4. 古いデータベースを参照していたビューを再作成します（該当する場合）。

{% alert note %}
新しいSnowflakeインターフェイスでは、**Data Products** > **Private Sharing** > **Shared with you**でBrazeの共有を見つけることができます。
{% endalert %}

## データ共有にデータが表示されないのはなぜですか？ {#why-dont-i-see-data-in-my-data-share}
データ共有を作成する際に、誤ったSnowflakeアカウントIDを使用した可能性があります。データ共有ダッシュボードのアカウントIDは、Snowflakeアカウントの`CURRENT_ACCOUNT()`の出力と一致する必要があります。

共有がクロスリージョンの場合、データがすぐに利用できないことがあります。データ量によっては、お使いのリージョンにデータが同期されるまで数時間かかる場合があります。

## データ共有の作成時にHIPAAコンプライアンスエラーが表示されるのはなぜですか？ {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

指定されたアカウントがHIPAA準拠ではないか、Business Criticalより低い[Snowflakeエディション](https://docs.snowflake.com/en/user-guide/intro-editions)を使用しています。データ共有でHIPAA準拠にするには、SnowflakeアカウントをBusiness Critical Editionにアップグレードする必要があります。アカウントのアップグレードについては、Snowflakeサポートにお問い合わせください。

## 以前のデータ共有を削除した後、新しいデータ共有を再作成できないのはなぜですか？ {#why-cant-i-recreate-a-data-share-after-deleting-one}

以前のデータ共有の削除がまだ処理中である可能性があります。プロビジョニング解除プロセスが完了するまで数分待ってから、新しいデータ共有の作成を再度お試しください。

## 複数のワークスペースが同じSnowflakeアカウントにデータを共有している場合、`CREATE DATABASE` を何回実行する必要がありますか？ {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` の実行は1回だけで済みます。異なるBrazeワークスペースからの複数のデータ共有が同じSnowflakeアカウントに共有される場合、それらは自動的に同じ共有にまとめられます。最初のデータベースを作成した後、追加のワークスペースからのデータは、追加の共有リクエストやデータベース作成ステップを必要とせずに、既存のデータベースに自動的に追加されます。

たとえば、ワークスペースAからSnowflakeアカウント123へのデータ共有を作成した場合、共有リクエストを承認してデータベースを作成します。その後、ワークスペースBから同じSnowflakeアカウント123へのデータ共有を作成しても、新しい共有リクエストは送信されません。データは既存の共有に即座に追加され、以前作成したデータベースで利用可能になります。

## 複数のワークスペースがある場合、1つのデータベースにすべてのデータが含まれますか？ {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

はい。複数のBrazeワークスペースから同じSnowflakeアカウントにデータを共有すると、すべてのデータが1つの共有にまとめられ、同じデータベースで利用できます。`app_group_id`でフィルタリングすることで、ワークスペースを区別できます。

ベストプラクティスとして、将来に備えてクエリでは常に`app_group_id`でフィルタリングしてください。これにより、将来ワークスペースを追加した場合でも、ダッシュボードやレポートの正確性が維持されます。このフィルターがないと、新しく追加されたワークスペースのデータが予期せず指標に含まれる可能性があります。

## 複数のワークスペースのデータをSnowflakeで管理するための推奨アプローチは何ですか？ {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

すべてのBrazeデータを同じデータベースに送信し、`app_group_id` でフィルターしてワークスペースを区別します。このアプローチにより、データ管理が簡素化され、組織全体で一貫したレポートが確保されます。

## 複数のワークスペースに必要なSnowflakeデータ共有コネクターの数はいくつですか？ {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

必要なコネクターの数は、お客様の具体的な構成とエンタイトルメントによって異なります。お客様のユースケースに適したエンタイトルメントについて詳しくは、Brazeアカウントチームにお問い合わせください。

## 同じSnowflakeアカウント内の異なるワークスペースのデータを分離するにはどのような方法がありますか？ {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

`app_group_id`カラムを使用して論理的に分離できます。このカラムは、各データ行がどのワークスペースに属しているかを識別します。最も一般的なアプローチは以下のとおりです。

- **ビュー（推奨）：** `app_group_id`でフィルタリングしたビューをワークスペースごとに作成します。データを複製することなく、各チームやユースケースに対してクリーンでスコープされたワークスペースデータのビューを提供できます。
- **ローカルテーブルコピー：** `app_group_id`でフィルタリングしたデータを別々のテーブルにコピーします。この方法ではデータが複製されるため、一般的にはビューのアプローチが推奨されます。
- **行アクセスポリシーとロール：** Snowflakeネイティブの行アクセスポリシーとロールを組み合わせて、各ロールがクエリできる行を制限します。データを単一のテーブルに保持しながら、クエリ時にアクセスを制御できます。

これらの設定はSnowflakeアカウント内で行います。

## 異なるワークスペースのデータを分離するために、別々のSnowflakeアカウントを使用できますか？ {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

はい。ワークスペースAがアカウントXに共有し、ワークスペースBがアカウントYに共有する場合、各アカウントは個別のデータを持つ独立した共有を受け取ります。ただし、ほとんどの組織ではすべてのビジネスデータに単一のSnowflakeアカウントを使用しています。そのため、このアプローチは運用上のオーバーヘッドが増える可能性があります。前のセクションで説明した論理的な分離アプローチと比較して、このトレードオフを検討してから選択してください。

## ワークスペースのデータ分離は、Snowflakeデータ共有でサポートされるユースケースですか？ {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

はい、前のセクションで説明した論理的な分離アプローチを通じてサポートされます。Brazeはワークスペースごとに個別の共有を作成しないため、ビュー、行アクセスポリシー、または個別のアカウントを使用してSnowflakeレベルで分離を管理します。