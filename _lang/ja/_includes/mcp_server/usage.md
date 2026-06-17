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
**Example prompt:** `What are my available Braze functions?`

**Example response:** Called `list_functions` and returned categories like Campaign, Canvas, Templates, and Content Blocks with sample functions such as `get_canvas_list` and `create_email_template`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`

**Example response:** Queried `list_functions`, confirmed available function groups, and listed examples including `get_canvas_details` and `update_content_block`.
{% endtab %}
{% endtabs %}

`list_functions`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}を参照してください。

### キャンバス IDの詳細を取得する {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Used `get_canvas_details` and returned sample metadata (status, channel, created/updated time) for `YOUR-TEST-CANVAS-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Returned Canvas and message details with dummy values like `YOUR-TEST-MESSAGE-ID-123` and `YOUR-TEST-SUBJECT-LINE`.
{% endtab %}
{% endtabs %}

`get_canvas_details`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}を参照してください。

### 最近のキャンバスを表示する {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Called `get_canvas_list` and returned recent items such as `YOUR-TEST-CANVAS-ALPHA` with IDs like `YOUR-TEST-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Listed recently edited Canvases with sample values for name, last edited time, ID, and tags.
{% endtab %}
{% endtabs %}

`get_canvas_list`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}を参照してください。

### メールテンプレートを作成する {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Create an email template named "YOUR-TEST-TEMPLATE-NAME".`

**Example response:** Created a template via `create_email_template` and returned `YOUR-TEST-TEMPLATE-ID-123`.
{% endtab %}
{% endtabs %}

`create_email_template`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}を参照してください。

### コンテンツブロックを更新する {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123".`

**Example response:** Updated the block with `update_content_block` and confirmed `YOUR-TEST-CONTENT-BLOCK-ID-123` moved to a new version.
{% endtab %}
{% endtabs %}

`update_content_block`関数の詳細については、[利用可能なAPI関数]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}を参照してください。

{% multi_lang_include mcp_server/legal_disclaimer.md %}