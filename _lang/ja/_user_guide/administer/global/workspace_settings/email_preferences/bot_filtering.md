---
nav_title: メールのボットフィルタリング
article_title: メールのボットフィルタリング
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "この記事では、メールのボットフィルタリングの概要について説明します。"
---

# メールのボットフィルタリング

> [メール設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/)でボットフィルタリングを設定して、すべての疑わしいマシンまたはボットクリックを除外します。メールの「ボットクリック」とは、自動プログラムにより生成されたメール内のハイパーリンクのクリックを指します。これらのボットクリックをフィルタリングすることで、メッセージを意図的にトリガーし、エンゲージメントのある受信者に配信できます。

{% alert important %}
2025年7月9日以降、作成されたすべての新しいワークスペースでボットフィルタリング設定がオンになり、Braze でのクリックレポートがより正確になります。
{% endalert %}

## ボットクリックについて

Braze には、疑わしいボットクリック（人間以外とのインタラクション（NHI）とも呼ばれます）を特定するために複数の入力を使用する検出システムがあります。ボットクリックは、クリック率を人為的に増大させて、メールエンゲージメントの指標を歪める可能性があります。このアプローチでは、クリックエンゲージメント指標とインサイトの完全性を確保するために、真の人間とのインタラクションと疑わしいボットアクティビティを区別できるようになります。

## ボットクリックの影響を受ける指標

{% alert note %}
自動クリックの疑いがある場合は、ボットフィルターがアクティブにブロックし、エンゲージメント指標の精度を向上させます。しかし、スキャナやボットは時とともに進化し続けるため、Braze は人間以外のすべてのインタラクションを除去することを保証することはできません。
{% endalert %}

以下の Braze 指標は、ボットクリックの影響を受ける可能性があります。

- 総クリック率
- ユニーククリック率
- クリック開封率
- コンバージョンレート（コンバージョンイベントとして「クリック Campaign」が選択されている場合）
- ヒートマップ
- 一部のセグメンテーションフィルター

[Braze Intelligence の機能]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/)は、検出システムの上にあるクリックデータを活用するため、影響を受ける場合があります。この設定をオンにすると、検出システムが一時的に中断する可能性があります。その結果、疑わしいボットクリックが除外されることから、指標または入力が減少する可能性があります。

- インテリジェントセレクション
- インテリジェントチャネル
- インテリジェントタイミング
- 実験ステップ
    - 勝者パス
    - パーソナライズされたパス
- Campaign
    - 勝者バリアント
    - パーソナライズされたバリアント
- 推定実質開封率

疑わしいボットクリックからの配信停止は、影響を受けません。Braze は引き続き、すべての配信停止リクエストを通常どおり処理します。Braze でこれらの配信停止をブロックする場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administer/personal/product_portal/)を送信してください。

## ボットフィルタリングの影響を受けるセグメンテーションフィルター

以下の[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)は、メールメッセージのボットフィルタリングの影響を受ける可能性があります。

- [タグ付き Campaign または Canvas をクリック/開封]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-opened-campaign-or-canvas-with-tag)
- [ステップをクリック/開封]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-opened-step)
- [Campaign 内のエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-alias-in-campaign)
- [キャンバスステップ内のエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-alias-in-canvas-step)
- [任意の Campaign またはキャンバスステップ内のエイリアスをクリック]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-alias-in-any-campaign-or-canvas-step)
- [最後にメッセージにエンゲージ]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#last-engaged-with-message)
- [インテリジェントチャネル]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#intelligent-channel)

## ボットフィルタリングをオンにする

**設定** > **メール設定**に移動します。次に、**ボットクリックを削除**を選択します。この設定はワークスペースレベルで適用されます。

疑わしいボットクリックは、設定がオンになった後にのみ削除され、ワークスペースの指標に遡って適用されることはありません。

![メール設定でボットフィルタリングのメール設定がオンになっている状態。]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
この設定をオンにした後にオフにした場合、Braze は以前に削除されたボットアクティビティを分析に復元することはできません。
{% endalert %}

## Currents および Snowflake のメールクリックイベントのフィールド

Braze は、メールクリックイベントに対して Currents および Snowflake でフィールド `is_suspected_bot_click` と `suspected_bot_click_reason` を送信します。

| フィールド | データタイプ | 説明 |
| `is_suspected_bot_click` | ブール値 | これが疑わしいボットクリックであることを示します。**ボットクリックを削除**ワークスペース設定をオンにするまで、null 値として送信されます。このアプローチにより、ワークスペースで疑わしいボットクリックのフィルタリングがいつ開始されたかをプログラムで把握でき、Currents および Snowflake のデータと正確に比較できます。 |
| `suspected_bot_click_reason` | 配列 | これが疑わしいボットクリックである理由を示します。ボットフィルタリングのワークスペース設定が無効になっている場合でも、`user_agent` や `ip_address` などの値が入力されます。このフィールドは、疑わしいボットクリックから発生するクリック数と人間のインタラクションを比較することで、この設定をオンにした場合の潜在的な影響に関するインサイトを提供できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## よくある質問

### ボットフィルタリングは Campaign のパフォーマンスにどのような影響を与えますか？

すでに送信済みの以前の Campaign の指標には影響しません。ワークスペースでボットフィルタリングがオンになると、Braze はすべてのクリックから疑わしいボットクリックのフィルタリングを開始します。クリック率の低下に気づく場合がありますが、そのクリック率はユーザーのメールメッセージへのエンゲージメントをより正確に表しています。

### ボットフィルタリングは、Braze の配信停止リンクをクリックしたボットによる配信停止を防止しますか？

いいえ。すべての配信停止リクエストは引き続き処理されます。

### マシンオープンはボットクリックフィルタリングで考慮されますか？

いいえ。