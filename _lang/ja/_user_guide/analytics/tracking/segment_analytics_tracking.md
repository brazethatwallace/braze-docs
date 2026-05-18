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

> あるSegmentについて分析の追跡がオンになっている場合、そのSegmentのセッション、カスタムイベント、および収益の推移を表示できます。

Segmentの分析の追跡をオンにしなくても、そのSegmentの[リアルタイム統計情報]({{site.baseurl}}/user_guide/audience/segments/segment_data/#segment-statistics)にアクセスして、ユーザーをCampaignsのターゲットにすることができます。唯一の違いは、このページに記載されている特定の分析ツールにアクセスできるかどうかです。

## Segment分析を有効にする {#turning-on-segment-analytics}

Segmentのページの**Segment Details**セクションで、**Analytics Tracking**を有効にします。

![Segmentの分析の追跡トグル]({% image_buster /assets/img_archive/A_Tracking_2.png %})

アプリでは、最大25個のSegmentについて追跡をオンにすることができます。Brazeでは、Campaignsがセッション、収益、および購入に及ぼす効果を把握するうえで、分析すべき重要なSegmentsを追跡することをお勧めします。

{% alert note %}
分析の追跡を有効にした後、Segmentデータが反映されるまでに時間がかかる場合があります。24時間以内にデータが反映されない場合は、[サポートにお問い合わせください]({{site.baseurl}}/braze_support/)。
{% endalert %}

## 収益と購入の推移の表示 {#viewing-revenue-and-purchases-over-time}

[このSegmentの収益と購入の推移]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/)に関するデータを表示するには、**Analytics** > **Revenue Report**に移動します。

![Segment別の収益データ]({% image_buster /assets/img_archive/Revenue.png %})

任意のカスタム期間のSegmentデータを視覚的に比較するには、Segmentsをグラフに追加するか、グラフから削除します。**Breakdown**ドロップダウンで**By Segment**を選択し、**Breakdown values**でSegmentsを選択します。

グラフの上にある任意のSegment名を選択して、そのSegmentの指標の表示・非表示を切り替えます。

![複数Segmentの収益]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## セッション数の推移 {#sessions-over-time}

同様に、[この特定Segmentのセッション数の推移]({{site.baseurl}}/user_guide/analytics/dashboards/home/#exporting-app-usage-data)に関するデータは、**Home**ページで確認できます。

![Segment別のセッションデータ]({% image_buster /assets/img_archive/events_over_time2.png %})

## カスタムイベントの推移を表示する {#view-custom-events-over-time}

**Analytics** > **Custom events report**に移動して、[Segmentsのカスタムイベント数の推移]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#analytics)に関するデータを表示します。

## クエリビルダーテンプレートの使用 {#using-query-builder-templates}

分析の追跡をオンにすると、クエリビルダーのレポートテンプレートを使用して、Campaigns、Canvas、バリアント、ステップのパフォーマンス指標をSegments別に分類できます。詳細については、[Segmentデータ]({{site.baseurl}}/user_guide/audience/segments/segment_data/#performance-data-by-segment)を参照してください。