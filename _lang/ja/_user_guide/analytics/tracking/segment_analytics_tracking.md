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

## セグメント分析の有効化 {#turning-on-segment-analytics}

セグメントのページの**セグメントの詳細**セクションで、**分析トラッキング**を有効にします。

![セグメントの分析トラッキングトグル]({% image_buster /assets/img_archive/A_Tracking_2.png %})

ワークスペースでは、最大25個のセグメントに対してトラッキングを有効にできます。Brazeでは、キャンペーンがセッション、収益、購入に与える影響を分析する際に重要なセグメントをトラッキングすることを推奨しています。

{% alert note %}
分析トラッキングを有効にした後、セグメントデータがレポートに反映されるまでに時間がかかる場合があります。24時間以内にデータが反映されない場合は、[サポートにお問い合わせください]({{site.baseurl}}/braze_support)。
{% endalert %}

## 収益と購入の時系列表示 {#viewing-revenue-and-purchases-over-time}

**分析** > **収益レポート**に移動して、[このセグメントの収益と購入の時系列データ]({{site.baseurl}}/user_guide/analytics/reports/revenue_report)を確認します。

収益と購入のグラフには、そのセグメントの分析トラッキングが有効になった後に記録されたアクティビティが反映されます。トラッキングを有効にしても、それ以前の購入データがレポートにさかのぼって反映されることはありません。セグメントを比較する際は、選択した各セグメントでトラッキングが有効になっていた期間のみを使用してください。

![セグメント別の収益データ]({% image_buster /assets/img_archive/Revenue.png %})

任意のカスタム期間でセグメントデータを視覚的に比較するには、グラフにセグメントを追加または削除します。**内訳**ドロップダウンで**セグメント別**を選択し、**内訳の値**でセグメントを選択します。

グラフの凡例でセグメント名を選択すると、そのセグメントの指標の表示・非表示を切り替えることができます。

![複数セグメントの収益]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## 経時的なセッション {#sessions-over-time}

同様に、**ホーム**ページでは、[この特定のセグメントの経時的なセッション]({{site.baseurl}}/user_guide/analytics/dashboards/home)に関するデータを確認できます。

![セグメント別のセッションデータ]({% image_buster /assets/img_archive/events_over_time2.png %})

## カスタムイベントの推移を表示する {#view-custom-events-over-time}

セグメント別の[カスタムイベントの推移]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics)に関するデータを表示するには、**分析** > **カスタムイベントレポート**に移動します。

## Query Builderテンプレートの使用 {#using-query-builder-templates}

分析トラッキングがオンになっている場合、Query Builderのレポートテンプレートを使用して、キャンペーン、キャンバス、バリアント、およびステップのパフォーマンス指標をセグメント別に分析できます。詳細については、[セグメントデータ]({{site.baseurl}}/user_guide/audience/segments/segment_data#viewing-performance-data-by-segment)を参照してください。

## よくある質問 {#frequently-asked-questions}

### 分析トラッキングが正しく表示されない、または空の場合、何を確認すべきですか？ {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

**セグメントの詳細**で**分析トラッキング**がまだ有効になっていることを確認し、ワークスペースごとの上限（トラッキング付きセグメント25件）を超えていないことを確認してください。また、トラッキングを初めて有効にした後、データが反映されるまで最大24時間かかる場合があります。問題が解決しない場合は、セグメントの定義とレポートの日付範囲を確認してから、[サポートに連絡]({{site.baseurl}}/braze_support)してください。