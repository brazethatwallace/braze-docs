---
nav_title: エクスポート
article_title: エクスポートエンドポイント
search_tag: Endpoint
page_order: 2
description: "このリファレンス記事では、Brazeのエクスポートエンドポイントについて、前提条件、エクスポートできるデータ、データの配信方法、およびエンドポイントの完全なリストを含めて説明します。"
page_type: reference
---

# エクスポートエンドポイント {#export-endpoints}

このエンドポイントコレクションを使用すると、KPI、アプリセッション、ユーザー、セグメント、キャンペーン、キャンバスに関するさまざまなレベルの詳細にアクセスしてエクスポートできます。パラメーターとリクエストボディを作成する際には、[Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)、[APIキー]({{site.baseurl}}/api/basics)、および[API識別子]({{site.baseurl}}/api/identifier_types)を確認してください。

## 前提条件 {#prerequisites}

始める前に、以下が揃っていることを確認してください。

| 要件 | 説明 |
| --- | --- |
| Braze REST APIキー | 呼び出す予定のエンドポイントに適切なエクスポート権限を持つREST APIキー。APIキーは特定のエンドポイントにスコープされ、作成後に権限を変更することはできません。詳細については、[REST APIキー]({{site.baseurl}}/api/basics#about-rest-api-keys)を参照してください。 |
| 関連する識別子 | エクスポートしたいデータの識別子（キャンペーンID、セグメントID、キャンバスIDなど）。これらはBrazeダッシュボードで確認できます。完全なリストについては、[API識別子タイプ]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| クラウドストレージの認証情報（任意） | 大規模なデータセットをエクスポートする場合は、[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)、[Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)、または[Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)バケットを接続して、エクスポートファイルをストレージに直接書き込むことができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% alert note %}
APIアクセス権を持たないマーケターやチームメンバーの場合は、組織内の開発者または管理者と連携してAPIキーと連携の設定を行ってください。
{% endalert %}

## エクスポートできるもの {#what-you-can-export}

以下の表は、エクスポートAPIで利用可能なデータカテゴリーをまとめたものです。

| カテゴリー | 含まれる内容 | APIリファレンス |
| --- | --- | --- |
| キャンペーン | パフォーマンス分析、キャンペーンの詳細、キャンペーン一覧、送信分析 | [キャンペーンエンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| キャンバス | データ系列分析、分析サマリー、キャンバスの詳細、キャンバス一覧 | [キャンバスエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| セグメント | セグメント一覧、セグメント分析、セグメントの詳細 | [セグメントエンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| ユーザーデータ | 識別子またはセグメントによる完全なユーザープロファイル、グローバルコントロールグループによるユーザー | [ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| KPIs | デイリーアクティブユーザー、マンスリーアクティブユーザー、日別新規ユーザー、日付別アンインストール数 | [KPIエンドポイント]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| セッション | アプリセッションの時系列データ | [セッションエンドポイント]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| カスタムイベント | イベント名、イベント一覧、期間ごとのイベント分析 | [カスタムイベントエンドポイント]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| カスタム属性 | 属性名 | [カスタム属性エンドポイント]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| 購入 | 期間ごとの収益データ、商品ID一覧、購入回数 | [購入エンドポイント]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="エクスポートできるもの" }

## エクスポートデータの配信方法 {#how-export-data-is-delivered}

APIエクスポートは、ダッシュボードからダウンロードするCSVファイルとは異なり、JSON形式でデータを返します。配信方法は、クラウドストレージが接続されているかどうかによって異なります。

- **クラウドストレージなしの場合:** BrazeはエクスポートファイルをBraze独自のS3バケットに書き込み、APIレスポンスに一時的なダウンロードURLを含めます。このURLは4時間後に期限切れになります。エクスポートはJSONファイルを含む圧縮アーカイブ（`output_format` パラメーターに応じてZIPまたはGZIP）としてパッケージ化されます。JSONファイルの各行は1つのデータオブジェクトを表します。
- **クラウドストレージが接続されている場合:** Brazeはエクスポートファイルを設定済みのバケットに直接書き込みます。APIレスポンスにダウンロードURLは含まれません。ファイルは独自の保持ポリシーに従い、大規模なエクスポートでは通常より信頼性が高くなります。

{% alert tip %}
「クラウドストレージ」とは、お客様独自のストレージバケット（例：Amazon S3、Microsoft Azure Blob Storage、Google Cloud Storage）を指します。**パートナー連携** > **テクノロジーパートナー**でバケットを接続すると、Brazeがエクスポートファイルを直接書き込めるようになります。
{% endalert %}

エクスポートの配信とトラブルシューティングの詳細については、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)を参照してください。

## エクスポートエンドポイント

以下の表は、利用可能なすべてのエクスポートAPIの一覧です。

| カテゴリ | メソッド | エンドポイント |
| --- | --- | --- |
| キャンペーン | GET | [キャンペーン分析]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| キャンペーン | GET | [キャンペーンの詳細]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) |
| キャンペーン | GET | [キャンペーン一覧]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) |
| キャンペーン | GET | [送信分析]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) |
| キャンバス | GET | [キャンバスデータシリーズ分析]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| キャンバス | GET | [キャンバス分析サマリー]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) |
| キャンバス | GET | [キャンバスの詳細]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) |
| キャンバス | GET | [キャンバス一覧]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) |
| カスタムイベント | GET | [カスタムイベント]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| カスタムイベント | GET | [カスタムイベント一覧]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) |
| カスタムイベント | GET | [カスタムイベント分析]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) |
| カスタム属性 | GET | [カスタム属性]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| KPIs | GET | [日別新規ユーザーのKPIs]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) |
| KPIs | GET | [日別アクティブユーザーのKPIs]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| KPIs | GET | [過去30日間の月間アクティブユーザーのKPIs]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) |
| KPIs | GET | [日別アンインストールのKPIs]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) |
| 購入 | GET | [商品ID一覧]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) |
| 購入 | GET | [購入数]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) |
| 購入 | GET | [時間別収益データ]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
| セグメント | GET | [セグメント一覧]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| セグメント | GET | [セグメント分析]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) |
| セグメント | GET | [セグメントの詳細]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) |
| セッション | GET | [アプリセッション時系列データ]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| ユーザーデータ | POST | [識別子によるユーザーデータ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| ユーザーデータ | POST | [セグメントによるユーザーデータ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
| ユーザーデータ | POST | [グローバルコントロールグループによるユーザーデータ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="エクスポートエンドポイント" }

## 関連記事 {#related-articles}

ダッシュボードからの単発エクスポートについては、以下の記事を参照してください。

- [キャンペーンデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data)
- [キャンバスデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)
- [セグメントデータのCSVエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)