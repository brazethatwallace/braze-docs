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

Brazeには、疑わしいボットクリック（非人間インタラクション（NHI）とも呼ばれます）を特定するために複数の入力を使用する検出システムがあります。ボットクリックは、クリック率を人為的に増大させて、メールエンゲージメント指標を歪める可能性があります。このアプローチにより、クリックエンゲージメント指標とインサイトの整合性を維持するために、真の人間によるインタラクションと疑わしいボットアクティビティを区別できます。

## ボットクリックの影響を受ける指標 {#metrics-affected-by-bot-clicks}

{% alert note %}
ボットフィルタリングは、自動クリックの疑いがあるものをアクティブにブロックし、エンゲージメント指標の精度を向上させます。しかし、スキャナやボットは時とともに進化し続けるため、Brazeは人間以外のすべてのインタラクションの除去を保証することはできません。
{% endalert %}

以下のBraze指標は、ボットクリックの影響を受ける可能性があります。

- 総クリック率
- ユニーククリック率
- クリック開封率
- コンバージョンレート（コンバージョンイベントとして「Campaignをクリック」が選択されている場合）
- ヒートマップ
- 一部のセグメンテーションフィルター

[Braze Intelligenceの機能]({{site.baseurl}}/user_guide/brazeai/intelligence_suite)は、検出システムの上にあるクリックデータを活用するため、影響を受ける場合があります。この設定をオンにすると、検出システムが一時的に中断する可能性があり、その結果、疑わしいボットクリックの除外により指標または入力が減少する可能性があります。

- インテリジェントセレクション
- インテリジェントチャネル
- インテリジェントタイミング
- 実験ステップ
    - 勝者パス
    - パーソナライズドパス
- Campaign
    - 勝者バリアント
    - パーソナライズドバリアント
- 推定実質開封率

疑わしいボットクリックからの配信停止は影響を受けません。Brazeは引き続き、すべての配信停止リクエストを通常どおり処理します。Brazeでこれらの配信停止をブロックする場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administer/personal/product_portal)を送信してください。

## ボットフィルタリングの影響を受けるセグメンテーションフィルター {#segmentation-filters-affected-by-bot-filtering}

以下の[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)は、メールメッセージのボットフィルタリングの影響を受ける可能性があります。

- [タグ付きCampaignまたはCanvasをクリック/開封]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [ステップをクリック/開封]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [Campaign内のエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [キャンバスステップ内のエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [任意のCampaignまたはキャンバスステップ内のエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [最後にメッセージにエンゲージ]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [インテリジェントチャネル]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## ボットフィルタリングをオンにする {#turning-on-bot-filtering}

**設定** > **メール設定**に移動します。次に、**ボットクリックを削除**を選択します。この設定はワークスペースレベルで適用されます。

疑わしいボットクリックは、設定がオンになった後にのみ削除され、ワークスペースの指標に遡って適用されることはありません。

![メール設定でボットフィルタリングのメール設定がオンになっている状態。]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
この設定をオンにした後にオフにした場合、Brazeは以前に削除されたボットアクティビティを分析に復元することはできません。
{% endalert %}

## CurrentsおよびSnowflakeのメールクリックイベントのフィールド {#fields-in-email-click-events-for-currents-and-snowflake}

Brazeは、メールクリックイベントに対してCurrentsおよびSnowflakeでフィールド`is_suspected_bot_click`と`suspected_bot_click_reason`を送信します。

| フィールド | データタイプ | 説明 |
| `is_suspected_bot_click` | ブール値 | これが疑わしいボットクリックであることを示します。**ボットクリックを削除**ワークスペース設定をオンにするまで、null値として送信されます。このアプローチにより、ワークスペースで疑わしいボットクリックのフィルタリングがいつ開始されたかをプログラムで把握でき、CurrentsおよびSnowflakeのデータと正確に比較できます。 |
| `suspected_bot_click_reason` | 配列 | これが疑わしいボットクリックである理由を示します。ボットフィルタリングのワークスペース設定が無効になっている場合でも、`user_agent`や`ip_address`などの値が入力されます。このフィールドは、疑わしいボットクリックから発生するクリック数と人間のインタラクションを比較することで、この設定をオンにした場合の潜在的な影響に関するインサイトを提供できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CurrentsおよびSnowflakeのメールクリックイベントのフィールド" }

## よくある質問 {#frequently-asked-questions}

### ボットフィルタリングはCampaignのパフォーマンスにどのような影響を与えますか？ {#how-will-bot-filtering-impact-my-campaigns-performance}

すでに送信済みの以前のCampaignの指標には影響しません。ワークスペースでボットフィルタリングがオンになると、Brazeはすべてのクリックから疑わしいボットクリックのフィルタリングを開始します。クリック率の低下に気づく場合がありますが、そのクリック率はユーザーのメールメッセージへのエンゲージメントをより正確に表しています。

### ボットフィルタリングは、Brazeの配信停止リンクをクリックしたボットによる配信停止を防止しますか？ {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

いいえ。すべての配信停止リクエストは引き続き処理されます。

### マシンオープンはボットクリックフィルタリングで考慮されますか？ {#are-machine-opens-considered-in-the-bot-click-filtering}

いいえ。