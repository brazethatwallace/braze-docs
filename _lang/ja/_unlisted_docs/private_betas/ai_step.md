---
nav_title: AI ステップ
article_title: AI ステップ
permalink: /ai_step/
description: "このリファレンス記事では、CanvasのAIステップについて説明します。"
tool:
  - Canvas
hidden: true
---

# AI ステップ {#ai-step}

> Canvas内のAIステップは、ChatGPTを活用して、ユーザー生成の入力（アンケートのフィードバックなど）を解釈し、適切な応答を判断し、メッセージをトリガーすることで、パーソナライズされたマーケティングを自動化します。これらはすべてBraze内で完結します。ChatGPTはサードパーティであるOpenAIによって提供されています。

{% alert note %}
AIステップは現在ベータ機能として利用可能です。このベータトライアルへの参加にご興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## AIステップの作成 {#create-ai-step}

1. Canvasに新しいステップを追加し、**AIステップ**を選択します。<br><br>![Canvasビルダー内のAIステップ][1]{: style="max-width: 30%;"}<br><br>
2. さまざまなユーザーアクションに対してAIがどのように応答するかを指示するプロンプトを作成します。応答には、カスタム属性の更新やメッセージの送信を含めることができます。このプロンプトでは、Liquidを使用して、異なるユーザー属性や入力に基づいて異なる応答出力を割り当てることができます。<br><br>同じCanvas内の今後のメッセージをパーソナライズするために使用できる出力を割り当てるには、特定の名前（例：「message」や「sentiment score」）で変数を保存するプロンプトを作成します。<br><br> ![生成されたセンチメントスコアに基づいてパーソナライズされたメッセージを送信するためにAIステップ設定で使用されるサンプルAIプロンプト。この例は「顧客センチメント応答」セクションに記載されています。][2] <br><br>
3. **プレビュー**タブを使用して、特定のユーザーに対してAIが出力する内容をテストします。<br><br> ![AIステップ設定のプレビュータブ。名が「Cameron」、製品名が「shoes」、テキストが「decent but my shoe lace already broke」の3つのパラメーターに対してAIが生成したパーソナライズされたメッセージが表示されています。][3]

## Liquidを使用したAI出力の参照 {#referencing-ai-output-using-liquid}

後続のステップでAI出力を参照するには、Liquidロジック `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}` を挿入します。`key_name`はAIステップ内のプロンプトで設定できます。

例えば、変数「message」と「sentiment score」を使用している場合、`{% raw %}{{ai_step_output.${message}}}{% endraw %}` を使用して、同じCanvas内の後続のメッセージをパーソナライズできます。

また、ユーザーの更新キャンバスステップを使用して、AIステップの出力をカスタム属性として記録することもできます。この場合、AIステップの出力（例：`{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`）を読み取ります。出力がカスタム属性として保存されていない場合、同じCanvasの後続ステップ以外の場所では使用できません。

### コンテキストステップの使用 {#using-context-steps}

[Canvasコンテキストステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works)を活用して、Canvas内の後続で出力を簡単に参照できます。

以下は、AIステップの後に設定できるコンテキストステップの例です。この例では、先行するAIステップにセンチメントスコアとメッセージのAIステップ出力が含まれており、このコンテキストステップで変数 `sentiment_score` と `message` を作成し、後続のステップで使用できるようにしています。

![2つの変数「sentiment_score」と「message」を持つコンテキストステップ。][6]

また、コンテキスト変数の値に基づいてユーザーを異なるパスに送るオーディエンスパスステップを作成することもできます。この例では、センチメントスコアに応じてユーザーを異なるターゲットにすることができます。また、Liquidを使用して、{% raw %}`{{context.${message}}}`{% endraw %}で変数を挿入することで、メッセージ変数をメールの本文に組み込むこともできます。

![オーディエンスグループ「Group 1」を持つオーディエンスパスステップ。フィルターは「sentiment_scoreが80を超える」です。][7]

## AIステップの指標 {#ai-step-metrics}

AIステップには、以下のステップレベルの指標があります。

| 指標 | 説明 |
| _次のステップに進んだ_ | Canvas内の後続のステップに進んだユーザー数 |
| _Canvasを退出した_ | AIステップが最後のステップだった場合にCanvasを退出したユーザー数 |
| _出力成功_ | AIステップが正常に出力を生成したユーザー数 |
| _出力失敗_ | AIステップが出力の生成に失敗したユーザー数。この場合、ユーザーは後続のステップに進みます |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### AIステップ出力の理解 {#understanding-your-ai-step-outputs}

BrazeがAIステップの出力を破棄し、顧客を次のステップに送るシナリオがいくつかあります。

- 出力が1,024文字を超える場合
- 出力がJSON形式でない場合
- プロンプトがOpenAIの[モデレーション](https://platform.openai.com/docs/guides/moderation/overview)要件に違反した場合（不適切なユーザー生成コンテンツがフラグされます）

## AIステップのユースケース {#ai-step-use-cases}

### 顧客センチメント応答 {#customer-sentiment-responses}

[AIステップの作成](#create-ai-step)の例で示したように、顧客フィードバックから生成されたセンチメントスコアに基づいて、AIにフォローアップメッセージを送信させることができます。

- **ポジティブなセンチメントスコア：** レビューの投稿を依頼するプッシュ通知をトリガーします
- **中程度のセンチメントスコア：** 追加のサポートが必要かどうかを尋ねるメールをトリガーします
- **低いセンチメントスコア：** サポート担当者がきめ細かなフォローアップを作成できるよう、ユーザーヘルプデスクに通知するWebhookをトリガーします

#### AIプロンプトの例 {#example-ai-prompt}

この例は[AIステップの作成](#create-ai-step)で使用されたものです。

顧客が「`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`」を購入し、製品フィードバックとして「`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`」を提供しました。0から100の整数としてセンチメントスコアを作成してください。次に、パーソナライズされたメッセージを作成してください。これは「message」と「sentiment score」の2つの変数を返す必要があります。

### アンケートのフォローアップ {#survey-follow-ups}

自由回答セクションを含むアプリ内またはブラウザ内アンケートを実施している場合、AIステップを使用して自由回答を分析し、適切にフォローアップできます。

例えば、化粧品小売業者が「今年のビューティーアワードにノミネートしたい製品は何ですか？」というアンケートを実施している場合、ユーザーのお気に入りの製品タイプやブランドを特定して属性を割り当てるプロンプトを使用し、このデータに基づいて今後のコンテンツをパーソナライズできます。

#### AIプロンプトの例

ユーザーの回答からお気に入りのブランドを特定してください。次に、アンケートへの回答に感謝し、ビューティーエキスパートもそのお気に入りブランドを愛用していることに言及するメッセージを作成してください。これは「message」と「favorite brand」の2つの変数を返す必要があります。

![AIステップ設定のプレビュータブ。アンケート回答パラメーター「I love Beauty Brand face creams」に対してAIが生成したパーソナライズされたメッセージが表示されており、アンケートへの回答に感謝し、フェイスクリームをおすすめしています。][4]

### 行動に基づくおすすめ {#behavior-driven-recommendations}

顧客はAIにユーザーの行動を分析させ、おすすめメッセージを送信させることができます。

例えば、ユーザーの直近50件の購入を分析し、最も頻繁に購入されたカテゴリを新しいカスタム属性として設定するプロンプトを作成できます。その後、各ユーザーのお気に入りカテゴリに対してパーソナライズされたメールのおすすめを送信できます。

#### AIプロンプトの例

顧客が以下の製品を購入しました：「`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`」。ユーザーの最も購入頻度の高い製品カテゴリを特定してください。これは「most purchased category」の新しい変数を返す必要があります。

![AIステップ設定のプレビュータブ。最も購入頻度の高いカテゴリのパラメーターに対してAIが生成した変数「book」が表示されています。][5]

## レート制限 {#rate-limits}

会社あたり1分間に10リクエスト（RPM）の制限があります。つまり、任意のAIステップにおいて、1分間に最大10人のユーザーがそのステップを受け取ることができ、10人を超えるユーザーは自動的に次のステップに進みます。次の1分が始まるとユーザーは再びAIステップを受け取ることができますが、レート制限をトリガーした以前のユーザーは再試行されません。

## AIステップの制限事項 {#ai-step-limitations}

- この機能はGPT-3.5を活用しています。
- この機能はBrazeのOpenAI APIキーを使用します。独自のOpenAI APIキーは使用できません。
- ワークスペースあたり1分間に5リクエスト（RPM）、会社あたり10 RPMの制限があります。
- この機能はHIPAAに準拠しておらず、顧客は個人を特定できる情報（PII）や保護対象保健情報（PHI）を送信しないでください。

## データはどのように使用され、OpenAIに送信されますか {#how-is-my-data-used-and-sent-to-openai}

BrazeがOpenAIを活用していると特定するBraze AI機能を通じてAI出力（「出力」）を生成するために、Brazeはプロンプト（メッセージコンテンツ、エンドユーザーのセンチメント、ブランドガイドライン、過去のCampaignデータ、またはその他の入力など、該当するもの）（「入力」）を[OpenAI](https://openai.com/)に送信します。AIステップでBrazeのChatGPT統合を使用する際に個人データがOpenAIに送信される場合、OpenAIはお客様とBraze間のDPAに定められているとおり、Brazeのサブプロセッサーとして機能します。独自の大規模言語モデル（LLM）をAIステップと統合する場合、そのLLMのプロバイダーはサードパーティプロバイダーとみなされ、個人データの処理はお客様と当該サードパーティプロバイダー間の条件に従います。[OpenAIのAPIプラットフォームコミットメント](https://openai.com/enterprise-privacy/)に基づき、Brazeを通じてOpenAIのAPIに送信されたデータは、OpenAIモデルのトレーニングや改善には使用されず、OpenAIのシステムから30日後に削除されます。お客様とBraze間において、出力はお客様の知的財産です。Brazeはそのような出力に対して著作権の所有権を主張しません。Brazeは、出力を含むAI生成コンテンツ全般に関して、いかなる種類の保証も行いません。

[1]: {% image_buster /assets/unlisted_docs/img/ai_step1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/ai_step2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/ai_step3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/ai_step4.png %}
[5]: {% image_buster /assets/unlisted_docs/img/ai_step5.png %}
[6]: {% image_buster /assets/unlisted_docs/img/ai_step6.png %}
[7]: {% image_buster /assets/unlisted_docs/img/ai_step7.png %}