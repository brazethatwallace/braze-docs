---
nav_title: リファレンス
article_title: エージェントのリファレンス
description: "Brazeエージェントの主要な詳細について説明します。"
page_order: 3
---

# エージェントのリファレンス {#reference-for-agents}

> カスタムエージェントを作成する際、インストラクションや出力スキーマなどの主要な設定の詳細については、この記事を参照してください。ステップバイステップのセットアップについては、[カスタムエージェントの作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)を参照してください。概要については、[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents)および[よくある質問]({{site.baseurl}}/user_guide/brazeai/agents/faq)を参照してください。

## モデル {#models}

エージェントを設定するときに、レスポンスの生成に使用するモデルを選択できます。Brazeパワードモデルの使用と、独自のAPIキーの持ち込みの2つのオプションがあります。

{% alert important %}
Brazeパワードの**Auto**モデルは、カタログ検索やセグメントメンバーシップなどのタスクを実行するのに十分な思考能力を持つモデルに最適化されています。他のモデルを使用する場合は、ご利用のユースケースに適しているかどうかをテストで確認することをお勧めします。速度や能力が異なるモデルに対して、さまざまなレベルの詳細やステップバイステップの思考を与えるために、[インストラクション](#writing-instructions)を調整する必要がある場合があります。
{% endalert %}

### オプション1：Brazeパワードモデルを使用する {#option-1-use-a-braze-powered-model}

これは最もシンプルなオプションで、追加のセットアップは不要です。Brazeは大規模言語モデル（LLM）への直接アクセスを提供します。このオプションを使用するには、Geminiモデルを使用する**Auto**を選択します。

{% alert important %}
エージェント作成時に**Model**ドロップダウンに**Braze Auto**が表示されない場合は、カスタマーサクセスマネージャーに連絡して、Braze Autoモデルの使用資格を取得する方法をご確認ください。
{% endalert %}

### オプション2：独自のAPIキーを持ち込む {#option-2-bring-your-own-api-key}

このオプションでは、OpenAI、Anthropic、Google GeminiなどのプロバイダーにBrazeアカウントを接続できます。LLMプロバイダーから独自のAPIキーを持ち込む場合、トークンコストはBrazeではなくプロバイダーを通じて直接請求されます。

レガシーモデルは数か月後に廃止または非推奨になる可能性があるため、最新のモデルを定期的にテストすることをお勧めします。エージェントをスケールで実行するために、プロバイダーに十分なクレジットがあることを確認してください。また、[通知設定]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences)でエージェントコンソールの通知に登録すると、Brazeがモデルの利用不可を検出した場合やLLMプロバイダーとの課金の問題が発生した場合にアラートを受け取ることができます。

設定方法：

1. **パートナー連携** > **テクノロジーパートナー**に移動し、プロバイダーを見つけます。
2. プロバイダーから取得したAPIキーを入力します。
3. **保存**を選択します。

その後、エージェントに戻ってモデルを選択できます。

Braze提供のLLMを使用する場合、そのモデルのプロバイダーは、お客様とBraze間のデータ処理補遺（DPA）の条件に従い、Brazeのサブプロセッサーとして機能します。独自のAPIキーを持ち込むことを選択した場合、LLMサブスクリプションのプロバイダーは、お客様とBraze間の契約に基づくサードパーティプロバイダーと見なされます。

#### 思考レベル {#thinking-levels}

一部のLLMプロバイダーでは、選択したモデルの思考レベルを調整できます。思考レベルは、モデルが回答する前に使用する思考の範囲を定義します。素早く直接的なレスポンスから、より長い推論の連鎖まで対応します。これはレスポンスの品質、レイテンシー、トークン使用量に影響します。

| レベル | 使用するタイミング |
|-------|-------------|
| **Minimal** | シンプルで明確に定義されたタスク（カタログ検索、単純な分類など）。最速のレスポンスで最低コストです。 |
| **Low** | もう少し推論が必要だが、深い分析は不要なタスク。 |
| **Medium** | 複数ステップまたはニュアンスのあるタスク（複数の入力を分析してアクションを推奨するなど）。 |
| **High** | 複雑な推論、エッジケース、またはモデルにステップを踏んで回答させたい場合。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="思考レベル" }

まず**Minimal**から始めて、エージェントのレスポンスをテストすることをお勧めします。エージェントが正確な回答を提供するのに苦労している場合は、思考レベルを**Low**または**Medium**に調整できます。まれに**High**の思考レベルが必要になることがありますが、このレベルを使用するとトークンコストが高くなり、レスポンス時間が長くなったり、タイムアウトエラーのリスクが高くなったりする可能性があります。エージェントが複数ステップの推論と妥当なレスポンス時間のバランスに苦労している場合は、ユースケースを複数のエージェントに分割し、キャンバスやカタログで連携させることを検討してください。

Brazeは、Connected Contentと同じIP範囲をアウトバウンドLLMコールに使用します。範囲は[Connected Content IP許可リスト]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting)に記載されています。プロバイダーがIP許可リストをサポートしている場合、Brazeのみがキーを使用できるようにこれらの範囲に制限できます。

{% alert important %}
Braze提供のLLMを使用する場合、そのモデルのプロバイダーは、お客様とBraze間のデータ処理補遺（DPA）の条件に従い、Brazeのサブプロセッサーとして機能します。独自のAPIキーを持ち込むことを選択した場合、LLMサブスクリプションのプロバイダーは、お客様とBraze間の契約に基づくサードパーティプロバイダーと見なされます。
{% endalert %}

#### 使用するモデルの決定 {#determine-which-model-to-use}

各LLMプロバイダーは、モデルの能力、コスト、思考レベルの組み合わせがそれぞれ異なります。以下に一般的なガイドラインとベストプラクティスを示します。

- コスト効率を重視する場合は、高コストモデルよりも低トークンコストモデルのテストを優先してください。低コストモデルがユースケースに対応できない場合や、一貫性のない不正確な出力を生成する場合にのみ、高コストモデルに調整してください。
- 速度とパフォーマンス効率を重視する場合は、高い思考レベルよりも低いモデル思考レベルのテストを優先してください。低い思考レベルがユースケースに対応できない場合や、一貫性のない不正確な出力を生成する場合にのみ、高い思考レベルのモデルに調整してください。
- 低コストモデルやモデル思考レベルがユースケースに対応できない場合や、一貫性のない不正確な出力を生成する場合は、高コストモデルや高い思考レベルのモデルへの調整を検討してください。
- テスト中は、信頼性と精度をトークン使用量と呼び出し時間とバランスさせるようにしてください。
- ユースケースごとに最適なモデルと思考レベルが異なる場合があります。タイムアウトなしで一貫した品質を確認するために、徹底的にテストすることをお勧めします。

### 呼び出しフロー制御 {#invocation-flow-controls}

以下の呼び出しフロー制御がワークスペースごとに適用されます。

- **Brazeパワードモデル：** 1分あたり5,000回の呼び出し
- **独自のAPIキーの持ち込み：** 1分あたり5,000回の呼び出し

多くのユーザーが同時にエージェントステップに入ると、Brazeはこれらの制限に従って呼び出しをキューに入れるため、大量送信時には処理に時間がかかる場合があります。

### レート制限エラー {#rate-limit-errors}

LLMプロバイダーが**キャンバスエージェントステップ**でレート制限エラーを返した場合、Brazeはエクスポネンシャルバックオフを使用して、コールが成功するかBrazeが完了不可能と判断するまで継続的にリクエストを再試行します。**カタログエージェント**はレート制限された呼び出しを再試行しません。

キャンバスの再試行が尽きると、**Logs**の詳細パネルに**Error**が表示され、**Output**にプロバイダーメッセージ（`Rate limit exceeded`など）が表示されます。最初の呼び出しの最終的な成功・失敗にかかわらず、再試行はログに表示されます。特定のユーザーについて、成功するまでに4回の再試行が必要だった場合、ユーザーIDで検索すると**Logs**に5件すべて（オリジナルと4回の再試行）が表示され、オリジナルと最初の3回の再試行には`Rate limit exceeded`の**Error**が表示されます。

![Outputフィールドにレート制限超過エラーが表示されているエージェントコンソールのログ詳細。]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## インストラクションの記述 {#writing-instructions}

インストラクションは、エージェントに与えるルールまたはガイドライン（システムプロンプト）です。エージェントが実行されるたびにどのように動作するかを定義します。システムインストラクションは最大25 KBです。

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)を使用して[開始テンプレート]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)でエージェントを構築した場合は、事前入力されたインストラクションを確認し、必要に応じて編集してください。

プロンプト作成を始めるための一般的なベストプラクティスを以下に示します。

1. ゴールを念頭に置いて始めましょう。まず目標を述べます。
2. モデルにロールまたはペルソナを与えます（「You are a ...」）。
3. 明確なコンテキストと制約を設定します（オーディエンス、長さ、トーン、フォーマット）。
4. 構造を求めます（「Return JSON/bullet list/table...」）。
5. 説明するのではなく、示しましょう。質の高い例をいくつか含めます。
6. 複雑なタスクを順序付けられたステップに分割します（「ステップ1... ステップ2...」）。
7. 推論を促します（「内部的にステップを考え、簡潔な最終回答を提供してください」または「判断を簡潔に説明してください」）。
8. パイロット、検査、反復を行います。小さな調整が大きな品質向上につながります。
9. エッジケースを処理し、ガードレールを追加し、拒否のインストラクションを追加します。
10. 再利用とスケーリングのために、うまくいったことを測定し文書化します。

### 例 {#examples}

エージェントコンソールの開始設定については、[Operatorで構築されたエージェントテンプレート]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)を参照してください。

コピーまたはアレンジできる完全なインストラクション例については、[Brazeエージェントのユースケースライブラリ]({{site.baseurl}}/user_guide/brazeai/agents/examples)を参照してください。

| 例 | カテゴリ | エージェントタイプ | 内容 |
| --- | --- | --- | --- |
| [ユーザーのコンテキストに基づいてパーソナライズされたメッセージを作成する]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | コンテンツ生成 | キャンバスステップエージェント | 検索したが予約しなかったユーザー向けに、メールの件名/プリヘッダーとプッシュのタイトル/本文を連携して生成します。 |
| [ユーザーフィードバックを分析して次のステップを決定する]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | データ標準化 | キャンバスステップエージェント | 旅行後のアンケートのセンチメントとトピックを分類し、CRMの次のステップを推奨します。 |
| [既存の属性からユーザーを興味バケットに分類する]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | アフィニティエージェント | キャンバスステップエージェント | 属性と高インテントシグナルからユーザーを興味バケットに分類し、最適な次のエクスペリエンスまたはアイテムを推奨します。 |
| [最近の行動から最も関連性の高いキャンバスパスにユーザーをルーティングする]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | アフィニティエージェント | キャンバスステップエージェント | 最近の行動からモチベーションを推測し、ユーザーの次のキャンバスステップに最適なルートキーを返します。 |
| [リアルタイムの高インテントアクションからユーザーを興味カテゴリに割り当てる]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | アフィニティエージェント | キャンバスステップエージェント | 高インテントアクションから興味カテゴリを割り当て、最適な次のエクスペリエンスまたはアイテムを推奨します。 |
| [インバウンドメッセージをオプトアウトインテントで分類する]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | 分類とルーティング | キャンバスステップエージェント | メッセージがオプトアウトリクエストかどうかを示す厳密なブール値を返します。 |
| [インバウンドメッセージをオートメーション用の構造化データに標準化する]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | データ標準化 | キャンバスステップエージェント | インバウンドSMSまたはチャットを、ダウンストリームオートメーション用の構造化されたインテント、エンティティ、コンプライアンスフラグに正規化します。 |
| [ブランドガイドラインに沿った高コンバージョンの説明文を作成する]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | コンテンツ生成 | カタログエージェント | 各カタログ行に対して、短くブランドに沿った説明文を生成します。 |
| [地域で使用される言語に基づいて翻訳を提供する]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | カタログエンリッチメント | カタログエージェント | ロケールと文字数制限に応じてUIおよびマーケティング文字列をローカライズします。 |
| [カタログアイテムを説明文、カテゴリ、タグでエンリッチする]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | カタログエンリッチメント | カタログエージェント | 既存のカタログアイテムデータから、強化された説明文、カテゴリ、タグを生成します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="例の概要" }

### Liquidの使用 {#using-liquid}

エージェントのインストラクションに[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を含めると、レスポンスにパーソナライゼーションのレイヤーを追加できます。エージェントが取得する正確なLiquid変数を指定し、プロンプトのコンテキストに含めることができます。たとえば、「名」を明示的に記述する代わりに、Liquidスニペット{% raw %}`{{${first_name}}}`{% endraw %}を使用できます。

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

**エージェントコンソール**の**Logs**セクションで、エージェントの入出力の詳細を確認し、Liquidからどのような値がレンダリングされるかを理解できます。

![インストラクションにLiquidを含むエージェントの詳細。]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

カタログエージェントの場合は、JSONスキーマではなく**Output**セクションの**Fields**を使用します。ただし、インストラクション内でモデルにフィールド名に一致するキーバリュー出力を求めることは可能です。

プロンプトのベストプラクティスの詳細については、以下のモデルプロバイダーのガイドを参照してください。

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## 出力 {#outputs}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)を使用して[開始テンプレート]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)でエージェントを構築した場合は、事前入力された出力スキーマを確認し、必要に応じて編集してください。

### 基本スキーマ {#basic-schemas}

基本スキーマは、エージェントが返すシンプルな出力です。文字列、数値、ブール値、文字列の配列、または数値の配列を指定できます。

たとえば、製品を受け取った後の顧客満足度を判定するために、シンプルなフィードバック調査からユーザーのセンチメントスコアを収集したい場合、出力フォーマットを構造化するために基本スキーマとして**Number**を選択できます。

{% alert important %}
配列はキャンバスエージェントでのみ使用可能で、カタログエージェントでは使用できません。
{% endalert %}

![基本スキーマとしてNumberが選択されたエージェントコンソール。]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### 高度なスキーマ {#advanced-schemas}

高度なスキーマオプションには、フィールドの手動構造化またはJSONの使用が含まれます。

- **Fields：** 一貫して使用できるエージェント出力を強制するノーコードの方法です。
- **JSON：** 正確な出力フォーマットを作成するコードアプローチで、JSONスキーマ内に変数やオブジェクトをネストできます。キャンバスエージェントでのみ使用可能で、カタログエージェントでは使用できません。

エージェントに単一値の出力ではなく、構造化された方法で定義された複数の値を持つデータ構造を返させたい場合は、高度なスキーマの使用をお勧めします。これにより、出力が一貫したコンテキスト変数としてより適切にフォーマットされます。

### フォールバック出力 {#fallback-output}

フォールバック値は**キャンバスステップエージェント**でのみ使用可能です。キャンバスエージェントのエージェントコンソールの**Output**セクションで、呼び出しが失敗した場合にBrazeが使用する値を定義できます。

**JSON**スキーマの場合、Brazeはスキーマを読み取り、各プロパティの入力フィールドを生成するため、キーごとにフォールバック値を設定できます。**Fields**スキーマの場合、各フィールドにフォールバック値を入力します。基本スキーマの場合、単一のフォールバック値を入力します。キャンバスエージェントはフォールバック値でLiquidをサポートしています。

セットアップ手順については、[フォールバック値の設定]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values)を参照してください。キャンバスでのランタイム動作については、[エラー処理とフォールバック動作]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior)を参照してください。

たとえば、ユーザーが送信したフォームに基づいてサンプル旅行プランを作成するエージェント内で出力フォーマットを使用できます。出力フォーマットにより、すべてのエージェントレスポンスが`tripStartDate`、`tripEndDate`、`destination`の値を含んで返されるように定義できます。これらの各値はコンテキスト変数から抽出し、Liquidを使用してメッセージステップに配置してパーソナライゼーションに活用できます。

{% tabs %}
{% tab Fields %}

レストランの最新アイスクリームフレーバーを推薦する可能性を判定するために、シンプルなフィードバック調査へのレスポンスをフォーマットしたい場合、出力フォーマットを構造化するために以下のフィールドを設定できます。

| フィールド名 | 値 |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="高度なスキーマ" }

![likelihood score、explanation、confidence scoreの3つの出力フィールドを表示するエージェントコンソール。]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSONスキーマ %}

レストランチェーンでの最新の食事体験に関するユーザーフィードバックを収集したい場合、出力フォーマットとして**JSON Schema**を選択し、以下のJSONを挿入して、センチメント変数と理由変数を含むデータオブジェクトを返すことができます。

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

## カタログとフィールド {#catalogs-and-fields}

エージェントが参照する特定のカタログを選択し、製品やその他の関連する非ユーザーデータを理解するために必要なコンテキストをエージェントに提供します。エージェントはツールを使用して関連するアイテムのみを検索し、トークン使用量を最小限に抑えるためにそれらのみをLLMに送信します。

![エージェントが検索するために選択された「restaurants」カタログと「Loyalty_Program」列。]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

カタログエージェントをカタログフィールドにデプロイする場合、必須入力コントロールを有効にし、エージェントが呼び出される前に**実行に必要な**選択済み列を選択します。エージェントは、必須列のいずれかが空白または欠落している場合にのみ行をスキップします。たとえば、まだ入力されていない`gender`フィールドなどです。選択済み列はデフォルトで必須として開始されますが、実行をブロックせずに空でもよい列を削除できます。これにより、不完全なデータでのトークンの無駄遣いを防ぎます。

カタログエージェントは、入力フィールドが互いに依存している場合に列の順序も尊重します。列Dが列BとCから生成される場合、エージェントはBとCにその行の値が含まれるまで列Dを実行しません。

デプロイシナリオと例については、[カタログエージェントの使用]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents)および[カタログエージェントのベストプラクティス]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices)を参照してください。

## セグメントメンバーシップのコンテキスト {#segment-membership-context}

エージェントがキャンバスで使用されている場合に、各ユーザーのセグメントメンバーシップを相互参照するためのセグメントを最大5つまで選択できます。たとえば、エージェントが「Loyalty Users」セグメントのメンバーシップを選択しており、そのエージェントがキャンバスで使用されているとします。ユーザーがエージェントステップに入ると、エージェントは各ユーザーがエージェントコンソールで指定した各セグメントのメンバーであるかどうかを相互参照し、各ユーザーのメンバーシップ（または非メンバーシップ）をLLMのコンテキストとして使用できます。

![エージェントメンバーシップアクセス用に選択された「Loyalty Users」セグメント。]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## ブランド・ガイドライン {#brand-guidelines}

エージェントがレスポンスで遵守する[ブランド・ガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)を選択できます。たとえば、エージェントがジムのメンバーシップへの登録を促すSMSコピーを生成する場合、このフィールドを使用して、事前定義された大胆でモチベーショナルなガイドラインを参照できます。

## ユーザー固有のインタラクション履歴 {#user-history}

ユーザーのインタラクションデータには、最近のキャンペーンおよびキャンバスの開封、クリック、コンバージョンデータが含まれます。たとえば、キャンバスで評価される際にエージェントが参照するコンテキストとしてこのデータを含めることができます。ユーザー固有のインタラクション履歴は、パーソナライズされたメッセージコピーを作成するエージェントに影響を与えるのにも役立ちます。

## エージェントの複製 {#duplicate-agents}

エージェントの改善や反復をテストするには、エージェントを複製してから変更を適用し、オリジナルと比較できます。また、エージェントの複製をバージョン管理として扱い、エージェントの詳細の変化やメッセージングへの影響を追跡することもできます。エージェントを複製するには：

1. エージェントの行にカーソルを合わせ、<i class="fas fa-ellipsis-vertical" aria-label="その他のオプション"></i>メニューを選択します。
2. **複製**を選択します。

## エージェントのアーカイブ {#archive-agents}

カスタムエージェントをさらに作成すると、アクティブに使用されていないエージェントをアーカイブすることで**エージェント管理**ページを整理できます。エージェントをアーカイブするには：

1. エージェントの行にカーソルを合わせ、<i class="fas fa-ellipsis-vertical" aria-label="その他のオプション"></i>メニューを選択します。
2. **アーカイブ**を選択します。