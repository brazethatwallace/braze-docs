---
nav_title: エージェントを作成する
article_title: カスタムエージェントを作成する
description: "エージェントの作成方法、開始前に準備すべきこと、そしてメッセージング、意思決定、データ管理の分野でエージェントを活用する方法を学びます。"
page_order: 1
alias: /creating-agents/
---

# カスタムエージェントを作成する {#create-custom-agents}

> カスタムエージェントの作成方法、開始前に準備すべき事項、そしてメッセージング、意思決定、データ管理の分野でそれらを活用する方法を学びます。より一般的な情報については、[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents)を参照してください。

## 前提条件 {#prerequisites}

始める前に、以下が必要です。

- ワークスペースで**エージェントコンソール**にアクセスするための[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)。このオプションが表示されない場合は、Braze管理者に確認してください。
- カスタムAIエージェントを作成および編集する権限。
- エージェントに何を達成させたいかについてのアイデア。Brazeエージェントは以下のアクションをサポートしています。
   - **パーソナライズされたメッセージング:** 件名、見出し、プロダクト内コピー、その他のコンテンツを生成します。
   - **ユーザールーティング:** 行動、好み、またはカスタム属性に基づいてキャンバス内のユーザーをルーティングします。
   - **データ管理:** 値の計算、カタログエントリのエンリッチメント、またはプロファイルフィールドの更新を行います。

## 仕組み {#how-it-works}

エージェントを作成する際に、その目的を定義し、動作のガードレールを設定します。ライブにした後、エージェントはBrazeにデプロイして、パーソナライズされたコピーの生成、リアルタイムの意思決定、カタログフィールドの更新に使用できます。エージェントの構築中に下書きとして保存し、ダッシュボードからいつでも更新できます。保存するたびに新しいバージョンが作成され、[バージョン履歴]({{site.baseurl}}/user_guide/brazeai/agents/reference#version-history)タブで確認できます。

以下のユースケースでは、カスタムエージェントを活用するいくつかの方法を紹介します。

| ユースケース | 説明 |
| --- | --- |
| 顧客フィードバックの処理 | ユーザーのフィードバックをエージェントに渡して、センチメントを分析し、共感的なフォローアップメッセージを生成します。高価値ユーザーの場合、エージェントは対応をエスカレーションしたり、特典を含めたりすることがあります。 |
| コンテンツのローカライズ | グローバルキャンペーン向けにカタログテキストを別の言語に翻訳したり、地域固有のチャネルに合わせてトーンや長さを調整したりします。例えば、「Classic Clubmaster Sunglasses」をスペイン語で「Gafas de sol Classic Clubmaster」に翻訳したり、SMSキャンペーン向けに説明を短縮したりします。 |
| レビューやフィードバックの要約 | センチメントやフィードバックを新しいフィールドに要約します。例えば、Positive、Neutral、Negativeなどのセンチメントスコアを割り当てたり、「ほとんどの顧客はフィット感を高く評価していますが、配送の遅さを指摘しています」といった短いテキスト要約を作成したりします。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="仕組み" }

## エージェントを作成する {#create-an-agent}

### ステップ1：エージェントタイプを選択する {#step-1-choose-an-agent-type}

エージェントを作成するには、まずエージェントタイプを選択します。

1. **エージェントコンソール**に移動します。
2. **キャンバス Step Agents** または **Catalog Agents** を選択します。

### ステップ2：エージェントの構築方法を選択する {#step-2-choose-how-to-build-an-agent}

**Create agent** を選択し、次のいずれかのオプションを選びます。

- **Custom agent**：白紙の状態からエージェントを構築します
- **Create an agent with Operator** のオプション：[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)を使用して[スターティングテンプレート](#agent-templates-built-with-operator)を適用します

Operatorを使用する場合は、次のステップに進む前に、チャットで変更内容を確認し承認してください。

### ステップ3：詳細を設定する {#agent-instructions}

次に、エージェントの詳細を設定します。

1. チームがエージェントの目的を理解できるよう、名前と説明を入力します。
2. （オプション）エージェントをフィルターするためのタグを追加します。
3. エージェントが使用する[モデル]({{site.baseurl}}/user_guide/brazeai/agents/reference#models)を選択します。
4. **Braze Auto** モデルを使用していない場合は、モデルの[思考レベル]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels)を選択します。最小、低、中、高から選べます。まず **Minimal** から始めて、エージェントの応答をテストし、必要に応じて調整することをお勧めします。
5. 1日あたりの呼び出し上限を設定します。デフォルトでは250,000に設定されていますが、1,000,000まで引き上げることができます。1,000,000を超える上限に引き上げたい場合は、カスタマーサクセスマネージャーに連絡して詳細を確認してください。テスト後の想定オーディエンスサイズに十分な上限を設定してください。上限が低すぎると、1日あたりの上限エラーが発生します（クレジットは消費されませんが、フォールバック値が適用されるか、出力が`null`のままになります）。

**Daily action credit cost limit** フィールドは、このエージェントが1日あたりに消費できるクレジットの最大数を指定します。Brazeは、選択したモデルのワークスペースごとの呼び出しあたりのクレジット比率（契約に基づき、[Credit Ratios]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)ページに表示）に1日あたりの呼び出し上限を掛けて計算します。モデルや呼び出し上限を変更すると、見積もりが更新されます。

コストを管理するには、1日あたりの呼び出し上限を下げてください。[自前のキー（BYO）]({{site.baseurl}}/user_guide/brazeai/agents/reference#option-2-bring-your-own-api-key)モデルの場合は、より低コストのモデルに切り替えるか、[思考レベル]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels)を下げることもできます。**Braze Auto** は思考レベルの調整をサポートしていません。実際の使用状況は **Settings** > **Billing** > **Credits Usage** > **Agent Console** で追跡できます。

![Brazeでカスタムエージェントを作成するためのエージェントコンソールのインターフェイス。エージェント名と説明を入力するフィールド、モデルの選択、1日あたりの呼び出し上限の設定が表示されています。]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### ステップ4：指示を記述する

エージェントに指示を与えます。Operatorテンプレートを使用した場合は、事前入力された指示を確認し、必要に応じて編集してください。

予期しないシナリオや曖昧なシナリオでエージェントが何をすべきかについての指示を含めてください。これにより、エージェントの混乱がエラーにつながるリスクを最小限に抑えます。たとえば、エージェントに「ポジティブ」または「ネガティブ」のセンチメント値のみを求める代わりに、判断できない場合は「unsure」を返すように求めてください。

ベストプラクティスについては[指示の記述]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions)を、エージェントへのプロンプトのインスピレーションについては[例]({{site.baseurl}}/user_guide/brazeai/agents/reference#examples)を参照してください。

#### コンテキストを追加する {#add-resources}

{% alert important %}
エージェントは、明示的に渡されたデータのみを受け取ります。ユーザープロファイルを検索したり、必要なデータが不足している場合に警告したりすることはありません。指示にLiquidを使用するか、**+ Agent context** を選択するか、キャンバスに上流の[Contextステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)を追加するか、Agent ステップに追加のコンテキストを渡してください。データソースとデザインガイダンスの完全なリストについては、[エージェントが受け取るデータ]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive)を参照してください。
{% endalert %}

**+ Agent context** を選択して、エージェントが参照できるものを選びます。以下が含まれます。

- [カタログフィールド]({{site.baseurl}}/user_guide/brazeai/agents/reference#catalogs-and-fields)：より正確な応答のためにカタログデータへのアクセスをエージェントに提供します。
- [ナレッジソース]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources)：カタログを直接添付するよりも正確な検索のため、ナレッジソースを通じてカタログデータへのアクセスをエージェントに提供します。
- [セグメントメンバーシップ]({{site.baseurl}}/user_guide/brazeai/agents/reference#segment-membership-context)：ユーザーが属するセグメントに基づいて、エージェントが応答をパーソナライズできるようにします。最大5つのセグメントを選択できます。
- [ブランドガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)：エージェントが従うべきブランドの声やスタイルのガイドラインを参照します。たとえば、ジムの会員登録を促すSMSコピーをエージェントに生成させたい場合、事前に定義した力強くモチベーションを高めるガイドラインを参照するためにこのフィールドを使用できます。
- [すべてのキャンバスコンテキスト]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)：このエージェントが呼び出されたとき、**指示**セクションで参照されていない変数を含め、ユーザーのすべてのキャンバスコンテキストデータを分析します。
- [ユーザーインタラクションデータ]({{site.baseurl}}/user_guide/brazeai/agents/reference#user-history)：各ユーザーの最近のキャンペーンとキャンバスの開封、クリック、コンバージョンデータをエージェントに提供します。

{% alert tip %}
キャンバスエージェントの場合、指示にLiquidを使用して、姓や名、カスタム属性などのユーザー属性を参照できます。エージェントの指示に含まれるLiquid変数は、ユーザーがステップに入ると自動的にAgentステップに渡されます。キャンバスコンテキストとプロファイルデータを意図的に渡す方法については、[エージェントが受け取るデータ]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive)を参照してください。
{% endalert %}

### ステップ5：出力を選択する {#select-output}

**Output** セクションでは、基本スキーマまたは高度なスキーマでエージェントの[出力]({{site.baseurl}}/user_guide/brazeai/agents/reference#outputs)を整理・定義できます。Operatorテンプレートを使用した場合は、事前入力された出力スキーマを確認し、必要に応じて編集してください。

最良の結果を得るために、**Output** セクションで指定する内容が[ステップ4](#agent-instructions)で入力したエージェントの指示と一致していることを確認してください。たとえば、エージェントの指示で2つの文字列を持つオブジェクトが欲しいと記述した場合、**Output** セクションでも2つの文字列を持つオブジェクトを指定してください。エージェントの指示が指定した出力と一致していない場合、エージェントが混乱したり、タイムアウトしたり、意図しない出力を生成したりする可能性があります。

{% alert tip %}
[高度な出力スキーマ]({{site.baseurl}}/user_guide/brazeai/agents/reference#advanced-schemas)を使用する場合、エージェントが他の出力に加えてその根拠を返すようにしたいときは、`explanation`という名前の文字列フィールドを追加してください。応答の確認やデバッグに役立つ場合は、[指示](#agent-instructions)でエージェントに`explanation`を入力するよう伝えてください。
{% endalert %}

#### フォールバック値を設定する {#configure-fallback-values}

フォールバック値はキャンバス Step Agentsでのみ利用できます。キャンバス Step Agentの **Output** セクションでは、エージェントの呼び出しが失敗した場合（たとえば、LLMがタイムアウトしたり、無効なAPIキーエラーを返した場合など）にBrazeが使用する値を定義できます。フォールバック値はパーソナライゼーションのデフォルトのように機能します。エージェントが実行できないときにも、ユーザーに有用な出力を提供する静的な件名や短いメッセージを設定できます。

Catalog Agentsは、エージェントコンソールでのフォールバック値の設定をサポートしていません。

![Numberスキーマのフォールバック出力フィールドを表示するエージェントコンソールの出力設定。]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

キャンバスエージェントの場合、フォールバック値は[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)テンプレートをサポートしているため、フォールバックテキストでユーザー属性やコンテキスト変数を参照できます。

フォールバックフィールドはキャンバス Step Agentの出力形式に応じて変化します。

| 出力形式 | フォールバック設定 |
| --- | --- |
| 文字列、数値、またはブール値 | 単一のフォールバック値を入力します（Liquidサポート）。 |
| フィールド（高度なスキーマ） | エージェントの出力で定義された各フィールドに対してフォールバック値を入力します。 |
| JSONスキーマ（高度なスキーマ） | BrazeがJSONスキーマを読み取り、各プロパティに対して入力フィールドを生成するため、キーごとにフォールバック値を定義できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="フォールバック値の設定" }

フォールバック値を持つキャンバス Step Agentが[Agentステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)で実行されると、Brazeはユーザーごとにフォールバックをレンダリングし、`null`の代わりに出力変数に保存します。フォールバック値を設定しない場合、失敗した呼び出しではキャンバスの出力が未設定（`null`）のままになります。

ランタイムの動作については、[エラーハンドリングとフォールバック動作]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior)を参照してください。

### ステップ6：エージェントをテストする {#step-6-test-the-agent}

**Preview** ペインは、設定画面内にサイドバイサイドのパネルとして表示されるエージェントのインスタンスです。このセクションを使用して、エージェントの作成中や更新中にテストし、エンドユーザーと同様の方法で体験できます。このステップにより、期待どおりに動作していることを確認でき、公開前に微調整を行うことができます。

1. **Test your agent** フィールドに、エージェントが処理する実際のシナリオを反映した顧客データや顧客の応答の例を入力します。
2. ランダムユーザー、既存のユーザー、またはカスタムユーザーに対するエージェントの応答をプレビューします。
3. **Simulate response** を選択します。エージェントは設定に基づいて実行され、応答を表示します。

{% alert note %}
テスト実行は1日あたりの呼び出し上限にカウントされます。
{% endalert %}

![カスタムエージェントのテスト用のプレビューペインを表示するエージェントコンソール。サンプル入力フィールドに顧客データの例、テスト実行ボタン、エージェントの出力が表示される応答エリアがあります。]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

出力を批判的な目で確認してください。次の点を検討します。

- コピーはブランドに合っていますか？
- 意思決定ロジックは顧客を意図どおりにルーティングしていますか？
- 計算された値は正確ですか？

何か違和感がある場合は、エージェントの設定を更新して再度テストしてください。データがない場合や無効な応答などのエッジケースを含む、さまざまな入力を実行して、エージェントがシナリオ間でどのように適応するかを確認してください。

{% alert tip %}
エージェントに対して、やってほしくないことを正確に伝えることは避けてください。LLMは、指示に記述するとそのコンテンツを生成してしまう場合があります。
{% endalert %}

### ステップ7：エージェントを使用する {#step-7-use-your-agent}

エージェントを使用する準備ができました！詳細については、[エージェントのデプロイ]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)を参照してください。

## オペレーターで構築されたエージェントテンプレート {#agent-templates-built-with-operator}

オペレーターは、以下のエージェントコンソール開始テンプレートの指示、出力フィールド、コンテキストを事前設定できます。オペレーターでテンプレートを選択するか、名前を指定してオペレーターにテンプレートの適用を依頼してください。

### キャンバスステップエージェントテンプレート {#canvas-step-agent-templates}

| テンプレート | 説明 | 出力例 |
| --- | --- | --- |
| パーソナライズドコピーライター | ユーザー属性、キャンバスコンテキスト、ブランドガイドラインからチャネル固有のメッセージコピーを生成します | メールの件名とプリヘッダー、プッシュのタイトルと本文 |
| フィードバックアナリスト | 自由記述のアンケートやサポートフィードバックを、キャンバス分岐用の構造化フィールドに解析します | 感情、トピック、推奨される次のアクション |
| ジャーニールーター | プロファイルとジャーニーコンテキストに基づいて、各ユーザーを最も関連性の高いキャンバスパスに振り分けます | パス名または条件分岐ステップ用のブール値 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="キャンバスステップエージェントテンプレート" }

### カタログエージェントテンプレート {#catalog-agent-templates}

| テンプレート | 説明 | 出力例 |
| --- | --- | --- |
| 説明文ライター | 既存のカタログ列から短いマーケティング説明文を作成します | 製品または送信先の説明 |
| アイテムカテゴライザー | 行データからカテゴリやタグを割り当てます | フィルタリングやおすすめ用のカテゴリラベル |
| ローカライゼーション翻訳者 | 文字数制限内でカタログ文字列をターゲットロケールに翻訳します | ロケールごとのローカライズされたテキスト |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カタログエージェントテンプレート" }

## 関連リソース {#related-resources}

- [エージェントのリファレンス]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [よくある質問]({{site.baseurl}}/user_guide/brazeai/agents/faq)
- [Braze ウェビナー：AI in Action: 3 new use cases for 1:1 personalization](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)