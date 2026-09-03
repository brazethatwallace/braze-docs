---
nav_title: データ取り込みオプションの比較
article_title: 永続型およびゼロコピー型データ取り込みオプションの比較
page_order: 1
page_type: reference
description: "Cloud Data Ingestion標準同期、CDIセグメント、CDIキャンバストリガー、/users/track APIを比較して、ウェアハウスやアプリケーションのデータをBrazeプロファイル、セグメント、キャンバスに届ける方法を選択します。"
---

# 永続型およびゼロコピー型データ取り込みオプションの比較 {#compare-persistent-and-zero-copy-data-ingestion-options}

> 取り込みパイプラインを設計する前に、ウェアハウスやアプリケーションからのデータをBrazeにどのように届けるか（ユーザープロファイルにコピーするか、セグメンテーションのためにその場でクエリするか、キャンバスに一時的に渡すか）を選択します。

## この例について {#about-this-example}

MovieCanonは架空の映画ストリーミングサービスです。顧客データ、チケットデータ、視聴データをウェアハウスに集約しています。データチームは、3つの一般的なニーズに対応するために、Brazeへのデータ供給方法を決定する必要があります。

- **プロファイルデータ:** Brazeユーザープロファイルに永続的に保持されるロイヤルティティア、LTV、ジャンルやフォーマットの嗜好属性。
- **オーディエンス構築:** すべてのカラムをBrazeにコピーせず、ウェアハウステーブルからSQLで定義するセグメント。
- **トリガーメッセージング:** プロファイルに永続化する必要のない行単位のパーソナライゼーションと共にキャンバスにエントリするウェアハウス行。

Brazeは4つの主要な取り込みパスを提供しています。標準Cloud Data Ingestion（CDI）同期と[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) APIはどちらもプロファイルにデータを永続化します。CDIセグメント（Connected Sources）とCDIキャンバストリガーはゼロコピーオプションで、ウェアハウスデータはウェアハウスに残り、Brazeユーザープロファイルには書き込まれません。

アーキテクチャの計画、スループットの見積もり、または開発チームやマーケティングチームへのトレードオフの説明を行う際にこの比較を活用してください。各オプションの統合設定ガイドの代わりにはなりません。

## 考慮事項 {#considerations}

- Cloud Data Ingestionは包括的な機能です。標準CDI同期はBrazeプロファイルにデータをコピーします（`/users/track`と同様）。CDIセグメントとCDIキャンバストリガーはウェアハウスデータをその場に保持し、Brazeユーザープロファイルには書き込みません。
- CDI定期同期は15分ごとから月1回まで実行できます。15分より高い頻度が必要な場合は、カスタマーサクセスマネージャーに連絡するか、REST API取り込みを使用してください。[Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を参照してください。
- CDIキャンバストリガーは、そのエンドポイントへの他のトラフィックと[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) REST APIレート制限を共有します。`/users/track`には独自の制限とバッチルールがあります。デフォルトの制限は引き上げ可能です。**設定** > **APIと識別子** > **APIの制限**に移動し、[APIレート制限]({{site.baseurl}}/api/api_limits)を参照してください。
- Connected SourcesとCDIセグメントエクステンションはウェアハウスでクエリを実行します。ウェアハウスのコンピューティングコストが発生しますが、Brazeはそれらのクエリに対してデータポイントを記録しません。[Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)を参照してください。

## 設定 {#setup}

### ステップ1: ユースケースを取り込みパスにマッピングする {#step-1-map-your-use-case-to-an-ingestion-path}

目標を推奨される取り込みパスと、そのパスがBrazeプロファイルに書き込むかどうかに対応付けます。

| 目標 | 推奨パス | プロファイルへの書き込み |
| --- | --- | --- |
| ウェアハウスから属性、イベント、購入、またはカタログアイテムを永続化する | 標準CDI同期 | あり（データはBrazeプロファイルまたはカタログにコピーされます） |
| ソーステーブルをBrazeにコピーせずにウェアハウスSQLからオーディエンスを構築する | CDIセグメント（Connected Sources） | なし（メンバーシップのみ） |
| プロファイルに永続化すべきでないウェアハウス行コンテキストでユーザーをキャンバスにエントリさせる | CDIキャンバストリガー | なし（一時的なキャンバスコンテキストプロパティ） |
| アプリ、サーバー、またはストリーミングパイプラインからほぼリアルタイムでデータをプッシュする | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)（またはSDK） | あり（データはプロファイルに永続化されます） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユースケースを取り込みパスにマッピングする" }

### ステップ2: 永続性、レイテンシー、スループットを比較する {#step-2-compare-persistence-latency-and-throughput}

各パスがデータレジデンシー、レイテンシー、スループット、ユーザー作成をどのように処理するか比較します。

| ディメンション | 標準CDI同期 | CDIセグメント | CDIキャンバストリガー | `/users/track` |
| --- | --- | --- | --- | --- |
| 動作内容 | ウェアハウステーブルのスケジュール読み取り。属性、イベント、購入、ユーザー削除、またはカタログを書き込みます | Brazeがウェアハウスにクエリを実行しSQLセグメントエクステンションを作成します | ウェアハウス行がキャンバスコンテキストプロパティとして行コンテキストを持つキャンバスエントリをトリガーします | アプリ、サーバー、またはストリーミングパイプラインが属性、イベント、購入をプロファイルに書き込みます |
| データレジデンシー | Brazeプロファイルにコピーおよび永続化されます | ウェアハウスに残ります。プロファイルには何も書き込まれません | キャンバスコンテキストプロパティは一時的で、プロファイルには永続化されません | Brazeプロファイルにコピーおよび永続化されます |
| 一般的なレイテンシー | リアルタイムではありません。最小15分の同期頻度（ウェアハウスの鮮度も影響します） | リアルタイムではありません。セグメントエクステンションのスケジュールに基づいてリフレッシュされます（ウェアハウスの変更ごとにメンバーシップは更新されません） | リアルタイムではありません。同期スケジュールに制限されます（最小15分） | ほぼリアルタイム（非同期処理） |
| スループットの注意事項 | 同期ごとに完全なクエリ結果。Brazeが内部的に`/users/track`、`/users/delete`、またはCatalogエンドポイントにバッチ処理します | Connected Sourceごとにクエリ実行時間上限60分。リクエストあたりのオブジェクト上限なし | `/canvas/trigger/send`のレート制限を共有。同期実行あたり約375万キャンバスエントリ | リクエストあたり最大75オブジェクト（合計）。[APIレート制限]({{site.baseurl}}/api/api_limits)を参照してください |
| バッチサイズ | CDI側のウェアハウス読み取りにはオブジェクトあたりの上限なし | 該当なし（クエリ出力がメンバーシップを定義します） | 同期実行ごとにウェアハウス行1行につき1キャンバスエントリ | リクエストあたり75属性、イベント、購入の合計（デフォルト） |
| ユーザー作成 | あり（既存のみ更新が設定されていない場合） | なし（クエリ結果内の不明なユーザーは無視されます） | なし（既存のBrazeユーザーのみ） | あり（`_update_existing_only`がtrueでない場合） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="永続性、レイテンシー、スループットを比較する" }

### ステップ3: スキーマと識別子の要件を比較する {#step-3-compare-schema-and-identifier-requirements}

各パスの必須カラムとサポートされる識別子を比較します。標準CDI同期ごとに1つのデータタイプを設定してください（例: 1つの統合で属性、別の統合でイベント）。

| ディメンション | 標準CDI同期 | CDIセグメント | CDIキャンバストリガー | `/users/track` |
| --- | --- | --- | --- | --- |
| 必須カラム／形式 | ユーザー識別子 + `UPDATED_AT` + `PAYLOAD`（JSON）（行ごと） | SQLは`external_user_id`のみを出力する必要があります | 識別子 + `UPDATED_AT` + `PROPERTIES`（JSON。空の場合は`{}`を使用） | 標準`/users/track`リクエストボディ |
| サポートされる識別子 | `external_id`、ユーザーエイリアス、`braze_id`、メール、または電話番号 | `external_user_id`のみ（文字列） | `external_id`またはユーザーエイリアスのみ | `external_id`、ユーザーエイリアス、`braze_id`、メール、または電話番号 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="スキーマと識別子の要件を比較する" }

### ステップ4: 選択したパスを実装する {#step-4-implement-the-path-you-selected}

- **標準CDI同期:** ウェアハウスのテーブルまたはビューを作成し、[Cloud Data Ingestion統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)および[テーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)に従ってください。
- **CDIセグメント:** [Connected Source]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)を追加し、[CDIセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)を作成します。
- **CDIキャンバストリガー:** `PROPERTIES`を含むソーステーブルを設定し、宛先キャンバスを構築して起動した後、[CDIを使用したゼロコピーパーソナライゼーション]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)に従って同期を作成します。
- **`/users/track`:** アプリケーションまたはミドルウェアからリクエストを送信します。[POST: ユーザーの作成と更新]({{site.baseurl}}/api/endpoints/user_data/post_user_track)に従ってペイロードをフォーマットしてください。

MovieCanonの一般的なパターンは、夜間のプロファイルエンリッチメントには標準CDI同期、ウェアハウスのみのオーディエンスルールにはCDIセグメント、行レベルのコンテキストを持つチケットステータスや視聴ジャーニーにはキャンバストリガー、リアルタイムのアプリイベントには`/users/track`を使用するというものです。

## 関連記事 {#related-articles}

- [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)
- [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)
- [CDIを使用したゼロコピーパーソナライゼーション]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)
- [CDIセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)
- [Cloud Data Ingestionのテーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)
- [POST: ユーザーの作成と更新]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [APIレート制限]({{site.baseurl}}/api/api_limits)