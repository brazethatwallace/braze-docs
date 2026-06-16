---
nav_title: エージェント
article_title: エージェントステップ
alias: /agent_step/
page_order: 2
page_type: reference
description: "このリファレンス記事では、Canvasのエージェントステップを使用して、コンテンツを生成したり、リアルタイムでインテリジェントな判断を行ったりする方法について説明します。"
tool: Canvas
toc_headers: h2
---

# エージェントステップ {#agent-step}

> エージェントステップを使用すると、AIを活用した意思決定やコンテンツ生成をCanvasワークフローに直接組み込むことができます。一般的な情報については、[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents/)を参照してください。

![Canvasのユーザージャーニーにおけるエージェントステップ。]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## 前提条件 {#prerequisites}

エージェントステップは、[Canvasコンテキスト変数]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)を使用して関連するコンテキストを取り込み、Canvasで活用できる変数を出力します。

## 仕組み {#how-it-works}

ユーザーがCanvasのエージェントステップに到達すると、Brazeは設定した入力データ（完全なコンテキストまたは選択したフィールド）を選択したエージェントに送信します。エージェントはそのモデルと指示を使用して入力を処理し、出力を返します。その出力は、ステップで定義した出力変数に保存されます。

この変数は主に3つの方法で使用できます。

- **意思決定:** エージェントの応答に基づいて、ユーザーを異なるCanvasパスにルーティングします。たとえば、リードスコアリングエージェントが「Sales Ready」、「Marketing Qualified」、「Disqualified」のリードカテゴリを返す場合があります。この割り当てを使用して、「Sales Ready」リードに対してSlackアラートや自動メッセージをトリガーし、「Disqualified」リードをジャーニーから除外できます。
- **パーソナライゼーション:** エージェントの応答をメッセージに直接挿入します。たとえば、エージェントが顧客のフィードバックを分析し、顧客のコメントに言及して解決策を提案する共感的なフォローアップメールを生成できます。
- **ユーザーデータの処理:** ユーザーデータを分析・標準化し、ユーザープロファイルに保存するか、Webhookを使用して送信します。たとえば、エージェントがセンチメントスコアや製品アフィニティの割り当てを返すことができます。そのデータをユーザープロファイルに保存して、将来の利用に活用できます。

## エージェントステップの作成 {#creating-an-agent-step}

### ステップ 1: ステップを追加する {#step-1-add-a-step}

サイドバーから**エージェント**コンポーネントをドラッグ＆ドロップするか、ステップの下部にある <i class="fas fa-plus-circle"></i> プラスボタンを選択して**エージェント**を選択します。

### ステップ 2: エージェントを選択する {#step-2-choose-your-agent}

このステップでデータを処理するエージェントを選択します。既存のエージェントから選択してください。セットアップのガイダンスについては、[カスタムエージェントの作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)を参照してください。

### ステップ 3: エージェントの出力を設定する {#define-the-output-variable}

エージェントの出力は「出力変数」と呼ばれ、簡単にアクセスできるように[コンテキスト変数]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#context-variable-types)に保存されます。出力変数を定義するには、変数に名前を付けます。

出力変数のデータタイプは[エージェントコンソール]({{site.baseurl}}/user_guide/brazeai/agents/)から設定されます。エージェントの出力は、文字列、数値、ブール値、またはオブジェクトとして保存できます。これにより、Canvasでのテキストパーソナライゼーションと条件ロジックの両方に柔軟に対応できます。各タイプの一般的な用途は以下のとおりです。

| データタイプ | 一般的な用途 |
| --- | --- |
| 文字列 | メッセージのパーソナライゼーション（件名、コピー、応答） |
| 数値 | スコアリング、しきい値、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/)でのルーティング |
| ブール値 | [条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)でのYes/No分岐 |
| オブジェクト | 単一のLLM呼び出しで、予測可能なデータ構造内の上記データタイプを1つ以上活用 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 3: エージェントの出力を設定する" }

出力変数は、コンテキスト変数と同じテンプレート構文を使用してCanvas全体で使用できます。**Context Variable** Segmentフィルターを使用するか、Liquidを使用してエージェントの応答を直接テンプレート化します: {% raw %}`{{context.${response_variable_name}}}`{% endraw %}。

オブジェクト出力変数から特定のプロパティを使用するには、Liquidでドット記法を使用してそのプロパティにアクセスします: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![変数「agent_output」のオブジェクトデータタイプ出力を持つBody HTML Writerのエージェントステップ。]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### ステップ 4: 追加のコンテキストを追加する（オプション） {#step-4-add-any-additional-context-optional}

エージェントステップの実行時に参照する追加のコンテキスト値を含めることができます。Canvasで通常使用する任意のLiquidテンプレート値を入力できます。

{% alert note %}
エージェントは**Instructions**セクションで設定されたコンテキストを自動的に受信しています。そこで既に設定されたLiquid変数をここで再入力する必要はありません。
{% endalert %}

![Liquidを使用してエージェントステップに追加のコンテキストを追加するオプション。]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### ステップ 5: エージェントをテストする {#step-5-test-the-agent}

エージェントステップを設定した後、このステップの出力をテストしてプレビューできます。

![ランダムなユーザーとしてエージェントの出力をプレビューします。]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## エラー処理 {#error-handling}

Brazeがエージェントの失敗、レート制限エラー、呼び出しフロー制御をどのように処理するかについては、Brazeエージェントの[エラー処理]({{site.baseurl}}/user_guide/brazeai/agents/#error-handling)を参照してください。

- エージェントが何らかの理由（タイムアウトエラーや無効なAPIキーなど）で失敗した場合、出力変数は`null`に設定されます。
    - エージェントが1日の呼び出し上限に達した場合、出力変数は`null`に設定されます。
- エラーに対するバッファとして[デフォルトのLiquid値]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/)を使用してください。たとえば、**Add Personalization**モーダルで、{% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %}や{% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}のようなデフォルトのLiquid値を入力できます。
- 同一の入力に対する応答はキャッシュされ、数分以内の同一の呼び出しに再利用される場合があります。
    - キャッシュされた値を使用する応答も、合計および1日の呼び出し回数にカウントされます。
- エージェントステップは、大量のユーザーバッチの処理に時間がかかる場合があります。Brazeは[呼び出しフロー制御]({{site.baseurl}}/user_guide/brazeai/agents/reference/#invocation-flow-controls)に従って呼び出しをキューに入れるため、大量送信時にユーザーが保留中になる場合があります。ログを確認して呼び出しが行われていることを確認してください。

## 分析 {#analytics}

エージェントステップのパフォーマンスを追跡するには、以下の指標を参照してください。

| 指標 | 説明 |
| --- | --- |
| _Entered_ | ユーザーがエージェントステップに入った回数です。 |
| _Proceeded to Next Step_ | エージェントステップを通過した後、フロー内の次のステップに進んだユーザー数です。 |
| _Exited Canvas_ | エージェントステップを通過した後、Canvasを退出したユーザー数です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析" }

## ベストプラクティス {#best-practices}

### 複雑なユースケースではエージェント間でタスクを分割する {#split-tasks-between-agents-for-complicated-use-cases}

エージェントが求められているタスクの複雑さに苦戦している場合は、複数のエージェントステップに作業を分割してください。1つのプロンプトにデータクリーンアップ、ルーティングロジック、完全なメッセージ作成を混在させると、それらの目標が競合し、出力品質にばらつきが生じる可能性があります。

以下のパターンでは、旅行の例として3つのエージェントを使用します。ユーザーが最近アプリで検索したが予約しなかった場合に、チェックアウトに誘導するリターゲティングコピーを作成します。

- エージェント1はCanvasコンテキストを要約します。ロイヤルティティア、最後に検索した都市、高インテントの検索行動などのフィールドを読み取り、後続のステップで再利用できる出力変数として短い構造化サマリーを返します。
- エージェント2はCanvasが分岐に使用できるルーティング値を返します。出力が分岐方法と一致するように、数値、ブール値、または構造化オブジェクトを使用します。その値を[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/)または[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)ステップにマッピングします。たとえば、ロイヤルティ主導のメッセージングとディール主導のメッセージングで別々のパスを検討してください。
- エージェント3は、必要なブランチでのみ生成メッセージテキストを作成します。エージェント1のサマリー（およびブランチ固有のコンテキスト）を渡すことで、このエージェントは同じプロンプト内で入力の正規化や戦略の選択ではなく、トーンとチャネル制限に集中できます。

### 実験パスステップを使用してエージェントジャーニーを小規模でテストする {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

エージェントのパフォーマンスとクレジット消費を既存のジャーニーと比較してテストするには、[実験パス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/)ステップを追加して、オーディエンスの一部のみがエージェントステップを含むブランチに入るようにします。

たとえば、1日あたり数千人のユーザーをエージェントのあるパスに送り、残りをコントロールパスまたはエージェントのないパスに送ることから始めることができます。1〜2週間データを収集し、パス間でKPI、カウンター指標、エージェントクレジット消費を比較します。こうすることで、エージェント対応ブランチへのトラフィックを増やす前に確信を持ちROIを証明でき、呼び出し消費も抑えられます。

## よくある質問 {#frequently-asked-questions}

### エージェントステップはいつ使用すべきですか？ {#when-should-i-use-an-agent-step}

一般的に、特定の文脈に応じたデータをLLMに入力し、人間には不可能な規模でCanvasコンテキスト変数をインテリジェントにエージェント的に割り当てたい場合に、エージェントステップの使用をお勧めします。

たとえば、以前にチョコレートとストロベリーを注文したユーザーに、新しいアイスクリームフレーバーをおすすめするパーソナライズされたメッセージを送信するとします。エージェントステップとAI 項目のレコメンデーションの違いは以下のとおりです。

- **エージェントステップ:** LLMを使用して、エージェントに与えられた指示とコンテキストデータポイントに基づいて、ユーザーが何を望むかについて定性的な判断を行います。この例では、エージェントステップはユーザーが異なるフレーバーを試したいという可能性に基づいて、新しいフレーバーをおすすめする場合があります。
- **AI 項目のレコメンデーション:** 機械学習モデルを使用して、購入などの過去のユーザーイベントに基づいて、ユーザーが最も欲しいと思われる製品を予測します。この例では、AI 項目のレコメンデーションは、ユーザーの過去2回の注文（チョコレートとストロベリー）と、ワークスペース内の他のユーザーの動作との比較に基づいて、フレーバー（バニラ）を提案します。

### エージェントステップは入力データをどのように使用しますか？ {#how-do-agent-steps-use-input-data}

エージェントステップは、エージェントが使用するように設定されたコンテキストデータと、[エージェントに提供された](#step-4-add-any-additional-context-optional)追加のコンテキストを分析します。

## 関連記事 {#related-articles}

- [Brazeエージェントの概要]({{site.baseurl}}/user_guide/brazeai/agents/)
- [カスタムエージェントの作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [エージェントのデプロイ]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
- [エージェントのリファレンス]({{site.baseurl}}/user_guide/brazeai/agents/reference/)