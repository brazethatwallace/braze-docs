---
nav_title: エクスポート
article_title: エクスポートエンドポイント
search_tag: Endpoint
page_order: 2
description: "このリファレンス記事では、Brazeのエクスポートエンドポイントについて、前提条件、エクスポートできるデータ、データの配信方法、およびエンドポイントの完全なリストを含めて説明します。"
page_type: reference
---

# エクスポートエンドポイント {#export-endpoints}

このエンドポイントコレクションを使用すると、KPI、アプリセッション、ユーザー、セグメント、キャンペーン、キャンバスに関するさまざまなレベルの詳細にアクセスしてエクスポートできます。パラメーターとリクエストボディを作成する際には、[Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)、[APIキー]({{site.baseurl}}/api/api_key/)、および[API識別子]({{site.baseurl}}/api/identifier_types/)を確認してください。

## 前提条件 {#prerequisites}

開始する前に、以下を準備してください。

| 要件 | 説明 |
| --- | --- |
| Braze REST APIキー | 呼び出す予定のエンドポイントに対する適切なエクスポート権限を持つREST APIキー。APIキーは特定のエンドポイントにスコープされ、作成後に権限を変更することはできません。詳細については、[REST APIキー]({{site.baseurl}}/api/basics/#about-rest-api-keys)を参照してください。 |
| 関連する識別子 | エクスポートしたいデータの識別子（キャンペーン ID、セグメント ID、キャンバス IDなど）。これらはBrazeダッシュボードで確認できます。完全なリストについては、[API識別子タイプ]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| クラウドストレージの認証情報（オプション） | 大規模なデータセットをエクスポートする場合は、[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)、[Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)、または[Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)バケットを接続して、エクスポートファイルをストレージに直接書き込むことができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert note %}
APIアクセス権を持たないマーケターやチームメンバーの場合は、組織内の開発者または管理者と連携してAPIキーと統合を設定してください。
{% endalert %}

## エクスポートできるデータ {#what-you-can-export}

以下の表は、エクスポートAPIで利用可能なデータカテゴリをまとめたものです。

| カテゴリ | 含まれるデータ | APIリファレンス |
| --- | --- | --- |
| キャンペーン | パフォーマンス分析、キャンペーンの詳細、キャンペーンリスト、送信分析 | [キャンペーンエンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) |
| キャンバス | データシリーズ分析、分析サマリー、キャンバスの詳細、キャンバスリスト | [キャンバスエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) |
| セグメント | セグメントリスト、セグメント分析、セグメントの詳細 | [セグメントエンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) |
| ユーザーデータ | 識別子またはセグメント別の完全なユーザープロファイル、グローバルコントロールグループ別のユーザー | [ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |
| KPI | デイリーアクティブユーザー、月間アクティブユーザー、日次新規ユーザー、日付別アンインストール | [KPIエンドポイント]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |
| セッション | アプリセッションの時系列データ | [セッションエンドポイント]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) |
| カスタムイベント | イベント名、イベントリスト、時系列のイベント分析 | [カスタムイベントエンドポイント]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) |
| カスタム属性 | 属性名 | [カスタム属性エンドポイント]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) |
| 購入 | 時間別収益データ、製品IDリスト、購入数 | [購入エンドポイント]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="What you can export" }

## エクスポートデータの配信方法 {#how-export-data-is-delivered}

APIエクスポートは、ダッシュボードからダウンロードするCSVファイルとは異なり、JSON形式でデータを返します。配信方法は、クラウドストレージが接続されているかどうかによって異なります。

- **クラウドストレージなしの場合：** BrazeはエクスポートファイルをBraze独自のS3バケットに書き込み、APIレスポンスに一時的なダウンロードURLを含めます。このURLは4時間後に期限切れになり、エクスポートはJSONファイルを含む圧縮アーカイブ（`output_format`パラメーターに応じてZIPまたはGZIP）としてパッケージされます。JSONファイルの各行は1つのデータオブジェクトを表します。
- **クラウドストレージ接続済みの場合：** Brazeはエクスポートファイルを設定済みのバケットに直接書き込みます。APIレスポンスにはダウンロードURLは含まれません。ファイルは独自の保持ポリシーに従い、大規模なエクスポートではより信頼性が高くなります。

{% alert tip %}
「クラウドストレージ」とは、お客様独自のストレージバケット（Amazon S3、Microsoft Azure Blob Storage、Google Cloud Storageなど）を指します。**パートナー連携** > **テクノロジーパートナー**でバケットを接続すると、Brazeがエクスポートファイルを直接書き込めるようになります。
{% endalert %}

エクスポートの配信とトラブルシューティングの詳細については、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)を参照してください。

## エクスポートエンドポイント一覧

以下の表は、利用可能なすべてのエクスポートAPIを一覧にしたものです。

| カテゴリ | メソッド | エンドポイント |
| --- | --- | --- |
| キャンペーン | GET | [キャンペーン分析]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) |
| キャンペーン | GET | [キャンペーンの詳細]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) |
| キャンペーン | GET | [キャンペーンリスト]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) |
| キャンペーン | GET | [送信分析]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) |
| キャンバス | GET | [キャンバスデータシリーズ分析]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) |
| キャンバス | GET | [キャンバス分析サマリー]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) |
| キャンバス | GET | [キャンバスの詳細]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) |
| キャンバス | GET | [キャンバスリスト]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |
| カスタムイベント | GET | [カスタムイベント]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) |
| カスタムイベント | GET | [カスタムイベントリスト]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) |
| カスタムイベント | GET | [カスタムイベント分析]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) |
| カスタム属性 | GET | [カスタム属性]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) |
| KPI | GET | [日付別の日次新規ユーザーKPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) |
| KPI | GET | [日付別のデイリーアクティブユーザーKPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |
| KPI | GET | [過去30日間の月間アクティブユーザーKPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) |
| KPI | GET | [日付別のアンインストールKPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) |
| 購入 | GET | [製品IDリスト]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) |
| 購入 | GET | [購入数]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) |
| 購入 | GET | [時間別収益データ]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) |
| セグメント | GET | [セグメントリスト]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) |
| セグメント | GET | [セグメント分析]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) |
| セグメント | GET | [セグメントの詳細]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) |
| セッション | GET | [アプリセッションの時系列データ]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) |
| ユーザーデータ | POST | [識別子によるユーザーデータ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |
| ユーザーデータ | POST | [セグメントによるユーザーデータ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |
| ユーザーデータ | POST | [グローバルコントロールグループによるユーザーデータ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Export endpoints" }

## 関連記事 {#related-articles}

ダッシュボードからの単発エクスポートについては、以下の記事を参照してください。

- [キャンペーンデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data/)
- [キャンバスデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/)
- [セグメントデータをCSVにエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/)