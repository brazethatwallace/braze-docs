---
nav_title: レポートとインサイト
article_title: レポートとインサイト
description: "BrazeでBrazeAI Decisioning Studio™レポートを表示する方法について説明します。これにより、AIを活用した意思決定がキャンペーンにどのような影響を与えるかを理解できます。"
page_order: 6
---

# レポートとインサイト {#reports-and-insights}

> BrazeでBrazeAI Decisioning Studio™レポートを表示する方法について説明します。これにより、AIを活用した意思決定がキャンペーンにどのような影響を与えるかを理解できます。パフォーマンス指標からデータの健全性やシステムの変更まで、これらのレポートは結果の理解、問題のトラブルシューティング、そして確信を持った意思決定に役立ちます。

## 前提条件 {#prerequisites}

BrazeでDecisioning Studioのレポートを確認するには、以下の条件を満たしている必要があります。

- BrazeおよびBrazeAI Decisioning Studio™の有効な契約があること。
- カスタマーサクセスマネージャーに連絡して、BrazeAI Decisioning Studio™の有効化を依頼すること。
- 有効なBrazeAI Decisioning Studio™エージェントがあること。

## レポートの表示 {#view}

BrazeでDecisioning Studioエージェントの指標を表示するには、**AI Decisioning** > **BrazeAI Decisioning Studio™**に移動し、エージェントを選択します。

ここでは、パフォーマンス、インサイト、診断、タイムラインなどのレポートを表示できます。詳しくは、[利用可能なレポート](#available-reports)をご覧ください。

## レポートの日付を変更する {#change-report-dates}

[レポートを開いた](#view)後、カレンダーのドロップダウンから新しい開始日と終了日を選択して、日付範囲を変更できます。

![BrazeAI Decisioning Studio™の日付範囲セレクターが開いており、カレンダーのドロップダウンが表示されています。カレンダーには、レポートビューをカスタマイズするための選択可能な開始日と終了日が表示されています。]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

デフォルトの開始日を設定したり、常に除外する日付を選択したりすることもできます。除外された日付は、そのエージェントのすべてのレポートからフィルターで除外されます。

日付を設定または除外するには、<i class="fa-solid fa-gear" aria-label="設定"></i> **Settings**を選択し、必要に応じてデフォルトの日付を変更するか、日付を除外します。

![BrazeAI Decisioning Studio™で設定パネルが開いており、デフォルトの開始日を設定したり、レポートから特定の日付を除外するオプションが表示されています。パネルには「Default start date」と「Exclude dates」の2つのセクションが表示されています。「Exclude dates」の下には、それぞれの横にチェックボックスが付いた複数の日付が一覧表示されています。]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## 利用可能なレポート {#available-reports}

- [パフォーマンス]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance): トリートメントグループとコントロールグループを比較するハイレベルなエージェント指標です。**Trending**と**Driver Tree**のビューがあります。
- [インサイト]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights): アクションバンク内のおすすめオプションがどのように生成されるかを示します。エージェントの設定やSHAPsレポートを含みます。
- [診断]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics): アウトバウンドおよびインバウンドのデータ健全性です。おすすめのボリュームやデータフィードの監視を含みます。
- [タイムライン]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline): 主要なイベント（エージェントの実行、設定変更、ガードレールの更新）をパフォーマンス指標と共に表示する視覚的な記録です。