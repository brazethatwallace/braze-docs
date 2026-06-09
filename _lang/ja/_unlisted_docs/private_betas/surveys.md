---
nav_title: アンケート
article_title: Brazeアンケート
description: "アプリ内メッセージやランディングページでアンケートを作成し、回答を確認し、クローズドベータ期間中にユーザーをリターゲティングする方法を説明します。"
permalink: /braze_surveys/
hidden: true
---

# Brazeアンケート {#braze-surveys}

> Brazeアンケートは、アプリ内メッセージやランディングページでフィードバックを収集し、分析やフォローアップメッセージングに活用できます。

{% alert important %}
Brazeアンケートはクローズドベータ版です。ベータに関するフィードバックは [surveys-feedback@braze.com](mailto:surveys-feedback@braze.com) までお送りください。
{% endalert %}

## 前提条件 {#prerequisites}

アンケートを作成する前に、以下の条件を満たす必要があります。

- Brazeワークスペースでランディングページ、アプリ内メッセージ、またはその両方へのアクセス権を取得していること
- [ランディングページの作成](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/)に精通していること
- [ドラッグ＆ドロップによるアプリ内メッセージの作成](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)に精通していること

## アンケートを作成する {#create-a-survey}

ベータ期間中、アンケートは既存のメッセージ作成フロー内で構築します。

1. **Messaging** > **Landing Pages** に移動するか、CampaignまたはCanvas内で[アプリ内メッセージ](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/)を作成します。
2. 新しいメッセージを作成します。
3. メッセージタイプとして**Survey**を選択します。

## アプリ内メッセージアンケートを作成する {#compose-an-in-app-message-survey}

アプリ内メッセージアンケートには、デフォルトで2つのページが含まれます。

- **ページ1**：ユーザーが質問に回答するページ
- **確認ページ**：アンケートが送信されるページ

デフォルトでは、ボタンは**Next page**にリンクされています。この動作を変更するには、**アクション**パネルで各ボタンを更新します。

![アプリ内メッセージアンケートのページフローとアクション設定。]({% image_buster /assets/unlisted_docs/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

## アンケートフォームブロックを使用する {#use-survey-form-blocks}

共通のスタイリングと作成コントロールについては、以下を参照してください。

- [アプリ内メッセージのドラッグ＆ドロップエディターブロック](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- [ランディングページのフォームブロック](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)

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
- 作成時に文字数制限を表示するかどうか
- テキストエリアの高さ（行数）
- プレースホルダーテキスト

ベータ期間中、長文テキストの回答はレポートとエクスポートで利用できますが、ユーザープロファイルのカスタム属性として記録することはできません。

![長文テキストキャプチャブロックの設定。]({% image_buster /assets/unlisted_docs/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## 必須フィールドと属性を設定する {#configure-required-fields-and-attributes}

各フォームブロックについて、右側の設定パネルで**レポート用識別子**を入力します。この識別子はアンケートレポートとCSVエクスポートに表示されます。

ベータ期間中：

- ほとんどのアンケート回答をユーザープロファイルのカスタム属性として記録できます。
- 長文テキストの回答はカスタム属性として記録できません。
- 回答をユーザー属性として記録しない場合、その回答値でユーザーをセグメンテーションすることはできません。

![レポート用識別子と属性記録の設定。]({% image_buster /assets/unlisted_docs/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## レポートと分析を確認する {#view-reporting-and-analytics}

配信後、以下で結果を確認できます。

- アプリ内メッセージアンケートの**回答**タブ
- ランディングページアンケートのランディングページ分析ビュー

![ランディングページの分析タブ。]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-1.png %})

トップレベルの分析には以下が含まれます。

- **全回答：**完了および未完了の回答の合計
- **完了：**すべての必須質問に回答したユーザー
- **部分的に完了：**一部のデータを送信したが、すべての必須質問に回答しなかったユーザー
- **ユニークインプレッション：**合計ページビュー数

{% alert note %}
ベータ期間中、ランディングページアンケートでは部分的に完了した回答は追跡されません。
{% endalert %}

質問ごとの回答内訳を確認したり、データをCSVとしてエクスポートしたりすることもできます。

![アンケート分析の概要と質問レベルの内訳。]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-text.png %})

![アンケートの質問レベルの内訳を示す棒グラフ。]({% image_buster /assets/unlisted_docs/img/surveys/bar-charts-1.png %})

## リターゲティングとトリガー {#retarget-and-trigger}

ベータ期間中、以下のことが可能です。

- ユーザー属性として記録されたアンケート回答でユーザーをセグメンテーションできます。
- アンケートの完了ステータスでユーザーをセグメンテーションできます。<br><br>![アンケートフォローアップ用のトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/unlisted_docs/img/surveys/submit-survey-segment.png %})<br><br>
- ユーザーがランディングページまたはアプリ内メッセージCampaignでアンケートを完了した際に、CampaignやCanvasをトリガーできます。<br><br>![ランディングページアンケートフォローアップ用のトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/unlisted_docs/img/surveys/trigger_landing_page_survey.png %}) <br><br>![アプリ内メッセージCampaignアンケートフォローアップ用のトリガー設定とセグメンテーションフィルター。]({% image_buster /assets/unlisted_docs/img/surveys/interact-campaign-step.png %})

### 制限事項 {#limitations}

ベータ期間中、以下の制限があります。

- 長文テキストの回答でユーザーをセグメンテーションすることはできません。
- 記録されたユーザー属性に依存しない質問と回答のトリガーは利用できません。