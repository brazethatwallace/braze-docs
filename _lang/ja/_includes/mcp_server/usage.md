# Braze MCPサーバーを使用する {#using-the-braze-mcp-server}

> ClaudeやCursorのような自然言語ツールを使って、Brazeデータとやり取りする方法を学習しましょう。より一般的な情報については、[Braze MCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}を参照してください。

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件 {#prerequisites}

この機能を使用する前に、[Braze MCPサーバーのセットアップ]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}を完了する必要があります。

## ベストプラクティス {#best-practices}

ClaudeやCursorのような自然言語ツールを通じてBraze MCPサーバーを使用する際は、最良の結果を得るために以下のポイントを念頭に置いてください。

- LLMは間違いを犯すことがあるため、回答は必ずダブルチェックしてください。
- データ分析では、必要な時間範囲を明確にしてください。短い範囲の方が、より正確な結果を得られることが多いです。
- 正確な[Brazeの用語](https://www.braze.com/resources/articles/glossary)を使用して、LLMが正しい関数を呼び出せるようにしましょう。
- 結果が不完全に見える場合は、LLMに続行またはさらに掘り下げるよう促してください。
- 創造的なプロンプトを試してみましょう！MCPクライアントによっては、CSVやその他の便利なファイルをエクスポートできる場合があります。

## 使用例 {#usage-examples}

[Braze MCPサーバーのセットアップ]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}が完了したら、ClaudeやCursorのようなツールを使って自然言語でBrazeとやり取りできます。以下にいくつかの例を紹介します。

### 利用可能なBraze関数は何ですか？ {#what-are-my-available-braze-functions}

{% tabs %}
{% tab Claude %}
**プロンプトの例**

`What are my available Braze functions?`

**応答の例**

`list_functions`を使ってBraze MCPサーバーを確認したところ、38個の利用可能なAPI関数が見つかりました。

カテゴリ別の例をいくつか紹介します。

- **キャンペーンの分析と管理**
  - `get_campaign_dataseries`
  - `get_campaign_details`
  - `get_campaign_list`
- **キャンバスの分析と管理**
  - `get_canvas_data_series`
  - `get_canvas_data_summary`
  - `get_canvas_list`
  - `get_canvas_details`
- **テンプレート**
  - `create_email_template`
- **コンテンツブロック**
  - `create_content_block`
  - `get_content_blocks`
  - `get_content_block_info`
  - `update_content_block`
{% endtab %}

{% tab Cursor %}
**プロンプトの例**

`What are my available Braze functions?`

**応答の例**

Braze MCPサーバーを使って利用可能な関数を確認します。

- `list_functions`を呼び出しました

その結果に基づくと、以下のようなカテゴリに整理された38個のBraze API関数があります。

- キャンペーンの分析と管理
- キャンバスの分析と管理
- テンプレート
- コンテンツブロック

関数の例：

- `get_campaign_list`
- `get_canvas_list`
- `get_canvas_details`
- `create_email_template`
- `update_content_block`
{% endtab %}
{% endtabs %}

`list_functions`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}を参照してください。

### キャンバス IDの詳細を取得する {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**プロンプトの例**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**応答の例**

`get_canvas_details`を使って`YOUR-TEST-CANVAS-ID-123`の詳細を取得しました。

- **キャンバス名:** `YOUR-TEST-CANVAS-NAME`
- **ID:** `YOUR-TEST-CANVAS-ID-123`
- **ステータス:** 下書き（無効）
- **作成日時:** 2026年1月15日 10:30 AM UTC
- **最終更新日時:** 2026年1月16日 02:45 PM UTC
- **スケジュールタイプ:** 時間ベース
- **プライマリチャネル:** メール

メールメッセージの詳細：

- **件名:** `YOUR-TEST-SUBJECT-LINE`
- **送信元:** `YOUR-TEST-SENDER@example.com`
- **メッセージID:** `YOUR-TEST-MESSAGE-ID-123`
{% endtab %}

{% tab Cursor %}
**プロンプトの例**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**応答の例**

`get_canvas_details`を使ってこのキャンバスを取得しました。

- **キャンバス ID:** `YOUR-TEST-CANVAS-ID-123`
- **キャンバス名:** `YOUR-TEST-CANVAS-NAME`
- **ステータス:** 下書き
- **チャネル:** メール
- **メッセージID:** `YOUR-TEST-MESSAGE-ID-123`

メールコンテンツの概要：

1. ブランド画像を含むヘッダーセクション
2. メインの見出しセクション
3. CTAボタンを含むヒーローセクション
4. サポートコンテンツを含む機能セクション
{% endtab %}
{% endtabs %}

`get_canvas_details`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}を参照してください。

### 最近のキャンバスを表示する {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**プロンプトの例**

`Show me my recent キャンバス`

**応答の例**

`list_functions`で利用可能なツールを確認し、`get_canvas_list`を使って最近編集されたキャンバスを取得しました。

最近のキャンバス：

1. **YOUR-TEST-CANVAS-ALPHA**
   - ID: `YOUR-TEST-ID-123`
   - 最終編集日時: 2026年1月16日 02:45 PM UTC
2. **YOUR-TEST-CANVAS-BETA**
   - ID: `YOUR-TEST-ID-456`
   - 最終編集日時: 2026年1月15日 11:10 AM UTC
3. **YOUR-TEST-CANVAS-GAMMA**
   - ID: `YOUR-TEST-ID-789`
   - 最終編集日時: 2026年1月14日 08:25 PM UTC
{% endtab %}

{% tab Cursor %}
**プロンプトの例**

`Show me my recent キャンバス`

**応答の例**

Braze MCPサーバーから最近のキャンバス一覧を取得します。

- `list_functions`を呼び出しました
- `get_canvas_list`を呼び出しました

最近のキャンバス（最終編集日時順）：

- **キャンバス名:** `YOUR-TEST-CANVAS-ALPHA`
  - **最終編集日時:** 2026年1月16日 02:45 PM UTC
  - **キャンバス ID:** `YOUR-TEST-ID-123`
  - **タグ:** `lifecycle`, `email`
- **キャンバス名:** `YOUR-TEST-CANVAS-BETA`
  - **最終編集日時:** 2026年1月15日 11:10 AM UTC
  - **キャンバス ID:** `YOUR-TEST-ID-456`
  - **タグ:** `promo`
{% endtab %}
{% endtabs %}

`get_canvas_list`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}を参照してください。

### メールテンプレートを作成する {#create-an-email-template}

{% tabs %}
{% tab Claude %}
**プロンプトの例**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**応答の例**

`create_email_template`を使ってテンプレートを作成しました。

- **テンプレート名:** `YOUR-TEST-TEMPLATE-NAME`
- **テンプレートID:** `YOUR-TEST-TEMPLATE-ID-123`
- **件名:** `YOUR-TEST-SUBJECT-LINE`
- **プリヘッダー:** `YOUR-TEST-PREHEADER`
- **作成日時:** 2026年1月16日 03:10 PM UTC

キャンペーンやキャンバスを作成・更新する際に`YOUR-TEST-TEMPLATE-ID-123`を参照できます。
{% endtab %}

{% tab Cursor %}
**プロンプトの例**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**応答の例**

`create_email_template`を使って新しいテンプレートを正常に作成しました。

- **テンプレートID:** `YOUR-TEST-TEMPLATE-ID-123`
- **テンプレート名:** `YOUR-TEST-TEMPLATE-NAME`
- **件名:** `YOUR-TEST-SUBJECT-LINE`
- **説明:** `Onboarding lifecycle template`

ご希望であれば、このテンプレート用のスターターHTMLボディとプレーンテキストのフォールバックも生成できます。
{% endtab %}
{% endtabs %}

`create_email_template`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}を参照してください。

### コンテンツブロックを更新する {#update-a-content-block}

{% tabs %}
{% tab Claude %}
**プロンプトの例**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**応答の例**

`update_content_block`を使ってコンテンツブロックを更新しました。

- **コンテンツブロックID:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **名前:** `YOUR-TEST-CONTENT-BLOCK-NAME`
- **ステータス:** 更新済み
- **更新日時:** 2026年1月16日 03:25 PM UTC

プレビュー：

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}

{% tab Cursor %}
**プロンプトの例**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**応答の例**

`update_content_block`を実行し、更新が完了したことを確認しました。

- **コンテンツブロックID:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **前のバージョン:** `v1`
- **現在のバージョン:** `v2`
- **最終更新日時:** 2026年1月16日 03:25 PM UTC

更新されたコンテンツのプレビュー：

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}
{% endtabs %}

`update_content_block`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}を参照してください。

{% multi_lang_include mcp_server/legal_disclaimer.md %}