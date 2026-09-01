# Braze MCPサーバーの設定 {#setting-up-the-braze-mcp-server}

> BrazeリモートMCPサーバーへの接続方法、OAuthによる認証、MCPクライアントからのBrazeツールの使用開始方法について説明します。詳細については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件 {#prerequisites}

始める前に、以下の準備が整っていることを確認してください。

| 前提条件 | 説明 |
|----------|------|
| サポート対象のMCPクライアント | OAuthを使用したリモートMCPサーバーをサポートする任意のクライアントが使用できます。Brazeでは、Claude、ChatGPT、Cursor、OpenAI Codex、Claude Code、およびVisual Studio Codeでの動作を検証済みです。 |
| Brazeダッシュボードアカウント | 通常のBraze認証情報でサインインします。会社がSSOまたはSAMLを使用している場合はそれも含まれます。MCP専用のログインは不要です。 |
| サーバーエンドポイントの選択 | `https://mcp.braze.com/mcp`（US）または`https://mcp.braze.eu/mcp`（EU）を選択してください。どちらのエンドポイントからでも任意のBrazeクラスターにアクセスできます。 |
| IP許可リストなし | [IP許可リスト](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting)を使用しているお客様は、現時点ではBraze MCPサーバーを使用できません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% alert note %}
エージェントのアクセス権はダッシュボードの権限を反映します。ダッシュボードのアクセスがワークスペース全体ではなくチームにスコープされている場合、一部のツールが機能しないことがあります。
{% endalert %}

## アクセスの管理（管理者向け） {#managing-access-for-admins}

{% alert note %}
ユーザーが接続する前に、会社の管理者が**設定** > **管理者設定** > **OAuth**で**MCP OAuthアクセス**を有効にする必要があります。詳細については、[OAuth設定の管理]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin)を参照してください。
{% endalert %}

### アクセスの付与 {#grant-access}

管理者は「Use MCP Server」権限を通じてMCPサーバーへのアクセスをコントロールします。デフォルトでは、ユーザーはこの権限を持っておらず、明示的に付与する必要があります。

### アクセスの取り消し {#revoke-access}

アクセスを取り消すには、ユーザーから「Use MCP Server」権限を削除します。ダッシュボードの権限をユーザーから削除すると、次のリクエスト時に接続されているすべてのエージェントからもその機能が削除されます。

### 利用状況の監査 {#audit-usage}

ユーザーがOAuthを通じて正常に接続すると、[セキュリティイベントレポート](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#security-event-report)にイベントが記録されます。

## クライアントを接続する {#connect-your-client}

### ステップ1：権限とワークスペースアクセスを確認する {#step-1-confirm-permissions-and-workspace-access}

1. あなたまたは会社の管理者が、「Use MCP Server」権限が付与されていることを確認する必要があります。
2. 複数のワークスペースにアクセスする必要がある場合は、関連するすべてのワークスペースでその権限が有効になっていることを確認してください。

### ステップ2：BrazeをリモートMCPコネクターとして追加する {#step-2-add-braze-as-a-remote-mcp-connector}

MCPクライアントで、新しいリモートサーバーまたはカスタムコネクターを追加し、Braze MCPのURLを入力します。たとえば、Claudeでは**Settings** > **Connectors** > **Add custom connector**に移動してURLを貼り付けます。

クライアントID、クライアントシークレット、APIキーは不要です。クライアントはBrazeに自動的に登録されます。

Braze MCPエンドポイントオプション：

- `https://mcp.braze.com/mcp`（US）
- `https://mcp.braze.eu/mcp`（EU）

{% alert tip %}
EUの顧客はEUエンドポイントを使用してください。EU以外の顧客はどちらのエンドポイントでも使用できます。
{% endalert %}

クライアント設定ガイド：

- [Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code](https://code.claude.com/docs/en/mcp-quickstart)
- [ChatGPT](https://developers.openai.com/api/docs/guides/developer-mode)
- [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
- [OpenAI Codex](https://developers.openai.com/codex/mcp)
- [Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

### ステップ3：OAuthを通じてBrazeにサインインする {#step-3-sign-in-to-braze-through-oauth}

エージェントが初めてBrazeツールを呼び出すと、クライアントがブラウザウィンドウを開き、Brazeのサインインページに遷移します。

1. SSOが必要な場合も含め、通常どおりBrazeにサインインします。
2. ログインが同じクラスター上の複数の会社にアクセスできる場合は、使用する会社を選択します。
3. 同意画面で、アプリケーションが要求しているアクセス権を確認します。
4. Brazeプライバシーポリシーに同意する確認チェックボックスを選択し、**Continue**を選択してMCPクライアントに戻ります。

![Claude DesktopがBrazeアカウント情報およびBrazeデータへの幅広いアクセスを要求していることを表示するBraze同意画面。プライバシーポリシーの確認チェックボックスと、CancelおよびContinueボタンが含まれています。]({% image_buster /assets/img/mcp_server/oauth_consent_screen.png %}){: style="max-width:65%;"}

セッションは自動的にリフレッシュされる短期間のアクセストークンを使用します。場合によっては再度サインインが必要になることがあります。

### ステップ4：使用するワークスペースをエージェントに伝える {#step-4-tell-your-agent-which-workspace-to-use}

アカウントが複数のワークスペースにアクセスできる場合は、プロンプトでワークスペースを指定してください。例：

- `I'd like to look at campaign analytics for the past week in the Production workspace.`
- `Can you compare this week's analytics between my prod-1 workspace and my prod-2 workspace?`

ワークスペースを指定しない場合、エージェントから確認を求められることがあります。

### ステップ5：テストプロンプトを送信する {#step-5-send-a-test-prompt}

設定後、次のような簡単な検証プロンプトを送信します：

- `List the Braze tools available in this workspace.`
- `Show my recent キャンバス from the Production workspace.`

その他の例については、[Braze MCPサーバーの使用]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}を参照してください。

## 例：Claudeとの接続 {#example-connect-with-claude}

クライアントの接続は数ステップで完了します。以下のウォークスルーではClaudeを使用していますが、他のサポート対象クライアントでもフローは同様です。

1. Claudeで、**Settings** > **Connectors** > **Add custom connector**に移動します。
2. `Braze`などの名前を入力し、Braze MCP URLを貼り付けます：USの場合は`https://mcp.braze.com/mcp`、EUの場合は`https://mcp.braze.eu/mcp`です。クライアントID、クライアントシークレット、APIキーは必要ありません。
3. **Add**を選択してコネクターを保存します。ClaudeはBrazeに自動的に登録されます。
4. **Connect**を選択して認証を開始します。Claudeがブラウザウィンドウを開き、Brazeのサインイン画面に移動します。
5. SSO（会社で使用している場合を含む）など、通常の認証情報でBrazeにサインインします。ログインアカウントが同じクラスター上の複数の会社にアクセスできる場合は、使用する会社を選択します。
6. 同意画面で、要求されたアクセスを確認し、承認チェックボックスを選択してから、**Continue**を選択します。Claudeがチャットに戻り、エージェントがBrazeツールを使用できるようになります。

接続を確認するには、`Show my recent キャンバス from the Production workspace`のようなテストプロンプトを送信します。

## ローカルベータサーバーからの移行 {#migrating-from-the-local-beta-server}

移行期間中は、ローカルベータサーバーとリモートホストサーバーを並行して実行できます。どちらを使用するか、エージェントに明示的に指定する必要がある場合があります。

リモートホストサーバーには、ローカルベータサーバーには存在しない新しいツールが含まれています。ローカルサーバー用にスキルを構築した場合、新しいツール名や動作を参照するようにスキルを更新する必要がある場合があります。

ワークフローとスキルがリモートサーバーで正常に動作することを確認したら、ローカルホストサーバーを無効にしてください。

## トラブルシューティング {#troubleshooting}

### サポートされているクライアントで認証に失敗する {#authentication-fails-in-a-supported-client}

1. 会社の管理者が[OAuth設定]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin)で**MCP OAuthアクセス**を有効にしていることを確認します。
2. ユーザーに「Use MCP Server」権限があることを確認します。
3. サインインと認証を再試行します。

### 未検証のクライアントで認証がブロックされる {#authentication-is-blocked-in-an-unverified-client}

Brazeはセキュリティのため、サポートされているクライアントドメインの許可リストを管理しています。許可リストにないクライアントから接続すると、認証がブロックされる場合があります。{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="support for your MCP client" %}

Claude CodeやOpenAI Codexなど、カスタムスキームなしでローカルマシン上で実行されるクライアントも動作するはずです。

### クライアントにツールが表示されない {#tools-dont-appear-in-your-client}

エージェントがBrazeツールを一覧表示できない場合は、数分待ってから再試行してください。これらの問題は一時的なもので、自然に解消されることが多いです。

問題が続く場合は、動画を録画して[mcp-product@braze.com](mailto:mcp-product@braze.com)に送信し、調査を依頼してください。

### エージェントが期待するツールにアクセスできない {#agent-cannot-access-expected-tools}

1. ダッシュボードユーザーに必要な権限があることを確認します。エージェントが使用できるツールは、ユーザー自身のダッシュボードアクセス権に対応するもののみです。
2. プロンプトで期待するワークスペースを選択していることを確認します。
3. エージェントに`get_workspaces`を呼び出すよう依頼し、利用可能なワークスペースIDを確認します。

### エージェントが間違ったワークスペースを使用する {#agent-uses-the-wrong-workspace}

アカウントが複数のワークスペースにアクセスできる場合は、Brazeダッシュボードに表示されている正確な名前を使用して、プロンプトでワークスペースを指定してください。ワークスペースを指定しない場合、エージェントが確認を求めたり、意図しないワークスペースを使用したりする可能性があります。

{% alert important %}
エージェントが作業を開始する前に、使用しているワークスペースを必ず確認してください。エージェントが意図したものとは異なるワークスペースを選択する場合があります。
{% endalert %}

### 別の会社に切り替える {#switching-to-a-different-company}

会社は最初の認証時に設定されます。同じクラスター上の別の会社で作業するには、クライアントでBrazeコネクタを切断し、再認証を行い、サインイン時にもう一方の会社を選択してください。

{% multi_lang_include mcp_server/legal_disclaimer.md %}