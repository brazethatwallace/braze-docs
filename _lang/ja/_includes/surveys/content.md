{% comment %}
  Brazeアンケート共通ドキュメント。
  パラメーター:
  - channel (必須): "in_app_message" または "landing_page"
{% endcomment %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Braze surveys' %}

## 前提条件 {#prerequisites}

アンケートを作成する前に、以下の条件を満たす必要があります。

{% if include.channel == 'in_app_message' %}
- Brazeワークスペースでアプリ内メッセージにアクセスできること
- [ドラッグ＆ドロップエディターでのアプリ内メッセージの作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)に精通していること
{% elsif include.channel == 'landing_page' %}
- Brazeワークスペースでランディングページにアクセスできること
- [ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)に精通していること
{% else %}
- Brazeワークスペースでランディングページ、アプリ内メッセージ、またはその両方にアクセスできること
- [ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)および[ドラッグ＆ドロップエディターでのアプリ内メッセージの作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)に精通していること
{% endif %}

## アンケートを作成する {#create-a-survey}

早期アクセス期間中、アンケートは既存のメッセージ作成フロー内で構築されます。

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

アプリ内メッセージアンケートには、デフォルトで2つのページが含まれています。

- **ページ1**: ユーザーが質問に回答するページ
- **確認ページ**: アンケートが送信されるページ

デフォルトでは、ボタンは**Next page**にリンクされています。この動作を変更するには、**Actions**パネルで各ボタンを更新します。

![アプリ内メッセージアンケートのページフローとアクション設定。]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## アンケートフォームブロックの使用 {#use-survey-form-blocks}

共有のスタイリングおよびコンポジションコントロールについては、以下を参照してください。

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

### 回答選択肢のランダム化 {#randomize-answer-choices}

ラジオボタングループ、チェックボックスグループ、およびドロップダウンブロックでは、回答選択肢のランダム化がサポートされています。**Randomize choice order** をオンにすると、アンケートが読み込まれるたびに選択肢がシャッフルされます。同じ最初の選択肢が回答を偏らせる可能性がある場合に、順序バイアスを軽減するためにこの設定を使用してください。

ランダム化は、各アンケート回答者に対する表示順序のみを変更します。レポートのラベルと値は設定した選択肢にマッピングされたままなので、分析、CSVエクスポート、セグメンテーションでは同じ回答データが使用されます。

### 長文キャプチャ {#long-text-capture}

長文キャプチャは、定性的なフィードバックの収集に役立ちます。

以下を設定できます。

- 最小および最大文字数（最大1,000文字）
- 作成中に文字数制限を表示するかどうか
- テキストエリアの高さ（行数）
- プレースホルダーテキスト

早期アクセス期間中、長文の回答はレポートとエクスポートで利用できますが、ユーザープロファイルのカスタム属性として記録することはできません。

![長文キャプチャブロックの設定。]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

### 評価スケール {#rating-scale}

評価スケールは、感情、満足度、または推奨の可能性を単一の数値として収集するのに役立ちます。

設定パネルで、ドロップダウンからスケールを選択します。

- **1〜10**
- **1〜5**
- **0〜10**（標準的なネットプロモータースコア（NPS）の範囲）

評価はアンケートの回答として収集したり、整数のカスタム属性として記録したり、またはその両方を行うことができます。評価スケールブロックと[長文キャプチャ](#long-text-capture)ブロックを組み合わせることで、同じアンケート内で数値スコアと定性的なフィードバックを一緒に収集できます。

{% if include.channel == 'in_app_message' %}
![ストア体験を1から5で評価する評価スケール。]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![友人に商品を推奨する可能性を1から10で評価する評価スケール。]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![友人に商品を推奨する可能性を1から10で評価する評価スケール。]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## 必須フィールドと属性の設定 {#configure-required-fields-and-attributes}

各フォームブロックについて、右側の設定パネルで**レポート用識別子**を入力します。この識別子はアンケートレポートおよびCSVエクスポートに表示されます。

早期アクセス期間中：

- ほとんどのアンケート回答をユーザープロファイルのカスタム属性に記録できます。
- 長文テキストの回答はカスタム属性として記録できません。
- 回答をユーザー属性として記録しないことを選択した場合、その回答値でユーザーをセグメント化することはできません。

![レポート用識別子と属性ログの設定。]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## レポートと分析の確認 {#view-reporting-and-analytics}

ローンチ後、以下で結果を確認します。

{% if include.channel == 'in_app_message' %}
- アプリ内メッセージアンケートの**レスポンス**タブ
{% elsif include.channel == 'landing_page' %}
- ランディングページアンケートのランディングページ分析ビュー
{% else %}
- アプリ内メッセージアンケートの**レスポンス**タブ
- ランディングページアンケートのランディングページ分析ビュー
{% endif %}

トップレベルの分析には以下が含まれます。

- **全レスポンス:** 完了および未完了のレスポンスの合計
- **完了:** すべての必須質問に回答したユーザー
- **部分的に完了:** 一部のデータを送信したが、すべての必須質問に回答しなかったユーザー
- **ユニークインプレッション:** 合計ページビュー数

{% if include.channel == 'landing_page' %}
{% alert note %}
ランディングページアンケートでは、早期アクセス期間中は部分的に完了したレスポンスを追跡しません。
{% endalert %}
{% endif %}

質問ごとのレスポンスの内訳を確認したり、データをCSVとしてエクスポートしたりすることもできます。

### チャートタイプの選択 {#choose-a-chart-type}

ラジオボタン、ドロップダウン、チェックボックスのフォームブロックでは、アンケート分析ビューで3つのチャートタイプから選択できます。これにより、サードパーティツールにエクスポートすることなく、インサイトをより柔軟に解釈・共有できます。

| チャートタイプ | 最適な用途 |
| --- | --- |
| 棒グラフ | レスポンス数とパーセンテージのデフォルトの横向き表示です。 |
| 縦棒グラフ | レスポンス数とパーセンテージの縦向き表示です。複数選択の質問や回答オプションが多い質問でレスポンスを並べて比較する場合に使用します。 |
| 円グラフ | レスポンスの比率の内訳です。単一選択の質問で、オプション全体にレスポンスがどのように分布しているかを確認したい場合に使用します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アンケートのチャートタイプ" }

各チャートはレスポンスが届くとリアルタイムで更新されます。基になるデータに影響を与えることなく、いつでもチャートタイプを切り替えることができます。

![棒グラフを使用したアンケートの質問レベルの内訳。]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## リターゲティングとトリガー {#retarget-and-trigger}

早期アクセス期間中は、以下のことが可能です。

- ユーザー属性として記録されたアンケート回答に基づいてユーザーをセグメント化できます。
- アンケートの完了ステータスに基づいてユーザーをセグメント化できます。

{% if include.channel == 'in_app_message' %}

![アンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- アプリ内メッセージキャンペーンでユーザーがアンケートを完了したときに、キャンペーンやキャンバスをトリガーできます。

![アプリ内メッセージキャンペーンのアンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![ランディングページのアンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- ランディングページでユーザーがアンケートを完了したときに、キャンペーンやキャンバスをトリガーできます。

{% else %}

![アンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- ランディングページまたはアプリ内メッセージキャンペーンでユーザーがアンケートを完了したときに、キャンペーンやキャンバスをトリガーできます。

![ランディングページのアンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![アプリ内メッセージキャンペーンのアンケートフォローアップのためのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### 制限事項 {#limitations}

早期アクセス期間中は、以下の制限があります。

- 自由記述形式のテキスト回答に基づいてユーザーをセグメント化することはできません。
- 記録されたユーザー属性に依存しない質問と回答のトリガーは利用できません。