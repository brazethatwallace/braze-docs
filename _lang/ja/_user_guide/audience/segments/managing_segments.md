---
nav_title: Segmentの管理
article_title: Segmentの管理
page_order: 2
page_type: tutorial
tool: Segments
description: "この記事では、Segmentのリストのフィルタリング、Segmentの作成、Segmentの編集など、Segmentを管理するために実行できるアクションについて説明します。"

---

# Segmentの管理 {#manage-segments}

> Segmentsセクションでは、既存のSegmentの包括的なリストを表示したり、新しいSegmentを作成したり、既存のSegmentを編集したりできます。さまざまなフィルターや列を選択してSegmentのリストを絞り込み、最も関連性の高い情報のみを表示できます。

![アクティブなSegmentのリストを表示するSegmentsセクション。]({% image_buster /assets/img/segment/segments_page.png %})

## ビューのカスタマイズ {#customizing-your-view}

フィルターを使用し、表示する列を変更して、Segmentリストのビューをカスタマイズできます。**Segments**セクションを離れて戻ると、リストはデフォルトのビューに戻り、以前に選択したフィルターはすべてクリアされます。

### ステータスフィルター {#status-filter}

リストを絞り込んで、アクティブなSegmentまたはアーカイブされたSegmentのみを表示できます。アーカイブされていないSegmentはすべてアクティブとみなされます。

### フィルター {#filters}

以下のフィルターを調整して、リスト内のSegmentを並べ替えます。
- **Last Edited By:** Segmentを最後に編集したユーザー
- **Last Edited:** Segmentが最後に編集された時間範囲
- **Estimated Size:** Segment内のユーザー数のおおよその範囲
- **Tags:** Segmentに関連付けられたタグ
- **Teams:** Segmentに関連付けられたチーム
- **Advanced Tracking Segments Only:** [分析トラッキング]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/#segment-analytics-tracking)が有効になっているSegmentのみを表示します。

### 列 {#columns}

Segmentリストに表示するために選択できる情報の列は以下のとおりです。
- **Filters:** Segment内のフィルター数
- **Last edited:** Segmentが最後に編集された日付
- **Last edited by:** Segmentを最後に編集したユーザー
- **Tags:** Segmentに関連付けられたタグ
- **Teams:** Segmentに関連付けられたチーム
- **Estimated size:** Segment内の推定ユーザー数
- **Canvases:** Segmentを使用しているCanvasesの数
- **Campaigns:** Segmentを使用しているCampaignsの数

### スター付きのみ表示 {#show-starred-only}

**Show Starred Only**を選択すると、自分がスターを付けたSegmentのみにビューが絞り込まれます。

## Segmentのメッセージング使用状況の表示 {#messaging-use}

Segmentの**Messaging Use**セクションに移動すると、他のSegment、Campaigns、Canvases内など、そのSegmentがどこで使用されているかの概要を確認できます。

{% alert note %}
Segmentが相互に参照するループを防ぐため、**Segment Membership**フィルターを使用するSegmentは、他のSegmentから参照できません。詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)を参照してください。
{% endalert %}

## 特定のSegmentの管理 {#managing-specific-segments}

![「Edit」、「Duplicate」、「Archive」、「Add to starred」のオプションを表示するSegmentの編集メニュー。]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

特定のSegmentを管理するには、そのSegmentにカーソルを合わせ、行の末尾にあるメニューアイコンを選択して、以下のオプションを表示します。
- **Edit:** Segment内のフィルターを編集します。
- **Duplicate:** Segmentのコピーを作成します。
- **Archive:** Segmentをアーカイブします。これにより、そのSegmentを使用しているCampaignsやCanvasesもアーカイブされることに注意してください。
- **Add to starred:** Segmentにスターを付けます。これにより、Segmentsセクションの「Show Starred Only」ボックスをチェックして、すばやくアクセスできるようになります。

複数のSegment名の横にあるチェックボックスをオンにすることで、一括アーカイブや一括タグ付けなどの一括アクションを実行することもできます。

![複数のSegmentが選択され、「Tag As」ドロップダウンフィールドで「CRM」が選択されている状態。]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### 最終閲覧以降の変更 {#changes-since-last-viewed}

チームの他のメンバーによるSegmentの更新数は、Segment概要ページの*最終閲覧以降の変更*指標で追跡されます。**Changes Since Last Viewed**を選択すると、Segmentの名前、説明、ターゲットオーディエンスの更新に関する変更ログを表示できます。各更新について、誰がいつ更新を行ったかを確認できます。この変更ログを使用して、Segmentへの変更を監査できます。

## Segmentの検索 {#searching-for-segments}

検索フィールドにキーワードを入力して、Segment名を検索します。

このフィールドに入力されたすべてのキーワードと文字列が検索されます。たとえば、「test segment 1」を検索すると、名前に「test」、「segment」、または「1」が含まれるSegmentが返されます。完全一致の文字列を検索するには、検索キーワードを引用符で囲みます。["test segment 1"]を検索すると、名前に「test segment 1」という正確なフレーズが含まれるすべてのSegmentが返されます。

![検索フィールドに「all users」と入力した検索結果に「All Users (Test)」、「All Users」、「All Users 15」が表示されている。]({% image_buster /assets/img/segment/segments_search.png %})

### Canvases内のSegment {#segments-in-canvases}

他のSegment、Campaigns、またはCanvases内のものを含むすべてのSegment参照を検索するには、Segmentの[メッセージング使用状況](#messaging-use)セクションに移動します。**Canvas**ページの**Target segment**フィルターは、CanvasオーディエンスSegmentのみを検索します。

![Canvasページのターゲットセグメントフィルター。]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}