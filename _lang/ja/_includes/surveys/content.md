{% comment %}
  Brazeアンケート共通ドキュメント。
  パラメーター:
  - channel (必須): "in_app_message" または "landing_page"
{% endcomment %}

アンケートの概要やチャネル間で共有される機能については、[アンケート]({{site.baseurl}}/user_guide/messaging/surveys)を参照してください。

## 前提条件 {#prerequisites}

アンケートを作成する前に、以下を満たしている必要があります。

{% if include.channel == 'in_app_message' %}
- Brazeワークスペースでアプリ内メッセージにアクセスできること
- [ドラッグ＆ドロップエディターでのアプリ内メッセージの作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)に慣れていること
{% elsif include.channel == 'landing_page' %}
- Brazeワークスペースでランディングページにアクセスできること
- [ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)に慣れていること
{% else %}
- Brazeワークスペースでランディングページ、アプリ内メッセージ、またはその両方にアクセスできること
- [ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)および[ドラッグ＆ドロップエディターでのアプリ内メッセージの作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)に慣れていること
{% endif %}

## アンケートを作成する {#create-a-survey}

アンケートは、既存のメッセージ作成フローの中で構築します。

{% if include.channel == 'in_app_message' %}
1. キャンペーンまたはキャンバスで[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)を作成します。
2. メッセージタイプとして**Survey**を選択します。
{% elsif include.channel == 'landing_page' %}
1. **メッセージング** > **ランディングページ**に移動します。
2. 新しいランディングページを作成します。
3. メッセージタイプとして**Survey**を選択します。
{% else %}
1. **メッセージング** > **ランディングページ**に移動するか、キャンペーンまたはキャンバスで[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)を作成します。
2. 新しいメッセージを作成します。
3. メッセージタイプとして**Survey**を選択します。
{% endif %}

{% if include.channel == 'in_app_message' %}

## アプリ内メッセージアンケートを作成する {#compose-an-in-app-message-survey}

アプリ内メッセージアンケートには、デフォルトで2つのページがあります。

- **ページ1**：ユーザーが質問に回答するページ
- **確認ページ**：アンケートが送信されるページ

デフォルトでは、ボタンは**次のページ**にリンクされています。この動作を変更するには、**アクション**パネルで各ボタンを更新します。

![アプリ内メッセージアンケートのページフローとアクション設定。]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## アンケートフォームブロックの使用 {#use-survey-form-blocks}

共通のスタイリングおよびコンポジションコントロールについては、以下を参照してください。

{% if include.channel == 'in_app_message' %}
- [アプリ内メッセージのドラッグ＆ドロップエディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [ランディングページフォームブロック]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- [アプリ内メッセージのドラッグ＆ドロップエディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [ランディングページフォームブロック]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% endif %}

アンケートには以下のフォームブロックを追加できます。

- 電話番号キャプチャ
- メールキャプチャ
- ラジオボタングループ
- 短文キャプチャ
- 長文キャプチャ
- ドロップダウン
- 単一チェックボックス
- チェックボックスグループ
- 評価スケール
- NPS

### 回答選択肢のランダム化 {#randomize-answer-choices}

ラジオボタングループ、チェックボックスグループ、およびドロップダウンブロックでは、回答選択肢のランダム化がサポートされています。**Randomize choice order** をオンにすると、アンケートが読み込まれるたびに選択肢がシャッフルされます。詳細については、[回答選択肢のランダム順序]({{site.baseurl}}/user_guide/messaging/surveys#randomized-choice-order)を参照してください。

### 長文キャプチャ {#long-text-capture}

長文キャプチャは、最大1,000文字の定性的なフィードバックの収集に適しています。詳細については、[長文テキストキャプチャ]({{site.baseurl}}/user_guide/messaging/surveys#long-form-text-capture)を参照してください。

### 評価スケール {#rating-scale}

評価スケール（数値スケール質問とも呼ばれます）は、感情、満足度、または推薦の可能性を単一の数値としてキャプチャするのに適しています。詳細については、[数値スケール質問]({{site.baseurl}}/user_guide/messaging/surveys#number-scale-questions)を参照してください。

{% if include.channel == 'in_app_message' %}
![店舗体験を1から5で評価する評価スケール。]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![友人に商品を薦める可能性を1から10で評価する評価スケール。]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![友人に商品を薦める可能性を1から10で評価する評価スケール。]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## 必須フィールドと属性の設定 {#configure-required-fields-and-attributes}

各フォームブロックについて、右側の設定パネルで**レポート用識別子**を入力します。この識別子はアンケートのレポートやCSVエクスポートに表示されます。

注意事項:

- ほとんどのアンケート回答は、ユーザープロファイルのカスタム属性に記録できます。
- 長文テキストの回答はカスタム属性として記録できません。
- 回答をユーザー属性として記録しないことを選択した場合、その回答値でユーザーをセグメント化することはできません。

![レポート用識別子と属性記録の設定]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## レポートと分析の確認 {#view-reporting-and-analytics}

配信後、以下で結果を確認できます。

{% if include.channel == 'in_app_message' %}
- アプリ内メッセージアンケートの「**Responses**」タブ
{% elsif include.channel == 'landing_page' %}
- ランディングページアンケートのランディングページ分析ビュー
{% else %}
- アプリ内メッセージアンケートの「**Responses**」タブ
- ランディングページアンケートのランディングページ分析ビュー
{% endif %}

すべてのアンケートで利用可能なトップレベルの分析（全回答、完了、部分的に完了、ユニークインプレッション）の定義については、[分析]({{site.baseurl}}/user_guide/messaging/surveys#analytics)を参照してください。

{% if include.channel == 'landing_page' %}
{% alert note %}
ランディングページアンケートは、アンケートが[マルチステップフォーム]({{site.baseurl}}/user_guide/messaging/surveys#multi-step-landing-page-forms)を使用している場合に、部分的に完了した回答を追跡します。
{% endalert %}
{% endif %}

また、質問ごとの回答の内訳を確認したり、3種類のチャートタイプから選択したり、データをCSVとしてエクスポートしたりすることもできます。詳細については、[チャートタイプ]({{site.baseurl}}/user_guide/messaging/surveys#chart-types)を参照してください。

## リターゲティングとトリガー {#retarget-and-trigger}

次のことができます。

- ユーザー属性として記録されたアンケート回答によってユーザーをセグメント化できます。
- アンケートの完了ステータスによってユーザーをセグメント化できます。

{% if include.channel == 'in_app_message' %}

![アンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- ユーザーがアプリ内メッセージキャンペーンでアンケートを完了したときに、キャンペーンやキャンバスをトリガーできます。

![アプリ内メッセージキャンペーンのアンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![ランディングページのアンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- ユーザーがランディングページでアンケートを完了したときに、キャンペーンやキャンバスをトリガーできます。

{% else %}

![アンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- ユーザーがランディングページまたはアプリ内メッセージキャンペーンでアンケートを完了したときに、キャンペーンやキャンバスをトリガーできます。

![ランディングページのアンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![アプリ内メッセージキャンペーンのアンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### 制限事項 {#limitations}

以下の制限があります。

- 自由記述形式のテキスト回答によるユーザーのセグメント化はできません。
- 記録されたユーザー属性に依存しない質問と回答のトリガーは利用できません。