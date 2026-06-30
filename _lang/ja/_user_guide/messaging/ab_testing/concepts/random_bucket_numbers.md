---
nav_title: ランダムバケット番号
article_title: ランダムバケット番号
page_order: 2
page_type: reference
description: "この記事では、ランダムバケット番号の概念と、それを使用してバリアントやコントロールグループを作成する方法について説明します。"
page_type: reference
tool:
  - Campaign
  - Canvas

---

# ランダムバケット番号 {#random-bucket-numbers}

> ランダムバケット番号は、ランダムなユーザーの均一に分散したSegmentを作成するために使用できるユーザー属性です。

## 概要 {#overview}

Brazeでユーザープロファイルが作成されると、そのユーザーには0から9999（両端を含む）の間のランダムバケット番号が自動的に割り当てられます。これらのSegmentを使用して、時間の経過とともにユーザーグループに対する複数のCampaignsやCanvasesの効果をテストできます。

### グローバルコントロールグループでの使用 {#global-control-group-usage}

ランダムバケット番号は、グローバルコントロールグループ&#8212;CampaignsやCanvasesを一切受信しないユーザーのグループで使用されます。Brazeはランダムバケット番号の複数の範囲をランダムに選択し、選択されたバケットのユーザーを含めます。ランダムバケット番号は、重み付けや最近割り当てられた番号を考慮せずに割り当てられます。

{% alert note %}
ユーザーが削除されて再作成された場合、そのユーザーは新しいユーザーとみなされるため、異なるランダムバケット番号が割り当てられます。
{% endalert %}

グローバルコントロールグループを設定済みで、他のユースケースにランダムバケット番号を使用したい場合は、[注意すべき点]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for)を確認してください。

### ランダムバケット番号を使用するタイミング {#when-to-use-random-bucket-numbers}

時間の経過とともに複数のCampaignsやCanvasesの効果に対する長期的なテストを行いたい場合は、ランダムバケット番号を使用してユーザーをセグメント化できます。

### 別の方法を使用するタイミング {#when-to-use-something-else}

単一のCampaignまたは単一のCanvas内でテスト用にユーザーをセグメント化したい場合は、Campaignsには[ABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests)を使用してください。Canvasesの場合は、ジャーニーレベルのテストには異なる[バリアント]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-21-add-a-variant)を作成し、ステップレベルのテストには[実験パス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)を使用できます。

## ランダムバケット番号を使用したSegmentの作成 {#create-segments-using-random-bucket-numbers}

[Segmentを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)する際に、「Random Bucket #」フィルターを追加します。次に、Segmentに含める番号または番号の範囲を指定します。

![ランダムバケット番号が「3000」以下のSegmentフィルター。]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

3つの異なるバリアントのテストを実行し、コントロールグループも含めたい場合に、このタイプのSegmentを使用できます。3つのバリアントとコントロールグループに対して均等なサイズのSegmentを作成するためのサンプルプランを以下に示します。

- バケット番号0〜2499はコントロールSegmentに対応
- バケット番号2500〜4999はバリアント1を受け取るSegmentに対応
- バケット番号5000〜7499はバリアント2を受け取るSegmentに対応
- バケット番号7500〜9999はバリアント3を受け取るSegmentに対応

必要なSegment数と各Segment内のユーザー分布に応じて、プランは異なる場合があります。

コントロールグループを含む各ランダムバケット番号Segmentについて、[分析トラッキング]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)を有効にしてください。コントロールグループに対するバリアントの成功を評価する際は、[カスタムイベント]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report)ページにアクセスして、各Segmentが特定のカスタムイベントを完了した頻度を確認できます。

{% alert tip %}
Canvasでランダムバケット番号Segmentを使用する場合（例えば、[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)ステップのフィルターとして）、Canvasの[終了条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)、オーディエンスフィルター、および上流のステップが、バケット範囲の1つと重複するSegmentをターゲットにしていないことを確認してください。重複している場合、その範囲のユーザーが分岐に到達する前に不均衡に除外され、パス間の分布が不均等になる可能性があります。
{% endalert %}

### ランダムバケット番号を使用したランダムオーディエンスの再エントリ {#random-audience-re-entry-using-random-bucket-numbers}

ランダムオーディエンスの再エントリは、[ABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing#what-are-multivariate-and-ab-testing)やCampaignsで特定のユーザーグループをターゲットにする場合に役立ちます。ランダムバケット番号を使用してランダムオーディエンスの再エントリを行うには、以下の手順に従ってください。

1. [Segmentを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)します。
2. ランダムバケットを定義します。CampaignまたはCanvasで、ランダムバケットフィルターを使用してオーディエンスを異なるグループに分割します。例えば、オーディエンスを2つのランダムバケットに分割するよう正確に指定できます（バケットあたりユーザーの50%）。
3. CampaignまたはCanvasの**Target Audiences**セクションで、ランダムバケットの設定を指定します。これにより、Brazeは定義されたパーセンテージに基づいてユーザーを適切なバケットに自動的に割り当てます。
4. ユーザーがSegmentに再エントリできるロジックを設定します。例えば、15日間アプリを利用していないユーザーがSegmentに再エントリできるように設定できます。
5. Campaignを起動し、各バケットのパフォーマンスを監視します。エンゲージメント率やコンバージョン率などの指標を分析して、ランダムオーディエンスの再エントリがユースケースにどの程度効果的かを判断できます。