---
nav_title: LLMで構築する
article_title: LLMを用いた構築
page_order: 4
description: "Brazeのドキュメントを活用してAIコーディングアシスタントを使い、SDK統合ワークフローを加速させる方法を学びます。"
platform:
  - Web
  - React Native
---

# LLMを用いた構築 {#building-with-an-llm}

> AIコーディングアシスタントを使って、Brazeの統合ワークフローを加速させましょう。Context7を介してIDEをBraze Docs MCPサーバーに接続し、開発環境内で正確かつ最新のSDKガイダンスを直接入手できます。

AIコーディングアシスタントは、統合コードの記述や問題のトラブルシューティング、Braze SDKの機能探索を支援できます。ただし、適切なコンテキストが与えられている場合に限ります。Braze Docs MCPサーバーは、AIアシスタントにBrazeドキュメントへの直接アクセスを提供するため、最新のSDKリファレンスに基づいて正確なコードスニペットを生成し、技術的な質問に回答できます。

## Braze Docs MCPへの接続 {#connecting-to-the-braze-docs-mcp}

[Context7](https://context7.com/braze-inc/braze-docs)は、AIアシスタントとBrazeドキュメントライブラリーをつなぐ橋渡し役です。IDEのMCP設定にContext7を追加すると、AIアシスタントがBrazeの全ドキュメントセットにクエリを実行し、関連するSDKリファレンス、コード例、統合ガイドをオンデマンドで取得できるようになります。

### Context7の設定 {#setting-up-context7}

Context7を通じてAIアシスタントをBraze Docs MCPに接続するには、IDEの`mcp.json`ファイルに以下の設定を追加します。

{% tabs %}
{% tab Cursor %}
[Cursor](https://cursor.com/)で、**Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP**へ移動し、以下のスニペットを追加します。

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

設定を保存し、Cursorを再起動します。プロンプトに`use context7`を含めることで、AIアシスタントがContext7経由でBrazeドキュメントにアクセスできるようになります。
{% endtab %}

{% tab Claude %}
Claude Desktopで、**Settings** > **Developer** > **Edit Config**へ移動し、`claude_desktop_config.json`ファイルに以下を追加します。

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

設定を保存し、Claude Desktopを再起動します。
{% endtab %}

{% tab VS Code %}
VS Codeの`settings.json`または`.vscode/mcp.json`ファイルに以下を追加します。

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

設定を保存し、VS Codeを再起動します。
{% endtab %}
{% endtabs %}

{% alert note %}
Context7は[Braze MCPサーバー]({{site.baseurl}}/developer_guide/mcp_server)とは異なります。Context7はAIアシスタントに**Brazeドキュメント**へのアクセスを提供し、Braze MCPサーバーは**Brazeワークスペースデータ**（Campaigns、Segments、分析など）への読み取り専用アクセスを提供します。両方を併用することで、より充実したAI支援開発体験を得られます。
{% endalert %}

## Braze SDK開発向けのプロンプト作成 {#writing-prompts-for-braze-sdk-development}

Context7を設定した後、プロンプトに`use context7`を含めることで、AIアシスタントにBrazeドキュメントをコンテキストとして取り込むよう指示します。以下の例は、一般的なSDKタスクに対して効果的なプロンプトを作成する方法を示しています。

### React Native SDK {#react-native-sdk}

これらのプロンプトは、[Braze React Native SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native)の一般的な統合タスクを示しています。

#### SDKの初期化 {#initializing-the-sdk}

```text
Using the Braze React Native SDK, show me how to initialize the SDK
in my App.tsx with an API key and custom endpoint. Include the
configuration for automatic session tracking. Use context7.
```

#### プロパティ付きカスタムイベントの記録 {#logging-custom-events-with-properties}

```text
I need to track user activity in my React Native app using the Braze
React Native SDK. Show me how to log a custom event called
"ProductViewed" with properties for product_id, category, and price.
Use context7.
```

#### プッシュ通知の設定 {#setting-up-push-notifications}

```text
Using the Braze React Native SDK, walk me through requesting push
notification permissions on both iOS and Android 13+. Include the
code for registering the push token with Braze. Use context7.
```

#### アプリ内メッセージの処理 {#handling-in-app-messages}

```text
Show me how to subscribe to in-app messages using the Braze React
Native SDK, including how to log impressions and button clicks
programmatically. Use context7.
```

### Web SDK {#web-sdk}

これらのプロンプトは、[Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)の一般的な統合タスクを示しています。

#### SDKの初期化

```text
Using the Braze Web SDK, show me how to initialize the SDK with
braze.initialize(), including the API key, base URL, and options
for enabling logging and automatic in-app message display.
Use context7.
```

#### カスタムイベントと購入のトラッキング {#tracking-custom-events-and-purchases}

```text
Using the Braze Web SDK, create a JavaScript module that logs a
custom event called "VideoPlayed" with properties for video_id,
duration_seconds, and completion_percentage. Also show how to log
a purchase with product ID, price, currency code, and quantity.
Use context7.
```

#### Webプッシュの登録 {#registering-for-web-push}

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to
register a user for web push notifications after they click a
"Subscribe to updates" button. Include the service worker setup.
Use context7.
```

#### ユーザー属性の管理 {#managing-user-attributes}

```text
Using the Braze Web SDK, show me how to set standard user attributes
(first name, email, country) and custom user attributes (favorite_genre,
subscription_tier) for the current user. Use context7.
```

## プレーンテキストドキュメント {#plain-text-documentation}

Braze開発者ガイドのドキュメントは、AIツールやLLM向けに最適化されたプレーンテキストファイルとしてアクセスできます。これらのファイルは、HTMLレンダリングのオーバーヘッドなしにAIアシスタントが解析・理解できる形式でBrazeドキュメントを提供します。

| ファイル | 説明 |
|------|-------------|
| [llms.txt]({{site.baseurl}}/developer_guide/llms.txt) | Braze開発者向けドキュメントページのタイトルと説明のインデックスです。利用可能なドキュメントを見つけるための出発点として使用できます。 |
| [llms-full.txt]({{site.baseurl}}/developer_guide/llms-full.txt) | Braze開発者向けドキュメントの完全版を、LLMが利用しやすい形式でフォーマットした単一のプレーンテキストファイルです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プレーンテキストドキュメント" }

これらのファイルは[llms.txt標準](https://llmstxt.org/)に準拠しています。これはAIツールがドキュメントにアクセスしやすくするための新しい規約です。プロンプト内でこれらのファイルを直接参照したり、内容をLLMに貼り付けてコンテキストとして使用したりできます。