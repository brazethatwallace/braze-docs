---
nav_title: セグメント分析の追跡
article_title: セグメント分析の追跡
page_order: 3
page_type: reference
description: "このリファレンス記事では、セグメント分析の追跡と、収益と購入の推移、セッション数の推移、およびカスタムイベント数の推移を確認する方法について説明します。"
tool:
  - Segments
  - Reports
---

# セグメント分析の追跡 {#segment-analytics-tracking}

> あるセグメントについて分析の追跡がオンになっている場合、そのセグメントのセッション、カスタムイベント、および収益の推移を表示できます。

セグメントの分析の追跡をオンにしなくても、そのセグメントの[リアルタイム統計情報]({{site.baseurl}}/user_guide/audience/segments/segment_data#segment-statistics)にアクセスして、ユーザーをキャンペーンのターゲットにすることができます。唯一の違いは、このページに記載されている特定の分析ツールにアクセスできるかどうかです。

## セグメント分析を有効にする {#turning-on-segment-analytics}

セグメントのページの**セグメントの詳細**セクションで、**分析の追跡**を有効にします。

![セグメントの分析の追跡トグル]({% image_buster /assets/img_archive/A_Tracking_2.png %})

アプリでは、最大25個のセグメントについて追跡をオンにすることができます。Brazeでは、キャンペーンがセッション、収益、および購入に及ぼす効果を把握するうえで、分析すべき重要なセグメントを追跡することをお勧めします。

{% alert note %}
分析の追跡を有効にした後、セグメントデータが反映されるまでに時間がかかる場合があります。24時間以内にデータが反映されない場合は、[サポートにお問い合わせください]({{site.baseurl}}/braze_support)。
{% endalert %}

## 収益と購入の推移の表示 {#viewing-revenue-and-purchases-over-time}

[このセグメントの収益と購入の推移]({{site.baseurl}}/user_guide/analytics/reports/revenue_report)に関するデータを表示するには、**Analytics** > **Revenue Report**に移動します。

収益と購入のグラフには、そのセグメントの分析の追跡がオンになった後に記録されたアクティビティが反映されます。追跡をオンにしても、それ以前の購入がレポートに遡って反映されることはありません。セグメントを比較する場合は、選択した各セグメントで追跡が有効になっていた期間のみを使用してください。

![セグメント別の収益データ]({% image_buster /assets/img_archive/Revenue.png %})

任意のカスタム期間のセグメントデータを視覚的に比較するには、セグメントをグラフに追加するか、グラフから削除します。**Breakdown**ドロップダウンで**By セグメント**を選択し、**Breakdown values**でセグメントを選択します。

グラフの凡例にある任意のセグメント名を選択して、そのセグメントの指標の表示・非表示を切り替えます。

![複数セグメントの収益]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## セッション数の推移 {#sessions-over-time}

同様に、[この特定セグメントのセッション数の推移]({{site.baseurl}}/user_guide/analytics/dashboards/home#exporting-app-usage-data)に関するデータは、**Home**ページで確認できます。

![セグメント別のセッションデータ]({% image_buster /assets/img_archive/events_over_time2.png %})

## カスタムイベントの推移を表示する {#view-custom-events-over-time}

**Analytics** > **Custom events report**に移動して、[セグメントのカスタムイベント数の推移]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics)に関するデータを表示します。

## クエリビルダーテンプレートの使用 {#using-query-builder-templates}

分析の追跡をオンにすると、クエリビルダーのレポートテンプレートを使用して、キャンペーン、キャンバス、バリアント、ステップのパフォーマンス指標をセグメント別に分類できます。詳細については、[セグメントデータ]({{site.baseurl}}/user_guide/audience/segments/segment_data#performance-data-by-segment)を参照してください。

## よくある質問 {#frequently-asked-questions}

### 分析の追跡が正しくない、または空に見える場合は何を確認すべきですか？ {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

**セグメントの詳細**で**分析の追跡**がまだ有効になっていることを確認し、アプリごとの上限（追跡対象のセグメントは25個まで）を超えていないことを確認してください。また、追跡を初めて有効にした後、データが反映されるまで最大24時間かかる場合があります。問題が続く場合は、セグメントの定義とレポートの日付範囲を確認してから、[サポートにお問い合わせください]({{site.baseurl}}/braze_support)。