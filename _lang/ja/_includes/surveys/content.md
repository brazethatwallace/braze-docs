{% comment %}
  Braze アンケート共通ドキュメント。
  パラメーター:
  - channel (必須): "in_app_message" または "landing_page"
{% endcomment %}

{% multi_lang_include surveys/beta_alert.md %}

## 前提条件 {#prerequisites}

アンケートを作成する前に、以下の条件を満たす必要があります。

{% if include.channel == 'in_app_message' %}
- Brazeワークスペースでアプリ内メッセージにアクセスできること
- [ドラッグ＆ドロップエディターでのアプリ内メッセージ作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)に精通していること
{% elsif include.channel == 'landing_page' %}
- Brazeワークスペースでランディングページにアクセスできること
- [ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/)に精通していること
{% else %}
- Brazeワークスペースでランディングページ、アプリ内メッセージ、またはその両方にアクセスできること
- [ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/)および[ドラッグ＆ドロップエディターでのアプリ内メッセージ作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)に精通していること
{% endif %}

## アンケートを作成する {#create-a-survey}

ベータ期間中、アンケートは既存のメッセージ作成フロー内で構築します。

{% if include.channel == 'in_app_message' %}
1. CampaignまたはCanvasで[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)を作成します。
2. メッセージタイプとして**Survey**を選択します。
{% elsif include.channel == 'landing_page' %}
1. **メッセージング** > **ランディングページ**に移動します。
2. 新しいランディングページを作成します。
3. メッセージタイプとして**Survey**を選択します。
{% else %}
1. **メッセージング** > **ランディングページ**に移動するか、CampaignまたはCanvasで[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)を作成します。
2. 新しいメッセージを作成します。
3. メッセージタイプとして**Survey**を選択します。
{% endif %}

{% if include.channel == 'in_app_message' %}

## アプリ内メッセージアンケートを作成する {#compose-an-in-app-message-survey}

アプリ内メッセージアンケートには、デフォルトで2つのページが含まれます。

- **ページ1**: ユーザーが質問に回答するページ
- **確認ページ**: アンケートが送信されるページ

デフォルトでは、ボタンは**次のページ**にリンクされています。この動作を変更するには、**アクション**パネルで各ボタンを更新してください。

![アプリ内メッセージアンケートのページフローとアクション設定。]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## アンケートフォームブロックを使用する {#use-survey-form-blocks}

共通のスタイリングと作成コントロールについては、以下を参照してください。

{% if include.channel == 'in_app_message' %}
- [アプリ内メッセージのドラッグ＆ドロップエディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [ランディングページのフォームブロック]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% else %}
- [アプリ内メッセージのドラッグ＆ドロップエディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [ランディングページのフォームブロック]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% endif %}

アンケートには以下のフォームブロックを追加できます。

- 電話番号キャプチャ
- メールキャプチャ
- ラジオボタングループ
- 短文テキストキャプチャ
- 長文テキストキャプチャ
- ドロップダウン
- 単一チェックボックス
- チェックボックスグループ

### 長文テキストキャプチャ {#long-text-capture}

長文テキストキャプチャは、定性的なフィードバックの収集に役立ちます。

以下を設定できます。

- 最小および最大文字数（最大1,000文字）
- 作成中に文字数制限を表示するかどうか
- テキストエリアの高さ（行数）
- プレースホルダーテキスト

ベータ期間中、長文テキストの回答はレポートとエクスポートで利用できますが、ユーザープロファイルのカスタム属性として記録することはできません。

![長文テキストキャプチャブロックの設定。]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## 必須フィールドと属性を設定する {#configure-required-fields-and-attributes}

各フォームブロックについて、右側の設定パネルで**レポート用識別子**を入力します。この識別子はアンケートレポートとCSVエクスポートに表示されます。

ベータ期間中:

- ほとんどのアンケート回答をユーザープロファイルのカスタム属性に記録できます。
- 長文テキストの回答はカスタム属性として記録できません。
- 回答をユーザー属性として記録しない場合、その回答値でユーザーをセグメント化することはできません。

![レポート用識別子と属性記録の設定。]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## レポートと分析を確認する {#view-reporting-and-analytics}

起動後、以下で結果を確認できます。

{% if include.channel == 'in_app_message' %}
- アプリ内メッセージアンケートの**回答**タブ
{% elsif include.channel == 'landing_page' %}
- ランディングページアンケートのランディングページ分析ビュー
{% else %}
- アプリ内メッセージアンケートの**回答**タブ
- ランディングページアンケートのランディングページ分析ビュー
{% endif %}

![ランディングページの分析タブ。]({% image_buster /assets/img/surveys/survey-analytics-1.png %})

トップレベルの分析には以下が含まれます。

- **全回答:** 完了および未完了の回答の合計
- **完了:** すべての必須質問に回答したユーザー
- **部分的に完了:** 一部のデータを送信したが、すべての必須質問に回答しなかったユーザー
- **ユニークインプレッション:** 合計ページビュー数

{% if include.channel == 'landing_page' %}
{% alert note %}
ベータ期間中、ランディングページアンケートでは部分的に完了した回答は追跡されません。
{% endalert %}
{% endif %}

質問ごとの回答内訳を確認したり、データをCSVとしてエクスポートしたりすることもできます。

### チャートタイプを選択する {#choose-a-chart-type}

ラジオボタン、ドロップダウン、チェックボックスのフォームブロックでは、アンケート分析ビューで3種類のチャートタイプから選択できます。これにより、サードパーティツールにエクスポートすることなく、インサイトをより柔軟に解釈・共有できます。

| チャートタイプ | 最適な用途 |
| --- | --- |
| 棒グラフ | 回答数とパーセンテージのデフォルトの横向き表示です。 |
| 縦棒グラフ | 回答数とパーセンテージの縦向き表示です。複数選択の質問や回答オプションが多い質問で、回答を並べて比較する場合に使用します。 |
| 円グラフ | 回答の比率内訳です。単一選択の質問で、回答がオプション間でどのように分布しているかを確認する場合に使用します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アンケートのチャートタイプ" }

各チャートは回答が届くとリアルタイムで更新されます。基礎データに影響を与えることなく、いつでもチャートタイプを切り替えることができます。

![棒グラフを使用したアンケートの質問レベルの内訳。]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## リターゲティングとトリガー {#retarget-and-trigger}

ベータ期間中、以下のことが可能です。

- ユーザー属性として記録されたアンケート回答でユーザーをセグメント化できます。
- アンケート完了ステータスでユーザーをセグメント化できます。

{% if include.channel == 'in_app_message' %}

![アンケートフォローアップのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- ユーザーがアプリ内メッセージCampaignでアンケートを完了した際に、CampaignやCanvasをトリガーできます。

![アプリ内メッセージCampaignアンケートフォローアップのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![ランディングページアンケートフォローアップのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- ユーザーがランディングページでアンケートを完了した際に、CampaignやCanvasをトリガーできます。

{% else %}

![アンケートフォローアップのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- ユーザーがランディングページまたはアプリ内メッセージCampaignでアンケートを完了した際に、CampaignやCanvasをトリガーできます。

![ランディングページアンケートフォローアップのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![アプリ内メッセージCampaignアンケートフォローアップのトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### 制限事項 {#limitations}

ベータ期間中は、以下の制限があります。

- 長文テキストの回答でユーザーをセグメント化することはできません。
- 記録されたユーザー属性に依存しない質問と回答のトリガーは利用できません。