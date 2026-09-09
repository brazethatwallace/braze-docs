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

## Operatorにアクセスする {#access-operator}

Brazeダッシュボードの任意のページからOperatorを開きます。

1. ユーザープロファイルの横にある**BrazeAI Operator<sup>TM</sup>**を選択します。
2. サイドパネルにOperatorのチャットパネルが開きます。

![Operatorのチャットパネル。]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
パネルを最大化すると読みやすくなります。また、最小化すると作業中もOperatorを利用可能な状態に保てます。
{% endalert %}

## Operatorを使用する {#use-operator}

自然言語を使用して、達成したいことを説明してください。明確で具体的なプロンプトを使用すると、より有用な回答が得られます。プロンプトは、単一の質問から完全なビルドリクエストまで幅広く使用できます。

- **質問する:** Liquidが正しくレンダリングされないのはなぜですか？
- **何かを作成する:** 過去7日間にカートを放棄したユーザーのセグメントを下書きしてください。

Operatorは、ステップバイステップの手順、Brazeドキュメントへのリンク、わかりやすい説明、キャンペーン、キャンバス、セグメント、コンテンツの下書きを提供し、それらを確認して作業に直接挿入できます。Operatorが変更を提案・適用する方法については、[Operatorでアクションを実行する](#take-action-with-operator)を参照してください。

Operatorは[GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra)を使用しており、複雑なマルチステップタスクに適しています。Operatorで構築できる内容の全範囲については、[Operatorでできること]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)を参照してください。すぐに使える例については、[プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)を参照してください。

Operatorでできることの一例をこちらの動画でご覧ください。

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## ベストプラクティス {#best-practices}

Operatorを検索エンジンではなく、会話として扱いましょう。短く自然なプロンプトが最も効果的です。

- **具体的に伝える：**「キャンバスについて教えて」ではなく、「キャンバスでアクションパスを使うにはどうすればいいですか？」のように質問してみてください。
- **フォローアップの質問をする：** 最初の回答がニーズに合わない場合は、明確化や追加の詳細を求めてください。Operatorはチャット履歴をクリアするまで、会話の以前のメッセージを記憶しています。
- **ページ対応コンテキストを活用する：** OperatorはBraze内での現在のページを理解しています。最も正確な結果を得るには、関連するページを表示した状態でOperatorを開いてください。

## 体験をカスタマイズする {#customize-your-experience}

### ブランド・ガイドラインを適用する {#apply-brand-guidelines}

ブランド・ガイドラインをコンテキストとして追加すると、Operatorがコピーの提案や機能の説明をする際に、ブランドの声、トーン、パーソナリティに合わせることができます。

1. チャットパネルで<i class="fa-regular fa-plus"></i>&nbsp;**Add context for Operator**を選択します。
2. **Brand guidelines**で、1つ以上のガイドラインを選択します。

Operatorは選択したガイドラインのみを適用します。ワークスペースのデフォルトを含め、デフォルトでは何も選択されていません。

エージェントコンソールの**Generate with Operator**または**Refine with Operator**からOperatorを開くと、Operatorはエージェントに既に設定されているガイドラインをコンテキストとして添付します。同じメニューからガイドラインを追加または削除できます。

ブランド・ガイドラインを設定するには、**コンテンツ** > **ブランド・ガイドライン**に移動します。詳細については、[ブランド・ガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)を参照してください。

![Operatorチャットパネルでブランド・ガイドラインを選択する画面。]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### ページ対応コンテキストの活用 {#leverage-page-aware-context}

Operatorは、Braze内での現在の位置を自動的に理解し、そのコンテキストに基づいて回答を調整します。たとえば、キャンバスを構築中にOperatorを開くと、ワークフロー内のどこにいるかを説明しなくても、関連するステップを提案したり、キャンバスの機能に関するガイダンスを提供したりできます。

このコンテキスト認識により、Operatorと短く自然なプロンプトでやり取りできます。たとえば「エディター設定をブランド・ガイドラインに合わせて更新して」などです。リクエストにダッシュボードの別の部分が必要な場合、Operatorが直接[そこへ移動します]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard)。


すぐに使えるプロンプトのアイデアについては、[プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)を参照してください。

## Operatorの回答を活用する {#work-with-operator-responses}

### 推奨プロンプトで始める {#get-started-with-suggested-prompts}

Operatorとの会話を開くと、よくあるタスクや現在のページに基づいた推奨プロンプトが表示されます。いずれかを選択してすぐに始めるか、独自の質問を入力してください。

### Operatorの思考プロセスを理解する {#understand-how-operator-thinks}

Operatorは、**Reasoned**というラベルの折りたたみ可能なセクションに推論ステップを表示します。ドロップダウンを選択してこれらのセクションを展開すると、Operatorがどのように回答を導き出したかを確認できます。これは、提案の背後にあるロジックを理解したり、アプローチを検証したりしたい場合に役立ちます。

![Operatorの回答内の折りたたまれた「Reasoned」ドロップダウン。]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operatorでアクションを実行する {#take-action-with-operator}

Operatorは、フォームフィールドの入力、設定の更新、コンテンツの生成、リクエストを完了するための別のページへのナビゲーションなど、Brazeダッシュボードで直接変更を提案し実行できます。提案された各変更は、適用前に確認・承認できるアクションカードとして提示されます。この仕組みの詳細については、[アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)を参照してください。

### 回答を他のツールにコピーする {#copy-responses-to-other-tools}

Operatorの回答はMarkdown形式でフォーマットされています。回答を受け取ったら、表示されるツールバーの**Copy**を選択して、回答全体をクリップボードにコピーできます。ほとんどのツールはMarkdownをネイティブにレンダリングするか、わずかな調整で受け入れます。コピー先に応じてタブを選択してください。

{% tabs %}
{% tab Google Docs %}

まず、**Tools** > **Preferences**に移動し、**Automatically detect Markdown**を選択します。次にMarkdownを貼り付けるには、**Edit** > **Paste from Markdown**に移動します。右クリックして**Paste from Markdown**を選択することもできます。

{% endtab %}
{% tab Microsoft WordとOutlook %}

WordとOutlookはMarkdownをネイティブにレンダリングしません。回答をWebベースのMarkdownプレビューアーに貼り付け、レンダリングされた出力をコピーして、**Keep Source Formatting**でWordまたはOutlookに貼り付けてください。または、プレーンテキストとして貼り付けて手動でフォーマットすることもできます。

{% endtab %}
{% tab ConfluenceとNotion %}

直接貼り付けてください。両方のプラットフォームがMarkdownを自動的にレンダリングします。

{% endtab %}
{% tab Slack %}

直接貼り付けてください。Slackは太字、インラインコード、コードブロック、ブロック引用、箇条書きリストをレンダリングしますが、Markdownの見出しやリンク構文はレンダリングしません。

{% endtab %}
{% tab その他のツール %}

ファイルで作業したり変換ツールを使用したい場合は、以下の方法もあります。

- [VS Code](https://code.visualstudio.com/)などのテキストエディターを開いて新しいテキストファイルを作成し、Markdownを貼り付けてプレビューでフォーマットを確認してから、変換したり他の場所に貼り付けたりします。
- [Pandoc](https://pandoc.org/)を使用して、MarkdownをWord文書、HTML、またはPDFに変換すれば、ブラウザからの貼り付けなしでWordやOutlookで予測可能な構造を得られます。

{% endtab %}
{% endtabs %}

## セッションを管理する {#manage-your-session}

### 応答を停止する {#stop-a-response}

オペレーターが応答を生成している間、**送信**ボタンは**停止**ボタンに変わります。質問を言い換えたい場合や、応答が意図しない方向に進んでいる場合は、**停止**を選択して応答を途中で終了できます。

### 履歴をクリアする {#clear-your-history}

最初からやり直したい場合や、会話から機密情報を削除したい場合は、**チャット履歴をクリア**を選択します。これにより、現在のすべてのコンテンツが削除され、会話のコンテキストがリセットされます。

### フィードバックを送る {#provide-feedback}

各応答の下部にある「いいね」または「よくないね」ボタンを使用して、簡単なフィードバックを送ることができます。フィードバックは、オペレーターの回答を継続的に改善するために役立てられます。

## データプライバシーとセキュリティ {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup>はOpenAIと統合しており、OpenAIはお客様とBraze間のデータ処理補遺（DPA）の条件に従うBrazeのサブプロセッサーとして機能します。Brazeを通じてOpenAIに送信されるデータは、OpenAIモデルのトレーニングや改善には使用されません。HIPAAコンプライアンス、データ保持、PII処理、ガバナンスの詳細については、[データプライバシーとセキュリティ]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)を参照してください。

## 次のステップ {#next-steps}

{% article_tiles %}
- name: Operatorでできること
  link: /docs/user_guide/brazeai/operator/capabilities
- name: プロンプトライブラリ
  link: /docs/user_guide/brazeai/operator/prompt_library
- name: アクションの確認
  link: /docs/user_guide/brazeai/operator/reviewing_actions
- name: サポートチケットの提出
  link: /docs/user_guide/brazeai/operator/support_tickets
- name: トラブルシューティング
  link: /docs/user_guide/brazeai/operator/troubleshooting
- name: データプライバシーとセキュリティ
  link: /docs/user_guide/brazeai/operator/data_privacy_security
{% endarticle_tiles %}