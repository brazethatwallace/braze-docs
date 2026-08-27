---
nav_title: オペレーター
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "BrazeAI Operator<sup>TM</sup>へのアクセス方法と使用方法について説明します。これはBrazeダッシュボードに組み込まれたAI搭載のアシスタントで、その機能やベストプラクティスを紹介します。"
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup>は、ダッシュボードに組み込まれたAI搭載のアシスタントです。オペレーターは、キャンペーン、キャンバス、セグメント、コンテンツの下書きなどの構築を支援するほか、質問への回答、問題のトラブルシューティング、アイデアのブレインストーミングなど、行き詰まった際のサポートも行います。

## オペレーターにアクセスする {#access-operator}

Brazeダッシュボードの任意のページからオペレーターを開きます。

1. ユーザープロファイルの横にある**BrazeAI Operator<sup>TM</sup>**を選択します。
2. サイドパネルにオペレーターチャットパネルが開きます。

![オペレーターチャットパネル。]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
パネルを最大化すると読みやすくなります。作業中もオペレーターを利用できるよう、最小化しておくこともできます。
{% endalert %}

## オペレーターを使用する {#use-operator}

自然言語で達成したいことを説明してください。明確で具体的なプロンプトほど、より有用な回答が得られます。プロンプトは、1つの質問から完全なビルドリクエストまで多岐にわたります。

- **質問する：** Liquidが正しくレンダリングされないのはなぜですか？
- **何かを作成する：** 過去7日間にカートを放棄したユーザーのセグメントを下書きしてください。

オペレーターは、ステップバイステップの手順、Brazeドキュメントへのリンク、わかりやすい説明、キャンペーン、キャンバス、セグメント、コンテンツの下書きを提供でき、それらを確認して作業に直接挿入できます。オペレーターが変更を提案・適用する方法については、[オペレーターでアクションを実行する](#take-action-with-operator)を参照してください。

オペレーターは[GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra)を使用しており、複雑なマルチステップタスクに適しています。オペレーターで構築できる内容の全範囲については、[Operatorでできること]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)を参照してください。すぐに使えるプロンプト例については、[プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)を参照してください。

オペレーターでできることの一例をこちらの動画でご覧ください。

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## ベストプラクティス {#best-practices}

Operatorは検索エンジンではなく、会話として扱ってください。短く自然なプロンプトが最も効果的です。

- **具体的に質問する：**「キャンバスについて教えて」ではなく、「キャンバスでアクションパスをどう使えばいいですか？」と聞いてみてください。
- **フォローアップの質問をする：** 最初の回答がニーズに合わない場合は、さらに明確化や詳細を求めてください。Operatorはチャット履歴をクリアするまで、会話の中で以前のメッセージを記憶しています。
- **ページ対応コンテキストを活用する：** OperatorはBraze内での現在の表示位置を理解しています。最も正確な結果を得るために、関連するページを表示した状態でOperatorを開いてください。

## 体験をカスタマイズする {#customize-your-experience}

### ブランド・ガイドラインを適用する {#apply-brand-guidelines}

ブランド・ガイドラインをコンテキストとしてOperatorのクエリに追加すると、回答がブランドの声、トーン、パーソナリティに合うようになります。Operatorはワークスペースで設定されたブランド・ガイドラインを使用するため、コピーの提案や機能の説明時に一貫したメッセージングを確保できます。

ブランド・ガイドラインを設定するには、**コンテンツ** > **ブランド・ガイドライン**に移動します。詳細については、[ブランド・ガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)を参照してください。

![Operatorチャットパネルでブランド・ガイドラインを選択する画面。]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### ページ対応コンテキストを活用する {#leverage-page-aware-context}

Operatorは、Braze内でのあなたの現在位置を自動的に把握し、そのコンテキストに基づいて回答を調整します。たとえば、キャンバスの構築中にOperatorを開くと、ワークフローのどこにいるかを説明しなくても、関連するステップを提案したり、キャンバス機能に関するガイダンスを提供したりできます。

このコンテキスト認識により、「エディターの設定をブランド・ガイドラインに合わせて更新して」のような短く自然なプロンプトでOperatorとやり取りできます。リクエストにダッシュボードの別の部分が必要な場合、Operatorは直接[そこへ移動します]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard)。


すぐに使えるプロンプトのアイデアについては、[プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)を参照してください。

## オペレーターの応答を活用する {#work-with-operator-responses}

### おすすめプロンプトで始める {#get-started-with-suggested-prompts}

オペレーターとの会話を開くと、一般的なタスクと現在のページに基づいておすすめのプロンプトが表示されます。いずれかを選択してすぐに始めるか、自分の質問を入力してください。

### オペレーターの思考プロセスを理解する {#understand-how-operator-thinks}

オペレーターは、**Reasoned**というラベルの折りたたみ可能なセクションに推論ステップを表示します。ドロップダウンを選択してこれらのセクションを展開し、オペレーターがどのように回答を導き出したかを確認できます。提案の背後にあるロジックを理解したい場合やアプローチを検証したい場合に役立ちます。

![オペレーターの応答内で折りたたまれた「Reasoned」ドロップダウン。]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### オペレーターでアクションを実行する {#take-action-with-operator}

オペレーターは、フォームフィールドの入力、設定の更新、コンテンツの生成、リクエストを完了するための別のページへのナビゲーションなど、Brazeダッシュボードで直接変更を提案・実行できます。提案された各変更は、適用前にレビューして承認できるアクションカードとして提示されます。仕組みの詳細については、[アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)を参照してください。

### 応答を他のツールにコピーする {#copy-responses-to-other-tools}

オペレーターの応答はMarkdown形式でフォーマットされています。応答を受け取ったら、表示されるツールバーの**Copy**を選択して、応答全体をクリップボードにコピーします。ほとんどのツールはMarkdownをネイティブにレンダリングするか、わずかな調整で受け入れます。コピー先に応じてタブを選択してください。

{% tabs %}
{% tab Google Docs %}

まず、**Tools** > **Preferences**に移動し、**Automatically detect Markdown**を選択します。次に、Markdownを貼り付けるには、**Edit** > **Paste from Markdown**に移動します。右クリックして**Paste from Markdown**を選択することもできます。

{% endtab %}
{% tab Microsoft Word and Outlook %}

WordとOutlookはMarkdownをネイティブにレンダリングしません。応答をWebベースのMarkdownプレビューアーに貼り付けてから、レンダリングされた出力をコピーし、**Keep Source Formatting**でWordまたはOutlookに貼り付けてください。または、プレーンテキストとして貼り付けて手動でフォーマットすることもできます。

{% endtab %}
{% tab Confluence and Notion %}

そのまま貼り付けてください。どちらのプラットフォームもMarkdownを自動的にレンダリングします。

{% endtab %}
{% tab Slack %}

そのまま貼り付けてください。Slackは太字、インラインコード、コードブロック、引用、箇条書きリストをレンダリングしますが、Markdownの見出しやリンク構文はレンダリングしません。

{% endtab %}
{% tab その他のツール %}

ファイルで作業したい場合や変換ツールを使用したい場合は、以下の方法もあります。

- [VS Code](https://code.visualstudio.com/)などのテキストエディターを開いて新しいテキストファイルを作成し、Markdownを貼り付けてプレビューでフォーマットを確認してから、変換したり別の場所に貼り付けたりします。
- [Pandoc](https://pandoc.org/)を使用して、MarkdownをWord文書、HTML、またはPDFに変換します。ブラウザーから貼り付けずにWordやOutlookで安定した構造が必要な場合に便利です。

{% endtab %}
{% endtabs %}

## セッションを管理する {#manage-your-session}

### 応答を停止する {#stop-a-response}

オペレーターが応答を生成している間、**送信**ボタンは**停止**ボタンに変わります。質問を言い換えたい場合や、応答が意図しない方向に進んでいる場合は、**停止**を選択して応答を途中で終了できます。

### 履歴をクリアする {#clear-your-history}

会話をリセットしたり、会話からセンシティブな情報を削除したりするには、**チャット履歴をクリア**を選択します。これにより、現在のコンテンツがすべて削除され、会話のコンテキストがリセットされます。

### フィードバックを送る {#provide-feedback}

各応答の下部にあるサムズアップまたはサムズダウンボタンを使用して、簡単なフィードバックを送信できます。フィードバックは、オペレーターの回答を継続的に改善するために役立てられます。

## データプライバシーとセキュリティ {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup>はOpenAIと統合しており、OpenAIはお客様とBraze間のデータ処理補遺（DPA）の条件に従うBrazeのサブプロセッサーとして機能します。Brazeを通じてOpenAIに送信されるデータは、OpenAIモデルのトレーニングや改善には使用されません。HIPAAコンプライアンス、データ保持、PII処理、ガバナンスの詳細については、[データプライバシーとセキュリティ]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)を参照してください。

## 次のステップ {#next-steps}

- [Operatorでできること]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)：ダッシュボード全体にわたるオペレーターの機能を確認できます
- [プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)：ダッシュボードページ別に整理されたプロンプト例を閲覧できます
- [アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)：オペレーターが提案した変更を確認・承認する方法を説明します
- [サポートチケットの提出]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets)：オペレーターから直接サポートチケットを提出できます
- [トラブルシューティング]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting)：よくある問題と解決策を参照できます
- [データプライバシーとセキュリティ]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)：HIPAAコンプライアンス、データ保持、PII最小化に関するガイダンスを確認できます