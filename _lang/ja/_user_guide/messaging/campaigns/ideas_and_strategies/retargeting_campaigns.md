---
nav_title: Campaignのリターゲティング
article_title: Campaignのリターゲティング
page_order: 2
page_type: reference
description: "このリファレンス記事では、ユーザーが受信したメッセージに基づいてCampaignをリターゲティングする方法とその理由について説明します。"
tool:
  - Campaigns

---

# Campaignのリターゲティング {#retarget-campaigns}

> メールを開封したかどうかなど、ユーザーの過去のアクションに基づいてCampaignをリターゲティングすることで、ユーザーを再分類し、効果的なデータドリブン型のマーケティングアプローチへの道を開くことができます。

Brazeは、ユーザーが受信したメッセージに基づいてリターゲティングする機能をサポートしています。CampaignsやCanvasesとのインタラクションに基づいてユーザーをリターゲティングできます。

これらのリターゲティングフィルターはそれぞれ、追加後にいくつかのオプションを提供します。ユーザーのターゲティングの詳細については、Campaignセットアップに関する[Brazeラーニングコース](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)をご覧ください。

![利用可能なフィルターのドロップダウンメニューが表示されたSegment詳細セクション。]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## リターゲティングフィルター {#retargeting-filters}

このセクションのリターゲティングフィルターを、CampaignsやCanvases内のユーザーに対して使用できます。

### Campaignをクリック/開封 {#clickedopened-campaign}

このフィルターを使用して、以下のアクションを行った、または行っていないユーザーを検索します:

- メールをクリックした
- アプリ内メッセージをクリックした
- プッシュ通知を直接開封した
- メールを開封した
- アプリ内メッセージを閲覧した

![チャネルインタラクションオプションが表示されたCampaignをクリック/開封フィルター。]({% image_buster /assets/img_archive/clickedopened.png %})

リターゲティングするCampaignを選択して、さらに絞り込むことができます。

### タグ付きのCampaignまたはCanvasをクリックまたは開封 {#clicked-or-opened-campaign-or-canvas-with-tag}

このフィルターを使用して、指定したタグを持つCampaignsまたはCanvasesとインタラクションした、またはしていないユーザーを検索します:

- メールをクリックした
- アプリ内メッセージをクリックした
- プッシュ通知を直接開封した
- メールを開封した
- アプリ内メッセージを閲覧した

![タグ付きのCampaignまたはCanvasをクリックまたは開封フィルター。]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Campaignからコンバージョン {#converted-from-campaign}

このフィルターを使用して、ターゲットCampaignでコンバージョンした（1次コンバージョンに基づく）、またはしていないユーザーを検索します。

定期Campaignsの場合、このフィルターはCampaignの最新メッセージでユーザーがコンバージョンしたかどうかを参照します。

![Campaign選択が表示されたCampaignからコンバージョンフィルター。]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Canvasからコンバージョン {#converted-from-canvas}

このフィルターを使用して、ターゲットCanvasでコンバージョンした（1次コンバージョンに基づく）、またはしていないユーザーを検索します。

定期Canvasesの場合、このフィルターはユーザーがCanvasを通過した際にこれまでにコンバージョンしたことがあるかどうかを参照します。

![Canvas選択が表示されたCanvasからコンバージョンフィルター。]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### Campaignのコントロールグループに所属 {#in-campaign-control-group}

このフィルターを使用して、ターゲットCampaignのコントロールグループに所属している、またはしていないユーザーを検索します。

![Campaign選択が表示されたCampaignのコントロールグループに所属フィルター。]({% image_buster /assets/img_archive/campaign_control_group.png %})

### Canvasのコントロールグループに所属 {#in-canvas-control-group}

このフィルターを使用して、ターゲットCanvasのコントロールグループに所属している、またはしていないユーザーを検索します。ターゲットCanvasはドロップダウンから選択できます。

![Canvas選択が表示されたCanvasのコントロールグループに所属フィルター。]({% image_buster /assets/img_archive/canvas_control_group.png %})

### 特定のCampaignからの最終受信メッセージ {#last-received-message-from-specific-campaign}

このフィルターを使用して、指定した日付または日数の前後に特定のCampaignを最後に受信したユーザーを検索します。このフィルターは、ユーザーが他のCampaignsを受信した時期は考慮しません。

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![日付オプションが表示された特定のCampaignからの最終受信メッセージフィルター。]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### タグ付きのCampaignまたはCanvasからの最終受信メッセージ {#last-received-message-from-campaign-or-canvas-with-tag}

このフィルターを使用して、指定した日付または日数の前後に、指定したタグを持つCampaignまたはCanvasを最後に受信したユーザーを検索します。このフィルターは、ユーザーが他のCampaignsやCanvasesを受信した時期は考慮しません。

![タグ付きのCampaignまたはCanvasからの最終受信メッセージフィルター。]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Campaignからメッセージを受信 {#received-message-from-campaign}

このフィルターを使用して、ターゲットCampaignを受信した、またはしていないユーザーを検索します。

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![Campaign選択が表示されたCampaignからメッセージを受信フィルター。]({% image_buster /assets/img_archive/receivedcamp.png %})

### タグ付きのCampaignまたはCanvasからメッセージを受信 {#received-message-from-campaign-or-canvas-with-tag}

このフィルターを使用して、ターゲットタグを持つCampaignまたはCanvasを受信した、またはしていないユーザーを検索します。

![タグ付きのCampaignまたはCanvasからメッセージを受信フィルター。]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Campaignのリターゲティングの利点 {#advantages-with-retargeting-campaigns}

リターゲティングは、元のSegmentにユーザーに取ってほしい特定のアクションが含まれている場合に特に効果的です。たとえば、購入したことがないユーザーをターゲットにしたカードがあるとします。そのカードでは、アプリ内購入の割引プロモーションを宣伝しています。初期Segmentは次のようになります:

- アプリ内の支出額がちょうど0
- 最終アプリ使用日が14日以内

Segment内のユーザー総数は100,000人で、コンテンツカードの統計から60,000人のユニークユーザーがカードを閲覧し、20,000人のユニークユーザーがカードをクリックしたことがわかっています。セグメンターを使用して、カードをクリックしたユーザーのうち実際に購入したユーザー数を確認できます:

- アプリ内の支出額が0より大きい
- クリックしたカードがカード名

これらの統計を確認した後、カードをクリックしたが購入しなかったユーザーのSegmentを作成できます:

- アプリ内の支出額がちょうど0
- クリックしたカードがカード名

このSegmentに対して、プロモーションや別のアプリ内購入に関する追加メッセージでリターゲティングできます。リターゲティングはメッセージングCampaignで実行できます。マルチチャネルアプローチにより、ユーザーが最も反応しやすい場所でリーチでき、Campaignsの効果を高めることができます。