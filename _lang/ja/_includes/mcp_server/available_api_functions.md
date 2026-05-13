# Braze MCPサーバー関数 {#braze-mcp-server-functions}

> Braze MCPサーバーは、特定のBraze REST APIエンドポイントに対応するAPI関数のセットを公開しています。ClaudeやCursorなどのMCPクライアントは、これらの関数を呼び出して非PIIデータの取得や、PIIを含まない書き込みアクションを実行できます。より一般的な情報については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件 {#prerequisites}

この機能を使用する前に、[Braze MCPサーバーのセットアップ]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}を完了する必要があります。

## 利用可能なBraze API関数 {#available-braze-api-functions}

MCPクライアントは、Braze MCPサーバーとやり取りするために以下のAPI関数を参照します。

### 一般関数 {#general-functions}

これらの関数は、MCPクライアントが利用可能なBraze API関数を検出し、実行するのに役立ちます。

| 関数 | 説明 |
|----------|-------------|
| `list_functions` | 利用可能なすべてのBraze API関数を、説明とパラメーターと共に一覧表示します。 |
| `call_function` | 指定されたパラメーターで特定の読み取り専用Braze API関数を呼び出します。 |
| `call_write_function` | 指定されたパラメーターで特定の書き込み可能なBraze API関数を呼び出します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="General functions" }

### Campaigns

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | メタデータ付きのCampaignリストをエクスポートします。 |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | 特定のCampaignに関する詳細情報を取得します。 |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Campaignの時系列分析データを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campaigns" }

### Canvases

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | メタデータ付きのCanvasリストをエクスポートします。 |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | 特定のCanvasに関する詳細情報を取得します。 |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Canvasのパフォーマンスに関するサマリー分析を取得します。 |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Canvasの時系列分析データを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvases" }

### カタログ {#catalogs}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | ワークスペース内のカタログのリストを返します。 |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | ページネーションをサポートして、複数のカタログアイテムとその内容を返します。 |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | 特定のカタログアイテムとその内容をIDで返します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Catalogs" }

### クラウドデータ取り込み {#cloud-data-ingestion}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | 既存のCDI統合のリストを返します。 |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | 指定されたCDI統合の過去の同期ステータスを返します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cloud Data Ingestion" }

### Content Blocks

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | 利用可能なコンテンツブロックを一覧表示します。 |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | コンテンツブロックに関する情報を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Blocks" }

### カスタム属性 {#custom-attributes}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | アプリ用に記録されたカスタム属性をエクスポートします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom Attributes" }

### イベント {#events}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | アプリ用に記録されたカスタムイベントのリストをエクスポートします。 |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | カスタムイベントの時系列データを取得します。 |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | ページネーション対応の詳細なイベントデータを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Events" }

### KPI {#kpis}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | 新規ユーザー数の日次推移。 |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | デイリーアクティブユーザーの時系列データ。 |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | 月間アクティブユーザーの時系列データ。 |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | アプリのアンインストール時系列データ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="KPIs" }

### メディアライブラリ {#media-library}

これはBraze MCPサーバーにおける唯一の書き込み関数です。使用するには、APIキーに `media_library.create` 権限が必要です。

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | Brazeメディアライブラリにアセットをアップロードします。公開アクセス可能なURL（`asset_url`）またはBase64エンコードされたファイル（`asset_file_base64`）のいずれかを指定できますが、両方を同時に指定することはできません。画像のサイズ上限は5 MBです。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Media Library" }

### メッセージ {#messages}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | 今後のスケジュール済みCampaignsとCanvasesを一覧表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages" }

### ユーザー設定センター {#preference-centers}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | 利用可能なユーザー設定センターを一覧表示します。 |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | 特定のユーザー設定センターの詳細（HTMLコンテンツやオプションを含む）を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Preference Centers" }

### 購入 {#purchases}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | 商品IDのページネーション付きリストをエクスポートします。 |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | 収益分析の時系列データ。 |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | 購入数量の時系列データ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Purchases" }

### Segments

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | 分析トラッキングステータス付きのSegmentリストをエクスポートします。 |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Segmentの時系列分析データ。 |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | 特定のSegmentに関する詳細情報。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segments" }

### 送信 {#sends}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | トラッキング対象Campaign送信の日次分析。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sends" }

### セッション {#sessions}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | アプリセッション数の時系列データ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sessions" }

### SDK認証キー {#sdk-authentication-keys}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | アプリのすべてのSDK認証キーを一覧表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SDK Authentication Keys" }

### サブスクリプション {#subscription}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | 特定のユーザーのサブスクリプショングループを一覧表示し、取得します。 |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | サブスクリプショングループ内のユーザーのサブスクリプション状態を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subscription" }

### テンプレート {#templates}

| 関数 | エンドポイント | 説明 |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | 利用可能なメールテンプレートを一覧表示します。 |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | メールテンプレートに関する情報を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Templates" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}