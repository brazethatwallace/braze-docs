---
nav_title: 機能
article_title: Operatorでできること
page_order: 1
page_type: reference
toc_headers: h2
description: "このリファレンス記事では、BrazeAI Operator™がダッシュボード全体でできることについて説明します。キャンペーン、セグメント、エージェントの構築、コピー・メッセージ・Liquid・画像の生成、データ変換、コンテンツ品質のレビュー、情報の検索などが含まれます。"
---

# Operatorでできること {#operator-capabilities}

> [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)は、Brazeダッシュボードに組み込まれたAIアシスタントです。質問に回答し、メッセージを作成し、対応するページ上でアクションを実行します。やりたいことを自然言語で説明すれば、Operatorがコンテキストに沿って処理します。

Operatorはワークスペース（ブランドガイドライン、カスタム属性、Connected Content、作業中のページ）を理解しているため、スタンドアロンのアシスタントよりもコンテキストを考慮した出力が可能です。Operatorがキャンペーン、セグメント、その他のオブジェクトへの変更を提案する場合、保存前に確認・承認できる[アクションカード]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)としてビジュアルdiffで変更を表示します。

フォローアップで会話を続けることもできます。Operatorはチャット履歴をクリアするまで、以前のメッセージを記憶しています。

## 前提条件 {#prerequisites}

オペレーターはあなたと同じ権限を持っているため、特定のアクションにはそのサーフェスに関連する権限が必要です。たとえば、画像を生成するには*メディアライブラリアセットの編集*権限が必要です。エントリポイントが表示されない場合は、管理者に権限を確認してください。詳細については、[権限のリスト]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)を参照してください。

## Operatorが作成できるもの {#what-operator-can-create}

コピーやLiquidの生成に加えて、Operatorはダッシュボード全体でさまざまなオブジェクトの構築を支援できます。以下はその一例です：

- キャンペーン
- Content Blocks
- カスタムエージェント
- 画像
- メッセージとメッセージテンプレート（[メッセージの生成](#generate-messages)と[メッセージテンプレートの作成](#create-message-templates)を参照）
- セグメント
- セグメントエクステンション

{% alert note %}
Operatorのダッシュボード全体での機能は定期的に拡張されています。最新の情報については、**Operatorに直接聞いてください**。
{% endalert %}

## キャンペーンとオーディエンス {#campaigns-and-audiences}

Operatorは、アイデアからキャンペーンやオーディエンスの下書きを作成し、作成後にそれらを改善するのを支援できます。Operatorがキャンペーンやセグメントに提案する変更は、保存前に確認するアクションカードとして表示されます。

開始するには、キャンペーンやセグメントを作成する際に**Operatorで作成**オプションを探してください。

![キャンペーン作成メニューとセグメント作成メニュー。それぞれにOperatorで作成オプションが表示されています。]({% image_buster /assets/img/operator/operator_create_with_operator.png %}){:style="max-width:90%"}

- **キャンペーンの作成と編集：** キャンペーンを開始する際、Operatorは単一の自然言語ブリーフからエンドツーエンドで下書きを作成できます。これにはオーディエンス、コンテンツ、配信設定が含まれます。また、ターゲティングの調整やメッセージコンテンツの更新など、既存のキャンペーンの編集もOperatorに依頼できます。
- **ブリーフからキャンペーンへ：** キャンペーンブリーフ全体を説明すると、Operatorがコピー、画像、パーソナライゼーション、ターゲティング、送信時間の推奨を含む下書きの作成を支援します。キャンペーンコンポーザーで下書きを確認し、起動前にフォローアッププロンプトで改善します。
- **セグメントの作成と編集：** セグメントを開始する際、希望するオーディエンスを説明すると、Operatorが属性条件、イベント履歴、カタログルックアップを含むフィルターロジックの構築を支援します。ターゲティング戦略の変更が必要な場合、Operatorは既存のセグメントのフィルター編集も支援できます。
- **セグメントエクステンションの作成：** Operatorは、定義するクエリを記述することで、SQLで定義された[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)の構築を支援できます。希望するオーディエンスロジックを説明すると、Operatorが保存前に確認するクエリの下書きを作成します。OperatorとSQLの詳細については、[SQLクエリの記述](#write-sql-queries)を参照してください。

## エージェント {#agents}

![エージェント作成メニュー。カスタムエージェントオプションとOperatorで構築されたエージェントテンプレートが表示されています。]({% image_buster /assets/img/operator/operator_create_agent.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

Operatorは、[エージェントコンソール]({{site.baseurl}}/user_guide/brazeai/agents)でエージェントの構築と改善を支援できます。Operatorがエージェントに提案する変更は、保存前に確認するアクションカードとして表示されます。

- **ゼロからエージェントを作成：** Operatorはエージェントコンソールのすべてのフィールドにアクセスできるため、希望するエージェントを説明すると、Operatorが設定を支援します。これには指示、出力設定、その他のエージェントフィールドが含まれます。
- **テンプレートから開始：** エージェントコンソールには、コピーライティング、感情分析、ジャーニールーティング、カタログエンリッチメントなどの一般的なユースケース向けに事前に記述されたプロンプトを読み込む**Operatorでエージェントを作成**オプションがあります。カテゴリを選択すると、Operatorが改善可能なエージェントの下書きを支援します。テンプレートの完全なリストについては、[Operatorで構築されたエージェントテンプレート]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)を参照してください。
- **既存のエージェントを改善：** エージェントを編集する際、エージェントの指示フィールドの近くにある**Operatorで生成**または**Operatorで改善**を選択して、エージェントのプロンプトと出力設定の記述や修正についてOperatorの支援を受けられます。

## コンテンツとクリエイティブ {#content-and-creative}

オペレーターは、コピー、メッセージHTML、Liquid、画像を含むメッセージのコンテンツを生成・レビューでき、ブランドガイドラインが設定されている場所では自動的に適用します。

### ブランドガイドラインの適用 {#apply-brand-guidelines}

オペレーターは、ワークスペースで設定されたブランドガイドラインを使用して、生成されたコピー、テンプレート、画像がブランドのボイス、トーン、スタイルに一致するようにします。ブランドガイドラインを設定するには、**コンテンツ** > **ブランド・ガイドライン**に移動します。詳細については、[ブランド・ガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)およびオペレーター使用ガイドの[ブランドガイドラインの適用]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines)を参照してください。

### コピーの生成 {#generate-copy}

オペレーターを使用して、どこからでもコピーのブレインストーミングや生成ができますが、メッセージ作成画面内で直接使用すると、作成中のメッセージと一緒に作業できるため、最良のエクスペリエンスが得られます。製品やキャンペーンを説明すると、オペレーターがレビューして挿入できるコピーを返します。

オペレーターは、スタンドアロンのコピーライターからいくつかの点で改善されています：

- 設定されている場合、[ブランドガイドライン](#apply-brand-guidelines)を自動的に適用します。
- [ページ対応コンテキスト]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context)を使用するため、作業中のチャネルやメッセージを再度説明する必要がありません。ページ対応であるため、ゼロから生成する代わりに、既存のメッセージの編集や改善にも使用できます。
- [カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)やイベントを検索できるため、実際のLiquidを使用したパーソナライズされたコピーの推奨を依頼できます。
- 会話を続けてイテレーションできます。たとえば、異なるトーン、短いバージョン、翻訳を依頼できます。

#### トーン {#generate-copy-tones}

生成されるコピーのトーンはプロンプトによって決まります。希望するスタイルを説明すると、オペレーターがそれに合わせて出力を調整します。たとえば、フォーマル、カジュアル、緊急、目を引くなどを指定できます。フォローアッププロンプトでトーンを調整することもできます。たとえば、よりリラックスした、またはより洗練されたバージョンを依頼できます。ブランドガイドラインが設定されている場合、オペレーターはそれを自動的に適用し、コピーがブランドのボイスと一貫性を保つようにします。

### メッセージの生成 {#generate-messages}

オペレーターは、HTMLモードを持つ任意のチャネルやエディターで完全なメッセージデザインを生成できます。以下はその一例です：

- メール
- SMS/MMS/RCS
- アプリ内メッセージ
- Content Card
- バナー
- プッシュ
- Webhook

ドラッグ＆ドロップエディターは直接的なデザイン生成をサポートしていませんが、オペレーターは手動で追加するコピーやその他のコンテンツの支援は可能です。自然言語でメッセージを説明し、出力をレビューしてコンポーザーに挿入します。会話を続けて結果を改善できます。たとえば、HTMLをエディターに挿入する前に、異なるレイアウト、短いコピー、更新されたボタンスタイリングを依頼できます。

作成中のコンポーザー内でオペレーターを使用すると、チャネルとメッセージタイプの[ページ対応コンテキスト]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context)を持つため、最良の結果が得られます。ブランドガイドラインが設定されている場合、オペレーターはそれを自動的に適用します。

### Content Blocksの作成 {#create-content-blocks}

オペレーターは、メッセージ間で挿入する再利用可能なコンテンツである[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)の作成を支援できます。希望するブロックを説明すると、オペレーターが保存前に確認するコンテンツの下書きを作成します。Content Blocksは共有されるため、1つを更新すると、それを参照するすべてのメッセージが更新されます。

オペレーターはダッシュボードで一度に1つずつContent Blocksを作成します。Content Blocksを一括で作成するには、`content_blocks.create`権限を持つAPIキーで[Content Blocksの作成]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)エンドポイントを使用してください。

### メッセージテンプレートの作成 {#create-message-templates}

オペレーターは、キャンペーン全体で適用できる再利用可能な[メッセージテンプレート]({{site.baseurl}}/user_guide/messaging/templates)の作成を支援できます。希望するテンプレートを説明すると、オペレーターが保存前に確認する下書きを作成します。テンプレートの生成はメッセージの生成と同様に機能するため、対応するチャネルとエディターについては[メッセージの生成](#generate-messages)を参照してください。

### Liquidの生成 {#generate-liquid}

オペレーターは[Liquid構文]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)に非常に優れています。属性、イベント、[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)データを検索してサンプル値を見つけることを含め、ワークスペース内のデータに基づいた複雑なLiquidロジックを生成できます。また、キャンペーンの既存のLiquidをレビューして説明することもできます。

コピーライティングと同様に、どこからでもオペレーターにLiquidの生成を依頼でき、すべてのチャネルとメッセージ作成画面で動作します。メッセージ作成画面内から使用すると、オペレーターが作成中のメッセージの完全なコンテキストを持つため、最良の結果が得られます。

{% details Liquidプロンプトのベストプラクティス %}

#### コンテキストを提供する {#generate-liquid-give-context}

コンテキストを提供することで、オペレーターがプロジェクトの全体像を理解しやすくなります。以下のようなコンテキストを含めると効果的です：

- 会社名と業界
- ブラックフライデーやホリデーセールなど、取り組んでいるキャンペーン
- クリックスルー率の向上など、目標
- メッセージに含めたい特定のカスタム属性

プロンプトにコンテキストを含めることで、オペレーターがニーズに合わせた応答を提供できます。キャンペーン、メッセージブリーフ、ブレインストーミングドキュメントの詳細を含めて、オペレーターに状況を把握させることもできます。

#### 具体的にする {#generate-liquid-be-specific}

オペレーターはフォローアップの質問をすることができますが、事前に詳細を提供することで、より正確な結果をより早く得ることができます。以下のような詳細を含めることを検討してください：

- メッセージに関する既知の好みや要件
- メッセージ受信者からの応答がない場合やフォールバックメッセージオプションなど、状況の処理方法に関する指示
- 使用したいカスタム属性の正確な値または類似の値（オペレーターがより正確なロジックを生成・テストするのに役立ちます）
- Connected Contentを使用するLiquidを依頼する場合、APIエンドポイントのドキュメント、サンプルAPIレスポンス、またはその両方

#### 創造性を発揮する {#generate-liquid-get-creative}

さまざまなプロンプトを試して、オペレーターがメッセージングをどのように強化できるかを確認してください。さまざまなプロンプトやアイデアを試してみてください。創造性がより魅力的な結果につながることがあります。

{% enddetails %}

### 画像の生成 {#generate-images}

オペレーターは、OpenAIのAIシステムであり、Brazeのサードパーティプロバイダーである[GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)を使用して画像を生成します。これにより、自然言語の説明からリアルな画像やアートを作成できます。

[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)で、**アセットをアップロード**パネルから**オペレーターで生成**を選択します。希望する画像を説明すると、オペレーターがそれを生成し、メディアライブラリに直接保存します。

#### プロンプトのヒント {#generate-images-prompt-tips}

- 被写体、スタイル、ムード、色を具体的に説明してください。詳細を含めるほど、より良い結果が得られます。参照画像のアップロードはサポートされていません。
- オペレーターのプロンプトでコンテキストとして[ブランドガイドライン](#apply-brand-guidelines)を適用すると、オペレーターがそれを生成画像に直接適用するため、ブランドのビジュアルスタイルが反映された結果になります。
- 画像生成は、1日のオペレーター使用制限にカウントされます。詳細については、[制限事項](#limitations)を参照してください。

### コンテンツ品質のレビュー {#review-content-quality}

SMS、Androidプッシュ通知、iOSプッシュ通知、従来のアプリ内メッセージの**テスト**タブで、**オペレーターでレビュー**を選択して、送信前にコンテンツをレビューします。デフォルトでは、オペレーターはスペルと文法のエラー、ブランドに合わないまたは不適切なトーン、不適切な言語、不要なコード、テストコンテンツ、レンダリングされていないLiquidについてキャンペーンをレビューし、見つかった問題の修正方法を推奨します。プロンプトで直接、オペレーターにコンテンツのレビュー方法をカスタマイズするよう依頼することもできます。

デフォルトのレビューに加えて、オペレーターに特定のチェックに焦点を当てるよう指示できます。以下のいずれかを確認するようプロンプトすることを検討してください：

- **スペルと文法：** スペルと文法の間違いを校正し、コンテンツの正確性を向上させる修正を提案します。
- **トーン：** トーンが意図したコミュニケーションスタイルに合っているかを評価し、誤解される可能性のある箇所をフラグします。
- **不適切な言語：** 不適切または不快な言語がないかスキャンし、メッセージングを敬意あるものに保つために修正できるようにします。
- **意図しないコンテンツ：** テストユーザーでレンダリングされなかったLiquidを含め、意図せず追加された不要なコード、マークアップ、テストメッセージを検出します。
- **他の言語：** 他の言語で書かれたコンテンツをレビューします。英語以外のコンテンツのサポートは異なる場合があるため、結果を慎重に確認してください。

#### ベストプラクティス {#review-content-quality-best-practices}

コンテンツレビューを最大限に活用するために、以下を検討してください：

- **メッセージを校正する：** コンテンツレビューはエラーの特定に役立ちますが、手動でコンテンツを校正することも依然として重要です。AI生成の提案を参考にしつつ、正確性を確保するためにご自身の判断を使用してください。
- **トーン分析を理解する：** トーン分析の結果は主観的であり、AIモデルの理解に基づいています。有用なインサイトを提供できますが、意図したトーンと会話のコンテキストを考慮して適切な調整を行ってください。
- **フラグされた不適切な言語を再確認する：** 不適切な言語の検出は堅牢に設計されていますが、誤検出が発生する場合があります。フラグされたセクションを慎重にレビューし、必要に応じて適切な変更を行ってください。

## データオートメーションとルックアップ {#data-automation-and-lookup}

オペレーターは、ワークスペースデータやBrazeドキュメントのリファレンスとして機能し、データを直接クエリする必要がある場合にSQLを記述し、Webhookペイロードなどの受信データをBrazeが使用できる形式に変換するコードを生成できます。

### オペレーターが検索できるもの {#what-operator-can-look-up}

オペレーターは、質問に回答したり生成するコンテンツの根拠とするために、以下を参照できます（一例です）：

- Brazeドキュメント
- [セグメント]({{site.baseurl}}/user_guide/audience/segments)
- [カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)と[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)データ
- 既存の[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)と[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas)の設定（ターゲティングや配信設定など）
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [プロモーションコード]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)のレスポンス
- [エージェント]({{site.baseurl}}/user_guide/brazeai/agents)

特定の情報を検索できるかどうかわからない場合は、オペレーターに直接聞いてください。

### パフォーマンスデータの分析 {#analyze-performance-data}

キャンペーンやキャンバスのパフォーマンスについて、オペレーターに自然言語で質問すると、ワークスペースデータからチャート、比較、簡潔なインサイトを返します。表示中のページのコンテキストを必要とするオペレーターのページ対応機能とは異なり、分析機能はダッシュボードのどこからでも回答できます。詳しくは、[オペレーター分析]({{site.baseurl}}/user_guide/brazeai/operator/analyze)を参照してください。

### SQLクエリの記述 {#write-sql-queries}

オペレーターは、[セグメントエクステンション](#campaigns-and-audiences)やクエリビルダーの[クエリテンプレート]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)用のSQLの記述を支援できます。希望するクエリを自然言語で説明すると、オペレーターが実行前に確認するSQLを生成します。

### データ変換コードの生成 {#generate-data-transformation-code}

[データ変換]({{site.baseurl}}/user_guide/data/unification/data_transformation)エディターで、**コードを挿入**を選択して、受信Webhookペイロードを有効なBraze APIリクエストに変換する変換コードを生成します。変換の作成手順については、[変換の作成]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation)を参照してください。

## ワークスペース設定 {#workspace-settings}

オペレーターは、複数のワークスペース設定ページにわたって設定を確認・更新できます。変更したい内容を説明すると、オペレーターがアクションカードとして提案し、保存前に確認できます。サポートされている設定ページには、以下が含まれますが、これらに限定されません。

- [サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- [プッシュ設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings)
- [メッセージングレート制限]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)
- [承認ワークフロー]({{site.baseurl}}/user_guide/messaging/governance/approvals)（[メッセージングルール]({{site.baseurl}}/user_guide/messaging/governance/approvals/messaging_rules)および常時承認を含む）
- [APIと識別子]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)（[その他の識別子]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers#other-identifiers)およびAPI制限を含む）
- [管理者設定の連絡先情報]({{site.baseurl}}/user_guide/administer/global/admin_settings/contact_information)

{% alert note %}
オペレーターがカバーする設定ページは定期的に拡大しています。設定可能な内容の最新情報については、**オペレーターに直接お問い合わせください**。
{% endalert %}

## 制限事項 {#limitations}

{% alert note %}
Operatorの対応範囲は頻繁に変更されます。特定の画面やワークフローがサポートされているかどうかわからない場合は、Operatorに直接聞いてください。
{% endalert %}

Operatorのダッシュボードサポートは広範ですが、制限があります。

- **キャンバス：** Operatorは[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas)の作成や編集はできませんが、既存のキャンバスの設定（ターゲティングや配信設定など）を参照して、質問に回答したり出力の根拠とすることができます。
- **キャンペーンの複製：** Operatorはキャンペーン一覧ビューから既存のキャンペーンを複製することはできません。類似のキャンペーンを作成するには、Operatorに新規作成を依頼するか、一覧ビューの**その他のアクション**メニューから手動でキャンペーンを複製してください。
- **ドラッグ＆ドロップエディター：** Operatorは、[メール]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)、[バナー]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner)、[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)のドラッグ＆ドロップエディターでメッセージデザインを直接生成・挿入することはできません。対応するHTMLエディターに切り替えてOperatorを使用するか、コピーなどのコンテンツを生成して手動で貼り付けるようOperatorに依頼してください。対応するチャネルとエディターについては、[メッセージの生成](#generate-messages)を参照してください。
- **画面の可視性：** Operatorは、対応するプレビューやエディター内のコンテンツを含め、表示中のページを理解するためにページ対応コンテキストを使用します。Operatorが読み取れない部分がある場合、推測する代わりにその旨を通知するため、そのコンテンツを自分で説明する必要があることがわかります。
- **使用制限：** Operatorには、24時間ごとにリセットされる会社全体の1日の使用制限があります。画像生成はこの制限にカウントされます。制限に達すると、「1日の使用制限を超えました」というメッセージが表示され、リセットされるまでリクエストを送信できなくなります。トラブルシューティングの手順については、[トラブルシューティング]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting)を参照してください。

## レガシーアシスタント {#legacy-assistants}

Operator以前は、AIコピーライター、AI Liquidアシスタント、AI画像ジェネレーター、AI SQLジェネレーター、データ変換AI Copilot、コンテンツレビューなど、いくつかのAI機能が個別のスタンドアロンアシスタントとして存在していました。これらのエントリポイントはすべてそのまま残っており、Operatorにルーティングされるため、既存のワークフローに影響はありません。これらの現在の機能については、[コンテンツとクリエイティブ](#content-and-creative)および[データオートメーションとルックアップ](#data-automation-and-lookup)を参照してください。

{% multi_lang_include brazeai/generative_ai/policy.md %}

## データプライバシーとセキュリティ {#data-privacy-and-security}

Operatorは出力を生成するためにOpenAIと統合しています。BrazeがOpenAIに送信する情報、そのデータの使用方法、知的財産権の詳細については、[OpenAIでのデータの使用方法]({{site.baseurl}}/user_guide/brazeai/operator#data-privacy-and-security)を参照してください。

## 次のステップ {#next-steps}

- [Operatorを始める]({{site.baseurl}}/user_guide/brazeai/operator)：Operatorへのアクセスと使用方法
- [プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)：すぐに使えるプロンプト例を閲覧
- [アクションのレビュー]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)：Operatorが提案した変更のレビューと承認
- [トラブルシューティング]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting)：一般的な問題と解決策のリファレンス