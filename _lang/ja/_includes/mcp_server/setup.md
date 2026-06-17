# Braze MCPサーバーの設定 {#setting-up-the-braze-mcp-server}

> Braze MCPサーバーの設定方法を学習すれば、ClaudeやCursorのような自然言語ツールを使ってBrazeデータとやり取りできるようになります。より一般的な情報については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件 {#prerequisites}

開始する前に、以下のものが必要です。

| 前提条件 | 説明 |
|--------------|-------------|
| Braze APIキー | 必要な権限を持つBraze APIキー。[Braze MCPサーバーを設定する](#create-api-key)際に、新しいキーを作成します。 |
| MCPクライアント | [Claude](https://claude.ai/)、[Cursor](https://cursor.com/)、[Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli)が公式にサポートされています。Braze MCPサーバーを使用するには、これらのクライアントのいずれかのアカウントが必要です。 |
| ターミナル | コマンドの実行やツールのインストールに使用するターミナルアプリ。お好みのターミナルアプリ、またはコンピューターにプリインストールされているものを使用してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Braze MCPサーバーの設定

### ステップ1:`uv`をインストールする {#step-1-install-uv}

まず、`uv`をインストールします。これは[Astralが提供するコマンドラインツール](https://docs.astral.sh/uv/getting-started/installation/)で、依存関係管理とPythonパッケージ処理に使用します。

{% tabs local %}
{% tab MacOS and Linux %}
ターミナルアプリケーションを開き、以下のコマンドを貼り付けて、<kbd>Enter</kbd>を押します。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

出力は以下のようになります。

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Windows %}
 Windows PowerShellを開き、以下のコマンドを貼り付けて<kbd>Enter</kbd>を押します。

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

出力は以下のようになります。

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### ステップ2:APIキーを作成する {#create-api-key}

Braze MCPサーバーには、読み取り専用エンドポイントと書き込みエンドポイントの両方が含まれています。これらのエンドポイントはBrazeユーザープロファイルからデータを返しません。書き込みエンドポイントを使用すると、エージェントがワークスペース内のコンテンツを作成または更新できます。

APIキーを作成するには：

1. **設定** > **APIキー** > **APIキー**に移動します。
2. 新しいキーを作成します。
3. 以下の権限の一部または全部をキーに割り当てます。

{% alert important %}
エージェントに使用させたい権限のみを割り当ててください。エージェントがBraze内で変更を行うことを防ぐには、APIキーを作成する際に書き込み権限を外しておいてください。
{% endalert %}

{% details サポートされている権限の一覧 %}
#### Campaigns

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

#### Canvas

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas" }

#### カタログ {#catalogs}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カタログ" }

#### クラウドデータ取り込み {#cloud-data-ingestion}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クラウドデータ取り込み" }

#### Content Blocks

`content_blocks.create`と`content_blocks.update`の権限は書き込み権限です。エージェントにワークスペース内のコンテンツブロックの作成や更新を許可する場合のみ、これらの権限を追加してください。

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | `content_blocks.info` |
| [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | `content_blocks.create` |
| [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | `content_blocks.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

#### カスタム属性 {#custom-attributes}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタム属性" }

#### イベント {#events}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="イベント" }

#### KPI {#kpis}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KPI" }

#### メディアライブラリ {#media-library}

`media_library.create`の権限は書き込み権限です。エージェントにメディアライブラリへのアセットのアップロードを許可する場合のみ、この権限を追加してください。

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | `media_library.create` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メディアライブラリ" }

#### メッセージ {#messages}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メッセージ" }

#### ユーザー設定センター {#preference-center}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー設定センター" }

#### 購入 {#purchases}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="購入" }

#### Segments

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segments" }

#### 送信 {#sends}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="送信" }

#### セッション {#sessions}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="セッション" }

#### SDK認証キー {#sdk-authentication-keys}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK認証キー" }

#### サブスクリプション {#subscription}

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サブスクリプション" }

#### テンプレート {#templates}

`templates.email.create`と`templates.email.update`の権限は書き込み権限です。エージェントにワークスペース内のメールテンプレートの作成や更新を許可する場合のみ、これらの権限を追加してください。

| エンドポイント | 必要な権限 |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | `templates.email.info` |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | `templates.email.create` |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | `templates.email.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テンプレート" }
{% enddetails %}

{% alert warning %}
既存のAPIキーを再利用しないでください。MCPクライアント専用に新しいキーを作成してください。エージェントに必要な権限のみを割り当ててください。エージェントは付与された権限を使用しようとする可能性があるため、Braze内で変更を行わせたくない場合は、書き込み権限を外しておいてください。
{% endalert %}

### ステップ3:識別子とエンドポイントを取得する {#step-3-get-your-identifier-and-endpoint}

MCPクライアントを設定する際には、APIキーの識別子とワークスペースのRESTエンドポイントが必要です。これらの詳細を取得するには、ダッシュボードの**APIキー**ページに戻ります。[次のステップ](#configure-client)で参照できるよう、このページを開いたままにしておいてください。

![Brazeの「APIキー」ページに、新しく作成されたAPIキーとユーザーのRESTエンドポイントが表示されている。]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### ステップ4:MCPクライアントを設定する {#configure-client}

あらかじめ用意された設定ファイルを使って、MCPクライアントを設定します。

{% tabs %}
{% tab Claude %}
[Claude Desktop](https://claude.ai/download)のコネクタディレクトリを使ってMCPサーバーを設定します。

1. Claude Desktopで、**Settings** > **Connectors** > **Browse Connectors** > **Desktop Extensions** > **Braze MCP Server** > **Install**に移動します。
2. APIキーとベースURLを入力します。
3. 設定を保存し、Claude Desktopを再起動します。

{% endtab %}

{% tab Cursor %}
[Cursor](https://cursor.com/)で、**Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP**に移動し、以下のスニペットを追加します。

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

`key-identifier`と`rest-endpoint`を、Brazeの**APIキー**ページにある対応する値で置き換えます。設定は以下のようになります。

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

完了したら、設定を保存してCursorを再起動します。
{% endtab %}
{% tab Gemini CLI %}
Gemini CLIはユーザー設定を`~/.gemini/settings.json`から読み込みます。このファイルが存在しない場合は、ターミナルで以下のコマンドを実行して作成できます。

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

次に、`yourname`をターミナルプロンプトの`@BZXXXXXXXX`の前にある文字列に正確に置き換えます。続いて、`key-identifier`と`rest-endpoint`を、Brazeの**APIキー**ページにある対応する値で置き換えます。

設定は以下のようになります。

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

完了したら、設定を保存してGemini CLIを再起動します。次に、Geminiで以下のコマンドを実行して、Braze MCPサーバーがリストに表示されていること、およびツールとスキーマが使用可能であることを確認します。

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

利用可能なツールとスキーマとともに`braze`サーバーが一覧表示されるはずです。

{% endtab %}
{% endtabs %}

### ステップ5:テストプロンプトを送信する {#step-5-send-a-test-prompt}

Braze MCPサーバーを設定したら、MCPクライアントにテストプロンプトを送信してみましょう。その他の例やベストプラクティスについては、[Braze MCPサーバーの使い方]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}を参照してください。

{% tabs %}
{% tab Claude %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Used `list_functions` and returned available Braze MCP function groups.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Queried `list_functions` and listed sample functions such as `get_canvas_list`.
{% endtab %}

{% tab Gemini CLI %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Queried `list_functions` in Gemini CLI and returned available Braze MCP function categories and sample functions.
{% endtab %}
{% endtabs %}

## トラブルシューティング {#troubleshooting}

### ターミナルエラー {#terminal-errors}

#### `uvx`コマンドが見つからない {#uvx-command-not-found}

`uvx`コマンドが見つからないというエラーが表示された場合は、`uv`を再インストールしてターミナルを再起動してください。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT`エラー {#spawn-uvx-enoent-error}

`spawn uvx ENOENT`エラーが発生した場合は、クライアントの設定ファイル内のファイルパスを更新する必要があるかもしれません。まず、ターミナルを開いて以下のコマンドを実行します。

```bash
which uvx
```

コマンドは以下のようなメッセージを返すはずです。

```bash
/Users/alex-lee/.local/bin/uvx
```

メッセージをクリップボードにコピーし、[クライアントの設定ファイル](#configure-client)を開きます。`"command": "uvx"`をコピーしたパスで置き換え、クライアントを再起動します。例：

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### パッケージのインストールに失敗する {#package-installation-fails}

パッケージのインストールに失敗した場合は、特定のPythonバージョンを指定してインストールしてみてください。

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### クライアント設定 {#client-configuration}

#### 「この拡張機能はお使いのデバイスと互換性がありません」 {#this-extension-is-not-compatible-with-your-device}

Braze MCPサーバー拡張機能のインストール時にこのエラーが表示された場合、以下のいずれかが原因である可能性があります。

- **デバイスが要件を満たしていない**：一部のMCPサーバー拡張機能には、特定のオペレーティングシステムバージョンやハードウェアが必要です。
- **開発ツールがインストールされていない（macOSのみ）**：macOSでは、拡張機能のインストールにPythonコマンドを実行するためのコマンドライン開発者ツールが必要です。これらのツールがインストールされていない場合、このエラーでインストールが失敗します。

macOSでコマンドライン開発者ツールをインストールするには、ターミナルで以下を実行します。

```bash
xcode-select --install
```

インストールが完了したら、MCPクライアントを再起動し、拡張機能のインストールを再度お試しください。

#### MCPクライアントがBrazeサーバーを見つけられない {#mcp-client-cant-find-the-braze-server}

1. MCPクライアントの設定構文が正しいことを確認してください。
2. 設定変更後にMCPクライアントを再起動してください。
3. `uvx`がシステムの`PATH`に含まれていることを確認してください。

#### 認証エラー {#authentication-errors}

1. `BRAZE_API_KEY`が正しく、アクティブであることを確認してください。
2. `BRAZE_BASE_URL`がBrazeインスタンスと一致していることを確認してください。
3. APIキーに[正しい権限](#create-api-key)が設定されていることを確認してください。

#### 接続タイムアウトまたはネットワークエラー {#connection-timeouts-or-network-errors}

1. `BRAZE_BASE_URL`がインスタンスに対して正しいことを確認してください。
2. ネットワーク接続とファイアウォールの設定を確認してください。
3. ベースURLでHTTPSを使用していることを確認してください。

{% multi_lang_include mcp_server/legal_disclaimer.md %}