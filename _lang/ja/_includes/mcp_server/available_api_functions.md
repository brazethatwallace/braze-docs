# Braze MCPサーバー関数 {#braze-mcp-server-functions}

> Braze MCPサーバーは、特定のBraze REST APIエンドポイントに対応する読み取りおよび書き込みツールを公開しています。詳細については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert note %}
Braze MCPサーバーには、ベータプログラムに参加している顧客のみが利用できるツールが含まれています。ベータプログラムの一部であるツールにアクセスしようとした際に、アカウントでその機能が有効になっていない場合、エラーレスポンスが返されることがあります。ベータプログラムに参加するには、アカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

この機能を使用する前に、[Braze MCPサーバーの設定]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}を完了する必要があります。

## 利用可能なBraze API関数 {#available-braze-api-functions}

MCPクライアントは、これらのツールを使用してBraze MCPサーバーとやり取りします。

### ワークスペース {#workspaces}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | read | 現在のOAuthアクセストークンでアクセスできるBrazeワークスペースを確認します。最初にこれを呼び出してください。返される各ワークスペースの`id`が、他のすべてのツールで必要な`app_group_id`となります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ワークスペース" }

### キャンペーン {#campaigns}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | read | 名前、キャンペーンAPI識別子、APIキャンペーンフラグ、およびタグを含むキャンペーンの一覧をエクスポートします。 |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | read | `campaign_id`で指定されたキャンペーンの関連情報を取得します。 |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | read | キャンペーンの統計情報（送信数、開封数、クリック数、チャネル別コンバージョン数）の日次系列を取得します。 |
| `duplicate_campaign` | [`/campaigns/duplicate`]({{site.baseurl}}/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns) | create | 既存のキャンペーンを複製します。 |
| `create_campaign`<sup>*</sup> | N/A | create | 新しいキャンペーンを作成します。 |
| `edit_campaign`<sup>*</sup> | N/A | update | 既存のキャンペーンを編集します。 |
| `launch_campaign`<sup>*</sup> | N/A | update | キャンペーンを起動します。 |
| `stop_campaign`<sup>*</sup> | N/A | update | 実行中のキャンペーンを停止します。 |
| `archive_campaign`<sup>*</sup> | N/A | update | キャンペーンをアーカイブします。 |
| `unarchive_campaign`<sup>*</sup> | N/A | update | キャンペーンのアーカイブを解除します。 |
| `get_campaign_draft`<sup>*</sup> | N/A | read | キャンペーンの下書き詳細を取得します。 |
| `get_campaign_live_details`<sup>*</sup> | N/A | read | ライブキャンペーンの詳細を取得します。 |
| `create_campaign_message`<sup>*</sup> | N/A | create | キャンペーン内にメッセージを作成します。 |
| `update_campaign_message`<sup>*</sup> | N/A | update | キャンペーンメッセージを更新します。 |
| `delete_campaign_message`<sup>*</sup> | N/A | delete | キャンペーンメッセージを削除します。 |
| `create_campaign_message_variation`<sup>*</sup> | N/A | create | キャンペーン内にメッセージバリエーションを作成します。 |
| `update_campaign_message_variation`<sup>*</sup> | N/A | update | キャンペーンメッセージバリエーションを更新します。 |
| `delete_campaign_message_variation`<sup>*</sup> | N/A | delete | キャンペーンメッセージバリエーションを削除します。 |
| `update_campaign_distribution`<sup>*</sup> | N/A | update | キャンペーンの配信設定を更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="キャンペーン" }

<sup>*</sup> このツールは、キャンペーンAPIベータプログラムに参加している顧客のみが利用できます。アカウントでこの機能が有効になっていない場合、使用時にエラーが発生する可能性があります。ベータプログラムに参加するには、アカウントマネージャーにお問い合わせください。
{: .reset-td-br-1 }

### キャンバス {#canvases}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | read | 名前、キャンバスAPI識別子、およびタグを含むキャンバスの一覧をエクスポートします。 |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | read | キャンバスのメタデータ（名前、作成日時、現在のステータスなど）をエクスポートします。 |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | read | キャンバスの時系列データをエクスポートします。 |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | read | キャンバスの時系列データの集計をエクスポートし、簡潔な結果サマリーを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="キャンバス" }

### カタログ {#catalogs}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | read | ワークスペース内のカタログを一覧表示します。 |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | read | 複数のカタログアイテムとそのコンテンツを返します。 |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | read | 単一のカタログアイテムとそのコンテンツを返します。 |
| `create_catalog` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | create | カタログを作成します。 |
| `delete_catalog` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | delete | カタログを削除します。 |
| `create_catalog_fields` | [`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields) | create | カタログに複数のフィールドを作成します。 |
| `delete_catalog_field` | [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field) | delete | カタログフィールドを削除します。 |
| `create_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | create | カタログに複数のアイテムを作成します。1リクエストあたり最大50アイテムです。 |
| `edit_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | update | カタログ内の複数の既存アイテムを編集します。1リクエストあたり最大50アイテムです。 |
| `replace_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | update | カタログ内の複数のアイテムを置換します。アイテムが存在しない場合は作成されます。1リクエストあたり最大50アイテムです。 |
| `delete_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | delete | カタログ内の複数のアイテムを削除します。1リクエストあたり最大50アイテムです。 |
| `create_catalog_selection` | [`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | create | カタログにセレクションを作成します。 |
| `delete_catalog_selection` | [`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection) | delete | カタログセレクションを削除します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カタログ" }

### カスタム属性 {#custom-attributes}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | read | アプリに記録されたカスタム属性を、アルファベット順に50件ずつエクスポートします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタム属性" }

### カスタムイベント {#custom-events}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | read | アプリに記録されたカスタムイベントを、アルファベット順に50件ずつエクスポートします（カーソルページネーション）。 |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | read | カスタムイベント名を、アルファベット順に250件ずつエクスポートします（ページページネーション）。 |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | read | 指定された期間におけるカスタムイベントの発生回数を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムイベント" }

### CDI連携 {#cdi-integrations}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | read | 既存のクラウドデータ取り込み連携を、1回の呼び出しにつき10件ずつ一覧表示します。 |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | read | 指定されたCDI連携の過去の同期ステータスを、1回の呼び出しにつき10件ずつ取得します。 |
| `trigger_integration_sync` | [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | write | 指定されたCDI連携の同期をトリガーします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CDI連携" }

### KPI

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | read | 日付ごとのユニークアクティブユーザー数の日次系列を取得します。 |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | read | 30日間のローリングウィンドウにおけるユニークアクティブユーザー数の日次系列を取得します。 |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | read | 日付ごとの新規ユーザー総数の日次系列を取得します。 |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | read | 日付ごとのアンインストール総数の日次系列を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### メディアライブラリ {#media-library}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | create | 外部URLまたはbase64ファイルコンテンツを使用して、Brazeメディアライブラリにアセットをアップロードします。いずれか1つのアップロードモードを指定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="メディアライブラリ" }

### 購入 {#purchases}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | read | ページネーションされたプロダクトIDの一覧を取得します。 |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | read | 指定期間におけるアプリ内の購入総数を取得します。 |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | read | 指定期間におけるアプリ内の合計消費金額を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="購入" }

### セグメント {#segments}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | read | 名前、セグメントAPI識別子、および分析トラッキングフラグを含むセグメントをエクスポートします。 |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | read | `segment_id`で指定されたセグメントの関連情報を取得します。 |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | read | セグメントの推定サイズの日次系列を取得します。 |
| `get_segment_filters`<sup>*</sup> | N/A | read | セグメントフィルターの定義を取得します。 |
| `create_segment`<sup>*</sup> | N/A | create | 新しいセグメントを作成します。 |
| `edit_segment`<sup>*</sup> | N/A | update | 既存のセグメントを編集します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="セグメント" }

<sup>*</sup> このツールは、セグメントAPIベータプログラムに参加している顧客のみが利用できます。アカウントでこの機能が有効になっていない場合、使用時にエラーが発生する可能性があります。ベータプログラムに参加するには、アカウントマネージャーにお問い合わせください。
{: .reset-td-br-1 }

### 送信 {#sends}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | read | トラッキングされた`send_id`（APIキャンペーン）の日次統計を取得します。Brazeは送信後14日間、送信分析を保持します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="送信" }

### セッション {#sessions}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | read | 指定された期間におけるアプリのセッション数を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="セッション" }

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
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | read | 既存のコンテンツブロックの情報を取得します。オプションでキャンペーンまたはキャンバスの利用データも含められます。 |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | create | コンテンツブロックを作成します。 |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | update | コンテンツブロックを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="コンテンツブロック" }

### オペレーター {#operator}

| ツール | APIエンドポイント | アクセス | 説明 |
| --- | --- | --- | --- |
| `send_operator_prompt` | N/A | update | 自然言語のプロンプトをBrazeAI Operatorに送信します。バックグラウンドジョブを送信し、job_idを返します。 |
| `get_operator_result` | N/A | read | job_idを使用して、送信済みのオペレータージョブの結果をポーリングします。 |
| `cancel_operator_job` | N/A | update | 実行中のオペレータージョブをキャンセルします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オペレーター" }

{% alert important %}
これらのツールは、オペレーターベータプログラムに参加している顧客のみが利用できます。アカウントでこの機能が有効になっていない場合、使用時にエラーが発生する可能性があります。ベータプログラムに参加するには、アカウントマネージャーにお問い合わせください。
{% endalert %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}