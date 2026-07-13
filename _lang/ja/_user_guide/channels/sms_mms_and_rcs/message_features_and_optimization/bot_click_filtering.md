---
nav_title: "ボットクリックフィルタリング"
article_title: "SMSおよびRCSボットクリックフィルタリング"
description: "このリファレンス記事では、SMSおよびRCSのボットクリックフィルタリングについて説明しています。"
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 5
channel:
  - SMS
  - RCS
---

# SMSおよびRCSボットクリックフィルタリング {#sms-and-rcs-bot-click-filtering}

> SMSおよびRCSボットクリックフィルタリングは、疑わしいボットクリックを除外することで、キャンペーンの分析やワークフローを強化します。「ボットクリック」とは、Webクローラー、AndroidやiOSのリンクプレビュー、CPaaSセキュリティソフトウェアなどによる、SMSおよびRCSメッセージ内の短縮リンクへの自動クリックを指します。この機能により、正確なレポート、セグメンテーション、オーケストレーションが可能になり、実際のユーザーにエンゲージできます。<br><br> メールキャンペーンのボットクリックフィルタリングについては、[メールのボットフィルタリング]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering)を参照してください。

## 仕組み {#how-it-works}

Brazeは、複数の入力を使用して疑わしいボットクリック（非人間インタラクション（NHI）とも呼ばれます）を識別する独自の検出システムを備えています。ボットクリックはクリック率を膨張させ、エンゲージメント指標を歪める可能性があります。これらをフィルタリングすることで、Brazeは意思決定のための信頼性の高いデータの取得を促進します。

このシステムは、Webクローラー、AndroidやiOSのリンクプレビュー、またはCPaaSセキュリティソフトウェアに関連するユーザーエージェントを分析します。フィルタリングされるユーザーエージェントの例としては、`GoogleBot`、`GoogleMessages/20`、`python-requests/2.32.3`、`Barracuda Sentinel (EE)` などがあります。

## 影響を受ける指標とワークフロー {#affected-metrics-and-workflows}

以下のBrazeの指標とワークフローがボットクリックの影響を受けます。

- **_合計クリック数_：** キャンペーン分析およびキャンバス分析はボットクリックを除外し、人間のインタラクションのみを反映します。
- **セグメンテーションフィルター：** SMSリンクインタラクションを参照するセグメントフィルターは、キャンペーンおよびキャンバスでのより正確なリターゲティングのためにボットクリックを除外します。
- **オーケストレーション：** ボットクリックは、SMSリンクインタラクションを参照するアクションベースのトリガーおよびキャンバスのアクションパスからフィルタリングされ、トリガーが人間の行動を反映できるようになります。
- **Brazeインテリジェンス：**
    - **インテリジェントセレクション：** バリアント選択の最適化時にボットクリックを除外します。
    - **インテリジェントチャネル：** SMSまたはRCSが選択された場合、正確なチャネル選択のためにボットクリックを除外します。
    - **実験ステップ：** 信頼性の高い実験結果のためにボットクリックを除外します。
    - **Currentsデータエクスポート：** 人間のクリックとボットクリックの分析に役立つ`is_suspected_bot_click`および`suspected_bot_click_reason`フィールドが含まれます。これらのフィールドは、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)、[Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)、および[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)で利用できます。

疑わしいボットクリックによる購読解除は影響を受けません。Brazeはすべての購読解除リクエストを通常どおり処理します。{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## SMSクリックイベントのCurrentsフィールド {#currents-fields-in-sms-click-events}

Brazeは、SMSクリックイベントに対して以下のCurrentsフィールドを提供しています。

| フィールド | データタイプ | 説明 |
| --- | --- | --- |
| `is_suspected_bot_click` | ブール値 | クリックが疑わしいボットクリックかどうかを示します。ボットクリックフィルタリングが会社で有効になるまで、すべてのユーザーに対して`null`を返します。有効にすると、以降のすべての新しいクリックに対して`true`または`false`が設定されます。 |
| `suspected_bot_click_reason` | 文字列、配列 | 疑わしいボットクリックの理由（`user_agent`など）を示します。フィルタリングが無効の場合でも設定され、潜在的なボットアクティビティに関するインサイトを提供します。このフィールドはグローバルに利用可能で、ボットクリックフィルタリングがまだ有効になっていない場合でも、すべてのユーザーに対して理由が設定されます。これにより、ボットクリックフィルタリングを有効にする前に、潜在的なボットアクティビティに関するインサイトを得ることができます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMSクリックイベントのCurrentsフィールド" }

## クエリビルダーテンプレート {#query-builder-template}

データの分析に役立てるために、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)の事前構築済みモバイルテンプレート**SMS click events by bots**を使用できます。

## よくある質問 {#frequently-asked-questions}

### ボットクリックフィルタリングはキャンペーンのパフォーマンスにどのような影響を与えますか？ {#how-does-bot-click-filtering-impact-campaign-performance}

フィルタリングは、以前に送信されたキャンペーンには影響しません。有効にすると、ボットクリックを除外することで、その時点以降のクリック率が低下します。

### ボットクリックフィルタリングは、ボットが購読解除リンクをクリックするのを防ぎますか？ {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

いいえ。すべての購読解除リクエストは通常どおり処理されます。

### リンクプレビューはボットクリックフィルタリングに含まれますか？ {#are-link-previews-included-in-bot-click-filtering}

はい。リンクプレビュー（AndroidやiOSのリンクプレビューなど）はボットクリックとしてフラグが付けられ、フィルタリングされます。

### ボットクリックフィルタリングを有効にするにはどうすればよいですか？ {#how-do-i-enable-bot-click-filtering}

早期アクセス期間中にボットクリックフィルタリングを有効にするには、Brazeアカウントチームに連絡する必要があります。ボットクリックフィルタリングが一般提供されると、この機能はすべてのSMSおよびRCSユーザーに対してデフォルトで有効になります。

また、[リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)の高度なクリックトラッキングが有効になっていることを確認してください。これにより、個々のユーザーレベルでこのデータをトラッキングするため、ボットクリックの分析データを受け取ることができます。

{% alert note %}
さらにサポートが必要な場合は、[サポートに連絡]({{site.baseurl}}/braze_support)してください。
{% endalert %}