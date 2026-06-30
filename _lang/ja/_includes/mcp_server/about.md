# Braze MCPサーバー {#the-braze-mcp-server}

> Braze MCPサーバーについて学びましょう。これはClaudeやCursorのようなAIツールが非PIIのBrazeデータにアクセスして質問に答え、傾向を分析し、インサイトを提供できるようにする安全な接続です。

{% alert important %}
今夏、BrazeはリモートのBrazeホスト型MCPサーバーを早期アクセスとして提供開始します。これは、ローカルホスト型のベータサーバー（[PyPI](https://pypi.org/project/braze-mcp-server/)上の`braze-mcp-server`およびClaude Desktopの拡張機能ディレクトリ）に代わるものです。<br><br>

**これがあなたにとって意味すること：**<br><br>

- ローカルホスト型サーバーは引き続き動作しますが、サポートは終了しています。ベータ版への新しいエンドポイントの追加や問題の修正は行いません。
- リモートサーバーが早期アクセスで利用可能になった際には、切り替えが必要です。リモートサーバーはローカルインストール不要で、静的APIキーの代わりにOAuthを使用し、Claude、Copilot、Gemini CLI、Codex、CursorなどのMCPクライアントで動作します。
- 早期アクセスの提供開始については、このページをご確認いただくか、Brazeアカウントチームにご連絡ください。
{% endalert %}

## モデルコンテキストプロトコル（MCP）とは {#what-is-model-context-protocol-mcp}

モデルコンテキストプロトコル（MCP）とは、AIエージェントが別のプラットフォームのデータに接続し、そのデータと連動できるようにする規格です。主に2つの部分で構成されています。

- **MCPクライアント：** AIエージェントが動作するアプリケーション（CursorやClaudeなど）。
- **MCPサーバー：** 別のプラットフォーム（Brazeなど）が提供するサービスで、AIが使用できるツールとアクセス可能なデータを定義します。

## Braze MCPサーバーについて {#about-the-braze-mcp-server}

[Braze MCPサーバーの設定]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}後、エージェントやアシスタント、チャットボットなどのAIツールをBrazeに直接接続し、CanvasやCampaignの分析、カスタム属性、Segmentsなどの集計データを読み取れるようになります。Braze MCPサーバーは以下のようなユースケースに最適です。

- Brazeのコンテキストを必要とするAI搭載ツールの構築。
- マルチステップのエージェントワークフローを作成するCRMエンジニア。
- 自然言語クエリを試す技術系マーケター。

Braze MCPサーバーには、読み取り専用と書き込みの両方のエンドポイントが含まれています。Brazeユーザープロファイルからデータを返すことはありません。Braze APIキーに割り当てるエンドポイントを選択することで、エージェントが読み取り、作成、または更新できる範囲をコントロールできます。利用可能なエンドポイントの完全なリストと必要な権限については、[利用可能なAPI機能]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}を参照してください。

{% alert warning %}
エージェントに持たせたいAPIキーの権限のみを割り当ててください。エージェントにBraze内で変更を加えさせたくない場合は、APIキーを作成する際に書き込み権限をオフのままにしてください。エージェントは、付与された書き込み権限を通じてデータの書き込みを試みる可能性があります。
{% endalert %}

## 使用例 {#usage-example}

ClaudeやCursorのようなツールを使って、自然言語でBrazeとやり取りできます。その他の例やベストプラクティスについては、[Braze MCPサーバーの使用方法]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}を参照してください。

{% tabs %}
{% tab Claude %}
**プロンプトの例：** `What are my available Braze functions?`
**応答の例：** `list_functions`を使用し、利用可能なBraze MCP機能カテゴリを返しました。
{% endtab %}

{% tab Cursor %}
**プロンプトの例：** `What are my available Braze functions?`
**応答の例：** `list_functions`をクエリし、`get_canvas_list`などの機能を一覧表示しました。
{% endtab %}
{% endtabs %}

## よくある質問（FAQ） {#faq}

### どのMCPクライアントがサポートされていますか？ {#which-mcp-clients-are-supported}

正式にサポートされているのは[Claude](https://claude.ai/)と[Cursor](https://cursor.com/)のみです。Braze MCPサーバーを利用するには、これらのクライアントのいずれかのアカウントが必要です。

### MCPクライアントはBrazeのどのデータにアクセスできますか？ {#what-braze-data-can-my-mcp-client-access}

MCPクライアントは、PIIを返さないエンドポイントにアクセスできます。エージェントが使用できるエンドポイントは、APIキーに割り当てた権限によってコントロールできます。

### MCPクライアントはBrazeデータを変更できますか？ {#can-my-mcp-client-change-braze-data}

はい。サーバーは、エージェントがワークスペース内のコンテンツ（メディアライブラリのアセット、メールテンプレート、Content Blocksなど）を作成または更新できる、限定された書き込みエンドポイントのセットを公開しています。各書き込みエンドポイントには、それぞれ独自のAPIキー権限が必要です。エージェントにBraze内で特定の変更を加えさせたくない場合は、APIキーを作成する際にその権限をオフのままにしてください。書き込み機能の完全なリストと必要な権限については、[利用可能なAPI機能]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}を参照してください。

### BrazeでサードパーティのMCPサーバーを使用できますか？ {#can-i-use-a-third-party-mcp-server-for-braze}

Brazeデータに対してサードパーティのMCPサーバーを使用することは推奨されません。[PyPi](https://pypi.org/project/braze-mcp-server/)でホストされている公式のBraze MCPサーバーのみを使用してください。

### なぜBraze MCPサーバーはPIIアクセスを提供しないのですか？ {#why-doesnt-the-braze-mcp-server-offer-pii-access}

ユーザーデータを保護しつつ価値あるユースケースをサポートするため、サーバーは通常PIIを返さないエンドポイントに限定されています。これにより、ワークスペースとそこに含まれるユーザーのリスクが軽減されます。

### APIキーは再利用できますか？ {#can-i-reuse-my-api-keys}

いいえ。MCPクライアント用に新しいAPIキーを作成する必要があります。AIツールには許容できる範囲のアクセスのみを付与し、過剰な権限は避けてください。

### Braze MCPサーバーはローカルでホストされていますか、それともリモートですか？ {#is-the-braze-mcp-server-hosted-locally-or-remotely}

現在利用可能なBraze MCPサーバーはローカルでホストされています。リモートのBrazeホスト型MCPサーバーは今夏に早期アクセスとして提供開始され、ローカルホスト型のベータサーバーに代わるものとなります。

### Cursorが関数のリストしか表示しないのはなぜですか？ {#why-is-cursor-only-listing-functions}

askモードかagentモードかを確認してください。MCPサーバーを使用するには、agentモードである必要があります。

### エージェントが誤った回答を返した場合はどうすればよいですか？ {#what-do-i-do-when-the-agent-returns-an-answer-that-looks-incorrect}

Cursorのようなツールを使用している場合は、使用するモデルを変更してみてください。例えば、自動設定にしている場合は、特定のモデルに変更し、ユースケースに最適なモデルを見つける実験をしてみてください。新しいチャットを開始してプロンプトを再試行することもできます。

問題が解決しない場合は、[mcp-product@braze.com](mailto:mcp-product@braze.com)までメールでお知らせください。可能であれば、動画を添付し、コール機能を展開してエージェントが試みたコールを確認できるようにしてください。

{% multi_lang_include mcp_server/legal_disclaimer.md %}