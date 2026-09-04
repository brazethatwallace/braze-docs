## 免責事項 {#legal-disclaimer}
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

### 指示と応答の処理方法 {#how-instructions-and-responses-are-handled}

Braze MCPサーバーは、Claude、ChatGPT、Copilot、Gemini CLI、Codex、CursorなどのサードパーティプロバイダーのMCPクライアントから、そのプロバイダーの基盤AIモデルが生成した指示をそのまま受け取ります。自然言語でリクエストを入力すると、AIモデルがリクエストを解釈し、Brazeへの1つ以上の具体的なツール呼び出しに変換します。Brazeは送信されたツール呼び出しをそのまま受信して実行します。Brazeはお客様の元の自然言語プロンプトを参照することはできず、生成されたツール呼び出しがお客様の意図したリクエストを完全かつ正確に反映しているかどうかを検証することもできません。

Brazeがデータや結果を返す際、その応答はサードパーティプロバイダーのMCPクライアントに送信され、クライアント側で解釈、フォーマット、表示が行われます。Brazeは、AIモデルが返された情報をどのように表示、要約、または説明するかを制御しません。

Brazeは、サードパーティプロバイダーのMCPクライアントによって生成された指示、またはそれを通じて伝達された応答について責任を負いません。サードパーティプロバイダーのMCPクライアントがアクションの自動実装のための「自動モード」を提供している場合、Brazeはその使用を推奨しません。AIが生成した要約はBrazeダッシュボードのソースデータと照合して確認し、AIが提案するアクションはサードパーティプロバイダーのMCPクライアントを通じて実装する前に必ず確認してください。