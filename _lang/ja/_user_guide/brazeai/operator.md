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
2. サイドパネルにOperatorチャットパネルが開きます。

![Operatorチャットパネル。]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
パネルを最大化すると読みやすくなります。最小化すれば、作業中もOperatorを利用可能な状態に保てます。
{% endalert %}

## Operatorを使用する {#use-operator}

自然言語を使って、達成したいことを記述してください。明確で具体的なプロンプトは、より有用な回答につながります。プロンプトは、単一の質問からフルビルドリクエストまで多岐にわたります。

- **質問する：** Liquidが正しくレンダリングされないのはなぜですか？
- **何かを構築する：** 過去7日間にカートを放棄したユーザーのセグメントを下書きしてください。

Operatorは、ステップバイステップの手順、Brazeドキュメントへのリンク、わかりやすい説明、およびキャンペーン、キャンバス、セグメント、コンテンツの下書きを提供でき、それらを確認して作業に直接挿入できます。Operatorが変更を提案・適用する方法については、[Operatorでアクションを実行する](#take-action-with-operator)を参照してください。

Operatorは[GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra)を使用しており、複雑なマルチステップタスクに適しています。Operatorで構築できる内容の全範囲については、[Operatorでできること]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)を参照してください。すぐに使えるプロンプト例については、[プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)を参照してください。

Operatorでできることの一例を、こちらの動画でご覧ください。

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## ベストプラクティス {#best-practices}

Operatorは検索エンジンではなく、会話として扱ってください。短く自然なプロンプトが最も効果的です。

- **具体的に質問する：** 「キャンバスについて教えて」ではなく、「キャンバスでアクションパスを使うにはどうすればよいですか？」と質問してみてください。
- **フォローアップの質問をする：** 最初の回答がニーズに合わない場合は、追加の説明や詳細を求めてください。Operatorはチャット履歴をクリアするまで、会話の以前のメッセージを記憶しています。
- **ページ対応コンテキストを活用する：** OperatorはBraze内での現在の位置を理解しています。最も正確な結果を得るために、関連するページを表示しながらOperatorを開いてください。

## 体験をカスタマイズする {#customize-your-experience}

### ブランド・ガイドラインを適用する {#apply-brand-guidelines}

ブランド・ガイドラインをコンテキストとして追加することで、Operatorがコピーを提案したり機能を説明したりする際に、ブランドの声、トーン、パーソナリティに合わせることができます。

1. チャットパネルで<i class="fa-regular fa-plus"></i>&nbsp;**Add context for Operator**を選択します。
2. **Brand guidelines**の下で、1つ以上のガイドラインを選択します。

Operatorは選択したガイドラインのみを適用します。ワークスペースのデフォルトを含め、デフォルトでは何も選択されていません。

エージェントコンソールの**Generate with Operator**または**Refine with Operator**からOperatorを開くと、Operatorはエージェントに設定済みのガイドラインをコンテキストとして自動的に添付します。同じメニューからガイドラインを追加または削除できます。

ブランド・ガイドラインを設定するには、**コンテンツ** > **ブランド・ガイドライン**に移動します。詳細については、[ブランド・ガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)を参照してください。

![Operatorチャットパネルでブランド・ガイドラインを選択する。]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### ページ対応コンテキストを活用する {#leverage-page-aware-context}

OperatorはBraze内での現在位置を自動的に把握し、そのコンテキストに基づいて回答を調整します。たとえば、キャンバスの構築中にOperatorを開くと、ワークフローのどこにいるかを説明しなくても、関連するステップを提案したり、キャンバスの機能に関するガイダンスを提供したりできます。

このコンテキスト認識により、「エディターの設定をブランド・ガイドラインに合わせて更新して」のように、短く自然なプロンプトでOperatorとやり取りできます。リクエストにダッシュボードの別の部分が必要な場合、Operatorは直接[そこへ移動]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard)できます。

すぐに使えるプロンプトのアイデアについては、[プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)を参照してください。

## Operatorの応答を活用する {#work-with-operator-responses}

### 提案されたプロンプトで始める {#get-started-with-suggested-prompts}

Operatorとの会話を開くと、一般的なタスクや現在のページに基づいて提案されたプロンプトが表示されます。プロンプトを選択してすぐに開始するか、独自のカスタム質問を入力してください。

### Operatorの思考プロセスを理解する {#understand-how-operator-thinks}

Operatorは、**Reasoned**というラベルの折りたたみ可能なセクションで推論ステップを表示します。ドロップダウンを選択してこれらのセクションを展開し、Operatorがどのように回答を決定したかを確認できます。これは、提案の背後にあるロジックを理解したい場合や、アプローチを検証したい場合に役立ちます。

![Operatorの応答に表示された折りたたまれた「Reasoned」ドロップダウン。]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operatorでアクションを実行する {#take-action-with-operator}

Operatorは、フォームフィールドの入力、設定の更新、コンテンツの生成、リクエストを完了するための別のページへのナビゲーションなど、Brazeダッシュボードで直接変更を提案・実行できます。提案された各変更は、適用される前に確認・承認できるアクションカードとして提示されます。この仕組みの詳細については、[アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)を参照してください。

### 応答を他のツールにコピーする {#copy-responses-to-other-tools}

Operatorの応答はMarkdown形式でフォーマットされています。応答を受け取ったら、表示されるツールバーの**Copy**を選択して、応答全体をクリップボードにコピーします。ほとんどのツールはMarkdownをネイティブにレンダリングするか、わずかな調整で受け入れます。コピー先に応じてタブを選択してください。

{% tabs %}
{% tab Google Docs %}

まず、**Tools** > **Preferences**に移動し、**Automatically detect Markdown**を選択します。次に、Markdownを貼り付けるには、**Edit** > **Paste from Markdown**に移動します。右クリックして**Paste from Markdown**を選択することもできます。

{% endtab %}
{% tab Microsoft Word and Outlook %}

WordとOutlookはMarkdownをネイティブにレンダリングしません。応答をWebベースのMarkdownプレビューアーに貼り付け、レンダリングされた出力をコピーして、**Keep Source Formatting**でWordまたはOutlookに貼り付けてください。または、プレーンテキストとして貼り付けて手動でフォーマットしてください。

{% endtab %}
{% tab Confluence and Notion %}

直接貼り付けてください。両方のプラットフォームがMarkdownを自動的にレンダリングします。

{% endtab %}
{% tab Slack %}

直接貼り付けてください。Slackは太字、インラインコード、コードブロック、引用ブロック、箇条書きリストをレンダリングしますが、Markdownの見出しやリンク構文はレンダリングしません。

{% endtab %}
{% tab その他のツール %}

ファイルで作業したい場合や変換ツールを使用したい場合は、以下の方法もあります。

- [VS Code](https://code.visualstudio.com/)などのテキストエディターを開いて新しいテキストファイルを作成し、Markdownを貼り付けてプレビューでフォーマットを確認してから、他の場所に変換または貼り付けてください。
- [Pandoc](https://pandoc.org/)を使用して、MarkdownをWordドキュメント、HTML、またはPDFに変換すると、ブラウザから貼り付けることなくWordやOutlookで予測可能な構造を得られます。

{% endtab %}
{% endtabs %}

## セッションの管理 {#manage-your-session}

### レスポンスを停止する {#stop-a-response}

オペレーターがレスポンスを生成している間、**送信**ボタンは**停止**ボタンに変わります。質問を言い換えたい場合や、レスポンスが意図した方向と異なる場合は、**停止**を選択してレスポンスを途中で終了できます。

### 履歴をクリアする {#clear-your-history}

会話をリセットしたり、会話から機密情報を削除したりするには、**チャット履歴をクリア**を選択します。これにより、現在のすべてのコンテンツが削除され、会話コンテキストがリセットされます。

### フィードバックを提供する {#provide-feedback}

各レスポンスの下部にある「いいね」または「よくないね」ボタンを使用して、簡単なフィードバックを提供できます。フィードバックは、オペレーターの回答を継続的に改善するために活用されます。

## データプライバシーとセキュリティ {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup>はOpenAIと統合しており、OpenAIはお客様とBraze間のデータ処理補遺（DPA）の条件に従うBrazeのサブプロセッサーとして機能します。Brazeを通じてOpenAIに送信されるデータは、OpenAIモデルのトレーニングや改善に使用されることはありません。HIPAAコンプライアンス、データ保持、PII処理、ガバナンスの詳細については、[データプライバシーとセキュリティ]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)を参照してください。

## 次のステップ {#next-steps}

- [Operatorでできること]({{site.baseurl}}/user_guide/brazeai/operator/capabilities): ダッシュボード全体にわたるオペレーターの機能を確認できます
- [プロンプトライブラリ]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): ダッシュボードページ別に整理されたプロンプト例を閲覧できます
- [アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): オペレーターが提案した変更を確認・承認する方法を説明します
- [サポートチケットの送信]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets): オペレーターから直接サポートチケットを送信できます
- [トラブルシューティング]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): よくある問題と解決策を参照できます
- [データプライバシーとセキュリティ]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security): HIPAAコンプライアンス、データ保持、PII最小化に関するガイダンスを確認できます