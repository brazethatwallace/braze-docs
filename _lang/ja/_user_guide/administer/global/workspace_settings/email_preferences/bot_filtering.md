---
nav_title: メールのボットフィルタリング
article_title: メールのボットフィルタリング
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "この記事では、メールのボットフィルタリングの概要について説明します。"
---

# メールのボットフィルタリング {#bot-filtering-for-emails}

> [メール設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)でボットフィルタリングを設定して、すべての疑わしいマシンまたはボットクリックを除外します。メールの「ボットクリック」とは、自動プログラムにより生成されたメール内のハイパーリンクのクリックを指します。これらのボットクリックをフィルタリングすることで、メッセージを意図的にトリガーし、エンゲージメントのある受信者に配信できます。

{% alert important %}
2025年7月9日以降、作成されたすべての新しいワークスペースでボットフィルタリング設定がオンになり、Brazeでのクリックレポートがより正確になります。
{% endalert %}

## ボットクリックについて {#about-bot-clicks}

Brazeには、ボットクリック（非人間インタラクション（NHI）とも呼ばれます）の疑いを特定するために、複数の入力を活用する検出システムがあります。ボットクリックは、クリック率を人為的に膨張させることでメールのエンゲージメント指標を歪める可能性があります。このアプローチにより、真の人間によるインタラクションとボットアクティビティの疑いを区別し、クリックエンゲージメント指標とインサイトの整合性を維持できます。

## ボットクリックの影響を受ける指標 {#metrics-affected-by-bot-clicks}

{% alert note %}
ボットフィルタリングは、エンゲージメント指標の精度を向上させるために、自動化されたクリックと疑われるものを積極的にブロックします。ただし、スキャナーやボットは時間の経過とともに進化し続けるため、Brazeは人間以外のインタラクションをすべて除去することを保証できません。
{% endalert %}

以下のBraze指標はボットクリックの影響を受ける可能性があります。

- 合計クリック率
- ユニーククリック率
- クリック対開封率
- コンバージョン率（コンバージョンイベントとして「キャンペーンをクリック」が選択されている場合）
- ヒートマップ
- 特定のセグメントフィルター

ボットフィルタリングが有効になっている場合、ボットと疑われるクリックはクリックデータから除外されます。その結果、以下の[BrazeAIインテリジェンス機能]({{site.baseurl}}/user_guide/brazeai/intelligence_suite)では、クリック関連のボリュームが低く表示される場合があります。

- インテリジェントチャネル
- インテリジェントタイミング
- 実験ステップ
    - 勝者パス
- 推定実質開封率

[BrazeAI<sup>TM</sup>で最適化]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)を使用してクリックベースの目標に対して最適化する場合も、クリック関連のボリュームが低く表示されることがあります。

ボットと疑われるクリックからの購読解除は影響を受けません。Brazeは引き続きすべての購読解除リクエストを通常どおり処理します。{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## ボットフィルタリングの影響を受けるセグメンテーションフィルター {#segmentation-filters-affected-by-bot-filtering}

以下の[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)は、メールメッセージのボットフィルタリングの影響を受ける可能性があります。

- [タグ付きキャンペーンまたはキャンバスをクリック/開封]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [ステップをクリック/開封]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [キャンペーンでエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [キャンバスステップでエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [任意のキャンペーンまたはキャンバスステップでエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [最後にメッセージに関与した日時]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [インテリジェントチャネル]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## ボットフィルタリングの有効化 {#turning-on-bot-filtering}

**設定** > **メール設定**に移動します。次に、**ボットクリックを除去**を選択します。この設定はワークスペースレベルで適用されます。

疑わしいボットクリックは、設定が有効になった後にのみ除去され、ワークスペースの既存の指標には遡って適用されません。

![メール設定でボットフィルタリングのメール設定が有効になっている状態。]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
この設定を有効にした後に無効にすると、Brazeは以前に除去されたボットアクティビティを分析に復元することはできません。
{% endalert %}

## CurrentsおよびSnowflakeのメールクリックイベントのフィールド {#fields-in-email-click-events-for-currents-and-snowflake}

Brazeは、メールクリックイベントに対して、CurrentsおよびSnowflakeで`is_suspected_bot_click`と`suspected_bot_click_reason`のフィールドを送信します。

| フィールド | データ型 | 説明 |
| `is_suspected_bot_click` | Boolean | ボットによるクリックの疑いがあることを示します。**Remove bots clicks**ワークスペース設定をオンにするまで、null値として送信されます。このアプローチにより、ワークスペースでボットクリックの疑いがあるクリックのフィルタリングがいつ開始されたかをプログラム的に把握でき、CurrentsおよびSnowflakeのデータと正確に比較できます。 |
| `suspected_bot_click_reason` | Array | ボットによるクリックの疑いがある理由を示します。ボットフィルタリングのワークスペース設定が無効になっている場合でも、`user_agent`や`ip_address`などの値が入力されます。このフィールドは、ボットクリックの疑いがあるクリック数と人間によるインタラクション数を比較することで、この設定をオンにした場合の潜在的な影響についてのインサイトを提供します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CurrentsおよびSnowflakeのメールクリックイベントのフィールド" }

## よくある質問 {#frequently-asked-questions}

### ボットフィルタリングはキャンペーンのパフォーマンスにどのような影響を与えますか？ {#how-will-bot-filtering-impact-my-campaigns-performance}

すでに送信済みのキャンペーンの指標には影響しません。ワークスペースでボットフィルタリングをオンにすると、Brazeはすべてのクリックからボットと疑われるクリックを除外し始めます。クリック率の低下に気づく場合がありますが、このクリック率はユーザーのメールメッセージに対するエンゲージメントをより正確に表しています。

### ボットフィルタリングにより、Brazeの購読解除リンクをクリックしたボットの購読解除が阻止されますか？ {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

いいえ。すべての購読解除リクエストは引き続き処理されます。

### マシンオープンはボットクリックフィルタリングの対象に含まれますか？ {#are-machine-opens-considered-in-the-bot-click-filtering}

いいえ。