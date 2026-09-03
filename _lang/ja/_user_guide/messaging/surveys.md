---
nav_title: アンケート
article_title: アンケート
page_order: 9
page_type: reference
channel:
  - landing pages
  - in-app messages
description: "Brazeアンケートを使用して、ランディングページやアプリ内メッセージでファーストパーティフィードバックを収集する方法（分析、フォームブロック、Currentsエクスポートを含む）について説明します。"
---

# アンケート {#surveys}

> Brazeアンケートでは、ユーザーからファーストパーティフィードバックを直接収集し、Brazeダッシュボードを離れることなくフォローアップメッセージングに活用できます。アンケートを使用して、ユーザーの意見を把握し、好みを収集し、回答からセグメントやトリガーを構築できます。


## チャネルの利用可否 {#channel-availability}

アンケートは2つのチャネルで利用できます。各チャネルページでは、チャネル固有の作成フロー、コンポジション、レポートの場所について説明しています。このページでは、両方に共通するコンセプトと機能について説明します。

| チャネル | アンケートの作成場所 |
| --- | --- |
| ランディングページ | [ランディングページアンケート]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| アプリ内メッセージ | [アプリ内メッセージアンケート]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アンケートチャネルの利用可否" }

## アンケートページ {#surveys-page}

**メッセージング** > **アンケート**に移動すると、ランディングページ、キャンペーン、キャンバスのアンケートを1か所で確認できます。チャネル全体のアンケートパフォーマンスを確認するためのエントリポイントとして使用してください。

{% alert note %}
**メッセージング**の下に**アンケート**が表示されない場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 分析 {#analytics}

すべてのアンケートの質問タイプには、デフォルトで拡張レポートが含まれているため、セグメントを構築したり別のツールにエクスポートしたりすることなく、回答データを一目で確認できます。

トップレベルの分析には以下が含まれます：

- **すべての回答：**完了した回答と未完了の回答の合計
- **完了：**すべての必須質問を完了したユーザー
- **一部完了：**一部のデータを送信したが、すべての必須質問を完了しなかったユーザー
- **ユニークインプレッション：**合計ページビュー数

![NPSスコア分析を表示するアンケート回答ページ。推奨者、中立者、批判者のパーセンテージとスコア分布の水平棒グラフが表示されています。]({% image_buster /assets/img/surveys/survey_responses.png %})

### チャートタイプ {#chart-types}

ラジオボタン、ドロップダウン、チェックボックスのフォームブロックでは、アンケート分析ビューで3つのチャートタイプから選択できます。これにより、サードパーティツールにエクスポートすることなく、インサイトを解釈・共有する柔軟性が高まります。

| チャートタイプ | 最適な用途 |
| --- | --- |
| **棒グラフ** | 回答数とパーセンテージのデフォルトの水平表示です。 |
| **縦棒グラフ** | 回答数とパーセンテージの垂直表示です。複数選択の質問や回答選択肢が多い質問の回答を並べて比較する場合に使用します。 |
| **円グラフ** | 回答の比率の内訳です。回答が選択肢全体にどのように分布しているかを確認したい単一選択の質問に使用します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アンケートのチャートタイプ" }

各チャートには、回答が届くとリアルタイムでデータが表示されます。チャートタイプはいつでも切り替えることができ、基になるデータには影響しません。

![棒グラフを使用したアンケートの質問レベルの内訳。]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## マルチステップランディングページフォーム {#multi-step-landing-page-forms}

複数のスタンドアロンランディングページを作成して手動でリンクする代わりに、自動的にリンクされる複数のステップを持つ単一のランディングページとしてアンケートを構築できます。たとえば、各アンケートの質問ごとに個別のステップを定義し、最後に確認ステップを追加できます。

この機能はランディングページチャネル固有のものです。アプリ内メッセージアンケートもステップ間の移動にページマネージャーをサポートしています。詳細については、[アプリ内メッセージアンケートの作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey)を参照してください。

![マルチステップフォームのプレビューと、ステップ一覧とロックされた確認ステップが表示されたフォームプロパティパネルを備えたランディングページエディター。]({% image_buster /assets/img/surveys/multi_step.png %})

## 質問とフォームブロック {#question-and-form-blocks}

ランディングページとアプリ内メッセージは、ラジオボタングループ、チェックボックス、チェックボックスグループ、ドロップダウン、電話番号キャプチャ、メールキャプチャ、ショートテキストキャプチャなど、すべての標準フォームブロックをアンケートでもサポートしています。このセクションでは、アンケート専用のレポートが組み込まれた3つのフォームブロック（NPS、数値スケール、長文テキスト）について説明します。

{% tabs local %}
{% tab NPS %}
### スタンドアロンNPSブロック {#standalone-nps-block}

**NPS**ブロックは、**評価**（数値スケール）ブロックとは別のフォームブロックであり、その設定オプションではありません。アンケートに追加して、標準的なNet Promoter Scoreの質問（0〜10）を尋ね、そのユースケース専用に構築されたレポートを取得できます。

**NPS**ブロックは、同じ目的で使用するプレーンな評価質問よりも優れたダッシュボードレポートを提供します。番号ごとの単純な回答数のカウントではなく、Brazeが回答を推奨者（9〜10）、中立者（7〜8）、批判者（0〜6）に自動的にグループ化し、それらのセグメントと結果のNPSスコアをアンケート分析ビューに直接表示します。

Currentsは、**Survey Response**イベントで数値スコア（および追加された場合はフリーテキストフィードバックフィールド）をエクスポートします。推奨者、中立者、批判者のセグメントは個別のCurrentsフィールドではありません。

![モバイルNPSアンケートと、NPSスコア、推奨者・中立者・批判者の内訳、回答分布チャートが表示されたアンケート回答ダッシュボード。]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab 数値スケール %}
### 数値スケール質問 {#number-scale-questions}

チャネルページでは評価スケールとも呼ばれます。どちらの用語も同じ**評価**フォームブロックを指します。1〜5、1〜10、または0〜10の数値スケール質問をキャプチャして、シンプルな満足度評価から推奨可能性スコアまで、さまざまなアンケートやレポートのニーズに対応できます。チャネル固有のコンポジションスクリーンショットについては、[ランディングページアンケート]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale)または[アプリ内メッセージアンケート]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale)ページの評価スケールセクションを参照してください。

評価をアンケートの回答として収集したり、整数カスタム属性として記録したり、あるいはその両方を行ったりできます。数値スケール質問と[長文テキストキャプチャ](#long-form-text-capture)ブロックを組み合わせることで、同じアンケートで数値スコアと定性的なフィードバックを収集できます。

![1〜5の評価質問が選択され、右側に評価プロパティパネルが開かれたランディングページアンケートエディター。]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab 長文テキスト %}
### 長文テキストキャプチャ {#long-form-text-capture}

長文テキストキャプチャは、定性的なフィードバックに役立ちます。最小文字数と最大文字数（最大1,000文字）、コンポジション中に文字数制限を表示するかどうか、テキストエリアの高さ、プレースホルダーテキストを設定できます。

![長文テキストキャプチャブロックの設定。]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

長文テキストの回答はレポートやエクスポートで利用できますが、ユーザープロファイルのカスタム属性として記録することはできません。そのため、長文回答の値でユーザーを直接セグメント化することはできません。詳細については、各チャネルページの[制限事項]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations)を参照してください。

Currentsでは、長文回答は`answer_type = 'free_form_text'`を使用し、テキストは`answer_long_string`に格納されます。
{% endtab %}
{% endtabs %}

## 回答選択肢のランダム化 {#randomized-choice-order}

ラジオボタングループ、チェックボックスグループ、ドロップダウンブロックでは、回答選択肢のランダム化をサポートしています。**Randomize choice order**をオンにすると、アンケートが読み込まれるたびに選択肢がシャッフルされ、同じ最初の選択肢が回答を偏らせる可能性がある場合の順序バイアスを軽減します。

ランダム化は、各アンケート回答者に対する表示順序のみを変更します。レポートのラベルと値は設定した選択肢にマッピングされたままなので、分析、CSVエクスポート、セグメンテーションでは、ユーザーが見た順序に関係なく同じ回答データが使用されます。

## アンケートテンプレート {#survey-templates}

ランディングページまたはアプリ内メッセージのテンプレートライブラリからアンケートをテンプレートとして保存すると、毎回同じ質問やフォームブロックを再作成する代わりに、ビルダーがそのテンプレートから開始できます。ワークスペースでアンケートテンプレートが有効になっている場合は、ライブラリを**Survey**でフィルタリングして、保存されたアンケート構造をキャンペーン、キャンバス、ランディングページ全体で検索し再利用できます。

## Survey Responseイベント {#survey-response-events}

アンケートの回答は[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)に流れるため、アンケートデータをデータウェアハウスやサードパーティのBIツールにエクスポートして、下流の分析、他のエンゲージメントデータとの結合、ダッシュボードの組み込み分析を超えたカスタムレポートに利用できます。

Brazeは、個々のアンケートの回答を**Survey Response**イベント（`users.messages.survey.Response`）を通じてCurrentsにエクスポートします。各イベントは、1人の回答者が1つのアンケートの質問に対して行った回答を表します。完全なフィールドリファレンスについては、Currentsイベント用語集の[Survey Responseイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events)を参照してください。

## ランディングページエンゲージメントファネル {#landing-page-engagement-funnel}

ランディングページアンケートは、ページビューとトラッキングされたクリックに対して**Landing Page Impression**イベントと**Landing Page Click**イベントも生成します。ランディングページアンケートを完了すると**Survey Response**イベントが書き込まれます。標準（非アンケート）のランディングページフォーム用の汎用**Landing Page Form Submission**イベントは発火しません。これらのイベントの完全なフィールドリファレンスについては、[Currentsイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)を参照してください。

## 関連記事 {#related-articles}

- [ランディングページアンケート]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys)：ランディングページチャネルの作成フロー、コンポジション、レポート
- [アプリ内メッセージアンケート]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys)：アプリ内メッセージチャネルの作成フロー、コンポジション、レポート
- [ドラッグ＆ドロップエディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks)：アンケートに追加できるフォームブロックの完全なリファレンス
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)：データウェアハウスやBIツールへのデータエクスポートの設定