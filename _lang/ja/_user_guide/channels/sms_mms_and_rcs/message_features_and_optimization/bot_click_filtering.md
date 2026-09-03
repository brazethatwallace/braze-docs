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

Brazeには、ボットクリック（非人間インタラクション（NHI）とも呼ばれます）の疑いを特定するために複数の入力を使用する独自の検出システムがあります。ボットクリックはクリック率を水増しし、エンゲージメント指標を歪める可能性があります。これらをフィルタリングすることで、Brazeは意思決定のための信頼性の高いデータの取得を促進します。

このシステムは、Webクローラー、AndroidおよびiOSのリンクプレビュー、またはCPaaSセキュリティソフトウェアに関連するユーザーエージェントを分析します。フィルタリングされるユーザーエージェントの例には、`GoogleBot`、`GoogleMessages/20`、`python-requests/2.32.3`、`Barracuda Sentinel (EE)` などがあります。

## 影響を受ける指標とワークフロー {#affected-metrics-and-workflows}

以下のBraze指標とワークフローは、ボットクリックの影響を受けます。

- **_合計クリック数_:** キャンペーン分析とキャンバス分析ではボットクリックが除外され、人間のインタラクションのみが反映されます。
- **セグメンテーションフィルター:** SMSリンクインタラクションを参照するセグメントフィルターではボットクリックが除外され、キャンペーンやキャンバスでのより正確なリターゲティングが可能になります。
- **オーケストレーション:** SMSリンクインタラクションを参照するアクションベースのトリガーやキャンバスのアクションパスからボットクリックがフィルタリングされ、トリガーが人間の行動を反映できるようになります。
- **Brazeインテリジェンス:**
    - **BrazeAI<sup>TM</sup>で最適化:** バリアント選択の最適化時にボットクリックを除外します。
    - **インテリジェントチャネル:** SMSまたはRCSが選択された場合、正確なチャネル選択のためにボットクリックを除外します。
    - **実験ステップ:** 信頼性の高い実験結果のためにボットクリックを除外します。
    - **Currentsデータエクスポート:** 人間のクリックとボットのクリックの分析に役立つ`is_suspected_bot_click`フィールドと`suspected_bot_click_reason`フィールドが含まれます。これらのフィールドは[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)、[Snowflakeデータシェアリング]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)、および[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)で利用できます。

ボットクリックが疑われるケースからの購読解除には影響しません。Brazeはすべての購読解除リクエストを通常どおり処理します。{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## SMSクリックイベントのCurrentsフィールド {#currents-fields-in-sms-click-events}

Brazeでは、SMSクリックイベントに対して以下のCurrentsフィールドが含まれています。

| フィールド | データ型 | 説明 |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolean | クリックがボットによるクリックの疑いがあるかどうかを示します。SMSおよびRCSのショートリンククリックの場合、Brazeはクリックごとにボット検出を評価し、このフィールドに`true`または`false`を設定します。 |
| `suspected_bot_click_reason` | String, Array | ボットによるクリックの疑いの理由（`user_agent`など）を示します。SMSおよびRCSのショートリンククリックに対してボット検出が実行された際に設定されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMSクリックイベントのCurrentsフィールド" }

## クエリビルダーテンプレート {#query-builder-template}

データの分析に役立てるために、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)の事前構築済みモバイルテンプレート「**SMS click events by bots**」を使用できます。

## よくある質問 {#frequently-asked-questions}

### ボットクリックフィルタリングはキャンペーンのパフォーマンスにどのような影響を与えますか？ {#how-does-bot-click-filtering-impact-campaign-performance}

ボットクリックフィルタリングは、SMSおよびRCSの短縮リンクのクリックに対して自動的に実行されます。ダッシュボードのクリック率にはボットの疑いがあるクリックが除外されるため、レポートされる数値には、自動リンクプレビューやクローラートラフィックではなく、人間によるインタラクションが反映されます。

### ボットクリックフィルタリングは、ボットによる購読解除リンクのクリックを防止しますか？ {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

いいえ。すべての購読解除リクエストは通常どおり処理されます。

### リンクプレビューはボットクリックフィルタリングに含まれますか？ {#are-link-previews-included-in-bot-click-filtering}

はい。リンクプレビュー（AndroidやiOSのリンクプレビューなど）はボットクリックとしてフラグ付けされ、フィルタリングで除外されます。