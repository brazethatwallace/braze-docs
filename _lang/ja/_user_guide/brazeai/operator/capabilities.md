---
nav_title: 機能
article_title: Operatorでできること
page_order: 1
page_type: reference
toc_headers: h2
description: "このリファレンス記事では、BrazeAI Operator™で利用できるAIタスク（コピーライティング、Liquid、画像生成、データ変換コード、コンテンツレビューなど）について説明します。"
---

# Operatorでできること {#operator-capabilities}

> 以前はスタンドアロンのアシスタントとして利用できたAI機能が、[BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)を通じてアクセスできるようになりました。Operatorはダッシュボードに組み込まれており、ワークスペース（ブランドガイドライン、属性、コネクテッドコンテンツ、作業中のページ）を理解しているため、以前のアシスタントよりもコンテキストを考慮した出力が可能です。

タスクごとに異なるツールを開く代わりに、自然言語でやりたいことを説明すれば、Operatorがコンテキストに沿って処理します。会話を続けることもでき、異なるトーン、短いバージョン、翻訳などを最初からやり直すことなく依頼できます。Operatorは、適用前に確認できる[アクションカード]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)を通じて、変更を直接提案・実行することもできます。

## 前提条件 {#prerequisites}

Operatorはあなたと同じ権限を持っているため、特定のアクションにはそのサーフェスに関連する権限が必要です。たとえば、画像の生成には*メディアライブラリアセットの編集*権限が必要です。エントリポイントが表示されない場合は、管理者に権限を確認してください。詳細については、[権限一覧]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)を参照してください。

## Operatorで利用できる機能 {#whats-available-through-operator}

既存のエントリポイントはすべてそのまま残っているため、ワークフローに影響はありません。これらのエクスペリエンスはOperatorによって提供されるようになりました。以下の表は、以前のスタンドアロンアシスタントと現在の場所の対応を示しています。

| 以前のアシスタント | 機能 | 現在の場所 |
| --- | --- | --- |
| AIコピーライター | 製品名や説明からマーケティングコピーを生成 | SMS、プッシュ通知、HTMLメール、キャンバスコンポーザーの新しい**Ask Operator**アイコン |
| AI Liquidアシスタント | パーソナライゼーション用のLiquidを生成 | SMS、プッシュ通知、HTMLメール、キャンバスコンポーザーの新しい**Ask Operator**アイコン |
| AI画像ジェネレーター | テキストプロンプトからメディアライブラリ用の画像を生成 | メディアライブラリの新しい**Operatorで生成**ボタン |
| データ変換AI Copilot | 変換コードを生成 | データ変換ページの**コードを挿入**ボタン |
| コンテンツレビュー | スペル、文法、トーン、不適切な言語、不要なコードをチェック | **テスト**タブの**Operatorでレビュー**ボタン |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Operatorで利用できる機能" }

## ブランドガイドラインの適用 {#apply-brand-guidelines}

Operatorは、ワークスペースで設定されたブランドガイドラインを使用して、生成されたコピー、テンプレート、画像がブランドのボイス、トーン、スタイルに一致するようにします。ブランドガイドラインを設定するには、**コンテンツ** > **ブランドガイドライン**に移動します。詳細については、[ブランドガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)を参照してください。Operatorでブランドガイドラインを適用する方法の詳細については、[ブランドガイドラインの適用]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines)を参照してください。

## コピーの生成 {#generate-copy}

Operatorを使用して、どこからでもコピーのブレインストーミングや生成ができますが、メッセージコンポーザー内で直接使用すると、作成中のメッセージと一緒に作業できるため、最良のエクスペリエンスが得られます。製品やキャンペーンを説明すると、Operatorがレビューして挿入できるコピーを返します。

Operatorは、スタンドアロンのコピーライターからいくつかの点で改善されています：

- 設定されている場合、[ブランドガイドライン](#apply-brand-guidelines)を自動的に適用します。
- [ページ対応コンテキスト]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context)を使用するため、作業中のチャネルやメッセージを再度説明する必要がありません。ページ対応であるため、ゼロから生成する代わりに、既存のメッセージの編集や改善にも使用できます。
- [カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)やイベントを検索できるため、実際のLiquidを使用したパーソナライズされたコピーの推奨を依頼できます。
- 会話を続けてイテレーションできます。たとえば、異なるトーン、短いバージョン、翻訳を依頼できます。

### トーン {#generate-copy-tones}

生成されるコピーのトーンはプロンプトによって決まります。フォーマル、カジュアル、緊急、目を引くなど、希望するスタイルを説明すると、Operatorがそれに合わせて出力を調整します。フォローアップのプロンプトでトーンを調整することもできます。たとえば、よりリラックスした、またはより洗練されたバージョンを依頼できます。[ブランドガイドライン](#apply-brand-guidelines)が設定されている場合、Operatorはそれを自動的に適用し、コピーがブランドのボイスと一貫性を保つようにします。

### プロンプトの例 {#generate-copy-example-prompts}

{% include copy_block.html content="Write a short, eye-catching push notification announcing our summer sale." %}

{% include copy_block.html content="Rewrite this subject line in a more casual tone." %}

{% include copy_block.html content="Translate this copy into Spanish." %}

## Liquidの生成 {#generate-liquid}

任意のメッセージコンポーザーでOperatorを開き、パーソナライゼーション用のLiquidを生成・改善できます。Operatorは[Liquid構文]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)、標準および[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を理解しており、コードの内容を説明することもできます。

### Liquidを生成できる場所 {#generate-liquid-supported-channels}

コピーライティングと同様に、どこからでもOperatorにLiquidの生成を依頼でき、すべてのチャネルとメッセージコンポーザーで動作します。メッセージコンポーザー内から使用すると、Operatorが作成中のメッセージの完全なコンテキストを持つため、最良の結果が得られます。

### Liquidの機能 {#generate-liquid-attributes}

OperatorはLiquidに非常に優れています。ワークスペース内のデータに基づいた複雑なLiquidロジックを生成でき、[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)データを検索してサンプル値を見つけることも含まれます。また、キャンペーンの既存のLiquidをレビューして説明することもできます。

### ベストプラクティス {#generate-liquid-best-practices}

#### 自然言語を使用する {#generate-liquid-use-natural-language}

Operatorは自然言語を理解するようにトレーニングされています。助けを求めるときは、同僚に話しかけるようにチャットしてください。これにより、Operatorがニーズを理解し、正確なサポートを提供できます。

#### コンテキストを提供する {#generate-liquid-give-context}

コンテキストを提供することで、Operatorがプロジェクトの全体像を理解しやすくなります。以下のようなコンテキストを含めると効果的です：

- 会社名と業界
- ブラックフライデーやホリデーセールなど、取り組んでいるキャンペーン
- クリックスルー率の向上など、目標
- メッセージに含めたい特定のカスタム属性

プロンプトにコンテキストを含めることで、Operatorがニーズに合わせた応答を提供できます。キャンペーン、メッセージブリーフ、ブレインストーミングドキュメントの詳細を含めて、Operatorに状況を把握させることもできます。

#### 具体的にする {#generate-liquid-be-specific}

Operatorはフォローアップの質問をすることができますが、事前に詳細を提供することで、より正確な結果をより早く得ることができます。以下のような詳細を含めることを検討してください：

- メッセージに関する既知の好みや要件
- メッセージ受信者からの応答がない場合やフォールバックメッセージオプションなど、状況の処理方法に関する指示
- 使用したいカスタム属性の正確な値または類似の値（Operatorがより正確なロジックを生成・テストするのに役立ちます）
- コネクテッドコンテンツを使用するLiquidを依頼する場合、APIエンドポイントのドキュメント、サンプルAPIレスポンス、またはその両方

#### 創造性を発揮する {#generate-liquid-get-creative}

さまざまなプロンプトを試して、Operatorがメッセージングをどのように強化できるかを確認してください。さまざまなプロンプトやアイデアを試してみてください。創造性がより魅力的な結果につながることがあります。

### プロンプトの例 {#generate-liquid-example-prompts}

{% tabs local %}
{% tab Liquidについて %}

{% include copy_block.html content="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" %}

{% include copy_block.html content="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" %}

{% include copy_block.html content="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" %}

{% include copy_block.html content="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" %}

{% endtab %}
{% tab パーソナライゼーション %}

{% include copy_block.html content="Add a countdown to this message that shows the time until the user's flight." %}

{% include copy_block.html content="Personalize this message with the user's first name, with a fallback if it's missing." %}

{% include copy_block.html content="Improve this Liquid so it's easier to read." %}

{% include copy_block.html content="Create a message that shows different content based on my customer's loyalty status. If we don't know about their loyalty status, send a fallback message." %}

{% include copy_block.html content="Write a dynamic message that includes a user's favorite product and their last purchase date. If there's no last purchase, abort the message." %}

{% include copy_block.html content="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." %}

{% include copy_block.html content="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." %}

{% include copy_block.html content="Write Liquid to personalize a message based on a customer's country. I want to fill in the message with the country's name. If we don't have either of them, suggest they click on a link to update their profile." %}

{% include copy_block.html content="How can I personalize a welcome message with a user's first name and write different copy based on the user's gender?" %}

{% include copy_block.html content="Write Liquid to display different messages based on a custom attribute, \"CUSTOM_ATTRIBUTE_NAME\" and its value. There are six different options I could send. If there's no value for the custom attribute, I want to send a placeholder message." %}

{% endtab %}
{% endtabs %}

## 画像の生成 {#generate-images}

Operatorは、OpenAIのAIシステムであり、Brazeのサードパーティプロバイダーである[GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)を使用して画像を生成します。これにより、自然言語の説明からリアルな画像やアートを作成できます。

[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)で、**アセットをアップロード**パネルから**Operatorで生成**を選択します。希望する画像を説明すると、Operatorがそれを生成し、メディアライブラリに直接保存します。

### プロンプトのヒント {#generate-images-prompt-tips}

- 被写体、スタイル、ムード、色を具体的に説明してください。詳細を含めるほど、より良い結果が得られます。
- テキスト入力のみ対応しています。参照画像のアップロードはサポートされていません。
- Operatorのプロンプトでコンテキストとして[ブランドガイドライン](#apply-brand-guidelines)を適用すると、Operatorがそれを生成画像に直接適用するため、ブランドのビジュアルスタイルが反映された結果になります。
- 画像生成は、1日のOperator使用制限にカウントされます。詳細については、[制限事項]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting#limitations)を参照してください。

### プロンプトの例 {#generate-images-example-prompts}

{% include copy_block.html content="Generate a bright, summery banner image of a beach scene for an email header." %}

{% include copy_block.html content="Create a minimalist product background in our brand colors." %}

## データ変換コードの生成 {#generate-data-transformation-code}

[データ変換]({{site.baseurl}}/user_guide/data/unification/data_transformation)エディターで、**コードを挿入**を選択して、受信Webhookペイロードを有効なBraze APIリクエストに変換する変換コードを生成します。

変換の作成手順については、[変換の作成]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation)を参照してください。

### プロンプトの例 {#generate-data-transformation-example-prompts}

{% include copy_block.html content="Write transformation code that maps this survey webhook to a custom event on the user's profile." %}

{% include copy_block.html content="Update this transformation to identify users by email address instead of external ID." %}

## コンテンツ品質のレビュー {#review-content-quality}

SMS、Androidプッシュ通知、iOSプッシュ通知、従来のアプリ内メッセージの**テスト**タブで、**Operatorでレビュー**を選択して、送信前にコンテンツをレビューします。デフォルトでは、Operatorはスペルと文法のエラー、ブランドに合わないまたは不適切なトーン、不適切な言語、不要なコード、テストコンテンツ、レンダリングされていないLiquidについてキャンペーンをレビューし、見つかった問題の修正方法を推奨します。プロンプトで直接、Operatorにコンテンツのレビュー方法をカスタマイズするよう依頼することもできます。

### Operatorに確認を依頼できる内容 {#review-content-quality-supported-features}

デフォルトのレビューに加えて、Operatorに特定のチェックに焦点を当てるよう指示できます。以下のいずれかを確認するようプロンプトすることを検討してください：

| チェック項目 | 依頼内容 |
| --- | --- |
| スペルと文法 | Operatorにスペルと文法の間違いを校正し、コンテンツの正確性を向上させる修正を提案するよう依頼します。 |
| トーン | Operatorにトーンが意図したコミュニケーションスタイルに合っているかを評価し、誤解される可能性のある箇所をフラグするよう依頼します。 |
| 不適切な言語 | Operatorに不適切または不快な言語がないかスキャンし、メッセージングを敬意あるものに保つために修正できるよう依頼します。 |
| 意図しないコンテンツ | Operatorに、テストユーザーでレンダリングされなかったLiquidを含め、意図せず追加された不要なコード、マークアップ、テストメッセージを検出するよう依頼します。 |
| 他の言語 | Operatorに他の言語で書かれたコンテンツをレビューするよう依頼します。英語以外のコンテンツのサポートは異なる場合があるため、結果を慎重に確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Operatorに確認を依頼できる内容" }

### ベストプラクティス {#review-content-quality-best-practices}

コンテンツレビューを最大限に活用するために、以下を検討してください：

- **メッセージを校正する：** コンテンツレビューはエラーの特定に役立ちますが、手動でコンテンツを校正することも依然として重要です。AI生成の提案を参考にしつつ、正確性を確保するためにご自身の判断を使用してください。
- **トーン分析を理解する：** トーン分析の結果は主観的であり、AIモデルの理解に基づいています。有用なインサイトを提供できますが、意図したトーンと会話のコンテキストを考慮して適切な調整を行ってください。
- **フラグされた不適切な言語を再確認する：** 不適切な言語の検出は堅牢に設計されていますが、誤検出が発生する場合があります。フラグされたセクションを慎重にレビューし、必要に応じて適切な変更を行ってください。

### プロンプトの例 {#review-content-quality-example-prompts}

{% include copy_block.html content="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." %}

{% multi_lang_include brazeai/generative_ai/policy.md %}

## データプライバシーとセキュリティ {#data-privacy-and-security}

Operatorは出力を生成するためにOpenAIと統合しています。BrazeがOpenAIに送信する情報、そのデータの使用方法、知的財産権の詳細については、[OpenAIでのデータの使用方法]({{site.baseurl}}/user_guide/brazeai/operator#how-data-is-used-with-openai)を参照してください。

## 次のステップ {#next-steps}

- [Operatorを始める]({{site.baseurl}}/user_guide/brazeai/operator)：Operatorへのアクセスと使用方法
- [アクションのレビュー]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)：Operatorが提案した変更のレビューと承認
- [トラブルシューティング]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting)：一般的な問題と解決策のリファレンス