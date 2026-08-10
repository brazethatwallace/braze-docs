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

Brazeには、ボットクリック（非人間インタラクション（NHI）とも呼ばれます）の疑いを特定するために複数の入力を活用する検出システムがあります。ボットクリックは、クリック率を人為的に膨らませることで、メールのエンゲージメント指標を歪める可能性があります。このアプローチにより、本物の人間のインタラクションとボットアクティビティの疑いを区別し、クリックエンゲージメント指標とインサイトの整合性を維持できます。

## ボットクリックの影響を受ける指標 {#metrics-affected-by-bot-clicks}

{% alert note %}
ボットフィルタリングは、疑わしい自動クリックを積極的にブロックし、エンゲージメント指標の精度を向上させます。ただし、スキャナーやボットは時間の経過とともに進化し続けるため、Brazeはすべての人間以外のインタラクションの除去を保証することはできません。
{% endalert %}

以下のBraze指標はボットクリックの影響を受ける可能性があります。

- 合計クリック率
- ユニーククリック率
- クリック・トゥ・オープン率
- コンバージョン率（コンバージョンイベントとして「キャンペーンをクリック」が選択されている場合）
- ヒートマップ
- 特定のセグメントフィルター

ボットフィルタリングが有効になっている場合、疑わしいボットクリックはクリックデータから除外されます。その結果、以下の[BrazeAIインテリジェンス機能]({{site.baseurl}}/user_guide/brazeai/intelligence_suite)では、クリック関連のボリュームが低く表示される場合があります。

- インテリジェントセレクション
- インテリジェントチャネル
- インテリジェントタイミング
- 実験ステップ
    - 勝者パス
    - パーソナライズされたパス
- キャンペーン
    - 勝者バリアント
    - パーソナライズされたバリアント
- 推定実開封率

疑わしいボットクリックによる購読解除は影響を受けません。Brazeは引き続き、すべての購読解除リクエストを通常どおり処理します。{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## ボットフィルタリングの影響を受けるセグメンテーションフィルター {#segmentation-filters-affected-by-bot-filtering}

以下の[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)は、メールメッセージのボットフィルタリングの影響を受ける可能性があります。

- [タグ付きキャンペーンまたはキャンバスをクリック/開封]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [ステップをクリック/開封]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [キャンペーンでエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [キャンバスステップでエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [任意のキャンペーンまたはキャンバスステップでエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [最後にメッセージにエンゲージした日]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [インテリジェントチャネル]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## ボットフィルタリングの有効化 {#turning-on-bot-filtering}

**設定** > **メール設定**に移動します。次に、**ボットクリックを除去**を選択します。この設定はワークスペースレベルで適用されます。

疑わしいボットクリックは、設定が有効になった後にのみ除去され、ワークスペース内の指標に遡って適用されることはありません。

![メール設定でボットフィルタリングのメール設定が有効になっている状態。]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
この設定を有効にした後に無効にした場合、Brazeは以前に除去されたボットアクティビティを分析に復元することはできません。
{% endalert %}

## CurrentsおよびSnowflakeのメールクリックイベントのフィールド {#fields-in-email-click-events-for-currents-and-snowflake}

Brazeは、メールクリックイベントに対して、CurrentsおよびSnowflakeで`is_suspected_bot_click`と`suspected_bot_click_reason`のフィールドを送信します。

| フィールド | データ型 | 説明 |
| `is_suspected_bot_click` | Boolean | ボットによるクリックの疑いがあることを示します。**ボットクリックの除去**ワークスペース設定をオンにするまで、null値として送信されます。このアプローチにより、ワークスペースでボットクリックの疑いがあるクリックのフィルタリングがいつ開始されたかをプログラムで把握でき、CurrentsおよびSnowflakeのデータと正確に比較できます。 |
| `suspected_bot_click_reason` | Array | ボットによるクリックの疑いがある理由を示します。ボットフィルタリングのワークスペース設定が無効になっている場合でも、`user_agent`や`ip_address`などの値が入力されます。このフィールドは、ボットクリックの疑いがあるクリックから発生したクリック数と人間のインタラクションを比較することで、この設定をオンにした場合の潜在的な影響についてインサイトを提供します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CurrentsおよびSnowflakeのメールクリックイベントのフィールド" }

## よくある質問 {#frequently-asked-questions}

### ボットフィルタリングはキャンペーンのパフォーマンスにどのような影響を与えますか？ {#how-will-bot-filtering-impact-my-campaigns-performance}

すでに送信済みのキャンペーンの指標には影響しません。ワークスペースでボットフィルタリングをオンにすると、Brazeはすべてのクリックからボットと疑われるクリックをフィルタリングし始めます。クリック率が低下する場合がありますが、そのクリック率はユーザーのメールメッセージに対するエンゲージメントをより正確に反映したものです。

### ボットフィルタリングは、Brazeの購読解除リンクをクリックするボットの購読解除を防止しますか？ {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

いいえ。すべての購読解除リクエストは引き続き処理されます。

### マシンオープンはボットクリックフィルタリングで考慮されますか？ {#are-machine-opens-considered-in-the-bot-click-filtering}

いいえ。