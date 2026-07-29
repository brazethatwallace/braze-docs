# Braze MCPサーバー関数 {#braze-mcp-server-functions}

> Braze MCPサーバーは、特定のBraze REST APIエンドポイントに対応する読み取りおよび書き込みツールを公開しています。詳細については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件 {#prerequisites}

この機能を使用する前に、[Braze MCPサーバーのセットアップ]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}を完了する必要があります。

## 利用可能なBraze API関数 {#available-braze-api-functions}

MCPクライアントは、Braze MCPサーバーとやり取りするためにこれらのツールを参照します。

### ワークスペース {#workspaces}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | read | 現在のOAuthアクセストークンがアクセスできるBrazeワークスペースを検出します。最初にこれを呼び出してください。返される各ワークスペースの`id`が、他のすべてのツールで必要な`app_group_id`になります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ワークスペース" }

### キャンペーン {#campaigns}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | read | 名前、キャンペーンAPI識別子、APIキャンペーンフラグ、タグを含むキャンペーンのリストをエクスポートします。 |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | read | `campaign_id`で指定されたキャンペーンに関する関連情報を取得します。 |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | read | キャンペーン統計の日次推移（チャネル別の送信数、開封数、クリック数、コンバージョン数）を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="キャンペーン" }

### キャンバス {#canvases}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | read | 名前、キャンバスAPI識別子、タグを含むキャンバスのリストをエクスポートします。 |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | read | キャンバスのメタデータ（名前、作成日時、現在のステータスなど）をエクスポートします。 |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | read | キャンバスの時系列データをエクスポートします。 |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | read | キャンバスの時系列データのロールアップをエクスポートし、簡潔な結果サマリーを提供します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="キャンバス" }

### カタログ {#catalogs}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | read | ワークスペース内のカタログを一覧表示します。 |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | read | 複数のカタログアイテムとその内容を返します。 |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | read | 単一のカタログアイテムとその内容を返します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カタログ" }

### カスタム属性 {#custom-attributes}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | read | アプリ用に記録されたカスタム属性を、50件ずつアルファベット順にエクスポートします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタム属性" }

### カスタムイベント {#custom-events}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | read | アプリ用に記録されたカスタムイベントを、50件ずつアルファベット順にエクスポートします（カーソルページネーション）。 |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | read | カスタムイベント名を、250件ずつアルファベット順にエクスポートします（ページページネーション）。 |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | read | 指定された期間におけるカスタムイベントの発生回数を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムイベント" }

### CDI連携 {#cdi-integrations}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | read | 既存のクラウドデータ取り込み連携を、1回の呼び出しにつき10件ずつ一覧表示します。 |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | read | 指定されたCDI連携の過去の同期ステータスを、1回の呼び出しにつき10件ずつ取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CDI連携" }

### KPI

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | read | 日付ごとのユニークアクティブユーザーの日次推移です。 |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | read | 30日間のローリングウィンドウにおけるユニークアクティブユーザーの日次推移です。 |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | read | 日付ごとの新規ユーザー総数の日次推移です。 |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | read | 日付ごとのアンインストール総数の日次推移です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### メディアライブラリ {#media-library}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | create | 外部URLまたはBase64ファイルコンテンツを使用して、Brazeメディアライブラリにアセットをアップロードします。アップロードモードはいずれか1つのみ指定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="メディアライブラリ" }

### メッセージ {#messages}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | read | 現在から指定された`end_time`までの間にスケジュールされたキャンペーンとエントリキャンバスを一覧表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="メッセージ" }

### 購入 {#purchases}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | read | 商品IDのページネーション付きリストです。 |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | read | 指定された期間におけるアプリ内の購入総数です。 |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | read | 指定された期間におけるアプリ内の総支出額です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="購入" }

### SDK認証 {#sdk-authentication}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | read | アプリのすべてのSDK認証キーを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="SDK認証" }

### セグメント {#segments}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | read | 名前、セグメントAPI識別子、分析トラッキングフラグを含むセグメントをエクスポートします。 |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | read | `segment_id`で指定されたセグメントに関する関連情報を取得します。 |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | read | セグメントの推定サイズの日次推移を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="セグメント" }

### 送信 {#sends}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | read | トラッキング対象の`send_id`（APIキャンペーン）の日次統計です。Brazeは送信後14日間、送信分析データを保存します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="送信" }

### セッション {#sessions}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | read | 指定された期間におけるアプリのセッション数です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="セッション" }

### 購読グループ {#subscription-groups}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | read | 購読グループ内のユーザーの購読状態を取得します。 |
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | read | ユーザーの購読グループを一覧表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="購読グループ" }

### テンプレート {#templates}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | read | Brazeアカウントで利用可能なメールテンプレートを一覧表示します。 |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | read | 特定のメールテンプレートの情報を取得します。ドラッグ＆ドロップエディターのテンプレートは対象外です。 |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | create | Brazeダッシュボードでメールテンプレートを作成します。 |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | update | 既存のメールテンプレートを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="テンプレート" }

### コンテンツブロック {#content-blocks}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | read | 既存のコンテンツブロック情報を一覧表示します。 |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | read | 既存のコンテンツブロックの情報を取得します。オプションでキャンペーンまたはキャンバスの包含データも取得できます。 |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | create | コンテンツブロックを作成します。 |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | update | コンテンツブロックを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="コンテンツブロック" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}