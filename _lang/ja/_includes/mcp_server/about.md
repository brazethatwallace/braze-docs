# Braze MCPサーバー {#the-braze-mcp-server}

> Braze MCPサーバーについて学びましょう。これはClaudeやCursorのようなAIツールが非PIIのBrazeデータにアクセスして質問に答え、傾向を分析し、インサイトを提供し、コンテンツを作成できるようにする安全なリモート接続です。

{% alert important %}
リモートMCPサーバーは早期アクセス段階です。アクセスをリクエストするには、アカウントマネージャーにお問い合わせください。
{% endalert %}

## モデルコンテキストプロトコル（MCP）とは {#what-is-model-context-protocol-mcp}

モデルコンテキストプロトコル（MCP）とは、AIエージェントが別のプラットフォームのデータに接続し、そのデータと連動できるようにする規格です。主に2つの部分で構成されています。

- **MCPクライアント：** AIエージェントが動作するアプリケーション（CursorやClaudeなど）。
- **MCPサーバー：** 別のプラットフォーム（Brazeなど）が提供するサービスで、AIが使用できるツールとアクセス可能なデータを定義します。

## Braze MCPサーバーについて {#about-the-braze-mcp-server}

[Braze MCPサーバーの設定]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}後、エージェントやアシスタント、チャットボットなどのAIツールをBrazeに直接接続し、キャンバスやキャンペーンの分析、カスタム属性、セグメントなどの集計データを読み取れるようになります。Braze MCPサーバーは以下のようなユースケースに最適です。

- Brazeのコンテキストを必要とするAI搭載ツールの構築。
- マルチステップのエージェントワークフローを作成するCRMエンジニア。
- 自然言語クエリを試す技術系マーケター。

Braze MCPサーバーには、読み取りと書き込みの両方のツールが含まれています。これらのツールはBrazeユーザープロファイルからデータを返すことはありません。エージェントはBrazeダッシュボードのユーザー権限を継承します。利用可能なツールの完全なリストについては、[利用可能なAPI機能]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}を参照してください。

{% alert warning %}
ユーザーレベルのPIIを公開するツールは利用できません。
{% endalert %}

MCPサーバーを使用して、キャンペーンやキャンバスのパフォーマンスに関する質問をしたり、セグメントやカスタム属性を調べたり、レポートを生成したり、メールテンプレート、コンテンツブロック、メディアライブラリのアセットなどのコンテンツを自然言語で作成したりできます。

## ベータ版MCPサーバーは非推奨ですか？ {#is-the-beta-mcp-server-deprecated}

はい。2025年8月にリリースされたローカルホスト型MCPサーバーは非推奨であり、追加の更新は行われません。引き続き使用できますが、Brazeはリモートホスト版への移行を推奨しています。

### リモートサーバーはどう違いますか？ {#how-is-the-remote-server-different}

以前のBraze MCPサーバーはローカルマシン上で動作していました。パッケージのインストール、設定ファイルの管理、適切な権限を持つBraze APIキーの作成が必要でした。リモートMCPサーバーでは、そのローカル設定が不要になります。

サポートされているMCPクライアントから1分以内に接続できます。認証にはOAuthを使用します。アクセスは共有APIキーではなくBrazeダッシュボードのユーザーアカウントに紐づいているため、エージェントが閲覧・実行できる内容はダッシュボードの権限と同じです。ダッシュボードユーザーがBrazeでアクセスを失うと、クライアントもアクセスを失います。

主な違いは以下のとおりです。

- **設定：** パッケージのインストールや設定ファイルの編集の代わりに、BrazeのURLを貼り付けるだけです。
- **認証：** APIキーの作成の代わりに、Brazeアカウントでサインインします。
- **権限：** APIキーの権限ではなく、ダッシュボードのユーザーアカウントに基づいてアクセスが決まります。
- **ワークスペースの指定：** ローカル設定で固定するのではなく、リクエストごとにワークスペースのコンテキストが渡されます。

## よくある質問（FAQ） {#faq}

### どのMCPクライアントがサポートされていますか？ {#which-mcp-clients-are-supported}

OAuthを使用したリモートMCPサーバーをサポートするMCPクライアントであれば動作します。Brazeが検証済みのクライアントは以下のとおりです。

- カスタムコネクター経由のClaude
- カスタムコネクター経由のChatGPT
- Cursor
- OpenAI Codex
- Claude Code

### MCPクライアントはBrazeのどのデータにアクセスできますか？ {#what-braze-data-can-my-mcp-client-access}

MCPクライアントは、ユーザーレベルのPIIを返さないツールにアクセスできます。

### MCPクライアントはBrazeデータを変更できますか？ {#can-my-mcp-client-change-braze-data}

はい、ダッシュボードユーザーにその権限がある場合は変更できます。

### Braze APIキーは引き続き必要ですか？ {#do-i-still-need-a-braze-api-key}

MCPには不要です。APIキーはREST APIで引き続き使用でき、非推奨にはなりません。

### どのリージョンがサポートされていますか？ {#which-regions-are-supported}

両方のBrazeクラスターがサポートされています。現在、2つのエンドポイントが利用可能です。

- `https://mcp.braze.com/mcp`（US）
- `https://mcp.braze.eu/mcp`（EU）

どちらのエンドポイントからでも、すべてのBrazeクラスターにアクセスできます。

### 検証済みリスト以外のツールでBrazeリモートMCPサーバーを使用できますか？ {#can-i-use-the-braze-remote-mcp-server-with-tools-other-than-the-verified-list}

試すことはできますが、認証がブロックされる場合があります。Brazeは現在、セキュリティのためにサポート対象ドメインの許可リストを管理しています。お使いのツールがリストに含まれておらず、認証の問題が発生した場合は、[mcp-product@braze.com](mailto:mcp-product@braze.com)までお問い合わせください。

### リモートサーバーは複数のワークスペースをサポートしていますか？ {#does-the-remote-server-support-multiple-workspaces}

はい。会話ごとまたはリクエストごとにワークスペースを指定できます。1つの接続で、アクセスが許可されているすべてのワークスペースをカバーできます。

### エージェントはユーザーレベルのPIIにアクセスできますか？ {#can-my-agent-access-user-level-pii}

いいえ。現時点では、PIIを公開するツールは利用できません。

### 権限が変更された場合はどうなりますか？ {#what-happens-when-my-permissions-change}

エージェントのアクセスはダッシュボードユーザーに連動して変更されます。権限の変更は次のリクエスト時に適用されます。無効化されたダッシュボードユーザーはMCPアクセスを失います。

### クライアントのディレクトリにBrazeコネクターが表示されないのはなぜですか？ {#why-do-i-not-see-the-braze-connector-in-my-clients-directory}

ディレクトリへの掲載は早期アクセス開始後に順次展開されます。Braze MCPのURLを使用して、いつでも手動で接続できます。

### 当社ではIP許可リストを使用しています。リモートMCPサーバーを使用できますか？ {#my-company-uses-ip-allowlisting-can-we-use-the-remote-mcp-server}

現時点ではできません。[IP許可リスト](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting)を使用しているお客様は、早期アクセスプログラムに参加できません。

{% multi_lang_include mcp_server/legal_disclaimer.md %}