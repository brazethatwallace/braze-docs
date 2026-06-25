---
nav_title: "アイドル状態のCampaignsとCanvases"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# アイドル状態のCampaignsとCanvases {#idle-campaigns-and-canvases}

> このリファレンス記事では、CampaignsとCanvasesのアイドルステータスについて説明し、よくある質問に回答します。

{% alert note %}
2024年より、Canvasesもキャンペーンと同様に**アイドル**としてマークされ、停止されるようになります。Canvasesがアイドルまたは停止された場合、このドキュメントに記載されたロジックに従います。
{% endalert %}

CampaignsとCanvasesは、一定期間メッセージを送信していない、またはユーザーがエントリーしていない場合にアイドルステータスが割り当てられます。これらのCampaignsとCanvasesは、関連する停止日に自動的に停止されます。アイドル状態のCampaignsとCanvasesをフィルタリングして、CampaignsとCanvasesのリストの並べ替えや管理に役立てることができます。

終了日が設定されているCampaignsとCanvases、および1回限りの送信は、自動停止の7日前にアイドル状態になります。11か月間メッセージを送信していないCampaignsとCanvasesは、自動停止の1か月前にアイドル状態になります。

## アイドル状態のCampaigns {#idle-campaigns}

以下の基準を満たすアイドル状態のCampaignsは、継続的に停止されます：

- スケジュールされた1回限りの送信で、送信日から7日が経過している
- 終了日が設定されたスケジュール配信またはアクションベースのCampaignで、終了日から7日が経過している
- 終了日が設定されておらず、1年間メッセージを送信していないCampaign

終了日が設定されていないCampaignsの場合、メッセージが送信されるか、Campaignが更新されると、停止までの1年間のカウントダウンがリセットされます。Campaignsが停止されると、Brazeはダッシュボードおよびメールで顧客に通知します。

Campaignsは、デフォルトの停止日と最後のコンバージョン期限の翌日のうち、遅い方の日付で停止されます。Winning VariantまたはPersonalized Variantの結果として行われる送信はスケジュール送信として扱われ、Winning VariantまたはPersonalized Variantが送信されてから7日後に停止されます。すべてのCampaignsは、毎日UTC午前4時にすべてのBrazeユーザーに対して停止されます。

Content Cardsは有効期限まで停止されず、前述の基準およびコンバージョン期限ルールにも従います。

アイドル状態のCampaignをアクティブに保つ方法については、以下の表を参照してください：

| アイドルステータスの理由                                                                              | Campaignをアクティブにする手順                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| スケジュールされた1回限りの送信で、送信日を過ぎているCampaigns                 | 将来の送信をスケジュールする                            |
| スケジュール配信またはアクションベースで、終了日が設定されており、終了日を過ぎているCampaigns | 終了日を延長する                               |
| 終了日が設定されておらず、1年間メッセージを送信していないCampaigns                                | メッセージを1件送信するか、Campaignに何らかの編集を行う |
| 終了日が設定されており、1回限りの送信のCampaigns | 将来の送信をスケジュールする |
| 11か月間メッセージを送信していないCampaigns | メッセージを1件送信するか、Campaignに何らかの編集を行う |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### アプリ内メッセージCampaigns {#in-app-message-campaigns}

アプリ内メッセージCampaignにインプレッションがなく、30日以上編集されていない場合、アイドル状態のCampaignになります。アイドル状態のアプリ内メッセージCampaignは設定に基づいて配信を継続しますが、アプリ内メッセージはテンプレート化されたアプリ内メッセージになります。

ユーザーがインプレッションイベントをトリガーするか、マーケターがCampaignを編集すると、Campaignはアクティブステータスに戻り、30日間のカウンターがリセットされます。

## アイドル状態のCanvases {#idle-canvases}

以下の基準を満たすアイドル状態のCanvasesは、継続的に停止されます：

- スケジュールされた1回限りの送信で、送信日と最大期間から7日以上経過している
- 終了日が設定されたスケジュール配信またはアクションベースのCanvasで、終了日と最大期間から7日以上経過している
- 終了日が設定されておらず、12か月以上ユーザーがエントリーしていない、または編集されていないCanvasで、最大期間を超えている

終了日が設定されていないCanvasesの場合、ユーザーがエントリーするか、Canvasが更新されると、停止までの1年間のカウントダウンがリセットされます。Canvasesが停止されると、Brazeはダッシュボードおよびメールで顧客に通知します。

Canvasの[最大期間]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)とは、ユーザーが特定のCanvasを完了するまでにかかる最長の時間です。この期間には、Content Cardsおよびアプリ内メッセージの有効期限が含まれます。

アイドル状態のCanvasをアクティブに保つ方法については、以下の表を参照してください：

| アイドルステータスの理由                                                                                                  | Canvasをアクティブにする手順                     |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| スケジュールされた1回限りの送信で、最大期間が送信日を過ぎているCanvases                 | 将来の送信をスケジュールする                          |
| スケジュール配信またはアクションベースで、終了日が設定されており、最大期間が終了日を過ぎているCanvases | 終了日を延長する                             |
| 終了日が設定されておらず、1年間メッセージを送信していないCanvases                                                      | メッセージを1件送信するか、Canvasに何らかの編集を行う |
| 終了日が設定されており、1回限りの送信のCanvases | 将来の送信をスケジュールする |
| 11か月間メッセージを送信していないCanvases | メッセージを1件送信するか、Canvasに何らかの編集を行う |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

インタラクションデータを復元するオプションが表示されない場合、以下の理由が考えられます：

- 復元またはその他のインタラクションデータ関連の操作が現在進行中である。
- このCanvasにインタラクションデータが存在しなかった。
- Canvasが2021年より前に作成された場合、以前のポリシーに基づいてデータが完全に削除されている可能性があります。

## よくある質問 {#frequently-asked-questions}

### これはどのCampaignsまたはCanvasesに適用されますか？ {#what-campaigns-or-canvases-does-this-apply-to}

これは、前述の基準をすでに満たしているCampaignsとCanvases、および今後基準を満たすCampaignsとCanvasesに適用されます。

### CampaignまたはCanvasがアイドル状態かどうかはどうすればわかりますか？ {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

アイドル状態のCampaignsとCanvasesは、CampaignおよびCanvasのリストページで**アイドル**カテゴリの下に表示されます。CampaignまたはCanvasが停止される日付は、リストの列として表示されます。

![「Campaigns」ページの「アイドル」フィルター。][1]{: style="max-width:60%;"}

### アイドル状態のCampaignまたはCanvasが更新された場合はどうなりますか？ {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

メッセージを送信していないCampaign、またはユーザーがエントリーしていないCanvasが更新された場合、カウントダウンがリセットされます。

### 1年間メッセージを送信していないCampaigns（または1年間ユーザーがエントリーしていないCanvases）で、将来の終了日が設定されている場合はどうなりますか？ {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

これらのCampaignsとCanvasesは、終了日から7日後のUTC午前4時に停止されます。

#### Campaignsの自動停止を防ぐことはできますか？ {#can-i-stop-campaigns-from-automatically-stopping}

いいえ。これは、必要なCampaignsのみをアクティブに保ち、ダッシュボードの煩雑さを軽減してパフォーマンスを向上させるためのものです。自動停止されたすべてのCampaignsのリストが必要な場合は、[サポートチケットを送信]({{site.baseurl}}/help/support/)してリストを提供してもらうことができます。

### 停止されたCampaignsとCanvasesに関するメール通知は誰が受け取りますか？ {#who-will-receive-email-notifications-about-stopped-campaigns-and-canvases}

デフォルトでは、管理者権限を持つすべてのユーザーが、CampaignsとCanvasesの自動停止に関するメール通知にオプトインされています。CampaignまたはCanvasの作成者は、停止された際に常に通知されます。ユーザーは、**会社の設定** > **通知設定**に移動し、**Campaign Automatically Stopped**通知および**Canvas Automatically Stopped**通知の受信者を追加または削除することで、メール通知設定を管理できます。

### Content Cardsの停止はどのように機能しますか？ {#how-does-stopping-content-cards-work}

CampaignsのContent Cardsは、有効期限と適切なバッファ期間が経過するまで停止されません。バッファ期間（Campaignが1回限りの送信か、終了日があるか、終了日がないかに対応）と有効期限のうち、遅い方の日付で停止されます。

たとえば、Content Cardsの有効期限が4月1日で、1回限りの送信であり、コンバージョン期限が10日間の場合、4月12日（コンバージョン期限から10日後、プラス1日）に停止されます。Content Cardsの有効期限が4月1日で、APIトリガーであり、3月15日以降メッセージを送信していない場合、翌年の3月15日に期限切れになります。

Canvasesは、Content Cardsが停止された後、つまり最大期間が経過した後にのみ停止されます。

### Canvasにフィーチャーフラグの実験があります。フィーチャーフラグが設定された後、Canvasはアクティブのままですか？ {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-will-the-canvas-remain-active}

フィーチャーフラグステップを含むCanvasesは自動的に停止されず、アイドル状態にもなりません。

### アクティブなCampaignsのみを表示するフィルターを適用したのに、Campaignsリストにアイドル状態のCampaignsが表示されるのはなぜですか？ {#why-am-i-seeing-idle-campaigns-displayed-in-my-campaigns-list-when-i-applied-a-filter-to-show-active-campaigns-only}

アイドル状態のCampaignsは、停止されるまではアクティブとみなされます。

### Campaignがまだプッシュ通知を送信しているのに、アイドルとして表示されることはありますか？ {#would-a-campaign-be-listed-as-idle-when-its-still-sending-push-notifications}

いいえ。Campaignは、メッセージのアクティブな送信を行っていない場合にのみアイドルとして表示されます。

[1]: {% image_buster /assets/unlisted_docs/img/idle_filter.png %}