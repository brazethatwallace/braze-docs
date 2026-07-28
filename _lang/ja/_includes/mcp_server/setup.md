# Braze MCPサーバーの設定 {#setting-up-the-braze-mcp-server}

> BrazeリモートMCPサーバーへの接続方法、OAuthによる認証、MCPクライアントからのBrazeツールの使用開始方法について説明します。詳細については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件 {#prerequisites}

開始する前に、以下の準備が整っていることを確認してください。

| 前提条件 | 説明 |
|--------------|-------------|
| 早期アクセスへの登録 | アカウントマネージャーが早期アクセスプログラムに貴社を登録できます。 |
| サポートされているMCPクライアント | OAuthを使用したリモートMCPサーバーをサポートする任意のクライアントが使用できます。BrazeではClaude、ChatGPT、Cursor、OpenAI Codex、Claude Codeでの動作を確認しています。 |
| Brazeダッシュボードアカウント | 通常のBraze認証情報（貴社がSSOまたはSAMLを使用している場合はそれを含む）でサインインします。MCP専用のログインはありません。 |
| サーバーエンドポイントの選択 | `https://mcp.braze.com/mcp`（US）または`https://mcp.braze.eu/mcp`（EU）を選択してください。どちらのエンドポイントでも任意のBrazeクラスターにアクセスできます。 |
| IPアローリスティング不可 | 現時点では、[IPアローリスティング](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting)を使用しているお客様は早期アクセスに参加できません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% alert note %}
エージェントのアクセス権はダッシュボードの権限と同じです。ダッシュボードのアクセスがワークスペース全体ではなくチームにスコープされている場合、早期アクセス中に一部のツールが動作しないことがあります。
{% endalert %}

## アクセスの管理（管理者向け） {#managing-access-for-admins}

### アクセスの付与 {#grant-access}

管理者は**Use MCP Server**権限を通じてMCPサーバーへのアクセスを制御します。デフォルトではユーザーにこの権限はなく、明示的に付与する必要があります。

管理者にこの権限が表示されない場合は、Brazeアカウントマネージャーに連絡して早期アクセスへの登録をリクエストしてください。

### アクセスの取り消し {#revoke-access}

アクセスを取り消すには、ユーザーから**Use MCP Server**権限を削除します。ユーザーからダッシュボード権限を削除すると、次のリクエスト時に接続されているエージェントからもそれらの機能が削除されます。

### 使用状況の監査 {#audit-usage}

ユーザーがOAuthを通じて正常に接続すると、[セキュリティイベントレポート](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#security-event-report)にイベントが記録されます。

## クライアントの接続 {#connect-your-client}

### ステップ1：権限とワークスペースアクセスを確認する {#step-1-confirm-permissions-and-workspace-access}

1. 自分または会社の管理者が、**Use MCP Server**権限があることを確認します。
2. 複数のワークスペースにアクセスする必要がある場合は、関連するすべてのワークスペースで権限が有効になっていることを確認します。

### ステップ2：BrazeをリモートMCPコネクタとして追加する {#step-2-add-braze-as-a-remote-mcp-connector}

MCPクライアントで、新しいリモートサーバーまたはカスタムコネクタを追加し、Braze MCPのURLを入力します。例えば、Claudeでは**Settings** > **Connectors** > **Add custom connector**に移動してURLを貼り付けます。

クライアントID、クライアントシークレット、APIキーは不要です。クライアントはBrazeに自動的に登録されます。

Braze MCPエンドポイントオプション：

- `https://mcp.braze.com/mcp`（US）
- `https://mcp.braze.eu/mcp`（EU）

{% alert tip %}
EUのお客様はEUエンドポイントを使用してください。EU以外のお客様はどちらのエンドポイントでも使用できます。
{% endalert %}

クライアント設定ガイド：

- [Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code](https://code.claude.com/docs/en/mcp-quickstart)
- [ChatGPT](https://developers.openai.com/api/docs/guides/developer-mode)
- [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
- [OpenAI Codex](https://developers.openai.com/codex/mcp)

### ステップ3：OAuthを通じてBrazeにサインインする {#step-3-sign-in-to-braze-through-oauth}

エージェントが初めてBrazeツールを呼び出すと、クライアントがブラウザウィンドウを開き、Brazeのサインインページに移動します。

1. 通常どおりBrazeにサインインします（必要に応じてSSOを含む）。
2. ログインが同じクラスター上の複数の会社にアクセスできる場合は、使用する会社を選択します。
3. 同意画面で、アプリケーションがリクエストしているアクセスを確認します。
4. Brazeプライバシーポリシーに同意する確認チェックボックスを選択し、**Continue**を選択してMCPクライアントに戻ります。

![Claude DesktopがBrazeアカウント情報およびBrazeデータへの広範なアクセスをリクエストしていることを示すBraze同意画面。プライバシーポリシーの確認チェックボックスと「Cancel」および「Continue」ボタンが表示されています。]({% image_buster /assets/img/mcp_server/oauth_consent_screen.png %}){: style="max-width:65%;"}

セッションは自動的に更新される短期間のアクセストークンを使用します。再度サインインが必要になる場合があります。

### ステップ4：エージェントに使用するワークスペースを指示する {#step-4-tell-your-agent-which-workspace-to-use}

アカウントが複数のワークスペースにアクセスできる場合は、プロンプトでワークスペースを指定します。例：

- `I'd like to look at campaign analytics for the past week in the Production workspace.`
- `Can you compare this week's analytics between my prod-1 workspace and my prod-2 workspace?`

ワークスペースを指定しない場合、エージェントが確認を求めることがあります。

### ステップ5：テストプロンプトを送信する {#step-5-send-a-test-prompt}

設定後、以下のような簡単な検証プロンプトを送信します。

- `List the Braze tools available in this workspace.`
- `Show my recent キャンバス from the Production workspace.`

その他の例については、[Braze MCPサーバーの使い方]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}を参照してください。

## 例：Claudeとの接続 {#example-connect-with-claude}

クライアントの接続は数ステップで完了します。以下のウォークスルーではClaudeを使用していますが、他のサポートされているクライアントでも同様のフローです。

1. Claudeで、**Settings** > **Connectors** > **Add custom connector**に移動します。
2. `Braze`などの名前を入力し、Braze MCPのURLを貼り付けます：USの場合は`https://mcp.braze.com/mcp`、EUの場合は`https://mcp.braze.eu/mcp`。クライアントID、クライアントシークレット、APIキーは不要です。
3. **Add**を選択してコネクタを保存します。ClaudeはBrazeに自動的に登録されます。
4. **Connect**を選択して認証を開始します。Claudeがブラウザウィンドウを開き、Brazeのサインインページに移動します。
5. 通常の認証情報でBrazeにサインインします（貴社がSSOを使用している場合はそれを含む）。ログインが同じクラスター上の複数の会社にアクセスできる場合は、使用する会社を選択します。
6. 同意画面で、リクエストされたアクセスを確認し、確認チェックボックスを選択してから**Continue**を選択します。Claudeがチャットに戻り、エージェントがBrazeツールを使用できるようになります。

接続を確認するには、`Show my recent キャンバス from the Production workspace`のようなテストプロンプトを送信します。

## ローカルベータサーバーからの移行 {#migrating-from-the-local-beta-server}

移行中は、ローカルベータサーバーとリモートホストサーバーを並行して実行できます。エージェントにどちらを使用するか明示的に指示する必要がある場合があります。

リモートホストサーバーには、ローカルベータサーバーには存在しない新しいツールが含まれています。ローカルサーバー用にスキルを構築した場合は、新しいツール名と動作を参照するようにスキルを更新する必要がある場合があります。

リモートサーバーでワークフローとスキルが正常に動作することを確認したら、ローカルホストサーバーを無効にしてください。

## トラブルシューティング {#troubleshooting}

### サポートされているクライアントで認証に失敗する {#authentication-fails-in-a-supported-client}

1. 貴社が早期アクセスに登録されていることを確認します。
2. ユーザーに**Use MCP Server**権限があることを確認します。
3. サインインと認可を再試行します。

### 未検証のクライアントで認証がブロックされる {#authentication-is-blocked-in-an-unverified-client}

早期アクセス中、Brazeはセキュリティのためにサポートされているクライアントドメインのアローリストを管理しています。アローリストにないクライアントから接続すると、認証がブロックされる場合があります。クライアントがサポートされるべきだと思われる場合は、[mcp-product@braze.com](mailto:mcp-product@braze.com)にお問い合わせください。

Claude CodeやOpenAI Codexなど、カスタムスキームなしでローカルマシン上で実行されるクライアントも動作するはずです。

### エージェントが期待されるツールにアクセスできない {#agent-cannot-access-expected-tools}

1. ダッシュボードユーザーに必要な権限があることを確認します。エージェントは、自分のダッシュボードアクセスに一致するツールのみを使用できます。
2. プロンプトで期待されるワークスペースを選択したことを確認します。
3. エージェントに`get_workspaces`を呼び出させ、利用可能なワークスペースIDを確認します。

### エージェントが間違ったワークスペースを使用する {#agent-uses-the-wrong-workspace}

アカウントが複数のワークスペースにアクセスできる場合は、Brazeダッシュボードに表示されている正確な名前を使用してプロンプトでワークスペースを指定してください。ワークスペースを指定しない場合、エージェントが確認を求めるか、意図しないワークスペースを使用する可能性があります。

{% alert important %}
エージェントが作業を開始する前に、使用しているワークスペースを必ず確認してください。場合によっては、エージェントが意図したものとは異なるワークスペースを選択することがあります。
{% endalert %}

### 別の会社への切り替え {#switching-to-a-different-company}

会社は最初の認可時に設定されます。同じクラスター上の別の会社で作業するには、クライアントでBrazeコネクタを切断し、再認可して、サインイン時に別の会社を選択してください。

{% multi_lang_include mcp_server/legal_disclaimer.md %}