---
nav_title: オペレーター
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "BrazeAI Operator<sup>TM</sup>へのアクセス方法と使用方法について説明します。これはBrazeダッシュボードに組み込まれたAI搭載のアシスタントで、その機能やベストプラクティスを紹介します。"
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup>は、ダッシュボードに組み込まれたAI搭載のアシスタントです。Operatorは、質問への回答、セットアップの手順案内、問題のトラブルシューティング、アイデアのブレインストーミングなど、さまざまな作業をサポートします。

## Operatorにアクセスする {#access-operator}

Brazeダッシュボードの任意のページからOperatorを開きます。

1. ユーザープロファイルの横にある**BrazeAI Operator<sup>TM</sup>**を選択します。

![ユーザープロファイルの横にあるBrazeAI Operatorアイコン。]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. 画面の右側にOperatorチャットパネルが開きます。

![Operatorチャットパネル。]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
パネルを最大化して読みやすくしたり、最小化して作業中もOperatorを利用可能な状態に保つことができます。
{% endalert %}

Operatorでできることの一例を、こちらの動画でご覧ください。

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Operatorを使用する {#use-operator}

自然言語を使って、達成したいことを説明します。プロンプトは、シンプルな質問から複雑なリクエストまで対応できます。

- **シンプル：** Liquidが正しくレンダリングされないのはなぜですか？
- **複雑：** メッセージの`abort_message`タグに、中止の原因となったユーザー属性を含めるにはどうすればよいですか？

Operatorは、ステップバイステップの手順、Brazeドキュメントへのリンク、わかりやすい説明を提供できます。明確で具体的な質問をすることで、より有益な回答が得られます。Operatorは[GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2)を使用しており、強力な推論能力を備え、複雑なマルチステップのタスクに適しています。すぐに使えるプロンプト例については、[プロンプトライブラリー]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)を参照してください。

## ベストプラクティス {#best-practices}

Operatorを検索エンジンではなく会話として扱いましょう。短く自然なプロンプトが最も効果的です。

- **具体的に：** 「Canvasについて教えてください」ではなく、「Canvasでアクションパスをどのように使用しますか？」と聞いてみましょう。
- **フォローアップの質問をする：** 最初の回答がニーズに合わない場合は、明確化や追加の詳細を求めましょう。
- **ページ認識コンテキストを活用する：** OperatorはBraze内での現在の位置を理解します。最も正確な結果を得るために、関連するページを表示しながらOperatorを開きましょう。

## 体験をカスタマイズする {#customize-your-experience}

### ブランドガイドラインを適用する {#apply-brand-guidelines}

Operatorのクエリにブランドガイドラインをコンテキストとして追加することで、ブランドの声、トーン、パーソナリティに合った回答を得ることができます。Operatorはワークスペースで設定されたブランドガイドラインを使用するため、コピーの提案や機能の説明時に一貫したメッセージングを確保できます。

ブランドガイドラインを設定するには、**設定** > **ブランドガイドライン**に移動します。詳細については、[ブランドガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)を参照してください。

![Operatorチャットパネルでのブランドガイドラインの選択。]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### ページ認識コンテキストを活用する {#leverage-page-aware-context}

Operatorは、Braze内での現在の位置を自動的に理解し、そのコンテキストに基づいて回答を調整します。たとえば、Canvasの作成中にOperatorを開くと、ワークフローのどこにいるかを説明しなくても、関連するステップを提案したり、Canvasの機能についてのガイダンスを提供したりできます。

このコンテキスト認識により、「Canvasワークフローに遅延ステップを追加するにはどうすればよいですか？」ではなく、「遅延を追加するにはどうすればよいですか？」のように、より短く自然な質問ができます。ダッシュボードのページ別に整理されたすぐに使えるプロンプトについては、[プロンプトライブラリー]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)を参照してください。

## Operatorの回答を活用する {#work-with-operator-responses}

### 推奨プロンプトから始める {#get-started-with-suggested-prompts}

Operatorとの会話を開くと、一般的なタスクと現在のページに基づいて推奨プロンプトが表示されます。すぐに始めるにはプロンプトを選択するか、独自の質問を入力します。

### Operatorの思考プロセスを理解する {#understand-how-operator-thinks}

Operatorは、**Reasoned**とラベル付けされた折りたたみ可能なセクションに推論ステップを表示します。ドロップダウンを選択してこれらのセクションを展開し、Operatorがどのように回答を導き出したかを確認できます。提案の背後にあるロジックを理解したり、アプローチを検証したりする際に役立ちます。

![Operatorの回答内の折りたたまれた「Reasoned」ドロップダウン。]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operatorでアクションを実行する {#take-action-with-operator}

Operatorは、フォームフィールドの入力、設定の更新、コンテンツの生成など、Brazeダッシュボードで直接変更を提案・実行できます。提案された変更はそれぞれアクションカードとして表示され、適用前に確認・承認できます。この仕組みの詳細については、[アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)を参照してください。

### 回答を他のツールにコピーする {#copy-responses-to-other-tools}

Operatorの回答はMarkdown形式でフォーマットされています。回答を受け取ったら、表示されるツールバーの**コピー**を選択して、回答全体をクリップボードにコピーできます。ほとんどのツールはMarkdownをネイティブにレンダリングするか、わずかな調整で受け入れます。コピー先に応じてタブを選択してください。

{% tabs %}
{% tab Google Docs %}

まず、**Tools** > **Preferences**に移動し、**Automatically detect Markdown**を選択します。次に、Markdownを貼り付けるには、**Edit** > **Paste from Markdown**に移動します。右クリックして**Paste from Markdown**を選択することもできます。

{% endtab %}
{% tab Microsoft WordとOutlook %}

WordとOutlookはMarkdownをネイティブにレンダリングしません。回答をWebベースのMarkdownプレビューアーに貼り付け、レンダリングされた出力をコピーして、**Keep Source Formatting**でWordまたはOutlookに貼り付けます。または、プレーンテキストとして貼り付けて手動でフォーマットします。

{% endtab %}
{% tab ConfluenceとNotion %}

直接貼り付けます。両方のプラットフォームがMarkdownを自動的にレンダリングします。

{% endtab %}
{% tab Slack %}

直接貼り付けます。Slackは太字、インラインコード、コードブロック、ブロック引用、箇条書きリストをレンダリングしますが、Markdownの見出しやリンク構文はレンダリングしません。

{% endtab %}
{% tab その他のツール %}

ファイルで作業したり、変換ツールを使用したりする場合は、以下の方法もあります。

- [VS Code](https://code.visualstudio.com/)などのテキストエディターを開いて新しいテキストファイルを作成し、Markdownを貼り付けてプレビューでフォーマットを確認してから、変換または他の場所に貼り付けます。
- [Pandoc](https://pandoc.org/)を使用して、MarkdownをWord文書、HTML、またはPDFに変換します。ブラウザーからの貼り付けなしで、WordやOutlookで予測可能な構造が必要な場合に便利です。

{% endtab %}
{% endtabs %}

## セッションを管理する {#manage-your-session}

### 回答を停止する {#stop-a-response}

Operatorが回答を生成している間、**送信**ボタンは**停止**ボタンに変わります。質問を言い換えたい場合や、回答が意図しない方向に進んでいる場合は、**停止**を選択して回答を早期に終了できます。

### 履歴をクリアする {#clear-your-history}

最初からやり直したい場合や、会話から機密情報を削除したい場合は、**チャット履歴をクリア**を選択します。これにより、現在のすべてのコンテンツが削除され、会話のコンテキストがリセットされます。

### フィードバックを提供する {#provide-feedback}

各回答の下部にある、サムズアップまたはサムズダウンボタンを使って、素早くフィードバックを提供できます。フィードバックは、Operatorの回答を継続的に改善するのに役立ちます。

## データプライバシーとセキュリティ {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup>はOpenAIと統合されており、OpenAIはお客様とBraze間のData Processing Addendum（DPA）に基づくBrazeのサブプロセッサーとして機能します。Brazeを介してOpenAIに送信されるデータは、OpenAIモデルのトレーニングや改善には使用されません。HIPAAコンプライアンス、データ保持、PII処理、ガバナンスの詳細については、[データプライバシーとセキュリティ]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)を参照してください。

## 次のステップ {#next-steps}

- [プロンプトライブラリー]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)：ダッシュボードのページ別に整理されたプロンプト例を参照できます
- [アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)：Operatorが提案した変更を確認・承認する方法を学べます
- [サポートチケットの提出]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets)：Operatorから直接サポートチケットを提出できます
- [トラブルシューティング]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting)：よくある問題とソリューションを参照できます
- [データプライバシーとセキュリティ]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)：HIPAAコンプライアンス、データ保持、PII最小化のガイダンスを確認できます