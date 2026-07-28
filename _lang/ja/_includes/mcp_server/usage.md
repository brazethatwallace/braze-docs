# Braze MCPサーバーを使用する {#using-the-braze-mcp-server}

> リモートBraze MCPサーバーに接続した後、自然言語を使ってBrazeデータとやり取りする方法を学習しましょう。詳細については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件 {#prerequisites}

この機能を使用する前に、[Braze MCPサーバーのセットアップ]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}を完了する必要があります。

## ベストプラクティス {#best-practices}

自然言語ツールを通じてBraze MCPサーバーを使用する際は、以下のポイントを念頭に置いてください。

- 特に複数のワークスペースにアクセスできる場合は、プロンプトでワークスペースを確認してください。
- 分析をリクエストする際は、日付範囲と指標を具体的に指定してください。
- 出力を検証する際は、エージェントにどのツールを使用したか確認するよう依頼してください。
- 影響の大きいレコメンデーションは、Brazeダッシュボードのソースデータと照合してください。

## 使用例 {#usage-examples}

[Braze MCPサーバーのセットアップ]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}が完了したら、自然言語でBrazeとやり取りできます。以下に開始するための例を紹介します。

### どのワークスペースにアクセスできますか？ {#which-workspaces-can-i-access}

{% tabs %}
{% tab プロンプトの例 %}

`Show my available Braze workspaces and tell me which one to use for production campaign analytics.`
{% endtab %}
{% tab 応答の例 %}

`get_workspaces`を呼び出し、以下のワークスペースが見つかりました。

- `Marketing - Production`（`app_group_id`: `YOUR-APP-GROUP-ID-1`）
- `Marketing - Staging`（`app_group_id`: `YOUR-APP-GROUP-ID-2`）

本番キャンペーン分析のプロンプトには`Marketing - Production`を使用してください。
{% endtab %}
{% endtabs %}

詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#workspaces){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#workspaces){% endif %}を参照してください。

### 先週のキャンペーンパフォーマンスを表示する {#show-me-campaign-performance-for-last-week}

{% tabs %}
{% tab プロンプトの例 %}

`In the Marketing - Production workspace, show campaign performance for the last seven days, including sends, opens, clicks, and top performers.`
{% endtab %}
{% tab 応答の例 %}

リクエストされたワークスペースと日付範囲に対して`get_campaign_list`と`get_campaign_dataseries`を使用しました。

概要：

- 総送信数: `YOUR-TEST-SENDS`
- 総開封数: `YOUR-TEST-OPENS`
- 総クリック数: `YOUR-TEST-CLICKS`
- 開封数トップのキャンペーン: `YOUR-TEST-CAMPAIGN-NAME`

必要に応じて、キャンペーン別、チャネル別、または日別に分解できます。
{% endtab %}
{% endtabs %}

詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#campaigns){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#campaigns){% endif %}を参照してください。

### メールテンプレートを作成する {#create-an-email-template}

{% tabs %}
{% tab プロンプトの例 %}

`In the Marketing - Production workspace, create an onboarding email template named "YOUR-TEST-TEMPLATE-NAME".`
{% endtab %}
{% tab 応答の例 %}

`create_email_template`を使用してテンプレートを作成しました。

- **テンプレートID:** `YOUR-TEST-TEMPLATE-ID-123`
- **テンプレート名:** `YOUR-TEST-TEMPLATE-NAME`
- **ワークスペース:** `Marketing - Production`
{% endtab %}
{% endtabs %}

詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates-email){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates-email){% endif %}を参照してください。

## ワークフローの例 {#example-workflows}

以下の例では、複数のツールを組み合わせてタスクを最初から最後まで完了します。

### 複数のワークスペースにまたがるレポート {#report-across-multiple-workspaces}

{% tabs %}
{% tab プロンプトの例 %}

`Get me an analytics report for the past week from my US Prod workspace and my EU Prod workspace, and compare total sends and open rates.`
{% endtab %}
{% tab 応答の例 %}

`get_workspaces`を呼び出してアクセスを確認し、過去7日間について各ワークスペースで`get_campaign_dataseries`を実行しました。

- `US Prod`: `YOUR-TEST-SENDS`件の送信、開封率`YOUR-TEST-OPEN-RATE`
- `EU Prod`: `YOUR-TEST-SENDS`件の送信、開封率`YOUR-TEST-OPEN-RATE`

今週は`US Prod`の方がより多くのメッセージを送信しましたが、`EU Prod`の方が開封率が高い結果となりました。いずれかのワークスペースをキャンペーン別またはチャネル別に分解できます。
{% endtab %}
{% endtabs %}

### ステージングから本番へテンプレートをコピーする {#copy-templates-from-staging-to-production}

{% tabs %}
{% tab プロンプトの例 %}

`Copy the email templates from my Staging workspace to my Production workspace.`
{% endtab %}
{% tab 応答の例 %}

`get_email_templates`と`get_email_template_info`を使用して`Staging`のテンプレートを読み取り、`create_email_template`を使用して`Production`にそれぞれ再作成しました。

- `YOUR-TEST-TEMPLATE-NAME-1`: `Production`に作成済み（`YOUR-TEST-TEMPLATE-ID-1`）
- `YOUR-TEST-TEMPLATE-NAME-2`: `Production`に作成済み（`YOUR-TEST-TEMPLATE-ID-2`）

ドラッグ＆ドロップエディターのテンプレートは`get_email_template_info`でサポートされていないためスキップしました。コピーされたテンプレートを確認する必要があればお知らせください。
{% endtab %}
{% endtabs %}

### 週次キャンペーンヘルスサマリー {#summarize-weekly-campaign-health}

{% tabs %}
{% tab プロンプトの例 %}

`Give me a weekly campaign health summary for the Production workspace.`
{% endtab %}
{% tab 応答の例 %}

`get_campaign_list`と`get_campaign_dataseries`を使用して、`Production`の過去7日間のアクティビティを取得しました。

- 総送信数: `YOUR-TEST-SENDS`
- 開封率: `YOUR-TEST-OPEN-RATE`
- クリック率: `YOUR-TEST-CLICK-RATE`
- コンバージョン数トップのキャンペーン: `YOUR-TEST-CAMPAIGN-NAME`

送信数は前週比で増加しました。チャネル別の内訳を追加したり、エンゲージメントが低下しているキャンペーンをフラグ付けしたりすることもできます。
{% endtab %}
{% endtabs %}

## リモートMCPサーバーの仕組み {#how-the-remote-mcp-server-works}

リクエストを送信すると、裏側でいくつかのステップが実行されます。

1. **クライアントにプロンプトを入力します。** 先週のキャンペーンパフォーマンスを尋ねるなど、自然言語でリクエストを入力します。
2. **クライアントのモデルがツールを選択します。** クライアントのAIモデルがリクエストを解釈し、`get_campaign_list`や`get_campaign_dataseries`などの1つ以上のBrazeツール呼び出しに変換します。
3. **Brazeがツール呼び出しを実行します。** リモートMCPサーバーは、認証済みのOAuthセッションを通じて各ツール呼び出しを受信し、指定されたワークスペースを適用して、対応するBraze REST APIエンドポイントに対して実行します。
4. **Brazeが結果を返します。** サーバーがデータをクライアントに返し、クライアントがフォーマットして表示します。

アクセス権は以下の2つの交差部分で決まります。

- **接続を認可した際に付与されたスコープ**（`mcp:tools`など）。
- **ダッシュボードのユーザー権限。** ダッシュボードでキャンペーンを表示できない場合、エージェントも表示できません。メールテンプレートを作成できる場合、エージェントも作成できます。エージェントがユーザー自身のアクセス権を超えることはありません。

ワークスペースのコンテキストはローカルの設定ファイルに保存されるのではなく、各リクエストとともに渡されるため、1つの接続でアクセスが認可されたすべてのワークスペースを操作できます。

{% multi_lang_include mcp_server/legal_disclaimer.md %}